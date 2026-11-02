# rpc

45 checked ideas, 10 actionable. [Back to the summary](../README.md).

## Actionable (10)

High or medium value, verdict `not` or `partial`.

<a id="rpc-017"></a>
<details>
<summary><b>rpc-017</b> Serve stored DB bytes without decode, re-encode or recompression — <i>not · medium · L · cpu, latency</i></summary>

**Idea.** When serving blocks (and stored payload bodies) by range/root, send the bytes as stored in the DB, already snappy-compressed if stored that way, straight to the network encoder instead of deserializing, re-serializing and recompressing each object; read only the fields needed. This removes decode/encode CPU per served item.

**Gap in Lighthouse.** No raw-bytes path: add a response variant carrying pre-encoded SSZ (or snappy-framed) bytes and a store getter returning stored bytes; blinded blocks need payload splice and blocks are zstd on disk, so a pure passthrough needs a storage format change. Blobs/columns are stored as plain SSZ and could be passed through more easily.

**Impact.** Removes decode+encode per served item; snappy compression still needed unless stored framed. Moderate CPU win for heavily-queried serving nodes.

**Best measured result.** None (pr:caplin#24220)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/codec.rs:75`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L75) every RpcSuccessResponse variant is encoded with as_ssz_bytes from a decoded object
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1189`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1189) get_blocks streams Arc&lt;SignedBeaconBlock&gt;
- [`beacon_node/store/src/hot_cold_store.rs:96`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L96) block_cache holds decoded blocks only
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1695`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1695) BlobsByRange uses get_blobs (decoded)

**Second check.** Searched the store for any get-bytes-for-RPC path and the RPC codec for a pre-encoded response variant; none exist, all responses encode from decoded types.

**Sources.** [nimbus#3598](https://github.com/status-im/nimbus-eth2/pull/3598), [lodestar#3435](https://github.com/ChainSafe/lodestar/pull/3435), [caplin#24220](https://github.com/erigontech/erigon/pull/24220)

</details>

<a id="rpc-041"></a>
<details>
<summary><b>rpc-041</b> Abort API work once request deadline passes — <i>not · medium · S · cpu, latency</i></summary>

**Idea.** Check request deadline/cancellation before expensive loops in API handlers (state transitions, duties, attestation data) and abort work whose requester is gone; skip optional logging work when disabled.

**Gap in Lighthouse.** When a client disconnects, warp drops only the awaiting future; the work already handed to the beacon processor (or a detached tokio task) still runs, and queued API requests are executed even after the requester is gone. Cheap first step: check tx.is_closed() in the task_spawner closures before calling func (skips stale queued work); deeper cancellation inside state-advance/duties loops would need a token threaded through.

**Impact.** Small on a mainnet node; saves work only for requests whose clients timed out, mostly under API overload when the P0/P1 queues back up.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/task_spawner.rs:61-66`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/task_spawner.rs#L61-L66) (blocking closure runs func() unconditionally; result send ignored if receiver dropped)
- [`beacon_node/http_api/src/task_spawner.rs:131-136`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/task_spawner.rs#L131-L136) (async wrapper awaits func fully, no tx.is_closed()/cancel check)
- [`beacon_node/http_api/src/task_spawner.rs:151`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/task_spawner.rs#L151) (no-processor path uses detached tokio::task::spawn, not cancelled on drop)
- [`beacon_node/beacon_processor/src/lib.rs:1734-1737`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1734-L1737) (queued ApiRequestP0/P1 executed with no staleness or requester-gone check)

**Second check.** Checked the http_api TaskSpawner, the beacon_processor ApiRequest dispatch and warp_utils for any receiver-closed, deadline or cancellation-token logic; none exists, so dropped requests still run to completion. Effort lowered to S because a tx.is_closed() guard in task_spawner would skip stale queued work.

**Sources.** [prysm#2541](https://github.com/OffchainLabs/prysm/pull/2541)

</details>

<a id="rpc-064"></a>
<details>
<summary><b>rpc-064</b> Grow decode buffer as bytes arrive, not upfront — <i>not · medium · S · memory</i></summary>

**Idea.** In the req/resp chunk decoder, grow the output buffer as payload bytes are actually received instead of allocating the full declared length (up to MAX_PAYLOAD_SIZE) upfront, so a bogus length prefix cannot pin memory.

**Gap in Lighthouse.** Full declared length is zero-allocated upfront on every decode attempt (and again after each partial-buffer retry, since the buffer is dropped on UnexpectedEof). The allocation is transient, not pinned across calls, but is up to the per-protocol max for a bogus prefix. Read via take(length).read_to_end into a growing Vec or keep a reusable buffer.

**Impact.** Less allocation churn on partial chunks; robustness against bogus prefixes. Small CPU effect.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/codec.rs:187`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L187) vec![0; length] before read_exact in request decode
- [`beacon_node/lighthouse_network/src/rpc/codec.rs:283`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L283) same in decode_response
- [`beacon_node/lighthouse_network/src/rpc/codec.rs:175`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L175) only bound is ssz limits / max_packet_size
- [`beacon_node/lighthouse_network/src/rpc/codec.rs:444`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L444) handle_error only caps compressed bytes read

**Second check.** Checked all three decode paths (request, response, error) and handle_error; no incremental buffer or reuse of decoded_buffer between retries exists.

**Sources.** [caplin#24648](https://github.com/erigontech/erigon/pull/24648)

</details>

<a id="rpc-082"></a>
<details>
<summary><b>rpc-082</b> Reconstruct pruned column sidecars to serve requests — <i>not · medium · L · disk, cpu</i></summary>

**Idea.** On supernodes, let column by-root/by-range handlers rebuild pruned extension sidecars from archived proofs/data within a configurable retention border, so less storage still serves peers.

**Gap in Lighthouse.** No retention border for extension columns and no serve-time reconstruction; columns are stored whole and pruned by data availability age. Would need partial-column storage plus recomputation (via rust_eth_kzg recovery) in the by-root/by-range handlers.

**Impact.** Storage saving on supernodes at the cost of serve-time CPU; not a CPU win.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2602`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2602) get_data_columns reads only stored column keys
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1857`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1857) serving reads stored columns only

**Second check.** Searched store and rpc_methods for reconstruct/recompute paths; only historic state reconstruction exists, nothing for column sidecars on the serving path.

**Sources.** [teku#10153](https://github.com/Consensys-Incorporated/teku/pull/10153)

</details>

<a id="rpc-023"></a>
<details>
<summary><b>rpc-023</b> Bounded throttling queue between req/resp handlers and storage — <i>partial · medium · S · cpu, memory, disk, latency</i></summary>

**Idea.** Put a bounded queue with a concurrency cap (e.g. max 5 concurrent) between req/resp handlers (blocks, data column by range/root, historical reads) and the database, and reject or drop excess requests. Request bursts then cannot pile up unbounded storage work and memory or starve the critical path.

**Gap in Lighthouse.** Per-peer per-protocol concurrency (2), rate limiting before execution and bounded queues exist, but there is no global cap on concurrent storage-reading RPC jobs: many peers can still occupy all num_cpus workers with by-range reads. A global semaphore (e.g. a few concurrent by-range/by-root jobs) in the beacon processor would close it.

**Impact.** Small to moderate: bounds DB contention under multi-peer floods; per-peer limits already cover single-peer bursts.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/inbound_limiter.rs:126`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/inbound_limiter.rs#L126) rejects a request when the peer already has MAX_CONCURRENT_REQUESTS (2) active on that protocol
- [`beacon_node/lighthouse_network/src/rpc/inbound_limiter.rs:66`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/inbound_limiter.rs#L66) requests are delayed/rejected before execution so no response memory is consumed
- [`beacon_node/lighthouse_network/src/rpc/mod.rs:51`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/mod.rs#L51) MAX_CONCURRENT_REQUESTS = 2
- [`beacon_node/beacon_processor/src/scheduler/work_queue.rs:390`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_queue.rs#L390) bounded RPC queues (1024) drop excess
- [`beacon_node/beacon_processor/src/lib.rs:890`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L890) worker pool capped at num_cpus
- [`beacon_node/beacon_processor/src/lib.rs:1106`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1106) RPC serving drained after consensus work

**Second check.** Found the inbound limiter's per-peer concurrent-request cap and pre-execution rate limiting, which the earlier review missed; they strengthen partial but are per-peer, not a global storage concurrency cap.

**Sources.** [teku#9828](https://github.com/Consensys-Incorporated/teku/pull/9828), [teku#9689](https://github.com/Consensys-Incorporated/teku/pull/9689)

</details>

<a id="rpc-033"></a>
<details>
<summary><b>rpc-033</b> Serve by-range/by-root requests from in-memory pending caches first — <i>partial · medium · M · latency, disk, bandwidth</i></summary>

**Idea.** When serving by-range and by-root requests, look up recent blocks and sidecars in the in-memory availability/pending import and early attester caches before going to the database, so peers can fetch them before import finishes without DB reads.

**Gap in Lighthouse.** By-range (blocks, blobs, columns) only lists imported blocks via fork choice/store and never consults pending-import caches; recent imported blocks do hit the store's decoded-block LRU, so DB reads are partly avoided. Blobs/columns by range have no memory cache.

**Impact.** Small: only matters for peers syncing the very tip.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_block_streamer.rs:171`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_block_streamer.rs#L171) check_caches for by-root block serving
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:235`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L235) BlocksByRoot uses get_blocks_checking_caches
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:698`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L698) BlobsByRoot checks data_availability_checker and early_attester_cache
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:833`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L833) DataColumnsByRoot uses get_data_columns_checking_all_caches
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1201`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1201) by-range get_blocks uses CheckCaches::No
- [`beacon_node/store/src/hot_cold_store.rs:74`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L74) store block_cache LRU serves recently imported blocks from memory for by-range too

**Second check.** Confirmed by-range uses CheckCaches::No and roots come only from imported fork-choice nodes; noted the hot_cold_store block LRU as a partial memory path for by-range blocks that the earlier review did not mention.

**Sources.** [lighthouse#5138](https://github.com/sigp/lighthouse/pull/5138), [teku#7787](https://github.com/Consensys-Incorporated/teku/pull/7787)

</details>

<a id="rpc-071"></a>
<details>
<summary><b>rpc-071</b> Global cross-peer quota applied before decode — <i>partial · medium · M · bandwidth, cpu</i></summary>

**Idea.** Apply req/resp quotas before decoding the request message, and add a global quota for block requests shared by all peers in addition to per-peer quotas, bounding total serving CPU and bandwidth.

**Gap in Lighthouse.** Total serving CPU is bounded globally by the BeaconProcessor's shared bounded queues and worker pool, but there is no global cross-peer token quota for bandwidth, and quotas are checked on the decoded request. Add a shared Limiter key in RPCRateLimiter for BlocksByRange/ByRoot if bandwidth bounding is wanted.

**Impact.** Mostly bandwidth fairness during sync storms; CPU is already globally bounded by the processor.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_queue.rs:390`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_queue.rs#L390) global bounded block_brange_queue/block_broots_queue (1024) shared by all peers
- [`beacon_node/beacon_processor/src/scheduler/work_queue.rs:48`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_queue.rs#L48) FifoQueue::push drops work when full
- [`beacon_node/beacon_processor/src/lib.rs:890`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L890) serving runs on at most max_workers (num_cpus) shared workers
- [`beacon_node/beacon_processor/src/lib.rs:1106`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1106) own-peer/priority ordering over other peers' sync requests
- [`beacon_node/lighthouse_network/src/rpc/rate_limiter.rs:388`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/rate_limiter.rs#L388) token quotas are per PeerId only
- [`beacon_node/lighthouse_network/src/rpc/mod.rs:51`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/mod.rs#L51) MAX_CONCURRENT_REQUESTS per peer per protocol

**Second check.** Reviewer only looked at the rate limiter; the BeaconProcessor's shared bounded RPC queues and fixed worker pool are an equivalent global bound on serving CPU, though not a quota and not pre-decode.

**Sources.** [nimbus#4254](https://github.com/status-im/nimbus-eth2/pull/4254)

</details>

<a id="rpc-075"></a>
<details>
<summary><b>rpc-075</b> Charge rate limiter by blocks actually served — <i>partial · medium · M · sync, bandwidth</i></summary>

**Idea.** Charge the blocks-by-range rate limiter by the number of blocks actually returned, after streaming, instead of a fixed per-request amount, so honest peers making small interleaved requests are not banned.

**Gap in Lighthouse.** Charge scales with the requested count (so small honest requests cost little) and over-quota requests are delayed, which removes the honest-peer-ban problem the idea addressed. Still no refund of tokens for blocks not actually served (skip slots, missing range). Refund in complete_request using the served count.

**Impact.** Minor fairness gain for peers requesting ranges with many skip slots; no CPU effect.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/rate_limiter.rs:393`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/rate_limiter.rs#L393) tokens = request.max_responses (requested count), not a fixed per-request amount
- [`beacon_node/lighthouse_network/src/rpc/inbound_limiter.rs:178`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/inbound_limiter.rs#L178) over-quota requests are delayed (TooSoon), not banned
- [`beacon_node/lighthouse_network/src/rpc/inbound_limiter.rs:200`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/inbound_limiter.rs#L200) complete_request does not refund unused tokens

**Second check.** The Prysm problem was a fixed per-request charge plus banning; Lighthouse already charges proportionally to the requested count and delays instead of banning, so only the post-serve refund part is missing.

**Sources.** [prysm#5853](https://github.com/OffchainLabs/prysm/pull/5853)

</details>

<a id="rpc-076"></a>
<details>
<summary><b>rpc-076</b> Downscore peers requesting too many columns — <i>partial · medium · S · bandwidth</i></summary>

**Idea.** Track data columns served per peer over RPC and downscore peers that request too many, to cap upload bandwidth spent serving columns.

**Gap in Lighthouse.** Per-peer column count is tracked and capped by the inbound rate limiter (bounding upload bandwidth per peer), but abusive requesters are not downscored. Add a PeerAction when a peer repeatedly hits Reject on column protocols.

**Impact.** Bandwidth cap already exists per peer; downscoring would only shed persistent abusers sooner.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/protocol.rs:866`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/protocol.rs#L866) DataColumnsByRange charges count*columns tokens
- [`beacon_node/lighthouse_network/src/rpc/protocol.rs:865`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/protocol.rs#L865) DataColumnsByRoot charges per requested column
- [`beacon_node/lighthouse_network/src/rpc/config.rs:148`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/config.rs#L148) per-peer quota 16384 column sidecars per 10s
- [`beacon_node/lighthouse_network/src/rpc/inbound_limiter.rs:167`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/inbound_limiter.rs#L167) over-quota requests rejected or delayed
- [`beacon_node/lighthouse_network/src/rpc/mod.rs:439`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/mod.rs#L439) rejection sends RateLimited error, no peer score action

**Second check.** Reviewer saw only the handler; the inbound rate limiter counts column sidecars per peer (count * columns) against a dedicated quota, which is the tracking half of the idea.

**Sources.** [prysm#15205](https://github.com/OffchainLabs/prysm/pull/15205)

</details>

<a id="rpc-090"></a>
<details>
<summary><b>rpc-090</b> Await each response write before loading next — <i>partial · medium · L · memory, bandwidth, latency</i></summary>

**Idea.** For multi-chunk responses, wait for the previous chunk write to complete (with a write timeout that closes the stream) before loading the next item from the DB, instead of firing all writes in parallel, so outbound buffers and memory stay bounded.

**Gap in Lighthouse.** The write side already matches Teku's fix: chunks are written one at a time per substream, and a 10s per-chunk timeout closes a stalled stream. What is missing is backpressure on loading: the beacon processor reads every block/column from the DB and queues it into the unbounded pending_items before the peer reads, so memory is not bounded by the write rate. To close it, a bounded per-request channel or a write ack from the handler must gate the DB loader.

**Impact.** Bounds memory held for slow peers on big by-range responses (at most 2 concurrent per peer/protocol, timeout-bounded); a robustness gain with little CPU change.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/handler.rs:471-486`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L471-L486) (Idle substream pops one pending item and starts one send future; never more than one write in flight per substream)
- [`beacon_node/lighthouse_network/src/rpc/handler.rs:526-559`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L526-L559) (next chunk is written only after the previous send future completes)
- [`beacon_node/lighthouse_network/src/rpc/handler.rs:541-545`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L541-L545) (RESP_TIMEOUT reset after each chunk: 'Each chunk is allowed RESPONSE_TIMEOUT to be sent')
- [`beacon_node/lighthouse_network/src/rpc/handler.rs:414-436`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L414-L436) (expired per-chunk timeout removes the substream with StreamTimeout)
- [`beacon_node/lighthouse_network/src/rpc/mod.rs:51`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/mod.rs#L51) + inbound_limiter.rs (MAX_CONCURRENT_REQUESTS=2 per peer/protocol bounds concurrent responses)
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1840-1870`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1840-L1870) (loader still reads all items from DB and pushes them without waiting on writes)
- [`beacon_node/lighthouse_network/src/rpc/handler.rs:169`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L169),337 (unbounded pending_items VecDeque)

**Second check.** The earlier review called RESP_TIMEOUT only an overall stream timeout. The handler resets it per chunk and serialises writes per substream, so the 'await previous write plus write timeout' half exists. Only the load-gating half is missing.

**Sources.** [teku#2486](https://github.com/Consensys-Incorporated/teku/pull/2486), [teku#10949](https://github.com/Consensys-Incorporated/teku/pull/10949)

</details>

## Other checked ideas (35)

Implemented, not applicable, or low value.

<a id="rpc-002"></a>
<details>
<summary><b>rpc-002</b> O(1) custody index for serving data column requests — <i>not · low · S · cpu</i></summary>

**Idea.** When serving data column requests, test custody of each column against a precomputed O(1) index (bytemap/bitset) and split available/missing in one pass. This replaces repeated linear array scans per requested column.

**Gap in Lighthouse.** Custody check is a linear scan of a slice of up to 128 indices per requested column. Build a bitset/bool array (or sorted slice binary search) in CustodyContext and use it in handle_data_columns_by_root_request_inner and handle_data_columns_by_range_request_inner.

**Impact.** Saves at most ~16k comparisons per request on a supernode; negligible versus the DB reads that follow.

**Best measured result.** None (pr:lodestar#9457)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:823-831`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L823-L831) (by root: available_columns.contains(c) on a slice)
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1844-1851`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1844-L1851) (by range: same slice contains)
- [`beacon_node/beacon_chain/src/custody_context.rs:525-537`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L525-L537) (custody_columns_for_epoch returns &amp;[ColumnIndex])

**Sources.** [lodestar#9457](https://github.com/ChainSafe/lodestar/pull/9457)

</details>

<a id="rpc-043"></a>
<details>
<summary><b>rpc-043</b> Deduplicate by-root request roots and stream in batches — <i>not · low · S · cpu, latency</i></summary>

**Idea.** In by-root block/envelope handlers, deduplicate requested roots before lookup and reconstruct/stream results in small batches, so duplicate roots are not reconstructed repeatedly and the first chunks go out early.

**Gap in Lighthouse.** In handle_blocks_by_root_request_inner and handle_payload_envelopes_by_root_request_inner (and the data-columns variant), dedup the root list (order-preserving) before calling get_blocks_checking_caches / get_payload_envelopes. Streaming already happens per item via the stream.

**Impact.** A peer repeating one root up to the request cap repeats block loading/payload reconstruction; dedup bounds the abuse cost. Rate limiter charges per requested root, so exposure is limited; real mainnet savings are small.

**Best measured result.** None (pr:lodestar#10207)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:217-247`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L217-L247) BlocksByRoot passes request.block_roots().to_vec() straight to get_blocks_checking_caches with no dedup
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:581-600`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L581-L600) envelopes by root same
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1173-1185`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1173-L1185) streamer launch_stream(block_roots)

**Sources.** [lodestar#10207](https://github.com/ChainSafe/lodestar/pull/10207)

</details>

<a id="rpc-070"></a>
<details>
<summary><b>rpc-070</b> Reuse snappy encoder/decoder objects — <i>not · low · M · memory, cpu</i></summary>

**Idea.** Reuse snappy encoder and decoder objects per stream or from a pool instead of constructing a new (~64-100 kB) codec for each RPC message or chunk, cutting allocations and an allocation DoS vector.

**Gap in Lighthouse.** Encoders/decoders are built per message; snap frame codecs allocate internal buffers each time. Keep a reusable encoder/decoder per codec (or use snap::raw with reusable Encoder/Decoder) in SSZSnappyInboundCodec/OutboundCodec encode/decode_response.

**Impact.** Fewer allocations per RPC message (~64-100 kB each in the other client); on Lighthouse likely small CPU/alloc win during sync with many chunks.

**Best measured result.** None (pr:prysm#6085)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/codec.rs:127`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L127) FrameEncoder::new(Vec::new()) per message
- [`beacon_node/lighthouse_network/src/rpc/codec.rs:187`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L187) FrameDecoder::new per decode, plus vec![0; length] buffer
- [`beacon_node/lighthouse_network/src/rpc/codec.rs:281`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L281),318,389 same

**Sources.** [silver#139](https://github.com/gattaca-com/silver/pull/139), [prysm#6085](https://github.com/OffchainLabs/prysm/pull/6085), [silver#215](https://github.com/gattaca-com/silver/pull/215)

</details>

<a id="rpc-007"></a>
<details>
<summary><b>rpc-007</b> Use a faster native snappy codec for RPC — <i>partial · low · S · cpu, latency</i></summary>

**Idea.** Swap the snappy framed codec used for ssz_snappy req/resp payloads for a faster native (or WASM) implementation writing into a preallocated buffer, optionally behind a flag. Encoding and decoding is CPU on every req/resp chunk.

**Gap in Lighthouse.** Codec is already the native Rust snap crate (1.1.2), so there is no JS-to-native swap to make. Missing: per-message encoder and Vec allocation, and a decode buffer; encode_response could reuse a codec-owned buffer or use snap::raw::Encoder directly with max_compress_len preallocation.

**Impact.** Small CPU/alloc saving on every req/resp chunk; only visible when serving many blocks/columns, likely a few percent of that path.

**Best measured result.** None (pr:lodestar#10062)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/codec.rs:8-9`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L8-L9),127-135 (native Rust snap FrameEncoder::new(Vec::new()) per message)
- [`beacon_node/lighthouse_network/src/rpc/codec.rs:183-190`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L183-L190) (FrameDecoder with vec![0; length] per message)

**Sources.** [teku#10918](https://github.com/Consensys-Incorporated/teku/pull/10918), [lodestar#10062](https://github.com/ChainSafe/lodestar/pull/10062)

</details>

<a id="rpc-025"></a>
<details>
<summary><b>rpc-025</b> Bulk hardware CRC32C for snappy frame checksums — <i>partial · low · M · cpu, latency</i></summary>

**Idea.** Compute snappy frame CRC32C checksums with a native, hardware-accelerated bulk implementation over whole buffers, without per-byte updates or intermediate buffer copies.

**Gap in Lighthouse.** On x86_64 the snap crate already does hardware bulk CRC32C; on aarch64 it falls back to software slice-by-16. Would need a custom frame codec using a crc32c crate with ARM CRC intrinsics.

**Impact.** Only matters on ARM nodes; on x86 mainnet nodes it is already fast. Saves milliseconds per MB of large block/blob chunks.

**Best measured result.** None (pr:teku#11593)

**Evidence (Lighthouse @ 928b61e719).**

- snap-1.1.2/src/crc32.rs:47-61 crc32c uses SSE4.2 on x86_64 with runtime detection, slice16 fallback elsewhere
- [`beacon_node/lighthouse_network/src/rpc/codec.rs:187`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L187) FrameDecoder from snap crate

**Sources.** [teku#11593](https://github.com/Consensys-Incorporated/teku/pull/11593), [lodestar#7406](https://github.com/ChainSafe/lodestar/pull/7406)

</details>

<a id="rpc-051"></a>
<details>
<summary><b>rpc-051</b> Slot-only lookups in sidecar by-root handlers, no full block — <i>partial · low · S · disk, latency</i></summary>

**Idea.** In blob and data column by-root RPC handlers, resolve the block slot with a slot-only index lookup (once per root, cached) or the finalized block slot instead of loading the full signed block, and skip the non-canonical sidecar fallback lookup.

**Gap in Lighthouse.** On a cache miss get_data_columns_checking_all_caches loads a full blinded block per root only to read the fork; replace with a slot/fork-only lookup (or finalized-slot shortcut) in the store, and cache it per root in the blobs handler.

**Impact.** Cheaper disk reads on by-root sidecar serving during lookups; small, only matters under heavy by-root load.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:1243`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1243) data-column by-root cache miss calls get_blinded_block just to get fork name
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:689`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L689) blobs by-root resolves slot only from DA/early-attester caches
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:816`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L816) columns handler no slot lookup

**Sources.** [teku#10486](https://github.com/Consensys-Incorporated/teku/pull/10486), [teku#10444](https://github.com/Consensys-Incorporated/teku/pull/10444), [teku#10485](https://github.com/Consensys-Incorporated/teku/pull/10485)

</details>

<a id="rpc-056"></a>
<details>
<summary><b>rpc-056</b> Expire stale requests in outbound self rate limiter — <i>partial · low · S · sync</i></summary>

**Idea.** Track request ids in the outbound self rate limiter and expire entries older than a timeout, so dead requests do not hold quota and slow sync.

**Gap in Lighthouse.** Delayed requests in SelfRateLimiter never expire; add a max age check in poll_ready/next_peer_request_ready dropping entries older than a timeout and reporting failure. Active slots are already freed by handler timeouts.

**Impact.** Avoids stale queued requests blocking sync after peer stalls; minor.

**Best measured result.** None (pr:lodestar#8295)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/self_limiter.rs:27`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/self_limiter.rs#L27) queued_at only used for metrics (line 309)
- [`beacon_node/lighthouse_network/src/rpc/mod.rs:498`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/mod.rs#L498) request_completed on handler failure releases active count
- self_limiter.rs delayed_requests/ready_requests have no timeout

**Sources.** [lodestar#8295](https://github.com/ChainSafe/lodestar/pull/8295)

</details>

<a id="rpc-008"></a>
<details>
<summary><b>rpc-008</b> Close or reset req/resp streams promptly on every path — <i>implemented · medium · memory, latency</i></summary>

**Idea.** Close or reset the libp2p req/resp stream as soon as the exchange finishes and on every error path (with correct error codes), so streams and their per-stream buffers are released promptly instead of leaking.

**Gap in Lighthouse.** 

**Impact.** Already closes on completion, error, timeout and shutdown; nothing further to gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/handler.rs:466`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L466) inbound substreams driven, closed on last chunk (send_message_to_inbound_substream last_chunk)
- [`beacon_node/lighthouse_network/src/rpc/handler.rs:555`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L555) stream removed and timeout deleted when closed
- [`beacon_node/lighthouse_network/src/rpc/handler.rs:620`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L620) send error removes substream and reports error
- [`beacon_node/lighthouse_network/src/rpc/handler.rs:492`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L492) deactivated handler closes all streams
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:216`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L216) terminate_response_stream sends error code plus terminator on every Err path

**Sources.** [lodestar@14e40c04f](https://github.com/ChainSafe/lodestar/commit/14e40c04f580), [lodestar@cf39face7](https://github.com/ChainSafe/lodestar/commit/cf39face7e81), [caplin#7582](https://github.com/erigontech/erigon/pull/7582), [prysm#6481](https://github.com/OffchainLabs/prysm/pull/6481)

</details>

<a id="rpc-011"></a>
<details>
<summary><b>rpc-011</b> Serve API head queries from in-memory chain head — <i>implemented · medium · cpu, disk</i></summary>

**Idea.** Answer validator/API calls that need the head block, root or state from the chain's in-memory head instead of reading them from the database on each request.

**Gap in Lighthouse.** 

**Impact.** Head queries already skip the DB.

**Best measured result.** None (pr:prysm#4752)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/state_id.rs:29`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L29) StateId Head root from canonical_head.head_and_execution_status (in memory)
- [`beacon_node/http_api/src/state_id.rs:179`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L179) head state cloned from cached_head.snapshot.beacon_state
- [`beacon_node/http_api/src/block_id.rs:48`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L48) head block root from cached head
- [`beacon_node/http_api/src/block_id.rs:182`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L182) head blinded block from cached_head.snapshot.beacon_block

**Sources.** [prysm#4752](https://github.com/OffchainLabs/prysm/pull/4752), [prysm#3309](https://github.com/OffchainLabs/prysm/pull/3309)

</details>

<a id="rpc-013"></a>
<details>
<summary><b>rpc-013</b> Read only blocks in requested by-range span and step — <i>implemented · medium · S · disk, latency, cpu, bandwidth</i></summary>

**Idea.** In blocks-by-range serving, read from the DB only the blocks inside the requested start/count/step span, applying the step in the DB query and not reading an extra step past the end, instead of loading all blocks in range and discarding.

**Gap in Lighthouse.** 

**Impact.** None left: Lighthouse already reads only the requested span by root and step no longer exists in the protocol.

**Best measured result.** None (pr:prysm#4488)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1233`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1233) get_block_roots_for_slot_range resolves only roots in [start, start+count)
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1351`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1351) store path take_while(slot &lt; start+count), no read past the end
- [`beacon_node/beacon_chain/src/beacon_chain.rs:8427`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L8427) block_roots_from_fork_choice filters start&lt;=slot&lt;end and breaks below start
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1161`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1161) get_blocks loads only those roots
- [`beacon_node/lighthouse_network/src/rpc/methods.rs:470`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/methods.rs#L470) step dropped on decode (deprecated in spec, treated as 1)

**Second check.** The earlier gap itself said nothing is left to change; I confirmed both root paths (store iterator and fork choice) stop at start+count and that step is discarded at decode, so the verdict is implemented, not partial.

**Sources.** [prysm#4046](https://github.com/OffchainLabs/prysm/pull/4046), [prysm#4488](https://github.com/OffchainLabs/prysm/pull/4488)

</details>

<a id="rpc-030"></a>
<details>
<summary><b>rpc-030</b> Validate and cap by-range request counts before DB reads — <i>implemented · medium · bandwidth, cpu, disk</i></summary>

**Idea.** Validate and clamp blocks/blobs/columns by-range and by-root request counts (and column counts) to spec maxima and the available range before any DB reads, and stop the read loop at the cap. A single request then cannot force unbounded reads and responses.

**Gap in Lighthouse.** 

**Impact.** Requests are rejected or clamped before any DB read; blocks-by-range relies on the rate limiter TooLarge rather than an explicit handler check, with the same effect.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/rate_limiter.rs:388`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/rate_limiter.rs#L388) allows() charges request.max_responses tokens before any processing
- [`beacon_node/lighthouse_network/src/rpc/rate_limiter.rs:526`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/rate_limiter.rs#L526) TooLarge returned when count exceeds bucket (128 per 10s for BlocksByRange)
- [`beacon_node/lighthouse_network/src/rpc/config.rs:128`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/config.rs#L128) DEFAULT_BLOCKS_BY_RANGE_QUOTA 128/10s
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1617`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1617) blobs by range max_blobs_requested checked before roots/DB
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1779`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1779) data columns by range max_requested checked before DB reads
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:329`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L329) by-head cap at MAX_REQUEST_BLOCKS_DENEB
- [`beacon_node/lighthouse_network/src/rpc/codec.rs:543`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L543) by-root list lengths bounded at decode

**Sources.** [teku#2309](https://github.com/Consensys-Incorporated/teku/pull/2309), [nimbus#915](https://github.com/status-im/nimbus-eth2/pull/915), [nimbus#7594](https://github.com/status-im/nimbus-eth2/pull/7594), [teku#9085](https://github.com/Consensys-Incorporated/teku/pull/9085), [nimbus#8958](https://github.com/status-im/nimbus-eth2/pull/8958)

</details>

<a id="rpc-034"></a>
<details>
<summary><b>rpc-034</b> Stream by-range/by-root responses chunk by chunk from DB — <i>implemented · medium · S · latency, memory, sync</i></summary>

**Idea.** Serve blocks by range/root by streaming items from the DB iterator to the network encoder and writing each as a separate chunk as it is produced, instead of collecting the whole response in memory first. This bounds memory and lets the first chunk go out early.

**Gap in Lighthouse.** 

**Impact.** None, already done.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1161`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1161) blocks stream consumed with next().await, one SendResponse per block
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1201`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1201) get_blocks returns BeaconBlockStreamer stream

**Sources.** [prysm#3528](https://github.com/OffchainLabs/prysm/pull/3528), [lodestar#622](https://github.com/ChainSafe/lodestar/pull/622), [lodestar@c03541065](https://github.com/ChainSafe/lodestar/commit/c03541065648), [lodestar#684](https://github.com/ChainSafe/lodestar/pull/684), [lodestar@c7978049f](https://github.com/ChainSafe/lodestar/commit/c7978049f2a6)

</details>

<a id="rpc-038"></a>
<details>
<summary><b>rpc-038</b> Outbound self rate limiter capping concurrent requests per peer — <i>implemented · medium · S · bandwidth, latency, sync</i></summary>

**Idea.** Queue or fail locally outgoing RPC requests to a peer, per protocol (e.g. max 2 concurrent in flight), so they stay under the peer's inbound limits. Peers are not flooded, slow responses do not pile up, and rejected requests need no retry.

**Gap in Lighthouse.** 

**Impact.** None, already done.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/mod.rs:51`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/mod.rs#L51) MAX_CONCURRENT_REQUESTS=2
- [`beacon_node/lighthouse_network/src/rpc/self_limiter.rs:134`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/self_limiter.rs#L134) queues requests at the limit

**Sources.** [teku#8912](https://github.com/Consensys-Incorporated/teku/pull/8912), [lighthouse@493784366](https://github.com/sigp/lighthouse/commit/493784366f3d), [lodestar#8185](https://github.com/ChainSafe/lodestar/pull/8185)

</details>

<a id="rpc-040"></a>
<details>
<summary><b>rpc-040</b> Run sync-response DB reads on blocking threads — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Run database reads for blocks-by-range/root responses on blocking worker threads off the core async executor, so large responses run in parallel and do not stall networking.

**Gap in Lighthouse.** 

**Impact.** None, already done.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1127`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1127) spawn_blocking_handle for root lookup
- [`beacon_node/beacon_chain/src/beacon_block_streamer.rs:260`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_block_streamer.rs#L260) block loads via spawn_blocking_handle

**Sources.** [lighthouse#1909](https://github.com/sigp/lighthouse/pull/1909)

</details>

<a id="rpc-049"></a>
<details>
<summary><b>rpc-049</b> Refuse validator API requests while node is syncing — <i>implemented · medium · S · cpu, sync</i></summary>

**Idea.** Do not serve duty and state validator API requests while the node is syncing, so they do not compete with sync for CPU.

**Gap in Lighthouse.** 

**Impact.** None, already done.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/validator/mod.rs:78`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L78) not_while_syncing_filter on duties and validator endpoints

**Sources.** [prysm#2353](https://github.com/OffchainLabs/prysm/pull/2353)

</details>

<a id="rpc-055"></a>
<details>
<summary><b>rpc-055</b> Free every per-peer rate limiter state for disconnected peers — <i>implemented · medium · S · memory</i></summary>

**Idea.** Remove a peer's RPC rate-limiter buckets on disconnect, and prune every per-protocol limiter (including light-client protocols) on a timer, so entries for disconnected peers do not live for the node's lifetime.

**Gap in Lighthouse.** 

**Impact.** None, already done.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/rate_limiter.rs:425`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/rate_limiter.rs#L425) prune() covers all protocols incl. light client
- [`beacon_node/lighthouse_network/src/rpc/rate_limiter.rs:475`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/rate_limiter.rs#L475) 30s prune timer
- [`beacon_node/lighthouse_network/src/rpc/self_limiter.rs:233`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/self_limiter.rs#L233) peer_disconnected

**Sources.** [prysm#16916](https://github.com/OffchainLabs/prysm/pull/16916), [lighthouse#8058](https://github.com/sigp/lighthouse/pull/8058)

</details>

<a id="rpc-058"></a>
<details>
<summary><b>rpc-058</b> Filter column requests to custody columns before DB — <i>implemented · medium · S · disk, cpu, bandwidth</i></summary>

**Idea.** Filter DataColumnsByRoot/ByRange requests to the columns the node custodies before hitting the database, so requests for non-custodied columns do not cause lookups that always miss.

**Gap in Lighthouse.** 

**Impact.** None, already done.

**Best measured result.** None (pr:lighthouse#7897)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:824`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L824) by-root filters to custody columns
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1840`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1840) by-range filters before get_data_column

**Sources.** [lighthouse#7897](https://github.com/sigp/lighthouse/pull/7897), [grandine@31108d74e](https://github.com/grandinetech/grandine/commit/31108d74e0a3)

</details>

<a id="rpc-060"></a>
<details>
<summary><b>rpc-060</b> Half-close request stream after sending request — <i>implemented · medium · S · sync, latency</i></summary>

**Idea.** After writing an RPC request, half-close the write side of the stream as the spec requires so the responder starts processing at once, and use per-chunk response timeouts instead of one total timeout.

**Gap in Lighthouse.** 

**Impact.** None, already done.

**Best measured result.** None (pr:nimbus#1621)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/outbound.rs:65`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/outbound.rs#L65) send request then socket.close()
- [`beacon_node/lighthouse_network/src/rpc/handler.rs:711`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L711) RESP_TIMEOUT reset per chunk

**Sources.** [nimbus#1621](https://github.com/status-im/nimbus-eth2/pull/1621)

</details>

<a id="rpc-061"></a>
<details>
<summary><b>rpc-061</b> Compute by-range block roots by hashing loaded blocks — <i>implemented · medium · disk, latency</i></summary>

**Idea.** When serving blocks-by-range, derive each block root by hashing the blocks already loaded instead of looking each root up in the DB. DB root lookups are slow during non-finality.

**Gap in Lighthouse.** 

**Impact.** Roots come from fork choice or the forward block-root iterator, not per-slot DB lookups; hashing blocks would cost more.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1106`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1106) blocks-by-range inner
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1141`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1141) get_block_roots_for_slot_range
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1237`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1237) roots from fork choice or store iterator

**Sources.** [prysm#7028](https://github.com/OffchainLabs/prysm/pull/7028)

</details>

<a id="rpc-066"></a>
<details>
<summary><b>rpc-066</b> Interleave response chunks across concurrent substreams — <i>implemented · medium · latency</i></summary>

**Idea.** In the RPC handler, interleave sending chunks of responses across concurrent inbound substreams instead of sending each response fully in sequence, so long responses do not cause other streams to time out under load.

**Gap in Lighthouse.** 

**Impact.** Each poll services every inbound substream one message at a time, so long responses do not starve others.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/handler.rs:465`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L465) loop over all inbound_substreams each poll
- [`beacon_node/lighthouse_network/src/rpc/handler.rs:476`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L476) one pending item popped per idle substream

**Sources.** [lighthouse#2815](https://github.com/sigp/lighthouse/pull/2815)

</details>

<a id="rpc-067"></a>
<details>
<summary><b>rpc-067</b> BlobSidecarsByRange: iterate only indices with commitments — <i>implemented · medium · S · disk, cpu, latency</i></summary>

**Idea.** When serving BlobSidecarsByRange, use each block's KZG commitment count to read only the blob indices that exist, instead of probing every possible blob index per slot in the DB.

**Gap in Lighthouse.** Idea's waste (probing each possible blob index per slot) cannot occur: Lighthouse stores blobs per block root as a single list. Residual is one blobs-DB miss per block with zero commitments; could be skipped via the block's commitment count, but that is a different, small optimisation.

**Impact.** None for the stated idea; the residual empty-block miss is negligible.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2616`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2616) get_blobs reads all blobs of a block from one BeaconBlob key
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1694`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1694) BlobsByRange loops once per block root, iterating only the stored sidecars

**Second check.** Confirmed storage schema is one key per block root (not per index) and the range handler only iterates stored sidecars, so the per-index probing Teku fixed has no Lighthouse counterpart.

**Sources.** [teku#6949](https://github.com/Consensys-Incorporated/teku/pull/6949)

</details>

<a id="rpc-001"></a>
<details>
<summary><b>rpc-001</b> Per-peer per-protocol inbound rate limits on requests and objects — <i>implemented · low · S · cpu, bandwidth, latency, disk</i></summary>

**Idea.** Rate limit inbound req/resp per peer and per protocol with a continuously refilling token bucket (GCRA) in the RPC behaviour, counting both requests and storage-backed objects (blocks, blobs, columns) per window, enabled by default. Violators are rejected, penalized or disconnected, so one peer cannot force unbounded DB reads, CPU or bandwidth, and serving load is spread evenly.

**Gap in Lighthouse.** 

**Impact.** Already present; no change.

**Best measured result.** None (pr:nimbus#7952)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/rate_limiter.rs:24`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/rate_limiter.rs#L24),388-405 (GCRA Limiter, tokens = max_responses so objects counted, per peer per protocol)
- [`beacon_node/lighthouse_network/src/rpc/rate_limiter.rs:485-515`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/rate_limiter.rs#L485-L515) (Limiter TAT GCRA)
- [`beacon_node/lighthouse_network/src/rpc/inbound_limiter.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/inbound_limiter.rs) (inbound limiter)
- [`beacon_node/src/config.rs:1524`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/config.rs#L1524) (enabled by default unless disable-inbound-rate-limiter)

**Sources.** [lighthouse#1402](https://github.com/sigp/lighthouse/pull/1402), [grandine@dc0d3e071](https://github.com/grandinetech/grandine/commit/dc0d3e071010), [nimbus#7952](https://github.com/status-im/nimbus-eth2/pull/7952), [teku#9841](https://github.com/Consensys-Incorporated/teku/pull/9841), [teku#2488](https://github.com/Consensys-Incorporated/teku/pull/2488), [caplin#8868](https://github.com/erigontech/erigon/pull/8868), [teku#2500](https://github.com/Consensys-Incorporated/teku/pull/2500), [prysm#17504](https://github.com/OffchainLabs/prysm/pull/17504), [lodestar#3454](https://github.com/ChainSafe/lodestar/pull/3454)

</details>

<a id="rpc-006"></a>
<details>
<summary><b>rpc-006</b> Allocation-free shared varint encoder for req/resp length prefixes — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** Encode and decode the LEB128 varint length prefix and response prefix of every req/resp (and gossip) message with one shared fast implementation that writes into a stack or preallocated buffer, without a heap allocation per message. This cuts allocations and CPU on every message.

**Gap in Lighthouse.** 

**Impact.** Varint is already a shared allocation-free codec; remaining per-message allocations are the ssz Vec and snappy Vec (see rpc-007), not the varint.

**Best measured result.** None (commit:nimbus@4e191a06ac07)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/codec.rs:46`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L46),142-145 (unsigned_varint Uvi encodes into dst, no heap allocation)
- beacon_node/unsigned-varint-0.8.0/src/codec.rs:51-57 (serialise uses stack buffer)
- [`beacon_node/lighthouse_network/src/rpc/codec.rs:496-504`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L496-L504) (shared decode helper using Uvi)

**Sources.** [nimbus@4e191a06a](https://github.com/status-im/nimbus-eth2/commit/4e191a06ac07), [lodestar#5895](https://github.com/ChainSafe/lodestar/pull/5895), [nimbus#2182](https://github.com/status-im/nimbus-eth2/pull/2182), [caplin#18961](https://github.com/erigontech/erigon/pull/18961)

</details>

<a id="rpc-012"></a>
<details>
<summary><b>rpc-012</b> Answer Status from fork choice, no state or DB reads — <i>implemented · low · S · cpu, latency, disk</i></summary>

**Idea.** When handling an inbound or outbound Status message (and checking peer relevance), take head root/slot, finalized checkpoint and 'is this root finalized' from in-memory fork choice or the cached head instead of loading the head state or calling block_root_at_slot. block_root_at_slot iterates states and is very slow without finality.

**Gap in Lighthouse.** 

**Impact.** Already avoids state loads; only a freezer block_root_at_slot for peers with old finality.

**Best measured result.** None (pr:lodestar#902)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/status.rs:21-52`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/status.rs#L21-L52) (status_message from cached_head, in-memory data_column_custody_info_cache and anchor info)
- [`beacon_node/store/src/hot_cold_store.rs:2592-2594`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2592-L2594) (custody info from RwLock cache)
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:100-160`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L100-L160) (check_peer_relevance compares checkpoints, DB lookup only for finalized below split, otherwise none)

**Sources.** [lighthouse#5481](https://github.com/sigp/lighthouse/pull/5481), [prysm#10978](https://github.com/OffchainLabs/prysm/pull/10978), [lighthouse#7056](https://github.com/sigp/lighthouse/pull/7056), [lighthouse#7054](https://github.com/sigp/lighthouse/pull/7054), [lighthouse#7082](https://github.com/sigp/lighthouse/pull/7082), [lodestar@e0f646dd6](https://github.com/ChainSafe/lodestar/commit/e0f646dd6738), [lodestar#902](https://github.com/ChainSafe/lodestar/pull/902)

</details>

<a id="rpc-020"></a>
<details>
<summary><b>rpc-020</b> Resolve unfinalized by-range roots from fork choice in one walk — <i>implemented · low · S · cpu, disk, latency</i></summary>

**Idea.** When serving by-range requests, take block roots for unfinalized slots from the fork choice proto-array in one backwards walk over the whole range, and only finalized roots from the store. This avoids per-slot store lookups and state loads or regeneration during long non-finality.

**Gap in Lighthouse.** 

**Impact.** Already done; no change.

**Best measured result.** None (pr:teku#2156)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1250-1296`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1250-L1296) (get_block_roots_for_slot_range splits at finalized slot)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:8427-8453`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L8427-L8453) (block_roots_from_fork_choice: one proto_array iter_block_roots walk from head)
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1320`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1320) (store forwards_iter_block_roots for finalized part)

**Sources.** [teku#2156](https://github.com/Consensys-Incorporated/teku/pull/2156), [lighthouse#7058](https://github.com/sigp/lighthouse/pull/7058), [lighthouse#7098](https://github.com/sigp/lighthouse/pull/7098), [lighthouse#7066](https://github.com/sigp/lighthouse/pull/7066), [teku#2166](https://github.com/Consensys-Incorporated/teku/pull/2166)

</details>

<a id="rpc-021"></a>
<details>
<summary><b>rpc-021</b> Cap received response chunks by requested item count — <i>implemented · low · bandwidth, cpu, memory</i></summary>

**Idea.** For each outgoing request, compute the maximum expected response chunks from the request (number of roots or count) and tight sizes for fixed-size messages, and reject or close the stream as soon as a peer sends more, instead of reading and decoding the surplus.

**Gap in Lighthouse.** 

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/handler.rs:987`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L987) max_responses computed per outbound request
- [`beacon_node/lighthouse_network/src/rpc/handler.rs:695-710`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L695-L710) max_remaining_chunks decremented, stream closed at 0
- [`beacon_node/lighthouse_network/src/rpc/protocol.rs:854`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/protocol.rs#L854) RequestType::max_responses

**Sources.** [teku#1030](https://github.com/Consensys-Incorporated/teku/pull/1030), [nimbus#6961](https://github.com/status-im/nimbus-eth2/pull/6961), [nimbus#6954](https://github.com/status-im/nimbus-eth2/pull/6954), [nimbus#4264](https://github.com/status-im/nimbus-eth2/pull/4264)

</details>

<a id="rpc-022"></a>
<details>
<summary><b>rpc-022</b> Bound length prefix by per-type SSZ limits before decompressing — <i>implemented · low · memory, bandwidth, cpu</i></summary>

**Idea.** Precompute min/max SSZ encoded size per RPC message type, reject a chunk whose declared length is outside that range, and wrap the snappy decoder in a reader limited to max_compressed_len(declared length). Bad, padded or compression-bomb payloads are rejected before reading or allocating for them.

**Gap in Lighthouse.** 

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/codec.rs:171-186`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L171-L186) is_out_of_bounds check on length before decode, Take(max_compress_len)
- [`beacon_node/lighthouse_network/src/rpc/codec.rs:268-281`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L268-L281) same for responses
- [`beacon_node/lighthouse_network/src/rpc/protocol.rs:30-126`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/protocol.rs#L30-L126) LazyLock min/max SSZ sizes

**Sources.** [prysm#7445](https://github.com/OffchainLabs/prysm/pull/7445), [nimbus@3433c77c3](https://github.com/status-im/nimbus-eth2/commit/3433c77c35f3), [teku#2360](https://github.com/Consensys-Incorporated/teku/pull/2360), [lighthouse#1738](https://github.com/sigp/lighthouse/pull/1738), [prysm#7479](https://github.com/OffchainLabs/prysm/pull/7479), [caplin#25079](https://github.com/erigontech/erigon/pull/25079), [prysm#17660](https://github.com/OffchainLabs/prysm/pull/17660), [lighthouse#1250](https://github.com/sigp/lighthouse/pull/1250)

</details>

<a id="rpc-027"></a>
<details>
<summary><b>rpc-027</b> Compute RPC protocol size limits once statically — <i>implemented · low · cpu</i></summary>

**Idea.** Compute the constant per-protocol RPC size limits once in a lazily initialised static instead of recomputing them on every encode/decode call.

**Gap in Lighthouse.** 

**Best measured result.** None (pr:lighthouse#6595)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/protocol.rs:30-126`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/protocol.rs#L30-L126) pub static LazyLock size limits
- [`beacon_node/lighthouse_network/src/rpc/protocol.rs:138`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/protocol.rs#L138) rpc_block_limits_by_fork uses the statics

**Sources.** [lighthouse#6595](https://github.com/sigp/lighthouse/pull/6595)

</details>

<a id="rpc-032"></a>
<details>
<summary><b>rpc-032</b> Lower rate-limit quota cost for blob sidecars — <i>implemented · low · bandwidth</i></summary>

**Idea.** Charge blob sidecars a much smaller inbound rate-limit quota cost than full blocks, so serving syncing peers is not throttled by blob count.

**Gap in Lighthouse.** 

**Best measured result.** None (pr:nimbus#6120)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/rate_limiter.rs:104-113`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/rate_limiter.rs#L104-L113) separate limiter per protocol (blobs vs blocks)
- [`beacon_node/lighthouse_network/src/rpc/rate_limiter.rs:391-397`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/rate_limiter.rs#L391-L397) tokens = request.max_responses (blob count)
- [`beacon_node/lighthouse_network/src/rpc/config.rs:74-75`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/config.rs#L74-L75) blobs quotas 1152 per 13s

**Sources.** [nimbus#6120](https://github.com/status-im/nimbus-eth2/pull/6120)

</details>

<a id="rpc-035"></a>
<details>
<summary><b>rpc-035</b> Clear request timeout timers and abort listeners on completion — <i>implemented · low · memory, latency, cpu</i></summary>

**Idea.** Remove the request/response timeout timer and abort-signal/cancellation listeners as soon as the response stream completes or is aborted. Otherwise finished requests are later reported as timeouts and timers/closures accumulate per request.

**Gap in Lighthouse.** 

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/handler.rs:745`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L745),774,793 outbound_substreams_delay.remove on completion/abort
- [`beacon_node/lighthouse_network/src/rpc/handler.rs:500`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L500),574,608 inbound_substreams_delay.remove
- [`beacon_node/lighthouse_network/src/rpc/handler.rs:414-446`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L414-L446) expired substreams purged

**Sources.** [lighthouse#2804](https://github.com/sigp/lighthouse/pull/2804), [lodestar#9029](https://github.com/ChainSafe/lodestar/pull/9029), [lodestar@f0caf77f5](https://github.com/ChainSafe/lodestar/commit/f0caf77f50a5), [lodestar@765885746](https://github.com/ChainSafe/lodestar/commit/765885746a06)

</details>

<a id="rpc-042"></a>
<details>
<summary><b>rpc-042</b> Decode snappy frames directly into one destination buffer — <i>implemented · low · memory, cpu, bandwidth</i></summary>

**Idea.** Decompress framed snappy req/resp payloads straight into one final output buffer sized from the advertised length, without intermediate slices or composite buffers that are re-summed or re-copied, and abort as soon as the payload exceeds the expected size.

**Gap in Lighthouse.** 

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/codec.rs:182-190`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L182-L190) vec![0; length] destination and read_exact via FrameDecoder over Take(max_compress_len)
- [`beacon_node/lighthouse_network/src/rpc/codec.rs:279-282`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L279-L282) same for responses

**Sources.** [nimbus@a605c7244](https://github.com/status-im/nimbus-eth2/commit/a605c7244e14), [nimbus#1018](https://github.com/status-im/nimbus-eth2/pull/1018), [teku#11587](https://github.com/Consensys-Incorporated/teku/pull/11587), [teku#11589](https://github.com/Consensys-Incorporated/teku/pull/11589)

</details>

<a id="rpc-046"></a>
<details>
<summary><b>rpc-046</b> Snappy-compress req/resp payloads by default — <i>implemented · low · bandwidth</i></summary>

**Idea.** Compress SSZ req/resp (and gossip) payloads with framed snappy, enabled by default, to cut bytes on the wire.

**Gap in Lighthouse.** 

**Impact.** Already default; nothing to gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/codec.rs:127`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L127) FrameEncoder on every RPC payload
- [`beacon_node/lighthouse_network/src/types/pubsub.rs:6`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L6) raw snappy for gossip

**Sources.** [teku#2552](https://github.com/Consensys-Incorporated/teku/pull/2552), [teku#1584](https://github.com/Consensys-Incorporated/teku/pull/1584), [teku#1670](https://github.com/Consensys-Incorporated/teku/pull/1670), [lighthouse#866](https://github.com/sigp/lighthouse/pull/866), [nimbus@75c1c6a95](https://github.com/status-im/nimbus-eth2/commit/75c1c6a95c24)

</details>

<a id="rpc-050"></a>
<details>
<summary><b>rpc-050</b> Compute committee assignments via index lookup, no pubkey scan — <i>implemented · low · cpu, latency</i></summary>

**Idea.** For committee assignment queries, look up requested validators by index and compute assignments directly, instead of filtering all pubkeys for active status in O(n).

**Gap in Lighthouse.** 

**Impact.** Duties computed from requested indices and shuffling cache, no pubkey scan.

**Best measured result.** None (pr:prysm#2787)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/attester_duties.rs:15`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L15) attester_duties takes request_indices
- [`beacon_node/http_api/src/attester_duties.rs:50`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L50) cached_attestation_duties via validator_attestation_duties with indices and shuffling cache

**Sources.** [prysm#2787](https://github.com/OffchainLabs/prysm/pull/2787)

</details>

<a id="rpc-028"></a>
<details>
<summary><b>rpc-028</b> Share proposer signature check across RPC column sidecars — <i>n/a · medium · cpu</i></summary>

**Idea.** When verifying data column sidecars received over by-root/by-range RPC, cache the verified signed block header (LRU keyed by header) so all columns of one block share a single BLS verification.

**Gap in Lighthouse.** 

**Impact.** Lighthouse's RPC column path performs no proposer BLS check at all (columns are tied to the requested block root, KZG-verified in batch), so there is no repeated signature to share.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context/requests/data_columns_by_root.rs:57`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/requests/data_columns_by_root.rs#L57) RPC columns matched to requested block_root only
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1122`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1122) verify_kzg_for_data_column_list does KZG only, no header signature
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1185`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1185) verify_proposer_and_signature is gossip path only

**Sources.** [teku#10042](https://github.com/Consensys-Incorporated/teku/pull/10042)

</details>

<a id="rpc-091"></a>
<details>
<summary><b>rpc-091</b> Yield to scheduler between served items — <i>n/a · medium · S · latency</i></summary>

**Idea.** In column by-range/by-root handlers, yield to the event loop/scheduler between items so a large request cannot block other work (one blocked for 2 s and missed a block).

**Gap in Lighthouse.** Nimbus problem was a single-threaded event loop blocked; Lighthouse serves these on blocking worker threads off the async runtime, so a large request cannot stall the event loop.

**Impact.** Nothing; a large request occupies one worker thread but not the async scheduler.

**Best measured result.** None (pr:nimbus#9192)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/mod.rs:855-870`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L855-L870) (columns by range run as Work::DataColumnsByRangeRequest blocking closure on beacon processor worker)
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1127`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1127),1456 (blocks/envelopes by range use spawn_blocking_handle)

**Sources.** [nimbus#9192](https://github.com/status-im/nimbus-eth2/pull/9192)

</details>

