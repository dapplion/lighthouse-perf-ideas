# block_import

158 ideas: 16 not, 21 partial, 81 implemented, 40 n/a; 23 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [block_import-001](#block_import-001) **★** | Separate CPU-bound and IO-bound beacon processor worker pools | not | medium | M | cpu, latency |
| [block_import-002](#block_import-002) | Wait for data availability before entering serial import queue | implemented | medium | S | latency |
| [block_import-003](#block_import-003) | Send forkchoiceUpdated every sync-limit blocks during bulk sync | implemented | low | S | sync |
| [block_import-004](#block_import-004) | Propagate gossip blocks/envelopes before state transition and EL verdict | implemented | high | S | latency |
| [block_import-005](#block_import-005) | Pre-advance head state to next slot and reuse it | implemented | high | S | latency, cpu |
| [block_import-006](#block_import-006) **★** | Set head first, persist block and checkpoints afterwards | partial | high | L | latency, disk |
| [block_import-007](#block_import-007) | Overlap EL calls with import work; Arc-shared blocks | implemented | medium | S | latency, cpu, memory |
| [block_import-008](#block_import-008) | Fetch block pre-state asynchronously without blocking threads | n/a | low |  | latency |
| [block_import-009](#block_import-009) | Avoid copying or cloning blocks through queues and verification | partial | low | S | cpu, memory, latency |
| [block_import-010](#block_import-010) | Reuse held fork choice read lock in block verification | implemented | low | S | cpu, latency |
| [block_import-011](#block_import-011) | Use block's own payload status instead of fork choice lookup | implemented | low | S | latency |
| [block_import-012](#block_import-012) | Non-blocking queue push instead of a future per item | n/a | low |  | cpu, memory |
| [block_import-013](#block_import-013) | Skip head block DB read unless block can change head | n/a | low |  | disk, latency |
| [block_import-014](#block_import-014) | Do not retain BeaconStates in long-lived tasks and channels | implemented | high | S | memory, latency |
| [block_import-015](#block_import-015) **★** | Send forkchoiceUpdated in background, publish head early | partial | medium | S | latency, cpu |
| [block_import-016](#block_import-016) | Run finalization migration and pruning after import in background | implemented | medium | S | latency |
| [block_import-017](#block_import-017) **★** | Batch-verify all signatures of a chain segment | partial | medium | M | cpu, sync |
| [block_import-018](#block_import-018) | Rebuild participation flags tree once for overlapping attestations | implemented | medium | S | cpu |
| [block_import-019](#block_import-019) | Verify all block signatures in one batch including sync aggregate | implemented | high | S | cpu |
| [block_import-020](#block_import-020) **★** | Batch block, head and state DB writes during sync | partial | medium | M | sync, disk, latency, cpu |
| [block_import-021](#block_import-021) | Insert sync blocks into EL in rounds bounded by limit | n/a | low |  | sync, disk, latency |
| [block_import-022](#block_import-022) | Run sanity checks over whole block segment at once | implemented | low | S | cpu, sync |
| [block_import-023](#block_import-023) **★** | Blacklist descendants of known-bad blocks | partial | medium | S | cpu |
| [block_import-024](#block_import-024) | Read previous block root from state block_roots | implemented | low | S | disk, latency |
| [block_import-025](#block_import-025) **★** | Process gossip blocks on blocking executor, not async core | partial | high | S | latency, cpu |
| [block_import-026](#block_import-026) **★** | Bound pending and future block queues by count and bytes | partial | medium | S | memory |
| [block_import-027](#block_import-027) | Cap delayed execution payload envelope queue | implemented | low | S | memory |
| [block_import-028](#block_import-028) | Requeue RPC blocks only before attestation deadline | not | low | S | cpu |
| [block_import-029](#block_import-029) | Compute base_reward_per_increment once per block | implemented | low | S | cpu |
| [block_import-030](#block_import-030) | Cache block roots that failed inclusion list check | n/a | low |  | cpu |
| [block_import-031](#block_import-031) | Keep latest finalized state in memory for import | n/a | low |  | cpu, disk, latency |
| [block_import-032](#block_import-032) | Cache genesis block root | implemented | low | S | cpu |
| [block_import-033](#block_import-033) | Compute indexed attestations once per block and reuse | implemented | medium | S | cpu, latency, disk |
| [block_import-034](#block_import-034) | Read active validator count from cached shuffling | implemented | low | S | cpu |
| [block_import-035](#block_import-035) | Cancel-safe counter for signature batching decision | n/a | low | S | cpu, latency |
| [block_import-036](#block_import-036) | Cancellable block collector flush on shutdown | n/a | low | S | latency |
| [block_import-037](#block_import-037) **★** | Import chain segment with one pre-state lookup | partial | medium | M | cpu, sync |
| [block_import-038](#block_import-038) | Evaluate cheap flags before 32-byte hash comparisons | n/a | low | S | cpu |
| [block_import-039](#block_import-039) | Structural checks before pubkey collection and signature verification | implemented | medium | S | cpu |
| [block_import-040](#block_import-040) | Return early from post-block fcU when no payload attributes | partial | low | S | cpu, memory, latency |
| [block_import-041](#block_import-041) | Coalesce head and reorg events during sync | implemented | low | S | cpu |
| [block_import-042](#block_import-042) | Compute block root once and pass it through pipeline | implemented | medium | S | cpu, latency |
| [block_import-043](#block_import-043) | Dedupe validation tasks per block; offload mutator work | implemented | low | S | cpu, latency |
| [block_import-044](#block_import-044) | Insert finalized deposits into cache in background | n/a | low | S | latency |
| [block_import-045](#block_import-045) | Run state defragmentation after block import | n/a | medium |  | latency |
| [block_import-046](#block_import-046) **★** | Delay attestation production while head block imports | partial | medium | M | latency |
| [block_import-047](#block_import-047) | Apply EL payload status after block accepted in fork choice | n/a | low | S | latency, cpu |
| [block_import-048](#block_import-048) | Direct field equality instead of reflection for Eth1Data | implemented | low | S | cpu, memory |
| [block_import-049](#block_import-049) | Drop envelope execution-parent DB existence check | n/a | low |  | cpu, disk |
| [block_import-050](#block_import-050) | Reject future-slot blocks early instead of queueing | implemented | medium | S | memory, disk, bandwidth |
| [block_import-051](#block_import-051) | Remove obsolete optimistic import candidate check | n/a | low |  | latency, sync |
| [block_import-052](#block_import-052) | Do not recompute an already known state root | implemented | low | S | cpu |
| [block_import-053](#block_import-053) | Reject known, finalized or non-descendant blocks before state load | implemented | medium | S | cpu, memory, disk, latency, sync |
| [block_import-054](#block_import-054) | Load block collector without temporary in-memory DB | n/a | low |  | memory, disk |
| [block_import-055](#block_import-055) | Call slot tick handler directly, skipping missed ticks | n/a | low |  | latency, cpu |
| [block_import-056](#block_import-056) | Deduplicate in-flight block imports across gossip and RPC | implemented | medium | S | cpu, disk, memory |
| [block_import-057](#block_import-057) | Size processor queues from active validator count | implemented | medium | S | memory |
| [block_import-058](#block_import-058) | Produce light client updates eagerly after import | implemented | low | S | cpu, latency |
| [block_import-059](#block_import-059) **★** | Emit head/block events right after head update | partial | medium | S | latency |
| [block_import-060](#block_import-060) **★** | Send fcU from in-memory head before block persisted | not | high | L | latency |
| [block_import-061](#block_import-061) **★** | Update head immediately after block state transition | partial | medium | M | latency, cpu |
| [block_import-062](#block_import-062) | Verify proposer signature before state transition and DA | implemented | medium | S | cpu |
| [block_import-063](#block_import-063) | Epoch-boundary metrics off block import path | not | low | S | latency, cpu |
| [block_import-064](#block_import-064) | Running Eth1Data vote count cache | not | low | M | cpu |
| [block_import-065](#block_import-065) | Event-driven head publication on block index commit | n/a | low |  | latency |
| [block_import-066](#block_import-066) | Emit block events without waiting for EL validity | not | low | S | latency |
| [block_import-067](#block_import-067) | Evict received-set entries when delayed queue full | implemented | low | S | memory |
| [block_import-068](#block_import-068) | Evict cached inputs of unimported repeat proposals | implemented | low | S | memory |
| [block_import-069](#block_import-069) | Start block and payload verification before data availability completes | implemented | high | S | latency, cpu |
| [block_import-070](#block_import-070) | Faster justification and finalization checkpoint updates | implemented | low | S | latency, cpu |
| [block_import-071](#block_import-071) | Fast RwLocks and rayon parallelism in block processing | implemented | low | S | cpu, latency |
| [block_import-072](#block_import-072) | Finalized-descendant check via fork choice membership | implemented | low | S | cpu, disk, latency |
| [block_import-073](#block_import-073) | Check block existence in fork choice before DB | implemented | medium | S | cpu, disk, latency |
| [block_import-074](#block_import-074) **★** | Import block once half of columns are available | partial | high | M | latency |
| [block_import-075](#block_import-075) | Early return from save-head when head unchanged | implemented | low | S | cpu, sync |
| [block_import-076](#block_import-076) | Use in-memory head state when parent is head | partial | low | S | latency, disk |
| [block_import-077](#block_import-077) | Update head once per slot while far behind | implemented | medium | S | cpu, sync |
| [block_import-078](#block_import-078) | Compute total active balance once per block | implemented | low | S | cpu |
| [block_import-079](#block_import-079) | Check sync block cache before DB lookups | n/a | low |  | disk, latency |
| [block_import-080](#block_import-080) | Wake slot wait early when block arrives | n/a | low |  | latency |
| [block_import-081](#block_import-081) | Iterate validator tree list from index, not skip | implemented | low | S | cpu, latency |
| [block_import-082](#block_import-082) | Justification from progressively tracked balances | implemented | medium | S | cpu, latency |
| [block_import-083](#block_import-083) | Compute signed block header lazily | implemented | medium | S | cpu, latency |
| [block_import-084](#block_import-084) | Skip import of already-known blocks | implemented | medium | S | cpu, sync |
| [block_import-085](#block_import-085) | Recheck known block under fork choice lock | implemented | low | S | cpu, disk, latency |
| [block_import-086](#block_import-086) | Load missing parent from local DB | n/a | low | S | sync, bandwidth |
| [block_import-087](#block_import-087) **★** | Reject blocks with huge parent skip distance | not | medium | S | memory, disk |
| [block_import-088](#block_import-088) | Move parent state into import, no clone | implemented | medium | S | cpu, memory |
| [block_import-089](#block_import-089) | Narrow deposit signature pre-verification set | n/a | low | S | cpu |
| [block_import-090](#block_import-090) **★** | Advance next-slot state immediately after head update | partial | medium | S | latency |
| [block_import-091](#block_import-091) **★** | Send proposer FCU before next-slot cache update | partial | medium | S | latency |
| [block_import-092](#block_import-092) | Notify reprocess queue on every import path | partial | low | S | latency |
| [block_import-093](#block_import-093) | Query optimistic status once per batch tail | n/a | medium |  | cpu |
| [block_import-094](#block_import-094) | Run state transition concurrently with newPayload | implemented | high | S | latency |
| [block_import-095](#block_import-095) **★** | Persist block concurrently with verification | not | medium | M | latency, disk |
| [block_import-096](#block_import-096) **★** | Write blobs in parallel with fork choice write | not | medium | S | latency, disk |
| [block_import-097](#block_import-097) | Parallel attestation signature verification per block | not | low | M | cpu, latency |
| [block_import-098](#block_import-098) | Reuse in-hand state instead of DB refetch | implemented | low | S | disk, latency, cpu |
| [block_import-099](#block_import-099) **★** | Pause gossip intake while processing current block | not | medium | S | latency, cpu |
| [block_import-100](#block_import-100) | Pipelined block processing stream | n/a | low | L | cpu, latency |
| [block_import-101](#block_import-101) | Plain struct for signature-only indexed attestation | implemented | low | S | cpu, memory |
| [block_import-102](#block_import-102) | Point pubkey lookups for sync aggregate | implemented | medium | S | cpu, memory |
| [block_import-103](#block_import-103) | Cheap pre-checks before EL validation | implemented | low | S | sync, latency, cpu |
| [block_import-104](#block_import-104) | Preallocated zero values for empty-payload checks | n/a | low | S | memory, cpu |
| [block_import-105](#block_import-105) | Prebuild committee cache on pre-state | implemented | low | S | cpu |
| [block_import-106](#block_import-106) | Precompute next epoch transition ahead of time | implemented | high | S | latency, cpu |
| [block_import-107](#block_import-107) | Precomputed blob schedule lookup | implemented | low | S | cpu |
| [block_import-108](#block_import-108) | Prefetch deposit request signature checks | not | low | M | cpu, latency |
| [block_import-109](#block_import-109) | Prime proposer cache during state advance | implemented | low | S | latency |
| [block_import-110](#block_import-110) | Apply proposer boost before DB write | implemented | medium | S | latency |
| [block_import-111](#block_import-111) | Remove block-waiter listeners after resolution | n/a | low | S | memory |
| [block_import-112](#block_import-112) | Skip non-newer finalized checkpoint DB write | implemented | low | S | disk |
| [block_import-113](#block_import-113) | Cheap override-FCU check before payload attributes | implemented | low | S | cpu, latency |
| [block_import-114](#block_import-114) | Skip proposer prep work during initial sync | implemented | medium | S | cpu, latency, sync |
| [block_import-115](#block_import-115) | Skip slot processing for payload attributes | implemented | medium | S | cpu, latency |
| [block_import-116](#block_import-116) | Restore chain from in-memory blocks at restart | n/a | low | L | startup, disk |
| [block_import-117](#block_import-117) | Retry DA-failed import on tracker completion | implemented | low | S | latency |
| [block_import-118](#block_import-118) | Retry import when parent became known meanwhile | partial | low | S | sync |
| [block_import-119](#block_import-119) | Reuse cached versioned hashes for newPayload | not | low | S | cpu |
| [block_import-120](#block_import-120) | Read lock where block verification only reads | implemented | low | S | latency |
| [block_import-121](#block_import-121) **★** | Persist received SSZ bytes, no reserialization | not | medium | M | cpu, latency, memory |
| [block_import-122](#block_import-122) | Block root from header with body root | implemented | low | S | cpu, latency |
| [block_import-123](#block_import-123) | Skip churn computation when block has no exits | implemented | low | S | cpu |
| [block_import-124](#block_import-124) | Single-pass pubkey fetch for signature verify | implemented | low | S | cpu, memory |
| [block_import-125](#block_import-125) | Execution block hash from envelope alone | implemented | low | S | cpu |
| [block_import-126](#block_import-126) | Skip EL validation for finalized sync envelopes | not | low | M | sync |
| [block_import-127](#block_import-127) | Skip post-block FCU after Gloas | n/a | low |  | cpu, latency |
| [block_import-128](#block_import-128) | Skip ancestor DB walk when parent known | n/a | low |  | cpu, disk |
| [block_import-129](#block_import-129) | Skip newPayload assembly with null engine | n/a | low | S | cpu, latency |
| [block_import-130](#block_import-130) | Skip indexed attestation build for trusted signatures | implemented | low | S | cpu, memory |
| [block_import-131](#block_import-131) | Run single queued job immediately | n/a | low | S | latency |
| [block_import-132](#block_import-132) | Do not re-verify already verified block signature | implemented | medium | S | cpu, latency |
| [block_import-133](#block_import-133) | Skip state rewind when parent state is current | n/a | low |  | cpu |
| [block_import-134](#block_import-134) | Wait for gossip sidecars only for recent slots | n/a | medium |  | latency, sync |
| [block_import-135](#block_import-135) | Bound reprocess queue capacity | implemented | medium | S | memory, latency |
| [block_import-136](#block_import-136) **★** | Validate block outside the fork choice lock | partial | high | M | latency, cpu |
| [block_import-137](#block_import-137) | Stop ancestor lookup on cancellation | n/a | low | S | cpu, latency |
| [block_import-138](#block_import-138) | Load envelope summary instead of full payload | implemented | low | S | disk, latency |
| [block_import-139](#block_import-139) | Synchronous block validation without async overhead | n/a | low | S | latency |
| [block_import-140](#block_import-140) | Tree-backed blocks during state regeneration | n/a | low | S | cpu |
| [block_import-141](#block_import-141) | Trigger envelope import once per arrival | implemented | low | S | cpu |
| [block_import-142](#block_import-142) **★** | Checkpoint sync from unfinalized state | partial | medium | M | startup, sync |
| [block_import-143](#block_import-143) | Backpressure on async block DB write queue | n/a | high |  | memory |
| [block_import-144](#block_import-144) | Yield to scheduler between block imports | n/a | low | S | latency, cpu, memory |
| [block_import-145](#block_import-145) | Import fetched block ranges as one chain segment call | implemented | low | S | cpu, sync, latency |
| [block_import-146](#block_import-146) | Detect default payloads without copying transactions | implemented | low | S | cpu, memory |
| [block_import-147](#block_import-147) | Delay-queue slightly early gossip blocks until slot start | implemented | low | S | latency, bandwidth |
| [block_import-148](#block_import-148) | Import quarantined children of head when synced ahead | implemented | low | S | sync, latency |
| [block_import-149](#block_import-149) | Run independent post-block steps concurrently | not | low | M | latency |
| [block_import-150](#block_import-150) | Remove always-on per-block state dumps | implemented | low | S | disk, cpu |
| [block_import-151](#block_import-151) | Reuse resolved parent and lazily wrap quarantined blocks | n/a | low | S | cpu |
| [block_import-152](#block_import-152) | Check known blocks with a single map lookup | n/a | low | S | cpu |
| [block_import-153](#block_import-153) | Skip duplicate check and DB rewrite when replaying at startup | n/a | low |  | startup, disk, cpu |
| [block_import-154](#block_import-154) | Skip attestation and signature work when replaying finalized blocks | implemented | low | S | cpu, latency |
| [block_import-155](#block_import-155) | Skip blob transaction decoding for versioned hashes | implemented | low | S | cpu, latency |
| [block_import-156](#block_import-156) | Skip verbose logging and rebroadcast for sync imports | implemented | low | S | sync, cpu |
| [block_import-157](#block_import-157) | Skip execution block hash for empty pre-merge payloads | implemented | low | S | cpu |
| [block_import-158](#block_import-158) | Skip data-availability wait when blobs leave block path | implemented | low | S | latency |

★ actionable. Click an id for the full record.

## Ideas

<a id="block_import-001"></a>
<details>
<summary><b>block_import-001</b> Separate CPU-bound and IO-bound beacon processor worker pools — <i>not · medium · M · cpu, latency</i></summary>

**Idea.** Split beacon processor workers into CPU-bound and IO-bound classes. Cap CPU-heavy tasks near the core count and let IO-bound tasks run in larger numbers, so IO waits do not take CPU worker slots and CPU work does not oversubscribe cores.

**Gap in Lighthouse.** Give each WorkType a CPU or IO class and add a second counter in the manager loop, so CPU work is capped at core count and IO-bound work (DB-backed RPC serving, async RPC handlers) has its own larger cap. PR 8661 was closed unmerged.

**Impact.** IO-bound jobs would stop holding CPU slots and delaying gossip verification under load; the gain is mainly in tail latency under load and is hard to quantify.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:130`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L130) one max_workers = num_cpus
- [`beacon_node/beacon_processor/src/lib.rs:890`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L890) can_spawn = current_workers &lt; max_workers for all work
- [`beacon_node/beacon_processor/src/lib.rs:1636-1637`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1636-L1637) every spawned item, async (tokio) or blocking, takes a worker slot until SendOnDrop
- [`common/task_executor/src/rayon_pool_provider.rs:8-38`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/task_executor/src/rayon_pool_provider.rs#L8-L38) rayon High/LowPriority pools are CPU-priority pools, used only for backfill (lib.rs:1728)

**Second check.** Also checked the Blocking/Async split in spawn_worker and the rayon priority pools; async tasks still count against max_workers, and the rayon pools split by priority, not by CPU vs IO.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [lighthouse#8661](https://github.com/sigp/lighthouse/pull/8661)

</details>


<a id="block_import-002"></a>
<details>
<summary><b>block_import-002</b> Wait for data availability before entering serial import queue — <i>implemented · medium · S · latency</i></summary>

**Idea.** Wait for the execution payload envelope's (or block's) data availability before taking a slot in the serial block import queue. A slow DA wait then does not block other queued imports behind it.

**Impact.** A slow DA wait holds no worker or queue slot, so there is no head-of-line blocking of other imports.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:4055-4058`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4055-L4058) process_block returns MissingComponents immediately instead of waiting for DA
- [`beacon_node/beacon_chain/src/pending_payload_cache/mod.rs:1-12`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/mod.rs#L1-L12) Gloas envelopes and columns wait in a cache keyed by block root
- [`beacon_node/beacon_processor/src/lib.rs:904-948`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L904-L948) blocks are processed by parallel workers, not in one serial import queue

**Skeptic check.** Confirmed that LH has no serial import queue that waits on DA: a block with missing data is parked in the DA checker and import finishes when the last component arrives. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#10485](https://github.com/ChainSafe/lodestar/pull/10485)

</details>


<a id="block_import-003"></a>
<details>
<summary><b>block_import-003</b> Send forkchoiceUpdated every sync-limit blocks during bulk sync — <i>implemented · low · S · sync</i></summary>

**Idea.** During range sync, trigger a forkchoiceUpdated to the EL every sync-limit batch of imported blocks instead of on a large fixed interval (or per block). The EL can then advance and prune at a cadence matched to its own batch limit.

**Impact.** Range sync sends forkchoiceUpdated once per batch, so the EL advances at a regular cadence, neither per block nor on a large fixed interval.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:640-660`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L640-L660) process_blocks calls recompute_head_at_current_slot once per processed chain segment (batch)
- [`beacon_node/beacon_chain/src/canonical_head.rs:1296`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1296) recompute_head spawns the EL forkchoiceUpdated

**Skeptic check.** Verified the per-batch head recompute in process_blocks. The Caplin PR is a one-line fix for an Erigon-embedded collector; matching an EL's internal limit does not apply to LH. Value lowered to low for that reason.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#10362](https://github.com/erigontech/erigon/pull/10362)

</details>


<a id="block_import-004"></a>
<details>
<summary><b>block_import-004</b> Propagate gossip blocks/envelopes before state transition and EL verdict — <i>implemented · high · S · latency</i></summary>

**Idea.** Accept and re-publish a gossip block or execution payload envelope right after the cheap spec gossip checks (proposer signature, equivocation), and run the state transition and EL verification after propagation. Propagation latency then does not include block processing time.

**Impact.** Block and envelope re-publish does not wait for the state transition or the EL verdict.

**Best measured result.** block_publishing_initiated +291ms before vs +3ms after; total 361ms -&gt; 315ms (pr:teku#8820)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1661`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1661) MessageAcceptance::Accept after verify_block_for_gossip, before process_gossip_verified_block (state transition, EL)
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:3856`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L3856) envelope Accept after verify_envelope_for_gossip, before process_gossip_verified_execution_payload_envelope
- [`beacon_node/beacon_chain/src/payload_envelope_verification/gossip_verified_envelope.rs:146-290`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/gossip_verified_envelope.rs#L146-L290) envelope gossip checks are consistency and signature only, no EL call

**Skeptic check.** Checked both the block path and the Gloas envelope path; both accept on gossip after cheap checks only. The earlier evidence covered blocks; envelopes are covered as well.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#25469](https://github.com/erigontech/erigon/pull/25469), [teku#8820](https://github.com/Consensys-Incorporated/teku/pull/8820), [prysm#2033](https://github.com/OffchainLabs/prysm/pull/2033)

</details>


<a id="block_import-005"></a>
<details>
<summary><b>block_import-005</b> Pre-advance head state to next slot and reuse it — <i>implemented · high · S · latency, cpu</i></summary>

**Idea.** After importing a block, use idle time in the slot to advance the head state through the next slot (and epoch) transition and cache it, then take the next block's pre-state from that cache instead of re-running slot/epoch processing on arrival.

**Impact.** The next block's pre-state comes pre-advanced from the state cache, so slot and epoch processing are not on the import path.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:126`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L126) head state advanced at 3/4 of the slot
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:258`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L258) advance_head runs per_slot_processing (including epoch processing), primes committee/shuffling/proposer caches, put_state
- [`beacon_node/beacon_chain/src/block_verification.rs:2065`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L2065) block pre-state loaded via get_advanced_hot_state

**Skeptic check.** This is Lighthouse's own PR #2174 and is present in current code. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#2174](https://github.com/sigp/lighthouse/pull/2174), [teku#3386](https://github.com/Consensys-Incorporated/teku/pull/3386), [prysm#12515](https://github.com/OffchainLabs/prysm/pull/12515)

</details>


<a id="block_import-006"></a>
<details>
<summary><b>block_import-006</b> Set head first, persist block and checkpoints afterwards — <i>partial · high · L · latency, disk</i></summary>

**Idea.** After a block is verified, update the canonical head first and persist the block, blobs, fork choice, justified checkpoint and op pool afterwards (or asynchronously through a write queue, serving unfinalized data from memory). Disk writes then do not delay the head update.

**Gap in Lighthouse.** Fork choice and op pool persistence are off the head path (lighthouse#2547), and a head-like view (fork choice get_head + early attester cache + SSE head events) is set before the DB write. The block, state and blob/column write is still synchronous inside import_block, under the fork choice write lock, and before recompute_head updates cached_head. Moving it out would need an in-memory unfinalized block/state/blob store and an async write queue in HotColdDB.

**Impact.** Removes a block+state+blob DB commit (tens of ms, more with columns) from the fork-choice write lock hold and the cached_head update; attestation already uses the early attester cache, so the gain is lock contention and head-update latency.

**Best measured result.** persisting head ~200ms; op pool persist up to 1.2s removed from head path (pr:lighthouse#2547)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:4555`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4555) fork_choice.get_head runs inside import_block before the DB write
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4572`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4572) early_attester_cache.add_head_block makes the new head attestable before the DB write; head/head_v2 SSE events also fire here
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4756`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4756) do_atomically_with_block_and_blobs_cache writes block+state+blobs synchronously while the fork choice write lock is held (dropped at 4769)
- [`beacon_node/store/src/hot_cold_store.rs:1459`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1459) do_atomically_with_block_and_blobs_cache is a synchronous batch commit with no write queue
- [`beacon_node/beacon_chain/src/canonical_head.rs:1565`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1565) persist_fork_choice only on epoch transition or reorg
- [`beacon_node/beacon_chain/src/beacon_chain.rs:8464`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L8464) persist_op_pool only at shutdown

**Second check.** Checked that get_head and early-attester/SSE head events run before the DB write (more than the earlier review stated), and that HotColdDB has no async write queue or deferred commit path.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [lodestar#8784](https://github.com/ChainSafe/lodestar/pull/8784), [prysm#9651](https://github.com/OffchainLabs/prysm/pull/9651), [lighthouse#2547](https://github.com/sigp/lighthouse/pull/2547)

</details>


<a id="block_import-007"></a>
<details>
<summary><b>block_import-007</b> Overlap EL calls with import work; Arc-shared blocks — <i>implemented · medium · S · latency, cpu, memory</i></summary>

**Idea.** Make block import and fork choice async so EL calls overlap with other work (state transition vs newPayload, head update vs forkchoiceUpdated), and pass blocks between stages behind a shared pointer instead of cloning them per stage.

**Impact.** newPayload overlaps with the state transition, fcU runs off the head-update path, and blocks are not cloned per stage.

**Best measured result.** avoids cloning blocks at least 2 times per block processing (pr:lighthouse#3244)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1561-1571`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1561-L1571) notify_new_payload spawned as a task concurrent with the state transition
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4099-4103`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4099-L4103) into_executed_block awaits payload_verification_handle afterwards
- [`beacon_node/beacon_chain/src/canonical_head.rs:1296`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1296) spawn_execution_layer_updates runs forkchoiceUpdated asynchronously
- [`beacon_node/beacon_chain/src/block_verification.rs:742`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L742) blocks passed as Arc&lt;SignedBeaconBlock&gt;

**Skeptic check.** This is Lighthouse's own PR #3244. Confirmed the spawned payload verification handle and the async EL updates; the earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#3244](https://github.com/sigp/lighthouse/pull/3244)

</details>


<a id="block_import-008"></a>
<details>
<summary><b>block_import-008</b> Fetch block pre-state asynchronously without blocking threads — <i>n/a · low · latency</i></summary>

**Idea.** Retrieve or regenerate the block's pre-state asynchronously so block import threads are not blocked on a DB read or state replay.

**Impact.** Block verification runs on the beacon processor's blocking worker pool, not on async executor threads, so DB reads do not block the runtime.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:2009`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L2009) load_parent runs synchronously inside beacon processor blocking workers

**Sources.** [teku#2364](https://github.com/Consensys-Incorporated/teku/pull/2364)

</details>


<a id="block_import-009"></a>
<details>
<summary><b>block_import-009</b> Avoid copying or cloning blocks through queues and verification — <i>partial · low · S · cpu, memory, latency</i></summary>

**Idea.** Pass blocks and sidecars through the sync, gossip, clearance and import verification stages as one shared or owned object (reference, pointer or moved value) instead of copying, cloning or converting them at each step. This saves the memcpy and allocation of large blocks.

**Gap in Lighthouse.** Verification and queues pass Arc&lt;SignedBeaconBlock&gt;, but the storage step deep-clones the full block on every import: HotColdDB::do_atomically handles StoreOp::PutBlock with block.as_ref().clone() so block_as_kv_store_ops can split the owned block into blinded block + payload and then rebuild it (try_into_full_block), only to serialise both. Backfill (historical_blocks.rs:200) does the same with (*block).clone(). When the block cache is enabled, BlockCache::put_block takes a second owned clone because the cache stores SignedBeaconBlock, not Arc. Fix: serialise blinded header/body and payload by reference (no ownership split) and make BlockCache hold Arc&lt;SignedBeaconBlock&gt;.

**Impact.** One full block deep copy (payload transactions, attestations) per imported block and per backfilled block when payloads are kept; a few hundred KB memcpy+alloc, small against import time.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:742`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L742)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4751`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4751)
- [`beacon_node/store/src/hot_cold_store.rs:1299-1304`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1299-L1304)
- [`beacon_node/store/src/hot_cold_store.rs:527-549`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L527-L549)
- [`beacon_node/store/src/hot_cold_store.rs:1599-1600`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1599-L1600)
- [`beacon_node/store/src/hot_cold_store.rs:96`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L96)
- [`beacon_node/beacon_chain/src/historical_blocks.rs:200`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_blocks.rs#L200)

**Skeptic check.** Confirmed blocks travel as Arc through gossip, sync (RangeSyncBlock) and verification, as the earlier evidence said; but the earlier check stopped before the DB write, where hot_cold_store.rs:1302 clones the whole block to consume it in block_as_kv_store_ops.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [nimbus#2610](https://github.com/status-im/nimbus-eth2/pull/2610), [nimbus#7546](https://github.com/status-im/nimbus-eth2/pull/7546), [lighthouse@c278c08e3](https://github.com/sigp/lighthouse/commit/c278c08e34ee), [lighthouse#1448](https://github.com/sigp/lighthouse/pull/1448), [nimbus#2698](https://github.com/status-im/nimbus-eth2/pull/2698)

</details>


<a id="block_import-010"></a>
<details>
<summary><b>block_import-010</b> Reuse held fork choice read lock in block verification — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Pass an already-held fork choice read lock into block verification helpers instead of releasing it and re-acquiring it in each helper. This avoids lock contention and inconsistent views between steps.

**Impact.** Gossip block verification takes one fork choice read lock and passes it by reference to check_block_is_finalized_checkpoint_or_descendant and verify_parent_block_and_envelope_are_known; the remaining separate acquisitions (check_block_relevancy at 1950, load_parent at 2025 on the RPC path) are short uncontended read locks in different stages.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:970-1000`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L970-L1000)
- [`beacon_node/beacon_chain/src/block_verification.rs:981-989`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L981-L989)
- [`beacon_node/beacon_chain/src/block_verification.rs:1987-2001`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1987-L2001)
- [`beacon_node/beacon_chain/src/block_verification.rs:1834-1839`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1834-L1839)

**Skeptic check.** Verified the gossip path matches PRs #4978/#4688 (lock held across helpers, dropped at 1000). The RPC/sync path still re-takes read locks in check_block_relevancy and load_parent, but that is not the immediate release/re-acquire bounce the idea targets and has negligible cost.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#4978](https://github.com/sigp/lighthouse/pull/4978), [lighthouse#4688](https://github.com/sigp/lighthouse/pull/4688)

</details>


<a id="block_import-011"></a>
<details>
<summary><b>block_import-011</b> Use block&#x27;s own payload status instead of fork choice lookup — <i>implemented · low · S · latency</i></summary>

**Idea.** During import, read the payload status already known for the incoming block instead of querying fork choice for it, avoiding a fork choice lock and lookup on the import path.

**Impact.** The import path uses the incoming status; the remaining lookup needs no extra lock and is an in-memory proto-array read.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:4434`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4434) payload_verification_status from the verified payload outcome passed into import_block
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4539`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4539) fork_choice.on_block receives it as a parameter
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4563`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4563) the only status lookup after on_block runs under the already-held fork choice write lock to gate the early attester cache

**Skeptic check.** Prysm#12559 removed a fork choice IsOptimistic call used for the finalized event. LH passes the payload status into on_block and does no separate locked lookup on import. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#12559](https://github.com/OffchainLabs/prysm/pull/12559)

</details>


<a id="block_import-012"></a>
<details>
<summary><b>block_import-012</b> Non-blocking queue push instead of a future per item — <i>n/a · low · cpu, memory</i></summary>

**Idea.** In the gossip processing pipeline, push work items into queues with a non-blocking add instead of spawning an async task/future per item. This avoids task scheduling overhead and copies of the item into each task.

**Impact.** Beacon processor pushes items into in-memory queues and spawns only when a worker is free.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:1312`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1312) work pushed to preallocated queues in the manager loop, no task per item

**Sources.** [nimbus#2157](https://github.com/status-im/nimbus-eth2/pull/2157)

</details>


<a id="block_import-013"></a>
<details>
<summary><b>block_import-013</b> Skip head block DB read unless block can change head — <i>n/a · low · disk, latency</i></summary>

**Idea.** On block receipt, load the current head block from the DB only when the new block can change the head (for example its parent root is not the head root), instead of on every block.

**Impact.** Head block is held in memory (cached_head snapshot), so there is no per-block head DB read to skip.

**Evidence (Lighthouse @ 928b61e719).**

- beacon_chain/src/canonical_head.rs:735 head_beacon_block returns Arc from in-memory cached head
- beacon_chain/src/block_verification.rs:2023 load_parent checks fork choice, reads only the parent

**Sources.** [prysm#4506](https://github.com/OffchainLabs/prysm/pull/4506), [prysm#4518](https://github.com/OffchainLabs/prysm/pull/4518)

</details>


<a id="block_import-014"></a>
<details>
<summary><b>block_import-014</b> Do not retain BeaconStates in long-lived tasks and channels — <i>implemented · high · S · memory, latency</i></summary>

**Idea.** Do not keep BeaconState values in forkchoice-update arguments, background migrator channel messages or post-transition event handlers; send only roots or checkpoints and load what is needed. Old states are then freed instead of pinned in memory by slow or queued work.

**Impact.** Migrator Notification variants carry only state roots and checkpoints; spawn_execution_layer_updates carries ForkchoiceUpdateParameters (hashes/roots), recompute_head tasks capture only the chain Arc and slot.

**Best measured result.** Retained state memory 615MB to 77MB (pr:lodestar#2184)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/migrate.rs:121-138`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L121-L138)
- [`beacon_node/beacon_chain/src/migrate.rs:165-183`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L165-L183)
- [`beacon_node/beacon_chain/src/canonical_head.rs:1724-1731`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1724-L1731)
- [`beacon_node/beacon_chain/src/canonical_head.rs:1885-1912`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1885-L1912)

**Skeptic check.** Checked migrator messages, the EL forkchoice-update task and other spawned post-import tasks; none hold a BeaconState. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#16361](https://github.com/OffchainLabs/prysm/pull/16361), [lighthouse#1923](https://github.com/sigp/lighthouse/pull/1923), [lodestar#2184](https://github.com/ChainSafe/lodestar/pull/2184)

</details>


<a id="block_import-015"></a>
<details>
<summary><b>block_import-015</b> Send forkchoiceUpdated in background, publish head early — <i>partial · medium · S · latency, cpu</i></summary>

**Idea.** Do not make block import and its callers wait for the forkchoiceUpdated EL round trip; send fcU in a background or concurrent task and publish the new head (events, API, attestation data) without waiting for the reply. Also skip a redundant second fcU and the epoch transition before payload attributes where not needed.

**Gap in Lighthouse.** Cached head and head/SSE events (after_new_head) are published before fcU, and fcU runs in a spawned task, but recompute_head_at_slot still awaits the EL join handle, so every gossip/sync/API caller waits for the fcU round trip (plus prepare_beacon_proposer). The first fcU already carries cached payload attributes when present (execution_layer lib.rs:1579), but prepare_beacon_proposer can still send a second one. Fix: stop awaiting el_update_handle in recompute_head_at_slot outside tests, and skip the second fcU when attributes were already sent with the first.

**Impact.** Frees the beacon-processor worker and import caller for the fcU round trip (Caplin measured 0.23 s median); head is already visible to API/events earlier.

**Best measured result.** EL head commit delay of 0.23 s median, 0.35 s p90 between block event and head event removed (pr:caplin#25581)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:1190`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1190)
- [`beacon_node/beacon_chain/src/canonical_head.rs:1208`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1208)
- [`beacon_node/beacon_chain/src/canonical_head.rs:1296`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1296)
- [`beacon_node/beacon_chain/src/canonical_head.rs:796`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L796)
- [`beacon_node/beacon_chain/src/canonical_head.rs:1895`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1895)
- [`beacon_node/beacon_chain/src/canonical_head.rs:1931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1931)
- [`beacon_node/execution_layer/src/lib.rs:1579`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1579)
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1008`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1008)

**Second check.** Confirmed that head events fire before the EL update and that notify_forkchoice_updated already attaches cached payload attributes to the first fcU, which reduces the double-fcU case to when the cache misses; the await of the join handle at canonical_head.rs:796 is still there.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [prysm#16149](https://github.com/OffchainLabs/prysm/pull/16149), [nimbus#3842](https://github.com/status-im/nimbus-eth2/pull/3842), [nimbus#3880](https://github.com/status-im/nimbus-eth2/pull/3880), [caplin#25581](https://github.com/erigontech/erigon/pull/25581)

</details>


<a id="block_import-016"></a>
<details>
<summary><b>block_import-016</b> Run finalization migration and pruning after import in background — <i>implemented · medium · S · latency</i></summary>

**Idea.** Run hot-to-cold state migration, storage rebase and pruning on finalization in a background task (guarded against concurrent runs) after the block is imported and the head updated, not inline in block processing.

**Impact.** Hot-to-cold migration and blob pruning run on a single dedicated migrator thread that coalesces queued notifications to the latest finalized checkpoint (no concurrent runs). Inline work left in after_finalization: op_pool.prune_all, persist_fork_choice and fork_choice_write_lock().prune(), all small next to migration.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/migrate.rs:165-183`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L165-L183)
- [`beacon_node/beacon_chain/src/migrate.rs:434-494`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L434-L494)
- [`beacon_node/beacon_chain/src/canonical_head.rs:1714-1741`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1714-L1741)

**Skeptic check.** Verified process_finalization sends to the background thread and the thread loop drains and coalesces messages, which also gives the concurrent-run guard. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#11501](https://github.com/OffchainLabs/prysm/pull/11501), [silver#363](https://github.com/gattaca-com/silver/pull/363)

</details>


<a id="block_import-017"></a>
<details>
<summary><b>block_import-017</b> Batch-verify all signatures of a chain segment — <i>partial · medium · M · cpu, sync</i></summary>

**Idea.** When importing a chain segment during sync (or a single block through the same pipeline), collect the signature sets of all its blocks into one batched BLS verification and mark the blocks signature-verified, instead of verifying per block. Carry gossip verification results to import so they are not redone.

**Gap in Lighthouse.** Block signatures of a same-epoch chain segment are batched in signature_verify_chain_segment, and gossip results carry to import via from_gossip_verified_block. But post-Gloas range sync takes the envelopes out before batching (beacon_chain.rs:3289) and verifies each one later in process_range_sync_envelope with verify_execution_payload_envelope(VerifySignatures::True), one builder signature check per block, and this runs inside the async fn, not the blocking pool. The envelope signature sets should go into the same batch verifier in signature_verify_chain_segment (backfill already batches self-built envelope signatures).

**Impact.** Post-Gloas range sync does one separate pairing check per block for envelopes (about 32 per epoch batch) instead of a share of one multi-pairing; this also blocks an async worker.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:671-733`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L671-L733)
- [`beacon_node/beacon_chain/src/block_verification.rs:1255-1280`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1255-L1280)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3289-3300`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3289-L3300)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3366-3376`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3366-L3376)
- [`beacon_node/beacon_chain/src/payload_envelope_verification/import.rs:420-438`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/import.rs#L420-L438)
- [`beacon_node/beacon_chain/src/historical_blocks.rs:352-363`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_blocks.rs#L352-L363)

**Skeptic check.** Confirmed block batching and gossip carry-over as earlier evidence said; the earlier check missed that Gloas envelopes in process_chain_segment bypass the batch and are verified one by one.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [prysm#7244](https://github.com/OffchainLabs/prysm/pull/7244), [lodestar@4f15d28b4](https://github.com/ChainSafe/lodestar/commit/4f15d28b457a), [lodestar#1966](https://github.com/ChainSafe/lodestar/pull/1966), [lighthouse#913](https://github.com/sigp/lighthouse/pull/913), [lodestar#4317](https://github.com/ChainSafe/lodestar/pull/4317)

</details>


<a id="block_import-018"></a>
<details>
<summary><b>block_import-018</b> Rebuild participation flags tree once for overlapping attestations — <i>implemented · medium · S · cpu</i></summary>

**Idea.** When many attestations in a block touch the same validators, apply all participation flag updates to a flat array and rebuild the participation list/tree once instead of updating each validator's leaf individually.

**Impact.** Per-validator get_mut/add_flag writes only to milhouse's pending update map; the participation tree is rebuilt once per list in apply_updates (backing.update with all updates) when pending mutations are applied before hashing.

**Best measured result.** altair block processing 40% faster (pr:lodestar#3225)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/process_operations.rs:258-290`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L258-L290)
- d67aabd/src/interface.rs:68-71
- d67aabd/src/interface.rs:86-101
- [`consensus/types/src/state/beacon_state.rs:3071`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3071)

**Second check.** The earlier review missed milhouse's Interface layer. List::get_mut copies the value on write into a MaxMap&lt;VecMap&gt; update buffer and does not touch the tree. Interface::apply_updates then rebuilds the packed participation tree once for all attestations in the block, which is the mechanism Lodestar added in #3225.

**Skeptic check.** Verified the milhouse revision in Cargo.lock (d67aabd): Interface::get_mut goes to the updates map, and apply_updates does one batched tree update. Same effect as the Lodestar flat-array approach; earlier evidence was right.

**Verdict history.** not (checked) → implemented (refuted) → implemented (skeptic)

**Sources.** [lodestar#3225](https://github.com/ChainSafe/lodestar/pull/3225)

</details>


<a id="block_import-019"></a>
<details>
<summary><b>block_import-019</b> Verify all block signatures in one batch including sync aggregate — <i>implemented · high · S · cpu</i></summary>

**Idea.** Collect every signature of a block (proposer, randao, attestations, slashings, exits, sync aggregate) into one set and verify it with a single multi-pairing batch check instead of one by one.

**Impact.** One batched verify covers proposal, randao, proposer/attester slashings, attestations, exits, sync aggregate, BLS changes, and Gloas bid and payload attestations; ParallelSignatureSets splits it across rayon chunks.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/block_signature_verifier.rs:151-187`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/block_signature_verifier.rs#L151-L187)
- [`consensus/state_processing/src/per_block_processing/block_signature_verifier.rs:430-436`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/block_signature_verifier.rs#L430-L436)
- [`beacon_node/beacon_chain/src/block_verification.rs:1205-1210`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1205-L1210)

**Skeptic check.** Confirmed include_all_signatures_except_proposal adds every block signature type, including the sync aggregate and Gloas additions, and verify() runs once. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#4010](https://github.com/Consensys-Incorporated/teku/pull/4010), [lighthouse#739](https://github.com/sigp/lighthouse/pull/739)

</details>


<a id="block_import-020"></a>
<details>
<summary><b>block_import-020</b> Batch block, head and state DB writes during sync — <i>partial · medium · M · sync, disk, latency, cpu</i></summary>

**Idea.** During initial/batch sync, hold imported blocks in memory and write blocks, head root and states to the DB once per batch or at finalization instead of on every imported block. Avoid triggers that flush every slot, such as rewriting an unchanged finalized checkpoint or DB lookups of attestation targets.

**Gap in Lighthouse.** Head and fork-choice persistence is already not per block, and most hot states are small summaries. Missing: blocks, summaries and blobs/columns are still committed in one DB transaction per block during range sync. A fix would accumulate ops across a segment in process_chain_segment and flush once, keeping fork choice and DB consistent on write failure (handle_import_block_db_write_error).

**Impact.** Fewer DB commits during range sync; modest gain because states are already summaries. The Prysm 80-100% figure is unlikely to transfer.

**Best measured result.** 80-100% faster blocks per second (pr:prysm#5215)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:3322`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3322) process_chain_segment imports each signature-verified block through process_block one at a time
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4751`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4751) PutBlock+PutState pushed into per-block ops
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4756`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4756) do_atomically_with_block_and_blobs_cache once per imported block
- [`beacon_node/beacon_chain/src/canonical_head.rs:1565`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1565) fork choice/head persisted only on epoch transition or reorg
- [`beacon_node/store/src/hot_cold_store.rs:1697`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1697) hot state stored as summary if not at a diff/snapshot boundary

**Second check.** Re-read the segment import loop and the per-block write path; found no deferred or batched write mode for range sync in beacon_chain or the store.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [prysm#5215](https://github.com/OffchainLabs/prysm/pull/5215), [prysm#9244](https://github.com/OffchainLabs/prysm/pull/9244), [prysm#6584](https://github.com/OffchainLabs/prysm/pull/6584), [prysm#6599](https://github.com/OffchainLabs/prysm/pull/6599), [prysm#4219](https://github.com/OffchainLabs/prysm/pull/4219), [prysm#5293](https://github.com/OffchainLabs/prysm/pull/5293)

</details>


<a id="block_import-021"></a>
<details>
<summary><b>block_import-021</b> Insert sync blocks into EL in rounds bounded by limit — <i>n/a · low · sync, disk, latency</i></summary>

**Idea.** During bulk block download, insert blocks into the execution client and execute them in rounds bounded by the EL's sync batch limit, instead of inserting a very large amount at once.

**Impact.** Lighthouse sends engine_newPayload per block, no bulk EL insertion path exists; EL sync batching is the EL's job.

**Evidence (Lighthouse @ 928b61e719).**

- beacon_chain/src/beacon_chain.rs:3235 process_chain_segment imports in epoch chunks, each block does its own newPayload

**Sources.** [caplin#10341](https://github.com/erigontech/erigon/pull/10341)

</details>


<a id="block_import-022"></a>
<details>
<summary><b>block_import-022</b> Run sanity checks over whole block segment at once — <i>implemented · low · S · cpu, sync</i></summary>

**Idea.** When importing a chain segment, run the known/slot/parent/finality sanity checks over the whole segment in one pass and apply the chain-tip-only checks to the last block only.

**Impact.** Segment sanity checks already run in one pass; the per-block checks are cheap in-memory lookups.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:3068`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3068) filter_chain_segment checks linearity, fork and relevancy for the whole segment in one pass
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3132`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3132) check_block_relevancy per block skips known or finalized blocks
- [`beacon_node/beacon_chain/src/block_verification.rs:671`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L671) signature_verify_chain_segment batches signatures and loads the parent once

**Skeptic check.** Verified that filter_chain_segment does the batched known/slot/parent/finality filtering that lodestar's verifyBlocksSanityChecks added. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#4318](https://github.com/ChainSafe/lodestar/pull/4318)

</details>


<a id="block_import-023"></a>
<details>
<summary><b>block_import-023</b> Blacklist descendants of known-bad blocks — <i>partial · medium · S · cpu</i></summary>

**Idea.** When a block's parent root is in the invalid-block blacklist, add the block to the blacklist and reject it without processing, so whole bad chains are dropped cheaply.

**Gap in Lighthouse.** Pending descendants of a failed lookup are dropped together, and EL-invalid descendants are rejected through fork choice. Missing: a consensus-invalid block root is not remembered, so a later child of it starts a new parent lookup that downloads and processes the bad parent again. ignored_chains is filled only on chain-too-long. Fix: insert the root into ignored_chains (or a BeaconChain LRU checked by parent_root in check_invalid_block_roots) on a consensus processing failure.

**Impact.** Negligible on mainnet; only saves repeated download and processing of bad chains.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:3879`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3879) check_invalid_block_roots checks only the static config set
- [`beacon_node/beacon_chain/src/chain_config.rs:108`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/chain_config.rs#L108) invalid_block_roots is a static HashSet, never changed at runtime
- [`beacon_node/beacon_chain/src/block_verification.rs:1500`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1500) child of an EL-invalid parent rejected through fork choice
- [`beacon_node/network/src/sync/block_lookups/mod.rs:616`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L616) drop_lookup_and_children drops all pending descendants when a lookup fails (mod.rs:695)
- [`beacon_node/network/src/sync/block_lookups/mod.rs:282`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L282) ignored_chains is filled only for too-long parent chains; mod.rs:369 checks it
- [`beacon_node/network/src/sync/range_sync/range.rs:77`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/range.rs#L77) failed_chains LRU keyed by remote finalized root, 30s

**Second check.** Checked as well the lookup failure path (drop_lookup_and_children), every insert into ignored_chains, and range sync failed_chains. None records a block that failed consensus as bad for its descendants.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [lodestar#7500](https://github.com/ChainSafe/lodestar/pull/7500), [grandine#155](https://github.com/grandinetech/grandine/pull/155)

</details>


<a id="block_import-024"></a>
<details>
<summary><b>block_import-024</b> Read previous block root from state block_roots — <i>implemented · low · S · disk, latency</i></summary>

**Idea.** Get the previous block root from the state's block_roots history vector instead of a database read.

**Impact.** There is no DB read for the previous block root; nothing to save.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:1276`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1276) get_block_root reads the block_roots vector
- [`beacon_node/beacon_chain/src/block_verification.rs:2045`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L2045) parent root taken from block.parent_root()

**Skeptic check.** LH takes block roots from the state vector or the block header. The prysm PR was closed unmerged, and nothing equivalent is missing. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#2003](https://github.com/OffchainLabs/prysm/pull/2003)

</details>


<a id="block_import-025"></a>
<details>
<summary><b>block_import-025</b> Process gossip blocks on blocking executor, not async core — <i>partial · high · S · latency, cpu</i></summary>

**Idea.** Run gossip block processing on a worker in the blocking executor instead of on the core async executor, so CPU-heavy block verification does not stall async networking tasks; ignore gossip blocks while syncing.

**Gap in Lighthouse.** Gossip verification and import_block (the fork choice update and DB write) run on the blocking pool. The heavy middle step, into_execution_pending_block (signature batch verification, state catch-up, per_block_processing, tree hash), runs synchronously on a tokio core worker. Fix: wrap it in spawn_blocking_handle. I found no ignore-gossip-blocks-while-syncing check in the gossip block path.

**Impact.** Frees a tokio worker for tens to ~100 ms per block so libp2p and other async tasks are not stalled during import; small gain on multi-core nodes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:1705`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1705) Work::GossipBlock dispatched with task_spawner.spawn_async (lib.rs:1776 spawns on the main tokio executor)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3406`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3406) gossip verification runs in spawn_blocking_handle
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3973`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3973) into_execution_pending_block (sync: signature verification, state advance, per_block_processing at block_verification.rs:1706) is called inline inside the async import future
- [`beacon_node/beacon_chain/src/block_verification.rs:1566`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1566) only the EL newPayload call is spawned as a separate task
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4428`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4428) import_block itself runs in spawn_blocking_handle

**Second check.** Confirmed that import_block and the gossip checks run on the blocking pool but into_execution_pending_block does not; lighthouse#1523's blocking-executor design was later replaced by spawn_async. The only spawned subtask is the EL newPayload call.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [lighthouse#1523](https://github.com/sigp/lighthouse/pull/1523)

</details>


<a id="block_import-026"></a>
<details>
<summary><b>block_import-026</b> Bound pending and future block queues by count and bytes — <i>partial · medium · S · memory</i></summary>

**Idea.** Limit the queues of future-slot blocks and of blocks with unknown parents by count per slot and by total bytes, sized for the decoded in-heap size (4-5x SSZ), evicting the furthest-future entries first, so peers cannot grow memory without limit.

**Gap in Lighthouse.** Queues are bounded by count only and drop the newcomer when full. There is no byte budget for decoded size and no per-slot cap. Evicting the furthest-future block matters little because gossip rejects future blocks beyond clock disparity. Fix: add a byte counter to the lookup store of downloaded blocks and columns.

**Impact.** Bounds worst-case memory under a hostile peer; count caps already keep it to tens of MB.

**Best measured result.** Stated: ~1 GB potential heap down to a few hundred MB; observed peak 1.97 MB (pr:teku#11435)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:78`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L78) MAXIMUM_QUEUED_BLOCKS=16; newcomer dropped when full (line 670-679)
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:664`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L664) duplicate roots refused
- [`beacon_node/beacon_chain/src/block_verification.rs:922`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L922) FutureSlot rejection beyond clock disparity, so the early queue only holds blocks for the next instant
- [`beacon_node/network/src/sync/block_lookups/mod.rs:408`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L408) MAX_LOOKUPS=200 cap on unknown-parent lookups; mod.rs:276 PARENT_DEPTH_TOLERANCE

**Second check.** Confirmed that the FutureSlot gossip check bounds how far in the future early blocks can be, which makes the evict-furthest part mostly moot. Found no byte-based accounting in the reprocess queue or block_lookups.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [teku#11434](https://github.com/Consensys-Incorporated/teku/pull/11434), [nimbus#1564](https://github.com/status-im/nimbus-eth2/pull/1564), [teku#11435](https://github.com/Consensys-Incorporated/teku/pull/11435)

</details>


<a id="block_import-027"></a>
<details>
<summary><b>block_import-027</b> Cap delayed execution payload envelope queue — <i>implemented · low · S · memory</i></summary>

**Idea.** Put a maximum size on the delayed queue of execution payload envelopes that wait for their block, with separate limits for gossip and requested envelopes, and evict the highest-slot envelope (or reject) when full.

**Impact.** Early-envelope and awaiting-block envelope queues are each capped at 16, with dedup by block root and a one-slot timeout, and new envelopes are dropped when full. Requested envelopes go through bounded sync lookups; the local PendingPayloadEnvelopes cache is pruned by slot age.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:80-81`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L80-L81)
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:713-736`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L713-L736)
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:779-799`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L779-L799)
- [`beacon_node/beacon_chain/src/pending_payload_envelopes.rs:85-90`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_envelopes.rs#L85-L90)

**Skeptic check.** Verified both caps and the drop-on-full behaviour. The eviction policy differs from Grandine's (drop the new one, not evict the highest slot), but memory is bounded the same way.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine@ac21ead8f](https://github.com/grandinetech/grandine/commit/ac21ead8f363), [grandine@29750218c](https://github.com/grandinetech/grandine/commit/29750218c4a4), [grandine#931](https://github.com/grandinetech/grandine/pull/931)

</details>


<a id="block_import-028"></a>
<details>
<summary><b>block_import-028</b> Requeue RPC blocks only before attestation deadline — <i>not · low · S · cpu</i></summary>

**Idea.** Re-queue an early RPC block for delayed processing only if it arrived before the attestation deadline, to break requeue loops, and check whether the proposal is already known lazily so the observed-proposers lock is not taken needlessly.

**Gap in Lighthouse.** The old early-RPC-block requeue loop (observed-proposer based) no longer exists; the current requeue keys on in-flight duplicate_cache, so there is no loop to break and no lateness check is needed. Nothing to add.

**Impact.** Negligible: the loop this guarded against was removed with the redesign.

**Evidence (Lighthouse @ 928b61e719).**

- network/src/network_beacon_processor/sync_methods.rs:117 process_lookup_block requeues via duplicate_cache only when a gossip import of the same root is in flight
- beacon_processor/src/scheduler/work_reprocessing_queue.rs:805 RpcBlock requeued for fixed QUEUED_RPC_BLOCK_DELAY
- beacon_chain/src/observed_block_producers.rs:135 proposer_has_been_observed no longer used on the RPC path

**Sources.** [lighthouse#4208](https://github.com/sigp/lighthouse/pull/4208)

</details>


<a id="block_import-029"></a>
<details>
<summary><b>block_import-029</b> Compute base_reward_per_increment once per block — <i>implemented · low · S · cpu</i></summary>

**Idea.** Compute base_reward_per_increment (integer sqrt of total active balance) once per block or epoch and pass it into attestation processing instead of recomputing it per attestation.

**Impact.** None left: the epoch cache computes BaseRewardPerIncrement once per epoch and precomputes base rewards per effective-balance step; attestation processing only reads that table. One isqrt per block remains in sync aggregate rewards.

**Best measured result.** non-epoch slot with block 851 ms -&gt; 70 ms avg, 60k validators (pr:nimbus#2681)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/epoch_cache.rs:93-113`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/epoch_cache.rs#L93-L113)
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:280`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L280),421
- [`consensus/state_processing/src/per_block_processing/altair/sync_committee.rs:93`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/altair/sync_committee.rs#L93)

**Skeptic check.** Confirmed the epoch cache build and the cached get_base_reward lookups in Altair+ attestation processing. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#2681](https://github.com/status-im/nimbus-eth2/pull/2681)

</details>


<a id="block_import-030"></a>
<details>
<summary><b>block_import-030</b> Cache block roots that failed inclusion list check — <i>n/a · low · cpu</i></summary>

**Idea.** Remember block roots that failed the inclusion-list satisfaction check so the check is not re-run for the same block.

**Impact.** Inclusion-list satisfaction check is a future-fork feature absent from Lighthouse block import.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/pubsub.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs): no inclusion list block check in block import path

**Sources.** [teku#9579](https://github.com/Consensys-Incorporated/teku/pull/9579)

</details>


<a id="block_import-031"></a>
<details>
<summary><b>block_import-031</b> Keep latest finalized state in memory for import — <i>n/a · low · cpu, disk, latency</i></summary>

**Idea.** Cache the latest finalized state in memory so block import does not read it from storage on every block.

**Impact.** Block import needs the parent state, not the finalized state; finalized checkpoint comes from the cached head and fork choice, no storage read.

**Evidence (Lighthouse @ 928b61e719).**

- beacon_chain/src/block_verification.rs:2063 get_advanced_hot_state loads parent state from hot cache/DB
- beacon_chain/src/canonical_head.rs:735 cached head holds finalized checkpoint

**Sources.** [teku#3033](https://github.com/Consensys-Incorporated/teku/pull/3033)

</details>


<a id="block_import-032"></a>
<details>
<summary><b>block_import-032</b> Cache genesis block root — <i>implemented · low · S · cpu</i></summary>

**Idea.** Cache the genesis block root at startup so block processing does not recompute or look it up repeatedly.

**Impact.** Genesis root is a cached field.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:488`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L488) genesis_block_root field on BeaconChain
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1052`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1052) returns self.genesis_block_root for slot 0

**Skeptic check.** Verified genesis_block_root is a struct field set at startup. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#6069](https://github.com/OffchainLabs/prysm/pull/6069)

</details>


<a id="block_import-033"></a>
<details>
<summary><b>block_import-033</b> Compute indexed attestations once per block and reuse — <i>implemented · medium · S · cpu, latency, disk</i></summary>

**Idea.** Compute a block's indexed attestations once during signature verification and keep them in the block-processing context for per-block processing, fork choice and slasher instead of recomputing them. Also run payload verification before advancing/writing the pre-state and defer non-essential work until after the early attester cache is primed.

**Impact.** Already done. The cache key is tree_hash_root(attestation), so each lookup rehashes one small attestation. With at most 8 attestations per block after Electra, this cost is negligible.

**Best measured result.** eager state writes were adding ~20-30ms before payload verification; parallel attestation observation saves 5-10ms (pr:lighthouse#3696)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/consensus_context.rs:30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/consensus_context.rs#L30),161-195
- [`consensus/state_processing/src/per_block_processing/block_signature_verifier.rs:297`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/block_signature_verifier.rs#L297)
- [`consensus/state_processing/src/per_block_processing/verify_attestation.rs:92`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/verify_attestation.rs#L92)
- [`beacon_node/beacon_chain/src/block_verification.rs:1283`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1283),1561-1571,1764
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4572`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4572),4987,5054,5094

**Skeptic check.** The ConsensusContext carries indexed attestations from signature verification through per_block_processing, fork choice, the validator monitor, observation and the slasher. Payload verification is spawned before the state advance and the skip-slot state writes (#3696). The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#3696](https://github.com/sigp/lighthouse/pull/3696), [lodestar#8637](https://github.com/ChainSafe/lodestar/pull/8637)

</details>


<a id="block_import-034"></a>
<details>
<summary><b>block_import-034</b> Read active validator count from cached shuffling — <i>implemented · low · S · cpu</i></summary>

**Idea.** Take the active validator count from the cached epoch shuffling instead of filtering all validators of the post-state.

**Impact.** Block import and head paths read the cached shuffling; nothing left to save.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:389`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L389) active_validator_count from get_cached_active_validator_indices
- [`beacon_node/beacon_chain/src/early_attester_cache.rs:22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/early_attester_cache.rs#L22) uses committee cache indices
- [`beacon_node/beacon_chain/src/metrics.rs:2407`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/metrics.rs#L2407) scrape_head_state scans all validators, but only on metrics scrape and it needs slashed/withdrawn counts anyway

**Skeptic check.** No active-validator scan on block import or head update. The only full scan is in metrics scrape_head_state, which also counts slashed and withdrawn validators, so a cached count would not remove the scan (it also sums balances twice, a trivial separate waste). The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@e1bdf7fa1](https://github.com/ChainSafe/lodestar/commit/e1bdf7fa1bde)

</details>


<a id="block_import-035"></a>
<details>
<summary><b>block_import-035</b> Cancel-safe counter for signature batching decision — <i>n/a · low · S · cpu, latency</i></summary>

**Idea.** Make the pending-block-stores counter that decides whether signature verification can be batched exception- and cancel-safe (try/finally), so a cancelled store cannot leave it stuck and disable batching permanently.

**Gap in Lighthouse.** Nimbus async-cancellation counter; Lighthouse has no such shared counter and Rust drop semantics/blocking tasks are not cancelled mid-way.

**Impact.** None; no stuck counter can disable batching.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs): signature batching is decided per call, no global pending-store counter exists
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4454`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4454) import_block is sync under a blocking task

**Sources.** [nimbus#8457](https://github.com/status-im/nimbus-eth2/pull/8457)

</details>


<a id="block_import-036"></a>
<details>
<summary><b>block_import-036</b> Cancellable block collector flush on shutdown — <i>n/a · low · S · latency</i></summary>

**Idea.** Flush pending sync block batches with a cancellable context so shutdown does not wait for every batch queued behind the EL.

**Gap in Lighthouse.** Lighthouse has no collector buffering batches for the EL; shutdown just drops the task queue.

**Impact.** None; shutdown latency is not driven by a flush queue.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:3202`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3202) process_chain_segment processes batches sequentially via the beacon processor; no separate block-collector queue behind the EL
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs): per-batch work items

**Sources.** [caplin#24895](https://github.com/erigontech/erigon/pull/24895)

</details>


<a id="block_import-037"></a>
<details>
<summary><b>block_import-037</b> Import chain segment with one pre-state lookup — <i>partial · medium · M · cpu, sync</i></summary>

**Idea.** Import a segment of consecutive blocks with one pre-state lookup and carry the post-state forward from block to block, instead of loading or regenerating the pre-state per block.

**Gap in Lighthouse.** The first block reuses the segment pre-state. Every later block gets its pre-state again through load_parent and the state cache, instead of carrying the post-state forward. It is cheap when the cache hits. Fix: pass the post-state of block N into block N+1's PreProcessingSnapshot in process_chain_segment.

**Impact.** Saves one state cache lookup and clone plus one parent block read per block in range sync; under 1 ms per block when the cache hits.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:680`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L680) signature_verify_chain_segment does one load_parent for the segment
- [`beacon_node/beacon_chain/src/block_verification.rs:731`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L731) only the first block gets the loaded parent; others have parent: None (line 711)
- [`beacon_node/beacon_chain/src/block_verification.rs:1360-1364`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1360-L1364) blocks without parent call load_parent -&gt; get_advanced_hot_state
- [`beacon_node/store/src/hot_cold_store.rs:1130`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1130) state_cache hit on the previous block's post-state (cheap milhouse clone)

**Second check.** Found that the first block of the segment already reuses the signature-verification parent (line 731). This was not in the earlier review, but it confirms that the other blocks are not carried forward.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [lodestar@1b3a33391](https://github.com/ChainSafe/lodestar/commit/1b3a333912fa)

</details>


<a id="block_import-038"></a>
<details>
<summary><b>block_import-038</b> Evaluate cheap flags before 32-byte hash comparisons — <i>n/a · low · S · cpu</i></summary>

**Idea.** In short-circuit conditions on the import path, evaluate cheap boolean flags first and the 32-byte root comparison last.

**Gap in Lighthouse.** A 32-byte memcmp in Rust costs nanoseconds and the compiler/LLVM choices make the reorder immaterial; no hot site identified.

**Impact.** Negligible.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array) and beacon_chain import path use plain Hash256 equality; no hot short-circuit with a 32-byte compare ahead of a flag found

**Sources.** [nimbus@8db65ef57](https://github.com/status-im/nimbus-eth2/commit/8db65ef574e0)

</details>


<a id="block_import-039"></a>
<details>
<summary><b>block_import-039</b> Structural checks before pubkey collection and signature verification — <i>implemented · medium · S · cpu</i></summary>

**Idea.** Run cheap structural checks (for example attestation bits equal proof participants, bitfield lengths) before collecting public keys and verifying signatures, so malformed blocks are rejected without crypto work.

**Impact.** Malformed bitfields, bad committee indices and oversized operation lists are rejected while signature sets are collected, before the single batch verify. Pubkeys come from the decompressed pubkey cache.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/block_signature_verifier.rs:168-184`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/block_signature_verifier.rs#L168-L184),284-306,429-435
- [`consensus/state_processing/src/common/get_attesting_indices.rs:25-31`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/get_attesting_indices.rs#L25-L31),113-147
- [`beacon_node/beacon_chain/src/block_verification.rs:721`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L721),911-955

**Skeptic check.** All signature sets are collected first. Any structural error in get_indexed_attestation (bitlist length, committee_bits) aborts before ParallelSignatureSets::verify, and gossip runs the list-length and blob-count checks earlier. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [ethlambda#202](https://github.com/lambdaclass/ethlambda/pull/202)

</details>


<a id="block_import-040"></a>
<details>
<summary><b>block_import-040</b> Return early from post-block fcU when no payload attributes — <i>partial · low · S · cpu, memory, latency</i></summary>

**Idea.** In the post-block forkchoiceUpdated path, return early when there are no payload attributes (no local proposer next slot) before fetching or copying the head block.

**Gap in Lighthouse.** prepare_beacon_proposer exits early only when the EL holds no preparation data at all. On any node with an attached VC, each head change spawns a blocking task and runs overridden_forkchoice_update_params, which takes the fork choice lock. It also runs proposer_shuffling_decision_root_at_epoch and, post-gloas, a second fork choice read lock plus should_build_on_full. All of this runs before has_proposer_preparation_data(proposer) finds the next-slot proposer is not local. The fix: compute the proposer index from the proposer cache first and return before the head and fork choice work.

**Impact.** Saves one or two fork choice read locks and a blocking task per head change on non-proposing slots; the absolute time is small (microseconds), and there is no block copy because the head is an Arc.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:6737`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6737) early exit only when no proposer data is registered at all
- [`beacon_node/beacon_chain/src/beacon_chain.rs:6750`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6750) spawn_blocking head read: overridden_forkchoice_update_params (fork choice read lock, get_preliminary_proposer_head), get_pre_payload_attributes, proposer_shuffling_decision_root_at_epoch, and for gloas a second fork choice read lock plus should_build_on_full
- [`beacon_node/beacon_chain/src/beacon_chain.rs:6895`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6895) has_proposer_preparation_data(proposer) is checked only after all of that
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5531`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5531) overridden_forkchoice_update_params_or_failure_reason takes fork choice read lock
- [`beacon_node/beacon_chain/src/canonical_head.rs:1931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1931) prepare_beacon_proposer runs after every head change

**Skeptic check.** The earlier claim of an 'equivalent early exit' is right only for nodes with no registered proposers. For nodes running validators, the proposer-locality check comes after the head and fork choice work, the same ordering prysm#13465 fixed, but without the block copy.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [prysm#13465](https://github.com/OffchainLabs/prysm/pull/13465)

</details>


<a id="block_import-041"></a>
<details>
<summary><b>block_import-041</b> Coalesce head and reorg events during sync — <i>implemented · low · S · cpu</i></summary>

**Idea.** Suppress per-block head update and reorg events while syncing and publish one coalesced event at the end, so subscribers do not do redundant work per block.

**Impact.** Per-block head events and fork-choice get_head are already skipped for sync blocks; head/reorg events fire once per segment.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:185`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L185) EARLY_ATTESTER_CACHE_HISTORIC_SLOTS = 4
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4554`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4554) get_head and Head SSE only for blocks within 4 slots of current slot
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:633-661`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L633-L661) process_blocks calls recompute_head_at_current_slot once per chain segment
- [`beacon_node/beacon_chain/src/canonical_head.rs:1088-1100`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1088-L1100) recompute returns early (no after_new_head events) when view unchanged

**Skeptic check.** Verified the recent-slot gate in import_block and that range sync recomputes head once per segment, not per block. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#3022](https://github.com/Consensys-Incorporated/teku/pull/3022)

</details>


<a id="block_import-042"></a>
<details>
<summary><b>block_import-042</b> Compute block root once and pass it through pipeline — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Compute the block's hash_tree_root (or a tree-backed form with cached roots) once on receipt and pass it through gossip verification, signature verification, import, sync, observed-proposer and API paths instead of rehashing the block at each stage.

**Impact.** Already done. Every remaining non-test canonical_root call on a block in beacon_chain, network and http_api is at a single entry point.

**Best measured result.** block root ~10ms; ~30ms of duplicates against 300-400ms seen-to-imported (pr:lighthouse#3590)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1965`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1965)
- [`beacon_node/beacon_chain/src/block_verification_types.rs:27`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification_types.rs#L27)
- [`beacon_node/network/src/sync/network_context/requests/blocks_by_root.rs:39`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/requests/blocks_by_root.rs#L39)
- [`beacon_node/network/src/sync/block_sidecar_coupling.rs:140`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_sidecar_coupling.rs#L140)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3094`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3094)
- [`beacon_node/http_api/src/publish_blocks.rs:167`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L167)

**Skeptic check.** I searched every canonical_root and tree_hash_root call on blocks. The other hits are in tests or at genesis and builder setup, and the gossip, RPC, range-sync and publish paths carry block_root along with the block. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#14609](https://github.com/OffchainLabs/prysm/pull/14609), [lodestar@eb2b0deb5](https://github.com/ChainSafe/lodestar/commit/eb2b0deb5f5c), [lighthouse#3590](https://github.com/sigp/lighthouse/pull/3590), [lodestar#9795](https://github.com/ChainSafe/lodestar/pull/9795), [prysm#5785](https://github.com/OffchainLabs/prysm/pull/5785), [nimbus#3048](https://github.com/status-im/nimbus-eth2/pull/3048), [ethlambda#172](https://github.com/lambdaclass/ethlambda/pull/172)

</details>


<a id="block_import-043"></a>
<details>
<summary><b>block_import-043</b> Dedupe validation tasks per block; offload mutator work — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Remove a pending block from the delayed queue once its validation is spawned, so each newly arrived data column does not spawn another validation of the same block, and build data columns and proofs on workers instead of in the single-threaded fork choice loop.

**Impact.** Arriving columns never re-trigger block validation; column and proof building run on blocking worker threads, not under the fork choice lock.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:483`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L483) put_kzg_verified_data_columns adds to one pending entry per block root
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:524`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L524) check_availability_and_cache_components imports once when complete
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:592-634`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L592-L634) check_and_set_reconstruction_started dedupes reconstruction
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:671`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L671) column building from EL blobs on spawn_blocking_handle

**Skeptic check.** The grandine bug is specific to its Mutator delayed queue; Lighthouse verifies the block once and caches it in the DA checker keyed by root. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine#474](https://github.com/grandinetech/grandine/pull/474)

</details>


<a id="block_import-044"></a>
<details>
<summary><b>block_import-044</b> Insert finalized deposits into cache in background — <i>n/a · low · S · latency</i></summary>

**Idea.** Move insertion of finalized deposits into the deposit cache to a background task instead of the block processing path.

**Gap in Lighthouse.** Lighthouse no longer keeps an eth1 deposit cache, so there is no finalized-deposit insertion on the block path.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- grep for DepositCache/deposit_cache across beacon_node and consensus finds only a metric in [`consensus/state_processing/src/metrics.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/metrics.rs)
- beacon_node/ has no eth1 deposit service (client, genesis, execution_layer only)

**Sources.** [prysm#8405](https://github.com/OffchainLabs/prysm/pull/8405)

</details>


<a id="block_import-045"></a>
<details>
<summary><b>block_import-045</b> Run state defragmentation after block import — <i>n/a · medium · latency</i></summary>

**Idea.** Run the state tree defragmentation/compaction walk in a background task after block import completes, not synchronously before taking the fork choice write lock.

**Impact.** Lighthouse states are milhouse persistent trees with no Prysm-style multi-value-slice fragmentation and no defragmentation walk in block import, so there is nothing to move off the hot path.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5881`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5881) apply_pending_mutations before state root (milhouse persistent tree)
- [`consensus/types/src/state/beacon_state.rs:3416`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3416) rebase_on (structural sharing, not a defrag walk)
- [`beacon_node/beacon_chain/src/block_verification.rs:1731`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1731) update_tree_hash_cache

**Sources.** [prysm#16920](https://github.com/OffchainLabs/prysm/pull/16920)

</details>


<a id="block_import-046"></a>
<details>
<summary><b>block_import-046</b> Delay attestation production while head block imports — <i>partial · medium · M · latency</i></summary>

**Idea.** When a block that will become head is being imported, make attestation production wait (bounded, e.g. 1.5s) on a condvar until it is imported, so attestations vote for it instead of its parent.

**Gap in Lighthouse.** produce_unaggregated_attestation never waits. The early attester cache gets the block only after the state transition, the EL newPayload and fork choice (beacon_chain.rs:4572), so it covers only the DB-write window. A current-slot block that passed gossip verification but is still in state transition, notify_new_payload or data availability when the VC asks at 1/3 slot gets an attestation for its parent. Nothing in produce_unaggregated_attestation or the http_api attestation_data handler does a bounded wait on an in-flight import of a request_slot block.

**Impact.** Fewer wrong head votes for late blocks that arrive near the attestation deadline. Only blocks that arrive in the ~100-500ms before 1/3 slot are affected.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2010-2039`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2010-L2039)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4572`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4572)
- [`beacon_node/beacon_chain/src/block_verification.rs:1561-1571`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1561-L1571),1720-1745
- [`beacon_node/http_api/src/validator/mod.rs:295`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L295)

**Skeptic check.** The early attester cache only removes the gap between fork choice and the DB write, which was the motivation of #2575. It does not give the condvar wait over the whole import, so the earlier claim of the same effect without a wait was wrong for the state-transition and payload-verification window.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lighthouse#2575](https://github.com/sigp/lighthouse/pull/2575)

</details>


<a id="block_import-047"></a>
<details>
<summary><b>block_import-047</b> Apply EL payload status after block accepted in fork choice — <i>n/a · low · S · latency, cpu</i></summary>

**Idea.** Delay applying the execution engine's newPayload status until the beacon block has been validated and inserted into fork choice, so payload status handling does not interleave with block processing.

**Gap in Lighthouse.** n/a

**Impact.** None; no equivalent interleaving problem.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1555`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1555) notify_new_payload awaited during verification
- Lighthouse starts newPayload as a future in parallel with state transition and passes the status into fork choice on_block; Grandine's change is about its actor message ordering.

**Sources.** [grandine@bc4e630f5](https://github.com/grandinetech/grandine/commit/bc4e630f55d1)

</details>


<a id="block_import-048"></a>
<details>
<summary><b>block_import-048</b> Direct field equality instead of reflection for Eth1Data — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Compare Eth1Data (and similar small containers on the vote counting path) with direct field comparison instead of generic reflection/proto equality, removing allocations.

**Impact.** Equality is already a derived field-wise compare with no allocation.

**Best measured result.** 4937 -&gt; 46.4 ns/op, 21 -&gt; 0 allocs (pr:prysm#4712)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/execution/eth1_data.rs:12-21`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/execution/eth1_data.rs#L12-L21) derive PartialEq/Eq on plain fields
- [`consensus/state_processing/src/per_block_processing.rs:371-380`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing.rs#L371-L380) vote counting compares Eth1Data values directly

**Skeptic check.** Rust derive(PartialEq) is a direct field compare; reflection-based equality does not exist here. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#4712](https://github.com/OffchainLabs/prysm/pull/4712)

</details>


<a id="block_import-049"></a>
<details>
<summary><b>block_import-049</b> Drop envelope execution-parent DB existence check — <i>n/a · low · cpu, disk</i></summary>

**Idea.** Remove the DB lookup that checks the execution-parent envelope exists when importing a head payload, since the check is redundant.

**Impact.** Nothing to remove.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/payload_envelope_verification`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification)/ (grep parent_envelope/execution_parent: no hits)
- No execution-parent envelope DB existence check found in LH envelope import path.

**Sources.** [nimbus#9029](https://github.com/status-im/nimbus-eth2/pull/9029)

</details>


<a id="block_import-050"></a>
<details>
<summary><b>block_import-050</b> Reject future-slot blocks early instead of queueing — <i>implemented · medium · S · memory, disk, bandwidth</i></summary>

**Idea.** Drop blocks whose slot is beyond the clock-disparity bound before parent lookup, instead of queueing them or storing them as pending, so fabricated future blocks cost no memory, disk writes or parent fetches.

**Impact.** Already done. Future-slot blocks are rejected before the parent check (so no ParentUnknown lookup), before state loads and before block_times_cache writes. This holds on the gossip, RPC and range-segment paths.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:916-926`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L916-L926),1404,1448,1926-1931
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3942-3950`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3942-L3950),3125
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1846`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1846)
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1716`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1716)

**Skeptic check.** The gossip FutureSlot check comes before verify_parent_block_and_envelope_are_known, and the RPC paths call check_block_relevancy first in into_execution_pending_block_slashable. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#3210](https://github.com/ChainSafe/lodestar/pull/3210), [ethlambda#324](https://github.com/lambdaclass/ethlambda/pull/324)

</details>


<a id="block_import-051"></a>
<details>
<summary><b>block_import-051</b> Remove obsolete optimistic import candidate check — <i>n/a · low · latency, sync</i></summary>

**Idea.** Remove the merge-era safe-slots-to-import optimistic candidate check so blocks are imported optimistically without the extra check and delay.

**Impact.** Nothing to remove.

**Evidence (Lighthouse @ 928b61e719).**

- repo-wide grep optimistic_candidate/safe_slots: no hits
- No optimistic import candidate / safe-slots check exists in LH source (grep empty).

**Sources.** [nimbus#4129](https://github.com/status-im/nimbus-eth2/pull/4129)

</details>


<a id="block_import-052"></a>
<details>
<summary><b>block_import-052</b> Do not recompute an already known state root — <i>implemented · low · S · cpu</i></summary>

**Idea.** Avoid a redundant hash_tree_root of the BeaconState in block import/production by reusing a state root that is already known, and do not compute and compare the post-state root a second time once the state transition validated it.

**Impact.** One state root per import. The parent block's state root is reused for the first slot advance, and the milhouse tree hash cache makes repeats incremental. A locally produced block is still re-executed and rehashed at import, but that is a separate idea.

**Best measured result.** 16 to 12 state roots per run; 0.05s each (pr:nimbus#933)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1610-1640`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1610-L1640),1731-1745,1039-1046
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4752`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4752)

**Skeptic check.** Confirmed one update_tree_hash_cache plus a compare against block.state_root(). Import then stores the state under that root with no second hash, and per_slot_processing gets the known root. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#933](https://github.com/status-im/nimbus-eth2/pull/933), [prysm#3114](https://github.com/OffchainLabs/prysm/pull/3114)

</details>


<a id="block_import-053"></a>
<details>
<summary><b>block_import-053</b> Reject known, finalized or non-descendant blocks before state load — <i>implemented · medium · S · cpu, memory, disk, latency, sync</i></summary>

**Idea.** Before loading the parent block and state, or running state transition in segment/queue import, reject blocks that are already known, at or below the finalized slot, or not descended from finality. Stale blocks then cost no DB reads, state loads or full validation.

**Impact.** Already done. Known blocks and blocks at or below the finalized slot are dropped before the parent and state load. A non-descendant on the RPC path fails is_parent_imported, because fork choice get_block filters non-descendants, and so returns before any DB read.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:958-986`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L958-L986),1404,1448,1825-1850,1857-1900,1942-1955,2022-2031
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3068-3140`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3068-L3140)
- [`consensus/fork_choice/src/fork_choice.rs:1600-1612`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1600-L1612),1652

**Skeptic check.** Confirmed check_block_relevancy is first on the RPC and segment paths, and gossip also runs check_block_is_finalized_checkpoint_or_descendant before loading the parent. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#679](https://github.com/OffchainLabs/prysm/pull/679), [lighthouse#2289](https://github.com/sigp/lighthouse/pull/2289), [prysm#13089](https://github.com/OffchainLabs/prysm/pull/13089), [lighthouse#2474](https://github.com/sigp/lighthouse/pull/2474), [lighthouse#1041](https://github.com/sigp/lighthouse/pull/1041), [lodestar@81bbf5b96](https://github.com/ChainSafe/lodestar/commit/81bbf5b96fd2), [teku#1076](https://github.com/Consensys-Incorporated/teku/pull/1076)

</details>


<a id="block_import-054"></a>
<details>
<summary><b>block_import-054</b> Load block collector without temporary in-memory DB — <i>n/a · low · memory, disk</i></summary>

**Idea.** Load sync blocks straight from the ETL collector into the block collector without an intermediate temporary in-memory DB copy.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync) (no ETL collector)
- Caplin ETL collector specific; LH has no such temporary DB copy.

**Sources.** [caplin#11215](https://github.com/erigontech/erigon/pull/11215)

</details>


<a id="block_import-055"></a>
<details>
<summary><b>block_import-055</b> Call slot tick handler directly, skipping missed ticks — <i>n/a · low · latency, cpu</i></summary>

**Idea.** Drive the per-slot tick handler directly from a single-threaded scheduler that skips missed ticks instead of queueing tick events, so a slow consumer cannot make the node's clock fall behind.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/timer/src/lib.rs:18-25`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/timer/src/lib.rs#L18-L25) sleep(duration_to_next_slot) loop
- LH timer sleeps until the next slot boundary each loop (recomputed from the clock), so missed ticks are skipped and no queue exists.

**Sources.** [teku#5171](https://github.com/Consensys-Incorporated/teku/pull/5171)

</details>


<a id="block_import-056"></a>
<details>
<summary><b>block_import-056</b> Deduplicate in-flight block imports across gossip and RPC — <i>implemented · medium · S · cpu, disk, memory</i></summary>

**Idea.** Track block roots that are being processed or were recently imported, shared by gossip, RPC and pending-block retry paths, and make a second arrival skip, wait for or share the in-flight result instead of processing it again.

**Impact.** Gossip and lookup share one in-flight root set. A lookup block that finds the root in flight goes to the reprocess queue, and a gossip block that finds it in flight is dropped. Only the Gloas payload envelope path lacks this (a TODO at gossip_methods.rs:3807), and Gloas is not live.

**Best measured result.** spin loop ~25 iterations/ms until 8GB OOM before fix (pr:lodestar#9501)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:166-200`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L166-L200)
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1561`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1561)
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:121-150`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L121-L150)
- [`beacon_node/network/src/network_beacon_processor/mod.rs:71`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L71)
- [`beacon_node/beacon_chain/src/block_verification.rs:1085-1097`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1085-L1097)
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:3807`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L3807)

**Skeptic check.** Verified DuplicateCache RAII handle on gossip (process_gossip_block) and lookup (process_lookup_block, which requeues via ReprocessQueueMessage::RpcBlock). Earlier evidence was correct. The one hole is the Gloas envelope TODO, which is pre-fork.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#2647](https://github.com/sigp/lighthouse/pull/2647), [prysm#12905](https://github.com/OffchainLabs/prysm/pull/12905), [lighthouse#4179](https://github.com/sigp/lighthouse/pull/4179), [lodestar#9501](https://github.com/ChainSafe/lodestar/pull/9501)

</details>


<a id="block_import-057"></a>
<details>
<summary><b>block_import-057</b> Size processor queues from active validator count — <i>implemented · medium · S · memory</i></summary>

**Idea.** Size beacon processor work queues (especially attestation queues) from the active validator count at startup, so they do not overflow and drop work on large networks.

**Impact.** Already done.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_queue.rs:11`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_queue.rs#L11)
- [`beacon_node/beacon_processor/src/scheduler/work_queue.rs:336-370`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_queue.rs#L336-L370)
- [`beacon_node/client/src/builder.rs:757`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L757)

**Skeptic check.** from_state sizes attestation_queue and unknown_block_attestation_queue as 110% of active validators / slots_per_epoch, and the client builder calls it at startup. The other queues are fixed, and they are large enough (aggregates 4096). Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#5573](https://github.com/sigp/lighthouse/pull/5573)

</details>


<a id="block_import-058"></a>
<details>
<summary><b>block_import-058</b> Produce light client updates eagerly after import — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** After each imported block, compute light client updates on a separate thread from the in-memory state and cache the proofs, so each update is computed once and serving queries needs no block replay.

**Impact.** Each update is computed once per block, off the import thread, from proofs cached from the in-memory post-state.

**Best measured result.** each update computed at most once (pr:lighthouse#4969)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:4787-4790`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4787-L4790)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5178-5190`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5178-L5190)
- [`beacon_node/beacon_chain/src/light_client_server_cache.rs:59-75`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_server_cache.rs#L59-L75)
- [`beacon_node/beacon_chain/src/light_client_server_cache.rs:80`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_server_cache.rs#L80)

**Skeptic check.** cache_state_data stores the proofs in prev_block_cache during import. recompute_and_cache_updates runs on the producer task that light_client_server_tx feeds. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#4969](https://github.com/sigp/lighthouse/pull/4969)

</details>


<a id="block_import-059"></a>
<details>
<summary><b>block_import-059</b> Emit head/block events right after head update — <i>partial · medium · S · latency</i></summary>

**Idea.** Emit the block/head and payload-attributes events right after the head update, before slower follow-up work, and do not emit them twice, so validators and builders see the new head sooner.

**Gap in Lighthouse.** Block SSE still waits for the DB write; PayloadAttributes SSE after a new head waits for a no-attributes forkchoiceUpdated round trip to the EL. Move the Block event next to the early Head event, and compute/emit payload attributes before (or concurrently with) the first FCU in spawn_execution_layer_updates.

**Impact.** Builders/relays get the block event tens of ms earlier and payload_attributes tens to hundreds of ms earlier after a head change; Head is already early.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:4618`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4618) Head SSE registered inside import_block right after fork choice head decision, before the DB write
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4680`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4680) HeadV2 SSE emitted at the same early point
- [`beacon_node/beacon_chain/src/canonical_head.rs:1222-1262`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1222-L1262) second HeadV2 only when payload status changes for the same root (no duplicate); no Head event in recompute_head
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4756-4769`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4756-L4769) do_atomically_with_block_and_blobs_cache DB write, then fork choice lock drop
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5165`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5165) Block SSE in import_block_update_metrics_and_events, after the DB commit
- [`beacon_node/beacon_chain/src/canonical_head.rs:1908-1931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1908-L1931) spawn_execution_layer_updates awaits update_execution_engine_forkchoice before prepare_beacon_proposer
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7092`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7092) PayloadAttributes SSE emitted only inside prepare_beacon_proposer

**Second check.** Checked all prepare_beacon_proposer callers (state_advance_timer, proposer_prep_service, http_api, canonical_head) and every EventKind emission in canonical_head.rs: no earlier PayloadAttributes or Block emission exists; Head/HeadV2 are early and not duplicated, matching the earlier partial verdict.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [prysm#8422](https://github.com/OffchainLabs/prysm/pull/8422), [caplin#17122](https://github.com/erigontech/erigon/pull/17122)

</details>


<a id="block_import-060"></a>
<details>
<summary><b>block_import-060</b> Send fcU from in-memory head before block persisted — <i>not · high · L · latency</i></summary>

**Idea.** During block import, recompute the head with the in-memory block and state and send forkchoiceUpdated to the EL before the block is fully persisted, so the EL starts payload building earlier.

**Gap in Lighthouse.** Recompute the head and send fcU from import_block, with the in-memory block and state, before the store write; the head recompute and after_new_head assume block and state are in the store.

**Impact.** fcU and payload building start about the DB write plus cache updates earlier (tens of ms) after each block; PR 7752 was closed unmerged as a prototype.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:4752-4765`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4752-L4765) store.do_atomically_with_block_and_blobs_cache runs inside import_block before any head recompute
- [`beacon_node/beacon_chain/src/canonical_head.rs:1909`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1909) the only head-driven fcU is spawned from recompute_head_at_slot_internal/after_new_head
- [`beacon_node/network/src/network_beacon_processor/mod.rs:1036`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L1036) recompute_head_at_current_slot is called only after process_block returns (import finished)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7135`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7135) the other fcU is proposer-prep, which reuses the current head and is not triggered by a new block

**Second check.** Checked every update_execution_engine_forkchoice call site (canonical_head.rs:1909, proposer prep at beacon_chain.rs:7135) and the network callers of recompute_head; none run before the DB write.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [lighthouse#7752](https://github.com/sigp/lighthouse/pull/7752)

</details>


<a id="block_import-061"></a>
<details>
<summary><b>block_import-061</b> Update head immediately after block state transition — <i>partial · medium · M · latency, cpu</i></summary>

**Idea.** Recompute and set the head right after the block's state transition/import succeeds, before post-processing steps (attestation handling, caches, pruning), so head and downstream consumers see the block sooner and head-lock contention drops.

**Gap in Lighthouse.** Attestation and head SSE already see the new head right after the state transition (early attester cache + get_head inside import_block). The canonical cached_head is still set only by recompute_head_at_slot after import_block returns, so after shuffling/observe/validator-monitor/slasher work, the DB write, light-client caching and metrics. Moving the cached_head update earlier would need care because a DB write failure reverts fork choice (handle_import_block_db_write_error).

**Impact.** Small: consumers of cached_head (HTTP head, proposer prep, forkchoiceUpdated to the EL) see the block some tens of ms earlier; attesting already uses the early attester cache.

**Best measured result.** Said to have a big impact on block processing time; no numbers (pr:prysm#9224)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:4545-4700`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4545-L4700) get_head right after fork_choice.on_block; new head goes into early_attester_cache and head/head_v2 SSE events before any post-processing
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4714-4733`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4714-L4733) shuffling cache, observe attestations, validator monitor, slasher run after the early head computation
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4752-4772`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4752-L4772) DB write, then fork choice write lock dropped
- [`beacon_node/beacon_chain/src/canonical_head.rs:781`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L781) recompute_head_at_slot (sets cached_head) is only called by callers after import returns, e.g. gossip_methods.rs:1008, publish_blocks.rs:610, sync_methods.rs:207

**Second check.** Re-read import_block end to end, the post-DB-write tail, and every recompute_head_at_* caller in beacon_chain, network and http_api; no caller sets cached_head inside import_block or before the DB write, so the earlier partial verdict stands.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [prysm#8412](https://github.com/OffchainLabs/prysm/pull/8412), [prysm#9224](https://github.com/OffchainLabs/prysm/pull/9224)

</details>


<a id="block_import-062"></a>
<details>
<summary><b>block_import-062</b> Verify proposer signature before state transition and DA — <i>implemented · medium · S · cpu</i></summary>

**Idea.** Verify the block proposer signature before the full state transition and before starting data availability checks, so blocks with bad signatures are rejected cheaply and the fault is attributed to that block copy.

**Impact.** None needed.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1055-1073`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1055-L1073)
- [`beacon_node/beacon_chain/src/block_verification.rs:1075-1097`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1075-L1097)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3969-3993`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3969-L3993)

**Skeptic check.** GossipVerifiedBlock::new verifies the proposer signature before observe_proposal and before the state transition. process_block calls put_pre_execution_block (or the Gloas insert_block) only after into_execution_pending_block succeeds. Earlier evidence was correct, but one cited path said block_verification.rs:3980 when the code is in beacon_chain.rs.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#11401](https://github.com/Consensys-Incorporated/teku/pull/11401), [nimbus#955](https://github.com/status-im/nimbus-eth2/pull/955)

</details>


<a id="block_import-063"></a>
<details>
<summary><b>block_import-063</b> Epoch-boundary metrics off block import path — <i>not · low · S · latency, cpu</i></summary>

**Idea.** Run epoch-boundary metrics reporting that iterates the whole validator set asynchronously after import, so the epoch-boundary block is imported and visible to attesters sooner.

**Gap in Lighthouse.** Epoch-boundary validator monitor work (process_valid_state, summary/status processing in validator_monitor.rs) runs inline during block import. Would need to spawn it on a blocking task after import. Cost is small unless many validators are monitored; the O(n) registry scan is already replaced by iter_from.

**Impact.** Shaves a few ms to tens of ms from epoch-boundary block import only when validator monitor is in use; negligible for default nodes.

**Best measured result.** blocks imported &gt;4s into slot at epoch transitions: 3 of 37 epochs (8%) after fix (pr:prysm#16731)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_monitor.rs:490`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_monitor.rs#L490) process_valid_state runs within import path
- [`beacon_node/beacon_chain/src/validator_monitor.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_monitor.rs) process_valid_state / process_validator_statuses

**Sources.** [prysm#16731](https://github.com/OffchainLabs/prysm/pull/16731)

</details>


<a id="block_import-064"></a>
<details>
<summary><b>block_import-064</b> Running Eth1Data vote count cache — <i>not · low · M · cpu</i></summary>

**Idea.** Keep a running vote count per Eth1Data value in a cache instead of scanning the whole eth1_data_votes list on every block.

**Gap in Lighthouse.** Add a vote-count cache on the state or a transient cache in per-block processing keyed by Eth1Data.

**Impact.** Saves microseconds per block; negligible against block processing.

**Best measured result.** ProcessBlock 20s -&gt; 2.3s over 10000 iterations at 65536 validators (pr:prysm#2754)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing.rs:371-390`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing.rs#L371-L390) get_new_eth1_data filter().count()
- LH still counts votes by scanning eth1_data_votes (up to 2048 entries) once per block; no running count cache. Cost is ~2k 72-byte compares per block, microseconds.

**Sources.** [prysm#2754](https://github.com/OffchainLabs/prysm/pull/2754)

</details>


<a id="block_import-065"></a>
<details>
<summary><b>block_import-065</b> Event-driven head publication on block index commit — <i>n/a · low · latency</i></summary>

**Idea.** Wake head publication on block-index commit events (with a short fallback timer) instead of waiting for the next slot, and share storage backoff across queued persistence jobs so a failing DB is not retried by every job.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:7471`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7471) per_slot_task
- Caplin block-index commit mechanism; LH head update is synchronous in import_block and store writes are not retried per queued job.

**Sources.** [caplin#25533](https://github.com/erigontech/erigon/pull/25533)

</details>


<a id="block_import-066"></a>
<details>
<summary><b>block_import-066</b> Emit block events without waiting for EL validity — <i>not · low · S · latency</i></summary>

**Idea.** Emit block-imported SSE events and update the head without waiting for the execution client's payload status, so subscribers are not delayed by the EL round trip.

**Gap in Lighthouse.** Move Block event registration ahead of awaiting payload_verification_handle in process_block, with execution_optimistic=true.

**Impact.** Subscribers see blocks one EL newPayload round trip (tens to hundreds of ms) earlier; only matters for SSE consumers, no node-internal gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5111`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5111) Block SSE emitted in import_block_update_metrics_and_events, after import
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4102`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4102) payload_verification_handle awaited before import

**Sources.** [grandine@46732b6ed](https://github.com/grandinetech/grandine/commit/46732b6ed890), [grandine#824](https://github.com/grandinetech/grandine/pull/824), [prysm#16894](https://github.com/OffchainLabs/prysm/pull/16894)

</details>


<a id="block_import-067"></a>
<details>
<summary><b>block_import-067</b> Evict received-set entries when delayed queue full — <i>implemented · low · S · memory</i></summary>

**Idea.** When a delayed queue is full and an item is rejected or evicted, also remove its entry from the received/seen collections so it does not leak and can be retried.

**Impact.** Queue-internal seen sets cannot leak on a full queue; dropped items are retryable via lookup sync.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:664-682`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L664-L682) queued_gossip_block_roots inserted only after capacity check
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:867-876`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L867-L876) column queue full drops before any map insert
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:1172`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L1172) root removed on dequeue
- [`beacon_node/beacon_chain/src/block_verification.rs:1486-1496`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1486-L1496) RPC/import path re-observes and does not reject on observed_block_producers, so a dropped early block can be recovered by lookup

**Skeptic check.** Checked every capacity-check branch in the reprocess queue and the gossip early-block path. A dropped early gossip block stays in observed_block_producers, but gossipsub dedupes the same message anyway and the RPC path does not consult that cache, so retry still works.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine@22f4e8972](https://github.com/grandinetech/grandine/commit/22f4e8972c61)

</details>


<a id="block_import-068"></a>
<details>
<summary><b>block_import-068</b> Evict cached inputs of unimported repeat proposals — <i>implemented · low · S · memory</i></summary>

**Idea.** Remove the block input and payload envelope cache entries of repeat proposals that are not imported, with single-entry removal, so an equivocating proposer cannot make the node keep unlimited full blocks until finalization.

**Impact.** Memory is already bounded: both the pre-Gloas and the Gloas availability caches are 32-entry LRUs, and a gossip equivocation fails with Slashable before it is cached.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1085-1097`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1085-L1097)
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:53`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L53)
- [`beacon_node/beacon_chain/src/pending_payload_cache/mod.rs:55`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/mod.rs#L55)
- [`beacon_node/beacon_chain/src/pending_payload_cache/mod.rs:103-118`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/mod.rs#L103-L118)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3973-3983`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3973-L3983)

**Skeptic check.** Lighthouse does not do single-entry eviction of repeat proposals. It gets the same effect, bounded retention, from the 32-entry LRU caps on DataAvailabilityChecker and PendingPayloadCache, plus remove_block on verification failure. The earlier 'implemented' holds as an effect, not as the same mechanism.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#10083](https://github.com/ChainSafe/lodestar/pull/10083)

</details>


<a id="block_import-069"></a>
<details>
<summary><b>block_import-069</b> Start block and payload verification before data availability completes — <i>implemented · high · S · latency, cpu</i></summary>

**Idea.** Start state transition, signature checks and EL newPayload as soon as the block arrives, in parallel with waiting for blobs/columns, and only await data availability before final import.

**Impact.** Already done: newPayload is spawned in parallel with the state transition, and the import waits for columns only after execution.

**Best measured result.** column wait can take 2+ s of the 4 s window (pr:nimbus#8561)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1541-1570`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1541-L1570)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3969-4022`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3969-L4022)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4096`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4096)

**Skeptic check.** The gossip and lookup paths run into_execution_pending_block (newPayload is spawned through spawn_handle) and into_executed_block before the DA checker decides availability. Columns are verified on their own as they arrive. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#12924](https://github.com/erigontech/erigon/pull/12924), [nimbus#8561](https://github.com/status-im/nimbus-eth2/pull/8561), [silver#230](https://github.com/gattaca-com/silver/pull/230), [lodestar#6087](https://github.com/ChainSafe/lodestar/pull/6087)

</details>


<a id="block_import-070"></a>
<details>
<summary><b>block_import-070</b> Faster justification and finalization checkpoint updates — <i>implemented · low · S · latency, cpu</i></summary>

**Idea.** Speed up the justification and finalization processing done when updating checkpoints during block import (avoid recomputation over the full state).

**Impact.** None needed: unrealized justification and finalization at import is O(1) from progressive_balances_cache, and it is skipped when the parent's checkpoints already apply.

**Best measured result.** Mainnet block import ~30-40 ms faster (pr:grandine#584)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/altair/justification_and_finalization.rs:9-30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/altair/justification_and_finalization.rs#L9-L30)
- [`consensus/fork_choice/src/fork_choice.rs:932-971`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L932-L971)

**Skeptic check.** Verified that the altair process_justification_and_finalization reads only the cached target balances, with no validator loop, and that on_block reuses the parent's unrealized checkpoints when there are no slashings. The Grandine PR diff was not available. Lighthouse's path has no per-validator cost left to remove.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine#584](https://github.com/grandinetech/grandine/pull/584)

</details>


<a id="block_import-071"></a>
<details>
<summary><b>block_import-071</b> Fast RwLocks and rayon parallelism in block processing — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Use low-overhead (parking_lot-style) RwLocks and rayon data parallelism for independent work in block and attestation processing.

**Impact.** Already in place; the idea is a Lighthouse commit.

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.toml:207 parking_lot
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4498`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4498) parking_lot RwLockUpgradableReadGuard on pubkey cache
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4510`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4510) fork_choice_upgradable_read_lock

**Skeptic check.** The source is Lighthouse's own commit; parking_lot locks and rayon are used throughout. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@20e45b336](https://github.com/sigp/lighthouse/commit/20e45b3369f7)

</details>


<a id="block_import-072"></a>
<details>
<summary><b>block_import-072</b> Finalized-descendant check via fork choice membership — <i>implemented · low · S · cpu, disk, latency</i></summary>

**Idea.** Check that a block descends from the finalized checkpoint by looking up its parent in the in-memory fork choice (which only holds finalized-compatible nodes) instead of loading blocks from the DB or walking ancestry.

**Impact.** None needed.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1857-1900`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1857-L1900)
- [`consensus/fork_choice/src/fork_choice.rs:1829`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1829)
- [`consensus/proto_array/src/proto_array.rs:2251-2311`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L2251-L2311)
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1725`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1725)

**Skeptic check.** The proto_array check first compares the node's checkpoints (fast path), then walks the in-memory parent links back to the finalized slot. The DB is read only through block_exists, on the failure path, to choose the error. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#12040](https://github.com/OffchainLabs/prysm/pull/12040), [prysm#10905](https://github.com/OffchainLabs/prysm/pull/10905), [prysm#12041](https://github.com/OffchainLabs/prysm/pull/12041), [prysm#12046](https://github.com/OffchainLabs/prysm/pull/12046)

</details>


<a id="block_import-073"></a>
<details>
<summary><b>block_import-073</b> Check block existence in fork choice before DB — <i>implemented · medium · S · cpu, disk, latency</i></summary>

**Idea.** For duplicate and parent-known checks during import, query the in-memory fork choice store first and only fall back to the DB, making the common check synchronous and far cheaper.

**Impact.** None needed; duplicate and parent-known checks are in-memory fork choice lookups on gossip, RPC and range sync paths.

**Best measured result.** HasBlock DB 381 ns/op vs fork choice 40.0 ns/op (pr:prysm#4821)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:970-973`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L970-L973) gossip GossipVerifiedBlock::new_without_slasher_checks checks fork_choice contains_block before loading parent
- [`beacon_node/beacon_chain/src/block_verification.rs:1948-1954`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1948-L1954) check_block_relevancy uses fork choice contains_block
- [`beacon_node/beacon_chain/src/block_verification.rs:2023-2026`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L2023-L2026) load_parent uses fork_choice is_parent_imported before any DB read
- [`beacon_node/beacon_chain/src/block_verification.rs:1891-1894`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1891-L1894) store.block_exists only on the NotFinalizedDescendant error path
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4512`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4512) import re-check in fork choice

**Skeptic check.** Verified all duplicate/parent checks on import paths go to fork choice; the only store.block_exists calls are on an error branch and in the HTTP API root lookup, which must read the block anyway. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#4821](https://github.com/OffchainLabs/prysm/pull/4821), [lodestar@f6a6945d2](https://github.com/ChainSafe/lodestar/commit/f6a6945d2a15)

</details>


<a id="block_import-074"></a>
<details>
<summary><b>block_import-074</b> Import block once half of columns are available — <i>partial · high · M · latency</i></summary>

**Idea.** Treat a PeerDAS block as available, and import it, as soon as about 50% of data columns are accepted, since the rest can be reconstructed; complete the remaining columns in the background instead of waiting for all custody columns. This cuts import latency on supernodes.

**Gap in Lighthouse.** Reconstruction starts at 50%, but import waits for it to finish. To match, make_available would accept &gt;= 50% verified columns, import the block with the received set, and fill and persist the custody columns in the background.

**Impact.** On supernodes this removes the wait for KZG cell recovery (hundreds of ms) before import once half the columns arrive. No effect on non-supernodes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:212-232`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L212-L232) make_available requires verified_data_columns.len() == num_expected (all sampling columns)
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:617-624`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L617-L624) reconstruction is triggered at &gt;= half of all columns
- [`beacon_node/network/src/network_beacon_processor/mod.rs:1213`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L1213) attempt_data_column_reconstruction; the block becomes available only after reconstructed columns are put in the cache

**Second check.** Read make_available and check_and_set_reconstruction_started directly; there is no availability shortcut under another name. The only early step is that reconstruction is triggered at half.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [teku#10365](https://github.com/Consensys-Incorporated/teku/pull/10365), [grandine@39bab2591](https://github.com/grandinetech/grandine/commit/39bab2591f87)

</details>


<a id="block_import-075"></a>
<details>
<summary><b>block_import-075</b> Early return from save-head when head unchanged — <i>implemented · low · S · cpu, sync</i></summary>

**Idea.** In sync, return early from save-head when the new head root equals the cached head root, and share one post-state saving path between normal and sync import.

**Impact.** Head update work is skipped when the head is unchanged; sync and gossip share the import path.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:1088-1100`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1088-L1100) recompute_head_at_slot_internal returns Ok(None) when view, payload status and fcU params are unchanged
- [`beacon_node/beacon_chain/src/canonical_head.rs:1107-1110`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1107-L1110) cached head only replaced when head root changes
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:640`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L640) sync uses the same process_chain_segment/process_block import path

**Skeptic check.** Verified the early return in recompute_head. Lighthouse does not persist head per block, so there is no per-block save-head cost to skip. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#6562](https://github.com/OffchainLabs/prysm/pull/6562)

</details>


<a id="block_import-076"></a>
<details>
<summary><b>block_import-076</b> Use in-memory head state when parent is head — <i>partial · low · S · latency, disk</i></summary>

**Idea.** When fetching the pre-state for block or attestation processing, check whether the parent/target root is the current head and use the in-memory head state. This skips a DB read and state deserialization on the common path.

**Gap in Lighthouse.** State part is done (state_cache for blocks, cached head state for attestations). But load_parent still does a DB read and SSZ decode of the parent SignedBlindedBeaconBlock on every block import, only to get slot/state_root (which fork choice ProtoBlock has) and to fill PreProcessingSnapshot.beacon_block. When parent == head, canonical_head.cached_head().snapshot.beacon_block is in memory; get_blinded_block also skips the store's block_cache.

**Impact.** Removes one hot-DB get plus blinded-block decode (including signature point decoding) per import; sub-millisecond to ~1 ms, so small.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:2045-2057`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L2045-L2057) load_parent reads the parent blinded block from the DB on every import via chain.get_blinded_block
- [`beacon_node/store/src/hot_cold_store.rs:663-686`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L663-L686) get_blinded_block goes straight to hot_db.get_bytes + SSZ decode, bypassing block_cache
- [`beacon_node/store/src/hot_cold_store.rs:1130`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1130) get_advanced_hot_state serves the state from state_cache first
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:400-404`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L400-L404) attestation committee path uses cached_head beacon_state when root is head

**Skeptic check.** Earlier evidence was right that the pre-state comes from the in-memory state cache with no DB read or deserialization. It missed that the same load_parent path still reads the parent block from the DB, so the idea's 'skip a DB read' effect is only partly achieved.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [prysm#4830](https://github.com/OffchainLabs/prysm/pull/4830), [prysm#4853](https://github.com/OffchainLabs/prysm/pull/4853), [prysm#4972](https://github.com/OffchainLabs/prysm/pull/4972), [prysm#4974](https://github.com/OffchainLabs/prysm/pull/4974)

</details>


<a id="block_import-077"></a>
<details>
<summary><b>block_import-077</b> Update head once per slot while far behind — <i>implemented · medium · S · cpu, sync</i></summary>

**Idea.** During sync, when the node is more than a few epochs behind, do not run the fork choice head update after every imported block; update the head once per slot instead. This removes repeated head computation per block.

**Impact.** None needed; range sync recomputes head once per batch, not per block, and old blocks skip get_head.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:4554-4556`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4554-L4556) get_head during import only when block is within EARLY_ATTESTER_CACHE_HISTORIC_SLOTS of current slot
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:638-660`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L638-L660) process_blocks calls recompute_head_at_current_slot once per chain segment
- [`beacon_node/beacon_chain/src/beacon_chain.rs:186-194`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L186-L194) MAX_PER_SLOT_FORK_CHOICE_DISTANCE skips per-slot fork choice when far behind

**Skeptic check.** Verified range sync imports a whole segment through process_chain_segment and recomputes the head once afterwards; per-block get_head is gated on recency. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#2780](https://github.com/Consensys-Incorporated/teku/pull/2780)

</details>


<a id="block_import-078"></a>
<details>
<summary><b>block_import-078</b> Compute total active balance once per block — <i>implemented · low · S · cpu</i></summary>

**Idea.** In per-block attestation participation processing, compute the total active balance once per block and pass it to each attestation instead of recomputing it per attestation.

**Impact.** Total active balance and base rewards are computed once per epoch, not per attestation.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/process_operations.rs:258-290`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L258-L290) altair process_attestation uses state.get_base_reward per validator
- [`consensus/types/src/state/beacon_state.rs:3136`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3136) get_base_reward reads epoch_cache
- consensus/types/src/epoch_cache.rs:130-145 base_rewards table precomputed per effective-balance increment

**Skeptic check.** Base reward is a table lookup in the epoch cache; no total-active-balance recomputation on the attestation path. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#9417](https://github.com/OffchainLabs/prysm/pull/9417)

</details>


<a id="block_import-079"></a>
<details>
<summary><b>block_import-079</b> Check sync block cache before DB lookups — <i>n/a · low · disk, latency</i></summary>

**Idea.** During range sync, look up blocks in the in-memory batch block cache before reading them from the database, through one shared getBlock helper. This avoids disk reads for blocks that are not yet persisted.

**Impact.** Range sync passes blocks by value to import; there is no DB lookup of batch blocks to avoid.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain.rs:120`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L120) batches hold downloaded blocks in memory and are passed directly to process_blocks
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:633`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L633)

**Sources.** [prysm#10568](https://github.com/OffchainLabs/prysm/pull/10568)

</details>


<a id="block_import-080"></a>
<details>
<summary><b>block_import-080</b> Wake slot wait early when block arrives — <i>n/a · low · latency</i></summary>

**Idea.** When the processing loop waits for the slot's block with a timeout, interrupt the wait as soon as the block arrives so processing starts immediately instead of sleeping until the timeout.

**Impact.** Lighthouse does not poll with a slot timeout; blocks are pushed through channels and delay queues.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:660-690`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L660-L690) and 805-830 event-driven queues

**Sources.** [teku#586](https://github.com/Consensys-Incorporated/teku/pull/586)

</details>


<a id="block_import-081"></a>
<details>
<summary><b>block_import-081</b> Iterate validator tree list from index, not skip — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** In per-block validator monitoring or any scan that starts at a validator index, use an iterator that seeks to the index (iter_from) on the persistent tree list instead of skip(n), which walks the whole prefix.

**Impact.** Already done (lighthouse#9995).

**Best measured result.** Median import_block 199.87 ms to 38.47 ms (second window 191.60 to 40.56) with 2.36M validators (pr:lighthouse#9995)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_monitor.rs:487-497`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_monitor.rs#L487-L497) process_valid_state uses state.validators().iter_from(start_index)
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:95`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L95) import_new_pubkeys uses iter_from
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:384`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L384) pending deposits iter_from
- [`consensus/types/src/state/beacon_state.rs:2983`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2983) iter_from(start_index)

**Skeptic check.** Verified iter_from in validator monitor and the other index-offset scans; no remaining validators().iter().skip(n) on non-test paths. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#9995](https://github.com/sigp/lighthouse/pull/9995)

</details>


<a id="block_import-082"></a>
<details>
<summary><b>block_import-082</b> Justification from progressively tracked balances — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Track target/participation balances incrementally as attestations are processed and use them for justification/unrealized checkpoint computation at block import, instead of scanning the validator set.

**Impact.** None needed.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fork_choice/src/fork_choice.rs:946-954`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L946-L954) on_block computes unrealized checkpoints with altair process_justification_and_finalization
- [`consensus/state_processing/src/per_epoch_processing/altair/justification_and_finalization.rs:9-30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/altair/justification_and_finalization.rs#L9-L30) reads progressive_balances_cache target balances, no validator scan
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:161`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L161) initialize_progressive_balances_cache

**Skeptic check.** Verified the post-Altair J&amp;F used at import reads cached target attesting balances (updated during attestation processing) and skips entirely when parent checkpoints can be reused. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#4326](https://github.com/ChainSafe/lodestar/pull/4326)

</details>


<a id="block_import-083"></a>
<details>
<summary><b>block_import-083</b> Compute signed block header lazily — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** On the block import hot path, do not compute the signed block header (which hashes the full body including payload) up front; compute it only on the slashing/error path that needs it. This removes a full block hash per import.

**Impact.** Done by lighthouse#8446.

**Best measured result.** shaves 10-20ms off pre-newPayload delay and every block import (pr:lighthouse#8446)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1324-1335`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1324-L1335) from_gossip_verified_block_check_slashable builds header only in map_err
- [`beacon_node/beacon_chain/src/block_verification.rs:1247-1253`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1247-L1253) check_slashable lazy header
- [`beacon_node/beacon_chain/src/block_verification.rs:1360-1376`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1360-L1376) SignatureVerifiedBlock path lazy
- [`beacon_node/beacon_chain/src/block_verification.rs:1446-1449`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1446-L1449) LookupBlock lazy
- [`beacon_node/beacon_chain/src/block_verification.rs:851-855`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L851-L855) success-path header only when slasher enabled
- [`beacon_node/beacon_chain/src/block_verification.rs:886-890`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L886-L890) gossip header doubles as block-root computation

**Skeptic check.** Verified gossip, lookup and range-sync (SignatureVerifiedBlock) paths build the header only on error. The eager header in the RangeSyncBlock impl (block_verification.rs:1403) is not on the range sync path, which goes through signature_verify_chain_segment.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#8446](https://github.com/sigp/lighthouse/pull/8446)

</details>


<a id="block_import-084"></a>
<details>
<summary><b>block_import-084</b> Skip import of already-known blocks — <i>implemented · medium · S · cpu, sync</i></summary>

**Idea.** At the start of block processing or requeue, check whether the block root is already in fork choice (or the live chain index) and return early, so duplicates from gossip and sync never rerun state transition or pre-state regeneration. The check must survive state pruning.

**Impact.** None needed.

**Best measured result.** Loop consumed 100% CPU for hours and ~3.5GB of logs per node (pr:ethlambda#234)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:970-973`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L970-L973) gossip contains_block -&gt; DuplicateFullyImported before parent load
- [`beacon_node/beacon_chain/src/block_verification.rs:1948-1954`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1948-L1954) check_block_relevancy at start of lookup/range import
- [`beacon_node/beacon_chain/src/block_verification.rs:1089-1095`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1089-L1095) observed_block_producers -&gt; DuplicateImportStatusUnknown
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3142`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3142) chain segment skips duplicates
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4512`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4512) final re-check under fork choice lock

**Skeptic check.** Verified duplicates are rejected via fork choice (which holds blocks after state pruning; pre-finalized blocks are rejected by check_block_against_finalized_slot) before any state load on gossip, RPC and range sync. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [ethlambda#234](https://github.com/lambdaclass/ethlambda/pull/234), [prysm#5850](https://github.com/OffchainLabs/prysm/pull/5850), [teku#1214](https://github.com/Consensys-Incorporated/teku/pull/1214), [lighthouse#4214](https://github.com/sigp/lighthouse/pull/4214)

</details>


<a id="block_import-085"></a>
<details>
<summary><b>block_import-085</b> Recheck known block under fork choice lock — <i>implemented · low · S · cpu, disk, latency</i></summary>

**Idea.** After acquiring the fork-choice lock in block import, re-check whether the block was already imported by a concurrent task and return early, avoiding repeated state writes and head recomputation.

**Impact.** Already in place (lighthouse#8050).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:4508-4518`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4508-L4518) upgradable read lock, contains_block returns DuplicateFullyImported before upgrade to write

**Skeptic check.** Verified the re-check under the fork choice lock in import_block, before on_block and state writes. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#8050](https://github.com/sigp/lighthouse/pull/8050)

</details>


<a id="block_import-086"></a>
<details>
<summary><b>block_import-086</b> Load missing parent from local DB — <i>n/a · low · S · sync, bandwidth</i></summary>

**Idea.** When a block's parent is unknown to fork choice, check the local database for the parent block and enqueue it, instead of requesting the branch from the network.

**Impact.** A parent in the DB but not in fork choice is pre-finalization or conflicting, so it cannot be imported anyway; fork choice is persisted across restarts, so the case Nimbus handles does not arise.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1518`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1518) ParentUnknown only when fork choice lacks parent
- block_verification.rs:1895 store.block_exists used only to distinguish NotFinalizedDescendant

**Sources.** [nimbus#6122](https://github.com/status-im/nimbus-eth2/pull/6122)

</details>


<a id="block_import-087"></a>
<details>
<summary><b>block_import-087</b> Reject blocks with huge parent skip distance — <i>not · medium · S · memory, disk</i></summary>

**Idea.** Reject blocks whose parent is more than a configurable number of slots behind, so minority forks cannot force long state advances and storage of their states.

**Gap in Lighthouse.** The block check from #1530 was deliberately removed in #4403. Adding it back means a parent.slot + import_max_skip_slots &lt; block.slot check in block verification, using chain.config.import_max_skip_slots. This needs a reason that outweighs why #4403 removed it (the tree-states store makes long advances cheap).

**Impact.** Limits state advances and stored states on minority forks. Little gain on a healthy mainnet node.

**Best measured result.** bounds RAM and disk use on minority forks; no numbers (pr:lighthouse#1530)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1003-1005`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1003-L1005) parent skip distance only observed as metric GOSSIP_BEACON_BLOCK_SKIPPED_SLOTS
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1264`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1264) TooManySkippedSlots only for attestations
- [`beacon_node/src/cli.rs:1091-1097`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L1091-L1097) --max-skip-slots help says attestations only, disabled by default
- git log: 719a69aee0 (#1530) added the block check, c76afc6630 (#4403) 'Remove legacy max-skip-slots checks' removed it from block_verification.rs

**Second check.** Searched git history (read-only) and found that Lighthouse once had this exact check and removed it on purpose in #4403. Today only the attestation path and a skip-slot metric remain.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [lighthouse#1530](https://github.com/sigp/lighthouse/pull/1530), [lighthouse#1539](https://github.com/sigp/lighthouse/pull/1539)

</details>


<a id="block_import-088"></a>
<details>
<summary><b>block_import-088</b> Move parent state into import, no clone — <i>implemented · medium · S · cpu, memory</i></summary>

**Idea.** Pass the parent pre-state into the block import function by value instead of cloning it, and load/deserialize it once for both signature verification and state transition.

**Impact.** None needed.

**Best measured result.** "avoids the previous .clone() — minor perf win" (pr:ethlambda#157)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1579`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1579) let mut state = parent.pre_state (moved)
- [`beacon_node/beacon_chain/src/block_verification.rs:1195-1201`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1195-L1201) and 1263-1274 signature verification borrows &amp;mut parent.pre_state via cheap_state_advance_to_obtain_committees
- [`beacon_node/beacon_chain/src/block_verification.rs:1038-1048`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1038-L1048) proposer-cache-miss path clones once and keeps parent in opt_parent for reuse

**Skeptic check.** Verified the parent is loaded once by load_parent and carried through signature verification into state transition by value; the one clone (milhouse, structurally shared) is on the rare proposer-cache miss. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [ethlambda#157](https://github.com/lambdaclass/ethlambda/pull/157)

</details>


<a id="block_import-089"></a>
<details>
<summary><b>block_import-089</b> Narrow deposit signature pre-verification set — <i>n/a · low · S · cpu</i></summary>

**Idea.** When pre-verifying queued deposit signatures, verify only the deposits whose result the state transition will actually read, skipping the scan and BLS work for other same-pubkey deposits.

**Impact.** Lighthouse has no async deposit-signature pre-verification queue, so there is nothing to narrow.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/process_operations.rs:757`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L757) deposit signature verified inline during state transition

**Sources.** [lodestar#10480](https://github.com/ChainSafe/lodestar/pull/10480)

</details>


<a id="block_import-090"></a>
<details>
<summary><b>block_import-090</b> Advance next-slot state immediately after head update — <i>partial · medium · S · latency</i></summary>

**Idea.** Right after a block becomes head (including late blocks), advance and cache the head state to the next slot at once, so proposals and attestations do not wait for a later state advance.

**Gap in Lighthouse.** When a head changes after the 3/4-slot timer has fired (a late block), nothing advances the new head state to the next slot. Spawn advance_head after recompute_head when the timer has already run for this slot.

**Impact.** Removes a per-slot or epoch transition from the proposal path after late blocks. This is tens of ms, or hundreds at epoch boundaries.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:125-131`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L125-L131) single advance at 3/4 slot; skipped for the slot if past it
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:258-290`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L258-L290) advance_head advances head one slot into state cache
- [`beacon_node/beacon_chain/src/canonical_head.rs:1499-1560`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1499-L1560) after_new_head updates caches/shuffling ids, no state advance
- [`beacon_node/beacon_chain/src/canonical_head.rs:1329-1355`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1329-L1355) FCR advances head state to epoch start but does not cache it
- [`beacon_node/beacon_chain/src/block_production/mod.rs:96-101`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L96-L101) production relies on timer-cached advanced state, else advances lazily

**Second check.** I also checked after_new_head, the FCR head-state advance (not cached), the shuffling and proposer caches (partial advances only) and block production state loading. None of them eagerly caches a next-slot head state after a late block.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [prysm#12462](https://github.com/OffchainLabs/prysm/pull/12462), [prysm#12321](https://github.com/OffchainLabs/prysm/pull/12321)

</details>


<a id="block_import-091"></a>
<details>
<summary><b>block_import-091</b> Send proposer FCU before next-slot cache update — <i>partial · medium · S · latency</i></summary>

**Idea.** On late-block tasks, send fork choice updates with payload attributes only when a local validator proposes next, and do it before updating the next-slot cache, giving the EL more time to build.

**Gap in Lighthouse.** The local-proposer gate exists, so the earlier evidence that it was 'gated on any registered proposer' was wrong. The missing part: on a new head, the first FCU has no attributes because none are cached yet for the new root. The attribute FCU then waits for withdrawals to be computed (a state advance). Computing the attributes before or in the first FCU would give the EL one FCU and more build time.

**Impact.** Gives the EL a little more build time on proposer slots after late blocks and saves one FCU. The effect is small.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:6893-6902`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6893-L6902) prepare_beacon_proposer returns early unless the EL has preparation data for the specific next-slot proposer (local-proposer gate exists)
- [`beacon_node/execution_layer/src/lib.rs:1578-1581`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1578-L1581) every FCU attaches cached payload attributes for (next_slot, head_root) when present
- [`beacon_node/beacon_chain/src/canonical_head.rs:1907-1935`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1907-L1935) head update sends FCU first, then prepare_beacon_proposer (second FCU with attributes; comment accepts the double call)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5396-5460`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5396-L5460) withdrawals for new attributes are computed via partial_state_advance before the attribute FCU is sent

**Second check.** Corrected the evidence: the per-proposer gate is at beacon_chain.rs:6896, and the any-proposer check at 6738 is only an early exit. Lighthouse has no separate next-slot cache, so the 'before cache update' ordering becomes 'before the withdrawals state advance', which is not done.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [prysm#12469](https://github.com/OffchainLabs/prysm/pull/12469)

</details>


<a id="block_import-092"></a>
<details>
<summary><b>block_import-092</b> Notify reprocess queue on every import path — <i>partial · low · S · latency</i></summary>

**Idea.** When a block or payload is imported through any path (gossip, RPC columns), notify the reprocessing queue so attestations waiting on it are released at once instead of on a fallback timer.

**Gap in Lighthouse.** Not every import path notifies. attempt_data_column_reconstruction (network_beacon_processor/mod.rs) completes the import through reconstruct_data_columns and only calls recompute_head_at_current_slot, so attestations queued on that root (or, post-Gloas, on its payload) wait for the 12s QUEUED_ATTESTATION_DELAY fallback. The HTTP API paths (publish_blocks.rs publish_block_p2p result handling and execution_payload_envelopes.rs process_execution_payload_envelope) also do not send BlockImported/PayloadEnvelopeImported; http_api has no beacon_processor_send handle for this. Fix: call notify_import_after_column after reconstruction import, and plumb a reprocess sender (or an import event the network processor listens to) for the HTTP paths.

**Impact.** Attestations waiting on a block or payload that became available through column reconstruction, or was published via the HTTP API, are released at once instead of after up to 12s.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:4104`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L4104) notify_import_after_column helper
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1009`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1009),1450,1957,4087 gossip column, partial column, block and envelope paths notify
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:191`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L191),290,363 RPC block, custody column and envelope paths notify
- [`beacon_node/network/src/network_beacon_processor/mod.rs:1037`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L1037) EL-blobs path notifies
- [`beacon_node/network/src/network_beacon_processor/mod.rs:1213-1226`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L1213-L1226) attempt_data_column_reconstruction: Imported -&gt; recompute_head_at_current_slot only, no notify
- [`beacon_node/http_api/src/publish_blocks.rs:589-610`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L589-L610) HTTP-API block import: recompute_head only, no reprocess notification
- [`beacon_node/http_api/src/beacon/execution_payload_envelopes.rs:334-346`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/execution_payload_envelopes.rs#L334-L346) HTTP-API envelope import: no PayloadEnvelopeImported notification
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:53`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L53) QUEUED_ATTESTATION_DELAY 12s fallback

**Skeptic check.** The earlier evidence is right for gossip, RPC and EL-blobs paths (PR #10128 added the RPC-column one), but the reconstruction import in mod.rs:1220 and both HTTP API import paths do not notify the reprocess queue.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lighthouse#10128](https://github.com/sigp/lighthouse/pull/10128)

</details>


<a id="block_import-093"></a>
<details>
<summary><b>block_import-093</b> Query optimistic status once per batch tail — <i>n/a · medium · cpu</i></summary>

**Idea.** When importing a batch of blocks, query execution validity/optimistic status for the last block only, since a valid tail implies valid ancestors.

**Impact.** Lighthouse learns validity from each newPayload response, not by querying optimistic status per block, so there is no per-block query to skip.

**Evidence (Lighthouse @ 928b61e719).**

- beacon_chain.rs:3208 process_chain_segment imports blocks sequentially
- block_verification.rs newPayload response recorded per block into fork choice

**Sources.** [prysm#12741](https://github.com/OffchainLabs/prysm/pull/12741)

</details>


<a id="block_import-094"></a>
<details>
<summary><b>block_import-094</b> Run state transition concurrently with newPayload — <i>implemented · high · S · latency</i></summary>

**Idea.** During block import, send engine_newPayload and run the consensus state transition concurrently instead of sequentially, so import costs the max of the two, not the sum.

**Impact.** Import already costs max(newPayload, state transition).

**Best measured result.** shed about 200ms on a normal slot (pr:prysm#12590)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1531-1571`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1531-L1571) PayloadNotifier future spawned with spawn_handle before state advance
- [`beacon_node/beacon_chain/src/block_verification.rs:1573-1710`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1573-L1710) catch-up per_slot_processing and per_block_processing run while newPayload is in flight
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4092-4112`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4092-L4112) into_executed_block awaits payload_verification_handle afterwards

**Skeptic check.** Verified: notify_new_payload is spawned as its own task before catch-up and per_block_processing, and joined only in into_executed_block. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [ethlambda#755](https://github.com/lambdaclass/ethlambda/pull/755), [prysm#12590](https://github.com/OffchainLabs/prysm/pull/12590)

</details>


<a id="block_import-095"></a>
<details>
<summary><b>block_import-095</b> Persist block concurrently with verification — <i>not · medium · M · latency, disk</i></summary>

**Idea.** Start writing the block and blobs to the database in parallel with signature, state transition and payload verification, and delete them if verification fails, so DB I/O is off the critical path to head.

**Gap in Lighthouse.** Start the block (and blobs/columns) DB write concurrently with signature/state/payload verification and roll back with StoreOp::DeleteBlock on failure; must keep fork choice and DB consistent (issue #2028 comment at import_block).

**Impact.** Removes block DB write latency from the head-update path; early_attester_cache already makes the block attestable before the write, so gain is mostly shorter fork-choice lock hold and faster import completion.

**Best measured result.** Persisting a block took 1-2s, up to 3s under I/O lag (pr:lodestar#5473)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:4733-4756`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4733-L4756) PutBlock/PutState/blobs ops pushed and written only after fork choice on_block, inside import_block
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4759-4761`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4759-L4761) fork choice write lock held until DB write completes
- [`beacon_node/store/src/hot_cold_store.rs:1488-1534`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1488-L1534) do_atomically_with_block_and_blobs_cache is one synchronous write, no early/speculative path

**Second check.** Checked the full import_block tail and the store atomic write for any speculative or early persist of blocks or columns; none exists, data columns stay in the DA checker until import.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [lodestar#5473](https://github.com/ChainSafe/lodestar/pull/5473)

</details>


<a id="block_import-096"></a>
<details>
<summary><b>block_import-096</b> Write blobs in parallel with fork choice write — <i>not · medium · S · latency, disk</i></summary>

**Idea.** During block import, write blobs/columns to the database in parallel with the fork choice and block write instead of sequentially.

**Gap in Lighthouse.** Run the blobs_db write concurrently with the hot_db write (e.g. std::thread::scope / rayon::join) inside do_atomically_with_block_and_blobs_cache, joining before the block cache guard and fork choice lock are released; rollback logic is reusable.

**Impact.** Overlaps the blob/column write with the hot DB write on import of blocks with data; saves up to the blob write duration (few to tens of ms).

**Best measured result.** small gain, no numbers (pr:lighthouse#8404)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1519-1534`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1519-L1534) blobs_db.do_atomically runs, then hot_db.do_atomically, strictly sequential
- [`beacon_node/store/src/hot_cold_store.rs:1536`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1536) rollback of blob ops on hot_db failure already exists
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4740-4756`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4740-L4756) blobs op added to the same ops batch as PutBlock

**Second check.** Grepped hot_cold_store.rs for spawn/thread::scope/rayon::join and found no parallel write; upstream PR #8404 that did this is not in the tree.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [lighthouse#8404](https://github.com/sigp/lighthouse/pull/8404)

</details>


<a id="block_import-097"></a>
<details>
<summary><b>block_import-097</b> Parallel attestation signature verification per block — <i>not · low · M · cpu, latency</i></summary>

**Idea.** Verify the signatures of all attestations in a block in parallel across threads during block import, since BLS verification dominates import time.

**Gap in Lighthouse.** Lighthouse already batch-verifies all block signatures with random-scalar multi-pairing (cheaper than Teku's per-attestation verify) but on one thread despite the struct name. Change ParallelSignatureSets::verify to split sets into N chunks and run verify_signature_sets per chunk with rayon (or the blocking pool), AND-ing results; also parallelize pubkey aggregation/set construction in include_attestations.

**Impact.** Block signature verification (~128 attestation sets, tens of ms) could drop by a factor of the cores used, roughly 2-4x on the signature step of block import; loses some batch amortization of the final exponentiation.

**Best measured result.** Block import 0.351-&gt;0.226 s/op (1024 validators), 0.529-&gt;0.352 s/op (3072); ~50% faster (pr:teku#1106)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/block_signature_verifier.rs:459-461`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/block_signature_verifier.rs#L459-L461) ParallelSignatureSets::verify calls verify_signature_sets once
- [`crypto/bls/src/impls/blst.rs:36-110`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L36-L110) single-threaded randomized batch verify, one multi-pairing
- [`consensus/state_processing/src/per_block_processing/block_signature_verifier.rs:283-308`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/block_signature_verifier.rs#L283-L308) attestation sets collected sequentially

**Sources.** [teku#1106](https://github.com/Consensys-Incorporated/teku/pull/1106)

</details>


<a id="block_import-098"></a>
<details>
<summary><b>block_import-098</b> Reuse in-hand state instead of DB refetch — <i>implemented · low · S · disk, latency, cpu</i></summary>

**Idea.** Load the beacon state once per block and pass the reference (pre- and post-state) to later steps such as fork choice vote processing, instead of re-reading state from the database.

**Impact.** No extra DB reads on import.

**Best measured result.** 3 DB fetches reduced (pr:prysm#1257)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:4454-4462`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4454-L4462) import_block takes the post-state by value
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4532-4540`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4532-L4540) fork_choice.on_block receives &amp;state
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4720-4734`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4720-L4734) shuffling cache, attestation observation, validator monitor and slasher reuse the same &amp;state

**Skeptic check.** Verified: the post-state from per_block_processing flows by reference through on_block and the post-import hooks, and nothing re-reads it from the store. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#1257](https://github.com/OffchainLabs/prysm/pull/1257), [prysm#4395](https://github.com/OffchainLabs/prysm/pull/4395)

</details>


<a id="block_import-099"></a>
<details>
<summary><b>block_import-099</b> Pause gossip intake while processing current block — <i>not · medium · S · latency, cpu</i></summary>

**Idea.** While the current-slot block is being processed, stop pulling new gossip jobs from the network processor so the block gets full CPU, instead of capping concurrency for the whole slot.

**Gap in Lighthouse.** Track a current-slot block-in-flight flag in the BeaconProcessor manager loop (set when spawning GossipBlock, cleared on WorkerFinished) and hold attestation/aggregate/low-priority work in their queues while it is set.

**Impact.** More CPU for block signature verification and state transition in the hot window; modest because queue priority already favours blocks and workers are capped at num_cpus.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:890`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L890) can_spawn only checks current_workers &lt; max_workers
- [`beacon_node/beacon_processor/src/lib.rs:801-810`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L801-L810) worker completion only decrements worker count and per-peer block queue state
- [`beacon_node/beacon_processor/src/scheduler/work_queue.rs:170-214`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_queue.rs#L170-L214) per-peer gossip block queue gives per-peer fairness, not a global pause
- [`beacon_node/beacon_processor/src/lib.rs:1290`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1290) any other work spawns immediately whenever a worker slot is free, even while a block is processing

**Second check.** Checked the scheduler work_queue per-peer block gating and the reprocess queue; both are unrelated to pausing other work while a block runs.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [lodestar#5458](https://github.com/ChainSafe/lodestar/pull/5458)

</details>


<a id="block_import-100"></a>
<details>
<summary><b>block_import-100</b> Pipelined block processing stream — <i>n/a · low · L · cpu, latency</i></summary>

**Idea.** Process blocks as a pipeline of validate/process/post-process stages, with parent-missing blocks held in a pool and requeued when the parent arrives.

**Impact.** Lighthouse's design is a beacon processor work queue plus sync lookups with its own staged verification (gossip -&gt; signature -&gt; import); a Lodestar-style stream pipeline would be a redesign with no clear gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1500-1530`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1500-L1530) ParentUnknown returned and handled by sync lookups
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs) reprocess queue for early/unknown-parent work

**Sources.** [lodestar#758](https://github.com/ChainSafe/lodestar/pull/758)

</details>


<a id="block_import-101"></a>
<details>
<summary><b>block_import-101</b> Plain struct for signature-only indexed attestation — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** For indexed (payload) attestations used only for signature verification in block processing, use a plain struct instead of an SSZ tree-backed container, avoiding tree node allocation.

**Impact.** No tree-node allocation for indexed payload attestations; already in place.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/attestation/indexed_payload_attestation.rs:15`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/attestation/indexed_payload_attestation.rs#L15) plain struct (VariableList + PayloadAttestationData + AggregateSignature), no milhouse tree
- [`consensus/state_processing/src/consensus_context.rs:32`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/consensus_context.rs#L32),197-210 cached in a HashMap and built once per payload attestation

**Skeptic check.** Verified: Lighthouse operation types are plain SSZ structs, not tree-backed views, so Teku's change has no counterpart to make. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#10964](https://github.com/Consensys-Incorporated/teku/pull/10964)

</details>


<a id="block_import-102"></a>
<details>
<summary><b>block_import-102</b> Point pubkey lookups for sync aggregate — <i>implemented · medium · S · cpu, memory</i></summary>

**Idea.** When processing a SyncAggregate, look up the 512 committee pubkeys individually in the state pubkey index instead of building a map of all validator pubkeys.

**Impact.** No per-block full validator map build.

**Best measured result.** 190k-entry map and 190k lookups reduced to 512 lookups (pr:prysm#9177)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:1753-1767`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1753-L1767) get_sync_committee_indices does 512 pubkey_cache().get() lookups
- [`consensus/types/src/state/beacon_state.rs:2979-2993`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2979-L2993) update_pubkey_cache only inserts validators past the cached length
- [`consensus/types/src/state/pubkey_cache.rs:8-14`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/pubkey_cache.rs#L8-L14) persistent HashTrieMap shared structurally across state clones
- [`consensus/state_processing/src/per_block_processing/altair/sync_committee.rs:50`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/altair/sync_committee.rs#L50) process_sync_aggregate uses it

**Skeptic check.** Verified: the pubkey index lives on the state as a persistent map that clones cheaply, and it is updated incrementally, so a sync aggregate costs 512 point lookups. A state freshly loaded from disk starts with an empty cache and rebuilds it once, but epoch processing (single_pass.rs:165) needs that anyway.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#9177](https://github.com/OffchainLabs/prysm/pull/9177)

</details>


<a id="block_import-103"></a>
<details>
<summary><b>block_import-103</b> Cheap pre-checks before EL validation — <i>implemented · low · S · sync, latency, cpu</i></summary>

**Idea.** Run cheap checks (known unviable, duplicate, missing parent) before calling the EL in block import, so invalid or redundant blocks never cost an engine call.

**Impact.** Duplicate, unknown-parent, pre-finalized and invalid-parent blocks never cost an engine call, on gossip, RPC and range-sync paths.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1500-1522`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1500-L1522) parent unknown / parent payload invalid rejected before EL
- [`beacon_node/beacon_chain/src/block_verification.rs:1528`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1528) check_block_relevancy runs before PayloadNotifier
- [`beacon_node/beacon_chain/src/block_verification.rs:1915-1957`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1915-L1957) check_block_relevancy: future slot, finalized slot, DuplicateFullyImported via fork_choice.contains_block
- [`beacon_node/beacon_chain/src/block_verification.rs:1555`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1555) notify_new_payload only after those checks

**Skeptic check.** Verified that into_execution_pending_block, which every import path (gossip, RPC lookup, chain segment) goes through, runs the parent, relevancy and duplicate checks before it creates the newPayload future. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#5169](https://github.com/status-im/nimbus-eth2/pull/5169)

</details>


<a id="block_import-104"></a>
<details>
<summary><b>block_import-104</b> Preallocated zero values for empty-payload checks — <i>n/a · low · S · memory, cpu</i></summary>

**Idea.** When checking whether execution payload fields are empty, compare against static preallocated zero values instead of allocating zero buffers on every call.

**Impact.** Rust compares by value against a stack default; empty VariableList/Vec do not allocate, and post-Capella the check is skipped, so there is no per-call allocation to remove.

**Best measured result.** Allocations per call 8 -&gt; 0 (pr:prysm#16264)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/execution/execution_payload_header.rs:169`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/execution/execution_payload_header.rs#L169) is_default_with_zero_roots compares to Default::default() on the stack
- [`consensus/state_processing/src/per_block_processing.rs:508`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing.rs#L508) is_merge_transition_complete short-circuits true from Capella

**Sources.** [prysm#16264](https://github.com/OffchainLabs/prysm/pull/16264)

</details>


<a id="block_import-105"></a>
<details>
<summary><b>block_import-105</b> Prebuild committee cache on pre-state — <i>implemented · low · S · cpu</i></summary>

**Idea.** Build the current-epoch committee cache on the pre-state once before per-block processing so attestation processing reads cached committees.

**Impact.** Attestation processing reads cached committees already.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing.rs:184-186`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing.rs#L184-L186) builds Previous and Current committee caches before operations
- [`beacon_node/beacon_chain/src/block_verification.rs:1692`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1692) build_all_committee_caches on the pre-state before per_block_processing
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:334-340`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L334-L340) committee caches built on the advanced head state

**Skeptic check.** Verified that the caches are built once on the pre-state before operations are processed, and that the state advance builds them ahead of time. This is the Lighthouse commit itself.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@f530f5a84](https://github.com/sigp/lighthouse/commit/f530f5a848c5)

</details>


<a id="block_import-106"></a>
<details>
<summary><b>block_import-106</b> Precompute next epoch transition ahead of time — <i>implemented · high · S · latency, cpu</i></summary>

**Idea.** Near the end of an epoch, run the epoch transition for the head state on a background worker and cache the advanced state keyed by (epoch, parent root), so the first block of the epoch reuses it instead of running process_epoch inline.

**Impact.** The first block of an epoch skips inline process_epoch when it builds on the head.

**Best measured result.** Epoch-start blocks take ~1.5 s vs ~0.58 s for an ordinary block (the cost targeted); no after-number given (pr:ethlambda#652)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:117-178`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L117-L178) timer fires at 3/4 of the slot and spawns advance_head on a blocking worker
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:258-298`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L258-L298) advance_head loads the head state and runs per_slot_processing, including epoch processing at the boundary
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:455`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L455) put_state caches the advanced state
- [`beacon_node/beacon_chain/src/block_verification.rs:2063`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L2063) block verification loads the parent via get_advanced_hot_state, which returns the pre-advanced state

**Skeptic check.** Verified: the head state is advanced one slot (epoch transition included) in the tail of each slot and stored for get_advanced_hot_state, keyed by block root and slot. As in ethlambda, this covers only the head, and a last-slot block that arrives after 9s does not get the advance.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [ethlambda#652](https://github.com/lambdaclass/ethlambda/pull/652)

</details>


<a id="block_import-107"></a>
<details>
<summary><b>block_import-107</b> Precomputed blob schedule lookup — <i>implemented · low · S · cpu</i></summary>

**Idea.** Precompute the blob schedule (epoch to max blobs) into a sorted/indexed structure at startup, instead of scanning the schedule per processed block.

**Impact.** The schedule is sorted once; each lookup is a short scan with no sort or allocation.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/core/chain_spec.rs:805-815`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/core/chain_spec.rs#L805-L815) max_blobs_per_block uses blob_schedule
- [`consensus/types/src/core/chain_spec.rs:2077-2084`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/core/chain_spec.rs#L2077-L2084) EpochSchedule::new sorts once (reverse by epoch) at construction/deserialize
- [`consensus/types/src/core/chain_spec.rs:2097`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/core/chain_spec.rs#L2097) entry_for_epoch is a first-match find over the pre-sorted vec

**Skeptic check.** Verified: the per-call sort or scan that Teku removed does not exist here. The lookup is an early-exit find over a few pre-sorted entries. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#9563](https://github.com/Consensys-Incorporated/teku/pull/9563)

</details>


<a id="block_import-108"></a>
<details>
<summary><b>block_import-108</b> Prefetch deposit request signature checks — <i>not · low · M · cpu, latency</i></summary>

**Idea.** When a payload envelope arrives, batch-verify its deposit request signatures off the critical path and cache the invalid indices by execution_requests_root, so block processing skips inline BLS verification.

**Gap in Lighthouse.** Builder deposit request signatures are checked inline with one BLS verify each, with no prefetch on envelope receipt and no cache keyed by execution_requests_root. Lighthouse would add a prefetch task at envelope gossip verification that batch-verifies builder_deposits and stores results (a new cache, domain BuilderDeposit kept separate from OnboardBuildersCache), read by process_builder_deposit_request.

**Impact.** Only matters post-Gloas and only for envelopes carrying builder deposits (rare, a few BLS verifies, ~1 ms each); takes a little off envelope import, not mainnet-visible today.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/process_operations.rs:925`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L925) process_builder_deposit_request verifies signature inline (line 941)
- [`consensus/state_processing/src/builder_deposits_cache.rs:164`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/builder_deposits_cache.rs#L164) cache exists only for fork-time onboarding of pending_deposits
- [`consensus/state_processing/src/per_block_processing.rs:643`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing.rs#L643) requests processed inline in block processing

**Sources.** [prysm#16812](https://github.com/OffchainLabs/prysm/pull/16812)

</details>


<a id="block_import-109"></a>
<details>
<summary><b>block_import-109</b> Prime proposer cache during state advance — <i>implemented · low · S · latency</i></summary>

**Idea.** During the pre-slot state advance, prime the proposer shuffling cache so importing the next block does not pay a proposer cache miss.

**Impact.** The state advance fills the proposer cache before the next block arrives, so the block's gossip proposer check does not miss the cache.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:347-367`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L347-L367) with_proposer_cache primes current-epoch proposer shuffling on epoch transition
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:369-393`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L369-L393) also primes next-epoch shuffling when past its decision slot (post-Fulu lookahead)

**Skeptic check.** Verified the priming in advance_head on epoch boundaries, which is this Lighthouse PR. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#2252](https://github.com/sigp/lighthouse/pull/2252)

</details>


<a id="block_import-110"></a>
<details>
<summary><b>block_import-110</b> Apply proposer boost before DB write — <i>implemented · medium · S · latency</i></summary>

**Idea.** On block import, set proposer boost in fork choice before persisting the block and state, so the boost does not wait for the DB write.

**Impact.** The boost and the attestable head do not wait for the DB write.

**Best measured result.** ~100ms to set boost, ~50ms of it DB save; about 50% less wait (pr:prysm#10509)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:4532-4540`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4532-L4540) fork_choice.on_block (sets proposer boost) runs first
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4545-4700`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4545-L4700) get_head with the boost and the early attester cache come before the DB write
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4752-4769`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4752-L4769) do_atomically_with_block_and_blobs_cache comes after, and then the fork choice lock is dropped

**Skeptic check.** Verified: the boost is set inside on_block, and the boosted get_head plus the early attester cache run before the block and state are persisted. The fork choice write lock is still held through the DB write, so canonical head recompute and FCU happen only after it. Prysm's PR changed the boost order only, so the idea is upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#10509](https://github.com/OffchainLabs/prysm/pull/10509)

</details>


<a id="block_import-111"></a>
<details>
<summary><b>block_import-111</b> Remove block-waiter listeners after resolution — <i>n/a · low · S · memory</i></summary>

**Idea.** When a task waits for a block to be processed via an event listener, remove the listener once the block arrives so listeners do not accumulate.

**Impact.** JS event-listener leak; Lighthouse uses channel/state-machine based lookups with no listener lists to accumulate.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/mod.rs:516`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L516) lookups are event/state-machine driven, no per-block listeners

**Sources.** [lodestar@d03974477](https://github.com/ChainSafe/lodestar/commit/d039744775be)

</details>


<a id="block_import-112"></a>
<details>
<summary><b>block_import-112</b> Skip non-newer finalized checkpoint DB write — <i>implemented · low · S · disk</i></summary>

**Idea.** Write the finalized checkpoint to the database only when it is newer than the stored one.

**Impact.** Finalization DB work runs only when the checkpoint changes. Fork choice finality is monotonic, so an older checkpoint is never written.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:1280`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1280) after_finalization runs only when finalized_checkpoint changed
- [`beacon_node/beacon_chain/src/canonical_head.rs:1563-1566`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1563-L1566) fork choice persisted per head update only on epoch transition or reorg
- [`beacon_node/beacon_chain/src/canonical_head.rs:1720`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1720) persist + migration only inside after_finalization

**Skeptic check.** Verified the gate in recompute_head. Lighthouse has no separate finalized-checkpoint key that each block import writes. Prysm's bug (writing a stale checkpoint) has no counterpart here.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#11356](https://github.com/OffchainLabs/prysm/pull/11356)

</details>


<a id="block_import-113"></a>
<details>
<summary><b>block_import-113</b> Cheap override-FCU check before payload attributes — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Run the cheap fork choice check for whether an FCU with attributes is needed before computing payload attributes, which copies state and may process slots.

**Impact.** The expensive attribute work (withdrawals and a possible state load) happens only for a registered local proposer on a cache miss, after the cheap fork-choice and proposer checks.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:6738-6742`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6738-L6742) early exit when no proposer preparation data
- [`beacon_node/beacon_chain/src/beacon_chain.rs:6763-6776`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6763-L6776) overridden_forkchoice_update_params (pre-Gloas) then get_pre_payload_attributes using proposer cache and cached head, no state copy
- [`beacon_node/beacon_chain/src/beacon_chain.rs:6893-6899`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6893-L6899) has_proposer_preparation_data(proposer) check before any withdrawals work
- [`beacon_node/beacon_chain/src/beacon_chain.rs:6960-6985`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6960-L6985) cached payload attributes reused; compute_withdrawals_for_payload_attributes only on cache miss

**Skeptic check.** The mechanism differs from Prysm. In Lighthouse the override check changes the head instead of skipping the FCU, so the attributes are still needed. But the cheap checks and the attribute cache come first, so no state copy is wasted. The earlier evidence is correct in effect.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#16952](https://github.com/OffchainLabs/prysm/pull/16952)

</details>


<a id="block_import-114"></a>
<details>
<summary><b>block_import-114</b> Skip proposer prep work during initial sync — <i>implemented · medium · S · cpu, latency, sync</i></summary>

**Idea.** While the node is initial-syncing (detected by head age or sync state), skip payload-attribute computation, late-block tasks and attestation-triggered head updates, since no FCU with attributes is sent.

**Impact.** Payload-attribute and late-slot work is skipped while syncing.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:6738-6742`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6738-L6742) early exit with no registered proposers
- [`beacon_node/beacon_chain/src/beacon_chain.rs:6753-6761`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6753-L6761) prepare_beacon_proposer returns when head_slot + sync_tolerance_epochs*32 &lt; current_slot
- [`beacon_node/beacon_chain/src/chain_config.rs:16`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/chain_config.rs#L16) DEFAULT_SYNC_TOLERANCE_EPOCHS = 2
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:205-208`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L205-L208) no fork choice lookahead or proposer prep when best_slot + 256 &lt; current_slot
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:264-273`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L264-L273) no state advance during sync
- [`beacon_node/beacon_chain/src/canonical_head.rs:1931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1931) the post-head-update call goes through the same gated prepare_beacon_proposer

**Skeptic check.** Verified: every payload-attribute path goes through prepare_beacon_proposer, which bails out on a stale head, and the timer tasks bail out at 256 slots behind. Lighthouse has no attestation-triggered head update to gate. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#16721](https://github.com/OffchainLabs/prysm/pull/16721), [prysm#13479](https://github.com/OffchainLabs/prysm/pull/13479), [prysm#12526](https://github.com/OffchainLabs/prysm/pull/12526)

</details>


<a id="block_import-115"></a>
<details>
<summary><b>block_import-115</b> Skip slot processing for payload attributes — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** When computing payload attributes, skip process_slots and state copying unless a local validator proposes the next slot (proposer lookahead is in state).

**Impact.** No epoch processing at slot 31 unless a local validator proposes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5286-5358`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5286-L5358) get_pre_payload_attributes gets the proposer from beacon_proposer_cache, and on a miss from a head-state clone
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:321-355`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L321-L355) ensure_state_can_determine_proposers_for_epoch advances only when the state epoch is below the decision epoch, which is never the case post-Fulu for the next epoch
- [`beacon_node/beacon_chain/src/beacon_chain.rs:6895-6902`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6895-L6902) has_proposer_preparation_data(proposer) gate
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5396-5430`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5396-L5430) withdrawals (the state advance) are computed only after that gate

**Skeptic check.** Verified: the proposer index comes from the cache or the proposer lookahead with no process_slots, and withdrawals and get_advanced_hot_state run only after the local-proposer check. The tree-states clone is cheap. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#16168](https://github.com/OffchainLabs/prysm/pull/16168)

</details>


<a id="block_import-116"></a>
<details>
<summary><b>block_import-116</b> Restore chain from in-memory blocks at restart — <i>n/a · low · L · startup, disk</i></summary>

**Idea.** On restart, rebuild chain state by reprocessing blocks from in-memory data instead of reading each from the database.

**Impact.** Lighthouse restores fork choice from a persisted snapshot and the head from the DB; it does not replay blocks on restart (replay happens only on fork-choice corruption recovery), so there is nothing to feed from memory.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/builder.rs:245`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L245) load_fork_choice restores persisted fork choice at restart instead of reprocessing blocks

**Sources.** [lodestar#926](https://github.com/ChainSafe/lodestar/pull/926)

</details>


<a id="block_import-117"></a>
<details>
<summary><b>block_import-117</b> Retry DA-failed import on tracker completion — <i>implemented · low · S · latency</i></summary>

**Idea.** When a block import fails for missing data, attach the retry to the blob/column tracker completion future instead of a polling retry pool, so it retries immediately.

**Impact.** No polling delay.

**Best measured result.** no delay, no polling (pr:teku#8157)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker.rs:322-452`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L322-L452) put_* return Availability::Available when the last component arrives
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:546`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L546) availability check on each insert
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4362-4395`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4362-L4395) process_availability imports at once on Available

**Skeptic check.** Verified: the pending block waits in the DA cache, and the blob or column insert that completes it returns Available and triggers the import in the same call. There is no retry pool. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#8157](https://github.com/Consensys-Incorporated/teku/pull/8157)

</details>


<a id="block_import-118"></a>
<details>
<summary><b>block_import-118</b> Retry import when parent became known meanwhile — <i>partial · low · S · sync</i></summary>

**Idea.** If a block fails with unknown parent but the parent was imported during processing, retry it immediately instead of dropping it.

**Gap in Lighthouse.** When the parent was imported between gossip verification and the sync message, nothing re-checks fork choice: handle_unknown_parent / search_child_and_parent should check chain.block_is_known_to_fork_choice(parent_root) and resend the child to the beacon processor instead of creating a parent lookup. Today the parent is re-downloaded by BlocksByRoot (get_block_process_status returns Unknown for imported blocks), processed as a duplicate, then the child is imported.

**Impact.** Saves one RPC round-trip and duplicate processing on a rare race; the block is not dropped today.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1691`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1691) ParentUnknown sends SyncMessage::UnknownParentBlock with no re-check of fork choice
- [`beacon_node/network/src/sync/manager.rs:1001`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L1001) handle_unknown_parent creates child+parent lookups unconditionally
- [`beacon_node/network/src/sync/block_lookups/mod.rs:178`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L178) search_child_and_parent, no fork-choice check of parent_root
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1390`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1390) get_block_process_status only checks DA cache and pending payload cache, returns Unknown for a fully imported block
- [`beacon_node/network/src/sync/network_context.rs:742`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L742) so an imported parent is downloaded again by RPC
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:817`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L817) duplicate import treated as Ok, child then resumes

**Skeptic check.** Verified the block is not lost (lookup chain resumes after the duplicate parent import), but the earlier evidence was wrong that get_block_process_status skips the download for an imported block: it only sees the DA and pending-payload caches, so the parent is fetched again.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [teku#2668](https://github.com/Consensys-Incorporated/teku/pull/2668)

</details>


<a id="block_import-119"></a>
<details>
<summary><b>block_import-119</b> Reuse cached versioned hashes for newPayload — <i>not · low · S · cpu</i></summary>

**Idea.** Reuse the versioned hashes cached on the block input when building newPayload instead of recomputing them from KZG commitments.

**Gap in Lighthouse.** Cache the Vec&lt;VersionedHash&gt; next to the block and pass it to NewPayloadRequest::try_from and fetch_blobs instead of recomputing from commitments.

**Impact.** A few sha256 of 48 bytes per block; microseconds, negligible.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engine_api/new_payload_request.rs:186`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/new_payload_request.rs#L186) Deneb/Electra/Fulu recompute hashes via kzg_commitment_to_versioned_hash per call
- [`beacon_node/beacon_chain/src/payload_envelope_verification/mod.rs:417`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/mod.rs#L417) Gloas path also recomputes
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:142`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L142) recomputed again for blob fetch

**Sources.** [lodestar#8409](https://github.com/ChainSafe/lodestar/pull/8409)

</details>


<a id="block_import-120"></a>
<details>
<summary><b>block_import-120</b> Read lock where block verification only reads — <i>implemented · low · S · latency</i></summary>

**Idea.** Take a read lock instead of a write lock on fork choice or caches in block verification steps that only read.

**Impact.** Already landed (lighthouse#4340); remaining write locks mutate observed_slashable, observed_block_producers, block_times_cache and fork choice.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:970`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L970) fork_choice_read_lock in gossip verification
- [`beacon_node/beacon_chain/src/block_verification.rs:1498`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1498) fork_choice_read_lock in signature-verified path
- [`beacon_node/beacon_chain/src/block_verification.rs:1668`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1668) validator_monitor.read()
- [`beacon_node/beacon_chain/src/block_verification.rs:2218`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L2218) validator_pubkey_cache.read()
- [`beacon_node/beacon_chain/src/block_verification.rs:1755`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1755) fork_choice_write_lock only for on_attestation/on_attester_slashing (mutation)

**Skeptic check.** Checked every lock in block_verification.rs; all write locks are genuine mutations. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#4340](https://github.com/sigp/lighthouse/pull/4340)

</details>


<a id="block_import-121"></a>
<details>
<summary><b>block_import-121</b> Persist received SSZ bytes, no reserialization — <i>not · medium · M · cpu, latency, memory</i></summary>

**Idea.** Keep the raw SSZ bytes of a block received from gossip or RPC alongside the decoded block and write those bytes to the database, instead of re-serializing the block on import.

**Gap in Lighthouse.** Carry the received SSZ bytes with the block through gossip/RPC verification to the store; because the store keeps blinded block and payload in separate columns, bytes would have to be sliced at the payload offset (only practical for blinded writes, or post-Gloas blocks without a payload).

**Impact.** Saves one SSZ encode of a ~100-200 KB block per import (about 1 ms or less); small.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:527-548`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L527-L548) block_as_kv_store_ops splits into blinded block + payload and re-encodes
- [`beacon_node/store/src/hot_cold_store.rs:551-561`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L551-L561) blinded_block_as_kv_store_ops writes blinded_block.as_ssz_bytes()

**Second check.** Grepped beacon_chain, store, network and lighthouse_network for retained raw/original block bytes; none are kept past decode, and the split blinded storage format makes direct reuse impossible without slicing.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [lodestar#5573](https://github.com/ChainSafe/lodestar/pull/5573), [lodestar#5426](https://github.com/ChainSafe/lodestar/pull/5426), [lodestar#7391](https://github.com/ChainSafe/lodestar/pull/7391)

</details>


<a id="block_import-122"></a>
<details>
<summary><b>block_import-122</b> Block root from header with body root — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** In gossip verification compute the block root from the signed block header built with the body root, instead of hashing the full block again.

**Impact.** None; the gossip path hashes the body once, then the small header. The sync paths (block_sidecar_coupling.rs:140, blocks_by_root.rs:39) hash the full block once, which costs the same and has no second header hash.

**Best measured result.** ~10ms average block root on mainnet; header should take microseconds (pr:lighthouse#5003)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:886-890`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L886-L890) gossip path builds signed_block_header() once and hashes the header via get_block_header_root
- [`beacon_node/beacon_chain/src/block_verification.rs:1975-1983`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1975-L1983) get_block_header_root hashes only the header message

**Skeptic check.** Verified that PR 5003 is still in place on the gossip path. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#5003](https://github.com/sigp/lighthouse/pull/5003)

</details>


<a id="block_import-123"></a>
<details>
<summary><b>block_import-123</b> Skip churn computation when block has no exits — <i>implemented · low · S · cpu</i></summary>

**Idea.** Skip computing the exit churn limit (an active validator scan) when a block contains no voluntary exits.

**Impact.** With zero exits no churn computation or validator scan runs.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/process_operations.rs:573`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L573) process_exits loops only over the block's exits
- [`consensus/state_processing/src/common/initiate_validator_exit.rs:19`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/initiate_validator_exit.rs#L19) exit cache and churn (compute_exit_epoch_and_update_churn / get_validator_churn_limit) computed only inside initiate_validator_exit

**Skeptic check.** Verified churn is computed lazily per exit, both pre-Electra and Electra. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#12976](https://github.com/OffchainLabs/prysm/pull/12976)

</details>


<a id="block_import-124"></a>
<details>
<summary><b>block_import-124</b> Single-pass pubkey fetch for signature verify — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** In block signature verification, bounds-check and fetch validator pubkeys in one iterator pass without an intermediate vector.

**Impact.** No intermediate index Vec or second bounds-check pass exists.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/signature_sets.rs:306`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/signature_sets.rs#L306) indexed_attestation_signature_set fetches pubkeys with ValidatorUnknown check in one loop into a pre-sized Vec
- [`consensus/state_processing/src/per_block_processing/signature_sets.rs:818`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/signature_sets.rs#L818) sync aggregate pubkeys filtered and collected in one iterator pass

**Skeptic check.** The ethlambda fix removed a separate ID Vec plus bounds-check pass; Lighthouse already does lookup and bounds check in one pass. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [ethlambda#255](https://github.com/lambdaclass/ethlambda/pull/255)

</details>


<a id="block_import-125"></a>
<details>
<summary><b>block_import-125</b> Execution block hash from envelope alone — <i>implemented · low · S · cpu</i></summary>

**Idea.** Compute the execution block hash from the payload envelope alone so all incoming channels share one path and the hash check can run early.

**Impact.** One shared function; block is only needed for the bid's versioned hashes, not for the hash itself. Gloas only.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/payload_envelope_verification/mod.rs:436`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/mod.rs#L436) verify_envelope_payload_hash, the single shared check
- [`beacon_node/beacon_chain/src/payload_envelope_verification/mod.rs:420`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/mod.rs#L420) hash inputs taken from envelope.message (payload, parent_beacon_block_root, execution_requests)
- [`beacon_node/beacon_chain/src/payload_envelope_verification/execution_pending_envelope.rs:89`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/execution_pending_envelope.rs#L89) gossip path
- [`beacon_node/beacon_chain/src/payload_envelope_verification/import.rs:442`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/import.rs#L442) range-sync path
- [`beacon_node/beacon_chain/src/historical_blocks.rs:259`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_blocks.rs#L259) backfill path
- [`beacon_node/beacon_chain/src/payload_envelope_streamer/mod.rs:297`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_streamer/mod.rs#L297) streamer recomputes hash from envelope fields only

**Skeptic check.** Nimbus#9218 switched to envelope.parent_beacon_block_root for the hash and one call site; Lighthouse already builds the hash from envelope fields in one function used by all channels. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#9218](https://github.com/status-im/nimbus-eth2/pull/9218)

</details>


<a id="block_import-126"></a>
<details>
<summary><b>block_import-126</b> Skip EL validation for finalized sync envelopes — <i>not · low · M · sync</i></summary>

**Idea.** During sync, skip EL newPayload validation for payload envelopes from sources claiming finalization, sending to the EL only occasionally.

**Gap in Lighthouse.** In the range-sync envelope import, skip notify_new_payload for envelopes under a trusted finalized checkpoint except occasionally, importing as optimistic.

**Impact.** Gloas only: saves an engine call per envelope during sync; limited since EL still needs payloads.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/payload_envelope_verification/import.rs:448`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/import.rs#L448) range-sync envelope import always calls notify_new_payload
- [`beacon_node/beacon_chain/src/payload_envelope_verification/import.rs:383`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/import.rs#L383) only optimistic flag handling, no finalized skip

**Sources.** [nimbus#9130](https://github.com/status-im/nimbus-eth2/pull/9130)

</details>


<a id="block_import-127"></a>
<details>
<summary><b>block_import-127</b> Skip post-block FCU after Gloas — <i>n/a · low · cpu, latency</i></summary>

**Idea.** From Gloas onward, do not send forkchoiceUpdated to the EL in post-block processing when not needed, saving an engine call per block.

**Impact.** FCU follows head recomputation, not a fixed post-block step, so there is no separate per-block call to drop.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:1889`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1889) spawn_execution_layer_updates sends FCU only after a head change
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7180`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7180) update_execution_engine_forkchoice takes head_payload_status

**Sources.** [prysm#16373](https://github.com/OffchainLabs/prysm/pull/16373)

</details>


<a id="block_import-128"></a>
<details>
<summary><b>block_import-128</b> Skip ancestor DB walk when parent known — <i>n/a · low · cpu, disk</i></summary>

**Idea.** On regular sync, skip walking the database to fill missing fork choice ancestors when fork choice already contains the parent.

**Impact.** Lighthouse never walks the DB to fill fork choice ancestors; unknown parents trigger lookups.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:2023`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L2023) load_parent rejects ParentUnknown via in-memory fork choice check
- [`beacon_node/beacon_chain/src/block_verification.rs:1498`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1498) get_parent_import_status

**Sources.** [prysm#10957](https://github.com/OffchainLabs/prysm/pull/10957)

</details>


<a id="block_import-129"></a>
<details>
<summary><b>block_import-129</b> Skip newPayload assembly with null engine — <i>n/a · low · S · cpu, latency</i></summary>

**Idea.** When running without an execution engine (replay, state-only), skip building the newPayload request (block hash_tree_root, payload clone, versioned hashes), ideally compiled out via a static flag.

**Impact.** None on a mainnet node.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:4454`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4454) import_block (always has EL; replay uses BlockReplayer without newPayload)

**Sources.** [grandine@7d85f89e6](https://github.com/grandinetech/grandine/commit/7d85f89e66b9)

</details>


<a id="block_import-130"></a>
<details>
<summary><b>block_import-130</b> Skip indexed attestation build for trusted signatures — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** When replaying blocks with already-verified signatures, skip building indexed attestations and copying pubkeys used only for signature verification.

**Impact.** Negligible. What is left is a Vec alloc and a sortedness check per attestation, and Lighthouse needs the indices for participation anyway.

**Best measured result.** removes is_valid_indexed_attestation from performance benchmarks when replaying blocks (commit:nimbus@5ca10d3de263)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/is_valid_indexed_attestation.rs:53-64`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/is_valid_indexed_attestation.rs#L53-L64) pubkey lookup and signature set only when verify_signatures is true
- [`consensus/state_processing/src/consensus_context.rs:161-194`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/consensus_context.rs#L161-L194) indexed attestations are cached per attestation and reused from signature verification (set_indexed_attestations:220)
- [`consensus/state_processing/src/per_block_processing/verify_attestation.rs:92-93`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/verify_attestation.rs#L92-L93) indexed attestation is needed anyway for participation updates

**Skeptic check.** Lighthouse already skips the pubkey and signature work when signatures are not checked, and it reuses cached indexed attestations. The Nimbus saving applies only where the indices were built just for the signature check, which is not the case here.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus@5ca10d3de](https://github.com/status-im/nimbus-eth2/commit/5ca10d3de263)

</details>


<a id="block_import-131"></a>
<details>
<summary><b>block_import-131</b> Run single queued job immediately — <i>n/a · low · S · latency</i></summary>

**Idea.** When a processing queue (gossip validation, block processor, engine) holds a single job, run it immediately instead of waiting for the scheduler tick.

**Impact.** None.

**Best measured result.** Job wait time &gt;1s ratios charted (screenshots only) (pr:lodestar#4858)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:890`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L890) can_spawn: work spawned immediately when worker free, event-driven not tick-driven

**Sources.** [lodestar#4858](https://github.com/ChainSafe/lodestar/pull/4858)

</details>


<a id="block_import-132"></a>
<details>
<summary><b>block_import-132</b> Do not re-verify already verified block signature — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Skip re-verifying the proposer or builder signature in block/envelope processing when gossip validation already verified it, avoiding an extra BLS check and full block hash.

**Impact.** Gossip import already skips the second proposer and builder BLS check and the block re-hash. Range-sync envelopes verify signatures once (import.rs:436) because gossip never checked them.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1282-1285`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1282-L1285) include_all_signatures_except_proposal after gossip verification
- [`beacon_node/beacon_chain/src/block_verification.rs:1710`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1710) BlockSignatureStrategy::NoVerification in per_block_processing after batch verification
- [`beacon_node/beacon_chain/src/payload_envelope_verification/execution_pending_envelope.rs:80-84`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/execution_pending_envelope.rs#L80-L84) envelope verified with VerifySignatures::False after gossip verification
- [`beacon_node/beacon_chain/src/block_verification.rs:890`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L890) block root computed once and carried along

**Skeptic check.** Confirmed that the proposal signature is skipped on import after gossip, and that envelope import passes VerifySignatures::False. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#14820](https://github.com/OffchainLabs/prysm/pull/14820), [caplin#25134](https://github.com/erigontech/erigon/pull/25134)

</details>


<a id="block_import-133"></a>
<details>
<summary><b>block_import-133</b> Skip state rewind when parent state is current — <i>n/a · low · cpu</i></summary>

**Idea.** When the block's parent state is already the in-memory state, apply the block directly without rewinding and replaying, saving state hash_tree_root calls.

**Impact.** Lighthouse never rewinds a head state to the parent; it loads the parent's (pre-advanced) state from the state cache, so there is nothing to skip.

**Best measured result.** saves 4 hash_tree_roots per state; hash_tree_root was ~45-50% of node time (pr:nimbus#919)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:2057-2090`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L2057-L2090) load_parent takes a cloned state advanced to block slot via get_advanced_hot_state
- no rewind/replay machinery in the import path

**Sources.** [nimbus#919](https://github.com/status-im/nimbus-eth2/pull/919)

</details>


<a id="block_import-134"></a>
<details>
<summary><b>block_import-134</b> Wait for gossip sidecars only for recent slots — <i>n/a · medium · latency, sync</i></summary>

**Idea.** Block on gossip sidecar arrival only for current or next-slot blocks; for older blocks read sidecars from storage or fetch by root immediately instead of waiting a slot.

**Impact.** Lighthouse has no blocking wait on sidecar notifier: blocks/envelopes park in the availability cache and complete when columns arrive; missing columns trigger sync lookups. The Prysm 12s stall does not exist by design.

**Best measured result.** 12s per queued slot wait removed; fetch took ~0.9s (pr:prysm#17429)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/payload_envelope_verification/import.rs:139`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/import.rs#L139) MissingComponents returns instead of blocking
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:64`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L64),794 envelope queue delay is a timer-based reprocess entry, not a blocking wait

**Sources.** [prysm#17429](https://github.com/OffchainLabs/prysm/pull/17429)

</details>


<a id="block_import-135"></a>
<details>
<summary><b>block_import-135</b> Bound reprocess queue capacity — <i>implemented · medium · S · memory, latency</i></summary>

**Idea.** Cap the reprocessing queue and its channel below the main work channel capacity so late blocks and attestations cannot build unbounded work.

**Impact.** Both reprocess channels are bounded at 75% of the work channel, and each delay queue has its own cap. This is the mechanism of lighthouse#3239.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:91`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L91) DEFAULT_MAX_SCHEDULED_WORK_QUEUE_LEN = 3/4 of DEFAULT_MAX_WORK_EVENT_QUEUE_LEN
- [`beacon_node/beacon_processor/src/lib.rs:770-774`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L770-L774) ready_work and reprocess_work channels bounded by max_scheduled_work_queue_len
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:78-90`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L78-L90),595,670,724,807,867,898 per-kind caps checked before insertion

**Skeptic check.** Verified the channel bounds and the per-queue caps on every delay queue (blocks, envelopes, attestations, columns, LC updates). The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#3239](https://github.com/sigp/lighthouse/pull/3239)

</details>


<a id="block_import-136"></a>
<details>
<summary><b>block_import-136</b> Validate block outside the fork choice lock — <i>partial · high · M · latency, cpu</i></summary>

**Idea.** Run state transition, payload execution and signature checks before taking the fork-choice write lock, and hold the lock only to insert the block, so the lock is held briefly and forks process in parallel.

**Gap in Lighthouse.** Verification is already outside the write lock. What is missing is to release the write lock after on_block and before the block/state DB write; this needs another way to keep fork choice and the DB consistent (see handle_import_block_db_write_error).

**Impact.** Fork choice readers (attestation and gossip verification, head queries) stop blocking during the block and state DB write, a few to tens of ms per block, more for epoch-boundary states.

**Best measured result.** replay 0.25-0.35 s on Hoodi under the lock (avoided) (pr:caplin#25332)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1498`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1498) state transition, newPayload and signature checks run under only a fork choice read lock
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4510-4516`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4510-L4516) import_block upgrades to the write lock for on_block
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4752-4767`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4752-L4767) write lock is held across the DB write and dropped after it (comment: 'at the expense of concurrency')

**Second check.** Confirmed in the source that the write-lock guard is dropped only after do_atomically_with_block_and_blobs_cache, and that the code comment says this is deliberate; the write is synchronous, not deferred.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [teku#4751](https://github.com/Consensys-Incorporated/teku/pull/4751), [prysm#12589](https://github.com/OffchainLabs/prysm/pull/12589), [caplin#25332](https://github.com/erigontech/erigon/pull/25332)

</details>


<a id="block_import-137"></a>
<details>
<summary><b>block_import-137</b> Stop ancestor lookup on cancellation — <i>n/a · low · S · cpu, latency</i></summary>

**Idea.** Stop recursive ancestor lookups when the request context is cancelled so work does not continue after the deadline.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/mod.rs:779`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L779) drop_stuck_lookups; :742 drop_lookups_without_peers; :67 LOOKUP_MAX_DURATION_STUCK_SECS

**Sources.** [prysm#4420](https://github.com/OffchainLabs/prysm/pull/4420)

</details>


<a id="block_import-138"></a>
<details>
<summary><b>block_import-138</b> Load envelope summary instead of full payload — <i>implemented · low · S · disk, latency</i></summary>

**Idea.** Where only summary fields are needed (head snapshot, re-org production), load a small payload envelope summary instead of the full envelope from disk on each head change.

**Impact.** Already landed; the only full get_payload_envelope in non-test code is the sync network_context serving path. Gloas only.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:1124`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1124) get_payload_envelope_summary for head snapshot
- [`beacon_node/beacon_chain/src/builder.rs:793`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L793) summary on startup
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5478`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5478) summary in block production
- [`beacon_node/beacon_chain/src/block_production/mod.rs:268`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L268) summary for re-org parent
- [`beacon_node/store/src/hot_cold_store.rs:703`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L703) summary stored separately from PayloadBody column

**Skeptic check.** Grepped all envelope loads in beacon_chain; head, startup, production and bid verification all use the summary. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#10178](https://github.com/sigp/lighthouse/pull/10178), [lighthouse#10187](https://github.com/sigp/lighthouse/pull/10187)

</details>


<a id="block_import-139"></a>
<details>
<summary><b>block_import-139</b> Synchronous block validation without async overhead — <i>n/a · low · S · latency</i></summary>

**Idea.** Make block validation code synchronous when it does no I/O, removing async/promise overhead per block.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:1657`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1657) block work runs via spawn_blocking

**Sources.** [lodestar@d93bdcf2b](https://github.com/ChainSafe/lodestar/commit/d93bdcf2b877)

</details>


<a id="block_import-140"></a>
<details>
<summary><b>block_import-140</b> Tree-backed blocks during state regeneration — <i>n/a · low · S · cpu</i></summary>

**Idea.** When replaying blocks for state regeneration, keep blocks in tree-backed form instead of converting them, and skip event handlers on replay.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:3202`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3202) process_chain_segment

**Sources.** [lodestar#2383](https://github.com/ChainSafe/lodestar/pull/2383)

</details>


<a id="block_import-141"></a>
<details>
<summary><b>block_import-141</b> Trigger envelope import once per arrival — <i>implemented · low · S · cpu</i></summary>

**Idea.** Trigger payload envelope processing once on arrival and await data availability with a single wait, instead of re-triggering on every data-column sidecar.

**Impact.** Each column only does a cache insert; envelope import runs once when the cache reports completeness. Gloas only.

**Best measured result.** "up to 128 times per slot" redundant calls removed; no timings (pr:lodestar#9223)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:3787`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L3787) envelope processing triggered on envelope arrival
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4150`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4150) Gloas columns go to pending_payload_cache.put_gossip_verified_data_columns
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4379`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4379) process_payload_envelope_availability imports only when the cache returns Available, else MissingComponents
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3463`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3463) is_block_data_imported early return for late columns

**Skeptic check.** The earlier evidence said column gossip has no envelope trigger; in fact it does call process_payload_envelope_availability, but the import runs only on the Available transition, so there is no per-column re-trigger. Verdict upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#9223](https://github.com/ChainSafe/lodestar/pull/9223)

</details>


<a id="block_import-142"></a>
<details>
<summary><b>block_import-142</b> Checkpoint sync from unfinalized state — <i>partial · medium · M · startup, sync</i></summary>

**Idea.** Allow checkpoint sync from a recent unfinalized state by treating it as the fork choice anchor, so a node can start and attest during long non-finality.

**Gap in Lighthouse.** The fake-finalized anchor exists (manual --checkpoint-state), but under long non-finality descendants of the anchor carry a real justified checkpoint older than the anchor epoch, so node_is_viable_for_head rejects them and the head sticks at the anchor until the chain justifies again. Prysm's PR clamps descendant justified/finalized checkpoints to the anchor; Lighthouse has no clamp. Also missing: a non-finalized StateId option on checkpoint-sync-url, status/range-sync handling when our fake finalized epoch is ahead of peers, and custody/backfill origin handling.

**Impact.** Lets a node resync and attest within minutes during long non-finality instead of failing to find a finalized checkpoint; no gain in normal mainnet operation.

**Best measured result.** node catches up and attests immediately from a 6-epoch-old unfinalized checkpoint (pr:prysm#17559)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_fork_choice_store.rs:169-174`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_fork_choice_store.rs#L169-L174) anchor epoch/root used as both justified and finalized regardless of the state's real finality
- [`beacon_node/beacon_chain/src/builder.rs:406-435`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L406-L435) weak_subjectivity_state accepts any state and advances it to an epoch boundary, no finality check
- [`beacon_node/client/src/builder.rs:437-441`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L437-L441) checkpoint-sync-url hardcodes StateId::Finalized
- [`beacon_node/src/cli.rs:1241-1258`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L1241-L1258) --checkpoint-state/--checkpoint-block accept a manual state (the only route to an unfinalized anchor)
- [`consensus/proto_array/src/proto_array.rs:2165-2167`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L2165-L2167) viability filter needs voting_source.epoch == store justified (= anchor) or within 2 epochs of current; no clamp of descendant checkpoints to the anchor

**Second check.** Beyond the earlier review, checked the fork choice store init (anchor forced as justified+finalized), the proto_array viability filter, and searched fork_choice/proto_array for any checkpoint clamp (none). The viability check means the manual-file path likely does not work under real non-finality, which strengthens the gap; the store-test WSS tests only cover anchors near finality.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [prysm#17559](https://github.com/OffchainLabs/prysm/pull/17559)

</details>


<a id="block_import-143"></a>
<details>
<summary><b>block_import-143</b> Backpressure on async block DB write queue — <i>n/a · high · memory</i></summary>

**Idea.** During sync, wait for free capacity in the async block/column write queue before enqueuing more, so queued data cannot grow without bound.

**Best measured result.** Supernode external memory spiked ~4.5GB to ~10GB causing OOM before fix (pr:lodestar#8885)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:4752`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4752) block and columns written synchronously via store.do_atomically_with_block_and_blobs_cache inside spawn_blocking
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4410`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4410) import_available_block awaits import, no unbounded write queue

**Sources.** [lodestar#8885](https://github.com/ChainSafe/lodestar/pull/8885)

</details>


<a id="block_import-144"></a>
<details>
<summary><b>block_import-144</b> Yield to scheduler between block imports — <i>n/a · low · S · latency, cpu, memory</i></summary>

**Idea.** Yield to the event loop/scheduler between block imports and after epoch processing in long import chains, so gossip, duties and state eviction are not starved.

**Impact.** None.

**Best measured result.** Resolved OOM crash loops on infra nodes (pr:lodestar#8925)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:1657`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1657) blocking work on dedicated threads
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3202`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3202) process_chain_segment

**Sources.** [lodestar@e8a7369da](https://github.com/ChainSafe/lodestar/commit/e8a7369da1b1), [lodestar#8925](https://github.com/ChainSafe/lodestar/pull/8925)

</details>


<a id="block_import-145"></a>
<details>
<summary><b>block_import-145</b> Import fetched block ranges as one chain segment call — <i>implemented · low · S · cpu, sync, latency</i></summary>

**Idea.** Hand a fetched range of blocks to the chain as a single segment import instead of importing blocks one at a time and awaiting per-block events, while the next range is fetched in parallel. The chain can then batch work across the segment.

**Impact.** Already batched; signatures are verified together for each segment.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:3202`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3202)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3300-3305`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3300-L3305)
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:641`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L641)

**Skeptic check.** Range sync and backfill give a whole batch to process_chain_segment, which verifies the segment's signatures in one batch (signature_verify_chain_segment). The sync manager downloads other batches at the same time.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@f6e35f5f6](https://github.com/ChainSafe/lodestar/commit/f6e35f5f63e9)

</details>


<a id="block_import-146"></a>
<details>
<summary><b>block_import-146</b> Detect default payloads without copying transactions — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Decide whether an execution payload is the default/empty one by comparing fixed fields and checking transaction-list emptiness by count only. This avoids materializing a full payload that copies every transaction.

**Impact.** Negligible; the check only runs when the parent has no execution, and it compares by reference.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/execution/payload.rs:322-332`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/execution/payload.rs#L322-L332)
- [`beacon_node/beacon_chain/src/execution_payload.rs:251`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/execution_payload.rs#L251)

**Skeptic check.** is_default_with_zero_roots compares the payload by reference against a default value. The default has empty lists that do not allocate, and the list equality checks length first, so no transactions are copied. Also, parent_has_execution short-circuits the check after the merge.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@24c563078](https://github.com/ChainSafe/lodestar/commit/24c563078894)

</details>


<a id="block_import-147"></a>
<details>
<summary><b>block_import-147</b> Delay-queue slightly early gossip blocks until slot start — <i>implemented · low · S · latency, bandwidth</i></summary>

**Idea.** Hold gossip-verified blocks that arrive within clock disparity of their slot in a delay queue and import them at slot start. Attestations for them then do not hit unknown-block handling and peers are not downscored, avoiding refetches.

**Impact.** Avoids refetching and downscoring for slightly early blocks.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1835-1880`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1835-L1880)
- [`beacon_node/beacon_chain/src/block_verification.rs:919-922`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L919-L922)
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:113`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L113)

**Skeptic check.** Gossip verification accepts blocks within the clock-disparity tolerance. If block_slot &gt; current_slot, the block is sent to the reprocess queue as EarlyBlock and imported at slot start. This is the lighthouse#2155 mechanism.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#2155](https://github.com/sigp/lighthouse/pull/2155)

</details>


<a id="block_import-148"></a>
<details>
<summary><b>block_import-148</b> Import quarantined children of head when synced ahead — <i>implemented · low · S · sync, latency</i></summary>

**Idea.** Run a periodic loop that, when the synced head is ahead of the local head, pops quarantined orphan or sidecarless blocks whose parent is the current head and imports them immediately. This avoids waiting on a new request or timer.

**Impact.** Children waiting on a parent are resumed as soon as the parent imports, with no periodic timer needed.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/mod.rs:586`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L586) continue_child_lookups resolves lookups awaiting the imported parent and continues their requests

**Skeptic check.** Verified that continue_child_lookups calls resolve_awaiting_parent and continue_requests on every lookup whose parent was just imported. The earlier evidence is right: this is the event-driven form of Nimbus's periodic orphan-pop loop and has the same effect.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus@2f9d44681](https://github.com/status-im/nimbus-eth2/commit/2f9d44681237)

</details>


<a id="block_import-149"></a>
<details>
<summary><b>block_import-149</b> Run independent post-block steps concurrently — <i>not · low · M · latency</i></summary>

**Idea.** Run the independent post-block steps, such as block operation DB processing and attestation processing, concurrently instead of sequentially. This shortens block import latency.

**Gap in Lighthouse.** import_block could overlap independent post-fork-choice work (cache updates, DB op preparation) on other threads.

**Impact.** Little independent work; one atomic DB batch. At most a few ms per block.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:4454`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4454) import_block is one synchronous function in spawn_blocking; steps run in sequence

**Sources.** [lodestar@f6725e314](https://github.com/ChainSafe/lodestar/commit/f6725e314827)

</details>


<a id="block_import-150"></a>
<details>
<summary><b>block_import-150</b> Remove always-on per-block state dumps — <i>implemented · low · S · disk, cpu</i></summary>

**Idea.** Do not serialise the block plus pre and post states to disk on every import. The dump writes huge volumes of data and adds SSZ serialisation work to the import path.

**Impact.** There are no always-on per-block state dumps on the import path.

**Best measured result.** None (pr:teku#3445)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:7751`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7751) chain_dump is a test/debug helper, not called on import
- [`beacon_node/beacon_chain/src/beacon_chain.rs:8237`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L8237) dump_as_dot is debug only

**Skeptic check.** A grep for dump in beacon_chain/src finds only chain_dump and dump_as_dot, which are debug helpers. Nothing serialises the pre or post state to disk per block, so the earlier verdict holds.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#3445](https://github.com/Consensys-Incorporated/teku/pull/3445)

</details>


<a id="block_import-151"></a>
<details>
<summary><b>block_import-151</b> Reuse resolved parent and lazily wrap quarantined blocks — <i>n/a · low · S · cpu</i></summary>

**Idea.** When re-queueing quarantined blocks after their parent is imported, pass the already-resolved parent reference instead of re-looking it up by root, and defer building the fork-wrapped block object until it is added to quarantine. This avoids redundant lookups and allocations.

**Impact.** Lighthouse has no Nimbus-style quarantine; design differs.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/mod.rs:586`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L586) lookups hold their own state; no orphan quarantine

**Sources.** [nimbus#7675](https://github.com/status-im/nimbus-eth2/pull/7675)

</details>


<a id="block_import-152"></a>
<details>
<summary><b>block_import-152</b> Check known blocks with a single map lookup — <i>n/a · low · S · cpu</i></summary>

**Idea.** When checking whether a block is already known, use one map access that returns the value instead of a contains check followed by a second lookup. The key is hashed once.

**Impact.** Nim-specific double-hash pattern; Rust uses get/entry APIs.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/mod.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs) lookups keyed by root in a map

**Sources.** [nimbus#926](https://github.com/status-im/nimbus-eth2/pull/926)

</details>


<a id="block_import-153"></a>
<details>
<summary><b>block_import-153</b> Skip duplicate check and DB rewrite when replaying at startup — <i>n/a · low · startup, disk, cpu</i></summary>

**Idea.** When replaying stored blocks at startup to rebuild the state cache and fork choice, skip the duplicate-block check and do not re-write blocks to the DB, replaying only blocks after the finalized block.

**Impact.** Nothing to gain: no startup block replay exists.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:692`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L692) load_fork_choice reads persisted fork choice from DB, no block replay at startup

**Sources.** [lodestar@8fd3f3790](https://github.com/ChainSafe/lodestar/commit/8fd3f379079c)

</details>


<a id="block_import-154"></a>
<details>
<summary><b>block_import-154</b> Skip attestation and signature work when replaying finalized blocks — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** When regenerating state by replaying already-finalized blocks, skip per-block side effects such as feeding attestations into fork choice and signature checks, since the blocks are already trusted.

**Impact.** State regeneration replays stored blocks with no signature checks and does not feed fork choice.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2565-2567`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2565-L2567) replay_blocks uses BlockReplayer with no_signature_verification and minimal_block_root_verification
- [`consensus/state_processing/src/block_replayer.rs:113`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/block_replayer.rs#L113) no_signature_verification sets BlockSignatureStrategy::NoVerification
- [`beacon_node/http_api/src/sync_committee_rewards.rs:69-72`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/sync_committee_rewards.rs#L69-L72) API replay also skips signatures

**Skeptic check.** Both BlockReplayer call sites outside tests (store regen and the API) disable signature verification. BlockReplayer only runs per_block_processing and never touches fork choice, so the earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@60c0b324e](https://github.com/ChainSafe/lodestar/commit/60c0b324ef4d)

</details>


<a id="block_import-155"></a>
<details>
<summary><b>block_import-155</b> Skip blob transaction decoding for versioned hashes — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Do not decode blob-carrying transactions during block import and gossip validation; treat transactions as opaque bytes and derive versioned hashes from the block KZG commitments, leaving the cross-check to the execution engine.

**Impact.** Normal gossip and import treat transactions as opaque and leave the cross-check to the EL.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engine_api/new_payload_request.rs:184-191`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/new_payload_request.rs#L184-L191) versioned_hashes come from blob_kzg_commitments via kzg_commitment_to_versioned_hash
- [`beacon_node/beacon_chain/src/execution_payload.rs:77-94`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/execution_payload.rs#L77-L94) transactions are decoded only for NotifyExecutionLayer::No with optimistic_finalized_sync
- [`beacon_node/execution_layer/src/versioned_hashes.rs:63-70`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/versioned_hashes.rs#L63-L70) beacon_tx_to_tx_envelope is reached only from verify_versioned_hashes

**Skeptic check.** Confirmed that TxEnvelope::decode is reached only through perform_optimistic_sync_verifications, which runs only when the EL is not notified during optimistic finalized sync, a path that has no EL to do the check. The earlier evidence is accurate.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#5569](https://github.com/ChainSafe/lodestar/pull/5569)

</details>


<a id="block_import-156"></a>
<details>
<summary><b>block_import-156</b> Skip verbose logging and rebroadcast for sync imports — <i>implemented · low · S · sync, cpu</i></summary>

**Idea.** Give the block import entry point options to skip verbose logging and gossip rebroadcast when importing blocks during initial sync, avoiding wasted work on bulk imports.

**Impact.** Sync imports do no gossip rebroadcast; logging cost is negligible.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:3329-3335`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3329-L3335) range-sync import passes BlockImportSource::RangeSync and a no-op publish closure
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3937`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3937) block_source parameter on process_block

**Skeptic check.** Verified that process_chain_segment imports each block with `|| Ok(())` as the publish function, so sync never rebroadcasts. Lighthouse logs per-block import at debug level, so the logging half of the idea does not matter.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#2113](https://github.com/OffchainLabs/prysm/pull/2113)

</details>


<a id="block_import-157"></a>
<details>
<summary><b>block_import-157</b> Skip execution block hash for empty pre-merge payloads — <i>implemented · low · S · cpu</i></summary>

**Idea.** Skip recomputing the execution block hash (keccak over the RLP header) for blocks whose payload is not an execution payload, such as pre-merge-transition blocks with empty payloads.

**Impact.** No keccak/RLP block hash is computed for payloads that are not execution-enabled.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/execution_payload.rs:58-63`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/execution_payload.rs#L58-L63) Gloas blocks get Irrelevant
- [`beacon_node/beacon_chain/src/execution_payload.rs:61`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/execution_payload.rs#L61),96-98 blocks without execution enabled get Irrelevant with no hash work
- [`beacon_node/beacon_chain/src/execution_payload.rs:77-94`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/execution_payload.rs#L77-L94) block hash is computed only in the optimistic-sync path

**Skeptic check.** The is_execution_enabled gate returns PayloadVerificationStatus::Irrelevant before any hash work, and on the normal path the EL computes the hash anyway. The earlier evidence is correct and the gain only ever mattered at the merge.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#4687](https://github.com/status-im/nimbus-eth2/pull/4687)

</details>


<a id="block_import-158"></a>
<details>
<summary><b>block_import-158</b> Skip data-availability wait when blobs leave block path — <i>implemented · low · S · latency</i></summary>

**Idea.** Skip the data-availability wait during block import on forks where blob availability is separated from the block path, so import does not block on DA and finishes sooner.

**Impact.** Gloas block import does not wait on data availability; DA moved to the payload envelope.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:3988-3991`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3988-L3991) Gloas blocks go to pending_payload_cache rather than data_availability_checker.put_pre_execution_block
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:871-873`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L871-L873) Gloas skips the MissingCustodyColumns check
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:936-945`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L936-L945) new_gloas builds an available block with NoData
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4150-4158`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4150-L4158) Gloas data columns feed payload-envelope availability, not block availability

**Skeptic check.** Verified that Gloas blocks skip the block-level DA checker and are made available with NoData. Their columns are routed to process_payload_envelope_availability, so the earlier evidence holds.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#16396](https://github.com/OffchainLabs/prysm/pull/16396)

</details>


