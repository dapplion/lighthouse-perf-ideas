# state_transition

174 ideas: 14 not, 27 partial, 79 implemented, 54 n/a; 5 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [state_transition-001](#state_transition-001) | Sparse BTreeMap for pending updates in persistent lists | partial | low | S | cpu, memory |
| [state_transition-002](#state_transition-002) | Incremental deposit Merkle tree at genesis | implemented | low | S | cpu, startup |
| [state_transition-003](#state_transition-003) | Cache total active balance per epoch and use it | implemented | low | S | cpu |
| [state_transition-004](#state_transition-004) | Cache base reward per increment per epoch | implemented | low | S | cpu |
| [state_transition-005](#state_transition-005) | Allocation-free swap-or-not shuffle and hashing | implemented | low | S | cpu, memory |
| [state_transition-006](#state_transition-006) | Check-free byte conversions in shuffle inner loop | implemented | low | S | cpu |
| [state_transition-007](#state_transition-007) | Inline per-index work in shuffle loop | implemented | low | S | cpu |
| [state_transition-008](#state_transition-008) | Faster SHA256 for shuffling hashes | partial | low | M | cpu |
| [state_transition-009](#state_transition-009) | Whole-list swap-or-not shuffling | implemented | low | S | cpu |
| [state_transition-010](#state_transition-010) | Altona optimization batch (unspecified) | n/a | low | S | cpu |
| [state_transition-011](#state_transition-011) | Amortize hashing in proposer and sync committee selection | partial | low | S | cpu |
| [state_transition-012](#state_transition-012) | Append builders directly at fork upgrade | implemented | low | S | cpu |
| [state_transition-013](#state_transition-013) | Free-slot cursor when onboarding builders | partial | low | S | cpu |
| [state_transition-014](#state_transition-014) | Pubkey index for builder registry lookups | partial | low | M | cpu |
| [state_transition-015](#state_transition-015) **★** | Verify pending deposit signatures lazily, once per pubkey | partial | medium | S | cpu |
| [state_transition-016](#state_transition-016) | Background verification of pending deposit signatures | implemented | low | S | cpu, latency |
| [state_transition-017](#state_transition-017) | Compute shuffling on a worker thread | n/a | low | S | latency, cpu |
| [state_transition-018](#state_transition-018) | Read validators via read-only references, not copies | partial | low | S | cpu, memory, latency |
| [state_transition-019](#state_transition-019) | Avoid block copies during replay | implemented | low | S | cpu, memory |
| [state_transition-020](#state_transition-020) | Use tracked max index in attestation bounds check | n/a | low | S | cpu |
| [state_transition-021](#state_transition-021) | Cache and incrementally update exit queue churn | implemented | low | S | cpu, memory |
| [state_transition-022](#state_transition-022) | Fuse exit-epoch and churn scans | implemented | low | S | cpu |
| [state_transition-023](#state_transition-023) | Carry state root with the state | partial | low | M | cpu |
| [state_transition-024](#state_transition-024) | Use known state roots in per-slot processing | implemented | medium | S | cpu, latency |
| [state_transition-025](#state_transition-025) | Previous-slot root via incremental tree hash | implemented | low | S | cpu |
| [state_transition-026](#state_transition-026) | Recompute state root instead of DB read | n/a | low | S | disk, latency |
| [state_transition-027](#state_transition-027) | Avoid full beacon state copies | implemented | low | S | cpu, memory |
| [state_transition-028](#state_transition-028) | Copy-on-write for large state fields | implemented | low | S | memory, cpu |
| [state_transition-029](#state_transition-029) | Hash fixed-size values from raw bytes | n/a | low | S | cpu |
| [state_transition-030](#state_transition-030) | Avoid temporary hash sets in hot paths | partial | low | S | cpu, memory |
| [state_transition-031](#state_transition-031) | Skip pubkey index build in deposit requests | implemented | low | S | cpu |
| [state_transition-032](#state_transition-032) | Update pubkey map in place on append | implemented | low | S | cpu, memory |
| [state_transition-033](#state_transition-033) | Pubkey-to-index map for O(1) validator lookups | partial | low | M | cpu, memory, latency |
| [state_transition-034](#state_transition-034) | Pubkey index held in memory with state | implemented | low | S | disk, latency |
| [state_transition-035](#state_transition-035) | Bloom filter for new-deposit pubkey checks | n/a | low | S | cpu |
| [state_transition-036](#state_transition-036) | Split pubkey cache into finalized and unfinalized | implemented | low | S | memory, cpu |
| [state_transition-037](#state_transition-037) | Per-block block-root cache and batched proposer reward | partial | low | S | cpu |
| [state_transition-038](#state_transition-038) | Compute same-slot attestation cache once per block | partial | low | S | cpu |
| [state_transition-039](#state_transition-039) | Batch-verify deposit signatures in a block | partial | low | M | cpu |
| [state_transition-040](#state_transition-040) | Cache committees/shuffling on the state | implemented | low | S | cpu |
| [state_transition-041](#state_transition-041) | Build all caches eagerly at known points | implemented | low | S | cpu, latency |
| [state_transition-042](#state_transition-042) | Per-epoch context object for fast transition | implemented | low | L | cpu |
| [state_transition-043](#state_transition-043) | Use the cached fast slot processing everywhere | n/a | low |  | cpu |
| [state_transition-044](#state_transition-044) | Epoch cache of effective balances | implemented | low | S | cpu, memory |
| [state_transition-045](#state_transition-045) | Read epoch from cached context | n/a | low |  | cpu |
| [state_transition-046](#state_transition-046) | Cache the beacon proposer index per slot | implemented | low | S | cpu |
| [state_transition-047](#state_transition-047) | Direct sampling for proposer index | implemented | low | S | cpu |
| [state_transition-048](#state_transition-048) | Cache signature domains per fork | not | low | S | cpu |
| [state_transition-049](#state_transition-049) | Cheap eth1 data equality in vote counting | not | low | S | cpu |
| [state_transition-050](#state_transition-050) | Skip eth1 vote tallying until majority is possible | not | low | S | cpu, sync |
| [state_transition-051](#state_transition-051) | No Eth1Data copy per eth1 vote loop iteration | n/a | low |  | cpu, memory |
| [state_transition-052](#state_transition-052) | Sync committee index cache per period | not | low | S | cpu, memory |
| [state_transition-053](#state_transition-053) | Indices-only sync committee getter | n/a | low |  | cpu |
| [state_transition-054](#state_transition-054) **★** | Skip validator tree reads in withdrawals | not | medium | M | cpu |
| [state_transition-055](#state_transition-055) | Bound the withdrawals sweep | implemented | low | S | cpu |
| [state_transition-056](#state_transition-056) | Cached length for copy-on-write slice append | n/a | low |  | cpu |
| [state_transition-057](#state_transition-057) | Flat validator array beside tree state | implemented | medium | S | cpu, memory |
| [state_transition-058](#state_transition-058) | Flat arrays with page-table reads | n/a | low |  | cpu |
| [state_transition-059](#state_transition-059) | Cheap zero check for sync committee | n/a | low |  | cpu |
| [state_transition-060](#state_transition-060) | Chunk-granular state delta edits | n/a | low |  | cpu, memory |
| [state_transition-061](#state_transition-061) | Columnar state with delta overlays | n/a | medium |  | cpu, memory |
| [state_transition-062](#state_transition-062) | In-place rebase of deltas on finalization | n/a | low |  | cpu, memory |
| [state_transition-063](#state_transition-063) | Collect signature sets for later batch verify | implemented | low | S | cpu |
| [state_transition-064](#state_transition-064) | Verify block operation signatures in parallel | implemented | low | S | cpu, latency |
| [state_transition-065](#state_transition-065) | Compute all committees of a slot at once | implemented | low | S | cpu |
| [state_transition-066](#state_transition-066) | Compute post-state once per slot | n/a | medium |  | cpu, disk |
| [state_transition-067](#state_transition-067) | Genesis validators root as constant | implemented | low | S | cpu |
| [state_transition-068](#state_transition-068) | Copy committee out of shuffled list | n/a | low |  | memory |
| [state_transition-069](#state_transition-069) | Copy field tries for late blocks | n/a | low |  | cpu, latency |
| [state_transition-070](#state_transition-070) | Hand-written copy for small state objects | n/a | low |  | cpu |
| [state_transition-071](#state_transition-071) | Honor deadlines in multi-slot advance | n/a | low |  | cpu |
| [state_transition-072](#state_transition-072) | Invalidate participation hash once per block | n/a | low | S | cpu |
| [state_transition-073](#state_transition-073) | Cheaper dirty-index tracking in hash tree | n/a | low |  | cpu |
| [state_transition-074](#state_transition-074) | Early block operation length checks | implemented | low | S | cpu |
| [state_transition-075](#state_transition-075) | Reject wrong-fork blocks early | implemented | low | S | cpu |
| [state_transition-076](#state_transition-076) | Early-exit pending withdrawal existence check | not | low | S | cpu |
| [state_transition-077](#state_transition-077) | Cheaper payload timeliness committee computation | partial | low | S | cpu |
| [state_transition-078](#state_transition-078) | Scale genesis building to large deposit sets | n/a | low |  | cpu, startup |
| [state_transition-079](#state_transition-079) | Genesis constructor without deposits | not | low | M | startup, cpu |
| [state_transition-080](#state_transition-080) | Build genesis incrementally as deposits arrive | n/a | low |  | cpu, startup |
| [state_transition-081](#state_transition-081) | Remove slow paths in large simulations | implemented | low | S | cpu |
| [state_transition-082](#state_transition-082) | Correct fixed-length vector initialization | n/a | low |  | memory |
| [state_transition-083](#state_transition-083) | Fixed-size arrays for root vectors | n/a | low |  | memory, cpu |
| [state_transition-084](#state_transition-084) | Hardware sqrt for integer square root | not | low | S | cpu |
| [state_transition-085](#state_transition-085) | Hoist epoch and lock out of validator loop | n/a | low |  | cpu |
| [state_transition-086](#state_transition-086) | Inclusion slot map for rewards | implemented | low | S | cpu |
| [state_transition-087](#state_transition-087) | Lightweight asserts in hot paths | n/a | low | S | cpu |
| [state_transition-088](#state_transition-088) | Lazy pubkey parsing and clean reads | partial | low | L | cpu |
| [state_transition-089](#state_transition-089) | Linear scan for state diff on load | implemented | low | S | cpu, latency |
| [state_transition-090](#state_transition-090) | Bulk-build persistent validators list | implemented | low | S | cpu |
| [state_transition-091](#state_transition-091) | Bound empty-slot fill before allocation | n/a | low |  | memory |
| [state_transition-092](#state_transition-092) | Bulk validator iterator taking the lock once | n/a | low |  | cpu |
| [state_transition-093](#state_transition-093) | Simpler Merkle branch verification loop | implemented | low | S | cpu |
| [state_transition-094](#state_transition-094) | Swap-or-not shuffle and sampling in native code | n/a | low | S | cpu |
| [state_transition-095](#state_transition-095) | Native typed beacon state instead of protobuf wrapper | n/a | low | S | memory, cpu |
| [state_transition-096](#state_transition-096) | Native state transition backend fed with serialized bytes | n/a | low | S | cpu, memory |
| [state_transition-097](#state_transition-097) | Next-epoch committee cache including registry update | implemented | medium | S | cpu |
| [state_transition-098](#state_transition-098) | Trusted no-verify path for replaying known blocks | implemented | low | S | cpu, memory, latency |
| [state_transition-099](#state_transition-099) | Machine integers instead of bigints for balances | n/a | low | S | cpu, memory |
| [state_transition-100](#state_transition-100) | Run state transition in a worker thread | n/a | low | S | cpu, latency |
| [state_transition-101](#state_transition-101) | Packed u32 arrays for shuffling and committees | partial | low | M | memory |
| [state_transition-102](#state_transition-102) | Parallel per-validator epoch processing, no quadratic loops | partial | low | L | cpu |
| [state_transition-103](#state_transition-103) | Parallel swap-or-not shuffle across threads | not | low | M | cpu, memory, latency |
| [state_transition-104](#state_transition-104) | Peek, not consume, in state-root iterator during replay | implemented | low | S | cpu |
| [state_transition-105](#state_transition-105) | Per-pubkey index of pending deposits | implemented | low | S | cpu |
| [state_transition-106](#state_transition-106) | Per-slot lock to dedup head state advance | n/a | medium | S | cpu, memory, latency |
| [state_transition-107](#state_transition-107) | Persistent tree vectors with non-power-of-two length | implemented | low | S | memory, cpu |
| [state_transition-108](#state_transition-108) | Upgrade persistent data structure library for stable timing | n/a | low | S | latency, cpu |
| [state_transition-109](#state_transition-109) | Pipeline independent state transition steps | partial | low | M | cpu, latency |
| [state_transition-110](#state_transition-110) **★** | Pre-verify builder deposit signatures before fork | partial | high | M | cpu, latency |
| [state_transition-111](#state_transition-111) **★** | Preallocate vectors with known capacity | partial | medium | S | cpu, memory |
| [state_transition-112](#state_transition-112) | Speculatively advance head state before next slot | implemented | medium | S | latency, cpu |
| [state_transition-113](#state_transition-113) | Integer sqrt with primitive arithmetic | implemented | low | S | cpu, memory |
| [state_transition-114](#state_transition-114) | Proposer index from shuffling cache | partial | low | M | cpu |
| [state_transition-115](#state_transition-115) | Tune incremental vs full rebuild threshold for field tries | n/a | medium | S | cpu |
| [state_transition-116](#state_transition-116) | Read tree-backed state fields once into locals | n/a | low | S | cpu |
| [state_transition-117](#state_transition-117) | Read proposers from stored proposer_lookahead | implemented | medium | S | cpu |
| [state_transition-118](#state_transition-118) | Read-only bulk traversal of tree-backed lists | implemented | medium | S | memory, cpu |
| [state_transition-119](#state_transition-119) | Remove duplicated check in Electra block processing | implemented | low | S | cpu |
| [state_transition-120](#state_transition-120) | Compute committees once for assignment | partial | low | S | cpu |
| [state_transition-121](#state_transition-121) | Direct balances access without proxy wrapper | n/a | low | S | cpu |
| [state_transition-122](#state_transition-122) | Linear deposit processing for many deposits | implemented | low | S | cpu |
| [state_transition-123](#state_transition-123) | Avoid double copy of randao mix | n/a | low | S | cpu, memory |
| [state_transition-124](#state_transition-124) | Skip slot processing when state already at target | implemented | medium | S | cpu, startup, latency |
| [state_transition-125](#state_transition-125) | Avoid per-committee temporary allocations in transition | partial | low | S | cpu, memory |
| [state_transition-126](#state_transition-126) | Reuse hasher and scratch buffers in sync selection | partial | low | S | cpu, memory |
| [state_transition-127](#state_transition-127) | Reuse computed next-epoch proposer indices | implemented | low | S | cpu, latency |
| [state_transition-128](#state_transition-128) | Reuse pre-advanced state across validation, import, replay | partial | low | S | cpu, latency |
| [state_transition-129](#state_transition-129) | Reuse checkpoint state for attestation production | implemented | medium | S | cpu, latency |
| [state_transition-130](#state_transition-130) | Reuse attesting indices cache in block import | implemented | low | S | cpu |
| [state_transition-131](#state_transition-131) | Cache the full epoch shuffling per seed | implemented | low | S | cpu |
| [state_transition-132](#state_transition-132) | Per-index shuffle with per-index cache | n/a | low |  | cpu, memory |
| [state_transition-133](#state_transition-133) | Pass committee cache into voluntary exit processing | n/a | low |  | cpu |
| [state_transition-134](#state_transition-134) | Reuse destination tree buffers on state copy | n/a | low |  | memory, cpu |
| [state_transition-135](#state_transition-135) **★** | Reuse tree nodes and hashes at fork upgrade | partial | medium | M | cpu, latency, memory |
| [state_transition-136](#state_transition-136) | Mutate state in place in fork upgrade | implemented | low | S | cpu, memory |
| [state_transition-137](#state_transition-137) | Roll back on failure instead of cloning state | n/a | medium |  | cpu, memory |
| [state_transition-138](#state_transition-138) | Keep state small to cheapen clones | implemented | low | S | cpu, memory |
| [state_transition-139](#state_transition-139) | Sample PTC per committee without concatenation | not | low | S | memory, cpu |
| [state_transition-140](#state_transition-140) | Share pubkey caches across epoch-context copies | implemented | medium | S | cpu, memory |
| [state_transition-141](#state_transition-141) | Carry pubkey index cache across fork upgrade | implemented | low | S | cpu, latency |
| [state_transition-142](#state_transition-142) | Scan registry backwards for deposit pubkeys | implemented | low | S | cpu |
| [state_transition-143](#state_transition-143) | Sync signature checks independent of exact state | implemented | medium | S | cpu, memory |
| [state_transition-144](#state_transition-144) | Single shared shuffled-index computation for sampling | not | low | M | cpu |
| [state_transition-145](#state_transition-145) | Single-pass participation flag update | implemented | medium | S | cpu, memory |
| [state_transition-146](#state_transition-146) | Skip deposit crypto when building test genesis | not | low | S | cpu, startup |
| [state_transition-147](#state_transition-147) | Skip mock genesis when loading stored state | n/a | low | S | startup |
| [state_transition-148](#state_transition-148) | Skip deposit-count check after bridge transition | n/a | low | S | cpu |
| [state_transition-149](#state_transition-149) | Scan pending deposits only for blocks with deposits | n/a | low | S | cpu |
| [state_transition-150](#state_transition-150) | Skip pubkey cache build in no-verify replay | not | low | M | cpu, startup |
| [state_transition-151](#state_transition-151) | Avoid redundant deposit pubkey decompression | implemented | low | S | cpu |
| [state_transition-152](#state_transition-152) | Skip registry update on skip slots | n/a | low | S | cpu, latency |
| [state_transition-153](#state_transition-153) | Drop stale slot ticks; small tier indices | n/a | low | S | cpu |
| [state_transition-154](#state_transition-154) | Advance next epoch only when lookahead needs it | implemented | low | S | cpu, latency |
| [state_transition-155](#state_transition-155) | Skip pre-fork withdrawal calc; single pass | implemented | low | S | cpu |
| [state_transition-156](#state_transition-156) | Slashed-validator bitset cache | implemented | medium | S | memory, cpu |
| [state_transition-157](#state_transition-157) | Native slice instead of per-byte copy | implemented | low | S | cpu |
| [state_transition-158](#state_transition-158) | Specialized converters for hot structs | n/a | low | S | cpu |
| [state_transition-159](#state_transition-159) | Compare against static default value | not | low | S | cpu |
| [state_transition-160](#state_transition-160) | Plain structs for pending queue items | implemented | medium | S | cpu |
| [state_transition-161](#state_transition-161) | Structural equality instead of serialize-and-compare | implemented | low | S | cpu, memory |
| [state_transition-162](#state_transition-162) | Tree-backed state in tests | n/a | low | S | cpu |
| [state_transition-163](#state_transition-163) | Return read-only validator wrapper by value | n/a | low | S | memory, cpu |
| [state_transition-164](#state_transition-164) | Zero-copy validator pubkey access | implemented | low | S | cpu, memory |
| [state_transition-165](#state_transition-165) | Pass large inputs by reference, not by value | implemented | low | S | cpu, memory |
| [state_transition-166](#state_transition-166) | Append into one shared output buffer | implemented | low | S | cpu, memory |
| [state_transition-167](#state_transition-167) | Mutate one epoch context in place across transition | implemented | low | S | cpu, memory |
| [state_transition-168](#state_transition-168) | Cache sync participant reward per epoch | partial | low | S | cpu |
| [state_transition-169](#state_transition-169) | Store payload timeliness committee window in state | implemented | low | S | cpu |
| [state_transition-170](#state_transition-170) | Order operation validity checks cheapest first | implemented | low | S | cpu |
| [state_transition-171](#state_transition-171) | Compact participation flag arrays with index accessors | implemented | low | S | memory, cpu |
| [state_transition-172](#state_transition-172) | Make debug state and block dumps opt-in | implemented | low | S | cpu, disk, latency |
| [state_transition-173](#state_transition-173) | Remove spec-dropped vectors from beacon state | implemented | low | S | cpu, memory |
| [state_transition-174](#state_transition-174) | Hold state as persistent tree throughout the node | implemented | high | L | cpu, memory |

★ actionable. Click an id for the full record.

## Ideas

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


<a id="state_transition-002"></a>
<details>
<summary><b>state_transition-002</b> Incremental deposit Merkle tree at genesis — <i>implemented · low · S · cpu, startup</i></summary>

**Idea.** When building the genesis state from deposits, maintain one incremental deposit Merkle tree (and a pubkey-to-index table) instead of recomputing the deposit root or generating a proof per deposit. Genesis construction becomes linear in the deposit count.

**Impact.** Genesis-only, testnet path; already linear (O(n * depth)).

**Best measured result.** None (pr:lighthouse#834)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/genesis/src/common.rs:9-38`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/genesis/src/common.rs#L9-L38)
- [`consensus/state_processing/src/genesis.rs:36-45`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/genesis.rs#L36-L45)
- [`consensus/state_processing/src/common/deposit_data_tree.rs:33-55`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/deposit_data_tree.rs#L33-L55)

**Skeptic check.** Both genesis_deposits and initialize_beacon_state_from_eth1 keep one incremental MerkleTree with cached node hashes (push_leaf, root from cached tree hash), and apply_deposit looks pubkeys up via the pubkey cache. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus@b022dc4d1](https://github.com/status-im/nimbus-eth2/commit/b022dc4d1fd8), [lighthouse#834](https://github.com/sigp/lighthouse/pull/834)

</details>


<a id="state_transition-003"></a>
<details>
<summary><b>state_transition-003</b> Cache total active balance per epoch and use it — <i>implemented · low · S · cpu</i></summary>

**Idea.** Compute the total active balance once per epoch, keep it in a state or epoch cache, and make the total-active-balance helper read that cache instead of summing over all validators for each attestation, base reward or churn computation. Block processing and replay then do no per-call validator scans for it.

**Impact.** Already cached; no per-call validator scans.

**Best measured result.** None (pr:nimbus#4434)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:819`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L819) total_active_balance Option&lt;(Epoch,u64)&gt; cache in state
- [`consensus/types/src/state/beacon_state.rs:2682`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2682) get_total_active_balance_at_epoch reads cache or errors (no fallback scan)
- [`consensus/types/src/state/beacon_state.rs:2701`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2701) set_total_active_balance from single-pass epoch processing
- [`consensus/state_processing/src/per_block_processing/altair/sync_committee.rs:90`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/altair/sync_committee.rs#L90) sync aggregate reads cached value

**Skeptic check.** Getter returns the cached value or an error, never rescans; epoch processing sets it in single pass. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#4434](https://github.com/status-im/nimbus-eth2/pull/4434), [lighthouse#2560](https://github.com/sigp/lighthouse/pull/2560), [ethlambda#648](https://github.com/lambdaclass/ethlambda/pull/648), [prysm#9152](https://github.com/OffchainLabs/prysm/pull/9152), [prysm#9469](https://github.com/OffchainLabs/prysm/pull/9469)

</details>


<a id="state_transition-004"></a>
<details>
<summary><b>state_transition-004</b> Cache base reward per increment per epoch — <i>implemented · low · S · cpu</i></summary>

**Idea.** Compute base_reward_per_increment (which needs an integer sqrt of total active balance) once per epoch in the epoch cache, and in attestation processing sum effective-balance increments over attesters then multiply once. This removes per-attester and per-attestation recomputation.

**Impact.** Already done; isqrt once per epoch, per-attester reward is a table lookup.

**Best measured result.** None (pr:lodestar#2626)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/epoch_cache.rs:96`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/epoch_cache.rs#L96) base_reward_per_increment and per-effective-balance base_rewards table computed once per epoch
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:280`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L280) attestation rewards via state.get_base_reward(index) table lookup
- [`consensus/state_processing/src/common/altair.rs:23`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/altair.rs#L23) get_base_reward takes precomputed BaseRewardPerIncrement

**Skeptic check.** Lighthouse does a per-attester table lookup instead of summing increments then multiplying once; same effect (no recomputation). Sync aggregate does one isqrt per block, negligible.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@54ec19ebb](https://github.com/ChainSafe/lodestar/commit/54ec19ebb9e7), [lodestar#2626](https://github.com/ChainSafe/lodestar/pull/2626)

</details>


<a id="state_transition-005"></a>
<details>
<summary><b>state_transition-005</b> Allocation-free swap-or-not shuffle and hashing — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Implement the swap-or-not shuffle so its inner loop does not allocate intermediate sequences or a digest per hash: reuse one hasher and fixed stack buffers per call and read the 32-byte digest in place. Shuffles do thousands of hashes, so this removes most allocations in committee computation and replay.

**Impact.** Already allocation-free.

**Best measured result.** None (pr:nimbus#1547)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/swap_or_not_shuffle/src/shuffle_list.rs:11`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/swap_or_not_shuffle/src/shuffle_list.rs#L11) stack Buf [u8;37] and hash_fixed returning [u8;32], no heap alloc
- [`consensus/swap_or_not_shuffle/src/compute_shuffled_index.rs:52`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/swap_or_not_shuffle/src/compute_shuffled_index.rs#L52) Context hashing over stack slices

**Skeptic check.** Whole-list shuffle (used for committee cache) reuses one stack buffer with hash_fixed; no per-hash allocation. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#1547](https://github.com/status-im/nimbus-eth2/pull/1547), [lodestar@6078dc9e1](https://github.com/ChainSafe/lodestar/commit/6078dc9e1294), [teku#6189](https://github.com/Consensys-Incorporated/teku/pull/6189), [caplin#22390](https://github.com/erigontech/erigon/pull/22390), [lighthouse#867](https://github.com/sigp/lighthouse/pull/867)

</details>


<a id="state_transition-006"></a>
<details>
<summary><b>state_transition-006</b> Check-free byte conversions in shuffle inner loop — <i>implemented · low · S · cpu</i></summary>

**Idea.** In the swap-or-not shuffle inner loop, build hash inputs and read the pivot u64 with infallible fixed-size array conversions or direct little-endian loads instead of length-checked slice helpers. This removes a branch and panic path per iteration.

**Impact.** Equivalent; the source PR measured no difference.

**Best measured result.** Benchmarks showed no difference (pr:lighthouse#6483)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/swap_or_not_shuffle/src/shuffle_list.rs:36`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/swap_or_not_shuffle/src/shuffle_list.rs#L36) copy_from_slice from fixed digest into [u8;8] then from_le_bytes
- [`consensus/swap_or_not_shuffle/src/compute_shuffled_index.rs:77`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/swap_or_not_shuffle/src/compute_shuffled_index.rs#L77) bytes_to_int64 similar

**Skeptic check.** Conversions are on fixed-size arrays with constant ranges, so bounds checks are compiled out; lighthouse#6483 measured no difference.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#12690](https://github.com/OffchainLabs/prysm/pull/12690), [lighthouse#6483](https://github.com/sigp/lighthouse/pull/6483)

</details>


<a id="state_transition-007"></a>
<details>
<summary><b>state_transition-007</b> Inline per-index work in shuffle loop — <i>implemented · low · S · cpu</i></summary>

**Idea.** Inline the per-position step of the swap-or-not shuffle instead of calling a function or closure per index, and reuse each round hash across positions. Non-hash CPU time in the shuffle drops by about half.

**Impact.** Per-position step is an #[inline(always)] branchless masked_swap inside the loop; round hash recomputed only every 256 positions and byte only every 8.

**Best measured result.** None (pr:lodestar#2353)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/swap_or_not_shuffle/src/shuffle_list.rs:53-63`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/swap_or_not_shuffle/src/shuffle_list.rs#L53-L63)
- [`consensus/swap_or_not_shuffle/src/shuffle_list.rs:116-130`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/swap_or_not_shuffle/src/shuffle_list.rs#L116-L130)

**Skeptic check.** Verified the inner loop has no per-index function call or closure beyond the inline(always) swap. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#2353](https://github.com/ChainSafe/lodestar/pull/2353)

</details>


<a id="state_transition-008"></a>
<details>
<summary><b>state_transition-008</b> Faster SHA256 for shuffling hashes — <i>partial · low · M · cpu</i></summary>

**Idea.** Use a faster SHA256 implementation (batched or hardware-accelerated) for the swap-or-not shuffling round hashes, so committee shuffling per epoch costs less CPU.

**Gap in Lighthouse.** Batch the per-round position hashes in shuffle_list (compute all n/256 digests for a round up front with a multi-buffer/SIMD sha256) in shuffle_list.rs.

**Impact.** Shuffling a 1M-validator set is ~370k hashes per epoch, tens of ms of CPU; batching could trim part of that. Marginal.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/swap_or_not_shuffle/src/shuffle_list.rs:47`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/swap_or_not_shuffle/src/shuffle_list.rs#L47) hash() via ethereum_hashing::hash_fixed (runtime SHA-NI/ring dispatch)
- [`consensus/swap_or_not_shuffle/src/shuffle_list.rs:92-170`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/swap_or_not_shuffle/src/shuffle_list.rs#L92-L170) one sequential hash per 256 positions per round

**Sources.** [lodestar#10471](https://github.com/ChainSafe/lodestar/pull/10471)

</details>


<a id="state_transition-009"></a>
<details>
<summary><b>state_transition-009</b> Whole-list swap-or-not shuffling — <i>implemented · low · S · cpu</i></summary>

**Idea.** Shuffle or unshuffle the entire active-index list in one list-wise pass with the swap-or-not round structure (one hash per 256 positions, flip pivots per round), instead of computing the shuffled position of each index separately. This needs far fewer hash calls per epoch shuffling.

**Impact.** Already done on the epoch committee shuffling path, which is what the member PRs changed.

**Best measured result.** None (pr:teku#2539)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/swap_or_not_shuffle/src/shuffle_list.rs:92`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/swap_or_not_shuffle/src/shuffle_list.rs#L92) shuffle_list: whole-list swap-or-not, one pivot hash per round, one source hash per 256 positions (lines 116, 124, 139)
- [`consensus/types/src/state/committee_cache.rs:147`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L147) epoch committee shuffling uses shuffle_list

**Skeptic check.** Confirmed: CommitteeCache::initialized shuffles the whole active list with shuffle_list. compute_shuffled_index stays only in proposer, sync-committee and balance-weighted selection (beacon_state.rs:1372, 1800, 3725), which the spec defines per index and the member PRs did not touch.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#2539](https://github.com/Consensys-Incorporated/teku/pull/2539), [lodestar@7bbe89b18](https://github.com/ChainSafe/lodestar/commit/7bbe89b18fc2), [lodestar@a2b934e33](https://github.com/ChainSafe/lodestar/commit/a2b934e33116), [nimbus@8baab40ea](https://github.com/status-im/nimbus-eth2/commit/8baab40ea604)

</details>


<a id="state_transition-010"></a>
<details>
<summary><b>state_transition-010</b> Altona optimization batch (unspecified) — <i>n/a · low · S · cpu</i></summary>

**Idea.** A batch of state-transition optimizations shipped for the Altona testnet; the specific techniques are not recorded. Check the original diff before comparing with Lighthouse.

**Gap in Lighthouse.** Unspecified 2020 batch (title 'Proto/altona optimization', no description); not judgeable and Lighthouse's equivalents predate it.

**Impact.** None identifiable.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/committee_cache.rs:147`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L147) shuffle_list already whole-list

**Sources.** [lodestar#1120](https://github.com/ChainSafe/lodestar/pull/1120), [lodestar@b8ca543b9](https://github.com/ChainSafe/lodestar/commit/b8ca543b9bab)

</details>


<a id="state_transition-011"></a>
<details>
<summary><b>state_transition-011</b> Amortize hashing in proposer and sync committee selection — <i>partial · low · S · cpu</i></summary>

**Idea.** In Electra proposer and sync committee selection, hash once per 16 candidates and take 2-byte random values from the cached 32-byte digest, instead of hashing for every candidate.

**Gap in Lighthouse.** Cache the last (i/16, digest) in compute_proposer_index and compute_balance_weighted_selection/acceptance and slice from it.

**Impact.** Saves ~15/16 of one hash per candidate; each candidate also costs ~180 hashes in compute_shuffled_index, so the saving is about 0.5% of selection cost, once per epoch.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:1503`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1503) shuffling_random_u16_electra hashes per candidate, i/16 preimage, no cache (also allocs seed.to_vec)
- [`consensus/types/src/state/beacon_state.rs:1353`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1353) compute_proposer_index calls it per candidate
- [`consensus/types/src/state/beacon_state.rs:3704`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3704) compute_balance_weighted_selection same

**Sources.** [teku#8916](https://github.com/Consensys-Incorporated/teku/pull/8916)

</details>


<a id="state_transition-012"></a>
<details>
<summary><b>state_transition-012</b> Append builders directly at fork upgrade — <i>implemented · low · S · cpu</i></summary>

**Idea.** At the fork that creates the builder registry, append onboarded builders directly with a dedicated append function instead of an add-or-update routine that scans the registry per deposit, removing an O(n^2) scan.

**Impact.** Fork-time onboarding already O(n): builders accumulated in a local Vec with a pubkey-&gt;index HashMap and written once, skipping add_builder_to_registry.

**Best measured result.** None (pr:lodestar#9840)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/upgrade/gloas.rs:221-300`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/upgrade/gloas.rs#L221-L300)

**Skeptic check.** Verified onboard_builders_from_pending_deposits asserts an empty registry and appends directly instead of calling add_builder_to_registry/get_index_for_new_builder per deposit. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#9840](https://github.com/ChainSafe/lodestar/pull/9840)

</details>


<a id="state_transition-013"></a>
<details>
<summary><b>state_transition-013</b> Free-slot cursor when onboarding builders — <i>partial · low · S · cpu</i></summary>

**Idea.** When adding several builders in one block, keep a running next-free-index cursor across deposits instead of rescanning the builder registry for a reusable slot per deposit, turning O(n^2) into O(n).

**Gap in Lighthouse.** Per-block path: process_builder_deposit_requests calls process_builder_deposit_request per request, which does a linear builders().iter().position() pubkey scan and then add_builder_to_registry -&gt; get_index_for_new_builder, which rescans the whole registry from index 0 for a free slot each time (TODO(gloas) comment admits it). No next-free-index cursor is carried across requests in a block (Nimbus #9137 passes next_index through process_builder_deposit_request), and no pubkey-&gt;builder index map.

**Impact.** Block processing cost O(k * n_builders) per block with k builder deposits; negligible while the builder registry is small, grows with registry size.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/process_operations.rs:913-943`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L913-L943)
- [`consensus/types/src/state/beacon_state.rs:2480-2525`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2480-L2525)
- [`consensus/state_processing/src/upgrade/gloas.rs:221-300`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/upgrade/gloas.rs#L221-L300)

**Skeptic check.** Fork-time onboarding is linear (earlier evidence right there), but the idea targets blocks adding several builders; the per-block path rescans the registry per deposit, which the earlier check did not examine.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [nimbus#9137](https://github.com/status-im/nimbus-eth2/pull/9137)

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

**Sources.** [lighthouse#9345](https://github.com/sigp/lighthouse/pull/9345), [teku#10729](https://github.com/Consensys-Incorporated/teku/pull/10729), [lodestar#10263](https://github.com/ChainSafe/lodestar/pull/10263), [lodestar#9397](https://github.com/ChainSafe/lodestar/pull/9397), [lighthouse#8833](https://github.com/sigp/lighthouse/pull/8833), [teku#10261](https://github.com/Consensys-Incorporated/teku/pull/10261)

</details>


<a id="state_transition-015"></a>
<details>
<summary><b>state_transition-015</b> Verify pending deposit signatures lazily, once per pubkey — <i>partial · medium · S · cpu</i></summary>

**Idea.** When onboarding builders or processing deposit requests, check whether a pubkey has a pending validator deposit with an O(1) per-pubkey status set, and BLS-verify a pending deposit signature only when needed and at most once, instead of eagerly verifying or rescanning the whole pending-deposit queue.

**Gap in Lighthouse.** onboard_builders_from_pending_deposits verifies the signature of every new-validator deposit as it walks the queue (the teku#11155 eager scheme), not lazily. The lazy scheme (teku#11511) records validator deposits per pubkey unverified, and verifies them only when a builder-credential deposit for that pubkey asks is_pending_validator. With the OnboardBuildersCache seeded, the fork-time cost is mostly cache lookups. But the cache pre-verifies every pending deposit in the background. On a cold or absent cache (node started near the fork, replay across the fork, cache: None callers), the fork-time path does one BLS verification per new-validator deposit.

**Impact.** One-time Gloas fork transition: with a cold cache, about N BLS verifications go down to only the pubkeys that builder deposits ask about (teku: 6.8 s -&gt; 81 ms for 10k deposits). It also removes the background pre-verification of the whole queue.

**Best measured result.** None (pr:teku#11511)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/upgrade/gloas.rs:253`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/upgrade/gloas.rs#L253) valid_pending_validator_pubkeys HashSet gives an O(1) pending-validator check (no queue rescan)
- [`consensus/state_processing/src/upgrade/gloas.rs:268-273`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/upgrade/gloas.rs#L268-L273) every new-validator (non-builder) deposit is signature-checked eagerly via is_valid_deposit_signature_cached, whether or not a builder deposit later asks about its pubkey
- [`consensus/state_processing/src/builder_deposits_cache.rs:178`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/builder_deposits_cache.rs#L178) is_valid_deposit_signature_cached: on cache None or miss, verifies inline at the fork
- [`consensus/state_processing/src/builder_deposits_cache.rs:66`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/builder_deposits_cache.rs#L66) seed_from_state / :86 add_new_pending_deposits pre-verify every pending deposit ahead of the fork (eager, off the critical path)
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:883`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L883) process_deposit_requests only pushes to pending queue

**Skeptic check.** Verified that the O(1) set and verify-once-with-writeback are real. The earlier evidence called this lazy, but the code verifies every non-builder new-validator deposit eagerly, either ahead of the fork through the cache or inline when the cache misses.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lodestar#9180](https://github.com/ChainSafe/lodestar/pull/9180), [lodestar#9374](https://github.com/ChainSafe/lodestar/pull/9374), [teku#11155](https://github.com/Consensys-Incorporated/teku/pull/11155), [teku#11511](https://github.com/Consensys-Incorporated/teku/pull/11511), [prysm#17387](https://github.com/OffchainLabs/prysm/pull/17387)

</details>


<a id="state_transition-016"></a>
<details>
<summary><b>state_transition-016</b> Background verification of pending deposit signatures — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Verify BLS signatures of pending deposits in a background task as blocks are imported (and for the anchor state at startup) and cache the results, so the fork-transition block does not verify the whole pending queue at once.

**Impact.** Fork transition block does cache lookups instead of verifying the whole pending queue.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/builder_deposits_cache.rs:41-140`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/builder_deposits_cache.rs#L41-L140)
- [`consensus/state_processing/src/builder_deposits_cache.rs:194-219`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/builder_deposits_cache.rs#L194-L219)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4814-4829`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4814-L4829)
- [`beacon_node/beacon_chain/src/builder.rs:1188-1200`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L1188-L1200)
- [`consensus/state_processing/src/upgrade/gloas.rs:180`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/upgrade/gloas.rs#L180)

**Skeptic check.** Verified seed_from_state at startup from the head state and add_new_pending_deposits after each pre-Gloas block import, both on the low-priority rayon pool with batch verification, and lookup via is_valid_deposit_signature_cached at upgrade. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine@272975377](https://github.com/grandinetech/grandine/commit/272975377a7e)

</details>


<a id="state_transition-017"></a>
<details>
<summary><b>state_transition-017</b> Compute shuffling on a worker thread — <i>n/a · low · S · latency, cpu</i></summary>

**Idea.** Run epoch shuffling computation asynchronously on a worker thread so it does not block the main event loop or block import.

**Gap in Lighthouse.** Lighthouse has no single-threaded JS event loop; state processing and shuffling already run on beacon-processor worker/blocking threads, with a shuffling cache.

**Impact.** Nothing to gain; no event loop to unblock.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/committee_cache.rs:147`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L147) shuffle_list runs synchronously inside state processing
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:317`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L317) cache with shared promises

**Sources.** [lodestar@944104e7d](https://github.com/ChainSafe/lodestar/commit/944104e7db40)

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


<a id="state_transition-019"></a>
<details>
<summary><b>state_transition-019</b> Avoid block copies during replay — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** When replaying blocks to rebuild a state, pass blocks by reference and do not copy block data.

**Impact.** Replay passes &amp;block to per_block_processing and hooks; blinded blocks are moved in once.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/block_replayer.rs:215-270`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/block_replayer.rs#L215-L270)
- [`beacon_node/store/src/hot_cold_store.rs:2579`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2579)

**Skeptic check.** Verified apply_blocks iterates blocks.iter() and passes references throughout; no per-step block clone. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#3284](https://github.com/status-im/nimbus-eth2/pull/3284)

</details>


<a id="state_transition-020"></a>
<details>
<summary><b>state_transition-020</b> Use tracked max index in attestation bounds check — <i>n/a · low · S · cpu</i></summary>

**Idea.** In indexed attestation index-bounds validation, compare against the already-known highest index instead of doing an extra last-element lookup.

**Impact.** Nothing to gain: Lighthouse has no separate last-element lookup; the sorted-unique scan is already one pass.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/is_valid_indexed_attestation.rs:15`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/is_valid_indexed_attestation.rs#L15) - no max-index bounds check; sortedness via tuple_windows

**Sources.** [lodestar#9089](https://github.com/ChainSafe/lodestar/pull/9089)

</details>


<a id="state_transition-021"></a>
<details>
<summary><b>state_transition-021</b> Cache and incrementally update exit queue churn — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Compute the exit queue epoch and churn (only the latest exit epoch, not a map of all exit epochs) at most once per block or epoch, cache it, and update it incrementally as exits are initiated, instead of scanning all validators for each exit or slashing. Blocks with many exits go from O(exits*validators) to O(exits).

**Impact.** Already O(exits) per block.

**Best measured result.** None (pr:teku#7034)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/common/initiate_validator_exit.rs:19`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/initiate_validator_exit.rs#L19) build_exit_cache once per state (cached), pre-Electra max_epoch/get_churn_at
- [`consensus/state_processing/src/common/initiate_validator_exit.rs:45`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/initiate_validator_exit.rs#L45) record_validator_exit incremental update
- [`consensus/types/src/state/beacon_state.rs:3314`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3314) compute_exit_epoch_and_update_churn uses state earliest_exit_epoch/exit_balance_to_consume, no validator scan

**Skeptic check.** Confirmed: the exit cache is built once and updated per exit before Electra. From Electra on, the churn comes from state fields with the cached total active balance.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#15764](https://github.com/OffchainLabs/prysm/pull/15764), [prysm#14990](https://github.com/OffchainLabs/prysm/pull/14990), [teku#7034](https://github.com/Consensys-Incorporated/teku/pull/7034), [nimbus#6161](https://github.com/status-im/nimbus-eth2/pull/6161), [lodestar#2695](https://github.com/ChainSafe/lodestar/pull/2695), [lodestar#2928](https://github.com/ChainSafe/lodestar/pull/2928), [lodestar#1764](https://github.com/ChainSafe/lodestar/pull/1764), [lighthouse#5280](https://github.com/sigp/lighthouse/pull/5280)

</details>


<a id="state_transition-022"></a>
<details>
<summary><b>state_transition-022</b> Fuse exit-epoch and churn scans — <i>implemented · low · S · cpu</i></summary>

**Idea.** In initiate_validator_exit, compute the max exit epoch and the churn count in one pass over validators instead of two passes.

**Impact.** No per-exit validator scans; the exit cache replaces both passes.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/common/initiate_validator_exit.rs:19`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/initiate_validator_exit.rs#L19) build_exit_cache (one scan, cached on state)
- [`consensus/state_processing/src/common/initiate_validator_exit.rs:22-36`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/initiate_validator_exit.rs#L22-L36) Electra churn via compute_exit_epoch_and_update_churn; pre-Electra max_epoch/get_churn_at are O(1) cache reads
- [`consensus/types/src/state/beacon_state.rs:2777-2781`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2777-L2781) build_exit_cache builds only when uninitialized

**Skeptic check.** Verified initiate_validator_exit reads max epoch and churn from ExitCache and records the exit into it; the earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#6146](https://github.com/status-im/nimbus-eth2/pull/6146)

</details>


<a id="state_transition-023"></a>
<details>
<summary><b>state_transition-023</b> Carry state root with the state — <i>partial · low · M · cpu</i></summary>

**Idea.** Keep the computed state root attached to the state (hashed state) through the pipeline and derive the latest block root from the latest block header, so state roots are not recomputed by tree hashing before proposal or on each use.

**Gap in Lighthouse.** Root is carried only as a function argument, not stored with the state; callers without a root recompute via the milhouse cache (incremental).

**Impact.** Saves at most one incremental tree-hash per reuse, small since milhouse caches.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_slot_processing.rs:34-40`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_slot_processing.rs#L34-L40),126-145 - state_root passed in as Option, else update_tree_hash_cache
- [`consensus/types/src/state/beacon_state.rs:1877-1888`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1877-L1888) - latest block root derived from header with filled state root

**Sources.** [nimbus#3096](https://github.com/status-im/nimbus-eth2/pull/3096), [nimbus#260](https://github.com/status-im/nimbus-eth2/pull/260)

</details>


<a id="state_transition-024"></a>
<details>
<summary><b>state_transition-024</b> Use known state roots in per-slot processing — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** When importing or replaying blocks, pass the already known per-slot state root (from the parent block, the block itself, or a stored empty-slot root cache) to slot processing, or skip a root nobody observes, so it does not tree-hash the full state each slot. This saves a full state hash tree root per block and per replayed slot.

**Impact.** Already done on import, replay and cheap advance.

**Best measured result.** None (pr:lighthouse#2863)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_slot_processing.rs:38`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_slot_processing.rs#L38) per_slot_processing takes state_root: Option&lt;Hash256&gt;, cache_state uses it
- [`beacon_node/beacon_chain/src/block_verification.rs:1610`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1610) block import passes parent.beacon_block.state_root() for the first slot; skipped slots hash (roots are stored)
- [`consensus/state_processing/src/block_replayer.rs:176`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/block_replayer.rs#L176) replay takes roots from state_root_iter or the block's state_root
- [`consensus/state_processing/src/state_advance.rs:74`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/state_advance.rs#L74) partial_state_advance skips unobserved roots

**Skeptic check.** Confirmed on the block import path (block_verification.rs:1610), on replay and on partial advance. Note that the earlier citation of block_verification.rs:2175 points to cheap_state_advance_to_obtain_committees, which is the partial path.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#2863](https://github.com/sigp/lighthouse/pull/2863), [nimbus#961](https://github.com/status-im/nimbus-eth2/pull/961), [lighthouse#762](https://github.com/sigp/lighthouse/pull/762), [nimbus#2537](https://github.com/status-im/nimbus-eth2/pull/2537)

</details>


<a id="state_transition-025"></a>
<details>
<summary><b>state_transition-025</b> Previous-slot root via incremental tree hash — <i>implemented · low · S · cpu</i></summary>

**Idea.** In per-slot processing, compute the previous state root with the incremental tree hash cache instead of a full tree_hash_root of the state.

**Impact.** Already done; no further gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_slot_processing.rs:122-130`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_slot_processing.rs#L122-L130) cache_state uses the known state_root or state.update_tree_hash_cache()
- [`consensus/types/src/state/beacon_state.rs:3070-3076`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3070-L3076) milhouse incremental tree hash

**Skeptic check.** cache_state uses a supplied root when known and otherwise the incremental milhouse hash; this is Lighthouse's own commit and the earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@4dd1239b2](https://github.com/sigp/lighthouse/commit/4dd1239b243b)

</details>


<a id="state_transition-026"></a>
<details>
<summary><b>state_transition-026</b> Recompute state root instead of DB read — <i>n/a · low · S · disk, latency</i></summary>

**Idea.** Compute the state root by tree hashing instead of reading it from the database, since hashing is now fast and a DB lookup costs more.

**Impact.** Lighthouse's state transition never reads state roots from DB; hot-path roots come from the caller or the milhouse cache.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_slot_processing.rs:126-130`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_slot_processing.rs#L126-L130) - root is known by caller or computed by incremental hash; no DB read in state transition

**Sources.** [nimbus#1297](https://github.com/status-im/nimbus-eth2/pull/1297)

</details>


<a id="state_transition-027"></a>
<details>
<summary><b>state_transition-027</b> Avoid full beacon state copies — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Do not deep-copy the whole beacon state during state transition: pass views or references, take ownership of states that are not used again, and restore from the head state on failure instead of copying before each transition. This removes multi-MB copies per block and cuts allocations.

**Impact.** State clones are structural-sharing clones, so no multi-MB deep copies on the block path.

**Best measured result.** None (pr:prysm#1232)

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.lock milhouse git rev d67aabd: ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/list.rs:43 List holds Arc&lt;Tree&gt;, progressive_list.rs:18 Arc&lt;ProgressiveTree&gt;
- [`consensus/types/src/state/beacon_state.rs:488`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L488) BeaconState derives Clone over milhouse fields (shallow Arc clones)
- [`consensus/state_processing/src/upgrade/electra.rs:167`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/upgrade/electra.rs#L167) fork upgrades mem::take caches

**Skeptic check.** Confirmed that milhouse lists and vectors clone by Arc. The earlier line citation was off (beacon_state.rs:96 is BeaconStateError; the struct derive is at :488), but the claim is right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#16420](https://github.com/OffchainLabs/prysm/pull/16420), [nimbus#1551](https://github.com/status-im/nimbus-eth2/pull/1551), [nimbus#45](https://github.com/status-im/nimbus-eth2/pull/45), [nimbus#930](https://github.com/status-im/nimbus-eth2/pull/930), [prysm#1232](https://github.com/OffchainLabs/prysm/pull/1232), [prysm#4602](https://github.com/OffchainLabs/prysm/pull/4602), [prysm#9226](https://github.com/OffchainLabs/prysm/pull/9226), [nimbus@fdcbfdff0](https://github.com/status-im/nimbus-eth2/commit/fdcbfdff0564)

</details>


<a id="state_transition-028"></a>
<details>
<summary><b>state_transition-028</b> Copy-on-write for large state fields — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** Share large state fields (validators, balances, roots) between state clones and copy only on mutation, or store them in chunks so a copy shares unchanged chunks. State clones become cheap in time and memory.

**Impact.** Already done via milhouse.

**Best measured result.** None (pr:prysm#4699)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/tree.rs:14 Tree nodes are Arc-shared, mutations rebuild only the touched path
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/progressive_tree.rs:25 progressive lists (Gloas) also share subtrees
- [`consensus/types/src/state/beacon_state.rs:2466`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2466) appends touch only new leaves

**Skeptic check.** Confirmed that validators, balances and roots are persistent milhouse trees with copy-on-write, and that the Gloas ProgressiveList is also persistent. The milhouse source is the git checkout d67aabd, not the registry crate.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#4699](https://github.com/OffchainLabs/prysm/pull/4699), [prysm#12077](https://github.com/OffchainLabs/prysm/pull/12077)

</details>


<a id="state_transition-029"></a>
<details>
<summary><b>state_transition-029</b> Hash fixed-size values from raw bytes — <i>n/a · low · S · cpu</i></summary>

**Idea.** Pass the raw byte arrays of fixed-size values (randao reveal, seed, signature, fork version) straight into hashing instead of re-serializing or copying them through the SSZ type system.

**Impact.** Rust tree_hash hashes fixed arrays directly; the Lodestar cost came from its JS type wrappers.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:3070`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3070) - hashing is via tree_hash crate on native Rust types, no JS-style SSZ view reserialization

**Sources.** [lodestar@8d6e3f093](https://github.com/ChainSafe/lodestar/commit/8d6e3f093a23)

</details>


<a id="state_transition-030"></a>
<details>
<summary><b>state_transition-030</b> Avoid temporary hash sets in hot paths — <i>partial · low · S · cpu, memory</i></summary>

**Idea.** In exit pool, gossip validation and block processing, avoid building temporary hash sets; iterate or test membership directly.

**Gap in Lighthouse.** Block packing builds a temporary HashSet of slashed indices; it is only a few entries and per proposal.

**Impact.** Negligible; runs once per proposal on handful of items.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/lib.rs:507-516`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L507-L516) - to_be_slashed HashSet built for block packing
- [`beacon_node/operation_pool/src/lib.rs:529`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L529) - HashSet&lt;u64&gt; passed through slashing selection

**Sources.** [nimbus#3003](https://github.com/status-im/nimbus-eth2/pull/3003)

</details>


<a id="state_transition-031"></a>
<details>
<summary><b>state_transition-031</b> Skip pubkey index build in deposit requests — <i>implemented · low · S · cpu</i></summary>

**Idea.** Do not build the validator pubkey search structure in process_deposit_request, since that function does not use it.

**Impact.** No pubkey index is built in deposit request processing.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/process_operations.rs:883-909`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L883-L909) process_deposit_requests only sets start index and pushes PendingDeposit

**Skeptic check.** Read process_deposit_requests: no update_pubkey_cache or get_validator_index call; the pubkey lookup happens only later in epoch pending-deposit processing, where it is needed.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#7088](https://github.com/status-im/nimbus-eth2/pull/7088)

</details>


<a id="state_transition-032"></a>
<details>
<summary><b>state_transition-032</b> Update pubkey map in place on append — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** When appending validators during deposit processing, insert only the new pubkey-to-index entries into the existing map, instead of copying or rebuilding the whole map per deposit.

**Impact.** No per-deposit rebuild or copy.

**Best measured result.** None (pr:prysm#6659)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:2466-2474`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2466-L2474) add_validator_to_registry inserts the new pubkey into the cache directly
- [`consensus/types/src/state/beacon_state.rs:2979`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2979) update_pubkey_cache inserts only from iter_from(len)
- [`consensus/types/src/state/pubkey_cache.rs:5`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/pubkey_cache.rs#L5) rpds HashTrieMapSync, insert_mut, persistent cheap clone

**Skeptic check.** Confirmed: the cache is a persistent map with in-place inserts on append, and state clones share it.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#5780](https://github.com/OffchainLabs/prysm/pull/5780), [prysm#6659](https://github.com/OffchainLabs/prysm/pull/6659)

</details>


<a id="state_transition-033"></a>
<details>
<summary><b>state_transition-033</b> Pubkey-to-index map for O(1) validator lookups — <i>partial · low · M · cpu, memory, latency</i></summary>

**Idea.** Keep a pubkey-to-validator (or builder) index map with the state or epoch context, update it as validators are appended, and use it in deposit processing, sync committee index lookup and builder lookup instead of a linear registry scan. Deposit processing becomes linear instead of quadratic.

**Gap in Lighthouse.** Validator lookups are O(1). Builder lookups are not: process_builder_deposit_request and process_builder_exit_request scan the whole builders registry by pubkey for each request (up to 64 deposits and 16 exits per payload). get_index_for_new_builder also scans for each new builder. There is no persistent builder pubkey-&gt;index cache on BeaconState, which prysm#16813 added.

**Impact.** Each payload pays O(requests x builders) compares. This is small today and grows with the builder registry (devnets have ~10k builders).

**Best measured result.** None (pr:teku#3315)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/pubkey_cache.rs:21`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/pubkey_cache.rs#L21) PubkeyCache pubkey-&gt;validator index
- [`consensus/types/src/state/beacon_state.rs:1105`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1105) get_validator_index uses it; :1753 get_sync_committee_indices uses it
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:937`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L937) process_builder_deposit_request: builders().iter().position(pubkey ==) linear scan
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:994`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L994) process_builder_exit_request: linear scan by pubkey
- [`consensus/types/src/state/beacon_state.rs:2480`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2480) add_builder_to_registry -&gt; get_index_for_new_builder linear scan (TODO(gloas) comment)
- [`consensus/state_processing/src/upgrade/gloas.rs:256`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/upgrade/gloas.rs#L256) the fork upgrade alone uses a local builder_pubkey_to_index HashMap

**Skeptic check.** The validator side (deposits, pending deposits, sync committee, withdrawal requests) is confirmed O(1). The idea also names builder lookup, and Lighthouse still scans linearly on the post-fork per-payload builder request paths.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [teku#3315](https://github.com/Consensys-Incorporated/teku/pull/3315), [nimbus#590](https://github.com/status-im/nimbus-eth2/pull/590), [nimbus#6469](https://github.com/status-im/nimbus-eth2/pull/6469), [prysm#4641](https://github.com/OffchainLabs/prysm/pull/4641), [lighthouse#301](https://github.com/sigp/lighthouse/pull/301), [lodestar#504](https://github.com/ChainSafe/lodestar/pull/504), [prysm#16813](https://github.com/OffchainLabs/prysm/pull/16813), [lodestar#1009](https://github.com/ChainSafe/lodestar/pull/1009), [lodestar#9861](https://github.com/ChainSafe/lodestar/pull/9861), [teku#3836](https://github.com/Consensys-Incorporated/teku/pull/3836), [teku#5194](https://github.com/Consensys-Incorporated/teku/pull/5194)

</details>


<a id="state_transition-034"></a>
<details>
<summary><b>state_transition-034</b> Pubkey index held in memory with state — <i>implemented · low · S · disk, latency</i></summary>

**Idea.** Look up validator indices from a pubkey map held with the beacon state instead of a separate database index, removing DB reads and writes on the hot path.

**Impact.** Hot-path pubkey lookups are pure in-memory map reads.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/pubkey_cache.rs:8-14`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/pubkey_cache.rs#L8-L14) in-memory pubkey-&gt;index map held in the state
- [`consensus/types/src/state/beacon_state.rs:1105-1111`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1105-L1111) get_validator_index uses it after incremental update
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:26`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L26) chain-level in-memory map

**Skeptic check.** Verified the per-state PubkeyCache and get_validator_index; no DB reads on the lookup path. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#5383](https://github.com/OffchainLabs/prysm/pull/5383)

</details>


<a id="state_transition-035"></a>
<details>
<summary><b>state_transition-035</b> Bloom filter for new-deposit pubkey checks — <i>n/a · low · S · cpu</i></summary>

**Idea.** For blocks with several deposits, build a Bloom filter of existing validator pubkeys once per block so new-validator deposits skip the registry lookup or scan.

**Impact.** A Bloom filter only avoids a linear scan or costly lookup; Lighthouse already has a hash map lookup (and the cache is kept across blocks), so a per-block filter build (~10ms at 1.5M keys) would cost more than it saves.

**Best measured result.** None (pr:nimbus#5982)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/pubkey_cache.rs:5`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/pubkey_cache.rs#L5) - persistent hash map gives O(1) lookup
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:739`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L739) - existence check is a hash lookup

**Sources.** [nimbus#5982](https://github.com/status-im/nimbus-eth2/pull/5982)

</details>


<a id="state_transition-036"></a>
<details>
<summary><b>state_transition-036</b> Split pubkey cache into finalized and unfinalized — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** Keep a large shared finalized pubkey-to-index cache plus a small per-fork unfinalized map cloned with the state, and move entries on finalization, so new validators do not force copying or invalidating the big shared cache.

**Impact.** State clones share the map structurally; new validators path-copy a few nodes, giving the same effect as a finalized/unfinalized split.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/pubkey_cache.rs:2`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/pubkey_cache.rs#L2),13 rpds HashTrieMapSync persistent map
- [`consensus/types/src/state/beacon_state.rs:2979-2993`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2979-L2993) update_pubkey_cache appends only validators from start_index

**Skeptic check.** Confirmed the persistent rpds map and incremental append; a different mechanism with the same effect (no full copy or invalidation per fork).

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#6042](https://github.com/ChainSafe/lodestar/pull/6042)

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


<a id="state_transition-038"></a>
<details>
<summary><b>state_transition-038</b> Compute same-slot attestation cache once per block — <i>partial · low · S · cpu</i></summary>

**Idea.** Build the per-block same-slot attestation root cache once per block transition and reuse it for every attestation, instead of recomputing it per attestation.

**Gap in Lighthouse.** The Gloas branch calls is_attestation_same_slot inside the per-attester loop; compute it once per attestation before the loop and put the payment_withdrawal_amount&gt;0 test first. No per-block cache exists, but the function is two vector reads.

**Impact.** Saves two array lookups per newly-participating attester in Gloas blocks only; negligible next to tree writes.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:2633`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2633) is_attestation_same_slot does two get_block_root lookups
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:436`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L436) called per attester, only in the Gloas payment path
- [`consensus/state_processing/src/common/get_attestation_participation.rs:43`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/get_attestation_participation.rs#L43) called once per attestation

**Sources.** [lodestar#9664](https://github.com/ChainSafe/lodestar/pull/9664)

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


<a id="state_transition-040"></a>
<details>
<summary><b>state_transition-040</b> Cache committees/shuffling on the state — <i>implemented · low · S · cpu</i></summary>

**Idea.** Compute the shuffling and committees once per epoch (or slot) and store them in a cache on the state object, reused by block processing, attestation processing and duties, instead of recomputing the shuffle on each lookup.

**Impact.** Shuffling computed once per epoch, shared across block processing, attestation verification and duties.

**Best measured result.** None (pr:teku#514)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:825`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L825) committee_caches: [Arc&lt;CommitteeCache&gt;; CACHED_EPOCHS]
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:128`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L128) ShufflingCache
- [`consensus/types/src/state/beacon_state.rs:2768`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2768) build_all_committee_caches

**Skeptic check.** CommitteeCache is held on BeaconState per relative epoch and shared across states via ShufflingCache; earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#234](https://github.com/sigp/lighthouse/pull/234), [teku@b4a317d3f](https://github.com/Consensys-Incorporated/teku/commit/b4a317d3fa24), [lighthouse@a5de6a191](https://github.com/sigp/lighthouse/commit/a5de6a1915b3), [teku#514](https://github.com/Consensys-Incorporated/teku/pull/514), [lighthouse@b211e3933](https://github.com/sigp/lighthouse/commit/b211e39331de)

</details>


<a id="state_transition-041"></a>
<details>
<summary><b>state_transition-041</b> Build all caches eagerly at known points — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Provide a build-all-caches call and run it at block production and import so committee and other caches are built once up front rather than lazily and repeatedly.

**Impact.** Caches built once up front at load, head update and production.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/all_caches.rs:26-31`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/all_caches.rs#L26-L31) build_all_caches
- [`beacon_node/beacon_chain/src/canonical_head.rs:1150`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1150) on new head
- [`beacon_node/store/src/hot_cold_store.rs:1171`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1171),1832,2054,2369 on state load
- [`beacon_node/beacon_chain/src/builder.rs:440`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L440) at startup
- [`beacon_node/beacon_chain/src/block_verification.rs:2185-2207`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L2185-L2207) committee caches before import
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5970-5971`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5970-L5971) production builds total active balance and epoch cache

**Skeptic check.** Verified build_all_caches and its call sites; this is Lighthouse's own commit. Block production and import build the needed caches explicitly, not lazily per access.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@b26f1f8e1](https://github.com/sigp/lighthouse/commit/b26f1f8e1cfd)

</details>


<a id="state_transition-042"></a>
<details>
<summary><b>state_transition-042</b> Per-epoch context object for fast transition — <i>implemented · low · L · cpu</i></summary>

**Idea.** Hold a per-epoch context beside the state (shuffling, proposers, pubkey-to-index and index-to-pubkey maps, flat validator and participation data), implement block and slot processing on it instead of a spec-literal implementation, and clone it with the state. The fast path never recomputes derived data from the tree.

**Impact.** Derived data is not recomputed from the tree on the hot path; flat participation copies would add memory for marginal gain in Rust.

**Best measured result.** None (pr:lodestar#931)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:837`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L837) pubkey_cache, :856 epoch_cache held in state and cloned with it
- [`consensus/state_processing/src/all_caches.rs:26-31`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/all_caches.rs#L26-L31) committee, epoch, progressive balance caches
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:393`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L393) epoch_cache effective balance lookup

**Skeptic check.** Lighthouse holds the per-epoch derived caches (shuffling, proposers, pubkey map, effective balances, progressive balances) with the state; it lacks only flat validator/participation arrays, which matter for Lodestar's JS tree costs, not for milhouse iteration.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@2155ee9a9](https://github.com/ChainSafe/lodestar/commit/2155ee9a9f13), [lodestar@ae5fb1a2b](https://github.com/ChainSafe/lodestar/commit/ae5fb1a2b4b8), [lodestar@56f231c74](https://github.com/ChainSafe/lodestar/commit/56f231c74df3), [lodestar#931](https://github.com/ChainSafe/lodestar/pull/931), [lodestar@2efccac33](https://github.com/ChainSafe/lodestar/commit/2efccac33889)

</details>


<a id="state_transition-043"></a>
<details>
<summary><b>state_transition-043</b> Use the cached fast slot processing everywhere — <i>n/a · low · cpu</i></summary>

**Idea.** Route every caller of slot processing (API, gossip validation, block import) through the optimized cached-context implementation instead of a slow generic spec-style path.

**Impact.** Lighthouse has one slot-processing implementation over the cached state, there is no slow generic path to route away from.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_slot_processing.rs:38`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_slot_processing.rs#L38) single per_slot_processing used by all callers

**Sources.** [lodestar#1111](https://github.com/ChainSafe/lodestar/pull/1111), [lodestar@23f59e123](https://github.com/ChainSafe/lodestar/commit/23f59e123197)

</details>


<a id="state_transition-044"></a>
<details>
<summary><b>state_transition-044</b> Epoch cache of effective balances — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Keep an epoch cache of per-validator effective balances (e.g. a flat array of 1-byte increments) and related values like proposer indices, and read it in block processing instead of reading tree-structured validator records.

**Impact.** Block processing reads flat effective balances; no tree walk.

**Best measured result.** None (pr:lodestar#3718)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/epoch_cache.rs:33`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/epoch_cache.rs#L33) effective_balances: Vec&lt;u64&gt;
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:262`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L262) attestation rewards read epoch_cache().get_effective_balance
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:392`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L392)

**Skeptic check.** EpochCache holds a flat Vec&lt;u64&gt; of effective balances plus base rewards, read on the attestation path in process_operations; proposer indices live in proposer_lookahead post-Fulu. Earlier verdict correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#4429](https://github.com/sigp/lighthouse/pull/4429), [lodestar#3718](https://github.com/ChainSafe/lodestar/pull/3718)

</details>


<a id="state_transition-045"></a>
<details>
<summary><b>state_transition-045</b> Read epoch from cached context — <i>n/a · low · cpu</i></summary>

**Idea.** Read current and previous epoch from a cached context instead of recomputing them from the state slot each time.

**Impact.** current_epoch is one division by a compile-time constant; caching it gains nothing in Rust.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:1114`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1114) current_epoch is slot divided by a constant

**Sources.** [lodestar#3274](https://github.com/ChainSafe/lodestar/pull/3274)

</details>


<a id="state_transition-046"></a>
<details>
<summary><b>state_transition-046</b> Cache the beacon proposer index per slot — <i>implemented · low · S · cpu</i></summary>

**Idea.** Compute the proposer index once per slot (or for all slots of the epoch), cache it in the epoch cache, and reuse it in block processing, signature verification, slashings and rewards instead of recomputing it from the shuffled indices on each call.

**Impact.** Nothing material left on mainnet post-Fulu.

**Best measured result.** None (pr:nimbus#1120)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/consensus_context.rs:104`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/consensus_context.rs#L104) get_proposer_index_no_checks cached per block
- [`consensus/types/src/state/beacon_state.rs:1655`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1655) post-Fulu proposer_lookahead read
- [`beacon_node/beacon_chain/src/builder.rs:758`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L758) BeaconProposerCache

**Skeptic check.** Post-Fulu get_beacon_proposer_index is a lookahead vector read; ConsensusContext caches per block and BeaconProposerCache serves duties/gossip. Only pre-Fulu path recomputes, irrelevant now.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku@91c92e927](https://github.com/Consensys-Incorporated/teku/commit/91c92e927f55), [nimbus#1120](https://github.com/status-im/nimbus-eth2/pull/1120), [lighthouse#3604](https://github.com/sigp/lighthouse/pull/3604), [nimbus@3cb7896ba](https://github.com/status-im/nimbus-eth2/commit/3cb7896bab9e)

</details>


<a id="state_transition-047"></a>
<details>
<summary><b>state_transition-047</b> Direct sampling for proposer index — <i>implemented · low · S · cpu</i></summary>

**Idea.** Select the proposer with a direct sampling loop over shuffled positions (about two probes expected) instead of computing the full shuffle, and derive committee count from the cached active validator count.

**Impact.** Proposer selection costs a few shuffled-index probes.

**Best measured result.** None (pr:nimbus#1312)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:1353`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1353) compute_proposer_index probes compute_shuffled_index per candidate, no full shuffle

**Skeptic check.** Verified compute_proposer_index loops compute_shuffled_index per probe (spec direct sampling); committee count comes from CommitteeCache. Earlier verdict correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#1312](https://github.com/status-im/nimbus-eth2/pull/1312)

</details>


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


<a id="state_transition-049"></a>
<details>
<summary><b>state_transition-049</b> Cheap eth1 data equality in vote counting — <i>not · low · S · cpu</i></summary>

**Idea.** When tallying eth1 data votes, compare votes by cached hash tree root or raw bytes rather than generic SSZ equality.

**Gap in Lighthouse.** get_new_eth1_data scans up to 2048 votes of a milhouse List per block with a 72-byte struct equality; could compare cached tree hash or keep a vote count map. Needs no spec change.

**Impact.** A few microseconds per block at most (list iteration over a tree); not visible in profiles.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing.rs:371`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing.rs#L371) get_new_eth1_data iterates eth1_data_votes and compares with derived PartialEq
- [`consensus/state_processing/src/per_epoch_processing/resets.rs:17`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/resets.rs#L17) votes reset per voting period

**Sources.** [lodestar#1119](https://github.com/ChainSafe/lodestar/pull/1119), [lodestar#2881](https://github.com/ChainSafe/lodestar/pull/2881)

</details>


<a id="state_transition-050"></a>
<details>
<summary><b>state_transition-050</b> Skip eth1 vote tallying until majority is possible — <i>not · low · S · cpu, sync</i></summary>

**Idea.** In eth1 data processing, skip vote counting until the votes in the period could reach a majority (more than half the voting period), and compare votes by cached hash roots. This removes most tallying work, notably in historical sync.

**Gap in Lighthouse.** Add a fast path in get_new_eth1_data that returns None when votes.len()+1 cannot reach more than half of SlotsPerEth1VotingPeriod... (note: Lighthouse PR #1093 was closed unmerged); the check num_votes+1 &gt; period/2 only helps early in the voting period if the remaining slots can't make a majority, which is hard since the current vote can always add up.

**Impact.** Saves up to ~2048 Eth1Data comparisons per block, a few microseconds; only noticeable in historical replay.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing.rs:373`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing.rs#L373) get_new_eth1_data filters all votes every block, no early skip
- [`consensus/state_processing/src/per_block_processing.rs:358`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing.rs#L358) process_eth1_data

**Sources.** [lighthouse#1093](https://github.com/sigp/lighthouse/pull/1093), [lodestar@5a83c7719](https://github.com/ChainSafe/lodestar/commit/5a83c7719c61)

</details>


<a id="state_transition-051"></a>
<details>
<summary><b>state_transition-051</b> No Eth1Data copy per eth1 vote loop iteration — <i>n/a · low · cpu, memory</i></summary>

**Idea.** When counting eth1 data majority support, compare votes by reference or copy the Eth1Data once before the loop, instead of deep-copying it on every iteration.

**Impact.** Rust compares by reference; no per-iteration copy exists.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing.rs:373`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing.rs#L373) comparison is by reference (*vote == eth1_data), clone only on the majority branch

**Sources.** [prysm#16122](https://github.com/OffchainLabs/prysm/pull/16122), [prysm#16118](https://github.com/OffchainLabs/prysm/pull/16118)

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

**Sources.** [nimbus#3115](https://github.com/status-im/nimbus-eth2/pull/3115), [lodestar#3729](https://github.com/ChainSafe/lodestar/pull/3729), [lodestar#2514](https://github.com/ChainSafe/lodestar/pull/2514)

</details>


<a id="state_transition-053"></a>
<details>
<summary><b>state_transition-053</b> Indices-only sync committee getter — <i>n/a · low · cpu</i></summary>

**Idea.** When only sync committee validator indices are needed (e.g. monitoring at import), fetch them with an indices-only getter instead of building the full sync committee map.

**Impact.** Lighthouse never builds a full sync committee map at import; the monitor does a slice scan per monitored validator once per epoch.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_monitor.rs:984`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_monitor.rs#L984) uses sync_committee.contains(pubkey) on the epoch summary
- [`consensus/types/src/sync_committee/sync_committee.rs:92`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/sync_committee/sync_committee.rs#L92) contains is a linear scan of pubkeys, no map built

**Sources.** [lodestar#10350](https://github.com/ChainSafe/lodestar/pull/10350)

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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [lodestar#4792](https://github.com/ChainSafe/lodestar/pull/4792)

</details>


<a id="state_transition-055"></a>
<details>
<summary><b>state_transition-055</b> Bound the withdrawals sweep — <i>implemented · low · S · cpu</i></summary>

**Idea.** Cap the validators scanned per block in the withdrawals sweep at min(validator count, MAX_VALIDATORS_PER_WITHDRAWALS_SWEEP), so process_withdrawals has a fixed worst-case cost and small states do not loop past the registry.

**Impact.** Sweep already bounded.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/withdrawals.rs:258`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/withdrawals.rs#L258) validators_limit = min(validators.len(), max_validators_per_withdrawals_sweep)

**Skeptic check.** Verified the sweep limit is min(registry len, MAX_VALIDATORS_PER_WITHDRAWALS_SWEEP). Earlier verdict correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#4916](https://github.com/ChainSafe/lodestar/pull/4916), [teku#6593](https://github.com/Consensys-Incorporated/teku/pull/6593), [prysm#16231](https://github.com/OffchainLabs/prysm/pull/16231), [prysm#11760](https://github.com/OffchainLabs/prysm/pull/11760)

</details>


<a id="state_transition-056"></a>
<details>
<summary><b>state_transition-056</b> Cached length for copy-on-write slice append — <i>n/a · low · cpu</i></summary>

**Idea.** In a copy-on-write multi-value list, append using the cached length to find the next position instead of scanning prior appended positions, removing quadratic cost when adding many validators.

**Impact.** Prysm's copy-on-write multi-value slice does not exist in Lighthouse; milhouse appends via tree with cached length.

**Best measured result.** None (pr:prysm#17591)

**Evidence (Lighthouse @ 928b61e719).**

- milhouse List::push (milhouse list.rs:168) is a persistent tree push, no multi-value slice

**Sources.** [prysm#17591](https://github.com/OffchainLabs/prysm/pull/17591)

</details>


<a id="state_transition-057"></a>
<details>
<summary><b>state_transition-057</b> Flat validator array beside tree state — <i>implemented · medium · S · cpu, memory</i></summary>

**Idea.** Keep a flat, structurally shared array (or persistent vector) of validator records or their hot fields beside the tree-backed state, and iterate it in epoch processing, exits, activations and effective-balance collection instead of reading validators through the SSZ tree. Per-block clones stay cheap.

**Impact.** Same effect: native-record persistent vector with cheap clones and linear iteration; residual is O(log n) indexed reads.

**Best measured result.** None (pr:lodestar#1816)

**Evidence (Lighthouse @ 928b61e719).**

- d67aabd/src/leaf.rs:14 leaves hold native Arc&lt;T&gt;
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:243`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L243) validators.iter_cow() linear epoch iteration
- [`consensus/types/src/state/epoch_cache.rs:33`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/epoch_cache.rs#L33) flat effective balances
- [`consensus/types/src/state/beacon_state.rs:825`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L825) committee caches

**Second check.** Read milhouse (git rev d67aabd from Cargo.lock): leaves store Arc&lt;Validator&gt; natively, which is the equivalent of Lodestar's flat persistent validator array merged with the hash tree. Verdict rests on mechanism equivalence, hence low confidence.

**Skeptic check.** Different mechanism (milhouse persistent tree of native Validator structs instead of a separate flat array) but it removes the deserialization cost Lodestar's change targeted; single-pass epoch processing iterates with iter_cow. Upheld with low confidence because indexed reads stay O(log n).

**Verdict history.** partial (checked) → implemented (refuted) → implemented (skeptic)

**Sources.** [lodestar#1816](https://github.com/ChainSafe/lodestar/pull/1816), [lodestar@7b11d2ba1](https://github.com/ChainSafe/lodestar/commit/7b11d2ba14b4), [lodestar#2360](https://github.com/ChainSafe/lodestar/pull/2360), [lodestar@fa8136795](https://github.com/ChainSafe/lodestar/commit/fa81367957eb), [lodestar#3065](https://github.com/ChainSafe/lodestar/pull/3065), [lodestar@a15c47e35](https://github.com/ChainSafe/lodestar/commit/a15c47e355d8)

</details>


<a id="state_transition-058"></a>
<details>
<summary><b>state_transition-058</b> Flat arrays with page-table reads — <i>n/a · low · cpu</i></summary>

**Idea.** Write balances and participation as flat arrays in the working state and read through a page-table structure, avoiding tree traversal on each access.

**Impact.** Silver-specific working-state design; Lighthouse uses milhouse trees with its own CoW and update caches.

**Evidence (Lighthouse @ 928b61e719).**

- milhouse persistent trees hold balances and participation in beacon_state

**Sources.** [silver#143](https://github.com/gattaca-com/silver/pull/143)

</details>


<a id="state_transition-059"></a>
<details>
<summary><b>state_transition-059</b> Cheap zero check for sync committee — <i>n/a · low · cpu</i></summary>

**Idea.** Check whether a sync committee is default by testing a few fields (first pubkey, aggregate pubkey) instead of comparing against a multi-MB static zero value.

**Impact.** Lighthouse never compares sync committees to a default value, so there is nothing to speed up.

**Best measured result.** None (pr:nimbus#8779)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/sync_committee/sync_committee.rs:44`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/sync_committee/sync_committee.rs#L44) temporary() only used at upgrade/altair.rs:60 and tests; no comparison against a zero committee found

**Sources.** [nimbus#8779](https://github.com/status-im/nimbus-eth2/pull/8779), [prysm#10024](https://github.com/OffchainLabs/prysm/pull/10024), [prysm#10026](https://github.com/OffchainLabs/prysm/pull/10026)

</details>


<a id="state_transition-060"></a>
<details>
<summary><b>state_transition-060</b> Chunk-granular state delta edits — <i>n/a · low · cpu, memory</i></summary>

**Idea.** Record state deltas at 32-byte chunk granularity instead of per value, giving fewer edit entries and fewer hash leaf updates.

**Impact.** Milhouse already stores and hashes packed values at chunk granularity, and has no delta log.

**Evidence (Lighthouse @ 928b61e719).**

- milhouse packed_leaf.rs packs values into 32-byte chunks already (PackedLeaf::tree_hash)

**Sources.** [silver#131](https://github.com/gattaca-com/silver/pull/131)

</details>


<a id="state_transition-061"></a>
<details>
<summary><b>state_transition-061</b> Columnar state with delta overlays — <i>n/a · medium · cpu, memory</i></summary>

**Idea.** Store state in flat columnar form over a shared finalized base and apply each block as a thin delta overlay, rehashing only changed paths.

**Gap in Lighthouse.** Lighthouse's tree-states design already shares a persistent tree across states and rehashes only dirty paths, so a separate columnar plus delta overlay layer is a different architecture, not a missing optimisation.

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.lock milhouse 0.9.0: persistent tree with structural sharing, incremental rehash of changed paths ([`consensus/types`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types) BeaconState uses List/Vector from milhouse)

**Sources.** [silver#59](https://github.com/gattaca-com/silver/pull/59), [silver#98](https://github.com/gattaca-com/silver/pull/98)

</details>


<a id="state_transition-062"></a>
<details>
<summary><b>state_transition-062</b> In-place rebase of deltas on finalization — <i>n/a · low · cpu, memory</i></summary>

**Idea.** On finalization, rebase and prune state deltas into a preallocated target in place and skip rebuilding hash subtrees the winning branch did not change.

**Impact.** There are no state deltas in Lighthouse; states are full milhouse trees with shared subtrees.

**Evidence (Lighthouse @ 928b61e719).**

- milhouse is a persistent structural-sharing tree; no delta layers to rebase

**Sources.** [silver#111](https://github.com/gattaca-com/silver/pull/111)

</details>


<a id="state_transition-063"></a>
<details>
<summary><b>state_transition-063</b> Collect signature sets for later batch verify — <i>implemented · low · S · cpu</i></summary>

**Idea.** Add a state-transition mode that skips signature verification and returns all signature sets (block, randao, attestations, deposits) for one later batch verification.

**Impact.** Already batched on gossip, RPC and sync paths.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/block_signature_verifier.rs:137-148`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/block_signature_verifier.rs#L137-L148) verify_entire_block collects all sets then verifies once
- [`consensus/state_processing/src/per_block_processing.rs:71`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing.rs#L71),77,147,164 VerifyBulk and NoVerification strategies
- [`beacon_node/beacon_chain/src/block_verification.rs:718-724`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L718-L724) chain segment sets verified in one batch
- [`beacon_node/beacon_chain/src/block_verification.rs:1207-1214`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1207-L1214),1279-1287 gossip/RPC block signatures batched
- [`beacon_node/beacon_chain/src/block_verification.rs:1710`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1710) state transition run with NoVerification after batch

**Skeptic check.** Verified BlockSignatureVerifier collects block, randao, proposer slashing, attestation and exit sets and verifies once, then per_block_processing runs with NoVerification; deposits are excluded per spec. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#6482](https://github.com/OffchainLabs/prysm/pull/6482)

</details>


<a id="state_transition-064"></a>
<details>
<summary><b>state_transition-064</b> Verify block operation signatures in parallel — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Verify independent signatures of block operations and genesis deposits (each slashable attestation in attester slashings, attestations, deposits, exits) in parallel across cores, then apply the state mutations serially without re-verifying. Signature checks are independent, so this scales with core count.

**Impact.** Already parallel across cores.

**Best measured result.** Provides a large speed improvement (commit:lighthouse@7108d057fb8b)

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/impls/blst.rs:113`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L113) verify_signature_sets calls blst verify_multiple_aggregate_signatures
- ~/.cargo/registry/src/*/blst-0.3.17/src/lib.rs:1337 mt::da_pool() multi-threaded pairing
- [`consensus/state_processing/src/per_block_processing/verify_deposit.rs:109`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/verify_deposit.rs#L109) deposits decompressed par_iter and verified in par_chunks
- [`consensus/state_processing/src/per_block_processing/block_signature_verifier.rs:439`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/block_signature_verifier.rs#L439) all block op signatures batched

**Skeptic check.** BlockSignatureVerifier batches all op signatures into one blst multi-aggregate verify that uses blst's thread pool; deposits verified with rayon; mutations then run with VerifySignatures::False. Earlier verdict correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@3f9884936](https://github.com/sigp/lighthouse/commit/3f988493622a), [lighthouse@7108d057f](https://github.com/sigp/lighthouse/commit/7108d057fb8b), [lighthouse@e7fba3a47](https://github.com/sigp/lighthouse/commit/e7fba3a47358), [lighthouse@1ca99b8c4](https://github.com/sigp/lighthouse/commit/1ca99b8c4c7d), [lighthouse#264](https://github.com/sigp/lighthouse/pull/264)

</details>


<a id="state_transition-065"></a>
<details>
<summary><b>state_transition-065</b> Compute all committees of a slot at once — <i>implemented · low · S · cpu</i></summary>

**Idea.** Compute all beacon committees of a slot or epoch in one call, computing the active validator set and committee count once, instead of per-committee helpers that recompute shared inputs in loops.

**Impact.** Active set and committee count computed once per epoch.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/committee_cache.rs:233`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L233) get_beacon_committees_at_slot from cached shuffling
- [`consensus/types/src/state/beacon_state.rs:1252`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1252) get_beacon_committees_at_epoch

**Skeptic check.** get_beacon_committees_at_slot slices one cached shuffling with cached committees_per_slot; no per-committee recomputation. Earlier verdict correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#14282](https://github.com/OffchainLabs/prysm/pull/14282), [prysm#14284](https://github.com/OffchainLabs/prysm/pull/14284), [prysm#14286](https://github.com/OffchainLabs/prysm/pull/14286)

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


<a id="state_transition-067"></a>
<details>
<summary><b>state_transition-067</b> Genesis validators root as constant — <i>implemented · low · S · cpu</i></summary>

**Idea.** Read the genesis validators root from a constant in chain config instead of from the state, avoiding state access and locks on hot paths.

**Impact.** None left: the root is a plain Hash256 on BeaconChain, set once at build time; no beacon_node path outside the builder reads it from a head state under a lock.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:492`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L492)
- [`beacon_node/beacon_chain/src/builder.rs:921`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L921)
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1361`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1361)

**Skeptic check.** A grep for .genesis_validators_root() under beacon_node finds only the builder (startup). Hot paths use chain.genesis_validators_root. The earlier evidence is right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#14365](https://github.com/OffchainLabs/prysm/pull/14365), [prysm#14392](https://github.com/OffchainLabs/prysm/pull/14392)

</details>


<a id="state_transition-068"></a>
<details>
<summary><b>state_transition-068</b> Copy committee out of shuffled list — <i>n/a · low · memory</i></summary>

**Idea.** Return each cached committee as its own right-sized copy instead of a subslice of the big shuffled list, so the multi-MB backing array can be freed.

**Impact.** Committees are borrowed slices of one Arc-shared CommitteeCache; no GC backing-array retention problem in Rust, the cache is freed as a whole.

**Best measured result.** None (pr:prysm#17606)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/committee_cache.rs:29`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L29) shuffling Vec&lt;usize&gt;
- [`consensus/types/src/state/committee_cache.rs:370`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L370) compute_committee returns a slice into it

**Sources.** [prysm#17606](https://github.com/OffchainLabs/prysm/pull/17606)

</details>


<a id="state_transition-069"></a>
<details>
<summary><b>state_transition-069</b> Copy field tries for late blocks — <i>n/a · low · cpu, latency</i></summary>

**Idea.** For late blocks, copy the state's field tries instead of recomputing tries for older states, so the next-slot cache stays usable.

**Impact.** Lighthouse uses milhouse persistent trees with structural sharing and a per-tree hash cache; cloning is O(1) and there are no per-state field tries to recompute.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs) milhouse persistent lists (structural sharing)

**Sources.** [prysm#12461](https://github.com/OffchainLabs/prysm/pull/12461)

</details>


<a id="state_transition-070"></a>
<details>
<summary><b>state_transition-070</b> Hand-written copy for small state objects — <i>n/a · low · cpu</i></summary>

**Idea.** Replace reflection-based generic clones of pending attestations and checkpoints with hand-written field-wise copy functions.

**Impact.** Rust derives field-wise Clone at compile time; no reflection.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/attestation`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/attestation)/ derived Clone on Checkpoint/PendingAttestation

**Sources.** [prysm#4711](https://github.com/OffchainLabs/prysm/pull/4711)

</details>


<a id="state_transition-071"></a>
<details>
<summary><b>state_transition-071</b> Honor deadlines in multi-slot advance — <i>n/a · low · cpu</i></summary>

**Idea.** Check context deadlines during multi-slot state advancement so abandoned requests stop computing.

**Impact.** State advance is synchronous Rust running in a spawned blocking task; there is no context deadline concept and requests rarely span many slots.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_slot_processing.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_slot_processing.rs) plain synchronous loop

**Sources.** [prysm#2961](https://github.com/OffchainLabs/prysm/pull/2961)

</details>


<a id="state_transition-072"></a>
<details>
<summary><b>state_transition-072</b> Invalidate participation hash once per block — <i>n/a · low · S · cpu</i></summary>

**Idea.** In block attestation processing, apply participation flag updates and invalidate or rehash the participation list once for the whole block (or operation), not per attestation.

**Gap in Lighthouse.** Only micro-gain: hoist get_epoch_participation_mut out of the inner flag loop in process_attestation (both variants).

**Impact.** Milhouse tracks dirtiness per leaf path and hashes lazily at tree_hash_root, so there is no list-wide hash invalidation per attestation to batch; hoisting the accessor would save a few lookups per validator, negligible.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/process_operations.rs:266`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L266) get_epoch_participation_mut per flag per validator
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:407`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L407) same on the altair-electra path

**Sources.** [silver#364](https://github.com/gattaca-com/silver/pull/364), [nimbus#3063](https://github.com/status-im/nimbus-eth2/pull/3063)

</details>


<a id="state_transition-073"></a>
<details>
<summary><b>state_transition-073</b> Cheaper dirty-index tracking in hash tree — <i>n/a · low · cpu</i></summary>

**Idea.** Micro-optimize dirty-index tracking in the incremental state hash tree, with cheaper insertion and no redundant setters.

**Impact.** Dirty tracking is inside milhouse's persistent tree (copy-on-write nodes with cached hashes), not an index set owned by Lighthouse.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs) milhouse List/Vector

**Sources.** [prysm#9338](https://github.com/OffchainLabs/prysm/pull/9338)

</details>


<a id="state_transition-074"></a>
<details>
<summary><b>state_transition-074</b> Early block operation length checks — <i>implemented · low · S · cpu</i></summary>

**Idea.** Check block operation list lengths against limits before any processing, so invalid blocks fail before expensive work.

**Impact.** Oversize operation lists are rejected at SSZ decode (VariableList max length), before gossip verification or state work. verify_operation_list_lengths covers lists built without decoding.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/process_operations.rs:22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L22)
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:92`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L92)
- [`consensus/state_processing/src/per_block_processing.rs:436`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing.rs#L436)

**Skeptic check.** Confirmed that the bounded SSZ types reject oversize lists at decode, and that the explicit Gloas check runs first in process_operations. The earlier evidence is right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#2900](https://github.com/OffchainLabs/prysm/pull/2900)

</details>


<a id="state_transition-075"></a>
<details>
<summary><b>state_transition-075</b> Reject wrong-fork blocks early — <i>implemented · low · S · cpu</i></summary>

**Idea.** Reject blocks of the wrong fork before entering fork-specific state transition code.

**Impact.** Wrong-fork blocks fail with InconsistentBlockFork/InconsistentStateFork at entry; the source gain was C code size, not runtime.

**Best measured result.** None (pr:nimbus#3444)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing.rs:126-133`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing.rs#L126-L133) signed_block.fork_name and state.fork_name checked before any fork-specific processing
- [`consensus/state_processing/src/per_slot_processing.rs:44-46`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_slot_processing.rs#L44-L46) state fork check before slot/epoch processing

**Skeptic check.** Verified both checks run first in per_block_processing and per_slot_processing. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#3444](https://github.com/status-im/nimbus-eth2/pull/3444)

</details>


<a id="state_transition-076"></a>
<details>
<summary><b>state_transition-076</b> Early-exit pending withdrawal existence check — <i>not · low · S · cpu</i></summary>

**Idea.** When a check only needs to know whether a validator has any pending partial withdrawal or pending balance, return on the first match instead of summing the whole pending list.

**Gap in Lighthouse.** Add has_pending_balance_to_withdraw(validator_index) using any() and use it in verify_exit.rs, the full-exit branch (process_operations.rs:843) and the consolidation check (:1171).

**Impact.** Exit verification and consolidation requests stop scanning the full pending list on the common no-match path; the list is normally short so the gain is tiny.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:3232`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3232) get_pending_balance_to_withdraw sums whole list
- [`consensus/state_processing/src/per_block_processing/verify_exit.rs:84`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/verify_exit.rs#L84) only tests ==0
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:1171`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L1171) only tests &gt;0

**Sources.** [prysm#14200](https://github.com/OffchainLabs/prysm/pull/14200), [prysm#16189](https://github.com/OffchainLabs/prysm/pull/16189)

</details>


<a id="state_transition-077"></a>
<details>
<summary><b>state_transition-077</b> Cheaper payload timeliness committee computation — <i>partial · low · S · cpu</i></summary>

**Idea.** Compute the payload timeliness committee with a cheaper selection that reuses per-epoch data already computed, instead of a slower per-slot computation.

**Gap in Lighthouse.** Only the per-slot lookup is cached (ptc_window); the selection itself is not optimized. In compute_ptc_with_cache, each slot collects all committee members into a new Vec. Then compute_balance_weighted_selection calls compute_balance_weighted_acceptance once per candidate. Each call runs shuffling_random_u16_electra, which does a fresh SHA256 of seed\|\|i/16 (one digest gives 16 values, so this is 16x redundant), and get_effective_balance, a milhouse tree read. Acceptance is about EB/2048 ETH, so a 512-member PTC takes tens of thousands of iterations per slot, times 32 slots each epoch (also in upgrade_to_gloas). Fix: cache the digest per block of 16 iterations, and read effective balances from the epoch cache. The TODO at beacon_state.rs:3752 says so.

**Impact.** Roughly 16x fewer SHA256 calls, and no tree reads, in process_ptc_window. This is likely tens of ms per epoch transition after Gloas. Lodestar measured about 4x faster PTC computation. The same helpers also serve proposer and sync-committee selection.

**Best measured result.** None (pr:lodestar#8881)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:539`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L539)
- [`consensus/types/src/state/beacon_state.rs:3591`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3591)
- [`consensus/types/src/state/beacon_state.rs:3639`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3639)
- [`consensus/types/src/state/beacon_state.rs:3704`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3704)
- [`consensus/types/src/state/beacon_state.rs:3745`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3745)
- [`consensus/types/src/state/beacon_state.rs:1503`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1503)

**Skeptic check.** The earlier evidence is right that the PTC is computed once per epoch and get_ptc is a lookup. It missed that the lodestar PR made the computation itself cheaper, and Lighthouse's compute_balance_weighted_selection still hashes once per candidate and reads balances from the tree.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lodestar#8881](https://github.com/ChainSafe/lodestar/pull/8881)

</details>


<a id="state_transition-078"></a>
<details>
<summary><b>state_transition-078</b> Scale genesis building to large deposit sets — <i>n/a · low · cpu, startup</i></summary>

**Idea.** Make genesis state building scale to about 100K validators; the mechanism is not recorded, so check the original change.

**Impact.** Mainnet nodes load a prebuilt genesis state; genesis building only runs in tests and devnets.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/genesis.rs:18`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/genesis.rs#L18) initialize_beacon_state_from_eth1
- [`beacon_node/client/src/builder.rs:993`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L993) genesis state loaded from bundled SSZ

**Sources.** [nimbus#2020](https://github.com/status-im/nimbus-eth2/pull/2020)

</details>


<a id="state_transition-079"></a>
<details>
<summary><b>state_transition-079</b> Genesis constructor without deposits — <i>not · low · M · startup, cpu</i></summary>

**Idea.** Provide a genesis-state constructor that inserts validators directly, with no deposit proofs or proof-of-possession checks, for tests and tooling.

**Gap in Lighthouse.** Add a genesis constructor that inserts validators directly without deposit tree proofs or signature checks, used by InteropGenesisBuilder and test_utils.

**Impact.** Only test and devnet startup get faster; no mainnet effect.

**Best measured result.** None (commit:lighthouse@f82c4268e29a)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/genesis/src/interop.rs:85`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/genesis/src/interop.rs#L85) build_genesis_state signs deposits and calls initialize_beacon_state_from_eth1
- [`consensus/state_processing/src/genesis.rs:42`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/genesis.rs#L42) apply_deposit with proofs and signature check

**Sources.** [lighthouse@f82c4268e](https://github.com/sigp/lighthouse/commit/f82c4268e29a)

</details>


<a id="state_transition-080"></a>
<details>
<summary><b>state_transition-080</b> Build genesis incrementally as deposits arrive — <i>n/a · low · cpu, startup</i></summary>

**Idea.** Build the candidate genesis state incrementally as eth1 deposit logs arrive (and count activated validators while adding them), instead of rebuilding from all deposits for every candidate block.

**Impact.** Lighthouse no longer has an eth1 genesis watcher; genesis comes from a bundled or downloaded state.

**Best measured result.** None (pr:teku#1126)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/genesis.rs:18`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/genesis.rs#L18) builds genesis in one batch from deposits
- [`beacon_node/client/src/builder.rs:993`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L993) no eth1 genesis service remains

**Sources.** [teku#1630](https://github.com/Consensys-Incorporated/teku/pull/1630), [lodestar#1042](https://github.com/ChainSafe/lodestar/pull/1042), [teku#1126](https://github.com/Consensys-Incorporated/teku/pull/1126)

</details>


<a id="state_transition-081"></a>
<details>
<summary><b>state_transition-081</b> Remove slow paths in large simulations — <i>implemented · low · S · cpu</i></summary>

**Idea.** Remove slow committee and attestation handling paths in slot processing that made 50k-validator block simulations intractable.

**Impact.** Committee cache, epoch cache and single-pass epoch processing keep mainnet-size (1M+) validator sets tractable; no 2020-era slow committee/attestation path remains.

**Best measured result.** None (pr:nimbus#1287)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/committee_cache.rs:233`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L233) cached committee lookup
- [`consensus/state_processing/src/epoch_cache.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/epoch_cache.rs) per-epoch precompute
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs) single-pass epoch processing

**Skeptic check.** Nimbus #1287 removed naive per-slot committee recomputation; Lighthouse computes committees once per epoch in CommitteeCache. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#1287](https://github.com/status-im/nimbus-eth2/pull/1287)

</details>


<a id="state_transition-082"></a>
<details>
<summary><b>state_transition-082</b> Correct fixed-length vector initialization — <i>n/a · low · memory</i></summary>

**Idea.** Initialize large fixed-length state vectors once at their length with shared default elements, not with wrongly sized or per-element allocations.

**Impact.** Java vector allocation bug; milhouse tree-backed vectors do not allocate per element.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:811`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L811) states use milhouse Vector/List with structural sharing

**Sources.** [teku#789](https://github.com/Consensys-Incorporated/teku/pull/789)

</details>


<a id="state_transition-083"></a>
<details>
<summary><b>state_transition-083</b> Fixed-size arrays for root vectors — <i>n/a · low · memory, cpu</i></summary>

**Idea.** Store block_roots, state_roots, historical_roots and randao_mixes as fixed-size 32-byte arrays rather than lists of byte slices, avoiding per-root heap allocations.

**Impact.** Roots are already fixed-size Hash256 values in milhouse, not slices.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:811`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L811) milhouse Vector&lt;Hash256&gt; roots (32-byte fixed values)

**Sources.** [prysm#9845](https://github.com/OffchainLabs/prysm/pull/9845), [prysm#9861](https://github.com/OffchainLabs/prysm/pull/9861), [prysm#9862](https://github.com/OffchainLabs/prysm/pull/9862), [prysm#9835](https://github.com/OffchainLabs/prysm/pull/9835)

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


<a id="state_transition-085"></a>
<details>
<summary><b>state_transition-085</b> Hoist epoch and lock out of validator loop — <i>n/a · low · cpu</i></summary>

**Idea.** Compute the current epoch once before looping over validators for total active balance, instead of per validator with a state read lock each time.

**Impact.** No locks in the validator loop and the total is cached per state.

**Best measured result.** None (pr:prysm#9178)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:2652`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2652) compute_total_active_balance_slow computes epoch once
- [`consensus/types/src/state/beacon_state.rs:819`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L819) total_active_balance cached

**Sources.** [prysm#9178](https://github.com/OffchainLabs/prysm/pull/9178)

</details>


<a id="state_transition-086"></a>
<details>
<summary><b>state_transition-086</b> Inclusion slot map for rewards — <i>implemented · low · S · cpu</i></summary>

**Idea.** During attestation processing, record a map of attester to inclusion slot and use it for inclusion-delay rewards instead of nested loops.

**Impact.** Phase0 only. Inclusion delay and proposer are stored in a per-validator status vector in one pass over the attestations.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/base/validator_statuses.rs:279`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/base/validator_statuses.rs#L279)
- [`consensus/state_processing/src/per_epoch_processing/base/validator_statuses.rs:294`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/base/validator_statuses.rs#L294)

**Skeptic check.** Confirmed that InclusionInfo goes into the indexed statuses Vec for each attester; there are no nested loops. The earlier evidence is right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#2344](https://github.com/OffchainLabs/prysm/pull/2344)

</details>


<a id="state_transition-087"></a>
<details>
<summary><b>state_transition-087</b> Lightweight asserts in hot paths — <i>n/a · low · S · cpu</i></summary>

**Idea.** Replace generic or heavy assert helpers in hot state-transition code with direct inline condition checks.

**Impact.** Rust has no heavy assert helper; checks are inline conditions.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/verify_attestation.rs:28`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/verify_attestation.rs#L28) plain inline checks with Result

**Sources.** [lodestar#3019](https://github.com/ChainSafe/lodestar/pull/3019), [lodestar@531943db3](https://github.com/ChainSafe/lodestar/commit/531943db3539)

</details>


<a id="state_transition-088"></a>
<details>
<summary><b>state_transition-088</b> Lazy pubkey parsing and clean reads — <i>partial · low · L · cpu</i></summary>

**Idea.** Keep validator pubkeys and signatures as raw bytes and parse curve points lazily, compare pubkeys by bytes, and do not mark the hash cache dirty on read-only list access.

**Gap in Lighthouse.** Pubkey side is done, but signatures are not kept as raw bytes: GenericSignature::deserialize / GenericAggregateSignature::deserialize decompress every block, attestation, sync-aggregate, RANDAO and exit signature at SSZ decode. HotColdDB::get_blinded_block -&gt; load_blocks_to_replay -&gt; BlockReplayer (NoVerification) pays G2 decompression for signatures it never checks. A lazy (bytes-first) signature type in SignedBeaconBlock/Attestation would remove that work on replay, reconstruction and API block reads.

**Impact.** About 10-15 G2 decompressions per post-Electra block (tens of microseconds each), so roughly 0.5-1 ms per replayed block; matters for long state-regen replays and historic reconstruction, not for gossip import, where the points are needed anyway.

**Best measured result.** None (pr:nimbus#2259)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/validator/validator.rs:22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/validator/validator.rs#L22) state pubkeys are PublicKeyBytes
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:24-29`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L24-L29) keys decompressed once, indexed by PublicKeyBytes
- [`consensus/types/src/block/signed_beacon_block.rs:121`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/block/signed_beacon_block.rs#L121) block signature is Signature, not SignatureBytes
- [`consensus/types/src/attestation/attestation.rs:90`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/attestation/attestation.rs#L90) attestation signature is AggregateSignature
- [`crypto/bls/src/generic_signature.rs:145-156`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/generic_signature.rs#L145-L156) deserialize decompresses the G2 point eagerly (blst Signature::from_bytes -&gt; uncompress)
- [`crypto/bls/src/generic_aggregate_signature.rs:166-177`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/generic_aggregate_signature.rs#L166-L177) same for aggregates
- [`beacon_node/store/src/hot_cold_store.rs:663-668`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L663-L668) get_blinded_block SSZ-decodes the full block, used by load_blocks_to_replay (2502)
- [`beacon_node/store/src/hot_cold_store.rs:2566`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2566) replay then runs with no_signature_verification

**Skeptic check.** Confirmed state pubkeys are bytes and milhouse reads do not dirty hashes. The earlier verdict missed the 'signatures as raw bytes, parsed lazily' half of the idea: Lighthouse decompresses signatures eagerly on decode, including on the no-verify replay path.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [nimbus#2259](https://github.com/status-im/nimbus-eth2/pull/2259)

</details>


<a id="state_transition-089"></a>
<details>
<summary><b>state_transition-089</b> Linear scan for state diff on load — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** When diffing validator and inactivity-score buffers against a seed state, first compare whole buffers, then do one linear scan over fixed-size elements instead of recursive binary partitioning.

**Impact.** Lighthouse never had the recursive binary partition; hdiff compute and apply are already linear scans over fixed-size elements.

**Best measured result.** None (commit:lodestar@ddaca79cddee)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hdiff.rs:438-470`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L438-L470) ValidatorsDiff::compute single linear pass with per-element y == x skip
- [`beacon_node/store/src/hdiff.rs:384-404`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L384-L404) CompressedU64Diff::compute linear for balances and inactivity_scores
- [`beacon_node/store/src/hdiff.rs:406-430`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L406-L430) CompressedU64Diff::apply linear on load

**Skeptic check.** Verified compute and apply are linear with no recursion. Lodestar's separate design (load a state onto a seed state to share tree nodes) is a different idea and is not assessed here; the earlier evidence was correct for the mechanism described.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@ddaca79cd](https://github.com/ChainSafe/lodestar/commit/ddaca79cddee)

</details>


<a id="state_transition-090"></a>
<details>
<summary><b>state_transition-090</b> Bulk-build persistent validators list — <i>implemented · low · S · cpu</i></summary>

**Idea.** Build the persistent validators list from an array in one pass rather than appending items one by one.

**Impact.** List::try_from_iter builds the tree bottom-up with Builder in one pass. SSZ decode of fixed-length items, such as the validators list in state loads, uses it.

**Evidence (Lighthouse @ 928b61e719).**

- d67aabd/src/list.rs:88
- d67aabd/src/list.rs:502
- [`beacon_node/store/src/hdiff.rs:230`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L230)

**Skeptic check.** Checked the milhouse revision in Cargo.lock (d67aabd; the earlier evidence cited c70f128, but the code is the same). The slow push loop exists only as try_from_iter_slow for tests.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#2028](https://github.com/ChainSafe/lodestar/pull/2028)

</details>


<a id="state_transition-091"></a>
<details>
<summary><b>state_transition-091</b> Bound empty-slot fill before allocation — <i>n/a · low · memory</i></summary>

**Idea.** Reject blocks whose slot gap would exceed the historical list limit before filling empty-slot entries, so a large slot cannot trigger unbounded allocation.

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

**Impact.** BeaconState is an owned lock-free milhouse tree, so there is no per-index lock to amortise.

**Best measured result.** 16-29% faster at 2.3M validators, allocations unchanged (pr:prysm#17480)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:24`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L24) plain Vec/HashMap, no per-index lock

**Sources.** [prysm#17480](https://github.com/OffchainLabs/prysm/pull/17480), [prysm#16310](https://github.com/OffchainLabs/prysm/pull/16310)

</details>


<a id="state_transition-093"></a>
<details>
<summary><b>state_transition-093</b> Simpler Merkle branch verification loop — <i>implemented · low · S · cpu</i></summary>

**Idea.** Verify Merkle branches (deposit proofs) with a tight, simple loop over the branch nodes instead of a more general construction. Less per-level overhead per proof.

**Impact.** Already a minimal per-level loop; deposit proofs are a cold path after Fulu removed the Eth1 bridge.

**Best measured result.** about 3% faster (pr:teku#5206)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/merkle_proof/src/lib.rs:382-397`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/merkle_proof/src/lib.rs#L382-L397) merkle_root_from_branch is a tight loop of hash32_concat per level
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:687-699`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L687-L699) deposit proofs verified in parallel with par_iter

**Skeptic check.** Read the loop; it matches the Teku simplification. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#5206](https://github.com/Consensys-Incorporated/teku/pull/5206)

</details>


<a id="state_transition-094"></a>
<details>
<summary><b>state_transition-094</b> Swap-or-not shuffle and sampling in native code — <i>n/a · low · S · cpu</i></summary>

**Idea.** Run the swap-or-not shuffle and the committee, proposer, sync committee and PTC sampling built on it in compiled native code rather than in a managed runtime. Native code makes the per-epoch shuffle and per-slot sampling tens of times faster.

**Impact.** Lighthouse is already native; shuffle is whole-list and hash-batched.

**Best measured result.** Epoch: TS 37.3 ms/op vs Rust 0.90 ms/op at 250k validators; slot 1.94 ms vs 0.32 ms (pr:lodestar#9225)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/swap_or_not_shuffle/src/shuffle_list.rs:92`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/swap_or_not_shuffle/src/shuffle_list.rs#L92) shuffle_list is native Rust

**Sources.** [lodestar#9225](https://github.com/ChainSafe/lodestar/pull/9225), [lodestar#9263](https://github.com/ChainSafe/lodestar/pull/9263), [lodestar#9829](https://github.com/ChainSafe/lodestar/pull/9829), [lodestar@99f06eab3](https://github.com/ChainSafe/lodestar/commit/99f06eab3bd5)

</details>


<a id="state_transition-095"></a>
<details>
<summary><b>state_transition-095</b> Native typed beacon state instead of protobuf wrapper — <i>n/a · low · S · memory, cpu</i></summary>

**Idea.** Hold the beacon state for every fork as native typed struct fields (fixed-size arrays for root vectors, plain slices for per-validator lists) rather than a serialization-framework object. Copy, hash and mutate then need no marshalling or per-element byte-slice allocations, and large lists can be shared copy-on-write.

**Impact.** State is already native typed fields with structural sharing.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:825`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L825) native typed struct with milhouse persistent lists

**Sources.** [prysm#9820](https://github.com/OffchainLabs/prysm/pull/9820), [prysm#9871](https://github.com/OffchainLabs/prysm/pull/9871), [prysm#9874](https://github.com/OffchainLabs/prysm/pull/9874), [prysm#10086](https://github.com/OffchainLabs/prysm/pull/10086), [prysm#10121](https://github.com/OffchainLabs/prysm/pull/10121), [prysm#10139](https://github.com/OffchainLabs/prysm/pull/10139), [prysm#9911](https://github.com/OffchainLabs/prysm/pull/9911), [prysm#9821](https://github.com/OffchainLabs/prysm/pull/9821)

</details>


<a id="state_transition-096"></a>
<details>
<summary><b>state_transition-096</b> Native state transition backend fed with serialized bytes — <i>n/a · low · S · cpu, memory</i></summary>

**Idea.** Run the whole state transition in a native backend behind a state-view interface and feed it the already-serialized block bytes from gossip/sync. This avoids re-encoding blocks and conversions between managed object trees and the native state.

**Impact.** No managed runtime boundary to cross in Lighthouse.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src)/ native Rust throughout

**Sources.** [lodestar#9516](https://github.com/ChainSafe/lodestar/pull/9516), [lodestar#9632](https://github.com/ChainSafe/lodestar/pull/9632), [lodestar#10345](https://github.com/ChainSafe/lodestar/pull/10345)

</details>


<a id="state_transition-097"></a>
<details>
<summary><b>state_transition-097</b> Next-epoch committee cache including registry update — <i>implemented · medium · S · cpu</i></summary>

**Idea.** Build and keep an extra committee cache for the next epoch (that already reflects the registry update), so next-epoch committee and duty lookups do not recompute the shuffling.

**Impact.** There is a Next-epoch committee cache. advance_caches rotates it to Current at the epoch boundary, so next-epoch duties need no reshuffle.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:825`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L825)
- [`consensus/types/src/state/beacon_state.rs:2768`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2768)
- [`consensus/types/src/state/beacon_state.rs:2887`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2887)

**Skeptic check.** This is the Lighthouse PR itself (lighthouse#308), and its mechanism is still present: build_all_committee_caches builds Previous, Current and Next, and advance_caches rotates them.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#308](https://github.com/sigp/lighthouse/pull/308)

</details>


<a id="state_transition-098"></a>
<details>
<summary><b>state_transition-098</b> Trusted no-verify path for replaying known blocks — <i>implemented · low · S · cpu, memory, latency</i></summary>

**Idea.** Give block processing a trusted mode for blocks already verified (replay, state regeneration, initial sync, locally built blocks) that skips BLS signature checks (proposer, RANDAO, attestations, deposits, exits) and the pubkey copying they need. Signature work dominates replay, so skipping it makes regeneration much faster.

**Impact.** BLS checks are skipped on replay, regen, reconstruction, post-verification import and local production; range sync must verify untrusted blocks and batches them instead.

**Best measured result.** Profile showed those two verifications as the biggest bottleneck (pr:prysm#4943)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/block_replayer.rs:113-115`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/block_replayer.rs#L113-L115) no_signature_verification sets BlockSignatureStrategy::NoVerification
- [`beacon_node/store/src/hot_cold_store.rs:2566`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2566) state regen replays without signatures
- [`beacon_node/store/src/reconstruct.rs:165`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/reconstruct.rs#L165) historic reconstruction uses NoVerification
- [`beacon_node/beacon_chain/src/block_verification.rs:1710`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1710) import after batch signature verification uses NoVerification
- [`beacon_node/beacon_chain/src/beacon_chain.rs:6530-6531`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6530-L6531) local block production uses VerifyRandao or NoVerification

**Skeptic check.** Verified every trusted path passes NoVerification. Signature decompression at decode still happens on replay; that is counted under state_transition-088, not here.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#3589](https://github.com/OffchainLabs/prysm/pull/3589), [prysm#4943](https://github.com/OffchainLabs/prysm/pull/4943), [nimbus#2266](https://github.com/status-im/nimbus-eth2/pull/2266), [nimbus#4435](https://github.com/status-im/nimbus-eth2/pull/4435), [lodestar@3b37d7abf](https://github.com/ChainSafe/lodestar/commit/3b37d7abfc32), [lodestar#536](https://github.com/ChainSafe/lodestar/pull/536), [grandine#920](https://github.com/grandinetech/grandine/pull/920), [prysm#1674](https://github.com/OffchainLabs/prysm/pull/1674)

</details>


<a id="state_transition-099"></a>
<details>
<summary><b>state_transition-099</b> Machine integers instead of bigints for balances — <i>n/a · low · S · cpu, memory</i></summary>

**Idea.** Store balances, effective balances, slots and epochs as machine integers (effective balance in increments) and avoid bigint conversions in epoch rewards, balance updates and request indices. Machine arithmetic avoids allocation and slow big-number math.

**Impact.** Rust already uses u64 for balances; no bigint.

**Best measured result.** Described as faster processing and memory savings; no numbers (pr:lodestar#2973)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/validator/validator.rs:25`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/validator/validator.rs#L25) effective_balance: u64

**Sources.** [lodestar#2973](https://github.com/ChainSafe/lodestar/pull/2973), [lodestar#7564](https://github.com/ChainSafe/lodestar/pull/7564), [lodestar#3044](https://github.com/ChainSafe/lodestar/pull/3044), [lodestar@a42a24fe3](https://github.com/ChainSafe/lodestar/commit/a42a24fe34cb), [lodestar@e90beae10](https://github.com/ChainSafe/lodestar/commit/e90beae1076a), [lodestar@eac14970f](https://github.com/ChainSafe/lodestar/commit/eac14970f039)

</details>


<a id="state_transition-100"></a>
<details>
<summary><b>state_transition-100</b> Run state transition in a worker thread — <i>n/a · low · S · cpu, latency</i></summary>

**Idea.** Offload state transitions to a dedicated worker thread, passing the serialized state without a buffer copy, with a FIFO queue that dedups identical jobs. The main thread stays free for networking and fork choice.

**Impact.** Lighthouse already runs state transitions on blocking/rayon threads, so the networking runtime is not blocked; no JS single-thread problem exists.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:3046`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3046) spawn_blocking_handle runs block import off the async runtime

**Sources.** [lodestar#1551](https://github.com/ChainSafe/lodestar/pull/1551)

</details>


<a id="state_transition-101"></a>
<details>
<summary><b>state_transition-101</b> Packed u32 arrays for shuffling and committees — <i>partial · low · M · memory</i></summary>

**Idea.** Store active indices and the shuffling as packed u32 arrays and make committees subarray views of the shuffling, rather than arrays of boxed numbers or separately allocated committee vectors. This packs memory tighter and shares it between shuffling and committees.

**Gap in Lighthouse.** Committees are already slices of the shuffling; only the element width is 8 bytes (usize) instead of 4. Change CommitteeCache.shuffling to Vec&lt;u32&gt; and adapt getters (shuffling(), compute_committee, shuffling_positions).

**Impact.** Halves committee cache memory (~1M validators: ~8MB to ~4MB per epoch cache, a few caches); negligible runtime gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/committee_cache.rs:29`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L29) shuffling: Vec&lt;usize&gt;
- [`consensus/types/src/state/committee_cache.rs:370`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L370) compute_committee returns &amp;[usize] slice of shuffling
- [`consensus/types/src/state/committee_cache.rs:31`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L31) shuffling_positions Vec&lt;NonZeroUsizeOption&gt;

**Sources.** [lodestar#6475](https://github.com/ChainSafe/lodestar/pull/6475)

</details>


<a id="state_transition-102"></a>
<details>
<summary><b>state_transition-102</b> Parallel per-validator epoch processing, no quadratic loops — <i>partial · low · L · cpu</i></summary>

**Idea.** Parallelize per-validator loops in epoch and block processing across cores and remove O(n^2) loops, so state transition scales with large validator sets.

**Gap in Lighthouse.** O(n^2) loops are gone (single pass with epoch/pubkey caches), but the epoch pass itself is single-threaded; one could chunk the validator loop with rayon in process_epoch_single_pass.

**Impact.** Epoch processing on mainnet is already a few hundred ms once per epoch; rayon might cut it a few-fold but it is off the block-critical path mostly (state advance timer precomputes it).

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:155`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L155) process_epoch_single_pass: one sequential pass over validators, no quadratic loops
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:689`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L689) par_iter only for deposits
- [`consensus/state_processing/src/per_block_processing/verify_deposit.rs:109`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/verify_deposit.rs#L109) par_iter

**Sources.** [lighthouse#291](https://github.com/sigp/lighthouse/pull/291)

</details>


<a id="state_transition-103"></a>
<details>
<summary><b>state_transition-103</b> Parallel swap-or-not shuffle across threads — <i>not · low · M · cpu, memory, latency</i></summary>

**Idea.** Split the swap-or-not shuffle of a large index list into chunks processed on separate threads in each round, so the full-registry shuffle at epoch boundaries uses all cores.

**Gap in Lighthouse.** Split each round's swap pass in shuffle_list into chunks run on rayon; needs care since swaps pair i and flip(i).

**Impact.** Shuffle of ~1M validators takes tens of ms once per epoch and is already precomputed in the state advance timer; marginal gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/swap_or_not_shuffle/src/shuffle_list.rs:1`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/swap_or_not_shuffle/src/shuffle_list.rs#L1) single-threaded shuffle_list, no rayon/thread use (grep empty)
- [`consensus/types/src/state/committee_cache.rs:147`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L147) shuffle_list call
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:335`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L335) committee caches built ahead of time

**Sources.** [prysm#4648](https://github.com/OffchainLabs/prysm/pull/4648), [grandine@ec002eda1](https://github.com/grandinetech/grandine/commit/ec002eda1b25)

</details>


<a id="state_transition-104"></a>
<details>
<summary><b>state_transition-104</b> Peek, not consume, in state-root iterator during replay — <i>implemented · low · S · cpu</i></summary>

**Idea.** When replaying blocks with a state-root iterator that has gaps, peek at the next item when testing the slot predicate instead of consuming it, so state roots are not dropped and the tree hash cache is not rebuilt.

**Impact.** Replay no longer drops state roots at gaps, so it does not fall back to recomputing state roots.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/block_replayer.rs:44`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/block_replayer.rs#L44)
- [`consensus/state_processing/src/block_replayer.rs:129`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/block_replayer.rs#L129)
- [`consensus/state_processing/src/block_replayer.rs:185`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/block_replayer.rs#L185)

**Skeptic check.** Confirmed that get_state_root uses peeking_take_while on a Peekable iterator, which is the lighthouse#4803 fix.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#4803](https://github.com/sigp/lighthouse/pull/4803)

</details>


<a id="state_transition-105"></a>
<details>
<summary><b>state_transition-105</b> Per-pubkey index of pending deposits — <i>implemented · low · S · cpu</i></summary>

**Idea.** Index the pending deposit queue by pubkey with progress and verified-signature state, so a deposit request or builder onboarding touches only that pubkey's pending deposits. This avoids quadratic rescans and repeated BLS verification of the whole queue.

**Impact.** No per-block scan or re-verification of the pending queue remains; the fork-time onboarding is linear with cached signature results.

**Best measured result.** Quadratic scan stalled nodes on a devnet (pr:lighthouse#9954)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/builder_deposits_cache.rs:42-80`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/builder_deposits_cache.rs#L42-L80) OnboardBuildersCache pre-verifies pending deposit signatures
- [`consensus/state_processing/src/upgrade/gloas.rs:240-305`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/upgrade/gloas.rs#L240-L305) onboarding uses HashSet of pending-validator pubkeys and a HashMap of builder indices, one registry write
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:883-910`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L883-L910) process_deposit_requests only appends; no scan of pending_deposits
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:925-937`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L925-L937) builder deposits come from a separate request type and scan only the builder registry

**Skeptic check.** Grep found no is_pending_validator scan outside the comment in gloas.rs. The remaining builders().iter().position at line 937/994 is linear in the small builder registry, as the earlier evidence said.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#9954](https://github.com/sigp/lighthouse/pull/9954), [lodestar#9247](https://github.com/ChainSafe/lodestar/pull/9247)

</details>


<a id="state_transition-106"></a>
<details>
<summary><b>state_transition-106</b> Per-slot lock to dedup head state advance — <i>n/a · medium · S · cpu, memory, latency</i></summary>

**Idea.** When several concurrent requests need the head state advanced to the same slot (e.g. sync committee message verification), take a per-slot lock so only one advanced state is computed and the rest reuse it.

**Impact.** Sync committee message verification does not advance a state at all, and the other advance-needing path (attestation shuffling) already dedups with cache Promises.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/sync_committee_verification.rs:471`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/sync_committee_verification.rs#L471) sync committee from chain.sync_committee_at_next_slot, no state advance
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:106`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L106) Promise variant dedups concurrent shuffling computations

**Sources.** [prysm#9595](https://github.com/OffchainLabs/prysm/pull/9595)

</details>


<a id="state_transition-107"></a>
<details>
<summary><b>state_transition-107</b> Persistent tree vectors with non-power-of-two length — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** Support persistent (structurally shared) vectors whose length is not a power of two via an incomplete-tree variant, so such state fields can also use structural sharing.

**Impact.** milhouse Vector wraps a List with depth int_log(N) (next power of two), so any length is structurally shared. Example: ptc_window with PtcWindowLength (not a power of two) is a milhouse Vector.

**Evidence (Lighthouse @ 928b61e719).**

- d67aabd/src/vector.rs:54
- d67aabd/src/utils.rs:42
- d67aabd/src/list.rs:200
- [`consensus/types/src/state/beacon_state.rs:811`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L811)

**Skeptic check.** Confirmed in the milhouse revision in Cargo.lock. The earlier evidence cited the registry 0.9.0 copy, but the code matches.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine#663](https://github.com/grandinetech/grandine/pull/663)

</details>


<a id="state_transition-108"></a>
<details>
<summary><b>state_transition-108</b> Upgrade persistent data structure library for stable timing — <i>n/a · low · S · latency, cpu</i></summary>

**Idea.** Upgrade the persistent data structure library behind state lists to a version that makes block processing time stable.

**Impact.** This was a Lodestar library bump; Lighthouse uses milhouse and has no stable-timing issue tied to a version bump.

**Best measured result.** "We want block processing time to be stable" (no numbers) (pr:lodestar#3363)

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.lock: milhouse 0.9.0 (recent version)

**Sources.** [lodestar#3363](https://github.com/ChainSafe/lodestar/pull/3363)

</details>


<a id="state_transition-109"></a>
<details>
<summary><b>state_transition-109</b> Pipeline independent state transition steps — <i>partial · low · M · cpu, latency</i></summary>

**Idea.** Run independent state transition steps as concurrent pipeline stages so they overlap in time.

**Gap in Lighthouse.** EL verification already overlaps; signature batch verification (SignatureVerifiedBlock) runs before the state transition rather than concurrently, so overlapping them on separate threads would be the remaining step in block_verification.rs.

**Impact.** Could hide up to a few ms to tens of ms of signature verification behind state transition per block; modest.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:775`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L775) payload_verification_handle: EL newPayload runs concurrently with state transition
- [`beacon_node/beacon_chain/src/block_verification.rs:1710`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1710) state transition runs with NoVerification after separate signature verification stage

**Sources.** [prysm#8297](https://github.com/OffchainLabs/prysm/pull/8297)

</details>


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

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [lighthouse#9311](https://github.com/sigp/lighthouse/pull/9311), [prysm#17440](https://github.com/OffchainLabs/prysm/pull/17440), [lodestar#9727](https://github.com/ChainSafe/lodestar/pull/9727), [lodestar#9436](https://github.com/ChainSafe/lodestar/pull/9436), [nimbus#8887](https://github.com/status-im/nimbus-eth2/pull/8887)

</details>


<a id="state_transition-111"></a>
<details>
<summary><b>state_transition-111</b> Preallocate vectors with known capacity — <i>partial · medium · S · cpu, memory</i></summary>

**Idea.** Preallocate result vectors with known or upper-bound capacity in hot state-transition paths (sync committee indices, attesting indices, bit packing, pubkey lists, tree-hash helpers). This removes repeated growth reallocation and copying.

**Gap in Lighthouse.** attesting_indices_electra::get_attesting_indices (also used for Gloas) is the hot path on mainnet today, and it is not preallocated: attesting_indices = vec![] grows by repeated extend, and each committee allocates and hashes a HashSet&lt;u64&gt;. Preallocate with the summed committee lengths (participant_count is known) or aggregation_bits.num_set_bits(), and push directly; committee members are already unique, so the HashSet is not needed for dedup.

**Impact.** On-chain Electra aggregates span up to 64 committees (~30k indices at 1M validators): about 15 Vec regrowths plus ~30k SipHash inserts per attestation, paid in block import (ConsensusContext::get_indexed_attestation) and in gossip aggregate verification.

**Best measured result.** Targets ~38% of profiled alloc_space (packBits 9.3%, attesting indices 9.4%, eligible validators 20%) (pr:caplin#22397)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/common/get_attesting_indices.rs:33`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/get_attesting_indices.rs#L33) base (phase0) path uses with_capacity(num_set_bits)
- [`consensus/state_processing/src/common/get_attesting_indices.rs:102`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/get_attesting_indices.rs#L102) Electra/Gloas get_attesting_indices starts from vec![]
- [`consensus/state_processing/src/common/get_attesting_indices.rs:120-140`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/get_attesting_indices.rs#L120-L140) per committee it collects attesters into a std HashSet&lt;u64&gt; (SipHash) and then extends the Vec
- [`consensus/state_processing/src/consensus_context.rs:181`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/consensus_context.rs#L181) block processing uses the Electra path
- [`beacon_node/beacon_chain/src/attestation_verification.rs:732`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L732) gossip aggregate verification uses the Electra path
- [`consensus/types/src/state/beacon_state.rs:1798`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1798) sync committee indices preallocated

**Skeptic check.** The earlier evidence cited the phase0 path's with_capacity and called line 102 'cold'. That is wrong: line 102 is the Electra/Gloas function that every current attestation goes through.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lighthouse#3301](https://github.com/sigp/lighthouse/pull/3301), [caplin#22397](https://github.com/erigontech/erigon/pull/22397), [prysm#10408](https://github.com/OffchainLabs/prysm/pull/10408), [caplin#6792](https://github.com/erigontech/erigon/pull/6792)

</details>


<a id="state_transition-112"></a>
<details>
<summary><b>state_transition-112</b> Speculatively advance head state before next slot — <i>implemented · medium · S · latency, cpu</i></summary>

**Idea.** Run slot and epoch processing on a cached head state ahead of the next block (also right after a late block), so block import and duties find the pre-state ready and epoch processing is off the critical path; on a miss, fall back to replay.

**Impact.** Block import and duties find the next-slot pre-state ready; epoch processing is off the critical path for any head imported before 9s into the slot.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:125-131`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L125-L131) timer fires 3/4 through each slot
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:258-307`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L258-L307) advance_head runs per_slot_processing (incl. epoch processing) on the head state and caches it
- [`beacon_node/beacon_chain/src/block_verification.rs:2065-2069`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L2065-L2069) load_parent uses get_advanced_hot_state, falls back to replay in per_slot loop at 1607

**Skeptic check.** Verified the timer advances whatever the head is at 3/4 slot, so blocks late by up to ~9s (the grandine#253 case, imported before the attesting interval) are covered. Only blocks imported after 9s miss the advance and pay per_slot_processing at next import; earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#2616](https://github.com/status-im/nimbus-eth2/pull/2616), [nimbus@df7bc87af](https://github.com/status-im/nimbus-eth2/commit/df7bc87af544), [grandine#253](https://github.com/grandinetech/grandine/pull/253)

</details>


<a id="state_transition-113"></a>
<details>
<summary><b>state_transition-113</b> Integer sqrt with primitive arithmetic — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Compute integer square root with primitive 64-bit arithmetic instead of big-number or overflow-checked wrapper types, avoiding garbage and checks in reward calculations.

**Impact.** None left: sqrt runs on primitive u64 via the integer-sqrt crate, once per epoch cache build; no heap allocation.

**Best measured result.** Significantly reduces garbage objects (no numbers) (pr:teku#4813)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/common/base.rs:8-13`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/base.rs#L8-L13) SqrtTotalActiveBalance wraps plain u64 integer_sqrt
- [`consensus/state_processing/src/common/altair.rs:41-48`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/altair.rs#L41-L48) get_base_reward_per_increment uses u64.integer_sqrt()
- [`consensus/state_processing/src/epoch_cache.rs:95`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/epoch_cache.rs#L95) sqrt computed once when the epoch cache is built

**Skeptic check.** Verified every sqrt call site in state_processing operates on u64 with no bignum type; the earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#4813](https://github.com/Consensys-Incorporated/teku/pull/4813)

</details>


<a id="state_transition-114"></a>
<details>
<summary><b>state_transition-114</b> Proposer index from shuffling cache — <i>partial · low · M · cpu</i></summary>

**Idea.** Compute the proposer index from the committee cache by mapping positions in the unshuffled active validator list via the cached shuffling, instead of rebuilding the active validator list per block.

**Gap in Lighthouse.** The mechanism (map unshuffled active index to the committee cache shuffling) was never merged: lighthouse#3263 is CLOSED. Pre-Fulu get_beacon_proposer_index and get_beacon_proposer_indices still rebuild the active list via get_active_validator_indices; this is paid on pre-Fulu replay (BlockReplayer, historic state reconstruction).

**Impact.** None on mainnet live block processing (post-Fulu lookahead removes the need); ~3ms/block saving on pre-Fulu replay only.

**Best measured result.** process block ~6.0ms to ~3.0ms (pr:lighthouse#3263)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:1652-1658`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1652-L1658) post-Fulu proposer read from proposer_lookahead (no active list)
- [`consensus/types/src/state/beacon_state.rs:1659-1665`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1659-L1665) pre-Fulu get_beacon_proposer_index calls get_active_validator_indices on every call
- [`consensus/types/src/state/beacon_state.rs:1172-1185`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1172-L1185) get_active_validator_indices does a full registry iteration, no cache
- pr:lighthouse#3263 state=CLOSED, never merged

**Skeptic check.** The lighthouse member PR #3263 was closed unmerged, so the idea as described is not in the code; the Fulu proposer_lookahead gives the same effect on the live path only. The earlier evidence named the gap correctly but should not have called it implemented.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lighthouse#3263](https://github.com/sigp/lighthouse/pull/3263)

</details>


<a id="state_transition-115"></a>
<details>
<summary><b>state_transition-115</b> Tune incremental vs full rebuild threshold for field tries — <i>n/a · medium · S · cpu</i></summary>

**Idea.** Raise the dirty-index threshold above which a state field trie is fully rebuilt instead of updated incrementally, because post-Electra epochs touch many more validators and incremental updates stay cheaper.

**Impact.** Milhouse persistent trees always update incrementally with no full-rebuild switch, so there is no threshold to tune.

**Best measured result.** limit 8000 to 20000 (pr:prysm#15252)

**Evidence (Lighthouse @ 928b61e719).**

- d67aabd/src/tree.rs:164 with_updated_leaves always applies updates incrementally, no rebuild threshold
- d67aabd/src/list.rs:194 apply_updates

**Sources.** [prysm#15252](https://github.com/OffchainLabs/prysm/pull/15252)

</details>


<a id="state_transition-116"></a>
<details>
<summary><b>state_transition-116</b> Read tree-backed state fields once into locals — <i>n/a · low · S · cpu</i></summary>

**Idea.** Read state.slot and similar tree-backed fields once per function into a local, because each read walks a tree node and decodes bytes.

**Impact.** Tree-backed field reads in LH are cheap struct fields (milhouse only for large lists); the JS view-decode overhead does not exist.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:505-530`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L505-L530) reads via typed accessors

**Sources.** [lodestar#2963](https://github.com/ChainSafe/lodestar/pull/2963), [lodestar#2941](https://github.com/ChainSafe/lodestar/pull/2941)

</details>


<a id="state_transition-117"></a>
<details>
<summary><b>state_transition-117</b> Read proposers from stored proposer_lookahead — <i>implemented · medium · S · cpu</i></summary>

**Idea.** Serve proposer indices for current and next epoch from the state's stored proposer_lookahead instead of recomputing the seeded shuffle-based proposer selection.

**Impact.** The seeded shuffle runs once per epoch, for epoch+2 only; gossip, import and the API read the stored vector.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:1652-1658`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1652-L1658) get_beacon_proposer_index reads proposer_lookahead post-Fulu
- [`consensus/types/src/state/beacon_state.rs:1679-1694`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1679-L1694) get_beacon_proposer_indices serves current and next epoch from lookahead
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:227`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L227) proposer cache fill uses get_beacon_proposer_indices
- [`beacon_node/http_api/src/proposer_duties.rs:285`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/proposer_duties.rs#L285) duties API uses get_beacon_proposer_indices
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:506-532`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L506-L532) process_proposer_lookahead computes only epoch+2

**Skeptic check.** Verified every proposer consumer (proposer cache, duties API, block processing) goes through the lookahead-aware accessors. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#10162](https://github.com/Consensys-Incorporated/teku/pull/10162), [grandine@5add6ceec](https://github.com/grandinetech/grandine/commit/5add6ceec169), [grandine#312](https://github.com/grandinetech/grandine/pull/312), [caplin#21655](https://github.com/erigontech/erigon/pull/21655), [prysm#15129](https://github.com/OffchainLabs/prysm/pull/15129)

</details>


<a id="state_transition-118"></a>
<details>
<summary><b>state_transition-118</b> Read-only bulk traversal of tree-backed lists — <i>implemented · medium · S · memory, cpu</i></summary>

**Idea.** Iterate tree-backed state lists (validators, balances, pending withdrawals, block operations, bitfields) with a read-only bulk traversal of tree nodes instead of per-index get() or converting to an array first. This avoids per-element view creation and tree walks.

**Impact.** Epoch processing and pending-queue scans use bulk tree traversal; the remaining per-index get() calls are on small, bounded loops.

**Evidence (Lighthouse @ 928b61e719).**

- d67aabd/src/iter.rs:7-80 stack-based tree Iter yields &amp;T without per-index root walks (packed leaves too)
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:243`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L243) single-pass epoch uses iter/iter_cow over validators, balances, inactivity scores
- [`consensus/types/src/state/beacon_state.rs:3232-3245`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3232-L3245) get_pending_balance_to_withdraw iterates pending_partial_withdrawals with iter() (the lodestar#7419 case)
- [`consensus/state_processing/src/per_block_processing/withdrawals.rs:275-279`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/withdrawals.rs#L275-L279) withdrawal sweep uses per-index get_validator, bounded and usually stops after 16 hits

**Skeptic check.** Confirmed milhouse Iter is a real bulk traversal and that the hot epoch and pending-list loops use it. The only per-index loop found is the withdrawal sweep, which is bounded and early-exits, so the earlier verdict stands.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#7419](https://github.com/ChainSafe/lodestar/pull/7419), [lodestar@04647c85b](https://github.com/ChainSafe/lodestar/commit/04647c85bc39), [lodestar@e51bcae3a](https://github.com/ChainSafe/lodestar/commit/e51bcae3a9dc), [lodestar#1233](https://github.com/ChainSafe/lodestar/pull/1233)

</details>


<a id="state_transition-119"></a>
<details>
<summary><b>state_transition-119</b> Remove duplicated check in Electra block processing — <i>implemented · low · S · cpu</i></summary>

**Idea.** Remove a check in block processing that runs twice once Electra is active.

**Impact.** None: the duplicated validator-index range check removed in nimbus#7082 never existed in Lighthouse's verify_exit.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/verify_exit.rs:31-34`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/verify_exit.rs#L31-L34) single bounds-checked validator lookup
- [`consensus/state_processing/src/per_block_processing/verify_exit.rs:81-89`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/verify_exit.rs#L81-L89) Electra pending-withdrawal check without a second index range check

**Skeptic check.** nimbus#7082 removed a second `validator_index >= len` check inside the Electra branch; Lighthouse's verify_exit does the bounds check once via validators().get(). Earlier evidence is right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#7082](https://github.com/status-im/nimbus-eth2/pull/7082)

</details>


<a id="state_transition-120"></a>
<details>
<summary><b>state_transition-120</b> Compute committees once for assignment — <i>partial · low · S · cpu</i></summary>

**Idea.** When computing a validator's committee assignment, compute committees once and reuse them instead of computing them twice.

**Gap in Lighthouse.** Attester duties are done once from the committee cache, but Gloas PTC duties (BeaconChain::compute_ptc_duties -&gt; BeaconState::get_ptc_assignment -&gt; get_ptc) rebuild each slot's PTC vector (512-entry Vec allocation + linear contains) for every requested validator: 32*N PTC materialisations per request instead of 32 once plus an index map.

**Impact.** PTC duties request for e.g. 10k validators: ~320k Vec allocations of 512 usize and ~160M comparisons per call; building the 32 PTCs once and a validator-&gt;slot map makes it O(32*512+N). Gloas-only, API path.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:1735-1764`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1735-L1764) validator_attestation_duties reads one cached CommitteeCache for all validators
- [`consensus/types/src/state/committee_cache.rs:295-327`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L295-L327) get_attestation_duties via shuffled_position, no committee recompute
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1766-1812`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1766-L1812) compute_ptc_duties calls get_ptc_assignment per validator (TODO notes O(N*slots*PTCSize))
- [`consensus/types/src/state/beacon_state.rs:3685-3698`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3685-L3698) get_ptc_assignment calls get_ptc for each of 32 slots per validator
- [`consensus/types/src/state/beacon_state.rs:3621-3626`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3621-L3626) get_ptc allocates a fresh Vec&lt;usize&gt; of PTCSize on each call

**Skeptic check.** Attester assignment path upheld (cached committee cache, earlier evidence correct for it), but the new Gloas PTC assignment path recomputes the committee per validator, which is exactly the inefficiency of prysm#3499; the code itself carries a TODO for it.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [prysm#3499](https://github.com/OffchainLabs/prysm/pull/3499)

</details>


<a id="state_transition-121"></a>
<details>
<summary><b>state_transition-121</b> Direct balances access without proxy wrapper — <i>n/a · low · S · cpu</i></summary>

**Idea.** Access the balances list directly in hot state code instead of through a proxy wrapper.

**Impact.** No proxy wrapper in Rust; balances accessed directly (and via the single-pass epoch cache).

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs) balances is a milhouse List accessed directly

**Sources.** [lodestar#3200](https://github.com/ChainSafe/lodestar/pull/3200)

</details>


<a id="state_transition-122"></a>
<details>
<summary><b>state_transition-122</b> Linear deposit processing for many deposits — <i>implemented · low · S · cpu</i></summary>

**Idea.** Process many deposits in linear time by avoiding repeated work per deposit (e.g. recomputing proofs or trees), instead of quadratic work.

**Impact.** None: genesis deposit tree is built incrementally (linear), block and pending-deposit processing use O(1) pubkey lookup.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/genesis.rs:37-46`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/genesis.rs#L37-L46) incremental DepositDataTree push_leaf per deposit at genesis, no tree rebuild
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:652-690`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L652-L690) block deposit proofs verified independently
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:1136`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L1136) pending deposits use pubkey_cache HashMap lookup

**Skeptic check.** teku#2172 restored incremental deposit-tree building for genesis; Lighthouse's initialize_beacon_state_from_eth1 pushes leaves into one incremental tree. Earlier evidence is right, and genesis.rs adds the path it missed.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#2172](https://github.com/Consensys-Incorporated/teku/pull/2172)

</details>


<a id="state_transition-123"></a>
<details>
<summary><b>state_transition-123</b> Avoid double copy of randao mix — <i>n/a · low · S · cpu, memory</i></summary>

**Idea.** Do not copy a randao mix a second time when the state getter already returns an owned copy.

**Impact.** Go owned-copy getter detail; Rust returns references, no double copy.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs) randao mixes are a milhouse Vector read by reference

**Sources.** [prysm#6420](https://github.com/OffchainLabs/prysm/pull/6420)

</details>


<a id="state_transition-124"></a>
<details>
<summary><b>state_transition-124</b> Skip slot processing when state already at target — <i>implemented · medium · S · cpu, startup, latency</i></summary>

**Idea.** Return early from slot advance when the state is already at the target slot, and call only block processing when the pre-state is already advanced. This avoids a redundant state hash tree root and redundant state transitions.

**Impact.** No redundant state-root hashing or slot transitions when the pre-state is already at the block slot.

**Best measured result.** 3x reduction when profiling attestation-request RPC (pr:prysm#4314)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/state_advance.rs:40`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/state_advance.rs#L40) and 98 while state.slot() &lt; target_slot: no-op when already at target
- [`beacon_node/beacon_chain/src/block_verification.rs:1607-1615`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1607-L1615) distance-based per_slot loop; reuses parent state_root instead of hashing when not advanced
- [`beacon_node/beacon_chain/src/block_verification.rs:2064-2069`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L2064-L2069) pre-state loaded already advanced to block slot

**Skeptic check.** Verified both the advance helpers and block import skip slot processing when the state is at the target slot. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#1059](https://github.com/Consensys-Incorporated/teku/pull/1059), [nimbus#177](https://github.com/status-im/nimbus-eth2/pull/177), [prysm#4314](https://github.com/OffchainLabs/prysm/pull/4314), [nimbus#2630](https://github.com/status-im/nimbus-eth2/pull/2630), [prysm#16482](https://github.com/OffchainLabs/prysm/pull/16482), [prysm#3349](https://github.com/OffchainLabs/prysm/pull/3349)

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

**Sources.** [nimbus#5235](https://github.com/status-im/nimbus-eth2/pull/5235), [lodestar@33b4110b9](https://github.com/ChainSafe/lodestar/commit/33b4110b91fd)

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


<a id="state_transition-127"></a>
<details>
<summary><b>state_transition-127</b> Reuse computed next-epoch proposer indices — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** After importing the last slot of an epoch, reuse the already computed next-epoch proposer indices during forkchoice update instead of recomputing the proposer shuffling.

**Impact.** None: the FCU/proposer-prep path reuses cached proposers by decision root; on a miss, post-Fulu it reads the state lookahead instead of reshuffling.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5307-5345`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5307-L5345) get_pre_payload_attributes looks up proposer via with_proposer_cache keyed by proposer shuffling decision root
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:227`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L227) proposer cache populated once per decision root
- [`consensus/types/src/state/beacon_state.rs:1681-1696`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1681-L1696) post-Fulu next-epoch proposers read from proposer_lookahead

**Skeptic check.** Verified the proposer-preparation path in get_pre_payload_attributes uses the decision-root-keyed proposer cache, and the Fulu lookahead makes a miss cheap. Earlier evidence is right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#13377](https://github.com/OffchainLabs/prysm/pull/13377)

</details>


<a id="state_transition-128"></a>
<details>
<summary><b>state_transition-128</b> Reuse pre-advanced state across validation, import, replay — <i>partial · low · S · cpu, latency</i></summary>

**Idea.** Reuse the slot/epoch-advanced state computed earlier (for gossip proposer checks or the next-slot cache) when importing a block or replaying it for rewards, so the epoch transition runs only once.

**Gap in Lighthouse.** The rewards API path does not reuse the pre-advanced state: get_state_before_applying_block (used by compute_beacon_block_rewards and compute_sync_committee_rewards) calls chain.get_state at the parent slot and runs BlockReplayer to block.slot. That reruns the epoch transition for slot-0 blocks, even when the advanced state is in the state cache. Fix: use store.get_advanced_hot_state(parent_root, block.slot, parent_state_root) and replay only the remaining slots.

**Impact.** Gossip, import and production run the epoch transition once. The beacon rewards APIs pay a full epoch transition per slot-0 block query (the prysm#13678 500ms-to-20ms case).

**Best measured result.** 500ms+ to ~20ms for slot-0 blocks (pr:prysm#13678)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1030-1050`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1030-L1050) gossip proposer-cache miss loads parent once and keeps it in opt_parent for import
- [`beacon_node/beacon_chain/src/block_verification.rs:2064-2069`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L2064-L2069) import uses get_advanced_hot_state
- [`beacon_node/beacon_chain/src/block_production/mod.rs:95-101`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L95-L101) block production (and its consensus_block_value) uses the advanced state
- [`beacon_node/http_api/src/sync_committee_rewards.rs:48-77`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/sync_committee_rewards.rs#L48-L77) get_state_before_applying_block loads the parent state at the parent slot and replays to block.slot with BlockReplayer
- [`beacon_node/http_api/src/standard_block_rewards.rs:18`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/standard_block_rewards.rs#L18) block rewards API uses that replay

**Skeptic check.** Confirmed the gossip-to-import reuse (lodestar#2385) and the production path. The earlier evidence missed the rewards-replay path that the idea names explicitly, where Lighthouse replays from the unadvanced parent state.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lodestar#2385](https://github.com/ChainSafe/lodestar/pull/2385), [prysm#13678](https://github.com/OffchainLabs/prysm/pull/13678)

</details>


<a id="state_transition-129"></a>
<details>
<summary><b>state_transition-129</b> Reuse checkpoint state for attestation production — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** For attestation production on an old head, use a cached epoch-boundary checkpoint state instead of replaying slots, so committees are not recomputed.

**Impact.** An old head across an epoch boundary is served from the timer-advanced cached state; committees come from the state's caches instead of a replay.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2124-2136`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2124-L2136) same-epoch head: justified checkpoint and committee length from the head state
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2152-2168`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2152-L2168) other epoch: get_advanced_hot_state, partial_state_advance only if still behind
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:283-288`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L283-L288) timer advances the cached head state one slot every slot, so an old head's epoch-boundary state is already cached

**Skeptic check.** Verified that the state advance timer keeps advancing a stale head every slot, so get_advanced_hot_state returns an epoch-boundary state for attestation production. A partial advance only runs in rare cases (request for a slot before the head, or the timer skipped). This is equivalent to the teku checkpoint-state reuse.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#2533](https://github.com/Consensys-Incorporated/teku/pull/2533)

</details>


<a id="state_transition-130"></a>
<details>
<summary><b>state_transition-130</b> Reuse attesting indices cache in block import — <i>implemented · low · S · cpu</i></summary>

**Idea.** Pass the shared attesting-indices cache into block attestation processing so attesting indices are not recomputed per attestation.

**Impact.** None: attesting indices are computed once per block attestation and shared across signature verification, state transition, fork choice and slasher.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/consensus_context.rs:161-195`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/consensus_context.rs#L161-L195) indexed_attestations memoised by attestation root
- [`consensus/state_processing/src/per_block_processing/block_signature_verifier.rs:297`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/block_signature_verifier.rs#L297) signature verification fills the cache
- [`consensus/state_processing/src/per_block_processing/verify_attestation.rs:92`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/verify_attestation.rs#L92) block processing reuses it
- [`beacon_node/beacon_chain/src/block_verification.rs:1283-1285`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1283-L1285) same context carried from signature verification into execution-pending block
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4987-5106`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4987-L5106) fork choice, observers and slasher on import reuse ctxt.get_indexed_attestation

**Skeptic check.** Traced ConsensusContext from signature verification through per_block_processing and import_block; one context is reused throughout. Earlier evidence is right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#3792](https://github.com/Consensys-Incorporated/teku/pull/3792)

</details>


<a id="state_transition-131"></a>
<details>
<summary><b>state_transition-131</b> Cache the full epoch shuffling per seed — <i>implemented · low · S · cpu</i></summary>

**Idea.** Compute the full shuffled validator list once per epoch, cache it keyed by seed/epoch, and slice committees from it at every call site, instead of shuffling per slot or per call.

**Impact.** The full shuffle runs once per epoch per decision root and is shared by all call sites.

**Best measured result.** Block import 16384: 0.266 to 0.183 s; 32768: 0.387 to 0.219 s; epoch 32768: 1.638 to 1.493 s (pr:teku#1278)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/committee_cache.rs:135-150`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L135-L150) active list and shuffle_list computed once per epoch; committees are slices
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:128`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L128) ShufflingCache keyed by AttestationShufflingId (decision root + epoch)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7593`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7593) with_committee_cache serves gossip attestation verification from the shuffling cache

**Skeptic check.** Confirmed that CommitteeCache holds the whole-epoch shuffling and that the chain-level ShufflingCache shares it across gossip and API callers. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#1095](https://github.com/status-im/nimbus-eth2/pull/1095), [prysm#2682](https://github.com/OffchainLabs/prysm/pull/2682), [teku#1278](https://github.com/Consensys-Incorporated/teku/pull/1278)

</details>


<a id="state_transition-132"></a>
<details>
<summary><b>state_transition-132</b> Per-index shuffle with per-index cache — <i>n/a · low · cpu, memory</i></summary>

**Idea.** Compute committee membership by shuffling individual indices with swap-or-not and caching by (seed, index), instead of shuffling and caching the whole list.

**Impact.** Lighthouse needs every validator shuffled each epoch, where the whole-list algorithm is ~250x faster than per-index; the per-index idea only suits tiny lookups, which it already does for proposer/sync.

**Best measured result.** 4M validators worst case 282 ms; 128000 validators 10 s -&gt; 7.7 ms uncached (pr:prysm#2728)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/swap_or_not_shuffle/src/compute_shuffled_index.rs:21`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/swap_or_not_shuffle/src/compute_shuffled_index.rs#L21) per-index shuffle exists, used only for proposer/sync selection
- [`consensus/types/src/state/committee_cache.rs:147`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L147) committees use whole-list shuffle_list

**Sources.** [prysm#2728](https://github.com/OffchainLabs/prysm/pull/2728)

</details>


<a id="state_transition-133"></a>
<details>
<summary><b>state_transition-133</b> Pass committee cache into voluntary exit processing — <i>n/a · low · cpu</i></summary>

**Idea.** Pass the existing committee/state cache into voluntary exit processing instead of building it from scratch per exit.

**Impact.** Exit processing in Lighthouse needs no committee cache; nothing is rebuilt per exit.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/verify_exit.rs:21`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/verify_exit.rs#L21) verify_exit only reads validators, no committee cache
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:573`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L573) process_exits

**Sources.** [nimbus#1507](https://github.com/status-im/nimbus-eth2/pull/1507)

</details>


<a id="state_transition-134"></a>
<details>
<summary><b>state_transition-134</b> Reuse destination tree buffers on state copy — <i>n/a · low · memory, cpu</i></summary>

**Idea.** When copying a state's Merkle tree into a reusable destination, reuse its layer buffers (grow with headroom only when too small) and memcpy, instead of allocating new layers per copy.

**Impact.** Milhouse persistent trees share structure on clone; there is no flat destination buffer copy to reuse.

**Best measured result.** Reduced allocs by 58% overall (pr:caplin#12696)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/upgrade/capella.rs:70`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/upgrade/capella.rs#L70) mem::take moves caches
- [`beacon_node/store`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store) state handling uses milhouse persistent trees with structural sharing

**Sources.** [caplin#12696](https://github.com/erigontech/erigon/pull/12696)

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

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [lodestar#9601](https://github.com/ChainSafe/lodestar/pull/9601)

</details>


<a id="state_transition-136"></a>
<details>
<summary><b>state_transition-136</b> Mutate state in place in fork upgrade — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** In fork upgrade functions, mutate the freshly built state in place instead of copying it first.

**Impact.** None: upgrades take &amp;mut pre-state and move fields; the leftover .clone() calls are on persistent milhouse vectors (cheap Arc clones); runs once per fork.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/upgrade/capella.rs:16-72`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/upgrade/capella.rs#L16-L72) mem::take of large fields, remaining clones are milhouse Arc-shared
- [`consensus/state_processing/src/upgrade/electra.rs:103-169`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/upgrade/electra.rs#L103-L169) same pattern
- [`consensus/state_processing/src/upgrade/fulu.rs:45-66`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/upgrade/fulu.rs#L45-L66) same pattern

**Skeptic check.** Checked all upgrade_* functions: they move or structurally share fields, with no full-state deep copy. Earlier evidence is right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#10102](https://github.com/OffchainLabs/prysm/pull/10102)

</details>


<a id="state_transition-137"></a>
<details>
<summary><b>state_transition-137</b> Roll back on failure instead of cloning state — <i>n/a · medium · cpu, memory</i></summary>

**Idea.** When producing a block or applying speculative changes, apply on the live state and roll back on failure instead of cloning the whole BeaconState.

**Impact.** Cloning a BeaconState in Lighthouse is a structural-sharing clone (milhouse Arc trees, rpds persistent caches), so the speculative-apply-on-a-clone design already avoids the full copy that rollback was meant to avoid.

**Best measured result.** state_sim 30% faster (pr:nimbus#1060)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:96`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L96) BeaconState derives Clone over milhouse persistent trees (Arc-shared nodes)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5344`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5344) states are taken by cheap .clone() of the head state

**Sources.** [nimbus#1060](https://github.com/status-im/nimbus-eth2/pull/1060), [nimbus@f06df1cea](https://github.com/status-im/nimbus-eth2/commit/f06df1cea6eb)

</details>


<a id="state_transition-138"></a>
<details>
<summary><b>state_transition-138</b> Keep state small to cheapen clones — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Avoid full-state clones on hot paths (or keep the state small) because whole-state clone cost scales with state size; use structural sharing.

**Impact.** None: state clones share structure through milhouse trees (Arc leaves) and persistent rpds caches.

**Best measured result.** state around 900Kb, slow for proto.Clone (pr:prysm#2144)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:717-725`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L717-L725)
- [`consensus/types/src/state/pubkey_cache.rs:1-14`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/pubkey_cache.rs#L1-L14)
- ~/.cargo/registry/src/*/milhouse-0.9.0/src/leaf.rs:8-27

**Skeptic check.** Verified BeaconState fields are milhouse List/ProgressiveList with Arc&lt;T&gt; leaves and the pubkey/slashings caches are rpds persistent maps, so a clone is O(1) per field. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#2144](https://github.com/OffchainLabs/prysm/pull/2144)

</details>


<a id="state_transition-139"></a>
<details>
<summary><b>state_transition-139</b> Sample PTC per committee without concatenation — <i>not · low · S · memory, cpu</i></summary>

**Idea.** Compute the payload timeliness committee by sampling committee by committee instead of concatenating all beacon committees of the slot into one temporary list.

**Gap in Lighthouse.** Change compute_ptc_with_cache/compute_balance_weighted_selection to index into committee slices lazily (compute the committee-offset mapping) instead of collecting a Vec of all slot committee members.

**Impact.** Saves one small allocation and copy (~thousands of usizes) per slot of PTC window computation, once per epoch; negligible and Gloas-only.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:3639`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3639) compute_ptc_with_cache flat_maps all slot committees into a Vec&lt;usize&gt; before compute_balance_weighted_selection
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:539`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L539) process_ptc_window calls it per slot

**Sources.** [prysm#16293](https://github.com/OffchainLabs/prysm/pull/16293)

</details>


<a id="state_transition-140"></a>
<details>
<summary><b>state_transition-140</b> Share pubkey caches across epoch-context copies — <i>implemented · medium · S · cpu, memory</i></summary>

**Idea.** Share pubkey-to-index and index-to-pubkey caches between epoch-context/state copies instead of deep-copying them per block, and check indexed-attestation sortedness with one linear pass instead of a set and sort.

**Impact.** None: pubkey cache is a persistent HashTrieMap shared across state copies; sortedness is one tuple_windows pass.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/pubkey_cache.rs:6-38`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/pubkey_cache.rs#L6-L38)
- [`consensus/state_processing/src/per_block_processing/is_valid_indexed_attestation.rs:36-50`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/is_valid_indexed_attestation.rs#L36-L50)

**Skeptic check.** Confirmed PubkeyCache is rpds HashTrieMapSync with insert_mut only for new indices, and check_sorted is a single linear pass over the indices. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@e5872c38d](https://github.com/ChainSafe/lodestar/commit/e5872c38da27)

</details>


<a id="state_transition-141"></a>
<details>
<summary><b>state_transition-141</b> Carry pubkey index cache across fork upgrade — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** At the fork upgrade, carry the pubkey-to-index cache from the pre-fork state into the upgraded state instead of rebuilding it.

**Impact.** None: every upgrade_state_to_* moves pubkey_cache with mem::take, and Gloas builder onboarding uses state.get_validator_index on the carried cache.

**Best measured result.** Speeds up onboardBuildersFromPendingDeposits (no numbers) (pr:teku#10917)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/upgrade/electra.rs:167`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/upgrade/electra.rs#L167)
- [`consensus/state_processing/src/upgrade/fulu.rs:109`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/upgrade/fulu.rs#L109)
- [`consensus/state_processing/src/upgrade/gloas.rs:174`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/upgrade/gloas.rs#L174)
- [`consensus/state_processing/src/upgrade/gloas.rs:180`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/upgrade/gloas.rs#L180)
- [`consensus/state_processing/src/upgrade/gloas.rs:260`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/upgrade/gloas.rs#L260)

**Skeptic check.** Confirmed all eight upgrade files take the pre-state pubkey cache; onboard_builders_from_pending_deposits (the Teku hot spot) looks up the carried cache rather than rebuilding. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#10917](https://github.com/Consensys-Incorporated/teku/pull/10917)

</details>


<a id="state_transition-142"></a>
<details>
<summary><b>state_transition-142</b> Scan registry backwards for deposit pubkeys — <i>implemented · low · S · cpu</i></summary>

**Idea.** Without an index, search the validator registry backwards for deposit pubkeys, because top-up deposits tend to match recent validators.

**Impact.** None: a persistent pubkey-&gt;index HashMap lookup is O(1), which beats nimbus's backward linear scan on every deposit path.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/verify_deposit.rs:39`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/verify_deposit.rs#L39) get_existing_validator_index via state.get_validator_index (pubkey cache)
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:733`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L733) apply_deposit uses it
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:1136`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L1136) pending deposits use pubkey_cache().get

**Skeptic check.** nimbus#5914 is a workaround for having no index; Lighthouse keeps a long-lived pubkey cache on the state and uses it for both block deposits and Electra pending deposits. Earlier evidence is right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#5914](https://github.com/status-im/nimbus-eth2/pull/5914)

</details>


<a id="state_transition-143"></a>
<details>
<summary><b>state_transition-143</b> Sync signature checks independent of exact state — <i>implemented · medium · S · cpu, memory</i></summary>

**Idea.** Build block signature sets (sync aggregate) from block data and the sync committee indices rather than the full head state, so verification works on any state of the epoch and can batch across blocks.

**Impact.** None: sync_aggregate_signature_set takes block slot and parent root as arguments and reads only the epoch's sync committee, fork and genesis root from state.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/signature_sets.rs:794-845`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/signature_sets.rs#L794-L845)
- [`consensus/state_processing/src/per_block_processing/block_signature_verifier.rs:367-385`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/block_signature_verifier.rs#L367-L385)

**Skeptic check.** Confirmed the function signature and doc comment explicitly support batch verification on a state that has not had the blocks applied; include_sync_aggregate passes block.slot() and block.parent_root(). Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#8720](https://github.com/ChainSafe/lodestar/pull/8720), [lodestar#4280](https://github.com/ChainSafe/lodestar/pull/4280)

</details>


<a id="state_transition-144"></a>
<details>
<summary><b>state_transition-144</b> Single shared shuffled-index computation for sampling — <i>not · low · M · cpu</i></summary>

**Idea.** Do proposer and sync committee sampling through one shared swap-or-not shuffled-index computation instead of a second private fixed-capacity cache.

**Gap in Lighthouse.** Both samplers compute per-index swap-or-not (90 rounds of hashing each) independently; could share a full shuffle_list result or memoise pivot/source hashes across candidates. Functions: compute_proposer_indices, get_next_sync_committee_indices, compute_balance_weighted_selection.

**Impact.** Sampling needs a few hundred shuffled-index calls per epoch for sync committee (period boundary) and 32 proposers; saving is a few ms per epoch at most.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:1353`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1353) compute_proposer_index and :1770 get_next_sync_committee_indices both call compute_shuffled_index per candidate ([`consensus/swap_or_not_shuffle/src/compute_shuffled_index.rs:21`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/swap_or_not_shuffle/src/compute_shuffled_index.rs#L21))

**Sources.** [lodestar@807bae379](https://github.com/ChainSafe/lodestar/commit/807bae379eb0)

</details>


<a id="state_transition-145"></a>
<details>
<summary><b>state_transition-145</b> Single-pass participation flag update — <i>implemented · medium · S · cpu, memory</i></summary>

**Idea.** Mutate participation flags in one pass through a callback instead of copying the participation list on read and again on write per attestation.

**Impact.** None: participation flags are mutated in place via get_epoch_participation_mut().get_mut(index).add_flag().

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/process_operations.rs:258-290`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L258-L290)
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:388-400`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L388-L400)

**Skeptic check.** Confirmed in-place per-validator mutation through milhouse get_mut on both the Altair and Gloas attestation paths; no whole-list read-copy-write. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#10409](https://github.com/OffchainLabs/prysm/pull/10409)

</details>


<a id="state_transition-146"></a>
<details>
<summary><b>state_transition-146</b> Skip deposit crypto when building test genesis — <i>not · low · S · cpu, startup</i></summary>

**Idea.** For test and devnet genesis, allow disabling deposit signature and Merkle proof generation/verification and deposit root computation, so large initial states build quickly.

**Gap in Lighthouse.** Add a flag to initialize_beacon_state_from_eth1/apply_deposit to skip proof and signature verification and deposit-tree building for test genesis.

**Impact.** Only speeds up building huge test/devnet genesis states; no effect on mainnet nodes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/genesis/src/interop.rs:79-140`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/genesis/src/interop.rs#L79-L140) build_genesis_state signs every deposit then calls initialize_beacon_state_from_eth1
- [`consensus/state_processing/src/genesis.rs:18-47`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/genesis.rs#L18-L47) pushes deposit tree leaf and apply_deposit with Some(proof) so Merkle proof and signature are always verified

**Sources.** [teku#1089](https://github.com/Consensys-Incorporated/teku/pull/1089), [teku#1148](https://github.com/Consensys-Incorporated/teku/pull/1148), [teku#1147](https://github.com/Consensys-Incorporated/teku/pull/1147)

</details>


<a id="state_transition-147"></a>
<details>
<summary><b>state_transition-147</b> Skip mock genesis when loading stored state — <i>n/a · low · S · startup</i></summary>

**Idea.** When starting from a stored SSZ state, skip generating a mock genesis state and take validator indices from the loaded state.

**Impact.** No startup cost to save; LH loads the checkpoint/stored state directly.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/genesis.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/genesis.rs): LH has no mock-genesis path when loading a stored state

**Sources.** [teku#870](https://github.com/Consensys-Incorporated/teku/pull/870)

</details>


<a id="state_transition-148"></a>
<details>
<summary><b>state_transition-148</b> Skip deposit-count check after bridge transition — <i>n/a · low · S · cpu</i></summary>

**Idea.** Skip the eth1 deposit-count check in block processing once the deposit requests transition period is complete.

**Impact.** Nothing to save; the check is a few integer comparisons per block.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/process_operations.rs:652-686`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L652-L686) process_deposits: the post-transition check is an O(1) compare of eth1_deposit_index with min(start_index,deposit_count), no scan

**Sources.** [grandine#176](https://github.com/grandinetech/grandine/pull/176)

</details>


<a id="state_transition-149"></a>
<details>
<summary><b>state_transition-149</b> Scan pending deposits only for blocks with deposits — <i>n/a · low · S · cpu</i></summary>

**Idea.** Scan the state's pending deposits for validators only when the block contains deposits, skipping that scan for most blocks.

**Impact.** LH never scans pending_deposits per block; builder deposits arrive in a separate list and scan builders only when present.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/process_operations.rs:883-910`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L883-L910) process_deposit_requests only pushes to pending_deposits, no scan
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:710-790`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L710-L790) apply_deposit uses the pubkey cache, no pending scan
- [`consensus/state_processing/src/upgrade/gloas.rs:227-278`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/upgrade/gloas.rs#L227-L278) pending-validator scan done once at fork upgrade with a HashSet

**Sources.** [nimbus#8555](https://github.com/status-im/nimbus-eth2/pull/8555)

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


<a id="state_transition-151"></a>
<details>
<summary><b>state_transition-151</b> Avoid redundant deposit pubkey decompression — <i>implemented · low · S · cpu</i></summary>

**Idea.** In deposit processing do not decompress/subgroup-check the deposit pubkey separately from signature verification; use the already-deserialized pubkey cache.

**Impact.** Already done; deposits are rare, so the gain is small.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/process_operations.rs:733`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L733)
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:757`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L757)
- [`consensus/state_processing/src/per_block_processing/signature_sets.rs:545-554`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/signature_sets.rs#L545-L554)
- [`consensus/state_processing/src/per_block_processing/verify_deposit.rs:23-33`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/verify_deposit.rs#L23-L33)
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:1136`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L1136)

**Skeptic check.** apply_deposit and the Electra pending-deposit path in single_pass look up the existing validator by PublicKeyBytes in the state pubkey cache. The pubkey is decompressed only once, inside deposit_pubkey_signature_message, and only for new validators. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#1610](https://github.com/sigp/lighthouse/pull/1610), [teku#2173](https://github.com/Consensys-Incorporated/teku/pull/2173), [lighthouse#545](https://github.com/sigp/lighthouse/pull/545)

</details>


<a id="state_transition-152"></a>
<details>
<summary><b>state_transition-152</b> Skip registry update on skip slots — <i>n/a · low · S · cpu, latency</i></summary>

**Idea.** Skip validator registry updates when there is no block (skip slot), so concurrent duty requests do not each take the registry lock and redo it.

**Impact.** LH has no registry lock and no per-request registry update, so skip slots cost nothing extra.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs): registry updates run once per epoch inside epoch processing, not per slot or per duty request

**Sources.** [prysm#2326](https://github.com/OffchainLabs/prysm/pull/2326)

</details>


<a id="state_transition-153"></a>
<details>
<summary><b>state_transition-153</b> Drop stale slot ticks; small tier indices — <i>n/a · low · S · cpu</i></summary>

**Idea.** Drop outdated slot-ticker events at the source, and use small u8 indices to make the state smaller.

**Impact.** Silver-specific design (slot ticker events, u8 tier indices); no equivalent in LH.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/timer`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/timer): slot clock is a single timer task with no tier indices

**Sources.** [silver#13](https://github.com/gattaca-com/silver/pull/13)

</details>


<a id="state_transition-154"></a>
<details>
<summary><b>state_transition-154</b> Advance next epoch only when lookahead needs it — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Cache next-epoch proposer shuffling, with the extra epoch of state advance, only when the fork needs it (post-Fulu lookahead), not on pre-Fulu networks.

**Impact.** None: this is Lighthouse's own PR #8388; next-epoch proposer caching is gated on state.slot() &gt; proposer_shuffling_decision_slot(next_epoch), which is only reachable post-Fulu.

**Best measured result.** State advances observed especially slow pre-Fulu; no numbers (pr:lighthouse#8388)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:369-392`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L369-L392)
- [`consensus/types/src/core/chain_spec.rs:1176-1196`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/core/chain_spec.rs#L1176-L1196)

**Skeptic check.** Confirmed the gate and the fulu_enabled(epoch-1) branch in proposer_shuffling_decision_slot. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#8388](https://github.com/sigp/lighthouse/pull/8388)

</details>


<a id="state_transition-155"></a>
<details>
<summary><b>state_transition-155</b> Skip pre-fork withdrawal calc; single pass — <i>implemented · low · S · cpu</i></summary>

**Idea.** Skip computing partially withdrawn balance before the fork that uses it, and compute it in a single pass instead of filter then reduce.

**Impact.** None on current forks. The value is used post-Electra, and the Rust filter/map/sum chain is already a single lazy pass over at most 16 withdrawals.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/withdrawals.rs:125-129`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/withdrawals.rs#L125-L129)
- [`consensus/state_processing/src/per_block_processing/withdrawals.rs:281`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/withdrawals.rs#L281)
- [`consensus/state_processing/src/per_block_processing/withdrawals.rs:314-328`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/withdrawals.rs#L314-L328)

**Skeptic check.** get_balance_after_withdrawals uses one lazy iterator pass with no intermediate array, so the 'single pass' half is done. The sweep at line 281 still runs it pre-Electra, but only historical Capella/Deneb replay hits that, and it costs a handful of compares. The earlier evidence cited the early return of the pending-partials function, not the sweep, but the conclusion holds.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#7389](https://github.com/ChainSafe/lodestar/pull/7389)

</details>


<a id="state_transition-156"></a>
<details>
<summary><b>state_transition-156</b> Slashed-validator bitset cache — <i>implemented · medium · S · memory, cpu</i></summary>

**Idea.** Keep a bitset of slashed flags per state (cloned lazily on write) so attestation processing checks slash status without reading validator records.

**Impact.** None: SlashingsCache is a persistent HashTrieSet (O(1) clone, sparse so tiny memory) consulted in attestation processing.

**Best measured result.** 0-30MB vs ~500MB extra memory; clone 60x faster (pr:lodestar#4401)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/slashings_cache.rs:7-30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/slashings_cache.rs#L7-L30)
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:263`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L263)
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:393`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L393)

**Skeptic check.** Confirmed the persistent set and its use in both attestation paths; a sparse set achieves the same clone-cost and memory effect as Lodestar's bitset. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#4401](https://github.com/ChainSafe/lodestar/pull/4401), [lodestar@d5dcf7cb1](https://github.com/ChainSafe/lodestar/commit/d5dcf7cb1838)

</details>


<a id="state_transition-157"></a>
<details>
<summary><b>state_transition-157</b> Native slice instead of per-byte copy — <i>implemented · low · S · cpu</i></summary>

**Idea.** Take the first N bytes of a root with a native slice/copy instead of a per-byte loop when computing domains and fork digests.

**Impact.** None; the copies are already memcpy slices, and the fork-data tree hash dominates.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/core/chain_spec.rs:722-737`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/core/chain_spec.rs#L722-L737)
- [`consensus/types/src/core/chain_spec.rs:658-665`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/core/chain_spec.rs#L658-L665)

**Skeptic check.** compute_domain and compute_fork_digest use copy_from_slice on slices of the root. The only per-byte loop is a 4-byte XOR for the Fulu blob mask, which is trivial. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@bf6d8524a](https://github.com/ChainSafe/lodestar/commit/bf6d8524a114)

</details>


<a id="state_transition-158"></a>
<details>
<summary><b>state_transition-158</b> Specialized converters for hot structs — <i>n/a · low · S · cpu</i></summary>

**Idea.** Use specialized creation/conversion code for hot structs (validator) instead of generic reflective loops.

**Impact.** None: derives are static code, no reflective loops.

**Best measured result.** createValidatorFlat much faster than createFlat (pr:lodestar#2331)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/validator/validator.rs:22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/validator/validator.rs#L22) Validator is a plain struct with derived TreeHash

**Sources.** [lodestar#2331](https://github.com/ChainSafe/lodestar/pull/2331), [lodestar@6534332d8](https://github.com/ChainSafe/lodestar/commit/6534332d84bb)

</details>


<a id="state_transition-159"></a>
<details>
<summary><b>state_transition-159</b> Compare against static default value — <i>not · low · S · cpu</i></summary>

**Idea.** Compare execution payload headers against a precomputed static default instead of constructing a zeroed temporary on every merge-complete check.

**Gap in Lighthouse.** Only Bellatrix-only states hit the compare; the temp is cheap (empty VariableLists). Could compare fields to zero in is_default_with_zero_roots.

**Impact.** Negligible: path is skipped after Capella.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing.rs:505`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing.rs#L505) is_merge_transition_complete returns true on Capella+ without any compare
- [`consensus/types/src/execution/execution_payload_header.rs:172`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/execution/execution_payload_header.rs#L172) compares with Default::default() temp

**Sources.** [nimbus#3399](https://github.com/status-im/nimbus-eth2/pull/3399)

</details>


<a id="state_transition-160"></a>
<details>
<summary><b>state_transition-160</b> Plain structs for pending queue items — <i>implemented · medium · S · cpu</i></summary>

**Idea.** Represent pending deposit, partial withdrawal and consolidation items as plain structs rather than tree-backed containers, so epoch processing over tens of thousands of items does direct field reads.

**Impact.** None: pending queue items are plain Rust structs stored as Arc&lt;T&gt; milhouse leaves; field reads are direct.

**Best measured result.** ~33x speedup: 12.8 ops/s to 417 ops/s on 50,000 items (pr:lodestar#9054)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:717-725`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L717-L725)
- ~/.cargo/registry/src/*/milhouse-0.9.0/src/leaf.rs:8-15
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:1104-1106`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L1104-L1106)

**Skeptic check.** Confirmed milhouse Leaf holds value: Arc&lt;T&gt;, so iterating pending_deposits in single_pass reads struct fields without per-field tree traversal (Lodestar's ContainerType problem does not exist here). Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#9054](https://github.com/ChainSafe/lodestar/pull/9054)

</details>


<a id="state_transition-161"></a>
<details>
<summary><b>state_transition-161</b> Structural equality instead of serialize-and-compare — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Compare containers (eth1 data, headers, attestation data) with type-aware structural equality instead of serializing both and comparing bytes.

**Impact.** None; already structural equality.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing.rs:377-381`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing.rs#L377-L381)
- [`consensus/state_processing/src/per_block_processing/verify_proposer_slashing.rs:40`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/verify_proposer_slashing.rs#L40)
- [`consensus/types/src/validator/validator.rs:19`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/validator/validator.rs#L19)

**Skeptic check.** The places the lodestar commit changed (eth1 vote counting and proposer-slashing header comparison) use derived PartialEq in LH (`*vote == eth1_data`, `header_1 != header_2`). A grep found no as_ssz_bytes()== or tree_hash_root()== comparisons on the hot paths.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@0c42ad2eb](https://github.com/ChainSafe/lodestar/commit/0c42ad2ebfb1)

</details>


<a id="state_transition-162"></a>
<details>
<summary><b>state_transition-162</b> Tree-backed state in tests — <i>n/a · low · S · cpu</i></summary>

**Idea.** Use tree-backed (persistent Merkle) state in tests instead of plain objects so large state operations are cheaper.

**Impact.** Only affects test speed; Lighthouse states are already tree-backed.

**Best measured result.** finality tests 67-167s to ~10s each (pr:lodestar#1795)

**Evidence (Lighthouse @ 928b61e719).**

- test-only idea; BeaconState already uses milhouse persistent trees

**Sources.** [lodestar#1795](https://github.com/ChainSafe/lodestar/pull/1795)

</details>


<a id="state_transition-163"></a>
<details>
<summary><b>state_transition-163</b> Return read-only validator wrapper by value — <i>n/a · low · S · memory, cpu</i></summary>

**Idea.** Return short-lived read-only validator wrappers by value instead of pointer so they stay on the stack and cause no heap allocation per read.

**Impact.** Go pointer-escape detail; Rust returns references with no heap allocation.

**Best measured result.** No numbers (pr:prysm#7710)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/validator/validator.rs:22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/validator/validator.rs#L22) validators accessed as &amp;Validator via milhouse

**Sources.** [prysm#9410](https://github.com/OffchainLabs/prysm/pull/9410), [prysm#7710](https://github.com/OffchainLabs/prysm/pull/7710)

</details>


<a id="state_transition-164"></a>
<details>
<summary><b>state_transition-164</b> Zero-copy validator pubkey access — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Expose validator pubkeys as a slice view into the state buffer instead of copying 48 bytes per access.

**Impact.** None; validators are held as structs in the milhouse tree and pubkeys are borrowed through get_validator().

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/validator/validator.rs:21-22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/validator/validator.rs#L21-L22)
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:1136`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L1136)

**Skeptic check.** The Caplin issue came from a flat serialized buffer that copied on every access. LH stores Validator structs with PublicKeyBytes in persistent tree leaves, and access is by reference. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#7622](https://github.com/erigontech/erigon/pull/7622)

</details>


<a id="state_transition-165"></a>
<details>
<summary><b>state_transition-165</b> Pass large inputs by reference, not by value — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Pass shuffling inputs and hash lists to helper functions by reference or borrow instead of moving or cloning them on every call. This avoids per-call allocations and copies in shuffling and attestation helpers.

**Impact.** Large inputs are borrowed or moved once; the 2018 commits are Lighthouse's own and long superseded.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/swap_or_not_shuffle/src/shuffle_list.rs:92`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/swap_or_not_shuffle/src/shuffle_list.rs#L92) shuffle_list takes Vec by value, shuffles in place
- [`consensus/types/src/state/committee_cache.rs:195`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L195) shuffling() returns &amp;[usize]
- [`consensus/state_processing/src/common/get_attesting_indices.rs:96`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/get_attesting_indices.rs#L96) takes references to committees and aggregation bits

**Skeptic check.** Both members are Lighthouse commits; current helpers borrow. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@4ec0de6f5](https://github.com/sigp/lighthouse/commit/4ec0de6f5e1b), [lighthouse@29cfc4dce](https://github.com/sigp/lighthouse/commit/29cfc4dce91c)

</details>


<a id="state_transition-166"></a>
<details>
<summary><b>state_transition-166</b> Append into one shared output buffer — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** When gathering results (such as expected withdrawals) from several helpers, pass one output buffer to each helper to append into rather than returning new vectors that are then concatenated. This removes intermediate allocations and copies.

**Impact.** Already a single shared output buffer.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/withdrawals.rs:28`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/withdrawals.rs#L28) Vec::with_capacity(max_withdrawals_per_payload)
- [`consensus/state_processing/src/per_block_processing/withdrawals.rs:32-44`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/withdrawals.rs#L32-L44) get_builder_withdrawals, get_pending_partial_withdrawals, get_builders_sweep_withdrawals, get_validators_sweep_withdrawals all append into &amp;mut Vec&lt;Withdrawal&gt;

**Skeptic check.** Verified all four helpers take &amp;mut withdrawals. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#16282](https://github.com/OffchainLabs/prysm/pull/16282)

</details>


<a id="state_transition-167"></a>
<details>
<summary><b>state_transition-167</b> Mutate one epoch context in place across transition — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Use a single epoch/shuffling context object through block and slot processing and mutate it in place, instead of wrapping and copying it into a transition-specific context and rebuilding it per block. This avoids per-block context copies.

**Impact.** No per-block wrapping or copy of the epoch context exists in Lighthouse.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:825`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L825) committee caches stored in the state as Arc, reused across blocks
- [`consensus/state_processing/src/consensus_context.rs:18`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/consensus_context.rs#L18) ConsensusContext is a small per-block struct with no copied epoch data

**Skeptic check.** Lodestar's change removed a JS-specific wrapper copy; Lighthouse keeps epoch caches in the state and never rebuilds them per block. Upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@f6aefc9af](https://github.com/ChainSafe/lodestar/commit/f6aefc9af3f6)

</details>


<a id="state_transition-168"></a>
<details>
<summary><b>state_transition-168</b> Cache sync participant reward per epoch — <i>partial · low · S · cpu</i></summary>

**Idea.** Compute the sync committee participant reward once per epoch and store it in the epoch cache rather than recomputing it each block. Also read attestation aggregation bits through a faster direct accessor than generic bitlist indexing.

**Gap in Lighthouse.** The participant/proposer reward is not cached per epoch (compute_sync_aggregate_rewards runs per block), and the sync committee validator indices are re-derived via 512 pubkey lookups in BeaconState::get_sync_committee_indices on every block instead of being cached per sync-committee period. The bit-access half is implemented.

**Impact.** Microseconds per block (one isqrt plus ~512 hash lookups); not measurable in block import time.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/altair/sync_committee.rs:47`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/altair/sync_committee.rs#L47) compute_sync_aggregate_rewards called on every block
- [`consensus/state_processing/src/per_block_processing/altair/sync_committee.rs:83-104`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/altair/sync_committee.rs#L83-L104) reward recomputed (BaseRewardPerIncrement::new does an integer sqrt) per block
- [`consensus/state_processing/src/per_block_processing/altair/sync_committee.rs:50`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/altair/sync_committee.rs#L50) get_sync_committee_indices per block
- [`consensus/types/src/state/beacon_state.rs:1753-1767`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1753-L1767) get_sync_committee_indices: 512 pubkey-cache hash lookups + Vec alloc per call
- [`consensus/state_processing/src/per_block_processing/altair/sync_committee.rs:58`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/altair/sync_committee.rs#L58) sync_committee_bits.iter() direct bit iteration

**Skeptic check.** Earlier verdict admitted the reward is recomputed per block, so the caching mechanism is not implemented; only the direct bit iteration is. Saving is negligible in Rust.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lodestar#2554](https://github.com/ChainSafe/lodestar/pull/2554)

</details>


<a id="state_transition-169"></a>
<details>
<summary><b>state_transition-169</b> Store payload timeliness committee window in state — <i>implemented · low · S · cpu</i></summary>

**Idea.** Keep the payload timeliness committee for the lookahead window in the beacon state and refresh it once per epoch, so per-slot lookups read the cached value instead of redoing the balance-weighted selection.

**Impact.** Per-slot PTC lookups (payload attestation verification, API, op pool) read state.ptc_window; balance-weighted selection (compute_ptc_with_cache) runs only in process_ptc_window and the Gloas upgrade.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:811`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L811)
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:539-576`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L539-L576)
- [`consensus/types/src/state/beacon_state.rs:3591-3625`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3591-L3625)
- [`consensus/state_processing/src/common/get_payload_attesting_indices.rs:30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/get_payload_attesting_indices.rs#L30)
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:41-90`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L41-L90)

**Skeptic check.** Verified that compute_ptc has no hot-path callers and that get_ptc indexes the stored window. compute_ptc_duties (beacon_chain.rs:1771) still scans the window per validator, which is O(N*slots*PTCSize), but it does not redo the selection, so the earlier verdict holds.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#10544](https://github.com/Consensys-Incorporated/teku/pull/10544)

</details>


<a id="state_transition-170"></a>
<details>
<summary><b>state_transition-170</b> Order operation validity checks cheapest first — <i>implemented · low · S · cpu</i></summary>

**Idea.** In request processing (for example consolidation requests), run the cheapest rejection checks before validator lookups and credential checks so invalid requests exit early.

**Impact.** Negligible: requests are few per block and the checks already run in spec order.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/process_operations.rs:1090-1160`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L1090-L1160)

**Skeptic check.** The source PR only reorders Lodestar's checks to match the spec (source!=target, queue full, churn, then source creds before target creds). Lighthouse process_consolidation_request has exactly that order.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#7576](https://github.com/ChainSafe/lodestar/pull/7576)

</details>


<a id="state_transition-171"></a>
<details>
<summary><b>state_transition-171</b> Compact participation flag arrays with index accessors — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** Expose epoch participation flags as compact byte arrays and read only the validator indices needed instead of materializing the whole participation list. This saves memory and copying.

**Impact.** Participation is a packed u8 milhouse List read by index. The op-pool reward cache uses BitVecs. No hot path materializes the whole list.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:585`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L585)
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:249`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L249)
- [`beacon_node/operation_pool/src/reward_cache.rs:22-24`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/reward_cache.rs#L22-L24)
- [`beacon_node/beacon_chain/src/attestation_rewards.rs:237-255`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_rewards.rs#L237-L255)

**Skeptic check.** The Lodestar PR changed a JS view API to return Uint8Array and added per-index getters. Lighthouse already gets this from milhouse's packed lists and index access. beacon_block_reward.rs:287 uses to_owned_list, which is a structural-sharing clone on an API path, not a flat copy.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#8963](https://github.com/ChainSafe/lodestar/pull/8963)

</details>


<a id="state_transition-172"></a>
<details>
<summary><b>state_transition-172</b> Make debug state and block dumps opt-in — <i>implemented · low · S · cpu, disk, latency</i></summary>

**Idea.** Do not serialize and write every post-state and block to disk in the state transition path unless a debug flag enables it. This removes a full SSZ serialization and file write per block.

**Impact.** The default build does no SSZ dumps.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:118`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L118)
- [`beacon_node/beacon_chain/src/block_verification.rs:2284-2310`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L2284-L2310)
- [`beacon_node/beacon_chain/Cargo.toml:13`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/Cargo.toml#L13)

**Skeptic check.** write_state and write_block return early unless the write_ssz_files compile feature is on. These are the only dump sites.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#3566](https://github.com/OffchainLabs/prysm/pull/3566)

</details>


<a id="state_transition-173"></a>
<details>
<summary><b>state_transition-173</b> Remove spec-dropped vectors from beacon state — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Drop state fields that the spec no longer uses (such as active index roots and compact committee roots), so the state is smaller and no per-epoch work computes or hashes them.

**Impact.** The state has no obsolete vectors to hash.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:516-563`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L516-L563)

**Skeptic check.** A grep finds no active_index_roots or compact_committees_root in consensus/. The state struct follows the current spec only.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#3869](https://github.com/OffchainLabs/prysm/pull/3869)

</details>


<a id="state_transition-174"></a>
<details>
<summary><b>state_transition-174</b> Hold state as persistent tree throughout the node — <i>implemented · high · L · cpu, memory</i></summary>

**Idea.** Keep the beacon state as a persistent tree-backed structure everywhere instead of converting between flat objects and trees, so copies share structure and hashing is incremental.

**Impact.** State clones share structure, and hashing is incremental through milhouse.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:516`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L516)
- [`consensus/types/src/state/beacon_state.rs:3070-3077`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3070-L3077)
- Cargo.toml:299

**Skeptic check.** BeaconState fields are milhouse List/Vector. update_tree_hash_cache only applies pending mutations and hashes the trees. There is no flat-to-tree conversion in the state transition.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#1104](https://github.com/ChainSafe/lodestar/pull/1104)

</details>


