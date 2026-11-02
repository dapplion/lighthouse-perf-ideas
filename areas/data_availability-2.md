# data_availability (part 2 of 2)

175 ideas: 27 not, 35 partial, 81 implemented, 32 n/a; 30 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

Pages: [part 1](data_availability.md) · [part 2](data_availability-2.md)

<a id="data_availability-152"></a>
<details>
<summary><b>data_availability-152</b> Store blobs Snappy-compressed as on the wire — <i>not · low · S · disk, cpu</i></summary>

**Idea.** Store blob sidecars on disk Snappy-compressed in the wire encoding, so no re-encoding is needed and storage is smaller.

**Gap in Lighthouse.** Compress the SSZ bytes in put_blobs/blobs_as_kv_store_ops (zstd via StoreConfig::compress_bytes, or snappy) and decompress in get_blobs; needs a schema/format marker or migration for existing uncompressed entries. Alternatively enable leveldb Snappy compression on the blobs DB. Storing in wire (ssz_snappy) format would only save re-encoding for RPC serving, which is minor since Lighthouse serves from the in-memory SSZ.

**Impact.** Blob DB disk footprint shrinks (rollup blobs often compress; zero top bytes of each field element give at least a few percent); modest CPU added per write/read. No meaningful hot-path gain; low value.

**Best measured result.** 38 GB on sepolia (pr:caplin#9500)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L931) put_blobs writes blobs.as_ssz_bytes() raw to blobs_db, no compression
- [`beacon_node/store/src/hot_cold_store.rs:943`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L943) blobs_as_kv_store_ops also raw SSZ
- [`beacon_node/store/src/database/leveldb_impl.rs:37`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/leveldb_impl.rs#L37) Options::new() with no compression set; leveldb-0.8.6 options.rs:72 defaults to Compression::No
- [`beacon_node/store/src/config.rs:198`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L198) compress_bytes (zstd) exists but is used for blocks/state diffs, not BeaconBlob

**Sources.** [caplin#9500](https://github.com/erigontech/erigon/pull/9500)

</details>


<a id="data_availability-153"></a>
<details>
<summary><b>data_availability-153</b> Sort custody groups once — <i>n/a · low · cpu</i></summary>

**Idea.** Sort the custody group list once after the selection loop instead of in each iteration.

**Impact.** LH does not sort inside the selection loop at all.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/data/data_column_custody_group.rs:51`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/data/data_column_custody_group.rs#L51) get_custody_groups_ordered has no sort in the loop; get_custody_groups collects into a HashSet

**Sources.** [prysm#15524](https://github.com/OffchainLabs/prysm/pull/15524)

</details>


<a id="data_availability-154"></a>
<details>
<summary><b>data_availability-154</b> Staged blob reconstruction: concatenate first — <i>partial · medium · S · cpu, bandwidth</i></summary>

**Idea.** Rebuild blobs first by concatenating the original first-half columns without KZG, then recover from any half by erasure coding, and only then use the network.

**Gap in Lighthouse.** In reconstruct_blobs_with_indices, if columns 0..NUMBER_OF_COLUMNS/2 are all present, concatenate their cells directly. Otherwise recover only the polynomial and evaluate the cells, with no FK20 proof computation, because only blob bytes are needed. The network fallback stage does not apply to this API path.

**Impact.** Blob sidecar and blobs API serving from columns would skip RS recovery and FK20 proof generation per blob when the first half is stored. This is tens of ms per blob for supernodes and semi-supernodes that serve blob endpoints.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/kzg_utils.rs:797-815`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L797-L815) reconstruct_blobs_with_indices concatenates cells only when all 128 columns are present, otherwise it calls recover_cells_and_compute_kzg_proofs
- [`beacon_node/http_api/src/block_id.rs:501-533`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L501-L533) get_data_columns_for_blob_reconstruction passes every stored column, with no first-half check
- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/rust_eth_kzg-0.9.1/src/recovery.rs:22-66 recover_polynomial_coeff always runs the RS erasure recovery, with no fast path when there are no erasures in the first half
- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/rust_eth_kzg-0.9.1/src/prover.rs:156-171 recovery always also computes all 128 multi-opening proofs (FK20), which blob serving discards

**Second check.** I also checked the rust_eth_kzg 0.9.1 recovery and the http_api column loader for a hidden fast path. There is none, and recovery always computes proofs too, which makes the cost worse than the earlier review said.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [teku#10274](https://github.com/Consensys-Incorporated/teku/pull/10274)

</details>


<a id="data_availability-155"></a>
<details>
<summary><b>data_availability-155</b> Smaller pending-components cache capacity — <i>implemented · medium · S · memory</i></summary>

**Idea.** Use a small capacity for the pending-components DA cache because each entry grows with blob count and few are needed.

**Impact.** Bounds the pending-components cache memory at about 0.4 GB worst case.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker.rs:42-53`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L42-L53) OVERFLOW_LRU_CAPACITY = 32, sized for 48 blobs at about 0.4 GB

**Skeptic check.** Confirmed the capacity is 32 and the doc comment sizes it for blob count. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#7825](https://github.com/sigp/lighthouse/pull/7825)

</details>


<a id="data_availability-156"></a>
<details>
<summary><b>data_availability-156</b> Persist only custody columns — <i>implemented · medium · S · disk</i></summary>

**Idea.** Persist only the columns the node must custody, not extra sampled or reconstructed columns, to cut DB writes and storage.

**Impact.** Non-supernodes do not write the extra sampled or reconstructed columns.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:8407-8421`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L8407-L8421) get_blobs_or_columns_store_op retains only custody_columns_for_epoch unless supernode
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4744`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4744) block import uses it
- [`beacon_node/beacon_chain/src/historical_blocks.rs:217`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_blocks.rs#L217) backfill uses it
- [`beacon_node/beacon_chain/src/historical_blocks.rs:278`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_blocks.rs#L278) Gloas envelope columns in backfill use it
- [`beacon_node/beacon_chain/src/payload_envelope_verification/import.rs:295`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/import.rs#L295) Gloas envelope import uses it

**Skeptic check.** Confirmed that every PutDataColumns write path (forward import, envelope import, backfill) goes through the custody filter. Custody backfill writes only the columns it requested.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#8188](https://github.com/sigp/lighthouse/pull/8188), [prysm#14083](https://github.com/OffchainLabs/prysm/pull/14083)

</details>


<a id="data_availability-157"></a>
<details>
<summary><b>data_availability-157</b> Keep only sampling columns in fork choice store — <i>n/a · low · memory</i></summary>

**Idea.** Hold only the node's sampling columns in the in-memory fork choice store instead of all columns.

**Impact.** LH fork choice store holds no columns; the DA checker holds only custody/sampling columns already.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fork_choice/src/fork_choice.rs:707`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L707) on_block takes only status, no column storage
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:312`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L312) columns live in DA checker

**Sources.** [grandine#344](https://github.com/grandinetech/grandine/pull/344)

</details>


<a id="data_availability-158"></a>
<details>
<summary><b>data_availability-158</b> Minimum custody until synced — <i>partial · low · M · sync, bandwidth, disk</i></summary>

**Idea.** Custody only the minimum column count until the node has been synced for a while, then grow to the balance-based count.

**Gap in Lighthouse.** Lighthouse already syncs the historical backlog at minimum custody and defers column backfill until synced, because CGC changes are keyed to the wall-clock epoch. What is missing: (1) no sync-state input, so gossip subnets and the ENR go to full CGC during sync, and epochs after registration that are still being range-synced need full CGC; (2) a persisted high CGC (restart after downtime) is never reduced to the minimum while catching up; (3) there is no stability period. Adding a sync-status gate in CustodyContext::register_validators and in the CustodyCountChanged subscription would close it.

**Impact.** Smaller than the earlier estimate: the large part of the benefit (backlog columns at minimum custody during fresh checkpoint sync) already exists. What is left helps mostly a validator node that restarts after long downtime (catch-up range sync at full CGC) and cuts gossip column load during sync.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/custody_context.rs:120-135`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L120-L135) a CGC increase takes effect only from wall-clock (current_slot + delay).epoch + 1, so older epochs keep the old (minimum) CGC
- [`beacon_node/beacon_chain/src/custody_context.rs:468-511`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L468-L511) custody_group_count_at_epoch / sampling_columns_for_epoch fall back to custody_requirement for epochs before the first increase
- [`beacon_node/network/src/sync/network_context.rs:984-991`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L984-L991) range sync fetches columns with sampling_columns_for_epoch(block_epoch), so the sync backlog is downloaded at minimum custody
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:360-370`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L360-L370) RPC columns are filtered to the epoch's sampling columns
- [`beacon_node/network/src/sync/manager.rs:683-733`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L683-L733) custody (column) backfill for the higher CGC starts only once SyncState::Synced and block backfill is complete
- [`beacon_node/network/src/sync/manager.rs:738-757`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L738-L757) custody backfill is paused while range sync runs
- [`beacon_node/network/src/service.rs:786-795`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L786-L795) gossip column subnets and ENR CGC are raised at once, not deferred until synced

**Verdict history.** not (checked) → partial (refuted)

**Sources.** [nimbus#8205](https://github.com/status-im/nimbus-eth2/pull/8205), [teku#10240](https://github.com/Consensys-Incorporated/teku/pull/10240)

</details>


<a id="data_availability-159"></a>
<details>
<summary><b>data_availability-159</b> Synthesize empty sidecar lists, do not store them — <i>implemented · low · S · disk</i></summary>

**Idea.** For blocks without KZG commitments, return an empty sidecar list on lookup instead of storing empty entries.

**Impact.** Saves a tiny write per blob-less block on both forward import and backfill.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:8398`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L8398) get_blobs_or_columns_store_op NoData =&gt; None
- [`beacon_node/beacon_chain/src/historical_blocks.rs:211`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_blocks.rs#L211) backfill skips store op for NoData
- [`beacon_node/store/src/hot_cold_store.rs:2649`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2649) get_blobs returns NoBlobs/NoRoot

**Skeptic check.** Verified both import and backfill paths skip writes for NoData and lookups synthesize the empty result. Earlier verdict upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@01ac7ad23](https://github.com/sigp/lighthouse/commit/01ac7ad23c36)

</details>


<a id="data_availability-160"></a>
<details>
<summary><b>data_availability-160</b> Unified blob availability cache for all paths — <i>partial · low · M · memory, latency</i></summary>

**Idea.** Use one in-memory cache plus persistence layer for blob availability checks shared by gossip, initial sync and backfill.

**Gap in Lighthouse.** Gossip and range/lookup share the DA overflow cache, but backfilled columns bypass it and the store keeps its own cache; unifying them would need routing historical imports through the checker.

**Impact.** Little: cache duplication is small, no clear CPU or disk gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs): shared pending cache used by gossip and RPC
- [`beacon_node/beacon_chain/src/historical_data_columns.rs:121`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_data_columns.rs#L121) historical columns written straight to the store, bypassing the cache
- [`beacon_node/store/src/hot_cold_store.rs:124`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L124) separate store block cache

**Sources.** [prysm#13122](https://github.com/OffchainLabs/prysm/pull/13122)

</details>


<a id="data_availability-161"></a>
<details>
<summary><b>data_availability-161</b> Use EL blobs until block data is imported — <i>not · medium · S · bandwidth, latency</i></summary>

**Idea.** Keep the EL getBlobs response while the block's data (including Gloas payload) is not yet imported, instead of discarding it once the block is in fork choice.

**Gap in Lighthouse.** Replace the two fork_choice_contains_block checks in fetch_blobs/mod.rs with BeaconChain::is_block_data_imported through the adapter, and handle the duplicate payload import after a late merge (PR lighthouse#10488 is still open).

**Impact.** Gloas only: keeps the EL getBlobs response when the block is imported before its payload, which avoids fetching cells from peers. No effect on Fulu.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:272-279`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L272-L279) (V2/V3) and :485-491 (V4) return early on fork_choice_contains_block
- [`beacon_node/beacon_chain/src/fetch_blobs/fetch_blobs_beacon_adapter.rs:146-151`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/fetch_blobs_beacon_adapter.rs#L146-L151) fork_choice_contains_block is plain contains_block and does not check payload_received
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3898-3916`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3898-L3916) is_block_data_imported (Gloas payload_received aware) exists and is used only by gossip/RPC column paths (3463, 3508, 3592, 3715, 3798), not by fetch_blobs

**Verdict history.** not (checked) → not (refuted)

**Sources.** [lighthouse#10488](https://github.com/sigp/lighthouse/pull/10488)

</details>


<a id="data_availability-162"></a>
<details>
<summary><b>data_availability-162</b> Verify availability-critical columns first — <i>not · medium · S · latency</i></summary>

**Idea.** Split KZG batch verification so the sidecars that make the block available are verified first and the remaining columns in a second batch.

**Gap in Lighthouse.** In put_rpc_custody_columns, filter to sampling columns before KZG verification, then split into the columns that complete availability and the remainder. Verify and import the first group, then verify the rest in a second call.

**Impact.** Small: saves a few ms of latency on RPC/lookup paths only. Gossip already verifies per column. Filtering before verification also saves verification work that is thrown away.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker.rs:356-372`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L356-L372) put_rpc_custody_columns KZG-verifies the whole batch first and filters it to sampling columns only after that (extra columns are verified too)
- [`beacon_node/beacon_chain/src/data_column_verification.rs:507-519`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L507-L519) from_batch_with_scoring does one verify_kzg_for_data_column_list call over all columns
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:495-530`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L495-L530) range-sync batch verification is also a single batch over all blocks

**Verdict history.** not (checked) → not (refuted)

**Sources.** [silver#239](https://github.com/gattaca-com/silver/pull/239)

</details>


<a id="data_availability-163"></a>
<details>
<summary><b>data_availability-163</b> Verify sidecars before persisting — <i>implemented · medium · S · disk</i></summary>

**Idea.** During sync and backfill, verify sidecar KZG commitments before writing them, and store columns only after block viability is known.

**Impact.** Invalid sidecars are never written during range sync, backfill or custody backfill. Gossip columns stay in the DA cache until block import.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:670-690`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L670-L690) process_backfill_blocks runs batch_verify_kzg_for_range_sync_blocks before import_historical_block_batch
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:495-520`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L495-L520) batch_verify_kzg_for_range_sync_blocks covers blobs, Fulu columns and Gloas envelope columns
- [`beacon_node/beacon_chain/src/historical_data_columns.rs:182-205`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_data_columns.rs#L182-L205) custody backfill verifies KZG before blobs_db.do_atomically
- [`beacon_node/beacon_chain/src/beacon_chain.rs:8391`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L8391) columns are written only in the block import batch, after block validation

**Skeptic check.** Confirmed that KZG verification comes before every DB write on backfill and custody backfill. In forward sync, columns are persisted only in the import batch of a fully validated block. Fulu columns are verified per block, not in one cross-block batch, but this does not affect the idea.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#13060](https://github.com/OffchainLabs/prysm/pull/13060), [nimbus#7386](https://github.com/status-im/nimbus-eth2/pull/7386)

</details>


<a id="data_availability-164"></a>
<details>
<summary><b>data_availability-164</b> Start EL blob lookup immediately near deadline — <i>implemented · low · S · latency</i></summary>

**Idea.** Start the getBlobs lookup immediately when a block arrives near the attestation deadline instead of after a minimum delay (reverted for too many RPC requests).

**Impact.** getBlobs already starts immediately on block/header arrival; no minimum delay exists in fetch_blobs.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/mod.rs:1020`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L1020) fetch_and_process_engine_blobs called directly
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1127`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1127) getBlobs triggered immediately after header verification, no delay

**Skeptic check.** No sleep or delay found in fetch_blobs or the gossip trigger; the call starts as soon as the header is verified. Earlier verdict upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#8864](https://github.com/Consensys-Incorporated/teku/pull/8864)

</details>


<a id="data_availability-165"></a>
<details>
<summary><b>data_availability-165</b> Fetch EL blobs when payload envelope awaits blobs — <i>implemented · medium · S · latency, bandwidth</i></summary>

**Idea.** When a payload envelope arrives before its blob data is available, call engine_getBlobs, build the missing column sidecars into the quarantine and re-enqueue the pending envelope. Availability is met locally without waiting for gossip columns.

**Impact.** getBlobs runs on Gloas block receipt (gossip, RPC, HTTP) from the bid's commitments, and the EL-built columns complete the pending envelope's availability without waiting for gossip columns. There is no second getBlobs attempt when the envelope arrives (process_gossip_verified_execution_payload_envelope), but nimbus#8498 also fires at block time, so this matches the source.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1925-1941`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1925-L1941) Gloas gossip block inserted into pending_payload_cache then spawn_fetch_block_columns
- [`beacon_node/network/src/network_beacon_processor/mod.rs:960-995`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L960-L995) spawn_fetch_block_columns -&gt; fetch_engine_blobs_and_publish_full
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:369-392`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L369-L392) Bid path merges EL columns into pending_payload_cache, publishes, calls process_payload_envelope_availability
- [`beacon_node/network/src/service.rs:689-700`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L689-L700) HTTP-published blocks also trigger the fetch
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:209-224`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L209-L224) RPC lookup block with MissingComponents also calls getBlobs

**Skeptic check.** Read the nimbus#8498 diff: it calls getBlobs on the Gloas block and puts the columns in the gloas quarantine, the same thing Lighthouse does at gossip_methods.rs:1936 with fetch_blobs/mod.rs:369-392. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine#569](https://github.com/grandinetech/grandine/pull/569), [nimbus#8498](https://github.com/status-im/nimbus-eth2/pull/8498)

</details>


<a id="data_availability-166"></a>
<details>
<summary><b>data_availability-166</b> Refresh quarantine LRU position on sidecar request — <i>not · low · S · memory, latency</i></summary>

**Idea.** In the sidecar quarantine, move an entry to the front of the LRU on request (pop) as well as on insert. Blocks still being assembled are not evicted before completion.

**Gap in Lighthouse.** Lighthouse could take a write lock and use get() in the by-root request paths (get_data_columns, peek_data_columns) to refresh LRU position; it chose read-lock peeks. Eviction needs &gt;32 concurrent roots.

**Impact.** Only matters under extreme churn (&gt;32 roots in flight); negligible on mainnet.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/pending_payload_cache/mod.rs:612-617`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/mod.rs#L612-L617) peek_pending_components uses LruCache::peek, no promotion
- [`beacon_node/beacon_chain/src/pending_payload_cache/mod.rs:55`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/mod.rs#L55) capacity 32
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:396-434`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L396-L434) peek_blob/peek_data_columns/peek_pending_components use peek under a read lock

**Sources.** [nimbus@4d745a671](https://github.com/status-im/nimbus-eth2/commit/4d745a671bee)

</details>


<a id="data_availability-167"></a>
<details>
<summary><b>data_availability-167</b> Defer payload envelope signature checks in bounded queue — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Keep unvalidated gossip envelopes in a small bounded queue per (block root, builder) keyed by signature, and verify signatures only when the block arrives, preferring trusted-source envelopes. This avoids verifying envelopes that are never used.

**Impact.** Envelope BLS checks are deferred until the block is known, and the queue is bounded. The queue holds one envelope per block root with first-wins, not one per (root, builder, signature), and it does not prefer trusted sources. That is a robustness difference, not extra signature work.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/payload_envelope_verification/gossip_verified_envelope.rs:164-168`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/gossip_verified_envelope.rs#L164-L168) BlockRootUnknown returned before any signature work
- [`beacon_node/beacon_chain/src/payload_envelope_verification/gossip_verified_envelope.rs:173-186`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/gossip_verified_envelope.rs#L173-L186) observed-envelope dedupe before signature verify
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:3893-3965`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L3893-L3965) unknown-block envelope queued unverified; verified only when the block is imported
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:763-799`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L763-L799) bounded queue (MAXIMUM_QUEUED_ENVELOPES=16), one per block root, timeout

**Skeptic check.** Confirmed the deferral and the bounded queue. The earlier evidence was correct. The TODO at work_reprocessing_queue.rs:767 notes that a first-arriving garbage envelope can occupy the root's single slot.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#9317](https://github.com/status-im/nimbus-eth2/pull/9317)

</details>


<a id="data_availability-168"></a>
<details>
<summary><b>data_availability-168</b> Check in-memory column status before DB block read — <i>implemented · low · S · disk, latency</i></summary>

**Idea.** When answering whether blob data is available for a block, check the in-memory column availability status first and read the block from the database only if no columns are stored. The common case avoids a DB read.

**Impact.** The PTC blob_data_available answer comes only from memory and never reads a block from the DB, so the cost prysm#17222 removed does not exist here.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2254-2259`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2254-L2259) payload attestation data takes blob_data_available from pending_payload_cache
- [`beacon_node/beacon_chain/src/pending_payload_cache/mod.rs:149-162`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/mod.rs#L149-L162) is_blob_data_available peeks in-memory pending components only
- [`beacon_node/beacon_chain/src/pending_payload_cache/pending_components.rs:216-220`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/pending_components.rs#L216-L220) compares cached column count to the custody requirement

**Skeptic check.** Verified that the path makes no store access. The earlier evidence was right. A possible correctness concern, outside this perf scope: the function returns false once the entry has left the pending cache.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#17222](https://github.com/OffchainLabs/prysm/pull/17222)

</details>


<a id="data_availability-169"></a>
<details>
<summary><b>data_availability-169</b> Drop KZG commitments from data column sidecars — <i>implemented · low · S · bandwidth, disk</i></summary>

**Idea.** Do not carry KZG commitments in every column sidecar when they are in the block or builder bid; take them from there. Sidecars are smaller to gossip, serve and store.

**Impact.** Gloas sidecars carry no commitments, header or inclusion proof. Fulu keeps them because the spec requires it.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/data/data_column_sidecar.rs:94-97`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/data/data_column_sidecar.rs#L94-L97) kzg_commitments is only(Fulu); Gloas commitments come from the bid
- [`beacon_node/beacon_chain/src/data_column_verification.rs:407-418`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L407-L418) Gloas gossip verification takes the commitment count from load_gloas_payload_bid

**Skeptic check.** This is Lighthouse's own PR #8739, and it is present in the type definition and the verification path. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#16309](https://github.com/OffchainLabs/prysm/pull/16309), [lighthouse#8739](https://github.com/sigp/lighthouse/pull/8739)

</details>


<a id="data_availability-170"></a>
<details>
<summary><b>data_availability-170</b> Do not backfill columns when custody increases — <i>not · low · M · bandwidth, sync</i></summary>

**Idea.** When validator custody count increases, custody only new columns going forward and advance the earliest-available slot instead of requesting historical columns by root. This removes periodic refill requests.

**Gap in Lighthouse.** Lighthouse would have to drop CustodyBackFillSync (start/include_next_batch/send_batch) and, when the custody group count rises, set earliest_data_column_slot to the current epoch start instead of downloading older columns. Needs a decision that serving fewer historical columns is acceptable.

**Impact.** Only nodes whose validator custody grows (validators attached, balance increases) download the columns of up to ~18 days of history, one time. Dropping it saves that bandwidth and DB writes, but those nodes then serve less history.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/custody_backfill_sync/mod.rs:130-330`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/custody_backfill_sync/mod.rs#L130-L330) full custody backfill sync state machine requests historical columns by range when custody grows
- [`beacon_node/store/src/metadata.rs:215-221`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/metadata.rs#L215-L221) earliest_data_column_slot tracks backfill progress
- [`beacon_node/network/src/status.rs:36`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/status.rs#L36) advertises earliest_data_column_slot in Status

**Sources.** [nimbus#7601](https://github.com/status-im/nimbus-eth2/pull/7601)

</details>


<a id="data_availability-171"></a>
<details>
<summary><b>data_availability-171</b> Publish proposer column sidecars before payload envelope — <i>not · low · S · latency</i></summary>

**Idea.** At proposal time compute and broadcast data column sidecars before the execution payload envelope is published. Receivers have the columns for their availability check when the envelope arrives.

**Gap in Lighthouse.** In publish_execution_payload_envelope, await column_build_future and call publish_column_sidecars before publish_fn broadcasts the envelope (or at least at the same time). Trade-off with idea 172: publishing columns before validation.

**Impact.** Peers would hold the columns when the envelope arrives, so payload availability could complete sooner. Only affects self-built or API-submitted payloads (proposers), a latency gain of the KZG column build time, not CPU.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/beacon/execution_payload_envelopes.rs:228-246`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/execution_payload_envelopes.rs#L228-L246) column build is spawned in parallel with envelope gossip
- [`beacon_node/http_api/src/beacon/execution_payload_envelopes.rs:376-396`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/execution_payload_envelopes.rs#L376-L396) columns are published only after the envelope is published and imported
- [`beacon_node/http_api/src/publish_blocks.rs:168-172`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L168-L172) Gloas block publish does not publish columns

**Sources.** [prysm#16618](https://github.com/OffchainLabs/prysm/pull/16618)

</details>


<a id="data_availability-172"></a>
<details>
<summary><b>data_availability-172</b> Proposer publishes sidecars only when responsible — <i>implemented · low · S · bandwidth, cpu</i></summary>

**Idea.** Publish data column sidecars from the proposer only when it self-builds the payload, and on the envelope publish API only after the envelope passes validation. Invalid or builder-owned payloads do not cause sidecar gossip.

**Impact.** Invalid envelopes never cause column gossip. Self-built columns are published once, from the envelope endpoint. Builder payloads go through the normal getBlobs path that every node runs.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/beacon/execution_payload_envelopes.rs:262-271`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/execution_payload_envelopes.rs#L262-L271) envelope gossip-verified first; errors return before any publish
- [`beacon_node/http_api/src/beacon/execution_payload_envelopes.rs:342-362`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/execution_payload_envelopes.rs#L342-L362) import errors return before columns are published
- [`beacon_node/http_api/src/beacon/execution_payload_envelopes.rs:368-376`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/execution_payload_envelopes.rs#L368-L376) publish_and_import_columns only after successful envelope processing
- [`beacon_node/http_api/src/publish_blocks.rs:168-172`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L168-L172) self-built payload skips the EL fetch at block publish; columns come only from the envelope endpoint

**Skeptic check.** Verified the ordering: verify, then import, then publish columns. The column build is spawned early in parallel but is published only on success. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine#818](https://github.com/grandinetech/grandine/pull/818), [grandine#754](https://github.com/grandinetech/grandine/pull/754)

</details>


<a id="data_availability-173"></a>
<details>
<summary><b>data_availability-173</b> Per-type block data availability state machines — <i>n/a · low · S · cpu</i></summary>

**Idea.** Model block data-availability tracking as separate per-type structures (pre-DA, blobs, columns) so each does only the work its type needs and objects have a stable shape. This helps runtime optimization.

**Impact.** The Lodestar change is about stable object shapes for the V8 JIT (monomorphic classes); Rust enums and separate types are already static, so there is no runtime gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker.rs:764-775`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L764-L775) AvailableBlockData enum with Blobs and DataColumns variants
- [`beacon_node/beacon_chain/src/pending_payload_cache/pending_components.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/pending_components.rs) separate Gloas pending-components type

**Sources.** [lodestar#7745](https://github.com/ChainSafe/lodestar/pull/7745)

</details>


<a id="data_availability-174"></a>
<details>
<summary><b>data_availability-174</b> One getBlobs attempt per slot, not per column gossip — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Trigger the EL getBlobs call once at slot start for the latest sidecarless block instead of on every incoming column gossip message. This avoids repeated EL calls and work.

**Impact.** There are at most about two getBlobs calls per block (block arrival plus the first new partial header), never one per column message.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1936`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1936) getBlobs once per gossip block
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1119-1133`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1119-L1133) partial-header path calls getBlobs only when !header.was_cached()
- [`beacon_node/network/src/network_beacon_processor/mod.rs:960-995`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L960-L995) spawn_fetch_block_columns; full-column gossip handlers never call it

**Skeptic check.** Grepped every trigger site: gossip block, first partial header, RPC lookup and HTTP publish. None of them is on the per-column gossip path. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#7480](https://github.com/status-im/nimbus-eth2/pull/7480)

</details>


<a id="data_availability-175"></a>
<details>
<summary><b>data_availability-175</b> Skip custody increase detection without validators — <i>implemented · low · S · bandwidth, disk</i></summary>

**Idea.** Skip end-of-epoch validator custody detection and any column custody increase when no validators are attached. Non-validating nodes do not raise custody or download extra columns.

**Impact.** There is no end-of-epoch custody scan. A node without validators stays at the minimum custody and never raises it.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/custody_context.rs:401-445`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L401-L445) register_validators raises custody only on VC registration
- [`beacon_node/beacon_chain/src/custody_context.rs:450-459`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L450-L459) no validators -&gt; spec.custody_requirement
- [`beacon_node/http_api/src/validator/mod.rs:1104`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L1104) only non-test caller is the validator HTTP endpoint

**Skeptic check.** Confirmed that the only production caller of register_validators is the validator API. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#7606](https://github.com/status-im/nimbus-eth2/pull/7606)

</details>


