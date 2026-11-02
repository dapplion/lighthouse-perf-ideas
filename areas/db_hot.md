# db_hot

69 checked ideas, 18 actionable. [Back to the summary](../README.md).

## Actionable (18)

High or medium value, verdict `not` or `partial`.

<a id="db_hot-082"></a>
<details>
<summary><b>db_hot-082</b> Retention pruning during finality stalls — <i>partial · high · M · memory, disk</i></summary>

**Idea.** When finalization does not advance, still prune states, blocks and attestation tables older than max(finalized, head - window) on head updates, protecting head/justified/finalized and evicting orphans whose parents never arrive, so storage does not grow without bound.

**Gap in Lighthouse.** Lighthouse has an operator-triggered equivalent (POST /lighthouse/finalize) that migrates and prunes the hot DB at a chosen unfinalized checkpoint during a stall, but nothing automatic: no head-driven retention window that prunes old hot states/blocks while finality is stuck. Blob pruning is also capped by the split, so it stalls too. Missing: an automatic head-window prune in migrate.rs that keeps head/justified/finalized and fork-choice nodes.

**Impact.** Bounds hot DB growth in long non-finality without operator help; hdiff storage and the manual endpoint already reduce the need.

**Best measured result.** Estimated 10,800 states x 100+ MB after 12h without finalization; closed unmerged (pr:ethlambda#175)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs:2860`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L2860) POST lighthouse/finalize manual finalization endpoint
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1837`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1837) manually_finalize_state sends ManualFinalizationNotification
- [`beacon_node/beacon_chain/src/migrate.rs:292`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L292) run_manual_migration runs full run_migration/prune_hot_db at an unfinalized checkpoint
- [`beacon_node/store/src/hot_cold_store.rs:3307`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3307) blob pruning also capped by split slot
- [`beacon_node/beacon_chain/src/migrate.rs:310`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L310) automatic migration only on finalization

**Second check.** Beyond the earlier review I found the manual finalization HTTP endpoint and its migrator path, which prune the hot DB during non-finality when an operator calls them. I also checked that blob pruning is bounded by the split slot.

**Sources.** [ethlambda#179](https://github.com/lambdaclass/ethlambda/pull/179), [ethlambda#176](https://github.com/lambdaclass/ethlambda/pull/176), [ethlambda#175](https://github.com/lambdaclass/ethlambda/pull/175)

</details>

<a id="db_hot-027"></a>
<details>
<summary><b>db_hot-027</b> Tune KV store write buffer and flush settings — <i>not · medium · S · memory, disk</i></summary>

**Idea.** Set an explicit, bounded write buffer/memtable size (for example 128 MB) and tune bytes_per_sync, background flush jobs and block size per DB size and CPU count. This bounds memory and smooths write I/O, avoiding disk spikes during sync.

**Gap in Lighthouse.** Set write_buffer_size (and optionally block_size/cache/max_open_files) on leveldb Options in LevelDB::open behind a config flag; the leveldb 0.8.6 crate already exposes these fields, so no crate change is needed.

**Impact.** Bounded/larger memtable may smooth write I/O during sync; LevelDB default is 4MB so the effect is uncertain and needs measuring.

**Best measured result.** 256MB buffer caused &gt;1GB disk spikes; 128MB avoids spike, a couple of flushes per minute (pr:teku#2239)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/database/leveldb_impl.rs:36-41`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/leveldb_impl.rs#L36-L41) LevelDB::open sets only create_if_missing
- ~/.cargo/registry/src/*/leveldb-0.8.6/src/database/options.rs:38-58 crate already exposes write_buffer_size, block_size, max_open_files, cache (unused by Lighthouse)
- [`beacon_node/store/src/database/redb_impl.rs:28-35`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/redb_impl.rs#L28-L35) redb::Database::create with defaults, no cache size set

**Second check.** Checked the leveldb 0.8.6 crate Options and redb open path; tuning knobs exist but Lighthouse sets none. Corrected the earlier gap: no need to expose crate fields.

**Sources.** [teku#2248](https://github.com/Consensys-Incorporated/teku/pull/2248), [teku#2225](https://github.com/Consensys-Incorporated/teku/pull/2225), [teku#2222](https://github.com/Consensys-Incorporated/teku/pull/2222), [teku#2239](https://github.com/Consensys-Incorporated/teku/pull/2239), [teku#6208](https://github.com/Consensys-Incorporated/teku/pull/6208), [teku#2381](https://github.com/Consensys-Incorporated/teku/pull/2381)

</details>

<a id="db_hot-041"></a>
<details>
<summary><b>db_hot-041</b> Persist received bytes without re-serializing — <i>not · medium · M · cpu, memory</i></summary>

**Idea.** Keep the serialized bytes of blocks and data column sidecars received from gossip or req/resp until the async DB write finishes, and write those bytes instead of serializing the decoded object again.

**Gap in Lighthouse.** Carry raw gossip/RPC SSZ bytes with verified blocks/columns and add a StoreOp variant that writes them; blocks are stored blinded so only columns (and blob sidecars) benefit simply.

**Impact.** Avoids one SSZ encode per data column (and a block clone); small CPU saving on import.

**Best measured result.** Fix: cache was always empty at write time, defeating the serialization optimization (pr:lodestar#8907)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1296-1302`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1296-L1302) PutBlock clones block then block_as_kv_store_ops
- [`beacon_node/store/src/hot_cold_store.rs:560`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L560) blinded_block.as_ssz_bytes()
- [`beacon_node/store/src/hot_cold_store.rs:965`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L965) data_column.as_ssz_bytes()

**Second check.** Searched beacon_chain and network for retained raw/ssz bytes; only debug dumps re-encode blocks, nothing keeps received bytes for the DB write.

**Sources.** [lodestar#8627](https://github.com/ChainSafe/lodestar/pull/8627), [lodestar#8907](https://github.com/ChainSafe/lodestar/pull/8907)

</details>

<a id="db_hot-050"></a>
<details>
<summary><b>db_hot-050</b> Disk-backed deposits and immutable validator data — <i>not · medium · L · memory</i></summary>

**Idea.** Store deposits and immutable validator data (pubkeys, pubkey-to-index) in an append-only disk-backed store and read them on demand, instead of holding them all in memory.

**Gap in Lighthouse.** Only pubkeys apply (deposit cache no longer exists). Could drop the in-memory pubkey_bytes Vec or move it to on-demand disk reads; replacing decompressed PublicKey Vec would hurt signature verification.

**Impact.** Frees roughly 100-300 MB RSS on mainnet at the cost of lookup latency; likely not a speed win.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:24-29`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L24-L29) pubkeys, pubkey_bytes and indices all held in memory
- beacon_node (no eth1 crate; no DepositCache anywhere in the tree)

**Second check.** Verified the eth1 deposit cache is gone from the tree, so the deposit half is moot; milhouse structural sharing reduces per-state validator memory but is not disk-backed.

**Sources.** [nimbus@e6320e588](https://github.com/status-im/nimbus-eth2/commit/e6320e588125), [nimbus@ce1fda119](https://github.com/status-im/nimbus-eth2/commit/ce1fda119534)

</details>

<a id="db_hot-065"></a>
<details>
<summary><b>db_hot-065</b> Blob sidecars as files with atomic rename — <i>not · medium · L · disk</i></summary>

**Idea.** Store blob sidecars as individual files written to a temporary file and atomically renamed, instead of in the key-value DB, keeping writes crash-safe without DB overhead.

**Gap in Lighthouse.** There is no file-per-sidecar storage. Blobs and data columns go to a separate KV instance. A filesystem backend with temp-file plus rename would have to sit behind put_blobs/get_blobs/delete and pruning.

**Impact.** Low: blobs are already in their own DB, so this would mostly remove compaction write amplification on that DB.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:275`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L275) blobs_db opened as BeaconNodeBackend (LevelDB/redb)
- [`beacon_node/store/src/database/leveldb_impl.rs:36`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/leveldb_impl.rs#L36) and redb_impl.rs:28 are the only backends

**Second check.** Searched beacon_node and common for fs::rename and tempfile persist use: the only hits are test mocks and account_utils, none in the store. The store has only the leveldb and redb backends.

**Sources.** [prysm#13129](https://github.com/OffchainLabs/prysm/pull/13129)

</details>

<a id="db_hot-072"></a>
<details>
<summary><b>db_hot-072</b> One KV instance for hot and finalized data — <i>not · medium · L · memory, disk, latency</i></summary>

**Idea.** Keep hot and finalized data as column families or tables in one key-value store instance instead of two, so each instance's native caches and buffers are not duplicated and a write that touches both is one atomic transaction.

**Gap in Lighthouse.** Hot, cold and blobs are three separate KV instances, and the redb backend does not share one either. Merging them would need one instance with column prefixes or tables, a datadir migration, and an atomic migrate_database.

**Impact.** A few hundred MB of native cache, and an atomic finalization migration; no CPU gain.

**Best measured result.** "should reduce native memory consumption by ~500Mb" (pr:teku#2934)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:270`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L270) hot_db = BeaconNodeBackend::open(hot_path)
- [`beacon_node/store/src/hot_cold_store.rs:284`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L284) cold_db opened separately at cold_path
- [`beacon_node/store/src/database/redb_impl.rs:30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/redb_impl.rs#L30) each redb backend is its own database file

**Second check.** Checked HotColdDB::open and both backend constructors: every instance is opened on its own path. Neither backend shares a cache or an environment between instances.

**Sources.** [teku#5730](https://github.com/Consensys-Incorporated/teku/pull/5730), [teku#2934](https://github.com/Consensys-Incorporated/teku/pull/2934)

</details>

<a id="db_hot-095"></a>
<details>
<summary><b>db_hot-095</b> Write-back buffer for state summaries — <i>not · medium · S · cpu, disk</i></summary>

**Idea.** Buffer state summaries in memory in the DB layer and flush them in one batch (on a count threshold, or with blocks during initial sync) instead of writing each summary on its own.

**Gap in Lighthouse.** No write-back buffer: each block import (and each skipped-slot state) is its own DB batch. A buffer would batch summaries across blocks during range sync and serve reads from it; LH already avoids Prysm's original problem (separate summary transaction) by writing the summary in the block's own batch.

**Impact.** Small: summaries are ~100 bytes and already share the block's atomic write; saving is fewer write batches during initial sync only.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:4751-4756`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4751-L4756) block, columns and PutState (summary+diff) go in one do_atomically_with_block_and_blobs_cache batch per block
- [`beacon_node/store/src/hot_cold_store.rs:1307`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1307) PutState -&gt; store_hot_state; :1722 store_hot_state_summary pushes one op immediately, no cross-block buffer
- [`beacon_node/beacon_chain/src/block_verification.rs:1630-1633`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1630-L1633) each skipped-slot state written in its own hot_db.do_atomically

**Second check.** Checked the block-import op list and StoreOp::PutState handling: the summary rides in the same batch as the block, which covers the 'with blocks' half of the Prysm idea, but there is no in-memory summary buffer or count-threshold flush anywhere in store/.

**Sources.** [prysm#8101](https://github.com/OffchainLabs/prysm/pull/8101), [prysm#11388](https://github.com/OffchainLabs/prysm/pull/11388)

</details>

<a id="db_hot-098"></a>
<details>
<summary><b>db_hot-098</b> Persist committee caches with stored states — <i>not · medium · M · cpu, latency</i></summary>

**Idea.** Store committee/shuffling caches together with the state in the hot DB so a state loaded from disk does not need a shuffling recompute.

**Gap in Lighthouse.** Committee caches are neither stored with hot snapshots/diffs nor is ShufflingCache persisted; a state loaded from disk rebuilds committees on demand. Would need an extra column keyed by shuffling id or decision root.

**Impact.** Saves one shuffling compute (~100s of ms) after restart or on a state_cache miss; rare on a running node.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3865-3871`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3865-L3871) HotStateSummary: slot, block roots, diff base, previous state root only
- [`beacon_node/store/src`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src)/: no reference to committee_cache or ShufflingCache in the store crate
- [`beacon_node/beacon_chain/src/shuffling_cache.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs): in-memory only

**Second check.** Grepped the whole store crate for committee/shuffling persistence and checked the state cache put path; the only committee data persisted is sync committees for light client, not attester shufflings.

**Sources.** [lighthouse@67fdb4a7f](https://github.com/sigp/lighthouse/commit/67fdb4a7fb42)

</details>

<a id="db_hot-102"></a>
<details>
<summary><b>db_hot-102</b> Persist data columns on arrival, prune cache after — <i>not · medium · M · memory, disk, sync</i></summary>

**Idea.** Write each accepted data column sidecar to disk as soon as it is accepted, and remove it from the in-memory column cache only once persistence is confirmed (with a short retention window). No column is lost to cache pruning and the cache stays bounded.

**Gap in Lighthouse.** Gossip/RPC columns are not written to disk on acceptance; they live in the DA LRU until the block imports, so eviction under load forces refetch. Persisting on arrival needs a hot-DB write in the DA put path plus orphan-column pruning.

**Impact.** Avoids re-download of evicted pending columns; adds disk writes for columns of blocks that may never import; benefit unclear.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:351`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L351) pending columns held only in an in-memory LruCache
- [`beacon_node/beacon_chain/src/beacon_chain.rs:8421`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L8421) StoreOp::PutDataColumns built only at block import
- [`beacon_node/store/src/hot_cold_store.rs:985`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L985) put_data_columns only called from checkpoint-sync builder (builder.rs:583) and historical backfill (historical_data_columns.rs:121)

**Second check.** Enumerated every caller of put_data_columns / data_column_as_kv_store_ops / PutDataColumns: none is on the gossip or RPC acceptance path (the old disk-overflow store of the DA cache is gone).

**Sources.** [grandine@03a65e85e](https://github.com/grandinetech/grandine/commit/03a65e85e5cd), [grandine@c3b25ed8d](https://github.com/grandinetech/grandine/commit/c3b25ed8d112), [grandine@2242cea39](https://github.com/grandinetech/grandine/commit/2242cea393f3)

</details>

<a id="db_hot-149"></a>
<details>
<summary><b>db_hot-149</b> Trust local blocks, skip signature work on load — <i>not · medium · M · startup, cpu, memory</i></summary>

**Idea.** Mark blocks read from the local DB as trusted and skip BLS signature deserialization and checks when loading them; load blocks lazily during state rewinds.

**Gap in Lighthouse.** No trusted/lazy decode for DB blocks: every uncached block load decompresses all G2 signatures. A decoder using SignatureBytes on the DB path would be needed. The LRU block cache mitigates repeated loads but is not the mechanism; startup does not replay blocks, so Nimbus's startup gain does not apply.

**Impact.** Tens of microseconds per signature on uncached block loads (RPC serving, replay, migration); minor on a mainnet node.

**Best measured result.** 50x startup time improvement, 200x block load time improvement (Initialize DB 187709 ms -&gt; 3815 ms; load block 0.558 -&gt; 0.043 ms) (pr:nimbus#1227)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:663-686`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L663-L686) get_blinded_block/get_block_with decode every read with SignedBeaconBlock::from_ssz_bytes
- [`crypto/bls/src/impls/blst.rs:195-197`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L195-L197) Signature deserialize = blst from_bytes (point decompression)
- [`crypto/bls/src/generic_signature.rs:68-74`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/generic_signature.rs#L68-L74) GenericSignature holds a decoded point, no lazy bytes mode
- [`beacon_node/store/src/hot_cold_store.rs:96`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L96),571-597 LRU block_cache only avoids re-decoding recently used full blocks

**Second check.** Checked the BLS GenericSignature wrapper for lazy decoding and the store block cache; neither skips signature decompression on a DB read.

**Sources.** [nimbus#1227](https://github.com/status-im/nimbus-eth2/pull/1227)

</details>

<a id="db_hot-003"></a>
<details>
<summary><b>db_hot-003</b> Spread pruning over slots instead of epoch bursts — <i>partial · medium · M · latency, disk</i></summary>

**Idea.** Prune a small slice (one slot or one epoch leaving the retention window) on each slot tick instead of a large prune at an epoch or period boundary. Cost is spread out and there are no event-loop or import stalls at boundaries.

**Gap in Lighthouse.** Pruning runs in a background thread, one finalized epoch per run on a healthy chain (epochs_per_migration and epochs_per_blob_prune default 1). It is not split per slot. After a finality gap, one run deletes the whole range in one atomic batch. Only the reconstruction step is chunked (BLOCKS_PER_RECONSTRUCTION).

**Impact.** Small on a healthy chain, because work is already per-epoch and off the import path. It helps mainly with the large burst when finality resumes after a stall.

**Best measured result.** "taking 1.1s or more at the epoch boundary"; per-slot queries up to ~50ms (pr:nimbus#8852)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/migrate.rs:32`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L32) DEFAULT_EPOCHS_PER_MIGRATION = 1 (prune each finalized epoch)
- [`beacon_node/store/src/config.rs:30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L30) DEFAULT_EPOCHS_PER_BLOB_PRUNE = 1
- [`beacon_node/beacon_chain/src/migrate.rs:434`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L434) background migrator thread, off the import path
- [`beacon_node/beacon_chain/src/migrate.rs:808`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L808) prune_hot_db deletes all abandoned/finalized items in one atomic batch
- [`beacon_node/beacon_chain/src/canonical_head.rs:1725`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1725) migration and blob prune triggered on finalization update

**Second check.** Checked the migration/blob-prune default frequencies (one epoch), the background thread and the single atomic delete batch in prune_hot_db. The only chunked work is reconstruction, so partial stays.

**Sources.** [nimbus#8852](https://github.com/status-im/nimbus-eth2/pull/8852), [nimbus@884193b2d](https://github.com/status-im/nimbus-eth2/commit/884193b2d2a5), [prysm#8911](https://github.com/OffchainLabs/prysm/pull/8911)

</details>

<a id="db_hot-039"></a>
<details>
<summary><b>db_hot-039</b> Serialize state once without extra copies — <i>partial · medium · M · cpu, memory, latency</i></summary>

**Idea.** When persisting a state, reference large lists (validators, balances, inactivity scores) instead of copying them and serialize once directly into a value buffer preallocated from the known SSZ size. This saves full state-sized copies and shortens state write transactions.

**Gap in Lighthouse.** Serialize the state straight into the zstd encoder (or stream) instead of a full intermediate SSZ Vec, and avoid to_vec() copies of milhouse lists in HDiffBuffer::from_state.

**Impact.** Saves one or two state-sized transient buffers (hundreds of MB on mainnet) per snapshot/diff write; periodic, not per block.

**Best measured result.** append-copy 412756 ns/op 8683521 B/op vs marshal-into-key 303836 ns/op 5939200 B/op (pr:prysm#17518)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2187-2200`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2187-L2200) store_hot_state_as_snapshot: as_ssz_bytes (preallocated from ssz_bytes_len) then a second pass through the zstd encoder
- [`beacon_node/store/src/hdiff.rs:173-197`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L173-L197) HDiffBuffer::from_state takes lists out of the state (no copy of the state) but then to_vec() copies validators, balances, inactivity scores, historical roots/summaries

**Second check.** Confirmed SSZ encoding preallocates from known length and take_* avoids cloning the whole state, but the intermediate SSZ buffer and list to_vec() copies remain.

**Sources.** [prysm#14612](https://github.com/OffchainLabs/prysm/pull/14612), [prysm#17518](https://github.com/OffchainLabs/prysm/pull/17518), [prysm#14613](https://github.com/OffchainLabs/prysm/pull/14613)

</details>

<a id="db_hot-059"></a>
<details>
<summary><b>db_hot-059</b> Store only hot blocks, regenerate hot states — <i>partial · medium · M · cpu, disk</i></summary>

**Idea.** Do not persist each new unfinalized state on import; store only hot blocks and regenerate hot states by replaying from the finalized (or migrated) state, leaving state persistence to the finalization migration. This trades CPU for disk and write volume.

**Gap in Lighthouse.** Most hot states already cost only a summary and are rebuilt by replay, but Lighthouse still writes hdiffs at every lowest-layer slot (each epoch with default exponents) and snapshots at higher layers during import. Making hot persistence summary-only, with replay from the finalized state, would need a hot-only hierarchy with no diff layers below the anchor.

**Impact.** Small: the remaining writes are per-epoch diffs; dropping them adds replay cost during long non-finality.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1741`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1741) store_hot_state_diffs: ReplayFrom slots persist only the summary, layer slots get a diff or snapshot
- [`beacon_node/store/src/hdiff.rs:660`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L660) storage_strategy returns ReplayFrom for slots that are not on a diff layer, so those states are rebuilt by block replay
- [`beacon_node/store/src/hot_cold_store.rs:407`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L407) hot_storage_strategy uses the anchor (finalized) slot as the hot hdiff start snapshot

**Second check.** Confirmed that the hot hdiff design already gives the replay path for non-layer slots (StorageStrategy::ReplayFrom). The hierarchy exponents are shared by hot and cold (cli hierarchy-exponents), and I found no hot-only config that turns off hot diffs.

**Sources.** [prysm#16739](https://github.com/OffchainLabs/prysm/pull/16739), [teku#1577](https://github.com/Consensys-Incorporated/teku/pull/1577)

</details>

<a id="db_hot-096"></a>
<details>
<summary><b>db_hot-096</b> Persist states only when a block follows — <i>partial · medium · S · disk, cpu</i></summary>

**Idea.** Do not write states produced by empty-slot advancement or attestation-driven processing to the hot DB; store a state only when a block is applied to it. Such states are cheap to recompute, rarely read and bloat the DB.

**Gap in Lighthouse.** The state-advance timer still persists the advanced (empty-slot) state each slot; it is a summary on most slots but a diff/snapshot when the advanced slot is a hierarchy boundary. That state is not in chain history when a block does follow at that slot. Drop the put_state in advance_head (or defer it until the slot is known to be empty).

**Impact.** Avoids one summary write per slot and an hdiff/snapshot computation+write at boundary slots on the state-advance thread; DB-size impact is small because of hierarchical storage.

**Best measured result.** storing states is (very) slow; avoids state database size explosion (pr:nimbus#1860)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:455`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L455) put_state of the empty-slot-advanced head state every slot
- [`beacon_node/store/src/hot_cold_store.rs:1068-1076`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1068-L1076) put_state -&gt; store_hot_state
- [`beacon_node/store/src/hot_cold_store.rs:1750-1760`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1750-L1760) ReplayFrom slots store only a summary; Snapshot/DiffFrom slots store a full snapshot or hdiff
- [`beacon_node/store/src/hot_cold_store.rs:1698-1706`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1698-L1706) skips diff computation if summary already on disk

**Second check.** Confirmed no attestation-driven path persists states (attestation verification uses shuffling/state caches), and that the hierarchical diff scheme makes most empty-slot writes summary-only, which is the partial mitigation; the advance-timer write remains.

**Sources.** [nimbus#1860](https://github.com/status-im/nimbus-eth2/pull/1860), [nimbus#1720](https://github.com/status-im/nimbus-eth2/pull/1720)

</details>

<a id="db_hot-108"></a>
<details>
<summary><b>db_hot-108</b> Prune blocks older than retention window — <i>partial · medium · M · disk, memory</i></summary>

**Idea.** Delete blocks and associated data older than a retention tail (e.g. min_epochs_for_block_requests or a weak-subjectivity based tail) from DB and in-memory indexes, so storage does not grow without bound.

**Gap in Lighthouse.** No retention prune for finalized blocks: once stored, beacon blocks (blinded) below a retention slot are never deleted and oldest_block_slot never moves up. Add a retention prune in the migrator that deletes blinded blocks below e.g. current_epoch - MIN_EPOCHS_FOR_BLOCK_REQUESTS via the cold BeaconBlockRoots index and raises anchor oldest_block_slot (status/blocks_by_range already honour it).

**Impact.** Disk only; since payloads are already pruned the remaining blinded blocks are tens of GB on a genesis-synced mainnet node. No CPU/hot-path gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3119`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3119) try_prune_execution_payloads (finalized payloads deleted, the bulk of post-merge block bytes)
- [`beacon_node/store/src/hot_cold_store.rs:3277`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3277) try_prune_blobs (blobs past DA boundary)
- [`beacon_node/store/src/hot_cold_store.rs:3471`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3471) prune_historic_states (freezer states only, no blocks)
- [`database_manager/src/cli.rs:75`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/database_manager/src/cli.rs#L75) subcommands: PrunePayloads/PruneBlobs/PruneStates, no PruneBlocks
- [`beacon_node/store/src/metadata.rs:99`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/metadata.rs#L99) oldest_block_slot only ever moves down via backfill
- [`beacon_node/store/src/hot_cold_store.rs:919`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L919) delete_block used only for abandoned forks (migrate.rs pruning)

**Second check.** Searched store, beacon_chain and database_manager for any block retention/prune (prune_blocks, DeleteBlock callers, anchor oldest_block_slot updates, db subcommands); only payload, blob, freezer-state and abandoned-fork pruning exist.

**Sources.** [nimbus@777b3f4e2](https://github.com/status-im/nimbus-eth2/commit/777b3f4e29c2), [grandine@d556ebf3d](https://github.com/grandinetech/grandine/commit/d556ebf3d9cd)

</details>

<a id="db_hot-143"></a>
<details>
<summary><b>db_hot-143</b> Skip checkpoint state writes during sync — <i>partial · medium · M · disk, sync</i></summary>

**Idea.** Do not persist checkpoint states while syncing, avoiding large state writes not needed during sync.

**Gap in Lighthouse.** Lighthouse's analogue of the Grandine checkpoint state (the head state advanced to the next epoch boundary by the state advance timer, written via put_state) is already not computed or written while syncing. What remains is the block-import path: hot summaries plus hdiff snapshots/diffs at hierarchy boundaries are written during range sync too; deferring the diff part while far behind is possible but migration needs those states.

**Impact.** Remaining gain small: diffs only at hierarchy-boundary slots, and the clock-driven checkpoint state write is already skipped during sync.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:33`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L33) MAX_ADVANCE_DISTANCE: 'avoids doing unnecessary work whilst the node is syncing'
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:268`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L268) head advance refused when head_slot + 256 &lt; current_slot
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:455`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L455) put_state of the advanced (next-epoch checkpoint) state, so skipped during sync
- [`beacon_node/beacon_chain/src/migrate.rs:314`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L314) epochs_per_migration batches finalization migration
- [`beacon_node/store/src/hot_cold_store.rs:1660`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1660) store_hot_state still writes summary + diffs for every imported block state, no sync check
- [`beacon_node/beacon_chain/src/block_verification.rs:1631`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1631) skip-slot states stored unconditionally

**Second check.** Checked the state advance timer, which the earlier review missed: it refuses to advance (and thus to persist the advanced epoch-boundary state) when head is &gt;256 slots behind, matching the Grandine commit's is_forward_synced gate on its checkpoint-state append; import-path hot state writes remain unconditional.

**Sources.** [grandine@40d873a34](https://github.com/grandinetech/grandine/commit/40d873a3419b)

</details>

<a id="db_hot-154"></a>
<details>
<summary><b>db_hot-154</b> Snappy-compress blocks and states in DB — <i>partial · medium · S · disk, sync</i></summary>

**Idea.** Compress stored block and state values with snappy by default, shrinking disk size and I/O and speeding sync.

**Gap in Lighthouse.** States (hdiffs) are zstd-compressed, but blocks, blobs and columns are stored uncompressed and LevelDB's built-in block compression is off (snappy not even compiled in). Enabling LevelDB snappy or zstd-compressing the BeaconBlock column would close it.

**Impact.** Maybe 20-30% smaller block column and less read I/O at small CPU cost; modest since hdiff already dominates savings.

**Best measured result.** 3GB vs 12GB for 4000 epochs; 3-4x sync blocks/sec (pr:nimbus#1169)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:557-560`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L557-L560) blinded block stored as raw as_ssz_bytes()
- [`beacon_node/store/src/database/leveldb_impl.rs:37-39`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/leveldb_impl.rs#L37-L39) Options::new() with no compression set
- ~/.cargo/registry/src/*/leveldb-0.8.6/src/database/options.rs:72 default compression: Compression::No (and store/Cargo.toml:22 uses default-features = false, dropping the leveldb-sys snappy feature)
- [`beacon_node/store/src/hdiff.rs:402`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L402) state diffs zstd-compressed

**Second check.** Checked the dependency layer the earlier review skipped: the leveldb crate defaults to Compression::No and Lighthouse disables its snappy feature, so there is no hidden storage-engine compression. Enabling LevelDB snappy is an S-effort route needing no schema migration.

**Sources.** [nimbus#1169](https://github.com/status-im/nimbus-eth2/pull/1169), [prysm#4125](https://github.com/OffchainLabs/prysm/pull/4125), [prysm#4157](https://github.com/OffchainLabs/prysm/pull/4157)

</details>

<a id="db_hot-159"></a>
<details>
<summary><b>db_hot-159</b> Separate block header and body tables — <i>partial · medium · M · disk, cpu</i></summary>

**Idea.** Store block headers and bodies separately so header-only code paths (parent lookup, slot scans, pruning) do not read or decode bodies.

**Gap in Lighthouse.** The largest body part (execution payload) is already a separate column, and slot/root/parent/pruning paths use BeaconBlockRoots, summaries and fork choice. What remains is that header-only reads (e.g. beacon/headers API, some RPC/lookup paths) still decode the blinded body (attestations, signatures); a BeaconBlockHeader column would remove that.

**Impact.** Small: saves decoding blinded bodies in a few API/RPC paths; heavy payload bytes are already avoided.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:527-548`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L527-L548) block_as_kv_store_ops splits the block into a blinded block and a separately stored execution payload (DBColumn::ExecPayload)
- [`beacon_node/store/src/hot_cold_store.rs:663-670`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L663-L670) get_blinded_block reads only the blinded block, not the payload
- [`beacon_node/store/src/hot_cold_store.rs:3085-3099`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3085-L3099) BeaconBlockRoots column serves slot-&gt;root scans without block reads
- [`beacon_node/beacon_chain/src/migrate.rs:509`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L509) pruning uses HotStateSummary
- [`beacon_node/http_api/src/block_id.rs:74-79`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L74-L79) slot lookups via block_root_at_slot

**Second check.** Found an equivalent split the earlier review missed: blocks are stored as blinded block plus a separate ExecPayload column, so header-ish reads skip the payload, plus a slot-&gt;root column for scans. Not a true header table, so partial.

**Sources.** [ethlambda#96](https://github.com/lambdaclass/ethlambda/pull/96)

</details>

## Other checked ideas (51)

Implemented, not applicable, or low value.

<a id="db_hot-004"></a>
<details>
<summary><b>db_hot-004</b> Apply store updates in memory before disk write — <i>not · low · L · latency, disk</i></summary>

**Idea.** Apply block-import and finalization updates to the in-memory store immediately and write them to disk asynchronously, keeping references to pending data to avoid read-before-write races. Block import does not wait on storage I/O.

**Gap in Lighthouse.** Block import writes block, state diff and blobs to disk synchronously before releasing the fork choice write lock and declaring the block imported; only the state cache is updated in memory first. To copy Teku, import would hand the KV batch to a background writer, serve reads from a pending-writes overlay, and release fork choice before the write finishes. This conflicts with the explicit crash-consistency design (fork choice must not be ahead of disk, issue 2028).

**Impact.** Removes the DB write (BLOCK_PROCESSING_DB_WRITE, tens of ms, more on diff slots) from the import critical path and fork choice write lock, at the cost of crash-consistency risk; modest gain.

**Evidence (Lighthouse @ 928b61e719).**

- beacon_chain/src/beacon_chain.rs:~4750 import_block calls store.do_atomically_with_block_and_blobs_cache(ops) synchronously, fork choice write lock held until it returns
- store/src/hot_cold_store.rs:~1520 hot_db.do_atomically runs inline under the block_cache mutex
- store/src/hot_cold_store.rs:1665 store_hot_state puts the state into state_cache in memory first, but the diff/summary KV ops are still written inline

**Sources.** [teku#6086](https://github.com/Consensys-Incorporated/teku/pull/6086), [teku#3407](https://github.com/Consensys-Incorporated/teku/pull/3407), [teku#6194](https://github.com/Consensys-Incorporated/teku/pull/6194)

</details>

<a id="db_hot-110"></a>
<details>
<summary><b>db_hot-110</b> Prune dangling states at startup — <i>not · low · S · disk, startup</i></summary>

**Idea.** At startup, delete states between genesis and the last finalized slot that are not on archive/restore-point boundaries, to shrink the state store.

**Gap in Lighthouse.** Add a startup pass that scans hot state summaries below the split and deletes those not on a snapshot/diff boundary. Lighthouse already deletes non-boundary hot states at finalization migration, so only legacy leftovers would benefit.

**Impact.** Smaller DB on nodes with leftover states; no runtime speed change. Lighthouse's finalization migration already prunes, so little to gain.

**Best measured result.** 4000 state keys down to 86 (pr:prysm#4697)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3471`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3471) prune_historic_states only for archive-to-hdiff migration, run on user command
- [`beacon_node/store/src/hot_cold_store.rs:1661`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1661) store_hot_state: hot states stored as summaries+diffs, finalization migrates and deletes them

**Sources.** [prysm#7729](https://github.com/OffchainLabs/prysm/pull/7729), [prysm#4697](https://github.com/OffchainLabs/prysm/pull/4697)

</details>

<a id="db_hot-155"></a>
<details>
<summary><b>db_hot-155</b> Compress cached anchor states in memory — <i>not · low · S · memory</i></summary>

**Idea.** Snappy-compress full states held in an in-memory anchor/diff-base cache to halve its memory, at the cost of compression time.

**Gap in Lighthouse.** Could compress HDiffBuffer entries in HistoricStateCache with snappy/zstd; trades CPU on each get/put for memory. Lighthouse's hot cache shares structure so it has no anchor-blob equivalent.

**Impact.** Halves historic hdiff buffer cache memory (archive/historic queries only); not relevant for a normal mainnet node.

**Best measured result.** cut the cache size approximately in half; adds around 500ms to saving a state to DB (mainnet) (pr:prysm#16790)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/historic_state_cache.rs:14`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/historic_state_cache.rs#L14) caches HDiffBuffer (raw SSZ-like bytes) and BeaconState in LRU caches, uncompressed
- [`beacon_node/store/src/state_cache.rs:39`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L39) hot StateCache holds BeaconState structs (milhouse tree sharing), not full SSZ blobs

**Sources.** [prysm#16790](https://github.com/OffchainLabs/prysm/pull/16790)

</details>

<a id="db_hot-002"></a>
<details>
<summary><b>db_hot-002</b> Split large prunes into many small transactions — <i>partial · low · S · disk, latency, memory</i></summary>

**Idea.** Delete large ranges of old data in bounded chunks, each in its own write transaction, instead of one huge transaction. The writer lock is not held for the whole prune, and the store does not rebalance or crash after a massive commit.

**Gap in Lighthouse.** Pruning is naturally incremental (runs each finalization), but nothing bounds a single batch. try_prune_blobs with force or after a gap, prune_hot_db after long non-finality, and prune_historic_states put the whole range in one write batch. Chunk the ops Vec in these functions (e.g. 1 epoch or N thousand ops per do_atomically).

**Impact.** Only matters for catch-up cases (database_manager prune-blobs/prune-states, recovery after long non-finality); steady-state mainnet pruning is already small. Avoids a huge write batch and long write stall.

**Best measured result.** naive prune had to delete over 37 million records at once; increments of 100 epochs (pr:prysm#8764)

**Evidence (Lighthouse @ 928b61e719).**

- store/src/hot_cold_store.rs:3410 try_prune_blobs collects all deletes into one blobs_db_ops Vec, one do_atomically (~3452)
- beacon_chain/src/migrate.rs:~830 prune_hot_db builds one StoreOp batch, one do_atomically_with_block_and_blobs_cache
- store/src/config.rs:30 DEFAULT_EPOCHS_PER_BLOB_PRUNE=1, so blob prune normally covers ~1 epoch
- store/src/hot_cold_store.rs:3501-3520 prune_historic_states stages every freezer key in one cold_ops batch

**Sources.** [prysm#14929](https://github.com/OffchainLabs/prysm/pull/14929), [prysm#7754](https://github.com/OffchainLabs/prysm/pull/7754), [prysm#8599](https://github.com/OffchainLabs/prysm/pull/8599), [prysm#8764](https://github.com/OffchainLabs/prysm/pull/8764)

</details>

<a id="db_hot-007"></a>
<details>
<summary><b>db_hot-007</b> In-memory caches of blocks and states over DB — <i>partial · low · S · memory, disk, latency</i></summary>

**Idea.** Keep bounded LRU caches of recently used blocks and states (and latest votes) inside or in front of the store layer, pruned on finalization, so fork choice, import and every read path do not read and decode them from disk on every access.

**Gap in Lighthouse.** States are cached by default (state cache 128, hdiff buffer cache, historic state cache), and the block LRU code exists, but the block cache is disabled by default, so blocks are read and SSZ-decoded from the DB on each get_blinded_block/get_full_block outside the early attester cache. Change DEFAULT_BLOCK_CACHE_SIZE and the CLI default after measuring memory.

**Impact.** Cheaper repeated block reads (BlocksByRange/Root serving, REST, payload lookups) for a few MB per cached block; small on a validating node, larger on one serving peers.

**Best measured result.** intermediate state memory down 32x; removes read amplification (pr:lighthouse#837)

**Evidence (Lighthouse @ 928b61e719).**

- store/src/hot_cold_store.rs:74 block_cache: Option&lt;Mutex&lt;BlockCache&gt;&gt; LRU of blocks, blobs, columns
- store/src/config.rs:22 DEFAULT_BLOCK_CACHE_SIZE=0 and [`beacon_node/src/cli.rs:794`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L794) --block-cache-size default 0: block cache off by default
- store/src/config.rs:23 DEFAULT_STATE_CACHE_SIZE=128; store/src/state_cache.rs state LRU pruned in update_finalized_state (hot_cold_store.rs:434)
- store/src/hot_cold_store.rs:87 historic_state_cache; fork choice keeps latest votes in memory (proto_array)

**Sources.** [prysm#3249](https://github.com/OffchainLabs/prysm/pull/3249), [prysm#2560](https://github.com/OffchainLabs/prysm/pull/2560), [lighthouse#837](https://github.com/sigp/lighthouse/pull/837)

</details>

<a id="db_hot-013"></a>
<details>
<summary><b>db_hot-013</b> Key-only DB iteration without reading values — <i>partial · low · S · cpu, memory, disk</i></summary>

**Idea.** When listing, counting or scanning keys (column indices, state roots, blob counts), iterate keys only and do not read or copy values into memory.

**Gap in Lighthouse.** Key-only iteration exists in both backends and is used for state snapshots, but get_data_column_keys still reads full column values. Change it to iter_column_keys_from(DBColumn::BeaconDataColumn, block_root) with the same prefix take_while and parse_data_column_key.

**Impact.** Pruning and by-root column serving stop reading column payloads from disk just to list indices; saves reading the full stored column set (up to MBs per block post-Fulu) of each pruned block per finalization.

**Best measured result.** avoids a 247MB hot state allocation in getStateRootsBeforeSlot; blob value reads 76 to 53 in test (pr:teku#9033)

**Evidence (Lighthouse @ 928b61e719).**

- store/src/hot_cold_store.rs:2657 get_data_column_keys uses blobs_db.iter_column_from (reads and copies values) only to list indices
- beacon_chain/src/migrate.rs:788 and :848 call it for every pruned block on each finalization; hot_cold_store.rs:2602 and http_api/src/block_id.rs:506 also
- store/src/database/leveldb_impl.rs:228 iter_column_keys_from and redb_impl.rs:202 exist and are used at hot_cold_store.rs:2254 and :3501
- Upstream PR lighthouse#10503 is still OPEN

**Sources.** [lighthouse#10503](https://github.com/sigp/lighthouse/pull/10503), [teku#9033](https://github.com/Consensys-Incorporated/teku/pull/9033), [teku#6755](https://github.com/Consensys-Incorporated/teku/pull/6755), [teku#6780](https://github.com/Consensys-Incorporated/teku/pull/6780)

</details>

<a id="db_hot-037"></a>
<details>
<summary><b>db_hot-037</b> Keep DB transactions short, work outside them — <i>partial · low · S · cpu, latency</i></summary>

**Idea.** Do reads (for example pruner queries), serialization, compression, encoding, index computation, cache lookups and lock acquisition before or after a write transaction, never inside it. The transaction and its lock are held only for raw reads and writes, so writers and other DB users are not blocked.

**Gap in Lighthouse.** The DB write transaction holds only raw ops, but the block_cache mutex (and fork choice write lock) are held across convert_to_kv_batch (hdiff computation, block encoding) plus the blobs_db and hot_db writes. Move convert_to_kv_batch for both op sets before taking the cache guard in do_atomically_with_block_and_blobs_cache.

**Impact.** Shorter block_cache lock hold so concurrent block/blob reads from RPC and HTTP stall less during import; small since the block cache is off by default.

**Best measured result.** SaveBlocks up to 800ms, ReceiveBlock 2s before fix (pr:prysm#9431)

**Evidence (Lighthouse @ 928b61e719).**

- store/src/hot_cold_store.rs:~1514 block_cache mutex guard taken, then convert_to_kv_batch and hot_db.do_atomically run under it
- store/src/hot_cold_store.rs:1307 convert_to_kv_batch -&gt; store_hot_state computes hdiff and block encoding inside the guard
- store/src/hot_cold_store.rs:1462-1500 DeleteBlobs/DeleteDataColumns reads done before the guard (good)
- store/src/database/redb_impl.rs:155 do_atomically gets already-encoded ops, so the write txn does only raw inserts; leveldb uses a plain write batch
- beacon_chain/src/beacon_chain.rs:~4750 whole write also under the fork choice write lock

**Sources.** [prysm#8677](https://github.com/OffchainLabs/prysm/pull/8677), [prysm#11745](https://github.com/OffchainLabs/prysm/pull/11745), [teku#6917](https://github.com/Consensys-Incorporated/teku/pull/6917), [prysm#9431](https://github.com/OffchainLabs/prysm/pull/9431), [grandine@d7644f3d3](https://github.com/grandinetech/grandine/commit/d7644f3d3237)

</details>

<a id="db_hot-060"></a>
<details>
<summary><b>db_hot-060</b> Skip no-op DB deletes and empty transactions — <i>partial · low · S · cpu, disk</i></summary>

**Idea.** Do not issue DB deletes for keys known to be absent, and do not open or commit a transaction or storage update when the write batch is empty.

**Gap in Lighthouse.** Add early return `if ops_batch.is_empty()` in leveldb/redb do_atomically (and skip blobs_db write in do_atomically_with_block_and_blobs_cache when kv_blob_ops empty); in migrate prune only queue Delete ops for columns known present (fork/slot based). DeleteBlobs also does a get_blobs read first.

**Impact.** Small per-block saving: avoids an empty redb write tx (with fsync cost under redb) on every block import, and a few hundred tombstone writes per finalization; leveldb deletes are cheap so likely sub-ms to ms.

**Best measured result.** removed 20k key encodings and level db searches per block (pr:lodestar#1409)

**Evidence (Lighthouse @ 928b61e719).**

- store/src/hot_cold_store.rs:1376-1420 DeleteState picks snapshot/diff/none by slot via hot_storage_strategy (avoids some absent-key deletes)
- store/src/hot_cold_store.rs:3405 prune_blobs checks key_exists before queuing delete
- beacon_chain/src/migrate.rs:777-791 prune pushes 5-6 unconditional DeleteKey ops per abandoned block (ExecPayload, PayloadSummary+Body, BeaconBlob, SyncCommitteeBranch) even if absent
- store/src/hot_cold_store.rs:1487-1500 do_atomically_with_block_and_blobs_cache always calls blobs_db.do_atomically even with empty ops
- store/src/database/redb_impl.rs:155-189 do_atomically opens write tx and commits even for empty batch; leveldb_impl.rs:143-168 writes empty Writebatch

**Sources.** [grandine@91d83ff67](https://github.com/grandinetech/grandine/commit/91d83ff672b3), [lodestar#1409](https://github.com/ChainSafe/lodestar/pull/1409), [teku#6244](https://github.com/Consensys-Incorporated/teku/pull/6244)

</details>

<a id="db_hot-118"></a>
<details>
<summary><b>db_hot-118</b> Raise DB and open-file resource limits — <i>partial · low · S · sync, disk</i></summary>

**Idea.** Raise KV store limits (mmap/initial size) and the process open-file soft limit to the hard limit at startup, so the DB does not stall or crash on default resource limits.

**Gap in Lighthouse.** Call fdlimit::raise_fd_limit at beacon node startup (lighthouse/src/main.rs or the beacon_node client builder) and log the outcome, as the validator client does.

**Impact.** Avoids too-many-open-files failures with leveldb and many peers/sockets on hosts with a 1024 soft limit; a stability fix, not speed.

**Best measured result.** crash after days on 1024 limit (pr:ethlambda#422)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/src/lib.rs:128`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/src/lib.rs#L128) fdlimit::raise_fd_limit used only in validator client
- [`beacon_node/store/src/database/leveldb_impl.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/leveldb_impl.rs) and redb_impl.rs: no open-files or mmap options set
- grep fdlimit/rlimit finds nothing in beacon_node or [`lighthouse/src`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/src)

**Sources.** [prysm#4485](https://github.com/OffchainLabs/prysm/pull/4485), [ethlambda#422](https://github.com/lambdaclass/ethlambda/pull/422)

</details>

<a id="db_hot-001"></a>
<details>
<summary><b>db_hot-001</b> Batch many small DB writes into one transaction — <i>implemented · medium · S · disk, cpu, sync</i></summary>

**Idea.** Group many per-item writes or deletes (attestations, votes, validator index entries, states, slasher spans) into one key-value write batch or transaction instead of one commit per item. This removes per-commit fsync and lock overhead.

**Gap in Lighthouse.** 

**Impact.** Already batched.

**Best measured result.** validator test ~400s down to ~1s (pr:prysm#1732)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1459`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1459) do_atomically_with_block_and_blobs_cache takes Vec&lt;StoreOp&gt; batch
- [`beacon_node/store/src/lib.rs:71`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/lib.rs#L71) KeyValueStore::do_atomically
- [`slasher/src/database.rs:329`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L329) slasher uses one rw txn per batch

**Sources.** [prysm#3496](https://github.com/OffchainLabs/prysm/pull/3496), [prysm#5041](https://github.com/OffchainLabs/prysm/pull/5041), [prysm#3622](https://github.com/OffchainLabs/prysm/pull/3622), [prysm#1732](https://github.com/OffchainLabs/prysm/pull/1732), [prysm#3820](https://github.com/OffchainLabs/prysm/pull/3820), [prysm#4494](https://github.com/OffchainLabs/prysm/pull/4494), [prysm#4489](https://github.com/OffchainLabs/prysm/pull/4489), [prysm#3672](https://github.com/OffchainLabs/prysm/pull/3672), [prysm#5534](https://github.com/OffchainLabs/prysm/pull/5534), [prysm#5320](https://github.com/OffchainLabs/prysm/pull/5320), [teku#5903](https://github.com/Consensys-Incorporated/teku/pull/5903)

</details>

<a id="db_hot-009"></a>
<details>
<summary><b>db_hot-009</b> Do not store EL-reconstructible execution payloads — <i>implemented · medium · S · disk</i></summary>

**Idea.** Store beacon blocks blinded (without payload transactions and withdrawals), or prune payloads of finalized blocks at migration, since the execution client already holds them, and rebuild the full block from the EL when serving it. This avoids storing each payload twice and cuts disk usage and write I/O.

**Gap in Lighthouse.** 

**Impact.** Done: blinded blocks stored, payloads of finalized blocks optionally pruned.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:533`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L533) block split into blinded block + payload
- [`beacon_node/store/src/hot_cold_store.rs:3119`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3119) try_prune_execution_payloads

**Sources.** [lodestar#6029](https://github.com/ChainSafe/lodestar/pull/6029), [lodestar#7034](https://github.com/ChainSafe/lodestar/pull/7034), [lighthouse#3157](https://github.com/sigp/lighthouse/pull/3157), [lodestar#5705](https://github.com/ChainSafe/lodestar/pull/5705), [lighthouse#3565](https://github.com/sigp/lighthouse/pull/3565), [grandine#949](https://github.com/grandinetech/grandine/pull/949)

</details>

<a id="db_hot-010"></a>
<details>
<summary><b>db_hot-010</b> Load blinded block when payload not needed — <i>implemented · medium · S · disk, cpu</i></summary>

**Idea.** When a caller only needs block metadata or commitments, read the blinded block from the DB instead of the full block with payload, avoiding a large read and decode.

**Gap in Lighthouse.** 

**Impact.** Done.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:663`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L663) get_blinded_block
- [`beacon_node/store/src/iter.rs:188`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/iter.rs#L188) block iterators use blinded blocks
- [`beacon_node/http_api/src/block_id.rs:119`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L119) API uses blinded read

**Sources.** [lighthouse@caad492d4](https://github.com/sigp/lighthouse/commit/caad492d48aa)

</details>

<a id="db_hot-012"></a>
<details>
<summary><b>db_hot-012</b> Store each data column/blob sidecar under its own key — <i>implemented · medium · S · cpu, disk, bandwidth</i></summary>

**Idea.** Key each data column or blob sidecar by (block root or slot, index) instead of storing the whole per-block list under one key. Serving one column reads and decodes one item, and shared fields are not duplicated.

**Gap in Lighthouse.** 

**Impact.** Done.

**Best measured result.** avoids up to x128 more I/O than necessary (pr:lighthouse#5890)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/lib.rs:144`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/lib.rs#L144) get_data_column_key = block_root\|\|column_index
- [`beacon_node/store/src/hot_cold_store.rs:956`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L956) data_column_as_kv_store_ops one key per column

**Sources.** [lighthouse#5890](https://github.com/sigp/lighthouse/pull/5890), [lodestar#8206](https://github.com/ChainSafe/lodestar/pull/8206), [lodestar#8233](https://github.com/ChainSafe/lodestar/pull/8233), [lighthouse#6073](https://github.com/sigp/lighthouse/pull/6073)

</details>

<a id="db_hot-018"></a>
<details>
<summary><b>db_hot-018</b> Hierarchical state diffs in the hot DB — <i>implemented · medium · S · disk</i></summary>

**Idea.** Store hot states as periodic snapshots plus hierarchical diffs, as in the freezer, and skip storing a state whose summary already exists. Hot DB disk footprint and write I/O drop a lot, especially during non-finality.

**Gap in Lighthouse.** 

**Impact.** Done.

**Best measured result.** massively reduce disk footprint during non-finality and overall I/O; ~1MB per written diff on Holesky (pr:lighthouse#6750)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1695`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1695) skip diff if summary already stored
- [`beacon_node/store/src/hot_cold_store.rs:1741`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1741) store_hot_state_diffs
- [`beacon_node/store/src/hot_cold_store.rs:1771`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1771) store_hot_state_as_diff

**Sources.** [lighthouse#6750](https://github.com/sigp/lighthouse/pull/6750), [lighthouse#7087](https://github.com/sigp/lighthouse/pull/7087)

</details>

<a id="db_hot-021"></a>
<details>
<summary><b>db_hot-021</b> Bound prune iteration to not-yet-pruned range — <i>implemented · medium · S · disk, cpu</i></summary>

**Idea.** Start pruning at the first existing key or oldest stored slot and stop at the first entry already pruned or still retained, using an ordered cursor or backward iterator, instead of scanning the whole column on each prune.

**Gap in Lighthouse.** 

**Impact.** Blob and payload prunes touch only the new range; no gain left there.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3378`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3378) blob prune iterates parent roots backwards and breaks at first block with blobs already pruned
- [`beacon_node/store/src/hot_cold_store.rs:3148`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3148) payload prune checks finalized_payloads_are_pruned first; loop stops at oldest_block_slot

**Sources.** [lighthouse#8266](https://github.com/sigp/lighthouse/pull/8266), [prysm#8627](https://github.com/OffchainLabs/prysm/pull/8627), [lighthouse#6745](https://github.com/sigp/lighthouse/pull/6745), [lodestar@335059d5f](https://github.com/ChainSafe/lodestar/commit/335059d5fa8a)

</details>

<a id="db_hot-022"></a>
<details>
<summary><b>db_hot-022</b> Prune blobs outside retention window, verify deletion — <i>implemented · medium · S · disk</i></summary>

**Idea.** Delete blob sidecars from the DB once they are outside the data availability retention window, and check that pruning uses the same key encoding as writes and a correct existence check so expired data is really deleted and the blob store stays bounded.

**Gap in Lighthouse.** 

**Impact.** Blob store stays bounded already.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3277`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3277) try_prune_blobs deletes blobs/columns older than DA boundary minus margin
- [`beacon_node/store/src/hot_cold_store.rs:3367`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3367) key_exists check on the same key encoding used for writes (block root / column keys)

**Sources.** [grandine@3efe29029](https://github.com/grandinetech/grandine/commit/3efe2902904a), [lighthouse#4693](https://github.com/sigp/lighthouse/pull/4693), [nimbus#5283](https://github.com/status-im/nimbus-eth2/pull/5283)

</details>

<a id="db_hot-023"></a>
<details>
<summary><b>db_hot-023</b> Delete abandoned fork blocks and states at finalization — <i>implemented · medium · S · disk</i></summary>

**Idea.** On finalization, delete blocks and states (including skipped-slot states) of abandoned forks at or below the finalized slot from the hot DB, keeping states shared with the canonical chain and the finalized boundary state. Abandoned forks then do not accumulate and the hot DB stops growing without bound.

**Gap in Lighthouse.** 

**Impact.** Abandoned forks are removed at each finalization.

**Best measured result.** should end unbounded chain_db growth (pr:lighthouse#1564)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/migrate.rs:509`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L509) prune_hot_db builds state summaries DAG and prunes non-descendants of finalized checkpoint
- [`beacon_node/beacon_chain/src/migrate.rs:640`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L640) states_to_prune/blocks_to_prune keep finalized-descendant and required hdiff states

**Sources.** [lighthouse#1564](https://github.com/sigp/lighthouse/pull/1564), [lighthouse#916](https://github.com/sigp/lighthouse/pull/916), [grandine#145](https://github.com/grandinetech/grandine/pull/145), [grandine@4c2be4b16](https://github.com/grandinetech/grandine/commit/4c2be4b16434)

</details>

<a id="db_hot-025"></a>
<details>
<summary><b>db_hot-025</b> Keep pruning off the startup path — <i>implemented · medium · S · disk, startup</i></summary>

**Idea.** Do not run heavy scan-and-delete pruning (old states, payloads) synchronously at startup: put it behind a flag, run it in a background thread, or do it incrementally. Node startup is then not blocked for minutes.

**Gap in Lighthouse.** 

**Impact.** Startup is not blocked by payload or blob pruning; state pruning is an explicit db subcommand.

**Best measured result.** startup prune 2m5s on good I/O, 16m on slow (pr:lighthouse#3587)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/builder.rs:1164`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L1164) try_prune_execution_payloads runs in spawn_blocking background task
- [`beacon_node/beacon_chain/src/builder.rs:1178`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L1178) blob prune via store_migrator.process_prune_blobs in background

**Sources.** [lighthouse#3587](https://github.com/sigp/lighthouse/pull/3587), [nimbus#5191](https://github.com/status-im/nimbus-eth2/pull/5191), [prysm#5011](https://github.com/OffchainLabs/prysm/pull/5011)

</details>

<a id="db_hot-058"></a>
<details>
<summary><b>db_hot-058</b> Periodic hot state snapshots to bound replay — <i>implemented · medium · cpu, disk, startup</i></summary>

**Idea.** Persist full hot (unfinalized) states only at regular intervals (every N slots or epochs, for example every epoch or every other epoch, also during sync and long non-finality) and rebuild other states by replaying blocks from the nearest snapshot. This bounds hot DB size and write volume as well as the replay cost on restart or state regeneration.

**Gap in Lighthouse.** 

**Impact.** Already bounds hot state storage and restart replay; nothing to gain.

**Best measured result.** cuts hot DB state storage by a factor of SLOTS_PER_EPOCH (32) (pr:lighthouse#746)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1727`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1727) store_hot_state_summary writes a summary for every state
- [`beacon_node/store/src/hot_cold_store.rs:1752`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1752) store_hot_state_diffs: Snapshot/DiffFrom only on hierarchy layer slots, ReplayFrom stores nothing more
- [`beacon_node/store/src/hot_cold_store.rs:1949`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1949) load_hot_state replays from nearest stored base (ReplayFrom)

**Sources.** [teku#3017](https://github.com/Consensys-Incorporated/teku/pull/3017), [prysm#16589](https://github.com/OffchainLabs/prysm/pull/16589), [teku#2611](https://github.com/Consensys-Incorporated/teku/pull/2611), [teku#2663](https://github.com/Consensys-Incorporated/teku/pull/2663), [prysm#16808](https://github.com/OffchainLabs/prysm/pull/16808), [lighthouse#746](https://github.com/sigp/lighthouse/pull/746), [lighthouse#2833](https://github.com/sigp/lighthouse/pull/2833), [nimbus#1887](https://github.com/status-im/nimbus-eth2/pull/1887)

</details>

<a id="db_hot-061"></a>
<details>
<summary><b>db_hot-061</b> Get state root from next block in replay — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** During block replay, load one extra block to read the state root it commits to instead of tree-hashing the replayed state.

**Gap in Lighthouse.** 

**Impact.** Replay avoids tree-hashing the state at block slots; already done.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/block_replayer.rs:183`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/block_replayer.rs#L183) get_state_root takes root from prev block
- [`consensus/state_processing/src/block_replayer.rs:222`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/block_replayer.rs#L222) extra leading block used only for its state root
- [`beacon_node/store/src/hot_cold_store.rs:2530`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2530) load_blocks_to_replay includes block at start slot for its state root

**Sources.** [lighthouse#862](https://github.com/sigp/lighthouse/pull/862)

</details>

<a id="db_hot-074"></a>
<details>
<summary><b>db_hot-074</b> Resolve block slot without loading block or state — <i>implemented · medium · cpu, disk, latency</i></summary>

**Idea.** Answer root-to-slot queries (for example in state pruning) from fork choice, a slot index, a state summary or the block instead of decoding the full state, so callers that need only the slot do not load large objects.

**Gap in Lighthouse.** 

**Impact.** State/block pruning and slot lookups already use summaries, not full states.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3867`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3867) HotStateSummary stores slot, latest_block_slot, previous_state_root
- [`beacon_node/store/src/hot_cold_store.rs:3003`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3003) load_hot_state_summary gives slot without loading state
- [`beacon_node/beacon_chain/src/migrate.rs:537`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L537) prune_hot_db builds DAG from summaries, never loads states

**Sources.** [prysm#5246](https://github.com/OffchainLabs/prysm/pull/5246), [teku#10454](https://github.com/Consensys-Incorporated/teku/pull/10454), [prysm#16040](https://github.com/OffchainLabs/prysm/pull/16040)

</details>

<a id="db_hot-084"></a>
<details>
<summary><b>db_hot-084</b> Prune hot states older than finalization — <i>implemented · medium · disk</i></summary>

**Idea.** When a new checkpoint finalizes, delete hot-DB states older than the finalized slot (including boundary states), optionally keeping only sparse periodic states, and enable this by default so state storage stays bounded.

**Gap in Lighthouse.** 

**Impact.** Hot state storage is already bounded by finalization, keeping only sparse hierarchy states.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/migrate.rs:509`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L509) prune_hot_db
- [`beacon_node/beacon_chain/src/migrate.rs:640`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L640) states_to_prune: everything not descendant of finalized checkpoint, except sparse hdiff layer points (required_finalized_diff_state_slots)

**Sources.** [prysm#2034](https://github.com/OffchainLabs/prysm/pull/2034), [prysm#4139](https://github.com/OffchainLabs/prysm/pull/4139), [nimbus#1624](https://github.com/status-im/nimbus-eth2/pull/1624), [prysm#4082](https://github.com/OffchainLabs/prysm/pull/4082), [prysm#3856](https://github.com/OffchainLabs/prysm/pull/3856), [prysm#3824](https://github.com/OffchainLabs/prysm/pull/3824), [nimbus#191](https://github.com/status-im/nimbus-eth2/pull/191), [prysm#4204](https://github.com/OffchainLabs/prysm/pull/4204)

</details>

<a id="db_hot-085"></a>
<details>
<summary><b>db_hot-085</b> Optional pruning of historical states — <i>implemented · medium · disk</i></summary>

**Idea.** Make deletion of historical (cold) states not needed for the node's mode available, as a configurable option or an offline command, trading availability of old states for much less disk usage.

**Gap in Lighthouse.** 

**Impact.** Already lets a node drop historical states offline; disk saving only for nodes that wanted them.

**Best measured result.** takes a few seconds max on mainnet (pr:lighthouse#4835)

**Evidence (Lighthouse @ 928b61e719).**

- [`database_manager/src/lib.rs:458`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/database_manager/src/lib.rs#L458) prune-states subcommand calls prune_historic_states
- [`beacon_node/store/src/hot_cold_store.rs:3471`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3471) prune_historic_states deletes all freezer state columns and sets state_upper_limit NO_RETAIN

**Sources.** [prysm#2210](https://github.com/OffchainLabs/prysm/pull/2210), [lighthouse#4835](https://github.com/sigp/lighthouse/pull/4835)

</details>

<a id="db_hot-092"></a>
<details>
<summary><b>db_hot-092</b> Partial state getters and cached state hash — <i>implemented · medium · cpu, memory</i></summary>

**Idea.** Give callers getters for single state fields (validators, balances) and a cached state hash, so they do not clone or rehash the whole state.

**Gap in Lighthouse.** 

**Impact.** Equivalent effect via milhouse structural sharing: state clone is O(1) and root is incremental, so no whole-state clone/rehash.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:3070`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3070) update_tree_hash_cache, :1087 canonical_root: hash cache lives inside the state (milhouse)
- [`beacon_node/store/src/state_cache.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs): states cached and cloned cheaply (persistent trees)

**Sources.** [prysm#2334](https://github.com/OffchainLabs/prysm/pull/2334)

</details>

<a id="db_hot-101"></a>
<details>
<summary><b>db_hot-101</b> Persist head, fork choice and eth1 data less often — <i>implemented · medium · disk, cpu, latency</i></summary>

**Idea.** Write chain metadata (head pointer, fork choice, op pool, eth1 cache, wall-clock time) only when it changes or at coarse points (epoch crossing, every N blocks, shutdown) instead of on every block, attestation or tick. Split large persisted objects so only the changed part is written.

**Gap in Lighthouse.** 

**Impact.** Already coarse: fork choice per epoch/reorg/finality, op pool only at shutdown, head pointer not rewritten per block.

**Best measured result.** "committing less frequently to the database, which should help with contention" (pr:teku#1232)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:1564-1566`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1564-L1566) persist_fork_choice only on epoch transition or reorg
- canonical_head.rs:1720 persist at finalization
- [`beacon_node/beacon_chain/src/beacon_chain.rs:8464-8466`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L8464-L8466) op pool, custody context and fork choice persisted on Drop
- [`beacon_node/beacon_chain/src/beacon_chain.rs:687`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L687) head persisted only as genesis root; no eth1 cache or wall-clock persistence

**Sources.** [lighthouse#851](https://github.com/sigp/lighthouse/pull/851), [prysm#3669](https://github.com/OffchainLabs/prysm/pull/3669), [prysm#9764](https://github.com/OffchainLabs/prysm/pull/9764), [teku#1232](https://github.com/Consensys-Incorporated/teku/pull/1232)

</details>

<a id="db_hot-104"></a>
<details>
<summary><b>db_hot-104</b> Store previous state root in hot summaries — <i>implemented · medium · cpu, memory, latency</i></summary>

**Idea.** Store the previous state root in each hot state summary so loading a state from disk needs no tree hashing; reading a few summaries is cheaper than building a tree hash cache.

**Gap in Lighthouse.** 

**Impact.** Already done: state roots found by summary links, no tree hash cache build when loading from disk.

**Best measured result.** tree hash cache costs 1s+ CPU and 300MB+ RAM; summaries read &lt;250ms for 32 (pr:lighthouse#2954)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3872`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3872) HotStateSummary.previous_state_root
- [`beacon_node/store/src/hot_cold_store.rs:3981-3993`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3981-L3993) filled in HotStateSummary::new
- [`beacon_node/store/src/hot_cold_store.rs:3859`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3859) get_ancestor_state_root walks previous_state_root links without hashing

**Sources.** [lighthouse#2954](https://github.com/sigp/lighthouse/pull/2954)

</details>

<a id="db_hot-109"></a>
<details>
<summary><b>db_hot-109</b> Write intermediate states to DB as temporary — <i>implemented · medium · memory</i></summary>

**Idea.** Write intermediate states created during block processing directly to the hot DB marked temporary, clear the mark on success, and garbage-collect leftovers at startup, so they need not be held in memory.

**Gap in Lighthouse.** 

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1632`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1632) intermediate skip-slot states written via store_hot_state immediately
- [`beacon_node/store/src/lib.rs:304`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/lib.rs#L304) BeaconStateTemporary column deprecated
- [`beacon_node/store/src/hot_cold_store.rs:1741`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1741) store_hot_state_diffs writes only summary on replay slots

**Sources.** [lighthouse#1798](https://github.com/sigp/lighthouse/pull/1798)

</details>

<a id="db_hot-119"></a>
<details>
<summary><b>db_hot-119</b> Slot-ordered range scans instead of per-key lookups — <i>implemented · medium · disk, cpu</i></summary>

**Idea.** Iterate slot-ordered DB keys with range filters (gt/lt/reverse/limit, streaming) instead of issuing one lookup per slot or scanning a hash-keyed index, for custody scans, pruning and queries.

**Gap in Lighthouse.** 

**Best measured result.** Average ~400 block queries per call before (pr:teku#9797)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/forwards_iter.rs:117`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/forwards_iter.rs#L117) FrozenForwardsIterator uses iter_column_from over big-endian slot keys
- [`beacon_node/store/src/hot_cold_store.rs:2488`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2488) load_cold_blocks uses the forwards root iterator
- [`beacon_node/store/src/hot_cold_store.rs:3577`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3577) BeaconBlockRoots keyed by slot be bytes

**Sources.** [teku#9797](https://github.com/Consensys-Incorporated/teku/pull/9797), [teku#6912](https://github.com/Consensys-Incorporated/teku/pull/6912), [lodestar#858](https://github.com/ChainSafe/lodestar/pull/858)

</details>

<a id="db_hot-127"></a>
<details>
<summary><b>db_hot-127</b> Find highest block at or below slot quickly — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** Answer 'highest block at or below slot' (e.g. replay base lookup) by seeking a slot index to the target and walking backwards, or with a per-slot bitfield, instead of scanning forward or keeping boundary-root bookkeeping.

**Gap in Lighthouse.** 

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3070`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3070) store_frozen_block_root_at_skip_slots fills a per-slot root index (skipped slots point to prior block)
- [`beacon_node/store/src/hot_cold_store.rs:3097`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3097) get_cold_block_root is a point lookup by slot
- [`beacon_node/store/src/forwards_iter.rs:29`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/forwards_iter.rs#L29) hot part walks state block_roots backwards

**Sources.** [prysm#10772](https://github.com/OffchainLabs/prysm/pull/10772), [prysm#5182](https://github.com/OffchainLabs/prysm/pull/5182), [prysm#5230](https://github.com/OffchainLabs/prysm/pull/5230)

</details>

<a id="db_hot-142"></a>
<details>
<summary><b>db_hot-142</b> Start from stored hot states without block replay — <i>implemented · medium · startup</i></summary>

**Idea.** Offer a startup mode that loads stored hot states directly instead of replaying blocks from the finalized state.

**Gap in Lighthouse.** 

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/builder.rs:784`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L784) get_advanced_hot_state loads head state from DB on restart
- [`beacon_node/store/src/hot_cold_store.rs:1949`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1949) load_hot_state loads snapshot/diff directly, replays only from the nearest diff layer
- [`beacon_node/store/src/hot_cold_store.rs:407`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L407) hot_storage_strategy

**Sources.** [teku#2617](https://github.com/Consensys-Incorporated/teku/pull/2617)

</details>

<a id="db_hot-144"></a>
<details>
<summary><b>db_hot-144</b> Reuse fresh DB state instead of checkpoint download — <i>implemented · medium · S · startup, bandwidth</i></summary>

**Idea.** When started with a checkpoint sync URL, reuse the persisted finalized state if it is recent enough relative to the wall clock and skip the download.

**Gap in Lighthouse.** 

**Impact.** Restart with a persisted DB never re-downloads the state; stricter than a recency bound (no staleness check, node just syncs forward from DB).

**Best measured result.** bound 450 slots (~30 min) (pr:ethlambda#403)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/client/src/builder.rs:290-305`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L290-L305) if the DB already holds a chain, checkpoint sync is refused and ClientGenesis::FromStore used
- [`beacon_node/client/src/builder.rs:423`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L423) download only happens on empty DB

**Sources.** [ethlambda#403](https://github.com/lambdaclass/ethlambda/pull/403)

</details>

<a id="db_hot-158"></a>
<details>
<summary><b>db_hot-158</b> Run DB reads off the async executor — <i>implemented · medium · S · latency</i></summary>

**Idea.** Run blocking DB reads (block by root, payload bids) on a blocking thread pool instead of async executor threads so they do not stall the runtime.

**Gap in Lighthouse.** 

**Impact.** Already prevents DB reads from stalling tokio workers.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:4308-4319`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4308-L4319) get_or_load_gloas_payload_bid loads via spawn_blocking_handle
- [`beacon_node/beacon_chain/src/beacon_block_streamer.rs:260`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_block_streamer.rs#L260) streamer uses spawn_blocking_handle
- [`beacon_node/http_api/src/task_spawner.rs:48`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/task_spawner.rs#L48) blocking_task for HTTP handlers
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:345`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L345) parent walk on blocking thread

**Sources.** [lighthouse#5585](https://github.com/sigp/lighthouse/pull/5585), [lighthouse#9634](https://github.com/sigp/lighthouse/pull/9634)

</details>

<a id="db_hot-005"></a>
<details>
<summary><b>db_hot-005</b> Slot-indexed canonical block root lookup — <i>implemented · low · cpu, disk, latency</i></summary>

**Idea.** Maintain a slot-indexed index (DB table or in-memory array) from slot to canonical block root, updated on head change, reorg and finalization, so by-slot lookups (REST, BlocksByRange, ancestors) are direct reads instead of walking parent links back from the head.

**Gap in Lighthouse.** 

**Evidence (Lighthouse @ 928b61e719).**

- beacon_chain/src/beacon_chain.rs:1060 block_root_at_slot_skips_none fast path reads state.get_block_root from the head state's block_roots vector
- beacon_chain/src/beacon_chain.rs:1124 block_root_at_slot_skips_prev same fast path
- store/src/hot_cold_store.rs:3096 get_cold_block_root and store/src/forwards_iter.rs:140 FrozenForwardsIterator: slot-indexed DBColumn::BeaconBlockRoots in the freezer
- store/src/forwards_iter.rs:21-40 only the unfinalized range walks BlockRootsIterator over the end state

**Sources.** [ethlambda#495](https://github.com/lambdaclass/ethlambda/pull/495), [prysm#2278](https://github.com/OffchainLabs/prysm/pull/2278), [prysm#15063](https://github.com/OffchainLabs/prysm/pull/15063), [nimbus#3144](https://github.com/status-im/nimbus-eth2/pull/3144)

</details>

<a id="db_hot-020"></a>
<details>
<summary><b>db_hot-020</b> Cache hot hdiff buffers alongside state cache — <i>implemented · low · cpu, disk, latency</i></summary>

**Idea.** Keep an in-memory cache of the hot DB hierarchical-diff buffers on the path to the finalized state, so storing a new hot state does not reload and rebuild those buffers.

**Gap in Lighthouse.** 

**Best measured result.** Costs about 438 MB per buffer on Holesky; reduces store time (pr:lighthouse#7615)

**Evidence (Lighthouse @ 928b61e719).**

- store/src/state_cache.rs:59 HotHDiffBufferCache LRU of pre-finalized HDiffBuffers
- store/src/state_cache.rs:152-175 update_finalized_state prunes and refills buffers needed by the hdiff grid
- store/src/hot_cold_store.rs:1861 load_hot_hdiff_buffer checks state_cache.get_hdiff_buffer_by_state_root before rebuilding; :1924 put_hdiff_buffer
- store/src/config.rs:28 DEFAULT_HOT_HDIFF_BUFFER_CACHE_SIZE=1

**Sources.** [lighthouse#7615](https://github.com/sigp/lighthouse/pull/7615)

</details>

<a id="db_hot-036"></a>
<details>
<summary><b>db_hot-036</b> Skip fsync on rebuildable cache dumps — <i>implemented · low · disk, latency</i></summary>

**Idea.** Do not fsync files that only hold rebuildable cache data (for example periodic fork-graph or head-state dumps), shortening the time held under shared locks.

**Gap in Lighthouse.** 

**Best measured result.** head-state dump p50 ~540 ms for 143 MB (baseline; gain not stated) (pr:caplin#25251)

**Evidence (Lighthouse @ 928b61e719).**

- store/src/database/leveldb_impl.rs:50 default write options sync=false; fsync only via put_sync/sync()
- put_sync/sync() callers: store/src/hot_cold_store.rs:3627,3655 (split point) and beacon_chain/src/historical_blocks.rs:434-480 (backfill metadata), all correctness-critical
- beacon_chain/src/beacon_chain.rs:723 persist_op_pool and :735 persist_custody_context use put_item, no sync

**Sources.** [caplin#25251](https://github.com/erigontech/erigon/pull/25251)

</details>

<a id="db_hot-046"></a>
<details>
<summary><b>db_hot-046</b> Store sync committees once, reference by hash — <i>implemented · low · disk</i></summary>

**Idea.** Store each distinct sync committee once in its own column and have light-client bootstrap records reference it by hash, instead of embedding the ~24 KB committee in every bootstrap.

**Gap in Lighthouse.** 

**Impact.** Already stores committee once per period with only the Merkle branch per checkpoint block; no ~20x duplication.

**Best measured result.** per period 8192*25KB=205MB down to 8192*1.2KB+24KB=10MB (~20x) (pr:prysm#14775)

**Evidence (Lighthouse @ 928b61e719).**

- store/src/hot_cold_store.rs:785 get_sync_committee keyed by period
- store/src/hot_cold_store.rs:816 store_sync_committee stores each committee once per period
- store/src/hot_cold_store.rs:770 branch stored separately per block root
- beacon_chain/src/light_client_server_cache.rs:418-432 bootstrap assembled on demand from branch + committee

**Sources.** [prysm#14775](https://github.com/OffchainLabs/prysm/pull/14775)

</details>

<a id="db_hot-049"></a>
<details>
<summary><b>db_hot-049</b> Store earliest available block slot as DB variable — <i>implemented · low · latency, disk</i></summary>

**Idea.** Keep the earliest stored block slot in a single DB variable updated on write and prune, so BlocksByRange answers immediately instead of scanning for it.

**Gap in Lighthouse.** 

**Impact.** Earliest block slot is an in-memory value persisted in anchor info and updated on backfill; no scan.

**Best measured result.** query varied from a few ms to double-digit seconds (pr:teku#8722)

**Evidence (Lighthouse @ 928b61e719).**

- store/src/hot_cold_store.rs:2793 get_anchor_info reads in-memory RwLock&lt;AnchorInfo&gt;
- store/src/metadata.rs:99 AnchorInfo.oldest_block_slot persisted
- network/src/network_beacon_processor/rpc_methods.rs:520 BlocksByRange uses get_oldest_block_slot, no scan

**Sources.** [teku#8722](https://github.com/Consensys-Incorporated/teku/pull/8722)

</details>

<a id="db_hot-076"></a>
<details>
<summary><b>db_hot-076</b> Clean up temporary hot states and their flags — <i>implemented · low · disk, startup</i></summary>

**Idea.** Clear the temporary flag on stored advanced pre-states correctly, delete a state's temporary flag whenever the state is deleted, and prune hot states older than the split slot by scanning hot state summaries. Advanced states and stale flags then do not accumulate on disk or need garbage collection at startup.

**Gap in Lighthouse.** 

**Impact.** Temporary flags no longer exist and advanced states are pruned via summary DAG at finalization, so no startup GC of ~200k states.

**Best measured result.** "Garbage collecting 223069 temporary states" at startup (problem) (pr:lighthouse#6422)

**Evidence (Lighthouse @ 928b61e719).**

- store/src/lib.rs:304-307 BeaconStateTemporary column deprecated, temporary-state flag no longer used
- beacon_chain/src/state_advance_timer.rs:455 advanced state written with put_state (gets a hot summary)
- beacon_chain/src/migrate.rs:690-795 prune_hot_db builds states_to_prune from hot summaries DAG and queues DeleteState for all not on finalized/descendant chain
- store/src/hot_cold_store.rs:1376 DeleteState removes summary + snapshot/diff

**Sources.** [lighthouse#6422](https://github.com/sigp/lighthouse/pull/6422), [lighthouse#5768](https://github.com/sigp/lighthouse/pull/5768)

</details>

<a id="db_hot-080"></a>
<details>
<summary><b>db_hot-080</b> Avoid a global or redundant store lock — <i>implemented · low · cpu, latency</i></summary>

**Idea.** Do not serialize unrelated DB operations on one global store mutex or an outer lock around an already thread-safe DB handle: remove it where atomicity is guaranteed elsewhere, or give small disk I/O paths their own lock so they do not wait behind large state writes.

**Gap in Lighthouse.** 

**Impact.** Global/redundant store lock already removed (lighthouse#7311) and small writes go directly to the DB.

**Best measured result.** state dump 420 ms p50 vs envelope 0.2-3.6 ms (contention avoided) (pr:caplin#25436)

**Evidence (Lighthouse @ 928b61e719).**

- store/src/hot_cold_store.rs:52-90 HotColdDB has no global store mutex; hot_db/cold_db/blobs_db are plain handles
- store/src/hot_cold_store.rs:1057-1064 put_payload_envelope writes straight to hot_db without a lock
- store/src/database/redb_impl.rs:14 only RwLock around redb handle (read for writes)
- store/src/hot_cold_store.rs:74-87 only cache mutexes, not held across state writes

**Sources.** [lighthouse@b3a94de08](https://github.com/sigp/lighthouse/commit/b3a94de086ae), [lighthouse#7311](https://github.com/sigp/lighthouse/pull/7311), [caplin#25436](https://github.com/erigontech/erigon/pull/25436)

</details>

<a id="db_hot-106"></a>
<details>
<summary><b>db_hot-106</b> Prune orphaned execution payload envelopes — <i>implemented · low · disk</i></summary>

**Idea.** On each finalization, delete hot-DB execution payload envelopes whose block is no longer in fork choice, since the finalized-chain walk never reaches them.

**Gap in Lighthouse.** 

**Impact.** Envelopes of abandoned blocks are deleted at each finalization together with their block.

**Best measured result.** Observed 17 stale hot envelopes on a devnet node (pr:lodestar#10206)

**Evidence (Lighthouse @ 928b61e719).**

- beacon_chain/src/migrate.rs:777 blocks_to_prune built from summaries DAG minus finalized/descendant blocks (includes forks no longer in fork choice)
- beacon_chain/src/migrate.rs:777-779 pushes DeletePayloadWithSummary per pruned block
- store/src/hot_cold_store.rs:1352-1362 DeletePayloadWithSummary removes PayloadSummary and PayloadBody (envelope)

**Sources.** [lodestar#10206](https://github.com/ChainSafe/lodestar/pull/10206)

</details>

<a id="db_hot-122"></a>
<details>
<summary><b>db_hot-122</b> Reuse computed block root when saving blocks — <i>implemented · low · S · cpu</i></summary>

**Idea.** Carry the already computed block root (a wrapper caching hash_tree_root) into the block save path instead of re-hashing the block there.

**Gap in Lighthouse.** 

**Impact.** Nothing; block root is passed by the caller already, no hash_tree_root in the save path.

**Best measured result.** FullBlock SaveBlock ROBlock -99.99% time, allocs 2069 -&gt; 1; SaveBlocks/64 -22.96% time, -38% B/op (pr:prysm#16300)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:507`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L507) put_block takes block_root: &amp;Hash256
- [`beacon_node/store/src/hot_cold_store.rs:527`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L527) block_as_kv_store_ops takes key root, no re-hashing

**Sources.** [prysm#16300](https://github.com/OffchainLabs/prysm/pull/16300)

</details>

<a id="db_hot-051"></a>
<details>
<summary><b>db_hot-051</b> Persist pending unknown-parent blocks on disk — <i>n/a · high · S · memory</i></summary>

**Idea.** Store blocks waiting for an unknown parent in the DB with only an in-memory index of roots, instead of holding full blocks in memory during long non-finality.

**Gap in Lighthouse.** 

**Impact.** Negligible; memory is already bounded.

**Best measured result.** not sustainable in memory during non-finality (pr:lodestar#1670)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/mod.rs:77`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L77) MAX_LOOKUPS=200
- [`beacon_node/network/src/sync/block_lookups/mod.rs:408`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L408) lookup rejected when at cap

**Sources.** [lodestar#1670](https://github.com/ChainSafe/lodestar/pull/1670)

</details>

<a id="db_hot-075"></a>
<details>
<summary><b>db_hot-075</b> Defer pruning until block-processing cascade ends — <i>n/a · medium · cpu</i></summary>

**Idea.** Run heavy state and block pruning only after a cascade of pending child blocks finishes processing, so states just computed for those children are not deleted and recomputed.

**Gap in Lighthouse.** Lighthouse prunes on finalization in a separate migrator thread and removes only non-viable forks and pre-finalization states, never states of pending child blocks; there is no block-processing cascade that would invalidate freshly computed states.

**Best measured result.** Fixes devnet loop at 100% CPU (pr:ethlambda#240)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/migrate.rs:310`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L310) run_migration on finalization in background thread, prune_hot_db at :509 only deletes states not descendant of finalized checkpoint

**Sources.** [ethlambda#240](https://github.com/lambdaclass/ethlambda/pull/240)

</details>

<a id="db_hot-120"></a>
<details>
<summary><b>db_hot-120</b> Move blocks hot-to-cold as raw bytes — <i>n/a · medium · cpu, latency</i></summary>

**Idea.** When migrating finalized blocks from the hot to the cold/finalized DB, copy the raw stored bytes keyed by the known root (use the DB key as root) instead of deserializing, re-hashing and re-serializing each block.

**Gap in Lighthouse.** 

**Best measured result.** Spike: doUpdate took 1522 ms (finalized 306 ms, hot 1216 ms) (pr:teku#7638)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3532`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3532) migrate_database only writes BeaconBlockRoots slot-&gt;root entries
- [`beacon_node/store/src/lib.rs:257`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/lib.rs#L257) single BeaconBlock column keyed by root

**Sources.** [teku#7672](https://github.com/Consensys-Incorporated/teku/pull/7672), [teku#7638](https://github.com/Consensys-Incorporated/teku/pull/7638), [lodestar@968f18473](https://github.com/ChainSafe/lodestar/commit/968f184732db)

</details>

<a id="db_hot-129"></a>
<details>
<summary><b>db_hot-129</b> Avoid memory-hungry DB format — <i>n/a · medium · memory, sync</i></summary>

**Idea.** A newer DB storage format made process memory grow significantly, slowing sync and causing OOM; check DB format choices for native memory growth.

**Gap in Lighthouse.** 

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/database/interface.rs:1`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/interface.rs#L1) backend is leveldb or redb, selected by feature
- [`beacon_node/store/src/database/leveldb_impl.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/leveldb_impl.rs) no format-specific cache settings found

**Sources.** [teku#3009](https://github.com/Consensys-Incorporated/teku/pull/3009)

</details>

<a id="db_hot-148"></a>
<details>
<summary><b>db_hot-148</b> Skip fork pruning with a single head — <i>n/a · medium · S · cpu, memory</i></summary>

**Idea.** Skip fork pruning at finalization when there is only one head, since it replays blocks and rebuilds tree hash caches for nothing.

**Gap in Lighthouse.** The 2020 pruning replayed blocks via head tracker; current pruning is a pure summary-DAG walk with no block replay or tree-hash cache rebuild, so the pathology no longer exists.

**Impact.** None; pruning cost is a DAG over hot summaries, small.

**Best measured result.** 5.5GB allocations in ~1 min (12.8% of total) during Witti sync; pruning vanished from the flamegraph (pr:lighthouse#1268)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/migrate.rs:509`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L509) prune_hot_db works on state summaries DAG (load_hot_state_summaries, descendants_of, ancestors_of)
- [`beacon_node/beacon_chain/src/migrate.rs:372`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L372) call site

**Sources.** [lighthouse#1268](https://github.com/sigp/lighthouse/pull/1268)

</details>

<a id="db_hot-153"></a>
<details>
<summary><b>db_hot-153</b> Smaller in-memory block cache — <i>n/a · medium · S · memory</i></summary>

**Idea.** Size the in-memory block cache to about one epoch of blocks since post-merge blocks are much larger, reducing heap pressure.

**Gap in Lighthouse.** Lighthouse's DB block cache is off by default, so there is no large block cache to shrink.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/config.rs:22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L22) DEFAULT_BLOCK_CACHE_SIZE = 0
- [`beacon_node/store/src/hot_cold_store.rs:229`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L229) cache only created if size &gt; 0
- [`beacon_node/src/cli.rs:790`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L790) --block-cache-size default 0

**Sources.** [teku#6217](https://github.com/Consensys-Incorporated/teku/pull/6217)

</details>

<a id="db_hot-162"></a>
<details>
<summary><b>db_hot-162</b> Validator entry dedup cache hits on state save — <i>n/a · medium · S · cpu, disk</i></summary>

**Idea.** Make the validator-entry cache used for deduplicated validator storage hit, so state saves do not re-read or re-hash the validator list.

**Gap in Lighthouse.** Lighthouse stores states as snapshots plus hierarchical diffs where the validator list is an append-only diff, not a per-validator content-addressed store, so there is no validator-entry cache to miss.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hdiff.rs:131-143`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L131-L143) validators handled as append-only diff, no per-validator dedup store
- [`beacon_node/store/src/hot_cold_store.rs:2148`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2148) hot state saved as snapshot or HDiff

**Sources.** [prysm#9310](https://github.com/OffchainLabs/prysm/pull/9310)

</details>

<a id="db_hot-066"></a>
<details>
<summary><b>db_hot-066</b> Epoch-keyed blob directory layout with summary — <i>n/a · low · startup, disk</i></summary>

**Idea.** Lay out blob files as period/epoch/root/index and keep an in-memory summary per block root (epoch plus index mask), so startup warmup and pruning list epoch directories instead of reading every sidecar.

**Gap in Lighthouse.** 

**Impact.** Blobs/columns live in a KV database (no file tree), there is no startup cache warm-up and pruning only visits the newly expired range, so a directory layout does not apply.

**Best measured result.** order of magnitude faster cache warm up time and sub-ms pruning times (pr:prysm#14023)

**Evidence (Lighthouse @ 928b61e719).**

- store/src/hot_cold_store.rs:3340-3430 prune_blobs walks back from end block until an already-pruned block, only touching newly expired blocks
- store/src/lib.rs:259 BeaconBlob column in KV DB keyed by block root

**Sources.** [prysm#14023](https://github.com/OffchainLabs/prysm/pull/14023)

</details>

<a id="db_hot-089"></a>
<details>
<summary><b>db_hot-089</b> Run metric column scans off the pruning path — <i>n/a · low · latency, disk</i></summary>

**Idea.** Run full O(N) column count scans used only for metrics on a separate low-priority task, not at the end of the pruning cycle, so pruning is not delayed by minutes.

**Gap in Lighthouse.** 

**Impact.** Lighthouse does not run O(N) column-count scans for metrics, so there is nothing to move off the pruning path.

**Best measured result.** scans "can take minutes on large databases" (pr:teku#11171)

**Evidence (Lighthouse @ 928b61e719).**

- store/src/hot_cold_store.rs:456-506 store metrics set only in-memory gauges (caches, anchor info)
- beacon_chain/src/migrate.rs: no column count scans at end of pruning

**Sources.** [teku#11171](https://github.com/Consensys-Incorporated/teku/pull/11171)

</details>

<a id="db_hot-126"></a>
<details>
<summary><b>db_hot-126</b> Avoid blinded-block storage layout — <i>n/a · low · S · latency, disk</i></summary>

**Idea.** Teku found storing blinded blocks (payload separated) slower than full blocks and dropped it, managing size by block pruning instead; check whether the blinded layout costs read performance.

**Gap in Lighthouse.** 

**Impact.** Lighthouse deliberately stores blinded blocks with payloads in a separate column; the Teku finding is a design-level tradeoff and changing it would be a storage redesign. Idea is only a check, no change implied.

**Best measured result.** PR states it showed worse performance (pr:teku#6617)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:533`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L533) blocks are split into blinded block plus separate payload and stored blinded

**Sources.** [teku#6617](https://github.com/Consensys-Incorporated/teku/pull/6617)

</details>

