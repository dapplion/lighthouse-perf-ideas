# range_sync

58 ideas: 11 not, 12 partial, 32 implemented, 3 n/a; 16 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

The area has 135 numbered ideas; the 77 ids missing here have not been checked against Lighthouse yet.

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [range_sync-001](#range_sync-001) | Send forkchoiceUpdated once per sync batch | implemented | high | S | latency, sync |
| [range_sync-002](#range_sync-002) | Pipeline batch download concurrently with import | implemented | low |  | latency, sync |
| [range_sync-003](#range_sync-003) | Self rate-limit outgoing by-range requests per peer | implemented | medium | S | bandwidth, latency, sync |
| [range_sync-005](#range_sync-005) **★** | Filter sync peers by earliest available slot | partial | medium | S | bandwidth, sync |
| [range_sync-006](#range_sync-006) | Skip range requests for already known or queued blocks | implemented | low |  | sync, bandwidth |
| [range_sync-007](#range_sync-007) **★** | Clip sidecar requests to DA window and fork | partial | medium | S | bandwidth, sync |
| [range_sync-008](#range_sync-008) | Choose range or by-root sync by distance | implemented | low |  | bandwidth, sync |
| [range_sync-011](#range_sync-011) | Batch-verify signatures across a whole sync segment | implemented | low |  | cpu, sync |
| [range_sync-012](#range_sync-012) | Couple block and sidecar downloads per batch | implemented | medium | S | bandwidth, cpu, latency, sync |
| [range_sync-013](#range_sync-013) | Request sidecars only for blocks with commitments | implemented | low |  | bandwidth, sync |
| [range_sync-016](#range_sync-016) | Request blocks in ranged batches, not singly | implemented | low |  | sync, latency, bandwidth |
| [range_sync-017](#range_sync-017) | Use larger blocks-per-request batch size | not | low | M | sync, latency |
| [range_sync-018](#range_sync-018) | Cap items per outgoing by-range request | implemented | low |  | memory, sync |
| [range_sync-019](#range_sync-019) | Bound download lookahead ahead of processing | implemented | low |  | bandwidth, memory |
| [range_sync-020](#range_sync-020) | Cap concurrent in-flight sync requests per peer | partial | low | S | bandwidth, latency, sync |
| [range_sync-031](#range_sync-031) | Skip per-slot tick work while syncing | implemented | medium |  | cpu, sync |
| [range_sync-035](#range_sync-035) **★** | Sync columns from minimal covering peer set | not | medium | S | bandwidth, sync |
| [range_sync-038](#range_sync-038) **★** | Do not advance sync on unverified empty responses | partial | medium | S | sync, bandwidth |
| [range_sync-039](#range_sync-039) | Ignore gossip blocks as sync triggers while range syncing | implemented | low |  | sync, cpu, bandwidth |
| [range_sync-045](#range_sync-045) | Cheap batch attempt hashing | implemented | low |  | cpu, memory |
| [range_sync-049](#range_sync-049) | Check batch is parent-linked chain before import | implemented | medium |  | cpu, sync |
| [range_sync-054](#range_sync-054) | Align sync batches to epoch boundaries | implemented | medium |  | cpu |
| [range_sync-056](#range_sync-056) | Keep latest state in memory during initial sync | implemented | high | S | disk, sync |
| [range_sync-057](#range_sync-057) | Download ranges from several peers in parallel | implemented | medium |  | bandwidth, latency, sync |
| [range_sync-059](#range_sync-059) **★** | Find common ancestor instead of restarting at finalized | partial | medium | M | sync, bandwidth |
| [range_sync-061](#range_sync-061) | Rank finalized sync peers by finalized epoch | partial | low | S | sync |
| [range_sync-062](#range_sync-062) | Start range requests after blocks already held | not | low | S | bandwidth, cpu, sync |
| [range_sync-064](#range_sync-064) | Skip already-imported blocks before batch processing | implemented | low |  | cpu, disk, sync |
| [range_sync-070](#range_sync-070) **★** | Save synced blocks to DB concurrently | not | medium | L | sync, cpu, disk |
| [range_sync-071](#range_sync-071) **★** | Verify execution payload in parallel with block | not | medium | M | latency, sync, cpu |
| [range_sync-073](#range_sync-073) | Do not count non-fault failures against batch retries | partial | low | S | sync, bandwidth |
| [range_sync-074](#range_sync-074) **★** | Score sync peers by observed throughput | not | high | M | sync, bandwidth |
| [range_sync-075](#range_sync-075) **★** | Weighted round robin on peer rate-limit capacity | partial | medium | M | sync, bandwidth |
| [range_sync-076](#range_sync-076) | Randomize sync peer selection | implemented | low | S | sync, bandwidth |
| [range_sync-078](#range_sync-078) | Wait for full custody subnet coverage before column batches | implemented | medium |  | sync, bandwidth |
| [range_sync-079](#range_sync-079) | Pool peers per chain and load-balance batches | implemented | medium |  | sync, bandwidth |
| [range_sync-081](#range_sync-081) | Keep partial column responses, retry only missing columns | implemented | medium |  | sync, bandwidth |
| [range_sync-083](#range_sync-083) | Re-trigger sync on a periodic timer | implemented | low | S | sync, latency |
| [range_sync-084](#range_sync-084) | Peer-unbound worker pool keeps requests pipelined | implemented | medium |  | sync, bandwidth |
| [range_sync-088](#range_sync-088) | Prune sync block buffer below finalized | n/a | medium |  | memory |
| [range_sync-090](#range_sync-090) | Drain queued messages before expiring batches | n/a | low | S | cpu, sync |
| [range_sync-092](#range_sync-092) **★** | Narrow redownload range on batch retry | partial | medium | S | sync, bandwidth |
| [range_sync-096](#range_sync-096) | Remove disconnected peer from all sync chains | implemented | low | S | sync |
| [range_sync-099](#range_sync-099) | Cheap slot check before DB lookup | implemented | low | S | disk, cpu |
| [range_sync-101](#range_sync-101) | Retry failed batch with a different peer | implemented | medium | S | sync, bandwidth |
| [range_sync-105](#range_sync-105) | Skip attestation processing for finalized sync blocks | not | low | M | cpu, disk, sync |
| [range_sync-109](#range_sync-109) | No blob wait outside DA window | implemented | medium | S | latency, sync |
| [range_sync-111](#range_sync-111) **★** | Serve stored SSZ bytes directly for by-range | not | medium | L | cpu, memory |
| [range_sync-112](#range_sync-112) | Skip long runs of empty slots quickly | not | low | M | sync, bandwidth |
| [range_sync-115](#range_sync-115) | Skip newPayload for finalized sync blocks | implemented | high | S | latency, sync |
| [range_sync-120](#range_sync-120) **★** | Skip block verification up to trusted finality | partial | medium | M | cpu, sync |
| [range_sync-121](#range_sync-121) | Bound column retry for withheld origin payloads | n/a | low | S | cpu |
| [range_sync-122](#range_sync-122) | Use smaller range sync batches | implemented | medium | S | sync, bandwidth |
| [range_sync-130](#range_sync-130) | Do not pre-filter peers for column sync | implemented | low | S | sync |
| [range_sync-131](#range_sync-131) **★** | Larger download lookahead window | partial | medium | S | sync, latency |
| [range_sync-132](#range_sync-132) **★** | Unified peer-driven block and sidecar fetch loop | not | medium | L | sync, bandwidth |
| [range_sync-133](#range_sync-133) **★** | Verify proposer signature first in range sync | not | medium | S | cpu |
| [range_sync-135](#range_sync-135) **★** | Compute custody peer pool once per retry round | partial | medium | M | cpu, bandwidth |

★ actionable. Click an id for the full record.

## Ideas

<a id="range_sync-001"></a>
<details>
<summary><b>range_sync-001</b> Send forkchoiceUpdated once per sync batch — <i>implemented · high · S · latency, sync</i></summary>

**Idea.** During range/initial sync, do not send engine forkchoiceUpdated after every imported block; send it once per batch (for its last block, in the background) or once at the end of sync. This cuts EL round trips during bulk import.

**Impact.** Already one fcU per batch; it is awaited rather than backgrounded, a small remaining cost.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:632-660`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L632-L660) process_blocks calls recompute_head_at_current_slot once after process_chain_segment
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3320-3350`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3320-L3350) per-block loop calls process_block with no head recompute
- [`beacon_node/beacon_chain/src/canonical_head.rs:1909`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1909) fcU issued only from recompute_head

**Sources.** [prysm#17109](https://github.com/OffchainLabs/prysm/pull/17109), [prysm#10520](https://github.com/OffchainLabs/prysm/pull/10520), [prysm#16199](https://github.com/OffchainLabs/prysm/pull/16199)

</details>


<a id="range_sync-002"></a>
<details>
<summary><b>range_sync-002</b> Pipeline batch download concurrently with import — <i>implemented · low · latency, sync</i></summary>

**Idea.** Decouple range-sync block fetching from block processing with a queue or batch state machine, so the next batches download from peers while earlier batches are imported in order. Network wait and import overlap instead of alternating.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain.rs:33`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L33) BATCH_BUFFER_SIZE=5 batches queued ahead
- network/src/sync/range_sync/chain.rs:474 processing_target/to_be_downloaded advance separately

**Sources.** [prysm#5148](https://github.com/OffchainLabs/prysm/pull/5148), [prysm#4978](https://github.com/OffchainLabs/prysm/pull/4978), [lodestar#1961](https://github.com/ChainSafe/lodestar/pull/1961), [prysm#4931](https://github.com/OffchainLabs/prysm/pull/4931), [prysm#5096](https://github.com/OffchainLabs/prysm/pull/5096), [prysm#5064](https://github.com/OffchainLabs/prysm/pull/5064), [lodestar#1685](https://github.com/ChainSafe/lodestar/pull/1685), [lodestar@927005cf8](https://github.com/ChainSafe/lodestar/commit/927005cf899c), [prysm#4965](https://github.com/OffchainLabs/prysm/pull/4965), [prysm#5286](https://github.com/OffchainLabs/prysm/pull/5286)

</details>


<a id="range_sync-003"></a>
<details>
<summary><b>range_sync-003</b> Self rate-limit outgoing by-range requests per peer — <i>implemented · medium · S · bandwidth, latency, sync</i></summary>

**Idea.** Throttle outgoing blocks/blobs-by-range requests to each peer to the quota that peer enforces, counting cost the way the responder does (slots times max blobs, adjusted for empty slots), and schedule a retry exactly when the quota replenishes. Requests are not rejected, penalised or disconnected, and the node does not wait longer than needed.

**Gap in Lighthouse.** Cost does not adjust for empty slots, and quotas are our configured ones, not learned from the peer.

**Impact.** Avoids rate-limit penalties on sync peers; throttling already exists, so little extra gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/self_limiter.rs:34-130`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/self_limiter.rs#L34-L130) SelfRateLimiter queues and retries via DelayQueue at wait_time
- [`beacon_node/lighthouse_network/src/rpc/rate_limiter.rs:394-399`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/rate_limiter.rs#L394-L399) cost = max_responses
- [`beacon_node/lighthouse_network/src/rpc/protocol.rs:858-866`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/protocol.rs#L858-L866) BlocksByRange count, BlobsByRange max_blobs_requested

**Sources.** [teku#8984](https://github.com/Consensys-Incorporated/teku/pull/8984), [teku#6604](https://github.com/Consensys-Incorporated/teku/pull/6604), [prysm#4637](https://github.com/OffchainLabs/prysm/pull/4637), [teku#2822](https://github.com/Consensys-Incorporated/teku/pull/2822), [prysm#11853](https://github.com/OffchainLabs/prysm/pull/11853)

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

**Sources.** [grandine@4db1043b5](https://github.com/grandinetech/grandine/commit/4db1043b56fa), [grandine#411](https://github.com/grandinetech/grandine/pull/411), [prysm#17602](https://github.com/OffchainLabs/prysm/pull/17602), [prysm#17770](https://github.com/OffchainLabs/prysm/pull/17770), [grandine@57da4967a](https://github.com/grandinetech/grandine/commit/57da4967a7f4), [nimbus#9127](https://github.com/status-im/nimbus-eth2/pull/9127)

</details>


<a id="range_sync-006"></a>
<details>
<summary><b>range_sync-006</b> Skip range requests for already known or queued blocks — <i>implemented · low · sync, bandwidth</i></summary>

**Idea.** When new block roots or gossip blocks arrive during sync, check whether the block or its parent is already known or queued (keyed by root) and only request the span that is new. This avoids duplicate downloads and lookups.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/peer_sync_info.rs:49-80`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/peer_sync_info.rs#L49-L80) remote_sync_type skips peers whose head is known to fork choice
- [`beacon_node/network/src/sync/manager.rs:451`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L451) unknown head goes to by-root lookup only if not known
- [`beacon_node/network/src/sync/range_sync/sync_type.rs:28`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/sync_type.rs#L28) Finalized only if finalized root unknown

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

**Sources.** [silver#320](https://github.com/gattaca-com/silver/pull/320), [nimbus#7039](https://github.com/status-im/nimbus-eth2/pull/7039), [teku#6779](https://github.com/Consensys-Incorporated/teku/pull/6779), [grandine#413](https://github.com/grandinetech/grandine/pull/413), [grandine#811](https://github.com/grandinetech/grandine/pull/811)

</details>


<a id="range_sync-008"></a>
<details>
<summary><b>range_sync-008</b> Choose range or by-root sync by distance — <i>implemented · low · bandwidth, sync</i></summary>

**Idea.** When a peer is only a few slots or epochs ahead, use head sync or by-root fetches instead of a full finalized range sync; when it is further behind, fetch the gap with blocks-by-range at max request size instead of many by-root requests. Each gap size uses the cheaper method.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/peer_sync_info.rs:26-80`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/peer_sync_info.rs#L26-L80) Behind/FullySynced/Advanced by distance with SLOT_IMPORT_TOLERANCE
- [`beacon_node/network/src/sync/manager.rs:432-455`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L432-L455) FullySynced with unknown head uses by-root lookup, Advanced uses range sync

**Sources.** [lighthouse#1258](https://github.com/sigp/lighthouse/pull/1258), [nimbus@9dca55917](https://github.com/status-im/nimbus-eth2/commit/9dca559173c8), [ethlambda#351](https://github.com/lambdaclass/ethlambda/pull/351)

</details>


<a id="range_sync-011"></a>
<details>
<summary><b>range_sync-011</b> Batch-verify signatures across a whole sync segment — <i>implemented · low · cpu, sync</i></summary>

**Idea.** Pass a complete downloaded range-sync batch to the chain as one segment, collect the signature sets of all its blocks and verify them in one batched BLS job (in worker threads) alongside the state transition. One batched verification is much cheaper than per-block verification.

**Best measured result.** Quoted: verifyImport 3.6543 s/op vs 6.6473 s/op (ratio 0.55); roughly 8s to 4s for 32 blocks (pr:lodestar#3989)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:671-740`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L671-L740) signature_verify_chain_segment collects all block signature sets into one verifier and verifies once
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3202`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3202) process_chain_segment

**Sources.** [lodestar#3989](https://github.com/ChainSafe/lodestar/pull/3989), [prysm#6470](https://github.com/OffchainLabs/prysm/pull/6470), [prysm#6469](https://github.com/OffchainLabs/prysm/pull/6469), [lodestar@f699d7fcc](https://github.com/ChainSafe/lodestar/commit/f699d7fccd2f)

</details>


<a id="range_sync-012"></a>
<details>
<summary><b>range_sync-012</b> Couple block and sidecar downloads per batch — <i>implemented · medium · S · bandwidth, cpu, latency, sync</i></summary>

**Idea.** For each range-sync batch, request blocks and blob/column sidecars concurrently, buffer them until all are complete, and submit the batch to the processor only when fully downloaded, storing sidecars before importing their blocks. Import does not refetch sidecars or fail on partial batches.

**Gap in Lighthouse.** Columns are fetched by custody-by-root after blocks, not by range, but batches are still submitted only when complete.

**Impact.** Already avoids partial-batch import and refetch.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_sidecar_coupling.rs:28-38`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_sidecar_coupling.rs#L28-L38) RangeBlockComponentsRequest buffers blocks+blobs/columns/envelopes until complete
- [`beacon_node/network/src/sync/block_sidecar_coupling.rs:295-356`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_sidecar_coupling.rs#L295-L356) responses() returns coupled RangeSyncBlocks
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3320`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3320) process_chain_segment imports already-coupled blocks

**Sources.** [teku#6982](https://github.com/Consensys-Incorporated/teku/pull/6982), [teku#6684](https://github.com/Consensys-Incorporated/teku/pull/6684), [nimbus#8842](https://github.com/status-im/nimbus-eth2/pull/8842), [lodestar#5053](https://github.com/ChainSafe/lodestar/pull/5053), [lodestar#8032](https://github.com/ChainSafe/lodestar/pull/8032)

</details>


<a id="range_sync-013"></a>
<details>
<summary><b>range_sync-013</b> Request sidecars only for blocks with commitments — <i>implemented · low · bandwidth, sync</i></summary>

**Idea.** When building blob or data-column by-range requests, skip blocks (and whole batches) without KZG commitments and missed slots, and request only the (block, column) pairs still missing per peer instead of the union over the range.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_sidecar_coupling.rs:238-252`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_sidecar_coupling.rs#L238-L252) only blocks with num_expected_blobs()&gt;0 get custody requests; empty batch skips fetching
- [`beacon_node/network/src/sync/network_context.rs:493-540`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L493-L540) blobs by range only for BlocksAndBlobs batch type

**Sources.** [prysm#14843](https://github.com/OffchainLabs/prysm/pull/14843), [prysm#14522](https://github.com/OffchainLabs/prysm/pull/14522), [nimbus#6121](https://github.com/status-im/nimbus-eth2/pull/6121)

</details>


<a id="range_sync-016"></a>
<details>
<summary><b>range_sync-016</b> Request blocks in ranged batches, not singly — <i>implemented · low · sync, latency, bandwidth</i></summary>

**Idea.** During sync, request and serve many blocks per BlocksByRange message in bounded chunks and import them in bulk, instead of one block per request/response. This cuts round trips.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain.rs:30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L30) EPOCHS_PER_BATCH=1, one BlocksByRange of up to 32 blocks per request
- [`beacon_node/network/src/sync/network_context.rs:461`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L461) block_components_by_range_request

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
<summary><b>range_sync-018</b> Cap items per outgoing by-range request — <i>implemented · low · memory, sync</i></summary>

**Idea.** Limit the number of blocks or columns per by-range request (for example 512 column items) and page through larger ranges, so responders do not reject oversized requests and responses stay bounded in memory.

**Impact.** Requests are structurally bounded to one epoch; nothing further to gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain.rs:30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L30) EPOCHS_PER_BATCH=1 so each by-range request is 32 slots
- [`beacon_node/network/src/sync/batch.rs:448`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/batch.rs#L448) to_blocks_by_range_request count=end-start
- Fulu columns fetched by custody-by-root after blocks arrive (network_context.rs:~540 comment), no large by-range column requests

**Sources.** [teku#1061](https://github.com/Consensys-Incorporated/teku/pull/1061), [nimbus@65ca74c98](https://github.com/status-im/nimbus-eth2/commit/65ca74c9807d), [prysm#14495](https://github.com/OffchainLabs/prysm/pull/14495)

</details>


<a id="range_sync-019"></a>
<details>
<summary><b>range_sync-019</b> Bound download lookahead ahead of processing — <i>implemented · low · bandwidth, memory</i></summary>

**Idea.** Limit how many range-sync batches or slots are downloaded ahead of the processed head (for example 4 batches, or a bounded slot window started when the previous target is processed), and enforce that limit in the send path. This bounds memory and wasted bandwidth when a batch fails.

**Impact.** Bounds memory and wasted bandwidth already.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain.rs:33`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L33) BATCH_BUFFER_SIZE=5
- [`beacon_node/network/src/sync/range_sync/chain.rs:1188-1215`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L1188-L1215) include_next_batch counts Downloading\|AwaitingProcessing against the buffer

**Sources.** [lighthouse#4720](https://github.com/sigp/lighthouse/pull/4720), [prysm#13599](https://github.com/OffchainLabs/prysm/pull/13599), [lodestar@76e1ca231](https://github.com/ChainSafe/lodestar/commit/76e1ca2312a8)

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


<a id="range_sync-031"></a>
<details>
<summary><b>range_sync-031</b> Skip per-slot tick work while syncing — <i>implemented · medium · cpu, sync</i></summary>

**Idea.** Maintain a cheap is-syncing flag set as soon as sync starts, and have per-slot tick handlers read it to skip fork choice, duties and other per-slot work during sync, instead of computing a full peer-based sync status each tick. Resources go to catching up.

**Impact.** Already skips per-slot fork choice during sync with a cheap local slot comparison; no peer-based status computed in the tick.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:7491`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7491) per_slot_task returns early when best_slot + MAX_PER_SLOT_FORK_CHOICE_DISTANCE &lt; slot (before recompute_head_at_current_slot)

**Sources.** [teku#1470](https://github.com/Consensys-Incorporated/teku/pull/1470), [teku#1484](https://github.com/Consensys-Incorporated/teku/pull/1484), [teku#1406](https://github.com/Consensys-Incorporated/teku/pull/1406), [teku#1405](https://github.com/Consensys-Incorporated/teku/pull/1405)

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

**Sources.** [grandine#329](https://github.com/grandinetech/grandine/pull/329)

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

**Sources.** [nimbus#7197](https://github.com/status-im/nimbus-eth2/pull/7197), [nimbus#7318](https://github.com/status-im/nimbus-eth2/pull/7318)

</details>


<a id="range_sync-039"></a>
<details>
<summary><b>range_sync-039</b> Ignore gossip blocks as sync triggers while range syncing — <i>implemented · low · sync, cpu, bandwidth</i></summary>

**Idea.** During initial/range sync, do not subscribe to or act on gossip blocks for triggering fetches; trigger new range requests only from blocks sync itself imported. This avoids duplicate processing and spurious requests.

**Impact.** Gossip blocks do not drive range requests during initial sync.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/manager.rs:772-780`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L772-L780) subscribe_core_topics only once sync state is Synced
- [`beacon_node/network/src/sync/manager.rs:1156-1175`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L1156-L1175) should_search_for_block ignores unknown-block triggers far from head when not synced

**Sources.** [lodestar@dbf397621](https://github.com/ChainSafe/lodestar/commit/dbf397621b06), [lodestar#1618](https://github.com/ChainSafe/lodestar/pull/1618), [lodestar@d1af8dfb4](https://github.com/ChainSafe/lodestar/commit/d1af8dfb4e00), [prysm#2524](https://github.com/OffchainLabs/prysm/pull/2524)

</details>


<a id="range_sync-045"></a>
<details>
<summary><b>range_sync-045</b> Cheap batch attempt hashing — <i>implemented · low · cpu, memory</i></summary>

**Idea.** Compute the identity hash of a downloaded sync batch from block tree-hash roots (cached per block/envelope) concatenated into one preallocated buffer, instead of SSZ-serialising blocks or manual byte loops. This avoids large temporary allocations.

**Impact.** No SSZ serialisation or large buffers; already the cheap form.

**Best measured result.** byteArrayConcat 2.03 ns/op vs Buffer.concat 1.35 ns/op (pr:lodestar#4343)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain.rs:65-69`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L65-L69) batch_attempt_hash uses DefaultHasher over the data
- [`beacon_node/beacon_chain/src/block_verification_types.rs:63-66`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification_types.rs#L63-L66) Hash for RangeSyncBlock hashes only the cached block_root

**Sources.** [lodestar#9686](https://github.com/ChainSafe/lodestar/pull/9686), [lighthouse#2916](https://github.com/sigp/lighthouse/pull/2916), [lodestar#4343](https://github.com/ChainSafe/lodestar/pull/4343)

</details>


<a id="range_sync-049"></a>
<details>
<summary><b>range_sync-049</b> Check batch is parent-linked chain before import — <i>implemented · medium · cpu, sync</i></summary>

**Idea.** Sort a downloaded batch and verify that each block's parent root links to the previous block before any state transition; reject the batch and switch away from the peer on failure. Invalid or orphaned batches are rejected cheaply.

**Impact.** Already cheap-rejects non-linked batches; the check is in beacon_chain, not in the sync layer before queueing, but is before any heavy work.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:3079-3112`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3079-L3112) filter_chain_segment checks block_root == child parent_root and strictly increasing slots (NonLinearParentRoots/NonLinearSlots) before signature verification or state transition
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:960`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L960) NonLinearParentRoots mapped to peer-fault

**Sources.** [lodestar#1736](https://github.com/ChainSafe/lodestar/pull/1736), [lodestar@51675fad0](https://github.com/ChainSafe/lodestar/commit/51675fad027e), [caplin#6243](https://github.com/erigontech/erigon/pull/6243)

</details>


<a id="range_sync-054"></a>
<details>
<summary><b>range_sync-054</b> Align sync batches to epoch boundaries — <i>implemented · medium · cpu</i></summary>

**Idea.** Choose range-sync batch boundaries so all blocks in a processing segment are in the same epoch, so they share one shuffling/committee cache for batch signature verification.

**Impact.** Batches are epoch-aligned and segments split by epoch, so one shuffling is used per signature-verification batch.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain.rs:30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L30) EPOCHS_PER_BATCH=1, batch ids are epochs
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3236-3245`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3236-L3245) segment partitioned into same-epoch runs for signature verification
- [`beacon_node/beacon_chain/src/block_verification.rs:668`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L668) signature_verify_chain_segment requires same epoch

**Sources.** [lodestar#4322](https://github.com/ChainSafe/lodestar/pull/4322)

</details>


<a id="range_sync-056"></a>
<details>
<summary><b>range_sync-056</b> Keep latest state in memory during initial sync — <i>implemented · high · S · disk, sync</i></summary>

**Idea.** During initial sync, keep the latest state in an in-memory cache instead of writing the state to the database after every block.

**Impact.** Full states are not written per block; only a small summary, plus a diff/snapshot at hdiff layer boundaries.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1667`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1667) store_hot_state puts state into state_cache
- [`beacon_node/store/src/hot_cold_store.rs:1749-1757`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1749-L1757) only summary written; full state/diff only at hierarchy boundaries
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4752`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4752) PutState per block

**Sources.** [prysm#4199](https://github.com/OffchainLabs/prysm/pull/4199)

</details>


<a id="range_sync-057"></a>
<details>
<summary><b>range_sync-057</b> Download ranges from several peers in parallel — <i>implemented · medium · bandwidth, latency, sync</i></summary>

**Idea.** Track the heads of all suitable peers and send block-by-range requests to several of them concurrently (round-robin), instead of syncing serially from a single peer. Total download time is bounded by the slowest parallel request, not the sum.

**Impact.** Batches from a chain's peer set are downloaded in parallel from different peers; already in place.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain.rs:33`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L33) BATCH_BUFFER_SIZE=5 batches in flight
- [`beacon_node/network/src/sync/network_context.rs:478-498`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L478-L498) block_components_by_range_request picks a peer per batch, random tie-break, de-prioritising busy/failed peers

**Sources.** [prysm#2550](https://github.com/OffchainLabs/prysm/pull/2550), [prysm#3538](https://github.com/OffchainLabs/prysm/pull/3538), [prysm#3675](https://github.com/OffchainLabs/prysm/pull/3675), [nimbus#264](https://github.com/status-im/nimbus-eth2/pull/264)

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

**Sources.** [teku#9211](https://github.com/Consensys-Incorporated/teku/pull/9211), [caplin#16915](https://github.com/erigontech/erigon/pull/16915), [teku#2618](https://github.com/Consensys-Incorporated/teku/pull/2618), [teku#3045](https://github.com/Consensys-Incorporated/teku/pull/3045), [teku#9057](https://github.com/Consensys-Incorporated/teku/pull/9057), [nimbus#1919](https://github.com/status-im/nimbus-eth2/pull/1919)

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

**Sources.** [nimbus#3512](https://github.com/status-im/nimbus-eth2/pull/3512), [ethlambda#645](https://github.com/lambdaclass/ethlambda/pull/645), [lodestar#1585](https://github.com/ChainSafe/lodestar/pull/1585), [teku#1079](https://github.com/Consensys-Incorporated/teku/pull/1079), [prysm#4130](https://github.com/OffchainLabs/prysm/pull/4130), [nimbus#1279](https://github.com/status-im/nimbus-eth2/pull/1279), [lodestar#1425](https://github.com/ChainSafe/lodestar/pull/1425)

</details>


<a id="range_sync-064"></a>
<details>
<summary><b>range_sync-064</b> Skip already-imported blocks before batch processing — <i>implemented · low · cpu, disk, sync</i></summary>

**Idea.** Before processing a sync batch, drop duplicate blocks and blocks already in fork choice or the DB, and skip their post-processing, so overlapping, replayed or retried batches cost almost nothing.

**Impact.** Overlapping or retried batches cost only a relevancy check; download cost remains (see range_sync-062).

**Best measured result.** 4x faster forward sync (title) (pr:caplin#11663)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:3068-3142`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3068-L3142) filter_chain_segment drops DuplicateFullyImported, genesis and finalized-slot blocks before import
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3220`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3220) process_chain_segment calls it first

**Sources.** [prysm#6146](https://github.com/OffchainLabs/prysm/pull/6146), [caplin#11663](https://github.com/erigontech/erigon/pull/11663), [prysm#13442](https://github.com/OffchainLabs/prysm/pull/13442)

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

**Sources.** [lodestar#9103](https://github.com/ChainSafe/lodestar/pull/9103)

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

**Sources.** [prysm#5798](https://github.com/OffchainLabs/prysm/pull/5798), [prysm#5887](https://github.com/OffchainLabs/prysm/pull/5887), [prysm#6187](https://github.com/OffchainLabs/prysm/pull/6187)

</details>


<a id="range_sync-076"></a>
<details>
<summary><b>range_sync-076</b> Randomize sync peer selection — <i>implemented · low · S · sync, bandwidth</i></summary>

**Idea.** Pick range sync peers randomly (or shuffle the peer list) instead of a fixed order or a complex scoring policy, so load spreads over all peers and the same few are not hammered.

**Impact.** Load already spreads randomly over peers with fewer active requests.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context.rs:478-492`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L478-L492) block_components_by_range_request picks peer by (deprioritised, at-concurrency-limit, rand::random) ordering

**Sources.** [lodestar@25fb1b672](https://github.com/ChainSafe/lodestar/commit/25fb1b672278), [caplin#16995](https://github.com/erigontech/erigon/pull/16995), [grandine#158](https://github.com/grandinetech/grandine/pull/158)

</details>


<a id="range_sync-078"></a>
<details>
<summary><b>range_sync-078</b> Wait for full custody subnet coverage before column batches — <i>implemented · medium · sync, bandwidth</i></summary>

**Idea.** In custody column range sync, only send a batch once there are peers for every custody column subnet, and choose a randomized custody peer per column, so batches do not fail at once and loop retrying against a failing peer.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain.rs:1168`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L1168) good_peers_on_sampling_subnets gates include_next_batch and send_batch
- [`beacon_node/network/src/sync/network_context/custody.rs:352`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L352) select_column_peer picks randomized custody peer per column

**Sources.** [lighthouse#6004](https://github.com/sigp/lighthouse/pull/6004)

</details>


<a id="range_sync-079"></a>
<details>
<summary><b>range_sync-079</b> Pool peers per chain and load-balance batches — <i>implemented · medium · sync, bandwidth</i></summary>

**Idea.** Group peers that report the same finalized/head chain into one syncing chain and load-balance its batch downloads over the whole peer pool through one state machine.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain.rs:1028`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L1028) send_batch uses chain-wide self.peers pool
- [`beacon_node/network/src/sync/range_sync/chain_collection.rs:480`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain_collection.rs#L480) add_peer_or_create_chain groups peers by target chain

**Sources.** [lighthouse#663](https://github.com/sigp/lighthouse/pull/663)

</details>


<a id="range_sync-081"></a>
<details>
<summary><b>range_sync-081</b> Keep partial column responses, retry only missing columns — <i>implemented · medium · sync, bandwidth</i></summary>

**Idea.** In range sync, accept column responses that miss some columns, keep the good data, attribute the missing columns to the responsible peer, and re-request only those columns from other peers of the syncing chain instead of failing and re-downloading the whole batch.

**Best measured result.** Improve sync performance by retrying only the failed columns from other peers (pr:lighthouse#7733)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_sidecar_coupling.rs:200`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_sidecar_coupling.rs#L200) columns fetched via one custody-by-root request after blocks arrive
- [`beacon_node/network/src/sync/network_context/custody.rs:352`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L352) per-column peer selection with attempt counts; Downloaded columns kept, only missing re-requested (Status enum custody.rs:395)

**Sources.** [lighthouse#7733](https://github.com/sigp/lighthouse/pull/7733), [lighthouse#7726](https://github.com/sigp/lighthouse/pull/7726), [lodestar#8387](https://github.com/ChainSafe/lodestar/pull/8387)

</details>


<a id="range_sync-083"></a>
<details>
<summary><b>range_sync-083</b> Re-trigger sync on a periodic timer — <i>implemented · low · S · sync, latency</i></summary>

**Idea.** Re-evaluate and restart the sync engine on a fixed timer in addition to peer status changes, so a node that is still behind with a stable peer set does not idle for minutes after a batch completes.

**Impact.** Restart after chain completion is event driven (immediate re-status), no idle gap; no fixed sync timer exists but the same effect is reached.

**Best measured result.** restart takes ~5 minutes after 'Syncing completed' otherwise (pr:teku#9849)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/range.rs:361`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/range.rs#L361) on chain removal network.status_peers(chain.peers()) re-statuses peers immediately
- [`beacon_node/network/src/sync/range_sync/range.rs:374`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/range.rs#L374) chains.update after removal
- [`beacon_node/lighthouse_network/src/peer_manager/config.rs:2`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/config.rs#L2) periodic status every 300s as fallback

**Sources.** [teku#9849](https://github.com/Consensys-Incorporated/teku/pull/9849)

</details>


<a id="range_sync-084"></a>
<details>
<summary><b>range_sync-084</b> Peer-unbound worker pool keeps requests pipelined — <i>implemented · medium · sync, bandwidth</i></summary>

**Idea.** Use a pool of sync workers that each take a fresh available peer for every request and issue the next request as soon as any in-flight one completes, so slow peers do not stall the pipeline and peer bandwidth stays used.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain.rs:1188`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L1188) include_next_batch keeps up to BATCH_BUFFER_SIZE=5 batches in flight
- [`beacon_node/network/src/sync/network_context.rs:477`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L477) each batch picks a fresh peer from chain pool, deprioritising failed peers and peers at concurrency limit

**Sources.** [nimbus#117](https://github.com/status-im/nimbus-eth2/pull/117), [nimbus#1602](https://github.com/status-im/nimbus-eth2/pull/1602)

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

**Sources.** [nimbus#3461](https://github.com/status-im/nimbus-eth2/pull/3461), [grandine@b2bb3003e](https://github.com/grandinetech/grandine/commit/b2bb3003ec92)

</details>


<a id="range_sync-096"></a>
<details>
<summary><b>range_sync-096</b> Remove disconnected peer from all sync chains — <i>implemented · low · S · sync</i></summary>

**Idea.** On peer disconnect, remove that peer from every syncing chain's peer pool so no batches are assigned to it and sync does not stall.

**Impact.** Already prevents stalls on disconnect.

**Best measured result.** stalled syncs no longer seen on Schlesi (pr:lighthouse#1150)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/manager.rs:548-561`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L548-L561) peer_disconnect calls range_sync.peer_disconnect
- [`beacon_node/network/src/sync/range_sync/range.rs:281`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/range.rs#L281) remove_peer iterates all chains
- [`beacon_node/network/src/sync/range_sync/chain.rs:248`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L248) Chain::remove_peer, EmptyPeerPool drops chain

**Sources.** [lighthouse#1150](https://github.com/sigp/lighthouse/pull/1150)

</details>


<a id="range_sync-099"></a>
<details>
<summary><b>range_sync-099</b> Cheap slot check before DB lookup — <i>implemented · low · S · disk, cpu</i></summary>

**Idea.** In the already-processed block check, compare the block slot with the head slot first and only query the database when that cheap test is inconclusive.

**Impact.** DB lookup is already avoided via slot and fork choice checks.

**Best measured result.** avoids one DB lookup (pr:prysm#10620)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:3068`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3068) filter_chain_segment uses check_relevancy only
- [`beacon_node/beacon_chain/src/block_verification.rs:1935-1953`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1935-L1953) check_block_relevancy: finalized-slot check then in-memory fork_choice contains_block, no DB read

**Sources.** [prysm#10620](https://github.com/OffchainLabs/prysm/pull/10620)

</details>


<a id="range_sync-101"></a>
<details>
<summary><b>range_sync-101</b> Retry failed batch with a different peer — <i>implemented · medium · S · sync, bandwidth</i></summary>

**Idea.** When a sync request fails or returns an inconsistent range, return it to the queue as failed and assign it to a peer that has not been tried for it yet, instead of leaving it in flight or re-requesting from the same peer.

**Impact.** Already retries failed batches on other peers; failed peers are deprioritised, not hard-excluded.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/batch.rs:203`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/batch.rs#L203) failed_peers() collects download+processing failures
- [`beacon_node/network/src/sync/range_sync/chain.rs:1038`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L1038) send_batch passes failed_peers
- [`beacon_node/network/src/sync/network_context.rs:461`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L461) block_components_by_range_request deprioritises failed peers

**Sources.** [nimbus#7275](https://github.com/status-im/nimbus-eth2/pull/7275), [nimbus#5615](https://github.com/status-im/nimbus-eth2/pull/5615), [lodestar#9360](https://github.com/ChainSafe/lodestar/pull/9360)

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


<a id="range_sync-109"></a>
<details>
<summary><b>range_sync-109</b> No blob wait outside DA window — <i>implemented · medium · S · latency, sync</i></summary>

**Idea.** For blocks outside the data availability window, mark data as available at once instead of waiting for blob sidecars and their timeout.

**Impact.** Blocks outside the window are requested without sidecars and imported without waiting.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context.rs:1296`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L1296) batch_type returns Blocks outside DA window
- [`beacon_node/beacon_chain/src/custody_context.rs:574`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L574) da_check_required_for_epoch
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:867`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L867) columns/blobs required only inside window

**Sources.** [teku#9713](https://github.com/Consensys-Incorporated/teku/pull/9713)

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


<a id="range_sync-115"></a>
<details>
<summary><b>range_sync-115</b> Skip newPayload for finalized sync blocks — <i>implemented · high · S · latency, sync</i></summary>

**Idea.** When syncing a finalized chain, import blocks as optimistic and skip the engine newPayload call, since finality already vouches for them, removing an EL round trip per block.

**Impact.** Already skips newPayload for finalized sync; only block-hash verification remains.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:497-506`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L497-L506) NotifyExecutionLayer::No when is_syncing_finalized
- [`beacon_node/beacon_chain/src/execution_payload.rs:77-94`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/execution_payload.rs#L77-L94) returns PayloadVerificationStatus::Optimistic, skipping newPayload (config optimistic_finalized_sync)

**Sources.** [lighthouse#3738](https://github.com/sigp/lighthouse/pull/3738)

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

**Impact.** Batches are already one epoch (32 blocks), so retries are cheap.

**Best measured result.** 2000 blobs is ~250 MB per minute per peer max (pr:teku#8982)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain.rs:30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L30) EPOCHS_PER_BATCH = 1
- [`beacon_node/network/src/sync/range_sync/chain.rs:33`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L33) BATCH_BUFFER_SIZE = 5

**Sources.** [lighthouse#1812](https://github.com/sigp/lighthouse/pull/1812), [prysm#5128](https://github.com/OffchainLabs/prysm/pull/5128), [teku#8982](https://github.com/Consensys-Incorporated/teku/pull/8982), [grandine@846e07ee7](https://github.com/grandinetech/grandine/commit/846e07ee7949), [grandine#96](https://github.com/grandinetech/grandine/pull/96), [nimbus#988](https://github.com/status-im/nimbus-eth2/pull/988)

</details>


<a id="range_sync-130"></a>
<details>
<summary><b>range_sync-130</b> Do not pre-filter peers for column sync — <i>implemented · low · S · sync</i></summary>

**Idea.** Pass all candidate peers to the column-by-range request logic and let it filter per request, instead of pre-restricting initial sync to a small peer set, and do not block responses waiting for unavailable data.

**Impact.** Already avoids the slow initial sync from pre-filtering; peer set is the syncing chain's peers, and a column with no custody peer fails the request (NoPeer) rather than waiting.

**Best measured result.** "initial sync takes hours" with peer filtering (pr:prysm#14482)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context.rs:578`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L578) - select_columns_by_range_peers_to_request picks per column among chain peers by is_custody_peer_of
- [`beacon_node/network/src/sync/network_context.rs:598`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L598) - peers filtered per request, with deprioritization and concurrency-limit ordering, not pre-restricted to supernodes

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

**Sources.** [lighthouse#10462](https://github.com/sigp/lighthouse/pull/10462)

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

**Sources.** [grandine@28f28818f](https://github.com/grandinetech/grandine/commit/28f28818fca6)

</details>


