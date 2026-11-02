# el_interaction

41 ideas: 7 not, 10 partial, 20 implemented, 4 n/a; 15 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

Ids missing from the sequence are ideas that have not been checked against Lighthouse yet.

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [el_interaction-001](#el_interaction-001) | Fetch blobs from EL to build sidecars locally | implemented | high |  | bandwidth, cpu, latency |
| [el_interaction-002](#el_interaction-002) | Use getBlobsV4 to build partial columns from sparse blobpools | implemented | high |  | bandwidth, latency |
| [el_interaction-003](#el_interaction-003) **★** | Fetch blobs from EL during range sync too | not | medium | M | sync, latency |
| [el_interaction-004](#el_interaction-004) **★** | SSZ over REST transport for the engine API | not | medium | L | cpu, latency, bandwidth |
| [el_interaction-005](#el_interaction-005) **★** | SSZ encoding for builder API calls | partial | medium | S | bandwidth, cpu, latency |
| [el_interaction-007](#el_interaction-007) **★** | Drive EL sync from light-client head | not | medium | L | sync |
| [el_interaction-011](#el_interaction-011) | Send early forkchoiceUpdated with payload attributes | implemented | medium |  | latency |
| [el_interaction-012](#el_interaction-012) | Prepare payloads only for imminent local proposals | partial | low | S | cpu, latency, sync |
| [el_interaction-016](#el_interaction-016) | Exempt critical builder calls from request throttling | n/a | medium |  | latency |
| [el_interaction-017](#el_interaction-017) **★** | Send timeout header on builder getHeader | partial | medium | S | latency |
| [el_interaction-018](#el_interaction-018) | Use blinded-block submit V2 with empty response | implemented | medium |  | bandwidth |
| [el_interaction-023](#el_interaction-023) | Use 256-bit integers in engine API types | implemented | low | S | cpu, memory |
| [el_interaction-024](#el_interaction-024) | Decode and validate block access list once | n/a | low | S | cpu, latency |
| [el_interaction-025](#el_interaction-025) **★** | Faster JSON decoder for large engine payloads | not | medium | M | cpu, latency |
| [el_interaction-027](#el_interaction-027) | Borrow or move execution payloads instead of cloning | partial | low | M | cpu, memory |
| [el_interaction-029](#el_interaction-029) | Keep at most one forkchoiceUpdated in flight | implemented | medium |  | cpu, latency |
| [el_interaction-030](#el_interaction-030) | Deduplicate identical forkchoiceUpdated calls | implemented | medium | S | latency, cpu, bandwidth |
| [el_interaction-033](#el_interaction-033) | Unblind blocks with batched engine_getPayloadBodies | implemented | medium | S | bandwidth, cpu, latency, memory |
| [el_interaction-034](#el_interaction-034) **★** | Store blinded blocks and fetch payloads from EL | partial | high | M | disk |
| [el_interaction-039](#el_interaction-039) **★** | Limit and dedupe getBlobs calls per block root | partial | medium | S | bandwidth, cpu, latency, memory |
| [el_interaction-044](#el_interaction-044) | Cache justified/finalized payload hashes for fcU | implemented | low | S | disk, latency |
| [el_interaction-053](#el_interaction-053) | Slot-based deadline for early-block newPayload | n/a | medium | S | latency |
| [el_interaction-054](#el_interaction-054) | Per-method engine API timeouts | implemented | medium | S | latency |
| [el_interaction-063](#el_interaction-063) **★** | Send fcU after SYNCING newPayload | partial | medium | S | sync |
| [el_interaction-064](#el_interaction-064) | Send forkchoiceUpdated on slot tick | implemented | medium | S | latency |
| [el_interaction-066](#el_interaction-066) | Verify block hash locally, skip newPayload on finalized sync | implemented | high |  | cpu, latency, sync |
| [el_interaction-069](#el_interaction-069) **★** | Fast hex decoding of Engine API responses | partial | medium | M | cpu, memory, latency |
| [el_interaction-071](#el_interaction-071) **★** | Keep builder relay connections warm | not | medium | S | latency |
| [el_interaction-077](#el_interaction-077) **★** | Separate EL queue for payload-body serving | partial | medium | S | latency |
| [el_interaction-078](#el_interaction-078) **★** | Bound concurrent in-flight EL requests | partial | medium | S | latency, cpu |
| [el_interaction-079](#el_interaction-079) | Optimistic block import when EL syncing or offline | implemented | high |  | sync, latency |
| [el_interaction-080](#el_interaction-080) | Skip EL calls for already finalized blocks during sync | implemented | high | S | sync, latency |
| [el_interaction-081](#el_interaction-081) **★** | Ordered trie root for payload hash | not | medium | M | cpu |
| [el_interaction-082](#el_interaction-082) | Use latestValidHash to mark ancestor runs | implemented | medium |  | cpu, sync |
| [el_interaction-084](#el_interaction-084) | Correct payload id cache key for prepared payloads | implemented | medium |  | latency |
| [el_interaction-085](#el_interaction-085) | Split head FCU and payload-attributes FCU | implemented | medium |  | latency |
| [el_interaction-086](#el_interaction-086) | Stable payload attributes target slot | implemented | medium |  | latency |
| [el_interaction-087](#el_interaction-087) | Longer getPayload timeout without prior preparation | implemented | low | S | latency |
| [el_interaction-088](#el_interaction-088) **★** | Short getPayload deadline to fail over fast | not | medium | S | latency |
| [el_interaction-102](#el_interaction-102) | Drop duplicate queued blocks before newPayload | implemented | medium | S | cpu, latency |
| [el_interaction-133](#el_interaction-133) | Reuse received transaction encodings | n/a | medium | S | cpu |

★ actionable. Click an id for the full record.

## Ideas

<a id="el_interaction-001"></a>
<details>
<summary><b>el_interaction-001</b> Fetch blobs from EL to build sidecars locally — <i>implemented · high · bandwidth, cpu, latency</i></summary>

**Idea.** When a block or first data column sidecar arrives, call engine_getBlobs (V1/V2) to pull its blobs and proofs from the local EL blob pool and build blob or data column sidecars locally. This skips waiting for gossip or downloading from peers, and lets the node publish the sidecars itself.

**Impact.** Already saves column downloads/gossip waiting on a mainnet node.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:113`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L113) fetch_and_process_engine_blobs
- [`beacon_node/network/src/network_beacon_processor/mod.rs:998`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L998) fetch_engine_blobs_and_publish_full, publishes columns
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:225`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L225) get_blobs_v2 builds columns

**Sources.** [prysm#15469](https://github.com/OffchainLabs/prysm/pull/15469), [prysm#14513](https://github.com/OffchainLabs/prysm/pull/14513), [teku#8662](https://github.com/Consensys-Incorporated/teku/pull/8662), [grandine@047520e97](https://github.com/grandinetech/grandine/commit/047520e97856), [lighthouse#6268](https://github.com/sigp/lighthouse/pull/6268), [lighthouse#5829](https://github.com/sigp/lighthouse/pull/5829), [grandine#258](https://github.com/grandinetech/grandine/pull/258)

</details>


<a id="el_interaction-002"></a>
<details>
<summary><b>el_interaction-002</b> Use getBlobsV4 to build partial columns from sparse blobpools — <i>implemented · high · bandwidth, latency</i></summary>

**Idea.** Call engine_getBlobsV4 to get cells for the blobs the EL has, even when it holds only part of them, and build partial data columns locally. This reduces column downloads from peers when the EL blob pool is sparse.

**Impact.** Already reduces column downloads on sparse blobpools.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:317`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L317) import_custody_partial_columns
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:531`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L531) build_partial_columns_from_v4_response
- [`beacon_node/execution_layer/src/engine_api.rs:673`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api.rs#L673) get_blobs_v4 capability

**Sources.** [lighthouse#9438](https://github.com/sigp/lighthouse/pull/9438), [prysm#17378](https://github.com/OffchainLabs/prysm/pull/17378)

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

**Sources.** [lighthouse#10505](https://github.com/sigp/lighthouse/pull/10505), [lodestar#8994](https://github.com/ChainSafe/lodestar/pull/8994), [lighthouse#9652](https://github.com/sigp/lighthouse/pull/9652), [lodestar#10204](https://github.com/ChainSafe/lodestar/pull/10204), [prysm#16447](https://github.com/OffchainLabs/prysm/pull/16447), [lighthouse#10242](https://github.com/sigp/lighthouse/pull/10242), [prysm#16901](https://github.com/OffchainLabs/prysm/pull/16901)

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

**Sources.** [lodestar#7180](https://github.com/ChainSafe/lodestar/pull/7180), [lodestar#7444](https://github.com/ChainSafe/lodestar/pull/7444), [lighthouse#6859](https://github.com/sigp/lighthouse/pull/6859), [prysm#14976](https://github.com/OffchainLabs/prysm/pull/14976), [lodestar#7185](https://github.com/ChainSafe/lodestar/pull/7185)

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

**Sources.** [nimbus#4041](https://github.com/status-im/nimbus-eth2/pull/4041), [nimbus#4805](https://github.com/status-im/nimbus-eth2/pull/4805)

</details>


<a id="el_interaction-011"></a>
<details>
<summary><b>el_interaction-011</b> Send early forkchoiceUpdated with payload attributes — <i>implemented · medium · latency</i></summary>

**Idea.** When a local validator proposes in the next slot, send forkchoiceUpdated with payload attributes ahead of time (one slot early, or immediately when a timely block does not become head) and cache the payload id. Block production then gets an already-built payload instead of waiting for the EL.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:1931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1931) prepare_beacon_proposer after every head change
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:217`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L217) prepare_beacon_proposer from the late-slot timer
- [`beacon_node/beacon_chain/src/proposer_prep_service.rs:47`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/proposer_prep_service.rs#L47) periodic prepare_beacon_proposer
- [`beacon_node/beacon_chain/src/beacon_chain.rs:6954`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6954) sends fcU with payload attributes for next slot
- [`beacon_node/execution_layer/src/engines.rs:149`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engines.rs#L149) payload_id_cache reused by get_payload

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

**Sources.** [nimbus#8960](https://github.com/status-im/nimbus-eth2/pull/8960)

</details>


<a id="el_interaction-018"></a>
<details>
<summary><b>el_interaction-018</b> Use blinded-block submit V2 with empty response — <i>implemented · medium · bandwidth</i></summary>

**Idea.** Submit blinded blocks with the builder submitBlindedBlockV2 endpoint, which returns an empty response instead of the full payload and blob bundle, because the relay publishes the block itself.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/builder_client/src/pre_gloas_builder_http_client.rs:262`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/builder_client/src/pre_gloas_builder_http_client.rs#L262) POST /eth/v2/builder/blinded_blocks (SSZ and JSON)
- [`beacon_node/builder_client/src/pre_gloas_builder_http_client.rs:296`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/builder_client/src/pre_gloas_builder_http_client.rs#L296) expects 202 ACCEPTED with no body
- [`beacon_node/execution_layer/src/lib.rs:1836`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1836) post_builder_blinded_blocks_v2 is the only submit path

**Sources.** [lodestar#8055](https://github.com/ChainSafe/lodestar/pull/8055)

</details>


<a id="el_interaction-023"></a>
<details>
<summary><b>el_interaction-023</b> Use 256-bit integers in engine API types — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Represent baseFeePerGas, blockValue and similar engine API fields as fixed 256-bit integers instead of big integers, avoiding conversions and allocations per payload.

**Impact.** Already fixed-size U256 (alloy), no bigint allocations.

**Best measured result.** decode 35 -&gt; 33 allocs, encode 40 -&gt; 36 allocs; time within noise (pr:caplin#24016)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engine_api/json_structures.rs:100`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/json_structures.rs#L100) base_fee_per_gas: Uint256
- [`beacon_node/execution_layer/src/engine_api/json_structures.rs:711`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/json_structures.rs#L711) block_value: Uint256

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

**Sources.** [caplin#24017](https://github.com/erigontech/erigon/pull/24017)

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


<a id="el_interaction-029"></a>
<details>
<summary><b>el_interaction-029</b> Keep at most one forkchoiceUpdated in flight — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** Await each forkchoiceUpdated call to the EL instead of spawning it detached, so at most one fcU is in flight. This cuts EL load and makes head updates ordered.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:7225`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7225) execution_engine_forkchoice_lock held while reading head and sending fcU
- [`beacon_node/beacon_chain/src/canonical_head.rs:1296`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1296) fcU task spawned but serialized by that lock

**Sources.** [nimbus#4609](https://github.com/status-im/nimbus-eth2/pull/4609)

</details>


<a id="el_interaction-030"></a>
<details>
<summary><b>el_interaction-030</b> Deduplicate identical forkchoiceUpdated calls — <i>implemented · medium · S · latency, cpu, bandwidth</i></summary>

**Idea.** Remember the last forkchoiceUpdated arguments (head, safe, finalized hashes; ignore fields implied by the head) and do not re-send an identical fcU, apart from at most one repeat per slot to survive EL restarts. This removes redundant EL calls.

**Gap in Lighthouse.** Dedup is done at the fork-choice change level, not by comparing last-sent args; prepare_beacon_proposer (beacon_chain.rs:7135) can still send a second fcU for the same head with payload attributes, which is needed anyway.

**Impact.** Negligible; fcU calls already only follow head/checkpoint changes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:1084`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1084) exits early with 'No change in canonical head' when view, payload status and fcU params are unchanged, so no fcU is sent
- [`beacon_node/beacon_chain/src/canonical_head.rs:1296`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1296) spawn_execution_layer_updates only reached after a change
- [`beacon_node/execution_layer/src/engines.rs:193`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engines.rs#L193) latest_forkchoice_state resent on EL reconnect (upcheck:248), covering EL restarts

**Sources.** [prysm#12091](https://github.com/OffchainLabs/prysm/pull/12091), [nimbus#5635](https://github.com/status-im/nimbus-eth2/pull/5635), [nimbus#8799](https://github.com/status-im/nimbus-eth2/pull/8799)

</details>


<a id="el_interaction-033"></a>
<details>
<summary><b>el_interaction-033</b> Unblind blocks with batched engine_getPayloadBodies — <i>implemented · medium · S · bandwidth, cpu, latency, memory</i></summary>

**Idea.** When serving block ranges or the HTTP API from blinded blocks, fetch execution payloads with engine_getPayloadBodiesByHash/ByRange in batched chunks (for example 32 hashes per call) instead of one request per block or whole-block eth_getBlockByHash. Payload bodies carry less data, avoid JSON block conversion and need fewer EL round trips.

**Impact.** Already done; blinded-block unblinding for RPC ranges and API uses batched bodies.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_block_streamer.rs:226`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_block_streamer.rs#L226) fetch_payload_bodies chunks hashes by MAX_PAYLOAD_BODIES_PER_REQUEST (32) via get_payload_bodies_by_hash
- [`beacon_node/execution_layer/src/lib.rs:1678`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1678) get_payload_bodies_by_hash

**Sources.** [prysm#11210](https://github.com/OffchainLabs/prysm/pull/11210), [prysm#12997](https://github.com/OffchainLabs/prysm/pull/12997), [lighthouse#4102](https://github.com/sigp/lighthouse/pull/4102), [prysm#12630](https://github.com/OffchainLabs/prysm/pull/12630), [lighthouse@787614f6f](https://github.com/sigp/lighthouse/commit/787614f6f646)

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

**Sources.** [grandine@b7a0fcc26](https://github.com/grandinetech/grandine/commit/b7a0fcc26c3b)

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

**Sources.** [lodestar#10329](https://github.com/ChainSafe/lodestar/pull/10329), [nimbus#8884](https://github.com/status-im/nimbus-eth2/pull/8884), [nimbus#8982](https://github.com/status-im/nimbus-eth2/pull/8982), [lodestar#8381](https://github.com/ChainSafe/lodestar/pull/8381), [lodestar#8399](https://github.com/ChainSafe/lodestar/pull/8399), [lodestar#8282](https://github.com/ChainSafe/lodestar/pull/8282)

</details>


<a id="el_interaction-044"></a>
<details>
<summary><b>el_interaction-044</b> Cache justified/finalized payload hashes for fcU — <i>implemented · low · S · disk, latency</i></summary>

**Idea.** Keep the execution block hashes of the justified and finalized checkpoints in memory so each forkchoiceUpdated avoids database lookups for them.

**Impact.** Hashes are cached in the head snapshot, so fcU does no DB lookups for them.

**Best measured result.** saves 2 DB lookups per head update, ~100ms on the author's machine (pr:prysm#10657)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:7227-7250`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7227-L7250) fcU takes justified_hash and finalized_hash from cached ForkchoiceUpdateParameters
- [`beacon_node/beacon_chain/src/beacon_chain.rs:6770`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6770) cached_head.forkchoice_update_parameters()

**Sources.** [prysm#10657](https://github.com/OffchainLabs/prysm/pull/10657)

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

- [`beacon_node/execution_layer/src/engine_api/http.rs:44`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L44) NEW_PAYLOAD 8s, :52 GET_PAYLOAD 2s, :59 FORKCHOICE_UPDATED 8s, :74 GET_BLOBS 1s, :63 payload bodies 10s
- [`beacon_node/execution_layer/src/engine_api/http.rs:988`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L988) getPayload uses its own timeout

**Sources.** [grandine@5ce858023](https://github.com/grandinetech/grandine/commit/5ce858023642)

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

**Sources.** [nimbus#3618](https://github.com/status-im/nimbus-eth2/pull/3618)

</details>


<a id="el_interaction-064"></a>
<details>
<summary><b>el_interaction-064</b> Send forkchoiceUpdated on slot tick — <i>implemented · medium · S · latency</i></summary>

**Idea.** Trigger forkchoiceUpdated at slot start and before attesting, not only when a new head is stored, through one shared fork-choice refresh path.

**Impact.** Already done; fcU at slot start follows recompute_head, only when something changed.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:7471`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7471) per_slot_task calls recompute_head_at_current_slot each slot
- [`beacon_node/beacon_chain/src/canonical_head.rs:1084`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1084),1296 fcU sent through the same path when the view changes

**Sources.** [nimbus#4009](https://github.com/status-im/nimbus-eth2/pull/4009)

</details>


<a id="el_interaction-066"></a>
<details>
<summary><b>el_interaction-066</b> Verify block hash locally, skip newPayload on finalized sync — <i>implemented · high · cpu, latency, sync</i></summary>

**Idea.** During sync of finalized blocks, verify the execution block hash locally (RLP header, including new fork header fields, plus transactions and withdrawals trie roots) and skip the newPayload call, falling back to the EL only on failure. Local hashing costs about 500us per block, far below an EL round trip.

**Impact.** Already avoids an EL round trip per block during finalized sync.

**Best measured result.** block hash verification about 500us per block on mainnet (pr:lighthouse#3794)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engine_api/new_payload_request.rs:101-124`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/new_payload_request.rs#L101-L124) perform_optimistic_sync_verifications / verify_payload_block_hash
- [`beacon_node/beacon_chain/src/execution_payload.rs:78-95`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/execution_payload.rs#L78-L95) skips newPayload when NotifyExecutionLayer::No and optimistic_finalized_sync, falls back to EL on failure
- [`beacon_node/execution_layer/src/block_hash.rs:17`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/block_hash.rs#L17) calculate_execution_block_hash

**Sources.** [lighthouse#3920](https://github.com/sigp/lighthouse/pull/3920), [lighthouse#3794](https://github.com/sigp/lighthouse/pull/3794), [lighthouse#3877](https://github.com/sigp/lighthouse/pull/3877)

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

**Sources.** [lodestar#10358](https://github.com/ChainSafe/lodestar/pull/10358), [teku#10457](https://github.com/Consensys-Incorporated/teku/pull/10457), [teku#10469](https://github.com/Consensys-Incorporated/teku/pull/10469)

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

**Sources.** [prysm#17493](https://github.com/OffchainLabs/prysm/pull/17493), [lodestar#9947](https://github.com/ChainSafe/lodestar/pull/9947)

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

**Sources.** [teku#4852](https://github.com/Consensys-Incorporated/teku/pull/4852), [teku#1151](https://github.com/Consensys-Incorporated/teku/pull/1151)

</details>


<a id="el_interaction-079"></a>
<details>
<summary><b>el_interaction-079</b> Optimistic block import when EL syncing or offline — <i>implemented · high · sync, latency</i></summary>

**Idea.** Import blocks optimistically when the EL returns SYNCING or is unreachable, instead of stalling. The beacon chain stays synced and can give the EL the latest head right away when it recovers.

**Impact.** Already keeps node synced when EL is syncing.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/execution_payload.rs:151`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/execution_payload.rs#L151) PayloadStatus::Syncing\|Accepted =&gt; PayloadVerificationStatus::Optimistic
- [`beacon_node/execution_layer/src/payload_status.rs:73`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/payload_status.rs#L73) Syncing handling

**Sources.** [lighthouse#2683](https://github.com/sigp/lighthouse/pull/2683), [nimbus#4458](https://github.com/status-im/nimbus-eth2/pull/4458)

</details>


<a id="el_interaction-080"></a>
<details>
<summary><b>el_interaction-080</b> Skip EL calls for already finalized blocks during sync — <i>implemented · high · S · sync, latency</i></summary>

**Idea.** During range sync, treat blocks that are finalized or far behind the wall slot as optimistic on CL verification alone and skip per-block newPayload/forkchoiceUpdated, updating the EL only occasionally. Per-block EL calls on a syncing EL are wasted work.

**Gap in Lighthouse.** Only applies when the sync state is syncing-finalized, not for non-finalized blocks that are merely far behind the wall slot; that remainder is small.

**Impact.** Already skips per-block EL calls on finalized range sync, which is the bulk of the saving.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:495-503`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L495-L503) NotifyExecutionLayer::No when is_syncing_finalized
- [`beacon_node/beacon_chain/src/execution_payload.rs:78`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/execution_payload.rs#L78) skips newPayload in that case

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

**Sources.** [nimbus#6610](https://github.com/status-im/nimbus-eth2/pull/6610)

</details>


<a id="el_interaction-082"></a>
<details>
<summary><b>el_interaction-082</b> Use latestValidHash to mark ancestor runs — <i>implemented · medium · cpu, sync</i></summary>

**Idea.** Use the latestValidHash in newPayload/fcU responses to mark a whole chain of optimistic ancestors valid or invalid in fork choice at once, instead of verifying each block with the EL.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/execution_payload.rs:180`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/execution_payload.rs#L180) newPayload INVALID uses latest_valid_hash with InvalidateMany
- [`consensus/proto_array/src/proto_array.rs:943`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L943) propagate_execution_payload_validation marks all optimistic ancestors Valid at once

**Sources.** [teku#4924](https://github.com/Consensys-Incorporated/teku/pull/4924)

</details>


<a id="el_interaction-084"></a>
<details>
<summary><b>el_interaction-084</b> Correct payload id cache key for prepared payloads — <i>implemented · medium · latency</i></summary>

**Idea.** Key the proposer payload-id cache only by head block hash (and attributes or slot), the same key used when filling it, including skipped slots and epoch boundaries. The payload prepared by an earlier fcU is then reused at proposal instead of another fcU and build wait.

**Best measured result.** slot 0 proposal p50 603ms vs 525ms for other slots (pr:lodestar#10432)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engines.rs:109`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engines.rs#L109) PayloadIdCacheKey = head_block_hash + full payload_attributes
- [`beacon_node/execution_layer/src/engines.rs:176`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engines.rs#L176) inserted on every fcU with attributes using the same key
- [`beacon_node/execution_layer/src/lib.rs:1342`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1342) get_full_payload_with looks up the same key, hit/miss metric

**Sources.** [prysm#11567](https://github.com/OffchainLabs/prysm/pull/11567), [lodestar#10432](https://github.com/ChainSafe/lodestar/pull/10432), [prysm#12987](https://github.com/OffchainLabs/prysm/pull/12987)

</details>


<a id="el_interaction-085"></a>
<details>
<summary><b>el_interaction-085</b> Split head FCU and payload-attributes FCU — <i>implemented · medium · latency</i></summary>

**Idea.** On block import, send forkchoiceUpdated without payload attributes immediately, then send a second FCU with attributes asynchronously only when proposing next slot. The EL learns the head earlier and the state advance for attributes leaves the import path.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/lib.rs:1527`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1527) payload_attributes returns Some only if a proposer was primed for next slot and head root
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7135`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7135) prepare_beacon_proposer sends a separate fcU with attributes near the proposal slot

**Sources.** [prysm#13403](https://github.com/OffchainLabs/prysm/pull/13403)

</details>


<a id="el_interaction-086"></a>
<details>
<summary><b>el_interaction-086</b> Stable payload attributes target slot — <i>implemented · medium · latency</i></summary>

**Idea.** Compute FCU payload attributes for a stable target slot and do not re-send FCU on proposer-data refresh or late block import. The EL then does not rebuild or drop its payload, and no corrective FCU plus immediate getPayload is needed.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/lib.rs:1527`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1527) attributes looked up by ProposerKey{next slot, head root, status}, not recomputed
- [`beacon_node/execution_layer/src/lib.rs:816`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L816) update_proposer_preparation only updates maps, sends no fcU
- [`beacon_node/execution_layer/src/lib.rs:426`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L426) key deliberately omits fee recipient

**Sources.** [teku#8009](https://github.com/Consensys-Incorporated/teku/pull/8009)

</details>


<a id="el_interaction-087"></a>
<details>
<summary><b>el_interaction-087</b> Longer getPayload timeout without prior preparation — <i>implemented · low · S · latency</i></summary>

**Idea.** When block production finds no prior fcU-prepared payload, allow a longer getPayload timeout so the fallback build is not cut off and the proposal missed.

**Impact.** None needed: the fallback build gets a separate generous timeout per call, so there is no 500ms cutoff to remove.

**Best measured result.** avoids ~500ms added latency (pr:nimbus#5194)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/lib.rs:1342`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1342) - looks up cached payload_id, else falls back to a fresh forkchoiceUpdated with attributes
- [`beacon_node/execution_layer/src/lib.rs:1403`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1403) - then calls get_payload as a separate request
- [`beacon_node/execution_layer/src/engine_api/http.rs:52`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L52) - getPayload timeout 2s, not shortened on the fallback path
- [`beacon_node/execution_layer/src/engine_api/http.rs:59`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L59) - fcU fallback has its own 8s timeout, so the build is not cut off by one shared deadline

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

**Sources.** [prysm#17212](https://github.com/OffchainLabs/prysm/pull/17212)

</details>


<a id="el_interaction-102"></a>
<details>
<summary><b>el_interaction-102</b> Drop duplicate queued blocks before newPayload — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Keep a small FIFO of recent (block root, signature) in the block processor and drop duplicate queued blocks before processing, avoiding repeated newPayload calls.

**Impact.** Duplicate blocks are rejected by observed_block_producers/fork-choice checks and in-flight cache before newPayload; no signature-keyed FIFO, but same effect.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:181`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L181) DuplicateCache of in-flight block roots
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:121`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L121) check_and_insert before processing, else reprocess queue
- [`beacon_node/beacon_chain/src/block_verification.rs:972`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L972) and :1953 fork-choice contains_block returns DuplicateFullyImported before any state load or newPayload

**Sources.** [nimbus#4814](https://github.com/status-im/nimbus-eth2/pull/4814), [nimbus#4850](https://github.com/status-im/nimbus-eth2/pull/4850)

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


