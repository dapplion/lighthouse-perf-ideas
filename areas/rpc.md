# rpc

102 ideas: 15 not, 17 partial, 47 implemented, 23 n/a; 11 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [rpc-001](#rpc-001) | Per-peer per-protocol inbound rate limits on requests and objects | implemented | low | S | cpu, bandwidth, latency, disk |
| [rpc-002](#rpc-002) | O(1) custody index for serving data column requests | not | low | S | cpu |
| [rpc-003](#rpc-003) | Wake RPC connection handler when new events arrive | implemented | low | S | latency |
| [rpc-004](#rpc-004) | Aggregate attestations before streaming to slasher consumers | n/a | low | S | cpu, bandwidth |
| [rpc-005](#rpc-005) | Serve block ranges without intermediate block list allocation | implemented | low | S | memory |
| [rpc-006](#rpc-006) | Allocation-free shared varint encoder for req/resp length prefixes | implemented | low | S | memory, cpu |
| [rpc-007](#rpc-007) | Use a faster native snappy codec for RPC | partial | low | S | cpu, latency |
| [rpc-008](#rpc-008) | Close or reset req/resp streams promptly on every path | implemented | low | S | memory, latency |
| [rpc-009](#rpc-009) | Process RPC responses on a separate async queue | n/a | low | L | memory, latency |
| [rpc-010](#rpc-010) | Run snappy compression off the network event loop | not | low | L | cpu, latency |
| [rpc-011](#rpc-011) | Serve API head queries from in-memory chain head | implemented | low | S | cpu, disk |
| [rpc-012](#rpc-012) | Answer Status from fork choice, no state or DB reads | implemented | low | S | cpu, latency, disk |
| [rpc-013](#rpc-013) | Read only blocks in requested by-range span and step | implemented | low | S | disk, latency, cpu, bandwidth |
| [rpc-014](#rpc-014) | Read head state without cloning in read-only endpoints | implemented | low | S | cpu, memory |
| [rpc-015](#rpc-015) | Do not pin per-stream state to connection-lifetime futures | n/a | low | S | memory |
| [rpc-016](#rpc-016) | Skip response timeout wait when already done | n/a | low | S | latency |
| [rpc-017](#rpc-017) **★** | Serve stored DB bytes without decode, re-encode or recompression | not | medium | L | cpu, latency |
| [rpc-018](#rpc-018) | Copy decoded fields out of pooled network buffers | n/a | low | S | memory |
| [rpc-019](#rpc-019) | Size column by-root request batches by max blobs | not | low | S | bandwidth, latency |
| [rpc-020](#rpc-020) | Resolve unfinalized by-range roots from fork choice in one walk | implemented | low | S | cpu, disk, latency |
| [rpc-021](#rpc-021) | Cap received response chunks by requested item count | implemented | low | S | bandwidth, cpu, memory |
| [rpc-022](#rpc-022) | Bound length prefix by per-type SSZ limits before decompressing | implemented | low | S | memory, bandwidth, cpu |
| [rpc-023](#rpc-023) **★** | Bounded throttling queue between req/resp handlers and storage | partial | medium | S | cpu, memory, disk, latency |
| [rpc-024](#rpc-024) | Buffered handoff channel to avoid leaked response workers | n/a | low | S | memory |
| [rpc-025](#rpc-025) | Bulk hardware CRC32C for snappy frame checksums | partial | low | M | cpu, latency |
| [rpc-026](#rpc-026) | Slasher caches committees instead of repeated beacon RPCs | n/a | low | S | bandwidth, latency |
| [rpc-027](#rpc-027) | Compute RPC protocol size limits once statically | partial | low | S | cpu |
| [rpc-028](#rpc-028) | Share proposer signature check across RPC column sidecars | n/a | medium |  | cpu |
| [rpc-029](#rpc-029) | Cancel response producer when consumer stops early | not | low | M | cpu, bandwidth, memory |
| [rpc-030](#rpc-030) | Validate and cap by-range request counts before DB reads | implemented | medium | S | bandwidth, cpu, disk |
| [rpc-031](#rpc-031) | Read wide column by-range requests in bounded batches | implemented | low | S | memory, disk |
| [rpc-032](#rpc-032) | Lower rate-limit quota cost for blob sidecars | implemented | low | S | bandwidth |
| [rpc-033](#rpc-033) **★** | Serve by-range/by-root requests from in-memory pending caches first | partial | medium | M | latency, disk, bandwidth |
| [rpc-034](#rpc-034) **★** | Stream by-range/by-root responses chunk by chunk from DB | partial | medium | M | latency, memory, sync |
| [rpc-035](#rpc-035) | Clear request timeout timers and abort listeners on completion | implemented | low | S | memory, latency, cpu |
| [rpc-036](#rpc-036) | Write response code, length and payload together | implemented | low | S | latency, bandwidth |
| [rpc-037](#rpc-037) | Snappy-compress RPC responses directly into destination buffer | not | low | S | memory, cpu |
| [rpc-038](#rpc-038) | Outbound self rate limiter capping concurrent requests per peer | implemented | medium | S | bandwidth, latency, sync |
| [rpc-039](#rpc-039) | Load justified state from DB by root | n/a | low | S | cpu, latency |
| [rpc-040](#rpc-040) | Run sync-response DB reads on blocking threads | implemented | medium | S | cpu, latency |
| [rpc-041](#rpc-041) **★** | Abort API work once request deadline passes | not | medium | S | cpu, latency |
| [rpc-042](#rpc-042) | Decode snappy frames directly into one destination buffer | partial | low | M | memory, cpu, bandwidth |
| [rpc-043](#rpc-043) | Deduplicate by-root request roots and stream in batches | not | low | S | cpu, latency |
| [rpc-044](#rpc-044) | Stop ancestor walk at already-requested roots | n/a | low | S | bandwidth, cpu |
| [rpc-045](#rpc-045) | Compute each validator status once in duties | n/a | low | S | cpu |
| [rpc-046](#rpc-046) | Snappy-compress req/resp payloads by default | implemented | low | S | bandwidth |
| [rpc-047](#rpc-047) | Copy uncompressed snappy chunks directly to destination | not | low | M | cpu, latency, memory |
| [rpc-048](#rpc-048) | Disable HTTP pipelining in the API server | implemented | low | S | latency |
| [rpc-049](#rpc-049) | Refuse validator API requests while node is syncing | implemented | medium | S | cpu, sync |
| [rpc-050](#rpc-050) | Compute committee assignments via index lookup, no pubkey scan | implemented | low | S | cpu, latency |
| [rpc-051](#rpc-051) | Slot-only lookups in sidecar by-root handlers, no full block | partial | low | S | disk, latency |
| [rpc-052](#rpc-052) | Avoid copying encoded request buffers before send | not | low | S | memory, cpu |
| [rpc-053](#rpc-053) | Drop queued requests from disconnected peers | implemented | low | S | cpu |
| [rpc-054](#rpc-054) | Reject blob requests for post-Fulu slots early | partial | low | S | cpu, disk |
| [rpc-055](#rpc-055) | Free every per-peer rate limiter state for disconnected peers | implemented | medium | S | memory |
| [rpc-056](#rpc-056) | Expire stale requests in outbound self rate limiter | partial | low | S | sync |
| [rpc-057](#rpc-057) | Fewer async stream pipe layers in req/resp | n/a | low | S | cpu, latency |
| [rpc-058](#rpc-058) | Filter column requests to custody columns before DB | implemented | medium | S | disk, cpu, bandwidth |
| [rpc-059](#rpc-059) | Filter by-range sidecar responses to requested slots | implemented | low | S | bandwidth |
| [rpc-060](#rpc-060) | Half-close request stream after sending request | implemented | medium | S | sync, latency |
| [rpc-061](#rpc-061) | Compute by-range block roots by hashing loaded blocks | implemented | medium | S | disk, latency |
| [rpc-062](#rpc-062) | Hoist per-message timeout defaults out of hot path | n/a | low |  | cpu |
| [rpc-063](#rpc-063) | Do not await Goodbye response | implemented | low | S | latency |
| [rpc-064](#rpc-064) **★** | Grow decode buffer as bytes arrive, not upfront | not | medium | S | memory |
| [rpc-065](#rpc-065) | Validate blob responses incrementally per chunk | implemented | low | S | cpu, bandwidth |
| [rpc-066](#rpc-066) | Interleave response chunks across concurrent substreams | implemented | medium | S | latency |
| [rpc-067](#rpc-067) | BlobSidecarsByRange: iterate only indices with commitments | implemented | low | S | disk, cpu, latency |
| [rpc-068](#rpc-068) | Upgrade JSON-RPC library for engine API client | n/a | low |  | memory, cpu |
| [rpc-069](#rpc-069) | Charge rate limiter for full request count upfront | implemented | high | S | cpu, memory, bandwidth |
| [rpc-070](#rpc-070) | Reuse snappy encoder/decoder objects | not | low | M | memory, cpu |
| [rpc-071](#rpc-071) **★** | Global cross-peer quota applied before decode | partial | medium | M | bandwidth, cpu |
| [rpc-072](#rpc-072) | Prioritize Status handling over heavy requests | implemented | low | S | latency, sync |
| [rpc-073](#rpc-073) | Prefer Status v2 in protocol list | implemented | low | S | latency, sync |
| [rpc-074](#rpc-074) | Quadratic rate-limit cost for BlocksByRange step | implemented | low | S | cpu, disk |
| [rpc-075](#rpc-075) **★** | Charge rate limiter by blocks actually served | partial | medium | M | sync, bandwidth |
| [rpc-076](#rpc-076) **★** | Downscore peers requesting too many columns | partial | medium | S | bandwidth |
| [rpc-077](#rpc-077) | Read request before applying quota on mplex | implemented | low | S | latency, bandwidth |
| [rpc-078](#rpc-078) | Drop inbound substream on response timeout | implemented | low | S | memory |
| [rpc-079](#rpc-079) | Close request decoder when stream dropped | n/a | low | S | memory |
| [rpc-080](#rpc-080) | Reuse snappy output buffer across partial-frame retries | not | low | M | cpu, memory |
| [rpc-081](#rpc-081) | Serve RPC from bounded priority work queue | implemented | low | S | latency, cpu |
| [rpc-082](#rpc-082) **★** | Reconstruct pruned column sidecars to serve requests | not | medium | L | disk, cpu |
| [rpc-083](#rpc-083) | Skip empty BlobsByRange response chunks | implemented | low | S | bandwidth |
| [rpc-084](#rpc-084) | Poll only network peers/streams with pending work | n/a | low | S | cpu |
| [rpc-085](#rpc-085) | Skip unknown roots in BlocksByRoot, keep streaming | implemented | low | S | sync |
| [rpc-086](#rpc-086) | Use 4-byte payload length prefix | n/a | low |  | bandwidth |
| [rpc-087](#rpc-087) | Stagger large by-range responses over time | not | low | S | bandwidth, cpu |
| [rpc-088](#rpc-088) | Cache Status earliest-available-slot per epoch | implemented | low | S | cpu, disk |
| [rpc-089](#rpc-089) | Non-blocking snappy frame decoding | n/a | low |  | memory, latency |
| [rpc-090](#rpc-090) **★** | Await each response write before loading next | partial | medium | L | memory, bandwidth, latency |
| [rpc-091](#rpc-091) | Yield to scheduler between served items | n/a | medium | S | latency |
| [rpc-092](#rpc-092) | Encode status and RPC messages in compact binary, not text | implemented | low | S | bandwidth, cpu |
| [rpc-093](#rpc-093) | Build status message only when sending | partial | low | S | cpu |
| [rpc-094](#rpc-094) | Combine status and ping/metadata exchange per peer | n/a | low |  | bandwidth, latency |
| [rpc-095](#rpc-095) | Truncate peer-supplied error message before decoding | implemented | low | S | cpu, memory |
| [rpc-096](#rpc-096) | Cap simultaneous inbound substreams per peer | implemented | low | S | memory, bandwidth |
| [rpc-097](#rpc-097) | Run cleanup when async request supplier throws | n/a | low | S | memory |
| [rpc-098](#rpc-098) | Trim by-root/by-range requests to servable range before expensive reads | partial | low | S | cpu, disk, latency |
| [rpc-099](#rpc-099) | Send only each sidecar own bytes in by-range responses | n/a | low | S | bandwidth |
| [rpc-100](#rpc-100) | Fork-dependent maximum RPC and gossip message sizes | partial | low | M | memory, bandwidth |
| [rpc-101](#rpc-101) | Group column by-root requests per block root | implemented | low | S | bandwidth |
| [rpc-102](#rpc-102) | Release pooled decoder buffers once response is decoded | n/a | low | S | memory |

★ actionable. Click an id for the full record.

## Ideas

<a id="rpc-001"></a>
<details>
<summary><b>rpc-001</b> Per-peer per-protocol inbound rate limits on requests and objects — <i>implemented · low · S · cpu, bandwidth, latency, disk</i></summary>

**Idea.** Rate limit inbound req/resp per peer and per protocol with a continuously refilling token bucket (GCRA) in the RPC behaviour, counting both requests and storage-backed objects (blocks, blobs, columns) per window, enabled by default. Violators are rejected, penalized or disconnected, so one peer cannot force unbounded DB reads, CPU or bandwidth, and serving load is spread evenly.

**Impact.** Already present; no change.

**Best measured result.** None (pr:nimbus#7952)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/rate_limiter.rs:388-410`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/rate_limiter.rs#L388-L410) allows(): tokens = max_responses per request, per-protocol GCRA limiter per peer
- [`beacon_node/lighthouse_network/src/rpc/protocol.rs:858-866`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/protocol.rs#L858-L866) max_responses counts blocks and count*columns for DataColumnsByRange
- [`beacon_node/lighthouse_network/src/rpc/inbound_limiter.rs:167-180`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/inbound_limiter.rs#L167-L180) TooLarge/TooSoon handling
- [`beacon_node/lighthouse_network/src/rpc/mod.rs:444-454`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/mod.rs#L444-L454) RateLimited error response
- [`beacon_node/src/config.rs:1522-1532`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/config.rs#L1522-L1532) enabled by default

**Skeptic check.** Verified a per-peer, per-protocol GCRA limiter that charges the requested object count, including columns times slots, and is on by default. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#1402](https://github.com/sigp/lighthouse/pull/1402), [grandine@dc0d3e071](https://github.com/grandinetech/grandine/commit/dc0d3e071010), [nimbus#7952](https://github.com/status-im/nimbus-eth2/pull/7952), [teku#9841](https://github.com/Consensys-Incorporated/teku/pull/9841), [teku#2488](https://github.com/Consensys-Incorporated/teku/pull/2488), [caplin#8868](https://github.com/erigontech/erigon/pull/8868), [teku#2500](https://github.com/Consensys-Incorporated/teku/pull/2500), [prysm#17504](https://github.com/OffchainLabs/prysm/pull/17504), [lodestar#3454](https://github.com/ChainSafe/lodestar/pull/3454)

</details>


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


<a id="rpc-003"></a>
<details>
<summary><b>rpc-003</b> Wake RPC connection handler when new events arrive — <i>implemented · low · S · latency</i></summary>

**Idea.** Store a waker in the RPC connection handler and wake it when an outbound event is queued, so the handler is polled promptly instead of stalling until another event happens.

**Impact.** None: this is the Lighthouse PR itself and it is present.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/handler.rs:148`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L148) waker field
- [`beacon_node/lighthouse_network/src/rpc/handler.rs:364-365`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L364-L365) wake_by_ref when an event is queued
- [`beacon_node/lighthouse_network/src/rpc/handler.rs:380-385`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L380-L385) waker stored/updated in poll

**Skeptic check.** Waker stored in poll and woken on send, as in lighthouse#2721. Earlier evidence correct (paths were abbreviated).

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#2721](https://github.com/sigp/lighthouse/pull/2721)

</details>


<a id="rpc-004"></a>
<details>
<summary><b>rpc-004</b> Aggregate attestations before streaming to slasher consumers — <i>n/a · low · S · cpu, bandwidth</i></summary>

**Idea.** Buffer attestations with equal data root, aggregate them and flush periodically before streaming them to a consumer such as a slasher. This sends far fewer messages than streaming each unaggregated attestation.

**Impact.** Slasher runs in-process with no streaming to an external consumer, so there is no message stream to cut by aggregation.

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/attestation_queue.rs:55`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/attestation_queue.rs#L55),80 per-attestation queue grouped by validator chunk
- [`beacon_node/beacon_chain/src/attestation_verification.rs:443`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L443) slasher fed in-process

**Sources.** [prysm#5029](https://github.com/OffchainLabs/prysm/pull/5029)

</details>


<a id="rpc-005"></a>
<details>
<summary><b>rpc-005</b> Serve block ranges without intermediate block list allocation — <i>implemented · low · S · memory</i></summary>

**Idea.** Serve blocks-by-range by iterating ancestors and writing results straight into a caller-provided buffer, without first collecting an intermediate list of blocks.

**Impact.** None material: no intermediate block list, only a &lt;=1024 root vector.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1135-1152`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1135-L1152) only block roots are collected into a Vec
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1180-1200`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1180-L1200) chain.get_blocks stream; each block sent as its own SendResponse

**Skeptic check.** Verified blocks are streamed one by one from get_blocks to the network. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus@da988e4e4](https://github.com/status-im/nimbus-eth2/commit/da988e4e404c)

</details>


<a id="rpc-006"></a>
<details>
<summary><b>rpc-006</b> Allocation-free shared varint encoder for req/resp length prefixes — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** Encode and decode the LEB128 varint length prefix and response prefix of every req/resp (and gossip) message with one shared fast implementation that writes into a stack or preallocated buffer, without a heap allocation per message. This cuts allocations and CPU on every message.

**Impact.** Varint prefix is already allocation-free; the remaining per-message allocations are the ssz and snappy Vecs, not the varint.

**Best measured result.** None (commit:nimbus@4e191a06ac07)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/codec.rs:46`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L46) Uvi codec shared across RPC codecs
- [`beacon_node/lighthouse_network/src/rpc/codec.rs:494-510`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L494-L510) handle_length shared varint decode on BytesMut
- ~/.cargo/registry/src/index.crates.io-*/unsigned-varint-0.8.0/src/codec.rs:33-36 serialise encodes into a stack array then extends dst

**Skeptic check.** Verified unsigned-varint 0.8.0 encodes into a stack buffer and decodes in place. The earlier evidence gave a wrong path (beacon_node/unsigned-varint-0.8.0); the crate is under the cargo registry. Gossip has no varint length prefix, so the gossip part does not apply.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus@4e191a06a](https://github.com/status-im/nimbus-eth2/commit/4e191a06ac07), [lodestar#5895](https://github.com/ChainSafe/lodestar/pull/5895), [nimbus#2182](https://github.com/status-im/nimbus-eth2/pull/2182), [caplin#18961](https://github.com/erigontech/erigon/pull/18961)

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


<a id="rpc-008"></a>
<details>
<summary><b>rpc-008</b> Close or reset req/resp streams promptly on every path — <i>implemented · low · S · memory, latency</i></summary>

**Idea.** Close or reset the libp2p req/resp stream as soon as the exchange finishes and on every error path (with correct error codes), so streams and their per-stream buffers are released promptly instead of leaking.

**Impact.** None: inbound and outbound streams are closed or dropped on completion, error, timeout and shutdown.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/handler.rs:466-482`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L466-L482) last_chunk passed to send_message_to_inbound_substream
- [`beacon_node/lighthouse_network/src/rpc/handler.rs:487-518`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L487-L518) deactivated handler closes idle inbound streams
- [`beacon_node/lighthouse_network/src/rpc/handler.rs:553-640`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L553-L640) inbound stream and timeout removed on completion and on send error
- [`beacon_node/lighthouse_network/src/rpc/handler.rs:670-700`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L670-L700) outbound stream moved to Closing on single response, close_after or last expected chunk
- [`beacon_node/lighthouse_network/src/rpc/handler.rs:782-797`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L782-L797) outbound stream and timeout dropped on decode error
- [`beacon_node/lighthouse_network/src/rpc/handler.rs:440-450`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L440-L450) timed-out outbound stream removed
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:216`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L216) terminate_response_stream sends error code plus terminator

**Skeptic check.** Read both the inbound and outbound poll loops in RPCHandler::poll. Every exit path removes the stream and its delay key. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@14e40c04f](https://github.com/ChainSafe/lodestar/commit/14e40c04f580), [lodestar@cf39face7](https://github.com/ChainSafe/lodestar/commit/cf39face7e81), [caplin#7582](https://github.com/erigontech/erigon/pull/7582), [prysm#6481](https://github.com/OffchainLabs/prysm/pull/6481)

</details>


<a id="rpc-009"></a>
<details>
<summary><b>rpc-009</b> Process RPC responses on a separate async queue — <i>n/a · low · L · memory, latency</i></summary>

**Idea.** Hand received RPC response chunks to a separate processing queue so slow handling does not count against network read timeouts and peer bytes are not buffered unbounded in the transport; stop processing once the request is finished.

**Impact.** Rust libp2p handler forwards decoded chunks over channels to the router; Lighthouse's streams are read by the handler and processing happens in other tasks, so processing time does not count against read timeouts.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/handler.rs:374`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L374) poll; inbound/outbound substream timeouts are DelayQueue-based and responses are forwarded as events to the router

**Sources.** [teku#1201](https://github.com/Consensys-Incorporated/teku/pull/1201)

</details>


<a id="rpc-010"></a>
<details>
<summary><b>rpc-010</b> Run snappy compression off the network event loop — <i>not · low · L · cpu, latency</i></summary>

**Idea.** Do snappy compression and decompression of req/resp payloads asynchronously on worker threads so large payloads do not block the networking event loop.

**Gap in Lighthouse.** Snappy encode/decode runs synchronously inside the libp2p swarm task. To offload, the codec would have to move compression to spawn_blocking/rayon and hand bytes to the stream asynchronously (SSZ-snappy codec in lighthouse_network/src/rpc/codec.rs).

**Impact.** Would free the single swarm task during large block/column responses (a few ms per multi-hundred-KB payload); gain is small on most nodes and mostly matters on serving nodes under load.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/codec.rs:127`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L127) FrameEncoder::new(Vec::new()) compresses inline in the encoder; codec.rs:187 FrameDecoder decodes inline in the swarm/handler task

**Sources.** [nimbus#986](https://github.com/status-im/nimbus-eth2/pull/986)

</details>


<a id="rpc-011"></a>
<details>
<summary><b>rpc-011</b> Serve API head queries from in-memory chain head — <i>implemented · low · S · cpu, disk</i></summary>

**Idea.** Answer validator/API calls that need the head block, root or state from the chain's in-memory head instead of reading them from the database on each request.

**Impact.** None: head root, state and block are served from CanonicalHead without DB reads.

**Best measured result.** None (pr:prysm#4752)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/state_id.rs:29-38`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L29-L38) StateId::root Head from canonical_head.head_and_execution_status
- [`beacon_node/http_api/src/state_id.rs:178-187`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L178-L187) StateId::state Head clones cached_head.snapshot.beacon_state
- [`beacon_node/http_api/src/block_id.rs:48-57`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L48-L57) BlockId::root Head from cached head
- [`beacon_node/http_api/src/block_id.rs:182-192`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L182-L192) blinded_block Head from cached_head.snapshot.beacon_block
- [`beacon_node/http_api/src/block_id.rs:239`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L239) full block Head from cached head

**Skeptic check.** Confirmed that the Head variants of StateId and BlockId return early from the cached head before any store lookup. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#4752](https://github.com/OffchainLabs/prysm/pull/4752), [prysm#3309](https://github.com/OffchainLabs/prysm/pull/3309)

</details>


<a id="rpc-012"></a>
<details>
<summary><b>rpc-012</b> Answer Status from fork choice, no state or DB reads — <i>implemented · low · S · cpu, latency, disk</i></summary>

**Idea.** When handling an inbound or outbound Status message (and checking peer relevance), take head root/slot, finalized checkpoint and 'is this root finalized' from in-memory fork choice or the cached head instead of loading the head state or calling block_root_at_slot. block_root_at_slot iterates states and is very slow without finality.

**Impact.** None: there are no state loads. The only DB read is a freezer root lookup for peers with older finality, and that read is cheap.

**Best measured result.** None (pr:lodestar#902)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/status.rs:21-52`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/status.rs#L21-L52) status_message built from cached_head plus in-memory custody and anchor info
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:106-160`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L106-L160) check_peer_relevance: checkpoint comparisons, block_root_at_slot only for remote finalized slot below the split (freezer)

**Skeptic check.** Status building and relevance checks use cached head and fork-choice checkpoints. The slow hot-state block_root_at_slot path is explicitly skipped for slots above the split. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#5481](https://github.com/sigp/lighthouse/pull/5481), [prysm#10978](https://github.com/OffchainLabs/prysm/pull/10978), [lighthouse#7056](https://github.com/sigp/lighthouse/pull/7056), [lighthouse#7054](https://github.com/sigp/lighthouse/pull/7054), [lighthouse#7082](https://github.com/sigp/lighthouse/pull/7082), [lodestar@e0f646dd6](https://github.com/ChainSafe/lodestar/commit/e0f646dd6738), [lodestar#902](https://github.com/ChainSafe/lodestar/pull/902)

</details>


<a id="rpc-013"></a>
<details>
<summary><b>rpc-013</b> Read only blocks in requested by-range span and step — <i>implemented · low · S · disk, latency, cpu, bandwidth</i></summary>

**Idea.** In blocks-by-range serving, read from the DB only the blocks inside the requested start/count/step span, applying the step in the DB query and not reading an extra step past the end, instead of loading all blocks in range and discarding.

**Impact.** None: only the requested span is read. Step is deprecated and handled as 1.

**Best measured result.** None (pr:prysm#4488)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1250-1296`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1250-L1296) get_block_roots_for_slot_range resolves only [start, start+count)
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1344-1347`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1344-L1347) store path take_while(slot &lt; start+count)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:8427-8453`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L8427-L8453) block_roots_from_fork_choice filters and breaks below start
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1172`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1172) get_blocks loads only resolved roots
- [`beacon_node/lighthouse_network/src/rpc/methods.rs:470-485`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/methods.rs#L470-L485) step forced to 1

**Second check.** The earlier gap itself said nothing is left to change; I confirmed both root paths (store iterator and fork choice) stop at start+count and that step is discarded at decode, so the verdict is implemented, not partial.

**Skeptic check.** Roots are resolved first and only those blocks are loaded. Blocks, blobs, columns and envelopes by-range all share this resolver. The earlier evidence was correct.

**Verdict history.** partial (checked) → implemented (refuted) → implemented (skeptic)

**Sources.** [prysm#4046](https://github.com/OffchainLabs/prysm/pull/4046), [prysm#4488](https://github.com/OffchainLabs/prysm/pull/4488), [teku#1131](https://github.com/Consensys-Incorporated/teku/pull/1131)

</details>


<a id="rpc-014"></a>
<details>
<summary><b>rpc-014</b> Read head state without cloning in read-only endpoints — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** In RPC/API endpoints that only read the head state, borrow a read-only reference instead of copying the full state per request.

**Impact.** Read-only state endpoints already borrow the head; remaining clones are cheap tree-sharing clones.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/state_id.rs:218-241`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L218-L241) map_state_and_execution_optimistic_and_finalized borrows head.snapshot.beacon_state for Head
- [`beacon_node/http_api/src/state_id.rs:178-188`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L178-L188) state() for Head clones, but BeaconState clone is milhouse structural sharing
- [`beacon_node/http_api/src/lib.rs:1735`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L1735),2175 remaining state() callers need an owned state (e.g. SSZ debug state)

**Skeptic check.** Verified the borrow path for Head and that other state() users are non-head slots or need ownership. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#11950](https://github.com/OffchainLabs/prysm/pull/11950)

</details>


<a id="rpc-015"></a>
<details>
<summary><b>rpc-015</b> Do not pin per-stream state to connection-lifetime futures — <i>n/a · low · S · memory</i></summary>

**Idea.** Do not chain per-stream callbacks off long-lived connection-close futures, which keep the closures alive until the connection ends; race the two with anyOf/select so per-stream state is freed when the stream ends.

**Impact.** Java CompletableFuture closure retention has no Rust equivalent; per-stream state is dropped with the substream.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/handler.rs:119`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L119) per-substream state kept in maps and removed on completion

**Sources.** [teku#2335](https://github.com/Consensys-Incorporated/teku/pull/2335)

</details>


<a id="rpc-016"></a>
<details>
<summary><b>rpc-016</b> Skip response timeout wait when already done — <i>n/a · low · S · latency</i></summary>

**Idea.** In req/resp, do not wait for the response timeout when the response has already completed or no response is expected; return immediately.

**Impact.** Lighthouse uses DelayQueue keys removed on completion, not a wait on a timer; no extra wait occurs.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/handler.rs:414`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L414) purges expired inbound substreams via DelayQueue; completed substreams are removed from the queue

**Sources.** [lodestar#7800](https://github.com/ChainSafe/lodestar/pull/7800)

</details>


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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [nimbus#3598](https://github.com/status-im/nimbus-eth2/pull/3598), [lodestar#3435](https://github.com/ChainSafe/lodestar/pull/3435), [caplin#24220](https://github.com/erigontech/erigon/pull/24220)

</details>


<a id="rpc-018"></a>
<details>
<summary><b>rpc-018</b> Copy decoded fields out of pooled network buffers — <i>n/a · low · S · memory</i></summary>

**Idea.** Copy decoded message fields (e.g. peer Status) out of the pooled network buffer instead of keeping references into it, so the buffer can be released back to the pool.

**Impact.** Rust decode produces owned values; no pooled-buffer retention problem.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/codec.rs:187`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L187) decoding yields owned SSZ-decoded values from a Cursor over BytesMut; no references into pooled buffers kept

**Sources.** [teku#968](https://github.com/Consensys-Incorporated/teku/pull/968)

</details>


<a id="rpc-019"></a>
<details>
<summary><b>rpc-019</b> Size column by-root request batches by max blobs — <i>not · low · S · bandwidth, latency</i></summary>

**Idea.** When requesting data columns by root, size each request batch from max blobs per block so every response stays near a target cell count, and split queued requests accordingly.

**Gap in Lighthouse.** Cap block_roots per DataColumnsByRoot request by a cell budget (max_request_data_column_sidecars / indices.len(), and by max_blobs_per_block for response size) and split into several requests in custody.rs request loop / try_into_request.

**Impact.** Custody lookups usually involve one block root, so batching rarely hits large sizes; it only bounds response size in multi-block parent lookups.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context/requests/data_columns_by_root.rs:16`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/requests/data_columns_by_root.rs#L16) try_into_request builds one identifier per block root capped only by spec.max_request_blocks
- network/src/sync/network_context/custody.rs:301 each peer request carries all lookup block_roots x indices

**Sources.** [teku#10279](https://github.com/Consensys-Incorporated/teku/pull/10279)

</details>


<a id="rpc-020"></a>
<details>
<summary><b>rpc-020</b> Resolve unfinalized by-range roots from fork choice in one walk — <i>implemented · low · S · cpu, disk, latency</i></summary>

**Idea.** When serving by-range requests, take block roots for unfinalized slots from the fork choice proto-array in one backwards walk over the whole range, and only finalized roots from the store. This avoids per-slot store lookups and state loads or regeneration during long non-finality.

**Impact.** None: unfinalized roots come from one fork-choice walk on every by-range protocol.

**Best measured result.** None (pr:teku#2156)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1250-1296`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1250-L1296) split at finalized slot between store and fork choice
- [`beacon_node/beacon_chain/src/beacon_chain.rs:8427-8453`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L8427-L8453) one proto_array iter_block_roots walk from head
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1129`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1129),1458,1674,1837 blocks, envelopes, blobs and columns by-range all use get_block_roots_for_slot_range

**Skeptic check.** Verified that the split exists and that all four by-range handlers call the shared resolver. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#2156](https://github.com/Consensys-Incorporated/teku/pull/2156), [lighthouse#7058](https://github.com/sigp/lighthouse/pull/7058), [lighthouse#7098](https://github.com/sigp/lighthouse/pull/7098), [lighthouse#7066](https://github.com/sigp/lighthouse/pull/7066), [teku#2166](https://github.com/Consensys-Incorporated/teku/pull/2166)

</details>


<a id="rpc-021"></a>
<details>
<summary><b>rpc-021</b> Cap received response chunks by requested item count — <i>implemented · low · S · bandwidth, cpu, memory</i></summary>

**Idea.** For each outgoing request, compute the maximum expected response chunks from the request (number of roots or count) and tight sizes for fixed-size messages, and reject or close the stream as soon as a peer sends more, instead of reading and decoding the surplus.

**Impact.** None: surplus chunks are never read or decoded once the expected count is reached.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/handler.rs:670-700`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L670-L700) outbound max_remaining_chunks decremented, stream moved to Closing at 0 or on single-response requests
- [`beacon_node/lighthouse_network/src/rpc/handler.rs:800-826`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L800-L826) Closing state drops the stream and reports EndOfStream even if responder keeps sending
- [`beacon_node/lighthouse_network/src/rpc/codec.rs:268-275`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L268-L275) per-protocol min/max size check per chunk

**Skeptic check.** After the expected chunks arrive, the outbound stream goes to Closing and is never polled for data again. Size bounds come from rpc_response_limits. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#1030](https://github.com/Consensys-Incorporated/teku/pull/1030), [nimbus#6961](https://github.com/status-im/nimbus-eth2/pull/6961), [nimbus#6954](https://github.com/status-im/nimbus-eth2/pull/6954), [nimbus#4264](https://github.com/status-im/nimbus-eth2/pull/4264)

</details>


<a id="rpc-022"></a>
<details>
<summary><b>rpc-022</b> Bound length prefix by per-type SSZ limits before decompressing — <i>implemented · low · S · memory, bandwidth, cpu</i></summary>

**Idea.** Precompute min/max SSZ encoded size per RPC message type, reject a chunk whose declared length is outside that range, and wrap the snappy decoder in a reader limited to max_compressed_len(declared length). Bad, padded or compression-bomb payloads are rejected before reading or allocating for them.

**Impact.** None: the length is bounded before the decoded buffer is allocated, and compressed input is capped.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/codec.rs:167-186`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L167-L186) request: is_out_of_bounds check then Cursor.take(max_compress_len) around FrameDecoder
- [`beacon_node/lighthouse_network/src/rpc/codec.rs:265-281`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L265-L281) same for responses
- [`beacon_node/lighthouse_network/src/rpc/codec.rs:315-317`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L315-L317) same for error responses
- [`beacon_node/lighthouse_network/src/rpc/protocol.rs:568-655`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/protocol.rs#L568-L655) per-protocol RpcLimits

**Skeptic check.** The bounds check happens before the vec![0; length] allocation, and the snappy reader is wrapped in take(max_compress_len) on the request, response and error paths. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#7445](https://github.com/OffchainLabs/prysm/pull/7445), [nimbus@3433c77c3](https://github.com/status-im/nimbus-eth2/commit/3433c77c35f3), [teku#2360](https://github.com/Consensys-Incorporated/teku/pull/2360), [lighthouse#1738](https://github.com/sigp/lighthouse/pull/1738), [prysm#7479](https://github.com/OffchainLabs/prysm/pull/7479), [caplin#25079](https://github.com/erigontech/erigon/pull/25079), [prysm#17660](https://github.com/OffchainLabs/prysm/pull/17660), [lighthouse#1250](https://github.com/sigp/lighthouse/pull/1250), [lodestar@f57debc24](https://github.com/ChainSafe/lodestar/commit/f57debc2483d)

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

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [teku#9828](https://github.com/Consensys-Incorporated/teku/pull/9828), [teku#9689](https://github.com/Consensys-Incorporated/teku/pull/9689)

</details>


<a id="rpc-024"></a>
<details>
<summary><b>rpc-024</b> Buffered handoff channel to avoid leaked response workers — <i>n/a · low · S · memory</i></summary>

**Idea.** Use a buffered channel (capacity 1) for the request/response handoff so the worker can finish its send after the caller returns on cancel, avoiding leaked goroutines/tasks that hold responses.

**Impact.** None; Go goroutine leak pattern does not exist in Lighthouse's Rust channel design.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1934`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1934) terminate_response_stream: handlers are plain Rust fns/tokio tasks sending on an mpsc, no request/response worker rendezvous channel

**Sources.** [caplin#16782](https://github.com/erigontech/erigon/pull/16782)

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


<a id="rpc-026"></a>
<details>
<summary><b>rpc-026</b> Slasher caches committees instead of repeated beacon RPCs — <i>n/a · low · S · bandwidth, latency</i></summary>

**Idea.** Cache committees in the slasher (or other API consumer) so it does not repeat the same committee RPC calls to the beacon node.

**Impact.** None; no RPC boundary between slasher and beacon node.

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/slasher.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/slasher.rs): slasher runs in-process and is fed IndexedAttestations by the beacon chain, no committee RPC to a beacon node

**Sources.** [prysm#4812](https://github.com/OffchainLabs/prysm/pull/4812)

</details>


<a id="rpc-027"></a>
<details>
<summary><b>rpc-027</b> Compute RPC protocol size limits once statically — <i>partial · low · S · cpu</i></summary>

**Idea.** Compute the constant per-protocol RPC size limits once in a lazily initialised static instead of recomputing them on every encode/decode call.

**Gap in Lighthouse.** The #6595 statics cover blocks, but not data columns. On every DataColumnsByRange/ByRoot response chunk, SSZSnappyOutboundCodec::decode_response calls ProtocolId::rpc_response_limits, which calls rpc_data_column_limits. That function runs DataColumnSidecarFulu::min_size() and max_size(max_blobs), and each one builds a whole sidecar (max_blobs x 2048-byte cells plus commitments and proofs) and SSZ-encodes it only to read its length. This also repeats on each decode retry while a large column arrives in several frames. Fix: compute Fulu min/max with ssz_fixed_len arithmetic (as DataColumnSidecarGloas::max_size does), or cache per (fork, max_blobs).

**Impact.** Removes one allocation and SSZ encode of tens to hundreds of KB per received data column chunk during sync. This is the same pattern that #6595 measured at about 10% of CPU for blocks, but here it is a smaller fraction of column decode cost.

**Best measured result.** None (pr:lighthouse#6595)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/protocol.rs:30-126`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/protocol.rs#L30-L126) block and light-client limits are LazyLock statics
- [`beacon_node/lighthouse_network/src/rpc/protocol.rs:638-643`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/protocol.rs#L638-L643) DataColumnsByRoot/ByRange response limits call rpc_data_column_limits on every call
- [`beacon_node/lighthouse_network/src/rpc/protocol.rs:727-754`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/protocol.rs#L727-L754) rpc_data_column_limits builds the limits each call
- [`consensus/types/src/data/data_column_sidecar.rs:297-332`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/data/data_column_sidecar.rs#L297-L332) DataColumnSidecarFulu::min_size/max_size allocate a sidecar with max_blobs cells (2048 B each) and SSZ-encode it to measure length
- [`beacon_node/lighthouse_network/src/rpc/codec.rs:270`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L270) rpc_response_limits called in decode_response for every chunk and again on every partial-data retry

**Skeptic check.** The earlier evidence was right for blocks, light-client and blob limits (statics). It missed the data-column response limits, which are still recomputed by building and encoding a full-size sidecar on the column sync hot path.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lighthouse#6595](https://github.com/sigp/lighthouse/pull/6595)

</details>


<a id="rpc-028"></a>
<details>
<summary><b>rpc-028</b> Share proposer signature check across RPC column sidecars — <i>n/a · medium · cpu</i></summary>

**Idea.** When verifying data column sidecars received over by-root/by-range RPC, cache the verified signed block header (LRU keyed by header) so all columns of one block share a single BLS verification.

**Impact.** Lighthouse's RPC column path performs no proposer BLS check at all (columns are tied to the requested block root, KZG-verified in batch), so there is no repeated signature to share.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context/requests/data_columns_by_root.rs:57`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/requests/data_columns_by_root.rs#L57) RPC columns matched to requested block_root only
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1122`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1122) verify_kzg_for_data_column_list does KZG only, no header signature
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1185`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1185) verify_proposer_and_signature is gossip path only

**Sources.** [teku#10042](https://github.com/Consensys-Incorporated/teku/pull/10042)

</details>


<a id="rpc-029"></a>
<details>
<summary><b>rpc-029</b> Cancel response producer when consumer stops early — <i>not · low · M · cpu, bandwidth, memory</i></summary>

**Idea.** When a req/resp stream consumer stops early, propagate cancellation to the producer so it stops reading the DB, decompressing and copying chunks that will be dropped, and release rate limiter slots at once.

**Gap in Lighthouse.** Handlers would need a cancellation signal (e.g. a token or send-failure/closed-stream check from the RPC handler back to the beacon processor) checked in each per-block loop in handle_blocks_by_range/root and handle_data_columns_by_*; also release the inbound limiter slot early.

**Impact.** Saves DB reads and compression for requests whose peer reset or disconnected; only matters under abusive or flaky peers, small on a typical node.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:217-285`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L217-L285) blocks_by_root loop keeps reading and sending with no check that the stream/peer is gone
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1800-1860`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1800-L1860) data_columns_by_range loop sends via network_tx unbounded with no cancellation check

**Sources.** [lodestar#10304](https://github.com/ChainSafe/lodestar/pull/10304)

</details>


<a id="rpc-030"></a>
<details>
<summary><b>rpc-030</b> Validate and cap by-range request counts before DB reads — <i>implemented · medium · S · bandwidth, cpu, disk</i></summary>

**Idea.** Validate and clamp blocks/blobs/columns by-range and by-root request counts (and column counts) to spec maxima and the available range before any DB reads, and stop the read loop at the cap. A single request then cannot force unbounded reads and responses.

**Impact.** Oversized requests are rejected in the RPC handler before any DB read, and responses stop at the cap.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/handler.rs:923-983`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L923-L983) on_fully_negotiated_inbound rejects BlocksByRange/BlobsByRange/PayloadEnvelopesByRange/DataColumnsByRange above spec maxima before the request reaches the processor
- [`beacon_node/lighthouse_network/src/rpc/handler.rs:987-1010`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L987-L1010) max_remaining_chunks = max_responses stops the response at the cap
- [`beacon_node/lighthouse_network/src/rpc/rate_limiter.rs:388-397`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/rate_limiter.rs#L388-L397) tokens = max_responses charged up front
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1615-1640`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1615-L1640) blobs-by-range cap plus clamp at Fulu fork and DA boundary
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1779`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1779) data columns cap; 1848-1853 only custodied columns read
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:329-330`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L329-L330) by-head clamp
- [`beacon_node/lighthouse_network/src/rpc/codec.rs:543`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L543) by-root lists bounded at decode

**Skeptic check.** Upheld. The earlier impact text was wrong to say blocks-by-range relies only on the rate limiter: handler.rs:925 has an explicit count check against max_request_blocks, the same as for blobs, columns and envelopes.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#2309](https://github.com/Consensys-Incorporated/teku/pull/2309), [nimbus#915](https://github.com/status-im/nimbus-eth2/pull/915), [nimbus#7594](https://github.com/status-im/nimbus-eth2/pull/7594), [teku#9085](https://github.com/Consensys-Incorporated/teku/pull/9085), [nimbus#8958](https://github.com/status-im/nimbus-eth2/pull/8958), [lodestar#8248](https://github.com/ChainSafe/lodestar/pull/8248)

</details>


<a id="rpc-031"></a>
<details>
<summary><b>rpc-031</b> Read wide column by-range requests in bounded batches — <i>implemented · low · S · memory, disk</i></summary>

**Idea.** In data column by-range handlers, read from the DB in batches no wider than the configured block batch limit while still covering the full request range, so wide requests do not trigger one huge synchronous read.

**Impact.** Same effect: reads are per item and interleaved with sends, so a wide request is never one huge synchronous read.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1779-1784`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1779-L1784) request capped by max_request_data_column_sidecars
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1833-1860`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1833-L1860) per-root per-column get_data_column with each sidecar sent immediately

**Skeptic check.** Verified reads are per (root, column) and streamed; there is no bulk range read to batch. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#17331](https://github.com/OffchainLabs/prysm/pull/17331)

</details>


<a id="rpc-032"></a>
<details>
<summary><b>rpc-032</b> Lower rate-limit quota cost for blob sidecars — <i>implemented · low · S · bandwidth</i></summary>

**Idea.** Charge blob sidecars a much smaller inbound rate-limit quota cost than full blocks, so serving syncing peers is not throttled by blob count.

**Impact.** Blob and column requests are charged against their own buckets, so blob count never uses up the block quota; a peer can sync 128 slots of blocks plus blobs per window.

**Best measured result.** None (pr:nimbus#6120)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/rate_limiter.rs:398-415`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/rate_limiter.rs#L398-L415) separate token bucket per protocol (bbrange_rl vs blbrange_rl / dcbrange_rl)
- [`beacon_node/lighthouse_network/src/rpc/config.rs:74-75`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/config.rs#L74-L75) inbound blobs quotas 1152/13s, sized to one full MAX_REQUEST_BLOB_SIDECARS request
- [`beacon_node/lighthouse_network/src/rpc/config.rs:148-151`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/config.rs#L148-L151) data columns 16384/10s
- [`beacon_node/lighthouse_network/src/rpc/methods.rs:387-390`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/methods.rs#L387-L390) blob cost = count * max_blobs_per_block

**Skeptic check.** The mechanism is different from Nimbus (separate per-protocol buckets instead of a lower per-blob weight in one shared budget), but the effect is the same: serving blobs does not throttle block serving. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#6120](https://github.com/status-im/nimbus-eth2/pull/6120)

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

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [lighthouse#5138](https://github.com/sigp/lighthouse/pull/5138), [teku#7787](https://github.com/Consensys-Incorporated/teku/pull/7787), [lighthouse#4136](https://github.com/sigp/lighthouse/pull/4136)

</details>


<a id="rpc-034"></a>
<details>
<summary><b>rpc-034</b> Stream by-range/by-root responses chunk by chunk from DB — <i>partial · medium · M · latency, memory, sync</i></summary>

**Idea.** Serve blocks by range/root by streaming items from the DB iterator to the network encoder and writing each as a separate chunk as it is produced, instead of collecting the whole response in memory first. This bounds memory and lets the first chunk go out early.

**Gap in Lighthouse.** BeaconBlockStreamer::stream (used by BlocksByRange, BlocksByRoot and BlocksByHead through get_blocks/get_blocks_checking_caches) materializes the whole response: all load_block results and then all EL payload bodies before the first sender.send. Up to 1024 blinded blocks plus their payloads sit in memory, and the first chunk waits for the slowest DB read and EL call. Fix: load and send in chunks of 32 roots (load chunk, fetch its bodies, send, repeat), or pipeline loads with sends.

**Impact.** Lower peak memory per blocks-by-range request and an earlier first chunk (time-to-first-byte) for syncing peers, mainly when payloads must be rebuilt from the EL.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_block_streamer.rs:257-271`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_block_streamer.rs#L257-L271) stream() loads every requested block into a Vec in one spawn_blocking task (collect) before yielding anything
- [`beacon_node/beacon_chain/src/beacon_block_streamer.rs:285`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_block_streamer.rs#L285) fetch_payload_bodies for all blinded blocks (in 32-hash chunks, but all awaited) before the first send
- [`beacon_node/beacon_chain/src/beacon_block_streamer.rs:297-318`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_block_streamer.rs#L297-L318) sends start only after all loads and EL fetches finish
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1180-1194`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1180-L1194) handler sends one chunk per stream item (this part matches)
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1695-1720`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1695-L1720) blobs-by-range and 1855-1870 data-columns-by-range do read and send item by item

**Skeptic check.** Each block is a separate chunk on the wire, and blobs and columns do stream from the DB. But the block streamer the earlier evidence cites collects all blocks and all payload bodies before it yields, so the 'stream' interface does not give the bounded-memory or early-first-chunk effect.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [prysm#3528](https://github.com/OffchainLabs/prysm/pull/3528), [lodestar#622](https://github.com/ChainSafe/lodestar/pull/622), [lodestar@c03541065](https://github.com/ChainSafe/lodestar/commit/c03541065648), [lodestar#684](https://github.com/ChainSafe/lodestar/pull/684), [lodestar@c7978049f](https://github.com/ChainSafe/lodestar/commit/c7978049f2a6)

</details>


<a id="rpc-035"></a>
<details>
<summary><b>rpc-035</b> Clear request timeout timers and abort listeners on completion — <i>implemented · low · S · memory, latency, cpu</i></summary>

**Idea.** Remove the request/response timeout timer and abort-signal/cancellation listeners as soon as the response stream completes or is aborted. Otherwise finished requests are later reported as timeouts and timers/closures accumulate per request.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/handler.rs:745`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L745),774,793 outbound_substreams_delay.remove on stream end, error and close
- [`beacon_node/lighthouse_network/src/rpc/handler.rs:500`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L500),574,608 inbound_substreams_delay.remove on completion
- [`beacon_node/lighthouse_network/src/rpc/handler.rs:416-446`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L416-L446) only entries still present can expire as StreamTimeout

**Skeptic check.** Verified that timers live in per-handler DelayQueues, and that the keys are removed on every completion path (and reset on each chunk), so finished requests are never reported as timeouts. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#2804](https://github.com/sigp/lighthouse/pull/2804), [lodestar#9029](https://github.com/ChainSafe/lodestar/pull/9029), [lodestar@f0caf77f5](https://github.com/ChainSafe/lodestar/commit/f0caf77f50a5), [lodestar@765885746](https://github.com/ChainSafe/lodestar/commit/765885746a06)

</details>


<a id="rpc-036"></a>
<details>
<summary><b>rpc-036</b> Write response code, length and payload together — <i>implemented · low · S · latency, bandwidth</i></summary>

**Idea.** Write the req/resp response code and length prefix in the same write as the payload instead of separate writes, so each response chunk needs fewer network packets.

**Impact.** None: each chunk is one buffer handed to the framed sink.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/codec.rs:141-150`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L141-L150) encode() puts the response code into dst
- [`beacon_node/lighthouse_network/src/rpc/codec.rs:117-134`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L117-L134) context bytes, varint length and snappy payload appended to the same dst BytesMut

**Skeptic check.** Verified code, context bytes, length prefix and payload are encoded into one BytesMut per chunk. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus@a83aa8364](https://github.com/status-im/nimbus-eth2/commit/a83aa83644ca)

</details>


<a id="rpc-037"></a>
<details>
<summary><b>rpc-037</b> Snappy-compress RPC responses directly into destination buffer — <i>not · low · S · memory, cpu</i></summary>

**Idea.** Compress RPC responses through a writer straight into the output/destination buffer instead of into a temporary Vec, removing one allocation and copy per response.

**Gap in Lighthouse.** Replace the temporary Vec with FrameEncoder::new(dst.writer()) in SSZSnappyInboundCodec::encode_response (and outbound request encode), keeping the flush; PR 10410 does this.

**Impact.** Removes one allocation and one memcpy per response chunk (up to ~128 KiB for blocks/columns); small CPU and allocator gain on serving nodes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/codec.rs:127-131`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L127-L131) FrameEncoder::new(Vec::new()) then extend_from_slice(writer.get_ref()) copies into dst (same at :389 for requests)
- pr:lighthouse#10410 is OPEN (not merged) at the checked commit

**Sources.** [lighthouse#10410](https://github.com/sigp/lighthouse/pull/10410)

</details>


<a id="rpc-038"></a>
<details>
<summary><b>rpc-038</b> Outbound self rate limiter capping concurrent requests per peer — <i>implemented · medium · S · bandwidth, latency, sync</i></summary>

**Idea.** Queue or fail locally outgoing RPC requests to a peer, per protocol (e.g. max 2 concurrent in flight), so they stay under the peer's inbound limits. Peers are not flooded, slow responses do not pile up, and rejected requests need no retry.

**Impact.** None, already done.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/mod.rs:51`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/mod.rs#L51) MAX_CONCURRENT_REQUESTS = 2
- [`beacon_node/lighthouse_network/src/rpc/self_limiter.rs:90-118`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/self_limiter.rs#L90-L118) requests queued per (peer, protocol) behind earlier queued ones
- [`beacon_node/lighthouse_network/src/rpc/self_limiter.rs:127-146`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/self_limiter.rs#L127-L146) try_send_request delays when 2 in flight (unconditional), then optional token-bucket check

**Skeptic check.** The concurrency cap applies whether or not the outbound rate limiter config is set, and requests are queued, not dropped. This matches the idea.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#8912](https://github.com/Consensys-Incorporated/teku/pull/8912), [lighthouse@493784366](https://github.com/sigp/lighthouse/commit/493784366f3d), [lodestar#8185](https://github.com/ChainSafe/lodestar/pull/8185)

</details>


<a id="rpc-039"></a>
<details>
<summary><b>rpc-039</b> Load justified state from DB by root — <i>n/a · low · S · cpu, latency</i></summary>

**Idea.** Fetch the justified state directly from the database by its root instead of regenerating it from state block roots when serving requests.

**Impact.** Lighthouse already loads the justified state from the store by root and caches balances; no request path regenerates it from block roots.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_fork_choice_store.rs:55`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_fork_choice_store.rs#L55),78,100 justified balances cached (JustifiedBalancesCache keyed by block root) and loaded from the store by state root at :217-220
- Lighthouse req/resp does not serve the justified state

**Sources.** [prysm#2154](https://github.com/OffchainLabs/prysm/pull/2154)

</details>


<a id="rpc-040"></a>
<details>
<summary><b>rpc-040</b> Run sync-response DB reads on blocking threads — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Run database reads for blocks-by-range/root responses on blocking worker threads off the core async executor, so large responses run in parallel and do not stall networking.

**Impact.** None, already done.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1124-1140`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1124-L1140) roots via spawn_blocking_handle
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:347-355`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L347-L355) by-head ancestor walk on blocking thread
- [`beacon_node/beacon_chain/src/beacon_block_streamer.rs:257-271`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_block_streamer.rs#L257-L271) block loads on spawn_blocking_handle
- [`beacon_node/beacon_chain/src/payload_envelope_streamer/mod.rs:126`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_streamer/mod.rs#L126) envelope loads on spawn_blocking_handle
- [`beacon_node/network/src/network_beacon_processor/mod.rs:811`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L811),863 blobs/columns by range run as blocking beacon-processor work

**Skeptic check.** Checked every by-range and by-root handler: DB reads happen on blocking threads or blocking beacon-processor workers, never on the async executor.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#1909](https://github.com/sigp/lighthouse/pull/1909)

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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [prysm#2541](https://github.com/OffchainLabs/prysm/pull/2541)

</details>


<a id="rpc-042"></a>
<details>
<summary><b>rpc-042</b> Decode snappy frames directly into one destination buffer — <i>partial · low · M · memory, cpu, bandwidth</i></summary>

**Idea.** Decompress framed snappy req/resp payloads straight into one final output buffer sized from the advertised length, without intermediate slices or composite buffers that are re-summed or re-copied, and abort as soon as the payload exceeds the expected size.

**Gap in Lighthouse.** SSZSnappyInboundCodec::decode and SSZSnappyOutboundCodec::decode restart from the start of the chunk on every call. While a multi-MB block or column chunk is still arriving, each socket read allocates a new zeroed `length` buffer and decompresses all frames received so far, then throws the result away on UnexpectedEof. That is O(n^2) decompress and memset work per chunk, which is what teku#11587/#11589 remove. Fix: keep a persistent FrameDecoder state and output buffer in the codec across decode calls (decode each complete snappy frame once and append), or wait until max_compress_len bytes or a complete frame sequence is buffered before decoding.

**Impact.** Less CPU and allocation when receiving large by-range responses (blocks up to 10 MiB, data columns) that arrive over many reads.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/codec.rs:182-190`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L182-L190) vec![0; length] + FrameDecoder over Take(max_compress_len) + read_exact (single destination, size-bounded: matches)
- [`beacon_node/lighthouse_network/src/rpc/codec.rs:279-292`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L279-L292) same for responses
- [`beacon_node/lighthouse_network/src/rpc/codec.rs:451-462`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L451-L462) UnexpectedEof on incomplete input returns Ok(None) and discards the work
- tokio-util-0.7.19/src/codec/framed_impl.rs:202-221 Framed calls decode() again after every socket read

**Skeptic check.** The earlier evidence is right that there is one destination buffer sized from the advertised length, with an early abort past max_compress_len. It missed that the decode is not incremental: Framed calls decode after every read, and each call re-decompresses everything from scratch.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [nimbus@a605c7244](https://github.com/status-im/nimbus-eth2/commit/a605c7244e14), [nimbus#1018](https://github.com/status-im/nimbus-eth2/pull/1018), [teku#11587](https://github.com/Consensys-Incorporated/teku/pull/11587), [teku#11589](https://github.com/Consensys-Incorporated/teku/pull/11589)

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


<a id="rpc-044"></a>
<details>
<summary><b>rpc-044</b> Stop ancestor walk at already-requested roots — <i>n/a · low · S · bandwidth, cpu</i></summary>

**Idea.** When serving ancestor-block requests for several roots, stop walking a chain once it reaches a root that is also requested and cap the response, so the same blocks are not read and sent twice.

**Impact.** Nimbus 2019 ancestor-block walk has no counterpart; BlocksByHead is already capped and deduped.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:197-285`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L197-L285) BlocksByRoot returns exactly the requested roots from caches/DB with no ancestor walk
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:453-520`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L453-L520) BlocksByHead walks proto-array/freezer with dedup on insert and a count cap

**Sources.** [nimbus#254](https://github.com/status-im/nimbus-eth2/pull/254)

</details>


<a id="rpc-045"></a>
<details>
<summary><b>rpc-045</b> Compute each validator status once in duties — <i>n/a · low · S · cpu</i></summary>

**Idea.** In the get-duties API handler compute each validator's status once and reuse it for the assignment, instead of calling the status lookup twice.

**Impact.** Lighthouse duties endpoints do not compute validator status, so the double lookup does not exist.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/attester_duties.rs:15`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L15) duties looked up by index, no per-validator status computed

**Sources.** [prysm#8313](https://github.com/OffchainLabs/prysm/pull/8313)

</details>


<a id="rpc-046"></a>
<details>
<summary><b>rpc-046</b> Snappy-compress req/resp payloads by default — <i>implemented · low · S · bandwidth</i></summary>

**Idea.** Compress SSZ req/resp (and gossip) payloads with framed snappy, enabled by default, to cut bytes on the wire.

**Impact.** Already default; nothing to gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/codec.rs:126-131`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L126-L131) FrameEncoder on every RPC chunk
- [`beacon_node/lighthouse_network/src/types/pubsub.rs:149-150`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L149-L150) raw snappy compress for gossip

**Skeptic check.** Snappy is the only encoding for both req/resp and gossip; it is not optional. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#2552](https://github.com/Consensys-Incorporated/teku/pull/2552), [teku#1584](https://github.com/Consensys-Incorporated/teku/pull/1584), [teku#1670](https://github.com/Consensys-Incorporated/teku/pull/1670), [lighthouse#866](https://github.com/sigp/lighthouse/pull/866), [nimbus@75c1c6a95](https://github.com/status-im/nimbus-eth2/commit/75c1c6a95c24)

</details>


<a id="rpc-047"></a>
<details>
<summary><b>rpc-047</b> Copy uncompressed snappy chunks directly to destination — <i>not · low · M · cpu, latency, memory</i></summary>

**Idea.** For snappy frames marked uncompressed, copy the payload bytes straight from the stream into the output buffer instead of through the decoder or an intermediate decompress buffer; also avoid re-parsing multistream headers.

**Gap in Lighthouse.** Lighthouse uses the snap crate FrameDecoder, which reads uncompressed chunks into its own buffer first and copies out. Fixing needs a custom frame reader or patched snap in rpc/codec.rs decode paths.

**Impact.** One extra memcpy only for incompressible chunks (rare, mostly small); negligible on a mainnet node.

**Evidence (Lighthouse @ 928b61e719).**

- snap-1.1.2/src/read.rs:188 uncompressed chunk read_exact into internal dst then copied to caller
- [`beacon_node/lighthouse_network/src/rpc/codec.rs:316`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L316) FrameDecoder over limit reader into vec

**Sources.** [silver#102](https://github.com/gattaca-com/silver/pull/102), [silver#91](https://github.com/gattaca-com/silver/pull/91)

</details>


<a id="rpc-048"></a>
<details>
<summary><b>rpc-048</b> Disable HTTP pipelining in the API server — <i>implemented · low · S · latency</i></summary>

**Idea.** Disable HTTP pipelining by default in the beacon API HTTP server so one slow request does not block later requests on the same connection.

**Impact.** Pipelining is off by default for the beacon API server in the warp fork Lighthouse uses.

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.toml:305 warp patched to macladson fork rev 6f5f21b
- 6f5f21b/src/server.rs:23 pipeline: false default
- 6f5f21b/src/server.rs:333 hyper http1 pipeline_flush(pipeline)
- 6f5f21b/src/server.rs:391 same on the TLS path

**Skeptic check.** Checked that the Cargo.lock warp source is the 6f5f21b fork checkout and that both the plain and TLS serve paths pass pipeline=false to hyper. Earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#4950](https://github.com/status-im/nimbus-eth2/pull/4950)

</details>


<a id="rpc-049"></a>
<details>
<summary><b>rpc-049</b> Refuse validator API requests while node is syncing — <i>implemented · medium · S · cpu, sync</i></summary>

**Idea.** Do not serve duty and state validator API requests while the node is syncing, so they do not compete with sync for CPU.

**Impact.** None, already done.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs:475`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L475) not_while_syncing_filter rejects when SyncingFinalized/SyncingHead and head is beyond sync_tolerance_epochs
- [`beacon_node/http_api/src/validator/mod.rs:78`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L78) filter applied to duties and other validator endpoints (also :125, :161, :197, :335, :471, :539, ...)

**Skeptic check.** Verified the warp filter returns not_synced during range/head sync and is chained onto the validator duty/production endpoints. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#2353](https://github.com/OffchainLabs/prysm/pull/2353)

</details>


<a id="rpc-050"></a>
<details>
<summary><b>rpc-050</b> Compute committee assignments via index lookup, no pubkey scan — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** For committee assignment queries, look up requested validators by index and compute assignments directly, instead of filtering all pubkeys for active status in O(n).

**Impact.** Duties computed per requested index from the shuffling cache, no scan over all pubkeys.

**Best measured result.** None (pr:prysm#2787)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/attester_duties.rs:15`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L15) attester_duties takes request_indices
- [`beacon_node/http_api/src/attester_duties.rs:60`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L60) cached_attestation_duties calls validator_attestation_duties
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1735`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1735) validator_attestation_duties uses cached shuffling committee_cache.get_attestation_duties(validator_index) per requested index

**Skeptic check.** Confirmed per-index lookup in the committee cache (shuffling positions), with no O(n) active-pubkey filtering. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#2787](https://github.com/OffchainLabs/prysm/pull/2787)

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


<a id="rpc-052"></a>
<details>
<summary><b>rpc-052</b> Avoid copying encoded request buffers before send — <i>not · low · S · memory, cpu</i></summary>

**Idea.** Pass SSZ-snappy encoded request buffers to the RPC send path without copying them when the callee does not retain them, cutting allocations and GC pressure.

**Gap in Lighthouse.** Request encode allocates an SSZ Vec then snappy-frames into dst; could encode into a reused buffer in the outbound codec encode(). Requests are tiny and infrequent.

**Impact.** Saves one small allocation per outbound request; unmeasurable.

**Best measured result.** None (pr:caplin#17792)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/codec.rs:339`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L339) encode() builds as_ssz_bytes Vec then compresses into dst

**Sources.** [caplin#17792](https://github.com/erigontech/erigon/pull/17792)

</details>


<a id="rpc-053"></a>
<details>
<summary><b>rpc-053</b> Drop queued requests from disconnected peers — <i>implemented · low · S · cpu</i></summary>

**Idea.** Before processing a queued inbound RPC request, drop it if the requesting peer has already disconnected.

**Impact.** Requests from peers that are already gone do not reach the beacon processor.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/service.rs:1014-1018`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L1014-L1018) handle_rpc_request drops requests when peers.is_connected(peer_id) is false
- [`beacon_node/lighthouse_network/src/rpc/mod.rs:370-374`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/mod.rs#L370-L374) inbound_request_limiter.connection_closed drops delayed requests on connection close

**Skeptic check.** The source PR (lighthouse#1919) adds exactly this is_connected check in handle_rpc_request, and it is still present. The rate limiter also drops requests it delayed when the connection closes. Requests already in the beacon processor queue are not checked again when a worker picks them up, so a small residual case remains, but the idea's mechanism is there.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#1919](https://github.com/sigp/lighthouse/pull/1919)

</details>


<a id="rpc-054"></a>
<details>
<summary><b>rpc-054</b> Reject blob requests for post-Fulu slots early — <i>partial · low · S · cpu, disk</i></summary>

**Idea.** Reject BlobsByRange/ByRoot requests for slots at or after the data-column fork before any store lookup, since those blobs cannot exist.

**Gap in Lighthouse.** By-range rejects before any lookup. By-root only skips ids whose block is in DA checker or early attester cache; unknown roots still hit blob lookups/store. Could resolve slot from fork choice in handle_blobs_by_root_request_inner.

**Impact.** Avoids a few DB misses on by-root blob requests for post-Fulu blocks; small.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:684`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L684) fulu_start_slot in by-root, skip only if block slot found in cache
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1625`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1625) by-range returns early/truncates count at fulu start

**Sources.** [lighthouse#7328](https://github.com/sigp/lighthouse/pull/7328), [lighthouse#7756](https://github.com/sigp/lighthouse/pull/7756)

</details>


<a id="rpc-055"></a>
<details>
<summary><b>rpc-055</b> Free every per-peer rate limiter state for disconnected peers — <i>implemented · medium · S · memory</i></summary>

**Idea.** Remove a peer's RPC rate-limiter buckets on disconnect, and prune every per-protocol limiter (including light-client protocols) on a timer, so entries for disconnected peers do not live for the node's lifetime.

**Impact.** None, already done; bucket entries of a gone peer are freed at most one replenish window after disconnect.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/rate_limiter.rs:425`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/rate_limiter.rs#L425) prune() destructures and prunes every protocol limiter incl. light client
- [`beacon_node/lighthouse_network/src/rpc/rate_limiter.rs:553`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/rate_limiter.rs#L553) Limiter::prune drops keys whose bucket has refilled
- [`beacon_node/lighthouse_network/src/rpc/rate_limiter.rs:474`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/rate_limiter.rs#L474) 30s prune interval driven by poll
- [`beacon_node/lighthouse_network/src/rpc/inbound_limiter.rs:324`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/inbound_limiter.rs#L324) inbound limiter polls the RPCRateLimiter (prune)
- [`beacon_node/lighthouse_network/src/rpc/self_limiter.rs:233`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/self_limiter.rs#L233) peer_disconnected clears active/ready/delayed state
- [`beacon_node/lighthouse_network/src/rpc/mod.rs:373`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/mod.rs#L373) connection_closed / peer_disconnected on ConnectionClosed

**Skeptic check.** Token buckets are not removed on disconnect, but the timer prune covers all protocols and removes any peer whose bucket is full, so no entry lives for the node lifetime; queue state is cleared on disconnect. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#16916](https://github.com/OffchainLabs/prysm/pull/16916), [lighthouse#8058](https://github.com/sigp/lighthouse/pull/8058)

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


<a id="rpc-057"></a>
<details>
<summary><b>rpc-057</b> Fewer async stream pipe layers in req/resp — <i>n/a · low · S · cpu, latency</i></summary>

**Idea.** Remove async-iterator pipe layers in the req/resp request and response paths, e.g. by folding timeout handling into the main loop, to cut per-chunk async overhead.

**Impact.** JS async iterator overhead has no Rust equivalent.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/handler.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs) async state machine, no async-iterator pipe layers

**Sources.** [lodestar#4385](https://github.com/ChainSafe/lodestar/pull/4385), [lodestar#4345](https://github.com/ChainSafe/lodestar/pull/4345)

</details>


<a id="rpc-058"></a>
<details>
<summary><b>rpc-058</b> Filter column requests to custody columns before DB — <i>implemented · medium · S · disk, cpu, bandwidth</i></summary>

**Idea.** Filter DataColumnsByRoot/ByRange requests to the columns the node custodies before hitting the database, so requests for non-custodied columns do not cause lookups that always miss.

**Impact.** None, already done.

**Best measured result.** None (pr:lighthouse#7897)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:824`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L824) by-root filters requested columns to custody_columns_for_epoch before get_data_columns_checking_all_caches
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1840`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1840) by-range filters req.columns to custody columns before the per-block get_data_column loop

**Skeptic check.** Both handlers filter to custody columns before any DB access. Earlier evidence was right; a separate residual (by-range still probes custody columns for blocks with zero blob commitments) is not this idea.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#7897](https://github.com/sigp/lighthouse/pull/7897), [grandine@31108d74e](https://github.com/grandinetech/grandine/commit/31108d74e0a3), [lighthouse#7942](https://github.com/sigp/lighthouse/pull/7942)

</details>


<a id="rpc-059"></a>
<details>
<summary><b>rpc-059</b> Filter by-range sidecar responses to requested slots — <i>implemented · low · S · bandwidth</i></summary>

**Idea.** Filter blob and data column by-range responses to the requested slot range so items outside it are not sent.

**Impact.** By-range responses for blobs, columns, blocks and envelopes contain only items in the requested slots.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1700-1701`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1700-L1701) blob sidecars filtered to [start_slot, start_slot+effective_count)
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1861-1862`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1861-L1862) data column sidecars filtered to the requested range
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1386`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1386) skip-slot first root dropped in get_block_roots_from_store
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1187`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1187) blocks also filtered
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1512-1513`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1512-L1513) payload envelopes filtered

**Skeptic check.** Confirmed the slot-range checks on both the blob and data column by-range serving paths, and the matching checks for blocks and envelopes. Earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#7611](https://github.com/sigp/lighthouse/pull/7611)

</details>


<a id="rpc-060"></a>
<details>
<summary><b>rpc-060</b> Half-close request stream after sending request — <i>implemented · medium · S · sync, latency</i></summary>

**Idea.** After writing an RPC request, half-close the write side of the stream as the spec requires so the responder starts processing at once, and use per-chunk response timeouts instead of one total timeout.

**Impact.** None, already done.

**Best measured result.** None (pr:nimbus#1621)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/outbound.rs:65`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/outbound.rs#L65) socket.send(req) then socket.close() half-closes write side
- [`beacon_node/lighthouse_network/src/rpc/handler.rs:711`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L711) outbound RESP_TIMEOUT reset per received chunk
- [`beacon_node/lighthouse_network/src/rpc/handler.rs:545`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L545) inbound per-chunk timer reset

**Skeptic check.** Outbound upgrade closes the write half right after sending; timeouts are per chunk on both sides. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#1621](https://github.com/status-im/nimbus-eth2/pull/1621)

</details>


<a id="rpc-061"></a>
<details>
<summary><b>rpc-061</b> Compute by-range block roots by hashing loaded blocks — <i>implemented · medium · S · disk, latency</i></summary>

**Idea.** When serving blocks-by-range, derive each block root by hashing the blocks already loaded instead of looking each root up in the DB. DB root lookups are slow during non-finality.

**Impact.** Non-finalized roots come from in-memory fork choice, so the slow non-finality DB lookups the idea targets do not happen.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1131`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1131) roots resolved once via get_block_roots_for_slot_range before get_blocks stream
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1260`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1260) unfinalized portion from block_roots_from_fork_choice (in memory), finalized portion from store root iterator

**Skeptic check.** Different mechanism (fork choice instead of hashing loaded blocks) but same effect: during non-finality the whole unfinalized range is read from proto-array, not the DB. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#7028](https://github.com/OffchainLabs/prysm/pull/7028)

</details>


<a id="rpc-062"></a>
<details>
<summary><b>rpc-062</b> Hoist per-message timeout defaults out of hot path — <i>n/a · low · cpu</i></summary>

**Idea.** Resolve req/resp timeout and option defaults once at setup instead of evaluating fallback conditionals on every sent or handled message, cutting per-message CPU in the hottest send/handle paths.

**Impact.** JS option-fallback overhead; Rust resolves config at construction.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/config.rs:254`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/config.rs#L254) quotas resolved at config build, not per message

**Sources.** [lodestar#6801](https://github.com/ChainSafe/lodestar/pull/6801)

</details>


<a id="rpc-063"></a>
<details>
<summary><b>rpc-063</b> Do not await Goodbye response — <i>implemented · low · S · latency</i></summary>

**Idea.** Send the Goodbye RPC without waiting for a response, since the peer usually disconnects first and the response has no value; this frees the request slot and avoids waiting on a timeout.

**Impact.** The outbound Goodbye stream is dropped after it is sent. No response slot or timeout is held.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/protocol.rs:857`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/protocol.rs#L857) Goodbye max_responses = 0
- [`beacon_node/lighthouse_network/src/rpc/handler.rs:1060-1068`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L1060-L1068) outbound substream kept and RESP_TIMEOUT armed only when max_responses &gt; 0
- [`beacon_node/lighthouse_network/src/rpc/handler.rs:1024-1026`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L1024-L1026) inbound Goodbye shuts down the handler

**Skeptic check.** Verified that on_fully_negotiated_outbound drops the stream when max_responses is 0, which it is for Goodbye, so nothing waits for a reply. Earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#4905](https://github.com/ChainSafe/lodestar/pull/4905)

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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [caplin#24648](https://github.com/erigontech/erigon/pull/24648)

</details>


<a id="rpc-065"></a>
<details>
<summary><b>rpc-065</b> Validate blob responses incrementally per chunk — <i>implemented · low · S · cpu, bandwidth</i></summary>

**Idea.** Validate each blob sidecar response chunk as it is read from the stream (index order, ascending slot, block root/parent consistency, bounds) and abort on the first invalid chunk, instead of reading the full response before validating.

**Impact.** An invalid blob chunk ends the request when it arrives, before the rest of the stream is read.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context/requests/blobs_by_range.rs:27-50`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/requests/blobs_by_range.rs#L27-L50) add() checks each chunk for slot range, index bound, inclusion proof and duplicates, and returns an error
- [`beacon_node/network/src/sync/network_context/requests/data_columns_by_range.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/requests/data_columns_by_range.rs) per-chunk add() for columns

**Skeptic check.** ActiveRequestItems::add runs on each streamed chunk and also checks the inclusion proof, so a bad chunk aborts the request early, which is the effect the idea wants. Ascending-order and parent-root checks per chunk (from the Prysm PR) are absent. Block consistency is checked later during coupling, so the remaining saving is marginal.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#13511](https://github.com/OffchainLabs/prysm/pull/13511)

</details>


<a id="rpc-066"></a>
<details>
<summary><b>rpc-066</b> Interleave response chunks across concurrent substreams — <i>implemented · medium · S · latency</i></summary>

**Idea.** In the RPC handler, interleave sending chunks of responses across concurrent inbound substreams instead of sending each response fully in sequence, so long responses do not cause other streams to time out under load.

**Impact.** Each substream sends chunk by chunk with its own future, so long responses do not block others.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/handler.rs:465`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L465) every poll iterates all inbound_substreams
- [`beacon_node/lighthouse_network/src/rpc/handler.rs:473`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L473) one pending item popped into an independent Busy send future per substream

**Skeptic check.** This is the Lighthouse PR 2815 mechanism itself, present in the handler poll loop. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#2815](https://github.com/sigp/lighthouse/pull/2815)

</details>


<a id="rpc-067"></a>
<details>
<summary><b>rpc-067</b> BlobSidecarsByRange: iterate only indices with commitments — <i>implemented · low · S · disk, cpu, latency</i></summary>

**Idea.** When serving BlobSidecarsByRange, use each block's KZG commitment count to read only the blob indices that exist, instead of probing every possible blob index per slot in the DB.

**Impact.** None for the stated idea; the per-index probing cannot happen with this storage layout.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2616`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2616) get_blobs reads one BeaconBlob key holding all sidecars of a block
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1693`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1693) BlobsByRange does one get_blobs per block root and iterates only stored sidecars

**Second check.** Confirmed storage schema is one key per block root (not per index) and the range handler only iterates stored sidecars, so the per-index probing Teku fixed has no Lighthouse counterpart.

**Skeptic check.** Confirmed blobs are stored and read per block root as one list, so there is no per-index DB probing; only a single miss per zero-commitment block remains, which is negligible. Earlier evidence was right.

**Verdict history.** partial (checked) → implemented (refuted) → implemented (skeptic)

**Sources.** [teku#6949](https://github.com/Consensys-Incorporated/teku/pull/6949)

</details>


<a id="rpc-068"></a>
<details>
<summary><b>rpc-068</b> Upgrade JSON-RPC library for engine API client — <i>n/a · low · memory, cpu</i></summary>

**Idea.** Use a JSON-RPC library version with lower memory use and faster encoding/decoding for the engine API connection to the EL.

**Impact.** Nim-specific library choice.

**Best measured result.** None (pr:nimbus#7754)

**Evidence (Lighthouse @ 928b61e719).**

- Lighthouse engine API uses reqwest and serde_json, not the Nim JSON-RPC library

**Sources.** [nimbus#7746](https://github.com/status-im/nimbus-eth2/pull/7746), [nimbus#7754](https://github.com/status-im/nimbus-eth2/pull/7754)

</details>


<a id="rpc-069"></a>
<details>
<summary><b>rpc-069</b> Charge rate limiter for full request count upfront — <i>implemented · high · S · cpu, memory, bandwidth</i></summary>

**Idea.** Charge the inbound rate limiter the maximum response count (request count) when the request arrives, before any DB read, EL payload reconstruction or encoding, so over-limit requests are rejected before work is done and one token cannot buy many expensive responses.

**Impact.** Over-quota requests are delayed or rejected in the RPC behaviour before any DB read, EL reconstruction or encoding.

**Best measured result.** None (pr:prysm#17655)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/rate_limiter.rs:388-399`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/rate_limiter.rs#L388-L399) allows() charges max_responses tokens (minimum 1)
- [`beacon_node/lighthouse_network/src/rpc/protocol.rs:854-874`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/protocol.rs#L854-L874) max_responses = count, count*max_blobs, count*columns, roots len
- [`beacon_node/lighthouse_network/src/rpc/methods.rs:387-390`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/methods.rs#L387-L390) and 405-407 saturating count multipliers
- [`beacon_node/lighthouse_network/src/rpc/mod.rs:429-444`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/mod.rs#L429-L444) inbound_request_limiter.allows runs on arrival, before deliver_request; requests are delayed or rejected
- [`beacon_node/lighthouse_network/src/rpc/inbound_limiter.rs:162-170`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/inbound_limiter.rs#L162-L170) requests larger than the quota are rejected

**Skeptic check.** Confirmed that the inbound limiter charges the full response count when the request arrives, in the behaviour layer, before the request reaches the router or beacon processor. This covers blocks, blobs and columns (count times columns) and payload envelopes. Earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@b7a6e6406](https://github.com/sigp/lighthouse/commit/b7a6e64066d3), [prysm#17655](https://github.com/OffchainLabs/prysm/pull/17655)

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

**Verdict history.** not (checked) → partial (refuted)

**Sources.** [nimbus#4254](https://github.com/status-im/nimbus-eth2/pull/4254)

</details>


<a id="rpc-072"></a>
<details>
<summary><b>rpc-072</b> Prioritize Status handling over heavy requests — <i>implemented · low · S · latency, sync</i></summary>

**Idea.** Process inbound Status messages ahead of heavy by-range/by-root requests in the RPC handling queue, so handshakes are not delayed behind expensive work.

**Impact.** Status replies go out without any queue, and status processing outranks heavy by-range and by-root work.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:1105-1124`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1105-L1124) status_queue popped before block/blob/column by-range and by-root queues
- [`beacon_node/network/src/service.rs:1126-1139`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L1126-L1139) on_status_request sends the Status reply directly from the network service, without queuing

**Skeptic check.** Verified the beacon processor pop order. The network service also answers Status inline, so the handshake response never waits behind heavy requests. Earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine@ae1b91068](https://github.com/grandinetech/grandine/commit/ae1b91068f29)

</details>


<a id="rpc-073"></a>
<details>
<summary><b>rpc-073</b> Prefer Status v2 in protocol list — <i>implemented · low · S · latency, sync</i></summary>

**Idea.** List the newest Status protocol version first in the supported RPC protocols, so handshakes negotiate the newer version directly.

**Impact.** Inbound and outbound negotiation both try Status v2 first.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/protocol.rs:423-424`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/protocol.rs#L423-L424) inbound currently_supported lists StatusV2 before StatusV1
- [`beacon_node/lighthouse_network/src/rpc/protocol.rs:949-952`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/protocol.rs#L949-L952) outbound supported_protocols for Status lists V2 first
- [`beacon_node/network/src/status.rs:46`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/status.rs#L46) status message built as V2

**Skeptic check.** Checked both the inbound protocol list and the outbound protocol list for Status requests. V2 comes first in both. Earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine#261](https://github.com/grandinetech/grandine/pull/261)

</details>


<a id="rpc-074"></a>
<details>
<summary><b>rpc-074</b> Quadratic rate-limit cost for BlocksByRange step — <i>implemented · low · S · cpu, disk</i></summary>

**Idea.** Charge BlocksByRange rate-limit tokens quadratically in the step parameter and saturate start+count*step, so requests with large skips cannot force long chain walks cheaply.

**Impact.** A large step cannot force a long chain walk: at most one block is served while the limiter still charges by count, so the cost is bounded without a quadratic charge.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/service.rs:1023-1034`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L1023-L1034) step&gt;1 clamps count to 1 and rewrites to a step-1 BlocksByRangeRequest
- [`beacon_node/lighthouse_network/src/service/mod.rs:1673-1684`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L1673-L1684) step==0 penalises peer and drops request
- [`beacon_node/lighthouse_network/src/rpc/methods.rs:470-486`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/methods.rs#L470-L486) served request type has fixed step 1

**Skeptic check.** Verified the step clamp in handle_rpc_request and the step==0 rejection; the mechanism differs from a quadratic charge but removes the same attack, so the earlier verdict stands.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#1583](https://github.com/sigp/lighthouse/pull/1583)

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

**Verdict history.** not (checked) → partial (refuted)

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

**Verdict history.** not (checked) → partial (refuted)

**Sources.** [prysm#15205](https://github.com/OffchainLabs/prysm/pull/15205)

</details>


<a id="rpc-077"></a>
<details>
<summary><b>rpc-077</b> Read request before applying quota on mplex — <i>implemented · low · S · latency, bandwidth</i></summary>

**Idea.** Read the inbound request message fully before waiting on the rate quota, because on a multiplexed connection an unread message blocks the whole connection.

**Impact.** The request is already read before the quota wait, so a delayed request does not block the connection.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/mod.rs:418-440`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/mod.rs#L418-L440) inbound limiter is applied to HandlerEvent::Ok(Request) after the handler has fully decoded the request; Admission::Delayed queues it inside the limiter
- [`beacon_node/lighthouse_network/src/rpc/handler.rs:395-436`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L395-L436) handler continues polling other substreams independently

**Skeptic check.** Confirmed the limiter runs in the behaviour on already-decoded requests, so the stream reader is never held by the quota wait; earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#4697](https://github.com/status-im/nimbus-eth2/pull/4697)

</details>


<a id="rpc-078"></a>
<details>
<summary><b>rpc-078</b> Drop inbound substream on response timeout — <i>implemented · low · S · memory</i></summary>

**Idea.** When an inbound RPC substream's response timeout expires, remove it at once and cancel the in-flight send and queued responses so memory is reclaimed.

**Impact.** Memory of timed-out inbound substreams is reclaimed immediately.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/handler.rs:413-436`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L413-L436) expired inbound substreams are removed from inbound_substreams at once (dropping the in-flight send future and pending items) and InboundStreamClosed is emitted

**Skeptic check.** Verified the poll_expired loop removes the InboundInfo entry (which owns the state and queued responses) immediately; matches #10486.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#10486](https://github.com/sigp/lighthouse/pull/10486)

</details>


<a id="rpc-079"></a>
<details>
<summary><b>rpc-079</b> Close request decoder when stream dropped — <i>n/a · low · S · memory</i></summary>

**Idea.** When an incoming RPC stream is closed or dropped, close its request decoder so retained buffers are released.

**Impact.** Rust ownership frees the decoder buffers on drop; no explicit close step exists.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/codec.rs:157`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L157) decoder state is owned by the substream and dropped with it

**Sources.** [teku#10268](https://github.com/Consensys-Incorporated/teku/pull/10268)

</details>


<a id="rpc-080"></a>
<details>
<summary><b>rpc-080</b> Reuse snappy output buffer across partial-frame retries — <i>not · low · M · cpu, memory</i></summary>

**Idea.** When a snappy frame is incomplete and decoding is retried after more bytes arrive, reuse the previously allocated output buffer instead of allocating a fresh large one each attempt.

**Gap in Lighthouse.** Cache the decoded buffer (and snappy progress) in the codec struct across decode() calls for the same length prefix, reset on success or fatal error, in SSZSnappyInboundCodec::decode and SSZSnappyOutboundCodec::decode/decode_error.

**Impact.** Avoids repeated up-to-10MB zeroed allocations when large blocks arrive in several TCP chunks; the snappy frame is also re-decompressed from scratch each retry, which is the bigger cost. Gain small on typical nodes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/codec.rs:188`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L188) vec![0; length] allocated on every decode() call, also at :283 and :319
- codec.rs:183 decode retries from the start of src on every poll

**Sources.** [lighthouse#9030](https://github.com/sigp/lighthouse/pull/9030)

</details>


<a id="rpc-081"></a>
<details>
<summary><b>rpc-081</b> Serve RPC from bounded priority work queue — <i>implemented · low · S · latency, cpu</i></summary>

**Idea.** Run blocks-by-range/root serving and Status processing as work items in the prioritized beacon processor with bounded queues, instead of one unbounded spawned task per request or serial handling in the router.

**Impact.** RPC serving already runs in the bounded prioritized beacon processor queues.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:460-469`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L460-L469) Work::Status, BlocksByRangeRequest, BlobsByRangeRequest, DataColumnsByRangeRequest
- [`beacon_node/beacon_processor/src/lib.rs:1105-1108`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1105-L1108) status_queue prioritised over range queues
- [`beacon_node/beacon_processor/src/lib.rs:1360-1430`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1360-L1430) RPC work pushed into bounded FIFO queues
- [`beacon_node/network/src/network_beacon_processor/mod.rs:688-758`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L688-L758) send_status_message / send_blocks_by_range_request / send_blocks_by_roots_request enqueue work

**Skeptic check.** Confirmed Status and all by-range/by-root serving are beacon processor work items with dedicated bounded queues; earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#1936](https://github.com/sigp/lighthouse/pull/1936)

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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [teku#10153](https://github.com/Consensys-Incorporated/teku/pull/10153)

</details>


<a id="rpc-083"></a>
<details>
<summary><b>rpc-083</b> Skip empty BlobsByRange response chunks — <i>implemented · low · S · bandwidth</i></summary>

**Idea.** In the BlobsByRange handler, do not emit a response chunk for blocks with zero blobs, saving bytes and messages.

**Impact.** No empty chunks are sent.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1694-1708`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1694-L1708) one chunk per blob sidecar in the range; blocks with an empty blob list emit nothing

**Skeptic check.** Verified the per-blob loop; a block with zero blobs yields no response. (It still calls get_blobs per block root, but that is a separate lookup cost, not the empty-chunk idea.)

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@597363d2f](https://github.com/sigp/lighthouse/commit/597363d2f9f2)

</details>


<a id="rpc-084"></a>
<details>
<summary><b>rpc-084</b> Poll only network peers/streams with pending work — <i>n/a · low · S · cpu</i></summary>

**Idea.** In the network loop, track dirty peers/streams and next deadlines and only poll or drain those with pending work, so the loop stops spinning over idle peers.

**Impact.** Lighthouse uses the libp2p swarm, where handlers are woken by waker and only polled when they have events or timers; there is no custom loop scanning idle peers.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/handler.rs:414`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L414) per-connection handler polled by libp2p swarm with DelayQueue deadlines

**Sources.** [silver#136](https://github.com/gattaca-com/silver/pull/136)

</details>


<a id="rpc-085"></a>
<details>
<summary><b>rpc-085</b> Skip unknown roots in BlocksByRoot, keep streaming — <i>implemented · low · S · sync</i></summary>

**Idea.** When serving blocks by root, skip roots not found and continue streaming the rest instead of aborting the response.

**Impact.** Unknown roots are skipped without aborting the response.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:244-262`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L244-L262) Ok(None) logs 'Peer requested unknown block' and continues the stream

**Skeptic check.** Verified BlocksByRoot continues on missing roots; only EL-missing payload errors abort. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#3743](https://github.com/OffchainLabs/prysm/pull/3743)

</details>


<a id="rpc-086"></a>
<details>
<summary><b>rpc-086</b> Use 4-byte payload length prefix — <i>n/a · low · bandwidth</i></summary>

**Idea.** Encode the payload body length in 4 bytes instead of 8 in the wire framing.

**Impact.** Wire framing is fixed by the consensus p2p spec (uvarint length); not a client choice.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/codec.rs:120-135`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L120-L135) (varint length prefix per spec)

**Sources.** [teku#524](https://github.com/Consensys-Incorporated/teku/pull/524)

</details>


<a id="rpc-087"></a>
<details>
<summary><b>rpc-087</b> Stagger large by-range responses over time — <i>not · low · S · bandwidth, cpu</i></summary>

**Idea.** Send blocks-by-range responses in batches spread over time within the response deadline, so serving large ranges to many peers does not burst and trip their rate limiters.

**Gap in Lighthouse.** Handler sends all blocks back-to-back with no pacing; Lighthouse's own requests use a self-limiter. Would need a paced send loop in handle_blocks_by_range_request_inner.

**Impact.** Avoids tripping remote peers' limiters when serving large ranges; mostly affects only peers that ask beyond their quota. Marginal for a mainnet node.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1106-1135`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1106-L1135) (by-range handler loads roots then streams blocks as fast as read)
- [`beacon_node/lighthouse_network/src/rpc/rate_limiter.rs:104-190`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/rate_limiter.rs#L104-L190) (inbound bbrange quota limits the requester)

**Sources.** [prysm#5618](https://github.com/OffchainLabs/prysm/pull/5618)

</details>


<a id="rpc-088"></a>
<details>
<summary><b>rpc-088</b> Cache Status earliest-available-slot per epoch — <i>implemented · low · S · cpu, disk</i></summary>

**Idea.** Compute the earliest-available-slot field for Status messages from local chain data at most once per epoch and cache it, instead of per request.

**Impact.** Status building reads only in-memory cached values; nothing expensive to cache per epoch.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/status.rs:33-45`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/status.rs#L33-L45) earliest_available_slot from get_data_column_custody_info / get_anchor_info
- [`beacon_node/store/src/hot_cold_store.rs:2592-2594`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2592-L2594) data_column_custody_info_cache RwLock read
- [`beacon_node/store/src/hot_cold_store.rs:2793-2795`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2793-L2795) anchor_info RwLock read

**Skeptic check.** Confirmed both inputs are in-memory cached values cloned under a lock, with no DB access; the per-epoch cache Teku needed has no cost to remove here.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#9762](https://github.com/Consensys-Incorporated/teku/pull/9762)

</details>


<a id="rpc-089"></a>
<details>
<summary><b>rpc-089</b> Non-blocking snappy frame decoding — <i>n/a · low · memory, latency</i></summary>

**Idea.** Decode snappy frames incrementally from network buffers as bytes arrive, instead of a blocking stream reader that parks a thread per response chunk and copies more.

**Impact.** Rust tokio codec decodes from the buffered BytesMut without parking a thread; the JVM blocking-stream problem does not exist.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/codec.rs:186-187`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L186-L187) (FrameDecoder over Cursor on already-buffered BytesMut)

**Sources.** [teku#2005](https://github.com/Consensys-Incorporated/teku/pull/2005)

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

**Verdict history.** not (checked) → partial (refuted)

**Sources.** [teku#2486](https://github.com/Consensys-Incorporated/teku/pull/2486), [teku#10949](https://github.com/Consensys-Incorporated/teku/pull/10949)

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


<a id="rpc-092"></a>
<details>
<summary><b>rpc-092</b> Encode status and RPC messages in compact binary, not text — <i>implemented · low · S · bandwidth, cpu</i></summary>

**Idea.** Encode status/hello and other RPC and gossip messages as fixed-width binary (SSZ) fields rather than JSON or strings. Messages are smaller on the wire and need no text parsing.

**Impact.** Already binary SSZ on the wire as the spec requires.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/codec.rs:330`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L330) Status and all RPC messages are SSZ-snappy encoded

**Skeptic check.** Spec-mandated SSZ-snappy for req/resp and gossip; trivially upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#852](https://github.com/Consensys-Incorporated/teku/pull/852), [teku#776](https://github.com/Consensys-Incorporated/teku/pull/776), [teku#780](https://github.com/Consensys-Incorporated/teku/pull/780)

</details>


<a id="rpc-093"></a>
<details>
<summary><b>rpc-093</b> Build status message only when sending — <i>partial · low · S · cpu</i></summary>

**Idea.** Do not construct the Status message (reading shared chain state) each time peer sync info is evaluated; build it only when it is to be sent.

**Gap in Lighthouse.** SyncManager::add_peer could read the local SyncInfo straight from canonical_head.cached_head() instead of building a StatusMessage; the sending path already builds it once per batch.

**Impact.** Saves a few locks and one small struct per received Status. Negligible; the real cost in the original PR was the Arc access, and cached_head is cheap now.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/manager.rs:418`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L418) add_peer calls self.chain.status_message() for each peer status to read local head/finalized
- [`beacon_node/network/src/status.rs:21`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/status.rs#L21) status_message builds from cached_head and takes only a cache read (store/src/hot_cold_store.rs:2592) and get_anchor_info
- [`beacon_node/network/src/service.rs:976`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L976) send_status builds once for all peers

**Sources.** [lighthouse#1896](https://github.com/sigp/lighthouse/pull/1896)

</details>


<a id="rpc-094"></a>
<details>
<summary><b>rpc-094</b> Combine status and ping/metadata exchange per peer — <i>n/a · low · bandwidth, latency</i></summary>

**Idea.** Merge the peer status request and the ping/metadata request into a single exchange so fewer round trips are needed per peer.

**Impact.** Status and Ping are separate spec protocols on separate streams opened concurrently, so merging them is a code-level batching in Prysm and saves no round trips here.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:85`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L85) separate status and ping queues; both are independent libp2p streams

**Sources.** [prysm#5319](https://github.com/OffchainLabs/prysm/pull/5319)

</details>


<a id="rpc-095"></a>
<details>
<summary><b>rpc-095</b> Truncate peer-supplied error message before decoding — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Truncate peer-supplied req/resp error message bytes to a small bound (e.g. 256) before decoding and sanitising, so a peer cannot force large string allocations.

**Impact.** Peer error strings are bounded to 256 bytes before allocation.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/codec.rs:307`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L307) decode_error rejects length &gt; ERROR_TYPE_MAX before allocating decoded_buffer
- [`beacon_node/lighthouse_network/src/rpc/protocol.rs:87`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/protocol.rs#L87) ERROR_TYPE_MAX derived from 256-byte ErrorType VariableList

**Skeptic check.** Lighthouse rejects instead of truncating, but the allocation bound is the same; earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@bd053bd9d](https://github.com/ChainSafe/lodestar/commit/bd053bd9dc6d)

</details>


<a id="rpc-096"></a>
<details>
<summary><b>rpc-096</b> Cap simultaneous inbound substreams per peer — <i>implemented · low · S · memory, bandwidth</i></summary>

**Idea.** Limit the number of concurrent inbound RPC substreams per peer and disconnect the peer when exceeded, so stream state and timers stay bounded.

**Impact.** Inbound substreams are bounded per connection and the offending peer is disconnected; nothing to gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/handler.rs:41`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L41) MAX_INBOUND_SUBSTREAMS=32
- [`beacon_node/lighthouse_network/src/rpc/handler.rs:994-1018`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L994-L1018) over cap emits HandlerRejected and calls self.shutdown
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:561`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L561) HandlerRejected =&gt; PeerAction::Fatal

**Skeptic check.** Verified the cap check in the inbound request path, the handler shutdown, and that the peer manager scores HandlerRejected as Fatal. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#3261](https://github.com/sigp/lighthouse/pull/3261)

</details>


<a id="rpc-097"></a>
<details>
<summary><b>rpc-097</b> Run cleanup when async request supplier throws — <i>n/a · low · S · memory</i></summary>

**Idea.** Catch exceptions thrown by async request task suppliers and propagate them to the returned future, so failed requests (e.g. closed streams) always run cleanup and do not leak pending request state.

**Impact.** Teku future/supplier pattern; Rust handler state is dropped via RAII and delay-queue removal, no pending-request leak mechanism of that kind.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/handler.rs:1017`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L1017) errors surfaced as HandlerEvent::Err

**Sources.** [teku#2151](https://github.com/Consensys-Incorporated/teku/pull/2151)

</details>


<a id="rpc-098"></a>
<details>
<summary><b>rpc-098</b> Trim by-root/by-range requests to servable range before expensive reads — <i>partial · low · S · cpu, disk, latency</i></summary>

**Idea.** In by-root and by-range handlers, clip the request to the servable slot range and skip roots known to be too old before doing expensive DB or EL work, so out-of-range requests cost almost nothing.

**Gap in Lighthouse.** By-range rejects out-of-range starts (cheap) instead of clipping, which is fine; by-root handlers could skip roots known pruned/older than boundary before DB/EL reads in handle_blocks_by_root_request_inner and blobs/columns by-root.

**Impact.** Saves a few DB misses for peers asking for old roots; marginal on mainnet.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1651-1672`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1651-L1672) BlobsByRange rejects start below oldest_data_slot/boundary
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:217-250`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L217-L250) BlocksByRoot has no age filter, goes to get_blocks_checking_caches

**Sources.** [teku#11052](https://github.com/Consensys-Incorporated/teku/pull/11052)

</details>


<a id="rpc-099"></a>
<details>
<summary><b>rpc-099</b> Send only each sidecar own bytes in by-range responses — <i>n/a · low · S · bandwidth</i></summary>

**Idea.** In BlobSidecarsByRange responses, serialize only each sidecar own bytes rather than all blobs of the block for every sidecar, avoiding inflated responses.

**Impact.** Lighthouse encodes each sidecar as its own object; no whole-block blob bytes inflation exists.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/methods.rs:666`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/methods.rs#L666) each response chunk is one Arc&lt;DataColumnSidecar&gt;/BlobSidecar encoded separately

**Sources.** [lodestar#5640](https://github.com/ChainSafe/lodestar/pull/5640)

</details>


<a id="rpc-100"></a>
<details>
<summary><b>rpc-100</b> Fork-dependent maximum RPC and gossip message sizes — <i>partial · low · M · memory, bandwidth</i></summary>

**Idea.** Set maximum RPC and gossip message sizes as a function of the active fork, so decoders never allocate or accept buffers larger than the fork allows.

**Gap in Lighthouse.** RPC response limits are fork-dependent, but gossip max transmit size and RPC max_rpc_size (rpc/mod.rs:322) are single fixed values; per-topic/fork gossip limits would need gossipsub per-topic size checks.

**Impact.** Tighter buffers bound DoS memory; small real-world gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/protocol.rs:138`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/protocol.rs#L138) rpc_block_limits_by_fork, :624-633 response limits per fork
- [`beacon_node/lighthouse_network/src/service/mod.rs:246`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L246) gossipsub_max_transmit_size = spec.max_message_size()
- [`consensus/types/src/core/chain_spec.rs:971`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/core/chain_spec.rs#L971) fixed max from max_payload_size

**Sources.** [lighthouse#2839](https://github.com/sigp/lighthouse/pull/2839)

</details>


<a id="rpc-101"></a>
<details>
<summary><b>rpc-101</b> Group column by-root requests per block root — <i>implemented · low · S · bandwidth</i></summary>

**Idea.** Encode data column by-root requests as one entry per block root with a list of column indices instead of one entry per (root, column), so roots are not repeated and requests are smaller.

**Impact.** Requests already carry one entry per block root (Fulu spec wire format).

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/data/data_column_sidecar.rs:40-45`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/data/data_column_sidecar.rs#L40-L45) DataColumnsByRootIdentifier { block_root, columns: VariableList&lt;ColumnIndex&gt; }
- [`beacon_node/lighthouse_network/src/rpc/methods.rs:574-576`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/methods.rs#L574-L576) DataColumnsByRootRequest holds a list of DataColumnsByRootIdentifier
- [`beacon_node/network/src/sync/network_context/requests/data_columns_by_root.rs:16-32`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/requests/data_columns_by_root.rs#L16-L32) try_into_request builds one identifier per block root with all requested indices

**Skeptic check.** Verified the wire type and the sync request builder group columns per root. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#7782](https://github.com/ChainSafe/lodestar/pull/7782)

</details>


<a id="rpc-102"></a>
<details>
<summary><b>rpc-102</b> Release pooled decoder buffers once response is decoded — <i>n/a · low · S · memory</i></summary>

**Idea.** Close per-message context, payload and error decoders as soon as a req/resp response is fully decoded so pooled byte buffers are released rather than leaked.

**Impact.** Java pooled-buffer leak; Rust buffers are freed by drop.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/codec.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs): codec uses owned BytesMut, no pooled decoder buffers

**Sources.** [teku#10668](https://github.com/Consensys-Incorporated/teku/pull/10668)

</details>


