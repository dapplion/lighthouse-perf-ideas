# range_sync

146 ideas: 20 not, 26 partial, 68 implemented, 32 n/a; 18 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [range_sync-001](#range_sync-001) | Send forkchoiceUpdated once per sync batch | implemented | medium | S | latency, sync |
| [range_sync-002](#range_sync-002) | Pipeline batch download concurrently with import | implemented | low | S | latency, sync |
| [range_sync-003](#range_sync-003) | Self rate-limit outgoing by-range requests per peer | implemented | low | S | bandwidth, latency, sync |
| [range_sync-004](#range_sync-004) | Keep block processing off the sync and network loop | implemented | medium | S | latency, sync |
| [range_sync-005](#range_sync-005) **★** | Filter sync peers by earliest available slot | partial | medium | S | bandwidth, sync |
| [range_sync-006](#range_sync-006) | Skip range requests for already known or queued blocks | implemented | low | S | sync, bandwidth |
| [range_sync-007](#range_sync-007) **★** | Clip sidecar requests to DA window and fork | partial | medium | S | bandwidth, sync |
| [range_sync-008](#range_sync-008) | Choose range or by-root sync by distance | implemented | low | S | bandwidth, sync |
| [range_sync-009](#range_sync-009) | Start sync from optimistic head, not validated head | implemented | low | S | sync, bandwidth |
| [range_sync-010](#range_sync-010) | Back off or exit sync when no peer ahead | n/a | low | S | cpu |
| [range_sync-011](#range_sync-011) | Batch-verify signatures across a whole sync segment | implemented | low | S | cpu, sync |
| [range_sync-012](#range_sync-012) | Couple block and sidecar downloads per batch | implemented | low | S | bandwidth, cpu, latency, sync |
| [range_sync-013](#range_sync-013) | Request sidecars only for blocks with commitments | implemented | low | S | bandwidth, sync |
| [range_sync-014](#range_sync-014) | Fetch batch columns by root after blocks arrive | implemented | medium | S | sync, bandwidth |
| [range_sync-015](#range_sync-015) | Build block batch when columns already present | n/a | low | S | sync |
| [range_sync-016](#range_sync-016) | Request blocks in ranged batches, not singly | implemented | low | S | sync, latency, bandwidth |
| [range_sync-017](#range_sync-017) | Use larger blocks-per-request batch size | not | low | M | sync, latency |
| [range_sync-018](#range_sync-018) | Cap items per outgoing by-range request | implemented | low | S | memory, sync |
| [range_sync-019](#range_sync-019) | Bound download lookahead ahead of processing | implemented | low | S | bandwidth, memory |
| [range_sync-020](#range_sync-020) | Cap concurrent in-flight sync requests per peer | partial | low | S | bandwidth, latency, sync |
| [range_sync-021](#range_sync-021) | Temporarily blacklist failed sync chains | implemented | low | S | sync, cpu |
| [range_sync-022](#range_sync-022) | Cancel in-flight import on batch abort | not | low | M | cpu, sync |
| [range_sync-023](#range_sync-023) | Cancel leaked futures and tasks in sync loops | n/a | low |  | memory, cpu |
| [range_sync-024](#range_sync-024) | Timeout envelope waits and cap per-batch retries | implemented | low | S | sync |
| [range_sync-025](#range_sync-025) | Raise batch retry limit under rate limiting | n/a | low |  | sync |
| [range_sync-026](#range_sync-026) | Remove sync request tracking entries on every exit | implemented | medium | S | memory |
| [range_sync-027](#range_sync-027) | Collect metrics only for active sync chains | n/a | low |  | memory |
| [range_sync-028](#range_sync-028) | Release batch block buffers when batch completes | n/a | low |  | memory |
| [range_sync-029](#range_sync-029) | Limit parallel head-chain syncs | implemented | medium | S | bandwidth, sync |
| [range_sync-030](#range_sync-030) | Cap sync peers with a fresh-peer pool | implemented | low | S | sync |
| [range_sync-031](#range_sync-031) | Skip per-slot tick work while syncing | implemented | medium | S | cpu, sync |
| [range_sync-032](#range_sync-032) | Checkpoint sync with background backfill | implemented | high | S | sync, startup |
| [range_sync-033](#range_sync-033) | Light client provides optimistic head for sync | n/a | low | L | sync |
| [range_sync-034](#range_sync-034) | Backward sync from trusted head with cheap verification | n/a | low | L | cpu, sync |
| [range_sync-035](#range_sync-035) **★** | Sync columns from minimal covering peer set | not | medium | S | bandwidth, sync |
| [range_sync-036](#range_sync-036) **★** | Prefer narrow-custody peers for column requests | partial | medium | S | bandwidth, sync |
| [range_sync-037](#range_sync-037) | Do not block startup on sync | implemented | low | S | startup |
| [range_sync-038](#range_sync-038) **★** | Do not advance sync on unverified empty responses | partial | medium | S | sync, bandwidth |
| [range_sync-039](#range_sync-039) | Ignore gossip blocks as sync triggers while range syncing | implemented | low | S | sync, cpu, bandwidth |
| [range_sync-040](#range_sync-040) | Extend forward batches to local head | implemented | low | S | sync |
| [range_sync-041](#range_sync-041) | Correct finalized range sync target slot | implemented | low | S | sync, bandwidth |
| [range_sync-042](#range_sync-042) | Do not start sync before genesis | n/a | low | S | cpu |
| [range_sync-043](#range_sync-043) | Locate boundary batch by reverse scan | partial | low | S | cpu |
| [range_sync-044](#range_sync-044) | Shorten sync state machine hot path | n/a | low | S | cpu |
| [range_sync-045](#range_sync-045) | Cheap batch attempt hashing | implemented | low | S | cpu, memory |
| [range_sync-046](#range_sync-046) | Downscore peers with timed-out sync requests | implemented | low | S | sync |
| [range_sync-047](#range_sync-047) | Do not redial poorly performing sync peers | implemented | low | S | sync |
| [range_sync-048](#range_sync-048) | Stop requesting columns at peer request cap | partial | low | S | bandwidth |
| [range_sync-049](#range_sync-049) | Check batch is parent-linked chain before import | implemented | medium | S | cpu, sync |
| [range_sync-050](#range_sync-050) | Race duplicate range requests across peers | not | low | M | sync, latency |
| [range_sync-051](#range_sync-051) | Cap concurrent downloads per block root | implemented | low | S | bandwidth |
| [range_sync-052](#range_sync-052) | Reject wrong fork digest before decoding | partial | low | S | cpu |
| [range_sync-053](#range_sync-053) | Never span fork boundaries in a sync batch | implemented | low | S | sync |
| [range_sync-054](#range_sync-054) | Align sync batches to epoch boundaries | implemented | medium | S | cpu |
| [range_sync-055](#range_sync-055) | Evict cached inputs after peer-caused batch failure | implemented | low | S | sync, cpu |
| [range_sync-056](#range_sync-056) | Keep latest state in memory during initial sync | implemented | high | S | disk, sync |
| [range_sync-057](#range_sync-057) | Download ranges from several peers in parallel | implemented | medium | S | bandwidth, latency, sync |
| [range_sync-058](#range_sync-058) | Disable periodic peer status updates while syncing | implemented | low | S | bandwidth, cpu |
| [range_sync-059](#range_sync-059) **★** | Find common ancestor instead of restarting at finalized | partial | medium | M | sync, bandwidth |
| [range_sync-060](#range_sync-060) | Include non-canonical heads in common ancestor search | not | low | M | sync, bandwidth |
| [range_sync-061](#range_sync-061) | Rank finalized sync peers by finalized epoch | partial | low | S | sync |
| [range_sync-062](#range_sync-062) | Start range requests after blocks already held | not | low | S | bandwidth, cpu, sync |
| [range_sync-063](#range_sync-063) | Silently skip pre-finalization blocks in range sync | implemented | low | S | sync |
| [range_sync-064](#range_sync-064) | Skip already-imported blocks before batch processing | implemented | low | S | cpu, disk, sync |
| [range_sync-065](#range_sync-065) | Handle switching target chain without stalling | n/a | low | S | sync |
| [range_sync-066](#range_sync-066) | Progress sync on local chain without remote | n/a | low | S | sync |
| [range_sync-067](#range_sync-067) | Ordered async delivery of sync status events | n/a | low | S | latency |
| [range_sync-068](#range_sync-068) | Yield between synced block imports | n/a | low |  | latency |
| [range_sync-069](#range_sync-069) | Race peers for block access lists alongside bodies | n/a | low |  | sync, latency |
| [range_sync-070](#range_sync-070) **★** | Save synced blocks to DB concurrently | not | medium | L | sync, cpu, disk |
| [range_sync-071](#range_sync-071) **★** | Verify execution payload in parallel with block | not | medium | M | latency, sync, cpu |
| [range_sync-072](#range_sync-072) | Pause range sync while execution layer offline | implemented | medium | S | cpu, sync |
| [range_sync-073](#range_sync-073) | Do not count non-fault failures against batch retries | partial | low | S | sync, bandwidth |
| [range_sync-074](#range_sync-074) **★** | Score sync peers by observed throughput | not | high | M | sync, bandwidth |
| [range_sync-075](#range_sync-075) **★** | Weighted round robin on peer rate-limit capacity | partial | medium | M | sync, bandwidth |
| [range_sync-076](#range_sync-076) | Randomize sync peer selection | implemented | low | S | sync, bandwidth |
| [range_sync-077](#range_sync-077) | Pick failover peer without scanning peer list | not | low | S | cpu |
| [range_sync-078](#range_sync-078) | Wait for full custody subnet coverage before column batches | implemented | medium | S | sync, bandwidth |
| [range_sync-079](#range_sync-079) | Pool peers per chain and load-balance batches | implemented | medium | S | sync, bandwidth |
| [range_sync-080](#range_sync-080) | Drop sync peers that return too few blocks | partial | low | M | sync |
| [range_sync-081](#range_sync-081) **★** | Keep partial column responses, retry only missing columns | partial | medium | M | sync, bandwidth |
| [range_sync-082](#range_sync-082) | Per-peer locks around fetch rate limiter | n/a | low |  | cpu, latency |
| [range_sync-083](#range_sync-083) | Re-trigger sync on a periodic timer | implemented | low | S | sync, latency |
| [range_sync-084](#range_sync-084) | Peer-unbound worker pool keeps requests pipelined | implemented | medium | S | sync, bandwidth |
| [range_sync-085](#range_sync-085) | Buffer gossip blocks to disk while syncing | not | low | L | sync, bandwidth |
| [range_sync-086](#range_sync-086) | Materialize cached blocks before processing | n/a | low |  | cpu |
| [range_sync-087](#range_sync-087) | Probe peers for range sync support | not | low | M | sync, bandwidth |
| [range_sync-088](#range_sync-088) | Prune sync block buffer below finalized | n/a | medium |  | memory |
| [range_sync-089](#range_sync-089) | Purge stale head chains after one completes | partial | low | S | sync, bandwidth |
| [range_sync-090](#range_sync-090) | Drain queued messages before expiring batches | n/a | low | S | cpu, sync |
| [range_sync-091](#range_sync-091) | Range sync batch state machine with indexed lookups | implemented | low | S | cpu, sync |
| [range_sync-092](#range_sync-092) **★** | Narrow redownload range on batch retry | partial | medium | S | sync, bandwidth |
| [range_sync-093](#range_sync-093) | One-slot buffer between fetchers and processor | implemented | low | S | memory, bandwidth |
| [range_sync-094](#range_sync-094) | Same retarget threshold after sync failure | implemented | low | S | sync |
| [range_sync-095](#range_sync-095) | Switch sync target only for more peers | implemented | low | S | sync, bandwidth |
| [range_sync-096](#range_sync-096) | Remove disconnected peer from all sync chains | implemented | low | S | sync |
| [range_sync-097](#range_sync-097) | Start sync without waiting for peers | implemented | low | S | sync, startup, latency |
| [range_sync-098](#range_sync-098) | No watchdog that resets slow sync workers | n/a | low | S | sync, bandwidth |
| [range_sync-099](#range_sync-099) | Cheap slot check before DB lookup | implemented | low | S | disk, cpu |
| [range_sync-100](#range_sync-100) | Move fork-choice weight to new head during sync | implemented | low | M | sync |
| [range_sync-101](#range_sync-101) | Retry failed batch with a different peer | implemented | medium | S | sync, bandwidth |
| [range_sync-102](#range_sync-102) | Process synced blocks sequentially | implemented | low | S | cpu, memory |
| [range_sync-103](#range_sync-103) | Sync from one best peer with large chunks | implemented | low | S | bandwidth, sync |
| [range_sync-104](#range_sync-104) | Avoid state copies in sync path | n/a | low |  | memory, cpu |
| [range_sync-105](#range_sync-105) | Skip attestation processing for finalized sync blocks | not | low | M | cpu, disk, sync |
| [range_sync-106](#range_sync-106) | Skip fork choice and head updates during catch-up | partial | low | M | cpu, sync |
| [range_sync-107](#range_sync-107) | Exclude payload-absent slots from column requests and DA | implemented | low | S | sync, bandwidth, cpu |
| [range_sync-108](#range_sync-108) | Skip importing orphaned payload envelopes | partial | low | M | cpu, latency |
| [range_sync-109](#range_sync-109) | No blob wait outside DA window | implemented | medium | S | latency, sync |
| [range_sync-110](#range_sync-110) | Skip sidecars already on disk | not | low | M | bandwidth, cpu |
| [range_sync-111](#range_sync-111) **★** | Serve stored SSZ bytes directly for by-range | not | medium | L | cpu, memory |
| [range_sync-112](#range_sync-112) | Skip long runs of empty slots quickly | not | low | M | sync, bandwidth |
| [range_sync-113](#range_sync-113) | Skip local replay when far behind peers | n/a | low |  | startup, sync |
| [range_sync-114](#range_sync-114) | No extra delays in light client sync | n/a | low |  | sync, latency |
| [range_sync-115](#range_sync-115) | Skip newPayload for finalized sync blocks | implemented | high | S | latency, sync |
| [range_sync-116](#range_sync-116) | Skip snapshot downloads below retained range | n/a | low |  | disk, bandwidth, startup |
| [range_sync-117](#range_sync-117) | Bootstrap from downloaded beacon snapshots | not | low | L | startup, sync |
| [range_sync-118](#range_sync-118) | Avoid importing orphaned blocks in initial sync | n/a | low |  | sync, cpu |
| [range_sync-119](#range_sync-119) | Skip finalized sync phase when already there | n/a | low |  | startup, sync |
| [range_sync-120](#range_sync-120) **★** | Skip block verification up to trusted finality | partial | medium | M | cpu, sync |
| [range_sync-121](#range_sync-121) | Bound column retry for withheld origin payloads | n/a | low | S | cpu |
| [range_sync-122](#range_sync-122) | Use smaller range sync batches | implemented | medium | S | sync, bandwidth |
| [range_sync-123](#range_sync-123) | Speculative background sync of forks | partial | low | M | sync |
| [range_sync-124](#range_sync-124) | Stop reading response at requested count | implemented | low | S | bandwidth, sync |
| [range_sync-125](#range_sync-125) | Wake backpressured workers on reset | n/a | low | S | sync |
| [range_sync-126](#range_sync-126) | Sync from finalized state, not head state | implemented | low | S | startup, cpu |
| [range_sync-127](#range_sync-127) | Sync engine rewrite | n/a | low | S | sync |
| [range_sync-128](#range_sync-128) | Query peer heads less often, concurrently | implemented | low | S | bandwidth, cpu |
| [range_sync-129](#range_sync-129) | Keep synced blocks tree-backed | n/a | low | S | cpu, sync |
| [range_sync-130](#range_sync-130) | Do not pre-filter peers for column sync | implemented | low | S | sync |
| [range_sync-131](#range_sync-131) **★** | Larger download lookahead window | partial | medium | S | sync, latency |
| [range_sync-132](#range_sync-132) **★** | Unified peer-driven block and sidecar fetch loop | not | medium | L | sync, bandwidth |
| [range_sync-133](#range_sync-133) **★** | Verify proposer signature first in range sync | not | medium | S | cpu |
| [range_sync-134](#range_sync-134) | Wait for in-flight import before retargeting | n/a | low | S | sync |
| [range_sync-135](#range_sync-135) **★** | Compute custody peer pool once per retry round | partial | medium | M | cpu, bandwidth |
| [range_sync-136](#range_sync-136) | Ban peers that serve invalid blocks in sync | implemented | low | S | sync, bandwidth |
| [range_sync-137](#range_sync-137) | Abort rest of batch after first invalid block | implemented | low | S | cpu, sync |
| [range_sync-138](#range_sync-138) | Use only sync peers whose head is ahead of ours | implemented | low | S | sync |
| [range_sync-139](#range_sync-139) | Minimal block-processing path for synced blocks | implemented | low | S | sync, cpu, bandwidth |
| [range_sync-140](#range_sync-140) | Verify batch data availability in parallel with execution | partial | low | M | latency, sync |
| [range_sync-141](#range_sync-141) | Await data availability once per payload segment | implemented | low | S | sync |
| [range_sync-142](#range_sync-142) | Rank sync peers by request-outcome score | partial | low | M | sync |
| [range_sync-143](#range_sync-143) | Persist snapshot download state to skip re-downloads | n/a | low |  | startup, sync, bandwidth |
| [range_sync-144](#range_sync-144) | Remember roots of blocks that failed processing | partial | low | S | cpu, sync |
| [range_sync-145](#range_sync-145) | Keep re-statusing peers in their sync head chains | not | low | S | sync, cpu |
| [range_sync-146](#range_sync-146) | Gate validator duties on sync status at startup | partial | low | S | sync, startup, cpu |

★ actionable. Click an id for the full record.

## Ideas

<a id="range_sync-001"></a>
<details>
<summary><b>range_sync-001</b> Send forkchoiceUpdated once per sync batch — <i>implemented · medium · S · latency, sync</i></summary>

**Idea.** During range/initial sync, do not send engine forkchoiceUpdated after every imported block; send it once per batch (for its last block, in the background) or once at the end of sync. This cuts EL round trips during bulk import.

**Impact.** One fcU per range-sync batch, sent from a spawned task.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:632-662`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L632-L662) process_blocks calls recompute_head_at_current_slot once after process_chain_segment
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3207-3260`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3207-L3260) process_chain_segment loop has no head recompute
- [`beacon_node/beacon_chain/src/canonical_head.rs:1890-1920`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1890-L1920) fcU sent from a spawn_handle task inside recompute_head

**Skeptic check.** Verified that range and backfill batches import all their blocks before one recompute_head. The earlier impact said the fcU is awaited, but the EL call runs in a spawned task.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#17109](https://github.com/OffchainLabs/prysm/pull/17109), [prysm#10520](https://github.com/OffchainLabs/prysm/pull/10520), [prysm#16199](https://github.com/OffchainLabs/prysm/pull/16199)

</details>


<a id="range_sync-002"></a>
<details>
<summary><b>range_sync-002</b> Pipeline batch download concurrently with import — <i>implemented · low · S · latency, sync</i></summary>

**Idea.** Decouple range-sync block fetching from block processing with a queue or batch state machine, so the next batches download from peers while earlier batches are imported in order. Network wait and import overlap instead of alternating.

**Impact.** Downloads of up to 5 batches overlap in-order import.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain.rs:33`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L33) BATCH_BUFFER_SIZE = 5
- [`beacon_node/network/src/sync/range_sync/chain.rs:1124-1215`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L1124-L1215) request_batches/include_next_batch download ahead of processing_target
- [`beacon_node/network/src/sync/range_sync/chain.rs:384`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L384) process_completed_batches sends batches to the beacon processor in order
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:632`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L632) processing runs on the beacon processor, separate from sync networking

**Skeptic check.** The range-sync state machine downloads ahead while earlier batches are processed on the beacon processor. Upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#5148](https://github.com/OffchainLabs/prysm/pull/5148), [prysm#4978](https://github.com/OffchainLabs/prysm/pull/4978), [lodestar#1961](https://github.com/ChainSafe/lodestar/pull/1961), [prysm#4931](https://github.com/OffchainLabs/prysm/pull/4931), [prysm#5096](https://github.com/OffchainLabs/prysm/pull/5096), [prysm#5064](https://github.com/OffchainLabs/prysm/pull/5064), [lodestar#1685](https://github.com/ChainSafe/lodestar/pull/1685), [lodestar@927005cf8](https://github.com/ChainSafe/lodestar/commit/927005cf899c), [prysm#4965](https://github.com/OffchainLabs/prysm/pull/4965), [prysm#5286](https://github.com/OffchainLabs/prysm/pull/5286)

</details>


<a id="range_sync-003"></a>
<details>
<summary><b>range_sync-003</b> Self rate-limit outgoing by-range requests per peer — <i>implemented · low · S · bandwidth, latency, sync</i></summary>

**Idea.** Throttle outgoing blocks/blobs-by-range requests to each peer to the quota that peer enforces, counting cost the way the responder does (slots times max blobs, adjusted for empty slots), and schedule a retry exactly when the quota replenishes. Requests are not rejected, penalised or disconnected, and the node does not wait longer than needed.

**Impact.** Already throttles to the peer's (Lighthouse-default) quota and retries exactly when tokens refill. The only difference from teku#8984 is that tokens are not refunded for empty slots, but the Lighthouse responder does not refund them either.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/self_limiter.rs:83-123`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/self_limiter.rs#L83-L123) allows() queues per (peer,protocol) and inserts into DelayQueue at the limiter's wait_time
- [`beacon_node/lighthouse_network/src/rpc/self_limiter.rs:155-178`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/self_limiter.rs#L155-L178) TooSoon(wait_time) re-queues instead of sending; TooLarge is sent anyway
- [`beacon_node/lighthouse_network/src/rpc/rate_limiter.rs:388-399`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/rate_limiter.rs#L388-L399) tokens = request.max_responses(), the same cost function the inbound limiter charges
- [`beacon_node/lighthouse_network/src/rpc/protocol.rs:853-866`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/protocol.rs#L853-L866) BlocksByRange=count, BlobsByRange=max_blobs_requested, DataColumnsByRange=max_requested
- [`beacon_node/src/config.rs:1500-1508`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/config.rs#L1500-L1508) self limiter on by default with default quotas
- [`beacon_node/lighthouse_network/src/rpc/config.rs:122-155`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/config.rs#L122-L155) shared default quota table

**Skeptic check.** Checked that SelfRateLimiter is enabled by default (beacon_node/src/config.rs:1502) and charges the same max_responses cost as the inbound limiter. The earlier evidence was correct. Its listed gap (no empty-slot adjustment) matches how a Lighthouse responder counts cost, so it is not a defect.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#8984](https://github.com/Consensys-Incorporated/teku/pull/8984), [teku#6604](https://github.com/Consensys-Incorporated/teku/pull/6604), [prysm#4637](https://github.com/OffchainLabs/prysm/pull/4637), [teku#2822](https://github.com/Consensys-Incorporated/teku/pull/2822), [prysm#11853](https://github.com/OffchainLabs/prysm/pull/11853)

</details>


<a id="range_sync-004"></a>
<details>
<summary><b>range_sync-004</b> Keep block processing off the sync and network loop — <i>implemented · medium · S · latency, sync</i></summary>

**Idea.** Send range-sync batches to a separate processor thread or work queue and receive the result as an event, instead of awaiting heavy import inside the sync manager or the shared async runtime. Networking and the sync loop are not blocked by import.

**Impact.** Already off the sync loop.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/mod.rs:664`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L664) range batches sent as Work::ChainSegment, backfill as Work::ChainSegmentBackfill
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:480`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L480) process_chain_segment runs in the beacon processor
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:546`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L546) result returned to sync via SyncMessage::BatchProcessed

**Skeptic check.** Range and backfill batches go through the beacon processor work queue, and the result comes back to the sync manager as an event. The sync manager never awaits the import.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#3036](https://github.com/sigp/lighthouse/pull/3036), [lighthouse#816](https://github.com/sigp/lighthouse/pull/816)

</details>


<a id="range_sync-005"></a>
<details>
<summary><b>range_sync-005</b> Filter sync peers by earliest available slot — <i>partial · medium · S · bandwidth, sync</i></summary>

**Idea.** Before assigning by-range requests (blocks, blobs, columns, envelopes, backfill), compare the requested slots with each peer's advertised earliest_available_slot and skip peers that cannot serve them. Requests are not wasted on peers that answer ResourceUnavailable.

**Gap in Lighthouse.** Forward range sync picks its blocks/blobs/envelopes peer from chain.peers without has_slot; filter block_peers in block_components_by_range_request with is_synced_or_advanced_with_available_slot(batch start slot).

**Impact.** Avoids wasted by-range requests to peers that answer ResourceUnavailable (checkpoint-synced or pruned peers); small, since forward sync starts near our own finalized slot.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/peerdb/sync_status.rs:35-40`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/peerdb/sync_status.rs#L35-L40) has_slot vs earliest_available_slot
- [`beacon_node/lighthouse_network/src/peer_manager/peerdb.rs:255-264`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/peerdb.rs#L255-L264) synced_peers_for_epoch used by backfill (backfill_sync/mod.rs:225,883) and custody backfill (custody_backfill_sync/mod.rs:1042)
- [`beacon_node/lighthouse_network/src/peer_manager/peerdb.rs:297-312`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/peerdb.rs#L297-L312) good_custody_subnet_peer filters by available slot; used for range columns via custody-by-root (network_context/custody.rs:364, network_context.rs:418-421)
- [`beacon_node/network/src/sync/network_context.rs:476-495`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L476-L495) forward range block/blob/envelope peer pick has no has_slot filter

**Second check.** Beyond the earlier review: range-sync data columns are fetched by custody-by-root whose peer set is already filtered by earliest_available_slot, and custody backfill also filters; only the forward-range block peer is unfiltered.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [grandine@4db1043b5](https://github.com/grandinetech/grandine/commit/4db1043b56fa), [grandine#411](https://github.com/grandinetech/grandine/pull/411), [prysm#17602](https://github.com/OffchainLabs/prysm/pull/17602), [prysm#17770](https://github.com/OffchainLabs/prysm/pull/17770), [grandine@57da4967a](https://github.com/grandinetech/grandine/commit/57da4967a7f4), [nimbus#9127](https://github.com/status-im/nimbus-eth2/pull/9127)

</details>


<a id="range_sync-006"></a>
<details>
<summary><b>range_sync-006</b> Skip range requests for already known or queued blocks — <i>implemented · low · S · sync, bandwidth</i></summary>

**Idea.** When new block roots or gossip blocks arrive during sync, check whether the block or its parent is already known or queued (keyed by root) and only request the span that is new. This avoids duplicate downloads and lookups.

**Impact.** Gossip and unknown-root triggers are deduplicated by root, so duplicate downloads and lookups are avoided.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/mod.rs:357-385`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L357-L385) new_current_lookup drops ignored chains and does not re-request a root that already has a lookup
- [`beacon_node/network/src/sync/block_lookups/mod.rs:254-285`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L254-L285) parent-chain trigger extends an existing lookup instead of creating a new one
- [`beacon_node/network/src/sync/manager.rs:440-455`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L440-L455) FullySynced peer head is looked up only if not known to fork choice
- [`beacon_node/network/src/sync/peer_sync_info.rs:49-80`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/peer_sync_info.rs#L49-L80) peers whose head is known to fork choice do not start range sync
- [`beacon_node/network/src/sync/range_sync/range.rs:187-195`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/range.rs#L187-L195) head chains start at min(local head, remote finalized)

**Skeptic check.** Checked that lookups are keyed by root and deduplicated, and that range sync is started only for unknown heads. This is the lodestar#502/lighthouse#418 mechanism. A finalized chain still restarts at the local finalized epoch, so blocks already imported during non-finality are downloaded again (and then skipped as already known), but that is a rare path.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#502](https://github.com/ChainSafe/lodestar/pull/502), [lighthouse@d2b5cf5a3](https://github.com/sigp/lighthouse/commit/d2b5cf5a32ee), [lighthouse#418](https://github.com/sigp/lighthouse/pull/418)

</details>


<a id="range_sync-007"></a>
<details>
<summary><b>range_sync-007</b> Clip sidecar requests to DA window and fork — <i>partial · medium · S · bandwidth, sync</i></summary>

**Idea.** Clip blob and data-column by-range requests (and column sync work) to slots that are inside the data availability retention window and in the fork that uses that sidecar type (no blobs pre-Deneb or post-Fulu). No requests go out for data peers do not have to serve; also re-request payload envelopes evicted from cache.

**Gap in Lighthouse.** Gloas branch of batch_type returns BlocksAndEnvelopesAndColumns without the DA-window check, so columns are still requested outside the retention window; add it. No re-request of payload envelopes evicted from cache was found.

**Impact.** Saves wasted column requests outside the DA window on Gloas; pre-Gloas is already clipped.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context.rs:1296-1318`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L1296-L1318) batch_type picks Blocks/BlocksAndBlobs/BlocksAndColumns per epoch
- [`beacon_node/beacon_chain/src/custody_context.rs:574-587`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L574-L587) DA boundary + fork gating for blobs/columns
- [`beacon_node/network/src/sync/block_sidecar_coupling.rs:236-245`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_sidecar_coupling.rs#L236-L245) columns requested only for blocks with num_expected_blobs&gt;0 (and revealed payloads on Gloas)
- [`beacon_node/network/src/sync/network_context.rs:1305-1307`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L1305-L1307) Gloas branch ignores DA window (TODO(gloas))

**Second check.** Also checked the coupling: columns are fetched per data-bearing block via custody-by-root, a finer clip than slot ranges, but it applies no DA-window check on Gloas; no envelope re-request on eviction exists in network/src/sync.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [silver#320](https://github.com/gattaca-com/silver/pull/320), [nimbus#7039](https://github.com/status-im/nimbus-eth2/pull/7039), [teku#6779](https://github.com/Consensys-Incorporated/teku/pull/6779), [grandine#413](https://github.com/grandinetech/grandine/pull/413), [grandine#811](https://github.com/grandinetech/grandine/pull/811), [teku#6728](https://github.com/Consensys-Incorporated/teku/pull/6728)

</details>


<a id="range_sync-008"></a>
<details>
<summary><b>range_sync-008</b> Choose range or by-root sync by distance — <i>implemented · low · S · bandwidth, sync</i></summary>

**Idea.** When a peer is only a few slots or epochs ahead, use head sync or by-root fetches instead of a full finalized range sync; when it is further behind, fetch the gap with blocks-by-range at max request size instead of many by-root requests. Each gap size uses the cheaper method.

**Impact.** Each gap size already uses the cheaper method.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/peer_sync_info.rs:26-80`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/peer_sync_info.rs#L26-L80) Behind/FullySynced/Advanced classified by SLOT_IMPORT_TOLERANCE distance
- [`beacon_node/network/src/sync/manager.rs:432-455`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L432-L455) near peers use a by-root lookup, far peers use range sync
- [`beacon_node/network/src/sync/manager.rs:466`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L466) add_peers_force_range_sync switches a long parent lookup to range sync

**Skeptic check.** Checked both directions: a short gap uses lookups, and a long lookup chain is handed to range sync via add_peers_force_range_sync. Range batches are one epoch (32 blocks) rather than the maximum request size, but several batches run in parallel.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#1258](https://github.com/sigp/lighthouse/pull/1258), [nimbus@9dca55917](https://github.com/status-im/nimbus-eth2/commit/9dca559173c8), [ethlambda#351](https://github.com/lambdaclass/ethlambda/pull/351)

</details>


<a id="range_sync-009"></a>
<details>
<summary><b>range_sync-009</b> Start sync from optimistic head, not validated head — <i>implemented · low · S · sync, bandwidth</i></summary>

**Idea.** When computing the common ancestor or start slot for sync, use the optimistically imported head slot instead of the fully validated head, so optimistically imported blocks are not downloaded again.

**Impact.** Optimistically imported blocks are not downloaded again; sync starts from the fork-choice head.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/status.rs:23`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/status.rs#L23) local status uses canonical_head cached_head (fork-choice head, includes optimistic blocks)
- [`beacon_node/network/src/sync/range_sync/range.rs:187`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/range.rs#L187) head chain start_epoch = min(local head_slot, remote finalized)
- [`beacon_node/network/src/sync/range_sync/chain_collection.rs:225-233`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain_collection.rs#L225-L233) local_head_epoch passed as optimistic start
- [`beacon_node/network/src/sync/range_sync/chain.rs:855-886`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L855-L886) start_syncing aligns optimistic_start to local head epoch

**Skeptic check.** Verified: the local SyncInfo head comes from the fork-choice cached head, which includes optimistic blocks, and both head-chain start and finalized-chain optimistic start use it. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#4925](https://github.com/Consensys-Incorporated/teku/pull/4925)

</details>


<a id="range_sync-010"></a>
<details>
<summary><b>range_sync-010</b> Back off or exit sync when no peer ahead — <i>n/a · low · S · cpu</i></summary>

**Idea.** When no peer has a high enough finalized slot or a head ahead of the local head, wait a fixed interval before re-checking or exit range sync, instead of spinning on the same peer set.

**Impact.** No spin loop exists; range sync is event driven by peer status, so no CPU to save.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/range.rs:120-150`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/range.rs#L120-L150) chains only created on peer Status events, no polling loop
- [`beacon_node/network/src/sync/range_sync/chain_collection.rs:423-460`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain_collection.rs#L423-L460) outdated chains/peers are purged

**Sources.** [prysm#7032](https://github.com/OffchainLabs/prysm/pull/7032), [prysm#6679](https://github.com/OffchainLabs/prysm/pull/6679)

</details>


<a id="range_sync-011"></a>
<details>
<summary><b>range_sync-011</b> Batch-verify signatures across a whole sync segment — <i>implemented · low · S · cpu, sync</i></summary>

**Idea.** Pass a complete downloaded range-sync batch to the chain as one segment, collect the signature sets of all its blocks and verify them in one batched BLS job (in worker threads) alongside the state transition. One batched verification is much cheaper than per-block verification.

**Impact.** One batched BLS job per epoch of blocks during range sync.

**Best measured result.** Quoted: verifyImport 3.6543 s/op vs 6.6473 s/op (ratio 0.55); roughly 8s to 4s for 32 blocks (pr:lodestar#3989)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:3235-3247`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3235-L3247) the segment is split into same-epoch runs
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3300-3303`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3300-L3303) signature_verify_chain_segment runs on a blocking worker
- [`beacon_node/beacon_chain/src/block_verification.rs:671-735`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L671-L735) collects all signature sets of every block in the run into one verifier and calls verify() once
- [`beacon_node/../consensus/state_processing/src/per_block_processing/block_signature_verifier.rs:430-436`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/../consensus/state_processing/src/per_block_processing/block_signature_verifier.rs#L430-L436) verify() uses ParallelSignatureSets

**Skeptic check.** Confirmed that range-sync batches are verified with one batched, parallel BLS verify per epoch. Verification runs before the state transition rather than at the same time, but the batching gain that lodestar#3989 measured is present.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#3989](https://github.com/ChainSafe/lodestar/pull/3989), [prysm#6470](https://github.com/OffchainLabs/prysm/pull/6470), [prysm#6469](https://github.com/OffchainLabs/prysm/pull/6469), [lodestar@f699d7fcc](https://github.com/ChainSafe/lodestar/commit/f699d7fccd2f)

</details>


<a id="range_sync-012"></a>
<details>
<summary><b>range_sync-012</b> Couple block and sidecar downloads per batch — <i>implemented · low · S · bandwidth, cpu, latency, sync</i></summary>

**Idea.** For each range-sync batch, request blocks and blob/column sidecars concurrently, buffer them until all are complete, and submit the batch to the processor only when fully downloaded, storing sidecars before importing their blocks. Import does not refetch sidecars or fail on partial batches.

**Impact.** Batches are submitted only when fully coupled, so there are no partial imports and no refetch at import.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_sidecar_coupling.rs:28-77`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_sidecar_coupling.rs#L28-L77) RangeBlockComponentsRequest buffers blocks, blobs/columns and envelopes until complete
- [`beacon_node/network/src/sync/block_sidecar_coupling.rs:230-268`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_sidecar_coupling.rs#L230-L268) Fulu columns are requested by custody-by-root once the blocks arrive
- [`beacon_node/network/src/sync/block_sidecar_coupling.rs:295-300`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_sidecar_coupling.rs#L295-L300) responses() returns None until every component is complete
- [`beacon_node/network/src/sync/network_context.rs:520-538`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L520-L538) blobs_by_range is sent at the same time as blocks_by_range for Deneb/Electra batches

**Skeptic check.** Confirmed the coupling and complete-before-submit behaviour. On Fulu, columns are fetched after the blocks rather than at the same time. This is deliberate, so that only data-bearing blocks are requested (range_sync-013), and parallel batches hide the extra round trip.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#6982](https://github.com/Consensys-Incorporated/teku/pull/6982), [teku#6684](https://github.com/Consensys-Incorporated/teku/pull/6684), [nimbus#8842](https://github.com/status-im/nimbus-eth2/pull/8842), [lodestar#5053](https://github.com/ChainSafe/lodestar/pull/5053), [lodestar#8032](https://github.com/ChainSafe/lodestar/pull/8032)

</details>


<a id="range_sync-013"></a>
<details>
<summary><b>range_sync-013</b> Request sidecars only for blocks with commitments — <i>implemented · low · S · bandwidth, sync</i></summary>

**Idea.** When building blob or data-column by-range requests, skip blocks (and whole batches) without KZG commitments and missed slots, and request only the (block, column) pairs still missing per peer instead of the union over the range.

**Impact.** Fulu range sync asks only for (data-bearing block, custody column) pairs.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_sidecar_coupling.rs:236-252`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_sidecar_coupling.rs#L236-L252) only blocks with num_expected_blobs()&gt;0 go into the custody-by-root request; a batch with no data completes with no request
- [`beacon_node/network/src/sync/network_context/custody.rs:236-270`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L236-L270) continue_requests requests only the columns not yet downloaded, assigned per peer
- [`beacon_node/network/src/sync/network_context/custody.rs:137-158`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L137-L158) a column that is returned is accepted for all blocks of the batch

**Skeptic check.** Confirmed on the Fulu hot path. A small remainder: if a peer returns a column for only some blocks of the batch, custody.rs:143-156 discards the partial result and asks for that column again for all blocks. The Deneb blobs_by_range path still asks for the whole range, but that data is now outside blob retention.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#14843](https://github.com/OffchainLabs/prysm/pull/14843), [prysm#14522](https://github.com/OffchainLabs/prysm/pull/14522), [nimbus#6121](https://github.com/status-im/nimbus-eth2/pull/6121)

</details>


<a id="range_sync-014"></a>
<details>
<summary><b>range_sync-014</b> Fetch batch columns by root after blocks arrive — <i>implemented · medium · S · sync, bandwidth</i></summary>

**Idea.** In range sync, download blocks first and then request custody columns by root for only the blocks with commitments, in one request per peer for the batch, instead of per-column by-range requests to separate peers. Column peers on another head can still serve them and retry bookkeeping shrinks.

**Impact.** One custody-by-root request per batch, only for blocks with commitments, replaces per-column by-range requests on forward and backfill sync.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context.rs:534-538`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L534-L538) Fulu+ batches fetch custody columns via custody-by-root after blocks arrive (no columns-by-range sent)
- [`beacon_node/network/src/sync/block_sidecar_coupling.rs:205-254`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_sidecar_coupling.rs#L205-L254) continue_requests collects only data-bearing block roots (num_expected_blobs &gt; 0) and issues one custody-by-root request for the batch
- [`beacon_node/network/src/sync/network_context.rs:1473-1516`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L1473-L1516) on_custody_by_root_response / handle_custody_by_root_result
- [`beacon_node/network/src/sync/backfill_sync/mod.rs:889`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/backfill_sync/mod.rs#L889) backfill uses the same block_components_by_range_request path

**Skeptic check.** Verified the mechanism of PR 9496 in block_sidecar_coupling continue_requests. Earlier evidence cited range_data_column_batch_request.rs, which is the by-range custody-backfill (CGC change) path, not range sync; the verdict holds on the correct code.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#9496](https://github.com/sigp/lighthouse/pull/9496), [lighthouse#7946](https://github.com/sigp/lighthouse/pull/7946)

</details>


<a id="range_sync-015"></a>
<details>
<summary><b>range_sync-015</b> Build block batch when columns already present — <i>n/a · low · S · sync</i></summary>

**Idea.** When all needed columns for a sync batch are already received, still create the block batch so sync proceeds instead of stalling.

**Impact.** Grandine bug was in its separate column/block batch planner; Lighthouse's batch is block-first so the stall cannot occur.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs): a batch is always created for the block download; columns come after blocks (PR 9496)

**Sources.** [grandine@2eb731faf](https://github.com/grandinetech/grandine/commit/2eb731faf418)

</details>


<a id="range_sync-016"></a>
<details>
<summary><b>range_sync-016</b> Request blocks in ranged batches, not singly — <i>implemented · low · S · sync, latency, bandwidth</i></summary>

**Idea.** During sync, request and serve many blocks per BlocksByRange message in bounded chunks and import them in bulk, instead of one block per request/response. This cuts round trips.

**Impact.** Already ranged and bulk-imported.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain.rs:30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L30) EPOCHS_PER_BATCH=1, one BlocksByRange of 32 slots per batch
- [`beacon_node/network/src/sync/network_context.rs:460-520`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L460-L520) block_components_by_range_request
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3202`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3202) process_chain_segment imports the batch in bulk

**Skeptic check.** This is basic range-sync design and it is clearly present. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus@f9e0418b5](https://github.com/status-im/nimbus-eth2/commit/f9e0418b5bae), [prysm#1119](https://github.com/OffchainLabs/prysm/pull/1119), [prysm#982](https://github.com/OffchainLabs/prysm/pull/982), [nimbus#241](https://github.com/status-im/nimbus-eth2/pull/241), [nimbus@c84d93030](https://github.com/status-im/nimbus-eth2/commit/c84d93030482), [nimbus@54f894fc7](https://github.com/status-im/nimbus-eth2/commit/54f894fc7e9b), [nimbus#245](https://github.com/status-im/nimbus-eth2/pull/245), [lodestar#509](https://github.com/ChainSafe/lodestar/pull/509)

</details>


<a id="range_sync-017"></a>
<details>
<summary><b>range_sync-017</b> Use larger blocks-per-request batch size — <i>not · low · M · sync, latency</i></summary>

**Idea.** Raise the number of blocks (or blobs) asked for per by-range request to the peer rate-limit maximum (for example 64 blocks) and use arbitrary-length batches instead of epoch-sized units, halving request count.

**Gap in Lighthouse.** Raise EPOCHS_PER_BATCH (or make count arbitrary) in range_sync/chain.rs and revisit BatchInfo epoch-based ids, the custody-by-root block_epoch assumption in RangeBlockComponentsRequest::continue_requests, and batch timeout/peer scoring for larger responses.

**Impact.** Fewer round trips during sync (up to half the requests at 64 blocks); gain depends on peer latency, likely modest since 5 batches already pipeline.

**Best measured result.** ~70-80 blk/s sync, occasionally 100; half as many requests (pr:prysm#5978)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain.rs:30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L30) EPOCHS_PER_BATCH=1 (32 blocks) while max_request_blocks is 1024
- [`beacon_node/network/src/sync/block_sidecar_coupling.rs:236`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_sidecar_coupling.rs#L236) comment assumes EPOCHS_PER_BATCH==1

**Sources.** [prysm#5978](https://github.com/OffchainLabs/prysm/pull/5978), [prysm#13531](https://github.com/OffchainLabs/prysm/pull/13531), [prysm#5646](https://github.com/OffchainLabs/prysm/pull/5646), [lodestar@96e6f9549](https://github.com/ChainSafe/lodestar/commit/96e6f9549c6f), [lodestar#1664](https://github.com/ChainSafe/lodestar/pull/1664)

</details>


<a id="range_sync-018"></a>
<details>
<summary><b>range_sync-018</b> Cap items per outgoing by-range request — <i>implemented · low · S · memory, sync</i></summary>

**Idea.** Limit the number of blocks or columns per by-range request (for example 512 column items) and page through larger ranges, so responders do not reject oversized requests and responses stay bounded in memory.

**Impact.** Every by-range or by-root sync request is bounded to one epoch: at most 32 blocks, or 32x128 = 4096 columns, which is under MAX_REQUEST_DATA_COLUMN_SIDECARS.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain.rs:30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L30) EPOCHS_PER_BATCH=1
- [`beacon_node/network/src/sync/backfill_sync/mod.rs:46`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/backfill_sync/mod.rs#L46) BACKFILL_EPOCHS_PER_BATCH=1
- [`beacon_node/network/src/sync/custody_backfill_sync/mod.rs:40`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/custody_backfill_sync/mod.rs#L40) CUSTODY_BACKFILL_EPOCHS_PER_BATCH=1
- [`beacon_node/network/src/sync/network_context.rs:1300-1301`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L1300-L1301) asserts batches are one epoch
- [`beacon_node/network/src/sync/block_sidecar_coupling.rs:236-252`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_sidecar_coupling.rs#L236-L252) columns by root for at most 32 blocks

**Skeptic check.** Confirmed that range, backfill and custody-backfill sync all use one-epoch batches, so requests stay structurally under the spec limits. The earlier evidence was correct, apart from not citing the backfill paths.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#1061](https://github.com/Consensys-Incorporated/teku/pull/1061), [nimbus@65ca74c98](https://github.com/status-im/nimbus-eth2/commit/65ca74c9807d), [prysm#14495](https://github.com/OffchainLabs/prysm/pull/14495)

</details>


<a id="range_sync-019"></a>
<details>
<summary><b>range_sync-019</b> Bound download lookahead ahead of processing — <i>implemented · low · S · bandwidth, memory</i></summary>

**Idea.** Limit how many range-sync batches or slots are downloaded ahead of the processed head (for example 4 batches, or a bounded slot window started when the previous target is processed), and enforce that limit in the send path. This bounds memory and wasted bandwidth when a batch fails.

**Impact.** In-flight and unprocessed batches per chain are capped at 5 epochs, so memory and wasted bandwidth are already bounded.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain.rs:33`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L33)
- [`beacon_node/network/src/sync/range_sync/chain.rs:1188-1215`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L1188-L1215)
- [`beacon_node/network/src/sync/range_sync/chain.rs:1157-1160`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L1157-L1160)

**Skeptic check.** request_batches loops send_batch only while include_next_batch returns Some, and include_next_batch returns None once Downloading\|AwaitingProcessing batches reach BATCH_BUFFER_SIZE. AwaitingValidation batches are not counted, but they are already processed, so the earlier evidence is right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#4720](https://github.com/sigp/lighthouse/pull/4720), [prysm#13599](https://github.com/OffchainLabs/prysm/pull/13599), [lodestar@76e1ca231](https://github.com/ChainSafe/lodestar/commit/76e1ca2312a8), [nimbus@310abe596](https://github.com/status-im/nimbus-eth2/commit/310abe596f00), [nimbus@438f4e6fb](https://github.com/status-im/nimbus-eth2/commit/438f4e6fbd6c)

</details>


<a id="range_sync-020"></a>
<details>
<summary><b>range_sync-020</b> Cap concurrent in-flight sync requests per peer — <i>partial · low · S · bandwidth, latency, sync</i></summary>

**Idea.** Track in-flight sync requests per peer (and per protocol), mark a peer at its limit as busy, and assign new batches only to free peers. Downloads spread over peers and do not queue at one peer or trip its rate limit.

**Gap in Lighthouse.** Peers at MAX_CONCURRENT_REQUESTS are only de-prioritised (tuple sort key), not excluded; if every chain peer is at the limit the request is still sent and queues at the peer. Making it strict would mean returning NoPeer/leaving the batch AwaitingDownload in block_components_by_range_request and retrying on request completion.

**Impact.** Avoids rate-limit rejections and queueing when few peers serve a chain; small effect on mainnet sync with many peers.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context.rs:97-118`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L97-L118) ActiveRequestsPerPeer/at_concurrency_limit
- [`beacon_node/network/src/sync/network_context.rs:476-490`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L476-L490) blocks_by_range peer pick sorts at-limit peers last
- [`beacon_node/network/src/sync/network_context.rs:595-606`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L595-L606) same for data_columns_by_range

**Sources.** [caplin#8023](https://github.com/erigontech/erigon/pull/8023), [lighthouse#801](https://github.com/sigp/lighthouse/pull/801), [lodestar#8166](https://github.com/ChainSafe/lodestar/pull/8166), [lighthouse#9456](https://github.com/sigp/lighthouse/pull/9456)

</details>


<a id="range_sync-021"></a>
<details>
<summary><b>range_sync-021</b> Temporarily blacklist failed sync chains — <i>implemented · low · S · sync, cpu</i></summary>

**Idea.** Remember finalized sync chains that failed for peer-attributable reasons for a short period and refuse to retry them, but do not blacklist when the failure is not the peer's fault. Sync does not loop on bad chains, and valid chains are not lost.

**Impact.** Prevents retry loops on bad finalized chains without blacklisting on network failures.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/range.rs:62`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/range.rs#L62) FAILED_CHAINS_EXPIRY_SECONDS=30
- [`beacon_node/network/src/sync/range_sync/range.rs:77`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/range.rs#L77) failed_chains LRUTimeCache
- [`beacon_node/network/src/sync/range_sync/range.rs:137-140`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/range.rs#L137-L140) finalized peer on a failed root ignored
- [`beacon_node/network/src/sync/range_sync/range.rs:343-353`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/range.rs#L343-L353) insert only when ChainFailed{blacklist:true} and Finalized
- [`beacon_node/network/src/sync/batch.rs:260-266`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/batch.rs#L260-L266),735-738 blacklist=false when download failures dominate (not peer fault)

**Skeptic check.** Verified the time cache, the insert condition and the blacklist flag derivation in batch.rs. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#3142](https://github.com/sigp/lighthouse/pull/3142), [lighthouse#3439](https://github.com/sigp/lighthouse/pull/3439)

</details>


<a id="range_sync-022"></a>
<details>
<summary><b>range_sync-022</b> Cancel in-flight import on batch abort — <i>not · low · M · cpu, sync</i></summary>

**Idea.** When a sync batch is aborted, cancel its in-flight import (block, payload, envelope fetch) and check for cancellation between blocks, so abandoned imports do not stack up and slow retries.

**Gap in Lighthouse.** Pass a cancellation flag (e.g. Arc&lt;AtomicBool&gt; or a chain-alive check) into process_chain_segment/process_blocks and check it between blocks; set it when RangeSync::remove_chain drops the chain.

**Impact.** Saves at most the rest of one batch (up to 32 slots of import) after a chain removal; imports do not stack because the processor runs chain segments serially, so gain is small.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:480-560`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L480-L560) process_chain_segment runs process_blocks to completion; no cancellation token
- [`beacon_node/network/src/sync/range_sync/chain.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs): no cancel path for in-flight processing, removed chain's result is just dropped
- [`beacon_node/network/src/network_beacon_processor/mod.rs:669`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L669) ChainSegment is one work item at a time in the beacon processor queue

**Sources.** [teku#11158](https://github.com/Consensys-Incorporated/teku/pull/11158), [teku#11178](https://github.com/Consensys-Incorporated/teku/pull/11178)

</details>


<a id="range_sync-023"></a>
<details>
<summary><b>range_sync-023</b> Cancel leaked futures and tasks in sync loops — <i>n/a · low · memory, cpu</i></summary>

**Idea.** In sync loops that race timers against peer events or send on result channels, cancel the losing future and make sends context-cancellable, so abandoned timers and blocked tasks do not accumulate.

**Impact.** Rust futures are cancelled on drop; no leaked timers or goroutines in sync loops.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/manager.rs:818`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L818) tokio::select! loop, futures dropped on loop iteration

**Sources.** [nimbus@dde65bed5](https://github.com/status-im/nimbus-eth2/commit/dde65bed50cd), [caplin#24765](https://github.com/erigontech/erigon/pull/24765)

</details>


<a id="range_sync-024"></a>
<details>
<summary><b>range_sync-024</b> Timeout envelope waits and cap per-batch retries — <i>implemented · low · S · sync</i></summary>

**Idea.** Do not let the sync service wait forever on a payload envelope that will not arrive, and cap retries per batch so a stuck batch fails over to another peer.

**Impact.** A missing envelope ends with an empty stream or RPC timeout, fails the batch download and retries on another peer up to a cap. ePBS only.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context.rs:540-560`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L540-L560) envelopes fetched via payload_envelopes_by_range RPC (stream end / RPC timeout completes it)
- [`beacon_node/network/src/sync/block_sidecar_coupling.rs:215-228`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_sidecar_coupling.rs#L215-L228) coupling waits for envelope response, withheld payloads handled by revealed root filter
- [`beacon_node/network/src/sync/manager.rs:538-539`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L538-L539) envelope RPC errors routed to on_payload_envelopes_by_range_response
- [`beacon_node/network/src/sync/range_sync/chain.rs:48`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L48) MAX_BATCH_DOWNLOAD_ATTEMPTS=5

**Skeptic check.** Verified envelope fetch is a by-range RPC under RPC timeouts and that batch attempts are capped; the coupling never waits on a gossip envelope. Gloas code is new, so an untested stall path is possible; earlier evidence was right in substance.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine@fc2b4a480](https://github.com/grandinetech/grandine/commit/fc2b4a48069e)

</details>


<a id="range_sync-025"></a>
<details>
<summary><b>range_sync-025</b> Raise batch retry limit under rate limiting — <i>n/a · low · sync</i></summary>

**Idea.** Allow more download retries per range-sync batch so transient peer rate limiting does not fail the whole chain, and decay pending data column request counts over time.

**Impact.** Lighthouse rate-limits its own outbound requests (self_limiter), so peer rate limiting rarely burns retries; raising 5 would only help devnets.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain.rs:48`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L48) attempts=5
- [`beacon_node/lighthouse_network/src/rpc/self_limiter.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/self_limiter.rs) outbound self rate limiting

**Sources.** [lodestar#8037](https://github.com/ChainSafe/lodestar/pull/8037)

</details>


<a id="range_sync-026"></a>
<details>
<summary><b>range_sync-026</b> Remove sync request tracking entries on every exit — <i>implemented · medium · S · memory</i></summary>

**Idea.** Delete range-sync in-flight request / coupling map entries on every exit path (retry, coupling error, chain removal, completion) so the maps do not grow without bound.

**Gap in Lighthouse.** Minor: entries for a removed chain are not cleaned at removal; they are dropped when their sub-requests respond, error or time out (RPC timeout / peer_disconnected).

**Impact.** Maps stay bounded by in-flight requests on all exit paths.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context.rs:642`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L642) components_by_range_requests entry removed on each response, re-inserted at :699 only while pending
- [`beacon_node/network/src/sync/network_context.rs:1482-1516`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L1482-L1516) custody_by_root_requests remove-then-reinsert, dropped on success or error
- [`beacon_node/network/src/sync/network_context.rs:1664-1694`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L1664-L1694) custody backfill batch map removed first so failures do not leak
- [`beacon_node/network/src/sync/network_context.rs:1734`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L1734) map length metric

**Skeptic check.** Verified the remove-then-reinsert pattern on all three coupling maps, so error, retry and completion paths do not leak. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#8890](https://github.com/sigp/lighthouse/pull/8890), [lighthouse#7767](https://github.com/sigp/lighthouse/pull/7767)

</details>


<a id="range_sync-027"></a>
<details>
<summary><b>range_sync-027</b> Collect metrics only for active sync chains — <i>n/a · low · memory</i></summary>

**Idea.** Have sync-chain metric collectors reference only active chains so removed chains are not kept alive by metrics.

**Impact.** Metric collector retaining objects is a JS GC issue; Rust metrics are plain gauges.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain_collection.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain_collection.rs) metrics read live chains

**Sources.** [lodestar#9568](https://github.com/ChainSafe/lodestar/pull/9568)

</details>


<a id="range_sync-028"></a>
<details>
<summary><b>range_sync-028</b> Release batch block buffers when batch completes — <i>n/a · low · memory</i></summary>

**Idea.** Keep downloaded blocks and sidecars attached to the batch through every lifecycle state and drop the references explicitly when the batch or request handler finishes, so large batch buffers are not leaked, duplicated or kept resident until GC.

**Impact.** Rust drops batch buffers deterministically when the batch state is replaced or the chain is removed.

**Best measured result.** memory stable after fix (screenshot) (pr:lodestar#8369)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs) batches BTreeMap, batch state moves blocks out on processing

**Sources.** [nimbus@571734ce5](https://github.com/status-im/nimbus-eth2/commit/571734ce5520), [lodestar#8369](https://github.com/ChainSafe/lodestar/pull/8369)

</details>


<a id="range_sync-029"></a>
<details>
<summary><b>range_sync-029</b> Limit parallel head-chain syncs — <i>implemented · medium · S · bandwidth, sync</i></summary>

**Idea.** Sync at most a small number (for example 2) of head chains in parallel, avoiding duplicate block downloads and RPC timeouts when many head chains exist.

**Impact.** At most 2 head chains download in parallel.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain_collection.rs:27`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain_collection.rs#L27) PARALLEL_HEAD_CHAINS=2
- [`beacon_node/network/src/sync/range_sync/chain_collection.rs:380-389`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain_collection.rs#L380-L389) only the top 2 preferred head chains start syncing

**Skeptic check.** Verified the cap in update_head_chains. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#1527](https://github.com/sigp/lighthouse/pull/1527)

</details>


<a id="range_sync-030"></a>
<details>
<summary><b>range_sync-030</b> Cap sync peers with a fresh-peer pool — <i>implemented · low · S · sync</i></summary>

**Idea.** Limit the number of peers used concurrently by sync and keep a pool of fresh peers to swap in when a worker fails.

**Impact.** Concurrent block peers per chain are bounded by the batch buffer, and failed peers are swapped for other chain peers on retry.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain.rs:33`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L33) BATCH_BUFFER_SIZE=5 bounds in-flight batches per chain
- [`beacon_node/network/src/sync/range_sync/chain.rs:1188-1212`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L1188-L1212) include_next_batch enforces buffer
- [`beacon_node/network/src/sync/network_context.rs:478-492`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L478-L492) block peer picked from chain peers, deprioritizing failed and at-limit peers
- [`beacon_node/network/src/sync/range_sync/chain_collection.rs:27`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain_collection.rs#L27) at most 2 head chains

**Skeptic check.** There is no explicit peer count cap or named spare pool as in nimbus#1172, but the batch buffer bounds concurrency and peer selection swaps in non-failed chain peers, which gives the same effect. Earlier evidence was right in substance.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#1172](https://github.com/status-im/nimbus-eth2/pull/1172)

</details>


<a id="range_sync-031"></a>
<details>
<summary><b>range_sync-031</b> Skip per-slot tick work while syncing — <i>implemented · medium · S · cpu, sync</i></summary>

**Idea.** Maintain a cheap is-syncing flag set as soon as sync starts, and have per-slot tick handlers read it to skip fork choice, duties and other per-slot work during sync, instead of computing a full peer-based sync status each tick. Resources go to catching up.

**Impact.** When the head is more than 256 slots behind, per-slot fork choice and the later per-slot work are skipped after a cheap slot comparison.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:187-195`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L187-L195)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7491-7493`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7491-L7493)

**Skeptic check.** per_slot_task runs only light pruning and then returns early when best_slot + 256 &lt; slot, before recompute_head_at_current_slot and builder-ban checks. The check is a local slot comparison, not a peer-based status, so the idea is met.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#1470](https://github.com/Consensys-Incorporated/teku/pull/1470), [teku#1484](https://github.com/Consensys-Incorporated/teku/pull/1484), [teku#1406](https://github.com/Consensys-Incorporated/teku/pull/1406), [teku#1405](https://github.com/Consensys-Incorporated/teku/pull/1405)

</details>


<a id="range_sync-032"></a>
<details>
<summary><b>range_sync-032</b> Checkpoint sync with background backfill — <i>implemented · high · S · sync, startup</i></summary>

**Idea.** Start from a trusted weak-subjectivity finalized state and block, follow head immediately, and backfill historical blocks in the background instead of syncing from genesis.

**Impact.** Startup in minutes instead of syncing from genesis.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/client/src/builder.rs:296-297`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L296-L297),423-502 CheckpointSyncUrl / WeakSubjSszBytes start from a weak subjectivity state and block
- [`beacon_node/network/src/sync/backfill_sync/mod.rs:120`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/backfill_sync/mod.rs#L120) BackFillSync downloads historical blocks in the background

**Skeptic check.** Verified checkpoint sync bootstrap in the client builder and the background backfill sync. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#2244](https://github.com/sigp/lighthouse/pull/2244), [nimbus@aed291128](https://github.com/status-im/nimbus-eth2/commit/aed291128a50), [nimbus#1778](https://github.com/status-im/nimbus-eth2/pull/1778), [prysm#10386](https://github.com/OffchainLabs/prysm/pull/10386), [lodestar#5652](https://github.com/ChainSafe/lodestar/pull/5652), [lodestar#1496](https://github.com/ChainSafe/lodestar/pull/1496)

</details>


<a id="range_sync-033"></a>
<details>
<summary><b>range_sync-033</b> Light client provides optimistic head for sync — <i>n/a · low · L · sync</i></summary>

**Idea.** Run a light client inside the beacon node to obtain recent trusted headers and hand optimistic candidate heads to sync, so the node imports near head optimistically before full sync catches up.

**Gap in Lighthouse.** Lighthouse has checkpoint sync plus range sync; an embedded light client would add a whole new trust and networking component.

**Impact.** Little gain: checkpoint sync already gives a trusted start and range sync reaches head quickly.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync)/ (no light client module)

**Sources.** [nimbus#3557](https://github.com/status-im/nimbus-eth2/pull/3557), [nimbus#3715](https://github.com/status-im/nimbus-eth2/pull/3715)

</details>


<a id="range_sync-034"></a>
<details>
<summary><b>range_sync-034</b> Backward sync from trusted head with cheap verification — <i>n/a · low · L · cpu, sync</i></summary>

**Idea.** Obtain a trusted head via light client updates and sync backwards to the known state, verifying historical blocks by hash chain only (skipping signatures and full state transition) since they lead to a trusted head.

**Gap in Lighthouse.** Backfill from the checkpoint already exists; the light client source of the trusted head is not needed.

**Impact.** Negligible; backfill already runs in background and verifies by hash chain plus batched signatures.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/backfill_sync/mod.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/backfill_sync/mod.rs) backfill verifies from a trusted checkpoint backwards

**Sources.** [nimbus#3432](https://github.com/status-im/nimbus-eth2/pull/3432), [nimbus#6515](https://github.com/status-im/nimbus-eth2/pull/6515)

</details>


<a id="range_sync-035"></a>
<details>
<summary><b>range_sync-035</b> Sync columns from minimal covering peer set — <i>not · medium · S · bandwidth, sync</i></summary>

**Idea.** Choose the smallest set of peers whose custody covers the needed data columns and sync columns from them, rather than querying many peers.

**Gap in Lighthouse.** Range sync column requests still choose a random custodian per column. Minimal step: reuse the by-root per-request RandomState ordering in select_columns_by_range_peers_to_request; full step: greedy set cover over peers' custody columns.

**Impact.** Fewer, larger DataColumnsByRange requests per batch on PeerDAS nodes; less request overhead and rate-limit pressure; modest sync throughput gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context.rs:588-627`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L588-L627) select_columns_by_range_peers_to_request picks the min of (deprioritized, at_limit, rand::random per column per peer) independently for each column, so range requests fragment across peers
- [`beacon_node/network/src/sync/network_context/custody.rs:237-239`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L237-L239),381 by-root custody path uses one RandomState per request (hash_one) so the same peer ranking applies to every column and columns cluster on the top-ranked custodian ('avoiding fragmentation'); not a set cover and not used by range sync

**Second check.** Found an anti-fragmentation mechanism (consistent per-request peer ranking) in the by-root custody lookup path, which the earlier review cited but did not credit; it is absent from the range path, so the verdict for range sync stays not, with lower effort since the pattern can be ported.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [grandine#329](https://github.com/grandinetech/grandine/pull/329)

</details>


<a id="range_sync-036"></a>
<details>
<summary><b>range_sync-036</b> Prefer narrow-custody peers for column requests — <i>partial · medium · S · bandwidth, sync</i></summary>

**Idea.** When assigning missing data columns to custodial peers, prefer peers that custody fewer columns, then maximise coverage, and skip peers with no overlap. Requests spread evenly and do not pile onto supernodes.

**Gap in Lighthouse.** Peers with no overlap are skipped and the concurrency limit plus random tie-break spread load, but nothing prefers peers with fewer custody columns, so supernodes (custodians of every column) win more per-column draws. Add a peer custody-group-count term ahead of the random factor in both tuple keys, and optionally group columns per peer for coverage.

**Impact.** Spreads column requests away from supernodes; small, hard-to-measure gain for fullnode sync under load.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context.rs:578`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L578) select_columns_by_range_peers_to_request: per-column min over (deprioritize, at_concurrency_limit, random) among custody peers; no custody-width term
- [`beacon_node/network/src/sync/network_context.rs:1616`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L1616) only caller (range and custody backfill share it)
- [`beacon_node/network/src/sync/network_context/custody.rs:353`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L353) select_column_peer by-root: (at_concurrency_limit, lookup_peers, attempts, hash); no custody-width term
- [`beacon_node/lighthouse_network/src/types/globals.rs:217`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/globals.rs#L217) is_custody_peer_of filter only skips non-overlapping peers

**Second check.** Checked every custody-peer selection site (is_custody_peer_of, get_custodial_peers callers, including custody backfill at network_context.rs:1616) and grepped sync and peerdb for cgc/custody_group_count/supernode terms; none of them weight peers by custody width, they only filter for overlap.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [grandine@5ab321883](https://github.com/grandinetech/grandine/commit/5ab3218839fe), [grandine#332](https://github.com/grandinetech/grandine/pull/332)

</details>


<a id="range_sync-037"></a>
<details>
<summary><b>range_sync-037</b> Do not block startup on sync — <i>implemented · low · S · startup</i></summary>

**Idea.** Start sync and gossip subscription concurrently in the background during node startup instead of awaiting sync, so API, validator and gossip are not delayed.

**Impact.** Startup of API, validator duties and gossip is not blocked on sync.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/service.rs:362`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L362) crate::sync::manager::spawn(...) starts sync as its own task
- [`beacon_node/network/src/service.rs:513`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L513) network service future spawned, not awaited

**Skeptic check.** Verified that the sync manager and network service are spawned on the executor and client startup does not await sync progress. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@353ac486b](https://github.com/ChainSafe/lodestar/commit/353ac486bf21), [lodestar@997ca7223](https://github.com/ChainSafe/lodestar/commit/997ca72231d3), [lodestar#2190](https://github.com/ChainSafe/lodestar/pull/2190)

</details>


<a id="range_sync-038"></a>
<details>
<summary><b>range_sync-038</b> Do not advance sync on unverified empty responses — <i>partial · medium · S · sync, bandwidth</i></summary>

**Idea.** Treat a dropped connection during a range request as a failure, and require empty responses from several distinct peers before advancing past a range, so the queue does not skip real blocks and refetch them later.

**Gap in Lighthouse.** The disconnect-as-failure half is implemented. Lighthouse does not ask a second peer to confirm an empty batch before moving on; a falsely empty batch is found only when the next batch fails, and then all unvalidated batches are refetched.

**Impact.** Avoids occasional redownload of ranges after a falsely empty response; rare, small saving.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/handler.rs:270`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L270),296,517 in-flight RPC streams end with RPCError::Disconnected on connection close
- [`beacon_node/network/src/sync/range_sync/chain.rs:916-975`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L916-L975) inject_error marks the batch download_failed and re-requests it, so a dropped connection is a failure, not an empty batch
- [`beacon_node/network/src/sync/batch.rs:141-145`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/batch.rs#L141-L145) empty batches stay AwaitingValidation until a later batch imports a block
- [`beacon_node/network/src/sync/range_sync/chain.rs:575-592`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L575-L592) empty batch does not advance_chain
- [`beacon_node/network/src/sync/range_sync/chain.rs:800-845`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L800-L845) handle_invalid_batch re-requests all unvalidated earlier batches and scores the original peer in advance_chain:711-750

**Second check.** Confirmed in the RPC handler that disconnects surface as RPCError::Disconnected and fail the batch, so the first half of the idea is done; no multi-peer empty confirmation exists.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [nimbus#7197](https://github.com/status-im/nimbus-eth2/pull/7197), [nimbus#7318](https://github.com/status-im/nimbus-eth2/pull/7318)

</details>


<a id="range_sync-039"></a>
<details>
<summary><b>range_sync-039</b> Ignore gossip blocks as sync triggers while range syncing — <i>implemented · low · S · sync, cpu, bandwidth</i></summary>

**Idea.** During initial/range sync, do not subscribe to or act on gossip blocks for triggering fetches; trigger new range requests only from blocks sync itself imported. This avoids duplicate processing and spurious requests.

**Impact.** During initial sync, gossip is not subscribed. When the node falls behind later, unknown-parent and unknown-root lookups more than SLOT_IMPORT_TOLERANCE from head are ignored.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/service.rs:288`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L288)
- [`beacon_node/network/src/sync/manager.rs:772-784`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L772-L784)
- [`beacon_node/network/src/sync/manager.rs:1001-1011`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L1001-L1011)
- [`beacon_node/network/src/sync/manager.rs:1036-1040`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L1036-L1040)
- [`beacon_node/network/src/sync/manager.rs:1151-1172`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L1151-L1172)

**Skeptic check.** Core topics are subscribed only on the move to Synced. handle_unknown_parent and handle_unknown_block_root both go through should_search_for_block, which rejects requests when the node is not synced, and range requests come only from sync's own peer status. The earlier evidence is right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@dbf397621](https://github.com/ChainSafe/lodestar/commit/dbf397621b06), [lodestar#1618](https://github.com/ChainSafe/lodestar/pull/1618), [lodestar@d1af8dfb4](https://github.com/ChainSafe/lodestar/commit/d1af8dfb4e00), [prysm#2524](https://github.com/OffchainLabs/prysm/pull/2524)

</details>


<a id="range_sync-040"></a>
<details>
<summary><b>range_sync-040</b> Extend forward batches to local head — <i>implemented · low · S · sync</i></summary>

**Idea.** When range sync starts from finalized, keep creating forward batches past the last range end up to the local head slot instead of restarting from the head, so batches are not skipped or redone.

**Impact.** Range chains keep a forward cursor and never restart batch creation from the local head, so no batches are skipped or redone.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain.rs:193`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L193) to_be_downloaded starts at start_epoch
- [`beacon_node/network/src/sync/range_sync/chain.rs:774-778`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L774-L778) to_be_downloaded = max(validating_epoch), skips existing batches
- [`beacon_node/network/src/sync/range_sync/chain.rs:1188-1241`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L1188-L1241) include_next_batch advances to_be_downloaded until target_head_slot

**Skeptic check.** The grandine fix is for its stateless batch builder that recomputed the start slot from the head; the Lighthouse SyncingChain keeps a persistent to_be_downloaded cursor up to target_head_slot. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine@6b58a70dd](https://github.com/grandinetech/grandine/commit/6b58a70dd93a)

</details>


<a id="range_sync-041"></a>
<details>
<summary><b>range_sync-041</b> Correct finalized range sync target slot — <i>implemented · low · S · sync, bandwidth</i></summary>

**Idea.** Compute the finalized range sync target with the right slot offset: far enough past the peer's finalized slot (2 epochs plus 1 slot) that local finality advances, but without an extra batch that cannot be processed.

**Impact.** The fix is in place.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/range.rs:147-152`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/range.rs#L147-L152) target_head_slot = remote_finalized_slot + 2*slots_per_epoch + 1

**Skeptic check.** This is a Lighthouse PR and the 2 epochs + 1 slot target is in current code with its explanatory comment.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@d1146ec8b](https://github.com/sigp/lighthouse/commit/d1146ec8b580), [lighthouse#2198](https://github.com/sigp/lighthouse/pull/2198)

</details>


<a id="range_sync-042"></a>
<details>
<summary><b>range_sync-042</b> Do not start sync before genesis — <i>n/a · low · S · cpu</i></summary>

**Idea.** Delay starting the sync service until genesis, since no block can be imported before then.

**Gap in Lighthouse.** Lighthouse does not delay the sync manager until genesis time. It needs only the genesis state, then starts network and sync before genesis. Pre-genesis, every peer status is at slot 0, so range sync and lookups stay idle and cost nothing.

**Impact.** None measurable: the sync manager is idle pre-genesis.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/service.rs:362`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L362) sync spawned at network start, without a genesis-time gate
- [`beacon_node/client/src/notifier.rs:70`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/notifier.rs#L70) node runs pre-genesis and only logs 'Waiting for genesis'

**Skeptic check.** The earlier evidence was wrong to say the client waits for genesis: it waits for the genesis state, not the genesis time, and manager.rs:887 is unrelated block lookup code. The mechanism is absent but has no performance effect in Lighthouse, so n/a.

**Verdict history.** implemented (checked) → n/a (skeptic)

**Sources.** [teku#1402](https://github.com/Consensys-Incorporated/teku/pull/1402)

</details>


<a id="range_sync-043"></a>
<details>
<summary><b>range_sync-043</b> Locate boundary batch by reverse scan — <i>partial · low · S · cpu</i></summary>

**Idea.** Keep range-sync batches sorted and find the boundary batch (for example the last awaiting validation) by scanning from the end, instead of filtering and mapping the whole list and taking a max.

**Gap in Lighthouse.** Lighthouse keeps batches in a BTreeMap and uses split_off, but include_next_batch still scans all batches (at most BATCH_BUFFER_SIZE plus validating ones) with filter+count. A reverse scan or counter would replace it.

**Impact.** Saves a scan of a few dozen entries per request; unmeasurable on a mainnet node.

**Evidence (Lighthouse @ 928b61e719).**

- network/src/sync/range_sync/chain.rs:45 batches is a BTreeMap (sorted)
- network/src/sync/range_sync/chain.rs:1209 include_next_batch filters whole map to count in-buffer batches
- chain.rs:708 advance_chain uses split_off on the sorted map

**Sources.** [lodestar#2106](https://github.com/ChainSafe/lodestar/pull/2106), [lodestar@bbe62acad](https://github.com/ChainSafe/lodestar/commit/bbe62acadb60)

</details>


<a id="range_sync-044"></a>
<details>
<summary><b>range_sync-044</b> Shorten sync state machine hot path — <i>n/a · low · S · cpu</i></summary>

**Idea.** Reduce the work done per call in the sync batch state machine event trigger, since it runs very often.

**Gap in Lighthouse.** Prysm's state machine event trigger has no Lighthouse counterpart; Lighthouse range sync is event driven over a small BTreeMap with no hot loop worth trimming.

**Impact.** Nothing measurable.

**Evidence (Lighthouse @ 928b61e719).**

- network/src/sync/range_sync/chain.rs:1124 request_batches
- chain.rs:1188 include_next_batch

**Sources.** [prysm#5881](https://github.com/OffchainLabs/prysm/pull/5881)

</details>


<a id="range_sync-045"></a>
<details>
<summary><b>range_sync-045</b> Cheap batch attempt hashing — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Compute the identity hash of a downloaded sync batch from block tree-hash roots (cached per block/envelope) concatenated into one preallocated buffer, instead of SSZ-serialising blocks or manual byte loops. This avoids large temporary allocations.

**Impact.** The batch attempt hash streams only the cached 32-byte block roots into a SipHash hasher. It does not serialize blocks or build a buffer.

**Best measured result.** byteArrayConcat 2.03 ns/op vs Buffer.concat 1.35 ns/op (pr:lodestar#4343)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain.rs:65-69`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L65-L69)
- [`beacon_node/beacon_chain/src/block_verification_types.rs:63-67`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification_types.rs#L63-L67)
- [`beacon_node/network/src/sync/batch.rs:503`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/batch.rs#L503)

**Skeptic check.** The Hash impl for RangeSyncBlock hashes only block_root(), and that root is cached in AvailableBlock or the Gloas variant. The hash is cheaper than the concatenated-buffer form.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#9686](https://github.com/ChainSafe/lodestar/pull/9686), [lighthouse#2916](https://github.com/sigp/lighthouse/pull/2916), [lodestar#4343](https://github.com/ChainSafe/lodestar/pull/4343)

</details>


<a id="range_sync-046"></a>
<details>
<summary><b>range_sync-046</b> Downscore peers with timed-out sync requests — <i>implemented · low · S · sync</i></summary>

**Idea.** Lower the score of peers whose sync batch requests time out so later batches go to responsive peers.

**Impact.** Timed-out peers are downscored and deprioritised for the batch retry.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:657-671`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L657-L671) outgoing StreamTimeout on BlocksByRange/DataColumnsByRange/ByRoot -&gt; MidToleranceError
- [`beacon_node/network/src/sync/batch.rs:203`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/batch.rs#L203) failed_peers
- [`beacon_node/network/src/sync/range_sync/chain.rs:1038-1049`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L1038-L1049) retry deprioritises failed peers

**Skeptic check.** Verified that the RPC timeout penalty covers all sync protocols on outgoing requests, and that batch retries deprioritise failed peers. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine@24d636304](https://github.com/grandinetech/grandine/commit/24d636304be3)

</details>


<a id="range_sync-047"></a>
<details>
<summary><b>range_sync-047</b> Do not redial poorly performing sync peers — <i>implemented · low · S · sync</i></summary>

**Idea.** Do not re-dial peers disconnected for poor sync performance, and include the epoch's first slot in batches so the finalized block is downloaded.

**Impact.** Peers disconnected for bad score are not redialed until the score recovers. Batches include the first slot of the epoch.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/peerdb.rs:153-159`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/peerdb.rs#L153-L159) should_dial excludes peers whose score state is banned or disconnected
- [`beacon_node/lighthouse_network/src/peer_manager/peerdb.rs:196-205`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/peerdb.rs#L196-L205) ForcedDisconnect \| Banned block dialing
- [`beacon_node/network/src/sync/batch.rs:186-188`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/batch.rs#L186-L188) batches start on epoch start slots

**Skeptic check.** The earlier evidence cited only the scoring code. should_dial is the real redial gate, and it confirms the claim. Batch alignment to the epoch start is also in place.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#1412](https://github.com/sigp/lighthouse/pull/1412)

</details>


<a id="range_sync-048"></a>
<details>
<summary><b>range_sync-048</b> Stop requesting columns at peer request cap — <i>partial · low · S · bandwidth</i></summary>

**Idea.** Stop sending column requests to a peer once it reaches the configured request count (&gt;=), so a peer that fails to deliver advertised columns gets no extra requests.

**Gap in Lighthouse.** ActiveCustodyRequest::select_column_peer has the same off-by-one that the nimbus PR fixed. The filter is `peer_attempts <= MAX_CUSTODY_PEER_ATTEMPTS`, so a peer that already got 3 requests and failed to serve its advertised columns can get a 4th. It should be `<`. The per-column cap MAX_CUSTODY_COLUMN_DOWNLOAD_ATTEMPTS = 3 limits this in most cases. The earlier cited at_concurrency_limit (&gt;=) is a different counter: it counts in-flight requests, not failed attempts.

**Impact.** At most one extra columns-by-root request to a withholding peer per custody request. Small.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context/custody.rs:318`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L318) peer_attempts incremented per request sent
- [`beacon_node/network/src/sync/network_context/custody.rs:367-370`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L367-L370) filter keeps peers with peer_attempts &lt;= MAX_CUSTODY_PEER_ATTEMPTS
- [`beacon_node/network/src/sync/network_context/custody.rs:397-398`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L397-L398) MAX_CUSTODY_PEER_ATTEMPTS = 3 ('Max number of attempts ... from a single peer')
- [`beacon_node/network/src/sync/network_context/custody.rs:150-158`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L150-L158) a missing column is a download error with no downscore for non-lookup peers

**Skeptic check.** The earlier evidence pointed at the in-flight concurrency limit, which does use &gt;=. The equivalent per-peer attempt cap for column requests in custody.rs uses &lt;=, which is the bug the nimbus PR fixed.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [nimbus#9208](https://github.com/status-im/nimbus-eth2/pull/9208)

</details>


<a id="range_sync-049"></a>
<details>
<summary><b>range_sync-049</b> Check batch is parent-linked chain before import — <i>implemented · medium · S · cpu, sync</i></summary>

**Idea.** Sort a downloaded batch and verify that each block's parent root links to the previous block before any state transition; reject the batch and switch away from the peer on failure. Invalid or orphaned batches are rejected cheaply.

**Impact.** Batches that are not linked are rejected before signature verification or the state transition, and the fault is put on the peer.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:3068-3112`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3068-L3112)
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:960`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L960)

**Skeptic check.** filter_chain_segment checks child.parent_root == block_root and strictly increasing slots for each pair, before any heavy work. Lighthouse rejects unsorted batches instead of sorting them, and the effect is the same.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#1736](https://github.com/ChainSafe/lodestar/pull/1736), [lodestar@51675fad0](https://github.com/ChainSafe/lodestar/commit/51675fad027e), [caplin#6243](https://github.com/erigontech/erigon/pull/6243)

</details>


<a id="range_sync-050"></a>
<details>
<summary><b>range_sync-050</b> Race duplicate range requests across peers — <i>not · low · M · sync, latency</i></summary>

**Idea.** Send the same block range request to several peers and use the first answer, so one slow peer does not stall sync.

**Gap in Lighthouse.** Send the same range request to 2 peers in block_components_by_range_request and take the first complete response, cancelling the other. Costs bandwidth and complicates coupling state.

**Impact.** Could cut tail latency of stalled batches, but doubles download bandwidth; marginal for most nodes.

**Evidence (Lighthouse @ 928b61e719).**

- network/src/sync/range_sync/chain.rs:1034 send_batch sends each batch to one peer and retries on failure
- network/src/sync/network_context.rs:578 picks one custody peer per column

**Sources.** [nimbus#6722](https://github.com/status-im/nimbus-eth2/pull/6722)

</details>


<a id="range_sync-051"></a>
<details>
<summary><b>range_sync-051</b> Cap concurrent downloads per block root — <i>implemented · low · S · bandwidth</i></summary>

**Idea.** Limit in-flight downloads per block root and entity (blocks, sidecars, envelopes) to a small number (for example 2) with a stale window, so lookups do not fetch the same data from many peers at once.

**Impact.** Lookups are deduplicated per root, with at most one in-flight request per component, so there is no multi-peer fan-out for the same data.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/mod.rs:374-378`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L374-L378) new_current_lookup does not re-request a root that already has a lookup
- [`beacon_node/network/src/sync/block_lookups/single_block_lookup.rs:375-386`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/single_block_lookup.rs#L375-L386) continue_requests uses maybe_start_downloading, one in-flight block request per lookup
- [`beacon_node/network/src/sync/network_context/custody.rs:367-380`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L367-L380) column requests go to one peer per column, with attempts tracked

**Skeptic check.** Verified the dedup per root and the single in-flight request state per component (block, data, payload). Lighthouse is stricter than the nimbus cap of 2. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#9138](https://github.com/status-im/nimbus-eth2/pull/9138)

</details>


<a id="range_sync-052"></a>
<details>
<summary><b>range_sync-052</b> Reject wrong fork digest before decoding — <i>partial · low · S · cpu</i></summary>

**Idea.** After reading a req/resp response chunk, check its fork digest against the expected fork and reject it before SSZ decoding.

**Gap in Lighthouse.** Unknown digests are rejected before SSZ decode, but a valid digest for a fork other than the one expected for the request is not rejected until after decoding. Pass the expected fork into the response decoder and compare after context_bytes_to_fork_name.

**Impact.** Saves a wasted decode of a block from a misbehaving peer; rare.

**Evidence (Lighthouse @ 928b61e719).**

- lighthouse_network/src/rpc/codec.rs:251 context bytes read before length/SSZ decode
- lighthouse_network/src/rpc/codec.rs:909 context_bytes_to_fork_name rejects unknown digest

**Sources.** [nimbus#8204](https://github.com/status-im/nimbus-eth2/pull/8204)

</details>


<a id="range_sync-053"></a>
<details>
<summary><b>range_sync-053</b> Never span fork boundaries in a sync batch — <i>implemented · low · S · sync</i></summary>

**Idea.** Make the sync queue split ranges so no request crosses a fork boundary, so each batch is decoded and verified as one fork type without splitting or re-requests.

**Impact.** None left: one-epoch, epoch-aligned batches cannot straddle an epoch-aligned fork boundary.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain.rs:30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L30) EPOCHS_PER_BATCH = 1
- [`beacon_node/network/src/sync/batch.rs:172-197`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/batch.rs#L172-L197) BatchInfo::new uses exact epoch start_slot..start_slot+n*slots_per_epoch, shift-by-one removed so batches are single-type
- [`beacon_node/network/src/sync/custody_backfill_sync/mod.rs:40`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/custody_backfill_sync/mod.rs#L40) CUSTODY_BACKFILL_EPOCHS_PER_BATCH = 1

**Skeptic check.** Verified BatchInfo::new builds exact epoch-aligned one-epoch ranges in range and backfill sync; the earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#7379](https://github.com/status-im/nimbus-eth2/pull/7379)

</details>


<a id="range_sync-054"></a>
<details>
<summary><b>range_sync-054</b> Align sync batches to epoch boundaries — <i>implemented · medium · S · cpu</i></summary>

**Idea.** Choose range-sync batch boundaries so all blocks in a processing segment are in the same epoch, so they share one shuffling/committee cache for batch signature verification.

**Impact.** Each range batch is one epoch, and process_chain_segment also splits segments into same-epoch runs, so one shuffling is used for each signature batch.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain.rs:30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L30)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3231-3245`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3231-L3245)
- [`beacon_node/beacon_chain/src/block_verification.rs:668`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L668)

**Skeptic check.** Batch ids are epochs and EPOCHS_PER_BATCH is 1. The segment loop partitions blocks by epoch before signature_verify_chain_segment, so the idea is met in two places.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#4322](https://github.com/ChainSafe/lodestar/pull/4322)

</details>


<a id="range_sync-055"></a>
<details>
<summary><b>range_sync-055</b> Evict cached inputs after peer-caused batch failure — <i>implemented · low · S · sync, cpu</i></summary>

**Idea.** When a range-sync batch fails due to peer-served data, evict its block input or envelope from the seen cache so the retry downloads fresh data from another peer instead of reverifying the same bad bytes.

**Impact.** None: the Lodestar bug comes from reusing seenBlockInputCache/seenPayloadEnvelopeInputCache on retry; Lighthouse range sync redownloads the batch and has no such cache in the path.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/batch.rs:377-399`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/batch.rs#L377-L399) processing_completed FaultyFailure/NonFaultyFailure move to AwaitingDownload, dropping the batch data
- [`beacon_node/network/src/sync/range_sync/chain.rs:327-379`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L327-L379) process_batch hands the batch's own blocks to send_chain_segment (no seen-input cache reuse)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3202`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3202) process_chain_segment consumes the passed RangeSyncBlocks

**Skeptic check.** Read lodestar#10025/#10028: they fix a stale-cache reuse specific to Lodestar. Lighthouse batches carry their own data and drop it on failure, so a retry verifies fresh bytes; earlier verdict upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#10028](https://github.com/ChainSafe/lodestar/pull/10028), [lodestar#10025](https://github.com/ChainSafe/lodestar/pull/10025)

</details>


<a id="range_sync-056"></a>
<details>
<summary><b>range_sync-056</b> Keep latest state in memory during initial sync — <i>implemented · high · S · disk, sync</i></summary>

**Idea.** During initial sync, keep the latest state in an in-memory cache instead of writing the state to the database after every block.

**Impact.** Post-block states stay in the in-memory state_cache. On most slots only a small summary goes to disk (ReplayFrom), and snapshots or diffs are written only at hierarchy boundaries.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1661-1671`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1661-L1671)
- [`beacon_node/store/src/hot_cold_store.rs:1706-1707`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1706-L1707)
- [`beacon_node/store/src/hot_cold_store.rs:1749-1768`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1749-L1768)

**Skeptic check.** store_hot_state puts the state into state_cache first, and then writes a summary plus a diff or snapshot only when the storage strategy asks for one. The full state is not written per block, so the earlier evidence is right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#4199](https://github.com/OffchainLabs/prysm/pull/4199)

</details>


<a id="range_sync-057"></a>
<details>
<summary><b>range_sync-057</b> Download ranges from several peers in parallel — <i>implemented · medium · S · bandwidth, latency, sync</i></summary>

**Idea.** Track the heads of all suitable peers and send block-by-range requests to several of them concurrently (round-robin), instead of syncing serially from a single peer. Total download time is bounded by the slowest parallel request, not the sum.

**Impact.** Up to 5 batches per chain download at the same time. Each one goes to a peer chosen from the chain's peer set, which skips failed peers and peers at the concurrency limit, with a random tie-break.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain.rs:33`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L33)
- [`beacon_node/network/src/sync/range_sync/chain.rs:1040-1049`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L1040-L1049)
- [`beacon_node/network/src/sync/network_context.rs:478-494`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L478-L494)

**Skeptic check.** send_batch calls block_components_by_range_request with the chain's peers for each batch. The peer selection spreads concurrent batches across peers, so the idea is met.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#2550](https://github.com/OffchainLabs/prysm/pull/2550), [prysm#3538](https://github.com/OffchainLabs/prysm/pull/3538), [prysm#3675](https://github.com/OffchainLabs/prysm/pull/3675), [nimbus#264](https://github.com/status-im/nimbus-eth2/pull/264), [nimbus@73dc72583](https://github.com/status-im/nimbus-eth2/commit/73dc72583fd0)

</details>


<a id="range_sync-058"></a>
<details>
<summary><b>range_sync-058</b> Disable periodic peer status updates while syncing — <i>implemented · low · S · bandwidth, cpu</i></summary>

**Idea.** Turn off periodic Status re-requests to peers while range sync is running.

**Impact.** Already saves periodic Status traffic during range sync.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs:83-99`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs#L83-L99) status_peers HashSetDelay only polled when sync_state is not SyncingFinalized/SyncingHead

**Skeptic check.** Verified the poll gate in the peer manager behaviour; it is the mechanism of lighthouse#1375 and the earlier evidence is right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#1375](https://github.com/sigp/lighthouse/pull/1375)

</details>


<a id="range_sync-059"></a>
<details>
<summary><b>range_sync-059</b> Find common ancestor instead of restarting at finalized — <i>partial · medium · M · sync, bandwidth</i></summary>

**Idea.** When starting or switching sync target, probe the peer for the highest shared block behind head (with exponentially growing jumps, never falling back to finalized on an RPC error, capped to a reorg range) and sync from there. During non-finality this avoids redownloading long ranges of known blocks.

**Gap in Lighthouse.** Lighthouse probes one point (the batch at local head) and on failure falls back to finalized. It has no exponential back-off search for the highest shared block between finalized and local head, so a node on a minority fork during long non-finality still redownloads from finalized.

**Impact.** Common case (local head on the peer's chain) already avoids redownload. The remaining saving is for fork-switch cases during long non-finality, which can still be thousands of blocks.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain_collection.rs:225`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain_collection.rs#L225),329,389 start_syncing is passed local_head_epoch as the optimistic start epoch
- [`beacon_node/network/src/sync/range_sync/chain.rs:882-887`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L882-L887) optimistic_start set to the aligned local-head batch
- [`beacon_node/network/src/sync/range_sync/chain.rs:1130-1148`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L1130-L1148) the optimistic batch is downloaded first, before any batch from the finalized start
- [`beacon_node/network/src/sync/range_sync/chain.rs:575-581`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L575-L581),707-775 if it imports blocks, advance_chain drops every earlier batch and moves start_epoch/processing_target past it, so the known range is not downloaded
- [`beacon_node/network/src/sync/range_sync/chain.rs:582-590`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L582-L590),661-680,816-821 if empty or invalid, the candidate is rejected and sync falls back to processing_target (the finalized-derived start)
- [`beacon_node/network/src/sync/range_sync/range.rs:187`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/range.rs#L187) head-chain start_epoch = min(local head slot, remote finalized slot)

**Second check.** The earlier review missed the optimistic_start mechanism: the chain first fetches the local-head batch, and if it links, advance_chain skips everything from finalized to local head. That is a one-step common-ancestor guess, not an exponential probe.

**Verdict history.** not (checked) → partial (refuted)

**Sources.** [teku#9211](https://github.com/Consensys-Incorporated/teku/pull/9211), [caplin#16915](https://github.com/erigontech/erigon/pull/16915), [teku#2618](https://github.com/Consensys-Incorporated/teku/pull/2618), [teku#3045](https://github.com/Consensys-Incorporated/teku/pull/3045), [teku#9057](https://github.com/Consensys-Incorporated/teku/pull/9057), [nimbus#1919](https://github.com/status-im/nimbus-eth2/pull/1919)

</details>


<a id="range_sync-060"></a>
<details>
<summary><b>range_sync-060</b> Include non-canonical heads in common ancestor search — <i>not · low · M · sync, bandwidth</i></summary>

**Idea.** When finding the common ancestor with a remote chain, also compare against all local non-canonical chain heads and pick the highest-slot ancestor, so blocks held on side forks are not downloaded again.

**Gap in Lighthouse.** Would need a common-ancestor search over fork-choice heads in RangeSync::add_peer before choosing start_epoch; today side-fork blocks we already hold are re-downloaded and dropped as duplicates.

**Impact.** Saves re-downloading a few epochs of side-fork blocks in rare reorg cases; negligible on normal nodes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/range.rs:187`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/range.rs#L187) head chain starts at min(local head, remote finalized) epoch; no common-ancestor search
- [`beacon_node/network/src/sync/range_sync/range.rs:150`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/range.rs#L150) finalized chain starts at local finalized epoch

**Sources.** [teku#9209](https://github.com/Consensys-Incorporated/teku/pull/9209), [teku#9210](https://github.com/Consensys-Incorporated/teku/pull/9210)

</details>


<a id="range_sync-061"></a>
<details>
<summary><b>range_sync-061</b> Rank finalized sync peers by finalized epoch — <i>partial · low · S · sync</i></summary>

**Idea.** Select sync peers whose finalized epoch and head reach the target (same fork, not behind us), rank them by finalized epoch then head slot, and pick the highest target, so requests go to peers that can serve the range.

**Gap in Lighthouse.** Peers behind or on another fork are filtered and grouped by finalized root, but the winning chain is the one with most peers, not the highest finalized epoch/head; no per-peer ranking. Rank in chain_collection::update_finalized_chains by (finalized epoch, head slot) before peer count.

**Impact.** Marginal: avoids syncing toward a lower finalized target first; few redundant requests on mainnet.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/range.rs:127-170`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/range.rs#L127-L170) chains keyed by remote finalized root, target = finalized slot+2 epochs+1
- [`beacon_node/network/src/sync/range_sync/chain_collection.rs:276-300`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain_collection.rs#L276-L300) update_finalized_chains picks max_by_key(available_peers)
- [`beacon_node/network/src/sync/peer_sync_info.rs:26-80`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/peer_sync_info.rs#L26-L80) remote_sync_type filters peers behind us / not ahead

**Sources.** [prysm#7619](https://github.com/OffchainLabs/prysm/pull/7619), [lodestar#7746](https://github.com/ChainSafe/lodestar/pull/7746), [lodestar@2bbc45f31](https://github.com/ChainSafe/lodestar/commit/2bbc45f3142d), [lodestar#713](https://github.com/ChainSafe/lodestar/pull/713), [lodestar@f75619710](https://github.com/ChainSafe/lodestar/commit/f756197106c0)

</details>


<a id="range_sync-062"></a>
<details>
<summary><b>range_sync-062</b> Start range requests after blocks already held — <i>not · low · S · bandwidth, cpu, sync</i></summary>

**Idea.** Compute the range-sync start slot from what the node already has (max of last imported block, local head and local finalized slot) and clamp every by-range request start, including the first, to it. The node does not re-download and re-import blocks it already holds.

**Gap in Lighthouse.** Start epoch is the local finalized epoch, not the max of imported block, head and finalized slot, so a new/restarted chain re-downloads the blocks between finalized and head (typically 2-3 epochs, up to ~100 blocks) and filters them afterwards. Clamp the start in range.rs add_peer / SyncingChain::new and start_syncing to local head epoch when the head is on the target chain.

**Impact.** Saves a few epochs of redundant block downloads and filter work on chain restarts; small steady-state effect.

**Best measured result.** 66 bursts / 748 redundant blocks in ~3 h on a follower, ~65 ms per redundant arrival, one 67-block burst delayed a gossip block 4.2 s (pr:ethlambda#645)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/range.rs:147-160`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/range.rs#L147-L160) finalized chain starts at local_info.finalized_epoch
- [`beacon_node/network/src/sync/range_sync/range.rs:187`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/range.rs#L187) head chain starts at min(local head, remote finalized) epoch
- [`beacon_node/network/src/sync/range_sync/chain.rs:855-880`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L855-L880) start_syncing advances only to local finalized epoch

**Sources.** [nimbus#3512](https://github.com/status-im/nimbus-eth2/pull/3512), [ethlambda#645](https://github.com/lambdaclass/ethlambda/pull/645), [lodestar#1585](https://github.com/ChainSafe/lodestar/pull/1585), [teku#1079](https://github.com/Consensys-Incorporated/teku/pull/1079), [prysm#4130](https://github.com/OffchainLabs/prysm/pull/4130), [nimbus#1279](https://github.com/status-im/nimbus-eth2/pull/1279), [lodestar#1425](https://github.com/ChainSafe/lodestar/pull/1425), [lighthouse#8416](https://github.com/sigp/lighthouse/pull/8416)

</details>


<a id="range_sync-063"></a>
<details>
<summary><b>range_sync-063</b> Silently skip pre-finalization blocks in range sync — <i>implemented · low · S · sync</i></summary>

**Idea.** In range sync, drop blocks from before local finalization without treating them as unknown-parent errors.

**Impact.** Already skipped without penalty or unknown-parent handling.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:3162-3166`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3162-L3166) filter_chain_segment silently drops WouldRevertFinalizedSlot blocks from the segment
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:854-857`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L854-L857) WouldRevertFinalizedSlot mapped to Ok(()) with no peer action
- [`beacon_node/beacon_chain/src/block_verification.rs:1843`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1843) finalized-slot check

**Skeptic check.** Pre-finalization blocks are filtered out of the chain segment before import and the error is treated as success; earlier verdict upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#3245](https://github.com/ChainSafe/lodestar/pull/3245)

</details>


<a id="range_sync-064"></a>
<details>
<summary><b>range_sync-064</b> Skip already-imported blocks before batch processing — <i>implemented · low · S · cpu, disk, sync</i></summary>

**Idea.** Before processing a sync batch, drop duplicate blocks and blocks already in fork choice or the DB, and skip their post-processing, so overlapping, replayed or retried batches cost almost nothing.

**Impact.** Replayed or overlapping batches skip signature, KZG and state work; only the download cost remains.

**Best measured result.** 4x faster forward sync (title) (pr:caplin#11663)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:3068-3142`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3068-L3142) filter_chain_segment drops DuplicateFullyImported, GenesisBlock and finalized-slot blocks via check_block_relevancy
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3218-3226`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3218-L3226) process_chain_segment runs the filter before signature_verify_chain_segment, KZG and import
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:646`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L646) recompute_head only when imported_blocks is non-empty

**Skeptic check.** Confirmed that the filter runs first on the forward range-sync path and skips all later processing for known blocks. Duplicates inside one batch are rejected (NonLinearSlots), not dropped, but that is a malformed-batch case. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#6146](https://github.com/OffchainLabs/prysm/pull/6146), [caplin#11663](https://github.com/erigontech/erigon/pull/11663), [prysm#13442](https://github.com/OffchainLabs/prysm/pull/13442), [caplin#13831](https://github.com/erigontech/erigon/pull/13831)

</details>


<a id="range_sync-065"></a>
<details>
<summary><b>range_sync-065</b> Handle switching target chain without stalling — <i>n/a · low · S · sync</i></summary>

**Idea.** Support switching from a longer target chain to a shorter one (including non-finalized back to finalized sync) without stalling batch sync, and mark sync failed when common ancestor search fails.

**Impact.** Lighthouse runs separate finalized/head chains per target rather than one retargetable batch sync, so the Teku stall does not arise.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain_collection.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain_collection.rs), range.rs:130 independent chains per target; failed_chains set

**Sources.** [teku#3705](https://github.com/Consensys-Incorporated/teku/pull/3705), [lodestar#2464](https://github.com/ChainSafe/lodestar/pull/2464)

</details>


<a id="range_sync-066"></a>
<details>
<summary><b>range_sync-066</b> Progress sync on local chain without remote — <i>n/a · low · S · sync</i></summary>

**Idea.** Allow sync to make progress on the local chain without requiring a remote chain target.

**Impact.** Teku-specific edge case of its single-sync-target design; Lighthouse local progress is driven by peer-created chains and gossip.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/range.rs:115`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/range.rs#L115) chains created only from a peer status; no remote-less mode

**Sources.** [teku#9184](https://github.com/Consensys-Incorporated/teku/pull/9184)

</details>


<a id="range_sync-067"></a>
<details>
<summary><b>range_sync-067</b> Ordered async delivery of sync status events — <i>n/a · low · S · latency</i></summary>

**Idea.** Deliver sync status notifications through an ordered async runner so subscribers cannot block the sync event thread.

**Impact.** Rust sync manager does not call blocking subscribers on its event loop.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/manager.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs) sync state is a plain message loop; network_globals sync_state set directly

**Sources.** [teku#2798](https://github.com/Consensys-Incorporated/teku/pull/2798)

</details>


<a id="range_sync-068"></a>
<details>
<summary><b>range_sync-068</b> Yield between synced block imports — <i>n/a · low · latency</i></summary>

**Idea.** Process synced blocks one by one and yield to the scheduler between them, so a cooperative event loop stays responsive during bulk import.

**Impact.** Tokio with a blocking pool and the beacon processor already keep other work responsive during chain segment import; no cooperative-loop starvation.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:474`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L474) process_chain_segment runs as beacon_processor work

**Sources.** [nimbus#1464](https://github.com/status-im/nimbus-eth2/pull/1464)

</details>


<a id="range_sync-069"></a>
<details>
<summary><b>range_sync-069</b> Race peers for block access lists alongside bodies — <i>n/a · low · sync, latency</i></summary>

**Idea.** When downloading block bodies in range/backward sync, fetch the block access lists (BALs) in the same pass and race several peers for them, taking the first hash-valid response, so blocks can execute in parallel with BALs available instead of falling back to serial execution.

**Impact.** Block access lists are a Glamsterdam feature not present in Lighthouse; nothing to race for.

**Best measured result.** Blocks executed with downloaded BAL ~30% -&gt; 100% on bal-devnet-7 resync (pr:caplin#21679)

**Evidence (Lighthouse @ 928b61e719).**

- beacon_node (grep block_access_list: only store/test/block_hash hits)

**Sources.** [caplin#21679](https://github.com/erigontech/erigon/pull/21679)

</details>


<a id="range_sync-070"></a>
<details>
<summary><b>range_sync-070</b> Save synced blocks to DB concurrently — <i>not · medium · L · sync, cpu, disk</i></summary>

**Idea.** During range sync, write imported blocks to the database asynchronously (off the import path) so DB writes do not serialize block processing.

**Gap in Lighthouse.** Move the hot DB write out of import_block into a background writer (queue ops, flush before head or finalization needs them) and keep crash consistency with fork choice persistence (issue 2028 revert logic).

**Impact.** Could overlap DB writes with state transition during initial sync. Prysm saw ~15 to 26 blk/s, but Lighthouse's write share is unknown (measure BLOCK_PROCESSING_DB_WRITE first).

**Best measured result.** ~15 blk/s to 26 blk/s in initial sync (pr:prysm#3673)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:4749-4756`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4749-L4756) import_block pushes PutBlock/PutState and calls store.do_atomically_with_block_and_blobs_cache synchronously, under BLOCK_PROCESSING_DB_WRITE timer, before fork choice is committed
- [`beacon_node/store/src/hot_cold_store.rs:1459`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1459) do_atomically_with_block_and_blobs_cache is a synchronous batch write
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3340-3380`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3340-L3380) chain segment blocks imported one after another

**Second check.** Searched beacon_chain and store for any write queue, deferred or background write path; none exists. Only the migrator (finalization) runs in the background, not per-block import writes.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [prysm#3673](https://github.com/OffchainLabs/prysm/pull/3673)

</details>


<a id="range_sync-071"></a>
<details>
<summary><b>range_sync-071</b> Verify execution payload in parallel with block — <i>not · medium · M · latency, sync, cpu</i></summary>

**Idea.** In range sync, run the EL newPayload call and the payload envelope state transition concurrently with consensus block verification, and batch the envelope signatures together with the block signature set, instead of doing them serially per block.

**Gap in Lighthouse.** In process_chain_segment, overlap envelope newPayload (EL) with the envelope state transition and with consensus verification of the next block, and add envelope signatures to the segment signature set in signature_verify_chain_segment.

**Impact.** Gloas-only; range sync envelope import is fully serial (state transition, then EL, then import, per block), so overlapping could hide EL latency per block.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:3298`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3298) signature_verify_chain_segment gets blocks only; envelopes extracted at 3291
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3372`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3372) process_range_sync_envelope awaited after each process_block, serially
- [`beacon_node/beacon_chain/src/payload_envelope_verification/import.rs:432`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/import.rs#L432) verify_execution_payload_envelope (signature + state transition) runs first with its own signature check
- [`beacon_node/beacon_chain/src/payload_envelope_verification/import.rs:452`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/import.rs#L452) notify_new_payload awaited only after state processing, not concurrently

**Second check.** Read process_range_sync_envelope itself: it verifies the envelope signature individually with VerifySignatures::True, then does the state transition, then awaits newPayload; no join/spawn overlap anywhere in this path.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [lodestar#9103](https://github.com/ChainSafe/lodestar/pull/9103)

</details>


<a id="range_sync-072"></a>
<details>
<summary><b>range_sync-072</b> Pause range sync while execution layer offline — <i>implemented · medium · S · cpu, sync</i></summary>

**Idea.** Stop processing range sync batches and lookups while the execution engine is offline and resume when it comes back, so batches are not processed, failed and penalised for nothing.

**Impact.** Already avoids processing, failing and penalising batches while the EL is offline.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context.rs:1279-1282`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L1279-L1282) beacon_processor_if_enabled returns None when EL offline
- [`beacon_node/network/src/sync/range_sync/chain.rs:338-340`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L338-L340) process_batch returns early without processing when EL offline
- [`beacon_node/network/src/sync/manager.rs:1177-1179`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L1177-L1179) lookups refuse to start when EL offline
- [`beacon_node/network/src/sync/manager.rs:1183-1221`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L1183-L1221) handle_new_execution_engine_state drops lookups on Offline, range_sync.resume on Online
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:898-912`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L898-L912) EL-caused ExecutionPayloadError gives peer_action None (NonFaultyFailure)

**Skeptic check.** Verified the gate is on the actual processing path (process_batch via beacon_processor_if_enabled) and resume re-kicks chains; the earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#3428](https://github.com/sigp/lighthouse/pull/3428)

</details>


<a id="range_sync-073"></a>
<details>
<summary><b>range_sync-073</b> Do not count non-fault failures against batch retries — <i>partial · low · S · sync, bandwidth</i></summary>

**Idea.** When a batch fails because the peer rate-limited us or for another reason that is not the peer's fault, do not consume the batch retry budget or penalise the peer; back that peer off and send the batch to a different peer, so the chain is not dropped and re-downloaded.

**Gap in Lighthouse.** Processing-side non-faulty failures are already exempt, but download-side RateLimited responses still burn a download attempt and penalise the peer. Add a RateLimited case in RpcResponseError handling in Chain::inject_error that skips Batch::download_failed's counter (or backs off the peer) and retries on another peer.

**Impact.** Avoids dropping a range-sync chain after repeated rate-limit responses from peers; only matters on busy/overloaded peer sets, small gain.

**Best measured result.** Observed 1,396 rate-limited responses causing peer loss (pr:lodestar#8924)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/batch.rs:308`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/batch.rs#L308) download_failed counts every failure incl. None against max attempts
- [`beacon_node/network/src/sync/range_sync/chain.rs:652`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L652) NonFaultyFailure handled only for processing results
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:605`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L605) RateLimited from BlocksByRange -&gt; MidToleranceError penalty
- [`beacon_node/network/src/sync/range_sync/chain.rs:916`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L916) inject_error has no rate-limit branch

**Sources.** [lodestar#9034](https://github.com/ChainSafe/lodestar/pull/9034), [lodestar#8924](https://github.com/ChainSafe/lodestar/pull/8924), [lighthouse#3245](https://github.com/sigp/lighthouse/pull/3245)

</details>


<a id="range_sync-074"></a>
<details>
<summary><b>range_sync-074</b> Score sync peers by observed throughput — <i>not · high · M · sync, bandwidth</i></summary>

**Idea.** Track per-peer download throughput (blocks returned and processed, bandwidth) and pick range sync peers by that score, weighted-random so others still get some requests, so fast peers receive more batches and slow peers fewer.

**Gap in Lighthouse.** No per-peer throughput or latency stats anywhere in sync or peer_manager. Add an EWMA of blocks (or bytes) per second per peer, updated on by-range responses, and use it as a weighted-random key in block_components_by_range_request, select_columns_by_range_peers_to_request and custody select_column_peer.

**Impact.** Faster peers get more batches during initial sync, which cuts download stalls; gain depends on peer spread, maybe tens of percent of sync time when some peers are slow.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context.rs:476-495`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L476-L495) block peer = min(deprioritized, at_concurrency_limit, rand::random); no speed term
- [`beacon_node/network/src/sync/network_context.rs:116-118`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L116-L118) at_concurrency_limit is a fixed MAX_CONCURRENT_REQUESTS cap, not a throughput score
- [`beacon_node/network/src/sync/network_context/custody.rs:353-392`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L353-L392) column peer pick uses attempts/lookup_peers/hash, no speed
- [`beacon_node/network/src/sync/range_sync/chain.rs:1028-1050`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L1028-L1050) send_batch passes chain peers + failed_peers only

**Second check.** Grepped network and lighthouse_network for throughput/latency/ewma/speed/response_time and every peer-selection .min()/sort; the only load-sensitive term is the 2-request concurrency cap, which lets a fast peer free its slots sooner but does not rank peers by speed.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [prysm#7974](https://github.com/OffchainLabs/prysm/pull/7974), [prysm#6709](https://github.com/OffchainLabs/prysm/pull/6709), [prysm#6928](https://github.com/OffchainLabs/prysm/pull/6928), [nimbus#1376](https://github.com/status-im/nimbus-eth2/pull/1376), [prysm#13820](https://github.com/OffchainLabs/prysm/pull/13820)

</details>


<a id="range_sync-075"></a>
<details>
<summary><b>range_sync-075</b> Weighted round robin on peer rate-limit capacity — <i>partial · medium · M · sync, bandwidth</i></summary>

**Idea.** Fetch each large contiguous batch from one peer and choose peers by weighted round robin on their remaining rate-limit capacity, so each peer's full burst rate is used without tripping its limit.

**Gap in Lighthouse.** Lighthouse already mirrors each peer's limit (self limiter) so it does not trip it, and fetches each batch from one peer; missing is using the self limiter's remaining tokens to weight peer selection in block_components_by_range_request (requests to a drained peer are delayed in the queue instead of routed to a peer with capacity).

**Impact.** Avoids batches waiting in the self-limiter queue of a drained peer while other peers are idle; gain depends on peer count and limits, unclear.

**Best measured result.** up to 90% of burst rate (640 blk/s) (pr:prysm#5887)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/self_limiter.rs:83`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/self_limiter.rs#L83) SelfRateLimiter::allows mirrors the peer's rate limiter per (peer, protocol) and queues outbound requests until quota is available
- [`beacon_node/src/config.rs:1500`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/config.rs#L1500) self limiter enabled by default with default params
- [`beacon_node/lighthouse_network/src/rpc/mod.rs:465`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/mod.rs#L465) outbound requests go through outbound_request_limiter
- [`beacon_node/network/src/sync/network_context.rs:476`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L476) peer choice uses deprioritize set, concurrency limit and random tie-break, not remaining quota
- [`beacon_node/network/src/sync/range_sync/chain.rs:30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L30) EPOCHS_PER_BATCH = 1, whole batch from one peer

**Second check.** The earlier review missed the lighthouse_network outbound SelfRateLimiter, which is the 'mirror the peer's limiter' half of the idea and is on by default; only quota-weighted peer choice is absent.

**Verdict history.** not (checked) → partial (refuted)

**Sources.** [prysm#5798](https://github.com/OffchainLabs/prysm/pull/5798), [prysm#5887](https://github.com/OffchainLabs/prysm/pull/5887), [prysm#6187](https://github.com/OffchainLabs/prysm/pull/6187)

</details>


<a id="range_sync-076"></a>
<details>
<summary><b>range_sync-076</b> Randomize sync peer selection — <i>implemented · low · S · sync, bandwidth</i></summary>

**Idea.** Pick range sync peers randomly (or shuffle the peer list) instead of a fixed order or a complex scoring policy, so load spreads over all peers and the same few are not hammered.

**Impact.** Batch and column peers are picked at random among equally eligible peers on forward sync and backfill.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context.rs:478-492`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L478-L492) block_components_by_range_request orders by (deprioritised, at_concurrency_limit, rand::random) and takes the min
- [`beacon_node/network/src/sync/range_sync/chain.rs:1040`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L1040) and [`beacon_node/network/src/sync/backfill_sync/mod.rs:889`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/backfill_sync/mod.rs#L889) both use it
- [`beacon_node/network/src/sync/network_context/custody.rs:353-389`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L353-L389) select_column_peer uses a per-request RandomState hash as tie-breaker

**Skeptic check.** Confirmed random tie-breaking on both range and backfill paths. One small correction: at_concurrency_limit is a boolean, so the code does not prefer peers with fewer active requests. It only skips peers that are at the limit.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@25fb1b672](https://github.com/ChainSafe/lodestar/commit/25fb1b672278), [caplin#16995](https://github.com/erigontech/erigon/pull/16995), [grandine#158](https://github.com/grandinetech/grandine/pull/158)

</details>


<a id="range_sync-077"></a>
<details>
<summary><b>range_sync-077</b> Pick failover peer without scanning peer list — <i>not · low · S · cpu</i></summary>

**Idea.** When choosing a replacement sync peer that excludes one peer, pick a random index and retry if it hits the excluded peer, instead of first copying and filtering the whole peer list.

**Gap in Lighthouse.** Replace the iterate-and-min with random index and retry; would need changes in block_components_by_range_request.

**Impact.** Peer set per chain is small (tens) and one pick per batch request; saving is negligible and the current scan also honours concurrency limits.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context.rs:478-492`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L478-L492) block_components_by_range_request iterates all chain peers, min of (deprioritized, at_limit, random)
- [`beacon_node/network/src/sync/range_sync/chain.rs:1040`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L1040) passes failed_peers

**Sources.** [prysm#6442](https://github.com/OffchainLabs/prysm/pull/6442)

</details>


<a id="range_sync-078"></a>
<details>
<summary><b>range_sync-078</b> Wait for full custody subnet coverage before column batches — <i>implemented · medium · S · sync, bandwidth</i></summary>

**Idea.** In custody column range sync, only send a batch once there are peers for every custody column subnet, and choose a randomized custody peer per column, so batches do not fail at once and loop retrying against a failing peer.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain.rs:1168-1184`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L1168-L1184) good_peers_on_sampling_subnets requires has_good_custody_range_sync_peer for every sampling subnet
- [`beacon_node/network/src/sync/range_sync/chain.rs:1221`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L1221) include_next_batch, :1015 attempt_send_awaiting_download_batches, :1133 request_batches, :481 gate on it
- [`beacon_node/network/src/sync/backfill_sync/mod.rs:1017`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/backfill_sync/mod.rs#L1017) same gate on backfill
- [`beacon_node/network/src/sync/network_context/custody.rs:353`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L353) select_column_peer picks a randomized custody peer per column

**Skeptic check.** Confirmed that the coverage gate is on every path that sends batches, on both forward and backfill sync, and that column peers are randomized per column. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#6004](https://github.com/sigp/lighthouse/pull/6004)

</details>


<a id="range_sync-079"></a>
<details>
<summary><b>range_sync-079</b> Pool peers per chain and load-balance batches — <i>implemented · medium · S · sync, bandwidth</i></summary>

**Idea.** Group peers that report the same finalized/head chain into one syncing chain and load-balance its batch downloads over the whole peer pool through one state machine.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain_collection.rs:480-520`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain_collection.rs#L480-L520) add_peer_or_create_chain joins peers with the same target (has_same_target) into one SyncingChain
- [`beacon_node/network/src/sync/range_sync/chain.rs:1028-1045`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L1028-L1045) send_batch draws block peers from the chain-wide self.peers pool
- [`beacon_node/network/src/sync/range_sync/chain.rs:33`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L33) BATCH_BUFFER_SIZE=5 batches spread over the pool

**Skeptic check.** Confirmed per-target chain grouping and one state machine per chain that load-balances batches over the pool. Custody columns come from global custodial peers, not from the chain pool, but that does not change the idea.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#663](https://github.com/sigp/lighthouse/pull/663)

</details>


<a id="range_sync-080"></a>
<details>
<summary><b>range_sync-080</b> Drop sync peers that return too few blocks — <i>partial · low · M · sync</i></summary>

**Idea.** When a peer returns only a few blocks per range request (throttling), fail the sync against it and do not choose it as sync target for a while unless it progresses a minimum number of slots.

**Gap in Lighthouse.** Throttled short responses are only caught after the following batch is processed (then faulty peers are deprioritised/penalised); no immediate per-response check for suspiciously few blocks or temporary exclusion from sync target selection. Add a min-blocks check in the by-range response handler and mark the peer failed for that batch.

**Impact.** Avoids slow peers throttling range sync; gain only when a peer rate-limits by returning short ranges.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain.rs:575-590`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L575-L590) empty batch handling and optimistic rejection
- [`beacon_node/network/src/sync/range_sync/chain.rs:1034`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L1034) failed_peers deprioritised in peer choice
- [`beacon_node/network/src/sync/batch.rs:143`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/batch.rs#L143) incomplete batches only detected when next batch imports

**Sources.** [teku#2420](https://github.com/Consensys-Incorporated/teku/pull/2420)

</details>


<a id="range_sync-081"></a>
<details>
<summary><b>range_sync-081</b> Keep partial column responses, retry only missing columns — <i>partial · medium · M · sync, bandwidth</i></summary>

**Idea.** In range sync, accept column responses that miss some columns, keep the good data, attribute the missing columns to the responsible peer, and re-request only those columns from other peers of the syncing chain instead of failing and re-downloading the whole batch.

**Gap in Lighthouse.** Columns that are missing at download time are kept and retried per column. But when a column fails processing (AvailabilityCheckError::InvalidColumn from the KZG check in process_chain_segment), range sync does not retry only that column from another peer. block_error_penalty's CustodyPeerForColumn is mapped to None in the range-sync arm of handle_failed_chain_segment, so the result is a NonFaultyFailure. The whole batch (blocks and all columns) is then downloaded again, and the peer that served the bad column is not penalized because the PeerGroup is dropped during coupling (RangeBlockComponentsRequest::responses). NonFaultyFailure never exhausts the batch, so a bad column peer can cause repeated full re-downloads. Also, only the block peer is in lookup_peers, so other column peers that withhold data are not downscored. A column is also accepted only when all of its block roots are present, so one missing sidecar makes the whole column be requested again.

**Impact.** An invalid column from one peer costs a full batch re-download (blocks plus every custody column) with no attribution. This repeats until a different peer happens to serve that column.

**Best measured result.** Improve sync performance by retrying only the failed columns from other peers (pr:lighthouse#7733)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context/custody.rs:133-160`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L133-L160) on_data_column_downloaded keeps Downloaded columns and resets only the missing ones
- [`beacon_node/network/src/sync/network_context/custody.rs:229-262`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L229-L262) continue_requests re-requests only columns awaiting download, from other peers (peer_attempts)
- [`beacon_node/network/src/sync/block_sidecar_coupling.rs:256-263`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_sidecar_coupling.rs#L256-L263) range batch columns via custody_lookup_request with lookup_peers = {block_peer} only
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:976-984`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L976-L984) in range sync, CustodyPeerForColumn -&gt; peer_action None: 'Range sync tracks one peer per batch and drops the column PeerGroup while coupling'
- [`beacon_node/network/src/sync/range_sync/chain.rs:651-656`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L651-L656) NonFaultyFailure re-downloads the whole batch

**Skeptic check.** The earlier evidence was right for missing columns at download time (the custody.rs Status machine). It missed the processing-failure path: sync_methods.rs:976-984 explicitly drops column-peer attribution in range sync and turns the failure into a whole-batch retry.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lighthouse#7733](https://github.com/sigp/lighthouse/pull/7733), [lighthouse#7726](https://github.com/sigp/lighthouse/pull/7726), [lodestar#8387](https://github.com/ChainSafe/lodestar/pull/8387)

</details>


<a id="range_sync-082"></a>
<details>
<summary><b>range_sync-082</b> Per-peer locks around fetch rate limiter — <i>n/a · low · cpu, latency</i></summary>

**Idea.** Guard the sync fetcher's rate-limiter state with one lock per peer (pruning stale ones) instead of one global lock, so requests to different peers do not contend.

**Impact.** Lighthouse's rate limiters are owned by the single-task RPC behaviour, not shared behind a global mutex, so there is no lock contention.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/rate_limiter.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/rate_limiter.rs)
- [`beacon_node/lighthouse_network/src/rpc/self_limiter.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/self_limiter.rs)

**Sources.** [prysm#5906](https://github.com/OffchainLabs/prysm/pull/5906)

</details>


<a id="range_sync-083"></a>
<details>
<summary><b>range_sync-083</b> Re-trigger sync on a periodic timer — <i>implemented · low · S · sync, latency</i></summary>

**Idea.** Re-evaluate and restart the sync engine on a fixed timer in addition to peer status changes, so a node that is still behind with a stable peer set does not idle for minutes after a batch completes.

**Impact.** When a chain completes, its peers are re-statused at once, so a node that is still behind starts a new chain without the idle gap the Teku PR fixed.

**Best measured result.** restart takes ~5 minutes after 'Syncing completed' otherwise (pr:teku#9849)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/range.rs:361`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/range.rs#L361) on_chain_removed (including ChainCompleted) calls network.status_peers(chain.peers()) at once
- [`beacon_node/network/src/sync/range_sync/range.rs:374`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/range.rs#L374) chains.update with awaiting_head_peers after removal
- [`beacon_node/lighthouse_network/src/peer_manager/config.rs:2`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/config.rs#L2) DEFAULT_STATUS_INTERVAL=300 periodic re-status as fallback

**Skeptic check.** Lighthouse has no fixed sync timer. The problem the idea addresses (idle minutes after 'sync completed' while still behind) is still prevented: chain removal re-statuses that chain's peers at once. The earlier verdict holds.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#9849](https://github.com/Consensys-Incorporated/teku/pull/9849)

</details>


<a id="range_sync-084"></a>
<details>
<summary><b>range_sync-084</b> Peer-unbound worker pool keeps requests pipelined — <i>implemented · medium · S · sync, bandwidth</i></summary>

**Idea.** Use a pool of sync workers that each take a fresh available peer for every request and issue the next request as soon as any in-flight one completes, so slow peers do not stall the pipeline and peer bandwidth stays used.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain.rs:1188-1242`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L1188-L1242) include_next_batch keeps up to BATCH_BUFFER_SIZE=5 batches downloading or awaiting processing
- [`beacon_node/network/src/sync/range_sync/chain.rs:322`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L322),603 request_batches is called again on every block response and process result
- [`beacon_node/network/src/sync/network_context.rs:478-492`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L478-L492) each batch request picks a fresh peer from the pool, deprioritising failed peers and peers at the concurrency limit

**Skeptic check.** Confirmed that every completion refills the pipeline and that each request is bound to a newly chosen peer, not a fixed worker per peer. A slow head-of-line batch can still hold processing, as in any in-order design, but the 5-batch buffer keeps the other peers busy.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#117](https://github.com/status-im/nimbus-eth2/pull/117), [nimbus#1602](https://github.com/status-im/nimbus-eth2/pull/1602)

</details>


<a id="range_sync-085"></a>
<details>
<summary><b>range_sync-085</b> Buffer gossip blocks to disk while syncing — <i>not · low · L · sync, bandwidth</i></summary>

**Idea.** While syncing, buffer incoming gossip blocks in a disk-backed sorted collector and insert them in batches once the gap closes, so the tip does not need to be fetched again by forward sync.

**Gap in Lighthouse.** Would need a disk-backed buffer of gossip blocks while SyncState is syncing and a drain into the chain after range sync completes.

**Impact.** Lighthouse refetches the tip blocks via range/lookup after sync; saves a few blocks of download only, with large complexity.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/manager.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs) (unknown-parent leads to parent lookup)
- [`beacon_node/network/src/sync/range_sync/range.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/range.rs) (forward sync refetches head)
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs) (no sync buffering)

**Sources.** [caplin#9421](https://github.com/erigontech/erigon/pull/9421)

</details>


<a id="range_sync-086"></a>
<details>
<summary><b>range_sync-086</b> Materialize cached blocks before processing — <i>n/a · low · cpu</i></summary>

**Idea.** Copy blocks popped from the sync block cache into a separate sequence before processing them, so processing does not interfere with the cache while iterating.

**Impact.** Nim sequence copy semantics; Rust moves batch blocks into the processor with no iteration-aliasing issue.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs) (batches owned by value, handed to processor)

**Sources.** [nimbus#9131](https://github.com/status-im/nimbus-eth2/pull/9131)

</details>


<a id="range_sync-087"></a>
<details>
<summary><b>range_sync-087</b> Probe peers for range sync support — <i>not · low · M · sync, bandwidth</i></summary>

**Idea.** Send each peer one blocks-by-range probe at the finalized epoch and remember whether it can serve sync, so range sync does not waste requests on peers that cannot.

**Gap in Lighthouse.** Add a per-peer 'can serve BlocksByRange' flag set by a first probe request at the finalized epoch, consulted when SyncingChain picks peers in request_batches. Today a bad peer is only learned about after a real batch fails and is excluded for that batch.

**Impact.** Saves a few wasted batch requests and retries per bad peer during range sync; small and only on peers that cannot serve.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain.rs:1038`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L1038) batch.failed_peers() avoided on retry
- [`beacon_node/network/src/sync/range_sync/chain.rs:1124`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L1124) request_batches picks idle peers, no capability probe

**Sources.** [lodestar#1361](https://github.com/ChainSafe/lodestar/pull/1361)

</details>


<a id="range_sync-088"></a>
<details>
<summary><b>range_sync-088</b> Prune sync block buffer below finalized — <i>n/a · medium · memory</i></summary>

**Idea.** Periodically drop entries below the finalized epoch start slot from the by-root/sync block buffer so it does not grow without bound during sync.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/mod.rs:719`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L719) prune_lookups is time-based (no-peer and stuck lookups)
- [`beacon_node/network/src/sync/range_sync/chain.rs:1188`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L1188) range sync holds only bounded batches, no by-root block buffer

**Sources.** [nimbus@f969fffc9](https://github.com/status-im/nimbus-eth2/commit/f969fffc9482)

</details>


<a id="range_sync-089"></a>
<details>
<summary><b>range_sync-089</b> Purge stale head chains after one completes — <i>partial · low · S · sync, bandwidth</i></summary>

**Idea.** When a head chain finishes syncing, remove the other queued non-syncing head chains and re-status peers instead of syncing all of them to completion.

**Gap in Lighthouse.** The lighthouse#1538 mechanism (ChainCollection::clear_head_chains, called on head-chain completion to drop every non-syncing head chain and re-status its peers) no longer exists. Queued head chains whose target is an unknown (e.g. orphaned or superseded) root survive purge_outdated_chains and are later synced to completion.

**Impact.** Small: only matters in chaotic networks with many queued head chains; saves downloading stale head-chain batches after reaching head.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/range.rs:361`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/range.rs#L361) on_chain_removed re-statuses only the removed chain's peers
- [`beacon_node/network/src/sync/range_sync/chain_collection.rs:421-462`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain_collection.rs#L421-L462) purge_outdated_chains removes only chains whose target is finalized/known to fork choice or with zero peers
- [`beacon_node/network/src/sync/range_sync/chain_collection.rs:344-401`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain_collection.rs#L344-L401) update_head_chains keeps non-syncing head chains queued (stop_syncing) beyond PARALLEL_HEAD_CHAINS
- [`beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs:83-86`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs#L83-L86) periodic Status is suppressed while SyncingHead, so stale targets of queued chains are not refreshed

**Skeptic check.** Read the 1538 diff: it removed all non-syncing head chains on completion. Current code only purges chains with known/finalized targets or no peers, so the earlier evidence describes a related but narrower mechanism.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lighthouse#1538](https://github.com/sigp/lighthouse/pull/1538)

</details>


<a id="range_sync-090"></a>
<details>
<summary><b>range_sync-090</b> Drain queued messages before expiring batches — <i>n/a · low · S · cpu, sync</i></summary>

**Idea.** In the sync service loop, check for expired batches only after processing messages already received, so timeouts are not triggered by an overloaded queue.

**Impact.** Range-sync batch timeouts are RPC-layer timeouts delivered as messages, there is no sync-service batch-expiry check to reorder.

**Best measured result.** Solves the overwhelmed block_sync_service problem (commit:grandine@f0fbc941804c)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/manager.rs:805-845`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L805-L845) sync loop timers only prune lookups/custody requests; no batch expiry timer
- [`beacon_node/network/src/sync/range_sync/chain.rs:916`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L916) batch errors come as RPC error messages from the network layer

**Sources.** [grandine@f0fbc9418](https://github.com/grandinetech/grandine/commit/f0fbc941804c)

</details>


<a id="range_sync-091"></a>
<details>
<summary><b>range_sync-091</b> Range sync batch state machine with indexed lookups — <i>implemented · low · S · cpu, sync</i></summary>

**Idea.** Keep batches as a state machine in a sorted map keyed by id with a request-id map for O(1) lookups, and advance the chain on import instead of resetting it, so download progress is kept.

**Impact.** Already done.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain.rs:45`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L45) RangeSyncBatches = BTreeMap&lt;BatchId, BatchInfo&gt;
- [`beacon_node/network/src/sync/batch.rs:377-399`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/batch.rs#L377-L399) BatchState state machine transitions
- [`beacon_node/network/src/sync/range_sync/chain.rs:695`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L695) advance_chain drops validated batches and moves start_epoch
- [`beacon_node/network/src/sync/range_sync/chain_collection.rs:44`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain_collection.rs#L44) chains keyed by id in FnvHashMap

**Skeptic check.** Verified the sorted batch map, the explicit batch state machine, id-keyed chain lookup and advance_chain on validation; earlier evidence is right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#1628](https://github.com/sigp/lighthouse/pull/1628)

</details>


<a id="range_sync-092"></a>
<details>
<summary><b>range_sync-092</b> Narrow redownload range on batch retry — <i>partial · medium · S · sync, bandwidth</i></summary>

**Idea.** When a batch fails, retry from just past the last safe/imported slot and only widen the redownload window after repeated failures, instead of re-requesting a whole epoch or finalized data again.

**Gap in Lighthouse.** Narrowing exists at batch granularity (imported blocks advance the chain so earlier batches are not refetched, as in nimbus#3461), but within the failed batch Lighthouse re-requests the full epoch instead of from the first non-imported slot, and it widens to all unvalidated batches on the first zero-import failure rather than after repeated failures.

**Impact.** Small: saves refetching up to 32 blocks of a 1-epoch batch after partial import; failures are rare.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain.rs:619`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L619) on FaultyFailure with imported_blocks &gt; 0, advance_chain to the failed batch so only that batch is re-downloaded
- [`beacon_node/network/src/sync/range_sync/chain.rs:828`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L828) with no imports, all earlier unvalidated batches are marked for re-download (widen)
- [`beacon_node/network/src/sync/batch.rs:447`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/batch.rs#L447) to_blocks_by_range_request always requests the full batch start_slot..end_slot
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3355`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3355) already-imported blocks on retry return DuplicateFullyImported and are skipped

**Second check.** Checked the FaultyFailure path in range_sync/chain.rs: imported_blocks &gt; 0 triggers advance_chain, which is the core of the nimbus change at batch level; the earlier review only looked at batch.rs.

**Verdict history.** not (checked) → partial (refuted)

**Sources.** [nimbus#3461](https://github.com/status-im/nimbus-eth2/pull/3461), [grandine@b2bb3003e](https://github.com/grandinetech/grandine/commit/b2bb3003ec92), [lodestar#1246](https://github.com/ChainSafe/lodestar/pull/1246)

</details>


<a id="range_sync-093"></a>
<details>
<summary><b>range_sync-093</b> One-slot buffer between fetchers and processor — <i>implemented · low · S · memory, bandwidth</i></summary>

**Idea.** Since only one batch is processed at a time, give the fetch-to-process queue a one-batch buffer instead of letting all fetch workers push concurrently, so batches are not buffered and refetched for nothing.

**Impact.** None: downloads are bounded ahead of the single processor and buffered batches are not refetched unless processing fails.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain.rs:33`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L33) BATCH_BUFFER_SIZE = 5
- [`beacon_node/network/src/sync/range_sync/chain.rs:1198-1215`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L1198-L1215) request_batches stops when Downloading+AwaitingProcessing reach the buffer
- [`beacon_node/network/src/sync/range_sync/chain.rs:332-334`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L332-L334) only one batch processed at a time per chain

**Skeptic check.** The Prysm problem (concurrent fetchers flooding the processor queue and refetching) does not exist: Lighthouse caps in-flight plus waiting batches at 5 and processes them sequentially. The buffer is deliberately larger than one to pipeline downloads.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#6471](https://github.com/OffchainLabs/prysm/pull/6471)

</details>


<a id="range_sync-094"></a>
<details>
<summary><b>range_sync-094</b> Same retarget threshold after sync failure — <i>implemented · low · S · sync</i></summary>

**Idea.** After a sync failure, choose the next target chain with the normal better-target threshold, not a larger margin, so the node keeps syncing to head instead of leaving sync mode early.

**Impact.** After a chain fails, the next chain is picked by the same max-peers rule in update_finalized_chains; there is no larger margin on the failure path.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain_collection.rs:276-303`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain_collection.rs#L276-L303)
- [`beacon_node/network/src/sync/range_sync/range.rs:329-370`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/range.rs#L329-L370)

**Skeptic check.** Checked that on_chain_removed blacklists the failed target only, re-statuses its peers and calls chains.update, which uses the normal selection. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#3585](https://github.com/Consensys-Incorporated/teku/pull/3585)

</details>


<a id="range_sync-095"></a>
<details>
<summary><b>range_sync-095</b> Switch sync target only for more peers — <i>implemented · low · S · sync, bandwidth</i></summary>

**Idea.** Change the sync target chain only when the other chain has more peers, not only a higher head, so sync does not thrash between forks.

**Impact.** A finalized chain switch needs strictly more peers and more than MIN_FINALIZED_CHAIN_PROCESSED_EPOCHS processed; on a tie the current chain stays.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain_collection.rs:282-310`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain_collection.rs#L282-L310)

**Skeptic check.** Checked the switch condition in update_finalized_chains. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#3468](https://github.com/Consensys-Incorporated/teku/pull/3468)

</details>


<a id="range_sync-096"></a>
<details>
<summary><b>range_sync-096</b> Remove disconnected peer from all sync chains — <i>implemented · low · S · sync</i></summary>

**Idea.** On peer disconnect, remove that peer from every syncing chain's peer pool so no batches are assigned to it and sync does not stall.

**Impact.** Prevents stalls on disconnect.

**Best measured result.** stalled syncs no longer seen on Schlesi (pr:lighthouse#1150)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/manager.rs:548-571`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L548-L571) peer_disconnect calls range_sync.peer_disconnect and backfill_sync.peer_disconnected, then injects RPCError::Disconnected on every request of that peer
- [`beacon_node/network/src/sync/range_sync/range.rs:281-292`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/range.rs#L281-L292) remove_peer calls chain.remove_peer on all chains
- [`beacon_node/network/src/sync/range_sync/chain.rs:248-257`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L248-L257) SyncingChain::remove_peer; an empty pool returns EmptyPeerPool

**Skeptic check.** Confirmed that the peer is removed from every chain and that its in-flight batches are retried through the injected Disconnected errors. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#1150](https://github.com/sigp/lighthouse/pull/1150)

</details>


<a id="range_sync-097"></a>
<details>
<summary><b>range_sync-097</b> Start sync without waiting for peers — <i>implemented · low · S · sync, startup, latency</i></summary>

**Idea.** Begin range sync immediately with any suitable peers that exist and wait only when none are available, instead of always waiting for a peer-connect event or the best peer.

**Impact.** An Advanced peer from a Status goes straight into range_sync.add_peer, which creates or joins a chain and calls chains.update to start syncing at once.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/manager.rs:418-440`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L418-L440)
- [`beacon_node/network/src/sync/range_sync/range.rs:114-200`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/range.rs#L114-L200)

**Skeptic check.** Checked that sync starts without waiting for a best peer. Head chains do wait while a finalized sync runs (awaiting_head_peers), and that is intended ordering, not a peer wait. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@a18b86c11](https://github.com/ChainSafe/lodestar/commit/a18b86c11e2e), [lodestar@b627fbe78](https://github.com/ChainSafe/lodestar/commit/b627fbe787e3)

</details>


<a id="range_sync-098"></a>
<details>
<summary><b>range_sync-098</b> No watchdog that resets slow sync workers — <i>n/a · low · S · sync, bandwidth</i></summary>

**Idea.** Do not reset sync workers on a watchdog timer when processing is slow; on slow machines repeated resets discard downloaded work.

**Impact.** Lighthouse has no watchdog that resets sync workers on slow processing, so nothing to remove.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs) and range_sync/range.rs: grep for watchdog/timeout finds none that resets the chain; only per-request RPC timeouts

**Sources.** [nimbus#2247](https://github.com/status-im/nimbus-eth2/pull/2247)

</details>


<a id="range_sync-099"></a>
<details>
<summary><b>range_sync-099</b> Cheap slot check before DB lookup — <i>implemented · low · S · disk, cpu</i></summary>

**Idea.** In the already-processed block check, compare the block slot with the head slot first and only query the database when that cheap test is inconclusive.

**Impact.** None; the already-known check is slot comparisons plus an in-memory fork choice lookup, never a DB read.

**Best measured result.** avoids one DB lookup (pr:prysm#10620)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1925-1956`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1925-L1956) check_block_relevancy: future/genesis/finalized-slot checks then in-memory fork_choice contains_block, no DB read
- [`beacon_node/beacon_chain/src/block_verification.rs:1404`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1404),1446 range-sync (RpcBlock) and lookup paths both call check_block_relevancy first

**Skeptic check.** Verified check_block_relevancy uses cheap slot checks then fork choice (in memory) and is used on range sync and lookup import paths. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#10620](https://github.com/OffchainLabs/prysm/pull/10620)

</details>


<a id="range_sync-100"></a>
<details>
<summary><b>range_sync-100</b> Move fork-choice weight to new head during sync — <i>implemented · low · M · sync</i></summary>

**Idea.** While forward sync runs with no votes in fork choice, move proto-array weight from the stale head branch to the newly imported branch once it is well ahead, so sync does not keep extending a stale tip.

**Impact.** Teku's problem only exists because its fork choice has no votes during sync. Lighthouse applies block attestations with AttestationFromBlock::True and skips the current-time target-epoch check for them, so votes for old blocks reach proto-array and the head follows the synced branch.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1748-1780`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1748-L1780)
- [`consensus/fork_choice/src/fork_choice.rs:1325-1370`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1325-L1370)
- [`consensus/fork_choice/src/fork_choice.rs:1182`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1182)

**Skeptic check.** Checked that on_attestation from a block bypasses validate_target_epoch_against_current_time and calls process_attestation for past slots, so synced blocks carry weight. The earlier evidence is correct, and a teku-style weight transfer is not needed.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#9268](https://github.com/Consensys-Incorporated/teku/pull/9268)

</details>


<a id="range_sync-101"></a>
<details>
<summary><b>range_sync-101</b> Retry failed batch with a different peer — <i>implemented · medium · S · sync, bandwidth</i></summary>

**Idea.** When a sync request fails or returns an inconsistent range, return it to the queue as failed and assign it to a peer that has not been tried for it yet, instead of leaving it in flight or re-requesting from the same peer.

**Impact.** Failed batches are retried and routed to untried peers first in range sync, backfill, custody backfill and custody-by-root column fetches.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/batch.rs:203-215`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/batch.rs#L203-L215) failed_peers() from download and processing failures
- [`beacon_node/network/src/sync/range_sync/chain.rs:1038-1049`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L1038-L1049) send_batch passes failed_peers
- [`beacon_node/network/src/sync/network_context.rs:461-495`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L461-L495) block_components_by_range_request orders failed peers last
- [`beacon_node/network/src/sync/backfill_sync/mod.rs:888-894`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/backfill_sync/mod.rs#L888-L894) backfill does the same
- [`beacon_node/network/src/sync/network_context/custody.rs:353-395`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L353-L395) select_column_peer deprioritises by peer_attempts and caps at MAX_CUSTODY_PEER_ATTEMPTS

**Skeptic check.** Verified failed-peer deprioritisation on every by-range path and the per-peer attempt count on the Fulu custody-by-root column path. Earlier evidence was right; failed peers are deprioritised, not excluded, which still gives a different peer whenever one exists.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#7275](https://github.com/status-im/nimbus-eth2/pull/7275), [nimbus#5615](https://github.com/status-im/nimbus-eth2/pull/5615), [lodestar#9360](https://github.com/ChainSafe/lodestar/pull/9360), [lodestar@349982a1e](https://github.com/ChainSafe/lodestar/commit/349982a1e2a5)

</details>


<a id="range_sync-102"></a>
<details>
<summary><b>range_sync-102</b> Process synced blocks sequentially — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Run state transitions for received sync blocks one after another instead of starting them all in parallel, which wastes work and memory because each depends on its parent.

**Impact.** Segment signatures are verified in one batch, then each block goes through process_block one at a time with an await.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:3235-3380`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3235-L3380)

**Skeptic check.** Checked the sequential import loop in process_chain_segment. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#368](https://github.com/ChainSafe/lodestar/pull/368)

</details>


<a id="range_sync-103"></a>
<details>
<summary><b>range_sync-103</b> Sync from one best peer with large chunks — <i>implemented · low · S · bandwidth, sync</i></summary>

**Idea.** Choose a single best peer whose head is near the current slot and download large chunks from it, instead of splitting requests over several peers that return duplicate or conflicting blocks.

**Impact.** Each batch of blocks, blobs and envelopes comes from one peer. Custody columns are fetched by root for the blocks that arrived, so they cannot conflict. Batches do not overlap, so parallel peers return no duplicates.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context.rs:461-560`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L461-L560)
- [`beacon_node/network/src/sync/block_sidecar_coupling.rs:200-260`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_sidecar_coupling.rs#L200-L260)

**Skeptic check.** The design is different (disjoint batches spread over peers, not one best peer), but it removes the duplicate and conflicting responses that the idea targets. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@5961fabe9](https://github.com/ChainSafe/lodestar/commit/5961fabe9fc2), [prysm#2471](https://github.com/OffchainLabs/prysm/pull/2471)

</details>


<a id="range_sync-104"></a>
<details>
<summary><b>range_sync-104</b> Avoid state copies in sync path — <i>n/a · low · memory, cpu</i></summary>

**Idea.** Pass the head state and store states in the sync cache without copying, and copy only when a state is retrieved, so sync keeps one state instead of several copies.

**Impact.** n/a: Lighthouse states are persistent milhouse trees, cloned without copying

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain.rs:328`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L328) process_batch passes blocks only; states are milhouse persistent trees cloned cheaply

**Sources.** [prysm#5764](https://github.com/OffchainLabs/prysm/pull/5764)

</details>


<a id="range_sync-105"></a>
<details>
<summary><b>range_sync-105</b> Skip attestation processing for finalized sync blocks — <i>not · low · M · cpu, disk, sync</i></summary>

**Idea.** During initial sync, skip applying block attestations to fork choice and skip saving them (unless archival) for blocks that are already finalized.

**Gap in Lighthouse.** In the signature-verified block import in block_verification.rs (the fork choice attestation loop) skip get_indexed_attestation and on_attestation when the block slot is at or below the finalized slot or the block is far behind the wall clock (sync mode). Must keep attester slashings.

**Impact.** Saves per-block committee lookups and indexed-attestation building for up to 128 attestations on finalized historical blocks during forward sync; likely a few percent of per-block import time, only during sync.

**Best measured result.** only 10 blocks per second before (pr:prysm#4075)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1749-1780`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1749-L1780) import path always applies every block attestation via fork_choice.on_attestation (errors ignored)
- beacon_node/consensus/fork_choice/src/fork_choice.rs:1325 on_attestation does no finalized-block shortcut

**Sources.** [prysm#4075](https://github.com/OffchainLabs/prysm/pull/4075), [lodestar#2362](https://github.com/ChainSafe/lodestar/pull/2362)

</details>


<a id="range_sync-106"></a>
<details>
<summary><b>range_sync-106</b> Skip fork choice and head updates during catch-up — <i>partial · low · M · cpu, sync</i></summary>

**Idea.** While catching up to the peer head from finalized, only store downloaded blocks and skip fork choice and per-block head updates until caught up.

**Gap in Lighthouse.** Lighthouse updates head once per batch but still runs fork choice on_block and attestation application for every block, since proto-array must contain the blocks. Skipping that is not possible without breaking block processing.

**Impact.** Head update cost is already amortised per epoch batch; remaining fork choice on_block cost per block is small relative to state transition.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:647`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L647) recompute_head_at_current_slot once per segment, not per block
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3327`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3327) process_block still runs fork_choice.on_block per block

**Sources.** [prysm#2111](https://github.com/OffchainLabs/prysm/pull/2111), [prysm#2118](https://github.com/OffchainLabs/prysm/pull/2118)

</details>


<a id="range_sync-107"></a>
<details>
<summary><b>range_sync-107</b> Exclude payload-absent slots from column requests and DA — <i>implemented · low · S · sync, bandwidth, cpu</i></summary>

**Idea.** In ePBS range sync, request data columns and run data-availability checks only for blocks whose payload was revealed and is canonical, skipping empty or orphaned payload slots, so batches with such slots do not fail and redownload forever.

**Impact.** continue_requests waits for the envelope response and asks for custody columns only for revealed block roots. Blocks without an envelope couple as AvailableBlockData::NoData, so empty slots do not fail the batch.

**Best measured result.** Stalled node synced in about one minute after fix (pr:lodestar#9937)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_sidecar_coupling.rs:205-250`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_sidecar_coupling.rs#L205-L250)
- [`beacon_node/network/src/sync/block_sidecar_coupling.rs:470-500`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_sidecar_coupling.rs#L470-L500)

**Skeptic check.** The stall fix (empty-payload slots) is present. The 'canonical' part is weaker: a revealed-but-orphaned envelope still gets columns and DA, and range_sync-108 covers that.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#16976](https://github.com/OffchainLabs/prysm/pull/16976), [lodestar#9937](https://github.com/ChainSafe/lodestar/pull/9937), [lodestar#9471](https://github.com/ChainSafe/lodestar/pull/9471), [prysm#17049](https://github.com/OffchainLabs/prysm/pull/17049)

</details>


<a id="range_sync-108"></a>
<details>
<summary><b>range_sync-108</b> Skip importing orphaned payload envelopes — <i>partial · low · M · cpu, latency</i></summary>

**Idea.** During range sync of old blocks, skip DA verification and import of orphaned payload envelopes, which only add dead fork-choice variants and EL newPayload calls.

**Gap in Lighthouse.** Forward range sync has no orphan check. process_chain_segment passes every coupled envelope to process_range_sync_envelope (full verify, EL notify_new_payload, fork-choice import), and continue_requests asks for its custody columns. Nothing compares the child block's bid parent_block_hash with the envelope's block hash. Backfill does this check (historical_blocks.rs payload_revealed, 'Dropping backfilled envelope for withheld payload'). The fix: compute the same check in coupling or in process_chain_segment, and skip orphaned envelopes for old blocks.

**Impact.** Low. An orphaned envelope arrives only when a peer serves one by range, which canonical-only servers should not do. It costs a wasted newPayload, column fetch and DA. In Lighthouse it does not park the head, because block attestations give the EMPTY branch weight.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:3290-3380`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3290-L3380)
- [`beacon_node/beacon_chain/src/payload_envelope_verification/import.rs:420-470`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/import.rs#L420-L470)
- [`beacon_node/beacon_chain/src/historical_blocks.rs:222-251`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_blocks.rs#L222-L251)
- [`beacon_node/network/src/sync/block_sidecar_coupling.rs:205-250`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_sidecar_coupling.rs#L205-L250)

**Skeptic check.** The earlier evidence was wrong: coupling is by block root, so an orphaned envelope for a canonical block matches and is imported. 'Canonical only' depends on the remote peer, not on a local check. Backfill has the filter; forward sync does not.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lodestar#10005](https://github.com/ChainSafe/lodestar/pull/10005)

</details>


<a id="range_sync-109"></a>
<details>
<summary><b>range_sync-109</b> No blob wait outside DA window — <i>implemented · medium · S · latency, sync</i></summary>

**Idea.** For blocks outside the data availability window, mark data as available at once instead of waiting for blob sidecars and their timeout.

**Impact.** Range sync and backfill blocks outside the window import at once with no sidecar wait or timeout.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context.rs:1296-1320`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L1296-L1320) batch_type returns Blocks when outside the DA window
- [`beacon_node/beacon_chain/src/custody_context.rs:574-597`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L574-L597) da_check_required_for_epoch / blobs_required_for_block / data_columns_required_for_block
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:856-875`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L856-L875) AvailableBlock::new accepts NoData when not required
- [`beacon_node/beacon_chain/src/block_verification.rs:1407-1419`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1407-L1419) RpcBlock goes straight to MaybeAvailableBlock::Available

**Skeptic check.** Verified on the sync paths. The lookup/gossip path goes through the pending-components cache, where make_available keys on num_blobs_expected and not the DA window (overflow_lru_cache.rs:209), but blocks that old do not arrive by gossip and seldom by lookup, so this is not a hot path.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#9713](https://github.com/Consensys-Incorporated/teku/pull/9713)

</details>


<a id="range_sync-110"></a>
<details>
<summary><b>range_sync-110</b> Skip sidecars already on disk — <i>not · low · M · bandwidth, cpu</i></summary>

**Idea.** In range sync, do not request blob sidecars already stored locally, and in the availability check verify and save only the sidecars not already known.

**Gap in Lighthouse.** Range-sync batches would have to check the store/da_checker for blobs or columns already held for a block before building the blobs-by-range / custody-by-root request in block_components_by_range_request and RangeBlockComponentsRequest::continue_requests.

**Impact.** Only helps when resuming sync over blocks already stored but not finalized; saves some blob/column bandwidth in that rare case.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context.rs:949`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L949) custody_lookup_request with ignore_cache=true fetches all sampling columns
- [`beacon_node/network/src/sync/network_context.rs:1096`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L1096) send_blobs_by_range_request requests the whole range
- [`beacon_node/network/src/sync/range_sync/range.rs:187`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/range.rs#L187) finalized sync starts from min(local head, remote finalized) so most known blocks are skipped

**Sources.** [prysm#13827](https://github.com/OffchainLabs/prysm/pull/13827)

</details>


<a id="range_sync-111"></a>
<details>
<summary><b>range_sync-111</b> Serve stored SSZ bytes directly for by-range — <i>not · medium · L · cpu, memory</i></summary>

**Idea.** When serving blocks-by-range/root, send the stored SSZ bytes straight to the wire with only framing, instead of deserializing and reserializing each block, and take rate-limit quota per block.

**Gap in Lighthouse.** No raw-bytes response path: the store keeps blinded blocks with separate payloads, so the full block must be rebuilt and re-encoded. A bytes-carrying RpcSuccessResponse variant plus a store read of full-block SSZ would be needed; same for blob/column sidecars.

**Impact.** Saves one SSZ decode+encode per served block/sidecar; small CPU saving on serving nodes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1172`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1172) get_blocks via BeaconBlockStreamer yields decoded Arc&lt;SignedBeaconBlock&gt; (may hit EL for payloads)
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1193`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1193) Response::BlocksByRange(Some(block.clone()))
- [`beacon_node/lighthouse_network/src/rpc/codec.rs:75`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L75) encoder re-serializes every response with as_ssz_bytes; no raw-bytes variant

**Second check.** Checked the RPC codec encode path for every response type and the beacon_block_streamer; all go through typed objects and as_ssz_bytes, no byte passthrough anywhere.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [nimbus#3358](https://github.com/status-im/nimbus-eth2/pull/3358)

</details>


<a id="range_sync-112"></a>
<details>
<summary><b>range_sync-112</b> Skip long runs of empty slots quickly — <i>not · low · M · sync, bandwidth</i></summary>

**Idea.** When ranges return no blocks, advance the request window, or sample ahead with stepped by-range requests, to find the next non-empty slot instead of walking empty epochs batch by batch.

**Gap in Lighthouse.** Add a skip-ahead strategy in Chain request_batches/include_next_batch: after N consecutive empty batches, probe further ahead with a stepped request. Needs care with the parent-root linkage checks.

**Impact.** Only helps after very long runs of skipped slots (rare on mainnet); negligible normally.

**Best measured result.** handles 50K+ skipped slots (1600 epochs) (pr:prysm#5975)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain.rs:30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L30) EPOCHS_PER_BATCH=1 and :33 BATCH_BUFFER_SIZE=5 fixed epoch-by-epoch windows
- [`beacon_node/network/src/sync/range_sync/chain.rs:349`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L349) empty batches are sent through the processor, no skip-ahead sampling

**Sources.** [prysm#5284](https://github.com/OffchainLabs/prysm/pull/5284), [prysm#5975](https://github.com/OffchainLabs/prysm/pull/5975)

</details>


<a id="range_sync-113"></a>
<details>
<summary><b>range_sync-113</b> Skip local replay when far behind peers — <i>n/a · low · startup, sync</i></summary>

**Idea.** If peers' heads are far ahead of the local persisted state, sync from peers instead of first replaying the on-disk blocks.

**Impact.** Lighthouse restarts from the persisted head/fork choice and does not replay stored blocks before syncing, so there is nothing to skip.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/sync_type.rs:19`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/sync_type.rs#L19) sync type chosen from finalized epoch and fork-choice, no on-disk block replay phase

**Sources.** [silver#97](https://github.com/gattaca-com/silver/pull/97)

</details>


<a id="range_sync-114"></a>
<details>
<summary><b>range_sync-114</b> No extra delays in light client sync — <i>n/a · low · sync, latency</i></summary>

**Idea.** In light client sync, do not delay the next by-range request when a peer returns fewer periods than requested, and do not retry update fetches immediately on failure.

**Impact.** Lighthouse does not sync via light client updates.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync)/ no light client sync module (grep light_client found nothing)

**Sources.** [nimbus#5112](https://github.com/status-im/nimbus-eth2/pull/5112)

</details>


<a id="range_sync-115"></a>
<details>
<summary><b>range_sync-115</b> Skip newPayload for finalized sync blocks — <i>implemented · high · S · latency, sync</i></summary>

**Idea.** When syncing a finalized chain, import blocks as optimistic and skip the engine newPayload call, since finality already vouches for them, removing an EL round trip per block.

**Impact.** No EL round trip per block during finalized sync; only the local block-hash check remains.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:497-506`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L497-L506) NotifyExecutionLayer::No when is_syncing_finalized
- [`beacon_node/beacon_chain/src/execution_payload.rs:77-94`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/execution_payload.rs#L77-L94) returns PayloadVerificationStatus::Optimistic without newPayload
- [`beacon_node/beacon_chain/src/execution_payload.rs:117-130`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/execution_payload.rs#L117-L130) notify_new_payload short-circuits on precomputed status
- [`beacon_node/beacon_chain/src/chain_config.rs:168`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/chain_config.rs#L168) optimistic_finalized_sync default true
- [`beacon_node/beacon_chain/src/payload_envelope_verification/payload_notifier.rs:33`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/payload_notifier.rs#L33) same for Gloas envelopes

**Skeptic check.** This is Lighthouse's own PR #3738, which is still in place, is on by default, and also covers Gloas payload envelopes. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#3738](https://github.com/sigp/lighthouse/pull/3738)

</details>


<a id="range_sync-116"></a>
<details>
<summary><b>range_sync-116</b> Skip snapshot downloads below retained range — <i>n/a · low · disk, bandwidth, startup</i></summary>

**Idea.** On pruned nodes, do not download block snapshot files older than the retained range, and delete old ones at retirement.

**Impact.** Lighthouse has no block snapshot files; backfill uses RPC by range.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/backfill_sync`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/backfill_sync)/ backfill fetches blocks by range, no snapshot files (no era/snapshot code found)

**Sources.** [caplin#10165](https://github.com/erigontech/erigon/pull/10165)

</details>


<a id="range_sync-117"></a>
<details>
<summary><b>range_sync-117</b> Bootstrap from downloaded beacon snapshots — <i>not · low · L · startup, sync</i></summary>

**Idea.** Bootstrap the beacon chain history by downloading prebuilt snapshot files instead of replaying it block by block from the network.

**Gap in Lighthouse.** Would need an era-file or snapshot importer that writes blocks into the hot/cold DB and feeds backfill. A new feature, plus a trust and distribution story.

**Impact.** Would make historical backfill after checkpoint sync cheaper in peer bandwidth and time, but backfill is low priority work and only matters for nodes that want full history.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/backfill_sync`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/backfill_sync)/ history comes from by-range RPC
- grep for era files found none in repo

**Sources.** [caplin#11250](https://github.com/erigontech/erigon/pull/11250)

</details>


<a id="range_sync-118"></a>
<details>
<summary><b>range_sync-118</b> Avoid importing orphaned blocks in initial sync — <i>n/a · low · sync, cpu</i></summary>

**Idea.** During initial sync, do not import blocks that are not on the canonical chain and avoid request timeouts that stall sync.

**Impact.** Blocks-by-range returns only the peer's canonical chain and finalized sync targets a finalized root, so orphans are not requested; the Lodestar fix was for its own import path.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/range.rs:136`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/range.rs#L136) finalized sync targets the peer's finalized root
- network/src/sync/network_context/requests/blocks_by_range.rs:24 by-range responses validated for slot range

**Sources.** [lodestar#1786](https://github.com/ChainSafe/lodestar/pull/1786)

</details>


<a id="range_sync-119"></a>
<details>
<summary><b>range_sync-119</b> Skip finalized sync phase when already there — <i>n/a · low · startup, sync</i></summary>

**Idea.** Skip the finalized-checkpoint sync phase when the head is already in the finalized epoch, so checkpoint-synced nodes go straight to head sync.

**Impact.** Lighthouse chooses finalized vs head sync from finalized epoch and fork-choice knowledge, not head slot, so a freshly checkpoint-synced node at the same finalized epoch already goes to head sync.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/sync_type.rs:27`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/sync_type.rs#L27) Finalized only if remote finalized epoch &gt; local and root unknown to fork choice
- network/src/sync/range_sync/range.rs:134 chain starts at local finalized epoch

**Sources.** [prysm#13083](https://github.com/OffchainLabs/prysm/pull/13083)

</details>


<a id="range_sync-120"></a>
<details>
<summary><b>range_sync-120</b> Skip block verification up to trusted finality — <i>partial · medium · M · cpu, sync</i></summary>

**Idea.** During initial sync to a trusted finalized checkpoint, skip most block signature (and other content) verification, with an option to verify everything.

**Gap in Lighthouse.** The goal (do not fully verify history up to a trusted finalized checkpoint) is met by checkpoint sync + light backfill, which is the default way Lighthouse syncs. Missing only for genesis sync: there is no no-verify mode up to a peer- or user-supplied finalized checkpoint, and forward sync from the anchor to head always verifies everything.

**Impact.** For checkpoint-synced nodes (the common case) the saving already exists in a stronger form; adding Prysm's mode would only help genesis syncs/archive nodes, with a security trade-off.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/client/src/builder.rs:423`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L423) ClientGenesis::CheckpointSyncUrl starts from a trusted finalized state, so no block before the trusted checkpoint is ever state-transitioned or fully verified
- [`beacon_node/beacon_chain/src/builder.rs:406`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L406) weak_subjectivity_state anchors the chain at the trusted checkpoint
- [`beacon_node/beacon_chain/src/historical_blocks.rs:398`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_blocks.rs#L398) backfill below the checkpoint only verifies proposer signatures (batched) plus hash linkage, no body signatures or state transition
- [`beacon_node/beacon_chain/src/block_verification.rs:671`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L671) forward range sync above the anchor always verifies all signatures

**Second check.** Earlier review only looked at forward-sync signature verification; checkpoint sync is an equivalent mechanism that skips all work up to a trusted finalized checkpoint, and backfill verifies only proposer signatures, so I rate it partial.

**Verdict history.** not (checked) → partial (refuted)

**Sources.** [prysm#4179](https://github.com/OffchainLabs/prysm/pull/4179), [prysm#3586](https://github.com/OffchainLabs/prysm/pull/3586)

</details>


<a id="range_sync-121"></a>
<details>
<summary><b>range_sync-121</b> Bound column retry for withheld origin payloads — <i>n/a · low · S · cpu</i></summary>

**Idea.** Do not retry fetching an origin block's data columns forever when its payload may be withheld; give up or skip the prefetch so the loop does not spin the CPU and downscore peers.

**Impact.** None today: no Gloas payload envelope or withheld-payload path exists in sync, and column fetches have a bounded retry count, so no 100% CPU spin.

**Best measured result.** 5M+ attempts in 7 minutes at 100% CPU (pr:prysm#17458)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/client/src/builder.rs:404`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L404) - origin blobs/columns are left to backfill, no origin column prefetch loop
- [`beacon_node/network/src/sync/network_context/custody.rs:245`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L245) - custody column download bounded by MAX_CUSTODY_COLUMN_DOWNLOAD_ATTEMPTS=3
- [`beacon_node/network/src/sync/network_context/custody.rs:395`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L395) - constant of 3 attempts

**Sources.** [prysm#17458](https://github.com/OffchainLabs/prysm/pull/17458)

</details>


<a id="range_sync-122"></a>
<details>
<summary><b>range_sync-122</b> Use smaller range sync batches — <i>implemented · medium · S · sync, bandwidth</i></summary>

**Idea.** Use smaller range sync batches (about one or two epochs or fewer) so a failed batch is cheap to retry, peers are not overwhelmed, and less data is requested redundantly.

**Impact.** Batches are one epoch on both forward and backfill sync.

**Best measured result.** 2000 blobs is ~250 MB per minute per peer max (pr:teku#8982)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain.rs:30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L30) EPOCHS_PER_BATCH = 1
- [`beacon_node/network/src/sync/network_context.rs:1298-1303`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L1298-L1303) compile-time assert that range and backfill batches are 1 epoch

**Skeptic check.** Verified one-epoch batches, enforced by a const assert for both range and backfill sync. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#1812](https://github.com/sigp/lighthouse/pull/1812), [prysm#5128](https://github.com/OffchainLabs/prysm/pull/5128), [teku#8982](https://github.com/Consensys-Incorporated/teku/pull/8982), [grandine@846e07ee7](https://github.com/grandinetech/grandine/commit/846e07ee7949), [grandine#96](https://github.com/grandinetech/grandine/pull/96), [nimbus#988](https://github.com/status-im/nimbus-eth2/pull/988)

</details>


<a id="range_sync-123"></a>
<details>
<summary><b>range_sync-123</b> Speculative background sync of forks — <i>partial · low · M · sync</i></summary>

**Idea.** During non-finality, sync forks with several pending blocks in the background without leaving in-sync mode, so all forks are explored.

**Gap in Lighthouse.** Forks with a head within SLOT_IMPORT_TOLERANCE of ours are treated as FullySynced and only explored by parent lookups (depth-capped). A background range sync for forks with many pending blocks would be needed; edit remote_sync_type and the lookup depth-exceeded path.

**Impact.** Only helps during long non-finality; rare on mainnet.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/peer_sync_info.rs:45`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/peer_sync_info.rs#L45) peer on a different head with equal finalized epoch and unknown head is Advanced -&gt; head chain sync
- network/src/sync/range_sync/range.rs:171 head chain created per peer target
- network/src/sync/block_lookups/mod.rs:59 parent lookups limited by PARENT_DEPTH_TOLERANCE

**Sources.** [teku#3476](https://github.com/Consensys-Incorporated/teku/pull/3476)

</details>


<a id="range_sync-124"></a>
<details>
<summary><b>range_sync-124</b> Stop reading response at requested count — <i>implemented · low · S · bandwidth, sync</i></summary>

**Idea.** Stop reading a blocks-by-range response stream once the requested count is reached and return the blocks read, instead of reading more chunks and discarding the whole response.

**Impact.** None left: response completes at the requested count and extra chunks are dropped without discarding the blocks read.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context/requests/blocks_by_range.rs:25-43`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/requests/blocks_by_range.rs#L25-L43) add() returns true when items.len() &gt;= count
- [`beacon_node/network/src/sync/network_context/requests.rs:126-135`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/requests.rs#L126-L135) Ok(true) consumes items and moves to State::CompletedEarly, returning blocks immediately
- [`beacon_node/network/src/sync/network_context/requests.rs:146`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/requests.rs#L146) CompletedEarly ignores later chunks

**Skeptic check.** Verified the ActiveRequests state machine returns the accumulated blocks as soon as count is reached and ignores the rest. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#17717](https://github.com/OffchainLabs/prysm/pull/17717)

</details>


<a id="range_sync-125"></a>
<details>
<summary><b>range_sync-125</b> Wake backpressured workers on reset — <i>n/a · low · S · sync</i></summary>

**Idea.** Make sync workers that block on backpressure wake when the queue is reset, and score missing-parent and invalid chunks differently.

**Impact.** Lighthouse range sync is event-driven with a batch state machine (chain.rs), not blocked worker tasks; no backpressure wakeup exists to fix.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain.rs:334`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L334) batches pulled by chain state, no blocking worker queue

**Sources.** [nimbus#1072](https://github.com/status-im/nimbus-eth2/pull/1072)

</details>


<a id="range_sync-126"></a>
<details>
<summary><b>range_sync-126</b> Sync from finalized state, not head state — <i>implemented · low · S · startup, cpu</i></summary>

**Idea.** Have syncing nodes request the finalized state (by finalized state root), which is stable, cacheable and stored, instead of the moving head state.

**Impact.** None: Lighthouse never fetches a moving head state over p2p; checkpoint sync anchors on the finalized state.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/client/src/builder.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs) checkpoint sync downloads the finalized state by checkpoint
- [`beacon_node/network/src/sync/range_sync/chain.rs:194`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L194) finalized chains target the finalized checkpoint

**Skeptic check.** The prysm idea (request finalized rather than head state during initial sync) maps to Lighthouse checkpoint sync from the finalized state; range sync replays blocks rather than requesting states. Earlier verdict upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#1955](https://github.com/OffchainLabs/prysm/pull/1955)

</details>


<a id="range_sync-127"></a>
<details>
<summary><b>range_sync-127</b> Sync engine rewrite — <i>n/a · low · S · sync</i></summary>

**Idea.** Replace range, head and orphan sync with a single new sync engine (mechanism not described in the source).

**Impact.** Source describes no mechanism, so there is nothing concrete to compare.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/range.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/range.rs), manager.rs

**Sources.** [silver#195](https://github.com/gattaca-com/silver/pull/195), [nimbus#7921](https://github.com/status-im/nimbus-eth2/pull/7921)

</details>


<a id="range_sync-128"></a>
<details>
<summary><b>range_sync-128</b> Query peer heads less often, concurrently — <i>implemented · low · S · bandwidth, cpu</i></summary>

**Idea.** Poll peers for their chain head at a lower rate and handle responses concurrently instead of a serial loop every second.

**Impact.** None: peers are re-statused every 300s on independent timers; responses are handled as async events, not a serial loop.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/config.rs:2`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/config.rs#L2) DEFAULT_STATUS_INTERVAL = 300
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:90`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L90),196 status_peers HashSetDelay with per-peer expiry
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:405`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L405),943 re-insert after status

**Skeptic check.** Verified the 300s per-peer delay queue; status responses arrive as independent RPC events. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#2178](https://github.com/OffchainLabs/prysm/pull/2178)

</details>


<a id="range_sync-129"></a>
<details>
<summary><b>range_sync-129</b> Keep synced blocks tree-backed — <i>n/a · low · S · cpu, sync</i></summary>

**Idea.** Keep blocks received over RPC and gossip in their tree-backed SSZ representation instead of converting them to plain objects, so sync avoids conversion and rehashing.

**Impact.** Lighthouse blocks are plain structs decoded once from SSZ; the tree-backed conversion cost is Lodestar-specific.

**Best measured result.** Pyrmont sync 22/21.5 min to 17.5/18 min (pr:lodestar#1861)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/codec.rs:75`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L75) SSZ decode to plain Rust types

**Sources.** [lodestar#1861](https://github.com/ChainSafe/lodestar/pull/1861)

</details>


<a id="range_sync-130"></a>
<details>
<summary><b>range_sync-130</b> Do not pre-filter peers for column sync — <i>implemented · low · S · sync</i></summary>

**Idea.** Pass all candidate peers to the column-by-range request logic and let it filter per request, instead of pre-restricting initial sync to a small peer set, and do not block responses waiting for unavailable data.

**Impact.** Column peer choice is per column over all custodial peers; there is no supernode-only or small fixed pre-filter.

**Best measured result.** "initial sync takes hours" with peer filtering (pr:prysm#14482)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context.rs:540-545`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L540-L545) Fulu range batches fetch custody columns by root after blocks arrive
- [`beacon_node/network/src/sync/network_context/custody.rs:353-395`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L353-L395) select_column_peer draws from all custodial peers (get_custodial_peers), prioritising lookup peers, filtering per column
- [`beacon_node/network/src/sync/network_context.rs:578-620`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L578-L620) select_columns_by_range_peers_to_request filters per column (custody backfill)
- [`beacon_node/network/src/sync/custody_backfill_sync/mod.rs:1037-1060`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/custody_backfill_sync/mod.rs#L1037-L1060) custody backfill passes all synced peers

**Skeptic check.** The earlier evidence cited the by-range selector, which forward sync now uses only for custody backfill. Forward Fulu sync uses custody-by-root with select_column_peer over all custodial peers, which is an even wider set. The verdict stands.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#14482](https://github.com/OffchainLabs/prysm/pull/14482), [prysm#15242](https://github.com/OffchainLabs/prysm/pull/15242)

</details>


<a id="range_sync-131"></a>
<details>
<summary><b>range_sync-131</b> Larger download lookahead window — <i>partial · medium · S · sync, latency</i></summary>

**Idea.** Let the forward downloader run further ahead of the processed head (larger slots-ahead window or unbounded rolling download), so the pipeline stays full during catch-up.

**Gap in Lighthouse.** Download runs ahead of processing, but only by a fixed 5 one-epoch batches. Raising the limit or making it adaptive (peer count, processing speed, memory for columns) is not done.

**Impact.** Keeps the pipeline fuller when downloads are slow relative to processing; likely small since processing usually dominates.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain.rs:30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L30) EPOCHS_PER_BATCH = 1
- [`beacon_node/network/src/sync/range_sync/chain.rs:33`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L33) BATCH_BUFFER_SIZE = 5
- [`beacon_node/network/src/sync/range_sync/chain.rs:1188`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L1188) include_next_batch caps Downloading+AwaitingProcessing batches at the buffer size; AwaitingValidation not counted

**Second check.** Confirmed constants and buffer logic; the custody backfill has the same fixed 5-batch buffer; no adaptive or unbounded lookahead elsewhere.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [caplin#9383](https://github.com/erigontech/erigon/pull/9383), [grandine@8401b5069](https://github.com/grandinetech/grandine/commit/8401b506957f)

</details>


<a id="range_sync-132"></a>
<details>
<summary><b>range_sync-132</b> Unified peer-driven block and sidecar fetch loop — <i>not · medium · L · sync, bandwidth</i></summary>

**Idea.** Use one peer-driven loop that fetches blocks with their sidecars, by-root near head and by-range further back, with adaptive status refresh, instead of separate range and by-root managers.

**Gap in Lighthouse.** Unifying RangeSync/BackFillSync/BlockLookups into one per-peer loop choosing by-root vs by-range by distance from finality would be a sync manager redesign.

**Impact.** Mostly simplicity/robustness; no clear CPU or bandwidth saving.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/range.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/range.rs) RangeSync is a separate manager
- [`beacon_node/network/src/sync/manager.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs) separately drives range sync, backfill, custody backfill and block_lookups

**Second check.** Lighthouse already couples blocks with sidecars in both range and lookup requests, but via separate state machines, not one peer-driven loop.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [nimbus#7578](https://github.com/status-im/nimbus-eth2/pull/7578)

</details>


<a id="range_sync-133"></a>
<details>
<summary><b>range_sync-133</b> Verify proposer signature first in range sync — <i>not · medium · S · cpu</i></summary>

**Idea.** For each range sync block, verify the proposer signature against the claimed proposer index using only the pubkey cache before parent load, state advance, KZG and body signatures, so invalid batches fail cheaply.

**Gap in Lighthouse.** Add a first pass verifying each block's proposer signature against the pubkey cache by proposer_index before load_parent/state advance/KZG (upstream PR #10462, not merged in this base).

**Impact.** Junk or invalid batches fail before parent load, state advance and KZG; no saving on honest batches.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:680`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L680) load_parent before any signature check
- [`beacon_node/beacon_chain/src/block_verification.rs:689`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L689) cheap_state_advance_to_obtain_committees before signatures
- [`beacon_node/beacon_chain/src/block_verification.rs:705`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L705) KZG column verification before signatures
- [`beacon_node/beacon_chain/src/block_verification.rs:719`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L719) proposer signature only checked inside the full batch verifier

**Second check.** Searched network sync and beacon_chain for any early proposer-signature check in the range path; only gossip columns and backfill verify proposer signatures standalone.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [lighthouse#10462](https://github.com/sigp/lighthouse/pull/10462)

</details>


<a id="range_sync-134"></a>
<details>
<summary><b>range_sync-134</b> Wait for in-flight import before retargeting — <i>n/a · low · S · sync</i></summary>

**Idea.** When restarting sync on a new target chain, wait for the in-flight import to finish before computing the common ancestor, so requests do not fail with unknown parent.

**Impact.** Lighthouse chains do not compute a common ancestor on retarget; a chain keeps one in-flight batch, and a new target creates a separate chain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain.rs:133`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L133),147 processing_target and single current_processing_batch
- chain.rs:334,389 no new batch is processed while one is in flight

**Sources.** [teku#2884](https://github.com/Consensys-Incorporated/teku/pull/2884)

</details>


<a id="range_sync-135"></a>
<details>
<summary><b>range_sync-135</b> Compute custody peer pool once per retry round — <i>partial · medium · M · cpu, bandwidth</i></summary>

**Idea.** Compute the list of custodial peers once per retry round and consume it across batches, giving each peer at most one column request, and batch by-root column requests when not synced.

**Gap in Lighthouse.** Cross-batch load spreading exists only as a soft tiebreak: ActiveRequestsPerPeer (global in-flight count, limit 2 per protocol) deprioritizes but never excludes busy peers, and the custodial peer list is recomputed per column per batch rather than built once per retry round and consumed so each peer gets at most one column request across concurrent batches.

**Impact.** Small: slightly more even peer load and fewer stacked column requests during Fulu range sync; Lighthouse already groups columns per peer and batches by-root requests.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_sidecar_coupling.rs:256-264`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_sidecar_coupling.rs#L256-L264) range batch issues one custody by-root lookup carrying all block roots of the batch
- [`beacon_node/network/src/sync/network_context/custody.rs:232-295`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L232-L295) columns grouped per peer into one DataColumnsByRoot request per peer per round
- [`beacon_node/network/src/sync/network_context/custody.rs:353-391`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L353-L391) select_column_peer recomputes custodial peers per column; deprioritizes peers at concurrency limit and by attempt count
- [`beacon_node/network/src/sync/network_context.rs:97-119`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L97-L119) ActiveRequestsPerPeer counts in-flight requests across all batches/lookups
- [`beacon_node/lighthouse_network/src/rpc/mod.rs:51`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/mod.rs#L51) MAX_CONCURRENT_REQUESTS = 2
- [`beacon_node/network/src/sync/network_context.rs:578-631`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L578-L631) by-range column peer selection, also per-column with concurrency deprioritization

**Second check.** Beyond the earlier review, checked ActiveRequestsPerPeer/MAX_CONCURRENT_REQUESTS, which is a global cross-batch per-peer budget but soft (sort key, limit 2), and the by-range selector used by custody backfill; neither builds a shared once-per-round pool, so partial stands.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [grandine@28f28818f](https://github.com/grandinetech/grandine/commit/28f28818fca6)

</details>


<a id="range_sync-136"></a>
<details>
<summary><b>range_sync-136</b> Ban peers that serve invalid blocks in sync — <i>implemented · low · S · sync, bandwidth</i></summary>

**Idea.** When a peer returns blocks that fail validation during range sync, ban or heavily downscore it and stop assigning it further requests. This avoids repeated round trips to peers that cannot help.

**Impact.** Peers serving invalid batches are downscored (banned below threshold by the peer manager) and avoided for retries of the batch.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:806`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L806) handle_failed_chain_segment maps BlockError to PeerAction (LowToleranceError, Fatal)
- [`beacon_node/network/src/sync/range_sync/chain.rs:608`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L608) FaultyFailure -&gt; network.report_peer(peer, penalty, faulty_batch)
- [`beacon_node/network/src/sync/range_sync/chain.rs:643`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L643) chain dropped and all peers penalised after retry limit
- [`beacon_node/network/src/sync/batch.rs:203`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/batch.rs#L203) failed_peers() passed to send_batch at chain.rs:1038 to avoid the faulty peer on retry

**Skeptic check.** Verified the penalty path and failed_peers exclusion in send_batch; earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#7411](https://github.com/erigontech/erigon/pull/7411)

</details>


<a id="range_sync-137"></a>
<details>
<summary><b>range_sync-137</b> Abort rest of batch after first invalid block — <i>implemented · low · S · cpu, sync</i></summary>

**Idea.** When processing a sync batch, stop at the first block that fails as invalid instead of processing the remaining blocks, which descend from the bad one. This saves state transitions on doomed blocks.

**Impact.** Blocks after the first invalid one in a segment are never state-transitioned.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:3366`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3366) process_block Err -&gt; return ChainSegmentResult::Failed immediately
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3310`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3310) signature verification failure returns early
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3227`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3227) filter_chain_segment error returns early

**Skeptic check.** process_chain_segment returns on the first block or envelope error; this is the Lighthouse source commit itself.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@a3ca3ec50](https://github.com/sigp/lighthouse/commit/a3ca3ec50d10)

</details>


<a id="range_sync-138"></a>
<details>
<summary><b>range_sync-138</b> Use only sync peers whose head is ahead of ours — <i>implemented · low · S · sync</i></summary>

**Idea.** Exclude peers whose reported head is not ahead of the local head from range-sync peer sets and target selection. Requests are not wasted on peers that cannot serve needed blocks or on empty ranges.

**Impact.** Behind and synced peers never join range-sync chains.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/peer_sync_info.rs:26`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/peer_sync_info.rs#L26) remote_sync_type classifies Behind/FullySynced/Advanced by finalized epoch and head slot
- [`beacon_node/network/src/sync/manager.rs:435`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L435) only PeerSyncType::Advanced calls range_sync.add_peer; Behind does nothing

**Skeptic check.** Verified the classification and dispatch in add_peer handling; earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#1417](https://github.com/ChainSafe/lodestar/pull/1417), [lodestar#1252](https://github.com/ChainSafe/lodestar/pull/1252)

</details>


<a id="range_sync-139"></a>
<details>
<summary><b>range_sync-139</b> Minimal block-processing path for synced blocks — <i>implemented · low · S · sync, cpu, bandwidth</i></summary>

**Idea.** Give initial sync a lean import path that does only validity checks, state transition and cleanup, without per-block gossip re-broadcast or other regular-sync overhead.

**Impact.** Range sync uses a dedicated segment import path without gossip checks or re-broadcast.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:3202`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3202) process_chain_segment: filter, per-epoch batched signature verification, direct process_block
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3334`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3334) BlockImportSource::RangeSync, no gossip verification or republish
- [`beacon_node/beacon_chain/src/block_verification.rs:680`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L680) signature_verify_chain_segment uses one cheap state advance for committees and one batch signature verify

**Skeptic check.** Confirmed segment path skips gossip verification and publishing; earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#2124](https://github.com/OffchainLabs/prysm/pull/2124)

</details>


<a id="range_sync-140"></a>
<details>
<summary><b>range_sync-140</b> Verify batch data availability in parallel with execution — <i>partial · low · M · latency, sync</i></summary>

**Idea.** During range sync, start data availability checks for the whole batch concurrently with state transition and signature verification instead of serially.

**Gap in Lighthouse.** Column KZG verification for an epoch chunk runs before, not concurrently with, that chunk's signature verification and state transitions, and is not pipelined with import of the previous chunk. Data is coupled with blocks at download time, so there is no DA wait to overlap; only KZG compute could be overlapped (spawn KZG of chunk N+1 while chunk N imports, or run KZG alongside the signature batch).

**Impact.** Small: KZG cell verification is already rayon-parallel across column indices and BLS batch verify is also parallel, so overlapping two CPU-saturating workloads mostly reorders work; gains limited to hiding KZG behind single-threaded state transition, maybe a few percent of batch time on blob-heavy ranges.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:699`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L699) verify_columns_against_block runs per block inside signature_verify_chain_segment, before the batched signature verify at :713-722 (serial, same blocking task)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3300`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3300) signature_verify_chain_segment awaited per epoch chunk, then blocks imported serially via process_block at :3322
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:639`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L639) verify_columns_against_block -&gt; verify_kzg_for_data_column_list / validate_data_columns_with_commitments
- [`crypto/kzg/src/lib.rs:222`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/kzg/src/lib.rs#L222) verify_cell_proof_batch groups cells by column index and verifies groups with rayon into_par_iter (:263), so column KZG already uses all cores
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:495`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L495) batch_verify_kzg_for_range_sync_blocks used only by backfill

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [lodestar#9242](https://github.com/ChainSafe/lodestar/pull/9242)

</details>


<a id="range_sync-141"></a>
<details>
<summary><b>range_sync-141</b> Await data availability once per payload segment — <i>implemented · low · S · sync</i></summary>

**Idea.** In range sync, wait for data availability once for a whole segment of payload envelopes and then import each directly, instead of waiting per payload in a queue.

**Impact.** No per-payload availability waiting in range sync; columns come with the envelope and are checked inline.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:3376`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3376) envelope processed directly after its block in the segment loop
- [`beacon_node/beacon_chain/src/payload_envelope_verification/import.rs:420`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/import.rs#L420) process_range_sync_envelope imports directly, no DA checker wait
- [`beacon_node/beacon_chain/src/block_verification.rs:704`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L704) columns KZG-verified inline in signature_verify_chain_segment

**Skeptic check.** No DA queue at all on the range-sync envelope path, which subsumes the idea; earlier claim that columns are verified 'once for the whole chunk' is imprecise (verify_columns_against_block runs per block), but that is not the idea.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#9269](https://github.com/ChainSafe/lodestar/pull/9269)

</details>


<a id="range_sync-142"></a>
<details>
<summary><b>range_sync-142</b> Rank sync peers by request-outcome score — <i>partial · low · M · sync</i></summary>

**Idea.** Keep a per-peer score for block-serving reliability updated from request outcomes, and use it to pick a limited set of peers and assign sync batches, avoiding slow or faulty peers.

**Gap in Lighthouse.** Peer choice uses only the batch's failed-peer set, concurrency and random tie-break; no per-peer success/latency/throughput score. Add a score field to chain peers updated in on_block_response/BatchProcessResult and sort by it in block_components_by_range_request and select_columns_by_range_peers_to_request.

**Impact.** Avoids assigning batches to slow peers during initial sync; gain depends on peer quality, probably modest.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context.rs:578`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L578) select_columns_by_range_peers_to_request orders by failed-peer flag, concurrency limit, random
- [`beacon_node/network/src/sync/range_sync/chain.rs:1038`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L1038) send_batch passes failed_peers
- [`beacon_node/network/src/sync/range_sync/chain.rs:608`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L608) penalties feed the global peer score used by the peer manager

**Sources.** [lodestar#1545](https://github.com/ChainSafe/lodestar/pull/1545), [lodestar@93d014538](https://github.com/ChainSafe/lodestar/commit/93d014538952)

</details>


<a id="range_sync-143"></a>
<details>
<summary><b>range_sync-143</b> Persist snapshot download state to skip re-downloads — <i>n/a · low · startup, sync, bandwidth</i></summary>

**Idea.** Record completed snapshot downloads (flag, per-type lock file or download database) so restarts, upgrades and downgrades do not look up or re-request already downloaded files.

**Impact.** Lighthouse does not download snapshot files via a torrent downloader, so there is no download state to persist. Checkpoint sync is a single HTTP fetch.

**Best measured result.** For mumbai retrieving torrent info can take up to 15mins even after download is completed. (pr:caplin#9311)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/range.rs:77`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/range.rs#L77) range sync is RPC based, no torrent snapshot download

**Sources.** [caplin#9766](https://github.com/erigontech/erigon/pull/9766), [caplin#9311](https://github.com/erigontech/erigon/pull/9311), [caplin#8939](https://github.com/erigontech/erigon/pull/8939)

</details>


<a id="range_sync-144"></a>
<details>
<summary><b>range_sync-144</b> Remember roots of blocks that failed processing — <i>partial · low · S · cpu, sync</i></summary>

**Idea.** In tip sync, add the root of a block that failed processing to a seen-roots set so it is not fetched and processed again in a retry loop.

**Gap in Lighthouse.** Block lookups do not record roots whose block failed processing as invalid: BlockLookups::on_processing_result -&gt; on_block_processing_result -&gt; on_processing_failure re-downloads and re-processes the same (content-addressed, so deterministically invalid) root from other peers up to SINGLE_BLOCK_LOOKUP_MAX_ATTEMPTS, and after the drop a new UnknownBlockHashFromAttestation/unknown-parent from another peer (or after debounce expiry) creates a fresh lookup. Insert the root into ignored_chains (or a beacon-chain invalid-root cache) on a BlockError that is a block-validity failure.

**Impact.** Avoids repeated download and state transition of a known-invalid block in tip sync; only matters under attack or on bad forks.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/mod.rs:282`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L282) ignored_chains is only inserted for parent chains that are too long (PARENT_DEPTH_TOLERANCE), not for processing failures
- [`beacon_node/network/src/sync/block_lookups/single_block_lookup.rs:980`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/single_block_lookup.rs#L980) on_processing_failure re-downloads the same root up to SINGLE_BLOCK_LOOKUP_MAX_ATTEMPTS
- [`beacon_node/network/src/sync/block_lookups/mod.rs:616`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L616) drop_lookup_and_children forgets the root after TooManyAttempts
- [`beacon_node/network/src/sync/manager.rs:922`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L922) notified_unknown_roots only debounces per (peer, root)
- [`beacon_node/network/src/sync/range_sync/range.rs:352`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/range.rs#L352) failed_chains keyed by chain target head root (range sync only)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3879`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3879) check_invalid_block_roots is a static config set

**Skeptic check.** The earlier evidence was wrong: ignored_chains is only filled for chain_too_long, not for failed processing, and failed_chains in range sync is keyed by chain target, not by the failing block.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [caplin#19923](https://github.com/erigontech/erigon/pull/19923)

</details>


<a id="range_sync-145"></a>
<details>
<summary><b>range_sync-145</b> Keep re-statusing peers in their sync head chains — <i>not · low · S · sync, cpu</i></summary>

**Idea.** When a peer sends a new status, update it in place rather than removing it from syncing head chains, so chains are not torn down and rebuilt.

**Gap in Lighthouse.** In RangeSync::add_peer Head arm, skip remove_peer when the peer is already in a head chain with the same target (head_root, head_slot), or add before removing from the others, so a sole-peer chain is not dropped and rebuilt and its batches are kept.

**Impact.** Avoids dropping and recreating a head chain (and its in-flight batches) when a sole peer re-statuses to a new head, which reduces head-chain churn. Small gain, only while head-syncing.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/range.rs:177`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/range.rs#L177) Head arm calls self.remove_peer before add_peer_or_create_chain
- [`beacon_node/network/src/sync/range_sync/chain.rs:248`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L248) remove_peer returns EmptyPeerPool when last peer leaves
- [`beacon_node/network/src/sync/range_sync/range.rs:139`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/range.rs#L139) Finalized arm keeps the peer in chains (only that path avoids it)

**Sources.** [lighthouse#1840](https://github.com/sigp/lighthouse/pull/1840)

</details>


<a id="range_sync-146"></a>
<details>
<summary><b>range_sync-146</b> Gate validator duties on sync status at startup — <i>partial · low · S · sync, startup, cpu</i></summary>

**Idea.** Hold duty computation and validator-facing work behind a sync-status tracker that stays in a start-up state until enough peers, a timeout, or sync start, so early requests do not force processing of many blocks.

**Gap in Lighthouse.** At startup sync_state is Stalled and the filter lets duty requests through, so a stale head can be asked for duties before peers arrive. Make not_while_syncing_filter also reject Stalled when head_slot lags the clock by more than the tolerance.

**Impact.** Avoids a validator client forcing long state advances on a stale head during the first seconds after start. Small and rare.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs:475`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L475) not_while_syncing_filter rejects duties only in SyncingFinalized/SyncingHead beyond sync_tolerance_epochs
- [`beacon_node/http_api/src/lib.rs:509`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L509) SyncState::Stalled =&gt; Ok(())
- [`beacon_node/lighthouse_network/src/types/globals.rs:95`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/globals.rs#L95) sync_state starts as Stalled

**Sources.** [teku#1605](https://github.com/Consensys-Incorporated/teku/pull/1605)

</details>


