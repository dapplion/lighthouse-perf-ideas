# db_hot

164 ideas: 20 not, 24 partial, 57 implemented, 63 n/a; 21 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [db_hot-001](#db_hot-001) | Batch many small DB writes into one transaction | implemented | medium | S | disk, cpu, sync |
| [db_hot-002](#db_hot-002) | Split large prunes into many small transactions | partial | low | S | disk, latency, memory |
| [db_hot-003](#db_hot-003) **★** | Spread pruning over slots instead of epoch bursts | partial | medium | M | latency, disk |
| [db_hot-004](#db_hot-004) | Apply store updates in memory before disk write | not | low | L | latency, disk |
| [db_hot-005](#db_hot-005) | Slot-indexed canonical block root lookup | implemented | low | S | cpu, disk, latency |
| [db_hot-006](#db_hot-006) | Big-endian fixed-width integer keys for range scans | implemented | low | S | disk, cpu |
| [db_hot-007](#db_hot-007) | In-memory caches of blocks and states over DB | partial | low | S | memory, disk, latency |
| [db_hot-008](#db_hot-008) | Disable contended store block cache | implemented | low | S | cpu, latency |
| [db_hot-009](#db_hot-009) | Do not store EL-reconstructible execution payloads | implemented | medium | S | disk |
| [db_hot-010](#db_hot-010) | Load blinded block when payload not needed | implemented | medium | S | disk, cpu |
| [db_hot-011](#db_hot-011) | Compact block summary table for fast startup | implemented | medium | S | startup, disk, cpu |
| [db_hot-012](#db_hot-012) | Store each data column/blob sidecar under its own key | implemented | medium | S | cpu, disk, bandwidth |
| [db_hot-013](#db_hot-013) | Key-only DB iteration without reading values | partial | low | S | cpu, memory, disk |
| [db_hot-014](#db_hot-014) | Existence check without loading value | partial | low | M | memory, cpu |
| [db_hot-015](#db_hot-015) | Single cursor pass for bulk state deletion | n/a | low |  | cpu, disk |
| [db_hot-016](#db_hot-016) | On-demand DB compaction endpoint | implemented | low | S | disk |
| [db_hot-017](#db_hot-017) | Manual finalization endpoint to migrate and prune | implemented | low | S | disk |
| [db_hot-018](#db_hot-018) | Hierarchical state diffs in the hot DB | implemented | medium | S | disk |
| [db_hot-019](#db_hot-019) **★** | Share validators via Arc in hdiff buffer | not | medium | M | memory, cpu |
| [db_hot-020](#db_hot-020) | Cache hot hdiff buffers alongside state cache | implemented | low | S | cpu, disk, latency |
| [db_hot-021](#db_hot-021) | Bound prune iteration to not-yet-pruned range | implemented | medium | S | disk, cpu |
| [db_hot-022](#db_hot-022) | Prune blobs outside retention window, verify deletion | implemented | medium | S | disk |
| [db_hot-023](#db_hot-023) | Delete abandoned fork blocks and states at finalization | implemented | medium | S | disk |
| [db_hot-024](#db_hot-024) | Prune in-memory hot collections on finalization | implemented | low | S | memory |
| [db_hot-025](#db_hot-025) | Keep pruning off the startup path | implemented | medium | S | disk, startup |
| [db_hot-026](#db_hot-026) | Tune RocksDB block cache, compaction and WAL | n/a | low |  | cpu, memory, disk, latency |
| [db_hot-027](#db_hot-027) **★** | Tune KV store write buffer and flush settings | not | medium | S | memory, disk |
| [db_hot-028](#db_hot-028) | Lower max open files for the KV store | not | low | S | memory |
| [db_hot-029](#db_hot-029) | Disable DB block cache, rely on page cache | not | low | S | memory |
| [db_hot-030](#db_hot-030) | Larger SQLite page cache | n/a | low | S | disk, memory |
| [db_hot-031](#db_hot-031) | Upgrade embedded LevelDB and Snappy | partial | low | M | disk, cpu |
| [db_hot-032](#db_hot-032) | Alternative embedded KV backend (LevelDB vs RocksDB) | implemented | low | S | memory, disk |
| [db_hot-033](#db_hot-033) | Large initial mmap size for embedded DB | n/a | low | S | latency, disk |
| [db_hot-034](#db_hot-034) | Size DB dirty-page limit from cgroup memory | n/a | low | S | memory |
| [db_hot-035](#db_hot-035) | WAL checkpoint once per slot, no fsync mid-slot | n/a | low | S | disk, latency |
| [db_hot-036](#db_hot-036) | Skip fsync on rebuildable cache dumps | implemented | low | S | disk, latency |
| [db_hot-037](#db_hot-037) | Keep DB transactions short, work outside them | partial | low | S | cpu, latency |
| [db_hot-038](#db_hot-038) | No read transaction nested in write transaction | n/a | low | S | latency |
| [db_hot-039](#db_hot-039) **★** | Serialize state once without extra copies | partial | medium | M | cpu, memory, latency |
| [db_hot-040](#db_hot-040) | Generated SSZ codecs for DB objects | n/a | low | S | cpu |
| [db_hot-041](#db_hot-041) **★** | Persist received bytes without re-serializing | not | medium | M | cpu, memory |
| [db_hot-042](#db_hot-042) | Fork-specific decoding of stored payloads | implemented | low | S | cpu |
| [db_hot-043](#db_hot-043) | Parallel slasher double-vote detection | not | low | M | cpu, disk |
| [db_hot-044](#db_hot-044) | Deduplicate slasher attestations by signing root | implemented | low | S | disk |
| [db_hot-045](#db_hot-045) | Deduplicate secondary index entries before write | n/a | low | S | disk |
| [db_hot-046](#db_hot-046) | Store sync committees once, reference by hash | implemented | low | S | disk |
| [db_hot-047](#db_hot-047) | Single cache for one DB query | n/a | low | S | disk, cpu |
| [db_hot-048](#db_hot-048) | Read cheap DB variable directly, no cache | n/a | low | S | latency |
| [db_hot-049](#db_hot-049) | Store earliest available block slot as DB variable | implemented | low | S | latency, disk |
| [db_hot-050](#db_hot-050) **★** | Disk-backed deposits and immutable validator data | not | medium | L | memory |
| [db_hot-051](#db_hot-051) | Persist pending unknown-parent blocks on disk | n/a | high | S | memory |
| [db_hot-052](#db_hot-052) | Archive all finalized blocks out of memory | n/a | low | S | memory |
| [db_hot-053](#db_hot-053) | Load chain-link state lazily when appending | n/a | low | S | cpu, memory |
| [db_hot-054](#db_hot-054) | Drive archiving from fork-choice prune events | not | low | M | cpu, disk |
| [db_hot-055](#db_hot-055) | Run block and state archiving concurrently | n/a | low | L | latency |
| [db_hot-056](#db_hot-056) | Configurable epochs between freezer migrations | implemented | low | S | disk, cpu |
| [db_hot-057](#db_hot-057) | Prune blobs once per day | implemented | low | S | disk, cpu |
| [db_hot-058](#db_hot-058) | Periodic hot state snapshots to bound replay | implemented | medium | S | cpu, disk, startup |
| [db_hot-059](#db_hot-059) **★** | Store only hot blocks, regenerate hot states | partial | medium | M | cpu, disk |
| [db_hot-060](#db_hot-060) | Skip no-op DB deletes and empty transactions | partial | low | S | cpu, disk |
| [db_hot-061](#db_hot-061) | Get state root from next block in replay | implemented | medium | S | cpu, latency |
| [db_hot-062](#db_hot-062) | Write DB backups without freelist | n/a | low | S | disk |
| [db_hot-063](#db_hot-063) | Keep freelist sync on bolt-style DBs and backups | n/a | low | S | disk, startup |
| [db_hot-064](#db_hot-064) | Back up DB without large memory snapshots | n/a | low | S | memory, latency |
| [db_hot-065](#db_hot-065) **★** | Blob sidecars as files with atomic rename | not | medium | L | disk |
| [db_hot-066](#db_hot-066) | Epoch-keyed blob directory layout with summary | n/a | low |  | startup, disk |
| [db_hot-067](#db_hot-067) | Check DB before regenerating justified state | implemented | low | S | cpu, sync |
| [db_hot-068](#db_hot-068) | Write large states as fixed-size chunks | not | low | L | memory |
| [db_hot-069](#db_hot-069) | Chunked field storage shared between states | implemented | medium | S | disk |
| [db_hot-070](#db_hot-070) | Close DB environments on shutdown of loops | n/a | low | S | memory |
| [db_hot-071](#db_hot-071) | Always close DB iterators | n/a | low | S | memory |
| [db_hot-072](#db_hot-072) **★** | One KV instance for hot and finalized data | not | medium | L | memory, disk, latency |
| [db_hot-073](#db_hot-073) | Fetch justified block from DB by root | implemented | low | S | cpu |
| [db_hot-074](#db_hot-074) | Resolve block slot without loading block or state | implemented | medium | S | cpu, disk, latency |
| [db_hot-075](#db_hot-075) | Defer pruning until block-processing cascade ends | n/a | medium |  | cpu |
| [db_hot-076](#db_hot-076) | Clean up temporary hot states and their flags | implemented | low | S | disk, startup |
| [db_hot-077](#db_hot-077) | Direct lookup for block at exact slot | implemented | low | S | latency, disk |
| [db_hot-078](#db_hot-078) | Drop orphan block roots without states at startup | n/a | low | S | startup, memory |
| [db_hot-079](#db_hot-079) | Do not store payload-derived state separately | implemented | low | S | disk |
| [db_hot-080](#db_hot-080) | Avoid a global or redundant store lock | implemented | low | S | cpu, latency |
| [db_hot-081](#db_hot-081) | Embed DB cursor wrapper by value | n/a | low |  | cpu, memory |
| [db_hot-082](#db_hot-082) **★** | Retention pruning during finality stalls | partial | high | M | memory, disk |
| [db_hot-083](#db_hot-083) | Keep few recent headers in DB, rest in snapshots | n/a | low |  | disk |
| [db_hot-084](#db_hot-084) | Prune hot states older than finalization | implemented | medium | S | disk |
| [db_hot-085](#db_hot-085) | Optional pruning of historical states | implemented | medium | S | disk |
| [db_hot-086](#db_hot-086) | Index finalized block roots | implemented | low | S | cpu, disk |
| [db_hot-087](#db_hot-087) | Hot state-root to state index | implemented | medium | S | cpu, latency |
| [db_hot-088](#db_hot-088) | Hoist DB bucket lookup out of loops | n/a | low |  | cpu |
| [db_hot-089](#db_hot-089) | Run metric column scans off the pruning path | n/a | low |  | latency, disk |
| [db_hot-090](#db_hot-090) | More threads for storage query executor | n/a | low |  | latency |
| [db_hot-091](#db_hot-091) | Dump chain in ascending order with rebase | implemented | low | S | memory, cpu |
| [db_hot-092](#db_hot-092) | Partial state getters and cached state hash | implemented | low | S | cpu, memory |
| [db_hot-093](#db_hot-093) | Read only needed vote cache entries from DB | n/a | low |  | disk |
| [db_hot-094](#db_hot-094) | One persist task per arriving sidecar | n/a | low |  | latency, disk |
| [db_hot-095](#db_hot-095) **★** | Write-back buffer for state summaries | not | medium | S | cpu, disk |
| [db_hot-096](#db_hot-096) **★** | Persist states only when a block follows | partial | medium | S | disk, cpu |
| [db_hot-097](#db_hot-097) | Persist all fork-choice heads in DB | n/a | low |  | startup, disk |
| [db_hot-098](#db_hot-098) **★** | Persist committee caches with stored states | not | medium | M | cpu, latency |
| [db_hot-099](#db_hot-099) | Persist deposit cache instead of refetching logs | n/a | low |  | startup, sync |
| [db_hot-100](#db_hot-100) | Store EL-fetched payloads when not pruning | n/a | low |  | bandwidth, latency, disk |
| [db_hot-101](#db_hot-101) | Persist head, fork choice and eth1 data less often | implemented | medium | S | disk, cpu, latency |
| [db_hot-102](#db_hot-102) **★** | Persist data columns on arrival, prune cache after | not | medium | M | memory, disk, sync |
| [db_hot-103](#db_hot-103) | Preallocate slices for block root ranges | not | low | S | memory, cpu |
| [db_hot-104](#db_hot-104) | Store previous state root in hot summaries | partial | low | S | cpu, memory, latency |
| [db_hot-105](#db_hot-105) | Prune hot DB via state summaries DAG | implemented | low | S | disk |
| [db_hot-106](#db_hot-106) | Prune orphaned execution payload envelopes | implemented | low | S | disk |
| [db_hot-107](#db_hot-107) | Prune unreachable data after head rewind | n/a | low |  | disk |
| [db_hot-108](#db_hot-108) **★** | Prune blocks older than retention window | partial | medium | M | disk, memory |
| [db_hot-109](#db_hot-109) | Write intermediate states to DB as temporary | implemented | low | S | memory |
| [db_hot-110](#db_hot-110) | Prune dangling states at startup | not | low | S | disk, startup |
| [db_hot-111](#db_hot-111) | Prune invalid-block blacklist at finality | n/a | low | S | disk, memory |
| [db_hot-112](#db_hot-112) | Incremental pruning of per-block vote cache | n/a | low | S | disk |
| [db_hot-113](#db_hot-113) | Prune live-chain index to finalized slot | n/a | low | S | disk, cpu |
| [db_hot-114](#db_hot-114) | Prune validator pubkey-to-index table | n/a | low | S | disk |
| [db_hot-115](#db_hot-115) | Prune slasher history outside window | implemented | low | S | disk |
| [db_hot-116](#db_hot-116) | Bound slashing-protection attestation history | implemented | low | S | disk |
| [db_hot-117](#db_hot-117) | Store validator pubkey cache inside the DB | implemented | low | S | startup, disk |
| [db_hot-118](#db_hot-118) | Raise DB and open-file resource limits | partial | low | S | sync, disk |
| [db_hot-119](#db_hot-119) | Slot-ordered range scans instead of per-key lookups | partial | low | S | disk, cpu |
| [db_hot-120](#db_hot-120) | Move blocks hot-to-cold as raw bytes | n/a | medium |  | cpu, latency |
| [db_hot-121](#db_hot-121) | Take block root from DB key on load | n/a | low | S | cpu, startup |
| [db_hot-122](#db_hot-122) | Reuse computed block root when saving blocks | implemented | low | S | cpu |
| [db_hot-123](#db_hot-123) | Readdir-based pruning of bucketed sidecar files | n/a | low |  | cpu, disk |
| [db_hot-124](#db_hot-124) **★** | Open redb with quick repair | not | medium | S | startup |
| [db_hot-125](#db_hot-125) | Drop DB writes and indexes nobody reads | partial | low | S | disk, cpu |
| [db_hot-126](#db_hot-126) | Avoid blinded-block storage layout | n/a | low | S | latency, disk |
| [db_hot-127](#db_hot-127) | Find highest block at or below slot quickly | implemented | low | S | cpu, latency |
| [db_hot-128](#db_hot-128) | Do not denormalize slasher attestation records | implemented | low | S | disk |
| [db_hot-129](#db_hot-129) | Avoid memory-hungry DB format | n/a | medium |  | memory, sync |
| [db_hot-130](#db_hot-130) | SQLite kv table with rowid for fast deletes | n/a | low |  | disk, cpu |
| [db_hot-131](#db_hot-131) | Uncorrelated pruning query | n/a | low |  | cpu, disk |
| [db_hot-132](#db_hot-132) | Save light client bootstraps on finalization only | partial | low | S | disk |
| [db_hot-133](#db_hot-133) | Secondary index buckets for attestation filters | n/a | low |  | cpu, disk |
| [db_hot-134](#db_hot-134) | Separate DB file for slasher | implemented | low | S | disk, latency |
| [db_hot-135](#db_hot-135) | Single atomic batch for puts and deletes | implemented | low | S | disk, latency |
| [db_hot-136](#db_hot-136) | Persist state once per epoch transition | n/a | low |  | disk, cpu |
| [db_hot-137](#db_hot-137) | Run DB migration in one transaction | n/a | low |  | startup |
| [db_hot-138](#db_hot-138) | Use plain update transactions instead of bolt Batch | n/a | low |  | memory |
| [db_hot-139](#db_hot-139) | Skip BLS checks when replaying stored deposits | n/a | low |  | cpu, startup |
| [db_hot-140](#db_hot-140) | Do not recreate empty temporary block DB | n/a | low |  | disk, cpu |
| [db_hot-141](#db_hot-141) | Skip attestation DB writes on non-archival nodes | implemented | low | S | disk |
| [db_hot-142](#db_hot-142) | Start from stored hot states without block replay | implemented | low | S | startup |
| [db_hot-143](#db_hot-143) **★** | Skip checkpoint state writes during sync | partial | medium | M | disk, sync |
| [db_hot-144](#db_hot-144) | Reuse fresh DB state instead of checkpoint download | implemented | low | S | startup, bandwidth |
| [db_hot-145](#db_hot-145) | Return cached states without deep clone | n/a | low | S | memory, cpu |
| [db_hot-146](#db_hot-146) | Skip writing empty blob sidecar lists | implemented | low | S | disk |
| [db_hot-147](#db_hot-147) | Avoid per-block DB iterator on import | n/a | low | S | cpu, disk |
| [db_hot-148](#db_hot-148) | Skip fork pruning with a single head | n/a | medium | S | cpu, memory |
| [db_hot-149](#db_hot-149) **★** | Trust local blocks, skip signature work on load | not | medium | M | startup, cpu, memory |
| [db_hot-150](#db_hot-150) | Skip legacy DB lookups on state write | n/a | low | S | cpu, disk |
| [db_hot-151](#db_hot-151) | Avoid startup scans over tombstoned legacy ranges | n/a | low | S | startup |
| [db_hot-152](#db_hot-152) | Pass slices instead of array copies to DB | n/a | low | S | memory, cpu |
| [db_hot-153](#db_hot-153) | Smaller in-memory block cache | n/a | medium | S | memory |
| [db_hot-154](#db_hot-154) **★** | Snappy-compress blocks and states in DB | partial | medium | S | disk, sync |
| [db_hot-155](#db_hot-155) | Compress cached anchor states in memory | not | low | S | memory |
| [db_hot-156](#db_hot-156) | Per-entry compression choice (zstd) | partial | low | M | disk |
| [db_hot-157](#db_hot-157) | In-memory cache over slasher span store | partial | low | M | disk, cpu |
| [db_hot-158](#db_hot-158) **★** | Run DB reads off the async executor | partial | medium | S | latency |
| [db_hot-159](#db_hot-159) **★** | Separate block header and body tables | partial | medium | M | disk, cpu |
| [db_hot-160](#db_hot-160) | Keep startup-only tables out of main allocator | n/a | low | S | memory |
| [db_hot-161](#db_hot-161) | Tree-backed storage of pending blocks | n/a | low | S | cpu, memory |
| [db_hot-162](#db_hot-162) | Validator entry dedup cache hits on state save | n/a | medium | S | cpu, disk |
| [db_hot-163](#db_hot-163) | Key stored aggregates by attestation root | n/a | low | S | cpu, disk |
| [db_hot-164](#db_hot-164) | Validate blocks before persisting as pending | n/a | low | S | disk, cpu |

★ actionable. Click an id for the full record.

## Ideas

<a id="db_hot-001"></a>
<details>
<summary><b>db_hot-001</b> Batch many small DB writes into one transaction — <i>implemented · medium · S · disk, cpu, sync</i></summary>

**Idea.** Group many per-item writes or deletes (attestations, votes, validator index entries, states, slasher spans) into one key-value write batch or transaction instead of one commit per item. This removes per-commit fsync and lock overhead.

**Impact.** Block import, pruning and slasher writes already go in one batch or transaction.

**Best measured result.** validator test ~400s down to ~1s (pr:prysm#1732)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1459`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1459) do_atomically_with_block_and_blobs_cache takes a Vec&lt;StoreOp&gt;
- [`beacon_node/store/src/lib.rs:71`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/lib.rs#L71) KeyValueStore::do_atomically
- [`beacon_node/store/src/database/leveldb_impl.rs:143`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/leveldb_impl.rs#L143) one WriteBatch per do_atomically
- [`slasher/src/slasher.rs:94`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/slasher.rs#L94) one rw txn per slasher batch

**Skeptic check.** Confirmed the main write paths (block import, migration, prune, slasher) use one batch or transaction. Cold-state migration writes one batch per state on purpose, because each diff depends on the state before it.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#3496](https://github.com/OffchainLabs/prysm/pull/3496), [prysm#5041](https://github.com/OffchainLabs/prysm/pull/5041), [prysm#3622](https://github.com/OffchainLabs/prysm/pull/3622), [prysm#1732](https://github.com/OffchainLabs/prysm/pull/1732), [prysm#3820](https://github.com/OffchainLabs/prysm/pull/3820), [prysm#4494](https://github.com/OffchainLabs/prysm/pull/4494), [prysm#4489](https://github.com/OffchainLabs/prysm/pull/4489), [prysm#3672](https://github.com/OffchainLabs/prysm/pull/3672), [prysm#5534](https://github.com/OffchainLabs/prysm/pull/5534), [prysm#5320](https://github.com/OffchainLabs/prysm/pull/5320), [teku#5903](https://github.com/Consensys-Incorporated/teku/pull/5903)

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

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [nimbus#8852](https://github.com/status-im/nimbus-eth2/pull/8852), [nimbus@884193b2d](https://github.com/status-im/nimbus-eth2/commit/884193b2d2a5), [prysm#8911](https://github.com/OffchainLabs/prysm/pull/8911), [nimbus#5391](https://github.com/status-im/nimbus-eth2/pull/5391)

</details>


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


<a id="db_hot-005"></a>
<details>
<summary><b>db_hot-005</b> Slot-indexed canonical block root lookup — <i>implemented · low · S · cpu, disk, latency</i></summary>

**Idea.** Maintain a slot-indexed index (DB table or in-memory array) from slot to canonical block root, updated on head change, reorg and finalization, so by-slot lookups (REST, BlocksByRange, ancestors) are direct reads instead of walking parent links back from the head.

**Impact.** By-slot lookups are O(1) from the head state's 8192-slot vector or the freezer column; a walk happens only for unfinalized slots more than 8192 slots behind the head.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:1060`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1060) block_root_at_slot_skips_none reads head state's block_roots vector
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1124`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1124) block_root_at_slot_skips_prev same fast path
- [`beacon_node/store/src/hot_cold_store.rs:3096`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3096) get_cold_block_root: slot-indexed DBColumn::BeaconBlockRoots in the freezer
- [`beacon_node/store/src/forwards_iter.rs:29`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/forwards_iter.rs#L29) forwards_iter_block_roots_using_state for the unfinalized range

**Skeptic check.** Verified both lookup paths. The only remaining walk (BlockRootsIterator over hot states) happens in non-finality longer than ~27h, which is too rare to count as a gap.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [ethlambda#495](https://github.com/lambdaclass/ethlambda/pull/495), [prysm#2278](https://github.com/OffchainLabs/prysm/pull/2278), [prysm#15063](https://github.com/OffchainLabs/prysm/pull/15063), [nimbus#3144](https://github.com/status-im/nimbus-eth2/pull/3144)

</details>


<a id="db_hot-006"></a>
<details>
<summary><b>db_hot-006</b> Big-endian fixed-width integer keys for range scans — <i>implemented · low · S · disk, cpu</i></summary>

**Idea.** Encode integer DB keys (slots, indices) as fixed-width big-endian so lexicographic key order equals numeric order. Slot-range queries become one ordered cursor range scan instead of a full scan.

**Impact.** Slot-keyed freezer columns use BE u64 keys and ordered range scans.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3577`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3577) BeaconBlockRoots keyed by slot.to_be_bytes()
- [`beacon_node/store/src/forwards_iter.rs:138`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/forwards_iter.rs#L138) iter_column_from BE start slot
- [`beacon_node/store/src/hot_cold_store.rs:2161`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2161) BeaconStateSnapshot keyed by BE slot

**Skeptic check.** Verified the BE keys and the cursor seek. Hot DB columns are keyed by root, so slot-range scans on them do not apply.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#875](https://github.com/ChainSafe/lodestar/pull/875), [prysm#3221](https://github.com/OffchainLabs/prysm/pull/3221)

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


<a id="db_hot-008"></a>
<details>
<summary><b>db_hot-008</b> Disable contended store block cache — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Make the store-level block cache optional and off by default, because the mutex around it contends when many threads read blocks concurrently.

**Impact.** The cache is off by default, so readers do not contend on its mutex.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/config.rs:22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L22) DEFAULT_BLOCK_CACHE_SIZE = 0
- [`beacon_node/store/src/hot_cold_store.rs:229`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L229) block_cache Option&lt;Mutex&lt;..&gt;&gt; only if size &gt; 0

**Skeptic check.** This is Lighthouse's own PR 8066, and it is present in the checkout.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#8066](https://github.com/sigp/lighthouse/pull/8066)

</details>


<a id="db_hot-009"></a>
<details>
<summary><b>db_hot-009</b> Do not store EL-reconstructible execution payloads — <i>implemented · medium · S · disk</i></summary>

**Idea.** Store beacon blocks blinded (without payload transactions and withdrawals), or prune payloads of finalized blocks at migration, since the execution client already holds them, and rebuild the full block from the EL when serving it. This avoids storing each payload twice and cuts disk usage and write I/O.

**Impact.** Finalized payloads are not kept twice; full blocks are rebuilt from the EL when served.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:527`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L527) block_as_kv_store_ops stores blinded block and payload separately
- [`beacon_node/beacon_chain/src/migrate.rs:868`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L868) finalization deletes ExecutionPayload/Payload when prune_payloads
- [`beacon_node/store/src/config.rs:117`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L117) prune_payloads defaults to true
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1275`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1275) get_block rebuilds a full block from the EL for blinded blocks
- [`beacon_node/store/src/hot_cold_store.rs:1019`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1019) Gloas envelope bodies are stored in a separate PayloadBody column and pruned too

**Skeptic check.** Confirmed blinded storage, pruning at each finalization migration (not only the startup try_prune_execution_payloads the earlier evidence cited), and EL rebuild on read.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#6029](https://github.com/ChainSafe/lodestar/pull/6029), [lodestar#7034](https://github.com/ChainSafe/lodestar/pull/7034), [lighthouse#3157](https://github.com/sigp/lighthouse/pull/3157), [lodestar#5705](https://github.com/ChainSafe/lodestar/pull/5705), [lighthouse#3565](https://github.com/sigp/lighthouse/pull/3565), [grandine#949](https://github.com/grandinetech/grandine/pull/949), [teku#5991](https://github.com/Consensys-Incorporated/teku/pull/5991), [teku#5959](https://github.com/Consensys-Incorporated/teku/pull/5959), [teku#6044](https://github.com/Consensys-Incorporated/teku/pull/6044)

</details>


<a id="db_hot-010"></a>
<details>
<summary><b>db_hot-010</b> Load blinded block when payload not needed — <i>implemented · medium · S · disk, cpu</i></summary>

**Idea.** When a caller only needs block metadata or commitments, read the blinded block from the DB instead of the full block with payload, avoiding a large read and decode.

**Impact.** Metadata readers load blinded blocks; only endpoints that return the payload load it.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:663`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L663) get_blinded_block
- [`beacon_node/http_api/src/block_id.rs:119`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L119) header/root API paths use get_blinded_block
- [`beacon_node/http_api/src/lib.rs:1199`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L1199) full_block only for GET beacon/blocks, which needs the payload
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1592`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1592) Gloas bid lookup: try_get_full_block has no payload to load for Gloas blocks

**Skeptic check.** Checked the get_block/full_block call sites in http_api, network and beacon_chain. The ones that remain need the payload or read fork-choice proto blocks, not the DB.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@caad492d4](https://github.com/sigp/lighthouse/commit/caad492d48aa)

</details>


<a id="db_hot-011"></a>
<details>
<summary><b>db_hot-011</b> Compact block summary table for fast startup — <i>implemented · medium · S · startup, disk, cpu</i></summary>

**Idea.** Persist a compact summary (root, parent, slot) for each block in its own table, loadable in one query, so startup can build the block DAG without loading and decoding full blocks.

**Impact.** Startup rebuilds the block DAG from one persisted proto-array read, with no full block decode.

**Best measured result.** startup times from minutes to seconds (pr:nimbus#1950)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:692`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L692) load_fork_choice reads one persisted ForkChoice blob (proto-array with root/parent/slot per node)
- [`beacon_node/beacon_chain/src/canonical_head.rs:1746`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1746) persist_fork_choice

**Skeptic check.** Verified load_fork_choice: one get_bytes plus decode. The earlier citation of load_hot_state_summaries is not on the startup DAG path (it is used for pruning), but the persisted proto-array alone gives the same effect.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus@fc7885b27](https://github.com/status-im/nimbus-eth2/commit/fc7885b27e6e), [nimbus#1950](https://github.com/status-im/nimbus-eth2/pull/1950), [nimbus@22ddf7475](https://github.com/status-im/nimbus-eth2/commit/22ddf747520d), [teku#953](https://github.com/Consensys-Incorporated/teku/pull/953)

</details>


<a id="db_hot-012"></a>
<details>
<summary><b>db_hot-012</b> Store each data column/blob sidecar under its own key — <i>implemented · medium · S · cpu, disk, bandwidth</i></summary>

**Idea.** Key each data column or blob sidecar by (block root or slot, index) instead of storing the whole per-block list under one key. Serving one column reads and decodes one item, and shared fields are not duplicated.

**Impact.** Done for data columns, the live post-Fulu path. Pre-Fulu blob sidecars remain one list per block, but that path is legacy and expires with the retention window.

**Best measured result.** avoids up to x128 more I/O than necessary (pr:lighthouse#5890)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/lib.rs:144`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/lib.rs#L144) get_data_column_key = block_root\|\|column_index
- [`beacon_node/store/src/hot_cold_store.rs:956`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L956) data_column_as_kv_store_ops one key per column
- [`beacon_node/store/src/hot_cold_store.rs:2679`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2679) get_data_column reads a single column key
- [`beacon_node/store/src/hot_cold_store.rs:943`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L943) blobs_as_kv_store_ops still stores the whole pre-Fulu BlobSidecarList under the block root

**Skeptic check.** Confirmed per-(root,index) keys for data columns on write, read and prune. The earlier evidence was right; only legacy Deneb/Electra blobs are still one list per block, which no longer matters after Fulu.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#5890](https://github.com/sigp/lighthouse/pull/5890), [lodestar#8206](https://github.com/ChainSafe/lodestar/pull/8206), [lodestar#8233](https://github.com/ChainSafe/lodestar/pull/8233), [lighthouse#6073](https://github.com/sigp/lighthouse/pull/6073)

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


<a id="db_hot-014"></a>
<details>
<summary><b>db_hot-014</b> Existence check without loading value — <i>partial · low · M · memory, cpu</i></summary>

**Idea.** Check whether a state or record exists in the DB with a key-existence call that does not allocate or read the value bytes.

**Gap in Lighthouse.** An existence API exists everywhere, but on LevelDB it calls Database::get and drops the value, so it still reads and allocates it. Leveldb crate 0.8.6 exposes no key-may-exist, so the fix would be a bloom/seek-based check or small summary-key checks.

**Impact.** Saves value reads only for existence checks on large values (blocks); these are not hot paths, so gain is negligible.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/database/leveldb_impl.rs:121`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/leveldb_impl.rs#L121) key_exists uses db.get then is_some (reads value)
- [`beacon_node/store/src/database/redb_impl.rs:128`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/redb_impl.rs#L128) key_exists uses table.get, no value copy
- [`beacon_node/store/src/hot_cold_store.rs:909`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L909),915 block/blob existence via key_exists

**Sources.** [prysm#8928](https://github.com/OffchainLabs/prysm/pull/8928)

</details>


<a id="db_hot-015"></a>
<details>
<summary><b>db_hot-015</b> Single cursor pass for bulk state deletion — <i>n/a · low · cpu, disk</i></summary>

**Idea.** When deleting many states, collect the keys in a set and traverse the bucket once with a cursor instead of a separate seek or binary search per key.

**Impact.** LevelDB deletes are tombstone writes in a WriteBatch, with no per-key seek or binary search, so the BoltDB cursor problem does not exist.

**Best measured result.** "much faster deletion of states" (pr:prysm#4909)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/database/leveldb_impl.rs:262`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/leveldb_impl.rs#L262) delete_batch builds one Writebatch of deletes by key
- [`beacon_node/store/src/hot_cold_store.rs:1446`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1446) delete_batch dedups keys in a HashSet

**Sources.** [prysm#4909](https://github.com/OffchainLabs/prysm/pull/4909)

</details>


<a id="db_hot-016"></a>
<details>
<summary><b>db_hot-016</b> On-demand DB compaction endpoint — <i>implemented · low · S · disk</i></summary>

**Idea.** Expose an API endpoint that triggers a background compaction of the key-value store, so operators can reclaim disk after large prunes or migrations.

**Impact.** Operators can trigger a background compaction on demand.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs:2897`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L2897) POST lighthouse/compaction
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1833`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1833) manually_compact_database -&gt; store_migrator.process_manual_compaction

**Skeptic check.** Verified that the route and the migrator call exist. This is Lighthouse's own PR.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#7104](https://github.com/sigp/lighthouse/pull/7104), [lighthouse#7072](https://github.com/sigp/lighthouse/pull/7072)

</details>


<a id="db_hot-017"></a>
<details>
<summary><b>db_hot-017</b> Manual finalization endpoint to migrate and prune — <i>implemented · low · S · disk</i></summary>

**Idea.** Expose an endpoint to force a finalization migration to the freezer and prune side chains (with summaries-DAG pruning), freeing hot DB disk during long non-finality.

**Impact.** Forces migration and pruning during long non-finality.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs:2860`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L2860) POST lighthouse/finalize
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1837`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1837) manually_finalize_state -&gt; store_migrator.process_manual_finalization

**Skeptic check.** Verified that the route validates the checkpoint against the hot summary and sends the job to the migrator. This is Lighthouse's own PR.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#7059](https://github.com/sigp/lighthouse/pull/7059), [lighthouse#7060](https://github.com/sigp/lighthouse/pull/7060)

</details>


<a id="db_hot-018"></a>
<details>
<summary><b>db_hot-018</b> Hierarchical state diffs in the hot DB — <i>implemented · medium · S · disk</i></summary>

**Idea.** Store hot states as periodic snapshots plus hierarchical diffs, as in the freezer, and skip storing a state whose summary already exists. Hot DB disk footprint and write I/O drop a lot, especially during non-finality.

**Impact.** Done.

**Best measured result.** massively reduce disk footprint during non-finality and overall I/O; ~1MB per written diff on Holesky (pr:lighthouse#6750)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1697`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1697) skip storing when load_hot_state_summary already exists
- [`beacon_node/store/src/hot_cold_store.rs:1741`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1741) store_hot_state_diffs dispatches Snapshot/DiffFrom/ReplayFrom
- [`beacon_node/store/src/hot_cold_store.rs:1771`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1771) store_hot_state_as_diff computes HDiff against the ancestor diff base

**Skeptic check.** Hot states use the hierarchy grid (snapshot, diff or summary-only replay), and duplicate stores are skipped by checking the summary. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#6750](https://github.com/sigp/lighthouse/pull/6750), [lighthouse#7087](https://github.com/sigp/lighthouse/pull/7087)

</details>


<a id="db_hot-019"></a>
<details>
<summary><b>db_hot-019</b> Share validators via Arc in hdiff buffer — <i>not · medium · M · memory, cpu</i></summary>

**Idea.** Hold the validator list in hierarchical-diff buffers as reference-counted shared records, so cloning a buffer shares validators instead of copying them.

**Gap in Lighthouse.** HDiffBuffer still owns Vec&lt;Validator&gt;; every buffer clone (cold and hot hdiff caches) and every from_state/as_state deep-copies all validator records. Switch to Vec&lt;Arc&lt;Validator&gt;&gt; or keep the milhouse List (whose leaves are already shared) so clones share records; ValidatorsDiff compute/apply must deref.

**Impact.** Avoids copying ~1M x ~121 B (~120 MB) of validator records per hdiff buffer clone and reduces RSS of hdiff buffer caches on archive and non-finality nodes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hdiff.rs:97-104`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L97-L104) HDiffBuffer derives Clone with validators: Vec&lt;Validator&gt;
- [`beacon_node/store/src/hdiff.rs:185`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L185) from_state does take_validators().to_vec() (deep copy out of milhouse List)
- [`beacon_node/store/src/hdiff.rs:227`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L227) as_state rebuilds via set_validators_from_iter(self.validators.iter().cloned())
- [`beacon_node/store/src/historic_state_cache.rs:37-50`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/historic_state_cache.rs#L37-L50) get_hdiff_buffer returns buffer_ref.clone() and clones again on insert
- [`beacon_node/store/src/state_cache.rs:59-63`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L59-L63) HotHDiffBufferCache LruCache&lt;Hash256,(Slot,HDiffBuffer)&gt;
- [`consensus/types/src/validator/validator.rs:21`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/validator/validator.rs#L21) Validator is a plain struct
- pr:lighthouse#7675 Vec&lt;Arc&lt;Validator&gt;&gt; change CLOSED, not merged

**Second check.** Grepped the whole tree for Arc&lt;Validator&gt; (no hits) and checked both hdiff buffer caches (historic_state_cache and hot state_cache) and their clone paths; the prescreen claim 'Lighthouse already does' is wrong, PR 7675 was closed unmerged.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [lighthouse#7675](https://github.com/sigp/lighthouse/pull/7675)

</details>


<a id="db_hot-020"></a>
<details>
<summary><b>db_hot-020</b> Cache hot hdiff buffers alongside state cache — <i>implemented · low · S · cpu, disk, latency</i></summary>

**Idea.** Keep an in-memory cache of the hot DB hierarchical-diff buffers on the path to the finalized state, so storing a new hot state does not reload and rebuild those buffers.

**Impact.** Done.

**Best measured result.** Costs about 438 MB per buffer on Holesky; reduces store time (pr:lighthouse#7615)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:58`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L58) HotHDiffBufferCache
- [`beacon_node/store/src/state_cache.rs:152-175`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L152-L175) update_finalized_state keeps the grid buffers and converts pruned states into buffers
- [`beacon_node/store/src/state_cache.rs:295`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L295) get_hdiff_buffer_by_state_root also falls back to full cached states
- [`beacon_node/store/src/hot_cold_store.rs:1861`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1861) load_hot_hdiff_buffer checks the cache first and caches the result via put_hdiff_buffer
- [`beacon_node/store/src/config.rs:28`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L28) DEFAULT_HOT_HDIFF_BUFFER_CACHE_SIZE=1

**Skeptic check.** Verified that the store path (store_hot_state_as_diff -&gt; load_hot_hdiff_buffer) hits the buffer cache, or a cached post-finalized state, before rebuilding. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#7615](https://github.com/sigp/lighthouse/pull/7615)

</details>


<a id="db_hot-021"></a>
<details>
<summary><b>db_hot-021</b> Bound prune iteration to not-yet-pruned range — <i>implemented · medium · S · disk, cpu</i></summary>

**Idea.** Start pruning at the first existing key or oldest stored slot and stop at the first entry already pruned or still retained, using an ordered cursor or backward iterator, instead of scanning the whole column on each prune.

**Impact.** Blob, column and payload prunes touch only the new range. A small cost remains: Fulu pruning does key_exists on all 128 column keys per block (hot_cold_store.rs:2672 get_all_data_column_keys).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3349`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3349) try_prune_blobs walks ParentRootBlockIterator backwards from end_slot
- [`beacon_node/store/src/hot_cold_store.rs:3419`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3419) breaks at the first block with blobs/columns already pruned
- [`beacon_node/store/src/hot_cold_store.rs:3148`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3148) try_prune_execution_payloads returns early when finalized_payloads_are_pruned
- [`beacon_node/store/src/hot_cold_store.rs:3202`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3202) payload loop stops at oldest_block_slot
- [`beacon_node/beacon_chain/src/migrate.rs:869`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L869) per-finalization payload prune only touches newly finalized blocks

**Skeptic check.** Verified the backward iterator with early break (#8266) and the early return plus oldest_block_slot bound for payloads (#6745). The full payload scan runs only when payloads are not yet pruned, so it is real work, not a rescan.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#8266](https://github.com/sigp/lighthouse/pull/8266), [prysm#8627](https://github.com/OffchainLabs/prysm/pull/8627), [lighthouse#6745](https://github.com/sigp/lighthouse/pull/6745), [lodestar@335059d5f](https://github.com/ChainSafe/lodestar/commit/335059d5fa8a), [lighthouse#7228](https://github.com/sigp/lighthouse/pull/7228)

</details>


<a id="db_hot-022"></a>
<details>
<summary><b>db_hot-022</b> Prune blobs outside retention window, verify deletion — <i>implemented · medium · S · disk</i></summary>

**Idea.** Delete blob sidecars from the DB once they are outside the data availability retention window, and check that pruning uses the same key encoding as writes and a correct existence check so expired data is really deleted and the blob store stays bounded.

**Impact.** Blob store stays bounded already.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3277`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3277) try_prune_blobs prunes to min(DA boundary - margin, split) - 1
- [`beacon_node/store/src/hot_cold_store.rs:2672`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2672) get_all_data_column_keys uses the same get_data_column_key as writes
- [`beacon_node/store/src/hot_cold_store.rs:3407`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3407) key_exists then DeleteKey on that key
- [`beacon_node/beacon_chain/src/migrate.rs:777-789`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L777-L789) abandoned-fork blocks also get DeleteBlobs/DeleteDataColumns
- [`beacon_node/beacon_chain/src/canonical_head.rs:1734`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1734) prune triggered on finalization

**Skeptic check.** The prune key encoding matches the write encoding, and existence is checked per key. Non-canonical blobs are removed by prune_hot_db, so the store stays bounded. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine@3efe29029](https://github.com/grandinetech/grandine/commit/3efe2902904a), [lighthouse#4693](https://github.com/sigp/lighthouse/pull/4693), [nimbus#5283](https://github.com/status-im/nimbus-eth2/pull/5283)

</details>


<a id="db_hot-023"></a>
<details>
<summary><b>db_hot-023</b> Delete abandoned fork blocks and states at finalization — <i>implemented · medium · S · disk</i></summary>

**Idea.** On finalization, delete blocks and states (including skipped-slot states) of abandoned forks at or below the finalized slot from the hot DB, keeping states shared with the canonical chain and the finalized boundary state. Abandoned forks then do not accumulate and the hot DB stops growing without bound.

**Impact.** Abandoned forks are removed at each finalization.

**Best measured result.** should end unbounded chain_db growth (pr:lighthouse#1564)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/migrate.rs:509`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L509) prune_hot_db builds StateSummariesDAG
- [`beacon_node/beacon_chain/src/migrate.rs:658-705`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L658-L705) states_to_prune: non-descendants of the finalized checkpoint, keeping the required hdiff grid states
- [`beacon_node/beacon_chain/src/migrate.rs:707-739`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L707-L739) blocks_to_prune for abandoned forks
- [`beacon_node/beacon_chain/src/migrate.rs:777-794`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L777-L794) deletes block, payload, blobs, columns and states

**Skeptic check.** Verified that every hot summary (skipped-slot states included) that does not descend from the finalized checkpoint is pruned, along with its blocks and sidecars. The finalized state and the grid states are kept. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#1564](https://github.com/sigp/lighthouse/pull/1564), [lighthouse#916](https://github.com/sigp/lighthouse/pull/916), [grandine#145](https://github.com/grandinetech/grandine/pull/145), [grandine@4c2be4b16](https://github.com/grandinetech/grandine/commit/4c2be4b16434)

</details>


<a id="db_hot-024"></a>
<details>
<summary><b>db_hot-024</b> Prune in-memory hot collections on finalization — <i>implemented · low · S · memory</i></summary>

**Idea.** Check that the finalization pruning of hot in-memory block and state collections actually removes entries (prune by map keys), so these collections shrink on finalization.

**Impact.** None: hot collections shrink on finalization.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array.rs:2073-2106`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L2073-L2106) maybe_prune removes indices keys for dropped roots, split_off nodes and children
- [`beacon_node/store/src/state_cache.rs:146-170`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L146-L170) block_map.prune and states.remove by state_root on finalization, hdiff buffer cache rebuilt

**Skeptic check.** Checked that proto_array maybe_prune removes map entries by key and the state cache deletes pruned state roots on finalization. The earlier evidence was right; the Teku bug (pruning by values) has no counterpart here.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#10308](https://github.com/Consensys-Incorporated/teku/pull/10308)

</details>


<a id="db_hot-025"></a>
<details>
<summary><b>db_hot-025</b> Keep pruning off the startup path — <i>implemented · medium · S · disk, startup</i></summary>

**Idea.** Do not run heavy scan-and-delete pruning (old states, payloads) synchronously at startup: put it behind a flag, run it in a background thread, or do it incrementally. Node startup is then not blocked for minutes.

**Impact.** Startup is not blocked by payload or blob pruning. Historic-state pruning is an explicit db subcommand.

**Best measured result.** startup prune 2m5s on good I/O, 16m on slow (pr:lighthouse#3587)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/builder.rs:1164`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L1164) try_prune_execution_payloads in spawn_blocking
- [`beacon_node/beacon_chain/src/builder.rs:1177`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L1177) process_prune_blobs sent to the background migrator
- [`beacon_node/beacon_chain/src/builder.rs:1159`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L1159) state reconstruction via the background migrator
- [`beacon_node/store/src/hot_cold_store.rs:389`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L389) foreground compaction only behind compact_on_init
- [`beacon_node/store/src/hot_cold_store.rs:3471`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3471) prune_historic_states only from the db subcommand

**Skeptic check.** Checked HotColdDB::open and the chain builder: the only synchronous heavy steps are schema migrations and an opt-in compaction. All pruning is in the background. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#3587](https://github.com/sigp/lighthouse/pull/3587), [nimbus#5191](https://github.com/status-im/nimbus-eth2/pull/5191), [prysm#5011](https://github.com/OffchainLabs/prysm/pull/5011)

</details>


<a id="db_hot-026"></a>
<details>
<summary><b>db_hot-026</b> Tune RocksDB block cache, compaction and WAL — <i>n/a · low · cpu, memory, disk, latency</i></summary>

**Idea.** Configure the embedded RocksDB with a sized shared block cache, dynamic level bytes, index/filter blocks not charged to the cache, more background jobs and subcompactions, larger compaction readahead, periodic sync, capped and recycled WAL and adjusted bottommost compression. Compaction keeps up and iterators and seeks become fast.

**Impact.** Lighthouse uses LevelDB (or redb), not RocksDB; these knobs do not exist there.

**Best measured result.** iterators from minutes to ms; memory similar (pr:teku#9080)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/database/leveldb_impl.rs:36`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/leveldb_impl.rs#L36) Options::new with defaults
- [`beacon_node/store/src/database/redb_impl.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/redb_impl.rs): redb backend alternative

**Sources.** [ethlambda#380](https://github.com/lambdaclass/ethlambda/pull/380), [teku#9080](https://github.com/Consensys-Incorporated/teku/pull/9080), [teku#9079](https://github.com/Consensys-Incorporated/teku/pull/9079)

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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [teku#2248](https://github.com/Consensys-Incorporated/teku/pull/2248), [teku#2225](https://github.com/Consensys-Incorporated/teku/pull/2225), [teku#2222](https://github.com/Consensys-Incorporated/teku/pull/2222), [teku#2239](https://github.com/Consensys-Incorporated/teku/pull/2239), [teku#6208](https://github.com/Consensys-Incorporated/teku/pull/6208), [teku#2381](https://github.com/Consensys-Incorporated/teku/pull/2381)

</details>


<a id="db_hot-028"></a>
<details>
<summary><b>db_hot-028</b> Lower max open files for the KV store — <i>not · low · S · memory</i></summary>

**Idea.** Set a lower, backend-specific default for maximum open files in the LevelDB/RocksDB store, because each open file costs memory.

**Gap in Lighthouse.** Set options.max_open_files (and optionally block cache size) in LevelDB::open, perhaps via a store config flag. LevelDB default is 1000 files.

**Impact.** Would bound file-handle memory on LevelDB nodes; the gain is small since the default is already modest.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/database/leveldb_impl.rs:36-41`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/leveldb_impl.rs#L36-L41) only create_if_missing set; max_open_files left None
- ~/.cargo/registry/src/*/leveldb-0.8.6/src/database/options.rs:42 max_open_files option exists

**Sources.** [teku#2428](https://github.com/Consensys-Incorporated/teku/pull/2428), [teku#6215](https://github.com/Consensys-Incorporated/teku/pull/6215)

</details>


<a id="db_hot-029"></a>
<details>
<summary><b>db_hot-029</b> Disable DB block cache, rely on page cache — <i>not · low · S · memory</i></summary>

**Idea.** Turn off the key-value store's own block cache and rely on the OS page cache to reduce resident memory.

**Gap in Lighthouse.** LevelDB::open could set options.cache to a zero-size Cache to drop the 8MB block cache; it is only 8MB, so the memory saving is tiny.

**Impact.** Saves at most ~8MB RSS on LevelDB nodes and could slow reads; no clear gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/database/leveldb_impl.rs:37`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/leveldb_impl.rs#L37) - Options::new() with only create_if_missing, so LevelDB's default 8MB block cache stays on
- [`beacon_node/store/src/database/redb_impl.rs:30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/redb_impl.rs#L30) - redb::Database::create with defaults, no cache setting

**Sources.** [teku#3538](https://github.com/Consensys-Incorporated/teku/pull/3538)

</details>


<a id="db_hot-030"></a>
<details>
<summary><b>db_hot-030</b> Larger SQLite page cache — <i>n/a · low · S · disk, memory</i></summary>

**Idea.** Raise the SQLite page cache size so more pages stay in memory and fewer reads hit disk.

**Impact.** Lighthouse has no SQLite backend.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/Cargo.toml:8-27`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/Cargo.toml#L8-L27) - only leveldb and redb backends, no SQLite

**Sources.** [nimbus#2607](https://github.com/status-im/nimbus-eth2/pull/2607)

</details>


<a id="db_hot-031"></a>
<details>
<summary><b>db_hot-031</b> Upgrade embedded LevelDB and Snappy — <i>partial · low · M · disk, cpu</i></summary>

**Idea.** Use recent LevelDB and Snappy versions to pick up upstream performance fixes.

**Gap in Lighthouse.** Only LevelDB 1.22 is bundled via an unmaintained sys crate; moving to 1.23 would need a forked leveldb-sys. Snappy is not used at all.

**Impact.** 1.23 has few performance changes; negligible gain for mainnet nodes.

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.lock:5719,5730 - leveldb 0.8.6 / leveldb-sys 2.0.9
- leveldb-sys-2.0.9/deps/leveldb-1.22 - bundled LevelDB 1.22 (2019), upstream is 1.23
- [`beacon_node/store/Cargo.toml:22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/Cargo.toml#L22) - default-features=false so the snappy feature is off, no Snappy is built

**Sources.** [teku#7504](https://github.com/Consensys-Incorporated/teku/pull/7504)

</details>


<a id="db_hot-032"></a>
<details>
<summary><b>db_hot-032</b> Alternative embedded KV backend (LevelDB vs RocksDB) — <i>implemented · low · S · memory, disk</i></summary>

**Idea.** Offer or switch to a second embedded key-value backend (for example LevelDB instead of RocksDB) behind the same accessor interface, to get a lighter database with smaller disk footprint, compaction cost and memory.

**Impact.** None: two embedded backends behind one interface, selectable at runtime.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/Cargo.toml:8-11`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/Cargo.toml#L8-L11) leveldb default feature, redb optional
- [`beacon_node/store/src/database/interface.rs:10-14`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/interface.rs#L10-L14) BeaconNodeBackend enum over LevelDb and Redb
- [`beacon_node/src/cli.rs:1679-1683`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L1679-L1683) --beacon-node-backend flag

**Skeptic check.** Confirmed that BeaconNodeBackend dispatches every KV operation to LevelDB or redb and that a CLI flag selects the backend. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#3550](https://github.com/Consensys-Incorporated/teku/pull/3550), [lighthouse@7d067926d](https://github.com/sigp/lighthouse/commit/7d067926dd20)

</details>


<a id="db_hot-033"></a>
<details>
<summary><b>db_hot-033</b> Large initial mmap size for embedded DB — <i>n/a · low · S · latency, disk</i></summary>

**Idea.** Set a large initial memory-map size for an mmap-based embedded DB so it does not remap while it grows, because remaps block reads and writes.

**Impact.** Lighthouse's default LevelDB backend has no mmap-resize stalls; redb (opt-in) uses its own growth policy.

**Best measured result.** Reports bad performance for 10-30 min at startup with many validators; no after numbers (pr:prysm#8448)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/database/leveldb_impl.rs:37`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/leveldb_impl.rs#L37) - LevelDB is not mmap-sized
- [`beacon_node/store/src/database/redb_impl.rs:30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/redb_impl.rs#L30) - redb grows its file itself, no initial map size set

**Sources.** [prysm#8448](https://github.com/OffchainLabs/prysm/pull/8448)

</details>


<a id="db_hot-034"></a>
<details>
<summary><b>db_hot-034</b> Size DB dirty-page limit from cgroup memory — <i>n/a · low · S · memory</i></summary>

**Idea.** Derive the embedded DB's dirty-page or cache limit from the container memory limit instead of host RAM, and set it before the environment opens, so the DB stays inside the memory budget.

**Impact.** Neither backend has an mmap dirty-page limit tied to RAM.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/database/leveldb_impl.rs:37`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/leveldb_impl.rs#L37) - LevelDB has no dirty-page limit option
- [`beacon_node/store/src/database/redb_impl.rs:30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/redb_impl.rs#L30) - redb has no such option

**Sources.** [caplin#9189](https://github.com/erigontech/erigon/pull/9189)

</details>


<a id="db_hot-035"></a>
<details>
<summary><b>db_hot-035</b> WAL checkpoint once per slot, no fsync mid-slot — <i>n/a · low · S · disk, latency</i></summary>

**Idea.** Run the database in WAL mode with auto-checkpoint and fsync off during slot processing, and checkpoint once at slot end or every few slots, so block processing never blocks on file-system sync.

**Impact.** No SQLite WAL; LevelDB writes are already non-fsync by default and redb durability is chosen per write.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/database/leveldb_impl.rs:27-33`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/leveldb_impl.rs#L27-L33) - write sync flag only per write, default no fsync
- [`beacon_node/store/src/database/redb_impl.rs:17-22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/redb_impl.rs#L17-L22) - Durability::Eventual vs Immediate per write

**Sources.** [nimbus#2236](https://github.com/status-im/nimbus-eth2/pull/2236), [nimbus#2195](https://github.com/status-im/nimbus-eth2/pull/2195)

</details>


<a id="db_hot-036"></a>
<details>
<summary><b>db_hot-036</b> Skip fsync on rebuildable cache dumps — <i>implemented · low · S · disk, latency</i></summary>

**Idea.** Do not fsync files that only hold rebuildable cache data (for example periodic fork-graph or head-state dumps), shortening the time held under shared locks.

**Impact.** No fsync on cache-like data. Lighthouse has no periodic head-state or fork-graph file dumps.

**Best measured result.** head-state dump p50 ~540 ms for 143 MB (baseline; gain not stated) (pr:caplin#25251)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/database/leveldb_impl.rs:49`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/leveldb_impl.rs#L49) write_options default sync=false
- [`beacon_node/store/src/database/redb_impl.rs:17-22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/redb_impl.rs#L17-L22),158 do_atomically uses Durability::Eventual unless sync
- [`beacon_node/store/src/hot_cold_store.rs:3627`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3627),3655 the only sync writes are cold_db.sync and the split put_sync
- [`beacon_node/beacon_chain/src/historical_blocks.rs:434`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_blocks.rs#L434) blobs_db.sync for backfill metadata ordering

**Skeptic check.** Every sync write is ordering-critical (split point, backfill). Op pool, custody context and fork choice persist without fsync on both backends. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#25251](https://github.com/erigontech/erigon/pull/25251)

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


<a id="db_hot-038"></a>
<details>
<summary><b>db_hot-038</b> No read transaction nested in write transaction — <i>n/a · low · S · latency</i></summary>

**Idea.** Do not open a DB read transaction inside a write transaction (for example when saving the head root); restructure so the code does not block remaps and stall for seconds.

**Impact.** The nested read-in-write deadlock is specific to bolt/mdbx; LevelDB has no transactions and redb is used with separate txns.

**Best measured result.** Put spans up to ~4s observed before fix (pr:prysm#9428)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/database/redb_impl.rs:74`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/redb_impl.rs#L74),158 - write txns do not open nested read txns
- [`beacon_node/store/src/database/leveldb_impl.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/leveldb_impl.rs) - LevelDB has no transactions

**Sources.** [prysm#9428](https://github.com/OffchainLabs/prysm/pull/9428)

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

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [prysm#14612](https://github.com/OffchainLabs/prysm/pull/14612), [prysm#17518](https://github.com/OffchainLabs/prysm/pull/17518), [prysm#14613](https://github.com/OffchainLabs/prysm/pull/14613)

</details>


<a id="db_hot-040"></a>
<details>
<summary><b>db_hot-040</b> Generated SSZ codecs for DB objects — <i>n/a · low · S · cpu</i></summary>

**Idea.** Encode and decode stored objects with generated SSZ marshal/unmarshal code instead of reflection-based protobuf serialization.

**Impact.** Lighthouse already stores SSZ, never protobuf; nothing to gain.

**Best measured result.** uses fast marshaling instead of proto.Marshal for speed (pr:prysm#5351)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:744`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L744) - stored objects use SSZ bytes via from_ssz_bytes_by_fork

**Sources.** [prysm#5351](https://github.com/OffchainLabs/prysm/pull/5351)

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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [lodestar#8627](https://github.com/ChainSafe/lodestar/pull/8627), [lodestar#8907](https://github.com/ChainSafe/lodestar/pull/8907)

</details>


<a id="db_hot-042"></a>
<details>
<summary><b>db_hot-042</b> Fork-specific decoding of stored payloads — <i>implemented · low · S · cpu</i></summary>

**Idea.** Decode stored execution payloads with the deserializer of the known fork instead of trying each fork variant in turn.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:735-751`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L735-L751) get_execution_payload decodes with from_ssz_bytes_by_fork(fork_name)
- [`beacon_node/store/src/hot_cold_store.rs:612`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L612),654 callers pass fork_name
- [`beacon_node/store/src/hot_cold_store.rs:755`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L755) get_execution_payload_dangerous_fork_agnostic has no callers

**Skeptic check.** Every caller of get_execution_payload passes the fork. A grep found no caller of the fork-agnostic variant. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#3758](https://github.com/sigp/lighthouse/pull/3758)

</details>


<a id="db_hot-043"></a>
<details>
<summary><b>db_hot-043</b> Parallel slasher double-vote detection — <i>not · low · M · cpu, disk</i></summary>

**Idea.** Run slasher double-vote detection concurrently across attestations, and keep the on-disk record schema compact (a denormalized per-validator copy of full records blew up disk and was reverted).

**Gap in Lighthouse.** Would need to split the read-check part of check_and_update_attester_record from the write and run it across attestations with rayon (already a slasher dependency), then apply writes serially. LMDB/MDBX write txn is single-threaded.

**Impact.** Only slasher-enabled nodes (rare) would see a faster batch; gain unclear.

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/slasher.rs:213-240`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/slasher.rs#L213-L240) - process_batch checks double votes in a sequential loop within one write txn
- [`slasher/src/slasher.rs:266-300`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/slasher.rs#L266-L300) - check_double_votes loops validators serially via db.check_and_update_attester_record

**Sources.** [prysm#8927](https://github.com/OffchainLabs/prysm/pull/8927), [prysm#9086](https://github.com/OffchainLabs/prysm/pull/9086)

</details>


<a id="db_hot-044"></a>
<details>
<summary><b>db_hot-044</b> Deduplicate slasher attestations by signing root — <i>implemented · low · S · disk</i></summary>

**Idea.** Store slasher attestation records once per signing root and reference them per validator, instead of one copy of the attestation data per validator.

**Impact.** None: the per-validator records reference one stored attestation.

**Best measured result.** Said to reduce disk requirements by a lot; no numbers (pr:prysm#9130)

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/database.rs:497-532`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L497-L532) store_indexed_attestation dedups by (target_epoch, indexed_attestation_hash) and returns one id
- [`slasher/src/attester_record.rs:22-26`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/attester_record.rs#L22-L26) CompactAttesterRecord per validator holds only the 8-byte indexed_attestation_id

**Skeptic check.** The dedup key is the indexed-attestation hash, not the signing root. So aggregates of the same data with different bits are stored separately, but the per-validator copy that Prysm removed does not exist here. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#9130](https://github.com/OffchainLabs/prysm/pull/9130)

</details>


<a id="db_hot-045"></a>
<details>
<summary><b>db_hot-045</b> Deduplicate secondary index entries before write — <i>n/a · low · S · disk</i></summary>

**Idea.** Remove duplicate entries before writing secondary filter indices to the DB so duplicates are not stored.

**Impact.** Lighthouse has no Prysm-style filter index tables to dedupe.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs) - no secondary filter indices; lookups are by block root / slot keys

**Sources.** [prysm#4118](https://github.com/OffchainLabs/prysm/pull/4118)

</details>


<a id="db_hot-046"></a>
<details>
<summary><b>db_hot-046</b> Store sync committees once, reference by hash — <i>implemented · low · S · disk</i></summary>

**Idea.** Store each distinct sync committee once in its own column and have light-client bootstrap records reference it by hash, instead of embedding the ~24 KB committee in every bootstrap.

**Impact.** None: committee already stored once per period, only the Merkle branch per block root.

**Best measured result.** per period 8192*25KB=205MB down to 8192*1.2KB+24KB=10MB (~20x) (pr:prysm#14775)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:785`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L785) get_sync_committee keyed by period in DBColumn::SyncCommittee
- [`beacon_node/store/src/hot_cold_store.rs:770`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L770) get_sync_committee_branch keyed by block root
- [`beacon_node/beacon_chain/src/light_client_server_cache.rs:212`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_server_cache.rs#L212) store_current_sync_committee skips rewrite when committee unchanged
- [`beacon_node/beacon_chain/src/light_client_server_cache.rs:396`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_server_cache.rs#L396) get_light_client_bootstrap assembles branch + per-period committee

**Skeptic check.** Verified that bootstraps are never stored whole; the committee is stored by period and the branch by block root, and the two are joined on demand. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#14775](https://github.com/OffchainLabs/prysm/pull/14775)

</details>


<a id="db_hot-047"></a>
<details>
<summary><b>db_hot-047</b> Single cache for one DB query — <i>n/a · low · S · disk, cpu</i></summary>

**Idea.** Use one shared cache or throttle instance for a given DB query (for example earliest available block slot) so the DB is not queried twice by two separate caches.

**Impact.** The value is held in memory behind one lock, so there is no double DB query.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2941`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2941) - oldest_block_slot read from in-memory anchor_info RwLock, no DB query or second cache

**Sources.** [teku#9906](https://github.com/Consensys-Incorporated/teku/pull/9906)

</details>


<a id="db_hot-048"></a>
<details>
<summary><b>db_hot-048</b> Read cheap DB variable directly, no cache — <i>n/a · low · S · latency</i></summary>

**Idea.** Remove a cache around a cheap single-key DB variable when the cache only serializes in-flight queries and makes reads queue behind large epoch-transition writes.

**Impact.** Lighthouse has no cache serializing cheap DB variable reads behind writes.

**Best measured result.** timing spikes come from reads queued behind epoch-transition DB write (pr:teku#9914)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2793-2795`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2793-L2795) - anchor info read from in-memory RwLock, not a DB read behind a queueing cache

**Sources.** [teku#9914](https://github.com/Consensys-Incorporated/teku/pull/9914)

</details>


<a id="db_hot-049"></a>
<details>
<summary><b>db_hot-049</b> Store earliest available block slot as DB variable — <i>implemented · low · S · latency, disk</i></summary>

**Idea.** Keep the earliest stored block slot in a single DB variable updated on write and prune, so BlocksByRange answers immediately instead of scanning for it.

**Impact.** None: earliest block slot is an O(1) in-memory read backed by persisted AnchorInfo.

**Best measured result.** query varied from a few ms to double-digit seconds (pr:teku#8722)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2793`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2793) get_anchor_info reads in-memory RwLock&lt;AnchorInfo&gt;
- [`beacon_node/store/src/hot_cold_store.rs:2941`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2941) get_oldest_block_slot
- [`beacon_node/store/src/hot_cold_store.rs:2804`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2804) compare_and_set_anchor_info updates it on backfill
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:520`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L520) BlocksByRange bounds the walk with get_oldest_block_slot

**Skeptic check.** Verified that AnchorInfo.oldest_block_slot is cached in memory, persisted, and updated with compare-and-set, and that RPC reads it without a scan. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#8722](https://github.com/Consensys-Incorporated/teku/pull/8722)

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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [nimbus@e6320e588](https://github.com/status-im/nimbus-eth2/commit/e6320e588125), [nimbus@ce1fda119](https://github.com/status-im/nimbus-eth2/commit/ce1fda119534)

</details>


<a id="db_hot-051"></a>
<details>
<summary><b>db_hot-051</b> Persist pending unknown-parent blocks on disk — <i>n/a · high · S · memory</i></summary>

**Idea.** Store blocks waiting for an unknown parent in the DB with only an in-memory index of roots, instead of holding full blocks in memory during long non-finality.

**Impact.** Negligible; memory is already bounded.

**Best measured result.** not sustainable in memory during non-finality (pr:lodestar#1670)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/mod.rs:77`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L77) MAX_LOOKUPS=200
- [`beacon_node/network/src/sync/block_lookups/mod.rs:408`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L408) lookup rejected when at cap

**Sources.** [lodestar#1670](https://github.com/ChainSafe/lodestar/pull/1670)

</details>


<a id="db_hot-052"></a>
<details>
<summary><b>db_hot-052</b> Archive all finalized blocks out of memory — <i>n/a · low · S · memory</i></summary>

**Idea.** At finalization, archive every finalized block, including optimistic or not-fully-verified ones, out of the in-memory store, so none stay resident; bound state loading during archiving.

**Impact.** Blocks are written to disk on import and only a size-limited LRU stays resident, so there is no resident finalized block set to evict.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:74`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L74),96-122 - blocks live in the DB with a bounded LRU block_cache, not an unbounded in-memory store
- [`beacon_node/beacon_chain/src/migrate.rs:166`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L166) - process_finalization prunes fork choice/hot states only

**Sources.** [grandine@d3886254f](https://github.com/grandinetech/grandine/commit/d3886254fa31), [grandine@47e697dec](https://github.com/grandinetech/grandine/commit/47e697dec5a7)

</details>


<a id="db_hot-053"></a>
<details>
<summary><b>db_hot-053</b> Load chain-link state lazily when appending — <i>n/a · low · S · cpu, memory</i></summary>

**Idea.** When appending blocks to storage, load each chain link's beacon state lazily only for links that are actually persisted, instead of loading or cloning it for every link.

**Gap in Lighthouse.** Lighthouse has no chain-link structure, and migrate_database already loads a state only for slots it persists.

**Impact.** none

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3594-3610`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3594-L3610) hot states loaded only for diff-boundary slots; others use store_cold_state_summary

**Sources.** [grandine@cfd3ed822](https://github.com/grandinetech/grandine/commit/cfd3ed822071), [grandine#127](https://github.com/grandinetech/grandine/pull/127)

</details>


<a id="db_hot-054"></a>
<details>
<summary><b>db_hot-054</b> Drive archiving from fork-choice prune events — <i>not · low · M · cpu, disk</i></summary>

**Idea.** Find finalized blocks and states to archive from fork-choice prune events and state-cache data, instead of iterating the DB or cache to discover finalized data.

**Gap in Lighthouse.** migrate_database would have to take the canonical chain from fork-choice prune output instead of RootsIterator. The current walk is a cheap in-memory iteration over state root arrays.

**Impact.** Negligible; the roots walk is tiny next to state loading and DB writes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3567-3571`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3567-L3571) RootsIterator walks finalized state roots back to split
- [`beacon_node/beacon_chain/src/migrate.rs:386`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L386) prune_hot_db loads all hot state summaries into a DAG

**Sources.** [lodestar@9c0e9266a](https://github.com/ChainSafe/lodestar/commit/9c0e9266a09a), [lodestar@13007df18](https://github.com/ChainSafe/lodestar/commit/13007df182ef)

</details>


<a id="db_hot-055"></a>
<details>
<summary><b>db_hot-055</b> Run block and state archiving concurrently — <i>n/a · low · L · latency</i></summary>

**Idea.** Run the finalized block archive and state archive tasks concurrently instead of one after the other, so finalization chores finish sooner.

**Gap in Lighthouse.** Lighthouse does not copy finalized blocks to a separate archive, and cold states are diffs that must be written sequentially (comment at 3613).

**Impact.** none

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3574-3616`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3574-L3616) migration writes only block-root index and state diffs; blocks are not moved

**Sources.** [lodestar@e4a7184a3](https://github.com/ChainSafe/lodestar/commit/e4a7184a3479)

</details>


<a id="db_hot-056"></a>
<details>
<summary><b>db_hot-056</b> Configurable epochs between freezer migrations — <i>implemented · low · S · disk, cpu</i></summary>

**Idea.** Make the number of epochs between hot-to-cold finalization migrations configurable, so the migration can run less often with larger batches.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/migrate.rs:47-50`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L47-L50) epochs_per_migration config
- [`beacon_node/beacon_chain/src/migrate.rs:310-327`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L310-L327) run_migration defers when epoch &lt; prev + epochs_per_migration
- [`beacon_node/src/cli.rs:770-771`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L770-L771) --epochs-per-migration
- [`beacon_node/src/config.rs:456-459`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/config.rs#L456-L459) applied to chain config

**Skeptic check.** Confirmed that the gate in run_migration is applied to every finalization notification and that a CLI flag sets it. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#4236](https://github.com/sigp/lighthouse/pull/4236)

</details>


<a id="db_hot-057"></a>
<details>
<summary><b>db_hot-057</b> Prune blobs once per day — <i>implemented · low · S · disk, cpu</i></summary>

**Idea.** Run blob pruning on a long period (for example every 256 epochs) instead of every few epochs, to reduce pruning work and DB churn.

**Impact.** None on CLI-launched nodes. Library users who keep StoreConfig::default() prune every epoch.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/src/cli.rs:1056-1063`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L1056-L1063) --epochs-per-blob-prune default 256
- [`beacon_node/src/config.rs:472-475`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/config.rs#L472-L475) overrides store default of 1 (store/src/config.rs:30)
- [`beacon_node/store/src/hot_cold_store.rs:3314-3316`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3314-L3316) should_prune gate in try_prune_blobs
- [`beacon_node/beacon_chain/src/migrate.rs:249`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L249) only non-forced caller

**Skeptic check.** Confirmed that the 256-epoch default is applied through the CLI and gates try_prune_blobs, which also prunes data columns. The struct default is still 1, which affects only embedders and tests.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#7113](https://github.com/sigp/lighthouse/pull/7113), [lighthouse@7103a257c](https://github.com/sigp/lighthouse/commit/7103a257cecd)

</details>


<a id="db_hot-058"></a>
<details>
<summary><b>db_hot-058</b> Periodic hot state snapshots to bound replay — <i>implemented · medium · S · cpu, disk, startup</i></summary>

**Idea.** Persist full hot (unfinalized) states only at regular intervals (every N slots or epochs, for example every epoch or every other epoch, also during sync and long non-finality) and rebuild other states by replaying blocks from the nearest snapshot. This bounds hot DB size and write volume as well as the replay cost on restart or state regeneration.

**Impact.** None: hot storage is already sparse (hdiff snapshots/diffs at layer slots, replay for the rest), which bounds writes and replay length during non-finality too.

**Best measured result.** cuts hot DB state storage by a factor of SLOTS_PER_EPOCH (32) (pr:lighthouse#746)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1722`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1722) store_hot_state_summary writes only a small summary for every state
- [`beacon_node/store/src/hot_cold_store.rs:1741`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1741) store_hot_state_diffs: ReplayFrom stores nothing, Snapshot/DiffFrom only at hierarchy slots
- [`beacon_node/store/src/hot_cold_store.rs:2042`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2042) load_hot_state replays blocks from the nearest stored base

**Skeptic check.** Verified the hot storage strategy in put_state: full data only at hierarchy layer points, summaries elsewhere, with replay from the nearest base. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#3017](https://github.com/Consensys-Incorporated/teku/pull/3017), [prysm#16589](https://github.com/OffchainLabs/prysm/pull/16589), [teku#2611](https://github.com/Consensys-Incorporated/teku/pull/2611), [teku#2663](https://github.com/Consensys-Incorporated/teku/pull/2663), [prysm#16808](https://github.com/OffchainLabs/prysm/pull/16808), [lighthouse#746](https://github.com/sigp/lighthouse/pull/746), [lighthouse#2833](https://github.com/sigp/lighthouse/pull/2833), [nimbus#1887](https://github.com/status-im/nimbus-eth2/pull/1887), [prysm#3561](https://github.com/OffchainLabs/prysm/pull/3561)

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

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [prysm#16739](https://github.com/OffchainLabs/prysm/pull/16739), [teku#1577](https://github.com/Consensys-Incorporated/teku/pull/1577)

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


<a id="db_hot-061"></a>
<details>
<summary><b>db_hot-061</b> Get state root from next block in replay — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** During block replay, load one extra block to read the state root it commits to instead of tree-hashing the replayed state.

**Impact.** None: post-block state roots come from the block, so no tree hash at block slots during replay.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/block_replayer.rs:176`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/block_replayer.rs#L176) get_state_root uses prev_block.state_root() when the state is at the block's slot
- [`consensus/state_processing/src/block_replayer.rs:221`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/block_replayer.rs#L221) extra leading block skipped and used only for its state root
- [`beacon_node/store/src/hot_cold_store.rs:2530`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2530) load_blocks_to_replay includes the block at start_slot for its state root

**Skeptic check.** Verified the mechanism of lighthouse#862 in BlockReplayer and load_blocks_to_replay. Hot replay passes no_state_root_iter (hot_cold_store.rs:2082), so skip slots are still tree-hashed, but that is outside this idea.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#862](https://github.com/sigp/lighthouse/pull/862)

</details>


<a id="db_hot-062"></a>
<details>
<summary><b>db_hot-062</b> Write DB backups without freelist — <i>n/a · low · S · disk</i></summary>

**Idea.** Write DB backups without copying the free-page list so backup files are much smaller, at the cost of a slightly slower backup.

**Gap in Lighthouse.** Lighthouse uses LevelDB/redb with no freelist-based backup feature.

**Impact.** none

**Best measured result.** "a bit slower, but results in a much smaller backup file" (pr:prysm#4847)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/database/leveldb_impl.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/leveldb_impl.rs) and redb_impl.rs: no backup function, only compact

**Sources.** [prysm#4847](https://github.com/OffchainLabs/prysm/pull/4847)

</details>


<a id="db_hot-063"></a>
<details>
<summary><b>db_hot-063</b> Keep freelist sync on bolt-style DBs and backups — <i>n/a · low · S · disk, startup</i></summary>

**Idea.** On a bolt-style DB with many deletions, and in its backups, keep freelist sync enabled: skipping it saves write cost but forces freelist reconstruction by traversing every bucket at open, which can take hours.

**Gap in Lighthouse.** Freelist sync is bolt-specific; neither backend in Lighthouse exposes it.

**Impact.** none

**Best measured result.** startup freelist reconstruction exceeded 2 hours on Pyrmont (pr:prysm#8629)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/database/redb_impl.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/redb_impl.rs), leveldb_impl.rs: no freelist sync option

**Sources.** [prysm#9069](https://github.com/OffchainLabs/prysm/pull/9069), [prysm#8629](https://github.com/OffchainLabs/prysm/pull/8629), [prysm#8601](https://github.com/OffchainLabs/prysm/pull/8601)

</details>


<a id="db_hot-064"></a>
<details>
<summary><b>db_hot-064</b> Back up DB without large memory snapshots — <i>n/a · low · S · memory, latency</i></summary>

**Idea.** Do not copy the database through process memory or one long read transaction (for example in an HTTP backup handler); copy the DB file externally or in many small per-bucket write batches. This avoids a large memory spike and keeps the node live.

**Gap in Lighthouse.** Lighthouse has no in-process DB backup handler, so no memory snapshot to avoid.

**Impact.** none

**Best measured result.** Large memory spike when backing up big DB; no numbers (pr:prysm#11235)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/database/interface.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/interface.rs): no backup API

**Sources.** [prysm#8543](https://github.com/OffchainLabs/prysm/pull/8543), [prysm#11235](https://github.com/OffchainLabs/prysm/pull/11235)

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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [prysm#13129](https://github.com/OffchainLabs/prysm/pull/13129)

</details>


<a id="db_hot-066"></a>
<details>
<summary><b>db_hot-066</b> Epoch-keyed blob directory layout with summary — <i>n/a · low · startup, disk</i></summary>

**Idea.** Lay out blob files as period/epoch/root/index and keep an in-memory summary per block root (epoch plus index mask), so startup warmup and pruning list epoch directories instead of reading every sidecar.

**Impact.** Blobs/columns live in a KV database (no file tree), there is no startup cache warm-up and pruning only visits the newly expired range, so a directory layout does not apply.

**Best measured result.** order of magnitude faster cache warm up time and sub-ms pruning times (pr:prysm#14023)

**Evidence (Lighthouse @ 928b61e719).**

- store/src/hot_cold_store.rs:3340-3430 prune_blobs walks back from end block until an already-pruned block, only touching newly expired blocks
- store/src/lib.rs:259 BeaconBlob column in KV DB keyed by block root

**Sources.** [prysm#14023](https://github.com/OffchainLabs/prysm/pull/14023)

</details>


<a id="db_hot-067"></a>
<details>
<summary><b>db_hot-067</b> Check DB before regenerating justified state — <i>implemented · low · S · cpu, sync</i></summary>

**Idea.** Before regenerating and saving the justified state, check whether the DB already holds it, so initial sync does not regenerate it at every justified checkpoint.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_fork_choice_store.rs:340-368`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_fork_choice_store.rs#L340-L368) set_justified_checkpoint uses balances_cache, loads the state only on a miss and never stores it
- [`beacon_node/beacon_chain/src/beacon_fork_choice_store.rs:260-300`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_fork_choice_store.rs#L260-L300) balances_cache filled from epoch-boundary states during import
- [`beacon_node/store/src/hot_cold_store.rs:1696-1704`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1696-L1704) store_hot_state skips the write when the summary already exists

**Skeptic check.** Lighthouse never regenerates and re-saves the justified state. Justified balances come from a cache that block import fills, and a re-store of a state is skipped when its summary exists. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#4905](https://github.com/OffchainLabs/prysm/pull/4905)

</details>


<a id="db_hot-068"></a>
<details>
<summary><b>db_hot-068</b> Write large states as fixed-size chunks — <i>not · low · L · memory</i></summary>

**Idea.** Persist the finalized or anchor state as several fixed-size chunks (for example 8 MiB) instead of one large value, avoiding huge single byte-array allocations on write and read.

**Gap in Lighthouse.** Split snapshot writes in store_hot_state_as_snapshot/store_cold_state_as_snapshot into fixed-size chunk keys with a count key. Needs DB migration.

**Impact.** Only lowers peak allocation for the rare full snapshots (a few hundred MB for mainnet); the tree-states hdiff layout already avoids per-block full-state writes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2187`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2187) - store_hot_state_as_snapshot SSZ-encodes whole state into one Vec then compresses into one value
- [`beacon_node/store/src/hot_cold_store.rs:1661`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1661) - hot states normally stored as hdiffs, not full values

**Sources.** [teku#9026](https://github.com/Consensys-Incorporated/teku/pull/9026)

</details>


<a id="db_hot-069"></a>
<details>
<summary><b>db_hot-069</b> Chunked field storage shared between states — <i>implemented · medium · S · disk</i></summary>

**Idea.** Store large BeaconState fields as separately keyed chunks so consecutive states share unchanged chunks, reducing duplication in the DB.

**Impact.** None: hdiffs remove the duplication between states more fully than chunking did.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/lib.rs:341-362`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/lib.rs#L341-L362) the chunked columns (bsr, bbr, bhr, brm) are now DEPRECATED
- [`beacon_node/store/src/hot_cold_store.rs:2160`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2160),2286 the freezer stores BeaconStateSnapshot plus BeaconStateDiff (hdiff hierarchy)
- [`beacon_node/store/src/hot_cold_store.rs:1705-1706`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1705-L1706) the hot DB stores the state summary plus hdiffs

**Skeptic check.** The effect is achieved by a stronger mechanism: hierarchical state diffs in the hot and cold DBs. The earlier evidence was partly wrong: the chunked vector columns it cited are deprecated legacy columns from before schema v22 and are no longer used for new data.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#383](https://github.com/sigp/lighthouse/pull/383)

</details>


<a id="db_hot-070"></a>
<details>
<summary><b>db_hot-070</b> Close DB environments on shutdown of loops — <i>n/a · low · S · memory</i></summary>

**Idea.** Close a persistent DB environment when its owning loop exits so it does not leak goroutines or threads.

**Impact.** none

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/database/leveldb_impl.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/leveldb_impl.rs) - LevelDB handle closes on Drop, no loop-owned environment

**Sources.** [caplin#24892](https://github.com/erigontech/erigon/pull/24892)

</details>


<a id="db_hot-071"></a>
<details>
<summary><b>db_hot-071</b> Always close DB iterators — <i>n/a · low · S · memory</i></summary>

**Idea.** Close every DB iterator (RAII) in full-scan reads so native memory is not leaked.

**Impact.** none

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/database/leveldb_impl.rs:206-281`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/leveldb_impl.rs#L206-L281) - iterators are Rust values dropped by RAII

**Sources.** [teku#2229](https://github.com/Consensys-Incorporated/teku/pull/2229)

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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [teku#5730](https://github.com/Consensys-Incorporated/teku/pull/5730), [teku#2934](https://github.com/Consensys-Incorporated/teku/pull/2934)

</details>


<a id="db_hot-073"></a>
<details>
<summary><b>db_hot-073</b> Fetch justified block from DB by root — <i>implemented · low · S · cpu</i></summary>

**Idea.** Load the justified block from the DB by its root instead of deriving it from block roots in a state.

**Impact.** None; justified block/state are resolved by root, never derived from a state's block_roots.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:6653`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6653) fork_choice.get_justified_block() reads the justified node from proto-array by root
- [`beacon_node/beacon_chain/src/beacon_fork_choice_store.rs:341-368`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_fork_choice_store.rs#L341-L368) set_justified_checkpoint keys by checkpoint root and loads the state by stored justified_state_root (balances cache first)

**Skeptic check.** Verified the justified block comes from proto-array by root and the justified state by its recorded state root. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#2172](https://github.com/OffchainLabs/prysm/pull/2172)

</details>


<a id="db_hot-074"></a>
<details>
<summary><b>db_hot-074</b> Resolve block slot without loading block or state — <i>implemented · medium · S · cpu, disk, latency</i></summary>

**Idea.** Answer root-to-slot queries (for example in state pruning) from fork choice, a slot index, a state summary or the block instead of decoding the full state, so callers that need only the slot do not load large objects.

**Impact.** None: slot lookups for pruning and the API use summaries, not full states.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3000`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3000) load_hot_state_summary gives the slot without loading the state
- [`beacon_node/store/src/hot_cold_store.rs:2992`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2992) load_cold_state_slot from ColdStateSummary
- [`beacon_node/http_api/src/state_id.rs:68`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L68) Root state id resolves the slot from the hot summary or cold summary
- [`beacon_node/beacon_chain/src/migrate.rs:537`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L537) prune_hot_db builds the DAG from summaries only

**Skeptic check.** Verified that the summary-based slot lookup covers pruning and API state_id. block_id root lookups load the blinded block (block_id.rs:118), which the idea allows.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#5246](https://github.com/OffchainLabs/prysm/pull/5246), [teku#10454](https://github.com/Consensys-Incorporated/teku/pull/10454), [prysm#16040](https://github.com/OffchainLabs/prysm/pull/16040), [lighthouse@182135b83](https://github.com/sigp/lighthouse/commit/182135b83229)

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


<a id="db_hot-076"></a>
<details>
<summary><b>db_hot-076</b> Clean up temporary hot states and their flags — <i>implemented · low · S · disk, startup</i></summary>

**Idea.** Clear the temporary flag on stored advanced pre-states correctly, delete a state's temporary flag whenever the state is deleted, and prune hot states older than the split slot by scanning hot state summaries. Advanced states and stale flags then do not accumulate on disk or need garbage collection at startup.

**Impact.** None: temporary flags no longer exist, and advanced and stale states are pruned from the summary DAG at each finalization.

**Best measured result.** "Garbage collecting 223069 temporary states" at startup (problem) (pr:lighthouse#6422)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/lib.rs:302`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/lib.rs#L302) BeaconStateTemporary column deprecated
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:455`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L455) advanced state written with put_state, no temporary flag
- [`beacon_node/beacon_chain/src/migrate.rs:664`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L664) every hot summary not descendant of finalized and not a required hdiff slot goes into states_to_prune
- [`beacon_node/beacon_chain/src/migrate.rs:790`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L790) DeleteState for each pruned state

**Skeptic check.** Verified that the temporary-state mechanism was removed and that prune_hot_db scans all hot summaries. The idea's goal (no accumulation, no startup GC) is met. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#6422](https://github.com/sigp/lighthouse/pull/6422), [lighthouse#5768](https://github.com/sigp/lighthouse/pull/5768)

</details>


<a id="db_hot-077"></a>
<details>
<summary><b>db_hot-077</b> Direct lookup for block at exact slot — <i>implemented · low · S · latency, disk</i></summary>

**Idea.** For a block at an exact slot, do a direct key lookup (plus an in-memory store check for non-finalized blocks) instead of a seek for the latest block at or before the slot.

**Impact.** None; exact-slot lookups are in-memory for recent slots and a keyed read for finalized slots.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:1050-1110`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1050-L1110) block_root_at_slot_skips_none: fast path reads head state block_roots (in-memory), else a two-element forwards iter over the slot-keyed BeaconBlockRoots column
- [`beacon_node/beacon_chain/src/beacon_chain.rs:944-956`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L944-L956) block_at_slot then fetches the block by root

**Skeptic check.** Confirmed the in-memory head-state fast path and keyed fallback (prev_slot..request_slot window, not a seek-to-latest scan). Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#7471](https://github.com/Consensys-Incorporated/teku/pull/7471), [prysm#4271](https://github.com/OffchainLabs/prysm/pull/4271)

</details>


<a id="db_hot-078"></a>
<details>
<summary><b>db_hot-078</b> Drop orphan block roots without states at startup — <i>n/a · low · S · startup, memory</i></summary>

**Idea.** At restart, delete stored block roots that have no matching state and do not load those blocks into memory.

**Impact.** Lighthouse does not load hot block roots into memory at startup, so orphan roots only cost disk until pruned by finalization migration.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_fork_choice_store.rs:212`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_fork_choice_store.rs#L212) - fork choice restored from persisted proto-array, not by loading all stored block roots into memory

**Sources.** [teku#1721](https://github.com/Consensys-Incorporated/teku/pull/1721)

</details>


<a id="db_hot-079"></a>
<details>
<summary><b>db_hot-079</b> Do not store payload-derived state separately — <i>implemented · low · S · disk</i></summary>

**Idea.** Do not persist a separate state for the post-payload step; regenerate it by replaying blocks, which reduces storage and regeneration work.

**Impact.** None; no separate post-payload state is persisted. Gloas-only.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/payload_envelope_verification/import.rs:293-312`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/import.rs#L293-L312) envelope import writes only data columns and StoreOp::PutPayloadEnvelope, no state
- [`beacon_node/beacon_chain/src/payload_envelope_verification/mod.rs:372`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/mod.rs#L372) load_snapshot_from_state_root uses the block post-state as pre-state

**Skeptic check.** Checked the envelope import ops: only the envelope and columns are written; the stale 'post-state' comment does not match the code. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#10564](https://github.com/Consensys-Incorporated/teku/pull/10564)

</details>


<a id="db_hot-080"></a>
<details>
<summary><b>db_hot-080</b> Avoid a global or redundant store lock — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Do not serialize unrelated DB operations on one global store mutex or an outer lock around an already thread-safe DB handle: remove it where atomicity is guaranteed elsewhere, or give small disk I/O paths their own lock so they do not wait behind large state writes.

**Impact.** None: no outer store lock serializes unrelated I/O; small writes are not queued behind a store-level lock.

**Best measured result.** state dump 420 ms p50 vs envelope 0.2-3.6 ms (contention avoided) (pr:caplin#25436)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:52`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L52) HotColdDB fields: hot_db/cold_db/blobs_db are plain handles, no global store mutex
- [`beacon_node/store/src/hot_cold_store.rs:74`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L74) only cache mutexes (block_cache, state_cache, historic_state_cache)
- [`beacon_node/store/src/database/redb_impl.rs:14`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/redb_impl.rs#L14) RwLock taken for read on reads and writes; write lock only for compaction (line 197)

**Skeptic check.** Searched store and beacon_chain for a transaction mutex or a global DB lock and found none. Any remaining serialization is inside the DB engine (LevelDB writer queue, redb single writer), which is not the redundant outer lock the idea targets.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@b3a94de08](https://github.com/sigp/lighthouse/commit/b3a94de086ae), [lighthouse#7311](https://github.com/sigp/lighthouse/pull/7311), [caplin#25436](https://github.com/erigontech/erigon/pull/25436)

</details>


<a id="db_hot-081"></a>
<details>
<summary><b>db_hot-081</b> Embed DB cursor wrapper by value — <i>n/a · low · cpu, memory</i></summary>

**Idea.** Store the cursor wrapper inline in the cursor struct instead of behind a pointer, saving one heap object and one indirection per cursor operation.

**Impact.** Go cursor-wrapper pointer indirection; Rust leveldb/redb wrappers have no equivalent heap object.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/database`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database)/

**Sources.** [caplin#23015](https://github.com/erigontech/erigon/pull/23015)

</details>


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

**Verdict history.** not (checked) → partial (refuted)

**Sources.** [ethlambda#179](https://github.com/lambdaclass/ethlambda/pull/179), [ethlambda#176](https://github.com/lambdaclass/ethlambda/pull/176), [ethlambda#175](https://github.com/lambdaclass/ethlambda/pull/175)

</details>


<a id="db_hot-083"></a>
<details>
<summary><b>db_hot-083</b> Keep few recent headers in DB, rest in snapshots — <i>n/a · low · disk</i></summary>

**Idea.** Keep only a few recent block headers in the hot DB and serve older ones from immutable snapshot files, limiting hot DB growth.

**Impact.** Caplin-specific snapshot (static file) architecture; Lighthouse prunes hot DB through finalization migration into the freezer instead.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:558`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L558) headers are part of full blocks in DBColumn::BeaconBlock; no snapshot-file layer

**Sources.** [caplin#8809](https://github.com/erigontech/erigon/pull/8809)

</details>


<a id="db_hot-084"></a>
<details>
<summary><b>db_hot-084</b> Prune hot states older than finalization — <i>implemented · medium · S · disk</i></summary>

**Idea.** When a new checkpoint finalizes, delete hot-DB states older than the finalized slot (including boundary states), optionally keeping only sparse periodic states, and enable this by default so state storage stays bounded.

**Impact.** None: hot state storage is bounded by finalization by default and keeps only sparse hierarchy states.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/migrate.rs:509`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L509) prune_hot_db runs on every finalization migration
- [`beacon_node/beacon_chain/src/migrate.rs:646`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L646) required_finalized_diff_state_slots keeps only sparse hdiff layer states
- [`beacon_node/beacon_chain/src/migrate.rs:664`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L664) everything else not descendant of the finalized checkpoint is pruned
- [`beacon_node/beacon_chain/src/migrate.rs:790`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L790) DeleteState batch

**Skeptic check.** Verified that pruning is unconditional on finalization and keeps only the hdiff grid points plus viable descendants. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#2034](https://github.com/OffchainLabs/prysm/pull/2034), [prysm#4139](https://github.com/OffchainLabs/prysm/pull/4139), [nimbus#1624](https://github.com/status-im/nimbus-eth2/pull/1624), [prysm#4082](https://github.com/OffchainLabs/prysm/pull/4082), [prysm#3856](https://github.com/OffchainLabs/prysm/pull/3856), [prysm#3824](https://github.com/OffchainLabs/prysm/pull/3824), [nimbus#191](https://github.com/status-im/nimbus-eth2/pull/191), [prysm#4204](https://github.com/OffchainLabs/prysm/pull/4204), [prysm#3918](https://github.com/OffchainLabs/prysm/pull/3918)

</details>


<a id="db_hot-085"></a>
<details>
<summary><b>db_hot-085</b> Optional pruning of historical states — <i>implemented · medium · S · disk</i></summary>

**Idea.** Make deletion of historical (cold) states not needed for the node's mode available, as a configurable option or an offline command, trading availability of old states for much less disk usage.

**Impact.** Nodes can drop all historic states offline and do not store new ones after; checkpoint-synced nodes never store them by default.

**Best measured result.** takes a few seconds max on mainnet (pr:lighthouse#4835)

**Evidence (Lighthouse @ 928b61e719).**

- [`database_manager/src/lib.rs:440-463`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/database_manager/src/lib.rs#L440-L463) prune-states (with --confirm) calls prune_historic_states
- [`beacon_node/store/src/hot_cold_store.rs:3471-3525`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3471-L3525) prune_historic_states sets state_upper_limit NO_RETAIN, deletes freezer state columns, compacts
- [`beacon_node/store/src/hot_cold_store.rs:3583-3611`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3583-L3611) migrate_database stores only cold state summaries below state_upper_limit afterwards
- [`beacon_node/store/src/hot_cold_store.rs:2776`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2776) checkpoint-synced nodes default to STATE_UPPER_LIMIT_NO_RETAIN

**Skeptic check.** Verified the offline command, the anchor change and that later migrations skip full cold states. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#2210](https://github.com/OffchainLabs/prysm/pull/2210), [lighthouse#4835](https://github.com/sigp/lighthouse/pull/4835)

</details>


<a id="db_hot-086"></a>
<details>
<summary><b>db_hot-086</b> Index finalized block roots — <i>implemented · low · S · cpu, disk</i></summary>

**Idea.** Maintain a DB index of finalized block roots so finality checks and lookups by root do not scan.

**Impact.** None; finality checks use the slot index, not a scan.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1219-1242`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1219-L1242) forwards_block_roots_iterator over slot-keyed DBColumn::BeaconBlockRoots
- [`beacon_node/store/src/hot_cold_store.rs:3577`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3577) finalized block roots written to BeaconBlockRoots on migration
- [`beacon_node/beacon_chain/src/beacon_chain.rs:631-646`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L631-L646) is_finalized_block checks finality via slot comparison plus a keyed slot-&gt;root lookup

**Skeptic check.** Index is slot-&gt;root rather than root-set, but is_finalized_block uses slot+root so no scan occurs; equivalent effect. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#3950](https://github.com/OffchainLabs/prysm/pull/3950)

</details>


<a id="db_hot-087"></a>
<details>
<summary><b>db_hot-087</b> Hot state-root to state index — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Keep a hot DB index from state root to stored state, pruned periodically, so states can be found by root without regeneration.

**Impact.** None; hot state-root index exists and is pruned at finalization.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3867`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3867) HotStateSummary keyed by state root
- [`beacon_node/store/src/hot_cold_store.rs:1870-1876`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1870-L1876) get_hot_state resolves by summary then diff/snapshot
- [`beacon_node/beacon_chain/src/migrate.rs:509-620`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L509-L620) prune_hot_db deletes summaries not descending from finalized

**Skeptic check.** Hot summaries keyed by state root plus hdiff/snapshot storage give lookup by root; pruning confirmed in migrate.rs. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#2389](https://github.com/Consensys-Incorporated/teku/pull/2389)

</details>


<a id="db_hot-088"></a>
<details>
<summary><b>db_hot-088</b> Hoist DB bucket lookup out of loops — <i>n/a · low · cpu</i></summary>

**Idea.** Look up or create the DB bucket handle once per call instead of once per item inside a loop.

**Impact.** bolt bucket handle lookup; Lighthouse uses column-prefixed keys in leveldb/redb, no per-call bucket creation.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/database/leveldb_impl.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/leveldb_impl.rs): column is a key prefix, no bucket handles

**Sources.** [prysm#8579](https://github.com/OffchainLabs/prysm/pull/8579)

</details>


<a id="db_hot-089"></a>
<details>
<summary><b>db_hot-089</b> Run metric column scans off the pruning path — <i>n/a · low · latency, disk</i></summary>

**Idea.** Run full O(N) column count scans used only for metrics on a separate low-priority task, not at the end of the pruning cycle, so pruning is not delayed by minutes.

**Impact.** Lighthouse does not run O(N) column-count scans for metrics, so there is nothing to move off the pruning path.

**Best measured result.** scans "can take minutes on large databases" (pr:teku#11171)

**Evidence (Lighthouse @ 928b61e719).**

- store/src/hot_cold_store.rs:456-506 store metrics set only in-memory gauges (caches, anchor info)
- beacon_chain/src/migrate.rs: no column count scans at end of pruning

**Sources.** [teku#11171](https://github.com/Consensys-Incorporated/teku/pull/11171)

</details>


<a id="db_hot-090"></a>
<details>
<summary><b>db_hot-090</b> More threads for storage query executor — <i>n/a · low · latency</i></summary>

**Idea.** Give the storage query executor enough threads that concurrent DB reads are not queued behind each other.

**Impact.** JVM executor pool for storage queries; Lighthouse reads run on the tokio blocking pool or caller threads, which is sized by the runtime.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/database`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database)/ no executor; DB calls run on spawn_blocking in beacon_chain

**Sources.** [teku#7474](https://github.com/Consensys-Incorporated/teku/pull/7474)

</details>


<a id="db_hot-091"></a>
<details>
<summary><b>db_hot-091</b> Dump chain in ascending order with rebase — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** When dumping or iterating many states, go in ascending slot order and rebase each state on the previous one, which is cheaper for tree-structured states; back the in-memory store with an ordered map.

**Impact.** None; test/debug path only.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:7840`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7840) chain dump calls beacon_state.rebase_on(&amp;prev) while iterating ascending
- [`beacon_node/store/src/memory_store.rs:9`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/memory_store.rs#L9) MemoryStore DBMap is a BTreeMap

**Skeptic check.** This is Lighthouse's own PR 4423 and both halves are present. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#4423](https://github.com/sigp/lighthouse/pull/4423)

</details>


<a id="db_hot-092"></a>
<details>
<summary><b>db_hot-092</b> Partial state getters and cached state hash — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Give callers getters for single state fields (validators, balances) and a cached state hash, so they do not clone or rehash the whole state.

**Impact.** Field accessors return references and state clone is O(1) with cached subtree hashes, so no whole-state copy or rehash.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:3070`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3070) update_tree_hash_cache incremental milhouse hashing
- [`consensus/types/src/state/beacon_state.rs:1087`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1087) canonical_root
- [`beacon_node/store/src/state_cache.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs) states cloned cheaply via structural sharing

**Skeptic check.** The Prysm idea targets full-state copies; Lighthouse's milhouse states give field references and incremental cached roots. Earlier verdict upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#2334](https://github.com/OffchainLabs/prysm/pull/2334)

</details>


<a id="db_hot-093"></a>
<details>
<summary><b>db_hot-093</b> Read only needed vote cache entries from DB — <i>n/a · low · disk</i></summary>

**Idea.** Keep the block vote cache outside the state and read or write only the entries for the block hashes involved, instead of the whole cache per block.

**Impact.** Lighthouse keeps no per-block vote cache in the state or DB; votes live in fork choice proto-array.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/persisted_fork_choice.rs:1`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/persisted_fork_choice.rs#L1) votes persisted in fork choice, no vote cache in state

**Sources.** [prysm#739](https://github.com/OffchainLabs/prysm/pull/739)

</details>


<a id="db_hot-094"></a>
<details>
<summary><b>db_hot-094</b> One persist task per arriving sidecar — <i>n/a · low · latency, disk</i></summary>

**Idea.** Spawn a persist task per data column sidecar as it arrives instead of one batched task for all, so sidecar writes do not wait on each other.

**Impact.** Columns are held in the DA cache and written in one op with the block import, there is no separate batched persist task to split.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:8407`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L8407) PutDataColumns store op at import
- [`beacon_node/store/src/hot_cold_store.rs:985`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L985) put_data_columns

**Sources.** [grandine#324](https://github.com/grandinetech/grandine/pull/324)

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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [prysm#8101](https://github.com/OffchainLabs/prysm/pull/8101), [prysm#11388](https://github.com/OffchainLabs/prysm/pull/11388)

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

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [nimbus#1860](https://github.com/status-im/nimbus-eth2/pull/1860), [nimbus#1720](https://github.com/status-im/nimbus-eth2/pull/1720)

</details>


<a id="db_hot-097"></a>
<details>
<summary><b>db_hot-097</b> Persist all fork-choice heads in DB — <i>n/a · low · startup, disk</i></summary>

**Idea.** Store every fork-choice DAG head (not only the canonical head) in the DB so restart does not rediscover side branches and stray block data is not left behind during non-finality.

**Impact.** Whole fork choice (all branches) is persisted and reloaded, and pruning uses the state summaries DAG, so there is no head set to rediscover.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/builder.rs:245`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L245) load_fork_choice restores whole proto-array
- [`beacon_node/beacon_chain/src/migrate.rs:537`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L537) prune uses summaries DAG

**Sources.** [nimbus#8590](https://github.com/status-im/nimbus-eth2/pull/8590)

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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [lighthouse@67fdb4a7f](https://github.com/sigp/lighthouse/commit/67fdb4a7fb42)

</details>


<a id="db_hot-099"></a>
<details>
<summary><b>db_hot-099</b> Persist deposit cache instead of refetching logs — <i>n/a · low · startup, sync</i></summary>

**Idea.** Store deposit containers in the DB and fill the deposit cache from them at startup instead of re-fetching deposit logs from the eth1 node.

**Impact.** Eth1 deposit log polling and deposit cache no longer exist in Lighthouse.

**Evidence (Lighthouse @ 928b61e719).**

- beacon_node/ls beacon_node shows no eth1 crate

**Sources.** [prysm#4384](https://github.com/OffchainLabs/prysm/pull/4384), [lodestar@a3d66d689](https://github.com/ChainSafe/lodestar/commit/a3d66d68923a)

</details>


<a id="db_hot-100"></a>
<details>
<summary><b>db_hot-100</b> Store EL-fetched payloads when not pruning — <i>n/a · low · bandwidth, latency, disk</i></summary>

**Idea.** When payload pruning is disabled, store execution payloads fetched from the EL in the DB so later requests do not download them again.

**Impact.** With prune_payloads=false the payload is already stored at import, so EL downloads only arise for blocks imported before disabling pruning; marginal.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/config.rs:117`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L117) prune_payloads default true
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1295`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1295) get_payload_for_header from EL

**Sources.** [lighthouse#3754](https://github.com/sigp/lighthouse/pull/3754)

</details>


<a id="db_hot-101"></a>
<details>
<summary><b>db_hot-101</b> Persist head, fork choice and eth1 data less often — <i>implemented · medium · S · disk, cpu, latency</i></summary>

**Idea.** Write chain metadata (head pointer, fork choice, op pool, eth1 cache, wall-clock time) only when it changes or at coarse points (epoch crossing, every N blocks, shutdown) instead of on every block, attestation or tick. Split large persisted objects so only the changed part is written.

**Impact.** Metadata writes are already coarse (per epoch/reorg/finality, shutdown). Fork choice is still written as one blob, but only per epoch, so splitting it would save little.

**Best measured result.** "committing less frequently to the database, which should help with contention" (pr:teku#1232)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:1564-1566`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1564-L1566) persist_fork_choice only on epoch transition or reorg
- [`beacon_node/beacon_chain/src/canonical_head.rs:1720`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1720) persist at finalization
- [`beacon_node/beacon_chain/src/beacon_chain.rs:8463-8466`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L8463-L8466) op pool, custody context, fork choice persisted on Drop
- [`beacon_node/beacon_chain/src/beacon_chain.rs:687`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L687) head persisted as genesis root only
- [`beacon_node/http_api/src/validator/mod.rs:1125`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L1125) custody context persisted only when custody changes

**Skeptic check.** Grepped all persist_* callers; none run per block or per attestation. The split-object part of the idea is not done but does not matter at this frequency.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#851](https://github.com/sigp/lighthouse/pull/851), [prysm#3669](https://github.com/OffchainLabs/prysm/pull/3669), [prysm#9764](https://github.com/OffchainLabs/prysm/pull/9764), [teku#1232](https://github.com/Consensys-Incorporated/teku/pull/1232)

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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [grandine@03a65e85e](https://github.com/grandinetech/grandine/commit/03a65e85e5cd), [grandine@c3b25ed8d](https://github.com/grandinetech/grandine/commit/c3b25ed8d112), [grandine@2242cea39](https://github.com/grandinetech/grandine/commit/2242cea393f3)

</details>


<a id="db_hot-103"></a>
<details>
<summary><b>db_hot-103</b> Preallocate slices for block root ranges — <i>not · low · S · memory, cpu</i></summary>

**Idea.** Preallocate collection capacity when collecting block roots over a slot range from the DB to avoid repeated reallocation.

**Gap in Lighthouse.** Lighthouse collects the backward iterator into a Vec with no size hint, but ranges are short (post-finalization only). In SimpleForwardsIterator constructors (forwards_iter_block_roots_using_state / _state_roots_) use Vec::with_capacity(end_state.slot() - start_slot + 1).

**Impact.** Saves a few reallocations on short ranges; negligible.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/forwards_iter.rs:41`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/forwards_iter.rs#L41) collect::&lt;Vec&lt;_&gt;&gt;() without capacity
- [`beacon_node/store/src/forwards_iter.rs:59`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/forwards_iter.rs#L59) same for state roots

**Sources.** [prysm#4540](https://github.com/OffchainLabs/prysm/pull/4540)

</details>


<a id="db_hot-104"></a>
<details>
<summary><b>db_hot-104</b> Store previous state root in hot summaries — <i>partial · low · S · cpu, memory, latency</i></summary>

**Idea.** Store the previous state root in each hot state summary so loading a state from disk needs no tree hashing; reading a few summaries is cheaper than building a tree hash cache.

**Gap in Lighthouse.** Hot replay (load_hot_state_using_replay -&gt; replay_blocks) gets no state-root iterator, so every skipped slot between replayed blocks and the advance to the target slot is tree-hashed. A reverse iterator over HotStateSummary.previous_state_root from the target state root could feed BlockReplayer::state_root_iter, as the cold path does. get_hot_state and get_advanced_hot_state also call update_tree_hash_cache after every disk load.

**Impact.** Small: with milhouse plus rebase_on_finalized, only the changed subtrees are hashed. The saving is on skip-slot replays and reorg state loads that miss the cache.

**Best measured result.** tree hash cache costs 1s+ CPU and 300MB+ RAM; summaries read &lt;250ms for 32 (pr:lighthouse#2954)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3867-3873`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3867-L3873) HotStateSummary.previous_state_root exists
- [`beacon_node/store/src/hot_cold_store.rs:3743-3860`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3743-L3860) used only by get_ancestor_state_root
- [`beacon_node/store/src/hot_cold_store.rs:2078-2084`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2078-L2084) load_hot_state_using_replay passes no_state_root_iter()
- [`consensus/state_processing/src/block_replayer.rs:176-208`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/block_replayer.rs#L176-L208) without an iterator, skipped-slot roots are computed with update_tree_hash_cache
- [`beacon_node/store/src/hot_cold_store.rs:2381-2394`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2381-L2394) cold replay does supply a state-root iterator
- [`beacon_node/store/src/hot_cold_store.rs:2016-2020`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2016-L2020) rebase_on_finalized limits the hashing cost

**Skeptic check.** The field exists but is used only for ancestor lookups. Hot replay still hashes skipped slots, so the goal of loading from disk with no hashing is not met. Source PR #2954 was closed unmerged.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lighthouse#2954](https://github.com/sigp/lighthouse/pull/2954)

</details>


<a id="db_hot-105"></a>
<details>
<summary><b>db_hot-105</b> Prune hot DB via state summaries DAG — <i>implemented · low · S · disk</i></summary>

**Idea.** Prune the hot DB without a separately persisted head tracker: after migrating the finalized chain, load all state summaries and delete every summary not descending from finalized, so pruning cannot drift from fork choice.

**Impact.** None; head tracker removed, pruning driven by summaries DAG.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/migrate.rs:509`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L509) prune_hot_db
- [`beacon_node/beacon_chain/src/migrate.rs:537-559`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L537-L559) load_hot_state_summaries into StateSummariesDAG
- [`beacon_node/beacon_chain/src/migrate.rs:590-600`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L590-L600) keeps only descendants_of(new_finalized_state_root)

**Skeptic check.** Lighthouse's own PRs 6744/7080; no HeadTracker type remains in beacon_chain/src. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#6744](https://github.com/sigp/lighthouse/pull/6744), [lighthouse#7080](https://github.com/sigp/lighthouse/pull/7080)

</details>


<a id="db_hot-106"></a>
<details>
<summary><b>db_hot-106</b> Prune orphaned execution payload envelopes — <i>implemented · low · S · disk</i></summary>

**Idea.** On each finalization, delete hot-DB execution payload envelopes whose block is no longer in fork choice, since the finalized-chain walk never reaches them.

**Impact.** Envelopes of abandoned forks are removed at each finalization together with their blocks.

**Best measured result.** Observed 17 stale hot envelopes on a devnet node (pr:lodestar#10206)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/migrate.rs:707-738`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L707-L738) blocks_to_prune = summaries-DAG blocks not descending from finalized checkpoint
- [`beacon_node/beacon_chain/src/migrate.rs:777-781`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L777-L781) DeletePayloadWithSummary for each pruned block
- [`beacon_node/beacon_chain/src/migrate.rs:830-846`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L830-L846) also deletes envelopes of canonical blocks finalized EMPTY
- [`beacon_node/store/src/hot_cold_store.rs:1357-1366`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1357-L1366) deletes PayloadSummary and PayloadBody

**Skeptic check.** Verified the prune set covers abandoned-fork blocks and that the envelope columns are deleted with them. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#10206](https://github.com/ChainSafe/lodestar/pull/10206)

</details>


<a id="db_hot-107"></a>
<details>
<summary><b>db_hot-107</b> Prune unreachable data after head rewind — <i>n/a · low · disk</i></summary>

**Idea.** When the stored head cannot be reconstructed at startup and the node rewinds, delete blocks and data between the old head pointer and the resolved head.

**Impact.** Head is recomputed from persisted fork choice; Lighthouse has no startup rewind of the stored head.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/builder.rs:245`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L245) load fork choice, head via get_head at :771

**Sources.** [nimbus#8584](https://github.com/status-im/nimbus-eth2/pull/8584)

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

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [nimbus@777b3f4e2](https://github.com/status-im/nimbus-eth2/commit/777b3f4e29c2), [grandine@d556ebf3d](https://github.com/grandinetech/grandine/commit/d556ebf3d9cd)

</details>


<a id="db_hot-109"></a>
<details>
<summary><b>db_hot-109</b> Write intermediate states to DB as temporary — <i>implemented · low · S · memory</i></summary>

**Idea.** Write intermediate states created during block processing directly to the hot DB marked temporary, clear the mark on success, and garbage-collect leftovers at startup, so they need not be held in memory.

**Impact.** Intermediate states go to disk right away and are not held in memory. Leftovers from failed imports are cleared by finalization pruning instead of a temporary flag.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1617-1634`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1617-L1634) skip-slot states stored with store_hot_state immediately
- [`beacon_node/store/src/lib.rs:300-305`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/lib.rs#L300-L305) BeaconStateTemporary deprecated
- [`beacon_node/beacon_chain/src/migrate.rs:700-703`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L700-L703) leftover hot states pruned on finalization

**Skeptic check.** The mechanism changed: no temporary mark, and garbage collection happens at finalization, not at startup. The effect the idea wants is achieved.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#1798](https://github.com/sigp/lighthouse/pull/1798)

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


<a id="db_hot-111"></a>
<details>
<summary><b>db_hot-111</b> Prune invalid-block blacklist at finality — <i>n/a · low · S · disk, memory</i></summary>

**Idea.** Delete stored blacklisted/invalid block hashes once finality makes them irrelevant so the set does not grow without bound.

**Impact.** Lighthouse keeps no persistent invalid-block set; invalid blocks live in proto_array, which is pruned at finalization.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs): fork choice head handling; no persistent blacklist column in store/src/lib.rs DBColumn

**Sources.** [prysm#2411](https://github.com/OffchainLabs/prysm/pull/2411), [prysm#2694](https://github.com/OffchainLabs/prysm/pull/2694)

</details>


<a id="db_hot-112"></a>
<details>
<summary><b>db_hot-112</b> Incremental pruning of per-block vote cache — <i>n/a · low · S · disk</i></summary>

**Idea.** Run an incremental background cleanup that deletes per-block vote/attestation cache entries for finalized blocks, resuming from the last cleaned slot.

**Impact.** No per-block vote cache is stored in the DB, so nothing grows to prune.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/lib.rs:329`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/lib.rs#L329) DBColumn list has no per-block vote cache; fork choice votes are in-memory proto_array

**Sources.** [prysm#972](https://github.com/OffchainLabs/prysm/pull/972)

</details>


<a id="db_hot-113"></a>
<details>
<summary><b>db_hot-113</b> Prune live-chain index to finalized slot — <i>n/a · low · S · disk, cpu</i></summary>

**Idea.** Prune the slot-to-block live-chain index to the finalized block's slot so it stops growing per block and full scans for head and import stay small.

**Impact.** Lighthouse has no slot-to-block live-chain DB index; proto_array nodes are pruned at finality.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs): fork choice proto_array prune on finalization

**Sources.** [ethlambda#627](https://github.com/lambdaclass/ethlambda/pull/627), [ethlambda#83](https://github.com/lambdaclass/ethlambda/pull/83)

</details>


<a id="db_hot-114"></a>
<details>
<summary><b>db_hot-114</b> Prune validator pubkey-to-index table — <i>n/a · low · S · disk</i></summary>

**Idea.** Prune the stored validator pubkey-to-index table so it does not grow without bound.

**Impact.** Pubkey cache is append-only and bounded by registry size (validators never leave the registry), about 1M entries; pruning gives nothing.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:55`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L55) load_from_store iterates DatabasePubkey by index

**Sources.** [nimbus#2576](https://github.com/status-im/nimbus-eth2/pull/2576)

</details>


<a id="db_hot-115"></a>
<details>
<summary><b>db_hot-115</b> Prune slasher history outside window — <i>implemented · low · S · disk</i></summary>

**Idea.** Delete slasher attestation and proposal records older than the history window so the slasher DB stays bounded.

**Impact.** None; slasher DB bounded by history_length (min/max target arrays are circular by design).

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/database.rs:740-748`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L740-L748) try_prune prunes proposers and indexed attestations
- [`slasher/src/database.rs:750-780`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L750-L780) prune_proposers delete_while below min_slot
- [`slasher/src/database.rs:782-825`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L782-L825) prune_indexed_attestations deletes ids, attestations and root cache entries below min_epoch
- [`slasher/service/src/service.rs:137`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/service/src/service.rs#L137) periodic prune_database

**Skeptic check.** Pruning of proposals and attestation records outside the window confirmed and runs periodically. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#8591](https://github.com/OffchainLabs/prysm/pull/8591)

</details>


<a id="db_hot-116"></a>
<details>
<summary><b>db_hot-116</b> Bound slashing-protection attestation history — <i>implemented · low · S · disk</i></summary>

**Idea.** In the validator slashing-protection DB keep only attestations at or above the lowest signed epoch watermark, since anything below is rejected anyway.

**Impact.** SQLite slashing-protection DB kept to about one epoch of history per validator.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/slashing_protection/src/slashing_database.rs:1069`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L1069) prune_signed_attestations deletes target_epoch &lt; new_min_target, keeping MAX row
- [`validator_client/slashing_protection/src/slashing_database.rs:1029`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L1029) prune_signed_blocks
- [`validator_client/lighthouse_validator_store/src/lib.rs:60`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/lighthouse_validator_store/src/lib.rs#L60) SLASHING_PROTECTION_HISTORY_EPOCHS = 1
- [`validator_client/lighthouse_validator_store/src/lib.rs:1395-1413`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/lighthouse_validator_store/src/lib.rs#L1395-L1413) prune_slashing_protection_db

**Skeptic check.** Verified the DELETE queries and the per-epoch prune with a 1-epoch history; this is the low-watermark bound the idea describes. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#8590](https://github.com/OffchainLabs/prysm/pull/8590)

</details>


<a id="db_hot-117"></a>
<details>
<summary><b>db_hot-117</b> Store validator pubkey cache inside the DB — <i>implemented · low · S · startup, disk</i></summary>

**Idea.** Keep the validator pubkey cache in the main DB instead of a separate file so it is loaded and appended atomically with the rest of the store.

**Impact.** Pubkey cache lives in the hot DB and is written atomically with block import.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:55-70`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L55-L70) load_from_store reads DatabasePubkey items from the main store
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:87-132`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L87-L132) import_new_pubkeys returns StoreOp::KeyValueOp
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4485-4499`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4485-L4499) pubkey ops start the block-import ops vec
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4756`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4756) do_atomically_with_block_and_blobs_cache(ops) commits them with the block

**Skeptic check.** Confirmed that new pubkey ops are part of the same atomic batch as PutBlock/PutState in block import. This is Lighthouse's own PR 2234, so the earlier verdict holds.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#2234](https://github.com/sigp/lighthouse/pull/2234)

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


<a id="db_hot-119"></a>
<details>
<summary><b>db_hot-119</b> Slot-ordered range scans instead of per-key lookups — <i>partial · low · S · disk, cpu</i></summary>

**Idea.** Iterate slot-ordered DB keys with range filters (gt/lt/reverse/limit, streaming) instead of issuing one lookup per slot or scanning a hash-keyed index, for custody scans, pruning and queries.

**Gap in Lighthouse.** try_prune_blobs does 128 key_exists point lookups per Fulu block via get_all_data_column_keys, where it could do one prefix range scan (get_data_column_keys). It also walks blocks backwards by parent root with get_blinded_block, where it could scan the slot-keyed BeaconBlockRoots range in the freezer. get_data_column_keys uses iter_column_from, which reads column values when it needs only keys; iter_column_keys_from would avoid that.

**Impact.** Fewer DB reads in blob/column pruning (128 lookups per block become 1 seek). Pruning runs in the background, so this is a modest gain.

**Best measured result.** Average ~400 block queries per call before (pr:teku#9797)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/forwards_iter.rs:117`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/forwards_iter.rs#L117) freezer roots scanned by slot-ordered keys
- [`beacon_node/store/src/hot_cold_store.rs:3366-3410`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3366-L3410) try_prune_blobs walks ParentRootBlockIterator (one block load per block) and calls key_exists for every column index
- [`beacon_node/store/src/hot_cold_store.rs:2672-2676`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2672-L2676) get_all_data_column_keys builds all 128 keys
- [`beacon_node/store/src/hot_cold_store.rs:2657-2665`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2657-L2665) get_data_column_keys prefix scan exists but is not used by pruning (and reads values too)

**Skeptic check.** Freezer range queries do use slot-ordered keys, but the pruning path uses per-key lookups, and the code comment itself says so. Earlier evidence cited only the freezer iterators.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [teku#9797](https://github.com/Consensys-Incorporated/teku/pull/9797), [teku#6912](https://github.com/Consensys-Incorporated/teku/pull/6912), [lodestar#858](https://github.com/ChainSafe/lodestar/pull/858), [prysm#4303](https://github.com/OffchainLabs/prysm/pull/4303)

</details>


<a id="db_hot-120"></a>
<details>
<summary><b>db_hot-120</b> Move blocks hot-to-cold as raw bytes — <i>n/a · medium · cpu, latency</i></summary>

**Idea.** When migrating finalized blocks from the hot to the cold/finalized DB, copy the raw stored bytes keyed by the known root (use the DB key as root) instead of deserializing, re-hashing and re-serializing each block.

**Best measured result.** Spike: doUpdate took 1522 ms (finalized 306 ms, hot 1216 ms) (pr:teku#7638)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3532`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3532) migrate_database only writes BeaconBlockRoots slot-&gt;root entries
- [`beacon_node/store/src/lib.rs:257`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/lib.rs#L257) single BeaconBlock column keyed by root

**Sources.** [teku#7672](https://github.com/Consensys-Incorporated/teku/pull/7672), [teku#7638](https://github.com/Consensys-Incorporated/teku/pull/7638), [lodestar@968f18473](https://github.com/ChainSafe/lodestar/commit/968f184732db)

</details>


<a id="db_hot-121"></a>
<details>
<summary><b>db_hot-121</b> Take block root from DB key on load — <i>n/a · low · S · cpu, startup</i></summary>

**Idea.** When decoding blocks loaded from the DB, set the block root from the storage key instead of recomputing hash_tree_root.

**Impact.** Lighthouse APIs take the root as an argument and do not recompute hash_tree_root after load, so there is no rehash to avoid.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:676`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L676) get_block_with decodes bytes only; callers pass block_root explicitly (e.g. store/src/iter.rs:188)
- SignedBeaconBlock has no cached root; no canonical_root() on loaded blocks in these paths

**Sources.** [nimbus#1572](https://github.com/status-im/nimbus-eth2/pull/1572)

</details>


<a id="db_hot-122"></a>
<details>
<summary><b>db_hot-122</b> Reuse computed block root when saving blocks — <i>implemented · low · S · cpu</i></summary>

**Idea.** Carry the already computed block root (a wrapper caching hash_tree_root) into the block save path instead of re-hashing the block there.

**Impact.** None: the block root computed at verification is reused for storage.

**Best measured result.** FullBlock SaveBlock ROBlock -99.99% time, allocs 2069 -&gt; 1; SaveBlocks/64 -22.96% time, -38% B/op (pr:prysm#16300)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:507-521`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L507-L521) put_block takes block_root from the caller
- [`beacon_node/store/src/hot_cold_store.rs:527-545`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L527-L545) block_as_kv_store_ops keys by the given root, with no hashing

**Skeptic check.** No hash_tree_root on the save path. Earlier verdict upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#16300](https://github.com/OffchainLabs/prysm/pull/16300)

</details>


<a id="db_hot-123"></a>
<details>
<summary><b>db_hot-123</b> Readdir-based pruning of bucketed sidecar files — <i>n/a · low · cpu, disk</i></summary>

**Idea.** Prune bucketed on-disk sidecar stores by listing the bucket directories that exist instead of iterating every bucket index from slot 0 on each call, avoiding thousands of no-op remove syscalls per slot.

**Gap in Lighthouse.** Lighthouse has no bucketed sidecar files; blobs/columns live in the KV store keyed by root and pruned in try_prune_blobs.

**Impact.** No equivalent cost exists.

**Best measured result.** previously (head-keep)/10,000 RemoveAll syscalls every slot (pr:caplin#23451)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3277`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3277) try_prune_blobs, KV-based

**Sources.** [caplin#23451](https://github.com/erigontech/erigon/pull/23451)

</details>


<a id="db_hot-124"></a>
<details>
<summary><b>db_hot-124</b> Open redb with quick repair — <i>not · medium · S · startup</i></summary>

**Idea.** Open redb databases (store and slasher) with the quick-repair option so startup after an unclean shutdown does not re-read the whole DB to verify it.

**Gap in Lighthouse.** Call tx.set_quick_repair(true) on every write transaction in the beacon store and slasher redb backends (in redb 2.6.4 it is a per-transaction flag, not an open option). Upstream PR #10452 does this and is still OPEN.

**Impact.** Near-instant restart after an unclean shutdown on nodes that use the non-default redb backend or the redb slasher, instead of a full walk of the DB to verify checksums; commits get slightly slower (2-phase commit).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/database/redb_impl.rs:30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/redb_impl.rs#L30) redb::Database::create(db_file), no Builder or repair options
- [`beacon_node/store/src/database/redb_impl.rs:73`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/redb_impl.rs#L73),146,157,277,297 begin_write() with no set_quick_repair call
- [`slasher/src/database/redb_impl.rs:46`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database/redb_impl.rs#L46) redb::Database::create(db_path)
- [`slasher/src/database/redb_impl.rs:83`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database/redb_impl.rs#L83),98 begin_write() with no set_quick_repair call
- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/redb-2.6.4/src/transactions.rs:1618-1630 set_quick_repair is per-transaction and defaults to disabled
- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/redb-2.6.4/src/db.rs:1050-1063 redb only sets quick_repair internally for its own allocator-state commit

**Verdict history.** not (checked) → not (refuted)

**Sources.** [lighthouse#10452](https://github.com/sigp/lighthouse/pull/10452)

</details>


<a id="db_hot-125"></a>
<details>
<summary><b>db_hot-125</b> Drop DB writes and indexes nobody reads — <i>partial · low · S · disk, cpu</i></summary>

**Idea.** Remove persisted variables and secondary indexes (e.g. sampling progress, blob versioned hash index) that no query path needs, saving a write per item and the pruning work for it.

**Gap in Lighthouse.** Lighthouse has no sampling-progress var or blob versioned-hash index; the only per-block write nobody reads outside finalized checkpoints is the light client sync-committee branch (see db_hot-132). A full audit of other unread columns was not done.

**Impact.** Saves at most a small write per block; gain is marginal.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/light_client_server_cache.rs:118`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_server_cache.rs#L118) store_sync_committee_branch on every attested block

**Sources.** [teku#10045](https://github.com/Consensys-Incorporated/teku/pull/10045), [teku#9964](https://github.com/Consensys-Incorporated/teku/pull/9964), [lodestar@0f4156747](https://github.com/ChainSafe/lodestar/commit/0f4156747a81), [lodestar@77346889d](https://github.com/ChainSafe/lodestar/commit/77346889dc2d), [nimbus#1493](https://github.com/status-im/nimbus-eth2/pull/1493)

</details>


<a id="db_hot-126"></a>
<details>
<summary><b>db_hot-126</b> Avoid blinded-block storage layout — <i>n/a · low · S · latency, disk</i></summary>

**Idea.** Teku found storing blinded blocks (payload separated) slower than full blocks and dropped it, managing size by block pruning instead; check whether the blinded layout costs read performance.

**Impact.** Lighthouse deliberately stores blinded blocks with payloads in a separate column; the Teku finding is a design-level tradeoff and changing it would be a storage redesign. Idea is only a check, no change implied.

**Best measured result.** PR states it showed worse performance (pr:teku#6617)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:533`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L533) blocks are split into blinded block plus separate payload and stored blinded

**Sources.** [teku#6617](https://github.com/Consensys-Incorporated/teku/pull/6617)

</details>


<a id="db_hot-127"></a>
<details>
<summary><b>db_hot-127</b> Find highest block at or below slot quickly — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Answer 'highest block at or below slot' (e.g. replay base lookup) by seeking a slot index to the target and walking backwards, or with a per-slot bitfield, instead of scanning forward or keeping boundary-root bookkeeping.

**Impact.** Slot-to-block-root lookup is already O(1) in the cold DB and a backwards parent walk in the hot DB.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3076-3091`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3076-L3091) store_frozen_block_root_at_skip_slots writes a root for every slot, skipped slots pointing at the prior block
- [`beacon_node/store/src/hot_cold_store.rs:3096-3102`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3096-L3102) get_cold_block_root point lookup by slot
- [`beacon_node/store/src/hot_cold_store.rs:2514-2549`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2514-L2549) load_blocks_to_replay walks parent roots backwards from the end block
- [`beacon_node/store/src/hot_cold_store.rs:2482`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2482) replay base comes from the hdiff storage strategy (ReplayFrom), not a scan

**Skeptic check.** Confirmed: the cold DB keeps a dense per-slot root index, so 'highest block at or below slot' is a single get; hot replay walks backwards from the target. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#10772](https://github.com/OffchainLabs/prysm/pull/10772), [prysm#5182](https://github.com/OffchainLabs/prysm/pull/5182), [prysm#5230](https://github.com/OffchainLabs/prysm/pull/5230), [prysm#5192](https://github.com/OffchainLabs/prysm/pull/5192), [prysm#5195](https://github.com/OffchainLabs/prysm/pull/5195), [prysm#5213](https://github.com/OffchainLabs/prysm/pull/5213)

</details>


<a id="db_hot-128"></a>
<details>
<summary><b>db_hot-128</b> Do not denormalize slasher attestation records — <i>implemented · low · S · disk</i></summary>

**Idea.** Store slasher attestation records once per signing root instead of copying full records per validator and epoch, which blows storage up to TB scale.

**Impact.** Per-validator records are compact ids; the full attestation is stored once.

**Best measured result.** Attestation records took about 1.2 TB on Prater (pr:prysm#9085)

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/database.rs:35`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L35) ATTESTERS_DB maps (target_epoch, validator_index) to CompactAttesterRecord (an id)
- [`slasher/src/database.rs:42`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L42) INDEXED_ATTESTATION_DB stores each IndexedAttestation once by id
- [`slasher/src/database.rs:44`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L44) INDEXED_ATTESTATION_ID_DB (target_epoch, hash) -&gt; id dedups
- [`slasher/src/database.rs:170`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L170) IndexedAttestationIdKey

**Skeptic check.** Verified the slasher schema: full attestations are stored once and per-validator rows hold only a compact id. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#9085](https://github.com/OffchainLabs/prysm/pull/9085)

</details>


<a id="db_hot-129"></a>
<details>
<summary><b>db_hot-129</b> Avoid memory-hungry DB format — <i>n/a · medium · memory, sync</i></summary>

**Idea.** A newer DB storage format made process memory grow significantly, slowing sync and causing OOM; check DB format choices for native memory growth.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/database/interface.rs:1`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/interface.rs#L1) backend is leveldb or redb, selected by feature
- [`beacon_node/store/src/database/leveldb_impl.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/leveldb_impl.rs) no format-specific cache settings found

**Sources.** [teku#3009](https://github.com/Consensys-Incorporated/teku/pull/3009)

</details>


<a id="db_hot-130"></a>
<details>
<summary><b>db_hot-130</b> SQLite kv table with rowid for fast deletes — <i>n/a · low · disk, cpu</i></summary>

**Idea.** Create SQLite key-value tables with an integer rowid (not WITHOUT ROWID) so deletes of large blobs during pruning and reorgs are fast.

**Gap in Lighthouse.** Lighthouse has no SQLite backend.

**Impact.** No equivalent cost in Lighthouse.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/database`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database)/ has only leveldb_impl.rs and redb_impl.rs

**Sources.** [nimbus@2c257438a](https://github.com/status-im/nimbus-eth2/commit/2c257438a03c), [nimbus#2561](https://github.com/status-im/nimbus-eth2/pull/2561)

</details>


<a id="db_hot-131"></a>
<details>
<summary><b>db_hot-131</b> Uncorrelated pruning query — <i>n/a · low · cpu, disk</i></summary>

**Idea.** Write DB pruning as delete-everything-except-keep-set (rowid NOT IN, index-backed max per key) instead of correlated subqueries that scan.

**Gap in Lighthouse.** Lighthouse has no SQL pruning queries.

**Impact.** No equivalent cost in Lighthouse.

**Best measured result.** Query plans show scans removed; screenshot of slow pruning on Pyrmont (pr:nimbus#2554)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/database`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database)/ has only leveldb_impl.rs and redb_impl.rs

**Sources.** [nimbus#2554](https://github.com/status-im/nimbus-eth2/pull/2554)

</details>


<a id="db_hot-132"></a>
<details>
<summary><b>db_hot-132</b> Save light client bootstraps on finalization only — <i>partial · low · S · disk</i></summary>

**Idea.** Store light client bootstrap data only for finalized checkpoint blocks instead of every imported block.

**Gap in Lighthouse.** Lighthouse persists the current-sync-committee branch (small merkle proof) for every attested block, not just finalized checkpoint blocks, and has no pruning for it. Change recompute_and_cache_updates to store it only for finalized checkpoint blocks, or prune non-finalized ones.

**Impact.** One small KV write per block (and growing stored data) removed on default nodes; negligible CPU, small disk saving.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/light_client_server_cache.rs:118`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_server_cache.rs#L118) stores the branch for every attested block
- light_client_server_cache.rs:418 bootstrap read only works for blocks with a stored branch
- [`beacon_node/beacon_chain/src/chain_config.rs:174`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/chain_config.rs#L174) light client server enabled by default

**Sources.** [prysm#15497](https://github.com/OffchainLabs/prysm/pull/15497)

</details>


<a id="db_hot-133"></a>
<details>
<summary><b>db_hot-133</b> Secondary index buckets for attestation filters — <i>n/a · low · cpu, disk</i></summary>

**Idea.** Maintain secondary index buckets (e.g. by parent root, epoch) mapping to data roots and intersect them to answer filtered queries instead of scanning all keys and values.

**Gap in Lighthouse.** Lighthouse's op pool and naive aggregation pool are in-memory maps keyed by data root, not DB buckets with filtered queries.

**Impact.** No equivalent cost in Lighthouse.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/lib.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs) in-memory pools

**Sources.** [prysm#3202](https://github.com/OffchainLabs/prysm/pull/3202)

</details>


<a id="db_hot-134"></a>
<details>
<summary><b>db_hot-134</b> Separate DB file for slasher — <i>implemented · low · S · disk, latency</i></summary>

**Idea.** Keep slasher data in its own database file so its heavy write load does not contend with the beacon node DB.

**Impact.** Slasher write load isolated from the hot/cold beacon DB.

**Best measured result.** slasher has significant pressure on the beacon node's database (pr:prysm#8749)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/src/config.rs:667-673`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/config.rs#L667-L673) slasher_dir defaults to data_dir/slasher_db, separate from chain DB
- [`slasher/src/database.rs:299`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L299) slasher opens its own environment

**Skeptic check.** Slasher uses its own DB environment in its own directory, with a separate backend (MDBX/LMDB/redb) from the beacon store. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#8749](https://github.com/OffchainLabs/prysm/pull/8749)

</details>


<a id="db_hot-135"></a>
<details>
<summary><b>db_hot-135</b> Single atomic batch for puts and deletes — <i>implemented · low · S · disk, latency</i></summary>

**Idea.** Coalesce puts and deletes for a store into one atomic write batch instead of separate put and delete batches.

**Impact.** Puts and deletes for one store already commit in one atomic batch.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/database/leveldb_impl.rs:143-168`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/leveldb_impl.rs#L143-L168) do_atomically builds one Writebatch with both put and delete
- [`beacon_node/store/src/database/redb_impl.rs:155`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/redb_impl.rs#L155) one write transaction for mixed ops
- [`beacon_node/store/src/hot_cold_store.rs:1291`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1291) StoreOp converted to a mixed KeyValueStoreOp vec

**Skeptic check.** Verified that the leveldb do_atomically loop puts PutKeyValue and DeleteKey into one Writebatch and does one write. Blobs go to a separate DB, but this idea is about a single store, so that does not change the verdict.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#8268](https://github.com/ChainSafe/lodestar/pull/8268)

</details>


<a id="db_hot-136"></a>
<details>
<summary><b>db_hot-136</b> Persist state once per epoch transition — <i>n/a · low · disk, cpu</i></summary>

**Idea.** Apply all per-validator changes in memory during epoch processing and persist the state once at the end instead of writing per validator.

**Impact.** Lighthouse has no per-validator DB writes in epoch processing; state is held in memory (milhouse) and stored once.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1661`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1661) states stored whole/diff once per state, not per validator

**Sources.** [prysm#367](https://github.com/OffchainLabs/prysm/pull/367), [prysm#2028](https://github.com/OffchainLabs/prysm/pull/2028)

</details>


<a id="db_hot-137"></a>
<details>
<summary><b>db_hot-137</b> Run DB migration in one transaction — <i>n/a · low · startup</i></summary>

**Idea.** Run one-time DB migrations inside a single transaction instead of per-row commits to cut first-start time.

**Impact.** Lighthouse schema migrations use KV batches, not per-row SQL commits.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/database/leveldb_impl.rs:143`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/leveldb_impl.rs#L143) LevelDB/redb, no SQLite row migrations

**Sources.** [nimbus@5974fb0e7](https://github.com/status-im/nimbus-eth2/commit/5974fb0e7d32), [nimbus#2632](https://github.com/status-im/nimbus-eth2/pull/2632)

</details>


<a id="db_hot-138"></a>
<details>
<summary><b>db_hot-138</b> Use plain update transactions instead of bolt Batch — <i>n/a · low · memory</i></summary>

**Idea.** Replace bolt Batch calls (e.g. state deletes) with a single Update transaction, because Batch dominated heap usage.

**Impact.** Bolt Batch is Go/bolt specific; Lighthouse writes use a single write batch/tx.

**Best measured result.** Heap flame graph showed bolt.Batch dominating memory (pr:prysm#4763)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/database/redb_impl.rs:155`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/redb_impl.rs#L155) redb/leveldb, no bolt

**Sources.** [prysm#4755](https://github.com/OffchainLabs/prysm/pull/4755), [prysm#4763](https://github.com/OffchainLabs/prysm/pull/4763), [prysm#4775](https://github.com/OffchainLabs/prysm/pull/4775)

</details>


<a id="db_hot-139"></a>
<details>
<summary><b>db_hot-139</b> Skip BLS checks when replaying stored deposits — <i>n/a · low · cpu, startup</i></summary>

**Idea.** When replaying stored deposits at startup, skip deposit-signature verification for deposits already known valid, and read DB rows as borrowed slices instead of copying.

**Impact.** Lighthouse no longer has an eth1 deposit cache to replay at startup.

**Evidence (Lighthouse @ 928b61e719).**

- repo grep: no deposit_cache/DepositCache outside state_processing metrics; beacon_node has no eth1 crate

**Sources.** [nimbus#2060](https://github.com/status-im/nimbus-eth2/pull/2060)

</details>


<a id="db_hot-140"></a>
<details>
<summary><b>db_hot-140</b> Do not recreate empty temporary block DB — <i>n/a · low · disk, cpu</i></summary>

**Idea.** For a temporary block-collector DB at chain tip, do not drop and reopen it on every flush: return early when empty, clear small ones in place, drop only when large.

**Impact.** Lighthouse has no temporary block-collector DB recreated every slot.

**Best measured result.** Previously dropped DB dir every 12s even if empty (pr:caplin#22428)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1459`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1459) blocks written directly, no temporary collector DB

**Sources.** [caplin#22428](https://github.com/erigontech/erigon/pull/22428)

</details>


<a id="db_hot-141"></a>
<details>
<summary><b>db_hot-141</b> Skip attestation DB writes on non-archival nodes — <i>implemented · low · S · disk</i></summary>

**Idea.** Persist individual attestations to the DB only on archival nodes.

**Impact.** No per-attestation DB writes on any node, so there is no cost to save.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2605`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2605) unaggregated attestations go only to the in-memory naive aggregation pool
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5023`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5023) import_block_observe_attestations is in-memory only

**Skeptic check.** Lighthouse has no DB column for individual attestations; they stay in in-memory pools (the op pool is persisted only on shutdown). The effect is the same as or better than the idea.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#4776](https://github.com/OffchainLabs/prysm/pull/4776)

</details>


<a id="db_hot-142"></a>
<details>
<summary><b>db_hot-142</b> Start from stored hot states without block replay — <i>implemented · low · S · startup</i></summary>

**Idea.** Offer a startup mode that loads stored hot states directly instead of replaying blocks from the finalized state.

**Impact.** Restart does not replay blocks from finalization; fork choice and the head state are loaded from disk.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/builder.rs:783-786`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L783-L786) get_advanced_hot_state loads the head state from the DB at startup
- [`beacon_node/store/src/hot_cold_store.rs:1949`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1949) load_hot_state loads a snapshot/diff and replays only from the nearest layer
- [`beacon_node/client/src/builder.rs:290-305`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L290-L305) an existing DB always resumes with ClientGenesis::FromStore

**Skeptic check.** Verified that the restart path resumes from the stored fork choice and the stored hot head state, with no replay of all blocks from the finalized state. The earlier verdict was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#2617](https://github.com/Consensys-Incorporated/teku/pull/2617)

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

**Verdict history.** not (checked) → partial (refuted)

**Sources.** [grandine@40d873a34](https://github.com/grandinetech/grandine/commit/40d873a3419b)

</details>


<a id="db_hot-144"></a>
<details>
<summary><b>db_hot-144</b> Reuse fresh DB state instead of checkpoint download — <i>implemented · low · S · startup, bandwidth</i></summary>

**Idea.** When started with a checkpoint sync URL, reuse the persisted finalized state if it is recent enough relative to the wall clock and skip the download.

**Impact.** A restart with a persisted DB never downloads the checkpoint state again.

**Best measured result.** bound 450 slots (~30 min) (pr:ethlambda#403)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/client/src/builder.rs:290-305`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L290-L305) if chain_exists, checkpoint sync flags are ignored and FromStore is used
- [`beacon_node/client/src/builder.rs:423`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L423) CheckpointSyncUrl download happens only when there is no chain in the DB

**Skeptic check.** Confirmed: Lighthouse always reuses the DB and refuses to checkpoint sync unless --purge-db is given. This is stricter than a recency bound, so the effect is the same or better.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [ethlambda#403](https://github.com/lambdaclass/ethlambda/pull/403)

</details>


<a id="db_hot-145"></a>
<details>
<summary><b>db_hot-145</b> Return cached states without deep clone — <i>n/a · low · S · memory, cpu</i></summary>

**Idea.** Return states from the read cache without deep-cloning them on each read.

**Impact.** State clone is an Arc-based milhouse structural-share clone, so there is no deep copy to avoid.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:275-281`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L275-L281) get_by_state_root returns state.clone()

**Sources.** [prysm#2349](https://github.com/OffchainLabs/prysm/pull/2349)

</details>


<a id="db_hot-146"></a>
<details>
<summary><b>db_hot-146</b> Skip writing empty blob sidecar lists — <i>implemented · low · S · disk</i></summary>

**Idea.** Do not write a blob sidecar record to the DB for blocks with zero blobs.

**Impact.** One small DB write saved per blob-less block.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker.rs:778-793`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L778-L793) new_with_blobs/new_with_data_columns map empty lists to NoData
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:209-211`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L209-L211) num_blobs_expected == 0 -&gt; NoData
- [`beacon_node/beacon_chain/src/beacon_chain.rs:8398`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L8398) AvailableBlockData::NoData =&gt; None (no PutBlobs op)
- [`beacon_node/store/src/hot_cold_store.rs:1311`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1311) PutBlobs written only when the op exists

**Skeptic check.** Confirmed that empty blob and column lists collapse to NoData at construction, so no store op is made for them on the gossip/import or RPC paths. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@92c4e9930](https://github.com/sigp/lighthouse/commit/92c4e9930555), [lighthouse#3848](https://github.com/sigp/lighthouse/pull/3848)

</details>


<a id="db_hot-147"></a>
<details>
<summary><b>db_hot-147</b> Avoid per-block DB iterator on import — <i>n/a · low · S · cpu, disk</i></summary>

**Idea.** Do not read the last stored finalized-state slot (a DB iterator) on every block import when it is only needed for archiving; this also makes compaction cheaper.

**Impact.** Lighthouse import path does not read a last-stored-state slot via a DB iterator; the Teku-specific problem does not exist.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1068`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1068) put_state has no last-finalized-state-slot iterator lookup
- [`beacon_node/store/src/hot_cold_store.rs:2254`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2254) iterators only in migration/pruning paths

**Sources.** [teku#3559](https://github.com/Consensys-Incorporated/teku/pull/3559)

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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [nimbus#1227](https://github.com/status-im/nimbus-eth2/pull/1227)

</details>


<a id="db_hot-150"></a>
<details>
<summary><b>db_hot-150</b> Skip legacy DB lookups on state write — <i>n/a · low · S · cpu, disk</i></summary>

**Idea.** Skip legacy-table DB lookups when writing a state and skip the epoch transition when the cache already holds the exact state.

**Impact.** Nimbus legacy-table layout has no counterpart in Lighthouse.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1068-1077`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1068-L1077) put_state writes directly without legacy-table lookups
- [`beacon_node/store/src/state_cache.rs:275`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L275) cache lookup by state root

**Sources.** [nimbus#2617](https://github.com/status-im/nimbus-eth2/pull/2617)

</details>


<a id="db_hot-151"></a>
<details>
<summary><b>db_hot-151</b> Avoid startup scans over tombstoned legacy ranges — <i>n/a · low · S · startup</i></summary>

**Idea.** Skip startup lookups and deletes over deleted legacy column ranges, which take minutes over accumulated LevelDB tombstones.

**Impact.** No startup scan over tombstoned legacy column ranges; this is Lodestar-specific.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3501`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3501) iter_column_keys only used in specific maintenance paths

**Sources.** [lodestar#10449](https://github.com/ChainSafe/lodestar/pull/10449)

</details>


<a id="db_hot-152"></a>
<details>
<summary><b>db_hot-152</b> Pass slices instead of array copies to DB — <i>n/a · low · S · memory, cpu</i></summary>

**Idea.** Pass pubkeys to DB index lookups by slice/reference instead of by fixed-size array copy.

**Impact.** Rust passes keys by reference/slice already; the Go array-copy cost does not exist.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L931) put_blobs takes &amp;Hash256 and slices

**Sources.** [prysm#4466](https://github.com/OffchainLabs/prysm/pull/4466)

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

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [nimbus#1169](https://github.com/status-im/nimbus-eth2/pull/1169), [prysm#4125](https://github.com/OffchainLabs/prysm/pull/4125), [prysm#4157](https://github.com/OffchainLabs/prysm/pull/4157)

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


<a id="db_hot-156"></a>
<details>
<summary><b>db_hot-156</b> Per-entry compression choice (zstd) — <i>partial · low · M · disk</i></summary>

**Idea.** Move compression into the storage layer so it can choose the codec per entry (e.g. zstd for new entries beside existing snappy data).

**Gap in Lighthouse.** Compression is zstd with a single configured level for all blocks, state diffs and values; a per-entry codec tag would need changes in config.rs compress_bytes/decompress and the column readers. Gain is marginal.

**Impact.** Maybe slightly cheaper writes for hot small entries by using level 0 or no compression; negligible on a mainnet node.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/config.rs:12`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L12),197-201 compress_bytes uses zstd with one global compression_level

**Sources.** [grandine@03302dcc0](https://github.com/grandinetech/grandine/commit/03302dcc0de0)

</details>


<a id="db_hot-157"></a>
<details>
<summary><b>db_hot-157</b> In-memory cache over slasher span store — <i>partial · low · M · disk, cpu</i></summary>

**Idea.** Front the slasher span DB with an in-memory cache, flushing writes on eviction, to cut DB reads and writes.

**Gap in Lighthouse.** Span chunks are cached in memory only within one update batch and written once at the end of it; there is no cross-batch cache (it relies on the LMDB/mdbx page cache). A persistent LRU of chunks would need to be added to SlasherDB.

**Impact.** Fewer chunk reads from the DB across batches for slasher users only; rare setup and modest gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/array.rs:397-418`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/array.rs#L397-L418) get_chunk_for_update uses a per-batch BTreeMap of updated chunks
- [`slasher/src/array.rs:620`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/array.rs#L620) chunks written once at batch end
- [`slasher/src/database.rs:75`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L75) LRU only for attestation data roots

**Sources.** [prysm#4997](https://github.com/OffchainLabs/prysm/pull/4997)

</details>


<a id="db_hot-158"></a>
<details>
<summary><b>db_hot-158</b> Run DB reads off the async executor — <i>partial · medium · S · latency</i></summary>

**Idea.** Run blocking DB reads (block by root, payload bids) on a blocking thread pool instead of async executor threads so they do not stall the runtime.

**Gap in Lighthouse.** The payload-bid and block-streamer paths are covered. But the HTTP block and envelope GET handlers call BlockId::root (store.block_exists, get_blinded_block, block_root_at_slot) and checkpoint_slot_and_execution_optimistic synchronously inside spawn_async_with_rejection futures. These run on tokio workers. Move the BlockId::root resolution into spawn_blocking (or a blocking_task) in BlockId::full_block and in the execution_payload_envelopes handler.

**Impact.** Under heavy API load (block explorers fetching blocks by root or slot), cold-DB reads can stall tokio worker threads that are shared with networking and the beacon processor's async work.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:4307-4322`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4307-L4322) get_or_load_gloas_payload_bid uses spawn_blocking_handle
- [`beacon_node/beacon_chain/src/beacon_block_streamer.rs:260`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_block_streamer.rs#L260) streamer loads blocks on a blocking thread
- [`beacon_node/http_api/src/task_spawner.rs:118-140`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/task_spawner.rs#L118-L140) spawn_async_with_rejection runs the future on the async executor, not on a blocking worker
- [`beacon_node/http_api/src/lib.rs:1197-1199`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L1197-L1199) GET beacon/blocks/{block_id} runs block_id.full_block inside spawn_async_with_rejection
- [`beacon_node/http_api/src/block_id.rs:75-79`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L75-L79) BlockId::root for a slot calls chain.block_root_at_slot (a DB/state read) synchronously
- [`beacon_node/http_api/src/block_id.rs:105-120`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L105-L120) BlockId::root for a root calls store.block_exists and chain.get_blinded_block synchronously
- [`beacon_node/http_api/src/block_id.rs:250-251`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L250-L251) full_block calls self.root(chain) inside the async future
- [`beacon_node/http_api/src/beacon/execution_payload_envelopes.rs:619-620`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/execution_payload_envelopes.rs#L619-L620) GET execution_payload_envelopes calls block_id.root(&amp;chain) inside an async task

**Skeptic check.** The cited spawn_blocking sites are real. But the async HTTP handlers for GET beacon/blocks and execution_payload_envelopes still do synchronous DB reads in BlockId::root on the async executor, so the earlier 'implemented' verdict missed the API path.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lighthouse#5585](https://github.com/sigp/lighthouse/pull/5585), [lighthouse#9634](https://github.com/sigp/lighthouse/pull/9634)

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

**Verdict history.** not (checked) → partial (refuted)

**Sources.** [ethlambda#96](https://github.com/lambdaclass/ethlambda/pull/96)

</details>


<a id="db_hot-160"></a>
<details>
<summary><b>db_hot-160</b> Keep startup-only tables out of main allocator — <i>n/a · low · S · memory</i></summary>

**Idea.** Load large startup-only tables into a separately allocated container and free them, so the startup peak does not set a permanent memory high-watermark.

**Impact.** Rust frees memory directly; no allocator high-watermark of this kind.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/peerdb.rs:42`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/peerdb.rs#L42) - plain Rust collections freed on drop

**Sources.** [nimbus@7e2fc2b72](https://github.com/status-im/nimbus-eth2/commit/7e2fc2b7262e)

</details>


<a id="db_hot-161"></a>
<details>
<summary><b>db_hot-161</b> Tree-backed storage of pending blocks — <i>n/a · low · S · cpu, memory</i></summary>

**Idea.** Keep pending blocks in tree-backed (lazy SSZ) form to avoid full deserialize/serialize.

**Impact.** Lighthouse keeps decoded Arc'd blocks; SSZ decode is cheap, lazy tree form brings nothing.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/mod.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs) - lookups hold decoded Arc blocks

**Sources.** [lodestar#2662](https://github.com/ChainSafe/lodestar/pull/2662)

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


<a id="db_hot-163"></a>
<details>
<summary><b>db_hot-163</b> Key stored aggregates by attestation root — <i>n/a · low · S · cpu, disk</i></summary>

**Idea.** Key pooled attestation aggregates in the store by the attestation hash-tree-root so presence checks and removal of included attestations are direct key lookups or deletes instead of loading and scanning all stored aggregates.

**Gap in Lighthouse.** The Lighthouse aggregate pool is in memory keyed by attestation data (persisted only at shutdown), so there is no stored-aggregate scan to replace.

**Impact.** none

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation_storage.rs:66`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L66) pool is an in-memory HashMap keyed by CompactAttestationData, not a DB table
- [`beacon_node/operation_pool/src/attestation_storage.rs:632`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L632) prune by epoch

**Sources.** [lodestar@5ef626b76](https://github.com/ChainSafe/lodestar/commit/5ef626b76882)

</details>


<a id="db_hot-164"></a>
<details>
<summary><b>db_hot-164</b> Validate blocks before persisting as pending — <i>n/a · low · S · disk, cpu</i></summary>

**Idea.** When a block's parent state is missing, check slot bounds, proposer and signature before writing it as a pending block, and delete discarded pending blocks from disk. Junk blocks are then neither written nor re-served in by-root requests.

**Gap in Lighthouse.** Lighthouse does not persist pending blocks with missing parent state to the DB nor serve them by root, so there is nothing to validate-before-write.

**Impact.** none

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs) gossip verification returns ParentUnknown without any DB write
- beacon_node/beacon_node/network/src/sync/block_lookups holds unknown-parent blocks in memory only

**Sources.** [ethlambda#657](https://github.com/lambdaclass/ethlambda/pull/657)

</details>


