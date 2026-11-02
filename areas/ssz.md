# ssz

92 ideas: 13 not, 14 partial, 27 implemented, 38 n/a; 5 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [ssz-001](#ssz-001) | Teku SSZ mutable-collection hot path micro-optimizations | n/a | low |  | cpu |
| [ssz-002](#ssz-002) | Encode SSZ into caller buffer without per-element allocations | partial | low | M | cpu, memory |
| [ssz-003](#ssz-003) | Avoid arbitrary-precision integers for uint64 SSZ fields | n/a | low |  | memory, cpu |
| [ssz-004](#ssz-004) | Compare against precomputed default for is-default checks | not | low | S | cpu, memory |
| [ssz-005](#ssz-005) | Read list length from tree without child cache | n/a | low |  | memory, cpu |
| [ssz-006](#ssz-006) | Pass SSZ containers by reference, not by value | n/a | low |  | cpu, memory |
| [ssz-007](#ssz-007) | Avoid dummy value allocation for type lookup | n/a | low |  | memory, cpu |
| [ssz-008](#ssz-008) | Cheap little-endian to uint256 conversion for base fee | implemented | low | S | cpu |
| [ssz-009](#ssz-009) | Allocation-free merkleization scratch buffers | implemented | low | S | cpu, memory |
| [ssz-010](#ssz-010) | Avoid proxy wrappers on hot state access | n/a | low |  | cpu |
| [ssz-011](#ssz-011) | Keep SSZ lists as-is when wrapping blocks | n/a | low |  | cpu, memory |
| [ssz-012](#ssz-012) **★** | Balances list type with cached flat array | not | medium | L | cpu, latency |
| [ssz-013](#ssz-013) | Bitlist overlap popcount without allocating result | partial | low | S | cpu, memory |
| [ssz-014](#ssz-014) | Word-wise set-bit index extraction for bitfields | not | low | S | cpu |
| [ssz-015](#ssz-015) **★** | Enforce SSZ list limits and offsets during decode | partial | medium | S | memory, cpu, bandwidth |
| [ssz-016](#ssz-016) | Bulk-convert tree-backed bitlist to flat bitlist | n/a | low | S | cpu |
| [ssz-017](#ssz-017) | Bulk memcpy for byte-vector and byte-list SSZ | partial | low | S | cpu |
| [ssz-018](#ssz-018) | Faster snappy implementation for gossip and database | implemented | low | S | cpu, latency |
| [ssz-019](#ssz-019) | In-order leaf traversal instead of per-index lookups | implemented | low | S | cpu, latency |
| [ssz-020](#ssz-020) | Bulk memcpy for uint list serialization | not | low | M | cpu |
| [ssz-021](#ssz-021) **★** | Pack multiple elements into one tree leaf node | not | medium | L | memory, cpu, disk |
| [ssz-022](#ssz-022) | Cache hash roots of large state lists | implemented | high | S | cpu |
| [ssz-023](#ssz-023) | Cache constant empty-container hash root | not | low | S | cpu |
| [ssz-024](#ssz-024) | Cache last tree path for sequential access | partial | low | M | cpu |
| [ssz-025](#ssz-025) | Compile-time generalized index constants | implemented | low | S | cpu |
| [ssz-026](#ssz-026) | Compute data column inclusion proof once per block | implemented | medium | S | cpu |
| [ssz-027](#ssz-027) | Flat buffer for execution payload transactions | not | low | L | memory, cpu, latency |
| [ssz-028](#ssz-028) | SSZ library bump with upstream perf change | n/a | low |  | cpu |
| [ssz-029](#ssz-029) **★** | Deserialize SSZ bytes directly into tree-backed values | partial | medium | M | cpu, memory, startup, latency |
| [ssz-030](#ssz-030) | Clone bitfields with native buffer copy | implemented | low | S | cpu |
| [ssz-031](#ssz-031) | Build merkle trees bottom-up without intermediate copies | implemented | low | S | cpu, memory |
| [ssz-032](#ssz-032) | DataView without explicit length in offset tables | n/a | low | S | cpu |
| [ssz-033](#ssz-033) | Store SSZ lists as node plus length | implemented | low | S | cpu, memory |
| [ssz-034](#ssz-034) | Explicit allocation and value types in SSZ decode | n/a | low | S | memory |
| [ssz-035](#ssz-035) | Generated SSZ codecs instead of reflection | implemented | low | S | cpu, memory, latency |
| [ssz-036](#ssz-036) | Fast hex encode/decode for API byte fields | not | low | M | cpu, latency |
| [ssz-037](#ssz-037) | Specialized 32-byte root equality | n/a | low | S | cpu |
| [ssz-038](#ssz-038) | Replace SSZ library with faster implementation | n/a | low | S | cpu |
| [ssz-039](#ssz-039) | Faster structural-to-tree conversion | n/a | low | S | cpu |
| [ssz-040](#ssz-040) | Fewer allocations in SSZ query path parsing | n/a | low | S | cpu, memory |
| [ssz-041](#ssz-041) | Faster expected withdrawals via cheap list reads | partial | low | S | cpu |
| [ssz-042](#ssz-042) | Fixed-size arrays for 32-byte roots | n/a | low | S | memory, cpu |
| [ssz-043](#ssz-043) | Fast-path decode for fixed-size containers | implemented | low | S | cpu, memory |
| [ssz-044](#ssz-044) | Keep objects as raw SSZ bytes with accessors | not | low | L | cpu, memory |
| [ssz-045](#ssz-045) | forEach over tree view without intermediate objects | n/a | low | S | memory, cpu |
| [ssz-046](#ssz-046) | Height-based merkleizer | partial | low | S | cpu |
| [ssz-047](#ssz-047) | Build state proofs from cached tree layers | n/a | low | S | cpu, memory, latency |
| [ssz-048](#ssz-048) | Immutable SSZ value types shared by reference | n/a | low | S | cpu, memory |
| [ssz-049](#ssz-049) | Deserialize and clone into caller-provided output | n/a | low |  | cpu, memory |
| [ssz-050](#ssz-050) | Inline small-vector storage for attestation bitfields | partial | low | M | memory, cpu |
| [ssz-051](#ssz-051) | Integer gindex paths for proof descriptors | not | low | M | cpu, memory |
| [ssz-052](#ssz-052) | Avoid boxed objects for primitive SSZ values | n/a | low | S | memory, cpu |
| [ssz-053](#ssz-053) | Lazy merkle tree for bitlists and bitvectors | n/a | low | S | cpu, memory |
| [ssz-054](#ssz-054) | Memoize derived values of composite SSZ views | n/a | low | S | cpu |
| [ssz-055](#ssz-055) | Native equality instead of serialize-and-compare | implemented | low | S | cpu |
| [ssz-056](#ssz-056) | No closure allocation in composite child access | n/a | low | S | memory, cpu |
| [ssz-057](#ssz-057) | Packed word storage for bitlists and bitvectors | partial | low | S | memory, cpu |
| [ssz-058](#ssz-058) | Packed serialized node for lists of byte lists | not | low | L | cpu, memory |
| [ssz-059](#ssz-059) | Packed specialized collections for primitive SSZ types | implemented | low | S | cpu, memory |
| [ssz-060](#ssz-060) | Pad once when expanding byte to bits | n/a | low | S | cpu |
| [ssz-061](#ssz-061) | Presize serialization output buffers | implemented | low | S | cpu, memory |
| [ssz-062](#ssz-062) | Persistent merkle tree backing for state fields | implemented | high | S | cpu, memory |
| [ssz-063](#ssz-063) | Preallocate decode Vec from byte length | implemented | low | S | memory, cpu |
| [ssz-064](#ssz-064) | Precompute SSZ length bounds per schema | partial | low | S | cpu, memory |
| [ssz-065](#ssz-065) | Progressive SSZ merkleization for unbounded lists | implemented | low | S | cpu, memory |
| [ssz-066](#ssz-066) | Keep validator pubkeys as raw compressed bytes | implemented | high | S | cpu |
| [ssz-067](#ssz-067) | Read-only single pass over tree-backed validator | n/a | low |  | cpu, memory |
| [ssz-068](#ssz-068) | Remove fork-ambiguous trial decode of attestations | implemented | low | S | cpu |
| [ssz-069](#ssz-069) | Zero-copy SSZ decode via input buffer views | n/a | low |  | memory, cpu, latency |
| [ssz-070](#ssz-070) | Share backing tree when blinding/unblinding blocks | n/a | low |  | memory, cpu |
| [ssz-071](#ssz-071) **★** | Intern validator pubkeys and cache their hash | partial | medium | M | memory, cpu |
| [ssz-072](#ssz-072) | Serialized size from length leaf | n/a | low |  | cpu, memory |
| [ssz-073](#ssz-073) | Skip public wrappers in recursive clone/equals | n/a | low |  | cpu |
| [ssz-074](#ssz-074) | Skip default-init before decoding fixed-size lists | implemented | low | S | cpu, startup |
| [ssz-075](#ssz-075) | Skip cached-root updates when decoding SSZ | implemented | low | S | cpu |
| [ssz-076](#ssz-076) | Read slot from SSZ bytes to pick fork | implemented | low | S | cpu, latency |
| [ssz-077](#ssz-077) | Encode small integers into exact-size buffer | n/a | low |  | memory, cpu |
| [ssz-078](#ssz-078) | Snappy compression of SSZ on the wire | implemented | low | S | bandwidth |
| [ssz-079](#ssz-079) | Serialize state lists by concatenating leaf data | partial | low | M | cpu, memory, disk |
| [ssz-080](#ssz-080) | Stream tree nodes without node-ID arrays | implemented | low | S | memory, cpu |
| [ssz-081](#ssz-081) | Streaming bounded-memory tree construction | implemented | low | S | memory, cpu |
| [ssz-082](#ssz-082) | Tree-backed bitfields with packed chunks | n/a | low |  | memory, cpu |
| [ssz-083](#ssz-083) | Convert block to tree-backed once before transition | partial | low | S | cpu |
| [ssz-084](#ssz-084) | Tree-backed containers with caches for heavy members | n/a | low |  | cpu, memory |
| [ssz-085](#ssz-085) | Validator list type with batch hashing | not | low | L | cpu, memory |
| [ssz-086](#ssz-086) | Read bitlists through tree view without copy | n/a | low |  | cpu, memory |
| [ssz-087](#ssz-087) | Send builder validator registrations as SSZ | not | low | S | bandwidth |
| [ssz-088](#ssz-088) | Shared singleton instances for common integer constants | n/a | low |  | cpu, memory |
| [ssz-089](#ssz-089) | Direct byte-order primitives for SSZ integer conversion | n/a | low |  | cpu |
| [ssz-090](#ssz-090) | Early return for already-parsed SSZ types | n/a | low |  | cpu |
| [ssz-091](#ssz-091) | Ordered map for pending child changes in mutable SSZ | implemented | low | S | cpu |
| [ssz-092](#ssz-092) | Value range loops in generated hash-tree-root code | n/a | low |  | cpu |

★ actionable. Click an id for the full record.

## Ideas

<a id="ssz-001"></a>
<details>
<summary><b>ssz-001</b> Teku SSZ mutable-collection hot path micro-optimizations — <i>n/a · low · cpu</i></summary>

**Idea.** In mutable SSZ collections, skip per-set schema validation, memoize fixed-part sizes and element schemas, batch packed primitive updates into one tree-node write, and hoist list sizes out of epoch loops. Each removes repeated per-element work on hot state-update paths.

**Impact.** Teku-specific mutable collection internals; Lighthouse uses milhouse with different design.

**Best measured result.** TransitionBenchmark.Epoch faster than before refactor; BeaconStateSerialization 489.9 -&gt; 893.1 ops/s (pr:teku#3735)

**Evidence (Lighthouse @ 928b61e719).**

- milhouse d67aabd src/list.rs:442-462 (Rust milhouse has its own tree/pending-update design)

**Sources.** [teku#3735](https://github.com/Consensys-Incorporated/teku/pull/3735), [teku#3722](https://github.com/Consensys-Incorporated/teku/pull/3722)

</details>


<a id="ssz-002"></a>
<details>
<summary><b>ssz-002</b> Encode SSZ into caller buffer without per-element allocations — <i>partial · low · M · cpu, memory</i></summary>

**Idea.** SSZ encoding (containers, lists, full states) appends directly into one caller-supplied output buffer instead of building intermediate per-field or per-element vectors and copying them. This removes one allocation and copy per container or element when serializing states and blocks.

**Gap in Lighthouse.** SszEncoder::container/append_parameterized/finalize write variable-length fields into a separate unreserved scratch Vec and then append it, so for BeaconState (validators, balances, participation, inactivity_scores are all variable fields) the bulk of the state is grown by doubling reallocs and copied a second time; the same happens per nested variable container (block body, attestation lists). Writing variable parts directly into the caller buffer (offsets computed from ssz_bytes_len of each field) would remove these copies.

**Impact.** Removes roughly one extra copy plus realloc churn of the variable part of each container; for a mainnet state that is ~150+ MB of memcpy per full-state encode (hdiff snapshots, state SSZ API).

**Best measured result.** non-epoch slot 310 -&gt; 84 ms; epoch slot 12381 -&gt; 2545 ms (2500 validators) (pr:nimbus#226)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/ethereum_ssz-ba970959eb75904b/974f78f/ssz/src/encode.rs:39-45 as_ssz_bytes preallocates the top-level buffer
- ~/.cargo/git/checkouts/ethereum_ssz-ba970959eb75904b/974f78f/ssz/src/encode.rs:93-132 SszEncoder::container stages every variable-size field in a fresh variable_bytes Vec (vec![], no reserve) and copies it into buf in finalize()
- ~/.cargo/git/checkouts/ethereum_ssz-ba970959eb75904b/974f78f/ssz_derive/src/lib.rs:480-494 derived containers always use SszEncoder
- ~/.cargo/git/checkouts/ethereum_ssz-ba970959eb75904b/974f78f/ssz/src/encode/impls.rs:305-312 and milhouse list.rs:464-470 lists of variable items use the same staging
- [`beacon_node/store/src/hdiff.rs:197`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L197) full BeaconState as_ssz_bytes on the hdiff storage path

**Skeptic check.** Top-level preallocation and fixed-size list appends are real, but the earlier evidence called the per-container scratch Vec small; for BeaconState it holds almost the whole state and is unreserved, so the idea is only partly implemented.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [nimbus#226](https://github.com/status-im/nimbus-eth2/pull/226), [lighthouse@56fe63f78](https://github.com/sigp/lighthouse/commit/56fe63f78d72), [lighthouse@daf6912d1](https://github.com/sigp/lighthouse/commit/daf6912d18ec), [nimbus#5996](https://github.com/status-im/nimbus-eth2/pull/5996), [nimbus#6051](https://github.com/status-im/nimbus-eth2/pull/6051), [nimbus#202](https://github.com/status-im/nimbus-eth2/pull/202), [lighthouse@480c5ff16](https://github.com/sigp/lighthouse/commit/480c5ff16028)

</details>


<a id="ssz-003"></a>
<details>
<summary><b>ssz-003</b> Avoid arbitrary-precision integers for uint64 SSZ fields — <i>n/a · low · memory, cpu</i></summary>

**Idea.** Represent uint64 SSZ fields (slashing indices, epochs, generic uints) with native fixed-width integers or raw 8-byte arrays instead of arbitrary-precision bigint objects. Native integers need no heap allocation and no GC.

**Impact.** Rust uses native u64 for uint64 fields; JS bigint issue.

**Evidence (Lighthouse @ 928b61e719).**

- Rust u64 is native; no bigint in SSZ types

**Sources.** [lodestar#7502](https://github.com/ChainSafe/lodestar/pull/7502), [lodestar#6116](https://github.com/ChainSafe/lodestar/pull/6116), [lodestar#2213](https://github.com/ChainSafe/lodestar/pull/2213), [lodestar#9528](https://github.com/ChainSafe/lodestar/pull/9528), [lodestar@84ed24d0b](https://github.com/ChainSafe/lodestar/commit/84ed24d0bfca), [lodestar#3977](https://github.com/ChainSafe/lodestar/pull/3977)

</details>


<a id="ssz-004"></a>
<details>
<summary><b>ssz-004</b> Compare against precomputed default for is-default checks — <i>not · low · S · cpu, memory</i></summary>

**Idea.** Check whether an SSZ object (e.g. ExecutionPayloadHeader) is the default value by comparing with one precomputed static default, instead of constructing a default object on each call.

**Gap in Lighthouse.** Compare against a static (lazy_static/OnceLock) default per fork, or check fields individually, in is_default_with_zero_roots/is_default_with_empty_roots.

**Impact.** Negligible on mainnet today: post-Capella paths short-circuit; remaining callers (execution_payload.rs:251, fork_choice.rs:433) are once per block.

**Best measured result.** 2.5x: 137M vs 54M ops/s (pr:teku#5207)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/execution/execution_payload_header.rs:169`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/execution/execution_payload_header.rs#L169) is_default_with_zero_roots compares *inner == Default::default(), building a default (logs_bloom, extra_data) each call
- [`consensus/types/src/execution/payload.rs:322`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/execution/payload.rs#L322) same for full payload
- [`consensus/state_processing/src/per_block_processing.rs:507`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing.rs#L507) is_merge_transition_complete returns early for Capella+, so hot path is only pre-Capella

**Sources.** [teku#5207](https://github.com/Consensys-Incorporated/teku/pull/5207)

</details>


<a id="ssz-005"></a>
<details>
<summary><b>ssz-005</b> Read list length from tree without child cache — <i>n/a · low · memory, cpu</i></summary>

**Idea.** On list view initialization, read the length directly from the tree length node instead of allocating a child-cache entry only to read it.

**Impact.** Lodestar persistent-merkle-tree child cache has no equivalent in milhouse.

**Evidence (Lighthouse @ 928b61e719).**

- milhouse d67aabd src/list.rs (List stores len directly; no child-cache)

**Sources.** [lodestar@77ad664a8](https://github.com/ChainSafe/lodestar/commit/77ad664a86e8)

</details>


<a id="ssz-006"></a>
<details>
<summary><b>ssz-006</b> Pass SSZ containers by reference, not by value — <i>n/a · low · cpu, memory</i></summary>

**Idea.** SSZ hash, serialize and container helper functions take references/pointers to large container fields instead of copying the structs on each call.

**Impact.** Rust passes containers by reference; nothing to change.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/block/beacon_block.rs:133`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/block/beacon_block.rs#L133) from_ssz_bytes takes &amp;[u8], methods take &amp;self

**Sources.** [lodestar@e459d5935](https://github.com/ChainSafe/lodestar/commit/e459d5935a6b), [lodestar@83e46c48f](https://github.com/ChainSafe/lodestar/commit/83e46c48f934), [lodestar@e1d9545f1](https://github.com/ChainSafe/lodestar/commit/e1d9545f107b)

</details>


<a id="ssz-007"></a>
<details>
<summary><b>ssz-007</b> Avoid dummy value allocation for type lookup — <i>n/a · low · memory, cpu</i></summary>

**Idea.** In deep-equality and reflection helpers used on SSZ types, get the type through compile-time lookup instead of allocating a dummy value.

**Impact.** Go reflection dummy-value issue; Rust resolves types at compile time.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/block/beacon_block.rs:152`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/block/beacon_block.rs#L152) map_fork_name! dispatches on the enum statically

**Sources.** [prysm#15627](https://github.com/OffchainLabs/prysm/pull/15627)

</details>


<a id="ssz-008"></a>
<details>
<summary><b>ssz-008</b> Cheap little-endian to uint256 conversion for base fee — <i>implemented · low · S · cpu</i></summary>

**Idea.** Convert the little-endian SSZ base fee bytes to a 256-bit integer with a direct byte-reversal routine or direct uint64 construction, without intermediate casts or generic big-integer paths.

**Impact.** None left; base fee is decoded with one direct LE slice conversion.

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/ethereum_ssz-ba970959eb75904b/974f78f/ssz/src/decode/impls.rs:356-372 U256 Decode is fixed 32 bytes, U256::from_le_slice directly
- [`consensus/types/src/execution/execution_payload.rs:193`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/execution/execution_payload.rs#L193) base_fee_per_gas: Uint256

**Skeptic check.** Verified the ssz U256 decode is a single from_le_slice with no intermediate casts or generic bigint path. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#10916](https://github.com/erigontech/erigon/pull/10916), [caplin#19049](https://github.com/erigontech/erigon/pull/19049)

</details>


<a id="ssz-009"></a>
<details>
<summary><b>ssz-009</b> Allocation-free merkleization scratch buffers — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** In the merkleizer, write basic elements and padding straight into reusable chunk buffers, reuse the hasher, and do not zero-initialize scratch memory. Hashing large arrays (e.g. the slashings vector) then makes no per-element heap allocation.

**Impact.** None left: hashing basic vectors (slashings, balances) does no per-element heap allocation; at most one SmallVec spill per hasher for deep trees, and milhouse state fields rehash only dirty leaves.

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/tree_hash-f96cb869d9a8a64f/e5ea187/tree_hash/src/merkle_hasher.rs:147-163 MerkleHasher: SmallVec8 half_nodes, 32-byte inline buffer, one Sha256 context per half node
- ~/.cargo/git/checkouts/tree_hash-f96cb869d9a8a64f/e5ea187/tree_hash/src/merkle_hasher.rs:217-244 write() hashes full 32-byte slices in place and copies partial ones into a stack leaf
- ~/.cargo/git/checkouts/tree_hash-f96cb869d9a8a64f/e5ea187/tree_hash/src/lib.rs:23 PackedEncoding = SmallVec&lt;[u8; 32]&gt; (inline, no heap)
- ~/.cargo/git/checkouts/ssz_types-19f835ca387d51e3/8955d22/src/tree_hash.rs:38-63 hash_vec streams packed encodings of basic elements into one MerkleHasher
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/packed_leaf.rs:29-49 PackedLeaf::tree_hash writes packed values into the 32-byte hash and caches it

**Skeptic check.** Verified the MerkleHasher, ssz_types hash_vec and milhouse PackedLeaf code. The earlier evidence was right; it cited registry paths, but the code actually used is the git checkouts (tree_hash e5ea187, milhouse d67aabd).

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#1058](https://github.com/status-im/nimbus-eth2/pull/1058), [nimbus#596](https://github.com/status-im/nimbus-eth2/pull/596), [caplin#7439](https://github.com/erigontech/erigon/pull/7439), [nimbus#5463](https://github.com/status-im/nimbus-eth2/pull/5463)

</details>


<a id="ssz-010"></a>
<details>
<summary><b>ssz-010</b> Avoid proxy wrappers on hot state access — <i>n/a · low · cpu</i></summary>

**Idea.** Access hot state fields directly instead of through dynamic proxy or wrapper objects that intercept each get; the indirection costs much more than a direct array read.

**Impact.** JS proxy overhead has no Rust equivalent.

**Best measured result.** x180 slower via proxy (27.3ms vs 0.145ms per 100k gets) (pr:lodestar#3109)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs): state fields accessed directly (milhouse List/Vector), no proxy wrappers

**Sources.** [lodestar#3109](https://github.com/ChainSafe/lodestar/pull/3109)

</details>


<a id="ssz-011"></a>
<details>
<summary><b>ssz-011</b> Keep SSZ lists as-is when wrapping blocks — <i>n/a · low · cpu, memory</i></summary>

**Idea.** When building wrapper objects (block plus blobs), reuse the existing SSZ list instead of converting it to a native list and back into a new SSZ list.

**Impact.** Java list conversion; Lighthouse keeps SSZ types (no native-list round trip).

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/kzg_ext/mod.rs:27`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/kzg_ext/mod.rs#L27) commitments kept as the SSZ list type inside the block

**Sources.** [teku#7747](https://github.com/Consensys-Incorporated/teku/pull/7747)

</details>


<a id="ssz-012"></a>
<details>
<summary><b>ssz-012</b> Balances list type with cached flat array — <i>not · medium · L · cpu, latency</i></summary>

**Idea.** Give the balances list a dedicated tree-backed type that keeps a cached flat array of values, so reads and hashing after each block do not miss the cache and walk the tree.

**Gap in Lighthouse.** Add a flat Vec&lt;u64&gt; balances cache to BeaconState (or a milhouse List variant) kept in sync by balance mutators and used for per-block reads and epoch iteration.

**Impact.** A few ms per block at most (Lodestar ~3ms); smaller on Lighthouse because packed milhouse leaves are already cache-friendly.

**Best measured result.** ~3ms faster per block on mainnet, ~4ms on holesky; balances cache misses near 0 (pr:lodestar#6557)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:554`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L554) balances is a plain milhouse List&lt;u64&gt;
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/packed_leaf.rs:10 PackedLeaf caches only its hash, no flat value array
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/update_map.rs:9 UpdateMap only buffers pending writes, not a full flat cache
- [`consensus/types/src/state/epoch_cache.rs:33`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/epoch_cache.rs#L33) EpochCache holds a flat Vec of effective_balances only, not balances
- [`beacon_node/store/src/hdiff.rs:198`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L198) flat Vec&lt;u64&gt; balances exist only transiently in HDiffBuffer for disk diffs

**Second check.** Checked the locked git milhouse rev (d67aabd, not the registry copy), its UpdateMap, EpochCache, ProgressiveBalancesCache and hdiff; none keeps a persistent flat balances array.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [lodestar#6557](https://github.com/ChainSafe/lodestar/pull/6557)

</details>


<a id="ssz-013"></a>
<details>
<summary><b>ssz-013</b> Bitlist overlap popcount without allocating result — <i>partial · low · S · cpu, memory</i></summary>

**Idea.** Count set bits of bitlist OR/AND/XOR directly over the byte slices, without allocating a result bitlist, for attestation aggregation overlap checks.

**Gap in Lighthouse.** Add a Bitfield::is_disjoint / intersection_is_zero doing a byte-wise (or u64-wise) AND-any over both slices with no result bitfield, and call it from should_aggregate in CompactIndexedAttestationBase/Electra and the Attestation aggregate checks.

**Impact.** Removes a small stack copy per aggregation check in the op pool; the cost is already tiny since the SmallVec is inline. Negligible on a mainnet node.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation_storage.rs:236`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L236) should_aggregate does intersection(..).is_zero()
- ~/.cargo/git/checkouts/ethereum_ssz-ba970959eb75904b/974f78f/ssz/src/bitfield.rs:232 intersection builds a new SmallVec&lt;[u8;128]&gt; (inline, no heap for committees &lt;=1024 bits)
- ~/.cargo/git/checkouts/ethereum_ssz-ba970959eb75904b/974f78f/ssz/src/bitfield.rs:496 is_zero scans bytes

**Sources.** [prysm#8299](https://github.com/OffchainLabs/prysm/pull/8299)

</details>


<a id="ssz-014"></a>
<details>
<summary><b>ssz-014</b> Word-wise set-bit index extraction for bitfields — <i>not · low · S · cpu</i></summary>

**Idea.** Extract the set-bit indices of a bitlist or bitvector by scanning machine words and jumping between set bits with trailing-zero count, instead of testing each bit. This speeds attestation aggregation-bit iteration.

**Gap in Lighthouse.** Add a set-bit index iterator (u64 words + trailing_zeros) to ssz Bitfield and use it in get_attesting_indices (base and electra); in electra also drop the per-committee HashSet in favour of a Vec since indices are unique.

**Impact.** Faster attestation to indexed-attestation conversion in block processing and op pool; committees are ~500 bits so savings are microseconds per attestation, the Electra HashSet is the larger cost.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/common/get_attesting_indices.rs:35`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/get_attesting_indices.rs#L35) loops every committee member with bitlist.get(i)
- [`consensus/state_processing/src/common/get_attesting_indices.rs:119`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/get_attesting_indices.rs#L119) electra path per-bit get plus HashSet collect
- ~/.cargo/git/checkouts/ethereum_ssz-ba970959eb75904b/974f78f/ssz/src/bitfield.rs:633 BitIter yields bool one bit at a time

**Sources.** [prysm#5162](https://github.com/OffchainLabs/prysm/pull/5162), [lodestar@19e243fcd](https://github.com/ChainSafe/lodestar/commit/19e243fcd355)

</details>


<a id="ssz-015"></a>
<details>
<summary><b>ssz-015</b> Enforce SSZ list limits and offsets during decode — <i>partial · medium · S · memory, cpu, bandwidth</i></summary>

**Idea.** Check offsets and type-level list limits (including progressive list limits and zero limits for forbidden lists) inside SSZ decoding, and pre-allocate only up to known maxima. Oversized or malformed gossip/RPC input is then rejected before large allocations, hashing or queuing.

**Gap in Lighthouse.** Type-level limits are missing for Gloas ExecutionRequestsGloas.deposits (should use E::MaxDepositRequestsPerPayload), AttestationGloas.aggregation_bits (ProgressiveBitList, lodestar#10042 bounds it by validators-per-slot), and ProgressiveTransactions / BlockAccessList. These decode on gossip/RPC with only the gossip message-size cap as a bound.

**Impact.** Robustness/DoS: oversized envelopes or aggregates are rejected only later in validation or state transition, not at decode; no steady-state throughput gain.

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/ssz_types-19f835ca387d51e3/8955d22/src/progressive_variable_list.rs:20-24,141-154 non-zero N enforced on decode and preallocation capped; default U0 means no limit
- [`consensus/types/src/block/beacon_block_body.rs:148-188`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/block/beacon_block_body.rs#L148-L188) Gloas body operation lists carry type-level limits
- [`consensus/types/src/execution/execution_requests.rs:88`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/execution/execution_requests.rs#L88) Gloas ExecutionRequests.deposits: ProgressiveVariableList&lt;DepositRequest&gt; with no limit (MaxDepositRequestsPerPayload exists at eth_spec.rs:165)
- [`consensus/types/src/attestation/attestation.rs:88`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/attestation/attestation.rs#L88) Gloas aggregation_bits: ProgressiveBitList with no limit
- [`consensus/types/src/execution/execution_payload.rs:26`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/execution/execution_payload.rs#L26),33 ProgressiveTransactions and BlockAccessList unbounded

**Skeptic check.** The ssz_types mechanism and most Gloas block body lists are bounded, as earlier evidence said, but the earlier gap missed the unbounded deposit requests list in the envelope. Lodestar#10042 also bounds attestation bits, so this is partial rather than implemented.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lighthouse#974](https://github.com/sigp/lighthouse/pull/974), [teku#11263](https://github.com/Consensys-Incorporated/teku/pull/11263), [lighthouse#10098](https://github.com/sigp/lighthouse/pull/10098), [lodestar#10042](https://github.com/ChainSafe/lodestar/pull/10042), [lighthouse#10106](https://github.com/sigp/lighthouse/pull/10106), [lodestar#10080](https://github.com/ChainSafe/lodestar/pull/10080)

</details>


<a id="ssz-016"></a>
<details>
<summary><b>ssz-016</b> Bulk-convert tree-backed bitlist to flat bitlist — <i>n/a · low · S · cpu</i></summary>

**Idea.** Convert a tree-backed bitlist to a flat bitlist by serializing its leaf nodes in bulk instead of reading each bit through a tree lookup.

**Impact.** Lighthouse never holds bitlists in the milhouse tree, so there is no tree-to-flat conversion to speed up.

**Best measured result.** fromNewListView 2514 -&gt; 40462 ops/s; fromCachedListView 19158 -&gt; 42554 ops/s (pr:teku#3413)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:554`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L554) state has no tree-backed bitlists; participation is List&lt;u8&gt;, justification_bits is a flat BitVector
- attestation bitfields use flat ssz_types BitList

**Sources.** [teku#3413](https://github.com/Consensys-Incorporated/teku/pull/3413)

</details>


<a id="ssz-017"></a>
<details>
<summary><b>ssz-017</b> Bulk memcpy for byte-vector and byte-list SSZ — <i>partial · low · S · cpu</i></summary>

**Idea.** Specialize SSZ encode and decode of byte lists, byte vectors and root vectors to copy the whole byte range in one operation after a length check, instead of the generic per-element path. Byte-heavy types (blocks, blob sidecars) decode several times faster.

**Gap in Lighthouse.** Decode of byte vectors/lists is already one memcpy. Encode of FixedVector&lt;u8,N&gt; and VariableList&lt;u8,N&gt; (blobs, cells, transactions) still appends byte by byte after a reserve. In ssz_types FixedVector::ssz_append and ethereum_ssz Vec&lt;T&gt;::ssz_append add a TypeId==u8 branch using extend_from_slice.

**Impact.** Cheaper SSZ encode of blob sidecars, cells and payloads for req/resp, publish and DB writes; a few x on those encodes but small in total node time.

**Best measured result.** SignedBeaconBlock decoding roughly 5x faster; BlobSidecar roughly 20x faster (commit:grandine@933a1a670861)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/registry/src/*/ssz_types-0.14.1/src/fixed_vector.rs:306-325 FixedVector&lt;u8&gt; decode does bytes.to_vec() after length check
- ~/.cargo/registry/src/*/ssz_types-0.14.1/src/variable_list.rs:309-325 same for VariableList&lt;u8&gt;
- ~/.cargo/registry/src/*/ssz_types-0.14.1/src/fixed_vector.rs:237-243 encode loops item.ssz_append per byte
- ~/.cargo/registry/src/*/ethereum_ssz-0.10.4/src/encode/impls.rs:316-327 Vec&lt;T&gt; encode is per-element
- [`consensus/types/src/data/mod.rs:32`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/data/mod.rs#L32) Blob = FixedVector&lt;u8, BytesPerBlob&gt;

**Sources.** [lodestar@27542ad2a](https://github.com/ChainSafe/lodestar/commit/27542ad2af40), [prysm#16483](https://github.com/OffchainLabs/prysm/pull/16483), [grandine@933a1a670](https://github.com/grandinetech/grandine/commit/933a1a670861), [grandine#167](https://github.com/grandinetech/grandine/pull/167)

</details>


<a id="ssz-018"></a>
<details>
<summary><b>ssz-018</b> Faster snappy implementation for gossip and database — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Use a fast snappy compressor/decompressor (bulk memory copies, optimized library) for gossip, req/resp, database and era files.

**Impact.** Nothing to gain: the Nimbus fix replaced a slow Nim snappy; Lighthouse already uses the optimized Rust snap crate on gossip and RPC, and zstd in the DB.

**Best measured result.** 3x snappy compression; ~100 ms saved per state write (pr:nimbus#3234)

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.lock snap 1.1.2 (native Rust snappy)
- [`beacon_node/lighthouse_network/src/types/pubsub.rs:6`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L6),136-152 gossip uses snap::raw Decoder/Encoder, compress_vec presizes output
- [`beacon_node/lighthouse_network/src/rpc/codec.rs:8-9`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L8-L9),183-187 req/resp uses snap FrameDecoder/FrameEncoder with a presized decode buffer
- [`beacon_node/store/src/hot_cold_store.rs:2151-2152`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2151-L2152) DB values use zstd, not snappy

**Skeptic check.** Confirmed snap is the only snappy implementation on the gossip and RPC paths and the store uses zstd. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#3234](https://github.com/status-im/nimbus-eth2/pull/3234), [nimbus#3564](https://github.com/status-im/nimbus-eth2/pull/3564)

</details>


<a id="ssz-019"></a>
<details>
<summary><b>ssz-019</b> In-order leaf traversal instead of per-index lookups — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** When reading all elements of a large tree-backed list or byte list, walk the leaves in one in-order traversal (copying whole 32-byte chunks) instead of one root-to-leaf lookup per index. This avoids re-traversing shared path nodes.

**Impact.** Small: state lists are already iterated in order. The large byte lists the Teku fix targets (payload transactions) are Vec-backed ssz_types in Lighthouse, not trees.

**Best measured result.** 1 MiB byte list 10.3 ms -&gt; 0.51 ms; 17.5% of samples in a Sepolia backfill profile were this chain (pr:teku#11485)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/iter.rs:6-100 Iter keeps a node stack and walks leaves in order, popping only the subtrees it has finished
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/list.rs:122-137 List::iter / iter_from use it
- [`consensus/state_processing/src/per_block_processing/withdrawals.rs:275-283`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/withdrawals.rs#L275-L283) withdrawal sweep uses per-index get_validator, but it stops after max_withdrawals_per_payload hits, so it is short on mainnet

**Skeptic check.** Verified the milhouse Iter does one in-order traversal. The only per-index full-list walk found is the withdrawal sweep, which exits early in practice. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#11485](https://github.com/Consensys-Incorporated/teku/pull/11485), [lodestar@eedeb5f49](https://github.com/ChainSafe/lodestar/commit/eedeb5f492e9)

</details>


<a id="ssz-020"></a>
<details>
<summary><b>ssz-020</b> Bulk memcpy for uint list serialization — <i>not · low · M · cpu</i></summary>

**Idea.** On little-endian targets, serialize and deserialize fixed-size uint lists and vectors (e.g. balances) with one bulk memory copy instead of per-element integer encoding.

**Gap in Lighthouse.** Milhouse List/Vector ssz_append and from_ssz_bytes would need a fast path for packed u64 leaves (copy leaf bytes directly on little-endian); balances and inactivity scores are the targets.

**Impact.** Full-state SSZ encode/decode (checkpoint sync, state API, hdiff snapshots) of balances/inactivity_scores would be several times cheaper; not on the per-block hot path.

**Evidence (Lighthouse @ 928b61e719).**

- milhouse-0.9.0/src/list.rs:449 ssz_append loops item.ssz_append per element
- milhouse-0.9.0/src/list.rs:513 decode via chunks().map(from_ssz_bytes)
- ethereum_ssz-0.10.4/src/encode/impls.rs:28 per-int extend_from_slice(to_le_bytes)

**Sources.** [lodestar@5f9f88920](https://github.com/ChainSafe/lodestar/commit/5f9f88920559)

</details>


<a id="ssz-021"></a>
<details>
<summary><b>ssz-021</b> Pack multiple elements into one tree leaf node — <i>not · medium · L · memory, cpu, disk</i></summary>

**Idea.** Group several list elements (e.g. 256 validators) into one tree node holding their serialized bytes, in memory and in the tree storage format. This cuts per-node memory, allocation and traversal cost for large, rarely changing lists.

**Gap in Lighthouse.** Milhouse needs a multi-element leaf for composite items (e.g. 256 validators as serialized bytes with lazy decode); this is a redesign of List&lt;Validator&gt; access.

**Impact.** Lower memory and traversal cost for the ~1M-validator tree; Arc sharing across states already removes most duplicate memory.

**Best measured result.** backing tree for 100K validators drops from ~66Mb to ~14Mb (pr:teku#3347)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/validator/validator.rs:21`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/validator/validator.rs#L21) Validator is a container stored as one Leaf per element
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/leaf.rs:9 Leaf holds a single value
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/packed_leaf.rs:10 PackedLeaf&lt;T&gt; packs only values that fit in one 32-byte chunk (basic types)

**Second check.** Re-checked the locked git milhouse rev, including the new progressive_list/progressive_tree files; packing is still limited to basic types.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [grandine#986](https://github.com/grandinetech/grandine/pull/986), [teku#3347](https://github.com/Consensys-Incorporated/teku/pull/3347), [teku#4334](https://github.com/Consensys-Incorporated/teku/pull/4334)

</details>


<a id="ssz-022"></a>
<details>
<summary><b>ssz-022</b> Cache hash roots of large state lists — <i>implemented · high · S · cpu</i></summary>

**Idea.** Cache the merkle tree of large SSZ lists and vectors in the beacon state so each state hash only rehashes the changed chunks.

**Impact.** Already realised: state hashing only rehashes dirty subtrees.

**Best measured result.** 5x block processing speed; apply block avg 131ms to 28ms (pr:nimbus#1084)

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.lock:6570 milhouse 0.9.0
- ~/.cargo/git/checkouts/milhouse-*/d67aabd/src/list.rs:41 ListInner holds Arc&lt;Tree&lt;T&gt;&gt; with cached node hashes
- [`consensus/types/src/state/beacon_state.rs:81-82`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L81-L82) validators/balances are milhouse lists (also pre-Gloas List/Vector fields)

**Skeptic check.** BeaconState large lists are milhouse persistent trees with cached hashes, which is the idea. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#1084](https://github.com/status-im/nimbus-eth2/pull/1084), [prysm#3814](https://github.com/OffchainLabs/prysm/pull/3814)

</details>


<a id="ssz-023"></a>
<details>
<summary><b>ssz-023</b> Cache constant empty-container hash root — <i>not · low · S · cpu</i></summary>

**Idea.** Cache the hash tree root of an empty execution-requests container as a constant instead of recomputing it at fork upgrade or for empty bids.

**Gap in Lighthouse.** Replace the default().tree_hash_root() calls with a lazily computed static constant.

**Impact.** Saves microseconds once per fork upgrade; negligible.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/upgrade/gloas.rs:135`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/upgrade/gloas.rs#L135) ExecutionRequestsGloas::default().tree_hash_root() computed at upgrade
- [`consensus/types/src/execution/execution_requests.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/execution/execution_requests.rs) no cached empty root

**Sources.** [prysm#16725](https://github.com/OffchainLabs/prysm/pull/16725)

</details>


<a id="ssz-024"></a>
<details>
<summary><b>ssz-024</b> Cache last tree path for sequential access — <i>partial · low · M · cpu</i></summary>

**Idea.** When accessing nearby elements of a tree-backed list, cache the last accessed leaf or root-to-leaf path and restart descent from the nearest common ancestor instead of the root.

**Gap in Lighthouse.** Sequential full scans are covered by Iter, but nearby get(i) calls have no cached last path and descend from the root each time (depth ~20 for validators). Add a cursor or cached last-leaf path to milhouse List::get and use it in loops calling validators().get(i)/balances().get(i).

**Impact.** Less tree descent for adjacent indexed gets; most hot loops already use iter/iter_cow so gain on a mainnet node is probably small.

**Best measured result.** iterateBeaconStateParticipationFlags 4.8 -&gt; 21.8 ops/s (36.5 with follow-up) (pr:teku#5611)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/registry/src/*/milhouse-0.9.0/src/tree.rs:85-104 get_recursive always descends from the root
- ~/.cargo/registry/src/*/milhouse-0.9.0/src/interface.rs:64-66 Interface::get: updates map then backing.get, no path cache
- ~/.cargo/registry/src/*/milhouse-0.9.0/src/iter.rs:6-100 Iter covers sequential scans

**Sources.** [teku#5611](https://github.com/Consensys-Incorporated/teku/pull/5611), [teku#9090](https://github.com/Consensys-Incorporated/teku/pull/9090)

</details>


<a id="ssz-025"></a>
<details>
<summary><b>ssz-025</b> Compile-time generalized index constants — <i>implemented · low · S · cpu</i></summary>

**Idea.** Derive generalized index constants for proofs at compile time from the type definitions instead of computing them at runtime.

**Impact.** None; gindices are compile-time constants.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/block/beacon_block_body.rs:58`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/block/beacon_block_body.rs#L58) BLOB_KZG_COMMITMENTS_INDEX const
- [`consensus/types/src/light_client/consts.rs:10-43`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/light_client/consts.rs#L10-L43) light client gindices as constants
- [`consensus/types/src/data/data_column_sidecar.rs:285-295`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/data/data_column_sidecar.rs#L285-L295) verify_inclusion_proof uses constant index and type-level depth

**Skeptic check.** Verified all proof gindices (blob commitments, light client) are hard-coded consts and depths come from typenum. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#8210](https://github.com/status-im/nimbus-eth2/pull/8210)

</details>


<a id="ssz-026"></a>
<details>
<summary><b>ssz-026</b> Compute data column inclusion proof once per block — <i>implemented · medium · S · cpu</i></summary>

**Idea.** Compute the KZG commitments inclusion proof once per block and reuse it for every data column sidecar, instead of once per sidecar.

**Impact.** Proof computed once per block and cloned per column on production, EL-blob and reconstruction paths.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/kzg_utils.rs:318-326`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L318-L326) blobs_to_data_column_sidecars computes kzg_commitments_merkle_proof once and passes it to build_data_column_sidecars_fulu
- [`beacon_node/beacon_chain/src/kzg_utils.rs:927-931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L927-L931) reconstruction reuses first_column.kzg_commitments_inclusion_proof
- [`beacon_node/beacon_chain/src/builder.rs:1540`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L1540) checkpoint path computes once
- [`consensus/types/src/data/partial_data_column_sidecar.rs:328`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/data/partial_data_column_sidecar.rs#L328) partial header computes once; blob_sidecar.rs:152 new_with_existing_proof reuses it

**Skeptic check.** Checked every caller of kzg_commitments_merkle_proof; none is per column. Gloas sidecars carry no inclusion proof. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#8230](https://github.com/status-im/nimbus-eth2/pull/8230)

</details>


<a id="ssz-027"></a>
<details>
<summary><b>ssz-027</b> Flat buffer for execution payload transactions — <i>not · low · L · memory, cpu, latency</i></summary>

**Idea.** Store execution payload transactions as one flat byte buffer plus offsets that mirror the SSZ layout, instead of one heap object per transaction. Decode does two allocations instead of N+1 and hashing reads from the buffer.

**Gap in Lighthouse.** Change Transactions to a flat byte buffer plus offsets type with SSZ/tree-hash/serde impls, and update the execution_layer and payload code paths that index transactions.

**Impact.** Block SSZ decode about 15% faster (about 0.5 ms of ~3.5 ms) and N+1 fewer allocations per block; lower memory for cached blocks.

**Best measured result.** 1M transactions in 4MB could exceed 200MB when deserialized (pr:lodestar#10399)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/execution/execution_payload.rs:20`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/execution/execution_payload.rs#L20) Transactions&lt;E&gt; is still VariableList&lt;VariableList&lt;u8&gt;&gt;
- pr:lighthouse#6609 is CLOSED unmerged (stale)

**Sources.** [lodestar#10399](https://github.com/ChainSafe/lodestar/pull/10399), [lodestar#10392](https://github.com/ChainSafe/lodestar/pull/10392), [lighthouse#6609](https://github.com/sigp/lighthouse/pull/6609), [prysm#17584](https://github.com/OffchainLabs/prysm/pull/17584)

</details>


<a id="ssz-028"></a>
<details>
<summary><b>ssz-028</b> SSZ library bump with upstream perf change — <i>n/a · low · cpu</i></summary>

**Idea.** Upgrade the SSZ library to pick up an upstream performance change (mechanism not shown in the record).

**Impact.** Lodestar-specific library bump with no recorded mechanism; Lighthouse tracks its own ssz crates.

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.lock ethereum_ssz 0.10.4, ssz_types 0.14.1 git rev 8955d22

**Sources.** [lodestar#9890](https://github.com/ChainSafe/lodestar/pull/9890)

</details>


<a id="ssz-029"></a>
<details>
<summary><b>ssz-029</b> Deserialize SSZ bytes directly into tree-backed values — <i>partial · medium · M · cpu, memory, startup, latency</i></summary>

**Idea.** Build tree-backed SSZ values (states, blocks, lists) directly from serialized bytes, creating leaf and packed nodes from byte ranges, instead of deserializing into an intermediate structural object and converting it. Hash caches stay lazy.

**Gap in Lighthouse.** No byte-range builder: every element goes through T::from_ssz_bytes and an allocation per leaf, and the hdiff load path goes through an intermediate Vec. A direct bytes-to-PackedLeaf builder for basic-type lists would skip per-element decode.

**Impact.** Faster state load from DB, checkpoint sync and SSZ HTTP; the validators list dominates, so the gain is limited without ssz-021.

**Best measured result.** 100K validators BeaconState deserialized almost 1000x faster: ~2-4ms instead of 2-3sec (pr:teku#3382)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/list.rs:502 List::from_ssz_bytes decodes each fixed-size item, then List::try_from_iter
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/builder.rs:5 bottom-up Builder builds the tree once, with lazy hashes
- [`beacon_node/store/src/hdiff.rs:212`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L212) HDiffBuffer::as_state decodes the state, then rebuilds balances/validators lists from Vecs (an intermediate structural form)

**Second check.** Confirmed on the locked git milhouse rev and also checked the hdiff state reconstruction path, which uses intermediate Vecs and does not decode directly into tree nodes.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [lodestar@8a002f841](https://github.com/ChainSafe/lodestar/commit/8a002f841e8f), [lodestar@c1197625b](https://github.com/ChainSafe/lodestar/commit/c1197625bc8a), [lodestar@2dea29be8](https://github.com/ChainSafe/lodestar/commit/2dea29be8db6), [teku#3382](https://github.com/Consensys-Incorporated/teku/pull/3382)

</details>


<a id="ssz-030"></a>
<details>
<summary><b>ssz-030</b> Clone bitfields with native buffer copy — <i>implemented · low · S · cpu</i></summary>

**Idea.** Clone bitlists and bitvectors with a direct buffer copy instead of a serialize then deserialize round trip.

**Impact.** None; clone is a native buffer copy.

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/ethereum_ssz-ba970959eb75904b/974f78f/ssz/src/bitfield.rs:116-118 Bitfield derives Clone over SmallVec&lt;[u8; N]&gt; bytes

**Skeptic check.** Bitfield clone is a derived byte buffer copy with no serialize round trip. Earlier evidence pointed at the registry copy, but the git checkout used by Lighthouse is the same.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@c777304a1](https://github.com/ChainSafe/lodestar/commit/c777304a1bbd)

</details>


<a id="ssz-031"></a>
<details>
<summary><b>ssz-031</b> Build merkle trees bottom-up without intermediate copies — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Build list, vector and bitlist trees directly bottom-up from element or packed leaf nodes using index ranges, without a writable intermediate copy, sublist views or serialize/deserialize round trips.

**Impact.** None left: state decode and list construction build trees bottom-up directly, and bitlists/bitvectors never become trees.

**Best measured result.** createBitlistAndSerialize 4.43x (2.57M to 11.4M ops/s), alloc -47%; HashTreeRoot 3.38x (pr:teku#10343)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/builder.rs:39-73 Builder::push packs values into PackedLeaf and folds nodes bottom-up on a stack
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/list.rs:84-104 List::builder / try_from_iter use Builder (the push-based path is only the test-only try_from_iter_slow)
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/list.rs:502-531 from_ssz_bytes streams chunks into try_from_iter
- ~/.cargo/git/checkouts/tree_hash-f96cb869d9a8a64f/e5ea187/tree_hash/src/impls.rs:175-185 bitfields are hashed from bytes with MerkleHasher, no tree

**Skeptic check.** Confirmed that the Builder is a direct bottom-up fold with no writable intermediate copy, and that decode uses it. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#10343](https://github.com/Consensys-Incorporated/teku/pull/10343), [teku#9088](https://github.com/Consensys-Incorporated/teku/pull/9088), [teku#10351](https://github.com/Consensys-Incorporated/teku/pull/10351), [teku#10839](https://github.com/Consensys-Incorporated/teku/pull/10839)

</details>


<a id="ssz-032"></a>
<details>
<summary><b>ssz-032</b> DataView without explicit length in offset tables — <i>n/a · low · S · cpu</i></summary>

**Idea.** Create DataViews over the buffer without an explicit length argument when reading or writing SSZ offset tables, avoiding a bounds computation per view.

**Impact.** None; no such per-view bounds cost in Rust.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/validator/validator.rs:19`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/validator/validator.rs#L19) - derives ethereum_ssz Encode/Decode over slices
- Lighthouse is Rust; ssz offsets are read from byte slices, no DataView object.

**Sources.** [lodestar@562e42143](https://github.com/ChainSafe/lodestar/commit/562e42143a07)

</details>


<a id="ssz-033"></a>
<details>
<summary><b>ssz-033</b> Store SSZ lists as node plus length — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Represent an SSZ list as one tree node plus a length instead of an inner container wrapping a vector and a length, removing an indirection on creation and access.

**Impact.** None; list is already a tree root plus length.

**Best measured result.** SszBeaconBlockBodyBenchmark.benchCreate 36766 -&gt; 22039 us/op (pr:teku#3556)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/milhouse-*/d67aabd/src/list.rs:30-49 List wraps ListInner{tree: Arc&lt;Tree&lt;T&gt;&gt;, length, depth, packing_depth} directly

**Skeptic check.** milhouse List is a tree node plus length with no extra container node. Block body lists are plain Vec-backed VariableList. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#3556](https://github.com/Consensys-Incorporated/teku/pull/3556)

</details>


<a id="ssz-034"></a>
<details>
<summary><b>ssz-034</b> Explicit allocation and value types in SSZ decode — <i>n/a · low · S · memory</i></summary>

**Idea.** Do not allocate heap references implicitly during SSZ decoding; prefer value types and make reference allocation explicit to reduce indirection and GC garbage.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/validator/validator.rs:19`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/validator/validator.rs#L19) - plain struct derive Decode
- Rust uses value types and explicit allocation by default; no implicit heap references in SSZ decode.

**Sources.** [nimbus#943](https://github.com/status-im/nimbus-eth2/pull/943)

</details>


<a id="ssz-035"></a>
<details>
<summary><b>ssz-035</b> Generated SSZ codecs instead of reflection — <i>implemented · low · S · cpu, memory, latency</i></summary>

**Idea.** Generate type-specific SSZ marshal, unmarshal and hash-tree-root code at build time instead of using a reflection-based or protobuf path.

**Impact.** None; Rust derive macros generate type-specific codecs at compile time.

**Best measured result.** 829 ns/op -&gt; 369 ns/op (pr:prysm#5218)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/validator/validator.rs:19`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/validator/validator.rs#L19) derive Encode, Decode, TreeHash (proc-macro generated per type)

**Skeptic check.** All Lighthouse SSZ and tree hash code comes from compile-time derives. There is no reflection path. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#1165](https://github.com/OffchainLabs/prysm/pull/1165), [prysm#5218](https://github.com/OffchainLabs/prysm/pull/5218), [prysm#5070](https://github.com/OffchainLabs/prysm/pull/5070), [prysm#6102](https://github.com/OffchainLabs/prysm/pull/6102), [prysm#5121](https://github.com/OffchainLabs/prysm/pull/5121)

</details>


<a id="ssz-036"></a>
<details>
<summary><b>ssz-036</b> Fast hex encode/decode for API byte fields — <i>not · low · M · cpu, latency</i></summary>

**Idea.** Encode and decode large hex strings (blobs, blocks in JSON APIs and engine getBlobs) with an optimized hex routine into a preallocated buffer instead of a generic hex library.

**Gap in Lighthouse.** Engine JSON-RPC hex for blobs, cells and payloads uses the scalar hex crate with temporary buffers; no SIMD, no decode into a preallocated buffer. Switch ethereum_serde_utils::hex and ssz_types hex_fixed_vec/hex_var_list to const-hex (decode_to_slice into the target buffer).

**Impact.** Engine API JSON handling of blobs and cells (getBlobsV2/V3, getPayload) gets cheaper; likely tens of ms per blob-heavy block, off the critical path for most blocks.

**Best measured result.** blob hex deserialize 332.7 ms vs 1.985 ms (browser fromHexInto), fromHex 1.96 s (pr:lodestar#8275)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/registry/src/*/ethereum_serde_utils-0.8.1/src/hex.rs:6-19 encode/decode use hex 0.4, with an extra String/Vec
- ~/.cargo/registry/src/*/ssz_types-0.14.1/src/serde_utils/hex_fixed_vec.rs:9-23 encode then PrefixedHexVisitor allocs a Vec then FixedVector::new
- Cargo.toml:170 hex = "0.4"
- [`beacon_node/execution_layer/src/engine_api/json_structures.rs:97`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/json_structures.rs#L97),126,1034,1096 blob/cell/payload fields use these helpers
- const-hex 1.19.3 in Cargo.lock is only a transitive dep of alloy

**Sources.** [lodestar#8275](https://github.com/ChainSafe/lodestar/pull/8275), [grandine@bdb716dd6](https://github.com/grandinetech/grandine/commit/bdb716dd6872), [lodestar#8562](https://github.com/ChainSafe/lodestar/pull/8562)

</details>


<a id="ssz-037"></a>
<details>
<summary><b>ssz-037</b> Specialized 32-byte root equality — <i>n/a · low · S · cpu</i></summary>

**Idea.** Give roots a dedicated 32-byte type so equality uses a fast fixed-size byte comparison instead of generic byte-vector equality.

**Impact.** Roots are already a dedicated 32-byte type and compare as a fixed array; the JS generic byte-array problem does not exist in Rust.

**Best measured result.** benchmark: ssz.Root.equals 57.9us vs byteArrayEquals 1.18us (pr:lodestar#2713)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fixed_bytes`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fixed_bytes); Hash256 is alloy FixedBytes&lt;32&gt; with derived [u8;32] equality (fixed-size memcmp)

**Sources.** [lodestar#2713](https://github.com/ChainSafe/lodestar/pull/2713)

</details>


<a id="ssz-038"></a>
<details>
<summary><b>ssz-038</b> Replace SSZ library with faster implementation — <i>n/a · low · S · cpu</i></summary>

**Idea.** Replace the general SSZ library with a faster dedicated implementation for encode, decode and hashing.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/validator/validator.rs:5-6`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/validator/validator.rs#L5-L6) - ssz_derive, tree_hash_derive
- Lighthouse already uses its own dedicated ethereum_ssz, tree_hash and milhouse; no generic slow library to swap.

**Sources.** [ethlambda#242](https://github.com/lambdaclass/ethlambda/pull/242)

</details>


<a id="ssz-039"></a>
<details>
<summary><b>ssz-039</b> Faster structural-to-tree conversion — <i>n/a · low · S · cpu</i></summary>

**Idea.** Use an SSZ library version with faster conversion from structural values to tree-backed values.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/registry/src/*/milhouse-0.9.0/src/list.rs:51 - List::new from Vec
- Lodestar JS library version bump for struct-to-tree conversion; Lighthouse builds Milhouse lists directly from Vec/iter.

**Sources.** [lodestar#1287](https://github.com/ChainSafe/lodestar/pull/1287)

</details>


<a id="ssz-040"></a>
<details>
<summary><b>ssz-040</b> Fewer allocations in SSZ query path parsing — <i>n/a · low · S · cpu, memory</i></summary>

**Idea.** Parse SSZ struct tags and query paths with fewer allocations to speed up path resolution in the SSZ query code.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/validator/validator.rs:19`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/validator/validator.rs#L19) - compile-time derive, no tag parsing
- Go struct-tag SSZ query paths have no counterpart; Lighthouse has no reflection-based SSZ query code.

**Sources.** [prysm#15931](https://github.com/OffchainLabs/prysm/pull/15931), [prysm#15886](https://github.com/OffchainLabs/prysm/pull/15886)

</details>


<a id="ssz-041"></a>
<details>
<summary><b>ssz-041</b> Faster expected withdrawals via cheap list reads — <i>partial · low · S · cpu</i></summary>

**Idea.** Compute expected withdrawals without slow per-element tree reads over the validator and balance lists, using a faster SSZ access path.

**Gap in Lighthouse.** Walk validators and balances with validators().iter_from(start) and balances().iter_from(start) (wrapping once at the end) in get_validators_sweep_withdrawals, instead of get_validator/get_balance per index; keep the withdrawals-vec adjustment only when the vec is non-empty for that index.

**Impact.** Block production and block processing sweep get cheaper: 16384 O(log n) descents replaced by sequential leaf walks, likely a few ms per block; no effect on other paths.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/withdrawals.rs:249-317`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/withdrawals.rs#L249-L317) - sweep loop, bounded by max_validators_per_withdrawals_sweep=16384 (chain_spec.rs:1398)
- withdrawals.rs:285-286 - state.get_validator(i) and get_balance_after_withdrawals(i) per index
- [`consensus/types/src/state/beacon_state.rs:2408`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2408) - get_validator is validators().get(i), O(log n) tree descent
- withdrawals.rs:319 - get_balance_after_withdrawals filters the withdrawals vec per index, then get_balance tree lookup
- ~/.cargo/registry/src/*/milhouse-0.9.0/src/list.rs:128 - iter_from(index) exists for sequential cursor reads

**Sources.** [lodestar#10301](https://github.com/ChainSafe/lodestar/pull/10301)

</details>


<a id="ssz-042"></a>
<details>
<summary><b>ssz-042</b> Fixed-size arrays for 32-byte roots — <i>n/a · low · S · memory, cpu</i></summary>

**Idea.** Use fixed-size byte arrays instead of heap slices for roots and other fixed-length fields in state and message types, so they need no separate allocation and are cheaper for the GC.

**Impact.** None; Rust roots are already inline fixed arrays.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/lib.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/lib.rs): Hash256 is a [u8;32] H256 array type

**Sources.** [prysm#9352](https://github.com/OffchainLabs/prysm/pull/9352), [prysm#2769](https://github.com/OffchainLabs/prysm/pull/2769), [prysm#4427](https://github.com/OffchainLabs/prysm/pull/4427)

</details>


<a id="ssz-043"></a>
<details>
<summary><b>ssz-043</b> Fast-path decode for fixed-size containers — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** For fixed-length SSZ containers (Checkpoint, Validator, PendingAttestation), decode fields at fixed offsets directly, without the generic per-field decoder builder.

**Impact.** Already done in ethereum_ssz derive for every fixed-size container.

**Best measured result.** 25% of allocations by count were in SszDecoderBuilder for state.validators; &gt;10% for PendingAttestation (pr:lighthouse#865)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/ethereum_ssz-ba970959eb75904b/974f78f/ssz_derive/src/lib.rs:1042-1045 fixed_decodes split_at(ssz_fixed_len) per field
- ~/.cargo/git/checkouts/ethereum_ssz-ba970959eb75904b/974f78f/ssz_derive/src/lib.rs:1072-1092 from_ssz_bytes takes the fixed path when is_ssz_fixed_len, builder only in else branch
- [`consensus/types/src/validator/validator.rs:19`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/validator/validator.rs#L19) Validator derives Decode
- [`consensus/types/src/attestation/checkpoint.rs:15`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/attestation/checkpoint.rs#L15) Checkpoint derives Decode

**Skeptic check.** Verified the derive emits a direct split_at decode for fixed-size containers and uses SszDecoderBuilder only for variable-size ones. PendingAttestation is variable-size (BitList) so it still needs offsets, which is inherent; earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#865](https://github.com/sigp/lighthouse/pull/865), [lighthouse#6657](https://github.com/sigp/lighthouse/pull/6657)

</details>


<a id="ssz-044"></a>
<details>
<summary><b>ssz-044</b> Keep objects as raw SSZ bytes with accessors — <i>not · low · L · cpu, memory</i></summary>

**Idea.** Store objects (attestations, cached roots) as flat SSZ byte buffers and read fields through accessors, instead of pointer-heavy structs, avoiding SSZ to struct to SSZ conversions.

**Gap in Lighthouse.** Would need zero-copy view types over SSZ bytes for attestations and cached roots; large refactor of types crate and all consumers.

**Impact.** Saves SSZ decode and re-encode allocations only; Lighthouse already has fixed fast-path decode and inline bitfields, so gain is small.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/attestation/attestation.rs:83`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/attestation/attestation.rs#L83) Attestation is a typed struct with BitList
- [`consensus/types/src/attestation/attestation_data.rs:19`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/attestation/attestation_data.rs#L19) plain struct

**Sources.** [caplin#7512](https://github.com/erigontech/erigon/pull/7512), [caplin#7454](https://github.com/erigontech/erigon/pull/7454)

</details>


<a id="ssz-045"></a>
<details>
<summary><b>ssz-045</b> forEach over tree view without intermediate objects — <i>n/a · low · S · memory, cpu</i></summary>

**Idea.** Iterate elements of a tree-backed list with a callback that receives views directly, instead of materializing intermediate plain objects for each element.

**Impact.** Rust iterators yield references, no intermediate objects to avoid.

**Best measured result.** GC metric improved vs beta (graphs only) (pr:lodestar#7079)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs): milhouse List iterated via iter() yielding references

**Sources.** [lodestar#7079](https://github.com/ChainSafe/lodestar/pull/7079)

</details>


<a id="ssz-046"></a>
<details>
<summary><b>ssz-046</b> Height-based merkleizer — <i>partial · low · S · cpu</i></summary>

**Idea.** Compute merkle roots with a merkleizer driven by tree height instead of generic chunk-count logic, to simplify hashing work.

**Gap in Lighthouse.** Lighthouse already computes roots height by height with cached zero hashes; a separate height-keyed merkleizer would only simplify code.

**Impact.** Essentially no speedup; a simplification.

**Evidence (Lighthouse @ 928b61e719).**

- e5ea187/tree_hash/src/merkleize_padded.rs:35-125 merkleize_padded loops by tree height with zero-hash per height
- e5ea187/tree_hash/src/lib.rs MerkleHasher streaming

**Sources.** [nimbus#5717](https://github.com/status-im/nimbus-eth2/pull/5717)

</details>


<a id="ssz-047"></a>
<details>
<summary><b>ssz-047</b> Build state proofs from cached tree layers — <i>n/a · low · S · cpu, memory, latency</i></summary>

**Idea.** For merkle proofs of state fields, take the top-level part of the proof from the cached state tree layers and run the generic proof collector only on the remaining sub-path, instead of collecting from the state root.

**Impact.** Lighthouse only proves top-level fields (sync committees, finalized root) from cached field roots, so there is no deep generic state proof walk to speed up.

**Best measured result.** States generic collection from root is slow (over seconds) and memory heavy; no numbers for the PR (pr:prysm#16295)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:3885-3960`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3885-L3960) compute_*_proof build a MerkleTree over top-level field roots (get_beacon_state_leaves)

**Sources.** [prysm#16295](https://github.com/OffchainLabs/prysm/pull/16295)

</details>


<a id="ssz-048"></a>
<details>
<summary><b>ssz-048</b> Immutable SSZ value types shared by reference — <i>n/a · low · S · cpu, memory</i></summary>

**Idea.** Make small SSZ types such as AttestationData and Checkpoint immutable so they can be shared by reference, removing defensive deep copies.

**Impact.** Rust ownership and borrows remove the need for defensive copies; Checkpoint is Copy (80 bytes or less) and AttestationData is passed by reference or Arc.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/attestation/checkpoint.rs:18`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/attestation/checkpoint.rs#L18) Checkpoint is Copy
- [`consensus/types/src/attestation/attestation_data.rs:19`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/attestation/attestation_data.rs#L19) Clone with borrow semantics

**Sources.** [teku#1002](https://github.com/Consensys-Incorporated/teku/pull/1002), [teku#1058](https://github.com/Consensys-Incorporated/teku/pull/1058)

</details>


<a id="ssz-049"></a>
<details>
<summary><b>ssz-049</b> Deserialize and clone into caller-provided output — <i>n/a · low · cpu, memory</i></summary>

**Idea.** Deserialize (and clone) SSZ values in place into a caller-provided destination instead of returning a value or building an intermediate copy, which avoids copying large containers.

**Impact.** Clones of tree-backed state are O(1) Arc structural sharing and Rust moves large values without GC copies; not applicable. No measurable saving expected.

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/ethereum_ssz-ba970959eb75904b/974f78f/ssz/src/decode.rs: Decode::from_ssz_bytes returns Self, no in-place variant
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/list.rs:502: List::from_ssz_bytes builds a new tree

**Sources.** [lodestar@796095ac3](https://github.com/ChainSafe/lodestar/commit/796095ac3b43), [lodestar@ab05f74f3](https://github.com/ChainSafe/lodestar/commit/ab05f74f3ac5), [lodestar@6d01bfe64](https://github.com/ChainSafe/lodestar/commit/6d01bfe643f4), [lodestar@786eb1cab](https://github.com/ChainSafe/lodestar/commit/786eb1cabfee), [lodestar@fdff81287](https://github.com/ChainSafe/lodestar/commit/fdff81287bc0), [nimbus@d4fa2c891](https://github.com/status-im/nimbus-eth2/commit/d4fa2c891364)

</details>


<a id="ssz-050"></a>
<details>
<summary><b>ssz-050</b> Inline small-vector storage for attestation bitfields — <i>partial · low · M · memory, cpu</i></summary>

**Idea.** Store attestation bitfields inline in a small stack-allocated vector sized to typical committee sizes, so SSZ encode/decode and attestation objects need no separate heap allocation.

**Gap in Lighthouse.** The 128-byte inline buffer was sized for per-committee bitfields (pre-Electra). Since Electra, AttestationElectra.aggregation_bits spans all committees of a slot (~1M validators / 32 slots = ~31k bits = ~3.9KB), so every aggregate, block attestation and op-pool/naive-aggregation-pool attestation bitfield spills to a heap SmallVec. Only committee_bits (BitVector&lt;64&gt;) and sync-committee bits still fit inline. A 4KB inline buffer is not sensible, so the fix would be a different representation (e.g. pooled/arena buffers or a sparse form) rather than a bigger SMALLVEC_LEN.

**Impact.** One heap allocation of ~4KB per Electra attestation bitfield on gossip aggregates, block decode and op-pool clones; the original 22%-of-allocations saving no longer applies on the current fork.

**Best measured result.** heaptrack: bitfield SSZ was 22% of all allocations by count; these disappear (pr:lighthouse#3025)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/ethereum_ssz-ba970959eb75904b/974f78f/ssz/src/bitfield.rs:34 SMALLVEC_LEN = 128 bytes (1024 bits)
- ~/.cargo/git/checkouts/ethereum_ssz-ba970959eb75904b/974f78f/ssz/src/bitfield.rs:118 bytes: SmallVec&lt;[u8; SMALLVEC_LEN]&gt;
- [`consensus/types/src/attestation/attestation.rs:83`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/attestation/attestation.rs#L83) Base aggregation_bits BitList&lt;MaxValidatorsPerCommittee&gt; (fits inline)
- [`consensus/types/src/attestation/attestation.rs:85`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/attestation/attestation.rs#L85) Electra aggregation_bits BitList&lt;MaxValidatorsPerSlot&gt; (per-slot, ~30k bits on mainnet = ~3.9KB, spills to heap)
- [`consensus/types/src/attestation/attestation.rs:88`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/attestation/attestation.rs#L88) Gloas ProgressiveBitList

**Skeptic check.** The SmallVec mechanism is real but sized for the pre-Electra per-committee layout; on the current-fork hot path (Electra aggregates and block attestations) the bitfield exceeds 128 bytes and is heap-allocated. Earlier evidence found the mechanism but not that it no longer covers the hot path.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lighthouse#3025](https://github.com/sigp/lighthouse/pull/3025), [lighthouse#2935](https://github.com/sigp/lighthouse/pull/2935)

</details>


<a id="ssz-051"></a>
<details>
<summary><b>ssz-051</b> Integer gindex paths for proof descriptors — <i>not · low · M · cpu, memory</i></summary>

**Idea.** Compute merkle proof descriptors from integer generalized-index paths sorted in path order and write bits directly into the output, instead of building binary strings for each index.

**Gap in Lighthouse.** Lighthouse has no multiproof descriptor builder at all, so there is no string-based path to replace; only relevant if adding multiproofs.

**Impact.** Rare path (light-client/proof serving); no mainnet node cost.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/merkle_proof/src/lib.rs:291`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/merkle_proof/src/lib.rs#L291) generate_proof for deposit tree only; progressive_container_proof at :514
- grep for multiproof/gindex descriptor in consensus and beacon_node found no light-client multiproof descriptor builder

**Sources.** [lodestar@d4cc6b9e9](https://github.com/ChainSafe/lodestar/commit/d4cc6b9e9b75)

</details>


<a id="ssz-052"></a>
<details>
<summary><b>ssz-052</b> Avoid boxed objects for primitive SSZ values — <i>n/a · low · S · memory, cpu</i></summary>

**Idea.** Use primitive integers instead of boxed wrapper objects for slots, epochs, balances, and intern the 256 possible byte values, so reading packed uint lists (participation flags) does not allocate per element.

**Impact.** None: Rust has no boxed primitives, so no per-element allocation exists. Does not apply: Java boxed wrappers.

**Best measured result.** removes ~2*V (~2M) SszByte allocations per slot; ~1.5 GB/epoch garbage claimed (pr:teku#10859)

**Evidence (Lighthouse @ 928b61e719).**

- 258380e/ssz/src/bitfield.rs:117 Bitfield is SmallVec bytes + len, no tree
- [`consensus/types/src/state/beacon_state.rs:627`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L627) inactivity_scores List&lt;u64&gt; plain integers

**Sources.** [teku#10859](https://github.com/Consensys-Incorporated/teku/pull/10859), [teku#550](https://github.com/Consensys-Incorporated/teku/pull/550)

</details>


<a id="ssz-053"></a>
<details>
<summary><b>ssz-053</b> Lazy merkle tree for bitlists and bitvectors — <i>n/a · low · S · cpu, memory</i></summary>

**Idea.** Back bitlists and bitvectors with a plain bit structure and build their merkle tree node lazily, only when a root or proof is needed.

**Impact.** None: bitfields are flat bytes and hashed only when a root is requested. Does not apply: no eager tree exists.

**Evidence (Lighthouse @ 928b61e719).**

- 258380e/ssz/src/bitfield.rs:117 Bitfield is SmallVec bytes + len, no tree

**Sources.** [teku#3580](https://github.com/Consensys-Incorporated/teku/pull/3580), [teku#3611](https://github.com/Consensys-Incorporated/teku/pull/3611)

</details>


<a id="ssz-054"></a>
<details>
<summary><b>ssz-054</b> Memoize derived values of composite SSZ views — <i>n/a · low · S · cpu</i></summary>

**Idea.** Memoize lazily computed derived values (children lists, views) of composite SSZ containers so repeated accessors do not rebuild them.

**Impact.** None: accessors return references, no derived child lists are rebuilt. Does not apply: Java view memoization.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:516`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L516) fields are milhouse Vector/List accessed by reference

**Sources.** [teku#7748](https://github.com/Consensys-Incorporated/teku/pull/7748)

</details>


<a id="ssz-055"></a>
<details>
<summary><b>ssz-055</b> Native equality instead of serialize-and-compare — <i>implemented · low · S · cpu</i></summary>

**Idea.** Compare SSZ objects with native field equality instead of serializing both sides and comparing bytes.

**Impact.** Already uses field-wise derived equality.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/execution/execution_payload.rs:159`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/execution/execution_payload.rs#L159) educe(PartialEq) field-wise equality
- [`consensus/types/src/attestation/attestation.rs:76`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/attestation/attestation.rs#L76) educe(PartialEq) on Attestation
- [`consensus/types/src/validator/validator.rs:19`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/validator/validator.rs#L19) derive(PartialEq) on Validator

**Skeptic check.** Grepped beacon_node and consensus for as_ssz_bytes() comparisons and tree_hash_root() equality used as object equality outside tests: none found. Earlier verdict upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#271](https://github.com/ChainSafe/lodestar/pull/271)

</details>


<a id="ssz-056"></a>
<details>
<summary><b>ssz-056</b> No closure allocation in composite child access — <i>n/a · low · S · memory, cpu</i></summary>

**Idea.** Read children of composite SSZ views through the int cache without a per-get lambda or callback, so the hot child-access path allocates no closures.

**Impact.** None: Rust has no per-get closure allocation. Does not apply: Java closures.

**Best measured result.** AbstractSszComposite lambda allocs 4.08 GiB -&gt; 0; ~4.27 GiB removed in baseline profile (pr:teku#10871)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:516`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L516) plain field access

**Sources.** [teku#10871](https://github.com/Consensys-Incorporated/teku/pull/10871)

</details>


<a id="ssz-057"></a>
<details>
<summary><b>ssz-057</b> Packed word storage for bitlists and bitvectors — <i>partial · low · S · memory, cpu</i></summary>

**Idea.** Back bitlists and bitvectors with packed machine words instead of one byte or bool per bit, so popcount, intersects and set-all work on whole words and use less memory.

**Gap in Lighthouse.** Bits are already packed, but ops run per byte instead of per u64 word. Process 8-byte chunks in num_set_bits, intersection, union, difference_inplace, is_zero (ethereum_ssz Bitfield).

**Impact.** Slightly cheaper attestation aggregation and committee bit counting; bitfields are a few hundred bytes at most and LLVM may already vectorize the loops, so gain is small.

**Best measured result.** countSetBits 21M -&gt; 249M ops/s; intersects 24M -&gt; 332M ops/s (pr:teku#1531)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/ethereum_ssz-ba970959eb75904b/974f78f/ssz/src/bitfield.rs:118: Bitfield wraps SmallVec&lt;[u8;N]&gt; (bit-packed, byte granularity)
- ~/.cargo/git/checkouts/ethereum_ssz-ba970959eb75904b/974f78f/ssz/src/bitfield.rs:501: num_set_bits sums byte.count_ones per byte
- ~/.cargo/git/checkouts/ethereum_ssz-ba970959eb75904b/974f78f/ssz/src/bitfield.rs:232: intersection/union loop byte by byte

**Sources.** [teku#1531](https://github.com/Consensys-Incorporated/teku/pull/1531), [teku#1595](https://github.com/Consensys-Incorporated/teku/pull/1595)

</details>


<a id="ssz-058"></a>
<details>
<summary><b>ssz-058</b> Packed serialized node for lists of byte lists — <i>not · low · L · cpu, memory</i></summary>

**Idea.** Keep a list of byte lists (execution transactions) in a tree as one packed buffer of serialized SSZ, compute its hash root by streaming merkleization, and expand to a full tree only on read or mutation.

**Gap in Lighthouse.** Transactions are a flat Vec of per-tx byte vectors and the root is streamed from them, so there is no tree to avoid. Only the per-tx allocation remains; a contiguous buffer plus offsets type would be needed in ssz_types / ExecutionPayload.

**Impact.** Would save thousands of small allocations per block decode; small gain for large API churn.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/execution/execution_payload.rs:201`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/execution/execution_payload.rs#L201) transactions: Transactions&lt;E&gt;
- 8955d22/src/variable_list.rs:53 VariableList is a Vec&lt;T&gt; (Vec&lt;Vec&lt;u8&gt;&gt; for txs)
- 8955d22/src/tree_hash.rs:66 vec_tree_hash_root streams items through MerkleHasher

**Sources.** [teku#10946](https://github.com/Consensys-Incorporated/teku/pull/10946), [teku#10951](https://github.com/Consensys-Incorporated/teku/pull/10951)

</details>


<a id="ssz-059"></a>
<details>
<summary><b>ssz-059</b> Packed specialized collections for primitive SSZ types — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Use specialized packed collections for hot primitive types (uint8 participation flags, u64 lists, Bytes32 vectors, pubkey/signature byte vectors) instead of generic lists of boxed element views.

**Impact.** None: primitive state lists are already stored packed, and iteration yields straight from the packed value vectors.

**Best measured result.** iterateBeaconStateParticipationFlags 77.1 -&gt; 104.8 ops/s (pr:teku#5632)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/packed_leaf.rs:10-15 PackedLeaf stores Vec&lt;T&gt; of up to 32/size_of(T) basic values per leaf
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/builder.rs:47-55 basic types are packed during construction
- [`consensus/types/src/state/beacon_state.rs:592-634`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L592-L634) participation flags, inactivity scores and balances are packed milhouse lists
- [`consensus/types/src/validator/validator.rs:22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/validator/validator.rs#L22) pubkey is fixed PublicKeyBytes, not boxed

**Skeptic check.** Verified that milhouse packs basic types per leaf and that iteration reads them directly. The Teku problem (boxed element views) has no equivalent here. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#5632](https://github.com/Consensys-Incorporated/teku/pull/5632), [teku#3623](https://github.com/Consensys-Incorporated/teku/pull/3623)

</details>


<a id="ssz-060"></a>
<details>
<summary><b>ssz-060</b> Pad once when expanding byte to bits — <i>n/a · low · S · cpu</i></summary>

**Idea.** Expand a byte to bits by padding its binary representation to 8 places once, instead of building an array and pushing extra false values.

**Impact.** None: bits are read by index from packed bytes. Does not apply: JS array padding.

**Evidence (Lighthouse @ 928b61e719).**

- 258380e/ssz/src/bitfield.rs:117 Bitfield is SmallVec bytes + len, no tree

**Sources.** [lodestar@c381bbb1e](https://github.com/ChainSafe/lodestar/commit/c381bbb1ed93)

</details>


<a id="ssz-061"></a>
<details>
<summary><b>ssz-061</b> Presize serialization output buffers — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Allocate the serialization output buffer once with the exact (or upper-bound) encoded length, or use page-based buffering, so encoding a state or blob list does not grow, reallocate and copy the buffer repeatedly.

**Impact.** None left: state, block and blob serialization do one exact-size allocation, and the compression buffers are presized too.

**Best measured result.** 10 txs: 69008 -&gt; 37949 ns/op, 353 -&gt; 210 allocs; 1000 txs: 5.56ms -&gt; 3.31ms (pr:prysm#147)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/ethereum_ssz-ba970959eb75904b/974f78f/ssz/src/encode.rs:39-45 as_ssz_bytes uses Vec::with_capacity(ssz_bytes_len())
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/list.rs:447-470 List ssz_bytes_len is exact; ssz_append reserves for fixed-size items
- [`beacon_node/store/src/hot_cold_store.rs:2151`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2151),2176 zstd output buffers presized via estimate_compressed/decompressed_size
- [`beacon_node/lighthouse_network/src/rpc/codec.rs:187`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L187) RPC decode buffer presized to the declared length

**Skeptic check.** Confirmed the exact-length presizing in the ethereum_ssz default as_ssz_bytes, which the state, gossip and RPC encodes use. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#7310](https://github.com/status-im/nimbus-eth2/pull/7310), [prysm#147](https://github.com/OffchainLabs/prysm/pull/147), [ethlambda#741](https://github.com/lambdaclass/ethlambda/pull/741), [lighthouse@6a870d468](https://github.com/sigp/lighthouse/commit/6a870d468cba)

</details>


<a id="ssz-062"></a>
<details>
<summary><b>ssz-062</b> Persistent merkle tree backing for state fields — <i>implemented · high · S · cpu, memory</i></summary>

**Idea.** Back beacon state fields (including inactivity scores and the roots/randao/slashings vectors) with persistent merkle trees, so hashTreeRoot is incremental and state copies share unchanged subtrees instead of holding flat copies.

**Impact.** Incremental state hashing and structural sharing of state copies via milhouse.

**Best measured result.** hashTreeRoot 10k validators: old 3.02 ops/s, structural 3.97, tree 5,403 ops/s (pr:lodestar#625)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:11`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L11) use milhouse::{List, ProgressiveList, Vector}
- [`consensus/types/src/state/beacon_state.rs:516`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L516) block_roots Vector
- [`consensus/types/src/state/beacon_state.rs:563`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L563) randao_mixes Vector
- [`consensus/types/src/state/beacon_state.rs:568`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L568) slashings Vector
- [`consensus/types/src/state/beacon_state.rs:627`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L627) inactivity_scores List&lt;u64&gt;
- [`consensus/types/src/state/beacon_state.rs:554`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L554) balances List&lt;u64&gt;
- [`consensus/types/src/state/beacon_state.rs:718`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L718) pending_deposits List

**Skeptic check.** All large state vectors/lists (validators, balances, participation, inactivity scores, roots, randao, slashings, pending queues, historical summaries) are milhouse persistent trees; the remaining non-tree fields are small fixed containers or Arc'd sync committees. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [ethlambda#650](https://github.com/lambdaclass/ethlambda/pull/650), [lodestar#625](https://github.com/ChainSafe/lodestar/pull/625), [lodestar@08240f898](https://github.com/ChainSafe/lodestar/commit/08240f898338), [ethlambda#634](https://github.com/lambdaclass/ethlambda/pull/634)

</details>


<a id="ssz-063"></a>
<details>
<summary><b>ssz-063</b> Preallocate decode Vec from byte length — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** When SSZ-decoding a list of fixed-length items, compute the item count from the byte length and preallocate the output vector instead of growing it.

**Impact.** Consensus list types preallocate; nothing material left.

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/ssz_types-19f835ca387d51e3/8955d22/src/variable_list.rs:325-348 VariableList fixed-len decode: Vec::with_capacity(num_items)
- ~/.cargo/git/checkouts/ethereum_ssz-ba970959eb75904b/974f78f/ssz/src/decode/try_from_iter.rs:10,52 variable-length lists preallocate from size_hint, capped at 1MiB
- ~/.cargo/git/checkouts/milhouse-*/d67aabd/src/list.rs:502-528 milhouse List decode streams chunks into the tree builder (no intermediate Vec)

**Skeptic check.** Both source PRs' mechanisms are present (VariableList with_capacity, try_from_iter with_capacity). Plain Vec&lt;T&gt; fixed-len decode (ssz/src/decode/impls.rs:439-446) still uses std collect over Result with a 0 lower size_hint, but it is only used off the hot path (http_api bodies, a sync-committee branch in the store), so the verdict stands.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#3417](https://github.com/sigp/lighthouse/pull/3417), [lighthouse#1921](https://github.com/sigp/lighthouse/pull/1921)

</details>


<a id="ssz-064"></a>
<details>
<summary><b>ssz-064</b> Precompute SSZ length bounds per schema — <i>partial · low · S · cpu, memory</i></summary>

**Idea.** Compute SSZ minimum/maximum serialized length bounds once per type and reuse them for each gossip message, instead of walking the type tree per message.

**Gap in Lighthouse.** Block, blob and light-client limits are cached, but data column response limits are not: for every DataColumnsByRange/ByRoot response chunk, InboundCodec/OutboundCodec decode calls rpc_response_limits -&gt; rpc_data_column_limits -&gt; DataColumnSidecarFulu::max_size(max_blobs) and min_size(), which allocate a max-size sidecar and serialize it (~2 x 45KB+ for 21 blobs, growing with BPO). It can also rerun on each partial-read retry. Fix: compute the Fulu bounds arithmetically like DataColumnSidecarGloas::max_size, or cache per (fork, max_blobs) in ForkContext.

**Impact.** Removes ~100KB of allocation + SSZ encoding per data column response chunk during range sync and by-root lookups; small next to KZG verification but pure waste on the sync hot path.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/protocol.rs:95-126`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/protocol.rs#L95-L126) LazyLock statics for block and light-client limits
- [`beacon_node/lighthouse_network/src/rpc/codec.rs:270`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L270) rpc_response_limits computed for every response chunk decode attempt
- [`beacon_node/lighthouse_network/src/rpc/protocol.rs:637-642`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/protocol.rs#L637-L642) DataColumnsByRoot/ByRange call rpc_data_column_limits each time
- [`beacon_node/lighthouse_network/src/rpc/protocol.rs:727-754`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/protocol.rs#L727-L754) rpc_data_column_limits calls DataColumnSidecarFulu::min_size()/max_size(max_blobs)
- [`consensus/types/src/data/data_column_sidecar.rs:297-332`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/data/data_column_sidecar.rs#L297-L332) Fulu min_size/max_size build a full sidecar (max_blobs x 2048-byte cells, commitments, proofs) and SSZ-encode it just to take .len()

**Skeptic check.** Gossip uses a flat max size so no per-message walk there, and block limits are LazyLock as the earlier evidence said; but the earlier check missed that data column RPC limits are recomputed by building and encoding a full max-size sidecar per chunk.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [teku#4262](https://github.com/Consensys-Incorporated/teku/pull/4262)

</details>


<a id="ssz-065"></a>
<details>
<summary><b>ssz-065</b> Progressive SSZ merkleization for unbounded lists — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Support progressive lists and containers whose merkle tree shape does not depend on the max length, so trees are shallower and updates touch fewer nodes.

**Impact.** Spec-mandated for Gloas and already implemented with cached hashes. Not active before Gloas, and the perf effect is a spec property rather than a client choice.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:80-82`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L80-L82),592-806 Gloas validators, balances, participation, inactivity and pending_* are ProgressiveList
- [`consensus/state_processing/src/upgrade/gloas.rs:99-118`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/upgrade/gloas.rs#L99-L118) upgrade converts these lists to ProgressiveList
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/progressive_tree.rs:14-36 tree-backed progressive spine with cached hashes
- [`consensus/types/src/attestation/payload_attestation.rs:17`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/attestation/payload_attestation.rs#L17) progressive_container tree hash

**Skeptic check.** Verified ProgressiveList is a persistent milhouse tree with hash caching and that the Gloas state uses it. I rated value low because progressive merkleization is a consensus format, not an optional optimization. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#10928](https://github.com/Consensys-Incorporated/teku/pull/10928), [teku#10395](https://github.com/Consensys-Incorporated/teku/pull/10395)

</details>


<a id="ssz-066"></a>
<details>
<summary><b>ssz-066</b> Keep validator pubkeys as raw compressed bytes — <i>implemented · high · S · cpu</i></summary>

**Idea.** Store validator pubkeys as raw bytes in the state and do not decompress them during state SSZ decode.

**Impact.** State decode never decompresses pubkeys.

**Best measured result.** couple of orders of magnitude decrease in state SSZ decode time (pr:lighthouse#671)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/validator/validator.rs:22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/validator/validator.rs#L22) pubkey: PublicKeyBytes
- [`crypto/bls/src/generic_public_key_bytes.rs:20`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/generic_public_key_bytes.rs#L20) raw [u8;48] wrapper, decompress only on demand

**Skeptic check.** Validator.pubkey is PublicKeyBytes, decoded by plain byte copy; decompression happens only in the validator pubkey cache for new validators. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#671](https://github.com/sigp/lighthouse/pull/671)

</details>


<a id="ssz-067"></a>
<details>
<summary><b>ssz-067</b> Read-only single pass over tree-backed validator — <i>n/a · low · cpu, memory</i></summary>

**Idea.** Build a flat validator struct by reading all fields from the tree-backed validator in one read-only pass, instead of per-field deserializing getters.

**Gap in Lighthouse.** Validators are plain structs inside milhouse leaves, so field reads are direct memory access with no per-field tree deserialization.

**Impact.** Not applicable to Lighthouse design.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/validator/validator.rs:15-30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/validator/validator.rs#L15-L30) Validator is a plain struct stored as milhouse leaf

**Sources.** [lodestar@8b6026b6c](https://github.com/ChainSafe/lodestar/commit/8b6026b6c1c9)

</details>


<a id="ssz-068"></a>
<details>
<summary><b>ssz-068</b> Remove fork-ambiguous trial decode of attestations — <i>implemented · low · S · cpu</i></summary>

**Idea.** Do not decode attestations by trying several fork variants in turn; persist and decode with an explicit fork tag.

**Impact.** Persisted and gossiped attestations are decoded with an explicit fork, no trial decode.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/attestation/attestation.rs:675-681`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/attestation/attestation.rs#L675-L681) AttestationOnDisk enum_behaviour=union (explicit fork tag)
- [`beacon_node/operation_pool/src/persistence.rs:36`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/persistence.rs#L36),64 op pool persists AttestationOnDisk
- [`beacon_node/lighthouse_network/src/types/pubsub.rs:232-237`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L232-L237) gossip aggregates decoded by fork from topic digest

**Skeptic check.** Verified attestations are decoded by explicit union tag on disk and by fork digest on gossip. A similar trial-decode pattern remains for ExecutionPayload store items (beacon_node/store/src/impls/execution_payload.rs:44-66 tries Gloas, Fulu, Electra, ... in turn), but that is a different object and outside this idea.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#5856](https://github.com/sigp/lighthouse/pull/5856)

</details>


<a id="ssz-069"></a>
<details>
<summary><b>ssz-069</b> Zero-copy SSZ decode via input buffer views — <i>n/a · low · memory, cpu, latency</i></summary>

**Idea.** Decode SSZ (gossip messages, data column sidecars, nested fields) as views or sub-slices over the received input buffer instead of copying bytes into new allocations.

**Impact.** The idea targets GC pressure; Rust has no GC and decode is one pass over a borrowed slice. Negligible on a mainnet node.

**Best measured result.** Deserialization usually &gt;100ms due to gc; lower gc, lower epoch transition time (pr:lodestar#8626)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/ethereum_ssz-ba970959eb75904b/974f78f/ssz/src/decode.rs: from_ssz_bytes(&amp;[u8]) takes a borrowed slice and decodes into owned types
- ssz_types fixed_vector.rs:302: FixedVector&lt;u8&gt; decode is one to_vec memcpy

**Sources.** [lodestar#8628](https://github.com/ChainSafe/lodestar/pull/8628), [nimbus@8d639d9bd](https://github.com/status-im/nimbus-eth2/commit/8d639d9bd75d), [lodestar#8626](https://github.com/ChainSafe/lodestar/pull/8626), [lighthouse@6c8c4d9b1](https://github.com/sigp/lighthouse/commit/6c8c4d9b1e87)

</details>


<a id="ssz-070"></a>
<details>
<summary><b>ssz-070</b> Share backing tree when blinding/unblinding blocks — <i>n/a · low · memory, cpu</i></summary>

**Idea.** Convert between blinded and full blocks by reusing the unchanged subtrees of the backing merkle tree instead of building a new copy.

**Gap in Lighthouse.** Blocks are plain Rust structs, not merkle-tree-backed; blind/unblind moves or clones fields, and there is no backing tree to share. Cost is a payload clone at most.

**Impact.** Not applicable to Lighthouse design.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/block`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/block)/ (blocks are plain structs, BlindedPayload/FullPayload generics)

**Sources.** [teku#5677](https://github.com/Consensys-Incorporated/teku/pull/5677)

</details>


<a id="ssz-071"></a>
<details>
<summary><b>ssz-071</b> Intern validator pubkeys and cache their hash — <i>partial · medium · M · memory, cpu</i></summary>

**Idea.** Intern validator pubkeys in one shared cache so all state copies share one buffer, and cache each pubkey hash so Validator hash_tree_root and state copy are cheaper.

**Gap in Lighthouse.** Memory sharing is already in place through Arc structural sharing plus rebase_on. Still missing: a cached pubkey hash, so a modified Validator does not rehash its 48-byte pubkey (needs a custom TreeHash or a pubkey type with a hash cache).

**Impact.** Saves about one SHA256 per modified validator when its root is recomputed; small.

**Best measured result.** ~400MB memory reduction on holesky; ~14% faster state HTR (1000ms to 870ms); copy ~80ms to ~60ms (pr:nimbus#5883)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/validator/validator.rs:19`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/validator/validator.rs#L19) Validator derives TreeHash with inline PublicKeyBytes, so there is no cached pubkey hash
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/leaf.rs:9 Leaf caches the whole Validator root; Arc&lt;Validator&gt; is shared across state copies
- [`consensus/types/src/state/beacon_state.rs:3416`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3416) rebase_on makes states loaded from disk share tree nodes (and so pubkeys) with the finalized state
- [`beacon_node/store/src/hot_cold_store.rs:1988`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1988) states loaded from diffs are rebased on the finalized state at once

**Second check.** Beyond the earlier review, found that rebase_on in the store and state cache covers the interning/memory half for states loaded from disk; the hash-cache half is still absent.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [nimbus#5883](https://github.com/status-im/nimbus-eth2/pull/5883)

</details>


<a id="ssz-072"></a>
<details>
<summary><b>ssz-072</b> Serialized size from length leaf — <i>n/a · low · cpu, memory</i></summary>

**Idea.** Compute the serialized size of a fixed-element list from its length leaf times the element size, instead of materializing the list.

**Gap in Lighthouse.** Lists are materialized Vecs, so size is len times element size; the length-leaf trick applies to lazy tree-backed lists only. milhouse List also knows its len.

**Impact.** Not applicable to Lighthouse design.

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/ethereum_ssz-ba970959eb75904b/974f78f/ssz/src/encode/impls.rs:253 Vec ssz_bytes_len uses fixed item size times len
- ~/.cargo/git/checkouts/ssz_types-19f835ca387d51e3/8955d22/src/variable_list.rs:258 delegates to vec

**Sources.** [lodestar@f3dc6ff88](https://github.com/ChainSafe/lodestar/commit/f3dc6ff88d1b), [nimbus@7e846a0bc](https://github.com/status-im/nimbus-eth2/commit/7e846a0bce50)

</details>


<a id="ssz-073"></a>
<details>
<summary><b>ssz-073</b> Skip public wrappers in recursive clone/equals — <i>n/a · low · cpu</i></summary>

**Idea.** In recursive SSZ clone and equals, call the internal helpers directly for each element instead of the public entry point, avoiding per-element type resolution and wrapper overhead.

**Gap in Lighthouse.** Rust derive macros monomorphize clone/eq/ssz per type; there is no runtime type resolution or wrapper dispatch to skip.

**Impact.** Not applicable to Lighthouse design.

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.lock ethereum_ssz 0.10.4 derive macros

**Sources.** [lodestar@246919c8d](https://github.com/ChainSafe/lodestar/commit/246919c8dd8a), [lodestar#591](https://github.com/ChainSafe/lodestar/pull/591)

</details>


<a id="ssz-074"></a>
<details>
<summary><b>ssz-074</b> Skip default-init before decoding fixed-size lists — <i>implemented · low · S · cpu, startup</i></summary>

**Idea.** When deserializing a list of fixed-size elements (e.g. validators), do not pre-fill the output with default values that the decode loop overwrites, removing an extra write pass over the whole list.

**Impact.** None: no default-init pass exists in any list decode path.

**Best measured result.** full-state decode: EPYC 40.8ms -&gt; 17.5ms cold (-56%), 28.8 -&gt; 8.7ms warm (-69%); M5 8.4 -&gt; 7.1ms (commit:lodestar@0c757be3f4a3)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/list.rs:507-528 fixed-size List decode maps chunks straight into List::try_from_iter, no prefill
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/vector.rs:396-401 Vector decode reuses the List decode
- ~/.cargo/git/checkouts/ethereum_ssz-ba970959eb75904b/974f78f/ssz/src/decode/impls.rs:439-448 Vec&lt;T&gt; decode collects from chunks
- ~/.cargo/git/checkouts/ssz_types-19f835ca387d51e3/8955d22/src/fixed_vector.rs:310-321 FixedVector&lt;u8&gt; decode is a single to_vec

**Skeptic check.** Confirmed that every fixed-size list decode path streams elements without pre-filling defaults. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@0c757be3f](https://github.com/ChainSafe/lodestar/commit/0c757be3f4a3)

</details>


<a id="ssz-075"></a>
<details>
<summary><b>ssz-075</b> Skip cached-root updates when decoding SSZ — <i>implemented · low · S · cpu</i></summary>

**Idea.** When decoding SSZ into objects with cached hash roots, do not compute or refresh the cached roots on read.

**Impact.** Decode never computes roots; hashes are filled lazily on first tree_hash_root.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:813-855`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L813-L855) (all caches ssz(skip_deserializing), default empty)
- [`consensus/types/src/state/beacon_state.rs:3830-3849`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3830-L3849) (from_ssz_bytes: slot peek + plain decode)
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/list.rs:502-530 (List decode builds tree with zero hashes, no hashing)
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/packed_leaf.rs:53-78 (hash initialised to ZERO, computed lazily)

**Skeptic check.** Verified state and milhouse list decoding leave node hash slots zeroed and caches empty; earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#2795](https://github.com/status-im/nimbus-eth2/pull/2795), [nimbus@c7d4659d3](https://github.com/status-im/nimbus-eth2/commit/c7d4659d3261)

</details>


<a id="ssz-076"></a>
<details>
<summary><b>ssz-076</b> Read slot from SSZ bytes to pick fork — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Read the slot of a signed block from its fixed offset in the SSZ bytes to choose the fork schema, instead of deserializing the whole object first.

**Impact.** No trial decode across forks on DB/sync paths; gossip/RPC use the fork from topic/context bytes anyway.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/block/beacon_block.rs:133-145`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/block/beacon_block.rs#L133-L145) (slot from bytes 0..8 picks fork)
- [`consensus/types/src/block/signed_beacon_block.rs:163-180`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/block/signed_beacon_block.rs#L163-L180) (from_ssz_bytes_with passes message bytes to the fork-aware decoder)
- [`consensus/types/src/state/beacon_state.rs:3830-3849`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3830-L3849) (state slot at fixed offset)

**Skeptic check.** Confirmed the slot peek then single-fork decode for blocks and states; any_from_ssz_bytes (try-all) exists only as a slow fallback.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#7190](https://github.com/Consensys-Incorporated/teku/pull/7190)

</details>


<a id="ssz-077"></a>
<details>
<summary><b>ssz-077</b> Encode small integers into exact-size buffer — <i>n/a · low · memory, cpu</i></summary>

**Idea.** Write a small integer directly into a buffer of the exact needed size with bit shifts, instead of allocating a larger buffer and slicing.

**Impact.** Rust integers encode via to_le_bytes into the output Vec; no oversize buffer plus slicing exists to fix.

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.lock (ethereum_ssz 0.10.4)

**Sources.** [prysm#15630](https://github.com/OffchainLabs/prysm/pull/15630)

</details>


<a id="ssz-078"></a>
<details>
<summary><b>ssz-078</b> Snappy compression of SSZ on the wire — <i>implemented · low · S · bandwidth</i></summary>

**Idea.** Compress SSZ network messages with snappy on gossip and req/resp, as the p2p spec requires, to reduce bytes sent.

**Impact.** Spec-mandated compression is in place on both gossip and req/resp.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/pubsub.rs:6`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L6),135-150 (snappy raw encoder in gossipsub outbound_transform, decoder in inbound)
- [`beacon_node/lighthouse_network/src/rpc/protocol.rs:485`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/protocol.rs#L485) (ssz_snappy req/resp encoding)

**Skeptic check.** Verified the gossip DataTransform compresses every outbound message with snappy and req/resp uses ssz_snappy framing.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#3198](https://github.com/OffchainLabs/prysm/pull/3198)

</details>


<a id="ssz-079"></a>
<details>
<summary><b>ssz-079</b> Serialize state lists by concatenating leaf data — <i>partial · low · M · cpu, memory, disk</i></summary>

**Idea.** Serialize tree-backed state lists of fixed-size elements (validators, balances) by writing leaf data or a hand-written per-element encoder straight into one presized buffer, instead of generic per-element tree traversal and encoding.

**Gap in Lighthouse.** Iteration is leaf-order and the buffer is presized, but each u64 or Validator is encoded individually. Add a packed-leaf fast path in milhouse List/Vector ssz_append that copies leaf values as bytes (u64 on little-endian) in bulk.

**Impact.** State serialization for balances/participation (hot-DB and hdiff snapshots) could get a few tens of percent cheaper; the Validator list stays per-field.

**Best measured result.** roughly x20 BeaconState SSZ serialization speedup (pr:teku#3062)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/list.rs:457: ssz_append iterates items and calls item.ssz_append per element
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/iter.rs:5: Iter walks leaves with a stack (no per-element root traversal)
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/packed_leaf.rs:14: PackedLeaf::values is Vec&lt;T&gt;, not raw bytes

**Sources.** [lodestar#6563](https://github.com/ChainSafe/lodestar/pull/6563), [teku#3062](https://github.com/Consensys-Incorporated/teku/pull/3062), [teku#11486](https://github.com/Consensys-Incorporated/teku/pull/11486)

</details>


<a id="ssz-080"></a>
<details>
<summary><b>ssz-080</b> Stream tree nodes without node-ID arrays — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** Read, size and serialize tree-backed lists and containers by streaming nodes through a depth iterator, instead of allocating a temporary array of all node IDs or materialized values.

**Impact.** Encoding/sizing tree lists streams through the iterator with no intermediate node-ID or value arrays.

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/list.rs:447-470 (ssz_bytes_len: fixed-len multiply, else iterator sum; ssz_append iterates items into buf)
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/iter.rs (stack-based depth iterator over tree nodes)

**Skeptic check.** Confirmed milhouse Encode impls iterate directly; fixed-size items get O(1) length. Earlier evidence cited the registry path but the crate is a git checkout at d67aabd; content is the same.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@f16981bd9](https://github.com/ChainSafe/lodestar/commit/f16981bd9789), [lodestar@5fbb0e23a](https://github.com/ChainSafe/lodestar/commit/5fbb0e23a64c)

</details>


<a id="ssz-081"></a>
<details>
<summary><b>ssz-081</b> Streaming bounded-memory tree construction — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** Build list, bitlist and container trees incrementally from values or bytes with a streaming builder that keeps only a bounded set of completed subtree roots, instead of buffering every child node.

**Impact.** Tree construction from bytes/values is streaming with an O(depth) stack.

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/builder.rs:1-80 (Builder keeps a stack of at most depth completed subtrees, merging on push by trailing zeros)
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/list.rs:88,502-530 (try_from_iter and fixed-len decode feed the Builder from a chunk iterator)

**Skeptic check.** Verified Builder::push folds completed left subtrees so the stack stays bounded; only variable-length item decode (ssz::decode_list_of_variable_length_items) collects into a Vec first, which is minor.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@41fa6dde7](https://github.com/ChainSafe/lodestar/commit/41fa6dde7d56)

</details>


<a id="ssz-082"></a>
<details>
<summary><b>ssz-082</b> Tree-backed bitfields with packed chunks — <i>n/a · low · memory, cpu</i></summary>

**Idea.** Store bitlists and bitvectors as packed chunks in a merkle tree backing, so they hash incrementally and share structure, instead of boolean arrays.

**Impact.** The large per-validator arrays are already packed milhouse leaves; the remaining bitfields (attestation aggregation bits, sync bits, justification bits) are small, so tree backing would not pay off.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs) (participation lists are milhouse packed List&lt;ParticipationFlags&gt;; justification_bits is a tiny BitVector)
- ssz_types-0.14.1 (BitList/BitVector are byte-backed)

**Sources.** [lodestar@999d02928](https://github.com/ChainSafe/lodestar/commit/999d029283a4)

</details>


<a id="ssz-083"></a>
<details>
<summary><b>ssz-083</b> Convert block to tree-backed once before transition — <i>partial · low · S · cpu</i></summary>

**Idea.** Convert the incoming block to a tree-backed SSZ value once before the state transition, so repeated hash-tree-root calls on the block and its parts reuse cached hashes.

**Gap in Lighthouse.** The block root is hashed once and cached, but body_root() is hashed again in temporary_block_header() for process_block_header, so the body is hashed twice. Lighthouse has no tree-backed block to share hashes. Compute the body root once (e.g. in the ConsensusContext or when the block root is computed from a header with body_root) and build the block root from the header, then reuse it in process_block_header/temporary_block_header.

**Impact.** Saves one body hash-tree-root per block import (roughly sub-millisecond to a couple ms, mostly the transactions list); small.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/consensus_context.rs:119-136`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/consensus_context.rs#L119-L136) (block root cached once in ConsensusContext)
- [`consensus/state_processing/src/per_block_processing.rs:168-174`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing.rs#L168-L174) (temporary_block_header)
- [`consensus/types/src/block/beacon_block.rs:278-283`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/block/beacon_block.rs#L278-L283),291-307 (body_root re-hashes the whole body)

**Sources.** [lodestar@66349e773](https://github.com/ChainSafe/lodestar/commit/66349e7733f9)

</details>


<a id="ssz-084"></a>
<details>
<summary><b>ssz-084</b> Tree-backed containers with caches for heavy members — <i>n/a · low · cpu, memory</i></summary>

**Idea.** Represent containers as backing trees with per-container caches for heavy members (signature, pubkey, bitlist), so serialization walks leaves and reuses data without re-encoding.

**Impact.** Lighthouse blocks and attestations are plain structs, not tree-backed views, so there is no tree-to-bytes re-encoding to cache.

**Best measured result.** BeaconBlockBody benchSerialize 357 -&gt; 59 usec/op; Attestation benchDeserializeAndSerialize 64.8 -&gt; 8.8 usec/op (pr:teku#3426)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:96`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L96) plain struct state
- [`consensus/types/src/validator/validator.rs:19`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/validator/validator.rs#L19) plain SSZ derive

**Sources.** [teku#3426](https://github.com/Consensys-Incorporated/teku/pull/3426)

</details>


<a id="ssz-085"></a>
<details>
<summary><b>ssz-085</b> Validator list type with batch hashing — <i>not · low · L · cpu, memory</i></summary>

**Idea.** Model the validator list as a dedicated type whose view batch-hashes only changed validators into preallocated buffers.

**Gap in Lighthouse.** Milhouse already rehashes only changed validators, but one container at a time via MerkleHasher. A batched path would need a Validator-specific tree_hash_root in tree_hash or milhouse using multi-buffer hashing.

**Impact.** Marginal: only changed validators are rehashed per slot, so the batch gain is a small part of state-root cost.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/validator/validator.rs:19`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/validator/validator.rs#L19) derive(TreeHash)
- tree_hash_derive-0.12.1/src/lib.rs:131 one MerkleHasher per container
- milhouse d67aabd src/tree.rs:507 only leaves with zero cached hash are rehashed

**Sources.** [lodestar#7622](https://github.com/ChainSafe/lodestar/pull/7622)

</details>


<a id="ssz-086"></a>
<details>
<summary><b>ssz-086</b> Read bitlists through tree view without copy — <i>n/a · low · cpu, memory</i></summary>

**Idea.** Read bitlist bits straight from the tree-backed structure through a view instead of copying the bitlist data out first.

**Impact.** Lighthouse bitlists live in plain structs (attestations) and are read in place; the state holds no bitlist list in a tree that needs copying out.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/attestation/attestation.rs:280`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/attestation/attestation.rs#L280) get_aggregation_bit reads the in-memory bitfield directly

**Sources.** [teku#3391](https://github.com/Consensys-Incorporated/teku/pull/3391)

</details>


<a id="ssz-087"></a>
<details>
<summary><b>ssz-087</b> Send builder validator registrations as SSZ — <i>not · low · S · bandwidth</i></summary>

**Idea.** Derive SSZ encode/decode for signed validator registrations and send them to the builder in SSZ instead of JSON. Payloads are smaller and serialization is cheaper.

**Gap in Lighthouse.** Add an SSZ post path (as_ssz_bytes of the Vec, Content-Type octet-stream) in post_builder_validators with fallback to JSON when the relay rejects it.

**Impact.** Registrations are sent once per epoch for all validators; SSZ shrinks payload and serialization, helpful only for nodes with many validators using builders.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/builder_client/src/pre_gloas_builder_http_client.rs:244-259`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/builder_client/src/pre_gloas_builder_http_client.rs#L244-L259) post_builder_validators uses post_generic (JSON)
- [`beacon_node/builder_client/src/pre_gloas_builder_http_client.rs:269`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/builder_client/src/pre_gloas_builder_http_client.rs#L269) blinded blocks v2 does use SSZ

**Sources.** [lighthouse#7081](https://github.com/sigp/lighthouse/pull/7081)

</details>


<a id="ssz-088"></a>
<details>
<summary><b>ssz-088</b> Shared singleton instances for common integer constants — <i>n/a · low · cpu, memory</i></summary>

**Idea.** Return shared cached instances for common uint64 values (zero, 32 ETH in gwei, max) from the value factory instead of allocating a new object each time.

**Impact.** Rust u64 is a plain value; no allocation per integer, nothing to cache.

**Evidence (Lighthouse @ 928b61e719).**

- milhouse-0.9.0/src/packed_leaf.rs: integers packed inline in leaves, no boxed values

**Sources.** [teku#7375](https://github.com/Consensys-Incorporated/teku/pull/7375)

</details>


<a id="ssz-089"></a>
<details>
<summary><b>ssz-089</b> Direct byte-order primitives for SSZ integer conversion — <i>n/a · low · cpu</i></summary>

**Idea.** Convert integers to and from little-endian SSZ bytes with direct byte-order primitives instead of copying into an aligned temporary buffer and calling a generic swap. This removes a copy per integer in decode and hash paths.

**Impact.** Already compiled to direct loads/stores.

**Evidence (Lighthouse @ 928b61e719).**

- Rust ssz uses to_le_bytes/from_le_bytes natively (ethereum_ssz); no aligned temp buffer + generic swap

**Sources.** [nimbus@7902d070c](https://github.com/status-im/nimbus-eth2/commit/7902d070cd66)

</details>


<a id="ssz-090"></a>
<details>
<summary><b>ssz-090</b> Early return for already-parsed SSZ types — <i>n/a · low · cpu</i></summary>

**Idea.** In SSZ type resolution, return at once when the type is already in fully parsed form, before string and array checks, so repeated serialize and hash calls skip re-parsing.

**Impact.** No runtime SSZ type resolution exists.

**Evidence (Lighthouse @ 928b61e719).**

- Types are static Rust generics resolved at compile time; no runtime type parsing

**Sources.** [lodestar@0ec8568f9](https://github.com/ChainSafe/lodestar/commit/0ec8568f9aed)

</details>


<a id="ssz-091"></a>
<details>
<summary><b>ssz-091</b> Ordered map for pending child changes in mutable SSZ — <i>implemented · low · S · cpu</i></summary>

**Idea.** Track pending child changes of a mutable SSZ container in an index-ordered map instead of a hash map, so committing the changes needs no sort. This speeds state mutation during epoch processing.

**Impact.** Milhouse pending updates are held in an index-ordered VecMap, so commit needs no sort.

**Best measured result.** pr:teku#5348: epoch transition 26.840 -&gt; 28.711 ops/s (32768 validators)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/milhouse-0.9.0/src/update_map.rs:101 UpdateMap impl for VecMap (index-ordered)
- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/milhouse-0.9.0/src/list.rs:30 List default U = MaxMap&lt;VecMap&lt;T&gt;&gt;
- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/milhouse-0.9.0/src/list.rs:184 apply_updates

**Skeptic check.** Verified the default update map for milhouse List is VecMap wrapped in MaxMap; iteration is index-ordered by construction. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#5348](https://github.com/Consensys-Incorporated/teku/pull/5348)

</details>


<a id="ssz-092"></a>
<details>
<summary><b>ssz-092</b> Value range loops in generated hash-tree-root code — <i>n/a · low · cpu</i></summary>

**Idea.** In generated hash-tree-root code, iterate list elements with a value range loop instead of an incrementing index, removing per-iteration bounds checks and indexing.

**Impact.** Rust iterators already elide bounds checks; tree hashing is in tree_hash/milhouse.

**Best measured result.** pr:prysm#9867: "research indicates is more performant, so it should not cause any slowdown in HTR computations" (no numbers)

**Evidence (Lighthouse @ 928b61e719).**

- Rust iterators over slices/lists; no generated htr code with indexed loops

**Sources.** [prysm#9867](https://github.com/OffchainLabs/prysm/pull/9867)

</details>


