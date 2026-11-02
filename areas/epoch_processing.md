# epoch_processing

62 checked ideas, 3 actionable. [Back to the summary](../README.md).

## Actionable (3)

High or medium value, verdict `not` or `partial`.

<a id="epoch_processing-093"></a>
<details>
<summary><b>epoch_processing-093</b> Parallelize per-validator epoch loops across cores — <i>not · medium · L · cpu, latency</i></summary>

**Idea.** Run independent per-validator epoch work (validator status building, inactivity scores, rewards/penalties, registry updates, total active balance) across worker threads, since each validator's entry is independent.

**Gap in Lighthouse.** No per-validator epoch work runs across threads. Lighthouse removes some loops by other means (progressive balances cache replaces the total active balance and flag balance sums; the single pass fuses the rest), but the remaining fused loop is serial. Would need chunked parallel passes for the independent parts (inactivity scores, reward deltas, effective balance checks) with registry updates kept serial; milhouse iter_cow would need chunked readers.

**Impact.** Epoch transition might drop 20-40 percent with enough cores; runs once per epoch and gates the first block of the epoch.

**Best measured result.** inactivity scores p50 6.09 -&gt; 0.92 ms; rewards 38.19 -&gt; 30.45 ms; ProcessEpoch 153.98 -&gt; 143.02 ms; epoch-first OnBlock 280.92 -&gt; 265.63 ms (pr:caplin#23966)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:155-340`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L155-L340) process_epoch_single_pass: one serial loop for inactivity, rewards, registry, slashings, pending deposits, effective balances
- [`consensus/state_processing/src/common/update_progressive_balances_cache.rs:16`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/update_progressive_balances_cache.rs#L16) total and per-flag balances kept incrementally, no per-epoch loop (alternative, not parallelism)
- [`consensus/state_processing/src/epoch_cache.rs:141`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/epoch_cache.rs#L141) base rewards and activation queue precomputed in cache (serial)
- [`consensus/state_processing/src/per_block_processing/verify_deposit.rs:109`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/verify_deposit.rs#L109) rayon used only in block processing

**Second check.** Searched consensus/, beacon_chain and milhouse for rayon, par_iter, thread::scope and spawn; only block-processing and tree hashing are parallel. The progressive balances cache and epoch cache are serial alternatives that remove work, not parallel execution, so the verdict stays not.

**Sources.** [caplin#23966](https://github.com/erigontech/erigon/pull/23966), [caplin#12191](https://github.com/erigontech/erigon/pull/12191), [caplin#12291](https://github.com/erigontech/erigon/pull/12291), [caplin#12277](https://github.com/erigontech/erigon/pull/12277), [teku#5826](https://github.com/Consensys-Incorporated/teku/pull/5826)

</details>

<a id="epoch_processing-017"></a>
<details>
<summary><b>epoch_processing-017</b> Cache reward deltas per effective balance value — <i>partial · medium · S · cpu</i></summary>

**Idea.** Effective balance takes at most 32 distinct values, so compute reward/penalty deltas once per (effective balance, status) and look them up per validator, computing all flag deltas in one pass over statuses.

**Gap in Lighthouse.** Base reward is already cached per effective balance and all flags are handled in a single pass, but the final per-flag reward/penalty values are still recomputed per validator; a table keyed by (EB increment, participation flags) built in RewardsAndPenaltiesContext::new would remove the 3x mul/div per validator. Inactivity penalty depends on per-validator inactivity score and cannot be fully tabled.

**Impact.** Small: a handful of u64 mul/div per validator per epoch (~1M validators), a few ms at most; Lodestar's &gt;10x gain came largely from what Lighthouse already does (per-EB base reward, single pass).

**Best measured result.** "&gt;10x improvement as in the benchmark diff" (pr:lodestar#2833)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/epoch_cache.rs:104-114`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/epoch_cache.rs#L104-L114) base_rewards precomputed once per effective-balance increment (0..=max EB)
- [`consensus/types/src/state/epoch_cache.rs:34-37`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/epoch_cache.rs#L34-L37) base_rewards keyed by effective_balance / effective_balance_increment
- [`consensus/types/src/state/epoch_cache.rs:130-145`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/epoch_cache.rs#L130-L145) get_base_reward is a table lookup
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:268`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L268) per-validator base_reward via cache lookup
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:667-701`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L667-L701) all flag deltas plus inactivity penalty computed in one pass per validator
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:706-733`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L706-L733) get_flag_index_delta still does mul/div per validator per flag

**Sources.** [lodestar#2833](https://github.com/ChainSafe/lodestar/pull/2833)

</details>

<a id="epoch_processing-061"></a>
<details>
<summary><b>epoch_processing-061</b> Parallel reward deltas, serial apply, skip no-op writes — <i>partial · medium · M · cpu</i></summary>

**Idea.** Compute reward/penalty deltas in parallel into a plain slice and apply them to the balances tree serially to avoid contended dirty marks, and skip effective-balance writes when the value is unchanged so fewer leaves are rehashed.

**Gap in Lighthouse.** The skip-no-op-write part exists (Cow writes only when the value changes). Reward and penalty deltas are still computed serially inside the fused single pass. To get the parallel part, compute get_flag_index_delta and get_inactivity_penalty_delta in a rayon pass into a Vec&lt;Delta&gt; (inputs are read-only: epoch_cache base rewards, participation, inactivity scores after update), then apply them serially.

**Impact.** Rewards portion of the epoch transition could shrink several times with multiple cores; the skip-no-op-write saving is already in place.

**Best measured result.** Fulu rewards ~115 -&gt; 17 ms, post-epoch hash ~101 -&gt; 20 ms (pr:caplin#25144)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:237-340`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L237-L340) serial izip loop over validators with iter_cow; deltas computed and applied inline
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:679-700`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L679-L700) Delta computed per validator, balance make_mut only when rewards or penalties nonzero
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:1405`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L1405) effective balance written only if changed
- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/milhouse-0.9.0/src/tree.rs:530 only rayon use in milhouse is parallel tree_hash, not delta computation

**Second check.** Grepped all of consensus/ and beacon_chain for rayon/par_iter/thread spawn: only per_block_processing (deposits, signature sets) and milhouse tree hashing use it. No parallel delta computation under any name.

**Sources.** [caplin#25144](https://github.com/erigontech/erigon/pull/25144)

</details>

## Other checked ideas (59)

Implemented, not applicable, or low value.

<a id="epoch_processing-012"></a>
<details>
<summary><b>epoch_processing-012</b> Fast exact integer square root — <i>not · low · S · cpu</i></summary>

**Idea.** Implement integer square root with float sqrt below 2^52 (exact there) and a fast exact algorithm above it, since isqrt of total active balance is on the rewards hot path.

**Gap in Lighthouse.** Replace integer_sqrt on u64 with an f64-sqrt fast path with correction step; callers are SqrtTotalActiveBalance::new and get_base_reward_per_increment.

**Impact.** Sqrt runs about once per epoch plus once per block; saves under 100ns each, effectively nothing.

**Best measured result.** Below 52 bits 29.7 ns/op, above 52 bits 83.9 ns/op, with datatable 16.6 ns/op and 0 allocs (pr:prysm#8910)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/common/base.rs:12`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/base.rs#L12) and common/altair.rs:47 use integer_sqrt crate 0.1.5 generic PrimInt bitwise loop
- ~/.cargo/registry integer-sqrt-0.1.5/src/lib.rs generic digit-by-digit algorithm

**Sources.** [prysm#8910](https://github.com/OffchainLabs/prysm/pull/8910)

</details>

<a id="epoch_processing-021"></a>
<details>
<summary><b>epoch_processing-021</b> Reuse one hash output for multiple random draws — <i>not · low · S · cpu</i></summary>

**Idea.** In compute_shuffled_index-based sampling (sync committee, PTC, proposer selection) compute hash(seed \|\| i/16) once per 16 iterations and reuse its 32 bytes, also caching pivot/source hashes, instead of hashing per candidate.

**Gap in Lighthouse.** Cache the 90 pivot hashes once per seed and the per-position source hash across candidates in compute_shuffled_index (or add a batched variant); cache the random-byte hash across 32 consecutive i in shuffling_random_byte/u16 and in compute_balance_weighted_selection.

**Impact.** Sync committee computation (once per 256 epochs) and proposer selection (per epoch under Fulu lookahead) get cheaper; each candidate currently costs ~180 SHA-256 plus one for the random byte. Likely tens of ms down to a few ms per call, small on a mainnet node.

**Best measured result.** naive computeShuffledIndex 15.06 s/op vs cached 517 ms/op (100k validators); getNextSyncCommitteeIndices ~4.7 s vs ~4.6 ms (pr:lodestar#7456)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/swap_or_not_shuffle/src/compute_shuffled_index.rs:21`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/swap_or_not_shuffle/src/compute_shuffled_index.rs#L21) - recomputes pivot hash every round and a source hash per call, no cache
- [`consensus/types/src/state/beacon_state.rs:1479`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1479) - shuffling_random_byte hashes seed\|\|i/32 per candidate, allocates preimage
- [`consensus/types/src/state/beacon_state.rs:1770`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1770) - get_next_sync_committee_indices calls compute_shuffled_index per candidate
- [`consensus/types/src/state/beacon_state.rs:3704`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3704) - Gloas compute_balance_weighted_selection same pattern

**Sources.** [lodestar#7456](https://github.com/ChainSafe/lodestar/pull/7456), [prysm#16708](https://github.com/OffchainLabs/prysm/pull/16708)

</details>

<a id="epoch_processing-079"></a>
<details>
<summary><b>epoch_processing-079</b> Sync committee sampling from one list shuffle — <i>not · low · S · cpu, latency</i></summary>

**Idea.** Select Electra+ sync committee members by walking a single list-shuffle of active indices with the same acceptance rule, instead of a 90-round compute_shuffled_index per candidate, and read pubkeys from the pubkey cache.

**Gap in Lighthouse.** In get_next_sync_committee_indices, replace the per-candidate compute_shuffled_index (90 rounds each) with one shuffle_list(active_indices, forwards) and walk the result with the same acceptance rule; read pubkeys via get_next_sync_committee.

**Impact.** Sync committee rotation (once per 256 epochs, in epoch processing) would drop from roughly 90-150 ms to ~25 ms; negligible averaged over time but trims a periodic epoch-boundary spike.

**Best measured result.** sync_committee_rotation 137-160 ms to 25.0 ms (apple_m1); mainnet 91.9 to 21.1 ms (commit:lodestar@78da4e7b9512)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:1770`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1770) get_next_sync_committee_indices calls compute_shuffled_index per candidate (line ~1798)
- [`consensus/swap_or_not_shuffle/src/shuffle_list.rs:92`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/swap_or_not_shuffle/src/shuffle_list.rs#L92) shuffle_list exists but unused here
- beacon_state.rs:1830 pubkeys read from validators().get, not pubkey_cache

**Sources.** [lodestar@78da4e7b9](https://github.com/ChainSafe/lodestar/commit/78da4e7b9512)

</details>

<a id="epoch_processing-085"></a>
<details>
<summary><b>epoch_processing-085</b> Shuffle u32 indices instead of u64 — <i>not · low · M · memory, cpu</i></summary>

**Idea.** Store active/shuffled validator indices as u32 (or shuffle u32 positions and gather) so the swap-or-not kernel moves half the data and the shuffling cache retains half the memory.

**Gap in Lighthouse.** Change shuffle_list and CommitteeCache.shuffling/active_validator_indices to u32 (or gather via u32 positions), adjusting get_active_validator_indices and callers returning &amp;[usize].

**Impact.** Shuffling list memory per cached epoch halves (8 MB to 4 MB per 1M validators, times up to a few cached shufflings) and the shuffle kernel gets ~15-20% faster; saves tens of ms per epoch transition.

**Best measured result.** EpochShuffling.init: 1M validators 56.67 to 45.89 ms (-19%), retained 16.03 to 8.03 MB; 2M validators 123.52 to 94.21 ms (-23.7%) (commit:lodestar@c17d13285875)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/committee_cache.rs:29`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L29) shuffling: Vec&lt;usize&gt;
- [`consensus/swap_or_not_shuffle/src/shuffle_list.rs:92`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/swap_or_not_shuffle/src/shuffle_list.rs#L92) shuffle_list takes Vec&lt;usize&gt;, masked_swap on usize (line 54)
- committee_cache.rs:~150 shuffling_positions uses 4-byte NonZeroUsizeOption already

**Sources.** [lodestar@ea963b101](https://github.com/ChainSafe/lodestar/commit/ea963b101ca5), [lodestar@c17d13285](https://github.com/ChainSafe/lodestar/commit/c17d13285875)

</details>

<a id="epoch_processing-086"></a>
<details>
<summary><b>epoch_processing-086</b> SIMD-vectorized swap-or-not shuffle — <i>not · low · M · cpu, latency</i></summary>

**Idea.** Vectorize the list shuffle's swap loop to process several pairs per step with a vector select driven by one source byte of decision bits, instead of one pair per iteration.

**Gap in Lighthouse.** Rewrite the inner loops of shuffle_list to process 8 or more pairs per step with SIMD selects driven by one source byte; needs u32 lanes (see 085) to be worthwhile.

**Impact.** Shuffle of ~1M validators per epoch (committee cache for Next epoch, plus Gloas lookahead) could drop 2-3x in the kernel, roughly 30-50 ms per epoch on the state-advance path, off the block-import critical path.

**Best measured result.** epoch_total 149-153 ms to 100-102 ms; kernel 1M u32 74-111 ms to 25 ms (M5) (commit:lodestar@40194cba93f7)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/swap_or_not_shuffle/src/shuffle_list.rs:92`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/swap_or_not_shuffle/src/shuffle_list.rs#L92) scalar loop, one pair per iteration with masked_swap (branchless, scalar)
- no std::simd or intrinsics in [`consensus/swap_or_not_shuffle/src`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/swap_or_not_shuffle/src)

**Sources.** [lodestar@40194cba9](https://github.com/ChainSafe/lodestar/commit/40194cba93f7)

</details>

<a id="epoch_processing-091"></a>
<details>
<summary><b>epoch_processing-091</b> Compute next epoch active indices in existing loop — <i>not · low · M · cpu</i></summary>

**Idea.** Collect the next epoch's active validator indices during an existing per-validator loop at the end of the previous epoch, instead of a separate full pass when rotating epoch caches.

**Gap in Lighthouse.** Collect next-epoch active indices inside the single_pass validator loop (PreEpochCache) and hand them to the next-epoch CommitteeCache build, replacing get_active_validator_indices in CommitteeCache::initialized_unchecked.

**Impact.** Saves one linear pass over ~1M validators per epoch (a few ms of a multi-hundred-ms transition); negligible on a mainnet node.

**Best measured result.** On an altair syncing node, getting active indices on rotateEpoch took 3.5% of time (pr:lodestar#2871)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/committee_cache.rs:135`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L135) initialized_unchecked calls get_active_validator_indices, a separate full pass over validators
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:189`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L189) PreEpochCache only tracks effective balances/total active balance in the loop, not indices

**Sources.** [lodestar#2871](https://github.com/ChainSafe/lodestar/pull/2871)

</details>

<a id="epoch_processing-003"></a>
<details>
<summary><b>epoch_processing-003</b> Flat array copy of validator fields for epoch loops — <i>partial · low · M · cpu</i></summary>

**Idea.** Copy the validator fields epoch processing reads (effective balance, slashed, activation/exit epochs) into a flat struct array once per transition, and iterate that instead of the tree-backed validator list. Fetch the full validator only when it must be modified.

**Gap in Lighthouse.** The single-pass loop does not copy validator fields into a flat struct array; it walks the tree sequentially with iter_cow (no per-index descent, but full Validator leaves are touched). A flat array built once in initialize_epoch_cache could feed process_epoch_single_pass.

**Impact.** Minor cache-locality gain in the per-validator loop at ~1M validators; teku's own measurement was a regression, so expect little.

**Best measured result.** epochTransition 2.836 -&gt; 3.157 ops/s at 400k validators (pr:teku#5833)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:243-262`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L243-L262) main loop reads validators via milhouse iter_cow, not a flat array
- [`consensus/types/src/state/epoch_cache.rs:33`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/epoch_cache.rs#L33) flat effective_balances Vec exists but is not the loop source

**Sources.** [lodestar@188555b33](https://github.com/ChainSafe/lodestar/commit/188555b33c24), [teku#5833](https://github.com/Consensys-Incorporated/teku/pull/5833), [lodestar#3049](https://github.com/ChainSafe/lodestar/pull/3049)

</details>

<a id="epoch_processing-011"></a>
<details>
<summary><b>epoch_processing-011</b> Memoize integer sqrt / base reward per increment — <i>partial · low · S · cpu</i></summary>

**Idea.** Cache the integer square root of total active balance (and the derived base reward per increment) in state/transition caches keyed by its input, so block and epoch processing reuse it across calls; on a miss, Newton iteration can start from the cached value.

**Gap in Lighthouse.** Store base_reward_per_increment (or the sqrt) in EpochCache and have compute_sync_aggregate_rewards read it instead of calling BaseRewardPerIncrement::new.

**Impact.** One u64 sqrt per block saved, tens of ns; negligible on a mainnet node. Epoch-level reuse already exists.

**Best measured result.** Above-52-bit sqrt about 2.3x faster; ~55ns old vs ~28-46ns new per op (pr:prysm#12191)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/epoch_cache.rs:96`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/epoch_cache.rs#L96) base_reward_per_increment/sqrt computed once per epoch in into_epoch_cache and baked into base_rewards table
- [`consensus/state_processing/src/per_block_processing/altair/sync_committee.rs:93`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/altair/sync_committee.rs#L93) compute_sync_aggregate_rewards recomputes BaseRewardPerIncrement::new (a sqrt) every block
- [`consensus/state_processing/src/common/altair.rs:41`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/altair.rs#L41) get_base_reward_per_increment

**Sources.** [prysm#11484](https://github.com/OffchainLabs/prysm/pull/11484), [prysm#12191](https://github.com/OffchainLabs/prysm/pull/12191), [teku#4815](https://github.com/Consensys-Incorporated/teku/pull/4815)

</details>

<a id="epoch_processing-059"></a>
<details>
<summary><b>epoch_processing-059</b> Preallocated reusable buffers, no per-validator allocations — <i>partial · low · S · cpu, memory</i></summary>

**Idea.** Hoist allocations out of per-validator epoch loops and keep validator-count-sized arrays (statuses, active indices, balances, inactivity scores, reward buffers) preallocated and reused across epoch transitions and replays, using iterators instead of copying participation arrays or validators. This avoids per-epoch allocation and memory spikes.

**Gap in Lighthouse.** Lighthouse uses iterators and structural-sharing clones, so no participation or validator copies. But PreEpochCache::new_for_next_epoch still allocates a fresh validator-count Vec every epoch, and the deposit context allocates HashMap/Vec. Reusing a buffer would mean recycling the old EpochCache Vec (Arc::try_unwrap) in PreEpochCache::new_for_next_epoch.

**Impact.** Saves one ~8 MB allocation (1M validators) per epoch plus a few small ones; negligible vs. the tree work, mainly less allocator churn.

**Best measured result.** epoch slot processing avg 2438 ms -&gt; 1156 ms (220k validators) (pr:nimbus#2811)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/epoch_cache.rs:38`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/epoch_cache.rs#L38) effective_balances Vec allocated each epoch (N*8 bytes)
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:1104`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L1104) PendingDepositsContext allocates HashMap/Vecs per epoch
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:225`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L225) ParticipationEpochSummary uses to_owned_list (O(1) milhouse clone, not a copy)
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:165`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L165) caches initialized only when invalid

**Sources.** [nimbus#2811](https://github.com/status-im/nimbus-eth2/pull/2811), [prysm#14439](https://github.com/OffchainLabs/prysm/pull/14439), [nimbus#2539](https://github.com/status-im/nimbus-eth2/pull/2539), [lodestar#6979](https://github.com/ChainSafe/lodestar/pull/6979), [lodestar#10523](https://github.com/ChainSafe/lodestar/pull/10523), [lodestar#6945](https://github.com/ChainSafe/lodestar/pull/6945)

</details>

<a id="epoch_processing-062"></a>
<details>
<summary><b>epoch_processing-062</b> Diff-synced flat validator cache across epochs — <i>partial · low · M · cpu</i></summary>

**Idea.** Keep a persistent flat index-addressed copy of the validator fields and bring it forward by diffing the last synced tree root against the current one, so the epoch-start validator pass is a linear scan that does not degrade as tree nodes scatter.

**Gap in Lighthouse.** Lighthouse carries a flat effective_balances array (EpochCache) forward, built during the single pass, so there is no separate epoch-start flat rebuild in steady state. But the main pass still walks the validator tree with iter_cow, and the cold rebuild (restart, reorg, loaded state) is a full tree scan. A diff-based sync (milhouse diff between last synced and current root) could feed initialize_epoch_cache.

**Impact.** Only helps cold epoch-cache rebuilds and the tree walk; roughly tens of ms per epoch at 1.5M validators at best.

**Best measured result.** Hoodi 1.59M validators: epoch-start init 29.2 ms to 15.7 ms at epoch 0 and 48.9 ms to 14.1 ms at epoch 900; flat stays about 14-15 ms (commit:lodestar@d7282c7a751d)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/epoch_cache.rs:141`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/epoch_cache.rs#L141) initialize_epoch_cache returns early when cache valid
- [`consensus/state_processing/src/epoch_cache.rs:165`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/epoch_cache.rs#L165) cold path iterates whole validator tree
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:486`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L486) next epoch cache produced as by-product of the single pass

**Sources.** [lodestar@d7282c7a7](https://github.com/ChainSafe/lodestar/commit/d7282c7a751d)

</details>

<a id="epoch_processing-065"></a>
<details>
<summary><b>epoch_processing-065</b> Lazily iterate pending deposits/consolidations with early stop — <i>partial · low · S · cpu, memory</i></summary>

**Idea.** In process_pending_deposits and process_pending_consolidations, walk the state list lazily (batched or via an iterator) and stop as soon as the per-epoch churn limit or first unprocessable entry is reached, instead of materializing the whole list. Cost scales with the processed prefix, not the queue length.

**Gap in Lighthouse.** Deposit scan stops early, but the tail is re-collected and the list rebuilt every epoch (O(queue length)); use pop_front(next_deposit_index) and push postponed ones instead, in single_pass.rs near line 381. get_validators_in_consolidations should only cover the processable prefix, or be computed lazily.

**Impact.** Cost drops from O(queue) to O(processed prefix) per epoch; only matters when the deposit queue is large (hundreds of thousands of entries), then it is meaningful (tens of ms to hundreds of ms and tree rebuild).

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:1121`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L1121) deposit loop breaks on churn/finalized-slot/max-per-epoch limit
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:384`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L384) iter_from(next_deposit_index).collect() then set_pending_deposits_from_iter rebuilds the whole remaining list
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:1239`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L1239) get_validators_in_consolidations scans the entire pending_consolidations list every epoch
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:1295`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L1295) pop_front is used for consolidations

**Sources.** [lodestar#7566](https://github.com/ChainSafe/lodestar/pull/7566), [lodestar#7584](https://github.com/ChainSafe/lodestar/pull/7584), [lodestar#7597](https://github.com/ChainSafe/lodestar/pull/7597)

</details>

<a id="epoch_processing-083"></a>
<details>
<summary><b>epoch_processing-083</b> Incremental PTC window: reuse retained subtrees — <i>partial · low · S · cpu, latency</i></summary>

**Idea.** When updating the payload timeliness committee window at the epoch boundary, sample only the new epoch and reuse the retained window subtrees and their cached hashes instead of rebuilding the whole window.

**Gap in Lighthouse.** Window is already incremental (pop_front + push 32 entries). Remaining cost is that the new epoch computation (compute_ptc_with_cache) is not memoized; the Gloas fork-time initialize_ptc_window (upgrade/gloas.rs:191) rebuilds all. Lodestar's gain was for hashing the accumulator vectors; Lighthouse's tree_hash caches should reuse subtrees already.

**Impact.** Mostly already achieved; small remaining win on the Gloas upgrade slot only.

**Best measured result.** Gloas/Heze historical accumulator vectors ~7 s locally (pr:lodestar#9903)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:539`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L539) process_ptc_window pops front with milhouse List and pushes only the new epoch
- single_pass.rs:546 retained subtrees reused

**Sources.** [lodestar#9903](https://github.com/ChainSafe/lodestar/pull/9903)

</details>

<a id="epoch_processing-087"></a>
<details>
<summary><b>epoch_processing-087</b> Share one shuffling across all PTC slot computations — <i>partial · low · S · cpu, latency</i></summary>

**Idea.** When computing the payload timeliness committee for all 32 slots of an epoch, compute the shuffling and per-epoch inputs once and share them, and read effective_balance directly instead of materializing validators in weighted selection.

**Gap in Lighthouse.** Shuffling is already computed once and shared across the 32 slots. Missing: effective balance read through the milhouse validator tree (get_effective_balance) per candidate instead of an epoch-cache/balances array; use the EpochCache effective balances in compute_balance_weighted_acceptance.

**Impact.** Shaves the weighted-selection part of the Gloas PTC computation (512 members x 32 slots, several candidates each); likely tens of ms per epoch transition.

**Best measured result.** gloas epoch processing ~6.6s down to ~800ms, then ~660ms with effective_balance accessor (commit:grandine@57b197afa7e2)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:566`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L566) compute_ptc_with_cache for each slot reuses one committee_cache built at line 563
- [`consensus/types/src/state/beacon_state.rs:3752`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3752) compute_balance_weighted_acceptance reads effective_balance via get_validator tree lookup
- beacon_state.rs:3749 TODO notes epoch cache not used

**Sources.** [grandine#957](https://github.com/grandinetech/grandine/pull/957), [grandine@57b197afa](https://github.com/grandinetech/grandine/commit/57b197afa7e2)

</details>

<a id="epoch_processing-088"></a>
<details>
<summary><b>epoch_processing-088</b> Reuse shuffling cache for proposer lookahead/PTC window — <i>partial · low · M · cpu, latency</i></summary>

**Idea.** Make the next-epoch shuffling needed during epoch processing (proposer lookahead, PTC window) come from and go into the shuffling cache, keyed by a decision root that also works for the current state, so it is computed once rather than per fresh state copy or after the transition.

**Gap in Lighthouse.** Result is reused after the transition, but process_epoch (in state_processing) never consults ShufflingCache, so each fresh state copy (e.g. block import on a non-advanced state, reorg, replay) recomputes the lookahead shuffling. Would need a cache lookup hook passed into process_epoch, keyed by a decision root valid for the current state.

**Impact.** Avoids ~100 ms shuffle recompute on Gloas epoch transitions for states not pre-advanced; common path (state advance timer) already reuses the result.

**Best measured result.** ProcessPtcWindow on fresh copy 110-137 ms -&gt; 14-25 ms (500k validators) (pr:caplin#25143)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:563`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L563) builds lookahead CommitteeCache fresh in process_ptc_window
- altair.rs:85 installs it as the Next committee cache, so it is not recomputed after the transition
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:409`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L409) inserts it into shuffling_cache
- single_pass.rs:517 process_proposer_lookahead uses get_beacon_proposer_indices with no shuffling at all

**Sources.** [lodestar#7988](https://github.com/ChainSafe/lodestar/pull/7988), [grandine@362e28d7a](https://github.com/grandinetech/grandine/commit/362e28d7a8d0), [caplin#25143](https://github.com/erigontech/erigon/pull/25143)

</details>

<a id="epoch_processing-038"></a>
<details>
<summary><b>epoch_processing-038</b> Precompute next epoch transition and caches before the boundary — <i>implemented · high · S · latency, cpu</i></summary>

**Idea.** Late in the last slot of an epoch (or during idle time before it), advance a copy of the head state through the epoch transition off the critical path and locks, building committee caches and total attester balances, and cache the result. The first block of the new epoch and duty queries then find the post-epoch state and caches ready instead of stalling on them.

**Gap in Lighthouse.** 

**Impact.** Already done: first block of the new epoch and duty queries find advanced state and shuffling ready.

**Best measured result.** epoch transition 467 ms p50 under lock (target removed); head 0.3-0.5 s later than peers (pr:caplin#25473)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:109`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L109) timer fires 3/4 into each slot (9s)
- state_advance_timer.rs:291 per_slot_processing on a copy of head state runs the epoch transition off the import path
- state_advance_timer.rs:335-339 builds Current and Next committee caches
- state_advance_timer.rs:409 inserts Next shuffling into shuffling_cache

**Sources.** [teku#3698](https://github.com/Consensys-Incorporated/teku/pull/3698), [caplin#25473](https://github.com/erigontech/erigon/pull/25473), [lodestar#3383](https://github.com/ChainSafe/lodestar/pull/3383), [teku#3399](https://github.com/Consensys-Incorporated/teku/pull/3399)

</details>

<a id="epoch_processing-004"></a>
<details>
<summary><b>epoch_processing-004</b> Flat balances array shared across epoch steps — <i>implemented · medium · S · cpu</i></summary>

**Idea.** Extract balances once into a flat array in the epoch-processing context, apply rewards, penalties, deposits, consolidations and effective-balance reads on it with plain arithmetic, and write it back to the tree once at the end. Later steps read the array instead of re-reading or writing balances through the state tree per element.

**Gap in Lighthouse.** Equivalent effect, not a literal flat array: balances are read once through a cow iterator and written back in place. Only consolidations (single_pass.rs:1253) re-read the tree by index, for few validators.

**Impact.** Negligible further gain; per-element tree reads are already amortised by the single pass.

**Best measured result.** saves 165ms with &gt;110000 validators (pr:lodestar#1805)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:155`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L155) process_epoch_single_pass fuses inactivity, rewards, registry, slashings, deposits, effective balance in one loop
- single_pass.rs:244 balances.iter_cow() walked once; single_pass.rs:1210 deposits applied in same pass

**Sources.** [lodestar#2150](https://github.com/ChainSafe/lodestar/pull/2150), [lodestar#2347](https://github.com/ChainSafe/lodestar/pull/2347), [lodestar#7018](https://github.com/ChainSafe/lodestar/pull/7018), [lodestar@5bf23dc4a](https://github.com/ChainSafe/lodestar/commit/5bf23dc4a664), [lodestar#1805](https://github.com/ChainSafe/lodestar/pull/1805), [lodestar@f4116f4a1](https://github.com/ChainSafe/lodestar/commit/f4116f4a1f41)

</details>

<a id="epoch_processing-006"></a>
<details>
<summary><b>epoch_processing-006</b> Write validators, balances and scores only when values change — <i>implemented · medium · S · cpu, memory, latency</i></summary>

**Idea.** In epoch processing (effective-balance updates, balances, registry, inactivity), read validators read-only and take a mutable reference, copy, or dirty mark only when the value actually changes, skipping validators that cannot cross the hysteresis threshold. Unchanged entries stay shared with the parent state and are not rehashed.

**Gap in Lighthouse.** 

**Impact.** Already done (lighthouse#4573); unchanged entries stay shared with parent state.

**Best measured result.** Epoch transition reduced from 5.4s to ~650ms on mainnet (pr:lodestar#2902)

**Evidence (Lighthouse @ 928b61e719).**

- single_pass.rs:244-248 iter_cow over validators, balances, inactivity scores
- single_pass.rs:652 inactivity score make_mut only when value changes
- single_pass.rs:688 balance make_mut only if delta non-zero
- single_pass.rs:1388-1402 effective balance make_mut only when new != old (hysteresis)

**Sources.** [prysm#7599](https://github.com/OffchainLabs/prysm/pull/7599), [prysm#8743](https://github.com/OffchainLabs/prysm/pull/8743), [lighthouse#4573](https://github.com/sigp/lighthouse/pull/4573), [prysm#9225](https://github.com/OffchainLabs/prysm/pull/9225), [prysm#14124](https://github.com/OffchainLabs/prysm/pull/14124), [silver#146](https://github.com/gattaca-com/silver/pull/146), [prysm#8844](https://github.com/OffchainLabs/prysm/pull/8844), [prysm#16631](https://github.com/OffchainLabs/prysm/pull/16631), [lodestar#2902](https://github.com/ChainSafe/lodestar/pull/2902), [nimbus#3089](https://github.com/status-im/nimbus-eth2/pull/3089), [teku#4256](https://github.com/Consensys-Incorporated/teku/pull/4256), [lodestar#7043](https://github.com/ChainSafe/lodestar/pull/7043)

</details>

<a id="epoch_processing-019"></a>
<details>
<summary><b>epoch_processing-019</b> Compute next-epoch shuffling asynchronously — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Compute the next epoch's committee shuffling off the epoch-transition critical path (in a background task) and store it in a shared shuffling cache keyed by epoch and decision root. The transition no longer spends about 1 s computing it inline.

**Gap in Lighthouse.** Block-import fallback still builds inline if the timer did not run (e.g. beacon_chain.rs:5224).

**Impact.** Already done; the roughly 0.3-1 s shuffle is off the import critical path in the normal case.

**Best measured result.** about 1 second of epoch transition spent on nextShuffling moved off critical path (pr:lodestar#6938)

**Evidence (Lighthouse @ 928b61e719).**

- state_advance_timer.rs:335-339 build_committee_cache(Next) runs in the state advance task, not in block import
- state_advance_timer.rs:409 result stored in shuffling_cache keyed by AttestationShufflingId (epoch + decision root)
- [`consensus/types/src/state/beacon_state.rs:2887`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2887) advance_caches only rotates caches during the transition

**Sources.** [lodestar#6521](https://github.com/ChainSafe/lodestar/pull/6521), [lodestar#6938](https://github.com/ChainSafe/lodestar/pull/6938)

</details>

<a id="epoch_processing-022"></a>
<details>
<summary><b>epoch_processing-022</b> Branchless swaps in swap-or-not shuffle — <i>implemented · medium · S · cpu</i></summary>

**Idea.** Use masked XOR swaps instead of data-dependent branches in the swap-or-not list shuffle, since the swap bit is random and branch mispredictions dominate.

**Gap in Lighthouse.** 

**Impact.** Already done (lighthouse#9630); committee cache build about 358 ms -&gt; 240 ms.

**Best measured result.** reverse shuffle 1M elements 210.7 ms -&gt; 82.6 ms; mainnet committee_cache_build 358 ms -&gt; 240 ms (pr:lighthouse#9630)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/swap_or_not_shuffle/src/shuffle_list.rs:54`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/swap_or_not_shuffle/src/shuffle_list.rs#L54) masked_swap with XOR mask
- shuffle_list.rs:132 and :155 used in both halves of each round
- shuffle_list.rs:229,254 plain swaps are only in the test reference implementation

**Sources.** [lighthouse#9630](https://github.com/sigp/lighthouse/pull/9630)

</details>

<a id="epoch_processing-025"></a>
<details>
<summary><b>epoch_processing-025</b> Keep payload timeliness committee window in state — <i>implemented · medium · S · cpu</i></summary>

**Idea.** Store the PTC assignments window in the beacon state and rotate it during epoch processing, so PTC lookups read it instead of rerunning balance-weighted sampling per call.

**Gap in Lighthouse.** 

**Impact.** Already done: PTC lookups read state.ptc_window instead of resampling per call.

**Best measured result.** Motivated by PayloadCommittee hotspot (~18-20% CPU) seen in profiling (pr:prysm#16573)

**Evidence (Lighthouse @ 928b61e719).**

- single_pass.rs:539 process_ptc_window keeps the PTC window in state and rotates via pop_front
- single_pass.rs:494 called from epoch processing
- [`beacon_node/beacon_chain/src/shuffling_cache.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs) CachedPTCs used at state_advance_timer.rs:405

**Sources.** [lodestar#9211](https://github.com/ChainSafe/lodestar/pull/9211), [prysm#16573](https://github.com/OffchainLabs/prysm/pull/16573)

</details>

<a id="epoch_processing-028"></a>
<details>
<summary><b>epoch_processing-028</b> Bulk participation rotation and reset at epoch boundary — <i>implemented · medium · S · cpu, memory</i></summary>

**Idea.** At the epoch boundary, rotate current to previous participation by moving or bulk-copying the list or reusing its tree nodes, and replace the current list with a prebuilt zero-filled list or tree of packed zero leaves. This avoids per-validator rebuilds and per-element zeroing.

**Gap in Lighthouse.** Gloas/Heze variants (beacon_state.rs:2301) use ProgressiveList::try_from_iter, a per-element build; not on mainnet forks yet.

**Impact.** Pre-Gloas already cheap. For Gloas, a repeat-style constructor for ProgressiveList would save one O(n) build per epoch (low tens of ms at 1M validators).

**Best measured result.** epochTransition 28.7 -&gt; 34.5 ops/s (pr:teku#5349)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:2278`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2278) rotate_participation_flags: mem::take moves current to previous (O(1))
- beacon_state.rs:2286 List::repeat builds zero list via milhouse repeat_list (repeat.rs:8), shared zero subtrees

**Sources.** [teku#5349](https://github.com/Consensys-Incorporated/teku/pull/5349), [teku#5774](https://github.com/Consensys-Incorporated/teku/pull/5774), [silver#144](https://github.com/gattaca-com/silver/pull/144), [lodestar#9671](https://github.com/ChainSafe/lodestar/pull/9671)

</details>

<a id="epoch_processing-057"></a>
<details>
<summary><b>epoch_processing-057</b> Cache next-epoch boundary state per block root — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** Cache one advanced post-state per (block root, epoch) so tick, attestation and block production reuse it instead of recomputing the epoch transition; advance multi-epoch gaps in one jump.

**Gap in Lighthouse.** 

**Impact.** Already avoids repeating the epoch transition at the slot-0 boundary; advance is one slot at a time, which is fine for the head case.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1124`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1124) get_advanced_hot_state serves cached state by (block_root, max_slot)
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:258`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L258) advance_head stores pre-advanced head state in state_cache
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5421`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5421) block production reuses it
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2161`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2161) attestation path reuses it

**Sources.** [silver#238](https://github.com/gattaca-com/silver/pull/238)

</details>

<a id="epoch_processing-060"></a>
<details>
<summary><b>epoch_processing-060</b> Sequential bulk iteration over validator and balance lists — <i>implemented · medium · cpu, memory</i></summary>

**Idea.** When epoch processing scans the validator registry or participation/balance lists, iterate the backing structure sequentially (tree-leaf, column or bulk forEach/getAll iterator) instead of calling an indexed getter per validator or allocating a view per element. Each indexed get costs a tree descent.

**Gap in Lighthouse.** 

**Impact.** Epoch processing already scans the lists sequentially with cursors, not per-index getters.

**Best measured result.** epoch-start stf 1503 to 709 ms (option c); this option 1126 ms (pr:ethlambda#630)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:230-260`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L230-L260) one pass using izip over participation iters plus iter_cow() on validators, balances, inactivity scores
- milhouse-0.9.0/src/list.rs:151 iter_cow is a sequential tree cursor

**Sources.** [lodestar#7617](https://github.com/ChainSafe/lodestar/pull/7617), [silver#145](https://github.com/gattaca-com/silver/pull/145), [lodestar#1349](https://github.com/ChainSafe/lodestar/pull/1349), [ethlambda#630](https://github.com/lambdaclass/ethlambda/pull/630)

</details>

<a id="epoch_processing-063"></a>
<details>
<summary><b>epoch_processing-063</b> In-order copy-on-write cursor for list writes — <i>implemented · medium · cpu, memory</i></summary>

**Idea.** Write epoch balance changes through an in-order lazy copy-on-write cursor over the persistent tree list, copying a leaf only on first write and keeping cached hashes for unchanged leaves, instead of buffering updates in a map, sorting and rehashing.

**Gap in Lighthouse.** 

**Impact.** Balances are already written through an in-order copy-on-write cursor; unchanged leaves keep cached hashes.

**Best measured result.** Estimate only: tens of ms off each epoch-start block; benchmark not run (pr:ethlambda#647)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs):~237 balances.iter_cow() with next_cow() and make_mut() copy only on write
- milhouse-0.9.0/src/list.rs:151 iter_cow

**Sources.** [ethlambda#647](https://github.com/lambdaclass/ethlambda/pull/647)

</details>

<a id="epoch_processing-064"></a>
<details>
<summary><b>epoch_processing-064</b> Advance committee caches per slot, not in epoch processing — <i>implemented · medium · cpu</i></summary>

**Idea.** Do not build the next-epoch committee/shuffling caches inside the epoch transition; rotate or build current/next caches during per-slot processing so the epoch transition does not pay for them and cache building is not repeated.

**Gap in Lighthouse.** 

**Impact.** Next-epoch committee cache is normally prebuilt per slot by the advance timer, so the transition does not pay for it.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:333-339`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L333-L339) builds Current and Next committee caches during per-slot head advance
- [`consensus/types/src/state/beacon_state.rs:2824`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2824) build_committee_cache is a no-op if already initialized
- [`consensus/state_processing/src/per_epoch_processing/altair.rs:30-32`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/altair.rs#L30-L32) only builds on a miss; advance_caches (beacon_state.rs:2887) just rotates

**Sources.** [lighthouse@073be906d](https://github.com/sigp/lighthouse/commit/073be906da49), [lighthouse#263](https://github.com/sigp/lighthouse/pull/263)

</details>

<a id="epoch_processing-069"></a>
<details>
<summary><b>epoch_processing-069</b> Lightweight justification-only balance totals — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** When only justification/finalization is needed (e.g. checkpoint state or unrealized justification during block import), compute just the participating-balance totals in one pass over validators and flags instead of building full per-validator summaries.

**Gap in Lighthouse.** 

**Impact.** Altair+ justification needs no validator pass at all. Only phase0 still builds ValidatorStatuses, irrelevant on mainnet.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/altair/justification_and_finalization.rs:20`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/altair/justification_and_finalization.rs#L20) uses progressive balances cache target-attesting balances, O(1)
- [`consensus/fork_choice/src/fork_choice.rs:954`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L954) unrealized justification uses it, with parent-checkpoint reuse at :930-945

**Sources.** [grandine@c4b676e3d](https://github.com/grandinetech/grandine/commit/c4b676e3daa0)

</details>

<a id="epoch_processing-092"></a>
<details>
<summary><b>epoch_processing-092</b> Parallel hashing of rebuilt balances leaves — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** After rebuilding the balances list at the epoch boundary, hash its leaf chunks in parallel on a thread pool instead of serially at the next state-root computation.

**Gap in Lighthouse.** 

**Impact.** Milhouse tree_hash is already parallel via rayon::join, covering the balances list at the next state root.

**Best measured result.** epoch 98.8 -&gt; 71.8 ms (M5), 110.2 -&gt; 93.1 ms (EPYC); same total CPU (pr:lodestar#10521)

**Evidence (Lighthouse @ 928b61e719).**

- milhouse-0.9.0/src/tree.rs:530 Node tree_hash uses rayon::join on left/right so balances leaf chunks hash in parallel

**Sources.** [lodestar#10521](https://github.com/ChainSafe/lodestar/pull/10521)

</details>

<a id="epoch_processing-001"></a>
<details>
<summary><b>epoch_processing-001</b> Index-addressed arrays instead of hash maps/sets for participation — <i>implemented · low · cpu, memory</i></summary>

**Idea.** Store per-epoch participation/attester data in a Vec indexed by validator index (or a flat status list) instead of HashMaps or per-attestation HashSets in epoch processing. Lookups become O(1) array reads with no hashing or set construction.

**Gap in Lighthouse.** 

**Impact.** Already done; the 10x phase0 win came in lighthouse#3254/#3255.

**Best measured result.** 10x speedup to epoch processing (commit:nimbus@7c0b4d28d29d)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:243-262`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L243-L262) single pass walks validators/balances/inactivity/participation by index
- [`consensus/types/src/state/epoch_cache.rs:33`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/epoch_cache.rs#L33) effective_balances Vec&lt;u64&gt; indexed by validator index
- participation is a list of flags per validator index, no per-attestation sets in Altair+

**Sources.** [lighthouse#3255](https://github.com/sigp/lighthouse/pull/3255), [lighthouse#3254](https://github.com/sigp/lighthouse/pull/3254), [lighthouse#304](https://github.com/sigp/lighthouse/pull/304), [nimbus@7c0b4d28d](https://github.com/status-im/nimbus-eth2/commit/7c0b4d28d29d), [nimbus@9244ae7a3](https://github.com/status-im/nimbus-eth2/commit/9244ae7a3867), [nimbus#1670](https://github.com/status-im/nimbus-eth2/pull/1670)

</details>

<a id="epoch_processing-002"></a>
<details>
<summary><b>epoch_processing-002</b> Precompute per-validator status and totals once per epoch — <i>implemented · low · cpu</i></summary>

**Idea.** At the start of the epoch transition, make one pass over validators and participation (or pending attestations) to build per-validator status flags (unslashed participating per flag, inclusion distance) and aggregate per-flag balances. Justification, rewards/penalties, inactivity and slashings then read that summary instead of each rescanning attestations or the registry.

**Gap in Lighthouse.** 

**Impact.** Already done; totals are even maintained incrementally across blocks.

**Best measured result.** Epoch 10240 validators 28.4-&gt;5.04 s/op; 3072: 2.54-&gt;0.77 s/op (pr:teku#1109)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:155`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L155) process_epoch_single_pass does all sub-steps in one pass
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:226`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L226) RewardsAndPenaltiesContext from ProgressiveBalancesCache totals
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:120`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L120) ValidatorInfo per-validator flags
- [`consensus/types/src/state/progressive_balances_cache.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/progressive_balances_cache.rs) per-flag balances kept incrementally

**Sources.** [lighthouse#2416](https://github.com/sigp/lighthouse/pull/2416), [lodestar@523f07608](https://github.com/ChainSafe/lodestar/commit/523f07608934), [lighthouse#2369](https://github.com/sigp/lighthouse/pull/2369), [teku#1109](https://github.com/Consensys-Incorporated/teku/pull/1109), [prysm#2346](https://github.com/OffchainLabs/prysm/pull/2346), [prysm#3792](https://github.com/OffchainLabs/prysm/pull/3792), [ethlambda#632](https://github.com/lambdaclass/ethlambda/pull/632), [prysm#4080](https://github.com/OffchainLabs/prysm/pull/4080), [prysm#3788](https://github.com/OffchainLabs/prysm/pull/3788), [silver#167](https://github.com/gattaca-com/silver/pull/167), [prysm#3783](https://github.com/OffchainLabs/prysm/pull/3783), [prysm#3793](https://github.com/OffchainLabs/prysm/pull/3793), [teku#5346](https://github.com/Consensys-Incorporated/teku/pull/5346), [prysm#3797](https://github.com/OffchainLabs/prysm/pull/3797), [teku#3352](https://github.com/Consensys-Incorporated/teku/pull/3352), [teku@c8c53a50e](https://github.com/Consensys-Incorporated/teku/commit/c8c53a50eef8), [lodestar@4206aed2e](https://github.com/ChainSafe/lodestar/commit/4206aed2ed7a), [prysm#3798](https://github.com/OffchainLabs/prysm/pull/3798), [nimbus#1902](https://github.com/status-im/nimbus-eth2/pull/1902), [teku#5778](https://github.com/Consensys-Incorporated/teku/pull/5778)

</details>

<a id="epoch_processing-005"></a>
<details>
<summary><b>epoch_processing-005</b> Flat or transient inactivity scores with batched write back — <i>implemented · low · cpu</i></summary>

**Idea.** Hold inactivity scores in a plain array or fast mutable/transient form for the inactivity update, update them there, and write back changed scores in one batched operation (skip when unchanged). This avoids reading and rebuilding tree paths per validator.

**Gap in Lighthouse.** 

**Impact.** Sequential cow iteration writes back only changed scores, equivalent to the batched write-back.

**Best measured result.** 5x-7x on altair, 3x in perf test (pr:lodestar#3178)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:245`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L245),258 inactivity_scores.iter_cow()
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:634-663`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L634-L663) process_single_inactivity_update skips make_mut when score is 0 and attesting

**Sources.** [lodestar#2721](https://github.com/ChainSafe/lodestar/pull/2721), [lodestar#3178](https://github.com/ChainSafe/lodestar/pull/3178), [lodestar#9911](https://github.com/ChainSafe/lodestar/pull/9911), [lodestar#2921](https://github.com/ChainSafe/lodestar/pull/2921)

</details>

<a id="epoch_processing-007"></a>
<details>
<summary><b>epoch_processing-007</b> Field-level read accessors without copying structs — <i>implemented · low · cpu, memory</i></summary>

**Idea.** Provide accessors that read one field (effective balance, finalized epoch) or one validator read-only by index, and use them in hot epoch, unrealized-justification and committee-selection loops instead of copying the whole checkpoint, validator object or validator array. This removes allocations.

**Gap in Lighthouse.** 

**Impact.** Hot loops read single fields without copying structs; I did not audit every committee-selection/unrealized-justification call site.

**Best measured result.** ProcessEpoch 34.9ms-&gt;25.0ms, 23.6MB-&gt;18.8MB, 389k-&gt;291k allocs (pr:prysm#4766)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/epoch_cache.rs:119`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/epoch_cache.rs#L119) get_effective_balance(index) single-field accessor
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:243`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L243) iter_cow yields references, Validator cloned only on make_mut
- [`consensus/types/src/state/beacon_state.rs:2538`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2538) get_effective_balance

**Sources.** [prysm#4766](https://github.com/OffchainLabs/prysm/pull/4766), [prysm#7698](https://github.com/OffchainLabs/prysm/pull/7698), [prysm#16753](https://github.com/OffchainLabs/prysm/pull/16753), [prysm#13656](https://github.com/OffchainLabs/prysm/pull/13656)

</details>

<a id="epoch_processing-009"></a>
<details>
<summary><b>epoch_processing-009</b> Hoist per-epoch constants out of validator loops — <i>implemented · low · cpu</i></summary>

**Idea.** Compute values that are constant within an epoch (previous epoch, finalized epoch, finality delay, inactivity-leak flag, base_reward/total division, config-derived constants, activation checkpoint) once before the per-validator loop. This avoids repeated getter, lock, division, and copy cost per validator.

**Gap in Lighthouse.** 

**Impact.** Constants are hoisted; lighthouse#3256 did this.

**Best measured result.** ~83ms to ~75ms (pr:lighthouse#3256)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:170-190`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L170-L190) StateContext (epochs, finalized checkpoint, inactivity-leak flag, total active balance, churn) built once
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:226`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L226) RewardsAndPenaltiesContext once
- [`consensus/state_processing/src/epoch_cache.rs:96`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/epoch_cache.rs#L96) BaseRewardPerIncrement once

**Sources.** [lighthouse#3256](https://github.com/sigp/lighthouse/pull/3256), [prysm#9445](https://github.com/OffchainLabs/prysm/pull/9445), [teku#5785](https://github.com/Consensys-Incorporated/teku/pull/5785), [prysm#5699](https://github.com/OffchainLabs/prysm/pull/5699), [teku#5780](https://github.com/Consensys-Incorporated/teku/pull/5780), [prysm#8757](https://github.com/OffchainLabs/prysm/pull/8757), [lodestar@c39ce160d](https://github.com/ChainSafe/lodestar/commit/c39ce160dc3d), [prysm#14197](https://github.com/OffchainLabs/prysm/pull/14197)

</details>

<a id="epoch_processing-010"></a>
<details>
<summary><b>epoch_processing-010</b> Compute sqrt of total balance once per epoch — <i>implemented · low · cpu</i></summary>

**Idea.** Compute integer_squareroot(total_active_balance) (base reward quotient) once per epoch transition and pass it into the reward/penalty loop instead of recomputing per validator.

**Gap in Lighthouse.** 

**Impact.** Sqrt is computed once per epoch and base reward is a table lookup per validator.

**Best measured result.** ~20% faster Altair epoch processing (block_sim 8m21s -&gt; 7m54s) (pr:nimbus#2797)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/epoch_cache.rs:95`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/epoch_cache.rs#L95) SqrtTotalActiveBalance::new once per epoch
- [`consensus/state_processing/src/epoch_cache.rs:109`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/epoch_cache.rs#L109) base_rewards table per effective-balance increment
- [`consensus/types/src/state/epoch_cache.rs:130`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/epoch_cache.rs#L130) get_base_reward is a table lookup
- [`consensus/state_processing/src/per_epoch_processing/base/rewards_and_penalties.rs:144`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/base/rewards_and_penalties.rs#L144) sqrt once (phase0)

**Sources.** [nimbus#2797](https://github.com/status-im/nimbus-eth2/pull/2797), [prysm#2753](https://github.com/OffchainLabs/prysm/pull/2753), [prysm#8945](https://github.com/OffchainLabs/prysm/pull/8945)

</details>

<a id="epoch_processing-013"></a>
<details>
<summary><b>epoch_processing-013</b> Pass total active balance into base reward computation — <i>implemented · low · cpu</i></summary>

**Idea.** Compute total active balance once per epoch pass and pass it into get_base_reward and proposer-reward helpers instead of recomputing it inside each per-validator call. This removes an O(n^2) loop in rewards processing.

**Gap in Lighthouse.** 

**Impact.** Already O(1) per validator for base reward and total active balance.

**Best measured result.** 10x or more speedup on epoch transitions at mid-thousands of validators; 4k validator state_sim from 3m30s to 1m30s (pr:nimbus#565)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:172`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L172) total_active_balance read once into StateContext
- [`consensus/state_processing/src/epoch_cache.rs:96-119`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/epoch_cache.rs#L96-L119) base_rewards table lookup by effective balance, get_base_reward(index) at single_pass.rs:226
- [`consensus/types/src/state/beacon_state.rs:2677`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2677) get_total_active_balance is a cached lookup

**Sources.** [nimbus@3c030d945](https://github.com/status-im/nimbus-eth2/commit/3c030d945d4d), [nimbus@8ac613421](https://github.com/status-im/nimbus-eth2/commit/8ac613421d71), [nimbus@6f87c8fd8](https://github.com/status-im/nimbus-eth2/commit/6f87c8fd89ad), [nimbus#561](https://github.com/status-im/nimbus-eth2/pull/561), [nimbus#565](https://github.com/status-im/nimbus-eth2/pull/565)

</details>

<a id="epoch_processing-014"></a>
<details>
<summary><b>epoch_processing-014</b> Per-epoch caches for active indices, count and totals — <i>implemented · low · cpu</i></summary>

**Idea.** Cache per-epoch derived values (active validator indices and count, current and previous total active balance, churn limit, proposers, seed) in the state or epoch cache. Epoch and block processing helpers look them up instead of scanning or summing over the registry on each use.

**Gap in Lighthouse.** 

**Impact.** Per-epoch derived values are cached; no registry rescans per use.

**Best measured result.** process epoch 96s -&gt; 0.5s at 16324 validators; 5min -&gt; 2.5s at 62500 (pr:prysm#2737)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:2677`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2677) total_active_balance cache
- [`consensus/types/src/state/beacon_state.rs:2824`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2824) build_committee_cache (active indices, shuffling, proposers)
- [`consensus/state_processing/src/epoch_cache.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/epoch_cache.rs) EpochCache with effective balances, base rewards, activation queue
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:156-160`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L156-L160) progressive balances and exit cache initialised before the loop

**Sources.** [lodestar#3096](https://github.com/ChainSafe/lodestar/pull/3096), [teku#1113](https://github.com/Consensys-Incorporated/teku/pull/1113), [teku#700](https://github.com/Consensys-Incorporated/teku/pull/700), [prysm#6254](https://github.com/OffchainLabs/prysm/pull/6254), [nimbus#1089](https://github.com/status-im/nimbus-eth2/pull/1089), [prysm#2737](https://github.com/OffchainLabs/prysm/pull/2737)

</details>

<a id="epoch_processing-015"></a>
<details>
<summary><b>epoch_processing-015</b> Sum next total active balance inside existing loop — <i>implemented · low · cpu, latency</i></summary>

**Idea.** Accumulate next epoch's total active balance inside the existing effective-balance-update or epoch-context validator loop and write it into the cache eagerly. This removes a separate full validator scan, including one on the first block of the next epoch.

**Gap in Lighthouse.** 

**Impact.** Next-epoch total active balance is summed in the single pass; no separate scan or first-block recompute.

**Best measured result.** avoids ~350 ms recomputation on first slot of epoch (2.3M validators) (pr:prysm#16738)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/epoch_cache.rs:57-80`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/epoch_cache.rs#L57-L80) PreEpochCache.update_effective_balance accumulates total_active_balance
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:343-362`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L343-L362) called inside the main validator loop, then into_epoch_cache installs it (epoch_cache.rs ~170)

**Sources.** [lodestar#3023](https://github.com/ChainSafe/lodestar/pull/3023), [lodestar#2929](https://github.com/ChainSafe/lodestar/pull/2929), [prysm#16738](https://github.com/OffchainLabs/prysm/pull/16738)

</details>

<a id="epoch_processing-016"></a>
<details>
<summary><b>epoch_processing-016</b> Fuse epoch sub-steps into a single validator pass — <i>implemented · low · cpu, memory</i></summary>

**Idea.** Merge the per-validator epoch steps (flag rewards/penalties, inactivity, registry updates, slashings, pending deposits/consolidations, effective-balance updates, rotation/exit data) into one or two loops over the validator set, with cached totals and cross-validator state kept outside the loop. The registry is traversed once per epoch with cache-friendly access instead of once per step.

**Gap in Lighthouse.** 

**Impact.** Already one registry traversal per epoch with milhouse iter_cow; further fusion of consolidations/proposer lookahead is small.

**Best measured result.** Epoch-start block stf mean 912 ms to 709 ms over the preceding summary-pass PR (1503 ms base); about 200 ms saved per epoch-start block (pr:ethlambda#633)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:156`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L156) process_epoch_single_pass fuses inactivity, rewards, registry updates, slashings, pending deposits, effective balance updates in one loop (lines 248-360)
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:36`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L36) SinglePassConfig for steps

**Sources.** [nimbus#5404](https://github.com/status-im/nimbus-eth2/pull/5404), [ethlambda#633](https://github.com/lambdaclass/ethlambda/pull/633), [lighthouse#1228](https://github.com/sigp/lighthouse/pull/1228), [lodestar#2831](https://github.com/ChainSafe/lodestar/pull/2831), [nimbus#2814](https://github.com/status-im/nimbus-eth2/pull/2814), [lighthouse#4483](https://github.com/sigp/lighthouse/pull/4483), [lighthouse#5279](https://github.com/sigp/lighthouse/pull/5279), [lighthouse#5761](https://github.com/sigp/lighthouse/pull/5761)

</details>

<a id="epoch_processing-018"></a>
<details>
<summary><b>epoch_processing-018</b> Cache total slashings sum in epoch cache — <i>implemented · low · cpu</i></summary>

**Idea.** Keep the sum of state.slashings in the epoch cache, apply slashing penalties in the rewards pass, and compute the penalty once per distinct effective balance instead of per slashed validator.

**Gap in Lighthouse.** 

**Impact.** Sum computed once per epoch (8192 adds, microseconds) and penalty is cheap arithmetic; worst-case slashing cost already tiny. Not cached across epochs, which is immaterial.

**Best measured result.** processSlashings worstcase 2.65 ms to 96.6 us (377.9 to 10352.7 ops/s) (pr:lodestar#6121)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:1029`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L1029) SlashingsContext::new sums state slashings once per epoch
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:1053`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L1053) process_single_slashing applied inside the main loop; electra uses penalty_per_effective_balance_increment precomputed

**Sources.** [lodestar#6121](https://github.com/ChainSafe/lodestar/pull/6121)

</details>

<a id="epoch_processing-020"></a>
<details>
<summary><b>epoch_processing-020</b> Compute shuffling once and reuse committees — <i>implemented · low · cpu</i></summary>

**Idea.** Compute the epoch shuffling once as a flat array of active indices, cache it by seed/decision root (check the cache before shuffling), and derive committees and attesting indices from it instead of recomputing committees per lookup or per slot.

**Gap in Lighthouse.** 

**Impact.** Shuffling is computed once per epoch and shared via ShufflingCache; committees derived by slicing.

**Best measured result.** 4x speedup on epoch processing for 64 validators (commit:nimbus@ced4dbe859c3)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:2824`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2824) build_committee_cache shuffles once per epoch into a flat CommitteeCache
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:196`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L196),349-362 ShufflingCache keyed by shuffling id with promises
- [`consensus/swap_or_not_shuffle/src/shuffle_list.rs:92`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/swap_or_not_shuffle/src/shuffle_list.rs#L92) whole-list shuffle

**Sources.** [nimbus#153](https://github.com/status-im/nimbus-eth2/pull/153), [prysm#5841](https://github.com/OffchainLabs/prysm/pull/5841), [lodestar@4d68bad56](https://github.com/ChainSafe/lodestar/commit/4d68bad56ebe), [nimbus@6cbf355c5](https://github.com/status-im/nimbus-eth2/commit/6cbf355c5a5a), [nimbus@ced4dbe85](https://github.com/status-im/nimbus-eth2/commit/ced4dbe859c3)

</details>

<a id="epoch_processing-032"></a>
<details>
<summary><b>epoch_processing-032</b> Return early from process_slashings when none apply — <i>implemented · low · cpu, memory</i></summary>

**Idea.** Skip the process_slashings validator loop (and any copy-on-write of the validator list) when no validator is slashed with a withdrawable epoch at the midpoint.

**Gap in Lighthouse.** 

**Impact.** Already no extra pass and no copy-on-write of the validator list when nothing applies.

**Best measured result.** heap flame graph shows validator copies; no numbers (pr:prysm#7587)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:327`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L327) - slashings fused into the single validator pass, no separate loop
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:1060`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L1060) - only slashed validators with matching withdrawable_epoch touch balance via make_mut (Cow)
- [`consensus/state_processing/src/per_epoch_processing/slashings.rs:26`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/slashings.rs#L26) - standalone slow path only for tests/tools

**Sources.** [lodestar#2943](https://github.com/ChainSafe/lodestar/pull/2943), [prysm#7587](https://github.com/OffchainLabs/prysm/pull/7587), [prysm#7544](https://github.com/OffchainLabs/prysm/pull/7544)

</details>

<a id="epoch_processing-033"></a>
<details>
<summary><b>epoch_processing-033</b> Exit queue cache instead of registry scans — <i>implemented · low · cpu</i></summary>

**Idea.** Keep a cache of the max exit epoch and its churn count, updated incrementally per exit, so initiate_validator_exit does not scan the whole validator registry for each exit.

**Gap in Lighthouse.** 

**Impact.** Exit queue lookups are O(1) after a single cache build; Electra uses earliest_exit_epoch/exit_balance_to_consume state fields.

**Best measured result.** no numbers; labeled optimization (pr:prysm#12737)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/common/initiate_validator_exit.rs:20`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/initiate_validator_exit.rs#L20) - build_exit_cache then exit_cache().max_epoch()/get_churn_at
- [`consensus/types/src/state/exit_cache.rs:13`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/exit_cache.rs#L13) - ExitCache with record_validator_exit incremental update
- [`consensus/state_processing/src/common/initiate_validator_exit.rs:46`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/initiate_validator_exit.rs#L46) - record_validator_exit after each exit

**Sources.** [lighthouse@5394726ca](https://github.com/sigp/lighthouse/commit/5394726caffb), [prysm#12737](https://github.com/OffchainLabs/prysm/pull/12737), [nimbus#6144](https://github.com/status-im/nimbus-eth2/pull/6144)

</details>

<a id="epoch_processing-034"></a>
<details>
<summary><b>epoch_processing-034</b> Bounded heap for activation queue selection — <i>implemented · low · cpu, memory</i></summary>

**Idea.** In registry updates, keep only the top churn-limit activation candidates in a bounded heap keyed by (eligibility epoch, index), instead of collecting and sorting all eligible validators.

**Gap in Lighthouse.** 

**Impact.** Equivalent effect: only candidates are tracked in an ordered structure, no collect-all-and-sort over the registry (and none at all post-Electra).

**Best measured result.** registry update avg 26ms to 17ms; ~35% faster registry processing (pr:nimbus#5412)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/activation_queue.rs:11`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/activation_queue.rs#L11) - ActivationQueue as sorted BTreeSet&lt;(eligibility_epoch,index)&gt;
- [`consensus/types/src/state/activation_queue.rs:36`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/activation_queue.rs#L36) - get_validators_eligible_for_activation takes first churn_limit entries
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:228`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L228) - queue read from epoch cache and next queue built during the pass

**Sources.** [nimbus#5412](https://github.com/status-im/nimbus-eth2/pull/5412)

</details>

<a id="epoch_processing-036"></a>
<details>
<summary><b>epoch_processing-036</b> Track participation total balances incrementally — <i>implemented · low · cpu, latency</i></summary>

**Idea.** Maintain current/previous epoch per-flag (including target) unslashed participating balance totals incrementally as each block's attestations are processed (progressive balances). Justification/finalization at the epoch boundary then reads the totals instead of scanning all validators; enable it by default without a from-scratch recheck.

**Gap in Lighthouse.** 

**Impact.** Already done (PR 4971), always on, no from-scratch recheck.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/progressive_balances_cache.rs:160`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/progressive_balances_cache.rs#L160) - on_new_attestation/on_slashing/on_effective_balance_change incremental updates
- [`consensus/state_processing/src/per_epoch_processing/altair/justification_and_finalization.rs:16`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/altair/justification_and_finalization.rs#L16) - J&amp;F reads cached target balances
- [`consensus/types/src/state/progressive_balances_cache.rs:293`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/progressive_balances_cache.rs#L293) - enabled for all Altair+ states unconditionally

**Sources.** [teku#6747](https://github.com/Consensys-Incorporated/teku/pull/6747), [teku#5963](https://github.com/Consensys-Incorporated/teku/pull/5963), [teku#5993](https://github.com/Consensys-Incorporated/teku/pull/5993), [lighthouse#4971](https://github.com/sigp/lighthouse/pull/4971), [teku#6804](https://github.com/Consensys-Incorporated/teku/pull/6804), [teku#6958](https://github.com/Consensys-Incorporated/teku/pull/6958), [teku#6993](https://github.com/Consensys-Incorporated/teku/pull/6993), [lodestar#4294](https://github.com/ChainSafe/lodestar/pull/4294), [lodestar#4205](https://github.com/ChainSafe/lodestar/pull/4205), [teku#5904](https://github.com/Consensys-Incorporated/teku/pull/5904)

</details>

<a id="epoch_processing-039"></a>
<details>
<summary><b>epoch_processing-039</b> Reuse unrealized-finality balances in epoch transition — <i>implemented · low · cpu</i></summary>

**Idea.** Cache the participating-balance totals computed for unrealized justification/finality on block receipt and reuse them when the real epoch transition runs on the same data.

**Gap in Lighthouse.** 

**Impact.** Both unrealized and real J&amp;F read the O(1) progressive-balances totals, so there is no balance scan to reuse; only the cheap weigh step runs twice.

**Best measured result.** saves ~10ms of epoch processing time (pr:nimbus#8216)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fork_choice/src/fork_choice.rs:954`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L954) - on_block computes unrealized J&amp;F via altair process_justification_and_finalization(state) using progressive balances
- [`consensus/state_processing/src/per_epoch_processing/altair.rs:40`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/altair.rs#L40) - real epoch transition calls the same function on the same cache

**Sources.** [nimbus#8216](https://github.com/status-im/nimbus-eth2/pull/8216)

</details>

<a id="epoch_processing-045"></a>
<details>
<summary><b>epoch_processing-045</b> Inline hot arithmetic helpers — <i>implemented · low · cpu</i></summary>

**Idea.** Mark thin checked-arithmetic and integer-division helper functions as inline so hot epoch-processing loops compile to direct ops instead of calls.

**Gap in Lighthouse.** 

**Impact.** Already inlined (PR 3229); safe_arith is the external crate used for all epoch-loop arithmetic.

**Best measured result.** epoch transition 398ms to 359ms (9.77%) (pr:lighthouse#3229)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/registry/src/*/safe_arith-0.1.0/src/lib.rs:139 - #[inline] on safe_add and the other checked-arithmetic impls (lines 90,139-154)

**Sources.** [lighthouse#3229](https://github.com/sigp/lighthouse/pull/3229), [lodestar#2345](https://github.com/ChainSafe/lodestar/pull/2345)

</details>

<a id="epoch_processing-048"></a>
<details>
<summary><b>epoch_processing-048</b> Nimbus processEpoch redundant-work cleanup — <i>implemented · low · S · cpu</i></summary>

**Idea.** Remove redundant work in epoch-processing helpers (exact change not recorded) so processEpoch runs several times faster.

**Gap in Lighthouse.** 

**Impact.** Already one fused pass over milhouse lists; no obvious redundant helper left. Source change is unrecorded so this is a generic match.

**Best measured result.** processEpoch 5x faster, total 2x faster with 16k validators (pr:nimbus#157)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:155`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L155) process_epoch_single_pass fuses inactivity, rewards, registry, slashings, effective balance in one validator loop

**Sources.** [nimbus#157](https://github.com/status-im/nimbus-eth2/pull/157)

</details>

<a id="epoch_processing-049"></a>
<details>
<summary><b>epoch_processing-049</b> Nimbus epoch hot-loop optimization — <i>implemented · low · S · cpu</i></summary>

**Idea.** Optimize hot loops in epoch processing (details not recorded in the source).

**Gap in Lighthouse.** 

**Impact.** Hot loops are already single-pass with cached base rewards; details of source change unknown.

**Best measured result.** 8x speedup on epoch processing for 64 validators (pr:nimbus#215)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:228`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L228) single fused hot loop with iter_cow cursors
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:243`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L243) per-validator work uses cached base_reward

**Sources.** [nimbus#215](https://github.com/status-im/nimbus-eth2/pull/215)

</details>

<a id="epoch_processing-055"></a>
<details>
<summary><b>epoch_processing-055</b> Append new validator caches in place — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** When the per-validator effective-balance cache is uniquely owned (freshly cloned at epoch start), append new validators in place instead of copying the whole array per deposit.

**Gap in Lighthouse.** 

**Impact.** A fresh Vec is built once per epoch with capacity and appended in place; there is no per-deposit array copy, so nothing to save.

**Best measured result.** Napkin math: 16 copies of ~1.9 MiB, about 30.5 MiB moved per epoch avoided (commit:lodestar@bc748d841e53)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/epoch_cache.rs:29`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/epoch_cache.rs#L29) PreEpochCache builds effective_balances with Vec::with_capacity and pushes in place
- [`consensus/state_processing/src/epoch_cache.rs:47`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/epoch_cache.rs#L47) update_effective_balance pushes when index == len

**Sources.** [lodestar@bc748d841](https://github.com/ChainSafe/lodestar/commit/bc748d841e53)

</details>

<a id="epoch_processing-066"></a>
<details>
<summary><b>epoch_processing-066</b> Use length accessors instead of copying lists — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Read the length of balances, randao mixes and similar state lists through a length accessor rather than copying the slice/list just to take its length in epoch processing.

**Gap in Lighthouse.** 

**Impact.** Lists are milhouse trees with O(1) len(); no copying for length reads.

**Best measured result.** 'Saves a little bit of time / space in epoch processing' (pr:prysm#4769)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:213`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L213) validators.len() on milhouse list
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:1104`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L1104) state.pending_deposits() borrows list, no copy

**Sources.** [prysm#4769](https://github.com/OffchainLabs/prysm/pull/4769)

</details>

<a id="epoch_processing-070"></a>
<details>
<summary><b>epoch_processing-070</b> Carry epoch caches into precomputed checkpoint state — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** When precomputing the next epoch's checkpoint state ahead of the boundary, transfer the already built epoch cache (shufflings, proposers, etc.) to the state used for block import so it is not rebuilt later.

**Gap in Lighthouse.** 

**Impact.** State advance timer runs the epoch transition ahead of the boundary and keeps EpochCache/committee caches in the stored state, and also primes shuffling and proposer caches.

**Best measured result.** Epoch transition mainnet 1.1s to 0.96s, 64-node 0.81s to 0.73s, 16-node 4s to 3.3s (pr:lodestar#6068)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:335`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L335) builds Current/Next committee caches on advanced state
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:445`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L445) put_state stores the advanced state with its caches
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:486`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L486) EpochCache for next epoch installed during epoch processing

**Sources.** [lodestar#6068](https://github.com/ChainSafe/lodestar/pull/6068)

</details>

<a id="epoch_processing-090"></a>
<details>
<summary><b>epoch_processing-090</b> Avoid computing shuffling for total active balance — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Do not build the committee shuffling just to obtain total_active_balance in process_epoch; get it from cached totals and defer shuffling to where it is actually needed.

**Gap in Lighthouse.** 

**Impact.** Total active balance does not need a shuffling in Lighthouse; shuffling is built at altair.rs:32 only because the Next cache becomes Current after advance_caches.

**Best measured result.** saves about 120ms for process_epoch on the massive deposit queue (pr:nimbus#8214)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/altair.rs:33`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/altair.rs#L33) build_total_active_balance_cache
- [`consensus/types/src/state/beacon_state.rs:2728`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2728) compute_total_active_balance_slow scans validators, no shuffling
- single_pass.rs:481 next-epoch total set from next_epoch_cache

**Sources.** [nimbus#8214](https://github.com/status-im/nimbus-eth2/pull/8214)

</details>

<a id="epoch_processing-096"></a>
<details>
<summary><b>epoch_processing-096</b> Validators in persistent vector with fast iteration — <i>implemented · low · S · cpu, sync</i></summary>

**Idea.** Keep validators in a persistent/structurally shared vector with cheap clone and array-like iteration, rather than iterating a slow tree-backed list during epoch processing.

**Gap in Lighthouse.** 

**Impact.** Already cheap clone and structural sharing; no further gain.

**Best measured result.** epoch transition 3.5-4.2s to 1.2-1.6s; prepareEpochProcessState 1500 to 100; 16 exits 6000 to 200 (pr:lodestar#1925)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:243-245`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L243-L245) milhouse persistent List with iter_cow over validators, balances, inactivity_scores
- Cargo.lock milhouse dependency

**Sources.** [lodestar#1877](https://github.com/ChainSafe/lodestar/pull/1877), [lodestar#1925](https://github.com/ChainSafe/lodestar/pull/1925)

</details>

<a id="epoch_processing-099"></a>
<details>
<summary><b>epoch_processing-099</b> Skip balance writes for zero reward deltas — <i>implemented · low · S · cpu</i></summary>

**Idea.** When applying rewards and penalties, skip the balance read/write for validators whose net delta is zero (e.g. exited validators).

**Gap in Lighthouse.** 

**Impact.** Already skipped; no gain.

**Best measured result.** "not a huge speed improvement"; ~15% of validator set has zero delta (pr:teku#7284)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:674`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L674) early return when !is_eligible
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:697`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L697) balance written only if delta.rewards != 0 \|\| delta.penalties != 0

**Sources.** [teku#7284](https://github.com/Consensys-Incorporated/teku/pull/7284)

</details>

<a id="epoch_processing-100"></a>
<details>
<summary><b>epoch_processing-100</b> Read-only registry scan, mutate collected indices — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** In process_registry_updates, do a read-only pass to collect indices for activation queue, activation and ejection, then mutate only those validators, avoiding copying the whole registry each epoch.

**Gap in Lighthouse.** 

**Impact.** Registry is not copied wholesale; only changed validators are cloned via copy-on-write.

**Best measured result.** worst case copy reduced to ~8 MB of indices; average case near zero allocation (pr:prysm#14130)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:243-300`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L243-L300) single pass over validators using Cow; make_mut only on changes (e.g. :1406)
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:845-860`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L845-L860) registry update reads validator, queues indices in BTreeSet/ActivationQueue

**Sources.** [prysm#14130](https://github.com/OffchainLabs/prysm/pull/14130)

</details>

<a id="epoch_processing-108"></a>
<details>
<summary><b>epoch_processing-108</b> Precompute OR-combined status flags per validator — <i>implemented · low · S · cpu</i></summary>

**Idea.** Combine per-validator status flags (OR) once before reward delta computation rather than in every loop iteration.

**Gap in Lighthouse.** 

**Impact.** Flags derived once per validator in the single pass; no gain.

**Best measured result.** 16% less getAttestationDeltas, ~150ms per epoch (pr:lodestar#2341)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:273`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L273) ValidatorInfo computed once per validator with is_eligible/is_active/participation flags used by all sub-steps
- [`consensus/types/src/state/progressive_balances_cache.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/progressive_balances_cache.rs) totals maintained incrementally

**Sources.** [lodestar#2341](https://github.com/ChainSafe/lodestar/pull/2341)

</details>

<a id="epoch_processing-097"></a>
<details>
<summary><b>epoch_processing-097</b> Reuse old balances tree as rebuild base — <i>n/a · medium · memory, cpu</i></summary>

**Idea.** When rebuilding the balances list tree at the epoch transition, reuse a retained balances tree from a pruned/finalized state as the base instead of building it from scratch, reducing allocation spikes and hashing.

**Gap in Lighthouse.** 

**Impact.** Lodestar rebuilds a persistent tree from a flat array; Lighthouse's milhouse copy-on-writes only changed leaves, so no from-scratch rebuild exists.

**Best measured result.** processRewardsAndPenalties spikes reduced; ~250ms saved average; prepareNextEpoch ~350ms saved (pr:lodestar#7084)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:243`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L243) iter_cow edits the milhouse tree in place, sharing untouched subtrees with the parent state
- milhouse 0.9.0 (git d67aabd) structural sharing

**Sources.** [lodestar#7084](https://github.com/ChainSafe/lodestar/pull/7084)

</details>

<a id="epoch_processing-040"></a>
<details>
<summary><b>epoch_processing-040</b> Byte lookup table for aggregation bit reads — <i>n/a · low · cpu</i></summary>

**Idea.** Read attestation aggregation bits via a precomputed 256-entry byte-to-bits table and per-bit accessors instead of materializing boolean arrays in epoch status loops.

**Gap in Lighthouse.** 

**Impact.** Aggregation bits are only read in epoch processing for phase0 (base validator_statuses), which is long past on mainnet; Lighthouse's Altair+ path uses flag bytes.

**Best measured result.** epoch transition 3.5s -&gt; 1.5s; aggregation bit access 14.5s -&gt; 3.1s (pr:lodestar#2510)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/attestation/participation_flags.rs:25`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/attestation/participation_flags.rs#L25) - Altair+ epoch loops read per-validator ParticipationFlags bytes, not aggregation bits
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:141`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L141) - has_flag

**Sources.** [lodestar#2510](https://github.com/ChainSafe/lodestar/pull/2510)

</details>

<a id="epoch_processing-075"></a>
<details>
<summary><b>epoch_processing-075</b> Machine-word integers for reward/penalty math — <i>n/a · low · S · cpu, memory</i></summary>

**Idea.** Use native 64-bit (or smaller) integers for per-validator reward and penalty arrays and divisions in epoch processing wherever values provably fit, instead of arbitrary-precision bigint arithmetic.

**Gap in Lighthouse.** 

**Impact.** None; Rust uses native u64 with safe_arith, no bigint to remove.

**Best measured result.** getAttestationDeltas average 130ms to 79ms (pr:lodestar#2092)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:171`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L171) u64 balances used natively

**Sources.** [lodestar@b0c8c21e3](https://github.com/ChainSafe/lodestar/commit/b0c8c21e3cc2), [lodestar#2092](https://github.com/ChainSafe/lodestar/pull/2092), [lodestar@ca51e1219](https://github.com/ChainSafe/lodestar/commit/ca51e1219c24)

</details>

<a id="epoch_processing-095"></a>
<details>
<summary><b>epoch_processing-095</b> Scan validator registry from packed SSZ bytes — <i>n/a · low · S · cpu, memory, latency</i></summary>

**Idea.** Read validator fields for epoch processing scans (statuses, active indices, registry and effective-balance updates) directly from the packed SSZ bytes without building and caching per-validator view objects, avoiding gigabytes of allocation on a freshly loaded state.

**Gap in Lighthouse.** 

**Impact.** Lighthouse already works on native structs; only the cost of decoding a freshly loaded state remains, which this idea does not address.

**Best measured result.** cold epoch transition 7,442 ms -&gt; 4,041 ms; warm 4,432 -&gt; 1,668 ms; heap growth 1,970 -&gt; 930 MB; used heap 5.56 -&gt; 3.80 GB (pr:teku#11597)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:243`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L243) validators.iter_cow() yields borrowed native Validator structs from milhouse, no per-validator view objects

**Sources.** [teku#11597](https://github.com/Consensys-Incorporated/teku/pull/11597)

</details>

