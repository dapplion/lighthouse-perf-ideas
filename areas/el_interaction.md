# el_interaction

158 ideas: 14 not, 25 partial, 28 implemented, 91 n/a; 18 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [el_interaction-001](#el_interaction-001) | Fetch blobs from EL to build sidecars locally | implemented | high | S | bandwidth, cpu, latency |
| [el_interaction-002](#el_interaction-002) | Use getBlobsV4 to build partial columns from sparse blobpools | implemented | high | S | bandwidth, latency |
| [el_interaction-003](#el_interaction-003) **★** | Fetch blobs from EL during range sync too | not | medium | M | sync, latency |
| [el_interaction-004](#el_interaction-004) **★** | SSZ over REST transport for the engine API | not | medium | L | cpu, latency, bandwidth |
| [el_interaction-005](#el_interaction-005) **★** | SSZ encoding for builder API calls | partial | medium | S | bandwidth, cpu, latency |
| [el_interaction-006](#el_interaction-006) | Send forkchoiceUpdated immediately after payload import | implemented | medium | S | latency |
| [el_interaction-007](#el_interaction-007) **★** | Drive EL sync from light-client head | not | medium | L | sync |
| [el_interaction-008](#el_interaction-008) | Light-client optimistic sync follows gossip directly | n/a | low | S | latency |
| [el_interaction-009](#el_interaction-009) | Fetch historical deposit logs over HTTP, not websocket | n/a | low | S | startup, sync |
| [el_interaction-010](#el_interaction-010) | Bounded, adaptive eth1 log/block query ranges | n/a | low | S | latency, memory, sync |
| [el_interaction-011](#el_interaction-011) | Send early forkchoiceUpdated with payload attributes | implemented | medium | S | latency |
| [el_interaction-012](#el_interaction-012) | Prepare payloads only for imminent local proposals | partial | low | S | cpu, latency, sync |
| [el_interaction-013](#el_interaction-013) | Correct withdrawals in lookahead proposal fcU | implemented | low | S | cpu, latency |
| [el_interaction-014](#el_interaction-014) | Skip missing-payload-id fill when slot block seen | partial | low | S | cpu, latency |
| [el_interaction-015](#el_interaction-015) | Async builder HTTP client with dedicated connection pool | partial | low | S | latency, cpu |
| [el_interaction-016](#el_interaction-016) | Exempt critical builder calls from request throttling | n/a | medium |  | latency |
| [el_interaction-017](#el_interaction-017) **★** | Send timeout header on builder getHeader | partial | medium | S | latency |
| [el_interaction-018](#el_interaction-018) | Use blinded-block submit V2 with empty response | implemented | medium | S | bandwidth |
| [el_interaction-019](#el_interaction-019) | Always close builder HTTP response bodies | n/a | low | S | memory |
| [el_interaction-020](#el_interaction-020) | Retry on existing EL connection instead of reconnecting | implemented | low | S | latency |
| [el_interaction-021](#el_interaction-021) | Back off redials and skip unsynced eth1 node | n/a | low | S | bandwidth |
| [el_interaction-022](#el_interaction-022) | Avoid interning addresses when decoding block access lists | n/a | low | S | cpu, latency |
| [el_interaction-023](#el_interaction-023) | Use 256-bit integers in engine API types | implemented | low | S | cpu, memory |
| [el_interaction-024](#el_interaction-024) | Decode and validate block access list once | n/a | low | S | cpu, latency |
| [el_interaction-025](#el_interaction-025) **★** | Faster JSON decoder for large engine payloads | not | medium | M | cpu, latency |
| [el_interaction-026](#el_interaction-026) | Avoid copying blobs in getBlobs and production paths | implemented | low | S | memory, cpu |
| [el_interaction-027](#el_interaction-027) | Borrow or move execution payloads instead of cloning | partial | low | M | cpu, memory |
| [el_interaction-028](#el_interaction-028) | Run without eth1 deposit follower when unneeded | n/a | low | S | bandwidth, disk, memory, startup |
| [el_interaction-029](#el_interaction-029) | Keep at most one forkchoiceUpdated in flight | implemented | medium | S | cpu, latency |
| [el_interaction-030](#el_interaction-030) | Deduplicate identical forkchoiceUpdated calls | partial | low | S | latency, cpu, bandwidth |
| [el_interaction-031](#el_interaction-031) | Batch JSON-RPC requests for eth1 block headers | n/a | low | S | latency, bandwidth, sync |
| [el_interaction-032](#el_interaction-032) | Switch to batched historical fetch when far behind | n/a | low | S | sync, latency |
| [el_interaction-033](#el_interaction-033) | Unblind blocks with batched engine_getPayloadBodies | implemented | medium | S | bandwidth, cpu, latency, memory |
| [el_interaction-034](#el_interaction-034) **★** | Store blinded blocks and fetch payloads from EL | partial | high | M | disk |
| [el_interaction-035](#el_interaction-035) | Fetch deposit logs per block range, not per block | n/a | low | S | bandwidth, latency, sync |
| [el_interaction-036](#el_interaction-036) | Batch database writes for deposit processing | n/a | low | S | cpu, disk |
| [el_interaction-037](#el_interaction-037) | Binary search deposit count per eth1 block | n/a | low | S | cpu, memory |
| [el_interaction-038](#el_interaction-038) | Bound terminal PoW block search by difficulty | n/a | low | S | bandwidth, latency |
| [el_interaction-039](#el_interaction-039) **★** | Limit and dedupe getBlobs calls per block root | partial | medium | S | bandwidth, cpu, latency, memory |
| [el_interaction-040](#el_interaction-040) | Cache eth1 blocks for eth1 data voting | n/a | low | S | bandwidth, latency, memory |
| [el_interaction-041](#el_interaction-041) | Fetch each distinct eth1 vote block once | n/a | low | S | latency, bandwidth |
| [el_interaction-042](#el_interaction-042) | Cache engine API JWT until near expiry | not | low | S | cpu |
| [el_interaction-043](#el_interaction-043) | Avoid slow serializer lookup on JWT creation | n/a | low | S | cpu, latency |
| [el_interaction-044](#el_interaction-044) | Cache justified/finalized payload hashes for fcU | implemented | low | S | disk, latency |
| [el_interaction-045](#el_interaction-045) | Cache deposit signature verification result | n/a | low | S | cpu |
| [el_interaction-046](#el_interaction-046) | Parse deposit contract ABI once | n/a | low | S | cpu, memory |
| [el_interaction-047](#el_interaction-047) | Cache chainId/net_version and poll EL less | n/a | low |  | bandwidth, cpu |
| [el_interaction-048](#el_interaction-048) | Decode persisted eth1 data once at startup | n/a | low |  | memory, startup |
| [el_interaction-049](#el_interaction-049) | Dedupe newPayload for duplicate payload envelopes | partial | low | S | cpu, latency |
| [el_interaction-050](#el_interaction-050) | Defer getBlobs call off the gossip path | partial | low | S | latency |
| [el_interaction-051](#el_interaction-051) | Derive eth1 data from deposit logs | n/a | low |  | sync, startup, bandwidth |
| [el_interaction-052](#el_interaction-052) | Persist deposit tree and restore it on restart | n/a | low |  | startup, sync |
| [el_interaction-053](#el_interaction-053) | Slot-based deadline for early-block newPayload | n/a | medium | S | latency |
| [el_interaction-054](#el_interaction-054) | Per-method engine API timeouts | implemented | medium | S | latency |
| [el_interaction-055](#el_interaction-055) | Encode engine payload once for multiple ELs | n/a | low |  | cpu, latency |
| [el_interaction-056](#el_interaction-056) | Engine API over IPC socket | not | low | M | latency, cpu |
| [el_interaction-057](#el_interaction-057) | Estimate eth1 block from timestamps | n/a | low | S | cpu, latency |
| [el_interaction-058](#el_interaction-058) | Startup shortcuts in eth1 deposit monitor | n/a | low | S | sync, startup |
| [el_interaction-059](#el_interaction-059) | Fast path for appending successor eth1 block | n/a | low | S | sync, startup |
| [el_interaction-060](#el_interaction-060) | Incremental deposit tree with larger log batches | n/a | low | S | sync, startup |
| [el_interaction-061](#el_interaction-061) | Fetch timestamps only for needed deposit blocks | n/a | low | S | latency, sync |
| [el_interaction-062](#el_interaction-062) | Websocket library without send throttling | n/a | low | S | latency, bandwidth |
| [el_interaction-063](#el_interaction-063) **★** | Send fcU after SYNCING newPayload | partial | medium | S | sync |
| [el_interaction-064](#el_interaction-064) | Send forkchoiceUpdated on slot tick | implemented | low | S | latency |
| [el_interaction-065](#el_interaction-065) | Finalize deposit tree before receiving blocks | n/a | low | S | latency, startup |
| [el_interaction-066](#el_interaction-066) **★** | Verify block hash locally, skip newPayload on finalized sync | partial | medium | S | cpu, latency, sync |
| [el_interaction-067](#el_interaction-067) | Fix busy loop in EL monitor | n/a | low | S | cpu |
| [el_interaction-068](#el_interaction-068) | Decode getBlobs response into preallocated buffers | n/a | low | S | memory, cpu |
| [el_interaction-069](#el_interaction-069) **★** | Fast hex decoding of Engine API responses | partial | medium | M | cpu, memory, latency |
| [el_interaction-070](#el_interaction-070) | In-process execution client engine calls | n/a | low | S | cpu, latency |
| [el_interaction-071](#el_interaction-071) **★** | Keep builder relay connections warm | not | medium | S | latency |
| [el_interaction-072](#el_interaction-072) | Shared HTTP client for EL requests | implemented | low | S | latency, cpu |
| [el_interaction-073](#el_interaction-073) | Persistent WebSocket transport for Engine API | not | low | M | latency, cpu |
| [el_interaction-074](#el_interaction-074) | Gzip compression on eth1 HTTP requests | not | low | S | bandwidth |
| [el_interaction-075](#el_interaction-075) | Fetch only eth1 block headers, not transactions | n/a | low | S | bandwidth, cpu |
| [el_interaction-076](#el_interaction-076) | LRU of recently unblinded payloads | not | low | S | latency, disk, cpu |
| [el_interaction-077](#el_interaction-077) **★** | Separate EL queue for payload-body serving | partial | medium | S | latency |
| [el_interaction-078](#el_interaction-078) **★** | Bound concurrent in-flight EL requests | partial | medium | S | latency, cpu |
| [el_interaction-079](#el_interaction-079) **★** | Optimistic block import when EL syncing or offline | partial | medium | M | sync, latency |
| [el_interaction-080](#el_interaction-080) **★** | Skip EL calls for already finalized blocks during sync | partial | medium | S | sync, latency |
| [el_interaction-081](#el_interaction-081) **★** | Ordered trie root for payload hash | not | medium | M | cpu |
| [el_interaction-082](#el_interaction-082) | Use latestValidHash to mark ancestor runs | partial | low | S | cpu, sync |
| [el_interaction-083](#el_interaction-083) | Persist validated merge-transition flag | n/a | low | S | cpu, latency |
| [el_interaction-084](#el_interaction-084) | Correct payload id cache key for prepared payloads | implemented | low | S | latency |
| [el_interaction-085](#el_interaction-085) | Split head FCU and payload-attributes FCU | implemented | low | S | latency |
| [el_interaction-086](#el_interaction-086) | Stable payload attributes target slot | implemented | low | S | latency |
| [el_interaction-087](#el_interaction-087) | Longer getPayload timeout without prior preparation | implemented | low | S | latency |
| [el_interaction-088](#el_interaction-088) **★** | Short getPayload deadline to fail over fast | not | medium | S | latency |
| [el_interaction-089](#el_interaction-089) | Retry getPayload with fresh preparation | partial | low | S | latency |
| [el_interaction-090](#el_interaction-090) | Do not block getPayload on parent-block wait | n/a | low | S | latency |
| [el_interaction-091](#el_interaction-091) | Notify FCU subscribers only on real sends | n/a | low | S | cpu |
| [el_interaction-092](#el_interaction-092) | Skip fcU for heads without newPayload response | n/a | low | S | latency |
| [el_interaction-093](#el_interaction-093) | Skip fcU for pre-merge blocks | n/a | low | S | cpu |
| [el_interaction-094](#el_interaction-094) | Drop exchangeTransitionConfiguration polling | implemented | low | S | cpu |
| [el_interaction-095](#el_interaction-095) | Stop builder status checks after builder removal | n/a | low | S | cpu, bandwidth |
| [el_interaction-096](#el_interaction-096) | Skip empty builder registration requests | partial | low | S | bandwidth |
| [el_interaction-097](#el_interaction-097) | Builder client fetches only slots it bid on | n/a | low |  | bandwidth, cpu |
| [el_interaction-098](#el_interaction-098) | No retries for inclusion list engine call | n/a | low |  | latency |
| [el_interaction-099](#el_interaction-099) | Per-EL state with multiple ELs, first-response getBlobs | n/a | low |  | latency |
| [el_interaction-100](#el_interaction-100) | Recheck cache after acquiring fetch lock | implemented | low | S | latency |
| [el_interaction-101](#el_interaction-101) | Single in-flight wait-for-EL-sync task | partial | low | S | cpu, memory |
| [el_interaction-102](#el_interaction-102) | Drop duplicate queued blocks before newPayload | implemented | medium | S | cpu, latency |
| [el_interaction-103](#el_interaction-103) | Skip terminal PoW block polling while syncing | n/a | low |  | cpu, bandwidth |
| [el_interaction-104](#el_interaction-104) | Stop eth1 deposit polling after EIP-6110 | implemented | low | S | cpu, bandwidth, disk |
| [el_interaction-105](#el_interaction-105) | Poll eth1 at block interval | n/a | low |  | cpu, bandwidth |
| [el_interaction-106](#el_interaction-106) | Avoid tight eth1 follower refetch loop | n/a | low | S | cpu, bandwidth |
| [el_interaction-107](#el_interaction-107) | Poll latest eth1 head instead of block filter | n/a | low | S | bandwidth |
| [el_interaction-108](#el_interaction-108) | Keep adaptive log chunk size across reconnects | n/a | low | S | sync, latency |
| [el_interaction-109](#el_interaction-109) | Load deposit tree snapshot once | n/a | low | S | startup, disk |
| [el_interaction-110](#el_interaction-110) | In-memory pending deposits store | n/a | low | S | disk, latency |
| [el_interaction-111](#el_interaction-111) | Incremental pre-genesis state from deposits | n/a | low | S | cpu, startup |
| [el_interaction-112](#el_interaction-112) | Lazy deposit iteration for proposals | n/a | low | S | memory, cpu |
| [el_interaction-113](#el_interaction-113) | Single-pass grouping of deposit events by block | n/a | low | S | cpu |
| [el_interaction-114](#el_interaction-114) | Precompute deposit log topic hash | n/a | low | S | cpu |
| [el_interaction-115](#el_interaction-115) | Pass deposit logs by pointer | n/a | low | S | memory |
| [el_interaction-116](#el_interaction-116) | No eth1 timestamp lookups in validator status | n/a | low | S | latency |
| [el_interaction-117](#el_interaction-117) | Do eth1 lookups in eth1 service, not state transition | n/a | low | S | latency |
| [el_interaction-118](#el_interaction-118) | Publish deposits as block responses arrive | n/a | low | S | latency, sync |
| [el_interaction-119](#el_interaction-119) | Update deposit tracking incrementally in background | n/a | low | S | latency |
| [el_interaction-120](#el_interaction-120) | Follow eth1 blocks, not only deposit events | n/a | low | S | sync |
| [el_interaction-121](#el_interaction-121) | Start eth1 scan at deposit contract deploy block | n/a | low | S | startup, bandwidth |
| [el_interaction-122](#el_interaction-122) | Wait until EL reaches deploy block before queries | n/a | low | S | bandwidth, cpu |
| [el_interaction-123](#el_interaction-123) | Skip genesis block search with anchor state | n/a | low | S | startup |
| [el_interaction-124](#el_interaction-124) | Fetch eth1 blocks only after a deposit event | n/a | low | S | bandwidth |
| [el_interaction-125](#el_interaction-125) | Store eth1 data only in needed window | n/a | low | S | disk, bandwidth |
| [el_interaction-126](#el_interaction-126) | Init deposit cache from finalized state | n/a | low | S | startup, cpu |
| [el_interaction-127](#el_interaction-127) | Borrow eth1 service instead of cloning | n/a | low | S | memory, cpu |
| [el_interaction-128](#el_interaction-128) | Release old RPC client on EL reconnect | implemented | low | S | memory |
| [el_interaction-129](#el_interaction-129) | In-place chunked HTTP decoding | n/a | low | S | memory, cpu |
| [el_interaction-130](#el_interaction-130) | Larger transport buffers for EL JSON-RPC | not | low | S | cpu |
| [el_interaction-131](#el_interaction-131) | Lightweight Engine API JSON-RPC client | implemented | low | S | cpu, latency |
| [el_interaction-132](#el_interaction-132) | Reuse execution requests codec instance | n/a | low | S | cpu, memory |
| [el_interaction-133](#el_interaction-133) | Reuse received transaction encodings | n/a | medium | S | cpu |
| [el_interaction-134](#el_interaction-134) | Single allocation for prefixed serialization | partial | low | S | memory, cpu |
| [el_interaction-135](#el_interaction-135) | Semaphore wake instead of poll loop | n/a | low | S | latency |
| [el_interaction-136](#el_interaction-136) | Parallel trie prefetch for state root | n/a | low | L | disk, latency |
| [el_interaction-137](#el_interaction-137) | Reject invalid block access list early | n/a | low | M | cpu |
| [el_interaction-138](#el_interaction-138) | Persist block access list for state read-ahead | n/a | low |  | cpu, latency |
| [el_interaction-139](#el_interaction-139) | Cache terminal PoW block lookups | n/a | low |  | latency, cpu |
| [el_interaction-140](#el_interaction-140) | Sparse checkpointed eth1 block scan for genesis | n/a | low |  | startup, sync |
| [el_interaction-141](#el_interaction-141) | Poll eth1 fast while behind, slow once caught up | n/a | low |  | sync, latency |
| [el_interaction-142](#el_interaction-142) | Single-pass typed decoding of block transactions | n/a | low |  | cpu, memory |
| [el_interaction-143](#el_interaction-143) | Fetch single payload body by hash | implemented | low | S | latency |
| [el_interaction-144](#el_interaction-144) | Bundle deposit tree snapshot per network | n/a | low |  | startup, sync |
| [el_interaction-145](#el_interaction-145) | Cache engine capabilities and client version | implemented | low | S | latency |
| [el_interaction-146](#el_interaction-146) | Check genesis readiness via contract constant | n/a | low |  | startup |
| [el_interaction-147](#el_interaction-147) | Drop redundant builder relay status request | implemented | low | S | latency, bandwidth |
| [el_interaction-148](#el_interaction-148) | Ask EL which blobs it holds via hasBlobs | partial | low | M | bandwidth, latency |
| [el_interaction-149](#el_interaction-149) | Refuse duties and block production when EL is unhealthy | partial | low | S | latency, cpu |
| [el_interaction-150](#el_interaction-150) | Hardcode terminal block hash per known network | n/a | low |  | startup, latency |
| [el_interaction-151](#el_interaction-151) | Resolve engine API method by milestone via map | n/a | low |  | cpu |
| [el_interaction-152](#el_interaction-152) | Parallelize block-by-hash and payload-bodies EL calls | n/a | low |  | latency |
| [el_interaction-153](#el_interaction-153) | Pass call-trace frames by pointer | n/a | low |  | cpu, memory |
| [el_interaction-154](#el_interaction-154) | Publish EL-built columns to all gossip subnets | not | low | M | bandwidth, latency |
| [el_interaction-155](#el_interaction-155) | Resume deposit log scan from last processed block | n/a | low |  | sync, startup |
| [el_interaction-156](#el_interaction-156) | Send builder registrations sequentially for one-per-call builders | n/a | low |  | latency, cpu |
| [el_interaction-157](#el_interaction-157) | Share one eth1 head block lookup across caches | n/a | low |  | latency |
| [el_interaction-158](#el_interaction-158) | Shrink engine request message slot size | n/a | low |  | memory |

★ actionable. Click an id for the full record.

## Ideas

<a id="el_interaction-001"></a>
<details>
<summary><b>el_interaction-001</b> Fetch blobs from EL to build sidecars locally — <i>implemented · high · S · bandwidth, cpu, latency</i></summary>

**Idea.** When a block or first data column sidecar arrives, call engine_getBlobs (V1/V2) to pull its blobs and proofs from the local EL blob pool and build blob or data column sidecars locally. This skips waiting for gossip or downloading from peers, and lets the node publish the sidecars itself.

**Impact.** Saves column downloads and gossip waiting on block import.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1934-1941`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1934-L1941) process_gossip_verified_block spawns spawn_fetch_block_columns right after gossip verification
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1118-1133`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1118-L1133) getBlobs triggered on first partial-column header
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:210-222`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L210-L222) RPC block path
- [`beacon_node/http_api/src/publish_blocks.rs:224`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L224) HTTP publish path
- [`beacon_node/network/src/network_beacon_processor/mod.rs:998-1040`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L998-L1040) fetch_engine_blobs_and_publish_full publishes columns gradually
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:190-300`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L190-L300) get_blobs_v2/v3 builds custody columns

**Skeptic check.** Verified on the gossip, RPC and HTTP block paths and on the partial-header path, with local publishing. A full (non-partial) DataColumnSidecar that arrives before the block does not trigger getBlobs (process_gossip_verified_data_column), but the block trigger covers the common case.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#15469](https://github.com/OffchainLabs/prysm/pull/15469), [prysm#14513](https://github.com/OffchainLabs/prysm/pull/14513), [teku#8662](https://github.com/Consensys-Incorporated/teku/pull/8662), [grandine@047520e97](https://github.com/grandinetech/grandine/commit/047520e97856), [lighthouse#6268](https://github.com/sigp/lighthouse/pull/6268), [lighthouse#5829](https://github.com/sigp/lighthouse/pull/5829), [grandine#258](https://github.com/grandinetech/grandine/pull/258), [caplin#17829](https://github.com/erigontech/erigon/pull/17829), [nimbus#7365](https://github.com/status-im/nimbus-eth2/pull/7365)

</details>


<a id="el_interaction-002"></a>
<details>
<summary><b>el_interaction-002</b> Use getBlobsV4 to build partial columns from sparse blobpools — <i>implemented · high · S · bandwidth, latency</i></summary>

**Idea.** Call engine_getBlobsV4 to get cells for the blobs the EL has, even when it holds only part of them, and build partial data columns locally. This reduces column downloads from peers when the EL blob pool is sparse.

**Impact.** Cuts column downloads when the EL blobpool is sparse.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:161`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L161) uses V4 when supports_get_blobs_v4
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:405-440`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L405-L440) fetch_and_process_blobs_v4 requests custody cells
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:531`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L531) build_partial_columns_from_v4_response
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:317`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L317) import_custody_partial_columns merges into partial assembler / pending payload cache
- [`beacon_node/network/src/network_beacon_processor/mod.rs:989`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L989) publish_partial_data_columns after fetch
- [`beacon_node/execution_layer/src/engine_api.rs:673`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api.rs#L673),746 get_blobs_v4 capability

**Skeptic check.** Verified the V4 sparse response is turned into partial columns that are merged and published, for both Fulu and Gloas. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#9438](https://github.com/sigp/lighthouse/pull/9438), [prysm#17378](https://github.com/OffchainLabs/prysm/pull/17378), [nimbus#9034](https://github.com/status-im/nimbus-eth2/pull/9034), [nimbus#9194](https://github.com/status-im/nimbus-eth2/pull/9194)

</details>


<a id="el_interaction-003"></a>
<details>
<summary><b>el_interaction-003</b> Fetch blobs from EL during range sync too — <i>not · medium · M · sync, latency</i></summary>

**Idea.** Also during sync, on the first received column sidecar call getBlobsV2 to build the remaining columns locally, and retry block import once half of the sampled columns are present. The node does not wait for peers to serve every column.

**Gap in Lighthouse.** Range/backfill sync batches download all custody columns from peers; there is no getBlobsV2 call on first column or batch, and no early import once enough columns are local. Would need range batch requests to consult the EL for recent blocks and mark columns as satisfied.

**Impact.** Lower column download volume and faster range sync near head while blobs are still in the EL blobpool; little effect for deep syncs.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:209-231`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L209-L231) getBlobs only after single-block lookup returns MissingComponents
- [`beacon_node/network/src/network_beacon_processor/mod.rs:960-995`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L960-L995) spawn_fetch_block_columns (gossip/RPC/HTTP sources only)
- [`beacon_node/network/src/service.rs:697`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L697) and gossip_methods.rs:1123,1936 gossip triggers
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:497-641`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L497-L641) chain segment import path has no EL blob fetch
- [`beacon_node/network/src/sync`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync)/ contains no fetch_blobs/get_blobs call (only a test mock at range_data_column_batch_request.rs:327)

**Second check.** Grepped all callers of fetch_engine_blobs_and_publish_full/spawn_fetch_block_columns and the whole sync/ directory for EL blob access; only gossip, HTTP and single-lookup paths use it.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [grandine@efc07cb58](https://github.com/grandinetech/grandine/commit/efc07cb58225)

</details>


<a id="el_interaction-004"></a>
<details>
<summary><b>el_interaction-004</b> SSZ over REST transport for the engine API — <i>not · medium · L · cpu, latency, bandwidth</i></summary>

**Idea.** Talk to the execution client over REST endpoints with SSZ bodies (optionally HTTP/2, negotiated through capabilities, with JSON-RPC fallback) for newPayload, forkchoiceUpdated, getPayload and getBlobs. Binary SSZ avoids hex-JSON encoding/decoding and roughly halves or better the wire size of large blob payloads; blob responses can be decoded as views without copies.

**Gap in Lighthouse.** Add an SSZ REST transport (optionally HTTP/2) next to HttpJsonRpc with capability negotiation and JSON-RPC fallback for newPayload, forkchoiceUpdated, getPayload and getBlobs, plus SSZ request/response types. The listed Lighthouse PRs are not merged in this checkout.

**Impact.** Removes hex-JSON encode/decode and shrinks large blob/payload bodies; reported getBlobsV2 roundtrip up to 17x faster.

**Best measured result.** Payload body 4.7x smaller; getBlobsV2 roundtrip 17x faster on average (pr:prysm#16901)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engine_api/http.rs:661-694`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L661-L694) rpc_request sends application/json and decodes JSON only
- [`beacon_node/execution_layer/src/engine_api`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api)/ contains only auth.rs, http.rs, json_structures.rs, new_payload_request.rs
- [`beacon_node/execution_layer/src/engine_api/http.rs:65`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L65) capability exchange is JSON-RPC method names only

**Second check.** Checked the request builder for any non-JSON content type and the engine_api module for alternative transports; the only SSZ use in http.rs is decoding deposit/withdrawal request fields inside JSON.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [lighthouse#10505](https://github.com/sigp/lighthouse/pull/10505), [lodestar#8994](https://github.com/ChainSafe/lodestar/pull/8994), [lighthouse#9652](https://github.com/sigp/lighthouse/pull/9652), [lodestar#10204](https://github.com/ChainSafe/lodestar/pull/10204), [prysm#16447](https://github.com/OffchainLabs/prysm/pull/16447), [lighthouse#10242](https://github.com/sigp/lighthouse/pull/10242), [prysm#16901](https://github.com/OffchainLabs/prysm/pull/16901), [nimbus#8895](https://github.com/status-im/nimbus-eth2/pull/8895), [nimbus#9048](https://github.com/status-im/nimbus-eth2/pull/9048), [prysm#16784](https://github.com/OffchainLabs/prysm/pull/16784), [teku#10455](https://github.com/Consensys-Incorporated/teku/pull/10455), [lighthouse#8937](https://github.com/sigp/lighthouse/pull/8937)

</details>


<a id="el_interaction-005"></a>
<details>
<summary><b>el_interaction-005</b> SSZ encoding for builder API calls — <i>partial · medium · S · bandwidth, cpu, latency</i></summary>

**Idea.** Use SSZ instead of JSON for builder API getHeader, submitBlindedBlock and validator registration requests and responses, with JSON fallback (for example on 415 or missing headers), and forward the original received SSZ block bytes to the builder without re-serialization. SSZ is smaller and cheaper to encode/decode than JSON.

**Gap in Lighthouse.** SSZ is used for getHeader responses and blinded block submission with JSON fallback. Missing: SSZ for validator registrations, and forwarding the original SSZ bytes received from the VC instead of re-encoding.

**Impact.** Small: registration bursts get cheaper encoding; skipping a re-encode of a blinded block saves microseconds.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/builder_client/src/pre_gloas_builder_http_client.rs:380`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/builder_client/src/pre_gloas_builder_http_client.rs#L380) getHeader Accept prefers SSZ unless disable_ssz
- [`beacon_node/builder_client/src/pre_gloas_builder_http_client.rs:263`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/builder_client/src/pre_gloas_builder_http_client.rs#L263) post_builder_blinded_blocks_v2_ssz sends SSZ body
- [`beacon_node/builder_client/src/pre_gloas_builder_http_client.rs:269`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/builder_client/src/pre_gloas_builder_http_client.rs#L269) blinded_block.as_ssz_bytes() re-encodes
- [`beacon_node/builder_client/src/pre_gloas_builder_http_client.rs:257`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/builder_client/src/pre_gloas_builder_http_client.rs#L257) post_builder_validators uses post_generic (JSON)
- [`beacon_node/builder_client/src/builder_http_client.rs:305`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/builder_client/src/builder_http_client.rs#L305) Gloas builder client also SSZ for block submit, no SSZ registration path
- [`beacon_node/execution_layer/src/lib.rs:1851`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1851) propose_blinded_beacon_block calls the SSZ submit when available

**Second check.** Also checked the new Gloas builder_http_client.rs: it adds SSZ bid responses and SSZ block submit, but registrations stay JSON there too and no raw-bytes passthrough exists.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [lodestar#7180](https://github.com/ChainSafe/lodestar/pull/7180), [lodestar#7444](https://github.com/ChainSafe/lodestar/pull/7444), [lighthouse#6859](https://github.com/sigp/lighthouse/pull/6859), [prysm#14976](https://github.com/OffchainLabs/prysm/pull/14976), [lodestar#7185](https://github.com/ChainSafe/lodestar/pull/7185), [grandine@29926b328](https://github.com/grandinetech/grandine/commit/29926b328d3e), [lighthouse#7009](https://github.com/sigp/lighthouse/pull/7009), [teku#8994](https://github.com/Consensys-Incorporated/teku/pull/8994), [teku#9065](https://github.com/Consensys-Incorporated/teku/pull/9065)

</details>


<a id="el_interaction-006"></a>
<details>
<summary><b>el_interaction-006</b> Send forkchoiceUpdated immediately after payload import — <i>implemented · medium · S · latency</i></summary>

**Idea.** After an execution payload is imported (for example a separate payload envelope), send forkchoiceUpdated to the EL at once instead of waiting for the next block or slot tick. The EL learns the new head hash as early as possible.

**Impact.** The EL learns the new payload head hash as soon as the envelope is imported, on gossip and RPC paths.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:4083-4084`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L4083-L4084) recompute_head_at_current_slot right after an Imported envelope on gossip
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:361-362`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L361-L362) same on the RPC envelope path
- [`beacon_node/beacon_chain/src/canonical_head.rs:1087-1096`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1087-L1096) early return only when view, payload status and fcU params are all unchanged, so an EMPTY-&gt;FULL switch proceeds
- [`consensus/fork_choice/src/fork_choice.rs:592-597`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L592-L597) head_hash taken from head_payload_block_hash(head_payload_status)
- [`beacon_node/beacon_chain/src/canonical_head.rs:1907-1914`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1907-L1914) update_execution_engine_forkchoice is spawned on the head change

**Skeptic check.** Verified that a payload-status change alone (same block root) passes the early-return check and triggers fcU with the payload's block hash. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#9285](https://github.com/ChainSafe/lodestar/pull/9285)

</details>


<a id="el_interaction-007"></a>
<details>
<summary><b>el_interaction-007</b> Drive EL sync from light-client head — <i>not · medium · L · sync</i></summary>

**Idea.** While the beacon chain DAG is behind, pass the light-client head execution block hash to the EL through forkchoiceUpdated (light-client sync on by default). The EL syncs to the wall slot in parallel with the CL forward sync.

**Gap in Lighthouse.** No light-client consumer or sync-committee follower exists in Lighthouse; while syncing, the EL only gets the CL's own lagging head. Needs a light-client follow component and a fcU path that sends the LC head hash while the CL is behind.

**Impact.** Helps only initial or long-range sync: the EL could sync to the tip in parallel with the CL.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/client/src/builder.rs:272`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L272) light client is server-only (enable_light_client_server)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7180`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7180) update_execution_engine_forkchoice sends only the fork-choice head

**Second check.** Searched network/src/sync and canonical_head/beacon_chain for any light-client bootstrap/update consumer or alternative head hash sent to the EL; found none.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [nimbus#4041](https://github.com/status-im/nimbus-eth2/pull/4041), [nimbus#4805](https://github.com/status-im/nimbus-eth2/pull/4805)

</details>


<a id="el_interaction-008"></a>
<details>
<summary><b>el_interaction-008</b> Light-client optimistic sync follows gossip directly — <i>n/a · low · S · latency</i></summary>

**Idea.** In light-client driven optimistic sync, import any gossip block whose parent has execution enabled, without waiting for the justified checkpoint or sync-manager logic. This cuts latency to the head.

**Impact.** Lighthouse has no light-client-driven optimistic sync mode; nothing to change.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src): no light-client driven sync; block import is via gossip + sync manager

**Sources.** [nimbus#4002](https://github.com/status-im/nimbus-eth2/pull/4002)

</details>


<a id="el_interaction-009"></a>
<details>
<summary><b>el_interaction-009</b> Fetch historical deposit logs over HTTP, not websocket — <i>n/a · low · S · startup, sync</i></summary>

**Idea.** At startup, fetch historical deposit contract logs over HTTP RPC instead of websocket to avoid message-size limits; use websocket only for subscribing to new logs.

**Impact.** Eth1 deposit log fetching is no longer used by the beacon node (deposits come via EIP-6110 requests); no startup cost.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engine_api/http.rs:549`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L549) get_deposit_logs_in_range defined but has no caller (grep)

**Sources.** [prysm#2299](https://github.com/OffchainLabs/prysm/pull/2299)

</details>


<a id="el_interaction-010"></a>
<details>
<summary><b>el_interaction-010</b> Bounded, adaptive eth1 log/block query ranges — <i>n/a · low · S · latency, memory, sync</i></summary>

**Idea.** Cap the block range (for example 1000 blocks) and the number of concurrent requests per eth_getLogs / eth1 block query, shrink the range on timeout or known range errors and grow it slowly after success. Large catch-ups then use bounded requests and memory and do not overload or time out the EL.

**Impact.** No eth_getLogs catch-up runs, so bounded adaptive ranges have nothing to improve.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engine_api/http.rs:549`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L549) eth_getLogs helper is dead code; no eth1 service dir in beacon_node

**Sources.** [teku#3182](https://github.com/Consensys-Incorporated/teku/pull/3182), [teku#6061](https://github.com/Consensys-Incorporated/teku/pull/6061), [lodestar#4532](https://github.com/ChainSafe/lodestar/pull/4532), [teku#2485](https://github.com/Consensys-Incorporated/teku/pull/2485), [lodestar@e586ecd1a](https://github.com/ChainSafe/lodestar/commit/e586ecd1a856), [prysm#5027](https://github.com/OffchainLabs/prysm/pull/5027), [teku#6180](https://github.com/Consensys-Incorporated/teku/pull/6180)

</details>


<a id="el_interaction-011"></a>
<details>
<summary><b>el_interaction-011</b> Send early forkchoiceUpdated with payload attributes — <i>implemented · medium · S · latency</i></summary>

**Idea.** When a local validator proposes in the next slot, send forkchoiceUpdated with payload attributes ahead of time (one slot early, or immediately when a timely block does not become head) and cache the payload id. Block production then gets an already-built payload instead of waiting for the EL.

**Impact.** Already done; payload is built during the previous slot and fetched by cached payload id.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/proposer_prep_service.rs:37`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/proposer_prep_service.rs#L37) fires prepare_beacon_proposer at slot end minus prepare_payload_lookahead (4s, chain_config.rs:166)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7126`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7126) sends fcU with cached payload attributes when within lookahead
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:212`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L212) recompute head early then prepare_beacon_proposer late in the slot
- [`beacon_node/beacon_chain/src/canonical_head.rs:1931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1931) prepare_beacon_proposer after every head change
- [`beacon_node/execution_layer/src/engines.rs:149`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engines.rs#L149) get_payload_id cache filled at engines.rs:176

**Skeptic check.** Verified the lookahead fcU with attributes from three triggers and the payload_id LRU cache read by get_payload; earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#3965](https://github.com/ChainSafe/lodestar/pull/3965), [prysm#11919](https://github.com/OffchainLabs/prysm/pull/11919)

</details>


<a id="el_interaction-012"></a>
<details>
<summary><b>el_interaction-012</b> Prepare payloads only for imminent local proposals — <i>partial · low · S · cpu, latency, sync</i></summary>

**Idea.** Send the proposer-preparation forkchoiceUpdated with payload attributes (and the state advance to find the proposer) only when a registered local validator proposes in the next slot, and skip it while the head is far behind the wall slot or optimistic. This avoids wasted EL payload builds and state rewinds for blocks that would not be used.

**Gap in Lighthouse.** Missing: no skip while head is optimistic, and the head-too-far-behind threshold is sync_tolerance_epochs (8 epochs) rather than about one slot. Add an optimistic check and a tighter lag bound in prepare_beacon_proposer.

**Impact.** Saves some wasted EL payload builds during sync/optimistic periods; negligible on a healthy mainnet node.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:6741`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6741) skips when no proposer preparation data registered
- [`beacon_node/beacon_chain/src/beacon_chain.rs:6757-6764`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6757-L6764) skips when head older than sync_tolerance_epochs
- [`beacon_node/beacon_chain/src/beacon_chain.rs:6895`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6895) checks has_proposer_preparation_data(proposer) for the next-slot proposer before fcU with attributes

**Sources.** [grandine@09dd08120](https://github.com/grandinetech/grandine/commit/09dd081200f4), [nimbus#4055](https://github.com/status-im/nimbus-eth2/pull/4055), [nimbus#4093](https://github.com/status-im/nimbus-eth2/pull/4093), [teku#4707](https://github.com/Consensys-Incorporated/teku/pull/4707)

</details>


<a id="el_interaction-013"></a>
<details>
<summary><b>el_interaction-013</b> Correct withdrawals in lookahead proposal fcU — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** At epoch boundaries, compute the withdrawals for the lookahead proposal forkchoiceUpdated from the correct (advanced) state, so the EL can use the early payload build instead of discarding it.

**Impact.** Lookahead fcU withdrawals are computed from a state advanced across the epoch boundary, so the early build is valid.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5396-5490`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5396-L5490) compute_withdrawals_for_payload_attributes: partial_state_advance to proposal_slot, then get_expected_withdrawals on the advanced state
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5464-5485`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5464-L5485) applies the parent execution requests for a Full Gloas parent before computing withdrawals
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5432-5441`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5432-L5441) an Empty parent reuses payload_expected_withdrawals
- [`beacon_node/beacon_chain/src/beacon_chain.rs:6954-6999`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6954-L6999) attributes are cached via insert_proposer and reused by the fcU

**Skeptic check.** Confirmed the state is advanced to proposal_slot (crossing the epoch boundary) before get_expected_withdrawals. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#4820](https://github.com/status-im/nimbus-eth2/pull/4820)

</details>


<a id="el_interaction-014"></a>
<details>
<summary><b>el_interaction-014</b> Skip missing-payload-id fill when slot block seen — <i>partial · low · S · cpu, latency</i></summary>

**Idea.** Skip the extra forkchoiceUpdated with attributes that fills a missing payload id when a block for the current slot was already received; it is only needed for missed slots.

**Gap in Lighthouse.** LH has no Prysm-style fill routine, but prepare_beacon_proposer has no dedupe. When the state_advance_timer runs it near the slot end, it re-sends a forkchoiceUpdated with the same head and attributes as the proposer_prep_service call ~3.5s earlier, even if the head and attributes have not changed (the slot block was seen and no re-org override applies). update_execution_engine_forkchoice and notify_forkchoice_updated do not skip identical (fcU params, attributes) pairs.

**Impact.** At most one redundant fcU-with-attributes per proposal slot. The EL returns the existing payload id, so the saving is one engine RPC: marginal.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/proposer_prep_service.rs:33-55`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/proposer_prep_service.rs#L33-L55) prepare_beacon_proposer fires every slot at prepare_payload_lookahead (slot/3) before the next slot
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:200-217`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L200-L217) a second prepare_beacon_proposer at fork_choice_instant (slot/24 before the next slot), unconditionally
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7123-7140`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7123-L7140) prepare_beacon_proposer sends fcU with attributes whenever till_prepare_slot &lt;= lookahead, with no check that the same head and attributes were already sent
- [`beacon_node/execution_layer/src/lib.rs:1342-1380`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1342-L1380) the get_payload cache-miss fcU is on demand only

**Skeptic check.** The earlier claim that the only extra fcU is the on-demand cache miss is wrong: the state_advance_timer adds a second unconditional prepare-proposer fcU. Its stated purpose is the abandoned re-org case, and it is not gated on that case.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [prysm#11669](https://github.com/OffchainLabs/prysm/pull/11669)

</details>


<a id="el_interaction-015"></a>
<details>
<summary><b>el_interaction-015</b> Async builder HTTP client with dedicated connection pool — <i>partial · low · S · latency, cpu</i></summary>

**Idea.** Make builder API requests with native async HTTP calls on a dedicated connection pool with long keep-alive, instead of blocking calls on a worker pool. This frees threads and avoids reconnect handshakes mid-epoch.

**Gap in Lighthouse.** The async and dedicated-pool parts are present. The long keep-alive part (Teku: 10-minute pool keep-alive) is missing: BuilderHttpClient::new and the pre-Gloas client use reqwest's default 90s pool_idle_timeout. Builder calls come once per proposal or once per epoch, more than 90s apart, so each getHeader/bid request after idle pays a new TCP+TLS handshake. Fix: set pool_idle_timeout(~10 min) and tcp_keepalive in the builder ClientBuilder.

**Impact.** Saves one TCP+TLS handshake (tens of ms to a remote relay) on the proposal-critical builder request.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/builder_client/src/builder_http_client.rs:82-86`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/builder_client/src/builder_http_client.rs#L82-L86) BuilderHttpClient::new builds async reqwest clients once (dedicated pool) with default settings
- [`beacon_node/builder_client/src/pre_gloas_builder_http_client.rs:81`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/builder_client/src/pre_gloas_builder_http_client.rs#L81) same, defaults
- no pool_idle_timeout / tcp_keepalive set anywhere in [`beacon_node/builder_client/src`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/builder_client/src)

**Skeptic check.** Confirmed native async and a reused client, so there is no thread blocking. The earlier evidence named the keep-alive gap but still said implemented. The keep-alive is an explicit part of the idea, so the verdict is partial.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [teku#11300](https://github.com/Consensys-Incorporated/teku/pull/11300)

</details>


<a id="el_interaction-016"></a>
<details>
<summary><b>el_interaction-016</b> Exempt critical builder calls from request throttling — <i>n/a · medium · latency</i></summary>

**Idea.** Do not route getHeader and getPayload builder calls through the throttler used for validator registrations, and cap non-critical concurrency, so registration batches cannot delay critical-path calls.

**Gap in Lighthouse.** Lighthouse has no shared throttler between registrations and getHeader/getPayload: registrations are forwarded as a separate task per VC request, so the Teku problem of registrations queueing ahead of critical calls does not exist (concurrency is just uncapped).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/validator/mod.rs:813`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L813) registrations forwarded in own spawned task
- [`beacon_node/builder_client/src/pre_gloas_builder_http_client.rs:81`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/builder_client/src/pre_gloas_builder_http_client.rs#L81) plain reqwest client, no throttler

**Sources.** [teku#9780](https://github.com/Consensys-Incorporated/teku/pull/9780)

</details>


<a id="el_interaction-017"></a>
<details>
<summary><b>el_interaction-017</b> Send timeout header on builder getHeader — <i>partial · medium · S · latency</i></summary>

**Idea.** Include a timeout header in the builder getHeader/bid request so the relay knows the deadline and responds in time.

**Gap in Lighthouse.** Gloas bid path sends X-Timeout-Ms and Date-Milliseconds; the pre-Gloas get_builder_header used on current forks does not. Add the header (timeouts.get_header in ms) there.

**Impact.** Lets relays fit their work into the 1 s deadline; fewer late or missed bids. No CPU saving on the node.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/builder_client/src/builder_http_client.rs:30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/builder_client/src/builder_http_client.rs#L30) X_TIMEOUT_MS header defined and sent on Gloas bid request (line 132)
- [`beacon_node/builder_client/src/bid_streams.rs:682`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/builder_client/src/bid_streams.rs#L682) X-Timeout-Ms on bid streams
- [`beacon_node/builder_client/src/pre_gloas_builder_http_client.rs:361`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/builder_client/src/pre_gloas_builder_http_client.rs#L361) get_builder_header sends only Accept, no timeout header

**Second check.** Grepped the whole repo for X-Timeout/Date-Milliseconds: only the Gloas client and bid streams set them.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [nimbus#8960](https://github.com/status-im/nimbus-eth2/pull/8960)

</details>


<a id="el_interaction-018"></a>
<details>
<summary><b>el_interaction-018</b> Use blinded-block submit V2 with empty response — <i>implemented · medium · S · bandwidth</i></summary>

**Idea.** Submit blinded blocks with the builder submitBlindedBlockV2 endpoint, which returns an empty response instead of the full payload and blob bundle, because the relay publishes the block itself.

**Impact.** Already done.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/lib.rs:1826`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1826) propose_blinded_beacon_block only calls post_builder_blinded_blocks_v2
- [`beacon_node/builder_client/src/pre_gloas_builder_http_client.rs:263`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/builder_client/src/pre_gloas_builder_http_client.rs#L263) POST /eth/v2/builder/blinded_blocks SSZ, :304 expects 202 with no body
- [`beacon_node/builder_client/src/pre_gloas_builder_http_client.rs:313`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/builder_client/src/pre_gloas_builder_http_client.rs#L313) JSON variant

**Skeptic check.** Confirmed the v2 endpoint is the sole submit path and returns () without downloading the payload; no v1 caller remains.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#8055](https://github.com/ChainSafe/lodestar/pull/8055)

</details>


<a id="el_interaction-019"></a>
<details>
<summary><b>el_interaction-019</b> Always close builder HTTP response bodies — <i>n/a · low · S · memory</i></summary>

**Idea.** Close every HTTP response body in the builder REST client, including on error paths, so connections and buffers are not leaked.

**Impact.** Rust drops response bodies automatically, so no leak.

**Evidence (Lighthouse @ 928b61e719).**

- builder_client uses reqwest; bodies consumed or dropped (RAII) on error paths

**Sources.** [teku#5758](https://github.com/Consensys-Incorporated/teku/pull/5758)

</details>


<a id="el_interaction-020"></a>
<details>
<summary><b>el_interaction-020</b> Retry on existing EL connection instead of reconnecting — <i>implemented · low · S · latency</i></summary>

**Idea.** Do not tear down and reconnect the execution client connection when no RPC call failed; retry calls on the existing connection.

**Impact.** There is never an explicit reconnect; reqwest's pool reuses connections and recovers on its own.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engine_api/http.rs:632-655`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L632-L655) one reqwest Client per HttpJsonRpc, built once
- [`beacon_node/execution_layer/src/engines.rs:352-385`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engines.rs#L352-L385) Engine::request runs the call regardless of state; on success or failure it only spawns an upcheck, with no client teardown

**Skeptic check.** Verified that there is no reconnect or client rebuild path on state transitions. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#14567](https://github.com/OffchainLabs/prysm/pull/14567)

</details>


<a id="el_interaction-021"></a>
<details>
<summary><b>el_interaction-021</b> Back off redials and skip unsynced eth1 node — <i>n/a · low · S · bandwidth</i></summary>

**Idea.** Do not request data from an execution node that reports it is not synced, and back off between redial attempts.

**Impact.** None; no eth1 follower to redial.

**Evidence (Lighthouse @ 928b61e719).**

- beacon_node/ has no eth1 crate; deposit logs come in-payload via EIP-6110 deposit requests (execution_layer/src/engine_api/json_structures.rs)

**Sources.** [prysm#6265](https://github.com/OffchainLabs/prysm/pull/6265)

</details>


<a id="el_interaction-022"></a>
<details>
<summary><b>el_interaction-022</b> Avoid interning addresses when decoding block access lists — <i>n/a · low · S · cpu, latency</i></summary>

**Idea.** Decode block access list addresses in newPayload as plain 20-byte values and intern them only where needed, instead of interning every address on the request path.

**Impact.** Lighthouse never decodes BAL addresses, so there is no interning cost to avoid.

**Best measured result.** 41 slow blocks sum 716-757 ms -&gt; 431-471 ms; p50 13.7-15.4 -&gt; 7.4-9.3 ms (pr:caplin#24024)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/execution/execution_payload.rs:33`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/execution/execution_payload.rs#L33) BlockAccessList = ProgressiveVariableList&lt;u8&gt;, opaque bytes
- [`beacon_node/execution_layer/src/engine_api/json_structures.rs:127`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/json_structures.rs#L127) passed through untouched

**Sources.** [caplin#24024](https://github.com/erigontech/erigon/pull/24024)

</details>


<a id="el_interaction-023"></a>
<details>
<summary><b>el_interaction-023</b> Use 256-bit integers in engine API types — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Represent baseFeePerGas, blockValue and similar engine API fields as fixed 256-bit integers instead of big integers, avoiding conversions and allocations per payload.

**Impact.** Fixed-size U256 already; no bigint allocations.

**Best measured result.** decode 35 -&gt; 33 allocs, encode 40 -&gt; 36 allocs; time within noise (pr:caplin#24016)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/core/mod.rs:54`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/core/mod.rs#L54) Uint256 = alloy_primitives::U256
- [`beacon_node/execution_layer/src/engine_api/json_structures.rs:99`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/json_structures.rs#L99) base_fee_per_gas: Uint256 via u256_hex_be
- [`beacon_node/execution_layer/src/engine_api/json_structures.rs:710`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/json_structures.rs#L710) block_value: Uint256

**Skeptic check.** Uint256 is alloy's stack U256 and the JSON types use it directly; earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#24016](https://github.com/erigontech/erigon/pull/24016)

</details>


<a id="el_interaction-024"></a>
<details>
<summary><b>el_interaction-024</b> Decode and validate block access list once — <i>n/a · low · S · cpu, latency</i></summary>

**Idea.** Decode and validate an incoming block access list once at the engine API entry, and carry the raw bytes plus the decoded value with memoized hash through later stages, instead of re-decoding and re-validating per stage; reject statically invalid lists before execution.

**Impact.** The CL treats the block access list as opaque bytes (RLP is the EL's job), so there is no decode or validation to dedupe; only one keccak in block hash check.

**Best measured result.** RLP decode 4-&gt;1, encode 1-&gt;0, validation 7-&gt;1 per newPayload (pr:caplin#23417)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/execution/execution_payload.rs:33`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/execution/execution_payload.rs#L33) BlockAccessList = ProgressiveVariableList&lt;u8&gt;
- [`beacon_node/execution_layer/src/block_hash.rs:45`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/block_hash.rs#L45) only keccak256 of the raw bytes

**Sources.** [caplin#23417](https://github.com/erigontech/erigon/pull/23417)

</details>


<a id="el_interaction-025"></a>
<details>
<summary><b>el_interaction-025</b> Faster JSON decoder for large engine payloads — <i>not · medium · M · cpu, latency</i></summary>

**Idea.** Use a faster JSON/hex decoder for large engine API payload bodies (around 1 MB, mostly hex transactions or access lists), because JSON validation and decoding cost several ms per newPayload.

**Gap in Lighthouse.** Engine responses go body -&gt; serde_json::Value -&gt; typed struct, with hex transactions decoded via ssz_types hex serde helpers. Deserialize directly into D (generic result or RawValue), consider a faster JSON/hex decoder, and avoid building params as serde_json::Value on the request side.

**Impact.** Could cut several ms from getPayload/newPayload with ~1 MB bodies; newPayload is on the block import critical path.

**Best measured result.** request-&gt;handling p50 8.16-8.26 -&gt; 3.02-3.34 ms; newPayload p50 11.9 -&gt; 7.0 ms (pr:caplin#24017)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engine_api/http.rs:694`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L694) body parsed by reqwest .json() into JsonResponseBody
- [`beacon_node/execution_layer/src/engine_api/json_structures.rs:38`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/json_structures.rs#L38) result is serde_json::Value (full tree)
- [`beacon_node/execution_layer/src/engine_api/http.rs:697`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L697) serde_json::from_value second pass
- Cargo.toml:230 plain serde_json, no simd_json/sonic

**Second check.** Searched for simd_json, sonic, RawValue and any SSZ engine transport in execution_layer; none exist.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [caplin#24017](https://github.com/erigontech/erigon/pull/24017)

</details>


<a id="el_interaction-026"></a>
<details>
<summary><b>el_interaction-026</b> Avoid copying blobs in getBlobs and production paths — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** Move or borrow 128 KiB blobs (and keep blobs, commitments and proofs together as one bundle) through getBlobs handling and block production instead of copying or converting each list. This avoids large stack use and duplicated memory.

**Impact.** There are no per-blob 128 KiB copies on the engine getBlobs or block-production paths.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:655-690`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L655-L690) blobs_and_proofs moved into the blocking task and passed by reference to blobs_to_partial_data_columns
- [`beacon_node/beacon_chain/src/kzg_utils.rs:288-294`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L288-L294) blobs_to_data_column_sidecars takes &amp;[&amp;Blob]
- [`beacon_node/beacon_chain/src/block_production/gloas.rs:916-932`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/gloas.rs#L916-L932) production blobs wrapped once in Arc and shared with the pending envelope cache (Arc clone only)

**Skeptic check.** Confirmed move/borrow semantics on both paths. The remaining copies are 2 KiB cell clones in the getBlobsV4 partial-column builder (fetch_blobs/mod.rs:565) and a per-blob clone in the beacon API blobs endpoint (http_api/src/block_id.rs:451). Neither is the path the idea targets.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#8526](https://github.com/status-im/nimbus-eth2/pull/8526), [nimbus#5562](https://github.com/status-im/nimbus-eth2/pull/5562)

</details>


<a id="el_interaction-027"></a>
<details>
<summary><b>el_interaction-027</b> Borrow or move execution payloads instead of cloning — <i>partial · low · M · cpu, memory</i></summary>

**Idea.** Build newPayload requests, convert EL JSON blocks to payloads and payloads to headers by borrowing or consuming the execution payload and its transactions (FnOnce closures, owning iterators) instead of cloning it, and derive versioned hashes from the raw transactions. This avoids copying large payloads per EL call.

**Gap in Lighthouse.** newPayload requests borrow the payload from the Arc'd block, then deep-clone it (transactions included) into the JSON type in new_payload_v1/v2/v3/v4/v5/v6 paths. Would need JSON types that serialize from references (or Cow) to avoid the clone.

**Impact.** Avoids copying up to ~1 MB of transactions per newPayload; likely sub-millisecond per block, small on a mainnet node.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engine_api/json_structures.rs:317-335`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/json_structures.rs#L317-L335) payload to JSON by value (consuming)
- [`beacon_node/execution_layer/src/engine_api/http.rs:845`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L845) new_payload_v3_deneb does execution_payload.clone().try_into()
- [`beacon_node/execution_layer/src/engine_api/new_payload_request.rs:90`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/new_payload_request.rs#L90) into_execution_payload clone_from_ref

**Sources.** [lighthouse#3983](https://github.com/sigp/lighthouse/pull/3983), [lighthouse#4832](https://github.com/sigp/lighthouse/pull/4832), [lighthouse@902f64a94](https://github.com/sigp/lighthouse/commit/902f64a94692), [lighthouse#3976](https://github.com/sigp/lighthouse/pull/3976)

</details>


<a id="el_interaction-028"></a>
<details>
<summary><b>el_interaction-028</b> Run without eth1 deposit follower when unneeded — <i>n/a · low · S · bandwidth, disk, memory, startup</i></summary>

**Idea.** Do not run the deposit/eth1 follower when no validators are attached or the node starts on an established network, or prune its cached chain. This avoids eth1 log fetches, storage and unbounded memory growth the node does not need.

**Impact.** None; the eth1 follower no longer exists in Lighthouse (deposit follower removed).

**Evidence (Lighthouse @ 928b61e719).**

- beacon_node/ has no eth1 crate; deposit logs come in-payload via EIP-6110 deposit requests (execution_layer/src/engine_api/json_structures.rs)

**Sources.** [nimbus@200902ccb](https://github.com/status-im/nimbus-eth2/commit/200902ccb307), [teku#8178](https://github.com/Consensys-Incorporated/teku/pull/8178), [nimbus@98761afc6](https://github.com/status-im/nimbus-eth2/commit/98761afc645b), [teku#1672](https://github.com/Consensys-Incorporated/teku/pull/1672)

</details>


<a id="el_interaction-029"></a>
<details>
<summary><b>el_interaction-029</b> Keep at most one forkchoiceUpdated in flight — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Await each forkchoiceUpdated call to the EL instead of spawning it detached, so at most one fcU is in flight. This cuts EL load and makes head updates ordered.

**Impact.** At most one fcU in flight and ordered; queued callers wait on the lock.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:7225`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7225) execution_engine_forkchoice_lock held across head read and notify_forkchoice_updated, dropped at :7258
- [`beacon_node/beacon_chain/src/canonical_head.rs:1296`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1296) spawn_execution_layer_updates tasks all go through that lock

**Skeptic check.** The global async lock gives exactly one in-flight fcU and ordered heads, the same effect as awaiting; earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#4609](https://github.com/status-im/nimbus-eth2/pull/4609)

</details>


<a id="el_interaction-030"></a>
<details>
<summary><b>el_interaction-030</b> Deduplicate identical forkchoiceUpdated calls — <i>partial · low · S · latency, cpu, bandwidth</i></summary>

**Idea.** Remember the last forkchoiceUpdated arguments (head, safe, finalized hashes; ignore fields implied by the head) and do not re-send an identical fcU, apart from at most one repeat per slot to survive EL restarts. This removes redundant EL calls.

**Gap in Lighthouse.** No last-sent-args check: when a local validator proposes next slot and the head does not change, prepare_beacon_proposer (from proposer_prep_service and from state_advance_timer, plus the after-head call in canonical_head.rs:1931) sends identical fcU+payload attributes two or more times per proposal, the exact duplicate pattern nimbus#5635 removed. Engine::notify_forkchoice_updated or update_execution_engine_forkchoice could skip when (forkchoice_state, payload attribute key) equals the last sent and a payload_id is cached.

**Impact.** Saves 1-2 redundant fcU per local proposal; EL usually returns the same payload id, so small.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:1086`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1086) head-change path exits early with no fcU when view/params are unchanged
- [`beacon_node/execution_layer/src/engines.rs:197`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engines.rs#L197) latest fcU state resent on EL reconnect
- [`beacon_node/beacon_chain/src/proposer_prep_service.rs:37`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/proposer_prep_service.rs#L37) fires prepare_beacon_proposer 4s before next slot
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:217`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L217) fires prepare_beacon_proposer again ~0.5s before next slot
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7126`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7126) each call within lookahead sends fcU unconditionally
- [`beacon_node/execution_layer/src/engines.rs:160`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engines.rs#L160) notify_forkchoice_updated has no last-sent comparison

**Skeptic check.** Earlier evidence was right for the plain head path and EL restarts, but its own gap shows the proposal path repeats identical fcU; verified two timers both send within the 4s lookahead.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [prysm#12091](https://github.com/OffchainLabs/prysm/pull/12091), [nimbus#5635](https://github.com/status-im/nimbus-eth2/pull/5635), [nimbus#8799](https://github.com/status-im/nimbus-eth2/pull/8799), [lodestar#3298](https://github.com/ChainSafe/lodestar/pull/3298)

</details>


<a id="el_interaction-031"></a>
<details>
<summary><b>el_interaction-031</b> Batch JSON-RPC requests for eth1 block headers — <i>n/a · low · S · latency, bandwidth, sync</i></summary>

**Idea.** Fetch many eth1 block headers in one JSON-RPC batch request instead of one request per block, and keep them in memory. One round trip replaces many.

**Impact.** None; the eth1 follower no longer exists in Lighthouse (header batching).

**Best measured result.** orders of magnitude faster block header queries (commit:lodestar@dea3f4d73c83)

**Evidence (Lighthouse @ 928b61e719).**

- beacon_node/ has no eth1 crate; deposit logs come in-payload via EIP-6110 deposit requests (execution_layer/src/engine_api/json_structures.rs)

**Sources.** [prysm#4392](https://github.com/OffchainLabs/prysm/pull/4392), [lodestar#1519](https://github.com/ChainSafe/lodestar/pull/1519), [lodestar@dea3f4d73](https://github.com/ChainSafe/lodestar/commit/dea3f4d73c83)

</details>


<a id="el_interaction-032"></a>
<details>
<summary><b>el_interaction-032</b> Switch to batched historical fetch when far behind — <i>n/a · low · S · sync, latency</i></summary>

**Idea.** When the eth1 follower is far behind the head, switch to the batched historical sync routine instead of issuing many single-block requests.

**Impact.** None; the eth1 follower no longer exists in Lighthouse (historical fetch).

**Evidence (Lighthouse @ 928b61e719).**

- beacon_node/ has no eth1 crate; deposit logs come in-payload via EIP-6110 deposit requests (execution_layer/src/engine_api/json_structures.rs)

**Sources.** [prysm#8146](https://github.com/OffchainLabs/prysm/pull/8146)

</details>


<a id="el_interaction-033"></a>
<details>
<summary><b>el_interaction-033</b> Unblind blocks with batched engine_getPayloadBodies — <i>implemented · medium · S · bandwidth, cpu, latency, memory</i></summary>

**Idea.** When serving block ranges or the HTTP API from blinded blocks, fetch execution payloads with engine_getPayloadBodiesByHash/ByRange in batched chunks (for example 32 hashes per call) instead of one request per block or whole-block eth_getBlockByHash. Payload bodies carry less data, avoid JSON block conversion and need fewer EL round trips.

**Impact.** Already done for RPC ranges and API.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_block_streamer.rs:226`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_block_streamer.rs#L226) fetch_payload_bodies chunks of 32 via get_payload_bodies_by_hash
- [`beacon_node/beacon_chain/src/payload_envelope_streamer/mod.rs:208`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_streamer/mod.rs#L208) same batching for Gloas envelopes (v2)
- [`beacon_node/execution_layer/src/lib.rs:1727`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1727) single-block get_payload_for_header prefers payload bodies, falls back to eth_getBlockByHash only without capability

**Skeptic check.** Confirmed batched by-hash bodies in both block and envelope streamers; this is Lighthouse's own PR #4102 lineage.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#11210](https://github.com/OffchainLabs/prysm/pull/11210), [prysm#12997](https://github.com/OffchainLabs/prysm/pull/12997), [lighthouse#4102](https://github.com/sigp/lighthouse/pull/4102), [prysm#12630](https://github.com/OffchainLabs/prysm/pull/12630), [lighthouse@787614f6f](https://github.com/sigp/lighthouse/commit/787614f6f646), [lighthouse#4028](https://github.com/sigp/lighthouse/pull/4028)

</details>


<a id="el_interaction-034"></a>
<details>
<summary><b>el_interaction-034</b> Store blinded blocks and fetch payloads from EL — <i>partial · high · M · disk</i></summary>

**Idea.** Store blocks and payload envelopes blinded, and fetch payload bodies from the EL with engine_getPayloadBodiesByHash on demand, so execution payloads are not duplicated in the CL database.

**Gap in Lighthouse.** Blocks and Gloas envelopes are stored blinded and finalized payloads are pruned and refetched from the EL on demand, but unfinalized (hot) payloads/payload bodies are still written to the CL DB in block_as_kv_store_ops and payload_envelope_as_kv_store_ops. Fully skipping that write would need every hot read path (make_full_block, block cache misses, reorg/RPC serving) to go via the EL.

**Impact.** Saves per-block payload writes and hot-DB size for the unfinalized window only; finalized payloads are already deduplicated.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:527-548`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L527-L548) block_as_kv_store_ops splits block into blinded block + ExecPayload column
- [`beacon_node/store/src/hot_cold_store.rs:563-623`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L563-L623) try_get_full_block returns Blinded for pruned finalized blocks
- [`beacon_node/store/src/hot_cold_store.rs:1019-1037`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1019-L1037) Gloas envelopes stored as summary + PayloadBody column (blinded envelope)
- [`beacon_node/store/src/hot_cold_store.rs:3119`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3119) try_prune_execution_payloads
- [`beacon_node/store/src/config.rs:117`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L117) prune_payloads: true
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1290-1330`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1290-L1330) get_payload_for_header reconstructs payload from EL with integrity check
- [`beacon_node/beacon_chain/src/beacon_block_streamer.rs:234`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_block_streamer.rs#L234) get_payload_bodies_by_hash for RPC serving

**Second check.** Also checked the Gloas envelope storage path (summary + PayloadBody column, pruned like payloads) and the beacon_chain EL reconstruction path; both confirm the blinded-plus-prune design but hot payloads are still persisted.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [grandine@b7a0fcc26](https://github.com/grandinetech/grandine/commit/b7a0fcc26c3b), [teku#6040](https://github.com/Consensys-Incorporated/teku/pull/6040), [prysm#10998](https://github.com/OffchainLabs/prysm/pull/10998)

</details>


<a id="el_interaction-035"></a>
<details>
<summary><b>el_interaction-035</b> Fetch deposit logs per block range, not per block — <i>n/a · low · S · bandwidth, latency, sync</i></summary>

**Idea.** Fetch deposit contract logs, including historical catch-up, for whole block ranges in batched periodic eth_getLogs calls (instead of a long-lived subscription or per-block queries) and process only blocks that contain deposit events.

**Impact.** None; the eth1 follower no longer exists in Lighthouse (deposit log fetching).

**Best measured result.** genesis detected in ~7s with 4 deposits (pr:lodestar#906)

**Evidence (Lighthouse @ 928b61e719).**

- beacon_node/ has no eth1 crate; deposit logs come in-payload via EIP-6110 deposit requests (execution_layer/src/engine_api/json_structures.rs)

**Sources.** [prysm#1605](https://github.com/OffchainLabs/prysm/pull/1605), [lodestar#969](https://github.com/ChainSafe/lodestar/pull/969), [lodestar#906](https://github.com/ChainSafe/lodestar/pull/906), [prysm#4015](https://github.com/OffchainLabs/prysm/pull/4015), [teku#1132](https://github.com/Consensys-Incorporated/teku/pull/1132)

</details>


<a id="el_interaction-036"></a>
<details>
<summary><b>el_interaction-036</b> Batch database writes for deposit processing — <i>n/a · low · S · cpu, disk</i></summary>

**Idea.** Process deposit logs in bulk per fetched range and write deposit data roots to the database in batches instead of one at a time.

**Impact.** None; the eth1 follower no longer exists in Lighthouse (deposit DB writes).

**Evidence (Lighthouse @ 928b61e719).**

- beacon_node/ has no eth1 crate; deposit logs come in-payload via EIP-6110 deposit requests (execution_layer/src/engine_api/json_structures.rs)

**Sources.** [lodestar@5ed2d7e83](https://github.com/ChainSafe/lodestar/commit/5ed2d7e8359c)

</details>


<a id="el_interaction-037"></a>
<details>
<summary><b>el_interaction-037</b> Binary search deposit count per eth1 block — <i>n/a · low · S · cpu, memory</i></summary>

**Idea.** Find the deposit count for an eth1 block by binary search over a sorted array of deposits by block number, instead of filling a map entry for every block number in the range.

**Impact.** Lighthouse removed its eth1 deposit cache and follows deposits via the execution requests (EIP-6110); no deposit-count-by-block lookup exists.

**Evidence (Lighthouse @ 928b61e719).**

- beacon_node/ (no eth1 dir)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5931) eth1_data copied from state

**Sources.** [lodestar@dd6082fbc](https://github.com/ChainSafe/lodestar/commit/dd6082fbca20)

</details>


<a id="el_interaction-038"></a>
<details>
<summary><b>el_interaction-038</b> Bound terminal PoW block search by difficulty — <i>n/a · low · S · bandwidth, latency</i></summary>

**Idea.** When searching for the terminal PoW block, stop walking back once total difficulty drops below the terminal threshold instead of walking to genesis.

**Impact.** Terminal PoW block search was removed post-merge; no walk-back loop exists.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engine_api.rs:155`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api.rs#L155) only a TTD-reached check on a block; no backwards terminal search

**Sources.** [lighthouse#2835](https://github.com/sigp/lighthouse/pull/2835)

</details>


<a id="el_interaction-039"></a>
<details>
<summary><b>el_interaction-039</b> Limit and dedupe getBlobs calls per block root — <i>partial · medium · S · bandwidth, cpu, latency, memory</i></summary>

**Idea.** Track engine_getBlobs requests per block root (allowing several blocks per slot): call it once, triggered by the first block or column gossip, share one in-flight request between block-arrival and column-arrival paths, and bound retries (max attempts, minimum interval, capped map). Repeated large getBlobs responses waste CPU and slow sidecar validation; the first request can be sent before newPayload so ELs that drop blobs after validation still answer.

**Gap in Lighthouse.** Header-after-block is deduped through the assembler cache and there are no retries, so the count is bounded at about 2-3 per root. Still missing: an in-flight per-root registry, so block-after-header and RPC-after-gossip do not issue a second getBlobs while the first is pending or after it succeeded.

**Impact.** Saves one extra getBlobs (up to ~0.8MB V2 response plus cell work) when the partial header arrives before the block, or when lookup re-imports. Far smaller than the 14x Lodestar case.

**Best measured result.** about 14 requests per blob block on a non-supernode, all with the same answer (pr:lodestar#10329)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1936`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1936) gossip block spawns getBlobs unconditionally (spawn_fetch_block_columns)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3993`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3993) put_pre_execution_block during block processing
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:458`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L458) put_pre_execution_block inits the partial-column assembler with the block's header
- [`beacon_node/beacon_chain/src/data_column_verification.rs:664`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L664) partial header marked previously_cached if assembler already has it
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1121`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1121) header path only triggers getBlobs when !was_cached, so header-after-block does not re-fetch
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:217`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L217) RPC block with MissingComponents triggers another fetch
- [`beacon_node/network/src/network_beacon_processor/mod.rs:998`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L998) fetch_engine_blobs_and_publish_full has no in-flight or per-root check
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:272`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L272) only post-response dedupe (block already in fork choice)

**Second check.** Traced the assembler cache shared by block insert and header verification: header-after-block is already deduped, and there are no retry loops. The block-after-header and RPC paths still have no in-flight registry.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [lodestar#10329](https://github.com/ChainSafe/lodestar/pull/10329), [nimbus#8884](https://github.com/status-im/nimbus-eth2/pull/8884), [nimbus#8982](https://github.com/status-im/nimbus-eth2/pull/8982), [lodestar#8381](https://github.com/ChainSafe/lodestar/pull/8381), [lodestar#8399](https://github.com/ChainSafe/lodestar/pull/8399), [lodestar#8282](https://github.com/ChainSafe/lodestar/pull/8282)

</details>


<a id="el_interaction-040"></a>
<details>
<summary><b>el_interaction-040</b> Cache eth1 blocks for eth1 data voting — <i>n/a · low · S · bandwidth, latency, memory</i></summary>

**Idea.** Keep a bounded in-memory cache of eth1 block headers (hash, number, timestamp), prefetched for the voting window at startup and filled while following the head and fetching deposit logs. Eth1 data voting and proposal lookups then read the cache instead of issuing execution-node RPCs per header.

**Impact.** Eth1 voting and its block cache no longer exist in Lighthouse; proposals copy state.eth1_data().

**Best measured result.** Zinken cache misses 280 -&gt; 3 (pr:prysm#7541)

**Evidence (Lighthouse @ 928b61e719).**

- beacon_node/ (no eth1 dir)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5931) eth1_data from state

**Sources.** [prysm#1769](https://github.com/OffchainLabs/prysm/pull/1769), [prysm#5347](https://github.com/OffchainLabs/prysm/pull/5347), [prysm#7861](https://github.com/OffchainLabs/prysm/pull/7861), [lodestar#759](https://github.com/ChainSafe/lodestar/pull/759), [prysm#1760](https://github.com/OffchainLabs/prysm/pull/1760), [lodestar#1520](https://github.com/ChainSafe/lodestar/pull/1520), [prysm#4924](https://github.com/OffchainLabs/prysm/pull/4924), [prysm#7541](https://github.com/OffchainLabs/prysm/pull/7541), [prysm#8110](https://github.com/OffchainLabs/prysm/pull/8110), [lodestar#1518](https://github.com/ChainSafe/lodestar/pull/1518)

</details>


<a id="el_interaction-041"></a>
<details>
<summary><b>el_interaction-041</b> Fetch each distinct eth1 vote block once — <i>n/a · low · S · latency, bandwidth</i></summary>

**Idea.** When tallying eth1 data votes for block production, fetch each distinct vote's block once instead of repeated fetches and existence checks per vote, keeping work linear in votes.

**Impact.** No eth1 vote tallying or per-vote block fetching remains.

**Evidence (Lighthouse @ 928b61e719).**

- beacon_node/ (no eth1 dir)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5931)

**Sources.** [prysm#1757](https://github.com/OffchainLabs/prysm/pull/1757)

</details>


<a id="el_interaction-042"></a>
<details>
<summary><b>el_interaction-042</b> Cache engine API JWT until near expiry — <i>not · low · S · cpu</i></summary>

**Idea.** Cache the generated JWT for engine API calls and reuse it until near expiry instead of signing a new token per request.

**Gap in Lighthouse.** Cache the encoded JWT in Auth and regenerate only when iat is older than about 30s (Engine API allows 60s skew); change Auth::generate_token.

**Impact.** Saves a few microseconds of HMAC signing per engine call; negligible.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engine_api/auth.rs:110-120`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/auth.rs#L110-L120) generate_token signs a new JWT each call
- [`beacon_node/execution_layer/src/engine_api/http.rs:683`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L683) calls auth.generate_token() per request

**Sources.** [teku#4980](https://github.com/Consensys-Incorporated/teku/pull/4980)

</details>


<a id="el_interaction-043"></a>
<details>
<summary><b>el_interaction-043</b> Avoid slow serializer lookup on JWT creation — <i>n/a · low · S · cpu, latency</i></summary>

**Idea.** Configure the JWT builder with an explicit JSON serializer so each token creation skips the library's slow service lookup.

**Impact.** Java JWT library serializer service lookup; the Rust jsonwebtoken crate has no such lookup.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engine_api/auth.rs:116`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/auth.rs#L116) uses Rust jsonwebtoken encode with static key

**Sources.** [teku#7580](https://github.com/Consensys-Incorporated/teku/pull/7580)

</details>


<a id="el_interaction-044"></a>
<details>
<summary><b>el_interaction-044</b> Cache justified/finalized payload hashes for fcU — <i>implemented · low · S · disk, latency</i></summary>

**Idea.** Keep the execution block hashes of the justified and finalized checkpoints in memory so each forkchoiceUpdated avoids database lookups for them.

**Impact.** No DB lookups on fcU.

**Best measured result.** saves 2 DB lookups per head update, ~100ms on the author's machine (pr:prysm#10657)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fork_choice/src/fork_choice.rs:493`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L493) get_forkchoice_update_parameters returns in-memory cached field set at :612
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7227`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7227) fcU uses params.justified_hash/finalized_hash with no DB lookups

**Skeptic check.** Justified and finalized execution hashes are stored in ForkChoice.forkchoice_update_parameters and copied into the cached head; earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#10657](https://github.com/OffchainLabs/prysm/pull/10657)

</details>


<a id="el_interaction-045"></a>
<details>
<summary><b>el_interaction-045</b> Cache deposit signature verification result — <i>n/a · low · S · cpu</i></summary>

**Idea.** Verify each deposit signature once when the deposit log enters the cache and store the result, so genesis or state building does not re-verify it.

**Impact.** Eth1 genesis service and deposit cache were removed; genesis deposit signature re-verification does not occur at runtime.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/genesis/src/common.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/genesis/src/common.rs) and interop.rs: no deposit cache or eth1 genesis service
- [`beacon_node/beacon_chain/src/beacon_chain.rs:547`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L547) pre-verifies pending deposit signatures ahead of Gloas

**Sources.** [lighthouse#1298](https://github.com/sigp/lighthouse/pull/1298)

</details>


<a id="el_interaction-046"></a>
<details>
<summary><b>el_interaction-046</b> Parse deposit contract ABI once — <i>n/a · low · S · cpu, memory</i></summary>

**Idea.** Parse the deposit contract ABI once and reuse it when decoding deposit logs instead of re-parsing per log.

**Impact.** Lighthouse no longer decodes deposit contract logs, so there is no ABI to parse.

**Evidence (Lighthouse @ 928b61e719).**

- beacon_node/ (no eth1 dir, no deposit log decoding)

**Sources.** [prysm#16061](https://github.com/OffchainLabs/prysm/pull/16061)

</details>


<a id="el_interaction-047"></a>
<details>
<summary><b>el_interaction-047</b> Cache chainId/net_version and poll EL less — <i>n/a · low · bandwidth, cpu</i></summary>

**Idea.** Cache eth_chainId and net_version per endpoint, invalidating only on endpoint failure, and poll endpoint health less often. This cuts routine RPC traffic to the EL.

**Impact.** Lighthouse has no eth1 module and no periodic eth_chainId/net_version polling, so there is no routine traffic to cut.

**Best measured result.** ~2000 to 360 requests per hour, 82% reduction (pr:lighthouse#2340)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engine_api/http.rs:375`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L375) get_chain_id defined, no caller outside http.rs
- [`beacon_node/execution_layer/src/engines.rs:240`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engines.rs#L240) upcheck uses engine API only

**Sources.** [lighthouse#2340](https://github.com/sigp/lighthouse/pull/2340), [lighthouse#3324](https://github.com/sigp/lighthouse/pull/3324)

</details>


<a id="el_interaction-048"></a>
<details>
<summary><b>el_interaction-048</b> Decode persisted eth1 data once at startup — <i>n/a · low · memory, startup</i></summary>

**Idea.** Read and decode the persisted eth1 chain/deposit data once at startup and reuse it, instead of decoding the (up to ~100 MB) blob twice.

**Impact.** Lighthouse no longer persists eth1/deposit data; nothing to decode at startup.

**Evidence (Lighthouse @ 928b61e719).**

- beacon_node/ (no eth1 crate; ls shows beacon_chain, execution_layer, store...)

**Sources.** [prysm#12826](https://github.com/OffchainLabs/prysm/pull/12826)

</details>


<a id="el_interaction-049"></a>
<details>
<summary><b>el_interaction-049</b> Dedupe newPayload for duplicate payload envelopes — <i>partial · low · S · cpu, latency</i></summary>

**Idea.** Store payload envelopes under the same lock as blocks and check already-stored inside it, so duplicate envelopes do not cause duplicate newPayload calls.

**Gap in Lighthouse.** Gossip duplicates are dropped atomically by ObservedPayloadEnvelopes, but envelopes from RPC/HTTP sources still pass through to newPayload even if already seen; add an already-imported check at the start of the import function in import.rs.

**Impact.** Avoids a redundant newPayload call only when the same envelope arrives via RPC/HTTP after gossip; rare, small saving.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/payload_envelope_verification/gossip_verified_envelope.rs:298`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/gossip_verified_envelope.rs#L298) observe_envelope atomic check
- gossip_verified_envelope.rs:302 duplicate rejected only when source==Gossip
- [`beacon_node/beacon_chain/src/payload_envelope_verification/import.rs:60`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/import.rs#L60) import path has no already-stored check before notify_new_payload

**Sources.** [nimbus#9126](https://github.com/status-im/nimbus-eth2/pull/9126)

</details>


<a id="el_interaction-050"></a>
<details>
<summary><b>el_interaction-050</b> Defer getBlobs call off the gossip path — <i>partial · low · S · latency</i></summary>

**Idea.** Schedule the heavy getBlobs call for a later event-loop tick / separate task so it does not block gossip processing.

**Gap in Lighthouse.** Only the gossip-block trigger is detached. process_gossip_partial_data_column_sidecar (first uncached partial header) awaits fetch_engine_blobs_and_publish_full inline. This holds a beacon-processor worker slot for the engine_getBlobs round trip and column computation. The RPC block path (process_rpc_block, MissingComponents) also awaits inline and delays SyncMessage::BlockComponentProcessed. Both should use spawn_fetch_block_columns or an equivalent detached spawn.

**Impact.** Frees one worker slot for tens to hundreds of ms per block when the partial header beats the block, and gives faster sync lookup completion. The gain is small because it fires once per block (was_cached guard).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1934-1940`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1934-L1940) gossip block path calls spawn_fetch_block_columns (detached executor.spawn)
- [`beacon_node/network/src/network_beacon_processor/mod.rs:960-995`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L960-L995) spawn_fetch_block_columns
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1120-1134`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1120-L1134) partial-header gossip path awaits fetch_engine_blobs_and_publish_full and publish_partial_data_columns inline
- [`beacon_node/beacon_processor/src/lib.rs:1627-1640`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1627-L1640),1709-1713 GossipPartialDataColumnSidecar runs as async work holding a worker slot (SendOnDrop) until the future completes
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:213-223`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L213-L223) RPC block path also awaits getBlobs inline before notifying sync

**Skeptic check.** The block gossip path is correctly detached. The earlier evidence found the inline await on the partial-column gossip path but called it minor because there is no event loop. In LH it still occupies a beacon-processor worker, so on that gossip path the idea is not applied.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lodestar#8384](https://github.com/ChainSafe/lodestar/pull/8384)

</details>


<a id="el_interaction-051"></a>
<details>
<summary><b>el_interaction-051</b> Derive eth1 data from deposit logs — <i>n/a · low · sync, startup, bandwidth</i></summary>

**Idea.** Compute deposit root and count for any eth1 block from the cached deposit logs and an incremental deposit merkle tree, instead of calling the deposit contract state per block. This avoids old-state queries on the EL.

**Impact.** Lighthouse removed eth1 deposit voting machinery; no per-block deposit contract queries remain.

**Evidence (Lighthouse @ 928b61e719).**

- beacon_node/ has no eth1 service; deposits come via EL requests (EIP-6110)

**Sources.** [lighthouse#709](https://github.com/sigp/lighthouse/pull/709), [teku#1902](https://github.com/Consensys-Incorporated/teku/pull/1902), [lodestar#1521](https://github.com/ChainSafe/lodestar/pull/1521)

</details>


<a id="el_interaction-052"></a>
<details>
<summary><b>el_interaction-052</b> Persist deposit tree and restore it on restart — <i>n/a · low · startup, sync</i></summary>

**Idea.** Persist the deposit cache/tree (or a snapshot at the last finalized deposit) and on startup restore from it, replaying only later deposit events, instead of reprocessing all eth1 deposit logs from genesis.

**Impact.** No deposit tree is rebuilt from logs on restart in current Lighthouse.

**Best measured result.** ~150ms from snapshot load to latest deposit event added on kiln (pr:teku#5954)

**Evidence (Lighthouse @ 928b61e719).**

- beacon_node/ has no deposit cache or eth1 log sync

**Sources.** [teku#5901](https://github.com/Consensys-Incorporated/teku/pull/5901), [teku#5954](https://github.com/Consensys-Incorporated/teku/pull/5954), [prysm#4581](https://github.com/OffchainLabs/prysm/pull/4581), [teku#6190](https://github.com/Consensys-Incorporated/teku/pull/6190)

</details>


<a id="el_interaction-053"></a>
<details>
<summary><b>el_interaction-053</b> Slot-based deadline for early-block newPayload — <i>n/a · medium · S · latency</i></summary>

**Idea.** For early-arriving blocks, derive the engine API request deadline from the block's slot (clamped to wall slot range) instead of the wall slot, so newPayload is not cancelled and left optimistic.

**Impact.** No slot-derived deadline exists, so early blocks are not cancelled by wall-slot clamping.

**Best measured result.** Optimistic REST samples 26/180 before, 0/768 after; longest optimistic run 22s -&gt; 0s (one node) (pr:nimbus#9329)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engine_api/http.rs:677`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L677) timeout is a relative reqwest Duration (ENGINE_NEW_PAYLOAD_TIMEOUT 8s, line 44), not a deadline from the wall slot

**Sources.** [nimbus#9329](https://github.com/status-im/nimbus-eth2/pull/9329)

</details>


<a id="el_interaction-054"></a>
<details>
<summary><b>el_interaction-054</b> Per-method engine API timeouts — <i>implemented · medium · S · latency</i></summary>

**Idea.** Set per-method timeouts on engine API calls (short for getPayload, longer for newPayload and forkchoiceUpdated) so a slow EL cannot stall block import or production.

**Impact.** Already done.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engine_api/http.rs:44`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L44) NEW_PAYLOAD 8s
- [`beacon_node/execution_layer/src/engine_api/http.rs:52`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L52) GET_PAYLOAD 2s
- [`beacon_node/execution_layer/src/engine_api/http.rs:59`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L59) FORKCHOICE_UPDATED 8s
- [`beacon_node/execution_layer/src/engine_api/http.rs:63`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L63) payload bodies 10s, :74 GET_BLOBS 1s

**Skeptic check.** Each engine method has its own timeout constant used by its call; earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine@5ce858023](https://github.com/grandinetech/grandine/commit/5ce858023642)

</details>


<a id="el_interaction-055"></a>
<details>
<summary><b>el_interaction-055</b> Encode engine payload once for multiple ELs — <i>n/a · low · cpu, latency</i></summary>

**Idea.** Serialize the engine API request once and reuse the bytes for retries and multiple EL endpoints instead of re-encoding per request.

**Impact.** Lighthouse supports one EL endpoint and the engine call does not re-encode across multiple ELs; the idea does not apply.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/lib.rs:496`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L496) single execution_endpoint: Option&lt;SensitiveUrl&gt;
- [`beacon_node/execution_layer/src/engine_api/http.rs:667-679`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L667-L679) rpc_request builds body and .json(&amp;body) per call

**Sources.** [nimbus#7439](https://github.com/status-im/nimbus-eth2/pull/7439)

</details>


<a id="el_interaction-056"></a>
<details>
<summary><b>el_interaction-056</b> Engine API over IPC socket — <i>not · low · M · latency, cpu</i></summary>

**Idea.** Support a Unix domain socket IPC transport to a co-located execution client, avoiding HTTP framing and TCP overhead.

**Gap in Lighthouse.** Add a Unix-socket transport (hyper over UnixStream or similar) to HttpJsonRpc and a CLI flag accepting a socket path; JWT auth would still be needed or skipped.

**Impact.** Saves a little HTTP/TCP loopback overhead per engine call, sub-millisecond; mostly irrelevant against EL execution time.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engine_api/http.rs:674`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L674) reqwest HTTP client only
- [`beacon_node/execution_layer/src/engine_api/auth.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/auth.rs) and lib.rs: no ipc/unix socket transport

**Sources.** [teku#10510](https://github.com/Consensys-Incorporated/teku/pull/10510)

</details>


<a id="el_interaction-057"></a>
<details>
<summary><b>el_interaction-057</b> Estimate eth1 block from timestamps — <i>n/a · low · S · cpu, latency</i></summary>

**Idea.** Estimate the eth1 block number for a target timestamp (follow distance, voting period) from average block time and refine iteratively, instead of scanning or bisecting with many RPC calls.

**Impact.** None: the feature does not exist in current Lighthouse, so nothing gets cheaper. Lighthouse no longer has an eth1 block/follow-distance voting module; block production copies state.eth1_data, so there is no eth1 block number to estimate.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5931) - block production just clones state.eth1_data(), no eth1 voting
- [`beacon_node/execution_layer/src/lib.rs:1-5`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1-L5) - execution_layer has no deposit-contract functionality; beacon_node/eth1 crate no longer exists

**Sources.** [prysm#2486](https://github.com/OffchainLabs/prysm/pull/2486), [prysm#7386](https://github.com/OffchainLabs/prysm/pull/7386)

</details>


<a id="el_interaction-058"></a>
<details>
<summary><b>el_interaction-058</b> Startup shortcuts in eth1 deposit monitor — <i>n/a · low · S · sync, startup</i></summary>

**Idea.** Add shortcuts in the eth1 deposit monitor so deposit logs catch up faster at startup.

**Impact.** None: the feature does not exist in current Lighthouse, so nothing gets cheaper. Lighthouse has no eth1 deposit-log monitor (beacon_node/eth1 removed; deposits come via EL requests in blocks post-Electra).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5931) - block production just clones state.eth1_data(), no eth1 voting
- [`beacon_node/execution_layer/src/lib.rs:1-5`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1-L5) - execution_layer has no deposit-contract functionality; beacon_node/eth1 crate no longer exists

**Sources.** [nimbus#1229](https://github.com/status-im/nimbus-eth2/pull/1229)

</details>


<a id="el_interaction-059"></a>
<details>
<summary><b>el_interaction-059</b> Fast path for appending successor eth1 block — <i>n/a · low · S · sync, startup</i></summary>

**Idea.** When a new eth1 block extends the cached chain with a consistent deposit count, append it directly and skip the parent-lookup repair path.

**Impact.** None: the feature does not exist in current Lighthouse, so nothing gets cheaper. Lighthouse has no cached eth1 block chain to append to.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5931) - block production just clones state.eth1_data(), no eth1 voting
- [`beacon_node/execution_layer/src/lib.rs:1-5`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1-L5) - execution_layer has no deposit-contract functionality; beacon_node/eth1 crate no longer exists

**Sources.** [nimbus@f20f07782](https://github.com/status-im/nimbus-eth2/commit/f20f07782755)

</details>


<a id="el_interaction-060"></a>
<details>
<summary><b>el_interaction-060</b> Incremental deposit tree with larger log batches — <i>n/a · low · S · sync, startup</i></summary>

**Idea.** Fetch deposits in larger incremental batches and maintain the deposit merkle tree incrementally, reducing eth1 RPC requests during eth1 sync.

**Impact.** None: the feature does not exist in current Lighthouse, so nothing gets cheaper. Lighthouse has no eth1 deposit-log syncing; the incremental deposit tree only remains in state_processing for snapshots/genesis.

**Best measured result.** Significantly faster ETH1 syncing (commit:nimbus@2f29e3e7f39c)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5931) - block production just clones state.eth1_data(), no eth1 voting
- [`beacon_node/execution_layer/src/lib.rs:1-5`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1-L5) - execution_layer has no deposit-contract functionality; beacon_node/eth1 crate no longer exists

**Sources.** [nimbus@2f29e3e7f](https://github.com/status-im/nimbus-eth2/commit/2f29e3e7f39c)

</details>


<a id="el_interaction-061"></a>
<details>
<summary><b>el_interaction-061</b> Fetch timestamps only for needed deposit blocks — <i>n/a · low · S · latency, sync</i></summary>

**Idea.** During deposit-log sync, fetch block timestamps only for blocks inside the range actually needed, avoiding one RPC per deposit block outside it.

**Impact.** None: the feature does not exist in current Lighthouse, so nothing gets cheaper. Lighthouse has no deposit-log sync that fetches block timestamps over RPC.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5931) - block production just clones state.eth1_data(), no eth1 voting
- [`beacon_node/execution_layer/src/lib.rs:1-5`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1-L5) - execution_layer has no deposit-contract functionality; beacon_node/eth1 crate no longer exists

**Sources.** [nimbus@2ee15a38e](https://github.com/status-im/nimbus-eth2/commit/2ee15a38ed8a)

</details>


<a id="el_interaction-062"></a>
<details>
<summary><b>el_interaction-062</b> Websocket library without send throttling — <i>n/a · low · S · latency, bandwidth</i></summary>

**Idea.** Use a websocket client without per-MB send delays and where cancelling a send does not break the socket, so large EL requests and reconnects are fast.

**Impact.** None: the feature does not exist in current Lighthouse, so nothing gets cheaper. Lighthouse does not use a Nim websocket library; EL is accessed through HTTP JSON-RPC with JWT.

**Best measured result.** "1 second delay between each MB of sent data" in the old library (pr:nimbus#4061)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5931) - block production just clones state.eth1_data(), no eth1 voting
- [`beacon_node/execution_layer/src/lib.rs:1-5`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1-L5) - execution_layer has no deposit-contract functionality; beacon_node/eth1 crate no longer exists

**Sources.** [nimbus#4061](https://github.com/status-im/nimbus-eth2/pull/4061)

</details>


<a id="el_interaction-063"></a>
<details>
<summary><b>el_interaction-063</b> Send fcU after SYNCING newPayload — <i>partial · medium · S · sync</i></summary>

**Idea.** When the EL answers newPayload with SYNCING, send forkchoiceUpdated so the EL starts fetching the missing data.

**Gap in Lighthouse.** Nothing reacts to the SYNCING newPayload result itself. fcU follows only when the block changes the head, when the watchdog sees the engine come back from offline, or for proposer prep. A SYNCING non-head block, or a head that does not change, gets no fcU.

**Impact.** Low. In the common sync case the SYNCING block becomes head and fcU follows straight away. The gap is only side branches and stalled heads.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/execution_payload.rs:151`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/execution_payload.rs#L151) Syncing/Accepted maps to Optimistic, no fcU issued
- [`beacon_node/beacon_chain/src/canonical_head.rs:1088`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1088) recompute_head returns early (no fcU) when the head view is unchanged
- [`beacon_node/beacon_chain/src/canonical_head.rs:1296`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1296) fcU via spawn_execution_layer_updates when the head changes (covers the optimistic block that becomes head, e.g. during sync)
- [`beacon_node/execution_layer/src/engines.rs:247`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engines.rs#L247) watchdog upcheck re-sends latest forkchoice state when the engine comes back to Synced
- [`beacon_node/execution_layer/src/lib.rs:717`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L717) watchdog runs once per slot
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7135`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7135) proposer-prep fcU on head (only near own proposals or with always_prepare_payload)

**Second check.** Checked other fcU paths beyond head change: the per-slot watchdog upcheck resend, startup fcU and proposer-prep fcU. None is triggered by a SYNCING newPayload, so partial stands.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [nimbus#3618](https://github.com/status-im/nimbus-eth2/pull/3618)

</details>


<a id="el_interaction-064"></a>
<details>
<summary><b>el_interaction-064</b> Send forkchoiceUpdated on slot tick — <i>implemented · low · S · latency</i></summary>

**Idea.** Trigger forkchoiceUpdated at slot start and before attesting, not only when a new head is stored, through one shared fork-choice refresh path.

**Impact.** None left: every fork choice run (slot tick, pre-advance, block import, sync, API publish) goes through recompute_head_at_slot_internal and sends fcU whenever anything changed.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:7496`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7496) per_slot_task -&gt; recompute_head_at_current_slot at slot start
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:211`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L211) recompute_head_at_slot(next_slot) late in the slot, then prepare_beacon_proposer
- [`beacon_node/beacon_chain/src/canonical_head.rs:1088-1096`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1088-L1096) early exit only when view, payload status and fcU params are all unchanged
- [`beacon_node/beacon_chain/src/canonical_head.rs:1296`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1296) spawn_execution_layer_updates sends fcU from the single shared recompute path

**Skeptic check.** Verified the shared recompute path is used by the slot timer, the state advance timer and every import path, and that it sends fcU on any change. Earlier evidence was right; skipping fcU when nothing changed is correct, because the EL already has that head.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#4009](https://github.com/status-im/nimbus-eth2/pull/4009)

</details>


<a id="el_interaction-065"></a>
<details>
<summary><b>el_interaction-065</b> Finalize deposit tree before receiving blocks — <i>n/a · low · S · latency, startup</i></summary>

**Idea.** Finalize accumulated deposits in the deposit tree at startup before the node starts processing blocks, so the lock is not held during the first blocks.

**Impact.** None: the feature does not exist in current Lighthouse, so nothing gets cheaper. Lighthouse has no deposit-tree finalize lock held during block import; the eth1 service was removed.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5931) - block production just clones state.eth1_data(), no eth1 voting
- [`beacon_node/execution_layer/src/lib.rs:1-5`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1-L5) - execution_layer has no deposit-contract functionality; beacon_node/eth1 crate no longer exists

**Sources.** [prysm#9639](https://github.com/OffchainLabs/prysm/pull/9639)

</details>


<a id="el_interaction-066"></a>
<details>
<summary><b>el_interaction-066</b> Verify block hash locally, skip newPayload on finalized sync — <i>partial · medium · S · cpu, latency, sync</i></summary>

**Idea.** During sync of finalized blocks, verify the execution block hash locally (RLP header, including new fork header fields, plus transactions and withdrawals trie roots) and skip the newPayload call, falling back to the EL only on failure. Local hashing costs about 500us per block, far below an EL round trip.

**Gap in Lighthouse.** Post-Gloas the payload is in the envelope, and BeaconChain::process_range_sync_envelope always builds PayloadNotifier with NotifyExecutionLayer::Yes. So finalized range sync of Gloas chains still calls newPayload for every envelope, even though PayloadNotifier already supports the local block-hash skip. Fix: thread notify_execution_layer from process_chain_segment into process_range_sync_envelope.

**Impact.** Pre-Gloas finalized sync already skips the EL round trip. On Gloas chains every finalized envelope in range sync still waits for an EL newPayload.

**Best measured result.** block hash verification about 500us per block on mainnet (pr:lighthouse#3794)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/execution_payload.rs:77-94`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/execution_payload.rs#L77-L94) NotifyExecutionLayer::No + optimistic_finalized_sync -&gt; perform_optimistic_sync_verifications, fallback to EL on failure (pre-Gloas blocks)
- [`beacon_node/execution_layer/src/block_hash.rs:17-66`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/block_hash.rs#L17-L66) calculate_execution_block_hash covers tx/withdrawals roots, blob gas, parent beacon root, requests hash, BAL hash, slot number
- [`beacon_node/beacon_chain/src/payload_envelope_verification/payload_notifier.rs:33`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/payload_notifier.rs#L33) envelope notifier supports the same skip
- [`beacon_node/beacon_chain/src/payload_envelope_verification/import.rs:419-451`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/import.rs#L419-L451) process_range_sync_envelope hardcodes NotifyExecutionLayer::Yes
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3273`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3273),3375 process_chain_segment calls process_range_sync_envelope without passing its notify_execution_layer

**Skeptic check.** The pre-Gloas block path and the block-hash code are real and complete, as the earlier evidence said. The earlier check missed that the Gloas range-sync envelope path ignores NotifyExecutionLayer::No.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lighthouse#3920](https://github.com/sigp/lighthouse/pull/3920), [lighthouse#3794](https://github.com/sigp/lighthouse/pull/3794), [lighthouse#3877](https://github.com/sigp/lighthouse/pull/3877)

</details>


<a id="el_interaction-067"></a>
<details>
<summary><b>el_interaction-067</b> Fix busy loop in EL monitor — <i>n/a · low · S · cpu</i></summary>

**Idea.** Fix the EL/eth1 monitor state machine so it sets state before awaiting and bounds the provider-online probe with a timeout, avoiding a CPU busy loop.

**Impact.** None: the feature does not exist in current Lighthouse, so nothing gets cheaper. Lighthouse has no eth1/EL monitor state machine of this kind (Nim async busy loop).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5931) - block production just clones state.eth1_data(), no eth1 voting
- [`beacon_node/execution_layer/src/lib.rs:1-5`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1-L5) - execution_layer has no deposit-contract functionality; beacon_node/eth1 crate no longer exists

**Sources.** [nimbus@c672628be](https://github.com/status-im/nimbus-eth2/commit/c672628be8c9)

</details>


<a id="el_interaction-068"></a>
<details>
<summary><b>el_interaction-068</b> Decode getBlobs response into preallocated buffers — <i>n/a · low · S · memory, cpu</i></summary>

**Idea.** Pass preallocated, reused blob buffers into the getBlobsV2 response decoder so each blob is written into an existing buffer instead of a fresh allocation. This cuts allocation and GC pressure from 128KB blobs.

**Impact.** Rust has no GC; JSON hex decode allocates per blob but a buffer-reuse API is not available via serde. Idea targets Lodestar GC pressure.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engine_api/http.rs:740`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L740) get_blobs_v2 deserializes JSON into Vec&lt;BlobAndProofV2&gt;

**Sources.** [lodestar#10203](https://github.com/ChainSafe/lodestar/pull/10203)

</details>


<a id="el_interaction-069"></a>
<details>
<summary><b>el_interaction-069</b> Fast hex decoding of Engine API responses — <i>partial · medium · M · cpu, memory, latency</i></summary>

**Idea.** Decode large hex fields (blobs, transactions) in Engine API JSON responses directly into byte buffers with a native or lookup-table decoder, without intermediate strings or per-char loops, and avoid reflection-based deserialization. Hex decoding of blobs dominates getBlobs response cost.

**Gap in Lighthouse.** Decoding is already native compiled code with derive-based serde, so the JS-loop and reflection costs in the source PRs do not apply. Still missing: deserializing straight from bytes, skipping serde_json::Value (which holds an extra ~256KB String per blob), and a SIMD decoder (const-hex is already in Cargo.lock) writing into the final buffer.

**Impact.** Small: probably well under 1ms per getBlobsV2 call (one String alloc+copy and a branchy decoder per blob). The 8-17ms Lodestar gain came from replacing a JS loop.

**Best measured result.** fromHexInto 128KB blob ~1.04 ms/op to 120.3 us/op; getBlobsV2 call was 8-17ms slower with JS loop (pr:lodestar#10358)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engine_api/json_structures.rs:1034`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/json_structures.rs#L1034) blob uses compile-time serde derive with ssz_types hex_fixed_vec (no reflection)
- ~/.cargo/git/checkouts/ssz_types-19f835ca387d51e3/8955d22/src/serde_utils/hex_fixed_vec.rs:20 PrefixedHexVisitor -&gt; Vec&lt;u8&gt; moved into FixedVector
- ~/.cargo/registry/src/*/ethereum_serde_utils-0.8.1/src/hex.rs:16 native hex::decode
- ~/.cargo/registry/src/*/hex-0.4.3/src/lib.rs:175 per-byte match decoder, compiled native, not SIMD or LUT
- [`beacon_node/execution_layer/src/engine_api/http.rs:693`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L693) body parsed into serde_json::Value first, then from_value at :696 (an extra owned String per blob)

**Second check.** Read the dependency decoders: hex 0.4.3 is a native per-byte match, and serde is compile-time derive. So two of the three parts of the idea (native decoder, no reflection) hold. Only the intermediate Value/String and the non-SIMD decode remain, so I changed not to partial.

**Verdict history.** not (checked) → partial (refuted)

**Sources.** [lodestar#10358](https://github.com/ChainSafe/lodestar/pull/10358), [teku#10457](https://github.com/Consensys-Incorporated/teku/pull/10457), [teku#10469](https://github.com/Consensys-Incorporated/teku/pull/10469)

</details>


<a id="el_interaction-070"></a>
<details>
<summary><b>el_interaction-070</b> In-process execution client engine calls — <i>n/a · low · S · cpu, latency</i></summary>

**Idea.** When the execution client runs in the same process, call its newPayload, forkchoiceUpdated, getPayload and getBlobs handlers directly with typed values instead of JSON-RPC over HTTP with JWT. This removes serialization, hex encoding and socket overhead.

**Impact.** Lighthouse and the EL are separate processes by design; no in-process EL exists.

**Best measured result.** engine_getPayload mean 16.1 ms JSON-RPC vs 0.39 ms typed (pr:prysm#17702)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engine_api/http.rs:637`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L637) HTTP JSON-RPC client only

**Sources.** [ethlambda#730](https://github.com/lambdaclass/ethlambda/pull/730), [prysm#17702](https://github.com/OffchainLabs/prysm/pull/17702), [ethlambda#530](https://github.com/lambdaclass/ethlambda/pull/530), [prysm#17334](https://github.com/OffchainLabs/prysm/pull/17334)

</details>


<a id="el_interaction-071"></a>
<details>
<summary><b>el_interaction-071</b> Keep builder relay connections warm — <i>not · medium · S · latency</i></summary>

**Idea.** Ping every configured builder/relay periodically or just before the proposal slot so TCP/TLS connections are established before the bid request. The getHeader request then skips the handshake within the tight bid deadline.

**Gap in Lighthouse.** Add a task that hits each relay (status or HEAD) shortly before a local proposer's slot, on the same reqwest::Client, so the pooled TLS connection exists at getHeader time.

**Impact.** Removes a TCP/TLS handshake from the getHeader deadline for proposers using a builder; lodestar measured bid latency 918ms to 294ms.

**Best measured result.** bid request errors 51% (21/41) to 5.7% (8/140); bids received 49% to 83%; bid request 918ms to 294ms (pr:lodestar#9947)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/builder_client/src/pre_gloas_builder_http_client.rs:407`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/builder_client/src/pre_gloas_builder_http_client.rs#L407) get_builder_status defined, no non-test caller
- [`beacon_node/builder_client/src/builder_http_client.rs:82`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/builder_client/src/builder_http_client.rs#L82) plain reqwest::Client::builder(), default pool settings
- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/reqwest-0.12.26/src/async_impl/client.rs:297 default pool_idle_timeout 90s
- [`beacon_node/http_api/src/lib.rs:2833`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L2833) register_validator is the only periodic relay traffic (once per epoch, 384s &gt; 90s idle)

**Second check.** Checked for any warmup path: per-epoch validator registrations do reach the relay but at 384s intervals, above reqwest's 90s pool idle timeout, so the connection is not kept warm; no keepalive or pool settings on the builder clients.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [prysm#17493](https://github.com/OffchainLabs/prysm/pull/17493), [lodestar#9947](https://github.com/ChainSafe/lodestar/pull/9947)

</details>


<a id="el_interaction-072"></a>
<details>
<summary><b>el_interaction-072</b> Shared HTTP client for EL requests — <i>implemented · low · S · latency, cpu</i></summary>

**Idea.** Use one long-lived HTTP client with a connection pool for all eth1/Engine API JSON-RPC requests instead of building a client and connection per request. This avoids repeated TCP setup.

**Impact.** None; one pooled reqwest Client per EL endpoint is reused for every call.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engine_api/http.rs:637`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L637)
- [`beacon_node/execution_layer/src/engine_api/http.rs:652`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L652)
- [`beacon_node/execution_layer/src/engine_api/http.rs:672-676`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L672-L676)
- [`beacon_node/execution_layer/src/lib.rs:581`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L581)

**Skeptic check.** Checked that HttpJsonRpc builds one reqwest Client at construction (lib.rs:581 is the only production constructor) and rpc_request reuses self.client for every POST. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#3060](https://github.com/sigp/lighthouse/pull/3060)

</details>


<a id="el_interaction-073"></a>
<details>
<summary><b>el_interaction-073</b> Persistent WebSocket transport for Engine API — <i>not · low · M · latency, cpu</i></summary>

**Idea.** Offer a persistent WebSocket connection to the EL for Engine API calls, matching responses by request id, instead of one HTTP request per call. This removes per-request connection and HTTP header overhead.

**Gap in Lighthouse.** Add a WS transport behind HttpJsonRpc::rpc_request with id-matched responses.

**Impact.** Reqwest keep-alive pool already avoids per-call TCP setup; WS saves only header bytes (microseconds per call). Also needs EL WS engine support.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engine_api/http.rs:637`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L637) HTTP only; grep for websocket/ws:// in execution_layer/src finds nothing

**Sources.** [teku#10492](https://github.com/Consensys-Incorporated/teku/pull/10492)

</details>


<a id="el_interaction-074"></a>
<details>
<summary><b>el_interaction-074</b> Gzip compression on eth1 HTTP requests — <i>not · low · S · bandwidth</i></summary>

**Idea.** Send Accept-Encoding gzip on HTTP requests to the eth1/EL node so JSON-RPC responses are compressed. This reduces bytes transferred for large responses.

**Gap in Lighthouse.** Original PR is gone; enabling reqwest gzip is a one-line change, but the Engine API is on localhost where compression costs more CPU than it saves.

**Impact.** Negligible: local loopback traffic, compression would add CPU.

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.toml:220 reqwest features lack gzip; no Accept-Encoding set in engine_api/http.rs
- [`beacon_node/execution_layer/src/engine_api/http.rs:637`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L637) plain Client::builder()

**Sources.** [lighthouse#641](https://github.com/sigp/lighthouse/pull/641)

</details>


<a id="el_interaction-075"></a>
<details>
<summary><b>el_interaction-075</b> Fetch only eth1 block headers, not transactions — <i>n/a · low · S · bandwidth, cpu</i></summary>

**Idea.** When following the eth1 chain for deposits and eth1 data voting, request block headers (or getBlockByNumber without full txs) and do not decode transaction hashes or bodies. Only header fields are needed, so transaction transfer and decoding is waste.

**Impact.** Eth1 deposit-following and eth1 data voting no longer exist in Lighthouse, so there is nothing to fetch.

**Evidence (Lighthouse @ 928b61e719).**

- No beacon_node/eth1 crate exists in the checkout; deposit/eth1 voting removed (ls beacon_node)

**Sources.** [prysm#7121](https://github.com/OffchainLabs/prysm/pull/7121), [prysm#11006](https://github.com/OffchainLabs/prysm/pull/11006)

</details>


<a id="el_interaction-076"></a>
<details>
<summary><b>el_interaction-076</b> LRU of recently unblinded payloads — <i>not · low · S · latency, disk, cpu</i></summary>

**Idea.** Keep a small LRU of recently reconstructed (unblinded) execution payloads so repeated lookups for the same block skip the DB and EL payload-body fetch.

**Gap in Lighthouse.** Cache reconstructed full payloads in the reconstruction path (ExecutionLayer reconstruct/get_payload_by_hash callers in beacon_chain) keyed by block root.

**Impact.** Saves repeated EL getPayloadBodies calls for repeated API/blinded-block lookups of the same block; occasional on API-serving nodes, nothing on validating nodes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/payload_cache.rs:9`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/payload_cache.rs#L9) LRU of size 10 holds payloads Lighthouse itself produced (builder/local), not unblinded ones
- [`beacon_node/execution_layer/src/lib.rs:661-667`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L661-L667) get_payload_by_root reads that cache only

**Sources.** [teku#10568](https://github.com/Consensys-Incorporated/teku/pull/10568)

</details>


<a id="el_interaction-077"></a>
<details>
<summary><b>el_interaction-077</b> Separate EL queue for payload-body serving — <i>partial · medium · S · latency</i></summary>

**Idea.** Run engine_getPayloadBodiesByHash for peer RPC serving on its own bounded queue separate from newPayload/forkchoiceUpdated, with batching and per-peer limits. RPC serving then cannot delay block import calls.

**Gap in Lighthouse.** No dedicated EL-side queue or small in-flight cap for getPayloadBodiesByHash: up to num_cpus serving tasks can each have a bodies call in flight on the shared engine HTTP client while newPayload/fcU run. Add a semaphore (e.g. 2) around get_payload_bodies_by_hash v1/v2 and a global/per-peer concurrent-serving limit.

**Impact.** Small for Lighthouse: unlike Teku, LH has no global EL throttle, so newPayload never waits behind bodies calls in a CL queue; the remaining effect is only EL-side contention under heavy serving.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:905-929`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L905-L929) block import queues (chain segment, rpc block, gossip block) are dequeued before
- [`beacon_node/beacon_processor/src/lib.rs:1110-1112`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1110-L1112) BlocksByRange/Root serving queues (separate bounded FIFOs, 1024 each at scheduler/work_queue.rs:390)
- [`beacon_node/beacon_processor/src/lib.rs:1721-1725`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1721-L1725) serving work runs via spawn_async, holding a worker slot until done (lib.rs:1776-1784, max_workers=num_cpus lib.rs:130, 890)
- [`beacon_node/lighthouse_network/src/rpc/config.rs:131-138`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/config.rs#L131-L138) per-peer inbound quotas for blocks and payload envelopes (128 per 10s)
- [`beacon_node/beacon_chain/src/beacon_block_streamer.rs:231`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_block_streamer.rs#L231) and payload_envelope_streamer/mod.rs:208,276 bodies fetched in batches of 32

**Second check.** Beyond execution_layer, checked the beacon processor scheduler, worker-slot accounting and the RPC inbound rate limiter: queue separation, batching and per-peer limits already exist at the CL scheduling layer; only the EL-level dedicated cap is missing.

**Verdict history.** not (checked) → partial (refuted)

**Sources.** [teku#11564](https://github.com/Consensys-Incorporated/teku/pull/11564)

</details>


<a id="el_interaction-078"></a>
<details>
<summary><b>el_interaction-078</b> Bound concurrent in-flight EL requests — <i>partial · medium · S · latency, cpu</i></summary>

**Idea.** Throttle Engine API and eth1 calls with a bounded queue or in-flight cap, and avoid overlapping validations of the same optimistic head. This keeps the EL from being flooded and timing out during bulk work.

**Gap in Lighthouse.** No explicit in-flight cap in Engine::request/HttpJsonRpc; HTTP API, timer and proposer-prep paths bypass the processor bound. Add a semaphore in Engine::request with priority for newPayload/fcU.

**Impact.** Modest; the worker-pool bound and duplicate cache already prevent most flooding, a hard cap would only guard against slow-EL timeouts from non-processor paths.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:130`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L130) max_workers=num_cpus; lib.rs:890 can_spawn gate bounds all block import / chain segment / RPC serving work that issues EL calls
- [`beacon_node/beacon_processor/src/lib.rs:1776-1784`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1776-L1784) async work keeps its worker slot until the EL call completes
- [`beacon_node/beacon_processor/src/lib.rs:179`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L179) DuplicateCache; network/src/network_beacon_processor/gossip_methods.rs:1561, sync_methods.rs:121 avoid concurrent import (and duplicate newPayload) of the same block
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7225`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7225) execution_engine_forkchoice_lock serialises fcU
- [`beacon_node/beacon_processor/src/lib.rs:1726-1731`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1726-L1731) backfill segments on a low-priority rayon pool when rate limiting is enabled

**Second check.** The earlier review looked only for a Semaphore in execution_layer; the beacon processor worker pool indirectly bounds concurrent EL calls and DuplicateCache prevents overlapping validation of one block. The eth1 service no longer exists, so that half of the idea is n/a.

**Verdict history.** not (checked) → partial (refuted)

**Sources.** [teku#4852](https://github.com/Consensys-Incorporated/teku/pull/4852), [teku#1151](https://github.com/Consensys-Incorporated/teku/pull/1151)

</details>


<a id="el_interaction-079"></a>
<details>
<summary><b>el_interaction-079</b> Optimistic block import when EL syncing or offline — <i>partial · medium · M · sync, latency</i></summary>

**Idea.** Import blocks optimistically when the EL returns SYNCING or is unreachable, instead of stalling. The beacon chain stays synced and can give the EL the latest head right away when it recovers.

**Gap in Lighthouse.** Only the SYNCING/ACCEPTED path imports optimistically. When the EL is unreachable or offline, notify_new_payload returns RequestFailed and the block is rejected; Nimbus #4458 treats a missing EL like SYNCING after local block-hash checks. On the gossip/head path LH stalls while the EL is down, except for finalized range sync, which skips the EL.

**Impact.** During EL outages or restarts LH falls behind on head and must catch up after the EL returns, instead of handing the EL the latest head right away.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/execution_payload.rs:150-152`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/execution_payload.rs#L150-L152) Syncing\|Accepted -&gt; PayloadVerificationStatus::Optimistic
- [`beacon_node/beacon_chain/src/execution_payload.rs:213`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/execution_payload.rs#L213) Err(e) =&gt; ExecutionPayloadError::RequestFailed, block not imported
- [`beacon_node/execution_layer/src/engines.rs:114`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engines.rs#L114) EngineError::Offline surfaces as a request error

**Skeptic check.** Verified that the Syncing handling is real. The earlier evidence covered only the SYNCING half of the idea and missed that an unreachable EL turns into a hard import error.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lighthouse#2683](https://github.com/sigp/lighthouse/pull/2683), [nimbus#4458](https://github.com/status-im/nimbus-eth2/pull/4458)

</details>


<a id="el_interaction-080"></a>
<details>
<summary><b>el_interaction-080</b> Skip EL calls for already finalized blocks during sync — <i>partial · medium · S · sync, latency</i></summary>

**Idea.** During range sync, treat blocks that are finalized or far behind the wall slot as optimistic on CL verification alone and skip per-block newPayload/forkchoiceUpdated, updating the EL only occasionally. Per-block EL calls on a syncing EL are wasted work.

**Gap in Lighthouse.** (1) Gloas: BeaconChain::process_range_sync_envelope ignores the segment's NotifyExecutionLayer and calls newPayload for every envelope, even during finalized sync. (2) Head (non-finalized) range sync of blocks far behind the wall slot still calls newPayload per block.

**Impact.** Pre-Gloas finalized range sync already avoids per-block EL calls. After Gloas that saving is lost, because the payload moved into the envelope path.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:497-506`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L497-L506) NotifyExecutionLayer::No only when is_syncing_finalized
- [`beacon_node/beacon_chain/src/execution_payload.rs:78`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/execution_payload.rs#L78) newPayload skipped for pre-Gloas blocks in that case
- [`beacon_node/beacon_chain/src/payload_envelope_verification/import.rs:447-451`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/import.rs#L447-L451) process_range_sync_envelope always NotifyExecutionLayer::Yes
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:175`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L175),350 lookup/parent paths always Yes

**Skeptic check.** The earlier evidence for the pre-Gloas block path was right. It missed that post-Gloas newPayload happens in process_range_sync_envelope, which hardcodes Yes.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [nimbus#4591](https://github.com/status-im/nimbus-eth2/pull/4591), [teku#4458](https://github.com/Consensys-Incorporated/teku/pull/4458), [nimbus#5248](https://github.com/status-im/nimbus-eth2/pull/5248)

</details>


<a id="el_interaction-081"></a>
<details>
<summary><b>el_interaction-081</b> Ordered trie root for payload hash — <i>not · medium · M · cpu</i></summary>

**Idea.** Compute the transactions and withdrawals roots of the execution block header with an ordered-trie routine specialised for index-keyed tries instead of a generic Merkle Patricia trie. Block hash verification gets much faster.

**Gap in Lighthouse.** Replace triehash in calculate_execution_block_hash with an index-keyed ordered trie builder (alloy-trie HashBuilder over sorted rlp(index) keys) for transactions and withdrawals roots.

**Impact.** Not on the live newPayload path: the hash is recomputed only during finalized range sync without the EL and envelope backfill, where it is a per-block CPU cost that limits sync throughput.

**Best measured result.** 100x speed boost (pr:nimbus#6610)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/block_hash.rs:7`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/block_hash.rs#L7),25,29 triehash::ordered_trie_root (generic MPT, crate triehash 0.8.4) for transactions and withdrawals roots
- Cargo.lock:659 alloy-trie 0.9.8 is in the tree but not used by any Lighthouse crate
- [`beacon_node/beacon_chain/src/execution_payload.rs:78-82`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/execution_payload.rs#L78-L82) block hash computed only when NotifyExecutionLayer::No (finalized sync, optimistic_finalized_sync)
- [`beacon_node/beacon_chain/src/payload_envelope_verification/mod.rs:436-441`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/mod.rs#L436-L441) also for Gloas envelope backfill

**Second check.** Confirmed no specialised ordered-trie routine and alloy-trie unused; corrected the earlier impact: verify_payload_block_hash runs only on the NotifyExecutionLayer::No path, not on every newPayload.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [nimbus#6610](https://github.com/status-im/nimbus-eth2/pull/6610)

</details>


<a id="el_interaction-082"></a>
<details>
<summary><b>el_interaction-082</b> Use latestValidHash to mark ancestor runs — <i>partial · low · S · cpu, sync</i></summary>

**Idea.** Use the latestValidHash in newPayload/fcU responses to mark a whole chain of optimistic ancestors valid or invalid in fork choice at once, instead of verifying each block with the EL.

**Gap in Lighthouse.** On an INVALID response, ProtoArray::propagate_execution_payload_invalidation / find_deepest_node_to_invalidate use latestValidHash only to bound the invalidation. Unlike Teku #4924 (markNodeValid on the parent of the first invalid node), they do not promote the latestValidHash block and its optimistic ancestors to Valid, so those ancestors stay optimistic until a later VALID.

**Impact.** Small: it matters only after an INVALID payload, where it lets an optimistic ancestor chain become Valid at once.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/execution_payload.rs:180-191`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/execution_payload.rs#L180-L191) newPayload INVALID -&gt; InvalidateMany with latest_valid_hash
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7279`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7279),7346-7351 fcU VALID -&gt; on_valid_execution_payload; fcU INVALID -&gt; InvalidateMany
- [`consensus/proto_array/src/proto_array.rs:1048-1072`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L1048-L1072) propagate_execution_payload_invalidation only invalidates head..LVH, never marks LVH valid
- [`consensus/proto_array/src/proto_array.rs:960`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L960) propagate_execution_payload_validation used only on VALID responses

**Skeptic check.** The invalidate-many half and the VALID-propagation half are real. The valid-marking half of the Teku mechanism on INVALID responses is missing.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [teku#4924](https://github.com/Consensys-Incorporated/teku/pull/4924)

</details>


<a id="el_interaction-083"></a>
<details>
<summary><b>el_interaction-083</b> Persist validated merge-transition flag — <i>n/a · low · S · cpu, latency</i></summary>

**Idea.** Once the optimistic merge transition payload is validated by the EL, store that fact in DB and memory so the node stops re-validating the transition block.

**Impact.** Merge transition validation code has been removed from Lighthouse; post-merge chain has no transition block to re-validate.

**Evidence (Lighthouse @ 928b61e719).**

- grep for terminal_pow/validate_merge/TerminalBlock across beacon_node and consensus finds nothing

**Sources.** [teku#4995](https://github.com/Consensys-Incorporated/teku/pull/4995)

</details>


<a id="el_interaction-084"></a>
<details>
<summary><b>el_interaction-084</b> Correct payload id cache key for prepared payloads — <i>implemented · low · S · latency</i></summary>

**Idea.** Key the proposer payload-id cache only by head block hash (and attributes or slot), the same key used when filling it, including skipped slots and epoch boundaries. The payload prepared by an earlier fcU is then reused at proposal instead of another fcU and build wait.

**Impact.** The fill and lookup keys are the same, so a prepared payload is reused whenever the attributes are the same. A miss happens only when the attributes really differ, and then a new fcU is needed anyway.

**Best measured result.** slot 0 proposal p50 603ms vs 525ms for other slots (pr:lodestar#10432)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engines.rs:108-111`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engines.rs#L108-L111) PayloadIdCacheKey{head_block_hash, payload_attributes}
- [`beacon_node/execution_layer/src/engines.rs:175-180`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engines.rs#L175-L180) inserted on every fcU with attributes with the same key
- [`beacon_node/execution_layer/src/lib.rs:1340-1352`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1340-L1352) get_full_payload_with looks up the same key, HIT/MISS metric, fallback fcU on miss

**Skeptic check.** Verified that insert and lookup use identical keys built from the same PayloadAttributes. The Prysm/Lodestar bugs came from key mismatches that do not exist here.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#11567](https://github.com/OffchainLabs/prysm/pull/11567), [lodestar#10432](https://github.com/ChainSafe/lodestar/pull/10432), [prysm#12987](https://github.com/OffchainLabs/prysm/pull/12987)

</details>


<a id="el_interaction-085"></a>
<details>
<summary><b>el_interaction-085</b> Split head FCU and payload-attributes FCU — <i>implemented · low · S · latency</i></summary>

**Idea.** On block import, send forkchoiceUpdated without payload attributes immediately, then send a second FCU with attributes asynchronously only when proposing next slot. The EL learns the head earlier and the state advance for attributes leaves the import path.

**Impact.** The EL learns the head first. Attribute computation runs in a spawned task, not in block import.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:1896-1938`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1896-L1938) spawn_execution_layer_updates: fcU for the new head first, then prepare_beacon_proposer sends a second fcU with attributes, in a spawned task off the import path
- [`beacon_node/execution_layer/src/lib.rs:1525-1545`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1525-L1545) payload_attributes keyed by (slot, head_root, payload_status), so the first fcU after a new head has none
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7124-7140`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7124-L7140) prepare_beacon_proposer sends fcU with attributes within prepare_payload_lookahead

**Skeptic check.** The code comment at canonical_head.rs:1923-1929 describes exactly this two-fcU split. The earlier verdict was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#13403](https://github.com/OffchainLabs/prysm/pull/13403)

</details>


<a id="el_interaction-086"></a>
<details>
<summary><b>el_interaction-086</b> Stable payload attributes target slot — <i>implemented · low · S · latency</i></summary>

**Idea.** Compute FCU payload attributes for a stable target slot and do not re-send FCU on proposer-data refresh or late block import. The EL then does not rebuild or drop its payload, and no corrective FCU plus immediate getPayload is needed.

**Impact.** A VC preparation POST at the start of the proposal slot targets slot+1, which is outside the lookahead, so it sends no fcU and does not disturb the in-progress build (Teku scenario 1). A repeated fcU re-sends identical attributes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/lib.rs:1525-1545`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1525-L1545) attributes looked up by ProposerKey{next_slot, head_root, payload_status}
- [`beacon_node/execution_layer/src/lib.rs:1578-1580`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1578-L1580) fcU always uses current_slot+1 as attribute slot
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7124-7140`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7124-L7140) prepare_beacon_proposer sends fcU only within prepare_payload_lookahead of next slot
- [`beacon_node/http_api/src/validator/mod.rs:1066-1080`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L1066-L1080) VC preparation POST calls prepare_beacon_proposer(current_slot), which targets the next slot only

**Skeptic check.** Verified that the attribute slot is fixed at next slot, that it is keyed by head root, and that the lookahead gate is in place. I did not check every late-import-during-proposal interleaving.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#8009](https://github.com/Consensys-Incorporated/teku/pull/8009)

</details>


<a id="el_interaction-087"></a>
<details>
<summary><b>el_interaction-087</b> Longer getPayload timeout without prior preparation — <i>implemented · low · S · latency</i></summary>

**Idea.** When block production finds no prior fcU-prepared payload, allow a longer getPayload timeout so the fallback build is not cut off and the proposal missed.

**Impact.** None: the unprepared fallback (fcU then getPayload) runs each call under its own timeout, so no shared short deadline cuts off the build as in nimbus before #5194.

**Best measured result.** avoids ~500ms added latency (pr:nimbus#5194)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/lib.rs:1342`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1342) cached payload_id lookup, else fresh forkchoiceUpdated with attributes
- [`beacon_node/execution_layer/src/lib.rs:1403`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1403) get_payload issued as a separate request
- [`beacon_node/execution_layer/src/engine_api/http.rs:52`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L52) ENGINE_GET_PAYLOAD_TIMEOUT 2s per call
- [`beacon_node/execution_layer/src/engine_api/http.rs:59`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L59) ENGINE_FORKCHOICE_UPDATED_TIMEOUT 8s per call

**Skeptic check.** Verified get_full_payload_with: missing payload_id triggers a fresh fcU (8s) then getPayload (2s), with no combined deadline. The earlier evidence was right; the nimbus bug (one tight timeout around the fallback) does not exist in Lighthouse.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#5194](https://github.com/status-im/nimbus-eth2/pull/5194)

</details>


<a id="el_interaction-088"></a>
<details>
<summary><b>el_interaction-088</b> Short getPayload deadline to fail over fast — <i>not · medium · S · latency</i></summary>

**Idea.** Use a short deadline (about 300ms) for engine_getPayload in late forks so a slow EL call fails over to another path quickly within the slot.

**Gap in Lighthouse.** Add a shorter getPayload deadline for Gloas+ (about 300ms, times execution_timeout_multiplier) so a stuck local EL gives up early in block production, and the builder bid or an error comes back sooner.

**Impact.** Only matters when the EL is slow at proposal time: the proposer gives up after about 300ms instead of 2s. No steady-state saving.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engine_api/http.rs:52`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L52) ENGINE_GET_PAYLOAD_TIMEOUT = 2s
- [`beacon_node/execution_layer/src/engine_api/http.rs:988-1136`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L988-L1136) every getPayload version (Gloas/Heze included) uses that 2s times execution_timeout_multiplier
- [`beacon_node/execution_layer/src/lib.rs:1077`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1077) tokio::join! waits for both builder header and local payload; no shorter deadline on the local leg

**Verdict history.** not (checked) → not (refuted)

**Sources.** [prysm#17212](https://github.com/OffchainLabs/prysm/pull/17212)

</details>


<a id="el_interaction-089"></a>
<details>
<summary><b>el_interaction-089</b> Retry getPayload with fresh preparation — <i>partial · low · S · latency</i></summary>

**Idea.** If getPayload with a cached payload_id fails, prepare a fresh payload with a new fcU and retry so block production does not miss.

**Gap in Lighthouse.** Lighthouse uses a fresh fcU only on cache miss; if get_payload fails with a cached id it returns the error. Add a retry in the closure in get_payload_impl that issues notify_forkchoice_updated with attributes and calls get_payload again.

**Impact.** Only rescues rare proposals where EL has dropped the payload id; negligible on normal nodes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/lib.rs:1342`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1342) cached payload_id else fresh fcU
- [`beacon_node/execution_layer/src/lib.rs:1403`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1403) get_payload error propagates, no retry

**Sources.** [grandine@165139e95](https://github.com/grandinetech/grandine/commit/165139e95b9f)

</details>


<a id="el_interaction-090"></a>
<details>
<summary><b>el_interaction-090</b> Do not block getPayload on parent-block wait — <i>n/a · low · S · latency</i></summary>

**Idea.** When getPayload is called, stop the payload builder waiting for the txpool to see the parent block after a short grace and wake it, so it returns the best available payload at once.

**Impact.** Erigon txpool/payload-builder internal behaviour; Lighthouse is only an Engine API client.

**Best measured result.** getPayload had waited ~9 s in a head-rewind case (devnet) (pr:caplin#25082)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/lib.rs:1354`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1354) getPayload path just calls the EL

**Sources.** [caplin#25082](https://github.com/erigontech/erigon/pull/25082)

</details>


<a id="el_interaction-091"></a>
<details>
<summary><b>el_interaction-091</b> Notify FCU subscribers only on real sends — <i>n/a · low · S · cpu</i></summary>

**Idea.** Emit forkchoice-updated notifications only when an FCU is actually sent to the EL, not on every check, cutting redundant downstream work.

**Impact.** Lighthouse has no FCU event subscribers to notify; fcU is called directly from update_execution_engine_forkchoice.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:7180`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7180) fcU sent directly under lock, no subscriber notification

**Sources.** [teku#7864](https://github.com/Consensys-Incorporated/teku/pull/7864)

</details>


<a id="el_interaction-092"></a>
<details>
<summary><b>el_interaction-092</b> Skip fcU for heads without newPayload response — <i>n/a · low · S · latency</i></summary>

**Idea.** Do not send forkchoiceUpdated for a head whose newPayload got no EL response, since the EL has not seen the block.

**Impact.** A block whose newPayload errored is not imported as head in Lighthouse, so fcU never targets a head the EL has not seen; Syncing answers import optimistically and fcU is intended.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:7180`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7180) update_execution_engine_forkchoice uses head_hash of imported head

**Sources.** [nimbus#4623](https://github.com/status-im/nimbus-eth2/pull/4623)

</details>


<a id="el_interaction-093"></a>
<details>
<summary><b>el_interaction-093</b> Skip fcU for pre-merge blocks — <i>n/a · low · S · cpu</i></summary>

**Idea.** Do not send forkchoiceUpdated to the EL for heads before the merge transition, avoiding identical redundant Engine API calls.

**Impact.** Pre-merge heads have no head_hash and are skipped; pre-merge is irrelevant on mainnet today.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:7213`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7213) merge-transition proposal no longer supported, returns early when no head_hash

**Sources.** [nimbus#3773](https://github.com/status-im/nimbus-eth2/pull/3773)

</details>


<a id="el_interaction-094"></a>
<details>
<summary><b>el_interaction-094</b> Drop exchangeTransitionConfiguration polling — <i>implemented · low · S · cpu</i></summary>

**Idea.** Remove the periodic engine_exchangeTransitionConfiguration call once it is deprecated, removing a recurring Engine API round trip.

**Impact.** None; there is no recurring transition-configuration call.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engine_api/json_structures.rs:1425`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/json_structures.rs#L1425)
- [`beacon_node/execution_layer/src/engines.rs:295`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engines.rs#L295)

**Skeptic check.** A grep finds no engine_exchangeTransitionConfiguration method or caller. Only the TransitionConfigurationV1 struct remains, and nothing uses it. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#13127](https://github.com/OffchainLabs/prysm/pull/13127), [lighthouse#4517](https://github.com/sigp/lighthouse/pull/4517), [teku#7326](https://github.com/Consensys-Incorporated/teku/pull/7326), [prysm#10413](https://github.com/OffchainLabs/prysm/pull/10413)

</details>


<a id="el_interaction-095"></a>
<details>
<summary><b>el_interaction-095</b> Stop builder status checks after builder removal — <i>n/a · low · S · cpu, bandwidth</i></summary>

**Idea.** Stop the per-slot external builder status health check once the fork that removes the external builder is active.

**Impact.** Lighthouse does not poll builder status per slot (no caller of get_builder_status), so nothing to stop.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/builder_client/src/pre_gloas_builder_http_client.rs:407`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/builder_client/src/pre_gloas_builder_http_client.rs#L407) get_builder_status exists but no per-slot caller found in beacon_node

**Sources.** [teku#11583](https://github.com/Consensys-Incorporated/teku/pull/11583)

</details>


<a id="el_interaction-096"></a>
<details>
<summary><b>el_interaction-096</b> Skip empty builder registration requests — <i>partial · low · S · bandwidth</i></summary>

**Idea.** Do not send the builder validator registration request when the registration list is empty.

**Gap in Lighthouse.** VC already skips empty batches, but the BN forwards a request to the builder even when filtering leaves zero registrations. Add an is_empty check before post_builder_validators in the register_validator handler.

**Impact.** Saves an occasional empty relay HTTP call; trivial.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/preparation_service.rs:442`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/preparation_service.rs#L442) VC skips when signed is empty
- [`beacon_node/http_api/src/validator/mod.rs:813`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L813) BN forwards filtered_registration_data without an empty check

**Sources.** [teku#5682](https://github.com/Consensys-Incorporated/teku/pull/5682)

</details>


<a id="el_interaction-097"></a>
<details>
<summary><b>el_interaction-097</b> Builder client fetches only slots it bid on — <i>n/a · low · bandwidth, cpu</i></summary>

**Idea.** A builder-side client fetches imported blocks only for slots where it submitted a bid, not every slot.

**Impact.** Lighthouse is not a builder client; it has no per-slot bid set to restrict fetching to.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:202`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L202) get_blobs fetch path; no builder-side bid tracking

**Sources.** [lodestar#10257](https://github.com/ChainSafe/lodestar/pull/10257)

</details>


<a id="el_interaction-098"></a>
<details>
<summary><b>el_interaction-098</b> No retries for inclusion list engine call — <i>n/a · low · latency</i></summary>

**Idea.** Disable retries for the inclusion-list Engine API call so a failing request does not hold the serial engine queue ahead of fcU/newPayload.

**Impact.** No standalone inclusion-list Engine API call exists in Lighthouse (only fields in payload attributes), so there are no retries to disable.

**Best measured result.** 3 inclusion-list requests before vs 1 after in tests (pr:lodestar#10415)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engine_api/json_structures.rs:906`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/json_structures.rs#L906) only inclusion_list_transactions in payload attributes; no separate inclusion-list engine call found

**Sources.** [lodestar#10415](https://github.com/ChainSafe/lodestar/pull/10415)

</details>


<a id="el_interaction-099"></a>
<details>
<summary><b>el_interaction-099</b> Per-EL state with multiple ELs, first-response getBlobs — <i>n/a · low · latency</i></summary>

**Idea.** With several ELs configured, keep payload-id cache, validation and retries per connection, and return getBlobs as soon as one EL answers instead of waiting for all.

**Impact.** Lighthouse supports exactly one execution endpoint, so per-EL state and first-response getBlobs do not apply.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/src/config.rs:298-303`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/config.rs#L298-L303) parse_only_one_value for --execution-endpoint (single EL only)

**Sources.** [nimbus#8008](https://github.com/status-im/nimbus-eth2/pull/8008), [nimbus#7847](https://github.com/status-im/nimbus-eth2/pull/7847)

</details>


<a id="el_interaction-100"></a>
<details>
<summary><b>el_interaction-100</b> Recheck cache after acquiring fetch lock — <i>implemented · low · S · latency</i></summary>

**Idea.** For a cached static EL value such as the client version, check the cache again after winning the fetch lock so concurrent callers do not issue redundant engine calls.

**Impact.** None; concurrent callers wait on the async mutex and then read the cache that the first caller filled.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engine_api/http.rs:1449-1463`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L1449-L1463)
- [`beacon_node/execution_layer/src/engine_api/http.rs:1390-1400`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L1390-L1400)

**Skeptic check.** get_engine_version and get_engine_capabilities take the tokio Mutex first, check the cache while holding it, and keep holding it through the fetch. This gives the same result as rechecking after the lock. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#22957](https://github.com/erigontech/erigon/pull/22957)

</details>


<a id="el_interaction-101"></a>
<details>
<summary><b>el_interaction-101</b> Single in-flight wait-for-EL-sync task — <i>partial · low · S · cpu, memory</i></summary>

**Idea.** Allow only one pending wait-for-EL-sync loop at a time instead of spawning parallel ones that pile up.

**Gap in Lighthouse.** Add a single-flight guard (AtomicBool or tokio Mutex try_lock) in Engine::upcheck so only one upcheck task runs at a time; extra callers return immediately.

**Impact.** Under a flapping or offline EL, many concurrent upcheck tasks and RPCs pile up; a guard cuts them to one. Negligible on healthy nodes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engines.rs:340-388`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engines.rs#L340-L388) Engine::request spawns an upcheck task per failed call (and per success while not Synced)
- [`beacon_node/execution_layer/src/engines.rs:240`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engines.rs#L240) upcheck has no in-flight guard

**Sources.** [nimbus@89dccedcc](https://github.com/status-im/nimbus-eth2/commit/89dccedcc9e9), [nimbus#4711](https://github.com/status-im/nimbus-eth2/pull/4711)

</details>


<a id="el_interaction-102"></a>
<details>
<summary><b>el_interaction-102</b> Drop duplicate queued blocks before newPayload — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Keep a small FIFO of recent (block root, signature) in the block processor and drop duplicate queued blocks before processing, avoiding repeated newPayload calls.

**Impact.** Duplicate blocks on gossip, RPC and sync are dropped before newPayload, keyed by root (not root+signature) with the same effect.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:181`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L181) DuplicateCache of in-flight block roots
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1561`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1561) gossip block check_and_insert before process_gossip_verified_block
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:121`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L121) RPC/lookup block check_and_insert, else reprocess queue
- [`beacon_node/beacon_chain/src/block_verification.rs:972`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L972) fork-choice contains_block -&gt; DuplicateFullyImported before state load
- [`beacon_node/beacon_chain/src/block_verification.rs:1953`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1953) same check on the RPC/sync path
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:3807`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L3807) TODO(gloas): no in-flight dedup yet for execution payload envelopes

**Skeptic check.** Verified both the in-flight DuplicateCache on gossip and RPC paths and the fork-choice known-block check on all paths. Only caveat is future Gloas: newPayload moves to the envelope and the gossip/RPC envelope race has no in-flight dedup (TODO at gossip_methods.rs:3807), though gossip envelopes are deduped by observed_payload_envelopes.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#4814](https://github.com/status-im/nimbus-eth2/pull/4814), [nimbus#4850](https://github.com/status-im/nimbus-eth2/pull/4850)

</details>


<a id="el_interaction-103"></a>
<details>
<summary><b>el_interaction-103</b> Skip terminal PoW block polling while syncing — <i>n/a · low · cpu, bandwidth</i></summary>

**Idea.** Do not poll the EL for the terminal PoW block while the CL is still syncing, since the result is unused until synced.

**Impact.** Terminal PoW block polling no longer exists in Lighthouse (post-merge).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:421`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L421) only a stale terminal-block error variant; no PoW terminal block polling in beacon_node

**Sources.** [teku#5009](https://github.com/Consensys-Incorporated/teku/pull/5009), [nimbus#4152](https://github.com/status-im/nimbus-eth2/pull/4152)

</details>


<a id="el_interaction-104"></a>
<details>
<summary><b>el_interaction-104</b> Stop eth1 deposit polling after EIP-6110 — <i>implemented · low · S · cpu, bandwidth, disk</i></summary>

**Idea.** Once deposit requests (EIP-6110) have taken over all legacy deposits, stop eth1 head tracking, deposit-log fetching and eth1 data voting. This removes recurring RPC traffic and processing.

**Impact.** None; there is no eth1 service, no deposit-log polling and no eth1 voting.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5931-5933`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5931-L5933)
- [`beacon_node/beacon_chain/src/block_production/gloas.rs:423`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/gloas.rs#L423)
- [`beacon_node/client/src/builder.rs:54-55`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L54-L55)

**Skeptic check.** Block production copies state.eth1_data() and uses an empty deposits vec, so no eth1 voting or deposit cache runs. The only eth1 constant left is for genesis polling. get_deposit_logs_in_range has no production caller. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#7114](https://github.com/status-im/nimbus-eth2/pull/7114), [prysm#15274](https://github.com/OffchainLabs/prysm/pull/15274), [lodestar#7414](https://github.com/ChainSafe/lodestar/pull/7414), [teku#8141](https://github.com/Consensys-Incorporated/teku/pull/8141), [prysm#15311](https://github.com/OffchainLabs/prysm/pull/15311)

</details>


<a id="el_interaction-105"></a>
<details>
<summary><b>el_interaction-105</b> Poll eth1 at block interval — <i>n/a · low · cpu, bandwidth</i></summary>

**Idea.** Poll the EL for new blocks and logs at the eth1 block interval rather than every second, since data is only needed per voting period.

**Impact.** No eth1 block/log polling exists in Lighthouse at runtime; only the genesis-time wait loop.

**Best measured result.** from 1 request per second to the eth1 block interval (pr:prysm#6221)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/client/src/builder.rs:54-55`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L54-L55) eth1 polling only for genesis (7s interval), no runtime eth1 service

**Sources.** [prysm#6221](https://github.com/OffchainLabs/prysm/pull/6221)

</details>


<a id="el_interaction-106"></a>
<details>
<summary><b>el_interaction-106</b> Avoid tight eth1 follower refetch loop — <i>n/a · low · S · cpu, bandwidth</i></summary>

**Idea.** In the eth1 follower, when the follow distance is at its minimum and blocks are slow, report caught up and return to slow polling instead of refetching in a tight loop.

**Impact.** None: Lighthouse has no eth1 follower or block cache; the eth1 service was removed post-merge, so there is no polling loop.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5931) - block production copies state.eth1_data() and uses deposits = vec![]; no eth1 deposit/log service
- [`beacon_node/client/src/builder.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs) - no eth1 service; grep for deposit_cache/Eth1Service/eth1_block_cache finds nothing in beacon_node
- [`beacon_node/genesis/src`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/genesis/src) - only interop genesis, no eth1 genesis service

**Sources.** [lodestar#4221](https://github.com/ChainSafe/lodestar/pull/4221)

</details>


<a id="el_interaction-107"></a>
<details>
<summary><b>el_interaction-107</b> Poll latest eth1 head instead of block filter — <i>n/a · low · S · bandwidth</i></summary>

**Idea.** Detect new eth1 blocks by polling the latest block at a fixed period instead of an installed block filter.

**Impact.** None: Lighthouse has no eth1 block polling or filter; no eth1 service exists.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5931) - block production copies state.eth1_data() and uses deposits = vec![]; no eth1 deposit/log service
- [`beacon_node/client/src/builder.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs) - no eth1 service; grep for deposit_cache/Eth1Service/eth1_block_cache finds nothing in beacon_node
- [`beacon_node/genesis/src`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/genesis/src) - only interop genesis, no eth1 genesis service

**Sources.** [teku#1990](https://github.com/Consensys-Incorporated/teku/pull/1990)

</details>


<a id="el_interaction-108"></a>
<details>
<summary><b>el_interaction-108</b> Keep adaptive log chunk size across reconnects — <i>n/a · low · S · sync, latency</i></summary>

**Idea.** Remember the adaptive deposit-log chunk size across EL reconnects so fetches do not restart at large chunks that time out again.

**Impact.** None: Lighthouse has no deposit log fetching from the EL; deposits come via the execution requests in the payload.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5931) - block production copies state.eth1_data() and uses deposits = vec![]; no eth1 deposit/log service
- [`beacon_node/client/src/builder.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs) - no eth1 service; grep for deposit_cache/Eth1Service/eth1_block_cache finds nothing in beacon_node
- [`beacon_node/genesis/src`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/genesis/src) - only interop genesis, no eth1 genesis service

**Sources.** [nimbus#3960](https://github.com/status-im/nimbus-eth2/pull/3960)

</details>


<a id="el_interaction-109"></a>
<details>
<summary><b>el_interaction-109</b> Load deposit tree snapshot once — <i>n/a · low · S · startup, disk</i></summary>

**Idea.** Load the deposit tree snapshot once at startup with a fixed source precedence (custom path, DB, bundled file) instead of querying and loading it repeatedly.

**Impact.** None: Lighthouse has no deposit tree snapshot or deposit cache; there is nothing to load.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5931) - block production copies state.eth1_data() and uses deposits = vec![]; no eth1 deposit/log service
- [`beacon_node/client/src/builder.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs) - no eth1 service; grep for deposit_cache/Eth1Service/eth1_block_cache finds nothing in beacon_node
- [`beacon_node/genesis/src`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/genesis/src) - only interop genesis, no eth1 genesis service

**Sources.** [teku#8113](https://github.com/Consensys-Incorporated/teku/pull/8113)

</details>


<a id="el_interaction-110"></a>
<details>
<summary><b>el_interaction-110</b> In-memory pending deposits store — <i>n/a · low · S · disk, latency</i></summary>

**Idea.** Keep pending deposits in memory keyed by eth1 block number (insert on log, remove on inclusion) instead of querying the DB when building a block.

**Impact.** None: Lighthouse has no pending-deposit store from eth1 logs; block production sets deposits = vec![] (beacon_chain.rs:5933).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5931) - block production copies state.eth1_data() and uses deposits = vec![]; no eth1 deposit/log service
- [`beacon_node/client/src/builder.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs) - no eth1 service; grep for deposit_cache/Eth1Service/eth1_block_cache finds nothing in beacon_node
- [`beacon_node/genesis/src`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/genesis/src) - only interop genesis, no eth1 genesis service

**Sources.** [prysm#1475](https://github.com/OffchainLabs/prysm/pull/1475)

</details>


<a id="el_interaction-111"></a>
<details>
<summary><b>el_interaction-111</b> Incremental pre-genesis state from deposits — <i>n/a · low · S · cpu, startup</i></summary>

**Idea.** Process each eth1 deposit into an in-memory pre-genesis state as it arrives instead of reprocessing all deposits at chain start.

**Impact.** None: Lighthouse has no eth1 genesis service building pre-genesis state from deposits; networks start from a genesis state file.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5931) - block production copies state.eth1_data() and uses deposits = vec![]; no eth1 deposit/log service
- [`beacon_node/client/src/builder.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs) - no eth1 service; grep for deposit_cache/Eth1Service/eth1_block_cache finds nothing in beacon_node
- [`beacon_node/genesis/src`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/genesis/src) - only interop genesis, no eth1 genesis service

**Sources.** [prysm#4306](https://github.com/OffchainLabs/prysm/pull/4306)

</details>


<a id="el_interaction-112"></a>
<details>
<summary><b>el_interaction-112</b> Lazy deposit iteration for proposals — <i>n/a · low · S · memory, cpu</i></summary>

**Idea.** Iterate deposits between two eth1 data points lazily and keep only roots, instead of materializing the whole deposit list during block proposal.

**Impact.** None: Lighthouse has no eth1 deposit iteration in block proposal; deposits = vec![] (beacon_chain.rs:5933).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5931) - block production copies state.eth1_data() and uses deposits = vec![]; no eth1 deposit/log service
- [`beacon_node/client/src/builder.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs) - no eth1 service; grep for deposit_cache/Eth1Service/eth1_block_cache finds nothing in beacon_node
- [`beacon_node/genesis/src`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/genesis/src) - only interop genesis, no eth1 genesis service

**Sources.** [nimbus#3947](https://github.com/status-im/nimbus-eth2/pull/3947)

</details>


<a id="el_interaction-113"></a>
<details>
<summary><b>el_interaction-113</b> Single-pass grouping of deposit events by block — <i>n/a · low · S · cpu</i></summary>

**Idea.** Group deposit events by block number in one sorted pass into a map instead of filtering the full list per block (quadratic).

**Impact.** None: Lighthouse has no deposit event log grouping; no eth1 deposit log processing exists.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5931) - block production copies state.eth1_data() and uses deposits = vec![]; no eth1 deposit/log service
- [`beacon_node/client/src/builder.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs) - no eth1 service; grep for deposit_cache/Eth1Service/eth1_block_cache finds nothing in beacon_node
- [`beacon_node/genesis/src`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/genesis/src) - only interop genesis, no eth1 genesis service

**Sources.** [lodestar@650b85a40](https://github.com/ChainSafe/lodestar/commit/650b85a40b60)

</details>


<a id="el_interaction-114"></a>
<details>
<summary><b>el_interaction-114</b> Precompute deposit log topic hash — <i>n/a · low · S · cpu</i></summary>

**Idea.** Hash the deposit event topic once at startup and compare logs against the constant instead of rehashing per comparison.

**Impact.** None; the deposit-log path does not run on a current node.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engine_api/http.rs:256`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L256)
- [`beacon_node/execution_layer/src/engine_api/http.rs:549`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L549)

**Skeptic check.** DEPOSIT_EVENT_TOPIC is a precomputed constant, so no rehashing happens. But get_deposit_logs_in_range has no production callers, so the idea does not apply to Lighthouse's live paths. I changed the verdict to n/a, not a gap.

**Verdict history.** implemented (checked) → n/a (skeptic)

**Sources.** [prysm#3981](https://github.com/OffchainLabs/prysm/pull/3981)

</details>


<a id="el_interaction-115"></a>
<details>
<summary><b>el_interaction-115</b> Pass deposit logs by pointer — <i>n/a · low · S · memory</i></summary>

**Idea.** Pass deposit log structures by reference instead of by value during log processing to avoid copies.

**Impact.** None on a current mainnet node; the eth1 deposit path is not run. Lighthouse no longer has an eth1 deposit-tracking service (deposits come via EL requests, EIP-6110); only dead helper code remains in engine_api/http.rs.

**Best measured result.** 14% of heap held in ProcessLog (pr:prysm#12818)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engine_api/http.rs:256`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L256) DEPOSIT_EVENT_TOPIC constant; get_deposit_logs_in_range (l.549) has no callers in the tree, no eth1 deposit service remains

**Sources.** [prysm#12818](https://github.com/OffchainLabs/prysm/pull/12818)

</details>


<a id="el_interaction-116"></a>
<details>
<summary><b>el_interaction-116</b> No eth1 timestamp lookups in validator status — <i>n/a · low · S · latency</i></summary>

**Idea.** Avoid per-validator eth1 block timestamp lookups in validator status API paths, which are slow against hosted providers.

**Impact.** None on a current mainnet node; the eth1 deposit path is not run. Lighthouse no longer has an eth1 deposit-tracking service (deposits come via EL requests, EIP-6110); only dead helper code remains in engine_api/http.rs.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engine_api/http.rs:256`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L256) DEPOSIT_EVENT_TOPIC constant; get_deposit_logs_in_range (l.549) has no callers in the tree, no eth1 deposit service remains

**Sources.** [prysm#8023](https://github.com/OffchainLabs/prysm/pull/8023)

</details>


<a id="el_interaction-117"></a>
<details>
<summary><b>el_interaction-117</b> Do eth1 lookups in eth1 service, not state transition — <i>n/a · low · S · latency</i></summary>

**Idea.** Fetch the eth1 block timestamp for each deposit in the eth1 service when the deposit is received, not inside state/genesis processing, so the event queue does not back up.

**Impact.** None on a current mainnet node; the eth1 deposit path is not run. Lighthouse no longer has an eth1 deposit-tracking service (deposits come via EL requests, EIP-6110); only dead helper code remains in engine_api/http.rs.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engine_api/http.rs:256`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L256) DEPOSIT_EVENT_TOPIC constant; get_deposit_logs_in_range (l.549) has no callers in the tree, no eth1 deposit service remains

**Sources.** [teku#1116](https://github.com/Consensys-Incorporated/teku/pull/1116)

</details>


<a id="el_interaction-118"></a>
<details>
<summary><b>el_interaction-118</b> Publish deposits as block responses arrive — <i>n/a · low · S · latency, sync</i></summary>

**Idea.** While fetching block data for deposits, publish deposits in order as each response arrives instead of waiting for all requests, overlapping processing with fetches.

**Impact.** None on a current mainnet node; the eth1 deposit path is not run. Lighthouse no longer has an eth1 deposit-tracking service (deposits come via EL requests, EIP-6110); only dead helper code remains in engine_api/http.rs.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engine_api/http.rs:256`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L256) DEPOSIT_EVENT_TOPIC constant; get_deposit_logs_in_range (l.549) has no callers in the tree, no eth1 deposit service remains

**Sources.** [teku#1156](https://github.com/Consensys-Incorporated/teku/pull/1156)

</details>


<a id="el_interaction-119"></a>
<details>
<summary><b>el_interaction-119</b> Update deposit tracking incrementally in background — <i>n/a · low · S · latency</i></summary>

**Idea.** Update eth1/deposit tracking structures in the background as finality advances instead of all at once just before proposing.

**Impact.** None on a current mainnet node; the eth1 deposit path is not run. Lighthouse no longer has an eth1 deposit-tracking service (deposits come via EL requests, EIP-6110); only dead helper code remains in engine_api/http.rs.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engine_api/http.rs:256`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L256) DEPOSIT_EVENT_TOPIC constant; get_deposit_logs_in_range (l.549) has no callers in the tree, no eth1 deposit service remains

**Sources.** [nimbus#2118](https://github.com/status-im/nimbus-eth2/pull/2118)

</details>


<a id="el_interaction-120"></a>
<details>
<summary><b>el_interaction-120</b> Follow eth1 blocks, not only deposit events — <i>n/a · low · S · sync</i></summary>

**Idea.** Follow eth1 blocks in addition to deposit logs to detect genesis precisely and sync eth1 deposit data faster.

**Impact.** None on a current mainnet node; the eth1 deposit path is not run. Lighthouse no longer has an eth1 deposit-tracking service (deposits come via EL requests, EIP-6110); only dead helper code remains in engine_api/http.rs.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engine_api/http.rs:256`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L256) DEPOSIT_EVENT_TOPIC constant; get_deposit_logs_in_range (l.549) has no callers in the tree, no eth1 deposit service remains

**Sources.** [nimbus#1247](https://github.com/status-im/nimbus-eth2/pull/1247), [nimbus@31e31bb30](https://github.com/status-im/nimbus-eth2/commit/31e31bb30c71)

</details>


<a id="el_interaction-121"></a>
<details>
<summary><b>el_interaction-121</b> Start eth1 scan at deposit contract deploy block — <i>n/a · low · S · startup, bandwidth</i></summary>

**Idea.** Start the min-genesis block search and deposit log scanning at the known deposit contract deploy block instead of earlier blocks.

**Impact.** None on a current mainnet node; the eth1 deposit path is not run. Lighthouse no longer has an eth1 deposit-tracking service (deposits come via EL requests, EIP-6110); only dead helper code remains in engine_api/http.rs.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engine_api/http.rs:256`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L256) DEPOSIT_EVENT_TOPIC constant; get_deposit_logs_in_range (l.549) has no callers in the tree, no eth1 deposit service remains

**Sources.** [teku#3338](https://github.com/Consensys-Incorporated/teku/pull/3338)

</details>


<a id="el_interaction-122"></a>
<details>
<summary><b>el_interaction-122</b> Wait until EL reaches deploy block before queries — <i>n/a · low · S · bandwidth, cpu</i></summary>

**Idea.** Do not issue deposit log or block range queries until the EL follow block has reached the deposit contract deploy block, so a syncing EL is not flooded.

**Impact.** No deposit log or block range queries are made, so no flood of a syncing EL. Lighthouse has no eth1/deposit-log service any more (no beacon_node/eth1 crate; deposits come from the EL via EIP-6110 requests in the block), so there is nothing to throttle.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/src/config.rs:513`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/config.rs#L513) - deploy block only logged
- beacon_node/ - no eth1 crate; ls shows beacon_chain, execution_layer, genesis, ...
- [`beacon_node/genesis/src`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/genesis/src) - only interop.rs/common.rs, no eth1 genesis service

**Sources.** [lodestar#3930](https://github.com/ChainSafe/lodestar/pull/3930)

</details>


<a id="el_interaction-123"></a>
<details>
<summary><b>el_interaction-123</b> Skip genesis block search with anchor state — <i>n/a · low · S · startup</i></summary>

**Idea.** Skip the min-genesis PoW block search when an anchor state is available, avoiding slow historic EL block lookups at startup.

**Impact.** No min-genesis search exists; genesis comes from a state file. Lighthouse has no eth1/deposit-log service any more (no beacon_node/eth1 crate; deposits come from the EL via EIP-6110 requests in the block), so there is nothing to throttle.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/src/config.rs:513`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/config.rs#L513) - deploy block only logged
- beacon_node/ - no eth1 crate; ls shows beacon_chain, execution_layer, genesis, ...
- [`beacon_node/genesis/src`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/genesis/src) - only interop.rs/common.rs, no eth1 genesis service

**Sources.** [teku#6104](https://github.com/Consensys-Incorporated/teku/pull/6104)

</details>


<a id="el_interaction-124"></a>
<details>
<summary><b>el_interaction-124</b> Fetch eth1 blocks only after a deposit event — <i>n/a · low · S · bandwidth</i></summary>

**Idea.** Do not fetch eth1 blocks until at least one deposit event has been fetched, since they are unused before.

**Impact.** No eth1 block fetching exists. Lighthouse has no eth1/deposit-log service any more (no beacon_node/eth1 crate; deposits come from the EL via EIP-6110 requests in the block), so there is nothing to throttle.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/src/config.rs:513`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/config.rs#L513) - deploy block only logged
- beacon_node/ - no eth1 crate; ls shows beacon_chain, execution_layer, genesis, ...
- [`beacon_node/genesis/src`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/genesis/src) - only interop.rs/common.rs, no eth1 genesis service

**Sources.** [lodestar@4b13ea35a](https://github.com/ChainSafe/lodestar/commit/4b13ea35ae3e)

</details>


<a id="el_interaction-125"></a>
<details>
<summary><b>el_interaction-125</b> Store eth1 data only in needed window — <i>n/a · low · S · disk, bandwidth</i></summary>

**Idea.** Fetch and store eth1 data only for blocks after the minimum timestamp needed for proposing, and only once synced.

**Impact.** No eth1 data cache exists. Lighthouse has no eth1/deposit-log service any more (no beacon_node/eth1 crate; deposits come from the EL via EIP-6110 requests in the block), so there is nothing to throttle.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/src/config.rs:513`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/config.rs#L513) - deploy block only logged
- beacon_node/ - no eth1 crate; ls shows beacon_chain, execution_layer, genesis, ...
- [`beacon_node/genesis/src`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/genesis/src) - only interop.rs/common.rs, no eth1 genesis service

**Sources.** [lodestar#1385](https://github.com/ChainSafe/lodestar/pull/1385)

</details>


<a id="el_interaction-126"></a>
<details>
<summary><b>el_interaction-126</b> Init deposit cache from finalized state — <i>n/a · low · S · startup, cpu</i></summary>

**Idea.** Initialize the deposit cache from the finalized checkpoint state instead of regenerating the head state.

**Impact.** No deposit cache is built from the head state; only a builder-deposits cache in state_processing. Lighthouse has no eth1/deposit-log service any more (no beacon_node/eth1 crate; deposits come from the EL via EIP-6110 requests in the block), so there is nothing to throttle.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/src/config.rs:513`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/config.rs#L513) - deploy block only logged
- beacon_node/ - no eth1 crate; ls shows beacon_chain, execution_layer, genesis, ...
- [`beacon_node/genesis/src`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/genesis/src) - only interop.rs/common.rs, no eth1 genesis service

**Sources.** [prysm#7715](https://github.com/OffchainLabs/prysm/pull/7715)

</details>


<a id="el_interaction-127"></a>
<details>
<summary><b>el_interaction-127</b> Borrow eth1 service instead of cloning — <i>n/a · low · S · memory, cpu</i></summary>

**Idea.** Pass the eth1 service by reference into async functions instead of cloning it.

**Impact.** The eth1 service the PR touched is gone; nothing to borrow.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/src/config.rs:513`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/config.rs#L513) - deploy block only logged
- beacon_node/ - no eth1 crate; ls shows beacon_chain, execution_layer, genesis, ...
- [`beacon_node/genesis/src`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/genesis/src) - only interop.rs/common.rs, no eth1 genesis service

**Sources.** [lighthouse#1294](https://github.com/sigp/lighthouse/pull/1294)

</details>


<a id="el_interaction-128"></a>
<details>
<summary><b>el_interaction-128</b> Release old RPC client on EL reconnect — <i>implemented · low · S · memory</i></summary>

**Idea.** On EL connection restart, fully release the old RPC client and its subscriptions so reconnects do not leak resources.

**Impact.** None; the EL is reached over HTTP with no subscriptions, and the client is never rebuilt on reconnect.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engine_api/http.rs:23`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L23)
- [`beacon_node/execution_layer/src/engine_api/http.rs:637-656`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L637-L656)
- [`beacon_node/execution_layer/src/lib.rs:581`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L581)

**Skeptic check.** The engine is reached by HTTP JSON-RPC with one client built at startup and no websocket subscriptions, so a reconnect has nothing to leak. The problem does not exist by design. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus@ba59dd85c](https://github.com/status-im/nimbus-eth2/commit/ba59dd85cd86)

</details>


<a id="el_interaction-129"></a>
<details>
<summary><b>el_interaction-129</b> In-place chunked HTTP decoding — <i>n/a · low · S · memory, cpu</i></summary>

**Idea.** Decode chunked HTTP responses from the EL in place, moving body bytes over the framing, so large responses are read without extra copies.

**Impact.** Hyper handles chunked decoding in its own buffer; a custom in-place decoder is a hand-written HTTP stack feature that Lighthouse does not have.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engine_api/http.rs:9`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L9) - uses reqwest (hyper) which decodes chunked bodies itself

**Sources.** [silver#291](https://github.com/gattaca-com/silver/pull/291), [silver#71](https://github.com/gattaca-com/silver/pull/71)

</details>


<a id="el_interaction-130"></a>
<details>
<summary><b>el_interaction-130</b> Larger transport buffers for EL JSON-RPC — <i>not · low · S · cpu</i></summary>

**Idea.** Use larger (16KB) transport read/write buffers for EL JSON-RPC to cut syscalls on large payloads.

**Gap in Lighthouse.** Lighthouse does not tune hyper read/write buffer sizes; one could set hyper buffer options on the reqwest builder in HttpJsonRpc::new, but hyper already grows its read buffer adaptively.

**Impact.** Negligible; a few fewer syscalls on multi-hundred-KB newPayload/getPayload bodies over loopback, unmeasurable against EL execution time.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engine_api/http.rs:637`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L637) Client::builder().build() with default reqwest/hyper buffers
- [`beacon_node/execution_layer/src/engine_api/http.rs:679`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L679) body serialised via .json(&amp;body), no buffer tuning

**Sources.** [nimbus#5893](https://github.com/status-im/nimbus-eth2/pull/5893)

</details>


<a id="el_interaction-131"></a>
<details>
<summary><b>el_interaction-131</b> Lightweight Engine API JSON-RPC client — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Use a thin HTTP client with direct JSON serialization for Engine API calls instead of a heavyweight generic web3 client.

**Impact.** None; the client is already thin.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engine_api/http.rs:660-694`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L660-L694)

**Skeptic check.** rpc_request is a plain reqwest POST with a serde JsonRequestBody and a typed response, with no web3 library layer. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#10475](https://github.com/Consensys-Incorporated/teku/pull/10475), [lodestar@df6b93532](https://github.com/ChainSafe/lodestar/commit/df6b9353200d)

</details>


<a id="el_interaction-132"></a>
<details>
<summary><b>el_interaction-132</b> Reuse execution requests codec instance — <i>n/a · low · S · cpu, memory</i></summary>

**Idea.** Keep one execution requests codec per fork instead of constructing one for each getPayload decode.

**Impact.** No codec instance exists to reuse; SSZ types are zero-sized Rust types.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engine_api/json_structures.rs:578-657`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/json_structures.rs#L578-L657) decode of requests is plain functions per fork, no codec object constructed

**Sources.** [teku#10893](https://github.com/Consensys-Incorporated/teku/pull/10893)

</details>


<a id="el_interaction-133"></a>
<details>
<summary><b>el_interaction-133</b> Reuse received transaction encodings — <i>n/a · medium · S · cpu</i></summary>

**Idea.** Keep the EIP-2718 transaction bytes received in a payload and reuse them when building stored block bodies instead of re-encoding.

**Impact.** Lighthouse stores EL-received transaction bytes as-is in the SSZ body and never re-encodes EIP-2718, so there is nothing to reuse.

**Best measured result.** p50 newPayload +1.0% faster (90.52 -&gt; 89.61 ms), p90 +1.7% (pr:caplin#21546)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/execution/execution_payload.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/execution/execution_payload.rs) transactions held as opaque byte lists
- [`beacon_node/execution_layer/src/engine_api/json_structures.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/json_structures.rs) JSON hex decoded straight into the SSZ payload

**Sources.** [caplin#21546](https://github.com/erigontech/erigon/pull/21546)

</details>


<a id="el_interaction-134"></a>
<details>
<summary><b>el_interaction-134</b> Single allocation for prefixed serialization — <i>partial · low · S · memory, cpu</i></summary>

**Idea.** Serialize execution requests with a prefix byte into one buffer allocated with an extra byte instead of allocating and copying twice.

**Gap in Lighthouse.** Allocate a Vec with capacity 1+ssz_bytes_len, push the type byte, then ssz_append into it, in build_execution_requests_list and its Electra/Gloas callers.

**Impact.** Saves one copy of the requests bytes per payload; requests are typically a few KB at most, so microseconds.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/execution/execution_requests.rs:146-153`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/execution/execution_requests.rs#L146-L153) build_execution_requests_list: as_ssz_bytes() Vec then Bytes::from_iter([type].chain(ssz)) copies into a second allocation
- [`consensus/types/src/execution/execution_requests.rs:158-165`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/execution/execution_requests.rs#L158-L165) requests_hash reuses that list
- [`beacon_node/execution_layer/src/engine_api/json_structures.rs:566-574`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/json_structures.rs#L566-L574) then hex::encode+format! allocate again

**Sources.** [lodestar#10356](https://github.com/ChainSafe/lodestar/pull/10356)

</details>


<a id="el_interaction-135"></a>
<details>
<summary><b>el_interaction-135</b> Semaphore wake instead of poll loop — <i>n/a · low · S · latency</i></summary>

**Idea.** Replace a 100ms poll/retry loop on a busy executor with a blocking semaphore acquire so work wakes as soon as the previous op releases.

**Impact.** Lighthouse is async and wakes on lock release already; the Go executor poll loop has no counterpart.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engines.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engines.rs) uses async tokio locks/tasks, no 100ms poll loop on a busy executor

**Sources.** [caplin#21549](https://github.com/erigontech/erigon/pull/21549)

</details>


<a id="el_interaction-136"></a>
<details>
<summary><b>el_interaction-136</b> Parallel trie prefetch for state root — <i>n/a · low · L · disk, latency</i></summary>

**Idea.** During state-root computation, prefetch trie branches, accounts and storage in parallel into a cache that the trie update reads first, avoiding repeated DB reads.

**Impact.** EL-side optimisation (Caplin embeds an EL); a consensus client has no trie.

**Evidence (Lighthouse @ 928b61e719).**

- Trie/state-root computation is inside the execution client; [`beacon_node/execution_layer`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer) only calls engine API (http.rs:811 newPayload)

**Sources.** [caplin#18473](https://github.com/erigontech/erigon/pull/18473)

</details>


<a id="el_interaction-137"></a>
<details>
<summary><b>el_interaction-137</b> Reject invalid block access list early — <i>n/a · low · M · cpu</i></summary>

**Idea.** Reject block access list indices beyond len(transactions)+1 before execution so invalid payloads do not trigger expensive expansion work.

**Impact.** Lighthouse never decodes or expands the BAL; the EL does that work and rejects invalid indices. A CL-side pre-check would require RLP-decoding the BAL for no CL benefit.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/execution/execution_payload.rs:33`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/execution/execution_payload.rs#L33) BlockAccessList = ProgressiveVariableList&lt;u8&gt;, opaque bytes
- [`beacon_node/execution_layer/src/engine_api.rs:502`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api.rs#L502) passed through to EL unparsed

**Sources.** [caplin#24908](https://github.com/erigontech/erigon/pull/24908), [caplin#24684](https://github.com/erigontech/erigon/pull/24684)

</details>


<a id="el_interaction-138"></a>
<details>
<summary><b>el_interaction-138</b> Persist block access list for state read-ahead — <i>n/a · low · cpu, latency</i></summary>

**Idea.** Persist the block access list when importing payloads in-process so the EL can warm state reads ahead of execution.

**Impact.** Lighthouse talks to an external EL over engine API; persisting the BAL for read-ahead is an in-process-EL (Caplin/Erigon) concern.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/lib.rs:2148`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L2148) BAL only carried inside payload bodies
- [`consensus/types/src/execution/signed_execution_payload_envelope.rs:166`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/execution/signed_execution_payload_envelope.rs#L166) block_access_list field

**Sources.** [caplin#22874](https://github.com/erigontech/erigon/pull/22874)

</details>


<a id="el_interaction-139"></a>
<details>
<summary><b>el_interaction-139</b> Cache terminal PoW block lookups — <i>n/a · low · latency, cpu</i></summary>

**Idea.** Keep a small cache of execution blocks fetched by hash so terminal-block validation does not repeat the same JSON-RPC lookup.

**Impact.** Lighthouse has no eth1/PoW code any more: beacon_node has no eth1 crate (ls beacon_node shows beacon_chain, genesis, execution_layer ...); grep for get_pow_block/is_valid_terminal_pow finds only a doc comment. Terminal PoW validation is gone post-merge.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engine_api.rs:139`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api.rs#L139) only stale doc mention of get_pow_block_hash_at_total_difficulty
- beacon_node (no eth1 dir)

**Sources.** [lighthouse#2635](https://github.com/sigp/lighthouse/pull/2635), [prysm#10205](https://github.com/OffchainLabs/prysm/pull/10205)

</details>


<a id="el_interaction-140"></a>
<details>
<summary><b>el_interaction-140</b> Sparse checkpointed eth1 block scan for genesis — <i>n/a · low · startup, sync</i></summary>

**Idea.** While building genesis, query eth1 blocks only at checkpoints, jumping by large steps far from the minimum genesis time and per block only when close. This cuts block lookups from n to about log n.

**Impact.** Eth1 genesis service removed; mainnet genesis is long past, so no scan is needed.

**Best measured result.** getBlock calls reduced from n to log2(n); Altona genesis found in ~1 min in CI (pr:lodestar#1101)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/genesis/src/lib.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/genesis/src/lib.rs), interop.rs: only interop/ genesis-state helpers
- no eth1 crate in beacon_node

**Sources.** [lodestar#1443](https://github.com/ChainSafe/lodestar/pull/1443), [lodestar#1101](https://github.com/ChainSafe/lodestar/pull/1101)

</details>


<a id="el_interaction-141"></a>
<details>
<summary><b>el_interaction-141</b> Poll eth1 fast while behind, slow once caught up — <i>n/a · low · sync, latency</i></summary>

**Idea.** Poll the eth1 deposit and block source at a short interval while behind the head and switch to the slow interval once caught up.

**Impact.** Eth1 deposit/block polling no longer exists in Lighthouse.

**Best measured result.** "Previously all polling happened at 7s intervals, this made it quite slow to catch up to the head." (pr:lighthouse#1103)

**Evidence (Lighthouse @ 928b61e719).**

- no eth1 crate in beacon_node (deposit-log polling removed)

**Sources.** [lighthouse#1103](https://github.com/sigp/lighthouse/pull/1103)

</details>


<a id="el_interaction-142"></a>
<details>
<summary><b>el_interaction-142</b> Single-pass typed decoding of block transactions — <i>n/a · low · cpu, memory</i></summary>

**Idea.** Decode the transaction list of JSON-RPC execution blocks directly into typed transactions instead of re-marshaling each generic JSON item and unmarshaling it again.

**Impact.** Lighthouse's eth_getBlockBy* calls fetch headers without full transactions and no generic re-marshal of tx lists happens.

**Best measured result.** PR states it reduces the performance hit of marshaling and unmarshaling each transaction; no numbers (pr:prysm#11060)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engine_api/http.rs:1773-1787`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L1773-L1787) encode/decode_transactions only used on engine API payloads
- http.rs:32,800 only eth_getBlockByNumber for header-only ExecutionBlock

**Sources.** [prysm#11060](https://github.com/OffchainLabs/prysm/pull/11060)

</details>


<a id="el_interaction-143"></a>
<details>
<summary><b>el_interaction-143</b> Fetch single payload body by hash — <i>implemented · low · S · latency</i></summary>

**Idea.** Fetch one execution payload body with getPayloadBodiesByHash instead of a by-range request with count 1.

**Impact.** Already uses by-hash for single bodies; there is no by-range call.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/lib.rs:1726-1730`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1726-L1730)
- [`beacon_node/execution_layer/src/engine_api/http.rs:1286`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L1286)

**Skeptic check.** get_payload_for_header calls get_payload_bodies_by_hash(vec![block_hash]). No get_payload_bodies_by_range caller exists in beacon_node. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#10007](https://github.com/sigp/lighthouse/pull/10007)

</details>


<a id="el_interaction-144"></a>
<details>
<summary><b>el_interaction-144</b> Bundle deposit tree snapshot per network — <i>n/a · low · startup, sync</i></summary>

**Idea.** Ship a deposit tree snapshot per network with the client and pick the better of bundled and stored, so startup does not replay deposit logs from the contract genesis.

**Impact.** Deposit log replay from the contract no longer happens; deposits come via EL requests (EIP-6110).

**Best measured result.** "dramatically decreases the time" of deposit log sync and replay at startup (no numbers) (pr:teku#7039)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/deposit/deposit_tree_snapshot.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/deposit/deposit_tree_snapshot.rs) exists for the types/API only; no eth1 deposit log sync in beacon_node

**Sources.** [teku#6496](https://github.com/Consensys-Incorporated/teku/pull/6496), [teku#7039](https://github.com/Consensys-Incorporated/teku/pull/7039)

</details>


<a id="el_interaction-145"></a>
<details>
<summary><b>el_interaction-145</b> Cache engine capabilities and client version — <i>implemented · low · S · latency</i></summary>

**Idea.** Cache the EL exchangeCapabilities and getClientVersion responses, refreshing only periodically or after the engine goes offline, instead of calling per use or per proposal.

**Impact.** Both responses are cached and refreshed on age limit or cache clear.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engine_api/http.rs:1384-1400`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L1384-L1400)
- [`beacon_node/execution_layer/src/engine_api/http.rs:1436-1464`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L1436-L1464)
- [`beacon_node/execution_layer/src/engine_api/http.rs:1423`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L1423)

**Skeptic check.** get_engine_capabilities and get_engine_version both use a CachedResponse with an age_limit. clear_engine_version_cache resets the version cache. Hot callers such as get_blobs_v2 pass None, so they always use the cached capabilities.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#3918](https://github.com/sigp/lighthouse/pull/3918), [caplin#22303](https://github.com/erigontech/erigon/pull/22303)

</details>


<a id="el_interaction-146"></a>
<details>
<summary><b>el_interaction-146</b> Check genesis readiness via contract constant — <i>n/a · low · startup</i></summary>

**Idea.** Read the genesis time constant from the deposit contract with one call instead of scanning all historical deposit logs at startup.

**Impact.** Lighthouse no longer has eth1 deposit-log scanning; genesis comes from checkpoint/genesis state, so nothing to scan.

**Best measured result.** PR states it is an efficiency increase; no numbers (pr:prysm#1557)

**Evidence (Lighthouse @ 928b61e719).**

- beacon_node/ has no eth1 module (ls: genesis, execution_layer, ...)
- [`beacon_node/genesis/src`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/genesis/src)/{common,interop,lib}.rs - only interop/state genesis

**Sources.** [prysm#1557](https://github.com/OffchainLabs/prysm/pull/1557)

</details>


<a id="el_interaction-147"></a>
<details>
<summary><b>el_interaction-147</b> Drop redundant builder relay status request — <i>implemented · low · S · latency, bandwidth</i></summary>

**Idea.** Remove the builder relay status call from the registration and health path and rely on registerValidators alone, saving one HTTP request per relay.

**Impact.** Status call is not on the registration or health path; nothing left to save.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/builder_client/src/pre_gloas_builder_http_client.rs:406-417`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/builder_client/src/pre_gloas_builder_http_client.rs#L406-L417)

**Skeptic check.** A grep of the whole repo finds get_builder_status only at its definition, with no caller. So no extra status request goes with registrations. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#5518](https://github.com/status-im/nimbus-eth2/pull/5518)

</details>


<a id="el_interaction-148"></a>
<details>
<summary><b>el_interaction-148</b> Ask EL which blobs it holds via hasBlobs — <i>partial · low · M · bandwidth, latency</i></summary>

**Idea.** On block arrival, query engine_hasBlobs to learn which blobs the EL already holds and build sidecars or columns from them instead of refetching from the network.

**Gap in Lighthouse.** Lighthouse has no engine_hasBlobs call: there is no has_blobs method in execution_layer/engine_api. On block arrival, fetch_and_process_blobs_v2_or_v3 and fetch_and_process_blobs_v4 transfer the blob or cell data at once. Lighthouse cannot learn which blobs the EL holds without transferring that data, so it cannot use that knowledge to choose which columns to request from the network. Source PR lighthouse#9546 is an open WIP and its usefulness is disputed.

**Impact.** The main effect (reusing EL blobs instead of fetching them from the network) is already there through getBlobs v2/v3/v4. Only a light-weight availability query is missing, so the gain is small and speculative.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:154-186`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L154-L186)
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:189-240`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L189-L240)
- [`beacon_node/execution_layer/src/lib.rs:1748`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1748)

**Skeptic check.** The earlier evidence called getBlobs the same thing as hasBlobs. getBlobs v3/v4 gives the same reuse of EL blobs, but Lighthouse never calls the hasBlobs probe the idea describes.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lighthouse#9546](https://github.com/sigp/lighthouse/pull/9546)

</details>


<a id="el_interaction-149"></a>
<details>
<summary><b>el_interaction-149</b> Refuse duties and block production when EL is unhealthy — <i>partial · low · S · latency, cpu</i></summary>

**Idea.** When the EL is offline or unsynced, reject validator duty and block-production API requests and poll offline engines on a short timer to detect recovery.

**Gap in Lighthouse.** Only the node-syncing style endpoints report EL-offline; duty and block-production endpoints are not rejected on EL state in the code I read. Add an is_el_offline check to the produce_block and duties handlers.

**Impact.** Avoids useless block production work and wrong proposals when the EL is down; small gain, VC already falls back via syncing status.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs:324`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L324) is_el_offline, used at :2448 and :2506-2518 (syncing endpoint returns not_synced when EL offline)
- [`beacon_node/execution_layer/src/lib.rs:811`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L811) is_offline_or_erroring
- [`beacon_node/execution_layer/src/engines.rs:240`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engines.rs#L240) upcheck (recovery polling)

**Sources.** [lighthouse#2672](https://github.com/sigp/lighthouse/pull/2672)

</details>


<a id="el_interaction-150"></a>
<details>
<summary><b>el_interaction-150</b> Hardcode terminal block hash per known network — <i>n/a · low · startup, latency</i></summary>

**Idea.** Embed the Bellatrix terminal block hash and epoch for known networks so the node never queries the EL to locate the terminal PoW block.

**Impact.** Merge long past; terminal block lookup is not performed by the node, and the hash is a spec config field already.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/core/chain_spec.rs:222-223`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/core/chain_spec.rs#L222-L223) terminal_block_hash fields exist
- mainnet config.yaml:20-21 TERMINAL_BLOCK_HASH zero, activation epoch max
- grep: no get_terminal_pow_block / eth_getBlockByHash caller in non-test code

**Sources.** [teku#8943](https://github.com/Consensys-Incorporated/teku/pull/8943)

</details>


<a id="el_interaction-151"></a>
<details>
<summary><b>el_interaction-151</b> Resolve engine API method by milestone via map — <i>n/a · low · cpu</i></summary>

**Idea.** Look up the engine API method per milestone through a nested map instead of scanning a list on every call.

**Impact.** Lighthouse selects the method via fork-matching and capability booleans, no list scan per call; the cost would be nanoseconds anyway.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engine_api.rs:662-716`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api.rs#L662-L716) capabilities are boolean flags, not a method list scan

**Sources.** [teku#7328](https://github.com/Consensys-Incorporated/teku/pull/7328)

</details>


<a id="el_interaction-152"></a>
<details>
<summary><b>el_interaction-152</b> Parallelize block-by-hash and payload-bodies EL calls — <i>n/a · low · latency</i></summary>

**Idea.** When reconstructing a payload, issue the block-by-hash call and the payload bodies call to the EL concurrently instead of sequentially.

**Impact.** Lighthouse reconstructs payloads from bodies alone (header from stored blinded block), no block-by-hash call to parallelize. Chunks themselves are sequential, which could be a minor S-effort tweak.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_block_streamer.rs:226-245`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_block_streamer.rs#L226-L245) only calls get_payload_bodies_by_hash, sequential chunks
- execution_layer/src/engine_api/http.rs:403 eth_getBlockByHash only via BlockQuery, no non-test caller

**Sources.** [prysm#16687](https://github.com/OffchainLabs/prysm/pull/16687)

</details>


<a id="el_interaction-153"></a>
<details>
<summary><b>el_interaction-153</b> Pass call-trace frames by pointer — <i>n/a · low · cpu, memory</i></summary>

**Idea.** Pass the call-frame struct by pointer when converting call traces, avoiding large struct copies.

**Impact.** Caplin-specific call tracing; Lighthouse has no such code.

**Evidence (Lighthouse @ 928b61e719).**

- No call-trace conversion in [`beacon_node/execution_layer`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer) (grep for trace frames empty)

**Sources.** [caplin#22732](https://github.com/erigontech/erigon/pull/22732)

</details>


<a id="el_interaction-154"></a>
<details>
<summary><b>el_interaction-154</b> Publish EL-built columns to all gossip subnets — <i>not · low · M · bandwidth, latency</i></summary>

**Idea.** After building data columns from the EL blobpool, publish all of them to their subnets, including non-custody ones, so peers receive them sooner and column traffic drops.

**Gap in Lighthouse.** Keep all columns from blobs_to_partial_data_columns, import only custody ones, but pass the non-custody ones to a publish path in compute_custody_columns_to_import / import_custody_partial_columns / the publish_fn closure.

**Impact.** Non-custody columns reach their subnets sooner when this node has the EL blobs; saves some column gossip but costs extra bandwidth and publish work for this node; benefit is small and only for nodes whose EL holds the blobs.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:696-707`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L696-L707) - compute_custody_columns_to_import filters to custody columns only
- [`beacon_node/network/src/network_beacon_processor/mod.rs:1010-1018`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L1010-L1018) - publish_fn only gets custody columns (gradual publish)

**Sources.** [nimbus#8480](https://github.com/status-im/nimbus-eth2/pull/8480)

</details>


<a id="el_interaction-155"></a>
<details>
<summary><b>el_interaction-155</b> Resume deposit log scan from last processed block — <i>n/a · low · sync, startup</i></summary>

**Idea.** Keep eth1 deposit sync progress across EL failures and restarts, resuming from the last processed block instead of refetching and reapplying processed blocks.

**Impact.** Eth1 deposit log scan is gone from this Lighthouse (deposits come from EL requests, EIP-6110), so nothing to resume.

**Evidence (Lighthouse @ 928b61e719).**

- beacon_node (no eth1 crate in listing: beacon_chain, client, execution_layer, ...)
- grep DepositCache only matches [`consensus/state_processing/src/metrics.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/metrics.rs)

**Sources.** [nimbus#3354](https://github.com/status-im/nimbus-eth2/pull/3354), [lodestar@d4787ed5c](https://github.com/ChainSafe/lodestar/commit/d4787ed5c3f9)

</details>


<a id="el_interaction-156"></a>
<details>
<summary><b>el_interaction-156</b> Send builder registrations sequentially for one-per-call builders — <i>n/a · low · latency, cpu</i></summary>

**Idea.** For builders whose API takes one registration per call, send calls sequentially and stop on network error or timeout instead of fanning out, avoiding congestion of the throttled HTTP client.

**Impact.** Builder API register_validator takes an array and Lighthouse sends one batched request, so the one-per-call fan-out issue does not exist.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/validator/mod.rs:813`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L813) - post_builder_validators sends the whole filtered list in one call
- [`beacon_node/builder_client/src/pre_gloas_builder_http_client.rs:244`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/builder_client/src/pre_gloas_builder_http_client.rs#L244) - batch registration endpoint

**Sources.** [teku#5535](https://github.com/Consensys-Incorporated/teku/pull/5535)

</details>


<a id="el_interaction-157"></a>
<details>
<summary><b>el_interaction-157</b> Share one eth1 head block lookup across caches — <i>n/a · low · latency</i></summary>

**Idea.** When updating the deposit log cache and block cache in the same cycle, fetch the eth1 head block number once and pass it to both.

**Impact.** Eth1 deposit/block cache update loop no longer exists, so no head lookup to share.

**Evidence (Lighthouse @ 928b61e719).**

- beacon_node: no eth1 crate; deposit cache and block cache sync removed

**Sources.** [lighthouse#1797](https://github.com/sigp/lighthouse/pull/1797)

</details>


<a id="el_interaction-158"></a>
<details>
<summary><b>el_interaction-158</b> Shrink engine request message slot size — <i>n/a · low · memory</i></summary>

**Idea.** Remove large inline variants from the engine request message so each queue slot is small.

**Impact.** Lighthouse does not use a preallocated message queue of engine request variants; requests are async HTTP calls, so slot size is not a concern.

**Best measured result.** EngineReq shrinks 4,120 to 976 bytes; slot 4,160 to 1,024 (pr:silver#279)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src) (JSON-RPC over HTTP via async calls, no fixed-size engine request queue enum)

**Sources.** [silver#279](https://github.com/gattaca-com/silver/pull/279)

</details>


