# db_cold

75 checked ideas, 18 actionable. [Back to the summary](../README.md).

## Actionable (18)

High or medium value, verdict `not` or `partial`.

<a id="db_cold-063"></a>
<details>
<summary><b>db_cold-063</b> Store base columns plus proofs, reconstruct extensions — <i>not · high · L · disk</i></summary>

**Idea.** For finalized data column sidecars, keep only the base half of the columns plus the KZG proofs of the extension columns, and reconstruct the extension half on demand via erasure coding. This roughly halves column storage.

**Gap in Lighthouse.** Supernodes store all 128 columns. Store the base half plus extension-column KZG proofs after finalization and rebuild the extension half on read (reuse the data availability checker reconstruction) in the get_data_column / by-range / by-root serving paths.

**Impact.** About half of supernode column storage (Teku: 508 GB to 260 GB at 14 blobs); CPU cost on serving extension columns; supernodes only.

**Best measured result.** 508 GB to ~259.67 GB for 14 target blobs supernode (pr:teku#10137)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:8411`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L8411) supernodes skip the custody retain and persist every column
- [`beacon_node/store/src/hot_cold_store.rs:985`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L985) put_data_columns writes each full DataColumnSidecar as SSZ
- [`beacon_node/store/src/hot_cold_store.rs:2679`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2679) get_data_column reads stored bytes only, no reconstruction on read

**Second check.** Checked the import path that chooses which columns to store (beacon_chain.rs block_data_to_store) and searched store and beacon_chain for any reconstruct-on-read or half-column storage; none found.

**Sources.** [teku#11250](https://github.com/Consensys-Incorporated/teku/pull/11250), [teku#10137](https://github.com/Consensys-Incorporated/teku/pull/10137)

</details>

<a id="db_cold-002"></a>
<details>
<summary><b>db_cold-002</b> Import and export ERA files for history — <i>not · medium · L · sync, startup, disk</i></summary>

**Idea.** Populate a fresh node's historical blocks and states from ERA files (and export them), replaying states only at boundaries, instead of backfilling history over the network.

**Gap in Lighthouse.** Add an e2store/ERA reader and writer and a database_manager import-era/export-era command that writes blocks and stores states at era boundaries. PR lighthouse#9273 is not merged in this checkout.

**Impact.** Fresh-node history from files instead of network backfill; no steady-state saving.

**Evidence (Lighthouse @ 928b61e719).**

- grep for era file / e2store / EraFile / .era across all .rs and .toml in the checkout and Cargo.lock: no matches
- [`database_manager/src/cli.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/database_manager/src/cli.rs): only hierarchy and prune/compact style subcommands, no era import/export

**Second check.** Searched the source and Cargo.lock for any ERA or e2store crate dependency and the database_manager CLI; nothing present.

**Sources.** [lighthouse#9273](https://github.com/sigp/lighthouse/pull/9273)

</details>

<a id="db_cold-003"></a>
<details>
<summary><b>db_cold-003</b> Compress finalized blocks in a slot-ordered freezer column — <i>not · medium · M · disk, bandwidth</i></summary>

**Idea.** Move finalized beacon blocks into a cold/freezer column or snapshot files keyed and ordered by slot, compressed (for example LZ4, zstd or snappy, per block or chunk). Compressed linear history takes less disk, is faster for slot-range reads and simpler to prune.

**Gap in Lighthouse.** Add a slot-keyed freezer block column with zstd-compressed (per block or chunk) blinded blocks, written in migrate_database and read by forwards iteration and by-range serving; delete from BeaconBlock after migration. A cheaper partial step is enabling LevelDB snappy compression.

**Impact.** Finalized blinded block history (100+ GB on mainnet) could shrink about 30-40% and by-range reads become sequential.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/database/leveldb_impl.rs:37`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/leveldb_impl.rs#L37) Options::new() with no compression set
- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/leveldb-0.8.6/src/database/options.rs:72 default compression: Compression::No
- [`beacon_node/store/Cargo.toml:22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/Cargo.toml#L22) leveldb with default-features = false (snappy feature of leveldb-sys not enabled)
- [`beacon_node/store/src/config.rs:198`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L198) compress_bytes (zstd) used only by hdiff.rs:402/529 and state snapshots
- [`beacon_node/store/src/lib.rs:257`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/lib.rs#L257) single root-keyed BeaconBlock column; freezer only holds BeaconBlockRoots (lib.rs:351)

**Second check.** Went further than the earlier review: checked whether LevelDB block-level compression gives this implicitly. The leveldb crate defaults to Compression::No and Lighthouse does not change it, so blocks are stored uncompressed (only blinded).

**Sources.** [caplin#8609](https://github.com/erigontech/erigon/pull/8609), [lighthouse#3583](https://github.com/sigp/lighthouse/pull/3583), [lighthouse#5905](https://github.com/sigp/lighthouse/pull/5905)

</details>

<a id="db_cold-008"></a>
<details>
<summary><b>db_cold-008</b> Finalized history in append-only indexed flat files — <i>not · medium · L · disk, sync, startup, memory, bandwidth</i></summary>

**Idea.** Store finalized history (blocks, sidecars) in immutable append-only flat files (e2store/era style or snapshot segments) with an offset/length index per slot instead of a key-value store. Reads by slot need no DB, bulk import needs one fsync per batch, and write amplification is lower.

**Gap in Lighthouse.** Add an append-only slot-indexed flat-file store (e2store/era or segment style, as in PR 9644) for finalized blocks and sidecars, and wire migrate_database and historical block import/backfill to it.

**Impact.** Cheaper ERA/backfill import, lower write amplification and DB size on archive-like nodes; no effect on head import.

**Best measured result.** described as a large ERA-import speedup measured in a downstream prototype, no numbers (pr:lighthouse#9644)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/lib.rs:246-260`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/lib.rs#L246-L260) all cold blocks/blobs/columns are KV columns
- [`beacon_node/store/src/database`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database)/ contains only interface.rs, leveldb_impl.rs, redb_impl.rs
- Cargo.lock: no era/e2store/static-file/segment crate

**Second check.** Searched the whole tree and Cargo.lock for era/e2store/static-file/segment code and crates; none present, only leveldb and redb backends.

**Sources.** [nimbus#820](https://github.com/status-im/nimbus-eth2/pull/820), [lighthouse#9644](https://github.com/sigp/lighthouse/pull/9644), [caplin#8357](https://github.com/erigontech/erigon/pull/8357), [teku#10281](https://github.com/Consensys-Incorporated/teku/pull/10281), [nimbus#1355](https://github.com/status-im/nimbus-eth2/pull/1355), [caplin#8570](https://github.com/erigontech/erigon/pull/8570)

</details>

<a id="db_cold-056"></a>
<details>
<summary><b>db_cold-056</b> Defer post-finalization archival within slot — <i>not · medium · S · latency</i></summary>

**Idea.** Schedule block/state archival triggered by finalization later in the slot instead of at slot start, so it does not contend with time-critical duties.

**Gap in Lighthouse.** The migrator thread loop has no in-slot scheduling. Add a slot-clock wait (for example, until after the attestation deadline) before the migration runs in Migrator::spawn_thread.

**Impact.** Less DB write and lock contention with block import and attestation duties near the epoch boundary. The gain is probably small because the work already runs on its own thread.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:1725-1735`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1725-L1735) after_finalization sends Finalization and PruneBlobs to the migrator at once
- [`beacon_node/beacon_chain/src/migrate.rs:436-500`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L436-L500) migrator thread does rx.recv() and runs at once (it only coalesces queued notifications), with no slot clock or delay

**Second check.** Read the whole migrator thread loop and the after_finalization path, and grepped migrate.rs for slot_clock, sleep and delay. The only batching is notification coalescing, and there is no time-of-slot deferral.

**Sources.** [grandine#605](https://github.com/grandinetech/grandine/pull/605), [grandine@c3d66409a](https://github.com/grandinetech/grandine/commit/c3d66409a6a0)

</details>

<a id="db_cold-090"></a>
<details>
<summary><b>db_cold-090</b> Store data column sidecars as flat files — <i>not · medium · L · disk, cpu</i></summary>

**Idea.** Store data column sidecars as flat files outside the KV DB (for example all columns of a block in one file with an offset table, in epoch directories), and prune by deleting whole files or directories. This avoids DB compaction and inode exhaustion and allows partial column reads.

**Gap in Lighthouse.** No flat-file sidecar store. Add a per-epoch directory file store (one file per block with offset table) behind put_data_columns/get_data_column/prune paths in hot_cold_store, replacing the BeaconDataColumn KV column in blobs_db; prune by unlinking epoch dirs.

**Impact.** Removes per-key deletes and leveldb/redb compaction on the blob DB; enables partial column reads. Lighthouse already isolates columns in a separate blobs_db, so compaction does not touch hot/cold state DBs; real gain is uncertain.

**Best measured result.** "over 16 million files" with old design (pr:prysm#15061)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/lib.rs:144`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/lib.rs#L144) get_data_column_key = block_root ++ column index KV key
- [`beacon_node/store/src/lib.rs:261`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/lib.rs#L261) DBColumn::BeaconDataColumn
- [`beacon_node/store/src/hot_cold_store.rs:275`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L275) blobs_db is a separate BeaconNodeBackend (leveldb/redb) instance
- [`beacon_node/store/src/hot_cold_store.rs:1353`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1353) per-key DeleteKey on prune
- [`beacon_node/store/src/hot_cold_store.rs:3398`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3398) pruning iterates per-column keys

**Second check.** Checked store/src/database (only leveldb_impl, redb_impl), all fs::create_dir_all/File writes in beacon_node (only debug SSZ dumps and network dirs), and the blob pruning path. Only related mechanism is the separate blobs_db KV instance, which is not a flat-file store.

**Sources.** [lodestar#8899](https://github.com/ChainSafe/lodestar/pull/8899), [prysm#15061](https://github.com/OffchainLabs/prysm/pull/15061), [teku#10287](https://github.com/Consensys-Incorporated/teku/pull/10287)

</details>

<a id="db_cold-128"></a>
<details>
<summary><b>db_cold-128</b> Prune contiguous key ranges with one range delete — <i>not · medium · L · disk, cpu</i></summary>

**Idea.** When pruning finalized data (blocks, signatures, states, data columns), lay keys out so the doomed rows form one contiguous range and delete it with a single range-delete instead of iterating and deleting key by key. One tombstone replaces thousands, so pruning cost stops scaling with chain height and later seeks do not crawl over tombstones.

**Gap in Lighthouse.** No DeleteRange op in KeyValueStoreOp or in either backend (C LevelDB has no native DeleteRange; redb has range-based retain_in/extract_from_if). Blob/column keys are by block root, so a range delete also needs slot-prefixed keys.

**Impact.** Fewer tombstones and less compaction during blob/column and state pruning; small steady-state saving.

**Best measured result.** States grew ~150 MiB per snapshot, ~33 GiB/day, previously never pruned (pr:ethlambda#683)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/lib.rs:99`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/lib.rs#L99) KeyValueStore only has delete_batch(HashSet keys) and delete_if, no range delete
- [`beacon_node/store/src/database/leveldb_impl.rs:262`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/leveldb_impl.rs#L262) delete_batch writes one tombstone per key
- [`beacon_node/store/src/database/leveldb_impl.rs:272`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/leveldb_impl.rs#L272) delete_if scans the whole column and deletes matching keys one by one
- [`beacon_node/store/src/database/redb_impl.rs:284`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/redb_impl.rs#L284) redb delete_batch uses table.retain over all keys
- [`beacon_node/store/src/hot_cold_store.rs:3277`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3277) try_prune_blobs per-key deletes

**Second check.** Also checked delete_if in leveldb/redb/memory backends and its callers: it is a full-column scan with per-key deletes, not a range delete.

**Sources.** [ethlambda#548](https://github.com/lambdaclass/ethlambda/pull/548), [ethlambda#683](https://github.com/lambdaclass/ethlambda/pull/683), [nimbus#8283](https://github.com/status-im/nimbus-eth2/pull/8283)

</details>

<a id="db_cold-143"></a>
<details>
<summary><b>db_cold-143</b> Independent retention mode for data columns — <i>not · medium · S · disk</i></summary>

**Idea.** Give data column sidecars their own retention/archive setting separate from blocks, since columns take an order of magnitude more disk and are not needed for consensus.

**Gap in Lighthouse.** Add a separate column retention setting (prune flag or retention epochs) and use it in the Fulu branch of try_prune_blobs.

**Impact.** Operators can keep or drop columns independently of blobs; disk saving only.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/config.rs:61`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L61) one prune_blobs bool
- [`beacon_node/store/src/config.rs:63`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L63) one epochs_per_blob_prune and blob_prune_margin_epochs shared by blobs and columns
- [`beacon_node/src/cli.rs:1046`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L1046) single --prune-blobs flag
- [`beacon_node/src/cli.rs:52`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L52) supernode/semi-supernode only change custody count, not retention

**Second check.** Checked all store config fields and CLI flags for column-specific retention; only custody-count flags (supernode/semi-supernode) affect column disk usage, which is not a retention mode.

**Sources.** [nimbus#9110](https://github.com/status-im/nimbus-eth2/pull/9110)

</details>

<a id="db_cold-148"></a>
<details>
<summary><b>db_cold-148</b> Serve historical blocks from ERA files — <i>not · medium · L · disk, sync, startup</i></summary>

**Idea.** Read historical/finalized blocks (and the checkpoint state) directly from ERA files with an index instead of importing them into the DB or downloading a checkpoint, saving DB storage.

**Gap in Lighthouse.** Needs an ERA (e2store) reader with index and a fallback block/state source in HotColdDB and backfill/checkpoint loading.

**Impact.** Could avoid storing/backfilling historical blocks (hundreds of GB) and speed up initial backfill.

**Evidence (Lighthouse @ 928b61e719).**

- no e2store/era/era1 crate in Cargo.lock and no ERA reader in any .rs file (grep)
- [`beacon_node/beacon_chain/src/historical_blocks.rs:84`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_blocks.rs#L84) import_historical_block_batch only imports network batches

**Second check.** Searched the whole tree and Cargo.lock for era/e2store/era1 names and dependency crates; none present.

**Sources.** [lodestar#8666](https://github.com/ChainSafe/lodestar/pull/8666), [nimbus#7888](https://github.com/status-im/nimbus-eth2/pull/7888)

</details>

<a id="db_cold-163"></a>
<details>
<summary><b>db_cold-163</b> Copy only needed fields when computing state diffs — <i>not · medium · S · memory, cpu</i></summary>

**Idea.** When computing a state diff, keep only the fields needed from the previous state (e.g. packed effective balances, a per-validator bitmap) and encode the diff in one pass, instead of holding two full states or copying full lists and building intermediate deltas.

**Gap in Lighthouse.** Lighthouse's diff format covers every Validator field, so it needs the full validator records (the Caplin effective-balance-only extraction does not map onto it). What does remain: stream the per-field deltas directly into the zstd Encoder instead of materialising uncompressed_bytes, and avoid to_vec copies of milhouse lists where iterating the source directly would do. Diffs run only at hdiff layer points, not every slot.

**Impact.** Low: a few tens of MB of transient allocation and some ms per hdiff layer write on mainnet; not a per-slot cost as in Caplin.

**Best measured result.** Copy 266MB -&gt; 17.6MB; per-epoch machinery 157ms -&gt; ~94ms (pr:caplin#22411)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hdiff.rs:173`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L173) HDiffBuffer::from_state copies the whole validators/balances/inactivity lists with to_vec and keeps the full remaining state as SSZ bytes
- [`beacon_node/store/src/hdiff.rs:253`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L253) HDiff::compute takes two full HDiffBuffers (source and target)
- [`beacon_node/store/src/hdiff.rs:390`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L390) CompressedU64Diff builds a full intermediate uncompressed delta Vec before zstd
- [`beacon_node/store/src/hdiff.rs:448`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L448) ValidatorsDiff builds an intermediate byte Vec, then compresses (line 529)
- [`beacon_node/store/src/state_cache.rs:173`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L173) buffers are cached as full HDiffBuffers

**Second check.** Read HDiff::compute, CompressedU64Diff/ValidatorsDiff compute, HDiffBuffer::from_state and the state_cache buffer paths, and compared them with caplin#22411, nimbus#4986 and prysm#17587. Lighthouse holds decomposed buffers rather than BeaconStates, but it still copies the full lists and makes a two-pass intermediate, so 'not' stands.

**Sources.** [nimbus#4986](https://github.com/status-im/nimbus-eth2/pull/4986), [caplin#22411](https://github.com/erigontech/erigon/pull/22411), [prysm#17587](https://github.com/OffchainLabs/prysm/pull/17587)

</details>

<a id="db_cold-004"></a>
<details>
<summary><b>db_cold-004</b> Slot-keyed finalized block archive with root and parent indexes — <i>partial · medium · M · disk, latency, startup, memory</i></summary>

**Idea.** Since finalized history is linear, store finalized blocks/block roots in a slot-keyed table with secondary indexes (block root to slot, parent root to slot). Range requests, startup chain loading and lookups by root, parent root or slot become point reads or sequential range seeks instead of scans or parent walks.

**Gap in Lighthouse.** Finalized slot-&gt;root is a slot-keyed range-seekable column, and blocks are point reads by root (root-&gt;slot via the block's own slot field). There is no root-&gt;slot or parent_root-&gt;slot secondary index and no slot-keyed block table; parent lookups use fork choice (non-finalized) or block bodies.

**Impact.** Small: range requests already do slot-&gt;root then point reads, and startup loads persisted fork choice instead of scanning, so the measured nimbus/lodestar startup gains do not apply.

**Best measured result.** mainnet startup 3-5x faster (3s on laptop) (pr:nimbus#3320)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/lib.rs:345-351`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/lib.rs#L345-L351) BeaconBlockRoots slot-&gt;root column in freezer
- [`beacon_node/store/src/hot_cold_store.rs:3574-3580`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3574-L3580) migration writes be-slot -&gt; block root
- [`beacon_node/store/src/hot_cold_store.rs:1219-1247`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1219-L1247) forwards_block_roots_iterator reads BeaconBlockRoots by slot range
- [`beacon_node/store/src/lib.rs:251-257`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/lib.rs#L251-L257) BeaconBlock keyed by root; doc says cold value is 8-byte slot but no cold_db write of BeaconBlock exists (stale doc)

**Second check.** Checked the BeaconBlock column doc claiming a cold root-&gt;slot value; grep found no cold_db write to BeaconBlock, so it is not a live index. Confirmed startup uses persisted ForkChoice column rather than a chain scan.

**Sources.** [caplin#8043](https://github.com/erigontech/erigon/pull/8043), [lodestar@8d3c0182c](https://github.com/ChainSafe/lodestar/commit/8d3c0182cdee), [caplin#6460](https://github.com/erigontech/erigon/pull/6460), [lodestar@69f4864a9](https://github.com/ChainSafe/lodestar/commit/69f4864a9d17), [lodestar@ba8ac4509](https://github.com/ChainSafe/lodestar/commit/ba8ac45099fd), [lodestar#523](https://github.com/ChainSafe/lodestar/pull/523), [nimbus#3320](https://github.com/status-im/nimbus-eth2/pull/3320), [lodestar@ed060f747](https://github.com/ChainSafe/lodestar/commit/ed060f747118), [teku#2205](https://github.com/Consensys-Incorporated/teku/pull/2205)

</details>

<a id="db_cold-013"></a>
<details>
<summary><b>db_cold-013</b> Asynchronous storage IO off import path — <i>partial · medium · L · latency, disk</i></summary>

**Idea.** Run DB reads and writes asynchronously on dedicated threads by default so storage IO does not block block import or other threads.

**Gap in Lighthouse.** DB IO never blocks the async runtime (blocking workers, dedicated migrator thread) and hot writes skip fsync, but block/state writes are still on the import critical path while holding the fork choice write lock; no write-behind queue in HotColdDB.

**Impact.** Modest: removing the write from the import path would shorten fork-choice lock hold time, but Lighthouse deliberately orders DB write before lock release for consistency (issue 2028).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:4426-4441`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4426-L4441) import_block runs in spawn_blocking_handle
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4750-4762`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4750-L4762) block+state DB write is synchronous inside import, under the fork choice write lock
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4764-4766`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4764-L4766) fork choice lock dropped only after DB write, by design
- [`beacon_node/store/src/database/leveldb_impl.rs:50-57`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/leveldb_impl.rs#L50-L57) default writes are non-fsync (sync only for split/migration)
- [`beacon_node/beacon_processor/src/lib.rs:747-748`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L747-L748) all processor work, incl. DB reads for RPC, on spawn_blocking workers
- [`beacon_node/beacon_chain/src/migrate.rs:434`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L434) finalization migration on a dedicated thread

**Second check.** Checked import_block ordering, leveldb WriteOptions sync defaults and beacon_processor threading; found no async/write-behind storage layer in store or dependencies.

**Sources.** [teku#6218](https://github.com/Consensys-Incorporated/teku/pull/6218), [teku#6222](https://github.com/Consensys-Incorporated/teku/pull/6222)

</details>

<a id="db_cold-028"></a>
<details>
<summary><b>db_cold-028</b> Bound the size of storage write and migration batches — <i>partial · medium · S · latency, disk, memory</i></summary>

**Idea.** Split large finalization writes, block archival/migration, deletions, snapshot indexing and pruning into bounded batches (fixed block count, chunks of epochs or a time budget) with commits in between, instead of one huge transaction. Memory stays bounded and a single transaction does not hold the writer lock or stall the node.

**Gap in Lighthouse.** Only state reconstruction has a bound. Chunk prune_hot_db, try_prune_blobs, migrate_database and prune_historic_states: flush every N ops or N slots, and update DataInfo/AnchorInfo after each chunk.

**Impact.** At steady state each run handles about one epoch, so batches are already small. A bound prevents memory spikes and long write stalls after long non-finality, a long catch-up, re-enabled blob pruning, or a prune-states run.

**Best measured result.** 5000 blocks per 15 min; ~66x arrival rate (pr:teku#7483)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/migrate.rs:29`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L29) BLOCKS_PER_RECONSTRUCTION=1024, the only bounded batch (used at migrate.rs:225)
- [`beacon_node/beacon_chain/src/migrate.rs:32`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L32) DEFAULT_EPOCHS_PER_MIGRATION=1 sets how often migration runs, not a cap on batch size
- [`beacon_node/store/src/hot_cold_store.rs:3356`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3356) try_prune_blobs puts every delete in one blobs_db_ops Vec, committed at 3469 in one do_atomically
- [`beacon_node/store/src/hot_cold_store.rs:3491`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3491) prune_historic_states puts every freezer key in one cold_ops Vec, committed at 3517 in one do_atomically
- [`beacon_node/store/src/database/leveldb_impl.rs:143`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/leveldb_impl.rs#L143) do_atomically builds one Writebatch for the whole op list (and delete_if at 272 does the same)

**Second check.** I also checked prune_historic_states, the leveldb do_atomically/delete_if/delete_batch paths, and the epochs_per_migration and epochs_per_blob_prune configs. None of them split a batch, so the earlier partial verdict stands.

**Sources.** [teku#3143](https://github.com/Consensys-Incorporated/teku/pull/3143), [teku#6597](https://github.com/Consensys-Incorporated/teku/pull/6597), [caplin#21594](https://github.com/erigontech/erigon/pull/21594), [grandine@a0ef64e37](https://github.com/grandinetech/grandine/commit/a0ef64e37522), [grandine#650](https://github.com/grandinetech/grandine/pull/650), [teku#7483](https://github.com/Consensys-Incorporated/teku/pull/7483), [prysm#15746](https://github.com/OffchainLabs/prysm/pull/15746), [caplin#11723](https://github.com/erigontech/erigon/pull/11723), [prysm#9298](https://github.com/OffchainLabs/prysm/pull/9298), [lodestar@b504f7815](https://github.com/ChainSafe/lodestar/commit/b504f7815a2d)

</details>

<a id="db_cold-030"></a>
<details>
<summary><b>db_cold-030</b> Big-endian slot-prefixed keys for ordered seeks — <i>partial · medium · L · disk, latency, cpu</i></summary>

**Idea.** Encode slot/epoch as a big-endian key prefix (then root, index) in prunable tables so key order equals slot order. Pruning and range queries seek directly to the cutoff slot and stream in order, instead of scanning from the table start or looking up headers per row.

**Gap in Lighthouse.** Most of the history is in big-endian slot-ordered keys with seek-based range reads (freezer roots, snapshots, diffs, LC updates). The prunable blob/column tables and the hot block/state tables are still keyed by root. Pruning them needs a block load plus up to 128 key_exists checks per block, not a seek and range delete. A slot prefix or a slot-&gt;root index needs a schema migration (store/src/metadata.rs) and changes to the BeaconBlob/BeaconDataColumn get/put paths.

**Impact.** Small at steady state: about 32 block loads per prune run, each with column key_exists checks. It matters more when catching up after pruning was off. The query side already gets ordered seeks for the freezer.

**Best measured result.** Requests tested under 2s per state regen from cold checkpoint (pr:prysm#6461)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/forwards_iter.rs:138`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/forwards_iter.rs#L138) freezer forwards iterator seeks with iter_column_from to a big-endian start slot
- [`beacon_node/store/src/hot_cold_store.rs:3086`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3086),3099,3112 BeaconBlockRoots and BeaconStateRoots are keyed by big-endian slot
- [`beacon_node/store/src/hot_cold_store.rs:2161`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2161),2170,2411 BeaconStateSnapshot and BeaconStateDiff are keyed by big-endian slot
- [`beacon_node/store/src/hot_cold_store.rs:865`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L865) LightClientUpdate is keyed by big-endian period, and range queries seek to start_period and stream in order
- [`beacon_node/store/src/hot_cold_store.rs:3328`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3328) try_prune_blobs uses the slot-keyed freezer block roots to seek to end_slot, walks back, and stops at the first block already pruned (3449), so it does not scan from the table start
- [`beacon_node/store/src/lib.rs:144`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/lib.rs#L144) BeaconBlob/BeaconDataColumn keys are block_root \|\| column_index, with no slot prefix

**Second check.** I searched for to_be_bytes and iter_column_from across the store. The mechanism (big-endian slot keys, seek to the cutoff, stream in order) exists for the freezer and LC-update tables, and blob pruning uses it to find its start point. Only the root-keyed prunable tables lack it, so I upgraded the verdict to partial.

**Sources.** [prysm#14151](https://github.com/OffchainLabs/prysm/pull/14151), [prysm#6461](https://github.com/OffchainLabs/prysm/pull/6461), [teku#10725](https://github.com/Consensys-Incorporated/teku/pull/10725), [ethlambda#453](https://github.com/lambdaclass/ethlambda/pull/453), [teku#6910](https://github.com/Consensys-Incorporated/teku/pull/6910)

</details>

<a id="db_cold-041"></a>
<details>
<summary><b>db_cold-041</b> Compact DB key ranges after large prunes — <i>partial · medium · S · disk, startup, latency</i></summary>

**Idea.** After finalization pruning, historic-state pruning or a large key-range delete, compact the affected (freezer) columns or force bottom-level compaction over that range. Deleted data is then physically reclaimed and later scans do not walk tombstones.

**Gap in Lighthouse.** On the default LevelDB backend, automatic compaction after a prune covers only BeaconStateHotSummary (hot) and four freezer state columns after historic-state pruning. Hot state snapshot/diff columns, blocks, and blob/data-column deletions in blobs_db (try_prune_blobs) never get a targeted compaction, except through the manual database_manager compact or LevelDB background compaction.

**Impact.** Disk reclaim and fewer tombstones in blob/column and hot-state ranges after large prunes; small CPU effect on a steady-state node.

**Best measured result.** startup 20 min to 3 ms; lookup 712 s; range 224.8 GB to 0 (pr:lodestar#10460)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/migrate.rs:410-417`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L410-L417) run_compaction after every finalization prune (rate limited, compact_on_prune default true per store/src/config.rs:116)
- [`beacon_node/store/src/database/leveldb_impl.rs:172-189`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/leveldb_impl.rs#L172-L189) LevelDB compact() only covers BeaconStateHotSummary, overriding the trait default at store/src/lib.rs:77-83 that also covers BeaconBlock
- [`beacon_node/store/src/database/redb_impl.rs:195-199`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/redb_impl.rs#L195-L199) redb backend compacts the whole file
- [`beacon_node/store/src/hot_cold_store.rs:3036-3050`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3036-L3050) compact_freezer after prune_historic_states (3521)
- [`beacon_node/store/src/hot_cold_store.rs:388-392`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L388-L392) compact_on_init
- [`database_manager/src/lib.rs:256-286`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/database_manager/src/lib.rs#L256-L286) manual per-column compaction incl. blobs_db and freezer
- [`beacon_node/http_api/src/lib.rs:2897`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L2897) POST lighthouse/compaction

**Second check.** Also checked the redb backend (whole-DB compact, so it covers this on redb), the unused trait-default compact with BeaconBlock, the compact_on_init option, and the db-manager and HTTP manual compaction paths. None compacts blobs_db or hot state columns automatically on LevelDB.

**Sources.** [lighthouse#5142](https://github.com/sigp/lighthouse/pull/5142), [lighthouse#1871](https://github.com/sigp/lighthouse/pull/1871), [lighthouse#6667](https://github.com/sigp/lighthouse/pull/6667), [lodestar#10460](https://github.com/ChainSafe/lodestar/pull/10460)

</details>

<a id="db_cold-055"></a>
<details>
<summary><b>db_cold-055</b> Prune blocks and states older than the retention window — <i>partial · medium · M · disk</i></summary>

**Idea.** By default (unless archive mode), continuously delete finalized blocks, states and similar large tables older than a retention window (MIN_EPOCHS_FOR_BLOCK_REQUESTS, weak subjectivity period or a fixed count), at finalization or in a background job. The database stays roughly constant size instead of growing without bound.

**Gap in Lighthouse.** Payloads, blobs, columns and hot states are pruned. Finalized blinded blocks and freezer state snapshots/diffs stored after the split are never deleted on a retention window. The only freezer-state pruning is the manual prune-states command, which deletes all of them. Add an automatic retention pass that deletes old BeaconBlock and cold state entries and moves the anchor forward.

**Impact.** Database growth of non-archive nodes would be bounded; little runtime effect.

**Best measured result.** caps database usage at around 60-70gb (pr:nimbus#4445)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3119`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3119) try_prune_execution_payloads (called at startup, beacon_chain/src/builder.rs:1168), blocks are kept in blinded form
- [`beacon_node/store/src/hot_cold_store.rs:3277`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3277) try_prune_blobs runs in the background on finalization (beacon_chain/src/canonical_head.rs:1731-1735)
- [`beacon_node/store/src/hot_cold_store.rs:3471`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3471) prune_historic_states deletes freezer states, only from [`database_manager/src/lib.rs:458`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/database_manager/src/lib.rs#L458) (manual)
- [`beacon_node/beacon_chain/src/migrate.rs:640-760`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L640-L760) hot DB pruning of non-canonical states and blocks

**Second check.** Searched for block or history retention pruning under other names (prune_blocks, history, retention, anchor updates) and traced prune_historic_states and payload pruning callers. Only manual or payload-level pruning exists. Nothing removes old blocks automatically.

**Sources.** [prysm#2433](https://github.com/OffchainLabs/prysm/pull/2433), [nimbus@503cde366](https://github.com/status-im/nimbus-eth2/commit/503cde366c59), [lighthouse#4158](https://github.com/sigp/lighthouse/pull/4158), [nimbus#4445](https://github.com/status-im/nimbus-eth2/pull/4445), [prysm#14687](https://github.com/OffchainLabs/prysm/pull/14687), [teku#6582](https://github.com/Consensys-Incorporated/teku/pull/6582), [caplin#8058](https://github.com/erigontech/erigon/pull/8058), [lodestar#7427](https://github.com/ChainSafe/lodestar/pull/7427), [lodestar#8547](https://github.com/ChainSafe/lodestar/pull/8547), [grandine#92](https://github.com/grandinetech/grandine/pull/92), [teku#6590](https://github.com/Consensys-Incorporated/teku/pull/6590), [caplin#8198](https://github.com/erigontech/erigon/pull/8198), [ethlambda#170](https://github.com/lambdaclass/ethlambda/pull/170), [silver#75](https://github.com/gattaca-com/silver/pull/75)

</details>

<a id="db_cold-147"></a>
<details>
<summary><b>db_cold-147</b> Throttle peer-driven chain data DB queries — <i>partial · medium · S · latency, disk</i></summary>

**Idea.** Wrap the chain-data DB client with a concurrency limiter so heavy RPC/peer requests cannot starve the node's own storage access.

**Gap in Lighthouse.** Peer-driven DB reads are bounded indirectly (per-peer concurrency 2, rate quotas, global max_workers shared with own work, low-priority queues), but there is no dedicated limiter that reserves storage capacity for the node's own access; add a semaphore around store reads in the by-range/by-root handlers.

**Impact.** Marginal: less DB contention during heavy peer serving.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/mod.rs:51`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/mod.rs#L51) MAX_CONCURRENT_REQUESTS = 2 per peer and protocol
- [`beacon_node/lighthouse_network/src/rpc/inbound_limiter.rs:126`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/inbound_limiter.rs#L126) rejects inbound requests over the per-peer concurrency limit
- [`beacon_node/beacon_processor/src/lib.rs:1715`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1715) by-range/by-root handlers run as beacon processor work
- [`beacon_node/beacon_processor/src/lib.rs:1776`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1776) spawn_async/spawn_blocking hold the worker slot (SendOnDrop) until the DB read finishes, so total peer-serving concurrency is bounded by max_workers

**Second check.** Found the per-peer inbound concurrency limiter and confirmed beacon processor worker slots are held for the whole request, which is an indirect global cap; still no DB-level limiter.

**Sources.** [teku#6937](https://github.com/Consensys-Incorporated/teku/pull/6937)

</details>

<a id="db_cold-165"></a>
<details>
<summary><b>db_cold-165</b> Snappy-compress stored states and blocks — <i>partial · medium · M · disk, sync</i></summary>

**Idea.** Compress states (including full snapshots) and blocks with snappy before writing them to the DB and decompress on read, cutting disk size and read I/O.

**Gap in Lighthouse.** All state storage (hot and cold snapshots, diffs) is zstd-compressed, which covers the state part of the idea and more. Blocks (blinded, with payloads already pruned to the EL), blobs and data columns are written as raw SSZ and LevelDB's own compression is off. Compressing the BeaconBlock column would need a schema migration and changes in the block put/get paths.

**Impact.** Low to medium: blinded blocks compress poorly (signatures, roots), maybe 1.2-1.5x on the block column. That saves disk and some read I/O, little CPU. The headline Nimbus/Prysm wins came from state compression, and Lighthouse already has that.

**Best measured result.** 3gb vs 12gb for 4000 epochs; 3-4x sync blocks/sec (commit:nimbus@360ebd705fd7)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2143`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2143) store_cold_state_as_snapshot zstd-compresses freezer snapshots
- [`beacon_node/store/src/hot_cold_store.rs:2187`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2187) store_hot_state_as_snapshot zstd-compresses hot snapshots
- [`beacon_node/store/src/hdiff.rs:402`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L402) hdiff balances/validators diffs zstd-compressed
- [`beacon_node/beacon_chain/src/persisted_fork_choice.rs:40`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/persisted_fork_choice.rs#L40) fork choice compressed too
- [`beacon_node/store/src/hot_cold_store.rs:551`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L551) blinded_block_as_kv_store_ops stores raw SSZ
- [`beacon_node/store/src/hot_cold_store.rs:676`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L676) get_block_with decodes raw bytes, no decompression
- [`beacon_node/store/src/config.rs:42`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L42) compression_level comment mentions blocks, but no block path calls compress_bytes

**Second check.** Searched every Encoder/compress_bytes call site in store and beacon_chain: states, hdiffs and fork choice are compressed, block/blob/column paths are not. Also noted that Lighthouse already stores only blinded blocks, which removes most of the block size.

**Sources.** [prysm#16858](https://github.com/OffchainLabs/prysm/pull/16858), [nimbus@360ebd705](https://github.com/status-im/nimbus-eth2/commit/360ebd705fd7)

</details>

## Other checked ideas (57)

Implemented, not applicable, or low value.

<a id="db_cold-059"></a>
<details>
<summary><b>db_cold-059</b> State delta against snapshot, not parent — <i>not · low · L · latency, disk</i></summary>

**Idea.** Store each non-snapshot state as a delta against the nearest snapshot on its branch rather than against its parent, so a cold read applies one delta instead of folding a chain of deltas.

**Gap in Lighthouse.** Change HierarchyModuli::storage_strategy and load_hdiff_buffer_for_slot to diff against the layer-top snapshot. Diffs get larger, trading disk for fewer applies; needs schema change.

**Impact.** Cold state reads apply at most a few diffs now (layers) so gain is small and disk grows; marginal.

**Best measured result.** None stated (up to 31 sequential deltas replaced by one) (pr:ethlambda#684)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hdiff.rs:660`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L660) storage_strategy: DiffFrom(previous layer slot/n_big*n_big), not snapshot
- [`beacon_node/store/src/hot_cold_store.rs:2423`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2423) load_hdiff_buffer_for_slot folds layer chain

**Sources.** [ethlambda#684](https://github.com/lambdaclass/ethlambda/pull/684)

</details>

<a id="db_cold-107"></a>
<details>
<summary><b>db_cold-107</b> Pool compression decoders, share one low-memory encoder — <i>not · low · S · memory, cpu</i></summary>

**Idea.** Reuse zstd/compression decoders from a pool instead of creating one per call, and use a single shared, reset encoder with a small window instead of pooling large encoders. This bounds memory while keeping read throughput.

**Gap in Lighthouse.** Keep a reusable zstd Decompressor (or bulk::Decompressor) per thread or in a pool and use it in StoreConfig::decompress_bytes; optionally share one reset encoder for compress_bytes.

**Impact.** Cuts per-call zstd context allocation on historic state loads (HTTP state queries, reconstruction); modest, probably single-digit percent of diff apply time.

**Best measured result.** Decoder pool gave 2x throughput; encoder pool caused high memory (pr:caplin#16023)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/config.rs:198-213`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L198-L213) compress_bytes/decompress_bytes create a fresh zstd Encoder/Decoder per call
- [`beacon_node/store/src/hot_cold_store.rs:2152`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2152) Encoder::new per snapshot write
- no pool anywhere in beacon_node (grep Decoder::/Encoder::)

**Sources.** [caplin#23435](https://github.com/erigontech/erigon/pull/23435), [caplin#16023](https://github.com/erigontech/erigon/pull/16023)

</details>

<a id="db_cold-130"></a>
<details>
<summary><b>db_cold-130</b> Shorten block retention window after new forks — <i>not · low · L · disk</i></summary>

**Idea.** Recompute the block retention/serving window from the new fork's churn parameters (e.g. ~8192 or ~14299 epochs instead of 33024) so the pruning cutoff keeps far fewer historical blocks, and cap blocks pruned per run so the larger catch-up prune does not stall.

**Gap in Lighthouse.** Lighthouse would need a block-pruning pass (e.g. alongside try_prune_blobs) that deletes finalized blocks older than a window computed from the current fork's churn limits, with a per-run cap. Blob/column cutoff already follows spec constants, but blocks are never pruned.

**Impact.** Pruning blocks beyond ~36 days would cut hundreds of GB on a full-history node (blocks are ~tens of GB per year on disk plus freezer growth); no effect on CPU.

**Best measured result.** window 33024 -&gt; 8192 epochs (~36 days) (pr:lodestar#10518)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/core/chain_spec.rs:297`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/core/chain_spec.rs#L297) min_epochs_for_block_requests field present, grep shows no use outside spec parsing
- [`beacon_node/store/src/hot_cold_store.rs:3277`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3277) try_prune_blobs only handles blobs and data columns, window from min_epochs_for_blob/data_column_sidecars_requests (canonical_head.rs:1651, hot_cold_store.rs:3250)
- no block pruning mode in [`database_manager/src/cli.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/database_manager/src/cli.rs)

**Sources.** [lodestar#10518](https://github.com/ChainSafe/lodestar/pull/10518), [lodestar#10120](https://github.com/ChainSafe/lodestar/pull/10120)

</details>

<a id="db_cold-104"></a>
<details>
<summary><b>db_cold-104</b> Presize state-diff serialization buffer — <i>partial · low · S · cpu, memory</i></summary>

**Idea.** Compute the serialized size of a state diff first and allocate the output buffer at that capacity, avoiding repeated growth and copies for large registries.

**Gap in Lighthouse.** Presize uncompressed_bytes in CompressedU64Diff::compute (ys.len()*8) and the ValidatorsDiff buffer, and size the compressed output from a better estimate; currently only the compressed Vec is presized with a fixed factor 2.

**Impact.** Small cut in allocation/copy churn when computing hdiffs at snapshot/diff boundaries during migration; background-thread work, not on the block-import path.

**Best measured result.** 369.45-&gt;329.48 ms/op (10.8% faster), 485-&gt;216 MB/op (55.6% less), allocs 5.1M-&gt;421k (pr:prysm#17427)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/config.rs:198`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L198) compress_bytes presizes output via estimate_compressed_size (len/2)
- [`beacon_node/store/src/hdiff.rs:390`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L390) CompressedU64Diff::compute builds uncompressed_bytes with flat_map().collect(), no exact capacity
- [`beacon_node/store/src/hdiff.rs:173`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L173) HDiffBuffer::from_state uses as_ssz_bytes (presized by ssz)

**Sources.** [prysm#17427](https://github.com/OffchainLabs/prysm/pull/17427)

</details>

<a id="db_cold-132"></a>
<details>
<summary><b>db_cold-132</b> Delete data violating current retention on mode change — <i>partial · low · M · disk</i></summary>

**Idea.** At startup or after switching storage mode (archive to prune/minimal), scan for stored finalized states that the current retention policy would not keep, delete them in batches, and compact the affected range so the disk space is actually reclaimed.

**Gap in Lighthouse.** Only a manual `lighthouse db prune-states --confirm` that deletes everything exists; there is no automatic cleanup on a mode or hierarchy-exponents change at startup, and no partial (batched) deletion of just the non-conforming states. Add a startup check in HotColdDB::open that compares stored layers with hierarchy_config and deletes in batches plus compact_column.

**Impact.** Reclaims disk after config changes (could be tens of GB on archive nodes); no runtime CPU effect.

**Best measured result.** Extra states accounted for 50GB of 120GB DB on Prater nodes (pr:lodestar#4526)

**Evidence (Lighthouse @ 928b61e719).**

- [`database_manager/src/lib.rs:406`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/database_manager/src/lib.rs#L406) prune_states and hot_cold_store.rs:3471 prune_historic_states delete all freezer states then compact_freezer
- no startup scan that detects states violating the current retention/hierarchy config
- hot_cold_store.rs:382 TODO(tree-states) about pruning advanced states

**Sources.** [teku#8725](https://github.com/Consensys-Incorporated/teku/pull/8725), [lodestar#4526](https://github.com/ChainSafe/lodestar/pull/4526)

</details>

<a id="db_cold-031"></a>
<details>
<summary><b>db_cold-031</b> Archive historical states as layered diffs against snapshots — <i>implemented · high · disk, cpu, latency, memory</i></summary>

**Idea.** Store archived states as sparse full snapshots plus diffs (binary or per-field, possibly at hierarchical slot intervals) against a base snapshot, and rebuild a state by applying a short chain of diffs plus a short block replay. This cuts archive disk use by about an order of magnitude versus full states or restore points and replays fewer blocks per load.

**Gap in Lighthouse.** 

**Impact.** Already cuts archive disk by roughly an order of magnitude vs full states; nothing to gain.

**Best measured result.** archival states 1.5-2Tb -&gt; ~150-200Gb; deltas 150Kb-1.5Mb vs ~200MB snapshot; 0-32 transitions vs 0-1024 (pr:grandine#906)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hdiff.rs:33`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L33) HierarchyConfig exponents, layered snapshots+diffs
- [`beacon_node/store/src/hot_cold_store.rs:3594`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3594) migrate_database stores diffs/snapshots only at layer boundaries, replay otherwise

**Sources.** [lodestar#7005](https://github.com/ChainSafe/lodestar/pull/7005), [lodestar#7664](https://github.com/ChainSafe/lodestar/pull/7664), [lodestar#7874](https://github.com/ChainSafe/lodestar/pull/7874), [grandine#523](https://github.com/grandinetech/grandine/pull/523), [grandine#906](https://github.com/grandinetech/grandine/pull/906), [caplin#9414](https://github.com/erigontech/erigon/pull/9414), [lodestar#8796](https://github.com/ChainSafe/lodestar/pull/8796), [lodestar#7663](https://github.com/ChainSafe/lodestar/pull/7663), [prysm#15288](https://github.com/OffchainLabs/prysm/pull/15288), [prysm#15437](https://github.com/OffchainLabs/prysm/pull/15437), [prysm#15438](https://github.com/OffchainLabs/prysm/pull/15438), [prysm#15439](https://github.com/OffchainLabs/prysm/pull/15439), [prysm#16033](https://github.com/OffchainLabs/prysm/pull/16033), [lighthouse#5978](https://github.com/sigp/lighthouse/pull/5978), [prysm#16049](https://github.com/OffchainLabs/prysm/pull/16049), [lighthouse#4652](https://github.com/sigp/lighthouse/pull/4652), [lodestar#7901](https://github.com/ChainSafe/lodestar/pull/7901), [prysm#15250](https://github.com/OffchainLabs/prysm/pull/15250), [prysm#16203](https://github.com/OffchainLabs/prysm/pull/16203)

</details>

<a id="db_cold-032"></a>
<details>
<summary><b>db_cold-032</b> Store finalized blocks blinded, payload from EL — <i>implemented · high · disk</i></summary>

**Idea.** Store post-merge beacon blocks with the execution payload replaced by its header, and rebuild full payloads from the execution client on demand when serving blocks. Transactions already held by the EL are then not stored twice.

**Gap in Lighthouse.** 

**Impact.** Finalized payload duplication already avoided; payloads come back from the EL.

**Best measured result.** ~29.5 MB/hour, ~258 GB/year of payload duplication avoided (pr:prysm#11010)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:551`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L551) blinded_block_as_kv_store_ops stores blinded block
- [`beacon_node/store/src/hot_cold_store.rs:3119`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3119) try_prune_execution_payloads deletes finalized payloads (config prune_payloads default true, config.rs:117)
- [`beacon_node/beacon_chain/src/beacon_block_streamer.rs:234`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_block_streamer.rs#L234) rebuilds payloads from EL via get_payload_bodies_by_hash

**Sources.** [prysm#11097](https://github.com/OffchainLabs/prysm/pull/11097), [teku#5980](https://github.com/Consensys-Incorporated/teku/pull/5980), [prysm#10709](https://github.com/OffchainLabs/prysm/pull/10709), [caplin#9058](https://github.com/erigontech/erigon/pull/9058), [grandine@4019f077e](https://github.com/grandinetech/grandine/commit/4019f077e9f9), [prysm#10580](https://github.com/OffchainLabs/prysm/pull/10580), [prysm#11591](https://github.com/OffchainLabs/prysm/pull/11591), [prysm#11010](https://github.com/OffchainLabs/prysm/pull/11010), [caplin#8080](https://github.com/erigontech/erigon/pull/8080)

</details>

<a id="db_cold-078"></a>
<details>
<summary><b>db_cold-078</b> Resume pruning from a persisted cursor in bounded steps — <i>implemented · high · disk, cpu, memory, startup, latency</i></summary>

**Idea.** Track the last pruned slot or earliest stored slot (persisted watermark or in-memory) and start each prune run right after it, scanning only newly eligible ranges and deleting a bounded amount per step, instead of rescanning from slot zero or over tombstones. This lowers prune CPU, memory and startup delay.

**Gap in Lighthouse.** 

**Impact.** Prune runs scan only the newly eligible range; deletion per run is not capped but the range is small.

**Best measured result.** Prune run avg 0.66s vs 3.99s; beacon RSS 9.60 GB vs 13.58 GB (pr:lodestar#10216)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3296`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3296) persisted DataInfo.oldest_data_slot is the blob/column prune cursor
- [`beacon_node/store/src/hot_cold_store.rs:3313`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3313) start_epoch..end_epoch window, run only each epochs_per_blob_prune
- [`beacon_node/store/src/hot_cold_store.rs:3359`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3359) iteration walks back from end block and stops at first already-pruned block
- [`beacon_node/store/src/hot_cold_store.rs:3144`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3144) payload pruning stops early if already pruned (finalized_payloads_are_pruned)

**Sources.** [nimbus#4887](https://github.com/status-im/nimbus-eth2/pull/4887), [nimbus#9404](https://github.com/status-im/nimbus-eth2/pull/9404), [lodestar#10216](https://github.com/ChainSafe/lodestar/pull/10216), [lighthouse@63ca3bfb2](https://github.com/sigp/lighthouse/commit/63ca3bfb2962), [teku#10807](https://github.com/Consensys-Incorporated/teku/pull/10807), [lighthouse@a2b8c6ee6](https://github.com/sigp/lighthouse/commit/a2b8c6ee69f1), [teku#9031](https://github.com/Consensys-Incorporated/teku/pull/9031)

</details>

<a id="db_cold-153"></a>
<details>
<summary><b>db_cold-153</b> Reuse existing states when archiving finalized states — <i>implemented · high · cpu, latency</i></summary>

**Idea.** When storing finalized state snapshots (e.g. after long non-finality), first check whether the state already exists in memory or the DB and use it, instead of regenerating it by block replay.

**Gap in Lighthouse.** 

**Impact.** Finalized snapshots reuse cached states and skip non-boundary slots; no regeneration by replay unless the cache misses.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1812`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1812) get_hot_state checks state_cache by state root first
- [`beacon_node/store/src/hot_cold_store.rs:3606`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3606) migrate_database loads hot state (cache hit if present) and only for diff-boundary slots

**Sources.** [teku#3092](https://github.com/Consensys-Incorporated/teku/pull/3092), [prysm#7686](https://github.com/OffchainLabs/prysm/pull/7686)

</details>

<a id="db_cold-161"></a>
<details>
<summary><b>db_cold-161</b> Migrate hot-to-cold state diffs in one pass — <i>implemented · high · cpu, disk</i></summary>

**Idea.** Make hot-to-cold state-diff migration handle long non-finality by migrating in one pass rather than piecemeal (exact mechanism not visible).

**Gap in Lighthouse.** 

**Impact.** Long non-finality is handled in a single migration pass already.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3532`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3532) migrate_database walks all state roots from old split to new finalized state in one call
- [`beacon_node/store/src/hot_cold_store.rs:3594`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3594) only diff-boundary states are loaded; others get summaries only

**Sources.** [prysm#16795](https://github.com/OffchainLabs/prysm/pull/16795)

</details>

<a id="db_cold-006"></a>
<details>
<summary><b>db_cold-006</b> Persist latest finalized state on each finalization — <i>implemented · medium · startup, disk</i></summary>

**Idea.** On every finalization, persist the latest finalized state (as raw SSZ that loads directly into the in-memory layout) so a restart starts from a recent state instead of replaying from far back or genesis.

**Gap in Lighthouse.** 

**Evidence (Lighthouse @ 928b61e719).**

- store/src/hot_cold_store.rs:3532-3662 migrate_database sets split to finalized state
- store/src/hot_cold_store.rs:1661 store_hot_state persists epoch-boundary states at import (snapshot/diff)
- beacon_chain/src/builder.rs:595 split persisted with chain

**Sources.** [silver#79](https://github.com/gattaca-com/silver/pull/79), [lodestar#5520](https://github.com/ChainSafe/lodestar/pull/5520)

</details>

<a id="db_cold-009"></a>
<details>
<summary><b>db_cold-009</b> Store payload envelopes as summary, rebuild body from EL — <i>implemented · medium · disk</i></summary>

**Idea.** For finalized post-Gloas payload envelopes, keep only a small summary/header form (transactions, withdrawals and access list replaced by roots) and delete the payload body, rebuilding the full envelope from the EL by block hash when serving. Keep the full envelope only while execution validity is pending.

**Gap in Lighthouse.** 

**Best measured result.** ~267 KB -&gt; ~1 KB per envelope, &gt;99%, ~690 GB/yr saved (pr:lodestar#10089)

**Evidence (Lighthouse @ 928b61e719).**

- store/src/hot_cold_store.rs:688-699 get_signed_payload_envelope rebuilds from summary + body
- beacon_chain/src/migrate.rs:820-870 prune_finalized_payloads deletes bodies on finalization
- store/src/lib.rs:314 SignedExecutionPayloadEnvelopeSummary column

**Sources.** [lodestar#10089](https://github.com/ChainSafe/lodestar/pull/10089), [lodestar#10088](https://github.com/ChainSafe/lodestar/pull/10088), [lighthouse#10015](https://github.com/sigp/lighthouse/pull/10015)

</details>

<a id="db_cold-010"></a>
<details>
<summary><b>db_cold-010</b> Periodic finalized state archival with cache pruning — <i>implemented · medium · memory, disk</i></summary>

**Idea.** Run a periodic task that archives finalized states to cold storage and prunes older states from the in-memory state cache, so memory stays bounded.

**Gap in Lighthouse.** 

**Evidence (Lighthouse @ 928b61e719).**

- beacon_chain/src/migrate.rs:166 process_finalization on finalization in background thread
- store/src/state_cache.rs:127-150 update_finalized_state prunes cache
- store/src/hot_cold_store.rs:3532 migrate_database moves states to freezer

**Sources.** [lodestar@18bb73a89](https://github.com/ChainSafe/lodestar/commit/18bb73a8925d)

</details>

<a id="db_cold-012"></a>
<details>
<summary><b>db_cold-012</b> Persist finalized state on shutdown — <i>implemented · medium · startup, sync</i></summary>

**Idea.** On graceful shutdown, write the current finalized (checkpoint) state to disk so the next start loads a recent state instead of one up to many epochs old.

**Gap in Lighthouse.** 

**Best measured result.** avoids ~5-10 min sync times on restart (pr:lodestar#7221)

**Evidence (Lighthouse @ 928b61e719).**

- beacon_chain/src/beacon_chain.rs:8456 Drop persists fork choice, op pool
- store/src/hot_cold_store.rs:1661 hot states and split already persisted on import/finalization, so restart does not need a shutdown snapshot

**Sources.** [lodestar#7221](https://github.com/ChainSafe/lodestar/pull/7221), [prysm#6431](https://github.com/OffchainLabs/prysm/pull/6431)

</details>

<a id="db_cold-021"></a>
<details>
<summary><b>db_cold-021</b> Run blob pruning in a background task — <i>implemented · medium · latency</i></summary>

**Idea.** Run blob/sidecar pruning on a background thread (spawned blocking task or the background migrator) after head update, so the deletes do not stall block import or head update.

**Gap in Lighthouse.** 

**Impact.** Already off the import path.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:1734`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1734) process_prune_blobs after finalization
- [`beacon_node/beacon_chain/src/migrate.rs:213`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L213) sends Notification::PruneBlobs to migrator thread
- [`beacon_node/beacon_chain/src/migrate.rs:492`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L492) run_prune_blobs on background thread

**Sources.** [lighthouse@2f565d25b](https://github.com/sigp/lighthouse/commit/2f565d25b263), [lighthouse@caa04db58](https://github.com/sigp/lighthouse/commit/caa04db58a3c)

</details>

<a id="db_cold-024"></a>
<details>
<summary><b>db_cold-024</b> Batch data column sidecar writes in one transaction — <i>implemented · medium · disk, cpu, latency</i></summary>

**Idea.** Persist all data column sidecars of a block (or of a time/size window) in one DB transaction with a reused prepared statement, memoizing the shared header root, and serve in-flight writes from memory.

**Gap in Lighthouse.** 

**Impact.** Per-block single write batch already; no prepared-statement/header memoization concept in leveldb/redb. Batching across blocks would be a minor extra gain.

**Best measured result.** about 40% speedup in batch persisting data column sidecars for fulu (pr:nimbus#8336)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1003`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1003) data_columns_as_kv_store_ops builds all columns of a block as one op list
- [`beacon_node/store/src/hot_cold_store.rs:1521`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1521) blobs_db.do_atomically single write batch (leveldb WriteBatch, leveldb_impl.rs:143)
- [`beacon_node/store/src/hot_cold_store.rs:996`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L996) in-flight columns served from block_cache

**Sources.** [nimbus#8336](https://github.com/status-im/nimbus-eth2/pull/8336), [teku#10293](https://github.com/Consensys-Incorporated/teku/pull/10293)

</details>

<a id="db_cold-027"></a>
<details>
<summary><b>db_cold-027</b> Run finalization migration every N epochs — <i>implemented · medium · disk</i></summary>

**Idea.** Run the hot-to-cold finalization migration only every N finalized epochs instead of every finalization, batching reads, deletes and freezer writes into larger transactions.

**Gap in Lighthouse.** 

**Impact.** Mechanism exists and is configurable (default 1, i.e. every finalization), so batching larger windows is only a tuning change.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/migrate.rs:31`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L31) DEFAULT_EPOCHS_PER_MIGRATION=1
- [`beacon_node/beacon_chain/src/migrate.rs:314`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L314) skips migration unless epoch &gt;= prev + epochs_per_migration

**Sources.** [lighthouse#3582](https://github.com/sigp/lighthouse/pull/3582)

</details>

<a id="db_cold-033"></a>
<details>
<summary><b>db_cold-033</b> Separate database for blob sidecars — <i>implemented · medium · disk</i></summary>

**Idea.** Store blob sidecars in a separate database or blob store from the hot and freezer data, so the hot DB stays small and blobs can live on other storage and be pruned independently.

**Gap in Lighthouse.** 

**Impact.** Already separate; hot DB stays small and blobs/columns can be placed on other storage via --blobs-dir.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:68`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L68) pub blobs_db field
- [`beacon_node/store/src/hot_cold_store.rs:259-283`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L259-L283) opened from separate blobs_db_path
- [`beacon_node/store/src/hot_cold_store.rs:1521`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1521) blobs written to blobs_db

**Sources.** [lighthouse#3869](https://github.com/sigp/lighthouse/pull/3869), [caplin#9573](https://github.com/erigontech/erigon/pull/9573), [lighthouse@f9737628f](https://github.com/sigp/lighthouse/commit/f9737628fc09)

</details>

<a id="db_cold-034"></a>
<details>
<summary><b>db_cold-034</b> Prune blob and column sidecars past DA window by default — <i>implemented · medium · disk</i></summary>

**Idea.** Delete stored blob sidecars and data column sidecars older than the data availability retention window, enabled by default and run at each finalization/migration rather than only at startup, so sidecar storage stays bounded.

**Gap in Lighthouse.** 

**Impact.** Already default-on and run each finalization; disabled only with --prune-blobs false or complete-blob-backfill.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/config.rs:120`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L120) prune_blobs default true
- [`beacon_node/beacon_chain/src/canonical_head.rs:1734`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1734) pruning triggered at each finalization via migrator
- [`beacon_node/store/src/hot_cold_store.rs:3277`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3277) try_prune_blobs handles BeaconBlob and BeaconDataColumn up to the DA boundary minus margin

**Sources.** [lighthouse@fe0c91140](https://github.com/sigp/lighthouse/commit/fe0c9114027f), [lighthouse@7bf88c233](https://github.com/sigp/lighthouse/commit/7bf88c2336fc), [lodestar#7717](https://github.com/ChainSafe/lodestar/pull/7717), [nimbus#7369](https://github.com/status-im/nimbus-eth2/pull/7369), [lighthouse@d67468d73](https://github.com/sigp/lighthouse/commit/d67468d737a5)

</details>

<a id="db_cold-039"></a>
<details>
<summary><b>db_cold-039</b> Cheaper block replay for frozen states — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** When loading frozen states, reuse block roots from the state-root iterator during replay instead of rehashing, pass the proposer index through instead of recomputing, and avoid state clones in the hot/cold DB.

**Gap in Lighthouse.** 

**Impact.** Already done; state clones are cheap with milhouse tree-states.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2555`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2555) replay_blocks uses BlockReplayer state_root_iter and minimal_block_root_verification
- [`consensus/state_processing/src/block_replayer.rs:260`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/block_replayer.rs#L260) set_proposer_index from the block
- [`consensus/state_processing/src/block_replayer.rs:184`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/block_replayer.rs#L184) state roots taken from iterator

**Sources.** [lighthouse#2431](https://github.com/sigp/lighthouse/pull/2431)

</details>

<a id="db_cold-046"></a>
<details>
<summary><b>db_cold-046</b> Run DB compaction rarely — <i>implemented · medium · memory, disk</i></summary>

**Idea.** Run full DB compaction only rarely (about every 1024 epochs, robust to skipped epochs) and make it optional, since frequent compaction caused OOM and consistency problems.

**Gap in Lighthouse.** 

**Impact.** Already done with an equivalent time-and-finality-gap rule.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/migrate.rs:19-24`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L19-L24) MAX 7d, MIN 2h, COMPACTION_FINALITY_DISTANCE 1024
- [`beacon_node/beacon_chain/src/migrate.rs:939`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L939) trigger condition
- [`beacon_node/store/src/config.rs:116`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L116) compact_on_prune configurable

**Sources.** [lighthouse#1916](https://github.com/sigp/lighthouse/pull/1916)

</details>

<a id="db_cold-054"></a>
<details>
<summary><b>db_cold-054</b> Store validator immutable fields once, not per state — <i>implemented · medium · disk, memory, cpu</i></summary>

**Idea.** Do not store the full validator registry (or its immutable fields such as pubkeys and withdrawal credentials) in every stored historical state; store them once in a separate table and persist states with only mutable fields (or with pubkeys zeroed so compression removes them), restoring them on load. This shrinks each stored state greatly.

**Gap in Lighthouse.** 

**Impact.** Equivalent: states are stored as diffs against periodic snapshots, so immutable validator fields are stored once per snapshot instead of per state. Full snapshots still hold the registry.

**Best measured result.** ~20% faster overall ncli_db bench; DB block+state store ~60% faster; DB size 17GiB to 3.9GiB (75% smaller) (pr:nimbus#2297)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hdiff.rs:163`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L163) ValidatorsDiff stores only changed validators, pubkey only on change
- [`beacon_node/store/src/hdiff.rs:456`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L456) pubkey_changed check
- consensus tree-states schema (PR 3626) merged

**Sources.** [prysm#9155](https://github.com/OffchainLabs/prysm/pull/9155), [lighthouse#3626](https://github.com/sigp/lighthouse/pull/3626), [nimbus#2514](https://github.com/status-im/nimbus-eth2/pull/2514), [nimbus#2297](https://github.com/status-im/nimbus-eth2/pull/2297), [grandine@d6269806c](https://github.com/grandinetech/grandine/commit/d6269806c780), [grandine#611](https://github.com/grandinetech/grandine/pull/611)

</details>

<a id="db_cold-057"></a>
<details>
<summary><b>db_cold-057</b> Delete sidecars of orphaned blocks at finalization — <i>implemented · medium · disk, cpu</i></summary>

**Idea.** At finalization, find blocks that conflict with the finalized chain (recording orphan roots that actually have stored blobs or columns) and delete their blob and data column sidecars in the same step. Slot-based retention pruning only finds canonical blocks, so orphan sidecars would otherwise leak forever.

**Gap in Lighthouse.** 

**Impact.** Done at finalization in prune_hot_db for blocks off the finalized chain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/migrate.rs:757-770`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L757-L770) blocks_to_prune pushes DeleteBlobs and DeleteDataColumns for abandoned blocks
- [`beacon_node/beacon_chain/src/migrate.rs:836-860`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L836-L860) prune_finalized_payloads deletes columns of EMPTY-finalized payloads
- [`beacon_node/store/src/hot_cold_store.rs:2657`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2657) get_data_column_keys reads only stored keys

**Sources.** [lighthouse@c7f53a906](https://github.com/sigp/lighthouse/commit/c7f53a9062de), [lighthouse@0bdc29149](https://github.com/sigp/lighthouse/commit/0bdc291490a5), [lighthouse@8752deece](https://github.com/sigp/lighthouse/commit/8752deeced23), [nimbus#9403](https://github.com/status-im/nimbus-eth2/pull/9403), [lighthouse#10286](https://github.com/sigp/lighthouse/pull/10286)

</details>

<a id="db_cold-071"></a>
<details>
<summary><b>db_cold-071</b> Per-index diff for validator and builder registries — <i>implemented · medium · S · cpu, disk, latency</i></summary>

**Idea.** When diffing states, diff list registries (validators, builders, balances) per index and store only (index, change) for changed entries, leaving a small remainder to a generic binary delta. Much faster and smaller than a generic byte diff of the whole list.

**Gap in Lighthouse.** 

**Impact.** Already done (PR 6556 present).

**Best measured result.** hdiff n=1M, 1000 mutated: ~354ms -&gt; ~27ms; n=2M: ~814ms -&gt; ~54ms; diff size slightly smaller (pr:lighthouse#6556)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hdiff.rs:439`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L439) ValidatorsDiff::compute emits (index, changed fields) only for changed validators, then zstd
- [`beacon_node/store/src/hdiff.rs:385`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L385) CompressedU64Diff for balances/inactivity_scores
- [`beacon_node/store/src/hdiff.rs:329`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L329) xdelta3 only for the remaining state bytes

**Sources.** [lighthouse#6556](https://github.com/sigp/lighthouse/pull/6556), [caplin#25231](https://github.com/erigontech/erigon/pull/25231)

</details>

<a id="db_cold-073"></a>
<details>
<summary><b>db_cold-073</b> Split hot and finalized databases, prune non-canonical — <i>implemented · medium · S · disk</i></summary>

**Idea.** Keep unfinalized blocks/states in a hot DB or tables and finalized data in a separate archive DB with its own schema and tuning, deleting non-canonical hot data at finalization. Disk holds only the finalized chain plus live forks, and sparse finalized state storage becomes possible.

**Gap in Lighthouse.** 

**Impact.** Already done.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:66`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L66) separate cold_db, hot_db and blobs_db
- [`beacon_node/beacon_chain/src/migrate.rs:509`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L509) prune_hot_db deletes non-canonical states/blocks at finalization
- [`beacon_node/beacon_chain/src/migrate.rs:645`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L645) abandoned-fork block pruning
- [`beacon_node/store/src/hot_cold_store.rs:3532`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3532) migrate_database moves finalized states to cold with hierarchical diffs

**Sources.** [teku#1060](https://github.com/Consensys-Incorporated/teku/pull/1060), [teku#2195](https://github.com/Consensys-Incorporated/teku/pull/2195)

</details>

<a id="db_cold-101"></a>
<details>
<summary><b>db_cold-101</b> Persist decompressed BLS pubkeys — <i>implemented · medium · S · startup, cpu, disk</i></summary>

**Idea.** Persist decompressed BLS pubkeys alongside the finalized checkpoint (and write finalized state in batches) so restarts skip expensive pubkey decompression.

**Gap in Lighthouse.** 

**Impact.** Already done: restart loads uncompressed pubkeys from the store instead of decompressing.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:60`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L60) load_from_store reads DatabasePubkey per index
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:209`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L209) DatabasePubkey holds PUBLIC_KEY_UNCOMPRESSED_BYTES_LEN bytes

**Sources.** [silver#83](https://github.com/gattaca-com/silver/pull/83)

</details>

<a id="db_cold-120"></a>
<details>
<summary><b>db_cold-120</b> Memoize deserialized diff anchor states — <i>implemented · medium · S · disk, cpu, startup</i></summary>

**Idea.** Cache the deserialized anchor/snapshot state per diff level (invalidated on replacement) instead of deserializing it on every reconstruction, and snapshot resume states periodically.

**Gap in Lighthouse.** 

**Impact.** Already done; anchors are cached as hdiff buffers (near-SSZ form), and put_both caches the snapshot state. Cache is keyed by slot, entries are immutable so invalidation is unneeded.

**Best measured result.** avoids ~410k full state deserializations on mainnet walk (pr:prysm#17292)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/historic_state_cache.rs:12`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/historic_state_cache.rs#L12) HistoricStateCache LRU of hdiff_buffers and states by slot
- [`beacon_node/store/src/hot_cold_store.rs:2424`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2424) load_hdiff_buffer_for_slot checks cache before recursing to the snapshot
- [`beacon_node/store/src/config.rs:27`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L27) cold hdiff buffer cache size 16

**Sources.** [prysm#17292](https://github.com/OffchainLabs/prysm/pull/17292)

</details>

<a id="db_cold-145"></a>
<details>
<summary><b>db_cold-145</b> Separate storage queue for column sidecar queries — <i>implemented · medium · latency</i></summary>

**Idea.** Route heavy data column sidecar reads through their own async channel/queue so they do not stall block and state storage operations.

**Gap in Lighthouse.** 

**Impact.** Column sidecar reads already go to their own DB handle and their own beacon processor queue, so they cannot block block/state storage through a shared queue.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:68`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L68) blobs_db is a separate database instance from hot/cold
- [`beacon_node/beacon_processor/src/lib.rs:600`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L600) DataColumnsByRangeRequest has its own work type and queue

**Sources.** [teku#10276](https://github.com/Consensys-Incorporated/teku/pull/10276)

</details>

<a id="db_cold-157"></a>
<details>
<summary><b>db_cold-157</b> Skip archiving blobs/columns outside retention window — <i>implemented · medium · disk, sync</i></summary>

**Idea.** When archiving finalized blocks during sync, do not write blobs or data columns that are already outside the data-availability retention window.

**Gap in Lighthouse.** 

**Impact.** Backfill does not request or write blobs/columns outside the DA window unless --complete-blob-backfill is set.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context.rs:1311`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L1311) data_columns_required_for_epoch gates column download by epoch
- [`beacon_node/network/src/sync/network_context.rs:1314`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L1314) blobs_required_for_epoch gates blobs
- [`beacon_node/beacon_chain/src/custody_context.rs:268`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L268) complete_blob_backfill opt-in beyond window
- [`beacon_node/beacon_chain/src/historical_blocks.rs:230`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_blocks.rs#L230) get_blobs_or_columns_store_op writes only delivered data

**Sources.** [lodestar#7760](https://github.com/ChainSafe/lodestar/pull/7760)

</details>

<a id="db_cold-160"></a>
<details>
<summary><b>db_cold-160</b> Coarser default spacing of full state snapshots — <i>implemented · medium · disk</i></summary>

**Idea.** Raise the default interval between stored full states (restore points), trading slower historical state reconstruction for several times less freezer disk and writes.

**Gap in Lighthouse.** 

**Impact.** Hierarchical state diffs replaced restore points; full snapshots are far sparser than the old 8192-slot default.

**Best measured result.** reduces disk usage by 32x, historical queries under 10s (pr:lighthouse#790)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hdiff.rs:622`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L622) default hierarchy exponents [5,9,11,13,16,18,21]: full snapshot every 2^21 slots
- [`beacon_node/src/cli.rs:746`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L746) --slots-per-restore-point deprecated, no effect
- [`beacon_node/store/src/config.rs:20`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L20) legacy DEFAULT_SLOTS_PER_RESTORE_POINT const unused

**Sources.** [prysm#6730](https://github.com/OffchainLabs/prysm/pull/6730), [lighthouse#3137](https://github.com/sigp/lighthouse/pull/3137), [lighthouse#790](https://github.com/sigp/lighthouse/pull/790), [nimbus@557717b51](https://github.com/status-im/nimbus-eth2/commit/557717b51799), [nimbus#2542](https://github.com/status-im/nimbus-eth2/pull/2542)

</details>

<a id="db_cold-172"></a>
<details>
<summary><b>db_cold-172</b> Cache regenerated finalized states for sequential reads — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** Keep recently regenerated finalized (cold) states in a soft/LRU cache so walking forward through historical slots replays from the previous regenerated state instead of from the stored snapshot each time.

**Gap in Lighthouse.** 

**Best measured result.** state by slot API: ~12 s per request uncached vs 0.3-0.6 s sequential (pr:teku#2216)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/historic_state_cache.rs:15`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/historic_state_cache.rs#L15) HistoricStateCache with LRU of states and hdiff buffers
- [`beacon_node/store/src/hot_cold_store.rs:2310`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2310) load_cold_state_by_slot looks for cached prior state in replay range and replays from it
- [`beacon_node/store/src/hot_cold_store.rs:2344`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2344) results put_both into cache

**Sources.** [teku#2216](https://github.com/Consensys-Incorporated/teku/pull/2216)

</details>

<a id="db_cold-011"></a>
<details>
<summary><b>db_cold-011</b> Store full finalized states only at sparse intervals — <i>implemented · low · disk</i></summary>

**Idea.** In the cold/freezer database store a full finalized state only every N slots or epochs (restore points, with an index of archived points), and regenerate intermediate states by replaying blocks from the nearest stored state. This uses far less disk than storing every finalized state.

**Gap in Lighthouse.** 

**Best measured result.** mainnet sync disk usage ~1GB with N=1024 (pr:lodestar#1937)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hdiff.rs:660`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L660) storage_strategy: Snapshot/DiffFrom/ReplayFrom hierarchy
- [`beacon_node/store/src/hot_cold_store.rs:2102`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2102) store_cold_state stores only snapshot or diff, nothing for replay slots

**Sources.** [lodestar#7433](https://github.com/ChainSafe/lodestar/pull/7433), [teku#2199](https://github.com/Consensys-Incorporated/teku/pull/2199), [prysm#4977](https://github.com/OffchainLabs/prysm/pull/4977), [lighthouse#649](https://github.com/sigp/lighthouse/pull/649), [prysm#5076](https://github.com/OffchainLabs/prysm/pull/5076), [teku#2217](https://github.com/Consensys-Incorporated/teku/pull/2217), [teku#2187](https://github.com/Consensys-Incorporated/teku/pull/2187), [lodestar#1937](https://github.com/ChainSafe/lodestar/pull/1937), [lodestar@3ca6b3cd9](https://github.com/ChainSafe/lodestar/commit/3ca6b3cd9581), [grandine@d319e8a52](https://github.com/grandinetech/grandine/commit/d319e8a52439), [prysm#4971](https://github.com/OffchainLabs/prysm/pull/4971), [prysm#4967](https://github.com/OffchainLabs/prysm/pull/4967)

</details>

<a id="db_cold-029"></a>
<details>
<summary><b>db_cold-029</b> Bucket scan for slashing-protection export — <i>implemented · low · disk, latency</i></summary>

**Idea.** Export slashing-protection proposal history by iterating the bucket keys in one transaction instead of one query per slot.

**Gap in Lighthouse.** 

**Best measured result.** Says lookups are 'a lot faster'; no numbers (pr:prysm#8378)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/slashing_protection/src/slashing_database.rs:984`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L984) export_interchange_blocks_for_validator single SELECT per validator ordered by slot
- [`validator_client/slashing_protection/src/slashing_database.rs:942`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L942) whole export inside one transaction

**Sources.** [prysm#8378](https://github.com/OffchainLabs/prysm/pull/8378)

</details>

<a id="db_cold-045"></a>
<details>
<summary><b>db_cold-045</b> Shrink slasher DB keys and records — <i>implemented · low · disk, memory, cpu</i></summary>

**Idea.** Shrink slasher on-disk keys (short validator index and modular epoch) and attester records, and compress stored attestation data, to cut slasher DB size.

**Gap in Lighthouse.** 

**Best measured result.** keys 16-&gt;7 bytes, records 64-&gt;6 bytes (pr:lighthouse#2776)

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/database.rs:96`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L96) AttesterKey: 2-byte modular target epoch + 5-byte validator index = 7 bytes
- [`slasher/src/attester_record.rs:29`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/attester_record.rs#L29) CompactAttesterRecord is just an 8-byte indexed attestation id
- [`slasher/src/array.rs:180`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/array.rs#L180) chunks zstd-compressed

**Sources.** [prysm#8701](https://github.com/OffchainLabs/prysm/pull/8701), [lighthouse#2776](https://github.com/sigp/lighthouse/pull/2776)

</details>

<a id="db_cold-053"></a>
<details>
<summary><b>db_cold-053</b> Store each distinct slasher attestation once — <i>implemented · low · S · disk, memory, cpu</i></summary>

**Idea.** In the slasher, store each distinct attestation once (keyed by root plus attesting-indices hash, shared by reference) with small per-validator pointers, instead of a full copy per attesting validator.

**Gap in Lighthouse.** 

**Impact.** Already done; slasher stores each indexed attestation once.

**Best measured result.** stores only 1-2% of attestations seen, a 50-100x reduction in data stored (pr:lighthouse#2767)

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/database.rs:498`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L498) store_indexed_attestation keyed by root-&gt;id
- [`slasher/src/database.rs:170`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L170) IndexedAttestationIdKey

**Sources.** [lighthouse#2767](https://github.com/sigp/lighthouse/pull/2767), [prysm#8720](https://github.com/OffchainLabs/prysm/pull/8720)

</details>

<a id="db_cold-060"></a>
<details>
<summary><b>db_cold-060</b> Drop in-memory index for archived block range — <i>implemented · low · S · memory</i></summary>

**Idea.** Do not keep an in-memory root-to-block index for the archived (backfilled) range; look up slot to root in a DB table on demand.

**Gap in Lighthouse.** 

**Impact.** No in-memory index of archived range exists; lookups go to DB.

**Best measured result.** 100-200MB memory savings for checkpoint-synced nodes (pr:nimbus#3429)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3099`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3099) get_cold_block_root reads slot-&gt;root from freezer DB column
- [`beacon_node/store/src/forwards_iter.rs:234`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/forwards_iter.rs#L234) forwards iterator over frozen columns

**Sources.** [nimbus#3429](https://github.com/status-im/nimbus-eth2/pull/3429)

</details>

<a id="db_cold-075"></a>
<details>
<summary><b>db_cold-075</b> Do not store historic finalized states by default — <i>implemented · low · S · disk, startup</i></summary>

**Idea.** Offer (and default to) a storage mode that drops finalized historic states instead of archiving them, with no or optional restore points, cutting disk usage and write load for non-archive nodes.

**Gap in Lighthouse.** 

**Impact.** Default non-archive nodes do not keep all historic states.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/src/cli.rs:1301`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L1301) --archive flag opt-in for all states
- [`beacon_node/src/config.rs:603`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/config.rs#L603) archive only when flag set

**Sources.** [teku#1383](https://github.com/Consensys-Incorporated/teku/pull/1383), [lighthouse#4610](https://github.com/sigp/lighthouse/pull/4610), [lighthouse#2144](https://github.com/sigp/lighthouse/pull/2144), [teku#7401](https://github.com/Consensys-Incorporated/teku/pull/7401)

</details>

<a id="db_cold-076"></a>
<details>
<summary><b>db_cold-076</b> Offline tool to prune historic states/blocks in place — <i>implemented · low · S · disk</i></summary>

**Idea.** Provide a command that deletes unneeded historic states and blocks from an existing database in place, reclaiming disk without a resync.

**Gap in Lighthouse.** 

**Impact.** Already available as lighthouse db prune-states.

**Best measured result.** 50G to 1.0G on disk (pr:nimbus#1593)

**Evidence (Lighthouse @ 928b61e719).**

- [`database_manager/src/lib.rs:406`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/database_manager/src/lib.rs#L406) prune_states in-place subcommand

**Sources.** [lighthouse#4648](https://github.com/sigp/lighthouse/pull/4648), [nimbus#1593](https://github.com/status-im/nimbus-eth2/pull/1593)

</details>

<a id="db_cold-087"></a>
<details>
<summary><b>db_cold-087</b> Forwards freezer iterator for historic root lookups — <i>implemented · low · S · memory, latency, cpu</i></summary>

**Idea.** Resolve historic block and state roots by slot with a forwards iterator over freezer restore-point data instead of reverse-iterating from the head, which materialises many states and spikes memory.

**Gap in Lighthouse.** 

**Impact.** Historic root lookups hit the DB directly, no state materialisation for frozen range.

**Best measured result.** memory spike 400mb to 800mb+ avoided; response from ~1-2s to near instant (informal) (pr:lighthouse#2376)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3099`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3099) per-slot BeaconBlockRoots column in freezer
- [`beacon_node/store/src/forwards_iter.rs:234`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/forwards_iter.rs#L234) HybridForwardsIterator reads frozen range forwards

**Sources.** [lighthouse#672](https://github.com/sigp/lighthouse/pull/672), [lighthouse#2376](https://github.com/sigp/lighthouse/pull/2376), [lighthouse#2422](https://github.com/sigp/lighthouse/pull/2422)

</details>

<a id="db_cold-095"></a>
<details>
<summary><b>db_cold-095</b> Do not preload all block summaries at startup — <i>implemented · low · S · memory</i></summary>

**Idea.** Read block summaries from the database on demand instead of loading all of them into memory at startup.

**Gap in Lighthouse.** 

**Impact.** No startup preload of all block summaries; fork choice restored from persisted proto-array.

**Best measured result.** RSS 1.56 GiB -&gt; 1.11 GiB; DAG load 6m45s -&gt; 7m00s (pr:nimbus#3164)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/migrate.rs:539`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L539) load_hot_state_summaries only used at finalization
- [`beacon_node/store/src/hot_cold_store.rs:3003`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3003) per-root summary read on demand

**Sources.** [nimbus#3164](https://github.com/status-im/nimbus-eth2/pull/3164)

</details>

<a id="db_cold-102"></a>
<details>
<summary><b>db_cold-102</b> Persist derived light-client data in the DB — <i>implemented · low · S · startup, disk, latency</i></summary>

**Idea.** Store light-client bootstrap and update data (sync committees, epoch-boundary headers) in a small DB table at finalization so they are served without historic states or block replay after restart or pruning.

**Gap in Lighthouse.** 

**Impact.** Light client data persisted so bootstrap/updates are served without historic states.

**Best measured result.** "A full database with default settings (129 periods) uses &lt;15 MB disk" (pr:nimbus#3823)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/light_client_server_cache.rs:212`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_server_cache.rs#L212) store_current_sync_committee persists sync committee+branch
- [`beacon_node/beacon_chain/src/light_client_server_cache.rs:396`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_server_cache.rs#L396) bootstrap built from persisted parts
- [`beacon_node/store/src/hot_cold_store.rs:831`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L831) LightClientUpdate column

**Sources.** [nimbus#4499](https://github.com/status-im/nimbus-eth2/pull/4499), [nimbus#3823](https://github.com/status-im/nimbus-eth2/pull/3823)

</details>

<a id="db_cold-131"></a>
<details>
<summary><b>db_cold-131</b> Reuse stored block roots instead of re-hashing — <i>implemented · low · S · cpu</i></summary>

**Idea.** When archiving or pruning finalized blocks, read roots from the DB keys or the root-to-slot index rather than recomputing hash_tree_root for each block.

**Gap in Lighthouse.** 

**Impact.** Already avoids per-block re-hashing in pruning and migration paths.

**Best measured result.** Switching a synced mainnet node from prune to minimal took about 80 minutes with no visible impact on block import (pr:teku#6606)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3366`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3366) try_prune_blobs walks with ParentRootBlockIterator: block roots come from parent_root links starting at a known root, not hash_tree_root
- [`beacon_node/store/src/iter.rs:243`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/iter.rs#L243) ParentRootBlockIterator
- [`beacon_node/beacon_chain/src/migrate.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs): migration uses roots from fork choice/state roots, no canonical_root of blocks (grep found none)

**Sources.** [lodestar#1137](https://github.com/ChainSafe/lodestar/pull/1137), [teku#6606](https://github.com/Consensys-Incorporated/teku/pull/6606)

</details>

<a id="db_cold-150"></a>
<details>
<summary><b>db_cold-150</b> Skip redundant CRC and buffer zeroing on loads — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** When loading blocks/states from DB or ERA files, skip CRC32 checks already done by the storage layer and avoid zero-initialising read buffers.

**Gap in Lighthouse.** 

**Impact.** Nothing left to gain; at most the storage-engine checksum remains, ~50ms per 110MB state at best.

**Best measured result.** CRC32 check cost ~50ms per 110MB state load (pr:nimbus#5207)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/config.rs:198-216`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L198-L216) zstd encoder/decoder, no frame checksum enabled (zstd default off), output Vec::with_capacity not zero-filled
- [`beacon_node/store/src/hot_cold_store.rs:2176-2179`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2176-L2179) read_to_end into with_capacity buffer, no zeroing

**Sources.** [nimbus#5207](https://github.com/status-im/nimbus-eth2/pull/5207)

</details>

<a id="db_cold-169"></a>
<details>
<summary><b>db_cold-169</b> Walk parent-child index between finalized checkpoints — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Compute newly finalized block roots by walking the parent-to-child index between previous and new finalized checkpoints instead of a broader scan.

**Gap in Lighthouse.** 

**Impact.** Already walks the in-memory summaries DAG instead of scanning; only milliseconds at stake.

**Best measured result.** shaves off 10ms from epoch processing time (pr:prysm#13486)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/migrate.rs:618-620`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L618-L620) state_summaries_dag.ancestors_of(new_finalized_state_root) walks parent links down from new finalized state
- [`beacon_node/beacon_chain/src/migrate.rs:593`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L593) descendants_of used for the other side
- [`beacon_node/beacon_chain/src/migrate.rs:626-634`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L626-L634) blocks_of_states for newly finalized set

**Sources.** [prysm#13486](https://github.com/OffchainLabs/prysm/pull/13486)

</details>

<a id="db_cold-171"></a>
<details>
<summary><b>db_cold-171</b> Cap state reconstruction batch to yield to migration — <i>implemented · low · S · memory, latency</i></summary>

**Idea.** Limit the number of blocks per historic state reconstruction batch so finalization migration runs regularly and the hot state cache does not thrash.

**Gap in Lighthouse.** 

**Impact.** Already in place; keeps migrations running during reconstruction.

**Best measured result.** Reduced by 32x to 1024 blocks; ~110 epochs to ~3.5 epochs between migrations (pr:lighthouse#6668)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/migrate.rs:29`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L29) const BLOCKS_PER_RECONSTRUCTION: usize = 1024
- [`beacon_node/beacon_chain/src/migrate.rs:225`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L225) reconstruct_historic_states(Some(BLOCKS_PER_RECONSTRUCTION)) then requeues

**Sources.** [lighthouse#6668](https://github.com/sigp/lighthouse/pull/6668)

</details>

<a id="db_cold-015"></a>
<details>
<summary><b>db_cold-015</b> Plain delete for single-key removals — <i>n/a · medium · memory, disk</i></summary>

**Idea.** When deleting one key (e.g. one archived state), use a plain delete rather than a batch delete, since the batch path caused RSS memory spikes.

**Gap in Lighthouse.** Lodestar's batchDelete RSS spike is a JS db wrapper artifact; Lighthouse single-state deletes go through a small leveldb WriteBatch with no spike.

**Best measured result.** batchDelete caused rss memory spike (no numbers given) (pr:lodestar#5607)

**Evidence (Lighthouse @ 928b61e719).**

- store/src/hot_cold_store.rs:1212 delete_state uses one StoreOp via do_atomically
- store/src/database/leveldb_impl.rs:133 key_delete exists; delete_batch only used for column cleanup (hot_cold_store.rs:1446)

**Sources.** [lodestar#5607](https://github.com/ChainSafe/lodestar/pull/5607)

</details>

<a id="db_cold-023"></a>
<details>
<summary><b>db_cold-023</b> Copy DB values as raw bytes during hot-to-cold migration — <i>n/a · medium · disk, cpu, memory</i></summary>

**Idea.** When migrating finalized blocks from hot to cold store, or bulk-copying between columns/DBs, read and write the already-serialized value bytes directly in one batch write instead of SSZ-decoding and re-encoding each object. Root/parent indexes can be built from fork-choice summaries instead of decoded blocks.

**Gap in Lighthouse.** 

**Impact.** Lighthouse does not move finalized blocks to the freezer (blocks stay in the hot/blocks column), so there are no per-block decode/encode copies; remaining state work is hdiff computation, not a raw copy.

**Best measured result.** 10 times faster as tested in e2e (pr:lodestar#1759)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3532`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3532) migrate_database writes only slot-&gt;block_root into BeaconBlockRoots (3576) and cold state summaries/diffs
- [`beacon_node/store/src/hot_cold_store.rs:3606`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3606) only diff-boundary states are loaded and re-encoded as hdiffs

**Sources.** [lodestar@f1882361d](https://github.com/ChainSafe/lodestar/commit/f1882361d299), [lodestar@271e4d0d6](https://github.com/ChainSafe/lodestar/commit/271e4d0d65d3), [lodestar#1739](https://github.com/ChainSafe/lodestar/pull/1739), [lodestar#1759](https://github.com/ChainSafe/lodestar/pull/1759), [lodestar@c69b4b8d1](https://github.com/ChainSafe/lodestar/commit/c69b4b8d1356), [teku#5962](https://github.com/Consensys-Incorporated/teku/pull/5962), [teku#4096](https://github.com/Consensys-Incorporated/teku/pull/4096)

</details>

<a id="db_cold-036"></a>
<details>
<summary><b>db_cold-036</b> Upper-bound KV iterators past tombstones — <i>n/a · medium · latency, disk, cpu</i></summary>

**Idea.** Set an exclusive upper bound on ranged key-value iterators so seeks stop at the range end instead of walking deletion tombstones, and skip the DB for ranges below the prune watermark.

**Gap in Lighthouse.** 

**Impact.** Lighthouse keys columns by block_root+index and serves by-range via block-root iterators and point gets, not slot-keyed KV range scans over tombstones; the Teku failure mode does not arise.

**Best measured result.** 32-slot request in 1M-4M tombstone band 41-167 ms -&gt; ~1.5 us (data columns); minutes-long requests on Sepolia (pr:teku#11585)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2657`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2657) get_data_column_keys seeks by block_root prefix with take_while
- [`beacon_node/store/src/database/leveldb_impl.rs:204`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/leveldb_impl.rs#L204) iter_column_from has no upper bound, only a column take_while

**Sources.** [teku#11585](https://github.com/Consensys-Incorporated/teku/pull/11585)

</details>

<a id="db_cold-062"></a>
<details>
<summary><b>db_cold-062</b> No delta encoding before general compression — <i>n/a · medium · S · disk, latency</i></summary>

**Idea.** Do not delta-encode balances in stored state snapshots when a general compressor (Snappy) is applied anyway; the delta pass costs much more CPU on load than it saves.

**Gap in Lighthouse.** 

**Impact.** None: snapshots already use only a general compressor; the balance delta in HDiff is between states (needed for diffs), not an intra-state delta before compression.

**Best measured result.** Database load 129ms -&gt; 12.5ms (10x faster), no compression gain (pr:nimbus#2397)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hdiff.rs:385`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L385) balances delta is state-to-state diff then zstd
- [`beacon_node/store/src/hot_cold_store.rs:2143`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2143) snapshots stored as plain SSZ + zstd, no delta
- note: Snapshots are stored without any delta pass (zstd only); the per-state balance delta is inherent to diffs, so the Nimbus anti-pattern does not occur.

**Sources.** [nimbus#2397](https://github.com/status-im/nimbus-eth2/pull/2397)

</details>

<a id="db_cold-072"></a>
<details>
<summary><b>db_cold-072</b> Persist archive/checkpoint states periodically during sync — <i>n/a · medium · S · sync, disk</i></summary>

**Idea.** During initial or range sync, write archive/checkpoint states to the DB at a fixed epoch interval instead of only at migration, so cold storage fills incrementally and a restart does not lose sync progress.

**Gap in Lighthouse.** 

**Impact.** Little: blocks and hot state snapshots/diffs are written on import so a restart resumes from the DB; cold states are produced by finalization migration.

**Best measured result.** Avoids losing 2+ hours of sync progress (pr:lodestar#2151)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2103`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2103) store_cold_state called from migration at finalization
- [`beacon_node/store/src/hot_cold_store.rs:1741`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1741) store_hot_state_diffs stores hot state diffs/snapshots on import
- note: Lighthouse imports synced blocks through the normal pipeline and persists hot state snapshots/diffs at hierarchy points, so there is no in-memory-only sync progress to lose; the problem is specific to the other clients' design.

**Sources.** [lodestar#2151](https://github.com/ChainSafe/lodestar/pull/2151), [prysm#5858](https://github.com/OffchainLabs/prysm/pull/5858)

</details>

<a id="db_cold-096"></a>
<details>
<summary><b>db_cold-096</b> Lazy branch nodes for reloaded tree states — <i>n/a · medium · L · memory, latency, disk</i></summary>

**Idea.** When loading a finalized state stored as tree nodes, create lazy branch nodes that fetch children from the DB only on access instead of loading the full tree.

**Gap in Lighthouse.** 

**Impact.** None: Lighthouse does not store states as DB-resident tree nodes; milhouse trees are built from SSZ bytes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hdiff.rs:173`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L173) HDiffBuffer::from_state/as_state work on SSZ bytes
- [`beacon_node/store/src/hot_cold_store.rs:2235`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2235) load_cold_state_as_snapshot deserializes whole SSZ state
- note: States are persisted as SSZ snapshots plus diffs, not as tree nodes keyed by hash, so lazy branch loading has no counterpart.

**Sources.** [teku#4342](https://github.com/Consensys-Incorporated/teku/pull/4342)

</details>

<a id="db_cold-127"></a>
<details>
<summary><b>db_cold-127</b> Point lookups for strided block range requests — <i>n/a · medium · S · disk, cpu</i></summary>

**Idea.** For blocks-by-range with step &gt; 1, fetch archived blocks by slot point lookups instead of streaming the whole range.

**Gap in Lighthouse.** 

**Impact.** None on mainnet; strided requests are essentially not issued.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/methods.rs:448`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/methods.rs#L448) step field kept only for v1 compat
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1319`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1319) get_block_roots_from_store uses forwards root iterator, then blocks fetched by root

**Sources.** [lodestar#3447](https://github.com/ChainSafe/lodestar/pull/3447)

</details>

<a id="db_cold-022"></a>
<details>
<summary><b>db_cold-022</b> Exponential backoff for failing background storage steps — <i>n/a · low · S · cpu, disk</i></summary>

**Idea.** Apply exponential backoff to periodic background archival/snapshot steps that fail deterministically, so they stop redoing the same expensive reads every slot.

**Gap in Lighthouse.** Lighthouse migration/pruning is triggered by finalization notifications, not a fixed-interval retry loop, so there is no per-tick retry storm to back off.

**Impact.** None meaningful; failures retry at most once per migration window.

**Best measured result.** 328 identical failing retries in 65 minutes, each re-reading ~3900 block bodies (pr:caplin#23252)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/migrate.rs:310`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L310) run_migration is event driven by finalization and gated by epochs_per_migration; prev_migration.epoch is set before the attempt so a failure waits for the next migration window
- [`beacon_node/beacon_chain/src/migrate.rs:366`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L366) failure just warns and returns

**Sources.** [caplin#23252](https://github.com/erigontech/erigon/pull/23252)

</details>

<a id="db_cold-038"></a>
<details>
<summary><b>db_cold-038</b> Cache known stored state tree nodes — <i>n/a · low · L · disk, sync, latency</i></summary>

**Idea.** Keep an in-memory set of state tree branch nodes already stored, so storing finalized states does not repeatedly query the KV store to check node existence.

**Gap in Lighthouse.** Lighthouse does not persist state merkle-tree branch nodes (it stores SSZ snapshots and diffs), so there is no node-existence check against the KV store.

**Impact.** None.

**Best measured result.** Avoids a significant number of requests into LevelDB while syncing (pr:teku#4467)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2102`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2102) stores whole-state snapshots/diffs keyed by slot, no per-tree-node persistence
- [`beacon_node/store/src/hdiff.rs:329`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L329) BytesDiff xdelta over SSZ bytes

**Sources.** [teku#4467](https://github.com/Consensys-Incorporated/teku/pull/4467)

</details>

<a id="db_cold-118"></a>
<details>
<summary><b>db_cold-118</b> Leaner state diffs: whole small fields, parallel shuffle — <i>n/a · low · M · disk, cpu</i></summary>

**Idea.** In the historical state diff store, store tiny fields (inactivity scores, slashings) whole instead of as diffs, reconstruct the previous epoch without DB reads, and compute shuffled sets in parallel.

**Gap in Lighthouse.** Lighthouse does not keep a per-field store with participation/slashings diff tables; the idea is specific to Caplin's per-field layout. The only transferable bit (store inactivity scores whole) is a tuning of CompressedU64Diff with unclear gain.

**Impact.** Not applicable to the single-blob hdiff design; no clear mainnet saving.

**Best measured result.** removed 15GB; dumps 2048 to 1024 added 5GB; 2x faster participation reads (pr:caplin#8963)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hdiff.rs:173`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L173) HDiffBuffer::from_state: whole state SSZ goes through xdelta BytesDiff; only balances, inactivity_scores, validators, historical lists are split out
- [`beacon_node/store/src/hdiff.rs:385`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L385) inactivity_scores use CompressedU64Diff (diffed, not whole)

**Sources.** [caplin#8963](https://github.com/erigontech/erigon/pull/8963)

</details>

<a id="db_cold-129"></a>
<details>
<summary><b>db_cold-129</b> Delete secondary index entries together with pruned blocks — <i>n/a · low · S · disk</i></summary>

**Idea.** When pruning archived blocks, also delete every secondary index entry (slot, root, parent-root indexes) in the same range delete, so no orphaned index keys accumulate on disk.

**Gap in Lighthouse.** Lighthouse never prunes finalized blocks and has no slot/parent-root secondary index columns for blocks, so there are no orphaned index keys. Blob pruning deletes by block root key, the only key.

**Impact.** Nothing to gain today; becomes relevant only if block pruning is added.

**Best measured result.** ~80 bytes per block of leftover index keys (pr:lodestar#10110)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3249-3470`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3249-L3470) only blobs/columns are pruned; blocks are kept forever
- [`consensus/types/src/core/chain_spec.rs:297`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/core/chain_spec.rs#L297) min_epochs_for_block_requests exists but is not used by any pruning
- [`beacon_node/store/src/lib.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/lib.rs) DBColumn: blocks are keyed by root only, no slot or parent-root secondary index

**Sources.** [lodestar#10110](https://github.com/ChainSafe/lodestar/pull/10110)

</details>

<a id="db_cold-142"></a>
<details>
<summary><b>db_cold-142</b> Stream-copy DB files instead of reading into memory — <i>n/a · low · S · memory</i></summary>

**Idea.** When copying or restoring large DB files, stream through the filesystem rather than reading the whole file into memory, avoiding OOM.

**Gap in Lighthouse.** Lighthouse has no DB restore/copy path that reads whole DB files into memory.

**Impact.** None.

**Best measured result.** prevents OOMs during database restoration (pr:prysm#8708)

**Evidence (Lighthouse @ 928b61e719).**

- [`database_manager/src/lib.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/database_manager/src/lib.rs): no backup/restore or file-copy command (grep copy/backup/restore found none)

**Sources.** [prysm#8708](https://github.com/OffchainLabs/prysm/pull/8708)

</details>

