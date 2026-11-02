# other_caches

38 ideas: 7 not, 8 partial, 20 implemented, 3 n/a; 7 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

Ids missing from the sequence are ideas that have not been checked against Lighthouse yet.

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [other_caches-002](#other_caches-002) **★** | FIFO eviction for recent block and blob caches | not | medium | S | memory, latency |
| [other_caches-003](#other_caches-003) **★** | LRU eviction for epoch and shuffling caches | not | medium | S | latency, memory, cpu |
| [other_caches-004](#other_caches-004) **★** | Bounded LRU unviable-block set with reason | partial | medium | M | cpu, memory |
| [other_caches-009](#other_caches-009) | Cache total active balance per epoch | implemented | low |  | cpu |
| [other_caches-011](#other_caches-011) **★** | Cache attestation data responses per slot | partial | medium | S | cpu, latency |
| [other_caches-015](#other_caches-015) | Read-only head state for active validator count | implemented | medium | S | memory, cpu |
| [other_caches-018](#other_caches-018) | Compact raw-byte keys for pubkey and byte-keyed caches | implemented | low |  | cpu, memory, latency |
| [other_caches-019](#other_caches-019) | Batch map operations under one lock | n/a | low |  | cpu, latency |
| [other_caches-020](#other_caches-020) | Well-distributed hash for committee cache keys | n/a | low | S | cpu, latency |
| [other_caches-022](#other_caches-022) | Bound quarantine missing-parent retry tables | implemented | medium | S | memory, bandwidth |
| [other_caches-024](#other_caches-024) | Cap gossip block buffer by count | implemented | medium | S | memory |
| [other_caches-025](#other_caches-025) **★** | Byte-weighted budget for pending block pool | partial | medium | M | memory |
| [other_caches-026](#other_caches-026) | Bound beacon processor and sync work queues | implemented | medium |  | memory, cpu |
| [other_caches-027](#other_caches-027) | Bounded seen-message dedup caches for gossip | implemented | medium |  | memory, cpu |
| [other_caches-031](#other_caches-031) | Cache shuffling and committees once per epoch | implemented | low | S | cpu, memory |
| [other_caches-032](#other_caches-032) | One shared cache of decompressed validator pubkeys | implemented | medium | S | cpu, memory, latency, sync, startup |
| [other_caches-034](#other_caches-034) | Next-epoch proposer indices warm in the proposer cache | implemented | medium |  | latency |
| [other_caches-035](#other_caches-035) | Sync committee cache keyed by period root | not | low | M | cpu, memory |
| [other_caches-038](#other_caches-038) | Committee cache invalidation only when needed | implemented | low | S | cpu, bandwidth |
| [other_caches-040](#other_caches-040) | Dynamic committee cache size during non-finality | not | low | S | memory |
| [other_caches-042](#other_caches-042) | Concurrent caches instead of synchronized LRU | n/a | low | L | cpu, latency |
| [other_caches-054](#other_caches-054) | Evict empty reprocess queue entries | implemented | medium |  | memory |
| [other_caches-057](#other_caches-057) | Fixed growth step for pubkey cache | not | low | S | memory, latency |
| [other_caches-060](#other_caches-060) | Per-period cache of validators' sync committee positions | not | low | M | cpu |
| [other_caches-061](#other_caches-061) **★** | Feed light client server only from new head blocks | partial | medium | M | cpu |
| [other_caches-068](#other_caches-068) | Size shuffling cache for forks; compute each once | implemented | medium |  | cpu, memory |
| [other_caches-069](#other_caches-069) | Dependent-root keyed shuffling cache with lookahead | implemented | medium |  | cpu, memory, latency |
| [other_caches-071](#other_caches-071) | Persist pubkeys uncompressed to skip startup decompression | implemented | medium |  | startup, cpu |
| [other_caches-072](#other_caches-072) | Parallel pubkey decompression when building pubkey cache | implemented | low | S | cpu, startup |
| [other_caches-075](#other_caches-075) | Configurable light client data retention period | not | low | S | sync, startup |
| [other_caches-078](#other_caches-078) | Don't block pubkey cache readers while adding new keys | partial | low | S | latency, cpu |
| [other_caches-086](#other_caches-086) | Precompute own committee duties per dependent root | implemented | medium | S | cpu, latency |
| [other_caches-087](#other_caches-087) | Check cache before recompute or reinsert | implemented | low | S | cpu, sync |
| [other_caches-088](#other_caches-088) | Proposer index from pre-advanced next-slot state | implemented | medium |  | cpu, latency |
| [other_caches-095](#other_caches-095) | Finalization-pruned seen cache for data column sidecars | implemented | medium |  | memory |
| [other_caches-103](#other_caches-103) | Block cache holding only most recent blocks | partial | low | S | memory |
| [other_caches-104](#other_caches-104) | In-memory block and state-root maps before DB | partial | low | M | cpu, disk |
| [other_caches-113](#other_caches-113) **★** | Stream validator comparison in state diffs | partial | medium | M | memory |

★ actionable. Click an id for the full record.

## Ideas

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

**Sources.** [nimbus#7685](https://github.com/status-im/nimbus-eth2/pull/7685)

</details>


<a id="other_caches-009"></a>
<details>
<summary><b>other_caches-009</b> Cache total active balance per epoch — <i>implemented · low · cpu</i></summary>

**Idea.** Compute total active balance once per epoch and cache it (in the epoch/committee cache or keyed by epoch and decision root) instead of summing effective balances of all active validators on every call.

**Impact.** Already computed once per epoch and cached in state.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:819`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L819) total_active_balance: Option&lt;(Epoch,u64)&gt; cache field
- [`consensus/types/src/state/beacon_state.rs:2682`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2682) get_total_active_balance_at_epoch reads cache
- [`consensus/types/src/state/beacon_state.rs:2703`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2703) set_total_active_balance set by single-pass epoch processing

**Sources.** [prysm#10550](https://github.com/OffchainLabs/prysm/pull/10550), [prysm#9456](https://github.com/OffchainLabs/prysm/pull/9456), [prysm#9366](https://github.com/OffchainLabs/prysm/pull/9366), [prysm#9567](https://github.com/OffchainLabs/prysm/pull/9567)

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

**Sources.** [prysm#4873](https://github.com/OffchainLabs/prysm/pull/4873), [prysm#2542](https://github.com/OffchainLabs/prysm/pull/2542)

</details>


<a id="other_caches-015"></a>
<details>
<summary><b>other_caches-015</b> Read-only head state for active validator count — <i>implemented · medium · S · memory, cpu</i></summary>

**Idea.** Compute the active validator count (and similar hot-path reads) from a read-only reference to the head state instead of cloning the full head state.

**Impact.** None needed.

**Best measured result.** pr:prysm#14592: about 500 MB less memory allocated on holesky

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:389`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L389) active_validator_count reads cached indices from the Arc head snapshot, no clone
- [`beacon_node/beacon_chain/src/canonical_head.rs:748`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L748) only state_at_slot (beacon_chain.rs:1536) clones, and the clone is milhouse structural sharing

**Sources.** [prysm#14592](https://github.com/OffchainLabs/prysm/pull/14592)

</details>


<a id="other_caches-018"></a>
<details>
<summary><b>other_caches-018</b> Compact raw-byte keys for pubkey and byte-keyed caches — <i>implemented · low · cpu, memory, latency</i></summary>

**Idea.** Key the pubkey-to-validator-index map and similar in-memory caches (e.g. blob availability index) by raw fixed-size byte arrays with a fast hash, optionally in native/off-heap memory, instead of hex strings or other heavy intermediate representations. This cuts per-key memory and hashing/allocation cost.

**Impact.** Raw fixed-size keys already used; only the default SipHash hasher could be swapped for small gain.

**Best measured result.** ~1400 bytes/key, ~350 MB for 250k concatenated string keys avoided (pr:lodestar#3561)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:25`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L25) indices: HashMap&lt;PublicKeyBytes, usize&gt; keyed by raw 48-byte array
- validator_pubkey_cache.rs:26 pubkey_bytes: Vec&lt;PublicKeyBytes&gt; flat

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

**Sources.** [teku#3758](https://github.com/Consensys-Incorporated/teku/pull/3758)

</details>


<a id="other_caches-022"></a>
<details>
<summary><b>other_caches-022</b> Bound quarantine missing-parent retry tables — <i>implemented · medium · S · memory, bandwidth</i></summary>

**Idea.** Bound the tables of missing parents/payloads that quarantines retry fetching, with a max capacity and capped exponential backoff, so unresolved items cannot grow memory or request load without limit.

**Impact.** None needed; bounded by lookup count, attempt cap and timeouts (no exponential backoff, but retries are capped).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/manager.rs:95`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L95) MAX_PENDING_UNKNOWN_ROOTS=1024 LRU plus TTL pruning
- [`beacon_node/network/src/sync/block_lookups/mod.rs:77`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L77) MAX_LOOKUPS=200
- [`beacon_node/network/src/sync/block_lookups/mod.rs:62`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L62) SINGLE_BLOCK_LOOKUP_MAX_ATTEMPTS=4
- [`beacon_node/network/src/sync/block_lookups/mod.rs:59`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L59) PARENT_DEPTH_TOLERANCE and :71 no-peer timeout

**Sources.** [nimbus#8407](https://github.com/status-im/nimbus-eth2/pull/8407)

</details>


<a id="other_caches-024"></a>
<details>
<summary><b>other_caches-024</b> Cap gossip block buffer by count — <i>implemented · medium · S · memory</i></summary>

**Idea.** Cap the number of gossip-received blocks held in memory awaiting processing and purge the oldest once over the limit.

**Impact.** None needed; bounded by count (drops newest instead of purging oldest, same memory bound).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_queue.rs:384`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_queue.rs#L384) gossip_block_queue length 1024, drops when full
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:78`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L78) MAXIMUM_QUEUED_BLOCKS=16 early-block queue, drops new ones when full

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

**Sources.** [teku#10758](https://github.com/Consensys-Incorporated/teku/pull/10758)

</details>


<a id="other_caches-026"></a>
<details>
<summary><b>other_caches-026</b> Bound beacon processor and sync work queues — <i>implemented · medium · memory, cpu</i></summary>

**Idea.** Put explicit length limits on the queues and in-flight work between network, sync and the beacon processor so bursts of blocks, blobs or lookups cannot grow without bound or starve other work.

**Impact.** Already bounds memory and starvation under bursts; nothing further to gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:82`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L82) DEFAULT_MAX_WORK_EVENT_QUEUE_LEN 16384 and per-queue limits
- [`beacon_node/beacon_processor/src/lib.rs:762`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L762) bounded idle channel
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:78-90`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L78-L90) MAXIMUM_QUEUED_* caps
- commit e31b5d0ca196 is an ancestor of HEAD

**Sources.** [lighthouse@e31b5d0ca](https://github.com/sigp/lighthouse/commit/e31b5d0ca196)

</details>


<a id="other_caches-027"></a>
<details>
<summary><b>other_caches-027</b> Bounded seen-message dedup caches for gossip — <i>implemented · medium · memory, cpu</i></summary>

**Idea.** Back gossip seen-message dedup sets (attestations per validator/target epoch, aggregators, exits, slashings, blocks) with bounded caches instead of unbounded maps, so duplicates are dropped cheaply with capped memory; reuse epoch-boundary checkpoint states from a cache keyed by (epoch, root).

**Impact.** Gossip duplicates are dropped cheaply with bounded memory already. Exits/slashings sets only reset at fork boundaries (small in practice). Checkpoint-state cache part is covered by store state cache, not analysed.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/observed_attesters.rs:26`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_attesters.rs#L26) MAX_CACHED_EPOCHS=4 auto-pruning epoch containers
- [`beacon_node/beacon_chain/src/observed_attesters.rs:88`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_attesters.rs#L88) EpochBitfield per-validator bitfield
- [`beacon_node/beacon_chain/src/observed_block_producers.rs:33`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_block_producers.rs#L33) pruned on finalization
- [`beacon_node/beacon_chain/src/observed_operations.rs:27`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_operations.rs#L27) HashSet cleared at fork boundary
- [`beacon_node/beacon_chain/src/beacon_chain.rs:436-468`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L436-L468) observed_* fields

**Sources.** [prysm#4208](https://github.com/OffchainLabs/prysm/pull/4208), [lodestar@97d413733](https://github.com/ChainSafe/lodestar/commit/97d4137333ab)

</details>


<a id="other_caches-031"></a>
<details>
<summary><b>other_caches-031</b> Cache shuffling and committees once per epoch — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Compute the shuffled active validator list and the committees (plus per-epoch counts such as committees per slot) once per epoch, cache them in one shared cache keyed by epoch/decision root, and slice committees from it for state transition, attestation validation and duties. This avoids reshuffling per state or per lookup and avoids duplicate shuffled-index caches.

**Impact.** Already in place; committees are sliced from the cached shuffling.

**Best measured result.** pr:nimbus#316: ~2x state_sim speedup (12m26 -&gt; ~8m with start_shard_cache and committee count)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/committee_cache.rs:26`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L26) one CommitteeCache per epoch holds shuffling, positions, committees_per_slot
- [`consensus/types/src/state/beacon_state.rs:2824`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2824) build_committee_cache builds once per epoch, Arc-shared
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5211`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5211) import_block_update_shuffling_cache_fallible primes ShufflingCache keyed by decision root

**Sources.** [nimbus#291](https://github.com/status-im/nimbus-eth2/pull/291), [prysm#3625](https://github.com/OffchainLabs/prysm/pull/3625), [prysm#2323](https://github.com/OffchainLabs/prysm/pull/2323), [prysm#2237](https://github.com/OffchainLabs/prysm/pull/2237), [prysm#2228](https://github.com/OffchainLabs/prysm/pull/2228), [teku#696](https://github.com/Consensys-Incorporated/teku/pull/696), [teku#746](https://github.com/Consensys-Incorporated/teku/pull/746), [nimbus#316](https://github.com/status-im/nimbus-eth2/pull/316), [prysm#7242](https://github.com/OffchainLabs/prysm/pull/7242), [nimbus#235](https://github.com/status-im/nimbus-eth2/pull/235), [nimbus#1068](https://github.com/status-im/nimbus-eth2/pull/1068), [prysm#3607](https://github.com/OffchainLabs/prysm/pull/3607), [prysm#3948](https://github.com/OffchainLabs/prysm/pull/3948)

</details>


<a id="other_caches-032"></a>
<details>
<summary><b>other_caches-032</b> One shared cache of decompressed validator pubkeys — <i>implemented · medium · S · cpu, memory, latency, sync, startup</i></summary>

**Idea.** Keep a single process-wide cache of decompressed BLS pubkey points per validator index, sized for the whole validator set and shared by state transition, signature verification, slasher and other components. BLS paths then never decompress the 48-byte key or re-fetch it per verification.

**Gap in Lighthouse.** Block processing in consensus/state_processing still decompresses in a few non-hot spots (per_block_processing.rs:153 closure fallback, deposits signature_sets.rs:549), which is expected for new keys.

**Impact.** Hot BLS paths avoid decompression already; the slasher does not need pubkeys.

**Best measured result.** pr:teku#3314: "speedup ~x50-x100" (partial fix of #3294)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:23`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L23) ValidatorPubkeyCache Vec&lt;PublicKey&gt; decompressed, indexed by validator index
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:144`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L144) parallel decompression at first startup
- [`beacon_node/beacon_chain/src/beacon_chain.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs) (pubkey cache used via validator_pubkey_cache field by gossip and block verification)

**Sources.** [teku#3314](https://github.com/Consensys-Incorporated/teku/pull/3314), [prysm#7967](https://github.com/OffchainLabs/prysm/pull/7967), [nimbus#2625](https://github.com/status-im/nimbus-eth2/pull/2625), [lodestar@dc9669dbb](https://github.com/ChainSafe/lodestar/commit/dc9669dbbe13), [prysm#5220](https://github.com/OffchainLabs/prysm/pull/5220)

</details>


<a id="other_caches-034"></a>
<details>
<summary><b>other_caches-034</b> Next-epoch proposer indices warm in the proposer cache — <i>implemented · medium · latency</i></summary>

**Idea.** At the epoch boundary (or earlier), compute the next epoch's proposer indices and keep both current and next epoch in the proposer cache, so the first duties/block request of an epoch does not compute them cold.

**Gap in Lighthouse.** Next-epoch pre-compute only happens post-Fulu (state.slot() &gt; next_epoch_decision_slot); pre-Fulu the next epoch depends on randao at the boundary so it cannot be known earlier.

**Impact.** First duties request of an epoch is served warm.

**Best measured result.** removes &gt;500ms GetDuty delay at slot 0 (pr:prysm#12484)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:355-395`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L355-L395) computes current and next epoch proposer shuffling in state advance
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:26`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L26) LRU of 16 keyed (epoch, decision root)

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


<a id="other_caches-038"></a>
<details>
<summary><b>other_caches-038</b> Committee cache invalidation only when needed — <i>implemented · low · S · cpu, bandwidth</i></summary>

**Idea.** Make sure the committee-per-slot cache is not cleared on every state transition, only when its key actually changes, and do not re-broadcast already-seen gossip messages.

**Impact.** Already done; committee caches are rebuilt only on epoch change, and gossip dedup exists via observed_* caches.

**Best measured result.** pr:teku#711: enabled 4 node test to finalize

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:2824`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2824) build_committee_cache only builds when the cached epoch differs (Arc&lt;CommitteeCache&gt; kept across slots)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5220`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5220) skips insert if shuffling id already cached

**Sources.** [teku#711](https://github.com/Consensys-Incorporated/teku/pull/711)

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


<a id="other_caches-054"></a>
<details>
<summary><b>other_caches-054</b> Evict empty reprocess queue entries — <i>implemented · medium · memory</i></summary>

**Idea.** In the delayed-work reprocess queue, remove the per-block-root entry when its last queued attestation times out, so entries for never-imported blocks do not leak.

**Impact.** Prevents the per-root map leak; negligible CPU, bounded memory.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:1265-1281`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L1265-L1281) removes empty Vec entry from awaiting_attestations_per_root on expiry

**Sources.** [lighthouse#8065](https://github.com/sigp/lighthouse/pull/8065)

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

**Sources.** [lodestar#3967](https://github.com/ChainSafe/lodestar/pull/3967)

</details>


<a id="other_caches-068"></a>
<details>
<summary><b>other_caches-068</b> Size shuffling cache for forks; compute each once — <i>implemented · medium · cpu, memory</i></summary>

**Idea.** Size the committee shuffling cache to hold several epochs across many forks (and long non-finality), and make a miss compute-once so concurrent requesters wait instead of recomputing. Late attestations and forks then do not evict and recompute shufflings repeatedly.

**Gap in Lighthouse.** Cache size is 16 entries, below teku long-non-finality sizing, but misses are deduplicated by promises (MAX_CONCURRENT_PROMISES=2 rejects extra instead).

**Impact.** Duplicate shuffling computation already avoided.

**Best measured result.** shuffling ~6% CPU, ~20 computes/epoch reduced to 1 (pr:teku#5892)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:25`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L25) DEFAULT_CACHE_SIZE=16
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:287`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L287) create_promise and oneshot waiters for compute-once
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:257`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L257) prune_cache keeps head ids, prunes oldest epochs

**Sources.** [prysm#7018](https://github.com/OffchainLabs/prysm/pull/7018), [teku#5892](https://github.com/Consensys-Incorporated/teku/pull/5892)

</details>


<a id="other_caches-069"></a>
<details>
<summary><b>other_caches-069</b> Dependent-root keyed shuffling cache with lookahead — <i>implemented · medium · cpu, memory, latency</i></summary>

**Idea.** Key the shuffling cache by the dependent (decision) root, separate from larger per-epoch data, and compute it ahead when the determining block is processed. Attestations on non-canonical forks then need no state replay, and forks sharing a dependent root share one shuffling.

**Gap in Lighthouse.** Cache stores Arc&lt;CommitteeCache&gt;, so forks with same decision root share one shuffling; there is no separate smaller per-epoch structure, but sharing exists.

**Impact.** Attestations on forks with same decision root need no state replay.

**Best measured result.** lower memory by sharing shufflings between EpochRefs of same dependent root (no numbers) (pr:nimbus#3990)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:143`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L143) keyed by AttestationShufflingId (epoch + shuffling_decision_block)
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:395-420`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L395-L420) inserts next-epoch committee cache ahead of time
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:489`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L489) insertion at block import

**Sources.** [nimbus#3990](https://github.com/status-im/nimbus-eth2/pull/3990)

</details>


<a id="other_caches-071"></a>
<details>
<summary><b>other_caches-071</b> Persist pubkeys uncompressed to skip startup decompression — <i>implemented · medium · startup, cpu</i></summary>

**Idea.** Store validator pubkeys in uncompressed (or checksummed flat snapshot) form on disk and load them directly at startup, avoiding decompressing every BLS key on restart.

**Impact.** Restart already skips decompression of every key.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:94`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L94) DatabasePubkey stores serialize_uncompressed()
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:55`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L55) load_from_store loads via deserialize_uncompressed (no decompress)
- validator_pubkey_cache.rs:~142 first import decompresses in parallel with rayon

**Sources.** [nimbus#2639](https://github.com/status-im/nimbus-eth2/pull/2639)

</details>


<a id="other_caches-072"></a>
<details>
<summary><b>other_caches-072</b> Parallel pubkey decompression when building pubkey cache — <i>implemented · low · S · cpu, startup</i></summary>

**Idea.** When building the validator pubkey cache from a fresh checkpoint state, decompress the pubkeys in parallel on a thread pool, since serial decompression of every key dominates startup.

**Impact.** Startup pubkey cache build from a checkpoint state is parallel; already captured.

**Best measured result.** Sepolia validator_pubkey_cache_new 109.64ms -&gt; 21ms; Hoodi import 12.77s vs &gt;120s timeout (pr:lighthouse#8451)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:117`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L117) is_initial_import when cache empty
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:148`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L148) into_par_iter rayon decompression

**Sources.** [lighthouse#8451](https://github.com/sigp/lighthouse/pull/8451)

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


<a id="other_caches-086"></a>
<details>
<summary><b>other_caches-086</b> Precompute own committee duties per dependent root — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Cache the node's own validators' committee membership keyed by dependent root and do the precomputation and pruning on a dedicated executor, off the block/attestation processing path.

**Impact.** None left: Lighthouse's split VC already keeps own-validator committee duties per dependent root, computed and pruned in background tasks; the BN keeps full shufflings per dependent root.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:323`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L323) type DependentRoot = Hash256
- [`validator_client/validator_services/src/duties_service.rs:325`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L325) AttesterMap = HashMap&lt;PublicKeyBytes, HashMap&lt;Epoch, (DependentRoot, DutyAndProof)&gt;&gt; - own validators' committee duties scoped by dependent root
- [`validator_client/validator_services/src/duties_service.rs:1256-1273`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1256-L1273) refetch only when (epoch, dependent_root) conflicts
- [`validator_client/validator_services/src/duties_service.rs:1369-1380`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1369-L1380) selection-proof precomputation spawned on executor, off the attestation path
- [`validator_client/validator_services/src/duties_service.rs:1205-1212`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1205-L1212) pruning of old duties (HISTORICAL_DUTIES_EPOCHS) in the background poll task
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:397-411`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L397-L411) BN side primes shuffling_cache keyed by AttestationShufflingId (epoch, decision block) for next epoch
- [`consensus/types/src/attestation/shuffling_id.rs:23`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/attestation/shuffling_id.rs#L23)

**Second check.** Earlier review searched only the beacon node; Grandine's integrated validator maps to Lighthouse's validator_client DutiesService, which caches own duties keyed by (epoch, dependent_root), precomputes selection proofs in spawned tasks and prunes old epochs.

**Sources.** [grandine#576](https://github.com/grandinetech/grandine/pull/576)

</details>


<a id="other_caches-087"></a>
<details>
<summary><b>other_caches-087</b> Check cache before recompute or reinsert — <i>implemented · low · S · cpu, sync</i></summary>

**Idea.** Before computing a value for a cache (proposer indices, committees, pubkeys), check whether the key already exists and return early, skipping the duplicate computation, validation and locked write.

**Impact.** Duplicate cache computations are largely already avoided via existence checks.

**Best measured result.** initial sync up to 20% faster (pr:prysm#8096)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:4490`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4490) skips pubkey import unless new validators
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:91`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L91) import_new_pubkeys length check
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:158`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L158) contains_key before insert
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:230-247`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L230-L247) insert_committee_cache / insert_cache_item

**Sources.** [prysm#8096](https://github.com/OffchainLabs/prysm/pull/8096), [prysm#4719](https://github.com/OffchainLabs/prysm/pull/4719), [lodestar@2e25d97fa](https://github.com/ChainSafe/lodestar/commit/2e25d97fadfb)

</details>


<a id="other_caches-088"></a>
<details>
<summary><b>other_caches-088</b> Proposer index from pre-advanced next-slot state — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** When validating gossip blocks, read the expected proposer index from a pre-advanced next-slot state cache instead of processing slots on a state copy for each call.

**Impact.** Gossip block proposer check is a cache lookup, state only on miss.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1031`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1031) gossip block proposer via with_proposer_cache keyed by decision root
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:355`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L355),382 pre-advanced state primes current and next epoch proposers
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:175`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L175) state loaded only on miss

**Sources.** [prysm#9709](https://github.com/OffchainLabs/prysm/pull/9709)

</details>


<a id="other_caches-095"></a>
<details>
<summary><b>other_caches-095</b> Finalization-pruned seen cache for data column sidecars — <i>implemented · medium · memory</i></summary>

**Idea.** Bound the observed/seen data column sidecar cache by slot and prune it on finalization (as for blobs), instead of a never-pruned map or a fixed-size LRU sized for 1000 blocks x 128 columns.

**Impact.** Bounded by finalization already.

**Best measured result.** 16.4 MB constant -&gt; 0.94 MB average (94.3%) (pr:prysm#15477)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/observed_data_sidecars.rs:208`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_data_sidecars.rs#L208) prune(finalized_slot) retains k.slot()&gt;finalized
- [`beacon_node/beacon_chain/src/canonical_head.rs:1615`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1615) observed_column_sidecars.write().prune on finalization
- observed_data_sidecars.rs:129 HashMap keyed by (root/proposer, slot) -&gt; HashSet of indices

**Sources.** [lighthouse#8531](https://github.com/sigp/lighthouse/pull/8531), [prysm#15477](https://github.com/OffchainLabs/prysm/pull/15477)

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

**Sources.** [prysm#17396](https://github.com/OffchainLabs/prysm/pull/17396)

</details>


