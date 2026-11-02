# validator_client

49 ideas: 8 not, 10 partial, 27 implemented, 4 n/a; 4 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

Ids missing from the sequence are ideas that have not been checked against Lighthouse yet.

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [validator_client-001](#validator_client-001) | Look up validator statuses via POST body, not batched GET | not | low | S | bandwidth, cpu, latency |
| [validator_client-002](#validator_client-002) | Batch pubkey-to-index and status lookups in large batches | not | low | S | latency, bandwidth, startup |
| [validator_client-004](#validator_client-004) | Subscribe to head event stream instead of polling | implemented | medium |  | latency, bandwidth, cpu |
| [validator_client-005](#validator_client-005) **★** | SSZ encoding for VC-BN block traffic | partial | medium | S | bandwidth, cpu, latency |
| [validator_client-007](#validator_client-007) | Attest as soon as the slot's head block arrives | implemented | medium |  | latency |
| [validator_client-008](#validator_client-008) **★** | Request blinded blocks from the beacon node | partial | medium | S | bandwidth, latency |
| [validator_client-010](#validator_client-010) | Sync committee messages as soon as block seen | implemented | low |  | latency |
| [validator_client-011](#validator_client-011) | Payload timeliness votes on payload-available event | implemented | medium |  | latency, cpu |
| [validator_client-012](#validator_client-012) | Slim duties response without full committee lists | implemented | low |  | bandwidth, cpu, latency |
| [validator_client-014](#validator_client-014) | Do not fetch all validators for activation-queue logging | implemented | low |  | latency, bandwidth, cpu |
| [validator_client-018](#validator_client-018) | Prefetch next-epoch duties off the critical path | partial | low | S | latency |
| [validator_client-019](#validator_client-019) | Batch attestation submission per slot | implemented | medium |  | latency, cpu, bandwidth |
| [validator_client-021](#validator_client-021) | Batch slashing-protection checks into one transaction | implemented | medium |  | latency, disk, cpu |
| [validator_client-022](#validator_client-022) | Fewer DB transactions per slashing-protection check | partial | low | M | latency, disk |
| [validator_client-023](#validator_client-023) | Bounded batches for builder registrations | implemented | low |  | bandwidth, latency |
| [validator_client-025](#validator_client-025) | Decrypt validator keystores in parallel at startup | not | low | S | startup, cpu |
| [validator_client-026](#validator_client-026) | Faster crypto for keystore KDF | not | low | S | startup, cpu |
| [validator_client-029](#validator_client-029) | Bound interchange import target epochs | n/a | low |  | cpu, disk |
| [validator_client-034](#validator_client-034) | Fetch attestation data once per slot and reuse | implemented | medium |  | latency, bandwidth, cpu |
| [validator_client-036](#validator_client-036) | Cache signed builder registrations | implemented | low | S | cpu, latency |
| [validator_client-038](#validator_client-038) | Register only active validators with builders | partial | low | S | cpu, bandwidth |
| [validator_client-040](#validator_client-040) | One encrypted store for all keys, one KDF | implemented | low | S | startup, cpu, memory |
| [validator_client-041](#validator_client-041) | Cache signing domain data per epoch | n/a | low | S | latency, bandwidth |
| [validator_client-044](#validator_client-044) | Cache aggregator selection proofs | implemented | low | S | cpu, latency |
| [validator_client-046](#validator_client-046) | Cache own validator index | implemented | low | S | latency, bandwidth |
| [validator_client-055](#validator_client-055) **★** | Refetch duties only when dependent root changes | partial | medium | S | bandwidth, cpu, latency |
| [validator_client-056](#validator_client-056) | Fetch duties once per epoch, serve slots from cache | implemented | low | S | bandwidth, latency, cpu |
| [validator_client-057](#validator_client-057) | Short lookahead, per-slot batches for selection proofs | implemented | low | S | cpu, bandwidth, latency |
| [validator_client-059](#validator_client-059) | Decrypt keystores before waiting for beacon node | implemented | low |  | startup |
| [validator_client-063](#validator_client-063) | Batch committee subnet subscriptions | implemented | low |  | latency, bandwidth |
| [validator_client-074](#validator_client-074) | Event-driven wait for activation | partial | low | S | latency |
| [validator_client-077](#validator_client-077) | Parallel keystore decryption for keymanager API imports | not | low | M | cpu, latency |
| [validator_client-080](#validator_client-080) | Cache KDF output for shared salt and password | not | low | M | cpu, startup |
| [validator_client-085](#validator_client-085) | Skip key cache decrypt with no local keystores | implemented | low |  | cpu, memory, latency |
| [validator_client-091](#validator_client-091) | Use validator index from duties response | not | low | S | memory, latency, bandwidth |
| [validator_client-092](#validator_client-092) | Prune slashing protection database | implemented | medium |  | cpu, disk, latency |
| [validator_client-100](#validator_client-100) | Lazy default slashing protection records | implemented | low |  | disk, startup |
| [validator_client-101](#validator_client-101) | Per-validator slashing protection locks | not | low | L | cpu, memory, latency |
| [validator_client-108](#validator_client-108) | Sign a slot's attestations in parallel | implemented | medium |  | cpu, latency |
| [validator_client-111](#validator_client-111) | Parallel attestation aggregation across subnets | implemented | low |  | cpu, latency |
| [validator_client-113](#validator_client-113) | Fetch duty types and epochs concurrently | partial | low | S | latency |
| [validator_client-116](#validator_client-116) | Share one HTTP client per remote signer | implemented | medium |  | memory |
| [validator_client-119](#validator_client-119) **★** | Throttle concurrent remote signer requests | partial | medium | S | latency, bandwidth |
| [validator_client-127](#validator_client-127) | Poll next-epoch duties before boundary | implemented | low |  | latency |
| [validator_client-135](#validator_client-135) | Reuse duty data instead of extra requests | implemented | low |  | latency |
| [validator_client-138](#validator_client-138) | Memoize genesis from beacon node | implemented | low |  | latency |
| [validator_client-154](#validator_client-154) | Hoist registry scan out of per-key status | n/a | low |  | cpu |
| [validator_client-155](#validator_client-155) | Single-pass multi-key committee assignments | partial | low | S | cpu, memory, latency |
| [validator_client-157](#validator_client-157) | Avoid state copies for selection proof serving | n/a | low | S | cpu, memory, latency |

★ actionable. Click an id for the full record.

## Ideas

<a id="validator_client-001"></a>
<details>
<summary><b>validator_client-001</b> Look up validator statuses via POST body, not batched GET — <i>not · low · S · bandwidth, cpu, latency</i></summary>

**Idea.** In the validator client, query the beacon node for validator statuses/indices of many pubkeys with one POST request carrying the ids in the body, instead of many GET requests chunked to stay under URL length limits. Fewer round trips, and the beacon node filters its validator set once.

**Gap in Lighthouse.** Index discovery queries one pubkey per GET. Add a batched POST /eth/v1/beacon/states/head/validators with ids body to eth2 client and use it in poll_validator_indices for all unknown pubkeys.

**Impact.** Only startup and new-key discovery; saves N requests for N unregistered keys, minor.

**Best measured result.** None (pr:lodestar#6897)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:945-975`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L945-L975) poll_validator_indices does one get_beacon_states_validator_id GET per unknown pubkey
- grep post_beacon_states_validators in validator_client: no hits

**Sources.** [lodestar#6897](https://github.com/ChainSafe/lodestar/pull/6897), [teku#7786](https://github.com/Consensys-Incorporated/teku/pull/7786)

</details>


<a id="validator_client-002"></a>
<details>
<summary><b>validator_client-002</b> Batch pubkey-to-index and status lookups in large batches — <i>not · low · S · latency, bandwidth, startup</i></summary>

**Idea.** Resolve validator indices and statuses for all local keys with batched beacon API requests of large size (50-64+ pubkeys, or all at once, with bounded concurrency) instead of one request per validator, small batches of 10, or fetching the full validator set. Cuts round trips and BN load at startup and per epoch with many keys.

**Gap in Lighthouse.** Lookups are serial one-per-pubkey rather than batched. Batch unknown pubkeys into POST requests of large size in poll_validator_indices.

**Impact.** Cuts startup round trips with many keys (thousands of sequential requests); one-off cost.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:945-975`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L945-L975) per-pubkey GET, serial loop

**Sources.** [lodestar#2730](https://github.com/ChainSafe/lodestar/pull/2730), [teku#2947](https://github.com/Consensys-Incorporated/teku/pull/2947), [lodestar#2234](https://github.com/ChainSafe/lodestar/pull/2234), [teku#3379](https://github.com/Consensys-Incorporated/teku/pull/3379), [lodestar#5743](https://github.com/ChainSafe/lodestar/pull/5743), [teku#4306](https://github.com/Consensys-Incorporated/teku/pull/4306)

</details>


<a id="validator_client-004"></a>
<details>
<summary><b>validator_client-004</b> Subscribe to head event stream instead of polling — <i>implemented · medium · latency, bandwidth, cpu</i></summary>

**Idea.** Have the validator client subscribe to the beacon node SSE event stream (with reconnect) and cache head slot/root, instead of polling the head block every slot or second. Removes per-slot HTTP requests and learns of heads sooner.

**Impact.** Already done: no per-slot head polling.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/beacon_node_fallback/src/beacon_head_monitor.rs:136`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/beacon_node_fallback/src/beacon_head_monitor.rs#L136) poll_head_event_from_beacon_nodes subscribes to SSE head events
- [`validator_client/beacon_node_fallback/src/beacon_head_monitor.rs:90`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/beacon_node_fallback/src/beacon_head_monitor.rs#L90) BeaconHeadCache per-BN head cache
- [`validator_client/src/config.rs:143`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/src/config.rs#L143) enable_beacon_head_monitor defaults true

**Sources.** [prysm#13453](https://github.com/OffchainLabs/prysm/pull/13453), [prysm#13354](https://github.com/OffchainLabs/prysm/pull/13354), [lodestar#2824](https://github.com/ChainSafe/lodestar/pull/2824)

</details>


<a id="validator_client-005"></a>
<details>
<summary><b>validator_client-005</b> SSZ encoding for VC-BN block traffic — <i>partial · medium · S · bandwidth, cpu, latency</i></summary>

**Idea.** Request unsigned blocks and submit signed blocks (and other large objects) between validator client and beacon node as SSZ octet-stream instead of JSON, with JSON fallback chosen by content type and remembered after a 406. SSZ is smaller and cheaper to encode/decode, which matters for large blob-carrying blocks.

**Gap in Lighthouse.** Blocks (and Gloas payload attestations, proposer/builder preferences) go SSZ with a per-call JSON fallback, but no per-BN memory of a 406/failed SSZ (every proposal retries SSZ on all nodes first), and attestation data, aggregates, attestation/aggregate POSTs and sync contributions stay JSON even where the eth2 client already has SSZ methods.

**Impact.** Small: avoids one failed SSZ pass against non-SSZ BNs and trims JSON encode/decode on attestation traffic; negligible on localhost.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/block_service.rs:787`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/block_service.rs#L787) SSZ v3 block GET, JSON second pass at 805
- [`validator_client/validator_services/src/block_service.rs:707`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/block_service.rs#L707) SSZ v4 (Gloas) block production
- [`validator_client/validator_services/src/block_service.rs:1110`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/block_service.rs#L1110) post_beacon_blocks_v2_ssz / 1124 post_beacon_blinded_blocks_v2_ssz
- [`validator_client/validator_services/src/proposer_preferences_service.rs:215`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/proposer_preferences_service.rs#L215) SSZ with JSON fallback
- [`validator_client/validator_services/src/attestation_service.rs:284`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L284) get_validator_attestation_data (JSON) although [`common/eth2/src/lib.rs:3794`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2/src/lib.rs#L3794) get_validator_attestation_data_ssz exists
- [`validator_client/validator_services/src/attestation_service.rs:667`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L667) JSON aggregate GET although [`common/eth2/src/lib.rs:3976`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2/src/lib.rs#L3976) get_validator_aggregate_attestation_v2_ssz exists
- [`validator_client/validator_services/src/attestation_service.rs:585`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L585) JSON attestation POST

**Second check.** Searched the VC for any content-type/SSZ-support cache (none) and checked which eth2 SSZ client methods are unused by the VC (attestation data and aggregate SSZ GETs exist but are not called).

**Sources.** [teku#6575](https://github.com/Consensys-Incorporated/teku/pull/6575), [lighthouse#6523](https://github.com/sigp/lighthouse/pull/6523), [prysm#15645](https://github.com/OffchainLabs/prysm/pull/15645), [teku#5517](https://github.com/Consensys-Incorporated/teku/pull/5517), [nimbus#4999](https://github.com/status-im/nimbus-eth2/pull/4999), [teku#5513](https://github.com/Consensys-Incorporated/teku/pull/5513)

</details>


<a id="validator_client-007"></a>
<details>
<summary><b>validator_client-007</b> Attest as soon as the slot&#x27;s head block arrives — <i>implemented · medium · latency</i></summary>

**Idea.** Produce and publish attestations as soon as the block for the current slot is imported and becomes head (head/block event) instead of always waiting for the fixed 1/3-slot deadline or an extra delay, keeping the deadline as fallback. Attestations propagate earlier in the slot.

**Impact.** Already done.

**Best measured result.** None (pr:prysm#4791)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/attestation_service.rs:212`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L212) head_event_or_deadline waits for head event or 1/3 slot deadline
- [`validator_client/validator_services/src/attestation_service.rs:273-310`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L273-L310) attests from head-event BN, deadline fallback
- [`validator_client/beacon_node_fallback/src/beacon_head_monitor.rs:64`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/beacon_node_fallback/src/beacon_head_monitor.rs#L64) head_event_or_deadline

**Sources.** [prysm#17243](https://github.com/OffchainLabs/prysm/pull/17243), [grandine#955](https://github.com/grandinetech/grandine/pull/955), [lodestar@50f12944f](https://github.com/ChainSafe/lodestar/commit/50f12944fe91), [prysm#4791](https://github.com/OffchainLabs/prysm/pull/4791), [prysm#8827](https://github.com/OffchainLabs/prysm/pull/8827), [teku#2432](https://github.com/Consensys-Incorporated/teku/pull/2432), [grandine@f08b0a49d](https://github.com/grandinetech/grandine/commit/f08b0a49da7f), [prysm#15410](https://github.com/OffchainLabs/prysm/pull/15410), [lodestar#3397](https://github.com/ChainSafe/lodestar/pull/3397), [lighthouse#7892](https://github.com/sigp/lighthouse/pull/7892), [lodestar#4788](https://github.com/ChainSafe/lodestar/pull/4788), [grandine@2506dfffd](https://github.com/grandinetech/grandine/commit/2506dfffd2c6)

</details>


<a id="validator_client-008"></a>
<details>
<summary><b>validator_client-008</b> Request blinded blocks from the beacon node — <i>partial · medium · S · bandwidth, latency</i></summary>

**Idea.** Let the validator client request blinded blocks (also for locally built payloads) so the full execution payload does not travel between beacon node and validator client; the beacon node reassembles it on publish.

**Gap in Lighthouse.** The BN side is complete: GET validator/blinded_blocks blinds locally built payloads, caches them in the EL payload cache, and POST blinded_blocks reassembles from that cache. Only the VC is missing: it has no option to call get_validator_blinded_blocks(_ssz) for local proposals, so v3 sends the full payload. A VC flag that calls the blinded endpoint and posts via the existing blinded SSZ path would close it (pre-Gloas only).

**Impact.** Small: saves the payload+blobs transfer VC&lt;-&gt;BN per proposal; matters only for remote BNs, moot after Gloas.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/produce_block.rs:308`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/produce_block.rs#L308) produce_blinded_block_v2 uses BlockProductionVersion::BlindedV2
- [`beacon_node/execution_layer/src/lib.rs:1003`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1003) BlindedV2 path; 1033 blinds a local Full payload into Blinded
- [`beacon_node/execution_layer/src/lib.rs:651`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L651) cache_payload / 1319 get_full_payload_caching stores the local payload
- [`beacon_node/http_api/src/publish_blocks.rs:714`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L714) reconstruct_block unblinds from el.get_payload_by_root (local payload cache)
- [`beacon_node/http_api/src/lib.rs:2727`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L2727) GET validator/blinded_blocks route
- [`common/eth2/src/lib.rs:3738`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2/src/lib.rs#L3738) get_validator_blinded_blocks_ssz client method
- [`validator_client/validator_services/src/block_service.rs:794`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/block_service.rs#L794) VC only calls v3 (or v4) produce, never the blinded endpoint

**Second check.** The earlier review looked only at the VC v3 flow; the BN still has the blinded-v2 production path that blinds local payloads and reassembles them from execution_layer payload_cache on publish, and the eth2 client already exposes the method.

**Sources.** [teku#5030](https://github.com/Consensys-Incorporated/teku/pull/5030), [lodestar#6227](https://github.com/ChainSafe/lodestar/pull/6227)

</details>


<a id="validator_client-010"></a>
<details>
<summary><b>validator_client-010</b> Sync committee messages as soon as block seen — <i>implemented · low · latency</i></summary>

**Idea.** Sign and publish sync committee messages as soon as the slot's block/head event arrives instead of waiting for the 1/3-slot timer, avoiding the busiest moment.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/sync_committee_service.rs:131-173`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/sync_committee_service.rs#L131-L173) head_event_or_deadline triggers signing on head event
- [`validator_client/validator_services/src/sync_committee_service.rs:251`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/sync_committee_service.rs#L251) uses head event root directly

**Sources.** [lighthouse#9675](https://github.com/sigp/lighthouse/pull/9675), [lodestar#4615](https://github.com/ChainSafe/lodestar/pull/4615), [lodestar#4667](https://github.com/ChainSafe/lodestar/pull/4667)

</details>


<a id="validator_client-011"></a>
<details>
<summary><b>validator_client-011</b> Payload timeliness votes on payload-available event — <i>implemented · medium · latency, cpu</i></summary>

**Idea.** Have the beacon node push payload-available events to validator clients and cast PTC payload attestations as soon as the payload envelope and data columns are seen (deadline as fallback), signing one payload attestation per validator rather than per committee position.

**Impact.** Already done.

**Best measured result.** PTC vote at 4.51s vs 0.23s of a 6s slot (pr:prysm#17500)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/beacon_node_fallback/src/beacon_head_monitor.rs:248`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/beacon_node_fallback/src/beacon_head_monitor.rs#L248) poll_payload_available_event_from_beacon_nodes (ExecutionPayloadAvailable SSE)
- [`validator_client/validator_services/src/payload_attestation_service.rs:149`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/payload_attestation_service.rs#L149) early trigger vs deadline
- [`validator_client/validator_services/src/payload_attestation_service.rs:288-326`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/payload_attestation_service.rs#L288-L326) checks payload_present and blob_data_available
- [`validator_client/validator_services/src/payload_attestation_service.rs:380`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/payload_attestation_service.rs#L380) one sign per PtcDuty (per validator)

**Sources.** [grandine@d70201c05](https://github.com/grandinetech/grandine/commit/d70201c053ff), [lighthouse#9434](https://github.com/sigp/lighthouse/pull/9434), [nimbus#9054](https://github.com/status-im/nimbus-eth2/pull/9054), [prysm#17500](https://github.com/OffchainLabs/prysm/pull/17500)

</details>


<a id="validator_client-012"></a>
<details>
<summary><b>validator_client-012</b> Slim duties response without full committee lists — <i>implemented · low · bandwidth, cpu, latency</i></summary>

**Idea.** Have the validator client get committee length and its committee index from the duties response (or a lighter duties endpoint) instead of fetching full committee member lists or a separate committees API call each epoch, and do not re-check validators missing from state. Smaller responses and fewer state lookups.

**Best measured result.** saves 100-400ms in some cases; similar in the happy case (pr:prysm#15445)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:1448`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1448) post_validator_duties_attester is the only duties call
- [`validator_client/validator_services/src/duties_service.rs:158`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L158) uses duty.committee_length from the duties response
- [`common/eth2/src/types.rs:865`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2/src/types.rs#L865) AttesterData carries committee_length, committee_index, validator_committee_index

**Sources.** [prysm#15380](https://github.com/OffchainLabs/prysm/pull/15380), [prysm#15039](https://github.com/OffchainLabs/prysm/pull/15039), [prysm#15273](https://github.com/OffchainLabs/prysm/pull/15273), [prysm#15445](https://github.com/OffchainLabs/prysm/pull/15445)

</details>


<a id="validator_client-014"></a>
<details>
<summary><b>validator_client-014</b> Do not fetch all validators for activation-queue logging — <i>implemented · low · latency, bandwidth, cpu</i></summary>

**Idea.** Avoid fetching the full validator set or total validator count from the beacon API just to log activation queue position; these calls are very expensive (15-20s).

**Best measured result.** None (pr:prysm#12471)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/notifier_service.rs:109`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/notifier_service.rs#L109) total_validators from local validator_store.num_voting_validators()
- [`validator_client/validator_services/src/duties_service.rs:962`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L962) only per-pubkey lookups for unknown indices

**Sources.** [prysm#12471](https://github.com/OffchainLabs/prysm/pull/12471), [prysm#14600](https://github.com/OffchainLabs/prysm/pull/14600)

</details>


<a id="validator_client-018"></a>
<details>
<summary><b>validator_client-018</b> Prefetch next-epoch duties off the critical path — <i>partial · low · S · latency</i></summary>

**Idea.** Fetch next-epoch duties in the background mid-epoch and promote cached next-epoch duties to current at the boundary, refetching only failed duty types; never await the next-epoch fetch before slot-critical work like block notification. Slot-0 proposals no longer wait on a duties fetch.

**Gap in Lighthouse.** Proposer path still awaits next-epoch proposer fetch before the 'additional proposers' notification (upstream #9952 is still open); attester next-epoch duties are refetched inline rather than cached and promoted. Move the current_epoch+1 fetch in poll_beacon_proposers into a spawned task, and cache next-epoch attester duties and promote at the boundary.

**Impact.** Slot-0 proposals whose duty only arrives from the BN poll start up to one next-epoch request earlier (hundreds of ms in bad cases); no effect on node CPU.

**Best measured result.** None (pr:prysm#17268)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:739-751`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L739-L751) attester polling runs in its own spawned task
- [`validator_client/validator_services/src/duties_service.rs:1092`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1092) next-epoch attester duties re-fetched every poll, no promotion cache
- [`validator_client/validator_services/src/duties_service.rs:1844-1870`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1844-L1870) proposer poll notifies from cache first, then awaits current and next epoch fetch in a loop

**Sources.** [lighthouse#9952](https://github.com/sigp/lighthouse/pull/9952), [prysm#17268](https://github.com/OffchainLabs/prysm/pull/17268), [prysm#17036](https://github.com/OffchainLabs/prysm/pull/17036)

</details>


<a id="validator_client-019"></a>
<details>
<summary><b>validator_client-019</b> Batch attestation submission per slot — <i>implemented · medium · latency, cpu, bandwidth</i></summary>

**Idea.** Sign all attestations for a slot first, then submit them to the beacon node in one batched request instead of one HTTP request per validator or committee, ideally by default. Cuts round trips and beacon node load.

**Impact.** Already done: all attestations of a slot are signed first and posted in one request.

**Best measured result.** None (pr:prysm#17225)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/attestation_service.rs:496`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L496) sign_and_publish_attestations
- [`validator_client/lighthouse_validator_store/src/lib.rs:1022`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/lighthouse_validator_store/src/lib.rs#L1022) sign_attestations signs all concurrently, returns a batch
- [`validator_client/validator_services/src/attestation_service.rs:585`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L585) one post_beacon_pool_attestations_v2 per batch

**Sources.** [nimbus#7874](https://github.com/status-im/nimbus-eth2/pull/7874), [lodestar#3923](https://github.com/ChainSafe/lodestar/pull/3923), [prysm#17225](https://github.com/OffchainLabs/prysm/pull/17225), [teku#4252](https://github.com/Consensys-Incorporated/teku/pull/4252), [teku#4803](https://github.com/Consensys-Incorporated/teku/pull/4803), [prysm#13809](https://github.com/OffchainLabs/prysm/pull/13809), [teku#4515](https://github.com/Consensys-Incorporated/teku/pull/4515), [lodestar#2416](https://github.com/ChainSafe/lodestar/pull/2416)

</details>


<a id="validator_client-021"></a>
<details>
<summary><b>validator_client-021</b> Batch slashing-protection checks into one transaction — <i>implemented · medium · latency, disk, cpu</i></summary>

**Idea.** Sign attestations for a slot first, then check and register them all in the slashing-protection DB in one batched transaction (or a queue flushed periodically), rather than one check-and-write transaction per validator. One fsync per batch and no write-lock contention.

**Impact.** Already done.

**Best measured result.** None (pr:nimbus#5604)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/lighthouse_validator_store/src/lib.rs:1080`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/lighthouse_validator_store/src/lib.rs#L1080) slashing_protect_attestations in one blocking task after signing
- [`validator_client/slashing_protection/src/slashing_database.rs:652`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L652) check_and_insert_attestations (single transaction)

**Sources.** [prysm#5695](https://github.com/OffchainLabs/prysm/pull/5695), [lighthouse#8516](https://github.com/sigp/lighthouse/pull/8516), [lighthouse#6219](https://github.com/sigp/lighthouse/pull/6219), [nimbus#5604](https://github.com/status-im/nimbus-eth2/pull/5604), [prysm#8243](https://github.com/OffchainLabs/prysm/pull/8243)

</details>


<a id="validator_client-022"></a>
<details>
<summary><b>validator_client-022</b> Fewer DB transactions per slashing-protection check — <i>partial · low · M · latency, disk</i></summary>

**Idea.** Reduce DB round trips per slashing-protection check: combine check and register, and write the record plus lowest signed source/target updates in one transaction per signing, caching internal ids and relying on unique indexes for duplicates. Shortens write-lock hold time per signature.

**Gap in Lighthouse.** Attestations are batched per transaction and check+insert share a txn, but each item does a validator-id SELECT plus several check SELECTs and no id cache; block proposals are one txn each. Cache validator ids in SlashingDatabase and fold check queries (check_attestation, check_block_proposal).

**Impact.** Shorter write-lock hold per signing batch; matters mainly for VCs with thousands of keys (hundreds of ms per slot at most).

**Best measured result.** None (pr:prysm#8087)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/slashing_protection/src/slashing_database.rs:652`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L652) check_and_insert_attestations does a whole batch in one exclusive transaction
- [`validator_client/slashing_protection/src/slashing_database.rs:298`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L298) get_validator_id_in_txn re-queries the validator row per check
- [`validator_client/slashing_protection/src/slashing_database.rs:732`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L732) check then insert in the same txn
- [`validator_client/slashing_protection/src/slashing_database.rs:177`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L177) EXCLUSIVE locking mode

**Sources.** [prysm#8087](https://github.com/OffchainLabs/prysm/pull/8087), [prysm#8100](https://github.com/OffchainLabs/prysm/pull/8100), [nimbus#2528](https://github.com/status-im/nimbus-eth2/pull/2528), [prysm#8196](https://github.com/OffchainLabs/prysm/pull/8196)

</details>


<a id="validator_client-023"></a>
<details>
<summary><b>validator_client-023</b> Bounded batches for builder registrations — <i>implemented · low · bandwidth, latency</i></summary>

**Idea.** Send validator registrations to the builder API/relays in bounded, configurable batches (e.g. 200-1000) rather than one huge request, and skip a new run while the previous is in progress, so requests do not time out or hit size limits.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/preparation_service.rs:449`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/preparation_service.rs#L449) signed.chunks(validator_registration_batch_size)
- [`validator_client/validator_services/src/preparation_service.rs:187-210`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/preparation_service.rs#L187-L210) serial loop, next run only after the previous finishes
- [`validator_client/src/cli.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/src/cli.rs) validator-registration-batch-size flag

**Sources.** [prysm#13178](https://github.com/OffchainLabs/prysm/pull/13178), [prysm#14981](https://github.com/OffchainLabs/prysm/pull/14981), [teku#5829](https://github.com/Consensys-Incorporated/teku/pull/5829), [nimbus#4364](https://github.com/status-im/nimbus-eth2/pull/4364), [lighthouse#4399](https://github.com/sigp/lighthouse/pull/4399)

</details>


<a id="validator_client-025"></a>
<details>
<summary><b>validator_client-025</b> Decrypt validator keystores in parallel at startup — <i>not · low · S · startup, cpu</i></summary>

**Idea.** At validator client startup, read and run the keystore KDF decryption for each key in parallel across CPU cores (thread pool) instead of serially on the main thread. Each decryption is independent and CPU-heavy, so wall-clock load time drops roughly by core count.

**Gap in Lighthouse.** Cold start (no key cache, or after new keys) decrypts keystores one at a time. Run the decrypt step of from_definition for all enabled LocalKeystore defs concurrently (rayon par_iter or FuturesUnordered of spawn_blocking) in update_validators, then insert results serially.

**Impact.** Only first start or new-key import with many keys: wall-clock load drops roughly by core count (10k keys: hour to ~15 min per upstream estimate). Zero effect on steady state.

**Best measured result.** 10000 keys: about 1 hour serial vs 15 minutes with 8 cores (pr:lighthouse#1699)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/initialized_validators/src/lib.rs:1262-1283`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/initialized_validators/src/lib.rs#L1262-L1283) serial for loop awaiting InitializedValidator::from_definition per key
- [`validator_client/initialized_validators/src/lib.rs:260`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/initialized_validators/src/lib.rs#L260) spawn_blocking per key but awaited immediately
- [`validator_client/initialized_validators/src/key_cache.rs:187`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/initialized_validators/src/key_cache.rs#L187) key cache decrypts one blob so restarts skip KDF

**Sources.** [lodestar#5274](https://github.com/ChainSafe/lodestar/pull/5274), [grandine@fd640b3d2](https://github.com/grandinetech/grandine/commit/fd640b3d23bc), [grandine#252](https://github.com/grandinetech/grandine/pull/252), [lodestar#5623](https://github.com/ChainSafe/lodestar/pull/5623), [lighthouse#1699](https://github.com/sigp/lighthouse/pull/1699), [lodestar#5357](https://github.com/ChainSafe/lodestar/pull/5357), [prysm#6788](https://github.com/OffchainLabs/prysm/pull/6788), [teku#2437](https://github.com/Consensys-Incorporated/teku/pull/2437)

</details>


<a id="validator_client-026"></a>
<details>
<summary><b>validator_client-026</b> Faster crypto for keystore KDF — <i>not · low · S · startup, cpu</i></summary>

**Idea.** Use an optimized native/assembly (SHA-NI) scrypt/pbkdf2/SHA-256 implementation for keystore decryption instead of a generic one, cutting startup time with many keys (~3x).

**Gap in Lighthouse.** Keystore KDF uses generic RustCrypto pbkdf2/scrypt; no SHA-NI/asm-specific build. Enable sha2 'asm' or swap in an accelerated scrypt/pbkdf2 in eth2_keystore decrypt.

**Impact.** Only cold-start keystore decryption time, up to ~3x faster per key; no steady-state effect.

**Best measured result.** None (pr:lodestar#6253)

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/eth2_keystore/Cargo.toml:17-19`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/eth2_keystore/Cargo.toml#L17-L19) pbkdf2 0.12 and scrypt 0.11 pure-Rust RustCrypto, default-features=false
- [`crypto/eth2_keystore`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/eth2_keystore) sha2 workspace crate

**Sources.** [lodestar#6956](https://github.com/ChainSafe/lodestar/pull/6956), [lodestar#6253](https://github.com/ChainSafe/lodestar/pull/6253), [nimbus#4301](https://github.com/status-im/nimbus-eth2/pull/4301)

</details>


<a id="validator_client-029"></a>
<details>
<summary><b>validator_client-029</b> Bound interchange import target epochs — <i>n/a · low · cpu, disk</i></summary>

**Idea.** Reject imported attestations with target epoch beyond current+1, since span updates do one DB read per epoch and huge targets run effectively forever.

**Gap in Lighthouse.** Lighthouse slashing protection stores only min/max-style records and does no per-epoch span updates on import, so a huge target epoch costs nothing.

**Best measured result.** None (pr:lodestar#10170)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/slashing_protection/src/slashing_database.rs:853`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L853) import_interchange_record takes max source/target and writes one synthetic record

**Sources.** [lodestar#10170](https://github.com/ChainSafe/lodestar/pull/10170)

</details>


<a id="validator_client-034"></a>
<details>
<summary><b>validator_client-034</b> Fetch attestation data once per slot and reuse — <i>implemented · medium · latency, bandwidth, cpu</i></summary>

**Idea.** Fetch attestation data once per slot (post-Electra committee index is 0, so it is identical for all committees) and copy it per committee/validator before signing, instead of one beacon API call per validator or committee.

**Impact.** Already done: one attestation_data call per slot.

**Best measured result.** attestation_data calls over 100 slots on minimal: 398 -&gt; 100 (pr:lighthouse#8171)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/attestation_service.rs:300`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L300) get_validator_attestation_data(slot, 0) once per slot
- [`validator_client/validator_services/src/attestation_service.rs:349`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L349) shared attestation_data cloned for all duties

**Sources.** [prysm#16236](https://github.com/OffchainLabs/prysm/pull/16236), [lodestar#3917](https://github.com/ChainSafe/lodestar/pull/3917), [lighthouse#8171](https://github.com/sigp/lighthouse/pull/8171), [teku#9620](https://github.com/Consensys-Incorporated/teku/pull/9620), [lodestar#7958](https://github.com/ChainSafe/lodestar/pull/7958)

</details>


<a id="validator_client-036"></a>
<details>
<summary><b>validator_client-036</b> Cache signed builder registrations — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Cache signed validator registrations per pubkey and only re-sign when fee recipient or gas limit changes, instead of re-creating and re-signing every epoch.

**Impact.** Already avoids re-signing; nothing left.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/preparation_service.rs:124`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/preparation_service.rs#L124) validator_registration_cache keyed by (fee_recipient,gas_limit,pubkey)
- [`validator_client/validator_services/src/preparation_service.rs:396`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/preparation_service.rs#L396) reuses cached signed registration

**Sources.** [nimbus#4040](https://github.com/status-im/nimbus-eth2/pull/4040), [prysm#11014](https://github.com/OffchainLabs/prysm/pull/11014), [lodestar#4447](https://github.com/ChainSafe/lodestar/pull/4447)

</details>


<a id="validator_client-038"></a>
<details>
<summary><b>validator_client-038</b> Register only active validators with builders — <i>partial · low · S · cpu, bandwidth</i></summary>

**Idea.** Filter unknown, pending and exited validators out of builder registrations before signing and sending them.

**Gap in Lighthouse.** Only validators without an index are skipped; pending, exited and withdrawn validators with an index are still registered. Would need status in ProposalData and a filter in collect_validator_registration_keys.

**Impact.** Saves a few BLS signs and builder POST entries for exited validators; negligible.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/preparation_service.rs:294`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/preparation_service.rs#L294) collect_validator_registration_keys skips keys with no validator_index
- [`validator_client/validator_services/src/preparation_service.rs:316`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/preparation_service.rs#L316) collect_proposal_data uses all voting pubkeys

**Sources.** [teku#7423](https://github.com/Consensys-Incorporated/teku/pull/7423), [teku#6313](https://github.com/Consensys-Incorporated/teku/pull/6313), [teku#6100](https://github.com/Consensys-Incorporated/teku/pull/6100)

</details>


<a id="validator_client-040"></a>
<details>
<summary><b>validator_client-040</b> One encrypted store for all keys, one KDF — <i>implemented · low · S · startup, cpu, memory</i></summary>

**Idea.** Keep all decrypted validator secret keys in one store or cache file encrypted by one password (or the concatenated passwords), so startup runs one KDF instead of one per keystore; verify pubkeys on load and update the cache asynchronously.

**Impact.** Startup KDF runs once instead of per keystore (already shipped).

**Best measured result.** None (pr:lighthouse#1695)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/initialized_validators/src/key_cache.rs:36`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/initialized_validators/src/key_cache.rs#L36) KeyCache
- [`validator_client/initialized_validators/src/lib.rs:685`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/initialized_validators/src/lib.rs#L685) key cache opened/updated on validator changes

**Sources.** [lodestar#5043](https://github.com/ChainSafe/lodestar/pull/5043), [lighthouse#1695](https://github.com/sigp/lighthouse/pull/1695), [prysm#6823](https://github.com/OffchainLabs/prysm/pull/6823)

</details>


<a id="validator_client-041"></a>
<details>
<summary><b>validator_client-041</b> Cache signing domain data per epoch — <i>n/a · low · S · latency, bandwidth</i></summary>

**Idea.** Cache signing domains (including selection proof and aggregate domains) per (epoch, domain type) in the validator client instead of asking the beacon node on every signature.

**Impact.** Lighthouse VC never asks the beacon node for domains; computes locally from spec, so there is no round trip to cache.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/lighthouse_validator_store/src/lib.rs:279`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/lighthouse_validator_store/src/lib.rs#L279) signing_context built locally from spec and fork
- [`validator_client/lighthouse_validator_store/src/lib.rs:493`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/lighthouse_validator_store/src/lib.rs#L493) domain_hash computed locally

**Sources.** [prysm#5931](https://github.com/OffchainLabs/prysm/pull/5931), [prysm#5726](https://github.com/OffchainLabs/prysm/pull/5726), [prysm#13263](https://github.com/OffchainLabs/prysm/pull/13263), [prysm#4914](https://github.com/OffchainLabs/prysm/pull/4914)

</details>


<a id="validator_client-044"></a>
<details>
<summary><b>validator_client-044</b> Cache aggregator selection proofs — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Cache aggregator selection proofs / slot signatures per (validator, slot) or by message in a small bounded cache pruned each epoch, so the same BLS signature is not computed twice.

**Impact.** Each proof is signed once per duty and kept with the duty until pruned.

**Best measured result.** None (pr:lodestar#3897)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:101`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L101) DutyAndProof stores selection_proof
- [`validator_client/validator_services/src/duties_service.rs:1507`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1507) existing proof kept if dependent_root unchanged

**Sources.** [lodestar#3897](https://github.com/ChainSafe/lodestar/pull/3897), [nimbus#2949](https://github.com/status-im/nimbus-eth2/pull/2949), [lighthouse#3223](https://github.com/sigp/lighthouse/pull/3223)

</details>


<a id="validator_client-046"></a>
<details>
<summary><b>validator_client-046</b> Cache own validator index — <i>implemented · low · S · latency, bandwidth</i></summary>

**Idea.** Fetch the validator index once (startup or duty update) and cache it instead of looking it up before every duty.

**Impact.** Index is cached in the validator definition; no per-duty lookup.

**Best measured result.** None (pr:prysm#4406)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:1003`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1003) index resolved once, stored via set_validator_index
- [`validator_client/lighthouse_validator_store/src/lib.rs:845`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/lighthouse_validator_store/src/lib.rs#L845) validator_index reads cached index

**Sources.** [prysm#4406](https://github.com/OffchainLabs/prysm/pull/4406), [prysm#1701](https://github.com/OffchainLabs/prysm/pull/1701)

</details>


<a id="validator_client-055"></a>
<details>
<summary><b>validator_client-055</b> Refetch duties only when dependent root changes — <i>partial · medium · S · bandwidth, cpu, latency</i></summary>

**Idea.** Invalidate and refetch attester/proposer duties only when the duties' dependent root changes (as reported by head events), rotating cached next-epoch duties into current at the boundary and polling otherwise once per epoch, instead of repolling every slot or on every reorg. The dependent root must be computed correctly or duties recompute constantly.

**Gap in Lighthouse.** The dependent root already gates the full refetch. But two probe POSTs (current and next epoch) still go out every slot, and the proposer duties are polled every slot. A head monitor exists, but HeadEvent has no previous_duty_dependent_root/current_duty_dependent_root and duties_service does not subscribe to it. To close the gap: add the dependent roots to HeadEvent, and probe only when they change, with a once-per-epoch fallback.

**Impact.** Saves about 2 small duties POSTs per slot per VC. That is negligible for one VC and matters only for BNs that serve many VCs.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:739-760`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L739-L760) attester poll loop runs every slot on a timer
- [`validator_client/validator_services/src/duties_service.rs:1066-1103`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1066-L1103) probes both current and next epoch every slot
- [`validator_client/validator_services/src/duties_service.rs:1240-1275`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1240-L1275) small probe of INITIAL_DUTIES_QUERY_SIZE indices; full refetch only if dependent_root differs
- [`validator_client/beacon_node_fallback/src/beacon_head_monitor.rs:17-21`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/beacon_node_fallback/src/beacon_head_monitor.rs#L17-L21) HeadEvent carries only slot and block root, no dependent roots
- [`validator_client/src/lib.rs:439-440`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/src/lib.rs#L439-L440),565,586 head events go only to attestation and sync committee services, not to duties_service

**Second check.** I found the beacon_head_monitor head-event subscription, which the earlier review did not mention. It only drives attestation and sync committee timing, and its event drops the dependent roots, so the verdict stays partial.

**Sources.** [teku#10384](https://github.com/Consensys-Incorporated/teku/pull/10384), [teku#3434](https://github.com/Consensys-Incorporated/teku/pull/3434), [nimbus#8877](https://github.com/status-im/nimbus-eth2/pull/8877), [lighthouse#4170](https://github.com/sigp/lighthouse/pull/4170), [prysm#16421](https://github.com/OffchainLabs/prysm/pull/16421)

</details>


<a id="validator_client-056"></a>
<details>
<summary><b>validator_client-056</b> Fetch duties once per epoch, serve slots from cache — <i>implemented · low · S · bandwidth, latency, cpu</i></summary>

**Idea.** Fetch attester and proposer duty assignments once per epoch (or when missing or the dependent root changes) and serve per-slot checks and attestation routines from the cache, instead of polling the beacon node every slot.

**Impact.** Per slot cost is one 1-index probe request; full duty fetch only on epoch change or reorg. Per-slot checks served from the local map.

**Best measured result.** 32 requests to 1 per epoch (pr:lighthouse#8905)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:49`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L49) INITIAL_DUTIES_QUERY_SIZE=1 probe
- [`validator_client/validator_services/src/duties_service.rs:1256`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1256) full fetch only if dependent_root differs or duties missing
- [`validator_client/validator_services/src/duties_service.rs:1031`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1031) poll_beacon_attesters

**Sources.** [prysm#2166](https://github.com/OffchainLabs/prysm/pull/2166), [prysm#2412](https://github.com/OffchainLabs/prysm/pull/2412), [lighthouse#9461](https://github.com/sigp/lighthouse/pull/9461), [lighthouse#8573](https://github.com/sigp/lighthouse/pull/8573), [lighthouse#8574](https://github.com/sigp/lighthouse/pull/8574), [lighthouse#8905](https://github.com/sigp/lighthouse/pull/8905)

</details>


<a id="validator_client-057"></a>
<details>
<summary><b>validator_client-057</b> Short lookahead, per-slot batches for selection proofs — <i>implemented · low · S · cpu, bandwidth, latency</i></summary>

**Idea.** Precompute aggregator/sync selection proofs only a few slots ahead, signing them in small per-slot batches, instead of 32 slots ahead or thousands of signing tasks at epoch start. Avoids wasted signing, remote signer load and contention with duty signing.

**Impact.** Proofs are signed in per-slot batches shortly before the slot, not 32 slots ahead.

**Best measured result.** with 5k validators replaces 5k tasks with 1 task signing ~160 proofs per slot; graphs show lower median signing time (pr:lighthouse#4033)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:121`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L121) SelectionProofConfig lookahead_slot default 0
- [`validator_client/validator_services/src/duties_service.rs:1581`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1581) fill_in_selection_proofs signs per slot batches
- [`validator_client/validator_services/src/duties_service.rs:1618`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1618) only lookahead_slot duties taken per tick

**Sources.** [nimbus#9416](https://github.com/status-im/nimbus-eth2/pull/9416), [nimbus#6609](https://github.com/status-im/nimbus-eth2/pull/6609), [lighthouse#4033](https://github.com/sigp/lighthouse/pull/4033)

</details>


<a id="validator_client-059"></a>
<details>
<summary><b>validator_client-059</b> Decrypt keystores before waiting for beacon node — <i>implemented · low · startup</i></summary>

**Idea.** Decrypt validator keystores at startup before waiting for the beacon node or genesis so the first slots are not missed.

**Impact.** Startup already decrypts before waiting for BN/genesis; nothing to gain.

**Best measured result.** None (pr:lighthouse#1299)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/src/lib.rs:207`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/src/lib.rs#L207) InitializedValidators::from_definitions (decrypts keystores) runs in Validator::new
- [`validator_client/src/lib.rs:388`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/src/lib.rs#L388) beacon genesis/BN wait comes later

**Sources.** [lighthouse#1299](https://github.com/sigp/lighthouse/pull/1299)

</details>


<a id="validator_client-063"></a>
<details>
<summary><b>validator_client-063</b> Batch committee subnet subscriptions — <i>implemented · low · latency, bandwidth</i></summary>

**Idea.** Send all committee subnet subscriptions for a slot/epoch to the beacon node in one batched request instead of one call per duty.

**Impact.** Already one batched request per poll.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:1151-1172`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1151-L1172) collects all duties into one Vec and sends a single post_validator_beacon_committee_subscriptions

**Sources.** [prysm#5332](https://github.com/OffchainLabs/prysm/pull/5332), [teku#2990](https://github.com/Consensys-Incorporated/teku/pull/2990), [lodestar@e4ef843f8](https://github.com/ChainSafe/lodestar/commit/e4ef843f8cd8)

</details>


<a id="validator_client-074"></a>
<details>
<summary><b>validator_client-074</b> Event-driven wait for activation — <i>partial · low · S · latency</i></summary>

**Idea.** Wake the wait-for-activation loop on key-change notifications instead of polling every 30s, so new keys are picked up immediately.

**Gap in Lighthouse.** Lighthouse has no 30s wait-for-activation loop; it re-polls unknown validators every slot (12s), not event-driven on key import. A new key waits up to one slot. Could notify the indices task from add_validator_keystore (tokio Notify) to poll immediately.

**Impact.** Negligible on a mainnet node; only shaves up to 12s off picking up a freshly imported key.

**Best measured result.** None (pr:prysm#13448)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:686`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L686) poll_validator_indices loop runs once per slot
- [`validator_client/validator_services/src/duties_service.rs:911`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L911) unknown pubkeys re-queried each slot (once per epoch backoff)
- [`validator_client/src/lib.rs:646`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/src/lib.rs#L646) pre-genesis poll

**Sources.** [prysm#13448](https://github.com/OffchainLabs/prysm/pull/13448)

</details>


<a id="validator_client-077"></a>
<details>
<summary><b>validator_client-077</b> Parallel keystore decryption for keymanager API imports — <i>not · low · M · cpu, latency</i></summary>

**Idea.** Decrypt keystores imported through the keymanager API in a queued parallel worker pool rather than serially, keeping the duty path free while KDF work runs.

**Gap in Lighthouse.** In import_keystores / import_single_keystore, run decrypt_keypair for all keystores in parallel (rayon or JoinSet of spawn_blocking), then add the validated keys; also avoid the double decryption by passing the decrypted keypair through.

**Impact.** Bulk keymanager imports of many keys (scrypt ~1s each, done twice) would be several times faster with cores; no effect on steady-state duties.

**Best measured result.** ~5x faster import of many keys (pr:lodestar#5624)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/http_api/src/keystores.rs:104-131`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/http_api/src/keystores.rs#L104-L131) keystores imported in a serial for loop
- [`validator_client/http_api/src/keystores.rs:198-218`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/http_api/src/keystores.rs#L198-L218) import_single_keystore decrypts once to validate then block_on(add_validator_keystore) decrypts again
- initialized_validators/src/lib.rs:260 spawn_blocking decrypt, one at a time

**Sources.** [lodestar#5624](https://github.com/ChainSafe/lodestar/pull/5624)

</details>


<a id="validator_client-080"></a>
<details>
<summary><b>validator_client-080</b> Cache KDF output for shared salt and password — <i>not · low · M · cpu, startup</i></summary>

**Idea.** When many keystores share the same KDF salt and password, cache the derived decryption key so the expensive KDF runs once, not per keystore.

**Gap in Lighthouse.** No cache keyed on (salt,password,kdf params). Note keystore KDF output depends on the keystore's own salt and Lighthouse-generated keystores have random salts, so benefit only exists for externally generated keystores sharing salt. Would need a derived-key cache in from_definition / Keystore::decrypt_keypair; the key cache already removes KDF cost on restarts.

**Impact.** Only first startup or first import of many same-salt keystores; restarts already hit the key cache. Seconds per key saved at most.

**Best measured result.** significantly improve decoding performance for keystores with single salt and password (pr:nimbus#4372)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/initialized_validators/src/lib.rs:229-300`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/initialized_validators/src/lib.rs#L229-L300) from_definition decrypts every keystore independently via decrypt_keypair
- [`validator_client/initialized_validators/src/key_cache.rs:36-80`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/initialized_validators/src/key_cache.rs#L36-L80) KeyCache stores one master-encrypted cache so restarts run only one KDF

**Sources.** [nimbus#4372](https://github.com/status-im/nimbus-eth2/pull/4372)

</details>


<a id="validator_client-085"></a>
<details>
<summary><b>validator_client-085</b> Skip key cache decrypt with no local keystores — <i>implemented · low · cpu, memory, latency</i></summary>

**Idea.** Do not decrypt or save the keystore key cache (scrypt) when no local keystore validators exist, e.g. only remote-signer keys.

**Impact.** Remote-signer-only setups already skip key cache decrypt and save.

**Best measured result.** Excessive CPU / slow PATCH validators with hundreds of keys; no numbers (pr:lighthouse#4126)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/initialized_validators/src/lib.rs:1255-1261`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/initialized_validators/src/lib.rs#L1255-L1261) has_local_definitions gate: KeyCache::new() instead of decrypt_key_cache when only Web3Signer
- [`validator_client/initialized_validators/src/lib.rs:1391`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/initialized_validators/src/lib.rs#L1391) save only if has_local_definitions &amp;&amp; is_modified

**Sources.** [lighthouse#4126](https://github.com/sigp/lighthouse/pull/4126)

</details>


<a id="validator_client-091"></a>
<details>
<summary><b>validator_client-091</b> Use validator index from duties response — <i>not · low · S · memory, latency, bandwidth</i></summary>

**Idea.** Take validator indices from the duties response (or include them there) instead of separate per-validator index lookups and a VC-side pubkey-to-index map.

**Gap in Lighthouse.** Duties are requested by index, so the index must be known first; Lighthouse resolves it with one HTTP call per validator. Batch via POST /eth/v1/beacon/states/head/validators with ids=[pubkeys] in poll_validator_indices (chunked), then set_validator_index for each result.

**Impact.** Startup and key-import with thousands of keys drops from thousands of BN requests to a handful; steady state unaffected (known indices are cached).

**Best measured result.** "thousands of requests" avoided (pr:prysm#4567)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:911-1010`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L911-L1010) poll_validator_indices does one GET states/head/validators/{pubkey} per unknown pubkey, sequentially
- [`validator_client/validator_services/src/duties_service.rs:1058`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1058),1281 indices used to request duties

**Sources.** [prysm#4567](https://github.com/OffchainLabs/prysm/pull/4567), [prysm#4634](https://github.com/OffchainLabs/prysm/pull/4634)

</details>


<a id="validator_client-092"></a>
<details>
<summary><b>validator_client-092</b> Prune slashing protection database — <i>implemented · medium · cpu, disk, latency</i></summary>

**Idea.** Periodically (and at startup) prune slashing-protection block/attestation records older than a horizon, relying on low-watermark guards, so tables stay small and signing checks stay fast.

**Best measured result.** about 0.5s for 1000 validators and 54,000 epochs (pr:prysm#8221)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/lighthouse_validator_store/src/lib.rs:1372-1415`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/lighthouse_validator_store/src/lib.rs#L1372-L1415) prune_slashing_protection_db prunes attestations and blocks via prune_all_signed_*
- [`validator_client/src/lib.rs:476`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/src/lib.rs#L476) first_run prune at startup
- [`validator_client/validator_services/src/attestation_service.rs:816`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L816) periodic prune

**Sources.** [lighthouse#8522](https://github.com/sigp/lighthouse/pull/8522), [prysm#8221](https://github.com/OffchainLabs/prysm/pull/8221), [nimbus#5551](https://github.com/status-im/nimbus-eth2/pull/5551), [lighthouse#2194](https://github.com/sigp/lighthouse/pull/2194)

</details>


<a id="validator_client-100"></a>
<details>
<summary><b>validator_client-100</b> Lazy default slashing protection records — <i>implemented · low · disk, startup</i></summary>

**Idea.** Return defaults when a key has no slashing-protection entry instead of pre-writing a default record per key at startup, avoiding N transactions on launch.

**Impact.** Rows are still pre-written at startup but in one transaction, not N, so the bottleneck the idea targets is absent.

**Best measured result.** removes a bottleneck for starting a validator client by no longer creating N validator DB transactions (pr:prysm#5323)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/src/lib.rs:265-268`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/src/lib.rs#L265-L268) register_validators for all voting pubkeys in a single call
- [`validator_client/slashing_protection/src/slashing_database.rs:214-218`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L214-L218) one with_transaction for all keys, prepared statement reused

**Sources.** [prysm#5323](https://github.com/OffchainLabs/prysm/pull/5323)

</details>


<a id="validator_client-101"></a>
<details>
<summary><b>validator_client-101</b> Per-validator slashing protection locks — <i>not · low · L · cpu, memory, latency</i></summary>

**Idea.** Replace the global lock around slashing-protection check-and-record with per-validator locks so distinct validators sign concurrently; only shared storage writes stay serialized.

**Gap in Lighthouse.** Slashing DB is one SQLite file with pool size 1 and EXCLUSIVE transactions, so all signers serialize on it; no per-validator locks. Would need per-key in-memory state with async flush in SlashingDatabase::check_and_insert_*.

**Impact.** Little on a normal node: attestations are batched into one txn per slot, so the lock is held briefly. Matters only for thousands of keys on slow disks.

**Best measured result.** about 2Gb memory for 1000 validating keys (pr:prysm#8086)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/slashing_protection/src/slashing_database.rs:20`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L20) POOL_SIZE=1 single sqlite connection
- [`validator_client/slashing_protection/src/slashing_database.rs:646`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L646) check_and_insert_attestations: one Exclusive txn per batch
- [`validator_client/slashing_protection/src/slashing_database.rs:589`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L589) block check also Exclusive txn

**Sources.** [prysm#8083](https://github.com/OffchainLabs/prysm/pull/8083), [prysm#8086](https://github.com/OffchainLabs/prysm/pull/8086), [teku#7819](https://github.com/Consensys-Incorporated/teku/pull/7819), [teku#7858](https://github.com/Consensys-Incorporated/teku/pull/7858)

</details>


<a id="validator_client-108"></a>
<details>
<summary><b>validator_client-108</b> Sign a slot&#x27;s attestations in parallel — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** Issue all per-validator signatures for a slot concurrently (CPU thread pool for local BLS, concurrent requests for a remote signer) instead of one after another, so the last attestation is published sooner.

**Best measured result.** Sequential 32 votes published from 1.61 s to ~2.3 s into the slot; 2/3-wide aggregate p50 6.49 s vs block build at 6.40 s (pr:ethlambda#655)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/lighthouse_validator_store/src/lib.rs:1020-1045`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/lighthouse_validator_store/src/lib.rs#L1020-L1045) sign_attestations join_all over per-validator futures
- [`validator_client/lighthouse_validator_store/src/lib.rs:1085`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/lighthouse_validator_store/src/lib.rs#L1085) spawn_blocking_handle for local BLS

**Sources.** [ethlambda#655](https://github.com/lambdaclass/ethlambda/pull/655), [lighthouse#8523](https://github.com/sigp/lighthouse/pull/8523), [teku#2571](https://github.com/Consensys-Incorporated/teku/pull/2571), [lodestar#3926](https://github.com/ChainSafe/lodestar/pull/3926)

</details>


<a id="validator_client-111"></a>
<details>
<summary><b>validator_client-111</b> Parallel attestation aggregation across subnets — <i>implemented · low · cpu, latency</i></summary>

**Idea.** Run aggregation duties for different subnets/committees concurrently instead of sequentially.

**Impact.** Aggregation per committee index (per subnet) already runs as concurrent tasks.

**Best measured result.** reduces aggregation time ~80% if you run more than 10 validators (pr:prysm#12699)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/attestation_service.rs:395-425`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L395-L425) per committee_index spawn_ignoring_error(handle_aggregates)

**Sources.** [prysm#12699](https://github.com/OffchainLabs/prysm/pull/12699)

</details>


<a id="validator_client-113"></a>
<details>
<summary><b>validator_client-113</b> Fetch duty types and epochs concurrently — <i>partial · low · S · latency</i></summary>

**Idea.** Fetch current and next epoch duties, and attester, proposer and sync duties within each, concurrently instead of sequentially.

**Gap in Lighthouse.** Duty types run as independent tasks, but within attesters current and next epoch are fetched one after the other (poll_beacon_attesters), and likewise in poll_beacon_proposers. Wrap the two epoch calls in futures::join!.

**Impact.** Halves duty polling latency at epoch boundaries for large key sets; mostly background, not critical path.

**Best measured result.** reduces the time to fetch duties from ~8-9s to ~2.5s (pr:prysm#13789)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:683-857`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L683-L857) separate spawned tasks for proposers, attesters, sync, PTC, IL
- [`validator_client/validator_services/src/duties_service.rs:1066`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1066) and :1090 current then next epoch attester fetch awaited sequentially
- [`validator_client/validator_services/src/duties_service.rs:1863`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1863) proposer epochs fetched in sequential for loop

**Sources.** [prysm#13789](https://github.com/OffchainLabs/prysm/pull/13789)

</details>


<a id="validator_client-116"></a>
<details>
<summary><b>validator_client-116</b> Share one HTTP client per remote signer — <i>implemented · medium · memory</i></summary>

**Idea.** Create one HTTP client per remote signer URL and reuse it for all validators and requests, so connections are pooled and memory/sockets do not scale per key.

**Best measured result.** VC with 200 keys on Web3Signer: ~200MB to ~50MB (pr:lighthouse#3335)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/initialized_validators/src/lib.rs:327-356`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/initialized_validators/src/lib.rs#L327-L356) web3_signer_client_map keyed by Web3SignerDefinition, client cloned per validator
- [`validator_client/initialized_validators/src/lib.rs:440-451`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/initialized_validators/src/lib.rs#L440-L451) build_web3_signer_client

**Sources.** [teku#2553](https://github.com/Consensys-Incorporated/teku/pull/2553), [lighthouse#3335](https://github.com/sigp/lighthouse/pull/3335)

</details>


<a id="validator_client-119"></a>
<details>
<summary><b>validator_client-119</b> Throttle concurrent remote signer requests — <i>partial · medium · S · latency, bandwidth</i></summary>

**Idea.** Queue signing requests to the remote signer and cap in-flight requests, since epoch-boundary selection proofs for all keys arrive in bulk.

**Gap in Lighthouse.** The burst this idea targets (selection proofs for all keys at the epoch boundary) is already removed: default mode signs them serially and spreads them across slots. What is still missing is a general cap on in-flight remote-signer requests. Per-slot attestation and aggregate signing uses join_all with no bound, and the DVT/parallel_sign mode signs selection proofs with no bound. To close the gap, add a Semaphore around the Web3Signer requests in SigningMethod.

**Impact.** Small. The epoch-boundary burst is already gone in default mode. A general cap would only smooth the per-slot signing of about 1/32 of the keys, or help DVT setups.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:1596-1625`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1596-L1625) attestation selection proofs are signed in per-slot batches at mid-slot with a lookahead, not all at the epoch boundary
- [`validator_client/validator_services/src/duties_service.rs:1666-1679`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1666-L1679) in the default (non-DVT) mode, selection proofs are signed serially (stream::iter().then(), one request in flight)
- [`validator_client/src/lib.rs:68-74`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/src/lib.rs#L68-L74),488-511 defaults: lookahead 8 slots, offset slot/2, parallel_sign=false for non-distributed mode
- [`validator_client/validator_services/src/sync.rs:636-680`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/sync.rs#L636-L680) the FuturesUnordered unbounded path runs only when parallel_sign is set (DVT)
- [`validator_client/initialized_validators/src/lib.rs:448-451`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/initialized_validators/src/lib.rs#L448-L451) the web3signer reqwest client sets only pool_max_idle_per_host, with no in-flight cap
- [`validator_client/lighthouse_validator_store/src/lib.rs:1228-1341`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/lighthouse_validator_store/src/lib.rs#L1228-L1341) attestation signing uses join_all with no cap

**Second check.** The earlier review searched only for Semaphore/buffer_unordered. It missed that fill_in_selection_proofs signs serially and in per-slot batches (lookahead 8, mid-slot), which is a scheduling equivalent of throttling the selection-proof burst.

**Sources.** [teku#3381](https://github.com/Consensys-Incorporated/teku/pull/3381)

</details>


<a id="validator_client-127"></a>
<details>
<summary><b>validator_client-127</b> Poll next-epoch duties before boundary — <i>implemented · low · latency</i></summary>

**Idea.** Fetch next-epoch proposer duties shortly before the epoch boundary, after the BN precomputes the next-epoch state, so the first-slot proposer is known without delay.

**Impact.** Next-epoch proposer duties are fetched every slot of the previous epoch, so the first-slot proposer is cached at the boundary.

**Best measured result.** polling at epoch start wasted up to 2 s causing missed proposals (pr:lodestar#5794)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:709-715`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L709-L715) proposer poll runs at the start of every slot
- [`validator_client/validator_services/src/duties_service.rs:1863`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1863) fetches current_epoch and current_epoch+1 every slot

**Sources.** [lodestar#5794](https://github.com/ChainSafe/lodestar/pull/5794)

</details>


<a id="validator_client-135"></a>
<details>
<summary><b>validator_client-135</b> Reuse duty data instead of extra requests — <i>implemented · low · latency</i></summary>

**Idea.** Use data already in the duty (committees per slot, committee length, aggregator index) for subnet subscription and aggregation rather than re-querying the BN.

**Impact.** Subscriptions and aggregator selection use fields already in AttesterData; no extra BN requests.

**Best measured result.** reduces the time needed to subscribe from 1-2 seconds to 1 millisecond (pr:prysm#13702)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:1150-1155`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1150-L1155) BeaconCommitteeSubscription built from duty.committees_at_slot and selection_proof.is_some()
- [`validator_client/validator_services/src/duties_service.rs:158`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L158) is_aggregator uses duty.committee_length

**Sources.** [prysm#13702](https://github.com/OffchainLabs/prysm/pull/13702), [prysm#13711](https://github.com/OffchainLabs/prysm/pull/13711)

</details>


<a id="validator_client-138"></a>
<details>
<summary><b>validator_client-138</b> Memoize genesis from beacon node — <i>implemented · low · latency</i></summary>

**Idea.** Fetch genesis info once and memoize it rather than requesting it on every call.

**Impact.** Genesis is fetched once at startup and passed by value.

**Best measured result.** for 1024 keys as many as 7 requests per second, becoming 1 total (pr:prysm#13796)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/src/lib.rs:388-395`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/src/lib.rs#L388-L395) genesis fetched once at startup
- [`validator_client/src/lib.rs:832`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/src/lib.rs#L832) only get_beacon_genesis call in the VC

**Sources.** [prysm#13796](https://github.com/OffchainLabs/prysm/pull/13796)

</details>


<a id="validator_client-154"></a>
<details>
<summary><b>validator_client-154</b> Hoist registry scan out of per-key status — <i>n/a · low · cpu</i></summary>

**Idea.** When resolving status for many pubkeys, compute the last-active-validator index once per state instead of per pubkey.

**Impact.** The VC resolves pubkey to index per key via the BN pubkey cache; there is no last-active-validator registry scan to hoist.

**Best measured result.** for large operators this is a strain (no numbers) (pr:prysm#12487)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:911-1000`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L911-L1000) resolves index per unknown pubkey via get_beacon_states_validator_id
- [`beacon_node/http_api/src/attester_duties.rs:210`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L210) pubkey lookups via pubkey cache

**Sources.** [prysm#12487](https://github.com/OffchainLabs/prysm/pull/12487)

</details>


<a id="validator_client-155"></a>
<details>
<summary><b>validator_client-155</b> Single-pass multi-key committee assignments — <i>partial · low · S · cpu, memory, latency</i></summary>

**Idea.** Compute committee assignments for all requested keys in one pass over the epoch's committees instead of per-key scans.

**Gap in Lighthouse.** No O(validators) scan per key (shuffled_position is O(1)), but each index scans up to 2048 committees to find its range. A binary search over compute_committee_range in CommitteeCache::get_attestation_duties would remove it.

**Impact.** Negligible: a few thousand integer comparisons per key per epoch on the BN.

**Best measured result.** 16k validators: 182708160 ns/op, 85 MB/op; previously over 4 minutes for 8k validators (pr:prysm#4294)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/committee_cache.rs:295`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L295) get_attestation_duties: O(1) shuffled_position then linear scan over committees per validator
- [`beacon_node/http_api/src/attester_duties.rs:15`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L15) per-index duties from cached CommitteeCache

**Sources.** [prysm#4294](https://github.com/OffchainLabs/prysm/pull/4294)

</details>


<a id="validator_client-157"></a>
<details>
<summary><b>validator_client-157</b> Avoid state copies for selection proof serving — <i>n/a · low · S · cpu, memory, latency</i></summary>

**Idea.** Compute active indices and seed from the shared head state rather than copying the state several times per aggregate-selection request.

**Impact.** None: no per-request state copies exist on this path, and BeaconState clones are cheap (milhouse persistent tree).

**Best measured result.** reduces 3 state copies to 1 per call (pr:prysm#5813)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/aggregate_attestation.rs:12`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/aggregate_attestation.rs#L12) get_aggregate_attestation looks up the naive aggregation pool by data root, no state load or copy
- Lighthouse selection proofs are signed in the validator client; the BN endpoint does not compute active indices or seed

**Sources.** [prysm#5813](https://github.com/OffchainLabs/prysm/pull/5813)

</details>


