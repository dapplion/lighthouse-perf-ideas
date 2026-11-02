# tree_hash

41 ideas: 9 not, 4 partial, 25 implemented, 3 n/a; 6 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

The area has 86 numbered ideas; the 45 ids missing here have not been checked against Lighthouse yet.

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [tree_hash-001](#tree_hash-001) **★** | SIMD multi-buffer SHA-256 for whole Merkle layers | not | high | L | cpu, memory |
| [tree_hash-002](#tree_hash-002) | Runtime-dispatched hardware-accelerated SHA-256 | implemented | low |  | cpu |
| [tree_hash-003](#tree_hash-003) | Batch node pairs into full AVX-512 groups | not | low | L | cpu |
| [tree_hash-006](#tree_hash-006) | Ensure and assert the fast hasher is used everywhere | implemented | low | S | cpu, memory |
| [tree_hash-007](#tree_hash-007) | Incremental dirty-leaf Merkle cache for beacon state | implemented | low |  | cpu, latency, memory |
| [tree_hash-008](#tree_hash-008) | Incremental tree hash cache for balances list | implemented | low |  | cpu |
| [tree_hash-017](#tree_hash-017) | Dirty hash cache only on real changes | implemented | medium | S | cpu |
| [tree_hash-019](#tree_hash-019) | Arena-backed tree hash cache with parallel registry | implemented | low |  | cpu, memory |
| [tree_hash-020](#tree_hash-020) **★** | Batch-hash dirty nodes collected at commit | not | medium | L | cpu, memory |
| [tree_hash-021](#tree_hash-021) | Run state hashing only at transitions | implemented | low |  | cpu |
| [tree_hash-022](#tree_hash-022) **★** | Bulk-build validator leaf hashes | not | medium | M | cpu, startup |
| [tree_hash-023](#tree_hash-023) | Cached child views with batched commit | implemented | low |  | cpu, latency |
| [tree_hash-024](#tree_hash-024) | Pack small basic fields into compact leaves | implemented | medium | S | memory, cpu |
| [tree_hash-026](#tree_hash-026) **★** | Compute block root once, cache and pass it along | partial | medium | M | cpu, latency, sync |
| [tree_hash-027](#tree_hash-027) | Cache block body root keyed by SSZ bytes | not | low | M | cpu |
| [tree_hash-033](#tree_hash-033) | Precomputed zero-subtree hash table for padding | implemented | low |  | cpu, memory, startup |
| [tree_hash-034](#tree_hash-034) | Hash node inputs directly without concatenation | implemented | low |  | cpu, memory |
| [tree_hash-035](#tree_hash-035) | Identity fast path for 32-byte root fields | implemented | low |  | cpu |
| [tree_hash-036](#tree_hash-036) | Reusable merkleizer scratch buffers | implemented | low |  | cpu, memory |
| [tree_hash-037](#tree_hash-037) | Allocation-free Merkle proof verification | implemented | low |  | cpu |
| [tree_hash-040](#tree_hash-040) | Exact-capacity preallocation of hashing buffers | implemented | low |  | cpu, memory |
| [tree_hash-047](#tree_hash-047) | Streaming bounded-memory Merkle accumulator | implemented | low |  | cpu, memory |
| [tree_hash-048](#tree_hash-048) | Derive many Merkle proofs from one tree | n/a | medium | S | cpu |
| [tree_hash-052](#tree_hash-052) | Upgrade SSZ library for faster hashing | n/a | low |  | cpu |
| [tree_hash-053](#tree_hash-053) | Persistent structurally shared Merkle tree for state | implemented | low |  | cpu, memory |
| [tree_hash-056](#tree_hash-056) | Extend tree hash cache to every list field | implemented | low |  | cpu, memory |
| [tree_hash-057](#tree_hash-057) | Partial top-level state root rebuild | partial | low | M | cpu, latency |
| [tree_hash-059](#tree_hash-059) | Full rebuild past a dirty-index threshold | n/a | medium | S | cpu, memory |
| [tree_hash-061](#tree_hash-061) **★** | Tune leaf bundle size of persistent lists | not | medium | L | cpu, memory |
| [tree_hash-064](#tree_hash-064) **★** | Persist Merkle caches to disk with states | partial | high | L | disk, latency |
| [tree_hash-065](#tree_hash-065) | Parallel hashing of large state lists | implemented | medium |  | cpu, latency, memory, startup |
| [tree_hash-068](#tree_hash-068) | Do not rehash already-hashed leaves | implemented | low |  | cpu |
| [tree_hash-071](#tree_hash-071) | Stack or inline buffers in tree hashing | implemented | low |  | cpu, memory |
| [tree_hash-072](#tree_hash-072) | Chunk byte data directly, no pack copy | implemented | low |  | cpu, memory |
| [tree_hash-074](#tree_hash-074) | Compact leaf storage with cached leaf hash | partial | low | M | cpu, memory |
| [tree_hash-076](#tree_hash-076) | Take previous state root from pre-state | implemented | low |  | cpu |
| [tree_hash-079](#tree_hash-079) | Build light client branches as one multiproof | not | low | S | cpu |
| [tree_hash-081](#tree_hash-081) | Collect proof siblings during merkleization | not | low | S | cpu, memory |
| [tree_hash-084](#tree_hash-084) | Skip state-root history hashing for attestations | implemented | low |  | cpu, memory |
| [tree_hash-085](#tree_hash-085) | Two-level dirty bitmap with deferred rehash | implemented | medium |  | cpu |
| [tree_hash-086](#tree_hash-086) | Cache progressive list roots on the list | not | low | M | cpu, latency |

★ actionable. Click an id for the full record.

## Ideas

<a id="tree_hash-001"></a>
<details>
<summary><b>tree_hash-001</b> SIMD multi-buffer SHA-256 for whole Merkle layers — <i>not · high · L · cpu, memory</i></summary>

**Idea.** When merkleizing, hash an entire layer of 64-byte child pairs in one call to a multi-buffer SIMD SHA-256 library (hashtree/gohashtree style, AVX2/AVX-512/NEON lanes) instead of one sha256 call per pair, and make it the default path for state hashing. Multi-lane kernels process several independent messages per instruction, so layer hashing costs a fraction of per-pair calls.

**Gap in Lighthouse.** Add a layer-wise multi-buffer hasher (e.g. hashtree-rs) to ethereum_hashing and use it from milhouse Tree::tree_hash and tree_hash merkleize_padded/MerkleHasher.

**Impact.** ~30% faster hashing elsewhere; mostly cold full rehashes and non-SHA-NI/ARM hosts.

**Best measured result.** ~30% faster hashing; 0.2-0.3s improvement per replayed state (pr:nimbus#5188)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/tree.rs:530-545 one hash32_concat per node pair after rayon::join
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/progressive_tree.rs:344 same per-pair pattern
- ~/.cargo/git/checkouts/tree_hash-f96cb869d9a8a64f/e5ea187/tree_hash/src/merkleize_padded.rs:82-139 per-chunk hash_fixed/hash32_concat
- ~/.cargo/registry/src/*/ethereum_hashing-0.8.0/src/lib.rs:24-36 only single-message hash/hash_fixed/hash32_concat
- Cargo.lock has no hashtree/hashtree-rs entry (hashtree-rs-0.2.0 in registry is unused)

**Second check.** Checked the actual git-pinned milhouse (d67aabd) and tree_hash (e5ea187) checkouts, not the registry copies the earlier review cited; both only call per-pair hash32_concat, parallelised by rayon but not SIMD-batched.

**Sources.** [caplin#6520](https://github.com/erigontech/erigon/pull/6520), [silver#49](https://github.com/gattaca-com/silver/pull/49), [nimbus#5188](https://github.com/status-im/nimbus-eth2/pull/5188), [prysm#16216](https://github.com/OffchainLabs/prysm/pull/16216), [prysm#12003](https://github.com/OffchainLabs/prysm/pull/12003), [prysm#15543](https://github.com/OffchainLabs/prysm/pull/15543), [prysm#13569](https://github.com/OffchainLabs/prysm/pull/13569), [lodestar#6977](https://github.com/ChainSafe/lodestar/pull/6977), [lodestar#8481](https://github.com/ChainSafe/lodestar/pull/8481), [prysm#15619](https://github.com/OffchainLabs/prysm/pull/15619), [prysm#10166](https://github.com/OffchainLabs/prysm/pull/10166), [prysm#11229](https://github.com/OffchainLabs/prysm/pull/11229), [prysm#10819](https://github.com/OffchainLabs/prysm/pull/10819), [prysm#11206](https://github.com/OffchainLabs/prysm/pull/11206), [prysm#12148](https://github.com/OffchainLabs/prysm/pull/12148)

</details>


<a id="tree_hash-002"></a>
<details>
<summary><b>tree_hash-002</b> Runtime-dispatched hardware-accelerated SHA-256 — <i>implemented · low · cpu</i></summary>

**Idea.** Use a SHA-256 implementation that detects CPU SHA extensions (SHA-NI, ARMv8 SHA) or AVX2 at runtime and dispatches to them, with a faster software fallback otherwise, for every tree-hash and shuffling digest. Hardware instructions are many times faster than a portable software implementation.

**Impact.** Already realised.

**Best measured result.** state tree hashing about 30% faster, 35ms to 25ms on Prater (Ryzen 5950X) (pr:lighthouse#2426)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/registry/src/*/ethereum_hashing-0.8.0/src/lib.rs:111 cpufeatures sha detection
- ~/.cargo/registry/src/*/ethereum_hashing-0.8.0/src/lib.rs:131 DynamicImpl::best picks sha2 (SHA-NI) else ring
- Cargo.lock ethereum_hashing deps: cpufeatures, ring, sha2

**Sources.** [prysm#3125](https://github.com/OffchainLabs/prysm/pull/3125), [teku#4842](https://github.com/Consensys-Incorporated/teku/pull/4842), [lighthouse#2426](https://github.com/sigp/lighthouse/pull/2426)

</details>


<a id="tree_hash-003"></a>
<details>
<summary><b>tree_hash-003</b> Batch node pairs into full AVX-512 groups — <i>not · low · L · cpu</i></summary>

**Idea.** Accumulate merkle pair hashes into full groups of 16 before calling the AVX-512 multi-buffer kernel, and use it where it beats SHA-NI, instead of issuing small partial batches. Full groups keep all SIMD lanes busy.

**Gap in Lighthouse.** Add a multi-buffer SHA-256 (AVX2/AVX-512, e.g. hashtree-style) to ethereum_hashing and make milhouse/tree_hash merkleize layers in batches (merkleize_padded, Tree::tree_hash) instead of per-pair calls.

**Impact.** Cold state hashing (full validator/balance trees, genesis, state loading without cache) could get a few times faster; per-slot incremental hashing gains little.

**Best measured result.** rehash&lt;FlatTree&lt;Current&gt;&gt; per block 1.099 -&gt; 0.711 ms; validators from_leaves 742 -&gt; 339 ms (pr:silver#432)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/registry/src/*/ethereum_hashing-0.8.0/src/lib.rs:31 hash_fixed / :36 hash32_concat hash one pair at a time
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/tree.rs:545 hash32_concat per node
- Cargo.lock has no hashtree/multibuffer crate

**Sources.** [silver#432](https://github.com/gattaca-com/silver/pull/432)

</details>


<a id="tree_hash-006"></a>
<details>
<summary><b>tree_hash-006</b> Ensure and assert the fast hasher is used everywhere — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Verify at build, startup or in CI that every merkleization path (generic helpers, all library instances and branches) resolves to the fast native SHA-256 implementation, with one explicitly selected copy of the hashing dependency. A silent fallback to a slow default hasher slows merkleization and raises allocation.

**Impact.** No gain; only guards regressions. A CI check would be optional. Single copy and dispatch is inside the crate so there is no slower generic path; no explicit assertion exists, but the failure mode is structurally absent.

**Best measured result.** 'significantly higher GC on mainnet' (screenshot, no numbers) (pr:lodestar#9352)

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.toml:153 single ethereum_hashing 0.8.0
- Cargo.lock: one ethereum_hashing entry, deps cpufeatures+ring+sha2
- ~/.cargo/registry/src/*/ethereum_hashing-0.8.0/src/lib.rs:131 runtime dispatch inside the crate

**Sources.** [lodestar#9349](https://github.com/ChainSafe/lodestar/pull/9349), [lodestar#7387](https://github.com/ChainSafe/lodestar/pull/7387), [lodestar#5969](https://github.com/ChainSafe/lodestar/pull/5969), [lodestar#7393](https://github.com/ChainSafe/lodestar/pull/7393), [lodestar@913da071b](https://github.com/ChainSafe/lodestar/commit/913da071b23d), [lodestar#9352](https://github.com/ChainSafe/lodestar/pull/9352), [lodestar#7394](https://github.com/ChainSafe/lodestar/pull/7394), [lodestar#7621](https://github.com/ChainSafe/lodestar/pull/7621), [lodestar#7705](https://github.com/ChainSafe/lodestar/pull/7705)

</details>


<a id="tree_hash-007"></a>
<details>
<summary><b>tree_hash-007</b> Incremental dirty-leaf Merkle cache for beacon state — <i>implemented · low · cpu, latency, memory</i></summary>

**Idea.** Keep a persistent cache of Merkle subtree hashes for the BeaconState and its large lists/vectors (validators, balances, root vectors), track dirty leaves, and on state root computation rehash only dirty leaves and their ancestors. This makes the per-slot state root O(changes * log n) instead of a full rehash.

**Impact.** Already realised.

**Best measured result.** "5x block processing speed on ncli_db" (commit:nimbus@f1dcee2749fe)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:3070`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3070) update_tree_hash_cache
- [`consensus/types/src/state/beacon_state.rs:3083`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3083) validators_mut().apply_updates
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/tree.rs:515 cached node hashes reused

**Sources.** [prysm#3155](https://github.com/OffchainLabs/prysm/pull/3155), [prysm#1711](https://github.com/OffchainLabs/prysm/pull/1711), [lighthouse@7b05c506d](https://github.com/sigp/lighthouse/commit/7b05c506df36), [nimbus@f1dcee274](https://github.com/status-im/nimbus-eth2/commit/f1dcee2749fe), [caplin#11096](https://github.com/erigontech/erigon/pull/11096), [prysm#4197](https://github.com/OffchainLabs/prysm/pull/4197), [lighthouse@b213a5ade](https://github.com/sigp/lighthouse/commit/b213a5ade479), [prysm#4421](https://github.com/OffchainLabs/prysm/pull/4421), [lighthouse@f65e981f6](https://github.com/sigp/lighthouse/commit/f65e981f6f12), [prysm#3076](https://github.com/OffchainLabs/prysm/pull/3076), [lighthouse@e28e97d3c](https://github.com/sigp/lighthouse/commit/e28e97d3c71c), [caplin#6264](https://github.com/erigontech/erigon/pull/6264), [prysm#6340](https://github.com/OffchainLabs/prysm/pull/6340), [prysm#5082](https://github.com/OffchainLabs/prysm/pull/5082), [prysm#4558](https://github.com/OffchainLabs/prysm/pull/4558), [prysm#6013](https://github.com/OffchainLabs/prysm/pull/6013), [silver#152](https://github.com/gattaca-com/silver/pull/152), [prysm#5398](https://github.com/OffchainLabs/prysm/pull/5398), [lighthouse#352](https://github.com/sigp/lighthouse/pull/352), [lighthouse#360](https://github.com/sigp/lighthouse/pull/360), [lighthouse#584](https://github.com/sigp/lighthouse/pull/584), [caplin#8234](https://github.com/erigontech/erigon/pull/8234), [lighthouse@56fe15625](https://github.com/sigp/lighthouse/commit/56fe15625bf3), [prysm#5117](https://github.com/OffchainLabs/prysm/pull/5117), [lighthouse@e5783d43a](https://github.com/sigp/lighthouse/commit/e5783d43a9c3), [silver#405](https://github.com/gattaca-com/silver/pull/405), [nimbus#5381](https://github.com/status-im/nimbus-eth2/pull/5381), [prysm#5118](https://github.com/OffchainLabs/prysm/pull/5118), [prysm#1929](https://github.com/OffchainLabs/prysm/pull/1929), [lighthouse@224a967cc](https://github.com/sigp/lighthouse/commit/224a967cce66)

</details>


<a id="tree_hash-008"></a>
<details>
<summary><b>tree_hash-008</b> Incremental tree hash cache for balances list — <i>implemented · low · cpu</i></summary>

**Idea.** Include the validator balances list in the incremental tree hash cache so a balance change rehashes only its chunk path. Balances change for most validators every epoch and are a large list, so full rehashing is expensive.

**Impact.** Already incremental: a balance change rehashes only its leaf-to-root path; nothing further to gain.

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/registry/src/*/milhouse-0.9.0/src/tree.rs:495 Tree::tree_hash caches per-node hash, so only dirty paths rehash
- [`consensus/types/src/state/beacon_state.rs:554`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L554) balances is milhouse List&lt;u64&gt;, packed leaves
- [`consensus/types/src/state/beacon_state.rs:3070`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3070) update_tree_hash_cache

**Sources.** [prysm#10552](https://github.com/OffchainLabs/prysm/pull/10552), [nimbus@fec01829c](https://github.com/status-im/nimbus-eth2/commit/fec01829c49a), [silver#74](https://github.com/gattaca-com/silver/pull/74), [prysm#9793](https://github.com/OffchainLabs/prysm/pull/9793)

</details>


<a id="tree_hash-017"></a>
<details>
<summary><b>tree_hash-017</b> Dirty hash cache only on real changes — <i>implemented · medium · S · cpu</i></summary>

**Idea.** Access cached-hash lists and fields through read-only accessors, mark subtrees dirty only on real writes (not on every setter or mutable borrow), skip recomputing a field cache when no element changed (e.g. validators during epoch processing), and deduplicate modified indices before recomputation. Spurious dirtying forces the next state root to rehash unchanged data.

**Impact.** Already avoids spurious dirtying: copy-on-write iterators and batched UpdateMap dedupe indices.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/effective_balance_updates.rs:25`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/effective_balance_updates.rs#L25),50 iter_cow + into_mut only on real change
- [`consensus/types/src/state/beacon_state.rs:3070`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3070) update_tree_hash_cache applies pending updates then hashes
- ~/.cargo/registry/src/*/milhouse-0.9.0/src/tree.rs:515 Node hash cached, recomputed only when zero (invalidated on change)

**Sources.** [nimbus#3660](https://github.com/status-im/nimbus-eth2/pull/3660), [prysm#6390](https://github.com/OffchainLabs/prysm/pull/6390), [nimbus#5286](https://github.com/status-im/nimbus-eth2/pull/5286), [prysm#5198](https://github.com/OffchainLabs/prysm/pull/5198)

</details>


<a id="tree_hash-019"></a>
<details>
<summary><b>tree_hash-019</b> Arena-backed tree hash cache with parallel registry — <i>implemented · low · cpu, memory</i></summary>

**Idea.** Store tree hash cache nodes in one contiguous arena instead of many small heap allocations, use stack buffers while hashing, and update validator registry subtrees in parallel. This cuts memory and allocator overhead and uses multiple cores.

**Impact.** The old arena cache (lighthouse#836) was replaced by milhouse persistent trees with Arc-shared nodes and parallel rayon hashing; same effect.

**Best measured result.** memory ~8gb to ~2.6gb; ~65% faster hashing; &gt;=50% faster parallel registry (pr:lighthouse#836)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/registry/src/*/milhouse-0.9.0/src/tree.rs:530 rayon::join parallel subtree hashing
- ~/.cargo/registry/src/*/milhouse-0.9.0/src/tree.rs:519 Zero(depth) nodes avoid materialising empty subtrees
- [`consensus/types/src/state/beacon_state.rs:554`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L554) balances/validators are milhouse persistent trees

**Sources.** [lighthouse#836](https://github.com/sigp/lighthouse/pull/836)

</details>


<a id="tree_hash-020"></a>
<details>
<summary><b>tree_hash-020</b> Batch-hash dirty nodes collected at commit — <i>not · medium · L · cpu, memory</i></summary>

**Idea.** During state commit, collect all dirty Merkle nodes (including modified validators) and hash them in one batched pass with a SIMD hasher on preallocated memory, instead of hashing node by node with a later traversal from the root. Fewer allocations and SIMD batching cut epoch-transition hashing time and GC.

**Gap in Lighthouse.** Level-order collection of dirty nodes hashed in batches into preallocated buffers; depends on a multi-buffer SHA-256 primitive (tree_hash-001).

**Impact.** A few ms per state root; modest.

**Best measured result.** saves around 2ms (pr:lodestar#7032)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/tree.rs:505-548 recursive per-node lazy tree_hash with RwLock per node and rayon::join
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/tree.rs:158 batch apply of updates is for values only, hashes are recomputed lazily
- [`consensus/types/src/state/beacon_state.rs:3852`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3852) apply_pending_mutations then inner.tree_hash_root()

**Second check.** Searched the pinned milhouse checkout for batched/level-order hashing (batch, hash_layer, simd); the only batching is applying value updates, not hashing.

**Sources.** [lodestar#7608](https://github.com/ChainSafe/lodestar/pull/7608), [lodestar#7032](https://github.com/ChainSafe/lodestar/pull/7032), [lodestar#7620](https://github.com/ChainSafe/lodestar/pull/7620), [lodestar#6939](https://github.com/ChainSafe/lodestar/pull/6939), [lodestar#7171](https://github.com/ChainSafe/lodestar/pull/7171)

</details>


<a id="tree_hash-021"></a>
<details>
<summary><b>tree_hash-021</b> Run state hashing only at transitions — <i>implemented · low · cpu</i></summary>

**Idea.** Do the batched state hashing only after block and epoch processing, not on every hash_tree_root call, so intermediate root requests do not trigger repeated hashing work.

**Impact.** Repeated root requests hit cached node hashes; hashing happens when mutations are applied, so nothing extra to gain.

**Best measured result.** lg1k comparable; test mainnet node better (graphs only) (pr:lodestar#7030)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:3070`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3070) update_tree_hash_cache applies pending mutations once then hashes
- [`consensus/state_processing/src/per_slot_processing.rs:129`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_slot_processing.rs#L129) root computed in slot processing
- ~/.cargo/registry/src/*/milhouse-0.9.0/src/tree.rs:495 node hashes cached, repeat root requests are O(1)

**Sources.** [lodestar#7030](https://github.com/ChainSafe/lodestar/pull/7030)

</details>


<a id="tree_hash-022"></a>
<details>
<summary><b>tree_hash-022</b> Bulk-build validator leaf hashes — <i>not · medium · M · cpu, startup</i></summary>

**Idea.** When rebuilding the validator list trie (state load or full rebuild), compute all validator roots in one batched SIMD pass instead of hashing validators one by one.

**Gap in Lighthouse.** No bulk SIMD validator-root pass; cold full rebuild (startup) hashes validators one by one (rayon-parallel). Rebase on finalized state avoids most validator rehash on later loads.

**Impact.** Only the cold full validator-list rehash at startup/checkpoint load; rebase already covers later loads.

**Best measured result.** accelerate by a large factor (no numbers) (pr:prysm#12585)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/tree.rs:507-527 Leaf hash computed lazily per validator via value.tree_hash_root()
- [`consensus/types/src/validator/validator.rs:19`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/validator/validator.rs#L19) derive(TreeHash) per-validator MerkleHasher
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/tree.rs:292-296 rebase reuses equal validator leaves (with hashes) from the finalized state, avoiding rehash rather than batching it

**Second check.** Found that Tree::rebase_on reuses already-hashed validator leaves from the finalized state, which reduces the need for this, but no batched bulk hashing exists.

**Sources.** [prysm#12585](https://github.com/OffchainLabs/prysm/pull/12585), [silver#44](https://github.com/gattaca-com/silver/pull/44)

</details>


<a id="tree_hash-023"></a>
<details>
<summary><b>tree_hash-023</b> Cached child views with batched commit — <i>implemented · low · cpu, latency</i></summary>

**Idea.** Make tree-backed state views cache child views and buffer writes in a map, then commit them in one batched tree rebuild that reuses unchanged subtrees, so reads are near array speed and writes do not rewrite tree paths each time.

**Impact.** Milhouse already buffers writes and commits in one batched rebuild.

**Best measured result.** Epoch 16384: 0.897 to 0.266 s; 32768: 1.638 to 0.452 s; block import 16384: 0.266 to 0.121 s (pr:teku#1465)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/registry/src/*/milhouse-0.9.0/src/interface.rs:39 Interface buffers writes in UpdateMap
- ~/.cargo/registry/src/*/milhouse-0.9.0/src/interface.rs:86 apply_updates batched rebuild
- ~/.cargo/registry/src/*/milhouse-0.9.0/src/tree.rs:158 with_updated_leaves reuses unchanged subtrees
- [`consensus/types/src/state/beacon_state.rs:3852`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3852) apply_pending_mutations

**Sources.** [teku#1465](https://github.com/Consensys-Incorporated/teku/pull/1465)

</details>


<a id="tree_hash-024"></a>
<details>
<summary><b>tree_hash-024</b> Pack small basic fields into compact leaves — <i>implemented · medium · S · memory, cpu</i></summary>

**Idea.** Store small basic fields (u64, bool) of containers such as Validator in compact leaf nodes holding only their bytes instead of a full 32-byte chunk node per field, shrinking the state tree and speeding traversal.

**Impact.** Equivalent already: validators are one leaf each, basic lists are packed, so tree is small.

**Best measured result.** state memory down ~25%; ~34 -&gt; ~35 slots/sec (pr:teku#3032)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/registry/src/*/milhouse-0.9.0/src/tree.rs Leaf stores the whole value (Validator) with one cached hash, not per-field nodes
- ~/.cargo/registry/src/*/milhouse-0.9.0/src/packed_leaf.rs PackedLeaf packs u64 balances/inactivity scores and bools into chunk-sized leaves
- [`consensus/types/src/validator/validator.rs:19`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/validator/validator.rs#L19) Validator is a single leaf value

**Sources.** [teku#3032](https://github.com/Consensys-Incorporated/teku/pull/3032)

</details>


<a id="tree_hash-026"></a>
<details>
<summary><b>tree_hash-026</b> Compute block root once, cache and pass it along — <i>partial · medium · M · cpu, latency, sync</i></summary>

**Idea.** Cache the block (and body) hash_tree_root in the block object once computed or on deserialization, and pass it with the block through gossip, import, storage, signing and fork-choice paths instead of recomputing it. The root is otherwise computed several times per block.

**Gap in Lighthouse.** Root is threaded on main import paths but not cached in SignedBeaconBlock; ~67 non-test canonical_root() call sites in beacon_node/consensus can still recompute.

**Impact.** Small remaining saving; a body hash per redundant call on large blocks.

**Best measured result.** Estimated 20-50 ms saved per block (5-15 ms per HTR, called 7-10 times) (pr:prysm#11530)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/block/signed_beacon_block.rs:359`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/block/signed_beacon_block.rs#L359) canonical_root() recomputes tree_hash_root, no cached field in the struct (line 102)
- [`beacon_node/beacon_chain/src/block_verification_types.rs:23-37`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification_types.rs#L23-L37),76-79,120-148 RpcBlock/AvailableBlock carry block_root alongside block
- [`beacon_node/beacon_chain/src/block_verification.rs:890`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L890),908 gossip verify computes root once and threads it

**Second check.** Confirmed no OnceLock/cached root in SignedBeaconBlock and counted remaining canonical_root() callers; earlier partial verdict stands.

**Sources.** [nimbus#1330](https://github.com/status-im/nimbus-eth2/pull/1330), [nimbus#1332](https://github.com/status-im/nimbus-eth2/pull/1332), [prysm#11530](https://github.com/OffchainLabs/prysm/pull/11530), [nimbus#1329](https://github.com/status-im/nimbus-eth2/pull/1329), [teku#2875](https://github.com/Consensys-Incorporated/teku/pull/2875), [grandine@04aaa88c6](https://github.com/grandinetech/grandine/commit/04aaa88c615d), [grandine#492](https://github.com/grandinetech/grandine/pull/492), [prysm#7716](https://github.com/OffchainLabs/prysm/pull/7716)

</details>


<a id="tree_hash-027"></a>
<details>
<summary><b>tree_hash-027</b> Cache block body root keyed by SSZ bytes — <i>not · low · M · cpu</i></summary>

**Idea.** Cache the block body hash_tree_root keyed by its SSZ encoding: re-encode, compare to cached bytes, return the cached root on a match. Encoding is much cheaper than hashing and the body root is requested many times per block.

**Gap in Lighthouse.** Add a body-root cache (SSZ bytes -&gt; root) used by BeaconBlock::block_header / canonical_root; or hash once and carry the root alongside the block (block already has root in most import paths).

**Impact.** Saves a few body re-hashes per block (a body is up to ~100s KB with attestations); likely sub-millisecond to a few ms per block, minor.

**Best measured result.** hit about 14x faster; miss ~6% slower; ~41 KB retained per body (pr:caplin#25191)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/block/beacon_block_body.rs:135`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/block/beacon_block_body.rs#L135) BeaconBlockBody derives TreeHash, no cached root
- [`consensus/types/src/block/signed_beacon_block.rs:359`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/block/signed_beacon_block.rs#L359) canonical_root recomputes
- [`consensus/types/src/block/beacon_block_body.rs:329`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/block/beacon_block_body.rs#L329) per-field tree_hash_root

**Sources.** [caplin#25191](https://github.com/erigontech/erigon/pull/25191)

</details>


<a id="tree_hash-033"></a>
<details>
<summary><b>tree_hash-033</b> Precomputed zero-subtree hash table for padding — <i>implemented · low · cpu, memory, startup</i></summary>

**Idea.** Precompute the zero-subtree hashes for every depth once (ideally as a compile-time global constant) and use them for padding to the list limit and for subtrees wholly past the last leaf. Padding then costs O(log n) lookups instead of hashing zero chunks, and no table is computed at runtime or threaded through calls.

**Impact.** Padding is already table lookups (LazyLock rather than const, negligible).

**Best measured result.** can be an x10 increase in performance (pr:prysm#3995)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/registry/src/*/ethereum_hashing-0.8.0/src/lib.rs:219 ZERO_HASHES static table up to depth 48
- ~/.cargo/registry/src/*/tree_hash-0.12.1/src/lib.rs:93 get_zero_hash used for padding
- ~/.cargo/registry/src/*/milhouse-0.9.0/src/tree.rs:519 Zero(depth) uses ZERO_HASHES

**Sources.** [nimbus@f53b55cbe](https://github.com/status-im/nimbus-eth2/commit/f53b55cbe0cc), [nimbus#1073](https://github.com/status-im/nimbus-eth2/pull/1073), [silver#51](https://github.com/gattaca-com/silver/pull/51), [lighthouse#436](https://github.com/sigp/lighthouse/pull/436), [prysm#3995](https://github.com/OffchainLabs/prysm/pull/3995), [lodestar@bade37edb](https://github.com/ChainSafe/lodestar/commit/bade37edb5a2), [silver#45](https://github.com/gattaca-com/silver/pull/45)

</details>


<a id="tree_hash-034"></a>
<details>
<summary><b>tree_hash-034</b> Hash node inputs directly without concatenation — <i>implemented · low · cpu, memory</i></summary>

**Idea.** Combine two 32-byte child roots (and length mix-ins) by updating the digest with each input slice directly, without generic serialization, stream machinery or a concatenated temporary buffer. Node combines dominate hashing, so removing the copy and allocation per sha256 is a large win.

**Impact.** Already done.

**Best measured result.** ~50% speedup; make test 4m53s to 2m23s; fixtures test 56.9s to 25.8s (pr:nimbus#595)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/registry/src/*/ethereum_hashing-0.8.0/src/lib.rs:36 hash32_concat updates context with each slice, no concat buffer
- ~/.cargo/registry/src/*/tree_hash-0.12.1/src/lib.rs:64 mix_in_length uses hash32_concat
- ~/.cargo/registry/src/*/milhouse-0.9.0/src/tree.rs:532 node combine via hash32_concat

**Sources.** [nimbus#595](https://github.com/status-im/nimbus-eth2/pull/595), [lodestar@5fcf84f4f](https://github.com/ChainSafe/lodestar/commit/5fcf84f4f693), [teku#4834](https://github.com/Consensys-Incorporated/teku/pull/4834)

</details>


<a id="tree_hash-035"></a>
<details>
<summary><b>tree_hash-035</b> Identity fast path for 32-byte root fields — <i>implemented · low · cpu</i></summary>

**Idea.** When a field is a 32-byte root/digest, return it as its own hash_tree_root instead of passing it through generic chunk merkleization.

**Impact.** 32-byte roots are returned with a copy and no hashing; equivalent to identity fast path.

**Best measured result.** ~50% speedup (commit title) (commit:nimbus@bde20436e86f)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/registry/src/*/tree_hash-0.12.1/src/impls.rs:137 FixedBytes&lt;N&gt; (Hash256) delegates to [u8;N]
- ~/.cargo/registry/src/*/tree_hash-0.12.1/src/impls.rs:73 root via merkle_root
- ~/.cargo/registry/src/*/tree_hash-0.12.1/src/lib.rs:31 merkle_root leaves==1 returns bytes copied, no hashing

**Sources.** [nimbus@bde20436e](https://github.com/status-im/nimbus-eth2/commit/bde20436e86f)

</details>


<a id="tree_hash-036"></a>
<details>
<summary><b>tree_hash-036</b> Reusable merkleizer scratch buffers — <i>implemented · low · cpu, memory</i></summary>

**Idea.** Merkleize with a reusable hasher and reusable scratch layer/chunk buffers (with room for padding) instead of allocating new buffers per layer, item or call, for example when merkleizing transaction lists.

**Impact.** Already allocation-light; no meaningful gain left.

**Best measured result.** 524955 B/op, 8195 allocs -&gt; 705 B/op, 5 allocs (pr:prysm#5234)

**Evidence (Lighthouse @ 928b61e719).**

- e5ea187/tree_hash/src/merkle_hasher.rs:200 half_nodes SmallVec sized to depth, no per-layer Vec
- e5ea187/tree_hash/src/lib.rs:49 merkle_root streams into MerkleHasher

**Sources.** [prysm#5234](https://github.com/OffchainLabs/prysm/pull/5234), [caplin#7488](https://github.com/erigontech/erigon/pull/7488), [caplin#22518](https://github.com/erigontech/erigon/pull/22518)

</details>


<a id="tree_hash-037"></a>
<details>
<summary><b>tree_hash-037</b> Allocation-free Merkle proof verification — <i>implemented · low · cpu</i></summary>

**Idea.** In Merkle branch verification, hash into fixed stack buffers and use the index bit only to order the two inputs, avoiding a heap allocation per level.

**Impact.** Done in #8614.

**Best measured result.** 33% faster, about 1.2us saved at depth 32 (pr:lighthouse#8614)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/merkle_proof/src/lib.rs:381`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/merkle_proof/src/lib.rs#L381) merkle_root_from_branch uses ith_bit to order slices and hash32_concat on stack arrays

**Sources.** [lighthouse#8614](https://github.com/sigp/lighthouse/pull/8614)

</details>


<a id="tree_hash-040"></a>
<details>
<summary><b>tree_hash-040</b> Exact-capacity preallocation of hashing buffers — <i>implemented · low · cpu, memory</i></summary>

**Idea.** Allocate leaf, input and output buffers in tree hashing and field tries at their known final capacity (from the actual field or element count) in one allocation instead of a hard-coded guess or growing and copying them.

**Impact.** Nothing left to gain.

**Best measured result.** Body construction 11543 -&gt; 1727 ns/op, 309 -&gt; 1 allocs; full 11.70ms -&gt; 10.93ms (pr:prysm#182)

**Evidence (Lighthouse @ 928b61e719).**

- e5ea187/tree_hash_derive/src/lib.rs:140 MerkleHasher::with_leaves(num_leaves) from field count
- e5ea187/tree_hash/src/impls.rs:179 bitfield with_leaves(leaf_count)
- e5ea187/tree_hash/src/merkle_hasher.rs:200 with_capacity(depth-1)

**Sources.** [lighthouse@bf1a93f44](https://github.com/sigp/lighthouse/commit/bf1a93f44422), [prysm#6722](https://github.com/OffchainLabs/prysm/pull/6722), [prysm#9977](https://github.com/OffchainLabs/prysm/pull/9977), [prysm#182](https://github.com/OffchainLabs/prysm/pull/182)

</details>


<a id="tree_hash-047"></a>
<details>
<summary><b>tree_hash-047</b> Streaming bounded-memory Merkle accumulator — <i>implemented · low · cpu, memory</i></summary>

**Idea.** Merkleize large lists and vectors by streaming chunks or child roots into a log-depth stack of partial hashes (a streaming MerkleHasher) instead of allocating a chunk array proportional to the input, and return fixed 32-byte roots instead of heap vectors. Workspace stays constant.

**Impact.** Done; roots are fixed Hash256.

**Evidence (Lighthouse @ 928b61e719).**

- e5ea187/tree_hash/src/merkle_hasher.rs:141 half_nodes log-depth stack
- [`beacon_node/beacon_chain/src/naive_aggregation_pool.rs:49`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/naive_aggregation_pool.rs#L49) MerkleHasher use
- [`consensus/types/src/block/beacon_block_body.rs:1627`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/block/beacon_block_body.rs#L1627) ProgressiveMerkleHasher

**Sources.** [lodestar@0d0498823](https://github.com/ChainSafe/lodestar/commit/0d04988234a1), [lodestar@3da79f3ef](https://github.com/ChainSafe/lodestar/commit/3da79f3ef34a), [nimbus@3ecb19763](https://github.com/status-im/nimbus-eth2/commit/3ecb197635be), [lodestar@1ceb7ca7d](https://github.com/ChainSafe/lodestar/commit/1ceb7ca7d14e), [lighthouse#861](https://github.com/sigp/lighthouse/pull/861)

</details>


<a id="tree_hash-048"></a>
<details>
<summary><b>tree_hash-048</b> Derive many Merkle proofs from one tree — <i>n/a · medium · S · cpu</i></summary>

**Idea.** Build the deposit (or other) Merkle tree once, or stream it once, and derive every needed proof from it, instead of rebuilding a tree from a growing prefix per proof, which is quadratic.

**Impact.** Lighthouse keeps one incremental tree (push_leaf is O(depth), proofs from the same tree); no deposit proof generation on a running mainnet node (deposit cache removed), only genesis tooling.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/common/deposit_data_tree.rs:9-60`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/deposit_data_tree.rs#L9-L60) incremental MerkleTree push_leaf and generate_proof
- [`consensus/state_processing/src/genesis.rs:37-45`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/genesis.rs#L37-L45) only user is genesis building

**Sources.** [nimbus@3d121d973](https://github.com/status-im/nimbus-eth2/commit/3d121d973401), [nimbus@07206ca26](https://github.com/status-im/nimbus-eth2/commit/07206ca264b1)

</details>


<a id="tree_hash-052"></a>
<details>
<summary><b>tree_hash-052</b> Upgrade SSZ library for faster hashing — <i>n/a · low · cpu</i></summary>

**Idea.** Upgrade the SSZ library to a release with a faster hash_tree_root implementation.

**Impact.** Nimbus-specific library bump; Lighthouse already uses its own recent tree_hash/ethereum_hashing.

**Best measured result.** 10% hash_tree_root perf increase (pr:nimbus#5292)

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.toml:262 tree_hash 0.12 (sigp fork rev e5ea187), ethereum_hashing 0.8.0 at line 153

**Sources.** [nimbus#5292](https://github.com/status-im/nimbus-eth2/pull/5292)

</details>


<a id="tree_hash-053"></a>
<details>
<summary><b>tree_hash-053</b> Persistent structurally shared Merkle tree for state — <i>implemented · low · cpu, memory</i></summary>

**Idea.** Back the BeaconState with a persistent (copy-on-write) binary Merkle tree whose nodes cache their hashes, so a mutation clones only the path to the touched leaf and states across slots/forks share untouched subtrees. Rehashing and state copies then touch only changed paths.

**Impact.** Core design of Lighthouse BeaconState.

**Best measured result.** Block import 16384 validators 0.266 s to ~0.19 s class (32768: 2.497 s to 0.387 s); epoch 32768 2.859 s to 1.638 s (pr:teku#1133)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:523`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L523) milhouse List/Vector fields
- d67aabd/src/tree.rs:20 Node hash cached in RwLock, structural sharing via Arc
- [`consensus/types/Cargo.toml:52`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/Cargo.toml#L52) milhouse

**Sources.** [teku#1133](https://github.com/Consensys-Incorporated/teku/pull/1133), [lodestar@2a4c9cb62](https://github.com/ChainSafe/lodestar/commit/2a4c9cb62f21), [silver#42](https://github.com/gattaca-com/silver/pull/42)

</details>


<a id="tree_hash-056"></a>
<details>
<summary><b>tree_hash-056</b> Extend tree hash cache to every list field — <i>implemented · low · cpu, memory</i></summary>

**Idea.** Give each large or frequently changing state field its own incremental tree hash cache (participation flags, inactivity scores, eth1 data votes, randao mixes, slashings, remaining fields), so no field is fully rehashed on each state root.

**Impact.** Every large field is a milhouse type with cached subtree hashes.

**Best measured result.** proposer index recompute potentially 128ms on large networks (pr:lighthouse#2459)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:529`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L529) eth1_data_votes List
- [`consensus/types/src/state/beacon_state.rs:563`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L563) randao_mixes Vector
- [`consensus/types/src/state/beacon_state.rs:568`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L568) slashings Vector
- [`consensus/types/src/state/beacon_state.rs:585`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L585) participation List
- [`consensus/types/src/state/beacon_state.rs:627`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L627) inactivity_scores List

**Sources.** [lighthouse#2459](https://github.com/sigp/lighthouse/pull/2459), [silver#186](https://github.com/gattaca-com/silver/pull/186), [silver#187](https://github.com/gattaca-com/silver/pull/187), [silver#182](https://github.com/gattaca-com/silver/pull/182), [lighthouse#919](https://github.com/sigp/lighthouse/pull/919), [lighthouse#2504](https://github.com/sigp/lighthouse/pull/2504)

</details>


<a id="tree_hash-057"></a>
<details>
<summary><b>tree_hash-057</b> Partial top-level state root rebuild — <i>partial · low · M · cpu, latency</i></summary>

**Idea.** Cache the top-level BeaconState container tree and, after field changes, recompute only the changed fields' subtrees and the spine to the root instead of rehashing the whole container.

**Gap in Lighthouse.** Large fields are cached inside milhouse, but the top container spine and small fields (fork, header, eth1_data, checkpoints, sync committee Arcs) are rehashed every state root; no cached container tree with dirty-field tracking. Would need a per-field dirty flag plus cached spine nodes in BeaconState tree-hash path.

**Impact.** Saves roughly 40 hashes per state root plus small-field hashing, microseconds; negligible next to validators/balances hashing.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:3070`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3070) update_tree_hash_cache calls derived inner.tree_hash_root()
- e5ea187/tree_hash_derive/src/lib.rs:140 derive builds a fresh MerkleHasher over all fields each call

**Sources.** [prysm#17034](https://github.com/OffchainLabs/prysm/pull/17034), [prysm#17291](https://github.com/OffchainLabs/prysm/pull/17291), [prysm#17002](https://github.com/OffchainLabs/prysm/pull/17002)

</details>


<a id="tree_hash-059"></a>
<details>
<summary><b>tree_hash-059</b> Full rebuild past a dirty-index threshold — <i>n/a · medium · S · cpu, memory</i></summary>

**Idea.** Cap the per-field dirty-index list; beyond a threshold drop it and rebuild the field's Merkle tree fully, since O(k log n) incremental updates exceed O(n) rebuild for large k and the index list itself costs memory.

**Gap in Lighthouse.** Lighthouse's milhouse buffers pending leaf values (not a dirty-index list) and with_updated_leaves walks only subtrees containing updates, so cost is capped near O(n) and the idea's memory/threshold problem does not arise in that form.

**Impact.** Negligible; apply_updates visits each touched node once so dense updates are already bounded by tree size.

**Best measured result.** "Fixes up wild memory usage" (no numbers) (pr:prysm#8740)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/tree.rs:164 with_updated_leaves prunes by index range per subtree
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/update_map.rs:1 UpdateMap holds values not index list

**Sources.** [prysm#8740](https://github.com/OffchainLabs/prysm/pull/8740)

</details>


<a id="tree_hash-061"></a>
<details>
<summary><b>tree_hash-061</b> Tune leaf bundle size of persistent lists — <i>not · medium · L · cpu, memory</i></summary>

**Idea.** Pack multiple elements (e.g. 64 balances or inactivity scores) per persistent-tree leaf node for frequently mutated uint64 lists, which reduces tree depth, node count and copy-on-write/hashing overhead.

**Gap in Lighthouse.** Milhouse would need a configurable leaf bundle (e.g. 64 u64 per leaf, a multi-chunk PackedLeaf hashed as a subtree) in PackedLeaf, Tree::with_updated_leaves, Builder and ProgressiveTree, used for balances and inactivity_scores.

**Impact.** Fewer Arc nodes and shallower CoW for balances/inactivity_scores (memory per state and update cost); gain uncertain because each dirty leaf rehashes its bundle.

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/packed_leaf.rs:43 PackedLeaf holds exactly one 32-byte chunk (BYTES_PER_CHUNK / packing_factor per value, 4 u64)
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/utils.rs:67 opt_packing_factor = T::tree_hash_packing_factor(), no configurable bundle
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/utils.rs:75 opt_packing_depth = log2(packing factor) only
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/progressive_tree.rs:68 Gloas ProgressiveList uses the same packing factor
- [`consensus/types/src/state/beacon_state.rs:554`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L554) balances: List&lt;u64&gt; (pre-Gloas), :559 ProgressiveList&lt;u64&gt; (Gloas), :629 inactivity_scores List&lt;u64&gt;, no custom leaf type

**Second check.** Checked milhouse utils packing depth/factor, the Gloas ProgressiveList/ProgressiveTree path and Lighthouse tree_hash_packing_factor overrides (none for u64); every leaf is still a single 32-byte chunk.

**Sources.** [grandine@4ff6dcaf4](https://github.com/grandinetech/grandine/commit/4ff6dcaf444e)

</details>


<a id="tree_hash-064"></a>
<details>
<summary><b>tree_hash-064</b> Persist Merkle caches to disk with states — <i>partial · high · L · disk, latency</i></summary>

**Idea.** Save the cached Merkle layers of large state lists alongside stored states and reload them, so a state loaded after a reorg or restart does not need a full rehash.

**Gap in Lighthouse.** Merkle caches are not persisted to disk: after a restart the first loaded (finalized/anchor) state is fully rehashed. Reorg/hot loads already reuse the in-memory finalized state's hashed subtrees via rebase, so only changed subtrees are rehashed.

**Impact.** Remaining saving is only the one-off full rehash at startup or for states older than the finalized state; the reorg case the idea targets is already mostly covered.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1984-1988`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1984-L1988) hdiff-loaded state is rebased on the finalized state before hashing
- [`beacon_node/store/src/hot_cold_store.rs:2009-2013`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2009-L2013) replay base state rebased 'so that we can reuse parts of the tree for state root calculation'
- [`beacon_node/store/src/state_cache.rs:197-208`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L197-L208) rebase_on_finalized
- [`consensus/types/src/state/beacon_state.rs:3416`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3416) BeaconState::rebase_on per field
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/tree.rs:282-330 Tree::rebase_on replaces equal leaves/subtrees with the base's already-hashed nodes (EqualReplace), short-cutting on equal hashes

**Second check.** The earlier review missed that load_hot_state rebases disk-loaded states on the in-memory finalized state, and milhouse rebase swaps in the base's hashed nodes, which gives an equivalent effect for reorg/hot loads without disk persistence.

**Sources.** [caplin#11554](https://github.com/erigontech/erigon/pull/11554)

</details>


<a id="tree_hash-065"></a>
<details>
<summary><b>tree_hash-065</b> Parallel hashing of large state lists — <i>implemented · medium · cpu, latency, memory, startup</i></summary>

**Idea.** Split the hashing of large lists (validator registry, balances, wide Merkle layers) across worker threads, each with its own scratch buffers and no shared locks in the inner loop, especially for cold full-tree builds.

**Impact.** Already realised.

**Best measured result.** cold HashSSZ 395-457 ms -&gt; 66-96 ms; Hoodi cold hash 3.89 s -&gt; 0.53 s wall (8 workers) (pr:caplin#25101)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/tree.rs:542 rayon::join(left.tree_hash, right.tree_hash) at every Node
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/progressive_tree.rs:344 same for progressive trees

**Sources.** [caplin#25101](https://github.com/erigontech/erigon/pull/25101), [prysm#17317](https://github.com/OffchainLabs/prysm/pull/17317), [prysm#12637](https://github.com/OffchainLabs/prysm/pull/12637), [caplin#6854](https://github.com/erigontech/erigon/pull/6854), [prysm#12639](https://github.com/OffchainLabs/prysm/pull/12639)

</details>


<a id="tree_hash-068"></a>
<details>
<summary><b>tree_hash-068</b> Do not rehash already-hashed leaves — <i>implemented · low · cpu</i></summary>

**Idea.** When merkleizing leaves that are already 32-byte roots, start at the first internal layer instead of hashing the leaves again, and avoid any extra hashing round on outputs.

**Impact.** Nothing to gain; child roots are never rehashed.

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/tree_hash-f96cb869d9a8a64f/e5ea187/tree_hash/src/merkle_hasher.rs:215 MerkleHasher.write takes 32-byte roots as leaves via process_leaf, hashed only in pairs
- ~/.cargo/git/checkouts/tree_hash-f96cb869d9a8a64f/e5ea187/tree_hash/src/merkle_hasher.rs:243 depth-1 tree: root equals the leaf, no hashing
- ~/.cargo/git/checkouts/tree_hash-f96cb869d9a8a64f/e5ea187/tree_hash/src/lib.rs:29 merkle_root fast paths: 1 leaf returns bytes, 2 leaves one hash_fixed
- ~/.cargo/git/checkouts/ssz_types-19f835ca387d51e3/8955d22/src/tree_hash.rs:42 container/list items write item.tree_hash_root() as leaf

**Sources.** [nimbus#42](https://github.com/status-im/nimbus-eth2/pull/42), [lodestar@069107aa0](https://github.com/ChainSafe/lodestar/commit/069107aa0253), [prysm#1653](https://github.com/OffchainLabs/prysm/pull/1653)

</details>


<a id="tree_hash-071"></a>
<details>
<summary><b>tree_hash-071</b> Stack or inline buffers in tree hashing — <i>implemented · low · cpu, memory</i></summary>

**Idea.** Use fixed-size stack or inline small-vector buffers (32-byte arrays) for packed leaf encoding, length mix-in and leaf scratch instead of heap-allocated vectors per call or element.

**Impact.** Already done (lighthouse#3581); no further saving.

**Best measured result.** block root 10-11ms to 8-9ms (pr:lighthouse#3581)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/tree_hash-f96cb869d9a8a64f/e5ea187/tree_hash/src/lib.rs:24 PackedEncoding = SmallVec&lt;[u8; SMALLVEC_SIZE]&gt; (inline)
- ~/.cargo/git/checkouts/tree_hash-f96cb869d9a8a64f/e5ea187/tree_hash/src/merkle_hasher.rs:141 half_nodes SmallVec8, :151 buffer SmallVec&lt;[u8;32]&gt;
- ~/.cargo/git/checkouts/tree_hash-f96cb869d9a8a64f/e5ea187/tree_hash/src/lib.rs:62 mix_in_length uses a [0;32] stack array and hash32_concat

**Sources.** [lighthouse#3581](https://github.com/sigp/lighthouse/pull/3581), [prysm#16251](https://github.com/OffchainLabs/prysm/pull/16251), [caplin#22486](https://github.com/erigontech/erigon/pull/22486)

</details>


<a id="tree_hash-072"></a>
<details>
<summary><b>tree_hash-072</b> Chunk byte data directly, no pack copy — <i>implemented · low · cpu, memory</i></summary>

**Idea.** Chunk byte lists and uint64 lists into 32-byte leaves directly in one pass with one exact allocation, skipping intermediate pack-into-chunks buffers.

**Impact.** No intermediate pack copy exists. Only residual cost is per-element write() calls for VariableList&lt;u8&gt; (each byte goes through a 1-byte SmallVec encoding), a CPU not an allocation cost; a bytes fast path would help large transaction/blob byte lists slightly.

**Best measured result.** 1M bytes: 7.70MB-&gt;2.77MB, 1.096ms-&gt;0.807ms (pr:prysm#17209)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/ssz_types-19f835ca387d51e3/8955d22/src/tree_hash.rs:35 hash_vec streams each item into MerkleHasher.write, no pack-into-chunks buffer
- ~/.cargo/git/checkouts/tree_hash-f96cb869d9a8a64f/e5ea187/tree_hash/src/merkle_hasher.rs:215 write() hashes full 32-byte slices in place, only a &lt;=32 byte SmallVec buffer for the tail
- ~/.cargo/git/checkouts/tree_hash-f96cb869d9a8a64f/e5ea187/tree_hash/src/impls.rs:60 [u8;N] hashes via merkle_root directly on the slice

**Sources.** [prysm#10830](https://github.com/OffchainLabs/prysm/pull/10830), [prysm#17209](https://github.com/OffchainLabs/prysm/pull/17209)

</details>


<a id="tree_hash-074"></a>
<details>
<summary><b>tree_hash-074</b> Compact leaf storage with cached leaf hash — <i>partial · low · M · cpu, memory</i></summary>

**Idea.** Store packed leaf node data as raw bytes, use a precomputed default leaf hash, and cache each leaf's hash, avoiding wrapper object and padding allocations during Merkle hashing.

**Gap in Lighthouse.** Leaf hash is cached, but the packed leaf stores typed values in a heap Vec&lt;T&gt; (plus RwLock) instead of raw bytes, and there is no shared default-leaf hash for zero/empty leaves. Milhouse PackedLeaf would need a fixed [u8;32]/inline array payload and a precomputed zero-leaf constant; insert_at_index/update clone the Vec each time.

**Impact.** Less allocation and memory per packed leaf in balances/participation/inactivity lists (millions of leaves on mainnet), cheaper tree-states clone/update; Teku saw ~68% less allocation on serialization but only a few percent on hashing, so expect a modest gain.

**Best measured result.** state serialization +11% ops/s; 68% less allocation; 2.6% less on generation (pr:teku#5208)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/packed_leaf.rs:12 PackedLeaf{hash: RwLock&lt;Hash256&gt;, values: Vec&lt;T&gt;} caches the leaf hash
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/packed_leaf.rs:28 tree_hash() returns cached hash if non-zero, else packs values into 32 bytes on the stack
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/packed_leaf.rs:60 empty()/single() allocate Vec::with_capacity(packing_factor) per leaf

**Sources.** [teku#5208](https://github.com/Consensys-Incorporated/teku/pull/5208), [teku#10387](https://github.com/Consensys-Incorporated/teku/pull/10387)

</details>


<a id="tree_hash-076"></a>
<details>
<summary><b>tree_hash-076</b> Take previous state root from pre-state — <i>implemented · low · cpu</i></summary>

**Idea.** During slot processing take the previous state root from the immutable pre-state whose root is already cached, instead of rehashing the mutable copy.

**Impact.** Only complete_state_advance later iterations and some test/builder paths rehash; hot paths already avoid it.

**Best measured result.** "only a minor improvement" (pr:teku#3973)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_slot_processing.rs:122`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_slot_processing.rs#L122) cache_state uses the supplied state_root, only update_tree_hash_cache() when None
- [`beacon_node/beacon_chain/src/block_verification.rs:1639`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1639) per_slot_processing(&amp;mut state, Some(state_root)) with parent state root
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:291`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L291) passes Some(head_state_root)
- [`consensus/state_processing/src/block_replayer.rs:233`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/block_replayer.rs#L233) passes known root from blocks

**Sources.** [teku#3973](https://github.com/Consensys-Incorporated/teku/pull/3973)

</details>


<a id="tree_hash-079"></a>
<details>
<summary><b>tree_hash-079</b> Build light client branches as one multiproof — <i>not · low · S · cpu</i></summary>

**Idea.** Compute the several Merkle branches needed for light client updates with one multi-proof (proof union) pass instead of separate per-branch proof builds.

**Gap in Lighthouse.** Add one BeaconState method returning all three branches: compute get_beacon_state_leaves() once, build the MerkleTree (or a multiproof) once, extract the three paths, and use it in LightClientCachedData::from_state. Also avoids re-hashing the 512-key sync committees three times.

**Impact.** Per imported block saves two of three state-leaf computations and tree builds (the two sync committee roots are uncached ~1k hashes each); roughly sub-millisecond to a few ms per block on the import path.

**Best measured result.** Saves ~10ms / block (pr:nimbus#8232)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:3876`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3876) compute_current_sync_committee_proof, :3892 next, :3908 finalized each call get_beacon_state_leaves() and generate_proof separately
- [`consensus/merkle_proof/src/lib.rs:69`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/merkle_proof/src/lib.rs#L69) MerkleTree::create builds a full boxed tree per proof
- [`beacon_node/beacon_chain/src/light_client_server_cache.rs:467`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_server_cache.rs#L467) LightClientCachedData::from_state calls all three; :71 runs it for every imported post-Altair block

**Sources.** [nimbus#8232](https://github.com/status-im/nimbus-eth2/pull/8232)

</details>


<a id="tree_hash-081"></a>
<details>
<summary><b>tree_hash-081</b> Collect proof siblings during merkleization — <i>not · low · S · cpu, memory</i></summary>

**Idea.** Generate SSZ Merkle proofs by collecting required sibling hashes during one merkleization sweep instead of building the whole tree and extracting proofs afterwards.

**Gap in Lighthouse.** Replace MerkleTree::create+generate_proof with a single-pass function that merkleizes the leaves while recording only the siblings of the target index (e.g. in merkle_proof crate, used by BeaconState::generate_proof and BeaconBlockBody proofs).

**Impact.** Only top-level container proofs (about 37-64 leaves, KZG and light-client) are generated, so it saves small allocations (boxed nodes) per proof; low impact on a mainnet node, mostly on blob-sidecar construction and light client.

**Best measured result.** Proof collector ~6.3x slower and 3.4x more memory than OptimizedValidatorRoots baseline; OptimizedContainerRoots ~2.3x faster than collector (pr:prysm#16177)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/merkle_proof/src/lib.rs:69`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/merkle_proof/src/lib.rs#L69),291 MerkleTree::create then generate_proof builds the whole tree and then extracts the path
- [`consensus/types/src/state/beacon_state.rs:3945`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3945) generate_proof builds tree from all top-level field roots
- [`consensus/types/src/block/beacon_block_body.rs:406`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/block/beacon_block_body.rs#L406),495 same tree-then-extract for body/kzg proofs
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/*.rs no proof API in milhouse

**Sources.** [prysm#16177](https://github.com/OffchainLabs/prysm/pull/16177)

</details>


<a id="tree_hash-084"></a>
<details>
<summary><b>tree_hash-084</b> Skip state-root history hashing for attestations — <i>implemented · low · cpu, memory</i></summary>

**Idea.** Load states for attestation verification without recomputing their state-root history and without cloning caches on intermediate states, avoiding tree hashing that dominated allocations.

**Impact.** Already in place (lighthouse#1522); attestation shuffling states skip state-root history hashing.

**Best measured result.** tree hashing was 23% of memory allocations by bytes (heaptrack) (pr:lighthouse#1522)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/state_advance.rs:73`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/state_advance.rs#L73) partial_state_advance passes zero state roots for intermediate slots, no tree hashing
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:454`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L454) uses partial_state_advance for shuffling since roots are irrelevant
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2164`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2164) committee-cache state path also partial_state_advance with known root

**Sources.** [lighthouse#1522](https://github.com/sigp/lighthouse/pull/1522)

</details>


<a id="tree_hash-085"></a>
<details>
<summary><b>tree_hash-085</b> Two-level dirty bitmap with deferred rehash — <i>implemented · medium · cpu</i></summary>

**Idea.** Track changed leaf chunks in a two-level bitmap (summary bit per 64-chunk word) and rehash once at commit over sorted maximal dirty ranges, so draining and clearing scan only touched words.

**Impact.** Already realised.

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/tree.rs:515 nodes with zero cached hash are rehashed, others skipped
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/tree.rs:186 with_updated_leaves builds new path nodes with empty hash
- [`consensus/types/src/state/beacon_state.rs:3070`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3070) update_tree_hash_cache applies updates once then hashes

**Sources.** [silver#372](https://github.com/gattaca-com/silver/pull/372)

</details>


<a id="tree_hash-086"></a>
<details>
<summary><b>tree_hash-086</b> Cache progressive list roots on the list — <i>not · low · M · cpu, latency</i></summary>

**Idea.** Cache roots of progressive SSZ lists (transactions, access lists, Gloas state lists) inside the list object, invalidated by mutators and kept across copies, and compute payload roots before taking the fork-choice lock.

**Gap in Lighthouse.** ssz_types ProgressiveVariableList (and ByteList equivalents) would need a OnceCell root cache invalidated by mutators and kept across clone; callers would then pre-warm the payload root before locking fork choice.

**Impact.** Only saves repeated re-hashing of the same Gloas payload (sub-ms to ~2 ms per hash); Lighthouse hashes payloads rarely and not under the fork-choice lock, so mainnet gain is negligible.

**Best measured result.** warm payload hash 534 us -&gt; 1.9 us (300 tx); 2.1 ms -&gt; 2 us (1500 tx) (pr:caplin#25193)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/execution/execution_payload.rs:25`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/execution/execution_payload.rs#L25) - Gloas ProgressiveTransactions is a plain ssz_types ProgressiveVariableList
- ssz_types-19f835ca387d51e3/src/progressive_variable_list.rs - no root cache field; tree_hash recomputed each call
- [`beacon_node/beacon_chain/src/payload_envelope_verification/gossip_verified_envelope.rs:124`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/gossip_verified_envelope.rs#L124) - only execution_requests hashed, uncached, no payload hash under fork-choice lock

**Sources.** [caplin#25193](https://github.com/erigontech/erigon/pull/25193), [caplin#25216](https://github.com/erigontech/erigon/pull/25216)

</details>


