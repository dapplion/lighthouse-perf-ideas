# other_caches

123 ideas: 13 not, 20 partial, 44 implemented, 46 n/a; 8 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [other_caches-001](#other_caches-001) | Finalized deposit tree snapshot keeping only frontier hashes | n/a | low |  | cpu, memory, startup, sync |
| [other_caches-002](#other_caches-002) **★** | FIFO eviction for recent block and blob caches | not | medium | S | memory, latency |
| [other_caches-003](#other_caches-003) **★** | LRU eviction for epoch and shuffling caches | not | medium | S | latency, memory, cpu |
| [other_caches-004](#other_caches-004) **★** | Bounded LRU unviable-block set with reason | partial | medium | M | cpu, memory |
| [other_caches-005](#other_caches-005) | LRU instead of LFU for slasher span cache | n/a | low |  | memory |
| [other_caches-006](#other_caches-006) | Bounded LRU for light client data caches | implemented | low | S | memory, cpu |
| [other_caches-007](#other_caches-007) | Read locks for read-only cache accessors | partial | low | S | cpu, latency |
| [other_caches-008](#other_caches-008) | TTL eviction for tracked proposer-preparation validators | implemented | low | S | memory |
| [other_caches-009](#other_caches-009) | Cache total active balance per epoch | implemented | low | S | cpu |
| [other_caches-010](#other_caches-010) | Cache active validator indices per epoch | implemented | low | S | cpu |
| [other_caches-011](#other_caches-011) **★** | Cache attestation data responses per slot | partial | medium | S | cpu, latency |
| [other_caches-012](#other_caches-012) | Peek instead of get when completing LRU entries | not | low | S | memory |
| [other_caches-013](#other_caches-013) | Read pool entries by reference, not copy | n/a | low |  | cpu, memory |
| [other_caches-014](#other_caches-014) | Avoid false sharing in ring-buffer caches | n/a | low |  | cpu |
| [other_caches-015](#other_caches-015) | Read-only head state for active validator count | implemented | medium | S | memory, cpu |
| [other_caches-016](#other_caches-016) | Skip rebuilding an existing deposit trie | n/a | low |  | cpu, startup |
| [other_caches-017](#other_caches-017) | Avoid temporary collections in hot helpers | partial | low | M | cpu, memory |
| [other_caches-018](#other_caches-018) | Compact raw-byte keys for pubkey and byte-keyed caches | implemented | low | S | cpu, memory, latency |
| [other_caches-019](#other_caches-019) | Batch map operations under one lock | n/a | low |  | cpu, latency |
| [other_caches-020](#other_caches-020) | Well-distributed hash for committee cache keys | n/a | low | S | cpu, latency |
| [other_caches-021](#other_caches-021) | Bound payload envelope caches and quarantines | partial | low | S | memory |
| [other_caches-022](#other_caches-022) | Bound quarantine missing-parent retry tables | implemented | medium | S | memory, bandwidth |
| [other_caches-023](#other_caches-023) | Prune envelope cache by cached parents only | n/a | low |  | cpu |
| [other_caches-024](#other_caches-024) | Cap gossip block buffer by count | implemented | medium | S | memory |
| [other_caches-025](#other_caches-025) **★** | Byte-weighted budget for pending block pool | partial | medium | M | memory |
| [other_caches-026](#other_caches-026) | Bound beacon processor and sync work queues | implemented | medium | S | memory, cpu |
| [other_caches-027](#other_caches-027) | Bounded seen-message dedup caches for gossip | implemented | medium | S | memory, cpu |
| [other_caches-028](#other_caches-028) | Cache builder indices in beacon state | not | low | M | cpu |
| [other_caches-029](#other_caches-029) | Cache payload timeliness committee per epoch | partial | low | S | cpu |
| [other_caches-030](#other_caches-030) | Attach sync committee assignments to verified messages | implemented | low | S | cpu |
| [other_caches-031](#other_caches-031) | Cache shuffling and committees once per epoch | implemented | low | S | cpu, memory |
| [other_caches-032](#other_caches-032) **★** | One shared cache of decompressed validator pubkeys | partial | medium | M | cpu, memory, latency, sync, startup |
| [other_caches-033](#other_caches-033) | Hold immutable config in memory, not DB | n/a | low |  | cpu, latency |
| [other_caches-034](#other_caches-034) | Next-epoch proposer indices warm in the proposer cache | implemented | medium | S | latency |
| [other_caches-035](#other_caches-035) | Sync committee cache keyed by period root | not | low | M | cpu, memory |
| [other_caches-036](#other_caches-036) | Populate sync committee cache on miss | n/a | low |  | cpu |
| [other_caches-037](#other_caches-037) | Cheap nil checks in hot validator accessors | n/a | low |  | cpu, latency |
| [other_caches-038](#other_caches-038) | Committee cache invalidation only when needed | implemented | low | S | cpu, bandwidth |
| [other_caches-039](#other_caches-039) | Committee cache also covers previous epoch | implemented | low | S | cpu, latency |
| [other_caches-040](#other_caches-040) | Dynamic committee cache size during non-finality | not | low | S | memory |
| [other_caches-041](#other_caches-041) | No redundant mutex around thread-safe caches | n/a | low |  | cpu |
| [other_caches-042](#other_caches-042) | Concurrent caches instead of synchronized LRU | n/a | low | L | cpu, latency |
| [other_caches-043](#other_caches-043) | Lock-free concurrent map instead of sharded dashmap | not | low | M | cpu, latency |
| [other_caches-044](#other_caches-044) | Fine-grained locks in rate limiter | n/a | low |  | cpu |
| [other_caches-045](#other_caches-045) | Configurable slasher span cache size | partial | low | M | memory, latency |
| [other_caches-046](#other_caches-046) | Preallocate committee vector with true count | implemented | low | S | memory, cpu |
| [other_caches-047](#other_caches-047) | In-memory cache for validator builder registrations | partial | low | S | disk, latency |
| [other_caches-048](#other_caches-048) | Delete unviable blocks from orphan quarantine | n/a | low |  | memory |
| [other_caches-049](#other_caches-049) | Drop intermediate deposit data early | n/a | low |  | memory |
| [other_caches-050](#other_caches-050) | Do not precompute next-epoch proposer cache | implemented | low | S | memory, cpu |
| [other_caches-051](#other_caches-051) | Recompute Merkle zero hashes instead of storing | n/a | low |  | memory, disk |
| [other_caches-052](#other_caches-052) | Array-backed maps for fork-keyed tables | n/a | low |  | cpu, memory |
| [other_caches-053](#other_caches-053) | Proposer cache keyed by epoch and decision root | implemented | low | S | cpu |
| [other_caches-054](#other_caches-054) | Evict empty reprocess queue entries | implemented | medium | S | memory |
| [other_caches-055](#other_caches-055) | Cheap checks before shuffling in committee cache | implemented | low | S | cpu |
| [other_caches-056](#other_caches-056) | Finalize deposits only up to finalized state | n/a | low |  | memory |
| [other_caches-057](#other_caches-057) | Fixed growth step for pubkey cache | not | low | S | memory, latency |
| [other_caches-058](#other_caches-058) | Free pre-genesis state after genesis | n/a | low |  | memory |
| [other_caches-059](#other_caches-059) | Prune proposer cache once per duties request | n/a | low | S | cpu |
| [other_caches-060](#other_caches-060) | Per-period cache of validators' sync committee positions | not | low | M | cpu |
| [other_caches-061](#other_caches-061) **★** | Feed light client server only from new head blocks | partial | medium | M | cpu |
| [other_caches-062](#other_caches-062) | In-memory execution payload envelope store for hot chain | not | low | M | memory, latency |
| [other_caches-063](#other_caches-063) | Keep aggregated attestation payloads in memory, not DB | n/a | low | S | memory |
| [other_caches-064](#other_caches-064) | Cached pubkey-to-index map instead of registry scans | implemented | high | S | cpu |
| [other_caches-065](#other_caches-065) | Single pubkey index map, no unfinalized pubkey cache | partial | low | M | memory, cpu |
| [other_caches-066](#other_caches-066) | Cache sync committee subnet ids per validator | n/a | low | S | cpu |
| [other_caches-067](#other_caches-067) | Iteration-safe bounded maps in the operation pool | implemented | low | S | cpu |
| [other_caches-068](#other_caches-068) | Size shuffling cache for forks; compute each once | implemented | medium | S | cpu, memory |
| [other_caches-069](#other_caches-069) | Dependent-root keyed shuffling cache with lookahead | implemented | medium | S | cpu, memory, latency |
| [other_caches-070](#other_caches-070) | Never evict head epoch shufflings from cache | implemented | medium | S | cpu |
| [other_caches-071](#other_caches-071) | Persist pubkeys uncompressed to skip startup decompression | implemented | medium | S | startup, cpu |
| [other_caches-072](#other_caches-072) | Parallel pubkey decompression when building pubkey cache | implemented | low | S | cpu, startup |
| [other_caches-073](#other_caches-073) | Lazy TTL expiry without per-cache sweeper threads | n/a | low | S | memory, cpu |
| [other_caches-074](#other_caches-074) | Lazy dirty-flag rehashing of deposit merkle tree | n/a | low | S | cpu |
| [other_caches-075](#other_caches-075) | Configurable light client data retention period | not | low | S | sync, startup |
| [other_caches-076](#other_caches-076) | Single-flight active validator count, fetched only when needed | n/a | low | S | cpu, disk, startup |
| [other_caches-077](#other_caches-077) | Pubkey cache reads that do not serialize on LRU recency | n/a | low | S | latency, cpu |
| [other_caches-078](#other_caches-078) | Don't block pubkey cache readers while adding new keys | partial | low | S | latency, cpu |
| [other_caches-079](#other_caches-079) | Remove timeout locks on shared caches | implemented | low | S | latency, cpu |
| [other_caches-080](#other_caches-080) | Native first/last DB lookups instead of iterators | n/a | low | S | disk, latency |
| [other_caches-081](#other_caches-081) | Cache unfinalized light client updates, flush on finality | not | low | M | disk, memory |
| [other_caches-082](#other_caches-082) | Oldest-first eviction of slasher span cache | n/a | low | L | memory |
| [other_caches-083](#other_caches-083) | Persist light client sync progress across restarts | n/a | low | S | startup |
| [other_caches-084](#other_caches-084) | Persist eth1 deposit and block caches on shutdown | n/a | low | S | startup, sync |
| [other_caches-085](#other_caches-085) | Preallocate maps; copy only fork data for chain info | n/a | low | S | memory, cpu |
| [other_caches-086](#other_caches-086) | Precompute own committee duties per dependent root | implemented | low | S | cpu, latency |
| [other_caches-087](#other_caches-087) | Check cache before recompute or reinsert | implemented | low | S | cpu, sync |
| [other_caches-088](#other_caches-088) | Proposer index from pre-advanced next-slot state | implemented | medium | S | cpu, latency |
| [other_caches-089](#other_caches-089) | Derive payload timeliness committee from cached committees | implemented | low | S | cpu |
| [other_caches-090](#other_caches-090) | Primitive int collections for validator indices | n/a | low | S | memory, cpu |
| [other_caches-091](#other_caches-091) | Prune the execution payload bid pool in production | implemented | low | S | memory |
| [other_caches-092](#other_caches-092) | Prune payload envelope input cache after each import | implemented | low | S | memory |
| [other_caches-093](#other_caches-093) | Prune invalid execution payload envelopes | n/a | low | S | memory, disk |
| [other_caches-094](#other_caches-094) | Drop finalized deposits and proofs from deposit cache | n/a | low | S | memory |
| [other_caches-095](#other_caches-095) | Finalization-pruned seen cache for data column sidecars | implemented | medium | S | memory |
| [other_caches-096](#other_caches-096) | Prune payload-ID/proposer preparation cache on duty requests | implemented | low | S | memory |
| [other_caches-097](#other_caches-097) | Prune beacon proposer cache on finalization | implemented | low | S | memory |
| [other_caches-098](#other_caches-098) | Prune eth1 data cache by voting-window timestamp | n/a | low | S | memory |
| [other_caches-099](#other_caches-099) | Reject future-slot blocks before block timing cache | implemented | low | S | memory |
| [other_caches-100](#other_caches-100) | Slot-first nested map for cheap seen-cache pruning | partial | low | S | cpu |
| [other_caches-101](#other_caches-101) | Pubkey-indexed map in the deposit cache | n/a | low | S | cpu, latency |
| [other_caches-102](#other_caches-102) | Recent blob sidecar cache in fork-choice store | partial | low | S | disk, latency |
| [other_caches-103](#other_caches-103) | Block cache holding only most recent blocks | partial | low | S | memory |
| [other_caches-104](#other_caches-104) | In-memory block and state-root maps before DB | partial | low | M | cpu, disk |
| [other_caches-105](#other_caches-105) | Cross-fork SSZ schema registry with shared instances | n/a | low |  | memory, startup, cpu |
| [other_caches-106](#other_caches-106) | Share chain spec via reference counting, not clones | implemented | low | S | memory |
| [other_caches-107](#other_caches-107) | One background worker for pubkey cache fetches | n/a | low |  | cpu |
| [other_caches-108](#other_caches-108) | Linear-scan single-item eviction protecting new entry | partial | low | S | memory, cpu |
| [other_caches-109](#other_caches-109) | Inline loop equality for 32/48-byte roots and pubkeys | n/a | low |  | cpu |
| [other_caches-110](#other_caches-110) | Is-all-zero check instead of comparing to default digest | n/a | low |  | cpu |
| [other_caches-111](#other_caches-111) | Skip cache insertion when the cache is disabled | n/a | low |  | cpu |
| [other_caches-112](#other_caches-112) | Build light client store only when serving enabled | implemented | low | S | memory, cpu |
| [other_caches-113](#other_caches-113) **★** | Stream validator comparison in state diffs | partial | medium | M | memory |
| [other_caches-114](#other_caches-114) | Cache head state for sync committee duty requests | implemented | low | S | memory, cpu |
| [other_caches-115](#other_caches-115) | Single-flight proposer cache fill via per-entry once-cell | implemented | low | S | cpu, latency |
| [other_caches-116](#other_caches-116) | Scan deposit list from the tail for recent heights | n/a | low |  | cpu |
| [other_caches-117](#other_caches-117) | Do not retain unfinalized blocks for obsolete forks | n/a | low |  | memory |
| [other_caches-118](#other_caches-118) | Evict imported blocks from pending-sidecar quarantine | not | low | S | memory |
| [other_caches-119](#other_caches-119) | Precomputed deduplicated light client init proofs | implemented | low | S | cpu, disk, latency |
| [other_caches-120](#other_caches-120) | Precomputed fork digest cache by epoch | partial | low | S | cpu |
| [other_caches-121](#other_caches-121) | Read-only iteration over tree-backed lists | n/a | low |  | cpu, memory |
| [other_caches-122](#other_caches-122) | Remove eth1 deposit and block caches after Electra | implemented | low | S | memory, disk, cpu |
| [other_caches-123](#other_caches-123) | Track only active local validators in known-validators set | n/a | low |  | memory, startup |

★ actionable. Click an id for the full record.

## Ideas

<a id="other_caches-001"></a>
<details>
<summary><b>other_caches-001</b> Finalized deposit tree snapshot keeping only frontier hashes — <i>n/a · low · cpu, memory, startup, sync</i></summary>

**Idea.** Store the finalized part of the deposit Merkle tree as an EIP-4881 snapshot that keeps only the log2(N) frontier hashes, not every deposit leaf and log. Inserts and proofs then only touch deposits since finalization, and a snapshot lets a node start or checkpoint-sync without replaying all historical deposits.

**Impact.** The snapshot type exists but no deposit cache or eth1 sync remains, so there is no historical replay to avoid. Deposits after Electra are in-payload requests.

**Best measured result.** pr:prysm#11942: insert 52.5 ms/op, 41.6 MB/op -&gt; 3.36 ms/op, 721 KB/op

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/common/deposit_data_tree.rs:60-100`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/deposit_data_tree.rs#L60-L100) get_snapshot/from_snapshot (PR 2915 code)
- [`consensus/types/src/deposit/deposit_tree_snapshot.rs:30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/deposit/deposit_tree_snapshot.rs#L30) DepositTreeSnapshot
- [`beacon_node/client/src/builder.rs:504`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L504) eth1 service removed

**Sources.** [prysm#11942](https://github.com/OffchainLabs/prysm/pull/11942), [lighthouse#2915](https://github.com/sigp/lighthouse/pull/2915), [lodestar@fd18c2121](https://github.com/ChainSafe/lodestar/commit/fd18c2121dc6)

</details>


<a id="other_caches-002"></a>
<details>
<summary><b>other_caches-002</b> FIFO eviction for recent block and blob caches — <i>not · medium · S · memory, latency</i></summary>

**Idea.** Evict the recent-block and recent-blob caches in insertion order (FIFO) instead of LRU, so RPC reads of old entries cannot promote them and push out the newest blocks that gossip and import need.

**Gap in Lighthouse.** BlockCache (block/blob/data_column) is hashlink LruCache and try_get_full_block both promotes on hit and inserts on miss, so any read (including RPC range serving) refreshes or adds entries. A FIFO (or peek-on-read) policy is absent; it only matters if block_cache_size is non-zero, which it is not by default.

**Impact.** Negligible on default nodes (cache size 0); with the cache enabled, keeps the newest blocks resident under RPC read load.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:95`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L95)
- [`beacon_node/store/src/hot_cold_store.rs:121`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L121)
- [`beacon_node/store/src/hot_cold_store.rs:571`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L571)
- [`beacon_node/store/src/hot_cold_store.rs:597`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L597)
- [`beacon_node/store/src/config.rs:22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L22)

**Second check.** Checked every BlockCache use in hot_cold_store.rs: reads go through LruCache::get and misses insert, no peek path. The import path uses DA checker and fork choice rather than this cache, so there is no other recent-block cache with FIFO semantics.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [teku#7677](https://github.com/Consensys-Incorporated/teku/pull/7677)

</details>


<a id="other_caches-003"></a>
<details>
<summary><b>other_caches-003</b> LRU eviction for epoch and shuffling caches — <i>not · medium · S · latency, memory, cpu</i></summary>

**Idea.** Evict the least-recently-used entry from the per-epoch shuffling/committee caches instead of the oldest epoch, so work alternating between two forks or epochs does not keep evicting each other and force repeated shuffling recomputation.

**Gap in Lighthouse.** ShufflingCache::get does not record use; prune_cache sorts by shuffling_epoch and evicts oldest non-head entries. Add recency tracking and evict least-recently-used non-head entries.

**Impact.** Marginal: 16 entries keyed by (epoch, decision block), head ids protected, and states carry their own committee caches, so thrashing needs many concurrent forks.

**Best measured result.** pr:nimbus#4196: "blocking of over 5 minutes in extreme cases" with the old oldest-first policy

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:128`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L128)
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:143`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L143)
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:254`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L254)

**Second check.** Re-read get/insert/prune in shuffling_cache.rs and the http_api historical committees LruCache (caches.rs:23, separate API-only cache). Head-id protection mitigates but the eviction policy is still oldest-epoch, not LRU.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [nimbus#4196](https://github.com/status-im/nimbus-eth2/pull/4196)

</details>


<a id="other_caches-004"></a>
<details>
<summary><b>other_caches-004</b> Bounded LRU unviable-block set with reason — <i>partial · medium · M · cpu, memory</i></summary>

**Idea.** Keep invalid/orphaned (unviable) block roots in a fixed-capacity LRU map and record why each is unviable, so gossip can reject descendants of known-bad blocks immediately without re-validating, at bounded memory.

**Gap in Lighthouse.** A bounded (512) LRU of orphaned pre-finalization roots exists (PreFinalizationBlockCache), but it has no reason field and is consulted only by attestation verification, not gossip block verification. Consensus-invalid roots are remembered only by sync's time-expiring ignored_chains/failed_chains. Missing: one capacity-bounded root-&gt;reason map checked in gossip block verification for parents, fed by failed imports.

**Impact.** Saves repeated lookups and re-validation of descendants of known-bad blocks; only matters under attack or after invalid-block forks.

**Best measured result.** pr:nimbus#7685: use minilru instead of OrderedTable for simplified capacity management and performance (no numbers)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/pre_finalization_cache.rs:9`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pre_finalization_cache.rs#L9)
- [`beacon_node/beacon_chain/src/pre_finalization_cache.rs:24`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pre_finalization_cache.rs#L24)
- [`beacon_node/beacon_chain/src/block_verification.rs:1842`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1842)
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1277`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1277)
- [`beacon_node/network/src/sync/block_lookups/mod.rs:96`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L96)
- [`beacon_node/network/src/sync/range_sync/range.rs:77`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/range.rs#L77)
- [`beacon_node/beacon_chain/src/block_verification.rs:1512`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1512)

**Second check.** Found PreFinalizationBlockCache (bounded hashlink LRU of unviable pre-finalization roots, fed from check_block_against_finalized_slot) that the earlier review missed; it strengthens partial but does not cover gossip descendants or record reasons.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [nimbus#7685](https://github.com/status-im/nimbus-eth2/pull/7685)

</details>


<a id="other_caches-005"></a>
<details>
<summary><b>other_caches-005</b> LRU instead of LFU for slasher span cache — <i>n/a · low · memory</i></summary>

**Idea.** Back the slasher span cache with a plain LRU instead of a frequency/admission-based cache, since span access is recency-driven and recent spans should stay resident.

**Impact.** Lighthouse's slasher has no persistent span cache to choose an eviction policy for; chunks come from the DB per batch, and its one cache is already an LRU.

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/array.rs:566`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/array.rs#L566) update_array loads chunks per batch into a local BTreeMap
- [`slasher/src/database.rs:76`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L76) only cache is attestation_root_cache (already LRU via hashlink)

**Sources.** [prysm#5037](https://github.com/OffchainLabs/prysm/pull/5037)

</details>


<a id="other_caches-006"></a>
<details>
<summary><b>other_caches-006</b> Bounded LRU for light client data caches — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** Hold light client bootstrap/update data in a bounded LRU cache instead of an ordered hash table with manual eviction, giving O(1) eviction and a hard memory cap.

**Impact.** Memory is already capped; the only multi-entry LC cache is a hashlink LRU, and the other entries are single latest values.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/light_client_server_cache.rs:37`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_server_cache.rs#L37) prev_block_cache Mutex&lt;LruCache&gt; bounded by PREV_BLOCK_CACHE_SIZE
- [`beacon_node/beacon_chain/src/light_client_server_cache.rs:29`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_server_cache.rs#L29) other entries are single Option slots

**Skeptic check.** Confirmed that the only map-like LC cache is a bounded LRU and that there is no ordered table with manual eviction. Earlier verdict right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#9415](https://github.com/status-im/nimbus-eth2/pull/9415)

</details>


<a id="other_caches-007"></a>
<details>
<summary><b>other_caches-007</b> Read locks for read-only cache accessors — <i>partial · low · S · cpu, latency</i></summary>

**Idea.** Take shared read locks (RwLock read) rather than exclusive locks in read-only accessors of shared queues and caches, so concurrent readers do not block each other.

**Gap in Lighthouse.** Main shared caches already use RwLock read with peek. Remaining read-only paths (proposer_preparation_data, pre_finalization contains_key, BeaconProposerCache) take exclusive Mutex.

**Impact.** Marginal less lock contention; the locks are held briefly.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/lib.rs:482`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L482) proposer_preparation_data is a tokio Mutex
- [`beacon_node/execution_layer/src/lib.rs:483`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L483) proposers is RwLock
- [`beacon_node/beacon_chain/src/pending_payload_cache/mod.rs:617`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/mod.rs#L617) read() + peek for read-only access
- [`beacon_node/beacon_chain/src/pre_finalization_cache.rs:109`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pre_finalization_cache.rs#L109) Mutex even for contains_key

**Sources.** [prysm#11603](https://github.com/OffchainLabs/prysm/pull/11603)

</details>


<a id="other_caches-008"></a>
<details>
<summary><b>other_caches-008</b> TTL eviction for tracked proposer-preparation validators — <i>implemented · low · S · memory</i></summary>

**Idea.** Give the tracked-validator / proposer-preparation cache a time-to-live (e.g. one hour or a few epochs) with periodic cleanup, so validators that stop sending preparations are evicted instead of the map growing forever.

**Impact.** Already bounded: stale preparations are evicted after 2 epochs.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/lib.rs:741-770`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L741-L770) spawn_clean_proposer_caches_routine runs every epoch
- [`beacon_node/execution_layer/src/lib.rs:851-867`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L851-L867) clean_proposer_caches retains preparation entries updated in last 2 epochs and prunes proposers map by slot
- [`beacon_node/client/src/builder.rs:811`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L811) routine spawned at startup

**Skeptic check.** Verified the TTL (2 epochs) and the per-epoch cleanup task that is actually spawned in the client builder; earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#14957](https://github.com/OffchainLabs/prysm/pull/14957)

</details>


<a id="other_caches-009"></a>
<details>
<summary><b>other_caches-009</b> Cache total active balance per epoch — <i>implemented · low · S · cpu</i></summary>

**Idea.** Compute total active balance once per epoch and cache it (in the epoch/committee cache or keyed by epoch and decision root) instead of summing effective balances of all active validators on every call.

**Impact.** Already computed once per epoch and cached in state.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:819`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L819)
- [`consensus/types/src/state/beacon_state.rs:2682`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2682)
- [`consensus/types/src/state/beacon_state.rs:2703`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2703)
- [`consensus/types/src/state/beacon_state.rs:2710`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2710)
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:482`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L482)
- [`consensus/types/src/state/beacon_state.rs:2838`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2838)

**Skeptic check.** Confirmed: get_total_active_balance reads only the (epoch, u64) cache. single_pass sets it for the next epoch, build_committee_cache builds it on demand, and compute_total_active_balance_slow is called only from force_build. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#10550](https://github.com/OffchainLabs/prysm/pull/10550), [prysm#9456](https://github.com/OffchainLabs/prysm/pull/9456), [prysm#9366](https://github.com/OffchainLabs/prysm/pull/9366), [prysm#9567](https://github.com/OffchainLabs/prysm/pull/9567)

</details>


<a id="other_caches-010"></a>
<details>
<summary><b>other_caches-010</b> Cache active validator indices per epoch — <i>implemented · low · S · cpu</i></summary>

**Idea.** Cache the list of active validator indices per epoch alongside the shuffling and serve the get-active-indices helper from it instead of scanning the registry each time.

**Impact.** Hot paths (committees, attestation verification) use the cached per-epoch indices; remaining full scans run once per epoch or per sync period.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/committee_cache.rs:135`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L135) active indices computed once per committee cache build and kept as the shuffling
- [`consensus/types/src/state/committee_cache.rs:190`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L190) active_validator_indices accessor
- [`consensus/types/src/state/beacon_state.rs:1163`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1163) get_cached_active_validator_indices
- [`consensus/types/src/state/beacon_state.rs:1699`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1699) get_beacon_proposer_indices scans the registry (needs sorted order), once per epoch/decision root behind the proposer cache
- [`consensus/types/src/state/beacon_state.rs:1776`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1776) next sync committee scan, once per period

**Skeptic check.** The cached copy is shuffled, so proposer and sync-committee selection still scan the registry, but only once per epoch/period (proposer cache, epoch processing), not per call; the earlier verdict holds.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#3629](https://github.com/OffchainLabs/prysm/pull/3629)

</details>


<a id="other_caches-011"></a>
<details>
<summary><b>other_caches-011</b> Cache attestation data responses per slot — <i>partial · medium · S · cpu, latency</i></summary>

**Idea.** Cache the attestation data API response per (slot, head/committee) so the many validators asking for the same slot share one computation, and enable this cache by default.

**Gap in Lighthouse.** The Lighthouse VC already fetches attestation data once per slot (index 0) and shares it across all its validators, and the BN fast path reads it from the head snapshot or early_attester_cache. Missing: a BN-side (slot, head root) response cache, so many separate VCs (other clients, DVT) still each run produce_unaggregated_attestation, and the off-epoch case repeats get_advanced_hot_state + partial_state_advance.

**Impact.** Small: per-request work is a head-snapshot read except at epoch-boundary/old-head cases; helps BNs serving many independent VCs.

**Best measured result.** pr:prysm#2542: hit 29796 vs miss 894 in cluster

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/attestation_service.rs:256`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L256)
- [`validator_client/validator_services/src/attestation_service.rs:284`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L284)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2025`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2025)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2126`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2126)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2157`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2157)

**Second check.** Checked the VC side the earlier review skipped: attestation_service.rs produces one AttestationData per slot for all duties, which is the sharing the idea targets for Lighthouse's own VC. BN has no response cache, so partial rather than not.

**Verdict history.** not (checked) → partial (refuted)

**Sources.** [prysm#4873](https://github.com/OffchainLabs/prysm/pull/4873), [prysm#2542](https://github.com/OffchainLabs/prysm/pull/2542)

</details>


<a id="other_caches-012"></a>
<details>
<summary><b>other_caches-012</b> Peek instead of get when completing LRU entries — <i>not · low · S · memory</i></summary>

**Idea.** When updating or completing entries in an LRU cache, use peek instead of get so finished entries are not promoted to most-recently-used and do not displace live ones.

**Gap in Lighthouse.** Lighthouse still uses get_mut at completion time and promotes finished entries to MRU.

**Impact.** Tiny: finished entries no longer displace live ones in a small LRU; matters only under churn or non-finality.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/pending_payload_cache/mod.rs:568`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/mod.rs#L568) get_mut used to clear span after availability, promoting entry in LRU
- [`beacon_node/beacon_chain/src/pending_payload_cache/mod.rs:617`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/mod.rs#L617) peek used for reads
- lighthouse#9988 closed unmerged

**Sources.** [lighthouse#9988](https://github.com/sigp/lighthouse/pull/9988)

</details>


<a id="other_caches-013"></a>
<details>
<summary><b>other_caches-013</b> Read pool entries by reference, not copy — <i>n/a · low · cpu, memory</i></summary>

**Idea.** Read per-slot entries of in-memory pools (e.g. builder bid pool) by reference or in place instead of copying the whole per-slot structure on each lookup.

**Impact.** Lighthouse keeps one latest bid per stream, not a per-slot pool copied on lookup.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/builder_client/src/bid_streams.rs:195`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/builder_client/src/bid_streams.rs#L195) clones only the single latest bid under mutex; no per-slot structure copied

**Sources.** [nimbus#8742](https://github.com/status-im/nimbus-eth2/pull/8742)

</details>


<a id="other_caches-014"></a>
<details>
<summary><b>other_caches-014</b> Avoid false sharing in ring-buffer caches — <i>n/a · low · cpu</i></summary>

**Idea.** Place producer-written and consumer-written head/tail fields of shared ring buffers on separate cache lines, and publish the consumer tail only when it changes, to cut cross-core cache-line contention.

**Impact.** Lighthouse has no hand-written ring-buffer caches; channels come from libraries.

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.toml and sources: no custom ring buffers, no CachePadded use found; queues use std/tokio channels

**Sources.** [silver#312](https://github.com/gattaca-com/silver/pull/312)

</details>


<a id="other_caches-015"></a>
<details>
<summary><b>other_caches-015</b> Read-only head state for active validator count — <i>implemented · medium · S · memory, cpu</i></summary>

**Idea.** Compute the active validator count (and similar hot-path reads) from a read-only reference to the head state instead of cloning the full head state.

**Impact.** None needed.

**Best measured result.** pr:prysm#14592: about 500 MB less memory allocated on holesky

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:389`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L389)
- [`beacon_node/network/src/service.rs:836`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L836)
- [`beacon_node/http_api/src/state_id.rs:227`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L227)
- [`beacon_node/beacon_processor/src/scheduler/work_queue.rs:335`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_queue.rs#L335)

**Skeptic check.** Confirmed: active_validator_count reads cached indices through the Arc head snapshot. The HTTP API head path uses map_state_* on a borrowed head state, and the only head_beacon_state_cloned user is state_at_slot, where the clone shares milhouse trees structurally. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#14592](https://github.com/OffchainLabs/prysm/pull/14592)

</details>


<a id="other_caches-016"></a>
<details>
<summary><b>other_caches-016</b> Skip rebuilding an existing deposit trie — <i>n/a · low · cpu, startup</i></summary>

**Idea.** Reuse the already-built deposit Merkle trie instead of regenerating it from all deposits when it is available, avoiding redundant trie construction at startup and block production.

**Impact.** Eth1 deposit cache/trie is no longer built in the beacon node, so there is nothing to skip rebuilding.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/deposit/mod.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/deposit/mod.rs) and [`consensus/state_processing/src/common/deposit_data_tree.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/deposit_data_tree.rs) only; no beacon_node usage of DepositDataTree/deposit cache

**Sources.** [prysm#4383](https://github.com/OffchainLabs/prysm/pull/4383)

</details>


<a id="other_caches-017"></a>
<details>
<summary><b>other_caches-017</b> Avoid temporary collections in hot helpers — <i>partial · low · M · cpu, memory</i></summary>

**Idea.** In attestation, shuffling, hashing and set-manipulation helpers, use slices/views and iterate directly instead of allocating temporary vectors or sets.

**Gap in Lighthouse.** Hot paths use cached slices, but several helpers still allocate temporary Vecs/sets; no audit has been done.

**Impact.** Small allocation savings spread over many paths; no single big win.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:1175`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1175) get_active_validator_indices returns a fresh Vec
- [`consensus/types/src/state/committee_cache.rs:440`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L440) builds Vec per call

**Sources.** [nimbus#1573](https://github.com/status-im/nimbus-eth2/pull/1573), [nimbus#3075](https://github.com/status-im/nimbus-eth2/pull/3075)

</details>


<a id="other_caches-018"></a>
<details>
<summary><b>other_caches-018</b> Compact raw-byte keys for pubkey and byte-keyed caches — <i>implemented · low · S · cpu, memory, latency</i></summary>

**Idea.** Key the pubkey-to-validator-index map and similar in-memory caches (e.g. blob availability index) by raw fixed-size byte arrays with a fast hash, optionally in native/off-heap memory, instead of hex strings or other heavy intermediate representations. This cuts per-key memory and hashing/allocation cost.

**Impact.** Raw fixed-size keys already used; only the default SipHash hasher could be swapped, for a small gain.

**Best measured result.** ~1400 bytes/key, ~350 MB for 250k concatenated string keys avoided (pr:lodestar#3561)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:25`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L25)
- [`consensus/types/src/state/pubkey_cache.rs:13`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/pubkey_cache.rs#L13)
- [`crypto/bls/src/generic_public_key_bytes.rs:21`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/generic_public_key_bytes.rs#L21)

**Skeptic check.** Confirmed: both the chain pubkey cache (HashMap) and the in-state PubkeyCache (rpds HashTrieMap) key by PublicKeyBytes, which is a [u8;48] newtype, so there are no string keys. Availability caches key by Hash256. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#7022](https://github.com/ChainSafe/lodestar/pull/7022), [prysm#13885](https://github.com/OffchainLabs/prysm/pull/13885), [lodestar@11ecb95bc](https://github.com/ChainSafe/lodestar/commit/11ecb95bc84a), [lodestar#7091](https://github.com/ChainSafe/lodestar/pull/7091), [lodestar#3561](https://github.com/ChainSafe/lodestar/pull/3561), [caplin#18540](https://github.com/erigontech/erigon/pull/18540)

</details>


<a id="other_caches-019"></a>
<details>
<summary><b>other_caches-019</b> Batch map operations under one lock — <i>n/a · low · cpu, latency</i></summary>

**Idea.** Provide closure-style helpers that run several operations on a shared map under one lock acquisition, instead of taking the lock separately for each get/insert.

**Best measured result.** pr:prysm#11953: GenericTx 25881 ns/op vs 53586 ns/op for separate locks (about 2x)

**Evidence (Lighthouse @ 928b61e719).**

- Rust lock guards (parking_lot Mutex/RwLock) already allow several map ops under one guard, e.g. [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:175`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L175) uses one lock scope

**Sources.** [prysm#11953](https://github.com/OffchainLabs/prysm/pull/11953)

</details>


<a id="other_caches-020"></a>
<details>
<summary><b>other_caches-020</b> Well-distributed hash for committee cache keys — <i>n/a · low · S · cpu, latency</i></summary>

**Idea.** Hash composite (slot, committee index) cache keys with a function that mixes both fields so keys do not collide into few buckets, and use a simple LRU map for the committee cache.

**Impact.** None; the keying problem does not exist. Lighthouse caches one CommitteeCache per epoch shuffling id, not per (slot, committee index).

**Best measured result.** pr:teku#3758: Block import 21.2 -&gt; 18.6 ms/block (~13%); getCommitteeHit 8.47M -&gt; 25.0M ops/s

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:128`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L128) HashMap keyed by AttestationShufflingId, 16 entries
- [`consensus/types/src/state/committee_cache.rs:26`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L26) CommitteeCache per epoch, no (slot,index) key

**Sources.** [teku#3758](https://github.com/Consensys-Incorporated/teku/pull/3758), [teku#880](https://github.com/Consensys-Incorporated/teku/pull/880)

</details>


<a id="other_caches-021"></a>
<details>
<summary><b>other_caches-021</b> Bound payload envelope caches and quarantines — <i>partial · low · S · memory</i></summary>

**Idea.** Cap the size of execution payload envelope caches, envelope quarantines and pending-payload queues, evicting lowest-slot entries on insert, since finality-based pruning does not fire during non-finality; optionally reload evicted entries from the database on demand.

**Gap in Lighthouse.** Add a max-slot-count eviction to ObservedPayloadEnvelopes::observe_envelope.

**Impact.** Bounds a small set of (root,builder) keys during long non-finality; memory effect is tiny, only matters in non-finality incidents.

**Best measured result.** pr:lodestar#9489: OOM crash loop at 8GB heap on devnet (no gain numbers)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/pending_payload_cache/mod.rs:57`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/mod.rs#L57) LRU capacity 32 for pending components
- [`beacon_node/beacon_chain/src/pending_payload_envelopes.rs:87`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_envelopes.rs#L87) slot-age prune (2 slots)
- [`beacon_node/beacon_chain/src/payload_envelope_verification/observed_payload_envelopes.rs:52`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/observed_payload_envelopes.rs#L52) prune only by finalized slot, no size cap
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:81`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L81) MAXIMUM_QUEUED_ENVELOPES=16

**Sources.** [lodestar#9489](https://github.com/ChainSafe/lodestar/pull/9489), [nimbus#8462](https://github.com/status-im/nimbus-eth2/pull/8462), [lodestar#9904](https://github.com/ChainSafe/lodestar/pull/9904), [caplin#21248](https://github.com/erigontech/erigon/pull/21248)

</details>


<a id="other_caches-022"></a>
<details>
<summary><b>other_caches-022</b> Bound quarantine missing-parent retry tables — <i>implemented · medium · S · memory, bandwidth</i></summary>

**Idea.** Bound the tables of missing parents/payloads that quarantines retry fetching, with a max capacity and capped exponential backoff, so unresolved items cannot grow memory or request load without limit.

**Impact.** None needed; bounded by lookup count, attempt cap and stuck/no-peer timeouts.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/manager.rs:95`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L95)
- [`beacon_node/network/src/sync/manager.rs:1089`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L1089)
- [`beacon_node/network/src/sync/block_lookups/mod.rs:62`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L62)
- [`beacon_node/network/src/sync/block_lookups/mod.rs:77`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L77)
- [`beacon_node/network/src/sync/block_lookups/mod.rs:408`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L408)
- [`beacon_node/network/src/sync/block_lookups/mod.rs:719`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L719)
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:81`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L81)

**Skeptic check.** Confirmed: lookups are capped at 200 (rejected at mod.rs:408), retries are capped at 4, a 15 s timer prunes stuck and peerless lookups, pending unknown roots are an LRU of 1024, and early envelopes are capped at 16. There is no exponential backoff, but memory and request load are bounded, which is the effect the idea asks for.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#8407](https://github.com/status-im/nimbus-eth2/pull/8407)

</details>


<a id="other_caches-023"></a>
<details>
<summary><b>other_caches-023</b> Prune envelope cache by cached parents only — <i>n/a · low · cpu</i></summary>

**Idea.** When pruning cached payload envelope inputs for a branch, look up the cache entries by parent directly instead of walking every fork-choice ancestor, so the cost scales with cache size, not chain depth.

**Impact.** No ancestor walk exists to remove.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/pending_payload_cache/mod.rs:662`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/mod.rs#L662) do_maintenance scans cache entries by epoch cutoff
- [`beacon_node/beacon_chain/src/pending_payload_envelopes.rs:87`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_envelopes.rs#L87) prune is retain over cache

**Sources.** [lodestar#9326](https://github.com/ChainSafe/lodestar/pull/9326)

</details>


<a id="other_caches-024"></a>
<details>
<summary><b>other_caches-024</b> Cap gossip block buffer by count — <i>implemented · medium · S · memory</i></summary>

**Idea.** Cap the number of gossip-received blocks held in memory awaiting processing and purge the oldest once over the limit.

**Impact.** None needed; bounded by count.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_queue.rs:384`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_queue.rs#L384)
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:78`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L78)
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:670`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L670)

**Skeptic check.** Confirmed: gossip_block_queue is capped at 1024, delayed_block_queue at 1024, and early gossip/RPC blocks in the reprocess queue at 16, with drops when full. When full it drops new blocks rather than purging the oldest, but the memory bound is the same.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#8944](https://github.com/erigontech/erigon/pull/8944)

</details>


<a id="other_caches-025"></a>
<details>
<summary><b>other_caches-025</b> Byte-weighted budget for pending block pool — <i>partial · medium · M · memory</i></summary>

**Idea.** Bound the unknown-parent pending block pool by total retained SSZ bytes as well as item count, evicting oldest first and rejecting oversized items, so memory is capped regardless of block size.

**Gap in Lighthouse.** All pending-block holders (reprocess queue 16 blocks, lookups 200, DA pending components) are count-capped; per-item size is bounded only by the gossip/RPC max message size. No total-SSZ-bytes budget with oldest-first eviction.

**Impact.** Only tightens worst-case memory with maximum-size blocks; count caps times max message size already bound it.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:78`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L78)
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:670`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L670)
- [`beacon_node/network/src/sync/block_lookups/mod.rs:77`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L77)
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:351`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L351)
- [`beacon_node/lighthouse_network/src/service/mod.rs:246`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L246)

**Second check.** Searched network, beacon_processor and DA checker for any byte accounting (ssz_bytes_len, byte budgets): none. Oversized items are rejected by gossipsub max_transmit_size, which covers the reject-oversized part of the idea.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [teku#10758](https://github.com/Consensys-Incorporated/teku/pull/10758)

</details>


<a id="other_caches-026"></a>
<details>
<summary><b>other_caches-026</b> Bound beacon processor and sync work queues — <i>implemented · medium · S · memory, cpu</i></summary>

**Idea.** Put explicit length limits on the queues and in-flight work between network, sync and the beacon processor so bursts of blocks, blobs or lookups cannot grow without bound or starve other work.

**Impact.** Already bounds memory and starvation under bursts.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:82`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L82)
- [`beacon_node/beacon_processor/src/lib.rs:762`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L762)
- [`beacon_node/beacon_processor/src/scheduler/work_queue.rs:378`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_queue.rs#L378)
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:78`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L78)
- [`beacon_node/network/src/sync/block_lookups/mod.rs:77`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L77)

**Skeptic check.** Confirmed that e31b5d0ca196 is an ancestor of HEAD and that the event, idle, per-work-type and reprocess queues are all bounded. The network-to-sync SyncMessage and NetworkMessage channels stay unbounded (network/src/service.rs:177,347), but their volume is limited by the bounded lookups and in-flight requests upstream.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@e31b5d0ca](https://github.com/sigp/lighthouse/commit/e31b5d0ca196)

</details>


<a id="other_caches-027"></a>
<details>
<summary><b>other_caches-027</b> Bounded seen-message dedup caches for gossip — <i>implemented · medium · S · memory, cpu</i></summary>

**Idea.** Back gossip seen-message dedup sets (attestations per validator/target epoch, aggregators, exits, slashings, blocks) with bounded caches instead of unbounded maps, so duplicates are dropped cheaply with capped memory; reuse epoch-boundary checkpoint states from a cache keyed by (epoch, root).

**Impact.** Duplicate gossip dropped via bounded bitfield/epoch-window caches; checkpoint states served from the hot state cache by (block root, slot).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/observed_attesters.rs:37`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_attesters.rs#L37) MAX_CACHED_EPOCHS=4
- [`beacon_node/beacon_chain/src/observed_attesters.rs:339`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_attesters.rs#L339) observe_validator auto-prunes on every insert
- [`beacon_node/beacon_chain/src/observed_aggregates.rs:429`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_aggregates.rs#L429) prune by slot window
- [`beacon_node/beacon_chain/src/observed_block_producers.rs:187`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_block_producers.rs#L187) prune on finalization (canonical_head.rs:1608)
- [`beacon_node/lighthouse_network/src/config.rs:507`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L507) gossipsub duplicate_cache_time 2 epochs
- [`beacon_node/store/src/state_cache.rs:316`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L316) get_by_block_root(block_root, slot) serves advanced/checkpoint states

**Skeptic check.** Verified auto-pruning epoch containers on gossip attester/aggregator paths and the libp2p time-bounded duplicate cache; earlier evidence was right. Exit/slashing sets are bounded by validator count.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#4208](https://github.com/OffchainLabs/prysm/pull/4208), [lodestar@97d413733](https://github.com/ChainSafe/lodestar/commit/97d4137333ab)

</details>


<a id="other_caches-028"></a>
<details>
<summary><b>other_caches-028</b> Cache builder indices in beacon state — <i>not · low · M · cpu</i></summary>

**Idea.** Keep a cache of builder indices in the beacon state (Gloas) instead of scanning the registry for builders on each lookup.

**Gap in Lighthouse.** Add a pubkey-to-index and free-slot index to BeaconState keyed off builders, updated in get_index_for_new_builder/add_builder_to_registry; needs invalidation on balance/withdrawable_epoch changes (noted in the TODO).

**Impact.** Only cheaper on builder deposits, which are rare while the builder set is small; negligible today.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:2513`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2513) TODO(gloas) get_index_for_new_builder linear scan of builders, no cache
- [`consensus/types/src/state/beacon_state.rs:2427`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2427) get_builder is direct indexing
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:935`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L935) builders lookups

**Sources.** [grandine#682](https://github.com/grandinetech/grandine/pull/682)

</details>


<a id="other_caches-029"></a>
<details>
<summary><b>other_caches-029</b> Cache payload timeliness committee per epoch — <i>partial · low · S · cpu</i></summary>

**Idea.** Compute the payload timeliness committee (PTC) for the whole epoch once and cache it with a validator-to-slots index, instead of re-running the balance-weighted selection per duty check and per payload attestation verification.

**Gap in Lighthouse.** No validator-to-slot reverse index: BeaconChain::compute_ptc_duties -&gt; BeaconState::get_ptc_assignment materializes 32 PTCs (512 indices each, read from the milhouse ptc_window) and linear-scans them for every requested validator, so a duties request for N validators costs N*32*512 reads plus 32N allocations. Building the epoch's PTCs once and a HashMap&lt;validator, slot&gt; (or using CachedPTCs from the shuffling cache) would make it O(N).

**Impact.** The expensive balance-weighted selection is never re-run (ptc_window plus shuffling cache), so gossip and block import are fine; only the PTC duties API is quadratic-ish, roughly 16M element reads per 1000 validators per call.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:44-71`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L44-L71) CachedPTCs holds all 32 PTCs of an epoch
- [`beacon_node/beacon_chain/src/payload_attestation_verification/gossip_verified_payload_attestation.rs:102-114`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_attestation_verification/gossip_verified_payload_attestation.rs#L102-L114) gossip uses cached ptc_for_slot
- [`consensus/types/src/state/beacon_state.rs:3591-3626`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3591-L3626) get_ptc reads ptc_window (no balance-weighted recompute) but allocates a new 512-entry Vec per call
- [`consensus/types/src/state/beacon_state.rs:3685-3698`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3685-L3698) get_ptc_assignment loops 32 slots x get_ptc x contains per validator
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1771-1810`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1771-L1810) compute_ptc_duties calls get_ptc_assignment per requested validator

**Skeptic check.** Earlier evidence is right for gossip and block processing, but the duties path the grandine PR targets (get_validator_ptc_slots) is missing in Lighthouse: compute_ptc_duties re-reads every slot's PTC per validator.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [grandine#488](https://github.com/grandinetech/grandine/pull/488), [prysm#16451](https://github.com/OffchainLabs/prysm/pull/16451)

</details>


<a id="other_caches-030"></a>
<details>
<summary><b>other_caches-030</b> Attach sync committee assignments to verified messages — <i>implemented · low · S · cpu</i></summary>

**Idea.** Store the computed sync subcommittee assignments (subnets and positions) on the verified sync committee message object so aggregation and pool insertion reuse them instead of recomputing.

**Impact.** Already done.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/sync_committee_verification.rs:282-285`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/sync_committee_verification.rs#L282-L285) VerifiedSyncCommitteeMessage stores subnet_positions
- [`beacon_node/beacon_chain/src/sync_committee_verification.rs:472`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/sync_committee_verification.rs#L472) positions computed once during gossip verification
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2644-2656`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2644-L2656) add_to_naive_sync_aggregation_pool reuses subnet_positions()

**Skeptic check.** Verified positions are computed once in verification and reused for pool insertion; earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#3874](https://github.com/Consensys-Incorporated/teku/pull/3874)

</details>


<a id="other_caches-031"></a>
<details>
<summary><b>other_caches-031</b> Cache shuffling and committees once per epoch — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Compute the shuffled active validator list and the committees (plus per-epoch counts such as committees per slot) once per epoch, cache them in one shared cache keyed by epoch/decision root, and slice committees from it for state transition, attestation validation and duties. This avoids reshuffling per state or per lookup and avoids duplicate shuffled-index caches.

**Impact.** Shuffling computed once per epoch per lineage and shared across state clones and attestation verification.

**Best measured result.** pr:nimbus#316: ~2x state_sim speedup (12m26 -&gt; ~8m with start_shard_cache and committee count)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:2824`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2824) build_committee_cache only builds if not initialized
- [`consensus/types/src/state/beacon_state.rs:2887`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2887) advance_caches rotates Arc caches at epoch transition
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5211`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5211) import_block_update_shuffling_cache_fallible primes ShufflingCache by decision root
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:340`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L340) with_cached_shuffling serves attestation validation

**Skeptic check.** Confirmed committee caches are Arc-shared, rotated at epoch boundaries and mirrored into the decision-root keyed ShufflingCache used by gossip; earlier verdict correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#291](https://github.com/status-im/nimbus-eth2/pull/291), [prysm#3625](https://github.com/OffchainLabs/prysm/pull/3625), [prysm#2323](https://github.com/OffchainLabs/prysm/pull/2323), [prysm#2237](https://github.com/OffchainLabs/prysm/pull/2237), [prysm#2228](https://github.com/OffchainLabs/prysm/pull/2228), [teku#696](https://github.com/Consensys-Incorporated/teku/pull/696), [teku#746](https://github.com/Consensys-Incorporated/teku/pull/746), [nimbus#316](https://github.com/status-im/nimbus-eth2/pull/316), [prysm#7242](https://github.com/OffchainLabs/prysm/pull/7242), [nimbus#235](https://github.com/status-im/nimbus-eth2/pull/235), [nimbus#1068](https://github.com/status-im/nimbus-eth2/pull/1068), [prysm#3607](https://github.com/OffchainLabs/prysm/pull/3607), [prysm#3948](https://github.com/OffchainLabs/prysm/pull/3948)

</details>


<a id="other_caches-032"></a>
<details>
<summary><b>other_caches-032</b> One shared cache of decompressed validator pubkeys — <i>partial · medium · M · cpu, memory, latency, sync, startup</i></summary>

**Idea.** Keep a single process-wide cache of decompressed BLS pubkey points per validator index, sized for the whole validator set and shared by state transition, signature verification, slasher and other components. BLS paths then never decompress the 48-byte key or re-fetch it per verification.

**Gap in Lighthouse.** Validator pubkeys are cached, but Gloas builder pubkeys are decompressed from state on every verification: gossip_verified_bid (execution_payload_bid_signature_set with get_builder_pubkey_from_state), BlockSignatureVerifier::include_execution_payload_bid during block import, direct_verified_bid, and gossip envelope verification for external builders (loads state). No ValidatorPubkeyCache equivalent for the builder registry.

**Impact.** Each gossip bid/envelope from an external builder pays a ~50us G1 decompression (and the envelope path a state load); matters once Gloas is live with many bids per slot.

**Best measured result.** pr:teku#3314: "speedup ~x50-x100" (partial fix of #3294)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:23`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L23) decompressed validator pubkeys by index
- [`beacon_node/beacon_chain/src/block_verification.rs:2236-2254`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L2236-L2254) block signature verifier uses pubkey cache
- [`consensus/state_processing/src/per_block_processing/signature_sets.rs:79`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/signature_sets.rs#L79) get_builder_pubkey_from_state decompresses per call
- [`consensus/state_processing/src/per_block_processing/block_signature_verifier.rs:413`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/block_signature_verifier.rs#L413) TODO(gloas) global builder pubkey cache
- [`beacon_node/beacon_chain/src/payload_bid_verification/gossip_verified_bid.rs:464`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_bid_verification/gossip_verified_bid.rs#L464) gossip bid decompresses builder pubkey
- [`beacon_node/beacon_chain/src/payload_envelope_verification/gossip_verified_envelope.rs:272`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/gossip_verified_envelope.rs#L272) TODO(gloas) builder pubkey cache, loads state

**Skeptic check.** Validator pubkey cache is real and used on block import and gossip; earlier evidence missed the Gloas builder-key paths, which carry explicit TODO(gloas) notes for a missing builder pubkey cache.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [teku#3314](https://github.com/Consensys-Incorporated/teku/pull/3314), [prysm#7967](https://github.com/OffchainLabs/prysm/pull/7967), [nimbus#2625](https://github.com/status-im/nimbus-eth2/pull/2625), [lodestar@dc9669dbb](https://github.com/ChainSafe/lodestar/commit/dc9669dbbe13), [prysm#5220](https://github.com/OffchainLabs/prysm/pull/5220), [lighthouse#854](https://github.com/sigp/lighthouse/pull/854)

</details>


<a id="other_caches-033"></a>
<details>
<summary><b>other_caches-033</b> Hold immutable config in memory, not DB — <i>n/a · low · cpu, latency</i></summary>

**Idea.** Keep immutable chain config/spec values as plain in-memory fields instead of reading and deserializing them from the database on tick, propose and import paths.

**Impact.** Nothing to change.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs) spec held as Arc&lt;ChainSpec&gt; in memory

**Sources.** [ethlambda#563](https://github.com/lambdaclass/ethlambda/pull/563)

</details>


<a id="other_caches-034"></a>
<details>
<summary><b>other_caches-034</b> Next-epoch proposer indices warm in the proposer cache — <i>implemented · medium · S · latency</i></summary>

**Idea.** At the epoch boundary (or earlier), compute the next epoch's proposer indices and keep both current and next epoch in the proposer cache, so the first duties/block request of an epoch does not compute them cold.

**Impact.** Proposer duties for the new epoch are computed during the previous epoch's last-slot state advance, so slot-0 duties are warm.

**Best measured result.** removes &gt;500ms GetDuty delay at slot 0 (pr:prysm#12484)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:346-394`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L346-L394) primes current (and post-Fulu next) epoch proposer shuffling when advancing into a new epoch
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:26`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L26) LRU keyed (epoch, decision root)

**Skeptic check.** Confirmed the state advance timer fills the proposer cache before the epoch boundary; pre-Fulu next epoch cannot be known earlier. Earlier verdict correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#12482](https://github.com/OffchainLabs/prysm/pull/12482), [prysm#12484](https://github.com/OffchainLabs/prysm/pull/12484)

</details>


<a id="other_caches-035"></a>
<details>
<summary><b>other_caches-035</b> Sync committee cache keyed by period root — <i>not · low · M · cpu, memory</i></summary>

**Idea.** Key the sync committee cache by the block root at the start of the sync period instead of the hash tree root of the committee, so a lookup needs no state copy and no tree hashing.

**Gap in Lighthouse.** Lighthouse has no cache keyed by sync period root. The committee lives in the state (Arc) so lookups need no state copy or tree hash; the cost that remains is the per-lookup pubkey scan. A period-root keyed cache of (committee, validator-&gt;positions) in BeaconChain would fix it; see other_caches-060.

**Impact.** Small: no copy/hash per lookup already, since the state holds the committee in an Arc. Gain is only avoiding repeated scans.

**Best measured result.** pr:prysm#9128: Saves one copy and one hash tree root per lookup

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:1753`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1753) get_sync_committee_indices resolves pubkeys through pubkey_cache each call
- [`beacon_node/beacon_chain/src/sync_committee_verification.rs:472`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/sync_committee_verification.rs#L472) subcommittee_positions_for_public_key scans the committee
- [`consensus/types/src/sync_committee/sync_committee.rs:70`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/sync_committee/sync_committee.rs#L70) linear scan

**Sources.** [prysm#9128](https://github.com/OffchainLabs/prysm/pull/9128)

</details>


<a id="other_caches-036"></a>
<details>
<summary><b>other_caches-036</b> Populate sync committee cache on miss — <i>n/a · low · cpu</i></summary>

**Idea.** On a sync committee cache miss (e.g. after restart), compute and fill the cache asynchronously so later lookups hit.

**Impact.** No cold cache after restart.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/sync_committee/sync_committee.rs:73`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/sync_committee/sync_committee.rs#L73) positions computed from the committee stored in the state
- [`consensus/types/src/state/beacon_state.rs:162`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L162) only error variant mentions a sync committee cache

**Sources.** [prysm#9176](https://github.com/OffchainLabs/prysm/pull/9176)

</details>


<a id="other_caches-037"></a>
<details>
<summary><b>other_caches-037</b> Cheap nil checks in hot validator accessors — <i>n/a · low · cpu, latency</i></summary>

**Idea.** Make the read-only validator view constructor do its cheap null check first and avoid expensive checks on this hot path.

**Impact.** None.

**Best measured result.** pr:prysm#12677: 10-20ms in happy case flame graph

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs) validators accessed through milhouse lists, no Go-style nil check wrapper

**Sources.** [prysm#12677](https://github.com/OffchainLabs/prysm/pull/12677)

</details>


<a id="other_caches-038"></a>
<details>
<summary><b>other_caches-038</b> Committee cache invalidation only when needed — <i>implemented · low · S · cpu, bandwidth</i></summary>

**Idea.** Make sure the committee-per-slot cache is not cleared on every state transition, only when its key actually changes, and do not re-broadcast already-seen gossip messages.

**Impact.** No per-slot committee cache invalidation; duplicates not re-forwarded.

**Best measured result.** pr:teku#711: enabled 4 node test to finalize

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:2824`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2824) build_committee_cache skips if initialized
- [`consensus/types/src/state/beacon_state.rs:2887`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2887) caches only rotated at epoch transition
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5220`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5220) skip if shuffling id already cached
- [`beacon_node/lighthouse_network/src/config.rs:507`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L507) gossipsub duplicate cache

**Skeptic check.** Committee caches survive per-slot processing and are rotated only at epoch change; gossipsub duplicate cache prevents rebroadcast. Earlier verdict correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#711](https://github.com/Consensys-Incorporated/teku/pull/711)

</details>


<a id="other_caches-039"></a>
<details>
<summary><b>other_caches-039</b> Committee cache also covers previous epoch — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Populate the committee cache for the previous epoch too, so previous-epoch attestations near an epoch boundary hit the cache instead of recomputing the shuffling.

**Impact.** Previous-epoch attestations hit the state or shuffling cache without recompute.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:59`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L59) CACHED_EPOCHS=3
- [`consensus/types/src/state/beacon_state.rs:2768-2773`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2768-L2773) build_all_committee_caches builds previous/current/next
- [`consensus/types/src/state/beacon_state.rs:2887-2893`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2887-L2893) advance_caches rotates current into previous at epoch transition
- [`beacon_node/beacon_chain/src/block_verification.rs:1692`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1692) build_all_committee_caches on block import
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5211-5230`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5211-L5230) shuffling cache (16 entries keyed by shuffling id) populated on import

**Skeptic check.** Previous-epoch committee cache exists on states and survives the epoch transition via rotation; gossip verification uses the keyed shuffling cache. Earlier verdict correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#4402](https://github.com/OffchainLabs/prysm/pull/4402)

</details>


<a id="other_caches-040"></a>
<details>
<summary><b>other_caches-040</b> Dynamic committee cache size during non-finality — <i>not · low · S · memory</i></summary>

**Idea.** Size the committee/shuffling cache small by default and grow it only when the chain is not finalizing, instead of permanently using a large capacity.

**Gap in Lighthouse.** ShufflingCache::new takes a fixed cache_size and prune uses it; make cache_size a function of finalization distance (update in the head-update path) and shrink back when finalizing.

**Impact.** Memory only: each entry is a few MB at 1M validators; 16 entries is already small, so saving is tens of MB at best. Non-finality growth is a resilience gain, not speed.

**Best measured result.** pr:prysm#13640: significantly less memory

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:25`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L25) DEFAULT_CACHE_SIZE = 16 fixed
- [`beacon_node/beacon_chain/src/chain_config.rs:169`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/chain_config.rs#L169) shuffling_cache_size static; shuffling_cache.rs:247 prune to fixed cache_size

**Sources.** [prysm#13640](https://github.com/OffchainLabs/prysm/pull/13640)

</details>


<a id="other_caches-041"></a>
<details>
<summary><b>other_caches-041</b> No redundant mutex around thread-safe caches — <i>n/a · low · cpu</i></summary>

**Idea.** Remove extra mutexes wrapped around caches that are already internally thread-safe (e.g. committee LRU), and use atomic contains-or-add instead of check-then-insert under a lock. Each access then takes one lock instead of two, cutting contention.

**Impact.** Rust caches use one explicit lock; there is no double-lock wrapper around an internally thread-safe cache.

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/database.rs:76`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L76) Mutex&lt;LruCache&gt; is the only cache lock, single lock per access
- [`beacon_node/lighthouse_network/src/rpc/rate_limiter.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/rate_limiter.rs) no locks

**Sources.** [prysm#13794](https://github.com/OffchainLabs/prysm/pull/13794), [prysm#13811](https://github.com/OffchainLabs/prysm/pull/13811), [prysm#16995](https://github.com/OffchainLabs/prysm/pull/16995)

</details>


<a id="other_caches-042"></a>
<details>
<summary><b>other_caches-042</b> Concurrent caches instead of synchronized LRU — <i>n/a · low · L · cpu, latency</i></summary>

**Idea.** Replace globally synchronized LRU caches on hot paths (state transition caches, finalized state cache, db block/validator caches) with a concurrent cache (Caffeine/ristretto-style), so a slow miss on one key does not block readers of other keys.

**Impact.** Not worth it: Rust Mutex sections are short and slow misses are not computed under the lock, so the Java synchronized-fallback blocking problem does not occur.

**Best measured result.** pr:teku#10225: Stated bottleneck only: synchronized get blocks all threads on a slow fallback; JMH benchmarks added, no numbers in text

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:571`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L571) block cache lock taken only for the map get; DB load and full-block rebuild happen outside the lock
- [`beacon_node/store/src/hot_cold_store.rs:82`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L82) state_cache is Mutex&lt;StateCache&gt; with short critical sections

**Sources.** [teku#2613](https://github.com/Consensys-Incorporated/teku/pull/2613), [teku#10225](https://github.com/Consensys-Incorporated/teku/pull/10225), [teku#10505](https://github.com/Consensys-Incorporated/teku/pull/10505), [teku#10506](https://github.com/Consensys-Incorporated/teku/pull/10506), [teku#10507](https://github.com/Consensys-Incorporated/teku/pull/10507), [prysm#4070](https://github.com/OffchainLabs/prysm/pull/4070)

</details>


<a id="other_caches-043"></a>
<details>
<summary><b>other_caches-043</b> Lock-free concurrent map instead of sharded dashmap — <i>not · low · M · cpu, latency</i></summary>

**Idea.** Replace sharded-lock concurrent maps (dashmap) with a lock-free, async-aware concurrent map (scc) for state maps and caches shared across threads, to reduce shard lock contention.

**Gap in Lighthouse.** Lighthouse does not use dashmap, so there is no sharded map to swap; replacing its RwLock caches with scc would be speculative.

**Impact.** Contention gain unproven; no mainnet hotspot known.

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.toml: no dashmap or scc dependency found
- [`beacon_node/beacon_chain/src`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src): caches use parking_lot RwLock/Mutex around LRU or maps

**Sources.** [grandine@f4dc7ddf9](https://github.com/grandinetech/grandine/commit/f4dc7ddf9924), [grandine#529](https://github.com/grandinetech/grandine/pull/529)

</details>


<a id="other_caches-044"></a>
<details>
<summary><b>other_caches-044</b> Fine-grained locks in rate limiter — <i>n/a · low · cpu</i></summary>

**Idea.** Use read-write locks on the rate limiter map, per-bucket locks and a separate heap lock instead of one global lock, to reduce contention.

**Impact.** The RPC rate limiter is owned by the network task and has no locks to split.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/rate_limiter.rs:485`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/rate_limiter.rs#L485) Limiter&lt;Key&gt; plain struct with FnvHashMap, mutated via &amp;mut self, no locks

**Sources.** [prysm#15277](https://github.com/OffchainLabs/prysm/pull/15277)

</details>


<a id="other_caches-045"></a>
<details>
<summary><b>other_caches-045</b> Configurable slasher span cache size — <i>partial · low · M · memory, latency</i></summary>

**Idea.** Make the slasher span cache size configurable so operators can cache more spans during long non-finality, trading memory for faster span updates.

**Gap in Lighthouse.** Span arrays are stored in the DB in chunks with no in-memory span cache whose size is configurable; only the attestation-root LRU size is configurable. Adding a span chunk cache config would need changes in slasher/src/array.rs and config.rs.

**Impact.** Only slasher operators during long non-finality would gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/config.rs:46`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/config.rs#L46) attestation_root_cache_size configurable
- [`slasher/src/database.rs:76`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L76) LRU of attestation roots
- [`slasher/src/config.rs:35-56`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/config.rs#L35-L56) chunk_size, validator_chunk_size, history_length

**Sources.** [prysm#7043](https://github.com/OffchainLabs/prysm/pull/7043)

</details>


<a id="other_caches-046"></a>
<details>
<summary><b>other_caches-046</b> Preallocate committee vector with true count — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** Preallocate the all-epoch committees vector with the actual committee count, not slots per epoch, to avoid reallocation while appending.

**Impact.** Landed (Lighthouse's own PR); trivial saving.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/committee_cache.rs:276-286`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L276-L286) get_all_beacon_committees uses Vec::with_capacity(epoch_committee_count())

**Skeptic check.** Confirmed the capacity is the true epoch committee count; this is the Lighthouse PR itself.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#4557](https://github.com/sigp/lighthouse/pull/4557)

</details>


<a id="other_caches-047"></a>
<details>
<summary><b>other_caches-047</b> In-memory cache for validator builder registrations — <i>partial · low · S · disk, latency</i></summary>

**Idea.** Keep validator builder (MEV) registrations in an in-memory cache by default instead of reading and writing them to the beacon database on every registration and proposal, and fetch proposer settings mid-epoch rather than at the epoch boundary. This removes DB round trips from block production.

**Gap in Lighthouse.** Registrations are cached in memory and only changed keys are re-published; Lighthouse has no DB write for them, so the main idea already holds. Mid-epoch proposer-settings fetch is not applicable.

**Impact.** Nothing meaningful remaining.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/preparation_service.rs:124`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/preparation_service.rs#L124) validator_registration_cache in-memory RwLock&lt;HashMap&gt;
- [`beacon_node/execution_layer/src/lib.rs:482`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L482) proposer_preparation_data in-memory Mutex&lt;HashMap&gt;

**Sources.** [prysm#12456](https://github.com/OffchainLabs/prysm/pull/12456), [prysm#12316](https://github.com/OffchainLabs/prysm/pull/12316)

</details>


<a id="other_caches-048"></a>
<details>
<summary><b>other_caches-048</b> Delete unviable blocks from orphan quarantine — <i>n/a · low · memory</i></summary>

**Idea.** When orphan blocks are marked unviable, also remove them from the orphan quarantine so they do not stay in memory.

**Impact.** Lighthouse has no orphan quarantine; failed lookups are dropped, so nothing stays in memory.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/single_block_lookup.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/single_block_lookup.rs): lookups are dropped on failure
- no orphan quarantine found in beacon_node

**Sources.** [nimbus#4782](https://github.com/status-im/nimbus-eth2/pull/4782)

</details>


<a id="other_caches-049"></a>
<details>
<summary><b>other_caches-049</b> Drop intermediate deposit data early — <i>n/a · low · memory</i></summary>

**Idea.** Generate deposits in a structure that drops intermediate values promptly, lowering peak memory (test harness).

**Impact.** Test-only deposit generation from 2019; the harness no longer exists. No mainnet effect.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/genesis/src/interop.rs:85`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/genesis/src/interop.rs#L85) build_genesis_state builds state directly, no 2019 test_harness deposit generator
- [`beacon_node/genesis/src/interop.rs:146`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/genesis/src/interop.rs#L146) drop_all_caches after build

**Sources.** [lighthouse@e76b5e1c3](https://github.com/sigp/lighthouse/commit/e76b5e1c3a0b)

</details>


<a id="other_caches-050"></a>
<details>
<summary><b>other_caches-050</b> Do not precompute next-epoch proposer cache — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** Drop the separate one-epoch-ahead proposer-indices precomputation once current-epoch shufflings already provide them, avoiding redundant work and memory.

**Impact.** No redundant next-epoch proposer computation: post-Fulu the next epoch's proposers are a copy out of proposer_lookahead, and pre-Fulu only the current epoch is primed.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:369-394`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L369-L394) next-epoch proposer cache priming only after the decision slot, served from the state
- [`consensus/types/src/state/beacon_state.rs:1673-1694`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1673-L1694) get_beacon_proposer_indices reads proposer_lookahead for current/next epoch post-Fulu
- [`consensus/types/src/state/beacon_state.rs:1655-1661`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1655-L1661) get_beacon_proposer_index reads proposer_lookahead post-Fulu

**Skeptic check.** The state-advance priming of the next epoch exists but costs a 32-entry read from the lookahead (with_proposer_cache is a no-op on hit), so there is no separate expensive precompute to drop.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#13385](https://github.com/OffchainLabs/prysm/pull/13385)

</details>


<a id="other_caches-051"></a>
<details>
<summary><b>other_caches-051</b> Recompute Merkle zero hashes instead of storing — <i>n/a · low · memory, disk</i></summary>

**Idea.** Do not serialize or store Merkle tree zero hashes; recompute or use a static table on construction since they are constant.

**Impact.** Lighthouse does not serialize Merkle zero hashes.

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.lock tree_hash/milhouse: zero hashes are static tables built on first use, not serialized with trees
- [`beacon_node/store/src/lib.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/lib.rs): states stored as SSZ/diffs, no tree internals

**Sources.** [lodestar@573650e40](https://github.com/ChainSafe/lodestar/commit/573650e40b41)

</details>


<a id="other_caches-052"></a>
<details>
<summary><b>other_caches-052</b> Array-backed maps for fork-keyed tables — <i>n/a · low · cpu, memory</i></summary>

**Idea.** Use array-backed enum maps/sets for tables keyed by fork or milestone enum instead of hash or tree maps, for faster lookup and less memory.

**Impact.** Rust enums with match need no enum-map; no hot table keyed by fork.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types): fork-keyed data uses ForkName enum matches and struct fields, not hash/tree maps

**Sources.** [teku#8591](https://github.com/Consensys-Incorporated/teku/pull/8591)

</details>


<a id="other_caches-053"></a>
<details>
<summary><b>other_caches-053</b> Proposer cache keyed by epoch and decision root — <i>implemented · low · S · cpu</i></summary>

**Idea.** Cache the proposer indices of an epoch keyed by (epoch, seed/decision root), pruned by epoch on update instead of a single LRU, so proposer selection runs once per fork and epoch and eviction is deterministic.

**Impact.** Already keyed by epoch and decision root and computed once per fork and epoch; LRU eviction of 16 tiny entries rather than epoch pruning has no measurable cost.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:1-9`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L1-L9) cache keyed by (epoch, decision block root)
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:26`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L26) CACHE_SIZE=16 LRU
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:14`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L14) OnceCell per key, so each key is computed once

**Skeptic check.** Verified the key and the compute-once OnceCell; the only difference from Prysm is LRU instead of epoch pruning, which does not matter for entries this small.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#13272](https://github.com/OffchainLabs/prysm/pull/13272), [prysm#4717](https://github.com/OffchainLabs/prysm/pull/4717), [prysm#13529](https://github.com/OffchainLabs/prysm/pull/13529)

</details>


<a id="other_caches-054"></a>
<details>
<summary><b>other_caches-054</b> Evict empty reprocess queue entries — <i>implemented · medium · S · memory</i></summary>

**Idea.** In the delayed-work reprocess queue, remove the per-block-root entry when its last queued attestation times out, so entries for never-imported blocks do not leak.

**Impact.** Per-root reprocess maps do not leak entries for never-imported blocks.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:1264-1284`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L1264-L1284) removes empty per-root Vec on expiry for both block and payload maps
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:1305-1316`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L1305-L1316) same for light client updates
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:1850`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L1850) regression test

**Skeptic check.** This is the Lighthouse PR itself; expiry removes the empty entry for attestations (block and payload maps) and LC updates. Earlier verdict correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#8065](https://github.com/sigp/lighthouse/pull/8065)

</details>


<a id="other_caches-055"></a>
<details>
<summary><b>other_caches-055</b> Cheap checks before shuffling in committee cache — <i>implemented · low · S · cpu</i></summary>

**Idea.** In committee cache construction, run cheap validity checks (validator count limits) before computing active indices and shuffling so failures return early.

**Impact.** Only affects invalid-input failure paths.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/committee_cache.rs:120-139`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L120-L139) initialized_unchecked checks ZeroSlotsPerEpoch and TooManyValidators before get_active_validator_indices, returns InsufficientValidators before get_seed/shuffle_list

**Skeptic check.** Verified the cheap checks run before active-index collection and shuffling in CommitteeCache::initialized_unchecked (Lighthouse's own PR #4556). Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#4556](https://github.com/sigp/lighthouse/pull/4556)

</details>


<a id="other_caches-056"></a>
<details>
<summary><b>other_caches-056</b> Finalize deposits only up to finalized state — <i>n/a · low · memory</i></summary>

**Idea.** Move deposits into the finalized deposit cache only up to the deposit count in the finalized state, not all deposits seen, so non-finalized deposits stay handled correctly.

**Impact.** The eth1 deposit cache is gone from Lighthouse, so there is nothing to finalize.

**Evidence (Lighthouse @ 928b61e719).**

- beacon_node has no eth1 or deposit cache module (ls beacon_node: no eth1 dir); deposits come from execution requests (Electra)

**Sources.** [prysm#7453](https://github.com/OffchainLabs/prysm/pull/7453)

</details>


<a id="other_caches-057"></a>
<details>
<summary><b>other_caches-057</b> Fixed growth step for pubkey cache — <i>not · low · S · memory, latency</i></summary>

**Idea.** Grow the validator pubkey cache by a fixed step instead of doubling capacity, avoiding a huge copy and over-reservation at mainnet registry size.

**Gap in Lighthouse.** validator_pubkey_cache load_from_store pushes without capacity and import_new_pubkeys uses Vec::reserve (amortized doubling); use reserve_exact or preallocate from the state's validator count.

**Impact.** Only matters at startup/rare growth: avoids one transient copy of a few hundred MB and some over-reserved memory.

**Best measured result.** commit:lodestar@133ef248a5e6: Doubling would copy ~450MB at mainnet scale

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:111`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L111) reserve(validator_keys.len()) on Vec (amortized, can still double) and HashMap
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:57`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L57) load_from_store pushes with no reserve

**Sources.** [lodestar@133ef248a](https://github.com/ChainSafe/lodestar/commit/133ef248a5e6)

</details>


<a id="other_caches-058"></a>
<details>
<summary><b>other_caches-058</b> Free pre-genesis state after genesis — <i>n/a · low · memory</i></summary>

**Idea.** Release the pre-genesis state and chainstart deposits from memory once the genesis state is built.

**Impact.** No pre-genesis state or chainstart deposit flow exists in current Lighthouse.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/genesis/src/lib.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/genesis/src/lib.rs) and interop.rs: no eth1 genesis service; genesis loaded from a checkpoint/genesis.ssz

**Sources.** [prysm#4656](https://github.com/OffchainLabs/prysm/pull/4656)

</details>


<a id="other_caches-059"></a>
<details>
<summary><b>other_caches-059</b> Prune proposer cache once per duties request — <i>n/a · low · S · cpu</i></summary>

**Idea.** Prune the proposer-id cache once per duties request instead of once per matched validator inside the loop.

**Impact.** None; no per-validator prune exists.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:7`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L7) LRU cache, never explicitly pruned per request

**Sources.** [prysm#12996](https://github.com/OffchainLabs/prysm/pull/12996)

</details>


<a id="other_caches-060"></a>
<details>
<summary><b>other_caches-060</b> Per-period cache of validators&#x27; sync committee positions — <i>not · low · M · cpu</i></summary>

**Idea.** Compute once per sync committee period each validator index's positions/subcommittee indices in the current and next sync committee and keep them in the state caches. Is-in-committee checks, subnet computation, selection-proof validation, gossip validation and aggregation then are lookups instead of scanning committee pubkeys.

**Gap in Lighthouse.** Add a per-period cache (validator_index -&gt; subnet positions, plus the committee index vector) stored in BeaconState caches or BeaconChain; use it in verify gossip sync messages, process_sync_aggregate (get_sync_committee_indices) and the HTTP duties.

**Impact.** Cuts a 512-key scan per gossiped sync message (thousands per slot on mainnet) and 512 hashtrie lookups per block; likely sub-ms per slot of CPU, small but cheap.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/sync_committee_verification.rs:472`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/sync_committee_verification.rs#L472) subcommittee_positions_for_public_key per message
- [`consensus/types/src/sync_committee/sync_committee.rs:70`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/sync_committee/sync_committee.rs#L70) iterates all 512 pubkeys comparing 48 byte keys
- [`consensus/types/src/state/beacon_state.rs:1753`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1753) get_sync_committee_indices does 512 pubkey_cache lookups per block (altair/sync_committee.rs:50)
- http_api/src/sync_committees.rs:307 same scan per duty

**Sources.** [teku#3845](https://github.com/Consensys-Incorporated/teku/pull/3845), [prysm#9074](https://github.com/OffchainLabs/prysm/pull/9074), [prysm#8884](https://github.com/OffchainLabs/prysm/pull/8884), [prysm#9317](https://github.com/OffchainLabs/prysm/pull/9317)

</details>


<a id="other_caches-061"></a>
<details>
<summary><b>other_caches-061</b> Feed light client server only from new head blocks — <i>partial · medium · M · cpu</i></summary>

**Idea.** Compute and import light client server data only for blocks that become the new head, not for every imported block. Blocks that never become canonical then cost no light client work.

**Gap in Lighthouse.** Neither cache_state_data nor the update producer is gated on the block becoming the new head; only a recency filter (&lt;32 slots) and a slot-based is_latest check exist. Gate both (or move them) to run after recompute_head when the block is the canonical head, or compute proofs lazily on demand.

**Impact.** Only on --light-client-server nodes; avoids per-block proof computation and update recompute (DB block reads, sync committee store writes) for non-canonical blocks, a few percent of blocks.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:4786-4796`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4786-L4796) cache_state_data runs for every imported block (no head check)
- [`beacon_node/beacon_chain/src/light_client_server_cache.rs:59-75`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_server_cache.rs#L59-L75) cache_state_data computes finality/sync-committee proofs via LightClientCachedData::from_state
- [`beacon_node/beacon_chain/src/light_client_server_cache.rs:467-477`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_server_cache.rs#L467-L477) from_state computes three merkle proofs per block
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5176-5190`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5176-L5190) producer event sent for any block with delay &lt; 32 slots, not only new heads
- [`beacon_node/beacon_chain/src/light_client_server_cache.rs:141-160`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_server_cache.rs#L141-L160) updates only kept if is_latest by (attested_slot, signature_slot), a slot heuristic rather than fork-choice head

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [lodestar#3967](https://github.com/ChainSafe/lodestar/pull/3967)

</details>


<a id="other_caches-062"></a>
<details>
<summary><b>other_caches-062</b> In-memory execution payload envelope store for hot chain — <i>not · low · M · memory, latency</i></summary>

**Idea.** Keep execution payload envelopes for the recent (hot) chain in an in-memory store so envelopes-by-range requests are served without database reads.

**Gap in Lighthouse.** Add an in-memory map of recent envelopes (summary + body) filled on import and pruned at finalization; consult it in the envelope streamer before get_payload_envelope_summary/get_payload_body.

**Impact.** Saves hot DB reads when serving envelopes-by-range to peers, only on Gloas and mostly for recent ranges; small gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/payload_envelope_streamer/beacon_chain_adapter.rs:30-41`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_streamer/beacon_chain_adapter.rs#L30-L41) reads summary and body from store
- [`beacon_node/store/src/hot_cold_store.rs:703-719`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L703-L719) hot_db reads
- [`beacon_node/beacon_chain/src/pending_payload_envelopes.rs:87`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_envelopes.rs#L87) only holds unpublished envelopes

**Sources.** [teku#10374](https://github.com/Consensys-Incorporated/teku/pull/10374)

</details>


<a id="other_caches-063"></a>
<details>
<summary><b>other_caches-063</b> Keep aggregated attestation payloads in memory, not DB — <i>n/a · low · S · memory</i></summary>

**Idea.** Hold aggregated attestation payloads in an in-memory buffer instead of writing and reading them through the database, removing DB round trips on the aggregation path.

**Impact.** Lighthouse aggregates in memory already; the ethlambda DB path does not exist.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/lib.rs:54`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L54) attestations are held in memory (AttestationMap), no DB path

**Sources.** [ethlambda#181](https://github.com/lambdaclass/ethlambda/pull/181)

</details>


<a id="other_caches-064"></a>
<details>
<summary><b>other_caches-064</b> Cached pubkey-to-index map instead of registry scans — <i>implemented · high · S · cpu</i></summary>

**Idea.** Maintain a pubkey-to-validator-index map built in one pass and extended incrementally from the last known index (indices never change), instead of linearly scanning the validator registry for each pubkey lookup.

**Impact.** O(1) pubkey lookups with incremental extension on block import, deposits, epoch processing and the API.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:26`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L26) indices HashMap&lt;PublicKeyBytes,usize&gt;
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:87-101`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L87-L101) import_new_pubkeys iter_from(self.pubkeys.len())
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:189`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L189) get_index
- [`consensus/types/src/state/beacon_state.rs:1105`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1105) get_validator_index via per-state PubkeyCache
- [`consensus/types/src/state/beacon_state.rs:2979-2991`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2979-L2991) update_pubkey_cache extends from start_index
- [`beacon_node/http_api/src/validator/mod.rs:47-63`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L47-L63) pubkey_to_validator_index uses global cache

**Skeptic check.** Both the global ValidatorPubkeyCache and the per-state PubkeyCache map pubkey to index and extend incrementally; deposit and pending-deposit paths use them. Only Gloas builder-registry lookups (process_operations.rs:934-937, 991-994) scan linearly, but that registry is small and outside this idea's scope.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#3325](https://github.com/Consensys-Incorporated/teku/pull/3325), [teku#1426](https://github.com/Consensys-Incorporated/teku/pull/1426)

</details>


<a id="other_caches-065"></a>
<details>
<summary><b>other_caches-065</b> Single pubkey index map, no unfinalized pubkey cache — <i>partial · low · M · memory, cpu</i></summary>

**Idea.** Do not keep a separate per-fork unfinalized pubkey-to-index cache; since validator indices assigned by deposit processing cannot change on reorg, add new pubkeys directly to one global index map.

**Gap in Lighthouse.** State transition (get_validator_index, update_pubkey_cache, single_pass process_pending_deposits, verify_deposit) keeps a second per-state persistent pubkey map instead of using the one global ValidatorPubkeyCache. That map is cloned with each state and rebuilt from scratch (about 2M HAMT inserts) when a state is loaded without caches (build_caches, reconstruct).

**Impact.** Saves some memory per cached state and avoids full rebuilds on cold state loads. Clones are already cheap because the map is structurally shared, so the gain is small.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:26`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L26) single global map in the chain
- [`consensus/types/src/state/pubkey_cache.rs:1-14`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/pubkey_cache.rs#L1-L14) per-state PubkeyCache (rpds HashTrieMap) carried by every BeaconState
- [`consensus/types/src/state/beacon_state.rs:1105-1111`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1105-L1111) get_validator_index uses the per-state map
- [`consensus/types/src/state/beacon_state.rs:2979-2997`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2979-L2997) update_pubkey_cache / drop_pubkey_cache
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:165`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L165),406 epoch processing uses the per-state map
- [`consensus/types/src/state/beacon_state.rs:2759`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2759) build_caches rebuilds it
- [`beacon_node/store/src/reconstruct.rs:129`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/reconstruct.rs#L129) build_caches on reconstructed state

**Skeptic check.** The earlier evidence looked only at ValidatorPubkeyCache and missed the per-state PubkeyCache in BeaconState. That per-state map is the same pattern as the Lodestar per-state immutable map that #7230 removed, although Lighthouse has no separate unfinalized/finalized split.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lodestar#7230](https://github.com/ChainSafe/lodestar/pull/7230)

</details>


<a id="other_caches-066"></a>
<details>
<summary><b>other_caches-066</b> Cache sync committee subnet ids per validator — <i>n/a · low · S · cpu</i></summary>

**Idea.** Cache the sync committee subnet ids for each validator per period so duty and subscription handling read them from a cache instead of recomputing from the state.

**Impact.** Subnet id is index/subcommittee_size taken from request data, no state lookup, so nothing worth caching.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/subnet_service/mod.rs:282`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L282) computes from indices supplied in the request
- [`consensus/types/src/sync_committee/sync_subnet_id.rs:45`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/sync_committee/sync_subnet_id.rs#L45) compute is one integer division per index

**Sources.** [prysm#9089](https://github.com/OffchainLabs/prysm/pull/9089), [prysm#9350](https://github.com/OffchainLabs/prysm/pull/9350)

</details>


<a id="other_caches-067"></a>
<details>
<summary><b>other_caches-067</b> Iteration-safe bounded maps in the operation pool — <i>implemented · low · S · cpu</i></summary>

**Idea.** Use a bounded map/set that is safe and consistent to iterate (copy-on-write or lock-based) for operation pool caches, instead of a weakly consistent concurrent wrapper.

**Impact.** Iteration is consistent under the lock.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/lib.rs:49-70`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L49-L70) every pool map/set is a parking_lot RwLock over HashMap/HashSet; no weakly consistent concurrent maps (no DashMap in beacon_node)

**Skeptic check.** Confirmed that every operation pool collection uses lock-based access, so iteration during packing is consistent. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#5616](https://github.com/Consensys-Incorporated/teku/pull/5616)

</details>


<a id="other_caches-068"></a>
<details>
<summary><b>other_caches-068</b> Size shuffling cache for forks; compute each once — <i>implemented · medium · S · cpu, memory</i></summary>

**Idea.** Size the committee shuffling cache to hold several epochs across many forks (and long non-finality), and make a miss compute-once so concurrent requesters wait instead of recomputing. Late attestations and forks then do not evict and recompute shufflings repeatedly.

**Impact.** Each shuffling computed once; concurrent requesters wait on the promise.

**Best measured result.** shuffling ~6% CPU, ~20 computes/epoch reduced to 1 (pr:teku#5892)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:25`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L25) DEFAULT_CACHE_SIZE=16
- [`beacon_node/src/cli.rs:675`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L675) --shuffling-cache-size configurable
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:256`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L256) prune_cache never evicts head shuffling ids
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:362-374`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L362-L374) miss creates promise under write lock; waiters block on it

**Skeptic check.** Compute-once promise and head-protected pruning verified; size is configurable. MAX_CONCURRENT_PROMISES=2 drops some attestations under heavy forking, a deliberate memory trade-off rather than a missing mechanism.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#7018](https://github.com/OffchainLabs/prysm/pull/7018), [teku#5892](https://github.com/Consensys-Incorporated/teku/pull/5892)

</details>


<a id="other_caches-069"></a>
<details>
<summary><b>other_caches-069</b> Dependent-root keyed shuffling cache with lookahead — <i>implemented · medium · S · cpu, memory, latency</i></summary>

**Idea.** Key the shuffling cache by the dependent (decision) root, separate from larger per-epoch data, and compute it ahead when the determining block is processed. Attestations on non-canonical forks then need no state replay, and forks sharing a dependent root share one shuffling.

**Impact.** Forks sharing a decision root share one Arc&lt;CommitteeCache&gt;; attestations hit the cache without state replay.

**Best measured result.** lower memory by sharing shufflings between EpochRefs of same dependent root (no numbers) (pr:nimbus#3990)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:143`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L143) keyed by AttestationShufflingId (epoch, decision block)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5211`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5211) primed at block import for current and next epoch
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:397-411`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L397-L411) next-epoch shuffling inserted ahead

**Skeptic check.** Shuffling cache is separate from states, keyed by decision root, and filled at import and state advance; earlier verdict correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#3990](https://github.com/status-im/nimbus-eth2/pull/3990)

</details>


<a id="other_caches-070"></a>
<details>
<summary><b>other_caches-070</b> Never evict head epoch shufflings from cache — <i>implemented · medium · S · cpu</i></summary>

**Idea.** Evict shuffling cache entries by lowest epoch rather than LRU, and pin the head's previous, current and next epoch shufflings so they are never evicted and recomputed.

**Impact.** Head previous/current/next shufflings are never evicted.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:252-285`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L252-L285) prune_cache sorts by shuffling_epoch and skips head_shuffling_ids
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:309`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L309) update_head_shuffling_ids
- [`beacon_node/beacon_chain/src/canonical_head.rs:1546`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1546) head ids updated on every head change

**Skeptic check.** Verified lowest-epoch eviction with head pinning, and that canonical_head updates the pinned ids on each fork-choice head change. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#4296](https://github.com/sigp/lighthouse/pull/4296)

</details>


<a id="other_caches-071"></a>
<details>
<summary><b>other_caches-071</b> Persist pubkeys uncompressed to skip startup decompression — <i>implemented · medium · S · startup, cpu</i></summary>

**Idea.** Store validator pubkeys in uncompressed (or checksummed flat snapshot) form on disk and load them directly at startup, avoiding decompressing every BLS key on restart.

**Impact.** Restart skips per-key decompression; what is left is one KV read per validator plus a cheap compress() for the index map.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:231-242`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L231-L242) DatabasePubkey::from_pubkey stores serialize_uncompressed, as_pubkey uses deserialize_uncompressed
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:55-79`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L55-L79) load_from_store reads stored uncompressed keys
- [`crypto/bls/src/impls/blst.rs:141-152`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L141-L152) deserialize_uncompressed -&gt; blst PublicKey::deserialize (on-curve only, no decompression sqrt)
- ~/.cargo/registry/src/*/blst-0.3.17/src/lib.rs:876-889

**Skeptic check.** Verified the on-disk format is uncompressed and the load path does no square-root decompression. The earlier evidence was correct; LH uses per-index KV rows, not one flat snapshot, but the effect the idea targets is there.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#2639](https://github.com/status-im/nimbus-eth2/pull/2639)

</details>


<a id="other_caches-072"></a>
<details>
<summary><b>other_caches-072</b> Parallel pubkey decompression when building pubkey cache — <i>implemented · low · S · cpu, startup</i></summary>

**Idea.** When building the validator pubkey cache from a fresh checkpoint state, decompress the pubkeys in parallel on a thread pool, since serial decompression of every key dominates startup.

**Impact.** Checkpoint-start cache build is parallel (lighthouse#8451).

**Best measured result.** Sepolia validator_pubkey_cache_new 109.64ms -&gt; 21ms; Hoodi import 12.77s vs &gt;120s timeout (pr:lighthouse#8451)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:36-51`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L36-L51) ValidatorPubkeyCache::new calls import_new_pubkeys on an empty cache
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:117`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L117) is_initial_import
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:143-159`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L143-L159) into_par_iter decompression

**Skeptic check.** This idea is Lighthouse's own PR, and the code is in the base checkout. Incremental imports during block import stay serial, which is correct because they are only a few deposits.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#8451](https://github.com/sigp/lighthouse/pull/8451)

</details>


<a id="other_caches-073"></a>
<details>
<summary><b>other_caches-073</b> Lazy TTL expiry without per-cache sweeper threads — <i>n/a · low · S · memory, cpu</i></summary>

**Idea.** Implement TTL caches that check expiry on read and insert instead of running a background sweeper thread per cache, so per-peer or per-request caches cost no thread and do not leak.

**Gap in Lighthouse.** No per-cache sweeper threads exist; expiry is driven by async DelayQueue/HashSetDelay.

**Impact.** None; no thread cost to remove.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/gossip_cache.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/gossip_cache.rs): uses delay-queue polled in the swarm task, no thread per cache

**Sources.** [caplin#24022](https://github.com/erigontech/erigon/pull/24022)

</details>


<a id="other_caches-074"></a>
<details>
<summary><b>other_caches-074</b> Lazy dirty-flag rehashing of deposit merkle tree — <i>n/a · low · S · cpu</i></summary>

**Idea.** Store the deposit merkle tree as full levels and mark nodes dirty on push, recomputing hashes only when a root or proof is requested, so batched pushes hash each node once.

**Gap in Lighthouse.** Lighthouse has no deposit merkle tree cache any more (eth1 deposit tree removed).

**Impact.** Nothing.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/metrics.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/metrics.rs) only mention of deposit cache; no eth1 DepositCache in tree

**Sources.** [lodestar@74677778b](https://github.com/ChainSafe/lodestar/commit/74677778bd61)

</details>


<a id="other_caches-075"></a>
<details>
<summary><b>other_caches-075</b> Configurable light client data retention period — <i>not · low · S · sync, startup</i></summary>

**Idea.** Make the number of sync committee periods of light client data the beacon node keeps configurable, so operators can retain fewer and shorten LC data computation during import and sync.

**Gap in Lighthouse.** Add a CLI flag and ChainConfig field for number of periods kept, and have the LC update storing/pruning (store_light_client_update, recompute_and_cache_light_client_updates) skip or delete older periods.

**Impact.** Small: LC server work is skipped entirely when disabled (enable_light_client_server); a retention knob would only trim DB size and per-block LC work for operators who keep it on. Gain unmeasured upstream.

**Best measured result.** lowering below default speeds up import (no numbers) (pr:nimbus#3799)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/chain_config.rs:88`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/chain_config.rs#L88) only enable_light_client_server bool
- [`beacon_node/store/src/hot_cold_store.rs:831-885`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L831-L885) get_light_client_update(s) read per period, no retention setting
- [`beacon_node/src/cli.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs): no LC retention flag

**Sources.** [nimbus#3799](https://github.com/status-im/nimbus-eth2/pull/3799)

</details>


<a id="other_caches-076"></a>
<details>
<summary><b>other_caches-076</b> Single-flight active validator count, fetched only when needed — <i>n/a · low · S · cpu, disk, startup</i></summary>

**Idea.** Compute the active validator count under a lock so one cache miss blocks other readers instead of each loading the state from disk, and fetch it only for gossip topics that need it.

**Gap in Lighthouse.** Count comes from the already-cached head state committee cache; no DB state load on a miss.

**Impact.** Nothing to save.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/service.rs:832`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L832) reads count from cached head
- [`beacon_node/beacon_chain/src/canonical_head.rs:389`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L389) active_validator_count from cached committee cache

**Sources.** [prysm#15955](https://github.com/OffchainLabs/prysm/pull/15955)

</details>


<a id="other_caches-077"></a>
<details>
<summary><b>other_caches-077</b> Pubkey cache reads that do not serialize on LRU recency — <i>n/a · low · S · latency, cpu</i></summary>

**Idea.** For the pubkey cache, avoid an LRU whose Get mutates recency under an exclusive lock: use a plain map with a read-write lock when all keys fit, or update recency asynchronously, so concurrent readers do not contend.

**Gap in Lighthouse.** Pubkey cache is a plain Vec/map behind an RwLock; reads do not mutate recency.

**Impact.** Nothing.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:1629`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1629) validator_pubkey_cache.read() RwLock, no LRU

**Sources.** [prysm#12414](https://github.com/OffchainLabs/prysm/pull/12414), [prysm#12476](https://github.com/OffchainLabs/prysm/pull/12476)

</details>


<a id="other_caches-078"></a>
<details>
<summary><b>other_caches-078</b> Don&#x27;t block pubkey cache readers while adding new keys — <i>partial · low · S · latency, cpu</i></summary>

**Idea.** When block import adds new validators to the pubkey cache, hold only a read (upgradable) lock or a separate lock while decompressing and persisting new keys, upgrading to write only when needed, so attestation verification readers are not blocked.

**Gap in Lighthouse.** Upgradable read and DB write deferral exist, but upgrade happens before decompression, so readers are blocked during decompression of new keys. Decompress the new keys (from state.validators().iter_from(len)) while only holding the upgradable guard, then upgrade just to push into pubkeys/pubkey_bytes/indices in import_new_pubkeys.

**Impact.** Slightly shorter write-lock hold on blocks that add validators (a few per block, decompression is tens of microseconds each); small attestation verification latency gain.

**Best measured result.** small improvement in attestation verification times (pr:lighthouse#6190)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:4487`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4487) upgradable_read then upgrade only if state.validators().len() &gt; cache.len()
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:91-101`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L91-L101),128-131 import and decompress run inside &amp;mut self; DB write deferred as StoreOp

**Sources.** [lighthouse#2381](https://github.com/sigp/lighthouse/pull/2381), [lighthouse#6190](https://github.com/sigp/lighthouse/pull/6190)

</details>


<a id="other_caches-079"></a>
<details>
<summary><b>other_caches-079</b> Remove timeout locks on shared caches — <i>implemented · low · S · latency, cpu</i></summary>

**Idea.** Use plain blocking read-write locks (or allow disabling lock timeouts) on attestation, pubkey and eth1 caches instead of timeout locks, so slow operations do not error and retry, wasting work and livelocking slow hardware.

**Impact.** Timeout locks are gone from the hot paths. The 30s timeout left in backfill only matters on very slow hardware.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/historical_blocks.rs:359`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_blocks.rs#L359) only remaining try_read_for (backfill, 30s)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1631-1700`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1631-L1700) pubkey cache accessed with blocking read()

**Skeptic check.** A grep for try_read_for/try_write_for/TimeoutRwLock in beacon_node finds only the backfill pubkey-cache read. Attestation and pubkey caches on gossip and import use blocking locks. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#2714](https://github.com/sigp/lighthouse/pull/2714), [lighthouse#6048](https://github.com/sigp/lighthouse/pull/6048)

</details>


<a id="other_caches-080"></a>
<details>
<summary><b>other_caches-080</b> Native first/last DB lookups instead of iterators — <i>n/a · low · S · disk, latency</i></summary>

**Idea.** Use the key-value store's native first()/last() lookups to find the lowest or highest key instead of creating an iterator and calling next()/next_back(), which is cheaper on B-tree stores.

**Gap in Lighthouse.** No code path finds a lowest/highest key through an iterator; LevelDB has no native first/last anyway, redb range is used for iteration.

**Impact.** Negligible.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/database/leveldb_impl.rs:204`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/leveldb_impl.rs#L204) iter_column_from seeks; no min/max key lookups via next()/next_back found
- [`beacon_node/store/src/hot_cold_store.rs:3339`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3339) only .next() use

**Sources.** [lighthouse#6481](https://github.com/sigp/lighthouse/pull/6481)

</details>


<a id="other_caches-081"></a>
<details>
<summary><b>other_caches-081</b> Cache unfinalized light client updates, flush on finality — <i>not · low · M · disk, memory</i></summary>

**Idea.** Keep light client updates for the non-finalized period in an in-memory per-branch cache, serve canonical updates from it, and write to cold storage only on finalization, avoiding DB writes for fork data.

**Gap in Lighthouse.** Updates are recomputed per block and written to the DB; Lighthouse would need a per-branch in-memory cache in recompute_and_cache_updates flushed at finalization.

**Impact.** Saves small DB writes per block for fork data; only matters for nodes serving light clients.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/light_client_server_cache.rs:243`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_server_cache.rs#L243) keeps only latest update per period, reads DB on miss
- [`beacon_node/store/src/hot_cold_store.rs:831`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L831) get_light_client_update from DB

**Sources.** [prysm#15585](https://github.com/OffchainLabs/prysm/pull/15585)

</details>


<a id="other_caches-082"></a>
<details>
<summary><b>other_caches-082</b> Oldest-first eviction of slasher span cache — <i>n/a · low · L · memory</i></summary>

**Idea.** Evict the oldest epochs from the slasher's in-memory span cache when pruning, and flush all spans to disk on shutdown, bounding memory without losing spans.

**Gap in Lighthouse.** Lighthouse slasher design differs (chunked on-disk arrays, batch updates), so the prysm eviction does not map.

**Impact.** Only affects slasher users.

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/array.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/array.rs): spans stored in a database per chunk, no prysm-style in-memory span map

**Sources.** [prysm#5953](https://github.com/OffchainLabs/prysm/pull/5953)

</details>


<a id="other_caches-083"></a>
<details>
<summary><b>other_caches-083</b> Persist light client sync progress across restarts — <i>n/a · low · S · startup</i></summary>

**Idea.** Persist the light client's latest finalized header and sync committee to disk so a restart resumes from it and skips the slow bootstrap step.

**Gap in Lighthouse.** n/a: Lighthouse has no light client sync client (only a server that already persists updates via store_light_client_update).

**Impact.** None; no client-side LC sync to resume.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/light_client_server_cache.rs:195`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_server_cache.rs#L195) server persists updates; no LC client in beacon_node

**Sources.** [nimbus#4371](https://github.com/status-im/nimbus-eth2/pull/4371)

</details>


<a id="other_caches-084"></a>
<details>
<summary><b>other_caches-084</b> Persist eth1 deposit and block caches on shutdown — <i>n/a · low · S · startup, sync</i></summary>

**Idea.** Save the eth1 deposit and eth1 block caches to disk on shutdown and reload them at startup, so they need not be re-downloaded and rebuilt from the execution node.

**Gap in Lighthouse.** n/a: Lighthouse removed the eth1 deposit/block caches; deposits come from state and execution requests.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- beacon_node/ has no eth1 module; [`consensus/state_processing/src/builder_deposits_cache.rs:42`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/builder_deposits_cache.rs#L42) only builder deposit sig cache

**Sources.** [lighthouse#760](https://github.com/sigp/lighthouse/pull/760)

</details>


<a id="other_caches-085"></a>
<details>
<summary><b>other_caches-085</b> Preallocate maps; copy only fork data for chain info — <i>n/a · low · S · memory, cpu</i></summary>

**Idea.** Preallocate map capacity when the final size is known, and when serving chain info copy only the fork field rather than cloning the whole beacon state.

**Gap in Lighthouse.** n/a: Go-specific map prealloc and state copy; Lighthouse's state_id::fork returns only the fork, and Rust collections are sized explicitly where hot.

**Impact.** Negligible.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/state_id.rs:165`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L165) fork() reads only the fork

**Sources.** [prysm#5099](https://github.com/OffchainLabs/prysm/pull/5099)

</details>


<a id="other_caches-086"></a>
<details>
<summary><b>other_caches-086</b> Precompute own committee duties per dependent root — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Cache the node's own validators' committee membership keyed by dependent root and do the precomputation and pruning on a dedicated executor, off the block/attestation processing path.

**Impact.** Lighthouse's separate VC already scopes own duties by dependent root and computes them in background tasks, so none of this runs on the BN block or attestation path.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:323-325`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L323-L325) AttesterMap keyed by epoch with DependentRoot
- [`validator_client/validator_services/src/duties_service.rs:1253-1273`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1253-L1273) refetch only on (epoch, dependent_root) conflict
- [`validator_client/validator_services/src/duties_service.rs:1369-1384`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1369-L1384) selection proofs computed in executor.spawn background task
- [`validator_client/validator_services/src/duties_service.rs:1206-1212`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1206-L1212) pruning by HISTORICAL_DUTIES_EPOCHS in the poll task
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:397-411`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L397-L411) BN shuffling cache primed per AttestationShufflingId off the import path

**Second check.** Earlier review searched only the beacon node; Grandine's integrated validator maps to Lighthouse's validator_client DutiesService, which caches own duties keyed by (epoch, dependent_root), precomputes selection proofs in spawned tasks and prunes old epochs.

**Skeptic check.** The grandine PR has no diff in the corpus; the title and description match what the LH VC duties service does. Upheld.

**Verdict history.** not (checked) → implemented (refuted) → implemented (skeptic)

**Sources.** [grandine#576](https://github.com/grandinetech/grandine/pull/576)

</details>


<a id="other_caches-087"></a>
<details>
<summary><b>other_caches-087</b> Check cache before recompute or reinsert — <i>implemented · low · S · cpu, sync</i></summary>

**Idea.** Before computing a value for a cache (proposer indices, committees, pubkeys), check whether the key already exists and return early, skipping the duplicate computation, validation and locked write.

**Impact.** Duplicate proposer, shuffling and pubkey computations are skipped.

**Best measured result.** initial sync up to 20% faster (pr:prysm#8096)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:133-143`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L133-L143) get_or_insert_key returns a OnceCell
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:185-195`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L185-L195) with_proposer_cache get_or_try_init computes once, even across threads
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:158`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L158) insert skips existing key
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5220-5225`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5220-L5225) import_block_update_shuffling_cache_fallible checks contains() before build_committee_cache
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:230-244`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L230-L244) insert_committee_cache keeps existing Committee
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4490`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4490) pubkey cache write lock only when new validators

**Skeptic check.** prysm#8096 skipped recomputing proposer indices on a cache hit. LH's OnceCell-based with_proposer_cache does this and also deduplicates concurrent misses, and block import checks the shuffling cache before it builds committees.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#8096](https://github.com/OffchainLabs/prysm/pull/8096), [prysm#4719](https://github.com/OffchainLabs/prysm/pull/4719), [lodestar@2e25d97fa](https://github.com/ChainSafe/lodestar/commit/2e25d97fadfb)

</details>


<a id="other_caches-088"></a>
<details>
<summary><b>other_caches-088</b> Proposer index from pre-advanced next-slot state — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** When validating gossip blocks, read the expected proposer index from a pre-advanced next-slot state cache instead of processing slots on a state copy for each call.

**Impact.** The gossip block proposer check is a cache lookup. The state is loaded only on a miss, and then from the state cache, which already holds the advanced state.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1025-1050`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1025-L1050) gossip proposer from with_proposer_cache keyed by shuffling decision root; parent state loaded only in the miss closure
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:355-394`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L355-L394) pre-advanced head state primes current and next epoch proposers
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:175-195`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L175-L195) state_provider called only when the OnceCell is empty

**Skeptic check.** Verified on the gossip block path. LH goes further than prysm#9709: the state advance timer fills the cache ahead of time, so it does not process slots on a state copy.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#9709](https://github.com/OffchainLabs/prysm/pull/9709)

</details>


<a id="other_caches-089"></a>
<details>
<summary><b>other_caches-089</b> Derive payload timeliness committee from cached committees — <i>implemented · low · S · cpu</i></summary>

**Idea.** Compute the ePBS payload timeliness committee from the already-cached beacon committees of the slot instead of recomputing the shuffling.

**Impact.** PTC is never recomputed from a fresh shuffling.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:3591-3627`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3591-L3627) get_ptc reads stored ptc_window
- [`consensus/types/src/state/beacon_state.rs:3632-3661`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3632-L3661) compute_ptc_with_cache builds PTC from committee_cache.get_beacon_committees_at_slot
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:566`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L566) epoch processing fills ptc_window with the lookahead committee cache
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:50-70`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L50-L70) CachedPTCs stored next to committee cache for gossip

**Skeptic check.** Verified that the PTC is derived from cached beacon committees and stored. A separate inefficiency exists: compute_ptc_duties (beacon_chain.rs:1767-1809) calls get_ptc_assignment per validator, which is O(N*slots*PTC) and has a TODO. It reads ptc_window and does not reshuffle, so it is not this idea.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#13969](https://github.com/OffchainLabs/prysm/pull/13969), [nimbus#9385](https://github.com/status-im/nimbus-eth2/pull/9385)

</details>


<a id="other_caches-090"></a>
<details>
<summary><b>other_caches-090</b> Primitive int collections for validator indices — <i>n/a · low · S · memory, cpu</i></summary>

**Idea.** Use primitive-specialized int maps, sets and lists (no boxed integer objects) for validator indices, subnets and similar collections, including those passed across APIs, to cut per-entry allocation and GC pressure.

**Gap in Lighthouse.** n/a: JVM boxed integers; Rust uses unboxed u64/usize collections.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context.rs:170`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L170) plain Vec&lt;usize&gt;

**Sources.** [teku#4984](https://github.com/Consensys-Incorporated/teku/pull/4984), [teku#4991](https://github.com/Consensys-Incorporated/teku/pull/4991)

</details>


<a id="other_caches-091"></a>
<details>
<summary><b>other_caches-091</b> Prune the execution payload bid pool in production — <i>implemented · low · S · memory</i></summary>

**Idea.** Actually prune old entries from the ePBS execution payload bid pool during normal operation (not only in tests) so old bids do not accumulate.

**Impact.** Old bids do not accumulate.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:7480`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7480) gossip_verified_payload_bid_cache.prune(slot) in per_slot_task, outside the sync-gated section
- [`beacon_node/beacon_chain/src/payload_bid_verification/payload_bid_cache.rs:135-139`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_bid_verification/payload_bid_cache.rs#L135-L139) prune split_off on highest_bid and seen_builder_bids
- [`beacon_node/builder_client/src/bid_streams.rs:462-466`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/builder_client/src/bid_streams.rs#L462-L466) bid stream prune retain by slot

**Skeptic check.** Confirmed production per-slot pruning of both BTreeMaps in the bid cache, and that the builder bid streams also prune by slot. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#8610](https://github.com/status-im/nimbus-eth2/pull/8610)

</details>


<a id="other_caches-092"></a>
<details>
<summary><b>other_caches-092</b> Prune payload envelope input cache after each import — <i>implemented · low · S · memory</i></summary>

**Idea.** Prune the payload-envelope (data availability input) cache after every block import, not only at synced next-slot preparation, so it cannot grow without bound during sync on a non-finalizing network.

**Impact.** Cache is hard-capped at 32 entries, so it cannot grow without bound during sync on a non-finalizing network.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/pending_payload_cache/mod.rs:55`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/mod.rs#L55) AVAILABILITY_CACHE_CAPACITY = 32
- [`beacon_node/beacon_chain/src/pending_payload_cache/mod.rs:118`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/mod.rs#L118) LruCache::new(AVAILABILITY_CACHE_CAPACITY)
- [`beacon_node/beacon_chain/src/pending_payload_cache/mod.rs:662`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/mod.rs#L662) do_maintenance by cutoff epoch
- [`beacon_node/beacon_chain/src/canonical_head.rs:1656`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1656) maintenance on finalization

**Skeptic check.** Lighthouse does not prune per import, but the fixed-capacity LRU (32) gives the same effect the idea targets: bounded memory. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#9509](https://github.com/ChainSafe/lodestar/pull/9509)

</details>


<a id="other_caches-093"></a>
<details>
<summary><b>other_caches-093</b> Prune invalid execution payload envelopes — <i>n/a · low · S · memory, disk</i></summary>

**Idea.** Remove execution payload envelopes that failed validation from the cache and storage so they do not accumulate.

**Gap in Lighthouse.** n/a: envelopes failing verification are never inserted in cache or store, and the cache is a bounded LRU pruned on finalization.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/payload_envelope_verification/import.rs:153`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/import.rs#L153) invalid payload status handled before storing
- [`beacon_node/beacon_chain/src/pending_payload_cache/mod.rs:118`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/mod.rs#L118) bounded LRU

**Sources.** [grandine#963](https://github.com/grandinetech/grandine/pull/963)

</details>


<a id="other_caches-094"></a>
<details>
<summary><b>other_caches-094</b> Drop finalized deposits and proofs from deposit cache — <i>n/a · low · S · memory</i></summary>

**Idea.** On finalization, drop merkle proofs (and, post-Electra, pending deposits) of finalized deposits from the in-memory eth1 deposit cache, keeping only leaves needed for the tree, since proofs are only needed for block inclusion.

**Impact.** Nothing to save: no eth1 deposit cache or proofs exist in the current tree (grep for DepositCache finds nothing outside tests/genesis).

**Best measured result.** Medalla deposit memory 223.17MB -&gt; 19.50MB (92%) (pr:prysm#7478)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:359`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L359) only a static eth1_data field remains; no deposit cache/proofs in src

**Sources.** [prysm#14829](https://github.com/OffchainLabs/prysm/pull/14829), [prysm#7478](https://github.com/OffchainLabs/prysm/pull/7478)

</details>


<a id="other_caches-095"></a>
<details>
<summary><b>other_caches-095</b> Finalization-pruned seen cache for data column sidecars — <i>implemented · medium · S · memory</i></summary>

**Idea.** Bound the observed/seen data column sidecar cache by slot and prune it on finalization (as for blobs), instead of a never-pruned map or a fixed-size LRU sized for 1000 blocks x 128 columns.

**Impact.** The column seen-cache is bounded by finalization, not by a fixed LRU.

**Best measured result.** 16.4 MB constant -&gt; 0.94 MB average (94.3%) (pr:prysm#15477)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/observed_data_sidecars.rs:129-135`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_data_sidecars.rs#L129-L135) HashMap&lt;ObservationKey(slot), HashSet&lt;index&gt;&gt;
- [`beacon_node/beacon_chain/src/observed_data_sidecars.rs:191-201`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_data_sidecars.rs#L191-L201) rejects sidecars at or before finalized slot
- [`beacon_node/beacon_chain/src/observed_data_sidecars.rs:205-213`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_data_sidecars.rs#L205-L213) prune retains slot &gt; finalized
- [`beacon_node/beacon_chain/src/canonical_head.rs:1615`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1615) observed_column_sidecars pruned on finalization
- [`beacon_node/beacon_chain/src/builder.rs:1034`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L1034)

**Skeptic check.** This is Lighthouse's own PR #8531, and it is in the base checkout. Upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#8531](https://github.com/sigp/lighthouse/pull/8531), [prysm#15477](https://github.com/OffchainLabs/prysm/pull/15477)

</details>


<a id="other_caches-096"></a>
<details>
<summary><b>other_caches-096</b> Prune payload-ID/proposer preparation cache on duty requests — <i>implemented · low · S · memory</i></summary>

**Idea.** Prune past-slot entries of the proposer preparation / payload-ID cache also when serving proposer-duties requests, so stale entries do not accumulate.

**Impact.** Memory stays bounded already; negligible.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/lib.rs:741`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L741) spawn_clean_proposer_caches_routine runs every epoch
- [`beacon_node/execution_layer/src/lib.rs:851`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L851) clean_proposer_caches retains last 2 epochs of proposer_preparation_data and proposers
- [`beacon_node/execution_layer/src/engines.rs:135`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engines.rs#L135) payload_id_cache is a fixed-size LRU

**Skeptic check.** The pruning is driven by a per-epoch timer, not by duty requests. Together with the LRU payload-ID cache this gives the same bounded result, so the earlier verdict holds.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#11568](https://github.com/OffchainLabs/prysm/pull/11568)

</details>


<a id="other_caches-097"></a>
<details>
<summary><b>other_caches-097</b> Prune beacon proposer cache on finalization — <i>implemented · low · S · memory</i></summary>

**Idea.** Prune entries of the beacon proposer cache for epochs older than finalization so the cache does not grow.

**Impact.** Entries are tiny and capped at 16; nothing to gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:7`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L7) doc: LRU, not pruned after finality
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:26`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L26) CACHE_SIZE=16
- [`beacon_node/execution_layer/src/lib.rs:851`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L851) clean_proposer_caches (the cache lighthouse#3109 actually pruned)

**Skeptic check.** lighthouse#3109 pruned the execution-layer proposers cache, which is still pruned every epoch. The beacon proposer cache is not pruned on finality, but its LRU cap of 16 keeps it bounded, so the effect is the same.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#3109](https://github.com/sigp/lighthouse/pull/3109)

</details>


<a id="other_caches-098"></a>
<details>
<summary><b>other_caches-098</b> Prune eth1 data cache by voting-window timestamp — <i>n/a · low · S · memory</i></summary>

**Idea.** Prune the eth1 block/data cache by the latest block timestamp so it holds only blocks inside the eth1 voting window range.

**Impact.** No eth1 data cache exists, so nothing to prune.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/builder.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs): no eth1 block cache; grep eth1_cache/DepositCache finds none

**Sources.** [teku#1597](https://github.com/Consensys-Incorporated/teku/pull/1597)

</details>


<a id="other_caches-099"></a>
<details>
<summary><b>other_caches-099</b> Reject future-slot blocks before block timing cache — <i>implemented · low · S · memory</i></summary>

**Idea.** Validate that a block's slot is not far in the future before inserting it into the block timing/observation cache, and bound its pruning, so peers cannot grow it with far-future entries.

**Impact.** Prevents peer-driven growth of the cache; already done.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:3942`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3942) FutureSlot rejection before block_times_cache.set_time_observed
- [`beacon_node/beacon_chain/src/block_times_cache.rs:288`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_times_cache.rs#L288) prune keeps slots in (current-64, current+1]
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1610`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1610) gossip records only after verify_block_for_gossip succeeds
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7478`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7478) prune per slot

**Skeptic check.** This is the lighthouse#10331 change, present in the code. The other writers (blob-observed at import, gossip after validation) are all after validation.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#10331](https://github.com/sigp/lighthouse/pull/10331)

</details>


<a id="other_caches-100"></a>
<details>
<summary><b>other_caches-100</b> Slot-first nested map for cheap seen-cache pruning — <i>partial · low · S · cpu</i></summary>

**Idea.** Key seen caches by slot in an outer map and by root in an inner map, so pruning below a slot removes whole outer entries instead of iterating every root and checking its slot.

**Gap in Lighthouse.** observed_aggregates is already slot-first; observed_block_producers, observed_slashable and observed_data_sidecars use flat maps and retain() over every key. Would need BTreeMap&lt;Slot, ..&gt; outer maps in those three.

**Impact.** Prune runs once per finalization over a few hundred small entries; microseconds, practically unmeasurable.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/observed_block_producers.rs:44`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_block_producers.rs#L44) flat HashMap&lt;ProposalKey{slot,proposer},..&gt;, prune at :187 iterates all keys
- [`beacon_node/beacon_chain/src/observed_slashable.rs:30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_slashable.rs#L30) same flat layout
- [`beacon_node/beacon_chain/src/observed_data_sidecars.rs:132`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_data_sidecars.rs#L132) flat HashMap keyed by ObservationKey
- [`beacon_node/beacon_chain/src/observed_aggregates.rs:429`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_aggregates.rs#L429) slot-first Vec&lt;SlotHashSet&gt;, prune drops whole sets

**Sources.** [lodestar#9312](https://github.com/ChainSafe/lodestar/pull/9312)

</details>


<a id="other_caches-101"></a>
<details>
<summary><b>other_caches-101</b> Pubkey-indexed map in the deposit cache — <i>n/a · low · S · cpu, latency</i></summary>

**Idea.** Keep a pubkey-to-deposit map inside the eth1 deposit cache so looking up a pending validator's deposit is O(1) instead of scanning all deposits.

**Impact.** No eth1 deposit cache; pending deposits are in beacon state post-Electra.

**Best measured result.** O(n) -&gt; O(1) per validator lookup (pr:prysm#9885)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:359`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L359) no deposit cache

**Sources.** [prysm#9885](https://github.com/OffchainLabs/prysm/pull/9885)

</details>


<a id="other_caches-102"></a>
<details>
<summary><b>other_caches-102</b> Recent blob sidecar cache in fork-choice store — <i>partial · low · S · disk, latency</i></summary>

**Idea.** Keep a small in-memory cache of recent blob sidecars keyed by block root next to the fork-choice store, so recent-chain blob lookups (e.g. by-root/by-range requests) skip DB reads.

**Gap in Lighthouse.** Recent-block sidecars are served from caches only while pending or for the single early-attester block; once imported, by-root/by-range of recent blocks hit the DB. A small LRU of recently imported sidecars keyed by root, filled in the import path and read in get_blobs/get_data_columns, would add it.

**Impact.** Saves DB reads for peers requesting the last few slots' sidecars; modest, mostly relevant when many peers request the same recent data.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:1204`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1204) get_blobs_checking_early_attester_cache checks early attester cache then DB
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1229`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1229) get_data_columns_checking_all_caches checks DA checker, pending payload cache, early attester cache then DB
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:304`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L304) get_blob / :312 get_data_columns from pending overflow LRU

**Sources.** [teku#7593](https://github.com/Consensys-Incorporated/teku/pull/7593)

</details>


<a id="other_caches-103"></a>
<details>
<summary><b>other_caches-103</b> Block cache holding only most recent blocks — <i>partial · low · S · memory</i></summary>

**Idea.** Restrict the in-memory block cache to the most recent blocks (about 3 epochs) so lookups for the recent chain hit more often with the same memory.

**Gap in Lighthouse.** Cache is an optional count-based LRU, off by default; recent blocks otherwise come from early_attester_cache / DB. To match, enable a default size of about 3 epochs of blocks (~96) or evict by slot relative to head.

**Impact.** Fewer DB reads and block decodes for recent-block RPC/lookups; teku saw ~10% more hits, likely minor on a Lighthouse node.

**Best measured result.** hits 1500 -&gt; 1650 of 2200/hour (~10%) (pr:teku#7531)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:95-125`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L95-L125) BlockCache is an LRU keyed by root, not age bounded
- [`beacon_node/store/src/config.rs:22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L22) DEFAULT_BLOCK_CACHE_SIZE = 0 and cli.rs:794 default 0 so disabled by default
- [`beacon_node/store/src/hot_cold_store.rs:571`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L571) try_get_full_block checks cache

**Sources.** [teku#7531](https://github.com/Consensys-Incorporated/teku/pull/7531)

</details>


<a id="other_caches-104"></a>
<details>
<summary><b>other_caches-104</b> In-memory block and state-root maps before DB — <i>partial · low · M · cpu, disk</i></summary>

**Idea.** Check in-memory maps for hot block and state-root lookups before going to the database, so frequent lookups skip SSZ decode/encode.

**Gap in Lighthouse.** Fork choice and state cache give in-memory block/state lookups for hot path, but generic block-root/state-root lookups through HotColdDB (load_hot_state_summary, get_blinded_block) go to the DB unless block_cache_size&gt;0. Could add small in-memory root maps in HotColdDB for the unfinalized range.

**Impact.** Avoids SSZ decode of summaries/blocks on repeated hot lookups; Lighthouse already decodes lazily and has state cache so gain is modest.

**Best measured result.** SSZ encode/decode was 20% of profiled time (pr:nimbus#945)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array.rs:93`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L93) ProtoNode keeps state_root in memory for fork choice
- [`beacon_node/store/src/hot_cold_store.rs:3010`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3010) load_block_root_from_summary reads DB summary
- [`beacon_node/store/src/state_cache.rs:316`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L316) get_by_block_root in-memory state lookup

**Sources.** [nimbus#945](https://github.com/status-im/nimbus-eth2/pull/945)

</details>


<a id="other_caches-105"></a>
<details>
<summary><b>other_caches-105</b> Cross-fork SSZ schema registry with shared instances — <i>n/a · low · memory, startup, cpu</i></summary>

**Idea.** Build all per-fork SSZ type schemas through a registry primed at startup, reusing the previous fork's instance when a schema is unchanged, so each schema object exists once and reads are lock-free.

**Impact.** SSZ schemas are compile-time types in Rust; nothing to share.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/fork/fork_context.rs:41`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/fork/fork_context.rs#L41) types are static Rust generics; no runtime schema objects

**Sources.** [teku#8614](https://github.com/Consensys-Incorporated/teku/pull/8614), [teku#8615](https://github.com/Consensys-Incorporated/teku/pull/8615), [teku#8828](https://github.com/Consensys-Incorporated/teku/pull/8828), [teku#8829](https://github.com/Consensys-Incorporated/teku/pull/8829), [teku#8843](https://github.com/Consensys-Incorporated/teku/pull/8843)

</details>


<a id="other_caches-106"></a>
<details>
<summary><b>other_caches-106</b> Share chain spec via reference counting, not clones — <i>implemented · low · S · memory</i></summary>

**Idea.** Hold the chain spec behind a shared reference-counted pointer (Arc) instead of cloning it per validator or component, so memory does not grow with the number of instances.

**Impact.** Already shared via Arc across the chain and the validator store.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:403`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L403) pub spec: Arc&lt;ChainSpec&gt;
- [`validator_client/lighthouse_validator_store/src/lib.rs:69`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/lighthouse_validator_store/src/lib.rs#L69) spec: Arc&lt;ChainSpec&gt;

**Skeptic check.** The source commit only changed the test harness, which now shares an Arc. Production components hold Arc&lt;ChainSpec&gt;; ForkContext keeps one owned copy per node, which does not grow with validators.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@becb81d84](https://github.com/sigp/lighthouse/commit/becb81d842b0)

</details>


<a id="other_caches-107"></a>
<details>
<summary><b>other_caches-107</b> One background worker for pubkey cache fetches — <i>n/a · low · cpu</i></summary>

**Idea.** Send pubkey cache fill work to a single long-lived background worker instead of spawning a task per fetch, so large pubkey batches in block or aggregate processing do not spawn huge numbers of tasks.

**Impact.** Lighthouse does not spawn a task per pubkey cache fetch; cache is an in-memory lookup.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/builder.rs:286`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L286) ValidatorPubkeyCache loaded once; no per-fetch task spawn in validator_pubkey_cache.rs

**Sources.** [prysm#12697](https://github.com/OffchainLabs/prysm/pull/12697)

</details>


<a id="other_caches-108"></a>
<details>
<summary><b>other_caches-108</b> Linear-scan single-item eviction protecting new entry — <i>partial · low · S · memory, cpu</i></summary>

**Idea.** When a bounded cache exceeds its size on insert, evict a single item by an O(N) scan instead of sorting all entries on every insertion, and never evict the just-inserted entry.

**Gap in Lighthouse.** ShufflingCache::prune_cache could use a min scan instead of sorted_by_key; cache is tiny (default 16) so gain is negligible. Just-inserted entry is not in the map at prune time, so already protected.

**Impact.** Saves a sort of ~16 keys per shuffling insert; unmeasurable.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:247-263`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L247-L263) prune_cache sorts keys by epoch on each insert, excludes head ids from pruning

**Sources.** [lodestar#9490](https://github.com/ChainSafe/lodestar/pull/9490)

</details>


<a id="other_caches-109"></a>
<details>
<summary><b>other_caches-109</b> Inline loop equality for 32/48-byte roots and pubkeys — <i>n/a · low · cpu</i></summary>

**Idea.** Compare small fixed-size byte values (32-byte roots, 48-byte pubkeys) with an inline loop and use the native memcmp only for large buffers, since native call overhead dominates for small inputs.

**Impact.** Rust fixed-size array equality has no FFI call overhead.

**Best measured result.** 32 B compare 49.7 ns -&gt; 14.7 ns (3.4x) (pr:lodestar#8846)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types) roots are alloy B256 / fixed arrays; slice equality compiles to inline memcmp

**Sources.** [lodestar#8846](https://github.com/ChainSafe/lodestar/pull/8846)

</details>


<a id="other_caches-110"></a>
<details>
<summary><b>other_caches-110</b> Is-all-zero check instead of comparing to default digest — <i>n/a · low · cpu</i></summary>

**Idea.** Test whether a digest/root is zero with an is-all-zero check instead of constructing a default zero hash and comparing, avoiding a temporary 32-byte value on hot paths.

**Impact.** Lighthouse already uses is_zero and Rust avoids temporaries.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/state_advance.rs:90`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/state_advance.rs#L90) uses Hash256::is_zero()

**Sources.** [nimbus#3386](https://github.com/status-im/nimbus-eth2/pull/3386)

</details>


<a id="other_caches-111"></a>
<details>
<summary><b>other_caches-111</b> Skip cache insertion when the cache is disabled — <i>n/a · low · cpu</i></summary>

**Idea.** When a cache is disabled (or the value is cheap to recompute), skip insertions entirely, because locking and hashing keys on insert can cost more than computing the value.

**Impact.** No cache in Lighthouse has a disabled mode, so no insertion to skip.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:230`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L230) caches are always on; no disable flag

**Sources.** [prysm#3131](https://github.com/OffchainLabs/prysm/pull/3131)

</details>


<a id="other_caches-112"></a>
<details>
<summary><b>other_caches-112</b> Build light client store only when serving enabled — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** Do not construct or maintain the light client server store and its data unless light client serving is enabled.

**Impact.** Light client work is skipped when serving is disabled. It is on by default, so most nodes pay the cost unless they pass --disable-light-client-server.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/client/src/builder.rs:272`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L272) producer channel created only if enable_light_client_server
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4787`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4787) cache_state_data gated by config
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5178`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5178) producer event gated
- [`beacon_node/beacon_chain/src/chain_config.rs:174`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/chain_config.rs#L174) enable_light_client_server defaults to true
- [`beacon_node/src/config.rs:1498`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/config.rs#L1498) --disable-light-client-server

**Skeptic check.** The gating is real on the import path (state data caching and the producer event). Unlike Prysm, the feature is on by default, which is a policy choice and not a missing mechanism.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#15464](https://github.com/OffchainLabs/prysm/pull/15464)

</details>


<a id="other_caches-113"></a>
<details>
<summary><b>other_caches-113</b> Stream validator comparison in state diffs — <i>partial · medium · M · memory</i></summary>

**Idea.** When diffing two states' validator registries, compare them by streaming through iterators instead of materializing both validator lists, lowering peak allocation.

**Gap in Lighthouse.** Target state's validator list is still copied to a Vec for every diff; compute ValidatorsDiff from milhouse iterators over the target state (and the cached source buffer) instead of to_vec.

**Impact.** Lowers peak allocation by ~one validator Vec (~120 MB at 1M validators) per stored diff; small CPU change.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hdiff.rs:102`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L102) HDiffBuffer holds validators: Vec&lt;Validator&gt;
- [`beacon_node/store/src/hdiff.rs:185`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L185) from_state does take_validators().to_vec()
- [`beacon_node/store/src/hdiff.rs:439-450`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L439-L450) ValidatorsDiff::compute single pass over slices emitting only changed entries
- [`beacon_node/store/src/hdiff.rs:227`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L227) apply rebuilds list via set_validators_from_iter
- [`beacon_node/store/src/hot_cold_store.rs:1791`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1791) and :2272 HDiffBuffer::from_state(state.clone()) materialises target per diff
- [`beacon_node/store/src/hot_cold_store.rs:235-239`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L235-L239) hot/cold hdiff buffer caches keep source buffers materialised (amortises source, not target)

**Second check.** Also checked hot_cold_store buffer caches: source buffers are cached materialised by design (needed for apply), so only the target-side copy is avoidable; the diff loop itself is already streaming.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [prysm#17396](https://github.com/OffchainLabs/prysm/pull/17396)

</details>


<a id="other_caches-114"></a>
<details>
<summary><b>other_caches-114</b> Cache head state for sync committee duty requests — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** Keep a cached head state reference for sync committee duty requests so repeated duty calls do not fetch or copy the state each time.

**Impact.** Already avoids a state fetch or copy on each duties call; nothing further to gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:3032`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3032) sync_committee_duties_from_head uses with_head, no state copy
- [`beacon_node/http_api/src/sync_committees.rs:44`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/sync_committees.rs#L44) duties served from head first; state load only on SyncCommitteeNotKnown

**Skeptic check.** Verified: the fast path borrows the cached head state under the head lock. The slow state load runs only for periods the head cannot answer.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#9448](https://github.com/OffchainLabs/prysm/pull/9448)

</details>


<a id="other_caches-115"></a>
<details>
<summary><b>other_caches-115</b> Single-flight proposer cache fill via per-entry once-cell — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Make each proposer-cache entry a once-initialised cell keyed by (epoch, decision root), so concurrent threads that miss wait for one computation instead of each loading and advancing state to compute the proposer shuffling.

**Impact.** Concurrent gossip misses (block + columns) share one state load.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:86`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L86) LruCache&lt;(Epoch, Hash256), Arc&lt;OnceCell&lt;EpochBlockProposers&gt;&gt;&gt;
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:133-143`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L133-L143) get_or_insert_key
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:180-195`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L180-L195) with_proposer_cache get_or_try_init runs state_provider once
- [`beacon_node/beacon_chain/src/block_verification.rs:1031`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1031) gossip block uses with_proposer_cache
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1746`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1746) data columns use it
- [`beacon_node/beacon_chain/src/payload_envelope_verification/gossip_verified_envelope.rs:227`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/gossip_verified_envelope.rs#L227) envelopes use it
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:355`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L355) timer primes it
- [`beacon_node/http_api/src/proposer_duties.rs:198-211`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/proposer_duties.rs#L198-L211) API computes from head and inserts outside the once-cell

**Skeptic check.** Verified the once-cell single-flight on all gossip/import paths. The HTTP proposer-duties path computes from the in-memory head state and inserts directly (not single-flight), but it does not load state from disk, so the effect holds where it matters.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#8101](https://github.com/sigp/lighthouse/pull/8101)

</details>


<a id="other_caches-116"></a>
<details>
<summary><b>other_caches-116</b> Scan deposit list from the tail for recent heights — <i>n/a · low · cpu</i></summary>

**Idea.** Look up the deposit count for an eth1 block height by scanning backward from the newest deposit, since queried heights are usually near the tail, instead of binary search.

**Impact.** Lighthouse no longer keeps an eth1 deposit cache, so there is no deposit lookup by height.

**Evidence (Lighthouse @ 928b61e719).**

- beacon_node/ has no eth1 crate; deposit cache removed

**Sources.** [prysm#8809](https://github.com/OffchainLabs/prysm/pull/8809)

</details>


<a id="other_caches-117"></a>
<details>
<summary><b>other_caches-117</b> Do not retain unfinalized blocks for obsolete forks — <i>n/a · low · memory</i></summary>

**Idea.** In the light client or optimistic sync path, do not keep unfinalized blocks only to learn execution block hashes of obsolete forks, shrinking the retained block cache.

**Impact.** Lighthouse is not a light client; no retained-unfinalized-block cache for execution hashes exists.

**Evidence (Lighthouse @ 928b61e719).**

- beacon_node/ has no light client sync / eth1 block cache to prune

**Sources.** [nimbus#6352](https://github.com/status-im/nimbus-eth2/pull/6352)

</details>


<a id="other_caches-118"></a>
<details>
<summary><b>other_caches-118</b> Evict imported blocks from pending-sidecar quarantine — <i>not · low · S · memory</i></summary>

**Idea.** When a block is imported, also remove it from the blob/column-pending block quarantine, not only the orphan quarantine, so imported blocks do not linger until size or slot pruning.

**Gap in Lighthouse.** Imported blocks' PendingComponents stay until do_maintenance prunes below the cutoff epoch; evicting on import in the DA checker (put/make_available paths) would free them earlier, but the code deliberately avoids it to prevent a re-insert race.

**Impact.** Frees a few blocks' worth of blobs/columns a short time earlier; marginal memory, risk of the race it was designed to avoid.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:540`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L540) comment: pending components never removed manually
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:719`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L719) do_maintenance prunes by finalization epoch cutoff

**Sources.** [nimbus#7466](https://github.com/status-im/nimbus-eth2/pull/7466)

</details>


<a id="other_caches-119"></a>
<details>
<summary><b>other_caches-119</b> Precomputed deduplicated light client init proofs — <i>implemented · low · S · cpu, disk, latency</i></summary>

**Idea.** Build light client bootstrap proofs incrementally as the chain progresses, store them with the sync committee part deduplicated, and prune outside the weak subjectivity period, instead of regenerating a historic state per request.

**Impact.** Bootstrap needs no historic state; committee stored once per period.

**Best measured result.** pr:lodestar#2782: init proof is 69k, mostly committee pubkeys

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/light_client_server_cache.rs:118-123`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_server_cache.rs#L118-L123) store_sync_committee_branch and store_current_sync_committee on each import
- [`beacon_node/beacon_chain/src/light_client_server_cache.rs:396-441`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_server_cache.rs#L396-L441) get_light_client_bootstrap built from stored branch and per-period committee, no state load
- [`beacon_node/store/src/hot_cold_store.rs:770-821`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L770-L821) SyncCommitteeBranch and SyncCommittee columns
- [`beacon_node/beacon_chain/src/migrate.rs:877-913`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L877-L913) prune_non_checkpoint_sync_committee_branches

**Skeptic check.** Verified incremental storage with the committee deduplicated by period and branches pruned to checkpoint blocks. No pruning of the SyncCommittee column outside the weak subjectivity period was found, but that is a minor storage detail, not the perf mechanism; no backfill of these values exists either.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#2782](https://github.com/ChainSafe/lodestar/pull/2782)

</details>


<a id="other_caches-120"></a>
<details>
<summary><b>other_caches-120</b> Precomputed fork digest cache by epoch — <i>partial · low · S · cpu</i></summary>

**Idea.** Cache fork digests keyed by epoch and precompute them at each fork and blob-schedule boundary, so gossip topics, ENR and req/resp context bytes do not rehash on each use.

**Gap in Lighthouse.** BeaconChain::compute_fork_digest (used by network service fork-topic subscription and light client http) could use ForkContext::context_bytes instead of rehashing.

**Impact.** Req/resp and gossip paths already use the precomputed table; remaining recomputes are rare (fork transitions, LC requests), so negligible savings.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/fork/fork_context.rs:58`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/fork/fork_context.rs#L58) digests precomputed for all digest epochs, context_bytes lookup at :138
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7869`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7869) compute_fork_digest recomputes each call
- [`beacon_node/network/src/service.rs:501`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L501)
- [`beacon_node/http_api/src/light_client.rs:159`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/light_client.rs#L159)

**Sources.** [lodestar#7954](https://github.com/ChainSafe/lodestar/pull/7954), [lodestar#8022](https://github.com/ChainSafe/lodestar/pull/8022)

</details>


<a id="other_caches-121"></a>
<details>
<summary><b>other_caches-121</b> Read-only iteration over tree-backed lists — <i>n/a · low · cpu, memory</i></summary>

**Idea.** Iterate tree-backed state lists such as eth1 data votes with a read-only traversal of the backing tree instead of materializing them into arrays, avoiding per-element deserialization overhead.

**Impact.** Milhouse lists iterate the tree directly without materializing arrays, so the problem described is absent.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing.rs:378`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing.rs#L378) iterates state.eth1_data_votes() via milhouse

**Sources.** [lodestar@ac2c4960f](https://github.com/ChainSafe/lodestar/commit/ac2c4960f657)

</details>


<a id="other_caches-122"></a>
<details>
<summary><b>other_caches-122</b> Remove eth1 deposit and block caches after Electra — <i>implemented · low · S · memory, disk, cpu</i></summary>

**Idea.** Once deposits come from the execution layer, delete the eth1 deposit-contract polling service and its deposit, block and finalization caches, saving memory, DB writes and EL polling.

**Impact.** No eth1 polling service or deposit/block caches remain.

**Evidence (Lighthouse @ 928b61e719).**

- beacon_node/ has no eth1 crate (directories: beacon_chain, beacon_processor, builder_client, client, execution_layer, genesis, http_api, http_metrics, lighthouse_network, network, operation_pool, proof_engine, store, timer)
- grep for DepositCache\|Eth1Service in beacon_node returns nothing

**Skeptic check.** Verified the eth1 crate and its caches are absent. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#7133](https://github.com/sigp/lighthouse/pull/7133)

</details>


<a id="other_caches-123"></a>
<details>
<summary><b>other_caches-123</b> Track only active local validators in known-validators set — <i>n/a · low · memory, startup</i></summary>

**Idea.** At startup, register local validators in the known-validators tracker only if active in the current or next epoch, rather than every validator with an index.

**Impact.** Lighthouse BN has no known-validators tracker populated from every local validator index; local validators live in the separate VC and the monitor is explicit/opt-in.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_monitor.rs:394`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_monitor.rs#L394) monitor is opt-in, explicit pubkeys, no all-validators known set
- [`beacon_node/beacon_chain/src/validator_monitor.rs:1104`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_monitor.rs#L1104) auto_register only when flag set

**Sources.** [nimbus#4793](https://github.com/status-im/nimbus-eth2/pull/4793)

</details>


