# ssz

23 ideas: 4 not, 6 partial, 8 implemented, 5 n/a; 4 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

Ids missing from the sequence are ideas that have not been checked against Lighthouse yet.

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [ssz-004](#ssz-004) | Compare against precomputed default for is-default checks | not | low | S | cpu, memory |
| [ssz-009](#ssz-009) | Allocation-free merkleization scratch buffers | implemented | medium | S | cpu, memory |
| [ssz-012](#ssz-012) **★** | Balances list type with cached flat array | not | medium | L | cpu, latency |
| [ssz-016](#ssz-016) | Bulk-convert tree-backed bitlist to flat bitlist | n/a | low | S | cpu |
| [ssz-017](#ssz-017) | Bulk memcpy for byte-vector and byte-list SSZ | partial | low | S | cpu |
| [ssz-018](#ssz-018) | Faster snappy implementation for gossip and database | implemented | low | S | cpu, latency |
| [ssz-019](#ssz-019) | In-order leaf traversal instead of per-index lookups | implemented | low | S | cpu, latency |
| [ssz-021](#ssz-021) **★** | Pack multiple elements into one tree leaf node | not | medium | L | memory, cpu, disk |
| [ssz-024](#ssz-024) | Cache last tree path for sequential access | partial | low | M | cpu |
| [ssz-029](#ssz-029) **★** | Deserialize SSZ bytes directly into tree-backed values | partial | medium | M | cpu, memory, startup, latency |
| [ssz-031](#ssz-031) | Build merkle trees bottom-up without intermediate copies | implemented | low | S | cpu, memory |
| [ssz-036](#ssz-036) | Fast hex encode/decode for API byte fields | not | low | M | cpu, latency |
| [ssz-037](#ssz-037) | Specialized 32-byte root equality | n/a | low | S | cpu |
| [ssz-047](#ssz-047) | Build state proofs from cached tree layers | n/a | low | S | cpu, memory, latency |
| [ssz-049](#ssz-049) | Deserialize and clone into caller-provided output | n/a | low |  | cpu, memory |
| [ssz-057](#ssz-057) | Packed word storage for bitlists and bitvectors | partial | low | S | memory, cpu |
| [ssz-059](#ssz-059) | Packed specialized collections for primitive SSZ types | implemented | low |  | cpu, memory |
| [ssz-061](#ssz-061) | Presize serialization output buffers | implemented | low |  | cpu, memory |
| [ssz-065](#ssz-065) | Progressive SSZ merkleization for unbounded lists | implemented | medium | S | cpu, memory |
| [ssz-069](#ssz-069) | Zero-copy SSZ decode via input buffer views | n/a | low |  | memory, cpu, latency |
| [ssz-071](#ssz-071) **★** | Intern validator pubkeys and cache their hash | partial | medium | M | memory, cpu |
| [ssz-074](#ssz-074) | Skip default-init before decoding fixed-size lists | implemented | low |  | cpu, startup |
| [ssz-079](#ssz-079) | Serialize state lists by concatenating leaf data | partial | low | M | cpu, memory, disk |

★ actionable. Click an id for the full record.

## Ideas

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


<a id="ssz-009"></a>
<details>
<summary><b>ssz-009</b> Allocation-free merkleization scratch buffers — <i>implemented · medium · S · cpu, memory</i></summary>

**Idea.** In the merkleizer, write basic elements and padding straight into reusable chunk buffers, reuse the hasher, and do not zero-initialize scratch memory. Hashing large arrays (e.g. the slashings vector) then makes no per-element heap allocation.

**Impact.** Already done; slashings/balances hashing allocates nothing per element and only dirty leaves rehash.

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/tree_hash-0.12.1/src/merkle_hasher.rs:123 MerkleHasher keeps half_nodes in SmallVec8 (no heap up to 256 leaves) and a 32-byte SmallVec buffer
- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/tree_hash-0.12.1/src/lib.rs:20 PackedEncoding is inline SmallVec
- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/milhouse-0.9.0/src/packed_leaf.rs:30 PackedLeaf::tree_hash writes packed values straight into the 32-byte hash buffer, result cached

**Sources.** [nimbus#1058](https://github.com/status-im/nimbus-eth2/pull/1058), [nimbus#596](https://github.com/status-im/nimbus-eth2/pull/596), [caplin#7439](https://github.com/erigontech/erigon/pull/7439), [nimbus#5463](https://github.com/status-im/nimbus-eth2/pull/5463)

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

**Sources.** [lodestar#6557](https://github.com/ChainSafe/lodestar/pull/6557)

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

**Impact.** Nothing to gain: Lighthouse already uses the native Rust snap crate 1.1.2; the Nim-specific slowness does not apply. DB uses zstd.

**Best measured result.** 3x snappy compression; ~100 ms saved per state write (pr:nimbus#3234)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/pubsub.rs:6`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L6),123,149 snap::raw Decoder/Encoder for gossip
- [`beacon_node/lighthouse_network/src/rpc/codec.rs:8-9`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L8-L9),127,187 snap FrameEncoder/FrameDecoder for req/resp
- [`beacon_node/store/src/hot_cold_store.rs:45`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L45) DB uses zstd, not snappy

**Sources.** [nimbus#3234](https://github.com/status-im/nimbus-eth2/pull/3234), [nimbus#3564](https://github.com/status-im/nimbus-eth2/pull/3564)

</details>


<a id="ssz-019"></a>
<details>
<summary><b>ssz-019</b> In-order leaf traversal instead of per-index lookups — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** When reading all elements of a large tree-backed list or byte list, walk the leaves in one in-order traversal (copying whole 32-byte chunks) instead of one root-to-leaf lookup per index. This avoids re-traversing shared path nodes.

**Gap in Lighthouse.** Residual: iteration yields element by element from PackedLeaf rather than copying whole 32-byte chunks; a bulk List&lt;u8&gt; copy path in milhouse would be a minor gain.

**Impact.** State lists (validators, balances, participation flags) are already iterated in order; remaining gain is small.

**Best measured result.** 1 MiB byte list 10.3 ms -&gt; 0.51 ms; 17.5% of samples in a Sepolia backfill profile were this chain (pr:teku#11485)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/registry/src/*/milhouse-0.9.0/src/iter.rs:6-100 Iter keeps a node stack and walks leaves in order
- ~/.cargo/registry/src/*/milhouse-0.9.0/src/list.rs:124-137 List::iter/iter_from use it

**Sources.** [teku#11485](https://github.com/Consensys-Incorporated/teku/pull/11485), [lodestar@eedeb5f49](https://github.com/ChainSafe/lodestar/commit/eedeb5f492e9)

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

**Sources.** [grandine#986](https://github.com/grandinetech/grandine/pull/986), [teku#3347](https://github.com/Consensys-Incorporated/teku/pull/3347), [teku#4334](https://github.com/Consensys-Incorporated/teku/pull/4334)

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

**Sources.** [lodestar@8a002f841](https://github.com/ChainSafe/lodestar/commit/8a002f841e8f), [lodestar@c1197625b](https://github.com/ChainSafe/lodestar/commit/c1197625bc8a), [lodestar@2dea29be8](https://github.com/ChainSafe/lodestar/commit/2dea29be8db6), [teku#3382](https://github.com/Consensys-Incorporated/teku/pull/3382)

</details>


<a id="ssz-031"></a>
<details>
<summary><b>ssz-031</b> Build merkle trees bottom-up without intermediate copies — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Build list, vector and bitlist trees directly bottom-up from element or packed leaf nodes using index ranges, without a writable intermediate copy, sublist views or serialize/deserialize round trips.

**Impact.** State decode and list construction already build trees bottom-up with no mutable intermediate; bitfields are plain byte arrays hashed without a tree.

**Best measured result.** createBitlistAndSerialize 4.43x (2.57M to 11.4M ops/s), alloc -47%; HashTreeRoot 3.38x (pr:teku#10343)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/registry/src/*/milhouse-0.9.0/src/builder.rs:5-60 Builder folds nodes bottom-up with a stack and packs PackedLeaf directly
- ~/.cargo/registry/src/*/milhouse-0.9.0/src/list.rs:84-100 List::builder/try_from_iter use Builder
- ~/.cargo/registry/src/*/milhouse-0.9.0/src/list.rs:494-520 from_ssz_bytes goes through try_from_iter

**Sources.** [teku#10343](https://github.com/Consensys-Incorporated/teku/pull/10343), [teku#9088](https://github.com/Consensys-Incorporated/teku/pull/9088), [teku#10351](https://github.com/Consensys-Incorporated/teku/pull/10351), [teku#10839](https://github.com/Consensys-Incorporated/teku/pull/10839)

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

**Sources.** [lodestar#8275](https://github.com/ChainSafe/lodestar/pull/8275), [grandine@bdb716dd6](https://github.com/grandinetech/grandine/commit/bdb716dd6872)

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


<a id="ssz-059"></a>
<details>
<summary><b>ssz-059</b> Packed specialized collections for primitive SSZ types — <i>implemented · low · cpu, memory</i></summary>

**Idea.** Use specialized packed collections for hot primitive types (uint8 participation flags, u64 lists, Bytes32 vectors, pubkey/signature byte vectors) instead of generic lists of boxed element views.

**Impact.** Already packed in milhouse; nothing to gain.

**Best measured result.** iterateBeaconStateParticipationFlags 77.1 -&gt; 104.8 ops/s (pr:teku#5632)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/packed_leaf.rs:10: PackedLeaf stores Vec&lt;T&gt; of several basic values per leaf
- [`consensus/types/src/state/beacon_state.rs:554`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L554): balances is List&lt;u64&gt;, participation is List&lt;ParticipationFlags&gt;
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/utils.rs:67: opt_packing_factor packs basic types
- [`consensus/types/src/validator/validator.rs:22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/validator/validator.rs#L22): pubkey is fixed-size PublicKeyBytes array, no boxing

**Sources.** [teku#5632](https://github.com/Consensys-Incorporated/teku/pull/5632), [teku#3623](https://github.com/Consensys-Incorporated/teku/pull/3623)

</details>


<a id="ssz-061"></a>
<details>
<summary><b>ssz-061</b> Presize serialization output buffers — <i>implemented · low · cpu, memory</i></summary>

**Idea.** Allocate the serialization output buffer once with the exact (or upper-bound) encoded length, or use page-based buffering, so encoding a state or blob list does not grow, reallocate and copy the buffer repeatedly.

**Impact.** Single exact-size allocation for state and blob serialization is already done.

**Best measured result.** 10 txs: 69008 -&gt; 37949 ns/op, 353 -&gt; 210 allocs; 1000 txs: 5.56ms -&gt; 3.31ms (pr:prysm#147)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/ethereum_ssz-ba970959eb75904b/974f78f/ssz/src/encode.rs:40: as_ssz_bytes uses Vec::with_capacity(ssz_bytes_len())
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/list.rs:457: List::ssz_append does buf.reserve for fixed-size items

**Sources.** [nimbus#7310](https://github.com/status-im/nimbus-eth2/pull/7310), [prysm#147](https://github.com/OffchainLabs/prysm/pull/147), [ethlambda#741](https://github.com/lambdaclass/ethlambda/pull/741)

</details>


<a id="ssz-065"></a>
<details>
<summary><b>ssz-065</b> Progressive SSZ merkleization for unbounded lists — <i>implemented · medium · S · cpu, memory</i></summary>

**Idea.** Support progressive lists and containers whose merkle tree shape does not depend on the max length, so trees are shallower and updates touch fewer nodes.

**Impact.** Already present for the Gloas fork (milhouse ProgressiveList, progressive containers in tree_hash derive); not active on pre-Gloas mainnet.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:82`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L82) BalancesGloas = ProgressiveList&lt;u64&gt;
- [`consensus/state_processing/src/upgrade/gloas.rs:99`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/upgrade/gloas.rs#L99) validators, balances, participation, pending_* converted to ProgressiveList at Gloas
- [`consensus/types/src/attestation/payload_attestation.rs:17`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/attestation/payload_attestation.rs#L17) tree_hash progressive_container
- [`consensus/types/src/data/data_column_sidecar.rs:94`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/data/data_column_sidecar.rs#L94) ProgressiveVariableList

**Sources.** [teku#10928](https://github.com/Consensys-Incorporated/teku/pull/10928), [teku#10395](https://github.com/Consensys-Incorporated/teku/pull/10395)

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

**Sources.** [lodestar#8628](https://github.com/ChainSafe/lodestar/pull/8628), [nimbus@8d639d9bd](https://github.com/status-im/nimbus-eth2/commit/8d639d9bd75d), [lodestar#8626](https://github.com/ChainSafe/lodestar/pull/8626)

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

**Sources.** [nimbus#5883](https://github.com/status-im/nimbus-eth2/pull/5883)

</details>


<a id="ssz-074"></a>
<details>
<summary><b>ssz-074</b> Skip default-init before decoding fixed-size lists — <i>implemented · low · cpu, startup</i></summary>

**Idea.** When deserializing a list of fixed-size elements (e.g. validators), do not pre-fill the output with default values that the decode loop overwrites, removing an extra write pass over the whole list.

**Impact.** No default-init pass exists to remove.

**Best measured result.** full-state decode: EPYC 40.8ms -&gt; 17.5ms cold (-56%), 28.8 -&gt; 8.7ms warm (-69%); M5 8.4 -&gt; 7.1ms (commit:lodestar@0c757be3f4a3)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/list.rs:526: fixed-size List decode streams chunks into List::try_from_iter, no prefill
- ethereum_ssz decode/impls.rs:439: Vec&lt;T&gt; decode collects from chunks, no default fill

**Sources.** [lodestar@0c757be3f](https://github.com/ChainSafe/lodestar/commit/0c757be3f4a3)

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

**Sources.** [lodestar#6563](https://github.com/ChainSafe/lodestar/pull/6563), [teku#3062](https://github.com/Consensys-Incorporated/teku/pull/3062)

</details>


