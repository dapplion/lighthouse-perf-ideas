# state_cache (part 2 of 2)

249 ideas: 20 not, 29 partial, 119 implemented, 81 n/a; 19 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

Pages: [part 1](state_cache.md) · [part 2](state_cache-2.md)

<a id="state_cache-235"></a>
<details>
<summary><b>state_cache-235</b> Copy head state outside lock, swap pointer — <i>implemented · low · S · latency</i></summary>

**Idea.** When publishing a new head state, copy it outside the reader lock and take the lock only to swap pointers, so duty readers are not blocked for the copy.

**Impact.** Duty readers are never blocked for a state copy.

**Best measured result.** sync-committee efficiency dropped to 94.60% (199/3686 missed) due to blocking (pr:caplin#24165)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:1150`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1150) build_all_caches on new snapshot before taking the write lock
- [`beacon_node/beacon_chain/src/canonical_head.rs:1163-1171`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1163-L1171) cached_head_write_lock only swaps CachedHead (Arc snapshot)
- [`beacon_node/beacon_chain/src/canonical_head.rs:748-751`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L748-L751) head_beacon_state_cloned takes Arc clone, clones state outside the read lock

**Skeptic check.** Confirmed the new snapshot is fully built outside the lock and the write lock holds only a pointer swap; readers clone outside the lock. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#24165](https://github.com/erigontech/erigon/pull/24165)

</details>


<a id="state_cache-236"></a>
<details>
<summary><b>state_cache-236</b> Faster persistent collection library — <i>n/a · low · L · cpu, memory</i></summary>

**Idea.** Replace the persistent collection implementation behind structurally shared states with a faster one to cut clone and sharing overhead.

**Impact.** Lighthouse already uses milhouse; swapping libraries is speculative with no identified faster alternative.

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.lock:6570 milhouse 0.9.0 is already a custom persistent tree

**Sources.** [grandine#1019](https://github.com/grandinetech/grandine/pull/1019)

</details>


<a id="state_cache-237"></a>
<details>
<summary><b>state_cache-237</b> Synchronous in-memory state cache access — <i>n/a · low · S · latency, cpu</i></summary>

**Idea.** Make state cache lookups synchronous instead of async so hot paths avoid promise and scheduling overhead.

**Impact.** Rust cache lookups are already synchronous; no promise overhead exists.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:81`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L81) - StateCache is a plain sync LruCache

**Sources.** [lodestar@f5c09f31f](https://github.com/ChainSafe/lodestar/commit/f5c09f31f61f), [lodestar#2030](https://github.com/ChainSafe/lodestar/pull/2030)

</details>


<a id="state_cache-238"></a>
<details>
<summary><b>state_cache-238</b> Fill only proposer indices on proposer cache miss — <i>implemented · low · S · cpu</i></summary>

**Idea.** On a proposer-indices cache miss compute only the proposer indices for that seed instead of rebuilding the full committee cache entry.

**Impact.** Proposer cache miss computes only proposer indices; post-Fulu it reads proposer_lookahead directly.

**Best measured result.** flame graph, no numbers (pr:prysm#4548)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:175-227`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L175-L227) with_proposer_cache fills EpochBlockProposers from state.get_beacon_proposer_indices
- [`consensus/types/src/state/beacon_state.rs:1674-1710`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1674-L1710) get_beacon_proposer_indices uses proposer_lookahead or get_active_validator_indices + compute_proposer_indices, no committee cache
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:197`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L197) OnceCell dedups concurrent fills

**Skeptic check.** Verified get_beacon_proposer_indices scans active validators and computes proposers without building a CommitteeCache. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#4548](https://github.com/OffchainLabs/prysm/pull/4548)

</details>


<a id="state_cache-239"></a>
<details>
<summary><b>state_cache-239</b> Tiered retention for persisted checkpoint states — <i>partial · low · M · disk</i></summary>

**Idea.** Prune persisted checkpoint states with tiered retention (every epoch recently, then exponentially sparser) so disk stays bounded while keeping sparse history.

**Gap in Lighthouse.** No tiered retention of unfinalized hot states: during long non-finality the hot DB keeps every epoch's diff and summary until finalization (prune_hot_db in migrate.rs), so disk grows linearly with non-finality length rather than staying bounded. The hdiff hierarchy makes each kept state cheap but does not drop old unfinalized ones.

**Impact.** Mostly mitigated by hdiffs (per-epoch cost is a diff, not a full state as in Lodestar); only matters for months-long non-finality devnets.

**Best measured result.** 64 epochs retained even over ~1 year (pr:lodestar#9898)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:407`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L407) hot_storage_strategy: every unfinalized epoch state stored as hdiff/snapshot per hierarchy
- [`beacon_node/beacon_chain/src/migrate.rs:509`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L509) prune_hot_db runs only on finalization
- [`beacon_node/store/src/state_cache.rs:127`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L127) update_finalized_state retains in-memory layer points only (memory cache, not disk)
- [`beacon_node/store/src/hot_cold_store.rs:3471`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3471) prune_historic_states deletes all cold history, not tiered

**Skeptic check.** The hdiff hierarchy is a storage layout that keeps every state reconstructable, not a retention policy that prunes; Lodestar's PR bounds disk by dropping old persisted checkpoint states. Earlier verdict conflated the two.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lodestar#9898](https://github.com/ChainSafe/lodestar/pull/9898)

</details>


<a id="state_cache-240"></a>
<details>
<summary><b>state_cache-240</b> One-entry state cache during range sync — <i>not · low · S · memory, sync</i></summary>

**Idea.** Shrink the hot state cache to one entry during initial range sync, since states are not reused out of order, and restore it afterwards.

**Gap in Lighthouse.** Add a resize on StateCache and shrink it while range sync is active, restoring on sync completion; callers are StateCache::new and the sync state machine in network/src/sync.

**Impact.** Saves some memory during initial sync only; Lighthouse sync rarely reuses states, so gain is modest and rare.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/config.rs:39`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L39) - fixed state_cache_size
- [`beacon_node/store/src/state_cache.rs:81`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L81) - capacity set at construction, no runtime resize (grep for resize in beacon_chain/network found none)

**Sources.** [lodestar@5d023e0a2](https://github.com/ChainSafe/lodestar/commit/5d023e0a2f65), [lodestar#2130](https://github.com/ChainSafe/lodestar/pull/2130)

</details>


<a id="state_cache-241"></a>
<details>
<summary><b>state_cache-241</b> Justified balances from epoch-boundary cache — <i>implemented · low · S · cpu</i></summary>

**Idea.** When fork choice needs justified checkpoint balances, take them from the epoch-boundary state cache instead of regenerating the state.

**Impact.** Justification updates take balances from BalancesCache; miss falls back to get_hot_state, which hits the in-memory state cache before disk.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_fork_choice_store.rs:96-102`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_fork_choice_store.rs#L96-L102)
- [`beacon_node/beacon_chain/src/beacon_fork_choice_store.rs:341-368`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_fork_choice_store.rs#L341-L368)
- [`beacon_node/store/src/hot_cold_store.rs:1812-1819`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1812-L1819)

**Skeptic check.** set_justified_checkpoint checks balances_cache (block_root, epoch) then the state cache; no regeneration in the normal case. Earlier evidence right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#12083](https://github.com/OffchainLabs/prysm/pull/12083)

</details>


<a id="state_cache-242"></a>
<details>
<summary><b>state_cache-242</b> Proposer caches from stored proposer lookahead — <i>implemented · low · S · cpu, startup</i></summary>

**Idea.** After loading a state, fill current and next epoch proposer caches from the state's proposer_lookahead field instead of recomputing from the shuffling.

**Impact.** Post-Fulu, current and next epoch proposers are copied from proposer_lookahead for the proposer cache, API duties and block processing.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:1641-1667`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1641-L1667)
- [`consensus/types/src/state/beacon_state.rs:1673-1695`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1673-L1695)
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:227`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L227)
- [`beacon_node/http_api/src/proposer_duties.rs:285`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/proposer_duties.rs#L285)

**Skeptic check.** Both get_beacon_proposer_index and get_beacon_proposer_indices read proposer_lookahead for current/next epoch; Lighthouse fills its proposer cache lazily rather than at state load, but never recomputes from shuffling, so the effect matches.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#9730](https://github.com/ChainSafe/lodestar/pull/9730)

</details>


<a id="state_cache-243"></a>
<details>
<summary><b>state_cache-243</b> Vec-indexed committee cache without clones — <i>implemented · medium · S · cpu, memory</i></summary>

**Idea.** Build the per-epoch committee cache with Vec lookups indexed by validator index instead of HashMaps, take committees from the shuffling without cloning, and preallocate the active-index vector.

**Impact.** Already in place: shuffling_positions is a Vec indexed by validator index, committees are slices of the shuffling Vec, and get_active_validator_indices preallocates with_capacity.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/committee_cache.rs:29`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L29)
- [`consensus/types/src/state/committee_cache.rs:147-160`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L147-L160)
- [`consensus/types/src/state/committee_cache.rs:440-447`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L440-L447)

**Skeptic check.** Verified initialized_unchecked moves the active-index Vec into shuffle_list (no clone), builds Vec&lt;NonZeroUsizeOption&gt; positions, and committees are borrowed slices. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@902b80a57](https://github.com/sigp/lighthouse/commit/902b80a57931)

</details>


<a id="state_cache-244"></a>
<details>
<summary><b>state_cache-244</b> Whole-list swap-or-not shuffle — <i>implemented · high · S · cpu</i></summary>

**Idea.** Shuffle the whole validator list in one swap-or-not pass (one hash per 256 positions per round) instead of computing each permuted index separately.

**Impact.** Committee shuffling uses the whole-list pass with one hash per 256 positions per round.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/swap_or_not_shuffle/src/shuffle_list.rs:92-140`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/swap_or_not_shuffle/src/shuffle_list.rs#L92-L140)
- [`consensus/types/src/state/committee_cache.rs:147`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L147)

**Skeptic check.** Verified shuffle_list is used by CommitteeCache::initialized_unchecked. compute_shuffled_index remains only for proposer, sync committee and balance-weighted selection (beacon_state.rs:1372,1800,3725), where few candidates are sampled with distinct seeds, so per-index is the right choice there.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@8aa7f25bb](https://github.com/sigp/lighthouse/commit/8aa7f25bbcb3), [lighthouse@c3b2f802a](https://github.com/sigp/lighthouse/commit/c3b2f802a782)

</details>


<a id="state_cache-245"></a>
<details>
<summary><b>state_cache-245</b> Persist block-and-slot to state-root index for rewinds — <i>partial · low · M · cpu, disk</i></summary>

**Idea.** Persist a (block root, slot) -&gt; state root index alongside saved states, so rewinding to an ancestor state, including at empty slots, is a direct lookup. Replay then starts from the nearest stored state instead of walking parent blocks.

**Gap in Lighthouse.** The block+slot-&gt;state_root index exists only in the in-memory cache; on disk lookups go through HotStateSummary by state_root and the hdiff grid. Persisting it would only help rewinds to empty slots without a known state root.

**Impact.** Marginal: rewinds already start from nearest hdiff/snapshot base, not by walking parents.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:26`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L26) BlockMap block_root-&gt;slot-&gt;state_root (in memory only)
- [`beacon_node/store/src/hot_cold_store.rs:3743`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3743) get_ancestor_state_root via state_roots/summaries/cold roots
- [`beacon_node/store/src/hot_cold_store.rs:1949`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1949) load_hot_state uses hdiff grid base, not parent walk

**Sources.** [nimbus@3ad605329](https://github.com/status-im/nimbus-eth2/commit/3ad60532981e)

</details>


<a id="state_cache-246"></a>
<details>
<summary><b>state_cache-246</b> Bound state replay horizon for non-finalized-only queries — <i>implemented · low · S · cpu, latency, disk</i></summary>

**Idea.** For operations needing only non-finalized data (gossip validation, duties), limit the state lookup horizon to post-finalized data and fail gracefully. This avoids loading and replaying old states from disk.

**Impact.** Hot-state lookups used by gossip and duties are bounded by the split and fail gracefully instead of replaying finalized history.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1124-1150`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1124-L1150) get_advanced_hot_state: cache first, then rejects max_slot &lt; split.slot with FinalizedStateNotInHotDatabase
- [`beacon_node/store/src/hot_cold_store.rs:1157`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1157) load_hot_state only from the hot DB (bounded by split)
- [`beacon_node/store/src/state_cache.rs:316`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L316) get_by_block_root cache-first lookup

**Skeptic check.** Verified the split bound and graceful error in get_advanced_hot_state, the entry point for gossip/shuffling state loads. Nimbus #3217 bounded replay horizon to post-finalized data; Lighthouse's hot/cold split gives the same effect.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#3217](https://github.com/status-im/nimbus-eth2/pull/3217)

</details>


<a id="state_cache-247"></a>
<details>
<summary><b>state_cache-247</b> Cache native state field reads in a wrapper — <i>n/a · low · cpu</i></summary>

**Idea.** Wrap the native-backed state view with a cache layer so repeated reads of the same field cross the native binding only once.

**Impact.** No native-binding crossing to amortise.

**Evidence (Lighthouse @ 928b61e719).**

- BeaconState is native Rust (milhouse); no FFI binding boundary

**Sources.** [lodestar#9412](https://github.com/ChainSafe/lodestar/pull/9412)

</details>


<a id="state_cache-248"></a>
<details>
<summary><b>state_cache-248</b> Reuse cached weak-subjectivity state in light client proofs — <i>n/a · low · cpu</i></summary>

**Idea.** On finalization, reuse the already computed weak-subjectivity-period state in the light client init proof builder instead of recomputing the state.

**Impact.** Lighthouse has no weak-subjectivity-state-based proof builder; it precomputes and persists the sync committee branch, so serving bootstrap needs no state recompute.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/light_client_server_cache.rs:389`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_server_cache.rs#L389) bootstrap branch persisted eagerly at finalization
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:978`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L978) handler just reads stored bootstrap

**Sources.** [lodestar#3174](https://github.com/ChainSafe/lodestar/pull/3174)

</details>


<a id="state_cache-249"></a>
<details>
<summary><b>state_cache-249</b> Ring buffer of in-place state deltas for unfinalized forks — <i>n/a · low · latency, cpu, memory</i></summary>

**Idea.** Keep unfinalized state forks as a fixed power-of-two ring buffer of delta structs reset or copied forward in place, with a lock-free read view. Readers get state without a full state clone per block.

**Impact.** Lighthouse state clone is O(1) structural sharing via milhouse, so a delta ring buffer with lock-free view has little to save and would be a redesign.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:39`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L39) StateCache (LRU of states)
- [`consensus/types/src/state/beacon_state.rs:825`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L825) Arc-shared committee caches, milhouse persistent trees

**Sources.** [silver#43](https://github.com/gattaca-com/silver/pull/43)

</details>


