# fork_choice

163 ideas: 16 not, 19 partial, 81 implemented, 47 n/a; 7 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [fork_choice-001](#fork_choice-001) | Init and update fork choice from cached epoch data | implemented | low | M | startup, cpu |
| [fork_choice-002](#fork_choice-002) | O(1) finalized-descendant check via stored checkpoints | implemented | low | S | cpu, latency |
| [fork_choice-003](#fork_choice-003) | Allocation-free vote removal in indexed weight store | n/a | low |  | cpu, memory |
| [fork_choice-004](#fork_choice-004) | Cache block ancestor at slot for vote counting | n/a | low |  | cpu |
| [fork_choice-005](#fork_choice-005) | get_ancestor on proto-array nodes via parent index | implemented | low | S | cpu |
| [fork_choice-006](#fork_choice-006) **★** | Answer ancestor/canonical queries from in-memory fork choice | partial | medium | S | cpu, disk, latency |
| [fork_choice-007](#fork_choice-007) | Dense per-validator array of compact vote records | implemented | low | S | cpu, memory |
| [fork_choice-008](#fork_choice-008) | Pass resolved node data instead of repeated lookups | partial | low | S | cpu |
| [fork_choice-009](#fork_choice-009) | Iterate voted index range instead of copying set | n/a | low |  | cpu, memory |
| [fork_choice-010](#fork_choice-010) | Single non-throwing lookup for proto-array root-to-index | partial | low | S | cpu |
| [fork_choice-011](#fork_choice-011) | Derive fork version from head, not full scan | n/a | low |  | cpu |
| [fork_choice-012](#fork_choice-012) | No cache rebuild on cloned head state per update | implemented | low | S | cpu, latency |
| [fork_choice-013](#fork_choice-013) | Slot-ordered queued attestations with bulk drain | implemented | low | S | cpu, memory |
| [fork_choice-014](#fork_choice-014) | Cache head in fork choice; serve duties from it | implemented | low | S | cpu, latency |
| [fork_choice-015](#fork_choice-015) | Avoid repeated root encoding and field reads | n/a | low |  | cpu |
| [fork_choice-016](#fork_choice-016) | Skip second fork choice run for proposer-boost anchor | n/a | low |  | cpu, latency |
| [fork_choice-017](#fork_choice-017) | Zero-allocation has-children check | partial | low | S | cpu, memory |
| [fork_choice-018](#fork_choice-018) | Iterate votes by reference in balance update | implemented | low | S | cpu |
| [fork_choice-019](#fork_choice-019) | Read balance array, not validator objects, in confirmation | implemented | low | S | cpu, memory |
| [fork_choice-020](#fork_choice-020) | Batch attestations into fork choice, recompute head periodically | implemented | low | S | cpu, latency |
| [fork_choice-021](#fork_choice-021) | One-pass whole-chain fast-confirmation scoring | implemented | low | S | cpu |
| [fork_choice-022](#fork_choice-022) | Reweight votes at justification from epoch-processing data | n/a | low |  | cpu, memory |
| [fork_choice-023](#fork_choice-023) | Bit-pack slot assignments into stored balances | n/a | low | S | memory |
| [fork_choice-024](#fork_choice-024) | Bitfield for payload timeliness votes with popcount | implemented | low | S | memory, cpu |
| [fork_choice-025](#fork_choice-025) | Stop ancestor walks early, at finalized slot | implemented | low | S | cpu, memory, latency |
| [fork_choice-026](#fork_choice-026) | Bound the invalid-block set by slot | n/a | medium |  | memory |
| [fork_choice-027](#fork_choice-027) | Bound fork choice initialization replay horizon | implemented | low | S | startup, cpu |
| [fork_choice-028](#fork_choice-028) | Keep only unfinalized blocks in in-memory block graph | implemented | low | S | memory, startup |
| [fork_choice-029](#fork_choice-029) **★** | Maintain viable heads/filtered tree incrementally | not | medium | M | cpu |
| [fork_choice-030](#fork_choice-030) | Cache head optimistic status on head update | not | low | S | cpu, latency |
| [fork_choice-031](#fork_choice-031) **★** | Cache per-node head viability in proto-array | partial | medium | M | cpu |
| [fork_choice-032](#fork_choice-032) | Compute justified balances once per justification change | implemented | low | S | cpu, memory |
| [fork_choice-033](#fork_choice-033) | Cache justified checkpoint total active balance | implemented | low | S | cpu |
| [fork_choice-034](#fork_choice-034) | Cache late-reorg head/parent weights on head update | implemented | low | S | cpu, latency |
| [fork_choice-035](#fork_choice-035) | Cache slot tick duration per fork | n/a | low | S | cpu |
| [fork_choice-036](#fork_choice-036) | Proto-array with best-descendant pointers and vote deltas | partial | low | M | cpu, memory, latency |
| [fork_choice-037](#fork_choice-037) | Optimised LMD-GHOST with ancestor helpers and per-child weights | implemented | low | S | cpu |
| [fork_choice-038](#fork_choice-038) **★** | Cached pulled-up state and parallel vote scan | partial | medium | M | cpu, latency |
| [fork_choice-039](#fork_choice-039) | Precomputed validator-to-slot table per shuffling seed | partial | low | M | cpu, memory |
| [fork_choice-040](#fork_choice-040) | Cheapest-first checks in proposer-head/override decisions | implemented | low | S | cpu, latency |
| [fork_choice-041](#fork_choice-041) | Cheap proto-array pruning on every finalization | implemented | low | S | cpu, memory |
| [fork_choice-042](#fork_choice-042) | Cheaper head retrieval for beacon API | implemented | low | S | cpu, latency |
| [fork_choice-043](#fork_choice-043) | Test own viability before best descendant's | partial | low | S | cpu |
| [fork_choice-044](#fork_choice-044) | Justified balances from caches built at import/epoch processing | implemented | low | S | cpu, memory, disk, latency |
| [fork_choice-045](#fork_choice-045) | Store block metadata and execution status in fork choice nodes | implemented | low | S | cpu, memory, disk, latency |
| [fork_choice-046](#fork_choice-046) | Clone justified balances only when changed | implemented | low | S | cpu, latency |
| [fork_choice-047](#fork_choice-047) | Build children index once per head walk, iterate filter | implemented | low | S | cpu |
| [fork_choice-048](#fork_choice-048) | Compact store for deferred fork-choice attestations | implemented | low | S | memory |
| [fork_choice-049](#fork_choice-049) | Load fork-choice states concurrently | n/a | low | S | latency, disk |
| [fork_choice-050](#fork_choice-050) | Run fork choice on demand, not inside import | implemented | medium | S | cpu, sync |
| [fork_choice-051](#fork_choice-051) | Dedupe fork-choice attestations by bitfield overlap | implemented | low | S | cpu |
| [fork_choice-052](#fork_choice-052) | Defer fork-choice service messages during storage load | n/a | low |  | startup, cpu |
| [fork_choice-053](#fork_choice-053) | Run fork-choice pruning off the head-update path | partial | low | S | latency |
| [fork_choice-054](#fork_choice-054) | Incremental vote weight tally across get_head calls | partial | low | M | cpu, latency |
| [fork_choice-055](#fork_choice-055) | Pointer-based tree fork-choice store | n/a | low |  | cpu |
| [fork_choice-056](#fork_choice-056) | No tracing spans in per-node fork-choice helpers | implemented | low | S | cpu |
| [fork_choice-057](#fork_choice-057) | Drop duplicate head events and conversions | implemented | low | S | cpu |
| [fork_choice-058](#fork_choice-058) | Clear references on fork-choice prune | n/a | low |  | memory |
| [fork_choice-059](#fork_choice-059) | Common ancestor early exit at finalized head | not | low | S | cpu |
| [fork_choice-060](#fork_choice-060) | Skip finalized-descent walk for canonical targets | n/a | low | S | cpu |
| [fork_choice-061](#fork_choice-061) | Early return for unchanged votes in compute_deltas | implemented | low | S | cpu |
| [fork_choice-062](#fork_choice-062) | Short-circuit fork choice on empty proto-array | n/a | low | S | cpu |
| [fork_choice-063](#fork_choice-063) | Grow per-validator vote tables without doubling | not | low | S | memory |
| [fork_choice-064](#fork_choice-064) | Consolidate fork choice locks into one external lock | partial | low | M | cpu, latency |
| [fork_choice-065](#fork_choice-065) | Load/advance states before taking fork-choice lock | partial | low | M | latency, cpu, sync |
| [fork_choice-066](#fork_choice-066) | Fewer integer divisions in proposer boost | not | low | S | cpu |
| [fork_choice-067](#fork_choice-067) | Load state once and pass it down | implemented | low | S | cpu, disk |
| [fork_choice-068](#fork_choice-068) | Native numbers instead of bigint for fork-choice weights | n/a | low | S | cpu |
| [fork_choice-069](#fork_choice-069) | Fixed-size zero-default field instead of Optional | n/a | low | S | memory |
| [fork_choice-070](#fork_choice-070) | Gather all support metrics in one validator pass | implemented | low | S | cpu |
| [fork_choice-071](#fork_choice-071) | Run fork choice right before block proposal | implemented | medium | S | latency |
| [fork_choice-072](#fork_choice-072) | Start LMD-GHOST from justified root | implemented | low | S | cpu |
| [fork_choice-073](#fork_choice-073) | Run fork choice after each block import | implemented | medium | S | latency |
| [fork_choice-074](#fork_choice-074) **★** | Run fork choice once per batch of imported children | partial | medium | M | cpu, sync |
| [fork_choice-075](#fork_choice-075) | Skip eager precompute when consumer unreachable | partial | low | S | cpu, latency |
| [fork_choice-076](#fork_choice-076) | Skip auxiliary indexes on forks that never read them | implemented | low | S | cpu, latency |
| [fork_choice-077](#fork_choice-077) | Ignore pre-genesis ticks | implemented | low | S | cpu |
| [fork_choice-078](#fork_choice-078) | Head fast path for child-of-head blocks | not | low | M | cpu, latency |
| [fork_choice-079](#fork_choice-079) | Update head without waiting for EL forkchoiceUpdated | implemented | medium | S | latency |
| [fork_choice-080](#fork_choice-080) | Header presence check instead of state load under lock | n/a | low | S | disk, cpu, latency |
| [fork_choice-081](#fork_choice-081) | Hoist zero-hash comparison out of balance loop | implemented | low | S | cpu |
| [fork_choice-082](#fork_choice-082) | Hoist proposer boost out of per-node score loop | implemented | low | S | cpu |
| [fork_choice-083](#fork_choice-083) | Keep latest votes in memory, not per-vote DB writes | implemented | low | S | disk, cpu |
| [fork_choice-084](#fork_choice-084) | Integer instead of float for weight changes | implemented | low | S | cpu |
| [fork_choice-085](#fork_choice-085) | Votes store small node index or target id, not root | not | low | L | cpu, memory |
| [fork_choice-086](#fork_choice-086) | Iterative weight propagation instead of recursion | implemented | low | S | cpu |
| [fork_choice-087](#fork_choice-087) | Key-only iteration skipping signature payloads | n/a | low |  | cpu, disk |
| [fork_choice-088](#fork_choice-088) | Proposer re-org of late weak heads with fcU override | implemented | low | S | latency |
| [fork_choice-089](#fork_choice-089) | Lazy head state update with in-memory block graph | implemented | low | S | cpu |
| [fork_choice-090](#fork_choice-090) | Small refillable ancestor root buffer | partial | low | M | memory, disk |
| [fork_choice-091](#fork_choice-091) | Lightweight vote target record in LMD-GHOST | implemented | low | S | cpu |
| [fork_choice-092](#fork_choice-092) | No fork choice lock across validation and newPayload | implemented | medium | S | latency |
| [fork_choice-093](#fork_choice-093) | Split canonical and non-canonical nodes in one traversal | n/a | low |  | cpu |
| [fork_choice-094](#fork_choice-094) | Reduced-tree LMD-GHOST tracking only branching nodes | n/a | low | S | cpu, latency |
| [fork_choice-095](#fork_choice-095) | On block insert, update only parent's best child | implemented | low | S | cpu |
| [fork_choice-096](#fork_choice-096) | Use parking_lot locks for the block graph | implemented | low | S | cpu |
| [fork_choice-097](#fork_choice-097) | Read locks for read-only fork choice paths | implemented | low | S | latency, cpu |
| [fork_choice-098](#fork_choice-098) | Split fork choice locks by independent fields | not | low | M | latency, cpu |
| [fork_choice-099](#fork_choice-099) | Simplify fork choice locking and attestation caches | n/a | low | S | cpu, latency |
| [fork_choice-100](#fork_choice-100) | Run fork choice on a dedicated single-thread executor | n/a | low | S | latency, cpu |
| [fork_choice-101](#fork_choice-101) | Pause fast-confirmation rule while syncing | n/a | low |  | cpu, sync |
| [fork_choice-102](#fork_choice-102) | Store epoch-boundary target pointer in each node | implemented | low | S | cpu, latency |
| [fork_choice-103](#fork_choice-103) | Keep updating head during sync so pruning proceeds | implemented | medium | S | memory, sync, cpu |
| [fork_choice-104](#fork_choice-104) | Skip per-slot fork choice runs while far behind | implemented | medium | S | cpu, latency, sync |
| [fork_choice-105](#fork_choice-105) | Skip periodic fork choice pass when attestation pool empty | not | low | S | cpu, sync |
| [fork_choice-106](#fork_choice-106) | Skip block-tree cache updates during sync import | n/a | low |  | cpu, sync |
| [fork_choice-107](#fork_choice-107) | Memoize total active balance in fast confirmation | n/a | low |  | cpu, latency |
| [fork_choice-108](#fork_choice-108) | Persist fork choice snapshot for fast restart | implemented | medium | S | startup, disk |
| [fork_choice-109](#fork_choice-109) | Rebuild proto-array at startup from stored block metadata | implemented | low | S | startup, disk |
| [fork_choice-110](#fork_choice-110) | Single ordered startup walk to init store and fork choice | n/a | medium | S | cpu, startup |
| [fork_choice-111](#fork_choice-111) | Primitive-valued maps for fork choice indices | n/a | low |  | memory, cpu |
| [fork_choice-112](#fork_choice-112) | Store checkpoints as plain structs in fork choice | n/a | low |  | memory |
| [fork_choice-113](#fork_choice-113) | Pre-aggregate attestations before fork choice | n/a | low | S | cpu |
| [fork_choice-114](#fork_choice-114) | Prewarm next justified checkpoint balances | implemented | low | S | latency, cpu |
| [fork_choice-115](#fork_choice-115) | Diff justified balances to reweight only changed validators | partial | low | M | cpu, latency |
| [fork_choice-116](#fork_choice-116) | Preload post-finalized blocks into fork choice at startup | implemented | low | S | latency, cpu |
| [fork_choice-117](#fork_choice-117) | Precollect ancestor structure in one pass for O(1) checks | not | low | M | cpu |
| [fork_choice-118](#fork_choice-118) | Progressive balances cache for unrealized justification | implemented | low | S | cpu, latency |
| [fork_choice-119](#fork_choice-119) | Prune block DAG exactly once per finality change | implemented | low | S | cpu, latency |
| [fork_choice-120](#fork_choice-120) **★** | Prune branches incompatible with finalized checkpoint | partial | medium | M | cpu, memory |
| [fork_choice-121](#fork_choice-121) | Prune secondary fork choice indices with nodes | n/a | low | S | memory |
| [fork_choice-122](#fork_choice-122) | Bound and prune delayed object queues | implemented | low | S | memory |
| [fork_choice-123](#fork_choice-123) | Skip re-validating gossip-verified attestations in fork choice | implemented | low | S | cpu |
| [fork_choice-124](#fork_choice-124) | Process block attestations into fork choice only once | implemented | low | S | cpu |
| [fork_choice-125](#fork_choice-125) | Reuse indexed attestations from block import | implemented | low | S | cpu |
| [fork_choice-126](#fork_choice-126) | Remove unreachable branches in fork choice code | implemented | low | S | cpu |
| [fork_choice-127](#fork_choice-127) | Remove fork choice caches that never hit | n/a | low | S | cpu |
| [fork_choice-128](#fork_choice-128) | Resolve payload committee from post-state in hand | implemented | low | S | latency, cpu |
| [fork_choice-129](#fork_choice-129) | Reuse one working state across reorgs | n/a | low |  | memory, cpu, latency |
| [fork_choice-130](#fork_choice-130) | Head state plus reverse changesets for forks | n/a | low |  | memory |
| [fork_choice-131](#fork_choice-131) | Share observation sets instead of cloning with store | n/a | low |  | cpu, memory |
| [fork_choice-132](#fork_choice-132) | Shrink persisted fork choice snapshot | implemented | low | S | disk, memory, latency |
| [fork_choice-133](#fork_choice-133) | Maintain canonical-block set inside fork choice | implemented | low | S | cpu |
| [fork_choice-134](#fork_choice-134) | Run only one fork choice implementation | n/a | low |  | cpu |
| [fork_choice-135](#fork_choice-135) | Find blocks at a slot set in one chain walk | implemented | low | S | cpu |
| [fork_choice-136](#fork_choice-136) | Skip early-slot head recompute without validators | n/a | low |  | cpu, latency |
| [fork_choice-137](#fork_choice-137) | Skip new-head side effects when head unchanged | implemented | low | S | cpu, latency, disk |
| [fork_choice-138](#fork_choice-138) | Skip fork choice while a head update is pending | n/a | low |  | cpu |
| [fork_choice-139](#fork_choice-139) | Skip duplicate forkchoiceUpdated before attestation duty | n/a | low |  | cpu, latency |
| [fork_choice-140](#fork_choice-140) | Drop block attestations with mismatched target ancestry | implemented | low | S | cpu |
| [fork_choice-141](#fork_choice-141) | Drop attestations with non-viable target state | not | low | Add an optional check in attestation_verification to reject non-viable targets before the shuffling-cache-miss state load. | cpu, latency |
| [fork_choice-142](#fork_choice-142) | Take first variant index in proto-array pruning | n/a | low |  | cpu |
| [fork_choice-143](#fork_choice-143) **★** | Ignore old block attestations in fork choice | not | medium | S | cpu, sync |
| [fork_choice-144](#fork_choice-144) | Skip get_ancestor in on_block justified update | implemented | low | S | cpu |
| [fork_choice-145](#fork_choice-145) | Inherit unrealized checkpoints from parent when unchanged | implemented | low | S | cpu |
| [fork_choice-146](#fork_choice-146) | Early return when no equivocators | implemented | low | S | cpu, latency |
| [fork_choice-147](#fork_choice-147) | Slim per-block summary record for target lookups | implemented | low | S | cpu, disk, memory |
| [fork_choice-148](#fork_choice-148) | Queue early attestations and slim fork choice state | implemented | low | S | cpu, memory |
| [fork_choice-149](#fork_choice-149) | Sorted cursor for equivocating indices in deltas | not | low | S | cpu |
| [fork_choice-150](#fork_choice-150) | Keep justified checkpoint cache updated during sync | n/a | medium |  | cpu, sync |
| [fork_choice-151](#fork_choice-151) | Proto-array as the store's block index | n/a | low |  | memory, startup |
| [fork_choice-152](#fork_choice-152) | Record payload status for replayed envelopes after restart | implemented | low | S | latency, startup |
| [fork_choice-153](#fork_choice-153) | Mark tips full from stored payloads at setup | implemented | low | S | sync |
| [fork_choice-154](#fork_choice-154) | Keep finalized checkpoint dependent root after pruning | not | low | S | cpu, memory |
| [fork_choice-155](#fork_choice-155) | Single cache for forkchoice update parameters | partial | low | M | memory |
| [fork_choice-156](#fork_choice-156) | Update blob pruning metadata once per head change | implemented | low | S | cpu, latency |
| [fork_choice-157](#fork_choice-157) | Count fork-choice votes from aggregate bitfield popcounts | n/a | low |  | cpu |
| [fork_choice-158](#fork_choice-158) | Ancestor skip tables at power-of-two heights | not | low | M | cpu, latency |
| [fork_choice-159](#fork_choice-159) | Drop redundant latest-messages map beside proto-array | implemented | low | S | memory, disk |
| [fork_choice-160](#fork_choice-160) | Rank empty payload variant above unsatisfied payload in own slot | n/a | low |  | latency, cpu |
| [fork_choice-161](#fork_choice-161) | Optional skip of finalized root consistency check | not | low | S | cpu |
| [fork_choice-162](#fork_choice-162) | Reuse one LMD-GHOST result for head and logging | n/a | low |  | cpu |
| [fork_choice-163](#fork_choice-163) | Shared backward sweep for committee unions over slot ranges | n/a | low | M | cpu, memory |

★ actionable. Click an id for the full record.

## Ideas

<a id="fork_choice-001"></a>
<details>
<summary><b>fork_choice-001</b> Init and update fork choice from cached epoch data — <i>implemented · low · M · startup, cpu</i></summary>

**Idea.** On startup and fork choice rebuild, feed fork choice from cached per-epoch committee/attester data (epoch refs) instead of loading full beacon states to derive attesters. This avoids state loads and replays, which dominate during long non-finality.

**Impact.** Startup restores proto-array and votes from the persisted ForkChoice; only the justified state is loaded once for balances, with no per-block state replay.

**Best measured result.** "dramatically speeds up startup in long periods of non-finality" (commit:nimbus@c6674de5d2db)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:692-715`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L692-L715)
- [`beacon_node/beacon_chain/src/beacon_fork_choice_store.rs:212-239`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_fork_choice_store.rs#L212-L239)
- [`beacon_node/beacon_chain/src/beacon_fork_choice_store.rs:349-367`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_fork_choice_store.rs#L349-L367)

**Skeptic check.** Verified load_fork_choice decodes the persisted fork choice (nodes plus votes) and from_persisted loads a single justified state; there is no fork-choice rebuild path that replays states from finalization. Same effect as the Nimbus change, by persistence rather than epoch refs.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus@c6674de5d](https://github.com/status-im/nimbus-eth2/commit/c6674de5d2db), [nimbus#1421](https://github.com/status-im/nimbus-eth2/pull/1421), [nimbus#1521](https://github.com/status-im/nimbus-eth2/pull/1521)

</details>


<a id="fork_choice-002"></a>
<details>
<summary><b>fork_choice-002</b> O(1) finalized-descendant check via stored checkpoints — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Decide whether a proto-array node descends from the finalized checkpoint (for head viability and block lookups) by comparing its stored justified/finalized/unrealized checkpoints or walking up from the node, instead of scanning all proto-array nodes. Removes O(n) work per node in head selection under non-finality.

**Best measured result.** Added perf test reproducing large updateHead time (600000 validators, 7200 blocks); no numbers stated (pr:lodestar#5867)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array.rs:2251-2310`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L2251-L2310)
- [`consensus/proto_array/src/proto_array.rs:2135-2174`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L2135-L2174)
- [`consensus/proto_array/src/proto_array.rs:1374-1441`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L1374-L1441)

**Skeptic check.** is_finalized_checkpoint_or_descendant first compares the node's stored finalized/justified/unrealized checkpoints (O(1) in the common non-finality case) and then walks parents only down to the finalized slot; filter_node_tree calls the viability check only on leaves. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#5906](https://github.com/ChainSafe/lodestar/pull/5906), [lodestar#5867](https://github.com/ChainSafe/lodestar/pull/5867), [nimbus#4100](https://github.com/status-im/nimbus-eth2/pull/4100), [teku#7606](https://github.com/Consensys-Incorporated/teku/pull/7606)

</details>


<a id="fork_choice-003"></a>
<details>
<summary><b>fork_choice-003</b> Allocation-free vote removal in indexed weight store — <i>n/a · low · cpu, memory</i></summary>

**Idea.** When removing a vote from a per-root indexed weight store, compact in place without allocating and read balances from the checkpoint state at query time, so the fork-choice lock is held only briefly per vote.

**Impact.** Lighthouse uses proto-array with per-validator vote trackers and delta computation; there is no per-root indexed weight store to compact.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array_fork_choice.rs:27`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L27) VoteTracker per validator in a Vec
- proto_array_fork_choice.rs:1387 compute_deltas

**Sources.** [caplin#21694](https://github.com/erigontech/erigon/pull/21694)

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


<a id="fork_choice-005"></a>
<details>
<summary><b>fork_choice-005</b> get_ancestor on proto-array nodes via parent index — <i>implemented · low · S · cpu</i></summary>

**Idea.** Implement get_ancestor inside proto-array by following parent indices directly instead of mapping parent root to index at each step, removing a hash lookup per hop.

**Impact.** There is no hash lookup per hop.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array.rs:1836-1882`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L1836-L1882) get_ancestor_node does one indices lookup, then follows parent() indices
- [`consensus/proto_array/src/proto_array.rs:2426-2439`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L2426-L2439) Iter follows node.parent() index
- [`consensus/fork_choice/src/fork_choice.rs:509-540`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L509-L540) get_ancestor uses iter_block_roots

**Skeptic check.** Verified that both ancestor walks follow parent indices after one root-to-index lookup. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#3108](https://github.com/Consensys-Incorporated/teku/pull/3108)

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

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [prysm#6753](https://github.com/OffchainLabs/prysm/pull/6753), [teku#5031](https://github.com/Consensys-Incorporated/teku/pull/5031), [lodestar#927](https://github.com/ChainSafe/lodestar/pull/927), [prysm#10512](https://github.com/OffchainLabs/prysm/pull/10512), [prysm#10516](https://github.com/OffchainLabs/prysm/pull/10516), [lodestar@81a43d8ba](https://github.com/ChainSafe/lodestar/commit/81a43d8bae59)

</details>


<a id="fork_choice-007"></a>
<details>
<summary><b>fork_choice-007</b> Dense per-validator array of compact vote records — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Store each validator's latest vote as a compact plain record (or dense parallel arrays with sentinels) in a flat array indexed by validator index, instead of a hash map, interned dedup index, or boxed/SSZ-backed objects. This gives O(1) set/get, fewer allocations and faster delta computation under the fork choice lock.

**Impact.** Already O(1) get/set in a flat Vec of plain records.

**Best measured result.** set with pinned messages 61,418 ns/op -&gt; 8.5 ns/op; ~1.66s lock hold per slot removed (pr:caplin#22352)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array_fork_choice.rs:26-34`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L26-L34)
- [`consensus/proto_array/src/proto_array_fork_choice.rs:430`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L430)
- [`consensus/proto_array/src/proto_array_fork_choice.rs:583`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L583)
- [`consensus/proto_array/src/proto_array_fork_choice.rs:693-700`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L693-L700)
- [`consensus/proto_array/src/proto_array_fork_choice.rs:1412`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L1412)

**Skeptic check.** VoteTracker is a plain ~82-byte struct in ElasticList (a Vec indexed by validator index); compute_deltas iterates it linearly. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#4316](https://github.com/Consensys-Incorporated/teku/pull/4316), [caplin#22352](https://github.com/erigontech/erigon/pull/22352), [teku#4254](https://github.com/Consensys-Incorporated/teku/pull/4254), [lodestar#8549](https://github.com/ChainSafe/lodestar/pull/8549)

</details>


<a id="fork_choice-008"></a>
<details>
<summary><b>fork_choice-008</b> Pass resolved node data instead of repeated lookups — <i>partial · low · S · cpu</i></summary>

**Idea.** Look up the fork-choice node (or its payload variants and slot) once and pass it through the dependent checks instead of re-resolving the block root in the store/index map for each check.

**Gap in Lighthouse.** Internal walks pass indices (IndexedForkChoiceNode), but outer callers (get_block, should_extend_payload, is_descendant...) each re-look up the root in the indices HashMap. Could add index-taking variants for callers that chain queries.

**Impact.** A few hashmap lookups per block import or head update; unmeasurable against the rest.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array_fork_choice.rs:1067`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L1067),1262,1148-1175 each public query re-resolves root-&gt;index
- [`consensus/proto_array/src/proto_array.rs:1448-1480`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L1448-L1480) find_head_walk computes proposer boost once and works on indices

**Sources.** [teku#10826](https://github.com/Consensys-Incorporated/teku/pull/10826), [teku#10786](https://github.com/Consensys-Incorporated/teku/pull/10786), [lighthouse#10327](https://github.com/sigp/lighthouse/pull/10327)

</details>


<a id="fork_choice-009"></a>
<details>
<summary><b>fork_choice-009</b> Iterate voted index range instead of copying set — <i>n/a · low · cpu, memory</i></summary>

**Idea.** Track the highest validator index that has voted and iterate the index range directly in score updates, instead of copying the full set of voted indices on every fork choice update.

**Gap in Lighthouse.** Lighthouse never copies a set of voted indices; it already iterates the vote vector length (= highest voted index + 1) directly.

**Impact.** None; already equivalent.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array_fork_choice.rs:1387-1420`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L1387-L1420) compute_deltas iterates votes.iter_mut() by index range
- [`consensus/proto_array/src/proto_array_fork_choice.rs:430-445`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L430-L445) ElasticList grows only to highest voted index

**Sources.** [teku#4260](https://github.com/Consensys-Incorporated/teku/pull/4260)

</details>


<a id="fork_choice-010"></a>
<details>
<summary><b>fork_choice-010</b> Single non-throwing lookup for proto-array root-to-index — <i>partial · low · S · cpu</i></summary>

**Idea.** Do proto-array root-to-index lookups with one map get returning a sentinel or default (e.g. -1/None), instead of contains followed by get, two sequential lookups, or an exception-raising lookup, so hits and misses are cheap.

**Gap in Lighthouse.** compute_deltas uses one indices.get per vote, but the ForkChoice wrappers do two SipHash lookups per call: ForkChoice::get_block calls is_finalized_checkpoint_or_descendant (indices.get) then proto_array.get_block (indices.get again), and ForkChoice::contains_block does indices.contains_key followed by the same descendant check's indices.get. get_block is on the gossip attestation path (attestation_verification.rs:1252). A variant of is_finalized_checkpoint_or_descendant that takes the already-resolved node, or returns it, would make these a single lookup.

**Impact.** Saves one HashMap&lt;Hash256,usize&gt; SipHash lookup per gossip attestation/block lookup; negligible next to signature verification.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array_fork_choice.rs:1434`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L1434)
- [`consensus/proto_array/src/proto_array_fork_choice.rs:1481`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L1481)
- [`consensus/proto_array/src/proto_array_fork_choice.rs:1500`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L1500)
- [`consensus/fork_choice/src/fork_choice.rs:1600-1612`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1600-L1612)
- [`consensus/proto_array/src/proto_array_fork_choice.rs:1062-1068`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L1062-L1068)
- [`consensus/proto_array/src/proto_array.rs:2256-2264`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L2256-L2264)
- [`consensus/proto_array/src/proto_array.rs:454`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L454)

**Skeptic check.** The earlier check looked only at compute_deltas, which is correct; the fork_choice.rs get_block/contains_block wrappers still do two sequential lookups for the same root.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [nimbus#8070](https://github.com/status-im/nimbus-eth2/pull/8070), [lodestar#9023](https://github.com/ChainSafe/lodestar/pull/9023), [teku#10448](https://github.com/Consensys-Incorporated/teku/pull/10448)

</details>


<a id="fork_choice-011"></a>
<details>
<summary><b>fork_choice-011</b> Derive fork version from head, not full scan — <i>n/a · low · cpu</i></summary>

**Idea.** When choosing spec/fork version for ancestor lookups, use the head block's slot instead of scanning the whole proto-array for the highest slot, removing an O(n) pass.

**Gap in Lighthouse.** Lighthouse does not choose a spec/fork version by scanning proto-array for the highest slot; the scan does not exist.

**Impact.** None.

**Best measured result.** Described as expensive search removed; no numbers (pr:teku#5108)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array.rs:1255-1283`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L1255-L1283) find_head starts at justified index and takes no fork version
- [`consensus/proto_array/src/proto_array.rs:1837`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L1837) get_ancestor_node uses no spec/fork lookup via highest slot

**Sources.** [teku#5108](https://github.com/Consensys-Incorporated/teku/pull/5108)

</details>


<a id="fork_choice-012"></a>
<details>
<summary><b>fork_choice-012</b> No cache rebuild on cloned head state per update — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** When the head state is cloned for a head change, do not rebuild pubkey/exit caches on each head update; keep or share caches so the ~70ms rebuild is not paid every time.

**Best measured result.** ~70ms+ penalty on mainnet (pr:lighthouse#3658)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:1134-1150`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1134-L1150)
- [`consensus/types/src/state/beacon_state.rs:2757-2763`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2757-L2763)
- [`consensus/types/src/state/beacon_state.rs:2777-2782`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2777-L2782)
- [`consensus/types/src/state/beacon_state.rs:2979-2993`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2979-L2993)
- [`consensus/types/src/state/pubkey_cache.rs:8-14`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/pubkey_cache.rs#L8-L14)

**Skeptic check.** The head state comes from the hot state cache with caches intact; build_caches only fills uninitialised caches, the exit cache is guarded by check_initialized, and the pubkey cache is a persistent HashTrieMap that is cloned cheaply and extended incrementally. The earlier note that the pubkey cache lives only on BeaconChain was imprecise, but the verdict holds.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#3658](https://github.com/sigp/lighthouse/pull/3658)

</details>


<a id="fork_choice-013"></a>
<details>
<summary><b>fork_choice-013</b> Slot-ordered queued attestations with bulk drain — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Keep fork choice's queued (future-slot) attestations ordered or bucketed by slot (e.g. BTreeMap by slot, sorted deque split with partition_point), so dequeuing due votes splits off a prefix in bulk instead of iterating, copying or reallocating the whole queue on every attestation or tick. Removes quadratic CPU when many attestations are gossiped.

**Impact.** Enqueue is O(log slots) and dequeue splits the due prefix in bulk; no per-attestation whole-queue copy remains (PR 9524: 61.9ms to 5.17ms at 93750 entries).

**Best measured result.** None (pr:lighthouse#9524)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fork_choice/src/fork_choice.rs:371`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L371) queued_attestations: BTreeMap&lt;Slot, Vec&lt;QueuedAttestation&gt;&gt;
- [`consensus/fork_choice/src/fork_choice.rs:311-325`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L311-L325) dequeue_attestations uses BTreeMap::split_off(&amp;current_slot) + mem::replace
- [`consensus/fork_choice/src/fork_choice.rs:1386-1389`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1386-L1389) on_attestation pushes into the slot bucket via entry().or_default()
- [`consensus/fork_choice/src/fork_choice.rs:1580`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1580) process_attestation_queue drains once per update_time

**Skeptic check.** Verified the BTreeMap bucket and split_off drain on the gossip on_attestation path; earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#5288](https://github.com/status-im/nimbus-eth2/pull/5288), [nimbus#1805](https://github.com/status-im/nimbus-eth2/pull/1805), [lodestar#7142](https://github.com/ChainSafe/lodestar/pull/7142), [lighthouse#8378](https://github.com/sigp/lighthouse/pull/8378), [lighthouse#9524](https://github.com/sigp/lighthouse/pull/9524)

</details>


<a id="fork_choice-014"></a>
<details>
<summary><b>fork_choice-014</b> Cache head in fork choice; serve duties from it — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Cache the computed head node (with its payload status) inside fork choice and recompute deltas/scores only at explicit points or when votes or balances changed since the last get_head. Validator duties (attesters, proposers) and block production read the cached head instead of re-running head selection.

**Gap in Lighthouse.** Minor: ProtoArrayForkChoice::find_head has no dirty flag, so compute_deltas (O(validators)) and the node_slots Vec collect run even when no votes or balances changed since the last call.

**Impact.** Duties, attestation and block production read the cached head; head is recomputed only at explicit points. A dirty-flag skip would save about one O(validators) scan per redundant recompute.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:282`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L282) CachedHead
- [`beacon_node/beacon_chain/src/canonical_head.rs:758`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L758) recompute_head_at_current_slot is the only head-selection entry, called per slot (beacon_chain.rs:7496) and after block/envelope import (gossip_methods.rs:1008,1449,1965,4084; sync_methods.rs:207)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4506`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4506),5401 import and payload-attribute paths read canonical_head.cached_head()
- [`consensus/proto_array/src/proto_array_fork_choice.rs:769-817`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L769-L817) find_head always runs compute_deltas

**Skeptic check.** Confirmed CachedHead is what consumers read and get_head runs only from recompute_head_* at explicit points; earlier evidence and its minor gap were right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#1907](https://github.com/status-im/nimbus-eth2/pull/1907), [lodestar#2696](https://github.com/ChainSafe/lodestar/pull/2696), [lodestar@9cebc9155](https://github.com/ChainSafe/lodestar/commit/9cebc9155d6e), [prysm#16419](https://github.com/OffchainLabs/prysm/pull/16419)

</details>


<a id="fork_choice-015"></a>
<details>
<summary><b>fork_choice-015</b> Avoid repeated root encoding and field reads — <i>n/a · low · cpu</i></summary>

**Idea.** Keep block roots in the representation each consumer needs and read lazily-decoded attestation fields once into locals, passing the encoded root along, instead of repeatedly converting roots (bytes&lt;-&gt;hex) or re-reading tree-backed fields in fork-choice loops.

**Gap in Lighthouse.** Rust holds roots as Hash256 with no hex/bytes conversions or lazy tree-backed field reads in fork-choice loops.

**Impact.** None.

**Best measured result.** redundant tree get and toHexString caused 14% of total time on a full-subnet node (pr:lodestar#2769)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array_fork_choice.rs:693`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L693) process_attestation takes Hash256 directly
- [`consensus/proto_array/src/proto_array_fork_choice.rs:1387`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L1387) compute_deltas uses Hash256 keys

**Sources.** [lodestar#3118](https://github.com/ChainSafe/lodestar/pull/3118), [lodestar#2769](https://github.com/ChainSafe/lodestar/pull/2769)

</details>


<a id="fork_choice-016"></a>
<details>
<summary><b>fork_choice-016</b> Skip second fork choice run for proposer-boost anchor — <i>n/a · low · cpu, latency</i></summary>

**Idea.** Use the justified checkpoint as the proposer-boost dependent-root anchor when it suffices and recompute head only when the justified block is older than the dependent slot, avoiding a second fork choice run on normal block import.

**Gap in Lighthouse.** Lighthouse keeps the proposer boost root in the store and applies it inside find_head; there is no dependent-root anchor or second fork choice run to avoid.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fork_choice/src/fork_choice.rs:568-600`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L568-L600) get_head runs find_head once
- [`consensus/fork_choice/src/fork_choice.rs:1502-1545`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1502-L1545) on_tick just zeroes proposer_boost_root
- [`consensus/proto_array/src/proto_array.rs:826-880`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L826-L880) should_apply_proposer_boost reads the boost block's parent via parent index

**Sources.** [lodestar#9853](https://github.com/ChainSafe/lodestar/pull/9853)

</details>


<a id="fork_choice-017"></a>
<details>
<summary><b>fork_choice-017</b> Zero-allocation has-children check — <i>partial · low · S · cpu, memory</i></summary>

**Idea.** When only testing whether a fork-choice node has children, use an existence check rather than cloning the children list and taking its length; it runs per node on every head computation.

**Gap in Lighthouse.** The children index is cached, so no parent scan is needed. But the hot paths still materialise the children just to test for them. get_filtered_node_tree pushes child indices into two fresh Vecs per node (one heap allocation per node that has children, over every node since justified), used only for emptiness and any() checks. These could be single-pass boolean folds over self.children[i]. find_head_walk and get_node_children clone a ProtoNode for each child and collect a Vec before the is_empty check.

**Impact.** Removes one Vec allocation per node in the filtered-tree pass, plus ProtoNode clones per child along the head walk, on every fork-choice head computation. These are small constant-factor savings.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array.rs:455-458`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L455-L458) cached children index
- [`consensus/proto_array/src/proto_array.rs:1387-1430`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L1387-L1430) get_filtered_node_tree allocates empty_children/full_children Vecs for every node on each head computation, only to test is_empty or any-viable
- [`consensus/proto_array/src/proto_array.rs:1481-1491`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L1481-L1491) find_head_walk collects get_node_children (cloned ProtoNodes) into a Vec and tests children.is_empty()
- [`consensus/proto_array/src/proto_array.rs:1885-1935`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L1885-L1935) get_node_children clones the full ProtoNode (several hundred bytes with three inline BitVector&lt;U512&gt;) per child

**Skeptic check.** The earlier evidence said the is_empty checks at 1387-1430 run on the cached index without cloning. In fact they run on Vecs that are freshly built per node, and get_node_children clones ProtoNodes. This is the same alloc-just-to-count pattern that prysm#17048 removed.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [prysm#17048](https://github.com/OffchainLabs/prysm/pull/17048)

</details>


<a id="fork_choice-018"></a>
<details>
<summary><b>fork_choice-018</b> Iterate votes by reference in balance update — <i>implemented · low · S · cpu</i></summary>

**Idea.** In the per-validator vote loop of fork-choice balance/delta updates, iterate by reference instead of copying each vote struct (with its roots) by value.

**Impact.** Votes are iterated by reference, so there is no per-vote struct copy.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array_fork_choice.rs:1412`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L1412) for (val_index, vote) in votes.iter_mut().enumerate()
- [`consensus/proto_array/src/proto_array_fork_choice.rs:27-34`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L27-L34) VoteTracker fields

**Skeptic check.** Confirmed that compute_deltas iterates votes by mutable reference. The Rust compiler makes this a non-issue in any case.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#14196](https://github.com/OffchainLabs/prysm/pull/14196)

</details>


<a id="fork_choice-019"></a>
<details>
<summary><b>fork_choice-019</b> Read balance array, not validator objects, in confirmation — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** In fast-confirmation (and similar per-validator scans), read a memoized effective-balance array with zero for inactive/slashed validators instead of reading each validator record for slashed and activation/exit epochs.

**Impact.** The FCR scans read flat memoized arrays, not Validator records.

**Best measured result.** JS heap grew hundreds of MB per scanned state with native views; sim 570 MB vs 0 MB heap per 1M validators (pr:lodestar#10371)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fast_confirmation/src/balance_source.rs:68-110`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fast_confirmation/src/balance_source.rs#L68-L110) BalanceSourceData::new builds effective_balances (0 when inactive) and slashed Vec once per balance source
- [`consensus/fast_confirmation/src/balance_source.rs:118-135`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fast_confirmation/src/balance_source.rs#L118-L135) unslashed_and_active_indices / unslashed_balance read the flat arrays
- [`consensus/fast_confirmation/src/optimizations.rs:290-310`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fast_confirmation/src/optimizations.rs#L290-L310) aggregate_vote_balances
- [`consensus/fast_confirmation/src/lib.rs:848-887`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fast_confirmation/src/lib.rs#L848-L887) get_node_support_between_slots iterates the balance array

**Skeptic check.** Verified that every FCR per-validator loop uses BalanceSourceData arrays. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#10371](https://github.com/ChainSafe/lodestar/pull/10371)

</details>


<a id="fork_choice-020"></a>
<details>
<summary><b>fork_choice-020</b> Batch attestations into fork choice, recompute head periodically — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Collect verified attestations and apply them to fork choice in one batch call (grouped by target, tracking dirty validators), and recompute the head on a timer such as once per slot, instead of one call per attestation that each propagates deltas or recomputes head.

**Gap in Lighthouse.** Minor: verified gossip batches (process_gossip_attestation_batch) are still applied with one apply_attestation_to_fork_choice call, and one fork choice write lock and update_time, per attestation, not one batched call per batch.

**Impact.** The expensive part (per-attestation delta propagation or head recompute) is already absent; batching the lock would only reduce write-lock acquisitions and contention with get_head.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fork_choice/src/fork_choice.rs:1325-1392`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1325-L1392) on_attestation only updates VoteTracker (process_attestation) or queues by slot; no delta propagation or head recompute
- [`consensus/proto_array/src/proto_array_fork_choice.rs:693`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L693) process_attestation sets next_root only
- [`consensus/proto_array/src/proto_array_fork_choice.rs:1387`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L1387) compute_deltas applies all pending vote changes in one pass per get_head
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7496`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7496) per-slot head recompute
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2573-2586`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2573-L2586) apply_attestation_to_fork_choice takes the fork choice write lock once per attestation
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:363`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L363),432 batch-verified gossip attestations applied one by one

**Skeptic check.** Verified vote recording is O(attesters) with lazy deltas at get_head and a per-slot recompute, which gives the idea's effect; the per-attestation lock is a small leftover, not a missing mechanism.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine@713420c47](https://github.com/grandinetech/grandine/commit/713420c47a6a), [silver#294](https://github.com/gattaca-com/silver/pull/294), [prysm#4802](https://github.com/OffchainLabs/prysm/pull/4802), [prysm#8381](https://github.com/OffchainLabs/prysm/pull/8381)

</details>


<a id="fork_choice-021"></a>
<details>
<summary><b>fork_choice-021</b> One-pass whole-chain fast-confirmation scoring — <i>implemented · low · S · cpu</i></summary>

**Idea.** For fast confirmation, memoize per-slot inputs (committees, thresholds, equivocators) and score the whole chain in one pass over validators by bucketing votes by block and prefix/suffix-summing, instead of one validator pass per block.

**Impact.** The one-pass whole-chain scoring originated in Lighthouse (lodestar#9227 cites sigp/lighthouse#8951). One O(V) pass per block remains: get_node_support_between_slots, reached through compute_safety_threshold, runs only for blocks whose parent slot was skipped. This is rare.

**Best measured result.** epoch transition 18-20 s to 2 s (M4 Max, mainnet); slot unchanged 300-400 ms (pr:teku#11212)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fast_confirmation/src/optimizations.rs:252-286`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fast_confirmation/src/optimizations.rs#L252-L286) precompute_chain_attestation_scores: aggregate by vote root, project onto chain, suffix-sum
- [`consensus/fast_confirmation/src/optimizations.rs:80-104`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fast_confirmation/src/optimizations.rs#L80-L104) HonestFfgSupportCache
- [`consensus/fast_confirmation/src/lib.rs:592-607`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fast_confirmation/src/lib.rs#L592-L607) find_latest_confirmed_descendant builds the score cache once for both loops
- [`consensus/fast_confirmation/src/lib.rs:803-812`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fast_confirmation/src/lib.rs#L803-L812) is_confirmed_chain_safe uses the same one-pass cache
- [`consensus/fast_confirmation/src/slot_assignments.rs:128`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fast_confirmation/src/slot_assignments.rs#L128) SlotAssignments memoized

**Skeptic check.** Confirmed that both FCR loops and the chain-safety check read the precomputed scores. The only per-block validator scan left is the skip-slot support discount (lib.rs:902-944), a minor residual.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#9227](https://github.com/ChainSafe/lodestar/pull/9227), [teku#11212](https://github.com/Consensys-Incorporated/teku/pull/11212)

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


<a id="fork_choice-023"></a>
<details>
<summary><b>fork_choice-023</b> Bit-pack slot assignments into stored balances — <i>n/a · low · S · memory</i></summary>

**Idea.** Store per-validator auxiliary data (slot assignment) in unused high bits of the already stored effective-balance array instead of allocating a separate per-validator array.

**Impact.** No separate per-validator slot array is allocated in Lighthouse, so there is nothing to pack into balance high bits.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fast_confirmation/src/slot_assignments.rs:85`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fast_confirmation/src/slot_assignments.rs#L85) assignments are resolved on demand from existing Arc&lt;CommitteeCache&gt; shufflings, no separate per-validator slot array exists
- [`consensus/fast_confirmation/src/balance_source.rs:58`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fast_confirmation/src/balance_source.rs#L58) effective_balances is a plain Vec&lt;u64&gt;

**Sources.** [nimbus#7985](https://github.com/status-im/nimbus-eth2/pull/7985)

</details>


<a id="fork_choice-024"></a>
<details>
<summary><b>fork_choice-024</b> Bitfield for payload timeliness votes with popcount — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** Store per-block payload-timeliness-committee votes as a bitfield and count them with popcount instead of a boolean array and filter, cutting memory per block ~8x and avoiding an allocation per check.

**Impact.** The votes are already a bitfield counted with popcount.

**Best measured result.** 8x memory reduction per tracked block (4KB to 64 bytes) (pr:lodestar#9021)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array.rs:157-163`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L157-L163) payload_timeliness_votes / payload_data_availability_votes: BitVector&lt;U512&gt;
- [`consensus/proto_array/src/proto_array.rs:277-293`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L277-L293) ptc_votes_timeliness uses num_set_bits
- ethereum_ssz-0.10.4/src/bitfield.rs:510-514 num_set_bits = count_ones per byte

**Skeptic check.** Verified that the PTC votes are BitVector&lt;U512&gt;, stored inline in a 128-byte SmallVec, and counted with count_ones. No allocation is made per check.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#9021](https://github.com/ChainSafe/lodestar/pull/9021)

</details>


<a id="fork_choice-025"></a>
<details>
<summary><b>fork_choice-025</b> Stop ancestor walks early, at finalized slot — <i>implemented · low · S · cpu, memory, latency</i></summary>

**Idea.** Iterate fork choice ancestors lazily newest-first and stop at the finalized root/slot, the window start, or the minimum needed (reorg distance, payload counts), instead of collecting or walking the whole chain back to genesis/anchor. Makes queries O(window) rather than O(chain).

**Impact.** Every proto-array ancestor walk caller found stops at its target, window or finalized slot; none collects the chain to the anchor.

**Best measured result.** Win only under prolonged non-finality (pr:lodestar#9824)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array.rs:2177`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L2177) iter_nodes lazy newest-first
- [`consensus/proto_array/src/proto_array.rs:2208-2218`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L2208-L2218) is_descendant take_while slot &gt;= ancestor slot
- [`consensus/proto_array/src/proto_array.rs:2251`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L2251) is_finalized_checkpoint_or_descendant early-exits on checkpoint match and stops at the finalized slot
- [`consensus/proto_array/src/proto_array.rs:1852-1880`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L1852-L1880) get_ancestor_node walks only down to the target slot
- [`consensus/fork_choice/src/fork_choice.rs:527`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L527) get_ancestor uses find(slot &lt;= ancestor_slot)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:8436-8445`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L8436-L8445) range roots break at start_slot
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:470`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L470) take(count)
- [`consensus/fast_confirmation/src/lib.rs:1352`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fast_confirmation/src/lib.rs#L1352),1382,1455 bounded by ancestor/terminal/epoch slot

**Skeptic check.** Checked every iter_block_roots/iter_nodes caller outside tests; all are lazy and bounded, so the earlier evidence holds.

**Verdict history.** implemented (checked) → implemented (skeptic)

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
<summary><b>fork_choice-027</b> Bound fork choice initialization replay horizon — <i>implemented · low · S · startup, cpu</i></summary>

**Idea.** On startup, limit how many unfinalized blocks are replayed into fork choice so long non-finalizing periods do not cause a full replay of every unfinalized block.

**Impact.** Startup cost does not depend on the number of unfinalized blocks replayed, because none are replayed: the proto-array is deserialized as-is (only rebuild_children_index, O(nodes)).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/builder.rs:245-253`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L245-L253) resume_from_db loads persisted fork choice
- [`beacon_node/beacon_chain/src/beacon_chain.rs:692-715`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L692-L715) load_fork_choice deserializes PersistedForkChoice from DBColumn::ForkChoice; no block replay

**Skeptic check.** Confirmed startup deserializes the proto-array and that no fork-choice reset/replay-from-finalization path remains in this tree; the earlier verdict is right, value lowered because there is no replay to bound.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#1904](https://github.com/status-im/nimbus-eth2/pull/1904), [nimbus#1910](https://github.com/status-im/nimbus-eth2/pull/1910)

</details>


<a id="fork_choice-028"></a>
<details>
<summary><b>fork_choice-028</b> Keep only unfinalized blocks in in-memory block graph — <i>implemented · low · S · memory, startup</i></summary>

**Idea.** Keep the in-memory by-root block index/graph only for the non-finalized portion and serve finalized blocks from an on-disk slot index, so memory does not grow with chain length and startup need not load the finalized index.

**Impact.** The in-memory block graph holds only non-finalized nodes (plus up to 256 pruning slack); finalized lookups go to the DB, so memory does not grow with chain length.

**Best measured result.** None (pr:nimbus#3513)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array.rs:2073-2127`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L2073-L2127) maybe_prune drops finalized nodes from nodes/indices/children (threshold DEFAULT_PRUNE_THRESHOLD=256, proto_array_fork_choice.rs:24)
- [`consensus/fork_choice/src/fork_choice.rs:509`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L509) get_ancestor works on the unfinalized DAG
- [`beacon_node/beacon_chain/src/beacon_chain.rs:793`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L793),819 finalized roots served by forwards_iter_block_roots(_until) from the store

**Skeptic check.** Verified pruning and DB-backed finalized lookups; Lighthouse never held a whole-chain in-memory block index like Nimbus's ChainDAG, so the earlier verdict holds.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#3293](https://github.com/status-im/nimbus-eth2/pull/3293), [nimbus#3513](https://github.com/status-im/nimbus-eth2/pull/3513)

</details>


<a id="fork_choice-029"></a>
<details>
<summary><b>fork_choice-029</b> Maintain viable heads/filtered tree incrementally — <i>not · medium · M · cpu</i></summary>

**Idea.** Maintain the set of viable heads (filtered block tree) incrementally as blocks arrive, instead of rebuilding it or walking the block tree on every head computation.

**Gap in Lighthouse.** Persist per-node viability (or the viable set) and update it in on_block, on execution-status changes (invalidation), on justified/finalized checkpoint changes and on prune, so find_head_walk reads it instead of rebuilding the filtered tree each call.

**Impact.** find_head is O(all nodes since start_index) with several allocations per call; negligible at healthy finality, grows during long non-finality.

**Best measured result.** "Huge improvements on flame" (pr:prysm#4515)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array.rs:1304`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L1304) get_filtered_node_tree allocates a new HashSet per call
- [`consensus/proto_array/src/proto_array.rs:1335`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L1335) filter_node_tree: forward pass over all nodes plus a reverse pass, rebuilding invalid_payloads HashSet and excluded Vec and per-node child Vecs each call
- [`consensus/proto_array/src/proto_array.rs:1448`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L1448) find_head_walk calls get_filtered_node_tree on every find_head (1465)
- [`consensus/proto_array/src/proto_array.rs:1529`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L1529) filtered_node_tree_leaves_and_weights rebuilds it again
- [`consensus/proto_array/src/proto_array.rs:116`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L116) best_child/best_descendant remain only as V17 SSZ fields; no maybe_update_best_child_and_descendant exists any more

**Second check.** Searched proto_array and fork_choice for any cached head, best_descendant updater or incremental viability flag; the old incremental best_child/best_descendant mechanism has been removed in this checkout in favour of the spec-style full filtered-tree walk, so nothing equivalent remains.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [prysm#4515](https://github.com/OffchainLabs/prysm/pull/4515), [nimbus#259](https://github.com/status-im/nimbus-eth2/pull/259)

</details>


<a id="fork_choice-030"></a>
<details>
<summary><b>fork_choice-030</b> Cache head optimistic status on head update — <i>not · low · S · cpu, latency</i></summary>

**Idea.** Record the head block's optimistic/execution status when the head changes, so readers do not query fork choice (and take its lock) each time.

**Gap in Lighthouse.** Add an execution verdict to CachedHead set in recompute_head, but status can change later (optimistic to valid) so it needs refresh on payload-status updates; head_execution_status and is_optimistic_or_invalid_head are the readers.

**Impact.** Saves a fork-choice read-lock acquisition on 7 non-test callers; negligible except under lock contention.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:577`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L577) head_execution_status takes the fork choice read lock and calls get_node_execution_status
- [`consensus/fork_choice/src/fork_choice.rs:1717`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1717) plus is_finalized_checkpoint_or_descendant check on each call
- [`beacon_node/beacon_chain/src/canonical_head.rs:282`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L282) CachedHead has no optimistic flag

**Sources.** [prysm#12552](https://github.com/OffchainLabs/prysm/pull/12552)

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

**Verdict history.** not (checked) → partial (refuted)

**Sources.** [nimbus#6076](https://github.com/status-im/nimbus-eth2/pull/6076)

</details>


<a id="fork_choice-032"></a>
<details>
<summary><b>fork_choice-032</b> Compute justified balances once per justification change — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Have fork choice hold a small snapshot of justified-checkpoint effective balances (zero for inactive/slashed) plus total, fetched lazily only when the justified checkpoint changes, instead of passing or looking up balances (or caching large epoch results) on every head update or vote.

**Gap in Lighthouse.** Minor: find_head compares old_balances != new_balances (full Vec compare, about 8 MB at 1M validators) on every call instead of keying on the justified checkpoint.

**Impact.** Balances are computed once per justified checkpoint change and reused for every get_head.

**Best measured result.** get_head regression 126 ms to 198 ms p50 cited as motivation; no after-number stated (pr:ethlambda#649)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/justified_balances.rs:7-55`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/justified_balances.rs#L7-L55) JustifiedBalances: effective balances, zero for inactive/slashed, plus total
- [`beacon_node/beacon_chain/src/beacon_fork_choice_store.rs:341-368`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_fork_choice_store.rs#L341-L368) set_justified_checkpoint refreshes from balances_cache or loads the justified state only on justified change
- [`consensus/fork_choice/src/fork_choice.rs:578-586`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L578-L586) get_head passes store.justified_balances() by reference
- [`consensus/proto_array/src/proto_array_fork_choice.rs:802-804`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L802-L804) stored old balances cloned only when changed

**Skeptic check.** Verified the snapshot is refreshed only in set_justified_checkpoint and borrowed by get_head; the earlier evidence is accurate.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#1702](https://github.com/ChainSafe/lodestar/pull/1702), [prysm#11964](https://github.com/OffchainLabs/prysm/pull/11964), [ethlambda#649](https://github.com/lambdaclass/ethlambda/pull/649), [nimbus#139](https://github.com/status-im/nimbus-eth2/pull/139)

</details>


<a id="fork_choice-033"></a>
<details>
<summary><b>fork_choice-033</b> Cache justified checkpoint total active balance — <i>implemented · low · S · cpu</i></summary>

**Idea.** Store the justified checkpoint's total active balance when the justified checkpoint updates and use it for proposer boost, instead of summing justified balances on every find_head.

**Impact.** Proposer boost and reorg thresholds read the cached total in O(1); the total is computed only when the justified checkpoint changes.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/justified_balances.rs:14`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/justified_balances.rs#L14)
- [`consensus/proto_array/src/justified_balances.rs:23`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/justified_balances.rs#L23)
- [`beacon_node/beacon_chain/src/beacon_fork_choice_store.rs:349`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_fork_choice_store.rs#L349)
- [`beacon_node/beacon_chain/src/beacon_fork_choice_store.rs:366`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_fork_choice_store.rs#L366)
- [`consensus/proto_array/src/proto_array.rs:2391`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L2391)
- [`consensus/proto_array/src/proto_array.rs:2404`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L2404)

**Skeptic check.** Verified: JustifiedBalances.total_effective_balance is computed once in from_justified_state, which runs only on a justified checkpoint change (balances_cache or state load). get_proposer_score and calculate_committee_fraction read the cached field. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#5437](https://github.com/status-im/nimbus-eth2/pull/5437), [lodestar#6288](https://github.com/ChainSafe/lodestar/pull/6288), [teku#11459](https://github.com/Consensys-Incorporated/teku/pull/11459)

</details>


<a id="fork_choice-034"></a>
<details>
<summary><b>fork_choice-034</b> Cache late-reorg head/parent weights on head update — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Compute head and parent weights used by late-block-reorg checks once per head update and cache them, removing the per-call recomputation and the state dependency.

**Impact.** Head/parent weights are stored per node by apply_score_changes; reorg checks read them in O(1) with no state access.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array.rs:803`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L803)
- [`consensus/proto_array/src/proto_array_fork_choice.rs:821`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L821)
- [`consensus/proto_array/src/proto_array_fork_choice.rs:879`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L879)
- [`consensus/proto_array/src/proto_array_fork_choice.rs:929`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L929)

**Skeptic check.** Verified: get_proposer_head and is_head_weak read node.weight()/attestation_score() kept up to date in proto_array, and thresholds come from the cached justified total. Teku's per-head-update cache serves the same purpose: no recomputation and no state dependency. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#7911](https://github.com/Consensys-Incorporated/teku/pull/7911)

</details>


<a id="fork_choice-035"></a>
<details>
<summary><b>fork_choice-035</b> Cache slot tick duration per fork — <i>n/a · low · S · cpu</i></summary>

**Idea.** Cache the tick/slot duration and recompute only when the fork phase changes, instead of on every tick.

**Impact.** Lighthouse has no per-tick duration computation; on_tick is a few integer ops per slot, nothing to cache.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fork_choice/src/fork_choice.rs:1523`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1523) on_tick only sets slot, resets boost, handles epoch change

**Sources.** [grandine#568](https://github.com/grandinetech/grandine/pull/568)

</details>


<a id="fork_choice-036"></a>
<details>
<summary><b>fork_choice-036</b> Proto-array with best-descendant pointers and vote deltas — <i>partial · low · M · cpu, memory, latency</i></summary>

**Idea.** Represent the non-finalized block tree as a flat array of nodes with parent, weight, best-child and best-descendant fields, apply only per-validator vote deltas in one backward pass that propagates weight to parents and updates best pointers. get_head is then a lookup of the justified node's best descendant instead of recomputing LMD-GHOST over the whole tree and all validators.

**Gap in Lighthouse.** The vote-delta half is present, but the best-descendant half was removed in schema v29: ProtoArray::find_head now runs filter_node_tree (O(nodes) with HashSet inserts, Vec allocations and an invalid_payloads HashSet scan) plus a find_head_walk from the justified root on every call, instead of maintaining best_child/best_descendant in apply_score_changes and doing an O(1) lookup. Restoring it would mean maintaining viability and best pointers per (node, PayloadStatus) in apply_score_changes, or caching filter_node_tree output until nodes or checkpoints change.

**Impact.** Under finality the DAG holds about 100 nodes, so the cost is microseconds. Under long non-finality (the code comment cites 500k+ blocks) every get_head pays an O(nodes) allocating pass that best-descendant pointers would avoid.

**Best measured result.** None (pr:prysm#4649)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array_fork_choice.rs:1387`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L1387) compute_deltas per-validator vote deltas
- [`consensus/proto_array/src/proto_array.rs:476-560`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L476-L560) apply_score_changes: one backward pass applying deltas and back-propagating weight
- [`consensus/proto_array/src/ssz_container.rs:88-91`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/ssz_container.rs#L88-L91) and beacon_chain/src/schema_change/migration_schema_v29.rs:11 best_child/best_descendant cleared, 'no longer used (replaced by the virtual tree walk)'
- [`consensus/proto_array/src/proto_array.rs:1255-1282`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L1255-L1282) find_head calls find_head_walk, not a best_descendant lookup
- [`consensus/proto_array/src/proto_array.rs:1466-1471`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L1466-L1471),1340-1440 get_filtered_node_tree/filter_node_tree: full forward and reverse pass over all nodes from the justified index on every get_head, building a HashSet&lt;(usize, PayloadStatus)&gt; and per-node children Vecs
- [`consensus/proto_array/src/proto_array.rs:1484-1525`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L1484-L1525) greedy walk recomputes get_weight and tiebreakers per child per level
- [`consensus/proto_array/src/proto_array_fork_choice.rs:781-786`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L781-L786) node_slots Vec collected over all nodes each find_head

**Skeptic check.** Earlier evidence cited best_descendant at proto_array.rs:119 as live, but it is a dead field cleared on load; weights are still incremental, but head selection is now a spec-style filter-plus-walk, not a pointer lookup.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [prysm#4643](https://github.com/OffchainLabs/prysm/pull/4643), [lodestar@4512c6320](https://github.com/ChainSafe/lodestar/commit/4512c6320e73), [lodestar@765aeaf53](https://github.com/ChainSafe/lodestar/commit/765aeaf53f59), [lighthouse#804](https://github.com/sigp/lighthouse/pull/804), [lodestar#898](https://github.com/ChainSafe/lodestar/pull/898), [nimbus#865](https://github.com/status-im/nimbus-eth2/pull/865), [prysm#4559](https://github.com/OffchainLabs/prysm/pull/4559), [prysm#4778](https://github.com/OffchainLabs/prysm/pull/4778), [prysm#4649](https://github.com/OffchainLabs/prysm/pull/4649), [lodestar@f5c8accd7](https://github.com/ChainSafe/lodestar/commit/f5c8accd7cc0), [teku#1170](https://github.com/Consensys-Incorporated/teku/pull/1170), [ethlambda#235](https://github.com/lambdaclass/ethlambda/pull/235), [nimbus#965](https://github.com/status-im/nimbus-eth2/pull/965), [lodestar#165](https://github.com/ChainSafe/lodestar/pull/165)

</details>


<a id="fork_choice-037"></a>
<details>
<summary><b>fork_choice-037</b> Optimised LMD-GHOST with ancestor helpers and per-child weights — <i>implemented · low · S · cpu</i></summary>

**Idea.** Replace naive LMD-GHOST, which walks the tree per vote and per child, with an optimised implementation behind a fork choice trait that uses precomputed ancestor-at-height lookups and per-child vote weights, so head selection does not rescan the whole block tree per vote.

**Impact.** Superseded by proto-array; naive per-vote tree walks no longer exist.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array.rs:476`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L476) apply_score_changes keeps per-node weights from vote deltas
- [`consensus/proto_array/src/proto_array.rs:1448`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L1448) find_head_walk walks children only, reading precomputed attestation_score
- [`consensus/proto_array/src/proto_array.rs:1765`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L1765) get_weight reads node score, no per-vote tree walk

**Skeptic check.** Verified find_head_walk uses node weights maintained by apply_score_changes and the cached children index; earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

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

**Verdict history.** partial (checked) → partial (refuted)

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


<a id="fork_choice-040"></a>
<details>
<summary><b>fork_choice-040</b> Cheapest-first checks in proposer-head/override decisions — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** In late-block-reorg proposer-head and should_override_forkchoice_update checks, evaluate cheap conditions first and exit on first mismatch, loading the justified state or computing weights only once and only if all cheap checks pass.

**Impact.** Both the fcU override path and the block-production re-org path exit on cheap checks first; the state is fetched from cache only after all checks pass.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5523`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5523)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5569`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5569)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5612`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5612)
- [`beacon_node/beacon_chain/src/block_production/mod.rs:187`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L187)
- [`beacon_node/beacon_chain/src/block_production/mod.rs:217`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L217)
- [`beacon_node/beacon_chain/src/block_production/mod.rs:229`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L229)
- [`beacon_node/beacon_chain/src/block_production/mod.rs:256`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L256)
- [`consensus/proto_array/src/proto_array_fork_choice.rs:879`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L879)

**Skeptic check.** Verified both paths: overridden_forkchoice_update_params_or_failure_reason checks disabled, slot timing, cached weights and lateness before the proposer-cache lookup; get_state_for_re_org checks disabled, timing, lateness and get_proposer_head before get_advanced_hot_state_from_cache. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#7753](https://github.com/Consensys-Incorporated/teku/pull/7753), [teku#7763](https://github.com/Consensys-Incorporated/teku/pull/7763)

</details>


<a id="fork_choice-041"></a>
<details>
<summary><b>fork_choice-041</b> Cheap proto-array pruning on every finalization — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Make proto-array pruning cheap (no table rebuilds) and prune nodes before the finalized block whenever finality advances, including during range sync and on slot ticks, instead of waiting for a large threshold. The tree stays small, head computation traverses fewer nodes and memory does not leak.

**Impact.** Tree stays near unfinalized size; the LH #3408 leak is fixed.

**Best measured result.** None (pr:lighthouse#3408)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:1738`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1738) prune() after each finalization migration
- [`consensus/fork_choice/src/fork_choice.rs:1956`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1956) prune -&gt; maybe_prune
- [`consensus/proto_array/src/proto_array.rs:2073`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L2073) maybe_prune: split_off and index shift, no rebuild
- [`consensus/proto_array/src/proto_array_fork_choice.rs:24`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L24) DEFAULT_PRUNE_THRESHOLD = 256

**Skeptic check.** Confirmed pruning runs on every finality advance in after_finalization, cheaply via split_off; the 256-node threshold bounds extra nodes to ~8 epochs, which is the intended design.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#1535](https://github.com/status-im/nimbus-eth2/pull/1535), [lighthouse#3408](https://github.com/sigp/lighthouse/pull/3408), [prysm#4642](https://github.com/OffchainLabs/prysm/pull/4642), [prysm#11387](https://github.com/OffchainLabs/prysm/pull/11387), [prysm#10768](https://github.com/OffchainLabs/prysm/pull/10768)

</details>


<a id="fork_choice-042"></a>
<details>
<summary><b>fork_choice-042</b> Cheaper head retrieval for beacon API — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Serve get_head/head lookups in the beacon API from cached fork-choice results without recomputation.

**Impact.** The head API reads the cached head (an Arc snapshot clone) plus one fork-choice read-lock lookup; get_head never runs.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/block_id.rs:48`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L48)
- [`beacon_node/beacon_chain/src/canonical_head.rs:589`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L589)
- [`beacon_node/beacon_chain/src/canonical_head.rs:627`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L627)

**Skeptic check.** Verified: BlockId::Head uses head_and_execution_status, which clones CachedHead and does one node execution-status lookup. Finalized and Justified also read the cached head. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#12377](https://github.com/erigontech/erigon/pull/12377)

</details>


<a id="fork_choice-043"></a>
<details>
<summary><b>fork_choice-043</b> Test own viability before best descendant&#x27;s — <i>partial · low · S · cpu</i></summary>

**Idea.** In proto-array best-descendant updates, check the node's own viability before its best descendant's (which walks ancestry), dropping cost from O(n^2) toward O(n) on long linear unfinalized chains.

**Gap in Lighthouse.** best_child/best_descendant were removed; the O(n^2) pattern is gone. Remaining analog: node_is_viable_for_head evaluates is_finalized_checkpoint_or_descendant even when correct_justified is already false; make it lazy (short-circuit order).

**Impact.** Saves an ancestry walk per leaf with a bad justified source on long non-finality; irrelevant in healthy mainnet.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array.rs:2135`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L2135) node_is_viable_for_head computes correct_finalized (ancestry walk) before &amp;&amp; with correct_justified
- [`consensus/proto_array/src/proto_array.rs:1255`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L1255) find_head uses filter_node_tree reverse pass, best_descendant removed (ssz_container.rs:88)

**Sources.** [teku#7598](https://github.com/Consensys-Incorporated/teku/pull/7598)

</details>


<a id="fork_choice-044"></a>
<details>
<summary><b>fork_choice-044</b> Justified balances from caches built at import/epoch processing — <i>implemented · low · S · cpu, memory, disk, latency</i></summary>

**Idea.** Build the effective-balances snapshot for each epoch-boundary checkpoint from a state already in hand (block import or the per-epoch transition cache), cache it keyed by (boundary root, epoch), and hand the same immutable list to fork choice. A justified checkpoint switch is then a lookup instead of regenerating, rewinding or decoding a checkpoint state and copying a full balance list.

**Gap in Lighthouse.** Minor: when the boundary slot is skipped, on_verified_block loads the boundary state with get_hot_state on the import path (:293); cache hits clone the Vec&lt;u64&gt;.

**Impact.** Justified switch is a lookup plus a clone in the common case.

**Best measured result.** Head recompute at epoch-start tick took 0.5-4 s (Hoodi 8 times, up to 2.3 s queue wait); snapshot build ~25 ms per checkpoint (pr:ethlambda#665)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_fork_choice_store.rs:260`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_fork_choice_store.rs#L260) on_verified_block caches boundary balances from the import state
- [`beacon_node/beacon_chain/src/beacon_fork_choice_store.rs:68`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_fork_choice_store.rs#L68) BalancesCache keyed by (root, epoch), 4 entries
- [`beacon_node/beacon_chain/src/beacon_fork_choice_store.rs:345`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_fork_choice_store.rs#L345) set_justified_checkpoint cache lookup, state load only on miss

**Skeptic check.** Verified the cache is filled from the state in hand at import and read on justification; earlier evidence correct. The skipped-boundary state load is a rare residual cost.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#4290](https://github.com/ChainSafe/lodestar/pull/4290), [lighthouse#2849](https://github.com/sigp/lighthouse/pull/2849), [ethlambda#665](https://github.com/lambdaclass/ethlambda/pull/665), [nimbus#1489](https://github.com/status-im/nimbus-eth2/pull/1489), [teku#3685](https://github.com/Consensys-Incorporated/teku/pull/3685), [lodestar#1537](https://github.com/ChainSafe/lodestar/pull/1537)

</details>


<a id="fork_choice-045"></a>
<details>
<summary><b>fork_choice-045</b> Store block metadata and execution status in fork choice nodes — <i>implemented · low · S · cpu, memory, disk, latency</i></summary>

**Idea.** Store per-block metadata (state root, execution block hash, optimistic/execution status, justified/finalized checkpoints, dependent roots) directly on fork choice nodes. API duties, execution checks, invalidation and head events then read it from the node instead of separate hash maps or loading blocks or states from disk.

**Impact.** Duties and execution checks avoid block/state loads.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array.rs:85`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L85) ProtoNode stores state_root, target_root, shuffling ids, checkpoints, execution_status
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1741`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1741) attestation duties read execution status from fork choice node

**Skeptic check.** Confirmed node fields and their use in validator_attestation_duties; earlier evidence right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#1014](https://github.com/status-im/nimbus-eth2/pull/1014), [lighthouse#2643](https://github.com/sigp/lighthouse/pull/2643), [prysm#15137](https://github.com/OffchainLabs/prysm/pull/15137), [lodestar@9865e62bb](https://github.com/ChainSafe/lodestar/commit/9865e62bb7ac), [nimbus#4969](https://github.com/status-im/nimbus-eth2/pull/4969), [prysm#10400](https://github.com/OffchainLabs/prysm/pull/10400), [prysm#16811](https://github.com/OffchainLabs/prysm/pull/16811)

</details>


<a id="fork_choice-046"></a>
<details>
<summary><b>fork_choice-046</b> Clone justified balances only when changed — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** In find_head, compare the new justified balances with the cached copy and clone only when they differ, avoiding a large copy under the fork-choice write lock on almost every call.

**Impact.** The balances clone happens only when the justified balances change; the O(n) equality compare remains.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array_fork_choice.rs:802`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L802)
- [`consensus/proto_array/src/proto_array_fork_choice.rs:780`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L780)

**Skeptic check.** Verified: find_head does `if old_balances != new_balances { *old_balances = new_balances.clone() }`. This is Lighthouse's own PR #9090. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#9090](https://github.com/sigp/lighthouse/pull/9090)

</details>


<a id="fork_choice-047"></a>
<details>
<summary><b>fork_choice-047</b> Build children index once per head walk, iterate filter — <i>implemented · low · S · cpu</i></summary>

**Idea.** In find_head, build the parent-to-children index once per call and run the viability filter pass iteratively in reverse node order, instead of scanning the whole block index at every visited node or recursing. This turns the walk from quadratic to linear in unfinalized blocks.

**Gap in Lighthouse.** Residual O(N) per call: filter_node_tree rebuilds invalid_payloads, excluded and viable sets each head computation.

**Impact.** Already linear in unfinalized nodes.

**Best measured result.** Unchanged in 130 of 131 calls; fork choice time in block import 31.58 ms to 15.00 ms (~53%) (pr:lighthouse#10023)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array.rs:458`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L458) cached children index
- [`consensus/proto_array/src/proto_array.rs:772`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L772) maintained in on_block
- [`consensus/proto_array/src/proto_array.rs:2101`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L2101) maintained in maybe_prune
- [`consensus/proto_array/src/proto_array.rs:1335`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L1335) filter_node_tree single reverse pass, no recursion

**Skeptic check.** Read filter_node_tree and find_head_walk: children index is persistent (better than per-call build), filter is iterative; earlier evidence right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#10023](https://github.com/sigp/lighthouse/pull/10023), [ethlambda#746](https://github.com/lambdaclass/ethlambda/pull/746)

</details>


<a id="fork_choice-048"></a>
<details>
<summary><b>fork_choice-048</b> Compact store for deferred fork-choice attestations — <i>implemented · low · S · memory</i></summary>

**Idea.** Hold attestations waiting for fork-choice application in a dedicated structure with only the data needed (indices, root, epoch) instead of full attestations in a generic future pool.

**Impact.** Deferred attestations are stored as minimal QueuedAttestation records (slot, indices, root, target epoch) in a slot-keyed BTreeMap; signatures and the full AttestationData are not kept.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fork_choice/src/fork_choice.rs:276`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L276)
- [`consensus/fork_choice/src/fork_choice.rs:297`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L297)
- [`consensus/fork_choice/src/fork_choice.rs:311`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L311)
- [`consensus/fork_choice/src/fork_choice.rs:371`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L371)

**Skeptic check.** Verified: QueuedAttestation is built from IndexedAttestationRef with only the fields fork choice needs and is dequeued via split_off. Teku dedups per validator, but the memory difference is minor. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#5481](https://github.com/Consensys-Incorporated/teku/pull/5481)

</details>


<a id="fork_choice-049"></a>
<details>
<summary><b>fork_choice-049</b> Load fork-choice states concurrently — <i>n/a · low · S · latency, disk</i></summary>

**Idea.** Load the several beacon states a per-slot fork-choice computation needs concurrently on async tasks, so the fork-choice thread is not blocked and loads overlap.

**Impact.** Lighthouse keeps justified balances in the fork-choice store, so no states are loaded per slot to overlap.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5517`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5517) override check uses cached JustifiedBalances, no state load
- [`consensus/fork_choice/src/fork_choice.rs:627`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L627) get_proposer_head takes balances from fc_store

**Sources.** [teku#11066](https://github.com/Consensys-Incorporated/teku/pull/11066)

</details>


<a id="fork_choice-050"></a>
<details>
<summary><b>fork_choice-050</b> Run fork choice on demand, not inside import — <i>implemented · medium · S · cpu, sync</i></summary>

**Idea.** Decouple fork choice from block import: run it when a head is needed rather than as part of every block import.

**Impact.** Block import does not run get_head. Callers recompute the head after import: once per segment in range sync, and once per imported block on gossip/RPC.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:758`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L758)
- [`beacon_node/beacon_chain/src/canonical_head.rs:781`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L781)
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:647`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L647)
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1008`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1008)
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:212`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L212)

**Skeptic check.** Verified: get_head runs only from recompute_head_at_slot_internal, and the network handlers call it after import. process_blocks calls it once per chain segment. This is Lighthouse's own PR #679. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#679](https://github.com/sigp/lighthouse/pull/679)

</details>


<a id="fork_choice-051"></a>
<details>
<summary><b>fork_choice-051</b> Dedupe fork-choice attestations by bitfield overlap — <i>implemented · low · S · cpu</i></summary>

**Idea.** Make the seen-attestation filter for fork choice aware of aggregation-bit overlap so attestations whose bits are a subset of already seen ones are not reprocessed.

**Impact.** Nothing left: a subset attestation costs one compare per bit, the same as a bitfield overlap check.

**Best measured result.** fork choice attestations 52/47/46 down to 15/29/14 (pr:prysm#4483)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array_fork_choice.rs:693`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L693) process_attestation is an O(1) slot compare per validator
- [`consensus/fork_choice/src/fork_choice.rs:1361`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1361) on_attestation loops indices, no per-attestation tree work
- [`beacon_node/beacon_chain/src/observed_aggregates.rs:125`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_aggregates.rs#L125) subset gossip aggregates are dropped before fork choice

**Second check.** The earlier review flagged block attestations as unfiltered. Reading ForkChoice::on_attestation and ProtoArray::process_attestation shows the latest-message tracker already makes reprocessing a no-op: per bit there is no weight or tree work, and compute_deltas skips unchanged votes. Prysm's PR fixed a heavier per-attestation path that Lighthouse does not have.

**Skeptic check.** Confirmed the latest-message design makes reprocessing cheap and gossip subsets are already filtered; the Prysm fix addressed a costlier per-attestation path LH never had.

**Verdict history.** partial (checked) → implemented (refuted) → implemented (skeptic)

**Sources.** [prysm#4483](https://github.com/OffchainLabs/prysm/pull/4483)

</details>


<a id="fork_choice-052"></a>
<details>
<summary><b>fork_choice-052</b> Defer fork-choice service messages during storage load — <i>n/a · low · startup, cpu</i></summary>

**Idea.** While replaying fork choice from storage at startup, hold messages to other services until loading finishes so they do not process intermediate states.

**Impact.** Lighthouse loads fork choice before services start; no inter-service messaging to defer.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:692`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L692) load_fork_choice builds from persisted data synchronously

**Sources.** [grandine@88c82fe7f](https://github.com/grandinetech/grandine/commit/88c82fe7f125)

</details>


<a id="fork_choice-053"></a>
<details>
<summary><b>fork_choice-053</b> Run fork-choice pruning off the head-update path — <i>partial · low · S · latency</i></summary>

**Idea.** Move DAG and fork-choice pruning after finalization out of the head-update path, running it after validator duties at slot end or when the processing queue is idle.

**Gap in Lighthouse.** Prune is gated by prune_threshold but runs inline under the fork-choice write lock right after a head update on finalization. Could be moved to a background task/after proposal duties.

**Impact.** Finalization happens once per epoch; prune is an O(nodes) index rewrite. Saves roughly sub-ms to a few ms of write-lock hold per epoch.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:1278`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1278) after_finalization runs inline in recompute_head
- [`beacon_node/beacon_chain/src/canonical_head.rs:1738`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1738) fork_choice write lock + prune()
- [`consensus/proto_array/src/proto_array.rs:2073`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L2073) maybe_prune has prune_threshold gate

**Sources.** [nimbus#2384](https://github.com/status-im/nimbus-eth2/pull/2384)

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


<a id="fork_choice-055"></a>
<details>
<summary><b>fork_choice-055</b> Pointer-based tree fork-choice store — <i>n/a · low · cpu</i></summary>

**Idea.** Use a node store with parent/children pointers (doubly linked tree) instead of a flat array, avoiding array-index bookkeeping and best-child/descendant updates.

**Impact.** A flat array with a children index already avoids best-child bookkeeping on the hot path; a pointer tree would not obviously be faster in Rust.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array.rs:2073`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L2073) flat nodes Vec plus children Vec&lt;Vec&lt;usize&gt;&gt;

**Sources.** [prysm#11212](https://github.com/OffchainLabs/prysm/pull/11212)

</details>


<a id="fork_choice-056"></a>
<details>
<summary><b>fork_choice-056</b> No tracing spans in per-node fork-choice helpers — <i>implemented · low · S · cpu</i></summary>

**Idea.** Remove tracing/instrumentation spans from hot fork-choice helpers called per node, where span cost exceeds the work.

**Impact.** Spans exist only on per-call entry points (get_head, get_proposer_head, on_block). The per-node proto_array helpers have none.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fork_choice/src/fork_choice.rs:567`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L567)
- [`consensus/fork_choice/src/fork_choice.rs:626`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L626)
- [`consensus/fork_choice/src/fork_choice.rs:785`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L785)

**Skeptic check.** Verified by grep: consensus/proto_array/src has no #[instrument] attributes, and fork_choice.rs has only three per-call spans. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#4808](https://github.com/OffchainLabs/prysm/pull/4808)

</details>


<a id="fork_choice-057"></a>
<details>
<summary><b>fork_choice-057</b> Drop duplicate head events and conversions — <i>implemented · low · S · cpu</i></summary>

**Idea.** Remove duplicate head event emission and redundant type conversions on head payload status updates.

**Impact.** None left: one head_v2 per head change plus one per Empty-&gt;Full change; no bool&lt;-&gt;block conversion round trip exists.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:1208-1215`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1208-L1215) after_new_head only on block-root change
- [`beacon_node/beacon_chain/src/canonical_head.rs:1222-1261`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1222-L1261) second head_v2 only when root same and payload status changed, and only with subscribers
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4593-4685`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4593-L4685) the only other head/head_v2 emission, gated by has_head_subscribers/has_head_v2_subscribers

**Skeptic check.** Verified head and head_v2 are emitted at exactly one site each for a new head, plus a payload-status-change event guarded by root equality. The Nimbus PR fixed a Nimbus-specific duplicate; earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#8903](https://github.com/status-im/nimbus-eth2/pull/8903)

</details>


<a id="fork_choice-058"></a>
<details>
<summary><b>fork_choice-058</b> Clear references on fork-choice prune — <i>n/a · low · memory</i></summary>

**Idea.** When pruning fork-choice nodes, clear their children links so pruned subtrees are freed by the allocator/GC.

**Impact.** Rust has no GC; dropped nodes are freed by ownership.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array.rs:2085`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L2085) split_off drops nodes by ownership

**Sources.** [prysm#11402](https://github.com/OffchainLabs/prysm/pull/11402)

</details>


<a id="fork_choice-059"></a>
<details>
<summary><b>fork_choice-059</b> Common ancestor early exit at finalized head — <i>not · low · S · cpu</i></summary>

**Idea.** In common-ancestor search, return the finalized head immediately when one argument is the finalized head, avoiding a parent walk.

**Gap in Lighthouse.** Add an early return in common_ancestor_slot when one root equals the finalized root. Only helps a metric path on reorgs.

**Impact.** Negligible; called only on reorg for a gauge.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array.rs:2223`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L2223) common_ancestor_slot walks both chains with no finalized shortcut
- [`beacon_node/beacon_chain/src/canonical_head.rs:1062`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1062) sole caller, only for a fast-confirmation metric on reorg

**Sources.** [nimbus#5174](https://github.com/status-im/nimbus-eth2/pull/5174)

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


<a id="fork_choice-061"></a>
<details>
<summary><b>fork_choice-061</b> Early return for unchanged votes in compute_deltas — <i>implemented · low · S · cpu</i></summary>

**Idea.** In fork-choice delta computation, skip a validator whose vote root, slot, payload hint and balance are unchanged before resolving vote nodes, avoiding two lookups per validator in the common case.

**Impact.** Unchanged votes cost only a field comparison; no HashMap lookups.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array_fork_choice.rs:1478-1482`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L1478-L1482) compute_deltas skips indices lookups unless root, balance, payload_present or slot changed
- [`consensus/proto_array/src/proto_array_fork_choice.rs:1415`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L1415) zero-vote skip

**Skeptic check.** Read compute_deltas: the indices.get lookups for current/next root sit inside the changed-vote condition, which matches teku#10604. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#10604](https://github.com/Consensys-Incorporated/teku/pull/10604)

</details>


<a id="fork_choice-062"></a>
<details>
<summary><b>fork_choice-062</b> Short-circuit fork choice on empty proto-array — <i>n/a · low · S · cpu</i></summary>

**Idea.** Return immediately from fork-choice operations when the proto-array is empty.

**Impact.** Nothing; the proto-array is never empty on a running node so the early return would never fire.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array.rs:1255`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L1255) find_head errors JustifiedNodeUnknown if root missing; proto array is seeded with the anchor at construction

**Sources.** [teku#9200](https://github.com/Consensys-Incorporated/teku/pull/9200)

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


<a id="fork_choice-066"></a>
<details>
<summary><b>fork_choice-066</b> Fewer integer divisions in proposer boost — <i>not · low · S · cpu</i></summary>

**Idea.** Compute proposer-boost weight with the simplified formula that avoids unnecessary integer divisions.

**Gap in Lighthouse.** Compute the boost once per find_head (or cache in JustifiedBalances) in calculate_committee_fraction/get_proposer_score; or fold into one mul/div.

**Impact.** Saves two u64 divisions per boosted-node weight evaluation; unmeasurable against the rest of head computation.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array.rs:2391`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L2391) calculate_committee_fraction does two checked_div (by slots_per_epoch, by 100)
- [`consensus/proto_array/src/proto_array.rs:2404`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L2404) get_proposer_score recomputes it per get_weight call (line 1791)

**Sources.** [nimbus#4892](https://github.com/status-im/nimbus-eth2/pull/4892)

</details>


<a id="fork_choice-067"></a>
<details>
<summary><b>fork_choice-067</b> Load state once and pass it down — <i>implemented · low · S · cpu, disk</i></summary>

**Idea.** During fork choice and block processing, fetch the needed state once and pass it to per-validator/per-step helpers instead of re-reading it from the store each time.

**Impact.** No per-validator or per-step store reads in fork choice; balances are cached in the fc store.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fork_choice/src/fork_choice.rs:580-588`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L580-L588) get_head passes cached store.justified_balances() into find_head
- [`consensus/proto_array/src/proto_array.rs:1255-1275`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L1255-L1275) find_head receives balances by reference
- [`consensus/fork_choice/src/fork_choice.rs:791`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L791) on_block takes &amp;BeaconState once

**Skeptic check.** Verified get_head uses cached justified balances and on_block uses the state passed in. This is a generic early-client fix, and Lighthouse's design never re-reads per step.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#2132](https://github.com/Consensys-Incorporated/teku/pull/2132), [prysm#2374](https://github.com/OffchainLabs/prysm/pull/2374), [nimbus#1381](https://github.com/status-im/nimbus-eth2/pull/1381), [nimbus#1350](https://github.com/status-im/nimbus-eth2/pull/1350)

</details>


<a id="fork_choice-068"></a>
<details>
<summary><b>fork_choice-068</b> Native numbers instead of bigint for fork-choice weights — <i>n/a · low · S · cpu</i></summary>

**Idea.** Compute fork-choice vote deltas and weights with native fixed-width numbers (fixed-point where needed) instead of bigint arithmetic, in a tight loop.

**Impact.** Rust already uses native fixed-width integers; no bigint is involved.

**Best measured result.** 10.933ms to 4.471ms per op (pr:lodestar#3270)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array_fork_choice.rs:1387`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L1387) compute_deltas uses native u64/i64 vectors

**Sources.** [lodestar#9804](https://github.com/ChainSafe/lodestar/pull/9804), [lodestar#3270](https://github.com/ChainSafe/lodestar/pull/3270)

</details>


<a id="fork_choice-069"></a>
<details>
<summary><b>fork_choice-069</b> Fixed-size zero-default field instead of Optional — <i>n/a · low · S · memory</i></summary>

**Idea.** Store the execution block hash in each fork-choice node as a fixed 32-byte value with zero default instead of an Optional, cutting per-node overhead.

**Impact.** Rust enum stores the hash inline with no boxing; the JVM Optional overhead does not exist.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array_fork_choice.rs:112`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L112) ExecutionStatus is an enum carrying ExecutionBlockHash by value, no heap Optional

**Sources.** [teku#4681](https://github.com/Consensys-Incorporated/teku/pull/4681)

</details>


<a id="fork_choice-070"></a>
<details>
<summary><b>fork_choice-070</b> Gather all support metrics in one validator pass — <i>implemented · low · S · cpu</i></summary>

**Idea.** Collect attestation support for noncanonical descendants, empty-slot support and equivocating-validator support inside one existing loop over nodes/validators instead of adding separate validator passes.

**Impact.** Empty/full payload support and equivocating support come from the existing single vote pass; no extra validator sweeps.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array_fork_choice.rs:1402-1500`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L1402-L1500) compute_deltas fills delta, empty_delta, full_delta and equivocating_attestation_delta in one loop over votes

**Skeptic check.** Confirmed all per-node support metrics come from the one compute_deltas loop. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#8082](https://github.com/status-im/nimbus-eth2/pull/8082), [nimbus#8026](https://github.com/status-im/nimbus-eth2/pull/8026)

</details>


<a id="fork_choice-071"></a>
<details>
<summary><b>fork_choice-071</b> Run fork choice right before block proposal — <i>implemented · medium · S · latency</i></summary>

**Idea.** Run fork choice just before producing a block so the proposer builds on the latest head without proposal delay.

**Impact.** None needed.

**Best measured result.** no proposal delays seen on testnets (pr:teku#5964)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_production/mod.rs:48`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L48) produce path calls wait_for_fork_choice_before_block_production
- [`beacon_node/beacon_chain/src/block_production/mod.rs:130`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L130) waits for per-slot fork choice with timeout
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7496`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7496) per_slot_task recompute_head_at_current_slot then notify_fork_choice_complete
- [`beacon_node/beacon_chain/src/builder.rs:891`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L891) signal channel always created

**Skeptic check.** Verified the per-slot fork choice run and the producer waiting on it; earlier evidence right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#5964](https://github.com/Consensys-Incorporated/teku/pull/5964)

</details>


<a id="fork_choice-072"></a>
<details>
<summary><b>fork_choice-072</b> Start LMD-GHOST from justified root — <i>implemented · low · S · cpu</i></summary>

**Idea.** Start the head walk from the justified block instead of the current head state, shrinking the set of blocks and votes traversed.

**Impact.** Head walk only covers the subtree under the justified block.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array.rs:1265-1275`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L1265-L1275) find_head resolves justified_index and calls find_head_walk from it
- [`consensus/proto_array/src/proto_array.rs:1448`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L1448) find_head_walk(start_index, ...)

**Skeptic check.** Verified find_head starts at the justified node index. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#2093](https://github.com/OffchainLabs/prysm/pull/2093)

</details>


<a id="fork_choice-073"></a>
<details>
<summary><b>fork_choice-073</b> Run fork choice after each block import — <i>implemented · medium · S · latency</i></summary>

**Idea.** Update head as soon as each block is imported instead of only on the slot tick, so the head is current earlier.

**Impact.** Head is updated immediately after every import path (gossip, RPC, range sync, API), not only on the slot tick.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1008`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1008) recompute_head_at_current_slot after gossip block import
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:207`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L207),289,362,647,658 after RPC/lookup/range imports
- [`beacon_node/http_api/src/publish_blocks.rs:610`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L610) after API-published block
- [`beacon_node/http_api/src/beacon/execution_payload_envelopes.rs:406`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/execution_payload_envelopes.rs#L406) after envelope import

**Skeptic check.** Checked every block import entry point calls recompute_head_at_current_slot afterwards. Earlier evidence was right and complete.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#7387](https://github.com/Consensys-Incorporated/teku/pull/7387)

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

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [prysm#2244](https://github.com/OffchainLabs/prysm/pull/2244)

</details>


<a id="fork_choice-075"></a>
<details>
<summary><b>fork_choice-075</b> Skip eager precompute when consumer unreachable — <i>partial · low · S · cpu, latency</i></summary>

**Idea.** Gate epoch-start eager precomputes (e.g. fast-confirmation FFG) on whether the memoized consumer will actually be called, skipping ~110ms of unused work.

**Gap in Lighthouse.** The FFG sweep (the Prysm case) is lazy. But find_latest_confirmed_descendant builds AttestationScoreCache::for_chain (O(V) aggregate_vote_balances) eagerly, before it checks whether loop1 or loop2 will run and before it checks for an empty chain (head == latest_confirmed_root). Build it lazily (OnceCell) on the first is_one_confirmed call, or return early when the chain is empty.

**Impact.** Saves one O(V) vote aggregation per FCR run on slots where no candidate block exists (e.g. head already confirmed) or both loop gates are closed. FCR is opt-in, so the impact is small.

**Best measured result.** getFFG() took ~110ms on Hoodi at each epoch boundary (pr:prysm#17434)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fast_confirmation/src/optimizations.rs:78-103`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fast_confirmation/src/optimizations.rs#L78-L103) HonestFfgSupportCache is a lazy OnceCell
- [`consensus/fast_confirmation/src/lib.rs:1123`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fast_confirmation/src/lib.rs#L1123),1146 FFG sweep only on get_or_compute
- [`consensus/fast_confirmation/src/lib.rs:590-605`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fast_confirmation/src/lib.rs#L590-L605) AttestationScoreCache::for_chain built eagerly before the loop1/loop2 gates
- [`consensus/fast_confirmation/src/optimizations.rs:252-260`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fast_confirmation/src/optimizations.rs#L252-L260) precompute_chain_attestation_scores always runs the O(V) aggregate_vote_balances
- [`consensus/fast_confirmation/src/lib.rs:505`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fast_confirmation/src/lib.rs#L505) find_latest_confirmed_descendant called with no head==confirmed short-circuit

**Skeptic check.** Earlier evidence was right that the FFG precompute is lazy. It missed that the chain attestation-score precompute in the same function is eager and has no reachability gate.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [prysm#17434](https://github.com/OffchainLabs/prysm/pull/17434)

</details>


<a id="fork_choice-076"></a>
<details>
<summary><b>fork_choice-076</b> Skip auxiliary indexes on forks that never read them — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Do not maintain fork-choice auxiliary indexes (e.g. a future-fork indexed weight store) per attestation on fork versions that never read them.

**Impact.** No per-attestation future-fork index maintenance exists; the Caplin regression cannot occur.

**Best measured result.** Hoodi: CPU ~7.5% -&gt; &lt;2%; profile samples 148.9% -&gt; 41.6%; stale head at deadline 64% -&gt; 4% (pr:caplin#21698)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array_fork_choice.rs:693-709`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L693-L709) process_attestation writes only the VoteTracker next_* fields, no secondary index or allocation
- [`consensus/proto_array/src/proto_array_fork_choice.rs:711-730`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L711-L730) PTC votes go to node bitfields only via process_payload_attestation
- [`consensus/proto_array/src/proto_array.rs:389-437`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L389-L437) pre-Gloas the only Gloas-only work is an i64 add/sub of empty/full deltas for changed votes, in compute_deltas

**Skeptic check.** Verified the per-attestation path has no auxiliary index. Pre-Gloas, the empty/full delta accounting runs only for changed votes in compute_deltas, costs a few integer ops and allocates nothing, so it is not the same cost.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#21698](https://github.com/erigontech/erigon/pull/21698)

</details>


<a id="fork_choice-077"></a>
<details>
<summary><b>fork_choice-077</b> Ignore pre-genesis ticks — <i>implemented · low · S · cpu</i></summary>

**Idea.** Guard the tick catch-up loop against times before genesis so unsigned wrap-around does not spin a core.

**Impact.** No pre-genesis spin possible.

**Best measured result.** about one CPU core kept busy (pr:caplin#24680)

**Evidence (Lighthouse @ 928b61e719).**

- [`common/slot_clock/src/manual_slot_clock.rs:117`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/slot_clock/src/manual_slot_clock.rs#L117) slot_of returns None before genesis
- [`beacon_node/beacon_chain/src/beacon_chain.rs:767`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L767) chain.slot() errors pre-genesis
- [`consensus/fork_choice/src/fork_choice.rs:1502`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1502) update_time loops only while store slot &lt; current_slot

**Skeptic check.** Confirmed the clock yields no slot before genesis, so the tick loop never sees a wrapped value; earlier evidence right.

**Verdict history.** implemented (checked) → implemented (skeptic)

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

**Impact.** None needed; attestation production reads the cached head and the early attester cache, not the FCU result.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:1165-1198`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1165-L1198) cached head written before any EL call
- [`beacon_node/beacon_chain/src/canonical_head.rs:1296`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1296) spawn_execution_layer_updates spawns FCU as a separate task
- [`beacon_node/beacon_chain/src/canonical_head.rs:1886-1935`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1886-L1935) FCU and prepare_beacon_proposer run in the spawned task
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4554-4700`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4554-L4700) early_attester_cache filled during import, before recompute_head

**Skeptic check.** Verified that recompute_head_at_slot_internal updates the cached head and then spawns FCU. The caller of recompute_head_at_slot awaits the FCU handle, but attesters do not, so the earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

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


<a id="fork_choice-081"></a>
<details>
<summary><b>fork_choice-081</b> Hoist zero-hash comparison out of balance loop — <i>implemented · low · S · cpu</i></summary>

**Idea.** In fork-choice balance updates, compute loop-invariant comparisons (zero-hash checks) once per update instead of per validator.

**Impact.** None: Hash256::zero() is a compile-time constant, so there is no per-validator config lookup to hoist.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array_fork_choice.rs:1412-1417`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L1412-L1417)
- [`consensus/proto_array/src/proto_array.rs:497`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L497)

**Skeptic check.** Prysm #12458 hoisted params.BeaconConfig().ZeroHash, a config getter, out of the per-vote loop. In compute_deltas Lighthouse compares against the constant Hash256::zero(), so the cost Prysm removed does not exist here. The earlier verdict is upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#12458](https://github.com/OffchainLabs/prysm/pull/12458)

</details>


<a id="fork_choice-082"></a>
<details>
<summary><b>fork_choice-082</b> Hoist proposer boost out of per-node score loop — <i>implemented · low · S · cpu</i></summary>

**Idea.** In proto-array score application, compute the proposer-boost root/score once before the per-node loop since its inputs are loop-invariant.

**Impact.** None on the all-nodes pass. get_proposer_score is still called for each supporting child during the head walk, but it only reads the cached total balance and runs for a few children.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array.rs:487-510`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L487-L510)
- [`consensus/proto_array/src/proto_array.rs:1477-1479`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L1477-L1479)
- [`consensus/proto_array/src/proto_array.rs:1765-1795`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L1765-L1795)
- [`consensus/proto_array/src/proto_array.rs:2404-2410`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L2404-L2410)

**Skeptic check.** apply_score_changes does not touch proposer boost. should_apply_proposer_boost runs once per find_head_walk, before the loop. The only work left per child in the head walk is is_supporting_vote plus a cheap calculate_committee_fraction, so the earlier verdict is upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#9040](https://github.com/ChainSafe/lodestar/pull/9040), [lighthouse#4585](https://github.com/sigp/lighthouse/pull/4585)

</details>


<a id="fork_choice-083"></a>
<details>
<summary><b>fork_choice-083</b> Keep latest votes in memory, not per-vote DB writes — <i>implemented · low · S · disk, cpu</i></summary>

**Idea.** Keep validators' latest fork-choice votes in an in-memory structure instead of writing each vote to the database.

**Impact.** None: there are no per-vote DB writes.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array_fork_choice.rs:27-34`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L27-L34)
- [`consensus/proto_array/src/proto_array_fork_choice.rs:693-709`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L693-L709)
- [`consensus/proto_array/src/ssz_container.rs:5`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/ssz_container.rs#L5),72

**Skeptic check.** Votes live in an in-memory ElasticList&lt;VoteTracker&gt;. They reach disk only inside the whole persisted fork-choice container, so the earlier verdict is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#4102](https://github.com/OffchainLabs/prysm/pull/4102)

</details>


<a id="fork_choice-084"></a>
<details>
<summary><b>fork_choice-084</b> Integer instead of float for weight changes — <i>implemented · low · S · cpu</i></summary>

**Idea.** Apply fork-choice weight changes with integer arithmetic instead of floating point.

**Impact.** None: there is no floating point anywhere in the weight arithmetic.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array_fork_choice.rs:1387-1500`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L1387-L1500)
- [`consensus/proto_array/src/proto_array.rs:2413-2423`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L2413-L2423)

**Skeptic check.** Deltas are i64 and are applied with checked integer arithmetic in apply_delta. Weights are u64. The earlier verdict is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#9438](https://github.com/OffchainLabs/prysm/pull/9438)

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


<a id="fork_choice-086"></a>
<details>
<summary><b>fork_choice-086</b> Iterative weight propagation instead of recursion — <i>implemented · low · S · cpu</i></summary>

**Idea.** Propagate fork-choice weight changes up the DAG with a backward loop instead of recursion, avoiding call overhead and stack growth on long chains.

**Impact.** None: propagation is one reverse linear pass with no recursion.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array.rs:487-488`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L487-L488)

**Skeptic check.** apply_score_changes walks the node indices in reverse and pushes each node's delta to its parent's delta (backprop_delta). This is the iterative scheme the idea describes, so the earlier verdict is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@fcbc7d84e](https://github.com/ChainSafe/lodestar/commit/fcbc7d84e748), [lodestar#1495](https://github.com/ChainSafe/lodestar/pull/1495)

</details>


<a id="fork_choice-087"></a>
<details>
<summary><b>fork_choice-087</b> Key-only iteration skipping signature payloads — <i>n/a · low · cpu, disk</i></summary>

**Idea.** When computing the per-slot safe target, iterate stored keys only without deserialising large signature/proof values, and batch per-block inserts into one write batch.

**Impact.** This is the leanSpec/ethlambda store design (per-slot safe target over stored signatures); Lighthouse has no such per-slot key-value scan.

**Best measured result.** Runs every slot and scales with validator count (no numbers) (pr:ethlambda#174)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array_fork_choice.rs:693`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L693) votes held in memory, no signature/proof store
- [`consensus/fast_confirmation/src/lib.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fast_confirmation/src/lib.rs) FCR works on VoteTracker in memory

**Sources.** [ethlambda#174](https://github.com/lambdaclass/ethlambda/pull/174)

</details>


<a id="fork_choice-088"></a>
<details>
<summary><b>fork_choice-088</b> Proposer re-org of late weak heads with fcU override — <i>implemented · low · S · latency</i></summary>

**Idea.** Track block timeliness and implement get_proposer_head so a proposer builds on the parent of a late, weak head, and should_override_forkchoice_update in all import paths so the late block is not sent to the EL as head. Run head processing early enough that the re-orging block is head before attestation deadlines.

**Impact.** Already done.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_production/mod.rs:205-229`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L205-L229) get_proposer_head in block production
- [`consensus/proto_array/src/proto_array_fork_choice.rs:823`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L823),875 get_proposer_head / get_proposer_head_info
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5500`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5500),5517 overridden_forkchoice_update_params
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7194`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7194) override applied in update_execution_engine_forkchoice
- [`beacon_node/beacon_chain/src/canonical_head.rs:1913`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1913) every head-change FCU passes OverrideForkchoiceUpdate::Yes
- [`consensus/fork_choice/src/fork_choice.rs:883-890`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L883-L890) block timeliness tracked

**Skeptic check.** Confirmed that proposer re-orgs and the fcU override exist. All FCU calls from recompute_head go through the override, so the earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#11981](https://github.com/OffchainLabs/prysm/pull/11981), [prysm#12146](https://github.com/OffchainLabs/prysm/pull/12146), [prysm#12034](https://github.com/OffchainLabs/prysm/pull/12034), [teku#9247](https://github.com/Consensys-Incorporated/teku/pull/9247), [prysm#12022](https://github.com/OffchainLabs/prysm/pull/12022), [lodestar#6581](https://github.com/ChainSafe/lodestar/pull/6581)

</details>


<a id="fork_choice-089"></a>
<details>
<summary><b>fork_choice-089</b> Lazy head state update with in-memory block graph — <i>implemented · low · S · cpu</i></summary>

**Idea.** Keep an in-memory block graph and update the head state lazily rather than on every block.

**Impact.** None: justified balances are rebuilt only when the justified checkpoint changes, and the head snapshot is swapped only when the head changes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_fork_choice_store.rs:341-370`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_fork_choice_store.rs#L341-L370)
- [`beacon_node/beacon_chain/src/beacon_fork_choice_store.rs:313-315`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_fork_choice_store.rs#L313-L315)
- [`consensus/fork_choice/src/fork_choice.rs:579-587`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L579-L587)
- [`beacon_node/beacon_chain/src/canonical_head.rs:284`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L284)

**Skeptic check.** The source Prysm PR #11513 fetches justified balances only when the justified checkpoint changes. Lighthouse does this in set_justified_checkpoint, which uses balances_cache or rebuilds JustifiedBalances once, and find_head reuses the stored value. The earlier evidence cited CachedHead, which is related but not the mechanism. The verdict still holds.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#11513](https://github.com/OffchainLabs/prysm/pull/11513)

</details>


<a id="fork_choice-090"></a>
<details>
<summary><b>fork_choice-090</b> Small refillable ancestor root buffer — <i>partial · low · M · memory, disk</i></summary>

**Idea.** Walk ancestors with a small fixed-length buffer of recent block/state roots refilled when exhausted, instead of holding a whole BeaconState; doubles as an in-memory root cache cutting DB reads.

**Gap in Lighthouse.** RootsIterator (and BlockRootsIterator/StateRootsIterator built on it) still holds a whole BeaconState in a Cow. When its root vectors run out, it loads another full state with next_historical_root_backtrack_state, and RootsIterator::from_block loads a full state just to start. No lean iterator exists that keeps only a short buffer of roots. PR #725, which proposed one (LeanReverseAncestorIterator), was closed unmerged.

**Impact.** Small. Fork-choice ancestor lookups use proto_array, and the freezer has root columns. Reverse walks across more than 8192 slots in the hot DB, and from_block calls, still load full states.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/iter.rs:150-154`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/iter.rs#L150-L154)
- [`beacon_node/store/src/iter.rs:197-232`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/iter.rs#L197-L232)
- [`beacon_node/store/src/iter.rs:183-195`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/iter.rs#L183-L195)

**Skeptic check.** The earlier evidence said the idea had "already landed", but PR #725 was closed unmerged. Current RootsIterator does what the idea replaces: it holds and reloads full BeaconStates rather than a small refillable root buffer. Milhouse sharing makes holding a state cheap, but each refill is still a full state load from the DB.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lighthouse#725](https://github.com/sigp/lighthouse/pull/725)

</details>


<a id="fork_choice-091"></a>
<details>
<summary><b>fork_choice-091</b> Lightweight vote target record in LMD-GHOST — <i>implemented · low · S · cpu</i></summary>

**Idea.** Count LMD-GHOST votes using a small (root, slot) target record instead of full block objects, avoiding repeated hashing and deep equality comparisons.

**Impact.** None needed.

**Best measured result.** fork choice was 2 to 3 seconds (pr:prysm#2333)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array_fork_choice.rs:27-34`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L27-L34) VoteTracker is (root, slot, payload_present) only

**Skeptic check.** VoteTracker holds only roots, slots and bools, and proto-array uses index deltas. No block objects are hashed or compared.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#2333](https://github.com/OffchainLabs/prysm/pull/2333)

</details>


<a id="fork_choice-092"></a>
<details>
<summary><b>fork_choice-092</b> No fork choice lock across validation and newPayload — <i>implemented · medium · S · latency</i></summary>

**Idea.** During block import, do not hold the fork choice write lock across consensus validation and the blocking EL newPayload call; reacquire it afterwards, re-check admission and handle invalid payloads then. Attestations, head computation and ticks are then not stalled by validation or EL latency, and CL and EL validation run in parallel.

**Impact.** None needed for validation/EL latency.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1530-1564`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1530-L1564) newPayload spawned as payload_verification_handle in parallel with consensus validation, without a fork choice lock
- [`beacon_node/beacon_chain/src/block_verification.rs:1755`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1755) write lock held only briefly for block attestations
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4508-4518`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4508-L4518) upgradable read then write lock taken only in import_block, after verification
- [`beacon_node/beacon_chain/src/payload_envelope_verification/import.rs:454`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/import.rs#L454) Gloas envelope newPayload awaited before import_execution_payload_envelope takes the lock (:259)

**Skeptic check.** Confirmed that no EL call runs under the fork choice lock on the block or envelope paths. Separately, import_block keeps the write lock through the block/state DB write (beacon_chain.rs:4757-4770) by design; that is a different idea from this one.

**Verdict history.** implemented (checked) → implemented (skeptic)

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


<a id="fork_choice-094"></a>
<details>
<summary><b>fork_choice-094</b> Reduced-tree LMD-GHOST tracking only branching nodes — <i>n/a · low · S · cpu, latency</i></summary>

**Idea.** Keep a reduced tree rooted at the finalized block that holds only branch points and latest votes, updated incrementally, so a head query does not walk full chain history.

**Impact.** Reduced tree was replaced by proto-array, which gives O(nodes) head with cached best_descendant.

**Best measured result.** None (pr:lighthouse#398)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array.rs:613`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L613) on_block flat node array
- [`consensus/proto_array/src/proto_array.rs:476`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L476) apply_score_changes

**Sources.** [lighthouse@f4621a9f1](https://github.com/sigp/lighthouse/commit/f4621a9f1ae6), [lighthouse#398](https://github.com/sigp/lighthouse/pull/398)

</details>


<a id="fork_choice-095"></a>
<details>
<summary><b>fork_choice-095</b> On block insert, update only parent&#x27;s best child — <i>implemented · low · S · cpu</i></summary>

**Idea.** When inserting a block into proto-array, re-evaluate best child and best descendant only for the direct parent instead of walking the full ancestor chain, since only the parent's best child can change on insert.

**Impact.** None: insert is O(1) apart from the execution-status walk, which stops early.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array.rs:613-790`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L613-L790)
- [`consensus/proto_array/src/proto_array.rs:990-1030`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L990-L1030)
- [`consensus/proto_array/src/proto_array.rs:1448-1520`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L1448-L1520)

**Skeptic check.** on_block pushes the node, appends it to the parent's children index, and only walks ancestors in propagate_execution_payload_validation_from, which stops at the first Valid ancestor. It never recomputes best child or descendant up the chain, because the head is found by a top-down walk in find_head_walk. The earlier verdict is upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#5580](https://github.com/ChainSafe/lodestar/pull/5580)

</details>


<a id="fork_choice-096"></a>
<details>
<summary><b>fork_choice-096</b> Use parking_lot locks for the block graph — <i>implemented · low · S · cpu</i></summary>

**Idea.** Guard fork choice / block graph state with parking_lot locks instead of std locks: smaller, faster, and no poisoning.

**Impact.** None; fork choice is already behind parking_lot locks.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:65`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L65)

**Skeptic check.** canonical_head.rs imports parking_lot Mutex/RwLock (incl. upgradable guards) for the fork choice lock; grep finds std::sync Mutex only in test files of beacon_chain and fork_choice. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@1e6f85a5e](https://github.com/sigp/lighthouse/commit/1e6f85a5eb5d)

</details>


<a id="fork_choice-097"></a>
<details>
<summary><b>fork_choice-097</b> Read locks for read-only fork choice paths — <i>implemented · low · S · latency, cpu</i></summary>

**Idea.** Take a shared read lock instead of an exclusive write lock for fork choice operations that only read (head computation, proposer boost getters, latest-message queries, invalidation checks whose write takes its own lock), so concurrent readers do not serialize.

**Impact.** None needed.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:650`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L650) fork_choice_read_lock for readers
- [`beacon_node/beacon_chain/src/canonical_head.rs:862-870`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L862-L870) write lock for get_head (mutates scores), then downgraded to read
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2378`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2378),2578,2943,6624,7278 write lock only for on_* mutations
- [`beacon_node/beacon_chain/src/execution_proof_verification/mod.rs:122`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/execution_proof_verification/mod.rs#L122) write lock for on_valid_execution_payload_by_block_root (mutating)

**Skeptic check.** Checked every non-test fork_choice_write_lock() call: each one mutates fork choice. get_head applies vote deltas, so it needs the write lock, and it is downgraded to a read lock right after.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#15648](https://github.com/OffchainLabs/prysm/pull/15648), [prysm#4784](https://github.com/OffchainLabs/prysm/pull/4784), [prysm#11172](https://github.com/OffchainLabs/prysm/pull/11172), [lighthouse@0d4b58978](https://github.com/sigp/lighthouse/commit/0d4b58978ccd)

</details>


<a id="fork_choice-098"></a>
<details>
<summary><b>fork_choice-098</b> Split fork choice locks by independent fields — <i>not · low · M · latency, cpu</i></summary>

**Idea.** Give independent fork choice data (e.g. vote updates vs store/time fields) their own locks, so heavy vote score application does not block cheap getters used by ticks and gossip.

**Gap in Lighthouse.** Move queued_attestations/vote intake and time/checkpoint getters out of the ForkChoice struct behind their own locks (ForkChoice::on_attestation, update_time, BeaconChain::apply_attestation_to_fork_choice).

**Impact.** Head is already served from a separate cached_head lock, so the contended readers are few; gain is shorter write-lock waits during gossip attestation bursts, small.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:458`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L458) single RwLock&lt;BeaconForkChoice&gt;
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2578`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2578) apply_attestation_to_fork_choice takes fork_choice_write_lock
- [`consensus/fork_choice/src/fork_choice.rs:371`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L371) queued_attestations inside same struct

**Sources.** [prysm#7634](https://github.com/OffchainLabs/prysm/pull/7634), [teku#6245](https://github.com/Consensys-Incorporated/teku/pull/6245)

</details>


<a id="fork_choice-099"></a>
<details>
<summary><b>fork_choice-099</b> Simplify fork choice locking and attestation caches — <i>n/a · low · S · cpu, latency</i></summary>

**Idea.** Simplify fork choice locking and its caches (e.g. attestation indices cache) to reduce contention between gossip, block import and API paths.

**Impact.** Caplin-specific attestation indices cache; Lighthouse derives indices before the lock and has no such cache in fork choice.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fork_choice/src/fork_choice.rs:1325`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1325) on_attestation takes an already-built IndexedAttestation

**Sources.** [caplin#9445](https://github.com/erigontech/erigon/pull/9445)

</details>


<a id="fork_choice-100"></a>
<details>
<summary><b>fork_choice-100</b> Run fork choice on a dedicated single-thread executor — <i>n/a · low · S · latency, cpu</i></summary>

**Idea.** Serialize fork choice tasks on one dedicated thread instead of guarding them with a lock, so worker-pool threads never block waiting for fork choice.

**Impact.** Recompute is already serialized and runs on the blocking pool, so async workers do not wait on the lock; the JVM executor design does not map.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:467`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L467) recompute_head_lock Mutex serializes recompute
- [`beacon_node/beacon_chain/src/canonical_head.rs:787`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L787) spawn_blocking_handle runs it off async workers

**Sources.** [teku#2644](https://github.com/Consensys-Incorporated/teku/pull/2644)

</details>


<a id="fork_choice-101"></a>
<details>
<summary><b>fork_choice-101</b> Pause fast-confirmation rule while syncing — <i>n/a · low · cpu, sync</i></summary>

**Idea.** Pause the per-slot fast-confirmation computation while far behind head, pinning the confirmed root to finalized, and resume once synced, to skip pointless work during long-range sync.

**Impact.** No fast confirmation rule exists in Lighthouse; nothing to pause.

**Evidence (Lighthouse @ 928b61e719).**

- grep for fast confirmation in beacon_node/consensus: none

**Sources.** [lodestar#9681](https://github.com/ChainSafe/lodestar/pull/9681), [lodestar#8363](https://github.com/ChainSafe/lodestar/pull/8363)

</details>


<a id="fork_choice-102"></a>
<details>
<summary><b>fork_choice-102</b> Store epoch-boundary target pointer in each node — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Keep a pointer/index to the epoch-boundary target node in each fork choice node so the checkpoint target root of a block is O(1) instead of walking ancestors during attestation verification.

**Impact.** None; target root per attestation is an O(1) field read.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array.rs:100`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L100)
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1379-1425`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1379-L1425)
- [`beacon_node/beacon_chain/src/attestation_verification.rs:643`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L643)
- [`beacon_node/beacon_chain/src/attestation_verification.rs:975`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L975)
- [`consensus/fork_choice/src/fork_choice.rs:1223`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1223)

**Skeptic check.** Each ProtoNode stores target_root (a hash, not an index, but same O(1) effect); verify_attestation_target_root on both unaggregated and aggregate gossip paths and validate_on_attestation read it without an ancestor walk. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#13249](https://github.com/OffchainLabs/prysm/pull/13249)

</details>


<a id="fork_choice-103"></a>
<details>
<summary><b>fork_choice-103</b> Keep updating head during sync so pruning proceeds — <i>implemented · medium · S · memory, sync, cpu</i></summary>

**Idea.** While importing blocks during sync, still run head selection regularly (per block or at epoch boundaries, with events coalesced) so finalization pruning proceeds and the non-finalized block pool does not grow unbounded.

**Impact.** None needed.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:646-648`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L646-L648),657-659 recompute_head after every chain segment, on success and on partial failure
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:207`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L207),289,362 recompute_head after RPC/lookup blocks
- [`beacon_node/beacon_chain/src/canonical_head.rs:1700-1738`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1700-L1738) after_finalization prunes op pool and fork choice

**Skeptic check.** Range sync recomputes the head once per batch (1-2 epochs), so finalization and pruning keep pace during sync.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#3055](https://github.com/Consensys-Incorporated/teku/pull/3055), [nimbus@4e85b50cb](https://github.com/status-im/nimbus-eth2/commit/4e85b50cb6c4)

</details>


<a id="fork_choice-104"></a>
<details>
<summary><b>fork_choice-104</b> Skip per-slot fork choice runs while far behind — <i>implemented · medium · S · cpu, latency, sync</i></summary>

**Idea.** Skip the per-slot and state-advance fork choice runs when the head is far behind the wall clock (e.g. more than 256 slots), so range sync is not interrupted by redundant, racing fork choice calls.

**Impact.** None; both timer-driven fork choice runs skip when head is &gt;256 slots behind.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:45`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L45)
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:205-212`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L205-L212)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:195`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L195)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7490-7496`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7490-L7496)

**Skeptic check.** Verified the state-advance fork choice (recompute_head_at_slot(next_slot)) and per_slot_task recompute_head_at_current_slot both return early when best_slot+256 &lt; slot; remaining recompute calls are event-driven (block import), which the idea does not target. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#3217](https://github.com/sigp/lighthouse/pull/3217), [lighthouse#3487](https://github.com/sigp/lighthouse/pull/3487)

</details>


<a id="fork_choice-105"></a>
<details>
<summary><b>fork_choice-105</b> Skip periodic fork choice pass when attestation pool empty — <i>not · low · S · cpu, sync</i></summary>

**Idea.** While syncing, skip the periodic fork choice attestation processing and head update when the fork choice attestation pool is empty.

**Gap in Lighthouse.** Add a dirty flag in ProtoArrayForkChoice (set when process_attestation/queued dequeue/balances/boost change) and return the cached head from get_head/find_head when clean, mainly useful in sync.

**Impact.** Saves a full compute_deltas over ~1M votes plus node_slots collect per redundant run; only matters when runs happen without new votes, mostly near-head sync, so marginal.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:834-865`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L834-L865) recompute_head always calls get_head
- [`consensus/proto_array/src/proto_array_fork_choice.rs:769-794`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L769-L794),1387-1412 find_head always runs compute_deltas over all votes with no dirty check
- [`consensus/fork_choice/src/fork_choice.rs:309-316`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L309-L316) queued attestations only dequeued by slot

**Sources.** [prysm#8436](https://github.com/OffchainLabs/prysm/pull/8436)

</details>


<a id="fork_choice-106"></a>
<details>
<summary><b>fork_choice-106</b> Skip block-tree cache updates during sync import — <i>n/a · low · cpu, sync</i></summary>

**Idea.** During sync-time block import that does not compute the head, skip updating auxiliary fork choice caches such as the filtered block tree cache.

**Impact.** Lighthouse has no filtered block tree cache; proto-array filters viability during head search.

**Evidence (Lighthouse @ 928b61e719).**

- no filtered block tree cache in [`consensus/proto_array`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array) or fork_choice

**Sources.** [prysm#4541](https://github.com/OffchainLabs/prysm/pull/4541)

</details>


<a id="fork_choice-107"></a>
<details>
<summary><b>fork_choice-107</b> Memoize total active balance in fast confirmation — <i>n/a · low · cpu, latency</i></summary>

**Idea.** Within one fast-confirmation run, memoize the total active balance per balance source instead of recomputing it with a full validator scan several times per block evaluation.

**Impact.** Feature absent, so nothing to memoize.

**Best measured result.** None (pr:lodestar#9572)

**Evidence (Lighthouse @ 928b61e719).**

- no fast confirmation rule in Lighthouse

**Sources.** [lodestar#9572](https://github.com/ChainSafe/lodestar/pull/9572)

</details>


<a id="fork_choice-108"></a>
<details>
<summary><b>fork_choice-108</b> Persist fork choice snapshot for fast restart — <i>implemented · medium · S · startup, disk</i></summary>

**Idea.** Persist the proto-array and vote snapshot to disk (e.g. each epoch) and reload it at startup instead of rebuilding fork choice by replaying stored blocks.

**Impact.** None needed.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:1564-1566`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1564-L1566) persist_fork_choice on epoch transition or reorg
- [`beacon_node/beacon_chain/src/canonical_head.rs:1720`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1720) persist on finalization
- [`beacon_node/beacon_chain/src/canonical_head.rs:1746`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1746) persist_fork_choice
- [`beacon_node/beacon_chain/src/beacon_chain.rs:8466`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L8466) persist on Drop/shutdown
- [`beacon_node/beacon_chain/src/beacon_chain.rs:692-715`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L692-L715) load_fork_choice decodes persisted proto-array at startup
- [`beacon_node/beacon_chain/src/builder.rs:245`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L245) builder uses load_fork_choice

**Skeptic check.** Fork choice (proto-array and votes) is persisted each epoch, on finalization and on shutdown, and reloaded at startup without replaying blocks.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#2270](https://github.com/Consensys-Incorporated/teku/pull/2270), [teku#1627](https://github.com/Consensys-Incorporated/teku/pull/1627), [teku#2319](https://github.com/Consensys-Incorporated/teku/pull/2319)

</details>


<a id="fork_choice-109"></a>
<details>
<summary><b>fork_choice-109</b> Rebuild proto-array at startup from stored block metadata — <i>implemented · low · S · startup, disk</i></summary>

**Idea.** Persist checkpoint epochs with each hot block's metadata and rebuild proto-array at startup from that metadata, using views without copying, instead of loading snapshots and regenerating states.

**Impact.** No startup speed to gain: Lighthouse never regenerates per-block states at load.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:692-715`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L692-L715) load_fork_choice decodes the whole PersistedForkChoice (proto-array nodes with checkpoints)
- [`beacon_node/beacon_chain/src/beacon_fork_choice_store.rs:212`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_fork_choice_store.rs#L212) from_persisted loads only the justified state
- [`beacon_node/beacon_chain/src/canonical_head.rs:1746`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1746) persist_fork_choice

**Skeptic check.** The goal of Teku#3124 (no state regeneration for blocks missing from a snapshot at startup) is met, but by a different mechanism: Lighthouse persists proto-array nodes that already carry the checkpoints and loads them directly. It does not rebuild from block metadata. Value lowered to low because nothing measurable remains.

**Verdict history.** implemented (checked) → implemented (skeptic)

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

**Sources.** [teku#2178](https://github.com/Consensys-Incorporated/teku/pull/2178), [prysm#4749](https://github.com/OffchainLabs/prysm/pull/4749)

</details>


<a id="fork_choice-111"></a>
<details>
<summary><b>fork_choice-111</b> Primitive-valued maps for fork choice indices — <i>n/a · low · memory, cpu</i></summary>

**Idea.** Use primitive-valued maps for proto-array root-to-index and pubkey-to-index lookups instead of maps of boxed integers, cutting memory and allocation.

**Impact.** Rust maps already store primitive values inline.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array_fork_choice.rs:1388`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L1388) indices: HashMap&lt;Hash256, usize&gt;; plain Rust values, no boxing

**Sources.** [teku#5012](https://github.com/Consensys-Incorporated/teku/pull/5012)

</details>


<a id="fork_choice-112"></a>
<details>
<summary><b>fork_choice-112</b> Store checkpoints as plain structs in fork choice — <i>n/a · low · memory</i></summary>

**Idea.** Convert tree-backed SSZ checkpoint objects held by fork choice into plain structs so they do not retain merkle subtrees.

**Impact.** Checkpoints in fork choice are plain structs with no merkle subtree retention.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array.rs:109-111`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L109-L111) Checkpoint stored as plain Copy struct

**Sources.** [lodestar#2292](https://github.com/ChainSafe/lodestar/pull/2292)

</details>


<a id="fork_choice-113"></a>
<details>
<summary><b>fork_choice-113</b> Pre-aggregate attestations before fork choice — <i>n/a · low · S · cpu</i></summary>

**Idea.** Aggregate attestations before feeding them to fork choice to reduce the number of distinct entries processed.

**Impact.** Fork choice stores one vote per validator, so aggregating first would not reduce entries processed.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2573`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2573) apply_attestation_to_fork_choice applies each verified attestation directly
- [`consensus/proto_array/src/proto_array_fork_choice.rs:693`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L693) process_attestation is an O(1) write to a per-validator vote slot

**Sources.** [prysm#4820](https://github.com/OffchainLabs/prysm/pull/4820)

</details>


<a id="fork_choice-114"></a>
<details>
<summary><b>fork_choice-114</b> Prewarm next justified checkpoint balances — <i>implemented · low · S · latency, cpu</i></summary>

**Idea.** Before the epoch boundary (tick handler or last slot of epoch), compute the next justified checkpoint state's active balances in the background and coalesce concurrent misses, so the first head computation after justification hits the cache instead of stalling.

**Impact.** Justification changes normally hit the cache; the stall the other clients measured comes from a miss, which Lighthouse avoids by filling the cache at import. A miss is still possible after a restart (the cache is not persisted) or after 4+ boundaries evict the entry.

**Best measured result.** None (pr:caplin#23981)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_fork_choice_store.rs:259`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_fork_choice_store.rs#L259) on_verified_block caches JustifiedBalances for each epoch-boundary block, loading the boundary state if the boundary slot was skipped
- [`beacon_node/beacon_chain/src/beacon_fork_choice_store.rs:345`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_fork_choice_store.rs#L345) set_justified_checkpoint hits balances_cache before any get_hot_state
- [`beacon_node/beacon_chain/src/beacon_fork_choice_store.rs:49`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_fork_choice_store.rs#L49) MAX_BALANCE_CACHE_SIZE=4

**Skeptic check.** Verified: balances are computed at boundary-block import, including the skipped-boundary case, and set_justified_checkpoint reads them from the cache. The work is done during import, not in the background, but the effect on the first head computation after justification is the same; the earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#6046](https://github.com/Consensys-Incorporated/teku/pull/6046), [caplin#23981](https://github.com/erigontech/erigon/pull/23981), [prysm#17463](https://github.com/OffchainLabs/prysm/pull/17463)

</details>


<a id="fork_choice-115"></a>
<details>
<summary><b>fork_choice-115</b> Diff justified balances to reweight only changed validators — <i>partial · low · M · cpu, latency</i></summary>

**Idea.** When installing a new justified checkpoint, diff its precomputed effective balances against the applied ones and reweight only validators whose balance changed, instead of sweeping all votes.

**Gap in Lighthouse.** Balances are diffed per validator inside compute_deltas, but it sweeps every validator on each find_head and the justified-change path does a full slice compare plus clone. Add a changed-index list so compute_deltas visits only changed validators plus those with pending votes.

**Impact.** The find_head sweep over ~1M votes could shrink to touched validators; a few ms per slot at most.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array_fork_choice.rs:802`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L802) old_balances != new_balances full compare then clone
- [`consensus/proto_array/src/proto_array_fork_choice.rs:1388`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L1388) compute_deltas iterates all votes on every call

**Sources.** [silver#290](https://github.com/gattaca-com/silver/pull/290)

</details>


<a id="fork_choice-116"></a>
<details>
<summary><b>fork_choice-116</b> Preload post-finalized blocks into fork choice at startup — <i>implemented · low · S · latency, cpu</i></summary>

**Idea.** On startup, load post-finalized blocks into the in-memory fork choice store so ancestor lookups for early attestations hit memory instead of the DB.

**Impact.** None; all non-finalized blocks are in the in-memory proto-array from startup.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:692`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L692)
- [`consensus/proto_array/src/ssz_container.rs:29`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/ssz_container.rs#L29)
- [`consensus/fork_choice/src/fork_choice.rs:1956`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1956)

**Skeptic check.** Lighthouse persists and reloads the whole proto-array (all post-finalized nodes) at startup, so ancestor/target lookups for attestations are memory-only. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#7665](https://github.com/OffchainLabs/prysm/pull/7665)

</details>


<a id="fork_choice-117"></a>
<details>
<summary><b>fork_choice-117</b> Precollect ancestor structure in one pass for O(1) checks — <i>not · low · M · cpu</i></summary>

**Idea.** Pre-process the recent chain once, collecting bounded slot-indexed ancestor data, then answer per-block checks with O(1) accessors instead of repeated is_ancestor/get_ancestor loops.

**Gap in Lighthouse.** Ancestor checks walk parent pointers each time. Precollect a bounded slot-indexed ancestor array and use it in get_ancestor_node and is_finalized_checkpoint_or_descendant.

**Impact.** Small gain; walks are short and nodes sit contiguously in a Vec.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array.rs:1837`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L1837) get_ancestor_node walks parent links per call
- [`consensus/proto_array/src/proto_array.rs:2251`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L2251) is_finalized_checkpoint_or_descendant walks nodes per call

**Sources.** [nimbus#8121](https://github.com/status-im/nimbus-eth2/pull/8121), [nimbus#8011](https://github.com/status-im/nimbus-eth2/pull/8011)

</details>


<a id="fork_choice-118"></a>
<details>
<summary><b>fork_choice-118</b> Progressive balances cache for unrealized justification — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Maintain running current/previous-epoch target-attesting balances in the state and use them for unrealized justification and viability in fork choice, instead of scanning participation arrays per imported block.

**Impact.** Unrealized justification per block is O(1) on balances.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fork_choice/src/fork_choice.rs:946`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L946) on_block calls altair::process_justification_and_finalization (skipped entirely when parent checkpoints can be reused)
- [`consensus/state_processing/src/per_epoch_processing/altair/justification_and_finalization.rs:9`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/altair/justification_and_finalization.rs#L9) reads previous/current target attesting balances from progressive_balances_cache, no participation scan
- [`consensus/state_processing/src/per_block_processing.rs:143`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing.rs#L143) initialize_progressive_balances_cache
- [`consensus/state_processing/src/common/update_progressive_balances_cache.rs:92`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/update_progressive_balances_cache.rs#L92) update_progressive_balances_on_attestation

**Skeptic check.** Verified: the altair JF function used by fork choice on_block reads only the progressive balances cache, which block processing keeps up to date. This is Lighthouse's own PR 4362; the earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#4362](https://github.com/sigp/lighthouse/pull/4362), [teku#6141](https://github.com/Consensys-Incorporated/teku/pull/6141), [teku#6065](https://github.com/Consensys-Incorporated/teku/pull/6065), [prysm#10659](https://github.com/OffchainLabs/prysm/pull/10659)

</details>


<a id="fork_choice-119"></a>
<details>
<summary><b>fork_choice-119</b> Prune block DAG exactly once per finality change — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Prune the block DAG once after each finality change instead of repeatedly.

**Impact.** None; pruning happens only from after_finalization, further amortized by prune_threshold.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:1738`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1738)
- [`consensus/fork_choice/src/fork_choice.rs:1956`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1956)
- [`consensus/proto_array/src/proto_array_fork_choice.rs:1044`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L1044)

**Skeptic check.** ForkChoice::prune -&gt; maybe_prune is called only from after_finalization (one call per finality change), and the threshold makes it even rarer. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#2469](https://github.com/status-im/nimbus-eth2/pull/2469)

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

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [prysm#11945](https://github.com/OffchainLabs/prysm/pull/11945)

</details>


<a id="fork_choice-121"></a>
<details>
<summary><b>fork_choice-121</b> Prune secondary fork choice indices with nodes — <i>n/a · low · S · memory</i></summary>

**Idea.** When pruning finalized fork choice nodes, also delete them from secondary indices (e.g. payload-hash index) so those maps do not leak.

**Impact.** No payload-hash index exists and the root index is cleaned on prune, so nothing leaks.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array.rs:2317`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L2317) execution_block_hash_to_node_indices does a linear scan, no secondary index
- [`consensus/proto_array/src/proto_array.rs:2085`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L2085) maybe_prune removes pruned roots from indices

**Sources.** [prysm#11813](https://github.com/OffchainLabs/prysm/pull/11813)

</details>


<a id="fork_choice-122"></a>
<details>
<summary><b>fork_choice-122</b> Bound and prune delayed object queues — <i>implemented · low · S · memory</i></summary>

**Idea.** Prune blocks, blobs, checkpoint states and attestations parked while waiting for dependencies once finalization (by block or slot tick) or epoch age makes them stale, and skip parking when the dependency is present, so delay queues cannot grow unbounded.

**Impact.** Every delay queue is bounded by count and expires within about one slot, so it cannot grow unbounded; pruning on finalization would add nothing.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:76`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L76) MAXIMUM_QUEUED_BLOCKS=16, :79 ENVELOPES=16, :82 ATTESTATIONS=16384, :85 DATA_COLUMNS=256, :88 LC updates=128
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:53`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L53) QUEUED_ATTESTATION_DELAY 12s, :61 column/envelope delay 1 slot, :67 RPC block delay 4s
- [`consensus/fork_choice/src/fork_choice.rs:311`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L311) dequeue_attestations drains every queued vote older than the current slot

**Skeptic check.** Verified the caps and timeouts (the earlier note wrongly put blocks at 16384; the block cap is 16). Grandine needed finalization-based pruning because its queues had no time expiry; Lighthouse's queues expire in seconds, so the same goal is met.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine@60c6d449d](https://github.com/grandinetech/grandine/commit/60c6d449d7ab), [grandine#637](https://github.com/grandinetech/grandine/pull/637), [grandine@d7b8e80a0](https://github.com/grandinetech/grandine/commit/d7b8e80a0f82), [grandine@632b3236c](https://github.com/grandinetech/grandine/commit/632b3236cded)

</details>


<a id="fork_choice-123"></a>
<details>
<summary><b>fork_choice-123</b> Skip re-validating gossip-verified attestations in fork choice — <i>implemented · low · S · cpu</i></summary>

**Idea.** When feeding attestations that gossip or block processing already validated into fork choice, skip the duplicate checks (signature, LMD/FFG consistency, target-root-known, time checks) and run only cheap index checks.

**Impact.** Negligible; no signature or state work is repeated in fork choice.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fork_choice/src/fork_choice.rs:1325`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1325) on_attestation does not run is_valid_indexed_attestation (signature verified upstream)
- [`consensus/fork_choice/src/fork_choice.rs:1181`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1181) validate_on_attestation skips the time check for AttestationFromBlock::True
- [`consensus/fork_choice/src/fork_choice.rs:1197-1235`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1197-L1235) remaining checks are proto_array hash lookups and field compares
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2579`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2579) gossip path passes verified.indexed_attestation()

**Skeptic check.** Verified: the expensive duplicate (signature verification) is never done in fork choice on either the gossip or the block path. What remains are O(1) lookups; the earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#8276](https://github.com/OffchainLabs/prysm/pull/8276), [prysm#8277](https://github.com/OffchainLabs/prysm/pull/8277), [prysm#8301](https://github.com/OffchainLabs/prysm/pull/8301), [prysm#3562](https://github.com/OffchainLabs/prysm/pull/3562)

</details>


<a id="fork_choice-124"></a>
<details>
<summary><b>fork_choice-124</b> Process block attestations into fork choice only once — <i>implemented · low · S · cpu</i></summary>

**Idea.** Do not feed block attestations to fork choice through a second path (separate routine or re-insert into the vote store) when the attestation pool path already applies them.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1763`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1763) single loop applies block attestations via fork_choice.on_attestation(AttestationFromBlock::True)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2579`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2579) the only other on_attestation caller is the gossip/API attestation path

**Skeptic check.** Verified with a grep: there are exactly two non-test callers of on_attestation, the block import loop and the gossip apply path, and there is no second vote store. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#4408](https://github.com/OffchainLabs/prysm/pull/4408), [prysm#11201](https://github.com/OffchainLabs/prysm/pull/11201), [prysm#3530](https://github.com/OffchainLabs/prysm/pull/3530)

</details>


<a id="fork_choice-125"></a>
<details>
<summary><b>fork_choice-125</b> Reuse indexed attestations from block import — <i>implemented · low · S · cpu</i></summary>

**Idea.** Capture indexed attestations computed during block import and reuse them for fork choice vote updates instead of recomputing them.

**Impact.** None; indexed attestations are built once per block.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/consensus_context.rs:161`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/consensus_context.rs#L161) get_indexed_attestation memoizes by attestation tree_hash_root
- [`consensus/state_processing/src/per_block_processing/block_signature_verifier.rs:297`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/block_signature_verifier.rs#L297) signature verification fills the cache
- [`beacon_node/beacon_chain/src/block_verification.rs:1283`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1283) the same consensus_context is carried from gossip verification into execution-pending
- [`beacon_node/beacon_chain/src/block_verification.rs:1764`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1764) fork choice reads from that context
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4987`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4987),5054,5094 import-time validator monitor, observed attesters and slasher reuse ctxt.get_indexed_attestation

**Skeptic check.** Traced ConsensusContext from signature verification through per_block_processing, fork choice and post-import consumers: every one reuses the cache. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#2643](https://github.com/Consensys-Incorporated/teku/pull/2643)

</details>


<a id="fork_choice-126"></a>
<details>
<summary><b>fork_choice-126</b> Remove unreachable branches in fork choice code — <i>implemented · low · S · cpu</i></summary>

**Idea.** Drop provably unreachable comparisons in proto-array best-child updates and block-import checkpoint computation.

**Impact.** Cosmetic.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fork_choice/src/fork_choice.rs:937-940`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L937-L940)
- [`consensus/proto_array/src/proto_array.rs:1448`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L1448)

**Skeptic check.** PR #4626's change (parent_finalized.epoch + 1 == block_epoch) is present at fork_choice.rs:940; PR #4583's best-child comparison no longer exists since head selection is now find_head_walk. Earlier evidence's line citation was loose but the verdict holds.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#4626](https://github.com/sigp/lighthouse/pull/4626), [lighthouse#4583](https://github.com/sigp/lighthouse/pull/4583)

</details>


<a id="fork_choice-127"></a>
<details>
<summary><b>fork_choice-127</b> Remove fork choice caches that never hit — <i>n/a · low · S · cpu</i></summary>

**Idea.** Measure hit rate of fork choice short-circuit caches (e.g. a 'synced' cache around delta computation) and drop those that never hit.

**Impact.** Lighthouse has no such cache, so nothing to remove.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array_fork_choice.rs:773`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L773) compute_deltas runs unconditionally, no short-circuit cache

**Sources.** [lodestar#4187](https://github.com/ChainSafe/lodestar/pull/4187)

</details>


<a id="fork_choice-128"></a>
<details>
<summary><b>fork_choice-128</b> Resolve payload committee from post-state in hand — <i>implemented · low · S · latency, cpu</i></summary>

**Idea.** When applying payload attestations from an imported block, resolve committee positions from the block's post-state already in hand instead of looking up the parent state in the state cache.

**Impact.** None; PTC resolved from the post-state in hand, no state-cache lookup.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1705-1730`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1705-L1730)
- [`beacon_node/beacon_chain/src/block_verification.rs:1783-1803`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1783-L1803)
- [`consensus/types/src/state/beacon_state.rs:3591`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3591)

**Skeptic check.** Payload attestations are applied to fork choice right after per_block_processing using the same mutable `state` (post-state) and its ptc_window via get_ptc, a cheap window read. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#11501](https://github.com/Consensys-Incorporated/teku/pull/11501)

</details>


<a id="fork_choice-129"></a>
<details>
<summary><b>fork_choice-129</b> Reuse one working state across reorgs — <i>n/a · low · memory, cpu, latency</i></summary>

**Idea.** On reorgs and block import in fork choice, copy into and reuse one working beacon state object instead of cloning or reloading a fresh state.

**Impact.** Lighthouse fork choice keeps no beacon state, and head change uses cached head plus milhouse cheap clones, so there is no per-reorg state object to reuse.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:834`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L834) recompute_head_at_slot_internal only runs get_head on proto-array, no state load or clone
- [`consensus/proto_array/src/proto_array_fork_choice.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs): fork choice holds no beacon state

**Sources.** [caplin#12735](https://github.com/erigontech/erigon/pull/12735), [caplin#12833](https://github.com/erigontech/erigon/pull/12833)

</details>


<a id="fork_choice-130"></a>
<details>
<summary><b>fork_choice-130</b> Head state plus reverse changesets for forks — <i>n/a · low · memory</i></summary>

**Idea.** Keep one head state plus reverse changesets to rewind to other forks instead of storing full states per block.

**Impact.** Single-head-plus-changesets is a different storage design; Lighthouse hot states are structurally shared via milhouse and cold states use hierarchical diffs.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:1060`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1060) uses head state block_roots; hot DB stores per-block states / snapshots, cold uses hdiff

**Sources.** [caplin#7185](https://github.com/erigontech/erigon/pull/7185)

</details>


<a id="fork_choice-131"></a>
<details>
<summary><b>fork_choice-131</b> Share observation sets instead of cloning with store — <i>n/a · low · cpu, memory</i></summary>

**Idea.** Keep seen-attester/aggregator observation sets behind a shared mutex handle so cloning the fork choice store snapshot does not deep-copy them.

**Impact.** Lighthouse fork choice store is not cloned as a snapshot and holds no seen-attester sets, so there is no deep copy to avoid.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_fork_choice_store.rs:51-58`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_fork_choice_store.rs#L51-L58) store holds only checkpoints and balances
- seen attesters/aggregators live in observed_* caches on BeaconChain, not in the fork choice store

**Sources.** [grandine@2c05ff3a5](https://github.com/grandinetech/grandine/commit/2c05ff3a5389), [prysm#8694](https://github.com/OffchainLabs/prysm/pull/8694)

</details>


<a id="fork_choice-132"></a>
<details>
<summary><b>fork_choice-132</b> Shrink persisted fork choice snapshot — <i>implemented · low · S · disk, memory, latency</i></summary>

**Idea.** Do not persist recomputable fork choice data (balance caches, justified balances) and compress persisted votes, so the fork choice snapshot written on each update is much smaller.

**Impact.** Already shipped by Lighthouse's own PR 7805.

**Best measured result.** None (pr:lighthouse#7805)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_fork_choice_store.rs:398`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_fork_choice_store.rs#L398) PersistedForkChoiceStoreV28 holds no balances_cache or justified_balances
- [`consensus/proto_array/src/ssz_container.rs:24`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/ssz_container.rs#L24) SszContainerV29 stores votes/nodes/indices only; balances are passed in on load (:60)
- [`beacon_node/beacon_chain/src/persisted_fork_choice.rs:65`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/persisted_fork_choice.rs#L65) as_bytes compresses the whole SSZ with store_config.compress_bytes

**Skeptic check.** Verified: the persisted format has no balance caches and the whole snapshot, votes included, is compressed. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#7805](https://github.com/sigp/lighthouse/pull/7805)

</details>


<a id="fork_choice-133"></a>
<details>
<summary><b>fork_choice-133</b> Maintain canonical-block set inside fork choice — <i>implemented · low · S · cpu</i></summary>

**Idea.** Maintain the set of canonical blocks inside fork choice, updated on head change, instead of recomputing canonical checks separately elsewhere.

**Impact.** None; Prysm's fix removed duplicated canonical-map maintenance that Lighthouse never had.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:631-646`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L631-L646)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1050-1080`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1050-L1080)

**Skeptic check.** Lighthouse keeps no separate canonical map to duplicate; canonical checks use the head state's block_roots (O(1)) with a DB fallback for old slots. The effect (no duplicated canonical compute) holds, though the mechanism differs from a fork-choice-maintained set.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#7602](https://github.com/OffchainLabs/prysm/pull/7602)

</details>


<a id="fork_choice-134"></a>
<details>
<summary><b>fork_choice-134</b> Run only one fork choice implementation — <i>n/a · low · cpu</i></summary>

**Idea.** Do not run a legacy fork choice (or update its vote and block-tree caches) alongside the new one.

**Impact.** Lighthouse only has proto-array; no legacy fork choice runs in parallel.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array_fork_choice.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs): sole fork choice implementation

**Sources.** [nimbus@344175d1a](https://github.com/status-im/nimbus-eth2/commit/344175d1a240), [prysm#4665](https://github.com/OffchainLabs/prysm/pull/4665)

</details>


<a id="fork_choice-135"></a>
<details>
<summary><b>fork_choice-135</b> Find blocks at a slot set in one chain walk — <i>implemented · low · S · cpu</i></summary>

**Idea.** When looking up canonical/unfinalized blocks for several slots, walk the fork choice chain once and filter by the slot set instead of one walk per slot.

**Impact.** Multi-slot lookups (BlocksByRange, chain dump) use one forward/ancestor iteration; remaining block_root_at_slot callers are single-slot lookups, not loops over a slot set.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:819`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L819) forwards_iter_block_roots_until walks a slot range once
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1060`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1060) block_root_at_slot_skips_none reads the root from the head state block_roots
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:453`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L453) get_block_roots_ancestor_of_head one ancestor walk for a request

**Skeptic check.** Checked every non-test block_root_at_slot caller: none loops over a slot set (historical_blocks.rs:134/173 are one-off anchor checks). The earlier evidence was right; the mechanism differs from Lodestar (state roots vector, not fork choice scan) but has the same effect.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@e66bc0d7d](https://github.com/ChainSafe/lodestar/commit/e66bc0d7dac1), [lodestar#1688](https://github.com/ChainSafe/lodestar/pull/1688)

</details>


<a id="fork_choice-136"></a>
<details>
<summary><b>fork_choice-136</b> Skip early-slot head recompute without validators — <i>n/a · low · cpu, latency</i></summary>

**Idea.** Skip the late-in-slot head recompute for the next proposer when the node has no connected validators, since only proposers need it.

**Impact.** The pre-emptive recompute only moves attestation dequeue and get_head off the next slot's hot path, work that is needed anyway; the proposer-only part (prepare_beacon_proposer) already returns early without connected validators.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:205-212`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L205-L212) recompute_head_at_slot(next_slot) runs unconditionally late in slot
- [`beacon_node/beacon_chain/src/beacon_chain.rs:6898`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6898) prepare_beacon_proposer already skips when no proposer preparation data

**Sources.** [prysm#13570](https://github.com/OffchainLabs/prysm/pull/13570)

</details>


<a id="fork_choice-137"></a>
<details>
<summary><b>fork_choice-137</b> Skip new-head side effects when head unchanged — <i>implemented · low · S · cpu, latency, disk</i></summary>

**Idea.** Run new-head processing (events, state lookups, persistence, reorg metrics) only when the head actually changes, and compare like with like so payload-status flags do not create spurious head changes.

**Impact.** Spurious head changes are already filtered out. One small leftover: a Gloas payload-status-only change still reloads the block and state and runs build_all_caches (TODO at canonical_head.rs:1110), and this happens at most once per slot.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:1088`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1088) early return when view, payload status and fcU params are unchanged
- [`beacon_node/beacon_chain/src/canonical_head.rs:1236`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1236) after_new_head (events, reorg detection) runs only when beacon_block_root changes
- [`beacon_node/beacon_chain/src/canonical_head.rs:1176`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1176) FFG-only changes reuse the old snapshot via Arc clone

**Skeptic check.** Verified the unchanged-head early return and that after_new_head is gated on the block root. The Gloas Empty-&gt;Full reload is a real status change, not a spurious one, so the idea holds; the earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#10675](https://github.com/Consensys-Incorporated/teku/pull/10675), [lighthouse#9191](https://github.com/sigp/lighthouse/pull/9191), [prysm#16508](https://github.com/OffchainLabs/prysm/pull/16508), [teku#2900](https://github.com/Consensys-Incorporated/teku/pull/2900)

</details>


<a id="fork_choice-138"></a>
<details>
<summary><b>fork_choice-138</b> Skip fork choice while a head update is pending — <i>n/a · low · cpu</i></summary>

**Idea.** Do not run fork choice when a previous head update is still waiting to be applied, since its result would be discarded.

**Impact.** Lighthouse has no separate pending head-update pipeline whose result could be discarded.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:781`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L781) recompute_head_at_slot computes and applies head in one blocking task

**Sources.** [teku#2592](https://github.com/Consensys-Incorporated/teku/pull/2592)

</details>


<a id="fork_choice-139"></a>
<details>
<summary><b>fork_choice-139</b> Skip duplicate forkchoiceUpdated before attestation duty — <i>n/a · low · cpu, latency</i></summary>

**Idea.** Skip the extra forkchoiceUpdated before attestation duties when block processing already sent one for the same head.

**Impact.** Lighthouse never sends an extra FCU before attestation duty; it sends on head change and proposer preparation only.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:1090`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1090) early return when head/FCU params unchanged
- [`beacon_node/beacon_chain/src/canonical_head.rs:1909`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1909) FCU sent only on head change
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7135`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7135) only prepare_beacon_proposer sends another FCU

**Sources.** [teku#7972](https://github.com/Consensys-Incorporated/teku/pull/7972)

</details>


<a id="fork_choice-140"></a>
<details>
<summary><b>fork_choice-140</b> Drop block attestations with mismatched target ancestry — <i>implemented · low · S · cpu</i></summary>

**Idea.** On block import, skip block attestations whose target checkpoint does not match the voted block's ancestry before applying them to fork choice.

**Impact.** None: Lighthouse already rejects target-ancestry mismatches before it applies block attestations to fork choice.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fork_choice/src/fork_choice.rs:1165`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1165) validate_on_attestation runs for block and gossip attestations
- [`consensus/fork_choice/src/fork_choice.rs:1220-1231`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1220-L1231) expected_target from block.target_root (or beacon_block_root when the block is from an earlier epoch); a mismatch gives InvalidTarget
- [`beacon_node/beacon_chain/src/block_verification.rs:1768-1777`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1768-L1777) block-import on_attestation drops InvalidAttestation errors, so those votes never reach proto_array

**Skeptic check.** Confirmed that the target-vs-ancestry check runs on the block import path (AttestationFromBlock::True) as well as gossip, and invalid votes are silently skipped. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#9156](https://github.com/status-im/nimbus-eth2/pull/9156)

</details>


<a id="fork_choice-141"></a>
<details>
<summary><b>fork_choice-141</b> Drop attestations with non-viable target state — <i>not · low · Add an optional check in attestation_verification to reject non-viable targets before the shuffling-cache-miss state load. · cpu, latency</i></summary>

**Idea.** Optionally drop attestations whose target state is not viable instead of loading and advancing a state for them.

**Gap in Lighthouse.** No option to drop attestations with a non-viable target; the shuffling-cache-miss path loads and advances a state.

**Impact.** S

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:1244`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1244) verify_head_block_is_known only checks known head and finalized descent
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1617`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1617) map_attestation_committees uses shuffling cache, loads state on miss

**Sources.** [prysm#16094](https://github.com/OffchainLabs/prysm/pull/16094)

</details>


<a id="fork_choice-142"></a>
<details>
<summary><b>fork_choice-142</b> Take first variant index in proto-array pruning — <i>n/a · low · cpu</i></summary>

**Idea.** In proto-array pruning take the first variant's index directly, since the pending variant is always inserted first, instead of a min over variants.

**Impact.** Proto-array keeps one node per block root, so there are no pending/empty/full variants to take a min over.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array.rs:2073`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L2073) maybe_prune has no min over variants
- [`consensus/proto_array/src/proto_array.rs:80`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L80) variants are V17/V29 node versions, one node per root

**Sources.** [lodestar#9068](https://github.com/ChainSafe/lodestar/pull/9068)

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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [teku#4300](https://github.com/Consensys-Incorporated/teku/pull/4300)

</details>


<a id="fork_choice-144"></a>
<details>
<summary><b>fork_choice-144</b> Skip get_ancestor in on_block justified update — <i>implemented · low · S · cpu</i></summary>

**Idea.** In on_block's justified checkpoint update, skip the get_ancestor walk when the new justified checkpoint already descends from the current one.

**Impact.** Justified checkpoint update in on_block is a pure epoch comparison; the get_ancestor walk the Prysm PR avoided does not exist (later spec removed it).

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fork_choice/src/fork_choice.rs:1107`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1107) update_checkpoints compares epochs only, no ancestor walk
- [`consensus/fork_choice/src/fork_choice.rs:872`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L872) only get_ancestor in on_block is the finalized-descendant check

**Skeptic check.** Read update_checkpoints and all get_ancestor calls in fork_choice.rs; earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#6282](https://github.com/OffchainLabs/prysm/pull/6282)

</details>


<a id="fork_choice-145"></a>
<details>
<summary><b>fork_choice-145</b> Inherit unrealized checkpoints from parent when unchanged — <i>implemented · low · S · cpu</i></summary>

**Idea.** Skip the O(validators) unrealized justification/finalization computation for a block when cheap checks show it cannot change: parent already computed it this epoch with the maximal result, or it is too early in the epoch.

**Impact.** None left after Altair. The grandine maximal-result skip exists, and the non-skipped path is constant-time. Only Prysm's early-in-epoch heuristic is absent, and it would save an O(1) call.

**Best measured result.** None (pr:grandine#678)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fork_choice/src/fork_choice.rs:932-946`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L932-L946) inherits parent unrealized checkpoints when there are no slashings, parent_justified.epoch == block_epoch and parent_finalized+1 == block_epoch
- [`consensus/state_processing/src/per_epoch_processing/altair/justification_and_finalization.rs:9-30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/altair/justification_and_finalization.rs#L9-L30) fallback reads progressive_balances_cache and cached total active balance, so it is O(1)

**Second check.** Read the altair process_justification_and_finalization the fallback calls: it uses the progressive balances cache and does not iterate validators, so the O(validators) cost the idea wants to skip is not there in Lighthouse after Altair. Only phase0 still does an O(validators) ValidatorStatuses pass.

**Skeptic check.** Verified the same skip as grandine#678 in on_block, and that the fallback does no validator iteration post-Altair (phase0 still uses ValidatorStatuses, which does not matter). The earlier evidence was correct.

**Verdict history.** partial (checked) → implemented (refuted) → implemented (skeptic)

**Sources.** [grandine#678](https://github.com/grandinetech/grandine/pull/678), [prysm#10955](https://github.com/OffchainLabs/prysm/pull/10955), [lighthouse#9471](https://github.com/sigp/lighthouse/pull/9471), [lodestar#10467](https://github.com/ChainSafe/lodestar/pull/10467)

</details>


<a id="fork_choice-146"></a>
<details>
<summary><b>fork_choice-146</b> Early return when no equivocators — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** In fast-confirmation equivocation scoring, return zero early when there are no equivocating validators instead of building the set of all attesters in the slot range.

**Impact.** None: with no equivocators the loop does zero iterations, and Lighthouse never builds the set of all slot attesters.

**Best measured result.** None (pr:lodestar#9553)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fast_confirmation/src/lib.rs:1076-1097`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fast_confirmation/src/lib.rs#L1076-L1097) get_equivocation_score iterates only equivocating_indices and tests membership via slot_assignments.is_in_range
- [`consensus/fast_confirmation/src/lib.rs:223`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fast_confirmation/src/lib.rs#L223) slot_assignments precomputed from head state, refreshed only on shuffling change (lib.rs:345)

**Skeptic check.** Confirmed that the loop is driven by the equivocator set, not by all attesters in the slot range, so the empty case is already free. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#9553](https://github.com/ChainSafe/lodestar/pull/9553)

</details>


<a id="fork_choice-147"></a>
<details>
<summary><b>fork_choice-147</b> Slim per-block summary record for target lookups — <i>implemented · low · S · cpu, disk, memory</i></summary>

**Idea.** Store a small per-block record (root, parent root, slot) and use it for fork choice attestation target lookups instead of decoding whole blocks.

**Impact.** Attestation target lookups use the in-memory proto array summary, never decode full blocks from DB.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array.rs:85`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L85) ProtoNode holds slot, root, parent, target_root in memory
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1244`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1244) attestation head/target check uses fork_choice get_block

**Skeptic check.** Proto array is a stronger form of Prysm's slim per-block record (in memory, not a DB bucket). Earlier evidence right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#2373](https://github.com/OffchainLabs/prysm/pull/2373)

</details>


<a id="fork_choice-148"></a>
<details>
<summary><b>fork_choice-148</b> Queue early attestations and slim fork choice state — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Keep less state in fork choice, query per-epoch caches less often, and queue attestations until their slot instead of processing them early.

**Impact.** Current-slot attestations are queued and applied only once their slot has passed; fork choice keeps compact proto nodes and vote list.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fork_choice/src/fork_choice.rs:311`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L311) dequeue_attestations splits the BTreeMap queue by current slot
- [`consensus/fork_choice/src/fork_choice.rs:1580`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1580) process_attestation_queue

**Skeptic check.** Verified the slot-keyed queue and dequeue; Nimbus' PR explicitly aligned with Lighthouse's design here. Earlier evidence right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#1520](https://github.com/status-im/nimbus-eth2/pull/1520)

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


<a id="fork_choice-151"></a>
<details>
<summary><b>fork_choice-151</b> Proto-array as the store&#x27;s block index — <i>n/a · low · memory, startup</i></summary>

**Idea.** Use the proto-array itself as the store's block root/slot index and remove the duplicate block tree, saving memory and startup rebuild.

**Impact.** Lighthouse has no separate in-memory block tree duplicating proto-array.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array.rs:85`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L85) proto-array is the only in-memory block index

**Sources.** [teku#3116](https://github.com/Consensys-Incorporated/teku/pull/3116), [teku#3136](https://github.com/Consensys-Incorporated/teku/pull/3136)

</details>


<a id="fork_choice-152"></a>
<details>
<summary><b>fork_choice-152</b> Record payload status for replayed envelopes after restart — <i>implemented · low · S · latency, startup</i></summary>

**Idea.** After restart, record payload status for envelopes replayed without EL validation so the full-payload head variant is available immediately instead of advancing one block per sync cycle.

**Impact.** Lighthouse does not rebuild fork choice by replaying envelopes at startup; payload_received is persisted and set independent of EL validation, so the Caplin one-block-per-cycle catch-up cannot arise.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array.rs:171`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L171) payload_received field on ProtoNodeV29
- [`consensus/proto_array/src/ssz_container.rs:39`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/ssz_container.rs#L39) SszContainerV29 persists full ProtoNode list
- [`consensus/proto_array/src/proto_array.rs:906`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L906) on_payload_envelope_received sets payload_received regardless of EL verdict
- [`consensus/proto_array/src/proto_array_fork_choice.rs:962`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L962) set_all_blocks_to_optimistic resets only execution_status, keeps payload_received
- [`beacon_node/beacon_chain/src/beacon_chain.rs:692`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L692) load_fork_choice restores persisted proto array on restart

**Skeptic check.** Confirmed payload_received is persisted, survives the payload-status reset, and is set whatever the verdict. Only an unclean shutdown between epoch-granular persists (canonical_head.rs:1565) loses recent marks, recovered through sync re-import.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#24878](https://github.com/erigontech/erigon/pull/24878)

</details>


<a id="fork_choice-153"></a>
<details>
<summary><b>fork_choice-153</b> Mark tips full from stored payloads at setup — <i>implemented · low · S · sync</i></summary>

**Idea.** At fork choice setup, mark tips as payload-full when their payload is already in the DB so peers syncing from this node can get the payload.

**Impact.** Tips keep their Full marking across clean restarts, and peers are served envelopes from the DB whatever the fork choice marking.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/ssz_container.rs:39`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/ssz_container.rs#L39) persisted ProtoNodeV29 keeps payload_received
- [`beacon_node/beacon_chain/src/builder.rs:790`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L790) head Full envelope loaded from store at startup
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1501`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1501) envelopes by range served from store via get_payload_envelopes, not gated on fork choice
- [`consensus/fork_choice/src/fork_choice.rs:834`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L834) ParentPayloadNotVerified triggers envelope recovery for a child

**Skeptic check.** There is no startup DB reconciliation like Prysm's, but there is no need for one: fork choice is persisted (also on Drop) and RPC serving reads the store. Small crash-window caveat: persistence is per epoch, reorg or finalization, not per envelope.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#17508](https://github.com/OffchainLabs/prysm/pull/17508)

</details>


<a id="fork_choice-154"></a>
<details>
<summary><b>fork_choice-154</b> Keep finalized checkpoint dependent root after pruning — <i>not · low · S · cpu, memory</i></summary>

**Idea.** Keep the dependent root of the finalized checkpoint in fork choice after its node is pruned, so head-state reuse by dependent root still works for finalized targets.

**Gap in Lighthouse.** Lighthouse accepts that attestations targeting the parent of the finalized block are skipped (comment says useless). Retaining the finalized checkpoint dependent root would need an extra field kept at prune time in ProtoArray.

**Impact.** Negligible: only a rare cache miss for finalized targets; Lighthouse's own comment treats those as useless.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2792-2830`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2792-L2830) shuffling compat check reads fork choice get_block and returns false for pruned parent-of-finalized
- [`consensus/proto_array/src/proto_array_fork_choice.rs:398-415`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L398-L415) shuffling ids kept only on live nodes

**Sources.** [prysm#16103](https://github.com/OffchainLabs/prysm/pull/16103)

</details>


<a id="fork_choice-155"></a>
<details>
<summary><b>fork_choice-155</b> Single cache for forkchoice update parameters — <i>partial · low · M · memory</i></summary>

**Idea.** Keep the fork choice head result (forkchoice update parameters) in one place instead of caching it in both fork choice and canonical head.

**Gap in Lighthouse.** Still duplicated: ForkChoice::forkchoice_update_parameters and CachedHead. Moving computation into BeaconChain would remove it, per closed PR 10112.

**Impact.** Code hygiene; no measurable runtime gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fork_choice/src/fork_choice.rs:373`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L373) forkchoice_update_parameters stored in ForkChoice
- [`beacon_node/beacon_chain/src/canonical_head.rs:420`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L420),502,923 also cached in CachedHead and re-read; PR 10112 was closed unmerged

**Sources.** [lighthouse#10112](https://github.com/sigp/lighthouse/pull/10112), [lighthouse#3065](https://github.com/sigp/lighthouse/pull/3065)

</details>


<a id="fork_choice-156"></a>
<details>
<summary><b>fork_choice-156</b> Update blob pruning metadata once per head change — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Update auxiliary metadata (blob pruning info) once after the canonical head is chosen instead of for each head candidate during fork choice, avoiding repeated state-root lookups and DB writes.

**Impact.** None: there is no per-block or per-candidate blob_info update in beacon_chain.rs. The original per-import write block was removed and later replaced by finalization-driven pruning.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:1499`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1499) after_new_head runs once per head change
- [`beacon_node/beacon_chain/src/canonical_head.rs:1734`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1734) process_prune_blobs runs only after finalization
- [`beacon_node/beacon_chain/src/migrate.rs:213-249`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L213-L249) blob pruning runs on the background migrator thread

**Skeptic check.** This is Lighthouse's own commit. grep finds no compare_and_set_blob_info in the beacon_chain import path, and pruning is driven once per finalization through the migrator. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@fb2ce909f](https://github.com/sigp/lighthouse/commit/fb2ce909f66e)

</details>


<a id="fork_choice-157"></a>
<details>
<summary><b>fork_choice-157</b> Count fork-choice votes from aggregate bitfield popcounts — <i>n/a · low · cpu</i></summary>

**Idea.** Compute LMD vote weights by counting set bits of each pooled aggregate's participation bitfield per target block into a count table, instead of resolving a latest-message target for every active validator.

**Impact.** Lighthouse keeps incremental per-validator latest messages and applies deltas; Nimbus popcount counting from pooled aggregates is a different design and would not be cheaper than the existing delta walk (which skips unchanged votes).

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array_fork_choice.rs:1387-1417`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L1387-L1417) - compute_deltas walks VoteTracker per validator, applying only changed votes as deltas

**Sources.** [nimbus@f0e3de6b1](https://github.com/status-im/nimbus-eth2/commit/f0e3de6b1943)

</details>


<a id="fork_choice-158"></a>
<details>
<summary><b>fork_choice-158</b> Ancestor skip tables at power-of-two heights — <i>not · low · M · cpu, latency</i></summary>

**Idea.** Store per-block ancestor pointers at power-of-two aligned heights when a block is added, so head finding and ancestor queries jump logarithmically instead of walking block by block.

**Gap in Lighthouse.** Add a skip pointer per ProtoNode and use it in get_ancestor / is_finalized_checkpoint_or_descendant.

**Impact.** Walks are over a contiguous Vec of roughly 64-100 nodes on a healthy chain, so the saving is microseconds per block/attestation; only matters in long non-finality.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fork_choice/src/fork_choice.rs:509`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L509) get_ancestor walks iter_block_roots linearly
- [`consensus/proto_array/src/proto_array.rs:2251`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L2251) is_finalized_checkpoint_or_descendant walks parent indices (with checkpoint shortcut at 2279)

**Sources.** [lighthouse@fb270a5a4](https://github.com/sigp/lighthouse/commit/fb270a5a419b)

</details>


<a id="fork_choice-159"></a>
<details>
<summary><b>fork_choice-159</b> Drop redundant latest-messages map beside proto-array — <i>implemented · low · S · memory, disk</i></summary>

**Idea.** When the proto-array already tracks votes, do not also keep or persist a separate per-validator latest-messages map in the store, removing duplicated data and its writes.

**Impact.** Already no duplicate per-validator map; votes live in proto_array.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/persisted_fork_choice.rs:9-23`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/persisted_fork_choice.rs#L9-L23)
- [`consensus/fork_choice/src/fork_choice.rs:1920-1921`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1920-L1921)

**Skeptic check.** PersistedForkChoice holds only the fork_choice (proto-array) container and the store. latest_message() goes to proto_array.latest_message, so there is no second map of votes.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#1579](https://github.com/Consensys-Incorporated/teku/pull/1579)

</details>


<a id="fork_choice-160"></a>
<details>
<summary><b>fork_choice-160</b> Rank empty payload variant above unsatisfied payload in own slot — <i>n/a · low · latency, cpu</i></summary>

**Idea.** During a payload's own slot, rank an unsatisfied payload below its empty variant in head selection so the prepared next-slot payload matches the head the proposer builds on, avoiding payload rebuild.

**Impact.** Lighthouse fork choice has no inclusion-list (Heze) satisfaction logic yet, so the unsatisfied-payload case does not exist; revisit if IL fork choice is added (tiebreaker would need the same own-slot rule).

**Best measured result.** following proposal reused prepared payload 2 of 2; on unstable every proposal rebuilt 4 of 4 (pr:lodestar#10416)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array.rs:1940`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L1940) get_payload_status_tiebreaker has no inclusion-list satisfaction input
- [`consensus/proto_array/src/proto_array.rs:2004`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L2004) should_extend_payload

**Sources.** [lodestar#10416](https://github.com/ChainSafe/lodestar/pull/10416)

</details>


<a id="fork_choice-161"></a>
<details>
<summary><b>fork_choice-161</b> Optional skip of finalized root consistency check — <i>not · low · S · cpu</i></summary>

**Idea.** Offer a switch to skip the finalized-root consistency check when processing blocks or attestations in fork choice where the check is redundant, saving hot-path work.

**Gap in Lighthouse.** Add an opt-out flag or early exit for the on_block get_ancestor check in ForkChoice::on_block.

**Impact.** Saves a ~64-100 step Vec walk per imported block; negligible (microseconds).

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fork_choice/src/fork_choice.rs:872`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L872) on_block always does get_ancestor(parent, finalized_slot) walk
- [`consensus/fork_choice/src/fork_choice.rs:1829`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1829) is_finalized_checkpoint_or_descendant on attestation paths, has early-exit via checkpoint match (proto_array.rs:2279)

**Sources.** [grandine#418](https://github.com/grandinetech/grandine/pull/418)

</details>


<a id="fork_choice-162"></a>
<details>
<summary><b>fork_choice-162</b> Reuse one LMD-GHOST result for head and logging — <i>n/a · low · cpu</i></summary>

**Idea.** Return the head, block set and weights from the fork choice run and reuse them for tree logging or other consumers, so LMD-GHOST and the live-chain walk run once per slot, not twice.

**Impact.** Lighthouse runs find_head once per head update and has no per-slot tree logging that reruns LMD-GHOST.

**Best measured result.** end-of-slot LMD GHOST computed twice before; once now (no numbers) (pr:ethlambda#536)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fork_choice/src/fork_choice.rs:568`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L568) get_head runs find_head once and returns the node only
- [`beacon_node/beacon_chain/src/beacon_chain.rs:8237`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L8237) dump_as_dot is a debug dump, not a per-slot log

**Sources.** [ethlambda#536](https://github.com/lambdaclass/ethlambda/pull/536)

</details>


<a id="fork_choice-163"></a>
<details>
<summary><b>fork_choice-163</b> Shared backward sweep for committee unions over slot ranges — <i>n/a · low · M · cpu, memory</i></summary>

**Idea.** When many queries need the union of committee members over slot ranges ending at the same slot, do one backward sweep recording each validator's latest slot and answer each range as a prefix, instead of rebuilding a large validator set per query.

**Gap in Lighthouse.** If Lighthouse adopts spec PR 5670 (exact union), build one backward sweep of latest assigned slot per validator in fast_confirmation and answer ranges as prefixes.

**Impact.** Not applicable today: the crate is a dependency of beacon_chain but uses the estimate, so no union is built; would matter only after moving to the exact-weight spec.

**Best measured result.** per-call union ~3 s, sweep 14 to 31 ms (1M validators, 92 range queries) (pr:lodestar#10525)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fast_confirmation/src/lib.rs:1520`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fast_confirmation/src/lib.rs#L1520) estimate_committee_weight_between_slots uses the old total_balance/slots_per_epoch estimate, no committee union
- [`consensus/fast_confirmation/src/lib.rs:1074`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fast_confirmation/src/lib.rs#L1074) equivocation check uses precomputed per-validator slot assignments

**Sources.** [lodestar#10525](https://github.com/ChainSafe/lodestar/pull/10525)

</details>


