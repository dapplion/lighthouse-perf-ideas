# fork_choice

63 ideas: 5 not, 9 partial, 41 implemented, 8 n/a; 6 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

Ids missing from the sequence are ideas that have not been checked against Lighthouse yet.

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [fork_choice-001](#fork_choice-001) | Init and update fork choice from cached epoch data | implemented | medium |  | startup, cpu |
| [fork_choice-002](#fork_choice-002) | O(1) finalized-descendant check via stored checkpoints | implemented | low |  | cpu, latency |
| [fork_choice-004](#fork_choice-004) | Cache block ancestor at slot for vote counting | n/a | low |  | cpu |
| [fork_choice-006](#fork_choice-006) **★** | Answer ancestor/canonical queries from in-memory fork choice | partial | medium | S | cpu, disk, latency |
| [fork_choice-007](#fork_choice-007) | Dense per-validator array of compact vote records | implemented | low |  | cpu, memory |
| [fork_choice-010](#fork_choice-010) | Single non-throwing lookup for proto-array root-to-index | implemented | low |  | cpu |
| [fork_choice-012](#fork_choice-012) | No cache rebuild on cloned head state per update | implemented | medium |  | cpu, latency |
| [fork_choice-013](#fork_choice-013) | Slot-ordered queued attestations with bulk drain | implemented | low |  | cpu, memory |
| [fork_choice-014](#fork_choice-014) | Cache head in fork choice; serve duties from it | implemented | low | S | cpu, latency |
| [fork_choice-020](#fork_choice-020) | Batch attestations into fork choice, recompute head periodically | implemented | medium | S | cpu, latency |
| [fork_choice-022](#fork_choice-022) | Reweight votes at justification from epoch-processing data | n/a | low |  | cpu, memory |
| [fork_choice-025](#fork_choice-025) | Stop ancestor walks early, at finalized slot | implemented | low |  | cpu, memory, latency |
| [fork_choice-026](#fork_choice-026) | Bound the invalid-block set by slot | n/a | medium |  | memory |
| [fork_choice-027](#fork_choice-027) | Bound fork choice initialization replay horizon | implemented | medium |  | startup, cpu |
| [fork_choice-028](#fork_choice-028) | Keep only unfinalized blocks in in-memory block graph | implemented | medium |  | memory, startup |
| [fork_choice-031](#fork_choice-031) **★** | Cache per-node head viability in proto-array | partial | medium | M | cpu |
| [fork_choice-032](#fork_choice-032) | Compute justified balances once per justification change | implemented | low |  | cpu, memory |
| [fork_choice-036](#fork_choice-036) | Proto-array with best-descendant pointers and vote deltas | implemented | low | S | cpu, memory, latency |
| [fork_choice-037](#fork_choice-037) | Optimised LMD-GHOST with ancestor helpers and per-child weights | implemented | low | S | cpu |
| [fork_choice-038](#fork_choice-038) **★** | Cached pulled-up state and parallel vote scan | partial | medium | M | cpu, latency |
| [fork_choice-039](#fork_choice-039) | Precomputed validator-to-slot table per shuffling seed | partial | low | M | cpu, memory |
| [fork_choice-041](#fork_choice-041) | Cheap proto-array pruning on every finalization | implemented | low | S | cpu, memory |
| [fork_choice-044](#fork_choice-044) | Justified balances from caches built at import/epoch processing | implemented | low | S | cpu, memory, disk, latency |
| [fork_choice-045](#fork_choice-045) | Store block metadata and execution status in fork choice nodes | implemented | low | S | cpu, memory, disk, latency |
| [fork_choice-047](#fork_choice-047) | Build children index once per head walk, iterate filter | implemented | low | S | cpu |
| [fork_choice-051](#fork_choice-051) | Dedupe fork-choice attestations by bitfield overlap | implemented | medium | S | cpu |
| [fork_choice-054](#fork_choice-054) | Incremental vote weight tally across get_head calls | partial | low | M | cpu, latency |
| [fork_choice-060](#fork_choice-060) | Skip finalized-descent walk for canonical targets | n/a | low | S | cpu |
| [fork_choice-063](#fork_choice-063) | Grow per-validator vote tables without doubling | not | low | S | memory |
| [fork_choice-064](#fork_choice-064) | Consolidate fork choice locks into one external lock | partial | low | M | cpu, latency |
| [fork_choice-065](#fork_choice-065) | Load/advance states before taking fork-choice lock | partial | low | M | latency, cpu, sync |
| [fork_choice-071](#fork_choice-071) | Run fork choice right before block proposal | implemented | medium | S | latency |
| [fork_choice-074](#fork_choice-074) **★** | Run fork choice once per batch of imported children | partial | medium | M | cpu, sync |
| [fork_choice-077](#fork_choice-077) | Ignore pre-genesis ticks | implemented | low | S | cpu |
| [fork_choice-078](#fork_choice-078) | Head fast path for child-of-head blocks | not | low | M | cpu, latency |
| [fork_choice-079](#fork_choice-079) | Update head without waiting for EL forkchoiceUpdated | implemented | medium | S | latency |
| [fork_choice-080](#fork_choice-080) | Header presence check instead of state load under lock | n/a | low | S | disk, cpu, latency |
| [fork_choice-085](#fork_choice-085) | Votes store small node index or target id, not root | not | low | L | cpu, memory |
| [fork_choice-088](#fork_choice-088) | Proposer re-org of late weak heads with fcU override | implemented | low |  | latency |
| [fork_choice-091](#fork_choice-091) | Lightweight vote target record in LMD-GHOST | implemented | low |  | cpu |
| [fork_choice-092](#fork_choice-092) | No fork choice lock across validation and newPayload | implemented | medium | S | latency |
| [fork_choice-093](#fork_choice-093) | Split canonical and non-canonical nodes in one traversal | n/a | low |  | cpu |
| [fork_choice-097](#fork_choice-097) | Read locks for read-only fork choice paths | implemented | low |  | latency, cpu |
| [fork_choice-103](#fork_choice-103) | Keep updating head during sync so pruning proceeds | implemented | medium | S | memory, sync, cpu |
| [fork_choice-108](#fork_choice-108) | Persist fork choice snapshot for fast restart | implemented | medium | S | startup, disk |
| [fork_choice-109](#fork_choice-109) | Rebuild proto-array at startup from stored block metadata | implemented | medium | S | startup, disk |
| [fork_choice-110](#fork_choice-110) | Single ordered startup walk to init store and fork choice | n/a | medium | S | cpu, startup |
| [fork_choice-114](#fork_choice-114) | Prewarm next justified checkpoint balances | implemented | medium | S | latency, cpu |
| [fork_choice-118](#fork_choice-118) | Progressive balances cache for unrealized justification | implemented | low |  | cpu, latency |
| [fork_choice-120](#fork_choice-120) **★** | Prune branches incompatible with finalized checkpoint | partial | medium | M | cpu, memory |
| [fork_choice-122](#fork_choice-122) | Bound and prune delayed object queues | implemented | medium | S | memory |
| [fork_choice-123](#fork_choice-123) | Skip re-validating gossip-verified attestations in fork choice | implemented | medium | S | cpu |
| [fork_choice-124](#fork_choice-124) | Process block attestations into fork choice only once | implemented | medium | S | cpu |
| [fork_choice-125](#fork_choice-125) | Reuse indexed attestations from block import | implemented | medium | S | cpu |
| [fork_choice-132](#fork_choice-132) | Shrink persisted fork choice snapshot | implemented | medium |  | disk, memory, latency |
| [fork_choice-137](#fork_choice-137) | Skip new-head side effects when head unchanged | implemented | medium |  | cpu, latency, disk |
| [fork_choice-140](#fork_choice-140) | Drop block attestations with mismatched target ancestry | implemented | medium |  | cpu |
| [fork_choice-143](#fork_choice-143) **★** | Ignore old block attestations in fork choice | not | medium | S | cpu, sync |
| [fork_choice-145](#fork_choice-145) | Inherit unrealized checkpoints from parent when unchanged | implemented | medium | S | cpu |
| [fork_choice-146](#fork_choice-146) | Early return when no equivocators | implemented | low |  | cpu, latency |
| [fork_choice-149](#fork_choice-149) | Sorted cursor for equivocating indices in deltas | not | low | S | cpu |
| [fork_choice-150](#fork_choice-150) | Keep justified checkpoint cache updated during sync | n/a | medium |  | cpu, sync |
| [fork_choice-156](#fork_choice-156) | Update blob pruning metadata once per head change | implemented | medium |  | cpu, latency |

★ actionable. Click an id for the full record.

## Ideas

<a id="fork_choice-001"></a>
<details>
<summary><b>fork_choice-001</b> Init and update fork choice from cached epoch data — <i>implemented · medium · startup, cpu</i></summary>

**Idea.** On startup and fork choice rebuild, feed fork choice from cached per-epoch committee/attester data (epoch refs) instead of loading full beacon states to derive attesters. This avoids state loads and replays, which dominate during long non-finality.

**Best measured result.** "dramatically speeds up startup in long periods of non-finality" (commit:nimbus@c6674de5d2db)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:692`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L692) load_fork_choice reads persisted ForkChoice from DB, no state loads
- [`beacon_node/beacon_chain/src/builder.rs:245`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L245) restart path uses persisted fork choice
- [`consensus/proto_array/src/proto_array.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs):~230 rebuild_children_index only rebuilds a transient index

**Sources.** [nimbus@c6674de5d](https://github.com/status-im/nimbus-eth2/commit/c6674de5d2db), [nimbus#1421](https://github.com/status-im/nimbus-eth2/pull/1421), [nimbus#1521](https://github.com/status-im/nimbus-eth2/pull/1521)

</details>


<a id="fork_choice-002"></a>
<details>
<summary><b>fork_choice-002</b> O(1) finalized-descendant check via stored checkpoints — <i>implemented · low · cpu, latency</i></summary>

**Idea.** Decide whether a proto-array node descends from the finalized checkpoint (for head viability and block lookups) by comparing its stored justified/finalized/unrealized checkpoints or walking up from the node, instead of scanning all proto-array nodes. Removes O(n) work per node in head selection under non-finality.

**Gap in Lighthouse.** Under long non-finality the parent walk can still be O(depth) per viable-check when stored checkpoints differ, but it is bounded by the finalized slot, same as the cited clients.

**Best measured result.** Added perf test reproducing large updateHead time (600000 validators, 7200 blocks); no numbers stated (pr:lodestar#5867)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array.rs:2251`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L2251) is_finalized_checkpoint_or_descendant checks node finalized/justified/unrealized checkpoints first, then walks parents only down to the finalized slot
- [`consensus/proto_array/src/proto_array.rs:2135`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L2135) node_is_viable_for_head uses it per node, no full-array scan per node

**Sources.** [lodestar#5906](https://github.com/ChainSafe/lodestar/pull/5906), [lodestar#5867](https://github.com/ChainSafe/lodestar/pull/5867), [nimbus#4100](https://github.com/status-im/nimbus-eth2/pull/4100), [teku#7606](https://github.com/Consensys-Incorporated/teku/pull/7606)

</details>


<a id="fork_choice-004"></a>
<details>
<summary><b>fork_choice-004</b> Cache block ancestor at slot for vote counting — <i>n/a · low · cpu</i></summary>

**Idea.** Keep a cache (block root, slot) -&gt; ancestor root so many votes for the same block resolve their ancestor once instead of each walking the chain during LMD-GHOST vote counting.

**Impact.** Votes are applied as deltas and back-propagated child to parent in one reverse pass, so there is no per-vote ancestor lookup to cache.

**Best measured result.** significant improvements in fork choice (pr:prysm#2358)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array_fork_choice.rs:1387`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L1387) compute_deltas credits each vote to its node index, no ancestor walk
- [`consensus/proto_array/src/proto_array.rs:1829`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L1829) get_ancestor_node only for the single proposer-boost message

**Sources.** [prysm#2358](https://github.com/OffchainLabs/prysm/pull/2358), [prysm#2279](https://github.com/OffchainLabs/prysm/pull/2279), [prysm#2269](https://github.com/OffchainLabs/prysm/pull/2269)

</details>


<a id="fork_choice-006"></a>
<details>
<summary><b>fork_choice-006</b> Answer ancestor/canonical queries from in-memory fork choice — <i>partial · medium · S · cpu, disk, latency</i></summary>

**Idea.** Resolve ancestor-at-slot, common ancestor, canonical checks and block root/slot lookups from the in-memory fork choice DAG before touching the database or head state's historical roots. Avoids DB reads and state loads, which become a bottleneck in long non-finality.

**Gap in Lighthouse.** Sync (BlocksByRange, by-head ancestor walk) and fork-choice ancestry already use the in-memory proto-array. What is left: BeaconChain::block_root_at_slot (HTTP API block_id by slot and other callers) still falls back to forwards_iter_block_roots_until when the slot is older than the head state's 8192-slot block_roots window. In deep non-finality that loads hot states. Answer slots &gt;= finalized slot from block_roots_from_fork_choice / proto-array iter_block_roots(head) first.

**Impact.** Avoids hot-DB state loads for canonical-by-slot HTTP API lookups only in deep non-finality (&gt;8192 slots unfinalized); sync already avoids them. Negligible on a healthy mainnet node.

**Best measured result.** Before/after screenshots only; bottleneck at 200 epochs without finality (pr:prysm#6753)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1250`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1250) get_block_roots_for_slot_range: BlocksByRange roots above finalization come from fork choice (:1269, :1291)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:8427`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L8427) block_roots_from_fork_choice walks proto_array iter_block_roots(head) in memory
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:453`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L453) get_block_roots_ancestor_of_head: proto-array first, zero DB reads above finalization
- [`consensus/fork_choice/src/fork_choice.rs:509`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L509) get_ancestor via proto-array iter_block_roots
- [`consensus/proto_array/src/proto_array.rs:2208`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L2208) is_descendant / :2224 common_ancestor_slot in memory
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1050`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1050) block_root_at_slot_skips_none: head-state block_roots, then forwards_iter_block_roots_until (:819, hot DB / state loads)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1121`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1121) block_root_at_slot_skips_prev same fallback
- [`beacon_node/http_api/src/block_id.rs:79`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L79) HTTP slot block_id uses block_root_at_slot

**Second check.** The earlier review missed that BlocksByRange/by-head sync already serves post-finalization roots from fork choice (rpc_methods.rs:1250, beacon_chain.rs:8427), so the gap is smaller: only block_root_at_slot callers such as the HTTP API. Verdict stays partial.

**Sources.** [prysm#6753](https://github.com/OffchainLabs/prysm/pull/6753), [teku#5031](https://github.com/Consensys-Incorporated/teku/pull/5031), [lodestar#927](https://github.com/ChainSafe/lodestar/pull/927), [prysm#10512](https://github.com/OffchainLabs/prysm/pull/10512), [prysm#10516](https://github.com/OffchainLabs/prysm/pull/10516)

</details>


<a id="fork_choice-007"></a>
<details>
<summary><b>fork_choice-007</b> Dense per-validator array of compact vote records — <i>implemented · low · cpu, memory</i></summary>

**Idea.** Store each validator's latest vote as a compact plain record (or dense parallel arrays with sentinels) in a flat array indexed by validator index, instead of a hash map, interned dedup index, or boxed/SSZ-backed objects. This gives O(1) set/get, fewer allocations and faster delta computation under the fork choice lock.

**Impact.** Already O(1) get/set in a flat array of plain records; no hash map or boxed objects.

**Best measured result.** set with pinned messages 61,418 ns/op -&gt; 8.5 ns/op; ~1.66s lock hold per slot removed (pr:caplin#22352)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array_fork_choice.rs:27`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L27) VoteTracker plain struct
- [`consensus/proto_array/src/proto_array_fork_choice.rs:430`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L430),583 ElasticList&lt;VoteTracker&gt; flat Vec indexed by validator index

**Sources.** [teku#4316](https://github.com/Consensys-Incorporated/teku/pull/4316), [caplin#22352](https://github.com/erigontech/erigon/pull/22352), [teku#4254](https://github.com/Consensys-Incorporated/teku/pull/4254), [lodestar#8549](https://github.com/ChainSafe/lodestar/pull/8549)

</details>


<a id="fork_choice-010"></a>
<details>
<summary><b>fork_choice-010</b> Single non-throwing lookup for proto-array root-to-index — <i>implemented · low · cpu</i></summary>

**Idea.** Do proto-array root-to-index lookups with one map get returning a sentinel or default (e.g. -1/None), instead of contains followed by get, two sequential lookups, or an exception-raising lookup, so hits and misses are cheap.

**Impact.** Hot loop uses one HashMap get per lookup, returning Option; no contains+get or exceptions.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array_fork_choice.rs:1434`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L1434),1482,1501 single indices.get(..).copied() in compute_deltas
- [`consensus/proto_array/src/proto_array.rs:621`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L621) contains_key only in on_block insert path

**Sources.** [nimbus#8070](https://github.com/status-im/nimbus-eth2/pull/8070), [lodestar#9023](https://github.com/ChainSafe/lodestar/pull/9023), [teku#10448](https://github.com/Consensys-Incorporated/teku/pull/10448)

</details>


<a id="fork_choice-012"></a>
<details>
<summary><b>fork_choice-012</b> No cache rebuild on cloned head state per update — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** When the head state is cloned for a head change, do not rebuild pubkey/exit caches on each head update; keep or share caches so the ~70ms rebuild is not paid every time.

**Best measured result.** ~70ms+ penalty on mainnet (pr:lighthouse#3658)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:1150`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1150) build_all_caches on new head snapshot
- [`consensus/types/src/state/beacon_state.rs:2777`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2777) build_exit_cache only builds when check_initialized fails
- pubkey cache lives on BeaconChain, not in cloned state (builder.rs validator_pubkey_cache)

**Sources.** [lighthouse#3658](https://github.com/sigp/lighthouse/pull/3658)

</details>


<a id="fork_choice-013"></a>
<details>
<summary><b>fork_choice-013</b> Slot-ordered queued attestations with bulk drain — <i>implemented · low · cpu, memory</i></summary>

**Idea.** Keep fork choice's queued (future-slot) attestations ordered or bucketed by slot (e.g. BTreeMap by slot, sorted deque split with partition_point), so dequeuing due votes splits off a prefix in bulk instead of iterating, copying or reallocating the whole queue on every attestation or tick. Removes quadratic CPU when many attestations are gossiped.

**Impact.** Queue is slot-bucketed with bulk prefix split; the quadratic case is gone (PR 9524 measured 61.9ms to 5.17ms at 93750 entries).

**Best measured result.** None (pr:lighthouse#9524)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fork_choice/src/fork_choice.rs:371`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L371) queued_attestations BTreeMap&lt;Slot,Vec&gt;
- [`consensus/fork_choice/src/fork_choice.rs:311-316`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L311-L316) dequeue_attestations uses split_off

**Sources.** [nimbus#5288](https://github.com/status-im/nimbus-eth2/pull/5288), [nimbus#1805](https://github.com/status-im/nimbus-eth2/pull/1805), [lodestar#7142](https://github.com/ChainSafe/lodestar/pull/7142), [lighthouse#8378](https://github.com/sigp/lighthouse/pull/8378), [lighthouse#9524](https://github.com/sigp/lighthouse/pull/9524)

</details>


<a id="fork_choice-014"></a>
<details>
<summary><b>fork_choice-014</b> Cache head in fork choice; serve duties from it — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Cache the computed head node (with its payload status) inside fork choice and recompute deltas/scores only at explicit points or when votes or balances changed since the last get_head. Validator duties (attesters, proposers) and block production read the cached head instead of re-running head selection.

**Gap in Lighthouse.** Minor: proto_array find_head (proto_array_fork_choice.rs:788) still runs compute_deltas over all validators on every get_head, with no skip when votes and balances are unchanged. Adding a dirty flag in ProtoArrayForkChoice::find_head would skip it.

**Impact.** Duties and block production already use the cached head. A dirty-flag skip would save one O(validators) vote scan per recompute_head (low value, order of ms).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:282`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L282) CachedHead
- [`consensus/../beacon_node/beacon_chain/src/beacon_chain.rs:4506`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/../beacon_node/beacon_chain/src/beacon_chain.rs#L4506),5401 duties and block production read canonical_head.cached_head()
- [`consensus/fork_choice/src/fork_choice.rs:568`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L568) get_head only called when head is recomputed

**Sources.** [nimbus#1907](https://github.com/status-im/nimbus-eth2/pull/1907), [lodestar#2696](https://github.com/ChainSafe/lodestar/pull/2696), [lodestar@9cebc9155](https://github.com/ChainSafe/lodestar/commit/9cebc9155d6e), [prysm#16419](https://github.com/OffchainLabs/prysm/pull/16419)

</details>


<a id="fork_choice-020"></a>
<details>
<summary><b>fork_choice-020</b> Batch attestations into fork choice, recompute head periodically — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Collect verified attestations and apply them to fork choice in one batch call (grouped by target, tracking dirty validators), and recompute the head on a timer such as once per slot, instead of one call per attestation that each propagates deltas or recomputes head.

**Gap in Lighthouse.** Minor: compute_deltas scans every validator vote rather than a dirty set, which is O(validators) per get_head.

**Impact.** Already batched; a dirty-set would save at most a ~1M-element scan per head update.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fork_choice/src/fork_choice.rs:1325`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1325) on_attestation only sets votes (process_attestation) or queues by slot
- [`consensus/proto_array/src/proto_array_fork_choice.rs:693`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L693) process_attestation updates VoteTracker next_root only
- [`consensus/proto_array/src/proto_array_fork_choice.rs:1387`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L1387) compute_deltas applies all votes in one pass per get_head
- [`consensus/fork_choice/src/fork_choice.rs:1580`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1580) process_attestation_queue drains queue once per update_time
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7496`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7496) per_slot_task recomputes head once per slot (plus after block import)

**Sources.** [grandine@713420c47](https://github.com/grandinetech/grandine/commit/713420c47a6a), [silver#294](https://github.com/gattaca-com/silver/pull/294), [prysm#4802](https://github.com/OffchainLabs/prysm/pull/4802), [prysm#8381](https://github.com/OffchainLabs/prysm/pull/8381)

</details>


<a id="fork_choice-022"></a>
<details>
<summary><b>fork_choice-022</b> Reweight votes at justification from epoch-processing data — <i>n/a · low · cpu, memory</i></summary>

**Idea.** When the justified checkpoint changes, reweight all fork-choice votes in one pass using balances and attester data already computed during epoch processing, instead of attaching weights per attestation; also stream blocks during archival.

**Impact.** Lighthouse does not attach weights per attestation; weights come from the per-validator vote array and justified balances in one delta pass per get_head, so there is nothing to batch at justification.

**Best measured result.** States attestation reweighting "is fast, lots of the work was already done as part of epoch processing"; no numbers (pr:lodestar#1540)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array_fork_choice.rs:788`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L788) find_head recomputes deltas from vote array and justified balances
- [`consensus/fork_choice/src/fork_choice.rs:1107`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1107) update_checkpoints

**Sources.** [lodestar#1517](https://github.com/ChainSafe/lodestar/pull/1517), [lodestar#1540](https://github.com/ChainSafe/lodestar/pull/1540)

</details>


<a id="fork_choice-025"></a>
<details>
<summary><b>fork_choice-025</b> Stop ancestor walks early, at finalized slot — <i>implemented · low · cpu, memory, latency</i></summary>

**Idea.** Iterate fork choice ancestors lazily newest-first and stop at the finalized root/slot, the window start, or the minimum needed (reorg distance, payload counts), instead of collecting or walking the whole chain back to genesis/anchor. Makes queries O(window) rather than O(chain).

**Impact.** Ancestor queries are lazy and stop at the target or finalized slot, so cost is O(window), including under non-finality.

**Best measured result.** Win only under prolonged non-finality (pr:lodestar#9824)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array.rs:2177`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L2177) iter_nodes lazy newest-first iterator
- [`consensus/proto_array/src/proto_array.rs:2208`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L2208) is_descendant take_while slot &gt;= ancestor
- [`consensus/proto_array/src/proto_array.rs:2251`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L2251) is_finalized_checkpoint_or_descendant bounded by finalized slot
- [`consensus/proto_array/src/proto_array.rs:1852`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L1852) get_ancestor_node stops at target slot

**Sources.** [lighthouse@e9e912323](https://github.com/sigp/lighthouse/commit/e9e912323e7a), [lodestar#9824](https://github.com/ChainSafe/lodestar/pull/9824), [lodestar#3125](https://github.com/ChainSafe/lodestar/pull/3125), [prysm#4761](https://github.com/OffchainLabs/prysm/pull/4761)

</details>


<a id="fork_choice-026"></a>
<details>
<summary><b>fork_choice-026</b> Bound the invalid-block set by slot — <i>n/a · medium · memory</i></summary>

**Idea.** Prune the invalid/bad-block root set by slot (or bound its size) so a peer cannot grow it without limit by sending many distinct invalid blocks.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/chain_config.rs:108`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/chain_config.rs#L108) invalid_block_roots is a fixed CLI/config set, not peer-fed
- [`consensus/fork_choice/src/fork_choice.rs:240`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L240) invalid blocks are never added to fork choice
- [`beacon_node/network/src/sync/range_sync/range.rs:77`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/range.rs#L77) failed_chains is an LRUTimeCache (time bounded)

**Sources.** [caplin#23830](https://github.com/erigontech/erigon/pull/23830)

</details>


<a id="fork_choice-027"></a>
<details>
<summary><b>fork_choice-027</b> Bound fork choice initialization replay horizon — <i>implemented · medium · startup, cpu</i></summary>

**Idea.** On startup, limit how many unfinalized blocks are replayed into fork choice so long non-finalizing periods do not cause a full replay of every unfinalized block.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/builder.rs:245`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L245) loads persisted proto-array, no replay of unfinalized blocks
- [`beacon_node/beacon_chain/src/beacon_chain.rs:692`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L692) load_fork_choice

**Sources.** [nimbus#1904](https://github.com/status-im/nimbus-eth2/pull/1904), [nimbus#1910](https://github.com/status-im/nimbus-eth2/pull/1910)

</details>


<a id="fork_choice-028"></a>
<details>
<summary><b>fork_choice-028</b> Keep only unfinalized blocks in in-memory block graph — <i>implemented · medium · memory, startup</i></summary>

**Idea.** Keep the in-memory by-root block index/graph only for the non-finalized portion and serve finalized blocks from an on-disk slot index, so memory does not grow with chain length and startup need not load the finalized index.

**Best measured result.** None (pr:nimbus#3513)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array.rs:2073`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L2073) maybe_prune drops finalized nodes from nodes/indices/children
- [`consensus/fork_choice/src/fork_choice.rs:509`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L509) get_ancestor works on unfinalized DAG only
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1050`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1050) finalized slot lookups go via forwards iterator on freezer DB

**Sources.** [nimbus#3293](https://github.com/status-im/nimbus-eth2/pull/3293), [nimbus#3513](https://github.com/status-im/nimbus-eth2/pull/3513)

</details>


<a id="fork_choice-031"></a>
<details>
<summary><b>fork_choice-031</b> Cache per-node head viability in proto-array — <i>partial · medium · M · cpu</i></summary>

**Idea.** Cache each proto-array node's viability-for-head result and invalidate on checkpoint change, since during long non-finality the viability check repeatedly walks the unfinalized chain.

**Gap in Lighthouse.** The costly part of the Nimbus problem (each leaf walking the unfinalized chain to prove it descends from finality) is already short-circuited in O(1) when the leaf's own checkpoint fields match the store's finalized checkpoint, which is the normal case in non-finality. Not done: viability is not cached between get_head calls. Each call rebuilds the filtered node tree in O(nodes since justified), with HashSet and Vec allocations. A cache keyed on (current_epoch, justified, finalized) and invalidated on on_block or an execution-status change would remove that rebuild.

**Impact.** Small on healthy mainnet. In long non-finality it removes an O(N) linear pass with allocations per head update. The ancestor walks per leaf that Nimbus fixed are already mostly avoided.

**Best measured result.** significant time during non-finality; no numbers (pr:nimbus#6076)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array.rs:2251`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L2251) is_finalized_checkpoint_or_descendant: O(1) fast path compares the node's own finalized/justified (:2279) and unrealized (:2285) checkpoints before walking ancestors
- [`consensus/proto_array/src/proto_array.rs:2135`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L2135) node_is_viable_for_head: called only for leaves (:1413-1416), uses that fast path
- [`consensus/proto_array/src/proto_array.rs:1448`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L1448) find_head_walk rebuilds get_filtered_node_tree (:1304) on every call
- [`consensus/proto_array/src/proto_array.rs:1336`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L1336) filter_node_tree: reverse single pass over all nodes from justified index, allocates invalid_payloads HashSet, excluded vec and per-node child vecs each call

**Second check.** The earlier review said the leaf finalized-descendant check walks ancestors. But is_finalized_checkpoint_or_descendant returns at once when the node's own finalized/justified/unrealized checkpoint equals the store finalized checkpoint. That is the main cost Nimbus #6076 cached. The rebuild of the full filtered tree on each call is still uncached, so the verdict is partial, not implemented.

**Sources.** [nimbus#6076](https://github.com/status-im/nimbus-eth2/pull/6076)

</details>


<a id="fork_choice-032"></a>
<details>
<summary><b>fork_choice-032</b> Compute justified balances once per justification change — <i>implemented · low · cpu, memory</i></summary>

**Idea.** Have fork choice hold a small snapshot of justified-checkpoint effective balances (zero for inactive/slashed) plus total, fetched lazily only when the justified checkpoint changes, instead of passing or looking up balances (or caching large epoch results) on every head update or vote.

**Impact.** Balances are computed once per justified checkpoint change and reused for every get_head.

**Best measured result.** get_head regression 126 ms to 198 ms p50 cited as motivation; no after-number stated (pr:ethlambda#649)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/justified_balances.rs:7`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/justified_balances.rs#L7) JustifiedBalances snapshot (effective balances zero for inactive/slashed, plus total)
- [`beacon_node/beacon_chain/src/beacon_fork_choice_store.rs:341-366`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_fork_choice_store.rs#L341-L366) set_justified_checkpoint refreshes via balances_cache or state load only on justified change
- [`consensus/proto_array/src/proto_array_fork_choice.rs:802`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L802) old balances replaced only if changed

**Sources.** [lodestar#1702](https://github.com/ChainSafe/lodestar/pull/1702), [prysm#11964](https://github.com/OffchainLabs/prysm/pull/11964), [ethlambda#649](https://github.com/lambdaclass/ethlambda/pull/649), [nimbus#139](https://github.com/status-im/nimbus-eth2/pull/139)

</details>


<a id="fork_choice-036"></a>
<details>
<summary><b>fork_choice-036</b> Proto-array with best-descendant pointers and vote deltas — <i>implemented · low · S · cpu, memory, latency</i></summary>

**Idea.** Represent the non-finalized block tree as a flat array of nodes with parent, weight, best-child and best-descendant fields, apply only per-validator vote deltas in one backward pass that propagates weight to parents and updates best pointers. get_head is then a lookup of the justified node's best descendant instead of recomputing LMD-GHOST over the whole tree and all validators.

**Impact.** Already done; head selection never re-sums votes over the tree.

**Best measured result.** None (pr:prysm#4649)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array.rs:476`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L476) apply_score_changes: one backward pass applying deltas and back-propagating to parents
- [`consensus/proto_array/src/proto_array_fork_choice.rs:1387`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L1387) compute_deltas: per-validator vote deltas
- [`consensus/proto_array/src/proto_array.rs:119`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L119) best_descendant (V17 node); V29 head walk uses find_head_walk with cached weights at :1448

**Sources.** [prysm#4643](https://github.com/OffchainLabs/prysm/pull/4643), [lodestar@4512c6320](https://github.com/ChainSafe/lodestar/commit/4512c6320e73), [lodestar@765aeaf53](https://github.com/ChainSafe/lodestar/commit/765aeaf53f59), [lighthouse#804](https://github.com/sigp/lighthouse/pull/804), [lodestar#898](https://github.com/ChainSafe/lodestar/pull/898), [nimbus#865](https://github.com/status-im/nimbus-eth2/pull/865), [prysm#4559](https://github.com/OffchainLabs/prysm/pull/4559), [prysm#4778](https://github.com/OffchainLabs/prysm/pull/4778), [prysm#4649](https://github.com/OffchainLabs/prysm/pull/4649), [lodestar@f5c8accd7](https://github.com/ChainSafe/lodestar/commit/f5c8accd7cc0), [teku#1170](https://github.com/Consensys-Incorporated/teku/pull/1170), [ethlambda#235](https://github.com/lambdaclass/ethlambda/pull/235), [nimbus#965](https://github.com/status-im/nimbus-eth2/pull/965), [lodestar#165](https://github.com/ChainSafe/lodestar/pull/165)

</details>


<a id="fork_choice-037"></a>
<details>
<summary><b>fork_choice-037</b> Optimised LMD-GHOST with ancestor helpers and per-child weights — <i>implemented · low · S · cpu</i></summary>

**Idea.** Replace naive LMD-GHOST, which walks the tree per vote and per child, with an optimised implementation behind a fork choice trait that uses precomputed ancestor-at-height lookups and per-child vote weights, so head selection does not rescan the whole block tree per vote.

**Impact.** Superseded by proto-array; the naive per-vote tree walks no longer exist.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array.rs:456`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L456) ProtoArray replaced the old LMD-GHOST implementations
- [`consensus/proto_array/src/proto_array.rs:1255`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L1255) find_head

**Sources.** [lighthouse#297](https://github.com/sigp/lighthouse/pull/297), [lighthouse@2b7aa269c](https://github.com/sigp/lighthouse/commit/2b7aa269c301), [lighthouse@8baae0e02](https://github.com/sigp/lighthouse/commit/8baae0e02ee7), [lighthouse@405b3ff6c](https://github.com/sigp/lighthouse/commit/405b3ff6c184), [lighthouse@472370709](https://github.com/sigp/lighthouse/commit/4723707097d4), [lighthouse#195](https://github.com/sigp/lighthouse/pull/195), [lighthouse@5b425c9bf](https://github.com/sigp/lighthouse/commit/5b425c9bf3f4)

</details>


<a id="fork_choice-038"></a>
<details>
<summary><b>fork_choice-038</b> Cached pulled-up state and parallel vote scan — <i>partial · medium · M · cpu, latency</i></summary>

**Idea.** For per-slot fork-choice work, fetch the pulled-up head state from the checkpoint-state cache instead of replaying the epoch transition, read a flat balances list, dedupe latest messages, scan votes in parallel chunks, and prefetch next epoch's balance-source state on the last slot.

**Gap in Lighthouse.** Everything except the parallel vote scan has an equivalent: pull-up comes from per-node unrealized checkpoints computed at import, balances are a flat cached list filled at epoch-boundary block import, votes are one-per-validator. Remaining gap: compute_deltas scans ~1M VoteTrackers on one thread; a chunked rayon scan with per-chunk delta vectors merged at the end would cut that.

**Impact.** A few ms of fork-choice write-lock time per get_head on mainnet; most of Teku's win (cached pulled-up state, balance prefetch) is already in Lighthouse.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fork_choice/src/fork_choice.rs:943`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L943) unrealized justification/finalization computed once at on_block from the post-state via progressive balances cache (or inherited from parent), stored per proto node; no epoch replay for pull-up
- [`beacon_node/beacon_chain/src/beacon_fork_choice_store.rs:260`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_fork_choice_store.rs#L260) on_verified_block populates balances_cache with flat JustifiedBalances for every epoch-boundary block (functions as the balance-source prefetch)
- [`beacon_node/beacon_chain/src/beacon_fork_choice_store.rs:349`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_fork_choice_store.rs#L349) set_justified_checkpoint reads cached balances, no state load on hit
- [`consensus/proto_array/src/proto_array_fork_choice.rs:693`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L693) latest messages are one VoteTracker per validator (deduped by construction)
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:125`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L125) head state advanced (incl. epoch transition) at 3/4 of the prior slot
- [`consensus/proto_array/src/proto_array_fork_choice.rs:1387`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L1387) compute_deltas is a sequential loop over all votes; no rayon in proto_array/fork_choice

**Second check.** Beyond the earlier review I checked the on_block unrealized-checkpoint path, the on_verified_block epoch-boundary balance caching and the state-advance timer; these cover the cached-state and prefetch parts, and grep found no parallelism in proto_array or fork_choice.

**Sources.** [teku#11214](https://github.com/Consensys-Incorporated/teku/pull/11214)

</details>


<a id="fork_choice-039"></a>
<details>
<summary><b>fork_choice-039</b> Precomputed validator-to-slot table per shuffling seed — <i>partial · low · M · cpu, memory</i></summary>

**Idea.** Precompute, per attester-shuffling seed for recent epochs, a table mapping validator index to slot offset with size hints, so building fast-confirmation support maps avoids random balance access and repeated appends under the fork-choice lock.

**Gap in Lighthouse.** Lighthouse has an O(1) lookup via shuffled_position but does arithmetic with 3 safe_div per validator per call and no flat table. Build a Vec&lt;u8&gt; slot_offset per AttestationShufflingId (pre-sized to active count) in SlotAssignment::new and make get_node_support_between_slots / is_in_range index it; ideally aggregate once per slot range.

**Impact.** Cuts the O(V) support scans inside the fork choice lock in on_fast_confirmation; with ~1M validators this is likely several times cheaper per scan (Prysm saw 8.9x), a few tens of ms per slot at most.

**Best measured result.** 1M validators: 106.2ms-&gt;11.95ms (8.9x), 62.6MB/2697 allocs -&gt; 10.4KB/9 (pr:prysm#17179)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fast_confirmation/src/slot_assignments.rs:149`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fast_confirmation/src/slot_assignments.rs#L149) SlotAssignments::is_in_range resolves a validator's slot on demand from CommitteeCache::shuffled_position, with 3 cached caches reused across head changes
- [`consensus/fast_confirmation/src/lib.rs:848`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fast_confirmation/src/lib.rs#L848) get_node_support_between_slots loops over all active validators and calls is_in_range each
- [`consensus/fast_confirmation/src/optimizations.rs:252`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fast_confirmation/src/optimizations.rs#L252) precompute_chain_attestation_scores batches scores, but it does not use slot assignments
- [`beacon_node/beacon_chain/src/canonical_head.rs:1376`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1376) on_fast_confirmation runs with proto_array and votes borrowed (fork choice lock held)

**Sources.** [prysm#17179](https://github.com/OffchainLabs/prysm/pull/17179)

</details>


<a id="fork_choice-041"></a>
<details>
<summary><b>fork_choice-041</b> Cheap proto-array pruning on every finalization — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Make proto-array pruning cheap (no table rebuilds) and prune nodes before the finalized block whenever finality advances, including during range sync and on slot ticks, instead of waiting for a large threshold. The tree stays small, head computation traverses fewer nodes and memory does not leak.

**Gap in Lighthouse.** Minor: pruning is not triggered on slot ticks or range sync steps, only when finalization migrates, and only when the finalized index is at least 256.

**Impact.** Already done; tree stays near the unfinalized size, so no meaningful extra saving.

**Best measured result.** None (pr:lighthouse#3408)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:1738`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1738) fork_choice_write_lock().prune() on every finalization
- [`consensus/fork_choice/src/fork_choice.rs:1957`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1957) prune -&gt; maybe_prune
- [`consensus/proto_array/src/proto_array_fork_choice.rs:24`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L24) DEFAULT_PRUNE_THRESHOLD = 256 nodes
- [`consensus/proto_array/src/proto_array.rs:2073`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L2073) maybe_prune: split_off plus index shift, no table rebuild

**Sources.** [nimbus#1535](https://github.com/status-im/nimbus-eth2/pull/1535), [lighthouse#3408](https://github.com/sigp/lighthouse/pull/3408), [prysm#4642](https://github.com/OffchainLabs/prysm/pull/4642), [prysm#11387](https://github.com/OffchainLabs/prysm/pull/11387), [prysm#10768](https://github.com/OffchainLabs/prysm/pull/10768)

</details>


<a id="fork_choice-044"></a>
<details>
<summary><b>fork_choice-044</b> Justified balances from caches built at import/epoch processing — <i>implemented · low · S · cpu, memory, disk, latency</i></summary>

**Idea.** Build the effective-balances snapshot for each epoch-boundary checkpoint from a state already in hand (block import or the per-epoch transition cache), cache it keyed by (boundary root, epoch), and hand the same immutable list to fork choice. A justified checkpoint switch is then a lookup instead of regenerating, rewinding or decoding a checkpoint state and copying a full balance list.

**Gap in Lighthouse.** Minor: cache hits clone the whole Vec&lt;u64&gt; (JustifiedBalances is not Arc) and the cache holds only 4 entries.

**Impact.** Already done; justified switches are a cache lookup plus a clone in the common case.

**Best measured result.** Head recompute at epoch-start tick took 0.5-4 s (Hoodi 8 times, up to 2.3 s queue wait); snapshot build ~25 ms per checkpoint (pr:ethlambda#665)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_fork_choice_store.rs:260`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_fork_choice_store.rs#L260) on_verified_block inserts epoch-boundary balances into BalancesCache from the import state
- [`beacon_node/beacon_chain/src/beacon_fork_choice_store.rs:98`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_fork_choice_store.rs#L98) BalancesCache keyed by (block_root, epoch)
- [`beacon_node/beacon_chain/src/beacon_fork_choice_store.rs:349`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_fork_choice_store.rs#L349) set_justified_checkpoint uses the cache and falls back to loading the state on a miss

**Sources.** [lodestar#4290](https://github.com/ChainSafe/lodestar/pull/4290), [lighthouse#2849](https://github.com/sigp/lighthouse/pull/2849), [ethlambda#665](https://github.com/lambdaclass/ethlambda/pull/665), [nimbus#1489](https://github.com/status-im/nimbus-eth2/pull/1489), [teku#3685](https://github.com/Consensys-Incorporated/teku/pull/3685)

</details>


<a id="fork_choice-045"></a>
<details>
<summary><b>fork_choice-045</b> Store block metadata and execution status in fork choice nodes — <i>implemented · low · S · cpu, memory, disk, latency</i></summary>

**Idea.** Store per-block metadata (state root, execution block hash, optimistic/execution status, justified/finalized checkpoints, dependent roots) directly on fork choice nodes. API duties, execution checks, invalidation and head events then read it from the node instead of separate hash maps or loading blocks or states from disk.

**Impact.** Already done; avoids block/state loads for duties and execution checks.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array.rs:78`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L78) ProtoNode stores state_root, target_root, justified/finalized checkpoints, execution_status, shuffling ids
- [`consensus/proto_array/src/proto_array_fork_choice.rs:309`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L309) Block carries the same metadata
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1741`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1741) duties and execution status read from fork choice node

**Sources.** [nimbus#1014](https://github.com/status-im/nimbus-eth2/pull/1014), [lighthouse#2643](https://github.com/sigp/lighthouse/pull/2643), [prysm#15137](https://github.com/OffchainLabs/prysm/pull/15137), [lodestar@9865e62bb](https://github.com/ChainSafe/lodestar/commit/9865e62bb7ac), [nimbus#4969](https://github.com/status-im/nimbus-eth2/pull/4969), [prysm#10400](https://github.com/OffchainLabs/prysm/pull/10400)

</details>


<a id="fork_choice-047"></a>
<details>
<summary><b>fork_choice-047</b> Build children index once per head walk, iterate filter — <i>implemented · low · S · cpu</i></summary>

**Idea.** In find_head, build the parent-to-children index once per call and run the viability filter pass iteratively in reverse node order, instead of scanning the whole block index at every visited node or recursing. This turns the walk from quadratic to linear in unfinalized blocks.

**Gap in Lighthouse.** Residual O(N) per head: filter_node_tree rebuilds the invalid_payloads set and the excluded vec each call, and the viable HashSet is rebuilt; could be cached when nothing changed.

**Impact.** Already linear in unfinalized nodes; any further saving is small.

**Best measured result.** Unchanged in 130 of 131 calls; fork choice time in block import 31.58 ms to 15.00 ms (~53%) (pr:lighthouse#10023)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array.rs:458`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L458) cached children index, maintained in on_block (:772) and maybe_prune (:2101)
- [`consensus/proto_array/src/proto_array.rs:1320`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L1320) filter_node_tree: single reverse pass using the children index, no recursion
- [`consensus/proto_array/src/proto_array.rs:1448`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L1448) find_head_walk uses get_node_children from the cached index

**Sources.** [lighthouse#10023](https://github.com/sigp/lighthouse/pull/10023), [ethlambda#746](https://github.com/lambdaclass/ethlambda/pull/746)

</details>


<a id="fork_choice-051"></a>
<details>
<summary><b>fork_choice-051</b> Dedupe fork-choice attestations by bitfield overlap — <i>implemented · medium · S · cpu</i></summary>

**Idea.** Make the seen-attestation filter for fork choice aware of aggregation-bit overlap so attestations whose bits are a subset of already seen ones are not reprocessed.

**Impact.** None left to gain: in Lighthouse's latest-message design a subset attestation costs one integer compare per set bit, which is what a bit-overlap filter would cost anyway.

**Best measured result.** fork choice attestations 52/47/46 down to 15/29/14 (pr:prysm#4483)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array_fork_choice.rs:693`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L693) process_attestation is a per-validator O(1) slot compare; a re-seen or subset attestation leaves VoteTracker unchanged
- [`consensus/proto_array/src/proto_array_fork_choice.rs:1387`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L1387) compute_deltas only moves weight for votes whose root changed, so a repeated attestation adds no weight work
- [`consensus/fork_choice/src/fork_choice.rs:1361`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1361) on_attestation loops attesting indices into process_attestation; no per-attestation tree/weight update
- [`consensus/state_processing/src/consensus_context.rs:161`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/consensus_context.rs#L161) indexed attestations for block attestations are cached from block processing (keyed by tree hash root), so fork-choice import does not recompute committees
- [`beacon_node/beacon_chain/src/observed_aggregates.rs:127`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_aggregates.rs#L127) gossip aggregates that are a bit-subset of seen ones are dropped before fork choice
- [`beacon_node/beacon_chain/src/attestation_verification.rs:997`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L997) unaggregated gossip attestations deduped per validator/epoch by observed_gossip_attesters

**Second check.** The earlier review flagged block attestations as unfiltered. Reading ForkChoice::on_attestation and ProtoArray::process_attestation shows the latest-message tracker already makes reprocessing a no-op: per bit there is no weight or tree work, and compute_deltas skips unchanged votes. Prysm's PR fixed a heavier per-attestation path that Lighthouse does not have.

**Sources.** [prysm#4483](https://github.com/OffchainLabs/prysm/pull/4483)

</details>


<a id="fork_choice-054"></a>
<details>
<summary><b>fork_choice-054</b> Incremental vote weight tally across get_head calls — <i>partial · low · M · cpu, latency</i></summary>

**Idea.** Keep per-root vote weights across get_head calls and update only for validators whose latest message or equivocation status changed (dirty set), rebuilding only when justified balances change, instead of summing all latest messages each time.

**Gap in Lighthouse.** Weights are incremental, but the delta pass is a full O(V) scan of votes (plus a node_slots Vec rebuild) on every find_head. Keep a dirty-validator list set by process_attestation / equivocation / balance change, and iterate only it in compute_deltas, falling back to a full scan when justified balances change.

**Impact.** Cuts the O(V) vote scan (~1M entries) on each head recompute: roughly a few ms to tens of ms per find_head on mainnet, relevant for the time between block import and the forkchoiceUpdated call.

**Best measured result.** execution done to FCU p50 107 ms -&gt; 41 ms (pr:caplin#24985)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array_fork_choice.rs:1387`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L1387) compute_deltas scans every VoteTracker each find_head
- [`consensus/proto_array/src/proto_array_fork_choice.rs:1412`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L1412) loop checks current vs next for each validator, no dirty set
- [`consensus/proto_array/src/proto_array.rs:476`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L476) node weights persist across calls and only deltas are applied
- [`consensus/proto_array/src/proto_array_fork_choice.rs:802`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L802) old balances kept and compared

**Sources.** [caplin#21913](https://github.com/erigontech/erigon/pull/21913), [caplin#24985](https://github.com/erigontech/erigon/pull/24985)

</details>


<a id="fork_choice-060"></a>
<details>
<summary><b>fork_choice-060</b> Skip finalized-descent walk for canonical targets — <i>n/a · low · S · cpu</i></summary>

**Idea.** In finalized-consistency checks for attestation targets, return early if the target is on the canonical chain (which implies finalized descent), skipping ancestor walks.

**Gap in Lighthouse.** Lighthouse validates attestation targets by comparing to the block's target_root (O(1)), so there is no per-attestation finalized-ancestor walk to skip.

**Impact.** Nothing on the gossip attestation path; negligible.

**Best measured result.** CPU flame graphs before and after, no numbers (pr:prysm#7628)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fork_choice/src/fork_choice.rs:1165`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1165) validate_on_attestation checks target via block.target_root equality, no finalized-descent walk
- [`consensus/proto_array/src/proto_array.rs:2251`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L2251) is_finalized_checkpoint_or_descendant only used in supported_node (beacon_chain.rs:1939 duty path) and block import, with checkpoint-compare shortcuts at 2273-2288

**Sources.** [prysm#7628](https://github.com/OffchainLabs/prysm/pull/7628)

</details>


<a id="fork_choice-063"></a>
<details>
<summary><b>fork_choice-063</b> Grow per-validator vote tables without doubling — <i>not · low · S · memory</i></summary>

**Idea.** When the per-validator vote/latest-message tables grow for new validator indices, reslice within existing capacity or reserve the exact size plus fixed headroom, instead of reallocating and doubling. Avoids allocating twice the needed size at a capacity edge (~120 MB on mainnet).

**Gap in Lighthouse.** Change ElasticList::ensure (or process_attestation) to reserve_exact(i + 1 + fixed headroom) before resize_with, so the Vec never doubles at a capacity edge.

**Impact.** Avoids a transient ~2x allocation of the vote table (~100 MB at ~1.1M validators); mostly virtual, small RSS win.

**Best measured result.** Expected saving about 120 MB on mainnet follower (pr:ethlambda#740)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array_fork_choice.rs:430-445`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L430-L445) ElasticList::ensure uses Vec::resize_with(i+1), which grows by amortized doubling
- proto_array_fork_choice.rs:27 VoteTracker is ~90 bytes per validator

**Sources.** [ethlambda#740](https://github.com/lambdaclass/ethlambda/pull/740), [caplin#23731](https://github.com/erigontech/erigon/pull/23731)

</details>


<a id="fork_choice-064"></a>
<details>
<summary><b>fork_choice-064</b> Consolidate fork choice locks into one external lock — <i>partial · low · M · cpu, latency</i></summary>

**Idea.** Remove internal per-method fork choice locks (and separate fork choice and canonical head locks) and take one lock at the top-level import/accessor caller, so block import does not repeatedly acquire and release fine-grained locks and contend with other paths.

**Gap in Lighthouse.** Lighthouse already has a single external fork-choice lock (no per-method locks); the head cache lock is still separate and block import re-acquires the write lock 2-3 times (attestations, on_block, recompute_head). Merging those acquisitions would be the remaining change.

**Impact.** Marginal; fork-choice lock hold times are already instrumented and typically milliseconds.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:455-467`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L455-L467) one external RwLock around BeaconForkChoice, no internal locks in [`consensus/fork_choice/src/fork_choice.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs) or proto_array
- canonical_head.rs:458,463 fork_choice and cached_head remain two separate RwLocks
- block_verification.rs:1755 write lock for attestations, then again at on_block and recompute_head (canonical_head.rs:862)
- pr:lighthouse#3175 is CLOSED unmerged

**Sources.** [prysm#12036](https://github.com/OffchainLabs/prysm/pull/12036), [prysm#12014](https://github.com/OffchainLabs/prysm/pull/12014), [lighthouse#3175](https://github.com/sigp/lighthouse/pull/3175)

</details>


<a id="fork_choice-065"></a>
<details>
<summary><b>fork_choice-065</b> Load/advance states before taking fork-choice lock — <i>partial · low · M · latency, cpu, sync</i></summary>

**Idea.** Do expensive state work (decoding the justified state from disk, advancing states, building caches) before acquiring the fork-choice write lock, and avoid duplicate decodes, so the lock is not held for seconds.

**Gap in Lighthouse.** Balances cache mitigates most cases, but misses still decode a state while holding the fork-choice write lock. Prefetch justified/boundary balances into balances_cache before taking fork_choice_write_lock in block import (beacon_chain.rs import path / block_verification.rs:1755) and avoid the duplicate decodes in set_justified_checkpoint and on_verified_block.

**Impact.** Removes multi-hundred-ms to seconds lock holds only on cache-miss events (restart, long sync, deep reorgs); steady state unaffected.

**Best measured result.** Mainnet: ForkChoice in ~2.9s after fix; duplicate InitBeaconState doubled decode time (pr:caplin#21228)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_fork_choice_store.rs:349-366`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_fork_choice_store.rs#L349-L366) set_justified_checkpoint loads the justified state with get_hot_state on a balances-cache miss, under the write lock
- beacon_fork_choice_store.rs:260-300 on_verified_block loads epoch-boundary state under the lock when the boundary slot was skipped
- [`consensus/fork_choice/src/fork_choice.rs:1024`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1024) call site inside on_block
- canonical_head.rs:114 hold-time logging only; no update_head_slot_assignments exists (pr:lighthouse#9895 closed unmerged)

**Sources.** [caplin#21228](https://github.com/erigontech/erigon/pull/21228), [lighthouse#9895](https://github.com/sigp/lighthouse/pull/9895)

</details>


<a id="fork_choice-071"></a>
<details>
<summary><b>fork_choice-071</b> Run fork choice right before block proposal — <i>implemented · medium · S · latency</i></summary>

**Idea.** Run fork choice just before producing a block so the proposer builds on the latest head without proposal delay.

**Impact.** None needed.

**Best measured result.** no proposal delays seen on testnets (pr:teku#5964)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_production/mod.rs:130`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L130) wait_for_fork_choice_before_block_production
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7496`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7496) per-slot recompute_head then signals proposer via ForkChoiceSignalTx

**Sources.** [teku#5964](https://github.com/Consensys-Incorporated/teku/pull/5964)

</details>


<a id="fork_choice-074"></a>
<details>
<summary><b>fork_choice-074</b> Run fork choice once per batch of imported children — <i>partial · medium · M · cpu, sync</i></summary>

**Idea.** When importing a block unblocks pending children, process the whole chain and run fork choice once at the end instead of after each block.

**Gap in Lighthouse.** Lookup-resolved children and blocks released from the reprocess queue are each imported with their own recompute_head_at_current_slot; recompute_head has no coalescing or dirty-flag debounce. Fix: coalesce concurrent recompute requests in canonical_head (run once if a request is already pending), or batch child imports in the lookup path.

**Impact.** Minor: saves a get_head and possibly an EL fcU per extra child in multi-child import bursts.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:647`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L647) range/backfill chain segments recompute head once per batch
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:207`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L207) single RPC/lookup block import recomputes head per block
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1449`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1449) gossip block import recomputes head per block
- [`beacon_node/beacon_chain/src/canonical_head.rs:843`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L843) recompute_head_lock serializes calls but does not coalesce them; each caller runs get_head
- [`beacon_node/beacon_chain/src/canonical_head.rs:797`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L797) EL forkchoiceUpdated is skipped only when the head does not change

**Second check.** I checked every recompute_head_at_current_slot call site and canonical_head.rs for a coalescing or pending-request mechanism. There is only a serializing mutex, so the earlier partial verdict stands.

**Sources.** [prysm#2244](https://github.com/OffchainLabs/prysm/pull/2244)

</details>


<a id="fork_choice-077"></a>
<details>
<summary><b>fork_choice-077</b> Ignore pre-genesis ticks — <i>implemented · low · S · cpu</i></summary>

**Idea.** Guard the tick catch-up loop against times before genesis so unsigned wrap-around does not spin a core.

**Impact.** No pre-genesis spin possible.

**Best measured result.** about one CPU core kept busy (pr:caplin#24680)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fork_choice/src/fork_choice.rs:1502-1511`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1502-L1511) update_time loops only while store slot &lt; current_slot, incrementing by 1
- beacon_chain.rs:767 chain.slot() returns Err via slot_clock.now() -&gt; None before genesis
- [`consensus/fork_choice/src/fork_choice.rs:1523`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1523) on_tick rejects jumps &gt;1

**Sources.** [caplin#24680](https://github.com/erigontech/erigon/pull/24680)

</details>


<a id="fork_choice-078"></a>
<details>
<summary><b>fork_choice-078</b> Head fast path for child-of-head blocks — <i>not · low · M · cpu, latency</i></summary>

**Idea.** When an imported block is a direct child of the current head with a higher slot, use that relation to set or decide the new head cheaply instead of running full fork choice.

**Gap in Lighthouse.** Add a shortcut in recompute_head: if the imported block's parent is the current head and no vote deltas / proposer boost changes are pending, set head directly. Hard to make correct given proposer boost, payload status and pending vote deltas; the cheaper win is making compute_deltas cheaper.

**Impact.** Would skip an O(validators) compute_deltas plus a node-array pass per imported block (a few ms to tens of ms on mainnet), but correctness risk is high.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array_fork_choice.rs:769-815`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L769-L815) find_head always runs compute_deltas over all votes, apply_score_changes, then proto_array.find_head
- canonical_head.rs:862 recompute_head always calls get_head; no child-of-head shortcut found

**Sources.** [teku#2637](https://github.com/Consensys-Incorporated/teku/pull/2637), [prysm#2310](https://github.com/OffchainLabs/prysm/pull/2310), [prysm#10648](https://github.com/OffchainLabs/prysm/pull/10648)

</details>


<a id="fork_choice-079"></a>
<details>
<summary><b>fork_choice-079</b> Update head without waiting for EL forkchoiceUpdated — <i>implemented · medium · S · latency</i></summary>

**Idea.** Update the consensus head as soon as block verification finishes and send forkchoiceUpdated to the EL lazily (or fall back to local head selection at epoch boundaries), so attestation production does not wait on the EL.

**Impact.** None needed.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:1296`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1296) spawn_execution_layer_updates runs FCU in a separate task after cached head is updated
- [`beacon_node/beacon_chain/src/canonical_head.rs:1886`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1886) FCU task

**Sources.** [nimbus#7457](https://github.com/status-im/nimbus-eth2/pull/7457), [nimbus#5195](https://github.com/status-im/nimbus-eth2/pull/5195)

</details>


<a id="fork_choice-080"></a>
<details>
<summary><b>fork_choice-080</b> Header presence check instead of state load under lock — <i>n/a · low · S · disk, cpu, latency</i></summary>

**Idea.** In readiness checks under the fork-choice lock, test for header/block presence instead of loading (disk read and replay) a state that is then discarded.

**Gap in Lighthouse.** Lighthouse has no fork-choice readiness check that loads and discards a state; its under-lock state loads are consumed for balances.

**Impact.** Not applicable.

**Best measured result.** state load per retry 2 -&gt; 1; lock work reduced to two map lookups (pr:caplin#25098)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_fork_choice_store.rs:360`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_fork_choice_store.rs#L360) the only state loads under the lock use the state (balances), they are not discarded readiness checks
- [`consensus/fork_choice/src/fork_choice.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs) has no readiness check that loads a state

**Sources.** [caplin#25098](https://github.com/erigontech/erigon/pull/25098)

</details>


<a id="fork_choice-085"></a>
<details>
<summary><b>fork_choice-085</b> Votes store small node index or target id, not root — <i>not · low · L · cpu, memory</i></summary>

**Idea.** Store each validator's latest/applied vote as a small integer (proto-array node index or interned vote-target id) instead of an inline 32-byte block root, resolving the root once on arrival and remapping on prune. Delta computation then reads ~8 bytes per validator and needs no per-vote hash lookups.

**Gap in Lighthouse.** Replace current_root/next_root with node indices (or interned target ids) in VoteTracker, resolve the root once in process_attestation, remap on prune_ (ProtoArray::maybe_prune), and keep persistence (SSZ container) compatible via a schema migration. compute_deltas then indexes deltas directly.

**Impact.** compute_deltas runs on every head recompute over ~1.1M votes; saving the 2 hash lookups per vote and shrinking the table from ~90 to ~40 bytes per validator could make it ~2x faster and save ~50 MB.

**Best measured result.** None (pr:lodestar#5882)

**Evidence (Lighthouse @ 928b61e719).**

- proto_array_fork_choice.rs:27-34 VoteTracker stores current_root and next_root as Hash256 (plus slots and flags)
- proto_array_fork_choice.rs:1412-1500 compute_deltas does indices.get(&amp;root) HashMap lookups per vote, and also allocates node_slots Vec per find_head (line 777)

**Sources.** [silver#361](https://github.com/gattaca-com/silver/pull/361), [lodestar#5882](https://github.com/ChainSafe/lodestar/pull/5882)

</details>


<a id="fork_choice-088"></a>
<details>
<summary><b>fork_choice-088</b> Proposer re-org of late weak heads with fcU override — <i>implemented · low · latency</i></summary>

**Idea.** Track block timeliness and implement get_proposer_head so a proposer builds on the parent of a late, weak head, and should_override_forkchoice_update in all import paths so the late block is not sent to the EL as head. Run head processing early enough that the re-orging block is head before attestation deadlines.

**Impact.** Already done; a proposer builds on the parent of a late weak head and the fcU is overridden.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_production/mod.rs:229`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L229) get_proposer_head used in block production
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5500`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5500) overridden_forkchoice_update_params (fcU override)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:6772`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6772),7197 override applied on fcU paths
- [`consensus/proto_array/src/proto_array_fork_choice.rs:823`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L823) get_proposer_head

**Sources.** [prysm#11981](https://github.com/OffchainLabs/prysm/pull/11981), [prysm#12146](https://github.com/OffchainLabs/prysm/pull/12146), [prysm#12034](https://github.com/OffchainLabs/prysm/pull/12034), [teku#9247](https://github.com/Consensys-Incorporated/teku/pull/9247), [prysm#12022](https://github.com/OffchainLabs/prysm/pull/12022), [lodestar#6581](https://github.com/ChainSafe/lodestar/pull/6581)

</details>


<a id="fork_choice-091"></a>
<details>
<summary><b>fork_choice-091</b> Lightweight vote target record in LMD-GHOST — <i>implemented · low · cpu</i></summary>

**Idea.** Count LMD-GHOST votes using a small (root, slot) target record instead of full block objects, avoiding repeated hashing and deep equality comparisons.

**Impact.** Votes are tracked as small root/slot records; no block objects are hashed or compared.

**Best measured result.** fork choice was 2 to 3 seconds (pr:prysm#2333)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array_fork_choice.rs:27`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L27) VoteTracker holds (current_root,next_root,slots) only

**Sources.** [prysm#2333](https://github.com/OffchainLabs/prysm/pull/2333)

</details>


<a id="fork_choice-092"></a>
<details>
<summary><b>fork_choice-092</b> No fork choice lock across validation and newPayload — <i>implemented · medium · S · latency</i></summary>

**Idea.** During block import, do not hold the fork choice write lock across consensus validation and the blocking EL newPayload call; reacquire it afterwards, re-check admission and handle invalid payloads then. Attestations, head computation and ticks are then not stalled by validation or EL latency, and CL and EL validation run in parallel.

**Impact.** None needed.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1535-1564`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1535-L1564) newPayload runs as payload_verification_handle in parallel with consensus work
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4511-4518`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4511-L4518) write lock taken only in import_block after verification, no EL call under it

**Sources.** [prysm#12560](https://github.com/OffchainLabs/prysm/pull/12560), [prysm#12561](https://github.com/OffchainLabs/prysm/pull/12561), [caplin#23691](https://github.com/erigontech/erigon/pull/23691)

</details>


<a id="fork_choice-093"></a>
<details>
<summary><b>fork_choice-093</b> Split canonical and non-canonical nodes in one traversal — <i>n/a · low · cpu</i></summary>

**Idea.** Find non-canonical fork choice nodes (for archiving or summaries) by walking the parent chain from the head to the finalized root once and taking the index ranges between canonical ancestors, instead of two passes or a per-node is-descendant check.

**Impact.** Lighthouse does not archive or summarize blocks from fork choice nodes; the hot/cold migration works from the store, so there is no canonical/non-canonical split on the hot path.

**Best measured result.** None (pr:lodestar#1758)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array.rs:2367`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L2367) heads_descended_from_finalization only used by HTTP heads and dump_as_dot (beacon_chain.rs:1520,8250)
- [`consensus/proto_array/src/proto_array.rs:2073`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L2073) maybe_prune drops nodes below finalized

**Sources.** [lodestar@89d4fc54b](https://github.com/ChainSafe/lodestar/commit/89d4fc54b50a), [lodestar#7528](https://github.com/ChainSafe/lodestar/pull/7528), [lodestar#1758](https://github.com/ChainSafe/lodestar/pull/1758)

</details>


<a id="fork_choice-097"></a>
<details>
<summary><b>fork_choice-097</b> Read locks for read-only fork choice paths — <i>implemented · low · latency, cpu</i></summary>

**Idea.** Take a shared read lock instead of an exclusive write lock for fork choice operations that only read (head computation, proposer boost getters, latest-message queries, invalidation checks whose write takes its own lock), so concurrent readers do not serialize.

**Impact.** Read-only paths take the shared lock and writers take the write lock, so readers do not serialize.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:650`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L650) fork_choice_read_lock used for readers (heads, proposer head, fcU override beacon_chain.rs:5530)
- [`beacon_node/beacon_chain/src/canonical_head.rs:862`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L862) write lock only in recompute_head where get_head mutates
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2378`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2378),2578,2943,6624,7278 write lock only for mutating on_* calls

**Sources.** [prysm#15648](https://github.com/OffchainLabs/prysm/pull/15648), [prysm#4784](https://github.com/OffchainLabs/prysm/pull/4784), [prysm#11172](https://github.com/OffchainLabs/prysm/pull/11172), [lighthouse@0d4b58978](https://github.com/sigp/lighthouse/commit/0d4b58978ccd)

</details>


<a id="fork_choice-103"></a>
<details>
<summary><b>fork_choice-103</b> Keep updating head during sync so pruning proceeds — <i>implemented · medium · S · memory, sync, cpu</i></summary>

**Idea.** While importing blocks during sync, still run head selection regularly (per block or at epoch boundaries, with events coalesced) so finalization pruning proceeds and the non-finalized block pool does not grow unbounded.

**Impact.** None needed.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:647`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L647) recompute_head after every chain segment during sync
- [`beacon_node/beacon_chain/src/canonical_head.rs:1720`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1720) finalization prunes fork choice

**Sources.** [teku#3055](https://github.com/Consensys-Incorporated/teku/pull/3055), [nimbus@4e85b50cb](https://github.com/status-im/nimbus-eth2/commit/4e85b50cb6c4)

</details>


<a id="fork_choice-108"></a>
<details>
<summary><b>fork_choice-108</b> Persist fork choice snapshot for fast restart — <i>implemented · medium · S · startup, disk</i></summary>

**Idea.** Persist the proto-array and vote snapshot to disk (e.g. each epoch) and reload it at startup instead of rebuilding fork choice by replaying stored blocks.

**Impact.** None needed.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:1720`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1720) persist_fork_choice on finalization
- [`beacon_node/beacon_chain/src/beacon_chain.rs:8466`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L8466) persist on shutdown
- [`beacon_node/beacon_chain/src/beacon_chain.rs:692`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L692) load_fork_choice at startup

**Sources.** [teku#2270](https://github.com/Consensys-Incorporated/teku/pull/2270), [teku#1627](https://github.com/Consensys-Incorporated/teku/pull/1627), [teku#2319](https://github.com/Consensys-Incorporated/teku/pull/2319)

</details>


<a id="fork_choice-109"></a>
<details>
<summary><b>fork_choice-109</b> Rebuild proto-array at startup from stored block metadata — <i>implemented · medium · S · startup, disk</i></summary>

**Idea.** Persist checkpoint epochs with each hot block's metadata and rebuild proto-array at startup from that metadata, using views without copying, instead of loading snapshots and regenerating states.

**Impact.** Startup already avoids per-block state loads; nothing to gain. Only a crash/corruption fallback rebuild is absent, which is a robustness matter, not speed.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:692`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L692) load_fork_choice reads whole PersistedForkChoice (proto-array + checkpoints) from DB
- [`beacon_node/beacon_chain/src/canonical_head.rs:1746`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1746) persist_fork_choice, called at :1565 and :1720 and on Drop (beacon_chain.rs:8466)
- [`beacon_node/beacon_chain/src/beacon_fork_choice_store.rs:212`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_fork_choice_store.rs#L212) from_persisted loads one justified state only

**Sources.** [teku#3124](https://github.com/Consensys-Incorporated/teku/pull/3124)

</details>


<a id="fork_choice-110"></a>
<details>
<summary><b>fork_choice-110</b> Single ordered startup walk to init store and fork choice — <i>n/a · medium · S · cpu, startup</i></summary>

**Idea.** Initialize the store and fork choice together in one ordered walk over non-finalized blocks, so each state is processed once instead of twice and in random order.

**Gap in Lighthouse.** Lighthouse restores a persisted proto-array snapshot, so there is no startup walk over blocks and states to merge.

**Impact.** None; no startup replay exists.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/builder.rs:245`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L245) resume_from_db loads persisted fork choice; no walk over non-finalized blocks
- [`consensus/fork_choice/src/fork_choice.rs:1966`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1966) proto_array_from_persisted

**Sources.** [teku#2178](https://github.com/Consensys-Incorporated/teku/pull/2178)

</details>


<a id="fork_choice-114"></a>
<details>
<summary><b>fork_choice-114</b> Prewarm next justified checkpoint balances — <i>implemented · medium · S · latency, cpu</i></summary>

**Idea.** Before the epoch boundary (tick handler or last slot of epoch), compute the next justified checkpoint state's active balances in the background and coalesce concurrent misses, so the first head computation after justification hits the cache instead of stalling.

**Gap in Lighthouse.** Equivalent effect: balances are precomputed on import of the boundary block, not in the background. A miss (skipped boundary slot or evicted entry) still loads a state and computes balances synchronously, once per epoch.

**Impact.** A miss would cost one hot-state load plus a balance pass over about 1M validators; rare, so the stall the other clients measured is mostly avoided.

**Best measured result.** None (pr:caplin#23981)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_fork_choice_store.rs:259`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_fork_choice_store.rs#L259) on_verified_block inserts epoch-boundary balances into BalancesCache at block import
- [`beacon_node/beacon_chain/src/beacon_fork_choice_store.rs:349`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_fork_choice_store.rs#L349) set_justified_checkpoint uses balances_cache.get (cache hit) before falling back to get_hot_state
- [`beacon_node/beacon_chain/src/beacon_fork_choice_store.rs:50`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_fork_choice_store.rs#L50) MAX_BALANCE_CACHE_SIZE=4

**Sources.** [teku#6046](https://github.com/Consensys-Incorporated/teku/pull/6046), [caplin#23981](https://github.com/erigontech/erigon/pull/23981), [prysm#17463](https://github.com/OffchainLabs/prysm/pull/17463)

</details>


<a id="fork_choice-118"></a>
<details>
<summary><b>fork_choice-118</b> Progressive balances cache for unrealized justification — <i>implemented · low · cpu, latency</i></summary>

**Idea.** Maintain running current/previous-epoch target-attesting balances in the state and use them for unrealized justification and viability in fork choice, instead of scanning participation arrays per imported block.

**Impact.** Done since PR 4362; unrealized justification uses running target balances rather than scanning participation.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fork_choice/src/fork_choice.rs:949`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L949) on_block calls altair::process_justification_and_finalization relying on progressive balances cache
- [`consensus/state_processing/src/per_epoch_processing/altair.rs:35`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/altair.rs#L35),52 progressive_balances_cache used
- [`consensus/state_processing/src/per_block_processing.rs:143`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing.rs#L143) initialize_progressive_balances_cache

**Sources.** [lighthouse#4362](https://github.com/sigp/lighthouse/pull/4362), [teku#6141](https://github.com/Consensys-Incorporated/teku/pull/6141), [teku#6065](https://github.com/Consensys-Incorporated/teku/pull/6065)

</details>


<a id="fork_choice-120"></a>
<details>
<summary><b>fork_choice-120</b> Prune branches incompatible with finalized checkpoint — <i>partial · medium · M · cpu, memory</i></summary>

**Idea.** On finalization, also remove fork choice nodes that are not descendants of the finalized checkpoint, so dead branches are not walked on every head computation.

**Gap in Lighthouse.** Side branches that forked before the finalized block but were inserted after it in the vec survive pruning and are visited on every apply_score_changes and filter_node_tree pass. Fix: in maybe_prune, after the prefix split, retain only nodes that descend from finalized_root (one forward pass using parent indices), then remap indices/children/parents.

**Impact.** Small on mainnet (dead forks are rare and short); larger after long non-finality with many competing forks, where per-head-computation work scales with all retained nodes.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array.rs:2073`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L2073) maybe_prune drops only nodes with index &lt; finalized_index (split_off at :2095)
- [`consensus/proto_array/src/proto_array.rs:2079`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L2079) no prune at all below prune_threshold
- [`consensus/fork_choice/src/fork_choice.rs:875`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L875) on_block rejects new blocks not descending from finalized (stops new dead nodes, does not remove existing ones)
- [`consensus/fork_choice/src/fork_choice.rs:1956`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1956) ForkChoice::prune only calls maybe_prune(finalized_root)
- [`consensus/proto_array/src/proto_array.rs:488`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L488) apply_score_changes walks every node
- [`consensus/proto_array/src/proto_array.rs:1374`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L1374) filter_node_tree reverse pass walks every node from justified index to end, including non-descendant side branches

**Sources.** [prysm#11945](https://github.com/OffchainLabs/prysm/pull/11945)

</details>


<a id="fork_choice-122"></a>
<details>
<summary><b>fork_choice-122</b> Bound and prune delayed object queues — <i>implemented · medium · S · memory</i></summary>

**Idea.** Prune blocks, blobs, checkpoint states and attestations parked while waiting for dependencies once finalization (by block or slot tick) or epoch age makes them stale, and skip parking when the dependency is present, so delay queues cannot grow unbounded.

**Gap in Lighthouse.** Queues are bounded by count and by short time expiry. They are not pruned on finalization, but the expiry is a few seconds to one slot, so they cannot grow unbounded.

**Impact.** Memory is already bounded; no meaningful gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:78-90`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L78-L90) hard caps MAXIMUM_QUEUED_BLOCKS/ATTESTATIONS(16384)/DATA_COLUMNS/ENVELOPES
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:53`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L53),67 delay-queue timeouts (12 s attestations, 4 s rpc blocks) expire stale items
- [`consensus/fork_choice/src/fork_choice.rs:311`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L311) dequeue_attestations drains queued_attestations each tick

**Sources.** [grandine@60c6d449d](https://github.com/grandinetech/grandine/commit/60c6d449d7ab), [grandine#637](https://github.com/grandinetech/grandine/pull/637), [grandine@d7b8e80a0](https://github.com/grandinetech/grandine/commit/d7b8e80a0f82), [grandine@632b3236c](https://github.com/grandinetech/grandine/commit/632b3236cded)

</details>


<a id="fork_choice-123"></a>
<details>
<summary><b>fork_choice-123</b> Skip re-validating gossip-verified attestations in fork choice — <i>implemented · medium · S · cpu</i></summary>

**Idea.** When feeding attestations that gossip or block processing already validated into fork choice, skip the duplicate checks (signature, LMD/FFG consistency, target-root-known, time checks) and run only cheap index checks.

**Gap in Lighthouse.** Signatures are verified once upstream and never in fork choice. The remaining checks (target known, block lookup, target match) are a few hash lookups per attestation, so there is no costly duplicate work to remove.

**Impact.** Negligible; remaining checks are O(1) lookups.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fork_choice/src/fork_choice.rs:1325`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1325) on_attestation takes already-indexed attestation; no signature check inside
- [`consensus/fork_choice/src/fork_choice.rs:1165`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1165) validate_on_attestation skips the time check when AttestationFromBlock::True (:1181)
- [`beacon_node/beacon_chain/src/block_verification.rs:1768`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1768) block path passes AttestationFromBlock::True

**Sources.** [prysm#8276](https://github.com/OffchainLabs/prysm/pull/8276), [prysm#8277](https://github.com/OffchainLabs/prysm/pull/8277), [prysm#8301](https://github.com/OffchainLabs/prysm/pull/8301), [prysm#3562](https://github.com/OffchainLabs/prysm/pull/3562)

</details>


<a id="fork_choice-124"></a>
<details>
<summary><b>fork_choice-124</b> Process block attestations into fork choice only once — <i>implemented · medium · S · cpu</i></summary>

**Idea.** Do not feed block attestations to fork choice through a second path (separate routine or re-insert into the vote store) when the attestation pool path already applies them.

**Gap in Lighthouse.** Each block attestation is applied once, in the import path. There is no second vote store or routine.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1763`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1763) block attestations applied to fork choice in a single loop
- [`beacon_node/beacon_chain/src/attestation_verification.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs): pool/gossip attestations reach fork choice only through apply_attestation_to_fork_choice, separate from block attestations
- [`consensus/fork_choice/src/fork_choice.rs:1325`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1325) on_attestation

**Sources.** [prysm#4408](https://github.com/OffchainLabs/prysm/pull/4408), [prysm#11201](https://github.com/OffchainLabs/prysm/pull/11201)

</details>


<a id="fork_choice-125"></a>
<details>
<summary><b>fork_choice-125</b> Reuse indexed attestations from block import — <i>implemented · medium · S · cpu</i></summary>

**Idea.** Capture indexed attestations computed during block import and reuse them for fork choice vote updates instead of recomputing them.

**Gap in Lighthouse.** The ConsensusContext cache is shared by signature verification, state transition and fork choice, so indexed attestations are computed once per block.

**Impact.** None; already shared.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/consensus_context.rs:161`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/consensus_context.rs#L161) get_indexed_attestation caches by attestation tree_hash_root
- [`consensus/state_processing/src/per_block_processing/block_signature_verifier.rs:297`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/block_signature_verifier.rs#L297) signature verification fills the cache
- [`beacon_node/beacon_chain/src/block_verification.rs:1764`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1764) fork choice reuses the same consensus_context

**Sources.** [teku#2643](https://github.com/Consensys-Incorporated/teku/pull/2643)

</details>


<a id="fork_choice-132"></a>
<details>
<summary><b>fork_choice-132</b> Shrink persisted fork choice snapshot — <i>implemented · medium · disk, memory, latency</i></summary>

**Idea.** Do not persist recomputable fork choice data (balance caches, justified balances) and compress persisted votes, so the fork choice snapshot written on each update is much smaller.

**Best measured result.** None (pr:lighthouse#7805)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_fork_choice_store.rs:398`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_fork_choice_store.rs#L398) PersistedForkChoiceStoreV28 holds no balances_cache or justified_balances
- [`beacon_node/beacon_chain/src/persisted_fork_choice.rs:30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/persisted_fork_choice.rs#L30) snapshot is zstd-compressed via store_config.compress_bytes (includes votes)
- [`consensus/proto_array/src/ssz_container.rs:61`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/ssz_container.rs#L61) balances rebuilt on load, not stored

**Sources.** [lighthouse#7805](https://github.com/sigp/lighthouse/pull/7805)

</details>


<a id="fork_choice-137"></a>
<details>
<summary><b>fork_choice-137</b> Skip new-head side effects when head unchanged — <i>implemented · medium · cpu, latency, disk</i></summary>

**Idea.** Run new-head processing (events, state lookups, persistence, reorg metrics) only when the head actually changes, and compare like with like so payload-status flags do not create spurious head changes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:1207`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1207) after_new_head only when beacon_block_root changes (payload-status-only change excluded)
- [`beacon_node/beacon_chain/src/canonical_head.rs:1085`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1085) early return when view, payload status and fcu params unchanged

**Sources.** [teku#10675](https://github.com/Consensys-Incorporated/teku/pull/10675), [lighthouse#9191](https://github.com/sigp/lighthouse/pull/9191), [prysm#16508](https://github.com/OffchainLabs/prysm/pull/16508)

</details>


<a id="fork_choice-140"></a>
<details>
<summary><b>fork_choice-140</b> Drop block attestations with mismatched target ancestry — <i>implemented · medium · cpu</i></summary>

**Idea.** On block import, skip block attestations whose target checkpoint does not match the voted block's ancestry before applying them to fork choice.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fork_choice/src/fork_choice.rs:1220`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1220) validate_on_attestation compares target.root with expected_target (block.target_root or block root); mismatch gives InvalidTarget
- [`beacon_node/beacon_chain/src/block_verification.rs:1778`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1778) InvalidAttestation errors from block attestations are ignored, so they are never applied

**Sources.** [nimbus#9156](https://github.com/status-im/nimbus-eth2/pull/9156)

</details>


<a id="fork_choice-143"></a>
<details>
<summary><b>fork_choice-143</b> Ignore old block attestations in fork choice — <i>not · medium · S · cpu, sync</i></summary>

**Idea.** Do not apply attestations from imported blocks to fork choice when their target is older than the previous epoch, saving work while syncing old blocks.

**Gap in Lighthouse.** Skip block attestations whose target.epoch + 1 &lt; current epoch before on_attestation (or in validate_on_attestation for from-block). Remaining saving is only the per-validator vote compare loop, because the indexed attestation is a cache hit and attestations to pruned/finalized targets already fail fast via UnknownTargetRoot.

**Impact.** Small: saves the O(attesters) proto_array vote loop for old-target attestations during sync of non-finalized blocks; committee lookup is already free (ConsensusContext cache).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1763-1780`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1763-L1780) every block attestation goes to fork_choice.on_attestation(AttestationFromBlock::True); no target-epoch cutoff, InvalidAttestation errors are just ignored
- [`consensus/fork_choice/src/fork_choice.rs:1182-1184`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1182-L1184) current-time target-epoch check skipped when is_from_block
- [`consensus/fork_choice/src/fork_choice.rs:1361-1368`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1361-L1368) per-validator proto_array.process_attestation loop runs for any attestation that passes validation
- [`consensus/state_processing/src/consensus_context.rs:161-184`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/consensus_context.rs#L161-L184) indexed attestations are cached from block processing, so get_indexed_attestation is a cache hit here

**Second check.** Checked the block import loop, on_attestation and validate_on_attestation and the ConsensusContext cache: no epoch cutoff exists anywhere. The cache does make the gain smaller than the earlier review said.

**Sources.** [teku#4300](https://github.com/Consensys-Incorporated/teku/pull/4300)

</details>


<a id="fork_choice-145"></a>
<details>
<summary><b>fork_choice-145</b> Inherit unrealized checkpoints from parent when unchanged — <i>implemented · medium · S · cpu</i></summary>

**Idea.** Skip the O(validators) unrealized justification/finalization computation for a block when cheap checks show it cannot change: parent already computed it this epoch with the maximal result, or it is too early in the epoch.

**Impact.** None left post-Altair: the exact skip covers the grandine case and the non-skipped path is already constant-time via the progressive balances cache. Only the Prysm early-in-epoch heuristic is missing, and it would save an O(1) call.

**Best measured result.** None (pr:grandine#678)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fork_choice/src/fork_choice.rs:916-946`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L916-L946) inherits parent unrealized checkpoints when parent justified == block epoch and finalized+1 == block epoch and no slashings (same as grandine#678 maximal-result case)
- [`consensus/state_processing/src/per_epoch_processing/altair/justification_and_finalization.rs:9-30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/altair/justification_and_finalization.rs#L9-L30) the fallback is O(1): it reads progressive_balances_cache target balances and the cached total active balance, no validator iteration
- [`consensus/state_processing/src/per_epoch_processing/justification_and_finalization_state.rs:28-40`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/justification_and_finalization_state.rs#L28-L40) state setup only copies checkpoints and bits
- consensus/types/src/beacon_state.rs:2677-2689 total active balance is cached

**Second check.** Read the altair process_justification_and_finalization the fallback calls: it uses the progressive balances cache and does not iterate validators, so the O(validators) cost the idea wants to skip is not there in Lighthouse after Altair. Only phase0 still does an O(validators) ValidatorStatuses pass.

**Sources.** [grandine#678](https://github.com/grandinetech/grandine/pull/678), [prysm#10955](https://github.com/OffchainLabs/prysm/pull/10955)

</details>


<a id="fork_choice-146"></a>
<details>
<summary><b>fork_choice-146</b> Early return when no equivocators — <i>implemented · low · cpu, latency</i></summary>

**Idea.** In fast-confirmation equivocation scoring, return zero early when there are no equivocating validators instead of building the set of all attesters in the slot range.

**Impact.** Lighthouse iterates only the equivocators and checks committee membership with precomputed slot_assignments, so with no equivocators the cost is already about zero.

**Best measured result.** None (pr:lodestar#9553)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fast_confirmation/src/lib.rs:1076`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fast_confirmation/src/lib.rs#L1076) get_equivocation_score loops over the equivocating_indices set (not all slot attesters)
- [`consensus/fast_confirmation/src/lib.rs:1088`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fast_confirmation/src/lib.rs#L1088) empty set means zero iterations

**Sources.** [lodestar#9553](https://github.com/ChainSafe/lodestar/pull/9553)

</details>


<a id="fork_choice-149"></a>
<details>
<summary><b>fork_choice-149</b> Sorted cursor for equivocating indices in deltas — <i>not · low · S · cpu</i></summary>

**Idea.** In vote delta computation, sort equivocating indices and walk them with a cursor during the validator loop instead of a set lookup per validator.

**Gap in Lighthouse.** In compute_deltas, replace the per-validator equivocating_indices.contains with a peekable iterator over the (already sorted) BTreeSet advanced alongside val_index.

**Impact.** Saves one BTreeSet lookup per validator per fork choice run (about 1M at mainnet); with an empty or tiny set the lookup is near free, so gain is well under a millisecond.

**Best measured result.** None (pr:lodestar#8525)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array_fork_choice.rs:1387`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L1387) compute_deltas does BTreeSet::contains(&amp;val_index) per validator at line 1426
- [`consensus/proto_array/src/proto_array_fork_choice.rs:1426`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L1426) no cursor

**Sources.** [lodestar#8525](https://github.com/ChainSafe/lodestar/pull/8525)

</details>


<a id="fork_choice-150"></a>
<details>
<summary><b>fork_choice-150</b> Keep justified checkpoint cache updated during sync — <i>n/a · medium · cpu, sync</i></summary>

**Idea.** Update the cached justified checkpoint during batch sync so finding it does not walk ancestors back to genesis.

**Impact.** Not applicable: Lighthouse keeps the justified checkpoint in the fork choice store, updated on each on_block, with no ancestor walk.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fork_choice/src/fork_choice.rs:905`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L905) on_block calls update_checkpoints with state's justified checkpoint directly
- [`beacon_node/beacon_chain/src/beacon_fork_choice_store.rs:313`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_fork_choice_store.rs#L313) justified checkpoint and balances held in the fork choice store

**Sources.** [prysm#6594](https://github.com/OffchainLabs/prysm/pull/6594)

</details>


<a id="fork_choice-156"></a>
<details>
<summary><b>fork_choice-156</b> Update blob pruning metadata once per head change — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** Update auxiliary metadata (blob pruning info) once after the canonical head is chosen instead of for each head candidate during fork choice, avoiding repeated state-root lookups and DB writes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:1209`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1209) after_new_head runs once per head change
- [`beacon_node/beacon_chain/src/canonical_head.rs:1731`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1731) blob pruning driven once on finalization via process_prune_blobs; no per-candidate blob info update in import path

**Sources.** [lighthouse@fb2ce909f](https://github.com/sigp/lighthouse/commit/fb2ce909f66e)

</details>


