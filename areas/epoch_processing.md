# epoch_processing

112 ideas: 9 not, 17 partial, 56 implemented, 30 n/a; 4 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [epoch_processing-001](#epoch_processing-001) | Index-addressed arrays instead of hash maps/sets for participation | implemented | low | S | cpu, memory |
| [epoch_processing-002](#epoch_processing-002) | Precompute per-validator status and totals once per epoch | implemented | low | S | cpu |
| [epoch_processing-003](#epoch_processing-003) | Flat array copy of validator fields for epoch loops | partial | low | M | cpu |
| [epoch_processing-004](#epoch_processing-004) | Flat balances array shared across epoch steps | implemented | low | S | cpu |
| [epoch_processing-005](#epoch_processing-005) | Flat or transient inactivity scores with batched write back | implemented | low | S | cpu |
| [epoch_processing-006](#epoch_processing-006) | Write validators, balances and scores only when values change | implemented | medium | S | cpu, memory, latency |
| [epoch_processing-007](#epoch_processing-007) | Field-level read accessors without copying structs | implemented | low | S | cpu, memory |
| [epoch_processing-008](#epoch_processing-008) | Contiguous allocation for per-validator epoch records | n/a | low | S | cpu, memory |
| [epoch_processing-009](#epoch_processing-009) | Hoist per-epoch constants out of validator loops | implemented | low | S | cpu |
| [epoch_processing-010](#epoch_processing-010) | Compute sqrt of total balance once per epoch | implemented | low | S | cpu |
| [epoch_processing-011](#epoch_processing-011) | Memoize integer sqrt / base reward per increment | partial | low | S | cpu |
| [epoch_processing-012](#epoch_processing-012) | Fast exact integer square root | not | low | S | cpu |
| [epoch_processing-013](#epoch_processing-013) | Pass total active balance into base reward computation | implemented | low | S | cpu |
| [epoch_processing-014](#epoch_processing-014) | Per-epoch caches for active indices, count and totals | implemented | low | S | cpu |
| [epoch_processing-015](#epoch_processing-015) | Sum next total active balance inside existing loop | implemented | low | S | cpu, latency |
| [epoch_processing-016](#epoch_processing-016) | Fuse epoch sub-steps into a single validator pass | partial | low | M | cpu, memory |
| [epoch_processing-017](#epoch_processing-017) | Cache reward deltas per effective balance value | partial | low | S | cpu |
| [epoch_processing-018](#epoch_processing-018) | Cache total slashings sum in epoch cache | implemented | low | S | cpu |
| [epoch_processing-019](#epoch_processing-019) | Compute next-epoch shuffling asynchronously | implemented | medium | S | cpu, latency |
| [epoch_processing-020](#epoch_processing-020) | Compute shuffling once and reuse committees | implemented | low | S | cpu |
| [epoch_processing-021](#epoch_processing-021) | Reuse one hash output for multiple random draws | not | low | S | cpu |
| [epoch_processing-022](#epoch_processing-022) | Branchless swaps in swap-or-not shuffle | implemented | medium | S | cpu |
| [epoch_processing-023](#epoch_processing-023) | Avoid per-iteration byte conversions in shuffle | implemented | low | S | cpu |
| [epoch_processing-024](#epoch_processing-024) | Skip sorting shuffled indices; cache epoch proposers | implemented | low | S | cpu |
| [epoch_processing-025](#epoch_processing-025) | Keep payload timeliness committee window in state | implemented | medium | S | cpu |
| [epoch_processing-026](#epoch_processing-026) | Update proposer lookahead in place | partial | low | S | cpu, memory |
| [epoch_processing-027](#epoch_processing-027) | Compute fork-dependent epoch data once after upgrade | implemented | low | S | cpu |
| [epoch_processing-028](#epoch_processing-028) **★** | Bulk participation rotation and reset at epoch boundary | partial | medium | M | cpu, memory |
| [epoch_processing-029](#epoch_processing-029) | Fast construction of zero-filled arrays | n/a | low | S | cpu |
| [epoch_processing-030](#epoch_processing-030) | Do not allocate throwaway zero arrays or caches | n/a | low | S | cpu, memory |
| [epoch_processing-031](#epoch_processing-031) | Sparse storage of slashing penalties | implemented | low | S | memory, cpu |
| [epoch_processing-032](#epoch_processing-032) | Return early from process_slashings when none apply | implemented | low | S | cpu, memory |
| [epoch_processing-033](#epoch_processing-033) | Exit queue cache instead of registry scans | implemented | low | S | cpu |
| [epoch_processing-034](#epoch_processing-034) | Bounded heap for activation queue selection | implemented | low | S | cpu, memory |
| [epoch_processing-035](#epoch_processing-035) | Track participation incrementally during block processing | implemented | low | S | cpu |
| [epoch_processing-036](#epoch_processing-036) | Track participation total balances incrementally | implemented | low | S | cpu, latency |
| [epoch_processing-037](#epoch_processing-037) | Cache total attester balance for fork choice | implemented | low | S | cpu |
| [epoch_processing-038](#epoch_processing-038) | Precompute next epoch transition and caches before the boundary | implemented | high | S | latency, cpu |
| [epoch_processing-039](#epoch_processing-039) | Reuse unrealized-finality balances in epoch transition | implemented | low | S | cpu |
| [epoch_processing-040](#epoch_processing-040) | Byte lookup table for aggregation bit reads | n/a | low |  | cpu |
| [epoch_processing-041](#epoch_processing-041) | Columnar per-field scans of validator data | not | low | L | cpu |
| [epoch_processing-042](#epoch_processing-042) | Precomputed attester hash sets for membership tests | n/a | low |  | cpu |
| [epoch_processing-043](#epoch_processing-043) | Linear deduplication of attester index sets | n/a | low |  | cpu, memory |
| [epoch_processing-044](#epoch_processing-044) | Incrementally hashed balances trie | implemented | low | S | cpu |
| [epoch_processing-045](#epoch_processing-045) | Inline hot arithmetic helpers | implemented | low | S | cpu |
| [epoch_processing-046](#epoch_processing-046) | Fast path for small checked multiplication | n/a | low |  | cpu |
| [epoch_processing-047](#epoch_processing-047) | Faster phase0-to-Altair state upgrade | n/a | low |  | cpu |
| [epoch_processing-048](#epoch_processing-048) | Nimbus processEpoch redundant-work cleanup | implemented | low | S | cpu |
| [epoch_processing-049](#epoch_processing-049) | Nimbus epoch hot-loop optimization | n/a | low | S | cpu |
| [epoch_processing-050](#epoch_processing-050) | Caplin rewards and penalties speedup | implemented | low | S | cpu |
| [epoch_processing-051](#epoch_processing-051) | Feature flag to skip crosslink processing | n/a | low | S | cpu, latency |
| [epoch_processing-052](#epoch_processing-052) | Structural equality instead of per-item hash tree root | n/a | low | S | cpu |
| [epoch_processing-053](#epoch_processing-053) | Compute historical batch root without temp object | n/a | low | S | cpu, memory |
| [epoch_processing-054](#epoch_processing-054) | Reuse an already fetched validator | implemented | low | S | cpu |
| [epoch_processing-055](#epoch_processing-055) | Append new validator caches in place | implemented | low | S | cpu, memory |
| [epoch_processing-056](#epoch_processing-056) | Fixed-size tail for new compounding flags | n/a | low | S | memory |
| [epoch_processing-057](#epoch_processing-057) | Cache next-epoch boundary state per block root | implemented | medium | S | cpu, latency |
| [epoch_processing-058](#epoch_processing-058) | Transfer epoch cache only across epoch boundary | implemented | low | S | cpu |
| [epoch_processing-059](#epoch_processing-059) | Preallocated reusable buffers, no per-validator allocations | partial | low | S | cpu, memory |
| [epoch_processing-060](#epoch_processing-060) | Sequential bulk iteration over validator and balance lists | implemented | medium | S | cpu, memory |
| [epoch_processing-061](#epoch_processing-061) **★** | Parallel reward deltas, serial apply, skip no-op writes | partial | medium | M | cpu |
| [epoch_processing-062](#epoch_processing-062) | Diff-synced flat validator cache across epochs | partial | low | M | cpu |
| [epoch_processing-063](#epoch_processing-063) **★** | In-order copy-on-write cursor for list writes | partial | medium | M | cpu, memory |
| [epoch_processing-064](#epoch_processing-064) | Advance committee caches per slot, not in epoch processing | implemented | medium | S | cpu |
| [epoch_processing-065](#epoch_processing-065) | Lazily iterate pending deposits/consolidations with early stop | partial | low | S | cpu, memory |
| [epoch_processing-066](#epoch_processing-066) | Use length accessors instead of copying lists | implemented | low | S | cpu, memory |
| [epoch_processing-067](#epoch_processing-067) | Compute next-epoch balances without full epoch transition | not | low | M | cpu, latency |
| [epoch_processing-068](#epoch_processing-068) | Apply rewards and penalties in one balance pass | implemented | low | S | cpu, memory |
| [epoch_processing-069](#epoch_processing-069) | Lightweight justification-only balance totals | implemented | medium | S | cpu, latency |
| [epoch_processing-070](#epoch_processing-070) | Carry epoch caches into precomputed checkpoint state | implemented | low | S | cpu, latency |
| [epoch_processing-071](#epoch_processing-071) | Precompute validator inclusion-distance map once | implemented | low | S | cpu |
| [epoch_processing-072](#epoch_processing-072) | Compute crosslink winning-root participants once per shard | n/a | low |  | cpu |
| [epoch_processing-073](#epoch_processing-073) | Single pass to derive matching source/target/head attestations | implemented | low | S | cpu |
| [epoch_processing-074](#epoch_processing-074) | Epoch-local inclusion maps without shared mutex | n/a | low |  | cpu |
| [epoch_processing-075](#epoch_processing-075) | Machine-word integers for reward/penalty math | n/a | low | S | cpu, memory |
| [epoch_processing-076](#epoch_processing-076) | Hoist constants into hot function locals | n/a | low |  | cpu |
| [epoch_processing-077](#epoch_processing-077) | Remove closures from shuffling hot loop | n/a | low |  | cpu |
| [epoch_processing-078](#epoch_processing-078) | List-wise swap-or-not shuffle for whole epoch | implemented | low | S | cpu |
| [epoch_processing-079](#epoch_processing-079) | Sync committee sampling from one list shuffle | not | low | S | cpu, latency |
| [epoch_processing-080](#epoch_processing-080) | Native code for shuffling and committee sampling | n/a | low |  | cpu, latency |
| [epoch_processing-081](#epoch_processing-081) | Async shuffling only at normal epoch transitions | n/a | low |  | cpu, memory |
| [epoch_processing-082](#epoch_processing-082) | Compute shufflings synchronously into cache | n/a | low |  | cpu, latency |
| [epoch_processing-083](#epoch_processing-083) | Incremental PTC window: reuse retained subtrees | partial | low | S | cpu, latency |
| [epoch_processing-084](#epoch_processing-084) | In-place low-allocation shuffling | implemented | low | S | cpu, memory |
| [epoch_processing-085](#epoch_processing-085) | Shuffle u32 indices instead of u64 | not | low | M | memory, cpu |
| [epoch_processing-086](#epoch_processing-086) | SIMD-vectorized swap-or-not shuffle | not | low | M | cpu, latency |
| [epoch_processing-087](#epoch_processing-087) | Share one shuffling across all PTC slot computations | partial | low | S | cpu, latency |
| [epoch_processing-088](#epoch_processing-088) | Reuse shuffling cache for proposer lookahead/PTC window | partial | low | M | cpu, latency |
| [epoch_processing-089](#epoch_processing-089) | Zero-copy committee views from shuffling buffer | implemented | low | S | memory, cpu |
| [epoch_processing-090](#epoch_processing-090) | Avoid computing shuffling for total active balance | implemented | low | S | cpu, latency |
| [epoch_processing-091](#epoch_processing-091) | Compute next epoch active indices in existing loop | not | low | M | cpu |
| [epoch_processing-092](#epoch_processing-092) | Parallel hashing of rebuilt balances leaves | implemented | medium | S | cpu, latency |
| [epoch_processing-093](#epoch_processing-093) **★** | Parallelize per-validator epoch loops across cores | not | medium | L | cpu, latency |
| [epoch_processing-094](#epoch_processing-094) | Keep cheap epoch loops single-threaded | implemented | low | S | cpu |
| [epoch_processing-095](#epoch_processing-095) | Scan validator registry from packed SSZ bytes | n/a | low | S | cpu, memory, latency |
| [epoch_processing-096](#epoch_processing-096) | Validators in persistent vector with fast iteration | implemented | low | S | cpu, sync |
| [epoch_processing-097](#epoch_processing-097) | Reuse old balances tree as rebuild base | n/a | medium |  | memory, cpu |
| [epoch_processing-098](#epoch_processing-098) | Stack-allocate fixed-size proposer lookahead | n/a | low |  | memory, cpu |
| [epoch_processing-099](#epoch_processing-099) | Skip balance writes for zero reward deltas | implemented | low | S | cpu |
| [epoch_processing-100](#epoch_processing-100) | Read-only registry scan, mutate collected indices | implemented | low | S | memory, cpu |
| [epoch_processing-101](#epoch_processing-101) | One state lock for whole balance update loop | n/a | low |  | cpu |
| [epoch_processing-102](#epoch_processing-102) | Compact u16 effective-balance increments array | partial | low | S | memory, cpu |
| [epoch_processing-103](#epoch_processing-103) | Sorted batch merge of participation updates | n/a | low |  | cpu |
| [epoch_processing-104](#epoch_processing-104) | Record participation totals at epoch processing | partial | low | S | cpu, latency |
| [epoch_processing-105](#epoch_processing-105) | Tighten per-validator checks in registry scans | implemented | low | S | cpu |
| [epoch_processing-106](#epoch_processing-106) | Reuse previous fork epoch processing code | n/a | low |  | cpu |
| [epoch_processing-107](#epoch_processing-107) | Plain loop reading validator fields once | n/a | low |  | cpu |
| [epoch_processing-108](#epoch_processing-108) | Precompute OR-combined status flags per validator | implemented | low | S | cpu |
| [epoch_processing-109](#epoch_processing-109) | Optimized epoch balance update path by default | n/a | low |  | cpu |
| [epoch_processing-110](#epoch_processing-110) | Single pass over participation flags for stats | n/a | low |  | cpu |
| [epoch_processing-111](#epoch_processing-111) | Count active validators without building index list | implemented | low | S | cpu, memory |
| [epoch_processing-112](#epoch_processing-112) | Compute only fork-applicable churn limits in epoch processing | partial | low | S | cpu |

★ actionable. Click an id for the full record.

## Ideas

<a id="epoch_processing-001"></a>
<details>
<summary><b>epoch_processing-001</b> Index-addressed arrays instead of hash maps/sets for participation — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Store per-epoch participation/attester data in a Vec indexed by validator index (or a flat status list) instead of HashMaps or per-attestation HashSets in epoch processing. Lookups become O(1) array reads with no hashing or set construction.

**Impact.** Already done; no hash maps or per-attestation sets on the Altair+ epoch path.

**Best measured result.** 10x speedup to epoch processing (commit:nimbus@7c0b4d28d29d)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:243-262`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L243-L262) single pass zips validators, balances, inactivity scores and participation flag lists by index
- [`consensus/types/src/state/epoch_cache.rs:33`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/epoch_cache.rs#L33) effective_balances Vec&lt;u64&gt; indexed by validator index
- [`consensus/state_processing/src/per_epoch_processing/altair/justification_and_finalization.rs:9`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/altair/justification_and_finalization.rs#L9) J&amp;F reads progressive balances totals, no sets

**Skeptic check.** Confirmed the Altair+ epoch path is index-addressed flag lists and Vec caches. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#3255](https://github.com/sigp/lighthouse/pull/3255), [lighthouse#3254](https://github.com/sigp/lighthouse/pull/3254), [lighthouse#304](https://github.com/sigp/lighthouse/pull/304), [nimbus@7c0b4d28d](https://github.com/status-im/nimbus-eth2/commit/7c0b4d28d29d), [nimbus@9244ae7a3](https://github.com/status-im/nimbus-eth2/commit/9244ae7a3867), [nimbus#1670](https://github.com/status-im/nimbus-eth2/pull/1670)

</details>


<a id="epoch_processing-002"></a>
<details>
<summary><b>epoch_processing-002</b> Precompute per-validator status and totals once per epoch — <i>implemented · low · S · cpu</i></summary>

**Idea.** At the start of the epoch transition, make one pass over validators and participation (or pending attestations) to build per-validator status flags (unslashed participating per flag, inclusion distance) and aggregate per-flag balances. Justification, rewards/penalties, inactivity and slashings then read that summary instead of each rescanning attestations or the registry.

**Impact.** Already done and better: per-flag totals are kept incrementally across blocks, and per-validator status is computed once per validator.

**Best measured result.** Epoch 10240 validators 28.4-&gt;5.04 s/op; 3072: 2.54-&gt;0.77 s/op (pr:teku#1109)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/altair.rs:40`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/altair.rs#L40) process_justification_and_finalization from cached totals
- [`consensus/state_processing/src/per_epoch_processing/altair/justification_and_finalization.rs:17-23`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/altair/justification_and_finalization.rs#L17-L23) progressive_balances_cache target balances
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:155`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L155) process_epoch_single_pass
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:225`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L225) RewardsAndPenaltiesContext::new(progressive_balances)
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:271`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L271) ValidatorInfo per-validator status computed once

**Skeptic check.** Verified that justification, rewards, inactivity, registry, slashings, deposits and effective balances all read one ValidatorInfo and cached totals. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#2416](https://github.com/sigp/lighthouse/pull/2416), [lodestar@523f07608](https://github.com/ChainSafe/lodestar/commit/523f07608934), [lighthouse#2369](https://github.com/sigp/lighthouse/pull/2369), [teku#1109](https://github.com/Consensys-Incorporated/teku/pull/1109), [prysm#2346](https://github.com/OffchainLabs/prysm/pull/2346), [prysm#3792](https://github.com/OffchainLabs/prysm/pull/3792), [ethlambda#632](https://github.com/lambdaclass/ethlambda/pull/632), [prysm#4080](https://github.com/OffchainLabs/prysm/pull/4080), [prysm#3788](https://github.com/OffchainLabs/prysm/pull/3788), [silver#167](https://github.com/gattaca-com/silver/pull/167), [prysm#3783](https://github.com/OffchainLabs/prysm/pull/3783), [prysm#3793](https://github.com/OffchainLabs/prysm/pull/3793), [teku#5346](https://github.com/Consensys-Incorporated/teku/pull/5346), [prysm#3797](https://github.com/OffchainLabs/prysm/pull/3797), [teku#3352](https://github.com/Consensys-Incorporated/teku/pull/3352), [teku@c8c53a50e](https://github.com/Consensys-Incorporated/teku/commit/c8c53a50eef8), [lodestar@4206aed2e](https://github.com/ChainSafe/lodestar/commit/4206aed2ed7a), [prysm#3798](https://github.com/OffchainLabs/prysm/pull/3798), [nimbus#1902](https://github.com/status-im/nimbus-eth2/pull/1902), [teku#5778](https://github.com/Consensys-Incorporated/teku/pull/5778), [lodestar@7ec58337f](https://github.com/ChainSafe/lodestar/commit/7ec58337f787), [lodestar@2d48b1a50](https://github.com/ChainSafe/lodestar/commit/2d48b1a50919), [prysm#9309](https://github.com/OffchainLabs/prysm/pull/9309)

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


<a id="epoch_processing-004"></a>
<details>
<summary><b>epoch_processing-004</b> Flat balances array shared across epoch steps — <i>implemented · low · S · cpu</i></summary>

**Idea.** Extract balances once into a flat array in the epoch-processing context, apply rewards, penalties, deposits, consolidations and effective-balance reads on it with plain arithmetic, and write it back to the tree once at the end. Later steps read the array instead of re-reading or writing balances through the state tree per element.

**Impact.** Same effect as a flat array: one sequential read, all steps share the value, writes are buffered and applied once.

**Best measured result.** saves 165ms with &gt;110000 validators (pr:lodestar#1805)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:243-251`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L243-L251) balances.iter_cow() walked once alongside validators
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:698`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L698) reward/penalty write via make_mut on the same Cow
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:1219`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L1219) pending deposits applied to the same Cow
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:352`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L352) effective balance reads the updated *balance in the same iteration
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/cow.rs:105-118 make_mut inserts into a pending-updates map, applied to the tree in one batch

**Skeptic check.** Confirmed in milhouse that Cow::make_mut buffers writes in an update map that apply_updates flushes in bulk, so this is the batched write-back. Only consolidations and new-validator top-ups re-read by index, for few validators.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#2150](https://github.com/ChainSafe/lodestar/pull/2150), [lodestar#2347](https://github.com/ChainSafe/lodestar/pull/2347), [lodestar#7018](https://github.com/ChainSafe/lodestar/pull/7018), [lodestar@5bf23dc4a](https://github.com/ChainSafe/lodestar/commit/5bf23dc4a664), [lodestar#1805](https://github.com/ChainSafe/lodestar/pull/1805), [lodestar@f4116f4a1](https://github.com/ChainSafe/lodestar/commit/f4116f4a1f41)

</details>


<a id="epoch_processing-005"></a>
<details>
<summary><b>epoch_processing-005</b> Flat or transient inactivity scores with batched write back — <i>implemented · low · S · cpu</i></summary>

**Idea.** Hold inactivity scores in a plain array or fast mutable/transient form for the inactivity update, update them there, and write back changed scores in one batched operation (skip when unchanged). This avoids reading and rebuilding tree paths per validator.

**Impact.** Unchanged scores are not written; changed scores are flushed in one batch.

**Best measured result.** 5x-7x on altair, 3x in perf test (pr:lodestar#3178)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:245`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L245) inactivity_scores.iter_cow()
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:634-664`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L634-L664) process_single_inactivity_update returns early without make_mut when score is 0 and the validator attested
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/cow.rs:105-118 buffered writes applied in bulk

**Skeptic check.** Verified the common case (score 0, attesting) skips the write, and milhouse buffers the rest. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#2721](https://github.com/ChainSafe/lodestar/pull/2721), [lodestar#3178](https://github.com/ChainSafe/lodestar/pull/3178), [lodestar#9911](https://github.com/ChainSafe/lodestar/pull/9911), [lodestar#2921](https://github.com/ChainSafe/lodestar/pull/2921)

</details>


<a id="epoch_processing-006"></a>
<details>
<summary><b>epoch_processing-006</b> Write validators, balances and scores only when values change — <i>implemented · medium · S · cpu, memory, latency</i></summary>

**Idea.** In epoch processing (effective-balance updates, balances, registry, inactivity), read validators read-only and take a mutable reference, copy, or dirty mark only when the value actually changes, skipping validators that cannot cross the hysteresis threshold. Unchanged entries stay shared with the parent state and are not rehashed.

**Impact.** Already done (lighthouse#4573); unchanged entries stay shared with the parent state and are not rehashed.

**Best measured result.** Epoch transition reduced from 5.4s to ~650ms on mainnet (pr:lodestar#2902)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:243-248`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L243-L248) iter_cow over validators, balances, inactivity scores
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:651-661`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L651-L661) inactivity make_mut only on change
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:697`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L697) balance make_mut only if delta non-zero
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:846`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L846),855,881,900 registry make_mut only on eligibility/activation change
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:1077`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L1077) slashing penalty make_mut only when applied
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:1405-1406`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L1405-L1406) effective balance make_mut only when new != old after hysteresis

**Skeptic check.** Checked every make_mut in single_pass.rs; all are behind a change condition. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#7599](https://github.com/OffchainLabs/prysm/pull/7599), [prysm#8743](https://github.com/OffchainLabs/prysm/pull/8743), [lighthouse#4573](https://github.com/sigp/lighthouse/pull/4573), [prysm#9225](https://github.com/OffchainLabs/prysm/pull/9225), [prysm#14124](https://github.com/OffchainLabs/prysm/pull/14124), [silver#146](https://github.com/gattaca-com/silver/pull/146), [prysm#8844](https://github.com/OffchainLabs/prysm/pull/8844), [prysm#16631](https://github.com/OffchainLabs/prysm/pull/16631), [lodestar#2902](https://github.com/ChainSafe/lodestar/pull/2902), [nimbus#3089](https://github.com/status-im/nimbus-eth2/pull/3089), [teku#4256](https://github.com/Consensys-Incorporated/teku/pull/4256), [lodestar#7043](https://github.com/ChainSafe/lodestar/pull/7043)

</details>


<a id="epoch_processing-007"></a>
<details>
<summary><b>epoch_processing-007</b> Field-level read accessors without copying structs — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Provide accessors that read one field (effective balance, finalized epoch) or one validator read-only by index, and use them in hot epoch, unrealized-justification and committee-selection loops instead of copying the whole checkpoint, validator object or validator array. This removes allocations.

**Impact.** Hot epoch, justification and committee/proposer/sync selection loops read single fields by reference with no struct copies.

**Best measured result.** ProcessEpoch 34.9ms-&gt;25.0ms, 23.6MB-&gt;18.8MB, 389k-&gt;291k allocs (pr:prysm#4766)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:2538`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2538) get_effective_balance reads one field through a reference
- [`consensus/types/src/state/beacon_state.rs:1383`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1383) compute_proposer_index uses get_effective_balance
- [`consensus/types/src/state/beacon_state.rs:1811`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1811) get_next_sync_committee_indices reads effective_balance by reference
- [`consensus/types/src/state/beacon_state.rs:3757`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3757) compute_balance_weighted_selection uses get_effective_balance
- [`consensus/state_processing/src/per_epoch_processing/altair/justification_and_finalization.rs:17-23`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/altair/justification_and_finalization.rs#L17-L23) unrealized/realized justification reads cached totals, copies no validators
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:243`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L243) iter_cow yields references; Validator cloned only on make_mut

**Skeptic check.** Audited proposer, sync committee and balance-weighted selection as well as justification; none copy validators. The only non-test validators to_vec found is in a validator_monitor test.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#4766](https://github.com/OffchainLabs/prysm/pull/4766), [prysm#7698](https://github.com/OffchainLabs/prysm/pull/7698), [prysm#16753](https://github.com/OffchainLabs/prysm/pull/16753), [prysm#13656](https://github.com/OffchainLabs/prysm/pull/13656)

</details>


<a id="epoch_processing-008"></a>
<details>
<summary><b>epoch_processing-008</b> Contiguous allocation for per-validator epoch records — <i>n/a · low · S · cpu, memory</i></summary>

**Idea.** Store per-validator precompute records, deltas and read-only wrappers in contiguous value arrays (or reuse one wrapper) instead of one heap object per validator. This removes millions of allocations and improves locality in epoch processing.

**Impact.** Rust structs are already inline and single-pass epoch processing allocates nothing per validator; the Go per-object allocation problem does not exist.

**Best measured result.** ProcessEpoch 5014ms -&gt; 3101ms; InitializePrecomputeValidators 1051ms -&gt; 551ms (pr:prysm#16871)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:120-132`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L120-L132) ValidatorInfo is a by-value stack struct built per validator
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:243-273`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L243-L273) streams validators/balances/scores via iter_cow, no per-validator heap object

**Sources.** [prysm#16871](https://github.com/OffchainLabs/prysm/pull/16871), [prysm#17438](https://github.com/OffchainLabs/prysm/pull/17438)

</details>


<a id="epoch_processing-009"></a>
<details>
<summary><b>epoch_processing-009</b> Hoist per-epoch constants out of validator loops — <i>implemented · low · S · cpu</i></summary>

**Idea.** Compute values that are constant within an epoch (previous epoch, finalized epoch, finality delay, inactivity-leak flag, base_reward/total division, config-derived constants, activation checkpoint) once before the per-validator loop. This avoids repeated getter, lock, division, and copy cost per validator.

**Impact.** Per-epoch constants are hoisted out of the validator loop; only trivial spec field reads remain per validator (get_inactivity_penalty_delta at single_pass.rs:745).

**Best measured result.** ~83ms to ~75ms (pr:lighthouse#3256)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:167-185`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L167-L185) previous/current/next epoch, is_in_inactivity_leak, total_active_balance, churn limits, finalized_checkpoint, fork_name computed once into StateContext
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:226`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L226) RewardsAndPenaltiesContext (participating increments, active_increments) once
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:188`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L188) SlashingsContext once
- [`consensus/state_processing/src/epoch_cache.rs:83-123`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/epoch_cache.rs#L83-L123) base_rewards table built once

**Skeptic check.** Verified StateContext/RewardsAndPenaltiesContext/SlashingsContext are built before the loop at single_pass.rs:247. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#3256](https://github.com/sigp/lighthouse/pull/3256), [prysm#9445](https://github.com/OffchainLabs/prysm/pull/9445), [teku#5785](https://github.com/Consensys-Incorporated/teku/pull/5785), [prysm#5699](https://github.com/OffchainLabs/prysm/pull/5699), [teku#5780](https://github.com/Consensys-Incorporated/teku/pull/5780), [prysm#8757](https://github.com/OffchainLabs/prysm/pull/8757), [lodestar@c39ce160d](https://github.com/ChainSafe/lodestar/commit/c39ce160dc3d), [prysm#14197](https://github.com/OffchainLabs/prysm/pull/14197), [prysm#9334](https://github.com/OffchainLabs/prysm/pull/9334)

</details>


<a id="epoch_processing-010"></a>
<details>
<summary><b>epoch_processing-010</b> Compute sqrt of total balance once per epoch — <i>implemented · low · S · cpu</i></summary>

**Idea.** Compute integer_squareroot(total_active_balance) (base reward quotient) once per epoch transition and pass it into the reward/penalty loop instead of recomputing per validator.

**Impact.** Sqrt is computed once per epoch; per validator base reward is an array lookup.

**Best measured result.** ~20% faster Altair epoch processing (block_sim 8m21s -&gt; 7m54s) (pr:nimbus#2797)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/epoch_cache.rs:94-95`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/epoch_cache.rs#L94-L95) SqrtTotalActiveBalance and BaseRewardPerIncrement computed once in into_epoch_cache
- [`consensus/state_processing/src/epoch_cache.rs:103-112`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/epoch_cache.rs#L103-L112) base_rewards table per effective-balance increment
- [`consensus/types/src/state/epoch_cache.rs:130-140`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/epoch_cache.rs#L130-L140) get_base_reward is a table lookup
- [`consensus/state_processing/src/per_epoch_processing/base/rewards_and_penalties.rs:144`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/base/rewards_and_penalties.rs#L144) phase0 sqrt once per epoch

**Skeptic check.** Confirmed both Altair+ (epoch cache table) and phase0 paths compute the sqrt once. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#2797](https://github.com/status-im/nimbus-eth2/pull/2797), [prysm#2753](https://github.com/OffchainLabs/prysm/pull/2753), [prysm#8945](https://github.com/OffchainLabs/prysm/pull/8945)

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


<a id="epoch_processing-013"></a>
<details>
<summary><b>epoch_processing-013</b> Pass total active balance into base reward computation — <i>implemented · low · S · cpu</i></summary>

**Idea.** Compute total active balance once per epoch pass and pass it into get_base_reward and proposer-reward helpers instead of recomputing it inside each per-validator call. This removes an O(n^2) loop in rewards processing.

**Impact.** No per-validator recomputation of total active balance; O(1) base reward.

**Best measured result.** 10x or more speedup on epoch transitions at mid-thousands of validators; 4k validator state_sim from 3m30s to 1m30s (pr:nimbus#565)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:172`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L172) total_active_balance read once from cache
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:268`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L268) epoch_cache.get_base_reward(index)
- [`consensus/types/src/state/beacon_state.rs:2677-2695`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2677-L2695) get_total_active_balance is a cached lookup

**Skeptic check.** Verified the reward path uses the cached total via StateContext and the epoch-cache base reward table. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus@3c030d945](https://github.com/status-im/nimbus-eth2/commit/3c030d945d4d), [nimbus@8ac613421](https://github.com/status-im/nimbus-eth2/commit/8ac613421d71), [nimbus@6f87c8fd8](https://github.com/status-im/nimbus-eth2/commit/6f87c8fd89ad), [nimbus#561](https://github.com/status-im/nimbus-eth2/pull/561), [nimbus#565](https://github.com/status-im/nimbus-eth2/pull/565)

</details>


<a id="epoch_processing-014"></a>
<details>
<summary><b>epoch_processing-014</b> Per-epoch caches for active indices, count and totals — <i>implemented · low · S · cpu</i></summary>

**Idea.** Cache per-epoch derived values (active validator indices and count, current and previous total active balance, churn limit, proposers, seed) in the state or epoch cache. Epoch and block processing helpers look them up instead of scanning or summing over the registry on each use.

**Impact.** Active indices/count, totals, churn, proposers are cached per epoch; helpers do not rescan the registry.

**Best measured result.** process epoch 96s -&gt; 0.5s at 16324 validators; 5min -&gt; 2.5s at 62500 (pr:prysm#2737)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:2677-2695`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2677-L2695) total active balance cache
- [`consensus/types/src/state/beacon_state.rs:2583-2591`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2583-L2591) churn limit from committee cache active count
- [`consensus/types/src/state/beacon_state.rs:1681-1696`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1681-L1696) post-Fulu proposers read from proposer_lookahead
- [`consensus/state_processing/src/epoch_cache.rs:12-16`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/epoch_cache.rs#L12-L16),83-123 EpochCache effective balances, base rewards, activation queue
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:160-165`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L160-L165) caches initialised before the loop

**Skeptic check.** Remaining uncached scans are get_active_validator_indices for epoch N+2 in process_proposer_lookahead (single_pass.rs:519, inherently a new epoch) and pre-Fulu get_beacon_proposer_index (beacon_state.rs:1665, not on mainnet now). Earlier verdict upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#3096](https://github.com/ChainSafe/lodestar/pull/3096), [teku#1113](https://github.com/Consensys-Incorporated/teku/pull/1113), [teku#700](https://github.com/Consensys-Incorporated/teku/pull/700), [prysm#6254](https://github.com/OffchainLabs/prysm/pull/6254), [nimbus#1089](https://github.com/status-im/nimbus-eth2/pull/1089), [prysm#2737](https://github.com/OffchainLabs/prysm/pull/2737), [nimbus#2981](https://github.com/status-im/nimbus-eth2/pull/2981), [lighthouse@37b8e9f39](https://github.com/sigp/lighthouse/commit/37b8e9f39a50)

</details>


<a id="epoch_processing-015"></a>
<details>
<summary><b>epoch_processing-015</b> Sum next total active balance inside existing loop — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Accumulate next epoch's total active balance inside the existing effective-balance-update or epoch-context validator loop and write it into the cache eagerly. This removes a separate full validator scan, including one on the first block of the next epoch.

**Impact.** Next-epoch total active balance comes from the single pass; first block of next epoch does not rescan.

**Best measured result.** avoids ~350 ms recomputation on first slot of epoch (2.3M validators) (pr:prysm#16738)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/epoch_cache.rs:47-75`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/epoch_cache.rs#L47-L75) PreEpochCache::update_effective_balance accumulates total_active_balance
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:1362`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L1362),1419 called from the effective balance update inside the main loop
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:480-486`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L480-L486) set_total_active_balance(next_epoch) and into_epoch_cache installed eagerly

**Skeptic check.** Verified accumulation in-loop and eager install after consolidations. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#3023](https://github.com/ChainSafe/lodestar/pull/3023), [lodestar#2929](https://github.com/ChainSafe/lodestar/pull/2929), [prysm#16738](https://github.com/OffchainLabs/prysm/pull/16738)

</details>


<a id="epoch_processing-016"></a>
<details>
<summary><b>epoch_processing-016</b> Fuse epoch sub-steps into a single validator pass — <i>partial · low · M · cpu, memory</i></summary>

**Idea.** Merge the per-validator epoch steps (flag rewards/penalties, inactivity, registry updates, slashings, pending deposits/consolidations, effective-balance updates, rotation/exit data) into one or two loops over the validator set, with cached totals and cross-validator state kept outside the loop. The registry is traversed once per epoch with cache-friendly access instead of once per step.

**Gap in Lighthouse.** On Fulu mainnet, process_proposer_lookahead calls get_beacon_proposer_indices -&gt; get_active_validator_indices, a second full validator-registry traversal after process_epoch_single_pass; active-at-N+2 indices could be collected inside the single-pass loop after process_single_registry_update, and compute_proposer_indices could read effective balances from the next PreEpochCache instead of milhouse validators().get. Pending consolidations are also a separate (small) pass.

**Impact.** Saves one registry iteration (~2M validators, likely ~10-20 ms) per epoch transition; the main fusion is already done.

**Best measured result.** Epoch-start block stf mean 912 ms to 709 ms over the preceding summary-pass PR (1503 ms base); about 200 ms saved per epoch-start block (pr:ethlambda#633)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:247-370`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L247-L370) one loop fuses inactivity, rewards, registry updates, slashings, pending deposits, effective balance updates
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:490`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L490) process_proposer_lookahead runs after the loop
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:505-519`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L505-L519) 'TOOO(EIP-7917): use balances cache'; get_beacon_proposer_indices(N+2)
- [`consensus/types/src/state/beacon_state.rs:1699`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1699) get_active_validator_indices full registry scan
- [`consensus/state_processing/src/per_epoch_processing/altair.rs:76`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/altair.rs#L76) rotate_participation_flags separate

**Skeptic check.** The single pass is real and covers the listed steps, but the Fulu proposer-lookahead step re-scans the registry, and the code comment admits it does not use the cache. Earlier evidence called this 'small' and still marked implemented.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [nimbus#5404](https://github.com/status-im/nimbus-eth2/pull/5404), [ethlambda#633](https://github.com/lambdaclass/ethlambda/pull/633), [lighthouse#1228](https://github.com/sigp/lighthouse/pull/1228), [lodestar#2831](https://github.com/ChainSafe/lodestar/pull/2831), [nimbus#2814](https://github.com/status-im/nimbus-eth2/pull/2814), [lighthouse#4483](https://github.com/sigp/lighthouse/pull/4483), [lighthouse#5279](https://github.com/sigp/lighthouse/pull/5279), [lighthouse#5761](https://github.com/sigp/lighthouse/pull/5761)

</details>


<a id="epoch_processing-017"></a>
<details>
<summary><b>epoch_processing-017</b> Cache reward deltas per effective balance value — <i>partial · low · S · cpu</i></summary>

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

**Verdict history.** not (checked) → partial (refuted)

**Sources.** [lodestar#2833](https://github.com/ChainSafe/lodestar/pull/2833)

</details>


<a id="epoch_processing-018"></a>
<details>
<summary><b>epoch_processing-018</b> Cache total slashings sum in epoch cache — <i>implemented · low · S · cpu</i></summary>

**Idea.** Keep the sum of state.slashings in the epoch cache, apply slashing penalties in the rewards pass, and compute the penalty once per distinct effective balance instead of per slashed validator.

**Impact.** Slashings applied in the fused pass with a once-per-epoch sum; per-validator cost is a multiply.

**Best measured result.** processSlashings worstcase 2.65 ms to 96.6 us (377.9 to 10352.7 ops/s) (pr:lodestar#6121)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:1023-1050`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L1023-L1050) SlashingsContext sums slashings once and precomputes penalty_per_effective_balance_increment
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:328`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L328) process_single_slashing inside the main loop
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:1053-1080`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L1053-L1080) per-validator penalty is one mul (Electra)

**Skeptic check.** Not cached across epochs, but the sum is 8192 adds once per epoch, so the effect (no worst-case per-slashed-validator scan) matches. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#6121](https://github.com/ChainSafe/lodestar/pull/6121)

</details>


<a id="epoch_processing-019"></a>
<details>
<summary><b>epoch_processing-019</b> Compute next-epoch shuffling asynchronously — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Compute the next epoch's committee shuffling off the epoch-transition critical path (in a background task) and store it in a shared shuffling cache keyed by epoch and decision root. The transition no longer spends about 1 s computing it inline.

**Impact.** The next-epoch shuffle is off the transition and pre-attestable import path in the normal case.

**Best measured result.** about 1 second of epoch transition spent on nextShuffling moved off critical path (pr:lodestar#6938)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/altair.rs:79`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/altair.rs#L79) advance_caches only rotates; epoch transition does not build the N+2 shuffling (pre-Gloas)
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:333-340`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L333-L340) build_committee_cache(Next) in the background state advance task
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:397-412`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L397-L412) inserted into shuffling_cache keyed by AttestationShufflingId
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4720`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4720),5211-5233 import fallback after the block is attestable, skipped if cached

**Skeptic check.** Verified for Fulu (mainnet). Under Gloas, process_ptc_window (single_pass.rs:539-579) builds the lookahead committee cache inline, but the spec requires it for the PTC window in state, and the result is reused as the Next cache. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#6521](https://github.com/ChainSafe/lodestar/pull/6521), [lodestar#6938](https://github.com/ChainSafe/lodestar/pull/6938), [lodestar#727](https://github.com/ChainSafe/lodestar/pull/727)

</details>


<a id="epoch_processing-020"></a>
<details>
<summary><b>epoch_processing-020</b> Compute shuffling once and reuse committees — <i>implemented · low · S · cpu</i></summary>

**Idea.** Compute the epoch shuffling once as a flat array of active indices, cache it by seed/decision root (check the cache before shuffling), and derive committees and attesting indices from it instead of recomputing committees per lookup or per slot.

**Impact.** None remaining; shuffling computed once per epoch/decision root and committees sliced from the flat array.

**Best measured result.** 4x speedup on epoch processing for 64 validators (commit:nimbus@ced4dbe859c3)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:2824`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2824) build_committee_cache skips rebuild when initialized for the epoch
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:315`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L315) with_cached_shuffling used by attestation verification
- [`consensus/swap_or_not_shuffle/src/shuffle_list.rs:92`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/swap_or_not_shuffle/src/shuffle_list.rs#L92) whole-list shuffle
- [`consensus/state_processing/src/common/get_attesting_indices.rs:25`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/get_attesting_indices.rs#L25) attesting indices from committee slices

**Skeptic check.** Verified the committee cache is built once per epoch and reused, and the ShufflingCache keyed by decision root serves gossip/block attestation paths. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#153](https://github.com/status-im/nimbus-eth2/pull/153), [prysm#5841](https://github.com/OffchainLabs/prysm/pull/5841), [lodestar@4d68bad56](https://github.com/ChainSafe/lodestar/commit/4d68bad56ebe), [nimbus@6cbf355c5](https://github.com/status-im/nimbus-eth2/commit/6cbf355c5a5a), [nimbus@ced4dbe85](https://github.com/status-im/nimbus-eth2/commit/ced4dbe859c3)

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


<a id="epoch_processing-022"></a>
<details>
<summary><b>epoch_processing-022</b> Branchless swaps in swap-or-not shuffle — <i>implemented · medium · S · cpu</i></summary>

**Idea.** Use masked XOR swaps instead of data-dependent branches in the swap-or-not list shuffle, since the swap bit is random and branch mispredictions dominate.

**Impact.** Already done (lighthouse#9630).

**Best measured result.** reverse shuffle 1M elements 210.7 ms -&gt; 82.6 ms; mainnet committee_cache_build 358 ms -&gt; 240 ms (pr:lighthouse#9630)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/swap_or_not_shuffle/src/shuffle_list.rs:54`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/swap_or_not_shuffle/src/shuffle_list.rs#L54) masked_swap XOR mask
- [`consensus/swap_or_not_shuffle/src/shuffle_list.rs:132`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/swap_or_not_shuffle/src/shuffle_list.rs#L132)
- [`consensus/swap_or_not_shuffle/src/shuffle_list.rs:155`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/swap_or_not_shuffle/src/shuffle_list.rs#L155)

**Skeptic check.** Both halves of each round in shuffle_list call masked_swap; no data-dependent branch remains on the production path. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#9630](https://github.com/sigp/lighthouse/pull/9630)

</details>


<a id="epoch_processing-023"></a>
<details>
<summary><b>epoch_processing-023</b> Avoid per-iteration byte conversions in shuffle — <i>implemented · low · S · cpu</i></summary>

**Idea.** In the shuffle loop, avoid converting ints to byte wrappers on every iteration (precompute once) and reuse a single SHA-256 hasher instance.

**Impact.** None on committee shuffling. compute_shuffled_index (used for proposer and sync-committee sampling) hashes for each call, but that is a different algorithm and not a hot loop of byte conversions.

**Best measured result.** profile screenshots only; intToBytes called 25 million times before (pr:teku#7149)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/swap_or_not_shuffle/src/shuffle_list.rs:12-49`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/swap_or_not_shuffle/src/shuffle_list.rs#L12-L49)
- [`consensus/swap_or_not_shuffle/src/shuffle_list.rs:107-135`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/swap_or_not_shuffle/src/shuffle_list.rs#L107-L135)

**Skeptic check.** shuffle_list uses one fixed stack buffer and writes the position bytes in place only on 256-index boundaries, with stateless hash_fixed, so there is no conversion for each item. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#7149](https://github.com/Consensys-Incorporated/teku/pull/7149)

</details>


<a id="epoch_processing-024"></a>
<details>
<summary><b>epoch_processing-024</b> Skip sorting shuffled indices; cache epoch proposers — <i>implemented · low · S · cpu</i></summary>

**Idea.** Read shuffled validator indices directly without sorting them, compute a full epoch of proposer indices once and cache it, and skip computing the active set when only needed for logging.

**Impact.** Proposers are computed once per epoch and cached (and stored in the Fulu state); there is no sort of the shuffled indices and no active-set build that only feeds logging.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:85`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L85) BeaconProposerCache keyed by (epoch, decision root) holds a whole epoch of proposers
- [`consensus/types/src/state/beacon_state.rs:1655`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1655) get_beacon_proposer_index reads proposer_lookahead post-Fulu
- [`consensus/types/src/state/beacon_state.rs:1681`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1681) get_beacon_proposer_indices returns a full epoch from proposer_lookahead
- [`consensus/types/src/state/beacon_state.rs:1700`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1700) pre-Fulu fallback computes active indices once per epoch call

**Skeptic check.** Verified the proposer cache and the Fulu lookahead read paths. The Nimbus sort and logging-only active set have no counterpart in Lighthouse; the pre-Fulu single-slot get_beacon_proposer_index still rescans active indices, but the hot paths go through the epoch cache and the Fulu lookahead.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#1529](https://github.com/status-im/nimbus-eth2/pull/1529), [nimbus@7de05efaa](https://github.com/status-im/nimbus-eth2/commit/7de05efaaf3c)

</details>


<a id="epoch_processing-025"></a>
<details>
<summary><b>epoch_processing-025</b> Keep payload timeliness committee window in state — <i>implemented · medium · S · cpu</i></summary>

**Idea.** Store the PTC assignments window in the beacon state and rotate it during epoch processing, so PTC lookups read it instead of rerunning balance-weighted sampling per call.

**Impact.** Lookups read state.ptc_window; no per-call balance-weighted resampling. Duties endpoint does repeated window reads per validator (noted TODO) but does not resample.

**Best measured result.** Motivated by PayloadCommittee hotspot (~18-20% CPU) seen in profiling (pr:prysm#16573)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:539`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L539) process_ptc_window pop_front + compute one new epoch
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:493`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L493)
- [`consensus/types/src/state/beacon_state.rs:3591`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3591) get_ptc reads ptc_window
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1768`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1768) compute_ptc_duties TODO: per-validator get_ptc_assignment is O(N*slots*PTCSize)

**Skeptic check.** Verified get_ptc indexes the window and compute_ptc (resampling) has no production callers outside window building. The duties API path is inefficient (beacon_chain.rs:1768 TODO) but that is a different issue from resampling.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#9211](https://github.com/ChainSafe/lodestar/pull/9211), [prysm#16573](https://github.com/OffchainLabs/prysm/pull/16573)

</details>


<a id="epoch_processing-026"></a>
<details>
<summary><b>epoch_processing-026</b> Update proposer lookahead in place — <i>partial · low · S · cpu, memory</i></summary>

**Idea.** In process_proposer_lookahead, shift the existing lookahead vector and fill only the tail instead of rebuilding it from scratch.

**Gap in Lighthouse.** process_proposer_lookahead copies the whole 64-entry vector into a Vec and rebuilds a milhouse Vector instead of mutating the existing one in place; could use get_mut on the Vector for the two shifts.

**Impact.** Saves a 64-element copy and tree rebuild once per epoch: microseconds.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:510`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L510) clones lookahead to Vec, copy_within shift, fill tail, then Vector::new at :530

**Sources.** [teku#9877](https://github.com/Consensys-Incorporated/teku/pull/9877)

</details>


<a id="epoch_processing-027"></a>
<details>
<summary><b>epoch_processing-027</b> Compute fork-dependent epoch data once after upgrade — <i>implemented · low · S · cpu</i></summary>

**Idea.** At a fork boundary, compute epoch data that depends on the upgraded state (such as proposers for current and next epoch) once after the upgrade instead of before and after.

**Impact.** Lighthouse epoch processing does not compute proposers eagerly, so there is no pre-upgrade proposer computation to duplicate. Fork boundary only, a rare path.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_slot_processing.rs:96`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_slot_processing.rs#L96) fork upgrades run after epoch processing and slot increment
- [`consensus/state_processing/src/upgrade/fulu.rs:20`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/upgrade/fulu.rs#L20) initialize_proposer_lookahead computes current and next epoch proposers once during the upgrade
- [`consensus/state_processing/src/per_slot_processing.rs:124`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_slot_processing.rs#L124) build_caches once after all upgrades

**Skeptic check.** Confirmed: Lodestar's double computation came from its afterProcessEpoch eagerly filling proposers. Lighthouse computes them lazily (proposer cache) or only in initialize_proposer_lookahead, once.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#8086](https://github.com/ChainSafe/lodestar/pull/8086)

</details>


<a id="epoch_processing-028"></a>
<details>
<summary><b>epoch_processing-028</b> Bulk participation rotation and reset at epoch boundary — <i>partial · medium · M · cpu, memory</i></summary>

**Idea.** At the epoch boundary, rotate current to previous participation by moving or bulk-copying the list or reusing its tree nodes, and replace the current list with a prebuilt zero-filled list or tree of packed zero leaves. This avoids per-validator rebuilds and per-element zeroing.

**Gap in Lighthouse.** BeaconState::rotate_participation_flags for Gloas/Heze rebuilds current_epoch_participation via ProgressiveList::try_from_iter over num_validators elements; milhouse ProgressiveList/ProgressiveTree lacks a repeat-style constructor sharing zero subtrees. This is exactly the path lodestar#9671 optimized (progressive participation rotation for EIP-7688).

**Impact.** One O(n) leaf build plus later hashing of a fresh tree per epoch on Gloas (~1M validators, ~32K packed leaves); low tens of ms per epoch transition once Gloas ships.

**Best measured result.** epochTransition 28.7 -&gt; 34.5 ops/s (pr:teku#5349)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:2283`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2283) rotate_basic: mem::take + List::repeat (shared zero subtrees) for Altair..Fulu
- [`consensus/types/src/state/beacon_state.rs:2301`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2301) Gloas: ProgressiveList::try_from_iter(repeat_n(default, n)) builds every leaf
- [`consensus/types/src/state/beacon_state.rs:2308`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2308) Heze: same per-element build
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/progressive_list.rs:36 ProgressiveList has only try_from_iter/new/empty, no repeat constructor

**Skeptic check.** Pre-Gloas rotation is O(1) move plus List::repeat, as the earlier check said. Gloas is not scheduled on mainnet (GLOAS_FORK_EPOCH far future) but it is the next fork and the member PR lodestar#9671 targets exactly this progressive-list path, so partial rather than implemented.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [teku#5349](https://github.com/Consensys-Incorporated/teku/pull/5349), [teku#5774](https://github.com/Consensys-Incorporated/teku/pull/5774), [silver#144](https://github.com/gattaca-com/silver/pull/144), [lodestar#9671](https://github.com/ChainSafe/lodestar/pull/9671), [prysm#8669](https://github.com/OffchainLabs/prysm/pull/8669)

</details>


<a id="epoch_processing-029"></a>
<details>
<summary><b>epoch_processing-029</b> Fast construction of zero-filled arrays — <i>n/a · low · S · cpu</i></summary>

**Idea.** Allocate zero-filled per-validator arrays with a native zeroed constructor rather than generic fill/map loops.

**Impact.** Rust vec![0; n] uses calloc and the single-pass epoch loop avoids per-validator side arrays; JS typed-array issue.

**Best measured result.** saves ~95ms per epoch on Prater (pr:lodestar#2344)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:188`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L188) single pass uses no per-validator zero arrays

**Sources.** [lodestar#2344](https://github.com/ChainSafe/lodestar/pull/2344)

</details>


<a id="epoch_processing-030"></a>
<details>
<summary><b>epoch_processing-030</b> Do not allocate throwaway zero arrays or caches — <i>n/a · low · S · cpu, memory</i></summary>

**Idea.** In epoch processing, reuse the caller's cache and avoid constructing, returning and discarding zero-filled arrays or empty caches.

**Impact.** Single-pass epoch processing has no discarded zero arrays or throwaway caches; Nim scaffolding concern.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:188`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L188) contexts built once and passed by reference

**Sources.** [nimbus@35f67cec6](https://github.com/status-im/nimbus-eth2/commit/35f67cec603d)

</details>


<a id="epoch_processing-031"></a>
<details>
<summary><b>epoch_processing-031</b> Sparse storage of slashing penalties — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** Store slashing penalties as one entry per slashed index alongside the index list, instead of a registry-sized array indexed by validator that must be allocated and zeroed.

**Impact.** No registry-sized penalty array exists on either the Altair+ or the phase0 path.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:1053`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L1053) process_single_slashing computes the penalty inline in the single pass
- [`consensus/state_processing/src/per_epoch_processing/slashings.rs:26`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/slashings.rs#L26) phase0 path collects only (index, effective_balance) of matching slashed validators

**Skeptic check.** Verified both slashing paths: the single pass applies the penalty per validator in place, and the base path keeps a sparse Vec of matching indices. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@b01424a11](https://github.com/ChainSafe/lodestar/commit/b01424a11f64)

</details>


<a id="epoch_processing-032"></a>
<details>
<summary><b>epoch_processing-032</b> Return early from process_slashings when none apply — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Skip the process_slashings validator loop (and any copy-on-write of the validator list) when no validator is slashed with a withdrawable epoch at the midpoint.

**Impact.** No separate loop and no copy-on-write when nothing applies.

**Best measured result.** heap flame graph shows validator copies; no numbers (pr:prysm#7587)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:327`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L327) slashings fused into the single validator pass
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:1060`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L1060) make_mut only when slashed and withdrawable epoch matches

**Skeptic check.** Verified process_single_slashing only mutates the balance Cow under the slashing condition; the validator list is not copied. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#2943](https://github.com/ChainSafe/lodestar/pull/2943), [prysm#7587](https://github.com/OffchainLabs/prysm/pull/7587), [prysm#7544](https://github.com/OffchainLabs/prysm/pull/7544)

</details>


<a id="epoch_processing-033"></a>
<details>
<summary><b>epoch_processing-033</b> Exit queue cache instead of registry scans — <i>implemented · low · S · cpu</i></summary>

**Idea.** Keep a cache of the max exit epoch and its churn count, updated incrementally per exit, so initiate_validator_exit does not scan the whole validator registry for each exit.

**Impact.** Exit queue lookups O(1) after one build; Electra needs no scan.

**Best measured result.** no numbers; labeled optimization (pr:prysm#12737)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/common/initiate_validator_exit.rs:19`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/initiate_validator_exit.rs#L19) build_exit_cache (no-op if built)
- [`consensus/state_processing/src/common/initiate_validator_exit.rs:28`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/initiate_validator_exit.rs#L28) max_epoch/get_churn_at from cache
- [`consensus/state_processing/src/common/initiate_validator_exit.rs:46`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/initiate_validator_exit.rs#L46) record_validator_exit incremental update
- [`consensus/state_processing/src/common/initiate_validator_exit.rs:24`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/initiate_validator_exit.rs#L24) Electra: compute_exit_epoch_and_update_churn uses state fields

**Skeptic check.** Confirmed initiate_validator_exit reads the ExitCache and updates it per exit rather than scanning the registry. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@5394726ca](https://github.com/sigp/lighthouse/commit/5394726caffb), [prysm#12737](https://github.com/OffchainLabs/prysm/pull/12737), [nimbus#6144](https://github.com/status-im/nimbus-eth2/pull/6144)

</details>


<a id="epoch_processing-034"></a>
<details>
<summary><b>epoch_processing-034</b> Bounded heap for activation queue selection — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** In registry updates, keep only the top churn-limit activation candidates in a bounded heap keyed by (eligibility epoch, index), instead of collecting and sorting all eligible validators.

**Impact.** No collect-and-sort over the registry; ordered set of candidates built during the pass.

**Best measured result.** registry update avg 26ms to 17ms; ~35% faster registry processing (pr:nimbus#5412)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/activation_queue.rs:17`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/activation_queue.rs#L17) BTreeSet&lt;(eligibility_epoch, index)&gt;
- [`consensus/types/src/state/activation_queue.rs:36`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/activation_queue.rs#L36) get_validators_eligible_for_activation takes first churn_limit
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:310`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L310) registry updates in the single pass

**Skeptic check.** Not a bounded heap, but the ordered BTreeSet of candidates only, filled during the existing single pass, gives the same effect; post-Electra the churn queue is in state. Earlier verdict upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#5412](https://github.com/status-im/nimbus-eth2/pull/5412)

</details>


<a id="epoch_processing-035"></a>
<details>
<summary><b>epoch_processing-035</b> Track participation incrementally during block processing — <i>implemented · low · S · cpu</i></summary>

**Idea.** Update per-validator participation flags and inclusion data as attestations are processed in blocks, so epoch processing needs no pass over pending attestations.

**Impact.** Altair+ epoch processing does no pass over attestations. Only historical phase0 states still scan pending attestations.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/process_operations.rs:257`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L257) epoch participation flags are set as block attestations are processed
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:282`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L282) update_progressive_balances_on_attestation tallies flag balances incrementally
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:226`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L226) RewardsAndPenaltiesContext reads the progressive balances, with no pass over attestations

**Skeptic check.** Confirmed that block processing updates the flags and the progressive balances cache, and that epoch processing consumes them. The phase0 scan is inherent to the phase0 state format and is irrelevant today.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#2384](https://github.com/ChainSafe/lodestar/pull/2384)

</details>


<a id="epoch_processing-036"></a>
<details>
<summary><b>epoch_processing-036</b> Track participation total balances incrementally — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Maintain current/previous epoch per-flag (including target) unslashed participating balance totals incrementally as each block's attestations are processed (progressive balances). Justification/finalization at the epoch boundary then reads the totals instead of scanning all validators; enable it by default without a from-scratch recheck.

**Impact.** Already done (lighthouse#4971), always on.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/progressive_balances_cache.rs:160`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/progressive_balances_cache.rs#L160) incremental on_new_attestation/on_slashing/on_effective_balance_change
- [`consensus/state_processing/src/per_epoch_processing/altair/justification_and_finalization.rs:16`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/altair/justification_and_finalization.rs#L16) J&amp;F reads cached target balances
- [`consensus/types/src/state/progressive_balances_cache.rs:293`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/progressive_balances_cache.rs#L293) enabled for all Altair+ states

**Skeptic check.** Verified J&amp;F reads previous/current target attesting balance from the cache with no from-scratch recomputation. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#6747](https://github.com/Consensys-Incorporated/teku/pull/6747), [teku#5963](https://github.com/Consensys-Incorporated/teku/pull/5963), [teku#5993](https://github.com/Consensys-Incorporated/teku/pull/5993), [lighthouse#4971](https://github.com/sigp/lighthouse/pull/4971), [teku#6804](https://github.com/Consensys-Incorporated/teku/pull/6804), [teku#6958](https://github.com/Consensys-Incorporated/teku/pull/6958), [teku#6993](https://github.com/Consensys-Incorporated/teku/pull/6993), [lodestar#4294](https://github.com/ChainSafe/lodestar/pull/4294), [lodestar#4205](https://github.com/ChainSafe/lodestar/pull/4205), [teku#5904](https://github.com/Consensys-Incorporated/teku/pull/5904)

</details>


<a id="epoch_processing-037"></a>
<details>
<summary><b>epoch_processing-037</b> Cache total attester balance for fork choice — <i>implemented · low · S · cpu</i></summary>

**Idea.** Compute total committee (attester) balance once per state and cache it so fork-choice proposer-boost weighting reads it instead of summing validator balances each time.

**Impact.** Proposer boost and re-org thresholds are O(1) per use.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/justified_balances.rs:23`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/justified_balances.rs#L23) from_justified_state sums total_effective_balance once per justified state
- [`consensus/proto_array/src/proto_array.rs:2391`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L2391) calculate_committee_fraction reads the cached total_effective_balance
- [`consensus/proto_array/src/proto_array.rs:2408`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L2408) proposer boost score uses calculate_committee_fraction

**Skeptic check.** Verified that the total is computed when JustifiedBalances is built and is reused by every committee-fraction call (boost, re-org thresholds).

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#3677](https://github.com/Consensys-Incorporated/teku/pull/3677)

</details>


<a id="epoch_processing-038"></a>
<details>
<summary><b>epoch_processing-038</b> Precompute next epoch transition and caches before the boundary — <i>implemented · high · S · latency, cpu</i></summary>

**Idea.** Late in the last slot of an epoch (or during idle time before it), advance a copy of the head state through the epoch transition off the critical path and locks, building committee caches and total attester balances, and cache the result. The first block of the new epoch and duty queries then find the post-epoch state and caches ready instead of stalling on them.

**Impact.** First block of the new epoch and duty queries find the post-epoch state, committee caches and shufflings ready; already in place.

**Best measured result.** epoch transition 467 ms p50 under lock (target removed); head 0.3-0.5 s later than peers (pr:caplin#25473)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:121-123`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L121-L123) timer fires at 3/4 of each slot
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:283-286`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L283-L286) clone of head state from get_advanced_hot_state
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:291`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L291) per_slot_processing (runs the epoch transition at the boundary) outside import locks
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:335-341`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L335-L341) builds Current and Next committee caches
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:351-409`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L351-L409) primes the proposer cache and the shuffling_cache
- [`beacon_node/beacon_chain/src/block_verification.rs:2065`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L2065) block import loads the pre-advanced parent state

**Skeptic check.** Verified that advance_head runs the epoch transition on a copy of the head state at 9s into the last slot, then primes the caches. Block import and production read the result through get_advanced_hot_state. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#3698](https://github.com/Consensys-Incorporated/teku/pull/3698), [caplin#25473](https://github.com/erigontech/erigon/pull/25473), [lodestar#3383](https://github.com/ChainSafe/lodestar/pull/3383), [teku#3399](https://github.com/Consensys-Incorporated/teku/pull/3399)

</details>


<a id="epoch_processing-039"></a>
<details>
<summary><b>epoch_processing-039</b> Reuse unrealized-finality balances in epoch transition — <i>implemented · low · S · cpu</i></summary>

**Idea.** Cache the participating-balance totals computed for unrealized justification/finality on block receipt and reuse them when the real epoch transition runs on the same data.

**Impact.** There is no participating-balance scan to deduplicate. Both paths read the O(1) progressive totals.

**Best measured result.** saves ~10ms of epoch processing time (pr:nimbus#8216)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fork_choice/src/fork_choice.rs:954`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L954) on_block unrealized J&amp;F calls altair::process_justification_and_finalization
- [`consensus/state_processing/src/per_epoch_processing/altair/justification_and_finalization.rs:17-23`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/altair/justification_and_finalization.rs#L17-L23) reads the totals from progressive_balances_cache, with no scan
- [`consensus/state_processing/src/per_epoch_processing/altair.rs:35`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/altair.rs#L35),39 the real transition reuses the already-initialized progressive cache
- [`consensus/state_processing/src/common/update_progressive_balances_cache.rs:20-24`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/update_progressive_balances_cache.rs#L20-L24) initialize is a no-op when the cache is already initialized
- [`consensus/fork_choice/src/fork_choice.rs:934-946`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L934-L946) reuses the parent's unrealized checkpoints when possible

**Skeptic check.** Nimbus caches the participating balances so it does not recompute them. Lighthouse keeps them incrementally in the progressive balances cache, which both the unrealized and the real J&amp;F read. This gives the same effect. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#8216](https://github.com/status-im/nimbus-eth2/pull/8216)

</details>


<a id="epoch_processing-040"></a>
<details>
<summary><b>epoch_processing-040</b> Byte lookup table for aggregation bit reads — <i>n/a · low · cpu</i></summary>

**Idea.** Read attestation aggregation bits via a precomputed 256-entry byte-to-bits table and per-bit accessors instead of materializing boolean arrays in epoch status loops.

**Impact.** Aggregation bits are only read in epoch processing for phase0 (base validator_statuses), which is long past on mainnet; Lighthouse's Altair+ path uses flag bytes.

**Best measured result.** epoch transition 3.5s -&gt; 1.5s; aggregation bit access 14.5s -&gt; 3.1s (pr:lodestar#2510)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/attestation/participation_flags.rs:25`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/attestation/participation_flags.rs#L25) - Altair+ epoch loops read per-validator ParticipationFlags bytes, not aggregation bits
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:141`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L141) - has_flag

**Sources.** [lodestar#2510](https://github.com/ChainSafe/lodestar/pull/2510)

</details>


<a id="epoch_processing-041"></a>
<details>
<summary><b>epoch_processing-041</b> Columnar per-field scans of validator data — <i>not · low · L · cpu</i></summary>

**Idea.** Store validator data as per-field columns and scan only the needed columns in epoch processing, instead of assembling a per-validator row struct with random access.

**Gap in Lighthouse.** Would need split validator storage (separate effective_balance/slashed/exit-epoch columns) in types::BeaconState and milhouse; rewrite process_epoch_single_pass loops.

**Impact.** Epoch processing scans less memory, perhaps tens of percent of the validator loop, but the single pass already touches each validator once; large redesign.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:243`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L243) iter_cow over milhouse validator List of Validator structs
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:155`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L155) process_epoch_single_pass visits whole Validator per index

**Sources.** [silver#119](https://github.com/gattaca-com/silver/pull/119)

</details>


<a id="epoch_processing-042"></a>
<details>
<summary><b>epoch_processing-042</b> Precomputed attester hash sets for membership tests — <i>n/a · low · cpu</i></summary>

**Idea.** Compute attesting indices once per pending attestation using the shared committee cache and store them in hash sets, so attester membership checks in epoch reward loops are O(1) instead of linear list scans per validator.

**Impact.** Phase0 pending attestations do not exist after Altair; Lighthouse already uses per-validator statuses.

**Best measured result.** Epoch 10240 validators 1.155-&gt;0.892 s/op (pr:teku#1114)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/base/validator_statuses.rs:261`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/base/validator_statuses.rs#L261) phase0 path computes attesting indices once per attestation and updates a per-validator status vec (no linear membership scans)

**Sources.** [teku#1114](https://github.com/Consensys-Incorporated/teku/pull/1114), [nimbus@36f15a368](https://github.com/status-im/nimbus-eth2/commit/36f15a368869), [nimbus@d84aa45a2](https://github.com/status-im/nimbus-eth2/commit/d84aa45a227b)

</details>


<a id="epoch_processing-043"></a>
<details>
<summary><b>epoch_processing-043</b> Linear deduplication of attester index sets — <i>n/a · low · cpu, memory</i></summary>

**Idea.** Collect attester indices directly into a (sorted) unique set, or dedupe with a linear hash/sort-based pass, instead of concatenating per-attestation lists and doing O(n^2) or post-hoc deduplication in epoch helpers.

**Impact.** Phase0-only code, not on mainnet runtime.

**Best measured result.** deduplicate was 45.16% of profile (pr:nimbus#221)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/base/validator_statuses.rs:294`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/base/validator_statuses.rs#L294) per-validator status vec, no list concatenation or dedup

**Sources.** [teku#704](https://github.com/Consensys-Incorporated/teku/pull/704), [lodestar@bbd6d0009](https://github.com/ChainSafe/lodestar/commit/bbd6d0009192), [nimbus#221](https://github.com/status-im/nimbus-eth2/pull/221), [nimbus@d74fa2027](https://github.com/status-im/nimbus-eth2/commit/d74fa2027aec)

</details>


<a id="epoch_processing-044"></a>
<details>
<summary><b>epoch_processing-044</b> Incrementally hashed balances trie — <i>implemented · low · S · cpu</i></summary>

**Idea.** Keep validator balances in an incrementally hashed trie so the state root after epoch processing rehashes only changed balance chunks.

**Impact.** Milhouse List&lt;u64&gt; caches the hash of each node, so the state root rehashes only the dirty subtrees. Most balances change every epoch anyway.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:244`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L244) balances.iter_cow() mutates only the changed leaves, so the tree structure is shared
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:697`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L697) a balance is made mutable only when delta is non-zero

**Skeptic check.** Confirmed that the copy-on-write iteration writes only when a balance changes, and that milhouse keeps a hash per tree node. This is the same incremental-trie effect as the Prysm PR.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#10112](https://github.com/OffchainLabs/prysm/pull/10112)

</details>


<a id="epoch_processing-045"></a>
<details>
<summary><b>epoch_processing-045</b> Inline hot arithmetic helpers — <i>implemented · low · S · cpu</i></summary>

**Idea.** Mark thin checked-arithmetic and integer-division helper functions as inline so hot epoch-processing loops compile to direct ops instead of calls.

**Impact.** Already inlined. PR 3229 is the source change.

**Best measured result.** epoch transition 398ms to 359ms (9.77%) (pr:lighthouse#3229)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/safe_arith-0.1.0/src/lib.rs:90,139-169 #[inline] on every checked-arithmetic impl
- Cargo.toml:286-290 maxperf profile has fat LTO and codegen-units=1
- [`.github/workflows/release.yml:41`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/.github/workflows/release.yml#L41),44 release binaries are built with maxperf

**Skeptic check.** safe_arith has #[inline] on every op. The Slot/Epoch SafeArith impls at consensus/types/src/core/slot_epoch_macros.rs:67 have no #[inline], and one is called per validator at single_pass.rs:265. Released binaries use fat LTO, so this has no real effect.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#3229](https://github.com/sigp/lighthouse/pull/3229), [lodestar#2345](https://github.com/ChainSafe/lodestar/pull/2345)

</details>


<a id="epoch_processing-046"></a>
<details>
<summary><b>epoch_processing-046</b> Fast path for small checked multiplication — <i>n/a · low · cpu</i></summary>

**Idea.** In checked u64 multiplication, use a fast path when the multiplier is small and the other operand cannot overflow, avoiding the slow wide-integer path in reward math.

**Impact.** Rust has native u64 checked_mul; no wide-integer slow path exists.

**Best measured result.** Not a huge performance gain (pr:teku#3372)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:667`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L667) reward math uses native u64 safe_mul

**Sources.** [teku#3372](https://github.com/Consensys-Incorporated/teku/pull/3372)

</details>


<a id="epoch_processing-047"></a>
<details>
<summary><b>epoch_processing-047</b> Faster phase0-to-Altair state upgrade — <i>n/a · low · cpu</i></summary>

**Idea.** Optimize the upgrade_to_altair conversion of pending attestations to participation flags to avoid slow per-attestation work.

**Impact.** Phase0-to-Altair upgrade never runs on mainnet nodes any more.

**Best measured result.** epoch slot with block avg 5420 ms -&gt; 1790 ms (60k validators) (pr:nimbus#2679)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/upgrade/altair.rs:49`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/upgrade/altair.rs#L49) upgrade_to_altair, run once at the long-past fork

**Sources.** [nimbus#2679](https://github.com/status-im/nimbus-eth2/pull/2679)

</details>


<a id="epoch_processing-048"></a>
<details>
<summary><b>epoch_processing-048</b> Nimbus processEpoch redundant-work cleanup — <i>implemented · low · S · cpu</i></summary>

**Idea.** Remove redundant work in epoch-processing helpers (exact change not recorded) so processEpoch runs several times faster.

**Impact.** Lighthouse already reuses active validator indices and loop-invariant totals.

**Best measured result.** processEpoch 5x faster, total 2x faster with 16k validators (pr:nimbus#157)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/altair.rs:29-34`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/altair.rs#L29-L34) builds the committee caches (active indices) and the total active balance cache once
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:226`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L226) RewardsAndPenaltiesContext computes the shared values once, outside the validator loop
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:243-262`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L243-L262) one fused validator pass

**Skeptic check.** The diff of nimbus#157 shows the mechanism: compute active_validator_indices once and reuse it for ejections, and move the committee total and attesting balances out of the per-member loop (pre-phase0 crosslinks). Lighthouse caches active indices and the total active balance, and computes the reward context once. Upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#157](https://github.com/status-im/nimbus-eth2/pull/157)

</details>


<a id="epoch_processing-049"></a>
<details>
<summary><b>epoch_processing-049</b> Nimbus epoch hot-loop optimization — <i>n/a · low · S · cpu</i></summary>

**Idea.** Optimize hot loops in epoch processing (details not recorded in the source).

**Impact.** Not verifiable: the source records no mechanism.

**Best measured result.** 8x speedup on epoch processing for 64 validators (pr:nimbus#215)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:243-262`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L243-L262) fused hot loop with iter_cow cursors

**Skeptic check.** nimbus#215 has no diff and its description says only 'Ugly. Effective.', and it targets a 2019 pre-phase0 spec with 64 validators. There is nothing concrete to compare against. Calling it implemented is a generic match, not a verification.

**Verdict history.** implemented (checked) → n/a (skeptic)

**Sources.** [nimbus#215](https://github.com/status-im/nimbus-eth2/pull/215)

</details>


<a id="epoch_processing-050"></a>
<details>
<summary><b>epoch_processing-050</b> Caplin rewards and penalties speedup — <i>implemented · low · S · cpu</i></summary>

**Idea.** Speed up rewards and penalties processing in the epoch transition (mechanism not recorded).

**Impact.** The Erigon PR precomputes the per-flag totals once and merges the flag loops into one validator loop. Lighthouse does both, and gets the totals from an incremental cache with no validator scan at all.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:667`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L667) process_single_reward_and_penalty merges all flag deltas and the inactivity penalty per validator
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:762`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L762) RewardsAndPenaltiesContext::new precomputes the per-flag unslashed participating increments from the progressive balances

**Skeptic check.** Read the Caplin diff (the per-flag totals are computed once and the per-flag loops are merged into one) and the matching Lighthouse single-pass code. The earlier verdict is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#6958](https://github.com/erigontech/erigon/pull/6958)

</details>


<a id="epoch_processing-051"></a>
<details>
<summary><b>epoch_processing-051</b> Feature flag to skip crosslink processing — <i>n/a · low · S · cpu, latency</i></summary>

**Idea.** Allow disabling unneeded crosslink/shard processing in the state transition when it cannot fit in a slot.

**Impact.** Crosslinks were removed from the spec in phase 0 finalization; nothing to skip.

**Best measured result.** unoptimized crosslinks overflowed slot duration (pr:prysm#2075)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:155`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L155) single-pass epoch has no crosslink stage

**Sources.** [prysm#2075](https://github.com/OffchainLabs/prysm/pull/2075)

</details>


<a id="epoch_processing-052"></a>
<details>
<summary><b>epoch_processing-052</b> Structural equality instead of per-item hash tree root — <i>n/a · low · S · cpu</i></summary>

**Idea.** When filtering attestations by crosslink or similar containers, compare with structural equality against the already fetched value instead of computing a hash tree root per item.

**Impact.** Crosslink attestations no longer exist; no per-item hash_tree_root comparison to replace.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:155`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L155) no crosslink attestation filtering

**Sources.** [lodestar@330b39ef4](https://github.com/ChainSafe/lodestar/commit/330b39ef40ac)

</details>


<a id="epoch_processing-053"></a>
<details>
<summary><b>epoch_processing-053</b> Compute historical batch root without temp object — <i>n/a · low · S · cpu, memory</i></summary>

**Idea.** In final epoch updates, compute the historical batch root directly instead of building and copying a large temporary HistoricalBatch object.

**Impact.** Only affects pre-Capella forks, never run on a mainnet node at head.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/historical_roots_update.rs:17`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/historical_roots_update.rs#L17) only pre-Capella historical_batch root, post-Capella uses historical summaries

**Sources.** [nimbus#925](https://github.com/status-im/nimbus-eth2/pull/925)

</details>


<a id="epoch_processing-054"></a>
<details>
<summary><b>epoch_processing-054</b> Reuse an already fetched validator — <i>implemented · low · S · cpu</i></summary>

**Idea.** In per-validator epoch code (participation cache build, pending consolidations), reuse the validator already fetched instead of calling get_validator again, saving a tree lookup.

**Impact.** There is no duplicate validator lookup in pending consolidations or in the main pass.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:1269`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L1269) process_pending_consolidations fetches source_validator once and reuses its effective_balance at :1283
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:243`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L243) validators.iter_cow() visits each validator once in the main pass
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:1138`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L1138) get_validator for a deposit pubkey, fetched once per deposit

**Skeptic check.** Verified the exact Lodestar #7641 case: the Lighthouse pending-consolidations code reads source_validator.effective_balance from the already fetched validator. The participation cache from #4608 was replaced by single-pass processing.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#7641](https://github.com/ChainSafe/lodestar/pull/7641), [lighthouse#4608](https://github.com/sigp/lighthouse/pull/4608)

</details>


<a id="epoch_processing-055"></a>
<details>
<summary><b>epoch_processing-055</b> Append new validator caches in place — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** When the per-validator effective-balance cache is uniquely owned (freshly cloned at epoch start), append new validators in place instead of copying the whole array per deposit.

**Impact.** There is no per-deposit full array copy to avoid.

**Best measured result.** Napkin math: 16 copies of ~1.9 MiB, about 30.5 MiB moved per epoch avoided (commit:lodestar@bc748d841e53)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/epoch_cache.rs:41-45`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/epoch_cache.rs#L41-L45) effective_balances Vec::with_capacity(validators.len())
- [`consensus/state_processing/src/epoch_cache.rs:53-58`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/epoch_cache.rs#L53-L58) append in place when index == len
- [`consensus/types/src/state/beacon_state.rs:2443-2470`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2443-L2470) deposits push to milhouse lists and insert into the pubkey cache; the EpochCache is not copied per deposit

**Skeptic check.** The per-epoch effective-balance cache is built once, with capacity, and appended to in place. Block-level deposits do not touch the Arc'd EpochCache, and the pubkey cache insert does not copy it. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@bc748d841](https://github.com/ChainSafe/lodestar/commit/bc748d841e53)

</details>


<a id="epoch_processing-056"></a>
<details>
<summary><b>epoch_processing-056</b> Fixed-size tail for new compounding flags — <i>n/a · low · S · memory</i></summary>

**Idea.** Track flags for new compounding validators as a base plus a fixed-size tail (deposits per epoch are capped) instead of a growing process-global reused array.

**Impact.** Lodestar's flags array is specific to its epoch cache design; Lighthouse derives compounding from credentials per validator and keeps no growing global array.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:199`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L199) get_validators_in_consolidations builds a BTreeSet of consolidating indices, no process-global reused array
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:1383`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L1383) compounding handled per validator in effective balance update

**Sources.** [lodestar@367b69f0e](https://github.com/ChainSafe/lodestar/commit/367b69f0e881)

</details>


<a id="epoch_processing-057"></a>
<details>
<summary><b>epoch_processing-057</b> Cache next-epoch boundary state per block root — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Cache one advanced post-state per (block root, epoch) so tick, attestation and block production reuse it instead of recomputing the epoch transition; advance multi-epoch gaps in one jump.

**Impact.** The tick, block import, block production and attestation paths share one advanced state per head root. Non-head targets cache the shuffling instead of the state.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1124-1130`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1124-L1130) get_advanced_hot_state serves a cached advanced state by (block_root, max_slot)
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:283-291`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L283-L291) the advanced head state goes into state_cache
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5421`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5421) block production reuses it
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2161-2164`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2161-L2164) the attestation path reuses it, with partial_state_advance for gaps
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:437-454`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L437-L454) non-head targets: partial advance, then the committee is cached in shuffling_cache

**Skeptic check.** Verified that the state advanced by the timer is cached by block root and reused by import, production and attestation. For multi-slot gaps, partial_state_advance skips the intermediate state roots. Epoch transitions cannot be skipped. The diff of silver#238 was truncated, so the comparison uses its description.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [silver#238](https://github.com/gattaca-com/silver/pull/238)

</details>


<a id="epoch_processing-058"></a>
<details>
<summary><b>epoch_processing-058</b> Transfer epoch cache only across epoch boundary — <i>implemented · low · S · cpu</i></summary>

**Idea.** In state pre-computation, transfer/clone the epoch cache only when the advance crosses an epoch boundary, since doing it on every slot made block transitions slower.

**Impact.** None; caches live in the state as Arc and are rebuilt/rotated only at epoch boundaries, so a per-slot advance carries no cache-transfer cost.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_slot_processing.rs:49-54`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_slot_processing.rs#L49-L54)
- [`consensus/types/src/state/beacon_state.rs:825`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L825)
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:335-343`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L335-L343)

**Skeptic check.** Lighthouse has no separate epoch-context transfer: committee caches are Arc&lt;CommitteeCache&gt; inside BeaconState, so clones are refcount bumps and epoch work runs only at the boundary. The earlier evidence is right; this is closer to n/a by design than to a port of the Lodestar change.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#6102](https://github.com/ChainSafe/lodestar/pull/6102)

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


<a id="epoch_processing-060"></a>
<details>
<summary><b>epoch_processing-060</b> Sequential bulk iteration over validator and balance lists — <i>implemented · medium · S · cpu, memory</i></summary>

**Idea.** When epoch processing scans the validator registry or participation/balance lists, iterate the backing structure sequentially (tree-leaf, column or bulk forEach/getAll iterator) instead of calling an indexed getter per validator or allocating a view per element. Each indexed get costs a tree descent.

**Impact.** The full-registry scans in epoch processing already use sequential tree cursors.

**Best measured result.** epoch-start stf 1503 to 709 ms (option c); this option 1126 ms (pr:ethlambda#630)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:243-262`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L243-L262) izip over participation iters plus iter_cow cursors on validators, balances and inactivity_scores
- [`consensus/state_processing/src/common/update_progressive_balances_cache.rs:35-40`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/update_progressive_balances_cache.rs#L35-L40) progressive cache init zips sequential iterators
- [`consensus/state_processing/src/epoch_cache.rs:165`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/epoch_cache.rs#L165) epoch cache init iterates validators sequentially

**Skeptic check.** Checked the main dense scans: the single pass, the progressive balances init and the epoch cache init. All use milhouse iterators, not per-index get. Indexed access remains only on sparse lists, such as pending deposits and consolidations. Upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#7617](https://github.com/ChainSafe/lodestar/pull/7617), [silver#145](https://github.com/gattaca-com/silver/pull/145), [lodestar#1349](https://github.com/ChainSafe/lodestar/pull/1349), [ethlambda#630](https://github.com/lambdaclass/ethlambda/pull/630)

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

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [caplin#25144](https://github.com/erigontech/erigon/pull/25144)

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


<a id="epoch_processing-063"></a>
<details>
<summary><b>epoch_processing-063</b> In-order copy-on-write cursor for list writes — <i>partial · medium · M · cpu, memory</i></summary>

**Idea.** Write epoch balance changes through an in-order lazy copy-on-write cursor over the persistent tree list, copying a leaf only on first write and keeping cached hashes for unchanged leaves, instead of buffering updates in a map, sorting and rehashing.

**Gap in Lighthouse.** The in-order cursor exists for reads, but milhouse InterfaceIterCow writes still go into the dense VecMap (MaxMap&lt;VecMap&gt;) update buffer, and Interface::apply_updates then does a second tree descent with Tree::with_updated_leaves and PackedLeaf::update. The cursor does not build new leaves while it walks the tree, and it does not compare a touched leaf with its original value to keep the original Arc and hash. ethlambda's cursor removes the buffer and apply phases (write 58 ms + apply 70 ms down to 27 ms at 2.4M validators).

**Impact.** Removes the dense update-map allocation and the separate apply_updates walk for balances (nearly every leaf changes at each epoch) and for effective-balance and inactivity writes. Estimate: tens of ms per epoch transition at mainnet size, not measured.

**Best measured result.** Estimate only: tens of ms off each epoch-start block; benchmark not run (pr:ethlambda#647)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:243-259`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L243-L259) iter_cow/next_cow over validators, balances, inactivity_scores
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:697-701`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L697-L701) balance make_mut only when delta is non-zero, deltas netted
- d67aabd/src/update_map.rs:102-138 VecMap get_cow_with: make_mut copies the value into the dense update map
- d67aabd/src/interface.rs:86-100 apply_updates takes the map and calls backing.update
- d67aabd/src/tree.rs:164-250 with_updated_leaves second descent, for_each_range probes per node
- d67aabd/src/packed_leaf.rs:86-115 update/insert_mut zeroes the leaf hash for any written index, even an unchanged value

**Skeptic check.** I read milhouse at the locked git rev d67aabd. The earlier evidence cited the registry milhouse-0.9.0, which is not the version in use. iter_cow is a read-in-order cursor with copy-on-write into an update map, so the 'instead of buffering updates in a map' part of the idea is not implemented. Lighthouse already gets the bigger wins ethlambda also took (one pass, netted deltas, writes only on change).

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [ethlambda#647](https://github.com/lambdaclass/ethlambda/pull/647)

</details>


<a id="epoch_processing-064"></a>
<details>
<summary><b>epoch_processing-064</b> Advance committee caches per slot, not in epoch processing — <i>implemented · medium · S · cpu</i></summary>

**Idea.** Do not build the next-epoch committee/shuffling caches inside the epoch transition; rotate or build current/next caches during per-slot processing so the epoch transition does not pay for them and cache building is not repeated.

**Impact.** The next-epoch shuffling is prebuilt by the per-slot advance, so the epoch transition normally finds it cached.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:333-340`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L333-L340) builds Current and Next committee caches on the advanced head state each slot
- [`consensus/types/src/state/beacon_state.rs:2824-2835`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2824-L2835) build_committee_cache returns early if already initialized
- [`consensus/state_processing/src/per_epoch_processing/altair.rs:30-32`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/altair.rs#L30-L32) builds only on a miss
- [`consensus/types/src/state/beacon_state.rs:2887-2893`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2887-L2893) advance_caches only rotates

**Skeptic check.** Both cited source items are Lighthouse's own changes. I confirmed the timer prebuilds Next, and that process_epoch and advance_caches do not rebuild it when it is present.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@073be906d](https://github.com/sigp/lighthouse/commit/073be906da49), [lighthouse#263](https://github.com/sigp/lighthouse/pull/263)

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


<a id="epoch_processing-066"></a>
<details>
<summary><b>epoch_processing-066</b> Use length accessors instead of copying lists — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Read the length of balances, randao mixes and similar state lists through a length accessor rather than copying the slice/list just to take its length in epoch processing.

**Impact.** Milhouse List len() is O(1) from the stored length. No list is copied to read its length.

**Best measured result.** 'Saves a little bit of time / space in epoch processing' (pr:prysm#4769)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:213`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L213) validators.len() on a milhouse List

**Skeptic check.** The earlier evidence is correct. The Prysm problem (slice copies from getters) does not exist with Lighthouse's borrowed milhouse lists.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#4769](https://github.com/OffchainLabs/prysm/pull/4769)

</details>


<a id="epoch_processing-067"></a>
<details>
<summary><b>epoch_processing-067</b> Compute next-epoch balances without full epoch transition — <i>not · low · M · cpu, latency</i></summary>

**Idea.** Factor epoch processing into per-validator functions so a single validator's post-epoch balance (e.g. for proposer withdrawals or payload attributes lookahead) can be computed without running the whole epoch transition on a state copy.

**Gap in Lighthouse.** Add a per-validator next-epoch balance function (rewards, penalties, slashing, pending deposits/consolidations effects) and use it in get_expected_withdrawals instead of cloning the state and running process_epoch_single_pass for the whole registry. Pending deposits and consolidations make the per-validator result depend on cross-validator state, which complicates it.

**Impact.** Only the prepare-proposer withdrawals call when the next slot crosses an epoch boundary (once per epoch, off the hot path in spawn_blocking); saves one epoch transition on a state copy, perhaps a few hundred ms, only for nodes with local proposers.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5396`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5396) compute_withdrawals_for_payload_attributes clones the state and calls partial_state_advance
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5453`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5453) partial_state_advance runs full per_epoch_processing when proposal slot is in next epoch
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:155`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L155) epoch processing is one monolithic function over all validators

**Sources.** [nimbus#5910](https://github.com/status-im/nimbus-eth2/pull/5910), [nimbus#6416](https://github.com/status-im/nimbus-eth2/pull/6416)

</details>


<a id="epoch_processing-068"></a>
<details>
<summary><b>epoch_processing-068</b> Apply rewards and penalties in one balance pass — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Compute each new balance as max(0, balance + reward - penalty) in one pass over validators, instead of copying balances and then looping separately to apply rewards and then penalties.

**Impact.** Already a single fused pass; one make_mut per changed balance.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:680-702`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L680-L702)
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:244-255`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L244-L255)

**Skeptic check.** Verified that process_single_reward_and_penalty accumulates a Delta, then applies balance += rewards and saturating_sub(penalties) once, and only when the delta is nonzero. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@16c61e214](https://github.com/ChainSafe/lodestar/commit/16c61e21485f)

</details>


<a id="epoch_processing-069"></a>
<details>
<summary><b>epoch_processing-069</b> Lightweight justification-only balance totals — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** When only justification/finalization is needed (e.g. checkpoint state or unrealized justification during block import), compute just the participating-balance totals in one pass over validators and flags instead of building full per-validator summaries.

**Impact.** After Altair, justification on block import costs O(1) and needs no per-validator summaries.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/altair/justification_and_finalization.rs:9-30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/altair/justification_and_finalization.rs#L9-L30) reads target balances from the progressive balances cache, no validator pass
- [`consensus/fork_choice/src/fork_choice.rs:932-967`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L932-L967) unrealized justification on block import reuses parent checkpoints or uses the cached path; ValidatorStatuses only pre-Altair

**Skeptic check.** I confirmed that the hot path, fork_choice on_block unrealized justification, uses the progressive balances cache. This is stronger than the Grandine one-pass totals.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine@c4b676e3d](https://github.com/grandinetech/grandine/commit/c4b676e3daa0)

</details>


<a id="epoch_processing-070"></a>
<details>
<summary><b>epoch_processing-070</b> Carry epoch caches into precomputed checkpoint state — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** When precomputing the next epoch's checkpoint state ahead of the boundary, transfer the already built epoch cache (shufflings, proposers, etc.) to the state used for block import so it is not rebuilt later.

**Impact.** The precomputed checkpoint state carries its EpochCache and committee caches into block import, so they are not built again.

**Best measured result.** Epoch transition mainnet 1.1s to 0.96s, 64-node 0.81s to 0.73s, 16-node 4s to 3.3s (pr:lodestar#6068)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:333-340`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L333-L340) builds committee caches on the advanced state
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:454`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L454) put_state stores the advanced state (with its caches) for block import via get_advanced_hot_state
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:481-488`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L481-L488) next-epoch EpochCache installed in the state during epoch processing
- [`beacon_node/store/src/hot_cold_store.rs:1124`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1124) get_advanced_hot_state

**Skeptic check.** The earlier evidence is correct. The epoch cache is produced inside epoch processing, and the advanced state is cached and served to block import.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#6068](https://github.com/ChainSafe/lodestar/pull/6068)

</details>


<a id="epoch_processing-071"></a>
<details>
<summary><b>epoch_processing-071</b> Precompute validator inclusion-distance map once — <i>implemented · low · S · cpu</i></summary>

**Idea.** For phase0 attestation rewards, build a validator-to-earliest-inclusion slot/distance/proposer map with one pass over previous-epoch pending attestations, instead of rescanning all attestations per validator (quadratic).

**Impact.** Phase0 only; already linear in attestations times committee size.

**Best measured result.** 100k validators: epoch slot 21662 -&gt; 11636 ms, attest 7755 -&gt; 4312 ms, ~40% overall block_sim speedup (pr:nimbus#1294)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/base/validator_statuses.rs:42-47`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/base/validator_statuses.rs#L42-L47)
- [`consensus/state_processing/src/per_epoch_processing/base/validator_statuses.rs:254-300`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/base/validator_statuses.rs#L254-L300)
- [`consensus/state_processing/src/per_epoch_processing/base/rewards_and_penalties.rs:301-310`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/base/rewards_and_penalties.rs#L301-L310)

**Skeptic check.** process_attestations makes one pass over pending attestations and keeps the minimum delay and its proposer through InclusionInfo::update. Rewards then read the precomputed inclusion_info, so there is no per-validator rescan. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#1294](https://github.com/status-im/nimbus-eth2/pull/1294), [lighthouse@63743a962](https://github.com/sigp/lighthouse/commit/63743a962c60), [lighthouse@f27b62d41](https://github.com/sigp/lighthouse/commit/f27b62d41039), [lighthouse@6f919e6f7](https://github.com/sigp/lighthouse/commit/6f919e6f7dbb), [nimbus#155](https://github.com/status-im/nimbus-eth2/pull/155), [lighthouse@53456a6c7](https://github.com/sigp/lighthouse/commit/53456a6c79b5)

</details>


<a id="epoch_processing-072"></a>
<details>
<summary><b>epoch_processing-072</b> Compute crosslink winning-root participants once per shard — <i>n/a · low · cpu</i></summary>

**Idea.** In phase0 crosslink and reward processing, compute each shard's winning root and participant set once (loop order: shard outer, validators inner) and memoize it for the rewards pass, instead of recomputing per validator.

**Impact.** Crosslinks were removed from the spec; nothing to optimise.

**Best measured result.** process_crosslinks 15-16s -&gt; 1s; attestation deltas 178s -&gt; 2s (512 validators) (pr:nimbus#314)

**Evidence (Lighthouse @ 928b61e719).**

- grep for crosslink in [`consensus/state_processing`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing) finds nothing

**Sources.** [nimbus#313](https://github.com/status-im/nimbus-eth2/pull/313), [nimbus#314](https://github.com/status-im/nimbus-eth2/pull/314), [nimbus@58b617465](https://github.com/status-im/nimbus-eth2/commit/58b61746549d), [nimbus@6f481f881](https://github.com/status-im/nimbus-eth2/commit/6f481f8812de), [lighthouse@a31914483](https://github.com/sigp/lighthouse/commit/a319144835f8)

</details>


<a id="epoch_processing-073"></a>
<details>
<summary><b>epoch_processing-073</b> Single pass to derive matching source/target/head attestations — <i>implemented · low · S · cpu</i></summary>

**Idea.** Derive the matching source, target and head pending-attestation sets and their aggregates in one pass over pending attestations, instead of one pass per helper (quadratic or cubic overall).

**Impact.** Phase0 only; source, target and head are classified in one loop.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/base/validator_statuses.rs:254-300`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/base/validator_statuses.rs#L254-L300)

**Skeptic check.** One loop over previous- and current-epoch attestations sets the attester, target and head flags. The totals come from a single later loop over the statuses. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#2342](https://github.com/OffchainLabs/prysm/pull/2342), [prysm#2379](https://github.com/OffchainLabs/prysm/pull/2379)

</details>


<a id="epoch_processing-074"></a>
<details>
<summary><b>epoch_processing-074</b> Epoch-local inclusion maps without shared mutex — <i>n/a · low · cpu</i></summary>

**Idea.** Build attestation inclusion maps locally inside epoch processing rather than in shared mutex-guarded maps outside the state transition.

**Impact.** Rust has no shared mutex map here; statuses are built locally inside epoch processing.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/base/validator_statuses.rs:254`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/base/validator_statuses.rs#L254) inclusion map built locally in ValidatorStatuses::process_attestations

**Sources.** [prysm#2347](https://github.com/OffchainLabs/prysm/pull/2347)

</details>


<a id="epoch_processing-075"></a>
<details>
<summary><b>epoch_processing-075</b> Machine-word integers for reward/penalty math — <i>n/a · low · S · cpu, memory</i></summary>

**Idea.** Use native 64-bit (or smaller) integers for per-validator reward and penalty arrays and divisions in epoch processing wherever values provably fit, instead of arbitrary-precision bigint arithmetic.

**Impact.** None; Rust uses native u64 with safe_arith, no bigint to remove.

**Best measured result.** getAttestationDeltas average 130ms to 79ms (pr:lodestar#2092)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:171`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L171) u64 balances used natively

**Sources.** [lodestar@b0c8c21e3](https://github.com/ChainSafe/lodestar/commit/b0c8c21e3cc2), [lodestar#2092](https://github.com/ChainSafe/lodestar/pull/2092), [lodestar@ca51e1219](https://github.com/ChainSafe/lodestar/commit/ca51e1219c24)

</details>


<a id="epoch_processing-076"></a>
<details>
<summary><b>epoch_processing-076</b> Hoist constants into hot function locals — <i>n/a · low · cpu</i></summary>

**Idea.** Bind constants used inside hot epoch-processing loops as local variables so the JIT/compiler does not perform module or global lookups per iteration.

**Impact.** Hoisting constants addresses JIT global lookups; compiled Rust has no such cost.

**Best measured result.** getAttestationDeltas avg 116ms to 47ms (pr:lodestar#2348)

**Evidence (Lighthouse @ 928b61e719).**

- Rust consts are compile-time inlined

**Sources.** [lodestar#2348](https://github.com/ChainSafe/lodestar/pull/2348)

</details>


<a id="epoch_processing-077"></a>
<details>
<summary><b>epoch_processing-077</b> Remove closures from shuffling hot loop — <i>n/a · low · cpu</i></summary>

**Idea.** Inline the code instead of calling a closure inside the epoch shuffling loop, since closure calls in the hot loop are slow.

**Impact.** Closure overhead is a JS issue; Rust closures are inlined.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/swap_or_not_shuffle/src/shuffle_list.rs:92`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/swap_or_not_shuffle/src/shuffle_list.rs#L92) plain loops

**Sources.** [lodestar#2922](https://github.com/ChainSafe/lodestar/pull/2922)

</details>


<a id="epoch_processing-078"></a>
<details>
<summary><b>epoch_processing-078</b> List-wise swap-or-not shuffle for whole epoch — <i>implemented · low · S · cpu</i></summary>

**Idea.** Compute the epoch's committees by shuffling the entire active index list in rounds (list-wise swap-or-not) instead of calling compute_shuffled_index per index.

**Impact.** Already list-wise.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/swap_or_not_shuffle/src/shuffle_list.rs:92-160`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/swap_or_not_shuffle/src/shuffle_list.rs#L92-L160)
- [`consensus/types/src/state/committee_cache.rs:147-152`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L147-L152)

**Skeptic check.** CommitteeCache::initialized calls shuffle_list on the whole active index list, which runs list-wise swap-or-not rounds. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#921](https://github.com/ChainSafe/lodestar/pull/921)

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


<a id="epoch_processing-080"></a>
<details>
<summary><b>epoch_processing-080</b> Native code for shuffling and committee sampling — <i>n/a · low · cpu, latency</i></summary>

**Idea.** Compute committee shuffling, proposer indices and sync committee indices in compiled native (optionally multithreaded, off-main-thread) code rather than in an interpreted runtime.

**Impact.** Lighthouse is already native code; the idea is moving JS to native.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/swap_or_not_shuffle/src/shuffle_list.rs:92`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/swap_or_not_shuffle/src/shuffle_list.rs#L92) is native Rust

**Sources.** [lodestar#7120](https://github.com/ChainSafe/lodestar/pull/7120), [lodestar#7499](https://github.com/ChainSafe/lodestar/pull/7499)

</details>


<a id="epoch_processing-081"></a>
<details>
<summary><b>epoch_processing-081</b> Async shuffling only at normal epoch transitions — <i>n/a · low · cpu, memory</i></summary>

**Idea.** Only schedule asynchronous shuffling computation at regular epoch transitions and compute other shufflings lazily on demand, to avoid piling up many pending shuffling tasks when processing old blocks.

**Impact.** Lighthouse has no async worker queue for epoch transitions; shuffling is a CommitteeCache built synchronously from a state, and the beacon-chain cache only holds on-demand promises.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:27`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L27) promise cache, computed on demand

**Sources.** [lodestar#7251](https://github.com/ChainSafe/lodestar/pull/7251)

</details>


<a id="epoch_processing-082"></a>
<details>
<summary><b>epoch_processing-082</b> Compute shufflings synchronously into cache — <i>n/a · low · cpu, latency</i></summary>

**Idea.** Compute shufflings synchronously during the epoch transition and insert them into the shuffling cache, dropping a separate async build path, since proposer lookahead needs them synchronously.

**Impact.** Lighthouse already builds shufflings synchronously in CommitteeCache::initialized; there is no separate async path to remove.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/committee_cache.rs:120`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L120) initialized_unchecked builds shuffling synchronously

**Sources.** [lodestar#8688](https://github.com/ChainSafe/lodestar/pull/8688)

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


<a id="epoch_processing-084"></a>
<details>
<summary><b>epoch_processing-084</b> In-place low-allocation shuffling — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Implement the shuffle in place over one buffer without allocating intermediate sequences, reducing allocator/GC pressure during block replay and epoch processing.

**Impact.** Already in place, with a single owned Vec and a reused hash buffer.

**Best measured result.** 4x improvement on non-epoch blocks, 1.5x on epoch blocks (Apply block 85.6ms -&gt; 21.7ms; epoch 506ms -&gt; 324ms) (commit:nimbus@61538fa5817d)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/swap_or_not_shuffle/src/shuffle_list.rs:92-160`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/swap_or_not_shuffle/src/shuffle_list.rs#L92-L160)

**Skeptic check.** shuffle_list takes ownership of the input Vec and swaps in place with masked_swap, reusing one Buf for the hashes. It allocates nothing per round. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus@61538fa58](https://github.com/status-im/nimbus-eth2/commit/61538fa5817d)

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


<a id="epoch_processing-089"></a>
<details>
<summary><b>epoch_processing-089</b> Zero-copy committee views from shuffling buffer — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** Take per-slot committees as zero-copy subarray views of the contiguous epoch shuffling buffer instead of concatenating them into new arrays.

**Impact.** Committees are borrowed slices of the epoch shuffling.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/committee_cache.rs:367-374`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L367-L374)
- [`consensus/types/src/state/committee_cache.rs:229-245`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L229-L245)

**Skeptic check.** compute_committee returns self.shuffling.get(range), which is a &amp;[usize] view. get_beacon_committees_at_slot only collects small BeaconCommittee structs that hold those slices. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#9012](https://github.com/ChainSafe/lodestar/pull/9012)

</details>


<a id="epoch_processing-090"></a>
<details>
<summary><b>epoch_processing-090</b> Avoid computing shuffling for total active balance — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Do not build the committee shuffling just to obtain total_active_balance in process_epoch; get it from cached totals and defer shuffling to where it is actually needed.

**Impact.** Total active balance never needs a shuffle. The Next committee cache built at altair.rs:32 becomes Current after advance_caches and is needed by block processing in any case.

**Best measured result.** saves about 120ms for process_epoch on the massive deposit queue (pr:nimbus#8214)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/altair.rs:33`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/altair.rs#L33) build_total_active_balance_cache
- [`consensus/types/src/state/beacon_state.rs:2728`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2728) compute_total_active_balance_slow scans validators, no shuffling
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:481-482`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L481-L482) next-epoch total set from next_epoch_cache

**Skeptic check.** The Nimbus bug (shuffling to get the active set) does not exist in Lighthouse. The shuffle built in process_epoch is not wasted work that the idea would remove.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#8214](https://github.com/status-im/nimbus-eth2/pull/8214)

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


<a id="epoch_processing-092"></a>
<details>
<summary><b>epoch_processing-092</b> Parallel hashing of rebuilt balances leaves — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** After rebuilding the balances list at the epoch boundary, hash its leaf chunks in parallel on a thread pool instead of serially at the next state-root computation.

**Impact.** Dirty balances subtrees hash in parallel on the rayon pool at the next state-root computation.

**Best measured result.** epoch 98.8 -&gt; 71.8 ms (M5), 110.2 -&gt; 93.1 ms (EPYC); same total CPU (pr:lodestar#10521)

**Evidence (Lighthouse @ 928b61e719).**

- d67aabd/src/tree.rs:530-547 Node::tree_hash recomputes dirty nodes with rayon::join on left/right

**Skeptic check.** I confirmed this in the milhouse git rev that is actually locked (d67aabd), not 0.9.0 as the earlier evidence cited. The mechanism is the same, so the earlier verdict stands.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#10521](https://github.com/ChainSafe/lodestar/pull/10521)

</details>


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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [caplin#23966](https://github.com/erigontech/erigon/pull/23966), [caplin#12191](https://github.com/erigontech/erigon/pull/12191), [caplin#12291](https://github.com/erigontech/erigon/pull/12291), [caplin#12277](https://github.com/erigontech/erigon/pull/12277), [teku#5826](https://github.com/Consensys-Incorporated/teku/pull/5826)

</details>


<a id="epoch_processing-094"></a>
<details>
<summary><b>epoch_processing-094</b> Keep cheap epoch loops single-threaded — <i>implemented · low · S · cpu</i></summary>

**Idea.** Run cheap per-validator epoch loops on one thread instead of spawning per-CPU workers, since scheduling overhead exceeds the tiny per-item work.

**Impact.** Epoch loops are sequential; nothing to change.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:240-255`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L240-L255)

**Skeptic check.** A grep found no rayon use under per_epoch_processing, and the per-validator work is one sequential fused pass. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#13007](https://github.com/erigontech/erigon/pull/13007)

</details>


<a id="epoch_processing-095"></a>
<details>
<summary><b>epoch_processing-095</b> Scan validator registry from packed SSZ bytes — <i>n/a · low · S · cpu, memory, latency</i></summary>

**Idea.** Read validator fields for epoch processing scans (statuses, active indices, registry and effective-balance updates) directly from the packed SSZ bytes without building and caching per-validator view objects, avoiding gigabytes of allocation on a freshly loaded state.

**Impact.** Lighthouse already works on native structs; only the cost of decoding a freshly loaded state remains, which this idea does not address.

**Best measured result.** cold epoch transition 7,442 ms -&gt; 4,041 ms; warm 4,432 -&gt; 1,668 ms; heap growth 1,970 -&gt; 930 MB; used heap 5.56 -&gt; 3.80 GB (pr:teku#11597)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:243`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L243) validators.iter_cow() yields borrowed native Validator structs from milhouse, no per-validator view objects

**Sources.** [teku#11597](https://github.com/Consensys-Incorporated/teku/pull/11597)

</details>


<a id="epoch_processing-096"></a>
<details>
<summary><b>epoch_processing-096</b> Validators in persistent vector with fast iteration — <i>implemented · low · S · cpu, sync</i></summary>

**Idea.** Keep validators in a persistent/structurally shared vector with cheap clone and array-like iteration, rather than iterating a slow tree-backed list during epoch processing.

**Impact.** The state clones cheaply with structural sharing, and epoch processing iterates the tree in order without a descent for each index.

**Best measured result.** epoch transition 3.5-4.2s to 1.2-1.6s; prepareEpochProcessState 1500 to 100; 16 exits 6000 to 200 (pr:lodestar#1925)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:243-259`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L243-L259) in-order iter_cow over the milhouse validators list
- [`consensus/types/src/state/beacon_state.rs:554`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L554) state lists are milhouse List (persistent, Arc-shared)

**Skeptic check.** The earlier evidence is correct. The milhouse tree iterator gives near-array iteration, and clone is O(1).

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#1877](https://github.com/ChainSafe/lodestar/pull/1877), [lodestar#1925](https://github.com/ChainSafe/lodestar/pull/1925)

</details>


<a id="epoch_processing-097"></a>
<details>
<summary><b>epoch_processing-097</b> Reuse old balances tree as rebuild base — <i>n/a · medium · memory, cpu</i></summary>

**Idea.** When rebuilding the balances list tree at the epoch transition, reuse a retained balances tree from a pruned/finalized state as the base instead of building it from scratch, reducing allocation spikes and hashing.

**Impact.** Lodestar rebuilds a persistent tree from a flat array; Lighthouse's milhouse copy-on-writes only changed leaves, so no from-scratch rebuild exists.

**Best measured result.** processRewardsAndPenalties spikes reduced; ~250ms saved average; prepareNextEpoch ~350ms saved (pr:lodestar#7084)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:243`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L243) iter_cow edits the milhouse tree in place, sharing untouched subtrees with the parent state
- milhouse 0.9.0 (git d67aabd) structural sharing

**Sources.** [lodestar#7084](https://github.com/ChainSafe/lodestar/pull/7084)

</details>


<a id="epoch_processing-098"></a>
<details>
<summary><b>epoch_processing-098</b> Stack-allocate fixed-size proposer lookahead — <i>n/a · low · memory, cpu</i></summary>

**Idea.** Fill the fixed-size proposer lookahead into a caller-owned stack array rather than a heap allocation freed right after epoch processing.

**Impact.** The lookahead is one small Vec per epoch (64 or so entries); the heap allocation is negligible in Rust and cost is dominated by get_beacon_proposer_indices.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:506`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L506) process_proposer_lookahead does one to_vec per epoch

**Sources.** [lodestar@5e82cc438](https://github.com/ChainSafe/lodestar/commit/5e82cc438a4f)

</details>


<a id="epoch_processing-099"></a>
<details>
<summary><b>epoch_processing-099</b> Skip balance writes for zero reward deltas — <i>implemented · low · S · cpu</i></summary>

**Idea.** When applying rewards and penalties, skip the balance read/write for validators whose net delta is zero (e.g. exited validators).

**Impact.** Already skipped; no gain.

**Best measured result.** "not a huge speed improvement"; ~15% of validator set has zero delta (pr:teku#7284)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:674-676`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L674-L676)
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:697-701`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L697-L701)
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:243-260`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L243-L260)

**Skeptic check.** process_single_reward_and_penalty returns early for ineligible validators and only calls balance.make_mut() when rewards or penalties are nonzero; balances are iterated via iter_cow so unchanged entries are never written. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#7284](https://github.com/Consensys-Incorporated/teku/pull/7284)

</details>


<a id="epoch_processing-100"></a>
<details>
<summary><b>epoch_processing-100</b> Read-only registry scan, mutate collected indices — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** In process_registry_updates, do a read-only pass to collect indices for activation queue, activation and ejection, then mutate only those validators, avoiding copying the whole registry each epoch.

**Impact.** Registry is never copied; only mutated validators are cloned through Cow::make_mut.

**Best measured result.** worst case copy reduced to ~8 MB of indices; average case near zero allocation (pr:prysm#14130)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:242-260`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L242-L260)
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:309-320`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L309-L320)
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:837-860`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L837-L860)
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:862-900`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L862-L900)

**Skeptic check.** Single pass uses validators.iter_cow(); registry update functions call make_mut only on eligibility, ejection or activation changes, and the activation queue is precomputed. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#14130](https://github.com/OffchainLabs/prysm/pull/14130)

</details>


<a id="epoch_processing-101"></a>
<details>
<summary><b>epoch_processing-101</b> One state lock for whole balance update loop — <i>n/a · low · cpu</i></summary>

**Idea.** Acquire the state lock once for an entire per-validator balance update loop rather than once per validator.

**Impact.** Lighthouse state is an owned milhouse tree mutated through &amp;mut, with no per-validator lock.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:255`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L255) balances iterated with a cow iterator, no lock

**Sources.** [prysm#6122](https://github.com/OffchainLabs/prysm/pull/6122)

</details>


<a id="epoch_processing-102"></a>
<details>
<summary><b>epoch_processing-102</b> Compact u16 effective-balance increments array — <i>partial · low · S · memory, cpu</i></summary>

**Idea.** Keep a compact per-validator effective balance in increments (u16) array in the epoch-level cache so scattered per-attester reads in reward loops hit CPU cache.

**Gap in Lighthouse.** EpochCache::effective_balances could store u16 increments instead of u64 (4x smaller), and get_effective_balance/get_base_reward would index it.

**Impact.** Slightly less cache pressure for scattered reads; Lighthouse's epoch pass walks validators in order and the cache is only used by block attestation rewards, so gain is small.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/epoch_cache.rs:33`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/epoch_cache.rs#L33) effective_balances: Vec&lt;u64&gt; in EpochCache
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:275`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L275) reward loop reads validator.effective_balance from the sequential validator iterator

**Sources.** [silver#366](https://github.com/gattaca-com/silver/pull/366)

</details>


<a id="epoch_processing-103"></a>
<details>
<summary><b>epoch_processing-103</b> Sorted batch merge of participation updates — <i>n/a · low · cpu</i></summary>

**Idea.** Collect participation-flag updates, sort by index and merge them into the sorted edit list in one linear pass instead of inserting each update individually.

**Impact.** Milhouse persistent list manages its own structural sharing; silver's sorted edit list has no counterpart.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/process_operations.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs): attestations update participation via milhouse list per index

**Sources.** [silver#64](https://github.com/gattaca-com/silver/pull/64)

</details>


<a id="epoch_processing-104"></a>
<details>
<summary><b>epoch_processing-104</b> Record participation totals at epoch processing — <i>partial · low · S · cpu, latency</i></summary>

**Idea.** Record per-epoch participation totals during epoch processing and keep them in a map, instead of recomputing them from state attestations every slot or per API query.

**Gap in Lighthouse.** On block import Lighthouse already gets participation totals from epoch processing and never recomputes them per slot. The API path does not. global_validator_inclusion_data and validator_inclusion_data call end_of_epoch_state (a state load or replay) and then a full process_epoch on every request. No epoch-&gt;summary map is kept from the EpochProcessingSummary that block_verification already computes. This is the repeat-query DoS cost that the Prysm PR removed.

**Impact.** Removes a full state load plus process_epoch per lighthouse/validator_inclusion request. The endpoint is Lighthouse-specific and used mainly by monitoring, so the effect on node-wide performance is low.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1639-1675`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1639-L1675) per_slot_processing returns EpochProcessingSummary once per epoch transition; used for metrics and validator monitor, then dropped
- [`beacon_node/http_api/src/validator_inclusion.rs:11-33`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator_inclusion.rs#L11-L33) end_of_epoch_state loads a full state and get_epoch_processing_summary runs process_epoch on every request
- [`beacon_node/http_api/src/validator_inclusion.rs:41-60`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator_inclusion.rs#L41-L60) global_validator_inclusion_data
- [`beacon_node/http_api/src/lib.rs:3217-3245`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L3217-L3245) GET lighthouse/validator_inclusion routes

**Skeptic check.** The earlier evidence (the progressive balances cache) is correct for block import and epoch processing. But the idea also covers API queries, and validator_inclusion.rs recomputes process_epoch on each call without caching.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [prysm#4430](https://github.com/OffchainLabs/prysm/pull/4430)

</details>


<a id="epoch_processing-105"></a>
<details>
<summary><b>epoch_processing-105</b> Tighten per-validator checks in registry scans — <i>implemented · low · S · cpu</i></summary>

**Idea.** Make full validator-registry scans in epoch processing and rewards cheaper by removing redundant accessor calls, checks and allocations per validator.

**Impact.** Already a single fused pass that computes each validator's values once.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:155-165`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L155-L165) process_epoch_single_pass builds the caches once, then runs one fused validator loop
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:247`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L247) izip over validators, balances and participation

**Skeptic check.** Confirmed that process_epoch_single_pass is the epoch path and that it does inactivity, rewards, registry, slashings and effective balance in one loop. The Teku micro-cleanups have no remaining analogue here.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#6994](https://github.com/Consensys-Incorporated/teku/pull/6994)

</details>


<a id="epoch_processing-106"></a>
<details>
<summary><b>epoch_processing-106</b> Reuse previous fork epoch processing code — <i>n/a · low · cpu</i></summary>

**Idea.** Reuse the previous fork's epoch processing operations and intermediates for the next fork instead of duplicating code paths.

**Impact.** Lighthouse already shares one epoch implementation across Altair and later forks; this is a code-reuse point with no runtime effect.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:155`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L155) shared single pass for all Altair+ forks

**Sources.** [grandine@13b5bf516](https://github.com/grandinetech/grandine/commit/13b5bf516c13)

</details>


<a id="epoch_processing-107"></a>
<details>
<summary><b>epoch_processing-107</b> Plain loop reading validator fields once — <i>n/a · low · cpu</i></summary>

**Idea.** Build validator statuses with a plain loop that reads each validator's fields once instead of streams with repeated field lookups.

**Impact.** The Teku fix replaces Java streams; Lighthouse already uses a plain loop reading each validator once.

**Best measured result.** createValidatorStatuses 11.028 -&gt; 15.271 ops/s (pr:teku#5776)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:247`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L247) plain for loop, reads fields once

**Sources.** [teku#5776](https://github.com/Consensys-Incorporated/teku/pull/5776)

</details>


<a id="epoch_processing-108"></a>
<details>
<summary><b>epoch_processing-108</b> Precompute OR-combined status flags per validator — <i>implemented · low · S · cpu</i></summary>

**Idea.** Combine per-validator status flags (OR) once before reward delta computation rather than in every loop iteration.

**Impact.** Flags derived once per validator; no gain.

**Best measured result.** 16% less getAttestationDeltas, ~150ms per epoch (pr:lodestar#2341)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:262-284`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L262-L284)
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:707-720`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L707-L720)

**Skeptic check.** ValidatorInfo (is_eligible, is_active_*, slashed, participation flags) is built once per validator and shared by inactivity, rewards and registry sub-steps. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#2341](https://github.com/ChainSafe/lodestar/pull/2341)

</details>


<a id="epoch_processing-109"></a>
<details>
<summary><b>epoch_processing-109</b> Optimized epoch balance update path by default — <i>n/a · low · cpu</i></summary>

**Idea.** Use the optimized epoch balance-update implementation as the default path rather than behind a flag.

**Impact.** No feature flag exists; the fused path is the only path.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:1372`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L1372) process_single_effective_balance_update runs unconditionally in the single pass

**Sources.** [prysm#10549](https://github.com/OffchainLabs/prysm/pull/10549)

</details>


<a id="epoch_processing-110"></a>
<details>
<summary><b>epoch_processing-110</b> Single pass over participation flags for stats — <i>n/a · low · cpu</i></summary>

**Idea.** When collecting validator participation statistics from Altair participation flags, compute all counters in one pass over the flags array instead of looping twice.

**Impact.** Lighthouse does not compute whole-registry participation statistics in a two-pass loop on a hot path; the stats are per-monitored-validator.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/epoch_processing_summary.rs:27`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/epoch_processing_summary.rs#L27) ParticipationEpochSummary only snapshots lists
- [`beacon_node/beacon_chain/src/validator_monitor.rs:481`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_monitor.rs#L481) only monitored validators processed

**Sources.** [teku#4158](https://github.com/Consensys-Incorporated/teku/pull/4158)

</details>


<a id="epoch_processing-111"></a>
<details>
<summary><b>epoch_processing-111</b> Count active validators without building index list — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Count active validators with a counting loop instead of materialising the active-index list just to take its length (committee counts, genesis). Avoids an allocation and a list build per call.

**Impact.** Active count comes from the already-built committee cache; the only list-just-for-len paths are one-time (startup, genesis). Nothing meaningful to gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:2583-2591`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2583-L2591)
- [`beacon_node/beacon_processor/src/scheduler/work_queue.rs:339-346`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_queue.rs#L339-L346)
- [`consensus/state_processing/src/genesis.rs:246`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/genesis.rs#L246)

**Skeptic check.** The churn limit and committee counts use committee_cache.active_validator_count(). The other get_active_validator_indices callers (proposer and sync committee selection, beacon_state.rs:1665,1699,1776) use the list itself, not only its length. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#1356](https://github.com/status-im/nimbus-eth2/pull/1356)

</details>


<a id="epoch_processing-112"></a>
<details>
<summary><b>epoch_processing-112</b> Compute only fork-applicable churn limits in epoch processing — <i>partial · low · S · cpu</i></summary>

**Idea.** In single-pass epoch processing, compute only the churn limits relevant to the current fork rather than all of them. Saves unused work per epoch.

**Gap in Lighthouse.** single_pass_apply should compute only the limits the current fork uses (as in the open PR sigp/lighthouse#9880); do it in single_pass.rs StateContext construction.

**Impact.** Each limit is a few arithmetic ops on a cached count, so the saving is negligible per epoch; code-quality change rather than speed.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:172-173`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L172-L173) - computes both churn_limit and activation_churn_limit for every fork
- [`consensus/types/src/state/beacon_state.rs:2583-2610`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2583-L2610) - helpers are O(1) given the committee cache

**Sources.** [lighthouse#9880](https://github.com/sigp/lighthouse/pull/9880)

</details>


