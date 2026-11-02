# db_cold

183 ideas: 34 not, 24 partial, 63 implemented, 62 n/a; 20 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [db_cold-001](#db_cold-001) | Store large static finalized values in RocksDB BlobDB | not | low | L | disk, latency |
| [db_cold-002](#db_cold-002) **★** | Import and export ERA files for history | not | medium | L | sync, startup, disk |
| [db_cold-003](#db_cold-003) **★** | Compress finalized blocks in a slot-ordered freezer column | not | medium | M | disk, bandwidth |
| [db_cold-004](#db_cold-004) **★** | Slot-keyed finalized block archive with root and parent indexes | partial | medium | M | disk, latency, startup, memory |
| [db_cold-005](#db_cold-005) | Move block storage from SQL to embedded KV | n/a | low |  | disk, memory |
| [db_cold-006](#db_cold-006) | Persist latest finalized state on each finalization | implemented | medium | M | startup, disk |
| [db_cold-007](#db_cold-007) | Alternative embedded slasher database backend | implemented | low | S | disk, cpu |
| [db_cold-008](#db_cold-008) **★** | Finalized history in append-only indexed flat files | not | medium | L | disk, sync, startup, memory, bandwidth |
| [db_cold-009](#db_cold-009) | Store payload envelopes as summary, rebuild body from EL | implemented | medium | M | disk |
| [db_cold-010](#db_cold-010) | Periodic finalized state archival with cache pruning | implemented | medium | S | memory, disk |
| [db_cold-011](#db_cold-011) | Store full finalized states only at sparse intervals | implemented | low | S | disk |
| [db_cold-012](#db_cold-012) | Persist finalized state on shutdown | implemented | low | S | startup, sync |
| [db_cold-013](#db_cold-013) **★** | Asynchronous storage IO off import path | partial | medium | L | latency, disk |
| [db_cold-014](#db_cold-014) | Atomic sidecar writes with other storage updates | implemented | low | S | disk |
| [db_cold-015](#db_cold-015) | Plain delete for single-key removals | n/a | medium |  | memory, disk |
| [db_cold-016](#db_cold-016) | Derive fork from epoch when pruning columns | n/a | low |  | disk, cpu |
| [db_cold-017](#db_cold-017) | Compute historical root lazily in ERA export | n/a | low |  | cpu |
| [db_cold-018](#db_cold-018) | Reuse scratch buffer for integer encoding | n/a | low |  | memory, cpu |
| [db_cold-019](#db_cold-019) | Reuse DB key object on reads | n/a | low |  | memory, cpu |
| [db_cold-020](#db_cold-020) | Store nearest state when archive slot missed | n/a | low |  | disk, latency |
| [db_cold-021](#db_cold-021) | Run blob pruning in a background task | implemented | medium | S | latency |
| [db_cold-022](#db_cold-022) | Exponential backoff for failing background storage steps | n/a | low | S | cpu, disk |
| [db_cold-023](#db_cold-023) | Copy DB values as raw bytes during hot-to-cold migration | n/a | medium |  | disk, cpu, memory |
| [db_cold-024](#db_cold-024) | Batch data column sidecar writes in one transaction | implemented | low | S | disk, cpu, latency |
| [db_cold-025](#db_cold-025) | Range query custody columns across slots | partial | low | S | disk, cpu |
| [db_cold-026](#db_cold-026) | Batch slasher min-span reads and writes | implemented | low | S | disk, cpu |
| [db_cold-027](#db_cold-027) | Run finalization migration every N epochs | implemented | low | S | disk |
| [db_cold-028](#db_cold-028) **★** | Bound the size of storage write and migration batches | partial | medium | S | latency, disk, memory |
| [db_cold-029](#db_cold-029) | Bucket scan for slashing-protection export | implemented | low | S | disk, latency |
| [db_cold-030](#db_cold-030) **★** | Big-endian slot-prefixed keys for ordered seeks | partial | medium | L | disk, latency, cpu |
| [db_cold-031](#db_cold-031) | Archive historical states as layered diffs against snapshots | implemented | high | S | disk, cpu, latency, memory |
| [db_cold-032](#db_cold-032) | Store finalized blocks blinded, payload from EL | implemented | high | S | disk |
| [db_cold-033](#db_cold-033) | Separate database for blob sidecars | implemented | medium | S | disk |
| [db_cold-034](#db_cold-034) | Prune blob and column sidecars past DA window by default | implemented | medium | S | disk |
| [db_cold-035](#db_cold-035) | Persist blocks to disk not memory | implemented | low | S | disk, memory |
| [db_cold-036](#db_cold-036) | Upper-bound KV iterators past tombstones | n/a | medium |  | latency, disk, cpu |
| [db_cold-037](#db_cold-037) | In-memory cache for slasher span chunks | not | low | M | disk, latency |
| [db_cold-038](#db_cold-038) | Cache known stored state tree nodes | n/a | low | L | disk, sync, latency |
| [db_cold-039](#db_cold-039) | Cheaper block replay for frozen states | implemented | medium | S | cpu, latency |
| [db_cold-040](#db_cold-040) | Key column sidecars by block root first | implemented | low | S | disk |
| [db_cold-041](#db_cold-041) **★** | Compact DB key ranges after large prunes | partial | medium | S | disk, startup, latency |
| [db_cold-042](#db_cold-042) | Default to compact archive DB layout | n/a | low | S | disk |
| [db_cold-043](#db_cold-043) | Compact encoding of queue-like state fields | not | low | L | disk |
| [db_cold-044](#db_cold-044) | Compact attestation encoding in stored blocks | not | low | L | disk, memory |
| [db_cold-045](#db_cold-045) | Shrink slasher DB keys and records | partial | low | S | disk, memory, cpu |
| [db_cold-046](#db_cold-046) | Run DB compaction rarely | implemented | medium | S | memory, disk |
| [db_cold-047](#db_cold-047) | Compress outside the cache lock | partial | low | S | latency, cpu |
| [db_cold-048](#db_cold-048) | Concurrent archive write and hot delete | not | low | M | disk, latency |
| [db_cold-049](#db_cold-049) | Configurable in-memory diff buffer cache | implemented | low | S | memory |
| [db_cold-050](#db_cold-050) | Prune archived states by correct slot cutoff | n/a | low | S | disk |
| [db_cold-051](#db_cold-051) | Right-sized integer encoding in DB values | n/a | low | S | disk |
| [db_cold-052](#db_cold-052) | Persist cold migration cursor separately | implemented | low | S | cpu, disk |
| [db_cold-053](#db_cold-053) | Store each distinct slasher attestation once | implemented | low | S | disk, memory, cpu |
| [db_cold-054](#db_cold-054) | Store validator immutable fields once, not per state | implemented | medium | S | disk, memory, cpu |
| [db_cold-055](#db_cold-055) **★** | Prune blocks and states older than the retention window | partial | medium | M | disk |
| [db_cold-056](#db_cold-056) **★** | Defer post-finalization archival within slot | not | medium | S | latency |
| [db_cold-057](#db_cold-057) | Delete sidecars of orphaned blocks at finalization | implemented | medium | S | disk, cpu |
| [db_cold-058](#db_cold-058) | Delete unused legacy DB buckets | partial | low | S | disk |
| [db_cold-059](#db_cold-059) | State delta against snapshot, not parent | not | low | L | latency, disk |
| [db_cold-060](#db_cold-060) | Drop in-memory index for archived block range | implemented | low | S | memory |
| [db_cold-061](#db_cold-061) | Do not archive derivable per-epoch data | implemented | low | S | disk |
| [db_cold-062](#db_cold-062) | No delta encoding before general compression | n/a | medium | S | disk, latency |
| [db_cold-063](#db_cold-063) **★** | Store base columns plus proofs, reconstruct extensions | not | high | L | disk |
| [db_cold-064](#db_cold-064) | Remove legacy blob sidecar serving path | n/a | low | S | disk |
| [db_cold-065](#db_cold-065) | Stop scanning obsolete buckets during archival | n/a | low | S | disk, latency |
| [db_cold-066](#db_cold-066) | Encode slasher records outside DB transaction | partial | low | S | cpu, memory |
| [db_cold-067](#db_cold-067) | ERA file layout with trailing slot index | not | low | L | disk, startup |
| [db_cold-068](#db_cold-068) | Zero-copy ETL and pooled writers in storage | n/a | low |  | memory, disk, cpu |
| [db_cold-069](#db_cold-069) | Exact-size copy of compressed cache entries | n/a | low |  | memory |
| [db_cold-070](#db_cold-070) | Faster finalized state pruner rate | n/a | low |  | disk |
| [db_cold-071](#db_cold-071) | Per-index diff for validator and builder registries | partial | low | M | cpu, disk, latency |
| [db_cold-072](#db_cold-072) | Persist archive/checkpoint states periodically during sync | n/a | medium | S | sync, disk |
| [db_cold-073](#db_cold-073) | Split hot and finalized databases, prune non-canonical | implemented | medium | S | disk |
| [db_cold-074](#db_cold-074) | Freezer DB with shared fixed-size vector field tables | implemented | low | S | disk |
| [db_cold-075](#db_cold-075) | Do not store historic finalized states by default | implemented | low | S | disk, startup |
| [db_cold-076](#db_cold-076) | Offline tool to prune historic states/blocks in place | implemented | low | S | disk |
| [db_cold-077](#db_cold-077) | Archive-mode pruner for states older than N epochs | not | low | M | disk |
| [db_cold-078](#db_cold-078) | Resume pruning from a persisted cursor in bounded steps | partial | low | S | disk, cpu, memory, startup, latency |
| [db_cold-079](#db_cold-079) | Throttle sidecar pruning to once per N epochs | implemented | low | S | disk, cpu |
| [db_cold-080](#db_cold-080) | Prune execution payload envelopes with block history | partial | low | S | disk |
| [db_cold-081](#db_cold-081) | Key execution payloads by block root for pruning | implemented | low | S | disk |
| [db_cold-082](#db_cold-082) | Prune per-slot index rows covered by frozen snapshots | n/a | low | S | disk |
| [db_cold-083](#db_cold-083) | Prune old state-diff tree entries | not | low | M | disk |
| [db_cold-084](#db_cold-084) | Prune stale pubkey-to-index table entries | n/a | low | S | disk, memory |
| [db_cold-085](#db_cold-085) | Index light-client header table for pruning | n/a | low | S | disk, cpu |
| [db_cold-086](#db_cold-086) | Fork-choice-driven block archival on finalization | implemented | low | S | disk, cpu, latency |
| [db_cold-087](#db_cold-087) | Forwards freezer iterator for historic root lookups | implemented | low | S | memory, latency, cpu |
| [db_cold-088](#db_cold-088) | Index of finalized block roots for range requests | implemented | low | S | disk, bandwidth |
| [db_cold-089](#db_cold-089) | Finalized state root to slot index | implemented | low | S | latency, disk |
| [db_cold-090](#db_cold-090) **★** | Store data column sidecars as flat files | not | medium | L | disk, cpu |
| [db_cold-091](#db_cold-091) | File datastore for persisted states | not | low | L | disk, memory |
| [db_cold-092](#db_cold-092) | Periodic SQLite WAL checkpoints during bulk writes | n/a | low |  | disk, startup |
| [db_cold-093](#db_cold-093) | Flat per-epoch span records in slasher DB | implemented | low | S | disk, cpu |
| [db_cold-094](#db_cold-094) | Lazy-load finalized validator list | n/a | low |  | startup |
| [db_cold-095](#db_cold-095) | Do not preload all block summaries at startup | implemented | low | S | memory |
| [db_cold-096](#db_cold-096) | Lazy branch nodes for reloaded tree states | n/a | medium | L | memory, latency, disk |
| [db_cold-097](#db_cold-097) | Lazy demand-driven warming of known-branch cache | n/a | low |  | startup, disk |
| [db_cold-098](#db_cold-098) | Size stored-node cache to the full state tree | n/a | low |  | disk, startup |
| [db_cold-099](#db_cold-099) | Store finalized states as shared Merkle tree nodes | n/a | low |  | disk, latency |
| [db_cold-100](#db_cold-100) | Write finalized validators only when a state is stored | implemented | low | S | disk |
| [db_cold-101](#db_cold-101) | Persist decompressed BLS pubkeys | implemented | medium | S | startup, cpu, disk |
| [db_cold-102](#db_cold-102) | Persist derived light-client data in the DB | implemented | low | S | startup, disk, latency |
| [db_cold-103](#db_cold-103) | Pooled buffer for state serialization | not | low | S | memory |
| [db_cold-104](#db_cold-104) | Presize state-diff serialization buffer | partial | low | S | cpu, memory |
| [db_cold-105](#db_cold-105) | Preallocate validator key slice in DB migration | n/a | low |  | cpu, memory |
| [db_cold-106](#db_cold-106) | Pool and cap ETL sort buffers of history collectors | n/a | low |  | memory |
| [db_cold-107](#db_cold-107) | Pool compression decoders, share one low-memory encoder | not | low | S | memory, cpu |
| [db_cold-108](#db_cold-108) | Finer-grained snapshot retirement schedule | n/a | low |  | disk, cpu |
| [db_cold-109](#db_cold-109) | Retire snapshot segments one at a time | n/a | low |  | latency, disk |
| [db_cold-110](#db_cold-110) | Parallel compression of backlogged segments | n/a | low |  | cpu, disk |
| [db_cold-111](#db_cold-111) | Native async generator over DB iterator | n/a | low |  | cpu |
| [db_cold-112](#db_cold-112) | Strict read-only DB open, drop legacy tables | not | low | S | disk |
| [db_cold-113](#db_cold-113) | Single bucket per type, fork from serialized slot | implemented | low | S | disk, cpu |
| [db_cold-114](#db_cold-114) | Store blocks in framed snappy as on the wire | not | low | L | cpu, disk |
| [db_cold-115](#db_cold-115) | Answer has-state without loading the state | not | low | S | cpu, disk |
| [db_cold-116](#db_cold-116) | Hoist prune-interval config conversion | n/a | low | S | cpu |
| [db_cold-117](#db_cold-117) | Read only the last key for latest-slot queries | not | low | S | latency, disk |
| [db_cold-118](#db_cold-118) | Leaner state diffs: whole small fields, parallel shuffle | n/a | low | M | disk, cpu |
| [db_cold-119](#db_cold-119) | Load small diffs before decoding the base snapshot | partial | low | S | cpu, memory, disk |
| [db_cold-120](#db_cold-120) | Memoize deserialized diff anchor states | implemented | medium | S | disk, cpu, startup |
| [db_cold-121](#db_cold-121) | Step by archive-point stride in cold migration | not | low | S | cpu |
| [db_cold-122](#db_cold-122) | Manual pseudo-finalization to migrate and prune | implemented | low | S | disk |
| [db_cold-123](#db_cold-123) | Upgrade the embedded database library | partial | low | M | disk, cpu |
| [db_cold-124](#db_cold-124) | New DB file for schema change, old file read-only | n/a | low |  | disk, latency |
| [db_cold-125](#db_cold-125) | Ordered async storage channel for writes and queries | n/a | low |  | latency, disk |
| [db_cold-126](#db_cold-126) | Per-column larger RocksDB block cache | not | low | S | disk, memory |
| [db_cold-127](#db_cold-127) | Point lookups for strided block range requests | n/a | medium | S | disk, cpu |
| [db_cold-128](#db_cold-128) **★** | Prune contiguous key ranges with one range delete | not | medium | L | disk, cpu |
| [db_cold-129](#db_cold-129) | Delete secondary index entries together with pruned blocks | n/a | low | S | disk |
| [db_cold-130](#db_cold-130) | Shorten block retention window after new forks | not | low | L | disk |
| [db_cold-131](#db_cold-131) | Reuse stored block roots instead of re-hashing | implemented | low | S | cpu |
| [db_cold-132](#db_cold-132) | Delete data violating current retention on mode change | partial | low | M | disk |
| [db_cold-133](#db_cold-133) | Exit background retire loops on cancel, no fsync sleep | n/a | low |  | cpu, latency |
| [db_cold-134](#db_cold-134) | Auto-delete superseded snapshot segment files | n/a | low |  | disk |
| [db_cold-135](#db_cold-135) | Drop defensive copies before sorting collector | n/a | low |  | memory, cpu |
| [db_cold-136](#db_cold-136) | Same hash salt across all snapshot indexes | n/a | low |  | cpu |
| [db_cold-137](#db_cold-137) | Share one DB transaction across batched operations | partial | low | M | cpu, latency |
| [db_cold-138](#db_cold-138) | Skip DB transaction for empty write batches | not | low | S | cpu, disk |
| [db_cold-139](#db_cold-139) | Cap snapshot file size, keep big files immutable | n/a | low |  | disk, cpu |
| [db_cold-140](#db_cold-140) | Retire old historical-state tables into static files | n/a | low |  | disk |
| [db_cold-141](#db_cold-141) | Serialize blocks directly into writer or compressor | n/a | low |  | memory, cpu |
| [db_cold-142](#db_cold-142) | Stream-copy DB files instead of reading into memory | n/a | low | S | memory |
| [db_cold-143](#db_cold-143) **★** | Independent retention mode for data columns | not | medium | S | disk |
| [db_cold-144](#db_cold-144) | Per-type tables instead of one shared KV table | n/a | low |  | startup, disk, latency |
| [db_cold-145](#db_cold-145) | Separate storage queue for column sidecar queries | implemented | medium | S | latency |
| [db_cold-146](#db_cold-146) | Serialize data column persist tasks | n/a | low |  | disk, cpu |
| [db_cold-147](#db_cold-147) **★** | Throttle peer-driven chain data DB queries | partial | medium | S | latency, disk |
| [db_cold-148](#db_cold-148) **★** | Serve historical blocks from ERA files | not | medium | L | disk, sync, startup |
| [db_cold-149](#db_cold-149) | Read whole ERA index in one read | n/a | low |  | disk, latency |
| [db_cold-150](#db_cold-150) | Skip redundant CRC and buffer zeroing on loads | implemented | low | S | cpu, latency |
| [db_cold-151](#db_cold-151) | Load finalized state once at startup for all services | n/a | low |  | startup, cpu |
| [db_cold-152](#db_cold-152) | Skip unneeded genesis and duplicate lookups at startup | not | low | S | startup |
| [db_cold-153](#db_cold-153) | Reuse existing states when archiving finalized states | implemented | high | S | cpu, latency |
| [db_cold-154](#db_cold-154) | Skip finalized state work the storage mode discards | implemented | low | S | cpu, memory |
| [db_cold-155](#db_cold-155) | Skip historical state lookup when not archive | n/a | low | S | latency, disk |
| [db_cold-156](#db_cold-156) | Switch state storage scheme without re-saving history | n/a | low | S | startup, cpu |
| [db_cold-157](#db_cold-157) | Skip archiving blobs/columns outside retention window | implemented | medium | S | disk, sync |
| [db_cold-158](#db_cold-158) | Archive epoch-constant data once per epoch | n/a | low | S | disk |
| [db_cold-159](#db_cold-159) | Write back only dirty slasher span chunks | not | low | S | disk |
| [db_cold-160](#db_cold-160) | Coarser default spacing of full state snapshots | implemented | medium | S | disk |
| [db_cold-161](#db_cold-161) | Migrate hot-to-cold state diffs in one pass | implemented | low | S | cpu, disk |
| [db_cold-162](#db_cold-162) **★** | Structurally-shared tree types for diff buffers | not | medium | M | cpu, memory |
| [db_cold-163](#db_cold-163) **★** | Copy only needed fields when computing state diffs | not | medium | S | memory, cpu |
| [db_cold-164](#db_cold-164) **★** | Apply validator registry diffs in place | partial | medium | M | memory, cpu |
| [db_cold-165](#db_cold-165) **★** | Snappy-compress stored states and blocks | partial | medium | M | disk, sync |
| [db_cold-166](#db_cold-166) | Compress slasher span chunks on disk | implemented | low | S | disk |
| [db_cold-167](#db_cold-167) | Prefix slasher records with signing root | partial | low | S | cpu |
| [db_cold-168](#db_cold-168) | Stream block roots from cursor during state load | implemented | low | S | memory, latency |
| [db_cold-169](#db_cold-169) | Walk parent-child index between finalized checkpoints | implemented | low | S | cpu, latency |
| [db_cold-170](#db_cold-170) | Skip legacy read-only tables when pruning | n/a | low | S | cpu, latency |
| [db_cold-171](#db_cold-171) | Cap state reconstruction batch to yield to migration | implemented | low | S | memory, latency |
| [db_cold-172](#db_cold-172) | Cache regenerated finalized states for sequential reads | implemented | medium | S | cpu, latency |
| [db_cold-173](#db_cold-173) | Reopen DB iterator per migration batch | n/a | low | S | memory, disk |
| [db_cold-174](#db_cold-174) | Encode slot directly into range-scan bounds | implemented | low | S | cpu, memory |
| [db_cold-175](#db_cold-175) | Background service rebuilding historical states by block replay | implemented | low | S | disk, cpu |
| [db_cold-176](#db_cold-176) | Partial-read length for archived era state fields | n/a | low |  | disk, cpu, latency |
| [db_cold-177](#db_cold-177) | Stream snapshot block reads into pooled buffer | n/a | low |  | cpu, memory |
| [db_cold-178](#db_cold-178) | Precompute per-epoch summaries into the database | not | low | M | cpu, latency |
| [db_cold-179](#db_cold-179) | Use read-only DB transactions for lookups | implemented | low | S | latency, disk |
| [db_cold-180](#db_cold-180) | Serialize finalization archival and cache pruning tasks | implemented | low | S | cpu, latency |
| [db_cold-181](#db_cold-181) | Copy immutable validator fields only for new indices on load | partial | low | M | cpu |
| [db_cold-182](#db_cold-182) | Skip state existence lookup when a summary proves it | implemented | low | S | cpu, disk |
| [db_cold-183](#db_cold-183) | DB index from versioned hash to sidecar | n/a | low | S | latency, cpu |

★ actionable. Click an id for the full record.

## Ideas

<a id="db_cold-001"></a>
<details>
<summary><b>db_cold-001</b> Store large static finalized values in RocksDB BlobDB — <i>not · low · L · disk, latency</i></summary>

**Idea.** Store large immutable finalized values (blocks, states, blob and column sidecars) in RocksDB BlobDB mode so values live in separate blob files outside the LSM tree. This cuts write amplification and compaction cost compared to plain SST storage.

**Gap in Lighthouse.** Would require a RocksDB backend with BlobDB or a separate blob-file store for sidecars; large redesign of store backends.

**Impact.** About 5% disk saving on a full custody node and lower compaction cost for sidecar writes in Teku's measure; LevelDB has no equivalent.

**Best measured result.** ~5% disk usage saving on a full custody node (pr:teku#10900)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L931) blobs/columns are plain put_bytes into blobs_db
- [`beacon_node/store/Cargo.toml`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/Cargo.toml): backends are LevelDB and redb, no RocksDB

**Sources.** [teku#10900](https://github.com/Consensys-Incorporated/teku/pull/10900), [teku#10470](https://github.com/Consensys-Incorporated/teku/pull/10470)

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

**Verdict history.** not (checked) → not (refuted)

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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [caplin#8609](https://github.com/erigontech/erigon/pull/8609), [lighthouse#3583](https://github.com/sigp/lighthouse/pull/3583), [lighthouse#5905](https://github.com/sigp/lighthouse/pull/5905)

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

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [caplin#8043](https://github.com/erigontech/erigon/pull/8043), [lodestar@8d3c0182c](https://github.com/ChainSafe/lodestar/commit/8d3c0182cdee), [caplin#6460](https://github.com/erigontech/erigon/pull/6460), [lodestar@69f4864a9](https://github.com/ChainSafe/lodestar/commit/69f4864a9d17), [lodestar@ba8ac4509](https://github.com/ChainSafe/lodestar/commit/ba8ac45099fd), [lodestar#523](https://github.com/ChainSafe/lodestar/pull/523), [nimbus#3320](https://github.com/status-im/nimbus-eth2/pull/3320), [lodestar@ed060f747](https://github.com/ChainSafe/lodestar/commit/ed060f747118), [teku#2205](https://github.com/Consensys-Incorporated/teku/pull/2205)

</details>


<a id="db_cold-005"></a>
<details>
<summary><b>db_cold-005</b> Move block storage from SQL to embedded KV — <i>n/a · low · disk, memory</i></summary>

**Idea.** Store blocks and their indices in an embedded key-value store (MDBX) with integer-keyed indices instead of a SQL database, for cheaper lookups and writes.

**Impact.** Lighthouse never used SQL for blocks.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs): blocks already in a KV store (LevelDB/redb), no SQL

**Sources.** [caplin#8470](https://github.com/erigontech/erigon/pull/8470)

</details>


<a id="db_cold-006"></a>
<details>
<summary><b>db_cold-006</b> Persist latest finalized state on each finalization — <i>implemented · medium · M · startup, disk</i></summary>

**Idea.** On every finalization, persist the latest finalized state (as raw SSZ that loads directly into the in-memory layout) so a restart starts from a recent state instead of replaying from far back or genesis.

**Impact.** On restart, Lighthouse loads the head state from recent hot DB snapshots or diffs, never from genesis.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1661`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1661) store_hot_state persists every epoch-boundary state (snapshot/diff) at import
- [`beacon_node/store/src/hot_cold_store.rs:3532`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3532) migrate_database advances split to the finalized state
- [`beacon_node/store/src/hot_cold_store.rs:407`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L407) hot_storage_strategy hdiff grid in the hot DB

**Skeptic check.** Lighthouse goes further than the idea: it persists all post-finalization epoch-boundary states as hot snapshots or diffs, plus the split state, so a restart replays at most a few epochs. The mechanism differs (hdiff, not raw SSZ of only the finalized state), but the effect is the same.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [silver#79](https://github.com/gattaca-com/silver/pull/79), [lodestar#5520](https://github.com/ChainSafe/lodestar/pull/5520)

</details>


<a id="db_cold-007"></a>
<details>
<summary><b>db_cold-007</b> Alternative embedded slasher database backend — <i>implemented · low · S · disk, cpu</i></summary>

**Idea.** Offer a pure-Rust embedded key-value store (redb) as a slasher database backend alongside LMDB/MDBX.

**Impact.** Only matters for slasher operators; backend exists behind a non-default feature.

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/database/redb_impl.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database/redb_impl.rs) redb backend
- [`slasher/Cargo.toml:12`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/Cargo.toml#L12) redb feature
- [`lighthouse/Cargo.toml:31`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/Cargo.toml#L31) slasher-redb feature

**Skeptic check.** redb backend present alongside lmdb and mdbx. Earlier verdict upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#4529](https://github.com/sigp/lighthouse/pull/4529)

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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [nimbus#820](https://github.com/status-im/nimbus-eth2/pull/820), [lighthouse#9644](https://github.com/sigp/lighthouse/pull/9644), [caplin#8357](https://github.com/erigontech/erigon/pull/8357), [teku#10281](https://github.com/Consensys-Incorporated/teku/pull/10281), [nimbus#1355](https://github.com/status-im/nimbus-eth2/pull/1355), [caplin#8570](https://github.com/erigontech/erigon/pull/8570)

</details>


<a id="db_cold-009"></a>
<details>
<summary><b>db_cold-009</b> Store payload envelopes as summary, rebuild body from EL — <i>implemented · medium · M · disk</i></summary>

**Idea.** For finalized post-Gloas payload envelopes, keep only a small summary/header form (transactions, withdrawals and access list replaced by roots) and delete the payload body, rebuilding the full envelope from the EL by block hash when serving. Keep the full envelope only while execution validity is pending.

**Impact.** Finalized envelopes keep only the summary, and both RPC and the HTTP API rebuild the body from the EL.

**Best measured result.** ~267 KB -&gt; ~1 KB per envelope, &gt;99%, ~690 GB/yr saved (pr:lodestar#10089)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:688-720`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L688-L720) envelope split into PayloadSummary and prunable PayloadBody
- [`beacon_node/beacon_chain/src/migrate.rs:820-872`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L820-L872) prune_finalized_payloads deletes bodies (DeletePayload) for finalized slots below split
- [`beacon_node/beacon_chain/src/payload_envelope_streamer/mod.rs:90-108`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_streamer/mod.rs#L90-L108) serves the stored body if present
- [`beacon_node/beacon_chain/src/payload_envelope_streamer/mod.rs:211`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_streamer/mod.rs#L211) rebuilds missing bodies via get_payload_bodies_by_hash_v2
- [`beacon_node/http_api/src/beacon/execution_payload_envelopes.rs:13`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/execution_payload_envelopes.rs#L13) API uses the streamer
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:6`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L6) RPC uses the streamer

**Skeptic check.** Confirmed the summary/body split, body pruning at finalization, and EL reconstruction by block hash in the streamer that both RPC and the API use. BeaconChain::get_payload_envelope (store-only) returns None for pruned bodies, but it is not the serving path.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#10089](https://github.com/ChainSafe/lodestar/pull/10089), [lodestar#10088](https://github.com/ChainSafe/lodestar/pull/10088), [lighthouse#10015](https://github.com/sigp/lighthouse/pull/10015)

</details>


<a id="db_cold-010"></a>
<details>
<summary><b>db_cold-010</b> Periodic finalized state archival with cache pruning — <i>implemented · medium · S · memory, disk</i></summary>

**Idea.** Run a periodic task that archives finalized states to cold storage and prunes older states from the in-memory state cache, so memory stays bounded.

**Impact.** State cache memory stays bounded, and finalized states are archived on each finalization.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/migrate.rs:166`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L166) process_finalization runs migration on a background thread at each finalization
- [`beacon_node/store/src/hot_cold_store.rs:3532`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3532) migrate_database moves states to the freezer
- [`beacon_node/store/src/hot_cold_store.rs:3665`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3665) calls update_finalized_state
- [`beacon_node/store/src/state_cache.rs:127-160`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L127-L160) update_finalized_state prunes the block map and hdiff buffers

**Skeptic check.** Confirmed that migration and state cache pruning run on every finalization notification, not on a timer, which has the same effect. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@18bb73a89](https://github.com/ChainSafe/lodestar/commit/18bb73a8925d)

</details>


<a id="db_cold-011"></a>
<details>
<summary><b>db_cold-011</b> Store full finalized states only at sparse intervals — <i>implemented · low · S · disk</i></summary>

**Idea.** In the cold/freezer database store a full finalized state only every N slots or epochs (restore points, with an index of archived points), and regenerate intermediate states by replaying blocks from the nearest stored state. This uses far less disk than storing every finalized state.

**Impact.** The freezer stores sparse snapshots plus hierarchical diffs. Intermediate states are rebuilt by replay.

**Best measured result.** mainnet sync disk usage ~1GB with N=1024 (pr:lodestar#1937)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hdiff.rs:660-680`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L660-L680) storage_strategy Snapshot/DiffFrom/ReplayFrom hierarchy
- [`beacon_node/store/src/hot_cold_store.rs:2103-2140`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2103-L2140) store_cold_state stores nothing but a summary for ReplayFrom slots

**Skeptic check.** Confirmed. The hdiff hierarchy is a better form of sparse restore points: it also replaces full snapshots with diffs. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#7433](https://github.com/ChainSafe/lodestar/pull/7433), [teku#2199](https://github.com/Consensys-Incorporated/teku/pull/2199), [prysm#4977](https://github.com/OffchainLabs/prysm/pull/4977), [lighthouse#649](https://github.com/sigp/lighthouse/pull/649), [prysm#5076](https://github.com/OffchainLabs/prysm/pull/5076), [teku#2217](https://github.com/Consensys-Incorporated/teku/pull/2217), [teku#2187](https://github.com/Consensys-Incorporated/teku/pull/2187), [lodestar#1937](https://github.com/ChainSafe/lodestar/pull/1937), [lodestar@3ca6b3cd9](https://github.com/ChainSafe/lodestar/commit/3ca6b3cd9581), [grandine@d319e8a52](https://github.com/grandinetech/grandine/commit/d319e8a52439), [prysm#4971](https://github.com/OffchainLabs/prysm/pull/4971), [prysm#4967](https://github.com/OffchainLabs/prysm/pull/4967), [prysm#5097](https://github.com/OffchainLabs/prysm/pull/5097), [nimbus@bbd94185a](https://github.com/status-im/nimbus-eth2/commit/bbd94185a4b0), [prysm#5023](https://github.com/OffchainLabs/prysm/pull/5023)

</details>


<a id="db_cold-012"></a>
<details>
<summary><b>db_cold-012</b> Persist finalized state on shutdown — <i>implemented · low · S · startup, sync</i></summary>

**Idea.** On graceful shutdown, write the current finalized (checkpoint) state to disk so the next start loads a recent state instead of one up to many epochs old.

**Impact.** None: on restart LH resumes from the persisted head and fork choice, so it never loads an old checkpoint state.

**Best measured result.** avoids ~5-10 min sync times on restart (pr:lodestar#7221)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:8456`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L8456) Drop persists op pool, custody context, fork choice
- [`beacon_node/store/src/hot_cold_store.rs:1661`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1661) store_hot_state writes every imported state (summary/diff/snapshot) to the hot DB
- [`beacon_node/beacon_chain/src/canonical_head.rs:1720`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1720) persist_fork_choice and process_finalization on every finalization

**Skeptic check.** LH does not snapshot on shutdown, but it writes all hot states since the split to disk on import, so the effect (a recent start point after restart) is already present. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#7221](https://github.com/ChainSafe/lodestar/pull/7221), [prysm#6431](https://github.com/OffchainLabs/prysm/pull/6431)

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

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [teku#6218](https://github.com/Consensys-Incorporated/teku/pull/6218), [teku#6222](https://github.com/Consensys-Incorporated/teku/pull/6222)

</details>


<a id="db_cold-014"></a>
<details>
<summary><b>db_cold-014</b> Atomic sidecar writes with other storage updates — <i>implemented · low · S · disk</i></summary>

**Idea.** Write column sidecars in the same atomic DB update as the other storage updates for a block.

**Impact.** Columns are written in the same atomic operation as block and state; the blobs DB is a separate DB but the function handles rollback of the blobs batch if the hot write fails.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:4741`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4741) blob/column store op pushed into the same ops vec as PutBlock/PutState
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4756`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4756) do_atomically_with_block_and_blobs_cache
- [`beacon_node/store/src/hot_cold_store.rs:1459`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1459) splits into hot and blobs DB batches

**Skeptic check.** Verified columns go through the combined atomic call in import_block; the only non-import column write is the weak-subjectivity anchor in builder.rs. Earlier verdict upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#10282](https://github.com/Consensys-Incorporated/teku/pull/10282)

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


<a id="db_cold-016"></a>
<details>
<summary><b>db_cold-016</b> Derive fork from epoch when pruning columns — <i>n/a · low · disk, cpu</i></summary>

**Idea.** When pruning data columns, compute the fork from the epoch once instead of loading each block from disk to learn its fork.

**Impact.** The prune loop must load each block anyway to find its parent root, so deriving the fork from epoch saves no extra load.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3350-3377`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3350-L3377) pruning iterates blocks via ParentRootBlockIterator and takes fork from the already loaded block
- [`beacon_node/store/src/hot_cold_store.rs:3396`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3396) fork_name.fulu_enabled()

**Sources.** [nimbus#8353](https://github.com/status-im/nimbus-eth2/pull/8353)

</details>


<a id="db_cold-017"></a>
<details>
<summary><b>db_cold-017</b> Compute historical root lazily in ERA export — <i>n/a · low · cpu</i></summary>

**Idea.** When exporting ERA files post-Capella, pass historical summaries and compute the historical root only when needed.

**Impact.** Lighthouse has no ERA export, so no historical root to compute lazily.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src) (no ERA export module)

**Sources.** [nimbus#4853](https://github.com/status-im/nimbus-eth2/pull/4853)

</details>


<a id="db_cold-018"></a>
<details>
<summary><b>db_cold-018</b> Reuse scratch buffer for integer encoding — <i>n/a · low · memory, cpu</i></summary>

**Idea.** Encode and decode fixed-size integers in storage code with a reused scratch buffer and direct byte-order calls instead of reflective per-scalar writers that allocate per value.

**Impact.** Go reflective writers; Lighthouse encodes through SSZ into byte vectors with no per-scalar allocation.

**Best measured result.** 200,080 -&gt; 78 allocs/op; 3.24 ms -&gt; 1.31 ms (~2.5x) (pr:caplin#22391)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2103`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2103) store_cold_state uses SSZ/hdiff bytes

**Sources.** [caplin#22391](https://github.com/erigontech/erigon/pull/22391)

</details>


<a id="db_cold-019"></a>
<details>
<summary><b>db_cold-019</b> Reuse DB key object on reads — <i>n/a · low · memory, cpu</i></summary>

**Idea.** Pass an existing key object straight to the DB get instead of rebuilding an identical key for each sidecar lookup, avoiding an allocation per read.

**Impact.** Teku key object reuse; Lighthouse keys are plain byte arrays, nothing to reuse.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2679`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2679) get_data_column builds a byte key per call

**Sources.** [teku#8222](https://github.com/Consensys-Incorporated/teku/pull/8222)

</details>


<a id="db_cold-020"></a>
<details>
<summary><b>db_cold-020</b> Store nearest state when archive slot missed — <i>n/a · low · disk, latency</i></summary>

**Idea.** When archiving at a frequency and the exact target slot's state is not available, store the nearest available state so gaps between snapshots stay small and regeneration stays cheap.

**Impact.** Lighthouse has a state for every slot at finalization and a fixed hdiff grid, so the missing-exact-slot case does not arise.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2103-2137`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2103-L2137) store_cold_state by StorageStrategy
- [`beacon_node/store/src/hdiff.rs:660`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L660) storage_strategy

**Sources.** [teku#2232](https://github.com/Consensys-Incorporated/teku/pull/2232)

</details>


<a id="db_cold-021"></a>
<details>
<summary><b>db_cold-021</b> Run blob pruning in a background task — <i>implemented · medium · S · latency</i></summary>

**Idea.** Run blob/sidecar pruning on a background thread (spawned blocking task or the background migrator) after head update, so the deletes do not stall block import or head update.

**Impact.** Already off the import and head-update path.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:1730`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1730) 'Prune blobs in the background' calls process_prune_blobs after finalization
- [`beacon_node/beacon_chain/src/migrate.rs:213`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L213) process_prune_blobs sends Notification::PruneBlobs to the migrator thread
- [`beacon_node/beacon_chain/src/migrate.rs:248`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L248) run_prune_blobs runs on the background thread
- [`beacon_node/beacon_chain/src/migrate.rs:450`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L450) notifications are coalesced, latest PruneBlobs kept

**Skeptic check.** Confirmed the only hot-path call site sends a channel notification; deletes run in the migrator thread. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@2f565d25b](https://github.com/sigp/lighthouse/commit/2f565d25b263), [lighthouse@caa04db58](https://github.com/sigp/lighthouse/commit/caa04db58a3c)

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


<a id="db_cold-023"></a>
<details>
<summary><b>db_cold-023</b> Copy DB values as raw bytes during hot-to-cold migration — <i>n/a · medium · disk, cpu, memory</i></summary>

**Idea.** When migrating finalized blocks from hot to cold store, or bulk-copying between columns/DBs, read and write the already-serialized value bytes directly in one batch write instead of SSZ-decoding and re-encoding each object. Root/parent indexes can be built from fork-choice summaries instead of decoded blocks.

**Impact.** Lighthouse does not move finalized blocks to the freezer (blocks stay in the hot/blocks column), so there are no per-block decode/encode copies; remaining state work is hdiff computation, not a raw copy.

**Best measured result.** 10 times faster as tested in e2e (pr:lodestar#1759)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3532`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3532) migrate_database writes only slot-&gt;block_root into BeaconBlockRoots (3576) and cold state summaries/diffs
- [`beacon_node/store/src/hot_cold_store.rs:3606`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3606) only diff-boundary states are loaded and re-encoded as hdiffs

**Sources.** [lodestar@f1882361d](https://github.com/ChainSafe/lodestar/commit/f1882361d299), [lodestar@271e4d0d6](https://github.com/ChainSafe/lodestar/commit/271e4d0d65d3), [lodestar#1739](https://github.com/ChainSafe/lodestar/pull/1739), [lodestar#1759](https://github.com/ChainSafe/lodestar/pull/1759), [lodestar@c69b4b8d1](https://github.com/ChainSafe/lodestar/commit/c69b4b8d1356), [teku#5962](https://github.com/Consensys-Incorporated/teku/pull/5962), [teku#4096](https://github.com/Consensys-Incorporated/teku/pull/4096)

</details>


<a id="db_cold-024"></a>
<details>
<summary><b>db_cold-024</b> Batch data column sidecar writes in one transaction — <i>implemented · low · S · disk, cpu, latency</i></summary>

**Idea.** Persist all data column sidecars of a block (or of a time/size window) in one DB transaction with a reused prepared statement, memoizing the shared header root, and serve in-flight writes from memory.

**Impact.** The nimbus 40% came from SQLite per-statement overhead; LH uses leveldb/redb write batches, so there is nothing equivalent to gain.

**Best measured result.** about 40% speedup in batch persisting data column sidecars for fulu (pr:nimbus#8336)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:8407`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L8407) get_blobs_or_columns_store_op makes one PutDataColumns op for all custody columns of a block
- [`beacon_node/store/src/hot_cold_store.rs:1003`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1003) data_columns_as_kv_store_ops
- [`beacon_node/store/src/hot_cold_store.rs:1522`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1522) blobs_db.do_atomically one write batch per import
- [`beacon_node/beacon_chain/src/historical_blocks.rs:432`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_blocks.rs#L432) backfill writes columns of many blocks in one blob_batch
- [`beacon_node/beacon_chain/src/historical_data_columns.rs:202`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_data_columns.rs#L202) historical column import in one batch

**Skeptic check.** Verified import, backfill and historical-column paths all write columns in a single write batch; until import they stay in the DA checker in memory. Earlier evidence cited put_data_columns (hot_cold_store.rs:985, per-column put_bytes) as the in-flight cache path, but that is only used at checkpoint-sync startup (builder.rs:583), not on the hot path.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#8336](https://github.com/status-im/nimbus-eth2/pull/8336), [teku#10293](https://github.com/Consensys-Incorporated/teku/pull/10293)

</details>


<a id="db_cold-025"></a>
<details>
<summary><b>db_cold-025</b> Range query custody columns across slots — <i>partial · low · S · disk, cpu</i></summary>

**Idea.** Query custody column identifiers for a slot range in one batched storage call instead of one per slot, and count reconstructable archived columns toward custody so they are not re-downloaded.

**Gap in Lighthouse.** Columns are keyed by block_root, so no slot-range query exists. get_data_columns scans keys then re-reads each column (double read); it could use the values from the prefix iterator directly and batch across roots. Counting reconstructable archived columns toward custody is absent.

**Impact.** Fewer DB reads when serving or checking by-range columns; small gain on that path only.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2597`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2597) get_data_columns: key scan per block root then a get per column
- [`beacon_node/store/src/hot_cold_store.rs:2657`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2657) get_data_column_keys
- [`beacon_node/network/src/sync/range_data_column_batch_request.rs:344`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_data_column_batch_request.rs#L344) per-root read

**Sources.** [teku#11595](https://github.com/Consensys-Incorporated/teku/pull/11595)

</details>


<a id="db_cold-026"></a>
<details>
<summary><b>db_cold-026</b> Batch slasher min-span reads and writes — <i>implemented · low · S · disk, cpu</i></summary>

**Idea.** In the slasher min/max span update, read and write all affected epochs in one DB transaction instead of one read and write per epoch.

**Impact.** Span updates load and write each chunk once per batch in one transaction, which matches the Prysm change.

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/array.rs:566`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/array.rs#L566) update_array accumulates updated_chunks BTreeMap under one RwTransaction
- [`slasher/src/array.rs:620`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/array.rs#L620) each chunk stored once after all epochs and attestations
- [`slasher/src/array.rs:397`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/array.rs#L397) get_chunk_for_update loads each chunk once

**Skeptic check.** Confirmed the chunked span design batches all epoch reads and writes in one transaction. Earlier verdict upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#5591](https://github.com/OffchainLabs/prysm/pull/5591)

</details>


<a id="db_cold-027"></a>
<details>
<summary><b>db_cold-027</b> Run finalization migration every N epochs — <i>implemented · low · S · disk</i></summary>

**Idea.** Run the hot-to-cold finalization migration only every N finalized epochs instead of every finalization, batching reads, deletes and freezer writes into larger transactions.

**Impact.** Mechanism is the Lighthouse PR itself; only the default (1) could be tuned.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/migrate.rs:31`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L31) DEFAULT_EPOCHS_PER_MIGRATION
- [`beacon_node/beacon_chain/src/migrate.rs:314`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L314) run_migration defers unless epoch &gt;= prev.epoch + epochs_per_migration
- [`beacon_node/src/cli.rs:770`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L770) --epochs-per-migration flag

**Skeptic check.** Confirmed the deferral check and the CLI flag. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#3582](https://github.com/sigp/lighthouse/pull/3582)

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

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [teku#3143](https://github.com/Consensys-Incorporated/teku/pull/3143), [teku#6597](https://github.com/Consensys-Incorporated/teku/pull/6597), [caplin#21594](https://github.com/erigontech/erigon/pull/21594), [grandine@a0ef64e37](https://github.com/grandinetech/grandine/commit/a0ef64e37522), [grandine#650](https://github.com/grandinetech/grandine/pull/650), [teku#7483](https://github.com/Consensys-Incorporated/teku/pull/7483), [prysm#15746](https://github.com/OffchainLabs/prysm/pull/15746), [caplin#11723](https://github.com/erigontech/erigon/pull/11723), [prysm#9298](https://github.com/OffchainLabs/prysm/pull/9298), [lodestar@b504f7815](https://github.com/ChainSafe/lodestar/commit/b504f7815a2d)

</details>


<a id="db_cold-029"></a>
<details>
<summary><b>db_cold-029</b> Bucket scan for slashing-protection export — <i>implemented · low · S · disk, latency</i></summary>

**Idea.** Export slashing-protection proposal history by iterating the bucket keys in one transaction instead of one query per slot.

**Impact.** No per-slot queries exist.

**Best measured result.** Says lookups are 'a lot faster'; no numbers (pr:prysm#8378)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/slashing_protection/src/slashing_database.rs:937`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L937) export_interchange_info opens one transaction
- [`validator_client/slashing_protection/src/slashing_database.rs:984`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L984) export_interchange_blocks_for_validator one SELECT per validator, ORDER BY slot
- [`validator_client/slashing_protection/src/slashing_database.rs:1002`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L1002) attestations one SELECT per validator

**Skeptic check.** Export is one range query per validator inside one SQLite transaction, which is the bucket-scan equivalent. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#8378](https://github.com/OffchainLabs/prysm/pull/8378)

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

**Verdict history.** not (checked) → partial (refuted)

**Sources.** [prysm#14151](https://github.com/OffchainLabs/prysm/pull/14151), [prysm#6461](https://github.com/OffchainLabs/prysm/pull/6461), [teku#10725](https://github.com/Consensys-Incorporated/teku/pull/10725), [ethlambda#453](https://github.com/lambdaclass/ethlambda/pull/453), [teku#6910](https://github.com/Consensys-Incorporated/teku/pull/6910)

</details>


<a id="db_cold-031"></a>
<details>
<summary><b>db_cold-031</b> Archive historical states as layered diffs against snapshots — <i>implemented · high · S · disk, cpu, latency, memory</i></summary>

**Idea.** Store archived states as sparse full snapshots plus diffs (binary or per-field, possibly at hierarchical slot intervals) against a base snapshot, and rebuild a state by applying a short chain of diffs plus a short block replay. This cuts archive disk use by about an order of magnitude versus full states or restore points and replays fewer blocks per load.

**Impact.** Already present (tree-states hdiff, pr:lighthouse#5978).

**Best measured result.** archival states 1.5-2Tb -&gt; ~150-200Gb; deltas 150Kb-1.5Mb vs ~200MB snapshot; 0-32 transitions vs 0-1024 (pr:grandine#906)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hdiff.rs:33`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L33) HierarchyConfig layered snapshots and diffs
- [`beacon_node/store/src/hot_cold_store.rs:218`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L218) hierarchy moduli from config used for cold and hot states
- [`beacon_node/store/src/hot_cold_store.rs:1771`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1771) store_hot_state_as_diff (hot DB also uses diffs)

**Skeptic check.** Hierarchical diffs are used for the freezer and also the hot DB. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#7005](https://github.com/ChainSafe/lodestar/pull/7005), [lodestar#7664](https://github.com/ChainSafe/lodestar/pull/7664), [lodestar#7874](https://github.com/ChainSafe/lodestar/pull/7874), [grandine#523](https://github.com/grandinetech/grandine/pull/523), [grandine#906](https://github.com/grandinetech/grandine/pull/906), [caplin#9414](https://github.com/erigontech/erigon/pull/9414), [lodestar#8796](https://github.com/ChainSafe/lodestar/pull/8796), [lodestar#7663](https://github.com/ChainSafe/lodestar/pull/7663), [prysm#15288](https://github.com/OffchainLabs/prysm/pull/15288), [prysm#15437](https://github.com/OffchainLabs/prysm/pull/15437), [prysm#15438](https://github.com/OffchainLabs/prysm/pull/15438), [prysm#15439](https://github.com/OffchainLabs/prysm/pull/15439), [prysm#16033](https://github.com/OffchainLabs/prysm/pull/16033), [lighthouse#5978](https://github.com/sigp/lighthouse/pull/5978), [prysm#16049](https://github.com/OffchainLabs/prysm/pull/16049), [lighthouse#4652](https://github.com/sigp/lighthouse/pull/4652), [lodestar#7901](https://github.com/ChainSafe/lodestar/pull/7901), [prysm#15250](https://github.com/OffchainLabs/prysm/pull/15250), [prysm#16203](https://github.com/OffchainLabs/prysm/pull/16203)

</details>


<a id="db_cold-032"></a>
<details>
<summary><b>db_cold-032</b> Store finalized blocks blinded, payload from EL — <i>implemented · high · S · disk</i></summary>

**Idea.** Store post-merge beacon blocks with the execution payload replaced by its header, and rebuild full payloads from the execution client on demand when serving blocks. Transactions already held by the EL are then not stored twice.

**Impact.** Finalized payload duplication already avoided on import, backfill, RPC and API paths.

**Best measured result.** ~29.5 MB/hour, ~258 GB/year of payload duplication avoided (pr:prysm#11010)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:551`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L551) blinded_block_as_kv_store_ops stores every block without payload
- [`beacon_node/store/src/hot_cold_store.rs:3119`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3119) try_prune_execution_payloads deletes finalized payloads
- [`beacon_node/store/src/config.rs:117`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L117) prune_payloads default true
- [`beacon_node/beacon_chain/src/beacon_block_streamer.rs:234`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_block_streamer.rs#L234) RPC block serving rebuilds payloads via get_payload_bodies_by_hash
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1288`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1288) get_block (API) loads the payload from the EL for blinded blocks
- [`beacon_node/beacon_chain/src/historical_blocks.rs:286`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_blocks.rs#L286) backfill stores only envelope summary when prune_payloads

**Skeptic check.** Verified the store, prune, and both serving paths (RPC streamer and API get_block). The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#11097](https://github.com/OffchainLabs/prysm/pull/11097), [teku#5980](https://github.com/Consensys-Incorporated/teku/pull/5980), [prysm#10709](https://github.com/OffchainLabs/prysm/pull/10709), [caplin#9058](https://github.com/erigontech/erigon/pull/9058), [grandine@4019f077e](https://github.com/grandinetech/grandine/commit/4019f077e9f9), [prysm#10580](https://github.com/OffchainLabs/prysm/pull/10580), [prysm#11591](https://github.com/OffchainLabs/prysm/pull/11591), [prysm#11010](https://github.com/OffchainLabs/prysm/pull/11010), [caplin#8080](https://github.com/erigontech/erigon/pull/8080), [prysm#10989](https://github.com/OffchainLabs/prysm/pull/10989), [prysm#10988](https://github.com/OffchainLabs/prysm/pull/10988)

</details>


<a id="db_cold-033"></a>
<details>
<summary><b>db_cold-033</b> Separate database for blob sidecars — <i>implemented · medium · S · disk</i></summary>

**Idea.** Store blob sidecars in a separate database or blob store from the hot and freezer data, so the hot DB stays small and blobs can live on other storage and be pruned independently.

**Impact.** Already separate; --blobs-dir puts it on other storage.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:68`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L68) blobs_db field
- [`beacon_node/store/src/hot_cold_store.rs:259`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L259) opened from separate blobs_db_path
- [`beacon_node/store/src/hot_cold_store.rs:1522`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1522) blobs and columns written to blobs_db

**Skeptic check.** All blob and column writes (import, backfill, historical columns) go to blobs_db. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#3869](https://github.com/sigp/lighthouse/pull/3869), [caplin#9573](https://github.com/erigontech/erigon/pull/9573), [lighthouse@f9737628f](https://github.com/sigp/lighthouse/commit/f9737628fc09)

</details>


<a id="db_cold-034"></a>
<details>
<summary><b>db_cold-034</b> Prune blob and column sidecars past DA window by default — <i>implemented · medium · S · disk</i></summary>

**Idea.** Delete stored blob sidecars and data column sidecars older than the data availability retention window, enabled by default and run at each finalization/migration rather than only at startup, so sidecar storage stays bounded.

**Impact.** Sidecar storage bounded by the DA window by default.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/config.rs:30-31`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L30-L31) DEFAULT_EPOCHS_PER_BLOB_PRUNE=1, margin 0
- [`beacon_node/store/src/config.rs:120`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L120) prune_blobs: true
- [`beacon_node/beacon_chain/src/canonical_head.rs:1730-1735`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1730-L1735) process_prune_blobs after every finalization
- [`beacon_node/store/src/hot_cold_store.rs:3277-3400`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3277-L3400) try_prune_blobs walks back from DA boundary, handles blob and data column columns

**Skeptic check.** Verified default-on pruning triggered from after_finalization on the migrator thread each finalization (every epoch by default), covering both blobs and Fulu columns. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@fe0c91140](https://github.com/sigp/lighthouse/commit/fe0c9114027f), [lighthouse@7bf88c233](https://github.com/sigp/lighthouse/commit/7bf88c2336fc), [lodestar#7717](https://github.com/ChainSafe/lodestar/pull/7717), [nimbus#7369](https://github.com/status-im/nimbus-eth2/pull/7369), [lighthouse@d67468d73](https://github.com/sigp/lighthouse/commit/d67468d737a5)

</details>


<a id="db_cold-035"></a>
<details>
<summary><b>db_cold-035</b> Persist blocks to disk not memory — <i>implemented · low · S · disk, memory</i></summary>

**Idea.** Persist blocks to an on-disk block store so block history is not held in memory.

**Impact.** None left: blocks live in the on-disk store and the optional in-memory block LRU is off by default.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:507`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L507) put_block writes to hot_db
- [`beacon_node/store/src/hot_cold_store.rs:631`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L631) get_full_block reads from DB
- [`beacon_node/store/src/config.rs:22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L22) DEFAULT_BLOCK_CACHE_SIZE = 0

**Skeptic check.** Confirmed that blocks are persisted in the KV store and read back from it. The in-memory block cache defaults to size 0. The earlier verdict was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#7941](https://github.com/erigontech/erigon/pull/7941)

</details>


<a id="db_cold-036"></a>
<details>
<summary><b>db_cold-036</b> Upper-bound KV iterators past tombstones — <i>n/a · medium · latency, disk, cpu</i></summary>

**Idea.** Set an exclusive upper bound on ranged key-value iterators so seeks stop at the range end instead of walking deletion tombstones, and skip the DB for ranges below the prune watermark.

**Impact.** Lighthouse keys columns by block_root+index and serves by-range via block-root iterators and point gets, not slot-keyed KV range scans over tombstones; the Teku failure mode does not arise.

**Best measured result.** 32-slot request in 1M-4M tombstone band 41-167 ms -&gt; ~1.5 us (data columns); minutes-long requests on Sepolia (pr:teku#11585)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2657`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2657) get_data_column_keys seeks by block_root prefix with take_while
- [`beacon_node/store/src/database/leveldb_impl.rs:204`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/leveldb_impl.rs#L204) iter_column_from has no upper bound, only a column take_while

**Sources.** [teku#11585](https://github.com/Consensys-Incorporated/teku/pull/11585)

</details>


<a id="db_cold-037"></a>
<details>
<summary><b>db_cold-037</b> In-memory cache for slasher span chunks — <i>not · low · M · disk, latency</i></summary>

**Idea.** Cache slasher span chunks in memory in front of the slasher DB so span reads and writes do not hit disk on every update.

**Gap in Lighthouse.** Add an LRU of decoded Chunk values keyed by (validator_chunk_index, chunk_index) in slasher/src/database.rs, consulted in TargetArrayChunk::load and updated on store, cleared on txn abort.

**Impact.** Slasher batches skip an LMDB read plus zlib inflate for hot chunks; helps only nodes running --slasher.

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/array.rs:154`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/array.rs#L154) TargetArrayChunk::load reads and zlib-decodes from txn each batch
- [`slasher/src/database.rs:75`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L75) only an attestation-root LRU exists, no chunk cache

**Sources.** [prysm#6199](https://github.com/OffchainLabs/prysm/pull/6199), [prysm#6248](https://github.com/OffchainLabs/prysm/pull/6248)

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


<a id="db_cold-039"></a>
<details>
<summary><b>db_cold-039</b> Cheaper block replay for frozen states — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** When loading frozen states, reuse block roots from the state-root iterator during replay instead of rehashing, pass the proposer index through instead of recomputing, and avoid state clones in the hot/cold DB.

**Impact.** Frozen-state replay avoids state rehashing and proposer recomputation; tree-states makes clones cheap.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2388-2394`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2388-L2394) cold replay passes forwards_state_roots_iterator
- [`beacon_node/store/src/hot_cold_store.rs:2565-2567`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2565-L2567) no signature verification, minimal block root verification
- [`consensus/state_processing/src/block_replayer.rs:184`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/block_replayer.rs#L184) state roots from iterator
- [`consensus/state_processing/src/block_replayer.rs:256-260`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/block_replayer.rs#L256-L260) proposer index taken from block

**Skeptic check.** Confirmed on the frozen path (load_cold_state_by_slot). The hot replay path at hot_cold_store.rs:2078 uses no_state_root_iter, but the idea is about frozen states and hot replay is short and uses the incremental tree hash cache.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#2431](https://github.com/sigp/lighthouse/pull/2431)

</details>


<a id="db_cold-040"></a>
<details>
<summary><b>db_cold-040</b> Key column sidecars by block root first — <i>implemented · low · S · disk</i></summary>

**Idea.** Key data column sidecars by block root then column index so all columns of a block are adjacent and can be read or deleted as one range.

**Impact.** The key layout matches the idea (Nimbus #7199 only changed the key layout). Pruning still does 128 point existence checks and single-key deletes per block, not one range delete. This is a minor background cost, which a code comment already admits.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/lib.rs:144`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/lib.rs#L144) get_data_column_key = block_root ++ column_index
- [`beacon_node/store/src/hot_cold_store.rs:2657`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2657) get_data_column_keys prefix range scan by block root
- [`beacon_node/store/src/hot_cold_store.rs:3396-3415`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3396-L3415) pruning checks key_exists for all 128 keys and deletes them one by one

**Skeptic check.** Confirmed that the layout is block_root first, so a block's columns sit next to each other, and that reads use a prefix scan. try_prune_blobs does not use that range: it probes every column index through get_all_data_column_keys. This is a small refinement, not a missing layout.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#7199](https://github.com/status-im/nimbus-eth2/pull/7199)

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

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [lighthouse#5142](https://github.com/sigp/lighthouse/pull/5142), [lighthouse#1871](https://github.com/sigp/lighthouse/pull/1871), [lighthouse#6667](https://github.com/sigp/lighthouse/pull/6667), [lodestar#10460](https://github.com/ChainSafe/lodestar/pull/10460)

</details>


<a id="db_cold-042"></a>
<details>
<summary><b>db_cold-042</b> Default to compact archive DB layout — <i>n/a · low · S · disk</i></summary>

**Idea.** Default archive storage to the more compact DB layout and use the tree layout only when storing every state.

**Impact.** Lighthouse has a single cold layout (hdiff), so there is no default to choose.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hdiff.rs:1`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L1) only the hierarchical diff layout exists for the freezer

**Sources.** [teku#5766](https://github.com/Consensys-Incorporated/teku/pull/5766)

</details>


<a id="db_cold-043"></a>
<details>
<summary><b>db_cold-043</b> Compact encoding of queue-like state fields — <i>not · low · L · disk</i></summary>

**Idea.** When storing historical states, encode queue-like fields (pending lists) compactly to shrink storage and speed reads.

**Gap in Lighthouse.** Would need custom encoding of pending_deposits/pending_consolidations/partial_withdrawals in HDiffBuffer::from_state/as_state and a schema migration.

**Impact.** Pending queues are small and already shrunk by xdelta3 diffs and zstd; negligible disk or read saving, and most nodes prune historic states.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hdiff.rs:100-140`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L100-L140) snapshot/diff splits out balances, inactivity scores and validators only; the rest of the state is SSZ then xdelta3/zstd
- [`beacon_node/store/src/hot_cold_store.rs:2145`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2145) store_cold_state_as_snapshot is plain SSZ + zstd

**Sources.** [caplin#14158](https://github.com/erigontech/erigon/pull/14158)

</details>


<a id="db_cold-044"></a>
<details>
<summary><b>db_cold-044</b> Compact attestation encoding in stored blocks — <i>not · low · L · disk, memory</i></summary>

**Idea.** Store block attestations with shared, deduplicated attestation data plus bitlists instead of full SSZ per attestation.

**Gap in Lighthouse.** Would need a custom block storage format deduplicating AttestationData across attestations in put_block / get_block paths, plus a schema migration.

**Impact.** zstd already squeezes repeated attestation data; saving is a few percent of block bytes, and only nodes keeping full history benefit.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2149`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2149) and 2194 blocks are stored as full SSZ then zstd, no attestation-data dedup
- [`beacon_node/store/src/impls`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/impls)/ (only execution payload impls, no block-specific encoding)

**Sources.** [caplin#6442](https://github.com/erigontech/erigon/pull/6442), [caplin#6446](https://github.com/erigontech/erigon/pull/6446)

</details>


<a id="db_cold-045"></a>
<details>
<summary><b>db_cold-045</b> Shrink slasher DB keys and records — <i>partial · low · S · disk, memory, cpu</i></summary>

**Idea.** Shrink slasher on-disk keys (short validator index and modular epoch) and attester records, and compress stored attestation data, to cut slasher DB size.

**Gap in Lighthouse.** Key and record shrinking is done (7-byte keys, 6-byte records). The 'compress stored attestation data' part (prysm#8701 snappy on all attestation data) is missing: Database::store_indexed_attestation stores the IndexedAttestation as plain SSZ (u64 attesting indices + signature) with no compression; ProposerKey stays 16 bytes.

**Impact.** Small: attestations are already deduplicated, so compressing the indexed_attestation_db would only cut the remaining slasher DB size by a modest amount.

**Best measured result.** keys 16-&gt;7 bytes, records 64-&gt;6 bytes (pr:lighthouse#2776)

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/database.rs:65-68`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L65-L68) ATTESTER_KEY_SIZE=7, INDEXED_ATTESTATION_ID_SIZE=6, PROPOSER_KEY_SIZE=16
- [`slasher/src/attester_record.rs:22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/attester_record.rs#L22) CompactAttesterRecord is a 6-byte id
- [`slasher/src/array.rs:180`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/array.rs#L180) only min/max chunks are zstd-compressed
- [`slasher/src/database.rs:524-527`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L524-L527) store_indexed_attestation writes raw SSZ, uncompressed

**Skeptic check.** Key/record sizes match PR 2776. The earlier evidence cited chunk zstd as the compression part, but that applies to the min/max arrays, not to stored attestation data.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [prysm#8701](https://github.com/OffchainLabs/prysm/pull/8701), [lighthouse#2776](https://github.com/sigp/lighthouse/pull/2776)

</details>


<a id="db_cold-046"></a>
<details>
<summary><b>db_cold-046</b> Run DB compaction rarely — <i>implemented · medium · S · memory, disk</i></summary>

**Idea.** Run full DB compaction only rarely (about every 1024 epochs, robust to skipped epochs) and make it optional, since frequent compaction caused OOM and consistency problems.

**Impact.** Compaction happens rarely and can be disabled.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/migrate.rs:19-23`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L19-L23) MAX 7d, MIN 2h, COMPACTION_FINALITY_DISTANCE 1024
- [`beacon_node/beacon_chain/src/migrate.rs:919-953`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L919-L953) run_compaction gated by compact_on_prune and the time/finality rule
- [`beacon_node/store/src/config.rs:115-116`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L115-L116) compact_on_init false, compact_on_prune configurable

**Skeptic check.** The only automatic compaction call (migrate.rs:411) goes through run_compaction, which uses a persisted timestamp so skipped epochs do not matter. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#1916](https://github.com/sigp/lighthouse/pull/1916)

</details>


<a id="db_cold-047"></a>
<details>
<summary><b>db_cold-047</b> Compress outside the cache lock — <i>partial · low · S · latency, cpu</i></summary>

**Idea.** In the state diff cache, do compression and decompression outside the mutex-protected section to cut lock contention.

**Gap in Lighthouse.** Diff decode, apply and zstd do run outside the lock. The expensive buffer conversions do not. In the hot StateCache, get_hdiff_buffer_by_state_root runs HDiffBuffer::from_state (it SSZ-encodes the whole state and copies validators, balances and inactivity scores into Vecs) inside the state_cache mutex, and put_hdiff_buffer and the cache-hit path deep-clone multi-hundred-MB buffers inside it too. Block import and get_advanced_hot_state use that same mutex. The cold HistoricStateCache does the same in get_hdiff_buffer and get_state (as_state). Fix: under the lock, clone only the Arc-backed BeaconState (or hold buffers in an Arc), and do the from_state/as_state conversion after the guard is dropped.

**Impact.** Removes lock hold times of tens of ms (full-state SSZ encode and Vec clones) on the hot state cache mutex when hot states are stored or loaded as diffs, typically at epoch boundaries and during non-finality. It also cuts contention for historic-state API serving.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2424-2468`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2424-L2468) cold diff read/decode/apply run outside historic_state_cache lock
- [`beacon_node/store/src/state_cache.rs:295-310`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L295-L310) get_hdiff_buffer_by_state_root clones buffer or runs HDiffBuffer::from_state (full-state SSZ encode + validators to_vec) while holding the hot state_cache mutex
- [`beacon_node/store/src/state_cache.rs:284-292`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L284-L292) put_hdiff_buffer deep-clones the buffer under the state_cache lock
- [`beacon_node/store/src/hot_cold_store.rs:1861-1866`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1861-L1866),1920-1923 load_hot_hdiff_buffer takes state_cache.lock() for get/put
- [`beacon_node/store/src/hot_cold_store.rs:1777-1794`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1777-L1794) store_hot_state_as_diff calls load_hot_hdiff_buffer on the state-store path
- [`beacon_node/store/src/historic_state_cache.rs:33-66`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/historic_state_cache.rs#L33-L66) get_hdiff_buffer from_state/clone and get_state as_state (SSZ decode) under the historic cache lock

**Skeptic check.** The earlier evidence was right that compression and diff application run outside the lock. It missed the hot StateCache path, where HDiffBuffer::from_state and large buffer clones run while the state_cache mutex is held. That is the same contention the Prysm PR removed.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [prysm#17406](https://github.com/OffchainLabs/prysm/pull/17406)

</details>


<a id="db_cold-048"></a>
<details>
<summary><b>db_cold-048</b> Concurrent archive write and hot delete — <i>not · low · M · disk, latency</i></summary>

**Idea.** During finalization pruning, issue the cold archive write and the hot batch delete concurrently instead of sequentially.

**Gap in Lighthouse.** Run prune_hot_db's batch delete concurrently with the cold write in Migrator::run_migration; must stay ordered after the cold sync and split update for crash safety.

**Impact.** Migration runs once per finalization on a background thread; for pruned nodes the cold write is tiny, so overlap saves little, and crash-safety ordering limits it.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3532`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3532) migrate_database writes cold ops (3615, 3626) and syncs, then updates split
- [`beacon_node/beacon_chain/src/migrate.rs:348-372`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L348-L372) migrate_database then prune_hot_db run sequentially on the migrator thread

**Sources.** [lodestar@00336bb48](https://github.com/ChainSafe/lodestar/commit/00336bb48266)

</details>


<a id="db_cold-049"></a>
<details>
<summary><b>db_cold-049</b> Configurable in-memory diff buffer cache — <i>implemented · low · S · memory</i></summary>

**Idea.** Expose the number of state diff buffers kept in memory as a flag so memory can be traded against reconstruction time.

**Impact.** Already configurable for both the hot and the cold buffer caches.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/src/cli.rs:809`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L809) --hdiff-buffer-cache-size
- [`beacon_node/src/cli.rs:821`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L821) --hot-hdiff-buffer-cache-size
- [`beacon_node/src/config.rs:417-426`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/config.rs#L417-L426) wired into StoreConfig
- [`beacon_node/store/src/hot_cold_store.rs:235-238`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L235-L238) caches sized from config

**Skeptic check.** This is Lighthouse's own PR. Confirmed that both flags are parsed and used to size the caches.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#4420](https://github.com/sigp/lighthouse/pull/4420)

</details>


<a id="db_cold-050"></a>
<details>
<summary><b>db_cold-050</b> Prune archived states by correct slot cutoff — <i>n/a · low · S · disk</i></summary>

**Idea.** Key archived states by slot and compute the prune cutoff as a slot (finalized epoch start slot, capped at the latest archived state), so the retention policy actually deletes old archived states.

**Impact.** Lighthouse has no rolling archived-state retention window to get the cutoff wrong; pruning is all-or-nothing.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3471`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3471) prune_historic_states deletes all freezer states at once; no per-slot cutoff retention
- [`beacon_node/store/src/hot_cold_store.rs:2297`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2297) cold states are keyed by big-endian slot

**Sources.** [lodestar#4508](https://github.com/ChainSafe/lodestar/pull/4508), [lodestar#10106](https://github.com/ChainSafe/lodestar/pull/10106)

</details>


<a id="db_cold-051"></a>
<details>
<summary><b>db_cold-051</b> Right-sized integer encoding in DB values — <i>n/a · low · S · disk</i></summary>

**Idea.** Encode slot index values as 8 bytes rather than an oversized buffer to shrink DB entries.

**Impact.** LH stores fixed-width integer keys already; no oversized buffer exists.

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/database.rs:177`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L177) epoch key as 8-byte BE
- [`slasher/src/database.rs:204`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L204) attestation id 6 bytes

**Sources.** [lodestar#2291](https://github.com/ChainSafe/lodestar/pull/2291)

</details>


<a id="db_cold-052"></a>
<details>
<summary><b>db_cold-052</b> Persist cold migration cursor separately — <i>implemented · low · S · cpu, disk</i></summary>

**Idea.** Keep the hot-to-cold migration progress cursor separate from cached finalized state info so progress is saved and migration work is not redone.

**Impact.** The split is already an independent persisted cursor that is updated on every successful migration. It does not depend on any cache being populated.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3567-3571`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3567-L3571) migration starts from the persisted current_split
- [`beacon_node/store/src/hot_cold_store.rs:3646-3659`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3646-L3659) Split persisted with put_sync before in-memory update
- [`beacon_node/store/src/metadata.rs:14`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/metadata.rs#L14) SPLIT_KEY

**Skeptic check.** The Prysm bug was that the cursor was saved only when the epoch-boundary cache had the finalized state. In Lighthouse, migrate_database always writes the Split. A crash during one migration redoes only that batch, by design.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#17345](https://github.com/OffchainLabs/prysm/pull/17345)

</details>


<a id="db_cold-053"></a>
<details>
<summary><b>db_cold-053</b> Store each distinct slasher attestation once — <i>implemented · low · S · disk, memory, cpu</i></summary>

**Idea.** In the slasher, store each distinct attestation once (keyed by root plus attesting-indices hash, shared by reference) with small per-validator pointers, instead of a full copy per attesting validator.

**Impact.** Each distinct attestation is stored once with 6-byte per-validator pointers.

**Best measured result.** stores only 1-2% of attestations seen, a 50-100x reduction in data stored (pr:lighthouse#2767)

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/database.rs:498-533`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L498-L533) store_indexed_attestation looks up (target, hash) id and stores each attestation once
- [`slasher/src/database.rs:170`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L170) IndexedAttestationIdKey
- [`slasher/src/attester_record.rs:22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/attester_record.rs#L22) per-validator CompactAttesterRecord pointer

**Skeptic check.** Verified dedup by (target epoch, indexed attestation hash) and per-validator id pointers. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#2767](https://github.com/sigp/lighthouse/pull/2767), [prysm#8720](https://github.com/OffchainLabs/prysm/pull/8720)

</details>


<a id="db_cold-054"></a>
<details>
<summary><b>db_cold-054</b> Store validator immutable fields once, not per state — <i>implemented · medium · S · disk, memory, cpu</i></summary>

**Idea.** Do not store the full validator registry (or its immutable fields such as pubkeys and withdrawal credentials) in every stored historical state; store them once in a separate table and persist states with only mutable fields (or with pubkeys zeroed so compression removes them), restoring them on load. This shrinks each stored state greatly.

**Impact.** Immutable validator fields are stored only in rare snapshots; diffs carry only changes.

**Best measured result.** ~20% faster overall ncli_db bench; DB block+state store ~60% faster; DB size 17GiB to 3.9GiB (75% smaller) (pr:nimbus#2297)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hdiff.rs:173-185`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L173-L185) HDiffBuffer takes validators out of the state SSZ
- [`beacon_node/store/src/hdiff.rs:440-470`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L440-L470) ValidatorsDiff emits only changed validators and zeroes unchanged pubkey/withdrawal_credentials

**Skeptic check.** Equivalent mechanism with the same effect: hdiff layers store the registry only in snapshot layers, and diffs zero unchanged pubkeys. Full snapshots still hold the registry, which the earlier note stated correctly.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#9155](https://github.com/OffchainLabs/prysm/pull/9155), [lighthouse#3626](https://github.com/sigp/lighthouse/pull/3626), [nimbus#2514](https://github.com/status-im/nimbus-eth2/pull/2514), [nimbus#2297](https://github.com/status-im/nimbus-eth2/pull/2297), [grandine@d6269806c](https://github.com/grandinetech/grandine/commit/d6269806c780), [grandine#611](https://github.com/grandinetech/grandine/pull/611)

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

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [prysm#2433](https://github.com/OffchainLabs/prysm/pull/2433), [nimbus@503cde366](https://github.com/status-im/nimbus-eth2/commit/503cde366c59), [lighthouse#4158](https://github.com/sigp/lighthouse/pull/4158), [nimbus#4445](https://github.com/status-im/nimbus-eth2/pull/4445), [prysm#14687](https://github.com/OffchainLabs/prysm/pull/14687), [teku#6582](https://github.com/Consensys-Incorporated/teku/pull/6582), [caplin#8058](https://github.com/erigontech/erigon/pull/8058), [lodestar#7427](https://github.com/ChainSafe/lodestar/pull/7427), [lodestar#8547](https://github.com/ChainSafe/lodestar/pull/8547), [grandine#92](https://github.com/grandinetech/grandine/pull/92), [teku#6590](https://github.com/Consensys-Incorporated/teku/pull/6590), [caplin#8198](https://github.com/erigontech/erigon/pull/8198), [ethlambda#170](https://github.com/lambdaclass/ethlambda/pull/170), [silver#75](https://github.com/gattaca-com/silver/pull/75)

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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [grandine#605](https://github.com/grandinetech/grandine/pull/605), [grandine@c3d66409a](https://github.com/grandinetech/grandine/commit/c3d66409a6a0)

</details>


<a id="db_cold-057"></a>
<details>
<summary><b>db_cold-057</b> Delete sidecars of orphaned blocks at finalization — <i>implemented · medium · S · disk, cpu</i></summary>

**Idea.** At finalization, find blocks that conflict with the finalized chain (recording orphan roots that actually have stored blobs or columns) and delete their blob and data column sidecars in the same step. Slot-based retention pruning only finds canonical blocks, so orphan sidecars would otherwise leak forever.

**Impact.** Orphan sidecars are deleted at finalization, so they do not leak.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/migrate.rs:713-745`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L713-L745) blocks off the finalized chain selected from state_summaries_dag
- [`beacon_node/beacon_chain/src/migrate.rs:777-792`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L777-L792) DeleteBlobs and DeleteDataColumns (stored keys) for each pruned block in the same batch
- [`beacon_node/beacon_chain/src/migrate.rs:836-850`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L836-L850) prune_finalized_payloads deletes columns of EMPTY-finalized Gloas payloads

**Skeptic check.** Verified that prune_hot_db deletes sidecars of abandoned blocks atomically with the blocks, using get_data_column_keys for stored columns. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@c7f53a906](https://github.com/sigp/lighthouse/commit/c7f53a9062de), [lighthouse@0bdc29149](https://github.com/sigp/lighthouse/commit/0bdc291490a5), [lighthouse@8752deece](https://github.com/sigp/lighthouse/commit/8752deeced23), [nimbus#9403](https://github.com/status-im/nimbus-eth2/pull/9403), [lighthouse#10286](https://github.com/sigp/lighthouse/pull/10286)

</details>


<a id="db_cold-058"></a>
<details>
<summary><b>db_cold-058</b> Delete unused legacy DB buckets — <i>partial · low · S · disk</i></summary>

**Idea.** Delete unused legacy data (e.g. eth1 deposit cache) from existing databases to reclaim disk.

**Gap in Lighthouse.** Eth1Cache column is deprecated but no schema migration deletes its leftover keys on old nodes. Add a migration step that deletes all keys of DBColumn::Eth1Cache and compacts that column.

**Impact.** Reclaims some MB of disk on nodes that ran pre-Electra; no runtime speedup.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/lib.rs:323`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/lib.rs#L323) DBColumn::Eth1Cache marked DEPRECATED, still present
- [`beacon_node/beacon_chain/src/schema_change`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/schema_change)/*.rs: no migration deletes the etc column
- [`beacon_node/store/src/database/leveldb_impl.rs:192`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/leveldb_impl.rs#L192) compact_column exists

**Sources.** [lodestar#8696](https://github.com/ChainSafe/lodestar/pull/8696)

</details>


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


<a id="db_cold-060"></a>
<details>
<summary><b>db_cold-060</b> Drop in-memory index for archived block range — <i>implemented · low · S · memory</i></summary>

**Idea.** Do not keep an in-memory root-to-block index for the archived (backfilled) range; look up slot to root in a DB table on demand.

**Impact.** No memory is spent on an in-memory index of the archived range.

**Best measured result.** 100-200MB memory savings for checkpoint-synced nodes (pr:nimbus#3429)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3096-3102`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3096-L3102) get_cold_block_root reads BeaconBlockRoots column by slot
- [`beacon_node/store/src/forwards_iter.rs:234`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/forwards_iter.rs#L234) frozen forwards iterator reads DB columns

**Skeptic check.** Lighthouse never had an in-memory index of the archived range; slot-to-root lookups go to the freezer column. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#3429](https://github.com/status-im/nimbus-eth2/pull/3429)

</details>


<a id="db_cold-061"></a>
<details>
<summary><b>db_cold-061</b> Do not archive derivable per-epoch data — <i>implemented · low · S · disk</i></summary>

**Idea.** Do not archive derived data such as per-epoch active validator indices; recompute it from the state on demand.

**Impact.** Lighthouse does not persist derived per-epoch data. Shuffling and committees are computed from the state.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/lib.rs:270-380`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/lib.rs#L270-L380) DBColumn list has no active-index, committee or shuffling column

**Skeptic check.** Checked the full column list. The only persisted caches are the pubkey cache and fork choice/op pool, which are not per-epoch archives. The earlier verdict was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#3573](https://github.com/OffchainLabs/prysm/pull/3573), [prysm#5445](https://github.com/OffchainLabs/prysm/pull/5445), [prysm#5365](https://github.com/OffchainLabs/prysm/pull/5365)

</details>


<a id="db_cold-062"></a>
<details>
<summary><b>db_cold-062</b> No delta encoding before general compression — <i>n/a · medium · S · disk, latency</i></summary>

**Idea.** Do not delta-encode balances in stored state snapshots when a general compressor (Snappy) is applied anyway; the delta pass costs much more CPU on load than it saves.

**Impact.** None: snapshots already use only a general compressor; the balance delta in HDiff is between states (needed for diffs), not an intra-state delta before compression.

**Best measured result.** Database load 129ms -&gt; 12.5ms (10x faster), no compression gain (pr:nimbus#2397)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hdiff.rs:385`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L385) balances delta is state-to-state diff then zstd
- [`beacon_node/store/src/hot_cold_store.rs:2143`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2143) snapshots stored as plain SSZ + zstd, no delta
- note: Snapshots are stored without any delta pass (zstd only); the per-state balance delta is inherent to diffs, so the Nimbus anti-pattern does not occur.

**Sources.** [nimbus#2397](https://github.com/status-im/nimbus-eth2/pull/2397)

</details>


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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [teku#11250](https://github.com/Consensys-Incorporated/teku/pull/11250), [teku#10137](https://github.com/Consensys-Incorporated/teku/pull/10137)

</details>


<a id="db_cold-064"></a>
<details>
<summary><b>db_cold-064</b> Remove legacy blob sidecar serving path — <i>n/a · low · S · disk</i></summary>

**Idea.** Stop serving pre-column blob sidecars over req/resp and remove their raw-bytes DB read path.

**Impact.** Pre-Fulu blob serving is still required on mainnet for the retention window; removing it would be a protocol change, not an optimisation.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:684`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L684) fulu_start_slot gating of blobs by root
- rpc_methods.rs:1625-1634 blobs by range stops at Fulu start

**Sources.** [nimbus#8928](https://github.com/status-im/nimbus-eth2/pull/8928)

</details>


<a id="db_cold-065"></a>
<details>
<summary><b>db_cold-065</b> Stop scanning obsolete buckets during archival — <i>n/a · low · S · disk, latency</i></summary>

**Idea.** Do not scan obsolete hot buckets for every finalized block during archiving, since repeated scans over LevelDB tombstones can stall archiving.

**Impact.** Lighthouse migration iterates the state-summary DAG, not obsolete buckets per finalized block.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/lib.rs:315-330`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/lib.rs#L315-L330) columns
- [`beacon_node/beacon_chain/src/migrate.rs:348`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L348) migrate_database

**Sources.** [lodestar#10447](https://github.com/ChainSafe/lodestar/pull/10447)

</details>


<a id="db_cold-066"></a>
<details>
<summary><b>db_cold-066</b> Encode slasher records outside DB transaction — <i>partial · low · S · cpu, memory</i></summary>

**Idea.** Encode attestation record indices once outside the slasher DB write transaction and reuse them, shortening the transaction.

**Gap in Lighthouse.** Attestation SSZ encoding (database.rs store_indexed_attestation) and key building happen while the LMDB/MDBX write txn is held. Pre-encode in Slasher::process_attestations before opening the txn (or in the queue stage) and pass bytes in.

**Impact.** Slightly shorter slasher write txn; encoding is small next to the db puts, and slasher is opt-in, so gain is marginal.

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/database.rs:525`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L525) as_ssz_bytes of the indexed attestation done inside store_indexed_attestation
- [`slasher/src/slasher.rs:94-97`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/slasher.rs#L94-L97) one rw txn around process_blocks/process_attestations
- [`slasher/src/slasher.rs:170`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/slasher.rs#L170) store call is within txn

**Sources.** [prysm#13337](https://github.com/OffchainLabs/prysm/pull/13337)

</details>


<a id="db_cold-067"></a>
<details>
<summary><b>db_cold-067</b> ERA file layout with trailing slot index — <i>not · low · L · disk, startup</i></summary>

**Idea.** Lay out archived history files as blocks, then state, then a trailing slot index, so any block or state is found by slot with one index read.

**Gap in Lighthouse.** Lighthouse has no ERA file import/export. It would need an era reader/writer (e2store format) with slot index and a CLI/db-manager command.

**Impact.** Would make history export/import and serving faster, but needs a new format and tooling; no effect on a running mainnet node.

**Evidence (Lighthouse @ 928b61e719).**

- No e2store/era files in repo (grep for era_file, e2store, .era found none)
- [`beacon_node/store/src/hot_cold_store.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs): history stored in leveldb/redb columns only

**Sources.** [nimbus#3226](https://github.com/status-im/nimbus-eth2/pull/3226)

</details>


<a id="db_cold-068"></a>
<details>
<summary><b>db_cold-068</b> Zero-copy ETL and pooled writers in storage — <i>n/a · low · memory, disk, cpu</i></summary>

**Idea.** Use a zero-copy in-memory ETL provider, pooled buffered writers, arrays instead of bitmaps in collation, and skip per-file globbing when building indices.

**Impact.** Nothing to gain; Caplin's ETL/snapshot pipeline has no counterpart.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/database`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database): leveldb/redb backends, no ETL/collation layer

**Sources.** [caplin#20497](https://github.com/erigontech/erigon/pull/20497)

</details>


<a id="db_cold-069"></a>
<details>
<summary><b>db_cold-069</b> Exact-size copy of compressed cache entries — <i>n/a · low · memory</i></summary>

**Idea.** Copy snappy-compressed output into an exactly sized buffer before caching it, so the max-size encode buffer is not kept alive.

**Impact.** No cache of snappy output exists; Go capacity retention does not apply to Rust Vec.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/codec.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs): snap used on the wire only, no compressed-entry cache
- [`beacon_node/store/src/config.rs:12`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L12) DB values use zstd

**Sources.** [prysm#17227](https://github.com/OffchainLabs/prysm/pull/17227)

</details>


<a id="db_cold-070"></a>
<details>
<summary><b>db_cold-070</b> Faster finalized state pruner rate — <i>n/a · low · disk</i></summary>

**Idea.** Make the finalized-state pruner delete states at a higher rate to reclaim disk sooner.

**Impact.** No separate rate-limited finalized-state pruner; hot states are deleted in the finalization migration.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3471`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3471) prune_historic_states is all-or-nothing
- [`beacon_node/beacon_chain/src/migrate.rs:166`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L166) process_finalization deletes hot states during migration

**Sources.** [teku#8734](https://github.com/Consensys-Incorporated/teku/pull/8734)

</details>


<a id="db_cold-071"></a>
<details>
<summary><b>db_cold-071</b> Per-index diff for validator and builder registries — <i>partial · low · M · cpu, disk, latency</i></summary>

**Idea.** When diffing states, diff list registries (validators, builders, balances) per index and store only (index, change) for changed entries, leaving a small remainder to a generic binary delta. Much faster and smaller than a generic byte diff of the whole list.

**Gap in Lighthouse.** The Gloas builder registry (BeaconState.builders) is not taken out in HDiffBuffer::from_state and has no per-index diff like ValidatorsDiff; it goes to the generic xdelta3 BytesDiff with the rest of the state. Validators and balances are done (PR 6556).

**Impact.** Small today: the builder list is short (see the TODO at beacon_state.rs:2513). It grows only if many builders register; the validator part, which gives the measured 354ms -&gt; 27ms, is already present.

**Best measured result.** hdiff n=1M, 1000 mutated: ~354ms -&gt; ~27ms; n=2M: ~814ms -&gt; ~54ms; diff size slightly smaller (pr:lighthouse#6556)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hdiff.rs:439`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L439) ValidatorsDiff::compute emits ValidatorDiffEntry{index, field deltas} only for changed validators
- [`beacon_node/store/src/hdiff.rs:385`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L385) CompressedU64Diff for balances and inactivity_scores
- [`beacon_node/store/src/hdiff.rs:175`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L175) HDiffBuffer::from_state takes out balances, inactivity_scores, validators, historical_roots/summaries only; builders stays in the state bytes
- [`beacon_node/store/src/hdiff.rs:333`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L333) BytesDiff::compute_xdelta covers the remaining state bytes
- [`consensus/types/src/state/beacon_state.rs:766`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L766) Gloas builders: ProgressiveList&lt;Builder&gt;

**Skeptic check.** Verified that the per-index validator diff and the u64 balance/inactivity diffs are real. The earlier verdict ignored the builder registry that the idea names (caplin#25231): it stays in the xdelta remainder.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lighthouse#6556](https://github.com/sigp/lighthouse/pull/6556), [caplin#25231](https://github.com/erigontech/erigon/pull/25231)

</details>


<a id="db_cold-072"></a>
<details>
<summary><b>db_cold-072</b> Persist archive/checkpoint states periodically during sync — <i>n/a · medium · S · sync, disk</i></summary>

**Idea.** During initial or range sync, write archive/checkpoint states to the DB at a fixed epoch interval instead of only at migration, so cold storage fills incrementally and a restart does not lose sync progress.

**Impact.** Little: blocks and hot state snapshots/diffs are written on import so a restart resumes from the DB; cold states are produced by finalization migration.

**Best measured result.** Avoids losing 2+ hours of sync progress (pr:lodestar#2151)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2103`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2103) store_cold_state called from migration at finalization
- [`beacon_node/store/src/hot_cold_store.rs:1741`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1741) store_hot_state_diffs stores hot state diffs/snapshots on import
- note: Lighthouse imports synced blocks through the normal pipeline and persists hot state snapshots/diffs at hierarchy points, so there is no in-memory-only sync progress to lose; the problem is specific to the other clients' design.

**Sources.** [lodestar#2151](https://github.com/ChainSafe/lodestar/pull/2151), [prysm#5858](https://github.com/OffchainLabs/prysm/pull/5858)

</details>


<a id="db_cold-073"></a>
<details>
<summary><b>db_cold-073</b> Split hot and finalized databases, prune non-canonical — <i>implemented · medium · S · disk</i></summary>

**Idea.** Keep unfinalized blocks/states in a hot DB or tables and finalized data in a separate archive DB with its own schema and tuning, deleting non-canonical hot data at finalization. Disk holds only the finalized chain plus live forks, and sparse finalized state storage becomes possible.

**Impact.** Already done.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:66`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L66) separate cold_db, blobs_db and hot_db
- [`beacon_node/beacon_chain/src/migrate.rs:509`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L509) prune_hot_db deletes non-canonical hot states/blocks at finalization
- [`beacon_node/beacon_chain/src/migrate.rs:645`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L645) abandoned-fork block deletion
- [`beacon_node/store/src/hot_cold_store.rs:3532`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3532) migrate_database moves finalized data to the freezer with hierarchical diffs

**Skeptic check.** Confirmed the hot/cold split, finalization-time pruning of non-canonical data and sparse freezer storage. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#1060](https://github.com/Consensys-Incorporated/teku/pull/1060), [teku#2195](https://github.com/Consensys-Incorporated/teku/pull/2195)

</details>


<a id="db_cold-074"></a>
<details>
<summary><b>db_cold-074</b> Freezer DB with shared fixed-size vector field tables — <i>implemented · low · S · disk</i></summary>

**Idea.** Migrate finalized states to a freezer DB in a background thread and store large fixed-size vector fields (block/state roots, randao) in separate tables so frozen states share them instead of duplicating.

**Impact.** Already done, and the hierarchical diffs that replaced the chunked vectors do it better.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/lib.rs:340`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/lib.rs#L340) BeaconStateRoots and BeaconBlockRoots per-slot columns
- [`beacon_node/store/src/lib.rs:360-362`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/lib.rs#L360-L362) BeaconRandaoMixes deprecated (superseded by hdiffs)
- [`beacon_node/store/src/hot_cold_store.rs:3532`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3532) migrate_database stores cold states as hdiff/snapshot
- [`beacon_node/beacon_chain/src/migrate.rs:440`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L440) background migrator thread

**Skeptic check.** This is Lighthouse's own PR. The chunked randao and historical columns are now deprecated, because states are stored as hierarchical diffs, which removes the duplication more fully. Migration runs on a background thread.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#508](https://github.com/sigp/lighthouse/pull/508)

</details>


<a id="db_cold-075"></a>
<details>
<summary><b>db_cold-075</b> Do not store historic finalized states by default — <i>implemented · low · S · disk, startup</i></summary>

**Idea.** Offer (and default to) a storage mode that drops finalized historic states instead of archiving them, with no or optional restore points, cutting disk usage and write load for non-archive nodes.

**Impact.** Default nodes store no historic finalized states, for both genesis and checkpoint sync.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/src/cli.rs:1301`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L1301) --archive (alias --reconstruct-historic-states) is opt-in
- [`beacon_node/beacon_chain/src/builder.rs:363`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L363) genesis start: retain_historic_states = chain_config.archive (default false)
- [`beacon_node/beacon_chain/src/builder.rs:519`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L519) checkpoint start: same
- [`beacon_node/store/src/hot_cold_store.rs:2775`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2775) STATE_UPPER_LIMIT_NO_RETAIN when not archiving
- [`beacon_node/store/src/hot_cold_store.rs:3585`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3585) migrate_database skips cold state writes below state_upper_limit

**Skeptic check.** Verified that the default applies to genesis sync too (builder.rs:363, since v4.4.0), not only to checkpoint sync. Earlier evidence was correct but did not cite the store path.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#1383](https://github.com/Consensys-Incorporated/teku/pull/1383), [lighthouse#4610](https://github.com/sigp/lighthouse/pull/4610), [lighthouse#2144](https://github.com/sigp/lighthouse/pull/2144), [teku#7401](https://github.com/Consensys-Incorporated/teku/pull/7401)

</details>


<a id="db_cold-076"></a>
<details>
<summary><b>db_cold-076</b> Offline tool to prune historic states/blocks in place — <i>implemented · low · S · disk</i></summary>

**Idea.** Provide a command that deletes unneeded historic states and blocks from an existing database in place, reclaiming disk without a resync.

**Impact.** Already available: lighthouse db prune-states, prune-payloads and prune-blobs.

**Best measured result.** 50G to 1.0G on disk (pr:nimbus#1593)

**Evidence (Lighthouse @ 928b61e719).**

- [`database_manager/src/lib.rs:406`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/database_manager/src/lib.rs#L406) prune_states deletes freezer states in place
- [`database_manager/src/cli.rs:79`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/database_manager/src/cli.rs#L79) prune-payloads, prune-blobs and prune-states subcommands
- [`beacon_node/beacon_chain/src/migrate.rs:509`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L509) non-canonical blocks/states deleted online at finalization

**Skeptic check.** Confirmed the offline in-place state prune plus payload/blob prune. The 'unnecessary blocks' in nimbus#1593 are non-finalized forks, which Lighthouse deletes online.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#4648](https://github.com/sigp/lighthouse/pull/4648), [nimbus#1593](https://github.com/status-im/nimbus-eth2/pull/1593)

</details>


<a id="db_cold-077"></a>
<details>
<summary><b>db_cold-077</b> Archive-mode pruner for states older than N epochs — <i>not · low · M · disk</i></summary>

**Idea.** In archive mode, delete finalized states older than a configured number of epochs in a background pruner, bounding disk growth while keeping a recent historic window.

**Gap in Lighthouse.** Add a store config option to keep only the last N epochs of freezer states and have the migrator delete snapshot/diff/summary entries older than the window after finalization; extend prune_historic_states with a cutoff slot.

**Impact.** Only bounds disk growth on archive nodes; no effect on ordinary mainnet nodes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3471`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3471) prune_historic_states deletes ALL freezer states
- [`database_manager/src/lib.rs:408`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/database_manager/src/lib.rs#L408) prune-states is a manual all-or-nothing command
- [`beacon_node/store/src/config.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs): no retention window option

**Sources.** [teku#8379](https://github.com/Consensys-Incorporated/teku/pull/8379)

</details>


<a id="db_cold-078"></a>
<details>
<summary><b>db_cold-078</b> Resume pruning from a persisted cursor in bounded steps — <i>partial · low · S · disk, cpu, memory, startup, latency</i></summary>

**Idea.** Track the last pruned slot or earliest stored slot (persisted watermark or in-memory) and start each prune run right after it, scanning only newly eligible ranges and deleting a bounded amount per step, instead of rescanning from slot zero or over tombstones. This lowers prune CPU, memory and startup delay.

**Gap in Lighthouse.** try_prune_blobs has the cursor, but it deletes the whole eligible range in one batch with no per-step bound. After downtime, or after re-enabling pruning, it builds one large blobs_db write batch and a removed_block_roots vec for all of it (the bounded steps of nimbus#9404 / teku#10807 are missing). try_prune_execution_payloads (startup only) has no cursor and rescans to the Bellatrix fork.

**Impact.** Steady state is fine (default 1 epoch per run). The gap gives a latency and memory spike on the migrator thread when catching up after downtime. Low.

**Best measured result.** Prune run avg 0.66s vs 3.99s; beacon RSS 9.60 GB vs 13.58 GB (pr:lodestar#10216)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3297`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3297) DataInfo.oldest_data_slot is the persisted blob/column prune cursor
- [`beacon_node/store/src/hot_cold_store.rs:3313`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3313) only runs once start_epoch + epochs_per_blob_prune &lt;= end_epoch + 1
- [`beacon_node/store/src/hot_cold_store.rs:3426`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3426) walk back stops at the first block already pruned
- [`beacon_node/store/src/hot_cold_store.rs:3367`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3367) removed_block_roots and blobs_db_ops collect the whole range in memory
- [`beacon_node/store/src/hot_cold_store.rs:3456`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3456) one blobs_db.do_atomically for the whole range, no cap
- [`beacon_node/store/src/hot_cold_store.rs:3171`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3171) try_prune_execution_payloads, once it starts, scans back to Bellatrix or the anchor with no stop at already-pruned blocks

**Skeptic check.** The cursor and the range-only scan are real, so the main lodestar#10216 effect is already present. The earlier verdict missed the 'bounded amount per step' part, which the impact field itself said was uncapped.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [nimbus#4887](https://github.com/status-im/nimbus-eth2/pull/4887), [nimbus#9404](https://github.com/status-im/nimbus-eth2/pull/9404), [lodestar#10216](https://github.com/ChainSafe/lodestar/pull/10216), [lighthouse@63ca3bfb2](https://github.com/sigp/lighthouse/commit/63ca3bfb2962), [teku#10807](https://github.com/Consensys-Incorporated/teku/pull/10807), [lighthouse@a2b8c6ee6](https://github.com/sigp/lighthouse/commit/a2b8c6ee69f1), [teku#9031](https://github.com/Consensys-Incorporated/teku/pull/9031)

</details>


<a id="db_cold-079"></a>
<details>
<summary><b>db_cold-079</b> Throttle sidecar pruning to once per N epochs — <i>implemented · low · S · disk, cpu</i></summary>

**Idea.** Run blob/column pruning at most once per epoch (or every N epochs) behind a guard, batching the iteration and deletes instead of repeating them on each import or finalization.

**Impact.** Already throttled and run off the hot path.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/config.rs:63`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L63),121 epochs_per_blob_prune
- [`beacon_node/store/src/hot_cold_store.rs:3289-3325`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3289-L3325) should_prune gate
- [`beacon_node/beacon_chain/src/migrate.rs:440-493`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L440-L493) PruneBlobs notifications coalesced to max in migrator thread

**Skeptic check.** Confirmed that the gate applies to both blobs and data columns, and that the migrator collapses queued PruneBlobs notifications into one. The earlier verdict was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@6346c3015](https://github.com/sigp/lighthouse/commit/6346c30158bd), [prysm#13355](https://github.com/OffchainLabs/prysm/pull/13355)

</details>


<a id="db_cold-080"></a>
<details>
<summary><b>db_cold-080</b> Prune execution payload envelopes with block history — <i>partial · low · S · disk</i></summary>

**Idea.** Include stored execution payload envelopes in history pruning using the same slot cutoff as blocks, since envelopes are the larger part of the archive.

**Gap in Lighthouse.** Envelope bodies are pruned at startup, not with any block-history prune (none exists). If a history-prune feature is added, delete PayloadBody/envelope summaries with the same slot cutoff in the function that deletes blocks.

**Impact.** Envelope bodies for finalized blocks are already pruned; further gain exists only with block-history pruning, and Gloas is not live.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3119`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3119) try_prune_execution_payloads deletes envelope bodies (DeletePayload) for finalized blocks
- [`beacon_node/beacon_chain/src/builder.rs:1168`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L1168) called only at startup
- no block-history pruning exists in Lighthouse

**Sources.** [lodestar#10105](https://github.com/ChainSafe/lodestar/pull/10105), [prysm#16742](https://github.com/OffchainLabs/prysm/pull/16742)

</details>


<a id="db_cold-081"></a>
<details>
<summary><b>db_cold-081</b> Key execution payloads by block root for pruning — <i>implemented · low · S · disk</i></summary>

**Idea.** Index stored execution payloads by block root so payloads of finalized blocks can be deleted by key instead of scanning.

**Impact.** None left: payloads are keyed by block root and deleted by key; pruning walks canonical roots, not a column scan.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/lib.rs:407-432`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/lib.rs#L407-L432) ExecPayload/PayloadBody/PayloadSummary key_size 32 (block root)
- [`beacon_node/store/src/hot_cold_store.rs:926`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L926) key_delete(DBColumn::ExecPayload, block_root)
- [`beacon_node/store/src/hot_cold_store.rs:3169-3209`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3169-L3209) try_prune_execution_payloads walks canonical BlockRootsIterator and pushes DeleteExecutionPayload/DeletePayload by root

**Skeptic check.** Verified payload columns use 32-byte block-root keys and pruning deletes by root while iterating canonical block roots from the split state. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#6030](https://github.com/Consensys-Incorporated/teku/pull/6030)

</details>


<a id="db_cold-082"></a>
<details>
<summary><b>db_cold-082</b> Prune per-slot index rows covered by frozen snapshots — <i>n/a · low · S · disk</i></summary>

**Idea.** Delete per-slot state rows from the hot/indexing DB once immutable snapshot files cover them, in resumable time-budgeted batches.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- store/src/hot_cold_store.rs:3532 migrate_database writes cold rows directly to KV

**Sources.** [caplin#22396](https://github.com/erigontech/erigon/pull/22396)

</details>


<a id="db_cold-083"></a>
<details>
<summary><b>db_cold-083</b> Prune old state-diff tree entries — <i>not · low · M · disk</i></summary>

**Idea.** Delete hierarchical state-diff entries older than the retention cutoff, keeping only the last entry per level at or before it plus blocks needed to replay, so diff storage stays bounded.

**Gap in Lighthouse.** Cold BeaconStateDiff/Snapshot rows are never pruned selectively; only a full wipe exists. A retention cutoff would need a new prune in migrate.rs keeping the last entry per hierarchy layer at or before the cutoff, updating AnchorInfo.state_lower_limit.

**Impact.** Bounds cold diff storage for nodes wanting limited state history; no gain to default nodes that keep all diffs (diff storage is already small under tree-states).

**Evidence (Lighthouse @ 928b61e719).**

- store/src/hot_cold_store.rs:3471 prune_historic_states only deletes whole cold columns
- beacon_chain/src/migrate.rs:640-700 prune_hot_db only trims hot hdiff grid, not cold diffs
- store/src/hdiff.rs HierarchyModuli

**Sources.** [prysm#17289](https://github.com/OffchainLabs/prysm/pull/17289)

</details>


<a id="db_cold-084"></a>
<details>
<summary><b>db_cold-084</b> Prune stale pubkey-to-index table entries — <i>n/a · low · S · disk, memory</i></summary>

**Idea.** Remove entries from the persisted pubkey-to-validator-index table that are no longer needed so it does not grow without bound.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- beacon_chain/src/validator_pubkey_cache.rs:214 DBColumn::PubkeyCache is append-only by validator index

**Sources.** [nimbus@8dbd79640](https://github.com/status-im/nimbus-eth2/commit/8dbd7964011d)

</details>


<a id="db_cold-085"></a>
<details>
<summary><b>db_cold-085</b> Index light-client header table for pruning — <i>n/a · low · S · disk, cpu</i></summary>

**Idea.** Add a DB index on the light client headers table so deleting old entries is a range delete instead of a table scan.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- store/src/lib.rs:329-444 DBColumn list: LevelDB/redb key-value columns, no SQL tables or secondary indexes

**Sources.** [nimbus#8626](https://github.com/status-im/nimbus-eth2/pull/8626)

</details>


<a id="db_cold-086"></a>
<details>
<summary><b>db_cold-086</b> Fork-choice-driven block archival on finalization — <i>implemented · low · S · disk, cpu, latency</i></summary>

**Idea.** On finalization, use fork choice's canonical and non-canonical block sets to pick blocks to archive and delete, fetch them by root and write in one batch, instead of scanning the whole hot block DB and testing ancestry per entry.

**Impact.** None left: blocks are never moved (shared block column), and abandoned-fork blocks are chosen from the hot summaries DAG without scanning the block DB or per-entry ancestry walks.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/migrate.rs:537-558`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L537-L558) StateSummariesDAG built from hot state summaries
- [`beacon_node/beacon_chain/src/migrate.rs:588-640`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L588-L640) descendants_of/ancestors_of finalized state give canonical and newly finalized block sets
- [`beacon_node/beacon_chain/src/migrate.rs:711-740`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L711-L740) blocks_to_prune chosen by set membership, deleted by root in one batch

**Skeptic check.** Lighthouse uses the hot state-summaries DAG rather than fork choice, but the effect is the same: no full block-DB scan and no per-block ancestry test. It does load all hot summaries, which are bounded to the unfinalized portion plus hdiff anchors.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@e8d3ef051](https://github.com/ChainSafe/lodestar/commit/e8d3ef0519eb), [lodestar#1656](https://github.com/ChainSafe/lodestar/pull/1656)

</details>


<a id="db_cold-087"></a>
<details>
<summary><b>db_cold-087</b> Forwards freezer iterator for historic root lookups — <i>implemented · low · S · memory, latency, cpu</i></summary>

**Idea.** Resolve historic block and state roots by slot with a forwards iterator over freezer restore-point data instead of reverse-iterating from the head, which materialises many states and spikes memory.

**Impact.** Historic root lookups read the freezer columns directly, with no state materialisation.

**Best measured result.** memory spike 400mb to 800mb+ avoided; response from ~1-2s to near instant (informal) (pr:lighthouse#2376)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/forwards_iter.rs:234`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/forwards_iter.rs#L234) HybridForwardsIterator reads the frozen range forwards from the per-slot columns
- [`beacon_node/beacon_chain/src/beacon_chain.rs:964`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L964) state_root_at_slot uses forwards_iter_state_roots_until
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1050`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1050) block_root_at_slot_skips_none/prev use forwards_iter_block_roots_until

**Skeptic check.** Confirmed that the API/RPC slot-to-root paths go through the forwards iterators. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#672](https://github.com/sigp/lighthouse/pull/672), [lighthouse#2376](https://github.com/sigp/lighthouse/pull/2376), [lighthouse#2422](https://github.com/sigp/lighthouse/pull/2422)

</details>


<a id="db_cold-088"></a>
<details>
<summary><b>db_cold-088</b> Index of finalized block roots for range requests — <i>implemented · low · S · disk, bandwidth</i></summary>

**Idea.** Maintain a finalized-block-root index so range requests drop non-finalized blocks with a key lookup instead of scanning.

**Impact.** None left: finalized range requests use the slot-&gt;root freezer index; non-finalized ranges use the canonical chain from fork choice.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1249-1295`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1249-L1295) get_block_roots_for_slot_range splits at finalized slot: fork choice above, store below
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1320-1330`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1320-L1330) get_block_roots_from_store uses forwards_iter_block_roots
- [`beacon_node/beacon_chain/src/beacon_chain.rs:792-812`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L792-L812) forwards_iter_block_roots over freezer BeaconBlockRoots (slot-&gt;root)

**Skeptic check.** Verified BlocksByRange/BlobsByRange pick roots from the canonical slot-&gt;root index for the finalized portion and fork choice for the rest, so non-canonical blocks are never scanned. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#3873](https://github.com/OffchainLabs/prysm/pull/3873)

</details>


<a id="db_cold-089"></a>
<details>
<summary><b>db_cold-089</b> Finalized state root to slot index — <i>implemented · low · S · latency, disk</i></summary>

**Idea.** Persist a state-root to slot index for finalized states (also filled during historic state reconstruction) so states can be found by root without scanning or recomputation.

**Impact.** None left: finalized states are found by root via a direct key lookup, including reconstructed ones.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2087-2099`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2087-L2099) store_cold_state_summary writes ColdStateSummary(root-&gt;slot) and BeaconStateRoots(slot-&gt;root)
- [`beacon_node/store/src/hot_cold_store.rs:2992`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2992) load_cold_state_slot looks up the root-&gt;slot index
- [`beacon_node/store/src/reconstruct.rs:180`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/reconstruct.rs#L180) reconstruction calls store_cold_state, filling the same indexes

**Skeptic check.** Verified the root-&gt;slot and slot-&gt;root cold indexes are written at migration and during reconstruction. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#2434](https://github.com/Consensys-Incorporated/teku/pull/2434), [teku#6055](https://github.com/Consensys-Incorporated/teku/pull/6055)

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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [lodestar#8899](https://github.com/ChainSafe/lodestar/pull/8899), [prysm#15061](https://github.com/OffchainLabs/prysm/pull/15061), [teku#10287](https://github.com/Consensys-Incorporated/teku/pull/10287)

</details>


<a id="db_cold-091"></a>
<details>
<summary><b>db_cold-091</b> File datastore for persisted states — <i>not · low · L · disk, memory</i></summary>

**Idea.** Store historical/checkpoint states as files in a filesystem datastore instead of in the key-value database.

**Gap in Lighthouse.** Snapshots and diffs live in the KV freezer DB; a file store would need a new backend behind load/store_cold_state in hot_cold_store.rs. Gain is marginal since only sparse snapshots are large.

**Impact.** Slightly less LevelDB compaction/write amplification for big snapshot values; small and unmeasured.

**Evidence (Lighthouse @ 928b61e719).**

- store/src/hot_cold_store.rs:2160-2170 snapshots stored in BeaconStateSnapshot KV column
- store/src/hdiff.rs:316 diffs in BeaconStateDiff KV column

**Sources.** [lodestar#7551](https://github.com/ChainSafe/lodestar/pull/7551)

</details>


<a id="db_cold-092"></a>
<details>
<summary><b>db_cold-092</b> Periodic SQLite WAL checkpoints during bulk writes — <i>n/a · low · disk, startup</i></summary>

**Idea.** During pruning tools and backfill, checkpoint the WAL periodically so it stays small and no multi-minute checkpoint is needed at the end or at startup.

**Impact.** Nothing to checkpoint: no SQLite WAL in the beacon DB (only the validator client slashing protection uses SQLite, not bulk-written).

**Best measured result.** stated: avoids a startup checkpoint of a few minutes (pr:nimbus#3516)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/lib.rs:329`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/lib.rs#L329) - hot/cold DBs are leveldb/redb, no SQLite in beacon store

**Sources.** [nimbus#2402](https://github.com/status-im/nimbus-eth2/pull/2402), [nimbus#3516](https://github.com/status-im/nimbus-eth2/pull/3516)

</details>


<a id="db_cold-093"></a>
<details>
<summary><b>db_cold-093</b> Flat per-epoch span records in slasher DB — <i>implemented · low · S · disk, cpu</i></summary>

**Idea.** Store slasher min/max spans as one flat record per epoch for all validators instead of an index entry per validator per epoch, reducing DB indices and attester-slashing detection I/O.

**Impact.** None left: chunked span records already collapse per-validator-per-epoch entries into far fewer DB records.

**Best measured result.** SetValidatorSpan 235 ns/op; SaveEpochSpans 27 ms/op (pr:prysm#6061)

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/array.rs:15-47`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/array.rs#L15-L47) spans stored as 2D chunks of K validators x C epochs (Vec&lt;u16&gt; distances)
- [`slasher/src/array.rs:159-177`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/array.rs#L159-L177) one compressed DB record per chunk

**Skeptic check.** Lighthouse's chunked min/max span matrix is the same design goal as Prysm's flat per-epoch records (and is in fact what Prysm later adopted). Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#6287](https://github.com/OffchainLabs/prysm/pull/6287), [prysm#6061](https://github.com/OffchainLabs/prysm/pull/6061), [prysm#6150](https://github.com/OffchainLabs/prysm/pull/6150)

</details>


<a id="db_cold-094"></a>
<details>
<summary><b>db_cold-094</b> Lazy-load finalized validator list — <i>n/a · low · startup</i></summary>

**Idea.** Load the finalized validator list from the DB only when needed instead of eagerly at startup.

**Impact.** No separate finalized validator list in the DB; the pubkey cache is needed for gossip signature checks of any validator, so lazy loading is not usable. (Startup load is sequential point reads plus decompression, a different optimisation.)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:55-81`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L55-L81) - load_from_store reads all pubkeys at startup
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:87-100`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L87-L100) - only new validators beyond cache len are imported

**Sources.** [grandine#643](https://github.com/grandinetech/grandine/pull/643)

</details>


<a id="db_cold-095"></a>
<details>
<summary><b>db_cold-095</b> Do not preload all block summaries at startup — <i>implemented · low · S · memory</i></summary>

**Idea.** Read block summaries from the database on demand instead of loading all of them into memory at startup.

**Impact.** No startup preload of block summaries; fork choice is restored from the persisted proto-array.

**Best measured result.** RSS 1.56 GiB -&gt; 1.11 GiB; DAG load 6m45s -&gt; 7m00s (pr:nimbus#3164)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3018`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3018) load_hot_state_summaries full scan is called only from migrate.rs:539 (finalization pruning)
- [`beacon_node/http_api/src/lib.rs:3289`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L3289) other full scans (invariants) only on a debug API call

**Skeptic check.** Searched for every full iter_column over the summary columns: none is on the startup path. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#3164](https://github.com/status-im/nimbus-eth2/pull/3164)

</details>


<a id="db_cold-096"></a>
<details>
<summary><b>db_cold-096</b> Lazy branch nodes for reloaded tree states — <i>n/a · medium · L · memory, latency, disk</i></summary>

**Idea.** When loading a finalized state stored as tree nodes, create lazy branch nodes that fetch children from the DB only on access instead of loading the full tree.

**Impact.** None: Lighthouse does not store states as DB-resident tree nodes; milhouse trees are built from SSZ bytes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hdiff.rs:173`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L173) HDiffBuffer::from_state/as_state work on SSZ bytes
- [`beacon_node/store/src/hot_cold_store.rs:2235`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2235) load_cold_state_as_snapshot deserializes whole SSZ state
- note: States are persisted as SSZ snapshots plus diffs, not as tree nodes keyed by hash, so lazy branch loading has no counterpart.

**Sources.** [teku#4342](https://github.com/Consensys-Incorporated/teku/pull/4342)

</details>


<a id="db_cold-097"></a>
<details>
<summary><b>db_cold-097</b> Lazy demand-driven warming of known-branch cache — <i>n/a · low · startup, disk</i></summary>

**Idea.** Do not scan all stored branch keys at startup to prefill the stored-node cache; on a miss do a point read and add it, so restarts of archive nodes are fast.

**Impact.** Lighthouse does not persist tree nodes, so there is no known-branch cache to prewarm at startup.

**Best measured result.** startup scan "can take over an hour" on archive nodes (pr:teku#11078)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hdiff.rs:197`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L197) - states stored as SSZ snapshots/diffs, no Merkle branch node store
- [`beacon_node/store/src/hot_cold_store.rs:2103-2280`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2103-L2280) - store_cold_state snapshot/diff paths

**Sources.** [teku#11078](https://github.com/Consensys-Incorporated/teku/pull/11078)

</details>


<a id="db_cold-098"></a>
<details>
<summary><b>db_cold-098</b> Size stored-node cache to the full state tree — <i>n/a · low · disk, startup</i></summary>

**Idea.** Size the cache of already-stored Merkle branch nodes to cover a mainnet-scale state tree so unchanged subtrees are skipped on write rather than rewritten after eviction.

**Impact.** No stored-node cache exists in Lighthouse; hdiff replaces node-level dedup.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2143-2280`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2143-L2280) - cold states written as snapshot or hdiff bytes, not per node
- [`beacon_node/store/src/hdiff.rs:439-524`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L439-L524) - validator diffs computed by comparing vectors

**Sources.** [teku#11051](https://github.com/Consensys-Incorporated/teku/pull/11051)

</details>


<a id="db_cold-099"></a>
<details>
<summary><b>db_cold-099</b> Store finalized states as shared Merkle tree nodes — <i>n/a · low · disk, latency</i></summary>

**Idea.** Persist finalized states as SSZ tree nodes keyed by hash, skipping nodes already stored and empty subtrees, so consecutive states share storage and only changed nodes are written. Historic state requests can then be served directly instead of replaying blocks.

**Impact.** Lighthouse shares storage between consecutive states via hierarchical diffs (different design, same goal); node-hash storage would be a redesign with unclear gain.

**Best measured result.** Improves access times for ARCHIVE nodes (pr:teku#4580)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hdiff.rs:253-333`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L253-L333) - HDiff::compute between states
- [`beacon_node/store/src/hot_cold_store.rs:2258-2280`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2258-L2280) - store_cold_state_as_diff

**Sources.** [teku#4199](https://github.com/Consensys-Incorporated/teku/pull/4199), [teku#4331](https://github.com/Consensys-Incorporated/teku/pull/4331), [teku#4580](https://github.com/Consensys-Incorporated/teku/pull/4580), [teku#10993](https://github.com/Consensys-Incorporated/teku/pull/10993), [teku#4333](https://github.com/Consensys-Incorporated/teku/pull/4333)

</details>


<a id="db_cold-100"></a>
<details>
<summary><b>db_cold-100</b> Write finalized validators only when a state is stored — <i>implemented · low · S · disk</i></summary>

**Idea.** Persist the finalized validator list/records to disk only when a state is actually stored, not on every finalization or update.

**Impact.** None left: Lighthouse has no separate finalized-validators record rewritten on finalization; pubkeys are written once per new validator, and validator data otherwise lives only inside stored states/hdiffs.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:86-99`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L86-L99) import_new_pubkeys only processes validators beyond the cache length
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:126-133`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L126-L133) new pubkeys staged as StoreOps in the block import batch

**Skeptic check.** The Grandine fix addresses a Grandine-specific separate validator store; Lighthouse has no equivalent per-finalization write. Upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine#647](https://github.com/grandinetech/grandine/pull/647), [grandine@841fc5f79](https://github.com/grandinetech/grandine/commit/841fc5f79bb8)

</details>


<a id="db_cold-101"></a>
<details>
<summary><b>db_cold-101</b> Persist decompressed BLS pubkeys — <i>implemented · medium · S · startup, cpu, disk</i></summary>

**Idea.** Persist decompressed BLS pubkeys alongside the finalized checkpoint (and write finalized state in batches) so restarts skip expensive pubkey decompression.

**Impact.** Already done: restart loads uncompressed pubkeys and skips decompression.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:54`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L54) load_from_store reads DatabasePubkey per index
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:209`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L209) DatabasePubkey stores PUBLIC_KEY_UNCOMPRESSED_BYTES_LEN bytes
- [`crypto/bls/src/impls/blst.rs:141`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L141) deserialize_uncompressed -&gt; blst PublicKey::deserialize on 96-byte affine input (no sqrt decompression)

**Skeptic check.** Verified down to blst: the 96-byte path does blst_p1_deserialize without a square root, and compress() on load is cheap. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [silver#83](https://github.com/gattaca-com/silver/pull/83)

</details>


<a id="db_cold-102"></a>
<details>
<summary><b>db_cold-102</b> Persist derived light-client data in the DB — <i>implemented · low · S · startup, disk, latency</i></summary>

**Idea.** Store light-client bootstrap and update data (sync committees, epoch-boundary headers) in a small DB table at finalization so they are served without historic states or block replay after restart or pruning.

**Impact.** Bootstrap and best updates are served from small DB columns (sync committee per period, branch per block root, LightClientUpdate per period), no state replay.

**Best measured result.** "A full database with default settings (129 periods) uses &lt;15 MB disk" (pr:nimbus#3823)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/light_client_server_cache.rs:212`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_server_cache.rs#L212)
- [`beacon_node/beacon_chain/src/light_client_server_cache.rs:203`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_server_cache.rs#L203)
- [`beacon_node/beacon_chain/src/light_client_server_cache.rs:396`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_server_cache.rs#L396)
- [`beacon_node/store/src/hot_cold_store.rs:834`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L834)

**Skeptic check.** Verified store_current_sync_committee, store_light_client_update and get_light_client_bootstrap read only persisted parts. Earlier evidence is right; there is no backfill of these values for periods before the node synced (comment at :389), which Nimbus also does not do.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#4499](https://github.com/status-im/nimbus-eth2/pull/4499), [nimbus#3823](https://github.com/status-im/nimbus-eth2/pull/3823)

</details>


<a id="db_cold-103"></a>
<details>
<summary><b>db_cold-103</b> Pooled buffer for state serialization — <i>not · low · S · memory</i></summary>

**Idea.** Serialize states for archiving and checkpoint persistence into a pooled, reused buffer instead of allocating a fresh large buffer each time.

**Gap in Lighthouse.** Reuse a buffer in store_cold_state_as_snapshot, store_hot_state_as_snapshot and HDiffBuffer::from_state.

**Impact.** Saves a few large allocations per snapshot; snapshots are rare, so marginal.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2148-2151`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2148-L2151) - state.as_ssz_bytes() allocates a fresh Vec per snapshot
- [`beacon_node/store/src/hot_cold_store.rs:2193-2196`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2193-L2196) - same for hot snapshot
- [`beacon_node/store/src/hdiff.rs:197`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L197) - fresh Vec in HDiffBuffer

**Sources.** [lodestar#7042](https://github.com/ChainSafe/lodestar/pull/7042)

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


<a id="db_cold-105"></a>
<details>
<summary><b>db_cold-105</b> Preallocate validator key slice in DB migration — <i>n/a · low · cpu, memory</i></summary>

**Idea.** Preallocate the collection with known capacity when gathering validator keys during a DB migration.

**Impact.** Migration-specific one-off Prysm code; nothing comparable in Lighthouse.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs): no validator-key gathering migration
- [`beacon_node/beacon_chain/src/schema_change`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/schema_change)/: migrations do not collect validator keys in a growing Vec

**Sources.** [prysm#16558](https://github.com/OffchainLabs/prysm/pull/16558)

</details>


<a id="db_cold-106"></a>
<details>
<summary><b>db_cold-106</b> Pool and cap ETL sort buffers of history collectors — <i>n/a · low · memory</i></summary>

**Idea.** Share preallocated in-memory sort buffers between the many history-indexing/state-reconstruction collectors via a pool and divide their size, so combined worst-case buffer memory is bounded.

**Impact.** Lighthouse has no ETL-style collectors with large sort buffers, so there is no combined buffer memory to pool or cap.

**Best measured result.** 18 collectors * 256mb / 8 = 512mb worst case vs ~4.5 GB (pr:caplin#9217)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs): freezer indexing done by direct leveldb batches, no ETL collectors/sort buffers
- [`beacon_node/store/src/reconstruct.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/reconstruct.rs): state reconstruction writes batches, no per-index collectors

**Sources.** [caplin#13375](https://github.com/erigontech/erigon/pull/13375), [caplin#16276](https://github.com/erigontech/erigon/pull/16276), [caplin#9217](https://github.com/erigontech/erigon/pull/9217)

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


<a id="db_cold-108"></a>
<details>
<summary><b>db_cold-108</b> Finer-grained snapshot retirement schedule — <i>n/a · low · disk, cpu</i></summary>

**Idea.** Retire DB data into snapshot files on a short ticker with a small, consistent merge limit so the work is spread out instead of large infrequent batches.

**Impact.** Lighthouse has no snapshot file retirement; freezer migration already runs per finalization (every few epochs), so no scheduling to refine.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/lib.rs:247`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/lib.rs#L247): DBColumn - cold data in leveldb columns, no snapshot files
- [`beacon_node/store/src/hot_cold_store.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs): migrate_database moves finalized data to freezer per finalization

**Sources.** [caplin#12121](https://github.com/erigontech/erigon/pull/12121), [caplin#12124](https://github.com/erigontech/erigon/pull/12124)

</details>


<a id="db_cold-109"></a>
<details>
<summary><b>db_cold-109</b> Retire snapshot segments one at a time — <i>n/a · low · latency, disk</i></summary>

**Idea.** Retire backlogged segments one at a time, reopening snapshots and pruning the DB after each, so DB space is reclaimed early and failures keep prior work.

**Impact.** No snapshot segments exist in Lighthouse, so there is no backlog to retire one at a time.

**Best measured result.** backlog of 72 segments took &gt;8 hours with no progress (pr:caplin#24586)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs): no segment/snapshot retirement; freezer migration is incremental per finalized range

**Sources.** [caplin#24586](https://github.com/erigontech/erigon/pull/24586)

</details>


<a id="db_cold-110"></a>
<details>
<summary><b>db_cold-110</b> Parallel compression of backlogged segments — <i>n/a · low · cpu, disk</i></summary>

**Idea.** When the retirement backlog spans multiple chunks, compress segments with several workers (single worker at tip) under a shared limiter.

**Impact.** No segment compression pipeline in Lighthouse.

**Best measured result.** 54 min per ~1.45 GB chunk single-threaded, ~2.4 days for 72-chunk backlog (pr:caplin#24316)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs): no segment compression stage; leveldb handles compression internally

**Sources.** [caplin#24316](https://github.com/erigontech/erigon/pull/24316)

</details>


<a id="db_cold-111"></a>
<details>
<summary><b>db_cold-111</b> Native async generator over DB iterator — <i>n/a · low · cpu</i></summary>

**Idea.** Wrap the DB range iterator directly in a native async generator, removing a stream wrapper layer per item on range reads.

**Impact.** Lodestar JS async generator overhead; Rust iterators are already direct.

**Evidence (Lighthouse @ 928b61e719).**

- beacon_node/store/src/leveldb_store.rs and hot_cold_store.rs: iterators are synchronous Rust iterators, no stream wrapper layers

**Sources.** [lodestar#2435](https://github.com/ChainSafe/lodestar/pull/2435)

</details>


<a id="db_cold-112"></a>
<details>
<summary><b>db_cold-112</b> Strict read-only DB open, drop legacy tables — <i>not · low · S · disk</i></summary>

**Idea.** Open the database read-only without creating legacy tables, and drop unused pre-fork compatibility tables.

**Gap in Lighthouse.** Add a read-only open option to LevelDB/redb wrappers (open in leveldb_impl.rs / redb_impl.rs) for offline inspection tools in database_manager. Legacy-table part does not apply (no SQLite).

**Impact.** Only helps offline DB inspection tools; no effect on running mainnet nodes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/database/leveldb_impl.rs:39`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/leveldb_impl.rs#L39): options.create_if_missing = true on every open
- [`beacon_node/store`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store): no read-only open mode found by grep for read_only/ReadOnly/OpenFlags

**Sources.** [nimbus#4362](https://github.com/status-im/nimbus-eth2/pull/4362)

</details>


<a id="db_cold-113"></a>
<details>
<summary><b>db_cold-113</b> Single bucket per type, fork from serialized slot — <i>implemented · low · S · disk, cpu</i></summary>

**Idea.** Store blocks and states of all forks in one bucket and read the slot from a fixed offset in the SSZ bytes to choose the fork type, avoiding per-fork buckets and extra lookups.

**Impact.** None left: one column per object type, fork chosen from the slot at a fixed SSZ offset.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/block/beacon_block.rs:133-145`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/block/beacon_block.rs#L133-L145) BeaconBlock::from_ssz_bytes reads slot from the first 8 bytes and decodes for fork_name_at_slot
- [`consensus/types/src/block/signed_beacon_block.rs:153-155`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/block/signed_beacon_block.rs#L153-L155) SignedBeaconBlock::from_ssz_bytes uses the slot-based decoder
- [`consensus/types/src/state/beacon_state.rs:3830`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3830) BeaconState::from_ssz_bytes reads slot at fixed offset
- [`beacon_node/store/src/lib.rs:247`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/lib.rs#L247) one DBColumn per type (blk, bst), not per fork

**Skeptic check.** Verified the slot-offset decode path and single-column-per-type layout. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#2440](https://github.com/ChainSafe/lodestar/pull/2440), [lodestar#8916](https://github.com/ChainSafe/lodestar/pull/8916)

</details>


<a id="db_cold-114"></a>
<details>
<summary><b>db_cold-114</b> Store blocks in framed snappy as on the wire — <i>not · low · L · cpu, disk</i></summary>

**Idea.** Store blocks in the DB in framed snappy, the same encoding as req/resp and era files, so serving and exporting need no recompression.

**Gap in Lighthouse.** Store blocks as snappy-framed bytes and have BlocksByRange/Root serve the stored bytes directly; needs a schema change and a new column format, touching get_block paths in hot_cold_store.rs and the RPC response encoder.

**Impact.** Would skip decode plus snappy re-encode when serving blocks to peers; small, since block serving is a minor CPU cost on a mainnet node and zstd gives better disk ratio today.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2149`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2149) blocks stored zstd-compressed SSZ via Encoder
- [`beacon_node/store/src/hot_cold_store.rs:663`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L663) get_blinded_block decodes SSZ; no raw-bytes path

**Sources.** [nimbus#3551](https://github.com/status-im/nimbus-eth2/pull/3551)

</details>


<a id="db_cold-115"></a>
<details>
<summary><b>db_cold-115</b> Answer has-state without loading the state — <i>not · low · S · cpu, disk</i></summary>

**Idea.** Answer has-state queries from state summaries or block plus diff-tree position instead of loading and decoding the state.

**Gap in Lighthouse.** Add a has_state(state_root) on HotColdDB that checks the hot summary then cold summary (key_exists) instead of get_state; replace call sites that only test presence. Few such call sites exist.

**Impact.** Avoids occasional full state load/decode for presence checks; rare path, negligible on a typical node.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1087`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1087) get_state loads full state
- [`beacon_node/store/src/hot_cold_store.rs:2992`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2992) load_cold_state_slot reads only ColdStateSummary
- [`beacon_node/store/src/hot_cold_store.rs:3000`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3000) load_hot_state_summary exists
- [`beacon_node/store/src/lib.rs:65`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/lib.rs#L65) key_exists on KeyValueStore

**Sources.** [prysm#16045](https://github.com/OffchainLabs/prysm/pull/16045)

</details>


<a id="db_cold-116"></a>
<details>
<summary><b>db_cold-116</b> Hoist prune-interval config conversion — <i>n/a · low · S · cpu</i></summary>

**Idea.** Convert the epochs-per-prune setting to its typed value once at config time instead of on every prune check.

**Impact.** The old commit's repeated slots_per_epoch multiplication no longer exists; the config is a u64 used once per prune call, so there is nothing to hoist.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/config.rs:63`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L63) epochs_per_blob_prune is a plain u64
- [`beacon_node/store/src/hot_cold_store.rs:3289`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3289) read once per prune call, compared to Epoch arithmetic

**Sources.** [lighthouse@b5abfe620](https://github.com/sigp/lighthouse/commit/b5abfe620a12)

</details>


<a id="db_cold-117"></a>
<details>
<summary><b>db_cold-117</b> Read only the last key for latest-slot queries — <i>not · low · S · latency, disk</i></summary>

**Idea.** When only the latest key of a column is needed (e.g. latest finalized state slot), read it with a reverse iterator instead of loading and deserializing the full value.

**Gap in Lighthouse.** Add a reverse/last-key iterator to KeyValueStore and use it wherever the newest key in a column is fetched; no hot path currently needs it.

**Impact.** No identified hot path scans a column for its latest key; gain negligible.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/lib.rs:88`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/lib.rs#L88) iter_column / iter_column_from only forward iteration
- [`beacon_node/store/src/hot_cold_store.rs:2306`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2306) cold state lookup is by slot key, no latest-key scan

**Sources.** [teku#3374](https://github.com/Consensys-Incorporated/teku/pull/3374)

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


<a id="db_cold-119"></a>
<details>
<summary><b>db_cold-119</b> Load small diffs before decoding the base snapshot — <i>partial · low · S · cpu, memory, disk</i></summary>

**Idea.** When reconstructing a state from diffs, verify and load all required diffs before decoding the large base snapshot, so a missing ancestor does not cause repeated wasted snapshot decodes.

**Gap in Lighthouse.** Pre-check that all hdiffs on the path exist (cheap key_exists) before decoding the snapshot in load_hdiff_buffer_for_slot. Only matters when a diff is missing, and decoded snapshot is cached anyway.

**Impact.** Only saves repeated snapshot decodes on a corrupt/missing-diff error path; not a normal mainnet case.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2423`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2423) load_hdiff_buffer_for_slot recurses to base first, then loads each diff
- [`beacon_node/store/src/hot_cold_store.rs:2325`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2325) historic_state_cache caches snapshot/hdiff buffers

**Sources.** [prysm#17590](https://github.com/OffchainLabs/prysm/pull/17590)

</details>


<a id="db_cold-120"></a>
<details>
<summary><b>db_cold-120</b> Memoize deserialized diff anchor states — <i>implemented · medium · S · disk, cpu, startup</i></summary>

**Idea.** Cache the deserialized anchor/snapshot state per diff level (invalidated on replacement) instead of deserializing it on every reconstruction, and snapshot resume states periodically.

**Impact.** Snapshot anchors are deserialized once and kept as HDiffBuffers in an LRU, on both the read path and the store_cold_state_as_diff write path; hot side has the same via state_cache.

**Best measured result.** avoids ~410k full state deserializations on mainnet walk (pr:prysm#17292)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/historic_state_cache.rs:14`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/historic_state_cache.rs#L14)
- [`beacon_node/store/src/hot_cold_store.rs:2423`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2423)
- [`beacon_node/store/src/hot_cold_store.rs:2435`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2435)
- [`beacon_node/store/src/hot_cold_store.rs:2270`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2270)
- [`beacon_node/store/src/hot_cold_store.rs:1861`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1861)
- [`beacon_node/store/src/state_cache.rs:295`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L295)
- [`beacon_node/store/src/config.rs:27`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L27)

**Skeptic check.** Verified load_hdiff_buffer_for_slot checks the cache first and caches each level's buffer (put_both for snapshots), and store_cold_state_as_diff loads its base through it. Earlier evidence is right. The Prysm resume-snapshot part does not apply: LH has no forward archive regeneration walk.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#17292](https://github.com/OffchainLabs/prysm/pull/17292)

</details>


<a id="db_cold-121"></a>
<details>
<summary><b>db_cold-121</b> Step by archive-point stride in cold migration — <i>not · low · S · cpu</i></summary>

**Idea.** In hot-to-cold migration, iterate archive-point slots by stepping the archive interval from the first aligned slot instead of testing a modulo on every slot.

**Gap in Lighthouse.** Loop must visit each slot anyway to write BeaconBlockRoots; only the per-slot cold_storage_strategy call could be replaced by stepping to diff boundaries. Gain is a few hundred cheap modulo ops per finalization.

**Impact.** Saves microseconds per finalization migration; negligible.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3574`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3574) loop over every slot in state_roots
- [`beacon_node/store/src/hot_cold_store.rs:3590`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3590) cold_storage_strategy(slot) evaluated per slot

**Sources.** [prysm#16101](https://github.com/OffchainLabs/prysm/pull/16101)

</details>


<a id="db_cold-122"></a>
<details>
<summary><b>db_cold-122</b> Manual pseudo-finalization to migrate and prune — <i>implemented · low · S · disk</i></summary>

**Idea.** Provide an operator-triggered pseudo finalization that migrates hot DB data to the freezer and prunes side chains during long non-finality, bounding hot DB growth.

**Impact.** None left: this is Lighthouse's own PR #7103 and it is present.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs:2860`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L2860) POST lighthouse/finalize
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1866`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1866) forwards to store_migrator.process_manual_finalization
- [`beacon_node/beacon_chain/src/migrate.rs:195`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L195) process_manual_finalization runs the migrate/prune path

**Skeptic check.** The idea is Lighthouse's own merged PR; endpoint and migrator hook exist at the cited lines. Upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#7103](https://github.com/sigp/lighthouse/pull/7103)

</details>


<a id="db_cold-123"></a>
<details>
<summary><b>db_cold-123</b> Upgrade the embedded database library — <i>partial · low · M · disk, cpu</i></summary>

**Idea.** Upgrade the embedded KV database library (mdbx) to a newer release for upstream fixes.

**Gap in Lighthouse.** mdbx is only the optional slasher backend, pinned to a sigp fork; bumping it means rebasing the fork on newer libmdbx. Beacon store does not use mdbx.

**Impact.** Upstream mdbx fixes would only help slasher users, a rare setup.

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.lock libmdbx 0.1.4 git sigp/libmdbx-rs rev e6ff4b9
- [`slasher/Cargo.toml:30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/Cargo.toml#L30) mdbx optional dep (slasher only)
- [`beacon_node/store/src/database/redb_impl.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/redb_impl.rs), leveldb_impl.rs: beacon DB uses redb 2.6.4 / leveldb, not mdbx

**Sources.** [grandine#286](https://github.com/grandinetech/grandine/pull/286)

</details>


<a id="db_cold-124"></a>
<details>
<summary><b>db_cold-124</b> New DB file for schema change, old file read-only — <i>n/a · low · disk, latency</i></summary>

**Idea.** Create new-schema tables in a separate DB file and keep the old file read-only instead of reorganising a large old table in place.

**Impact.** Lighthouse uses LevelDB key prefixes, not SQLite tables; there is no large-table reorganisation to avoid, and migrations are rare one-off steps.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/database/leveldb_impl.rs:35`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/leveldb_impl.rs#L35) LevelDB open, single keyspace with column prefixes
- [`beacon_node/beacon_chain/src/schema_change.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/schema_change.rs) migrations in place

**Sources.** [nimbus#2596](https://github.com/status-im/nimbus-eth2/pull/2596)

</details>


<a id="db_cold-125"></a>
<details>
<summary><b>db_cold-125</b> Ordered async storage channel for writes and queries — <i>n/a · low · latency, disk</i></summary>

**Idea.** Route async storage updates and queries through one ordered channel (queries on a separate executor) so a query after an update waits for it, avoiding buffering unfinished writes.

**Impact.** Lighthouse store is synchronous with atomic write batches; no async update/query channel exists or is needed for the stated problem.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs): synchronous store API called from spawn_blocking tasks
- [`beacon_node/store/src/database/leveldb_impl.rs:143`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/leveldb_impl.rs#L143) do_atomically is a single sync write

**Sources.** [teku#6198](https://github.com/Consensys-Incorporated/teku/pull/6198)

</details>


<a id="db_cold-126"></a>
<details>
<summary><b>db_cold-126</b> Per-column larger RocksDB block cache — <i>not · low · S · disk, memory</i></summary>

**Idea.** Enable a larger block cache only for DB columns with large reads via a per-column flag.

**Gap in Lighthouse.** Set a larger LevelDB block cache (rusty-leveldb/leveldb Options cache) for the hot DB, and optionally open the DB with a configurable cache size flag. LevelDB has no per-column cache, so it would be DB-wide (hot vs cold DB can differ).

**Impact.** Default 8MB LevelDB cache could cut disk reads for state/summary lookups on hot DB; gain unmeasured and small since Lighthouse has its own state and block caches.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/database/leveldb_impl.rs:36-44`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/leveldb_impl.rs#L36-L44) Options::new() with only create_if_missing; no cache_size set
- [`beacon_node/store/src/config.rs:36-49`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L36-L49) only in-memory caches, no LevelDB block cache option

**Sources.** [teku#9127](https://github.com/Consensys-Incorporated/teku/pull/9127)

</details>


<a id="db_cold-127"></a>
<details>
<summary><b>db_cold-127</b> Point lookups for strided block range requests — <i>n/a · medium · S · disk, cpu</i></summary>

**Idea.** For blocks-by-range with step &gt; 1, fetch archived blocks by slot point lookups instead of streaming the whole range.

**Impact.** None on mainnet; strided requests are essentially not issued.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/methods.rs:448`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/methods.rs#L448) step field kept only for v1 compat
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1319`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1319) get_block_roots_from_store uses forwards root iterator, then blocks fetched by root

**Sources.** [lodestar#3447](https://github.com/ChainSafe/lodestar/pull/3447)

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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [ethlambda#548](https://github.com/lambdaclass/ethlambda/pull/548), [ethlambda#683](https://github.com/lambdaclass/ethlambda/pull/683), [nimbus#8283](https://github.com/status-im/nimbus-eth2/pull/8283)

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


<a id="db_cold-131"></a>
<details>
<summary><b>db_cold-131</b> Reuse stored block roots instead of re-hashing — <i>implemented · low · S · cpu</i></summary>

**Idea.** When archiving or pruning finalized blocks, read roots from the DB keys or the root-to-slot index rather than recomputing hash_tree_root for each block.

**Impact.** Migration and pruning take block roots from state block_roots (RootsIterator) or parent_root links; no per-block hash_tree_root.

**Best measured result.** Switching a synced mainnet node from prune to minimal took about 80 minutes with no visible impact on block import (pr:teku#6606)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3567`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3567)
- [`beacon_node/store/src/hot_cold_store.rs:3574`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3574)
- [`beacon_node/store/src/iter.rs:243`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/iter.rs#L243)
- [`beacon_node/beacon_chain/src/historical_blocks.rs:158`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_blocks.rs#L158)

**Skeptic check.** Grep for canonical_root/tree_hash_root in store and migrate.rs finds no block hashing; migrate_database writes BeaconBlockRoots from RootsIterator. Backfill reuses the root computed at RPC receipt. Earlier evidence is right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#1137](https://github.com/ChainSafe/lodestar/pull/1137), [teku#6606](https://github.com/Consensys-Incorporated/teku/pull/6606)

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


<a id="db_cold-133"></a>
<details>
<summary><b>db_cold-133</b> Exit background retire loops on cancel, no fsync sleep — <i>n/a · low · cpu, latency</i></summary>

**Idea.** Make background snapshot retirement/antiquary loops return on context cancellation instead of busy-spinning, and remove fixed sleeps waiting for an fsync the writer already performs.

**Impact.** Lighthouse has no snapshot retire/antiquary background loops with fsync sleeps; pruning runs as one-off tasks.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3818`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3818) only loop is a descending state-summary walk, no sleeping retire loops

**Sources.** [caplin#22944](https://github.com/erigontech/erigon/pull/22944)

</details>


<a id="db_cold-134"></a>
<details>
<summary><b>db_cold-134</b> Auto-delete superseded snapshot segment files — <i>n/a · low · disk</i></summary>

**Idea.** After each snapshot dump on a running node, delete segment files and indexes that are superseded or overlapped by newer merged files, instead of only in a manual command.

**Impact.** Lighthouse has no snapshot segment files to merge or delete; compaction is handled by LevelDB.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs): data stored in LevelDB, no static segment files

**Sources.** [caplin#23471](https://github.com/erigontech/erigon/pull/23471)

</details>


<a id="db_cold-135"></a>
<details>
<summary><b>db_cold-135</b> Drop defensive copies before sorting collector — <i>n/a · low · memory, cpu</i></summary>

**Idea.** Pass key and value buffers straight to a sort/ETL collector that already copies internally, saving one allocation and copy per record during bulk DB loading.

**Impact.** No ETL collector exists in Lighthouse's store; bulk loads use WriteBatch which has no extra defensive copy beyond the key prefix build.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/database/leveldb_impl.rs:143-170`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/leveldb_impl.rs#L143-L170) do_atomically builds a Writebatch directly, no sort/ETL collector

**Sources.** [caplin#10673](https://github.com/erigontech/erigon/pull/10673)

</details>


<a id="db_cold-136"></a>
<details>
<summary><b>db_cold-136</b> Same hash salt across all snapshot indexes — <i>n/a · low · cpu</i></summary>

**Idea.** Use one hash salt for every static block-snapshot index file so a key is hashed once and the hash probes all files' indexes.

**Impact.** Lighthouse has no static snapshot index files; LevelDB manages its own tables and bloom filters.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/database/leveldb_impl.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/leveldb_impl.rs): LevelDB internal SSTables, no Lighthouse static indexes

**Sources.** [caplin#9719](https://github.com/erigontech/erigon/pull/9719)

</details>


<a id="db_cold-137"></a>
<details>
<summary><b>db_cold-137</b> Share one DB transaction across batched operations — <i>partial · low · M · cpu, latency</i></summary>

**Idea.** Pass one transaction (read-only for reads) through a batch of DB reads/writes instead of opening a transaction per operation.

**Gap in Lighthouse.** Writes already share one batch/transaction. Only the optional redb backend opens a read transaction per get_bytes/key_exists; a multi-get API reusing one read txn would be needed, with callers in hot_cold_store.rs batching lookups.

**Impact.** Marginal: LevelDB (the default) has no per-op transaction; redb read-txn reuse would only trim overhead on multi-key reads for the non-default backend.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/database/leveldb_impl.rs:143-170`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/leveldb_impl.rs#L143-L170) batched writes in one Writebatch
- [`beacon_node/store/src/database/redb_impl.rs:104-108`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/redb_impl.rs#L104-L108) get_bytes opens a new read txn per get
- [`beacon_node/store/src/database/redb_impl.rs:155-158`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/redb_impl.rs#L155-L158) do_atomically uses one write txn per batch

**Sources.** [caplin#8185](https://github.com/erigontech/erigon/pull/8185), [nimbus#3313](https://github.com/status-im/nimbus-eth2/pull/3313), [caplin#9876](https://github.com/erigontech/erigon/pull/9876)

</details>


<a id="db_cold-138"></a>
<details>
<summary><b>db_cold-138</b> Skip DB transaction for empty write batches — <i>not · low · S · cpu, disk</i></summary>

**Idea.** Do not open or commit a DB transaction when the write batch is empty.

**Gap in Lighthouse.** Add an early return when ops_batch is empty in LevelDB::do_atomically and Redb::do_atomically (or in do_atomically_with_block_and_blobs_cache for kv_blob_ops).

**Impact.** Saves one empty write call per block with no blobs/columns; negligible on leveldb, a skipped write transaction on redb.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1523`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1523) - blobs_db.do_atomically(kv_blob_ops) called on every import even when no blob ops
- [`beacon_node/store/src/database/leveldb_impl.rs:143`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/leveldb_impl.rs#L143) - builds Writebatch and db.write with no is_empty check
- [`beacon_node/store/src/database/redb_impl.rs:155`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/redb_impl.rs#L155) - begin_write and commit with no is_empty check

**Sources.** [grandine#648](https://github.com/grandinetech/grandine/pull/648)

</details>


<a id="db_cold-139"></a>
<details>
<summary><b>db_cold-139</b> Cap snapshot file size, keep big files immutable — <i>n/a · low · disk, cpu</i></summary>

**Idea.** Stop merging static snapshot files beyond a size threshold (500K blocks) so large files are never rewritten.

**Gap in Lighthouse.** Lighthouse has no snapshot-file layer to cap.

**Evidence (Lighthouse @ 928b61e719).**

- store/src/database/leveldb_impl.rs - all data in leveldb/redb, no static snapshot files

**Sources.** [caplin#9034](https://github.com/erigontech/erigon/pull/9034)

</details>


<a id="db_cold-140"></a>
<details>
<summary><b>db_cold-140</b> Retire old historical-state tables into static files — <i>n/a · low · disk</i></summary>

**Idea.** Move old historical-state tables (validator events, inactivity scores, etc.) out of the mutable DB into immutable snapshot files, served through a combined DB-plus-file getter, so the DB stays small.

**Gap in Lighthouse.** Lighthouse stores cold states as hdiffs, not per-field tables, so there is nothing to move to static files without a redesign.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hdiff.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs) - historical states are hierarchical diffs in the freezer KV DB
- [`beacon_node/store/src/database/interface.rs:98`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/interface.rs#L98) - only leveldb/redb backends

**Sources.** [caplin#12508](https://github.com/erigontech/erigon/pull/12508)

</details>


<a id="db_cold-141"></a>
<details>
<summary><b>db_cold-141</b> Serialize blocks directly into writer or compressor — <i>n/a · low · memory, cpu</i></summary>

**Idea.** Stream block SSZ encoding into the file or compressor writer instead of building an intermediate full-block byte buffer, avoiding an allocation and copy per block.

**Gap in Lighthouse.** Blocks are not compressed or written to files, so there is no writer to stream into.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:551-561`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L551-L561) - blocks stored uncompressed via as_ssz_bytes into a Vec
- [`beacon_node/store/src/hot_cold_store.rs:2148`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2148) - zstd used only for states

**Sources.** [caplin#8215](https://github.com/erigontech/erigon/pull/8215)

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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [nimbus#9110](https://github.com/status-im/nimbus-eth2/pull/9110)

</details>


<a id="db_cold-144"></a>
<details>
<summary><b>db_cold-144</b> Per-type tables instead of one shared KV table — <i>n/a · low · startup, disk, latency</i></summary>

**Idea.** In SQLite-style storage use separate rowid tables per data type (blocks, block summaries, state diffs) instead of one big key-value table, so summaries load in one query at startup and pruning one type does not delete rows from a giant shared table.

**Gap in Lighthouse.** Lighthouse uses leveldb/redb, not SQLite.

**Best measured result.** startup seconds instead of minutes; store/prune ms instead of seconds (pr:nimbus#2560)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/database/leveldb_impl.rs:155`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/leveldb_impl.rs#L155) - single leveldb keyed by column prefix, no SQLite

**Sources.** [nimbus#2573](https://github.com/status-im/nimbus-eth2/pull/2573), [nimbus#2560](https://github.com/status-im/nimbus-eth2/pull/2560), [nimbus#2460](https://github.com/status-im/nimbus-eth2/pull/2460)

</details>


<a id="db_cold-145"></a>
<details>
<summary><b>db_cold-145</b> Separate storage queue for column sidecar queries — <i>implemented · medium · S · latency</i></summary>

**Idea.** Route heavy data column sidecar reads through their own async channel/queue so they do not stall block and state storage operations.

**Impact.** No serialised storage channel exists in LH: column reads run synchronously on beacon-processor workers against the separate blobs_db, so they cannot queue ahead of block/state storage writes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:68`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L68)
- [`beacon_node/beacon_processor/src/lib.rs:600`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L600)
- [`beacon_node/beacon_processor/src/lib.rs:1122`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1122)

**Skeptic check.** Teku's problem is a single async storage channel; LH has no such queue, and DataColumnsByRange has its own low-priority work queue. Earlier verdict holds; worker-pool sharing is a different concern than the idea.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#10276](https://github.com/Consensys-Incorporated/teku/pull/10276)

</details>


<a id="db_cold-146"></a>
<details>
<summary><b>db_cold-146</b> Serialize data column persist tasks — <i>n/a · low · disk, cpu</i></summary>

**Idea.** Allow only one data column sidecar persistence task at a time to cap concurrent disk and CPU use.

**Gap in Lighthouse.** Columns are written inside the block import batch, not as separate persist tasks, so there is no concurrent persist task to limit.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:8421`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L8421) - columns emitted as StoreOp::PutDataColumns in the block import batch
- [`beacon_node/store/src/hot_cold_store.rs:1516-1528`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1516-L1528) - written in one blocking do_atomically during import_block (beacon_chain.rs:4756)

**Sources.** [grandine#631](https://github.com/grandinetech/grandine/pull/631)

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

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [teku#6937](https://github.com/Consensys-Incorporated/teku/pull/6937)

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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [lodestar#8666](https://github.com/ChainSafe/lodestar/pull/8666), [nimbus#7888](https://github.com/status-im/nimbus-eth2/pull/7888)

</details>


<a id="db_cold-149"></a>
<details>
<summary><b>db_cold-149</b> Read whole ERA index in one read — <i>n/a · low · disk, latency</i></summary>

**Idea.** When opening an ERA file index, read the full index record into a buffer with one read and parse offsets from memory instead of one small read per entry.

**Gap in Lighthouse.** Lighthouse has no ERA file support.

**Evidence (Lighthouse @ 928b61e719).**

- grep for ERA in beacon_node found nothing

**Sources.** [nimbus#6305](https://github.com/status-im/nimbus-eth2/pull/6305)

</details>


<a id="db_cold-150"></a>
<details>
<summary><b>db_cold-150</b> Skip redundant CRC and buffer zeroing on loads — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** When loading blocks/states from DB or ERA files, skip CRC32 checks already done by the storage layer and avoid zero-initialising read buffers.

**Impact.** LevelDB reads use ReadOptions::new() with verify_checksums=false; zstd frames have no checksum; decompression buffers are with_capacity, not zero-filled.

**Best measured result.** CRC32 check cost ~50ms per 110MB state load (pr:nimbus#5207)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/database/leveldb_impl.rs:46`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/leveldb_impl.rs#L46)
- [`beacon_node/store/src/config.rs:207`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L207)
- [`beacon_node/store/src/hot_cold_store.rs:2222`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2222)

**Skeptic check.** Confirmed in leveldb-0.8.6 options.rs:119 that verify_checksums defaults to false, and no ERA-file loading path exists in the node. Earlier evidence is right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#5207](https://github.com/status-im/nimbus-eth2/pull/5207)

</details>


<a id="db_cold-151"></a>
<details>
<summary><b>db_cold-151</b> Load finalized state once at startup for all services — <i>n/a · low · startup, cpu</i></summary>

**Idea.** Load the finalized state once at node startup and hand it to every service instead of each service regenerating or reloading it.

**Gap in Lighthouse.** Single BeaconChain object owns the state; services do not each reload it.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/builder.rs:784`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L784) - head state loaded once by the BeaconChain builder
- [`beacon_node/beacon_chain/src/builder.rs:261`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L261) - genesis state loaded once on resume

**Sources.** [prysm#9843](https://github.com/OffchainLabs/prysm/pull/9843)

</details>


<a id="db_cold-152"></a>
<details>
<summary><b>db_cold-152</b> Skip unneeded genesis and duplicate lookups at startup — <i>not · low · S · startup</i></summary>

**Idea.** Avoid loading genesis block data at startup and remove a duplicate state-root lookup when loading a state.

**Gap in Lighthouse.** In resume_from_db, store genesis_time (e.g. in the persisted chain/metadata item) or read it from the already-loaded head/finalized state instead of calling store.get_state for the genesis state; also pass update_cache=false.

**Impact.** Saves one cold-state load (snapshot decompress + SSZ decode + cache insert) per restart; a one-off startup saving of well under a few seconds.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/builder.rs:260`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L260) resume_from_db loads full genesis state via get_state(.., cache=true) on every restart
- [`beacon_node/beacon_chain/src/builder.rs:269`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L269) only genesis_time is used from it

**Sources.** [nimbus#3387](https://github.com/status-im/nimbus-eth2/pull/3387)

</details>


<a id="db_cold-153"></a>
<details>
<summary><b>db_cold-153</b> Reuse existing states when archiving finalized states — <i>implemented · high · S · cpu, latency</i></summary>

**Idea.** When storing finalized state snapshots (e.g. after long non-finality), first check whether the state already exists in memory or the DB and use it, instead of regenerating it by block replay.

**Impact.** Migration loads only diff-boundary states via get_hot_state (cache first, then hot hdiff buffers, which align with cold boundaries), and writes summaries for replay slots; no block replay.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3591`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3591)
- [`beacon_node/store/src/hot_cold_store.rs:3603`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3603)
- [`beacon_node/store/src/hot_cold_store.rs:1817`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1817)
- [`beacon_node/store/src/hot_cold_store.rs:1969`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1969)
- [`beacon_node/store/src/hot_cold_store.rs:402`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L402)

**Skeptic check.** Verified migrate_database skips ReplayFrom slots and the hot and cold hierarchies share epoch-aligned moduli, so boundary states come from the cache or hot diffs. Earlier verdict holds. A side cost (outside this idea) is that get_hot_state rebuilds the tree hash and committee caches on each state it loads only to re-diff it.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#3092](https://github.com/Consensys-Incorporated/teku/pull/3092), [prysm#7686](https://github.com/OffchainLabs/prysm/pull/7686)

</details>


<a id="db_cold-154"></a>
<details>
<summary><b>db_cold-154</b> Skip finalized state work the storage mode discards — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** On finalization, do not load or regenerate finalized states when the storage mode will not store them (prune mode), and in archive mode load only the data still needed (e.g. last finalized block).

**Impact.** Migration loads no states when historic states are not retained, and only snapshot/diff-boundary states otherwise.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3584`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3584) skip state storage when slot &lt; anchor_info.state_upper_limit (STATE_UPPER_LIMIT_NO_RETAIN = prune-like default)
- [`beacon_node/store/src/hot_cold_store.rs:3594`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3594) ReplayFrom slots store only a cold summary, no hot state load
- [`beacon_node/store/src/hot_cold_store.rs:3606`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3606) get_hot_state(..,false) only for snapshot/diff slots

**Skeptic check.** Verified migrate_database: the state_upper_limit check is the equivalent of Teku's PRUNE-mode skip, and the hierarchy skips loading replay-slot states. The earlier evidence was right, but its claim that there is no prune/archive switch is wrong: state_upper_limit is that switch.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#2117](https://github.com/Consensys-Incorporated/teku/pull/2117), [teku#3102](https://github.com/Consensys-Incorporated/teku/pull/3102)

</details>


<a id="db_cold-155"></a>
<details>
<summary><b>db_cold-155</b> Skip historical state lookup when not archive — <i>n/a · low · S · latency, disk</i></summary>

**Idea.** Do not query cold storage for historical finalized states when the node is not in archive mode, since the lookup cannot succeed.

**Impact.** Lighthouse has no archive/non-archive mode; the cold lookup that misses is one key read, negligible.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1095`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1095) get_state with slot skips hot lookup when below split; without slot cold lookup is a single summary key read (load_cold_state_slot)

**Sources.** [teku#7497](https://github.com/Consensys-Incorporated/teku/pull/7497)

</details>


<a id="db_cold-156"></a>
<details>
<summary><b>db_cold-156</b> Switch state storage scheme without re-saving history — <i>n/a · low · S · startup, cpu</i></summary>

**Idea.** When adopting a new state storage scheme, offer a path that keeps existing historical states instead of regenerating and re-saving all of them.

**Impact.** Prysm-specific migration between two storage schemes; no equivalent runtime choice in Lighthouse.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/config.rs:136`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L136) hierarchy exponents fixed once chosen; schema migrations are one-off in store/src schema code

**Sources.** [prysm#5871](https://github.com/OffchainLabs/prysm/pull/5871)

</details>


<a id="db_cold-157"></a>
<details>
<summary><b>db_cold-157</b> Skip archiving blobs/columns outside retention window — <i>implemented · medium · S · disk, sync</i></summary>

**Idea.** When archiving finalized blocks during sync, do not write blobs or data columns that are already outside the data-availability retention window.

**Impact.** Range sync and backfill choose the batch type from data_availability_boundary, so a genesis/old sync never fetches or stores blobs/columns outside the window unless --complete-blob-backfill is set.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context.rs:1296`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L1296)
- [`beacon_node/beacon_chain/src/custody_context.rs:561`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L561)
- [`beacon_node/beacon_chain/src/custody_context.rs:580`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L580)
- [`beacon_node/beacon_chain/src/custody_context.rs:585`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L585)

**Skeptic check.** Verified batch_type uses data_columns_required_for_epoch/blobs_required_for_epoch for both forward and backfill sync, which covers the Lodestar genesis-sync case. Earlier evidence is right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#7760](https://github.com/ChainSafe/lodestar/pull/7760)

</details>


<a id="db_cold-158"></a>
<details>
<summary><b>db_cold-158</b> Archive epoch-constant data once per epoch — <i>n/a · low · S · disk</i></summary>

**Idea.** Archive historical data that only changes at epoch boundaries (e.g. the PTC window) once per epoch rather than every slot.

**Impact.** Lighthouse does not archive per-slot state-derived data; an unchanged ptc_window costs near zero inside the xdelta diff.

**Best measured result.** ~32x less (0.74-1.2 GB/day -&gt; 23-37 MB/day) (pr:caplin#25201)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3594`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3594) cold states are stored only at hierarchy points (snapshot/xdelta diffs), not per slot
- [`beacon_node/store/src/hdiff.rs:98`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L98) ptc_window lives inside the xdelta-diffed state bytes

**Sources.** [caplin#25201](https://github.com/erigontech/erigon/pull/25201)

</details>


<a id="db_cold-159"></a>
<details>
<summary><b>db_cold-159</b> Write back only dirty slasher span chunks — <i>not · low · S · disk</i></summary>

**Idea.** Track whether an update changed a slasher min/max span chunk and write only modified chunks to the DB.

**Gap in Lighthouse.** Make TargetArrayChunk::update report whether any cell changed (set a dirty flag on the chunk), and in update_array only call chunk.store for dirty chunks; get_chunk_for_update would be read-only for check_slashable paths.

**Impact.** Cuts slasher DB writes and zlib compression for unchanged chunks; only nodes running the optional slasher benefit.

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/array.rs:397`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/array.rs#L397) get_chunk_for_update inserts every touched chunk in updated_chunks, even if only read by check_slashable
- [`slasher/src/array.rs:620`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/array.rs#L620) all updated_chunks stored unconditionally
- [`slasher/src/array.rs:169`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/array.rs#L169) store() always compress+put

**Sources.** [prysm#13749](https://github.com/OffchainLabs/prysm/pull/13749)

</details>


<a id="db_cold-160"></a>
<details>
<summary><b>db_cold-160</b> Coarser default spacing of full state snapshots — <i>implemented · medium · S · disk</i></summary>

**Idea.** Raise the default interval between stored full states (restore points), trading slower historical state reconstruction for several times less freezer disk and writes.

**Impact.** Hierarchical diffs with default exponents [5,9,11,13,16,18,21]: one full snapshot per 2^21 slots, diffs in between.

**Best measured result.** reduces disk usage by 32x, historical queries under 10s (pr:lighthouse#790)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hdiff.rs:619`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L619)
- [`beacon_node/src/cli.rs:746`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L746)
- [`beacon_node/store/src/hot_cold_store.rs:402`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L402)

**Skeptic check.** Verified the HierarchyConfig default and that --slots-per-restore-point is deprecated with no effect. Earlier evidence is right; LH went further than coarser restore points (lighthouse#3137/#790 are its own members).

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#6730](https://github.com/OffchainLabs/prysm/pull/6730), [lighthouse#3137](https://github.com/sigp/lighthouse/pull/3137), [lighthouse#790](https://github.com/sigp/lighthouse/pull/790), [nimbus@557717b51](https://github.com/status-im/nimbus-eth2/commit/557717b51799), [nimbus#2542](https://github.com/status-im/nimbus-eth2/pull/2542)

</details>


<a id="db_cold-161"></a>
<details>
<summary><b>db_cold-161</b> Migrate hot-to-cold state diffs in one pass — <i>implemented · low · S · cpu, disk</i></summary>

**Idea.** Make hot-to-cold state-diff migration handle long non-finality by migrating in one pass rather than piecemeal (exact mechanism not visible).

**Impact.** Long non-finality is migrated in a single call; per-state cold writes are sequential because diffs depend on prior states.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3532`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3532) migrate_database collects all roots from old split to new finalized state in one RootsIterator pass
- [`beacon_node/store/src/hot_cold_store.rs:3594`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3594) ReplayFrom slots only write summaries; only diff/snapshot slots load hot states
- [`beacon_node/store/src/hot_cold_store.rs:3621`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3621) block-root ops written in one batch at the end

**Skeptic check.** Verified migrate_database handles the whole range in one call and skips loading non-boundary states. The source Prysm PR is an unmerged 'vibe coded' change with no clear mechanism, so value is low and the match is approximate.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#16795](https://github.com/OffchainLabs/prysm/pull/16795)

</details>


<a id="db_cold-162"></a>
<details>
<summary><b>db_cold-162</b> Structurally-shared tree types for diff buffers — <i>not · medium · M · cpu, memory</i></summary>

**Idea.** Represent the hierarchical-diff buffer with the same persistent structurally-shared tree types as BeaconState, so applying diffs avoids converting to and from flat vectors and keeps sharing.

**Gap in Lighthouse.** Change HDiffBuffer to milhouse List/Vector fields and apply BalancesDiff/ValidatorsDiff/AppendOnlyDiff in place on them (lighthouse#9236, still open); update from_state/as_state and hot/cold load paths.

**Impact.** Each hdiff-based state load (hot state-cache miss, historic state query) and each buffer creation copies ~1M validators and balances twice; tree types would save tens to hundreds of ms per load and keep memory shared with cached states.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hdiff.rs:98`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L98) HDiffBuffer fields are flat Vec&lt;u64&gt;/Vec&lt;Validator&gt;/Vec&lt;Hash256&gt;/Vec&lt;HistoricalSummary&gt;
- [`beacon_node/store/src/hdiff.rs:185`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L185) from_state flattens milhouse lists with to_vec()
- [`beacon_node/store/src/hdiff.rs:227`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L227) as_state rebuilds every list via set_validators_from_iter/List::try_from_iter
- [`consensus/types/src/state/beacon_state.rs:2198`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2198) set_validators_from_iter builds a fresh List (no sharing)
- [`beacon_node/store/src/historic_state_cache.rs:15`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/historic_state_cache.rs#L15) the LRU caches flat HDiffBuffers, not tree-shared ones

**Second check.** Checked the hot and cold HDiffBuffer caches (historic_state_cache.rs, hot_cold_store.rs:1861-1982) and BeaconState setters; the buffer caches only avoid repeated diff chains, every buffer&lt;-&gt;state conversion still flattens and rebuilds.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [lighthouse#9236](https://github.com/sigp/lighthouse/pull/9236)

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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [nimbus#4986](https://github.com/status-im/nimbus-eth2/pull/4986), [caplin#22411](https://github.com/erigontech/erigon/pull/22411), [prysm#17587](https://github.com/OffchainLabs/prysm/pull/17587)

</details>


<a id="db_cold-164"></a>
<details>
<summary><b>db_cold-164</b> Apply validator registry diffs in place — <i>partial · medium · M · memory, cpu</i></summary>

**Idea.** When applying a validator-registry diff during state reconstruction, update only changed indices and append new validators in place, instead of rebuilding the whole registry.

**Gap in Lighthouse.** The diff application itself is in place, but on a flat Vec; converting back to a BeaconState rebuilds and later rehashes the full registry. Apply the diff directly on the milhouse List&lt;Validator&gt; (lighthouse#9236).

**Impact.** Avoids cloning and re-hashing ~1M validators per state reconstruction, the largest part of materialising a diffed state.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hdiff.rs:534`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L534) ValidatorsDiff::apply updates only changed indices (get_mut) and pushes new validators on the Vec
- [`beacon_node/store/src/hdiff.rs:227`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L227) as_state then rebuilds the whole validator List from the Vec
- [`consensus/types/src/state/beacon_state.rs:2198`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2198) set_validators_from_iter = List::try_from_iter, full rebuild

**Second check.** Confirmed that across a diff chain only the final step converts (intermediate buffers stay as Vec, cached in hot/cold hdiff buffer LRUs), so the in-place part of the idea exists; the registry rebuild at as_state remains.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [prysm#17507](https://github.com/OffchainLabs/prysm/pull/17507)

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

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [prysm#16858](https://github.com/OffchainLabs/prysm/pull/16858), [nimbus@360ebd705](https://github.com/status-im/nimbus-eth2/commit/360ebd705fd7), [prysm#16987](https://github.com/OffchainLabs/prysm/pull/16987)

</details>


<a id="db_cold-166"></a>
<details>
<summary><b>db_cold-166</b> Compress slasher span chunks on disk — <i>implemented · low · S · disk</i></summary>

**Idea.** Snappy-compress slasher min/max span chunks before writing them to the DB.

**Impact.** Span chunks are already compressed on disk (zlib rather than snappy).

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/array.rs:178`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/array.rs#L178) bincode + ZlibEncoder before txn.put
- [`slasher/src/array.rs:164`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/array.rs#L164) ZlibDecoder on load

**Skeptic check.** Verified that TargetArrayChunk::store/load compress each chunk with zlib. Same effect, different codec.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#8561](https://github.com/OffchainLabs/prysm/pull/8561)

</details>


<a id="db_cold-167"></a>
<details>
<summary><b>db_cold-167</b> Prefix slasher records with signing root — <i>partial · low · S · cpu</i></summary>

**Idea.** Store the signing root as a prefix of each slasher attestation/header record so equality checks need no decode of the full object.

**Gap in Lighthouse.** Attester path already avoids full decode via compact ids and an in-memory data-root cache. Proposer records (proposers_db) still store the bare header and compare after SSZ decode; prefixing a signing root would need a schema bump in check_or_insert_block_proposal.

**Impact.** Saves decoding a 208-byte header per proposal check; negligible, slasher only.

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/attester_record.rs:25`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/attester_record.rs#L25) attester records are a 6-byte indexed-attestation id
- [`slasher/src/database.rs:591`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L591) in-memory attestation data root cache for dedup
- [`slasher/src/database.rs:702`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L702) proposer path loads and decodes full SignedBeaconBlockHeader to compare

**Sources.** [prysm#8536](https://github.com/OffchainLabs/prysm/pull/8536)

</details>


<a id="db_cold-168"></a>
<details>
<summary><b>db_cold-168</b> Stream block roots from cursor during state load — <i>implemented · low · S · memory, latency</i></summary>

**Idea.** When reconstructing a state by iterating blocks, stream block roots from the DB cursor and stop at the needed block, instead of collecting all roots first.

**Impact.** Cold state replay and reconstruction stream roots from the cursor and stop at the target slot.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/reconstruct.rs:120`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/reconstruct.rs#L120) FrozenForwardsIterator consumed lazily via process_results
- [`beacon_node/store/src/forwards_iter.rs:129`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/forwards_iter.rs#L129) iter_column_from cursor, stops at end_slot
- [`beacon_node/store/src/hot_cold_store.rs:2488`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2488) load_cold_blocks streams roots from the forwards iterator bounded by end_slot

**Skeptic check.** Verified that reconstruction and load_cold_blocks use a bounded cursor iterator. Roots are not collected first. The block Vec built for replay is a separate cost and is bounded by the hierarchy diff span.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine@cf6e7094e](https://github.com/grandinetech/grandine/commit/cf6e7094eac8), [grandine#942](https://github.com/grandinetech/grandine/pull/942)

</details>


<a id="db_cold-169"></a>
<details>
<summary><b>db_cold-169</b> Walk parent-child index between finalized checkpoints — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Compute newly finalized block roots by walking the parent-to-child index between previous and new finalized checkpoints instead of a broader scan.

**Impact.** Newly finalized set comes from an in-memory DAG walk, not a DB scan.

**Best measured result.** shaves off 10ms from epoch processing time (pr:prysm#13486)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/migrate.rs:618`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L618) state_summaries_dag.ancestors_of(new_finalized_state_root)
- [`beacon_node/beacon_chain/src/migrate.rs:593`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L593) descendants_of for the finalized subtree
- [`beacon_node/beacon_chain/src/migrate.rs:626`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L626) blocks_of_states for newly finalized blocks

**Skeptic check.** Confirmed prune_hot_db walks the in-memory summaries DAG between the old split and the new finalized state; earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#13486](https://github.com/OffchainLabs/prysm/pull/13486)

</details>


<a id="db_cold-170"></a>
<details>
<summary><b>db_cold-170</b> Skip legacy read-only tables when pruning — <i>n/a · low · S · cpu, latency</i></summary>

**Idea.** Do not attempt to prune legacy read-only tables, where deletion is impossible or very slow.

**Impact.** Lighthouse has no legacy read-only tables (Nimbus era-file design); pruning deletes from normal columns.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/lib.rs:247`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/lib.rs#L247) DBColumn set has no read-only legacy tables
- [`beacon_node/store/src/hot_cold_store.rs:3471`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3471) prune_historic_states

**Sources.** [nimbus#5116](https://github.com/status-im/nimbus-eth2/pull/5116)

</details>


<a id="db_cold-171"></a>
<details>
<summary><b>db_cold-171</b> Cap state reconstruction batch to yield to migration — <i>implemented · low · S · memory, latency</i></summary>

**Idea.** Limit the number of blocks per historic state reconstruction batch so finalization migration runs regularly and the hot state cache does not thrash.

**Impact.** Migration runs between reconstruction batches.

**Best measured result.** Reduced by 32x to 1024 blocks; ~110 epochs to ~3.5 epochs between migrations (pr:lighthouse#6668)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/migrate.rs:29`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L29) BLOCKS_PER_RECONSTRUCTION = 1024
- [`beacon_node/beacon_chain/src/migrate.rs:221`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L221) run_reconstruction calls reconstruct_historic_states(Some(1024)) and requeues Notification::Reconstruction

**Skeptic check.** This is the Lighthouse PR itself (lighthouse#6668); the cap and requeue are present in current code.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#6668](https://github.com/sigp/lighthouse/pull/6668)

</details>


<a id="db_cold-172"></a>
<details>
<summary><b>db_cold-172</b> Cache regenerated finalized states for sequential reads — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Keep recently regenerated finalized (cold) states in a soft/LRU cache so walking forward through historical slots replays from the previous regenerated state instead of from the stored snapshot each time.

**Impact.** Sequential forward historic reads replay only one slot from the last result.

**Best measured result.** state by slot API: ~12 s per request uncached vs 0.3-0.6 s sequential (pr:teku#2216)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/historic_state_cache.rs:15`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/historic_state_cache.rs#L15) HistoricStateCache (LRU of states and hdiff buffers)
- [`beacon_node/store/src/hot_cold_store.rs:2306`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2306) load_cold_state_by_slot searches replay_from_range for a cached prior state and replays from it
- [`beacon_node/store/src/hot_cold_store.rs:2400`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2400) replayed state is put into the cache
- [`beacon_node/store/src/config.rs:26`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L26) DEFAULT_HISTORIC_STATE_CACHE_SIZE = 1

**Skeptic check.** Verified that each replayed cold state is cached and the next slot's load replays from the nearest cached prior state. Default cache size is 1, which still covers forward sequential walks.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#2216](https://github.com/Consensys-Incorporated/teku/pull/2216)

</details>


<a id="db_cold-173"></a>
<details>
<summary><b>db_cold-173</b> Reopen DB iterator per migration batch — <i>n/a · low · S · memory, disk</i></summary>

**Idea.** During block migration, reopen the DB block stream for each batch instead of holding one iterator open for the whole migration.

**Impact.** Migration does not hold one DB block stream open over a large range; work is per-finalization batch.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/migrate.rs:520`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L520) migration walks hot state summaries DAG, no long-lived block iterator
- [`beacon_node/store/src/hot_cold_store.rs:3532`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3532) migrate_database uses RootsIterator per finalization

**Sources.** [teku#6007](https://github.com/Consensys-Incorporated/teku/pull/6007)

</details>


<a id="db_cold-174"></a>
<details>
<summary><b>db_cold-174</b> Encode slot directly into range-scan bounds — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Build range-scan bounds for slot-indexed DB buckets by encoding the slot number into the key, not by allocating a buffer sized by the slot value. Check Lighthouse range queries for slot-sized allocations.

**Impact.** Range bounds are fixed-size encoded keys. No allocation scales with the slot value.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/forwards_iter.rs:138-140`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/forwards_iter.rs#L138-L140) slot range start is start_slot.to_be_bytes()
- [`beacon_node/store/src/hot_cold_store.rs:865`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L865) period-indexed scan uses start_period.to_be_bytes()
- [`beacon_node/store/src/database/leveldb_impl.rs:254-260`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/leveldb_impl.rs#L254-L260) full-column scans use vec![0; column.key_size()], a fixed per-column size
- [`beacon_node/store/src/database/redb_impl.rs:235`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/redb_impl.rs#L235),272 same fixed-size start key

**Skeptic check.** Checked every iter_column_from and iter_column_keys_from call site: all build their bounds from to_be_bytes or a fixed key_size. The lodestar bug pattern does not exist here.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@9d2d95a94](https://github.com/ChainSafe/lodestar/commit/9d2d95a9472a)

</details>


<a id="db_cold-175"></a>
<details>
<summary><b>db_cold-175</b> Background service rebuilding historical states by block replay — <i>implemented · low · S · disk, cpu</i></summary>

**Idea.** Offer an opt-in background task that replays stored blocks from genesis to regenerate historical finalized states, so a node can keep few states on disk yet regain archive state access later.

**Impact.** Opt-in background reconstruction already exists; it needs full block history (oldest_block_slot == 0), which backfill provides.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/reconstruct.rs:21`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/reconstruct.rs#L21) reconstruct_historic_states replays blocks from state_lower_limit with per_block_processing
- [`beacon_node/beacon_chain/src/migrate.rs:221`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L221) run_reconstruction runs batches of BLOCKS_PER_RECONSTRUCTION and requeues itself
- [`beacon_node/beacon_chain/src/migrate.rs:483`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L483) finalization and blob pruning run before each reconstruction batch so reconstruction does not starve them

**Skeptic check.** Verified that reconstruct_historic_states replays stored blocks into cold states in batches on the background migrator thread. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#5945](https://github.com/Consensys-Incorporated/teku/pull/5945), [teku#5968](https://github.com/Consensys-Incorporated/teku/pull/5968)

</details>


<a id="db_cold-176"></a>
<details>
<summary><b>db_cold-176</b> Partial-read length for archived era state fields — <i>n/a · low · disk, cpu, latency</i></summary>

**Idea.** When reading a single field or prefix of a state from an archived era file, pass the needed byte length so only that part is read and decoded, not the whole state.

**Impact.** Lighthouse has no era file archive; cold states are in the freezer DB.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2161`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2161) cold states stored as snapshot/diff columns, no era files

**Sources.** [nimbus#4437](https://github.com/status-im/nimbus-eth2/pull/4437)

</details>


<a id="db_cold-177"></a>
<details>
<summary><b>db_cold-177</b> Stream snapshot block reads into pooled buffer — <i>n/a · low · cpu, memory</i></summary>

**Idea.** When reading historical blocks from snapshot or flat files, stream chunks into a pooled reusable buffer instead of allocating and appending a fresh slice per chunk.

**Impact.** Lighthouse stores blocks in the KV store, not flat snapshot files.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs): blocks read from key-value DB, no snapshot/flat files

**Sources.** [caplin@98137bc90](https://github.com/erigontech/erigon/commit/98137bc901cb)

</details>


<a id="db_cold-178"></a>
<details>
<summary><b>db_cold-178</b> Precompute per-epoch summaries into the database — <i>not · low · M · cpu, latency</i></summary>

**Idea.** At epoch end, compute derived data such as validator participation once and store it in the DB so API queries read it instead of recomputing from a historical state.

**Gap in Lighthouse.** Add an epoch-summary column written at epoch processing and have compute_attestation_rewards / http_api rewards read it.

**Impact.** Rewards/participation API calls would skip a historical state load (tens to hundreds of ms each); only affects API users, not normal node operation.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_rewards.rs:36`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_rewards.rs#L36) compute_attestation_rewards loads end-of-epoch state via get_state and recomputes
- store/src/lib.rs DBColumn list has no per-epoch summary column

**Sources.** [prysm#3524](https://github.com/OffchainLabs/prysm/pull/3524)

</details>


<a id="db_cold-179"></a>
<details>
<summary><b>db_cold-179</b> Use read-only DB transactions for lookups — <i>implemented · low · S · latency, disk</i></summary>

**Idea.** Open read-only transactions for lookups that do not write, so they avoid the single-writer lock and commit/fsync cost.

**Impact.** All redb lookups and iterators already use read transactions. Only puts, deletes and batches open write transactions.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/database/redb_impl.rs:98`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/redb_impl.rs#L98) get_bytes takes self.db.read() and begin_read
- [`beacon_node/store/src/database/redb_impl.rs:128`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/redb_impl.rs#L128) key_exists uses begin_read
- [`beacon_node/store/src/database/redb_impl.rs:212`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/redb_impl.rs#L212) iter_column_keys_from uses begin_read
- [`beacon_node/store/src/database/redb_impl.rs:244`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/redb_impl.rs#L244) iter_column_from uses begin_read

**Skeptic check.** Verified that every redb read path uses begin_read behind an RwLock read guard. LevelDB, the default backend, has no transactions. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#6358](https://github.com/OffchainLabs/prysm/pull/6358)

</details>


<a id="db_cold-180"></a>
<details>
<summary><b>db_cold-180</b> Serialize finalization archival and cache pruning tasks — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** On finalization, run block archival, state archival and cache pruning one after another, not concurrently, so heavy tasks do not contend for the runtime or DB.

**Impact.** Heavy finalization DB work (block and state archival, pruning, blob pruning, reconstruction, compaction) runs in sequence on one dedicated thread. Pruning of in-memory caches is cheap.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/migrate.rs:430`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L430) spawn_thread runs one background migrator thread that drains and coalesces notifications
- [`beacon_node/beacon_chain/src/migrate.rs:483`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L483) run_migration, run_manual_migration, run_prune_blobs, run_reconstruction and run_manual_compaction run one after another
- [`beacon_node/beacon_chain/src/migrate.rs:310`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L310) run_migration does migrate_database and then prunes the hot DB on the same thread

**Skeptic check.** Verified the single migrator thread and its sequential dispatch order. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@fd6256825](https://github.com/ChainSafe/lodestar/commit/fd625682516a)

</details>


<a id="db_cold-181"></a>
<details>
<summary><b>db_cold-181</b> Copy immutable validator fields only for new indices on load — <i>partial · low · M · cpu</i></summary>

**Idea.** When loading a state from the DB into an existing state that already has validators, copy immutable validator fields (pubkey etc.) only for newly added indices, skipping the populated prefix.

**Gap in Lighthouse.** Lighthouse never loads into an existing populated state: HDiffBuffer::as_state clones every Validator into a fresh list, then rebase_on dedups memory. To skip the populated prefix it would have to start from a cached state's validator list and only append new indices in HDiffBuffer::as_state / load_hot_state.

**Impact.** Saves cloning/building the validator list (~1M entries) on a hot state cache miss; rare path and rebuild is already dominated by tree hashing, so small.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hdiff.rs:227`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L227) as_state rebuilds all validators via set_validators_from_iter(cloned)
- [`beacon_node/store/src/hot_cold_store.rs:1990`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1990) rebase_on_finalized shares tree with finalized state afterwards
- [`beacon_node/store/src/hdiff.rs:534`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L534) ValidatorsDiff::apply patches only changed fields on the buffer Vec

**Sources.** [nimbus#5264](https://github.com/status-im/nimbus-eth2/pull/5264)

</details>


<a id="db_cold-182"></a>
<details>
<summary><b>db_cold-182</b> Skip state existence lookup when a summary proves it — <i>implemented · low · S · cpu, disk</i></summary>

**Idea.** In the head-root save path, skip the extra state-existence read when the stored state summary already shows the state exists.

**Impact.** One summary read is the only existence check. No second state lookup happens after it.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1697`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1697) store_hot_state returns early when load_hot_state_summary already finds the summary
- [`beacon_node/beacon_chain/src/beacon_chain.rs:687`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L687) persist_head does not read whether the head state exists

**Skeptic check.** The Prysm PR stops calling HasState after HasStateSummary in SaveHeadBlockRoot. Lighthouse has no equivalent double check: store_hot_state uses only the summary read. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#17505](https://github.com/OffchainLabs/prysm/pull/17505)

</details>


<a id="db_cold-183"></a>
<details>
<summary><b>db_cold-183</b> DB index from versioned hash to sidecar — <i>n/a · low · S · latency, cpu</i></summary>

**Idea.** Maintain a DB index from blob versioned hash to stored sidecar identifier, updated on store, prune and move, so getBlobs-style lookups by versioned hash are a key read, not a scan.

**Gap in Lighthouse.** Lighthouse has no global versioned-hash lookup; its API resolves hashes within a known block via its kzg commitments, so no scan exists to index.

**Impact.** none

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/block_id.rs:395`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L395) get_blobs_by_versioned_hashes takes a block id and matches hashes against that block's commitments
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:139`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L139) getBlobs goes CL-&gt;EL, Lighthouse does not serve by versioned hash across the DB

**Sources.** [teku#9931](https://github.com/Consensys-Incorporated/teku/pull/9931)

</details>


