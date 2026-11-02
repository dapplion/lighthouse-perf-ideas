# state_cache (part 2 of 2)

249 ideas: 20 not, 29 partial, 119 implemented, 81 n/a; 19 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

Pages: [part 1](state_cache.md) · [part 2](state_cache-2.md)

<a id="state_cache-177"></a>
<details>
<summary><b>state_cache-177</b> Resolve block roots from state block_roots — <i>implemented · low · S · sync, startup</i></summary>

**Idea.** After checkpoint sync, answer block-at-slot queries from block_roots of in-memory states (up to SLOTS_PER_HISTORICAL_ROOT back) so dependent roots resolve before backfill.

**Impact.** Block-at-slot queries within SLOTS_PER_HISTORICAL_ROOT of head resolve from the in-memory head state, so they work right after checkpoint sync, before backfill.

**Best measured result.** accelerates the first couple minutes of checkpoint sync on mainnet (pr:nimbus#5869)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:1050-1082`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1050-L1082) block_root_at_slot_skips_none reads request and prev roots from head_state.block_roots before any DB/oldest_block_slot check
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1124-1142`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1124-L1142) block_root_at_slot_skips_prev fast path from head state
- [`beacon_node/beacon_chain/src/beacon_chain.rs:832-838`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L832-L838) forwards iterator falls back to head state

**Skeptic check.** Verified that both block_root_at_slot variants try head.beacon_state.get_block_root first, ahead of the oldest_block_slot range check. Earlier evidence was right; the more direct proof is the fast path at 1060-1082, not only the forwards iterator.

**Verdict history.** implemented (checked) → implemented (skeptic)

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

**Impact.** State cache pruning at finalization runs on the BackgroundMigrator thread, not under the fork-choice lock.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:1725`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1725) after_finalization hands pruning to store_migrator.process_finalization
- [`beacon_node/store/src/hot_cold_store.rs:3665`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3665) migrate_database -&gt; update_finalized_state on migrator thread
- [`beacon_node/store/src/hot_cold_store.rs:424-439`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L424-L439) only the state_cache mutex is held
- [`beacon_node/beacon_chain/src/canonical_head.rs:1738`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1738) the only work under fork_choice_write_lock is proto-array prune

**Skeptic check.** Verified that after_finalization only enqueues the migration, and that state-cache pruning happens in migrate_database. The fork-choice write lock covers only ForkChoice::prune. Earlier evidence was correct.

**Verdict history.** partial (checked) → implemented (refuted) → implemented (skeptic)

**Sources.** [grandine#522](https://github.com/grandinetech/grandine/pull/522), [grandine@c726d6341](https://github.com/grandinetech/grandine/commit/c726d6341b3c)

</details>


<a id="state_cache-180"></a>
<details>
<summary><b>state_cache-180</b> Pass state cache through rewind steps — <i>implemented · low · S · cpu</i></summary>

**Idea.** Build the per-state cache once and pass it through slot advance and block application during a rewind, rather than rebuilding it per step.

**Impact.** Committee, tree-hash and pubkey caches live in the state and carry through every replay step.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/block_replayer.rs:215`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/block_replayer.rs#L215) apply_blocks mutates one state via per_slot_processing/per_block_processing
- [`beacon_node/store/src/hot_cold_store.rs:2031`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2031) load_hot_state_using_replay

**Skeptic check.** Lighthouse caches are fields of BeaconState, so rewinds never rebuild them per step; this is the Nimbus fix's effect by design.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#1612](https://github.com/status-im/nimbus-eth2/pull/1612)

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


<a id="state_cache-182"></a>
<details>
<summary><b>state_cache-182</b> Prune grandparent snapshot after insert — <i>partial · low · S · memory</i></summary>

**Idea.** After inserting a block into the snapshot cache, prune the grandparent snapshot, which is safe from one-block reorgs, so skipped slots do not leave extra states cached.

**Gap in Lighthouse.** Snapshot cache is gone; StateCache::put_state does not drop the grandparent state after insert. Eviction only happens at capacity via cull(), which prefers advanced states.

**Impact.** Saves a few cached states' memory (milhouse shares most nodes) on skipped-slot runs; marginal.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:357`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L357) cull() evicts advanced states first, protects head, keeps cull_exempt most recent
- beacon_chain/src: snapshot_cache.rs no longer exists (only metric name in metrics.rs:102)
- [`beacon_node/store/src/state_cache.rs:215`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L215) put_state has no grandparent prune

**Sources.** [lighthouse#2917](https://github.com/sigp/lighthouse/pull/2917)

</details>


<a id="state_cache-183"></a>
<details>
<summary><b>state_cache-183</b> Epoch-matching state cache for attestations — <i>implemented · medium · S · sync, cpu</i></summary>

**Idea.** In attestation handling check the target epoch before rewinding, let the state cache match by epoch rather than exact slot, and store the updated state so repeated lookups hit.

**Impact.** Attestation committee lookups match by epoch/decision root and the result is cached, so repeated lookups do not rewind or replay states.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:330-353`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L330-L353) keyed by AttestationShufflingId (epoch + decision root), read-lock hit
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:398-447`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L398-L447) miss uses the head state when possible, else get_advanced_hot_state, and only partial-advances when the epoch requires it
- [`beacon_node/store/src/state_cache.rs:316`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L316) get_by_block_root returns highest slot &lt;= max_slot

**Skeptic check.** with_cached_shuffling checks the epoch need before advancing and caches the committee rather than the advanced state, which gives the same effect for attestations. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#1348](https://github.com/status-im/nimbus-eth2/pull/1348)

</details>


<a id="state_cache-184"></a>
<details>
<summary><b>state_cache-184</b> Rebase clearance state on head during chain stall — <i>implemented · low · S · latency</i></summary>

**Idea.** When the chain stalls, rebase the block clearance/advance state on the fork-choice head so a proposer does not have to catch up a long run of empty slots before it can propose.

**Impact.** Lighthouse has no separate clearance state that can drift from the head. The advance timer and block production both build on the fork-choice head.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:277-284`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L277-L284) advance_head always starts from the fork-choice head_snapshot block root
- [`beacon_node/beacon_chain/src/block_production/mod.rs:84-96`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L84-L96) proposer uses get_advanced_hot_state on the head block root
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:38`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L38),269 MAX_ADVANCE_DISTANCE=256 stops advancing during very long stalls

**Skeptic check.** Nimbus #6108 fixed a clearanceState that tracked the latest resolved block instead of the canonical head. Lighthouse always advances and proposes from head_snapshot. One small caveat: after a stall of more than 256 slots, the timer stops and the proposer replays the empty slots itself.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#6108](https://github.com/status-im/nimbus-eth2/pull/6108)

</details>


<a id="state_cache-185"></a>
<details>
<summary><b>state_cache-185</b> Refresh next-slot cache when execution payload arrives late — <i>implemented · low · S · latency</i></summary>

**Idea.** When a late execution payload changes the post-state, recompute the next-slot cache and boundary caches from it (and send forkchoice update if proposing next slot) so the next proposer has a warm pre-state.

**Impact.** Nothing left to gain. Lighthouse follows the deferred-payload Gloas spec: verify_execution_payload_envelope does not change the state, and process_parent_execution_payload applies the parent payload's effects inside the next block's processing. So the state the advance timer pre-advanced (keyed on the block state root) is already the right pre-state for the next proposer, Full or Empty. A late envelope runs recompute_head_at_current_slot. The head changes on a payload-status change alone, and that sends forkchoiceUpdated.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/envelope_processing.rs:97-107`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/envelope_processing.rs#L97-L107)
- [`consensus/state_processing/src/per_block_processing.rs:135-138`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing.rs#L135-L138)
- [`consensus/state_processing/src/per_block_processing.rs:562-595`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing.rs#L562-L595)
- [`beacon_node/beacon_chain/src/payload_envelope_verification/mod.rs:374-393`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/mod.rs#L374-L393)
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:4083-4085`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L4083-L4085)
- [`beacon_node/beacon_chain/src/canonical_head.rs:1106-1137`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1106-L1137)
- [`beacon_node/beacon_chain/src/canonical_head.rs:1884-1913`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1884-L1913)
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:276-296`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L276-L296)

**Second check.** The earlier screen said no_feature (Gloas-specific). I checked the Lighthouse Gloas code: envelope verification does not mutate state (execution requests are applied via process_parent_execution_payload in the next block). Gossip envelope import calls recompute_head_at_current_slot, which rebuilds the head snapshot on a payload-status change from get_advanced_hot_state and runs the FCU. The idea is therefore covered by an equivalent mechanism, and the Prysm next-slot-cache refresh has no counterpart to do.

**Skeptic check.** Checked that envelope verification is pure (it uses a cloned header and never writes the state) and that the deferred requests are applied in per_block_processing. So Prysm's next-slot cache refresh has nothing to fix in Lighthouse. Checked that canonical_head rebuilds the cached head when new_payload_status differs and spawns the EL forkchoice update. The earlier evidence was right.

**Verdict history.** not (checked) → implemented (refuted) → implemented (skeptic)

**Sources.** [prysm#16460](https://github.com/OffchainLabs/prysm/pull/16460)

</details>


<a id="state_cache-186"></a>
<details>
<summary><b>state_cache-186</b> Bound the number of full states held in memory — <i>implemented · high · S · memory</i></summary>

**Idea.** Cap the hot state/checkpoint cache to a small number of full states (fewer entries, every other slot, a bounded number of epochs) and regenerate the rest on demand, because each epoch-boundary state can cost hundreds of MB and unbounded caches OOM during non-finality.

**Impact.** The hot state cache is bounded by count and culls the least useful states, and evicted states are regenerated from disk. Disk-loaded states are rebased on the finalized state to share memory.

**Best measured result.** 128 entries ~20GB; 32 x 180MB ~ 6GB (pr:lighthouse#7055)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/config.rs:23`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L23) DEFAULT_STATE_CACHE_SIZE=128 bounded LRU (--state-cache-size, cli.rs:833)
- [`beacon_node/store/src/state_cache.rs:252-259`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L252-L259) cull on overflow
- [`beacon_node/store/src/state_cache.rs:357-412`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L357-L412) cull order: advanced, old boundary, mid-epoch, then good boundary states
- [`beacon_node/store/src/state_cache.rs:197-210`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L197-L210) rebase_on_finalized for states loaded from disk

**Skeptic check.** The cap is real. The default of 32 from lighthouse#7055/#7101 was reverted to 128 by #7364 (commit 6c8770e80d), which relies on structural sharing and rebase_on_finalized. The bound is a state count, not bytes.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#2294](https://github.com/Consensys-Incorporated/teku/pull/2294), [lighthouse#7055](https://github.com/sigp/lighthouse/pull/7055), [lighthouse#7101](https://github.com/sigp/lighthouse/pull/7101), [nimbus#1290](https://github.com/status-im/nimbus-eth2/pull/1290), [nimbus@fc8502c54](https://github.com/status-im/nimbus-eth2/commit/fc8502c54e35), [grandine#87](https://github.com/grandinetech/grandine/pull/87), [lodestar#452](https://github.com/ChainSafe/lodestar/pull/452)

</details>


<a id="state_cache-187"></a>
<details>
<summary><b>state_cache-187</b> Do expensive state work outside the cache lock — <i>partial · medium · M · latency, cpu</i></summary>

**Idea.** Do not hold the state or shuffling cache lock while computing or waiting for a state, shuffling or diff buffer; release the lock first and share the result through a promise or once-cell, so other threads are not blocked.

**Gap in Lighthouse.** lighthouse#8176 (OnceCell/Arc in HotHDiffBufferCache) was CLOSED, not merged. StateCache::get_hdiff_buffer_by_state_root, StateCache::put_state (pre-finalized branch) and StateCache::update_finalized_state still run HDiffBuffer::from_state (up to about 1s) while holding the state_cache mutex. HistoricStateCache::get_hdiff_buffer and get_state also run from_state/as_state under the historic cache lock. get_hot_state and get_advanced_hot_state have no in-flight promise, so concurrent misses on the same root each replay from disk.

**Impact.** Every state-cache lookup (block import, attestation miss path, API) can stall behind an HDiffBuffer conversion during hdiff loads and finalization.

**Best measured result.** HDiffBuffer::from_state can take up to 1s under lock (pr:lighthouse#8176)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1817-1858`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1817-L1858) get_hot_state locks only for lookup/put (correct)
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:370-377`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L370-L377) promise then drop lock (correct)
- [`beacon_node/store/src/hot_cold_store.rs:1919-1925`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1919-L1925) load_hot_hdiff_buffer calls get_hdiff_buffer_by_state_root under state_cache.lock()
- [`beacon_node/store/src/state_cache.rs:304-306`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L304-L306) HDiffBuffer::from_state of a cached state while the mutex is held
- [`beacon_node/store/src/state_cache.rs:229`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L229) put_state pre-finalized branch runs HDiffBuffer::from_state under the lock
- [`beacon_node/store/src/state_cache.rs:173`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L173) update_finalized_state converts pruned states to HDiffBuffers under the lock
- [`beacon_node/store/src/historic_state_cache.rs:42`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/historic_state_cache.rs#L42),64 get_hdiff_buffer/get_state run from_state/as_state under historic_state_cache lock (hot_cold_store.rs:2310,2424)

**Skeptic check.** The earlier verdict assumed #8176 was merged. show.py shows it was closed unmerged, and the from_state calls under the mutex are still in the code. The #3589 shuffling-promise part and the disk load outside the lock in get_hot_state are real.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lighthouse#3589](https://github.com/sigp/lighthouse/pull/3589), [lighthouse#8176](https://github.com/sigp/lighthouse/pull/8176), [teku#2664](https://github.com/Consensys-Incorporated/teku/pull/2664)

</details>


<a id="state_cache-188"></a>
<details>
<summary><b>state_cache-188</b> Check in-memory caches before DB state loads — <i>implemented · medium · S · latency, disk, cpu</i></summary>

**Idea.** On hot state-by-root and block-and-state lookups, check the in-memory state caches (hot cache, finalized state) first and fall back to a database load and replay only on a miss.

**Impact.** In-memory caches (hot cache and finalized state) are checked first. The node loads from the DB and replays blocks only on a miss.

**Best measured result.** avoids a lot of regenerated states (pr:teku#2610)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1124-1132`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1124-L1132) get_advanced_hot_state checks the cache first
- [`beacon_node/store/src/hot_cold_store.rs:1817`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1817) get_hot_state checks the cache first
- [`beacon_node/store/src/state_cache.rs:275-282`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L275-L282) get_by_state_root serves finalized_state
- [`beacon_node/store/src/hot_cold_store.rs:1087-1110`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1087-L1110) get_state routes through get_hot_state

**Skeptic check.** Verified the cache-first order on both hot lookup entry points and the finalized-state shortcut. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#7674](https://github.com/OffchainLabs/prysm/pull/7674), [teku#2610](https://github.com/Consensys-Incorporated/teku/pull/2610)

</details>


<a id="state_cache-189"></a>
<details>
<summary><b>state_cache-189</b> Advance epoch caches once per epoch transition — <i>implemented · low · S · cpu</i></summary>

**Idea.** Build or advance the per-epoch caches (committee, proposer, etc.) exactly once in the slot/epoch processing path rather than twice per epoch transition.

**Impact.** Caches rotate once per epoch transition.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/altair.rs:81`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/altair.rs#L81) single advance_caches
- [`consensus/state_processing/src/per_epoch_processing/base.rs:73`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/base.rs#L73) single advance_caches
- [`consensus/state_processing/src/per_slot_processing.rs:38-75`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_slot_processing.rs#L38-L75) no second advance after per_epoch_processing

**Skeptic check.** Grep shows advance_caches is called only once per fork's epoch processing; per_slot_processing does not call it again. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@b88750960](https://github.com/sigp/lighthouse/commit/b88750960736)

</details>


<a id="state_cache-190"></a>
<details>
<summary><b>state_cache-190</b> Drop fork-aware finalized pubkey cache — <i>n/a · low · memory, cpu</i></summary>

**Idea.** Delete a separate finalized pubkey-to-index cache and its maintenance once deposits are guaranteed finalized before validator creation, since one shared map suffices.

**Impact.** Lighthouse has no separate fork-aware finalized pubkey cache; one persistent map per state.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/pubkey_cache.rs:6-12`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/pubkey_cache.rs#L6-L12) single pubkey-&gt;index map
- [`consensus/types/src/state/beacon_state.rs:2979`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2979) update_pubkey_cache

**Sources.** [prysm#14497](https://github.com/OffchainLabs/prysm/pull/14497)

</details>


<a id="state_cache-191"></a>
<details>
<summary><b>state_cache-191</b> Remove redundant lock around thread-safe cache — <i>n/a · low · latency, cpu</i></summary>

**Idea.** Do not wrap an already thread-safe LRU state cache in an extra mutex/RwLock; the outer lock only adds contention.

**Impact.** Go LRU double-locking; Lighthouse uses a single Mutex over its own StateCache.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1201-1203`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1201-L1203) state_cache is a plain Mutex around a Rust cache, no nested thread-safe LRU

**Sources.** [prysm#11846](https://github.com/OffchainLabs/prysm/pull/11846), [prysm#16469](https://github.com/OffchainLabs/prysm/pull/16469)

</details>


<a id="state_cache-192"></a>
<details>
<summary><b>state_cache-192</b> Remove per-state caches that pin old states — <i>n/a · low · memory</i></summary>

**Idea.** Remove per-state view caches that hold references to views of older state instances when views are already cached at the backing-tree level, so old hot states can be freed.

**Impact.** Teku/JVM view caches; milhouse caches live in the tree nodes, nothing pins old states separately.

**Best measured result.** chart in PR of significantly lower hot state memory; no numbers (pr:teku#2175)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/pubkey_cache.rs:2`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/pubkey_cache.rs#L2) rpds persistent map, no per-state view caches pinning older states
- [`beacon_node/store/src/hot_cold_store.rs:1172-1175`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1172-L1175) states held in one state_cache

**Sources.** [teku#2175](https://github.com/Consensys-Incorporated/teku/pull/2175), [teku#2188](https://github.com/Consensys-Incorporated/teku/pull/2188), [lighthouse@931da1354](https://github.com/sigp/lighthouse/commit/931da13545d7)

</details>


<a id="state_cache-193"></a>
<details>
<summary><b>state_cache-193</b> Consult checkpoint cache only for viable non-canonical targets — <i>n/a · low · cpu</i></summary>

**Idea.** On attestation target-state lookup, read the checkpoint state cache only when the checkpoint is viable and not on the canonical branch, skipping the lookup otherwise.

**Impact.** Lighthouse has no checkpoint state cache; attestation target lookups go through the shuffling cache, so there is no lookup to skip.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs): attestations use shuffling cache keyed by decision root
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1750-1760`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1750-L1760) proposer cache then get_advanced_hot_state

**Sources.** [prysm#12397](https://github.com/OffchainLabs/prysm/pull/12397)

</details>


<a id="state_cache-194"></a>
<details>
<summary><b>state_cache-194</b> Keep persisted-file key when re-adding reloaded states — <i>n/a · low · disk</i></summary>

**Idea.** When a checkpoint state reloaded from disk is re-added to the in-memory cache, keep its on-disk key so later pruning deletes the file instead of orphaning it.

**Impact.** No on-disk checkpoint state files with an in-memory cache keyed by file; nothing to orphan.

**Evidence (Lighthouse @ 928b61e719).**

- grep checkpoint_cache/CheckpointCache in beacon_node: no matches
- [`beacon_node/store/src/hot_cold_store.rs:1124`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1124) hot states are in DB, not checkpoint files

**Sources.** [lodestar#9557](https://github.com/ChainSafe/lodestar/pull/9557)

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
<summary><b>state_cache-196</b> Reuse the block post-state as new head state — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** After importing a block, take the new head state from the post-state already in hand (or the clearance state) rather than requesting or replaying it from the state generator, which can also evict the cached pre-state needed next.

**Impact.** The new head state is the cached post-state of the imported block. It is not regenerated, and the head state is never culled.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:4752`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4752) PutState of the post-state on import
- [`beacon_node/store/src/hot_cold_store.rs:1661-1670`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1661-L1670) store_hot_state inserts into state_cache
- [`beacon_node/beacon_chain/src/canonical_head.rs:1134-1137`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1134-L1137) new head state from get_advanced_hot_state (cache hit)
- [`beacon_node/store/src/state_cache.rs:386-388`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L386-L388) head state exempt from cull

**Skeptic check.** Verified the import -&gt; state_cache -&gt; recompute_head path. Separately, recompute_head reloads the full head block from the DB (get_full_block, block cache default 0), but that is outside this state idea.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#1388](https://github.com/status-im/nimbus-eth2/pull/1388), [prysm#6729](https://github.com/OffchainLabs/prysm/pull/6729)

</details>


<a id="state_cache-197"></a>
<details>
<summary><b>state_cache-197</b> Use head state for prior-epoch data column validation — <i>partial · low · S · cpu, latency</i></summary>

**Idea.** When validating a data column whose parent state is the head state from the previous epoch, use the head state directly; on a miss replay only to the target checkpoint state rather than the parent state.

**Gap in Lighthouse.** On a proposer-cache miss Lighthouse loads the parent's (possibly slot-advanced) state rather than the head state or target checkpoint state; no epoch transition replay is done, but a state load from DB can occur when the advanced state is not cached. Could shortcut to canonical head state when parent is head. Change the closure in verify_proposer_and_signature.

**Impact.** Rare cache miss path only; the proposer cache already avoids state access in the common case, so gain is small.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_column_verification.rs:1738-1762`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1738-L1762) proposer cache keyed by shuffling root, miss loads parent state via get_advanced_hot_state(parent_root, column_slot)
- [`beacon_node/store/src/hot_cold_store.rs:1124-1184`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1124-L1184) returns cached advanced state or loads parent state and caches it

**Sources.** [prysm#16250](https://github.com/OffchainLabs/prysm/pull/16250)

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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [lodestar#6504](https://github.com/ChainSafe/lodestar/pull/6504)

</details>


<a id="state_cache-199"></a>
<details>
<summary><b>state_cache-199</b> Cache block post-states for block production — <i>partial · low · M · cpu, latency</i></summary>

**Idea.** Cache post-states (and block rewards) from block processing in a fine-grained-locked cache so block production reuses them rather than re-running state transitions.

**Gap in Lighthouse.** The grandine block processor caches the post-state and block rewards keyed by block root when it processes the produced block, so the import of the node's own block (and a second production of the same block) reuses them. In Lighthouse, complete_partial_beacon_block computes the post-state and then drops it (produce_block.rs `_block_state`). The own block is then processed again from the parent state in the publish -&gt; process_block import path. Block rewards come from a separate compute_beacon_block_reward pass, not from the processing pass.

**Impact.** Saves one per_block_processing pass and one tree-hash pass on the import of each locally proposed block (tens of ms on the proposal critical path). Only proposing nodes gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_production/mod.rs:87-89`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L87-L89) parent post-state served from the state cache via get_advanced_hot_state
- [`beacon_node/beacon_chain/src/beacon_chain.rs:6537-6553`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6537-L6553) complete_partial_beacon_block runs compute_beacon_block_reward as a separate pass, then per_block_processing + update_tree_hash_cache on the produced block
- [`beacon_node/beacon_chain/src/beacon_chain.rs:6589-6595`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6589-L6595) post-state returned in BeaconBlockResponse
- [`beacon_node/http_api/src/produce_block.rs:101`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/produce_block.rs#L101) _block_state discarded by the HTTP API
- [`beacon_node/http_api/src/build_block_contents.rs:17`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/build_block_contents.rs#L17) BeaconBlockResponse state not kept

**Skeptic check.** Verified: the parent post-state is reused, as the earlier evidence said. But the main mechanism of the source commit, caching the post-state of the produced block for its import, is absent. The earlier check matched only the parent-state half of the idea.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [grandine@67b707828](https://github.com/grandinetech/grandine/commit/67b707828989)

</details>


<a id="state_cache-200"></a>
<details>
<summary><b>state_cache-200</b> Reuse prebuilt pubkey cache from anchor state — <i>implemented · low · S · startup, cpu</i></summary>

**Idea.** At startup, if the anchor state already carries a built pubkey cache, reuse it instead of rebuilding by deserializing all pubkeys.

**Impact.** Restart already skips pubkey decompression. load_from_store is sequential, so parallel loading could save a few seconds at most.

**Best measured result.** ~30 seconds for 350k keys (pr:lodestar#4319)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:53-78`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L53-L78) load_from_store reads persisted uncompressed keys
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:237-242`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L237-L242) as_pubkey uses deserialize_uncompressed
- [`beacon_node/beacon_chain/src/builder.rs:286`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L286) persisted cache loaded at restart
- [`beacon_node/beacon_chain/src/builder.rs:875`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L875) ValidatorPubkeyCache::new from state only when no cache is persisted

**Skeptic check.** Confirmed that the persisted pubkey cache is reused on restart. This has the same effect as the Lodestar change (no expensive rebuild of all pubkeys from the anchor state).

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#4319](https://github.com/ChainSafe/lodestar/pull/4319)

</details>


<a id="state_cache-201"></a>
<details>
<summary><b>state_cache-201</b> Reuse pubkey map allocation when reinitializing caches — <i>n/a · low · memory, cpu</i></summary>

**Idea.** When re-initializing state caches, clear and reuse the existing pubkey-to-index map allocation rather than allocating a new map.

**Impact.** Persistent trie map has no big allocation to reuse; reinit is rare (drop_all_caches only).

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/pubkey_cache.rs:2-12`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/pubkey_cache.rs#L2-L12) rpds HashTrieMap, cloned structurally
- [`consensus/types/src/state/beacon_state.rs:2996`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2996) drop_pubkey_cache just resets to default

**Sources.** [caplin#14461](https://github.com/erigontech/erigon/pull/14461)

</details>


<a id="state_cache-202"></a>
<details>
<summary><b>state_cache-202</b> Load startup state once and share across services — <i>implemented · low · S · startup, memory</i></summary>

**Idea.** Register the startup (genesis/finalized) state once and hand it to all services instead of each service reloading it from the database.

**Impact.** Startup state is loaded once by the builder and shared via the BeaconChain (canonical head / state cache).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/builder.rs:302-330`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L302-L330) set_genesis_state builds caches and stores the state once
- [`beacon_node/beacon_chain/src/builder.rs:406`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L406) weak_subjectivity_state
- [`beacon_node/beacon_chain/src/builder.rs:229`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L229) resume_from_db

**Skeptic check.** All services take the single BeaconChain object; no service reloads the startup state from the database. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#9900](https://github.com/OffchainLabs/prysm/pull/9900)

</details>


<a id="state_cache-203"></a>
<details>
<summary><b>state_cache-203</b> Keep future-epoch info and per-block state cache — <i>n/a · low · S · cpu</i></summary>

**Idea.** Do not discard cached epoch info for future epochs, and do not build a fresh state cache per block application.

**Impact.** Nimbus separate EpochRef/StateCache design does not exist; caches are part of BeaconState and Next-epoch caches are kept.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:825`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L825) committee_caches live on the state (prev/current/next) and are cloned with it
- [`beacon_node/beacon_chain/src/block_verification.rs:1684`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1684) build_all_committee_caches on the state, no per-block fresh cache object

**Sources.** [nimbus#1610](https://github.com/status-im/nimbus-eth2/pull/1610)

</details>


<a id="state_cache-204"></a>
<details>
<summary><b>state_cache-204</b> Persist skipped-slot states using state_roots — <i>implemented · low · S · cpu</i></summary>

**Idea.** When persisting intermediate skipped-slot states during block processing, derive their roots from the next state's state_roots field instead of tree hashing each one.

**Impact.** Each skipped-slot state is hashed once (needed anyway by slot processing) and reused for persistence; no extra hashing.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1609-1645`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1609-L1645) update_tree_hash_cache once per skipped-slot state, stored, then passed as Some(state_root) to per_slot_processing

**Skeptic check.** Verified the root is computed once and reused for both the store and per_slot_processing, and the parent's state root is taken from the block when unadvanced. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@467852465](https://github.com/sigp/lighthouse/commit/4678524659f4)

</details>


<a id="state_cache-205"></a>
<details>
<summary><b>state_cache-205</b> Store shuffling once, derive committees and duties — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** Store only the shuffling plus a reverse map (validator index to position) in the committee cache and derive committees and duties on demand, instead of several redundant maps keyed by validator or slot.

**Impact.** Already compact; committees and duties derived from shuffling + shuffling_positions.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/committee_cache.rs:26-34`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L26-L34)

**Skeptic check.** CommitteeCache struct holds only initialized_epoch, shuffling, shuffling_positions (reverse map), committees_per_slot, slots_per_epoch; earlier evidence correct (this is Lighthouse's own change).

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@21de9c1cb](https://github.com/sigp/lighthouse/commit/21de9c1cb887), [lighthouse@9eb8c7411](https://github.com/sigp/lighthouse/commit/9eb8c7411f80)

</details>


<a id="state_cache-206"></a>
<details>
<summary><b>state_cache-206</b> Do not preallocate state cache tables — <i>n/a · low · S · memory</i></summary>

**Idea.** Create state cache hash tables small so they do not preallocate many unused full BeaconState slots.

**Impact.** Nim hash table preallocation; Lighthouse uses an LRU sized by capacity that allocates on insert.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:89`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L89) LruCache::new(capacity) no preallocated state slots

**Sources.** [nimbus#1002](https://github.com/status-im/nimbus-eth2/pull/1002)

</details>


<a id="state_cache-207"></a>
<details>
<summary><b>state_cache-207</b> Store next-slot cache hit into checkpoint cache — <i>partial · low · S · cpu</i></summary>

**Idea.** When the next-slot cache answers an attestation target-state request, save that state into the checkpoint cache so later attestations for the same target hit directly.

**Gap in Lighthouse.** In the miss path of the attestation data production, after partial_state_advance, put the advanced state into store.state_cache so later requests for the same target hit. The state advance timer already fills the cache in the common case, so this only matters on timer misses.

**Impact.** Avoids repeating an epoch-boundary state advance (tens of ms) on rare cache misses at the first slot of an epoch; marginal.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2161`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2161) get_advanced_hot_state used for attestation data; if state.current_epoch() &lt; request_epoch it runs partial_state_advance (:2164) and drops the result
- [`beacon_node/store/src/hot_cold_store.rs:1172`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1172) get_advanced_hot_state caches only the loaded state, not the advanced one
- [`beacon_node/store/src/state_cache.rs:316`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L316) get_by_block_root returns the latest cached state &lt;= slot

**Sources.** [prysm#12398](https://github.com/OffchainLabs/prysm/pull/12398)

</details>


<a id="state_cache-208"></a>
<details>
<summary><b>state_cache-208</b> Drop pubkey map and scan the registry — <i>n/a · low · S · memory</i></summary>

**Idea.** Remove the per-state pubkey-to-index hash map and find validators by linear registry scan, trading slower deposit processing for no memory spikes.

**Impact.** Prysm per-state full map copies caused spikes; Lighthouse's persistent map shares structure, so there is no spike to remove and a scan would be slower.

**Best measured result.** "completely removes memory spikes" (no numbers) (pr:prysm#8854)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/pubkey_cache.rs:9`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/pubkey_cache.rs#L9) per-state PubkeyCache is a persistent rpds HashTrieMap shared structurally between states
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:76`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L76) update_pubkey_cache adds only new validators

**Sources.** [prysm#8854](https://github.com/OffchainLabs/prysm/pull/8854)

</details>


<a id="state_cache-209"></a>
<details>
<summary><b>state_cache-209</b> Segmented page pool for lock-free state readers — <i>n/a · low · S · memory, latency</i></summary>

**Idea.** Grow the state page pool in fixed pre-zeroed segments with a pre-reserved segment list so growth never moves existing pages and lock-free readers stay valid.

**Impact.** Silver-specific page pool for lock-free readers; Lighthouse state cache is a mutex-guarded LRU of persistent trees.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:89`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L89) states are milhouse tree values in an LRU, no page pool

**Sources.** [silver#396](https://github.com/gattaca-com/silver/pull/396)

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


<a id="state_cache-212"></a>
<details>
<summary><b>state_cache-212</b> Serve finalized-state lookups from the in-memory copy — <i>implemented · low · S · cpu, disk</i></summary>

**Idea.** Serve finalized-state requests (by root, or for deposit pruning) from the finalized checkpoint state already held in memory instead of loading, regenerating or copying it from the database.

**Impact.** API 'finalized' state resolves to slot &gt;= split slot, goes through get_hot_state which returns the held finalized_state clone (cheap milhouse clone); no deposit-pruning path exists.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:275-281`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L275-L281)
- [`beacon_node/store/src/hot_cold_store.rs:1812-1819`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1812-L1819)
- [`beacon_node/store/src/hot_cold_store.rs:1087-1110`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1087-L1110)
- [`beacon_node/http_api/src/state_id.rs:41-47`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L41-L47)

**Skeptic check.** Verified get_by_state_root checks finalized_state first and both get_state and get_hot_state route through it; earlier evidence right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#10273](https://github.com/ChainSafe/lodestar/pull/10273), [prysm#9985](https://github.com/OffchainLabs/prysm/pull/9985)

</details>


<a id="state_cache-213"></a>
<details>
<summary><b>state_cache-213</b> Cheap presence check on shuffling cache — <i>implemented · low · S · cpu</i></summary>

**Idea.** Give the shuffling cache a has/contains check so callers can test presence without computing or memoizing an expensive shuffling.

**Impact.** Block import skips building committee caches when the shuffling is already cached.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:209-211`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L209-L211)
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:196-207`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L196-L207)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5216-5222`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5216-L5222)

**Skeptic check.** ShufflingCache::contains is a plain contains_key under a read lock and is used on the import path before build_committee_cache; get_shuffling_if_cached also non-mutating. Earlier evidence right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#9579](https://github.com/ChainSafe/lodestar/pull/9579)

</details>


<a id="state_cache-214"></a>
<details>
<summary><b>state_cache-214</b> Predict next-epoch duties without state advance — <i>implemented · low · S · cpu</i></summary>

**Idea.** Compute next-epoch attester shuffling and first proposer from the head state before the epoch boundary, skipping the full state advance when no effective balance can change.

**Impact.** Post-Fulu, the proposer_lookahead gives next-epoch proposers without an epoch transition. The attester shuffling already uses the one-epoch lookahead. Before Fulu, a partial_state_advance was still needed for next-epoch proposers, but that path is historical on mainnet.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:410-423`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L410-L423) the next-epoch attester shuffling comes from a state advanced only to the start of the previous epoch
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:321-354`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L321-L354) ensure_state_can_determine_proposers_for_epoch advances only when the decision slot needs it (post-Fulu, the lookahead makes the advance unnecessary)
- [`beacon_node/http_api/src/proposer_duties.rs:91-109`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/proposer_duties.rs#L91-L109) next-epoch proposer duties are computed from the head
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:342-420`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L342-L420) the next-epoch caches are primed off the critical path

**Skeptic check.** Verified the attester and proposer paths. The Nimbus prediction trick (skip the advance when no effective balance can change) is only relevant before Fulu, and Fulu's lookahead removes the need for it.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#5414](https://github.com/status-im/nimbus-eth2/pull/5414)

</details>


<a id="state_cache-215"></a>
<details>
<summary><b>state_cache-215</b> Single shared head state buffer for services — <i>n/a · low · memory</i></summary>

**Idea.** Keep one head state shared with API/services under a read lock with release callback rather than keeping extra full copies for readers.

**Impact.** Rust BeaconState uses persistent tree structure sharing, so readers do not hold full copies.

**Best measured result.** "Reduces memory usage by 600MB too" (pr:caplin#12519)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:279`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L279) states are cloned with tree sharing (milhouse), no separate buffer per reader

**Sources.** [caplin#12519](https://github.com/erigontech/erigon/pull/12519)

</details>


<a id="state_cache-216"></a>
<details>
<summary><b>state_cache-216</b> Replay only blocks after base state on regen — <i>partial · low · S · disk, cpu</i></summary>

**Idea.** When regenerating from a stored base state, replay only blocks after it and do not require or fetch the base state's own block.

**Gap in Lighthouse.** load_blocks_to_replay fetches the base-state block (kept deliberately for its state root) and can load one extra older block before take_while stops. Could pass the base state's latest_block_root and stop at it.

**Impact.** Saves one block read per hot-state regen; negligible vs replay cost.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2514-2549`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2514-L2549) load_blocks_to_replay still loads block at start_slot (and may read one older block) for its state root
- [`beacon_node/store/src/hot_cold_store.rs:2031-2042`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2031-L2042) load_hot_state_using_replay

**Sources.** [teku#3249](https://github.com/Consensys-Incorporated/teku/pull/3249)

</details>


<a id="state_cache-217"></a>
<details>
<summary><b>state_cache-217</b> State cache eviction policy and insertion rules — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** Tune state cache insertion and eviction: true LRU order, never evict the head, evict old epoch-boundary states first, cache ancestors only on epoch boundaries, and do not insert states read by migration/pruning so they do not evict useful states.

**Impact.** The policy is the merged form of the Lighthouse PRs themselves. No more gain is expected.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:357-412`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L357-L412) cull is LRU with extra order: advanced, old boundary, mid-epoch, could-finalize boundary; the head is never culled; the most recent 10% are exempt
- [`beacon_node/store/src/state_cache.rs:275-282`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L275-L282) get_by_state_root uses LruCache::get (promotes)
- [`beacon_node/store/src/hot_cold_store.rs:2031-2060`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2031-L2060) ancestor states are cached only on epoch boundaries and only when update_cache is set

**Skeptic check.** The source PRs are Lighthouse's own. The cull and LRU promotion code matches them.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#7067](https://github.com/sigp/lighthouse/pull/7067), [lighthouse#7095](https://github.com/sigp/lighthouse/pull/7095), [lighthouse#7364](https://github.com/sigp/lighthouse/pull/7364)

</details>


<a id="state_cache-218"></a>
<details>
<summary><b>state_cache-218</b> Store few checkpoint states while syncing — <i>partial · low · M · disk, sync</i></summary>

**Idea.** During sync, skip storing checkpoint states or store them only once per archival interval rather than every epoch.

**Gap in Lighthouse.** Hierarchical diffs already make full storage sparse (diff every 32 slots), but there is no sync-specific skip: every imported block puts its state in state_cache and writes a summary. Could skip caching/diffing while syncing far behind head.

**Impact.** Some CPU/IO saved during range sync from diff computation at grid slots; small since diffs are sparse.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1661-1720`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1661-L1720) store_hot_state always caches and writes summary per state
- [`beacon_node/store/src/hdiff.rs:660-700`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L660-L700) storage_strategy: full diffs only at grid slots, replay otherwise
- [`beacon_node/store/src/config.rs:254`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L254) exponents 5,8,11,...

**Sources.** [grandine#607](https://github.com/grandinetech/grandine/pull/607), [grandine#609](https://github.com/grandinetech/grandine/pull/609)

</details>


<a id="state_cache-219"></a>
<details>
<summary><b>state_cache-219</b> Delay next-epoch duty lookahead into the epoch — <i>n/a · low · cpu</i></summary>

**Idea.** Schedule next-epoch duties a few slots into the epoch so the lookahead state need not be advanced across empty slots to compute shuffling and proposers.

**Impact.** Beacon node answers next-epoch duties from the primed shuffling cache without advancing the state across empty slots; timing of VC lookahead is not a BN state cost.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/attester_duties.rs:187-194`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L187-L194) next-epoch attester duties use partial_state_advance only on cache miss
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5213-5225`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5213-L5225) shuffling cache primed for Current and Next epoch on import

**Sources.** [nimbus#5406](https://github.com/status-im/nimbus-eth2/pull/5406)

</details>


<a id="state_cache-220"></a>
<details>
<summary><b>state_cache-220</b> Skip parent regen at genesis on startup — <i>n/a · low · startup</i></summary>

**Idea.** On startup, skip regenerating the parent state when the finalized or head state is genesis.

**Impact.** Lighthouse resumes from persisted fork choice/head and does not regenerate a parent state at startup, so there is nothing to skip.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/builder.rs:245-270`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L245-L270) resume_from_db loads persisted fork choice and states, no regen of parent at genesis

**Sources.** [prysm#6237](https://github.com/OffchainLabs/prysm/pull/6237)

</details>


<a id="state_cache-221"></a>
<details>
<summary><b>state_cache-221</b> Cache decompressed pubkeys only for active validators — <i>not · low · M · memory</i></summary>

**Idea.** Do not insert decompressed pubkeys into the pubkey cache for validators that are not active, since they produce no consensus messages.

**Gap in Lighthouse.** Cache is a dense Vec indexed by validator index covering all registry entries including pending/inactive; deposits-only validators are decompressed at import. Would need lazy/sparse decompression keyed by activation status in import().

**Impact.** Saves decompression time at first startup and memory for not-yet-active validators (small fraction of ~1M validators; some tens of MB).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:103-177`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L103-L177) import decompresses every key, parallel on first import
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:24`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L24) index-addressed Vec of PublicKey

**Sources.** [prysm#13581](https://github.com/OffchainLabs/prysm/pull/13581)

</details>


<a id="state_cache-222"></a>
<details>
<summary><b>state_cache-222</b> Exact state cache hit skips epoch transition — <i>implemented · low · S · cpu, disk</i></summary>

**Idea.** When writing a state, skip slow legacy database reads and skip the epoch transition when an exact state match is already cached.

**Impact.** Cached (advanced) states returned without disk load or slot processing; no legacy DB in Lighthouse.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1124-1132`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1124-L1132)
- [`beacon_node/store/src/state_cache.rs:308-326`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L308-L326)
- [`beacon_node/store/src/hot_cold_store.rs:1660-1690`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1660-L1690)

**Skeptic check.** get_advanced_hot_state hits the cache first and get_by_block_root returns the newest cached state &lt;= slot; store_hot_state detects Duplicate (still checks summary on disk, cheap). The Nimbus legacy-DB part has no Lighthouse counterpart.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus@60df17786](https://github.com/status-im/nimbus-eth2/commit/60df17786e5e)

</details>


<a id="state_cache-223"></a>
<details>
<summary><b>state_cache-223</b> Skip state-root check when replaying stored blocks — <i>implemented · low · S · cpu</i></summary>

**Idea.** When regenerating a state by replaying stored blocks, skip the per-block post-state hash tree root comparison against block.state_root.

**Impact.** Replay does not check state roots, and it gets per-slot roots without hashing whenever it can.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/block_replayer.rs:241-283`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/block_replayer.rs#L241-L283) apply_blocks runs per_block_processing and has no post-state root comparison
- [`consensus/state_processing/src/block_replayer.rs:180-213`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/block_replayer.rs#L180-L213) get_state_root takes the state root from state_root_iter or from the previous block's state_root, and hashes only on a miss

**Skeptic check.** Verified in block_replayer.rs: no post-block state-root check, and slot processing takes trusted roots from the blocks or the iterator.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#5316](https://github.com/Consensys-Incorporated/teku/pull/5316)

</details>


<a id="state_cache-224"></a>
<details>
<summary><b>state_cache-224</b> Skip block validation when replaying local blocks — <i>implemented · low · S · cpu</i></summary>

**Idea.** When regenerating states from blocks already validated on import, skip signature and other block validation.

**Impact.** All non-test BlockReplayer sites skip signature verification and most block-root checks.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2565-2567`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2565-L2567) replay_blocks uses no_signature_verification + minimal_block_root_verification
- [`beacon_node/http_api/src/sync_committee_rewards.rs:69-70`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/sync_committee_rewards.rs#L69-L70) the other production replayer also skips signatures
- [`consensus/state_processing/src/block_replayer.rs:262-268`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/block_replayer.rs#L262-L268) the proposer index is taken from the block and not recomputed

**Skeptic check.** Searched all BlockReplayer uses. Every non-test site disables signature verification, so no replay path verifies signatures.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#2203](https://github.com/Consensys-Incorporated/teku/pull/2203)

</details>


<a id="state_cache-225"></a>
<details>
<summary><b>state_cache-225</b> In-memory cache of diff base/snapshot states — <i>implemented · low · S · disk, cpu, latency</i></summary>

**Idea.** Cache decoded hierarchical-diff base snapshots and buffers in memory (keyed by slot, holding either state or buffer form and converting lazily) so historic state loads skip DB reads and decoding and sequential queries reuse prior work.

**Impact.** Already present (from Lighthouse's own PR #6475). The default sizes are small, so this is only a tuning question.

**Best measured result.** Most sequential queries after the first served in 400-700ms on mainnet (hierarchy exponents 5,7,11) (pr:lighthouse#6475)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/historic_state_cache.rs:14-56`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/historic_state_cache.rs#L14-L56) LRUs of HDiffBuffer and BeaconState keyed by slot, converted lazily
- [`beacon_node/store/src/hot_cold_store.rs:2310-2319`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2310-L2319) cold state loads check the historic cache
- [`beacon_node/store/src/config.rs:26-27`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L26-L27) defaults: 1 state, 16 hdiff buffers

**Skeptic check.** Confirmed that HistoricStateCache exists with lazy buffer/state conversion and is used on cold loads, as the earlier evidence said.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#17573](https://github.com/OffchainLabs/prysm/pull/17573), [prysm#17561](https://github.com/OffchainLabs/prysm/pull/17561), [lighthouse#6475](https://github.com/sigp/lighthouse/pull/6475)

</details>


<a id="state_cache-226"></a>
<details>
<summary><b>state_cache-226</b> Reclaimable soft/weak references for cached states — <i>n/a · low · L · memory</i></summary>

**Idea.** Hold non-head cached states or cached tree views through soft/weak references so the runtime reclaims them under memory pressure, bounding the cache by memory instead of count.

**Impact.** Rust has no soft/weak-reference reclamation by memory pressure; cache is bounded by count and finality.

**Best measured result.** avoids OOM at the expense of possible ~2x state access slowdown (pr:teku#2235)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:43`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L43) states is a count-bounded LruCache; Rust has no GC soft refs

**Sources.** [teku#2235](https://github.com/Consensys-Incorporated/teku/pull/2235), [lodestar#3420](https://github.com/ChainSafe/lodestar/pull/3420)

</details>


<a id="state_cache-227"></a>
<details>
<summary><b>state_cache-227</b> Sparse checkpoint replay at attestation pool init — <i>n/a · low · L · startup, cpu</i></summary>

**Idea.** At startup, replay checkpoint states only for the first block of each long interval rather than for many blocks, keeping only recent blocks exact.

**Impact.** Lighthouse persists fork choice and does not replay checkpoint states to init an attestation pool.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs): fork choice is persisted, no attestation-pool EpochRef replay at startup

**Sources.** [nimbus#8578](https://github.com/status-im/nimbus-eth2/pull/8578)

</details>


<a id="state_cache-228"></a>
<details>
<summary><b>state_cache-228</b> Replay from last block at or before slot — <i>implemented · low · S · cpu, disk</i></summary>

**Idea.** To get a state at a slot, load the state of the last block at or before that slot and advance empty slots, rather than replaying from the latest saved state.

**Impact.** State-by-slot resolves the exact state root (summaries exist for skipped slots) and loads from the nearest snapshot/diff, replaying only blocks after it.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1087-1110`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1087-L1110)
- [`beacon_node/store/src/hot_cold_store.rs:1124-1186`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1124-L1186)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1531-1560`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1531-L1560)

**Skeptic check.** Lighthouse never replays from 'the latest saved state'; hot loads use per-slot summaries and hdiff bases, cold loads use hierarchical diffs by slot. Earlier evidence right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#8218](https://github.com/OffchainLabs/prysm/pull/8218)

</details>


<a id="state_cache-229"></a>
<details>
<summary><b>state_cache-229</b> Shared state cache keyed by state root — <i>implemented · low · S · cpu, disk</i></summary>

**Idea.** Keep an in-memory state cache keyed by state root used by block processing, attestation handling and block production to avoid DB reloads.

**Impact.** Block import, attestation shuffling and block production all use the shared state-root-keyed cache.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:82`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L82) StateCache keyed by state root behind a Mutex
- [`beacon_node/store/src/state_cache.rs:275`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L275) get_by_state_root
- [`beacon_node/beacon_chain/src/block_production/mod.rs:89`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L89) production uses get_advanced_hot_state
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:400-430`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L400-L430) the attestation shuffling path uses the head or cached states

**Skeptic check.** Verified that the StateCache is shared and keyed by state root. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@2b026c147](https://github.com/ChainSafe/lodestar/commit/2b026c147049)

</details>


<a id="state_cache-230"></a>
<details>
<summary><b>state_cache-230</b> Central state regenerator serving all pre-states — <i>partial · low · M · cpu</i></summary>

**Idea.** Centralise pre-state lookup in one regenerator that serves block pre-states, attestation target states and duty states from caches and advances slots only when needed.

**Gap in Lighthouse.** Lookups are spread across the store state cache, shuffling cache, proposer cache and state_advance_timer, not one regenerator; unifying them is a refactor with no direct speedup.

**Impact.** Little speed gain; mostly code structure.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1124`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1124) get_advanced_hot_state serves block pre-states
- [`beacon_node/beacon_chain/src/shuffling_cache.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs) and beacon_proposer_cache.rs serve attestation/duty lookups
- [`beacon_node/beacon_chain/src/state_advance_timer.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs) pre-advances head state

**Sources.** [lodestar@2b40bb266](https://github.com/ChainSafe/lodestar/commit/2b40bb2668ef)

</details>


<a id="state_cache-231"></a>
<details>
<summary><b>state_cache-231</b> Store states as deltas over a base — <i>implemented · medium · S · disk, memory</i></summary>

**Idea.** Define delta types for validator identity and beacon state so stored states are deltas over a base state.

**Impact.** Already done: hot and cold states are stored as hierarchical diffs over snapshots, including a dedicated validators diff.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hdiff.rs:127`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L127) HDiff (state_diff, balances_diff, inactivity_scores_diff, validators diff) over a base buffer
- [`beacon_node/store/src/hdiff.rs:622`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L622) default exponents [5,9,11,13,16,18,21]
- [`beacon_node/store/src/hot_cold_store.rs:407`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L407) hot_storage_strategy uses the same hierarchy for hot states
- [`beacon_node/store/src/hot_cold_store.rs:1949`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1949) load_hot_state applies diffs from snapshot

**Skeptic check.** Verified HDiff has per-field deltas including validators and is used for both hot (hot_storage_strategy) and cold DBs. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [silver#40](https://github.com/gattaca-com/silver/pull/40), [ethlambda#661](https://github.com/lambdaclass/ethlambda/pull/661)

</details>


<a id="state_cache-232"></a>
<details>
<summary><b>state_cache-232</b> Compact backing-tree layout for balances and validators — <i>n/a · low · L · memory</i></summary>

**Idea.** Change the state backing tree layout for balances and validator branch nodes to use fewer nodes, cutting per-state memory.

**Impact.** Teku-specific backing tree layout; milhouse has its own packed leaves for balances and validators.

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.lock milhouse 0.9.0 (sigp/milhouse): Lighthouse uses its own persistent tree layout, not Teku's

**Sources.** [teku#3286](https://github.com/Consensys-Incorporated/teku/pull/3286), [teku#3287](https://github.com/Consensys-Incorporated/teku/pull/3287)

</details>


<a id="state_cache-233"></a>
<details>
<summary><b>state_cache-233</b> Committee caches embedded in the state — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** Keep committee/shuffling caches as fields on the state, built explicitly and invalidated per epoch, instead of a separate duplicate cached state.

**Impact.** Committee caches are Arc-shared state fields built explicitly per relative epoch.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:825`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L825)
- [`consensus/types/src/state/beacon_state.rs:1039`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1039)

**Skeptic check.** Lighthouse's own PR #249 origin; field committee_caches: [Arc&lt;CommitteeCache&gt;; CACHED_EPOCHS] confirmed.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#249](https://github.com/sigp/lighthouse/pull/249)

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

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [grandine#763](https://github.com/grandinetech/grandine/pull/763), [grandine@70e0aad90](https://github.com/grandinetech/grandine/commit/70e0aad900ad)

</details>


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


