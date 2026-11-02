# tree_hash

90 ideas: 14 not, 12 partial, 43 implemented, 21 n/a; 9 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [tree_hash-001](#tree_hash-001) **★** | SIMD multi-buffer SHA-256 for whole Merkle layers | not | high | L | cpu, memory |
| [tree_hash-002](#tree_hash-002) | Runtime-dispatched hardware-accelerated SHA-256 | implemented | low | S | cpu |
| [tree_hash-003](#tree_hash-003) | Batch node pairs into full AVX-512 groups | not | low | L | cpu |
| [tree_hash-004](#tree_hash-004) | Compress-only SHA-256 for 64-byte node inputs | not | low | M | cpu |
| [tree_hash-005](#tree_hash-005) | Pick the fastest hash backend per platform | implemented | low | S | cpu |
| [tree_hash-006](#tree_hash-006) | Ensure and assert the fast hasher is used everywhere | implemented | low | S | cpu, memory |
| [tree_hash-007](#tree_hash-007) | Incremental dirty-leaf Merkle cache for beacon state | partial | low | S | cpu, latency, memory |
| [tree_hash-008](#tree_hash-008) | Incremental tree hash cache for balances list | implemented | low | S | cpu |
| [tree_hash-009](#tree_hash-009) | Incremental hashing of fixed root vectors | implemented | low | S | cpu |
| [tree_hash-010](#tree_hash-010) **★** | Incremental hashing of pending queues | partial | medium | M | cpu |
| [tree_hash-011](#tree_hash-011) | Incremental cache for progressive (EIP-7916) lists | implemented | low | S | cpu, latency |
| [tree_hash-012](#tree_hash-012) | Track changed generalized indices in tree views | implemented | low | S | cpu |
| [tree_hash-013](#tree_hash-013) | Track dirty chunks as ranges | implemented | low | S | cpu, memory |
| [tree_hash-014](#tree_hash-014) | Deduplicate parent hashing of dirty leaves | implemented | low | S | cpu |
| [tree_hash-015](#tree_hash-015) | Resize tree hash cache in place | implemented | low | S | cpu |
| [tree_hash-016](#tree_hash-016) | Per-type leaf offsets for nested caches | n/a | low | S | cpu |
| [tree_hash-017](#tree_hash-017) | Dirty hash cache only on real changes | partial | low | S | cpu |
| [tree_hash-018](#tree_hash-018) | Read only dirty elements during trie recompute | implemented | low | S | cpu, memory |
| [tree_hash-019](#tree_hash-019) | Arena-backed tree hash cache with parallel registry | implemented | low | S | cpu, memory |
| [tree_hash-020](#tree_hash-020) **★** | Batch-hash dirty nodes collected at commit | not | medium | L | cpu, memory |
| [tree_hash-021](#tree_hash-021) | Run state hashing only at transitions | implemented | low | S | cpu |
| [tree_hash-022](#tree_hash-022) **★** | Bulk-build validator leaf hashes | not | medium | M | cpu, startup |
| [tree_hash-023](#tree_hash-023) | Cached child views with batched commit | implemented | low | S | cpu, latency |
| [tree_hash-024](#tree_hash-024) | Pack small basic fields into compact leaves | implemented | low | S | memory, cpu |
| [tree_hash-025](#tree_hash-025) | Packed leaves for persistent progressive lists | implemented | low | S | memory, cpu |
| [tree_hash-026](#tree_hash-026) **★** | Compute block root once, cache and pass it along | partial | medium | M | cpu, latency, sync |
| [tree_hash-027](#tree_hash-027) | Cache block body root keyed by SSZ bytes | not | low | M | cpu |
| [tree_hash-028](#tree_hash-028) | Cache execution payload field hashes | not | low | M | cpu |
| [tree_hash-029](#tree_hash-029) | Cache eth1 votes root and reuse pair buffer | implemented | low | S | cpu, memory |
| [tree_hash-030](#tree_hash-030) | Forbid accidental uncached full hashing | partial | low | M | cpu |
| [tree_hash-031](#tree_hash-031) | Generated per-type hash_tree_root instead of reflection | n/a | low | S | cpu, memory |
| [tree_hash-032](#tree_hash-032) **★** | Direct hashing of transactions list | not | medium | S | cpu, memory |
| [tree_hash-033](#tree_hash-033) | Precomputed zero-subtree hash table for padding | implemented | low | S | cpu, memory, startup |
| [tree_hash-034](#tree_hash-034) | Hash node inputs directly without concatenation | implemented | low | S | cpu, memory |
| [tree_hash-035](#tree_hash-035) | Identity fast path for 32-byte root fields | implemented | low | S | cpu |
| [tree_hash-036](#tree_hash-036) | Reusable merkleizer scratch buffers | implemented | low | S | cpu, memory |
| [tree_hash-037](#tree_hash-037) | Allocation-free Merkle proof verification | implemented | low | S | cpu |
| [tree_hash-038](#tree_hash-038) | Write length mix-in directly | implemented | low | S | cpu, memory |
| [tree_hash-039](#tree_hash-039) | Append 32-byte values directly in generated hashing | implemented | low | S | cpu, memory |
| [tree_hash-040](#tree_hash-040) | Exact-capacity preallocation of hashing buffers | implemented | low | S | cpu, memory |
| [tree_hash-041](#tree_hash-041) | Avoid zero-buffer allocation in merkleization | implemented | low | S | cpu, memory |
| [tree_hash-042](#tree_hash-042) | Hash dirty basic fields without temp nodes | implemented | low | S | cpu, memory |
| [tree_hash-043](#tree_hash-043) | Reuse hasher instances across hash calls | n/a | low | S | cpu, memory |
| [tree_hash-044](#tree_hash-044) | Skip hash state zeroing and copies | n/a | low | S | cpu |
| [tree_hash-045](#tree_hash-045) | Alignment-agnostic digest hashing | n/a | low | S | cpu |
| [tree_hash-046](#tree_hash-046) | Bounded workspace for progressive merkleization | partial | low | S | memory |
| [tree_hash-047](#tree_hash-047) | Streaming bounded-memory Merkle accumulator | implemented | low | S | cpu, memory |
| [tree_hash-048](#tree_hash-048) | Derive many Merkle proofs from one tree | n/a | medium | S | cpu |
| [tree_hash-049](#tree_hash-049) | Hash the underlying tree-backed state directly | implemented | low | S | cpu |
| [tree_hash-050](#tree_hash-050) | Return orphaned nodes to the pool | n/a | low |  | memory |
| [tree_hash-051](#tree_hash-051) | Tune hash tree page size | n/a | low |  | memory, cpu |
| [tree_hash-052](#tree_hash-052) | Upgrade SSZ library for faster hashing | n/a | low |  | cpu |
| [tree_hash-053](#tree_hash-053) | Persistent structurally shared Merkle tree for state | implemented | low | S | cpu, memory |
| [tree_hash-054](#tree_hash-054) | Store tree hash cache inside the state | implemented | high | S | cpu, memory |
| [tree_hash-055](#tree_hash-055) | Share or copy tree hash caches on state clone | implemented | high | S | cpu, memory |
| [tree_hash-056](#tree_hash-056) | Extend tree hash cache to every list field | partial | low | S | cpu, memory |
| [tree_hash-057](#tree_hash-057) | Partial top-level state root rebuild | partial | low | M | cpu, latency |
| [tree_hash-058](#tree_hash-058) | Do not schedule rebuild for uncached fields | n/a | low |  | cpu |
| [tree_hash-059](#tree_hash-059) | Full rebuild past a dirty-index threshold | n/a | medium | S | cpu, memory |
| [tree_hash-060](#tree_hash-060) | Keep balances in a separate list | implemented | low | S | cpu |
| [tree_hash-061](#tree_hash-061) **★** | Tune leaf bundle size of persistent lists | not | medium | L | cpu, memory |
| [tree_hash-062](#tree_hash-062) | Recompute state root lazily on read | implemented | medium | S | cpu |
| [tree_hash-063](#tree_hash-063) | Memoize roots in plain fields, no wrapper | n/a | low |  | cpu, memory |
| [tree_hash-064](#tree_hash-064) **★** | Persist Merkle caches to disk with states | partial | high | L | disk, latency |
| [tree_hash-065](#tree_hash-065) | Parallel hashing of large state lists | implemented | medium | S | cpu, latency, memory, startup |
| [tree_hash-066](#tree_hash-066) | Parallel workers write leaves directly to cache | n/a | low | S | cpu, memory |
| [tree_hash-067](#tree_hash-067) | Native SHA-256 backend for merkleization | implemented | low | S | cpu |
| [tree_hash-068](#tree_hash-068) | Do not rehash already-hashed leaves | implemented | low | S | cpu |
| [tree_hash-069](#tree_hash-069) | Incremental prefix roots for deposits | n/a | low | S | cpu, startup |
| [tree_hash-070](#tree_hash-070) | Lazy iterator for prefix roots | n/a | low | S | memory |
| [tree_hash-071](#tree_hash-071) | Stack or inline buffers in tree hashing | implemented | low | S | cpu, memory |
| [tree_hash-072](#tree_hash-072) **★** | Chunk byte data directly, no pack copy | partial | medium | M | cpu, memory |
| [tree_hash-073](#tree_hash-073) | Reinterpret little-endian uint arrays as chunks | not | low | S | cpu |
| [tree_hash-074](#tree_hash-074) | Compact leaf storage with cached leaf hash | partial | low | M | cpu, memory |
| [tree_hash-075](#tree_hash-075) | Reuse deposit trie root, no double hash | n/a | low | S | cpu |
| [tree_hash-076](#tree_hash-076) | Take previous state root from pre-state | implemented | low | S | cpu |
| [tree_hash-077](#tree_hash-077) | Remove superseded SSZ hash-result caches | n/a | low | S | cpu, memory |
| [tree_hash-078](#tree_hash-078) | Short lock during field trie recompute | n/a | low | S | latency |
| [tree_hash-079](#tree_hash-079) | Build light client branches as one multiproof | not | low | S | cpu |
| [tree_hash-080](#tree_hash-080) | Compute body root and sub-roots in one pass | not | low | S | cpu |
| [tree_hash-081](#tree_hash-081) | Collect proof siblings during merkleization | not | low | S | cpu, memory |
| [tree_hash-082](#tree_hash-082) | Layered deposit trie with zero hashes | n/a | low | S | cpu, memory |
| [tree_hash-083](#tree_hash-083) | Precompute leaf offsets in cache overlay | n/a | low | S | cpu |
| [tree_hash-084](#tree_hash-084) | Skip state-root history hashing for attestations | implemented | low | S | cpu, memory |
| [tree_hash-085](#tree_hash-085) | Two-level dirty bitmap with deferred rehash | partial | low | M | cpu |
| [tree_hash-086](#tree_hash-086) | Cache progressive list roots on the list | not | low | M | cpu, latency |
| [tree_hash-087](#tree_hash-087) | Self-describing cache overlays avoid old-item copy | implemented | low | S | cpu, memory |
| [tree_hash-088](#tree_hash-088) | Native fixed-width integers in hashing paths | implemented | low | S | cpu, memory |
| [tree_hash-089](#tree_hash-089) | Hash fixed-size lists as packed primitive vectors | implemented | low | S | cpu |
| [tree_hash-090](#tree_hash-090) | Promote cached hashes on state finalization | n/a | low |  | cpu, memory |

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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [caplin#6520](https://github.com/erigontech/erigon/pull/6520), [silver#49](https://github.com/gattaca-com/silver/pull/49), [nimbus#5188](https://github.com/status-im/nimbus-eth2/pull/5188), [prysm#16216](https://github.com/OffchainLabs/prysm/pull/16216), [prysm#12003](https://github.com/OffchainLabs/prysm/pull/12003), [prysm#15543](https://github.com/OffchainLabs/prysm/pull/15543), [prysm#13569](https://github.com/OffchainLabs/prysm/pull/13569), [lodestar#6977](https://github.com/ChainSafe/lodestar/pull/6977), [lodestar#8481](https://github.com/ChainSafe/lodestar/pull/8481), [prysm#15619](https://github.com/OffchainLabs/prysm/pull/15619), [prysm#10166](https://github.com/OffchainLabs/prysm/pull/10166), [prysm#11229](https://github.com/OffchainLabs/prysm/pull/11229), [prysm#10819](https://github.com/OffchainLabs/prysm/pull/10819), [prysm#11206](https://github.com/OffchainLabs/prysm/pull/11206), [prysm#12148](https://github.com/OffchainLabs/prysm/pull/12148), [prysm#10927](https://github.com/OffchainLabs/prysm/pull/10927), [prysm#10939](https://github.com/OffchainLabs/prysm/pull/10939)

</details>


<a id="tree_hash-002"></a>
<details>
<summary><b>tree_hash-002</b> Runtime-dispatched hardware-accelerated SHA-256 — <i>implemented · low · S · cpu</i></summary>

**Idea.** Use a SHA-256 implementation that detects CPU SHA extensions (SHA-NI, ARMv8 SHA) or AVX2 at runtime and dispatches to them, with a faster software fallback otherwise, for every tree-hash and shuffling digest. Hardware instructions are many times faster than a portable software implementation.

**Impact.** Already realised on tree hashing and shuffling.

**Best measured result.** state tree hashing about 30% faster, 35ms to 25ms on Prater (Ryzen 5950X) (pr:lighthouse#2426)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/registry/src/*/ethereum_hashing-0.8.0/src/lib.rs:111 cpufeatures sha/sse4.1 runtime latch
- ~/.cargo/registry/src/*/ethereum_hashing-0.8.0/src/lib.rs:124 DynamicImpl::best: sha2 (SHA-NI) if available else ring (asm, ARMv8 SHA on aarch64)
- ~/.cargo/git/checkouts/tree_hash-f96cb869d9a8a64f/e5ea187/tree_hash/src/lib.rs:68 merkleization uses ethereum_hashing::hash32_concat
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/tree.rs:545 milhouse node hashing uses hash32_concat
- [`consensus/swap_or_not_shuffle/src/shuffle_list.rs:2`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/swap_or_not_shuffle/src/shuffle_list.rs#L2) shuffling uses ethereum_hashing::hash_fixed

**Skeptic check.** Verified runtime dispatch in ethereum_hashing 0.8.0 and that tree_hash, milhouse and swap_or_not_shuffle all route through it. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

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


<a id="tree_hash-004"></a>
<details>
<summary><b>tree_hash-004</b> Compress-only SHA-256 for 64-byte node inputs — <i>not · low · M · cpu</i></summary>

**Idea.** Hash Merkle node pairs by calling the SHA-256 block compression function directly with a precomputed fixed padding block for 64-byte messages, instead of a generic buffered digest (init/update/finalize) per pair. This skips buffering and padding work for every node.

**Gap in Lighthouse.** ethereum_hashing::hash32_concat would call the block compression directly with a precomputed padding block for 64-byte input (upstream crate change, then tree_hash picks it up).

**Impact.** Merkleization hash cost per node could drop somewhat (maybe 10-30% on pair hashing) but SHA-NI already makes it cheap; state root caching limits volume.

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ethereum_hashing-0.8.0/src/lib.rs:36 hash32_concat uses a DynamicContext update/update/finalize per pair
- sha2 0.10.9 / ring used as generic digests, no compress-only path

**Sources.** [ethlambda#753](https://github.com/lambdaclass/ethlambda/pull/753)

</details>


<a id="tree_hash-005"></a>
<details>
<summary><b>tree_hash-005</b> Pick the fastest hash backend per platform — <i>implemented · low · S · cpu</i></summary>

**Idea.** Benchmark and disable SHA-256 tree-hash backends (for example arm64 assembly) that are slower or broken on a platform, falling back to the better implementation there. A wrongly chosen backend silently regresses all tree hashing on that architecture.

**Impact.** No known slow backend is selected. x86_64 uses sha2 with SHA-NI when it is present and ring otherwise; aarch64 always uses ring, which detects ARMv8 SHA2 instructions at runtime.

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ethereum_hashing-0.8.0/src/lib.rs:110-150
- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ethereum_hashing-0.8.0/Cargo.toml:30-35

**Skeptic check.** The backend is chosen at runtime per CPU. There is no benchmark-driven disable list, but none is needed unless a platform is found where ring or sha2 is slower. I did not benchmark arm64, so confidence is low.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#6278](https://github.com/status-im/nimbus-eth2/pull/6278)

</details>


<a id="tree_hash-006"></a>
<details>
<summary><b>tree_hash-006</b> Ensure and assert the fast hasher is used everywhere — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Verify at build, startup or in CI that every merkleization path (generic helpers, all library instances and branches) resolves to the fast native SHA-256 implementation, with one explicitly selected copy of the hashing dependency. A silent fallback to a slow default hasher slows merkleization and raises allocation.

**Impact.** No gain; the Lodestar failure mode (duplicate hasher packages, JS fallback) is structurally absent.

**Best measured result.** 'significantly higher GC on mainnet' (screenshot, no numbers) (pr:lodestar#9352)

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.toml:153 ethereum_hashing = "0.8.0"
- Cargo.lock one ethereum_hashing, one tree_hash, one milhouse entry
- ~/.cargo/registry/src/*/ethereum_hashing-0.8.0/src/lib.rs:124 dispatch inside the crate, no slow generic fallback
- ~/.cargo/git/checkouts/tree_hash-f96cb869d9a8a64f/e5ea187/tree_hash/src/merkle_hasher.rs:2 MerkleHasher uses ethereum_hashing Context

**Skeptic check.** Confirmed a single ethereum_hashing copy in Cargo.lock, used by tree_hash and milhouse, with dispatch built in; direct sha2 uses are only in keystores, network config and build scripts, and sha2 itself detects SHA-NI. No explicit assertion exists, but nothing needs one.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#9349](https://github.com/ChainSafe/lodestar/pull/9349), [lodestar#7387](https://github.com/ChainSafe/lodestar/pull/7387), [lodestar#5969](https://github.com/ChainSafe/lodestar/pull/5969), [lodestar#7393](https://github.com/ChainSafe/lodestar/pull/7393), [lodestar@913da071b](https://github.com/ChainSafe/lodestar/commit/913da071b23d), [lodestar#9352](https://github.com/ChainSafe/lodestar/pull/9352), [lodestar#7394](https://github.com/ChainSafe/lodestar/pull/7394), [lodestar#7621](https://github.com/ChainSafe/lodestar/pull/7621), [lodestar#7705](https://github.com/ChainSafe/lodestar/pull/7705)

</details>


<a id="tree_hash-007"></a>
<details>
<summary><b>tree_hash-007</b> Incremental dirty-leaf Merkle cache for beacon state — <i>partial · low · S · cpu, latency, memory</i></summary>

**Idea.** Keep a persistent cache of Merkle subtree hashes for the BeaconState and its large lists/vectors (validators, balances, root vectors), track dirty leaves, and on state root computation rehash only dirty leaves and their ancestors. This makes the per-slot state root O(changes * log n) instead of a full rehash.

**Gap in Lighthouse.** The milhouse lists/vectors (validators, balances, root vectors, participation, inactivity) are incremental. current_sync_committee and next_sync_committee are plain ssz_types structs behind Arc with no cached root, so every BeaconState::update_tree_hash_cache / canonical_root rehashes both: about 2 x 1025 SHA-256 compressions per state root, even though they change only once per 256 epochs. Fix: cache the root on SyncCommittee (e.g. OnceLock&lt;Hash256&gt; skipped in SSZ/eq) or keep it in a skip_hashing state field.

**Impact.** About 2k hashes (~0.5-1 ms) saved per state root computation; several state roots per slot (block import, per_slot_processing cache_state, state advance).

**Best measured result.** "5x block processing speed on ncli_db" (commit:nimbus@f1dcee2749fe)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:3070`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3070) update_tree_hash_cache applies pending updates then calls derived tree_hash_root
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/tree.rs:507 Tree::tree_hash reuses cached node hashes
- [`consensus/types/src/state/beacon_state.rs:639`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L639) current_sync_committee: Arc&lt;SyncCommittee&lt;E&gt;&gt; (not a milhouse type, no cached root)
- [`consensus/types/src/sync_committee/sync_committee.rs:34`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/sync_committee/sync_committee.rs#L34) SyncCommittee derives plain TreeHash over ssz_types FixedVector&lt;PublicKeyBytes, 512&gt;

**Skeptic check.** Milhouse caching is real and covers the large registries. The earlier check missed that the two sync committees sit outside milhouse and are rehashed in full on every state root.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [prysm#3155](https://github.com/OffchainLabs/prysm/pull/3155), [prysm#1711](https://github.com/OffchainLabs/prysm/pull/1711), [lighthouse@7b05c506d](https://github.com/sigp/lighthouse/commit/7b05c506df36), [nimbus@f1dcee274](https://github.com/status-im/nimbus-eth2/commit/f1dcee2749fe), [caplin#11096](https://github.com/erigontech/erigon/pull/11096), [prysm#4197](https://github.com/OffchainLabs/prysm/pull/4197), [lighthouse@b213a5ade](https://github.com/sigp/lighthouse/commit/b213a5ade479), [prysm#4421](https://github.com/OffchainLabs/prysm/pull/4421), [lighthouse@f65e981f6](https://github.com/sigp/lighthouse/commit/f65e981f6f12), [prysm#3076](https://github.com/OffchainLabs/prysm/pull/3076), [lighthouse@e28e97d3c](https://github.com/sigp/lighthouse/commit/e28e97d3c71c), [caplin#6264](https://github.com/erigontech/erigon/pull/6264), [prysm#6340](https://github.com/OffchainLabs/prysm/pull/6340), [prysm#5082](https://github.com/OffchainLabs/prysm/pull/5082), [prysm#4558](https://github.com/OffchainLabs/prysm/pull/4558), [prysm#6013](https://github.com/OffchainLabs/prysm/pull/6013), [silver#152](https://github.com/gattaca-com/silver/pull/152), [prysm#5398](https://github.com/OffchainLabs/prysm/pull/5398), [lighthouse#352](https://github.com/sigp/lighthouse/pull/352), [lighthouse#360](https://github.com/sigp/lighthouse/pull/360), [lighthouse#584](https://github.com/sigp/lighthouse/pull/584), [caplin#8234](https://github.com/erigontech/erigon/pull/8234), [lighthouse@56fe15625](https://github.com/sigp/lighthouse/commit/56fe15625bf3), [prysm#5117](https://github.com/OffchainLabs/prysm/pull/5117), [lighthouse@e5783d43a](https://github.com/sigp/lighthouse/commit/e5783d43a9c3), [silver#405](https://github.com/gattaca-com/silver/pull/405), [nimbus#5381](https://github.com/status-im/nimbus-eth2/pull/5381), [prysm#5118](https://github.com/OffchainLabs/prysm/pull/5118), [prysm#1929](https://github.com/OffchainLabs/prysm/pull/1929), [lighthouse@224a967cc](https://github.com/sigp/lighthouse/commit/224a967cce66), [prysm#9283](https://github.com/OffchainLabs/prysm/pull/9283), [lighthouse@0c0eebd77](https://github.com/sigp/lighthouse/commit/0c0eebd7740f), [lighthouse@d79616fee](https://github.com/sigp/lighthouse/commit/d79616fee67a), [lighthouse@35ceb92f2](https://github.com/sigp/lighthouse/commit/35ceb92f2e94), [lighthouse@acb1dd47c](https://github.com/sigp/lighthouse/commit/acb1dd47cd71), [lighthouse@e33d1d0eb](https://github.com/sigp/lighthouse/commit/e33d1d0ebb69), [lighthouse@0bdd61e56](https://github.com/sigp/lighthouse/commit/0bdd61e564f6)

</details>


<a id="tree_hash-008"></a>
<details>
<summary><b>tree_hash-008</b> Incremental tree hash cache for balances list — <i>implemented · low · S · cpu</i></summary>

**Idea.** Include the validator balances list in the incremental tree hash cache so a balance change rehashes only its chunk path. Balances change for most validators every epoch and are a large list, so full rehashing is expensive.

**Impact.** Already incremental for balances on all forks.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:554`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L554) balances: List&lt;u64&gt; (milhouse)
- [`consensus/types/src/state/beacon_state.rs:82`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L82) BalancesGloas = ProgressiveList&lt;u64&gt;
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/packed_leaf.rs:30 PackedLeaf caches its chunk hash
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/tree.rs:194 with_updated_leaves rebuilds only paths with updates
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/progressive_tree.rs:331 progressive tree also caches node hashes

**Skeptic check.** Verified in the actual git milhouse d67aabd (earlier evidence cited the registry 0.9.0 copy, which is not the one in Cargo.lock, but the mechanism is the same). Gloas ProgressiveList also caches.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#10552](https://github.com/OffchainLabs/prysm/pull/10552), [nimbus@fec01829c](https://github.com/status-im/nimbus-eth2/commit/fec01829c49a), [silver#74](https://github.com/gattaca-com/silver/pull/74), [prysm#9793](https://github.com/OffchainLabs/prysm/pull/9793), [prysm#10011](https://github.com/OffchainLabs/prysm/pull/10011)

</details>


<a id="tree_hash-009"></a>
<details>
<summary><b>tree_hash-009</b> Incremental hashing of fixed root vectors — <i>implemented · low · S · cpu</i></summary>

**Idea.** Cover the large fixed-length vectors of the state (block_roots, state_roots, randao_mixes) with the incremental hash cache, so the one entry written each slot rehashes only its branch.

**Impact.** Already in place; a single per-slot write rehashes only one branch.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:515-518`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L515-L518)
- [`consensus/types/src/state/beacon_state.rs:563`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L563)
- d67aabd/src/tree.rs:506-540

**Skeptic check.** block_roots, state_roots and randao_mixes are milhouse Vectors. Tree::tree_hash returns the cached node hash unless an update zeroed it, so a single-entry write recomputes only that path. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [silver#185](https://github.com/gattaca-com/silver/pull/185), [lighthouse@15f81c090](https://github.com/sigp/lighthouse/commit/15f81c090701)

</details>


<a id="tree_hash-010"></a>
<details>
<summary><b>tree_hash-010</b> Incremental hashing of pending queues — <i>partial · medium · M · cpu</i></summary>

**Idea.** Track the pending deposit/withdrawal/consolidation queues in the incremental hash cache so appends and pops at the front rehash only touched paths instead of the whole queue.

**Gap in Lighthouse.** The pending_deposits queue, the largest of the three, is rebuilt every epoch: process_epoch_single_pass collects iter_from(next_deposit_index) into a Vec and calls set_pending_deposits_from_iter -&gt; List::try_from_iter / ProgressiveList::try_from_iter. Every leaf (PendingDeposit container hash) and every internal node is rehashed, and structural sharing with the parent state is lost. milhouse List::pop_front reuses only subtrees of size 2^trailing_zeros(n), so an odd n keeps the cached leaves but rehashes every internal node. ProgressiveList::pop_front (Gloas/Heze, used per block for pending_partial_withdrawals and builder_pending_withdrawals, and per epoch for consolidations) rebuilds the whole tree from the iterator.

**Impact.** Per epoch, the full pending_deposits queue is rehashed: roughly 7 hashes per entry, so tens of ms when the queue holds tens of thousands of deposits, plus the lost memory sharing. In Gloas, every block also rebuilds the small withdrawal queues.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:381-390`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L381-L390)
- [`consensus/types/src/state/beacon_state.rs:2317-2333`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2317-L2333)
- d67aabd/src/list.rs:88-103
- d67aabd/src/list.rs:217-252
- d67aabd/src/utils.rs:54-65
- d67aabd/src/progressive_list.rs:195-212
- [`consensus/state_processing/src/per_block_processing/withdrawals.rs:386-396`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/withdrawals.rs#L386-L396)
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:1296`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L1296)

**Skeptic check.** The earlier evidence cited pop_front on consolidations and the milhouse hash cache, but missed two things. pending_deposits does not use pop_front: it is replaced by a freshly built list each epoch. And milhouse pop_front keeps cached hashes only for subtrees aligned to the pop count, with ProgressiveList rebuilding fully. A fix would use pop_front plus push for pending_deposits and an offset-aware front pop in milhouse.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [silver#101](https://github.com/gattaca-com/silver/pull/101)

</details>


<a id="tree_hash-011"></a>
<details>
<summary><b>tree_hash-011</b> Incremental cache for progressive (EIP-7916) lists — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Make the field tree hash cache support progressive merkleization: cache per-segment subtrees plus the right spine for progressive lists and containers (balances, validators, inactivity scores) and mark only touched chunks dirty. A changed leaf then rehashes its segment branch and spine, keeping incremental rehash after a progressive-list fork.

**Impact.** Changed leaf rehashes only its segment branch plus the spine nodes above it; already in place for all Gloas progressive state lists.

**Best measured result.** 600 balance changes + hash: 16.8-22.4 ms -&gt; 1.0 ms (41 ms -&gt; ~3.7 on node) (pr:caplin#25102)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:81-82`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L81-L82) ValidatorsGloas/BalancesGloas are ProgressiveList
- [`consensus/types/src/state/beacon_state.rs:592-806`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L592-L806) participation, inactivity_scores, pending_* and builders are ProgressiveList
- [`consensus/types/src/state/beacon_state.rs:3852-3881`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3852-L3881) apply_pending_mutations flushes Gloas/Heze progressive fields before hashing
- d67aabd/src/progressive_tree.rs:177-230 with_updated_leaves_recursive: only spine levels at or below max update index get a fresh hash, untouched left subtrees and right spines are reused
- d67aabd/src/progressive_tree.rs:331-352 ProgressiveNode caches hash, recomputes only zeroed nodes
- d67aabd/src/tree.rs:164-246 binary segment update descends only into dirty ranges
- d67aabd/src/progressive_list.rs:108-130 apply_updates single spine walk; :274-282 tree_hash_root uses cached tree

**Skeptic check.** Verified milhouse ProgressiveTree caches per-segment subtree hashes and per-spine-node hashes, and updates rebuild only the dirty segment path and spine prefix. Earlier evidence was correct; full rebuilds only happen where all values change (participation rotation) or on pop_front, which is inherent.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#25102](https://github.com/erigontech/erigon/pull/25102), [prysm#17306](https://github.com/OffchainLabs/prysm/pull/17306), [prysm#17018](https://github.com/OffchainLabs/prysm/pull/17018)

</details>


<a id="tree_hash-012"></a>
<details>
<summary><b>tree_hash-012</b> Track changed generalized indices in tree views — <i>implemented · low · S · cpu</i></summary>

**Idea.** In tree-backed state views, record the generalized indices that were modified and on commit rehash only those paths, instead of scanning or rebuilding the view.

**Impact.** Only dirty paths are rebuilt and rehashed on commit.

**Evidence (Lighthouse @ 928b61e719).**

- d67aabd/src/update_map.rs:9-35 UpdateMap records modified indices (BTreeMap/VecMap)
- d67aabd/src/tree.rs:164-246 with_updated_leaves descends only into subtrees with updates, clones the rest
- d67aabd/src/tree.rs:507-549 tree_hash recomputes only zero-hash (new) nodes
- [`consensus/types/src/state/beacon_state.rs:3070-3077`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3070-L3077) update_tree_hash_cache applies pending mutations then hashes

**Skeptic check.** Milhouse keeps the modified indices in an update map and on apply_updates rebuilds only the paths to them; new nodes get zero hash and are the only ones rehashed. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@3c53d332c](https://github.com/ChainSafe/lodestar/commit/3c53d332cc55)

</details>


<a id="tree_hash-013"></a>
<details>
<summary><b>tree_hash-013</b> Track dirty chunks as ranges — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Represent dirty leaves in the tree-hash cache as index ranges instead of individual ids, so rehash walks fewer entries and contiguous updates are processed together.

**Impact.** Sorted dirty indices are queried by range per subtree; contiguous updates share one descent. Extra range encoding would be a micro gain.

**Evidence (Lighthouse @ 928b61e719).**

- d67aabd/src/update_map.rs:80-93 for_each_range uses BTreeMap::range over sorted indices
- d67aabd/src/tree.rs:186-221 per-node left/right range existence checks with early break
- d67aabd/src/progressive_tree.rs:233-244 has_updates_in_range per spine segment

**Skeptic check.** Milhouse does not walk dirty ids one by one: each node does two O(log n) range probes on the sorted map and recurses once per dirty subtree, the same effect as range-tracked dirty chunks. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [silver#159](https://github.com/gattaca-com/silver/pull/159)

</details>


<a id="tree_hash-014"></a>
<details>
<summary><b>tree_hash-014</b> Deduplicate parent hashing of dirty leaves — <i>implemented · low · S · cpu</i></summary>

**Idea.** When propagating dirty leaves up the tree, deduplicate shared parent nodes so each ancestor is hashed once per update, not once per dirty child.

**Impact.** Each ancestor is hashed once per apply_updates.

**Evidence (Lighthouse @ 928b61e719).**

- d67aabd/src/tree.rs:186-229 one top-down descent per batch; a shared parent is rebuilt once regardless of dirty child count
- d67aabd/src/tree.rs:530-547 node hash computed once and cached in RwLock

**Skeptic check.** Batch application is top-down over the whole update set, so every ancestor node is created and hashed exactly once. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#17330](https://github.com/OffchainLabs/prysm/pull/17330)

</details>


<a id="tree_hash-015"></a>
<details>
<summary><b>tree_hash-015</b> Resize tree hash cache in place — <i>implemented · low · S · cpu</i></summary>

**Idea.** When a cached list grows or shrinks, resize the cached Merkle tree in place and reuse unchanged subtrees instead of rebuilding the cache from scratch.

**Impact.** List growth reuses all unchanged subtrees in the persistent tree; no cache rebuild.

**Evidence (Lighthouse @ 928b61e719).**

- d67aabd/src/tree.rs:225-243 growth splits Zero nodes, unchanged subtrees shared by Arc
- d67aabd/src/list.rs:217-247 List::pop_front reuses aligned internal nodes via level_iter/push_node
- d67aabd/src/progressive_tree.rs:194-201 progressive growth opens new spine levels without touching old ones
- [`consensus/types/src/state/beacon_state.rs:3070`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3070) update_tree_hash_cache

**Skeptic check.** The persistent tree makes resize a structural-sharing update; Lighthouse's own commits in this cluster are the old cache resize, now superseded. ProgressiveList::pop_front (progressive_list.rs:195-212, used by Gloas withdrawals.rs:386/396 and single_pass.rs:1296) rebuilds from scratch and drops cached element roots, but front removal shifts every leaf, which is a different issue from resizing.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@75177837d](https://github.com/sigp/lighthouse/commit/75177837d071), [lighthouse@a124042e3](https://github.com/sigp/lighthouse/commit/a124042e30ee), [lighthouse@0b186f772](https://github.com/sigp/lighthouse/commit/0b186f772fdf), [lighthouse@9bc051909](https://github.com/sigp/lighthouse/commit/9bc0519092e3), [lighthouse@da74c4ce7](https://github.com/sigp/lighthouse/commit/da74c4ce74e4), [lighthouse@42d6a3983](https://github.com/sigp/lighthouse/commit/42d6a39832d8)

</details>


<a id="tree_hash-016"></a>
<details>
<summary><b>tree_hash-016</b> Per-type leaf offsets for nested caches — <i>n/a · low · S · cpu</i></summary>

**Idea.** Let each cached-hash type report its leaf offsets within the parent cache, so a nested container updates only its own region without rebuilding siblings.

**Impact.** Design replaced: milhouse persistent tree has no flat cache needing per-type leaf offsets.

**Evidence (Lighthouse @ 928b61e719).**

- d67aabd/src/tree.rs:164 milhouse tree stores hashes in nodes, no parallel flat cache with leaf offsets
- [`consensus/types/src/state/beacon_state.rs:3070`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3070) no CachedTreeHash in current code

**Sources.** [lighthouse@40bfd5a6c](https://github.com/sigp/lighthouse/commit/40bfd5a6c742)

</details>


<a id="tree_hash-017"></a>
<details>
<summary><b>tree_hash-017</b> Dirty hash cache only on real changes — <i>partial · low · S · cpu</i></summary>

**Idea.** Access cached-hash lists and fields through read-only accessors, mark subtrees dirty only on real writes (not on every setter or mutable borrow), skip recomputing a field cache when no element changed (e.g. validators during epoch processing), and deduplicate modified indices before recomputation. Spurious dirtying forces the next state root to rehash unchanged data.

**Gap in Lighthouse.** Epoch processing is clean, but block-import attestation processing (altair::process_attestation and the Gloas variant in process_operations.rs) calls epoch_participation.get_mut(index) for every attesting index and flag before checking has_flag. milhouse get_mut copies the value into the UpdateMap, so validators whose flags are already set (redundant or overlapping aggregates) still dirty their packed participation chunk, and apply_updates rebuilds and rehashes that path. Fix: check with get() first and call get_mut only when the flag is missing.

**Impact.** Avoids rehashing participation chunks for already-flagged attesters on block import; small, since new flags dirty many chunks anyway.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:243`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L243) iter_cow over validators/balances/inactivity
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:648`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L648) inactivity score not mutated when 0
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:697`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L697) balance mutated only when delta non-zero
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:1405`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L1405) effective balance written only on change
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:274`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L274) epoch_participation.get_mut(index) before has_flag check
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:415`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L415) same pattern in the Gloas attestation path
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/update_map.rs:43 get_mut_with inserts a copy into the UpdateMap (marks dirty)

**Skeptic check.** Epoch-processing claims verified (iter_cow and change-only writes; UpdateMap dedupes indices). Earlier evidence missed the block-processing attestation path, where get_mut dirties a leaf even when nothing changes.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [nimbus#3660](https://github.com/status-im/nimbus-eth2/pull/3660), [prysm#6390](https://github.com/OffchainLabs/prysm/pull/6390), [nimbus#5286](https://github.com/status-im/nimbus-eth2/pull/5286), [prysm#5198](https://github.com/OffchainLabs/prysm/pull/5198)

</details>


<a id="tree_hash-018"></a>
<details>
<summary><b>tree_hash-018</b> Read only dirty elements during trie recompute — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** When recomputing field tries for validator-like lists, read only the dirty elements from shared storage instead of copying the whole list first, then hash them.

**Impact.** Validator rehash touches only modified elements and their ancestors; no list copy.

**Evidence (Lighthouse @ 928b61e719).**

- d67aabd/src/update_map.rs:38-55 get_mut_with copies only the touched element on write
- d67aabd/src/tree.rs:164-246 with_updated_leaves reads only the update map entries
- [`consensus/types/src/state/beacon_state.rs:3082-3085`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3082-L3085) update_validators_tree_hash_cache applies updates then hashes cached tree

**Skeptic check.** Copy-on-write per element into the update map, then rebuild of only those leaves; the list is never copied. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#13238](https://github.com/OffchainLabs/prysm/pull/13238)

</details>


<a id="tree_hash-019"></a>
<details>
<summary><b>tree_hash-019</b> Arena-backed tree hash cache with parallel registry — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Store tree hash cache nodes in one contiguous arena instead of many small heap allocations, use stack buffers while hashing, and update validator registry subtrees in parallel. This cuts memory and allocator overhead and uses multiple cores.

**Impact.** Superseded by milhouse: structural sharing for memory and parallel hashing for the registry.

**Best measured result.** memory ~8gb to ~2.6gb; ~65% faster hashing; &gt;=50% faster parallel registry (pr:lighthouse#836)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/tree.rs:17 Arc-shared persistent nodes with inline RwLock&lt;Hash256&gt;
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/tree.rs:542 rayon::join parallel subtree hashing
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/tree.rs:531 Zero(depth) uses ZERO_HASHES, no empty subtree materialised
- [`consensus/types/src/state/beacon_state.rs:542`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L542) validators is a milhouse list

**Skeptic check.** No arena, but the arena was a means to cut memory and allocations. Milhouse Arc sharing across states plus rayon-parallel hashing gives the same or better effect. Earlier verdict upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [lodestar#7608](https://github.com/ChainSafe/lodestar/pull/7608), [lodestar#7032](https://github.com/ChainSafe/lodestar/pull/7032), [lodestar#7620](https://github.com/ChainSafe/lodestar/pull/7620), [lodestar#6939](https://github.com/ChainSafe/lodestar/pull/6939), [lodestar#7171](https://github.com/ChainSafe/lodestar/pull/7171)

</details>


<a id="tree_hash-021"></a>
<details>
<summary><b>tree_hash-021</b> Run state hashing only at transitions — <i>implemented · low · S · cpu</i></summary>

**Idea.** Do the batched state hashing only after block and epoch processing, not on every hash_tree_root call, so intermediate root requests do not trigger repeated hashing work.

**Impact.** Mutations are buffered and hashed only when a root is requested; repeat requests reuse the cached milhouse hashes.

**Best measured result.** lg1k comparable; test mainnet node better (graphs only) (pr:lodestar#7030)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:3070`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3070) update_tree_hash_cache: apply_pending_mutations then hash
- [`consensus/state_processing/src/per_slot_processing.rs:125`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_slot_processing.rs#L125) cache_state computes root once per slot unless supplied
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/tree.rs:534 cached node hash returned without recomputation

**Skeptic check.** Verified the batching and lazy hashing. One caveat: repeat roots are not fully O(1), because the uncached sync committees are rehashed each time; that gap is recorded under tree_hash-007.

**Verdict history.** implemented (checked) → implemented (skeptic)

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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [prysm#12585](https://github.com/OffchainLabs/prysm/pull/12585), [silver#44](https://github.com/gattaca-com/silver/pull/44)

</details>


<a id="tree_hash-023"></a>
<details>
<summary><b>tree_hash-023</b> Cached child views with batched commit — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Make tree-backed state views cache child views and buffer writes in a map, then commit them in one batched tree rebuild that reuses unchanged subtrees, so reads are near array speed and writes do not rewrite tree paths each time.

**Impact.** Write buffering and one batched rebuild already in place.

**Best measured result.** Epoch 16384: 0.897 to 0.266 s; 32768: 1.638 to 0.452 s; block import 16384: 0.266 to 0.121 s (pr:teku#1465)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/interface.rs:68 get_mut buffers writes in UpdateMap
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/interface.rs:86 apply_updates commits the batch
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/tree.rs:155 with_updated_leaves reuses unchanged subtrees (left.clone()/right.clone())
- [`consensus/types/src/state/beacon_state.rs:3852`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3852) apply_pending_mutations

**Skeptic check.** Verified in the git milhouse checkout that is actually used. Reads are O(log n) tree walks rather than array speed, but the hot paths use iter/iter_cow and side caches, and the batched-commit effect matches teku#1465.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#1465](https://github.com/Consensys-Incorporated/teku/pull/1465)

</details>


<a id="tree_hash-024"></a>
<details>
<summary><b>tree_hash-024</b> Pack small basic fields into compact leaves — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** Store small basic fields (u64, bool) of containers such as Validator in compact leaf nodes holding only their bytes instead of a full 32-byte chunk node per field, shrinking the state tree and speeding traversal.

**Impact.** None left: the state tree has no per-field chunk nodes for validators, and basic lists are packed.

**Best measured result.** state memory down ~25%; ~34 -&gt; ~35 slots/sec (pr:teku#3032)

**Evidence (Lighthouse @ 928b61e719).**

- d67aabd/src/leaf.rs:9 Leaf holds Arc&lt;T&gt; value plus one cached hash
- d67aabd/src/tree.rs:507 tree_hash: Leaf hashes value.tree_hash_root() once and caches it, no per-field nodes
- d67aabd/src/packed_leaf.rs:30 PackedLeaf packs basic values (balances, scores, participation) into one 32-byte chunk
- [`consensus/types/src/validator/validator.rs:21`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/validator/validator.rs#L21) Validator is a plain struct with u64/bool fields stored inline

**Skeptic check.** Confirmed that milhouse stores each Validator as one Leaf with a cached root and packs basic-type lists into PackedLeaf. The earlier evidence was right, but it cited a milhouse-0.9.0 registry path; the version in use is the git checkout d67aabd.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#3032](https://github.com/Consensys-Incorporated/teku/pull/3032)

</details>


<a id="tree_hash-025"></a>
<details>
<summary><b>tree_hash-025</b> Packed leaves for persistent progressive lists — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** Store persistent progressive lists with bundled leaf chunks (several elements per leaf node), as for persistent lists, so hashing and structural sharing operate on packed chunks rather than per-element nodes.

**Impact.** Progressive lists use the same packed leaves as milhouse List (Gloas onwards).

**Evidence (Lighthouse @ 928b61e719).**

- d67aabd/src/progressive_tree.rs:58-70 capacity_at_depth multiplies by opt_packing_factor
- d67aabd/src/progressive_tree.rs:161-163 packing_depth added for segment lookups
- d67aabd/src/builder.rs:47-52 builder packs basic values into PackedLeaf
- [`consensus/types/src/state/beacon_state.rs:82`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L82),592,634 BalancesGloas, participation, inactivity_scores are packed ProgressiveLists

**Skeptic check.** ProgressiveTree segments are ordinary milhouse Trees, so basic types (balances, scores, flags) are packed like in List: parity with Lighthouse's own persistent lists, which is what the idea asks. Grandine also bundles composite elements; milhouse does not do that for List or ProgressiveList, which is a separate idea.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine@e60be4773](https://github.com/grandinetech/grandine/commit/e60be4773c0c)

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

**Verdict history.** partial (checked) → partial (refuted)

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


<a id="tree_hash-028"></a>
<details>
<summary><b>tree_hash-028</b> Cache execution payload field hashes — <i>not · low · M · cpu</i></summary>

**Idea.** Cache hashes of execution payload fields (for example transactions root) instead of recomputing them during block processing.

**Gap in Lighthouse.** Transactions root is computed at least twice per block (block root and header conversion) with no memo. Could carry a cached transactions_root (OnceCell) in ExecutionPayload, or compute once and pass into to_execution_payload_header.

**Impact.** Saves one full transactions merkleization per imported block (a few ms with the current slow per-byte path, much less once hashing is fast).

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/execution/execution_payload_header.rs:287`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/execution/execution_payload_header.rs#L287) to_execution_payload_header recomputes payload.transactions.tree_hash_root() (and withdrawals :309)
- [`consensus/state_processing/src/per_block_processing.rs:466`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing.rs#L466) process_execution_payload builds header from payload each block
- [`consensus/types/src/block/beacon_block.rs:281`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/block/beacon_block.rs#L281) block body tree_hash_root rehashes the full payload; no cache on body/payload

**Sources.** [silver#286](https://github.com/gattaca-com/silver/pull/286)

</details>


<a id="tree_hash-029"></a>
<details>
<summary><b>tree_hash-029</b> Cache eth1 votes root and reuse pair buffer — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Cache the hash roots of eth1_data and the eth1_data_votes list keyed by content, and reuse a scratch buffer in the pair hash function, so repeated state hashing does not rehash unchanged votes.

**Impact.** Unchanged votes are never rehashed; scratch buffer is moot since hash32_concat is stack based.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:529`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L529) eth1_data_votes is a milhouse List
- [`consensus/state_processing/src/per_block_processing.rs:366`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing.rs#L366) push dirties one leaf path
- d67aabd/src/tree.rs:509-528 Leaf caches its Eth1Data root; :530-547 node hashes cached

**Skeptic check.** Each vote's root is cached in its Leaf and internal nodes cache hashes, so repeated state hashing only rehashes the new vote path. The top-level eth1_data field is a 3-field struct rehashed per state root, which is negligible. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#5058](https://github.com/OffchainLabs/prysm/pull/5058)

</details>


<a id="tree_hash-030"></a>
<details>
<summary><b>tree_hash-030</b> Forbid accidental uncached full hashing — <i>partial · low · M · cpu</i></summary>

**Idea.** Make full hash_tree_root on states and blocks a compile-time or hard error where a cached root exists, so no code path silently recomputes an expensive hash.

**Gap in Lighthouse.** The state side is guarded. The block side is not: BeaconBlock/SignedBeaconBlock derive TreeHash, and canonical_root() is callable anywhere. Nothing stops a recompute when a block_root is already known (RpcBlock, the DA checker, data_column_verification.rs:1986/2166/2316, overflow_lru_cache.rs:1288). Nimbus#5852 forbids this for blocks as well as states.

**Impact.** Small: it removes accidental block re-hashes (each one about 0.1-1 ms for blocks with large payloads). Hygiene, not a hot-path win.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:298-303`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L298-L303) BeaconState top-level enum does not implement TreeHash, so callers use canonical_root/update_tree_hash_cache
- [`consensus/types/src/state/beacon_state.rs:3070-3078`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3070-L3078) update_tree_hash_cache applies pending mutations first
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/list.rs:393-395 assert no pending updates in List::tree_hash_root
- [`consensus/types/src/block/signed_beacon_block.rs:359-361`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/block/signed_beacon_block.rs#L359-L361) SignedBeaconBlock::canonical_root rehashes message every call
- [`consensus/types/src/block/beacon_block.rs:190-192`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/block/beacon_block.rs#L190-L192) BeaconBlock freely implements TreeHash
- [`beacon_node/beacon_chain/src/block_verification_types.rs:27`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification_types.rs#L27) block_root == block.canonical_root() is only a caller-contract comment

**Skeptic check.** Verified that the top-level BeaconState has no TreeHash and that milhouse asserts there are no pending updates. The earlier evidence was right for states, but it ignored blocks, which the source PR also covers and which Lighthouse leaves unguarded.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [nimbus#5852](https://github.com/status-im/nimbus-eth2/pull/5852)

</details>


<a id="tree_hash-031"></a>
<details>
<summary><b>tree_hash-031</b> Generated per-type hash_tree_root instead of reflection — <i>n/a · low · S · cpu, memory</i></summary>

**Idea.** Compute hash_tree_root for hot types (blocks, headers, beacon state, attestation data) with generated or hand-written per-type code instead of a reflection-based generic SSZ hasher, and use it on every path (gossip, signing, slasher, proposal). Static code avoids reflection and intermediate allocations.

**Impact.** Rust derive macro already generates monomorphic hash code with no reflection; the Go-specific gain does not exist.

**Best measured result.** 129ms to 50ms/op, 469708 to 160480 allocs (about 3x) (pr:prysm#4077)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/tree_hash-f96cb869d9a8a64f/e5ea187/tree_hash_derive/src/lib.rs derive generates static per-type code
- [`consensus/types/src/block/beacon_block.rs:191`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/block/beacon_block.rs#L191) uses derived tree_hash_root

**Sources.** [prysm#5219](https://github.com/OffchainLabs/prysm/pull/5219), [prysm#5704](https://github.com/OffchainLabs/prysm/pull/5704), [prysm#5742](https://github.com/OffchainLabs/prysm/pull/5742), [prysm#5739](https://github.com/OffchainLabs/prysm/pull/5739), [prysm#5743](https://github.com/OffchainLabs/prysm/pull/5743), [prysm#4860](https://github.com/OffchainLabs/prysm/pull/4860), [prysm#6501](https://github.com/OffchainLabs/prysm/pull/6501), [prysm#6760](https://github.com/OffchainLabs/prysm/pull/6760), [prysm#7115](https://github.com/OffchainLabs/prysm/pull/7115), [prysm#6616](https://github.com/OffchainLabs/prysm/pull/6616), [prysm#6119](https://github.com/OffchainLabs/prysm/pull/6119), [prysm#6136](https://github.com/OffchainLabs/prysm/pull/6136), [prysm#4077](https://github.com/OffchainLabs/prysm/pull/4077)

</details>


<a id="tree_hash-032"></a>
<details>
<summary><b>tree_hash-032</b> Direct hashing of transactions list — <i>not · medium · S · cpu, memory</i></summary>

**Idea.** Hash the execution payload transactions (list of byte lists) with a dedicated routine that merkleizes each transaction directly, avoiding the generic SSZ path and intermediate allocations.

**Gap in Lighthouse.** No byte-list fast path: add a TreeHash for VariableList&lt;u8,N&gt; (or a Transaction newtype) that calls tree_hash::merkle_root(bytes, leaves) / writes the whole slice once, plus zero-hash padding to the limit depth, avoiding per-byte packed-encoding calls and the per-transaction heap allocation of the half-node stack. Same for the progressive (EIP-7916) variant.

**Impact.** Transactions root of a 100-200 KB payload pays per-byte call overhead and roughly one allocation per transaction; a direct slice path should make it several times faster, saving low single-digit ms per block where it is computed (block root and payload-to-header).

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/ssz_types-19f835ca387d51e3/8955d22/src/variable_list.rs:223-247 VariableList&lt;T,N&gt;::tree_hash_root is a blanket impl calling vec_tree_hash_root, with no u8 specialisation
- ~/.cargo/git/checkouts/ssz_types-19f835ca387d51e3/8955d22/src/tree_hash.rs:38-60 hash_vec Basic branch calls hasher.write(&amp;item.tree_hash_packed_encoding()) once per byte
- ~/.cargo/git/checkouts/tree_hash-f96cb869d9a8a64f/e5ea187/tree_hash/src/merkle_hasher.rs:215-243 MerkleHasher::write buffers 1-byte slices into a SmallVec until 32 bytes
- ~/.cargo/git/checkouts/tree_hash-f96cb869d9a8a64f/e5ea187/tree_hash/src/merkle_hasher.rs:183-203 with_leaves allocates half_nodes with capacity depth-1 (&gt;8 for 2^30-byte tx limit, so a heap allocation)
- [`consensus/types/src/execution/execution_payload.rs:20-26`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/execution/execution_payload.rs#L20-L26) Transactions/ProgressiveTransactions are plain VariableList / ProgressiveVariableList of byte lists, no custom TreeHash
- [`consensus/types/src/execution/execution_payload_header.rs:287-378`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/execution/execution_payload_header.rs#L287-L378) header conversion recomputes payload.transactions.tree_hash_root() with no cache

**Verdict history.** not (checked) → not (refuted)

**Sources.** [prysm#10030](https://github.com/OffchainLabs/prysm/pull/10030)

</details>


<a id="tree_hash-033"></a>
<details>
<summary><b>tree_hash-033</b> Precomputed zero-subtree hash table for padding — <i>implemented · low · S · cpu, memory, startup</i></summary>

**Idea.** Precompute the zero-subtree hashes for every depth once (ideally as a compile-time global constant) and use them for padding to the list limit and for subtrees wholly past the last leaf. Padding then costs O(log n) lookups instead of hashing zero chunks, and no table is computed at runtime or threaded through calls.

**Impact.** Padding to the list limit already costs a table lookup per level. LazyLock instead of a const costs about 48 hashes once.

**Best measured result.** can be an x10 increase in performance (pr:prysm#3995)

**Evidence (Lighthouse @ 928b61e719).**

- ethereum_hashing-0.8.0/src/lib.rs:231 ZERO_HASHES LazyLock table to depth 48, computed once per process
- e5ea187/tree_hash/src/lib.rs:123 get_zero_hash static lookup
- e5ea187/tree_hash/src/merkle_hasher.rs:291 finish pads whole missing subtrees with one zero_hash per level (O(log n))
- d67aabd/src/tree.rs:531 Tree::Zero(depth) returns ZERO_HASHES[depth]

**Skeptic check.** Verified that MerkleHasher::finish and milhouse Zero nodes both use the global table for whole zero subtrees. No path computes zero hashes per call. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus@f53b55cbe](https://github.com/status-im/nimbus-eth2/commit/f53b55cbe0cc), [nimbus#1073](https://github.com/status-im/nimbus-eth2/pull/1073), [silver#51](https://github.com/gattaca-com/silver/pull/51), [lighthouse#436](https://github.com/sigp/lighthouse/pull/436), [prysm#3995](https://github.com/OffchainLabs/prysm/pull/3995), [lodestar@bade37edb](https://github.com/ChainSafe/lodestar/commit/bade37edb5a2), [silver#45](https://github.com/gattaca-com/silver/pull/45)

</details>


<a id="tree_hash-034"></a>
<details>
<summary><b>tree_hash-034</b> Hash node inputs directly without concatenation — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Combine two 32-byte child roots (and length mix-ins) by updating the digest with each input slice directly, without generic serialization, stream machinery or a concatenated temporary buffer. Node combines dominate hashing, so removing the copy and allocation per sha256 is a large win.

**Impact.** Already done on every merkleization path that Lighthouse uses.

**Best measured result.** ~50% speedup; make test 4m53s to 2m23s; fixtures test 56.9s to 25.8s (pr:nimbus#595)

**Evidence (Lighthouse @ 928b61e719).**

- ethereum_hashing-0.8.0/src/lib.rs:36 hash32_concat updates the context with each slice, no concat buffer
- e5ea187/tree_hash/src/merkle_hasher.rs:56 HalfNode feeds the left child into a live Context and the right child at finish, so there is no concat buffer
- e5ea187/tree_hash/src/lib.rs:64 mix_in_length via hash32_concat on stack arrays
- d67aabd/src/tree.rs:544 milhouse node combine via hash32_concat

**Skeptic check.** All node combines in tree_hash, milhouse and merkle_proof pass the slices directly to the SHA context. merkleize_padded and merkleize_standard use temporary buffers, but Lighthouse does not call them. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#595](https://github.com/status-im/nimbus-eth2/pull/595), [lodestar@5fcf84f4f](https://github.com/ChainSafe/lodestar/commit/5fcf84f4f693), [teku#4834](https://github.com/Consensys-Incorporated/teku/pull/4834)

</details>


<a id="tree_hash-035"></a>
<details>
<summary><b>tree_hash-035</b> Identity fast path for 32-byte root fields — <i>implemented · low · S · cpu</i></summary>

**Idea.** When a field is a 32-byte root/digest, return it as its own hash_tree_root instead of passing it through generic chunk merkleization.

**Impact.** A 32-byte root costs one 32-byte copy and no SHA. That is the same effect as an identity fast path.

**Best measured result.** ~50% speedup (commit title) (commit:nimbus@bde20436e86f)

**Evidence (Lighthouse @ 928b61e719).**

- e5ea187/tree_hash/src/impls.rs:136 FixedBytes&lt;N&gt; (Hash256) delegates to [u8; N]
- e5ea187/tree_hash/src/impls.rs:73 [u8; N] root via merkle_root(self, 1)
- e5ea187/tree_hash/src/lib.rs:36 merkle_root with leaves == 1 copies the bytes and does no hashing

**Skeptic check.** Verified that the leaves==1 branch of merkle_root returns the bytes without a MerkleHasher or a hash. The earlier evidence was right, but the line numbers were off by a few lines.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus@bde20436e](https://github.com/status-im/nimbus-eth2/commit/bde20436e86f)

</details>


<a id="tree_hash-036"></a>
<details>
<summary><b>tree_hash-036</b> Reusable merkleizer scratch buffers — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Merkleize with a reusable hasher and reusable scratch layer/chunk buffers (with room for padding) instead of allocating new buffers per layer, item or call, for example when merkleizing transaction lists.

**Impact.** There is at most one heap allocation per merkleization call. For example, each Transaction (depth 26) spills about 6 KB once. Prysm also ended at about 5 allocations per call, so the effect is the same.

**Best measured result.** 524955 B/op, 8195 allocs -&gt; 705 B/op, 5 allocs (pr:prysm#5234)

**Evidence (Lighthouse @ 928b61e719).**

- e5ea187/tree_hash/src/merkle_hasher.rs:196 with_depth: one SmallVec of depth-1 HalfNodes (inline up to 8), the only allocation per call
- e5ea187/tree_hash/src/merkle_hasher.rs:339 process_right_node folds up the stack in place, no per-layer buffers
- ssz_types-0.14.1/src/tree_hash.rs:5 vec_tree_hash_root streams items into one MerkleHasher

**Skeptic check.** Confirmed that there are no per-layer or per-hash allocations. The hasher is not reused across transactions, so each tx root allocates once, which is negligible. A separate cost is that VariableList&lt;u8&gt; writes into the hasher one byte at a time (ssz_types tree_hash.rs:14). That is CPU overhead, not scratch buffers, so it is outside this idea.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#5234](https://github.com/OffchainLabs/prysm/pull/5234), [caplin#7488](https://github.com/erigontech/erigon/pull/7488), [caplin#22518](https://github.com/erigontech/erigon/pull/22518)

</details>


<a id="tree_hash-037"></a>
<details>
<summary><b>tree_hash-037</b> Allocation-free Merkle proof verification — <i>implemented · low · S · cpu</i></summary>

**Idea.** In Merkle branch verification, hash into fixed stack buffers and use the index bit only to order the two inputs, avoiding a heap allocation per level.

**Impact.** Done in #8614. Every gossip and block path that checks a Merkle branch uses the allocation-free function.

**Best measured result.** 33% faster, about 1.2us saved at depth 32 (pr:lighthouse#8614)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/merkle_proof/src/lib.rs:382`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/merkle_proof/src/lib.rs#L382) merkle_root_from_branch orders the slices by ith_bit and calls hash32_concat on [u8;32], no heap
- [`consensus/types/src/data/data_column_sidecar.rs:288`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/data/data_column_sidecar.rs#L288) data column inclusion proof uses verify_merkle_proof
- [`consensus/types/src/data/blob_sidecar.rs:223`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/data/blob_sidecar.rs#L223) blob inclusion proof uses the same function
- [`consensus/state_processing/src/per_block_processing/verify_deposit.rs:62`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/verify_deposit.rs#L62) deposit proof uses the same function

**Skeptic check.** Checked all callers of branch verification. They all go through merkle_proof::merkle_root_from_branch, and I found no second verifier that allocates. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#8614](https://github.com/sigp/lighthouse/pull/8614)

</details>


<a id="tree_hash-038"></a>
<details>
<summary><b>tree_hash-038</b> Write length mix-in directly — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** When mixing a list length into a root, write the length as little-endian u64 straight into a 32-byte chunk instead of using a buffered writer and copy.

**Impact.** Already minimal.

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/tree_hash-f96cb869d9a8a64f/e5ea187/tree_hash/src/lib.rs:62-72 mix_in_length writes the LE length into a stack [u8;32] and calls hash32_concat

**Skeptic check.** Confirmed: mix_in_length uses a stack chunk and has no buffered writer. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#8875](https://github.com/OffchainLabs/prysm/pull/8875)

</details>


<a id="tree_hash-039"></a>
<details>
<summary><b>tree_hash-039</b> Append 32-byte values directly in generated hashing — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** In generated hash_tree_root code, append 32-byte fields with a dedicated fixed-size append instead of a generic put-bytes path that copies and pads.

**Impact.** Already copy-free for 32-byte field roots.

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/tree_hash-f96cb869d9a8a64f/e5ea187/tree_hash/src/merkle_hasher.rs:206-215 write() passes a full 32-byte slice straight to process_leaf when the buffer is empty
- ~/.cargo/git/checkouts/tree_hash-f96cb869d9a8a64f/e5ea187/tree_hash_derive/src/lib.rs:230-237 the derive writes each field root slice into MerkleHasher

**Skeptic check.** Confirmed: derived container hashing writes 32-byte roots and takes the direct process_leaf path, with no copy or padding. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#16710](https://github.com/OffchainLabs/prysm/pull/16710)

</details>


<a id="tree_hash-040"></a>
<details>
<summary><b>tree_hash-040</b> Exact-capacity preallocation of hashing buffers — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Allocate leaf, input and output buffers in tree hashing and field tries at their known final capacity (from the actual field or element count) in one allocation instead of a hard-coded guess or growing and copying them.

**Impact.** Nothing left to gain. Containers do not build a leaf buffer at all.

**Best measured result.** Body construction 11543 -&gt; 1727 ns/op, 309 -&gt; 1 allocs; full 11.70ms -&gt; 10.93ms (pr:prysm#182)

**Evidence (Lighthouse @ 928b61e719).**

- e5ea187/tree_hash_derive/src/lib.rs:140 containers use MerkleHasher::with_leaves(field count) and stream the field roots, no leaf buffer
- e5ea187/tree_hash/src/merkle_hasher.rs:200 half_nodes with_capacity(depth-1), the exact final size
- e5ea187/tree_hash/src/impls.rs:177 bitfields with_leaves(leaf_count)
- d67aabd/src/packed_leaf.rs:53 PackedLeaf values with_capacity(packing factor)

**Skeptic check.** The derive streams field roots into a hasher sized from the field count, and the hasher's stack is pre-sized to the exact depth. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@bf1a93f44](https://github.com/sigp/lighthouse/commit/bf1a93f44422), [prysm#6722](https://github.com/OffchainLabs/prysm/pull/6722), [prysm#9977](https://github.com/OffchainLabs/prysm/pull/9977), [prysm#182](https://github.com/OffchainLabs/prysm/pull/182)

</details>


<a id="tree_hash-041"></a>
<details>
<summary><b>tree_hash-041</b> Avoid zero-buffer allocation in merkleization — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Return raw byte arrays from hash routines and let branch nodes read leaf data directly, so zero leaves use precomputed hashes without allocating zero-byte buffers.

**Impact.** Zero subtrees use precomputed static hashes with no allocation.

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/tree_hash-f96cb869d9a8a64f/e5ea187/tree_hash/src/merkle_hasher.rs:29-40 Preimage enum borrows a slice or holds a stack digest
- ~/.cargo/git/checkouts/tree_hash-f96cb869d9a8a64f/e5ea187/tree_hash/src/merkle_hasher.rs:355-357 zero_hash returns a slice of the static ZERO_HASHES
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/tree.rs:530 Tree::Zero uses ZERO_HASHES[depth]

**Skeptic check.** Confirmed in both MerkleHasher and the milhouse Tree::Zero. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#5368](https://github.com/Consensys-Incorporated/teku/pull/5368)

</details>


<a id="tree_hash-042"></a>
<details>
<summary><b>tree_hash-042</b> Hash dirty basic fields without temp nodes — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** For a dirty basic (uint/bool) field in a tree-backed container, hash the value straight into the field-root cache instead of building and freeing a temporary tree node.

**Impact.** No temporary node exists. Basic values go straight into a stack chunk or the cached leaf hash.

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/packed_leaf.rs:30-49 dirty packed basic values are encoded straight into the leaf's hash buffer
- ~/.cargo/git/checkouts/tree_hash-f96cb869d9a8a64f/e5ea187/tree_hash/src/impls.rs:7-11 int_to_hash256 builds a stack chunk for top-level uint fields

**Skeptic check.** Confirmed: top-level basic fields hash into a stack Hash256, and packed list leaves write their LE encoding in place. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@a8594031c](https://github.com/ChainSafe/lodestar/commit/a8594031c141)

</details>


<a id="tree_hash-043"></a>
<details>
<summary><b>tree_hash-043</b> Reuse hasher instances across hash calls — <i>n/a · low · S · cpu, memory</i></summary>

**Idea.** Reuse SHA-256 hasher/digest objects (pooled, thread-local fetched once, or passed through the recursion and hashing loops) instead of instantiating or looking one up per hash call, cutting allocation and setup cost.

**Impact.** Rust sha2 context is a stack value with no pool or thread-local lookup, so there is no per-call setup to remove.

**Best measured result.** sha256 1097-&gt;513 ns/op, 4-&gt;2 allocs; keccak 3352-&gt;2536 ns/op (pr:prysm#4710)

**Evidence (Lighthouse @ 928b61e719).**

- ethereum_hashing-0.8.0/src/lib.rs:149-186 DynamicContext is a stack value; best() reads a cached cpufeatures flag
- sha2_impl.rs:7-30 sha2::Sha256 stack context

**Sources.** [teku#7157](https://github.com/Consensys-Incorporated/teku/pull/7157), [prysm#4710](https://github.com/OffchainLabs/prysm/pull/4710), [teku#5268](https://github.com/Consensys-Incorporated/teku/pull/5268), [prysm#5244](https://github.com/OffchainLabs/prysm/pull/5244), [prysm#5239](https://github.com/OffchainLabs/prysm/pull/5239), [teku#7475](https://github.com/Consensys-Incorporated/teku/pull/7475), [teku#6991](https://github.com/Consensys-Incorporated/teku/pull/6991)

</details>


<a id="tree_hash-044"></a>
<details>
<summary><b>tree_hash-044</b> Skip hash state zeroing and copies — <i>n/a · low · S · cpu</i></summary>

**Idea.** In the digest helper, skip zeroing the hash state after use and the extra memcpy when producing the digest.

**Impact.** Hash state handling lives inside the sha2 crate (Rust moves the context into finalize); Lighthouse has no own digest helper.

**Evidence (Lighthouse @ 928b61e719).**

- ethereum_hashing-0.8.0/src/sha2_impl.rs:12-22 delegates to sha2 crate finalize

**Sources.** [nimbus#222](https://github.com/status-im/nimbus-eth2/pull/222), [nimbus@3117a4481](https://github.com/status-im/nimbus-eth2/commit/3117a4481ef9)

</details>


<a id="tree_hash-045"></a>
<details>
<summary><b>tree_hash-045</b> Alignment-agnostic digest hashing — <i>n/a · low · S · cpu</i></summary>

**Idea.** Make the digest routine accept unaligned input and align key/root types so the hasher can use wide or vectorized loads without copying into aligned buffers.

**Impact.** sha2 asm/intrinsics use unaligned loads and take byte slices; no aligned copy buffers exist.

**Evidence (Lighthouse @ 928b61e719).**

- ethereum_hashing-0.8.0/src/sha2_impl.rs:30-37 hashes &amp;[u8] directly with sha2 SHA-NI path (unaligned loads)

**Sources.** [nimbus#5296](https://github.com/status-im/nimbus-eth2/pull/5296)

</details>


<a id="tree_hash-046"></a>
<details>
<summary><b>tree_hash-046</b> Bounded workspace for progressive merkleization — <i>partial · low · S · memory</i></summary>

**Idea.** In progressive (EIP-7916) merkleization, fold subtree roots along the right spine with a fixed-size array bounded by maximum depth, instead of heap-allocated subtree storage and a padded final-subtree buffer.

**Gap in Lighthouse.** ProgressiveMerkleHasher::completed_roots could be a fixed array bounded by max spine depth (about 64) instead of Vec; small heap allocation per hash.

**Impact.** Streaming already avoids padded buffers; only a tiny Vec allocation per progressive hash remains, and progressive types are rare (Gloas withdrawals, bit lists).

**Evidence (Lighthouse @ 928b61e719).**

- e5ea187/tree_hash/src/progressive_merkle_hasher.rs:56-71 ProgressiveMerkleHasher keeps completed_roots: Vec&lt;Hash256&gt; and SmallVec buffer
- progressive_merkle_hasher.rs:163-200 finish builds root from completed_roots
- d67aabd/src/progressive_tree.rs:331-352 progressive tree_hash is cached recursion

**Sources.** [lodestar@52a973612](https://github.com/ChainSafe/lodestar/commit/52a97361212e), [lodestar@c243df8df](https://github.com/ChainSafe/lodestar/commit/c243df8df330)

</details>


<a id="tree_hash-047"></a>
<details>
<summary><b>tree_hash-047</b> Streaming bounded-memory Merkle accumulator — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Merkleize large lists and vectors by streaming chunks or child roots into a log-depth stack of partial hashes (a streaming MerkleHasher) instead of allocating a chunk array proportional to the input, and return fixed 32-byte roots instead of heap vectors. Workspace stays constant.

**Impact.** Done in #861. Workspace is O(log n) and roots are fixed 32-byte values.

**Evidence (Lighthouse @ 928b61e719).**

- e5ea187/tree_hash/src/merkle_hasher.rs:141 half_nodes log-depth stack of partial hashes
- e5ea187/tree_hash/src/merkle_hasher.rs:283 finish returns a fixed Hash256
- ssz_types-0.14.1/src/tree_hash.rs:25 lists and vectors stream child roots into MerkleHasher
- e5ea187/tree_hash/src/lib.rs:136 TreeHash::tree_hash_root returns Hash256

**Skeptic check.** Verified the streaming accumulator, and that ssz_types and the derive use it. The chunk-array merkleizers (merkleize_padded and merkleize_standard) exist but Lighthouse does not call them. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@0d0498823](https://github.com/ChainSafe/lodestar/commit/0d04988234a1), [lodestar@3da79f3ef](https://github.com/ChainSafe/lodestar/commit/3da79f3ef34a), [nimbus@3ecb19763](https://github.com/status-im/nimbus-eth2/commit/3ecb197635be), [lodestar@1ceb7ca7d](https://github.com/ChainSafe/lodestar/commit/1ceb7ca7d14e), [lighthouse#861](https://github.com/sigp/lighthouse/pull/861), [lodestar#672](https://github.com/ChainSafe/lodestar/pull/672)

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


<a id="tree_hash-049"></a>
<details>
<summary><b>tree_hash-049</b> Hash the underlying tree-backed state directly — <i>implemented · low · S · cpu</i></summary>

**Idea.** Compute the state root on the plain tree-backed state object, not through a wrapper or proxy with separate caches, so the cached tree nodes are hashed directly.

**Impact.** No wrapper or proxy cache layer exists.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:3070-3078`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3070-L3078) update_tree_hash_cache calls inner.tree_hash_root() on the variant struct, whose fields are milhouse lists with cached nodes

**Skeptic check.** Confirmed: the state root is computed directly on the per-fork struct, and the milhouse fields carry their own caches. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#2025](https://github.com/ChainSafe/lodestar/pull/2025), [lodestar@664a626a9](https://github.com/ChainSafe/lodestar/commit/664a626a9349)

</details>


<a id="tree_hash-050"></a>
<details>
<summary><b>tree_hash-050</b> Return orphaned nodes to the pool — <i>n/a · low · memory</i></summary>

**Idea.** In bulk tree node updates, return orphaned intermediate nodes to the node pool and clean up on failure, so the pool does not leak.

**Impact.** Milhouse uses Arc&lt;Tree&gt; with ordinary allocation; there is no node pool to leak from, so nothing to return.

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/tree.rs:15 Tree enum of Arc nodes, no node pool

**Sources.** [lodestar@76cde3c7e](https://github.com/ChainSafe/lodestar/commit/76cde3c7ea23)

</details>


<a id="tree_hash-051"></a>
<details>
<summary><b>tree_hash-051</b> Tune hash tree page size — <i>n/a · low · memory, cpu</i></summary>

**Idea.** Choose the page size of hash-tree node storage to fit the node layout, so copy-on-write snapshots copy and rehash less data.

**Impact.** Milhouse is a plain binary Merkle tree with no configurable page size; packing is dictated by the 32-byte SSZ chunk (4 u64 per leaf).

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/tree.rs:15 binary tree with Leaf/PackedLeaf nodes, no pages
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/packed_leaf.rs packing factor fixed by SSZ chunk size

**Sources.** [silver#183](https://github.com/gattaca-com/silver/pull/183)

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
<summary><b>tree_hash-053</b> Persistent structurally shared Merkle tree for state — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Back the BeaconState with a persistent (copy-on-write) binary Merkle tree whose nodes cache their hashes, so a mutation clones only the path to the touched leaf and states across slots/forks share untouched subtrees. Rehashing and state copies then touch only changed paths.

**Impact.** Core design of Lighthouse BeaconState; nothing left to gain.

**Best measured result.** Block import 16384 validators 0.266 s to ~0.19 s class (32768: 2.497 s to 0.387 s); epoch 32768 2.859 s to 1.638 s (pr:teku#1133)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:11`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L11) milhouse List/Vector/ProgressiveList imports
- [`consensus/types/src/state/beacon_state.rs:516`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L516) block_roots milhouse Vector
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/tree.rs:17 Node{hash: RwLock&lt;Hash256&gt;, left/right: Arc}
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/tree.rs:29 Clone shares Arc children
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/tree.rs:534 cached hash returned when non-zero

**Skeptic check.** Verified milhouse nodes are Arc-shared with cached RwLock hashes and every large state field is a milhouse type. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#1133](https://github.com/Consensys-Incorporated/teku/pull/1133), [lodestar@2a4c9cb62](https://github.com/ChainSafe/lodestar/commit/2a4c9cb62f21), [silver#42](https://github.com/gattaca-com/silver/pull/42), [silver#50](https://github.com/gattaca-com/silver/pull/50)

</details>


<a id="tree_hash-054"></a>
<details>
<summary><b>tree_hash-054</b> Store tree hash cache inside the state — <i>implemented · high · S · cpu, memory</i></summary>

**Idea.** Store the tree hash cache as owned data inside the BeaconState so it persists across slots and is updated in place, letting each state root reuse prior hashing work rather than rebuilding the cache.

**Impact.** Each slot rehashes only dirty paths, because the cache lives in the state's trees.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:3070-3078`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3070-L3078) update_tree_hash_cache hashes in place
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/tree.rs:507-550 Tree::tree_hash reuses the cached RwLock&lt;Hash256&gt; per node and recomputes only zeroed (dirty) nodes
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/leaf.rs:9-15 Leaf caches its hash

**Skeptic check.** Confirmed: milhouse persistent trees hold per-node hash caches inside the state. This replaces the older owned TreeHashCache from the cited Lighthouse commits, with the same effect.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@b05787207](https://github.com/sigp/lighthouse/commit/b05787207fb6), [lighthouse@6c9be1a73](https://github.com/sigp/lighthouse/commit/6c9be1a73c41)

</details>


<a id="tree_hash-055"></a>
<details>
<summary><b>tree_hash-055</b> Share or copy tree hash caches on state clone — <i>implemented · high · S · cpu, memory</i></summary>

**Idea.** When cloning a state, carry over (share or copy) the existing Merkle layer caches, and only when they exist, so the copy does not rebuild or rehash its caches from scratch.

**Impact.** A cloned state shares subtrees and their cached hashes, so there is no rebuild or rehash.

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/tree.rs:29-41 Tree::clone copies the cached hash and shares children by Arc
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/leaf.rs:17-27 Leaf clone copies the hash and shares the value Arc

**Skeptic check.** Confirmed: structural sharing in milhouse carries the caches across a clone. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#4689](https://github.com/OffchainLabs/prysm/pull/4689), [prysm#4735](https://github.com/OffchainLabs/prysm/pull/4735)

</details>


<a id="tree_hash-056"></a>
<details>
<summary><b>tree_hash-056</b> Extend tree hash cache to every list field — <i>partial · low · S · cpu, memory</i></summary>

**Idea.** Give each large or frequently changing state field its own incremental tree hash cache (participation flags, inactivity scores, eth1 data votes, randao mixes, slashings, remaining fields), so no field is fully rehashed on each state root.

**Gap in Lighthouse.** current_sync_committee and next_sync_committee are plain ssz_types FixedVector inside Arc&lt;SyncCommittee&gt;; BeaconState::update_tree_hash_cache rehashes both (~2x1025 SHA256 compressions) on every state root. Cache the root in SyncCommittee (OnceLock&lt;Hash256&gt;, the Arc is immutable) or make pubkeys a milhouse Vector. Smaller uncached fields (latest_execution_payload_header, execution_payload_availability BitVector) also rehash, but are tiny.

**Impact.** ~2k hashes (~0.2-0.5 ms) per state root computation; low because state roots are computed about once or twice per slot.

**Best measured result.** proposer index recompute potentially 128ms on large networks (pr:lighthouse#2459)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:529`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L529) eth1_data_votes milhouse List
- [`consensus/types/src/state/beacon_state.rs:627`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L627) inactivity_scores milhouse List
- [`consensus/types/src/state/beacon_state.rs:639`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L639) current_sync_committee: Arc&lt;SyncCommittee&lt;E&gt;&gt; (no cache)
- [`consensus/types/src/state/beacon_state.rs:642`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L642) next_sync_committee: Arc&lt;SyncCommittee&lt;E&gt;&gt; (no cache)
- [`consensus/types/src/sync_committee/sync_committee.rs:38`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/sync_committee/sync_committee.rs#L38) pubkeys: ssz_types FixedVector&lt;PublicKeyBytes, 512&gt;
- ~/.cargo/git/checkouts/tree_hash-f96cb869d9a8a64f/e5ea187/tree_hash/src/impls.rs:155 TreeHash for Arc&lt;T&gt; delegates, no memo
- [`consensus/types/src/state/beacon_state.rs:3070`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3070) update_tree_hash_cache calls inner.tree_hash_root() over all fields

**Skeptic check.** All list/vector fields are milhouse with cached subtrees, as the earlier evidence said, but the two sync committees (which silver#187 also migrated) are uncached and fully rehashed each time.

**Verdict history.** implemented (checked) → partial (skeptic)

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


<a id="tree_hash-058"></a>
<details>
<summary><b>tree_hash-058</b> Do not schedule rebuild for uncached fields — <i>n/a · low · cpu</i></summary>

**Idea.** Only flag a field for tree-hash cache rebuild when the field actually has an underlying cache/trie, so state mutation does not schedule useless rebuild work.

**Impact.** No per-field rebuild flag exists; unchanged lists have no pending updates and their roots are cached in the tree, so no useless work is scheduled.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:3852`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3852) apply_pending_mutations only flushes lists with pending updates
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/interface.rs:86 apply_updates

**Sources.** [prysm#14906](https://github.com/OffchainLabs/prysm/pull/14906)

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


<a id="tree_hash-060"></a>
<details>
<summary><b>tree_hash-060</b> Keep balances in a separate list — <i>implemented · low · S · cpu</i></summary>

**Idea.** Store validator balances as a separate contiguous state list instead of inside validator records, so frequent balance updates dirty only the cheap balances tree and not validator subtrees.

**Impact.** Balances are a separate packed list (spec-mandated); balance updates dirty only the balances tree.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:542`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L542) validators list
- [`consensus/types/src/state/beacon_state.rs:554`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L554) balances: List&lt;u64&gt; separate field (BalancesGloas for Gloas/Heze)

**Skeptic check.** Verified balances and validators are distinct state fields in every fork variant. The earlier evidence was right; this is the spec layout.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#1139](https://github.com/OffchainLabs/prysm/pull/1139)

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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [grandine@4ff6dcaf4](https://github.com/grandinetech/grandine/commit/4ff6dcaf444e), [lodestar#346](https://github.com/ChainSafe/lodestar/pull/346)

</details>


<a id="tree_hash-062"></a>
<details>
<summary><b>tree_hash-062</b> Recompute state root lazily on read — <i>implemented · medium · S · cpu</i></summary>

**Idea.** Mark fields dirty on write and recompute the state hash tree root only when it is read, so repeated mutations during the state transition do not each trigger rehashing.

**Impact.** Writes are buffered and node hashes are cached per subtree; the root is recomputed only on request and only for dirty subtrees.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:3069-3077`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3069-L3077) update_tree_hash_cache applies pending mutations then hashes once
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/list.rs:393 tree_hash_root requires applied updates; writes buffered in UpdateMap
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/interface.rs:86 apply_updates

**Skeptic check.** Verified the update_tree_hash_cache path applies batched milhouse updates and hashes once on read. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#4627](https://github.com/OffchainLabs/prysm/pull/4627)

</details>


<a id="tree_hash-063"></a>
<details>
<summary><b>tree_hash-063</b> Memoize roots in plain fields, no wrapper — <i>n/a · low · cpu, memory</i></summary>

**Idea.** Cache lazily computed hash roots directly in a plain (volatile/once) field of the SSZ object instead of a memoizing wrapper object, removing a per-object allocation.

**Impact.** Rust stores the cached root inline in the node struct; there is no memoizing wrapper allocation.

**Best measured result.** profiled on 300 mainnet blocks; graphs only, no numbers (pr:teku#5253)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/leaf.rs:12 hash stored inline in the Leaf, no wrapper object
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/tree.rs:19 hash inline in Node

**Sources.** [teku#5253](https://github.com/Consensys-Incorporated/teku/pull/5253)

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

**Verdict history.** not (checked) → partial (refuted)

**Sources.** [caplin#11554](https://github.com/erigontech/erigon/pull/11554)

</details>


<a id="tree_hash-065"></a>
<details>
<summary><b>tree_hash-065</b> Parallel hashing of large state lists — <i>implemented · medium · S · cpu, latency, memory, startup</i></summary>

**Idea.** Split the hashing of large lists (validator registry, balances, wide Merkle layers) across worker threads, each with its own scratch buffers and no shared locks in the inner loop, especially for cold full-tree builds.

**Impact.** Cold and incremental state hashing of validators/balances is already parallel via rayon work-stealing.

**Best measured result.** cold HashSSZ 395-457 ms -&gt; 66-96 ms; Hoodi cold hash 3.89 s -&gt; 0.53 s wall (8 workers) (pr:caplin#25101)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/tree.rs:542 rayon::join(left.tree_hash, right.tree_hash) for every un-hashed Node
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/progressive_tree.rs:344 same for progressive lists
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/tree.rs:534 lock only read once per node, not held in inner loop

**Skeptic check.** Verified recursive rayon::join over the milhouse tree; locks are per node and dropped before recursion. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#25101](https://github.com/erigontech/erigon/pull/25101), [prysm#17317](https://github.com/OffchainLabs/prysm/pull/17317), [prysm#12637](https://github.com/OffchainLabs/prysm/pull/12637), [caplin#6854](https://github.com/erigontech/erigon/pull/6854), [prysm#12639](https://github.com/OffchainLabs/prysm/pull/12639)

</details>


<a id="tree_hash-066"></a>
<details>
<summary><b>tree_hash-066</b> Parallel workers write leaves directly to cache — <i>n/a · low · S · cpu, memory</i></summary>

**Idea.** In parallel tree-hash workers, write each recomputed leaf hash straight into the cache buffer instead of collecting results in a concurrent map and copying them back.

**Gap in Lighthouse.** Milhouse is a persistent tree with per-node cached hashes; parallel halves return their hash into the node, with no side map to copy back.

**Impact.** None; idea does not apply.

**Evidence (Lighthouse @ 928b61e719).**

- milhouse-0.9.0/src/tree.rs:530 rayon::join left/right tree_hash, results stored in per-node cached hash

**Sources.** [caplin#11587](https://github.com/erigontech/erigon/pull/11587)

</details>


<a id="tree_hash-067"></a>
<details>
<summary><b>tree_hash-067</b> Native SHA-256 backend for merkleization — <i>implemented · low · S · cpu</i></summary>

**Idea.** Use a native compiled SHA-256 implementation with a reusable context for hash-tree-root instead of a slower pure-language implementation, since SHA-256 dominates merkleization cost.

**Impact.** Native SHA-256 (ring, or sha2 with SHA-NI) with reusable context; the idea is a JS-specific fix.

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/registry/src/*/ethereum_hashing-0.8.0/src/lib.rs:7-15 wrapper over sha2 and ring with DynamicContext
- ~/.cargo/registry/src/*/ethereum_hashing-0.8.0/src/lib.rs:61-68 ring::digest::Context backend
- ~/.cargo/registry/src/*/ethereum_hashing-0.8.0/Cargo.toml:31-35 default features ring + zero_hash_cache
- Cargo.lock:3810 ethereum_hashing 0.8.0

**Skeptic check.** Verified ethereum_hashing 0.8.0 uses native ring/sha2 backends with a context type. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@8810df498](https://github.com/ChainSafe/lodestar/commit/8810df4983bb)

</details>


<a id="tree_hash-068"></a>
<details>
<summary><b>tree_hash-068</b> Do not rehash already-hashed leaves — <i>implemented · low · S · cpu</i></summary>

**Idea.** When merkleizing leaves that are already 32-byte roots, start at the first internal layer instead of hashing the leaves again, and avoid any extra hashing round on outputs.

**Impact.** No redundant leaf hashing.

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/tree_hash-f96cb869d9a8a64f/e5ea187/tree_hash/src/merkle_hasher.rs:215 write() passes full 32-byte slices to process_leaf without hashing them
- ~/.cargo/git/checkouts/tree_hash-f96cb869d9a8a64f/e5ea187/tree_hash/src/lib.rs:29 merkle_root 1-leaf returns bytes, 2-leaf single hash_fixed
- ~/.cargo/git/checkouts/ssz_types-19f835ca387d51e3/8955d22/src/tree_hash.rs:50 container/list items write item.tree_hash_root() as the leaf
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/tree.rs:515 Leaf caches value.tree_hash_root(); Hash256 root is itself

**Skeptic check.** Confirmed child roots enter as leaves and are only hashed in pairs. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#42](https://github.com/status-im/nimbus-eth2/pull/42), [lodestar@069107aa0](https://github.com/ChainSafe/lodestar/commit/069107aa0253), [prysm#1653](https://github.com/OffchainLabs/prysm/pull/1653)

</details>


<a id="tree_hash-069"></a>
<details>
<summary><b>tree_hash-069</b> Incremental prefix roots for deposits — <i>n/a · low · S · cpu, startup</i></summary>

**Idea.** Compute successive list roots (e.g. deposit roots after each deposit) by feeding leaves into one running merkleizer and emitting the root after each element, instead of rehashing the growing list each time (O(n^2) to O(n)).

**Gap in Lighthouse.** Lighthouse has no eth1 deposit cache in the beacon node any more; the only user is genesis building, which already pushes leaves incrementally.

**Impact.** None; idea does not apply.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/common/deposit_data_tree.rs:36-41`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/deposit_data_tree.rs#L36-L41) push_leaf is incremental via MerkleTree
- [`consensus/state_processing/src/genesis.rs:37-44`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/genesis.rs#L37-L44) root after each push

**Sources.** [nimbus@fa2a703a1](https://github.com/status-im/nimbus-eth2/commit/fa2a703a173e)

</details>


<a id="tree_hash-070"></a>
<details>
<summary><b>tree_hash-070</b> Lazy iterator for prefix roots — <i>n/a · low · S · memory</i></summary>

**Idea.** Yield prefix (running) Merkle roots one at a time from an iterator instead of materializing the full sequence of n digests.

**Gap in Lighthouse.** No deposit prefix-root sequence exists in the node; only genesis (rare) computes running roots.

**Impact.** None; idea does not apply.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/genesis.rs:37-44`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/genesis.rs#L37-L44) only deposit-root loop; no prefix-root sequence materialized

**Sources.** [nimbus@b82328b14](https://github.com/status-im/nimbus-eth2/commit/b82328b1486a)

</details>


<a id="tree_hash-071"></a>
<details>
<summary><b>tree_hash-071</b> Stack or inline buffers in tree hashing — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Use fixed-size stack or inline small-vector buffers (32-byte arrays) for packed leaf encoding, length mix-in and leaf scratch instead of heap-allocated vectors per call or element.

**Impact.** Already done (lighthouse#3581).

**Best measured result.** block root 10-11ms to 8-9ms (pr:lighthouse#3581)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/tree_hash-f96cb869d9a8a64f/e5ea187/tree_hash/src/lib.rs:24 PackedEncoding = SmallVec&lt;[u8; 32]&gt;
- ~/.cargo/git/checkouts/tree_hash-f96cb869d9a8a64f/e5ea187/tree_hash/src/merkle_hasher.rs:141 half_nodes SmallVec8, buffer SmallVec&lt;[u8;32]&gt;
- ~/.cargo/git/checkouts/tree_hash-f96cb869d9a8a64f/e5ea187/tree_hash/src/lib.rs:62 mix_in_length uses stack [0;32] and hash32_concat
- ~/.cargo/git/checkouts/tree_hash-f96cb869d9a8a64f/e5ea187/tree_hash/src/lib.rs:43 2-leaf path uses a stack [0; 64]

**Skeptic check.** Verified inline/stack buffers in tree_hash. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#3581](https://github.com/sigp/lighthouse/pull/3581), [prysm#16251](https://github.com/OffchainLabs/prysm/pull/16251), [caplin#22486](https://github.com/erigontech/erigon/pull/22486)

</details>


<a id="tree_hash-072"></a>
<details>
<summary><b>tree_hash-072</b> Chunk byte data directly, no pack copy — <i>partial · medium · M · cpu, memory</i></summary>

**Idea.** Chunk byte lists and uint64 lists into 32-byte leaves directly in one pass with one exact allocation, skipping intermediate pack-into-chunks buffers.

**Gap in Lighthouse.** ssz_types hash_vec (VariableList/FixedVector::tree_hash_root) has no bulk path for packed basic types: u8 lists are fed one byte at a time and u64 lists 8 bytes at a time. Add a fast path (e.g. when T is u8 / packing factor 32, or via a new TreeHash method returning the packed slice) that calls MerkleHasher::write once on the whole byte slice. Local bench on this exact tree_hash/ssz_types rev: 1 MB VariableList&lt;u8&gt; root 13.4 ms per-byte vs 4.3 ms with merkle_root on the slice (same root).

**Impact.** ~3x faster transaction-byte hashing: ~9 ms saved per MB of transactions on the block-root computation in gossip verification and on payload header construction; also u64 lists outside milhouse.

**Best measured result.** 1M bytes: 7.70MB-&gt;2.77MB, 1.096ms-&gt;0.807ms (pr:prysm#17209)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/ssz_types-19f835ca387d51e3/8955d22/src/tree_hash.rs:44 Basic types: hasher.write(&amp;item.tree_hash_packed_encoding()) once per element (per byte for u8)
- ~/.cargo/git/checkouts/tree_hash-f96cb869d9a8a64f/e5ea187/tree_hash/src/impls.rs:21 u8 packed encoding builds a SmallVec per byte
- ~/.cargo/git/checkouts/tree_hash-f96cb869d9a8a64f/e5ea187/tree_hash/src/merkle_hasher.rs:225 1-byte slices go through buffer.extend_from_slice
- [`consensus/types/src/execution/execution_payload.rs:19`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/execution/execution_payload.rs#L19) Transaction = VariableList&lt;u8, N&gt;
- [`consensus/types/src/execution/execution_payload_header.rs:287`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/execution/execution_payload_header.rs#L287) transactions.tree_hash_root() for header
- [`beacon_node/beacon_chain/src/block_verification.rs:1965`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1965) get_block_root -&gt; block.canonical_root() hashes all tx bytes on gossip
- [`consensus/types/src/data/mod.rs:32`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/data/mod.rs#L32) Blob = FixedVector&lt;u8, ...&gt; same per-byte path

**Skeptic check.** Earlier evidence was right that there is no intermediate pack allocation, but wrong that the effect is the same: bytes are not chunked directly, and the per-element path measured 3x slower than direct chunking for 1 MB.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [prysm#10830](https://github.com/OffchainLabs/prysm/pull/10830), [prysm#17209](https://github.com/OffchainLabs/prysm/pull/17209)

</details>


<a id="tree_hash-073"></a>
<details>
<summary><b>tree_hash-073</b> Reinterpret little-endian uint arrays as chunks — <i>not · low · S · cpu</i></summary>

**Idea.** On little-endian machines treat the memory of fixed-size uint arrays directly as SSZ chunk bytes when merkleizing, instead of converting each element.

**Gap in Lighthouse.** Plain Vec/FixedVector of basic ints is hashed element by element through tree_hash_packed_encoding into MerkleHasher; no little-endian memcpy fast path. Big state lists go through milhouse PackedLeaf, which also encodes per element (packed_leaf.rs:44). Fix: add a cfg(target_endian = little) branch in ssz_types hash_vec / tree_hash packed path for u64/u8 slices feeding raw bytes to merkle_root (upstream crate work).

**Impact.** Saves a small per-element copy when hashing non-milhouse basic arrays (e.g. in non-cached paths); milhouse paths dominate state hashing, so gain is marginal.

**Evidence (Lighthouse @ 928b61e719).**

- ssz_types git 8955d22 src/tree_hash.rs:66-75 vec_tree_hash_root uses MerkleHasher with per-element packed encoding
- tree_hash e5ea187 tree_hash/src/impls.rs:29 per-int to_le conversion, no byte-slice reinterpret

**Sources.** [nimbus#3009](https://github.com/status-im/nimbus-eth2/pull/3009), [nimbus@15ce2de3f](https://github.com/status-im/nimbus-eth2/commit/15ce2de3f0a0)

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


<a id="tree_hash-075"></a>
<details>
<summary><b>tree_hash-075</b> Reuse deposit trie root, no double hash — <i>n/a · low · S · cpu</i></summary>

**Idea.** Reuse the deposit trie root already computed before an insertion instead of calling hash_tree_root twice on an unchanged trie per deposit log.

**Gap in Lighthouse.** No eth1 deposit polling in Lighthouse beacon node; genesis calls root once per deposit.

**Impact.** None; idea does not apply.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/common/deposit_data_tree.rs:46-51`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/deposit_data_tree.rs#L46-L51) root() computes once per call
- [`consensus/state_processing/src/genesis.rs:40-42`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/genesis.rs#L40-L42)

**Sources.** [prysm#16764](https://github.com/OffchainLabs/prysm/pull/16764)

</details>


<a id="tree_hash-076"></a>
<details>
<summary><b>tree_hash-076</b> Take previous state root from pre-state — <i>implemented · low · S · cpu</i></summary>

**Idea.** During slot processing take the previous state root from the immutable pre-state whose root is already cached, instead of rehashing the mutable copy.

**Impact.** Hot paths pass the known pre-state root; later iterations of complete_state_advance must hash a genuinely new state, and milhouse makes that incremental.

**Best measured result.** "only a minor improvement" (pr:teku#3973)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_slot_processing.rs:122`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_slot_processing.rs#L122) cache_state uses supplied state_root, hashes only when None
- [`beacon_node/beacon_chain/src/block_verification.rs:1639`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1639) per_slot_processing(&amp;mut state, Some(state_root))
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:291`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L291) Some(head_state_root)
- [`consensus/state_processing/src/block_replayer.rs:233`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/block_replayer.rs#L233) Some(state_root) from blocks
- [`consensus/state_processing/src/state_advance.rs:44`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/state_advance.rs#L44) complete_state_advance passes the known root on the first slot

**Skeptic check.** Verified known roots are passed on block import, state advance and replay. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#3973](https://github.com/Consensys-Incorporated/teku/pull/3973)

</details>


<a id="tree_hash-077"></a>
<details>
<summary><b>tree_hash-077</b> Remove superseded SSZ hash-result caches — <i>n/a · low · S · cpu, memory</i></summary>

**Idea.** Remove legacy per-object hash-result caches that per-field state caching already covers, saving their memory and the lookup/locking cost on the hashing path.

**Gap in Lighthouse.** Lighthouse has no legacy per-object hash-result caches to remove; milhouse caches hashes in tree nodes.

**Impact.** None; idea does not apply.

**Evidence (Lighthouse @ 928b61e719).**

- milhouse-0.9.0/src/tree.rs per-node cached hash only; no per-object hash caches in tree_hash 0.12

**Sources.** [prysm#10256](https://github.com/OffchainLabs/prysm/pull/10256)

</details>


<a id="tree_hash-078"></a>
<details>
<summary><b>tree_hash-078</b> Short lock during field trie recompute — <i>n/a · low · S · latency</i></summary>

**Idea.** Release the lock on the old field trie as soon as the new copied trie is swapped in, instead of holding it for the whole recompute.

**Gap in Lighthouse.** Go field-trie lock pattern does not exist in milhouse; trees are immutable and copy-on-write.

**Impact.** None; idea does not apply.

**Evidence (Lighthouse @ 928b61e719).**

- milhouse-0.9.0/src/tree.rs persistent Arc tree, no field trie lock

**Sources.** [prysm#9353](https://github.com/OffchainLabs/prysm/pull/9353)

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


<a id="tree_hash-080"></a>
<details>
<summary><b>tree_hash-080</b> Compute body root and sub-roots in one pass — <i>not · low · S · cpu</i></summary>

**Idea.** When both the BeaconBlockBody root and field sub-roots are needed, compute them all in a single hash_tree_root pass rather than hashing fields repeatedly.

**Gap in Lighthouse.** Block root and body_root/header are computed by separate tree_hash_root calls; add a helper returning (block_root, body_root) from one body hash (block root = hash(header fields with body_root)) and use it where both are needed (BeaconBlockRef::block_header, sidecar construction).

**Impact.** Saves one BeaconBlockBody hash (tens of microseconds to ~1ms with blobs/commitments) only on paths that need both, e.g. slasher and data column sidecar building; most gossip blocks need only the root.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/block/beacon_block.rs:190`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/block/beacon_block.rs#L190) canonical_root = full tree_hash_root
- [`consensus/types/src/block/beacon_block.rs:278`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/block/beacon_block.rs#L278) body_root rehashes body separately
- [`beacon_node/beacon_chain/src/block_verification.rs:886`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L886) signed_block_header() recomputes body root

**Sources.** [nimbus#8979](https://github.com/status-im/nimbus-eth2/pull/8979)

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


<a id="tree_hash-082"></a>
<details>
<summary><b>tree_hash-082</b> Layered deposit trie with zero hashes — <i>n/a · low · S · cpu, memory</i></summary>

**Idea.** Build the deposit sparse Merkle trie bottom-up as layer arrays with precomputed zero hashes per level, and read proofs straight from the layers, instead of a generic recursive trie.

**Gap in Lighthouse.** Lighthouse's deposit tree (merkle_proof MerkleTree, with zero-subtree nodes and finalization) is only used for genesis/test/lcli; the BN no longer builds deposit proofs on the hot path post-Electra (EIP-6110), so a layered rewrite would not affect mainnet nodes.

**Impact.** Nothing on a running mainnet node.

**Best measured result.** proof generation 25% faster; full trie from leaves 50% faster (49684 to 26494 ns/op, 377 to 214 allocs) (pr:prysm#3056)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/common/deposit_data_tree.rs:9`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/deposit_data_tree.rs#L9) DepositDataTree wraps merkle_proof::MerkleTree
- [`consensus/state_processing/src/genesis.rs:37`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/genesis.rs#L37) only user outside tests

**Sources.** [prysm#3056](https://github.com/OffchainLabs/prysm/pull/3056)

</details>


<a id="tree_hash-083"></a>
<details>
<summary><b>tree_hash-083</b> Precompute leaf offsets in cache overlay — <i>n/a · low · S · cpu</i></summary>

**Idea.** Precompute the leaf ranges of each tree-hash cache overlay once instead of summing preceding leaf lengths on every lookup (O(n^2) to O(n)), and store 32-byte hash leaves directly.

**Gap in Lighthouse.** The old cached_tree_hash overlay code the commit fixed was replaced by milhouse persistent trees with built-in hash caching, so the quadratic offset sum no longer exists.

**Impact.** None; the code is gone.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs): state hashing uses milhouse tree-hash caching (no cached_tree_hash crate in consensus/)
- Cargo.lock milhouse 0.9.0

**Sources.** [lighthouse@c58723350](https://github.com/sigp/lighthouse/commit/c58723350ce3)

</details>


<a id="tree_hash-084"></a>
<details>
<summary><b>tree_hash-084</b> Skip state-root history hashing for attestations — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Load states for attestation verification without recomputing their state-root history and without cloning caches on intermediate states, avoiding tree hashing that dominated allocations.

**Impact.** Already in place (lighthouse#1522); milhouse also makes intermediate state clones cheap.

**Best measured result.** tree hashing was 23% of memory allocations by bytes (heaptrack) (pr:lighthouse#1522)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/state_advance.rs:72`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/state_advance.rs#L72) partial_state_advance uses zero roots for intermediate slots
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:454`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L454) partial_state_advance for shuffling
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2164`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2164) committee-cache path partial_state_advance
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:346`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L346) proposer cache partial_state_advance
- [`beacon_node/beacon_chain/src/block_verification.rs:2197`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L2197) cheap_state_advance_to_obtain_committees partial_state_advance

**Skeptic check.** Verified all attestation/proposer shuffling advances use partial_state_advance. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#1522](https://github.com/sigp/lighthouse/pull/1522)

</details>


<a id="tree_hash-085"></a>
<details>
<summary><b>tree_hash-085</b> Two-level dirty bitmap with deferred rehash — <i>partial · low · M · cpu</i></summary>

**Idea.** Track changed leaf chunks in a two-level bitmap (summary bit per 64-chunk word) and rehash once at commit over sorted maximal dirty ranges, so draining and clearing scan only touched words.

**Gap in Lighthouse.** Deferred one-shot rehash of touched paths is real, but the dirty-set itself is not two-level: for lists on the default VecMap update map (balances, inactivity_scores, participation) VecMap::for_each_range scans every index linearly when with_updated_leaves probes for updates, and the VecMap is rebuilt dense up to the max touched index on every commit. A per-block sparse update (proposer/sync rewards at high indices) costs O(validator count) scan and allocation; a summary-bit bitmap (or BTreeMap for sparse phases) would make it O(touched).

**Impact.** Small: ~1M Option checks plus a multi-MB Vec allocation per affected list per block; epoch processing (dense updates) unaffected.

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/tree.rs:515 tree_hash skips nodes with non-zero cached hash (deferred rehash of touched paths only)
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/tree.rs:193-206 with_updated_leaves probes left/right ranges via for_each_range at every node
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/update_map.rs:144-159 VecMap::for_each_range walks every key in start..end (no summary bitmap)
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/interface.rs:88 apply_updates mem::take's the map, so a fresh VecMap is regrown to max index each commit
- [`consensus/types/src/state/beacon_state.rs:554`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L554) balances is List&lt;u64, _&gt; with default MaxMap&lt;VecMap&gt; update map
- [`consensus/types/src/state/beacon_state.rs:77`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L77) validators uses BTreeMap update map (sparse-efficient)

**Skeptic check.** Earlier evidence was right that milhouse buffers updates and rehashes once over dirty paths only, but missed that the update-map scan/clear is linear over the index range for VecMap-backed lists; validators use BTreeMap and are fine.

**Verdict history.** implemented (checked) → partial (skeptic)

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


<a id="tree_hash-087"></a>
<details>
<summary><b>tree_hash-087</b> Self-describing cache overlays avoid old-item copy — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Store the layout overlay (chunk offsets per field) inside the tree hash cache and walk it on update, comparing the current value only against cached dirty flags, so the previous item need not be cloned or kept. This removes a copy of the old value per cached update.

**Impact.** Superseded: milhouse keeps the hash caches inside the tree, so no old-item copy is kept.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:3070-3077`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3070-L3077)
- [`consensus/types/src/state/beacon_state.rs:3082-3085`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3082-L3085)

**Skeptic check.** The old cached_tree_hash crate appears only in ef_tests and a bench. Production hashing goes through milhouse internal caches, so the overlay mechanism is obsolete and its goal is met.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@4aeadfa60](https://github.com/sigp/lighthouse/commit/4aeadfa60f6e)

</details>


<a id="tree_hash-088"></a>
<details>
<summary><b>tree_hash-088</b> Native fixed-width integers in hashing paths — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Use native fixed-width integers (u64) rather than an arbitrary-precision bignum type for balances, slots and epochs in SSZ hash-tree-root and serialization. This avoids heap allocation and slow big-number arithmetic.

**Impact.** Native u64 is used throughout SSZ and hashing.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:568`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L568)
- [`consensus/types/src/data/data_column_custody_group.rs:63`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/data/data_column_custody_group.rs#L63)

**Skeptic check.** Balances, slots and epochs are u64 newtypes. No bignum crate is used in consensus hashing. U256 appears only in custody node-id math.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@0f53c8e11](https://github.com/ChainSafe/lodestar/commit/0f53c8e11a11)

</details>


<a id="tree_hash-089"></a>
<details>
<summary><b>tree_hash-089</b> Hash fixed-size lists as packed primitive vectors — <i>implemented · low · S · cpu</i></summary>

**Idea.** Declare small fixed-size sequences of integers (such as a committee) as vectors of primitives instead of lists of per-element containers, so the hash tree root packs several values per 32-byte chunk. Fewer chunks mean fewer hashes.

**Impact.** None left: the IL committee and PTC window are already packed u64 vectors.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/execution/inclusion_list.rs:10`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/execution/inclusion_list.rs#L10)
- [`consensus/types/src/state/beacon_state.rs:811`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L811)

**Skeptic check.** Teku #9384 switched the IL committee root to a primitive vector schema. Lighthouse defines InclusionListCommittee as FixedVector&lt;u64&gt;, and ptc_window as Vector&lt;FixedVector&lt;u64&gt;&gt;, so both hash as packed chunks. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#9384](https://github.com/Consensys-Incorporated/teku/pull/9384)

</details>


<a id="tree_hash-090"></a>
<details>
<summary><b>tree_hash-090</b> Promote cached hashes on state finalization — <i>n/a · low · cpu, memory</i></summary>

**Idea.** When an unfinalized state delta is merged into the finalized base, promote its already-computed hash overlay into the base's hash tree so finalization costs no SHA-256, and keep read-only views separate from the hashing overlay.

**Impact.** Silver's delta-merge overlay design; in Lighthouse cached hashes live in shared tree nodes, so finalization does not recompute them.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:1088`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1088) hashes cached in shared milhouse nodes
- [`beacon_node/store`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store) (hot/cold diff migration, not read in depth)

**Sources.** [silver#90](https://github.com/gattaca-com/silver/pull/90)

</details>


