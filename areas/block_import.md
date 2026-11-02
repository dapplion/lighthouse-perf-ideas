# block_import

77 ideas: 9 not, 14 partial, 49 implemented, 5 n/a; 21 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

The area has 143 numbered ideas; the 66 ids missing here have not been checked against Lighthouse yet.

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [block_import-001](#block_import-001) **★** | Separate CPU-bound and IO-bound beacon processor worker pools | not | medium | M | cpu, latency |
| [block_import-002](#block_import-002) | Wait for data availability before entering serial import queue | implemented | medium | S | latency |
| [block_import-003](#block_import-003) | Send forkchoiceUpdated every sync-limit blocks during bulk sync | implemented | medium | S | sync |
| [block_import-004](#block_import-004) | Propagate gossip blocks/envelopes before state transition and EL verdict | implemented | high | S | latency |
| [block_import-005](#block_import-005) | Pre-advance head state to next slot and reuse it | implemented | high | S | latency, cpu |
| [block_import-006](#block_import-006) **★** | Set head first, persist block and checkpoints afterwards | partial | high | L | latency, disk |
| [block_import-007](#block_import-007) | Overlap EL calls with import work; Arc-shared blocks | implemented | medium | S | latency, cpu, memory |
| [block_import-009](#block_import-009) | Avoid copying or cloning blocks through queues and verification | implemented | medium | S | cpu, memory, latency |
| [block_import-010](#block_import-010) | Reuse held fork choice read lock in block verification | implemented | medium | S | cpu, latency |
| [block_import-014](#block_import-014) | Do not retain BeaconStates in long-lived tasks and channels | implemented | high | S | memory, latency |
| [block_import-015](#block_import-015) **★** | Send forkchoiceUpdated in background, publish head early | partial | medium | S | latency, cpu |
| [block_import-016](#block_import-016) | Run finalization migration and pruning after import in background | implemented | medium | S | latency |
| [block_import-017](#block_import-017) | Batch-verify all signatures of a chain segment | implemented | high | S | cpu, sync |
| [block_import-018](#block_import-018) | Rebuild participation flags tree once for overlapping attestations | implemented | medium | S | cpu |
| [block_import-019](#block_import-019) | Verify all block signatures in one batch including sync aggregate | implemented | high | S | cpu |
| [block_import-020](#block_import-020) **★** | Batch block, head and state DB writes during sync | partial | medium | M | sync, disk, latency, cpu |
| [block_import-023](#block_import-023) **★** | Blacklist descendants of known-bad blocks | partial | medium | S | cpu |
| [block_import-025](#block_import-025) **★** | Process gossip blocks on blocking executor, not async core | partial | high | S | latency, cpu |
| [block_import-026](#block_import-026) **★** | Bound pending and future block queues by count and bytes | partial | medium | S | memory |
| [block_import-027](#block_import-027) | Cap delayed execution payload envelope queue | implemented | medium |  | memory |
| [block_import-029](#block_import-029) | Compute base_reward_per_increment once per block | implemented | low |  | cpu |
| [block_import-033](#block_import-033) | Compute indexed attestations once per block and reuse | implemented | medium |  | cpu, latency, disk |
| [block_import-037](#block_import-037) **★** | Import chain segment with one pre-state lookup | partial | medium | M | cpu, sync |
| [block_import-039](#block_import-039) | Structural checks before pubkey collection and signature verification | implemented | medium |  | cpu |
| [block_import-042](#block_import-042) | Compute block root once and pass it through pipeline | implemented | medium |  | cpu, latency |
| [block_import-045](#block_import-045) | Run state defragmentation after block import | n/a | medium |  | latency |
| [block_import-046](#block_import-046) | Delay attestation production while head block imports | implemented | medium |  | latency |
| [block_import-050](#block_import-050) | Reject future-slot blocks early instead of queueing | implemented | medium |  | memory, disk, bandwidth |
| [block_import-052](#block_import-052) | Do not recompute an already known state root | implemented | medium |  | cpu |
| [block_import-053](#block_import-053) | Reject known, finalized or non-descendant blocks before state load | implemented | medium |  | cpu, memory, disk, latency, sync |
| [block_import-056](#block_import-056) | Deduplicate in-flight block imports across gossip and RPC | implemented | medium |  | cpu, disk, memory |
| [block_import-057](#block_import-057) | Size processor queues from active validator count | implemented | high | S | memory |
| [block_import-058](#block_import-058) | Produce light client updates eagerly after import | implemented | medium |  | cpu, latency |
| [block_import-059](#block_import-059) **★** | Emit head/block events right after head update | partial | medium | S | latency |
| [block_import-060](#block_import-060) **★** | Send fcU from in-memory head before block persisted | not | high | L | latency |
| [block_import-061](#block_import-061) **★** | Update head immediately after block state transition | partial | medium | M | latency, cpu |
| [block_import-062](#block_import-062) | Verify proposer signature before state transition and DA | implemented | medium | S | cpu |
| [block_import-063](#block_import-063) | Epoch-boundary metrics off block import path | not | low | S | latency, cpu |
| [block_import-068](#block_import-068) | Evict cached inputs of unimported repeat proposals | implemented | medium | S | memory |
| [block_import-069](#block_import-069) | Start block and payload verification before data availability completes | implemented | high |  | latency, cpu |
| [block_import-070](#block_import-070) | Faster justification and finalization checkpoint updates | implemented | medium | S | latency, cpu |
| [block_import-072](#block_import-072) | Finalized-descendant check via fork choice membership | implemented | medium | S | cpu, disk, latency |
| [block_import-073](#block_import-073) | Check block existence in fork choice before DB | implemented | medium | S | cpu, disk, latency |
| [block_import-074](#block_import-074) **★** | Import block once half of columns are available | partial | high | M | latency |
| [block_import-076](#block_import-076) | Use in-memory head state when parent is head | implemented | medium | S | latency, disk |
| [block_import-077](#block_import-077) | Update head once per slot while far behind | implemented | medium | S | cpu, sync |
| [block_import-081](#block_import-081) | Iterate validator tree list from index, not skip | implemented | low |  | cpu, latency |
| [block_import-082](#block_import-082) | Justification from progressively tracked balances | implemented | medium |  | cpu, latency |
| [block_import-083](#block_import-083) | Compute signed block header lazily | implemented | medium |  | cpu, latency |
| [block_import-084](#block_import-084) | Skip import of already-known blocks | implemented | medium |  | cpu, sync |
| [block_import-087](#block_import-087) **★** | Reject blocks with huge parent skip distance | not | medium | S | memory, disk |
| [block_import-088](#block_import-088) | Move parent state into import, no clone | implemented | medium |  | cpu, memory |
| [block_import-090](#block_import-090) **★** | Advance next-slot state immediately after head update | partial | medium | S | latency |
| [block_import-091](#block_import-091) **★** | Send proposer FCU before next-slot cache update | partial | medium | S | latency |
| [block_import-093](#block_import-093) | Query optimistic status once per batch tail | n/a | medium |  | cpu |
| [block_import-094](#block_import-094) | Run state transition concurrently with newPayload | implemented | high |  | latency |
| [block_import-095](#block_import-095) **★** | Persist block concurrently with verification | not | medium | M | latency, disk |
| [block_import-096](#block_import-096) **★** | Write blobs in parallel with fork choice write | not | medium | S | latency, disk |
| [block_import-097](#block_import-097) | Parallel attestation signature verification per block | not | low | M | cpu, latency |
| [block_import-098](#block_import-098) | Reuse in-hand state instead of DB refetch | implemented | low |  | disk, latency, cpu |
| [block_import-099](#block_import-099) **★** | Pause gossip intake while processing current block | not | medium | S | latency, cpu |
| [block_import-102](#block_import-102) | Point pubkey lookups for sync aggregate | implemented | medium | S | cpu, memory |
| [block_import-106](#block_import-106) | Precompute next epoch transition ahead of time | implemented | high |  | latency, cpu |
| [block_import-110](#block_import-110) | Apply proposer boost before DB write | implemented | medium | S | latency |
| [block_import-114](#block_import-114) | Skip proposer prep work during initial sync | implemented | medium | S | cpu, latency, sync |
| [block_import-115](#block_import-115) | Skip slot processing for payload attributes | implemented | medium | S | cpu, latency |
| [block_import-117](#block_import-117) | Retry DA-failed import on tracker completion | implemented | low |  | latency |
| [block_import-121](#block_import-121) **★** | Persist received SSZ bytes, no reserialization | not | medium | M | cpu, latency, memory |
| [block_import-122](#block_import-122) | Block root from header with body root | implemented | low |  | cpu, latency |
| [block_import-130](#block_import-130) | Skip indexed attestation build for trusted signatures | implemented | low | S | cpu, memory |
| [block_import-132](#block_import-132) | Do not re-verify already verified block signature | implemented | medium |  | cpu, latency |
| [block_import-133](#block_import-133) | Skip state rewind when parent state is current | n/a | low |  | cpu |
| [block_import-134](#block_import-134) | Wait for gossip sidecars only for recent slots | n/a | medium |  | latency, sync |
| [block_import-135](#block_import-135) | Bound reprocess queue capacity | implemented | medium |  | memory, latency |
| [block_import-136](#block_import-136) **★** | Validate block outside the fork choice lock | partial | high | M | latency, cpu |
| [block_import-142](#block_import-142) **★** | Checkpoint sync from unfinalized state | partial | medium | M | startup, sync |
| [block_import-143](#block_import-143) | Backpressure on async block DB write queue | n/a | high |  | memory |

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

**Sources.** [lighthouse#8661](https://github.com/sigp/lighthouse/pull/8661)

</details>


<a id="block_import-002"></a>
<details>
<summary><b>block_import-002</b> Wait for data availability before entering serial import queue — <i>implemented · medium · S · latency</i></summary>

**Idea.** Wait for the execution payload envelope's (or block's) data availability before taking a slot in the serial block import queue. A slow DA wait then does not block other queued imports behind it.

**Impact.** Nothing waits in a serial queue: blocks go to the DA checker cache and process_block returns MissingComponents; Gloas envelopes wait in the pending payload cache. Beacon processor workers are parallel, so no head-of-line blocking.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:4075`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4075)
- [`beacon_node/beacon_chain/src/pending_payload_cache/mod.rs:1`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/mod.rs#L1)

**Sources.** [lodestar#10485](https://github.com/ChainSafe/lodestar/pull/10485)

</details>


<a id="block_import-003"></a>
<details>
<summary><b>block_import-003</b> Send forkchoiceUpdated every sync-limit blocks during bulk sync — <i>implemented · medium · S · sync</i></summary>

**Idea.** During range sync, trigger a forkchoiceUpdated to the EL every sync-limit batch of imported blocks instead of on a large fixed interval (or per block). The EL can then advance and prune at a cadence matched to its own batch limit.

**Impact.** Range sync calls recompute_head once per processed batch (fcU per batch), not per block or on a large fixed interval; matching the EL limit is EL specific.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:207`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L207)
- [`beacon_node/beacon_chain/src/canonical_head.rs:781`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L781)

**Sources.** [caplin#10362](https://github.com/erigontech/erigon/pull/10362)

</details>


<a id="block_import-004"></a>
<details>
<summary><b>block_import-004</b> Propagate gossip blocks/envelopes before state transition and EL verdict — <i>implemented · high · S · latency</i></summary>

**Idea.** Accept and re-publish a gossip block or execution payload envelope right after the cheap spec gossip checks (proposer signature, equivocation), and run the state transition and EL verification after propagation. Propagation latency then does not include block processing time.

**Impact.** Already done: re-publish does not wait for state transition or EL verdict.

**Best measured result.** block_publishing_initiated +291ms before vs +3ms after; total 361ms -&gt; 315ms (pr:teku#8820)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1568`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1568) process_gossip_unverified_block runs verify_block_for_gossip only
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1634`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1634) propagate_validation_result Accept before process_gossip_verified_block (state transition, EL)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3406`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3406) gossip checks run via GossipVerifiedBlock::new

**Sources.** [caplin#25469](https://github.com/erigontech/erigon/pull/25469), [teku#8820](https://github.com/Consensys-Incorporated/teku/pull/8820), [prysm#2033](https://github.com/OffchainLabs/prysm/pull/2033)

</details>


<a id="block_import-005"></a>
<details>
<summary><b>block_import-005</b> Pre-advance head state to next slot and reuse it — <i>implemented · high · S · latency, cpu</i></summary>

**Idea.** After importing a block, use idle time in the slot to advance the head state through the next slot (and epoch) transition and cache it, then take the next block's pre-state from that cache instead of re-running slot/epoch processing on arrival.

**Impact.** Already done.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:126`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L126) advances head state at 3/4 slot
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:258`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L258) advance_head does per_slot_processing, builds committee caches, primes shuffling and proposer caches, put_state
- [`beacon_node/beacon_chain/src/block_verification.rs:2065`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L2065) parent pre-state via get_advanced_hot_state (state cache)

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

**Sources.** [lodestar#8784](https://github.com/ChainSafe/lodestar/pull/8784), [prysm#9651](https://github.com/OffchainLabs/prysm/pull/9651), [lighthouse#2547](https://github.com/sigp/lighthouse/pull/2547)

</details>


<a id="block_import-007"></a>
<details>
<summary><b>block_import-007</b> Overlap EL calls with import work; Arc-shared blocks — <i>implemented · medium · S · latency, cpu, memory</i></summary>

**Idea.** Make block import and fork choice async so EL calls overlap with other work (state transition vs newPayload, head update vs forkchoiceUpdated), and pass blocks between stages behind a shared pointer instead of cloning them per stage.

**Impact.** Payload verification (newPayload) is spawned as a task concurrent with state transition and awaited in into_executed_block; fcU is a spawned task; blocks are Arc&lt;SignedBeaconBlock&gt;.

**Best measured result.** avoids cloning blocks at least 2 times per block processing (pr:lighthouse#3244)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1564`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1564)
- [`beacon_node/beacon_chain/src/block_verification.rs:742`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L742)
- [`beacon_node/beacon_chain/src/canonical_head.rs:1296`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1296)

**Sources.** [lighthouse#3244](https://github.com/sigp/lighthouse/pull/3244)

</details>


<a id="block_import-009"></a>
<details>
<summary><b>block_import-009</b> Avoid copying or cloning blocks through queues and verification — <i>implemented · medium · S · cpu, memory, latency</i></summary>

**Idea.** Pass blocks and sidecars through the sync, gossip, clearance and import verification stages as one shared or owned object (reference, pointer or moved value) instead of copying, cloning or converting them at each step. This saves the memcpy and allocation of large blocks.

**Impact.** Blocks travel as Arc&lt;SignedBeaconBlock&gt; through gossip, sync and import; moved into AvailableExecutedBlock.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:742`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L742)
- [`beacon_node/beacon_chain/src/block_verification.rs:798`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L798)

**Sources.** [nimbus#2610](https://github.com/status-im/nimbus-eth2/pull/2610), [nimbus#7546](https://github.com/status-im/nimbus-eth2/pull/7546), [lighthouse@c278c08e3](https://github.com/sigp/lighthouse/commit/c278c08e34ee), [lighthouse#1448](https://github.com/sigp/lighthouse/pull/1448)

</details>


<a id="block_import-010"></a>
<details>
<summary><b>block_import-010</b> Reuse held fork choice read lock in block verification — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Pass an already-held fork choice read lock into block verification helpers instead of releasing it and re-acquiring it in each helper. This avoids lock contention and inconsistent views between steps.

**Gap in Lighthouse.** Minor: check_block_against_finalized_slot and is_parent_imported at ~1941-1950 re-take the read lock separately in the signature-verified path.

**Impact.** Gossip verification holds one read lock across helpers (passed by reference); remaining re-acquisitions are cheap read locks.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:970`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L970)
- [`beacon_node/beacon_chain/src/block_verification.rs:983`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L983)
- [`beacon_node/beacon_chain/src/block_verification.rs:1989`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1989)
- [`beacon_node/beacon_chain/src/block_verification.rs:1498`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1498)

**Sources.** [lighthouse#4978](https://github.com/sigp/lighthouse/pull/4978), [lighthouse#4688](https://github.com/sigp/lighthouse/pull/4688)

</details>


<a id="block_import-014"></a>
<details>
<summary><b>block_import-014</b> Do not retain BeaconStates in long-lived tasks and channels — <i>implemented · high · S · memory, latency</i></summary>

**Idea.** Do not keep BeaconState values in forkchoice-update arguments, background migrator channel messages or post-transition event handlers; send only roots or checkpoints and load what is needed. Old states are then freed instead of pinned in memory by slow or queued work.

**Impact.** Already done: no BeaconState pinned in migrator channel or fork choice updates.

**Best measured result.** Retained state memory 615MB to 77MB (pr:lodestar#2184)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/migrate.rs:135`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L135) FinalizationNotification holds roots and checkpoint only
- [`beacon_node/beacon_chain/src/canonical_head.rs:1717`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1717) process_finalization passes state root, comment says state reloaded from cache
- [`beacon_node/beacon_chain/src/canonical_head.rs:1720`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1720) persist fork choice stores no state

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

**Sources.** [prysm#16149](https://github.com/OffchainLabs/prysm/pull/16149), [nimbus#3842](https://github.com/status-im/nimbus-eth2/pull/3842), [nimbus#3880](https://github.com/status-im/nimbus-eth2/pull/3880), [caplin#25581](https://github.com/erigontech/erigon/pull/25581)

</details>


<a id="block_import-016"></a>
<details>
<summary><b>block_import-016</b> Run finalization migration and pruning after import in background — <i>implemented · medium · S · latency</i></summary>

**Idea.** Run hot-to-cold state migration, storage rebase and pruning on finalization in a background task (guarded against concurrent runs) after the block is imported and the head updated, not inline in block processing.

**Impact.** Hot-to-cold migration and blob pruning run on a dedicated background thread via a channel; after_finalization only persists fork choice and sends a message. Fork choice prune still runs inline under a write lock.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/migrate.rs:34`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L34)
- [`beacon_node/beacon_chain/src/migrate.rs:149`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L149)
- [`beacon_node/beacon_chain/src/canonical_head.rs:1725`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1725)
- [`beacon_node/beacon_chain/src/canonical_head.rs:1597`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1597)

**Sources.** [prysm#11501](https://github.com/OffchainLabs/prysm/pull/11501), [silver#363](https://github.com/gattaca-com/silver/pull/363)

</details>


<a id="block_import-017"></a>
<details>
<summary><b>block_import-017</b> Batch-verify all signatures of a chain segment — <i>implemented · high · S · cpu, sync</i></summary>

**Idea.** When importing a chain segment during sync (or a single block through the same pipeline), collect the signature sets of all its blocks into one batched BLS verification and mark the blocks signature-verified, instead of verifying per block. Carry gossip verification results to import so they are not redone.

**Impact.** Already done.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:671`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L671) signature_verify_chain_segment, one verifier for all blocks
- [`beacon_node/beacon_chain/src/block_verification.rs:719`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L719) include_all_signatures per block, single verify() at 724
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3300`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3300) run on blocking pool
- [`beacon_node/beacon_chain/src/block_verification.rs:1214`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1214) gossip result carried via SignatureVerifiedBlock

**Sources.** [prysm#7244](https://github.com/OffchainLabs/prysm/pull/7244), [lodestar@4f15d28b4](https://github.com/ChainSafe/lodestar/commit/4f15d28b457a), [lodestar#1966](https://github.com/ChainSafe/lodestar/pull/1966), [lighthouse#913](https://github.com/sigp/lighthouse/pull/913), [lodestar#4317](https://github.com/ChainSafe/lodestar/pull/4317)

</details>


<a id="block_import-018"></a>
<details>
<summary><b>block_import-018</b> Rebuild participation flags tree once for overlapping attestations — <i>implemented · medium · S · cpu</i></summary>

**Idea.** When many attestations in a block touch the same validators, apply all participation flag updates to a flat array and rebuild the participation list/tree once instead of updating each validator's leaf individually.

**Impact.** None left: per-validator get_mut/add_flag only writes to milhouse's flat pending-update map (VecMap), and the participation tree is rebuilt once in one with_updated_leaves pass when apply_pending_mutations runs before state hashing.

**Best measured result.** altair block processing 40% faster (pr:lodestar#3225)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/process_operations.rs:266`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L266)
- [`consensus/types/src/state/beacon_state.rs:2739`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2739)
- d67aabd/src/interface.rs:68
- d67aabd/src/interface.rs:86
- d67aabd/src/list.rs:30
- d67aabd/src/tree.rs:164
- [`consensus/types/src/state/beacon_state.rs:3071`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3071)
- [`consensus/types/src/state/beacon_state.rs:3852`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3852)

**Second check.** The earlier review missed milhouse's Interface layer. List::get_mut copies the value on write into a MaxMap&lt;VecMap&gt; update buffer and does not touch the tree. Interface::apply_updates then rebuilds the packed participation tree once for all attestations in the block, which is the mechanism Lodestar added in #3225.

**Sources.** [lodestar#3225](https://github.com/ChainSafe/lodestar/pull/3225)

</details>


<a id="block_import-019"></a>
<details>
<summary><b>block_import-019</b> Verify all block signatures in one batch including sync aggregate — <i>implemented · high · S · cpu</i></summary>

**Idea.** Collect every signature of a block (proposer, randao, attestations, slashings, exits, sync aggregate) into one set and verify it with a single multi-pairing batch check instead of one by one.

**Impact.** Already done.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/../consensus/state_processing/src/per_block_processing/block_signature_verifier.rs:151`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/../consensus/state_processing/src/per_block_processing/block_signature_verifier.rs#L151) include_all_signatures covers proposal, randao, slashings, attestations, exits, sync aggregate (line 181)
- [`beacon_node/../consensus/state_processing/src/per_block_processing/block_signature_verifier.rs:430`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/../consensus/state_processing/src/per_block_processing/block_signature_verifier.rs#L430) single verify of all sets

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

**Sources.** [prysm#5215](https://github.com/OffchainLabs/prysm/pull/5215), [prysm#9244](https://github.com/OffchainLabs/prysm/pull/9244), [prysm#6584](https://github.com/OffchainLabs/prysm/pull/6584), [prysm#6599](https://github.com/OffchainLabs/prysm/pull/6599), [prysm#4219](https://github.com/OffchainLabs/prysm/pull/4219)

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

**Sources.** [lodestar#7500](https://github.com/ChainSafe/lodestar/pull/7500)

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

**Sources.** [teku#11434](https://github.com/Consensys-Incorporated/teku/pull/11434), [nimbus#1564](https://github.com/status-im/nimbus-eth2/pull/1564), [teku#11435](https://github.com/Consensys-Incorporated/teku/pull/11435)

</details>


<a id="block_import-027"></a>
<details>
<summary><b>block_import-027</b> Cap delayed execution payload envelope queue — <i>implemented · medium · memory</i></summary>

**Idea.** Put a maximum size on the delayed queue of execution payload envelopes that wait for their block, with separate limits for gossip and requested envelopes, and evict the highest-slot envelope (or reject) when full.

**Impact.** Already done.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:81`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L81) MAXIMUM_QUEUED_ENVELOPES=16
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:724`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L724),780 early-envelope and awaiting-block envelope queues each reject when full (dropping the new one)

**Sources.** [grandine@ac21ead8f](https://github.com/grandinetech/grandine/commit/ac21ead8f363), [grandine@29750218c](https://github.com/grandinetech/grandine/commit/29750218c4a4), [grandine#931](https://github.com/grandinetech/grandine/pull/931)

</details>


<a id="block_import-029"></a>
<details>
<summary><b>block_import-029</b> Compute base_reward_per_increment once per block — <i>implemented · low · cpu</i></summary>

**Idea.** Compute base_reward_per_increment (integer sqrt of total active balance) once per block or epoch and pass it into attestation processing instead of recomputing it per attestation.

**Impact.** Per-attestation sqrt is already avoided; at most one isqrt per block in sync committee processing, negligible.

**Best measured result.** non-epoch slot with block 851 ms -&gt; 70 ms avg, 60k validators (pr:nimbus#2681)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/epoch_cache.rs:96`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/epoch_cache.rs#L96),111 BaseRewardPerIncrement computed once per epoch cache build and per-validator base rewards cached
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:280`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L280),421 attestation processing uses state.get_base_reward(index) cache lookup
- [`consensus/state_processing/src/per_block_processing/altair/sync_committee.rs:93`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/altair/sync_committee.rs#L93) one integer_sqrt per block

**Sources.** [nimbus#2681](https://github.com/status-im/nimbus-eth2/pull/2681)

</details>


<a id="block_import-033"></a>
<details>
<summary><b>block_import-033</b> Compute indexed attestations once per block and reuse — <i>implemented · medium · cpu, latency, disk</i></summary>

**Idea.** Compute a block's indexed attestations once during signature verification and keep them in the block-processing context for per-block processing, fork choice and slasher instead of recomputing them. Also run payload verification before advancing/writing the pre-state and defer non-essential work until after the early attester cache is primed.

**Impact.** Already done.

**Best measured result.** eager state writes were adding ~20-30ms before payload verification; parallel attestation observation saves 5-10ms (pr:lighthouse#3696)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/consensus_context.rs:30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/consensus_context.rs#L30),161 ConsensusContext.indexed_attestations cache, get_indexed_attestation
- [`consensus/state_processing/src/per_block_processing/block_signature_verifier.rs:297`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/block_signature_verifier.rs#L297) sig verification fills the cache
- [`beacon_node/beacon_chain/src/block_verification.rs:1764`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1764) fork choice reuses cached indexed attestations; beacon_chain.rs:4987,5054,5094 validator monitor, observation and slasher reuse them
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4454-4500`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4454-L4500) import_block: only pre-fork-choice work before attestable, early attester cache primed before DB write at 4751

**Sources.** [lighthouse#3696](https://github.com/sigp/lighthouse/pull/3696), [lodestar#8637](https://github.com/ChainSafe/lodestar/pull/8637)

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

**Sources.** [lodestar@1b3a33391](https://github.com/ChainSafe/lodestar/commit/1b3a333912fa)

</details>


<a id="block_import-039"></a>
<details>
<summary><b>block_import-039</b> Structural checks before pubkey collection and signature verification — <i>implemented · medium · cpu</i></summary>

**Idea.** Run cheap structural checks (for example attestation bits equal proof participants, bitfield lengths) before collecting public keys and verifying signatures, so malformed blocks are rejected without crypto work.

**Impact.** Already done.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/block_signature_verifier.rs:168-181`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/block_signature_verifier.rs#L168-L181) include_* collect sets and return errors before verify() at line 430
- [`consensus/state_processing/src/common/get_attesting_indices.rs:25`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/get_attesting_indices.rs#L25) bitlist.len() != committee.len() rejects malformed bitfields while collecting
- [`beacon_node/beacon_chain/src/block_verification.rs:721-724`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L721-L724) include_all_signatures, then one batch verify

**Sources.** [ethlambda#202](https://github.com/lambdaclass/ethlambda/pull/202)

</details>


<a id="block_import-042"></a>
<details>
<summary><b>block_import-042</b> Compute block root once and pass it through pipeline — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** Compute the block's hash_tree_root (or a tree-backed form with cached roots) once on receipt and pass it through gossip verification, signature verification, import, sync, observed-proposer and API paths instead of rehashing the block at each stage.

**Impact.** Already done.

**Best measured result.** block root ~10ms; ~30ms of duplicates against 300-400ms seen-to-imported (pr:lighthouse#3590)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1965`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1965) get_block_root computes once (timed)
- [`beacon_node/beacon_chain/src/block_verification_types.rs:28`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification_types.rs#L28) RpcBlock/RangeSyncBlock::new carry block_root alongside the block
- [`beacon_node/network/src/sync/network_context/requests/blocks_by_root.rs:39`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/requests/blocks_by_root.rs#L39) root computed once on receipt in sync
- [`beacon_node/http_api/src/publish_blocks.rs:167`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L167) reuses supplied block_root

**Sources.** [prysm#14609](https://github.com/OffchainLabs/prysm/pull/14609), [lodestar@eb2b0deb5](https://github.com/ChainSafe/lodestar/commit/eb2b0deb5f5c), [lighthouse#3590](https://github.com/sigp/lighthouse/pull/3590), [lodestar#9795](https://github.com/ChainSafe/lodestar/pull/9795), [prysm#5785](https://github.com/OffchainLabs/prysm/pull/5785), [nimbus#3048](https://github.com/status-im/nimbus-eth2/pull/3048), [ethlambda#172](https://github.com/lambdaclass/ethlambda/pull/172)

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
<summary><b>block_import-046</b> Delay attestation production while head block imports — <i>implemented · medium · latency</i></summary>

**Idea.** When a block that will become head is being imported, make attestation production wait (bounded, e.g. 1.5s) on a condvar until it is imported, so attestations vote for it instead of its parent.

**Impact.** Already avoids attesting to the parent: the early attester cache gives the same effect as the closed condvar PR (#2575) without any wait. Nothing to gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2025`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2025) produce_unaggregated_attestation tries early_attester_cache first
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4572`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4572) early_attester_cache.add_head_block right after fork choice picks the new head, before DB write

**Sources.** [lighthouse#2575](https://github.com/sigp/lighthouse/pull/2575)

</details>


<a id="block_import-050"></a>
<details>
<summary><b>block_import-050</b> Reject future-slot blocks early instead of queueing — <i>implemented · medium · memory, disk, bandwidth</i></summary>

**Idea.** Drop blocks whose slot is beyond the clock-disparity bound before parent lookup, instead of queueing them or storing them as pending, so fabricated future blocks cost no memory, disk writes or parent fetches.

**Impact.** Fabricated future blocks cost no parent fetch, disk write or state load. Only blocks within the clock-disparity tolerance are held, in a bounded reprocess queue (work_reprocessing_queue.rs:659).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:915-926`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L915-L926) gossip FutureSlot with maximum_gossip_clock_disparity tolerance, before parent/state load
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3943-3948`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3943-L3948) process_block rejects future blocks before block_times_cache write
- [`beacon_node/beacon_chain/src/block_verification.rs:1926`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1926) check_block_relevancy FutureSlot (RPC/segment path)
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1716`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1716) FutureSlot -&gt; Ignore + peer penalty

**Sources.** [lodestar#3210](https://github.com/ChainSafe/lodestar/pull/3210), [ethlambda#324](https://github.com/lambdaclass/ethlambda/pull/324)

</details>


<a id="block_import-052"></a>
<details>
<summary><b>block_import-052</b> Do not recompute an already known state root — <i>implemented · medium · cpu</i></summary>

**Idea.** Avoid a redundant hash_tree_root of the BeaconState in block import/production by reusing a state root that is already known, and do not compute and compare the post-state root a second time once the state transition validated it.

**Impact.** State root is computed once per import, then reused from the verified block. update_tree_hash_cache is also incremental (milhouse), so a repeat would be cheap anyway.

**Best measured result.** 16 to 12 state roots per run; 0.05s each (pr:nimbus#933)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1731`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1731) post-state root computed once via update_tree_hash_cache, compared to block.state_root() at 1741
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4752`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4752) import stores state under block.state_root(), no recompute
- [`beacon_node/beacon_chain/src/beacon_chain.rs:6553`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6553) production computes the state root once
- [`beacon_node/beacon_chain/src/block_verification.rs:1039-1045`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1039-L1045),2088-2099 parent state root reused when known

**Sources.** [nimbus#933](https://github.com/status-im/nimbus-eth2/pull/933), [prysm#3114](https://github.com/OffchainLabs/prysm/pull/3114)

</details>


<a id="block_import-053"></a>
<details>
<summary><b>block_import-053</b> Reject known, finalized or non-descendant blocks before state load — <i>implemented · medium · cpu, memory, disk, latency, sync</i></summary>

**Idea.** Before loading the parent block and state, or running state transition in segment/queue import, reject blocks that are already known, at or below the finalized slot, or not descended from finality. Stale blocks then cost no DB reads, state loads or full validation.

**Impact.** Stale blocks are rejected from fork-choice memory without DB reads or state loads.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1404`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1404),1448,1529 check_block_relevancy runs before parent/state load
- [`beacon_node/beacon_chain/src/block_verification.rs:1820`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1820),1915-1960 finalized-slot and fork-choice contains_block checks
- [`beacon_node/beacon_chain/src/block_verification.rs:960-985`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L960-L985) gossip path: known and finalized-descendant checks before loading the parent
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3068`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3068) filter_chain_segment drops known/finalized blocks from range segments before signature verification

**Sources.** [prysm#679](https://github.com/OffchainLabs/prysm/pull/679), [lighthouse#2289](https://github.com/sigp/lighthouse/pull/2289), [prysm#13089](https://github.com/OffchainLabs/prysm/pull/13089), [lighthouse#2474](https://github.com/sigp/lighthouse/pull/2474), [lighthouse#1041](https://github.com/sigp/lighthouse/pull/1041), [lodestar@81bbf5b96](https://github.com/ChainSafe/lodestar/commit/81bbf5b96fd2)

</details>


<a id="block_import-056"></a>
<details>
<summary><b>block_import-056</b> Deduplicate in-flight block imports across gossip and RPC — <i>implemented · medium · cpu, disk, memory</i></summary>

**Idea.** Track block roots that are being processed or were recently imported, shared by gossip, RPC and pending-block retry paths, and make a second arrival skip, wait for or share the in-flight result instead of processing it again.

**Impact.** Gossip and RPC share one in-flight set; a second arrival is dropped (it does not wait for or share the result), which avoids duplicate processing.

**Best measured result.** spin loop ~25 iterations/ms until 8GB OOM before fix (pr:lodestar#9501)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:181-210`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L181-L210) DuplicateCache with RAII handle
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1561`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1561) gossip check_and_insert
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:121`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L121) lookup/RPC path uses the same cache (network_beacon_processor/mod.rs:71)
- [`beacon_node/beacon_chain/src/block_verification.rs:1095`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1095) DuplicateImportStatusUnknown from observed-producer cache

**Sources.** [lighthouse#2647](https://github.com/sigp/lighthouse/pull/2647), [prysm#12905](https://github.com/OffchainLabs/prysm/pull/12905), [lighthouse#4179](https://github.com/sigp/lighthouse/pull/4179), [lodestar#9501](https://github.com/ChainSafe/lodestar/pull/9501)

</details>


<a id="block_import-057"></a>
<details>
<summary><b>block_import-057</b> Size processor queues from active validator count — <i>implemented · high · S · memory</i></summary>

**Idea.** Size beacon processor work queues (especially attestation queues) from the active validator count at startup, so they do not overflow and drop work on large networks.

**Impact.** Already done.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_queue.rs:335`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_queue.rs#L335) BeaconProcessorQueueLengths::from_state sizes attestation_queue from active validator count / slots_per_epoch (110% overprovision, line 11)
- [`beacon_node/client/src/builder.rs:757`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L757) used at startup

**Sources.** [lighthouse#5573](https://github.com/sigp/lighthouse/pull/5573)

</details>


<a id="block_import-058"></a>
<details>
<summary><b>block_import-058</b> Produce light client updates eagerly after import — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** After each imported block, compute light client updates on a separate thread from the in-memory state and cache the proofs, so each update is computed once and serving queries needs no block replay.

**Impact.** Updates are computed once per block off the import thread, gated on enable_light_client_server and recency.

**Best measured result.** each update computed at most once (pr:lighthouse#4969)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:4787`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4787) cache_state_data caches proofs from the in-memory post-state at import
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5178-5190`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5178-L5190) sends (parent_root, slot, sync_aggregate) over light_client_server_tx to a separate producer task
- [`beacon_node/beacon_chain/src/light_client_server_cache.rs:80`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_server_cache.rs#L80) recompute_and_cache_updates; prev_block_cache keeps state data

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

**Sources.** [prysm#8412](https://github.com/OffchainLabs/prysm/pull/8412), [prysm#9224](https://github.com/OffchainLabs/prysm/pull/9224)

</details>


<a id="block_import-062"></a>
<details>
<summary><b>block_import-062</b> Verify proposer signature before state transition and DA — <i>implemented · medium · S · cpu</i></summary>

**Idea.** Verify the block proposer signature before the full state transition and before starting data availability checks, so blocks with bad signatures are rejected cheaply and the fault is attributed to that block copy.

**Impact.** None needed.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1056-1072`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1056-L1072) GossipVerifiedBlock::new verifies proposer signature before state transition
- [`beacon_node/beacon_chain/src/block_verification.rs:1285`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1285) from_gossip_verified_block uses include_all_signatures_except_proposal (no re-verify)
- [`beacon_node/beacon_chain/src/block_verification.rs:1212-1245`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1212-L1245) SignatureVerifiedBlock re-verifies proposer alone on batch failure to attribute fault
- [`beacon_node/beacon_chain/src/block_verification.rs:3980`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L3980) (beacon_chain.rs:3980-3995) put_pre_execution_block only after into_execution_pending_block (signatures) succeeded

**Sources.** [teku#11401](https://github.com/Consensys-Incorporated/teku/pull/11401)

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


<a id="block_import-068"></a>
<details>
<summary><b>block_import-068</b> Evict cached inputs of unimported repeat proposals — <i>implemented · medium · S · memory</i></summary>

**Idea.** Remove the block input and payload envelope cache entries of repeat proposals that are not imported, with single-entry removal, so an equivocating proposer cannot make the node keep unlimited full blocks until finalization.

**Gap in Lighthouse.** Lighthouse never seeds caches with a repeat proposal before gossip checks (equivocating block fails with Slashable first), and the DA cache is an LRU of 32, so unbounded retention to finalization does not occur. Minor residual: data columns/blobs of an unimported equivocating root may sit in the LRU until evicted.

**Impact.** Memory already bounded; nothing to gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1088-1097`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1088-L1097) observe_proposal returns Slashable/Duplicate before any caching
- beacon_node/beacon_chain/src/gossip_methods.rs:1677 BlockError::Slashable handled, block dropped
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3991`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3991) DA checker/pending_payload_cache only fed after verification
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3983`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3983) pending_payload_cache.remove_block on verification failure
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:53`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L53) OVERFLOW_LRU_CAPACITY=32 bounds the cache

**Sources.** [lodestar#10083](https://github.com/ChainSafe/lodestar/pull/10083)

</details>


<a id="block_import-069"></a>
<details>
<summary><b>block_import-069</b> Start block and payload verification before data availability completes — <i>implemented · high · latency, cpu</i></summary>

**Idea.** Start state transition, signature checks and EL newPayload as soon as the block arrives, in parallel with waiting for blobs/columns, and only await data availability before final import.

**Best measured result.** column wait can take 2+ s of the 4 s window (pr:nimbus#8561)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:3961-4022`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3961-L4022) process_block runs into_execution_pending_block, newPayload, then only checks availability
- [`beacon_node/beacon_chain/src/block_verification.rs:1535-1570`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1535-L1570) newPayload spawned on arrival, state transition proceeds in parallel
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4096`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4096) check_block_availability_and_import puts executed block in DA checker; waits for columns only after execution

**Sources.** [caplin#12924](https://github.com/erigontech/erigon/pull/12924), [nimbus#8561](https://github.com/status-im/nimbus-eth2/pull/8561), [silver#230](https://github.com/gattaca-com/silver/pull/230), [lodestar#6087](https://github.com/ChainSafe/lodestar/pull/6087)

</details>


<a id="block_import-070"></a>
<details>
<summary><b>block_import-070</b> Faster justification and finalization checkpoint updates — <i>implemented · medium · S · latency, cpu</i></summary>

**Idea.** Speed up the justification and finalization processing done when updating checkpoints during block import (avoid recomputation over the full state).

**Impact.** None needed.

**Best measured result.** Mainnet block import ~30-40 ms faster (pr:grandine#584)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/altair/justification_and_finalization.rs:9`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/altair/justification_and_finalization.rs#L9) uses progressive_balances_cache totals, no validator loop
- [`consensus/fork_choice/src/fork_choice.rs:934-971`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L934-L971) on_block reuses parent's unrealized checkpoints, skipping J&amp;F when possible

**Sources.** [grandine#584](https://github.com/grandinetech/grandine/pull/584)

</details>


<a id="block_import-072"></a>
<details>
<summary><b>block_import-072</b> Finalized-descendant check via fork choice membership — <i>implemented · medium · S · cpu, disk, latency</i></summary>

**Idea.** Check that a block descends from the finalized checkpoint by looking up its parent in the in-memory fork choice (which only holds finalized-compatible nodes) instead of loading blocks from the DB or walking ancestry.

**Impact.** None needed.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1857`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1857) check_block_is_finalized_checkpoint_or_descendant uses fork_choice.is_finalized_checkpoint_or_descendant(parent_root)
- [`consensus/fork_choice/src/fork_choice.rs:1829`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1829) proto_array lookup; DB is only hit on the failure path to choose the error
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4506`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4506) called under the fork choice write lock in import_block

**Sources.** [prysm#12040](https://github.com/OffchainLabs/prysm/pull/12040), [prysm#10905](https://github.com/OffchainLabs/prysm/pull/10905), [prysm#12041](https://github.com/OffchainLabs/prysm/pull/12041), [prysm#12046](https://github.com/OffchainLabs/prysm/pull/12046)

</details>


<a id="block_import-073"></a>
<details>
<summary><b>block_import-073</b> Check block existence in fork choice before DB — <i>implemented · medium · S · cpu, disk, latency</i></summary>

**Idea.** For duplicate and parent-known checks during import, query the in-memory fork choice store first and only fall back to the DB, making the common check synchronous and far cheaper.

**Impact.** None needed.

**Best measured result.** HasBlock DB 381 ns/op vs fork choice 40.0 ns/op (pr:prysm#4821)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1948-1954`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1948-L1954) check_block_relevancy uses fork_choice contains_block for duplicates
- [`beacon_node/beacon_chain/src/block_verification.rs:2023-2026`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L2023-L2026) load_parent checks is_parent_imported in fork choice first
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4501`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4501) import_block re-checks contains_block under upgradable lock

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

**Sources.** [teku#10365](https://github.com/Consensys-Incorporated/teku/pull/10365), [grandine@39bab2591](https://github.com/grandinetech/grandine/commit/39bab2591f87)

</details>


<a id="block_import-076"></a>
<details>
<summary><b>block_import-076</b> Use in-memory head state when parent is head — <i>implemented · medium · S · latency, disk</i></summary>

**Idea.** When fetching the pre-state for block or attestation processing, check whether the parent/target root is the current head and use the in-memory head state. This skips a DB read and state deserialization on the common path.

**Impact.** None needed. The in-memory state cache (keyed by block root, includes head and recent advanced states) serves the parent state without DB read or deserialization.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:2063-2065`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L2063-L2065) load_parent calls store.get_advanced_hot_state
- [`beacon_node/store/src/hot_cold_store.rs:1130`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1130),1196 state_cache lookup by block_root before any DB load
- [`beacon_node/store/src/state_cache.rs:316`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L316) get_by_block_root

**Sources.** [prysm#4830](https://github.com/OffchainLabs/prysm/pull/4830), [prysm#4853](https://github.com/OffchainLabs/prysm/pull/4853), [prysm#4972](https://github.com/OffchainLabs/prysm/pull/4972), [prysm#4974](https://github.com/OffchainLabs/prysm/pull/4974)

</details>


<a id="block_import-077"></a>
<details>
<summary><b>block_import-077</b> Update head once per slot while far behind — <i>implemented · medium · S · cpu, sync</i></summary>

**Idea.** During sync, when the node is more than a few epochs behind, do not run the fork choice head update after every imported block; update the head once per slot instead. This removes repeated head computation per block.

**Impact.** None needed; sync does at most one head update per batch and skips get_head for old blocks.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:185`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L185),4554 get_head per block only if block within 4 slots of current slot (EARLY_ATTESTER_CACHE_HISTORIC_SLOTS)
- beacon_node/beacon_chain/src/sync_methods.rs:638-660 process_blocks: recompute_head_at_current_slot once per chain segment, not per block

**Sources.** [teku#2780](https://github.com/Consensys-Incorporated/teku/pull/2780)

</details>


<a id="block_import-081"></a>
<details>
<summary><b>block_import-081</b> Iterate validator tree list from index, not skip — <i>implemented · low · cpu, latency</i></summary>

**Idea.** In per-block validator monitoring or any scan that starts at a validator index, use an iterator that seeks to the index (iter_from) on the persistent tree list instead of skip(n), which walks the whole prefix.

**Impact.** Already done (lighthouse#9995): median import avoided ~160 ms on huge registries; for mainnet ~1M validators it removes a full-prefix tree walk per block.

**Best measured result.** Median import_block 199.87 ms to 38.47 ms (second window 191.60 to 40.56) with 2.36M validators (pr:lighthouse#9995)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_monitor.rs:490`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_monitor.rs#L490) state.validators().iter_from(start_index) with comment about not walking the registry

**Sources.** [lighthouse#9995](https://github.com/sigp/lighthouse/pull/9995)

</details>


<a id="block_import-082"></a>
<details>
<summary><b>block_import-082</b> Justification from progressively tracked balances — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** Track target/participation balances incrementally as attestations are processed and use them for justification/unrealized checkpoint computation at block import, instead of scanning the validator set.

**Impact.** Already done; unrealized justification reads cached flag balances instead of scanning validators.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fork_choice/src/fork_choice.rs:949`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L949) unrealized checkpoints at import use progressive balances cache
- [`consensus/fork_choice/src/fork_choice.rs:954`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L954) altair process_justification_and_finalization(state)
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:161`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L161) initialize_progressive_balances_cache

**Sources.** [lodestar#4326](https://github.com/ChainSafe/lodestar/pull/4326)

</details>


<a id="block_import-083"></a>
<details>
<summary><b>block_import-083</b> Compute signed block header lazily — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** On the block import hot path, do not compute the signed block header (which hashes the full body including payload) up front; compute it only on the slashing/error path that needs it. This removes a full block hash per import.

**Impact.** Done by PR 8446; the remaining header build in gossip new() is for the block root and is cheap.

**Best measured result.** shaves 10-20ms off pre-newPayload delay and every block import (pr:lighthouse#8446)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1253`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1253) header built inside map_err only
- block_verification.rs:1365 and 1376 same lazy pattern
- block_verification.rs:886 gossip path still builds header for cheap root

**Sources.** [lighthouse#8446](https://github.com/sigp/lighthouse/pull/8446)

</details>


<a id="block_import-084"></a>
<details>
<summary><b>block_import-084</b> Skip import of already-known blocks — <i>implemented · medium · cpu, sync</i></summary>

**Idea.** At the start of block processing or requeue, check whether the block root is already in fork choice (or the live chain index) and return early, so duplicates from gossip and sync never rerun state transition or pre-state regeneration. The check must survive state pruning.

**Impact.** Duplicates are dropped before state transition; already in place.

**Best measured result.** Loop consumed 100% CPU for hours and ~3.5GB of logs per node (pr:ethlambda#234)

**Evidence (Lighthouse @ 928b61e719).**

- block_verification.rs:1948 contains_block on fork choice -&gt; DuplicateFullyImported
- block_verification.rs:972 gossip duplicate check
- block_verification.rs:1095 DuplicateImportStatusUnknown

**Sources.** [ethlambda#234](https://github.com/lambdaclass/ethlambda/pull/234), [prysm#5850](https://github.com/OffchainLabs/prysm/pull/5850), [teku#1214](https://github.com/Consensys-Incorporated/teku/pull/1214), [lighthouse#4214](https://github.com/sigp/lighthouse/pull/4214)

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

**Sources.** [lighthouse#1530](https://github.com/sigp/lighthouse/pull/1530)

</details>


<a id="block_import-088"></a>
<details>
<summary><b>block_import-088</b> Move parent state into import, no clone — <i>implemented · medium · cpu, memory</i></summary>

**Idea.** Pass the parent pre-state into the block import function by value instead of cloning it, and load/deserialize it once for both signature verification and state transition.

**Impact.** Parent state is loaded once and moved; the only clone is on the rare proposer-cache miss.

**Best measured result.** "avoids the previous .clone() — minor perf win" (pr:ethlambda#157)

**Evidence (Lighthouse @ 928b61e719).**

- block_verification.rs:1579 let mut state = parent.pre_state (moved, no clone)
- block_verification.rs:1198 and 1270 signature check borrows &amp;mut parent.pre_state
- block_verification.rs:1047 clone only on proposer cache miss in gossip

**Sources.** [ethlambda#157](https://github.com/lambdaclass/ethlambda/pull/157)

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

**Sources.** [prysm#12469](https://github.com/OffchainLabs/prysm/pull/12469)

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
<summary><b>block_import-094</b> Run state transition concurrently with newPayload — <i>implemented · high · latency</i></summary>

**Idea.** During block import, send engine_newPayload and run the consensus state transition concurrently instead of sequentially, so import costs the max of the two, not the sum.

**Best measured result.** shed about 200ms on a normal slot (pr:prysm#12590)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1535-1570`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1535-L1570) PayloadNotifier future spawned as task before state advance
- [`beacon_node/beacon_chain/src/block_verification.rs:1639-1710`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1639-L1710) per_slot_processing and per_block_processing run while newPayload is in flight
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4101-4115`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4101-L4115) into_executed_block awaits the handle afterwards

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
<summary><b>block_import-098</b> Reuse in-hand state instead of DB refetch — <i>implemented · low · disk, latency, cpu</i></summary>

**Idea.** Load the beacon state once per block and pass the reference (pre- and post-state) to later steps such as fork choice vote processing, instead of re-reading state from the database.

**Impact.** Nothing; import path already passes the post-state by reference.

**Best measured result.** 3 DB fetches reduced (pr:prysm#1257)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:4533`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4533) fork_choice.on_block receives &amp;state already in hand
- [`beacon_node/beacon_chain/src/block_verification.rs:2063`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L2063) parent state from get_advanced_hot_state (cache), not refetched later

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

**Sources.** [lodestar#5458](https://github.com/ChainSafe/lodestar/pull/5458)

</details>


<a id="block_import-102"></a>
<details>
<summary><b>block_import-102</b> Point pubkey lookups for sync aggregate — <i>implemented · medium · S · cpu, memory</i></summary>

**Idea.** When processing a SyncAggregate, look up the 512 committee pubkeys individually in the state pubkey index instead of building a map of all validator pubkeys.

**Best measured result.** 190k-entry map and 190k lookups reduced to 512 lookups (pr:prysm#9177)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:1753`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1753) get_sync_committee_indices does 512 pubkey_cache().get() lookups
- [`consensus/types/src/state/beacon_state.rs:2979`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2979) update_pubkey_cache is incremental and persistent on the state (only inserts new validators)
- [`consensus/state_processing/src/per_block_processing/signature_sets.rs:794`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/signature_sets.rs#L794) sync aggregate sig set uses committee pubkeys + bits, decompressor from ValidatorPubkeyCache

**Sources.** [prysm#9177](https://github.com/OffchainLabs/prysm/pull/9177)

</details>


<a id="block_import-106"></a>
<details>
<summary><b>block_import-106</b> Precompute next epoch transition ahead of time — <i>implemented · high · latency, cpu</i></summary>

**Idea.** Near the end of an epoch, run the epoch transition for the head state on a background worker and cache the advanced state keyed by (epoch, parent root), so the first block of the epoch reuses it instead of running process_epoch inline.

**Best measured result.** Epoch-start blocks take ~1.5 s vs ~0.58 s for an ordinary block (the cost targeted); no after-number given (pr:ethlambda#652)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:1-14`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L1-L14) advances head state a slot in the tail of each slot
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:258`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L258) advance_head, runs per_slot_processing incl. epoch processing
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:455`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L455) advanced state stored with put_state (state cache) for block verification

**Sources.** [ethlambda#652](https://github.com/lambdaclass/ethlambda/pull/652)

</details>


<a id="block_import-110"></a>
<details>
<summary><b>block_import-110</b> Apply proposer boost before DB write — <i>implemented · medium · S · latency</i></summary>

**Idea.** On block import, set proposer boost in fork choice before persisting the block and state, so the boost does not wait for the DB write.

**Best measured result.** ~100ms to set boost, ~50ms of it DB save; about 50% less wait (pr:prysm#10509)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:4533`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4533) fork_choice.on_block (sets proposer boost in store) runs in the pre-attestable section
- [`consensus/fork_choice/src/fork_choice.rs:647`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L647) proposer_boost_root used
- beacon_chain.rs:4733-4756 DB write comes after, with comment 'DO NOT add extra processing' at 4463

**Sources.** [prysm#10509](https://github.com/OffchainLabs/prysm/pull/10509)

</details>


<a id="block_import-114"></a>
<details>
<summary><b>block_import-114</b> Skip proposer prep work during initial sync — <i>implemented · medium · S · cpu, latency, sync</i></summary>

**Idea.** While the node is initial-syncing (detected by head age or sync state), skip payload-attribute computation, late-block tasks and attestation-triggered head updates, since no FCU with attributes is sent.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:6757-6769`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6757-L6769) prepare_beacon_proposer returns early when head_slot + sync_tolerance_epochs*slots &lt; current_slot
- beacon_chain.rs:6732 early exit when no proposer has registered with the EL
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:207`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L207) skips recompute_head/prepare when best_slot + 256 &lt; current_slot
- [`beacon_node/beacon_chain/src/canonical_head.rs:1931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1931) payload attributes only via prepare_beacon_proposer

**Sources.** [prysm#16721](https://github.com/OffchainLabs/prysm/pull/16721), [prysm#13479](https://github.com/OffchainLabs/prysm/pull/13479), [prysm#12526](https://github.com/OffchainLabs/prysm/pull/12526)

</details>


<a id="block_import-115"></a>
<details>
<summary><b>block_import-115</b> Skip slot processing for payload attributes — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** When computing payload attributes, skip process_slots and state copying unless a local validator proposes the next slot (proposer lookahead is in state).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5286`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5286) get_pre_payload_attributes takes proposer from beacon_proposer_cache/head state lookahead with no process_slots
- beacon_chain.rs:6795 withdrawals (state advance) computed only after the check that the proposer is a local registered validator (compute_withdrawals_for_payload_attributes at 5393)

**Sources.** [prysm#16168](https://github.com/OffchainLabs/prysm/pull/16168)

</details>


<a id="block_import-117"></a>
<details>
<summary><b>block_import-117</b> Retry DA-failed import on tracker completion — <i>implemented · low · latency</i></summary>

**Idea.** When a block import fails for missing data, attach the retry to the blob/column tracker completion future instead of a polling retry pool, so it retries immediately.

**Impact.** Nothing; the DA cache completes and imports the pending block when the final blob/column is added.

**Best measured result.** no delay, no polling (pr:teku#8157)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker.rs:322-452`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L322-L452) put_* calls return Available once last component arrives
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3345`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3345),4055 MissingComponents handled by import when components land, no polling

**Sources.** [teku#8157](https://github.com/Consensys-Incorporated/teku/pull/8157)

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

**Sources.** [lodestar#5573](https://github.com/ChainSafe/lodestar/pull/5573), [lodestar#5426](https://github.com/ChainSafe/lodestar/pull/5426), [lodestar#7391](https://github.com/ChainSafe/lodestar/pull/7391)

</details>


<a id="block_import-122"></a>
<details>
<summary><b>block_import-122</b> Block root from header with body root — <i>implemented · low · cpu, latency</i></summary>

**Idea.** In gossip verification compute the block root from the signed block header built with the body root, instead of hashing the full block again.

**Impact.** Nothing; already done (PR 5003 still in place).

**Best measured result.** ~10ms average block root on mainnet; header should take microseconds (pr:lighthouse#5003)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:890`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L890) get_block_header_root(&amp;header) used in gossip verification
- [`beacon_node/beacon_chain/src/block_verification.rs:1975`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1975) get_block_header_root

**Sources.** [lighthouse#5003](https://github.com/sigp/lighthouse/pull/5003)

</details>


<a id="block_import-130"></a>
<details>
<summary><b>block_import-130</b> Skip indexed attestation build for trusted signatures — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** When replaying blocks with already-verified signatures, skip building indexed attestations and copying pubkeys used only for signature verification.

**Gap in Lighthouse.** Only a small leftover: is_valid_indexed_attestation still allocates attesting_indices_to_vec and does the sort check when signatures are already verified.

**Impact.** Pubkey work is already skipped; leftover is a tiny Vec alloc per attestation, negligible on a mainnet node.

**Best measured result.** removes is_valid_indexed_attestation from performance benchmarks when replaying blocks (commit:nimbus@5ca10d3de263)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/is_valid_indexed_attestation.rs:50`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/is_valid_indexed_attestation.rs#L50) signature set and pubkey lookup only when verify_signatures is true
- [`consensus/state_processing/src/per_block_processing/verify_attestation.rs:92`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/verify_attestation.rs#L92) indexed attestation built once, cached in ConsensusContext, and needed anyway for participation updates (process_operations.rs:250)

**Sources.** [nimbus@5ca10d3de](https://github.com/status-im/nimbus-eth2/commit/5ca10d3de263)

</details>


<a id="block_import-132"></a>
<details>
<summary><b>block_import-132</b> Do not re-verify already verified block signature — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** Skip re-verifying the proposer or builder signature in block/envelope processing when gossip validation already verified it, avoiding an extra BLS check and full block hash.

**Impact.** Already avoids the second proposer/builder BLS check and block re-hash on gossip path. Range-sync envelopes still verify (import.rs:436), which is needed since they were not gossip-verified.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/payload_envelope_verification/execution_pending_envelope.rs:83`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/execution_pending_envelope.rs#L83) envelope processed with VerifySignatures::False, comment says gossip already verified
- [`beacon_node/beacon_chain/src/block_verification.rs:1285`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1285) include_all_signatures_except_proposal skips the proposal signature
- [`beacon_node/beacon_chain/src/block_verification.rs:12`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L12) module docs: do not re-verify proposal signature or re-hash

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
<summary><b>block_import-135</b> Bound reprocess queue capacity — <i>implemented · medium · memory, latency</i></summary>

**Idea.** Cap the reprocessing queue and its channel below the main work channel capacity so late blocks and attestations cannot build unbounded work.

**Impact.** Reprocess channels bounded at 75% of the work channel, plus per-type caps, as in lighthouse#3239.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:91`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L91) DEFAULT_MAX_SCHEDULED_WORK_QUEUE_LEN = 3/4 of main queue len
- [`beacon_node/beacon_processor/src/lib.rs:770-773`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L770-L773) both reprocess channels use max_scheduled_work_queue_len
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:78-90`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L78-L90) per-kind caps (16 blocks, 16384 attestations)

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

**Sources.** [teku#4751](https://github.com/Consensys-Incorporated/teku/pull/4751), [prysm#12589](https://github.com/OffchainLabs/prysm/pull/12589), [caplin#25332](https://github.com/erigontech/erigon/pull/25332)

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


