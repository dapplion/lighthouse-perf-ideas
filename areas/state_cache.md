# state_cache

124 ideas: 11 not, 12 partial, 79 implemented, 22 n/a; 17 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

Ids missing from the sequence are ideas that have not been checked against Lighthouse yet.

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [state_cache-003](#state_cache-003) | Share one pubkey-to-index map across state copies | implemented | low |  | cpu, memory, latency |
| [state_cache-004](#state_cache-004) | Bundle state with epoch context and derived caches | implemented | low |  | cpu, latency, memory |
| [state_cache-006](#state_cache-006) | State cache holds shared references, clones only on mutation | implemented | low |  | cpu, memory, latency |
| [state_cache-007](#state_cache-007) | Read-only callers use state references, not copies | implemented | medium |  | cpu, memory, latency |
| [state_cache-008](#state_cache-008) | Load or copy states into reused preallocated objects | not | low | L | cpu, memory, latency |
| [state_cache-009](#state_cache-009) | Eliminate redundant second state copy on head paths | n/a | medium |  | cpu, latency, memory |
| [state_cache-016](#state_cache-016) | Drop duplicate flat validator caches beside state | implemented | low |  | memory, cpu |
| [state_cache-017](#state_cache-017) | Per-state validator deltas over shared finalized registry | implemented | medium |  | memory |
| [state_cache-018](#state_cache-018) | Compress effective balances and use iterator committees | partial | low | S | memory, cpu, startup, disk |
| [state_cache-020](#state_cache-020) | One shared append-only decompressed validator key list | implemented | low |  | memory, cpu |
| [state_cache-021](#state_cache-021) | LRU eviction for checkpoint state cache | n/a | medium |  | cpu, latency |
| [state_cache-024](#state_cache-024) | Key checkpoint cache by (epoch, root) without hashing | n/a | low |  | cpu |
| [state_cache-026](#state_cache-026) **★** | Compute past shuffling from reference state plus RANDAO | not | medium | M | cpu, latency, disk |
| [state_cache-027](#state_cache-027) | Cache active validator indices per epoch | implemented | low |  | cpu |
| [state_cache-028](#state_cache-028) | Compute committee shuffling once per epoch and cache | implemented | medium |  | cpu, memory |
| [state_cache-029](#state_cache-029) | Cache proposer indices per epoch | implemented | low |  | cpu, latency |
| [state_cache-030](#state_cache-030) | Correct committee cache validity checks | implemented | medium |  | cpu |
| [state_cache-032](#state_cache-032) | Array-indexed pubkey cache without locks | partial | low | M | cpu, latency |
| [state_cache-035](#state_cache-035) | Run epoch cache priming off the slot thread | implemented | medium |  | latency |
| [state_cache-037](#state_cache-037) **★** | Single-flight state regeneration and loads | partial | medium | M | cpu, memory, latency |
| [state_cache-038](#state_cache-038) | Compact per-checkpoint attestation verification cache | implemented | low |  | memory, cpu |
| [state_cache-039](#state_cache-039) | Avoid pinning old head states in attestation workers | implemented | low |  | memory |
| [state_cache-040](#state_cache-040) | Select verification state by shuffling dependent root | implemented | medium |  | cpu, memory, latency |
| [state_cache-041](#state_cache-041) | Epoch-indexed checkpoint cache bounded by epoch count | n/a | medium |  | memory, latency |
| [state_cache-042](#state_cache-042) | Spill older checkpoint states to disk, reload on miss | implemented | high |  | memory, disk, cpu |
| [state_cache-043](#state_cache-043) **★** | Cap number of persisted checkpoint states on disk | partial | medium | M | disk |
| [state_cache-044](#state_cache-044) | Bounded hot states with replay regeneration | implemented | medium |  | memory, cpu |
| [state_cache-045](#state_cache-045) | Bounded smaller in-memory hot block cache | implemented | low | S | memory |
| [state_cache-048](#state_cache-048) | Size state caches to cover forks and late blocks | implemented | medium |  | cpu, latency |
| [state_cache-049](#state_cache-049) | Size state cache from real preset | n/a | low | S | cpu |
| [state_cache-052](#state_cache-052) | Limit validator-triggered head advance during sync | n/a | medium |  | memory |
| [state_cache-055](#state_cache-055) | Pooled buffer for state serialization | not | low | M | cpu, memory |
| [state_cache-056](#state_cache-056) | Serve head state from cache, bypass regen queue | implemented | low | S | latency, cpu |
| [state_cache-057](#state_cache-057) | Attestation pre-state from checkpoint cache first | implemented | medium |  | cpu, latency, disk |
| [state_cache-058](#state_cache-058) **★** | Cache slot-advanced states keyed by (root, slot) | partial | medium | M | cpu, latency, memory |
| [state_cache-060](#state_cache-060) | Cheap skip-slot cache key without state hashing | implemented | low | S | cpu, memory |
| [state_cache-065](#state_cache-065) | Cache every epoch-boundary state produced during import | implemented | medium |  | cpu, disk, sync, memory |
| [state_cache-069](#state_cache-069) **★** | Batch-load replay blocks concurrently | not | medium | S | latency, disk |
| [state_cache-071](#state_cache-071) | Batch summary writes and cheaper replay base in sync | n/a | medium |  | sync, disk |
| [state_cache-073](#state_cache-073) | Boot from persisted unfinalized checkpoint state | implemented | medium |  | sync, startup |
| [state_cache-075](#state_cache-075) | Keep head state resident in memory | implemented | low | S | cpu, latency, disk |
| [state_cache-079](#state_cache-079) **★** | Regenerate from nearest cached ancestor state | partial | medium | S | disk, cpu, latency |
| [state_cache-080](#state_cache-080) **★** | Cancel state replay on request cancellation | not | medium | M | cpu, latency |
| [state_cache-082](#state_cache-082) | Fall back to cached checkpoint state for parent | implemented | medium |  | latency, cpu |
| [state_cache-084](#state_cache-084) | Clear parent derived caches on transfer to child | n/a | low | S | memory |
| [state_cache-085](#state_cache-085) | Keep late-block pre-state in snapshot cache | implemented | medium |  | latency, cpu |
| [state_cache-087](#state_cache-087) | Skip re-persisting unchanged head state | implemented | low | S | disk, cpu, latency |
| [state_cache-091](#state_cache-091) | Diff-layered state storage with snapshots and LRU | implemented | medium |  | disk, memory, latency |
| [state_cache-092](#state_cache-092) | Do not retain epoch processing results per state | implemented | low |  | memory |
| [state_cache-093](#state_cache-093) | Bound epoch/shuffling refs to recent blocks | implemented | low |  | memory |
| [state_cache-097](#state_cache-097) | Never scan or clone all cached states | implemented | low |  | cpu, latency, memory |
| [state_cache-099](#state_cache-099) | Dedicated small cache of epoch-boundary states | implemented | medium |  | memory, disk, latency, cpu |
| [state_cache-100](#state_cache-100) | Shared per-epoch context object attached to blocks | implemented | medium | S | cpu, memory, latency |
| [state_cache-101](#state_cache-101) | Prune state cache often during sync and replay | implemented | medium | S | memory, startup |
| [state_cache-103](#state_cache-103) | Drop finalized and older states on finalization | implemented | medium | S | memory |
| [state_cache-104](#state_cache-104) **★** | Keep one epoch of states for far non-canonical forks | partial | medium | S | memory |
| [state_cache-106](#state_cache-106) | Cache finalized states keyed by slot for API | implemented | medium | S | cpu, latency, disk |
| [state_cache-107](#state_cache-107) **★** | Preload finalized epoch states into API cache | not | medium | S | latency |
| [state_cache-110](#state_cache-110) | Persist decompressed pubkey cache across restarts | implemented | medium | M | startup |
| [state_cache-112](#state_cache-112) | Preallocate pubkey cache capacity | partial | low | S | startup, memory |
| [state_cache-116](#state_cache-116) | Never evict possibly-finalizable epoch-boundary states | implemented | medium | S | memory, cpu, disk |
| [state_cache-117](#state_cache-117) **★** | Fork-aware state cache eviction by chain | not | medium | L | memory |
| [state_cache-118](#state_cache-118) **★** | Preserve fork-choice tip states when pruning | not | medium | S | cpu, memory |
| [state_cache-119](#state_cache-119) **★** | Head state never evicted; cap regen replay | partial | medium | S | cpu, memory |
| [state_cache-120](#state_cache-120) | Finalized state root fast path | implemented | low |  | latency, disk |
| [state_cache-124](#state_cache-124) | Global shuffling cache keyed by epoch and decision root | implemented | medium |  | cpu, disk, latency, memory |
| [state_cache-125](#state_cache-125) | Precompute next-epoch caches in the state-advance task | implemented | medium |  | cpu, latency |
| [state_cache-126](#state_cache-126) | Preheat n+1 shuffling at end of n-1 | implemented | medium |  | latency, cpu |
| [state_cache-127](#state_cache-127) | Seed sync committee cache from known committee | implemented | medium |  | cpu, sync |
| [state_cache-130](#state_cache-130) | Move snapshots out of cache instead of cloning | n/a | medium |  | cpu, memory, sync |
| [state_cache-132](#state_cache-132) | Persistent structurally shared tree-backed beacon states | implemented | low |  | memory, cpu |
| [state_cache-133](#state_cache-133) **★** | Rebase updated lists onto old tree | not | medium | M | memory |
| [state_cache-134](#state_cache-134) | Load states onto an existing in-memory tree | implemented | medium | S | memory, cpu, startup |
| [state_cache-136](#state_cache-136) | Pool and reuse large state field buffers | n/a | low |  | memory, cpu |
| [state_cache-138](#state_cache-138) | No state copies on head save and init sync | n/a | medium |  | memory, sync |
| [state_cache-139](#state_cache-139) | Read-only field accessors without state copy | implemented | low |  | memory, cpu |
| [state_cache-144](#state_cache-144) | Compact flattened checkpoint state | n/a | medium |  | memory, cpu |
| [state_cache-149](#state_cache-149) | In-memory LRU of recent hot states | implemented | medium |  | memory, latency, disk, cpu |
| [state_cache-150](#state_cache-150) | Tune hot state cache size | implemented | low |  | cpu, latency, memory, startup |
| [state_cache-151](#state_cache-151) | Store sparse states, regenerate by replay | implemented | low |  | memory, disk, cpu, latency |
| [state_cache-152](#state_cache-152) | Do not pin disk-loaded states in cache | implemented | medium |  | memory, disk |
| [state_cache-153](#state_cache-153) | Periodic hot state snapshots in long non-finality | implemented | medium |  | memory, disk |
| [state_cache-154](#state_cache-154) | Prune before persisting checkpoint states | n/a | low |  | disk, memory |
| [state_cache-155](#state_cache-155) | Prune on-disk states one epoch behind finality | implemented | medium |  | disk |
| [state_cache-157](#state_cache-157) **★** | Historical state regen on dedicated worker | partial | medium | M | cpu, latency |
| [state_cache-159](#state_cache-159) | State cache during initial sync | implemented | medium |  | sync |
| [state_cache-160](#state_cache-160) | Free sync caches after range sync | n/a | low |  | memory |
| [state_cache-161](#state_cache-161) | Fewer state dumps during forward sync | implemented | medium |  | memory, cpu |
| [state_cache-162](#state_cache-162) | Pre-advance head state and serve consumers from it | implemented | high |  | latency, cpu, memory |
| [state_cache-163](#state_cache-163) | Precompute state one epoch ahead at epoch end | implemented | medium | S | latency, cpu |
| [state_cache-167](#state_cache-167) | State existence check without reading state | not | low | S | latency, disk |
| [state_cache-169](#state_cache-169) | Advance clone before storing checkpoint state | n/a | medium | S | cpu, memory |
| [state_cache-170](#state_cache-170) | Past-epoch block root lookup in checkpoint processing | n/a | high |  | memory |
| [state_cache-171](#state_cache-171) **★** | Global active validator cache across state copies | partial | medium | S | cpu, memory |
| [state_cache-172](#state_cache-172) | Keep previous head state for reorgs | implemented | low |  | disk, memory, latency |
| [state_cache-173](#state_cache-173) | Dedicated justified state cache for fork choice | implemented | medium |  | cpu, latency |
| [state_cache-176](#state_cache-176) | Limit speculative proposer-prediction replays | n/a | low |  | latency, cpu, disk |
| [state_cache-177](#state_cache-177) | Resolve block roots from state block_roots | implemented | low |  | sync, startup |
| [state_cache-178](#state_cache-178) | Non-blocking try-lock in cache pruning | n/a | low | S | latency, cpu |
| [state_cache-179](#state_cache-179) | Run state cache pruning off the store lock | implemented | medium | S | latency |
| [state_cache-181](#state_cache-181) | Transfer hash caches only to imported clone | n/a | medium |  | cpu |
| [state_cache-183](#state_cache-183) | Epoch-matching state cache for attestations | implemented | medium |  | sync, cpu |
| [state_cache-184](#state_cache-184) | Rebase clearance state on head during chain stall | implemented | medium |  | latency |
| [state_cache-186](#state_cache-186) | Bound the number of full states held in memory | implemented | high |  | memory |
| [state_cache-187](#state_cache-187) | Do expensive state work outside the cache lock | implemented | medium |  | latency, cpu |
| [state_cache-188](#state_cache-188) | Check in-memory caches before DB state loads | implemented | medium |  | latency, disk, cpu |
| [state_cache-195](#state_cache-195) | Rebuild pruned pre-state for delayed sidecar blocks | n/a | medium |  | sync |
| [state_cache-196](#state_cache-196) | Reuse the block post-state as new head state | implemented | medium |  | cpu, latency |
| [state_cache-198](#state_cache-198) **★** | Archive persisted checkpoint bytes without re-serializing | not | medium | S | cpu, disk |
| [state_cache-199](#state_cache-199) | Cache block post-states for block production | implemented | medium | S | cpu, latency |
| [state_cache-200](#state_cache-200) | Reuse prebuilt pubkey cache from anchor state | implemented | low | S | startup, cpu |
| [state_cache-210](#state_cache-210) | Dedicated clearance state for block sync | n/a | medium | S | sync, cpu |
| [state_cache-211](#state_cache-211) | Process block attestations in target order | n/a | medium | S | cpu |
| [state_cache-214](#state_cache-214) | Predict next-epoch duties without state advance | implemented | medium | S | cpu |
| [state_cache-217](#state_cache-217) | State cache eviction policy and insertion rules | implemented | medium | S | memory, cpu |
| [state_cache-223](#state_cache-223) | Skip state-root check when replaying stored blocks | implemented | medium | S | cpu |
| [state_cache-224](#state_cache-224) | Skip block validation when replaying local blocks | implemented | high |  | cpu |
| [state_cache-225](#state_cache-225) | In-memory cache of diff base/snapshot states | implemented | medium | S | disk, cpu, latency |
| [state_cache-229](#state_cache-229) | Shared state cache keyed by state root | implemented | medium | S | cpu, disk |
| [state_cache-231](#state_cache-231) | Store states as deltas over a base | implemented | medium |  | disk, memory |
| [state_cache-234](#state_cache-234) **★** | Struct-of-arrays validators with shared pubkey list | partial | medium | M | memory, cpu |
| [state_cache-235](#state_cache-235) | Copy head state outside lock, swap pointer | implemented | low | S | latency |
| [state_cache-238](#state_cache-238) | Fill only proposer indices on proposer cache miss | implemented | low | S | cpu |
| [state_cache-239](#state_cache-239) | Tiered retention for persisted checkpoint states | implemented | medium |  | disk |

★ actionable. Click an id for the full record.

## Ideas

<a id="state_cache-003"></a>
<details>
<summary><b>state_cache-003</b> Share one pubkey-to-index map across state copies — <i>implemented · low · cpu, memory, latency</i></summary>

**Idea.** Keep the validator pubkey-to-index map shared by reference across state copies, as an append-only map or an immutable base plus a small per-state delta, extended incrementally rather than rebuilt or copied when a state is copied or loaded.

**Impact.** Pubkey-to-index map is persistent, structurally shared and extended incrementally; state clones do not copy it.

**Best measured result.** copy into reused spare, 1.14M validators: Fulu ~81 -&gt; 11.7 ms, Gloas ~80 -&gt; 11.1 ms (pr:caplin#25151)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/pubkey_cache.rs:9`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/pubkey_cache.rs#L9) PubkeyCache wraps rpds HashTrieMapSync (persistent, O(1) clone)
- [`consensus/types/src/state/beacon_state.rs:2979`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2979) update_pubkey_cache extends incrementally from len
- [`consensus/types/src/state/beacon_state.rs:3523`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3523) rebase_caches_on reuses base cache on loaded states

**Sources.** [caplin#25151](https://github.com/erigontech/erigon/pull/25151), [prysm#4713](https://github.com/OffchainLabs/prysm/pull/4713), [prysm#6910](https://github.com/OffchainLabs/prysm/pull/6910), [lodestar#1028](https://github.com/ChainSafe/lodestar/pull/1028), [prysm#8860](https://github.com/OffchainLabs/prysm/pull/8860), [prysm#13943](https://github.com/OffchainLabs/prysm/pull/13943), [grandine@f603cf04a](https://github.com/grandinetech/grandine/commit/f603cf04a6db), [prysm#17286](https://github.com/OffchainLabs/prysm/pull/17286), [caplin#18527](https://github.com/erigontech/erigon/pull/18527)

</details>


<a id="state_cache-004"></a>
<details>
<summary><b>state_cache-004</b> Bundle state with epoch context and derived caches — <i>implemented · low · cpu, latency, memory</i></summary>

**Idea.** Store the epoch context and derived caches (shufflings, proposers, pubkey caches) together with the state tree in one object used by the state transition, whose clone is cheap, so block import, API and gossip reuse them instead of recomputing them from the state.

**Impact.** BeaconState carries committee, pubkey, epoch, exit, slashings and progressive-balance caches and clones cheaply; only proposer and shuffling caches live outside, keyed by decision root.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:825`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L825) committee_caches Arc inside BeaconState
- [`consensus/types/src/state/beacon_state.rs:837`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L837) pubkey_cache field
- [`consensus/types/src/state/epoch_cache.rs:22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/epoch_cache.rs#L22) EpochCache Arc&lt;Inner&gt;
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs) and shuffling_cache.rs are separate chain-level caches

**Sources.** [lodestar@cdb79c222](https://github.com/ChainSafe/lodestar/commit/cdb79c222142), [lodestar#1997](https://github.com/ChainSafe/lodestar/pull/1997), [lodestar#2172](https://github.com/ChainSafe/lodestar/pull/2172)

</details>


<a id="state_cache-006"></a>
<details>
<summary><b>state_cache-006</b> State cache holds shared references, clones only on mutation — <i>implemented · low · cpu, memory, latency</i></summary>

**Idea.** Hold cached states as reference-counted pointers and have state and checkpoint caches hand out a shared reference, cloning only when the caller will run a state transition. Inserting and reading entries then does not duplicate full states.

**Impact.** State clone is an O(1) structural-sharing copy, so the cache never duplicates full states; copy on write.

**Best measured result.** removes one extra state copy that was getting really expensive (pr:prysm#5584)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:275`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L275) get_by_state_root returns state.clone()
- [`beacon_node/store/src/state_cache.rs:215`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L215) put_state stores state.clone()
- milhouse persistent tree: clone is Arc root clone

**Sources.** [prysm#5584](https://github.com/OffchainLabs/prysm/pull/5584), [lighthouse#775](https://github.com/sigp/lighthouse/pull/775), [lodestar#6512](https://github.com/ChainSafe/lodestar/pull/6512), [lodestar#4279](https://github.com/ChainSafe/lodestar/pull/4279), [nimbus#1007](https://github.com/status-im/nimbus-eth2/pull/1007)

</details>


<a id="state_cache-007"></a>
<details>
<summary><b>state_cache-007</b> Read-only callers use state references, not copies — <i>implemented · medium · cpu, memory, latency</i></summary>

**Idea.** Paths that only read the head, finalized or cached states (committee/duty APIs, RPC, monitors, pubkey lookups, attestation production, slot advance) should use a shared read-only reference or view, or pass only the needed values, instead of deep-copying the state or validator registry, and fetch it once per call.

**Impact.** Read paths take Arc snapshot; remaining clones are O(1) tree clones via milhouse.

**Best measured result.** 400x improvement on mainnet config node (pr:prysm#4328)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:284`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L284) CachedHead holds Arc&lt;BeaconSnapshot&gt;
- [`beacon_node/beacon_chain/src/canonical_head.rs:728`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L728) head_snapshot returns Arc clone
- [`beacon_node/beacon_chain/src/canonical_head.rs:748`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L748) head_beacon_state_cloned is a milhouse structural clone, not a deep copy

**Sources.** [prysm#4328](https://github.com/OffchainLabs/prysm/pull/4328), [caplin#11854](https://github.com/erigontech/erigon/pull/11854), [lodestar@af6d704dc](https://github.com/ChainSafe/lodestar/commit/af6d704dca9a), [prysm#10101](https://github.com/OffchainLabs/prysm/pull/10101), [prysm#2368](https://github.com/OffchainLabs/prysm/pull/2368), [prysm#16745](https://github.com/OffchainLabs/prysm/pull/16745), [prysm#17424](https://github.com/OffchainLabs/prysm/pull/17424), [prysm#17055](https://github.com/OffchainLabs/prysm/pull/17055), [prysm#16511](https://github.com/OffchainLabs/prysm/pull/16511), [prysm#17425](https://github.com/OffchainLabs/prysm/pull/17425), [prysm#17716](https://github.com/OffchainLabs/prysm/pull/17716), [prysm#12326](https://github.com/OffchainLabs/prysm/pull/12326), [prysm#8303](https://github.com/OffchainLabs/prysm/pull/8303), [lodestar#8728](https://github.com/ChainSafe/lodestar/pull/8728)

</details>


<a id="state_cache-008"></a>
<details>
<summary><b>state_cache-008</b> Load or copy states into reused preallocated objects — <i>not · low · L · cpu, memory, latency</i></summary>

**Idea.** When loading a state from the DB or cache, or producing a new head or checkpoint copy, decode or copy into a preallocated spare state object that is reused, instead of allocating a fresh BeaconState each time. This removes heap allocations and full copies.

**Gap in Lighthouse.** No spare-object reuse: HDiffBuffer::as_state, load_hot_state and load_cold_state_by_slot allocate a new BeaconState and tree per load. Would need a state pool with in-place decode, which conflicts with milhouse immutable Arc trees.

**Impact.** Possibly smaller allocation churn and RSS during state loads (not the block import hot path); gain unclear since states are Arc trees, not flat arrays.

**Best measured result.** alloc 96 -&gt; 22 MB/s, anon RSS 18.2 -&gt; 12.4 GB, flush+commit p50 76 -&gt; 60 ms (pr:caplin#25003)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hdiff.rs:210`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L210) as_state builds a new BeaconState from SSZ bytes each time
- [`beacon_node/store/src/hot_cold_store.rs:1949`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1949) load_hot_state allocates a fresh state
- [`beacon_node/store/src/hot_cold_store.rs:2306`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2306) load_cold_state_by_slot allocates and clones into historic cache

**Sources.** [nimbus#937](https://github.com/status-im/nimbus-eth2/pull/937), [nimbus#942](https://github.com/status-im/nimbus-eth2/pull/942), [nimbus#5881](https://github.com/status-im/nimbus-eth2/pull/5881), [caplin#25003](https://github.com/erigontech/erigon/pull/25003), [caplin#8020](https://github.com/erigontech/erigon/pull/8020)

</details>


<a id="state_cache-009"></a>
<details>
<summary><b>state_cache-009</b> Eliminate redundant second state copy on head paths — <i>n/a · medium · cpu, latency, memory</i></summary>

**Idea.** Where a privately copied head state is handed on (to synced-data holders or the next-slot advance), transfer ownership or skip the up-front copy when already at the target slot, so each head update or payload-attributes advance does at most one state copy.

**Impact.** Full-state copies cost ~ms in Caplin; in Lighthouse BeaconState clone is a persistent-tree clone, so a second copy is negligible.

**Best measured result.** second copy p50 38 -&gt; 0 ms; total p50 189 -&gt; 150 ms; anon mem 9.0-9.5 -&gt; 8.0-8.4 GB (pr:caplin#25237)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:284`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L284) head snapshot shared via Arc
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:273`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L273) advance_head clones from cache via get_advanced_hot_state

**Sources.** [caplin#25237](https://github.com/erigontech/erigon/pull/25237), [prysm#16836](https://github.com/OffchainLabs/prysm/pull/16836)

</details>


<a id="state_cache-016"></a>
<details>
<summary><b>state_cache-016</b> Drop duplicate flat validator caches beside state — <i>implemented · low · memory, cpu</i></summary>

**Idea.** Do not keep a flat array copy of validator data next to the state tree; represent validator leaves compactly in the tree and keep only a small effective-balance array for hot reads, so each cached state holds validator data once.

**Impact.** Cached states hold validator data once in the tree plus a small effective-balance array; no flat duplicate per state.

**Best measured result.** 658MB less per state (1593MB -&gt; 935MB); hashing ~x2 slower, epoch +8ms with full deposits (pr:lodestar#3046)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:542`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L542) validators held once as milhouse List&lt;Validator&gt;
- [`consensus/types/src/state/epoch_cache.rs:33`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/epoch_cache.rs#L33) effective_balances Vec&lt;u64&gt; is the only small hot array
- [`beacon_node/store/src/hdiff.rs:102`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L102) flat Vec&lt;Validator&gt; only in HDiffBuffer, not beside every cached state

**Sources.** [lodestar#3046](https://github.com/ChainSafe/lodestar/pull/3046), [lodestar#3009](https://github.com/ChainSafe/lodestar/pull/3009)

</details>


<a id="state_cache-017"></a>
<details>
<summary><b>state_cache-017</b> Per-state validator deltas over shared finalized registry — <i>implemented · medium · memory</i></summary>

**Idea.** Keep the immutable validator data (pubkey, credentials) in one shared finalized registry and store only per-state deltas of mutable fields, instead of a full validator array per state.

**Impact.** milhouse structural sharing gives per-state deltas over the finalized registry with the same memory effect.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:197`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L197) rebase_on_finalized shares validator tree nodes with finalized state
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:24`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L24) shared decompressed pubkey cache

**Sources.** [silver#34](https://github.com/gattaca-com/silver/pull/34)

</details>


<a id="state_cache-018"></a>
<details>
<summary><b>state_cache-018</b> Compress effective balances and use iterator committees — <i>partial · low · S · memory, cpu, startup, disk</i></summary>

**Idea.** Store effective balances in compressed form in memory, use iterator-based committee and participation computation to avoid small allocations, and avoid DB reads when rewinding to head on in-memory states.

**Gap in Lighthouse.** Tree-states (milhouse) share validators structurally and EpochCache gives O(1) balance lookups, so the memory problem is mostly solved differently. Effective balances remain Vec&lt;u64&gt;; could be Vec&lt;u8&gt; increments in EpochCache::new.

**Impact.** Small memory saving (8x on one Vec per cached epoch, ~1MB at 1M validators); epoch processing already uses single_pass.

**Best measured result.** medalla unfinalized 4gb -&gt; 1gb; 40% speedup on epoch processing (pr:nimbus#1899)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/epoch_cache.rs:36`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/epoch_cache.rs#L36) EpochCache effective_balances Vec&lt;u64&gt; (uncompressed, Arc-shared)
- [`consensus/types/src/state/committee_cache.rs:26`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L26) CommitteeCache plain Vec&lt;usize&gt; shuffling

**Sources.** [nimbus#1899](https://github.com/status-im/nimbus-eth2/pull/1899)

</details>


<a id="state_cache-020"></a>
<details>
<summary><b>state_cache-020</b> One shared append-only decompressed validator key list — <i>implemented · low · memory, cpu</i></summary>

**Idea.** Since the validator key list is append-only along a chain, keep one decompressed pubkey list shared by all per-epoch caches (older caches point to the newest longer list) instead of each cached epoch reference owning a copy.

**Impact.** Already one shared decompressed list; states do not hold copies.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:24`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L24) one chain-wide append-only pubkeys Vec&lt;PublicKey&gt; + indices map
- [`consensus/types/src/state/pubkey_cache.rs:9`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/pubkey_cache.rs#L9) persistent HashTrieMap shared structurally across states

**Sources.** [nimbus#1562](https://github.com/status-im/nimbus-eth2/pull/1562), [nimbus#1486](https://github.com/status-im/nimbus-eth2/pull/1486), [nimbus@abe0d7b4a](https://github.com/status-im/nimbus-eth2/commit/abe0d7b4aeee)

</details>


<a id="state_cache-021"></a>
<details>
<summary><b>state_cache-021</b> LRU eviction for checkpoint state cache — <i>n/a · medium · cpu, latency</i></summary>

**Idea.** Evict checkpoint state cache entries by least-recent use rather than insertion order, so checkpoint states that attestations keep targeting stay cached instead of being recomputed via epoch processing.

**Impact.** No checkpoint state cache exists; hot states live in an LRU keyed by state root and attestations are served by the shuffling cache, so there is no insertion-order eviction to fix.

**Best measured result.** hit ratio 70% to 95% without validators; 25% to 70% with 512 validators (pr:prysm#7010)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:43`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L43) states is an LruCache by state root, with cull() at :357 favouring LRU

**Sources.** [prysm#7010](https://github.com/OffchainLabs/prysm/pull/7010)

</details>


<a id="state_cache-024"></a>
<details>
<summary><b>state_cache-024</b> Key checkpoint cache by (epoch, root) without hashing — <i>n/a · low · cpu</i></summary>

**Idea.** Use the (epoch, root) tuple directly as the checkpoint state cache key instead of computing a hash tree root of the checkpoint container per access.

**Impact.** Lighthouse has no checkpoint state cache keyed by hashed checkpoint; keys are existing roots, no per-access hashing.

**Best measured result.** add/get/delete 146us/op to 49.8us/op (6836 to 20073 ops/s) (pr:lodestar#2745)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:43`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L43) states LruCache keyed by state_root Hash256
- no checkpoint-state cache found (grep CheckpointCache)

**Sources.** [lodestar#2745](https://github.com/ChainSafe/lodestar/pull/2745)

</details>


<a id="state_cache-026"></a>
<details>
<summary><b>state_cache-026</b> Compute past shuffling from reference state plus RANDAO — <i>not · medium · M · cpu, latency, disk</i></summary>

**Idea.** On a shuffling cache miss, or for the randao endpoint, compute the shuffling from any available state with the locked-in active validator set plus a RANDAO mix recovered from intermediate reveals or payloads, instead of loading and replaying a full state to the epoch.

**Gap in Lighthouse.** No path builds a shuffling or answers the randao endpoint from a reference state plus a RANDAO mix recovered from blocks/payloads. The miss path always loads (and may replay) a full state; partial_state_advance only skips state-root hashing.

**Impact.** Avoids multi-second state loads/replays on old-epoch or deep-fork shuffling misses and randao queries; rare on a healthy node.

**Best measured result.** replay can take several seconds (pr:nimbus#4911)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:432`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L432) miss path loads a full state with store.get_advanced_hot_state
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:453`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L453) then partial_state_advance and committee cache build on that state
- [`consensus/types/src/state/beacon_state.rs:2373`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2373) get_seed reads randao_mixes only from the state itself; no API takes an external mix
- [`beacon_node/http_api/src/beacon/states.rs:412`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L412) randao endpoint reads get_randao_mix on a fully loaded state

**Second check.** Grepped all get_randao_mix/get_seed/set_randao_mix users in beacon_node and consensus types; every caller works on a loaded state, none splices a mix into a cached state.

**Sources.** [nimbus#4959](https://github.com/status-im/nimbus-eth2/pull/4959), [nimbus#5190](https://github.com/status-im/nimbus-eth2/pull/5190), [nimbus#8608](https://github.com/status-im/nimbus-eth2/pull/8608), [nimbus#5197](https://github.com/status-im/nimbus-eth2/pull/5197), [nimbus#4911](https://github.com/status-im/nimbus-eth2/pull/4911)

</details>


<a id="state_cache-027"></a>
<details>
<summary><b>state_cache-027</b> Cache active validator indices per epoch — <i>implemented · low · cpu</i></summary>

**Idea.** Cache get_active_validator_indices per epoch in a fork-safe per-state cache, keyed consistently so it hits, since it is called many times per epoch.

**Impact.** Active indices cached per epoch and shared via shuffling cache.

**Best measured result.** Epoch 1024 validators 2.053-&gt;0.613 s/op; 3072: 16.2-&gt;2.7 s/op (pr:teku#1111)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/committee_cache.rs:135`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L135) active indices computed once per CommitteeCache
- [`consensus/types/src/state/committee_cache.rs:186`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L186) active_validator_indices() accessor
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:128`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L128) shared by shuffling id

**Sources.** [teku#1111](https://github.com/Consensys-Incorporated/teku/pull/1111), [caplin#18542](https://github.com/erigontech/erigon/pull/18542)

</details>


<a id="state_cache-028"></a>
<details>
<summary><b>state_cache-028</b> Compute committee shuffling once per epoch and cache — <i>implemented · medium · cpu, memory</i></summary>

**Idea.** Compute the shuffling and committees once per epoch (previous, current, next) and keep them in an always-on cache reused by all callers (attestations, block operations, proposer and duty lookups), instead of rebuilding per slot or per call.

**Impact.** Already done: committees are built once per epoch in the state and shared via the shuffling cache.

**Best measured result.** 8192 validators: 4661218 ns/op, 1.6MB, 229 allocs uncached vs 99.5 ns/op, 0 allocs cached (pr:prysm#2095)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:112`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L112) ShufflingCache keyed by AttestationShufflingId
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:409`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L409) inserts Next-epoch committee cache into shuffling cache
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:326`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L326) with_cached_shuffling shared by all callers
- [`beacon_node/../consensus/state_processing/src/per_epoch_processing/altair.rs:30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/../consensus/state_processing/src/per_epoch_processing/altair.rs#L30) Previous/Current/Next built once per epoch

**Sources.** [teku#1112](https://github.com/Consensys-Incorporated/teku/pull/1112), [lighthouse@779b6266a](https://github.com/sigp/lighthouse/commit/779b6266a5da), [prysm#4522](https://github.com/OffchainLabs/prysm/pull/4522), [prysm#2095](https://github.com/OffchainLabs/prysm/pull/2095), [lighthouse@944ac73ef](https://github.com/sigp/lighthouse/commit/944ac73ef9be)

</details>


<a id="state_cache-029"></a>
<details>
<summary><b>state_cache-029</b> Cache proposer indices per epoch — <i>implemented · low · cpu, latency</i></summary>

**Idea.** Compute the proposer index list for an epoch once (at epoch transition or on first miss) and cache it so proposer lookups do not rerun the shuffle per call.

**Impact.** Proposers computed once per (epoch, decision root).

**Best measured result.** "Fixes #4500"; flame improvement (pr:prysm#4528)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:85`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L85) LruCache&lt;(Epoch, Hash256), OnceCell&lt;EpochBlockProposers&gt;&gt;

**Sources.** [prysm#4528](https://github.com/OffchainLabs/prysm/pull/4528)

</details>


<a id="state_cache-030"></a>
<details>
<summary><b>state_cache-030</b> Correct committee cache validity checks — <i>implemented · medium · cpu</i></summary>

**Idea.** Check committee/epoch cache freshness against the actual epoch requested (and load the cache for the current state epoch while applying slots), so valid caches are hit rather than rebuilt.

**Impact.** Cache validity is checked against the requested epoch; no known rebuild waste remains.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:2955`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2955) committee_cache checks is_initialized_at(relative epoch)
- [`consensus/types/src/state/committee_cache.rs:175`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L175) is_initialized_at compares to requested epoch
- [`beacon_node/../consensus/state_processing/src/per_epoch_processing/altair.rs:30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/../consensus/state_processing/src/per_epoch_processing/altair.rs#L30) caches built during epoch processing

**Sources.** [lighthouse@64dca6fba](https://github.com/sigp/lighthouse/commit/64dca6fba70b), [nimbus@b11da2cb3](https://github.com/status-im/nimbus-eth2/commit/b11da2cb3476)

</details>


<a id="state_cache-032"></a>
<details>
<summary><b>state_cache-032</b> Array-indexed pubkey cache without locks — <i>partial · low · M · cpu, latency</i></summary>

**Idea.** Store validator public keys in an array indexed by validator index (contiguous, growable without blocking) with a concurrent map for pubkey-to-index, instead of a synchronized LRU or loading validator state, removing lock contention.

**Gap in Lighthouse.** Array-indexed and decompressed, but guarded by a RwLock and the map is a plain HashMap, so writers (block import) block readers. Could use an append-only chunked/ArcSwap structure and concurrent map.

**Impact.** Removes read-lock contention on gossip signature verification during block import; likely minor since writes are short.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:24`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L24) Vec&lt;PublicKey&gt; indexed by validator index plus HashMap&lt;PublicKeyBytes,usize&gt;
- beacon_chain.rs holds it under a RwLock

**Sources.** [teku#10527](https://github.com/Consensys-Incorporated/teku/pull/10527), [teku#10528](https://github.com/Consensys-Incorporated/teku/pull/10528), [caplin#8774](https://github.com/erigontech/erigon/pull/8774)

</details>


<a id="state_cache-035"></a>
<details>
<summary><b>state_cache-035</b> Run epoch cache priming off the slot thread — <i>implemented · medium · latency</i></summary>

**Idea.** Run epoch cache priming on an async executor, also when the state is already cached, so it never blocks the slot tick.

**Impact.** Already off the slot tick, on a blocking thread.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:167`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L167) advance_head run via executor.spawn_blocking off the timer task
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:335`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L335) builds Current and Next committee caches in that task

**Sources.** [teku#6214](https://github.com/Consensys-Incorporated/teku/pull/6214)

</details>


<a id="state_cache-037"></a>
<details>
<summary><b>state_cache-037</b> Single-flight state regeneration and loads — <i>partial · medium · M · cpu, memory, latency</i></summary>

**Idea.** Route state regeneration and hot or diff-buffer loads through a promise cache or queue that registers a shared result immediately, coalesces duplicate requests and starts from the nearest cached or in-flight state, so one state triggers one computation.

**Gap in Lighthouse.** Shuffling and proposer computations are single-flight, and replay caches epoch-boundary states and hdiff buffers for later reuse, but concurrent get_hot_state/get_advanced_hot_state/load_hot_hdiff_buffer/cold loads for the same root each run the full load or replay. Add an in-flight map (OnceCell/oneshot) keyed by state root.

**Impact.** Saves duplicate state loads/replays when several requests hit the same uncached state; modest on a healthy node.

**Best measured result.** Removing shuffling cache costs ~10ms (rare) to 20-50ms (rapid) per request on author machine (pr:lighthouse#5313)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:36`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L36) CacheItem::Promise single-flights shuffling computation
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:197`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L197) proposer duties single-flight via Arc&lt;OnceCell&gt;::get_or_try_init
- [`beacon_node/store/src/hot_cold_store.rs:1124`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1124) get_advanced_hot_state: cache check then uncoordinated load_hot_state
- [`beacon_node/store/src/hot_cold_store.rs:1812`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1812) get_hot_state: same, no in-flight registry
- [`beacon_node/store/src/hot_cold_store.rs:1861`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1861) load_hot_hdiff_buffer checks cache then loads without coalescing
- [`beacon_node/store/src/hot_cold_store.rs:2041`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2041) replay caches epoch-boundary states so later loads can start from them

**Second check.** Beyond the earlier review, found the proposer cache OnceCell single-flight and the replay hook that caches epoch-boundary states; searched store and beacon_chain for OnceCell/Promise/Notify/shared futures and found no in-flight coalescing for state loads.

**Sources.** [teku#2589](https://github.com/Consensys-Incorporated/teku/pull/2589), [teku#2628](https://github.com/Consensys-Incorporated/teku/pull/2628), [teku#2690](https://github.com/Consensys-Incorporated/teku/pull/2690), [prysm#4597](https://github.com/OffchainLabs/prysm/pull/4597), [teku#2629](https://github.com/Consensys-Incorporated/teku/pull/2629), [lighthouse#5313](https://github.com/sigp/lighthouse/pull/5313)

</details>


<a id="state_cache-038"></a>
<details>
<summary><b>state_cache-038</b> Compact per-checkpoint attestation verification cache — <i>implemented · low · memory, cpu</i></summary>

**Idea.** Verify attestation signatures from a compact per-checkpoint cache holding only committees/shuffling and pubkeys, rather than retaining a full beacon state per checkpoint, which lets the state cache shrink.

**Impact.** Attestation verification uses shuffling cache plus global pubkey cache, no full state per checkpoint.

**Best measured result.** reduces memory usage by 400-600MB (pr:prysm#7098)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:128`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L128) ShufflingCache holds committee caches only
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7593`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7593) with_committee_cache
- validator_pubkey_cache.rs:24 pubkeys held separately

**Sources.** [prysm#7098](https://github.com/OffchainLabs/prysm/pull/7098), [prysm#7048](https://github.com/OffchainLabs/prysm/pull/7048), [prysm#7070](https://github.com/OffchainLabs/prysm/pull/7070)

</details>


<a id="state_cache-039"></a>
<details>
<summary><b>state_cache-039</b> Avoid pinning old head states in attestation workers — <i>implemented · low · memory</i></summary>

**Idea.** Take the previous-epoch attestation pre-state from the checkpoint state cache rather than having each concurrent worker hold the old head state, so old head states can be freed.

**Impact.** Attestation workers do not hold old head states; they use shared committee caches.

**Best measured result.** Avg RSS 9,417 vs 10,594 MB (-11%); avg HeapLive 1,411 vs 1,939 MB (-27%); peak RSS -1,839 MB (pr:prysm#16426)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:7593`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7593) with_committee_cache reads shuffling cache first, state only on miss
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5198`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5198) shuffling cache populated at block import

**Sources.** [prysm#16426](https://github.com/OffchainLabs/prysm/pull/16426)

</details>


<a id="state_cache-040"></a>
<details>
<summary><b>state_cache-040</b> Select verification state by shuffling dependent root — <i>implemented · medium · cpu, memory, latency</i></summary>

**Idea.** Choose the state for attestation, sidecar and block validation by the shuffling decision (dependent) root rather than the target checkpoint root, so the head state is reused on sibling forks with the same shuffling and no parent state is loaded and advanced.

**Impact.** Sibling forks sharing a decision root hit the same shuffling entry; only a true miss loads the target block's state.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:344`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L344) shuffling id taken from fork choice block's decision roots, cache keyed by it
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:357`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L357) read-lock hit returns without loading a state
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:376`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L376) head state reused when head root matches

**Sources.** [prysm#15996](https://github.com/OffchainLabs/prysm/pull/15996)

</details>


<a id="state_cache-041"></a>
<details>
<summary><b>state_cache-041</b> Epoch-indexed checkpoint cache bounded by epoch count — <i>n/a · medium · memory, latency</i></summary>

**Idea.** Index the checkpoint state cache by epoch and cap it by number of epochs or entries (never evicting justified/finalized), pruning eagerly even on skipped-slot checkpoints, so memory is bounded in non-finality, pruning needs no scan, and lookups can return the latest state for a root at or below an epoch.

**Impact.** Lighthouse has no checkpoint state cache; its hot state cache is capacity-bounded and culled, so non-finality memory is already bounded.

**Best measured result.** ~18-22 MB per entry at 1M validators (pr:caplin#24902)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:39`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L39) StateCache bounded by capacity, keyed by state root with cull() and finalization pruning at :127
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:111`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L111) shuffling cache capped at 16 and never evicts head ids

**Sources.** [caplin#24902](https://github.com/erigontech/erigon/pull/24902), [lodestar#3586](https://github.com/ChainSafe/lodestar/pull/3586), [lodestar#1538](https://github.com/ChainSafe/lodestar/pull/1538), [silver#258](https://github.com/gattaca-com/silver/pull/258), [lodestar@fa9f7ed50](https://github.com/ChainSafe/lodestar/commit/fa9f7ed506c5), [grandine@6fd918031](https://github.com/grandinetech/grandine/commit/6fd9180316a9), [lodestar#7497](https://github.com/ChainSafe/lodestar/pull/7497), [lodestar@69ea8676b](https://github.com/ChainSafe/lodestar/commit/69ea8676b843)

</details>


<a id="state_cache-042"></a>
<details>
<summary><b>state_cache-042</b> Spill older checkpoint states to disk, reload on miss — <i>implemented · high · memory, disk, cpu</i></summary>

**Idea.** Keep only a bounded set of recent block and checkpoint states in memory and persist older unfinalized states to disk, reloading them on demand (onto a shared base tree), so memory stays flat during long non-finality.

**Impact.** Hot states are persisted as hierarchical diffs/summaries and reloaded on miss; memory flat in non-finality via LRU cap.

**Best measured result.** Used heap 4.7-5.7 GB to 3.2-3.8 GB (2 epochs, 32 states) and 2.8-3.4 GB (0 epochs, 4 states); reload ~2s (pr:lodestar#6008)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1949`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1949) load_hot_state rebuilds unfinalized states from hdiff/replay on disk
- [`beacon_node/store/src/hot_cold_store.rs:1986`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1986) rebase_on_finalized onto shared finalized tree
- [`beacon_node/store/src/state_cache.rs:55`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L55) HotHDiffBufferCache, LRU-bounded state cache

**Sources.** [lodestar#6008](https://github.com/ChainSafe/lodestar/pull/6008), [lodestar#6176](https://github.com/ChainSafe/lodestar/pull/6176), [lodestar#6538](https://github.com/ChainSafe/lodestar/pull/6538), [teku#2308](https://github.com/Consensys-Incorporated/teku/pull/2308), [lodestar#6250](https://github.com/ChainSafe/lodestar/pull/6250), [caplin#8546](https://github.com/erigontech/erigon/pull/8546), [grandine@27e16fb69](https://github.com/grandinetech/grandine/commit/27e16fb69b0a), [grandine#86](https://github.com/grandinetech/grandine/pull/86), [lodestar#6359](https://github.com/ChainSafe/lodestar/pull/6359)

</details>


<a id="state_cache-043"></a>
<details>
<summary><b>state_cache-043</b> Cap number of persisted checkpoint states on disk — <i>partial · medium · M · disk</i></summary>

**Idea.** Delete old persisted checkpoint states so only a fixed count or number of epochs stays on disk, so long non-finality does not use hundreds of GB.

**Gap in Lighthouse.** Disk growth in non-finality is already small because hot states are stored as hierarchical diffs, and an operator can bound the hot DB by hand with POST /lighthouse/finalize (manual migration + prune_hot_db). There is no automatic cap or cull of hot summaries/diffs older than N epochs before finalization.

**Impact.** Only matters in long non-finality; diffs plus the manual-finalize endpoint already cover most of the risk, so an automatic cap would add little.

**Best measured result.** Stated: 250MB per state, over 56GB per day (pr:lodestar#7510)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1661`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1661) store_hot_state writes summaries plus hdiff/snapshot only at hierarchy slots, not a full state per checkpoint
- [`beacon_node/store/src/hot_cold_store.rs:1771`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1771) store_hot_state_as_diff stores compressed diffs
- [`beacon_node/beacon_chain/src/migrate.rs:509`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L509) prune_hot_db runs only on a (real or manual) finalization notification
- [`beacon_node/http_api/src/lib.rs:2860`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L2860) POST lighthouse/finalize lets an operator force a migration/prune during non-finality
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1837`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1837) manually_finalize_state -&gt; migrate.rs:293 run_manual_migration

**Second check.** Beyond the earlier review I found the manual finalization path (http_api lighthouse/finalize -&gt; manually_finalize_state -&gt; run_manual_migration -&gt; prune_hot_db). It is an operator-triggered equivalent, not an automatic cap, so the verdict stays partial.

**Sources.** [lodestar#7510](https://github.com/ChainSafe/lodestar/pull/7510), [lodestar#8582](https://github.com/ChainSafe/lodestar/pull/8582)

</details>


<a id="state_cache-044"></a>
<details>
<summary><b>state_cache-044</b> Bounded hot states with replay regeneration — <i>implemented · medium · memory, cpu</i></summary>

**Idea.** Keep a bounded set of hot states (e.g. checkpoint states) in memory and regenerate an evicted state on demand by replaying blocks from the nearest retained ancestor state.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:357`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L357) cull: bounded LRU of full states
- [`beacon_node/store/src/hot_cold_store.rs:1949`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1949) load_hot_state regenerates evicted state
- [`beacon_node/store/src/hot_cold_store.rs:2031`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2031) load_hot_state_using_replay replays blocks from base state

**Sources.** [teku#2065](https://github.com/Consensys-Incorporated/teku/pull/2065), [teku#2007](https://github.com/Consensys-Incorporated/teku/pull/2007), [lodestar#1514](https://github.com/ChainSafe/lodestar/pull/1514)

</details>


<a id="state_cache-045"></a>
<details>
<summary><b>state_cache-045</b> Bounded smaller in-memory hot block cache — <i>implemented · low · S · memory</i></summary>

**Idea.** Keep only a small bounded set of recent hot blocks in memory and load others from the DB on demand, so memory does not grow with unfinalized chain length and the node fits a small heap.

**Impact.** None needed; memory is already bounded independent of unfinalized length.

**Best measured result.** default cache sizes make Teku struggle to run within 1Gb heap (pr:teku#2329)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:41`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L41) states is a bounded LruCache
- [`beacon_node/store/src/config.rs:23`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L23) DEFAULT_STATE_CACHE_SIZE=128
- [`beacon_node/store/src/config.rs:22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L22) DEFAULT_BLOCK_CACHE_SIZE=0, blocks read from DB on demand

**Sources.** [teku#2271](https://github.com/Consensys-Incorporated/teku/pull/2271), [teku#2329](https://github.com/Consensys-Incorporated/teku/pull/2329)

</details>


<a id="state_cache-048"></a>
<details>
<summary><b>state_cache-048</b> Size state caches to cover forks and late blocks — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** Size the block-state and checkpoint-state caches to cover concurrent forks and late or orphaned blocks (e.g. 64 blocks, 3+ epochs), so misses do not force epoch transitions, state roots or disk regeneration.

**Best measured result.** Hit ratio 97.9% to 99.9%, saving ~2000 hash tree roots and epoch transitions (pr:prysm#4818)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/config.rs:23`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L23) DEFAULT_STATE_CACHE_SIZE=128 states (about 4 epochs of block states plus advanced states)
- [`beacon_node/store/src/state_cache.rs:18`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L18) EPOCH_FINALIZATION_LIMIT=4, cull keeps epoch boundary states that could finalize
- [`beacon_node/store/src/state_cache.rs:316`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L316) get_by_block_root serves any fork

**Sources.** [prysm#4818](https://github.com/OffchainLabs/prysm/pull/4818), [lodestar#7104](https://github.com/ChainSafe/lodestar/pull/7104)

</details>


<a id="state_cache-049"></a>
<details>
<summary><b>state_cache-049</b> Size state cache from real preset — <i>n/a · low · S · cpu</i></summary>

**Idea.** Derive the state cache size from the active network preset (several epochs of slots) so sync does not regenerate states because the cache is too small.

**Impact.** Teku bug was a hard-coded size too small for the preset; Lighthouse sync does not use the hot state cache and 128 is CLI-tunable (--state-cache-size).

**Best measured result.** cache size 40 instead of 160 wasted CPU during sync (pr:teku#3459)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/config.rs:23`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L23) fixed 128 states (4 mainnet epochs)
- [`beacon_node/store/src/state_cache.rs:357`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L357) cull() keeps recent epochs

**Sources.** [teku#3459](https://github.com/Consensys-Incorporated/teku/pull/3459)

</details>


<a id="state_cache-052"></a>
<details>
<summary><b>state_cache-052</b> Limit validator-triggered head advance during sync — <i>n/a · medium · memory</i></summary>

**Idea.** Cap how far validator requests may advance the head state (e.g. one epoch) so the checkpoint cache does not fill with divergent advanced states and OOM near sync.

**Gap in Lighthouse.** Validator-triggered advances are not inserted into the state cache (only state_advance_timer's one-slot advance is stored), so divergent advanced states cannot fill it; CPU cost of far advances is a separate issue (closed PR 10453).

**Best measured result.** avoids OOM (pr:lodestar#3169)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2161`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2161) attestation_data uses get_advanced_hot_state then partial_state_advance on a local copy, result not stored
- [`beacon_node/http_api/src/attester_duties.rs:50`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L50) rejects request_epoch &gt; current_epoch+1
- [`beacon_node/http_api/src/proposer_duties.rs:81-124`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/proposer_duties.rs#L81-L124) epoch gating
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:38`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L38) MAX_ADVANCE_DISTANCE=256

**Sources.** [lodestar#3169](https://github.com/ChainSafe/lodestar/pull/3169)

</details>


<a id="state_cache-055"></a>
<details>
<summary><b>state_cache-055</b> Pooled buffer for state serialization — <i>not · low · M · cpu, memory</i></summary>

**Idea.** Serialize states for persistence and reload into a preallocated growable buffer from a pool, returned after use, instead of allocating a fresh state-sized buffer each time.

**Gap in Lighthouse.** Add a reusable Vec&lt;u8&gt; pool (or ssz encode into a pre-sized buffer) used by HDiffBuffer::from_state and store_hot_state_as_snapshot/store_cold_state_as_snapshot.

**Impact.** Saves a state-sized allocation (~250MB on mainnet) per snapshot/diff buffer; small CPU gain, mostly lower allocator churn and peak RSS.

**Best measured result.** now takes less than 300ms to serialize a mainnet state (pr:lodestar#7109)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hdiff.rs:197`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L197) HDiffBuffer::from_state calls as_ssz_bytes() with a fresh Vec
- [`beacon_node/store/src/hot_cold_store.rs:2148`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2148) store_cold_state_as_snapshot as_ssz_bytes then compress copy
- grep found no buffer pool in store/src

**Sources.** [lodestar#7109](https://github.com/ChainSafe/lodestar/pull/7109), [lodestar#6269](https://github.com/ChainSafe/lodestar/pull/6269)

</details>


<a id="state_cache-056"></a>
<details>
<summary><b>state_cache-056</b> Serve head state from cache, bypass regen queue — <i>implemented · low · S · latency, cpu</i></summary>

**Idea.** Get the head (or epoch-correct) state directly from the state cache and only go through the state regeneration queue on a real miss, so cache-answerable requests never wait in or get dropped from the queue.

**Impact.** Cache-answerable requests never wait on a queue; no change needed.

**Best measured result.** voluntary_exit validation sometimes took up to 4s waiting on regen (pr:lodestar#5401)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1130`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1130) get_advanced_hot_state tries state cache first
- [`beacon_node/beacon_chain/src/canonical_head.rs:463`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L463) cached_head holds head snapshot in memory
- no regen queue exists in Lighthouse

**Sources.** [lodestar#5401](https://github.com/ChainSafe/lodestar/pull/5401), [lodestar#1946](https://github.com/ChainSafe/lodestar/pull/1946), [lodestar@1b132eb0c](https://github.com/ChainSafe/lodestar/commit/1b132eb0c62d), [lodestar#2486](https://github.com/ChainSafe/lodestar/pull/2486), [lodestar#1723](https://github.com/ChainSafe/lodestar/pull/1723)

</details>


<a id="state_cache-057"></a>
<details>
<summary><b>state_cache-057</b> Attestation pre-state from checkpoint cache first — <i>implemented · medium · cpu, latency, disk</i></summary>

**Idea.** Cache the state advanced to each attestation target checkpoint and look it up before processing slots or reading the DB, so repeated attestations for the same target do not redo slot processing.

**Best measured result.** 10x improvement (flame graph) (pr:prysm#4688)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:437`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L437) shuffling cache miss path: get_advanced_hot_state then partial_state_advance, result cached by shuffling id
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:395`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L395) primes shuffling cache for next epoch

**Sources.** [prysm#4688](https://github.com/OffchainLabs/prysm/pull/4688), [teku#2599](https://github.com/Consensys-Incorporated/teku/pull/2599), [prysm#3333](https://github.com/OffchainLabs/prysm/pull/3333)

</details>


<a id="state_cache-058"></a>
<details>
<summary><b>state_cache-058</b> Cache slot-advanced states keyed by (root, slot) — <i>partial · medium · M · cpu, latency, memory</i></summary>

**Idea.** Cache states advanced through empty slots keyed by (block/state root, slot), hitting also when the cached state is already at the requested slot, and share them between gossip validation, duties and block production so process_slots and epoch transitions run once.

**Gap in Lighthouse.** Lighthouse shares the single-slot advanced head state through the state cache, and caches what is derived from it (committees with promise dedup, proposers), so most repeated epoch transitions are avoided. Multi-slot partial advances, which have no state root, are still not cached as states. attestation_data across epochs, block production on a stale head, and shuffling-cache misses each re-run process_slots. The fix is a small (root, slot) to partial-advanced-state cache, as in closed PR 10453.

**Impact.** Saves repeated epoch transitions only when the head is behind by one or more epochs (skipped slots, outages). No change in normal operation.

**Best measured result.** Epoch transition run 4 times for first block of epoch; 3 of 4 removed (pr:teku#3265)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:316`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L316) get_by_block_root returns cached state at or below max_slot for a block root
- [`beacon_node/store/src/hot_cold_store.rs:1124`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1124) get_advanced_hot_state checks the state cache first (shared by block verification, block production, duties, gossip)
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:455`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L455) advanced head state put into the store/state cache; :355,:409 primes proposer and shuffling caches
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:106`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L106) Promise items dedup concurrent committee computations keyed by (epoch, decision root)
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:175`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L175) with_proposer_cache caches proposer duties, advancing at :346 only on miss
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2161`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2161) attestation_data partial_state_advance result not cached
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5454`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5454) block production partial advance not cached

**Second check.** I also checked the shuffling cache promise dedup and the proposer cache. Both are equivalents for the derived data, not for the advanced state. All partial_state_advance call sites still discard the advanced state.

**Sources.** [prysm#9077](https://github.com/OffchainLabs/prysm/pull/9077), [lighthouse#10453](https://github.com/sigp/lighthouse/pull/10453), [prysm#4694](https://github.com/OffchainLabs/prysm/pull/4694), [prysm#5279](https://github.com/OffchainLabs/prysm/pull/5279), [prysm#5280](https://github.com/OffchainLabs/prysm/pull/5280), [prysm#10447](https://github.com/OffchainLabs/prysm/pull/10447), [prysm#3879](https://github.com/OffchainLabs/prysm/pull/3879), [teku#3265](https://github.com/Consensys-Incorporated/teku/pull/3265), [grandine@6ebe3d723](https://github.com/grandinetech/grandine/commit/6ebe3d723206)

</details>


<a id="state_cache-060"></a>
<details>
<summary><b>state_cache-060</b> Cheap skip-slot cache key without state hashing — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Key the skip-slot/advanced-state cache by a cheap unique identifier (latest block header root plus slot) instead of the full state hash tree root, keeping the key unique per state.

**Impact.** Lookup already costs a map access, no tree hash.

**Best measured result.** BenchmarkCacheKey 3261 ns/op -&gt; 174.7 ns/op (about 18x) (pr:prysm#11441)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:316`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L316) get_by_block_root keyed by block_root then slot to state_root, no hashing
- [`beacon_node/store/src/hot_cold_store.rs:1196`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1196) get_advanced_hot_state_from_cache

**Sources.** [prysm#11441](https://github.com/OffchainLabs/prysm/pull/11441), [prysm#4391](https://github.com/OffchainLabs/prysm/pull/4391), [prysm#8443](https://github.com/OffchainLabs/prysm/pull/8443)

</details>


<a id="state_cache-065"></a>
<details>
<summary><b>state_cache-065</b> Cache every epoch-boundary state produced during import — <i>implemented · medium · cpu, disk, sync, memory</i></summary>

**Idea.** While processing blocks (including batch sync), keep each epoch-boundary state as a checkpoint state in memory, so attestation validation, regen, justified/finalized lookups and migration find it instead of replaying.

**Best measured result.** state copying was 1/4 to 1/3 of rewind time (pr:nimbus#906)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1632`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1632) every intermediate post-slot state stored via store_hot_state during import (also in batch/chain-segment import)
- [`beacon_node/store/src/hot_cold_store.rs:1667`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1667) store_hot_state puts each state into state_cache
- [`beacon_node/store/src/hot_cold_store.rs:2031`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2031) replay hook caches epoch boundary states
- [`beacon_node/store/src/state_cache.rs:357`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L357) cull retains boundary states last

**Sources.** [prysm#12579](https://github.com/OffchainLabs/prysm/pull/12579), [prysm#6541](https://github.com/OffchainLabs/prysm/pull/6541), [lodestar#1516](https://github.com/ChainSafe/lodestar/pull/1516), [prysm#6542](https://github.com/OffchainLabs/prysm/pull/6542), [lodestar@b3dc98b1a](https://github.com/ChainSafe/lodestar/commit/b3dc98b1a560), [nimbus#906](https://github.com/status-im/nimbus-eth2/pull/906)

</details>


<a id="state_cache-069"></a>
<details>
<summary><b>state_cache-069</b> Batch-load replay blocks concurrently — <i>not · medium · S · latency, disk</i></summary>

**Idea.** During state regeneration load all blocks to replay from the DB in one concurrent batch instead of one by one.

**Gap in Lighthouse.** Blocks for replay are read and SSZ-decoded one at a time by following parent roots. No batch read, no parallel decode, and the LRU block_cache is not used. A fix could get the block roots from hot state summaries, then batch-read and decode them in parallel with rayon.

**Impact.** Small. Hot DB reads are local. The gain is in the decode cost when a state cache miss replays up to one diff layer of blocks.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2514`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2514) load_blocks_to_replay walks ParentRootBlockIterator one block at a time
- [`beacon_node/store/src/hot_cold_store.rs:663`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L663) get_blinded_block is a single hot_db.get_bytes + decode, no batching, no block_cache use
- [`beacon_node/store/src/hot_cold_store.rs:2042`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2042) load_hot_state_using_replay calls it synchronously

**Second check.** I checked get_blinded_block/get_block_with, the store's BlockCache, and the store for any multi_get or par_iter. Nothing batches or parallelizes the replay block loading.

**Sources.** [lodestar#7033](https://github.com/ChainSafe/lodestar/pull/7033)

</details>


<a id="state_cache-071"></a>
<details>
<summary><b>state_cache-071</b> Batch summary writes and cheaper replay base in sync — <i>n/a · medium · sync, disk</i></summary>

**Idea.** During sync, batch-save state summaries, read a block rather than a full state for its slot, and replay from the latest stored state at a slot rather than an epoch boundary.

**Impact.** Lighthouse writes a hot state summary for every imported block atomically with the block, so there is no lazy summary or block-read-for-slot problem.

**Best measured result.** 30-40% higher blocks per second (pr:prysm#5241)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:4752`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4752) PutState in same atomic batch as block
- [`beacon_node/store/src/hot_cold_store.rs:1661`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1661) store_hot_state writes summary+diff per block

**Sources.** [prysm#5241](https://github.com/OffchainLabs/prysm/pull/5241)

</details>


<a id="state_cache-073"></a>
<details>
<summary><b>state_cache-073</b> Boot from persisted unfinalized checkpoint state — <i>implemented · medium · sync, startup</i></summary>

**Idea.** On restart, start from the last safe persisted unfinalized checkpoint state kept locally, rather than the finalized state, to cut resync time.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/builder.rs:229`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L229) resume_from_db loads persisted fork choice and head
- [`beacon_node/store/src/hot_cold_store.rs:1661`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1661) all unfinalized states persisted as hot diffs

**Sources.** [lodestar#7509](https://github.com/ChainSafe/lodestar/pull/7509)

</details>


<a id="state_cache-075"></a>
<details>
<summary><b>state_cache-075</b> Keep head state resident in memory — <i>implemented · low · S · cpu, latency, disk</i></summary>

**Idea.** Keep the head block and head state in memory in the chain/block pool and serve head, attestation, RPC and sync reads from it, avoiding a DB read, decode and replay.

**Impact.** Head reads served from memory already.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:463`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L463) cached_head with BeaconSnapshot
- [`beacon_node/beacon_chain/src/beacon_snapshot.rs:20`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_snapshot.rs#L20) beacon_state in snapshot

**Sources.** [nimbus@b994da78a](https://github.com/status-im/nimbus-eth2/commit/b994da78a7c4), [prysm#3279](https://github.com/OffchainLabs/prysm/pull/3279), [prysm#1775](https://github.com/OffchainLabs/prysm/pull/1775)

</details>


<a id="state_cache-079"></a>
<details>
<summary><b>state_cache-079</b> Regenerate from nearest cached ancestor state — <i>partial · medium · S · disk, cpu, latency</i></summary>

**Idea.** When rebuilding a state (block replay or hierarchical diff chain), find the closest available ancestor in the in-memory caches (then the DB) and use it as base, only advancing slots or replaying blocks/diffs from there.

**Gap in Lighthouse.** Hot ReplayFrom path always replays from the diff-layer base (cached only as an hdiff buffer, which must be converted back to a state); it never looks in the full-state cache for that base or for a nearer cached ancestor (e.g. the parent's state) on the same chain. Look up state_cache by root for the base and walk back the block chain for the closest cached state before replaying.

**Impact.** Cheaper hot-state regeneration on cache miss (deep reorgs, API queries for old unfinalized states); rare on a healthy node.

**Best measured result.** Said to improve recent states a lot, little for old ones (pr:prysm#17580)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2306`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2306) load_cold_state_by_slot searches historic_state_cache over replay_from_range(slot).rev() for the nearest prior cached state, then replays
- [`beacon_node/store/src/hot_cold_store.rs:2423`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2423) cold load_hdiff_buffer_for_slot checks hdiff buffer cache at every diff layer before going to disk
- [`beacon_node/store/src/hot_cold_store.rs:1860`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1860) hot load_hot_hdiff_buffer checks state_cache hdiff buffer cache at every layer (Snapshot/DiffFrom/ReplayFrom base)
- [`beacon_node/store/src/hot_cold_store.rs:1817`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1817) get_hot_state checks full-state cache only for the exact requested root
- [`beacon_node/store/src/hot_cold_store.rs:1987`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1987) hot ReplayFrom base loaded via load_hot_state (no full-state cache lookup, no nearer ancestor)
- [`beacon_node/store/src/hot_cold_store.rs:1124`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1124) get_advanced_hot_state uses get_by_block_root cache first

**Second check.** Beyond the earlier review, confirmed the hot hdiff buffer cache is consulted at every diff layer, so a cached ancestor is used as a buffer; the cold side fully implements the idea. The hot full-state nearest-ancestor lookup is still missing.

**Sources.** [prysm#17580](https://github.com/OffchainLabs/prysm/pull/17580), [prysm#7063](https://github.com/OffchainLabs/prysm/pull/7063), [prysm#5475](https://github.com/OffchainLabs/prysm/pull/5475), [lodestar#1547](https://github.com/ChainSafe/lodestar/pull/1547)

</details>


<a id="state_cache-080"></a>
<details>
<summary><b>state_cache-080</b> Cancel state replay on request cancellation — <i>not · medium · M · cpu, latency</i></summary>

**Idea.** Check for request cancellation inside state loading and replay loops so long replays stop when the triggering API request is cancelled or times out.

**Gap in Lighthouse.** Pass a cancellation signal (for example tx.is_closed() on the oneshot, or a CancellationToken) from http_api task_spawner into get_state/load_*_state and the BlockReplayer hooks; at minimum skip queued blocking tasks whose receiver is already dropped.

**Impact.** Saves CPU and beacon-processor workers when clients time out on expensive historic state queries; only matters under API load.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/task_spawner.rs:60`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/task_spawner.rs#L60) blocking_task runs func unconditionally; the dropped receiver only makes tx.send fail after the work is done
- [`beacon_node/http_api/src/task_spawner.rs:198`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/task_spawner.rs#L198) send_to_beacon_processor has no cancellation path to the queued or running task
- [`beacon_node/http_api/src/beacon/execution_payload_envelopes.rs:248`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/execution_payload_envelopes.rs#L248) comment states blocking work is not cancelled
- [`beacon_node/store/src/hot_cold_store.rs:2555`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2555) replay_blocks has no cancellation check

**Second check.** Also checked the http_api TaskSpawner and beacon-processor dispatch: there is no early-exit on a dropped receiver even before the task starts, and the code base itself states that no work is cancelled.

**Sources.** [prysm#7596](https://github.com/OffchainLabs/prysm/pull/7596)

</details>


<a id="state_cache-082"></a>
<details>
<summary><b>state_cache-082</b> Fall back to cached checkpoint state for parent — <i>implemented · medium · latency, cpu</i></summary>

**Idea.** When the parent post-state is missing, use the latest cached checkpoint state for the parent root and advance it, instead of failing or regenerating from far back.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:316`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L316) get_by_block_root returns latest cached state for block root at slot &lt;= max_slot
- [`beacon_node/store/src/hot_cold_store.rs:1130`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1130) get_advanced_hot_state tries cache first
- [`beacon_node/beacon_chain/src/block_verification.rs:2063`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L2063) load_parent uses it

**Sources.** [lodestar@92c65ba5a](https://github.com/ChainSafe/lodestar/commit/92c65ba5a210)

</details>


<a id="state_cache-084"></a>
<details>
<summary><b>state_cache-084</b> Clear parent derived caches on transfer to child — <i>n/a · low · S · memory</i></summary>

**Idea.** When a child state takes over cached derived views from its parent, clear them in the parent so retained hot states do not each hold a full set.

**Impact.** Derived caches are Arc-shared or live in structurally shared milhouse trees, so cloned states do not duplicate them.

**Best measured result.** 390 consecutive states: 414 MB -&gt; 226 MB; 130 states: 229 -&gt; 172 MB; no change in TransitionBenchmark (pr:teku#2061)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:825`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L825) committee_caches are Arc&lt;CommitteeCache&gt;, shared on clone
- milhouse tree-hash caches live in shared tree nodes

**Sources.** [teku#2061](https://github.com/Consensys-Incorporated/teku/pull/2061)

</details>


<a id="state_cache-085"></a>
<details>
<summary><b>state_cache-085</b> Keep late-block pre-state in snapshot cache — <i>implemented · medium · latency, cpu</i></summary>

**Idea.** When a block arrives late, clone its pre-state rather than moving it out of the snapshot cache, so a reorg to a sibling block imports without reloading state from disk.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:2063`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L2063) load_parent uses get_advanced_hot_state (clone)
- [`beacon_node/store/src/state_cache.rs:275`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L275) get_by_state_root clones, leaving entry in LRU

**Sources.** [lighthouse#2832](https://github.com/sigp/lighthouse/pull/2832)

</details>


<a id="state_cache-087"></a>
<details>
<summary><b>state_cache-087</b> Skip re-persisting unchanged head state — <i>implemented · low · S · disk, cpu, latency</i></summary>

**Idea.** Remember the (block root, slot) of the last persisted head state and skip re-encoding and writing it when the same head is processed again.

**Impact.** Redundant encode/diff is avoided via a DB summary lookup (a small read) instead of an in-memory memo.

**Best measured result.** A head-state dump takes ~405 ms p50; up to 8 redundant dumps per epoch avoided on Gloas (by code reasoning) (pr:caplin#25539)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1697`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1697) store_hot_state skips if load_hot_state_summary exists
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:455`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L455) put_state of advanced state

**Sources.** [caplin#25539](https://github.com/erigontech/erigon/pull/25539)

</details>


<a id="state_cache-091"></a>
<details>
<summary><b>state_cache-091</b> Diff-layered state storage with snapshots and LRU — <i>implemented · medium · disk, memory, latency</i></summary>

**Idea.** Store a compact parent-linked diff per state plus periodic full snapshots, rebuild states by applying diffs from the nearest snapshot, and front it with a small LRU of recent states.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hdiff.rs:33`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L33) HierarchyConfig; :98 HDiffBuffer; :127 HDiff
- [`beacon_node/store/src/hot_cold_store.rs:1741`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1741) store_hot_state_diffs
- [`beacon_node/store/src/state_cache.rs:39`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L39) StateCache LRU + HotHDiffBufferCache

**Sources.** [ethlambda#444](https://github.com/lambdaclass/ethlambda/pull/444)

</details>


<a id="state_cache-092"></a>
<details>
<summary><b>state_cache-092</b> Do not retain epoch processing results per state — <i>implemented · low · memory</i></summary>

**Idea.** Drop per-epoch processing intermediate data after the state transition, passing only what fork choice needs, so cached states do not each retain it.

**Impact.** Nothing retained per state; no change.

**Best measured result.** 31MB per state; memory 1.6-1.9GB during sync (pr:lodestar#1693)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing.rs): EpochProcessingSummary is a return value, not stored in BeaconState
- [`beacon_node/beacon_chain/src/validator_monitor.rs:793`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_monitor.rs#L793) consumes summary transiently
- [`beacon_node/store/src/state_cache.rs:40`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L40) cache holds only BeaconState

**Sources.** [lodestar#1693](https://github.com/ChainSafe/lodestar/pull/1693)

</details>


<a id="state_cache-093"></a>
<details>
<summary><b>state_cache-093</b> Bound epoch/shuffling refs to recent blocks — <i>implemented · low · memory</i></summary>

**Idea.** Bound the per-epoch shuffling/epoch-info cache to a fixed count and do not attach epoch refs to every stored block, keeping them only for recent blocks.

**Impact.** Shuffling cache is capped at 16 entries and not attached to blocks; no change.

**Best measured result.** mainnet memory down ~160-180MB; epoch cache from ~950MB to 600-700MB (pr:nimbus#2403)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:25`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L25) DEFAULT_CACHE_SIZE=16 bounded LRU keyed by shuffling id
- [`beacon_node/store/src/state_cache.rs:43`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L43) blocks carry no epoch refs

**Sources.** [nimbus#2403](https://github.com/status-im/nimbus-eth2/pull/2403), [nimbus#1645](https://github.com/status-im/nimbus-eth2/pull/1645)

</details>


<a id="state_cache-097"></a>
<details>
<summary><b>state_cache-097</b> Never scan or clone all cached states — <i>implemented · low · cpu, latency, memory</i></summary>

**Idea.** Do not iterate, deserialize or clone every cached state in a hot path (to find an epoch's first state or to prune); use keyed lookups and clone only the needed state.

**Impact.** Already keyed lookups; clones are O(1) structural shares.

**Best measured result.** processing time reduced from ~2500ms to ~200ms (pr:lodestar#1123)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:316`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L316) get_by_block_root keyed lookup via block_map
- state_cache.rs:357 cull iterates by reference, no clones
- state_cache.rs:275 get_by_state_root clones only the one state (cheap tree clone)

**Sources.** [lodestar#1123](https://github.com/ChainSafe/lodestar/pull/1123), [lodestar@df5c91a07](https://github.com/ChainSafe/lodestar/commit/df5c91a075be)

</details>


<a id="state_cache-099"></a>
<details>
<summary><b>state_cache-099</b> Dedicated small cache of epoch-boundary states — <i>implemented · medium · memory, disk, latency, cpu</i></summary>

**Idea.** Keep a separate small in-memory cache of epoch-boundary (checkpoint) states, retrievable by slot or block root, in front of the database. Epoch transitions, attestation target checks and hot-to-cold migration then read these states without DB loads or replay, and the main hot cache can shrink.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:357`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L357) cull evicts advanced/mid-epoch first, keeps recent epoch-boundary states
- [`beacon_node/store/src/state_cache.rs:316`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L316) lookup by block_root+slot
- [`beacon_node/store/src/hot_cold_store.rs:2031`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2031) replay hook caches boundary states

**Sources.** [prysm#6460](https://github.com/OffchainLabs/prysm/pull/6460), [prysm#6486](https://github.com/OffchainLabs/prysm/pull/6486), [teku#7388](https://github.com/Consensys-Incorporated/teku/pull/7388), [teku#7359](https://github.com/Consensys-Incorporated/teku/pull/7359), [prysm#6464](https://github.com/OffchainLabs/prysm/pull/6464), [prysm#6488](https://github.com/OffchainLabs/prysm/pull/6488)

</details>


<a id="state_cache-100"></a>
<details>
<summary><b>state_cache-100</b> Shared per-epoch context object attached to blocks — <i>implemented · medium · S · cpu, memory, latency</i></summary>

**Idea.** Keep one shared epoch context per epoch (shuffling, proposers, validator key refs) referenced by blocks or cached states and used to prefill the state cache. Attestation and gossip validation look it up instead of rewinding a state, recomputing shuffling or allocating per block.

**Impact.** Already avoids state rewinds for attestation/gossip validation.

**Best measured result.** "drastically speed up processing in times of long non-finality, cut memory usage by 10x" (pr:nimbus#1527)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:21`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L21) ShufflingCache keyed by shuffling id
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5198`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5198) import_block_update_shuffling_cache primes committee caches at import
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:85`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L85) BeaconProposerCache

**Sources.** [nimbus#1527](https://github.com/status-im/nimbus-eth2/pull/1527), [lodestar#1084](https://github.com/ChainSafe/lodestar/pull/1084), [nimbus#1449](https://github.com/status-im/nimbus-eth2/pull/1449), [nimbus@46c94a18b](https://github.com/status-im/nimbus-eth2/commit/46c94a18ba50)

</details>


<a id="state_cache-101"></a>
<details>
<summary><b>state_cache-101</b> Prune state cache often during sync and replay — <i>implemented · medium · S · memory, startup</i></summary>

**Idea.** Run state cache pruning on every epoch change and several times per epoch while syncing or replaying blocks at startup, not only when synced or finalized. Memory stays bounded during long replays and non-finality.

**Impact.** Memory bounded by a capped cache culled on every put; no epoch-triggered prune, but same effect.

**Best measured result.** heap stable 1.5-2.5GB on main thread; 4-7 states retained (pr:lodestar#7241)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:215`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L215) put_state culls when at capacity
- [`beacon_node/store/src/state_cache.rs:355`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L355) cull
- [`beacon_node/store/src/config.rs:23`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L23) cap 128

**Sources.** [grandine@64428a70f](https://github.com/grandinetech/grandine/commit/64428a70f37d), [grandine@c8febe6c5](https://github.com/grandinetech/grandine/commit/c8febe6c5253), [lodestar#7241](https://github.com/ChainSafe/lodestar/pull/7241), [lodestar#1494](https://github.com/ChainSafe/lodestar/pull/1494)

</details>


<a id="state_cache-103"></a>
<details>
<summary><b>state_cache-103</b> Drop finalized and older states on finalization — <i>implemented · medium · S · memory</i></summary>

**Idea.** On each finalization, remove all states (and non-canonical blocks) at or before the finalized epoch from in-memory caches and stores, instead of relying only on a size cap. Old finalized states share little structure with the head and pin unique memory.

**Impact.** Finalization already drops pre-finalized states from the cache.

**Best measured result.** Memory regression fix; first LRU eviction took almost 5h without it (graph only) (pr:prysm#16458)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:127`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L127) update_finalized_state prunes block_map and removes states below finalized slot
- [`beacon_node/store/src/hot_cold_store.rs:3665`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3665) called on each migration
- [`beacon_node/beacon_chain/src/migrate.rs:372`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L372) prune_hot_db drops abandoned-fork states/blocks

**Sources.** [prysm#16458](https://github.com/OffchainLabs/prysm/pull/16458), [lodestar#2053](https://github.com/ChainSafe/lodestar/pull/2053), [teku#1225](https://github.com/Consensys-Incorporated/teku/pull/1225), [teku#2006](https://github.com/Consensys-Incorporated/teku/pull/2006), [lodestar@dffde1287](https://github.com/ChainSafe/lodestar/commit/dffde1287b4a), [teku#764](https://github.com/Consensys-Incorporated/teku/pull/764)

</details>


<a id="state_cache-104"></a>
<details>
<summary><b>state_cache-104</b> Keep one epoch of states for far non-canonical forks — <i>partial · medium · S · memory</i></summary>

**Idea.** For non-canonical chains far ahead of finality, keep only about one epoch of beacon states in memory. Cache growth stays bounded during long non-finality with many forks.

**Gap in Lighthouse.** Cache growth is bounded by a count cap and cull priority, but there is no per-fork policy that keeps only about one epoch for far non-canonical forks. Needs fork-distance logic in StateCache::cull using block_map and the head root.

**Impact.** Marginal: memory is already capped; it changes only which states survive in long non-finality with many forks.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:356`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L356) cull: LRU with advanced &gt; old boundary &gt; mid-epoch &gt; could-finalize order, no fork awareness
- [`beacon_node/store/src/state_cache.rs:375`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L375) only head_block_root is exempt; no canonical/fork distinction
- [`beacon_node/store/src/state_cache.rs:420`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L420) BlockMap::prune drops only pre-finalized-slot states
- [`beacon_node/store/src/config.rs:23`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L23) count cap 128

**Second check.** Re-read cull and BlockMap::prune: the only fork-related input is head_block_root (exempt from mid-epoch culling); no ancestry or distance check exists anywhere in state_cache.rs.

**Sources.** [grandine#201](https://github.com/grandinetech/grandine/pull/201), [grandine@fc5638e3c](https://github.com/grandinetech/grandine/commit/fc5638e3cfe8)

</details>


<a id="state_cache-106"></a>
<details>
<summary><b>state_cache-106</b> Cache finalized states keyed by slot for API — <i>implemented · medium · S · cpu, latency, disk</i></summary>

**Idea.** Keep a cache of finalized states keyed by slot for beacon API queries. Repeated requests for the same finalized slot are served from memory instead of reloading and replaying from the freezer.

**Gap in Lighthouse.** Default capacity is 1 state. API-heavy operators must raise --historic-state-cache-size; this is a tuning default, not a missing mechanism.

**Impact.** Already present; only a default-size change is possible.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/historic_state_cache.rs:15`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/historic_state_cache.rs#L15) HistoricStateCache: LRU of freezer states keyed by Slot
- [`beacon_node/store/src/hot_cold_store.rs:2306`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2306) load_cold_state_by_slot checks the slot cache first (exact hit returns, prior slot is replayed forward)
- [`beacon_node/store/src/hot_cold_store.rs:2403`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2403) loaded cold states are put into the cache
- [`beacon_node/src/cli.rs:799`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L799) --historic-state-cache-size makes it user-sizable
- [`beacon_node/store/src/config.rs:27`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L27) cold hdiff buffer cache default 16 makes misses cheap

**Second check.** The mechanism is exactly a slot-keyed cache of finalized (freezer) states on the API load path, with a CLI flag to size it and a 16-entry hdiff buffer cache behind it. A small default is a tuning choice, not a missing mechanism.

**Sources.** [grandine@f208e64dc](https://github.com/grandinetech/grandine/commit/f208e64dc866), [grandine#234](https://github.com/grandinetech/grandine/pull/234)

</details>


<a id="state_cache-107"></a>
<details>
<summary><b>state_cache-107</b> Preload finalized epoch states into API cache — <i>not · medium · S · latency</i></summary>

**Idea.** When archiving finalized blocks, preload the states of the first and last block of the previous epoch into the state-by-slot cache. Common API queries then hit the cache instead of regenerating states.

**Gap in Lighthouse.** After migrate_database, put the epoch-boundary states of the just-archived epoch into HistoricStateCache::put_state (this needs capacity above 1).

**Impact.** Small: the first API query for a just-archived state avoids a freezer reconstruction. Matters only for state-API nodes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3603`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3603) migrate_database stores cold states ('There is no reason to cache this state') and never touches historic_state_cache
- [`beacon_node/store/src/hot_cold_store.rs:2103`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2103) store_cold_state writes the DB only and does no cache population
- [`beacon_node/store/src/state_cache.rs:127`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L127) update_finalized_state keeps only the new finalized checkpoint state hot

**Second check.** Checked migrate_database and store_cold_state for any cache warming: there is none. The only near-equivalent is that the finalized checkpoint state stays in the hot StateCache, so 'finalized' state_id queries already hit memory.

**Sources.** [grandine#593](https://github.com/grandinetech/grandine/pull/593), [grandine@8edb1815c](https://github.com/grandinetech/grandine/commit/8edb1815cc21)

</details>


<a id="state_cache-110"></a>
<details>
<summary><b>state_cache-110</b> Persist decompressed pubkey cache across restarts — <i>implemented · medium · M · startup</i></summary>

**Idea.** Write the decompressed validator pubkey cache to a flat file on clean shutdown and load it at boot with a spot-check against the anchor state. This avoids decompressing every validator pubkey at startup.

**Gap in Lighthouse.** Storage format only: one DB row per validator (about 2M sequential get_item calls) instead of one flat blob. A bulk read might save a few seconds, but decompression, which is the cost the idea targets, is already avoided.

**Impact.** Already present: startup does no BLS decompression; at most a small I/O gain from a flat-file layout.

**Best measured result.** ~7.8s saved per restart on mainnet (9.4s to 1.6s for the cache step; 42.7s to 34.7s to metrics server); load 53-56ms for 2.37M entries (pr:lodestar#10152)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:53`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L53) load_from_store rebuilds the cache from the DB at boot
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:230`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L230) DatabasePubkey::from_pubkey persists serialize_uncompressed (96-byte affine)
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:236`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L236) as_pubkey: deserialize_uncompressed, no sqrt decompression
- [`crypto/bls/src/impls/blst.rs:141`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L141) uncompressed path calls blst deserialize
- blst-0.3.17/src/lib.rs:876 blst deserialize of 96-byte input: blst_p1_deserialize, no key_validate or subgroup check

**Second check.** Traced the load path down to blst: the persisted keys are uncompressed affine points and deserialize does only an on-curve parse (no sqrt, no subgroup check), so this is the same mechanism Lodestar added. compress() of an affine point is plain serialization.

**Sources.** [lodestar#10152](https://github.com/ChainSafe/lodestar/pull/10152)

</details>


<a id="state_cache-112"></a>
<details>
<summary><b>state_cache-112</b> Preallocate pubkey cache capacity — <i>partial · low · S · startup, memory</i></summary>

**Idea.** Reserve the pubkey cache arrays to their final size (plus registry growth headroom) when building it, reuse the loaded validators array, and skip writes of identical pubkeys. This avoids repeated reallocation and needless mutation of the shared cache.

**Gap in Lighthouse.** load_from_store could size pubkeys/indices/pubkey_bytes from a known validator count (or state validators len) and reserve small growth headroom; import already reserves exactly the delta.

**Impact.** Slightly less realloc/rehash at startup (~1M validators HashMap rehashes); minor and one-off.

**Best measured result.** ~31MB virtual, ~0 resident reservation (pr:lodestar#9640)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:111`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L111) reserve(len) in import for new keys
- validator_pubkey_cache.rs:55 load_from_store pushes in loop with no pre-sizing; new() starts with vec![]

**Sources.** [lodestar#7010](https://github.com/ChainSafe/lodestar/pull/7010), [lodestar#9640](https://github.com/ChainSafe/lodestar/pull/9640)

</details>


<a id="state_cache-116"></a>
<details>
<summary><b>state_cache-116</b> Never evict possibly-finalizable epoch-boundary states — <i>implemented · medium · S · memory, cpu, disk</i></summary>

**Idea.** In state cache eviction, protect epoch-boundary states that could become finalized (checked before other conditions like is_advanced, and robust to skipped slots). Finalization migration then does not rebuild them and keeps structural sharing with recent states.

**Impact.** Lighthouse PRs 4762/4833 are present in current source.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:16`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L16) EPOCH_FINALIZATION_LIMIT=4
- [`beacon_node/store/src/state_cache.rs:376`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L376) cull checks is_boundary first, could-finalize boundary states culled last

**Sources.** [lighthouse#4762](https://github.com/sigp/lighthouse/pull/4762), [lighthouse#4833](https://github.com/sigp/lighthouse/pull/4833)

</details>


<a id="state_cache-117"></a>
<details>
<summary><b>state_cache-117</b> Fork-aware state cache eviction by chain — <i>not · medium · L · memory</i></summary>

**Idea.** Track ancestry in the state cache, evict the least recently accessed chain first, and cap states per chain. Many forks cannot push useful head-chain states out.

**Gap in Lighthouse.** Add ancestry tracking (parent links) to StateCache, evict the least recently accessed chain first and cap states per chain in cull()/put_state().

**Impact.** Under long non-finality or many forks, fork states could push head-chain states out and cause reloads/replays; small on a healthy mainnet node.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:27-36`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L27-L36) BlockMap is block_root-&gt;slot-&gt;state_root only, no parent/chain links
- [`beacon_node/store/src/state_cache.rs:357-412`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L357-L412) cull() is LRU with state-kind buckets (advanced, old boundary, mid-epoch, good boundary), no per-chain grouping or cap
- [`beacon_node/store/src/state_cache.rs:228-285`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L228-L285) put_state() has no per-chain limit
- [`beacon_node/store/src/hot_cold_store.rs:1586`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1586) only fork pruning on finalization deletes abandoned-fork states (delete_block_states), not eviction priority

**Second check.** Checked all state_cache.lock() callers in store and beacon_chain, and the finalization fork pruning path; nothing groups or limits cached states by chain.

**Sources.** [lighthouse#7069](https://github.com/sigp/lighthouse/pull/7069)

</details>


<a id="state_cache-118"></a>
<details>
<summary><b>state_cache-118</b> Preserve fork-choice tip states when pruning — <i>not · medium · S · cpu, memory</i></summary>

**Idea.** When pruning the state cache, keep the states of all unfinalized fork-choice tips so they are not evicted and later recomputed or reloaded.

**Gap in Lighthouse.** Pass all fork-choice leaf block roots (proto-array heads) to StateCache and skip their states in cull().

**Impact.** Avoids reloading/replaying states for competing tips during fork-heavy periods; negligible with one tip.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:184-189`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L184-L189) update_head_block_root stores a single head root
- [`beacon_node/store/src/state_cache.rs:392-395`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L392-L395) cull() exempts only the unadvanced head-block state
- [`beacon_node/beacon_chain/src/canonical_head.rs:1515`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1515) the only caller passes only the canonical head

**Second check.** Grepped store, canonical_head and migrate for any heads/tips/leaves set fed to the cache; only the single head root reaches it.

**Sources.** [grandine@c2470af9a](https://github.com/grandinetech/grandine/commit/c2470af9a163)

</details>


<a id="state_cache-119"></a>
<details>
<summary><b>state_cache-119</b> Head state never evicted; cap regen replay — <i>partial · medium · S · cpu, memory</i></summary>

**Idea.** Hold the fork-choice head state through a strong reference that cache eviction cannot drop, and fail fast when regenerating a state would replay too many blocks.

**Gap in Lighthouse.** Head-state strong reference is done. Missing: an explicit fail-fast cap on replayed blocks/slots in load_blocks_to_replay/replay_blocks (replay is bounded only by the hierarchy layout config, and slot advancing for stale-fork attestations is uncapped unless import_max_skip_slots is set).

**Impact.** Head-state half already present; the cap only guards pathological configs or long skip-slot advances, so the remaining gain is small.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:284`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L284) CachedHead holds snapshot: Arc&lt;BeaconSnapshot&gt; with the head BeaconState, a strong reference outside the evictable StateCache
- [`beacon_node/store/src/state_cache.rs:392-395`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L392-L395) cull() never evicts the unadvanced head state
- [`beacon_node/store/src/hdiff.rs:622`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L622) and [`beacon_node/store/src/config.rs:254`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L254) default hierarchy smallest exponent 5: hot ReplayFrom is at most 31 slots of blocks by layout
- [`beacon_node/store/src/hot_cold_store.rs:1992-2014`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1992-L2014) load_hot_state ReplayFrom from the nearest diff layer
- [`beacon_node/store/src/hot_cold_store.rs:2031-2040`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2031-L2040) load_hot_state_using_replay / 2514 load_blocks_to_replay have no explicit block-count check or fail-fast error
- [`beacon_node/beacon_chain/src/chain_config.rs:151`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/chain_config.rs#L151) import_max_skip_slots defaults to None (attestation skip cap is opt-in)

**Second check.** Confirmed that the hdiff hierarchy bounds hot replay to under 32 blocks by default (not a runtime check), and checked import_max_skip_slots and MAX_ADVANCE_DISTANCE as alternative caps; neither is a regen replay fail-fast.

**Sources.** [lodestar#4944](https://github.com/ChainSafe/lodestar/pull/4944), [lodestar#1703](https://github.com/ChainSafe/lodestar/pull/1703)

</details>


<a id="state_cache-120"></a>
<details>
<summary><b>state_cache-120</b> Finalized state root fast path — <i>implemented · low · latency, disk</i></summary>

**Idea.** In state-root-at-slot lookups, return the cached finalized/split state root directly for the finalized slot instead of walking back through state loads.

**Impact.** Already present (lighthouse#8353).

**Best measured result.** prepare_beacon_proposer took 5-10s in non-finality; no after numbers (pr:lighthouse#8353)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:977-981`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L977-L981) fast path returns split.state_root when request_slot == split.slot

**Sources.** [lighthouse#8353](https://github.com/sigp/lighthouse/pull/8353)

</details>


<a id="state_cache-124"></a>
<details>
<summary><b>state_cache-124</b> Global shuffling cache keyed by epoch and decision root — <i>implemented · medium · cpu, disk, latency, memory</i></summary>

**Idea.** Cache shufflings in one shared cache keyed by (epoch, shuffling decision root) and use it for committee assignments and every attestation, so attestations on forks or across epoch boundaries hit the cache instead of memoizing per state or forcing state reads and recomputation.

**Best measured result.** OOM kill each startup before (screenshot) (pr:lodestar#9569)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types) AttestationShufflingId = (epoch, decision block root)
- [`beacon_node/beacon_chain/src/shuffling_cache.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs):~118 ShufflingCache keyed by AttestationShufflingId, 16 entries
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5217`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5217) uses shuffling_id with the cache
- [`beacon_node/beacon_chain/src/state_advance_timer.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs):~375 inserts committee cache

**Sources.** [lighthouse#1492](https://github.com/sigp/lighthouse/pull/1492), [nimbus#2463](https://github.com/status-im/nimbus-eth2/pull/2463), [nimbus#2614](https://github.com/status-im/nimbus-eth2/pull/2614), [lodestar#9569](https://github.com/ChainSafe/lodestar/pull/9569)

</details>


<a id="state_cache-125"></a>
<details>
<summary><b>state_cache-125</b> Precompute next-epoch caches in the state-advance task — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** Before an epoch boundary (last slot, even when skipped), build the next epoch's committee, shuffling and proposer caches, ideally in the same background task that pre-advances the head state, so the epoch transition is computed once and the first block and duties of the new epoch do not miss.

**Best measured result.** Avoids extra 500ms-1s latency on slot 0 proposal (pr:prysm#12651)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs):~310-335 builds Current and Next committee caches after advancing
- state_advance_timer.rs:~345-410 primes proposer cache (current/next epoch) and shuffling_cache via insert_committee_cache on epoch crossing
- state_advance_timer.rs:38 runs in the background task at slot end for the head

**Sources.** [prysm#12667](https://github.com/OffchainLabs/prysm/pull/12667), [lighthouse@c82bad760](https://github.com/sigp/lighthouse/commit/c82bad7602ba), [prysm#12651](https://github.com/OffchainLabs/prysm/pull/12651), [prysm#12661](https://github.com/OffchainLabs/prysm/pull/12661), [caplin#12227](https://github.com/erigontech/erigon/pull/12227), [prysm#12679](https://github.com/OffchainLabs/prysm/pull/12679), [prysm#12500](https://github.com/OffchainLabs/prysm/pull/12500), [prysm#12678](https://github.com/OffchainLabs/prysm/pull/12678), [prysm#13383](https://github.com/OffchainLabs/prysm/pull/13383), [prysm#12666](https://github.com/OffchainLabs/prysm/pull/12666)

</details>


<a id="state_cache-126"></a>
<details>
<summary><b>state_cache-126</b> Preheat n+1 shuffling at end of n-1 — <i>implemented · medium · latency, cpu</i></summary>

**Idea.** Compute the shuffling for epoch n+1 at the last slot of epoch n-1, when its dependent root is known, so validator duty requests at the start of epoch n hit a warm cache.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs):~375-395 at the last slot of epoch n-1 the head is advanced into n and the RelativeEpoch::Next (n+1) shuffling is inserted with its decision root
- shuffling_cache.rs insert_committee_cache

**Sources.** [nimbus#8835](https://github.com/status-im/nimbus-eth2/pull/8835)

</details>


<a id="state_cache-127"></a>
<details>
<summary><b>state_cache-127</b> Seed sync committee cache from known committee — <i>implemented · medium · cpu, sync</i></summary>

**Idea.** When applying blocks, seed the sync committee index cache with the known committee and cache total active balance per epoch, avoiding full validator traversals per block during sync.

**Best measured result.** 20-30% sync speedup post-altair, plus ~10% from cached total active balances (pr:nimbus#4592)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:1753`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1753) get_sync_committee_indices resolves pubkeys via the state's pubkey cache, no validator traversal
- beacon_state.rs:819,2682 total_active_balance cached per epoch, set in single-pass epoch processing
- consensus/state_processing/.../altair/sync_committee.rs:90 uses cached total

**Sources.** [nimbus#4592](https://github.com/status-im/nimbus-eth2/pull/4592)

</details>


<a id="state_cache-130"></a>
<details>
<summary><b>state_cache-130</b> Move snapshots out of cache instead of cloning — <i>n/a · medium · cpu, memory, sync</i></summary>

**Idea.** Make the block-processing snapshot/state cache move the pre-state out rather than clone it when it will not be reused (head import, sync block import), reducing clones and memory fragmentation.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_snapshot.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_snapshot.rs) only a type remains; snapshot cache removed
- [`beacon_node/store/src/state_cache.rs:275`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L275) get_by_state_root clones the state, which is O(1) via milhouse structural sharing

**Sources.** [lighthouse#863](https://github.com/sigp/lighthouse/pull/863), [lighthouse#3271](https://github.com/sigp/lighthouse/pull/3271)

</details>


<a id="state_cache-132"></a>
<details>
<summary><b>state_cache-132</b> Persistent structurally shared tree-backed beacon states — <i>implemented · low · memory, cpu</i></summary>

**Idea.** Represent the beacon state in memory as persistent structurally shared trees (and diffs on disk), so clones share unchanged subtrees and cached hash roots and the state cache can hold many more states for similar memory.

**Impact.** Already core design.

**Best measured result.** holds 32x more states for around the same memory cost (pr:lighthouse#5533)

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.lock:6570 milhouse 0.9.0 persistent trees
- [`beacon_node/store/src/state_cache.rs:229`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L229) HDiffBuffer, hierarchical diffs on disk
- state_cache.rs:263 state.clone() cheap

**Sources.** [lighthouse#5533](https://github.com/sigp/lighthouse/pull/5533), [lodestar@cf71a0110](https://github.com/ChainSafe/lodestar/commit/cf71a0110082), [lighthouse#3206](https://github.com/sigp/lighthouse/pull/3206)

</details>


<a id="state_cache-133"></a>
<details>
<summary><b>state_cache-133</b> Rebase updated lists onto old tree — <i>not · medium · M · memory</i></summary>

**Idea.** After bulk-updating a list such as inactivity_scores, rebase the new tree onto the old one to reuse identical subtrees, instead of duplicating the whole list in memory each update.

**Gap in Lighthouse.** #7062's List::intra_rebase call after the epoch-transition inactivity_scores update is not in unstable. During a leak or recovery every non-zero score is rewritten, so each post-epoch state carries a fresh ~80MB inactivity_scores tree. Re-add intra_rebase (or rebase_on against the pre-state list) after process_epoch_single_pass once the milhouse intra_rebase dedup bug is fixed.

**Impact.** During non-finality, about 70MB+ to about 4-5MB per inactivity_scores update per cached state (measured on Holesky in #7062); no effect when all scores are 0 (mainnet steady state), because zero scores already skip mutation.

**Best measured result.** ~70MB+ per update to ~4-5MB; rebase time 47ms (pr:lighthouse#7062)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:245`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L245) inactivity_scores.iter_cow(), no intra_rebase/rebase after the pass
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:646-650`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L646-L650) zero scores skip make_mut (avoids copies only in the all-zero common case, not the leak/recovery case #7062 targets)
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/list.rs:356 List::intra_rebase exists; only caller is milhouse src/tests/proptest/operations.rs:389, with a FIXME bug note at :394
- [`beacon_node/store/src/state_cache.rs:197-208`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L197-L208) rebase_on_finalized and [`beacon_node/beacon_chain/src/beacon_chain.rs:7840`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7840) rebase_on are whole-state rebases against another state for disk-loaded states, not after epoch updates

**Second check.** Searched for intra_rebase, rebase_on and .rebase( across the repo and milhouse d67aabd. The only related mechanisms are the zero-score make_mut skip and whole-state rebase_on for states loaded from disk. Neither dedups a list that was rewritten in bulk.

**Sources.** [lighthouse#7062](https://github.com/sigp/lighthouse/pull/7062)

</details>


<a id="state_cache-134"></a>
<details>
<summary><b>state_cache-134</b> Load states onto an existing in-memory tree — <i>implemented · medium · S · memory, cpu, startup</i></summary>

**Idea.** When deserializing a state (diff application, checkpoint-sync anchor), build it onto an already loaded related state's tree, reusing unchanged subtrees and applying only modified entries, so loaded states share memory and are not re-hashed.

**Gap in Lighthouse.** Done by rebasing after deserialising rather than deserialising directly onto the base tree: a transient full tree is still built first. Checkpoint-sync anchor path not checked for rebase.

**Impact.** Loaded hot states share memory and hashes with the finalized state; only the transient allocation and deserialisation CPU remain, which would need a diff-applied-onto-tree loader to remove.

**Best measured result.** startup blocking of ~24s removed after download (pr:lodestar#7056)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hdiff.rs:210`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L210) HDiffBuffer::as_state builds state from SSZ + balances/validators/inactivity lists
- [`beacon_node/store/src/hot_cold_store.rs:1984-1988`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1984-L1988) and 2009-2013 rebase_on_finalized right after loading a diff/replay base state
- [`beacon_node/store/src/state_cache.rs:197`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L197) rebase_on_finalized; [`consensus/types/src/state/beacon_state.rs:3416`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3416) BeaconState::rebase_on (milhouse Tree::rebase_on reuses base subtrees and their cached hashes) plus rebase_caches_on:3515
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7836-7841`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7836-L7841) chain dump also rebases on previous state

**Sources.** [lodestar#6057](https://github.com/ChainSafe/lodestar/pull/6057), [lighthouse#4416](https://github.com/sigp/lighthouse/pull/4416), [lodestar#7056](https://github.com/ChainSafe/lodestar/pull/7056)

</details>


<a id="state_cache-136"></a>
<details>
<summary><b>state_cache-136</b> Pool and reuse large state field buffers — <i>n/a · low · memory, cpu</i></summary>

**Idea.** Pool released large per-state arrays (randao mixes, 2D byte slices, COW buffers) and reuse them when a state field must be copied, instead of allocating new ones.

**Impact.** Tree-backed states copy only modified leaves, so pooling large flat arrays does not apply.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs): fields are milhouse persistent Lists/Vectors, clone shares nodes; no large per-state arrays copied
- no buffer pool found in store/src/state_cache.rs

**Sources.** [prysm#4824](https://github.com/OffchainLabs/prysm/pull/4824), [prysm#4903](https://github.com/OffchainLabs/prysm/pull/4903), [prysm#4896](https://github.com/OffchainLabs/prysm/pull/4896), [prysm#4811](https://github.com/OffchainLabs/prysm/pull/4811)

</details>


<a id="state_cache-138"></a>
<details>
<summary><b>state_cache-138</b> No state copies on head save and init sync — <i>n/a · medium · memory, sync</i></summary>

**Idea.** Do not copy the state when saving it as the head, and during initial sync (linear chain) return cached states without cloning and skip the skip-slot cache.

**Impact.** Prysm's deep-copy cost does not exist in Lighthouse: cloning a milhouse-backed state is cheap and there is no skip-slot cache.

**Best measured result.** Memory reduction down from 3GB to 600MB (pr:prysm#5778)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs): BeaconState uses milhouse persistent trees, clone is Arc-shared
- [`beacon_node/store/src/state_cache.rs:236`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L236) put_state clones the state (cheap structural share); no skip-slot cache module in [`beacon_node/beacon_chain/src`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src)

**Sources.** [prysm#5760](https://github.com/OffchainLabs/prysm/pull/5760), [prysm#5778](https://github.com/OffchainLabs/prysm/pull/5778)

</details>


<a id="state_cache-139"></a>
<details>
<summary><b>state_cache-139</b> Read-only field accessors without state copy — <i>implemented · low · memory, cpu</i></summary>

**Idea.** Provide read-only accessors on the state for validators and balance sums, so callers needing a few fields do not deep-copy the validator list or whole state.

**Impact.** Borrowing accessors on milhouse lists exist; clone is cheap anyway.

**Best measured result.** many times faster and doesn't require making copies (pr:prysm#13782)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:2408`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2408) get_validator returns &amp;Validator
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs):~95 validators().iter_from(n) borrows without copying

**Sources.** [prysm#16355](https://github.com/OffchainLabs/prysm/pull/16355), [prysm#13782](https://github.com/OffchainLabs/prysm/pull/13782)

</details>


<a id="state_cache-144"></a>
<details>
<summary><b>state_cache-144</b> Compact flattened checkpoint state — <i>n/a · medium · memory, cpu</i></summary>

**Idea.** Keep checkpoint states in a compact form: a pubkey array shared with the anchor state, balances only, active/slashed bitsets and one shuffled set.

**Impact.** Checkpoint states are structurally shared clones (validators list, pubkey cache), so a separate flattened compact form would add little.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:46-55`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L46-L55) cache holds full BeaconState values that share tree nodes via milhouse
- [`consensus/types/src/state/beacon_state.rs:3515`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3515) rebase_caches_on shares pubkey and committee caches between states

**Sources.** [caplin#8482](https://github.com/erigontech/erigon/pull/8482)

</details>


<a id="state_cache-149"></a>
<details>
<summary><b>state_cache-149</b> In-memory LRU of recent hot states — <i>implemented · medium · memory, latency, disk, cpu</i></summary>

**Idea.** Keep recent unfinalized post-states in an in-memory cache keyed by block root, so block import and duties do not read, write or replay states from the database.

**Impact.** Block import and duties already hit the in-memory cache, with the disk path as fallback.

**Best measured result.** hit ratio &gt;99% (cited from #4834) (pr:prysm#5004)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:46-55`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L46-L55) StateCache LRU keyed by state_root with block_map block_root-&gt;slot-&gt;state_root
- [`beacon_node/store/src/state_cache.rs:316`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L316) get_by_block_root; hot_cold_store.rs:1196 get_advanced_hot_state_from_cache
- [`beacon_node/store/src/config.rs:23`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L23) DEFAULT_STATE_CACHE_SIZE=128; hot_cold_store.rs:1661 store_hot_state fills the cache on import

**Sources.** [prysm#5004](https://github.com/OffchainLabs/prysm/pull/5004), [lodestar#910](https://github.com/ChainSafe/lodestar/pull/910), [nimbus#654](https://github.com/status-im/nimbus-eth2/pull/654)

</details>


<a id="state_cache-150"></a>
<details>
<summary><b>state_cache-150</b> Tune hot state cache size — <i>implemented · low · cpu, latency, memory, startup</i></summary>

**Idea.** Size the hot state cache large enough (e.g. 32 entries, larger at startup with many forks) to keep the miss rate low and avoid replay-based regeneration.

**Impact.** Cache default is 128, 4x the 32 suggested; already tunable via --state-cache-size.

**Best measured result.** hot state miss rate ~4% to 2% (pr:prysm#6033)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/config.rs:23`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L23) DEFAULT_STATE_CACHE_SIZE=128
- [`beacon_node/store/src/state_cache.rs:45`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L45) LRU state cache + hdiff buffer cache
- [`beacon_node/store/src/hot_cold_store.rs:1817`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1817) get_hot_state checks cache first, warns on miss

**Sources.** [prysm#7340](https://github.com/OffchainLabs/prysm/pull/7340), [prysm#6033](https://github.com/OffchainLabs/prysm/pull/6033), [teku#2591](https://github.com/Consensys-Incorporated/teku/pull/2591)

</details>


<a id="state_cache-151"></a>
<details>
<summary><b>state_cache-151</b> Store sparse states, regenerate by replay — <i>implemented · low · memory, disk, cpu, latency</i></summary>

**Idea.** Persist only periodic archive/restore-point states plus summaries and regenerate any other state by loading the nearest saved state and replaying blocks forward, instead of storing every state.

**Impact.** Hot states stored as periodic snapshots/diffs plus summaries and replayed; cold states use hierarchical diffs.

**Best measured result.** exp pods used 500MB less (from related flag PRs) (pr:prysm#6087)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1949`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1949) load_hot_state loads summary, diff base, then replays blocks
- [`beacon_node/store/src/hot_cold_store.rs:1968`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1968) hot_storage_strategy(slot) snapshot/diff/replay
- [`beacon_node/store/src/hdiff.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs) hierarchical diffs for cold states

**Sources.** [prysm#6087](https://github.com/OffchainLabs/prysm/pull/6087), [prysm#4834](https://github.com/OffchainLabs/prysm/pull/4834), [prysm#5393](https://github.com/OffchainLabs/prysm/pull/5393), [prysm#5108](https://github.com/OffchainLabs/prysm/pull/5108), [prysm#4877](https://github.com/OffchainLabs/prysm/pull/4877)

</details>


<a id="state_cache-152"></a>
<details>
<summary><b>state_cache-152</b> Do not pin disk-loaded states in cache — <i>implemented · medium · memory, disk</i></summary>

**Idea.** Keep states loaded from storage in the cache only on demand rather than pinning them, so cold states do not hold memory.

**Impact.** Cold or API loads can skip the cache and cached ones are evictable; no pinning.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1815-1850`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1815-L1850) get_hot_state only inserts disk-loaded states into the cache when update_cache is true
- [`beacon_node/store/src/state_cache.rs:357`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L357) cull evicts LRU with priority order, so loaded states are not pinned (only head and the 10% most recent are exempt)

**Sources.** [grandine@ce7476aa0](https://github.com/grandinetech/grandine/commit/ce7476aa0a0d)

</details>


<a id="state_cache-153"></a>
<details>
<summary><b>state_cache-153</b> Periodic hot state snapshots in long non-finality — <i>implemented · medium · memory, disk</i></summary>

**Idea.** During long non-finality persist a hot state every N slots so regeneration replays stay short, and delete them after finalization.

**Impact.** Replays are bounded to at most about one epoch of blocks even in long non-finality via on-disk epoch diffs, deleted/migrated at finalization; no regeneration spikes like Prysm's.

**Best measured result.** about 2GB extra disk on Medalla; memory spikes from replay otherwise (pr:prysm#7597)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hdiff.rs:619-624`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L619-L624) default hot hierarchy exponents [5,9,11,13,16,18,21]: a diff or snapshot every 32 slots (one epoch)
- [`beacon_node/store/src/hot_cold_store.rs:1706-1707`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1706-L1707) store_hot_state_summary+store_hot_state_diffs on each stored state; hot_storage_strategy:407
- [`beacon_node/beacon_chain/src/migrate.rs:509`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L509) prune_hot_db removes non-finalized-chain states after finalization

**Sources.** [prysm#7597](https://github.com/OffchainLabs/prysm/pull/7597)

</details>


<a id="state_cache-154"></a>
<details>
<summary><b>state_cache-154</b> Prune before persisting checkpoint states — <i>n/a · low · disk, memory</i></summary>

**Idea.** Prune finalized checkpoint states before persisting in one serialized flow, so a racing prune cannot orphan files and soon-pruned states are not serialized.

**Impact.** Lighthouse has no separate on-disk checkpoint-state file store (states go in DB with summaries), so there are no orphan files to race with pruning.

**Best measured result.** persisted checkpoint states grew ~197MB per orphan file (screenshot) (pr:lodestar#9463)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1068`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1068) put_state writes to hot/cold DB, not per-checkpoint files
- [`beacon_node/store/src/state_cache.rs:127`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L127) update_finalized_state prunes in-memory

**Sources.** [lodestar#9463](https://github.com/ChainSafe/lodestar/pull/9463)

</details>


<a id="state_cache-155"></a>
<details>
<summary><b>state_cache-155</b> Prune on-disk states one epoch behind finality — <i>implemented · medium · disk</i></summary>

**Idea.** Prune stored fork states up to one epoch behind the finalized slot (cutoff from the highest slot with a stored state), then drop fork-graph blocks older than the oldest stored state.

**Impact.** Hot DB state pruning at finalization exists; the one-epoch-behind cutoff and fork-graph block cutoff are Caplin-specific and not needed given Lighthouse prunes by finalized-checkpoint DAG.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/migrate.rs:509-720`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L509-L720) prune_hot_db prunes states of chains conflicting with the new finalized checkpoint and states before it, keeping only hdiff grid points
- [`beacon_node/store/src/state_cache.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs):~160 update_finalized_state prunes block_map below the finalized slot

**Sources.** [caplin#11219](https://github.com/erigontech/erigon/pull/11219), [caplin#11472](https://github.com/erigontech/erigon/pull/11472)

</details>


<a id="state_cache-157"></a>
<details>
<summary><b>state_cache-157</b> Historical state regen on dedicated worker — <i>partial · medium · M · cpu, latency</i></summary>

**Idea.** Serve historical state requests from a separate worker thread with its own regen queue and persisted pubkey index, so old-state API work does not block the main thread.

**Gap in Lighthouse.** Historic state requests are bounded and deprioritised in the shared beacon processor P1 queue with their own historic state cache, but they still run on the shared worker pool; no dedicated historic-state worker or separate regen queue. Lodestar's main-thread problem does not apply to multi-threaded Lighthouse.

**Impact.** Only matters for nodes serving heavy historical state API load; a long cold-state replay can hold one shared worker.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/task_spawner.rs:22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/task_spawner.rs#L22) API work goes into beacon processor ApiRequestP0/P1 queues
- [`beacon_node/beacon_processor/src/lib.rs:1153`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1153) api_request_p1_queue popped only after gossip/import work
- [`beacon_node/http_api/src/lib.rs:588`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L588) state endpoints use Priority::P1
- [`beacon_node/store/src/hot_cold_store.rs:2310`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2310) separate historic_state_cache for cold states

**Sources.** [lodestar#6033](https://github.com/ChainSafe/lodestar/pull/6033)

</details>


<a id="state_cache-159"></a>
<details>
<summary><b>state_cache-159</b> State cache during initial sync — <i>implemented · medium · sync</i></summary>

**Idea.** Keep states in a cache between consecutive blocks during initial sync, avoiding DB saves and loads per block.

**Impact.** Parent state for next block is served from StateCache so sync does not reload from disk per block.

**Best measured result.** "significant increase to sync speed" (pr:prysm#4938)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:215`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L215) put_state: post-state kept in in-memory LRU (default 128, config.rs:23)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4752`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4752) PutState on block import
- [`beacon_node/store/src/hot_cold_store.rs:1124`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1124) get_advanced_hot_state hits cache for parent state

**Sources.** [prysm#4938](https://github.com/OffchainLabs/prysm/pull/4938)

</details>


<a id="state_cache-160"></a>
<details>
<summary><b>state_cache-160</b> Free sync caches after range sync — <i>n/a · low · memory</i></summary>

**Idea.** Clear initial-sync state caches once range sync finishes, to release memory.

**Impact.** Lighthouse has no separate initial-sync state cache; range sync uses the one bounded LRU state cache that culls on finalization.

**Best measured result.** States were using 600mb in memory after sync (pr:prysm#4817)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:127`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L127) update_finalized_state / :357 cull bound the shared state cache
- [`beacon_node/store/src/state_cache.rs:45`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L45) single capped LRU, no separate sync-state cache

**Sources.** [prysm#4817](https://github.com/OffchainLabs/prysm/pull/4817)

</details>


<a id="state_cache-161"></a>
<details>
<summary><b>state_cache-161</b> Fewer state dumps during forward sync — <i>implemented · medium · memory, cpu</i></summary>

**Idea.** During forward sync save or dump states only at epoch-multiple slots and prune finalized cache entries later, cutting per-block state copies.

**Impact.** Non-grid slots persist only a small summary, so per-block state dumps are already avoided; states are cheap clones via milhouse.

**Best measured result.** 10x less memory allocs during forward sync (pr:caplin#11815)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1667`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1667) store_hot_state: cache first, DB only writes summary
- [`beacon_node/store/src/hot_cold_store.rs:1733`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1733) store_hot_state_diffs: full snapshot/diff only on hierarchy grid slots, ReplayFrom otherwise
- [`beacon_node/store/src/state_cache.rs:127`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L127) update_finalized_state prunes pre-finalized states

**Sources.** [caplin#11815](https://github.com/erigontech/erigon/pull/11815)

</details>


<a id="state_cache-162"></a>
<details>
<summary><b>state_cache-162</b> Pre-advance head state and serve consumers from it — <i>implemented · high · latency, cpu, memory</i></summary>

**Idea.** Before the next slot, advance the head state through the empty slot (and epoch transition) in the background and cache it, then serve block import, proposal, gossip validation, payload attributes, sync committee and duty lookups from it, so these paths skip slot processing on the critical path. Watch its memory cost.

**Impact.** None needed.

**Best measured result.** 30% memory increase seen on develop, suspected cause (pr:prysm#8855)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:122`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L122) advance at 3/4 slot
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:273`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L273) advance_head per_slot_processing + epoch transition
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:446`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L446) put_state of advanced state; get_advanced_hot_state serves block import (store/src/hot_cold_store.rs:1124)
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:395`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L395) primes proposer and shuffling caches

**Sources.** [prysm#10110](https://github.com/OffchainLabs/prysm/pull/10110), [prysm#8855](https://github.com/OffchainLabs/prysm/pull/8855), [prysm#12233](https://github.com/OffchainLabs/prysm/pull/12233), [prysm#8830](https://github.com/OffchainLabs/prysm/pull/8830), [prysm#8357](https://github.com/OffchainLabs/prysm/pull/8357), [prysm#16454](https://github.com/OffchainLabs/prysm/pull/16454), [prysm#16439](https://github.com/OffchainLabs/prysm/pull/16439), [prysm#8398](https://github.com/OffchainLabs/prysm/pull/8398), [prysm#9167](https://github.com/OffchainLabs/prysm/pull/9167), [prysm#9200](https://github.com/OffchainLabs/prysm/pull/9200), [lighthouse#4415](https://github.com/sigp/lighthouse/pull/4415), [prysm#12286](https://github.com/OffchainLabs/prysm/pull/12286), [prysm#12288](https://github.com/OffchainLabs/prysm/pull/12288), [prysm#12287](https://github.com/OffchainLabs/prysm/pull/12287), [prysm#9884](https://github.com/OffchainLabs/prysm/pull/9884)

</details>


<a id="state_cache-163"></a>
<details>
<summary><b>state_cache-163</b> Precompute state one epoch ahead at epoch end — <i>implemented · medium · S · latency, cpu</i></summary>

**Idea.** On the last slot of an epoch allow precomputing states one epoch further ahead, so the next epoch-boundary state is ready earlier.

**Impact.** Already present: the next epoch-boundary state and its shufflings are ready before the epoch starts.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:258`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L258) advance_head advances head state into the next slot (the epoch boundary on the last slot) before the slot starts and puts it in the state cache
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:345`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L345) when the advance crosses an epoch, primes proposer caches for the current and next epoch and the next-epoch attester shuffling
- [`beacon_node/http_api/src/attester_duties.rs:30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L30) tolerant_current_epoch accepts requests one epoch further near the boundary
- [`beacon_node/http_api/src/proposer_duties.rs:69`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/proposer_duties.rs#L69) same tolerance for proposer duties

**Sources.** [grandine#269](https://github.com/grandinetech/grandine/pull/269)

</details>


<a id="state_cache-167"></a>
<details>
<summary><b>state_cache-167</b> State existence check without reading state — <i>not · low · S · latency, disk</i></summary>

**Idea.** Implement has_state as a pure existence check: look in the cache without touching LRU order, then probe DB keys, never reading and decoding a full state.

**Gap in Lighthouse.** A cheap state-exists helper would check state_cache without LRU promotion and then probe the hot state summary key; no production caller currently needs it and none does a full state load just to test existence, so it is a minor API gap.

**Impact.** Negligible on a mainnet node: no hot-path caller found that decodes a state merely to check existence.

**Best measured result.** has_state guard p50 180 ms, p90 332 ms, max 536 ms on the block after each epoch's first block; 0-1 ms on most others (pr:ethlambda#658)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3000`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3000) load_hot_state_summary exists (summary-only read)
- [`beacon_node/store/src/hot_cold_store.rs:1087`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1087) get_state fully loads state; grep for has_state/state_exists found only test helpers
- [`beacon_node/store/src/state_cache.rs:275`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L275) get_by_state_root touches LRU order

**Sources.** [ethlambda#658](https://github.com/lambdaclass/ethlambda/pull/658)

</details>


<a id="state_cache-169"></a>
<details>
<summary><b>state_cache-169</b> Advance clone before storing checkpoint state — <i>n/a · medium · S · cpu, memory</i></summary>

**Idea.** In the checkpoint-state cache, clone the base state before advancing slots and store the advanced copy, so later attestations hit the cache and skip clone plus process_slots.

**Gap in Lighthouse.** Lighthouse has no checkpoint-state cache: attestation verification uses the shuffling cache keyed by decision root, so there is no target-state clone plus process_slots on that path.

**Impact.** None for gossip attestation verification; production path (produce_unaggregated_attestation) could cache the advanced state, minor.

**Best measured result.** Flame graph: clone much smaller after fix; no number (pr:prysm#4288)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:128`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L128) ShufflingCache serves attestation verification without a target state
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7593`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7593) with_committee_cache
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2164`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2164) only attestation production advances a clone

**Sources.** [prysm#4288](https://github.com/OffchainLabs/prysm/pull/4288)

</details>


<a id="state_cache-170"></a>
<details>
<summary><b>state_cache-170</b> Past-epoch block root lookup in checkpoint processing — <i>n/a · high · memory</i></summary>

**Idea.** Handle past-epoch processing so block-root lookups in checkpoint-state processing near head do not fail and trigger regeneration loops that OOM.

**Impact.** Lodestar-specific bug in persistent checkpoint cache regen; Lighthouse has no checkpoint state cache or regen loop.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1124`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1124) get_advanced_hot_state: states looked up by block root and advanced, no checkpoint-state cache
- [`beacon_node/store/src/hot_cold_store.rs:2031`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2031) load_hot_state_using_replay uses roots from stored state/iterators

**Sources.** [lodestar#7505](https://github.com/ChainSafe/lodestar/pull/7505)

</details>


<a id="state_cache-171"></a>
<details>
<summary><b>state_cache-171</b> Global active validator cache across state copies — <i>partial · medium · S · cpu, memory</i></summary>

**Idea.** Share a process-wide active-validator-index and total-active-balance cache keyed by epoch and dependent root across all state copies, filled even without balances, so the full validator scan runs once per epoch per fork.

**Gap in Lighthouse.** Active indices are shared globally and total active balance comes free from single-pass epoch processing, but the balance value is per state; states rebuilt from disk without the cache rescan validators. Would add a process-wide (epoch, decision root) -&gt; total_active_balance map.

**Impact.** Saves one O(validators) scan per reloaded state per epoch; minor.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:128`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L128) global shuffling cache keyed by (epoch, decision root) holds active indices
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:482`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L482) epoch transition sets next-epoch total active balance without an extra scan
- [`consensus/types/src/state/beacon_state.rs:2724`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2724) force_build_total_active_balance_cache full scan for states without the cache

**Sources.** [caplin#18525](https://github.com/erigontech/erigon/pull/18525), [caplin#18554](https://github.com/erigontech/erigon/pull/18554)

</details>


<a id="state_cache-172"></a>
<details>
<summary><b>state_cache-172</b> Keep previous head state for reorgs — <i>implemented · low · disk, memory, latency</i></summary>

**Idea.** Keep the head-1 state in memory, updated by copy-into, for fast 1-block reorgs, replacing a disk-backed merkle cache.

**Impact.** Recent states (including head's parent) are held in the in-memory state cache with structural sharing (milhouse), so 1-block reorgs hit cache; no separate disk-backed merkle cache.

**Best measured result.** less I/O and less RAM + faster reorg speed (pr:caplin#13671)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1196`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1196) get_advanced_hot_state_from_cache by block_root
- [`beacon_node/store/src/state_cache.rs:316`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L316) get_by_block_root
- [`beacon_node/store/src/state_cache.rs:45`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L45) 128-state in-memory cache keyed by block root

**Sources.** [caplin#13671](https://github.com/erigontech/erigon/pull/13671)

</details>


<a id="state_cache-173"></a>
<details>
<summary><b>state_cache-173</b> Dedicated justified state cache for fork choice — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** Keep a dedicated cached state for the justified checkpoint used by fork choice, and skip scheduled per-slot work when the node is behind the clock.

**Impact.** Fork choice avoids loading the justified state via the balances cache, and per-slot advance is skipped when behind.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_fork_choice_store.rs:59`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_fork_choice_store.rs#L59) BalancesCache keyed by block root holds JustifiedBalances
- [`beacon_node/beacon_chain/src/beacon_fork_choice_store.rs:341`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_fork_choice_store.rs#L341) set_justified_checkpoint uses cache before loading a state
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:269`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L269) skips advance when head is &gt;256 slots behind

**Sources.** [nimbus@e7b36c438](https://github.com/status-im/nimbus-eth2/commit/e7b36c438952)

</details>


<a id="state_cache-176"></a>
<details>
<summary><b>state_cache-176</b> Limit speculative proposer-prediction replays — <i>n/a · low · latency, cpu, disk</i></summary>

**Idea.** Skip the speculative next-epoch proposer prediction that replays states except in the last slot of the epoch.

**Impact.** Lighthouse primes proposer shuffling from the single state-advance copy, with no speculative multi-state replay.

**Best measured result.** 5s+ replays each slot on Holesky (replayDur=5s418ms) (pr:nimbus#7072)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:355-390`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L355-L390) proposer cache primed from the already-advanced head state
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:373`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L373) next-epoch shuffling taken from the state (Fulu lookahead), no replay

**Sources.** [nimbus#7072](https://github.com/status-im/nimbus-eth2/pull/7072)

</details>


<a id="state_cache-177"></a>
<details>
<summary><b>state_cache-177</b> Resolve block roots from state block_roots — <i>implemented · low · sync, startup</i></summary>

**Idea.** After checkpoint sync, answer block-at-slot queries from block_roots of in-memory states (up to SLOTS_PER_HISTORICAL_ROOT back) so dependent roots resolve before backfill.

**Impact.** Recent block roots are read from the head state's block_roots via the hybrid forwards iterator, so queries resolve before backfill.

**Best measured result.** accelerates the first couple minutes of checkpoint sync on mainnet (pr:nimbus#5869)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:839`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L839) forwards_block_roots_iterator_until with head state fallback
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1095`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1095) block_root_at_slot uses it
- [`beacon_node/store/src/forwards_iter.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/forwards_iter.rs) head-state block_roots used for recent slots

**Sources.** [nimbus#5869](https://github.com/status-im/nimbus-eth2/pull/5869)

</details>


<a id="state_cache-178"></a>
<details>
<summary><b>state_cache-178</b> Non-blocking try-lock in cache pruning — <i>n/a · low · S · latency, cpu</i></summary>

**Idea.** During state cache pruning use try-lock and skip busy entries (retrying at next prune) instead of waiting with a timeout, and remove emptied entries under a single lock acquisition.

**Impact.** None: states are owned values in a HashMap under one mutex, there are no per-entry locks to wait on; prune is a single in-memory pass.

**Best measured result.** waiting 1.5 s per busy entry adds up to minutes (commit:grandine@2ec9f905fd7e)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:82`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L82) state_cache is one parking_lot Mutex&lt;StateCache&gt;, plain lock()
- [`beacon_node/store/src/state_cache.rs:127-170`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L127-L170) update_finalized_state prunes block_map and states synchronously under that one lock; no per-entry locks
- [`beacon_node/store/src/state_cache.rs:421`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L421) BlockMap::prune is a retain pass

**Sources.** [grandine@2ec9f905f](https://github.com/grandinetech/grandine/commit/2ec9f905fd7e), [grandine#950](https://github.com/grandinetech/grandine/pull/950)

</details>


<a id="state_cache-179"></a>
<details>
<summary><b>state_cache-179</b> Run state cache pruning off the store lock — <i>implemented · medium · S · latency</i></summary>

**Idea.** Spawn state cache pruning as a separate task instead of running it while holding the fork-choice store lock, so other fork-choice operations are not blocked.

**Impact.** Already present: finalization pruning runs on a background thread and never blocks fork choice.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3665`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3665) migrate_database calls update_finalized_state (state cache prune)
- [`beacon_node/beacon_chain/src/migrate.rs:348`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L348) migrate_database runs on the BackgroundMigrator thread, which does not touch fork choice or canonical_head
- [`beacon_node/store/src/hot_cold_store.rs:434`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L434) pruning holds only the state_cache mutex
- [`beacon_node/store/src/state_cache.rs:256`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L256) LRU cull in put_state is batched by headroom

**Sources.** [grandine#522](https://github.com/grandinetech/grandine/pull/522), [grandine@c726d6341](https://github.com/grandinetech/grandine/commit/c726d6341b3c)

</details>


<a id="state_cache-181"></a>
<details>
<summary><b>state_cache-181</b> Transfer hash caches only to imported clone — <i>n/a · medium · cpu</i></summary>

**Idea.** On block import, give the tree-hash/serialization caches only to the state clone that is imported, not throwaway clones for validation, production or next-slot prep.

**Impact.** Tree-hash caches live inside the milhouse persistent tree, so state clones share them structurally; there is no per-clone cache to hand over, nothing to save.

**Best measured result.** motivated by metrics showing the SSZ cache almost never populated; no numbers (pr:lodestar#5172)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1148`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1148) update_tree_hash_cache on loaded state
- [`beacon_node/store/src/state_cache.rs:253`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L253) put_state clones state

**Sources.** [lodestar#5172](https://github.com/ChainSafe/lodestar/pull/5172)

</details>


<a id="state_cache-183"></a>
<details>
<summary><b>state_cache-183</b> Epoch-matching state cache for attestations — <i>implemented · medium · sync, cpu</i></summary>

**Idea.** In attestation handling check the target epoch before rewinding, let the state cache match by epoch rather than exact slot, and store the updated state so repeated lookups hit.

**Impact.** Attestations avoid state lookups via an epoch-keyed shuffling cache; already the same effect.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:315`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L315) with_cached_shuffling keyed by AttestationShufflingId (epoch+decision root), not slot
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:353`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L353) promise inserted so repeated lookups hit
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:403`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L403) primes next-epoch shuffling

**Sources.** [nimbus#1348](https://github.com/status-im/nimbus-eth2/pull/1348)

</details>


<a id="state_cache-184"></a>
<details>
<summary><b>state_cache-184</b> Rebase clearance state on head during chain stall — <i>implemented · medium · latency</i></summary>

**Idea.** When the chain stalls, rebase the block clearance/advance state on the fork-choice head so a proposer does not have to catch up a long run of empty slots before it can propose.

**Impact.** During a stall the advance timer advances the cached head state one more slot per slot, so the proposer finds it near-current; capped by MAX_ADVANCE_DISTANCE=256 slots.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:283`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L283) advance_head takes the most advanced cached head state each slot
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:432`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L432) put_state of advanced state
- [`beacon_node/beacon_chain/src/block_production/mod.rs:89`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L89) proposer fetches advanced state via get_advanced_hot_state
- [`beacon_node/store/src/state_cache.rs:316`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L316) get_by_block_root picks highest slot &lt;= max_slot

**Sources.** [nimbus#6108](https://github.com/status-im/nimbus-eth2/pull/6108)

</details>


<a id="state_cache-186"></a>
<details>
<summary><b>state_cache-186</b> Bound the number of full states held in memory — <i>implemented · high · memory</i></summary>

**Idea.** Cap the hot state/checkpoint cache to a small number of full states (fewer entries, every other slot, a bounded number of epochs) and regenerate the rest on demand, because each epoch-boundary state can cost hundreds of MB and unbounded caches OOM during non-finality.

**Impact.** Cache bounded at 128 (CLI --state-cache-size); cull on overflow, evicted states reload from disk. Default is larger than the 32 of the lighthouse PR but states share structure.

**Best measured result.** 128 entries ~20GB; 32 x 180MB ~ 6GB (pr:lighthouse#7055)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/config.rs:23`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L23) DEFAULT_STATE_CACHE_SIZE=128 (bounded LRU)
- [`beacon_node/store/src/state_cache.rs:357`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L357) cull prefers advanced/old boundary/mid-epoch states
- [`beacon_node/store/src/state_cache.rs:240`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L240) only fully-merkleised states cached; structural sharing keeps cost low

**Sources.** [teku#2294](https://github.com/Consensys-Incorporated/teku/pull/2294), [lighthouse#7055](https://github.com/sigp/lighthouse/pull/7055), [lighthouse#7101](https://github.com/sigp/lighthouse/pull/7101), [nimbus#1290](https://github.com/status-im/nimbus-eth2/pull/1290), [nimbus@fc8502c54](https://github.com/status-im/nimbus-eth2/commit/fc8502c54e35), [grandine#87](https://github.com/grandinetech/grandine/pull/87)

</details>


<a id="state_cache-187"></a>
<details>
<summary><b>state_cache-187</b> Do expensive state work outside the cache lock — <i>implemented · medium · latency, cpu</i></summary>

**Idea.** Do not hold the state or shuffling cache lock while computing or waiting for a state, shuffling or diff buffer; release the lock first and share the result through a promise or once-cell, so other threads are not blocked.

**Impact.** Already done by PRs #3589 and #8176; no lock held across state or diff-buffer loads.

**Best measured result.** HDiffBuffer::from_state can take up to 1s under lock (pr:lighthouse#8176)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1817-1860`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1817-L1860) get_hot_state takes the lock only for lookup and put, loads from disk unlocked
- [`beacon_node/store/src/hot_cold_store.rs:1920`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1920) load_hot_hdiff_buffer same pattern
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:370-380`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L370-L380) promise then drop write lock before computing
- [`beacon_node/store/src/hot_cold_store.rs:2310-2319`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2310-L2319) historic cache lock dropped before reconstruct

**Sources.** [lighthouse#3589](https://github.com/sigp/lighthouse/pull/3589), [lighthouse#8176](https://github.com/sigp/lighthouse/pull/8176), [teku#2664](https://github.com/Consensys-Incorporated/teku/pull/2664)

</details>


<a id="state_cache-188"></a>
<details>
<summary><b>state_cache-188</b> Check in-memory caches before DB state loads — <i>implemented · medium · latency, disk, cpu</i></summary>

**Idea.** On hot state-by-root and block-and-state lookups, check the in-memory state caches (hot cache, finalized state) first and fall back to a database load and replay only on a miss.

**Impact.** Cache first, DB load and replay only on miss.

**Best measured result.** avoids a lot of regenerated states (pr:teku#2610)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1130`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1130) get_advanced_hot_state checks state_cache first
- [`beacon_node/store/src/hot_cold_store.rs:1817`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1817) get_hot_state checks cache first
- [`beacon_node/store/src/state_cache.rs:275`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L275) get_by_state_root also serves finalized_state

**Sources.** [prysm#7674](https://github.com/OffchainLabs/prysm/pull/7674), [teku#2610](https://github.com/Consensys-Incorporated/teku/pull/2610)

</details>


<a id="state_cache-195"></a>
<details>
<summary><b>state_cache-195</b> Rebuild pruned pre-state for delayed sidecar blocks — <i>n/a · medium · sync</i></summary>

**Idea.** When a block delayed on blobs/data columns needs a pre-state that was pruned from cache, rebuild it through the state cache and retry instead of dropping the block.

**Impact.** Lighthouse executes the block (state transition) before waiting for blobs/columns and parks the executed block with its post-state, so no pruned pre-state is needed later; any miss at verification already rebuilds from DB.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:2065`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L2065) pre-state loaded with get_advanced_hot_state (rebuilds on cache miss) at verification time
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:439`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L439) AvailabilityPendingExecutedBlock keeps already-executed block

**Sources.** [grandine@324854cde](https://github.com/grandinetech/grandine/commit/324854cde1bd)

</details>


<a id="state_cache-196"></a>
<details>
<summary><b>state_cache-196</b> Reuse the block post-state as new head state — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** After importing a block, take the new head state from the post-state already in hand (or the clearance state) rather than requesting or replaying it from the state generator, which can also evict the cached pre-state needed next.

**Impact.** Head state comes from the cached post-state; no regeneration and the pre-state is not evicted for it.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:4752`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4752) StoreOp::PutState of the block post-state on import
- [`beacon_node/store/src/hot_cold_store.rs:1666`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1666) store_hot_state puts into state_cache
- [`beacon_node/beacon_chain/src/canonical_head.rs:1137`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1137) new head state read via get_advanced_hot_state hits cache
- [`beacon_node/store/src/state_cache.rs:383`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L383) head state never culled

**Sources.** [nimbus#1388](https://github.com/status-im/nimbus-eth2/pull/1388), [prysm#6729](https://github.com/OffchainLabs/prysm/pull/6729)

</details>


<a id="state_cache-198"></a>
<details>
<summary><b>state_cache-198</b> Archive persisted checkpoint bytes without re-serializing — <i>not · medium · S · cpu, disk</i></summary>

**Idea.** When a finalized checkpoint state is already persisted on disk, archive its stored bytes directly instead of deserializing and re-serializing the state.

**Gap in Lighthouse.** In migrate_database, when cold_storage_strategy(slot) is Snapshot and the hot DB holds a BeaconStateHotSnapshot for that root, copy the compressed bytes straight into BeaconStateSnapshot (keyed by slot) plus the cold summary, skipping get_hot_state and re-encode/re-compress. Diff layers cannot reuse bytes (different bases).

**Impact.** Tiny: only archive nodes, only cold-snapshot-layer slots that are also hot snapshots; saves one SSZ encode + zstd compress (and decode on cache miss) per rare snapshot.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3604-3610`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3604-L3610) migrate_database calls get_hot_state then store_cold_state for non-replay slots
- [`beacon_node/store/src/hot_cold_store.rs:1817-1819`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1817-L1819) get_hot_state returns state-cache hit (skips decode) but otherwise load_hot_state + tree hash + build_all_caches
- [`beacon_node/store/src/hot_cold_store.rs:2143-2163`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2143-L2163) store_cold_state_as_snapshot always as_ssz_bytes + zstd re-compress
- [`beacon_node/store/src/hot_cold_store.rs:2182-2209`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2182-L2209) hot snapshot already stored zstd-compressed under BeaconStateHotSnapshot (same format)
- [`beacon_node/store/src/hot_cold_store.rs:2212-2232`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2212-L2232) load_hot_state_bytes_as_snapshot exists but only used for decoding (line 2247), never for byte copy

**Second check.** Checked all store_cold_state callers (migrate_database, reconstruct.rs:180, genesis, store_state:1071) and the hot/cold snapshot byte helpers; none copy raw stored bytes. State cache hit only avoids the decode, not the re-serialization/compression.

**Sources.** [lodestar#6504](https://github.com/ChainSafe/lodestar/pull/6504)

</details>


<a id="state_cache-199"></a>
<details>
<summary><b>state_cache-199</b> Cache block post-states for block production — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Cache post-states (and block rewards) from block processing in a fine-grained-locked cache so block production reuses them rather than re-running state transitions.

**Impact.** Already avoids reloading/replaying states for block production; remaining cost is the unavoidable per-block state transition for the new block.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1667`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1667) store_hot_state puts every imported post-state in StateCache
- [`beacon_node/beacon_chain/src/block_production/mod.rs:89`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L89) production loads parent via get_advanced_hot_state (cache hit)
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:258`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L258) advance_head pre-advances head and caches it

**Sources.** [grandine@67b707828](https://github.com/grandinetech/grandine/commit/67b707828989)

</details>


<a id="state_cache-200"></a>
<details>
<summary><b>state_cache-200</b> Reuse prebuilt pubkey cache from anchor state — <i>implemented · low · S · startup, cpu</i></summary>

**Idea.** At startup, if the anchor state already carries a built pubkey cache, reuse it instead of rebuilding by deserializing all pubkeys.

**Impact.** Restart avoids decompressing validator keys; load still deserializes ~1M uncompressed keys one by one (sequential, no rayon in load_from_store), which could be parallelised for a few seconds.

**Best measured result.** ~30 seconds for 350k keys (pr:lodestar#4319)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:56-80`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L56-L80) load_from_store reads persisted decompressed keys from DB
- validator_pubkey_cache.rs:237-242 as_pubkey uses deserialize_uncompressed (no decompression)
- [`beacon_node/beacon_chain/src/builder.rs:860-875`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L860-L875) persisted cache reused and topped up from head state; only built from state when absent

**Sources.** [lodestar#4319](https://github.com/ChainSafe/lodestar/pull/4319)

</details>


<a id="state_cache-210"></a>
<details>
<summary><b>state_cache-210</b> Dedicated clearance state for block sync — <i>n/a · medium · S · sync, cpu</i></summary>

**Idea.** Use a separate state for block clearance so block sync does not alternate one temporary state between attestation and block use, which forces replays.

**Impact.** Lighthouse has no single shared temporary clearance state: each block gets a cloned (structurally shared) parent post-state from the keyed StateCache, so sync and attestation use do not alternate one state and force replays.

**Best measured result.** helps block sync speed a lot (pr:nimbus#1352)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:2063`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L2063) load_parent fetches parent post-state by block root from StateCache
- [`beacon_node/store/src/state_cache.rs:316`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L316) get_by_block_root

**Sources.** [nimbus#1352](https://github.com/status-im/nimbus-eth2/pull/1352)

</details>


<a id="state_cache-211"></a>
<details>
<summary><b>state_cache-211</b> Process block attestations in target order — <i>n/a · medium · S · cpu</i></summary>

**Idea.** Process a block's attestations sequentially ordered by target checkpoint so the first populates the checkpoint state cache and the rest hit it, instead of each recomputing the epoch-boundary state in parallel.

**Impact.** Lighthouse verifies block attestations on the single block pre-state with its committee caches and uses a promise-based ShufflingCache for gossip, so no per-attestation target checkpoint state is regenerated.

**Best measured result.** logs show ~1.8s processSlots repeated per attestation (pr:lodestar#1557)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:315`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L315) with_cached_shuffling
- [`consensus/state_processing/src/per_block_processing/process_operations.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs) (attestations processed in order on the one pre-state)

**Sources.** [lodestar#1557](https://github.com/ChainSafe/lodestar/pull/1557)

</details>


<a id="state_cache-214"></a>
<details>
<summary><b>state_cache-214</b> Predict next-epoch duties without state advance — <i>implemented · medium · S · cpu</i></summary>

**Idea.** Compute next-epoch attester shuffling and first proposer from the head state before the epoch boundary, skipping the full state advance when no effective balance can change.

**Impact.** Next-epoch attester shuffling already comes from the head-epoch state without a full boundary advance and post-Fulu proposers come from the lookahead vector; the timer also pre-advances off the critical path.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:410-423`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L410-L423) shuffling_epoch is served from a state advanced only to the start of the previous epoch (one-epoch lookahead)
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:342-420`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L342-L420) next-epoch proposer and attester shuffling primed after the pre-advance
- [`consensus/types/src/state/beacon_state.rs:761`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L761) proposer_lookahead in state (Fulu)

**Sources.** [nimbus#5414](https://github.com/status-im/nimbus-eth2/pull/5414)

</details>


<a id="state_cache-217"></a>
<details>
<summary><b>state_cache-217</b> State cache eviction policy and insertion rules — <i>implemented · medium · S · memory, cpu</i></summary>

**Idea.** Tune state cache insertion and eviction: true LRU order, never evict the head, evict old epoch-boundary states first, cache ancestors only on epoch boundaries, and do not insert states read by migration/pruning so they do not evict useful states.

**Impact.** Eviction policy already matches the idea; no further gain expected.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:357`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L357) cull: advanced, old boundary, mid-epoch, then could-finalize boundary order, head never culled, newest 10% exempt
- [`beacon_node/store/src/state_cache.rs:275`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L275) get_by_state_root uses hashlink LRU get (promotes)
- [`beacon_node/store/src/hot_cold_store.rs:2031-2060`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2031-L2060) ancestor states cached only on epoch boundaries and only if update_cache
- [`beacon_node/store/src/iter.rs:31`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/iter.rs#L31) and hot_cold_store.rs:3607 pruning/iteration reads use update_cache=false

**Sources.** [lighthouse#7067](https://github.com/sigp/lighthouse/pull/7067), [lighthouse#7095](https://github.com/sigp/lighthouse/pull/7095), [lighthouse#7364](https://github.com/sigp/lighthouse/pull/7364)

</details>


<a id="state_cache-223"></a>
<details>
<summary><b>state_cache-223</b> Skip state-root check when replaying stored blocks — <i>implemented · medium · S · cpu</i></summary>

**Idea.** When regenerating a state by replaying stored blocks, skip the per-block post-state hash tree root comparison against block.state_root.

**Impact.** Replay already skips the post-block state-root check; per-slot roots needed for history are taken from a state_root_iter when available.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/block_replayer.rs:241-250`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/block_replayer.rs#L241-L250) replay calls per_block_processing and never compares the post-state root with block.state_root
- [`beacon_node/store/src/hot_cold_store.rs:2565`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2565) replay_blocks uses no_signature_verification and minimal_block_root_verification

**Sources.** [teku#5316](https://github.com/Consensys-Incorporated/teku/pull/5316)

</details>


<a id="state_cache-224"></a>
<details>
<summary><b>state_cache-224</b> Skip block validation when replaying local blocks — <i>implemented · high · cpu</i></summary>

**Idea.** When regenerating states from blocks already validated on import, skip signature and other block validation.

**Impact.** Regeneration of hot states skips signature checks; replay still runs per_block_processing state transitions (needed).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2565`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2565) replay_blocks uses no_signature_verification + minimal_block_root_verification
- [`consensus/state_processing/src/block_replayer.rs:113`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/block_replayer.rs#L113) no_signature_verification

**Sources.** [teku#2203](https://github.com/Consensys-Incorporated/teku/pull/2203)

</details>


<a id="state_cache-225"></a>
<details>
<summary><b>state_cache-225</b> In-memory cache of diff base/snapshot states — <i>implemented · medium · S · disk, cpu, latency</i></summary>

**Idea.** Cache decoded hierarchical-diff base snapshots and buffers in memory (keyed by slot, holding either state or buffer form and converting lazily) so historic state loads skip DB reads and decoding and sequential queries reuse prior work.

**Impact.** Already caches diff base buffers and states and converts lazily; default sizes (historic_state_cache_size=1) are small and could be tuned.

**Best measured result.** Most sequential queries after the first served in 400-700ms on mainnet (hierarchy exponents 5,7,11) (pr:lighthouse#6475)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/historic_state_cache.rs:15`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/historic_state_cache.rs#L15) HistoricStateCache holds LRU of HDiffBuffer and BeaconState keyed by slot with lazy conversion
- [`beacon_node/store/src/hot_cold_store.rs:2310`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2310) and 2424 used when loading cold states
- [`beacon_node/store/src/state_cache.rs:284`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L284) hot hdiff buffer cache

**Sources.** [prysm#17573](https://github.com/OffchainLabs/prysm/pull/17573), [prysm#17561](https://github.com/OffchainLabs/prysm/pull/17561), [lighthouse#6475](https://github.com/sigp/lighthouse/pull/6475)

</details>


<a id="state_cache-229"></a>
<details>
<summary><b>state_cache-229</b> Shared state cache keyed by state root — <i>implemented · medium · S · cpu, disk</i></summary>

**Idea.** Keep an in-memory state cache keyed by state root used by block processing, attestation handling and block production to avoid DB reloads.

**Impact.** Shared state-root-keyed cache already serves block processing, attestation shuffling and production; the single Mutex is coarse but held briefly (clones are structural).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:82`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L82) StateCache keyed by state root (and block root map) behind a Mutex
- [`beacon_node/store/src/hot_cold_store.rs:1817`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1817) get_hot_state checks cache first
- [`beacon_node/beacon_chain/src/block_verification.rs:2065`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L2065), shuffling_cache.rs:436, block_production/mod.rs:89 all go through get_advanced_hot_state

**Sources.** [lodestar@2b026c147](https://github.com/ChainSafe/lodestar/commit/2b026c147049)

</details>


<a id="state_cache-231"></a>
<details>
<summary><b>state_cache-231</b> Store states as deltas over a base — <i>implemented · medium · disk, memory</i></summary>

**Idea.** Define delta types for validator identity and beacon state so stored states are deltas over a base state.

**Impact.** Already done: hot and cold states are stored as hierarchical diffs over snapshots.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hdiff.rs:127`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L127) HDiff with ValidatorsDiff over a base buffer
- [`beacon_node/store/src/hdiff.rs:622`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L622) default exponents [5,9,11,13,16,18,21]
- [`beacon_node/store/src/hot_cold_store.rs:1949`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1949) load_hot_state applies diffs from snapshot

**Sources.** [silver#40](https://github.com/gattaca-com/silver/pull/40)

</details>


<a id="state_cache-234"></a>
<details>
<summary><b>state_cache-234</b> Struct-of-arrays validators with shared pubkey list — <i>partial · medium · M · memory, cpu</i></summary>

**Idea.** Split the validator registry into an append-only pubkey list, effective balances and remaining fields, and share the pubkey list structurally between states so a state loaded from disk attaches it instead of copying every key.

**Gap in Lighthouse.** No struct-of-arrays split: pubkeys stay inline in each Validator leaf. Hot loads share nodes only via rebase_on_finalized (extra tree walk); cold/historic loads (load_cold_state_by_slot -&gt; HDiffBuffer::as_state) build a fresh validators List and are never rebased, so every historical state copies all keys. The chain-level ValidatorPubkeyCache is an append-only pubkey list but is not attached to states. Fix: rebase cold-loaded states on a shared base (e.g. finalized or the historic cache entry) or split pubkeys into a shared Arc list.

**Impact.** Lower memory and load time for historical states (API, reconstruction, historic_state_cache); hot path mostly covered by rebase_on_finalized.

**Best measured result.** saves memory loading historical states (commit:grandine@70e0aad900ad)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/validator/validator.rs:22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/validator/validator.rs#L22) Validator keeps pubkey: PublicKeyBytes inline in each milhouse leaf
- [`consensus/types/src/state/beacon_state.rs:3416`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3416) rebase_on shares tree nodes (incl. validators) with a base state
- [`beacon_node/store/src/state_cache.rs:197`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L197) rebase_on_finalized used for hot loads
- [`beacon_node/store/src/hot_cold_store.rs:1988`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1988) hot load rebases on finalized state
- [`beacon_node/store/src/hot_cold_store.rs:2340`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2340) cold load: buffer.as_state with no rebase
- [`beacon_node/store/src/hdiff.rs:226`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L226) as_state rebuilds validators via set_validators_from_iter(cloned)
- [`consensus/types/src/state/beacon_state.rs:2198`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2198) set_validators_from_iter builds a fresh List::try_from_iter
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:24`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L24) chain-wide append-only pubkey list exists but is not structurally shared into states

**Second check.** Checked load_cold_state_by_slot and the historic state cache path for any rebase (none in store crate besides hot loads), set_validators_from_iter, and the beacon_chain ValidatorPubkeyCache as a possible equivalent shared pubkey list; it is not shared into state structure.

**Sources.** [grandine#763](https://github.com/grandinetech/grandine/pull/763), [grandine@70e0aad90](https://github.com/grandinetech/grandine/commit/70e0aad900ad)

</details>


<a id="state_cache-235"></a>
<details>
<summary><b>state_cache-235</b> Copy head state outside lock, swap pointer — <i>implemented · low · S · latency</i></summary>

**Idea.** When publishing a new head state, copy it outside the reader lock and take the lock only to swap pointers, so duty readers are not blocked for the copy.

**Impact.** Duty readers are never blocked for a state copy; already no cost to recover.

**Best measured result.** sync-committee efficiency dropped to 94.60% (199/3686 missed) due to blocking (pr:caplin#24165)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:284`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L284) snapshot is Arc&lt;BeaconSnapshot&gt;
- canonical_head.rs:1150-1171 new snapshot (state, caches) fully built before cached_head_write_lock, lock only swaps the CachedHead
- canonical_head.rs:748-751 readers take Arc clone, clone state outside lock

**Sources.** [caplin#24165](https://github.com/erigontech/erigon/pull/24165)

</details>


<a id="state_cache-238"></a>
<details>
<summary><b>state_cache-238</b> Fill only proposer indices on proposer cache miss — <i>implemented · low · S · cpu</i></summary>

**Idea.** On a proposer-indices cache miss compute only the proposer indices for that seed instead of rebuilding the full committee cache entry.

**Impact.** Proposer cache miss computes only proposer indices (with state advance if needed); the committee cache is not built for it.

**Best measured result.** flame graph, no numbers (pr:prysm#4548)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:175-227`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L175-L227) with_proposer_cache fills EpochBlockProposers via state.get_beacon_proposer_indices only
- beacon_proposer_cache.rs:197 OnceCell dedups concurrent fills

**Sources.** [prysm#4548](https://github.com/OffchainLabs/prysm/pull/4548)

</details>


<a id="state_cache-239"></a>
<details>
<summary><b>state_cache-239</b> Tiered retention for persisted checkpoint states — <i>implemented · medium · disk</i></summary>

**Idea.** Prune persisted checkpoint states with tiered retention (every epoch recently, then exponentially sparser) so disk stays bounded while keeping sparse history.

**Impact.** Disk is bounded and history exponentially sparser via the hdiff hierarchy (every 32 slots recent, up to 2^21); Lighthouse does not persist separate checkpoint states.

**Best measured result.** 64 epochs retained even over ~1 year (pr:lodestar#9898)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hdiff.rs:622`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L622) exponential hierarchy of stored states
- [`beacon_node/store/src/hot_cold_store.rs:3471`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3471) prune_historic_states
- [`beacon_node/store/src/state_cache.rs:127`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L127) update_finalized_state keeps only grid-aligned pre-finalized buffers

**Sources.** [lodestar#9898](https://github.com/ChainSafe/lodestar/pull/9898)

</details>


