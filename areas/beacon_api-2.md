# beacon_api (part 2 of 2)

305 ideas: 34 not, 66 partial, 148 implemented, 57 n/a; 35 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

Pages: [part 1](beacon_api.md) · [part 2](beacon_api-2.md)

<a id="beacon_api-160"></a>
<details>
<summary><b>beacon_api-160</b> Keep column recovery queue in memory — <i>n/a · low · memory, disk, sync</i></summary>

**Idea.** Keep the column sidecar recovery queue in memory instead of persisting it in the database, and start blob/column downloads only when the node is synced.

**Impact.** Lighthouse does not persist a recovery queue in the DB; it is already in memory.

**Evidence (Lighthouse @ 928b61e719).**

- overflow_lru_cache.rs:73 pending components in memory
- network/src/network_beacon_processor/mod.rs:1213 reconstruction runs from memory

**Sources.** [caplin#16428](https://github.com/erigontech/erigon/pull/16428)

</details>


<a id="beacon_api-161"></a>
<details>
<summary><b>beacon_api-161</b> Serve blob by-root fetches from quarantine directly — <i>n/a · low · bandwidth, sync</i></summary>

**Idea.** Remove the async queue for blob by-root requests and compute the missing blobs directly from the quarantine, deduplicating and dropping stale requests.

**Impact.** No async quarantine queue exists; by-root requests are answered directly from store/cache.

**Evidence (Lighthouse @ 928b61e719).**

- network/src/network_beacon_processor/rpc_methods.rs:673 blobs-by-root served by direct lookup, no quarantine queue

**Sources.** [nimbus#5198](https://github.com/status-im/nimbus-eth2/pull/5198)

</details>


<a id="beacon_api-162"></a>
<details>
<summary><b>beacon_api-162</b> Skip gossip proof checks for EL-supplied blobs — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** When all blobs of a block come from the local EL, mark the block available and skip gossip KZG and inclusion proof verification, keeping a KZG check before persistence.

**Impact.** EL-supplied blob data skips KZG and inclusion-proof verification and goes straight to the DA checker; LH has no separate KZG check before persistence (it trusts the EL).

**Best measured result.** "doesn't call kzg proof verification and inclusion proof verification for 9 blobs per slot"; "faster block import (in happy cases)" (pr:nimbus#6913)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:627`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L627) v4 EL partial columns wrapped with KzgVerifiedPartialDataColumn::from_execution_verified
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:704`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L704) v2/v3 EL-computed columns wrapped with from_execution_verified (no KZG proof or inclusion proof check)
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:632-652`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L632-L652) dedup against gossip-observed and DA-cached columns

**Skeptic check.** Verified that both the v2/v3 and v4 getBlobs paths build columns as execution-verified and only filter against already-seen columns. The pre-Fulu blob path no longer exists, so no other path is uncovered. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#6913](https://github.com/status-im/nimbus-eth2/pull/6913)

</details>


<a id="beacon_api-163"></a>
<details>
<summary><b>beacon_api-163</b> Cache column inclusion proof results — <i>partial · medium · S · cpu</i></summary>

**Idea.** Cache the result of the KZG commitments inclusion proof check per block (key: hash of proof inputs) so other column sidecars of the same block skip the merkle proof.

**Gap in Lighthouse.** There is a per-block verify-once cache of the header and inclusion proof, but only on the partial-columns path, which is opt-in (--enable-partial-columns, default off). Full DataColumnSidecar gossip still recomputes kzg_commitments.tree_hash_root() and the merkle proof for each column of the same block. The fix: in verify_column_inclusion_proof, compare against a cached verified (block_root, commitments_root, proof), or reuse the assembler header cache for full columns.

**Impact.** Saves a commitments tree-hash and a short merkle proof for each additional custody column per block. A few hundred microseconds to a few ms of CPU per slot. Small.

**Best measured result.** 'reduce redundant work' when verifying inclusion proofs; no numbers (pr:prysm#15217)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2488-2497`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2488-L2497) verify_partial_data_column_header_for_gossip returns the cached header from the partial assembler on an equality match, and skips the inclusion proof
- [`beacon_node/beacon_chain/src/data_column_verification.rs:647`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L647) verify_partial_column_header_inclusion_proof runs only for the first header per block, then assembler.init caches it (line 666)
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1331-1334`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1331-L1334) partial columns without a header reuse the cached verified header (new_from_cached)
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1160-1176`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1160-L1176) full columns already in the DA cache (from EL or partials) return PriorKnownUnpublished before verify_column_inclusion_proof
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1178`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1178) full gossip columns still call verify_column_inclusion_proof every time
- [`beacon_node/beacon_chain/src/chain_config.rs:184`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/chain_config.rs#L184) enable_partial_columns defaults to false

**Second check.** The earlier review missed the partial-column header cache (PartialDataColumnAssembler get_header/init). That cache does verify once per block and then checks equality, but only when partial columns are enabled. Full columns that are already known also skip the proof through missing_cells_for_column_sidecar.

**Verdict history.** not (checked) → partial (refuted)

**Sources.** [prysm#15217](https://github.com/OffchainLabs/prysm/pull/15217)

</details>


<a id="beacon_api-164"></a>
<details>
<summary><b>beacon_api-164</b> Late DA check with per-block sampling tracker — <i>implemented · medium · S · disk, latency, bandwidth</i></summary>

**Idea.** Track sampled columns per block in memory as they arrive by gossip, EL or RPC, fetch only the missing ones by RPC, and run the availability check as late as possible to give gossip and EL more time.

**Gap in Lighthouse.** Minor: the cache snapshot is taken once, in custody_lookup_request; columns already in flight are not dropped from the request if they arrive by gossip or EL first.

**Impact.** LH defers RPC column fetches until peers corroborate the root and fetches only the missing columns. Re-filtering in-flight requests would only remove occasional duplicate downloads.

**Best measured result.** fewer RPC calls (no numbers) (pr:teku#10006)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1972-1978`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1972-L1978) MissingComponents on a gossip block only logs; no RPC lookup started
- [`beacon_node/network/src/sync/manager.rs:1036-1056`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L1036-L1056) handle_unknown_block_root needs corroboration from unknown_root_min_peers peers
- [`beacon_node/network/src/sync/network_context.rs:956-990`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L956-L990) custody_lookup_request fetches only sampling columns not in cached_data_column_indexes
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:177`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L177) cached_data_column_indexes is the per-block tracker for gossip, EL and RPC columns

**Second check.** Checked what starts RPC for a gossip block with missing components. Nothing does: the RPC fallback runs only from unknown-root events coming from attestations or columns, after corroboration from several peers. This is in effect Teku's late RPC/DA fallback. Eager availability checks on each arrival do not cause RPC, so they are not a gap.

**Skeptic check.** Re-read the gossip MissingComponents arm, the corroboration gate and the custody request filter; all match the cited lines. The earlier verdict and its small refinement gap were accurate.

**Verdict history.** partial (checked) → implemented (refuted) → implemented (skeptic)

**Sources.** [teku#10006](https://github.com/Consensys-Incorporated/teku/pull/10006)

</details>


<a id="beacon_api-165"></a>
<details>
<summary><b>beacon_api-165</b> Retry getBlobs until block columns are built — <i>partial · medium · S · latency, bandwidth</i></summary>

**Idea.** Poll engine_getBlobs again with short timeouts, triggered per gossip block, until the columns of a block without sidecars can be built from EL blobs.

**Gap in Lighthouse.** Lighthouse re-calls getBlobs once per distinct arrival event (partial header, gossip block, RPC lookup block, HTTP publish), so a block can get 2-3 independent attempts, but there is no timed re-poll after the last trigger misses. Add a bounded retry with short timeouts in fetch_engine_blobs_and_publish_full until the block is available or the slot cutoff passes.

**Impact.** Covers blobs that reach the EL mempool after the last trigger; builds more columns locally, saving download bandwidth and import latency. Probably modest gain because multiple event triggers already exist.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1123-1133`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1123-L1133) getBlobs triggered when a partial-column header is first seen
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1936`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1936) getBlobs triggered again (spawn_fetch_block_columns) when the gossip block is verified
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:211-222`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L211-L222) getBlobs triggered again for an RPC lookup block that is MissingComponents
- [`beacon_node/network/src/service.rs:692-702`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L692-L702) FetchBlockColumns for HTTP-published blocks
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:132-240`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L132-L240) no dedup/in-flight guard, no retry loop; miss returns Ok(None)
- [`beacon_node/execution_layer/src/engine_api/http.rs:74`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L74) ENGINE_GET_BLOBS_TIMEOUT 1s

**Second check.** Beyond the earlier review, found that getBlobs runs on several separate events (partial header and gossip block both, with no dedup), which is an event-driven re-attempt but not the timed polling the idea describes.

**Verdict history.** not (checked) → partial (refuted)

**Sources.** [nimbus#8012](https://github.com/status-im/nimbus-eth2/pull/8012), [nimbus#7445](https://github.com/status-im/nimbus-eth2/pull/7445)

</details>


<a id="beacon_api-166"></a>
<details>
<summary><b>beacon_api-166</b> Dedicated executor queue for DA tasks — <i>n/a · low · latency</i></summary>

**Idea.** Give data availability tasks their own async executor queue so they do not exhaust the shared operation pool and get rejected.

**Impact.** Beacon processor already has separate bounded queues for DA work, so it cannot exhaust a shared pool.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:953`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L953),1118 separate per-work-type queues (column reconstruction, rpc blob, gossip column)

**Sources.** [teku#9657](https://github.com/Consensys-Incorporated/teku/pull/9657)

</details>


<a id="beacon_api-167"></a>
<details>
<summary><b>beacon_api-167</b> Per-block-root cache of pending state queues — <i>not · low · M · cpu, latency</i></summary>

**Idea.** Keep per-block-root LRU caches of pending deposit, consolidation and partial-withdrawal queues in fork choice so the pending-queue API endpoints are served without loading or rebuilding a state.

**Gap in Lighthouse.** Add per-block-root caches of pending deposit/consolidation/withdrawal queues in fork choice or beacon chain and serve non-head state_ids from them in get_beacon_state_pending_* in states.rs.

**Impact.** Head queries already use the in-memory head state; only non-head state ids load a state. Rare endpoints, little gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/beacon/states.rs:273-303`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L273-L303) pending_deposits loads state via state_id and clones the list
- [`beacon_node/http_api/src/state_id.rs:218-242`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L218-L242) head state used directly, no load

**Sources.** [caplin#16231](https://github.com/erigontech/erigon/pull/16231)

</details>


<a id="beacon_api-168"></a>
<details>
<summary><b>beacon_api-168</b> Serve history from archived per-epoch data — <i>not · low · L · cpu, disk, latency</i></summary>

**Idea.** Archive compact per-epoch data (committee seed, active indices, proposer, balances) so historical duty and balance API queries read small records instead of regenerating or loading historical states.

**Gap in Lighthouse.** Archive compact per-epoch records (seed, active indices, proposer, balances) at finalization and read them in attester_duties.rs and states.rs committees/validator_balances for old epochs.

**Impact.** Old-epoch duty/balance queries would stop needing hdiff state reconstruction; matters only for explorer/archive API users.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/attester_duties.rs:120-145`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L120-L145) historical duties load state at epoch start slot and rebuild committee cache
- [`beacon_node/store/src/metadata.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/metadata.rs) hdiff store, no per-epoch archive of committees/balances

**Sources.** [prysm#3559](https://github.com/OffchainLabs/prysm/pull/3559), [prysm#3536](https://github.com/OffchainLabs/prysm/pull/3536)

</details>


<a id="beacon_api-169"></a>
<details>
<summary><b>beacon_api-169</b> Cache or compute shuffling dependent root once — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Compute the spec shuffling dependent root once per epoch from the head view and reuse it in duties and head events, avoiding per-request recomputation and byte/hex conversions; a stable value also stops validator clients refetching duties on every head.

**Impact.** Negligible; the hot duties path already uses the cached shuffling and its decision root.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/attester_duties.rs:45-80`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L45-L80)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1747-1763`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1747-L1763)
- [`beacon_node/beacon_chain/src/canonical_head.rs:1240-1244`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1240-L1244)

**Skeptic check.** The current and next epoch duties go through cached_attestation_duties, then with_committee_cache, which returns the dependent root with the cached shuffling. Only historic requests compute it from a state, with an O(1) block_roots lookup. The head event does an O(1) lookup per head and has no hex round-trips. The earlier verdict was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#4382](https://github.com/ChainSafe/lodestar/pull/4382), [caplin#24393](https://github.com/erigontech/erigon/pull/24393)

</details>


<a id="beacon_api-170"></a>
<details>
<summary><b>beacon_api-170</b> Compact merkle multiproof responses — <i>not · low · M · bandwidth, cpu</i></summary>

**Idea.** Serve proofs for several generalized indices as a deduplicated multiproof (shared nodes only) rather than one proof per path, shrinking responses.

**Gap in Lighthouse.** Would need a new state proof endpoint in http_api using milhouse/tree_hash multiproof generation; none exists.

**Impact.** No mainnet node cost; only a niche API with smaller responses for proof consumers.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs): no state proof route
- [`beacon_node/http_api/src/light_client.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/light_client.rs) bootstrap only

**Sources.** [lodestar#5155](https://github.com/ChainSafe/lodestar/pull/5155)

</details>


<a id="beacon_api-171"></a>
<details>
<summary><b>beacon_api-171</b> Narrow state-field and count endpoints — <i>partial · low · S · bandwidth, cpu, latency</i></summary>

**Idea.** Expose dedicated endpoints returning only a small piece of state (counts, a single field, committee for a slot) computed from caches, so consumers do not fetch and serialize the full state or validator set.

**Gap in Lighthouse.** Narrow endpoints mostly exist; missing a standard validator-count endpoint and serving non-head cases from caches instead of loaded states.

**Impact.** Consumers avoid fetching the full state; head requests already cheap, so gain is small.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs:622`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L622) finality_checkpoints, :690 states/ptc
- [`beacon_node/http_api/src/beacon/states.rs:586`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L586) committees, :273 pending_*, :431 sync_committees
- [`beacon_node/http_api/src/lib.rs:3068`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L3068) lighthouse/ui/validator_count

**Sources.** [prysm#12752](https://github.com/OffchainLabs/prysm/pull/12752), [lodestar#10190](https://github.com/ChainSafe/lodestar/pull/10190), [lodestar#7245](https://github.com/ChainSafe/lodestar/pull/7245), [lodestar#10189](https://github.com/ChainSafe/lodestar/pull/10189), [nimbus#6675](https://github.com/status-im/nimbus-eth2/pull/6675)

</details>


<a id="beacon_api-172"></a>
<details>
<summary><b>beacon_api-172</b> Delete dead computation in API handlers — <i>n/a · low · S · cpu</i></summary>

**Idea.** Remove per-request work in API handlers whose results are never read, such as full validator set scans or tree hashing, since they cost CPU with no consumer.

**Gap in Lighthouse.** The cited dead work was specific to Caplin/Prysm handlers; none found in a spot check (not a full audit).

**Impact.** None identified.

**Evidence (Lighthouse @ 928b61e719).**

- spot check of [`beacon_node/http_api/src`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src) handlers only

**Sources.** [caplin#24518](https://github.com/erigontech/erigon/pull/24518), [prysm#17009](https://github.com/OffchainLabs/prysm/pull/17009)

</details>


<a id="beacon_api-173"></a>
<details>
<summary><b>beacon_api-173</b> Do not sign API response bodies — <i>implemented · low · S · cpu</i></summary>

**Idea.** Do not hash and sign every HTTP API response body in the validator API, and skip client verification, saving CPU per request.

**Impact.** Already removed by lighthouse#5529.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/http_api/src/api_secret.rs:24`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/http_api/src/api_secret.rs#L24)
- [`common/eth2/src/lighthouse_vc/http_client.rs:124`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2/src/lighthouse_vc/http_client.rs#L124)

**Skeptic check.** api_secret.rs says the VC response signing and the secp256k1 key were removed. There is no signing or verification code left in the VC http_api or its client.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#5529](https://github.com/sigp/lighthouse/pull/5529)

</details>


<a id="beacon_api-174"></a>
<details>
<summary><b>beacon_api-174</b> Node-side cache of produced payload envelope — <i>implemented · low · S · latency</i></summary>

**Idea.** Keep the proposer-built execution payload envelope in a node-side cache and return it with the block so a stateless validator client needs no extra round trip or state.

**Impact.** Stateless VC mode with no extra envelope round trip.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/produce_block.rs:57-125`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/produce_block.rs#L57-L125)
- [`validator_client/validator_services/src/block_service.rs:281-345`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/block_service.rs#L281-L345)
- [`validator_client/validator_services/src/block_service.rs:702-750`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/block_service.rs#L702-L750)
- [`beacon_node/http_api/src/validator/execution_payload_envelopes.rs:51`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/execution_payload_envelopes.rs#L51)
- [`beacon_node/beacon_chain/src/block_production/gloas.rs:920`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/gloas.rs#L920)

**Skeptic check.** The earlier evidence cited only the separate GET from pending_payload_envelopes, which still costs a round trip. produce_block_v4 also takes include_payload and returns BlockAndEnvelope, and the VC uses it under --stateless-block-production. This matches Prysm's opt-in stateless block v4.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#16699](https://github.com/OffchainLabs/prysm/pull/16699)

</details>


<a id="beacon_api-175"></a>
<details>
<summary><b>beacon_api-175</b> Filter inactive validators from builder registrations — <i>implemented · low · S · bandwidth, cpu</i></summary>

**Idea.** Drop registrations of exited or slashed validators before forwarding them to the builder, so fewer registrations are sent and processed.

**Impact.** Already filters out inactive validators before forwarding to the builder.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/validator/mod.rs:730-760`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L730-L760)

**Skeptic check.** register_validator gets each validator from the head state and keeps only the Pending or Active superstatus before it sends registrations to the builder. Unknown pubkeys are also dropped.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#3473](https://github.com/sigp/lighthouse/pull/3473)

</details>


<a id="beacon_api-176"></a>
<details>
<summary><b>beacon_api-176</b> Resolve roots from fork choice before database — <i>partial · low · S · disk, latency</i></summary>

**Idea.** In API handlers, check in-memory fork choice (finalization status, highest received slot and root) before the database, falling back to disk only on a miss.

**Gap in Lighthouse.** Head/Finalized/Justified come from cached head with no DB. By-root lookups hit the hot DB first; fork choice is not consulted for existence/slot. In BlockId::root, check fork choice proto-array for Root ids first.

**Impact.** Saves a DB key check and block load per by-root API call on recent blocks; API is not hot.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/block_id.rs:75-96`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L75-L96) Slot uses block_root_at_slot
- [`beacon_node/http_api/src/block_id.rs:105-131`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L105-L131) Root: store.block_exists (hot DB) then blinded block load; fork choice only for optimistic flag
- [`beacon_node/beacon_chain/src/beacon_chain.rs:631`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L631) is_finalized_block uses cached_head

**Sources.** [prysm#11803](https://github.com/OffchainLabs/prysm/pull/11803), [prysm#14380](https://github.com/OffchainLabs/prysm/pull/14380)

</details>


<a id="beacon_api-177"></a>
<details>
<summary><b>beacon_api-177</b> Render JSON responses in place into buffer — <i>not · low · M · memory, cpu</i></summary>

**Idea.** Render JSON directly into the response buffer, writing Content-Length as padded whitespace filled in afterwards, avoiding a second body buffer and copy.

**Gap in Lighthouse.** Responses are serialized to a buffer and then handed to hyper; no in-place Content-Length padding. Would need a custom streaming writer.

**Impact.** Saves one copy on very large JSON responses; heavy clients use SSZ.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs): replies built with warp json into a separate buffer
- [`common/warp_utils/src/json.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/warp_utils/src/json.rs) request parsing only

**Sources.** [silver#278](https://github.com/gattaca-com/silver/pull/278)

</details>


<a id="beacon_api-178"></a>
<details>
<summary><b>beacon_api-178</b> Serve REST directly without gRPC proxy layer — <i>n/a · low · S · cpu, latency</i></summary>

**Idea.** Serve the REST API straight from handlers rather than through a proxy that converts to and from gRPC and re-serializes JSON, removing a hop and a serialization round trip.

**Gap in Lighthouse.** Lighthouse serves REST directly with no gRPC gateway.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs) warp handlers call beacon_chain directly

**Sources.** [prysm#13243](https://github.com/OffchainLabs/prysm/pull/13243)

</details>


<a id="beacon_api-179"></a>
<details>
<summary><b>beacon_api-179</b> Skip blob and column lookups when none can exist — <i>partial · low · S · disk, latency</i></summary>

**Idea.** In blob and data column sidecar APIs, return empty without touching storage for pre-fork blocks or blocks with no KZG commitments, and avoid loading payloads to test emptiness.

**Gap in Lighthouse.** Blob path already skips storage. Data column path still queries the column store for commitment-less post-Fulu blocks. Add a blob_kzg_commitments().is_empty() early return in BlockId::get_data_columns.

**Impact.** Avoids a DB read for empty blocks on a rarely called API; marginal.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/block_id.rs:292-306`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L292-L306) get_data_columns rejects pre-Fulu but loads the block first and never checks blob_kzg_commitments empty
- [`beacon_node/http_api/src/block_id.rs:359-387`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L359-L387) blob path skips storage when commitments empty

**Sources.** [lodestar#8336](https://github.com/ChainSafe/lodestar/pull/8336), [teku#7453](https://github.com/Consensys-Incorporated/teku/pull/7453), [teku#10209](https://github.com/Consensys-Incorporated/teku/pull/10209), [teku#10333](https://github.com/Consensys-Incorporated/teku/pull/10333)

</details>


<a id="beacon_api-L000"></a>
<details>
<summary><b>beacon_api-L000</b> parent root index — <i>n/a · low · cpu, latency</i></summary>

**Idea.** Add a secondary index parent_root -&gt; list of block roots so headers-by-parent queries do a lookup instead of scanning.

**Impact.** Lookup is a short iterator scan from parent slot to the first non-skipped root; no scan of all blocks, so an index gains almost nothing.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs:729-756`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L729-L756) parent_root query uses block lookup plus forwards_iter_block_roots from the parent slot

**Sources.** [caplin#11729](https://github.com/erigontech/erigon/pull/11729)

</details>


<a id="beacon_api-L001"></a>
<details>
<summary><b>beacon_api-L001</b> narrow lock scope, drop caches — <i>n/a · low · memory, cpu, latency</i></summary>

**Idea.** Release the shared state lock as early as possible during aggregate processing, and drop debug-only diff structures and compression of random 32-byte hash caches, which cost memory and allocations for no gain.

**Impact.** Go/Caplin-specific lock scope and debug diff structures have no counterpart in Lighthouse.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs) (no Caplin-style debug diff structures); aggregate processing uses fine-grained locks

**Sources.** [caplin#12571](https://github.com/erigontech/erigon/pull/12571)

</details>


<a id="beacon_api-L002"></a>
<details>
<summary><b>beacon_api-L002</b> pre-commit overlay notifications — <i>n/a · low · latency</i></summary>

**Idea.** Publish head/state-change notifications to RPC subscribers from the in-memory overlay before the DB commit finishes, so latest-state queries do not wait on disk.

**Impact.** Lighthouse has no DB overlay; latest-state queries read the in-memory cached head, not disk.

**Best measured result.** responsiveness not throughput; no numbers

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs): head is in an in-memory cached_head, SSE events fire from memory

**Sources.** [caplin#20195](https://github.com/erigontech/erigon/pull/20195)

</details>


<a id="beacon_api-L003"></a>
<details>
<summary><b>beacon_api-L003</b> pre-sized direct JSON encoding — <i>partial · low · S · cpu, latency, memory</i></summary>

**Idea.** For large JSON responses (blobs bundle), marshal directly into one pre-sized buffer with in-place hex encoding and write the already-encoded result verbatim through the RPC handler and codec, avoiding repeated reflection marshalling and compact re-scans of the payload.

**Gap in Lighthouse.** Rust serde is typed (no reflection), so the 10x reflection cost does not exist. Remaining: each blob is hex-encoded into two temporary Strings and the output Vec is not pre-sized. A hex-into-buffer serializer in ssz_types hex_fixed_vec plus a pre-sized body in blocking_json_task would remove it.

**Impact.** Blob/data-column JSON endpoints allocate ~2 extra copies per 128KB blob; small CPU saving on a rarely hit API, likely tens of percent on that call at most.

**Best measured result.** getBlobsV3 128 blobs: 309 ms -&gt; 29 ms (~10.6x); marshal 16,516 allocs -&gt; 1

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/task_spawner.rs:102`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/task_spawner.rs#L102) warp::reply::json -&gt; serde_json::to_vec, unsized growing Vec
- ~/.cargo ssz_types-0.14.1/src/serde_utils/hex_fixed_vec.rs:11 hex::encode builds String per blob
- ethereum_serde_utils-0.8.1/src/hex.rs:7-12 second String via '0x' prefix copy

**Sources.** [caplin#21606](https://github.com/erigontech/erigon/pull/21606)

</details>


<a id="beacon_api-L004"></a>
<details>
<summary><b>beacon_api-L004</b> publish head before state copy — <i>partial · medium · S · latency</i></summary>

**Idea.** Publish the selected fork-choice head (root, slot) atomically at selection time, before the state copy, and serve identity-only API endpoints from it, so public handlers need not wait ~750 ms for the memoized head state or trigger fork-choice work on a cache miss.

**Gap in Lighthouse.** API handlers never block on head computation (they read the previous CachedHead), but the new head root/slot is only published after the state load/advance and cache build. Publish (root, slot) atomically right after new_view is chosen in recompute_head_at_slot_internal and serve identity-only endpoints from it.

**Impact.** Removes lag of head root/header endpoints behind fork choice; small in steady state because the post-import state is normally a state-cache hit.

**Best measured result.** block/root endpoints lagged ~750 ms behind the selected head

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:1106-1160`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1106-L1160) new snapshot (get_full_block, get_advanced_hot_state, build_all_caches) built before cached_head write lock; only then is the new root visible
- [`beacon_node/http_api/src/block_id.rs:48-57`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L48-L57) BlockId::Head root reads canonical_head.head_and_execution_status() (old snapshot, no waiting)

**Second check.** Checked the BlockId::Head path and recompute_head: no early-published head identity exists; Lighthouse avoids the waiting half of the problem (handlers read the stale snapshot) but not the lag.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [caplin#23155](https://github.com/erigontech/erigon/pull/23155)

</details>


<a id="beacon_api-L005"></a>
<details>
<summary><b>beacon_api-L005</b> serialize lists without copy — <i>not · low · S · memory, cpu</i></summary>

**Idea.** Serialize the state's pending deposit, withdrawal and consolidation lists directly to JSON/SSZ through a trait object rather than copying them into new lists with different limits.

**Gap in Lighthouse.** In get_beacon_state_pending_{deposits,partial_withdrawals,consolidations}, serialize the milhouse List directly (or iterate) instead of to_owned_list() into a Vec.

**Impact.** Saves one Vec copy per request on rarely-called endpoints; pending_deposits can be large but call frequency is low.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/beacon/states.rs:58`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L58),118,298 call to_owned_list() on pending consolidations/withdrawals/deposits, then as_ssz_bytes / JSON

**Sources.** [grandine#968](https://github.com/grandinetech/grandine/pull/968)

</details>


<a id="beacon_api-L006"></a>
<details>
<summary><b>beacon_api-L006</b> time-based skip slot limit — <i>not · low · S · latency</i></summary>

**Idea.** Bound state skip-slot work by time rather than a fixed slot count.

**Gap in Lighthouse.** Add a time budget (Instant check) inside the while loop in the state-at-slot function and return an error when exceeded; the warn at 1543 does not bound work.

**Impact.** Protects API/duty requests from unbounded skip-slot work on a long-stalled chain; no gain in normal operation.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:1535-1580`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1535-L1580) state_at_slot loops per_slot_processing with only a warn when skipping more than an epoch

**Sources.** [lighthouse#639](https://github.com/sigp/lighthouse/pull/639)

</details>


<a id="beacon_api-L007"></a>
<details>
<summary><b>beacon_api-L007</b> remove rayon deadlock — <i>implemented · low · S · latency, cpu</i></summary>

**Idea.** Remove rayon parallelism from HTTP handlers because it deadlocked when combined with the blocking executor.

**Impact.** HTTP handlers do not use rayon parallelism directly, so the handler-level deadlock that PR #1562 removed is gone.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/Cargo.toml`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/Cargo.toml): no rayon dependency
- [`beacon_node/http_api/src`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src): no rayon or par_iter use (grep empty)

**Skeptic check.** Confirmed with grep that http_api has no rayon use. This is a correctness fix more than a performance idea. Shared code that handlers call can still use rayon internally, but that is not the pattern PR #1562 removed.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#1562](https://github.com/sigp/lighthouse/pull/1562)

</details>


<a id="beacon_api-L008"></a>
<details>
<summary><b>beacon_api-L008</b> server-side validator filter — <i>implemented · low · S · bandwidth, cpu</i></summary>

**Idea.** Let the validators endpoint filter by validator id and status server-side, so clients fetch only the validators they need instead of the whole registry.

**Impact.** Clients get only the validators they request. The registry is still scanned linearly (no direct index or pubkey-cache lookup), but this cost is small next to serialization.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/validators.rs:24-33`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validators.rs#L24-L33) id and status HashSet filters
- [`beacon_node/http_api/src/validators.rs:36-72`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validators.rs#L36-L72) filters applied while iterating, and only matches are cloned and serialized
- [`beacon_node/http_api/src/validators.rs:105-118`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validators.rs#L105-L118) same id filter for balances

**Skeptic check.** Filtering by id and status happens server-side as the idea says. A possible further step is a direct index or pubkey-cache lookup for small id lists, but that goes beyond this idea.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#1803](https://github.com/sigp/lighthouse/pull/1803)

</details>


<a id="beacon_api-L009"></a>
<details>
<summary><b>beacon_api-L009</b> skip proposer cache for future epoch — <i>implemented · low · S · cpu</i></summary>

**Idea.** For proposer duties requests on the next epoch, bypass the proposer cache because its dependent root changes each slot, so the cache would only be washed out by useless entries.

**Impact.** Next-epoch requests do not fill the proposer cache with useless entries, so block processing keeps its cached entries.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/proposer_duties.rs:81-89`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/proposer_duties.rs#L81-L89) only current/tolerant-current epoch reads or writes beacon_proposer_cache
- [`beacon_node/http_api/src/proposer_duties.rs:90-108`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/proposer_duties.rs#L90-L108) next epoch computed via compute_proposer_duties_from_head with no cache insert
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:254-310`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L254-L310) compute_proposer_duties_from_head does not touch the cache

**Skeptic check.** Confirmed that the next-epoch branch does not insert into the cache. Post-Fulu the next-epoch lookahead is deterministic, so caching it could now be safe, but that is a different idea.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#2963](https://github.com/sigp/lighthouse/pull/2963)

</details>


<a id="beacon_api-L010"></a>
<details>
<summary><b>beacon_api-L010</b> historic committee cache from randao — <i>partial · medium · S · latency, cpu</i></summary>

**Idea.** Serve historic committee queries by building a committee cache for the requested past epoch directly from randao mixes in a recent state, instead of replaying to a state at that epoch.

**Gap in Lighthouse.** Only GET beacon/states/{id}/committees uses CommitteeCache::initialized for past epochs. compute_historic_attester_duties (POST validator/duties/attester/{epoch} for a past epoch) loads a full state with StateId::from_slot(request_epoch.start_slot), which replays from cold storage, and then calls build_committee_cache. It could build the committee cache from the head state's randao mixes (and reuse HistoricalCommitteeCache), as the committees endpoint does.

**Impact.** Historic attester-duty queries would skip state replay (seconds to minutes) for epochs inside the head state's randao window.

**Best measured result.** reconstruction usually upwards of 20s, sometimes minutes

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/beacon/states.rs:640-687`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L640-L687)
- [`beacon_node/http_api/src/caches.rs:22-44`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/caches.rs#L22-L44)
- [`beacon_node/http_api/src/attester_duties.rs:83-126`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L83-L126)

**Skeptic check.** The committees endpoint does what PR #3272 describes, so the earlier evidence is right for that endpoint. The historic attester duties endpoint still replays a state.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lighthouse#3272](https://github.com/sigp/lighthouse/pull/3272)

</details>


<a id="beacon_api-L011"></a>
<details>
<summary><b>beacon_api-L011</b> pubkey cache lookup — <i>partial · low · S · cpu, latency</i></summary>

**Idea.** Look up validators by pubkey through the state's pubkey-to-index cache instead of scanning the whole validator registry per query.

**Gap in Lighthouse.** The single-validator path uses chain.validator_index. The bulk paths (get_beacon_state_validators, get_beacon_state_validator_balances, get_beacon_state_validator_identities) still iterate the whole registry (about 2M entries) for each request, and do two HashSet lookups per validator, even when only a few pubkeys/indices are requested. Resolving the ids through chain.validator_index and then indexing the state directly would make this O(m). External VCs (Teku, Vouch, Nimbus) use POST states/head/validators with id lists, so they take this path. sync_committee_rewards also calls state.get_validator_index for every reward times every id.

**Impact.** Small-id bulk validator queries would drop from a full registry scan (about 100ms or more) to microseconds.

**Best measured result.** queries by pubkey took 10ms+ from registry loop

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/validator/mod.rs:48-64`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L48-L64)
- [`beacon_node/http_api/src/beacon/states.rs:780`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L780)
- [`beacon_node/http_api/src/validators.rs:24-47`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validators.rs#L24-L47)
- [`beacon_node/http_api/src/validators.rs:100-116`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validators.rs#L100-L116)
- [`beacon_node/http_api/src/sync_committee_rewards.rs:35`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/sync_committee_rewards.rs#L35)

**Skeptic check.** The single lookup is implemented as described (it uses the global pubkey cache). The earlier evidence wrongly counted the bulk hash-filter path as a cache lookup: that path still scans the whole registry.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lighthouse#3559](https://github.com/sigp/lighthouse/pull/3559)

</details>


<a id="beacon_api-L012"></a>
<details>
<summary><b>beacon_api-L012</b> server-side status counting — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Provide an endpoint that counts validators by status in one pass server-side instead of returning the full validator set for the client to count.

**Impact.** One server-side pass returns the counts instead of the full validator set.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/ui.rs:23-73`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/ui.rs#L23-L73) get_validator_count does one pass over head state validators and counts by ValidatorStatus
- [`beacon_node/http_api/src/lib.rs:3068-3078`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L3068-L3078) GET lighthouse/ui/validator_count route

**Skeptic check.** Verified that the function and the route exist. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#3756](https://github.com/sigp/lighthouse/pull/3756)

</details>


<a id="beacon_api-L013"></a>
<details>
<summary><b>beacon_api-L013</b> single-pass accept parse — <i>implemented · low · S · cpu</i></summary>

**Idea.** Parse the HTTP Accept header in a single pass choosing the highest q-factor supported media type without sorting.

**Impact.** Accept parsing is a single pass. The gain is negligible.

**Evidence (Lighthouse @ 928b61e719).**

- [`common/eth2/src/types.rs:1721-1770`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2/src/types.rs#L1721-L1770) Accept::from_str keeps the highest q in one for_each pass, no sort
- [`beacon_node/http_api/src/aggregate_attestation.rs:18`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/aggregate_attestation.rs#L18) and validator/execution_payload_envelopes.rs:35 server parses Accept through this FromStr (warp::header::optional::&lt;Accept&gt;)

**Skeptic check.** Read the parser: it does a single pass with a running max and no sort, and the server handlers use it. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#4216](https://github.com/sigp/lighthouse/pull/4216)

</details>


<a id="beacon_api-L014"></a>
<details>
<summary><b>beacon_api-L014</b> head root priority and skip block load — <i>implemented · low · S · latency, disk</i></summary>

**Idea.** Raise the beacon-processor priority of head block root API requests used for sync committee messages, and avoid loading the blinded block unless block_id is a block root.

**Impact.** Head-root requests for sync committee messages jump the API queue and never load a block. The early-attester-cache path even answers before import completes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs:1244-1249`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L1244-L1249) BlockId::Head gets Priority::P0, others P1
- [`beacon_node/http_api/src/lib.rs:1250-1272`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L1250-L1272) head fast path from early_attester_cache, else block_id.root
- [`beacon_node/http_api/src/block_id.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs) root(): Head/Genesis/Finalized/Justified/Slot return without loading a block, and only the Root variant calls get_blinded_block

**Skeptic check.** Verified the priority split, and that BlockId::root loads the blinded block only for explicit roots (to compute finalized). The current code goes further than PR #4799 with the early-attester-cache fast path.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#4799](https://github.com/sigp/lighthouse/pull/4799)

</details>


<a id="beacon_api-L015"></a>
<details>
<summary><b>beacon_api-L015</b> single network channel send — <i>partial · low · S · latency, cpu</i></summary>

**Idea.** When publishing a block from the HTTP API, send the block and its blobs to the network service in a single channel message instead of several sends, to reduce overhead.

**Gap in Lighthouse.** Blobs no longer exist (Fulu data columns); block and columns go in separate channel messages, columns batched. Merging the block into the column message would be possible but block is intentionally sent first.

**Impact.** Saves one unbounded channel send per block proposal; negligible.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/publish_blocks.rs:184`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L184) block published via one NetworkMessage::Publish
- [`beacon_node/http_api/src/publish_blocks.rs:520`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L520) columns sent in one publish_pubsub_messages call plus one PublishPartialColumns
- [`beacon_node/http_api/src/utils.rs:73`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/utils.rs#L73) publish_pubsub_messages batches

**Sources.** [lighthouse#4863](https://github.com/sigp/lighthouse/pull/4863)

</details>


<a id="beacon_api-L016"></a>
<details>
<summary><b>beacon_api-L016</b> hashset id filter — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Filter validators by requested ids/pubkeys using a HashSet lookup per state validator instead of scanning the input list per validator, turning O(n*m) into O(n).

**Impact.** The filter is O(n) with O(1) set lookups on all three bulk endpoints.

**Best measured result.** 2s to 12+s with 8k IDs before (slowdown); fix removes it

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/validators.rs:24-27`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validators.rs#L24-L27)
- [`beacon_node/http_api/src/validators.rs:39-46`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validators.rs#L39-L46)
- [`beacon_node/http_api/src/validators.rs:95-116`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validators.rs#L95-L116)
- [`beacon_node/http_api/src/validators.rs:143-160`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validators.rs#L143-L160)

**Skeptic check.** Verified: the HashSet filter from PR #5468 is used by the validators, balances and identities endpoints. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#5468](https://github.com/sigp/lighthouse/pull/5468)

</details>


<a id="beacon_api-L017"></a>
<details>
<summary><b>beacon_api-L017</b> persist light client bootstrap — <i>implemented · medium · S · cpu, disk</i></summary>

**Idea.** Persist light client bootstrap parts (sync committee branch by block root, sync committee by period) so bootstrap is served without expensive computation or state queries.

**Impact.** Bootstrap is built from the blinded block plus the persisted branch and committee, with no state load, on both the RPC and HTTP paths.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/light_client_server_cache.rs:396-444`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_server_cache.rs#L396-L444)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:8374-8389`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L8374-L8389)
- [`beacon_node/store/src/hot_cold_store.rs:770-802`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L770-L802)
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:990`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L990)
- [`beacon_node/http_api/src/light_client.rs:71`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/light_client.rs#L71)

**Skeptic check.** Verified on both the RPC and HTTP paths. No backfill exists for periods before the node synced, but that limits coverage and does not affect performance. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#5915](https://github.com/sigp/lighthouse/pull/5915)

</details>


<a id="beacon_api-L018"></a>
<details>
<summary><b>beacon_api-L018</b> single lock acquisition — <i>implemented · low · S · latency</i></summary>

**Idea.** Read all needed fields from the canonical head under one lock acquisition instead of locking twice, to cut lock contention in the syncing endpoint.

**Impact.** None left; /node/syncing already reads the head once.

**Best measured result.** "responses were taking 4-10s on occasion"

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:589-598`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L589-L598) head_and_execution_status reads cached_head once, then one fork choice read lock
- [`beacon_node/http_api/src/lib.rs:2452-2455`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L2452-L2455) /node/syncing takes head slot and optimistic status from that single call

**Skeptic check.** Verified that /node/syncing gets head slot and execution status from one head_and_execution_status call, which is the #6202 change itself. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#6202](https://github.com/sigp/lighthouse/pull/6202)

</details>


<a id="beacon_api-L019"></a>
<details>
<summary><b>beacon_api-L019</b> raise API request priority — <i>implemented · low · S · latency</i></summary>

**Idea.** Raise the beacon-processor priority of validator-info HTTP requests so they are not starved and time out under load.

**Impact.** Head-state validator requests (GET/POST validators, single validator, validator_identities) run at P0, which is the exact change of PR 6292.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/beacon/states.rs:769`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L769)
- [`beacon_node/http_api/src/beacon/states.rs:850`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L850)
- [`beacon_node/http_api/src/beacon/states.rs:911`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L911)
- [`beacon_node/http_api/src/beacon/states.rs:948`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L948)

**Skeptic check.** The PR's three P1-&gt;P0 switches for state_id=head are present (moved from lib.rs to beacon/states.rs), and identities also has the switch. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#6292](https://github.com/sigp/lighthouse/pull/6292)

</details>


<a id="beacon_api-L020"></a>
<details>
<summary><b>beacon_api-L020</b> server-side supply computation — <i>not · low · S · bandwidth, cpu</i></summary>

**Idea.** Add a node-side endpoint that sums balances for a state, so clients do not download and parse 68MB of JSON validator balances.

**Gap in Lighthouse.** Add a non-standard route (e.g. GET /lighthouse/.../supply or beacon/states/{id}/total_balance) that sums state.balances() inside map_state_and_execution_optimistic_and_finalized and returns one number; also add it to eth2 client types.

**Impact.** Saves a ~68MB JSON download+parse per supply query for tooling/explorers; negligible for a validating node, only benefits API consumers.

**Best measured result.** avoids 68MB JSON download

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs), validators.rs, beacon/states.rs: grep for supply/total balance finds only validator_balances (returns full list)
- no supply endpoint in http_api/src

**Sources.** [lighthouse#7102](https://github.com/sigp/lighthouse/pull/7102)

</details>


<a id="beacon_api-L021"></a>
<details>
<summary><b>beacon_api-L021</b> not-while-syncing guard on duties — <i>implemented · medium · S · cpu, sync</i></summary>

**Idea.** Reject validator duty endpoints (e.g. proposer duties) while the node is far behind head, since computing duties requires advancing state over many slots and starves sync.

**Impact.** Proposer, attester and sync duties are rejected while the node is far behind, so state advances do not starve sync.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs:475-512`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L475-L512) not_while_syncing_filter rejects in SyncingFinalized/SyncingHead when head_slot + sync_tolerance_epochs*slots &lt; current_slot
- [`beacon_node/http_api/src/validator/mod.rs:1403`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L1403) get_validator_duties_proposer uses not_while_syncing_filter
- [`beacon_node/http_api/src/validator/mod.rs:161`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L161) post_validator_duties_attester uses it
- [`beacon_node/http_api/src/validator/mod.rs:125`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L125) post_validator_duties_sync uses it

**Skeptic check.** Verified that the filter is on the proposer, attester, sync and PTC duty routes and on block production. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#7962](https://github.com/sigp/lighthouse/pull/7962)

</details>


<a id="beacon_api-L022"></a>
<details>
<summary><b>beacon_api-L022</b> head root fast path — <i>implemented · low · S · latency</i></summary>

**Idea.** Serve the head block root endpoint from the early attester cache when it is at least as recent as the cached head, avoiding waiting for the import to finish.

**Impact.** Head block root is served from early_attester_cache before import completes, at P0.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs:1245`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L1245)
- [`beacon_node/http_api/src/lib.rs:1259`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L1259)

**Skeptic check.** get_beacon_block_root uses early_attester_cache.get_head_block_root when its slot &gt;= cached head slot, which is PR 8729. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#8729](https://github.com/sigp/lighthouse/pull/8729)

</details>


<a id="beacon_api-L023"></a>
<details>
<summary><b>beacon_api-L023</b> skip duties when stalled — <i>not · medium · S · cpu, latency</i></summary>

**Idea.** Skip proposer duty computation (expensive state advance) while sync is stalled, not only while syncing, to avoid overwhelming the work queue.

**Gap in Lighthouse.** Stalled state passes the filter, and the proposer duties handler has no own head-lag guard, so a far-behind stalled node still computes duties via state advance. Apply the head-slot-vs-tolerance check to the Stalled arm.

**Impact.** Avoids expensive state advances and api_request_p0 work-queue overflow on a stalled far-behind node; no steady-state effect.

**Best measured result.** avoids 'Work queue is full' api_request_p0 at 1024

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs:509`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L509) SyncState::Stalled =&gt; Ok(()) in not_while_syncing_filter
- [`beacon_node/http_api/src/lib.rs:2703-2706`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L2703-L2706) proposer duties route uses not_while_syncing_filter
- [`beacon_node/http_api/src/proposer_duties.rs:80-90`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/proposer_duties.rs#L80-L90) cache miss calls compute_and_cache_proposer_duties with no head-distance check
- [`beacon_node/network/src/sync/manager.rs:673`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L673) Stalled set when no advanced/synced peers

**Second check.** Also checked the proposer_duties handler itself for a head-distance or skip guard; none exists, so the earlier verdict stands.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [lighthouse#9538](https://github.com/sigp/lighthouse/pull/9538)

</details>


<a id="beacon_api-L024"></a>
<details>
<summary><b>beacon_api-L024</b> index lookup instead of full scan — <i>not · medium · S · cpu, latency</i></summary>

**Idea.** For validator/balance state endpoints with a requested validator set, resolve the ids to indices first and read those validators directly instead of scanning the whole registry and filtering.

**Gap in Lighthouse.** All three list endpoints scan the whole registry even for a few ids. Resolve ids to indices (index directly, pubkey via validator_pubkey_cache / state pubkey cache) and read validators().get(i)/balances().get(i); scan only when no ids (or status-only filter).

**Impact.** Subset requests drop from a full registry scan (~260 ms) to a few ms (6 ms for 100 vals per the PR).

**Best measured result.** validator_balances 100 vals: 260 ms to 6 ms; 10k: 260 to 23 ms; 100k: 320 to 110 ms

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/validators.rs:86-125`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validators.rs#L86-L125) balances endpoint scans validators().iter().zip(balances()) and filters by HashSet
- [`beacon_node/http_api/src/validators.rs:134-170`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validators.rs#L134-L170) identities endpoint does the same full scan
- [`beacon_node/http_api/src/validators.rs:9-75`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validators.rs#L9-L75) get_beacon_state_validators also full-scans with id filter

**Second check.** Read all of validators.rs including get_beacon_state_validators (not cited earlier): it uses the same full scan, so the verdict stands and the gap covers three endpoints.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [lighthouse#10037](https://github.com/sigp/lighthouse/pull/10037)

</details>


<a id="beacon_api-L025"></a>
<details>
<summary><b>beacon_api-L025</b> light client updates without state cache — <i>implemented · medium · S · memory</i></summary>

**Idea.** Generate light client updates only from the post-state at block import, kept as small proofs, without needing historical states in the state cache.

**Impact.** Updates come from proofs taken at import; a state load happens only on a cache miss.

**Best measured result.** No numbers

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:4787-4795`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4787-L4795) cache_state_data on the import post-state
- [`beacon_node/beacon_chain/src/light_client_server_cache.rs:59-77`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_server_cache.rs#L59-L77) LightClientCachedData::from_state stores branches in the prev_block_cache LRU
- [`beacon_node/beacon_chain/src/light_client_server_cache.rs:80-210`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_server_cache.rs#L80-L210) recompute_and_cache_updates uses only blocks and cached proofs
- [`beacon_node/beacon_chain/src/light_client_server_cache.rs:271-291`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_server_cache.rs#L271-L291) get_or_compute_prev_block_cache loads a state only on an LRU miss
- [`beacon_node/beacon_chain/src/light_client_server_cache.rs:396-440`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_server_cache.rs#L396-L440) bootstrap is served from stored sync committee branch, not state

**Skeptic check.** Verified that proofs are taken from the post-state at import and that updates and bootstrap are built from blocks plus the stored branches. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#3461](https://github.com/ChainSafe/lodestar/pull/3461)

</details>


<a id="beacon_api-L026"></a>
<details>
<summary><b>beacon_api-L026</b> zero-copy response body — <i>n/a · low · memory, cpu</i></summary>

**Idea.** Return a typed-array response body without copying its backing buffer; the HTTP server converts it to a Buffer as a view. This avoids copying large SSZ responses.

**Impact.** n/a: JS typed array copy semantics, no equivalent in Rust.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs:2148`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L2148) debug state handler returns Vec&lt;u8&gt; body directly

**Sources.** [lodestar#6626](https://github.com/ChainSafe/lodestar/pull/6626)

</details>


<a id="beacon_api-L027"></a>
<details>
<summary><b>beacon_api-L027</b> zero-copy state response — <i>n/a · low · memory, cpu</i></summary>

**Idea.** Convert the serialized state to a Buffer as a view over the same memory rather than copying it, when serving state as SSZ. This cuts memory growth and GC per state request.

**Impact.** n/a: JS Buffer.from copy has no Rust analogue; SSZ is encoded once into a Vec.

**Best measured result.** Buffer.from copy 137ms vs no copy 895ns

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs:2148`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L2148) get_debug_beacon_states

**Sources.** [lodestar#6687](https://github.com/ChainSafe/lodestar/pull/6687)

</details>


<a id="beacon_api-L028"></a>
<details>
<summary><b>beacon_api-L028</b> ssz http wire format — <i>partial · low · M · bandwidth, cpu</i></summary>

**Idea.** Prefer SSZ over JSON as the response wire format for validator-to-beacon-node HTTP APIs (and request format where supported), avoiding JSON encode/decode cost and payload size.

**Gap in Lighthouse.** Block production/publication and validator_identities already use SSZ; attester/proposer/sync duties, attestation data and aggregate submission still use JSON in the VC. Extending SSZ to those needs spec endpoints that support it.

**Impact.** Marginal CPU/bandwidth saving on VC&lt;-&gt;BN traffic; matters mostly for large validator sets.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/block_service.rs:714`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/block_service.rs#L714) post_validator_blocks_v4_ssz
- [`common/eth2/src/lib.rs:840`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2/src/lib.rs#L840) post_beacon_states_validator_identities_ssz
- [`common/eth2/src/types.rs:1714`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2/src/types.rs#L1714) Accept::Ssz

**Sources.** [lodestar#6840](https://github.com/ChainSafe/lodestar/pull/6840)

</details>


<a id="beacon_api-L029"></a>
<details>
<summary><b>beacon_api-L029</b> upgrade HTTP server — <i>n/a · low · cpu</i></summary>

**Idea.** Upgrade the HTTP server framework to a version that removed deprecated code paths for lower per-request overhead.

**Impact.** n/a: Node HTTP framework upgrade specific to Lodestar.

**Best measured result.** promises 5-10% performance increase

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.lock warp/axum HTTP stack

**Sources.** [lodestar#7101](https://github.com/ChainSafe/lodestar/pull/7101)

</details>


<a id="beacon_api-L030"></a>
<details>
<summary><b>beacon_api-L030</b> lightweight validator endpoint — <i>implemented · low · S · cpu, bandwidth</i></summary>

**Idea.** Offer a lightweight validator identities endpoint returning only pubkey and index, with SSZ encoding, instead of full validator objects, so clients that need only indices pull less data.

**Impact.** POST validator_identities returns only index, pubkey and activation_epoch, with SSZ when Accept is SSZ.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/validators.rs:134`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validators.rs#L134)
- [`beacon_node/http_api/src/beacon/states.rs:931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L931)
- [`beacon_node/http_api/src/beacon/states.rs:960`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L960)
- [`common/eth2/src/lib.rs:840`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2/src/lib.rs#L840)

**Skeptic check.** I confirmed the handler and its SSZ branch (as_ssz_bytes) and the eth2 client SSZ variant. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#7107](https://github.com/ChainSafe/lodestar/pull/7107), [prysm#15086](https://github.com/OffchainLabs/prysm/pull/15086)

</details>


<a id="beacon_api-L031"></a>
<details>
<summary><b>beacon_api-L031</b> serve checkpoint state API — <i>implemented · low · S · sync</i></summary>

**Idea.** Serve persisted safe checkpoint states over an API so new nodes can bootstrap quickly from peers.

**Impact.** Finalized, justified and any hot/cold state by root are served as SSZ through debug/beacon/states/{state_id}, which covers the non-finality rescue case.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/state_id.rs:41`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L41)
- [`beacon_node/http_api/src/state_id.rs:48`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L48)
- [`beacon_node/http_api/src/state_id.rs:68`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L68)
- [`beacon_node/http_api/src/lib.rs:2148`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L2148)

**Skeptic check.** Lodestar needed a new endpoint because its persisted checkpoint states were not reachable through the standard API. Lighthouse resolves Justified and arbitrary hot state roots from its store, so a safe non-finalized state is already servable. The earlier note said only finalized is served; that part was wrong, but the verdict holds.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#7541](https://github.com/ChainSafe/lodestar/pull/7541)

</details>


<a id="beacon_api-L032"></a>
<details>
<summary><b>beacon_api-L032</b> range read instead of full load — <i>not · low · S · cpu, memory</i></summary>

**Idea.** Compute pending balance to withdraw by reading a range of pending partial withdrawals rather than loading the entire list; consider a pending-balance cache.

**Gap in Lighthouse.** get_pending_balance_to_withdraw does a full O(n) scan of the ProgressiveList per call; a per-validator cache or index would avoid it. The list is usually small, so gain is minor.

**Impact.** Per-exit/withdrawal-request/consolidation scan of pending list; negligible on mainnet today unless the list grows large.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:3232`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3232) get_pending_balance_to_withdraw iterates all pending_partial_withdrawals with filter
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:840`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L840),1171 callers; verify_exit.rs:84

**Sources.** [lodestar#7598](https://github.com/ChainSafe/lodestar/pull/7598), [prysm#4262](https://github.com/OffchainLabs/prysm/pull/4262)

</details>


<a id="beacon_api-L033"></a>
<details>
<summary><b>beacon_api-L033</b> skip preprocessing without listeners — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Only guard event emission with listener-count checks where preprocessing is costly (hex mapping, async payload attribute building), skipping that work when no SSE subscribers exist.

**Impact.** Expensive SSE preprocessing (blob/data column sidecar conversion, payload attribute building) is skipped when there are no subscribers.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/events.rs:325`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/events.rs#L325)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3653`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3653)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3677`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3677)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7073`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7073)

**Skeptic check.** The blob sidecar, data column sidecar and payload attributes emit sites are the only register calls for those kinds, and each one is guarded by a has_*_subscribers check. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#8293](https://github.com/ChainSafe/lodestar/pull/8293)

</details>


<a id="beacon_api-L034"></a>
<details>
<summary><b>beacon_api-L034</b> skip stale light client updates — <i>partial · low · S · cpu, bandwidth</i></summary>

**Idea.** Do not emit light client updates that are stale relative to what was already emitted.

**Gap in Lighthouse.** Per-period best-update storage skips worse updates, but the finality/optimistic update gossip/SSE path was not shown to be gated on staleness; check the emit functions.

**Impact.** Marginal; light client serving is rare on mainnet nodes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/light_client_server_cache.rs:192-205`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_server_cache.rs#L192-L205) compares with is_better_light_client_update before persisting/caching

**Sources.** [lodestar#8522](https://github.com/ChainSafe/lodestar/pull/8522)

</details>


<a id="beacon_api-L035"></a>
<details>
<summary><b>beacon_api-L035</b> skip redundant DB lookup — <i>implemented · low · S · disk, latency</i></summary>

**Idea.** Skip the DB block fetch, deserialize and hashTreeRoot for the genesis block root when the state already provides it.

**Impact.** None to gain: the genesis block root is a BeaconChain field and is never read from the DB on request paths.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/block_id.rs:59`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L59)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:488`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L488)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1052`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1052)

**Skeptic check.** BlockId::Genesis and the block_root_at_slot genesis case both return the in-memory genesis_block_root. The source Lodestar PR was closed without merge. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#9082](https://github.com/ChainSafe/lodestar/pull/9082)

</details>


<a id="beacon_api-L036"></a>
<details>
<summary><b>beacon_api-L036</b> skip redundant DB lookup — <i>implemented · low · S · disk, latency</i></summary>

**Idea.** Skip the DB block fetch, deserialize and hashTreeRoot for the genesis block root when the state already provides it.

**Impact.** None to gain: the genesis block root is held in memory.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/block_id.rs:59`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L59)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:488`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L488)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1052`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1052)

**Skeptic check.** This is a duplicate of L035 (Lodestar 9083, closed). Lighthouse has no DB fetch for the genesis root. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#9083](https://github.com/ChainSafe/lodestar/pull/9083)

</details>


<a id="beacon_api-L037"></a>
<details>
<summary><b>beacon_api-L037</b> skip redundant DB lookup — <i>implemented · low · S · disk, latency</i></summary>

**Idea.** Skip the DB block fetch, deserialize and hashTreeRoot for the genesis block root when the state already provides it.

**Impact.** None to gain: the genesis block root is held in memory.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/block_id.rs:59`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L59)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:488`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L488)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1123`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1123)

**Skeptic check.** This is a duplicate of L035 (Lodestar 9084, closed). Lighthouse has no DB fetch for the genesis root. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#9084](https://github.com/ChainSafe/lodestar/pull/9084)

</details>


<a id="beacon_api-L038"></a>
<details>
<summary><b>beacon_api-L038</b> guard old-slot reconstruction — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** In blob REST endpoints, return 404 immediately for post-Fulu slots older than the data-column availability window instead of entering the expensive column reconstruction path.

**Impact.** Pruned (out-of-window) slots exit before reconstruction. An explicit window check would save one empty prefix scan and change 400 to 404.

**Best measured result.** ~407 getBlobs requests caused p99 event-loop lag spike to 18.1s

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/block_id.rs:501-520`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L501-L520) get_data_columns_for_blob_reconstruction counts stored column keys and returns 400 if fewer than NUMBER_OF_COLUMNS/2, before any column load or KZG recovery
- [`beacon_node/http_api/src/block_id.rs:365-368`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L365-L368) blob_sidecars reconstructs only after that check
- [`beacon_node/http_api/src/block_id.rs:434-437`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L434-L437) blobs-by-versioned-hashes uses the same guard
- [`beacon_node/store/src/hot_cold_store.rs:2657-2666`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2657-L2666) get_data_column_keys is a prefix scan that ends at once when columns are pruned

**Skeptic check.** Verified that both blob endpoints go through the key-count guard, and that pruned slots have no column keys, so they exit before reconstruction. The effect matches Lodestar's 404 guard. Only the status code differs.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#9536](https://github.com/ChainSafe/lodestar/pull/9536)

</details>


<a id="beacon_api-L039"></a>
<details>
<summary><b>beacon_api-L039</b> guard old-slot reconstruction — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** In blob REST endpoints, compute the data-column availability start as max(earliest available slot, retention floor) and return 404 early for older slots rather than attempting column reconstruction.

**Impact.** Same as L038: out-of-window slots never reach reconstruction. Only the max(earliest, retention floor) 404 is absent, and it is cosmetic.

**Best measured result.** ~407 getBlobs requests caused p99 event-loop lag spike to 18.1s

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/block_id.rs:501-520`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L501-L520) key-count guard before reconstruction
- [`beacon_node/http_api/src/block_id.rs:365-368`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L365-L368) blob_sidecars path
- [`beacon_node/http_api/src/block_id.rs:434-437`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L434-L437) blobs-by-versioned-hashes path
- [`beacon_node/store/src/hot_cold_store.rs:2657-2666`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2657-L2666) get_data_column_keys prefix scan

**Skeptic check.** This is a duplicate of L038 (Lodestar follow-up #9537). The guard decides on data that is actually present, not on a computed window, so slots older than the window exit early. Upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#9537](https://github.com/ChainSafe/lodestar/pull/9537)

</details>


<a id="beacon_api-L040"></a>
<details>
<summary><b>beacon_api-L040</b> refuse regen API while syncing — <i>not · medium · S · cpu, latency, sync</i></summary>

**Idea.** Reject REST requests for arbitrary-slot or root states with 503 while the node is syncing (keep head/finalized/justified/genesis served), so expensive regen is never triggered from the API while behind.

**Gap in Lighthouse.** Add a sync check in StateId::state (or on the beacon/states and debug/beacon/states routes) for CoreStateId::Slot and Root, returning 503 not_synced as not_while_syncing_filter does; keep Head/Finalized/Justified/Genesis served.

**Impact.** Stops arbitrary-slot state loads (cold hdiff replay, hot cache churn) from competing with sync on a lagging node; matters only when tools hit the API during sync. The beacon processor already runs P1 API work below range-sync chain segments, so the gain is smaller than in Lodestar.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/state_id.rs:174`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L174) StateId::state calls chain.get_state(root, slot, true) with no sync check
- [`beacon_node/http_api/src/lib.rs:2148`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L2148) GET debug/beacon/states/{state_id} has no not_while_syncing_filter
- [`beacon_node/http_api/src/beacon/states.rs:46`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L46) beacon/states/* routes spawn Priority::P1 tasks with no sync gate
- [`beacon_node/beacon_processor/src/lib.rs:1149`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1149) P1 API requests are popped only after chain segments and gossip work (scheduling mitigation, not rejection)

**Verdict history.** not (checked) → not (refuted)

**Sources.** [lodestar#9641](https://github.com/ChainSafe/lodestar/pull/9641)

</details>


<a id="beacon_api-L041"></a>
<details>
<summary><b>beacon_api-L041</b> set instead of array scan — <i>n/a · low · S · cpu</i></summary>

**Idea.** Look up requested validator indices in a hash set rather than Array.includes when filtering attestation rewards, removing O(ids x validators) cost.

**Gap in Lighthouse.** Lighthouse already converts ids to indices once and uses subset deltas; no O(ids x validators) Array.includes pattern exists (the validators endpoint uses HashSet). Idea does not apply as stated.

**Impact.** None meaningful.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_rewards.rs:360`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_rewards.rs#L360) validators_ids_to_indices
- [`beacon_node/beacon_chain/src/attestation_rewards.rs:213-216`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_rewards.rs#L213-L216)

**Sources.** [lodestar#10184](https://github.com/ChainSafe/lodestar/pull/10184)

</details>


<a id="beacon_api-L042"></a>
<details>
<summary><b>beacon_api-L042</b> pubkey index map — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Resolve pubkeys to indices with a map built once per request instead of scanning the registry per requested pubkey.

**Impact.** The builders endpoint (the Lodestar #10408 target) costs O(builders), not O(ids*builders).

**Best measured result.** 400 ids vs 24k builders: ~6.3s to ~66ms

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/builders.rs:24-41`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/builders.rs#L24-L41) get_beacon_state_builders puts requested ids in a HashSet once and scans builders once
- [`beacon_node/http_api/src/validators.rs:24-45`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validators.rs#L24-L45) same single-pass HashSet filter for validators
- [`beacon_node/http_api/src/validator/mod.rs:48-64`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L48-L64) pubkey_to_validator_index uses validator_pubkey_cache

**Skeptic check.** The source PR is about POST /states/{id}/builders. The earlier evidence cited the validators endpoint; the builders endpoint at builders.rs also builds the HashSet once, so the verdict holds. Outside the API, process_builder_deposit_request and process_builder_exit_request (process_operations.rs:934,991) still do a linear pubkey scan per request. That is a separate block-processing idea.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#10408](https://github.com/ChainSafe/lodestar/pull/10408)

</details>


<a id="beacon_api-L043"></a>
<details>
<summary><b>beacon_api-L043</b> share historical state reconstruction — <i>partial · low · M · cpu, latency</i></summary>

**Idea.** Cache the serialized response of the last requested historical state and share in-flight reconstruction between concurrent readers, so multiple field reads of the same archived state reconstruct it once.

**Gap in Lighthouse.** A decoded-state cache exists so sequential reads reuse the state, but there is no in-flight dedup: concurrent cold requests for the same slot both miss and reconstruct (lock dropped before work). Add a per-slot single-flight map (Arc&lt;OnceCell&gt;/watch) in load_cold_state_by_slot.

**Impact.** Concurrent archive-state API queries (explorers, tooling) would reconstruct once instead of N times; reduces multi-second CPU/memory spikes on archive nodes, up to ~2.5x on cold triple reads.

**Best measured result.** cold read 5.93s with 3 reconstructions vs 2.18-2.33s with one

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2310-2319`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2310-L2319) historic_state_cache lock, released before reconstruction
- hot_cold_store.rs:2344,2375,2401 results put in historic_state_cache
- hot_cold_store.rs:87 Mutex&lt;HistoricStateCache&gt; caches states, not serialized responses

**Sources.** [lodestar#10458](https://github.com/ChainSafe/lodestar/pull/10458)

</details>


<a id="beacon_api-L044"></a>
<details>
<summary><b>beacon_api-L044</b> pubkey-to-index cache — <i>partial · low · S · cpu, latency</i></summary>

**Idea.** Keep a validator pubkey to index map in memory and use it for validator API lookups, instead of scanning the validator registry of a state for each requested key.

**Gap in Lighthouse.** /validators with pubkey ids iterates the whole registry (HashSet membership per validator) instead of resolving ids via the chain's pubkey cache and indexing directly; use validator_index(pubkey) and state.validators().get(i) when ids are given and no status filter.

**Impact.** Cheaper validator-by-id queries (O(ids) instead of ~1M validator scan, a few ms to tens of ms per call); matters for VC/monitoring polling.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/validators.rs:41-44`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validators.rs#L41-L44) ids_filter_set HashSet but still scans every validator in the state
- [`beacon_node/beacon_chain/src/beacon_chain.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs) validator_pubkey_cache exists for other paths

**Sources.** [nimbus#2987](https://github.com/status-im/nimbus-eth2/pull/2987)

</details>


<a id="beacon_api-L045"></a>
<details>
<summary><b>beacon_api-L045</b> reuse state across history traversal — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** For historical state queries, reuse already replayed state across consecutive slot requests instead of replaying from a checkpoint each time.

**Impact.** Consecutive historical slot queries replay only from the last cached state.

**Best measured result.** getStateRoot 72.7 s -&gt; 6.7 s (up to 10x)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2306-2328`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2306-L2328) load_cold_state_by_slot searches HistoricStateCache back through replay_from_range for the nearest prior state
- [`beacon_node/store/src/hot_cold_store.rs:2358-2401`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2358-L2401) load_cold_state_by_slot_using_replay replays from it and put_state's the result
- [`beacon_node/store/src/historic_state_cache.rs:14`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/historic_state_cache.rs#L14) HistoricStateCache holds states and hdiff buffers

**Skeptic check.** Verified that load_cold_state_by_slot reuses the nearest cached prior state and caches the replay result, which is the Nimbus mechanism. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#3219](https://github.com/status-im/nimbus-eth2/pull/3219)

</details>


<a id="beacon_api-L046"></a>
<details>
<summary><b>beacon_api-L046</b> stream JSON without temp strings — <i>partial · low · M · cpu, memory, latency</i></summary>

**Idea.** Stream JSON directly to the output instead of allocating temporary strings for hex arrays and numbers, which matters for huge state responses.

**Gap in Lighthouse.** Hash/root types already format on the stack. Quoted u64 (balances, slots, indices) uses format! per value and byte vectors build Strings. Replace with itoa::Buffer in quoted_int serialize (ethereum_serde_utils) and write hex via a stack/ chunked buffer; optionally stream large states.

**Impact.** JSON state/validators/balances responses (millions of integers) would allocate far fewer small Strings; maybe 20-40% off serialization CPU on huge responses, no change for SSZ clients.

**Best measured result.** 2-3x faster on state endpoint, 6-7s down to 2-3s

**Evidence (Lighthouse @ 928b61e719).**

- ethereum_serde_utils-0.8.1/src/quoted_int.rs:92 serialize_str(&amp;format!("{}", v)) allocates a String per u64
- ssz_types-0.14.1/src/serde_utils/hex_fixed_vec.rs:11 hex String temporaries
- alloy-primitives-1.7.3/src/bits/serde.rs:11-12 hashes use stack hex::Buffer (no heap)
- [`beacon_node/http_api/src/task_spawner.rs:102`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/task_spawner.rs#L102) warp::reply::json builds whole Vec in memory

**Sources.** [nimbus#7385](https://github.com/status-im/nimbus-eth2/pull/7385)

</details>


<a id="beacon_api-L047"></a>
<details>
<summary><b>beacon_api-L047</b> recent state root from RAM — <i>implemented · low · S · disk, latency</i></summary>

**Idea.** Serve state_root lookups for recent states (last 8192 slots) from the in-memory head state's state_roots vector instead of requiring a DB index of historical state roots.

**Impact.** Recent state roots (within SLOTS_PER_HISTORICAL_ROOT of head) come from the in-memory head state's state_roots; no DB index needed.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:964-998`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L964-L998) state_root_at_slot: genesis, split-slot and head-state state_roots fast paths before any DB lookup
- [`beacon_node/http_api/src/state_id.rs:55-67`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L55-L67),128 StateId::Slot resolves via chain.state_root_at_slot

**Skeptic check.** Verified head.beacon_state.get_state_root(request_slot) fast path, used by the API StateId::Slot resolution. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#8819](https://github.com/status-im/nimbus-eth2/pull/8819)

</details>


<a id="beacon_api-L048"></a>
<details>
<summary><b>beacon_api-L048</b> head event on reorg — <i>partial · low · S · latency</i></summary>

**Idea.** Emit the SSE head event also when the new head is a reorg, so subscribed VCs detect reorgs sooner.

**Gap in Lighthouse.** The Head (and HeadV2) event is emitted from BeaconChain::import_block only when the newly imported block becomes head (and only for blocks within EARLY_ATTESTER_CACHE_HISTORIC_SLOTS). A head change found by recompute_head_at_slot/after_new_head without a new import (reorg to an existing block from attestation weight, proposer boost expiry, re-org of a late block at slot start) emits only chain_reorg, so a VC subscribed only to 'head' does not see it.

**Impact.** VCs subscribed only to head would detect non-import reorgs sooner and refresh duties; correctness/latency of VC reaction, not CPU.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:4554-4633`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4554-L4633) legacy Head SSE event is only registered inside import_block when get_head returns the block just imported
- [`beacon_node/beacon_chain/src/canonical_head.rs:1499-1589`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1499-L1589) after_new_head emits ChainReorg on reorg but no Head event
- [`beacon_node/beacon_chain/src/canonical_head.rs:1207-1258`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1207-L1258) recompute_head only emits HeadV2 for payload-status change of the same block
- [`beacon_node/beacon_chain/src/events.rs:349`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/events.rs#L349) has_head_subscribers only used at beacon_chain.rs:4597

**Skeptic check.** Earlier evidence cited events.rs dispatch, which is not an emission site; the real Head emission is tied to import_block, not to every canonical head change. Reorgs caused by an imported block becoming head are covered, others are not.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [nimbus#8874](https://github.com/status-im/nimbus-eth2/pull/8874)

</details>


<a id="beacon_api-L049"></a>
<details>
<summary><b>beacon_api-L049</b> reuse shuffling for PTC — <i>implemented · low · S · cpu</i></summary>

**Idea.** Compute PTC duties using the already-computed epoch shuffling reference instead of recomputing committees from the head state.

**Impact.** No committee/shuffling recompute for PTC duties. The only residual cost is a per-validator 32-slot scan that allocates a Vec per slot; a per-request slot-&gt;index map would avoid it but that is a different, minor optimization.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:1771-1814`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1771-L1814) compute_ptc_duties reads state only
- [`consensus/types/src/state/beacon_state.rs:3591-3628`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3591-L3628) get_ptc reads the precomputed ptc_window
- [`consensus/types/src/state/beacon_state.rs:3685-3698`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3685-L3698) get_ptc_assignment scans the 32 slot windows

**Skeptic check.** Verified PTC duties come from state.ptc_window, not from recomputed committees. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#9058](https://github.com/status-im/nimbus-eth2/pull/9058)

</details>


<a id="beacon_api-L050"></a>
<details>
<summary><b>beacon_api-L050</b> pubkey to index map — <i>partial · low · S · cpu, latency</i></summary>

**Idea.** Keep a pubkey to validator index map (persisted or in memory) instead of scanning the whole validator registry linearly for each pubkey lookup served via the API.

**Gap in Lighthouse.** Single-validator lookup uses the O(1) pubkey cache, but get_beacon_state_validators/_balances/_identities iterate every validator and test HashSet membership of ValidatorId::PublicKey. Resolve pubkey ids via chain.validator_index and index state.validators() directly when ids are given.

**Impact.** Queries by id on /validators, /validator_balances and /validator_identities (VC and staking-tool polling) would cost O(ids) not O(1.1M validators); saves tens of ms per request.

**Best measured result.** O(n) scan replaced by O(1) lookup

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:26`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L26) pubkey-&gt;index HashMap
- [`beacon_node/http_api/src/validator/mod.rs:48`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L48) pubkey_to_validator_index uses it
- [`beacon_node/http_api/src/validators.rs:43`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validators.rs#L43) list endpoints scan full registry per request

**Sources.** [prysm#1690](https://github.com/OffchainLabs/prysm/pull/1690)

</details>


<a id="beacon_api-L051"></a>
<details>
<summary><b>beacon_api-L051</b> per-slot committee cache for duties — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Cache the committee list per slot so duty/assignment API calls compute it once per slot instead of recomputing for every validator request.

**Impact.** Committees are computed once per shuffling and reused across duty calls.

**Best measured result.** one calculation per slot instead of per RPC call

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/attester_duties.rs:44-48`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L44-L48),60-77 current/next-epoch duties go through chain.validator_attestation_duties
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1747`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1747) validator_attestation_duties uses with_committee_cache (shuffling cache keyed by epoch/decision root)
- [`beacon_node/http_api/src/attester_duties.rs:143`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L143) historic path builds the committee cache once per request
- [`beacon_node/http_api/src/beacon/states.rs:605-690`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L605-L690) committees endpoint uses cached committees

**Skeptic check.** Verified that the hot current/next-epoch duty path uses the shared shuffling cache, not only a per-request build. Earlier evidence cited only the historic per-request path but was right in effect.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#2151](https://github.com/OffchainLabs/prysm/pull/2151)

</details>


<a id="beacon_api-L052"></a>
<details>
<summary><b>beacon_api-L052</b> hoist per-call lookups — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** In the list-assignments RPC, fetch the committee cache and archival epoch data once per call instead of per validator.

**Impact.** Committee cache and pubkeys are fetched once per request on both cached and historic paths.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/attester_duties.rs:63-78`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L63-L78) cached path calls chain.validator_attestation_duties once for all indices (shuffling cache)
- [`beacon_node/http_api/src/attester_duties.rs:141-163`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L141-L163) historic path builds committee cache once, then per-validator lookups
- [`beacon_node/http_api/src/attester_duties.rs:220-223`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L220-L223) pubkeys fetched in one validator_pubkey_bytes_many call

**Skeptic check.** Checked both current/next-epoch and historic duty paths; lookups are hoisted. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#4456](https://github.com/OffchainLabs/prysm/pull/4456)

</details>


<a id="beacon_api-L053"></a>
<details>
<summary><b>beacon_api-L053</b> use committee cache — <i>implemented · low · S · cpu</i></summary>

**Idea.** Use the cached committee lookup in the committees RPC instead of recomputing committees directly.

**Impact.** Committees are served from caches; recompute happens only on a cache miss.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/beacon/states.rs:611-687`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L611-L687) committees endpoint reads HistoricalCommitteeCache, then state.committee_cache if initialized, else builds once and inserts into the LRU
- [`beacon_node/http_api/src/caches.rs:22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/caches.rs#L22) HistoricalCommitteeCache

**Skeptic check.** Verified the committee cache chain. Minor correction: it is the http_api HistoricalCommitteeCache, not the chain shuffling_cache, and the state is still loaded before the cache check, but the idea (use cached committees) holds.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#4464](https://github.com/OffchainLabs/prysm/pull/4464)

</details>


<a id="beacon_api-L054"></a>
<details>
<summary><b>beacon_api-L054</b> single pass committee map — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Iterate committees once and store them in a map for archival assignment lookup instead of per-validator scans.

**Impact.** Committees are computed once per shuffling and validator assignment lookups are map reads, not per-validator committee scans.

**Best measured result.** stated lower response times

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/caches.rs:22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/caches.rs#L22) HistoricalCommitteeCache LRU keyed by HistoricalShufflingId
- [`beacon_node/http_api/src/beacon/states.rs:612`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L612) committees endpoint looks up shuffling id, builds CommitteeCache once and inserts it (676)
- [`beacon_node/http_api/src/attester_duties.rs:165`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L165) compute_historic_attester_duties builds the committee cache once then get_attestation_duties per index (O(1) position lookup)

**Skeptic check.** Verified the committees endpoint caches the CommitteeCache by shuffling id and historic attester duties build it once per request; earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#4480](https://github.com/OffchainLabs/prysm/pull/4480)

</details>


<a id="beacon_api-L055"></a>
<details>
<summary><b>beacon_api-L055</b> skip needless slot advance — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** For attestation-data requests, only advance the head state through empty slots when the requested slot is in a later epoch than the state, since only the epoch-boundary root is needed.

**Impact.** Attestation data production does no slot processing in the common case and only a partial advance (often pre-done by the state advance timer) at an epoch boundary.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2124`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2124) same-epoch path takes justified checkpoint and committee length straight from the head state
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2153`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2153) other epochs use get_advanced_hot_state and partial_state_advance only if state.current_epoch() &lt; request_epoch
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2111`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2111) target root read from head block_roots without advancing

**Skeptic check.** Read produce_unaggregated_attestation: advance happens only when the request epoch is later than the state epoch, matching the idea; earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#4501](https://github.com/OffchainLabs/prysm/pull/4501)

</details>


<a id="beacon_api-L056"></a>
<details>
<summary><b>beacon_api-L056</b> paginate before compute; custom marshal — <i>n/a · low · S · cpu, memory, latency</i></summary>

**Idea.** For paginated validator-balance queries compute only the requested page rather than all balances then slicing; use a hand-written fixed-layout marshal for balances in the archive instead of generic SSZ.

**Gap in Lighthouse.** Beacon API has no pagination for validator balances (that was a Prysm gRPC feature), and Lighthouse has no archive that stores balances as hand-marshalled blobs; balances live in milhouse lists.

**Impact.** None.

**Best measured result.** 62207 to 10719 ns/op, 1012 to 109 allocs; archive 28187 to 8016 ns/op

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/validators.rs:86`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validators.rs#L86) balances endpoint has no pagination, filters by ids

**Sources.** [prysm#4530](https://github.com/OffchainLabs/prysm/pull/4530), [teku#1265](https://github.com/Consensys-Incorporated/teku/pull/1265)

</details>


<a id="beacon_api-L057"></a>
<details>
<summary><b>beacon_api-L057</b> limit slot advance — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Advance the state only to the start slot of the requested epoch for attestation data, and clone head state in accessors.

**Impact.** Advance limited to epoch start; common case does no advance and no state clone.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2062-2139`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2062-L2139) attestation data uses a borrowed head snapshot and head state when in the same epoch
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2150-2165`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2150-L2165) otherwise get_advanced_hot_state + partial_state_advance only to request_epoch start slot
- [`beacon_node/http_api/src/attester_duties.rs:184-205`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L184-L205) duties advance only to target_epoch-1 start

**Skeptic check.** Verified both the bounded advance and that the head state is borrowed, not cloned, on the fast path. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#4533](https://github.com/OffchainLabs/prysm/pull/4533)

</details>


<a id="beacon_api-L058"></a>
<details>
<summary><b>beacon_api-L058</b> pre-allocate vectors — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** Pre-allocate response slices with known capacity in bulk API handlers (e.g. per-validator performance) so appending does not repeatedly reallocate.

**Impact.** Rust collect over exact-size iterators preallocates; remaining Vec::new() sites in http_api are small failure/peer lists, not per-validator bulk responses.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/attester_duties.rs:151-158`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L151-L158) duties collected from a slice-mapped iterator (exact size hint)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1797-1811`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1797-L1811) ptc duties collected the same way

**Skeptic check.** Grepped http_api for push-loop Vec::new patterns; none on per-validator bulk response paths. Earlier verdict correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#4979](https://github.com/OffchainLabs/prysm/pull/4979)

</details>


<a id="beacon_api-L059"></a>
<details>
<summary><b>beacon_api-L059</b> skip eth1 calls for active validators — <i>n/a · low · S · latency</i></summary>

**Idea.** Avoid eth1 RPC calls when answering validator activation-wait queries for already active validators; use state only.

**Impact.** Lighthouse validator/duties endpoints do not make eth1 calls, so there is nothing to skip.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/validator/mod.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs): validator endpoints use state only, no eth1 RPC

**Sources.** [prysm#5396](https://github.com/OffchainLabs/prysm/pull/5396)

</details>


<a id="beacon_api-L060"></a>
<details>
<summary><b>beacon_api-L060</b> group by block root — <i>n/a · medium · cpu, latency</i></summary>

**Idea.** In the indexed-attestations endpoint, group attestations by beacon block root so each state or committee set is loaded once per group instead of per attestation.

**Impact.** Lighthouse has no indexed-attestations HTTP endpoint (a Prysm-specific API), so there is nothing to batch.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs:1284`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L1284),1931 only the standard attestations routes; grep for indexed_attestation in http_api finds only publish paths

**Sources.** [prysm#5441](https://github.com/OffchainLabs/prysm/pull/5441)

</details>


<a id="beacon_api-L061"></a>
<details>
<summary><b>beacon_api-L061</b> remove unused eth1 calls — <i>n/a · low · S · latency</i></summary>

**Idea.** In the duties endpoint, do not query eth1 for inactive validators when the result is unused.

**Impact.** The duties endpoints have no eth1 query to remove.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/attester_duties.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs) and proposer_duties.rs: no eth1 queries

**Sources.** [prysm#5516](https://github.com/OffchainLabs/prysm/pull/5516)

</details>


<a id="beacon_api-L062"></a>
<details>
<summary><b>beacon_api-L062</b> use target-root state — <i>n/a · medium · cpu, latency</i></summary>

**Idea.** When converting attestations to indexed form for an API, use the shuffling/state at the target checkpoint instead of the attested block root, so the state does not have to be regenerated by replaying slots for every distinct block root.

**Impact.** No API endpoint converts attestations to indexed form; the gossip path already uses the shuffling cache keyed by decision block rather than replaying a state per block root.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:7593`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7593) with_committee_cache resolves shuffling by (block root, epoch) via the shuffling cache keyed by decision root
- [`beacon_node/http_api/src/lib.rs:1284`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L1284) no indexed-attestations endpoint

**Sources.** [prysm#5548](https://github.com/OffchainLabs/prysm/pull/5548)

</details>


<a id="beacon_api-L063"></a>
<details>
<summary><b>beacon_api-L063</b> read-only validator access — <i>implemented · low · S · memory</i></summary>

**Idea.** Use read-only validator accessors where validators are not mutated so each access does not copy the validator.

**Impact.** Validator reads borrow from milhouse; no per-access copy.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/validator/mod.rs:53-63`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L53-L63) state.validators().get(index) compares pubkey by reference
- ~/.cargo/registry/src/*/milhouse-*/src/list.rs:156 List::get returns Option&lt;&amp;T&gt;

**Skeptic check.** Confirmed milhouse List::get returns a reference; read paths do not copy validators. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#5775](https://github.com/OffchainLabs/prysm/pull/5775)

</details>


<a id="beacon_api-L064"></a>
<details>
<summary><b>beacon_api-L064</b> state regen by target root — <i>implemented · low · S · latency, cpu</i></summary>

**Idea.** When streaming indexed attestations, regenerate state keyed by the attestation target root rather than by epoch number, so committee lookup is near instant for real-time conversion.

**Impact.** Indexed-attestation conversion on gossip and API paths resolves committees by target root through the shuffling cache, with no epoch-number state regen; Lighthouse has no indexed-attestation stream.

**Best measured result.** realtime conversion near instant

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:1645`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1645) map_attestation_committees calls with_committee_cache(target.root, attestation_epoch)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7593`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7593) with_committee_cache -&gt; with_cached_shuffling keyed by shuffling decision root via shuffling_cache

**Skeptic check.** Confirmed committee lookup for attestations is keyed by target root/decision root, the same effect as the Prysm change; earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#5971](https://github.com/OffchainLabs/prysm/pull/5971)

</details>


<a id="beacon_api-L065"></a>
<details>
<summary><b>beacon_api-L065</b> offset slot ticker for streaming — <i>n/a · low · S · cpu, latency</i></summary>

**Idea.** Stream indexed attestations once per slot at a fixed offset (2/3 of a slot) so the work does not coincide with the node's duty-time processing.

**Impact.** Lighthouse events are pushed from a broadcast channel as events occur, with no per-slot polling stream to offset.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs:3451`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L3451) SSE via tokio broadcast; no indexed-attestation stream

**Sources.** [prysm#5999](https://github.com/OffchainLabs/prysm/pull/5999)

</details>


<a id="beacon_api-L066"></a>
<details>
<summary><b>beacon_api-L066</b> use head state when possible — <i>implemented · low · S · latency, cpu</i></summary>

**Idea.** For the list-validators API, use the head state directly when no specific epoch state is requested rather than regenerating a historical state.

**Impact.** Head requests read the in-memory head state; no regeneration.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/state_id.rs:179-186`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L179-L186) map_state_and_execution_optimistic_and_finalized returns the cached head snapshot state for Head
- [`beacon_node/http_api/src/state_id.rs:227-233`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L227-L233) map_state borrows head.snapshot.beacon_state without copy
- [`beacon_node/http_api/src/validators.rs:15-17`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validators.rs#L15-L17) list-validators goes through this state_id mapping

**Skeptic check.** Verified state_id.rs Head branch short-circuits to the cached head snapshot before any get_state call; earlier evidence was right (cited block_id.rs but state_id.rs is the relevant file).

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#6580](https://github.com/OffchainLabs/prysm/pull/6580)

</details>


<a id="beacon_api-L067"></a>
<details>
<summary><b>beacon_api-L067</b> iterate validators without copy — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Remove the helper that copies all validators into a list; iterate with a read-only per-validator callback instead.

**Impact.** Validators are borrowed and filtered lazily; only the response entries are built.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/validators.rs:35-40`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validators.rs#L35-L40) iterates state.validators().iter().zip(state.balances().iter()) inside the map_state closure with filters

**Skeptic check.** Confirmed the handler iterates the borrowed validator list with filter/filter_map; no intermediate full copy of all validators.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#7717](https://github.com/OffchainLabs/prysm/pull/7717)

</details>


<a id="beacon_api-L068"></a>
<details>
<summary><b>beacon_api-L068</b> short-circuit genesis slot — <i>n/a · low · S · db_hot</i></summary>

**Idea.** In the canonical-slot check, return true for slot 0 right away so the API does not hit the DB to compare against the genesis root.

**Impact.** Lighthouse has no Prysm-style canonical-slot DB comparison; slot ids resolve through block_root_at_slot.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/block_id.rs:59`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L59) Genesis handled via genesis_block_root; Slot goes via block_root_at_slot (fork choice/cached)

**Sources.** [prysm#8269](https://github.com/OffchainLabs/prysm/pull/8269)

</details>


<a id="beacon_api-L069"></a>
<details>
<summary><b>beacon_api-L069</b> head getters without state copy — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Provide head getters for validator index and pubkey that read from the head state without copying it.

**Impact.** Index and pubkey lookups never touch or copy a state; head-state API reads borrow the snapshot.

**Best measured result.** Says cheap, no state copy

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:1628`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1628) validator_index reads validator_pubkey_cache
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1666`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1666) validator_pubkey / validator_pubkey_bytes / validator_pubkey_bytes_many from the cache
- [`beacon_node/http_api/src/state_id.rs:218`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L218) map_state_and_execution_optimistic_and_finalized borrows the head state for CoreStateId::Head

**Skeptic check.** Verified both getters use the global pubkey cache and the head path passes a reference; earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#9303](https://github.com/OffchainLabs/prysm/pull/9303)

</details>


<a id="beacon_api-L070"></a>
<details>
<summary><b>beacon_api-L070</b> fewer state fetches — <i>n/a · low · S · latency, startup</i></summary>

**Idea.** For the doppelganger check, use only the head state and the state 32 slots earlier (using participation flags), fetching one fewer state per validator.

**Impact.** Liveness is answered from in-memory observed caches, not states, so there are no state fetches to reduce.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs:2995-3020`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L2995-L3020) liveness uses validator_seen_at_epoch (beacon_chain.rs:8346) observed-attester caches, no states

**Sources.** [prysm#9969](https://github.com/OffchainLabs/prysm/pull/9969)

</details>


<a id="beacon_api-L071"></a>
<details>
<summary><b>beacon_api-L071</b> skip replay for future slot — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Reject API requests for a state at a slot beyond the head before attempting state replay, avoiding useless slot processing.

**Impact.** Future-slot state requests return 404 without any state load or replay.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:964`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L964) state_root_at_slot returns None when request_slot &gt; self.slot()
- [`beacon_node/http_api/src/state_id.rs:150`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L150) StateId::root maps None to custom_not_found before StateId::state loads anything
- [`beacon_node/beacon_chain/src/beacon_chain.rs:984`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L984) slots between head block and clock resolve to the head state root
- [`beacon_node/store/src/hot_cold_store.rs:1087`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1087) get_state does not replay to the slot hint

**Skeptic check.** Confirmed the wall-clock check precedes any DB load, and the slot hint in get_state does not trigger replay; earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#10915](https://github.com/OffchainLabs/prysm/pull/10915)

</details>


<a id="beacon_api-L072"></a>
<details>
<summary><b>beacon_api-L072</b> root lookup instead of full state — <i>implemented · low · S · memory, cpu, latency</i></summary>

**Idea.** Determine optimistic status from the head root in fork choice rather than loading the full head state.

**Impact.** Optimistic status is a fork-choice lookup; no state load.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:7402-7406`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7402-L7406) is_optimistic_or_invalid_head
- [`beacon_node/beacon_chain/src/canonical_head.rs:577-582`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L577-L582) head_execution_status reads fork choice node status for cached head node

**Skeptic check.** Verified head_execution_status takes the cached head Arc and queries fork choice by node; earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#11074](https://github.com/OffchainLabs/prysm/pull/11074)

</details>


<a id="beacon_api-L073"></a>
<details>
<summary><b>beacon_api-L073</b> skip unchanged DB write — <i>implemented · low · S · disk</i></summary>

**Idea.** On proposer-preparation calls, read the stored fee recipient and write to the DB only when it changed, avoiding a DB write per validator per epoch.

**Impact.** There is no per-validator DB write on prepare_beacon_proposer; the cost the idea removes does not exist in Lighthouse.

**Best measured result.** Benchmark: 10000 validators 11.7ms/op; 1000 validators 1.0ms/op (shows read check is cheap)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/lib.rs:816`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L816) update_proposer_preparation updates an in-memory HashMap, no DB write
- [`beacon_node/execution_layer/src/lib.rs:851`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L851) clean_proposer_caches prunes entries older than 2 epochs

**Skeptic check.** Verified proposer preparation lives only in memory; the effect is achieved more strongly than the idea (arguably n/a), earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#11295](https://github.com/OffchainLabs/prysm/pull/11295)

</details>


<a id="beacon_api-L074"></a>
<details>
<summary><b>beacon_api-L074</b> skip unchanged DB write — <i>n/a · low · S · disk</i></summary>

**Idea.** Same as the Prysm API change: skip the fee recipient DB write when the value is unchanged.

**Impact.** Lighthouse keeps proposer preparation data in memory, there is no DB write to skip.

**Evidence (Lighthouse @ 928b61e719).**

- beacon_node/fee recipients held in VC/in-memory proposer preparation, no DB write per API call

**Sources.** [prysm#11296](https://github.com/OffchainLabs/prysm/pull/11296)

</details>


<a id="beacon_api-L075"></a>
<details>
<summary><b>beacon_api-L075</b> fix SSE library memory leak — <i>n/a · low · S · memory</i></summary>

**Idea.** Upgrade the server-sent-events library to fix a memory leak in event stream handling for long-lived subscribers.

**Impact.** The leak was in a Go library Lighthouse does not use.

**Best measured result.** None stated

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs:3451`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L3451) uses tokio_stream BroadcastStream, not the Go SSE library

**Sources.** [prysm#12676](https://github.com/OffchainLabs/prysm/pull/12676)

</details>


<a id="beacon_api-L076"></a>
<details>
<summary><b>beacon_api-L076</b> head state with next-slot cache — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** For duties of the current and next epoch, use the head state with the next-slot cache instead of advancing a state by slots, avoiding an epoch transition on each request.

**Impact.** Duties for current and next epoch avoid epoch transitions in normal operation; only historic epochs load or advance states.

**Best measured result.** avoids epoch transition in all calls during normal operation

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/attester_duties.rs:45`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L45) current/next epoch go to cached_attestation_duties -&gt; validator_attestation_duties (shuffling cache)
- [`beacon_node/http_api/src/proposer_duties.rs:81`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/proposer_duties.rs#L81) current epoch served from try_proposer_duties_from_cache
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:321`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L321) ensure_state_can_determine_proposers_for_epoch advances only below the decision epoch (no advance post-Fulu for next epoch)

**Skeptic check.** Checked attester and proposer duty routes; both serve current/next epoch from caches or the head state with at most a partial advance; earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#12940](https://github.com/OffchainLabs/prysm/pull/12940), [prysm#15548](https://github.com/OffchainLabs/prysm/pull/15548)

</details>


<a id="beacon_api-L077"></a>
<details>
<summary><b>beacon_api-L077</b> skip check on cache hit — <i>implemented · low · S · latency, cpu</i></summary>

**Idea.** On attestation-data requests, serve a cached attestation data for the current head before running the optimistic-status check, since a cached entry implies the head was already verified non-optimistic.

**Impact.** Cache hit skips the check; the slow path check is a cheap fork-choice read, so little to gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2025-2030`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2025-L2030) early_attester_cache.try_attest returns before filter_optimistic_attestation
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2201`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2201) filter_optimistic_attestation only on slow path
- [`beacon_node/http_api/src/validator/mod.rs:294-297`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L294-L297) attestation_data handler calls produce_unaggregated_attestation

**Skeptic check.** Lighthouse has no Prysm-style per-slot attestation-data cache, but its only cache (early attester cache, never filled with optimistic blocks) returns before the optimistic filter, which matches the idea; the remaining check is negligible.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#13462](https://github.com/OffchainLabs/prysm/pull/13462)

</details>


<a id="beacon_api-L078"></a>
<details>
<summary><b>beacon_api-L078</b> use next slot cache in rewards — <i>partial · medium · S · latency</i></summary>

**Idea.** Use the cached next-slot pre-advanced state for the block rewards/value API rather than replaying and processing the epoch transition on demand.

**Gap in Lighthouse.** Only the standalone rewards endpoints replay. In get_state_before_applying_block, try chain.store.get_advanced_hot_state(block.parent_root(), block.slot(), parent_block.state_root()) first (it returns the state-cache entry pre-advanced by the state advance timer, or advances it itself), falling back to the replay.

**Impact.** Block-production value (the Prysm PR's main case) is already fast. Remaining gain: /eth/v1/beacon/rewards/blocks and sync_committee rewards for recent epoch-boundary blocks drop from hundreds of ms to tens of ms; explorer/staking-pool traffic only.

**Best measured result.** ~500ms down to ~20ms for slot-0 blocks

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_production/mod.rs:83-91`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L83-L91) block production loads the head state pre-advanced to the proposal slot via store.get_advanced_hot_state (filled by the state advance timer)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:6537-6540`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6537-L6540) consensus_block_value is computed with compute_beacon_block_reward on that already-advanced production state, so /eth/v3/validator/blocks (the Prysm PR's motivating 500ms-&gt;20ms case) never replays the epoch transition
- [`beacon_node/http_api/src/sync_committee_rewards.rs:48-76`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/sync_committee_rewards.rs#L48-L76) get_state_before_applying_block (used by /eth/v1/beacon/rewards/blocks and sync_committee rewards) still loads the parent state and runs BlockReplayer.apply_blocks(vec![], Some(block.slot())), doing the epoch transition on demand
- [`beacon_node/http_api/src/standard_block_rewards.rs:18-21`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/standard_block_rewards.rs#L18-L21)

**Second check.** The earlier review looked only at the http_api rewards path; the produce-block path (block_production/mod.rs, beacon_chain.rs:6537) already computes the block value on the state-advance-timer state, which is exactly what Prysm#13684 targeted.

**Verdict history.** not (checked) → partial (refuted)

**Sources.** [prysm#13684](https://github.com/OffchainLabs/prysm/pull/13684)

</details>


<a id="beacon_api-L079"></a>
<details>
<summary><b>beacon_api-L079</b> read-only validator views — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** In the validators API, iterate read-only validator views instead of copying the full validator list from the state, avoiding copies.

**Impact.** The validators endpoint copies no validator list; only the returned rows are cloned. Non-head states are milhouse structural-sharing clones.

**Best measured result.** speeds up fetching all validators ~3x

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/state_id.rs:218`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L218) head state borrowed, not cloned
- [`beacon_node/http_api/src/validators.rs:35`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validators.rs#L35) iterates state.validators().iter() by reference and clones only matched Validator rows

**Skeptic check.** Verified the iteration is read-only over the milhouse list; earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#13873](https://github.com/OffchainLabs/prysm/pull/13873)

</details>


<a id="beacon_api-L080"></a>
<details>
<summary><b>beacon_api-L080</b> precompute and store updates — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Serve light client updates by range from precomputed updates stored in the DB instead of computing them per request, since the computation is heavy.

**Impact.** Updates by range are a DB column range read plus SSZ decode; no per-request computation.

**Best measured result.** computing them is described as a very heavy process

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/light_client_server_cache.rs:179-205`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_server_cache.rs#L179-L205)
- [`beacon_node/store/src/hot_cold_store.rs:855-890`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L855-L890)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1503-1511`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1503-L1511)
- [`beacon_node/http_api/src/light_client.rs:21-33`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/light_client.rs#L21-L33)

**Skeptic check.** Verified: LightClientUpdate is built on block import, best-per-period persisted via store_light_client_update, and the API endpoint reads DBColumn::LightClientUpdate by period range. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#14531](https://github.com/OffchainLabs/prysm/pull/14531)

</details>


<a id="beacon_api-L081"></a>
<details>
<summary><b>beacon_api-L081</b> precomputed bootstrap in DB — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Serve light client bootstrap requests from precomputed bootstraps stored in the database at block import time instead of building them from state on request.

**Impact.** Bootstrap request is a few DB reads, never a state load.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/light_client_server_cache.rs:118-123`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_server_cache.rs#L118-L123) sync committee branch and sync committee stored at block import
- [`beacon_node/beacon_chain/src/light_client_server_cache.rs:396-446`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_server_cache.rs#L396-L446) get_light_client_bootstrap built from blinded block + stored branch + stored committee
- [`beacon_node/beacon_chain/src/beacon_chain.rs:8374-8389`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L8374-L8389) uses head only for finalized period

**Skeptic check.** Confirmed the bootstrap components are persisted at import and assembled on request without states; the full bootstrap object is not stored but the expensive part (state-derived proof and committee) is.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#14718](https://github.com/OffchainLabs/prysm/pull/14718)

</details>


<a id="beacon_api-L082"></a>
<details>
<summary><b>beacon_api-L082</b> gzip HTTP responses — <i>partial · medium · S · bandwidth</i></summary>

**Idea.** Honor Accept-Encoding gzip in the HTTP API server and compress large responses such as states, cutting bytes transferred.

**Gap in Lighthouse.** The main beacon API is already served through axum (lib.rs:3701), so adding axum_utils::CompressionLayer (tower-http, already a dependency) on axum_router would honour Accept-Encoding for all routes; restrict to large bodies via a predicate (e.g. SizeAbove) and keep SSE streams uncompressed.

**Impact.** Cuts egress bytes for large JSON responses (states, validators, light client updates) by ~5-10x for remote clients; costs node CPU, so a bandwidth saving.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_metrics/src/lib.rs:120`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_metrics/src/lib.rs#L120) .layer(CompressionLayer::new()) on the metrics server only
- [`validator_client/http_metrics/src/lib.rs:128`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/http_metrics/src/lib.rs#L128) same for VC metrics
- [`beacon_node/http_api/src/lib.rs:3693-3705`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L3693-L3705) main API: warp routes wrapped in axum Router::new().fallback_service(warp::service(routes)) with no layers added
- Cargo.toml:276 warp built with default-features=false, features=["server"] (no compression feature)

**Second check.** Checked the axum server builder (common/axum_utils/src/server) and the http_api router assembly: no compression layer; the axum wrapper makes the fix a one-line layer, smaller than the earlier gap suggested.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [prysm#14982](https://github.com/OffchainLabs/prysm/pull/14982)

</details>


<a id="beacon_api-L083"></a>
<details>
<summary><b>beacon_api-L083</b> precompute LC updates — <i>implemented · low · S · cpu</i></summary>

**Idea.** Compute light client finality and optimistic updates once at block processing and store them, so the API and gossip can read the stored result instead of recomputing from state.

**Impact.** Computed once per import and reused by gossip, RPC and API.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/light_client_server_cache.rs:80-175`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_server_cache.rs#L80-L175) recompute_and_cache_updates builds optimistic/finality updates at import into latest_*_update
- [`beacon_node/http_api/src/sync_committees.rs:321-343`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/sync_committees.rs#L321-L343) gossip publishes stored updates via should_broadcast_*
- [`beacon_node/beacon_chain/src/light_client_finality_update_verification.rs:105-119`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_finality_update_verification.rs#L105-L119) gossip verification compares against stored update

**Skeptic check.** Verified the import-time computation and that gossip and verification read the stored update; earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#15124](https://github.com/OffchainLabs/prysm/pull/15124)

</details>


<a id="beacon_api-L084"></a>
<details>
<summary><b>beacon_api-L084</b> serve LC updates from store — <i>implemented · low · S · cpu</i></summary>

**Idea.** Serve light client finality and optimistic updates from the stored precomputed update rather than computing them from state on each API request.

**Impact.** API serves in-memory updates; no state work per request.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs:1816`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L1816) optimistic_update endpoint reads get_latest_optimistic_update
- [`beacon_node/http_api/src/lib.rs:1864`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L1864) finality_update endpoint reads get_latest_finality_update
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1032`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1032),1066 RPC also serves stored updates

**Skeptic check.** Confirmed both HTTP endpoints and RPC clone the stored latest update.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#15172](https://github.com/OffchainLabs/prysm/pull/15172)

</details>


<a id="beacon_api-L085"></a>
<details>
<summary><b>beacon_api-L085</b> use cached proposer index — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** For the payload attributes event, read the proposer index from the proposer cache first and only fall back to loading and advancing the state when it is missing.

**Impact.** Event emission adds no state load; proposer comes from the proposer cache.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5314-5317`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5314-L5317) get_pre_payload_attributes resolves proposer via with_proposer_cache, state fallback only on miss (5339-5344)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7071-7106`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7071-L7106) payload attributes SSE reuses the proposer computed for preparation

**Skeptic check.** Verified the SSE event is built from the same pre_payload_attributes whose proposer index is read from the proposer cache first, falling back to the head state only on a cache miss.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#15229](https://github.com/OffchainLabs/prysm/pull/15229)

</details>


<a id="beacon_api-L086"></a>
<details>
<summary><b>beacon_api-L086</b> reverse index for duties lookup — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** For large duty requests, build a validator-index to committee-assignment reverse map once per epoch and look up in O(1), instead of scanning slots x committees x members per validator. Keep linear scan for small requests (under ~3000).

**Gap in Lighthouse.** Residual only: get_attestation_duties loops over up to epoch_committee_count (2048) committee ranges per validator instead of computing the committee by division; compute_ptc_duties is still O(N*slots*PTC) (TODO at beacon_chain.rs:1766).

**Impact.** Members are never scanned; per-validator cost is O(committees) arithmetic, comparable to Prysm's post-fix cost.

**Best measured result.** 30000 validators 8.7s to 0.8s; 91% faster at 30k, 67% at 5k

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/committee_cache.rs:295-325`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L295-L325)
- [`consensus/types/src/state/committee_cache.rs:389-395`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L389-L395)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1735-1762`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1735-L1762)
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:315-410`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L315-L410)

**Second check.** The earlier review saw the committee loop but missed that shuffling_positions is precisely the per-epoch reverse index the idea asks for, cached with the CommitteeCache; the member scan Prysm eliminated does not exist in Lighthouse.

**Skeptic check.** Verified shuffling_positions reverse map built once per epoch cache and O(1) shuffled_position lookup, used by validator_attestation_duties through the shared shuffling cache. Earlier evidence correct; the remaining committee-range loop is a minor constant.

**Verdict history.** not (checked) → implemented (refuted) → implemented (skeptic)

**Sources.** [prysm#15558](https://github.com/OffchainLabs/prysm/pull/15558)

</details>


<a id="beacon_api-L087"></a>
<details>
<summary><b>beacon_api-L087</b> unify resolver lookup paths — <i>n/a · low · cpu</i></summary>

**Idea.** Unify block and blob lookup paths in the API block resolver, adding justified support and avoiding redundant lookups.

**Impact.** Prysm-specific refactor of its Blocker interface (justified id support, fewer duplicate lookups); Lighthouse BlockId resolves via fork choice/store in one path and the gain was cosmetic.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/block_id.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs) and state_id.rs: resolver design differs; no Prysm-style Blocker/Fetcher split
- [`beacon_node/http_api/src/lib.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs) block_id use

**Sources.** [prysm#15715](https://github.com/OffchainLabs/prysm/pull/15715)

</details>


<a id="beacon_api-L088"></a>
<details>
<summary><b>beacon_api-L088</b> use lookahead not state advance — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** For next-epoch proposer duties on Fulu, read the state's cached proposer lookahead rather than advancing the state.

**Impact.** Post-Fulu next-epoch proposer duties come from the head state's proposer_lookahead with no state advance; only an O(1) milhouse clone of the head state remains.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/proposer_duties.rs:91-108`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/proposer_duties.rs#L91-L108)
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:253-287`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L253-L287)
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:320-355`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L320-L355)
- [`consensus/types/src/core/chain_spec.rs:1176-1199`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/core/chain_spec.rs#L1176-L1199)

**Skeptic check.** Verified that post-Fulu proposer_shuffling_decision_slot(N+1) is the end of epoch N-1, so ensure_state_can_determine_proposers_for_epoch is a no-op for a head state in epoch N and get_beacon_proposer_indices reads the lookahead. The earlier evidence is correct. A state advance happens only when the head lags an epoch behind, and the spec requires it then.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#15534](https://github.com/OffchainLabs/prysm/pull/15534)

</details>


<a id="beacon_api-L089"></a>
<details>
<summary><b>beacon_api-L089</b> per-request committee assignment, early exit — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** For the duties endpoint, compute committee assignments only for the requested validator indices, exiting early once all are found, instead of precomputing every committee and building a per-validator map for the whole set.

**Impact.** Work and memory are proportional to the requested indices; the only shared structure is the per-epoch committee cache, already kept for gossip.

**Best measured result.** 100k validators: 12.6ms/11.8KB vs 16.7ms/7.9MB for 10 indices; 1.2-1.3x faster, 14-670x less memory

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:1752-1758`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1752-L1758)
- [`consensus/types/src/state/committee_cache.rs:295-325`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L295-L325)
- [`beacon_node/http_api/src/attester_duties.rs:152-159`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L152-L159)

**Skeptic check.** Verified both the cached and historic duty paths map only request_indices through get_attestation_duties, which returns on the first matching committee; no per-validator map for the full set is built. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#15784](https://github.com/OffchainLabs/prysm/pull/15784)

</details>


<a id="beacon_api-L090"></a>
<details>
<summary><b>beacon_api-L090</b> skip KZG proof computation on blob reconstruct — <i>not · medium · M · cpu, memory, latency</i></summary>

**Idea.** For the get-blobs API, rebuild blobs from stored data columns without computing KZG cell proofs, since the response needs only blob data.

**Gap in Lighthouse.** Two cheaper paths are missing: (1) the extension is systematic, so if columns 0..number_of_columns/2 are all held the blob is just their concatenation (the check at kzg_utils.rs:797 tests len &lt; number_of_columns instead of whether the first half is present); (2) otherwise recover cells only via ekzg-erasure-codes recover_polynomial_coefficient (or an upstream rust_eth_kzg recover_cells API) and skip the proof computation.

**Impact.** get_blobs / blob_sidecars on non-supernodes holding &gt;=50% columns: per-blob latency drops by orders of magnitude since proof computation dominates; irrelevant for supernodes holding all columns and off the consensus path.

**Best measured result.** 1 blob: 13,506x faster, 90.4% less memory; 6 blobs: 2,921x faster

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/kzg_utils.rs:797-811`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L797-L811) when fewer than all columns are present, calls kzg.recover_cells_and_compute_kzg_proofs and discards the proofs
- [`beacon_node/beacon_chain/src/kzg_utils.rs:812-817`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L812-L817) skip only when all columns are present (concatenate first half cells)
- [`crypto/kzg/src/lib.rs:307-318`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/kzg/src/lib.rs#L307-L318) wrapper exposes only the with-proofs recovery
- rust_eth_kzg-0.9.1/src/prover.rs:156 recover_cells_and_kzg_proofs is the only public recovery API; ekzg-erasure-codes-0.9.1/src/reed_solomon.rs:179 recover_polynomial_coefficient is the cells-only primitive

**Second check.** Checked rust_eth_kzg 0.9.1 and ekzg-* 0.9.1 public APIs and the full-columns shortcut in reconstruct_blobs_with_indices; only the all-columns case avoids proof computation.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [prysm#15902](https://github.com/OffchainLabs/prysm/pull/15902)

</details>


<a id="beacon_api-L091"></a>
<details>
<summary><b>beacon_api-L091</b> lower gzip level — <i>not · medium · S · cpu</i></summary>

**Idea.** Compress large API responses (e.g. validators list) at the fastest gzip level instead of the default level 6, since compression dominated the CPU profile.

**Gap in Lighthouse.** Depends on L082. When adding CompressionLayer to the HTTP API axum router, set .quality(CompressionLevel::Fastest); optionally the same for the metrics servers.

**Impact.** Only relevant after gzip is added to the API; avoids compression dominating CPU on large validator-list responses.

**Best measured result.** gzip was almost 40% of CPU profile on GetValidators

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs:3701`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L3701) main API has no compression layer, so no level to tune
- [`beacon_node/http_metrics/src/lib.rs:120`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_metrics/src/lib.rs#L120) CompressionLayer::new() uses tower-http's default level (no .quality(CompressionLevel::Fastest))
- [`validator_client/http_metrics/src/lib.rs:128`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/http_metrics/src/lib.rs#L128) same

**Second check.** Grepped the whole tree for CompressionLevel/quality: no level is configured anywhere.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [prysm#16399](https://github.com/OffchainLabs/prysm/pull/16399)

</details>


<a id="beacon_api-L092"></a>
<details>
<summary><b>beacon_api-L092</b> reject unavailable historical state early — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Return 404 for state requests older than the earliest available or backfill low slot instead of replaying from genesis, avoiding minutes of useless state replay on the API.

**Impact.** Slots in the unavailable (lower,upper) historic window return 404 before any state load or replay.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:964-975`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L964-L975)
- [`beacon_node/store/src/hot_cold_store.rs:2920-2938`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2920-L2938)
- [`beacon_node/http_api/src/state_id.rs:126-130`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L126-L130)

**Skeptic check.** Verified state_root_at_slot returns None for slots between state_lower_limit and min(state_upper_limit, split), which covers checkpoint-synced nodes without reconstruction; StateId turns None into not-found. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#16615](https://github.com/OffchainLabs/prysm/pull/16615)

</details>


<a id="beacon_api-L093"></a>
<details>
<summary><b>beacon_api-L093</b> per-slot cache plus singleflight — <i>n/a · low · cpu, latency</i></summary>

**Idea.** Cache the payload attestation data per slot and collapse concurrent misses with singleflight, so a burst of committee-member requests at the slot deadline costs a single forkchoice read.

**Impact.** Lighthouse has no heavy forkchoice read on this path; a burst of PTC requests costs a few lock reads each, so a cache or singleflight would gain almost nothing.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2217-2262`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2217-L2262) produce_payload_attestation_data does a head snapshot read, a short envelope_times_cache read and a pending_payload_cache lookup; no fork-choice read
- [`beacon_node/http_api/src/validator/mod.rs:319-400`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L319-L400) handler

**Sources.** [prysm#16744](https://github.com/OffchainLabs/prysm/pull/16744)

</details>


<a id="beacon_api-L094"></a>
<details>
<summary><b>beacon_api-L094</b> lazy filtered validator iteration — <i>implemented · low · S · memory, cpu, latency</i></summary>

**Idea.** Iterate validators lazily with a filter (iterator/yield) in validator-listing and counting endpoints instead of materializing the whole validator set before filtering, avoiding millions of allocations per request.

**Gap in Lighthouse.** Residual: with an id filter all validators are still iterated (HashSet lookup per validator) rather than indexing directly; no allocation though.

**Impact.** Only matching validators are cloned/allocated in validators, balances and identities endpoints.

**Best measured result.** status=withdrawal_possible: ~2.3M validators materialized -&gt; 1442

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/validators.rs:34-75`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validators.rs#L34-L75)
- [`beacon_node/http_api/src/validators.rs:86-125`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validators.rs#L86-L125)
- [`beacon_node/http_api/src/validators.rs:134-171`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validators.rs#L134-L171)

**Skeptic check.** Verified lazy iter().zip().enumerate().filter().filter_map().collect() in all three listing endpoints; clone happens only on match. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#16838](https://github.com/OffchainLabs/prysm/pull/16838), [nimbus#2126](https://github.com/status-im/nimbus-eth2/pull/2126)

</details>


<a id="beacon_api-L095"></a>
<details>
<summary><b>beacon_api-L095</b> read-only state in duties — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Use read-only (no-copy) beacon state handles in the duties endpoints, so computing proposer/attester/sync duties does not deep-copy the state.

**Impact.** The hot duty paths read the shuffling cache or the head's sync committees and copy no state; the fallback paths clone a milhouse state, which is a structural-sharing clone.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/attester_duties.rs:60-78`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L60-L78)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1735-1764`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1735-L1764)
- [`beacon_node/http_api/src/attester_duties.rs:90-104`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L90-L104)
- [`beacon_node/http_api/src/sync_committees.rs:44-55`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/sync_committees.rs#L44-L55)
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:260-268`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L260-L268)

**Skeptic check.** Current and next epoch attester duties go through validator_attestation_duties on the committee cache and clone no state at all. Sync duties use sync_committee_duties_from_head. Only the historic and fallback paths clone the head state, and that clone is cheap with milhouse. The earlier evidence cited only the fallback clone, but the verdict holds.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#17430](https://github.com/OffchainLabs/prysm/pull/17430)

</details>


<a id="beacon_api-L096"></a>
<details>
<summary><b>beacon_api-L096</b> linear-time incremental head parsing — <i>n/a · low · S · cpu, memory</i></summary>

**Idea.** In the HTTP API server, re-parse a partially received request head only when the buffered bytes could contain the end of the head (scanning each byte once) or when the buffer has doubled, so parsing cost is linear instead of quadratic. Also shrink a connection's read buffer back to a small size once a large request is consumed, and cap head size.

**Impact.** Head parsing is delegated to hyper, which reads into a bounded buffer and does not use the quadratic reparse pattern of a hand-written server.

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.toml:172 hyper 1 / :276 warp 0.4 do request-head parsing (httparse in hyper)

**Sources.** [silver#452](https://github.com/gattaca-com/silver/pull/452)

</details>


<a id="beacon_api-L097"></a>
<details>
<summary><b>beacon_api-L097</b> single storage read per request — <i>partial · low · S · cpu</i></summary>

**Idea.** In the chain head API handler, read the head once from storage and derive all fields from that snapshot instead of making several storage calls.

**Gap in Lighthouse.** The GET beacon/headers/{block_id} handler (get_beacon_headers_block_id) resolves 'head' to a root from the cached head, then calls BlockId::from_root(root).blinded_block(), which does a hot_db get_bytes and an SSZ decode of the head block, followed by block_root_at_slot. The head block is already in cached_head().snapshot, and block_id.blinded_block() has a CoreBlockId::Head fast path that this handler bypasses. This also takes two head views that can race across a head change.

**Impact.** Saves one DB read and one block SSZ decode for each headers/head request. This is small and matters only for clients that poll headers/head often.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs:813-822`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L813-L822)
- [`beacon_node/http_api/src/block_id.rs:150-166`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L150-L166)
- [`beacon_node/http_api/src/block_id.rs:182-191`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L182-L191)
- [`beacon_node/store/src/hot_cold_store.rs:663-686`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L663-L686)
- [`beacon_node/http_api/src/lib.rs:716-726`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L716-L726)
- [`beacon_node/http_api/src/state_id.rs:179-189`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L179-L189)

**Skeptic check.** Most head endpoints (state_id Head, the blocks Head fast path, and headers with no query) use the cached head snapshot, so the earlier evidence is right for them. headers/{head} is a real exception: it converts the request to a Root id and reads the block from the store again.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [teku#1207](https://github.com/Consensys-Incorporated/teku/pull/1207)

</details>


<a id="beacon_api-L098"></a>
<details>
<summary><b>beacon_api-L098</b> separate event delivery pool — <i>n/a · low · S · latency</i></summary>

**Idea.** Deliver events to connected API subscribers from a dedicated thread pool with its own queue, isolated from core processing.

**Impact.** Each SSE client is an async tokio task fed by a broadcast channel; producers never wait on consumers, so isolation exists by design.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/events.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/events.rs) tokio broadcast channels per topic
- [`beacon_node/http_api/src/lib.rs:105`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L105) BroadcastStream used per SSE client

**Sources.** [teku#2917](https://github.com/Consensys-Incorporated/teku/pull/2917)

</details>


<a id="beacon_api-L099"></a>
<details>
<summary><b>beacon_api-L099</b> suppress empty-slot head events — <i>implemented · low · S · cpu, bandwidth</i></summary>

**Idea.** Do not emit head update or reorg events when only empty slots changed, as clients using dependent roots do not need them.

**Impact.** Head events fire only when an imported block becomes the head, and reorg events fire only when there is a reorg distance. Empty slots produce no events.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:4593-4690`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4593-L4690)
- [`beacon_node/beacon_chain/src/canonical_head.rs:1227-1270`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1227-L1270)
- [`beacon_node/beacon_chain/src/canonical_head.rs:1570-1588`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1570-L1588)

**Skeptic check.** Verified that Head and HeadV2 are registered in the block-import path when the block becomes the head. The only other head_v2 emission is for a payload-status change on the same root, which is not empty-slot noise. ChainReorg requires reorg_distance. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#3449](https://github.com/Consensys-Incorporated/teku/pull/3449)

</details>


<a id="beacon_api-L100"></a>
<details>
<summary><b>beacon_api-L100</b> slim block event payload — <i>implemented · low · S · bandwidth, cpu</i></summary>

**Idea.** Send only block root and slot in the block SSE event instead of serializing the full signed block, shrinking payload and serialization work per imported block.

**Impact.** The block SSE event carries only slot, root, execution_optimistic and the optional builder_index and block_hash. The full block is never serialized.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5149-5174`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5149-L5174)

**Skeptic check.** Confirmed that SseBlock holds only small fields and is built only when there are block subscribers. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#3752](https://github.com/Consensys-Incorporated/teku/pull/3752)

</details>


<a id="beacon_api-L101"></a>
<details>
<summary><b>beacon_api-L101</b> lazy event serialization — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Skip serializing SSE/event payloads unless at least one client is subscribed to that event topic, so idle nodes do no JSON encoding work per head/block/attestation event.

**Impact.** When nobody subscribes, the node builds no event payloads, and JSON encoding happens only in the subscriber SSE streams.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/events.rs:325-398`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/events.rs#L325-L398)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5149-5150`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5149-L5150)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2290-2297`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2290-L2297)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3652-3654`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3652-L3654)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3676-3678`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3676-L3678)
- [`beacon_node/beacon_chain/src/canonical_head.rs:1574`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1574)
- [`beacon_node/beacon_chain/src/block_verification.rs:1119`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1119)

**Skeptic check.** Nearly every register(EventKind) call site is gated by a has_*_subscribers receiver_count check, including attestations, blobs, columns, head, block and block_gossip. The inclusion-list event (gossip_verified_inclusion_list.rs:282) is not gated, but it does only a cheap broadcast send and no serialization. The earlier evidence holds.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#3767](https://github.com/Consensys-Incorporated/teku/pull/3767)

</details>


<a id="beacon_api-L102"></a>
<details>
<summary><b>beacon_api-L102</b> multithreaded validator API — <i>n/a · low · S · latency, cpu</i></summary>

**Idea.** Allow the validator API handler to run on multiple threads so large validator sets do not queue behind a single thread.

**Impact.** API handlers run on the multithreaded tokio runtime and BeaconProcessor workers, so there is no single-thread bottleneck.

**Best measured result.** Useful at 10k+ validators; default left at 1 thread

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/task_spawner.rs:35-80`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/task_spawner.rs#L35-L80) API work goes to BeaconProcessor / tokio multi-thread runtime
- [`beacon_node/http_api/src/lib.rs:588`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L588) blocking_json_task

**Sources.** [teku#4472](https://github.com/Consensys-Incorporated/teku/pull/4472)

</details>


<a id="beacon_api-L103"></a>
<details>
<summary><b>beacon_api-L103</b> shared serialized event bytes — <i>not · low · S · memory, cpu</i></summary>

**Idea.** Serialize SSE events once into a single byte buffer shared by all subscribers instead of encoding a string to bytes per subscriber.

**Gap in Lighthouse.** Serialize the EventKind once in ServerSentEventHandler::register and broadcast an Arc&lt;str&gt;/Bytes (or Arc&lt;EventKind&gt; plus cached JSON), then build the warp Event from the cached string in the http_api events handler instead of calling json_data per subscriber.

**Impact.** Saves N-1 JSON serializations per event when several SSE subscribers share a topic. Negligible on a typical node with 1-3 subscribers; only matters for heavy topics like attestations or blob/column sidecars with many subscribers.

**Best measured result.** Single byte[] stored and reused for every subscriber

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs:3436-3441`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L3436-L3441) per-subscriber BroadcastStream map calls Event::default().event(..).json_data(data), serializing on every subscriber
- [`beacon_node/beacon_chain/src/events.rs:10-36`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/events.rs#L10-L36) broadcast channels carry typed EventKind&lt;E&gt;, not pre-serialized bytes
- [`beacon_node/beacon_chain/src/events.rs:102`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/events.rs#L102) register() sends the EventKind object

**Sources.** [teku#5492](https://github.com/Consensys-Incorporated/teku/pull/5492)

</details>


<a id="beacon_api-L104"></a>
<details>
<summary><b>beacon_api-L104</b> stream JSON response — <i>not · medium · M · memory</i></summary>

**Idea.** Stream JSON API responses straight into the HTTP output stream instead of building the full body in memory; large responses (validators list is 181MB of JSON) otherwise spike heap.

**Gap in Lighthouse.** Stream large JSON list responses (validators, balances) with an incremental serializer into a chunked body instead of Vec + warp::reply::json.

**Impact.** Removes a transient heap spike of hundreds of MB on full validator-list calls; no effect on normal duty paths.

**Best measured result.** Get state validators is 181Mb of JSON

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/task_spawner.rs:97-104`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/task_spawner.rs#L97-L104) blocking_json_task serialises the whole value with warp::reply::json into one in-memory body
- [`beacon_node/http_api/src/lib.rs:3701`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L3701) warp routes served through axum fallback_service; no streamed body anywhere in http_api or warp_utils (only stream use is SSE events at lib.rs:3480)

**Second check.** Grepped http_api, warp_utils and eth2 for Body::wrap_stream/from_stream/StreamBody/chunked; the only stream is the SSE events endpoint.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [teku#5525](https://github.com/Consensys-Incorporated/teku/pull/5525)

</details>


<a id="beacon_api-L105"></a>
<details>
<summary><b>beacon_api-L105</b> stream SSZ response — <i>not · medium · M · memory</i></summary>

**Idea.** Write SSZ response content incrementally to the output stream rather than materialising the full SSZ bytes first.

**Gap in Lighthouse.** Encode large SSZ responses (debug/beacon/states, finalized state) incrementally to a chunked body instead of as_ssz_bytes.

**Impact.** Saves one state-sized (~250MB+ mainnet) buffer per state download; checkpoint-sync server side only.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs:2180`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L2180) debug state SSZ path calls state.as_ssz_bytes() into a full Vec before building the response
- no streaming body in [`beacon_node/http_api/src`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src) or [`common/warp_utils/src`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/warp_utils/src)

**Second check.** Checked for any SSZ streaming encoder or chunked body in http_api, warp_utils and the response helpers; none.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [teku#5530](https://github.com/Consensys-Incorporated/teku/pull/5530)

</details>


<a id="beacon_api-L106"></a>
<details>
<summary><b>beacon_api-L106</b> reject future-slot state lookup — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Return not-found immediately when a state is requested for a slot beyond the head, avoiding processing empty slots to produce a state.

**Impact.** Slots after the wall clock return 404; slots between head and wall clock resolve to the head state root without slot processing.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:966-969`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L966-L969)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:984-990`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L984-L990)
- [`beacon_node/http_api/src/state_id.rs:126-130`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L126-L130)

**Skeptic check.** Verified the wall-clock check and the head fast path (head slot &lt;= request slot returns head state root), so no empty-slot processing happens. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#5533](https://github.com/Consensys-Incorporated/teku/pull/5533)

</details>


<a id="beacon_api-L107"></a>
<details>
<summary><b>beacon_api-L107</b> stop keepalive on closed SSE client — <i>n/a · low · S · cpu</i></summary>

**Idea.** Stop scheduling SSE keep-alive comments once the client has disconnected, so closed clients do not fill the executor queue and burn CPU on retries.

**Gap in Lighthouse.** Keep-alive is part of the response stream; dropping the stream on disconnect stops it, no executor queue exists.

**Impact.** None; no queued keepalive tasks to leak.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs:3482`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L3482) warp::sse::keep_alive().stream(s)

**Sources.** [teku#5919](https://github.com/Consensys-Incorporated/teku/pull/5919)

</details>


<a id="beacon_api-L108"></a>
<details>
<summary><b>beacon_api-L108</b> threads by cores — <i>n/a · low · S · cpu</i></summary>

**Idea.** Size the validator REST API thread pool as min(10, available cores) rather than a fixed count.

**Gap in Lighthouse.** API runs as tasks on the shared tokio runtime, no dedicated REST thread pool to size.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs:3482`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L3482) warp on tokio runtime

**Sources.** [teku#7433](https://github.com/Consensys-Incorporated/teku/pull/7433)

</details>


<a id="beacon_api-L109"></a>
<details>
<summary><b>beacon_api-L109</b> gzip REST responses — <i>not · medium · S · bandwidth</i></summary>

**Idea.** Enable gzip content encoding on REST responses and request gzip when downloading the initial state, shrinking transfer size.

**Gap in Lighthouse.** Add .layer(CompressionLayer::new()) to the axum_router in http_api serve, and enable reqwest gzip in the eth2 client for checkpoint-sync downloads.

**Impact.** Cuts transfer size of checkpoint-sync state and big JSON responses; bandwidth only, small CPU cost.

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.toml:220 workspace reqwest features have no gzip; Cargo.lock reqwest 0.12.28/0.13.5 entries pull no async-compression
- [`beacon_node/http_api/src/lib.rs:3701-3705`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L3701-L3705) beacon API now wrapped in an axum Router but no CompressionLayer is applied
- [`beacon_node/http_metrics/src/lib.rs:120`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_metrics/src/lib.rs#L120) CompressionLayer only on the metrics server
- [`common/axum_utils/src/lib.rs:7`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/axum_utils/src/lib.rs#L7) CompressionLayer re-export exists

**Second check.** Found the beacon API is now served via axum (lib.rs:3701), so the existing CompressionLayer makes the server side a one-line change, but it is not applied; no crate enables reqwest gzip via feature unification.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [teku#7457](https://github.com/Consensys-Incorporated/teku/pull/7457)

</details>


<a id="beacon_api-L110"></a>
<details>
<summary><b>beacon_api-L110</b> head state for duties — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Compute attester duties from the head state when requested epoch is current or next, avoiding cache misses and state regeneration.

**Impact.** Current/next epoch duties come from the shuffling cache; a miss clones the cached head state instead of loading from disk.

**Best measured result.** JMH showed good speed, no numbers

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/attester_duties.rs:44-50`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L44-L50)
- [`beacon_node/http_api/src/attester_duties.rs:63-80`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L63-L80)
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:350-400`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L350-L400)
- [`beacon_node/http_api/src/attester_duties.rs:90-110`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L90-L110)

**Skeptic check.** Verified cached_attestation_duties uses the head node via with_committee_cache, whose miss path uses cached_head.snapshot.beacon_state when the block is the head; historic path also reuses the head state when suitable. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#7573](https://github.com/Consensys-Incorporated/teku/pull/7573)

</details>


<a id="beacon_api-L111"></a>
<details>
<summary><b>beacon_api-L111</b> root lookup without full load — <i>partial · low · S · cpu, disk, latency</i></summary>

**Idea.** For block-root/state-root API lookups, read the root directly from the index or header when possible instead of loading the full block or state from DB.

**Gap in Lighthouse.** State-root lookup already reads only the hot summary. Block-root lookup by root loads the whole blinded block just for its slot. Change BlockId::root Root arm to take the slot from fork choice or a slot index instead of chain.get_blinded_block.

**Impact.** Saves one blinded block DB read and SSZ decode per lookup by root; minor, API is low traffic.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/block_id.rs:43-130`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L43-L130) BlockId::root; Root arm calls block_exists then get_blinded_block
- [`beacon_node/http_api/src/state_id.rs:23-110`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L23-L110) state root by root uses load_hot_state_summary (no state load)

**Sources.** [teku#7799](https://github.com/Consensys-Incorporated/teku/pull/7799)

</details>


<a id="beacon_api-L112"></a>
<details>
<summary><b>beacon_api-L112</b> header-based deserializer choice — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Pick the deserializer for block-production responses from a response header (blinded flag) instead of parsing the whole JSON body to detect the variant.

**Impact.** Both the SSZ and JSON v3 produce-block clients choose Blinded or Full from the Eth-Execution-Payload-Blinded header, and the VC uses SSZ by default.

**Evidence (Lighthouse @ 928b61e719).**

- [`common/eth2/src/lib.rs:3009-3031`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2/src/lib.rs#L3009-L3031)
- [`common/eth2/src/lib.rs:3076-3105`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2/src/lib.rs#L3076-L3105)
- [`validator_client/validator_services/src/block_service.rs:787-830`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/block_service.rs#L787-L830)
- [`common/eth2/src/beacon_response.rs:76-107`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2/src/beacon_response.rs#L76-L107)

**Skeptic check.** Confirmed that the blinded/full variant is chosen from the response header on both the SSZ and JSON paths. The JSON fallback still parses the body into a serde_json::Value (ForkVersionedResponse::deserialize) to read the fork version. That is a separate double-parse, it applies only on the JSON fallback, and it is not this idea.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#7989](https://github.com/Consensys-Incorporated/teku/pull/7989)

</details>


<a id="beacon_api-L113"></a>
<details>
<summary><b>beacon_api-L113</b> primitive map, single-pass duties — <i>n/a · low · S · cpu, latency</i></summary>

**Idea.** Compute attester duties for a requested validator set by iterating committees once and indexing validators with a primitive-keyed map (no boxed integers) in a single pass, avoiding per-validator committee lookups.

**Gap in Lighthouse.** Java boxing issue; Rust uses unboxed keys and the shuffling cache gives per-validator lookup.

**Impact.** None.

**Best measured result.** benchmark 1225 ops/s -&gt; ~975000 ops/s (later found buggy; benchmark did not produce duties)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/attester_duties.rs:61-80`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L61-L80) cached_attestation_duties via validator_attestation_duties and shuffling cache

**Sources.** [teku#8553](https://github.com/Consensys-Incorporated/teku/pull/8553)

</details>


<a id="beacon_api-L114"></a>
<details>
<summary><b>beacon_api-L114</b> primitive int-keyed map for duties — <i>n/a · low · S · cpu, latency</i></summary>

**Idea.** Generate attester duties with a primitive int-keyed hash map and a single pass over committee assignments instead of boxed maps and repeated lookups; verify the benchmark really produces duties.

**Gap in Lighthouse.** Java boxing optimisation; no equivalent cost in Rust.

**Impact.** None.

**Best measured result.** Int2ObjectOpenHashMap 272.6 ops/s vs 246.0 pre-optimization (20000 validators); ArrayMap variant 7.4 ops/s

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/attester_duties.rs:61-80`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L61-L80) cached_attestation_duties

**Sources.** [teku#8578](https://github.com/Consensys-Incorporated/teku/pull/8578)

</details>


<a id="beacon_api-L115"></a>
<details>
<summary><b>beacon_api-L115</b> on-demand sidecar fetch for blobs — <i>not · medium · L · bandwidth, disk</i></summary>

**Idea.** Let the get-blobs API fetch missing column sidecars from peers on demand and persist them, so nodes without full custody can serve blobs and later calls skip the network.

**Gap in Lighthouse.** When stored columns are below half, request missing columns by root from peers via the network service, persist them, then reconstruct.

**Impact.** Lets non-supernodes serve the blobs API; functionality gain that adds network load.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/block_id.rs:340-470`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L340-L470) blob endpoints read only stored columns then reconstruct
- [`beacon_node/http_api/src/block_id.rs:501-520`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L501-L520) returns 'Insufficient data columns ... run with --supernode or --semi-supernode' instead of fetching from peers
- no DataColumnsByRoot/network sender use in [`beacon_node/http_api/src`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src)

**Second check.** Searched http_api for any by-root network request or sync handle in the blob paths; only local store reads and a semi-supernode hint exist.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [teku#10234](https://github.com/Consensys-Incorporated/teku/pull/10234)

</details>


<a id="beacon_api-L116"></a>
<details>
<summary><b>beacon_api-L116</b> persist light client updates — <i>implemented · low · S · startup</i></summary>

**Idea.** Persist the best light client update per sync committee period (with signature block root) in the hot DB and reload on startup, instead of rebuilding the in-memory update store from scratch.

**Impact.** The best LightClientUpdate for each period is written to the store when it improves and is loaded lazily, so there is no rebuild at startup.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/light_client_server_cache.rs:188-205`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_server_cache.rs#L188-L205)
- [`beacon_node/beacon_chain/src/light_client_server_cache.rs:237-262`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_server_cache.rs#L237-L262)
- [`beacon_node/store/src/hot_cold_store.rs:831-900`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L831-L900)

**Skeptic check.** Verified that store_light_client_update runs when is_better_light_client_update is true, and that get_light_client_update falls back to the store and caches the result. Only the latest finality and optimistic updates are memory-only, and those are per-slot data. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#11337](https://github.com/Consensys-Incorporated/teku/pull/11337)

</details>


<a id="beacon_api-L117"></a>
<details>
<summary><b>beacon_api-L117</b> persist precomputed bootstraps — <i>implemented · low · S · cpu, disk, latency</i></summary>

**Idea.** Build the light client bootstrap once per new finalized checkpoint and store it in the database, serving bootstrap requests from storage instead of rebuilding from a state each time.

**Impact.** Bootstrap is assembled from the persisted sync_committee_branch and sync_committee plus one blinded block read; no state is loaded on either the RPC or the HTTP path.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/light_client_server_cache.rs:396-445`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_server_cache.rs#L396-L445)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:8374`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L8374)
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:990`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L990)
- [`beacon_node/http_api/src/light_client.rs:65`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/light_client.rs#L65)

**Skeptic check.** Verified get_light_client_bootstrap reads only the blinded block, the stored branch and the stored committee; both the req/resp and API paths call it. LH does not store the finished bootstrap object, but the costly part (state load) Teku removed is already absent, so the earlier verdict holds.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#11572](https://github.com/Consensys-Incorporated/teku/pull/11572)

</details>


<a id="beacon_api-L118"></a>
<details>
<summary><b>beacon_api-L118</b> hashset id filter, lazy status — <i>partial · low · S · cpu, latency</i></summary>

**Idea.** In state validators endpoint, use a hash set for id filtering and compute validator status only when a status filter is given.

**Gap in Lighthouse.** Status is part of ValidatorData so lazy status does not apply. The id filter is a HashSet but still scans every validator, hashing a 48-byte pubkey and an index per validator; get_beacon_state_validators could resolve ids to indices once (pubkey cache) and fetch only those.

**Impact.** Queries with a few ids on a 1M+ validator state would go from a full registry scan to a handful of lookups; only matters for API-heavy nodes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/validators.rs:24`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validators.rs#L24) HashSet id filter
- [`beacon_node/http_api/src/validators.rs:43`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validators.rs#L43) builds ValidatorId::PublicKey(validator.pubkey) per validator
- [`beacon_node/http_api/src/validators.rs:49`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validators.rs#L49) status computed for every validator (needed in output anyway)

**Sources.** [grandine@bdeb14e5f](https://github.com/grandinetech/grandine/commit/bdeb14e5f0ac)

</details>


<a id="beacon_api-L119"></a>
<details>
<summary><b>beacon_api-L119</b> serialize state lists without copying — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** For state endpoints returning pending deposits, partial withdrawals and consolidations, serialize the state's list directly to JSON/SSZ through a dyn list trait instead of copying it into a new list type with different limits.

**Impact.** to_owned_list is an Arc tree clone of the state's own list type (no re-typing to different limits); JSON serializes it directly. Only the SSZ branch does data.to_vec() before encoding, a small one-off copy.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/beacon/states.rs:58`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L58)
- [`beacon_node/http_api/src/beacon/states.rs:118`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L118)
- [`beacon_node/http_api/src/beacon/states.rs:298`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L298)

**Skeptic check.** Confirmed the three pending-list endpoints clone the milhouse list structurally and serialize it; the Grandine problem (copy into a list with pre-Gloas limits) does not exist. The SSZ to_vec copy is a minor leftover, not the mechanism in question.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine@93ea53af9](https://github.com/grandinetech/grandine/commit/93ea53af9c65)

</details>


<a id="beacon_api-L120"></a>
<details>
<summary><b>beacon_api-L120</b> pubkey index map lookup — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Resolve validator pubkey to index through the in-memory pubkey index map instead of linearly scanning the validator registry or querying the DB.

**Impact.** Single-pubkey lookups (states/validators/{id}, register_validator) use the chain's global pubkey cache map; duties take indices. sync_committee_rewards and validator_inclusion use the state's pubkey map (may be built once per loaded state). The multi-id validators list endpoint still iterates the registry, covered by the separate L118 idea.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/validator/mod.rs:48-64`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L48-L64)
- [`beacon_node/http_api/src/beacon/states.rs:780`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L780)
- [`beacon_node/http_api/src/validator/mod.rs:741`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L741)
- [`consensus/types/src/state/beacon_state.rs:1105-1111`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1105-L1111)
- [`beacon_node/http_api/src/validators.rs:25-60`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validators.rs#L25-L60)

**Skeptic check.** Verified pubkey_to_validator_index uses chain.validator_index (global map) and state.get_validator_index is a hash-map lookup, not a scan. The full-registry iteration in validators.rs is a filter over the whole list, which belongs to L118, so this idea's verdict holds.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@2992c2051](https://github.com/ChainSafe/lodestar/commit/2992c20515f7)

</details>


<a id="beacon_api-L121"></a>
<details>
<summary><b>beacon_api-L121</b> remove listener on close — <i>n/a · low · S · memory</i></summary>

**Idea.** Remove the event listener when an SSE block stream closes, to avoid leaking listeners and memory per client.

**Gap in Lighthouse.** Rust drops the broadcast receiver stream when the client disconnects; no manual listener removal exists to leak.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs) (SSE via warp; stream dropped on disconnect)

**Sources.** [lodestar@f1ed74632](https://github.com/ChainSafe/lodestar/commit/f1ed746329f1)

</details>


<a id="beacon_api-L122"></a>
<details>
<summary><b>beacon_api-L122</b> parallel db lookups in API — <i>n/a · low · S · latency</i></summary>

**Idea.** In the block headers API, process the candidate block summaries concurrently rather than awaiting each db lookup sequentially.

**Gap in Lighthouse.** Lighthouse API handlers run as blocking tasks with direct DB reads, not awaited sequential promises; the specific pattern is JS-specific.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/block_id.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs) (blocking task per request)

**Sources.** [lodestar@4c824f1ae](https://github.com/ChainSafe/lodestar/commit/4c824f1ae576)

</details>


<a id="beacon_api-L123"></a>
<details>
<summary><b>beacon_api-L123</b> remove wait before publish — <i>implemented · low · S · latency</i></summary>

**Idea.** Do not block publishing a validator-produced block waiting for the slot to start, so publication is not delayed.

**Impact.** publish_block gossips immediately; the only sleep is the test-only block_publishing_delay config.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/publish_blocks.rs:141-260`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L141-L260)
- [`beacon_node/http_api/src/publish_blocks.rs:250-255`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L250-L255)

**Skeptic check.** Searched publish_blocks.rs for sleep/wait/slot_clock: the only sleeps are the test-only block and data column publishing delays; there is no wait-for-slot. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@6f9212749](https://github.com/ChainSafe/lodestar/commit/6f9212749445)

</details>


<a id="beacon_api-L124"></a>
<details>
<summary><b>beacon_api-L124</b> read balance by index — <i>partial · low · S · memory, cpu</i></summary>

**Idea.** When serving a single validator's balance (validators endpoint), read the balance by index from the state instead of copying the whole balances list, avoiding a large per-request allocation.

**Gap in Lighthouse.** validator_balances with ids iterates the entire registry and builds a PublicKey id per validator instead of indexed gets; resolve ids to indices first and balances().get(i) each (get_beacon_state_validator_balances).

**Impact.** Balances-by-id queries on a 1M+ validator state drop from O(N) to O(k); modest for most nodes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/beacon/states.rs:779`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L779) single validator uses state.validators().get(index) and balances().get(index) (indexed, no copy)
- [`beacon_node/http_api/src/validators.rs:86`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validators.rs#L86) validator_balances scans all validators zip balances for any id list

**Sources.** [prysm#13279](https://github.com/OffchainLabs/prysm/pull/13279)

</details>


<a id="beacon_api-L125"></a>
<details>
<summary><b>beacon_api-L125</b> single-entry attestation data cache — <i>partial · low · S · cpu, latency</i></summary>

**Idea.** Keep a one-entry cache of attestation data for the current slot; per-committee-index requests reuse it after a single fork choice lookup, and reject requests for non-current slots.

**Gap in Lighthouse.** No per-slot attestation-data cache: each request re-runs produce_unaggregated_attestation (head snapshot read, a few cheap lookups); a one-entry cache keyed by (slot, head root) in the handler would skip it.

**Impact.** Saves a small amount of work per request when many VCs query attestation data in the same slot; cost already small since it reads cached head.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2026`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2026) early_attester_cache.try_attest (only for block mid-import)
- [`beacon_node/http_api/src/validator/mod.rs:294`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L294) calls produce_unaggregated_attestation(slot,0) per request, slot tolerance check at :283

**Sources.** [prysm#13300](https://github.com/OffchainLabs/prysm/pull/13300)

</details>


