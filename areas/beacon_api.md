# beacon_api (part 1 of 2)

305 ideas: 34 not, 66 partial, 148 implemented, 57 n/a; 35 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

Pages: [part 1](beacon_api.md) · [part 2](beacon_api-2.md)

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [beacon_api-001](#beacon_api-001) | Serve duty queries from epoch caches, not loaded states | partial | low | S | cpu, memory, latency |
| [beacon_api-002](#beacon_api-002) | Read sync committee duties from head state | implemented | medium | S | cpu, latency |
| [beacon_api-003](#beacon_api-003) | Cache validator-to-sync-committee positions per period | not | low | S | cpu, latency |
| [beacon_api-004](#beacon_api-004) | Serve proposer duties from a decision-root-keyed proposer cache | partial | low | S | cpu, latency |
| [beacon_api-005](#beacon_api-005) **★** | Compute duties for all validators in one committee pass | partial | medium | S | cpu, latency |
| [beacon_api-006](#beacon_api-006) | Return assignments only for requested validators | partial | low | S | memory, cpu |
| [beacon_api-007](#beacon_api-007) | Run HTTP API through bounded priority work scheduler | implemented | low | S | cpu, latency |
| [beacon_api-008](#beacon_api-008) | Run heavy API handlers on blocking thread pool | implemented | low | S | cpu, latency |
| [beacon_api-009](#beacon_api-009) | Bounded virtual-thread pool for REST and SSE | n/a | low | S | cpu, memory, latency |
| [beacon_api-010](#beacon_api-010) | HTTP cache headers for immutable REST responses | not | low | S | cpu, bandwidth |
| [beacon_api-011](#beacon_api-011) | POST variant of validators and balances queries | implemented | low | S | cpu, latency |
| [beacon_api-012](#beacon_api-012) | SSZ responses for validators and balances endpoints | partial | low | S | cpu, bandwidth, latency |
| [beacon_api-013](#beacon_api-013) | SSZ responses for get-block endpoints | implemented | low | S | cpu, bandwidth |
| [beacon_api-014](#beacon_api-014) | Serve SSZ blocks straight from stored bytes | partial | low | M | cpu, memory |
| [beacon_api-015](#beacon_api-015) | SSZ for block production endpoints | implemented | low | S | cpu, bandwidth, latency |
| [beacon_api-016](#beacon_api-016) | SSZ responses for beacon state endpoints | implemented | low | S | cpu, memory, bandwidth |
| [beacon_api-017](#beacon_api-017) | SSZ for attestation data and aggregate endpoints | partial | low | S | cpu, bandwidth, latency |
| [beacon_api-018](#beacon_api-018) | Accept SSZ bodies when publishing blocks | implemented | low | S | cpu, bandwidth, latency |
| [beacon_api-019](#beacon_api-019) **★** | Accept SSZ bodies on attestation pool submission | not | medium | S | cpu, bandwidth |
| [beacon_api-020](#beacon_api-020) | Accept SSZ bodies on register_validator | not | low | S | cpu, bandwidth |
| [beacon_api-021](#beacon_api-021) | Request builder API responses as SSZ | implemented | medium | S | cpu, bandwidth, latency |
| [beacon_api-022](#beacon_api-022) | SSZ for ePBS payload attestation and preference endpoints | implemented | low | S | cpu, bandwidth |
| [beacon_api-023](#beacon_api-023) | Generic Accept negotiation to serve SSZ | not | low | M | cpu, bandwidth |
| [beacon_api-024](#beacon_api-024) **★** | Process submitted pool messages in background after response | not | medium | M | latency |
| [beacon_api-025](#beacon_api-025) | Return envelope publish after broadcast, import in background | partial | low | S | latency |
| [beacon_api-026](#beacon_api-026) | Insert API attestations into pool synchronously | implemented | low | S | cpu |
| [beacon_api-027](#beacon_api-027) | Bounded per-subscriber SSE queues, drop slow clients | partial | low | S | latency, memory |
| [beacon_api-028](#beacon_api-028) | Eager SSE socket writes with larger output cap | n/a | low |  | latency, bandwidth |
| [beacon_api-029](#beacon_api-029) | Build SSE payloads only when subscribers exist | implemented | low | S | cpu |
| [beacon_api-030](#beacon_api-030) | Share payload attributes between SSE and engine call | implemented | low | S | cpu, latency |
| [beacon_api-031](#beacon_api-031) | Skip head SSE event when head unchanged | implemented | low | S | cpu, bandwidth |
| [beacon_api-032](#beacon_api-032) | Always unregister event-stream listeners | implemented | low | S | memory |
| [beacon_api-033](#beacon_api-033) | Emit head/block SSE event early in import | partial | low | S | latency |
| [beacon_api-034](#beacon_api-034) | Tear down cancelled REST responses, async timeout | n/a | low |  | memory |
| [beacon_api-035](#beacon_api-035) | Answer attestation_data from fork choice | partial | low | M | latency |
| [beacon_api-036](#beacon_api-036) | Cache attestation data per slot, no per-request state copy | implemented | low | S | memory, cpu |
| [beacon_api-037](#beacon_api-037) | Ancestor root from state block_roots for attestation data | implemented | low | S | disk, latency |
| [beacon_api-038](#beacon_api-038) | Read head state fields without cloning the state | implemented | low | S | memory, cpu |
| [beacon_api-039](#beacon_api-039) | No state mutation on read-only API paths | implemented | low | S | cpu, memory |
| [beacon_api-040](#beacon_api-040) | Send buffered HTTP bodies with Content-Length | implemented | low | S | bandwidth, latency |
| [beacon_api-041](#beacon_api-041) | No selection-proof check on subnet subscriptions | implemented | low | S | cpu |
| [beacon_api-042](#beacon_api-042) | Drop extra JSON marshal in debug state API | implemented | low | S | cpu, memory, latency |
| [beacon_api-043](#beacon_api-043) | Debug state as value without SSZ round trip | implemented | low | S | cpu, memory |
| [beacon_api-044](#beacon_api-044) | Primitive ints for validator index streams | n/a | low |  | memory, cpu |
| [beacon_api-045](#beacon_api-045) | Sync committee subscriptions without intermediate sequence | partial | low | S | memory |
| [beacon_api-046](#beacon_api-046) | Leak-free one-shot wait for checkpoint state | n/a | low |  | memory |
| [beacon_api-047](#beacon_api-047) | Blob sidecar requests resolve root without loading block | partial | low | M | disk, cpu |
| [beacon_api-048](#beacon_api-048) | Skip state root recompute after process_slots | implemented | low | S | cpu |
| [beacon_api-049](#beacon_api-049) | Hand-written hex QUANTITY validation, no regex | n/a | low |  | cpu |
| [beacon_api-050](#beacon_api-050) | Parse Accept header once per request | implemented | low | S | cpu |
| [beacon_api-051](#beacon_api-051) | Optimistic status from fork choice, not state hash | implemented | low | S | cpu, memory |
| [beacon_api-052](#beacon_api-052) | State root endpoint from stored block state_root | implemented | low | S | cpu, disk, latency |
| [beacon_api-053](#beacon_api-053) | Find last non-missed slot by scanning backwards | n/a | low |  | cpu, disk |
| [beacon_api-054](#beacon_api-054) | Array bodies for attestation and subscription submissions | implemented | low | S | cpu, latency |
| [beacon_api-055](#beacon_api-055) | Batch prepare_beacon_proposer under one lock | implemented | low | S | cpu, latency |
| [beacon_api-056](#beacon_api-056) | Bloom filter for multi-id validator queries | implemented | low | S | cpu |
| [beacon_api-057](#beacon_api-057) | Bound state regeneration for far-out API requests | implemented | low | S | cpu, latency |
| [beacon_api-058](#beacon_api-058) | Advance state only to epoch start for committees | implemented | low | S | cpu, latency |
| [beacon_api-059](#beacon_api-059) | RANDAO endpoint via accelerated shuffling recovery | not | low | M | cpu, disk, latency |
| [beacon_api-060](#beacon_api-060) | Box large async futures on block publish | implemented | low | S | memory, cpu |
| [beacon_api-061](#beacon_api-061) | Build API type definitions once | n/a | low |  | cpu, memory |
| [beacon_api-062](#beacon_api-062) | Precompute node version response | partial | low | S | cpu |
| [beacon_api-063](#beacon_api-063) | Precomputed field-name casing map for JSON | n/a | low |  | cpu |
| [beacon_api-064](#beacon_api-064) | Resolve block id via slot-indexed lookup | implemented | low | S | cpu, disk |
| [beacon_api-065](#beacon_api-065) | Resolve state_id directly via selector | partial | low | S | cpu, disk, latency |
| [beacon_api-066](#beacon_api-066) | Avoid copies when listing pool attestations | partial | low | S | cpu, memory |
| [beacon_api-067](#beacon_api-067) | Cheap API client request path building | n/a | low |  | cpu, memory |
| [beacon_api-068](#beacon_api-068) | Avoid repeated work per committee subscription entry | partial | low | S | cpu |
| [beacon_api-069](#beacon_api-069) | Separate small committee cache for HTTP committees route | implemented | low | S | cpu, memory |
| [beacon_api-070](#beacon_api-070) **★** | Promise cache deduplicating concurrent state requests | partial | medium | M | cpu, memory, latency |
| [beacon_api-071](#beacon_api-071) | Remove redundant storage call in block handler | partial | low | S | disk, latency |
| [beacon_api-072](#beacon_api-072) | Validator monitor caches balances for API queries | implemented | low | S | disk, cpu, latency |
| [beacon_api-073](#beacon_api-073) | Doppelganger check early return skips historical states | n/a | medium |  | cpu, startup |
| [beacon_api-074](#beacon_api-074) | Reject pre-fork requests before generating state | partial | low | S | cpu, latency |
| [beacon_api-075](#beacon_api-075) | Validator activation status check once per epoch | not | low | M | cpu |
| [beacon_api-076](#beacon_api-076) | Fast hex encode/decode in JSON serialization | partial | low | M | cpu |
| [beacon_api-077](#beacon_api-077) | Block rewards API loads state directly, no replay | implemented | low | S | cpu, disk, latency |
| [beacon_api-078](#beacon_api-078) | Fetch blobs from EL on gossip block arrival | implemented | high | M | latency, bandwidth, sync |
| [beacon_api-079](#beacon_api-079) **★** | Query EL first, request only remaining blobs from peers | partial | medium | M | latency, bandwidth |
| [beacon_api-080](#beacon_api-080) **★** | Trigger getBlobs on first gossip column sidecar | partial | medium | S | latency, bandwidth |
| [beacon_api-081](#beacon_api-081) | Call getBlobs before block verification completes | implemented | high | S | latency, bandwidth |
| [beacon_api-082](#beacon_api-082) | Fetch blobs from EL during block lookup sync | partial | low | M | latency, bandwidth |
| [beacon_api-083](#beacon_api-083) | Fetch EL blobs for blocks published via API | implemented | medium | S | latency, bandwidth |
| [beacon_api-084](#beacon_api-084) **★** | Use existence-only EL blob query | not | medium | M | latency, bandwidth |
| [beacon_api-085](#beacon_api-085) | Fill partial column cells from EL blobs | implemented | medium | S | latency, bandwidth |
| [beacon_api-086](#beacon_api-086) | Run blob tracker only for gossip blocks | partial | low | S | cpu, bandwidth |
| [beacon_api-087](#beacon_api-087) | Skip EL reconstruction when nothing is missing | partial | low | S | cpu |
| [beacon_api-088](#beacon_api-088) **★** | Build only custodied columns from EL blobs | partial | medium | S | cpu, memory |
| [beacon_api-089](#beacon_api-089) | Publish recovered columns off the availability path | partial | low | M | latency, bandwidth |
| [beacon_api-090](#beacon_api-090) | Publish only needed recovered columns | implemented | medium | S | cpu, bandwidth |
| [beacon_api-091](#beacon_api-091) **★** | Mark data available at 50% columns | not | medium | M | latency, bandwidth, sync |
| [beacon_api-092](#beacon_api-092) | Reconstruct remaining columns from half | implemented | medium | S | cpu, latency, bandwidth, sync |
| [beacon_api-093](#beacon_api-093) | Delay column reconstruction to wait for gossip | implemented | low | S | cpu, latency, sync |
| [beacon_api-094](#beacon_api-094) | Cap reconstruction debounce delay | not | low | S | cpu, latency |
| [beacon_api-095](#beacon_api-095) | Dynamic reconstruction timeout, none on non-supernodes | implemented | low | S | cpu |
| [beacon_api-096](#beacon_api-096) **★** | Run column reconstruction once per block | partial | medium | M | cpu, memory, disk |
| [beacon_api-097](#beacon_api-097) **★** | Dedicated thread pool for column reconstruction | partial | medium | M | cpu, latency |
| [beacon_api-098](#beacon_api-098) **★** | Run KZG reconstruction off async and fork-choice threads | partial | medium | S | cpu, latency |
| [beacon_api-099](#beacon_api-099) | Bound parallelism of per-blob cell recovery | partial | low | S | cpu, memory |
| [beacon_api-100](#beacon_api-100) | Semi-supernode: custody half the columns | implemented | medium | S | cpu, disk, bandwidth |
| [beacon_api-101](#beacon_api-101) | Custody first half of columns to skip reconstruction | not | low | L | cpu, bandwidth |
| [beacon_api-102](#beacon_api-102) | Background reconstruction of historical custody columns | not | low | M | cpu, disk, bandwidth |
| [beacon_api-103](#beacon_api-103) | Reconstruct API blobs from stored columns | implemented | low | S | cpu, memory |
| [beacon_api-104](#beacon_api-104) | Share blobs and cells by Arc, not copy | implemented | low | S | cpu, memory |
| [beacon_api-105](#beacon_api-105) | Store a blob as one flat byte array | n/a | low |  | memory |
| [beacon_api-106](#beacon_api-106) | Assemble partial columns in-place in ring buffer | partial | low | L | memory, latency, bandwidth |
| [beacon_api-107](#beacon_api-107) | Quarantine blobs and blobless blocks until joined | implemented | medium | S | memory, latency |
| [beacon_api-108](#beacon_api-108) **★** | Cache columns with unknown parent block | not | medium | M | latency, sync |
| [beacon_api-109](#beacon_api-109) | Index sidecar quarantine by root and slot | implemented | low | S | cpu |
| [beacon_api-110](#beacon_api-110) | Cache custody column set per node | implemented | low | S | cpu |
| [beacon_api-111](#beacon_api-111) | Batch KZG verify sidecars from RPC and sync | implemented | medium | S | cpu, latency, sync |
| [beacon_api-112](#beacon_api-112) **★** | Batch gossip column verification per block | partial | medium | M | cpu, latency |
| [beacon_api-113](#beacon_api-113) | Combine by-root sidecar requests per peer | implemented | low | S | bandwidth, sync |
| [beacon_api-114](#beacon_api-114) | Cap columns per by-root request | partial | low | S | bandwidth |
| [beacon_api-115](#beacon_api-115) | Request columns only from custody peers | implemented | medium | S | bandwidth, sync |
| [beacon_api-116](#beacon_api-116) **★** | Hedge slow column requests to alternate peers | not | medium | M | latency, sync |
| [beacon_api-117](#beacon_api-117) | Insert EL-built columns in one batch | implemented | low | S | cpu |
| [beacon_api-118](#beacon_api-118) | Async access to pending sidecar maps | n/a | low |  | latency |
| [beacon_api-119](#beacon_api-119) | Validate blob sidecars without state advancement | implemented | medium | S | cpu, memory, latency |
| [beacon_api-120](#beacon_api-120) | Iterate directly in pending-column availability check | partial | low | S | cpu, memory |
| [beacon_api-121](#beacon_api-121) | Prune blob and column data past DA window | implemented | medium | S | disk |
| [beacon_api-122](#beacon_api-122) | Derive column retention window from chain config | implemented | low | S | disk |
| [beacon_api-123](#beacon_api-123) | Never prune blobs needed at chain tip | implemented | low | S | latency |
| [beacon_api-124](#beacon_api-124) | Cheap filesystem traversal for blob pruning | n/a | medium |  | cpu, disk |
| [beacon_api-125](#beacon_api-125) **★** | Incremental capped low-priority blob pruning | partial | medium | S | cpu, disk, latency |
| [beacon_api-126](#beacon_api-126) | Store blob sidecars in KV database | implemented | low | S | memory, disk |
| [beacon_api-127](#beacon_api-127) | Persist data columns in dedicated disk store | implemented | low | S | disk |
| [beacon_api-128](#beacon_api-128) | In-memory index of stored sidecars | n/a | low |  | disk, startup |
| [beacon_api-129](#beacon_api-129) | Faster column reads from storage | implemented | low | S | cpu, disk |
| [beacon_api-130](#beacon_api-130) | Snapshot sidecar index cache at shutdown | n/a | low |  | startup |
| [beacon_api-131](#beacon_api-131) | Cache gossip-validated sidecars for import | implemented | medium | S | cpu, latency |
| [beacon_api-132](#beacon_api-132) | Drop sidecars for already-imported blocks | partial | low | S | cpu, memory, bandwidth |
| [beacon_api-133](#beacon_api-133) | Bound or fail fast on DA wait | n/a | medium |  | latency, sync |
| [beacon_api-134](#beacon_api-134) | Bounded cache of in-flight sampled blocks | implemented | low | S | memory |
| [beacon_api-135](#beacon_api-135) | Run DA check concurrently with execution verification | implemented | medium | S | latency |
| [beacon_api-136](#beacon_api-136) | Merge pre-import block cache into DA cache | implemented | low | S | memory |
| [beacon_api-137](#beacon_api-137) | Skip duplicate blob arrival notifications | implemented | low | S | cpu |
| [beacon_api-138](#beacon_api-138) | Track received columns to skip duplicate work | implemented | medium | S | cpu, disk, bandwidth |
| [beacon_api-139](#beacon_api-139) | Retry pending block only after reconstruction finishes | n/a | low | S | cpu |
| [beacon_api-140](#beacon_api-140) **★** | Delay RPC fetch of missing sidecars | partial | medium | M | latency, bandwidth, sync |
| [beacon_api-141](#beacon_api-141) **★** | Request missing blobs immediately on block seen | partial | medium | S | latency |
| [beacon_api-142](#beacon_api-142) | Pull late block when blobs arrive first | partial | low | S | latency |
| [beacon_api-143](#beacon_api-143) | Fetch missing blobs immediately for past slots | n/a | low | S | latency, sync |
| [beacon_api-144](#beacon_api-144) **★** | Fetch missing columns within the slot | partial | medium | M | latency |
| [beacon_api-145](#beacon_api-145) | Disable blob tracking after retention passes | n/a | low | S | cpu, memory |
| [beacon_api-146](#beacon_api-146) **★** | Disk-backed blob quarantine | not | medium | M | memory, disk |
| [beacon_api-147](#beacon_api-147) | Memory-only bounded LRU for pending components | implemented | low | S | memory, disk |
| [beacon_api-148](#beacon_api-148) | Remove duplicate store of column sidecars | n/a | low | S | memory |
| [beacon_api-149](#beacon_api-149) | Drop sidecars with out-of-range index | implemented | low | S | cpu, memory |
| [beacon_api-150](#beacon_api-150) | Remove repeated checks from isDataAvailable | n/a | low | S | cpu |
| [beacon_api-151](#beacon_api-151) | Drop stale validator custody registrations | implemented | low | S | memory |
| [beacon_api-152](#beacon_api-152) | Keep DA entries until import completes | implemented | medium | S | cpu, memory, disk, latency, bandwidth, sync |
| [beacon_api-153](#beacon_api-153) | Wait on store events instead of polling | n/a | low | S | cpu, latency |
| [beacon_api-154](#beacon_api-154) | Evict completed column recovery entries | implemented | low | S | cpu, memory |
| [beacon_api-155](#beacon_api-155) | Import only when blob count equals commitments | implemented | low | S | latency |
| [beacon_api-156](#beacon_api-156) | Drop gossip columns outside sampling set | implemented | medium | S | cpu, disk, bandwidth |
| [beacon_api-157](#beacon_api-157) | Correct proposer cache key in blob verification | implemented | medium | S | cpu, latency |
| [beacon_api-158](#beacon_api-158) | Consistent sidecar quarantine accounting | n/a | low |  | cpu, memory, disk |
| [beacon_api-159](#beacon_api-159) | High priority retry for delayed columns | implemented | medium | S | latency |
| [beacon_api-160](beacon_api-2.md#beacon_api-160) | Keep column recovery queue in memory | n/a | low |  | memory, disk, sync |
| [beacon_api-161](beacon_api-2.md#beacon_api-161) | Serve blob by-root fetches from quarantine directly | n/a | low |  | bandwidth, sync |
| [beacon_api-162](beacon_api-2.md#beacon_api-162) | Skip gossip proof checks for EL-supplied blobs | implemented | medium | S | cpu, latency |
| [beacon_api-163](beacon_api-2.md#beacon_api-163) **★** | Cache column inclusion proof results | partial | medium | S | cpu |
| [beacon_api-164](beacon_api-2.md#beacon_api-164) | Late DA check with per-block sampling tracker | implemented | medium | S | disk, latency, bandwidth |
| [beacon_api-165](beacon_api-2.md#beacon_api-165) **★** | Retry getBlobs until block columns are built | partial | medium | S | latency, bandwidth |
| [beacon_api-166](beacon_api-2.md#beacon_api-166) | Dedicated executor queue for DA tasks | n/a | low |  | latency |
| [beacon_api-167](beacon_api-2.md#beacon_api-167) | Per-block-root cache of pending state queues | not | low | M | cpu, latency |
| [beacon_api-168](beacon_api-2.md#beacon_api-168) | Serve history from archived per-epoch data | not | low | L | cpu, disk, latency |
| [beacon_api-169](beacon_api-2.md#beacon_api-169) | Cache or compute shuffling dependent root once | implemented | low | S | cpu, latency |
| [beacon_api-170](beacon_api-2.md#beacon_api-170) | Compact merkle multiproof responses | not | low | M | bandwidth, cpu |
| [beacon_api-171](beacon_api-2.md#beacon_api-171) | Narrow state-field and count endpoints | partial | low | S | bandwidth, cpu, latency |
| [beacon_api-172](beacon_api-2.md#beacon_api-172) | Delete dead computation in API handlers | n/a | low | S | cpu |
| [beacon_api-173](beacon_api-2.md#beacon_api-173) | Do not sign API response bodies | implemented | low | S | cpu |
| [beacon_api-174](beacon_api-2.md#beacon_api-174) | Node-side cache of produced payload envelope | implemented | low | S | latency |
| [beacon_api-175](beacon_api-2.md#beacon_api-175) | Filter inactive validators from builder registrations | implemented | low | S | bandwidth, cpu |
| [beacon_api-176](beacon_api-2.md#beacon_api-176) | Resolve roots from fork choice before database | partial | low | S | disk, latency |
| [beacon_api-177](beacon_api-2.md#beacon_api-177) | Render JSON responses in place into buffer | not | low | M | memory, cpu |
| [beacon_api-178](beacon_api-2.md#beacon_api-178) | Serve REST directly without gRPC proxy layer | n/a | low | S | cpu, latency |
| [beacon_api-179](beacon_api-2.md#beacon_api-179) | Skip blob and column lookups when none can exist | partial | low | S | disk, latency |
| [beacon_api-L000](beacon_api-2.md#beacon_api-L000) | parent root index | n/a | low |  | cpu, latency |
| [beacon_api-L001](beacon_api-2.md#beacon_api-L001) | narrow lock scope, drop caches | n/a | low |  | memory, cpu, latency |
| [beacon_api-L002](beacon_api-2.md#beacon_api-L002) | pre-commit overlay notifications | n/a | low |  | latency |
| [beacon_api-L003](beacon_api-2.md#beacon_api-L003) | pre-sized direct JSON encoding | partial | low | S | cpu, latency, memory |
| [beacon_api-L004](beacon_api-2.md#beacon_api-L004) **★** | publish head before state copy | partial | medium | S | latency |
| [beacon_api-L005](beacon_api-2.md#beacon_api-L005) | serialize lists without copy | not | low | S | memory, cpu |
| [beacon_api-L006](beacon_api-2.md#beacon_api-L006) | time-based skip slot limit | not | low | S | latency |
| [beacon_api-L007](beacon_api-2.md#beacon_api-L007) | remove rayon deadlock | implemented | low | S | latency, cpu |
| [beacon_api-L008](beacon_api-2.md#beacon_api-L008) | server-side validator filter | implemented | low | S | bandwidth, cpu |
| [beacon_api-L009](beacon_api-2.md#beacon_api-L009) | skip proposer cache for future epoch | implemented | low | S | cpu |
| [beacon_api-L010](beacon_api-2.md#beacon_api-L010) **★** | historic committee cache from randao | partial | medium | S | latency, cpu |
| [beacon_api-L011](beacon_api-2.md#beacon_api-L011) | pubkey cache lookup | partial | low | S | cpu, latency |
| [beacon_api-L012](beacon_api-2.md#beacon_api-L012) | server-side status counting | implemented | low | S | cpu, latency |
| [beacon_api-L013](beacon_api-2.md#beacon_api-L013) | single-pass accept parse | implemented | low | S | cpu |
| [beacon_api-L014](beacon_api-2.md#beacon_api-L014) | head root priority and skip block load | implemented | low | S | latency, disk |
| [beacon_api-L015](beacon_api-2.md#beacon_api-L015) | single network channel send | partial | low | S | latency, cpu |
| [beacon_api-L016](beacon_api-2.md#beacon_api-L016) | hashset id filter | implemented | low | S | cpu, latency |
| [beacon_api-L017](beacon_api-2.md#beacon_api-L017) | persist light client bootstrap | implemented | medium | S | cpu, disk |
| [beacon_api-L018](beacon_api-2.md#beacon_api-L018) | single lock acquisition | implemented | low | S | latency |
| [beacon_api-L019](beacon_api-2.md#beacon_api-L019) | raise API request priority | implemented | low | S | latency |
| [beacon_api-L020](beacon_api-2.md#beacon_api-L020) | server-side supply computation | not | low | S | bandwidth, cpu |
| [beacon_api-L021](beacon_api-2.md#beacon_api-L021) | not-while-syncing guard on duties | implemented | medium | S | cpu, sync |
| [beacon_api-L022](beacon_api-2.md#beacon_api-L022) | head root fast path | implemented | low | S | latency |
| [beacon_api-L023](beacon_api-2.md#beacon_api-L023) **★** | skip duties when stalled | not | medium | S | cpu, latency |
| [beacon_api-L024](beacon_api-2.md#beacon_api-L024) **★** | index lookup instead of full scan | not | medium | S | cpu, latency |
| [beacon_api-L025](beacon_api-2.md#beacon_api-L025) | light client updates without state cache | implemented | medium | S | memory |
| [beacon_api-L026](beacon_api-2.md#beacon_api-L026) | zero-copy response body | n/a | low |  | memory, cpu |
| [beacon_api-L027](beacon_api-2.md#beacon_api-L027) | zero-copy state response | n/a | low |  | memory, cpu |
| [beacon_api-L028](beacon_api-2.md#beacon_api-L028) | ssz http wire format | partial | low | M | bandwidth, cpu |
| [beacon_api-L029](beacon_api-2.md#beacon_api-L029) | upgrade HTTP server | n/a | low |  | cpu |
| [beacon_api-L030](beacon_api-2.md#beacon_api-L030) | lightweight validator endpoint | implemented | low | S | cpu, bandwidth |
| [beacon_api-L031](beacon_api-2.md#beacon_api-L031) | serve checkpoint state API | implemented | low | S | sync |
| [beacon_api-L032](beacon_api-2.md#beacon_api-L032) | range read instead of full load | not | low | S | cpu, memory |
| [beacon_api-L033](beacon_api-2.md#beacon_api-L033) | skip preprocessing without listeners | implemented | low | S | cpu, memory |
| [beacon_api-L034](beacon_api-2.md#beacon_api-L034) | skip stale light client updates | partial | low | S | cpu, bandwidth |
| [beacon_api-L035](beacon_api-2.md#beacon_api-L035) | skip redundant DB lookup | implemented | low | S | disk, latency |
| [beacon_api-L036](beacon_api-2.md#beacon_api-L036) | skip redundant DB lookup | implemented | low | S | disk, latency |
| [beacon_api-L037](beacon_api-2.md#beacon_api-L037) | skip redundant DB lookup | implemented | low | S | disk, latency |
| [beacon_api-L038](beacon_api-2.md#beacon_api-L038) | guard old-slot reconstruction | implemented | low | S | cpu, latency |
| [beacon_api-L039](beacon_api-2.md#beacon_api-L039) | guard old-slot reconstruction | implemented | low | S | cpu, latency |
| [beacon_api-L040](beacon_api-2.md#beacon_api-L040) **★** | refuse regen API while syncing | not | medium | S | cpu, latency, sync |
| [beacon_api-L041](beacon_api-2.md#beacon_api-L041) | set instead of array scan | n/a | low | S | cpu |
| [beacon_api-L042](beacon_api-2.md#beacon_api-L042) | pubkey index map | implemented | low | S | cpu, latency |
| [beacon_api-L043](beacon_api-2.md#beacon_api-L043) | share historical state reconstruction | partial | low | M | cpu, latency |
| [beacon_api-L044](beacon_api-2.md#beacon_api-L044) | pubkey-to-index cache | partial | low | S | cpu, latency |
| [beacon_api-L045](beacon_api-2.md#beacon_api-L045) | reuse state across history traversal | implemented | medium | S | cpu, latency |
| [beacon_api-L046](beacon_api-2.md#beacon_api-L046) | stream JSON without temp strings | partial | low | M | cpu, memory, latency |
| [beacon_api-L047](beacon_api-2.md#beacon_api-L047) | recent state root from RAM | implemented | low | S | disk, latency |
| [beacon_api-L048](beacon_api-2.md#beacon_api-L048) | head event on reorg | partial | low | S | latency |
| [beacon_api-L049](beacon_api-2.md#beacon_api-L049) | reuse shuffling for PTC | implemented | low | S | cpu |
| [beacon_api-L050](beacon_api-2.md#beacon_api-L050) | pubkey to index map | partial | low | S | cpu, latency |
| [beacon_api-L051](beacon_api-2.md#beacon_api-L051) | per-slot committee cache for duties | implemented | low | S | cpu, latency |
| [beacon_api-L052](beacon_api-2.md#beacon_api-L052) | hoist per-call lookups | implemented | low | S | cpu, latency |
| [beacon_api-L053](beacon_api-2.md#beacon_api-L053) | use committee cache | implemented | low | S | cpu |
| [beacon_api-L054](beacon_api-2.md#beacon_api-L054) | single pass committee map | implemented | low | S | cpu, latency |
| [beacon_api-L055](beacon_api-2.md#beacon_api-L055) | skip needless slot advance | implemented | medium | S | cpu, latency |
| [beacon_api-L056](beacon_api-2.md#beacon_api-L056) | paginate before compute; custom marshal | n/a | low | S | cpu, memory, latency |
| [beacon_api-L057](beacon_api-2.md#beacon_api-L057) | limit slot advance | implemented | low | S | cpu, latency |
| [beacon_api-L058](beacon_api-2.md#beacon_api-L058) | pre-allocate vectors | implemented | low | S | memory, cpu |
| [beacon_api-L059](beacon_api-2.md#beacon_api-L059) | skip eth1 calls for active validators | n/a | low | S | latency |
| [beacon_api-L060](beacon_api-2.md#beacon_api-L060) | group by block root | n/a | medium |  | cpu, latency |
| [beacon_api-L061](beacon_api-2.md#beacon_api-L061) | remove unused eth1 calls | n/a | low | S | latency |
| [beacon_api-L062](beacon_api-2.md#beacon_api-L062) | use target-root state | n/a | medium |  | cpu, latency |
| [beacon_api-L063](beacon_api-2.md#beacon_api-L063) | read-only validator access | implemented | low | S | memory |
| [beacon_api-L064](beacon_api-2.md#beacon_api-L064) | state regen by target root | implemented | low | S | latency, cpu |
| [beacon_api-L065](beacon_api-2.md#beacon_api-L065) | offset slot ticker for streaming | n/a | low | S | cpu, latency |
| [beacon_api-L066](beacon_api-2.md#beacon_api-L066) | use head state when possible | implemented | low | S | latency, cpu |
| [beacon_api-L067](beacon_api-2.md#beacon_api-L067) | iterate validators without copy | implemented | low | S | cpu, memory |
| [beacon_api-L068](beacon_api-2.md#beacon_api-L068) | short-circuit genesis slot | n/a | low | S | db_hot |
| [beacon_api-L069](beacon_api-2.md#beacon_api-L069) | head getters without state copy | implemented | low | S | cpu, memory |
| [beacon_api-L070](beacon_api-2.md#beacon_api-L070) | fewer state fetches | n/a | low | S | latency, startup |
| [beacon_api-L071](beacon_api-2.md#beacon_api-L071) | skip replay for future slot | implemented | medium | S | cpu, latency |
| [beacon_api-L072](beacon_api-2.md#beacon_api-L072) | root lookup instead of full state | implemented | low | S | memory, cpu, latency |
| [beacon_api-L073](beacon_api-2.md#beacon_api-L073) | skip unchanged DB write | implemented | low | S | disk |
| [beacon_api-L074](beacon_api-2.md#beacon_api-L074) | skip unchanged DB write | n/a | low | S | disk |
| [beacon_api-L075](beacon_api-2.md#beacon_api-L075) | fix SSE library memory leak | n/a | low | S | memory |
| [beacon_api-L076](beacon_api-2.md#beacon_api-L076) | head state with next-slot cache | implemented | medium | S | cpu, latency |
| [beacon_api-L077](beacon_api-2.md#beacon_api-L077) | skip check on cache hit | implemented | low | S | latency, cpu |
| [beacon_api-L078](beacon_api-2.md#beacon_api-L078) **★** | use next slot cache in rewards | partial | medium | S | latency |
| [beacon_api-L079](beacon_api-2.md#beacon_api-L079) | read-only validator views | implemented | low | S | cpu, latency |
| [beacon_api-L080](beacon_api-2.md#beacon_api-L080) | precompute and store updates | implemented | medium | S | cpu, latency |
| [beacon_api-L081](beacon_api-2.md#beacon_api-L081) | precomputed bootstrap in DB | implemented | low | S | cpu, latency |
| [beacon_api-L082](beacon_api-2.md#beacon_api-L082) **★** | gzip HTTP responses | partial | medium | S | bandwidth |
| [beacon_api-L083](beacon_api-2.md#beacon_api-L083) | precompute LC updates | implemented | low | S | cpu |
| [beacon_api-L084](beacon_api-2.md#beacon_api-L084) | serve LC updates from store | implemented | low | S | cpu |
| [beacon_api-L085](beacon_api-2.md#beacon_api-L085) | use cached proposer index | implemented | low | S | cpu, latency |
| [beacon_api-L086](beacon_api-2.md#beacon_api-L086) | reverse index for duties lookup | implemented | low | S | cpu, latency |
| [beacon_api-L087](beacon_api-2.md#beacon_api-L087) | unify resolver lookup paths | n/a | low |  | cpu |
| [beacon_api-L088](beacon_api-2.md#beacon_api-L088) | use lookahead not state advance | implemented | low | S | cpu, latency |
| [beacon_api-L089](beacon_api-2.md#beacon_api-L089) | per-request committee assignment, early exit | implemented | low | S | cpu, memory |
| [beacon_api-L090](beacon_api-2.md#beacon_api-L090) **★** | skip KZG proof computation on blob reconstruct | not | medium | M | cpu, memory, latency |
| [beacon_api-L091](beacon_api-2.md#beacon_api-L091) **★** | lower gzip level | not | medium | S | cpu |
| [beacon_api-L092](beacon_api-2.md#beacon_api-L092) | reject unavailable historical state early | implemented | medium | S | cpu, latency |
| [beacon_api-L093](beacon_api-2.md#beacon_api-L093) | per-slot cache plus singleflight | n/a | low |  | cpu, latency |
| [beacon_api-L094](beacon_api-2.md#beacon_api-L094) | lazy filtered validator iteration | implemented | low | S | memory, cpu, latency |
| [beacon_api-L095](beacon_api-2.md#beacon_api-L095) | read-only state in duties | implemented | low | S | cpu, memory |
| [beacon_api-L096](beacon_api-2.md#beacon_api-L096) | linear-time incremental head parsing | n/a | low | S | cpu, memory |
| [beacon_api-L097](beacon_api-2.md#beacon_api-L097) | single storage read per request | partial | low | S | cpu |
| [beacon_api-L098](beacon_api-2.md#beacon_api-L098) | separate event delivery pool | n/a | low | S | latency |
| [beacon_api-L099](beacon_api-2.md#beacon_api-L099) | suppress empty-slot head events | implemented | low | S | cpu, bandwidth |
| [beacon_api-L100](beacon_api-2.md#beacon_api-L100) | slim block event payload | implemented | low | S | bandwidth, cpu |
| [beacon_api-L101](beacon_api-2.md#beacon_api-L101) | lazy event serialization | implemented | low | S | cpu, memory |
| [beacon_api-L102](beacon_api-2.md#beacon_api-L102) | multithreaded validator API | n/a | low | S | latency, cpu |
| [beacon_api-L103](beacon_api-2.md#beacon_api-L103) | shared serialized event bytes | not | low | S | memory, cpu |
| [beacon_api-L104](beacon_api-2.md#beacon_api-L104) **★** | stream JSON response | not | medium | M | memory |
| [beacon_api-L105](beacon_api-2.md#beacon_api-L105) **★** | stream SSZ response | not | medium | M | memory |
| [beacon_api-L106](beacon_api-2.md#beacon_api-L106) | reject future-slot state lookup | implemented | low | S | cpu, latency |
| [beacon_api-L107](beacon_api-2.md#beacon_api-L107) | stop keepalive on closed SSE client | n/a | low | S | cpu |
| [beacon_api-L108](beacon_api-2.md#beacon_api-L108) | threads by cores | n/a | low | S | cpu |
| [beacon_api-L109](beacon_api-2.md#beacon_api-L109) **★** | gzip REST responses | not | medium | S | bandwidth |
| [beacon_api-L110](beacon_api-2.md#beacon_api-L110) | head state for duties | implemented | low | S | cpu, latency |
| [beacon_api-L111](beacon_api-2.md#beacon_api-L111) | root lookup without full load | partial | low | S | cpu, disk, latency |
| [beacon_api-L112](beacon_api-2.md#beacon_api-L112) | header-based deserializer choice | implemented | low | S | cpu, latency |
| [beacon_api-L113](beacon_api-2.md#beacon_api-L113) | primitive map, single-pass duties | n/a | low | S | cpu, latency |
| [beacon_api-L114](beacon_api-2.md#beacon_api-L114) | primitive int-keyed map for duties | n/a | low | S | cpu, latency |
| [beacon_api-L115](beacon_api-2.md#beacon_api-L115) **★** | on-demand sidecar fetch for blobs | not | medium | L | bandwidth, disk |
| [beacon_api-L116](beacon_api-2.md#beacon_api-L116) | persist light client updates | implemented | low | S | startup |
| [beacon_api-L117](beacon_api-2.md#beacon_api-L117) | persist precomputed bootstraps | implemented | low | S | cpu, disk, latency |
| [beacon_api-L118](beacon_api-2.md#beacon_api-L118) | hashset id filter, lazy status | partial | low | S | cpu, latency |
| [beacon_api-L119](beacon_api-2.md#beacon_api-L119) | serialize state lists without copying | implemented | low | S | cpu, memory |
| [beacon_api-L120](beacon_api-2.md#beacon_api-L120) | pubkey index map lookup | implemented | low | S | cpu, latency |
| [beacon_api-L121](beacon_api-2.md#beacon_api-L121) | remove listener on close | n/a | low | S | memory |
| [beacon_api-L122](beacon_api-2.md#beacon_api-L122) | parallel db lookups in API | n/a | low | S | latency |
| [beacon_api-L123](beacon_api-2.md#beacon_api-L123) | remove wait before publish | implemented | low | S | latency |
| [beacon_api-L124](beacon_api-2.md#beacon_api-L124) | read balance by index | partial | low | S | memory, cpu |
| [beacon_api-L125](beacon_api-2.md#beacon_api-L125) | single-entry attestation data cache | partial | low | S | cpu, latency |

★ actionable. Click an id for the full record.

## Ideas

<a id="beacon_api-001"></a>
<details>
<summary><b>beacon_api-001</b> Serve duty queries from epoch caches, not loaded states — <i>partial · low · S · cpu, memory, latency</i></summary>

**Idea.** Answer attester/committee duty and related validator queries for the previous, current and next epoch from the head state's committee/epoch caches (or preloaded head data) instead of loading a state from the DB or advancing a full state per request. This turns each duty request into cache lookups and keeps request floods from triggering state loads.

**Gap in Lighthouse.** Previous-epoch attester and proposer duty requests (request_epoch == current_epoch-1 with an up-to-date head) do not use the head state's previous-epoch committee cache or the shuffling cache. compute_historic_attester_duties and compute_historic_proposer_duties load a state from the store with StateId::from_slot for every request. The fix: serve previous epoch from the head's RelativeEpoch::Previous committee cache, or the shuffling cache keyed by the previous shuffling id.

**Impact.** Current and next epoch duty requests (the VC hot path) are cache lookups. A flood of previous-epoch duty requests still triggers one state load per request. Rare in practice.

**Best measured result.** memory required 4 GB -&gt; 10 GB, API consistently performant (pr:caplin#9457)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/attester_duties.rs:45-57`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L45-L57) current/next epoch go to cached_attestation_duties; anything older goes to compute_historic_attester_duties
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1735-1764`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1735-L1764) validator_attestation_duties uses with_committee_cache (shuffling cache)
- [`beacon_node/http_api/src/attester_duties.rs:83-127`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L83-L127) previous epoch: head state used only if head.current_epoch() &lt;= request_epoch, otherwise StateId::from_slot(...).state(chain) loads a state
- [`beacon_node/http_api/src/proposer_duties.rs:81-124`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/proposer_duties.rs#L81-L124),229-270 proposer duties: current from beacon_proposer_cache, next from compute_proposer_duties_from_head, previous via compute_historic_proposer_duties state load
- [`beacon_node/http_api/src/beacon/states.rs:611-680`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L611-L680) committees endpoint uses historical_committee_cache

**Skeptic check.** The earlier evidence is right for current and next epoch, the paths a VC uses. The idea also names the previous epoch, and Lighthouse serves that through a DB state load in compute_historic_attester_duties and compute_historic_proposer_duties.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [caplin#9457](https://github.com/erigontech/erigon/pull/9457), [nimbus@678a7efaa](https://github.com/status-im/nimbus-eth2/commit/678a7efaaa8c), [nimbus#1536](https://github.com/status-im/nimbus-eth2/pull/1536), [lighthouse#636](https://github.com/sigp/lighthouse/pull/636), [prysm#16136](https://github.com/OffchainLabs/prysm/pull/16136), [ethlambda#663](https://github.com/lambdaclass/ethlambda/pull/663)

</details>


<a id="beacon_api-002"></a>
<details>
<summary><b>beacon_api-002</b> Read sync committee duties from head state — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** For sync committee duties within the current or next sync period, read current_sync_committee/next_sync_committee from the head state instead of loading or replaying a state to the period start, because those fields are constant within a period.

**Impact.** Already done. Requests for the current and next sync period are answered from the head state's sync committee fields.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/sync_committees.rs:44-56`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/sync_committees.rs#L44-L56) sync_committee_duties_from_head tried first
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3032-3042`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3032-L3042) sync_committee_duties_from_head reads head.beacon_state
- [`consensus/types/src/state/beacon_state.rs:1731-1750`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1731-L1750) get_built_sync_committee returns current_sync_committee/next_sync_committee for current/next period
- [`beacon_node/http_api/src/sync_committees.rs:76-130`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/sync_committees.rs#L76-L130) duties_from_state_load only on SyncCommitteeNotKnown/IncorrectStateVariant

**Skeptic check.** Verified that the head path covers both the current and the next period through get_built_sync_committee. The state load runs only for older periods or a pre-Altair head. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#16688](https://github.com/OffchainLabs/prysm/pull/16688), [grandine@5b9bf12ab](https://github.com/grandinetech/grandine/commit/5b9bf12ab2f5), [grandine#264](https://github.com/grandinetech/grandine/pull/264), [lighthouse#5174](https://github.com/sigp/lighthouse/pull/5174)

</details>


<a id="beacon_api-003"></a>
<details>
<summary><b>beacon_api-003</b> Cache validator-to-sync-committee positions per period — <i>not · low · S · cpu, latency</i></summary>

**Idea.** Keep a validator-index to sync-committee-positions map for both the current and next sync period in the epoch context, rotating next into current at the period boundary, so sync duty requests are map lookups instead of scans of the committee pubkeys.

**Gap in Lighthouse.** Add a validator-index to positions map per sync period cached on the chain; use it in get_sync_committee_duties.

**Impact.** Sync duty requests become map lookups; saving only matters for nodes with many validators, negligible CPU.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:1855`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1855) get_sync_committee_duties: per-validator SyncDuty::from_sync_committee scans committee pubkeys
- [`beacon_node/http_api/src/sync_committees.rs:44`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/sync_committees.rs#L44) duties from head, no position map

**Sources.** [lodestar@e796e12f9](https://github.com/ChainSafe/lodestar/commit/e796e12f945c)

</details>


<a id="beacon_api-004"></a>
<details>
<summary><b>beacon_api-004</b> Serve proposer duties from a decision-root-keyed proposer cache — <i>partial · low · S · cpu, latency</i></summary>

**Idea.** Serve proposer duties (including next-epoch duties post-Fulu) from a shared proposer cache keyed by the shuffling decision root and primed ahead of time, and reuse cached attester shufflings, so concurrent or retried duty requests do not re-advance the head state. Use compressed pubkey bytes in duty responses so cloning and hashing are cheap.

**Gap in Lighthouse.** Next-epoch proposer duties (request_epoch == current+1) are recomputed from the head state on every request and never cached; make that branch in proposer_duties_internal look up/insert beacon_proposer_cache keyed by the next-epoch decision root (and prime it in state_advance_timer).

**Impact.** Repeated or retried next-epoch proposer duty calls (post-Fulu VCs poll this) stop advancing the head state; minor, a few ms per call.

**Best measured result.** Pyrmont: proposer duties 450ms peaks to &lt;1ms; attester duties &gt;1s to 20-30ms (pr:lighthouse#2243)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/proposer_duties.rs:135`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/proposer_duties.rs#L135) cache lookup keyed by decision root
- [`beacon_node/http_api/src/proposer_duties.rs:198`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/proposer_duties.rs#L198) compute_and_cache primes cache
- [`beacon_node/http_api/src/proposer_duties.rs:314`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/proposer_duties.rs#L314) pubkey bytes via validator_pubkey_bytes_many
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1735`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1735) attester duties via shuffling cache (with_committee_cache)
- [`beacon_node/http_api/src/proposer_duties.rs:73`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/proposer_duties.rs#L73) next-epoch branch calls compute_proposer_duties_from_head, no cache read/insert

**Sources.** [lighthouse#2243](https://github.com/sigp/lighthouse/pull/2243), [lighthouse#10459](https://github.com/sigp/lighthouse/pull/10459), [caplin#8777](https://github.com/erigontech/erigon/pull/8777)

</details>


<a id="beacon_api-005"></a>
<details>
<summary><b>beacon_api-005</b> Compute duties for all validators in one committee pass — <i>partial · medium · S · cpu, latency</i></summary>

**Idea.** When a duties request names many validators, iterate the target epoch's committees once while looking up members in a validator-index set or map, instead of searching the committees separately for each validator. This turns O(validators x committees) work into a single pass.

**Gap in Lighthouse.** Shuffling/cache lookup is already shared for the batch and the member lookup is O(1), but finding the committee still scans up to epoch_committee_count ranges per validator (O(V x C) integer arithmetic). Replace the loop with direct computation (i*count/len, adjust by one) or a binary search over the monotonic ranges.

**Impact.** Small: saves up to ~2048 cheap range computations per requested validator; only noticeable for VCs with many thousands of keys.

**Best measured result.** 3.35s to 1.29-1.65s per batch (about 2-2.6x) (pr:lodestar#2717)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/attester_duties.rs:61-69`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L61-L69) cached path calls chain.validator_attestation_duties for the whole index batch
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1747-1758`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1747-L1758) one with_committee_cache lookup for the batch, then per-validator committee_cache.get_attestation_duties
- [`consensus/types/src/state/committee_cache.rs:392-397`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L392-L397) shuffled_position is an O(1) array lookup (no per-validator committee materialisation)
- [`consensus/types/src/state/committee_cache.rs:302-323`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L302-L323) linear loop over 0..epoch_committee_count per validator
- [`consensus/types/src/state/committee_cache.rs:420-433`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L420-L433) committee ranges are floor(len*i/count), so the index is directly computable

**Second check.** Checked both http_api duty paths (cached and state fallback at attester_duties.rs:157 via BeaconState::get_attestation_duties) and compute_committee_range_in_epoch; no direct-index or single-pass variant exists. Lighthouse already avoids the expensive part of the Lodestar fix (per-validator committee search over materialised lists) via shuffling_positions.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [lodestar#2717](https://github.com/ChainSafe/lodestar/pull/2717), [prysm#4416](https://github.com/OffchainLabs/prysm/pull/4416), [lodestar#2698](https://github.com/ChainSafe/lodestar/pull/2698)

</details>


<a id="beacon_api-006"></a>
<details>
<summary><b>beacon_api-006</b> Return assignments only for requested validators — <i>partial · low · S · memory, cpu</i></summary>

**Idea.** In duty and assignment queries, build committee assignments only for the requested validator indices (and compute proposers separately) instead of building a map over every active validator, avoiding a large per-request allocation.

**Gap in Lighthouse.** Main paths already compute per requested index with no all-validator map. Committee-assignment style endpoints are not index-filtered at build time, but no all-validator map exists, so little is left to fix.

**Impact.** Negligible; no per-request O(N_validators) allocation seen in duty paths.

**Best measured result.** over 32 MB heap with 1M validators (pr:prysm#14039)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:1752`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1752) attester duties computed only for requested indices from committee cache
- [`beacon_node/http_api/src/proposer_duties.rs:230`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/proposer_duties.rs#L230) proposers computed separately
- [`beacon_node/http_api/src/attester_duties.rs:143`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L143) historic path builds committee cache and queries per index

**Sources.** [prysm#14039](https://github.com/OffchainLabs/prysm/pull/14039)

</details>


<a id="beacon_api-007"></a>
<details>
<summary><b>beacon_api-007</b> Run HTTP API through bounded priority work scheduler — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Route HTTP API requests through the same bounded, prioritised work scheduler as p2p work (beacon processor) instead of spawning an unbounded task per request, with block publish and validator-critical endpoints at the highest priority and excess requests dropped. Avoid router filters that backtrack across routes. This stops API load from starving block import and keeps block publication from queueing behind other API work.

**Impact.** API work goes through bounded, prioritised beacon processor queues; block publish at P0.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/task_spawner.rs:11-30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/task_spawner.rs#L11-L30) Priority P0/P1 mapped to Work::ApiRequestP0/P1
- [`beacon_node/http_api/src/task_spawner.rs:48-160`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/task_spawner.rs#L48-L160) blocking and async tasks sent with try_send to the beacon processor
- [`beacon_node/beacon_processor/src/lib.rs:956`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L956) api_request_p0_queue popped early in priority order
- [`beacon_node/beacon_processor/src/lib.rs:1153`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1153) api_request_p1_queue popped late
- [`beacon_node/beacon_processor/src/lib.rs:1436-1440`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1436-L1440) bounded queue push

**Skeptic check.** Verified the TaskSpawner routes requests to bounded ApiRequestP0/P1 queues (63 P0 and 72 P1 call sites); the only direct tokio spawns are inside handlers (builder futures), not per-request bypasses. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#4595](https://github.com/sigp/lighthouse/pull/4595), [lighthouse#4462](https://github.com/sigp/lighthouse/pull/4462)

</details>


<a id="beacon_api-008"></a>
<details>
<summary><b>beacon_api-008</b> Run heavy API handlers on blocking thread pool — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Run CPU-heavy HTTP handlers (state work, signature decompression in validator registrations) on a blocking thread pool instead of the async executor, and skip needless message passing to other services, so they do not stall other async tasks.

**Impact.** Already done. Handlers that work on the state run on blocking workers. The registration path does no signature decompression, so the grandine change has no Lighthouse equivalent to make.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/task_spawner.rs:48-82`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/task_spawner.rs#L48-L82) blocking_task sends handler to BeaconProcessor blocking workers (or tokio blocking pool)
- [`beacon_node/http_api/src/task_spawner.rs:97-104`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/task_spawner.rs#L97-L104) blocking_json_task
- [`beacon_node/http_api/src/beacon/states.rs:835-1000`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L835-L1000) validators/balances/identities handlers use blocking_json_task/blocking_response_task
- [`beacon_node/http_api/src/validator/mod.rs:694-800`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L694-L800) register_validator: no signature decompression in the BN (registrations are forwarded to the builder), builder wait spawned off the processor

**Skeptic check.** Verified the TaskSpawner mechanism and its use on the state and validator endpoints. register_validator runs as an async processor task but does only cheap pubkey-cache lookups and no BLS decompression, so nothing CPU-heavy runs on the executor there.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#1518](https://github.com/sigp/lighthouse/pull/1518), [grandine#467](https://github.com/grandinetech/grandine/pull/467), [grandine@54b8cd815](https://github.com/grandinetech/grandine/commit/54b8cd8158ad)

</details>


<a id="beacon_api-009"></a>
<details>
<summary><b>beacon_api-009</b> Bounded virtual-thread pool for REST and SSE — <i>n/a · low · S · cpu, memory, latency</i></summary>

**Idea.** Dispatch REST request handling to a semaphore-bounded pool of lightweight (virtual) threads while acceptors stay on platform threads, so many long-lived SSE connections do not each pin an OS thread, and the bound caps concurrent large state serialisations.

**Impact.** JVM virtual threads only; Lighthouse uses async tokio plus bounded processor queues.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/task_spawner.rs:1`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/task_spawner.rs#L1) uses tokio tasks and BeaconProcessor, no OS-thread-per-connection

**Sources.** [teku#10430](https://github.com/Consensys-Incorporated/teku/pull/10430), [teku#10495](https://github.com/Consensys-Incorporated/teku/pull/10495)

</details>


<a id="beacon_api-010"></a>
<details>
<summary><b>beacon_api-010</b> HTTP cache headers for immutable REST responses — <i>not · low · S · cpu, bandwidth</i></summary>

**Idea.** Add HTTP cache headers (Cache-Control/ETag) to REST responses for immutable data such as finalized state roots and finalized committees, so clients and proxies reuse responses instead of re-querying the node.

**Gap in Lighthouse.** Add Cache-Control: public, immutable on responses when finalized==true (e.g. state root, committees, finalized blocks) in the beacon routes using execution_optimistic_finalized_beacon_response.

**Impact.** Helps only repeated external queries via proxies; no gain for typical node.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs:3490`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L3490) only Cache-Control no-cache for SSE; grep for ETag/Cache-Control finds nothing else

**Sources.** [teku#1337](https://github.com/Consensys-Incorporated/teku/pull/1337)

</details>


<a id="beacon_api-011"></a>
<details>
<summary><b>beacon_api-011</b> POST variant of validators and balances queries — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Offer POST variants of the state validators and validator_balances endpoints that take the id list in the body, so clients fetch large validator subsets in one request instead of many per-validator GETs (each loading a state) or hitting URL length limits.

**Impact.** Already done.

**Best measured result.** qualitative: thousands of times slower with individual queries (pr:lighthouse#4872)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/beacon/states.rs:835-866`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L835-L866) post_beacon_state_validators takes ids from body, blocking_json_task
- [`beacon_node/http_api/src/beacon/states.rs:979-1000`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L979-L1000) post_beacon_state_validator_balances with body ids
- [`beacon_node/http_api/src/beacon/states.rs:931-960`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L931-L960) post_beacon_state_validator_identities

**Skeptic check.** The POST variants exist, read the id list from the request body, and load the state once per request. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#4872](https://github.com/sigp/lighthouse/pull/4872), [lodestar#6655](https://github.com/ChainSafe/lodestar/pull/6655)

</details>


<a id="beacon_api-012"></a>
<details>
<summary><b>beacon_api-012</b> SSZ responses for validators and balances endpoints — <i>partial · low · S · cpu, bandwidth, latency</i></summary>

**Idea.** Serve the state validators and validator_balances endpoints as SSZ (application/octet-stream) when the Accept header asks for it, avoiding JSON encoding cost and the large JSON response for big validator sets.

**Gap in Lighthouse.** Add Accept: application/octet-stream handling to post_beacon_state_validators and get_beacon_state_validators (ValidatorData SSZ-encode list), as done for balances.

**Impact.** Large /validators responses (whole set, ~1M entries) avoid JSON encode; saves hundreds of ms CPU and several x payload for tools that fetch all validators, rare on a node.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/beacon/states.rs:979`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L979),1020 validator_balances GET/POST honour Accept ssz
- [`beacon_node/http_api/src/beacon/states.rs:835`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L835),896 validators GET/POST take no Accept header, JSON only
- [`beacon_node/http_api/src/beacon/states.rs:931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L931) validator_identities has an ssz variant

**Sources.** [grandine@5e3bd3388](https://github.com/grandinetech/grandine/commit/5e3bd3388980), [grandine#801](https://github.com/grandinetech/grandine/pull/801), [lodestar#6060](https://github.com/ChainSafe/lodestar/pull/6060), [prysm#17077](https://github.com/OffchainLabs/prysm/pull/17077), [lighthouse#10082](https://github.com/sigp/lighthouse/pull/10082)

</details>


<a id="beacon_api-013"></a>
<details>
<summary><b>beacon_api-013</b> SSZ responses for get-block endpoints — <i>implemented · low · S · cpu, bandwidth</i></summary>

**Idea.** Serve blocks from the get-block HTTP endpoints as raw SSZ when the Accept header requests octet-stream, instead of JSON, giving smaller responses and no JSON serialisation.

**Impact.** Full and blinded block endpoints serve SSZ.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs:1211-1213`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L1211-L1213) get_beacon_block returns block.as_ssz_bytes() on Accept ssz
- [`beacon_node/http_api/src/lib.rs:1347-1349`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L1347-L1349) blinded block SSZ
- [`common/eth2/src/lib.rs:1879-1902`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2/src/lib.rs#L1879-L1902) get_beacon_blocks_ssz / get_beacon_blinded_blocks_ssz clients

**Skeptic check.** Verified both block endpoints return SSZ on Accept octet-stream and the eth2 client has SSZ getters. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#4046](https://github.com/Consensys-Incorporated/teku/pull/4046), [lighthouse#2209](https://github.com/sigp/lighthouse/pull/2209)

</details>


<a id="beacon_api-014"></a>
<details>
<summary><b>beacon_api-014</b> Serve SSZ blocks straight from stored bytes — <i>partial · low · M · cpu, memory</i></summary>

**Idea.** For SSZ block requests, return the SSZ bytes as stored in the database instead of decoding the block and re-encoding it, removing a decode/encode round trip per request.

**Gap in Lighthouse.** For Accept ssz on full blocks, fetch raw stored bytes from the hot/cold DB (store get_block_bytes variant) and return them, skipping decode/encode; needs a path in BlockId and store.

**Impact.** Saves a decode plus encode per block SSZ request; small CPU, only matters for heavy block-serving or checkpoint-sync servers.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs:1200`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L1200) block_id.full_block decodes block then :1213 as_ssz_bytes re-encodes
- [`beacon_node/http_api/src/block_id.rs:151`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L151) blinded_block_by_root etc. all return decoded types

**Sources.** [nimbus#3472](https://github.com/status-im/nimbus-eth2/pull/3472)

</details>


<a id="beacon_api-015"></a>
<details>
<summary><b>beacon_api-015</b> SSZ for block production endpoints — <i>implemented · low · S · cpu, bandwidth, latency</i></summary>

**Idea.** Support SSZ responses for the produce-block endpoints (full and blinded) and have the validator client request SSZ by default with JSON fallback, so large blocks skip JSON encoding and decoding on both sides.

**Impact.** Already done.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/produce_block.rs:225-233`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/produce_block.rs#L225-L233) v3/v4 Accept::Ssz returns as_ssz_bytes
- [`beacon_node/http_api/src/produce_block.rs:284-287`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/produce_block.rs#L284-L287),387-390 v2 and blinded SSZ
- [`validator_client/validator_services/src/block_service.rs:714`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/block_service.rs#L714) Gloas path uses post_validator_blocks_v4_ssz with JSON fallback at 729-765
- [`validator_client/validator_services/src/block_service.rs:794-806`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/block_service.rs#L794-L806) pre-Gloas uses get_validator_blocks_v3_ssz with JSON fallback
- [`validator_client/validator_services/src/block_service.rs:960`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/block_service.rs#L960) payload envelopes fetched as SSZ

**Skeptic check.** The BN serves SSZ for every produce endpoint. The VC requests SSZ first and falls back to JSON on both the pre-Gloas (v3) and the Gloas (v4) paths, and also for payload envelopes.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#15390](https://github.com/OffchainLabs/prysm/pull/15390), [prysm#10697](https://github.com/OffchainLabs/prysm/pull/10697), [lighthouse#4534](https://github.com/sigp/lighthouse/pull/4534), [teku#5374](https://github.com/Consensys-Incorporated/teku/pull/5374), [teku#5402](https://github.com/Consensys-Incorporated/teku/pull/5402)

</details>


<a id="beacon_api-016"></a>
<details>
<summary><b>beacon_api-016</b> SSZ responses for beacon state endpoints — <i>implemented · low · S · cpu, memory, bandwidth</i></summary>

**Idea.** Return beacon states from the debug state endpoint (and other large state endpoints) as SSZ when Accept is application/octet-stream, avoiding very large JSON encoding of the state.

**Impact.** Debug state and other state endpoints serve SSZ.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs:2170-2180`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L2170-L2180) debug state endpoint returns state.as_ssz_bytes() on Accept ssz
- [`beacon_node/http_api/src/beacon/states.rs:67-1046`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L67-L1046) many state sub-endpoints also return SSZ
- [`common/eth2/src/lib.rs:2772-2781`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2/src/lib.rs#L2772-L2781) get_debug_beacon_states_ssz

**Skeptic check.** Verified SSZ encoding of the full state on the debug endpoint and SSZ branches on the state sub-endpoints. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#2851](https://github.com/status-im/nimbus-eth2/pull/2851), [lighthouse#2111](https://github.com/sigp/lighthouse/pull/2111), [ethlambda#59](https://github.com/lambdaclass/ethlambda/pull/59), [lodestar#2987](https://github.com/ChainSafe/lodestar/pull/2987)

</details>


<a id="beacon_api-017"></a>
<details>
<summary><b>beacon_api-017</b> SSZ for attestation data and aggregate endpoints — <i>partial · low · S · cpu, bandwidth, latency</i></summary>

**Idea.** Support SSZ responses for the attestation_data and aggregate_attestation endpoints, so validator clients avoid JSON encode/decode on these per-slot calls.

**Gap in Lighthouse.** The beacon node serves SSZ for both endpoints, but the Lighthouse VC attestation_service still calls the JSON get_validator_attestation_data and get_validator_aggregate_attestation_v2/v1 instead of the existing *_ssz client methods, so an LH BN + LH VC pair still JSON-encodes and decodes these per-slot calls.

**Impact.** Small CPU and latency saving per slot on the VC and BN; payloads are small.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/validator/mod.rs:294-302`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L294-L302) attestation_data returns as_ssz_bytes on Accept ssz
- [`beacon_node/http_api/src/aggregate_attestation.rs:53-60`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/aggregate_attestation.rs#L53-L60) aggregate returns SSZ on Accept ssz
- [`common/eth2/src/lib.rs:3794-3816`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2/src/lib.rs#L3794-L3816) get_validator_attestation_data_ssz exists
- [`common/eth2/src/lib.rs:3976-3997`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2/src/lib.rs#L3976-L3997) get_validator_aggregate_attestation_v2_ssz exists
- [`validator_client/validator_services/src/attestation_service.rs:284`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L284),332 calls JSON get_validator_attestation_data
- [`validator_client/validator_services/src/attestation_service.rs:667`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L667),680 calls JSON get_validator_aggregate_attestation_v2/_v1

**Skeptic check.** Server side is done as the earlier evidence said, but the idea's goal (VCs avoid JSON on these calls) is not met by Lighthouse's own VC, which uses the JSON methods.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [prysm#15377](https://github.com/OffchainLabs/prysm/pull/15377), [grandine@01691d190](https://github.com/grandinetech/grandine/commit/01691d190934)

</details>


<a id="beacon_api-018"></a>
<details>
<summary><b>beacon_api-018</b> Accept SSZ bodies when publishing blocks — <i>implemented · low · S · cpu, bandwidth, latency</i></summary>

**Idea.** Accept SSZ request bodies (Content-Type octet-stream) on the publish block and publish blinded block endpoints, avoiding JSON parsing of large blocks and shrinking the request.

**Impact.** Already done. The BN accepts SSZ bodies and the VC publishes with them.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs:895`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L895) post_beacon_blocks_ssz
- [`beacon_node/http_api/src/lib.rs:977`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L977) post_beacon_blocks_v2_ssz
- [`beacon_node/http_api/src/lib.rs:1052`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L1052),1127 blinded v1/v2 SSZ
- [`beacon_node/http_api/src/lib.rs:3635-3640`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L3635-L3640) octet-stream routes
- [`validator_client/validator_services/src/block_service.rs:1110`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/block_service.rs#L1110),1124 VC publishes via post_beacon_blocks_v2_ssz / post_beacon_blinded_blocks_v2_ssz

**Skeptic check.** Verified that the octet-stream routes exist for full and blinded blocks, v1 and v2, and that the VC uses the SSZ publish calls.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#4504](https://github.com/sigp/lighthouse/pull/4504), [lighthouse#4479](https://github.com/sigp/lighthouse/pull/4479), [prysm#10663](https://github.com/OffchainLabs/prysm/pull/10663)

</details>


<a id="beacon_api-019"></a>
<details>
<summary><b>beacon_api-019</b> Accept SSZ bodies on attestation pool submission — <i>not · medium · S · cpu, bandwidth</i></summary>

**Idea.** Accept SSZ request bodies on the submit pool attestations endpoint, avoiding JSON decode cost for large attestation batches.

**Gap in Lighthouse.** Add post_beacon_pool_attestations_v2_ssz mirroring post_beacon_pool_payload_attestations_ssz (fixed-size SingleAttestation chunks, from_ssz_bytes) inside the octet-stream route group, plus an eth2 client SSZ method used by the VC attestation service with JSON fallback.

**Impact.** Saves JSON decode of the per-slot attestation batch on BNs serving large VCs; tens of ms per slot at most for thousands of keys, negligible for small setups.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/beacon/pool.rs:545`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/pool.rs#L545) post_beacon_pool_attestations_v2 decodes Vec&lt;SingleAttestation&gt; via warp_utils::json::json only
- [`beacon_node/http_api/src/lib.rs:3633-3646`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L3633-L3646) octet-stream route group lists post_beacon_pool_payload_attestations_ssz but no attestation SSZ route
- [`common/eth2/src/lib.rs:1971-1993`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2/src/lib.rs#L1971-L1993) VC client post_beacon_pool_attestations_v2 sends JSON (post_with_timeout_and_consensus_header)
- [`beacon_node/http_api/src/beacon/pool.rs:648-680`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/pool.rs#L648-L680) template: SSZ handler exists for PayloadAttestationMessage (chunked from_ssz_bytes)

**Verdict history.** not (checked) → not (refuted)

**Sources.** [prysm#15422](https://github.com/OffchainLabs/prysm/pull/15422), [prysm#15429](https://github.com/OffchainLabs/prysm/pull/15429), [grandine#216](https://github.com/grandinetech/grandine/pull/216), [prysm#17318](https://github.com/OffchainLabs/prysm/pull/17318), [prysm#17234](https://github.com/OffchainLabs/prysm/pull/17234)

</details>


<a id="beacon_api-020"></a>
<details>
<summary><b>beacon_api-020</b> Accept SSZ bodies on register_validator — <i>not · low · S · cpu, bandwidth</i></summary>

**Idea.** Accept SSZ-encoded bodies on the register_validator endpoint, avoiding JSON parsing of large validator registration lists.

**Gap in Lighthouse.** Add an SSZ route for register_validator (Vec&lt;SignedValidatorRegistrationData&gt;) and have preparation_service post SSZ with JSON fallback.

**Impact.** Registration is sent about once per epoch; saves a few ms of JSON parsing for large key sets only.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/validator/mod.rs:694-709`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L694-L709) post_validator_register_validator uses warp_utils::json::json()
- [`validator_client/validator_services/src/preparation_service.rs:453`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/preparation_service.rs#L453) VC posts JSON batches

**Sources.** [nimbus#6943](https://github.com/status-im/nimbus-eth2/pull/6943)

</details>


<a id="beacon_api-021"></a>
<details>
<summary><b>beacon_api-021</b> Request builder API responses as SSZ — <i>implemented · medium · S · cpu, bandwidth, latency</i></summary>

**Idea.** In the builder/MEV-relay client, prefer SSZ in the Accept header (and send SSZ) instead of JSON, avoiding JSON encode/decode and size for headers and payloads.

**Impact.** Already done for headers, bids and block submission, which are the large and latency-critical calls. Validator registrations are still sent as JSON, but they are not latency-critical.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/builder_client/src/lib.rs:23`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/builder_client/src/lib.rs#L23) PREFERENCE_ACCEPT_VALUE = octet-stream q=1.0, json q=0.9
- [`beacon_node/builder_client/src/pre_gloas_builder_http_client.rs:361-405`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/builder_client/src/pre_gloas_builder_http_client.rs#L361-L405) get_builder_header sends SSZ-preferring Accept unless disable_ssz, decodes SSZ by content-type (110-135)
- [`beacon_node/builder_client/src/pre_gloas_builder_http_client.rs:263-310`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/builder_client/src/pre_gloas_builder_http_client.rs#L263-L310) post_builder_blinded_blocks_v2_ssz sends SSZ body when ssz_available
- [`beacon_node/builder_client/src/builder_http_client.rs:115-118`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/builder_client/src/builder_http_client.rs#L115-L118),305 Gloas client same policy for bids and block submission
- [`beacon_node/builder_client/src/pre_gloas_builder_http_client.rs:244`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/builder_client/src/pre_gloas_builder_http_client.rs#L244) post_builder_validators still JSON

**Skeptic check.** Verified that the Accept preference and SSZ decode are on get_header and the Gloas bid call, and that blinded-block submission uses SSZ. This goes further than the nimbus PR, which did not send SSZ requests.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#6970](https://github.com/status-im/nimbus-eth2/pull/6970), [grandine#99](https://github.com/grandinetech/grandine/pull/99)

</details>


<a id="beacon_api-022"></a>
<details>
<summary><b>beacon_api-022</b> SSZ for ePBS payload attestation and preference endpoints — <i>implemented · low · S · cpu, bandwidth</i></summary>

**Idea.** Accept and serve SSZ on the payload attestation pool and proposer preference endpoints, and have the validator client use SSZ by default with JSON fallback on 415, avoiding JSON cost on these per-slot calls.

**Impact.** None left; both ePBS endpoints accept and serve SSZ and the VC uses SSZ by default.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs:3643`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L3643) post_beacon_pool_payload_attestations_ssz in SSZ content-type route group
- [`beacon_node/http_api/src/lib.rs:3645`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L3645) post_validator_proposer_preferences_ssz
- [`beacon_node/http_api/src/lib.rs:1476-1520`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L1476-L1520) GET beacon/proposer_preferences serves SSZ on Accept
- [`beacon_node/http_api/src/beacon/pool.rs:568-590`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/pool.rs#L568-L590) GET payload_attestations serves SSZ on Accept
- [`validator_client/validator_services/src/payload_attestation_service.rs:414-440`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/payload_attestation_service.rs#L414-L440) SSZ first, JSON fallback
- [`validator_client/validator_services/src/proposer_preferences_service.rs:208-235`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/proposer_preferences_service.rs#L208-L235) SSZ first, JSON fallback

**Skeptic check.** Verified the POST SSZ routes, the SSZ GET responses and the VC SSZ-first logic. Earlier evidence was right; the fallback triggers on any error rather than only 415, so a down BN is tried twice, which has no effect on the per-slot SSZ path.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#17064](https://github.com/OffchainLabs/prysm/pull/17064), [prysm#17054](https://github.com/OffchainLabs/prysm/pull/17054)

</details>


<a id="beacon_api-023"></a>
<details>
<summary><b>beacon_api-023</b> Generic Accept negotiation to serve SSZ — <i>not · low · M · cpu, bandwidth</i></summary>

**Idea.** Add a generic, configurable HTTP encoding layer with Accept-header negotiation so any REST endpoint can serve SSZ instead of JSON without per-endpoint code.

**Gap in Lighthouse.** Add a generic warp filter/reply wrapper that negotiates Accept and SSZ-encodes any Encode type, replacing the per-endpoint boilerplate.

**Impact.** No runtime gain on its own; only reduces code and makes adding SSZ to remaining JSON-only endpoints cheap.

**Best measured result.** 'more compact and performant'; no numbers (pr:prysm#15381)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/beacon/states.rs:40`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L40),100,160 each endpoint repeats warp::header::optional Accept and a match accept_header
- [`beacon_node/http_api/src/lib.rs:1190`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L1190) same per-endpoint pattern

**Sources.** [prysm#15381](https://github.com/OffchainLabs/prysm/pull/15381)

</details>


<a id="beacon_api-024"></a>
<details>
<summary><b>beacon_api-024</b> Process submitted pool messages in background after response — <i>not · medium · M · latency</i></summary>

**Idea.** For submitted attestations and sync committee messages, publish to gossip and return the HTTP response right away, and run validation-heavy work (state lookup, pool processing) in a detached background task, so request latency and timeouts are not tied to processing or the gossip loop.

**Gap in Lighthouse.** Network publish happens right after gossip verification, but fork choice, naive aggregation pool insert and unknown-block reprocessing waits stay on the response path. Lighthouse would need to respond after publish and detach the rest (fork choice, pool, reprocess wait), which drops the per-item error reporting the spec defines.

**Impact.** Lower submission latency, mostly for attestations to unknown blocks that wait in the reprocess queue; no CPU saving.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/publish_attestations.rs:70-120`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_attestations.rs#L70-L120) gossip verify, publish, then fork-choice and naive pool insert all run before returning
- [`beacon_node/http_api/src/publish_attestations.rs:140-252`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_attestations.rs#L140-L252) blocking_task is awaited and reprocess oneshots are joined (join_all) before building the response
- [`beacon_node/http_api/src/beacon/pool.rs:554`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/pool.rs#L554) route awaits publish_attestations
- [`beacon_node/http_api/src/beacon/pool.rs:181`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/pool.rs#L181) sync committee route calls process_sync_committee_signatures synchronously

**Second check.** Read the full publish_attestations flow incl. reprocess handling and the pool.rs routes; reprocessing is awaited asynchronously (not blocking workers) but the HTTP response still waits for it, so nothing detached exists.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [prysm#3487](https://github.com/OffchainLabs/prysm/pull/3487), [caplin#24259](https://github.com/erigontech/erigon/pull/24259), [prysm#16152](https://github.com/OffchainLabs/prysm/pull/16152)

</details>


<a id="beacon_api-025"></a>
<details>
<summary><b>beacon_api-025</b> Return envelope publish after broadcast, import in background — <i>partial · low · S · latency</i></summary>

**Idea.** In the execution payload envelope publish API, return once data columns and envelope are broadcast and run the local import (EL newPayload, fork choice) in a background task, so the builder reveal is not delayed by synchronous import.

**Gap in Lighthouse.** The envelope itself is broadcast before newPayload, but data columns are published after process_execution_payload_envelope completes and the HTTP reply blocks on the whole import. publish_and_import_columns could be run concurrently with the import (or the import moved to a spawned task after publish) in publish_execution_payload_envelope.

**Impact.** Cuts the delay on column reveal by the EL newPayload time (tens to hundreds of ms) for builder-submitting nodes only; no effect on ordinary nodes.

**Best measured result.** traced every PTC-voted-missing payload on devnet-7 to the synchronous import (pr:prysm#17198)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/beacon/execution_payload_envelopes.rs:306-312`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/execution_payload_envelopes.rs#L306-L312) envelope gossip published before import when validation=gossip
- [`beacon_node/beacon_chain/src/payload_envelope_verification/import.rs:94-103`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/import.rs#L94-L103) publish_fn called after consensus verification, before EL wait
- [`beacon_node/http_api/src/beacon/execution_payload_envelopes.rs:342-394`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/execution_payload_envelopes.rs#L342-L394) data columns are published only after the import (incl. EL newPayload) returns, and the response waits for it

**Sources.** [prysm#17198](https://github.com/OffchainLabs/prysm/pull/17198)

</details>


<a id="beacon_api-026"></a>
<details>
<summary><b>beacon_api-026</b> Insert API attestations into pool synchronously — <i>implemented · low · S · cpu</i></summary>

**Idea.** When attestations are submitted through the API, insert them into the pool synchronously instead of spawning a task per attestation, because the cache insert is cheaper than the task spawn.

**Impact.** None left; pool insert is inline per attestation inside one batch task.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/publish_attestations.rs:136-232`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_attestations.rs#L136-L232) one blocking_task verifies and inserts the whole batch
- [`beacon_node/http_api/src/publish_attestations.rs:98-99`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_attestations.rs#L98-L99) fork choice apply and naive aggregation pool insert inline in verify_and_publish_attestation

**Skeptic check.** Confirmed publish_attestations runs one blocking task for the batch and inserts each attestation into the naive aggregation pool inline. Only UnknownHeadBlock/UnknownPayloadEnvelope cases go to the reprocess queue, which matches the earlier evidence.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#12345](https://github.com/OffchainLabs/prysm/pull/12345)

</details>


<a id="beacon_api-027"></a>
<details>
<summary><b>beacon_api-027</b> Bounded per-subscriber SSE queues, drop slow clients — <i>partial · low · S · latency, memory</i></summary>

**Idea.** Give each SSE event-stream subscriber its own bounded queue and writer task, decoupled from the event producer, and disconnect subscribers that fall behind; flush once per drained batch. This stops one slow reader from back-pressuring block import or other subscribers.

**Gap in Lighthouse.** Each subscriber has a bounded broadcast receiver and the producer never blocks (send is non-blocking), so back-pressure on import is absent. Slow clients are not disconnected, they just get dropped-message comments; no per-batch flush. Would need a Lagged counter that closes the stream in the events handler in http_api/src/lib.rs.

**Impact.** Marginal: producer is already decoupled; only saves memory held by stalled SSE clients.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/events.rs:45`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/events.rs#L45) tokio broadcast channel per topic
- [`beacon_node/http_api/src/lib.rs:3449`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L3449) BroadcastStream, Lagged -&gt; comment, stream continues

**Sources.** [teku#2886](https://github.com/Consensys-Incorporated/teku/pull/2886), [prysm#14413](https://github.com/OffchainLabs/prysm/pull/14413), [caplin#24447](https://github.com/erigontech/erigon/pull/24447), [prysm#13329](https://github.com/OffchainLabs/prysm/pull/13329), [lighthouse#1107](https://github.com/sigp/lighthouse/pull/1107), [teku#5408](https://github.com/Consensys-Incorporated/teku/pull/5408)

</details>


<a id="beacon_api-028"></a>
<details>
<summary><b>beacon_api-028</b> Eager SSE socket writes with larger output cap — <i>n/a · low · latency, bandwidth</i></summary>

**Idea.** Write SSE frames to subscriber sockets eagerly when an event is published, and raise the pending-output cap, so event bursts do not disconnect subscribers whose sockets still have room.

**Impact.** Lighthouse uses tokio broadcast and warp SSE with no pending-output cap; slow subscribers get a lag comment instead of being disconnected, so the problem does not exist.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/events.rs:8`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/events.rs#L8) tokio broadcast channels, capacity 512 x multiplier
- [`beacon_node/http_api/src/lib.rs:3450-3470`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L3450-L3470) BroadcastStream with Lagged mapped to a comment, no disconnect

**Sources.** [silver#255](https://github.com/gattaca-com/silver/pull/255)

</details>


<a id="beacon_api-029"></a>
<details>
<summary><b>beacon_api-029</b> Build SSE payloads only when subscribers exist — <i>implemented · low · S · cpu</i></summary>

**Idea.** Send SSE events straight through a broadcast channel without intermediate message types and forwarding tasks, and build event payloads only when the event type has subscribers, avoiding wasted serialization and message passing.

**Impact.** None left; every register call site I checked is behind a has_*_subscribers check.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/events.rs:105-140`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/events.rs#L105-L140) register() sends straight on tokio broadcast channels
- [`beacon_node/http_api/src/lib.rs:3448-3470`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L3448-L3470) BroadcastStream per receiver, JSON built in the stream, no forwarding task
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2295`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2295),2348 attestation events gated on has_*_subscribers
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4594-4597`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4594-L4597),4638-4641,5149-5150 head, head_v2, block events gated
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3652-3653`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3652-L3653),3676-3677 blob/column events gated
- [`beacon_node/beacon_chain/src/block_verification.rs:1118-1119`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1118-L1119) block_gossip gated
- [`beacon_node/beacon_chain/src/inclusion_list_verification/gossip_verified_inclusion_list.rs:260-264`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/inclusion_list_verification/gossip_verified_inclusion_list.rs#L260-L264) clone only when subscribers

**Skeptic check.** Checked all EventKind register call sites in beacon_chain: each one builds its payload only after a subscriber check. JSON is serialized per subscriber stream, not once per event; that only costs extra with several subscribers and is outside this idea.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine@e48fd9ebe](https://github.com/grandinetech/grandine/commit/e48fd9ebef65), [lodestar@530591f8d](https://github.com/ChainSafe/lodestar/commit/530591f8d274)

</details>


<a id="beacon_api-030"></a>
<details>
<summary><b>beacon_api-030</b> Share payload attributes between SSE and engine call — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Compute payload attributes once and reuse them for both the payload_attributes SSE event and the engine API forkchoiceUpdated call, computing the event off the critical path, so slow computation does not block the event feed and work is not duplicated.

**Impact.** None left; one computation feeds both the SSE event and the engine fcU.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:6950-7069`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6950-L7069) attributes read from the EL proposer cache or computed once (withdrawals in spawn_blocking) and inserted into the cache
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7072-7108`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7072-L7108) same attributes moved into the SSE event only with subscribers
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7126-7135`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7126-L7135) fcU reads the primed cache via update_execution_engine_forkchoice

**Skeptic check.** Verified prepare_beacon_proposer: it computes the attributes once, caches them in the EL, reuses them for the event and the fcU, and does not run in an SSE reader. Attributes are made only for tracked proposers unless always_prepare_payload is set; this is a feature choice, not a duplicated cost.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#14644](https://github.com/OffchainLabs/prysm/pull/14644), [silver#444](https://github.com/gattaca-com/silver/pull/444)

</details>


<a id="beacon_api-031"></a>
<details>
<summary><b>beacon_api-031</b> Skip head SSE event when head unchanged — <i>implemented · low · S · cpu, bandwidth</i></summary>

**Idea.** Do not emit a head SSE event when fork choice recomputes the same head, avoiding duplicate events and their serialization.

**Impact.** None; a fork choice rerun that gives the same head emits no event.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:4555-4620`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4555-L4620) head SSE event emitted once, at import, only when the imported block becomes head
- [`beacon_node/beacon_chain/src/canonical_head.rs:1207-1214`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1207-L1214) after_new_head only on a head block root change
- [`beacon_node/beacon_chain/src/canonical_head.rs:1222-1228`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1222-L1228) second head_v2 only on payload status change

**Skeptic check.** The only EventKind::Head registration is in import_block, guarded by get_head returning the imported root, so a recomputed same head never emits. The earlier evidence pointed at after_new_head for the head event, which is the wrong place, but the conclusion holds.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine#179](https://github.com/grandinetech/grandine/pull/179)

</details>


<a id="beacon_api-032"></a>
<details>
<summary><b>beacon_api-032</b> Always unregister event-stream listeners — <i>implemented · low · S · memory</i></summary>

**Idea.** Unregister the REST event-stream listener from the event queue in a finally/defer/Drop path, so errors or disconnects cannot leave stale subscribers accumulating in memory.

**Impact.** None; receivers drop with the response stream (RAII), so no stale subscribers can build up.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs:3357-3470`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L3357-L3470) each topic subscribes a tokio broadcast Receiver wrapped in BroadcastStream inside the SSE response stream
- [`beacon_node/beacon_chain/src/events.rs:105`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/events.rs#L105) register() sends on broadcast Sender; dropped receivers stop counting

**Skeptic check.** In Rust the unsubscribe is the Drop of the broadcast Receiver when hyper drops the body stream on disconnect or error, which is the same as the nimbus defer fix. Lagged receivers get a comment and do not block the sender.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#8690](https://github.com/status-im/nimbus-eth2/pull/8690)

</details>


<a id="beacon_api-033"></a>
<details>
<summary><b>beacon_api-033</b> Emit head/block SSE event early in import — <i>partial · low · S · latency</i></summary>

**Idea.** Emit the head (or block-processed) SSE event as soon as fork choice selects the new head, before slow persistence and before the EL marks an optimistic head Valid (re-emit once then), so validator clients can attest sooner.

**Gap in Lighthouse.** The early emission before persistence is done. When a head is imported optimistically and the EL later marks it Valid (the on_valid_execution_payload path in update_execution_engine_forkchoice, or recompute_head with an unchanged block root), Lighthouse sends no new Head or HeadV2 event with execution_optimistic=false. The VC beacon_head_monitor drops the optimistic event, so it waits for the attestation deadline. The fix: re-emit the head event in recompute_head_at_slot_internal when the head verdict changes from optimistic to valid for the same block root.

**Impact.** The 500ms-1s persist_fork_choice delay is already avoided. The remaining gap applies only to slots where the EL returned SYNCING/ACCEPTED for newPayload, which is rare on a healthy node.

**Best measured result.** persist_fork_choice 500ms-1s avoided (pr:lighthouse#8718)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:4545-4640`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4545-L4640) Head/HeadV2 SSE registered in import_block right after fork_choice.get_head, before do_atomically_with_block_and_blobs_cache (~4756) and after_new_head/persist
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4618`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4618) only emission site of EventKind::Head
- [`beacon_node/beacon_chain/src/canonical_head.rs:1222-1262`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1222-L1262) second event is head_v2 only for Gloas payload_status Empty-&gt;Full, not optimistic-&gt;Valid
- [`validator_client/beacon_node_fallback/src/beacon_head_monitor.rs:197`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/beacon_node_fallback/src/beacon_head_monitor.rs#L197) VC skips head events with execution_optimistic=true
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7279`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7279) on_valid_execution_payload path emits no head event

**Skeptic check.** Confirmed that #8718's early emission is on the import hot path. The earlier evidence wrongly took the canonical_head.rs:1222 head_v2 re-emit as the 're-emit once Valid' part. That code fires on a Gloas payload-status change, not on an optimistic-to-valid transition.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lighthouse#8718](https://github.com/sigp/lighthouse/pull/8718), [prysm#17241](https://github.com/OffchainLabs/prysm/pull/17241), [silver#277](https://github.com/gattaca-com/silver/pull/277), [prysm#17560](https://github.com/OffchainLabs/prysm/pull/17560)

</details>


<a id="beacon_api-034"></a>
<details>
<summary><b>beacon_api-034</b> Tear down cancelled REST responses, async timeout — <i>n/a · low · memory</i></summary>

**Idea.** When a client cancels or times out an async REST request, tear down the response pipeline without cancelling shared upstream work, and apply an async timeout to non-SSE requests, so sockets and file descriptors are not retained.

**Impact.** Rust futures cancel on drop and shared upstream work is not tied to the response; the Java async pipeline problem does not exist.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs:3357`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L3357) warp/hyper futures are dropped on client disconnect

**Sources.** [teku#11004](https://github.com/Consensys-Incorporated/teku/pull/11004)

</details>


<a id="beacon_api-035"></a>
<details>
<summary><b>beacon_api-035</b> Answer attestation_data from fork choice — <i>partial · low · M · latency</i></summary>

**Idea.** Build attestation_data from fork-choice data (head root, ancestor target root, justified checkpoint) instead of waiting for or reading the new head state, so the request does not block on state publication on empty slots.

**Gap in Lighthouse.** When the head changes after the 3/4-slot state advance in the last slot of an epoch and the next slot is empty, produce_unaggregated_attestation runs partial_state_advance (epoch processing) per request just to get current_justified_checkpoint and committee length. The attestation_data endpoint discards the committee length, and the justified checkpoint is available from fork choice (unrealized justification of the head node). Missing: a fork-choice-only path in produce_unaggregated_attestation for attestation_data, or storing the advanced state back in the state cache / triggering advance_head after a late head change.

**Impact.** Removes a rare epoch-processing stall (hundreds of ms, repeated per request) at epoch boundaries after a late block; the common path is already fast.

**Best measured result.** every request answered within 3 ms; used to take 1 s on empty slots (pr:caplin#25359)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/validator/mod.rs:294-296`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L294-L296) attestation_data calls produce_unaggregated_attestation(slot, 0) and keeps only .data()
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2025-2039`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2025-L2039) early_attester_cache answers during import
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2063-2141`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2063-L2141) head root/target/justified read from head snapshot without waiting
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2153-2174`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2153-L2174) cross-epoch case: get_advanced_hot_state, then partial_state_advance (incl. epoch processing) on the request path if no advanced state exists; result is not cached
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:125-131`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L125-L131),258-286 the advance runs once at 3/4 slot for the head at that time; a head set later (late block, re-org at the 11.5s fork-choice run) gets no advanced state
- [`consensus/proto_array/src/proto_array.rs:130`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L130) fork choice already holds unrealized_justified_checkpoint per node

**Second check.** Earlier review missed the state_advance_timer: it pre-advances the head state into the next epoch at the end of the previous slot and puts it in the state cache, so the cross-epoch branch of produce_unaggregated_attestation is a cache hit, not a state load/advance, which is the Lighthouse equivalent of Caplin's fix.

**Skeptic check.** Verified the common path reads the head snapshot or the pre-advanced cached state, as earlier evidence said. Earlier evidence missed that the pre-advance only covers the head at 3/4 slot, so the request path still does a state transition after a late head change.

**Verdict history.** partial (checked) → implemented (refuted) → partial (skeptic)

**Sources.** [caplin#25359](https://github.com/erigontech/erigon/pull/25359)

</details>


<a id="beacon_api-036"></a>
<details>
<summary><b>beacon_api-036</b> Cache attestation data per slot, no per-request state copy — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** Compute attestation_data once per slot (shared by all committees and validator clients) and reuse a shared state reference, instead of copying the head state for every attestation_data request or committee.

**Impact.** No per-request deep state copy or per-committee recomputation exists in Lighthouse.

**Best measured result.** saves ~1GB runtime memory with 4k validators (pr:prysm#6025)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/attestation_service.rs:257`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L257),284,332 VC fetches attestation_data once per slot and shares it across committees
- [`beacon_node/http_api/src/validator/mod.rs:290-296`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L290-L296) always committee index 0
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2063-2141`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2063-L2141) borrows head snapshot Arc, no state copy
- [`beacon_node/store/src/hot_cold_store.rs:1124-1131`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1124-L1131) get_advanced_hot_state returns a structurally-shared milhouse clone

**Second check.** Checked the VC side (attestation_service fetches once per slot and fans out to committees) and the state-advance/state-cache path; the only missing piece is a literal BN memo, whose work it would skip is a handful of field reads.

**Skeptic check.** Confirmed: data computed once per slot by the VC and the BN reads head fields by reference. The only recompute case (late-head epoch boundary) is covered under beacon_api-035.

**Verdict history.** partial (checked) → implemented (refuted) → implemented (skeptic)

**Sources.** [caplin#11680](https://github.com/erigontech/erigon/pull/11680), [prysm#6025](https://github.com/OffchainLabs/prysm/pull/6025), [prysm#6185](https://github.com/OffchainLabs/prysm/pull/6185)

</details>


<a id="beacon_api-037"></a>
<details>
<summary><b>beacon_api-037</b> Ancestor root from state block_roots for attestation data — <i>implemented · low · S · disk, latency</i></summary>

**Idea.** When serving attestation data for a slot older than head, read the ancestor block root from the head state's block_roots vector instead of walking back block by block with a DB lookup each.

**Impact.** None left; no per-block DB walk.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2098-2110`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2098-L2110) head_state.get_block_root/get_state_root(request_slot) for slots before head
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2112-2119`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2112-L2119) target root from head_state.get_block_root(target_slot)

**Skeptic check.** Confirmed produce_unaggregated_attestation reads ancestor and target roots from the head state block_roots vector. A DB state load happens only in the cross-epoch case, to get the justified checkpoint and committee length, not to walk ancestors.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#5669](https://github.com/OffchainLabs/prysm/pull/5669), [lodestar@117f77b20](https://github.com/ChainSafe/lodestar/commit/117f77b20d4f)

</details>


<a id="beacon_api-038"></a>
<details>
<summary><b>beacon_api-038</b> Read head state fields without cloning the state — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** Serve API fields such as fork, genesis validators root, justified checkpoints, committee seeds and validator indices through cheap chain getters or a read-only head state reference, instead of deep-cloning the head state per request.

**Impact.** Head-state API fields are read by reference; clones are cheap tree-state clones.

**Best measured result.** wasteful to copy the entire state (1.3GB in heap profile) (pr:prysm#5582)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/state_id.rs:214-238`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L214-L238) map_state_and_execution_optimistic_and_finalized passes &amp;head.snapshot.beacon_state for head
- [`beacon_node/http_api/src/state_id.rs:140-170`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L140-L170) fork() goes through the by-reference map
- [`beacon_node/http_api/src/state_id.rs:178-188`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L178-L188) state() for head is a milhouse clone (structurally shared)

**Skeptic check.** Confirmed in state_id.rs. Non-head ids load from the state cache/DB, which is not the head-copy problem the Prysm PRs fixed.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#3671](https://github.com/OffchainLabs/prysm/pull/3671), [prysm#4333](https://github.com/OffchainLabs/prysm/pull/4333), [prysm#11949](https://github.com/OffchainLabs/prysm/pull/11949), [prysm#5582](https://github.com/OffchainLabs/prysm/pull/5582), [prysm#4335](https://github.com/OffchainLabs/prysm/pull/4335), [lighthouse@b0e3ce788](https://github.com/sigp/lighthouse/commit/b0e3ce78855c)

</details>


<a id="beacon_api-039"></a>
<details>
<summary><b>beacon_api-039</b> No state mutation on read-only API paths — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** On read-only API paths avoid mutating state (which invalidates its caches) and avoid copying validator records for balance requests.

**Impact.** None; read paths take &amp;BeaconState, and mutations happen only on owned copies, which do not invalidate shared caches.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/state_id.rs:214-240`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L214-L240) map_state_and_execution_optimistic_and_finalized passes &amp;head state with no copy
- [`beacon_node/http_api/src/state_id.rs:174-188`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L174-L188) head state clone is a structural-sharing milhouse clone
- [`beacon_node/http_api/src/validators.rs:86-125`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validators.rs#L86-L125) balances endpoint iterates validators()/balances() by reference and builds only index+balance

**Skeptic check.** Verified that the balances endpoint does not clone Validator records and that head reads borrow the state. In Lighthouse a mutation of a cloned state cannot invalidate the head's caches, so the nimbus issue does not exist here.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#3092](https://github.com/status-im/nimbus-eth2/pull/3092)

</details>


<a id="beacon_api-040"></a>
<details>
<summary><b>beacon_api-040</b> Send buffered HTTP bodies with Content-Length — <i>implemented · low · S · bandwidth, latency</i></summary>

**Idea.** In the HTTP client, pass already-buffered request bodies as bytes so Content-Length is set, instead of wrapping them in a stream that forces chunked transfer encoding.

**Impact.** None left: every request body in common/eth2, builder_client and the VC is buffered bytes or json(); no wrap_stream anywhere.

**Evidence (Lighthouse @ 928b61e719).**

- [`common/eth2/src/lib.rs:519`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2/src/lib.rs#L519) post_generic uses builder.json(body) (buffered, Content-Length set)
- [`common/eth2/src/lib.rs:582`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2/src/lib.rs#L582) post_generic_with_envelope_headers_and_ssz_body uses builder.body(bytes)
- [`beacon_node/builder_client/src/builder_http_client.rs:315`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/builder_client/src/builder_http_client.rs#L315) .body(block.as_ssz_bytes())

**Skeptic check.** Grepped all .body(/wrap_stream uses in eth2, builder_client, execution_layer and validator_client; all bodies are Vec&lt;u8&gt; or json(), so reqwest sets Content-Length. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#9834](https://github.com/ChainSafe/lodestar/pull/9834)

</details>


<a id="beacon_api-041"></a>
<details>
<summary><b>beacon_api-041</b> No selection-proof check on subnet subscriptions — <i>implemented · low · S · cpu</i></summary>

**Idea.** Do not require or verify a selection proof in the committee subnet subscription API, so the beacon node need not load committees to decide aggregators; trust the validator client's is_aggregator flag.

**Impact.** Handler does no committee lookup or proof verification; it only maps and forwards to the subnet service.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/validator/mod.rs:1141`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L1141) post_validator_beacon_committee_subscriptions
- [`beacon_node/http_api/src/validator/mod.rs:1173`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L1173) is_aggregator copied from request, no selection proof or committee load

**Skeptic check.** Read the handler: it trusts subscription.is_aggregator and sends one AttestationSubscribe message. Earlier evidence correct (this is the Lighthouse PR itself).

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#969](https://github.com/sigp/lighthouse/pull/969)

</details>


<a id="beacon_api-042"></a>
<details>
<summary><b>beacon_api-042</b> Drop extra JSON marshal in debug state API — <i>implemented · low · S · cpu, memory, latency</i></summary>

**Idea.** In the debug get-state JSON path, remove any extra full marshal of the state done only for type checking, so the serialized state is allocated once.

**Impact.** No extra marshal exists; state is serialized exactly once per request on both paths.

**Best measured result.** validators_100000: 225ms -&gt; 91ms (-60%), 347.5MB -&gt; 255.0MB; 1M validators: 2438ms -&gt; 1183ms (pr:prysm#16485)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs:2200`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L2200) JSON path: map_state_and_execution_optimistic_and_finalized then one warp::reply::json(&amp;res)
- [`beacon_node/http_api/src/version.rs:45`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/version.rs#L45) execution_optimistic_finalized_beacon_response wraps &amp;state by reference, no serialization
- [`beacon_node/http_api/src/lib.rs:2181`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L2181) SSZ path as_ssz_bytes once

**Skeptic check.** Verified the wrapper holds &amp;BeaconState and serde serializes once inside warp::reply::json; no type-check marshal. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#16485](https://github.com/OffchainLabs/prysm/pull/16485)

</details>


<a id="beacon_api-043"></a>
<details>
<summary><b>beacon_api-043</b> Debug state as value without SSZ round trip — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** In the debug state endpoint, convert the tree-backed state to a value object directly instead of serializing it to SSZ and deserializing it again.

**Impact.** No SSZ encode/decode round trip in the debug state endpoint.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs:2200`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L2200) JSON path serializes the milhouse-backed state directly via serde
- [`beacon_node/http_api/src/state_id.rs:226`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L226) head state passed by reference without clone or decode

**Skeptic check.** Confirmed there is no as_ssz_bytes/from_ssz_bytes pair on the JSON path; head state is borrowed from the canonical head. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#9078](https://github.com/ChainSafe/lodestar/pull/9078), [lodestar#9080](https://github.com/ChainSafe/lodestar/pull/9080)

</details>


<a id="beacon_api-044"></a>
<details>
<summary><b>beacon_api-044</b> Primitive ints for validator index streams — <i>n/a · low · memory, cpu</i></summary>

**Idea.** Carry validator indices in API handlers as primitive integers instead of boxed objects, avoiding a heap allocation per element.

**Impact.** Rust has no boxed integers; indices are plain u64.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/validator/mod.rs:662`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L662) Vec&lt;SyncCommitteeSubscription&gt; of plain u64 fields

**Sources.** [teku#5039](https://github.com/Consensys-Incorporated/teku/pull/5039)

</details>


<a id="beacon_api-045"></a>
<details>
<summary><b>beacon_api-045</b> Sync committee subscriptions without intermediate sequence — <i>partial · low · S · memory</i></summary>

**Idea.** In the sync committee subscriptions endpoint, process each entry directly instead of first building an intermediate collection.

**Gap in Lighthouse.** Handler already iterates directly with no intermediate collection, but it takes the validator_monitor write lock and does one try_send per subscription. Batching into one lock and one message would be the change in post_validator_sync_committee_subscriptions.

**Impact.** Tiny: saves a lock and channel send per entry on a request of at most a few hundred entries per epoch.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/validator/mod.rs:667-690`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L667-L690) loops subscriptions, sends one channel message per entry with vec![subscription], takes validator_monitor write lock per entry

**Sources.** [nimbus#4281](https://github.com/status-im/nimbus-eth2/pull/4281)

</details>


<a id="beacon_api-046"></a>
<details>
<summary><b>beacon_api-046</b> Leak-free one-shot wait for checkpoint state — <i>n/a · low · memory</i></summary>

**Idea.** When an API call waits for a checkpoint state, use a one-shot listener that is removed on timeout and does not hold a reference to the state, so leaked listeners cannot retain states in memory.

**Impact.** Lighthouse does not wait on checkpoint states through event listeners; the JS listener leak does not exist.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/state_id.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs) state lookup is synchronous from the cache/DB, no listener

**Sources.** [lodestar#6096](https://github.com/ChainSafe/lodestar/pull/6096)

</details>


<a id="beacon_api-047"></a>
<details>
<summary><b>beacon_api-047</b> Blob sidecar requests resolve root without loading block — <i>partial · low · M · disk, cpu</i></summary>

**Idea.** For blob sidecar REST requests, resolve the block id to a root only and read sidecars by root, instead of loading and decoding the full block from the DB.

**Gap in Lighthouse.** Root is resolved first, but the blinded block is still loaded and decoded to get the commitments, fork and max blobs. Could read the sidecars by root and take fork from the slot/epoch in get_blinded_block_and_blob_list_filtered, though the PeerDAS path needs the block anyway.

**Impact.** Saves one blinded-block DB read and decode per blob_sidecars request; rarely called, so negligible for a node.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/block_id.rs:353`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L353) self.root() resolves the id to a root
- [`beacon_node/http_api/src/block_id.rs:354`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L354) then loads the blinded block by root, needed for commitments, fork name, epoch

**Sources.** [nimbus#5668](https://github.com/status-im/nimbus-eth2/pull/5668), [teku#7360](https://github.com/Consensys-Incorporated/teku/pull/7360)

</details>


<a id="beacon_api-048"></a>
<details>
<summary><b>beacon_api-048</b> Skip state root recompute after process_slots — <i>implemented · low · S · cpu</i></summary>

**Idea.** When replaying a state for an API request, do not recompute the full state hash tree root if process_slots already set it; only patch the latest header state root for non-missing blocks.

**Impact.** Lighthouse never hashes the state or header to find the block root for an API state; the summary stores it.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/state_id.rs:66-98`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L66-L98) optimistic status uses hot_summary.latest_block_root, no state or header hashing
- [`beacon_node/http_api/src/state_id.rs:30-38`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L30-L38) head uses cached head_state_root
- [`consensus/state_processing/src/block_replayer.rs:176-208`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/block_replayer.rs#L176-L208) replay takes state roots from the root iterator or previous block before hashing
- [`beacon_node/store/src/hot_cold_store.rs:2390-2394`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2390-L2394) cold replay passes a state root iterator

**Skeptic check.** The Prysm PR removes a redundant HashTreeRoot when deriving a state's block root for IsOptimistic; Lighthouse reads latest_block_root from the hot state summary instead. Earlier evidence (partial_state_advance) cited a related but different mechanism; the verdict still holds.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#10852](https://github.com/OffchainLabs/prysm/pull/10852)

</details>


<a id="beacon_api-049"></a>
<details>
<summary><b>beacon_api-049</b> Hand-written hex QUANTITY validation, no regex — <i>n/a · low · cpu</i></summary>

**Idea.** Validate hex QUANTITY strings in API parameters with a hand-written character check instead of evaluating a regex on every request.

**Impact.** No regex is evaluated for hex parameters in Lighthouse.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs) query params are parsed with serde/FromStr, no regex

**Sources.** [teku#5947](https://github.com/Consensys-Incorporated/teku/pull/5947)

</details>


<a id="beacon_api-050"></a>
<details>
<summary><b>beacon_api-050</b> Parse Accept header once per request — <i>implemented · low · S · cpu</i></summary>

**Idea.** In HTTP content negotiation, parse the Accept header media types once and reuse them, instead of re-parsing the header inside each match check.

**Impact.** Header becomes a 3-variant enum once per route; later checks are enum matches, not re-parses.

**Evidence (Lighthouse @ 928b61e719).**

- [`common/eth2/src/types.rs:1721`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2/src/types.rs#L1721) Accept::from_str parses MediaTypeList once and picks the highest-q type in one pass
- [`beacon_node/http_api/src/lib.rs:2160`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L2160) warp::header::optional::&lt;Accept&gt; parses into an enum; handlers match on the enum

**Skeptic check.** Read the FromStr impl and the handler: one parse into Accept, then a match. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#16267](https://github.com/OffchainLabs/prysm/pull/16267)

</details>


<a id="beacon_api-051"></a>
<details>
<summary><b>beacon_api-051</b> Optimistic status from fork choice, not state hash — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** When an API response needs execution_optimistic, derive it from the block root and fork-choice data instead of computing the full state hash tree root, avoiding large allocations and CPU per request.

**Impact.** No state hash is computed for execution_optimistic.

**Best measured result.** Fixes reported out-of-memory on API requests; no numbers (pr:prysm#12143)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/state_id.rs:30-38`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L30-L38) head: head_and_execution_status
- [`beacon_node/http_api/src/state_id.rs:66-98`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L66-L98) root: fork_choice.is_optimistic_or_invalid_block_assuming_full(latest_block_root)
- [`beacon_node/http_api/src/state_id.rs:268-280`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L268-L280) checkpoint ids: fork choice by checkpoint root

**Skeptic check.** Confirmed every StateId branch derives execution_optimistic from fork choice or cached head status.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#12143](https://github.com/OffchainLabs/prysm/pull/12143)

</details>


<a id="beacon_api-052"></a>
<details>
<summary><b>beacon_api-052</b> State root endpoint from stored block state_root — <i>implemented · low · S · cpu, disk, latency</i></summary>

**Idea.** Serve the state root endpoint from the stored block's state_root field (or a root cache) instead of loading the full state and hashing it.

**Impact.** State root endpoint never loads or hashes a state.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/beacon/states.rs:1133-1146`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L1133-L1146) /states/{id}/root calls only StateId::root
- [`beacon_node/http_api/src/state_id.rs:23-136`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L23-L136) StateId::root resolves from cached head, split, summaries, no state load
- [`beacon_node/beacon_chain/src/beacon_chain.rs:964-1014`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L964-L1014) state_root_at_slot uses split, head state_roots vector, then forwards root iterator

**Skeptic check.** Confirmed the route handler and root resolution; no get_state call on this path.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#16765](https://github.com/OffchainLabs/prysm/pull/16765)

</details>


<a id="beacon_api-053"></a>
<details>
<summary><b>beacon_api-053</b> Find last non-missed slot by scanning backwards — <i>n/a · low · cpu, disk</i></summary>

**Idea.** When looking for the last non-missed slot in an epoch for an API query, iterate backwards from the epoch end instead of forwards from the start, stopping at the first hit.

**Impact.** Lighthouse has no API path that scans an epoch's slots for the last non-missed slot; it uses dependent roots from fork choice/shuffling.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src) grep: no last-non-missed-slot scan in any handler

**Sources.** [caplin#12062](https://github.com/erigontech/erigon/pull/12062)

</details>


<a id="beacon_api-054"></a>
<details>
<summary><b>beacon_api-054</b> Array bodies for attestation and subscription submissions — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Let pool submission and committee subscription endpoints accept an array so the validator client sends all its attestations or subscriptions in one request, cutting per-request overhead for many validators.

**Impact.** Both the BN endpoints and the VC use array bodies; attestations are streamed in batches deliberately to publish early.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/validator/mod.rs:1158`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L1158) committee subscriptions take Vec&lt;BeaconCommitteeSubscription&gt;
- [`validator_client/validator_services/src/duties_service.rs:1172`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1172) VC posts all subscriptions in one call
- [`validator_client/validator_services/src/attestation_service.rs:585`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L585) VC posts each signed batch as one array
- [`validator_client/validator_services/src/sync_committee_service.rs:353`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/sync_committee_service.rs#L353) sync signatures posted as array

**Skeptic check.** Checked both BN handlers and VC callers (attestations, aggregates, sync signatures, contributions, subscriptions, preparation) all send arrays. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#2367](https://github.com/ChainSafe/lodestar/pull/2367), [lodestar#2055](https://github.com/ChainSafe/lodestar/pull/2055), [lighthouse#1899](https://github.com/sigp/lighthouse/pull/1899)

</details>


<a id="beacon_api-055"></a>
<details>
<summary><b>beacon_api-055</b> Batch prepare_beacon_proposer under one lock — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Process a prepare_beacon_proposer request's registrations as one batch under a single lock acquisition, instead of a lock and message per validator.

**Impact.** One lock acquisition per request; no per-validator message.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/validator/mod.rs:1036`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L1036) handler takes Vec&lt;ProposerPreparationData&gt; and calls update_proposer_preparation once
- [`beacon_node/execution_layer/src/lib.rs:820`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L820) one proposer_preparation_data() lock, loop inside

**Skeptic check.** Read update_proposer_preparation: lock taken once before the loop over all entries. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine@5fd9afafb](https://github.com/grandinetech/grandine/commit/5fd9afafb421)

</details>


<a id="beacon_api-056"></a>
<details>
<summary><b>beacon_api-056</b> Bloom filter for multi-id validator queries — <i>implemented · low · S · cpu</i></summary>

**Idea.** When a validators REST request filters by many ids, build a Bloom filter (or hash set) of the ids so each validator in the state is checked in constant time instead of a linear scan of the id list.

**Impact.** All id-filtered state scans use O(1) hash set lookups.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/validators.rs:24`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validators.rs#L24) HashSet&lt;&amp;ValidatorId&gt; for GET validators
- [`beacon_node/http_api/src/validators.rs:95`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validators.rs#L95) HashSet for validator balances
- [`beacon_node/http_api/src/validators.rs:143`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validators.rs#L143) HashSet for third id-filtered endpoint
- [`beacon_node/http_api/src/builders.rs:24`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/builders.rs#L24) HashSet for builders

**Skeptic check.** All three id-filtered validator endpoints and the builders endpoint use HashSet; no linear id-list scan found. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#5212](https://github.com/status-im/nimbus-eth2/pull/5212)

</details>


<a id="beacon_api-057"></a>
<details>
<summary><b>beacon_api-057</b> Bound state regeneration for far-out API requests — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Reject API requests that would force regenerating or advancing a state through arbitrarily many slots: future slots beyond the clock, sync duties beyond the next period, or replays of empty slots beyond a cap, returning 404/400/503. This stops a single request from starving block import.

**Impact.** No API state path replays empty slots forward without bound; the Lodestar wedge (regen from head to a near-clock slot) cannot happen because Lighthouse serves the head state for slots past head.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:964-998`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L964-L998) state_root_at_slot returns None for slot &gt; clock and the head state root for slots past head (no forward replay)
- [`beacon_node/store/src/hot_cold_store.rs:1087-1111`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1087-L1111) get_state only loads by root, never advances
- [`beacon_node/http_api/src/sync_committees.rs:96-131`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/sync_committees.rs#L96-L131) sync duties bounded to current period + 1
- [`beacon_node/http_api/src/attester_duties.rs:45-55`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L45-L55) attester duties bounded to current epoch + 1
- [`beacon_node/http_api/src/validator/mod.rs:283-288`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L283-L288) attestation_data rejects slot &gt; current+1
- [`beacon_node/http_api/src/lib.rs:474-511`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L474-L511) not_while_syncing_filter

**Second check.** Earlier review missed not_while_syncing_filter: the validator endpoints that would call state_at_slot with a lagging head return 503 once the head is more than 2 epochs behind the clock while syncing, which is the empty-slot replay cap the idea asks for, enforced at the API layer.

**Skeptic check.** Confirmed the three protections plus the state-by-slot path the Lodestar PRs fixed. state_at_slot has no hard cap, but its API caller (sync duties) is period-bounded and syncing-gated.

**Verdict history.** partial (checked) → implemented (refuted) → implemented (skeptic)

**Sources.** [lodestar#9634](https://github.com/ChainSafe/lodestar/pull/9634), [teku#3956](https://github.com/Consensys-Incorporated/teku/pull/3956), [lodestar#8665](https://github.com/ChainSafe/lodestar/pull/8665)

</details>


<a id="beacon_api-058"></a>
<details>
<summary><b>beacon_api-058</b> Advance state only to epoch start for committees — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** When computing committees for a requested slot, advance the head state only to the start of that slot's epoch (not at all if the epoch is not ahead of head), instead of slot by slot to the requested slot.

**Impact.** Committee computations never advance slot by slot to the requested slot.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/beacon/states.rs:605-685`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L605-L685) committees from historical_committee_cache or CommitteeCache::initialized(state, epoch), no advance
- [`beacon_node/http_api/src/attester_duties.rs:187-200`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L187-L200) advances only to start of target_epoch-1
- [`beacon_node/beacon_chain/src/block_verification.rs:2173-2210`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L2173-L2210) cheap_state_advance_to_obtain_committees advances to epoch start
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:446-460`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L446-L460) attestation shuffling advance only when 2+ epochs behind

**Skeptic check.** Confirmed on the API, block verification and attestation shuffling paths.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#4297](https://github.com/OffchainLabs/prysm/pull/4297)

</details>


<a id="beacon_api-059"></a>
<details>
<summary><b>beacon_api-059</b> RANDAO endpoint via accelerated shuffling recovery — <i>not · low · M · cpu, disk, latency</i></summary>

**Idea.** Serve the REST randao endpoint using the fast RANDAO-mix recovery used for shuffling computation instead of loading a full state.

**Gap in Lighthouse.** For non-head state ids the randao handler loads a full state via StateId::state. A fast path could read the RANDAO mix from a cached/derived source (e.g. from the block header/state root lookup of the specific mix) for historic ids.

**Impact.** Only affects rare randao queries on non-head states; head case already free. Saves a state load (tens of ms to seconds) on those calls.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/beacon/states.rs:393`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L393) get_beacon_state_randao
- [`beacon_node/http_api/src/state_id.rs:218`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L218) head state is used from memory; other states go through self.state()

**Sources.** [nimbus#5204](https://github.com/status-im/nimbus-eth2/pull/5204)

</details>


<a id="beacon_api-060"></a>
<details>
<summary><b>beacon_api-060</b> Box large async futures on block publish — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** In the block publish path, box large futures (Box::pin) and pass Arcs instead of moving blocks or states by value, shrinking future sizes to avoid stack overflows and large stack copies.

**Impact.** Smaller futures on the publish path, avoids stack overflow; negligible CPU.

**Best measured result.** futures 100KB to ~33KB, then ~16KB (pr:lighthouse#5104)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/publish_blocks.rs:335`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L335) Box::pin(chain.process_gossip_data_columns(..))
- [`beacon_node/http_api/src/publish_blocks.rs:353`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L353) Box::pin(chain.process_block(..)) for gossip-verified block
- [`beacon_node/http_api/src/publish_blocks.rs:404`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L404) Box::pin(chain.process_block(..)) for LookupBlock
- [`beacon_node/http_api/src/publish_blocks.rs:185`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L185) publish closure takes Arc&lt;SignedBeaconBlock&gt;

**Skeptic check.** Confirmed the large process_block / process_gossip_data_columns futures are boxed on every publish branch and blocks move as Arc. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#5104](https://github.com/sigp/lighthouse/pull/5104)

</details>


<a id="beacon_api-061"></a>
<details>
<summary><b>beacon_api-061</b> Build API type definitions once — <i>n/a · low · cpu, memory</i></summary>

**Idea.** Build enum/type definitions used by the JSON API layer once and reuse them, instead of rebuilding the definition on every helper call.

**Impact.** Java-specific API type definition rebuilding; Lighthouse uses compile-time serde derives.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs) (Rust warp/serde, no runtime type-definition builder)

**Sources.** [teku#8542](https://github.com/Consensys-Incorporated/teku/pull/8542)

</details>


<a id="beacon_api-062"></a>
<details>
<summary><b>beacon_api-062</b> Precompute node version response — <i>partial · low · S · cpu</i></summary>

**Idea.** Compute the /eth/v1/node/version response once at startup and reuse it for every request, since the version string is constant for the process lifetime.

**Gap in Lighthouse.** Cache the string in a OnceLock/LazyLock inside version_with_platform. Cost today is one small allocation per call.

**Impact.** Negligible; endpoint is rarely hit.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs:2383`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L2383) get_node_version bypasses task spawner
- [`common/lighthouse_version/src/lib.rs:23`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/lighthouse_version/src/lib.rs#L23) version_with_platform() runs format! per request

**Sources.** [nimbus#2961](https://github.com/status-im/nimbus-eth2/pull/2961)

</details>


<a id="beacon_api-063"></a>
<details>
<summary><b>beacon_api-063</b> Precomputed field-name casing map for JSON — <i>n/a · low · cpu</i></summary>

**Idea.** Give each SSZ container a declaration-time map from JSON snake_case names to field names, so JSON encode/decode looks names up instead of running a case conversion on every field.

**Impact.** Rust serde derives resolve field names at compile time; no per-field case conversion at runtime.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs) (serde derive handles field names at compile time)

**Sources.** [lodestar#3288](https://github.com/ChainSafe/lodestar/pull/3288), [lodestar#3351](https://github.com/ChainSafe/lodestar/pull/3351), [lodestar@f4bd52dec](https://github.com/ChainSafe/lodestar/commit/f4bd52dec8f2)

</details>


<a id="beacon_api-064"></a>
<details>
<summary><b>beacon_api-064</b> Resolve block id via slot-indexed lookup — <i>implemented · low · S · cpu, disk</i></summary>

**Idea.** In validator API handlers, resolve the head or a slot block through a cheap slot-indexed lookup instead of the heavier generic block-by-selector helper.

**Impact.** Head and slot ids already resolve to a root by cheap in-memory or slot-indexed lookup; only BlockId::Root loads the blinded block to get its slot.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/block_id.rs:48`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L48) BlockId::Head reads canonical_head.head_and_execution_status(), no store read
- [`beacon_node/http_api/src/block_id.rs:74`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L74) BlockId::Slot resolves via chain.block_root_at_slot (slot-indexed root lookup), not a block load

**Skeptic check.** Nimbus commit d4970e07 swaps getBlockByXXX for atSlot in validator handlers; Lighthouse resolves Head from the cached head and Slot via block_root_at_slot. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus@d4970e07d](https://github.com/status-im/nimbus-eth2/commit/d4970e07d233)

</details>


<a id="beacon_api-065"></a>
<details>
<summary><b>beacon_api-065</b> Resolve state_id directly via selector — <i>partial · low · S · cpu, disk, latency</i></summary>

**Idea.** Resolve a state_id (head, finalized, root, slot) directly to the state through the matching selector instead of converting it to a slot first and looking the state up again, so head and finalized are served from in-memory states.

**Gap in Lighthouse.** Head is served from the in-memory snapshot, but finalized/justified go checkpoint -&gt; slot -&gt; state_root_at_slot -&gt; chain.get_state (state cache/DB). Could resolve finalized/justified straight to the checkpoint state root via fork choice/state cache in StateId::root and state.

**Impact.** Faster finalized/justified state API calls; rarely hot on a mainnet node.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/state_id.rs:25`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L25) root() resolves selector; Head returns early at :34 and :186; Finalized/Justified convert checkpoint to slot then state_root_at_slot at :112

**Sources.** [teku#3118](https://github.com/Consensys-Incorporated/teku/pull/3118), [teku#3119](https://github.com/Consensys-Incorporated/teku/pull/3119), [teku#3120](https://github.com/Consensys-Incorporated/teku/pull/3120), [teku#3123](https://github.com/Consensys-Incorporated/teku/pull/3123), [teku#3128](https://github.com/Consensys-Incorporated/teku/pull/3128)

</details>


<a id="beacon_api-066"></a>
<details>
<summary><b>beacon_api-066</b> Avoid copies when listing pool attestations — <i>partial · low · S · cpu, memory</i></summary>

**Idea.** Make the get pool attestations endpoint avoid redundant work and copies of attestations while filtering and listing the pool.

**Gap in Lighthouse.** Filter on slot first and compute the committee indices map only when committee_index is set; do the fork-variant filter inside get_filtered_attestations so non-matching variants are not cloned.

**Impact.** Rare debugging endpoint; saves a HashSet allocation per pool attestation and some clones, only matters when polled.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/beacon/pool.rs:484`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/pool.rs#L484) get_filtered_attestations then extend, clones every matching attestation
- [`beacon_node/operation_pool/src/lib.rs:775`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L775) filter calls get_committee_indices_map() (allocates a HashSet) per attestation, then clone_as_attestation()
- [`beacon_node/http_api/src/beacon/pool.rs:506`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/pool.rs#L506) second pass filters by fork and collects another Vec

**Sources.** [nimbus@088b00138](https://github.com/status-im/nimbus-eth2/commit/088b001388ed)

</details>


<a id="beacon_api-067"></a>
<details>
<summary><b>beacon_api-067</b> Cheap API client request path building — <i>n/a · low · cpu, memory</i></summary>

**Idea.** In the HTTP API client, build request paths by direct string concatenation instead of templating/format machinery, precompute constant headers, and share error-decoding helpers to cut per-request allocations.

**Impact.** The idea targets Prysm's Go HTTP client; Lighthouse's Rust client builds URLs with a Url builder off the BN request path.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs:1559`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L1559) BN serves the endpoint; the Rust client in [`common/eth2`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2) is used by the VC, not on a BN hot path

**Sources.** [prysm#16694](https://github.com/OffchainLabs/prysm/pull/16694)

</details>


<a id="beacon_api-068"></a>
<details>
<summary><b>beacon_api-068</b> Avoid repeated work per committee subscription entry — <i>partial · low · S · cpu</i></summary>

**Idea.** In the committee subscription handler, hoist work that is the same for all entries (state/epoch lookups) out of the per-subscription loop.

**Gap in Lighthouse.** Take the validator_monitor write lock once before the loop (or register all indices in one call) in post_validator_beacon_committee_subscriptions.

**Impact.** Saves one write-lock acquisition per subscription (hundreds per call for big VCs); microseconds.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/validator/mod.rs:1162-1176`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L1162-L1176) per-subscription validator_monitor.write() lock plus auto_register_local_validator
- [`beacon_node/http_api/src/validator/mod.rs:1180`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L1180) one try_send for the whole batch

**Sources.** [nimbus#3153](https://github.com/status-im/nimbus-eth2/pull/3153)

</details>


<a id="beacon_api-069"></a>
<details>
<summary><b>beacon_api-069</b> Separate small committee cache for HTTP committees route — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Serve the committees HTTP route for historical epochs from a separate small committee cache, so historical queries do not evict or constrain the main chain committee/shuffling cache.

**Impact.** Historical committee queries do not evict the main shuffling cache.

**Best measured result.** Slight extra memory cost; no speedup stated (pr:lighthouse#9318)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/caches.rs:22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/caches.rs#L22) HistoricalCommitteeCache LRU used only by HTTP API
- [`beacon_node/http_api/src/beacon/states.rs:602`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L602) committees route uses historical_committee_cache keyed by HistoricalShufflingId
- [`beacon_node/http_api/src/lib.rs:153`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L153) historical_committee_cache_size config

**Skeptic check.** The committees route reads and fills a separate LRU (states.rs:636/683) and does not touch the chain shuffling cache. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#9318](https://github.com/sigp/lighthouse/pull/9318)

</details>


<a id="beacon_api-070"></a>
<details>
<summary><b>beacon_api-070</b> Promise cache deduplicating concurrent state requests — <i>partial · medium · M · cpu, memory, latency</i></summary>

**Idea.** Put a promise cache in front of HTTP state loading so concurrent requests for the same state root share one computation, with a concurrency cap, instead of each request loading or replaying the state.

**Gap in Lighthouse.** No in-flight dedup: concurrent identical state requests that miss state_cache/historic_state_cache each do their own load/replay. Add a promise map keyed by state root (or cold slot) around get_hot_state/load_cold_state_by_slot, as PR 4879 did on tree-states before it was lost.

**Impact.** Bursts of parallel requests for the same non-cached state (indexers, explorers) do one reconstruction instead of N; no effect on pure validator nodes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/state_id.rs:196-197`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L196-L197) StateId::state calls chain.get_state directly, no in-flight sharing
- [`beacon_node/store/src/hot_cold_store.rs:1817-1826`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1817-L1826) get_hot_state checks state_cache then releases the lock and loads from disk, so concurrent misses each load
- [`beacon_node/store/src/hot_cold_store.rs:2310-2322`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2310-L2322) load_cold_state_by_slot drops historic_state_cache lock before hdiff load/replay, no promise
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:106`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L106),287-301 Promise + MAX_CONCURRENT_PROMISES only for attester shufflings
- [`beacon_node/http_api/src/task_spawner.rs:22-23`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/task_spawner.rs#L22-L23) HTTP work goes through beacon_processor ApiRequestP0/P1 queues, which caps concurrency by worker count but does not dedup

**Second check.** Checked the store layer (hot state_cache and historic_state_cache lock scopes) for implicit dedup through lock holding: locks are dropped before the expensive load. The beacon processor worker pool is the only concurrency cap; there is no PromiseCache or equivalent anywhere.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [lighthouse#4879](https://github.com/sigp/lighthouse/pull/4879)

</details>


<a id="beacon_api-071"></a>
<details>
<summary><b>beacon_api-071</b> Remove redundant storage call in block handler — <i>partial · low · S · disk, latency</i></summary>

**Idea.** In the get-block API handler, remove the redundant extra storage lookup so each request reads the block from the database once.

**Gap in Lighthouse.** In BlockId::root for CoreBlockId::Root, avoid the blinded block read: take the slot from fork choice (block_exists only as fallback) or hand the fetched block to callers.

**Impact.** A get-block-by-root costs up to 3 DB reads of a block instead of 1; modest saving on a rarely hot endpoint.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/block_id.rs:106-122`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L106-L122) by-root path does block_exists then get_blinded_block only to learn slot/finalized
- [`beacon_node/http_api/src/block_id.rs:274`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L274) full_block then reads the block again via chain.get_block
- [`beacon_node/http_api/src/block_id.rs:155`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L155) blinded_block_by_root reads again

**Sources.** [teku#3034](https://github.com/Consensys-Incorporated/teku/pull/3034)

</details>


<a id="beacon_api-072"></a>
<details>
<summary><b>beacon_api-072</b> Validator monitor caches balances for API queries — <i>implemented · low · S · disk, cpu, latency</i></summary>

**Idea.** Cache per-validator balances and summary metrics in the validator monitor at epoch processing and serve UI/API queries from that cache, so they need no historical state reads.

**Impact.** UI validator_info endpoint reads cached balances, no historical state loads.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/ui.rs:137`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/ui.rs#L137) get_validator_info serves validator.get_total_balance(epoch) from the monitor
- [`beacon_node/beacon_chain/src/validator_monitor.rs:514`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_monitor.rs#L514) balances registered into per-epoch summaries during epoch processing
- [`beacon_node/beacon_chain/src/validator_monitor.rs:366`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_monitor.rs#L366) get_total_balance

**Skeptic check.** This is Lighthouse's own PR #3863 and the code is present as cited. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#3863](https://github.com/sigp/lighthouse/pull/3863)

</details>


<a id="beacon_api-073"></a>
<details>
<summary><b>beacon_api-073</b> Doppelganger check early return skips historical states — <i>n/a · medium · cpu, startup</i></summary>

**Idea.** In the doppelganger/liveness check, return early when all requested keys were recently observed, so the expensive regeneration of historical states is skipped.

**Impact.** Lighthouse's liveness check reads in-memory observed attester sets and never loads historical states, bounded to prev/current/next epoch.

**Best measured result.** Not quantified; allows quicker validator restarts (pr:prysm#9964)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/validator/mod.rs:595-640`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L595-L640) liveness answered from in-memory observed_* sets
- [`beacon_node/beacon_chain/src/beacon_chain.rs:8346`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L8346) validator_seen_at_epoch

**Sources.** [prysm#9964](https://github.com/OffchainLabs/prysm/pull/9964)

</details>


<a id="beacon_api-074"></a>
<details>
<summary><b>beacon_api-074</b> Reject pre-fork requests before generating state — <i>partial · low · S · cpu, latency</i></summary>

**Idea.** For endpoints that only exist from a given fork (e.g. Altair sync committee), check the requested slot's fork version first and answer immediately, instead of generating a state and then failing.

**Gap in Lighthouse.** In sync_committee_duties also return early when request_epoch is before Altair, before calling state_at_slot.

**Impact.** Avoids a state load for pre-Altair requests; on mainnet this practically never happens.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/sync_committees.rs:104`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/sync_committees.rs#L104) early empty response only when the current epoch is pre-Altair
- [`beacon_node/http_api/src/sync_committees.rs:113-120`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/sync_committees.rs#L113-L120) pre-Altair request epoch is clamped to altair_fork_epoch and state_at_slot still runs

**Sources.** [teku#4302](https://github.com/Consensys-Incorporated/teku/pull/4302)

</details>


<a id="beacon_api-075"></a>
<details>
<summary><b>beacon_api-075</b> Validator activation status check once per epoch — <i>not · low · M · cpu</i></summary>

**Idea.** In validator listing/status queries, compute validator activation status checks once per epoch and reuse the result, instead of on every slot or call, since assignments only change per epoch.

**Gap in Lighthouse.** Cache per-epoch status or index-by-pubkey so get_beacon_state_validators avoids a full validator scan per call; the full scan with status per validator is O(N) over ~1M validators. Add an epoch-keyed cache in validators.rs.

**Impact.** Large unfiltered /validators calls would be cheaper; only matters for heavy API consumers.

**Best measured result.** ~6% of run time was spent in list_validators (pr:prysm#11340)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/validators.rs:13-70`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validators.rs#L13-L70) computes ValidatorStatus::from_validator per validator on each request, no cache

**Sources.** [prysm#11340](https://github.com/OffchainLabs/prysm/pull/11340)

</details>


<a id="beacon_api-076"></a>
<details>
<summary><b>beacon_api-076</b> Fast hex encode/decode in JSON serialization — <i>partial · low · M · cpu</i></summary>

**Idea.** Use an optimized hex encoding/decoding routine for byte fields in JSON serialization instead of a generic per-byte conversion.

**Gap in Lighthouse.** Move ethereum_serde_utils (or local wrappers) to const-hex with single-allocation prefixed encode/decode used for Hash256, bytes and signatures in JSON.

**Impact.** JSON responses heavy in hex (validators, blocks) get a few percent cheaper; SSZ responses unaffected.

**Evidence (Lighthouse @ 928b61e719).**

- ethereum_serde_utils-0.8.1/src/hex.rs:7-8 encode uses hex::encode then adds the 0x prefix (extra String)
- Cargo.lock: hex 0.4.3 and const-hex 1.19.3 both present; serde hex path uses hex 0.4.3, not const-hex

**Sources.** [grandine#84](https://github.com/grandinetech/grandine/pull/84), [caplin#23879](https://github.com/erigontech/erigon/pull/23879)

</details>


<a id="beacon_api-077"></a>
<details>
<summary><b>beacon_api-077</b> Block rewards API loads state directly, no replay — <i>implemented · low · S · cpu, disk, latency</i></summary>

**Idea.** For the block rewards API, load the relevant post or parent state directly from the store instead of loading the block and regenerating its state by replay.

**Impact.** Block rewards endpoint loads the parent state from the store with no block replay; the endpoint is rare.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/sync_committee_rewards.rs:48`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/sync_committee_rewards.rs#L48) get_state_before_applying_block loads the parent state by state root and only advances slots (apply_blocks(vec![]))
- [`beacon_node/http_api/src/standard_block_rewards.rs:18`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/standard_block_rewards.rs#L18) compute_beacon_block_rewards uses it

**Skeptic check.** Verified the only block-rewards endpoint (beacon/rewards/blocks) uses a direct parent-state load plus empty-slot advance, matching Teku #7344. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#7344](https://github.com/Consensys-Incorporated/teku/pull/7344)

</details>


<a id="beacon_api-078"></a>
<details>
<summary><b>beacon_api-078</b> Fetch blobs from EL on gossip block arrival — <i>implemented · high · M · latency, bandwidth, sync</i></summary>

**Idea.** When a gossip block with blob commitments arrives, call engine_getBlobs on the local EL and build the blob/data column sidecars from the response. The block becomes available without waiting for the sidecars from gossip or peers.

**Impact.** Blocks become available from EL blobs without waiting for gossip columns.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1936`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1936) spawn_fetch_block_columns on gossip-verified block
- [`beacon_node/network/src/network_beacon_processor/mod.rs:998`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L998) fetch_engine_blobs_and_publish_full
- [`beacon_node/beacon_chain/src/fetch_blobs/fetch_blobs_beacon_adapter.rs:54`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/fetch_blobs_beacon_adapter.rs#L54) get_blobs_v2/v3/v4
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:356`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L356) builds custody columns, publishes and imports via process_engine_blobs_fulu

**Skeptic check.** Gossip blocks (Fulu header and Gloas bid) trigger getBlobs, build custody columns and import them. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#7123](https://github.com/status-im/nimbus-eth2/pull/7123), [lodestar#7679](https://github.com/ChainSafe/lodestar/pull/7679), [prysm#15483](https://github.com/OffchainLabs/prysm/pull/15483), [caplin#25447](https://github.com/erigontech/erigon/pull/25447), [grandine#79](https://github.com/grandinetech/grandine/pull/79), [lodestar#7134](https://github.com/ChainSafe/lodestar/pull/7134), [nimbus#7866](https://github.com/status-im/nimbus-eth2/pull/7866)

</details>


<a id="beacon_api-079"></a>
<details>
<summary><b>beacon_api-079</b> Query EL first, request only remaining blobs from peers — <i>partial · medium · M · latency, bandwidth</i></summary>

**Idea.** When blobs or columns for a block are missing, query the local EL first and send RPC requests to peers only for the ones still missing. Share one received-sidecar set between the EL and the p2p fetch paths so no sidecar is fetched twice.

**Gap in Lighthouse.** The subtraction the earlier review asked for already exists: lookups skip columns already in the DA cache, and RPC lookup blocks trigger getBlobs. What is missing is ordering and in-flight sharing: the lookup custody request starts on block download, in parallel with (and before) the EL fetch that runs only after block processing, and ActiveCustodyRequest does not re-check the DA cache to drop columns the EL fills while requests are in flight. Fix: for recent blocks, run getBlobs first (or gate custody_lookup_request on it), and re-filter pending column indices against cached_data_column_indexes before each continue_requests.

**Impact.** Fewer redundant column RPC bytes and KZG verifications during unknown-block lookups when the EL holds the blobs; small on mainnet where gossip usually wins.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context.rs:970-991`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L970-L991) custody_lookup_request filters sampling columns by cached_data_column_indexes (gossip and EL-imported columns are skipped)
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:209-222`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L209-L222) lookup block with MissingComponents triggers fetch_engine_blobs_and_publish_full
- [`beacon_node/network/src/sync/block_lookups/single_block_lookup.rs:398-433`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/single_block_lookup.rs#L398-L433) data request starts as soon as the block is downloaded, not after the EL fetch settles
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1370`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1370) partial-column cell requests wait for local_fetch_settled

**Second check.** Found that custody_lookup_request already dedupes against the DA cache and that sync_methods triggers getBlobs for lookup blocks, so the earlier fix is already there; the remaining gap is that the RPC request is not gated on, or refreshed after, the EL result.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [teku#8663](https://github.com/Consensys-Incorporated/teku/pull/8663), [grandine@a850e357b](https://github.com/grandinetech/grandine/commit/a850e357b76b), [grandine#114](https://github.com/grandinetech/grandine/pull/114), [teku#8927](https://github.com/Consensys-Incorporated/teku/pull/8927)

</details>


<a id="beacon_api-080"></a>
<details>
<summary><b>beacon_api-080</b> Trigger getBlobs on first gossip column sidecar — <i>partial · medium · S · latency, bandwidth</i></summary>

**Idea.** Start the EL getBlobs fetch when the first valid data column sidecar arrives on gossip, also before its block arrives. The missing columns are then built from EL blobs sooner than with a trigger on block arrival only.

**Gap in Lighthouse.** A full Fulu data column sidecar arriving before the block passes gossip verification (it carries the signed header and commitments) but does not trigger getBlobs; only partial headers and blocks do. Fix: in process_gossip_verified_data_column, on the first column for a block root, build a PartialHeaderOrBid::PartialHeader from the column header/commitments and call fetch_engine_blobs_and_publish_full (lighthouse#7329 did this and was closed unmerged).

**Impact.** Saves tens to hundreds of ms when a full column beats the block; only matters for nodes or peers not using partial columns.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1119-1135`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1119-L1135) getBlobs triggered on first uncached partial header
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:926-1024`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L926-L1024) process_gossip_verified_data_column: republishes as partial and processes, MissingComponents only calls check_reconstruction_trigger, no getBlobs
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1242`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1242) BlockRootUnknown for full columns is Gloas-only (needs the bid); Fulu full columns verify without the block
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1936`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1936) trigger on gossip-verified block

**Second check.** Checked that the BlockRootUnknown branch the earlier review cited only fires for Gloas, and that the Fulu full-column success path has no EL trigger; lighthouse#7329 is closed unmerged.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [lighthouse#7329](https://github.com/sigp/lighthouse/pull/7329), [nimbus#8393](https://github.com/status-im/nimbus-eth2/pull/8393)

</details>


<a id="beacon_api-081"></a>
<details>
<summary><b>beacon_api-081</b> Call getBlobs before block verification completes — <i>implemented · high · S · latency, bandwidth</i></summary>

**Idea.** Start the EL getBlobs fetch as soon as a gossip block header is seen, before consensus and execution verification of the block. The local blobs then win the race against gossip and can be published.

**Impact.** The EL fetch runs at the same time as consensus and execution verification, so columns are published early.

**Best measured result.** 116 hits and 156 blobs published in 30 min on mainnet, up from a few hits per hour (pr:lighthouse#6600)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1936`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1936) spawn_fetch_block_columns before chain.process_block
- [`beacon_node/network/src/network_beacon_processor/mod.rs:960`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L960) detached executor.spawn task
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1127`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1127) also triggered by a partial-column header

**Skeptic check.** Confirmed: the fetch starts in a detached task right after gossip validation and does not wait for process_block. It also starts when only a partial-column header is seen. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#6600](https://github.com/sigp/lighthouse/pull/6600)

</details>


<a id="beacon_api-082"></a>
<details>
<summary><b>beacon_api-082</b> Fetch blobs from EL during block lookup sync — <i>partial · low · M · latency, bandwidth</i></summary>

**Idea.** In unknown-block / lookup sync for a block by root, also try engine_getBlobs before requesting blobs or columns from peers. Availability can then resolve locally without RPC.

**Gap in Lighthouse.** SingleBlockLookup::continue_requests issues custody_lookup_request to peers as soon as the block is downloaded. The getBlobs call (fetch_engine_blobs_and_publish_full in process_rpc_block) runs only after process_block completes. The peer column RPC is therefore never skipped when the EL has the blobs. Lodestar calls getBlobs before each peer by-root request. The missing step is to gate the custody request on an EL attempt, or to re-check the DA cache before the request is sent.

**Impact.** Saves column RPC bandwidth on lookups when the EL holds the blobs. Availability already resolves locally, so latency barely changes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:208`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L208) EL fetch only after lookup process_block returns MissingComponents
- [`beacon_node/network/src/sync/block_lookups/single_block_lookup.rs:398`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/single_block_lookup.rs#L398) DataRequest moves to Request and custody_lookup_request is sent as soon as the block is downloaded, in parallel with block processing
- [`beacon_node/network/src/sync/network_context.rs:971`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L971) cached_data_column_indexes is checked once, when the request is made, before the EL result exists

**Skeptic check.** The earlier evidence is right that lookup blocks try the EL. It is wrong that this happens before the peer request: the column RPC is sent at the same time and is not cancelled.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lodestar#7724](https://github.com/ChainSafe/lodestar/pull/7724)

</details>


<a id="beacon_api-083"></a>
<details>
<summary><b>beacon_api-083</b> Fetch EL blobs for blocks published via API — <i>implemented · medium · S · latency, bandwidth</i></summary>

**Idea.** When a block is published through the HTTP API without blob data, still trigger the EL getBlobs fetch and the column requests for it, because later gossip duplicates of the block are ignored.

**Impact.** Blocks published through the API without blobs still get EL blobs and partial-column requests.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/publish_blocks.rs:172`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L172) fetch_columns when request has no blobs and no locally cached payload blobs
- [`beacon_node/http_api/src/publish_blocks.rs:221`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L221) NetworkMessage::FetchBlockColumns after gossip publish
- [`beacon_node/network/src/service.rs:692`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L692) spawn_fetch_block_columns with EnvelopeSource::Http

**Skeptic check.** Confirmed: the publish closure starts the same EL fetch and partial-column retrieval that gossip blocks use. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#10396](https://github.com/sigp/lighthouse/pull/10396)

</details>


<a id="beacon_api-084"></a>
<details>
<summary><b>beacon_api-084</b> Use existence-only EL blob query — <i>not · medium · M · latency, bandwidth</i></summary>

**Idea.** Use an existence-only Engine API call (HasBlobs) to learn which blobs the EL holds, so held cells can be advertised to peers at once without the slower full getBlobs round trip.

**Gap in Lighthouse.** No existence-only Engine API call (HasBlobs or similar bitmap query) and no early advertisement of held cells before the full getBlobs response. Fix: add the method in execution_layer and use its bitmap to set present cells in the partial assembler early. Needs EL support.

**Impact.** Lets partial-column peers learn held cells one EL round trip earlier; tens of ms on propagation.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engine_api/http.rs:71-73`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L71-L73) only engine_getBlobsV2/V3/V4 constants
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:398-460`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L398-L460) V4 path fetches cells and proofs

**Second check.** Searched execution_layer and fetch_blobs for has_blobs, blobs_exist, bitmap and availability queries; only the getBlobs family exists.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [prysm#16774](https://github.com/OffchainLabs/prysm/pull/16774)

</details>


<a id="beacon_api-085"></a>
<details>
<summary><b>beacon_api-085</b> Fill partial column cells from EL blobs — <i>implemented · medium · S · latency, bandwidth</i></summary>

**Idea.** On a partial data column header, fetch the matching blobs from the EL (getBlobsV3) and fill the cell assembly locally. Fewer cells must come from peers.

**Impact.** Partial-column cells are filled locally from the EL on header receipt, so fewer cells come from peers.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1123`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1123) first-seen partial header triggers fetch_engine_blobs_and_publish_full
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:161`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L161) getBlobsV4 (custody cells only) with V2/V3 fallback at :190
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:333`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L333) EL cells merged into the PartialDataColumnAssembler
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:267`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L267) V3 partial responses are still used

**Skeptic check.** Confirmed the gossip partial-header path calls the EL and merges the returned cells into the assembler, with V3 partial responses accepted. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [silver#292](https://github.com/gattaca-com/silver/pull/292), [prysm#16324](https://github.com/OffchainLabs/prysm/pull/16324)

</details>


<a id="beacon_api-086"></a>
<details>
<summary><b>beacon_api-086</b> Run blob tracker only for gossip blocks — <i>partial · low · S · cpu, bandwidth</i></summary>

**Idea.** Start post-import fetch of missing blobs/columns (EL or peers) only for blocks that arrived via gossip, not for blocks imported by sync or other paths.

**Gap in Lighthouse.** Range-sync and backfill paths already do not fetch from the EL, so waste is limited. Lighthouse also fetches for RPC lookup blocks (publish_blobs=false), which is deliberate. Dropping that would only avoid one EL call per lookup block.

**Impact.** Little to gain: only lookup-sourced blocks differ and the extra EL call there can save a peer download.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1936`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1936) gossip block triggers spawn_fetch_block_columns
- [`beacon_node/network/src/service.rs:697`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L697) HTTP-published block triggers it
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:214`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L214) RPC lookup block with MissingComponents also triggers EL fetch
- range sync/chain segment path does not call it

**Sources.** [lodestar#9322](https://github.com/ChainSafe/lodestar/pull/9322)

</details>


<a id="beacon_api-087"></a>
<details>
<summary><b>beacon_api-087</b> Skip EL reconstruction when nothing is missing — <i>partial · low · S · cpu</i></summary>

**Idea.** Skip the EL getBlobs/sidecar build routine when the block has no KZG commitments or all its blobs or columns were already seen on gossip. This avoids needless engine calls and sidecar building.

**Gap in Lighthouse.** Add a guard in fetch_and_process_engine_blobs_inner (or fetch_engine_blobs_and_publish_full) that returns early when the DA checker/partial assembler already holds all custody columns for block_root, before calling get_blobs_v4/v3/v2.

**Impact.** Saves an engine call, and cell/proof processing, only when all columns arrived before the EL fetch. This is rare since the fetch starts at block arrival.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:144`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L144) returns early when versioned_hashes is empty
- [`beacon_node/network/src/network_beacon_processor/mod.rs:1020`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L1020) no check of already-seen columns before calling the EL
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:531`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L531) dedupe against gossip/DA cache only after the EL response

**Sources.** [prysm#14915](https://github.com/OffchainLabs/prysm/pull/14915)

</details>


<a id="beacon_api-088"></a>
<details>
<summary><b>beacon_api-088</b> Build only custodied columns from EL blobs — <i>partial · medium · S · cpu, memory</i></summary>

**Idea.** When data column sidecars are built from EL blobs, compute only the columns that the node custodies (column bitmap), not all 128 columns that are then filtered.

**Gap in Lighthouse.** Only the V4 path is custody-scoped. The V2/V3 fallback builds all 128 partial columns, then filters to custody and then dedupes against observed and cached columns. Fix: pass the custody indices minus already-known columns into blobs_to_partial_data_columns and build only those columns (cell computation via compute_cells still covers the whole blob).

**Impact.** Saves column assembly work and allocations per block on V2/V3 ELs for non-supernodes; cell FFT cost stays, so modest.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:158`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L158) V4 path requests only custody columns from the EL
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:686-705`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L686-L705) V2/V3 path calls blobs_to_partial_data_columns for all columns, then filters by custody_columns_indices
- [`beacon_node/beacon_chain/src/kzg_utils.rs:425-472`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L425-L472) blobs_to_partial_data_columns computes all cells and builds every column, no index parameter

**Second check.** Re-read the builder and the V2/V3 path; the custody filter and the observed/cached dedupe both run after all columns are built.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [nimbus#8672](https://github.com/status-im/nimbus-eth2/pull/8672)

</details>


<a id="beacon_api-089"></a>
<details>
<summary><b>beacon_api-089</b> Publish recovered columns off the availability path — <i>partial · low · M · latency, bandwidth</i></summary>

**Idea.** Publish columns recovered from EL blobs or reconstruction in a detached task after storing them, so block import and DA completion do not wait on network sends. Coalesce repeated partial publishes per (block, column).

**Gap in Lighthouse.** Recovered full columns are published in a detached task, so this half is done. Partial-column republishes are not coalesced: each merged partial update in process_gossip_partial_data_column (gossip_methods.rs:1404/1421) calls PublishPartialColumns -&gt; Network::publish_partial at once. Prysm batches these over a 250 ms window per (block, column).

**Impact.** Import and DA do not wait on network sends. Coalescing would reduce partial-column protocol chatter when partial columns are enabled.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:357`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L357) publish_fn called before process_engine_blobs_fulu, but it only spawns
- [`beacon_node/network/src/network_beacon_processor/mod.rs:1263`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L1263) publish_data_columns_gradually runs in a detached executor.spawn task
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1404`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1404) every partial merge immediately sends PublishPartialColumns
- [`beacon_node/lighthouse_network/src/service/mod.rs:907`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L907) publish_partial forwards each message to gossipsub with no per-(block,column) batching

**Skeptic check.** Verified the detached publish on the EL and reconstruction paths. The earlier evidence itself said no coalescing was found, which the idea explicitly includes, so 'implemented' was too strong.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [nimbus#8655](https://github.com/status-im/nimbus-eth2/pull/8655), [prysm#17791](https://github.com/OffchainLabs/prysm/pull/17791)

</details>


<a id="beacon_api-090"></a>
<details>
<summary><b>beacon_api-090</b> Publish only needed recovered columns — <i>implemented · medium · S · cpu, bandwidth</i></summary>

**Idea.** When recovered columns are redistributed to gossip, publish only the columns that the network still needs instead of all of them.

**Impact.** Only custody columns not yet seen are published, in shuffled delayed batches, which cuts outbound bandwidth.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:697`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L697) EL columns filtered to custody columns before import and publish
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:720`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L720) columns already observed on gossip or known to DA are dropped
- [`beacon_node/network/src/network_beacon_processor/mod.rs:1298`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L1298) each gradual batch re-filtered with observe_gossip_data_column, PriorKnown dropped

**Skeptic check.** Nimbus#8648 restricts redistribution to custody columns. Lighthouse does this, drops already-seen columns, and also re-checks before each batch. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#8648](https://github.com/status-im/nimbus-eth2/pull/8648)

</details>


<a id="beacon_api-091"></a>
<details>
<summary><b>beacon_api-091</b> Mark data available at 50% columns — <i>not · medium · M · latency, bandwidth, sync</i></summary>

**Idea.** On nodes that custody all columns, treat a block as data-available once at least 50% of columns are verified (enough to reconstruct), and import it before reconstruction of the rest completes.

**Gap in Lighthouse.** Let make_available (Fulu overflow_lru_cache and Gloas pending_components) return available once &gt;= NUMBER_OF_COLUMNS/2 verified columns are held on full-custody nodes, import the block, and finish reconstruction/custody storage of the remaining columns in the background; DB/RPC serving must handle columns arriving after import. PR #7598 was closed unmerged.

**Impact.** Supernodes import without waiting for reconstruction (and its scheduled delay) when only about half the columns have arrived; saves hundreds of ms on such blocks, only on nodes custodying &gt;= 64 columns.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:212-234`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L212-L234) make_available requires received == num_of_data_columns_to_sample (Ordering::Equal), Less =&gt; None
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:620`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L620) total/2 only gates reconstruction start
- [`beacon_node/beacon_chain/src/pending_payload_cache/pending_components.rs:218-220`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/pending_components.rs#L218-L220) Gloas is_blob_data_available also needs &gt;= full sampling count
- [`beacon_node/beacon_chain/src/pending_payload_cache/mod.rs:643`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/mod.rs#L643) Gloas 50% only gates reconstruction
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3785-3870`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3785-L3870) import after 50% happens only via reconstruct_data_columns -&gt; process_availability, i.e. after reconstruction completes

**Second check.** Also checked the Gloas pending_payload_cache path and the reconstruction-to-import flow in beacon_chain.rs; both require the full sampling count before import, so the 50% threshold is never an availability shortcut.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [nimbus#8417](https://github.com/status-im/nimbus-eth2/pull/8417), [lighthouse#7598](https://github.com/sigp/lighthouse/pull/7598), [teku#10248](https://github.com/Consensys-Incorporated/teku/pull/10248), [grandine#424](https://github.com/grandinetech/grandine/pull/424), [lodestar#8408](https://github.com/ChainSafe/lodestar/pull/8408), [lodestar#8818](https://github.com/ChainSafe/lodestar/pull/8818)

</details>


<a id="beacon_api-092"></a>
<details>
<summary><b>beacon_api-092</b> Reconstruct remaining columns from half — <i>implemented · medium · S · cpu, latency, bandwidth, sync</i></summary>

**Idea.** Once at least 50% of data columns for a block are held, recover the missing columns by erasure-coding reconstruction (cell recovery), store and publish them, instead of downloading every column.

**Impact.** Supernodes recover all columns from half, import and republish them.

**Best measured result.** &lt;800ms to recover with 20 blobs (pr:lodestar#7940)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:611-639`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L611-L639) check_and_set_reconstruction_started requires received &gt;= total/2 and &lt; sampling count
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:537-620`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L537-L620) reconstruct_data_columns imports only sampled, not-yet-held columns
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3785-3870`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3785-L3870) reconstruct then process_availability
- [`beacon_node/network/src/network_beacon_processor/mod.rs:1213-1217`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L1213-L1217) attempt_data_column_reconstruction publishes recovered columns (publish_data_columns_gradually)
- [`beacon_node/beacon_chain/src/custody_context.rs:492-497`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L492-L497) should_attempt_reconstruction only when sampling &gt; 50%

**Skeptic check.** Verified the full chain: gossip column -&gt; check_reconstruction_trigger -&gt; delayed reconstruction -&gt; recover -&gt; import + gradual publish. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#5781](https://github.com/sigp/lighthouse/pull/5781), [prysm#15454](https://github.com/OffchainLabs/prysm/pull/15454), [lodestar#7940](https://github.com/ChainSafe/lodestar/pull/7940), [lodestar#7935](https://github.com/ChainSafe/lodestar/pull/7935), [teku#10224](https://github.com/Consensys-Incorporated/teku/pull/10224), [prysm#17053](https://github.com/OffchainLabs/prysm/pull/17053)

</details>


<a id="beacon_api-093"></a>
<details>
<summary><b>beacon_api-093</b> Delay column reconstruction to wait for gossip — <i>implemented · low · S · cpu, latency, sync</i></summary>

**Idea.** Wait a short configurable time before starting column reconstruction (longer while syncing), because the missing columns often arrive via gossip or getBlobs and reconstruction is CPU-heavy.

**Impact.** Debounced reconstruction avoids redundant KZG recovery when gossip or getBlobs completes the set.

**Best measured result.** reduces the unnecessary amount of reconstructions during fast block import (commit:grandine@9e43a4aea5ad)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:73`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L73) QUEUED_RECONSTRUCTION_DELAY 150ms
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:1139-1166`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L1139-L1166) delay reset on every new column for the root, zero after 1/4-slot deadline
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1488-1520`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1488-L1520) check_reconstruction_trigger schedules instead of running

**Skeptic check.** Delay is a fixed debounce, not configurable or sync-dependent; Lighthouse only triggers reconstruction from gossip columns, so the grandine sync case (fast block import) does not arise. Earlier verdict upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#7588](https://github.com/sigp/lighthouse/pull/7588), [grandine@9e43a4aea](https://github.com/grandinetech/grandine/commit/9e43a4aea5ad), [grandine#526](https://github.com/grandinetech/grandine/pull/526), [grandine@4f7f8f0ae](https://github.com/grandinetech/grandine/commit/4f7f8f0ae248)

</details>


<a id="beacon_api-094"></a>
<details>
<summary><b>beacon_api-094</b> Cap reconstruction debounce delay — <i>not · low · S · cpu, latency</i></summary>

**Idea.** Put a hard maximum (for example 1 s from first enqueue) on the debounced delay before column reconstruction, so repeated column arrivals cannot postpone reconstruction and publication indefinitely.

**Gap in Lighthouse.** Track first-enqueue time per block_root in queued_column_reconstructions and skip reset (or cap the delay at about 1s from first enqueue) in the DelayColumnReconstruction arm.

**Impact.** Only affects supernodes. It bounds reconstruction postponement under a steady stream of columns, but the 150ms window and the 1/4-slot deadline already limit it.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:1139`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L1139) DelayColumnReconstruction handler
- work_reprocessing_queue.rs:1157 delay_queue.reset(delay_key, reconstruction_delay) on every arrival with no cap on total delay
- work_reprocessing_queue.rs:1148 delay set to 0 only after the 1/4-slot deadline
- lighthouse#7702 was closed, not merged

**Sources.** [lighthouse#7702](https://github.com/sigp/lighthouse/pull/7702)

</details>


<a id="beacon_api-095"></a>
<details>
<summary><b>beacon_api-095</b> Dynamic reconstruction timeout, none on non-supernodes — <i>implemented · low · S · cpu</i></summary>

**Idea.** Compute the reconstruction timeout dynamically, and do not run column reconstruction on nodes that do not custody enough columns.

**Impact.** Non-supernodes never reconstruct, and the delay adapts to the slot position.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/custody_context.rs:492`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L492) should_attempt_reconstruction requires sampling count &gt; NUMBER_OF_COLUMNS/2
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1488`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1488) check_reconstruction_trigger gated by it; it is the only caller of attempt_data_column_reconstruction
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:1139`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L1139) delay 150ms, or 0 after the 1/4-slot deadline, derived from slot duration

**Skeptic check.** Checked that every reconstruction entry point goes through the custody gate and that the delay scales with the slot duration. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#7628](https://github.com/status-im/nimbus-eth2/pull/7628)

</details>


<a id="beacon_api-096"></a>
<details>
<summary><b>beacon_api-096</b> Run column reconstruction once per block — <i>partial · medium · M · cpu, memory, disk</i></summary>

**Idea.** Record the block roots for which column reconstruction was dispatched, is in flight or is complete, and skip new reconstruction requests for them. Share one reconstruction result across concurrent requesters.

**Gap in Lighthouse.** Only the gossip column-reconstruction path is deduplicated. The API blob paths (BlockId::get_blobs_by_versioned_hashes and the PeerDAS branch of get_blinded_block_and_blob_list_filtered) rerun reconstruct_blobs -&gt; recover_cells_and_compute_kzg_proofs for every request on a semi-supernode/partial-custody node, with no in-flight sharing and no result cache; concurrent requests for the same block (e.g. several rollups/L2 indexers) each pay the full recovery.

**Impact.** On semi-supernodes serving /eth/v1/beacon/blobs, N concurrent requests for a recent block cost N full cell recoveries (~hundreds of ms of CPU each with many blobs); a shared per-root future/short-lived cache would make it one.

**Best measured result.** duplicate rate 4-6% to 0 in test (pr:lighthouse#8985)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:592-639`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L592-L639) reconstruction_started flag set under write lock (gossip path dedup)
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:1153-1166`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L1153-L1166),1357-1361 per-root queue entry, None marks dispatched (pruned on the next dispatch)
- [`beacon_node/http_api/src/block_id.rs:433-447`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L433-L447) get_blobs_by_versioned_hashes calls reconstruct_blobs on every request
- [`beacon_node/http_api/src/block_id.rs:501-534`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L501-L534) get_data_columns_for_blob_reconstruction reads columns from DB per request
- [`beacon_node/beacon_chain/src/kzg_utils.rs:767-822`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L767-L822) reconstruct_blobs_with_indices runs recover_cells_and_compute_kzg_proofs per blob when fewer than 128 columns held

**Skeptic check.** Gossip-path dedup via reconstruction_started is real and the earlier evidence for it is right. The idea's 'share one result across concurrent requesters' (teku#11508) is about request-driven reconstruction, which Lighthouse's API does per request with no sharing.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lighthouse#8855](https://github.com/sigp/lighthouse/pull/8855), [lighthouse#8923](https://github.com/sigp/lighthouse/pull/8923), [lighthouse#8985](https://github.com/sigp/lighthouse/pull/8985), [lodestar#8383](https://github.com/ChainSafe/lodestar/pull/8383), [teku#11508](https://github.com/Consensys-Incorporated/teku/pull/11508), [teku#10296](https://github.com/Consensys-Incorporated/teku/pull/10296)

</details>


<a id="beacon_api-097"></a>
<details>
<summary><b>beacon_api-097</b> Dedicated thread pool for column reconstruction — <i>partial · medium · M · cpu, latency</i></summary>

**Idea.** Run data column computation and cell recovery on a dedicated (high-priority) thread pool, separate from the general pool and the fork choice/block import threads, so heavy KZG work does not starve other tasks.

**Gap in Lighthouse.** Only DataAvailabilityChecker::reconstruct_data_columns (and the Gloas equivalent) run in the scoped HighPriority pool. Column computation (compute_cells in blobs_to_data_column_sidecars / blobs_to_partial_data_columns from fetch_blobs::compute_custody_columns_to_import and publish_blocks::build_data_columns) runs on the global rayon pool shared with other parallel work, and API-driven recovery in kzg_utils::reconstruct_blobs runs on a generic blocking thread. The high-priority pool is also not isolated (80% of CPUs, overlapping the global pool).

**Impact.** Under load, getBlobs column computation and API recovery compete with other global-pool rayon work; grandine reports lower p99 from moving both compute_cells and recovery to a dedicated executor.

**Best measured result.** reduces p99 latency during high load (commit:grandine@9af9e4de859b)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:3811`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3811),3845 reconstruction on RayonPoolType::HighPriority
- [`common/task_executor/src/rayon_pool_provider.rs:4-56`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/task_executor/src/rayon_pool_provider.rs#L4-L56) high pool = 80% of CPUs, 'critical tasks use the global pool'
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:656-690`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L656-L690) compute_custody_columns_to_import: spawn_blocking_handle + into_par_iter compute_cells on the global rayon pool
- [`beacon_node/http_api/src/publish_blocks.rs:440-470`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L440-L470) build_data_sidecars via spawn_blocking on global pool
- [`beacon_node/beacon_chain/src/kzg_utils.rs:400-420`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L400-L420) compute_cells into_par_iter (global pool)
- [`beacon_node/http_api/src/block_id.rs:437`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L437) API reconstruct_blobs runs on a beacon-processor blocking thread

**Skeptic check.** PR 8075 is real but covers reconstruction only, described as a stopgap. Earlier verdict overlooked compute_cells on the getBlobs and publish paths; whether the global pool is actually contended there is unmeasured.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [grandine@9af9e4de8](https://github.com/grandinetech/grandine/commit/9af9e4de859b), [grandine@79f20c521](https://github.com/grandinetech/grandine/commit/79f20c52179d), [grandine#362](https://github.com/grandinetech/grandine/pull/362), [lighthouse#8075](https://github.com/sigp/lighthouse/pull/8075)

</details>


<a id="beacon_api-098"></a>
<details>
<summary><b>beacon_api-098</b> Run KZG reconstruction off async and fork-choice threads — <i>partial · medium · S · cpu, latency</i></summary>

**Idea.** Call PeerDAS KZG and reconstruction functions in blocking tasks or async jobs off the caller, async runtime and single-threaded fork choice mutator. Do not spawn a new validation task per column for the same delayed block.

**Gap in Lighthouse.** RPC custody columns (single-block lookups and custody requests) are KZG batch-verified inside an async task on the tokio runtime: NetworkBeaconProcessor::process_rpc_custody_columns -&gt; BeaconChain::process_rpc_custody_columns -&gt; check_rpc_custody_columns_availability_and_import -&gt; DataAvailabilityChecker::put_rpc_custody_columns -&gt; KzgVerifiedDataColumn::from_batch_with_scoring (and PendingPayloadCache::put_rpc_custody_columns for Gloas), with no spawn_blocking. Gossip, partial and reconstruction paths are correctly offloaded.

**Impact.** A by-root response of many columns x many blobs (tens of ms of KZG) blocks a tokio worker, delaying networking and other async tasks during lookup sync bursts.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2451-2475`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2451-L2475) gossip column verification in spawn_blocking_handle
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2514-2541`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2514-L2541) partial column verification in spawn_blocking_handle
- [`beacon_node/network/src/network_beacon_processor/mod.rs:619-633`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L619-L633) send_rpc_custody_columns wraps work as async Work::RpcCustodyColumn
- [`beacon_node/beacon_processor/src/lib.rs:1701-1703`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1701-L1703) RpcCustodyColumn -&gt; task_spawner.spawn_async
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4264-4304`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4264-L4304) check_rpc_custody_columns_availability_and_import calls put_rpc_custody_columns inline in async fn
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:350-360`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L350-L360) put_rpc_custody_columns runs KzgVerifiedDataColumn::from_batch_with_scoring (batch cell-proof KZG) synchronously

**Skeptic check.** Earlier evidence checked only the gossip and reconstruction paths; the RPC custody column path verifies KZG on an async worker thread. Fork choice is not involved in KZG in any path.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [teku#9728](https://github.com/Consensys-Incorporated/teku/pull/9728), [grandine@5d83807db](https://github.com/grandinetech/grandine/commit/5d83807db95f), [grandine@e53a535e1](https://github.com/grandinetech/grandine/commit/e53a535e114c)

</details>


<a id="beacon_api-099"></a>
<details>
<summary><b>beacon_api-099</b> Bound parallelism of per-blob cell recovery — <i>partial · low · S · cpu, memory</i></summary>

**Idea.** Run per-blob cell recovery on worker tasks with a bounded number in flight, zero-copy views of inputs and reused buffers, instead of spawning one task per blob. This limits peak memory and scheduling overhead.

**Gap in Lighthouse.** Parallelism is rayon-bounded by pool size, not one task per blob, so peak in-flight is limited. Missing: reused buffers and fully zero-copy inputs (cell_ids.to_vec(), cells.to_vec() per blob).

**Impact.** Small allocation savings during supernode reconstruction; negligible for non-supernodes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/kzg_utils.rs:889`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L889) reconstruct_data_columns uses into_par_iter over blobs (rayon, bounded by pool threads)
- beacon_node/crypto/kzg/src/lib.rs:307 recover_cells_and_compute_kzg_proofs takes cell refs but to_vec()s inputs

**Sources.** [nimbus#7758](https://github.com/status-im/nimbus-eth2/pull/7758), [nimbus#7800](https://github.com/status-im/nimbus-eth2/pull/7800), [prysm#14397](https://github.com/OffchainLabs/prysm/pull/14397)

</details>


<a id="beacon_api-100"></a>
<details>
<summary><b>beacon_api-100</b> Semi-supernode: custody half the columns — <i>implemented · medium · S · cpu, disk, bandwidth</i></summary>

**Idea.** Offer a mode that custodies and subscribes to 64 of 128 column subnets, enough to reconstruct all blobs, to serve blobs with about half the bandwidth and storage of a supernode.

**Impact.** Half the column bandwidth/storage of a supernode while still serving blobs.

**Best measured result.** Storage ~50% vs supernode (64 vs 128 columns) (pr:prysm#16029)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/src/cli.rs:63-64`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L63-L64) --semi-supernode
- [`beacon_node/src/config.rs:130-134`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/config.rs#L130-L134) semi-supernode sets custody override
- [`beacon_node/beacon_chain/src/custody_context.rs:43-44`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L43-L44) cgc override (number_of_custody_groups/2)
- [`beacon_node/beacon_chain/src/custody_context.rs:492-497`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L492-L497) no reconstruction at exactly 50%
- [`beacon_node/http_api/src/block_id.rs:501-534`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L501-L534) blobs served by reconstruction from &gt;=64 columns

**Skeptic check.** Mode exists and the blob API reconstructs from 64 columns. The per-request recovery cost on that API path is covered under beacon_api-096.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#16029](https://github.com/OffchainLabs/prysm/pull/16029), [grandine@5ff11c24d](https://github.com/grandinetech/grandine/commit/5ff11c24d141), [lodestar#8568](https://github.com/ChainSafe/lodestar/pull/8568)

</details>


<a id="beacon_api-101"></a>
<details>
<summary><b>beacon_api-101</b> Custody first half of columns to skip reconstruction — <i>not · low · L · cpu, bandwidth</i></summary>

**Idea.** Custody the first 64 columns, which hold the original blob data, so blobs can be served directly without reconstruction CPU cost.

**Gap in Lighthouse.** Custody columns are derived from node id per spec (random order list); not chosen as the first 64. Spec mandates derived custody, so a client cannot pick columns freely without breaking peer expectations.

**Impact.** Would avoid reconstruction CPU only for blob serving; spec-incompatible as a default, so low real value.

**Best measured result.** avoids reconstruction CPU load (pr:nimbus#7752)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/custody_context.rs:507`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L507) sampling_columns_for_epoch slices ordered_custody_column_indices
- [`beacon_node/beacon_chain/src/custody_context.rs:1233`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L1233) generate_data_column_indices_rand_order

**Sources.** [nimbus#7752](https://github.com/status-im/nimbus-eth2/pull/7752)

</details>


<a id="beacon_api-102"></a>
<details>
<summary><b>beacon_api-102</b> Background reconstruction of historical custody columns — <i>not · low · M · cpu, disk, bandwidth</i></summary>

**Idea.** Run a background service that reconstructs missing custody columns from stored half-sets for recent history, walking from head back to the retention floor, so full columns can be served without download.

**Gap in Lighthouse.** Add a background task that walks from head to the data column retention floor, finds blocks with at least 64 but fewer than custody columns stored, calls kzg_utils::reconstruct_data_columns and stores the results.

**Impact.** Only helps nodes with half-sets on disk (semi-supernode/supernode after custody changes). It saves peer downloads for serving historic columns. Niche.

**Evidence (Lighthouse @ 928b61e719).**

- searched [`beacon_node/beacon_chain`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain), store, network for background column reconstruction; only block-time reconstruct_data_columns (data_availability_checker.rs:537) and historic state reconstruction (store/src/reconstruct.rs) exist
- [`beacon_node/http_api/src/block_id.rs:501`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L501) stores only keys present; no backfill of missing custody columns

**Sources.** [nimbus#8533](https://github.com/status-im/nimbus-eth2/pull/8533)

</details>


<a id="beacon_api-103"></a>
<details>
<summary><b>beacon_api-103</b> Reconstruct API blobs from stored columns — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Serve blob sidecars in the blobs API by reconstructing them from stored data column sidecars once at least half are held, and hold sidecars as Arc to avoid copies.

**Impact.** Blobs API already serves blobs rebuilt from stored columns, with columns held as Arc.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/block_id.rs:367`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L367) blob_sidecars reconstructs from columns post-PeerDAS
- [`beacon_node/http_api/src/block_id.rs:430`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L430) blobs-by-versioned-hash endpoint does the same
- [`beacon_node/http_api/src/block_id.rs:494`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L494) get_data_columns_for_blob_reconstruction requires &gt;= 64 stored columns, returns Vec&lt;Arc&lt;DataColumnSidecar&gt;&gt;
- [`beacon_node/beacon_chain/src/kzg_utils.rs:767`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L767) reconstruct_blobs_with_indices

**Skeptic check.** Verified both blob endpoints. A minor extra cost remains: below 128 columns, kzg_utils.rs:799 calls recover_cells_and_compute_kzg_proofs and throws away the proofs. That is beyond the idea's scope. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine#314](https://github.com/grandinetech/grandine/pull/314), [lighthouse#8103](https://github.com/sigp/lighthouse/pull/8103)

</details>


<a id="beacon_api-104"></a>
<details>
<summary><b>beacon_api-104</b> Share blobs and cells by Arc, not copy — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Hold blobs, sidecars and partial-column cells behind Arc/shared references on the heap and pass them by reference to KZG and caches, so each clone does not copy 128 KiB.

**Impact.** Sidecar clones are refcount bumps across gossip, RPC, DA cache and KZG.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/data/data_column_sidecar.rs:47`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/data/data_column_sidecar.rs#L47) DataColumnSidecarList = Vec&lt;Arc&lt;DataColumnSidecar&gt;&gt;
- [`consensus/types/src/data/blob_sidecar.rs:296`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/data/blob_sidecar.rs#L296) BlobSidecarList = RuntimeVariableList&lt;Arc&lt;BlobSidecar&gt;&gt;
- [`beacon_node/beacon_chain/src/blob_verification.rs:15-19`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/blob_verification.rs#L15-L19) KzgVerifiedBlob holds Arc&lt;BlobSidecar&gt;
- [`beacon_node/beacon_chain/src/data_column_verification.rs:484-487`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L484-L487) KzgVerifiedDataColumn holds Arc&lt;DataColumnSidecar&gt;
- [`beacon_node/beacon_chain/src/kzg_utils.rs:767-795`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L767-L795) recovery uses KzgCellRef references
- [`beacon_node/beacon_chain/src/block_production/gloas.rs:919-925`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/gloas.rs#L919-L925) pending envelope blobs behind Arc

**Skeptic check.** Remaining blob.clone() calls (http_api/src/block_id.rs:451) build API responses, not hot-path sharing. Earlier verdict upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#4593](https://github.com/sigp/lighthouse/pull/4593), [nimbus#9081](https://github.com/status-im/nimbus-eth2/pull/9081), [lighthouse#4980](https://github.com/sigp/lighthouse/pull/4980)

</details>


<a id="beacon_api-105"></a>
<details>
<summary><b>beacon_api-105</b> Store a blob as one flat byte array — <i>n/a · low · memory</i></summary>

**Idea.** Represent a blob as one flat byte array instead of a 2D slice of 32-byte field elements, removing a slice header per element.

**Impact.** No Go slice headers in Rust; blob cells are fixed arrays.

**Best measured result.** 24-byte slice header overhead per 32-byte element avoided (pr:prysm#11614)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:176`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L176) blobs held as Arc'd sidecars, no 2D slice

**Sources.** [prysm#11614](https://github.com/OffchainLabs/prysm/pull/11614)

</details>


<a id="beacon_api-106"></a>
<details>
<summary><b>beacon_api-106</b> Assemble partial columns in-place in ring buffer — <i>partial · low · L · memory, latency, bandwidth</i></summary>

**Idea.** Write cells from partial column messages directly into a preallocated ring buffer with per-row sub-reservations, and send per-peer cell messages from it, so there are no intermediate copies.

**Gap in Lighthouse.** Lighthouse supports partial columns but assembles them in per-column heap structures, not a preallocated ring buffer with gather writes. Would need a cell arena in PartialDataColumnAssembler plus a send path that reads from it.

**Impact.** Removes a few cell copies per partial column; small versus KZG and network cost.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/partial_data_column_assembler.rs:11`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/partial_data_column_assembler.rs#L11) PartialDataColumnAssembler merges partial columns into LRU of HashMap&lt;ColumnIndex,AssemblyColumn&gt;
- beacon_chain/src/fetch_blobs/mod.rs:380 merge_partial_data_columns

**Sources.** [silver#242](https://github.com/gattaca-com/silver/pull/242), [silver#245](https://github.com/gattaca-com/silver/pull/245)

</details>


<a id="beacon_api-107"></a>
<details>
<summary><b>beacon_api-107</b> Quarantine blobs and blobless blocks until joined — <i>implemented · medium · S · memory, latency</i></summary>

**Idea.** Keep gossip blobs and blocks whose blobs are missing in a quarantine and import when both are present, instead of dropping the block and requesting it again.

**Impact.** Blocks and blobs/columns wait in the DA cache until joined, so nothing is dropped and fetched again.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:442`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L442) put_kzg_verified_blobs caches blobs without a block
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:557`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L557) update_or_insert_pending_components
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:192`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L192) merge_block revalidates cached blobs
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:200`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L200) make_available joins once complete

**Skeptic check.** The DA checker's pending-components cache is exactly this quarantine-and-join mechanism. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#4808](https://github.com/status-im/nimbus-eth2/pull/4808)

</details>


<a id="beacon_api-108"></a>
<details>
<summary><b>beacon_api-108</b> Cache columns with unknown parent block — <i>not · medium · M · latency, sync</i></summary>

**Idea.** Cache data column sidecars whose parent block is unknown and validate them when the parent arrives, instead of discarding and fetching them again.

**Gap in Lighthouse.** On ParentUnknown, keep the column sidecar in a bounded cache keyed by block root (or hand it to the child lookup as a real component) and re-run gossip/KZG verification once the parent imports, like the BlockRootUnknown reprocessing path; touches gossip_methods, SyncMessage::UnknownParentSidecarHeader/BlockComponent::Sidecar and the lookup download logic.

**Impact.** Avoids re-fetching columns by RPC after a parent lookup on the rare unknown-parent path; small bandwidth/latency gain, mainly after reorgs or missed blocks.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:764-776`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L764-L776) ParentUnknown column: only sends UnknownParentSidecarHeader, the sidecar is not kept
- [`beacon_node/network/src/sync/manager.rs:151-159`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L151-L159) UnknownParentSidecarHeader carries only header info, no sidecar
- [`beacon_node/network/src/sync/manager.rs:903-919`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L903-L919) handled as BlockComponent::Sidecar (no data)
- [`beacon_node/network/src/sync/block_lookups/single_block_lookup.rs:340-344`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/single_block_lookup.rs#L340-L344) Sidecar component inserts nothing; lookup re-downloads its columns itself
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:148`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L148) reprocessing queue only covers UnknownBlockDataColumn (block-root unknown), not parent unknown

**Second check.** Followed the sync path beyond gossip_methods: the sync message and the lookup's BlockComponent::Sidecar explicitly carry no data, and the lookup comment says it downloads the columns itself; the reprocessing queue only handles unknown block roots.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [silver#157](https://github.com/gattaca-com/silver/pull/157)

</details>


<a id="beacon_api-109"></a>
<details>
<summary><b>beacon_api-109</b> Index sidecar quarantine by root and slot — <i>implemented · low · S · cpu</i></summary>

**Idea.** Index the blob/column quarantine by block root and slot for O(1) lookups, and use one pop returning an Option instead of has-then-pop double access.

**Impact.** Quarantine lookups are O(1) by root with no has-then-pop pattern.

**Best measured result.** Stated: API calls go from O(n) to O(1) (pr:nimbus#7100)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:351`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L351) LruCache&lt;Hash256, PendingComponents&gt; keyed by block root
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:382`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L382),400,419,434,597 single peek/get_mut by root returning Option
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:724`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L724) only full iteration is epoch pruning

**Skeptic check.** No slot-keyed lookups into the DA cache exist on hot paths (the API reads the store), so the lack of a slot index costs nothing. Earlier verdict upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#7100](https://github.com/status-im/nimbus-eth2/pull/7100)

</details>


<a id="beacon_api-110"></a>
<details>
<summary><b>beacon_api-110</b> Cache custody column set per node — <i>implemented · low · S · cpu</i></summary>

**Idea.** Compute the custody and sampling column indices for the node id once, store them as a hash set (swapped atomically when custody count changes), and use it for O(1) membership checks.

**Impact.** None left. Column order is computed once per node id and only sliced by the custody count of the epoch. Membership is a linear scan of at most 128 u64 values, which costs nothing.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/custody_context.rs:507`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L507) sampling_columns_for_epoch slices the precomputed ordered_custody_column_indices
- [`beacon_node/beacon_chain/src/custody_context.rs:525`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L525) custody_columns_for_epoch slices the same list
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:366`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L366) put_rpc_custody_columns filters with slice contains
- [`beacon_node/lighthouse_network/src/types/globals.rs:217`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/globals.rs#L217) is_custody_peer_of uses per-peer custody subnets stored in peer_info

**Skeptic check.** Verified: the ordered indices are precomputed and every call site slices them, so nothing is derived again per call. Earlier evidence was correct. The only difference from teku#10446 is a slice instead of a hash set, and that does not matter at 128 entries.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#10446](https://github.com/Consensys-Incorporated/teku/pull/10446), [prysm#14893](https://github.com/OffchainLabs/prysm/pull/14893), [nimbus#7210](https://github.com/status-im/nimbus-eth2/pull/7210)

</details>


<a id="beacon_api-111"></a>
<details>
<summary><b>beacon_api-111</b> Batch KZG verify sidecars from RPC and sync — <i>implemented · medium · S · cpu, latency, sync</i></summary>

**Idea.** Verify KZG proofs of all blob/column sidecars received by RPC or range sync for a block or batch together with batch KZG verification, instead of one by one.

**Impact.** RPC lookups and range sync already verify each block's sidecars in one batched call. Forward range sync batches per block, not across the segment. Cell-proof batch cost is close to linear, so batching across blocks would gain little.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker.rs:357`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L357) put_rpc_custody_columns -&gt; KzgVerifiedDataColumn::from_batch_with_scoring (one batch for the response)
- [`beacon_node/beacon_chain/src/data_column_verification.rs:507`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L507) from_batch_with_scoring calls verify_kzg_for_data_column_list on the whole list
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:335`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L335) put_rpc_blobs -&gt; KzgVerifiedBlobList::new batch
- [`beacon_node/beacon_chain/src/block_verification.rs:705`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L705) signature_verify_chain_segment batches the columns of each block with verify_columns_against_block
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:495`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L495) batch_verify_kzg_for_range_sync_blocks (backfill): blobs batched across the whole batch, columns per block

**Skeptic check.** Verified: by-root columns and blobs are verified as one batch per response, and range and backfill sync verify per block or per batch. Earlier evidence was right. Side observation, not checked in depth: signature_verify_chain_segment only verifies columns, so pre-Fulu blobs in forward range sync seem to skip KZG there. That is a correctness question, not a performance gap.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#13351](https://github.com/OffchainLabs/prysm/pull/13351), [lighthouse#4736](https://github.com/sigp/lighthouse/pull/4736)

</details>


<a id="beacon_api-112"></a>
<details>
<summary><b>beacon_api-112</b> Batch gossip column verification per block — <i>partial · medium · M · cpu, latency</i></summary>

**Idea.** Collect gossip data column sidecars of the same block header and verify their KZG cell proofs in one batch, with the inclusion proof and header signature verified once per batch.

**Gap in Lighthouse.** Header-once-per-block exists for partial-message columns (on by default), but full DataColumnSidecar gossip still re-checks inclusion proof and proposer signature per sidecar, and no path batches KZG cell proofs across columns of one block. Add a beacon_processor batch stage for gossip columns grouped by block root that calls verify_kzg_for_data_column_list once, with per-item fallback, and reuse a verified-header cache for full sidecars.

**Impact.** KZG batching across 8+ custody columns per block could cut gossip column job time several-fold (lodestar reports 3-4x, ~250ms); header dedupe gain is smaller since partial path already has it.

**Best measured result.** job time 3x-4x faster, saves ~250ms; ~35ms more wait time (pr:lodestar#7910)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/src/cli.rs:693-702`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L693-L702) --enable-partial-columns defaults to true
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2480-2511`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2480-L2511) verify_partial_data_column_header_for_gossip: header (inclusion proof + proposer signature) verified once per block root, later partials reuse cached header
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1316-1349`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1316-L1349) partial gossip path skips header checks when the assembler has a cached header
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1166-1192`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1166-L1192) full sidecar path KZG-verifies only cells missing from DA cache/assembler (missing_cells_for_column_sidecar), but still per-sidecar inclusion proof, signature and KZG
- [`beacon_node/beacon_processor/src/lib.rs:1311-1316`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1311-L1316) gossip_data_column_queue and gossip_partial_data_column_queue pop one item per job; no batching like GossipAttestationBatch

**Second check.** Earlier review missed the partial-columns path (default on) which caches the verified header per block root and skips header re-verification, and the missing-cells filter that avoids re-verifying known cells; KZG batching across columns is still absent.

**Verdict history.** not (checked) → partial (refuted)

**Sources.** [lodestar#7910](https://github.com/ChainSafe/lodestar/pull/7910)

</details>


<a id="beacon_api-113"></a>
<details>
<summary><b>beacon_api-113</b> Combine by-root sidecar requests per peer — <i>implemented · low · S · bandwidth, sync</i></summary>

**Idea.** Send one by-root RPC request per peer for all missing blobs or columns of a block (or several sampling requests), instead of one request per sidecar.

**Impact.** Custody lookups group all missing columns of the block(s) by the selected peer and send one by-root request per peer.

**Best measured result.** saves bandwidth (stated, no numbers) (pr:teku#8952)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context/custody.rs:295`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L295) one data_column_lookup_request per peer from columns_to_request_by_peer
- [`beacon_node/network/src/sync/network_context/requests/data_columns_by_root.rs:11`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/requests/data_columns_by_root.rs#L11) DataColumnsByRootRequestParams{block_roots, indices} becomes one DataColumnsByRootIdentifier list
- [`beacon_node/network/src/sync/network_context.rs:577`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L577) select_columns_by_range_peers_to_request groups columns per peer for by-range

**Skeptic check.** Verified: the custody request groups columns per peer, and one request carries all the block roots and indices. Earlier evidence was correct. Blob by-root lookups are gone post-Fulu, so only columns matter.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#8952](https://github.com/Consensys-Incorporated/teku/pull/8952), [lighthouse#6256](https://github.com/sigp/lighthouse/pull/6256)

</details>


<a id="beacon_api-114"></a>
<details>
<summary><b>beacon_api-114</b> Cap columns per by-root request — <i>partial · low · S · bandwidth</i></summary>

**Idea.** Limit the number of data columns asked from one peer in one request, so peers are not overloaded and requests do not time out.

**Gap in Lighthouse.** Add a cap on indices per DataColumnsByRootRequestParams in the loop at custody.rs:295 and split into several requests; today per-peer load is limited only by at_concurrency_limit and spec max_request limits.

**Impact.** Fewer timeouts when one peer is chosen for many columns of many blocks; matters mostly for supernodes and backfill-like lookups.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context/custody.rs:236-307`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L236-L307) groups columns per peer, no cap on indices per request
- network/src/sync/network_context/requests/data_columns_by_root.rs:11 params unbounded except spec max
- custody.rs:369 caps attempts and de-prioritizes peers at concurrency limit

**Sources.** [caplin#16989](https://github.com/erigontech/erigon/pull/16989)

</details>


<a id="beacon_api-115"></a>
<details>
<summary><b>beacon_api-115</b> Request columns only from custody peers — <i>implemented · medium · S · bandwidth, sync</i></summary>

**Idea.** Send by-root column requests only to peers whose custody set contains the columns, filtered by the peer's custody mask.

**Impact.** By-root and by-range column requests only go to peers whose advertised custody subnets contain the column.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context/custody.rs:356`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L356) select_column_peer draws only from get_custodial_peers(column_index, block_slot)
- [`beacon_node/network/src/sync/network_context.rs:419`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L419) get_custodial_peers -&gt; custody_peers_for_column
- [`beacon_node/lighthouse_network/src/types/globals.rs:201`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/globals.rs#L201) custody_peers_for_column -&gt; good_custody_subnet_peer(subnet, slot)
- [`beacon_node/network/src/sync/network_context.rs:592`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L592) by-range filters peers with is_custody_peer_of

**Skeptic check.** Verified on both the lookup path and the range path. The peer set comes from custody subnets in peer metadata, filtered by slot. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#14452](https://github.com/OffchainLabs/prysm/pull/14452), [caplin#17392](https://github.com/erigontech/erigon/pull/17392)

</details>


<a id="beacon_api-116"></a>
<details>
<summary><b>beacon_api-116</b> Hedge slow column requests to alternate peers — <i>not · medium · M · latency, sync</i></summary>

**Idea.** After a delay, send a slow in-flight data column request again to another custody peer, bounded to a fraction of pending requests and two attempts per request.

**Gap in Lighthouse.** No duplicate/hedged request: a slow custody peer holds the column until the 10s RPC timeout or an error. Add a per-column hedge timer in ActiveCustodyRequest that re-issues the by-root request to another custody peer after a delay, capped by a fraction of pending requests and 2 attempts, first response wins.

**Impact.** Lower tail latency for lookups when one custody peer is slow; no gain in the common case.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context/custody.rs:241-271`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L241-L271) only requests columns in NotStarted state; one in-flight request per column
- [`beacon_node/network/src/sync/network_context/custody.rs:405-455`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L405-L455) ColumnRequest status NotStarted/Downloading/Downloaded with no hedge timer; retry only after on_download_error
- [`beacon_node/lighthouse_network/src/rpc/handler.rs:44`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L44) RESP_TIMEOUT 10s is the only slow-peer bound

**Second check.** Checked custody.rs request loop, ColumnRequest state machine, network_context and RPC handler timeouts for any duplicate/parallel or speculative re-request; none found.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [teku#11011](https://github.com/Consensys-Incorporated/teku/pull/11011)

</details>


<a id="beacon_api-117"></a>
<details>
<summary><b>beacon_api-117</b> Insert EL-built columns in one batch — <i>implemented · low · S · cpu</i></summary>

**Idea.** Put the columns built from getBlobs into the column quarantine in one batch capped at the needed count, instead of one insert per column.

**Impact.** EL-built columns already go into the DA cache as one batch of custody columns only.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:483`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L483) put_kzg_verified_data_columns takes an iterator under one write lock with one availability check
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:361`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L361) process_engine_blobs_fulu receives all full columns at once
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:327`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L327) only custody columns are imported (capped to need)

**Skeptic check.** Verified a single batched insert of custody-only columns from both the V2/V3 and V4 paths. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#7725](https://github.com/status-im/nimbus-eth2/pull/7725)

</details>


<a id="beacon_api-118"></a>
<details>
<summary><b>beacon_api-118</b> Async access to pending sidecar maps — <i>n/a · low · latency</i></summary>

**Idea.** Access the pending-reconstruction and received-column maps through async methods so tasks yield instead of blocking on lock contention.

**Impact.** Lighthouse uses short sync parking_lot locks, not async maps; no contention issue evident.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:351`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L351) parking_lot RwLock around LRU, held briefly in sync code

**Sources.** [grandine@dbe7dba8a](https://github.com/grandinetech/grandine/commit/dbe7dba8ab91), [grandine@4355744bd](https://github.com/grandinetech/grandine/commit/4355744bdbcd)

</details>


<a id="beacon_api-119"></a>
<details>
<summary><b>beacon_api-119</b> Validate blob sidecars without state advancement — <i>implemented · medium · S · cpu, memory, latency</i></summary>

**Idea.** Do not run slot processing to get a state for blob sidecar validation. Use an existing state, or hold the sidecar until the block's state is ready.

**Impact.** In the normal case the proposer cache answers, and it is primed by block import and the state advance timer. With Fulu proposer lookahead, the decision slot is two epochs back, so a cache miss needs a partial advance only when the parent is more than one epoch behind. That happens only with empty epochs or deep forks.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_column_verification.rs:1747`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1747) verify_proposer_and_signature uses with_proposer_cache keyed by proposer shuffling root
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1759`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1759) on a miss loads the parent state via get_advanced_hot_state (cache first)
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:204`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L204) on a miss ensure_state_can_determine_proposers_for_epoch
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:346`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L346) partial_state_advance only when the parent state epoch &lt; decision epoch + 1

**Skeptic check.** Verified that the gossip column path reads the proposer cache and does not run slot processing on a hit. The earlier claim of no process_slots was not exact: a cache miss can run partial_state_advance. That case is rare after Fulu and is deduplicated through a OnceCell, so the verdict stands.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine#192](https://github.com/grandinetech/grandine/pull/192), [grandine@f6d472f38](https://github.com/grandinetech/grandine/commit/f6d472f38b7f), [grandine#183](https://github.com/grandinetech/grandine/pull/183)

</details>


<a id="beacon_api-120"></a>
<details>
<summary><b>beacon_api-120</b> Iterate directly in pending-column availability check — <i>partial · low · S · cpu, memory</i></summary>

**Idea.** In the check for pending columns, iterate directly instead of collecting into a Vec, which avoids an allocation.

**Gap in Lighthouse.** Callers that only test membership or count could use an iterator or a bitset instead of cached_data_column_indexes; sites include network_context.rs:978 and data_availability_checker.rs:584.

**Impact.** Saves one small Vec alloc per check; negligible.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:112`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L112) get_cached_data_columns_indices collects a Vec
- beacon_chain/src/data_availability_checker.rs:177 cached_data_column_indexes returns Vec

**Sources.** [grandine#331](https://github.com/grandinetech/grandine/pull/331)

</details>


<a id="beacon_api-121"></a>
<details>
<summary><b>beacon_api-121</b> Prune blob and column data past DA window — <i>implemented · medium · S · disk</i></summary>

**Idea.** Delete blob/column sidecars older than the data availability retention window (and non-canonical ones at finalization), with storage keyed by slot so pruning can stream in order. This keeps disk use bounded.

**Impact.** Disk use for sidecars is bounded by the DA window, and non-canonical sidecars are deleted at finalization. Pruning walks block roots backwards, not a slot-ordered key range. That is a separate idea about streaming.

**Best measured result.** 1.6TB in caplin dir on a Hoodi node (pr:caplin#20379)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3277`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3277) try_prune_blobs prunes blobs (pre-Fulu) and columns (Fulu+) older than the DA boundary minus margin
- [`beacon_node/beacon_chain/src/migrate.rs:217`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L217) and :249 run_prune_blobs runs on finalization migration
- [`beacon_node/beacon_chain/src/migrate.rs:780`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L780) DeleteBlobs and DeleteDataColumns for abandoned fork blocks
- [`consensus/types/src/core/chain_spec.rs:941`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/core/chain_spec.rs#L941) min_epoch_data_availability_boundary
- [`beacon_node/store/src/lib.rs:144`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/lib.rs#L144) column keys are block_root+index, not slot-prefixed

**Skeptic check.** Verified that automatic pruning runs from the migrator, uses the epoch-based DA boundary, and covers columns, and that abandoned forks have their columns deleted. Earlier evidence was right. The slot-keyed layout is missing, but the earlier check correctly assigned it to another idea.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#3852](https://github.com/sigp/lighthouse/pull/3852), [caplin#20379](https://github.com/erigontech/erigon/pull/20379), [teku#6587](https://github.com/Consensys-Incorporated/teku/pull/6587)

</details>


<a id="beacon_api-122"></a>
<details>
<summary><b>beacon_api-122</b> Derive column retention window from chain config — <i>implemented · low · S · disk</i></summary>

**Idea.** Compute the data column retention window as epochs times slots-per-epoch from the chain config, not a mainnet slot default, so chains with shorter epochs do not keep twice the data.

**Impact.** Retention is in epochs from the chain config, with no mainnet slot-count default, so Gnosis keeps the correct window.

**Best measured result.** gnosis retained 131072 slots against a 65536 window (2x) (pr:caplin#23610)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/core/chain_spec.rs:948`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/core/chain_spec.rs#L948) boundary = current_epoch - min_epochs_for_data_column_sidecars_requests (epochs)
- [`consensus/types/src/core/chain_spec.rs:2409`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/core/chain_spec.rs#L2409) loaded from network config
- [`common/eth2_network_config/built_in_network_configs/gnosis/config.yaml:167`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2_network_config/built_in_network_configs/gnosis/config.yaml#L167) MIN_EPOCHS_FOR_DATA_COLUMN_SIDECARS_REQUESTS: 16384

**Skeptic check.** Verified that the retention and prune boundary are computed in epochs from the spec loaded per network. The caplin bug, a slot-count flag default, has no equivalent in Lighthouse. Earlier evidence was correct. I rate the value low because nothing is left to gain.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#23610](https://github.com/erigontech/erigon/pull/23610)

</details>


<a id="beacon_api-123"></a>
<details>
<summary><b>beacon_api-123</b> Never prune blobs needed at chain tip — <i>implemented · low · S · latency</i></summary>

**Idea.** Limit pruning to blobs below what tip block processing still needs, so over-pruning does not force blob refetches.

**Impact.** None; tip blobs are never pruned.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:1731`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1731)
- [`beacon_node/store/src/hot_cold_store.rs:3303`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3303)
- [`beacon_node/store/src/hot_cold_store.rs:3307`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3307)

**Skeptic check.** try_prune_blobs sets end_epoch = min(DA boundary - margin - 1, split epoch - 1), so pruning stays below both the DA window and finalization. It runs only on finalization. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#9863](https://github.com/erigontech/erigon/pull/9863)

</details>


<a id="beacon_api-124"></a>
<details>
<summary><b>beacon_api-124</b> Cheap filesystem traversal for blob pruning — <i>n/a · medium · cpu, disk</i></summary>

**Idea.** When pruning file-based blob storage, walk directories with the efficient directory-iteration syscall and cache root-to-slot lookups from earlier passes, instead of a stat or file read per blob.

**Impact.** Lighthouse stores sidecars in the key-value database, so there is no directory traversal or stat per blob.

**Best measured result.** The pruning routine appears to consume a ton of disk or syscall resources on some systems (pr:prysm#13425)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3277-3450`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3277-L3450) blobs/columns live in a KV DB (BeaconBlob/BeaconDataColumn), not files
- [`beacon_node/store/src/lib.rs:144`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/lib.rs#L144) get_data_column_key

**Sources.** [prysm#13425](https://github.com/OffchainLabs/prysm/pull/13425), [prysm#13410](https://github.com/OffchainLabs/prysm/pull/13410)

</details>


<a id="beacon_api-125"></a>
<details>
<summary><b>beacon_api-125</b> Incremental capped low-priority blob pruning — <i>partial · medium · S · cpu, disk, latency</i></summary>

**Idea.** Prune blobs often in small capped chunks on a low-priority single thread, reading keys only from the KV store, instead of deleting a whole epoch at once.

**Gap in Lighthouse.** Pruning is frequent (per epoch) and off the hot path, but uncapped per run: a lagging node deletes everything in one atomic batch, and existence checks read all 128 column keys per block instead of iterating existing keys. Add a max-blocks/keys cap per call and iterate stored keys from the KV store.

**Impact.** Avoids a large delete stall and many existence reads on lagging nodes; negligible at steady state.

**Best measured result.** Cap 32 per minute vs about 5 new sidecars per minute (pr:teku#6628)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3277-3330`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3277-L3330) try_prune_blobs runs after finalization on the migrator background thread, gated by epochs_per_blob_prune (default 1)
- [`beacon_node/store/src/hot_cold_store.rs:3359-3433`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3359-L3433) iterates all blocks back to the last pruned one with no per-run cap and key_exists on all column keys per block
- [`beacon_node/store/src/hot_cold_store.rs:3448-3454`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3448-L3454) all deletes applied in one do_atomically batch

**Second check.** Re-read the full try_prune_blobs body; confirmed no cap, single atomic delete batch, and per-index key_exists (the code comment itself suggests reading existing indices as a future refactor).

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [teku#6628](https://github.com/Consensys-Incorporated/teku/pull/6628), [teku#6758](https://github.com/Consensys-Incorporated/teku/pull/6758)

</details>


<a id="beacon_api-126"></a>
<details>
<summary><b>beacon_api-126</b> Store blob sidecars in KV database — <i>implemented · low · S · memory, disk</i></summary>

**Idea.** Store blob sidecars in the key-value database (root to commitments, commitment to blob) instead of per-blob files with in-memory index maps.

**Impact.** None; blobs already live in the KV blobs_db.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2616`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2616)
- [`beacon_node/store/src/hot_cold_store.rs:2627`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2627)
- [`beacon_node/store/src/hot_cold_store.rs:2695`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2695)

**Skeptic check.** Blobs are stored in the blobs_db KV store (DBColumn::BeaconBlob, keyed by block root, one SSZ list per block). Columns use BeaconDataColumn keyed by root+index. There are no per-blob files or in-memory index maps, so the earlier verdict holds.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#9469](https://github.com/erigontech/erigon/pull/9469)

</details>


<a id="beacon_api-127"></a>
<details>
<summary><b>beacon_api-127</b> Persist data columns in dedicated disk store — <i>implemented · low · S · disk</i></summary>

**Idea.** Persist data column sidecars in their own on-disk store.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2695`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2695)
- [`beacon_node/store/src/hot_cold_store.rs:2597`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2597)

**Skeptic check.** Data columns are persisted in their own DB column (BeaconDataColumn) inside the separate blobs_db, keyed by block_root+index. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [silver#39](https://github.com/gattaca-com/silver/pull/39)

</details>


<a id="beacon_api-128"></a>
<details>
<summary><b>beacon_api-128</b> In-memory index of stored sidecars — <i>n/a · low · disk, startup</i></summary>

**Idea.** Keep an in-memory index of which blob/column sidecars are on disk (warmed at startup, updated on writes) so availability and presence checks do no filesystem reads.

**Impact.** Design is KV with prefix iteration, not per-file storage, so no filesystem presence reads exist to avoid.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2657`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2657) get_data_column_keys uses prefix iteration on KV
- [`beacon_node/store/src/hot_cold_store.rs:2695`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2695) point get with block cache

**Sources.** [prysm#15257](https://github.com/OffchainLabs/prysm/pull/15257), [prysm#13788](https://github.com/OffchainLabs/prysm/pull/13788)

</details>


<a id="beacon_api-129"></a>
<details>
<summary><b>beacon_api-129</b> Faster column reads from storage — <i>implemented · low · S · cpu, disk</i></summary>

**Idea.** Read data columns from storage without unnecessary reads in Get.

**Impact.** Negligible remaining gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2679`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2679)
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1855`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1855)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1229`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1229)

**Skeptic check.** get_data_column checks the block cache first, then does one point read per requested index. ByRange and ByRoot fetch only the requested custody indices. One small extra: get_data_columns_checking_all_caches loads the blinded block (usually a cache hit) only to get the fork name, which is not worth a change.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#15309](https://github.com/OffchainLabs/prysm/pull/15309)

</details>


<a id="beacon_api-130"></a>
<details>
<summary><b>beacon_api-130</b> Snapshot sidecar index cache at shutdown — <i>n/a · low · startup</i></summary>

**Idea.** Write the data column sidecar index cache to a snapshot file on graceful shutdown and load it on start, instead of walking the whole sidecar directory to warm it.

**Impact.** No sidecar directory walk or index cache warmed at startup exists in Lighthouse.

**Best measured result.** Warm-up 3.26s to 114ms; archive nodes could take over 20 minutes (pr:prysm#17762)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2657`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2657) index derived via DB prefix iteration on demand
- [`beacon_node/store/src/hot_cold_store.rs:276`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L276) only custody info is cached at startup

**Sources.** [prysm#17762](https://github.com/OffchainLabs/prysm/pull/17762)

</details>


<a id="beacon_api-131"></a>
<details>
<summary><b>beacon_api-131</b> Cache gossip-validated sidecars for import — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Keep the blob/column sidecars already validated on gossip in a cache so fork choice import does not verify them again.

**Impact.** Sidecars verified on gossip are kept with type-level proof of KZG verification and become available at import without another check.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker.rs:394`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L394) put_gossip_verified_data_columns wraps via KzgVerifiedCustodyDataColumn::from_asserted_custody (no re-verify)
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:483`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L483) put_kzg_verified_data_columns stores verified columns in PendingComponents
- [`beacon_node/beacon_chain/src/block_verification.rs:1412`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1412) verify_kzg_for_available_block only in the RangeSyncBlock IntoExecutionPendingBlock impl
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:676`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L676) batch_verify_kzg_for_range_sync_blocks only for backfill

**Skeptic check.** Verified that the only import-time KZG calls are on range-sync and backfill inputs, which never passed gossip verification. Gossip and RPC lookup columns are verified once, when they enter the DA cache. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#6636](https://github.com/Consensys-Incorporated/teku/pull/6636), [grandine@0e22c0ff9](https://github.com/grandinetech/grandine/commit/0e22c0ff9663)

</details>


<a id="beacon_api-132"></a>
<details>
<summary><b>beacon_api-132</b> Drop sidecars for already-imported blocks — <i>partial · low · S · cpu, memory, bandwidth</i></summary>

**Idea.** Ignore received blob sidecars (and do not request them) for blocks already imported into fork choice, and do not register historical sync data in the gossip blob pool, so no redundant verification or pool growth occurs.

**Gap in Lighthouse.** Gossip dedups by observed cache and by DA cache contents, but there is no early fork-choice 'already imported' ignore for full sidecars or RPC-sourced data; a late column for an imported block may still reach cache/verification until the observation path catches it. Add an is_block_data_imported check at the start of gossip column/blob verification and in lookup requests.

**Impact.** Saves occasional redundant KZG verification and cache entries; small.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_column_verification.rs:664`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L664) is_block_data_imported gate only for partial-column header caching
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1654`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1654) observation_key_is_known dedup
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1175`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1175) PriorKnownUnpublished via missing_cells_for_column_sidecar

**Sources.** [teku#7231](https://github.com/Consensys-Incorporated/teku/pull/7231), [grandine@f67342dc9](https://github.com/grandinetech/grandine/commit/f67342dc9f92), [grandine#140](https://github.com/grandinetech/grandine/pull/140)

</details>


<a id="beacon_api-133"></a>
<details>
<summary><b>beacon_api-133</b> Bound or fail fast on DA wait — <i>n/a · medium · latency, sync</i></summary>

**Idea.** During sync and payload envelope import, bound the data availability wait (for example one slot) or check availability synchronously and return an error so the batch is retried, instead of waiting indefinitely.

**Impact.** No blocking DA wait exists in Lighthouse: the cache is non-blocking and returns MissingComponents, so there is nothing to bound.

**Best measured result.** Fixed devnet sync dead-end at batch boundary (pr:prysm#16978)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:524`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L524) check_availability_and_cache_components returns MissingComponents immediately
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:676`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L676) range sync verifies coupled block+sidecars up front
- [`beacon_node/beacon_chain/src/payload_envelope_verification/import.rs:139`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/import.rs#L139) envelope import returns MissingComponents, no wait

**Sources.** [prysm#16991](https://github.com/OffchainLabs/prysm/pull/16991), [prysm#16978](https://github.com/OffchainLabs/prysm/pull/16978), [prysm#16993](https://github.com/OffchainLabs/prysm/pull/16993), [prysm#17152](https://github.com/OffchainLabs/prysm/pull/17152)

</details>


<a id="beacon_api-134"></a>
<details>
<summary><b>beacon_api-134</b> Bounded cache of in-flight sampled blocks — <i>implemented · low · S · memory</i></summary>

**Idea.** Keep blocks awaiting column sampling in a bounded cache with eviction, serve them to peers from it, and skip refetching blocks already held.

**Impact.** None; same effect as Teku's sampler cache.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:351`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L351)
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:379`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L379)
- [`beacon_node/beacon_chain/src/beacon_block_streamer.rs:173`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_block_streamer.rs#L173)
- [`beacon_node/network/src/sync/network_context.rs:742`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L742)

**Skeptic check.** All three parts are present. Pending blocks sit in a bounded LRU (capacity 32), BlocksByRoot serves them through get_block_process_status in the block streamer, and sync lookups use the same status to skip blocks already held. LRU eviction replaces Teku's soft/hard limits.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#10533](https://github.com/Consensys-Incorporated/teku/pull/10533), [teku#10264](https://github.com/Consensys-Incorporated/teku/pull/10264)

</details>


<a id="beacon_api-135"></a>
<details>
<summary><b>beacon_api-135</b> Run DA check concurrently with execution verification — <i>implemented · medium · S · latency</i></summary>

**Idea.** Run the data availability check concurrently with consensus verification and EL newPayload, in one cancel-on-failure group, not sequentially after them.

**Impact.** None on the head path. Column KZG verification runs on its own gossip/RPC tasks while the envelope (Gloas) or block (Fulu) runs consensus and EL checks, and the DA step after EL is only a cache insert plus a count.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/payload_envelope_verification/import.rs:89`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/import.rs#L89)
- [`beacon_node/beacon_chain/src/payload_envelope_verification/import.rs:173`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/import.rs#L173)
- [`beacon_node/beacon_chain/src/pending_payload_cache/mod.rs:1`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/mod.rs#L1)
- [`beacon_node/beacon_chain/src/pending_payload_cache/mod.rs:321`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/mod.rs#L321)
- [`beacon_node/beacon_chain/src/pending_payload_cache/mod.rs:352`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/mod.rs#L352)
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:524`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L524)

**Second check.** The source PR (prysm#16899) is about the Gloas payload envelope; the earlier review checked the pre-Gloas range-sync block path. Lighthouse's Gloas pending_payload_cache already decouples column KZG verification from envelope execution and joins them at a cache, so the DA check never runs after the EL.

**Skeptic check.** Verified that check_envelope_availability_and_import only calls put_executed_payload_envelope and that columns are verified against the bid on arrival, so DA work already overlaps EL newPayload. The Fulu block path uses the same event-driven cache. The earlier evidence was correct.

**Verdict history.** partial (checked) → implemented (refuted) → implemented (skeptic)

**Sources.** [prysm#16899](https://github.com/OffchainLabs/prysm/pull/16899)

</details>


<a id="beacon_api-136"></a>
<details>
<summary><b>beacon_api-136</b> Merge pre-import block cache into DA cache — <i>implemented · low · S · memory</i></summary>

**Idea.** Serve recent and pre-executed blocks to req/resp from the one bounded data availability cache instead of a separate, unbounded pre-import cache.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:1390`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1390)
- [`beacon_node/beacon_chain/src/beacon_block_streamer.rs:171`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_block_streamer.rs#L171)
- [`beacon_node/beacon_chain/src/pending_payload_cache/mod.rs:118`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/mod.rs#L118)
- [`beacon_node/beacon_chain/src/metrics.rs:527`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/metrics.rs#L527)

**Skeptic check.** There is no separate pre-import cache. The req/resp cache check goes through the DA checker LRU, plus the Gloas pending_payload_cache, which is also a bounded LruCache. Only the metric name remains, so the earlier verdict was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#8045](https://github.com/sigp/lighthouse/pull/8045)

</details>


<a id="beacon_api-137"></a>
<details>
<summary><b>beacon_api-137</b> Skip duplicate blob arrival notifications — <i>implemented · low · S · cpu</i></summary>

**Idea.** Check whether a blob index is already present before notifying the blob waiter, so the same blob is not processed twice.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:170`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L170)
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:176`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L176)
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1652`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1652)

**Skeptic check.** merge_blobs inserts only when !blob_exists(index), and merge_data_columns skips cached indices. Gossip also dedups through the observed caches before verification. A late duplicate re-runs the cheap availability check, but import is guarded downstream, so the same blob is never processed twice.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#13123](https://github.com/OffchainLabs/prysm/pull/13123)

</details>


<a id="beacon_api-138"></a>
<details>
<summary><b>beacon_api-138</b> Track received columns to skip duplicate work — <i>implemented · medium · S · cpu, disk, bandwidth</i></summary>

**Idea.** Track which data columns were received and stored per block, so a column from gossip and the same one recovered from EL is not processed, persisted or requested twice.

**Impact.** Duplicate KZG verification, publishing, storing and requesting of columns is already avoided.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:176`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L176)
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1163`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1163)
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:584`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L584)
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:631`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L631)
- [`beacon_node/network/src/sync/network_context.rs:971`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L971)

**Skeptic check.** Verified five dedup points. merge_data_columns skips cached indices. Gossip validation returns PriorKnownUnpublished for columns already cached (from the EL or reconstruction) before KZG. Reconstruction and fetch_blobs filter out observed and cached indices. Lookups request only uncached sampling columns. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#14467](https://github.com/OffchainLabs/prysm/pull/14467), [teku#9409](https://github.com/Consensys-Incorporated/teku/pull/9409)

</details>


<a id="beacon_api-139"></a>
<details>
<summary><b>beacon_api-139</b> Retry pending block only after reconstruction finishes — <i>n/a · low · S · cpu</i></summary>

**Idea.** After column reconstruction has started, retry the pending block only when all sampled columns are accepted, not at half, to avoid redundant block retries.

**Gap in Lighthouse.** No pending-block retry exists: blocks sit in the DA cache and become available when enough columns are put, so there is no half-vs-all retry trigger to tune.

**Impact.** Nothing; reconstruction runs at most once per block.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:592`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L592) reconstruction decision, once-only flag
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:537`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L537) reconstruct_data_columns

**Sources.** [grandine@5f32e526b](https://github.com/grandinetech/grandine/commit/5f32e526bf50)

</details>


<a id="beacon_api-140"></a>
<details>
<summary><b>beacon_api-140</b> Delay RPC fetch of missing sidecars — <i>partial · medium · M · latency, bandwidth, sync</i></summary>

**Idea.** Delay RPC fetches of missing blobs/columns by a slot-time-based interval (about 0.5 to 1 s, capped by the attestation deadline), so gossip can deliver them first and redundant requests are avoided.

**Gap in Lighthouse.** RPC by-root fetch is deferred implicitly by waiting for attestation-carrying peers, not by an explicit slot-time timer (0.5-1 s capped by the attestation deadline). A block that nobody has attested yet gets no scheduled fetch.

**Impact.** Mostly avoids redundant RPC; small bandwidth saving, no CPU impact.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/manager.rs:1036`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L1036) handle_unknown_block_root waits for unknown_root_min_peers corroboration (record_unknown_root:1061)
- [`beacon_node/network/src/sync/block_lookups/mod.rs:66`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L66) LOOKUP_MAX_DURATION_NO_PEERS_SECS: lookups created from gossip components have no peers until attestations arrive, so RPC waits roughly until the attestation deadline
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1016`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1016) gossip column MissingComponents only triggers reconstruction check, no RPC

**Second check.** Also checked the beacon_processor reprocess queue and the lookup constants for an explicit RPC delay timer; the only slot-time-based timer found is for column reconstruction (work_reprocessing_queue.rs:107), not for RPC fetches.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [teku#10094](https://github.com/Consensys-Incorporated/teku/pull/10094), [teku#7026](https://github.com/Consensys-Incorporated/teku/pull/7026)

</details>


<a id="beacon_api-141"></a>
<details>
<summary><b>beacon_api-141</b> Request missing blobs immediately on block seen — <i>partial · medium · S · latency</i></summary>

**Idea.** When a gossip block arrives, enqueue a peer request for missing blobs at once instead of waiting for the availability wait to expire.

**Gap in Lighthouse.** On block arrival Lighthouse fetches the blob data from the EL at once and, only with --enable-partial-columns (off by default), requests the missing cells from gossip peers. It does not start a by-root RPC request for missing custody columns on block arrival.

**Impact.** Faster availability when the EL mempool lacks blobs and gossip is late; matters on poorly connected nodes, not CPU.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1934`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1934) process_gossip_verified_block calls spawn_fetch_block_columns as soon as the block is gossip-valid, before process_block
- [`beacon_node/network/src/network_beacon_processor/mod.rs:960`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L960) spawn_fetch_block_columns: engine getBlobs from the EL (fetch_engine_blobs_and_publish_full:998), then publish_partial_data_columns:1070 asks mesh peers for missing cells (request_cells bitmap)
- [`beacon_node/lighthouse_network/src/config.rs:383`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L383) enable_partial_columns defaults to false
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1972`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1972) MissingComponents does not start an RPC lookup

**Second check.** The earlier review missed spawn_fetch_block_columns, which runs on block arrival: an EL getBlobs fetch plus an optional partial-column cell request to peers. That covers the main goal of 'pull data as soon as the block is seen', but not through peer RPC.

**Verdict history.** not (checked) → partial (refuted)

**Sources.** [lodestar#6499](https://github.com/ChainSafe/lodestar/pull/6499)

</details>


<a id="beacon_api-142"></a>
<details>
<summary><b>beacon_api-142</b> Pull late block when blobs arrive first — <i>partial · low · S · latency</i></summary>

**Idea.** If blobs arrive on gossip but the block does not arrive by a cutoff, fetch the block and remaining blobs from peers instead of waiting.

**Gap in Lighthouse.** BlockRootUnknown, which triggers SyncMessage::UnknownBlockHashFromAttestation, is returned only on the Gloas path (load_gloas_payload_bid in validate_data_column_sidecar_for_gossip_gloas and in the partial-column path). On Fulu, validate_data_column_sidecar_for_gossip_fulu accepts a column whose parent is known while its block is unseen. process_gossip_verified_data_column then gets MissingComponents and only calls check_reconstruction_trigger. No block lookup starts from the sidecar, at once or after a cutoff. The block arrives only by gossip or through a lookup that an attestation triggers.

**Impact.** Edge case: a Fulu block arrives late or never reaches us over gossip while its columns do. A sidecar-triggered lookup after a cutoff would fetch the block before attestations reference it. The gain is small because columns are usually published after the block.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:777`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L777)
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1241`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1241)
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1016`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1016)
- [`beacon_node/network/src/sync/manager.rs:921`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L921)

**Skeptic check.** The earlier evidence (gossip_methods.rs:780) is the BlockRootUnknown arm, and that arm is reachable only for Gloas columns, because Fulu columns carry their own signed header and never need the block to validate. So the mechanism is missing on Fulu, the fork that runs on mainnet today.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lodestar#6534](https://github.com/ChainSafe/lodestar/pull/6534)

</details>


<a id="beacon_api-143"></a>
<details>
<summary><b>beacon_api-143</b> Fetch missing blobs immediately for past slots — <i>n/a · low · S · latency, sync</i></summary>

**Idea.** When tracked data belongs to a past slot, fetch missing blobs at once instead of waiting the gossip delay.

**Gap in Lighthouse.** No gossip-delay-gated blob fetch pool; missing components are requested by lookup sync, which acts at once.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:351`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L351) pending cache only
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:816`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L816) by-root served from caches

**Sources.** [teku#7103](https://github.com/Consensys-Incorporated/teku/pull/7103)

</details>


<a id="beacon_api-144"></a>
<details>
<summary><b>beacon_api-144</b> Fetch missing columns within the slot — <i>partial · medium · M · latency</i></summary>

**Idea.** Run the missing-column fetcher every second and request missing custody columns by root after a grace of half the time to the attestation deadline, instead of waiting a minute.

**Gap in Lighthouse.** No periodic scan of DA-cache blocks with missing custody columns that requests them by root after a grace; non-supernodes rely on attestation-triggered lookups. Add a slot-clock-driven fetch in the sync manager.

**Impact.** Shortens time-to-available for blocks missing a few custody columns; matters for head liveness, not CPU.

**Best measured result.** block stayed unavailable for over a minute before (pr:caplin#24830)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/manager.rs:1036`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L1036) by-root column fetch only via attestation/unknown-root lookups
- [`beacon_node/network/src/sync/network_context.rs:960`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L960) custody column request for non-cached indices
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:1139`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L1139) in-slot reconstruction timer (RECONSTRUCTION_DEADLINE 1/4 slot, :107) recovers columns for nodes holding &gt;=50%
- [`beacon_node/network/src/sync/block_lookups/mod.rs:779`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L779) drop_stuck_lookups only prunes

**Second check.** Also checked the reprocess queue: it has an in-slot reconstruction deadline timer, which helps supernodes but does not fetch by root; the on-arrival getBlobs fetch (beacon_api-141) also reduces the cases, but there is no periodic fetcher.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [caplin#24830](https://github.com/erigontech/erigon/pull/24830)

</details>


<a id="beacon_api-145"></a>
<details>
<summary><b>beacon_api-145</b> Disable blob tracking after retention passes — <i>n/a · low · S · cpu, memory</i></summary>

**Idea.** After the blob retention window has passed beyond the fork that removed blob sidecars, swap in no-op blob sidecar managers and pools to stop their upkeep.

**Gap in Lighthouse.** No separate blob sidecar manager or tracker pool; post-Fulu the DA cache holds columns only, so there is no Deneb upkeep to swap out.

**Impact.** None measurable.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker.rs:680`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L680) single DA cache maintenance service

**Sources.** [teku#10502](https://github.com/Consensys-Incorporated/teku/pull/10502)

</details>


<a id="beacon_api-146"></a>
<details>
<summary><b>beacon_api-146</b> Disk-backed blob quarantine — <i>not · medium · M · memory, disk</i></summary>

**Idea.** Persist quarantined blob sidecars in a database table keyed by block root and index, deleted at finalization, so the quarantine does not hold them all in memory.

**Gap in Lighthouse.** Quarantined blobs and columns (PendingComponents) are memory only, bounded by LRU capacity and epoch pruning. The old disk overflow column (OverflowLRUCache) was deprecated and removed. To add it: a hot-DB column keyed by (block_root, index), written in put_kzg_verified_*, deleted on import or finalization.

**Impact.** Lowers peak RSS by the unimported sidecars held (tens to a few hundred MB in blob-heavy periods or sync), at the cost of disk writes. The LRU already bounds it, and Lighthouse removed a similar design before, so the gain is small.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:442`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L442) put_kzg_verified_blobs writes only to the in-memory critical LruCache
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:566`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L566) write_lock.entry(block_root) into the in-memory map, no store write
- [`beacon_node/store/src/lib.rs:374`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/lib.rs#L374),409 DBColumn::OverflowLRUCache = 33 marked DEPRECATED (the old disk overflow was removed)

**Second check.** Searched the store crate for a pending, quarantine or overflow column. Only the deprecated OverflowLRUCache DBColumn exists, which shows Lighthouse once had disk overflow and dropped it. Nothing current persists pending components.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [nimbus#7108](https://github.com/status-im/nimbus-eth2/pull/7108)

</details>


<a id="beacon_api-147"></a>
<details>
<summary><b>beacon_api-147</b> Memory-only bounded LRU for pending components — <i>implemented · low · S · memory, disk</i></summary>

**Idea.** Remove the disk overflow of the pending availability cache and keep only a bounded in-memory LRU, removing the disk I/O.

**Impact.** None; disk overflow is already removed.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:350`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L350)
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:366`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L366)

**Skeptic check.** DataAvailabilityCheckerInner holds only RwLock&lt;LruCache&lt;..&gt;&gt;. There is no store handle, and no overflow DB column remains (store references in the file are tests only). The earlier verdict was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#5891](https://github.com/sigp/lighthouse/pull/5891)

</details>


<a id="beacon_api-148"></a>
<details>
<summary><b>beacon_api-148</b> Remove duplicate store of column sidecars — <i>n/a · low · S · memory</i></summary>

**Idea.** Do not keep a second store of received data column sidecars when the data is already held elsewhere.

**Gap in Lighthouse.** Columns live in the DA cache until import, then in the DB; there is no second received-columns store.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs) get_data_columns_checking_all_caches (DA cache then store)
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:833`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L833)

**Sources.** [grandine#266](https://github.com/grandinetech/grandine/pull/266)

</details>


<a id="beacon_api-149"></a>
<details>
<summary><b>beacon_api-149</b> Drop sidecars with out-of-range index — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Track only blob sidecars whose index matches a commitment in the block, so the per-block tracker cannot grow without bound.

**Impact.** None. The per-block trackers are bounded by the maximum item count, and the DA cache stores a blob only when its index and commitment match the block.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/observed_data_sidecars.rs:192`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_data_sidecars.rs#L192)
- [`beacon_node/beacon_chain/src/observed_data_sidecars.rs:152`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_data_sidecars.rs#L152)
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1531`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1531)
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:162`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L162)
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:176`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L176)

**Skeptic check.** Verified that sanitize_data_sidecar rejects an index at or above max_num_of_items before insertion, that column gossip rejects an index at or above NUMBER_OF_COLUMNS, and that merge_single_blob requires a matching commitment. The earlier evidence was correct. I lowered the value to low because the blob gossip path no longer exists.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#7616](https://github.com/Consensys-Incorporated/teku/pull/7616)

</details>


<a id="beacon_api-150"></a>
<details>
<summary><b>beacon_api-150</b> Remove repeated checks from isDataAvailable — <i>n/a · low · S · cpu</i></summary>

**Idea.** Do not repeat blob/commitment consistency checks in the availability check when they were already done earlier.

**Gap in Lighthouse.** Availability check is a count of already-verified columns; no repeated consistency checks run there.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:164`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L164) commitment match once at merge
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:200`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L200) make_available only counts columns

**Sources.** [teku#7575](https://github.com/Consensys-Incorporated/teku/pull/7575)

</details>


<a id="beacon_api-151"></a>
<details>
<summary><b>beacon_api-151</b> Drop stale validator custody registrations — <i>implemented · low · S · memory</i></summary>

**Idea.** Remove validator custody registrations from memory when the validator stops registering, since the custody group count never decreases anyway.

**Impact.** Bounds memory of stale registrations; negligible runtime effect.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/custody_context.rs:92`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L92) register_validators
- [`beacon_node/beacon_chain/src/custody_context.rs:105`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L105) validators.retain drops entries older than VALIDATOR_REGISTRATION_EXPIRY_SLOTS on every registration
- [`beacon_node/beacon_chain/src/custody_context.rs:121`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L121) CGC only raised, never lowered

**Skeptic check.** Verified register_validators prunes stale validator entries on each call while CGC never decreases. The earlier evidence was right; this is the source PR itself (lighthouse#7594).

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#7594](https://github.com/sigp/lighthouse/pull/7594)

</details>


<a id="beacon_api-152"></a>
<details>
<summary><b>beacon_api-152</b> Keep DA entries until import completes — <i>implemented · medium · S · cpu, memory, disk, latency, bandwidth, sync</i></summary>

**Idea.** Do not remove a block's pending components or sampling tracker from the availability cache before fork choice import completes (evict by LRU/finality), and hold the cache write lock only for the insert. This prevents re-downloads and state re-computation.

**Impact.** Re-downloads and the race where components are removed and then inserted again after import are already avoided on both the Fulu and Gloas caches.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:524`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L524)
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:557`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L557)
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:668`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L668)
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:720`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L720)
- [`beacon_node/beacon_chain/src/pending_payload_cache/mod.rs:573`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/mod.rs#L573)
- [`beacon_node/beacon_chain/src/pending_payload_cache/mod.rs:662`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/mod.rs#L662)

**Skeptic check.** Verified that neither the Fulu DA cache nor the Gloas pending_payload_cache removes components on availability. Entries leave only through do_maintenance (finality cutoff), LRU eviction, or remove_pre_execution_block for execution-invalid blocks. update_or_insert_pending_components downgrades the write lock to a read lock after the insert. Lighthouse has no separate sampling tracker to keep. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#5845](https://github.com/sigp/lighthouse/pull/5845), [lighthouse#7961](https://github.com/sigp/lighthouse/pull/7961), [teku#10219](https://github.com/Consensys-Incorporated/teku/pull/10219)

</details>


<a id="beacon_api-153"></a>
<details>
<summary><b>beacon_api-153</b> Wait on store events instead of polling — <i>n/a · low · S · cpu, latency</i></summary>

**Idea.** When serving a column-by-root request for a column not yet stored, wait on a database write event instead of polling the store at an interval.

**Gap in Lighthouse.** Lighthouse does not wait or poll for missing columns in by-root requests; it returns what it has.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:816`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L816) by-root handler reads caches once, no wait or poll loop

**Sources.** [prysm#14062](https://github.com/OffchainLabs/prysm/pull/14062)

</details>


<a id="beacon_api-154"></a>
<details>
<summary><b>beacon_api-154</b> Evict completed column recovery entries — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Remove column recovery tasks from the tracking map at completion (with a timed sweep), store only slot and root per entry, and keep recent sidecars in memory instead of re-reading the DB.

**Impact.** No unbounded recovery map: the reprocess queue map drops dispatched entries, and the reconstruction inputs come from the bounded in-memory DA cache, not the DB.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:592`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L592) check_and_set_reconstruction_started uses a flag on PendingComponents and hands back in-memory verified_data_columns
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:630`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L630) handle_reconstruction_failure resets the flag
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:338`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L338) queued_column_reconstructions map
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:1357`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L1357) ReadyColumnReconstruction retains only pending entries, so completed ones are evicted
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:230`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L230) QueuedColumnReconstruction holds only block_root, slot and the closure

**Skeptic check.** The earlier evidence missed the separate queued_column_reconstructions map in the reprocess queue. I checked it: each dispatch retains only the pending entries, so completed entries are evicted and the map stays bounded. The inputs are the in-memory verified columns.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#9890](https://github.com/Consensys-Incorporated/teku/pull/9890), [teku#9874](https://github.com/Consensys-Incorporated/teku/pull/9874)

</details>


<a id="beacon_api-155"></a>
<details>
<summary><b>beacon_api-155</b> Import only when blob count equals commitments — <i>implemented · low · S · latency</i></summary>

**Idea.** Treat a block as complete only when the number of held blob sidecars exactly equals its KZG commitment count, so import is not triggered early and rejected.

**Impact.** None. A block becomes available only when the column count exactly equals the sampling count; a higher count is an error.

**Best measured result.** mitigates some stuttering in block updates when blobs arrived after blocks (pr:nimbus#5363)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:200`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L200)
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:214`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L214)
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:710`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L710)

**Skeptic check.** Verified that make_available compares verified_data_columns.len() with the expected count and treats Greater as an error. Pre-PeerDAS epochs fall through to NoData (line 236), so pre-Fulu blob DA is no longer enforced, but that path is outside the DA window and blob gossip has been removed. The column path matches the idea.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#5363](https://github.com/status-im/nimbus-eth2/pull/5363)

</details>


<a id="beacon_api-156"></a>
<details>
<summary><b>beacon_api-156</b> Drop gossip columns outside sampling set — <i>implemented · medium · S · cpu, disk, bandwidth</i></summary>

**Idea.** Drop incoming data column sidecars for columns that are not in the node's sampling set before KZG verification and storage.

**Impact.** Small. Only sampling subnets are subscribed, so non-sampling columns rarely arrive, and any that do are filtered out by sampling_columns_for_epoch before they enter the DA cache or storage.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/service.rs:792`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L792)
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1155`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1155)
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:404`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L404)
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:366`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L366)
- [`beacon_node/beacon_chain/src/pending_payload_cache/mod.rs:358`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/mod.rs#L358)

**Skeptic check.** Verified the subnet subscription limit and the sampling filter in put_gossip_verified_data_columns and put_rpc_custody_columns on both the Fulu and Gloas caches. Gossip KZG verification has no explicit sampling check. The trigger in the Grandine PR, a node that stays subscribed after its custody shrinks, does not apply here because Lighthouse custody only grows.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine#376](https://github.com/grandinetech/grandine/pull/376), [grandine@b970e9d91](https://github.com/grandinetech/grandine/commit/b970e9d91cbe)

</details>


<a id="beacon_api-157"></a>
<details>
<summary><b>beacon_api-157</b> Correct proposer cache key in blob verification — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Look up the proposer for blob sidecar verification with the correct shuffling decision root, so the proposer cache hits mid-epoch instead of recomputing the shuffling.

**Impact.** Mid-epoch proposer lookups for column gossip hit the proposer cache.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_column_verification.rs:1743`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1743)
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1746`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1746)
- [`beacon_node/beacon_chain/src/blob_verification.rs:83`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/blob_verification.rs#L83)

**Skeptic check.** Verified that verify_proposer_and_signature keys with_proposer_cache by parent_block.proposer_shuffling_root_for_child_block(column_epoch), and that blob_verification.rs now holds only KZG helpers, with no gossip proposer lookup. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#4646](https://github.com/sigp/lighthouse/pull/4646)

</details>


<a id="beacon_api-158"></a>
<details>
<summary><b>beacon_api-158</b> Consistent sidecar quarantine accounting — <i>n/a · low · cpu, memory, disk</i></summary>

**Idea.** Keep the quarantine's root set, counts and eviction order consistent (for example on a linked list with a root table), so entries do not leak and prune loops do not spin.

**Impact.** Lighthouse uses a bounded LRU keyed by block root, so root set and eviction order cannot diverge.

**Evidence (Lighthouse @ 928b61e719).**

- overflow_lru_cache.rs: bounded LRU keyed by root, no quarantine linked list

**Sources.** [nimbus#7634](https://github.com/status-im/nimbus-eth2/pull/7634), [nimbus#7743](https://github.com/status-im/nimbus-eth2/pull/7743)

</details>


<a id="beacon_api-159"></a>
<details>
<summary><b>beacon_api-159</b> High priority retry for delayed columns — <i>implemented · medium · S · latency</i></summary>

**Idea.** Retry delayed data column sidecars at high priority in the processing queue, since a block is waiting on them.

**Impact.** Delayed columns are retried ahead of attestation work, the same effect as the Grandine high-priority retry task.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:944-948`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L944-L948) unknown_block_data_column_queue popped right after gossip_data_column_queue, ahead of api p0, aggregates and attestations
- [`beacon_node/beacon_processor/src/lib.rs:318-320`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L318-L320) ReadyWork::DataColumn -&gt; Work::UnknownBlockDataColumn
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:1373`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L1373) queued columns released when the block arrives

**Skeptic check.** Confirmed the pop order in the beacon processor manager loop. Grandine moves retries into its high-priority pool; LH places the retry queue directly behind blocks and gossip columns, which is equivalent. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine@6997dfcff](https://github.com/grandinetech/grandine/commit/6997dfcff8be)

</details>


