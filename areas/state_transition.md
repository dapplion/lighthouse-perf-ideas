# state_transition

68 checked ideas, 3 actionable. [Back to the summary](../README.md).

## Actionable (3)

High or medium value, verdict `not` or `partial`.

<a id="state_transition-110"></a>
<details>
<summary><b>state_transition-110</b> Pre-verify builder deposit signatures before fork — <i>partial · high · M · cpu, latency</i></summary>

**Idea.** Verify pending builder-deposit BLS signatures in the background during idle slots before the fork that onboards builders (and as payloads arrive), and cache the results as a pure function of deposit data. The fork upgrade and block import then look up results instead of verifying thousands of signatures inline.

**Gap in Lighthouse.** Fork-boundary onboarding is pre-verified and cached. Post-Gloas BuilderDepositRequest signatures for new builders are still verified one by one inline in process_builder_deposit_request. A BuilderDeposit-domain cache (or batch pre-verify) filled when the envelope arrives on gossip is missing.

**Impact.** Fork stall already removed. Remaining gain is only in the adversarial case of many new-builder deposit requests in one payload (single BLS verifies each, up to the per-payload max) during envelope import.

**Best measured result.** s2 onboard 2m12s-&gt;214ms; s3 23.8s-&gt;40ms; s5 23.9s-&gt;25ms (pr:prysm#17440)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/builder_deposits_cache.rs:23`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/builder_deposits_cache.rs#L23) OnboardBuildersCache pre-verifies pending_deposits ahead of the Gloas fork
- [`consensus/state_processing/src/builder_deposits_cache.rs:131`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/builder_deposits_cache.rs#L131) batch verification via is_valid_deposit_signature_batch
- [`consensus/state_processing/src/upgrade/gloas.rs:270`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/upgrade/gloas.rs#L270) fork onboarding uses is_valid_deposit_signature_cached
- [`consensus/state_processing/src/builder_deposits_cache.rs:35`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/builder_deposits_cache.rs#L35) doc says the cache must never be used for BuilderDepositRequest (Domain::BuilderDeposit)
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:941`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L941) post-fork new-builder deposit signature verified inline
- [`consensus/types/src/builder/builder_deposit_request.rs:30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/builder/builder_deposit_request.rs#L30) is_valid_builder_deposit_signature single verify, no cache
- [`beacon_node/beacon_chain/src/payload_envelope_verification/gossip_verified_envelope.rs:100`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/gossip_verified_envelope.rs#L100) envelope gossip checks only the request count, not signatures

**Second check.** Checked envelope gossip verification and every caller of the cache and of is_valid_builder_deposit_signature; no pre-verify or batch path exists for post-fork builder deposits, and the cache doc explicitly forbids reusing it across domains.

**Sources.** [lighthouse#9311](https://github.com/sigp/lighthouse/pull/9311), [prysm#17440](https://github.com/OffchainLabs/prysm/pull/17440), [lodestar#9727](https://github.com/ChainSafe/lodestar/pull/9727), [lodestar#9436](https://github.com/ChainSafe/lodestar/pull/9436)

</details>

<a id="state_transition-054"></a>
<details>
<summary><b>state_transition-054</b> Skip validator tree reads in withdrawals — <i>not · medium · M · cpu</i></summary>

**Idea.** Cache validator-derived data so withdrawal processing does not traverse the whole validators and balances tree unless a withdrawal is actually due.

**Gap in Lighthouse.** No cache of withdrawable/partially-withdrawable validators, so the sweep always reads up to max_validators_per_withdrawals_sweep validators and balances. A per-state set of due indices (invalidated on credential, exit and balance changes) would let the sweep skip non-due ranges.

**Impact.** Small: the sweep is capped at 16384 milhouse reads of native values (no deserialization), probably low single-digit ms per block. Lodestar's worst case (reading from a serialized tree) does not apply to the same extent.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/withdrawals.rs:249`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/withdrawals.rs#L249) get_validators_sweep_withdrawals reads each validator with state.get_validator per index
- [`consensus/state_processing/src/per_block_processing/withdrawals.rs:279`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/withdrawals.rs#L279) get_balance_after_withdrawals per index
- [`consensus/types/src/state`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state)/ (activation_queue, exit_cache, slashings_cache, progressive_balances_cache, epoch_cache, pubkey_cache) has no withdrawal-eligibility cache
- [`consensus/types/src/state/beacon_state.rs:2514`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2514) comment notes a withdrawal-related cache would be fiddly

**Second check.** Searched all state caches and the withdrawals module for any eligibility or skip structure; none exists. Lodestar#4792 itself was closed unmerged.

**Sources.** [lodestar#4792](https://github.com/ChainSafe/lodestar/pull/4792)

</details>

<a id="state_transition-135"></a>
<details>
<summary><b>state_transition-135</b> Reuse tree nodes and hashes at fork upgrade — <i>partial · medium · M · cpu, latency, memory</i></summary>

**Idea.** In the fork upgrade, reuse the previous state's tree nodes for unchanged fields instead of rebuilding them, so cached hashes survive and the post-fork hash tree root is cheap.

**Gap in Lighthouse.** Registry and participation lists change from List to ProgressiveList at Gloas and are rebuilt element by element from cloned values, so every leaf hash and packed-leaf hash is lost and the first post-fork hash_tree_root re-hashes the whole registry. milhouse has no List-&gt;ProgressiveList conversion that reuses Arc leaves (for Validator) or carries over cached leaf hashes; adding one (or pre-seeding leaf hashes) would keep the leaf work and only rebuild the interior spine.

**Impact.** One-off at the Gloas fork boundary: shorter state upgrade and much cheaper first post-fork tree hash (Lodestar: 3.2s-&gt;1.2s upgrade, 32s-&gt;4.9s hash on mainnet); no steady-state gain.

**Best measured result.** 'upgradeStateToGloas 3205ms to 1178ms; hashTreeRoot 32196ms to 4899ms' (mainnet state) (pr:lodestar#9601)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/upgrade/gloas.rs:89-94`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/upgrade/gloas.rs#L89-L94),107-109 block_roots/state_roots/randao_mixes/slashings/sync committees cloned (Arc tree, cached hashes kept); historical_roots, eth1_data_votes, proposer_lookahead mem::take'd
- [`consensus/state_processing/src/upgrade/gloas.rs:98-99`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/upgrade/gloas.rs#L98-L99),104-109,117,146-152 validators, balances, participation, inactivity, pending_* rebuilt with ProgressiveList::try_from_iter(pre.x.iter().cloned())
- d67aabd/src/progressive_list.rs:36-45 try_from_iter builds a fresh tree from values
- d67aabd/src/progressive_tree.rs:101-128,394-410 ProgressiveTreeBuilder pushes values into new Builder subtrees with zero hashes; no constructor takes existing Arc leaves/subtrees from a List

**Second check.** Checked the git-pinned milhouse (rev d67aabd) that Lighthouse actually uses, not the registry 0.9.0: ProgressiveList/ProgressiveTree only offer value-based construction (try_from_iter/Builder), rebase only works between two ProgressiveLists, so no leaf-hash reuse path exists for the List-&gt;ProgressiveList conversion.

**Sources.** [lodestar#9601](https://github.com/ChainSafe/lodestar/pull/9601)

</details>

## Other checked ideas (65)

Implemented, not applicable, or low value.

<a id="state_transition-048"></a>
<details>
<summary><b>state_transition-048</b> Cache signature domains per fork — <i>not · low · S · cpu</i></summary>

**Idea.** Cache computed signature domains keyed by fork and domain type (with the genesis validators root) instead of recomputing them for every signature check.

**Gap in Lighthouse.** Add a small cache keyed by (domain, fork_version, genesis_validators_root) in ChainSpec or the signature-set builders; compute_domain and get_domain would consult it.

**Impact.** One sha256 per signature set; saves a few percent of signature-set building at most, tiny next to BLS verification.

**Best measured result.** None (pr:lodestar#2787)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/core/chain_spec.rs:591`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/core/chain_spec.rs#L591) get_domain -&gt; compute_domain:724 recompute fork data root (sha256) each call
- [`consensus/state_processing/src/per_block_processing/signature_sets.rs:159`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/signature_sets.rs#L159) callers

**Sources.** [lodestar#2515](https://github.com/ChainSafe/lodestar/pull/2515), [lodestar#2787](https://github.com/ChainSafe/lodestar/pull/2787)

</details>

<a id="state_transition-052"></a>
<details>
<summary><b>state_transition-052</b> Sync committee index cache per period — <i>not · low · S · cpu, memory</i></summary>

**Idea.** Cache the validator indices of sync committee members once per sync period as flat data in the shared epoch context, instead of resolving pubkeys to indices per block or duplicating it per state.

**Gap in Lighthouse.** Cache the Vec of indices per sync period (in a shared cache keyed by period/committee root) and use it in process_sync_aggregate and rewards instead of get_sync_committee_indices.

**Impact.** Removes 512 hash lookups and a pubkey-cache update check per block; microseconds to ~1 ms per block, small.

**Best measured result.** None (pr:nimbus#3115)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:1753`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1753) get_sync_committee_indices does 512 pubkey_cache hash lookups per call
- [`consensus/state_processing/src/per_block_processing/altair/sync_committee.rs:55`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/altair/sync_committee.rs#L55) called per block, also clones current_sync_committee:20

**Sources.** [nimbus#3115](https://github.com/status-im/nimbus-eth2/pull/3115), [lodestar#3729](https://github.com/ChainSafe/lodestar/pull/3729)

</details>

<a id="state_transition-084"></a>
<details>
<summary><b>state_transition-084</b> Hardware sqrt for integer square root — <i>not · low · S · cpu</i></summary>

**Idea.** Compute integer square root with the hardware float sqrt (with correction) instead of a software Newton loop.

**Gap in Lighthouse.** Replace integer_sqrt calls in BaseRewardPerIncrement::new and get_attestation_participation with u64::isqrt or f64 sqrt plus correction.

**Impact.** Called about once per block/epoch; saving ~50 ns is unmeasurable on a mainnet node.

**Best measured result.** None (pr:prysm#5253)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/common/base.rs:12`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/base.rs#L12) total_active_balance.integer_sqrt()
- integer-sqrt-0.1.5/src/lib.rs:44-70 software bitwise loop

**Sources.** [prysm#5253](https://github.com/OffchainLabs/prysm/pull/5253)

</details>

<a id="state_transition-150"></a>
<details>
<summary><b>state_transition-150</b> Skip pubkey cache build in no-verify replay — <i>not · low · M · cpu, startup</i></summary>

**Idea.** When replaying blocks without signature checks, skip building the decompressed pubkey cache and initialise other caches lazily.

**Gap in Lighthouse.** Add a flag so BlockReplayer / state load paths skip update_pubkey_cache (and lazily build it) when signatures are not verified; but process_operations.rs:76 needs it for Electra deposit requests so it would have to be built lazily there.

**Impact.** Small: the pubkey cache is an incremental persistent map (only new validators inserted), so the full ~1s rebuild only occurs on cold states; saves little on a running node.

**Best measured result.** pubkey cache build takes ~1s on the testnet (pr:lighthouse#783)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:2757`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2757) build_caches always calls update_pubkey_cache
- [`consensus/state_processing/src/per_slot_processing.rs:115`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_slot_processing.rs#L115) build_caches after each epoch transition
- [`beacon_node/store/src/hot_cold_store.rs:1832`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1832) build_all_caches on every hot state load
- [`consensus/state_processing/src/block_replayer.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/block_replayer.rs): no_signature_verification only changes signature strategy, no cache skipping

**Sources.** [lighthouse#783](https://github.com/sigp/lighthouse/pull/783)

</details>

<a id="state_transition-001"></a>
<details>
<summary><b>state_transition-001</b> Sparse BTreeMap for pending updates in persistent lists — <i>partial · low · S · cpu, memory</i></summary>

**Idea.** Store pending (uncommitted) updates to persistent validator and balance lists in a sparse ordered map (BTreeMap) keyed by index instead of a dense vector of options. Memory and work stay proportional to the number of changed entries, not the list length, so block processing and tree hashing of recent states get faster.

**Gap in Lighthouse.** Only validators use the sparse map. Balances, previous/current epoch participation and inactivity_scores still use the dense VecMap (Vec&lt;Option&lt;T&gt;&gt;). Change the type aliases (Balances, BalancesGloas and the participation/inactivity field types) to BTreeMap&lt;usize,u64&gt;/&lt;ParticipationFlags&gt;/&lt;u64&gt; and benchmark, since balances and participation are touched densely per epoch and the VecMap may win there.

**Impact.** Lower peak memory and cheaper clone/apply for recent states when few entries change; modest, since these lists are mutated densely at epoch boundaries.

**Best measured result.** block with exits: process 92.4ms to 12.5ms, post-block hash 132ms to 15.4ms (pr:lighthouse#9017)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:76-93`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L76-L93) Validators and ValidatorsGloas use BTreeMap&lt;usize, Validator&gt; (PR 9017)
- [`consensus/types/src/state/beacon_state.rs:78`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L78),82 Balances = List&lt;u64, N&gt; and BalancesGloas = ProgressiveList&lt;u64&gt; keep the default MaxMap&lt;VecMap&gt;
- participation and inactivity_scores lists also use the default (milhouse list.rs:30 default U = MaxMap&lt;VecMap&lt;T&gt;&gt;)

**Sources.** [lighthouse#6820](https://github.com/sigp/lighthouse/pull/6820), [lighthouse#7043](https://github.com/sigp/lighthouse/pull/7043), [lighthouse#9017](https://github.com/sigp/lighthouse/pull/9017)

</details>

<a id="state_transition-014"></a>
<details>
<summary><b>state_transition-014</b> Pubkey index for builder registry lookups — <i>partial · low · M · cpu</i></summary>

**Idea.** Keep (or build once per block) a pubkey-to-index map for the builder registry, and use the validator pubkey index for pending-deposit checks, so builder deposits, exits and fork-upgrade onboarding look up pubkeys in O(1) instead of scanning the registry or validator list.

**Gap in Lighthouse.** Runtime builder deposit and exit requests still scan state.builders() linearly. Add a builder pubkey-to-index cache on BeaconState (like pubkey_cache) maintained in add_builder_to_registry, and use it in process_builder_deposit_request and process_builder_exit_request.

**Impact.** Only matters with a large builder registry (thousands) under Gloas; block processing with many builder requests goes from O(requests*builders) to O(requests).

**Best measured result.** None (pr:lodestar#9397)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/upgrade/gloas.rs:256`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/upgrade/gloas.rs#L256) builder_pubkey_to_index HashMap at fork upgrade; get_validator_index at :262 for pending-deposit check
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:937`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L937) process_builder_deposit_request linear .position() over builders
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:994`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L994) process_builder_exit_request linear .position()

**Sources.** [lighthouse#9345](https://github.com/sigp/lighthouse/pull/9345), [teku#10729](https://github.com/Consensys-Incorporated/teku/pull/10729), [lodestar#10263](https://github.com/ChainSafe/lodestar/pull/10263), [lodestar#9397](https://github.com/ChainSafe/lodestar/pull/9397), [lighthouse#8833](https://github.com/sigp/lighthouse/pull/8833)

</details>

<a id="state_transition-018"></a>
<details>
<summary><b>state_transition-018</b> Read validators via read-only references, not copies — <i>partial · low · S · cpu, memory, latency</i></summary>

**Idea.** In non-mutating paths (exit initiation, slashings, withdrawals sweep, pending deposits, proposer and committee selection), read validator fields through read-only references or views instead of getters that copy a validator or the registry, or get-then-commit. Validator copies showed up as 10-20% of CPU.

**Gap in Lighthouse.** Most paths read by reference (milhouse is persistent, no copy). The one non-mutating read via get_validator_cow in initiate_validator_exit could use get_validator; Cow of a tree leaf may force the mut path to be created (validators_mut). Minor.

**Impact.** Negligible for Lighthouse; validator copies are not a hot spot as in Prysm.

**Best measured result.** None (pr:prysm#16530)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:2408`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2408) get_validator returns &amp;Validator (no copy)
- [`consensus/state_processing/src/common/initiate_validator_exit.rs:11`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/initiate_validator_exit.rs#L11) get_validator_cow used just to read exit_epoch
- [`consensus/state_processing/src/per_block_processing/withdrawals.rs:156`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/withdrawals.rs#L156) read-only get_validator

**Sources.** [prysm#7697](https://github.com/OffchainLabs/prysm/pull/7697), [prysm#1235](https://github.com/OffchainLabs/prysm/pull/1235), [prysm#16530](https://github.com/OffchainLabs/prysm/pull/16530), [prysm#5674](https://github.com/OffchainLabs/prysm/pull/5674), [nimbus#1594](https://github.com/status-im/nimbus-eth2/pull/1594), [prysm#14558](https://github.com/OffchainLabs/prysm/pull/14558), [prysm#5776](https://github.com/OffchainLabs/prysm/pull/5776), [prysm#7008](https://github.com/OffchainLabs/prysm/pull/7008), [prysm#14599](https://github.com/OffchainLabs/prysm/pull/14599), [lodestar@daebcf1be](https://github.com/ChainSafe/lodestar/commit/daebcf1beff5)

</details>

<a id="state_transition-037"></a>
<details>
<summary><b>state_transition-037</b> Per-block block-root cache and batched proposer reward — <i>partial · low · S · cpu</i></summary>

**Idea.** During block attestation processing, cache block roots for target and head lookups (most attestations share them) and accumulate the proposer reward across the block, writing the balance once. Benchmark whether the root cache beats direct state lookups.

**Gap in Lighthouse.** Proposer reward is accumulated per attestation but written to the balance once per attestation, not once per block; no block-root cache across attestations (direct milhouse get each time). To match: accumulate the reward in process_attestations (ctxt) and call increase_balance once at the end, and optionally cache target/head roots per distinct AttestationData.

**Impact.** Saves up to 8 (Electra) to 128 (pre-Electra) proposer balance tree writes per block; probably well under 0.1 ms. The root cache is likely a wash, as the source PR itself says to benchmark.

**Best measured result.** None (pr:lodestar#4374)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/process_operations.rs:255`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L255),299 - per-attestation get_attestation_participation_flag_indices and increase_balance(proposer)
- [`consensus/state_processing/src/common/get_attestation_participation.rs:37`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/get_attestation_participation.rs#L37),69 - direct state.get_block_root lookups per attestation
- [`consensus/types/src/state/beacon_state.rs:1911`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1911) - get_block_root is a milhouse Vector get

**Sources.** [lodestar#2938](https://github.com/ChainSafe/lodestar/pull/2938), [lodestar#4374](https://github.com/ChainSafe/lodestar/pull/4374), [lodestar#2836](https://github.com/ChainSafe/lodestar/pull/2836), [lodestar#4375](https://github.com/ChainSafe/lodestar/pull/4375)

</details>

<a id="state_transition-039"></a>
<details>
<summary><b>state_transition-039</b> Batch-verify deposit signatures in a block — <i>partial · low · M · cpu</i></summary>

**Idea.** Batch-verify all deposit signatures in a block at once, and fall back to per-deposit verification only when the batch fails.

**Gap in Lighthouse.** Batch verifier is only wired to the Gloas upgrade. Block path (apply_deposit) and the epoch pending-deposit loop (single_pass.rs new_validator_deposits) call is_valid_deposit_signature one by one. Collect first-time-pubkey deposits and call is_valid_deposit_signature_batch, taking care that duplicate pubkeys in the same batch only verify the first.

**Impact.** Epoch processing can see up to 16 new-validator deposits (and blocks up to 16 legacy ones): about 4ms vs 22ms per such block/epoch; matters only during deposit-heavy periods.

**Best measured result.** None (pr:teku#5274)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/verify_deposit.rs:104`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/verify_deposit.rs#L104) - is_valid_deposit_signature_batch exists (parallel decompress, chunked batch, fallback)
- [`consensus/state_processing/src/builder_deposits_cache.rs:131`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/builder_deposits_cache.rs#L131) - used only for Gloas builder onboarding
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:757`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L757) - block path verifies each new-validator deposit individually
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:410`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L410) - epoch pending-deposit path also individual

**Sources.** [teku#5274](https://github.com/Consensys-Incorporated/teku/pull/5274)

</details>

<a id="state_transition-125"></a>
<details>
<summary><b>state_transition-125</b> Avoid per-committee temporary allocations in transition — <i>partial · low · S · cpu, memory</i></summary>

**Idea.** Remove per-validator/per-attestation temporary allocations in state transition, e.g. reuse the participation flag sequence instead of allocating it per committee computation.

**Gap in Lighthouse.** Minor: a handful of per-attestation Vec allocs remain (get_attesting_indices variants, get_payload_attesting_indices.rs:33); could reuse buffers or return iterators.

**Impact.** Already mostly alloc-free; the participation-flag case is covered. Remaining savings are tiny versus signature and tree-hash cost.

**Best measured result.** hundreds of thousands of temp seq allocations removed (pr:nimbus#5235)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/common/get_attestation_participation.rs:77`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/get_attestation_participation.rs#L77) SmallVec for flag indices (no heap)
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs) single pass epoch processing avoids per-validator allocs
- [`consensus/state_processing/src/common/get_attesting_indices.rs:102`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/get_attesting_indices.rs#L102) vec![] per call in some paths

**Sources.** [nimbus#5235](https://github.com/status-im/nimbus-eth2/pull/5235)

</details>

<a id="state_transition-126"></a>
<details>
<summary><b>state_transition-126</b> Reuse hasher and scratch buffers in sync selection — <i>partial · low · S · cpu, memory</i></summary>

**Idea.** Reuse one SHA-256 hasher and stack scratch buffers in sync committee index selection and Merkle branch verification, instead of allocating a digest or result per hash.

**Gap in Lighthouse.** Merkle verification is fine, but sync committee/proposer selection allocates a preimage Vec and digest Vec per candidate and rehashes the same 32-byte block for up to 16/32 consecutive i. Cache the digest per i/16 and use a stack buffer in compute_proposer_index / get_next_sync_committee_indices.

**Impact.** Sync committee selection runs once per 256 epochs and proposer selection once per epoch (pre-Fulu or at lookahead), so the saving is a few hundred microseconds to low ms at most.

**Best measured result.** IsValidMerkleBranch depth 33: 67 -&gt; 34 allocs/op, 3201 -&gt; 1088 B/op (pr:caplin#22406)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/merkle_proof/src/lib.rs:382-397`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/merkle_proof/src/lib.rs#L382-L397) merkle_root_from_branch uses hash32_concat on stack, no per-level alloc
- [`consensus/types/src/state/beacon_state.rs:1487-1513`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1487-L1513) shuffling_random_byte/u16 does seed.to_vec(), int_to_bytes8 and hash()-&gt;Vec per candidate
- [`consensus/swap_or_not_shuffle/src/compute_shuffled_index.rs:80-90`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/swap_or_not_shuffle/src/compute_shuffled_index.rs#L80-L90) new Context per hash

**Sources.** [teku#6195](https://github.com/Consensys-Incorporated/teku/pull/6195), [caplin#22406](https://github.com/erigontech/erigon/pull/22406)

</details>

<a id="state_transition-015"></a>
<details>
<summary><b>state_transition-015</b> Verify pending deposit signatures lazily, once per pubkey — <i>implemented · medium · cpu</i></summary>

**Idea.** When onboarding builders or processing deposit requests, check whether a pubkey has a pending validator deposit with an O(1) per-pubkey status set, and BLS-verify a pending deposit signature only when needed and at most once, instead of eagerly verifying or rescanning the whole pending-deposit queue.

**Gap in Lighthouse.** 

**Best measured result.** None (pr:teku#11511)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/upgrade/gloas.rs:253`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/upgrade/gloas.rs#L253) valid_pending_validator_pubkeys HashSet gives O(1) is_pending_validator
- [`consensus/state_processing/src/upgrade/gloas.rs:164`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/upgrade/gloas.rs#L164) and builder_deposits_cache.rs:164 is_valid_deposit_signature_cached verifies once and writes back
- [`consensus/state_processing/src/upgrade/gloas.rs:270`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/upgrade/gloas.rs#L270) signature checked only for deposits that need it
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:883`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L883) process_deposit_requests only pushes to pending queue, no scan

**Sources.** [lodestar#9180](https://github.com/ChainSafe/lodestar/pull/9180), [lodestar#9374](https://github.com/ChainSafe/lodestar/pull/9374), [teku#11155](https://github.com/Consensys-Incorporated/teku/pull/11155), [teku#11511](https://github.com/Consensys-Incorporated/teku/pull/11511), [prysm#17387](https://github.com/OffchainLabs/prysm/pull/17387)

</details>

<a id="state_transition-024"></a>
<details>
<summary><b>state_transition-024</b> Use known state roots in per-slot processing — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** When importing or replaying blocks, pass the already known per-slot state root (from the parent block, the block itself, or a stored empty-slot root cache) to slot processing, or skip a root nobody observes, so it does not tree-hash the full state each slot. This saves a full state hash tree root per block and per replayed slot.

**Gap in Lighthouse.** 

**Best measured result.** None (pr:lighthouse#2863)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_slot_processing.rs:38`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_slot_processing.rs#L38) per_slot_processing takes state_root: Option&lt;Hash256&gt;, cache_state uses it
- [`consensus/state_processing/src/block_replayer.rs:176`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/block_replayer.rs#L176) get_state_root takes root from state_root_iter or previous block's state_root (line 200)
- [`consensus/state_processing/src/state_advance.rs:74`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/state_advance.rs#L74) partial_state_advance state_root_opt
- [`beacon_node/beacon_chain/src/block_verification.rs:2175`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L2175) state_root_opt passed through on block import

**Sources.** [lighthouse#2863](https://github.com/sigp/lighthouse/pull/2863), [nimbus#961](https://github.com/status-im/nimbus-eth2/pull/961), [lighthouse#762](https://github.com/sigp/lighthouse/pull/762), [nimbus#2537](https://github.com/status-im/nimbus-eth2/pull/2537)

</details>

<a id="state_transition-057"></a>
<details>
<summary><b>state_transition-057</b> Flat validator array beside tree state — <i>implemented · medium · L · cpu, memory</i></summary>

**Idea.** Keep a flat, structurally shared array (or persistent vector) of validator records or their hot fields beside the tree-backed state, and iterate it in epoch processing, exits, activations and effective-balance collection instead of reading validators through the SSZ tree. Per-block clones stay cheap.

**Gap in Lighthouse.** Indexed reads are O(log n) pointer descents instead of O(1) array lookups; no separate flat array exists, but it is not needed for the gain the idea targets.

**Impact.** The Lodestar gain came from reading validators out of a serialized merkle tree. Lighthouse's milhouse tree is itself a structurally shared persistent vector of native Validator records with hashes cached alongside, so clones are cheap and reads need no deserialization. Residual gain from an extra flat array would be negligible.

**Best measured result.** None (pr:lodestar#1816)

**Evidence (Lighthouse @ 928b61e719).**

- d67aabd/src/leaf.rs:14 milhouse leaves hold native Arc&lt;T&gt; values beside a lazily computed hash, not serialized chunks
- d67aabd/src/tree.rs:85 get_recursive returns &amp;T by pointer descent, no deserialization
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:243`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L243) epoch processing iterates validators linearly with iter_cow
- [`consensus/types/src/state/exit_cache.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/exit_cache.rs), activation_queue.rs, progressive_balances_cache.rs, epoch_cache.rs flat caches for exits, activations and effective balances

**Second check.** Read milhouse (git rev d67aabd from Cargo.lock): leaves store Arc&lt;Validator&gt; natively, which is the equivalent of Lodestar's flat persistent validator array merged with the hash tree. Verdict rests on mechanism equivalence, hence low confidence.

**Sources.** [lodestar#1816](https://github.com/ChainSafe/lodestar/pull/1816), [lodestar@7b11d2ba1](https://github.com/ChainSafe/lodestar/commit/7b11d2ba14b4), [lodestar#2360](https://github.com/ChainSafe/lodestar/pull/2360), [lodestar@fa8136795](https://github.com/ChainSafe/lodestar/commit/fa81367957eb), [lodestar#3065](https://github.com/ChainSafe/lodestar/pull/3065), [lodestar@a15c47e35](https://github.com/ChainSafe/lodestar/commit/a15c47e355d8)

</details>

<a id="state_transition-089"></a>
<details>
<summary><b>state_transition-089</b> Linear scan for state diff on load — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** When diffing validator and inactivity-score buffers against a seed state, first compare whole buffers, then do one linear scan over fixed-size elements instead of recursive binary partitioning.

**Gap in Lighthouse.** 

**Best measured result.** None (commit:lodestar@ddaca79cddee)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hdiff.rs:438`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L438) ValidatorsDiff::compute does a single linear scan comparing y == x per element, no recursion
- [`beacon_node/store/src/hdiff.rs:152`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L152) balances and inactivity_scores use CompressedU64Diff, linear subtraction (line 380)

**Sources.** [lodestar@ddaca79cd](https://github.com/ChainSafe/lodestar/commit/ddaca79cddee)

</details>

<a id="state_transition-112"></a>
<details>
<summary><b>state_transition-112</b> Speculatively advance head state before next slot — <i>implemented · medium · S · latency, cpu</i></summary>

**Idea.** Run slot and epoch processing on a cached head state ahead of the next block (also right after a late block), so block import and duties find the pre-state ready and epoch processing is off the critical path; on a miss, fall back to replay.

**Gap in Lighthouse.** 

**Impact.** Already on the critical path savings; block import skips per_slot_processing.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:258`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L258) advance_head advances head one slot at end of slot and primes caches
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:283`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L283) stores advanced state via get_advanced_hot_state/state cache
- [`beacon_node/store/src/hot_cold_store.rs:1124`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1124) get_advanced_hot_state returns pre-advanced state

**Sources.** [nimbus#2616](https://github.com/status-im/nimbus-eth2/pull/2616), [nimbus@df7bc87af](https://github.com/status-im/nimbus-eth2/commit/df7bc87af544), [grandine#253](https://github.com/grandinetech/grandine/pull/253)

</details>

<a id="state_transition-117"></a>
<details>
<summary><b>state_transition-117</b> Read proposers from stored proposer_lookahead — <i>implemented · medium · S · cpu</i></summary>

**Idea.** Serve proposer indices for current and next epoch from the state's stored proposer_lookahead instead of recomputing the seeded shuffle-based proposer selection.

**Gap in Lighthouse.** 

**Impact.** Shuffle-based selection is only run once per epoch for epoch+2 (and pre-Fulu).

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:1642`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1642) get_beacon_proposer_index reads proposer_lookahead post-Fulu
- [`consensus/types/src/state/beacon_state.rs:1674`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1674) get_beacon_proposer_indices serves current and next epoch from lookahead
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:506`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L506) process_proposer_lookahead shifts and appends

**Sources.** [teku#10162](https://github.com/Consensys-Incorporated/teku/pull/10162), [grandine@5add6ceec](https://github.com/grandinetech/grandine/commit/5add6ceec169), [grandine#312](https://github.com/grandinetech/grandine/pull/312)

</details>

<a id="state_transition-118"></a>
<details>
<summary><b>state_transition-118</b> Read-only bulk traversal of tree-backed lists — <i>implemented · medium · S · memory, cpu</i></summary>

**Idea.** Iterate tree-backed state lists (validators, balances, pending withdrawals, block operations, bitfields) with a read-only bulk traversal of tree nodes instead of per-index get() or converting to an array first. This avoids per-element view creation and tree walks.

**Gap in Lighthouse.** 

**Impact.** Epoch processing uses milhouse iter/iter_cow rather than get(i); some per-index get() remain in block operations but are small.

**Evidence (Lighthouse @ 928b61e719).**

- d67aabd/src/iter.rs:7 stack-based tree Iter yields &amp;T in bulk without per-index walks
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:243`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L243) validators/balances/inactivity iter_cow bulk traversal
- [`consensus/types/src/state/beacon_state.rs:1688`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1688) lookahead iter_from

**Sources.** [lodestar#7419](https://github.com/ChainSafe/lodestar/pull/7419), [lodestar@04647c85b](https://github.com/ChainSafe/lodestar/commit/04647c85bc39), [lodestar@e51bcae3a](https://github.com/ChainSafe/lodestar/commit/e51bcae3a9dc), [lodestar#1233](https://github.com/ChainSafe/lodestar/pull/1233)

</details>

<a id="state_transition-124"></a>
<details>
<summary><b>state_transition-124</b> Skip slot processing when state already at target — <i>implemented · medium · S · cpu, startup, latency</i></summary>

**Idea.** Return early from slot advance when the state is already at the target slot, and call only block processing when the pre-state is already advanced. This avoids a redundant state hash tree root and redundant state transitions.

**Gap in Lighthouse.** 

**Impact.** No redundant state root hashing when state is already at target.

**Best measured result.** 3x reduction when profiling attestation-request RPC (pr:prysm#4314)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/state_advance.rs:98`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/state_advance.rs#L98) while state.slot() &lt; target_slot loop is a no-op when already at target
- [`beacon_node/beacon_chain/src/block_verification.rs:1591`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1591) and 1610 only per_slot_processing when state.slot() &lt; block.slot()
- [`beacon_node/beacon_chain/src/block_verification.rs:2080`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L2080) checks pre-state already advanced

**Sources.** [teku#1059](https://github.com/Consensys-Incorporated/teku/pull/1059), [nimbus#177](https://github.com/status-im/nimbus-eth2/pull/177), [prysm#4314](https://github.com/OffchainLabs/prysm/pull/4314), [nimbus#2630](https://github.com/status-im/nimbus-eth2/pull/2630)

</details>

<a id="state_transition-128"></a>
<details>
<summary><b>state_transition-128</b> Reuse pre-advanced state across validation, import, replay — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Reuse the slot/epoch-advanced state computed earlier (for gossip proposer checks or the next-slot cache) when importing a block or replaying it for rewards, so the epoch transition runs only once.

**Gap in Lighthouse.** 

**Impact.** Epoch transition runs once and is reused by gossip checks, import and production.

**Best measured result.** 500ms+ to ~20ms for slot-0 blocks (pr:prysm#13678)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:2065`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L2065) block import loads get_advanced_hot_state (pre-advanced state from state cache)
- [`beacon_node/store/src/state_cache.rs:316`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L316) get_by_block_root returns most-advanced cached state &lt;= slot
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:283`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L283) timer output is stored in the same cache

**Sources.** [lodestar#2385](https://github.com/ChainSafe/lodestar/pull/2385), [prysm#13678](https://github.com/OffchainLabs/prysm/pull/13678)

</details>

<a id="state_transition-129"></a>
<details>
<summary><b>state_transition-129</b> Reuse checkpoint state for attestation production — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** For attestation production on an old head, use a cached epoch-boundary checkpoint state instead of replaying slots, so committees are not recomputed.

**Gap in Lighthouse.** 

**Impact.** Equivalent via state cache of advanced states plus shuffling/early-attester caches; only the rare old-head case pays a partial advance.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2125`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2125) uses head state when same epoch, else get_advanced_hot_state + partial_state_advance
- [`beacon_node/beacon_chain/src/early_attester_cache.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/early_attester_cache.rs) early attester cache avoids state access for fresh head
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:437`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L437) shuffling cache avoids committee recompute

**Sources.** [teku#2533](https://github.com/Consensys-Incorporated/teku/pull/2533)

</details>

<a id="state_transition-140"></a>
<details>
<summary><b>state_transition-140</b> Share pubkey caches across epoch-context copies — <i>implemented · medium · cpu, memory</i></summary>

**Idea.** Share pubkey-to-index and index-to-pubkey caches between epoch-context/state copies instead of deep-copying them per block, and check indexed-attestation sortedness with one linear pass instead of a set and sort.

**Gap in Lighthouse.** 

**Impact.** Pubkey caches are shared structurally between state copies and sortedness is a single linear pass; nothing left to gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/pubkey_cache.rs:6-14`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/pubkey_cache.rs#L6-L14) PubkeyCache is an rpds HashTrieMap (persistent, O(1) clone)
- [`consensus/types/src/state/beacon_state.rs:2979-2993`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2979-L2993) update_pubkey_cache only inserts new validators
- [`consensus/state_processing/src/per_block_processing/is_valid_indexed_attestation.rs:38-51`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/is_valid_indexed_attestation.rs#L38-L51) linear sortedness check over the slice

**Sources.** [lodestar@e5872c38d](https://github.com/ChainSafe/lodestar/commit/e5872c38da27)

</details>

<a id="state_transition-143"></a>
<details>
<summary><b>state_transition-143</b> Sync signature checks independent of exact state — <i>implemented · medium · cpu, memory</i></summary>

**Idea.** Build block signature sets (sync aggregate) from block data and the sync committee indices rather than the full head state, so verification works on any state of the epoch and can batch across blocks.

**Gap in Lighthouse.** 

**Impact.** Signature sets for sync aggregates are built without applying the block, so they batch across blocks in a segment.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/signature_sets.rs:794-845`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/signature_sets.rs#L794-L845) sync_aggregate_signature_set takes slot, block_root and only reads the sync committee for that epoch, fork and genesis root from the state
- [`consensus/state_processing/src/per_block_processing/block_signature_verifier.rs:373`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/block_signature_verifier.rs#L373) used from the batch verifier

**Sources.** [lodestar#8720](https://github.com/ChainSafe/lodestar/pull/8720), [lodestar#4280](https://github.com/ChainSafe/lodestar/pull/4280)

</details>

<a id="state_transition-145"></a>
<details>
<summary><b>state_transition-145</b> Single-pass participation flag update — <i>implemented · medium · cpu, memory</i></summary>

**Idea.** Mutate participation flags in one pass through a callback instead of copying the participation list on read and again on write per attestation.

**Gap in Lighthouse.** 

**Impact.** Flags are mutated in place per validator; no whole-list copy per attestation.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/process_operations.rs:262-284`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L262-L284) get_epoch_participation_mut then get_mut(index) and add_flag in place via milhouse pending-update cow
- [`consensus/types`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types) state.get_epoch_participation_mut returns a mutable list view, no list copy

**Sources.** [prysm#10409](https://github.com/OffchainLabs/prysm/pull/10409)

</details>

<a id="state_transition-156"></a>
<details>
<summary><b>state_transition-156</b> Slashed-validator bitset cache — <i>implemented · medium · memory, cpu</i></summary>

**Idea.** Keep a bitset of slashed flags per state (cloned lazily on write) so attestation processing checks slash status without reading validator records.

**Gap in Lighthouse.** 

**Impact.** Slashed check avoids reading validator records and the cache clones in O(1); a set instead of a bitset, with the same effect.

**Best measured result.** 0-30MB vs ~500MB extra memory; clone 60x faster (pr:lodestar#4401)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/slashings_cache.rs:9-15`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/slashings_cache.rs#L9-L15) SlashingsCache is an rpds HashTrieSet of slashed indices (persistent, cheap clone)
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:263`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L263),393 attestation processing checks slashings_cache().is_slashed(index)

**Sources.** [lodestar#4401](https://github.com/ChainSafe/lodestar/pull/4401), [lodestar@d5dcf7cb1](https://github.com/ChainSafe/lodestar/commit/d5dcf7cb1838)

</details>

<a id="state_transition-160"></a>
<details>
<summary><b>state_transition-160</b> Plain structs for pending queue items — <i>implemented · medium · cpu</i></summary>

**Idea.** Represent pending deposit, partial withdrawal and consolidation items as plain structs rather than tree-backed containers, so epoch processing over tens of thousands of items does direct field reads.

**Gap in Lighthouse.** 

**Impact.** Milhouse leaves hold T by value, so field reads are plain struct reads; no tree walk per field.

**Best measured result.** ~33x speedup: 12.8 ops/s to 417 ops/s on 50,000 items (pr:lodestar#9054)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/deposit/pending_deposit.rs:13`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/deposit/pending_deposit.rs#L13) PendingDeposit is a plain Rust struct (derive Encode/Decode/TreeHash)
- [`consensus/types/src/state/beacon_state.rs:717-725`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L717-L725) stored in milhouse List/ProgressiveList whose leaves hold the struct value directly

**Sources.** [lodestar#9054](https://github.com/ChainSafe/lodestar/pull/9054)

</details>

<a id="state_transition-003"></a>
<details>
<summary><b>state_transition-003</b> Cache total active balance per epoch and use it — <i>implemented · low · cpu</i></summary>

**Idea.** Compute the total active balance once per epoch, keep it in a state or epoch cache, and make the total-active-balance helper read that cache instead of summing over all validators for each attestation, base reward or churn computation. Block processing and replay then do no per-call validator scans for it.

**Gap in Lighthouse.** 

**Impact.** Already cached; no per-call validator scans.

**Best measured result.** None (pr:nimbus#4434)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:819`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L819) total_active_balance Option&lt;(Epoch,u64)&gt; cache in state
- [`consensus/types/src/state/beacon_state.rs:2682`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2682) get_total_active_balance_at_epoch reads cache
- [`consensus/types/src/state/beacon_state.rs:2710`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2710) build_total_active_balance_cache

**Sources.** [nimbus#4434](https://github.com/status-im/nimbus-eth2/pull/4434), [lighthouse#2560](https://github.com/sigp/lighthouse/pull/2560), [ethlambda#648](https://github.com/lambdaclass/ethlambda/pull/648), [prysm#9152](https://github.com/OffchainLabs/prysm/pull/9152), [prysm#9469](https://github.com/OffchainLabs/prysm/pull/9469)

</details>

<a id="state_transition-004"></a>
<details>
<summary><b>state_transition-004</b> Cache base reward per increment per epoch — <i>implemented · low · cpu</i></summary>

**Idea.** Compute base_reward_per_increment (which needs an integer sqrt of total active balance) once per epoch in the epoch cache, and in attestation processing sum effective-balance increments over attesters then multiply once. This removes per-attester and per-attestation recomputation.

**Gap in Lighthouse.** 

**Impact.** Already done; isqrt once per epoch.

**Best measured result.** None (pr:lodestar#2626)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/epoch_cache.rs:96`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/epoch_cache.rs#L96) base_reward_per_increment computed once per epoch cache
- [`consensus/state_processing/src/common/altair.rs:23`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/altair.rs#L23) get_base_reward takes precomputed BaseRewardPerIncrement

**Sources.** [lodestar@54ec19ebb](https://github.com/ChainSafe/lodestar/commit/54ec19ebb9e7), [lodestar#2626](https://github.com/ChainSafe/lodestar/pull/2626)

</details>

<a id="state_transition-005"></a>
<details>
<summary><b>state_transition-005</b> Allocation-free swap-or-not shuffle and hashing — <i>implemented · low · cpu, memory</i></summary>

**Idea.** Implement the swap-or-not shuffle so its inner loop does not allocate intermediate sequences or a digest per hash: reuse one hasher and fixed stack buffers per call and read the 32-byte digest in place. Shuffles do thousands of hashes, so this removes most allocations in committee computation and replay.

**Gap in Lighthouse.** 

**Impact.** Already allocation-free.

**Best measured result.** None (pr:nimbus#1547)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/swap_or_not_shuffle/src/shuffle_list.rs:11`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/swap_or_not_shuffle/src/shuffle_list.rs#L11) stack Buf and hash_fixed, no heap alloc
- [`consensus/swap_or_not_shuffle/src/compute_shuffled_index.rs:52`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/swap_or_not_shuffle/src/compute_shuffled_index.rs#L52) Context-based hashing, no heap alloc

**Sources.** [nimbus#1547](https://github.com/status-im/nimbus-eth2/pull/1547), [lodestar@6078dc9e1](https://github.com/ChainSafe/lodestar/commit/6078dc9e1294), [teku#6189](https://github.com/Consensys-Incorporated/teku/pull/6189), [caplin#22390](https://github.com/erigontech/erigon/pull/22390), [lighthouse#867](https://github.com/sigp/lighthouse/pull/867)

</details>

<a id="state_transition-006"></a>
<details>
<summary><b>state_transition-006</b> Check-free byte conversions in shuffle inner loop — <i>implemented · low · cpu</i></summary>

**Idea.** In the swap-or-not shuffle inner loop, build hash inputs and read the pivot u64 with infallible fixed-size array conversions or direct little-endian loads instead of length-checked slice helpers. This removes a branch and panic path per iteration.

**Gap in Lighthouse.** 

**Impact.** Equivalent; the source PR measured no difference.

**Best measured result.** Benchmarks showed no difference (pr:lighthouse#6483)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/swap_or_not_shuffle/src/shuffle_list.rs:36`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/swap_or_not_shuffle/src/shuffle_list.rs#L36) copy_from_slice into [u8;8] then from_le_bytes (fixed array)
- [`consensus/swap_or_not_shuffle/src/compute_shuffled_index.rs:77`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/swap_or_not_shuffle/src/compute_shuffled_index.rs#L77) bytes_to_int64 similar

**Sources.** [prysm#12690](https://github.com/OffchainLabs/prysm/pull/12690), [lighthouse#6483](https://github.com/sigp/lighthouse/pull/6483)

</details>

<a id="state_transition-009"></a>
<details>
<summary><b>state_transition-009</b> Whole-list swap-or-not shuffling — <i>implemented · low · cpu</i></summary>

**Idea.** Shuffle or unshuffle the entire active-index list in one list-wise pass with the swap-or-not round structure (one hash per 256 positions, flip pivots per round), instead of computing the shuffled position of each index separately. This needs far fewer hash calls per epoch shuffling.

**Gap in Lighthouse.** 

**Impact.** Already done (250x vs per-index).

**Best measured result.** None (pr:teku#2539)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/swap_or_not_shuffle/src/shuffle_list.rs:92`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/swap_or_not_shuffle/src/shuffle_list.rs#L92) shuffle_list whole-list swap-or-not, one hash per 256 positions, masked_swap

**Sources.** [teku#2539](https://github.com/Consensys-Incorporated/teku/pull/2539), [lodestar@7bbe89b18](https://github.com/ChainSafe/lodestar/commit/7bbe89b18fc2), [lodestar@a2b934e33](https://github.com/ChainSafe/lodestar/commit/a2b934e33116), [nimbus@8baab40ea](https://github.com/status-im/nimbus-eth2/commit/8baab40ea604)

</details>

<a id="state_transition-021"></a>
<details>
<summary><b>state_transition-021</b> Cache and incrementally update exit queue churn — <i>implemented · low · cpu, memory</i></summary>

**Idea.** Compute the exit queue epoch and churn (only the latest exit epoch, not a map of all exit epochs) at most once per block or epoch, cache it, and update it incrementally as exits are initiated, instead of scanning all validators for each exit or slashing. Blocks with many exits go from O(exits*validators) to O(exits).

**Gap in Lighthouse.** 

**Impact.** Already incremental.

**Best measured result.** None (pr:teku#7034)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/common/initiate_validator_exit.rs:19`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/initiate_validator_exit.rs#L19) build_exit_cache once, max_epoch/get_churn_at
- [`consensus/state_processing/src/common/initiate_validator_exit.rs:45`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/initiate_validator_exit.rs#L45) record_validator_exit incremental
- [`consensus/state_processing/src/common/initiate_validator_exit.rs:29`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/initiate_validator_exit.rs#L29) Electra uses compute_exit_epoch_and_update_churn (state-held earliest_exit_epoch, no scan)

**Sources.** [prysm#15764](https://github.com/OffchainLabs/prysm/pull/15764), [prysm#14990](https://github.com/OffchainLabs/prysm/pull/14990), [teku#7034](https://github.com/Consensys-Incorporated/teku/pull/7034), [nimbus#6161](https://github.com/status-im/nimbus-eth2/pull/6161), [lodestar#2695](https://github.com/ChainSafe/lodestar/pull/2695), [lodestar#2928](https://github.com/ChainSafe/lodestar/pull/2928), [lodestar#1764](https://github.com/ChainSafe/lodestar/pull/1764), [lighthouse#5280](https://github.com/sigp/lighthouse/pull/5280)

</details>

<a id="state_transition-027"></a>
<details>
<summary><b>state_transition-027</b> Avoid full beacon state copies — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Do not deep-copy the whole beacon state during state transition: pass views or references, take ownership of states that are not used again, and restore from the head state on failure instead of copying before each transition. This removes multi-MB copies per block and cuts allocations.

**Gap in Lighthouse.** 

**Impact.** Already cheap: state clones are shallow tree clones, so no multi-MB copies on the block path. Little left to gain.

**Best measured result.** None (pr:prysm#1232)

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.lock:milhouse 0.9.0 - persistent tree lists give O(1) structural-sharing clone
- [`consensus/types/src/state/beacon_state.rs:96`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L96) - BeaconState derives Clone over milhouse lists
- [`consensus/state_processing/src/upgrade/electra.rs:167`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/upgrade/electra.rs#L167) - fork upgrades mem::take caches instead of copying

**Sources.** [prysm#16420](https://github.com/OffchainLabs/prysm/pull/16420), [nimbus#1551](https://github.com/status-im/nimbus-eth2/pull/1551), [nimbus#45](https://github.com/status-im/nimbus-eth2/pull/45), [nimbus#930](https://github.com/status-im/nimbus-eth2/pull/930), [prysm#1232](https://github.com/OffchainLabs/prysm/pull/1232), [prysm#4602](https://github.com/OffchainLabs/prysm/pull/4602)

</details>

<a id="state_transition-028"></a>
<details>
<summary><b>state_transition-028</b> Copy-on-write for large state fields — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** Share large state fields (validators, balances, roots) between state clones and copy only on mutation, or store them in chunks so a copy shares unchanged chunks. State clones become cheap in time and memory.

**Gap in Lighthouse.** 

**Impact.** Already done via milhouse; state clones share unchanged chunks.

**Best measured result.** None (pr:prysm#4699)

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.lock:milhouse 0.9.0 - validators, balances, roots are milhouse List/Vector with shared subtrees, copy-on-write on mutation
- [`consensus/types/src/state/beacon_state.rs:2466`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2466) - appends touch only new leaves

**Sources.** [prysm#4699](https://github.com/OffchainLabs/prysm/pull/4699), [prysm#12077](https://github.com/OffchainLabs/prysm/pull/12077)

</details>

<a id="state_transition-032"></a>
<details>
<summary><b>state_transition-032</b> Update pubkey map in place on append — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** When appending validators during deposit processing, insert only the new pubkey-to-index entries into the existing map, instead of copying or rebuilding the whole map per deposit.

**Gap in Lighthouse.** 

**Impact.** Deposits append one entry; no map rebuild or copy per deposit.

**Best measured result.** None (pr:prysm#6659)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:2466-2474`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2466-L2474) - add_validator_to_registry inserts the new pubkey straight into the cache
- [`consensus/types/src/state/beacon_state.rs:2979`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2979) - update_pubkey_cache only inserts from iter_from(len)
- [`consensus/types/src/state/pubkey_cache.rs:5`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/pubkey_cache.rs#L5) - persistent rpds HashTrieMap, insert_mut, cheap clone

**Sources.** [prysm#5780](https://github.com/OffchainLabs/prysm/pull/5780), [prysm#6659](https://github.com/OffchainLabs/prysm/pull/6659)

</details>

<a id="state_transition-033"></a>
<details>
<summary><b>state_transition-033</b> Pubkey-to-index map for O(1) validator lookups — <i>implemented · low · S · cpu, memory, latency</i></summary>

**Idea.** Keep a pubkey-to-validator (or builder) index map with the state or epoch context, update it as validators are appended, and use it in deposit processing, sync committee index lookup and builder lookup instead of a linear registry scan. Deposit processing becomes linear instead of quadratic.

**Gap in Lighthouse.** 

**Impact.** Already O(1) per lookup; deposit processing is linear.

**Best measured result.** None (pr:teku#3315)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/pubkey_cache.rs:21`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/pubkey_cache.rs#L21) - PubkeyCache pubkey-&gt;index map
- [`consensus/types/src/state/beacon_state.rs:1105`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1105) - get_validator_index uses it
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:739`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L739) - apply_deposit via get_existing_validator_index
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:1136`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L1136) - pending deposits use pubkey_cache().get
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:805`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L805) - withdrawal requests use it

**Sources.** [teku#3315](https://github.com/Consensys-Incorporated/teku/pull/3315), [nimbus#590](https://github.com/status-im/nimbus-eth2/pull/590), [nimbus#6469](https://github.com/status-im/nimbus-eth2/pull/6469), [prysm#4641](https://github.com/OffchainLabs/prysm/pull/4641), [lighthouse#301](https://github.com/sigp/lighthouse/pull/301), [lodestar#504](https://github.com/ChainSafe/lodestar/pull/504), [prysm#16813](https://github.com/OffchainLabs/prysm/pull/16813), [lodestar#1009](https://github.com/ChainSafe/lodestar/pull/1009), [lodestar#9861](https://github.com/ChainSafe/lodestar/pull/9861), [teku#3836](https://github.com/Consensys-Incorporated/teku/pull/3836), [teku#5194](https://github.com/Consensys-Incorporated/teku/pull/5194)

</details>

<a id="state_transition-040"></a>
<details>
<summary><b>state_transition-040</b> Cache committees/shuffling on the state — <i>implemented · low · S · cpu</i></summary>

**Idea.** Compute the shuffling and committees once per epoch (or slot) and store them in a cache on the state object, reused by block processing, attestation processing and duties, instead of recomputing the shuffle on each lookup.

**Gap in Lighthouse.** 

**Impact.** Shuffling is computed once per epoch and reused across block processing, attestation verification and duties.

**Best measured result.** None (pr:teku#514)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:128`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L128) - ShufflingCache shares committee caches across states
- [`consensus/types/src/state/beacon_state.rs:50`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L50) - CommitteeCache stored on BeaconState per RelativeEpoch
- [`consensus/state_processing/src/all_caches.rs:47`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/all_caches.rs#L47) - build_all_caches

**Sources.** [lighthouse#234](https://github.com/sigp/lighthouse/pull/234), [teku@b4a317d3f](https://github.com/Consensys-Incorporated/teku/commit/b4a317d3fa24), [lighthouse@a5de6a191](https://github.com/sigp/lighthouse/commit/a5de6a1915b3), [teku#514](https://github.com/Consensys-Incorporated/teku/pull/514)

</details>

<a id="state_transition-044"></a>
<details>
<summary><b>state_transition-044</b> Epoch cache of effective balances — <i>implemented · low · cpu, memory</i></summary>

**Idea.** Keep an epoch cache of per-validator effective balances (e.g. a flat array of 1-byte increments) and related values like proposer indices, and read it in block processing instead of reading tree-structured validator records.

**Gap in Lighthouse.** 

**Impact.** Already done: block processing reads flat balances, no tree walk.

**Best measured result.** None (pr:lodestar#3718)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/epoch_cache.rs:12`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/epoch_cache.rs#L12) PreEpochCache collects effective_balances Vec&lt;u64&gt;
- [`consensus/types/src/state/epoch_cache.rs:33`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/epoch_cache.rs#L33) flat effective_balances read via get_effective_balance:119

**Sources.** [lighthouse#4429](https://github.com/sigp/lighthouse/pull/4429), [lodestar#3718](https://github.com/ChainSafe/lodestar/pull/3718)

</details>

<a id="state_transition-046"></a>
<details>
<summary><b>state_transition-046</b> Cache the beacon proposer index per slot — <i>implemented · low · S · cpu</i></summary>

**Idea.** Compute the proposer index once per slot (or for all slots of the epoch), cache it in the epoch cache, and reuse it in block processing, signature verification, slashings and rewards instead of recomputing it from the shuffled indices on each call.

**Gap in Lighthouse.** Only pre-Fulu get_beacon_proposer_index (beacon_state.rs:1666) recomputes per call, outside the ConsensusContext path.

**Impact.** Nothing material left on mainnet (Fulu uses lookahead).

**Best measured result.** None (pr:nimbus#1120)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/consensus_context.rs:104`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/consensus_context.rs#L104) get_proposer_index_no_checks caches per block
- [`consensus/types/src/state/beacon_state.rs:1655`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1655) post-Fulu reads proposer_lookahead
- [`beacon_node/beacon_chain/src/builder.rs:758`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L758) BeaconProposerCache

**Sources.** [teku@91c92e927](https://github.com/Consensys-Incorporated/teku/commit/91c92e927f55), [nimbus#1120](https://github.com/status-im/nimbus-eth2/pull/1120), [lighthouse#3604](https://github.com/sigp/lighthouse/pull/3604), [nimbus@3cb7896ba](https://github.com/status-im/nimbus-eth2/commit/3cb7896bab9e)

</details>

<a id="state_transition-047"></a>
<details>
<summary><b>state_transition-047</b> Direct sampling for proposer index — <i>implemented · low · cpu</i></summary>

**Idea.** Select the proposer with a direct sampling loop over shuffled positions (about two probes expected) instead of computing the full shuffle, and derive committee count from the cached active validator count.

**Gap in Lighthouse.** 

**Impact.** Same effect as direct sampling; per-slot proposer choice costs a few shuffled-index probes.

**Best measured result.** None (pr:nimbus#1312)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:1353`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1353) compute_proposer_index loops compute_shuffled_index per probe, no full shuffle

**Sources.** [nimbus#1312](https://github.com/status-im/nimbus-eth2/pull/1312)

</details>

<a id="state_transition-055"></a>
<details>
<summary><b>state_transition-055</b> Bound the withdrawals sweep — <i>implemented · low · cpu</i></summary>

**Idea.** Cap the validators scanned per block in the withdrawals sweep at min(validator count, MAX_VALIDATORS_PER_WITHDRAWALS_SWEEP), so process_withdrawals has a fixed worst-case cost and small states do not loop past the registry.

**Gap in Lighthouse.** 

**Impact.** Sweep already bounded.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/withdrawals.rs:258`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/withdrawals.rs#L258) validators_limit = min(validators.len(), max_validators_per_withdrawals_sweep)

**Sources.** [lodestar#4916](https://github.com/ChainSafe/lodestar/pull/4916), [teku#6593](https://github.com/Consensys-Incorporated/teku/pull/6593), [prysm#16231](https://github.com/OffchainLabs/prysm/pull/16231)

</details>

<a id="state_transition-064"></a>
<details>
<summary><b>state_transition-064</b> Verify block operation signatures in parallel — <i>implemented · low · cpu, latency</i></summary>

**Idea.** Verify independent signatures of block operations and genesis deposits (each slashable attestation in attester slashings, attestations, deposits, exits) in parallel across cores, then apply the state mutations serially without re-verifying. Signature checks are independent, so this scales with core count.

**Gap in Lighthouse.** 

**Impact.** Already done; scales across cores.

**Best measured result.** Provides a large speed improvement (commit:lighthouse@7108d057fb8b)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/block_signature_verifier.rs:439`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/block_signature_verifier.rs#L439) all op signatures batched into one verify_signature_sets, blst multithreaded
- [`consensus/state_processing/src/per_block_processing/verify_deposit.rs:109`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/verify_deposit.rs#L109) deposits decompressed with par_iter
- [`consensus/state_processing/src/per_block_processing.rs:24`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing.rs#L24) state mutations applied after with VerifySignatures::False

**Sources.** [lighthouse@3f9884936](https://github.com/sigp/lighthouse/commit/3f988493622a), [lighthouse@7108d057f](https://github.com/sigp/lighthouse/commit/7108d057fb8b), [lighthouse@e7fba3a47](https://github.com/sigp/lighthouse/commit/e7fba3a47358), [lighthouse@1ca99b8c4](https://github.com/sigp/lighthouse/commit/1ca99b8c4c7d)

</details>

<a id="state_transition-065"></a>
<details>
<summary><b>state_transition-065</b> Compute all committees of a slot at once — <i>implemented · low · cpu</i></summary>

**Idea.** Compute all beacon committees of a slot or epoch in one call, computing the active validator set and committee count once, instead of per-committee helpers that recompute shared inputs in loops.

**Gap in Lighthouse.** 

**Impact.** Committee cache computes the active set and committee count once per epoch; no per-committee recomputation.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/committee_cache.rs:233`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L233) get_beacon_committees_at_slot from one cached shuffling
- [`consensus/types/src/state/beacon_state.rs:1252`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1252) get_beacon_committees_at_epoch

**Sources.** [prysm#14282](https://github.com/OffchainLabs/prysm/pull/14282), [prysm#14284](https://github.com/OffchainLabs/prysm/pull/14284), [prysm#14286](https://github.com/OffchainLabs/prysm/pull/14286)

</details>

<a id="state_transition-075"></a>
<details>
<summary><b>state_transition-075</b> Reject wrong-fork blocks early — <i>implemented · low · cpu</i></summary>

**Idea.** Reject blocks of the wrong fork before entering fork-specific state transition code.

**Gap in Lighthouse.** 

**Impact.** Wrong-fork blocks fail with InconsistentBlockFork at the start of per_block_processing; gain was tiny anyway.

**Best measured result.** None (pr:nimbus#3444)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing.rs:127-134`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing.rs#L127-L134) fork_name checks on block and state before fork-specific processing
- [`consensus/state_processing/src/per_slot_processing.rs:44`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_slot_processing.rs#L44) same for state

**Sources.** [nimbus#3444](https://github.com/status-im/nimbus-eth2/pull/3444)

</details>

<a id="state_transition-081"></a>
<details>
<summary><b>state_transition-081</b> Remove slow paths in large simulations — <i>implemented · low · cpu</i></summary>

**Idea.** Remove slow committee and attestation handling paths in slot processing that made 50k-validator block simulations intractable.

**Gap in Lighthouse.** 

**Impact.** Committee cache, epoch cache and milhouse tree states avoid the slow per-slot recomputation; no known slow path remains.

**Best measured result.** None (pr:nimbus#1287)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/committee_cache.rs:233`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L233) cached committee lookup
- [`consensus/state_processing/src/epoch_cache.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/epoch_cache.rs) per-epoch precompute

**Sources.** [nimbus#1287](https://github.com/status-im/nimbus-eth2/pull/1287)

</details>

<a id="state_transition-088"></a>
<details>
<summary><b>state_transition-088</b> Lazy pubkey parsing and clean reads — <i>implemented · low · cpu</i></summary>

**Idea.** Keep validator pubkeys and signatures as raw bytes and parse curve points lazily, compare pubkeys by bytes, and do not mark the hash cache dirty on read-only list access.

**Gap in Lighthouse.** 

**Impact.** State keeps raw pubkey bytes, decompresses once into a cache, and reads do not invalidate hashes.

**Best measured result.** None (pr:nimbus#2259)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/validator/validator.rs:22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/validator/validator.rs#L22) pubkey is PublicKeyBytes
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:24-29`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L24-L29) keys decompressed once, indices keyed by PublicKeyBytes
- milhouse immutable reads do not dirty the tree-hash cache; only get_mut does

**Sources.** [nimbus#2259](https://github.com/status-im/nimbus-eth2/pull/2259)

</details>

<a id="state_transition-093"></a>
<details>
<summary><b>state_transition-093</b> Simpler Merkle branch verification loop — <i>implemented · low · cpu</i></summary>

**Idea.** Verify Merkle branches (deposit proofs) with a tight, simple loop over the branch nodes instead of a more general construction. Less per-level overhead per proof.

**Gap in Lighthouse.** 

**Impact.** Already a simple loop; the 3% gain is on a cold path.

**Best measured result.** about 3% faster (pr:teku#5206)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/merkle_proof/src/lib.rs:382-397`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/merkle_proof/src/lib.rs#L382-L397) tight loop of hash32_concat
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:687`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L687) deposit proofs verified in parallel

**Sources.** [teku#5206](https://github.com/Consensys-Incorporated/teku/pull/5206)

</details>

<a id="state_transition-098"></a>
<details>
<summary><b>state_transition-098</b> Trusted no-verify path for replaying known blocks — <i>implemented · low · cpu, memory, latency</i></summary>

**Idea.** Give block processing a trusted mode for blocks already verified (replay, state regeneration, initial sync, locally built blocks) that skips BLS signature checks (proposer, RANDAO, attestations, deposits, exits) and the pubkey copying they need. Signature work dominates replay, so skipping it makes regeneration much faster.

**Gap in Lighthouse.** 

**Impact.** Already skips BLS on replay/regen/reconstruction; nothing left to gain.

**Best measured result.** Profile showed those two verifications as the biggest bottleneck (pr:prysm#4943)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing.rs:69`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing.rs#L69) BlockSignatureStrategy::NoVerification
- [`consensus/state_processing/src/block_replayer.rs:113`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/block_replayer.rs#L113) no_signature_verification()
- [`beacon_node/store/src/hot_cold_store.rs:2566`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2566) state regen replays without signatures
- [`beacon_node/store/src/reconstruct.rs:165`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/reconstruct.rs#L165) historic state reconstruction uses NoVerification

**Sources.** [prysm#3589](https://github.com/OffchainLabs/prysm/pull/3589), [prysm#4943](https://github.com/OffchainLabs/prysm/pull/4943), [nimbus#2266](https://github.com/status-im/nimbus-eth2/pull/2266), [nimbus#4435](https://github.com/status-im/nimbus-eth2/pull/4435), [lodestar@3b37d7abf](https://github.com/ChainSafe/lodestar/commit/3b37d7abfc32), [lodestar#536](https://github.com/ChainSafe/lodestar/pull/536), [grandine#920](https://github.com/grandinetech/grandine/pull/920)

</details>

<a id="state_transition-105"></a>
<details>
<summary><b>state_transition-105</b> Per-pubkey index of pending deposits — <i>implemented · low · cpu</i></summary>

**Idea.** Index the pending deposit queue by pubkey with progress and verified-signature state, so a deposit request or builder onboarding touches only that pubkey's pending deposits. This avoids quadratic rescans and repeated BLS verification of the whole queue.

**Gap in Lighthouse.** 

**Impact.** Fork-time builder onboarding is linear; the quadratic scan is gone. Remaining: process_builder_deposit_request (process_operations.rs ~line 925) does a linear builders().iter().position per request, small.

**Best measured result.** Quadratic scan stalled nodes on a devnet (pr:lighthouse#9954)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/builder_deposits_cache.rs:42`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/builder_deposits_cache.rs#L42) OnboardBuildersCache caches deposit signature results
- [`consensus/state_processing/src/upgrade/gloas.rs:227-300`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/upgrade/gloas.rs#L227-L300) onboard_builders_from_pending_deposits uses HashSet/HashMap per pubkey, one registry write

**Sources.** [lighthouse#9954](https://github.com/sigp/lighthouse/pull/9954), [lodestar#9247](https://github.com/ChainSafe/lodestar/pull/9247)

</details>

<a id="state_transition-111"></a>
<details>
<summary><b>state_transition-111</b> Preallocate vectors with known capacity — <i>implemented · low · cpu, memory</i></summary>

**Idea.** Preallocate result vectors with known or upper-bound capacity in hot state-transition paths (sync committee indices, attesting indices, bit packing, pubkey lists, tree-hash helpers). This removes repeated growth reallocation and copying.

**Gap in Lighthouse.** 

**Impact.** Hot paths are preallocated; a few cold vec![] remain (get_attesting_indices.rs:102, single_pass.rs:1096) with negligible effect.

**Best measured result.** Targets ~38% of profiled alloc_space (packBits 9.3%, attesting indices 9.4%, eligible validators 20%) (pr:caplin#22397)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:1798`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1798) sync committee Vec::with_capacity
- [`consensus/state_processing/src/common/get_attesting_indices.rs:33`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/get_attesting_indices.rs#L33) with_capacity(num_set_bits)
- [`consensus/state_processing/src/per_block_processing/signature_sets.rs:306`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/signature_sets.rs#L306),339,752 pubkeys with_capacity
- [`consensus/types/src/state/committee_cache.rs:447`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L447) active indices with_capacity

**Sources.** [lighthouse#3301](https://github.com/sigp/lighthouse/pull/3301), [caplin#22397](https://github.com/erigontech/erigon/pull/22397), [prysm#10408](https://github.com/OffchainLabs/prysm/pull/10408), [caplin#6792](https://github.com/erigontech/erigon/pull/6792)

</details>

<a id="state_transition-114"></a>
<details>
<summary><b>state_transition-114</b> Proposer index from shuffling cache — <i>implemented · low · S · cpu</i></summary>

**Idea.** Compute the proposer index from the committee cache by mapping positions in the unshuffled active validator list via the cached shuffling, instead of rebuilding the active validator list per block.

**Gap in Lighthouse.** Only pre-Fulu replay still rebuilds the active list per block; could map via the committee cache shuffling.

**Impact.** Mainnet is post-Fulu so block processing reads the lookahead directly; only historic pre-Fulu replay pays the O(validators) scan.

**Best measured result.** process block ~6.0ms to ~3.0ms (pr:lighthouse#3263)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:1650-1657`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1650-L1657) post-Fulu proposer from proposer_lookahead
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:85`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L85) BeaconProposerCache
- [`consensus/types/src/state/beacon_state.rs:1664-1667`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1664-L1667) pre-Fulu path still rebuilds active indices (get_active_validator_indices) per call

**Sources.** [lighthouse#3263](https://github.com/sigp/lighthouse/pull/3263)

</details>

<a id="state_transition-131"></a>
<details>
<summary><b>state_transition-131</b> Cache the full epoch shuffling per seed — <i>implemented · low · cpu</i></summary>

**Idea.** Compute the full shuffled validator list once per epoch, cache it keyed by seed/epoch, and slice committees from it at every call site, instead of shuffling per slot or per call.

**Gap in Lighthouse.** 

**Impact.** Already computes the full shuffle once per epoch and shares it; no further gain.

**Best measured result.** Block import 16384: 0.266 to 0.183 s; 32768: 0.387 to 0.219 s; epoch 32768: 1.638 to 1.493 s (pr:teku#1278)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/committee_cache.rs:147`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L147) shuffle_list once per epoch
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:128`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L128) ShufflingCache keyed by AttestationShufflingId
- [`consensus/swap_or_not_shuffle/src/shuffle_list.rs:92`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/swap_or_not_shuffle/src/shuffle_list.rs#L92) optimised whole-list shuffle

**Sources.** [nimbus#1095](https://github.com/status-im/nimbus-eth2/pull/1095), [prysm#2682](https://github.com/OffchainLabs/prysm/pull/2682), [teku#1278](https://github.com/Consensys-Incorporated/teku/pull/1278)

</details>

<a id="state_transition-138"></a>
<details>
<summary><b>state_transition-138</b> Keep state small to cheapen clones — <i>implemented · low · cpu, memory</i></summary>

**Idea.** Avoid full-state clones on hot paths (or keep the state small) because whole-state clone cost scales with state size; use structural sharing.

**Gap in Lighthouse.** 

**Impact.** Already cheap clones via milhouse; nothing to gain.

**Best measured result.** state around 900Kb, slow for proto.Clone (pr:prysm#2144)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs): validators/balances are milhouse persistent lists, structural sharing makes state.clone() cheap
- [`consensus/types/src/state/pubkey_cache.rs:8`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/pubkey_cache.rs#L8) pubkey cache is a persistent HashTrieMap

**Sources.** [prysm#2144](https://github.com/OffchainLabs/prysm/pull/2144)

</details>

<a id="state_transition-141"></a>
<details>
<summary><b>state_transition-141</b> Carry pubkey index cache across fork upgrade — <i>implemented · low · cpu, latency</i></summary>

**Idea.** At the fork upgrade, carry the pubkey-to-index cache from the pre-fork state into the upgraded state instead of rebuilding it.

**Gap in Lighthouse.** 

**Impact.** Every upgrade_to_* moves the pubkey cache into the post-fork state, no rebuild.

**Best measured result.** Speeds up onboardBuildersFromPendingDeposits (no numbers) (pr:teku#10917)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/upgrade/electra.rs:167`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/upgrade/electra.rs#L167) pubkey_cache: mem::take(&amp;mut pre.pubkey_cache)
- upgrade/fulu.rs:109, gloas.rs:174, deneb.rs:70 etc. same

**Sources.** [teku#10917](https://github.com/Consensys-Incorporated/teku/pull/10917)

</details>

<a id="state_transition-154"></a>
<details>
<summary><b>state_transition-154</b> Advance next epoch only when lookahead needs it — <i>implemented · low · cpu, latency</i></summary>

**Idea.** Cache next-epoch proposer shuffling, with the extra epoch of state advance, only when the fork needs it (post-Fulu lookahead), not on pre-Fulu networks.

**Gap in Lighthouse.** 

**Impact.** Next-epoch proposer cache work is gated on Fulu lookahead; no extra epoch advance pre-Fulu.

**Best measured result.** State advances observed especially slow pre-Fulu; no numbers (pr:lighthouse#8388)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:371-390`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L371-L390) next-epoch proposer shuffling cached only if state.slot() &gt; proposer_shuffling_decision_slot(next_epoch)
- [`consensus/types/src/core/chain_spec.rs:1176`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/core/chain_spec.rs#L1176) decision slot depends on fulu_enabled at epoch-1

**Sources.** [lighthouse#8388](https://github.com/sigp/lighthouse/pull/8388)

</details>

<a id="state_transition-061"></a>
<details>
<summary><b>state_transition-061</b> Columnar state with delta overlays — <i>n/a · medium · cpu, memory</i></summary>

**Idea.** Store state in flat columnar form over a shared finalized base and apply each block as a thin delta overlay, rehashing only changed paths.

**Gap in Lighthouse.** Lighthouse's tree-states design already shares a persistent tree across states and rehashes only dirty paths, so a separate columnar plus delta overlay layer is a different architecture, not a missing optimisation.

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.lock milhouse 0.9.0: persistent tree with structural sharing, incremental rehash of changed paths ([`consensus/types`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types) BeaconState uses List/Vector from milhouse)

**Sources.** [silver#59](https://github.com/gattaca-com/silver/pull/59)

</details>

<a id="state_transition-066"></a>
<details>
<summary><b>state_transition-066</b> Compute post-state once per slot — <i>n/a · medium · cpu, disk</i></summary>

**Idea.** Keep the computed post-state for the first valid block of a slot in memory and reuse it, rather than recomputing and persisting it per block.

**Gap in Lighthouse.** Prysm PR is a 2019 prototype assuming one canonical block per slot; Lighthouse must compute a post-state per block for fork choice and already caches states in memory by root and persists only diffs.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1661`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1661) store_hot_state stores a summary plus diffs and caches post-state in state_cache keyed by state root
- [`beacon_node/store/src/hot_cold_store.rs:1124`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1124) get_advanced_hot_state reuses cached/advanced states

**Sources.** [prysm#457](https://github.com/OffchainLabs/prysm/pull/457)

</details>

<a id="state_transition-106"></a>
<details>
<summary><b>state_transition-106</b> Per-slot lock to dedup head state advance — <i>n/a · medium · S · cpu, memory, latency</i></summary>

**Idea.** When several concurrent requests need the head state advanced to the same slot (e.g. sync committee message verification), take a per-slot lock so only one advanced state is computed and the rest reuse it.

**Gap in Lighthouse.** 

**Impact.** Sync committee message verification does not advance a state at all, and the other advance-needing path (attestation shuffling) already dedups with cache Promises.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/sync_committee_verification.rs:471`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/sync_committee_verification.rs#L471) sync committee from chain.sync_committee_at_next_slot, no state advance
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:106`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L106) Promise variant dedups concurrent shuffling computations

**Sources.** [prysm#9595](https://github.com/OffchainLabs/prysm/pull/9595)

</details>

<a id="state_transition-115"></a>
<details>
<summary><b>state_transition-115</b> Tune incremental vs full rebuild threshold for field tries — <i>n/a · medium · S · cpu</i></summary>

**Idea.** Raise the dirty-index threshold above which a state field trie is fully rebuilt instead of updated incrementally, because post-Electra epochs touch many more validators and incremental updates stay cheaper.

**Gap in Lighthouse.** 

**Impact.** Milhouse persistent trees always update incrementally with no full-rebuild switch, so there is no threshold to tune.

**Best measured result.** limit 8000 to 20000 (pr:prysm#15252)

**Evidence (Lighthouse @ 928b61e719).**

- d67aabd/src/tree.rs:164 with_updated_leaves always applies updates incrementally, no rebuild threshold
- d67aabd/src/list.rs:194 apply_updates

**Sources.** [prysm#15252](https://github.com/OffchainLabs/prysm/pull/15252)

</details>

<a id="state_transition-137"></a>
<details>
<summary><b>state_transition-137</b> Roll back on failure instead of cloning state — <i>n/a · medium · cpu, memory</i></summary>

**Idea.** When producing a block or applying speculative changes, apply on the live state and roll back on failure instead of cloning the whole BeaconState.

**Gap in Lighthouse.** 

**Impact.** Cloning a BeaconState in Lighthouse is a structural-sharing clone (milhouse Arc trees, rpds persistent caches), so the speculative-apply-on-a-clone design already avoids the full copy that rollback was meant to avoid.

**Best measured result.** state_sim 30% faster (pr:nimbus#1060)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:96`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L96) BeaconState derives Clone over milhouse persistent trees (Arc-shared nodes)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5344`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5344) states are taken by cheap .clone() of the head state

**Sources.** [nimbus#1060](https://github.com/status-im/nimbus-eth2/pull/1060), [nimbus@f06df1cea](https://github.com/status-im/nimbus-eth2/commit/f06df1cea6eb)

</details>

<a id="state_transition-035"></a>
<details>
<summary><b>state_transition-035</b> Bloom filter for new-deposit pubkey checks — <i>n/a · low · S · cpu</i></summary>

**Idea.** For blocks with several deposits, build a Bloom filter of existing validator pubkeys once per block so new-validator deposits skip the registry lookup or scan.

**Gap in Lighthouse.** 

**Impact.** A Bloom filter only avoids a linear scan or costly lookup; Lighthouse already has a hash map lookup (and the cache is kept across blocks), so a per-block filter build (~10ms at 1.5M keys) would cost more than it saves.

**Best measured result.** None (pr:nimbus#5982)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/pubkey_cache.rs:5`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/pubkey_cache.rs#L5) - persistent hash map gives O(1) lookup
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:739`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L739) - existence check is a hash lookup

**Sources.** [nimbus#5982](https://github.com/status-im/nimbus-eth2/pull/5982)

</details>

<a id="state_transition-059"></a>
<details>
<summary><b>state_transition-059</b> Cheap zero check for sync committee — <i>n/a · low · cpu</i></summary>

**Idea.** Check whether a sync committee is default by testing a few fields (first pubkey, aggregate pubkey) instead of comparing against a multi-MB static zero value.

**Gap in Lighthouse.** 

**Impact.** Lighthouse never compares sync committees to a default value, so there is nothing to speed up.

**Best measured result.** None (pr:nimbus#8779)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/sync_committee/sync_committee.rs:44`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/sync_committee/sync_committee.rs#L44) temporary() only used at upgrade/altair.rs:60 and tests; no comparison against a zero committee found

**Sources.** [nimbus#8779](https://github.com/status-im/nimbus-eth2/pull/8779)

</details>

<a id="state_transition-091"></a>
<details>
<summary><b>state_transition-091</b> Bound empty-slot fill before allocation — <i>n/a · low · memory</i></summary>

**Idea.** Reject blocks whose slot gap would exceed the historical list limit before filling empty-slot entries, so a large slot cannot trigger unbounded allocation.

**Gap in Lighthouse.** 

**Impact.** Lighthouse state uses fixed-size circular block_roots/state_roots vectors, so there is no empty-slot list fill to bound.

**Best measured result.** None (pr:ethlambda#200)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_slot_processing.rs:49`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_slot_processing.rs#L49) cache_state writes one ring entry per slot, no list fill

**Sources.** [ethlambda#200](https://github.com/lambdaclass/ethlambda/pull/200)

</details>

<a id="state_transition-092"></a>
<details>
<summary><b>state_transition-092</b> Bulk validator iterator taking the lock once — <i>n/a · low · cpu</i></summary>

**Idea.** Expose a bulk iterator over the validator registry that takes the state lock once for the whole sweep instead of once per index, and use it in full-registry passes (pubkey cache, epoch precompute, shuffling). Fewer lock acquisitions make registry-wide reads faster.

**Gap in Lighthouse.** 

**Impact.** BeaconState is an owned lock-free milhouse tree, so there is no per-index lock to amortise.

**Best measured result.** 16-29% faster at 2.3M validators, allocations unchanged (pr:prysm#17480)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:24`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L24) plain Vec/HashMap, no per-index lock

**Sources.** [prysm#17480](https://github.com/OffchainLabs/prysm/pull/17480)

</details>

<a id="state_transition-132"></a>
<details>
<summary><b>state_transition-132</b> Per-index shuffle with per-index cache — <i>n/a · low · cpu, memory</i></summary>

**Idea.** Compute committee membership by shuffling individual indices with swap-or-not and caching by (seed, index), instead of shuffling and caching the whole list.

**Gap in Lighthouse.** 

**Impact.** Lighthouse needs every validator shuffled each epoch, where the whole-list algorithm is ~250x faster than per-index; the per-index idea only suits tiny lookups, which it already does for proposer/sync.

**Best measured result.** 4M validators worst case 282 ms; 128000 validators 10 s -&gt; 7.7 ms uncached (pr:prysm#2728)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/swap_or_not_shuffle/src/compute_shuffled_index.rs:21`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/swap_or_not_shuffle/src/compute_shuffled_index.rs#L21) per-index shuffle exists, used only for proposer/sync selection
- [`consensus/types/src/state/committee_cache.rs:147`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L147) committees use whole-list shuffle_list

**Sources.** [prysm#2728](https://github.com/OffchainLabs/prysm/pull/2728)

</details>

