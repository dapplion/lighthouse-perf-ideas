# data_availability (part 1 of 2)

175 ideas: 27 not, 35 partial, 81 implemented, 32 n/a; 30 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

Pages: [part 1](data_availability.md) · [part 2](data_availability-2.md)

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [data_availability-001](#data_availability-001) | Fetch blobs from EL on gossip block arrival | implemented | high | S | latency, bandwidth, sync |
| [data_availability-002](#data_availability-002) **★** | Query EL first, request only remaining blobs from peers | partial | medium | S | latency, bandwidth |
| [data_availability-003](#data_availability-003) **★** | Trigger getBlobs on first gossip column sidecar | partial | medium | S | latency, bandwidth |
| [data_availability-004](#data_availability-004) | Call getBlobs before block verification completes | implemented | medium | S | latency, bandwidth |
| [data_availability-005](#data_availability-005) | Fetch blobs from EL during block lookup sync | partial | low | M | latency, bandwidth |
| [data_availability-006](#data_availability-006) | Fetch EL blobs for blocks published via API | implemented | low | S | latency, bandwidth |
| [data_availability-007](#data_availability-007) | Use existence-only EL blob query | not | low | M | latency, bandwidth |
| [data_availability-008](#data_availability-008) | Fill partial column cells from EL blobs | implemented | medium | S | latency, bandwidth |
| [data_availability-009](#data_availability-009) | Run blob tracker only for gossip blocks | implemented | low | S | cpu, bandwidth |
| [data_availability-010](#data_availability-010) | Skip EL reconstruction when nothing is missing | partial | low | S | cpu |
| [data_availability-011](#data_availability-011) **★** | Build only custodied columns from EL blobs | partial | medium | S | cpu, memory |
| [data_availability-012](#data_availability-012) **★** | Publish recovered columns off the availability path | partial | medium | S | latency, bandwidth |
| [data_availability-013](#data_availability-013) | Publish only needed columns after reconstruction | implemented | medium | S | cpu, bandwidth |
| [data_availability-014](#data_availability-014) **★** | Mark data available at 50% columns | not | medium | M | latency, bandwidth, sync |
| [data_availability-015](#data_availability-015) | Reconstruct remaining columns locally from half | implemented | medium | S | cpu, latency, bandwidth, sync |
| [data_availability-016](#data_availability-016) | Delay column reconstruction, bounded by slot deadline | implemented | low | S | cpu, latency, sync |
| [data_availability-017](#data_availability-017) | Cap reconstruction debounce delay | partial | low | S | cpu, latency |
| [data_availability-018](#data_availability-018) | Reconstruct only on nodes custodying at least half | implemented | low | S | cpu |
| [data_availability-019](#data_availability-019) | Run column reconstruction at most once per block | implemented | medium | S | cpu, memory, disk |
| [data_availability-020](#data_availability-020) | Dedicated thread pool for column reconstruction | partial | low | S | cpu, latency |
| [data_availability-021](#data_availability-021) | Run KZG and reconstruction off async and fork-choice threads | implemented | medium | S | cpu, latency |
| [data_availability-022](#data_availability-022) | Parallel, bounded per-blob cell recovery | implemented | medium | S | cpu, memory, latency |
| [data_availability-023](#data_availability-023) | Semi-supernode: custody half the columns | implemented | high | S | cpu, disk, bandwidth |
| [data_availability-024](#data_availability-024) | Custody first half of columns to skip reconstruction | n/a | medium | S | cpu, bandwidth |
| [data_availability-025](#data_availability-025) **★** | Background reconstruction of historical custody columns | not | medium | L | cpu, disk, bandwidth |
| [data_availability-026](#data_availability-026) | Reconstruct API blobs from stored columns | implemented | low | S | cpu, memory |
| [data_availability-027](#data_availability-027) | Share blobs, cells and sidecars by reference | partial | low | M | cpu, memory |
| [data_availability-028](#data_availability-028) | Store a blob as one flat byte array | n/a | low | S | memory |
| [data_availability-029](#data_availability-029) | Assemble partial columns in-place in ring buffer | not | low | L | memory, latency, bandwidth |
| [data_availability-030](#data_availability-030) | Quarantine blobs with blobless blocks until joined | partial | low | M | memory, latency, bandwidth, sync |
| [data_availability-031](#data_availability-031) **★** | Cache columns with unknown parent block | not | medium | M | latency, sync |
| [data_availability-032](#data_availability-032) | Per-root indexed sidecar quarantine lookups | implemented | low | S | cpu |
| [data_availability-033](#data_availability-033) | Cache custody column set per node | implemented | low | S | cpu |
| [data_availability-034](#data_availability-034) | Batch KZG verify sidecars from RPC and sync | implemented | medium | S | cpu, latency, sync |
| [data_availability-035](#data_availability-035) **★** | Batch gossip column verification per block | not | medium | M | cpu, latency |
| [data_availability-036](#data_availability-036) | Combine by-root sidecar requests per peer | implemented | medium | S | bandwidth, sync |
| [data_availability-037](#data_availability-037) | Cap columns per by-root request | partial | low | S | bandwidth |
| [data_availability-038](#data_availability-038) | Request columns only from custody peers | implemented | medium | S | bandwidth, sync |
| [data_availability-039](#data_availability-039) **★** | Hedge slow column requests to alternate peers | not | medium | M | latency, sync |
| [data_availability-040](#data_availability-040) | Insert EL-built columns in one batch | implemented | low | S | cpu |
| [data_availability-041](#data_availability-041) | Async access to pending sidecar maps | n/a | low |  | latency |
| [data_availability-042](#data_availability-042) | Sidecar validation without state advancement | implemented | medium | S | cpu, memory, latency |
| [data_availability-043](#data_availability-043) | Avoid collecting vectors in pending-column check | not | low | S | cpu, memory |
| [data_availability-044](#data_availability-044) | Prune blob and column data past DA window | implemented | medium | M | disk |
| [data_availability-045](#data_availability-045) | Derive column retention window from chain config | implemented | low | S | disk |
| [data_availability-046](#data_availability-046) | Never prune blobs needed at chain tip | implemented | low | S | latency |
| [data_availability-047](#data_availability-047) | Cheap filesystem traversal for blob pruning | n/a | low |  | cpu, disk |
| [data_availability-048](#data_availability-048) | Incremental capped low-priority blob pruning | partial | low | S | cpu, disk, latency |
| [data_availability-049](#data_availability-049) | Store blob sidecars in KV database | implemented | low | S | memory, disk |
| [data_availability-050](#data_availability-050) | Persist data columns in dedicated disk store | implemented | low | S | disk |
| [data_availability-051](#data_availability-051) | In-memory index of stored sidecars | not | low | M | disk, startup |
| [data_availability-052](#data_availability-052) | Faster column reads from storage | partial | low | S | cpu, disk |
| [data_availability-053](#data_availability-053) | Snapshot sidecar index cache at shutdown | n/a | low |  | startup |
| [data_availability-054](#data_availability-054) **★** | Skip re-verifying already verified sidecars | partial | medium | S | cpu, latency |
| [data_availability-055](#data_availability-055) | Drop sidecars and fetches for imported blocks | partial | low | S | cpu, memory, bandwidth |
| [data_availability-056](#data_availability-056) | Bound or fail fast on DA wait | n/a | medium |  | latency, sync |
| [data_availability-057](#data_availability-057) | Bounded cache of in-flight sampled blocks | implemented | low | S | memory |
| [data_availability-058](#data_availability-058) **★** | Run DA check concurrently with block verification | partial | medium | M | latency |
| [data_availability-059](#data_availability-059) | Merge pre-import block cache into DA cache | implemented | low | S | memory |
| [data_availability-060](#data_availability-060) | Skip duplicate blob arrival notifications | implemented | low | S | cpu |
| [data_availability-061](#data_availability-061) | Track received columns to skip duplicate work | implemented | medium | S | cpu, disk, bandwidth |
| [data_availability-062](#data_availability-062) | Retry pending block only when all columns arrive | n/a | low |  | cpu |
| [data_availability-063](#data_availability-063) **★** | Delay RPC fetch of missing sidecars | partial | medium | S | latency, bandwidth, sync |
| [data_availability-064](#data_availability-064) | Request missing blobs immediately on block seen | not | low | S | latency |
| [data_availability-065](#data_availability-065) **★** | Pull late block when blobs arrive first | partial | medium | S | latency |
| [data_availability-066](#data_availability-066) | Fetch missing blobs immediately for past slots | n/a | low |  | latency, sync |
| [data_availability-067](#data_availability-067) **★** | Fetch missing columns within the slot | partial | medium | M | latency |
| [data_availability-068](#data_availability-068) | Disable blob tracking after retention passes | n/a | low |  | cpu, memory |
| [data_availability-069](#data_availability-069) | Disk-backed blob quarantine | n/a | medium |  | memory, disk |
| [data_availability-070](#data_availability-070) | Memory-only bounded LRU for pending components | implemented | medium | S | memory, disk |
| [data_availability-071](#data_availability-071) | Remove duplicate column sidecar stores | n/a | low |  | memory |
| [data_availability-072](#data_availability-072) | Drop sidecars with out-of-range index | implemented | low | S | cpu, memory |
| [data_availability-073](#data_availability-073) | Remove repeated checks from isDataAvailable | partial | low | S | cpu |
| [data_availability-074](#data_availability-074) | Drop stale validator custody registrations | implemented | low | S | memory |
| [data_availability-075](#data_availability-075) | Evict DA entries exactly when import completes | partial | low | S | cpu, memory, disk, latency, bandwidth, sync |
| [data_availability-076](#data_availability-076) | Wait on store events instead of polling | n/a | low |  | cpu, latency |
| [data_availability-077](#data_availability-077) | Free column recovery state promptly | n/a | medium |  | cpu, memory |
| [data_availability-078](#data_availability-078) | Import only when blob count equals commitments | implemented | low | S | latency |
| [data_availability-079](#data_availability-079) | Drop gossip columns outside sampling set | implemented | low | S | cpu, disk, bandwidth |
| [data_availability-080](#data_availability-080) | Correct proposer cache key in blob verification | implemented | medium | S | cpu, latency |
| [data_availability-081](#data_availability-081) | Consistent sidecar quarantine accounting | implemented | low | S | cpu, memory, disk |
| [data_availability-082](#data_availability-082) | High priority retry for delayed columns | implemented | low | S | latency |
| [data_availability-083](#data_availability-083) | Keep column recovery queue in memory | implemented | low | S | memory, disk, sync |
| [data_availability-084](#data_availability-084) | Serve blob by-root fetches from quarantine directly | implemented | low | S | bandwidth, sync |
| [data_availability-085](#data_availability-085) | Skip KZG and proof checks for EL-built columns | implemented | medium | S | cpu, latency |
| [data_availability-086](#data_availability-086) | Cache column inclusion proof results | not | low | S | cpu |
| [data_availability-087](#data_availability-087) | Late DA check with per-block sampling tracker | implemented | medium | M | disk, latency, bandwidth |
| [data_availability-088](#data_availability-088) **★** | Re-call getBlobs until block columns are complete | not | medium | S | latency, bandwidth |
| [data_availability-089](#data_availability-089) | Dedicated executor queue for DA tasks | n/a | low | S | latency |
| [data_availability-090](#data_availability-090) **★** | Allow column reconstruction while not synced | not | medium | M | sync, bandwidth |
| [data_availability-091](#data_availability-091) | Lock striping in column store | not | low | M | cpu, latency |
| [data_availability-092](#data_availability-092) | Compute sidecar inclusion proofs from shared merkle subtrees | partial | low | S | cpu, memory |
| [data_availability-093](#data_availability-093) | Validate column sidecars at mid processor priority | implemented | medium | S | latency |
| [data_availability-094](#data_availability-094) | Fetch column subsets from many peers in parallel | implemented | medium | M | sync, bandwidth |
| [data_availability-095](#data_availability-095) **★** | Give reconstruction a multi-thread worker allocation | partial | medium | S | cpu, latency |
| [data_availability-096](#data_availability-096) **★** | Reconstruct only when needed columns are missing | partial | medium | S | cpu |
| [data_availability-097](#data_availability-097) | No reconstruction when serving column RPC | implemented | medium | S | cpu, latency |
| [data_availability-098](#data_availability-098) | Non-blocking state access in sidecar handling | partial | low | M | latency |
| [data_availability-099](#data_availability-099) | Run gossip column KZG verification on blocking pool | implemented | medium | S | latency, cpu |
| [data_availability-100](#data_availability-100) | Operator flags to skip EL or blob handling | not | low | M | disk, bandwidth |
| [data_availability-101](#data_availability-101) | Mark columns available before disk write completes | n/a | low | S | latency |
| [data_availability-102](#data_availability-102) | Option to disable blob pruning | implemented | low | S | disk |
| [data_availability-103](#data_availability-103) **★** | Overflow pending DA cache to disk | not | medium | L | memory |
| [data_availability-104](#data_availability-104) | Parallel DA cache warmup at startup | n/a | low | S | startup |
| [data_availability-105](#data_availability-105) | Compute column sidecars from blobs in parallel | implemented | medium | S | cpu, latency |
| [data_availability-106](#data_availability-106) | Request sampled columns concurrently | implemented | low | S | latency |
| [data_availability-107](#data_availability-107) | Fetch payload envelope and columns in parallel | implemented | low | S | latency, sync |
| [data_availability-108](#data_availability-108) | Reconstruct only requested blobs for blob API | implemented | low | S | cpu, latency |
| [data_availability-109](#data_availability-109) | Request only custody cells from EL getBlobs | implemented | medium | S | bandwidth, cpu |
| [data_availability-110](#data_availability-110) | Partial data column dissemination at cell granularity | implemented | high | L | bandwidth, latency |
| [data_availability-111](#data_availability-111) | Pass KZG commitments into DA check, skip DB read | implemented | low | S | disk, cpu |
| [data_availability-112](#data_availability-112) | Cooldown peers that return empty column responses | not | low | S | bandwidth, sync |
| [data_availability-113](#data_availability-113) | Filter column request peers by earliest available slot | implemented | medium | S | sync |
| [data_availability-114](#data_availability-114) **★** | Rank column peers by historical response rate | not | medium | S | sync |
| [data_availability-115](#data_availability-115) | Persist columns before pruning | n/a | low | S | disk |
| [data_availability-116](#data_availability-116) | Prune stale DA and quarantine entries by finality or expiry | implemented | medium | S | memory |
| [data_availability-117](#data_availability-117) **★** | Store only original columns and rebuild extension on demand | not | high | M | disk |
| [data_availability-118](#data_availability-118) | Clean legacy unpruned column buckets at startup | n/a | low | S | disk |
| [data_availability-119](#data_availability-119) | Blob pruning at startup policy | n/a | low | S | disk, startup |
| [data_availability-120](#data_availability-120) | Skip rebroadcast of columns already seen on gossip | implemented | medium | S | bandwidth, cpu |
| [data_availability-121](#data_availability-121) | Retain sidecars for backfill window | n/a | low | S | bandwidth, sync |
| [data_availability-122](#data_availability-122) | Query columns by slot range during sync | implemented | medium | S | sync, bandwidth |
| [data_availability-123](#data_availability-123) | Reconstruct without holding the DA cache lock | partial | low | S | latency |
| [data_availability-124](#data_availability-124) | Reconstruction queue capacity one | implemented | low | S | cpu |
| [data_availability-125](#data_availability-125) **★** | Wall-clock timeout on column reconstruction | not | medium | S | latency |
| [data_availability-126](#data_availability-126) **★** | Minimum custody with full-subnet sampling mode | partial | medium | M | bandwidth |
| [data_availability-127](#data_availability-127) | Batch several epochs per missing-column refill | not | low | S | sync |
| [data_availability-128](#data_availability-128) | Remove blob archival semaphore | n/a | low |  | disk, latency |
| [data_availability-129](#data_availability-129) | Gloas: check DA on the envelope, not the block | partial | low | S | latency |
| [data_availability-130](#data_availability-130) | Remove redundant custody request layer | n/a | low |  | cpu, memory |
| [data_availability-131](#data_availability-131) | Remove coarse locks from column retriever | n/a | low |  | latency |
| [data_availability-132](#data_availability-132) | DA cache state storage: state root plus LRU vs direct | implemented | low | S | memory |
| [data_availability-133](#data_availability-133) | Shorter per-request lifecycle for column recovery | n/a | low | S | memory |
| [data_availability-134](#data_availability-134) | Pool and retry data-unavailable blocks | implemented | medium | S | bandwidth, sync |
| [data_availability-135](#data_availability-135) | Re-issue failed column fetches on availability recheck | implemented | low | S | sync |
| [data_availability-136](#data_availability-136) | Read-only head state for sidecar verification | implemented | medium | S | cpu, memory |
| [data_availability-137](#data_availability-137) | Data column sampling off by default | n/a | low |  | bandwidth, cpu |
| [data_availability-138](#data_availability-138) | Scale blob fetch concurrency with max blobs | n/a | low |  | sync |
| [data_availability-139](#data_availability-139) | Serialize column persistence tasks | n/a | low |  | cpu, disk |
| [data_availability-140](#data_availability-140) | Serve column reads from in-flight writes | implemented | low | S | latency |
| [data_availability-141](#data_availability-141) **★** | Single shared buffer for all column sources | partial | medium | M | memory |
| [data_availability-142](#data_availability-142) **★** | Singleflight proposer signature verification | partial | medium | S | cpu |
| [data_availability-143](#data_availability-143) **★** | Skip DA check outside blob retention window | partial | medium | S | sync, bandwidth |
| [data_availability-144](#data_availability-144) | Skip DA check for blocks loaded from local storage | n/a | low |  | startup |
| [data_availability-145](#data_availability-145) | Skip custody group derivation for supernodes | implemented | low | S | cpu |
| [data_availability-146](#data_availability-146) | Recompute custody count only on finalization | implemented | low | S | cpu |
| [data_availability-147](#data_availability-147) | Skip proposer checks for EL-built columns | implemented | low | S | cpu |
| [data_availability-148](#data_availability-148) | Skip DA work for blocks without blob commitments | implemented | low | S | cpu |
| [data_availability-149](#data_availability-149) **★** | Skip publishing columns while syncing | partial | medium | S | bandwidth, cpu |
| [data_availability-150](#data_availability-150) | Skip EL column compute for imported blocks | implemented | medium | S | cpu |
| [data_availability-151](#data_availability-151) | Skip block presence check after early import | n/a | low |  | cpu |
| [data_availability-152](data_availability-2.md#data_availability-152) | Store blobs Snappy-compressed as on the wire | not | low | S | disk, cpu |
| [data_availability-153](data_availability-2.md#data_availability-153) | Sort custody groups once | n/a | low |  | cpu |
| [data_availability-154](data_availability-2.md#data_availability-154) **★** | Staged blob reconstruction: concatenate first | partial | medium | S | cpu, bandwidth |
| [data_availability-155](data_availability-2.md#data_availability-155) | Smaller pending-components cache capacity | implemented | medium | S | memory |
| [data_availability-156](data_availability-2.md#data_availability-156) | Persist only custody columns | implemented | medium | S | disk |
| [data_availability-157](data_availability-2.md#data_availability-157) | Keep only sampling columns in fork choice store | n/a | low |  | memory |
| [data_availability-158](data_availability-2.md#data_availability-158) | Minimum custody until synced | partial | low | M | sync, bandwidth, disk |
| [data_availability-159](data_availability-2.md#data_availability-159) | Synthesize empty sidecar lists, do not store them | implemented | low | S | disk |
| [data_availability-160](data_availability-2.md#data_availability-160) | Unified blob availability cache for all paths | partial | low | M | memory, latency |
| [data_availability-161](data_availability-2.md#data_availability-161) **★** | Use EL blobs until block data is imported | not | medium | S | bandwidth, latency |
| [data_availability-162](data_availability-2.md#data_availability-162) **★** | Verify availability-critical columns first | not | medium | S | latency |
| [data_availability-163](data_availability-2.md#data_availability-163) | Verify sidecars before persisting | implemented | medium | S | disk |
| [data_availability-164](data_availability-2.md#data_availability-164) | Start EL blob lookup immediately near deadline | implemented | low | S | latency |
| [data_availability-165](data_availability-2.md#data_availability-165) | Fetch EL blobs when payload envelope awaits blobs | implemented | medium | S | latency, bandwidth |
| [data_availability-166](data_availability-2.md#data_availability-166) | Refresh quarantine LRU position on sidecar request | not | low | S | memory, latency |
| [data_availability-167](data_availability-2.md#data_availability-167) | Defer payload envelope signature checks in bounded queue | implemented | low | S | cpu, memory |
| [data_availability-168](data_availability-2.md#data_availability-168) | Check in-memory column status before DB block read | implemented | low | S | disk, latency |
| [data_availability-169](data_availability-2.md#data_availability-169) | Drop KZG commitments from data column sidecars | implemented | low | S | bandwidth, disk |
| [data_availability-170](data_availability-2.md#data_availability-170) | Do not backfill columns when custody increases | not | low | M | bandwidth, sync |
| [data_availability-171](data_availability-2.md#data_availability-171) | Publish proposer column sidecars before payload envelope | not | low | S | latency |
| [data_availability-172](data_availability-2.md#data_availability-172) | Proposer publishes sidecars only when responsible | implemented | low | S | bandwidth, cpu |
| [data_availability-173](data_availability-2.md#data_availability-173) | Per-type block data availability state machines | n/a | low | S | cpu |
| [data_availability-174](data_availability-2.md#data_availability-174) | One getBlobs attempt per slot, not per column gossip | implemented | low | S | cpu, latency |
| [data_availability-175](data_availability-2.md#data_availability-175) | Skip custody increase detection without validators | implemented | low | S | bandwidth, disk |

★ actionable. Click an id for the full record.

## Ideas

<a id="data_availability-001"></a>
<details>
<summary><b>data_availability-001</b> Fetch blobs from EL on gossip block arrival — <i>implemented · high · S · latency, bandwidth, sync</i></summary>

**Idea.** When a gossip block with blob commitments arrives, call engine_getBlobs on the local EL and build the blob/data column sidecars from the response. The block becomes available without waiting for the sidecars from gossip or peers.

**Impact.** Block becomes available from the local EL without waiting on gossip sidecars.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1936`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1936) spawn_fetch_block_columns on gossip-valid block
- [`beacon_node/network/src/network_beacon_processor/mod.rs:960-1060`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L960-L1060) spawn_fetch_block_columns/fetch_engine_blobs_and_publish_full publish and import EL columns
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:128-178`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L128-L178) getBlobsV4 or V2/V3, builds custody columns
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1119-1133`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1119-L1133) also triggered on a partial column header

**Skeptic check.** Verified gossip block arrival spawns the EL getBlobs fetch, builds/imports and publishes custody columns. Pre-Fulu (getBlobsV1) is no longer supported, irrelevant on post-Fulu mainnet.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#7123](https://github.com/status-im/nimbus-eth2/pull/7123), [lodestar#7679](https://github.com/ChainSafe/lodestar/pull/7679), [prysm#15483](https://github.com/OffchainLabs/prysm/pull/15483), [caplin#25447](https://github.com/erigontech/erigon/pull/25447), [grandine#79](https://github.com/grandinetech/grandine/pull/79), [lodestar#7134](https://github.com/ChainSafe/lodestar/pull/7134), [nimbus#7866](https://github.com/status-im/nimbus-eth2/pull/7866), [grandine@4c5ccd951](https://github.com/grandinetech/grandine/commit/4c5ccd951a55), [silver#110](https://github.com/gattaca-com/silver/pull/110), [prysm#16638](https://github.com/OffchainLabs/prysm/pull/16638), [caplin#25522](https://github.com/erigontech/erigon/pull/25522)

</details>


<a id="data_availability-002"></a>
<details>
<summary><b>data_availability-002</b> Query EL first, request only remaining blobs from peers — <i>partial · medium · S · latency, bandwidth</i></summary>

**Idea.** When blobs or columns for a block are missing, query the local EL first and send RPC requests to peers only for the ones still missing. Share one received-sidecar set between the EL and the p2p fetch paths so no sidecar is fetched twice.

**Gap in Lighthouse.** The peer request is not deferred until the EL result is known: both run at once, and ActiveCustodyRequest never re-checks the DA cache, so columns the EL supplies are still downloaded from peers. Make the lookup's DataRequest wait for block processing (which already awaits getBlobs) before calling custody_lookup_request, or re-filter indices against cached_data_column_indexes before each peer request.

**Impact.** Saves redundant column download on lookups of blocks whose blobs are in the local mempool; small since gossip blocks (the common case) already trigger EL first and lookups are rare.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/single_block_lookup.rs:397-433`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/single_block_lookup.rs#L397-L433) custody_lookup_request is issued as soon as the block is downloaded, in the same continue_requests call that sends the block to processing
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:209-224`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L209-L224) EL getBlobs is awaited inside RPC block processing, after MissingComponents, in parallel with the peer column request
- [`beacon_node/network/src/sync/network_context.rs:970-990`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L970-L990) custody_lookup_request skips only columns already in the DA cache (cached_data_column_indexes) at send time
- [`beacon_node/network/src/sync/network_context/custody.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs) (no DA-cache re-check on retries or after EL import)

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [teku#8663](https://github.com/Consensys-Incorporated/teku/pull/8663), [grandine@a850e357b](https://github.com/grandinetech/grandine/commit/a850e357b76b), [grandine#114](https://github.com/grandinetech/grandine/pull/114), [teku#8927](https://github.com/Consensys-Incorporated/teku/pull/8927)

</details>


<a id="data_availability-003"></a>
<details>
<summary><b>data_availability-003</b> Trigger getBlobs on first gossip column sidecar — <i>partial · medium · S · latency, bandwidth</i></summary>

**Idea.** Start the EL getBlobs fetch when the first valid data column sidecar arrives on gossip, also before its block arrives. The missing columns are then built from EL blobs sooner than with a trigger on block arrival only.

**Gap in Lighthouse.** There is no trigger on the first full Fulu DataColumnSidecar seen before its block (for example from peers that do not use partial messages, or with partial columns turned off). Fix: call fetch_engine_blobs_and_publish_full from process_gossip_verified_data_column with a PartialHeaderOrBid built from the sidecar's signed header, behind a per-block-root in-flight guard.

**Impact.** Only helps when a full column arrives before both the block and any partial header; with partial columns on by default this ordering is rare.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1117-1134`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1117-L1134) getBlobs is triggered on the first uncached Fulu partial-column header
- [`beacon_node/src/cli.rs:693-701`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L693-L701) enable-partial-columns defaults to true, so this trigger is active by default
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:926-1047`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L926-L1047) the full DataColumnSidecar gossip handler never calls fetch_engine_blobs_and_publish_full
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1066-1069`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1066-L1069) Gloas triggers getBlobs on the bid instead
- [`beacon_node/network/src/network_beacon_processor/mod.rs:960-1020`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L960-L1020) the only other triggers are a gossip/RPC/HTTP block (spawn_fetch_block_columns) and a lookup block

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [lighthouse#7329](https://github.com/sigp/lighthouse/pull/7329), [nimbus#8393](https://github.com/status-im/nimbus-eth2/pull/8393), [nimbus#7390](https://github.com/status-im/nimbus-eth2/pull/7390), [teku#9961](https://github.com/Consensys-Incorporated/teku/pull/9961)

</details>


<a id="data_availability-004"></a>
<details>
<summary><b>data_availability-004</b> Call getBlobs before block verification completes — <i>implemented · medium · S · latency, bandwidth</i></summary>

**Idea.** Start the EL getBlobs fetch as soon as a gossip block header is seen, before consensus and execution verification of the block. The local blobs then win the race against gossip and can be published.

**Impact.** Local blobs win the race against gossip.

**Best measured result.** 116 hits and 156 blobs published in 30 min on mainnet, up from a few hits per hour (pr:lighthouse#6600)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1936-1951`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1936-L1951) spawn_fetch_block_columns before chain.process_block
- [`beacon_node/network/src/network_beacon_processor/mod.rs:973-995`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L973-L995) spawned async task
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1119-1133`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1119-L1133) getBlobs on first verified partial column header, even before the block

**Skeptic check.** getBlobs is spawned right after gossip verification (signature/header checks), before state transition and newPayload; it is also started from a partial column header. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#6600](https://github.com/sigp/lighthouse/pull/6600), [lighthouse#6756](https://github.com/sigp/lighthouse/pull/6756)

</details>


<a id="data_availability-005"></a>
<details>
<summary><b>data_availability-005</b> Fetch blobs from EL during block lookup sync — <i>partial · low · M · latency, bandwidth</i></summary>

**Idea.** In unknown-block / lookup sync for a block by root, also try engine_getBlobs before requesting blobs or columns from peers. Availability can then resolve locally without RPC.

**Gap in Lighthouse.** Lookup sync does call engine getBlobs, but only after full block processing (including newPayload) returns MissingComponents in sync_methods.rs, while SingleBlockLookup::continue_requests has already sent the custody column RPC via custody_lookup_request. getBlobs is never tried before the peer request or before custody retries, so the RPC is always spent even when the EL holds every blob.

**Impact.** Saves custody column RPC bandwidth and peer load on lookups when the EL has the blobs; latency is already similar because both run concurrently.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/single_block_lookup.rs:398-435`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/single_block_lookup.rs#L398-L435) custody_lookup_request issued as soon as the block is downloaded, concurrent with block processing
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:208-225`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L208-L225) getBlobs only after process_block returns MissingComponents (publish_blobs=false)
- [`beacon_node/network/src/sync/network_context.rs:956-1000`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L956-L1000) custody_lookup_request filters only DA-cached columns

**Skeptic check.** Earlier evidence found the right call site, but the ordering differs from the idea: LH runs EL fetch after processing and in parallel with the RPC, not before it, so availability can resolve locally but the RPC is not avoided.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lodestar#7724](https://github.com/ChainSafe/lodestar/pull/7724)

</details>


<a id="data_availability-006"></a>
<details>
<summary><b>data_availability-006</b> Fetch EL blobs for blocks published via API — <i>implemented · low · S · latency, bandwidth</i></summary>

**Idea.** When a block is published through the HTTP API without blob data, still trigger the EL getBlobs fetch and the column requests for it, because later gossip duplicates of the block are ignored.

**Impact.** Already in tree (this is the Lighthouse PR itself). API-published blocks start the EL getBlobs fetch and partial column requests.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/publish_blocks.rs:220-234`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L220-L234) after publishing, sends NetworkMessage::FetchBlockColumns when fetch_columns (no blobs supplied)
- [`beacon_node/network/src/service.rs:692-700`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L692-L700) FetchBlockColumns -&gt; spawn_fetch_block_columns(EnvelopeSource::Http)
- [`beacon_node/network/src/network_beacon_processor/mod.rs:960-995`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L960-L995) spawn_fetch_block_columns runs fetch_engine_blobs_and_publish_full then publish_partial_data_columns

**Skeptic check.** Verified the publish path sends FetchBlockColumns and the network service spawns the shared getBlobs + partial column sequence. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#10396](https://github.com/sigp/lighthouse/pull/10396)

</details>


<a id="data_availability-007"></a>
<details>
<summary><b>data_availability-007</b> Use existence-only EL blob query — <i>not · low · M · latency, bandwidth</i></summary>

**Idea.** Use an existence-only Engine API call (HasBlobs) to learn which blobs the EL holds, so held cells can be advertised to peers at once without the slower full getBlobs round trip.

**Gap in Lighthouse.** Add an engine_hasBlobs-style call in engine_api/http.rs plus capability check, and in the gossip partial-header and spawn_fetch_block_columns paths call it first so publish_partial_data_columns can advertise held cells before the full getBlobs completes.

**Impact.** Advertising wanted/held cells could start one getBlobs round trip (tens to hundreds of ms) earlier on partial-column topics. Needs EL support (geth PR, not standard) and only helps partial-column messaging.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engine_api/http.rs:71-73`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L71-L73) only getBlobsV2/V3/V4 are known, no existence-only call
- [`beacon_node/network/src/network_beacon_processor/mod.rs:982-995`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L982-L995) publish_partial_data_columns is awaited only after fetch_engine_blobs_and_publish_full finishes
- [`beacon_node/beacon_chain/src/partial_data_column_assembler.rs:84`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/partial_data_column_assembler.rs#L84) has_local_blobs is just disable_get_blobs

**Sources.** [prysm#16774](https://github.com/OffchainLabs/prysm/pull/16774)

</details>


<a id="data_availability-008"></a>
<details>
<summary><b>data_availability-008</b> Fill partial column cells from EL blobs — <i>implemented · medium · S · latency, bandwidth</i></summary>

**Idea.** On a partial data column header, fetch the matching blobs from the EL (getBlobsV3) and fill the cell assembly locally. Fewer cells must come from peers.

**Impact.** EL cells fill the partial assembly before peer cell requests go out, so fewer cells come from peers.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1119-1137`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1119-L1137) a new (not cached) verified partial header triggers fetch_engine_blobs_and_publish_full then publish_partial_data_columns
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:154-185`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L154-L185) getBlobsV4 preferred, V2/V3 fallback
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:242-265`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L242-L265) V3 partial responses accepted (not discarded)
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:299-330`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L299-L330) import_custody_partial_columns merges EL cells into PartialDataColumnAssembler via merge_partials

**Skeptic check.** Confirmed the partial-header gossip handler calls getBlobs (V4 or V3 with partial responses kept) and merges the result into the assembler before publish_partial_data_columns. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [silver#292](https://github.com/gattaca-com/silver/pull/292), [prysm#16324](https://github.com/OffchainLabs/prysm/pull/16324), [nimbus#8513](https://github.com/status-im/nimbus-eth2/pull/8513)

</details>


<a id="data_availability-009"></a>
<details>
<summary><b>data_availability-009</b> Run blob tracker only for gossip blocks — <i>implemented · low · S · cpu, bandwidth</i></summary>

**Idea.** Start post-import fetch of missing blobs/columns (EL or peers) only for blocks that arrived via gossip, not for blocks imported by sync or other paths.

**Impact.** Range and backfill sync never trigger the EL fetch. Only gossip, API publish and single-block lookups with missing components do it, and the lookups do it for a reason.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1936`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1936) gossip blocks call spawn_fetch_block_columns
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:209-224`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L209-L224) RPC lookup blocks fetch only on MissingComponents, publish_blobs=false
- [`beacon_node/network/src/service.rs:697`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L697) only other caller is the HTTP publish path; process_chain_segment (range/backfill) has no fetch call

**Skeptic check.** Grepped every caller of fetch_engine_blobs_and_publish_full/spawn_fetch_block_columns: gossip, HTTP, RPC lookup with MissingComponents, and tests only. The Lodestar fix stopped a post-import trigger on every import path, and Lighthouse never had that trigger, so the earlier verdict holds.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#9322](https://github.com/ChainSafe/lodestar/pull/9322)

</details>


<a id="data_availability-010"></a>
<details>
<summary><b>data_availability-010</b> Skip EL reconstruction when nothing is missing — <i>partial · low · S · cpu</i></summary>

**Idea.** Skip the EL getBlobs/sidecar build routine when the block has no KZG commitments or all its blobs or columns were already seen on gossip. This avoids needless engine calls and sidecar building.

**Gap in Lighthouse.** Before the EL call in fetch_and_process_engine_blobs_inner (or fetch_engine_blobs_and_publish_full) check data_column_known_for_observation_key and cached_data_column_indexes; if all custody columns are already known, return Ok(None). This skips getBlobs and, on V2/V3, cell computation.

**Impact.** Saves one engine RPC and, on the V2/V3 path, the blob-to-cell KZG computation when columns arrived on gossip first. Small and only in the race where columns beat getBlobs.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:142-146`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L142-L146) returns early when no KZG commitments
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:640-655`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L640-L655) and :706-726 dedupe against gossip-observed and DA-cached columns only after the engine call (and after KZG cell computation on V2/V3)
- [`beacon_node/network/src/network_beacon_processor/mod.rs:998-1010`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L998-L1010) only disable_get_blobs check before the call

**Sources.** [prysm#14915](https://github.com/OffchainLabs/prysm/pull/14915), [lighthouse#7533](https://github.com/sigp/lighthouse/pull/7533)

</details>


<a id="data_availability-011"></a>
<details>
<summary><b>data_availability-011</b> Build only custodied columns from EL blobs — <i>partial · medium · S · cpu, memory</i></summary>

**Idea.** When data column sidecars are built from EL blobs, compute only the columns that the node custodies (column bitmap), not all 128 columns that are then filtered.

**Gap in Lighthouse.** On the V2/V3 path, pass the custody index set into blobs_to_partial_data_columns / build_partial_column_cells so only custody columns are assembled (cells+proofs copied, sidecars built). compute_cells still has to run the full extension per blob, so only assembly/clone/alloc work is saved. The V4 path already does this.

**Impact.** Small CPU/alloc saving per block for non-supernodes on ELs without getBlobsV4; nothing on V4 ELs or supernodes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:158`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L158) engine_getBlobsV4 path requests and assembles only custody columns
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:686`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L686) V2/V3 path calls blobs_to_partial_data_columns with no custody set
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:700`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L700) filters to custody_columns_indices only after all columns are built
- [`beacon_node/beacon_chain/src/kzg_utils.rs:425`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L425) blobs_to_partial_data_columns signature has no column filter
- [`beacon_node/beacon_chain/src/kzg_utils.rs:725`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L725) build_partial_column_cells allocates and fills all number_of_columns columns

**Second check.** Re-read the V4 dispatch and the full V2/V3 builder chain down to build_partial_column_cells; it loops over all 128 columns, and the custody filter only runs afterwards. Found no other column-subset builder.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [nimbus#8672](https://github.com/status-im/nimbus-eth2/pull/8672)

</details>


<a id="data_availability-012"></a>
<details>
<summary><b>data_availability-012</b> Publish recovered columns off the availability path — <i>partial · medium · S · latency, bandwidth</i></summary>

**Idea.** Publish columns recovered from EL blobs or reconstruction in a detached task after storing them, so block import and DA completion do not wait on network sends. Coalesce repeated partial publishes per (block, column).

**Gap in Lighthouse.** Publishing is already off the DA path. Repeated partial publishes per (block, column) are partly deduped in the gossipsub partial-messages extension (stale publishes are dropped, peers get only deltas), but there is no time-window coalescing like prysm#17791's 250 ms batch: each merge that adds cells still triggers its own send to every peer. Add a short debounce keyed by (block_root, column) before PublishPartialColumns if chatter is measured to matter.

**Impact.** Fewer small partial-column RPCs when many partial updates arrive for one column within a short window; no DA latency gain (already non-blocking).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/mod.rs:1213`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L1213) reconstruction result published via publish_data_columns_gradually (spawned) while import status is handled independently
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:357`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L357) publish_fn is a non-blocking callback before process of engine columns
- [`beacon_node/network/src/service.rs:689`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L689) PublishPartialColumns handled on the network task, not on the import path
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1404`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1404) PublishPartialColumns sent on every merge that updates partials
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/extensions/partial_messages.rs:497 handle_publish skips a publish whose metadata adds no new parts for that (topic, group_id)
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/extensions/partial_messages.rs:536 per-peer publish_action sends only what the peer lacks

**Second check.** Beyond the earlier review, read lighthouse_network publish_partial and the pinned sigp rust-libp2p gossipsub partial_messages handle_publish: it drops no-new-data publishes and diffs per peer, which covers part of the coalescing idea but not timed batching. The prysm coalescing PR is itself still open.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [nimbus#8655](https://github.com/status-im/nimbus-eth2/pull/8655), [prysm#17791](https://github.com/OffchainLabs/prysm/pull/17791)

</details>


<a id="data_availability-013"></a>
<details>
<summary><b>data_availability-013</b> Publish only needed columns after reconstruction — <i>implemented · medium · S · cpu, bandwidth</i></summary>

**Idea.** After columns are recovered from EL blobs or by reconstruction, publish to gossip only the missing columns the node custodies or samples and the network still needs, not every recovered column. This saves outbound bandwidth and send CPU.

**Impact.** Already limits post-reconstruction publishing to needed, unseen sampling columns, published in randomized delayed batches.

**Best measured result.** 'a node custodying 65 columns published at least 64 columns per reconstruction' before (pr:lodestar#9464)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker.rs:582-604`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L582-L604) re-reads cached indices after recovery and keeps only sampling columns not already held
- [`beacon_node/network/src/network_beacon_processor/mod.rs:1263-1321`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L1263-L1321) publish_data_columns_gradually shuffles, batches and drops columns already seen on gossip (observe_gossip_data_column PriorKnown)
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:282-304`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L282-L304) EL-blob path builds only custody columns and dedups against observed/cached ones

**Skeptic check.** Confirmed: reconstruct_data_columns filters to columns_to_sample minus existing_column_indices, and the gradual publisher re-checks gossip observation before each batch. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#8648](https://github.com/status-im/nimbus-eth2/pull/8648), [lodestar#9464](https://github.com/ChainSafe/lodestar/pull/9464), [lighthouse#8269](https://github.com/sigp/lighthouse/pull/8269)

</details>


<a id="data_availability-014"></a>
<details>
<summary><b>data_availability-014</b> Mark data available at 50% columns — <i>not · medium · M · latency, bandwidth, sync</i></summary>

**Idea.** On nodes that custody all columns, treat a block as data-available once at least 50% of columns are verified (enough to reconstruct), and import it before reconstruction of the rest completes.

**Gap in Lighthouse.** lighthouse#7598 was closed unmerged. To implement, add an availability path for supernodes that succeeds with &gt;= number_of_columns/2 verified columns, import to fork choice, then fill the rest by reconstruction; DB column writes, custody/sampling checks and RPC serving must tolerate columns arriving after import.

**Impact.** Supernodes import one reconstruction time earlier (hundreds of ms) when gossip delivers 50-99% of columns; none for non-supernodes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:214`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L214) make_available requires received == num_expected_columns
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:710`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L710) get_num_expected_columns = num_of_data_columns_to_sample (128 on supernodes)
- beacon_node/beacon_chain/src/validator_custody.rs:492 should_attempt_reconstruction uses the 50% threshold only to start reconstruction
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3785`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3785) reconstruct_data_columns imports availability only after reconstruction completes

**Second check.** Checked the expected-column count source (custody context sampling size, no supernode reduction) and searched the DA checker for any half-threshold availability variant; the 50% value is only used to trigger reconstruction.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [nimbus#8417](https://github.com/status-im/nimbus-eth2/pull/8417), [lighthouse#7598](https://github.com/sigp/lighthouse/pull/7598), [teku#10248](https://github.com/Consensys-Incorporated/teku/pull/10248), [grandine#424](https://github.com/grandinetech/grandine/pull/424), [lodestar#8408](https://github.com/ChainSafe/lodestar/pull/8408), [lodestar#8818](https://github.com/ChainSafe/lodestar/pull/8818)

</details>


<a id="data_availability-015"></a>
<details>
<summary><b>data_availability-015</b> Reconstruct remaining columns locally from half — <i>implemented · medium · S · cpu, latency, bandwidth, sync</i></summary>

**Idea.** Once at least 50% of a block's data columns are held, recover the missing columns by erasure-coding cell recovery in the data availability layer, then store and publish them. This is faster than waiting for gossip or requesting every column by root from peers.

**Impact.** Supernodes already recover missing columns locally once half arrive over gossip.

**Best measured result.** &lt;800ms to recover with 20 blobs (pr:lodestar#7940)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker.rs:536-627`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L536-L627) reconstruct_data_columns recovers, imports and returns columns to publish
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:592-626`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L592-L626) check_and_set_reconstruction_started requires received &gt;= total/2
- [`beacon_node/beacon_chain/src/kzg_utils.rs:889-920`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L889-L920) per-blob recover_cells_and_compute_kzg_proofs
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1024`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1024),1465,1488 trigger after each gossip (full or completed partial) column

**Skeptic check.** Confirmed on the gossip import path, which is the hot path. Columns that arrive by RPC lookup or range sync do not call check_reconstruction_trigger, but a supernode gets all columns there, so this is not a meaningful gap. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#5781](https://github.com/sigp/lighthouse/pull/5781), [prysm#15454](https://github.com/OffchainLabs/prysm/pull/15454), [lodestar#7940](https://github.com/ChainSafe/lodestar/pull/7940), [lodestar#7935](https://github.com/ChainSafe/lodestar/pull/7935), [teku#10224](https://github.com/Consensys-Incorporated/teku/pull/10224), [prysm#17053](https://github.com/OffchainLabs/prysm/pull/17053), [nimbus#6481](https://github.com/status-im/nimbus-eth2/pull/6481), [prysm#15593](https://github.com/OffchainLabs/prysm/pull/15593), [grandine#220](https://github.com/grandinetech/grandine/pull/220), [nimbus#6553](https://github.com/status-im/nimbus-eth2/pull/6553), [prysm#15023](https://github.com/OffchainLabs/prysm/pull/15023)

</details>


<a id="data_availability-016"></a>
<details>
<summary><b>data_availability-016</b> Delay column reconstruction, bounded by slot deadline — <i>implemented · low · S · cpu, latency, sync</i></summary>

**Idea.** After reaching 50% of columns, wait a short (configurable or randomized) delay before reconstructing, and reconstruct only if columns are still missing, with the maximum delay a fraction of slot time so it ends before the attestation deadline. Missing columns often arrive via gossip or getBlobs, and reconstruction is CPU-heavy.

**Impact.** Debounced reconstruction avoids redundant CPU work when the missing columns arrive by gossip or getBlobs.

**Best measured result.** reduces the unnecessary amount of reconstructions during fast block import (commit:grandine@9e43a4aea5ad)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:73`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L73) QUEUED_RECONSTRUCTION_DELAY 150ms
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:107`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L107) RECONSTRUCTION_DEADLINE 1/4 slot
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:1139-1165`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L1139-L1165) delay queue keyed by block root, reset on every new column, zero delay past the deadline
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:613-615`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L613-L615) skip if all sampling columns already received
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3798`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3798) skip if block data already imported

**Skeptic check.** Confirmed: a debounce of 150 ms per block root, forced to zero delay after 1/4 slot, and a recheck that columns are still missing when it fires. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#7588](https://github.com/sigp/lighthouse/pull/7588), [grandine@9e43a4aea](https://github.com/grandinetech/grandine/commit/9e43a4aea5ad), [grandine#526](https://github.com/grandinetech/grandine/pull/526), [grandine@4f7f8f0ae](https://github.com/grandinetech/grandine/commit/4f7f8f0ae248), [prysm#15705](https://github.com/OffchainLabs/prysm/pull/15705), [lighthouse#7976](https://github.com/sigp/lighthouse/pull/7976), [lighthouse#8067](https://github.com/sigp/lighthouse/pull/8067)

</details>


<a id="data_availability-017"></a>
<details>
<summary><b>data_availability-017</b> Cap reconstruction debounce delay — <i>partial · low · S · cpu, latency</i></summary>

**Idea.** Put a hard maximum (for example 1 s from first enqueue) on the debounced delay before column reconstruction, so repeated column arrivals cannot postpone reconstruction and publication indefinitely.

**Gap in Lighthouse.** Store first-enqueue Instant with the DelayKey in queued_column_reconstructions and skip the reset when elapsed exceeds a max (e.g. 1s) in the DelayColumnReconstruction handler. Needed for requests whose slot is not the current slot, where the 1/4-slot rule never applies.

**Impact.** Prevents indefinite postponement of reconstruction for old-slot blocks under a steady column trickle; current-slot case already bounded to about 3s into the slot. Only matters for supernodes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:1139-1166`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L1139-L1166) every new DelayColumnReconstruction resets the delay key to 150ms
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:1142-1152`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L1142-L1152) delay becomes 0 once past 1/4 slot of the request's current slot, which bounds postponement for current-slot blocks
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:73`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L73) QUEUED_RECONSTRUCTION_DELAY; no MAX_RECONSTRUCTION_DELAY or first-enqueue time exists

**Sources.** [lighthouse#7702](https://github.com/sigp/lighthouse/pull/7702)

</details>


<a id="data_availability-018"></a>
<details>
<summary><b>data_availability-018</b> Reconstruct only on nodes custodying at least half — <i>implemented · low · S · cpu</i></summary>

**Idea.** Enable column reconstruction only when the node samples or custodies at least 50% of columns (including validator-custody supernodes), with a dynamically computed reconstruction timeout. Other nodes skip it because recovery cannot succeed.

**Impact.** Nodes that do not need more than half of the columns never schedule reconstruction.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/custody_context.rs:484-497`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L484-L497) should_attempt_reconstruction requires num_of_data_columns_to_sample (from custody_group_count_at_epoch, includes validator custody) &gt; 50%
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1488-1492`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1488-L1492) gate before scheduling
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:1140-1151`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L1140-L1151) deadline derived from slot_duration

**Skeptic check.** Confirmed: the gate uses the epoch custody group count, so validator-custody nodes that grow above 50% qualify, and the timeout is a fraction of slot duration. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#7628](https://github.com/status-im/nimbus-eth2/pull/7628), [nimbus#7558](https://github.com/status-im/nimbus-eth2/pull/7558), [teku#9994](https://github.com/Consensys-Incorporated/teku/pull/9994), [lighthouse#8052](https://github.com/sigp/lighthouse/pull/8052)

</details>


<a id="data_availability-019"></a>
<details>
<summary><b>data_availability-019</b> Run column reconstruction at most once per block — <i>implemented · medium · S · cpu, memory, disk</i></summary>

**Idea.** Record per block root that reconstruction was dispatched, is in flight or is complete (flag or lock taken before checking column counts), and return immediately on new triggers. Share one reconstruction result across concurrent requesters.

**Impact.** At most one reconstruction per block root. Its result goes into the shared DA cache for all consumers.

**Best measured result.** duplicate rate 4-6% to 0 in test (pr:lighthouse#8985)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:596-626`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L596-L626) reconstruction_started checked and set under the critical write lock before column counts are returned
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:631-636`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L631-L636) flag reset only on failure
- [`beacon_node/beacon_chain/src/pending_payload_cache/mod.rs:620-650`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/mod.rs#L620-L650) same for Gloas
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:1152-1164`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L1152-L1164) one queued reconstruction per block root
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3798`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3798) early return if block data already imported

**Skeptic check.** Confirmed: dedup at two layers (the reprocess queue keyed by root and the flag under lock), and concurrent triggers return 'already started'. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#8855](https://github.com/sigp/lighthouse/pull/8855), [lighthouse#8923](https://github.com/sigp/lighthouse/pull/8923), [lighthouse#8985](https://github.com/sigp/lighthouse/pull/8985), [lodestar#8383](https://github.com/ChainSafe/lodestar/pull/8383), [teku#11508](https://github.com/Consensys-Incorporated/teku/pull/11508), [teku#10296](https://github.com/Consensys-Incorporated/teku/pull/10296), [prysm#15528](https://github.com/OffchainLabs/prysm/pull/15528), [lighthouse#5794](https://github.com/sigp/lighthouse/pull/5794)

</details>


<a id="data_availability-020"></a>
<details>
<summary><b>data_availability-020</b> Dedicated thread pool for column reconstruction — <i>partial · low · S · cpu, latency</i></summary>

**Idea.** Run data column computation and cell recovery on a dedicated (high-priority) thread pool, separate from the general pool and the fork choice/block import threads, so heavy KZG work does not starve other tasks.

**Gap in Lighthouse.** Only cell recovery (BeaconChain::reconstruct_data_columns) is on the scoped pool. Column computation from EL blobs (fetch_blobs, blobs_to_partial_data_columns/compute_cells) and at block publish (build_data_columns) still runs par_iter on the global rayon pool. That pool is shared with other critical parallel work. Grandine moved both compute_cells and recovery to a dedicated executor.

**Impact.** Small. Recovery is the heaviest part and is already isolated. Moving cell computation would only change contention on the global pool during getBlobs bursts.

**Best measured result.** reduces p99 latency during high load (commit:grandine@9af9e4de859b)

**Evidence (Lighthouse @ 928b61e719).**

- [`common/task_executor/src/rayon_pool_provider.rs:8-56`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/task_executor/src/rayon_pool_provider.rs#L8-L56) HighPriority scoped pool (~80% CPUs)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3811`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3811),3845 reconstruction runs via spawn_blocking_with_rayon_async(HighPriority)
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:669-690`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L669-L690) EL-blob column computation via spawn_blocking_handle, so par_iter runs on the global rayon pool
- [`beacon_node/http_api/src/publish_blocks.rs:436-455`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L436-L455) build_data_columns via spawn_blocking_handle (global rayon pool)
- [`beacon_node/beacon_chain/src/kzg_utils.rs:344`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L344),401,437,477 cell computation uses into_par_iter on whatever pool is current

**Skeptic check.** The earlier evidence was right about recovery (#8075), but the idea also covers data column computation, which still uses the global rayon pool. The HighPriority pool also takes about 80% of CPUs, so it caps recovery rather than fully isolating it.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [grandine@9af9e4de8](https://github.com/grandinetech/grandine/commit/9af9e4de859b), [grandine@79f20c521](https://github.com/grandinetech/grandine/commit/79f20c52179d), [grandine#362](https://github.com/grandinetech/grandine/pull/362), [lighthouse#8075](https://github.com/sigp/lighthouse/pull/8075)

</details>


<a id="data_availability-021"></a>
<details>
<summary><b>data_availability-021</b> Run KZG and reconstruction off async and fork-choice threads — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Call PeerDAS KZG and column reconstruction (including from EL blobs and for the beacon API) in blocking tasks or a background pool, off the async runtime and the single-threaded fork choice mutator. Do not spawn a new validation task per column for the same delayed block.

**Impact.** PeerDAS KZG and reconstruction already stay off the async runtime. Lighthouse has no single-threaded fork choice mutator for this to starve.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2451-2475`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2451-L2475) gossip column verification in spawn_blocking_handle
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:669-690`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L669-L690) EL-blob column computation in spawn_blocking_handle
- [`beacon_node/http_api/src/publish_blocks.rs:436-455`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L436-L455) build_data_columns in spawn_blocking_handle
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3811`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3811),3845 reconstruction on the rayon pool via a blocking spawn
- [`beacon_node/http_api/src/lib.rs:1394`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L1394) blob_sidecars API (reconstruct_blob_sidecars) runs in blocking_response_task

**Skeptic check.** Confirmed every cited path runs in blocking tasks. Fulu gossip columns are verified on their own without waiting for the block, so the per-column task spawning for a delayed block does not happen. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#9728](https://github.com/Consensys-Incorporated/teku/pull/9728), [grandine@5d83807db](https://github.com/grandinetech/grandine/commit/5d83807db95f), [grandine@e53a535e1](https://github.com/grandinetech/grandine/commit/e53a535e114c), [nimbus#8346](https://github.com/status-im/nimbus-eth2/pull/8346), [grandine#364](https://github.com/grandinetech/grandine/pull/364), [grandine@00e4af612](https://github.com/grandinetech/grandine/commit/00e4af612278)

</details>


<a id="data_availability-022"></a>
<details>
<summary><b>data_availability-022</b> Parallel, bounded per-blob cell recovery — <i>implemented · medium · S · cpu, memory, latency</i></summary>

**Idea.** Split column reconstruction into independent per-blob cell and proof recoveries and run them in parallel on worker tasks with a bounded number in flight, using zero-copy views of inputs and reused buffers. This cuts latency while limiting peak memory and scheduling overhead.

**Impact.** Already parallel per blob on a bounded pool, with zero-copy cell references. Only buffer reuse is left, a small gain.

**Best measured result.** logs show recovery ~644ms per blob index run concurrently (pr:prysm#14236)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/kzg_utils.rs:889-920`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L889-L920) reconstruct_data_columns into_par_iter over blob rows, each row recover_cells_and_compute_kzg_proofs on KzgCellRef views
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3845`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3845) runs inside the bounded HighPriority rayon pool

**Skeptic check.** Confirmed: per-blob recovery runs in parallel, the bounded rayon pool caps in-flight work, and cells are passed as references. The API-only reconstruct_blobs_with_indices is sequential on purpose (non-critical path). The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#7758](https://github.com/status-im/nimbus-eth2/pull/7758), [nimbus#7800](https://github.com/status-im/nimbus-eth2/pull/7800), [prysm#14397](https://github.com/OffchainLabs/prysm/pull/14397), [nimbus#7351](https://github.com/status-im/nimbus-eth2/pull/7351), [nimbus#7428](https://github.com/status-im/nimbus-eth2/pull/7428), [prysm#14236](https://github.com/OffchainLabs/prysm/pull/14236)

</details>


<a id="data_availability-023"></a>
<details>
<summary><b>data_availability-023</b> Semi-supernode: custody half the columns — <i>implemented · high · S · cpu, disk, bandwidth</i></summary>

**Idea.** Offer a mode that custodies and subscribes to 64 of 128 column subnets, enough to reconstruct all blobs, to serve blobs with about half the bandwidth and storage of a supernode.

**Impact.** n/a

**Best measured result.** Storage ~50% vs supernode (64 vs 128 columns) (pr:prysm#16029)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/custody_context.rs:231`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L231) NodeCustodyType::SemiSupernode
- [`beacon_node/beacon_chain/src/custody_context.rs:243`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L243) get_custody_count_override returns number_of_custody_groups / 2
- [`beacon_node/src/cli.rs:63`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L63) --semi-supernode flag
- [`beacon_node/src/config.rs:130-135`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/config.rs#L130-L135) flag parsed into NodeCustodyType::SemiSupernode

**Skeptic check.** Verified: --semi-supernode sets the custody group count to half of the groups, which is enough for reconstruction. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#16029](https://github.com/OffchainLabs/prysm/pull/16029), [grandine@5ff11c24d](https://github.com/grandinetech/grandine/commit/5ff11c24d141), [lodestar#8568](https://github.com/ChainSafe/lodestar/pull/8568)

</details>


<a id="data_availability-024"></a>
<details>
<summary><b>data_availability-024</b> Custody first half of columns to skip reconstruction — <i>n/a · medium · S · cpu, bandwidth</i></summary>

**Idea.** Custody the first 64 columns, which hold the original blob data, so blobs can be served directly without reconstruction CPU cost.

**Impact.** Spec assigns custody groups by node_id, so a node cannot choose the first 64 columns.

**Best measured result.** avoids reconstruction CPU load (pr:nimbus#7752)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/data/data_column_custody_group.rs:28`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/data/data_column_custody_group.rs#L28),91 custody groups derived from node_id hash, not selectable

**Sources.** [nimbus#7752](https://github.com/status-im/nimbus-eth2/pull/7752)

</details>


<a id="data_availability-025"></a>
<details>
<summary><b>data_availability-025</b> Background reconstruction of historical custody columns — <i>not · medium · L · cpu, disk, bandwidth</i></summary>

**Idea.** Run a background service that reconstructs missing custody columns from stored half-sets for recent history, walking from head back to the retention floor, so full columns can be served without download.

**Gap in Lighthouse.** Add a background service that, for stored slots with &gt;=50% of columns on disk, loads them, calls kzg_utils::reconstruct_data_columns and writes missing custody columns via the historical import path (e.g. after a cgc increase) instead of custody backfill download.

**Impact.** Saves custody-backfill download bandwidth for nodes that raise cgc or turn supernode, at CPU cost.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/mod.rs:1213`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L1213) attempt_data_column_reconstruction is the only network caller, triggered from gossip_methods.rs:1510
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3785`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3785) reconstruct_data_columns works only on in-memory DA checker / pending_payload_cache entries
- [`beacon_node/beacon_chain/src/historical_data_columns.rs:190`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_data_columns.rs#L190) historical import only KZG-verifies and stores downloaded columns
- [`beacon_node/store/src/reconstruct.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/reconstruct.rs) is state reconstruction, not column reconstruction

**Second check.** Searched all reconstruct call sites in beacon_chain, network (incl. custody_backfill_sync, rpc_methods) and store; only head/gossip-time reconstruction from in-memory caches exists, and RPC serving never reconstructs from stored half-sets.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [nimbus#8533](https://github.com/status-im/nimbus-eth2/pull/8533)

</details>


<a id="data_availability-026"></a>
<details>
<summary><b>data_availability-026</b> Reconstruct API blobs from stored columns — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Serve blob sidecars in the blobs API by reconstructing them from stored data column sidecars once at least half are held, and hold sidecars as Arc to avoid copies.

**Impact.** The blobs API is already served from stored columns, with the half-columns threshold, Arc sidecars and per-index reconstruction.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/block_id.rs:367-381`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L367-L381) PeerDAS epochs serve blobs via reconstruct_blob_sidecars
- [`beacon_node/http_api/src/block_id.rs:502-531`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L502-L531) get_data_columns_for_blob_reconstruction requires &gt;= NUMBER_OF_COLUMNS/2 and returns Vec&lt;Arc&lt;DataColumnSidecar&gt;&gt;
- [`beacon_node/beacon_chain/src/kzg_utils.rs:850-880`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L850-L880) reconstructs only the requested blob indices

**Skeptic check.** Verified the mechanism. One extra cost remains, outside the idea: get_data_columns_for_blob_reconstruction loads every stored column, and reconstruct_blobs_with_indices runs full cell recovery whenever fewer than 128 columns are held, even when columns 0..63 (systematic, no recovery needed) are all present.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine#314](https://github.com/grandinetech/grandine/pull/314)

</details>


<a id="data_availability-027"></a>
<details>
<summary><b>data_availability-027</b> Share blobs, cells and sidecars by reference — <i>partial · low · M · cpu, memory</i></summary>

**Idea.** Hold blobs, blob/column sidecars and partial-column cells behind Arc/reference-counted pointers and pass them by reference between gossip, EL recovery, KZG, caches, HTTP API and routing. Each handoff then does not copy the large sidecar.

**Gap in Lighthouse.** Full blob and column sidecars are shared through Arc on the gossip, DA-cache, EL-recovery and API paths. The partial-column path does not share them: the cells are plain FixedVector&lt;u8&gt; values. KzgVerifiedCustodyPartialDataColumnFulu::merge rebuilds the cell list by cloning every cell on each merge. PartialDataColumnAssembler::merge_partials then calls try_clone_full, which copies the complete column again, although try_into_full could move it. build_partial_columns_from_v4_response copies every EL cell. Storing cells as Arc, or merging in place and moving the merged partial into the full column, would remove these copies.

**Impact.** Small: about 2 KiB of memcpy per cell, per merge and per completion, for each custody column. The cost is around milliseconds per slot at high blob counts, and it applies only when partial messages are in use.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/blob_verification.rs:15-16`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/blob_verification.rs#L15-L16) KzgVerifiedBlob holds Arc&lt;BlobSidecar&gt;
- [`beacon_node/beacon_chain/src/data_column_verification.rs:484-486`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L484-L486),745-747 verified columns hold Arc&lt;DataColumnSidecar&gt;
- [`beacon_node/beacon_chain/src/data_column_verification.rs:886-945`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L886-L945) KzgVerifiedCustodyPartialDataColumnFulu::merge deep-copies every existing and new cell (cell.clone()) into a new partial
- [`beacon_node/beacon_chain/src/partial_data_column_assembler.rs:126`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/partial_data_column_assembler.rs#L126),148-152 merge_partials calls merge and then try_clone_full, which copies the whole column again
- [`consensus/types/src/data/partial_data_column_sidecar.rs:385-399`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/data/partial_data_column_sidecar.rs#L385-L399) try_clone_full clones sidecar.column
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:565`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L565) build_partial_columns_from_v4_response copies each EL cell (cell.0.clone())

**Skeptic check.** The earlier evidence was right for full sidecars. It missed the newer partial-column path (the subject of nimbus#9081), where merge and try_clone_full deep-copy the cells.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lighthouse#4593](https://github.com/sigp/lighthouse/pull/4593), [nimbus#9081](https://github.com/status-im/nimbus-eth2/pull/9081), [lighthouse#4980](https://github.com/sigp/lighthouse/pull/4980), [nimbus#8437](https://github.com/status-im/nimbus-eth2/pull/8437), [lighthouse@750c594f5](https://github.com/sigp/lighthouse/commit/750c594f5fad)

</details>


<a id="data_availability-028"></a>
<details>
<summary><b>data_availability-028</b> Store a blob as one flat byte array — <i>n/a · low · S · memory</i></summary>

**Idea.** Represent a blob as one flat byte array instead of a 2D slice of 32-byte field elements, removing a slice header per element.

**Impact.** Go slice-of-slices overhead; Rust types are already flat byte vectors.

**Best measured result.** 24-byte slice header overhead per 32-byte element avoided (pr:prysm#11614)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/data/mod.rs:32`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/data/mod.rs#L32) Blob&lt;E&gt; = FixedVector&lt;u8, BytesPerBlob&gt; is a flat byte vector
- [`consensus/types/src/data/data_column_sidecar.rs:36`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/data/data_column_sidecar.rs#L36) Cell&lt;E&gt; is also flat bytes

**Sources.** [prysm#11614](https://github.com/OffchainLabs/prysm/pull/11614)

</details>


<a id="data_availability-029"></a>
<details>
<summary><b>data_availability-029</b> Assemble partial columns in-place in ring buffer — <i>not · low · L · memory, latency, bandwidth</i></summary>

**Idea.** Write cells from partial column messages directly into a preallocated ring buffer with per-row sub-reservations, and send per-peer cell messages from it, so there are no intermediate copies.

**Gap in Lighthouse.** Cells are copied into per-column Vecs and again into new partial messages for each send; no preallocated shared ring buffer or per-row reservation. Replace per-column Vec storage with one preallocated arena and let publish_partial slice from it (assembler, PendingColumn::to_partial).

**Impact.** Saves copies of cells (2KiB each) on partial column paths; only matters when partial columns are enabled. Small CPU/alloc gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/partial_data_column_assembler.rs:60`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/partial_data_column_assembler.rs#L60) assembler keeps cells per column (Vec&lt;Option&lt;(Cell,KzgProof)&gt;&gt;), allocated per column
- [`beacon_node/beacon_chain/src/pending_payload_cache/pending_column.rs:15`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/pending_column.rs#L15) new_with_capacity per column; to_partial copies cells into fresh Vecs (line 58)
- [`beacon_node/lighthouse_network/src/service/mod.rs:906`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L906) publish_partial sends built messages

**Sources.** [silver#242](https://github.com/gattaca-com/silver/pull/242), [silver#245](https://github.com/gattaca-com/silver/pull/245)

</details>


<a id="data_availability-030"></a>
<details>
<summary><b>data_availability-030</b> Quarantine blobs with blobless blocks until joined — <i>partial · low · M · memory, latency, bandwidth, sync</i></summary>

**Idea.** Keep gossip blobs/columns and blocks whose data is missing together in a quarantine, keeping the sidecars while the block waits, and import when both are present. Nothing is dropped and requested again.

**Gap in Lighthouse.** When the parent is known, gossip blocks and sidecars wait together in PendingComponents. When the parent is unknown (orphan case), validate_data_column_sidecar_for_gossip_fulu rejects the column with ParentUnknown. The gossip handler then sends only the header to sync (UnknownParentSidecarHeader / BlockComponent::Sidecar) and drops the column. After the parent lookup resolves, the custody lookup requests the columns again by root. This is the round trip that nimbus#6127 removed by keeping the sidecars of a quarantined block. The fix is to keep the parent-unknown sidecars (KZG-verified or pending) in the lookup or the DA cache, keyed by block root.

**Impact.** Saves one by-root column round trip per orphaned block during re-org or late-parent cases. The common path is unaffected.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:68-75`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L68-L75) PendingComponents holds the block and the verified blobs/columns until both are present
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:764-777`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L764-L777) a gossip column with GossipDataColumnError::ParentUnknown only sends UnknownParentSidecarHeader, and the column is not cached
- [`beacon_node/network/src/sync/manager.rs:903-922`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L903-L922) UnknownParentSidecarHeader starts a lookup with BlockComponent::Sidecar, which carries no column data
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1691-1695`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1691-L1695) a gossip block with an unknown parent goes to sync and does not enter the DA cache

**Skeptic check.** The earlier evidence was right for the normal path: block and sidecars are joined in PendingComponents. In the unknown-parent case, Lighthouse drops the gossip sidecars and requests them again, which is what the idea says to avoid.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [nimbus#4808](https://github.com/status-im/nimbus-eth2/pull/4808), [nimbus#6127](https://github.com/status-im/nimbus-eth2/pull/6127)

</details>


<a id="data_availability-031"></a>
<details>
<summary><b>data_availability-031</b> Cache columns with unknown parent block — <i>not · medium · M · latency, sync</i></summary>

**Idea.** Cache data column sidecars whose parent block is unknown and validate them when the parent arrives, instead of discarding and fetching them again.

**Gap in Lighthouse.** Park ParentUnknown columns in a bounded queue keyed by parent root (the existing UnknownBlockDataColumn reprocess queue, MAXIMUM_QUEUED_DATA_COLUMNS=256, is a natural home) and re-run gossip validation when the parent imports; needs spam limits since signature cannot be checked yet.

**Impact.** Avoids re-fetching columns by RPC when a parent arrives late; small, rare bandwidth saving.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_column_verification.rs:1717`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1717) returns GossipDataColumnError::ParentUnknown
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:764-776`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L764-L776) sends only SyncMessage::UnknownParentSidecarHeader (no sidecar) and the column is ignored
- [`beacon_node/network/src/sync/manager.rs:154-160`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L154-L160) UnknownParentSidecarHeader carries only header info; manager.rs:903 passes BlockComponent::Sidecar with no payload
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:147`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L147) UnknownBlockDataColumn queue exists only for BlockRootUnknown, not ParentUnknown

**Second check.** Checked the reprocessing queue: a column-parking mechanism exists but only for the BlockRootUnknown case; the sync message for unknown-parent sidecars is explicitly decoupled from the sidecar, so the column is dropped.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [silver#157](https://github.com/gattaca-com/silver/pull/157)

</details>


<a id="data_availability-032"></a>
<details>
<summary><b>data_availability-032</b> Per-root indexed sidecar quarantine lookups — <i>implemented · low · S · cpu</i></summary>

**Idea.** Index the blob/column quarantine by block root and slot for O(1) lookups, check column completeness with one per-root gather instead of one hash lookup per column, and use one pop returning an Option instead of has-then-pop.

**Impact.** n/a

**Best measured result.** Stated: API calls go from O(n) to O(1) (pr:nimbus#7100)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:351`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L351) LRU keyed by block_root holding PendingComponents
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:84-92`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L84-L92) get_cached_data_column is a linear scan over at most 128 entries of a single root
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:213`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L213) completeness is a length compare

**Skeptic check.** Verified: the lookup is O(1) per root and completeness is a single length check. The earlier evidence was correct, and the scan within a root is negligible.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#7100](https://github.com/status-im/nimbus-eth2/pull/7100), [nimbus#7076](https://github.com/status-im/nimbus-eth2/pull/7076)

</details>


<a id="data_availability-033"></a>
<details>
<summary><b>data_availability-033</b> Cache custody column set per node — <i>implemented · low · S · cpu</i></summary>

**Idea.** Compute the custody and sampling column indices for the node id once, store them as a hash set (swapped atomically when custody count changes), and use it for O(1) membership checks.

**Impact.** n/a

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/custody_context.rs:265`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L265) ordered_custody_column_indices stored once on CustodyContext
- [`beacon_node/beacon_chain/src/custody_context.rs:507-510`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L507-L510) sampling_columns_for_epoch returns a prefix slice, no recomputation
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:366-369`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L366-L369) membership via slice contains
- [`beacon_node/lighthouse_network/src/peer_manager/peerdb/peer_info.rs:50`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/peerdb/peer_info.rs#L50),231 peer custody subnets cached as HashSet

**Skeptic check.** Verified: the column order is computed once, and a CGC change only changes the prefix length. Peer custody sets are cached HashSets. Membership uses a slice scan instead of a hash set, but with at most 128 entries this does not matter.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#10446](https://github.com/Consensys-Incorporated/teku/pull/10446), [prysm#14893](https://github.com/OffchainLabs/prysm/pull/14893), [nimbus#7210](https://github.com/status-im/nimbus-eth2/pull/7210)

</details>


<a id="data_availability-034"></a>
<details>
<summary><b>data_availability-034</b> Batch KZG verify sidecars from RPC and sync — <i>implemented · medium · S · cpu, latency, sync</i></summary>

**Idea.** Verify KZG proofs of all blob/column sidecars received by RPC or range sync for a block or batch together with batch KZG verification, instead of one by one.

**Impact.** n/a

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker.rs:335-340`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L335-L340) put_rpc_blobs batch-verifies via KzgVerifiedBlobList::new
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:358`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L358) put_rpc_custody_columns uses from_batch_with_scoring
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:495-526`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L495-L526) batch_verify_kzg_for_range_sync_blocks: blobs batched across the whole batch, columns batched per block
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:676`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L676) range sync calls it
- [`crypto/kzg/src/lib.rs:222-302`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/kzg/src/lib.rs#L222-L302) verify_cell_proof_batch groups by column and verifies in parallel

**Skeptic check.** Verified: RPC and range-sync sidecars are verified with batch KZG, never one by one. For range sync, Fulu columns are batched per block, not across blocks. Each per-block call is already a parallel batch over all cells, so a cross-block batch would gain little.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#13351](https://github.com/OffchainLabs/prysm/pull/13351), [lighthouse#4736](https://github.com/sigp/lighthouse/pull/4736)

</details>


<a id="data_availability-035"></a>
<details>
<summary><b>data_availability-035</b> Batch gossip column verification per block — <i>not · medium · M · cpu, latency</i></summary>

**Idea.** Collect gossip data column sidecars of the same block header and verify their KZG cell proofs in one batch, with the inclusion proof and header signature verified once per batch.

**Gap in Lighthouse.** Add a per-block-root gossip column batching work type in the beacon processor that verifies header signature and inclusion proof once and calls verify_kzg_for_data_column_list once for the batch, falling back to per-column on failure.

**Impact.** Supernodes verify up to 128 columns per block separately; batching could cut gossip column verification CPU several-fold (Lodestar 3-4x) for a few tens of ms latency.

**Best measured result.** job time 3x-4x faster, saves ~250ms; ~35ms more wait time (pr:lodestar#7910)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_column_verification.rs:1178-1193`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1178-L1193) per-sidecar inclusion proof, proposer signature and verify_kzg_for_data_column
- [`beacon_node/beacon_processor/src/lib.rs:417`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L417) GossipDataColumnSidecar is a single AsyncFn work item; batching exists only for attestations/aggregates (lib.rs:110,390,409)
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1166`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1166) missing_cells_for_column_sidecar skips KZG for cells already known (getBlobs/partials) - dedup, not batching
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1331`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1331) partial-column path reuses a cached verified header, but only for partial messages

**Second check.** Beyond the earlier review, checked the beacon processor batching work types, the missing-cells KZG skip and the partial-column header cache; none batches full gossip columns' KZG or shares header verification across full sidecars.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [lodestar#7910](https://github.com/ChainSafe/lodestar/pull/7910)

</details>


<a id="data_availability-036"></a>
<details>
<summary><b>data_availability-036</b> Combine by-root sidecar requests per peer — <i>implemented · medium · S · bandwidth, sync</i></summary>

**Idea.** Send one by-root RPC request per peer for all missing blobs or columns of a block (or several sampling requests), instead of one request per sidecar.

**Impact.** n/a

**Best measured result.** saves bandwidth (stated, no numbers) (pr:teku#8952)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context/custody.rs:231-275`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L231-L275) continue_requests groups missing columns into columns_to_request_by_peer
- [`beacon_node/network/src/sync/network_context/custody.rs:271`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L271) one DataColumnsByRootRequest per peer with all its indices

**Skeptic check.** Verified: the custody lookup sends one by-root request per selected peer for all the columns it is given. A deterministic per-request hash order keeps the columns from fragmenting across peers. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#8952](https://github.com/Consensys-Incorporated/teku/pull/8952), [lighthouse#6256](https://github.com/sigp/lighthouse/pull/6256)

</details>


<a id="data_availability-037"></a>
<details>
<summary><b>data_availability-037</b> Cap columns per by-root request — <i>partial · low · S · bandwidth</i></summary>

**Idea.** Limit the number of data columns asked from one peer in one request, so peers are not overloaded and requests do not time out.

**Gap in Lighthouse.** Only the protocol-wide maximum (16384 sidecars) is enforced; the requester does not cap columns per by-root request. Per-peer batches are naturally small since each peer custodies few columns. In custody.rs batch loop, chunk indices per peer into requests of a fixed size (e.g. 8-16 columns) and track multiple req_ids per peer.

**Impact.** Avoids timeouts for one oversized request to a supernode peer; rare on mainnet.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/handler.rs:971`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L971) inbound limit max_request_data_column_sidecars
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1779`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1779) rejects requests above max
- [`beacon_node/network/src/sync/network_context/custody.rs:255-300`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L255-L300) groups all needed indices per peer into one request with no client-side cap

**Sources.** [caplin#16989](https://github.com/erigontech/erigon/pull/16989), [caplin#16207](https://github.com/erigontech/erigon/pull/16207)

</details>


<a id="data_availability-038"></a>
<details>
<summary><b>data_availability-038</b> Request columns only from custody peers — <i>implemented · medium · S · bandwidth, sync</i></summary>

**Idea.** Send by-root column requests only to peers whose custody set contains the columns, and filter each request to the columns the chosen peer custodies before sending it.

**Impact.** n/a

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context/custody.rs:353-388`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L353-L388) select_column_peer draws only from cx.get_custodial_peers(column_index, block_slot)
- [`beacon_node/network/src/sync/network_context.rs:418`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L418) get_custodial_peers
- [`beacon_node/lighthouse_network/src/peer_manager/peerdb.rs:297`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/peerdb.rs#L297) good_custody_subnet_peer respects custody subnets and earliest_available_slot
- [`beacon_node/network/src/sync/network_context/custody.rs:254-258`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L254-L258) each peer's request holds only the columns that it was selected for

**Skeptic check.** Verified: a peer is chosen per column only from the peers that custody that column, so each per-peer request is already filtered to that peer's custody columns. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#14452](https://github.com/OffchainLabs/prysm/pull/14452), [caplin#17392](https://github.com/erigontech/erigon/pull/17392), [caplin#18025](https://github.com/erigontech/erigon/pull/18025)

</details>


<a id="data_availability-039"></a>
<details>
<summary><b>data_availability-039</b> Hedge slow column requests to alternate peers — <i>not · medium · M · latency, sync</i></summary>

**Idea.** After a delay, send a slow in-flight data column request again to another custody peer, bounded to a fraction of pending requests and two attempts per request.

**Gap in Lighthouse.** There is no hedging. A slow in-flight DataColumnsByRoot request is never duplicated to another custody peer. Only an RPC error or timeout moves the column back to NotStarted (max 3 attempts). The fix needs a send timestamp in Status::Downloading, a timer in ActiveCustodyRequest that re-issues still-pending columns to a different peer after a delay, a cap of 2 attempts per column, and a global cap on the fraction of hedged requests.

**Impact.** Lower tail latency for column lookups and gossip-miss recovery when a custody peer is slow. It costs a small amount of extra bandwidth.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context/custody.rs:405-415`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L405-L415) column Status is NotStarted(Instant)/Downloading(req_id)/Downloaded; no send time or deadline on Downloading
- [`beacon_node/network/src/sync/network_context/custody.rs:448-460`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L448-L460) Downloading only returns to NotStarted on download error
- [`beacon_node/network/src/sync/network_context/custody.rs:205`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L205) continue_requests only issues requests for NotStarted columns
- [`beacon_node/network/src/sync/range_sync/chain.rs:247`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L247) range/backfill re-request only after peer removal or batch failure, not on slowness

**Second check.** Searched sync/ and lighthouse_network/ for hedge, speculative, slow-peer and re-request logic, including range, backfill and custody_backfill. All re-requests are failure-driven. The only slow_peer hits are gossipsub scoring parameters, which do not apply to RPC.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [teku#11011](https://github.com/Consensys-Incorporated/teku/pull/11011)

</details>


<a id="data_availability-040"></a>
<details>
<summary><b>data_availability-040</b> Insert EL-built columns in one batch — <i>implemented · low · S · cpu</i></summary>

**Idea.** Put the columns built from getBlobs into the column quarantine in one batch capped at the needed count, instead of one insert per column.

**Impact.** Already one batch insert per block. The Nimbus cap at half+1 does not apply, because Lighthouse must store all of its custody columns.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:282-298`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L282-L298) compute_custody_columns_to_import filters to custody columns before import
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:317-330`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L317-L330) import_custody_partial_columns merges all EL-built columns in one merge_partials call
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:483`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L483) put_kzg_verified_data_columns takes the whole set under one pending-components update

**Skeptic check.** The Nimbus diff replaces a per-column quarantine put with one batch put. Lighthouse already imports the filtered custody set in one assembler/cache call. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#7725](https://github.com/status-im/nimbus-eth2/pull/7725)

</details>


<a id="data_availability-041"></a>
<details>
<summary><b>data_availability-041</b> Async access to pending sidecar maps — <i>n/a · low · latency</i></summary>

**Idea.** Access the pending-reconstruction and received-column maps through async methods so tasks yield instead of blocking on lock contention.

**Impact.** Lighthouse caches are guarded by sync parking_lot locks held briefly, not async tasks over shared maps; async access does not apply.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:503`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L503) uses synchronous parking_lot RwLock with short critical sections
- [`beacon_node/beacon_chain/src/partial_data_column_assembler.rs:66`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/partial_data_column_assembler.rs#L66) sync assembler

**Sources.** [grandine@dbe7dba8a](https://github.com/grandinetech/grandine/commit/dbe7dba8ab91), [grandine@4355744bd](https://github.com/grandinetech/grandine/commit/4355744bdbcd)

</details>


<a id="data_availability-042"></a>
<details>
<summary><b>data_availability-042</b> Sidecar validation without state advancement — <i>implemented · medium · S · cpu, memory, latency</i></summary>

**Idea.** Verify a blob/column sidecar's proposer index from a proposer cache computed once per block, or use an existing state or hold the sidecar until a state exists, instead of running slot processing for each sidecar in gossip validation.

**Impact.** Column gossip validation reads the proposer from a cache computed once per (epoch, decision root); a miss loads the parent state once and the OnceCell stops other threads from doing the same work again.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_column_verification.rs:1732`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1732) verify_proposer_and_signature
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1746`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1746) chain.with_proposer_cache keyed by proposer_shuffling_root
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:188-201`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L188-L201) get_or_insert_key + OnceCell get_or_try_init, state_provider only on miss
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:321`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L321) ensure_state_can_determine_proposers_for_epoch advances only to the decision epoch on a miss

**Skeptic check.** Verified that the cache is shared across all columns of a block, and that the OnceCell dedupes concurrent misses. Blob gossip verification no longer exists post-Fulu (blob_verification.rs is a 152-line wrapper). The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine#192](https://github.com/grandinetech/grandine/pull/192), [grandine@f6d472f38](https://github.com/grandinetech/grandine/commit/f6d472f38b7f), [grandine#183](https://github.com/grandinetech/grandine/pull/183), [grandine@181823273](https://github.com/grandinetech/grandine/commit/1818232735c6), [prysm#14231](https://github.com/OffchainLabs/prysm/pull/14231), [prysm#17776](https://github.com/OffchainLabs/prysm/pull/17776)

</details>


<a id="data_availability-043"></a>
<details>
<summary><b>data_availability-043</b> Avoid collecting vectors in pending-column check — <i>not · low · S · cpu, memory</i></summary>

**Idea.** In the pending-columns availability check, iterate directly or use a short-circuit any() instead of collecting column indices into a Vec, which avoids an allocation.

**Gap in Lighthouse.** Index lists are collected into a Vec/HashSet where a short-circuit iterator could be used; the hot cache check itself (make_available) compares counts. Return an iterator or use any()/contains in the callers of cached_data_column_indexes and in the HashSet check in data_availability_checker.rs:911.

**Impact.** Saves a tiny allocation per call (at most 128 entries); negligible.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:112`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L112) get_cached_data_columns_indices collects into a Vec
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:180`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L180) cached_data_column_indexes returns that Vec
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:911`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L911) collects sampling columns into a HashSet to check missing ones

**Sources.** [grandine#331](https://github.com/grandinetech/grandine/pull/331), [grandine@1aa81e630](https://github.com/grandinetech/grandine/commit/1aa81e630ed0)

</details>


<a id="data_availability-044"></a>
<details>
<summary><b>data_availability-044</b> Prune blob and column data past DA window — <i>implemented · medium · M · disk</i></summary>

**Idea.** Delete blob/column sidecars older than the data availability retention window (and non-canonical ones at finalization), with storage keyed by slot so pruning can stream in order. This keeps disk use bounded.

**Impact.** Disk use is bounded by DA-window pruning and fork pruning. Only the slot-keyed layout is missing. That would make the prune walk cheaper, but it is a small cost on mainnet.

**Best measured result.** 1.6TB in caplin dir on a Hoodi node (pr:caplin#20379)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3277`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3277) try_prune_blobs prunes blobs/columns up to DA boundary minus margin
- [`beacon_node/store/src/hot_cold_store.rs:3367`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3367) ParentRootBlockIterator walk with get_all_data_column_keys per block
- [`beacon_node/beacon_chain/src/migrate.rs:249`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L249) try_prune_blobs called from the background migrator
- [`beacon_node/beacon_chain/src/migrate.rs:777-789`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L777-L789) DeleteBlobs/DeleteDataColumns for abandoned forks at finalization

**Skeptic check.** Both pruning paths are confirmed. The storage is keyed by block_root, not slot, so pruning walks parents backwards instead of doing a range delete. That is a secondary detail of the idea, so the verdict stays implemented, as the earlier gap note said.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#3852](https://github.com/sigp/lighthouse/pull/3852), [caplin#20379](https://github.com/erigontech/erigon/pull/20379), [teku#6587](https://github.com/Consensys-Incorporated/teku/pull/6587)

</details>


<a id="data_availability-045"></a>
<details>
<summary><b>data_availability-045</b> Derive column retention window from chain config — <i>implemented · low · S · disk</i></summary>

**Idea.** Compute the data column retention window as epochs times slots-per-epoch from the chain config, not a mainnet slot default, so chains with shorter epochs do not keep twice the data.

**Impact.** None. Retention is computed in epochs and converted with the chain's own EthSpec, so gnosis does not keep extra data.

**Best measured result.** gnosis retained 131072 slots against a 65536 window (2x) (pr:caplin#23610)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/core/chain_spec.rs:941-951`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/core/chain_spec.rs#L941-L951) min_epoch_data_availability_boundary works in epochs from config
- [`consensus/types/src/core/chain_spec.rs:2407`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/core/chain_spec.rs#L2407) min_epochs_for_data_column_sidecars_requests is a config field
- [`common/eth2_network_config/built_in_network_configs/gnosis/config.yaml:167`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2_network_config/built_in_network_configs/gnosis/config.yaml#L167) MIN_EPOCHS_FOR_DATA_COLUMN_SIDECARS_REQUESTS 16384
- [`beacon_node/store/src/hot_cold_store.rs:3263`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3263) pruning uses this epoch boundary, converted with E::slots_per_epoch()

**Skeptic check.** A grep found no hard-coded mainnet slot window in beacon_node. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#23610](https://github.com/erigontech/erigon/pull/23610)

</details>


<a id="data_availability-046"></a>
<details>
<summary><b>data_availability-046</b> Never prune blobs needed at chain tip — <i>implemented · low · S · latency</i></summary>

**Idea.** Limit pruning to blobs below what tip block processing still needs, so over-pruning does not force blob refetches.

**Impact.** Pruning only touches finalized data older than the DA boundary, so blobs needed at the tip are never pruned.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3277`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3277) try_prune_blobs retains from data_availability_boundary - blob_prune_margin_epochs
- [`beacon_node/store/src/hot_cold_store.rs:3305-3308`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3305-L3308) end_epoch = min(DA boundary - margin - 1, split epoch - 1)

**Skeptic check.** Verified that the end_epoch bound is capped by both the DA boundary and the split. The Caplin over-pruning bug cannot happen here, so the earlier verdict holds.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#9863](https://github.com/erigontech/erigon/pull/9863)

</details>


<a id="data_availability-047"></a>
<details>
<summary><b>data_availability-047</b> Cheap filesystem traversal for blob pruning — <i>n/a · low · cpu, disk</i></summary>

**Idea.** When pruning file-based blob storage, walk directories with the efficient directory-iteration syscall and cache root-to-slot lookups from earlier passes, instead of a stat or file read per blob.

**Impact.** Lighthouse stores blobs and columns in the key-value DB, not per-blob files, so directory-walk cost does not exist.

**Best measured result.** The pruning routine appears to consume a ton of disk or syscall resources on some systems (pr:prysm#13425)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3395`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3395) pruning deletes DB keys (BeaconBlob/BeaconDataColumn) via blobs_db, not files

**Sources.** [prysm#13425](https://github.com/OffchainLabs/prysm/pull/13425), [prysm#13410](https://github.com/OffchainLabs/prysm/pull/13410)

</details>


<a id="data_availability-048"></a>
<details>
<summary><b>data_availability-048</b> Incremental capped low-priority blob pruning — <i>partial · low · S · cpu, disk, latency</i></summary>

**Idea.** Prune blobs often in small capped chunks on a low-priority single thread, reading keys only from the KV store, instead of deleting a whole epoch at once.

**Gap in Lighthouse.** Prune already runs about every epoch so chunks are small, but there is no per-run cap, no low-priority thread, and existence is probed with 128 key_exists calls per block. Add a cap on blocks per run in try_prune_blobs and replace get_all_data_column_keys probing with one prefix key scan on BeaconDataColumn.

**Impact.** Small: removes bursts after long pauses (checkpoint sync, prune disabled) and ~128 point lookups per block; minor on steady state.

**Best measured result.** Cap 32 per minute vs about 5 new sidecars per minute (pr:teku#6628)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3277`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3277) try_prune_blobs deletes everything from oldest_data_slot to end_epoch in one batch
- [`beacon_node/store/src/config.rs:30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L30) DEFAULT_EPOCHS_PER_BLOB_PRUNE = 1 so each run is about one epoch
- [`beacon_node/store/src/hot_cold_store.rs:3391`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3391) key_exists called per column index (128 per block) instead of key-only listing
- [`beacon_node/store/src/hot_cold_store.rs:3250`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3250) runs on the migrator thread after finalization, no priority control

**Sources.** [teku#6628](https://github.com/Consensys-Incorporated/teku/pull/6628), [teku#6758](https://github.com/Consensys-Incorporated/teku/pull/6758)

</details>


<a id="data_availability-049"></a>
<details>
<summary><b>data_availability-049</b> Store blob sidecars in KV database — <i>implemented · low · S · memory, disk</i></summary>

**Idea.** Store blob sidecars in the key-value database (root to commitments, commitment to blob) instead of per-blob files with in-memory index maps.

**Impact.** Sidecars are already KV-stored, keyed by block root (and column index), with no per-blob files.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:67-68`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L67-L68) blobs_db KV database
- [`beacon_node/store/src/hot_cold_store.rs:943`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L943) blobs_as_kv_store_ops, :1003 data_columns_as_kv_store_ops
- [`beacon_node/store/src/hot_cold_store.rs:2694`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2694) get_data_column reads DBColumn::BeaconDataColumn from blobs_db

**Skeptic check.** Lighthouse has always stored blobs and columns in the KV store. The earlier verdict is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#9469](https://github.com/erigontech/erigon/pull/9469)

</details>


<a id="data_availability-050"></a>
<details>
<summary><b>data_availability-050</b> Persist data columns in dedicated disk store — <i>implemented · low · S · disk</i></summary>

**Idea.** Persist data column sidecars in their own on-disk store.

**Impact.** Columns already live in their own on-disk database, apart from the hot and cold DBs.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:67-68`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L67-L68) separate blobs_db
- [`beacon_node/store/src/hot_cold_store.rs:2694`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2694) get_data_column reads DBColumn::BeaconDataColumn from blobs_db
- [`beacon_node/store/src/hot_cold_store.rs:2684`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2684) block_cache LRU in front of disk reads

**Skeptic check.** Verified the dedicated blobs_db and the column reads from it. The earlier verdict is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [silver#39](https://github.com/gattaca-com/silver/pull/39)

</details>


<a id="data_availability-051"></a>
<details>
<summary><b>data_availability-051</b> In-memory index of stored sidecars — <i>not · low · M · disk, startup</i></summary>

**Idea.** Keep an in-memory index of which blob/column sidecars are on disk (warmed at startup, updated on writes) so availability and presence checks do no filesystem reads.

**Gap in Lighthouse.** Add an in-memory set of (root,index) warmed at startup and maintained in put/delete in store ops; use it in get_data_column_keys. LH presence checks on hot paths hit LRU or the KV store, which is cheap (not filesystem).

**Impact.** Saves a few DB key scans in pruning/HTTP; negligible on RPC serving path.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2655`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2655) get_data_column_keys iterates DB prefix
- [`beacon_node/store/src/hot_cold_store.rs:2684`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2684) per-column get with LRU block_cache; no presence index
- [`beacon_node/beacon_chain/src/migrate.rs:788`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L788) pruning uses key scan

**Sources.** [prysm#15257](https://github.com/OffchainLabs/prysm/pull/15257), [prysm#13788](https://github.com/OffchainLabs/prysm/pull/13788)

</details>


<a id="data_availability-052"></a>
<details>
<summary><b>data_availability-052</b> Faster column reads from storage — <i>partial · low · S · cpu, disk</i></summary>

**Idea.** Read data columns from storage without unnecessary reads in Get.

**Gap in Lighthouse.** get_data_columns could iterate the prefix once and decode values directly, or use get_data_column_keys on keys only. Only called from HTTP API and one sync path; RPC serving uses single get_data_column with LRU cache.

**Impact.** Halves DB reads for whole-block column fetches on HTTP API; not on the p2p hot path.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2601`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2601) get_data_columns lists keys with iter_column_from (reads values) then get_data_column re-reads each
- [`beacon_node/store/src/hot_cold_store.rs:2655`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2655) get_data_column_keys

**Sources.** [prysm#15309](https://github.com/OffchainLabs/prysm/pull/15309)

</details>


<a id="data_availability-053"></a>
<details>
<summary><b>data_availability-053</b> Snapshot sidecar index cache at shutdown — <i>n/a · low · startup</i></summary>

**Idea.** Write the data column sidecar index cache to a snapshot file on graceful shutdown and load it on start, instead of walking the whole sidecar directory to warm it.

**Impact.** Lighthouse stores sidecars in a KV database with no startup directory walk, so there is nothing to warm or snapshot.

**Best measured result.** Warm-up 3.26s to 114ms; archive nodes could take over 20 minutes (pr:prysm#17762)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2655`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2655) no in-memory index to snapshot

**Sources.** [prysm#17762](https://github.com/OffchainLabs/prysm/pull/17762)

</details>


<a id="data_availability-054"></a>
<details>
<summary><b>data_availability-054</b> Skip re-verifying already verified sidecars — <i>partial · medium · S · cpu, latency</i></summary>

**Idea.** Track in the DA cache or quarantine which blob/column sidecars were already KZG-verified (gossip or EL) and at fork choice import or RPC processing verify only sidecars from unverified sources; accept identical known columns without re-verifying.

**Gap in Lighthouse.** The gossip and EL paths already skip identical known columns, and they KZG-verify only the missing cells. The RPC response path (put_rpc_custody_columns for Fulu and Gloas, and put_rpc_blobs) still verifies every sidecar, even when a column with the same content arrived by gossip while the request was in flight. The fix is to filter out exact matches against the cached KZG-verified columns before from_batch_with_scoring. Open PR sigp/lighthouse#10363 does this but is not merged.

**Impact.** Avoids redundant KZG batch verification of RPC columns that overlap with gossip arrivals during an in-flight lookup. PR #10363 measured about 1.4 ms saved per 8-column batch with 4 overlapping columns. This is a small, occasional saving.

**Best measured result.** verifySidecars often 350+ ms (samples 33 ms to 473 ms) (pr:nimbus#8542)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_column_verification.rs:422-443`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L422-L443) gossip column identical to a cached one (EL getBlobs or partials) is not re-KZG-verified: PriorKnownUnpublished
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1160-1175`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1160-L1175) same in the full gossip verification path; only missing cells go to KZG
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:187-246`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L187-L246) missing_cells_for_column_sidecar compares with the cached full column or partial cells and returns None when all are known
- [`beacon_node/network/src/sync/network_context.rs:971-990`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L971-L990) lookups request only columns not yet cached at request time
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:350-360`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L350-L360) put_rpc_custody_columns batch-KZG-verifies every returned column without a cache check
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:322-340`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L322-L340) put_rpc_blobs verifies all blobs without a cache check
- [`beacon_node/beacon_chain/src/pending_payload_cache/mod.rs:321-327`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/mod.rs#L321-L327) Gloas RPC path: from_batch_with_scoring_and_commitments, also no cache check

**Second check.** Beyond the earlier review, I found that the gossip path does skip identical cached columns and verifies only missing cells (data_column_verification.rs:431, data_availability_checker.rs:187). Lookups also exclude columns cached at request time, so the remaining gap is only RPC responses that race with gossip. Gloas pending_payload_cache has the same gap.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [teku#6636](https://github.com/Consensys-Incorporated/teku/pull/6636), [grandine@0e22c0ff9](https://github.com/grandinetech/grandine/commit/0e22c0ff9663), [lodestar#8139](https://github.com/ChainSafe/lodestar/pull/8139), [nimbus#8542](https://github.com/status-im/nimbus-eth2/pull/8542), [nimbus#8628](https://github.com/status-im/nimbus-eth2/pull/8628), [lighthouse#10363](https://github.com/sigp/lighthouse/pull/10363), [lighthouse#7493](https://github.com/sigp/lighthouse/pull/7493), [nimbus#8841](https://github.com/status-im/nimbus-eth2/pull/8841)

</details>


<a id="data_availability-055"></a>
<details>
<summary><b>data_availability-055</b> Drop sidecars and fetches for imported blocks — <i>partial · low · S · cpu, memory, bandwidth</i></summary>

**Idea.** Ignore received blob/column sidecars and skip pending RPC fetches for blocks already imported with DA satisfied or whose tracker was removed, and do not register historical sync data in the gossip blob pool. No redundant verification, requests or pool growth occur.

**Gap in Lighthouse.** A column not previously observed that arrives after the block is imported (or for a column outside the custody set) still goes through inclusion proof, signature and KZG verification. Add an early check in validate_data_column_sidecar_for_gossip_fulu against fork choice / DA checker for block_root already imported and return an ignore error. Gossip blob pool does not exist so that part is n/a.

**Impact.** Saves KZG cell verification (a few ms per late column) on duplicates arriving after import; modest, a handful of columns per block.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_column_verification.rs:1152`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1152) verify_is_unknown_sidecar drops columns already observed
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:187`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L187) missing_cells_for_column_sidecar returns None when column already cached (skips KZG)
- [`beacon_node/network/src/sync/network_context.rs:730`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L730) block_lookup_request skips fetch when block ExecutionValidated/known
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1139`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1139) no check that the block is already imported with DA satisfied before inclusion proof and KZG

**Sources.** [teku#7231](https://github.com/Consensys-Incorporated/teku/pull/7231), [grandine@f67342dc9](https://github.com/grandinetech/grandine/commit/f67342dc9f92), [grandine#140](https://github.com/grandinetech/grandine/pull/140), [teku#10789](https://github.com/Consensys-Incorporated/teku/pull/10789)

</details>


<a id="data_availability-056"></a>
<details>
<summary><b>data_availability-056</b> Bound or fail fast on DA wait — <i>n/a · medium · latency, sync</i></summary>

**Idea.** During sync, payload envelope import and block import, bound the data availability or sampling wait (for example one slot) or check availability synchronously and return an error so the batch or block is retried, instead of waiting indefinitely on a gossip subscription.

**Impact.** Lighthouse DA is a non-blocking pending-components cache; import returns MissingComponents and completes when data arrives, so there is no wait on a gossip subscription to bound.

**Best measured result.** Fixed devnet sync dead-end at batch boundary (pr:prysm#16978)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:209`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L209) MissingComponents returned, not awaited
- [`beacon_node/beacon_chain/src/payload_envelope_verification/import.rs:139`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/import.rs#L139) envelope import returns MissingComponents status

**Sources.** [prysm#16991](https://github.com/OffchainLabs/prysm/pull/16991), [prysm#16978](https://github.com/OffchainLabs/prysm/pull/16978), [prysm#16993](https://github.com/OffchainLabs/prysm/pull/16993), [prysm#17152](https://github.com/OffchainLabs/prysm/pull/17152), [prysm#16994](https://github.com/OffchainLabs/prysm/pull/16994), [teku#10694](https://github.com/Consensys-Incorporated/teku/pull/10694)

</details>


<a id="data_availability-057"></a>
<details>
<summary><b>data_availability-057</b> Bounded cache of in-flight sampled blocks — <i>implemented · low · S · memory</i></summary>

**Idea.** Keep blocks awaiting column sampling in a bounded cache with eviction, serve them to peers from it, and skip refetching blocks already held.

**Impact.** Bounded LRU holds in-flight blocks, serves them over req/resp and lets sync skip refetching.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:351`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L351) critical: RwLock&lt;LruCache&lt;Hash256, PendingComponents&gt;&gt;
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:379`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L379) get_cached_block peeks pre-execution and executed blocks
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1390`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1390) get_block_process_status checks DA cache then pending_payload_cache
- [`beacon_node/beacon_chain/src/beacon_block_streamer.rs:173`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_block_streamer.rs#L173) BlocksByRoot serves from the caches
- [`beacon_node/network/src/sync/network_context.rs:742`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L742) lookups skip download when block is cached
- [`beacon_node/beacon_chain/src/pending_payload_cache/mod.rs:118`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/mod.rs#L118) Gloas cache is also a bounded LruCache(32)

**Skeptic check.** Verified the DA cache is a bounded LruCache, that BlocksByRoot (block streamer) and BlobsByRoot read from it, and that sync lookups consult get_block_process_status. Earlier evidence was right; the Gloas pending_payload_cache is bounded too.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#10533](https://github.com/Consensys-Incorporated/teku/pull/10533), [teku#10264](https://github.com/Consensys-Incorporated/teku/pull/10264)

</details>


<a id="data_availability-058"></a>
<details>
<summary><b>data_availability-058</b> Run DA check concurrently with block verification — <i>partial · medium · M · latency</i></summary>

**Idea.** Persist gossip blobs from the gossip handler and run the data availability check concurrently with consensus verification and EL newPayload (one cancel-on-failure group), joining only at the end instead of running sequentially.

**Gap in Lighthouse.** On the gossip and envelope paths, the DA check is a cache join at the end. Range sync and RPC blocks that carry columns work differently: signature_verify_chain_segment (verify_columns_against_block) and SignatureVerifiedBlock::into_execution_pending_block_slashable (verify_kzg_for_available_block) run column KZG verification in sequence before signature verification, state transition and newPayload. KZG is not run in parallel with them and joined at import.

**Impact.** Gossip path: nothing to gain. Range sync: KZG for the whole segment (128 columns per block on supernodes) is serial with signature and execution work. Overlapping it would improve sync throughput.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker.rs:394-417`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L394-L417) gossip columns verified in their own handler and put into the pending cache
- [`beacon_node/beacon_chain/src/payload_envelope_verification/import.rs:106-118`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/import.rs#L106-L118) envelope: EL newPayload handle awaited, then availability is only a cache join (put_executed_payload_envelope)
- [`beacon_node/network/src/network_beacon_processor/mod.rs:982`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L982) getBlobs fetch spawned concurrently with block processing
- [`beacon_node/beacon_chain/src/block_verification.rs:699-706`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L699-L706) signature_verify_chain_segment runs verify_columns_against_block (KZG) serially for every block in the segment before signature verification and import
- [`beacon_node/beacon_chain/src/block_verification.rs:1409-1418`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1409-L1418) into_execution_pending_block_slashable runs verify_kzg_for_available_block serially before consensus/EL verification for RPC blocks with data

**Skeptic check.** The earlier evidence is right for the gossip and Gloas envelope paths, where prysm#16899 applies. It missed that the sync and RPC import paths still verify column KZG sequentially before consensus verification.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [prysm#16899](https://github.com/OffchainLabs/prysm/pull/16899), [prysm#12734](https://github.com/OffchainLabs/prysm/pull/12734)

</details>


<a id="data_availability-059"></a>
<details>
<summary><b>data_availability-059</b> Merge pre-import block cache into DA cache — <i>implemented · low · S · memory</i></summary>

**Idea.** Serve recent and pre-executed blocks to req/resp from the one bounded data availability cache instead of a separate, unbounded pre-import cache.

**Impact.** Already merged (PR 8045); no unbounded pre-import cache remains.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:379`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L379) get_cached_block returns PreExecution and Executed blocks
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:126`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L126) insert_pre_execution_block stored in the same PendingComponents
- [`beacon_node/beacon_chain/src/beacon_block_streamer.rs:173`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_block_streamer.rs#L173) req/resp reads via get_block_process_status (metric BEACON_REQRESP_PRE_IMPORT_CACHE_HITS)
- [`beacon_node/beacon_chain/src/pending_payload_cache/mod.rs:118`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/mod.rs#L118) Gloas block cache also bounded LRU

**Skeptic check.** Confirmed pre-execution blocks live in the bounded DA LRU and req/resp serves from it; no separate reqresp pre-import map exists. Earlier verdict correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#8045](https://github.com/sigp/lighthouse/pull/8045)

</details>


<a id="data_availability-060"></a>
<details>
<summary><b>data_availability-060</b> Skip duplicate blob arrival notifications — <i>implemented · low · S · cpu</i></summary>

**Idea.** Check whether a blob index is already present before notifying the blob waiter, so the same blob is not processed twice.

**Impact.** Duplicates are dropped on merge and sidecars for imported blocks are rejected before the DA checker; there is no waiter channel to double-notify.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:104`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L104) blob_exists
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:162`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L162) merge_single_blob skips existing index when no block
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:180`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L180) merge_data_columns skips cached column index
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3464`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3464) DuplicateFullyImported guards before re-processing sidecars of imported blocks

**Skeptic check.** With a block present a matching blob simply overwrites the same slot (harmless); duplicate gossip is filtered upstream by observed sidecars and fork-choice DuplicateFullyImported checks. Earlier verdict correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#13123](https://github.com/OffchainLabs/prysm/pull/13123)

</details>


<a id="data_availability-061"></a>
<details>
<summary><b>data_availability-061</b> Track received columns to skip duplicate work — <i>implemented · medium · S · cpu, disk, bandwidth</i></summary>

**Idea.** Track which data columns were received and stored per block, so a column from gossip and the same one recovered from EL is not processed, persisted or requested twice.

**Impact.** Columns are not verified, stored or requested a second time on the gossip, EL and RPC paths.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:176-186`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L176-L186) merge_data_columns skips cached indices
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:632-652`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L632-L652) EL columns deduped vs gossip-observed and DA-cached
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1163-1176`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1163-L1176) missing_cells_for_column_sidecar returns PriorKnownUnpublished before KZG
- [`beacon_node/network/src/sync/network_context.rs:978`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L978) RPC column requests exclude cached_data_column_indexes

**Skeptic check.** Confirmed dedup on all three ingress paths, and also on the sync request side. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#14467](https://github.com/OffchainLabs/prysm/pull/14467), [teku#9409](https://github.com/Consensys-Incorporated/teku/pull/9409), [silver#271](https://github.com/gattaca-com/silver/pull/271)

</details>


<a id="data_availability-062"></a>
<details>
<summary><b>data_availability-062</b> Retry pending block only when all columns arrive — <i>n/a · low · cpu</i></summary>

**Idea.** Retry a block waiting for columns only once every sampled column is accepted (after reconstruction finishes), not on each sidecar or at half, so the work queue is not flooded with redundant retries.

**Impact.** Lighthouse does not retry a pending block per sidecar; the DA cache imports when components are complete and reconstruction runs once, so no redundant retry flood exists.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:592`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L592) check_and_set_reconstruction_started guards with reconstruction_started and all-sampling-received
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1488`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1488) check_reconstruction_trigger

**Sources.** [grandine@5f32e526b](https://github.com/grandinetech/grandine/commit/5f32e526bf50), [grandine@8fcf5da96](https://github.com/grandinetech/grandine/commit/8fcf5da96fa7)

</details>


<a id="data_availability-063"></a>
<details>
<summary><b>data_availability-063</b> Delay RPC fetch of missing sidecars — <i>partial · medium · S · latency, bandwidth, sync</i></summary>

**Idea.** Delay RPC fetches of missing blobs/columns by a slot-time-based interval (about 0.5 to 1 s, capped by the attestation deadline), so gossip can deliver them first and redundant requests are avoided.

**Gap in Lighthouse.** There is no explicit slot-time-based delay. The delay comes only from the trigger: Lighthouse never fetches on block arrival, waits for attestations and 3 peers, and then requests only the columns it has not cached. The Gloas column BlockRootUnknown path (gossip_methods.rs:790) and unknown-parent lookups fetch at once, with no wait capped at the attestation deadline.

**Impact.** Small. Most of the redundant by-root requests are already avoided. An explicit delay would only help the Gloas column and unknown-parent triggers.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1972`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1972) gossip block with MissingComponents starts no RPC fetch
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:2874-2886`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L2874-L2886) the lookup is started only by attestations for a block not in fork choice (about 1/3 slot)
- [`beacon_node/network/src/sync/manager.rs:1036-1056`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L1036-L1056) handle_unknown_block_root waits for corroboration from several peers
- [`beacon_node/lighthouse_network/src/config.rs:25`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L25) DEFAULT_UNKNOWN_ROOT_MIN_PEERS = 3
- [`beacon_node/network/src/sync/network_context.rs:970-992`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L970-L992) custody_lookup_request leaves out columns already received on gossip (cached_data_column_indexes)
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:73`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L73) QUEUED_RECONSTRUCTION_DELAY 150ms gives gossip time before reconstruction

**Second check.** The earlier review missed that Lighthouse does not fetch at block arrival at all. Its lookup starts from attestations at about 4s and needs 3 corroborating peers, and it filters columns already received on gossip. This gives the 'let gossip deliver first' effect without a timer.

**Verdict history.** not (checked) → partial (refuted)

**Sources.** [teku#10094](https://github.com/Consensys-Incorporated/teku/pull/10094), [teku#7026](https://github.com/Consensys-Incorporated/teku/pull/7026)

</details>


<a id="data_availability-064"></a>
<details>
<summary><b>data_availability-064</b> Request missing blobs immediately on block seen — <i>not · low · S · latency</i></summary>

**Idea.** When a gossip block arrives, enqueue a peer request for missing blobs at once instead of waiting for the availability wait to expire.

**Gap in Lighthouse.** On MissingComponents for a gossip block, send a SyncMessage to start a lookup for the missing custody columns (via SingleBlockLookup DataRequest::Request) instead of waiting for gossip or an attestation naming the root. Lighthouse relies on EL getBlobs and gossip columns first, so a delayed trigger would be needed to avoid wasted requests.

**Impact.** Only helps when columns are late on gossip; saves some hundreds of ms on rare late-column blocks. Pull requests on every block would add bandwidth.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1972`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1972) MissingComponents only traces a log, no request
- [`beacon_node/network/src/sync/manager.rs:921`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L921) lookups start only from attestation/unknown-parent messages
- [`beacon_node/network/src/network_beacon_processor/mod.rs:998`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L998) fetch_engine_blobs_and_publish_full tries EL immediately

**Sources.** [lodestar#6499](https://github.com/ChainSafe/lodestar/pull/6499)

</details>


<a id="data_availability-065"></a>
<details>
<summary><b>data_availability-065</b> Pull late block when blobs arrive first — <i>partial · medium · S · latency</i></summary>

**Idea.** If blobs arrive on gossip but the block does not arrive by a cutoff, fetch the block and remaining blobs from peers instead of waiting.

**Gap in Lighthouse.** Gloas already does this: a column for an unknown block root starts a block lookup at once, with no cutoff. Fulu, the live fork, does not. A Fulu column carries a signed header, so with a known parent it verifies without the block, sits as MissingComponents, and the block is fetched only when attestations arrive. Add a cutoff timer after the first Fulu column for an unseen block that sends search_unknown_block for that root.

**Impact.** On Fulu, a block missed on gossip but whose columns arrive is recovered before the attestations come (about 4s), which improves head vote timing.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_column_verification.rs:1241-1246`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1241-L1246) a Gloas gossip column for an unknown block root returns BlockRootUnknown
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1386-1392`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1386-L1392) the same for partial columns ('Block not known, trigger lookup')
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:778-793`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L778-L793) BlockRootUnknown sends UnknownBlockHashFromAttestation to start a block lookup
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1173-1185`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1173-L1185) the partial column path does the same
- [`beacon_node/network/src/sync/manager.rs:921-925`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L921-L925),1036-1056 the lookup starts after peer corroboration
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1016-1023`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1016-L1023) a Fulu column with a known parent goes to the DA checker as MissingComponents and starts no block lookup

**Second check.** Found the Gloas and partial-column BlockRootUnknown path, which starts a lookup from a sidecar of an unknown block. The earlier review searched only UnknownParentSidecarHeader. Fulu remains uncovered, so the verdict is partial.

**Verdict history.** not (checked) → partial (refuted)

**Sources.** [lodestar#6534](https://github.com/ChainSafe/lodestar/pull/6534)

</details>


<a id="data_availability-066"></a>
<details>
<summary><b>data_availability-066</b> Fetch missing blobs immediately for past slots — <i>n/a · low · latency, sync</i></summary>

**Idea.** When tracked data belongs to a past slot, fetch missing blobs at once instead of waiting the gossip delay.

**Impact.** Lookups for past-slot roots have no availability wait, so nothing to remove.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/mod.rs:359`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L359) new_current_lookup creates the lookup and requests at once, no gossip-delay wait

**Sources.** [teku#7103](https://github.com/Consensys-Incorporated/teku/pull/7103)

</details>


<a id="data_availability-067"></a>
<details>
<summary><b>data_availability-067</b> Fetch missing columns within the slot — <i>partial · medium · M · latency</i></summary>

**Idea.** Run the missing-column fetcher every second and request missing custody columns by root after a grace of half the time to the attestation deadline, instead of waiting a minute.

**Gap in Lighthouse.** There is no periodic fetcher that scans the DA checker for blocks with missing custody columns. Recovery inside the slot depends on attestations that reference the block, from at least 3 peers. Add a 1s tick that scans pending components past a grace period and issues custody by-root requests, so recovery does not depend on attestation traffic.

**Impact.** Low to medium. The minute-long wait that Caplin fixed does not occur in Lighthouse when attestations flow. A tick would help only when few attestations reference the block, for example a late block or a small or isolated set of peers.

**Best measured result.** block stayed unavailable for over a minute before (pr:caplin#24830)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:2874-2886`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L2874-L2886) an attestation for a block that is pending in the DA checker (not in fork choice) starts a lookup within the slot
- [`beacon_node/network/src/sync/network_context.rs:956-992`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L956-L992) custody_lookup_request fetches only the custody columns that are not yet cached
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1023`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1023),1505-1518 reconstruction is queued (QUEUED_RECONSTRUCTION_DELAY 150ms) when columns are missing
- [`beacon_node/network/src/sync/manager.rs:805-842`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L805-L842) there is no periodic missing-column tick

**Second check.** The earlier review missed the following: when a block is stuck in the DA checker, gossip attestations for it fail with UnknownHeadBlock, and that already starts an in-slot lookup that fetches only the missing custody columns. This is event-driven, not periodic.

**Verdict history.** not (checked) → partial (refuted)

**Sources.** [caplin#24830](https://github.com/erigontech/erigon/pull/24830)

</details>


<a id="data_availability-068"></a>
<details>
<summary><b>data_availability-068</b> Disable blob tracking after retention passes — <i>n/a · low · cpu, memory</i></summary>

**Idea.** After the blob retention window has passed beyond the fork that removed blob sidecars, swap in no-op blob sidecar managers and pools to stop their upkeep.

**Impact.** Blob sidecars are not removed by any fork in Lighthouse's design; blob tracking is a few empty vectors per pending block, so a no-op swap saves almost nothing.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:285`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L285) PendingComponents allocates blob vec per block
- [`beacon_node/store/src/hot_cold_store.rs:3255`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3255) prune_blobs by DA boundary

**Sources.** [teku#10502](https://github.com/Consensys-Incorporated/teku/pull/10502)

</details>


<a id="data_availability-069"></a>
<details>
<summary><b>data_availability-069</b> Disk-backed blob quarantine — <i>n/a · medium · memory, disk</i></summary>

**Idea.** Persist quarantined blob sidecars in a database table keyed by block root and index, deleted at finalization, so the quarantine does not hold them all in memory.

**Impact.** Lighthouse deliberately removed disk overflow (sigp#5891) and bounds the in-memory LRU; a disk quarantine would go against that design.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:349`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L349) critical is an in-memory LruCache, no disk table

**Sources.** [nimbus#7108](https://github.com/status-im/nimbus-eth2/pull/7108)

</details>


<a id="data_availability-070"></a>
<details>
<summary><b>data_availability-070</b> Memory-only bounded LRU for pending components — <i>implemented · medium · S · memory, disk</i></summary>

**Idea.** Remove the disk overflow of the pending availability cache and keep only a bounded in-memory LRU, removing the disk I/O.

**Impact.** There is no disk I/O for pending components.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:349-376`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L349-L376) DataAvailabilityCheckerInner holds only RwLock&lt;LruCache&gt;, no store
- [`beacon_node/beacon_chain/src/pending_payload_cache/mod.rs:103-118`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/mod.rs#L103-L118) Gloas pending cache also memory-only LruCache

**Skeptic check.** The only store references in the file are in tests. The Gloas pending payload cache is also memory-only. This is LH's own PR #5891.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#5891](https://github.com/sigp/lighthouse/pull/5891)

</details>


<a id="data_availability-071"></a>
<details>
<summary><b>data_availability-071</b> Remove duplicate column sidecar stores — <i>n/a · low · memory</i></summary>

**Idea.** Do not keep a second copy of received data column sidecars (for example in the sync layer) when fork choice or the DA cache already holds them.

**Impact.** No second long-lived column store found in sync; fork choice does not hold columns. Not exhaustively traced.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context/requests.rs:14`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/requests.rs#L14) lookup/range request state only holds columns until processed
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:68`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L68) single DA cache is the store for pending columns

**Sources.** [grandine#266](https://github.com/grandinetech/grandine/pull/266), [grandine@62800ae30](https://github.com/grandinetech/grandine/commit/62800ae301f5)

</details>


<a id="data_availability-072"></a>
<details>
<summary><b>data_availability-072</b> Drop sidecars with out-of-range index — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Track only blob sidecars whose index matches a commitment in the block, so the per-block tracker cannot grow without bound.

**Impact.** Per-block tracker is a fixed-length vector; it cannot grow.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:139`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L139) insert_blob_at_index uses get_mut, out-of-range ignored
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:285`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L285) verified_blobs sized max_blobs_per_block
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:162`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L162) merge_single_blob requires commitment match once block is known
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:180`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L180) columns deduped by index

**Skeptic check.** Verified fixed-size RuntimeFixedVector and commitment matching on merge_block; blobs past commitments count but under max_blobs are kept only until the block arrives, still bounded. Earlier verdict correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#7616](https://github.com/Consensys-Incorporated/teku/pull/7616)

</details>


<a id="data_availability-073"></a>
<details>
<summary><b>data_availability-073</b> Remove repeated checks from isDataAvailable — <i>partial · low · S · cpu</i></summary>

**Idea.** Do not repeat blob/commitment consistency checks in the availability check when they were already done earlier.

**Gap in Lighthouse.** AvailableBlock::new repeats the commitment equality check that merge_single_blob/merge_block already did; could be skipped on the DA-cache path.

**Impact.** Micro: a few 48-byte compares per block; negligible.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker.rs:880`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L880) AvailableBlock::new rechecks every blob commitment against the block
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:162`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L162) merge_single_blob already checks commitment match

**Sources.** [teku#7575](https://github.com/Consensys-Incorporated/teku/pull/7575)

</details>


<a id="data_availability-074"></a>
<details>
<summary><b>data_availability-074</b> Drop stale validator custody registrations — <i>implemented · low · S · memory</i></summary>

**Idea.** Remove validator custody registrations from memory when the validator stops registering, since the custody group count never decreases anyway.

**Impact.** Done (PR 7594).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/custody_context.rs:104`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L104) validators.retain drops entries older than VALIDATOR_REGISTRATION_EXPIRY_SLOTS

**Skeptic check.** register_validators prunes stale registrations on every call while the CGC map only grows; matches the idea exactly.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#7594](https://github.com/sigp/lighthouse/pull/7594)

</details>


<a id="data_availability-075"></a>
<details>
<summary><b>data_availability-075</b> Evict DA entries exactly when import completes — <i>partial · low · S · cpu, memory, disk, latency, bandwidth, sync</i></summary>

**Idea.** Keep a block's pending components and sampling tracker in the availability cache until fork choice import completes, then remove them at once (otherwise LRU/finality), holding the write lock only for the insert. This prevents re-downloads and keeps the cache from growing.

**Gap in Lighthouse.** Lighthouse keeps entries (deliberately, to avoid a re-insert race) until LRU/finality, so re-downloads are prevented and the write lock is short, but entries are not freed at import completion. Could remove in the import-complete path via a remove on overflow_lru_cache after fork choice import, if the race is handled.

**Impact.** Only memory: a few tens of MB of columns held until finality; no CPU saving.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:540`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L540) comment: components are never removed manually, only LRU
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:720`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L720) do_maintenance removes entries older than cutoff epoch
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:557`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L557) write lock held only for the insert, then downgraded

**Sources.** [lighthouse#5845](https://github.com/sigp/lighthouse/pull/5845), [lighthouse#7961](https://github.com/sigp/lighthouse/pull/7961), [teku#10219](https://github.com/Consensys-Incorporated/teku/pull/10219), [lighthouse#4132](https://github.com/sigp/lighthouse/pull/4132), [nimbus#8501](https://github.com/status-im/nimbus-eth2/pull/8501)

</details>


<a id="data_availability-076"></a>
<details>
<summary><b>data_availability-076</b> Wait on store events instead of polling — <i>n/a · low · cpu, latency</i></summary>

**Idea.** When serving a column-by-root request for a column not yet stored, wait on a database write event instead of polling the store at an interval.

**Impact.** Lighthouse neither polls nor waits for unstored columns; it just serves what it has.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:816`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L816) by-root handler answers synchronously from caches/store, no waiting or polling

**Sources.** [prysm#14062](https://github.com/OffchainLabs/prysm/pull/14062)

</details>


<a id="data_availability-077"></a>
<details>
<summary><b>data_availability-077</b> Free column recovery state promptly — <i>n/a · medium · cpu, memory</i></summary>

**Idea.** Remove column recovery tasks from the tracking map at completion (with a timed sweep), keep references only to sidecars still pending reconstruction and store only slot and root per entry, instead of holding all retrieved sidecars for minutes.

**Impact.** Lighthouse has no per-block recovery task map retaining retrieved sidecars; reconstruction state is a flag inside the bounded pending-components LRU, freed on import or maintenance.

**Best measured result.** Heap graphs before/after shown (no numbers) (pr:teku#9648)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:592`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L592) check_and_set_reconstruction_started is a flag on LRU entry
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:720`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L720) do_maintenance

**Sources.** [teku#9890](https://github.com/Consensys-Incorporated/teku/pull/9890), [teku#9874](https://github.com/Consensys-Incorporated/teku/pull/9874), [teku#9648](https://github.com/Consensys-Incorporated/teku/pull/9648)

</details>


<a id="data_availability-078"></a>
<details>
<summary><b>data_availability-078</b> Import only when blob count equals commitments — <i>implemented · low · S · latency</i></summary>

**Idea.** Treat a block as complete only when the number of held blob sidecars exactly equals its KZG commitment count, so import is not triggered early and rejected.

**Impact.** None. Import does not start before all the data is present.

**Best measured result.** mitigates some stuttering in block updates when blobs arrived after blocks (pr:nimbus#5363)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:209-235`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L209-L235) make_available: Equal -&gt; available, Less -&gt; wait, Greater -&gt; error
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:404-407`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L404-L407) only sampling columns enter the cache, so count equality implies the full sampling set

**Skeptic check.** The Fulu analogue compares the column count with the expected sampling count. Because non-sampling columns are filtered out before insertion, an exact count means the set is complete. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#5363](https://github.com/status-im/nimbus-eth2/pull/5363)

</details>


<a id="data_availability-079"></a>
<details>
<summary><b>data_availability-079</b> Drop gossip columns outside sampling set — <i>implemented · low · S · cpu, disk, bandwidth</i></summary>

**Idea.** Drop incoming data column sidecars for columns that are not in the node's sampling set before KZG verification and storage.

**Impact.** Off-set columns do not arrive in normal operation because only sampling subnets are subscribed. KZG work is wasted only briefly after a CGC increase, between the subnet subscription and the epoch where sampling_columns_for_epoch includes the new columns.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/service.rs:786-792`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L786-L792) subscribe_new_data_column_subnets(sampling_count) subscribes only to sampling subnets
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:404-407`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L404-L407) put_gossip_verified_data_columns filters by sampling_columns_for_epoch
- [`beacon_node/beacon_chain/src/custody_context.rs:507`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L507) sampling_columns_for_epoch

**Skeptic check.** The earlier evidence cited lighthouse_network/service/utils.rs:302, which is the whitelist of all possible topics, not the subscription. The real subscription limit is in network/service.rs. The effect is equivalent to the Grandine check, which targeted the supernode-to-fullnode case.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine#376](https://github.com/grandinetech/grandine/pull/376), [grandine@b970e9d91](https://github.com/grandinetech/grandine/commit/b970e9d91cbe)

</details>


<a id="data_availability-080"></a>
<details>
<summary><b>data_availability-080</b> Correct proposer cache key in blob verification — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Look up the proposer for blob sidecar verification with the correct shuffling decision root, so the proposer cache hits mid-epoch instead of recomputing the shuffling.

**Impact.** Proposer cache hits for gossip column header checks mid-epoch, both pre- and post-Fulu lookahead.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_column_verification.rs:1743-1746`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1743-L1746)
- [`beacon_node/beacon_chain/src/block_verification.rs:1026-1029`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1026-L1029)
- [`consensus/proto_array/src/proto_array_fork_choice.rs:380-410`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L380-L410)
- [`beacon_node/beacon_chain/src/payload_envelope_verification/gossip_verified_envelope.rs:220-229`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/gossip_verified_envelope.rs#L220-L229)

**Skeptic check.** verify_proposer_and_signature keys with_proposer_cache by parent_block.proposer_shuffling_root_for_child_block, the same fork-aware decision root as block gossip; gossip BlobSidecar verification no longer exists, so no blob path remains. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#4646](https://github.com/sigp/lighthouse/pull/4646)

</details>


<a id="data_availability-081"></a>
<details>
<summary><b>data_availability-081</b> Consistent sidecar quarantine accounting — <i>implemented · low · S · cpu, memory, disk</i></summary>

**Idea.** Keep the quarantine's root set, counts and eviction order consistent (for example on a linked list with a root table), so entries do not leak and prune loops do not spin.

**Impact.** Single LRU structure owns roots, order and contents; no parallel count/root tables to desync.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:351`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L351) PendingComponents in one bounded LruCache keyed by block root
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:573`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L573) components removed only by LRU eviction
- [`beacon_node/beacon_chain/src/pending_payload_cache/mod.rs:103`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/mod.rs#L103) Gloas cache same design

**Skeptic check.** The Nimbus bug class (separate root table, counters and list drifting) cannot occur with a single hashlink LruCache. Earlier verdict correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#7634](https://github.com/status-im/nimbus-eth2/pull/7634), [nimbus#7743](https://github.com/status-im/nimbus-eth2/pull/7743)

</details>


<a id="data_availability-082"></a>
<details>
<summary><b>data_availability-082</b> High priority retry for delayed columns — <i>implemented · low · S · latency</i></summary>

**Idea.** Retry delayed data column sidecars at high priority in the processing queue, since a block is waiting on them.

**Impact.** Delayed columns re-enter at block/column priority, ahead of attestations and API work.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:946`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L946) unknown_block_data_column_queue popped right after gossip_data_column_queue, before API p0 and attestations
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:803`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L803) UnknownBlockDataColumn reprocess message

**Skeptic check.** Read the scheduler order: the retry queue sits directly after gossip columns in the block-tier section. Earlier verdict correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine@6997dfcff](https://github.com/grandinetech/grandine/commit/6997dfcff8be)

</details>


<a id="data_availability-083"></a>
<details>
<summary><b>data_availability-083</b> Keep column recovery queue in memory — <i>implemented · low · S · memory, disk, sync</i></summary>

**Idea.** Keep the column sidecar recovery queue in memory instead of persisting it in the database, and start blob/column downloads only when the node is synced.

**Impact.** Recovery/reconstruction state is never persisted to the DB; nothing to move.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:953`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L953) column_reconstruction_queue is an in-memory work queue
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:351`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L351) pending columns held in memory only

**Skeptic check.** Lighthouse never had a DB-persisted recovery queue; the Caplin fix addresses an architecture LH lacks, and column downloads are driven by sync/lookups rather than a pre-sync background downloader.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#16428](https://github.com/erigontech/erigon/pull/16428)

</details>


<a id="data_availability-084"></a>
<details>
<summary><b>data_availability-084</b> Serve blob by-root fetches from quarantine directly — <i>implemented · low · S · bandwidth, sync</i></summary>

**Idea.** Remove the async queue for blob by-root requests and compute the missing blobs directly from the quarantine, deduplicating and dropping stale requests.

**Impact.** Blob by-root is answered directly from the DA cache with per-root store reads deduplicated; no extra async stage to remove.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:655`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L655) handle_blobs_by_root_request runs inline in the RPC worker
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:725`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L725) data_availability_checker.get_blob(id) served from the DA cache first
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:734`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L734) blob_list_results Entry map loads each root once from store/early attester cache
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:717`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L717) post-Fulu roots skipped

**Skeptic check.** Read handle_blobs_by_root_request_inner: it serves from the DA cache, then a per-root deduplicated store/early-attester lookup, with no secondary queue. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#5198](https://github.com/status-im/nimbus-eth2/pull/5198)

</details>


<a id="data_availability-085"></a>
<details>
<summary><b>data_availability-085</b> Skip KZG and proof checks for EL-built columns — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** When blobs or columns of a block are built from the local EL getBlobs response, skip gossip KZG cell proof and inclusion proof verification (the EL already verified them), keeping only structural checks or one KZG check before persistence.

**Impact.** EL-built columns skip KZG cell-proof and inclusion-proof verification.

**Best measured result.** 6 blobs 65.3 -&gt; 16.8 ms, 21 blobs 218 -&gt; 58 ms (benchmark); ~28 ms per blob saved (pr:caplin#25510)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:685-705`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L685-L705)
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:627`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L627)
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:317-400`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L317-L400)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3621-3646`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3621-L3646)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4222-4247`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4222-L4247)

**Skeptic check.** V2/V3 and V4 getBlobs paths wrap computed/returned cells with KzgVerifiedPartialDataColumn::from_execution_verified and import via process_engine_blobs_fulu / pending payload cache, which only check header signature/slashability, not KZG. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#6913](https://github.com/status-im/nimbus-eth2/pull/6913), [caplin#25510](https://github.com/erigontech/erigon/pull/25510)

</details>


<a id="data_availability-086"></a>
<details>
<summary><b>data_availability-086</b> Cache column inclusion proof results — <i>not · low · S · cpu</i></summary>

**Idea.** Cache the result of the KZG commitments inclusion proof check per block (key: hash of proof inputs) so other column sidecars of the same block skip the merkle proof.

**Gap in Lighthouse.** Add a small LRU keyed by hash of (commitments root inputs, proof, body_root) consulted in verify_column_inclusion_proof and the RPC verifiers; or hash commitments once per block_root.

**Impact.** Saves a tree hash of the commitment list plus a ~4-deep merkle branch for each of up to 128 columns per block; tens of microseconds each, small total.

**Best measured result.** 'reduce redundant work' when verifying inclusion proofs; no numbers (pr:prysm#15217)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_column_verification.rs:1667`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1667) verify_column_inclusion_proof calls verify_inclusion_proof on every column
- [`consensus/types/src/data/data_column_sidecar.rs:285`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/data/data_column_sidecar.rs#L285) verify_inclusion_proof recomputes kzg_commitments.tree_hash_root and merkle branch each call
- [`beacon_node/network/src/sync/network_context/requests/data_columns_by_root.rs:63`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/requests/data_columns_by_root.rs#L63) and data_columns_by_range.rs:36 also verify per column, no cache

**Sources.** [prysm#15217](https://github.com/OffchainLabs/prysm/pull/15217)

</details>


<a id="data_availability-087"></a>
<details>
<summary><b>data_availability-087</b> Late DA check with per-block sampling tracker — <i>implemented · medium · M · disk, latency, bandwidth</i></summary>

**Idea.** Track sampled columns per block in memory as they arrive by gossip, EL or RPC, fetch only the missing ones by RPC, and run the availability check as late as possible to give gossip and EL more time.

**Impact.** Gossip block with missing columns waits for gossip/EL/reconstruction; RPC custody lookups fetch only uncached columns.

**Best measured result.** fewer RPC calls (no numbers) (pr:teku#10006)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:592`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L592)
- [`beacon_node/network/src/sync/network_context.rs:956-999`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L956-L999)
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1972-1978`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1972-L1978)
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:722-731`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L722-L731)

**Skeptic check.** PendingComponents tracks columns per block from every source and availability is re-evaluated on each arrival while block execution proceeds; gossip MissingComponents does not trigger RPC, and custody_lookup_request filters cached_data_column_indexes. Cached indexes are read once at request time, a minor difference from Teku's live tracker.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#10006](https://github.com/Consensys-Incorporated/teku/pull/10006)

</details>


<a id="data_availability-088"></a>
<details>
<summary><b>data_availability-088</b> Re-call getBlobs until block columns are complete — <i>not · medium · S · latency, bandwidth</i></summary>

**Idea.** Call engine_getBlobs again with short timeouts, triggered per gossip block, per arriving column and periodically, until all needed columns of the block can be built from EL blobs, instead of waiting for gossip.

**Gap in Lighthouse.** getBlobs fires at most once per trigger (gossip block, first partial header, RPC block); no re-call on later column/partial arrival and no periodic retry until custody columns are complete. Add a bounded retry loop (short timeouts, per-slot deadline) around fetch_engine_blobs_and_publish_full; V3/V4 partial merging already handles incremental results.

**Impact.** Higher EL hit rate when blobs reach the EL mempool after the block; fewer columns from gossip/RPC, earlier availability on late blobs (est. a few hundred ms in those cases).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1936`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1936) spawn_fetch_block_columns once per gossip block
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1120`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1120) getBlobs once on first (uncached) partial header only
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:217`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L217) once after RPC block
- [`beacon_node/network/src/network_beacon_processor/mod.rs:998`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L998) fetch_engine_blobs_and_publish_full: single call, MissingComponents/Ok(None) only logged
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:161`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L161) one V4 or V2/V3 attempt, no loop or timer

**Second check.** Also checked the partial-column path (publish_partial_data_columns, partial-header trigger) and the fetch_blobs V4 path for any retry/interval; the partial header trigger is a second one-shot call, not a retry.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [nimbus#8012](https://github.com/status-im/nimbus-eth2/pull/8012), [nimbus#7445](https://github.com/status-im/nimbus-eth2/pull/7445), [prysm#15520](https://github.com/OffchainLabs/prysm/pull/15520)

</details>


<a id="data_availability-089"></a>
<details>
<summary><b>data_availability-089</b> Dedicated executor queue for DA tasks — <i>n/a · low · S · latency</i></summary>

**Idea.** Give data availability tasks their own async executor queue so they do not exhaust the shared operation pool and get rejected.

**Impact.** Teku shared-executor exhaustion; Lighthouse's beacon processor already has separate per-type queues for DA work.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:375`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L375) each Work type has its own bounded queue and worker pool slot

**Sources.** [teku#9657](https://github.com/Consensys-Incorporated/teku/pull/9657)

</details>


<a id="data_availability-090"></a>
<details>
<summary><b>data_availability-090</b> Allow column reconstruction while not synced — <i>not · medium · M · sync, bandwidth</i></summary>

**Idea.** Permit data column reconstruction from 50% of columns during range sync and backfill (on by default), not only at head, so sync does not have to download the remaining columns from peers.

**Gap in Lighthouse.** Range sync and backfill request every sampling column from peers and never reconstruct. Request only 50% of columns for supernode/high-custody nodes during sync and reconstruct the rest locally (reconstruct_data_columns / KzgVerifiedCustodyDataColumn::reconstruct_columns) before import; backfill would need the same in historical_blocks import.

**Impact.** Supernodes and high-custody nodes could download about half the column data during range sync and backfill, at the cost of KZG recovery CPU.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1488`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1488) check_reconstruction_trigger only called from gossip paths (1024, 1465)
- [`beacon_node/network/src/network_beacon_processor/mod.rs:1213`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L1213) attempt_data_column_reconstruction only reached from gossip
- [`beacon_node/network/src/sync/network_context.rs:987`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L987) sync requests all sampling columns from peers
- [`beacon_node/beacon_chain/src/historical_blocks.rs:482`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_blocks.rs#L482) only state reconstruction in backfill, no column reconstruction
- [`beacon_node/beacon_chain/src/custody_context.rs:492`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L492) should_attempt_reconstruction does not depend on sync state but is never consulted by sync

**Second check.** Searched sync/ (range, backfill, block_sidecar_coupling, network_context) and historical_blocks.rs for any column reconstruction; the only 'reconstruct' there is historic state reconstruction.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [grandine@062840454](https://github.com/grandinetech/grandine/commit/062840454cce), [grandine#334](https://github.com/grandinetech/grandine/pull/334), [grandine#361](https://github.com/grandinetech/grandine/pull/361), [grandine@ef26a3a88](https://github.com/grandinetech/grandine/commit/ef26a3a8818e)

</details>


<a id="data_availability-091"></a>
<details>
<summary><b>data_availability-091</b> Lock striping in column store — <i>not · low · M · cpu, latency</i></summary>

**Idea.** Shard the data column store lock by block root or column index so concurrent reads, writes and recovery do not contend on one global lock.

**Gap in Lighthouse.** Shard the critical RwLock in DataAvailabilityCheckerInner by block root (e.g. N shards of LruCache) in overflow_lru_cache.rs. Reads already use shared read locks, so gain is small.

**Impact.** Would cut write-lock contention between gossip column insertion and reads/reconstruction; unlikely to be measurable on a mainnet node.

**Evidence (Lighthouse @ 928b61e719).**

- overflow_lru_cache.rs:351 single RwLock&lt;LruCache&gt; for all roots
- overflow_lru_cache.rs:412 column reads take the read lock without touching LRU

**Sources.** [caplin#17121](https://github.com/erigontech/erigon/pull/17121)

</details>


<a id="data_availability-092"></a>
<details>
<summary><b>data_availability-092</b> Compute sidecar inclusion proofs from shared merkle subtrees — <i>partial · low · S · cpu, memory</i></summary>

**Idea.** When building blob or column sidecars for a block, compute the block body merkle subtree and the KZG commitments branch once and derive every sidecar's inclusion proof from it, instead of rebuilding the tree per sidecar; cache the proposer signature result for the block too.

**Gap in Lighthouse.** reconstruct_blob_sidecars passes the &amp;SignedBlindedBeaconBlock into BlobSidecar::new_with_existing_proof for every blob; its TryInto&lt;PartialDataColumnHeader&gt; clones the commitments, recomputes signed_block_header() (full body tree hash) and kzg_commitments_merkle_proof() per blob. Convert to PartialDataColumnHeader once before the map. Hit by the blob_sidecars HTTP API for Fulu blocks.

**Impact.** Saves ~2 body tree hashes per blob on blob_sidecars API calls for PeerDAS blocks; small next to cell recovery cost. Column building on block production / getBlobs already computes the proof once.

**Best measured result.** 2.12x faster / 53% less memory at 3 blobs; 5.16x faster / 77% less at 9 blobs (pr:prysm#15473)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/kzg_utils.rs:318-326`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L318-L326)
- [`consensus/types/src/block/beacon_block_body.rs:406-421`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/block/beacon_block_body.rs#L406-L421)
- [`beacon_node/beacon_chain/src/kzg_utils.rs:850-880`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L850-L880)
- [`consensus/types/src/data/blob_sidecar.rs:141-155`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/data/blob_sidecar.rs#L141-L155)
- [`consensus/types/src/data/partial_data_column_sidecar.rs:321-329`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/data/partial_data_column_sidecar.rs#L321-L329)
- [`beacon_node/http_api/src/block_id.rs:371-377`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L371-L377)

**Skeptic check.** Column sidecar building (build_data_column_sidecars_fulu, fetch_blobs header) computes the commitments inclusion proof once per block and clones it, so the hot path is done. The API blob-reconstruction path still rebuilds the body tree per blob; the earlier note pointed at BlobSidecar::new, which is test-only now.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lighthouse#4968](https://github.com/sigp/lighthouse/pull/4968), [prysm#15473](https://github.com/OffchainLabs/prysm/pull/15473)

</details>


<a id="data_availability-093"></a>
<details>
<summary><b>data_availability-093</b> Validate column sidecars at mid processor priority — <i>implemented · medium · S · latency</i></summary>

**Idea.** Schedule gossip data column sidecar validation in the beacon processor at a priority below blocks, so a burst of sidecars does not delay block processing.

**Impact.** Gossip column bursts are queued behind gossip blocks and RPC blocks.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:928-938`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L928-L938)
- [`beacon_node/beacon_processor/src/lib.rs:944-955`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L944-L955)
- [`beacon_node/beacon_processor/src/lib.rs:1311-1312`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1311-L1312)

**Skeptic check.** Gossip columns are always pushed to gossip_data_column_queue and popped only after gossip_block_queue and execution payload queues are empty, but before attestations. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine@212000f60](https://github.com/grandinetech/grandine/commit/212000f60657)

</details>


<a id="data_availability-094"></a>
<details>
<summary><b>data_availability-094</b> Fetch column subsets from many peers in parallel — <i>implemented · medium · M · sync, bandwidth</i></summary>

**Idea.** During sync or lookup, split a column request across several custody peers in parallel instead of requesting all columns from one supernode, spreading load and removing single-peer dependence.

**Impact.** Column requests in range sync and lookups go to per-column custody peers, grouped into per-peer requests.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context.rs:577-630`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L577-L630)
- [`beacon_node/network/src/sync/network_context/custody.rs:232-320`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L232-L320)
- [`beacon_node/network/src/sync/network_context/custody.rs:353-391`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L353-L391)

**Skeptic check.** Range sync picks a random least-loaded custody peer per column; lookups pick per column with a per-request hash order (deliberately consolidates onto fewer peers, but falls back across custodians with attempt limits). No single-supernode requirement. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#14977](https://github.com/OffchainLabs/prysm/pull/14977)

</details>


<a id="data_availability-095"></a>
<details>
<summary><b>data_availability-095</b> Give reconstruction a multi-thread worker allocation — <i>partial · medium · S · cpu, latency</i></summary>

**Idea.** Let reconstruction claim several beacon processor worker slots and run on a scoped rayon pool of that size, so parallel KZG recovery does not oversubscribe cores shared with other tasks.

**Gap in Lighthouse.** Reconstruction runs on the shared HighPriority scoped rayon pool (80% of CPUs) but BeaconProcessor still counts it as one worker slot; no multi-permit allocation exists (PRs #7720/#7789 were closed unmerged). Need ColumnReconstruction to take N worker permits and install a rayon scope of size N.

**Impact.** Avoids core oversubscription on supernodes during reconstruction; small tail-latency gain for concurrent work.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:3811`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3811)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3845`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3845)
- [`common/task_executor/src/rayon_pool_provider.rs:4-47`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/task_executor/src/rayon_pool_provider.rs#L4-L47)
- [`beacon_node/beacon_processor/src/lib.rs:953`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L953)
- [`beacon_node/beacon_processor/src/lib.rs:1703`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1703)
- [`crypto/kzg/src/lib.rs:307-314`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/kzg/src/lib.rs#L307-L314)

**Second check.** Searched beacon_processor for any multi-worker/permit logic (spawn_multi, worker counts) and the KZG/rust_eth_kzg 0.9.1 context for its own thread caps; none found, and the source PRs were closed unmerged.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [lighthouse#7720](https://github.com/sigp/lighthouse/pull/7720), [lighthouse#7789](https://github.com/sigp/lighthouse/pull/7789)

</details>


<a id="data_availability-096"></a>
<details>
<summary><b>data_availability-096</b> Reconstruct only when needed columns are missing — <i>partial · medium · S · cpu</i></summary>

**Idea.** Trigger reconstruction (and EL getBlobs) only when one of the node's own sampling or custody columns is still missing, not when any column is missing or all columns are already held; run it at lower thread priority.

**Gap in Lighthouse.** Trigger conditions are done (also for the Gloas pending_payload_cache path). Execution is on the HighPriority rayon pool, and the reconstruction queue is polled ahead of API p0 and attestations; no low-priority pool or OS thread niceness. Switching to RayonPoolType::LowPriority would complete it.

**Impact.** Marginally less interference with block import on supernodes; only supernodes reconstruct.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/custody_context.rs:492`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L492)
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:617`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L617)
- [`beacon_node/beacon_chain/src/pending_payload_cache/mod.rs:909-920`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/mod.rs#L909-L920)
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1488-1505`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1488-L1505)
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:645-650`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L645-L650)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3811`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3811)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3845`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3845)
- [`beacon_node/beacon_processor/src/lib.rs:953`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L953)

**Second check.** Checked the Gloas reconstruction path and the beacon processor queue order: the HighPriority pool is below the global pool, but nothing runs reconstruction at lowered priority.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [grandine@76504f279](https://github.com/grandinetech/grandine/commit/76504f279498), [grandine#521](https://github.com/grandinetech/grandine/pull/521), [lighthouse#5806](https://github.com/sigp/lighthouse/pull/5806), [lodestar#8536](https://github.com/ChainSafe/lodestar/pull/8536)

</details>


<a id="data_availability-097"></a>
<details>
<summary><b>data_availability-097</b> No reconstruction when serving column RPC — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** When serving data columns by range or by root, return only stored columns and do not run reconstruction for missing ones; the requester fetches them elsewhere.

**Impact.** Serving column RPC never triggers reconstruction.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:816-840`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L816-L840)
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1857`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1857)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1229-1254`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1229-L1254)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1362-1371`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1362-L1371)

**Skeptic check.** By-root serving reads DA/pending/early-attester caches then the store; by-range reads store via get_data_column; neither calls reconstruction. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#8051](https://github.com/sigp/lighthouse/pull/8051)

</details>


<a id="data_availability-098"></a>
<details>
<summary><b>data_availability-098</b> Non-blocking state access in sidecar handling — <i>partial · low · M · latency</i></summary>

**Idea.** Use non-blocking or snapshot reads of fork-choice state when handling received column sidecars, so gossip handling does not wait on the fork-choice write lock.

**Gap in Lighthouse.** Read lock still waits while fork choice holds the write lock (on_block, head update). Could copy a ProtoBlock snapshot or use a lock-free cached proto-array view in verify_parent_block_and_finalized_descendant.

**Impact.** Gossip column verification would not stall behind fork-choice writes; the write hold is short, so gain is small.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_column_verification.rs:1712`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1712) uses fork_choice_read_lock, not the write lock
- data_column_verification.rs:1716 only get_block and finalized-descendant check under the lock

**Sources.** [grandine#552](https://github.com/grandinetech/grandine/pull/552)

</details>


<a id="data_availability-099"></a>
<details>
<summary><b>data_availability-099</b> Run gossip column KZG verification on blocking pool — <i>implemented · medium · S · latency, cpu</i></summary>

**Idea.** Run gossip data column KZG and signature verification on a blocking or rayon pool instead of inline on async runtime threads, so verification does not stall the async executor.

**Impact.** Async executor not stalled by gossip column verification.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2451-2477`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2451-L2477)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2514-2545`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2514-L2545)
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1306-1320`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1306-L1320)

**Skeptic check.** Full gossip columns and partial columns (including the partial header signature check, called from inside the closure) are verified inside spawn_blocking_handle. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#9271](https://github.com/sigp/lighthouse/pull/9271)

</details>


<a id="data_availability-100"></a>
<details>
<summary><b>data_availability-100</b> Operator flags to skip EL or blob handling — <i>not · low · M · disk, bandwidth</i></summary>

**Idea.** Offer operator flags to run without an EL or to skip blob gossip, RPC and availability checks for nodes that do not need them, saving storage and bandwidth.

**Gap in Lighthouse.** Would need a flag that disables column gossip subscriptions and DA checks in the network service and data_availability_checker; unsafe for validators, so only for non-validating nodes.

**Impact.** Saves large storage and bandwidth only for non-validating nodes that opt in; no effect on normal nodes.

**Best measured result.** 1.4TB storage reduction; 70% bandwidth reduction and 300Gb storage (pr:prysm#13841)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/src/cli.rs:944`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L944) only disable-get-blobs exists
- [`beacon_node/src/cli.rs:1046`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L1046) prune-blobs and cli.rs:1056 epochs-per-blob-prune only tune pruning
- [`beacon_node/src/cli.rs:845`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L845) execution-endpoint is required for a normal node; no flag to run without EL or skip DA/blob gossip

**Sources.** [prysm#13841](https://github.com/OffchainLabs/prysm/pull/13841)

</details>


<a id="data_availability-101"></a>
<details>
<summary><b>data_availability-101</b> Mark columns available before disk write completes — <i>n/a · low · S · latency</i></summary>

**Idea.** Update the availability cache and emit the availability event as soon as columns are queued for persistence, not after the filesystem write, and evict the entries if the write fails.

**Gap in Lighthouse.** Columns are persisted during block import, and the availability cache is memory-only, so availability is not gated on a separate column disk write.

**Impact.** None.

**Best measured result.** Shows DA waiting time before/after charts (images, no numbers) (pr:prysm#16137)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:483`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L483) put_kzg_verified_data_columns is in-memory only
- [`beacon_node/store/src/hot_cold_store.rs:1315`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1315) PutDataColumns written during block import

**Sources.** [prysm#16137](https://github.com/OffchainLabs/prysm/pull/16137)

</details>


<a id="data_availability-102"></a>
<details>
<summary><b>data_availability-102</b> Option to disable blob pruning — <i>implemented · low · S · disk</i></summary>

**Idea.** Offer a configuration switch to keep blobs instead of pruning them, and drop unused archival components.

**Impact.** Archival operators can already keep blobs; no performance impact on normal nodes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/config.rs:61`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L61) prune_blobs field, default true at :120
- [`beacon_node/src/config.rs:468`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/config.rs#L468) --prune-blobs wired to store config
- [`beacon_node/src/config.rs:860`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/config.rs#L860) complete-blob-backfill forces prune_blobs=false
- [`beacon_node/store/src/hot_cold_store.rs:3287`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3287) try_prune_blobs returns early when pruning disabled

**Skeptic check.** Confirmed the --prune-blobs switch reaches try_prune_blobs and skips pruning. The Caplin-specific part (dropping unused archival components) has no Lighthouse counterpart. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#9655](https://github.com/erigontech/erigon/pull/9655)

</details>


<a id="data_availability-103"></a>
<details>
<summary><b>data_availability-103</b> Overflow pending DA cache to disk — <i>not · medium · L · memory</i></summary>

**Idea.** Bound the in-memory size of the pending blocks and blobs cache with an LRU that spills evicted entries to disk, so waiting data cannot exhaust memory.

**Gap in Lighthouse.** Pending components live in a bounded in-memory LruCache and evicted entries are dropped; the DBColumn::OverflowLRUCache column is marked DEPRECATED, so the disk spill from PR #4203 was removed. Would need an eviction hook writing PendingComponents to the hot DB and a read-back on miss.

**Impact.** Only matters under long non-finality or blob spam; no gain in normal operation, and Lighthouse removed it on purpose.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:351`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L351)
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:372`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L372)
- [`beacon_node/beacon_chain/src/pending_payload_cache/mod.rs:118`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/mod.rs#L118)
- [`beacon_node/store/src/lib.rs:409`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/lib.rs#L409)

**Second check.** Also checked the Gloas pending_payload_cache (in-memory LRU only) and the store columns: the overflow column survives only as a deprecated id.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [lighthouse#4203](https://github.com/sigp/lighthouse/pull/4203), [lighthouse#4152](https://github.com/sigp/lighthouse/pull/4152)

</details>


<a id="data_availability-104"></a>
<details>
<summary><b>data_availability-104</b> Parallel DA cache warmup at startup — <i>n/a · low · S · startup</i></summary>

**Idea.** At startup, read and process the sidecar files of an epoch in parallel when warming the data column availability cache, instead of sequentially.

**Impact.** Nothing to speed up: Lighthouse stores columns in DB and has no startup file-scan warmup of the DA cache.

**Evidence (Lighthouse @ 928b61e719).**

- beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:366 cache is in-memory, no startup warmup
- store/src/hot_cold_store.rs:2597 get_data_columns reads DB lazily

**Sources.** [prysm#16207](https://github.com/OffchainLabs/prysm/pull/16207)

</details>


<a id="data_availability-105"></a>
<details>
<summary><b>data_availability-105</b> Compute column sidecars from blobs in parallel — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** When building data column sidecars from blobs or EL cell proofs (proposal or getBlobs), compute cells and columns in parallel across cores instead of sequentially.

**Impact.** Per-blob cell computation is already parallel across cores on the proposal, getBlobs and reconstruction paths; only the cheap column transposition is sequential.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/kzg_utils.rs:382-427`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L382-L427) compute_cells_with_provided_proofs into_par_iter (proposal / getBlobs V2-V3 with EL proofs)
- [`beacon_node/beacon_chain/src/kzg_utils.rs:343-355`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L343-L355) blobs_to_data_column_sidecars_gloas par compute_cells_and_proofs
- [`beacon_node/beacon_chain/src/kzg_utils.rs:431-470`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L431-L470) blobs_to_partial_data_columns par over blobs (fetch_blobs path)
- [`beacon_node/beacon_chain/src/kzg_utils.rs:475`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L475) compute_cells par
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:660-700`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L660-L700) compute_custody_columns_to_import runs it in spawn_blocking

**Skeptic check.** Verified every blob-to-column entry point (proposal, getBlobs, partial columns, reconstruction) uses rayon into_par_iter per blob. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#14396](https://github.com/OffchainLabs/prysm/pull/14396), [prysm#16115](https://github.com/OffchainLabs/prysm/pull/16115)

</details>


<a id="data_availability-106"></a>
<details>
<summary><b>data_availability-106</b> Request sampled columns concurrently — <i>implemented · low · S · latency</i></summary>

**Idea.** Request and verify the sampled data columns from peers concurrently, not one after another, so sampling finishes inside the slot.

**Impact.** Lighthouse does not do separate peer sampling; custody column fetches go to many peers at once.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context/custody.rs:240`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L240) continue_requests groups all pending columns by selected peer
- [`beacon_node/network/src/sync/network_context/custody.rs:295`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L295) one data_column_lookup_request per peer issued in the same pass, all in flight together
- [`beacon_node/network/src/sync/network_context.rs:540`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L540) range sync issues column by-range requests alongside block requests
- [`beacon_node/network/src/sync/block_lookups/single_block_lookup.rs:420`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/single_block_lookup.rs#L420) custody_lookup_request started as soon as the block is downloaded

**Skeptic check.** ActiveCustodyRequest::continue_requests sends by-root requests to every selected peer in one pass and does not wait for each result in turn. Earlier evidence cited the right area but not the fan-out code; that code is in custody.rs.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#14105](https://github.com/OffchainLabs/prysm/pull/14105)

</details>


<a id="data_availability-107"></a>
<details>
<summary><b>data_availability-107</b> Fetch payload envelope and columns in parallel — <i>implemented · low · S · latency, sync</i></summary>

**Idea.** For Gloas blocks, request the execution payload envelope and the block's data columns at the same time instead of one after the other.

**Impact.** Envelope and columns download concurrently on both lookup and range sync paths.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/single_block_lookup.rs:398`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/single_block_lookup.rs#L398) data request starts once block is downloaded (peek_downloaded_data), not imported
- [`beacon_node/network/src/sync/block_lookups/single_block_lookup.rs:455`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/single_block_lookup.rs#L455) payload envelope request starts on the same condition in the same continue_requests call
- [`beacon_node/network/src/sync/block_lookups/single_block_lookup.rs:481`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/single_block_lookup.rs#L481) only envelope processing waits for block import
- [`beacon_node/network/src/sync/network_context.rs:540`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L540) range sync BlocksAndEnvelopesAndColumns issues envelope and column by-range requests together

**Skeptic check.** Verified that both lookup sync and range sync send envelope and column requests together. Only processing is gated on block import, and that is required. Earlier evidence was right; range sync also does it.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#17486](https://github.com/OffchainLabs/prysm/pull/17486)

</details>


<a id="data_availability-108"></a>
<details>
<summary><b>data_availability-108</b> Reconstruct only requested blobs for blob API — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** When serving blobs through the API, recover only the requested blob rows (cell recovery only for those rows) instead of reconstructing all blobs of the block.

**Impact.** Single-blob API requests recover one row instead of all blobs.

**Best measured result.** Half columns, 72 blobs: all 2.84 s vs single blob 73 ms; half of blobs 1.48 s (pr:lodestar#8567)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/kzg_utils.rs:767-822`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L767-L822) reconstruct_blobs_with_indices recovers cells only for the requested row indices
- [`beacon_node/beacon_chain/src/kzg_utils.rs:829-842`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L829-L842) reconstruct_blobs uses blob_indices_opt
- [`beacon_node/http_api/src/block_id.rs:415-441`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L415-L441) blobs endpoint maps versioned_hashes to indices and passes them
- [`beacon_node/http_api/src/block_id.rs:371`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L371) blob_sidecars endpoint calls reconstruct_blob_sidecars with requested indices

**Skeptic check.** Both the blobs and blob_sidecars endpoints recover only requested rows, and skip recovery when all columns are held. A small extra remains: recover_cells_and_compute_kzg_proofs also computes proofs that the endpoint discards (KzgProof::empty).

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#8567](https://github.com/ChainSafe/lodestar/pull/8567), [prysm#15813](https://github.com/OffchainLabs/prysm/pull/15813)

</details>


<a id="data_availability-109"></a>
<details>
<summary><b>data_availability-109</b> Request only custody cells from EL getBlobs — <i>implemented · medium · S · bandwidth, cpu</i></summary>

**Idea.** Use engine_getBlobsV4 with a per-blob cell bitmap so the EL returns only the cells for the node's custody columns instead of full blobs.

**Impact.** EL returns only custody cells, which cuts EL-to-CL transfer and skips local cell derivation.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:158-169`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L158-L169) uses fetch_and_process_blobs_v4 when the EL supports engine_getBlobsV4
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:420-436`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L420-L436) CustodyColumnsBitArray built from custody_columns_indices and passed to get_blobs_v4

**Skeptic check.** Confirmed the V4 path with a custody-column bitmap; it falls back to V2/V3 only when the EL lacks V4. This matches the caplin PR, which uses one 128-bit cell bitmap per request.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#24088](https://github.com/erigontech/erigon/pull/24088), [prysm#15472](https://github.com/OffchainLabs/prysm/pull/15472)

</details>


<a id="data_availability-110"></a>
<details>
<summary><b>data_availability-110</b> Partial data column dissemination at cell granularity — <i>implemented · high · L · bandwidth, latency</i></summary>

**Idea.** Exchange data columns as gossipsub partial messages so peers send and request only the cells the other side lacks (tracked with per-peer bitmaps, served from held columns, verified with partial KZG checks) instead of whole column sidecars.

**Impact.** Peers send only missing cells, which cuts column bandwidth.

**Best measured result.** Tested on Hoodi and Sepolia; 'advantageous', no reports of reduced performance (pr:lighthouse#9896)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/partial.rs:3`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/partial.rs#L3) gossipsub partial_messages Partial/Metadata implementation
- [`beacon_node/lighthouse_network/src/service/mod.rs:374-375`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L374-L375) enable_partials_for_topic for column topics; :907 publish_partial
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:939-985`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L939-L985) full columns republished as partials; :1050-1134 partial verification and getBlobs trigger
- [`beacon_node/beacon_chain/src/partial_data_column_assembler.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/partial_data_column_assembler.rs) assembler
- [`beacon_node/src/cli.rs:693-701`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L693-L701) --enable-partial-columns default true

**Skeptic check.** This is Lighthouse's own PR #9896, present and on by default (the CLI default is true; it is disabled only on networks where one subnet holds more than one column). Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#9053](https://github.com/ChainSafe/lodestar/pull/9053), [prysm#17065](https://github.com/OffchainLabs/prysm/pull/17065), [lighthouse#9896](https://github.com/sigp/lighthouse/pull/9896), [prysm#17348](https://github.com/OffchainLabs/prysm/pull/17348), [silver#287](https://github.com/gattaca-com/silver/pull/287), [silver#289](https://github.com/gattaca-com/silver/pull/289), [silver#282](https://github.com/gattaca-com/silver/pull/282), [nimbus#8410](https://github.com/status-im/nimbus-eth2/pull/8410)

</details>


<a id="data_availability-111"></a>
<details>
<summary><b>data_availability-111</b> Pass KZG commitments into DA check, skip DB read — <i>implemented · low · S · disk, cpu</i></summary>

**Idea.** Pass the block's KZG commitments directly into the data availability check on import instead of reloading and decoding the block from the database.

**Impact.** No DB reload of the block on the import path; Gloas gossip columns hit an in-memory bid cache first.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:34`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L34) commitments read from the in-memory pending block
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:643`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L643) verify_columns_against_block takes commitments from the block/bid passed in
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1572`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1572) load_gloas_payload_bid checks pending_payload_cache then early_attester_cache before falling back to store, and caches the result

**Skeptic check.** Pre-Gloas commitments come from the cached pending block or the column itself. For Gloas, load_gloas_payload_bid reads the store only after two cache misses and then fills the cache. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#16405](https://github.com/OffchainLabs/prysm/pull/16405), [prysm#16515](https://github.com/OffchainLabs/prysm/pull/16515), [teku#10818](https://github.com/Consensys-Incorporated/teku/pull/10818), [prysm#16643](https://github.com/OffchainLabs/prysm/pull/16643)

</details>


<a id="data_availability-112"></a>
<details>
<summary><b>data_availability-112</b> Cooldown peers that return empty column responses — <i>not · low · S · bandwidth, sync</i></summary>

**Idea.** After a by-root column request returns zero sidecars, exclude that peer for a short cooldown in peer selection so download loops do not re-ask it many times per second.

**Gap in Lighthouse.** Record a per-peer last-empty time in ActiveCustodyRequest and skip such peers in select_column_peer for a few seconds.

**Impact.** Fewer redundant DataColumnsByRoot requests during lookups; small CPU and bandwidth gain.

**Best measured result.** one peer got 2,351 empty by-root requests in a minute (pr:caplin#24992)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context/custody.rs:243`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L243) empty response counted as success; comment admits many retries
- [`beacon_node/network/src/sync/network_context/custody.rs:238`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L238) select_column_peer has no empty-response cooldown

**Sources.** [caplin#24992](https://github.com/erigontech/erigon/pull/24992)

</details>


<a id="data_availability-113"></a>
<details>
<summary><b>data_availability-113</b> Filter column request peers by earliest available slot — <i>implemented · medium · S · sync</i></summary>

**Idea.** Select peers for sidecar requests using the earliest available slot they advertise in status, so requests do not go to peers that pruned the data.

**Impact.** Column requests avoid peers that pruned the data.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/peerdb/sync_status.rs:34-40`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/peerdb/sync_status.rs#L34-L40) has_slot uses earliest_available_slot
- [`beacon_node/lighthouse_network/src/peer_manager/peerdb/peer_info.rs:343`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/peerdb/peer_info.rs#L343) is_synced_or_advanced_with_available_slot
- [`beacon_node/lighthouse_network/src/peer_manager/peerdb.rs:255`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/peerdb.rs#L255) synced_peers_for_epoch; :297 good_custody_subnet_peer(subnet, slot)
- [`beacon_node/network/src/sync/network_context/custody.rs:364`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L364) select_column_peer uses get_custodial_peers(column, block_slot)
- [`beacon_node/network/src/sync/backfill_sync/mod.rs:225`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/backfill_sync/mod.rs#L225),883 and custody_backfill_sync/mod.rs:1042 synced_peers_for_epoch

**Skeptic check.** Custody by-root peer selection, which serves both lookups and range/backfill batches, filters by the slot the peer advertises. Backfill and custody backfill do the same at epoch level. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#10269](https://github.com/Consensys-Incorporated/teku/pull/10269)

</details>


<a id="data_availability-114"></a>
<details>
<summary><b>data_availability-114</b> Rank column peers by historical response rate — <i>not · medium · S · sync</i></summary>

**Idea.** Choose peers for column requests by past success rate (columns received versus requested), using free request capacity only as tiebreaker.

**Gap in Lighthouse.** Failure memory is per-lookup (peer_attempts) or per-batch (failed_peers) only; global peer score is a coarse filter. Keep per-peer columns-received/requested counters (PeerDB or SyncNetworkContext) and sort on them in select_column_peer and select_columns_by_range_peers_to_request before the random tiebreak.

**Impact.** Fewer failed custody column requests and retries in lookups and range sync; small sync latency gain, not CPU.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context/custody.rs:353`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L353) select_column_peer ranks by concurrency limit, lookup_peers, per-lookup peer_attempts, random hash
- [`beacon_node/network/src/sync/network_context.rs:578`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L578) select_columns_by_range_peers_to_request ranks by per-batch peers_to_deprioritize (batch.failed_peers), concurrency limit, random
- [`beacon_node/lighthouse_network/src/peer_manager/peerdb.rs:297`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/peerdb.rs#L297) good_custody_subnet_peer filters only by connected/good gossipsub score/custody/synced

**Verdict history.** not (checked) → not (refuted)

**Sources.** [teku#10277](https://github.com/Consensys-Incorporated/teku/pull/10277)

</details>


<a id="data_availability-115"></a>
<details>
<summary><b>data_availability-115</b> Persist columns before pruning — <i>n/a · low · S · disk</i></summary>

**Idea.** Write new data columns to storage before running pruning, so a pruning pass never deletes data that is not stored yet.

**Impact.** Pruning only touches data older than the split, never data about to be written, so the ordering race does not exist.

**Evidence (Lighthouse @ 928b61e719).**

- store/src/hot_cold_store.rs:3277 try_prune_blobs only prunes epochs older than min(DA boundary - margin, split)
- beacon_chain/src/migrate.rs:213 run on finalization in migrator thread

**Sources.** [grandine#327](https://github.com/grandinetech/grandine/pull/327)

</details>


<a id="data_availability-116"></a>
<details>
<summary><b>data_availability-116</b> Prune stale DA and quarantine entries by finality or expiry — <i>implemented · medium · S · memory</i></summary>

**Idea.** Prune the column quarantine, pending availability cache and related per-root caches on every finalization or pruning pass by slot or epoch, not only at a size threshold, so entries for blocks that never arrive cannot accumulate.

**Impact.** Pending DA and assembler entries for blocks that never arrive are dropped each epoch, in addition to the LRU cap.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker.rs:693-751`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L693-L751) availability_cache_maintenance_service runs every epoch with cutoff max(finalized+1, DA boundary)
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:720-737`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L720-L737) do_maintenance removes entries by epoch
- [`beacon_node/beacon_chain/src/partial_data_column_assembler.rs:256`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/partial_data_column_assembler.rs#L256) assembler do_maintenance
- [`beacon_node/beacon_chain/src/canonical_head.rs:1615`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1615) observed_column_sidecars.prune; :1656 pending_payload_cache.do_maintenance

**Skeptic check.** Confirmed a periodic epoch-based prune of the pending-components cache, the partial assembler and the observed caches, not only at a size threshold. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#8693](https://github.com/status-im/nimbus-eth2/pull/8693), [nimbus#8691](https://github.com/status-im/nimbus-eth2/pull/8691), [lighthouse#5895](https://github.com/sigp/lighthouse/pull/5895), [nimbus#9139](https://github.com/status-im/nimbus-eth2/pull/9139), [teku#8128](https://github.com/Consensys-Incorporated/teku/pull/8128)

</details>


<a id="data_availability-117"></a>
<details>
<summary><b>data_availability-117</b> Store only original columns and rebuild extension on demand — <i>not · high · M · disk</i></summary>

**Idea.** On supernodes, store only the first-half (original) data columns plus the extension columns' KZG proofs, and rebuild the extension columns on demand with deduplicated work, about halving column storage.

**Gap in Lighthouse.** Supernodes store all 128 columns. To halve storage: persist only columns 0..63 plus the extension cell KZG proofs, and rebuild columns 64..127 in the hot_cold_store get_data_column(s) read path (RPC DataColumnsByRoot/ByRange and HTTP), with a dedup of concurrent rebuilds per block root and an LRU of rebuilt columns; needs a DB schema change and a migration.

**Impact.** Supernode column storage roughly halves (Teku: ~508 GB to ~260 GB at 14 blobs); no effect on non-supernodes; adds CPU on serving extension columns.

**Best measured result.** ~508 GB to ~260 GB stated in #10137 for 14 blobs (pr:teku#10132)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:959-1011`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L959-L1011) put_data_column(s) writes every custody column sidecar in full to DBColumn::BeaconDataColumn
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1348-1371`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1348-L1371) get_data_columns/get_data_column read the store directly; no rebuild step
- [`beacon_node/beacon_chain/src/migrate.rs:786`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L786),846 DeleteDataColumns only for pruned or abandoned-payload blocks, not for extension columns
- [`beacon_node/http_api/src/block_id.rs:370`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L370),436 reconstruction from stored columns only to serve blobs over HTTP, not to save storage
- [`beacon_node/beacon_chain/src/kzg_utils.rs:889`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L889) reconstruct_data_columns used only by the in-memory DA checker / pending payload cache

**Verdict history.** not (checked) → not (refuted)

**Sources.** [teku#10132](https://github.com/Consensys-Incorporated/teku/pull/10132), [teku#10131](https://github.com/Consensys-Incorporated/teku/pull/10131), [teku#10508](https://github.com/Consensys-Incorporated/teku/pull/10508)

</details>


<a id="data_availability-118"></a>
<details>
<summary><b>data_availability-118</b> Clean legacy unpruned column buckets at startup — <i>n/a · low · S · disk</i></summary>

**Idea.** At startup, delete in batches columns in old storage buckets that the regular pruner never covers.

**Gap in Lighthouse.** Lighthouse uses one column DB bucket with no legacy unpruned buckets.

**Impact.** None.

**Best measured result.** 55,680 expired columns across 435 roots found on Hoodi (pr:lodestar#10223)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/lib.rs:261`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/lib.rs#L261) single DBColumn::BeaconDataColumn
- [`beacon_node/store/src/hot_cold_store.rs:1349`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1349) DeleteDataColumns in regular pruning

**Sources.** [lodestar#10223](https://github.com/ChainSafe/lodestar/pull/10223)

</details>


<a id="data_availability-119"></a>
<details>
<summary><b>data_availability-119</b> Blob pruning at startup policy — <i>n/a · low · S · disk, startup</i></summary>

**Idea.** Decide whether to run a blob pruning pass at startup: run one to remove blobs past retention when no new saves trigger pruning, or skip it to avoid a full directory scan at boot.

**Impact.** Blobs and columns live in a KV DB tracked by oldest_data_slot; there is no filesystem scan at boot.

**Evidence (Lighthouse @ 928b61e719).**

- store/src/hot_cold_store.rs:3277 prune driven by oldest_data_slot in DB info, no directory scan
- hot_cold_store.rs:3300 should_prune uses epochs_per_blob_prune

**Sources.** [prysm#16602](https://github.com/OffchainLabs/prysm/pull/16602), [prysm#13412](https://github.com/OffchainLabs/prysm/pull/13412)

</details>


<a id="data_availability-120"></a>
<details>
<summary><b>data_availability-120</b> Skip rebroadcast of columns already seen on gossip — <i>implemented · medium · S · bandwidth, cpu</i></summary>

**Idea.** Before publishing columns built from EL blobs or reconstruction, skip those already received on gossip (mark them in the gossip seen cache) and those not from the current slot.

**Impact.** Avoids redundant column publishing bandwidth.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/mod.rs:1264-1322`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L1264-L1322) publish_data_columns_gradually filters each batch by observe_gossip_data_column (PriorKnown skipped)
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:632-650`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L632-L650),710-732 EL-built columns deduped against gossip-observed and DA-cached indices
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:216`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L216) RPC/sync path calls fetch with publish_blobs=false
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1510`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1510) reconstruction (which publishes) is triggered only from gossip

**Skeptic check.** There is no explicit current-slot check. Publishing happens only on the gossip-triggered EL fetch and reconstruction paths; sync uses publish_blobs=false, and every batch is re-checked against the gossip seen cache just before it is sent, so the effect matches.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#8668](https://github.com/status-im/nimbus-eth2/pull/8668), [prysm#15153](https://github.com/OffchainLabs/prysm/pull/15153), [teku#8675](https://github.com/Consensys-Incorporated/teku/pull/8675)

</details>


<a id="data_availability-121"></a>
<details>
<summary><b>data_availability-121</b> Retain sidecars for backfill window — <i>n/a · low · S · bandwidth, sync</i></summary>

**Idea.** When backfill is required, keep sidecars in the quarantine back to the minimum request epochs instead of pruning at finalization, so backfill does not refetch them.

**Impact.** Lighthouse has no sidecar quarantine; columns for imported blocks are stored in the DB and are not refetched by backfill.

**Evidence (Lighthouse @ 928b61e719).**

- beacon_chain/src/data_availability_checker.rs no quarantine of sidecars; imported columns persisted to DB via put_data_columns (store/src/hot_cold_store.rs:985)

**Sources.** [nimbus#7294](https://github.com/status-im/nimbus-eth2/pull/7294)

</details>


<a id="data_availability-122"></a>
<details>
<summary><b>data_availability-122</b> Query columns by slot range during sync — <i>implemented · medium · S · sync, bandwidth</i></summary>

**Idea.** Request data columns by slot range during sync instead of one by-root request per block.

**Impact.** Forward range sync and backfill do not send one request per block; they send one batched request per peer per epoch.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_sidecar_coupling.rs:236-262`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_sidecar_coupling.rs#L236-L262) range batch collects all data-bearing block roots and issues one custody_lookup_request
- [`beacon_node/network/src/sync/network_context/custody.rs:294-304`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L294-L304) one DataColumnsByRoot request per peer carrying all block_roots of the batch
- [`beacon_node/network/src/sync/network_context.rs:1606-1640`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L1606-L1640) custody backfill uses DataColumnsByRange

**Skeptic check.** The earlier evidence was wrong about the mechanism. Forward range sync and backfill now fetch columns by root after blocks arrive (network_context.rs:535 comment), not by range; only custody backfill uses DataColumnsByRange. The cost the idea removes, one by-root request per block, is still avoided, because custody.rs batches all roots of the epoch into one request per peer.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [silver#31](https://github.com/gattaca-com/silver/pull/31)

</details>


<a id="data_availability-123"></a>
<details>
<summary><b>data_availability-123</b> Reconstruct without holding the DA cache lock — <i>partial · low · S · latency</i></summary>

**Idea.** Run erasure-coding reconstruction outside the availability cache write lock and recheck the cache before publishing, so other columns keep being processed and duplicates are not published.

**Gap in Lighthouse.** Gloas PendingPayloadCache::reconstruct_data_columns does not re-read the cache after reconstruction, so columns that arrived during the ~500ms recovery are imported and published again (gossipsub dedups the publish, so the cost is small).

**Impact.** Avoids re-import and duplicate publish attempts of columns received during Gloas reconstruction.

**Best measured result.** Logs show reconstruction blocked incoming column processing (~500ms between verify at 15.781 and reconstructed at 16.280) (pr:lighthouse#5986)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:592`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L592) check_and_set_reconstruction_started clones columns under the write lock, then releases it
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:565`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L565) reconstruct_columns runs outside the lock
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:583`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L583) Fulu path rechecks cached_data_column_indexes after reconstruction
- [`beacon_node/beacon_chain/src/pending_payload_cache/mod.rs:482`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/mod.rs#L482) Gloas path takes existing_column_indices from the pre-reconstruction snapshot
- [`beacon_node/beacon_chain/src/pending_payload_cache/mod.rs:512`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/mod.rs#L512) Gloas filter uses the stale snapshot; no recheck before import and publish

**Skeptic check.** Lock release and post-reconstruction recheck are real on the Fulu DataAvailabilityChecker path (earlier evidence correct there); the parallel Gloas reconstruction in pending_payload_cache lacks the recheck.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lighthouse#5986](https://github.com/sigp/lighthouse/pull/5986), [lighthouse#5990](https://github.com/sigp/lighthouse/pull/5990), [lighthouse#6403](https://github.com/sigp/lighthouse/pull/6403)

</details>


<a id="data_availability-124"></a>
<details>
<summary><b>data_availability-124</b> Reconstruction queue capacity one — <i>implemented · low · S · cpu</i></summary>

**Idea.** Limit the beacon processor reconstruction queue to one item so bursts do not queue many expensive reconstruction tasks.

**Impact.** At most one reconstruction task is queued, and the newest one replaces older ones.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_queue.rs:381`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_queue.rs#L381) column_reconstruction_queue: 1
- [`beacon_node/beacon_processor/src/scheduler/work_queue.rs:522`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_queue.rs#L522) LifoQueue::new(column_reconstruction_queue)
- [`beacon_node/beacon_processor/src/lib.rs:1352`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1352) Work::ColumnReconstruction pushed into that queue

**Skeptic check.** This is Lighthouse's own PR 8053, and it is present in the code. All ColumnReconstruction work goes through the capacity-1 LIFO queue.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#8053](https://github.com/sigp/lighthouse/pull/8053)

</details>


<a id="data_availability-125"></a>
<details>
<summary><b>data_availability-125</b> Wall-clock timeout on column reconstruction — <i>not · medium · S · latency</i></summary>

**Idea.** Bound column reconstruction with a wall-clock timeout checked before each per-blob task and while waiting for results, so slow recovery cannot stall the node.

**Gap in Lighthouse.** No wall-clock bound on the reconstruction itself. Check a deadline per blob row in kzg_utils::reconstruct_data_columns / around the awaited rayon task, and on expiry abort and reset reconstruction state.

**Impact.** Only matters for supernodes/semi-supernodes under slow recovery; protects the HighPriority rayon pool from stalls.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:3785`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3785) reconstruct_data_columns awaits spawn_blocking_with_rayon_async on HighPriority pool with no timeout
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:537`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L537) reconstruct_data_columns: timer metric only, failure resets via handle_reconstruction_failure, no deadline
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:107`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L107) RECONSTRUCTION_DEADLINE is a start trigger (1/4 slot), not an abort

**Verdict history.** not (checked) → not (refuted)

**Sources.** [nimbus#7610](https://github.com/status-im/nimbus-eth2/pull/7610)

</details>


<a id="data_availability-126"></a>
<details>
<summary><b>data_availability-126</b> Minimum custody with full-subnet sampling mode — <i>partial · medium · M · bandwidth</i></summary>

**Idea.** Offer a mode that custodies the minimum column count but subscribes to 64 column subnets to reconstruct all columns, serving fewer RPC requests than a supernode.

**Gap in Lighthouse.** Semi-supernode reaches reconstruction by advertising and serving 64 columns. No mode keeps the advertised cgc at the minimum while subscribing to 64 subnets; would need a sampling-subscription count decoupled from the advertised cgc in CustodyContext/NetworkGlobals.

**Impact.** Reconstruct-capable node with fewer RPC serving duties; saves upload bandwidth versus semi-supernode.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/custody_context.rs:231`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L231) NodeCustodyType::SemiSupernode custodies and advertises number_of_custody_groups/2
- [`beacon_node/src/cli.rs:63`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L63) --semi-supernode flag
- [`beacon_node/lighthouse_network/src/types/globals.rs:68`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/globals.rs#L68) sampling_subnets derived from spec sampling_size_custody_groups(cgc), no separate override

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [prysm#16014](https://github.com/OffchainLabs/prysm/pull/16014)

</details>


<a id="data_availability-127"></a>
<details>
<summary><b>data_availability-127</b> Batch several epochs per missing-column refill — <i>not · low · S · sync</i></summary>

**Idea.** When requesting missing columns, request several epochs (for example 3) per batch instead of one.

**Gap in Lighthouse.** Raise CUSTODY_BACKFILL_EPOCHS_PER_BATCH (and its uses at lines 306-582) to 3; check batch size limits of columns-by-range.

**Impact.** Fewer round trips during custody backfill only; a rare path, small gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/custody_backfill_sync/mod.rs:40`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/custody_backfill_sync/mod.rs#L40) CUSTODY_BACKFILL_EPOCHS_PER_BATCH=1
- [`beacon_node/network/src/sync/range_sync/chain.rs:30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L30) EPOCHS_PER_BATCH=1

**Sources.** [nimbus#7419](https://github.com/status-im/nimbus-eth2/pull/7419)

</details>


<a id="data_availability-128"></a>
<details>
<summary><b>data_availability-128</b> Remove blob archival semaphore — <i>n/a · low · disk, latency</i></summary>

**Idea.** Remove the semaphore that throttles blob archival when it is no longer needed, and add sanity checks on blob segment files.

**Impact.** LH stores blobs in its DB, with no Caplin-style blob segment files or archival semaphore.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store) (no blob segment archive; blobs live in the hot/cold DB)

**Sources.** [caplin#12235](https://github.com/erigontech/erigon/pull/12235)

</details>


<a id="data_availability-129"></a>
<details>
<summary><b>data_availability-129</b> Gloas: check DA on the envelope, not the block — <i>partial · low · S · latency</i></summary>

**Idea.** For Gloas, check data availability on the execution payload envelope so the beacon block enters fork choice without waiting for columns, and do not refetch an envelope already held.

**Gap in Lighthouse.** payload_lookup_request only avoids refetch when the envelope is already in fork choice; an envelope already held in PendingPayloadCache (executed, waiting on columns) is fetched again by RPC.

**Impact.** Saves a redundant PayloadEnvelopesByRoot request in lookups racing gossip; the main block-without-columns effect is already present.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker.rs:871`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L871) Gloas blocks skip MissingCustodyColumns; DA is on the envelope
- [`beacon_node/beacon_chain/src/payload_envelope_verification/mod.rs:79`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/mod.rs#L79) envelope DA via data_columns_required_for_bid
- [`beacon_node/network/src/sync/network_context.rs:829`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L829) payload_lookup_request skips download only if envelope_is_known_to_fork_choice

**Skeptic check.** Confirmed Gloas blocks enter fork choice without waiting for columns (main part implemented). The no-refetch check consults fork choice and store only, not the pending envelope cache.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [silver#377](https://github.com/gattaca-com/silver/pull/377)

</details>


<a id="data_availability-130"></a>
<details>
<summary><b>data_availability-130</b> Remove redundant custody request layer — <i>n/a · low · cpu, memory</i></summary>

**Idea.** Drop a custody-specific request layer when the sampler already covers the custody columns as a superset.

**Impact.** LH has no separate custody request layer; sync requests the sampling/custody columns directly.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context.rs:987`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L987) sampling_columns_for_epoch used directly

**Sources.** [teku#10047](https://github.com/Consensys-Incorporated/teku/pull/10047)

</details>


<a id="data_availability-131"></a>
<details>
<summary><b>data_availability-131</b> Remove coarse locks from column retriever — <i>n/a · low · latency</i></summary>

**Idea.** Replace the single coarse lock in the column sidecar retriever with finer synchronization so request scheduling and peer search do not serialize.

**Impact.** Teku Java retriever lock; LH sync runs in one task owning the network context, no shared coarse lock.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs) (single-owner sync manager, no coarse lock)

**Sources.** [teku#9613](https://github.com/Consensys-Incorporated/teku/pull/9613)

</details>


<a id="data_availability-132"></a>
<details>
<summary><b>data_availability-132</b> DA cache state storage: state root plus LRU vs direct — <i>implemented · low · S · memory</i></summary>

**Idea.** Decide how the pending-availability cache keeps states: a state root with a small LRU and replay on miss, or full states held directly when tree-states share memory, avoiding a redundant layer.

**Impact.** The redundant state LRU/replay layer was removed in favour of storing tree-states directly (lighthouse#8724).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification_types.rs:372`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification_types.rs#L372) BlockImportData holds state: BeaconState&lt;E&gt; directly
- [`beacon_node/beacon_chain/src/data_availability_checker`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker)/ (only overflow_lru_cache.rs and error.rs; no state_lru_cache)

**Skeptic check.** Confirmed that state_lru_cache.rs is gone and that pending blocks keep their full tree-state. This is Lighthouse's own PR, and earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#4801](https://github.com/sigp/lighthouse/pull/4801), [lighthouse#8724](https://github.com/sigp/lighthouse/pull/8724)

</details>


<a id="data_availability-133"></a>
<details>
<summary><b>data_availability-133</b> Shorter per-request lifecycle for column recovery — <i>n/a · low · S · memory</i></summary>

**Idea.** Model column recovery as per-request objects with separate download and rebuild phases and one shorter timeout, so stale requests free resources sooner.

**Gap in Lighthouse.** Lighthouse reconstructs from columns already in the DA cache, with no separate recovery request or long recovery timeout.

**Impact.** None.

**Best measured result.** timeout 2 minutes rather than 5 (pr:teku#9910)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker.rs:537`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L537) reconstruct_data_columns uses columns already in cache, no download phase
- [`beacon_node/network/src/sync/network_context/custody.rs:22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L22) ActiveCustodyRequest already per-request

**Sources.** [teku#9910](https://github.com/Consensys-Incorporated/teku/pull/9910)

</details>


<a id="data_availability-134"></a>
<details>
<summary><b>data_availability-134</b> Pool and retry data-unavailable blocks — <i>implemented · medium · S · bandwidth, sync</i></summary>

**Idea.** Keep blocks that failed import for missing data in a pool and retry them after more waiting instead of dropping and refetching them.

**Impact.** Blocks missing data wait in the DA cache and complete when columns arrive.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:351`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L351) pending components held in LRU awaiting missing data
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:200`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L200) make_available completes the block once columns arrive
- [`beacon_node/network/src/sync/block_lookups/single_block_lookup.rs:398`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/single_block_lookup.rs#L398) lookups request only the missing data, not the block again

**Skeptic check.** Upheld: a block with missing data returns MissingComponents and stays cached instead of being dropped; only LRU capacity eviction can lose it.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#7132](https://github.com/Consensys-Incorporated/teku/pull/7132)

</details>


<a id="data_availability-135"></a>
<details>
<summary><b>data_availability-135</b> Re-issue failed column fetches on availability recheck — <i>implemented · low · S · sync</i></summary>

**Idea.** Let the availability sampler re-issue column requests on incomplete trackers when availability is rechecked, instead of a fetched flag that blocks retries after a failure.

**Impact.** Failed column fetches are retried per column; no sticky fetched flag blocks retries.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context/custody.rs:241`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L241) every column still awaiting download is re-requested on each continue_requests call
- [`beacon_node/network/src/sync/network_context/custody.rs:245`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L245) per-column retry bounded by MAX_CUSTODY_COLUMN_DOWNLOAD_ATTEMPTS
- [`beacon_node/network/src/sync/network_context/custody.rs:262`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L262) columns with no peer stay pending up to MAX_STALE_NO_PEERS_DURATION and are retried when peers appear
- [`beacon_node/network/src/sync/block_lookups/single_block_lookup.rs:917`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/single_block_lookup.rs#L917) lookup-level retries after failed download

**Skeptic check.** The retry mechanism is per column in ActiveCustodyRequest. Failed or missing columns return to awaiting-download and are re-requested from other peers. Earlier evidence cited the lookup-level retry, which is real but less exact.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#10193](https://github.com/Consensys-Incorporated/teku/pull/10193)

</details>


<a id="data_availability-136"></a>
<details>
<summary><b>data_availability-136</b> Read-only head state for sidecar verification — <i>implemented · medium · S · cpu, memory</i></summary>

**Idea.** Verify data column and blob sidecars against the read-only head state when it has the same validator set and shuffling, instead of copying or regenerating the parent state.

**Impact.** Hit path needs no state at all, which is stronger than using the head state.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_column_verification.rs:1746`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1746) with_proposer_cache keyed by proposer shuffling root; state loaded only in miss closure
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1759`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1759) miss path uses get_advanced_hot_state (state cache, not a regen on the hit path)

**Skeptic check.** Upheld: the proposer cache removes state access on the hot path; on a miss it loads the advanced parent state rather than trying the head state, but misses are rare because the cache is primed at import and epoch advance.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#15977](https://github.com/OffchainLabs/prysm/pull/15977)

</details>


<a id="data_availability-137"></a>
<details>
<summary><b>data_availability-137</b> Data column sampling off by default — <i>n/a · low · bandwidth, cpu</i></summary>

**Idea.** Keep peer data column sampling behind an opt-in flag while it is not needed on the critical path.

**Impact.** LH implements custody columns only, with no separate peer sampling stage to gate behind a flag.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/src/cli.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs) (no peer-sampling flag; grep sampling finds only custody sampling_columns_for_epoch)

**Sources.** [lighthouse#6209](https://github.com/sigp/lighthouse/pull/6209)

</details>


<a id="data_availability-138"></a>
<details>
<summary><b>data_availability-138</b> Scale blob fetch concurrency with max blobs — <i>n/a · low · sync</i></summary>

**Idea.** Size blob or column fetch concurrency from the max blobs per block config instead of a fixed constant.

**Impact.** LH concurrency is capped per peer by RPC limits, not by a fixed fetcher constant; request sizes already use spec max blobs.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context.rs:98-117`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L98-L117) per-peer MAX_CONCURRENT_REQUESTS limit
- network_context.rs:1127 max_blobs_per_block already read from spec per epoch

**Sources.** [teku#7071](https://github.com/Consensys-Incorporated/teku/pull/7071)

</details>


<a id="data_availability-139"></a>
<details>
<summary><b>data_availability-139</b> Serialize column persistence tasks — <i>n/a · low · cpu, disk</i></summary>

**Idea.** Allow only one data column persistence task at a time, so bursts of writes do not saturate the thread pool.

**Impact.** LH has no separate async column persistence task pool; columns are written within the block import batch, so there is no burst of tasks to serialize.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:985`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L985) put_data_columns writes inline
- [`beacon_node/store/src/hot_cold_store.rs:1003`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1003) data_columns_as_kv_store_ops batched into block-import ops

**Sources.** [grandine@921e8d642](https://github.com/grandinetech/grandine/commit/921e8d6425fc)

</details>


<a id="data_availability-140"></a>
<details>
<summary><b>data_availability-140</b> Serve column reads from in-flight writes — <i>implemented · low · S · latency</i></summary>

**Idea.** Keep recently written column sidecars in an in-memory map and serve by-root reads from it before the DB write completes.

**Impact.** By-root reads hit in-memory caches first; DB write is synchronous within import and the DA cache entry is not removed on import (only LRU eviction / remove_block_on_execution_error), so there is no in-flight write window to cover.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:1229`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1229) get_data_columns_checking_all_caches checks DA checker, pending payload cache, early attester cache before DB
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4756`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4756) do_atomically_with_block_and_blobs_cache writes columns synchronously inside import_block
- [`beacon_node/store/src/hot_cold_store.rs:998`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L998) block cache populated on column put

**Skeptic check.** Verified the cache-first lookup and that columns stay in the DA checker after import; the Teku PR was a closed spike addressing an async-write window Lighthouse does not have. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#10233](https://github.com/Consensys-Incorporated/teku/pull/10233)

</details>


<a id="data_availability-141"></a>
<details>
<summary><b>data_availability-141</b> Single shared buffer for all column sources — <i>partial · medium · M · memory</i></summary>

**Idea.** Write full gossip columns, partial cells and EL-built columns into one per-slot column cell cache, instead of separate caches, so one buffer serves all sources.

**Gap in Lighthouse.** Gloas already has one per-block cell buffer (PendingColumn) fed by gossip full columns, partial cells, RPC and EL getBlobs. Fulu, the live mainnet fork, still keeps partial and EL cells in PartialDataColumnAssembler and full columns in the overflow_lru_cache PendingComponents, which means double lookups and conversions. Porting the Gloas design back to Fulu is the remaining work. It may not be worth doing as Gloas will replace this path.

**Impact.** Fulu only: saves duplicate cache lookups and the partial-to-full copies per column. Small CPU and memory gain, not a bottleneck. Gloas already has it.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/pending_payload_cache/pending_components.rs:31-32`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/pending_components.rs#L31-L32) Gloas PendingComponents.verified_data_columns is a per-block HashMap&lt;ColumnIndex, PendingColumn&gt; of per-cell Option&lt;(Cell, KzgProof)&gt;, partial or full
- [`beacon_node/beacon_chain/src/pending_payload_cache/pending_components.rs:96-116`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/pending_components.rs#L96-L116) merge_data_columns writes full gossip/RPC columns cell-by-cell into the same PendingColumn store
- [`beacon_node/beacon_chain/src/pending_payload_cache/pending_components.rs:122-150`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/pending_components.rs#L122-L150) merge_partial_data_columns writes partial cells into that same store
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:368-386`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L368-L386) Gloas EL getBlobs columns merge into pending_payload_cache, the same store
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:326-363`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L326-L363) Fulu EL columns go into PartialDataColumnAssembler, then full columns go to the DA checker separately
- [`beacon_node/beacon_chain/src/partial_data_column_assembler.rs:13-34`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/partial_data_column_assembler.rs#L13-L34) Fulu PartialDataColumnAssembler is separate from overflow_lru_cache PendingComponents
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:230-270`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L230-L270) Fulu missing_cells_* consults both caches

**Second check.** The earlier review looked only at the Fulu path. I found that the Gloas pending_payload_cache already uses one cell-level store for all sources, including EL getBlobs. This leaves only the Fulu split, so the verdict stays partial.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [silver#299](https://github.com/gattaca-com/silver/pull/299), [silver#272](https://github.com/gattaca-com/silver/pull/272)

</details>


<a id="data_availability-142"></a>
<details>
<summary><b>data_availability-142</b> Singleflight proposer signature verification — <i>partial · medium · S · cpu</i></summary>

**Idea.** Deduplicate concurrent proposer signature verification for sidecars of the same block (singleflight keyed by signing data), so one parent-state load and BLS verify serves all its columns.

**Gap in Lighthouse.** The parent-state load is single-flight. Partial-column headers are verified once per block and then reused from the assembler cache, but this is not single-flight for concurrent first arrivals. Full Fulu gossip columns still do one header BLS verify per column, up to 128 per block, even when the assembler already holds a verified header with the same signed_block_header. Fix: in verify_proposer_and_signature, or before the call at line 1185, reuse the assembler's verified header (or a small verified-header-root cache) when the signed header matches. Gloas columns carry no signed header, so this applies to Fulu only.

**Impact.** A supernode would do about 1 header BLS verify per block instead of up to 128 (about 1 ms each). This saves tens of ms of CPU in the gossip burst on Fulu.

**Best measured result.** cache misses reduced (graph); up to 128 concurrent duplicates avoided (pr:prysm#15954)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:197`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L197) OnceCell makes the proposer shuffling/state load single-flight
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2490-2501`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2490-L2501) partial-column headers: a cached verified header for the block root skips re-verification (dedup after the first verify)
- [`beacon_node/beacon_chain/src/data_column_verification.rs:654-668`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L654-L668) GossipVerifiedPartialDataColumnHeader::new verifies the signature once, then caches the header in the assembler
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1185`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1185) the full gossip column path calls verify_proposer_and_signature for every column and does not check the assembler header cache
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1774-1787`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1774-L1787) the header BLS verify runs every time it is called

**Second check.** Beyond the earlier review, I found the verified-header cache for partial-column headers (assembler.get_header / was_cached). It dedups after the first verify, but the full-column gossip path does not use it, so the verdict stays partial.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [prysm#15954](https://github.com/OffchainLabs/prysm/pull/15954)

</details>


<a id="data_availability-143"></a>
<details>
<summary><b>data_availability-143</b> Skip DA check outside blob retention window — <i>partial · medium · S · sync, bandwidth</i></summary>

**Idea.** Skip the data availability check and blob or column download for blocks older than the sidecar retention window during sync and checkpoint origin, since the data is not required.

**Gap in Lighthouse.** For Gloas epochs, SyncNetworkContext::batch_type ignores data_columns_required_for_epoch and RangeBlockComponentsRequest::continue_requests fetches custody columns for range/backfill batches older than the retention window.

**Impact.** Once Gloas is older than the retention window, range sync and backfill would download columns peers are not required to serve, causing failed or stalled batches and wasted bandwidth.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/custody_context.rs:574`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L574) da_check_required_for_epoch / data_columns_required_for_epoch use the DA boundary
- [`beacon_node/network/src/sync/network_context.rs:1305`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L1305) Gloas batch_type always BlocksAndEnvelopesAndColumns, with TODO(gloas) 'can be post-gloas and not require columns'
- [`beacon_node/network/src/sync/block_sidecar_coupling.rs:238`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_sidecar_coupling.rs#L238) continue_requests requests custody columns for every data-bearing block without a retention check
- [`beacon_node/network/src/sync/block_lookups/single_block_lookup.rs:405`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/single_block_lookup.rs#L405) lookups gated by data_columns_required_for_block

**Skeptic check.** Pre-Gloas the boundary gating is real on lookups, range sync and the availability check (earlier evidence right). The Gloas range-sync path has an explicit TODO and no gating.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [grandine@0e2fd7284](https://github.com/grandinetech/grandine/commit/0e2fd7284103), [caplin#15806](https://github.com/erigontech/erigon/pull/15806), [prysm#13686](https://github.com/OffchainLabs/prysm/pull/13686)

</details>


<a id="data_availability-144"></a>
<details>
<summary><b>data_availability-144</b> Skip DA check for blocks loaded from local storage — <i>n/a · low · startup</i></summary>

**Idea.** Do not run data availability checks for blocks reloaded from the local database at startup, since their data was already validated.

**Impact.** LH restores fork choice from a persisted snapshot and does not re-import blocks from the DB through the DA check at startup.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/builder.rs:1080`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L1080) DA checker only created empty; fork choice loaded from persisted state

**Sources.** [grandine@88e67880a](https://github.com/grandinetech/grandine/commit/88e67880aaf9)

</details>


<a id="data_availability-145"></a>
<details>
<summary><b>data_availability-145</b> Skip custody group derivation for supernodes — <i>implemented · low · S · cpu</i></summary>

**Idea.** When custody group count equals the total, return all groups directly instead of running the hash-based custody group computation.

**Best measured result.** described as slight optimization (pr:lodestar#8172)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/data/data_column_custody_group.rs:33`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/data/data_column_custody_group.rs#L33) get_custody_groups returns 0..number_of_custody_groups when count equals total
- [`consensus/types/src/data/data_column_custody_group.rs:96`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/data/data_column_custody_group.rs#L96) ordered full computation only once at startup (client/src/builder.rs:241)

**Skeptic check.** Upheld: all runtime callers (globals.rs, peer_manager) go through the shortcut; the hash loop runs only for the one-time ordered index list.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#8172](https://github.com/ChainSafe/lodestar/pull/8172), [lighthouse#7890](https://github.com/sigp/lighthouse/pull/7890), [teku#9709](https://github.com/Consensys-Incorporated/teku/pull/9709), [grandine@3139203d7](https://github.com/grandinetech/grandine/commit/3139203d7269)

</details>


<a id="data_availability-146"></a>
<details>
<summary><b>data_availability-146</b> Recompute custody count only on finalization — <i>implemented · low · S · cpu</i></summary>

**Idea.** Recompute validator custody group count only when finalization changes, not every slot.

**Impact.** No per-slot CGC recomputation; the cost is a sum over registered validators per subscription call, negligible.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/custody_context.rs:92`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L92) register_validators recomputes CGC only when validators register via the subscription API
- [`beacon_node/http_api/src/validator/mod.rs:1104`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L1104) only non-test caller
- [`beacon_node/beacon_chain/src/custody_context.rs:507`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L507) sampling_columns_for_epoch reads stored list

**Skeptic check.** Lighthouse computes CGC event-driven on validator registration and stores it per effective epoch, so the Teku per-slot recomputation problem does not exist. Earlier verdict upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#9723](https://github.com/Consensys-Incorporated/teku/pull/9723)

</details>


<a id="data_availability-147"></a>
<details>
<summary><b>data_availability-147</b> Skip proposer checks for EL-built columns — <i>implemented · low · S · cpu</i></summary>

**Idea.** For columns built from the EL getBlobs response of an already verified block, skip proposer and signature checks.

**Impact.** EL-built columns bypass gossip proposer/signature verification entirely and go straight into the DA cache as execution-verified.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:627`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L627) EL columns wrapped via KzgVerifiedPartialDataColumn::from_execution_verified
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:704`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L704) from_execution_verified for full columns
- [`beacon_node/beacon_chain/src/data_column_verification.rs:395`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L395) new_for_block_publishing skips proposer/signature checks for locally built columns

**Skeptic check.** PR 7553 itself was closed, but current fetch_blobs constructs columns as execution-verified without any proposer or signature check, which achieves the same effect. Earlier evidence cited the publishing path; the getBlobs path is the more relevant one and also skips checks.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#7553](https://github.com/sigp/lighthouse/pull/7553)

</details>


<a id="data_availability-148"></a>
<details>
<summary><b>data_availability-148</b> Skip DA work for blocks without blob commitments — <i>implemented · low · S · cpu</i></summary>

**Idea.** For blocks with zero blob commitments, skip KZG validation, quarantine lookups and sampling trackers entirely.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:210`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L210) num_expected_blobs == 0 makes the block available at once
- [`beacon_node/beacon_chain/src/custody_context.rs:590`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L590) data_columns_required_for_block requires num_expected_blobs &gt; 0 (lookups, sampling)
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:144`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L144) EL fetch returns early with no versioned hashes
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1542`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1542) commitments_len == 0 skips KZG

**Skeptic check.** Upheld: zero-blob blocks skip KZG, column requests and EL fetch; they still pass through the DA cache insert (and partial assembler init when enabled), which is trivial.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#7184](https://github.com/ChainSafe/lodestar/pull/7184), [nimbus#7674](https://github.com/status-im/nimbus-eth2/pull/7674), [teku#10327](https://github.com/Consensys-Incorporated/teku/pull/10327), [lodestar#8277](https://github.com/ChainSafe/lodestar/pull/8277), [lodestar#8473](https://github.com/ChainSafe/lodestar/pull/8473)

</details>


<a id="data_availability-149"></a>
<details>
<summary><b>data_availability-149</b> Skip publishing columns while syncing — <i>partial · medium · S · bandwidth, cpu</i></summary>

**Idea.** While the node is syncing, do not publish reconstructed or EL-recovered column sidecars to gossip.

**Gap in Lighthouse.** spawn_fetch_block_columns / fetch_engine_blobs_and_publish_full (gossip block, envelope and partial-header triggers) publish EL-recovered columns to gossip without checking network_globals.sync_state; only reconstruction and the RPC-sync path are gated.

**Impact.** A node that fell behind keeps doing column computation and gossip publishing for EL-recovered columns while syncing.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:314`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L314) queued ColumnReconstruction is drop_during_sync
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:216`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L216) RPC-sync EL fetch uses publish_blobs=false
- [`beacon_node/network/src/network_beacon_processor/mod.rs:205`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L205) gossip blocks are not dropped during sync
- [`beacon_node/network/src/network_beacon_processor/mod.rs:972`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L972) spawn_fetch_block_columns sets publish_blobs=true with no sync-state check
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1125`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1125) partial-header getBlobs path publishes unconditionally
- [`beacon_node/network/src/sync/manager.rs:775`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L775) core topics stay subscribed after the first Synced, so gossip blocks keep arriving when the node falls back to SyncingHead/SyncingFinalized

**Skeptic check.** Reconstruction drop-during-sync and RPC publish_blobs=false confirmed (earlier evidence right there), but the teku change also gates EL-recovered columns, which LH publishes from gossip-triggered getBlobs regardless of sync state.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [teku#10033](https://github.com/Consensys-Incorporated/teku/pull/10033), [teku#10103](https://github.com/Consensys-Incorporated/teku/pull/10103), [teku#10104](https://github.com/Consensys-Incorporated/teku/pull/10104)

</details>


<a id="data_availability-150"></a>
<details>
<summary><b>data_availability-150</b> Skip EL column compute for imported blocks — <i>implemented · medium · S · cpu</i></summary>

**Idea.** Before computing columns from EL blobs, check whether the block is already imported and skip the computation.

**Impact.** Skips KZG cell/proof computation for blocks already imported via gossip.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:272-279`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L272-L279) fork_choice_contains_block before compute_custody_columns_to_import (V1/V2/V3 path)
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:485-491`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L485-L491) same check before build_partial_columns_from_v4_response

**Skeptic check.** Confirmed the already-imported check sits right before column computation on both the getBlobs V3 and V4 paths. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#6816](https://github.com/sigp/lighthouse/pull/6816)

</details>


<a id="data_availability-151"></a>
<details>
<summary><b>data_availability-151</b> Skip block presence check after early import — <i>n/a · low · cpu</i></summary>

**Idea.** After a block is imported, skip the block presence check for later sidecars of it.

**Impact.** Grandine-specific block-presence lookup; LH gossip column checks use an observation cache and the DA cache, with no separate block presence store check to skip.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_column_verification.rs:1647`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1647) verify_is_unknown_sidecar uses observed cache
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1770`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1770) proposer check via cache

**Sources.** [grandine@bf1c0734f](https://github.com/grandinetech/grandine/commit/bf1c0734fbd5)

</details>


