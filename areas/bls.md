# bls

103 ideas: 18 not, 12 partial, 40 implemented, 33 n/a; 15 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [bls-001](#bls-001) | Use a fast native BLS library (blst) | implemented | high | S | cpu, latency, memory |
| [bls-002](#bls-002) | Keep the BLS library on recent releases | implemented | low | S | cpu |
| [bls-003](#bls-003) **★** | One index-keyed cache of decompressed validator pubkeys | partial | high | M | cpu, memory, startup |
| [bls-004](#bls-004) | Key pubkey cache by fixed-size byte array | n/a | low |  | cpu, memory |
| [bls-005](#bls-005) | Run BLS verification and aggregation off the main thread | implemented | medium | S | cpu, latency |
| [bls-006](#bls-006) | Size BLS thread pool from cgroup CPU quota | implemented | medium | S | cpu, latency |
| [bls-007](#bls-007) | Complete verification futures off the verifier thread | n/a | low |  | latency |
| [bls-008](#bls-008) | Group many signature jobs per worker message | n/a | low |  | latency, cpu |
| [bls-009](#bls-009) | Pass compressed points across thread boundaries | n/a | low |  | cpu, latency |
| [bls-010](#bls-010) | Avoid redundant parallelism around library batch verify | implemented | low | S | cpu |
| [bls-011](#bls-011) | Parallelize batch verification Miller loops across cores | implemented | medium | S | cpu, latency, sync |
| [bls-012](#bls-012) **★** | Combine same-message signature sets before batch verification | not | high | M | cpu |
| [bls-013](#bls-013) **★** | Multi-scalar multiplication for batch random scalars | not | medium | M | cpu, latency |
| [bls-014](#bls-014) | Batch-verify all signatures of a block at once | implemented | high | S | cpu, latency, sync |
| [bls-015](#bls-015) | Include sync aggregate in block signature batch | implemented | low | S | cpu, sync |
| [bls-016](#bls-016) | Include builder bid and payload attestations in block batch | implemented | low | S | cpu, latency |
| [bls-017](#bls-017) **★** | Batch-verify gossip signatures across messages | partial | medium | M | cpu, latency |
| [bls-018](#bls-018) **★** | Batch-verify payload timeliness committee signatures | not | medium | M | cpu, latency |
| [bls-019](#bls-019) | Batch-verify gossip BLS-to-execution changes | not | low | S | cpu |
| [bls-020](#bls-020) | Verify aggregate-and-proof's three signatures together | implemented | low | S | cpu, latency |
| [bls-021](#bls-021) **★** | Verify each gossip signature only once | partial | medium | S | cpu |
| [bls-022](#bls-022) | Batch-verify deposit signatures within a block | not | low | M | cpu |
| [bls-023](#bls-023) | Cache deposit signature verification results | implemented | low | S | cpu |
| [bls-024](#bls-024) **★** | Aggregate many pubkeys with batched point addition | not | medium | S | cpu, latency |
| [bls-025](#bls-025) **★** | Precompute committee pubkey sums and subtract non-attesters | not | high | M | cpu, latency |
| [bls-026](#bls-026) | Pass validator indices to the verifier, aggregate pubkeys there | n/a | low |  | cpu, latency |
| [bls-027](#bls-027) | Optimise signature aggregation with benchmarks | n/a | low | S | cpu |
| [bls-028](#bls-028) **★** | Run pairing product on SIMD IFMA lanes | not | medium | L | cpu, latency |
| [bls-029](#bls-029) **★** | Decompress signatures in batches | not | medium | L | cpu, latency |
| [bls-030](#bls-030) **★** | Batch-validate pubkeys during state load | partial | medium | L | startup, cpu |
| [bls-031](#bls-031) | Select fast CPU-specific BLS paths at runtime | implemented | low | S | cpu |
| [bls-032](#bls-032) | Enable aarch64 carryless multiply in crypto | n/a | low | S | cpu |
| [bls-033](#bls-033) | Aggregate-verify multiple messages with one multi-pairing | implemented | low | S | cpu |
| [bls-034](#bls-034) | Align signature types to 16 bytes | n/a | low |  | cpu |
| [bls-035](#bls-035) | Use raw signature bytes instead of reserializing | partial | low | S | cpu |
| [bls-036](#bls-036) | Copy BLS points without serialize roundtrip | implemented | low | S | cpu |
| [bls-037](#bls-037) | Pass BLS points by reference, avoid copies | implemented | low | S | cpu, memory |
| [bls-038](#bls-038) | Compare BLS keys by compressed bytes | implemented | low | S | cpu |
| [bls-039](#bls-039) | Avoid exceptions on pubkey cache miss | n/a | low |  | cpu |
| [bls-040](#bls-040) | Verify directly from compressed bytes natively | partial | low | M | cpu, memory |
| [bls-041](#bls-041) | Cap batch size at the native verifier limit | n/a | medium |  | cpu |
| [bls-042](#bls-042) | Avoid stream overhead in batch verify code | n/a | low |  | cpu |
| [bls-043](#bls-043) | Use library EIP-2333 key derivation | not | low | S | cpu |
| [bls-044](#bls-044) | Subgroup-check each pubkey once and reuse it | implemented | medium | S | cpu, memory |
| [bls-045](#bls-045) | Cheaper secret key zero check and marshal | n/a | low | S | cpu |
| [bls-046](#bls-046) | Compress aggregated proofs on the wire | n/a | low | L | bandwidth |
| [bls-047](#bls-047) | Bump proof-system dependency for prover speedups | n/a | low | S | cpu, memory |
| [bls-048](#bls-048) | Call native BLS library without abstraction layer | n/a | low | S | cpu |
| [bls-049](#bls-049) | Fast G2 cofactor clearing and subgroup check | implemented | low | S | cpu, sync |
| [bls-050](#bls-050) | Keep decompressed pubkeys in BLS change messages | not | low | M | cpu |
| [bls-051](#bls-051) | Faster batch signature verification (unspecified) | n/a | low | S | cpu |
| [bls-052](#bls-052) | SHA-256 instead of keccak in hash-to-G2 | n/a | low | S | cpu |
| [bls-053](#bls-053) | Verify deposit signatures only when the outcome depends on it | partial | low | S | cpu, memory |
| [bls-054](#bls-054) | Fixed-size arrays for BLS serialization | implemented | low | S | cpu |
| [bls-055](#bls-055) | Populate pubkey cache only when enabled | n/a | low | S | memory, cpu |
| [bls-056](#bls-056) | Cheaper public key hashing for hash maps | partial | low | S | cpu |
| [bls-057](#bls-057) **★** | Larger gossip signature batch size limit | partial | medium | S | cpu |
| [bls-058](#bls-058) | Lazy pubkey and signature decompression | implemented | medium | S | cpu, sync, startup |
| [bls-059](#bls-059) | Dispatch BLS jobs to lowest-latency worker | n/a | low |  | latency, cpu |
| [bls-060](#bls-060) | Plain map instead of LRU for pubkey cache | implemented | low | S | memory |
| [bls-061](#bls-061) | Reuse buffers in batch verification, no per-call allocation | partial | low | S | cpu, memory |
| [bls-062](#bls-062) | Raise default BLS verification threads and queue size | n/a | medium |  | cpu, latency |
| [bls-063](#bls-063) | BLS on native thread pool, not JS workers | n/a | low |  | cpu, latency |
| [bls-064](#bls-064) | Verify block attestation signatures in parallel | implemented | medium | S | cpu, latency |
| [bls-065](#bls-065) | Preallocate signature-set vectors with known capacity | implemented | low | S | cpu, memory |
| [bls-066](#bls-066) | Preassigned per-worker result slots in batch verify | n/a | low |  | cpu |
| [bls-067](#bls-067) | Precompute fork-data roots for domain derivation | not | low | S | cpu |
| [bls-068](#bls-068) | Prepopulate pubkey cache in background at startup | implemented | low | S | startup, sync, cpu |
| [bls-069](#bls-069) | API-submitted signatures bypass gossip verification queue | implemented | medium | S | latency, cpu |
| [bls-070](#bls-070) | Cache pubkey deserialization keyed by compressed bytes | implemented | low | S | cpu, sync |
| [bls-071](#bls-071) | Random linear combination batch verification | implemented | high | S | cpu |
| [bls-072](#bls-072) | Shared read lock for pubkey cache lookups | implemented | low | S | cpu, latency |
| [bls-073](#bls-073) **★** | Bisect failed signature batches recursively | not | medium | S | cpu |
| [bls-074](#bls-074) | Relaxed atomics for verify early-exit flag | implemented | low | S | cpu |
| [bls-075](#bls-075) | Fewer branches in Jacobian point addition | n/a | low |  | cpu |
| [bls-076](#bls-076) | Do not hash to G2 twice | implemented | medium | S | cpu |
| [bls-077](#bls-077) | No mutex around BLS thread pool task spawn | n/a | low |  | cpu, latency |
| [bls-078](#bls-078) | Benchmark BLS binding changes end to end | n/a | low |  | cpu, latency |
| [bls-079](#bls-079) | Put aggregate signature in the shared Miller loop | not | low | M | cpu |
| [bls-080](#bls-080) **★** | Shared hash-to-G2 cache keyed by signing root | not | medium | M | cpu |
| [bls-081](#bls-081) | Load only one BLS implementation per process | n/a | low |  | startup, memory |
| [bls-082](#bls-082) | Single merged block-level signature proof | n/a | low |  | bandwidth, cpu |
| [bls-083](#bls-083) | Single pass over keys and signatures in batch prep | partial | low | S | cpu |
| [bls-084](#bls-084) | Flag to skip BLS for profiling | partial | low | S | cpu |
| [bls-085](#bls-085) | Skip signature checks for trusted or pre-verified blocks | implemented | medium | S | cpu |
| [bls-086](#bls-086) | Verify sparse time-critical gossip objects unbatched | implemented | low | S | latency |
| [bls-087](#bls-087) | Do not recheck proposer signature verified at gossip | implemented | medium | S | cpu |
| [bls-088](#bls-088) | No pubkey aggregation for single-signer attestations | not | low | S | cpu |
| [bls-089](#bls-089) | Yield between very large BLS batches | n/a | low |  | cpu, latency |
| [bls-090](#bls-090) | Route batchable vs latency-critical BLS jobs separately | implemented | medium | S | latency, cpu |
| [bls-091](#bls-091) | Store pubkeys uncompressed on disk to skip decompression | implemented | medium | S | startup, cpu |
| [bls-092](#bls-092) | Fixed-size sub-batches for bulk signature verification | implemented | low | S | cpu |
| [bls-093](#bls-093) **★** | Subtract non-participants from full sync committee aggregate | not | medium | S | cpu |
| [bls-094](#bls-094) | Configurable signature batching parameters | implemented | low | S | cpu, latency |
| [bls-095](#bls-095) | Key deposit pubkey cache by decompressed key | n/a | low |  | cpu, memory |
| [bls-096](#bls-096) | Simpler y-sign flag in point decompression | n/a | low |  | cpu |
| [bls-097](#bls-097) | Aggregate attestation pubkeys inside the BLS library | implemented | low | S | cpu, latency |
| [bls-098](#bls-098) | Size pairing buffers from real library context size | implemented | low | S | memory |
| [bls-099](#bls-099) | Verify tiny signature batches inline on caller | not | low | S | cpu, latency |
| [bls-100](#bls-100) | Drop release loop over semi-aggregates in batch verify | n/a | low | S | cpu, memory |
| [bls-101](#bls-101) | Check signature subgroup once at deserialisation | implemented | low | S | cpu, memory |
| [bls-102](#bls-102) | Skip Pippenger for tiny multi-scalar multiplications | n/a | low | S | cpu, latency |
| [bls-103](#bls-103) | Wake only as many BLS workers as queued items | n/a | low | S | cpu, latency |

★ actionable. Click an id for the full record.

## Ideas

<a id="bls-001"></a>
<details>
<summary><b>bls-001</b> Use a fast native BLS library (blst) — <i>implemented · high · S · cpu, latency, memory</i></summary>

**Idea.** Back every BLS operation (verify, aggregate, batch verify) on all verification paths with a fast native BLS12-381 library such as blst with assembly-optimized field arithmetic, not a pure-language, managed or older slower backend. Pairings and point operations become several times cheaper.

**Impact.** All BLS verify, aggregate and batch paths run on blst (blst-0.3.x), which has assembly-optimized field arithmetic.

**Best measured result.** Blst 7-9x faster than Mikuli; block import 0.076s to 0.021s (pr:teku#2453)

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/impls/blst.rs:36-110`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L36-L110)
- [`crypto/bls/src/lib.rs:97`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/lib.rs#L97)
- [`beacon_node/beacon_chain/src/attestation_verification/batch.rs:109`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification/batch.rs#L109)

**Skeptic check.** The blst backend is the production bls implementation; fake_crypto is only for tests. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@8081a0554](https://github.com/ChainSafe/lodestar/commit/8081a055453d), [prysm#6539](https://github.com/OffchainLabs/prysm/pull/6539), [prysm#7805](https://github.com/OffchainLabs/prysm/pull/7805), [lodestar#570](https://github.com/ChainSafe/lodestar/pull/570), [caplin#5950](https://github.com/erigontech/erigon/pull/5950), [lighthouse#768](https://github.com/sigp/lighthouse/pull/768), [prysm#4181](https://github.com/OffchainLabs/prysm/pull/4181), [prysm#3670](https://github.com/OffchainLabs/prysm/pull/3670), [lodestar@dc4c8a5d5](https://github.com/ChainSafe/lodestar/commit/dc4c8a5d575b), [teku#2453](https://github.com/Consensys-Incorporated/teku/pull/2453), [prysm#3752](https://github.com/OffchainLabs/prysm/pull/3752), [prysm#8710](https://github.com/OffchainLabs/prysm/pull/8710), [nimbus#1791](https://github.com/status-im/nimbus-eth2/pull/1791), [teku#898](https://github.com/Consensys-Incorporated/teku/pull/898), [lodestar@d26e2ec52](https://github.com/ChainSafe/lodestar/commit/d26e2ec52cff)

</details>


<a id="bls-002"></a>
<details>
<summary><b>bls-002</b> Keep the BLS library on recent releases — <i>implemented · low · S · cpu</i></summary>

**Idea.** Track recent blst (or bindings) releases and the newer APIs they expose, so the client picks up upstream speedups in verification and batched multi-signature checks. Check the pinned BLS crate version against upstream.

**Impact.** Lighthouse pins blst 0.3.17, the newest version in the local crates.io index cache, and uses its batched verify_multiple_aggregate_signatures API.

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.lock:1801
- [`crypto/bls/Cargo.toml:18`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/Cargo.toml#L18)
- [`crypto/bls/src/impls/blst.rs:113`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L113)

**Skeptic check.** Verified Cargo.lock blst 0.3.17 and that the local index lists nothing newer; upstream freshness could not be checked online, hence low confidence. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#6675](https://github.com/Consensys-Incorporated/teku/pull/6675), [lodestar@9e8a96ebf](https://github.com/ChainSafe/lodestar/commit/9e8a96ebf86a), [teku#8386](https://github.com/Consensys-Incorporated/teku/pull/8386), [lighthouse#2601](https://github.com/sigp/lighthouse/pull/2601)

</details>


<a id="bls-003"></a>
<details>
<summary><b>bls-003</b> One index-keyed cache of decompressed validator pubkeys — <i>partial · high · M · cpu, memory, startup</i></summary>

**Idea.** Keep a single process-wide cache of every validator's public key in decompressed, already-validated form, indexed by validator index (a flat table, sized for the whole set, preloaded or persisted at startup), and use it from all signature verification and aggregation paths. This removes pubkey decompression, subgroup checks and hash-map lookups from each verification.

**Gap in Lighthouse.** Validator keys are covered: a Vec&lt;PublicKey&gt; indexed by validator index, persisted as uncompressed bytes. Gloas builder pubkeys have no cache. get_builder_pubkey_from_state decompresses (and subgroup-checks) the key from state.builders on every verification: in gossip bid verification, direct bid verification, the in-block bid set (include_execution_payload_bid) and gossip envelope verification. The code has TODO(gloas) notes about this. The sync aggregate decompressor also does one HashMap&lt;PublicKeyBytes&gt; get_index lookup per committee member per block.

**Impact.** Low today. It grows with the number of builder bids per slot after Gloas: each bid pays a pubkey decompression of about 50us.

**Best measured result.** hash-map pubkey lookups cost 0.5-0.7x of a block's pairing (removed) (pr:ethlambda#743)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:24-80`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L24-L80)
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:237-242`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L237-L242)
- [`beacon_node/beacon_chain/src/block_verification.rs:2236-2254`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L2236-L2254)
- [`consensus/state_processing/src/per_block_processing/signature_sets.rs:79-95`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/signature_sets.rs#L79-L95)
- [`consensus/state_processing/src/per_block_processing/block_signature_verifier.rs:413-416`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/block_signature_verifier.rs#L413-L416)
- [`beacon_node/beacon_chain/src/payload_bid_verification/gossip_verified_bid.rs:464`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_bid_verification/gossip_verified_bid.rs#L464)
- [`beacon_node/beacon_chain/src/payload_envelope_verification/gossip_verified_envelope.rs:272-273`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/gossip_verified_envelope.rs#L272-L273)

**Skeptic check.** The earlier evidence for the validator pubkey cache is correct. It missed the builder registry path, where Gloas bid and envelope verification decompress keys from the state every time.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [prysm#4417](https://github.com/OffchainLabs/prysm/pull/4417), [lighthouse#766](https://github.com/sigp/lighthouse/pull/766), [nimbus#3122](https://github.com/status-im/nimbus-eth2/pull/3122), [lodestar@c74278231](https://github.com/ChainSafe/lodestar/commit/c74278231d4f), [lodestar#1197](https://github.com/ChainSafe/lodestar/pull/1197), [grandine@d13679310](https://github.com/grandinetech/grandine/commit/d13679310226), [prysm#4737](https://github.com/OffchainLabs/prysm/pull/4737), [lodestar#1487](https://github.com/ChainSafe/lodestar/pull/1487), [lighthouse#849](https://github.com/sigp/lighthouse/pull/849), [ethlambda#743](https://github.com/lambdaclass/ethlambda/pull/743), [lodestar#8900](https://github.com/ChainSafe/lodestar/pull/8900), [lodestar#9728](https://github.com/ChainSafe/lodestar/pull/9728)

</details>


<a id="bls-004"></a>
<details>
<summary><b>bls-004</b> Key pubkey cache by fixed-size byte array — <i>n/a · low · cpu, memory</i></summary>

**Idea.** When a cache maps compressed pubkey bytes to decompressed keys, key it by the fixed 48-byte array (no allocation) rather than a heap string. This removes an allocation and conversion on each lookup.

**Impact.** Rust already keys by fixed 48-byte array, no heap string.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:26`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L26) HashMap&lt;PublicKeyBytes, usize&gt; fixed-size array key

**Sources.** [prysm#10440](https://github.com/OffchainLabs/prysm/pull/10440)

</details>


<a id="bls-005"></a>
<details>
<summary><b>bls-005</b> Run BLS verification and aggregation off the main thread — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Send signature verification jobs, including the random-linear-combination aggregation step of batch verification, to a dedicated worker or native thread pool with async signalling instead of running them on the main event loop or async executor. This keeps the main thread responsive under CPU limits and uses all cores.

**Impact.** BLS work runs on beacon processor blocking threads, never on the async executor, and blst spreads each batch across its own thread pool.

**Best measured result.** +40% sig verification throughput; attestation throughput 7k -&gt; ~10k/slot (pr:nimbus#5176)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:1657`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1657)
- [`crypto/bls/src/impls/blst.rs:36-110`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L36-L110)
- blst-0.3.17/src/lib.rs:1337-1347

**Skeptic check.** Confirmed that verification runs in spawn_blocking workers. The earlier gap text was wrong to say one batch uses one core: blst's verify_multiple_aggregate_signatures splits the work over mt::da_pool workers.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@ebdf36fa2](https://github.com/ChainSafe/lodestar/commit/ebdf36fa24e3), [lodestar#2328](https://github.com/ChainSafe/lodestar/pull/2328), [lodestar#6362](https://github.com/ChainSafe/lodestar/pull/6362), [lodestar#9342](https://github.com/ChainSafe/lodestar/pull/9342), [lodestar#7435](https://github.com/ChainSafe/lodestar/pull/7435), [lodestar#7761](https://github.com/ChainSafe/lodestar/pull/7761), [lodestar#7204](https://github.com/ChainSafe/lodestar/pull/7204), [nimbus#5176](https://github.com/status-im/nimbus-eth2/pull/5176)

</details>


<a id="bls-006"></a>
<details>
<summary><b>bls-006</b> Size BLS thread pool from cgroup CPU quota — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Compute the BLS verification thread count from the cgroup CPU quota and affinity, not the host core count. This avoids oversubscription and CFS throttling in containers.

**Impact.** Thread counts come from num_cpus::get() (1.17.0), which reads cgroup v1 cfs_quota and v2 cpu.max and sched_getaffinity on Linux; blst's internal ThreadPool::default uses the same; rayon's global pool uses available_parallelism, also cgroup-aware.

**Evidence (Lighthouse @ 928b61e719).**

- [`common/task_executor/src/rayon_pool_provider.rs:26`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/task_executor/src/rayon_pool_provider.rs#L26)
- [`beacon_node/beacon_processor/src/lib.rs:130`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L130)
- num_cpus-1.17.0/src/linux.rs:33
- num_cpus-1.17.0/src/linux.rs:227
- num_cpus-1.17.0/src/linux.rs:41
- blst-0.3.17/src/lib.rs:46

**Skeptic check.** Verified num_cpus 1.17 linux.rs applies cgroup quota (v1 and v2) and affinity, and every BLS-relevant pool (beacon processor workers, rayon pools, blst da_pool) is sized from it. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@3ae95226b](https://github.com/ChainSafe/lodestar/commit/3ae95226b31a)

</details>


<a id="bls-007"></a>
<details>
<summary><b>bls-007</b> Complete verification futures off the verifier thread — <i>n/a · low · latency</i></summary>

**Idea.** When a batch verification finishes, resolve the waiting futures/callbacks on another thread pool so downstream handlers do not run on, and block, the batch verification thread.

**Impact.** No dedicated verifier thread with futures to resolve; results are returned inline in the blocking worker.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:1657`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1657) verification runs inline in the work task, no separate verifier thread

**Sources.** [teku#4753](https://github.com/Consensys-Incorporated/teku/pull/4753)

</details>


<a id="bls-008"></a>
<details>
<summary><b>bls-008</b> Group many signature jobs per worker message — <i>n/a · low · latency, cpu</i></summary>

**Idea.** Send several signature-set jobs to BLS workers in one message to amortize thread messaging overhead, and route all gossip validation through the pool. Messaging cost becomes comparable to a single verification.

**Impact.** Lighthouse uses native threads/rayon-free blst call, no JS worker message boundary.

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/impls/blst.rs:36`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L36) in-process verification

**Sources.** [lodestar#2421](https://github.com/ChainSafe/lodestar/pull/2421)

</details>


<a id="bls-009"></a>
<details>
<summary><b>bls-009</b> Pass compressed points across thread boundaries — <i>n/a · low · cpu, latency</i></summary>

**Idea.** Send pubkeys and signatures to verification threads in compressed form (48/96 bytes) instead of uncompressed, halving the data copied between threads.

**Impact.** Verification is in-process; pubkeys are already decompressed points in the cache, nothing crosses a thread copy boundary.

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/impls/blst.rs:36`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L36) in-process verification

**Sources.** [lodestar#5779](https://github.com/ChainSafe/lodestar/pull/5779)

</details>


<a id="bls-010"></a>
<details>
<summary><b>bls-010</b> Avoid redundant parallelism around library batch verify — <i>implemented · low · S · cpu</i></summary>

**Idea.** Do not wrap a batch BLS verification in an outer parallel iterator when the library's multi-aggregate verify already uses multiple threads; call it directly. This avoids nested parallelism and contention.

**Impact.** No nested parallelism remains.

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/impls/blst.rs:36`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L36)
- [`consensus/state_processing/src/per_block_processing/block_signature_verifier.rs:460`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/block_signature_verifier.rs#L460)
- [`beacon_node/beacon_chain/src/attestation_verification/batch.rs:109`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification/batch.rs#L109),195
- [`beacon_node/beacon_chain/src/sync_committee_verification.rs:670`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/sync_committee_verification.rs#L670)

**Skeptic check.** Every verify_signature_sets caller (block, attestation batch, sync committee, deposits) calls it directly with no par_iter wrapper, and blst does the threading inside.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#5992](https://github.com/sigp/lighthouse/pull/5992)

</details>


<a id="bls-011"></a>
<details>
<summary><b>bls-011</b> Parallelize batch verification Miller loops across cores — <i>implemented · medium · S · cpu, latency, sync</i></summary>

**Idea.** Split a batch verification's multi-pairing across a thread pool (e.g. blst miller_loop_n, or per-thread partial Miller-loop accumulators merged before one final exponentiation) and enable it by default. Sync, block import and gossip batches then use all cores.

**Best measured result.** 10-20% faster sync; 8 threads about 1m29s vs 1 thread about 1m55s for 100 epochs (pr:nimbus#3493)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/blst-0.3.17/src/lib.rs:1336-1385 verify_multiple_aggregate_signatures runs per-worker Pairing accumulators on mt::da_pool(), merges them, one finalverify
- blst-0.3.17/src/lib.rs:35-41 da_pool is the threaded pool unless feature no-threads
- [`crypto/bls/Cargo.toml:11-18`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/Cargo.toml#L11-L18) blst enabled without no-threads
- [`crypto/bls/src/impls/blst.rs:113`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L113) every batch goes through it

**Skeptic check.** Confirmed: the Miller loops of a batch are split across the blst thread pool with partial accumulators merged before one final exponentiation, on by default. Small residue: the per-set signature subgroup check and pubkey aggregation in crypto/bls/src/impls/blst.rs:71-104 run serially on the caller before the parallel part, but that is not what the idea describes.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#5300](https://github.com/status-im/nimbus-eth2/pull/5300), [nimbus#3493](https://github.com/status-im/nimbus-eth2/pull/3493), [lodestar@6da152424](https://github.com/ChainSafe/lodestar/commit/6da152424950), [lodestar@11f83eb98](https://github.com/ChainSafe/lodestar/commit/11f83eb98bcf), [lodestar@4399a853b](https://github.com/ChainSafe/lodestar/commit/4399a853be89), [lodestar@34ff8c15a](https://github.com/ChainSafe/lodestar/commit/34ff8c15ab31), [nimbus#2718](https://github.com/status-im/nimbus-eth2/pull/2718)

</details>


<a id="bls-012"></a>
<details>
<summary><b>bls-012</b> Combine same-message signature sets before batch verification — <i>not · high · M · cpu</i></summary>

**Idea.** Before batch verification, deduplicate identical signatures and group sets that share a signing root (same attestation data), summing their pubkeys and signatures with random scalar coefficients (Pippenger MSM) so the batch needs one pairing per distinct message instead of one per set.

**Gap in Lighthouse.** Group sets by signing root in bls::verify_signature_sets: per group sum r_i*pk_i (MSM) and r_i*sig_i, one pairing per distinct message, keep per-set random scalars against cancellation. Open PR sigp/lighthouse#9521 does this; not merged in 928b61e719.

**Impact.** Fewer pairings for gossip attestation/aggregate batches and block attestations that share AttestationData; ~16% BLS CPU drop measured in #9521 on an all-subnets mainnet node.

**Best measured result.** 6x to &gt;10x faster than verifyMultipleSignatures (pr:lodestar#5747)

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/impls/blst.rs:36-120`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L36-L120) one (msg, aggregated pk, sig, rand) tuple per set passed straight to verify_multiple_aggregate_signatures; no grouping by message or dedup of signatures
- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/blst-0.3.17/src/lib.rs:1335 '// TODO - check msg uniqueness?' and :1350 '// TODO - engage multi-point mul-n-add' : the dependency does one mul_n_aggregate (Miller loop input) per element, no same-message merge

**Second check.** Checked the blst 0.3.17 crate (the version in Cargo.lock) as well as Lighthouse's wrapper: blst itself marks message uniqueness and multi-point mul-n-add as TODO, so no hidden grouping exists in the dependency.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [nimbus#6484](https://github.com/status-im/nimbus-eth2/pull/6484), [nimbus#3212](https://github.com/status-im/nimbus-eth2/pull/3212), [teku#11507](https://github.com/Consensys-Incorporated/teku/pull/11507), [prysm#10127](https://github.com/OffchainLabs/prysm/pull/10127), [nimbus#6459](https://github.com/status-im/nimbus-eth2/pull/6459), [lodestar@69d16877f](https://github.com/ChainSafe/lodestar/commit/69d16877f161), [lodestar#6516](https://github.com/ChainSafe/lodestar/pull/6516), [prysm#17763](https://github.com/OffchainLabs/prysm/pull/17763), [lodestar#5747](https://github.com/ChainSafe/lodestar/pull/5747), [lodestar#5734](https://github.com/ChainSafe/lodestar/pull/5734), [lighthouse#9521](https://github.com/sigp/lighthouse/pull/9521)

</details>


<a id="bls-013"></a>
<details>
<summary><b>bls-013</b> Multi-scalar multiplication for batch random scalars — <i>not · medium · M · cpu, latency</i></summary>

**Idea.** In batch verification, apply the random scalars to all pubkeys and signatures with one (optionally thread-parallel) Pippenger multi-scalar multiplication with reusable scratch memory, instead of a separate scalar multiplication per set.

**Gap in Lighthouse.** Would need custom pairing code using blst_p1s/p2s_mult_pippenger for the random-scalar step; blst already parallelises across its own thread pool and uses short scalars, so gain is small.

**Impact.** Negligible; source measured parity with existing blst.

**Best measured result.** 128 sets 8.95ms vs 8.84ms (comparable to existing blst) (commit:lodestar@28b43a9da89c)

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/impls/blst.rs:113-115`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L113-L115) calls blst verify_multiple_aggregate_signatures with 64-bit rands
- blst-0.3.17/src/lib.rs:1337-1370 thread-parallel per-element Pairing::mul_n_aggregate with a 'TODO - engage multi-point mul-n-add' comment; no Pippenger used

**Second check.** Read blst's std batch verify: it is thread-parallel (da_pool) but per-set scalar mult, with an explicit TODO for MSM, confirming the idea is not implemented.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [lodestar@403d8c6fa](https://github.com/ChainSafe/lodestar/commit/403d8c6fa38e), [lodestar@28b43a9da](https://github.com/ChainSafe/lodestar/commit/28b43a9da89c), [lodestar@8cfa1af06](https://github.com/ChainSafe/lodestar/commit/8cfa1af06813)

</details>


<a id="bls-014"></a>
<details>
<summary><b>bls-014</b> Batch-verify all signatures of a block at once — <i>implemented · high · S · cpu, latency, sync</i></summary>

**Idea.** Before the mutating state transition, collect every signature set in a block (proposer, randao, attestations, slashings, exits, BLS changes) and verify them in one randomized batch multi-signature verification, then run the transition with signature checks skipped.

**Impact.** Already in place.

**Best measured result.** Pairing per block 2.7-4x less wall time (loaded M3, mixes fewer final exponentiations and threading) (pr:ethlambda#738)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/block_signature_verifier.rs:160-185`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/block_signature_verifier.rs#L160-L185)
- [`consensus/state_processing/src/per_block_processing/block_signature_verifier.rs:440-461`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/block_signature_verifier.rs#L440-L461)
- [`beacon_node/beacon_chain/src/block_verification.rs:2226-2254`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L2226-L2254)

**Skeptic check.** include_all_signatures collects the proposal, randao, slashings, attestations, exits, sync aggregate, BLS changes, bid and payload attestations, then verifies them in one randomized blst batch. Deposits are left out on purpose. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#6277](https://github.com/OffchainLabs/prysm/pull/6277), [ethlambda#738](https://github.com/lambdaclass/ethlambda/pull/738), [lodestar@5d630b104](https://github.com/ChainSafe/lodestar/commit/5d630b104c86), [lighthouse#507](https://github.com/sigp/lighthouse/pull/507), [lodestar#1851](https://github.com/ChainSafe/lodestar/pull/1851), [nimbus#2250](https://github.com/status-im/nimbus-eth2/pull/2250), [prysm#7687](https://github.com/OffchainLabs/prysm/pull/7687), [teku#1632](https://github.com/Consensys-Incorporated/teku/pull/1632), [caplin#12356](https://github.com/erigontech/erigon/pull/12356), [prysm#11684](https://github.com/OffchainLabs/prysm/pull/11684), [prysm#11689](https://github.com/OffchainLabs/prysm/pull/11689), [lodestar@a5bacf7b5](https://github.com/ChainSafe/lodestar/commit/a5bacf7b5d80), [lodestar#1821](https://github.com/ChainSafe/lodestar/pull/1821), [silver#18](https://github.com/gattaca-com/silver/pull/18), [prysm#16837](https://github.com/OffchainLabs/prysm/pull/16837)

</details>


<a id="bls-015"></a>
<details>
<summary><b>bls-015</b> Include sync aggregate in block signature batch — <i>implemented · low · S · cpu, sync</i></summary>

**Idea.** Add the block's sync committee aggregate signature to the block-wide batch verifier (handling the empty/infinity case), and skip signature verification when replaying blocks already stored in the DB.

**Impact.** Already in place.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/block_signature_verifier.rs:181`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/block_signature_verifier.rs#L181)
- [`consensus/state_processing/src/per_block_processing/block_signature_verifier.rs:365-380`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/block_signature_verifier.rs#L365-L380)
- [`consensus/state_processing/src/block_replayer.rs:114`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/block_replayer.rs#L114)

**Skeptic check.** The sync aggregate set is added only when sync_aggregate_signature_set returns Some, which handles the empty/infinity case. BlockReplayer uses BlockSignatureStrategy::NoVerification for stored blocks.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#2625](https://github.com/ChainSafe/lodestar/pull/2625), [lighthouse#2415](https://github.com/sigp/lighthouse/pull/2415)

</details>


<a id="bls-016"></a>
<details>
<summary><b>bls-016</b> Include builder bid and payload attestations in block batch — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Add the builder bid signature and all payload attestation signatures of an ePBS block to the block's single batched BLS verification instead of verifying each separately.

**Impact.** Already in place.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/block_signature_verifier.rs:183-184`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/block_signature_verifier.rs#L183-L184)
- [`consensus/state_processing/src/per_block_processing/block_signature_verifier.rs:310-336`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/block_signature_verifier.rs#L310-L336)
- [`consensus/state_processing/src/per_block_processing/block_signature_verifier.rs:406-424`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/block_signature_verifier.rs#L406-L424)

**Skeptic check.** include_execution_payload_bid and include_payload_attestations both push into the same block batch. The builder pubkey is still decompressed from state for each check; that is tracked under bls-003.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#25192](https://github.com/erigontech/erigon/pull/25192)

</details>


<a id="bls-017"></a>
<details>
<summary><b>bls-017</b> Batch-verify gossip signatures across messages — <i>partial · medium · M · cpu, latency</i></summary>

**Idea.** Buffer gossip attestations, aggregates, sync messages and contributions in a shared time- and size-bounded batch verifier (e.g. flush every 50ms or at 100 signatures, or on backlog) and verify their signatures together in one randomized batch, falling back to individual verification only if the batch fails. Pairing and final exponentiation cost is shared across messages.

**Gap in Lighthouse.** Sync committee messages and contributions get no cross-message batching; attestation batching has no time window (only what is queued). Add a sync-message/contribution batch work type in beacon_processor and a batch verify path in sync_committee_verification.rs.

**Impact.** Saves final exponentiations on ~512 sync messages per slot per subscribed node; a modest share of total BLS CPU. A flush timer adds latency and is probably not worth it.

**Best measured result.** pprof shows more than 10x speed up (pr:caplin#11940)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:110-111`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L110-L111) attestation/aggregate batch sizes of 64, drained opportunistically from the queue
- [`beacon_node/beacon_chain/src/attestation_verification/batch.rs:109`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification/batch.rs#L109),195 batch verify with individual fallback
- [`beacon_node/beacon_processor/src/lib.rs:1332-1337`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1332-L1337) GossipSyncSignature and GossipSyncContribution pushed to plain FIFO queues; :1741-1742 run as single blocking fns, no batch work type
- [`beacon_node/beacon_chain/src/sync_committee_verification.rs:604`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/sync_committee_verification.rs#L604) contribution batch only covers the 3 sets inside one message

**Second check.** Checked the beacon_processor enqueue and dispatch paths for sync work and the sync_committee_verification module for any multi-message batch API; none exist, so attestations and aggregates are the only cross-message batches.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [lighthouse#2399](https://github.com/sigp/lighthouse/pull/2399), [silver#184](https://github.com/gattaca-com/silver/pull/184), [caplin#11940](https://github.com/erigontech/erigon/pull/11940), [lodestar#2801](https://github.com/ChainSafe/lodestar/pull/2801), [prysm#12151](https://github.com/OffchainLabs/prysm/pull/12151), [prysm#9344](https://github.com/OffchainLabs/prysm/pull/9344), [nimbus#3151](https://github.com/status-im/nimbus-eth2/pull/3151), [teku#4574](https://github.com/Consensys-Incorporated/teku/pull/4574), [caplin#11954](https://github.com/erigontech/erigon/pull/11954)

</details>


<a id="bls-018"></a>
<details>
<summary><b>bls-018</b> Batch-verify payload timeliness committee signatures — <i>not · medium · M · cpu, latency</i></summary>

**Idea.** Route gossip payload-timeliness-committee (PTC) message signatures through the randomized batch verifier, and re-check entries of a failed batch in parallel rather than serially.

**Gap in Lighthouse.** Add a GossipPayloadAttestationBatch work type in beacon_processor (mirroring GossipAttestationBatch) and a batch verify in payload_attestation_verification that calls bls::verify_signature_sets over all sets, falling back to per-item verify (optionally parallel) on batch failure.

**Impact.** Up to 512 single-validator PTC messages per slot in Gloas each pay a full pairing; batching roughly halves per-signature CPU, a few hundred ms CPU per slot on PTC-subscribed nodes.

**Best measured result.** failed 50-batch at 8 cores 45.4 -&gt; 11.7 ms; PTC CPU per run 758 -&gt; 387 ms vs immediate (pr:caplin#25198)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/payload_attestation_verification/gossip_verified_payload_attestation.rs:130-143`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_attestation_verification/gossip_verified_payload_attestation.rs#L130-L143) one signature set per message, signature_set.verify() called inline
- [`beacon_node/beacon_processor/src/lib.rs:474`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L474) Work::GossipPayloadAttestation(BlockingFn) is a single-item work type, no batch variant
- [`beacon_node/beacon_processor/src/lib.rs:373-392`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L373-L392) GossipAttestationBatch exists only for attestations/aggregates
- [`beacon_node/network/src/network_beacon_processor/mod.rs:512-523`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L512-L523) send_gossip_payload_attestation submits one message per work item

**Second check.** Searched payload_attestation_verification (no batch module, no verify_signature_sets call), beacon_processor work types and the network submit path; only the per-message path exists.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [silver#218](https://github.com/gattaca-com/silver/pull/218), [caplin#25198](https://github.com/erigontech/erigon/pull/25198)

</details>


<a id="bls-019"></a>
<details>
<summary><b>bls-019</b> Batch-verify gossip BLS-to-execution changes — <i>not · low · S · cpu</i></summary>

**Idea.** Verify BLS-to-execution-change gossip signatures through the shared batch verifier rather than inline one by one, amortizing pairing cost when many arrive at once.

**Gap in Lighthouse.** Add a batch work item for gossip_bls_to_execution_change_queue in beacon_processor that collects sets and calls bls::verify_signature_sets with a per-item fallback on failure.

**Impact.** Negligible on mainnet; BLS-change gossip is rare except in bursts after a fork. Saves a few ms of pairing time in those bursts.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2987`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2987) verify_bls_to_execution_change_for_gossip -&gt; single op validate
- [`beacon_node/beacon_chain/src/observed_operations.rs:125`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_operations.rs#L125) verify_and_observe validates one op at a time
- [`consensus/state_processing/src/per_block_processing/signature_sets.rs:183`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/signature_sets.rs#L183) bls_execution_change_signature_set builds a set, verified singly; beacon_processor gossip_bls_to_execution_change_queue has no batch path

**Sources.** [caplin#12441](https://github.com/erigontech/erigon/pull/12441), [nimbus#4637](https://github.com/status-im/nimbus-eth2/pull/4637), [teku#6736](https://github.com/Consensys-Incorporated/teku/pull/6736)

</details>


<a id="bls-020"></a>
<details>
<summary><b>bls-020</b> Verify aggregate-and-proof&#x27;s three signatures together — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Verify the selection proof, aggregator signature and aggregate signature of one aggregate-and-proof as a single batch multi-signature verification instead of three separate verifications.

**Impact.** Already done, and batched across aggregates.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:1440-1484`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1440-L1484) verify_signed_aggregate_signatures builds selection-proof, aggregator and aggregate sets and makes one verify_signature_sets call
- [`beacon_node/beacon_chain/src/attestation_verification/batch.rs:60-112`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification/batch.rs#L60-L112) gossip aggregate batch pushes all 3 sets per aggregate into one verify_signature_sets call
- [`beacon_node/beacon_chain/src/sync_committee_verification.rs:632-670`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/sync_committee_verification.rs#L632-L670) same three-set pattern for sync contributions

**Skeptic check.** Confirmed: the three signatures go through one RLC multi-pairing on the single and batch gossip paths, and for sync contributions too. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#11816](https://github.com/erigontech/erigon/pull/11816), [lodestar#2284](https://github.com/ChainSafe/lodestar/pull/2284)

</details>


<a id="bls-021"></a>
<details>
<summary><b>bls-021</b> Verify each gossip signature only once — <i>partial · medium · S · cpu</i></summary>

**Idea.** Verify gossip signatures only through the batch path, not individually and then again in a batch, so each signature is checked a single time.

**Gap in Lighthouse.** On the attestation and aggregate batch paths and on block import, each signature is checked once. But validate_data_column_sidecar_for_gossip_fulu -&gt; verify_proposer_and_signature does a full BLS verification of the same SignedBeaconBlockHeader signature for every gossip column of a block (8+ for a normal node, up to 128 for a supernode), and the gossip block has already checked the same proposer signature. Nothing caches the result by (block header root, signature). The only skip is for columns already in the DA checker (missing_cells_for_column_sidecar).

**Impact.** Saves about 1 BLS verification (~0.5-1 ms) per extra column sidecar per slot. A supernode does up to ~127 redundant verifications each slot, on the critical data-availability path.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification/batch.rs:53`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification/batch.rs#L53),109-112 batch success sets CheckAttestationSignature::No, so no re-verify
- [`beacon_node/beacon_chain/src/block_verification.rs:1285`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1285) include_all_signatures_except_proposal skips the proposer signature that was checked on gossip
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1185`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1185) validate_data_column_sidecar_for_gossip_fulu calls verify_proposer_and_signature for every column
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1772-1790`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1772-L1790) signed_block_header.verify_signature runs a full BLS verify on each call, with no cache keyed by header root or signature

**Skeptic check.** The attestation batch path does what lodestar#2770 asks: one verification on success, with an individual fallback only after a failed batch. The earlier check did not look at the data column sidecar path, where the identical header signature is verified again for each column.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lodestar#2770](https://github.com/ChainSafe/lodestar/pull/2770)

</details>


<a id="bls-022"></a>
<details>
<summary><b>bls-022</b> Batch-verify deposit signatures within a block — <i>not · low · M · cpu</i></summary>

**Idea.** Collect the deposit (and builder deposit request) signatures of a block and verify them in one batched BLS verification, using divide-and-conquer to find invalid ones, then apply them with a verified flag. One verification per block instead of one per deposit.

**Gap in Lighthouse.** Collect deposit signature sets for the block in process_deposits / process_deposit_requests and verify with verify_signature_sets, falling back to individual checks on failure, then apply with a verified flag.

**Impact.** Small: one signature check per new-validator deposit; blocks with many new deposits (up to 16 legacy, 8192 requests in Electra) would save pairings, but typical blocks have 0-few.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/process_operations.rs:702`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L702) process_deposits loops apply_deposit per deposit
- process_operations.rs:757 is_valid_deposit_signature called individually per new validator in apply_deposit

**Sources.** [prysm#16810](https://github.com/OffchainLabs/prysm/pull/16810), [prysm#6454](https://github.com/OffchainLabs/prysm/pull/6454), [prysm#17031](https://github.com/OffchainLabs/prysm/pull/17031), [teku#10708](https://github.com/Consensys-Incorporated/teku/pull/10708)

</details>


<a id="bls-023"></a>
<details>
<summary><b>bls-023</b> Cache deposit signature verification results — <i>implemented · low · S · cpu</i></summary>

**Idea.** Cache the outcome of deposit signature verification keyed by deposit data, so repeated or re-verified pending deposits (including at forks that re-check them) are BLS-verified at most once.

**Impact.** Already done (lighthouse#9817). Normal epoch processing (single_pass.rs:410) verifies each pending deposit once per transition and is capped at 16 per epoch.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/builder_deposits_cache.rs:42-150`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/builder_deposits_cache.rs#L42-L150) OnboardBuildersCache, an LRU keyed by DepositData tree_hash_root, pre-verified in batch
- [`consensus/state_processing/src/builder_deposits_cache.rs:164-191`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/builder_deposits_cache.rs#L164-L191) is_valid_deposit_signature_cached writes misses back to the cache
- [`consensus/state_processing/src/upgrade/gloas.rs:253-283`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/upgrade/gloas.rs#L253-L283) the fork upgrade uses the cache, plus a HashSet of valid pubkeys in place of repeated is_pending_validator scans
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:925-944`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L925-L944) process_builder_deposit_request has no pending-deposit re-scan, so it has no repeated verification to cache

**Skeptic check.** Grandine's cache targets repeated is_pending_validator scans in gloas deposit processing. Lighthouse has no such scan in block processing and caches the fork-upgrade checks, so the earlier verdict holds.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#9817](https://github.com/sigp/lighthouse/pull/9817), [grandine@7ea5ca346](https://github.com/grandinetech/grandine/commit/7ea5ca346e20)

</details>


<a id="bls-024"></a>
<details>
<summary><b>bls-024</b> Aggregate many pubkeys with batched point addition — <i>not · medium · S · cpu, latency</i></summary>

**Idea.** Sum large sets of public keys with the BLS library's batched affine point addition (shared field inversion, chunked across threads) instead of adding keys one by one or per-key FFI calls. Check the key aggregation path in block attestation verification.

**Gap in Lighthouse.** Use blst MultiPoint::add on a &amp;[PublicKey] slice in BlstAggregatePublicKey::aggregate and in verify_signature_sets for sets above a small threshold; keep the serial loop for tiny sets. Benchmark at committee sizes (~128-512 keys), where gains are smaller than the 32768-key headline.

**Impact.** Cheaper key aggregation for block attestation verification, gossip batches and 512-key sync aggregates, maybe 2-4x on that step; modest overall since pairings dominate BLS cost.

**Best measured result.** 32768 keys 15.8 -&gt; 1.8 ms (M3 Pro); 12.5 -&gt; 2.6 ms on Xeon E-2288G (pr:caplin#25542)

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/impls/blst.rs:177-183`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L177-L183) BlstAggregatePublicKey::aggregate calls blst AggregatePublicKey::aggregate(&amp;refs, false)
- [`crypto/bls/src/impls/blst.rs:95-106`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L95-L106) verify_signature_sets aggregates each set's signing keys with the same call
- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/blst-0.3.17/src/lib.rs:976-999 AggregatePublicKey::aggregate is a serial add_or_dbl_aff loop (one FFI call per key)
- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/blst-0.3.17/src/lib.rs:1721,2293 MultiPoint::add (batched affine addition) exists but no Lighthouse caller

**Second check.** Read the blst 0.3.17 aggregate source to confirm the prescreen claim (Lighthouse already uses batched addition) is false: the called path is per-key add_or_dbl_aff; grep found no MultiPoint or p1s_add use in crypto/, consensus/ or beacon_node/.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [caplin#25542](https://github.com/erigontech/erigon/pull/25542), [lighthouse#6178](https://github.com/sigp/lighthouse/pull/6178), [ethlambda#737](https://github.com/lambdaclass/ethlambda/pull/737)

</details>


<a id="bls-025"></a>
<details>
<summary><b>bls-025</b> Precompute committee pubkey sums and subtract non-attesters — <i>not · high · M · cpu, latency</i></summary>

**Idea.** Precompute each committee's aggregate pubkey once per shuffling, and for an attestation where most members attested derive the key as committee sum minus the missing members' keys, instead of summing every attester.

**Gap in Lighthouse.** Cache per-committee aggregate pubkey in the committee/shuffling cache and add a SignatureSet form 'committee sum minus missing keys' (needs G1 negation/subtraction in crypto/bls) handled in verify_signature_sets.

**Impact.** Cuts pubkey aggregation for high-participation attestations several-fold (~10x per source); a modest share of total verification CPU since pairings dominate.

**Best measured result.** Key aggregation with 5% missed 20-40x less (realistic ~10x), single-threaded loaded M3; key summation 12.3 ms CPU per block before on Ryzen 9700X (pr:ethlambda#742)

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/impls/blst.rs:88-103`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L88-L103) aggregates every signing key per set on each verify
- [`crypto/bls/src/impls/blst.rs:172-178`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L172-L178) AggregatePublicKey only has aggregate (no subtract/negate)
- [`consensus/types/src/state/beacon_state.rs:1843`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1843) only the sync committee aggregate_pubkey is precomputed, and it is not used for verification

**Second check.** Grepped crypto/bls, consensus and beacon_node for subtract/negate/AggregatePublicKey uses; no committee-sum cache or subtraction path exists anywhere, including blst wrapper.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [silver#163](https://github.com/gattaca-com/silver/pull/163), [ethlambda#742](https://github.com/lambdaclass/ethlambda/pull/742)

</details>


<a id="bls-026"></a>
<details>
<summary><b>bls-026</b> Pass validator indices to the verifier, aggregate pubkeys there — <i>n/a · low · cpu, latency</i></summary>

**Idea.** Put validator indices, not pubkey objects, in signature sets and let the verifier (worker or native BLS layer) look up and aggregate public keys from its own shared key cache. This removes pubkey fetching, serialization and per-key FFI or cross-thread transfer.

**Impact.** Lighthouse verifies in-process with Rust borrows from the shared pubkey cache, so there is no worker or FFI boundary for indices to avoid.

**Best measured result.** ~50% CPU improvement under normal gossip conditions (stated) (pr:lodestar#8946)

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/impls/blst.rs:28`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L28) verify_signature_sets runs in-process on borrowed keys
- [`beacon_node/beacon_chain/src/attestation_verification/batch.rs:73`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification/batch.rs#L73) pubkeys borrowed from ValidatorPubkeyCache via Cow::Borrowed

**Sources.** [lodestar@2f90603c1](https://github.com/ChainSafe/lodestar/commit/2f90603c1bd6), [lodestar#8803](https://github.com/ChainSafe/lodestar/pull/8803), [lodestar#8946](https://github.com/ChainSafe/lodestar/pull/8946), [lodestar#9820](https://github.com/ChainSafe/lodestar/pull/9820), [lodestar#9863](https://github.com/ChainSafe/lodestar/pull/9863), [lodestar#562](https://github.com/ChainSafe/lodestar/pull/562)

</details>


<a id="bls-027"></a>
<details>
<summary><b>bls-027</b> Optimise signature aggregation with benchmarks — <i>n/a · low · S · cpu</i></summary>

**Idea.** Optimise the signature aggregation routine, guided by dedicated BLS benchmarks; the record gives no specific mechanism.

**Impact.** Record names no mechanism; signature aggregation is already done by blst's assembly add and is a negligible share of CPU.

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/impls/blst.rs:200-260`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L200-L260) aggregate signature code is a thin wrapper over blst

**Sources.** [lodestar#406](https://github.com/ChainSafe/lodestar/pull/406)

</details>


<a id="bls-028"></a>
<details>
<summary><b>bls-028</b> Run pairing product on SIMD IFMA lanes — <i>not · medium · L · cpu, latency</i></summary>

**Idea.** Compute the pairing product of batched verification with AVX-512 IFMA lane arithmetic, using typed trusted-subgroup points so cached pubkeys are not re-checked.

**Gap in Lighthouse.** Requires a new BLS backend with AVX-512 IFMA field arithmetic behind crypto/bls traits.

**Impact.** Up to ~2x faster batch verification on IFMA CPUs only.

**Best measured result.** 1-vote flush 448.8 -&gt; 237.3 us (-47%); supernode verify_all per flush -48% (pr:silver#438)

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/impls/blst.rs:113-115`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L113-L115) single blst backend for batch pairing
- blst-0.3.17 source contains no ifma/avx512 code paths (grep empty)

**Second check.** Grepped the whole blst-0.3.17 crate for ifma/avx512 and Cargo.lock for alternative BLS crates; none found.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [silver#438](https://github.com/gattaca-com/silver/pull/438)

</details>


<a id="bls-029"></a>
<details>
<summary><b>bls-029</b> Decompress signatures in batches — <i>not · medium · L · cpu, latency</i></summary>

**Idea.** Decompress and subgroup-check gossip signatures several at a time using a batch decompression call or SIMD lanes, sharing field inversions, instead of one by one before batch verification.

**Gap in Lighthouse.** Add batched/SIMD signature decompression and subgroup checks (shared inversions) before verify_signature_sets; at minimum the serial subgroup_check loop could be moved into blst's parallel path (sigs_groupcheck=true).

**Impact.** Source reports 24-48% faster small gossip flushes; less with blst as baseline.

**Best measured result.** Mainnet supernode: non-empty flushes of 8-64 votes 24-48% faster; median 32-vote flush 1.6 ms vs 2.8 ms (pr:silver#371)

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/impls/blst.rs:195-197`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L195-L197) Signature::from_bytes per signature on decode
- [`crypto/bls/src/impls/blst.rs:71-74`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L71-L74) subgroup_check per signature, serially, before calling blst with sigs_groupcheck=false
- blst-0.3.17/src/lib.rs:1466 only single-point uncompress API

**Second check.** Confirmed blst offers no batch uncompress and attestation batch verification (attestation_verification/batch.rs) has no parallel decode; noticed subgroup checks run serially outside blst's thread pool.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [silver#371](https://github.com/gattaca-com/silver/pull/371), [prysm#10105](https://github.com/OffchainLabs/prysm/pull/10105)

</details>


<a id="bls-030"></a>
<details>
<summary><b>bls-030</b> Batch-validate pubkeys during state load — <i>partial · medium · L · startup, cpu</i></summary>

**Idea.** When loading state, decode and validate validator pubkeys in bounded batches with a batched (SIMD) G1 decoder instead of one at a time, cutting startup time.

**Gap in Lighthouse.** Keys are validated in parallel but individually; no batched SIMD G1 decoder. Incremental imports remain sequential.

**Impact.** First-startup only; rayon already gives most of the multi-core win; restarts avoid decompression.

**Best measured result.** ~2.3M keys decode+validate ~71s -&gt; ~15s on IFMA hosts (pr:silver#433)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:143-155`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L143-L155) rayon-parallel per-key decompress+validate on initial import
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:238-242`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L238-L242) restarts load uncompressed keys from DB
- [`crypto/bls/src/impls/blst.rs:130-138`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L130-L138) key_validate per key

**Second check.** Re-read the pubkey cache import path and DB load; state loads keep pubkeys as compressed bytes, so decoding only occurs in this cache, which is already parallel.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [silver#433](https://github.com/gattaca-com/silver/pull/433)

</details>


<a id="bls-031"></a>
<details>
<summary><b>bls-031</b> Select fast CPU-specific BLS paths at runtime — <i>implemented · low · S · cpu</i></summary>

**Idea.** Build or load the BLS library so it uses ADX/BMI2 (MULX) assembly paths when runtime CPU feature detection finds them, falling back to the portable build, so one binary gets the fast path where possible.

**Impact.** Release (portable) binaries already pick the ADX/MULX path at runtime.

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/registry/src/*/blst-0.3.17/build.rs:160-210 portable defines __BLST_PORTABLE__; the default build defines __ADX__ when the build host has ADX
- ~/.cargo/registry/src/*/blst-0.3.17/blst/build/assembly.S:8-22 under __BLST_PORTABLE__ both mulx and mulq objects are linked
- ~/.cargo/registry/src/*/blst-0.3.17/blst/build/elf/mulq_mont_384-x86_64.s:215-217 runtime jump to the mulx path when __blst_platform_cap (cpuid ADX bit, cpuid.c:41) is set
- Makefile:69 release cross builds use the portable feature
- [`lighthouse/Cargo.toml:18-21`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/Cargo.toml#L18-L21) portable / modern features

**Skeptic check.** Verified in blst 0.3.17: the portable build does cpuid-based runtime dispatch, and the default build picks ADX at build time from the build host. The earlier claim that the default build dispatches at runtime was slightly wrong, but the portable release binary does it, so the idea holds.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#4246](https://github.com/status-im/nimbus-eth2/pull/4246), [lighthouse#4624](https://github.com/sigp/lighthouse/pull/4624), [prysm#12720](https://github.com/OffchainLabs/prysm/pull/12720), [teku#4741](https://github.com/Consensys-Incorporated/teku/pull/4741)

</details>


<a id="bls-032"></a>
<details>
<summary><b>bls-032</b> Enable aarch64 carryless multiply in crypto — <i>n/a · low · S · cpu</i></summary>

**Idea.** Enable hardware carryless multiply on aarch64 for the crypto/signature backend.

**Impact.** The idea targets a different crypto backend (ethlambda); blst aarch64 asm needs no such flag.

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/impls/blst.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs) uses blst assembly, which has its own aarch64 paths; no Rust crypto backend with PMULL toggles in Lighthouse BLS

**Sources.** [ethlambda#606](https://github.com/lambdaclass/ethlambda/pull/606)

</details>


<a id="bls-033"></a>
<details>
<summary><b>bls-033</b> Aggregate-verify multiple messages with one multi-pairing — <i>implemented · low · S · cpu</i></summary>

**Idea.** Expose and use aggregate verification of many (message, pubkey) pairs against one aggregate signature, so one multi-pairing replaces many separate verifications.

**Impact.** No current consensus object is one aggregate over many messages. The old use case, phase0 custody-bit verify_multiple, is gone. Multi-set verification already uses one multi-pairing.

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/impls/blst.rs:270-281`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L270-L281) aggregate_verify of distinct messages against one aggregate signature, exposed through generic_aggregate_signature.rs:222
- [`crypto/bls/src/impls/blst.rs:36-117`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L36-L117) verify_signature_sets does one multi-pairing for many (msg, pubkeys, sig) sets

**Skeptic check.** aggregate_verify is exposed and used only by EF tests, because no production object needs it. The general one-multi-pairing goal is met by verify_signature_sets on block, attestation and aggregate paths.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@35ae1b674](https://github.com/sigp/lighthouse/commit/35ae1b6745bc), [lodestar@7b8b0fa97](https://github.com/ChainSafe/lodestar/commit/7b8b0fa97dd8)

</details>


<a id="bls-034"></a>
<details>
<summary><b>bls-034</b> Align signature types to 16 bytes — <i>n/a · low · cpu</i></summary>

**Idea.** Align signature types to 16 bytes so crypto routines can use aligned memory access.

**Impact.** blst manages its own point layout; Rust byte arrays are not alignment-constrained here.

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/impls/blst.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs): wraps blst_core types, no custom layout

**Sources.** [nimbus#5301](https://github.com/status-im/nimbus-eth2/pull/5301)

</details>


<a id="bls-035"></a>
<details>
<summary><b>bls-035</b> Use raw signature bytes instead of reserializing — <i>partial · low · S · cpu</i></summary>

**Idea.** Where only the original bytes of a signature are needed (e.g. aggregator selection check), use the raw bytes directly rather than deserializing and re-serializing.

**Gap in Lighthouse.** Selection proofs are deserialized from the wire and recompressed for is_aggregator; keep the raw 96 bytes (or take them from the SSZ container) and hash those in SelectionProof/SyncSelectionProof::is_aggregator_from_modulo.

**Impact.** One point compression (~tens of microseconds) saved per gossip aggregate and sync contribution; negligible overall.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/attestation/selection_proof.rs:54`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/attestation/selection_proof.rs#L54) hash(&amp;self.0.as_ssz_bytes())
- [`crypto/bls/src/generic_signature.rs:129`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/generic_signature.rs#L129) serialize recompresses point

**Sources.** [prysm#4298](https://github.com/OffchainLabs/prysm/pull/4298)

</details>


<a id="bls-036"></a>
<details>
<summary><b>bls-036</b> Copy BLS points without serialize roundtrip — <i>implemented · low · S · cpu</i></summary>

**Idea.** Clone public keys and signatures as in-memory structs instead of via serialize/deserialize round trips, and allocate domain buffers correctly.

**Best measured result.** Domain 29.5 ns/op -&gt; 7.55 ns/op (pr:prysm#5161)

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/generic_public_key.rs:45`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/generic_public_key.rs#L45) derive(Clone) over the in-memory blst point
- [`crypto/bls/src/generic_signature.rs:67`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/generic_signature.rs#L67) derive(Clone)
- [`crypto/bls/src/impls/blst.rs:137-142`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L137-L142) aggregate pubkey clone via to_public_key/from_public_key (affine conversion, no bytes)
- [`crypto/bls/src/impls/blst.rs:213-217`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L213-L217) aggregate signature clone the same way
- [`consensus/types/src/core/chain_spec.rs:724-735`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/core/chain_spec.rs#L724-L735) compute_domain writes into a fixed [u8; 32]

**Skeptic check.** Confirmed: no serialize/deserialize round trip in any clone, and the domain is built in a stack array. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#5161](https://github.com/OffchainLabs/prysm/pull/5161), [prysm#4770](https://github.com/OffchainLabs/prysm/pull/4770)

</details>


<a id="bls-037"></a>
<details>
<summary><b>bls-037</b> Pass BLS points by reference, avoid copies — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** When building signature sets, aggregating public keys and in aggregate verification, borrow cached pubkeys and signatures by reference and convert directly into aggregate types instead of cloning curve points. Each avoided clone saves a copy of a 96- or 192-byte point.

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/generic_signature_set.rs:68-69`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/generic_signature_set.rs#L68-L69) signature and signing_keys are Cow
- [`beacon_node/beacon_chain/src/attestation_verification/batch.rs:73`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification/batch.rs#L73) Cow::Borrowed from pubkey cache
- [`beacon_node/beacon_chain/src/block_verification.rs:2236-2241`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L2236-L2241) block verifier borrows cached pubkeys
- [`beacon_node/beacon_chain/src/sync_committee_verification.rs:641`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/sync_committee_verification.rs#L641),649-652,685 sync paths borrow
- [`beacon_node/beacon_chain/src/historical_blocks.rs:404`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_blocks.rs#L404) backfill clones one proposer pubkey per block (lock released before verify)

**Skeptic check.** Confirmed: the hot paths (gossip attestations, aggregates, sync messages, block import) borrow cached keys. The only clone is backfill, at one 96-byte point per block, which lets the cache lock drop before verify; it does not matter.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#12944](https://github.com/OffchainLabs/prysm/pull/12944), [lighthouse#985](https://github.com/sigp/lighthouse/pull/985), [lighthouse#8610](https://github.com/sigp/lighthouse/pull/8610)

</details>


<a id="bls-038"></a>
<details>
<summary><b>bls-038</b> Compare BLS keys by compressed bytes — <i>implemented · low · S · cpu</i></summary>

**Idea.** Implement equality for BLS public keys and signatures by comparing compressed bytes instead of deserialized points.

**Impact.** Negligible. Hot-path comparisons use PublicKeyBytes/SignatureBytes, which are plain byte compares.

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/generic_public_key.rs:105-109`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/generic_public_key.rs#L105-L109) PartialEq compares serialize() (compressed) bytes
- [`crypto/bls/src/generic_public_key_bytes.rs:96-99`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/generic_public_key_bytes.rs#L96-L99) and generic_signature_bytes.rs:81 byte equality for the byte forms used on hot paths
- [`crypto/bls/src/generic_signature.rs:67`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/generic_signature.rs#L67) derived PartialEq over the blst affine point (a direct coordinate compare, no decompression)

**Skeptic check.** Public key equality uses compressed bytes. Signature equality compares affine points, which is no slower than a byte compare. The earlier note about signatures is accurate but is not a performance gap.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#306](https://github.com/sigp/lighthouse/pull/306)

</details>


<a id="bls-039"></a>
<details>
<summary><b>bls-039</b> Avoid exceptions on pubkey cache miss — <i>n/a · low · cpu</i></summary>

**Idea.** On a pubkey decompression cache miss use a lookup-with-fallback API rather than exception-based control flow on the hot path.

**Impact.** Rust uses Option lookups, no exception control flow.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:179`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L179) get_pubkey_from_pubkey_bytes returns Option

**Sources.** [nimbus#1479](https://github.com/status-im/nimbus-eth2/pull/1479)

</details>


<a id="bls-040"></a>
<details>
<summary><b>bls-040</b> Verify directly from compressed bytes natively — <i>partial · low · M · cpu, memory</i></summary>

**Idea.** Pass compressed pubkey and signature bytes straight to the native verifier for block production, sync reward, bid and deposit signatures, instead of materializing deserialized key wrapper objects; respect the native batch size limit.

**Gap in Lighthouse.** Verification goes through deserialized PublicKey/Signature wrappers; blst has no compressed-byte verify path used. Gain only for rare signatures (deposits, bids); wrappers already deserialize once and pubkeys come from a decompressed cache.

**Impact.** Negligible; the hot attestation/block paths use the decompressed pubkey cache, which is faster than passing compressed bytes.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/verify_deposit.rs:23`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/verify_deposit.rs#L23) deposit sig via deserialized PublicKey
- [`crypto/bls/src/impls/blst.rs:113`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L113) batch takes deserialized points

**Sources.** [lodestar#9881](https://github.com/ChainSafe/lodestar/pull/9881)

</details>


<a id="bls-041"></a>
<details>
<summary><b>bls-041</b> Cap batch size at the native verifier limit — <i>n/a · medium · cpu</i></summary>

**Idea.** Cap the number of signature sets in one verification package at the native verifier's limit, so packages do not overshoot and fall back to slower individual verification.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:110`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L110) gossip batches capped at 64
- blst-0.3.17/src/lib.rs:1337 blst imposes no cap on set count (chunks internally)

**Sources.** [lodestar#9846](https://github.com/ChainSafe/lodestar/pull/9846)

</details>


<a id="bls-042"></a>
<details>
<summary><b>bls-042</b> Avoid stream overhead in batch verify code — <i>n/a · low · cpu</i></summary>

**Idea.** In batch BLS verification glue code, avoid the slower IntStream-style collection handling in favour of plain collections, as measured in production.

**Impact.** Rust iterators have no stream overhead; Java-specific.

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/impls/blst.rs:95-120`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L95-L120) plain Vec collections in batch glue

**Sources.** [teku#5591](https://github.com/Consensys-Incorporated/teku/pull/5591)

</details>


<a id="bls-043"></a>
<details>
<summary><b>bls-043</b> Use library EIP-2333 key derivation — <i>not · low · S · cpu</i></summary>

**Idea.** Derive keys per EIP-2333 with the BLS library's built-in implementation instead of a slower generic one.

**Gap in Lighthouse.** Replace BigUint mod_r and Lamport derivation with blst's keygen/derive_child (blst::min_pk::SecretKey::derive_child_eip2333) in derived_key.rs.

**Impact.** Only wallet/keystore tooling (account manager); no effect on a running node.

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/eth2_key_derivation/src/derived_key.rs:79`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/eth2_key_derivation/src/derived_key.rs#L79) derive_child_sk hand-written with num-bigint, sha2, hkdf
- derived_key.rs:121 mod_r uses BigUint

**Sources.** [nimbus@c4e5cd9f0](https://github.com/status-im/nimbus-eth2/commit/c4e5cd9f06e3)

</details>


<a id="bls-044"></a>
<details>
<summary><b>bls-044</b> Subgroup-check each pubkey once and reuse it — <i>implemented · medium · S · cpu, memory</i></summary>

**Idea.** Validate each public key (infinity and subgroup check) once when first seen, record or cache the validated object, and reuse it for sync committee and other verification, aggregating trusted keys with plain point addition. Expensive group checks and re-deserialization are not repeated.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:21-26`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L21-L26) decompressed (key_validate) keys held once per validator
- [`crypto/bls/src/impls/blst.rs:93`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L93),165 aggregate(&amp;keys,false) with no repeated group check
- [`crypto/bls/src/impls/blst.rs:122-131`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L122-L131) subgroup check happens only in deserialize
- [`beacon_node/beacon_chain/src/sync_committee_verification.rs:652`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/sync_committee_verification.rs#L652),685 sync verification reads keys from the cache
- [`beacon_node/beacon_chain/src/block_verification.rs:2250-2255`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L2250-L2255) block sync-aggregate decompressor maps bytes to the cache
- [`consensus/state_processing/src/per_block_processing/signature_sets.rs:61-76`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/signature_sets.rs#L61-L76) get_pubkey_from_state decompresses and validates again (gossip exits and slashings via verify_operation.rs:222,240,261)

**Skeptic check.** Confirmed: on every hot path, keys are validated once into the cache and aggregated with plain addition. Gossip exit, slashing and BLS-change validation still decompress from the state (get_pubkey_from_state), but those messages are rare, so the idea is effectively complete.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#4075](https://github.com/Consensys-Incorporated/teku/pull/4075), [teku#4836](https://github.com/Consensys-Incorporated/teku/pull/4836), [prysm#7971](https://github.com/OffchainLabs/prysm/pull/7971), [lighthouse#1979](https://github.com/sigp/lighthouse/pull/1979)

</details>


<a id="bls-045"></a>
<details>
<summary><b>bls-045</b> Cheaper secret key zero check and marshal — <i>n/a · low · S · cpu</i></summary>

**Idea.** Marshal secret keys without padding and use a dedicated zero-key check instead of a generic comparison.

**Impact.** Secret keys are only handled at validator-client keystore load and signing; no hot path on a beacon node.

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/impls/blst.rs:300`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L300) secret key serialize is blst to_bytes (fixed 32 bytes, no padding)

**Sources.** [prysm#9022](https://github.com/OffchainLabs/prysm/pull/9022)

</details>


<a id="bls-046"></a>
<details>
<summary><b>bls-046</b> Compress aggregated proofs on the wire — <i>n/a · low · L · bandwidth</i></summary>

**Idea.** Serialize aggregated signature proofs with compact encoding plus lz4 compression to shrink them on the wire.

**Impact.** Lean-consensus proof aggregation does not exist in Lighthouse mainnet; no wire format to compress.

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.toml:238 snap only; no aggregated-proof type in [`consensus/types`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types)

**Sources.** [ethlambda#411](https://github.com/lambdaclass/ethlambda/pull/411)

</details>


<a id="bls-047"></a>
<details>
<summary><b>bls-047</b> Bump proof-system dependency for prover speedups — <i>n/a · low · S · cpu, memory</i></summary>

**Idea.** Update the proof-system/aggregation dependency to revisions with prover performance fixes, such as avoiding a serial 256 MiB weights copy.

**Impact.** No zk proof-system dependency in Lighthouse.

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/impls/blst.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs) no proof-system dependency

**Sources.** [ethlambda#408](https://github.com/lambdaclass/ethlambda/pull/408), [ethlambda#421](https://github.com/lambdaclass/ethlambda/pull/421)

</details>


<a id="bls-048"></a>
<details>
<summary><b>bls-048</b> Call native BLS library without abstraction layer — <i>n/a · low · S · cpu</i></summary>

**Idea.** Use the native BLS library directly instead of through a generic abstraction layer, so serialization and validation steps can be skipped where inputs are trusted.

**Impact.** Lighthouse is Rust and already calls blst natively; the generic wrapper is zero-cost generics, with trusted pubkeys deserialized without re-validation from the validator pubkey cache.

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/impls/blst.rs:1-120`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L1-L120) calls blst crate directly

**Sources.** [lodestar#6706](https://github.com/ChainSafe/lodestar/pull/6706)

</details>


<a id="bls-049"></a>
<details>
<summary><b>bls-049</b> Fast G2 cofactor clearing and subgroup check — <i>implemented · low · S · cpu, sync</i></summary>

**Idea.** Use endomorphism-based G2 cofactor clearing in hash-to-G2 and the fast subgroup membership test, so hashing messages and checking signatures is cheaper.

**Best measured result.** hash-to-G2 more than doubled; syncing first 12k blocks ~16% faster (pr:teku#1827)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/blst-0.3.17/blst/src/map_to_g2.c:326-340 clear_cofactor uses the psi endomorphism (Budroni-Pintore)
- blst-0.3.17/blst/src/map_to_g2.c:403-429 POINTonE2_in_G2 uses Scott's psi(P) == [z]P test
- [`crypto/bls/src/impls/blst.rs:12`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L12) blst::min_pk

**Skeptic check.** Confirmed in the blst 0.3.17 sources: endomorphism-based cofactor clearing and a fast G2 subgroup test. The slow h_eff path is under #if 0.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#1827](https://github.com/Consensys-Incorporated/teku/pull/1827)

</details>


<a id="bls-050"></a>
<details>
<summary><b>bls-050</b> Keep decompressed pubkeys in BLS change messages — <i>not · low · M · cpu</i></summary>

**Idea.** Store the decompressed public key with BLS-to-execution-change messages (e.g. in the op pool) so re-verification clones a key instead of decompressing it each time.

**Gap in Lighthouse.** Changing BlsToExecutionChange.from_bls_pubkey to a decompressed key would alter the SSZ type; alternatively cache the decompressed key in SigVerifiedOp. Not worthwhile.

**Impact.** Saves one G1 decompression (~tens of microseconds) per change; changes are rare and verified once on gossip, once in block import. Negligible.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/signature_sets.rs:183-205`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/signature_sets.rs#L183-L205) bls_execution_change_signature_set decompresses from_bls_pubkey on every call
- lighthouse#4190 closed unmerged
- [`beacon_node/operation_pool/src/bls_to_execution_changes.rs:25`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/bls_to_execution_changes.rs#L25) pool stores SigVerifiedOp of the SignedBlsToExecutionChange with PublicKeyBytes

**Sources.** [lighthouse#4190](https://github.com/sigp/lighthouse/pull/4190)

</details>


<a id="bls-051"></a>
<details>
<summary><b>bls-051</b> Faster batch signature verification (unspecified) — <i>n/a · low · S · cpu</i></summary>

**Idea.** Speed up batch signature verification; the record does not describe the mechanism.

**Gap in Lighthouse.** The source PR (prysm#7287, closed unmerged, empty description, no diff in the corpus) does not describe a mechanism, so there is nothing specific to compare against.

**Impact.** Unknown; no mechanism to evaluate.

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/impls/blst.rs:36-117`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L36-L117) verify_signature_sets already uses random-scalar batch verification

**Skeptic check.** show.py shows an empty PR body and no diff, so the idea cannot be verified as implemented or not. Lighthouse does have generic RLC batch verification, but calling an unspecified idea implemented is not supportable.

**Verdict history.** implemented (checked) → n/a (skeptic)

**Sources.** [prysm#7287](https://github.com/OffchainLabs/prysm/pull/7287)

</details>


<a id="bls-052"></a>
<details>
<summary><b>bls-052</b> SHA-256 instead of keccak in hash-to-G2 — <i>n/a · low · S · cpu</i></summary>

**Idea.** Hash the message with SHA-256 rather than keccak256 when hashing to the G2 curve point. SHA-256 is faster and has hardware support, and it removes a native keccak dependency.

**Impact.** Lighthouse already hashes to G2 with SHA-256 per the spec DST; no keccak involved.

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/impls/blst.rs:14`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L14) DST is spec fixed SHA-256 XMD

**Sources.** [lodestar@d88a39b71](https://github.com/ChainSafe/lodestar/commit/d88a39b71ee3)

</details>


<a id="bls-053"></a>
<details>
<summary><b>bls-053</b> Verify deposit signatures only when the outcome depends on it — <i>partial · low · S · cpu, memory</i></summary>

**Idea.** When processing deposit requests or pending deposits (including Gloas builder onboarding), skip BLS signature verification for deposits whose result does not depend on it (pubkey already known or already pending, non-builder credentials), using a pubkey-to-index map. Only deposits that can create a new validator or builder pay for a pairing.

**Gap in Lighthouse.** onboard_builders_from_pending_deposits (upgrade/gloas.rs:268-273) calls is_valid_deposit_signature_cached for every non-builder deposit of an unknown pubkey. That result only matters if a later builder-credential deposit has the same pubkey; nimbus#8686 checks it lazily only then. OnboardBuildersCache::add_new_pending_deposits/seed_from_state likewise batch-verify every pending deposit instead of only builder deposits plus same-pubkey validator deposits (lighthouse#9946, closed wontfix). process_builder_deposit_request uses an O(n) builders().iter().position instead of a pubkey-to-index map.

**Impact.** Removes BLS verifications of ordinary validator deposits in the pre-Gloas window and at the fork transition; the cache already moves most of this work off the critical path.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/process_operations.rs:736-760`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L736-L760) apply_deposit verifies only for unknown pubkeys
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:403-410`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L403-L410) pending deposits verify only if the validator is unknown
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:920-934`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L920-L934) builder deposit skips non-builder credentials and known builders, but finds builders by linear .position() scan
- [`consensus/state_processing/src/upgrade/gloas.rs:266-273`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/upgrade/gloas.rs#L266-L273) onboarding verifies every non-builder new-validator pending deposit
- [`consensus/state_processing/src/builder_deposits_cache.rs:89-131`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/builder_deposits_cache.rs#L89-L131),193-218 OnboardBuildersCache pre-verifies every new pending deposit per slot, unfiltered

**Skeptic check.** The block and epoch deposit paths do skip verification as the earlier evidence says. The Gloas builder-onboarding path does not: the cache and the fork upgrade verify every pending deposit, and the LH member PR #9946 that would filter it was closed unmerged.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lighthouse#9946](https://github.com/sigp/lighthouse/pull/9946), [nimbus#8557](https://github.com/status-im/nimbus-eth2/pull/8557), [nimbus#8686](https://github.com/status-im/nimbus-eth2/pull/8686)

</details>


<a id="bls-054"></a>
<details>
<summary><b>bls-054</b> Fixed-size arrays for BLS serialization — <i>implemented · low · S · cpu</i></summary>

**Idea.** Return fixed-size byte arrays instead of heap-allocated Vecs from BLS public key and signature serialization and SSZ encode/decode. This removes one heap allocation per serialized key or signature.

**Best measured result.** considerably increases serialisation speeds (pr:lighthouse#1183)

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/impls/blst.rs:109`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L109) PublicKey serialize -&gt; [u8; PUBLIC_KEY_BYTES_LEN]
- [`crypto/bls/src/impls/blst.rs:192`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L192) Signature serialize -&gt; [u8; SIGNATURE_BYTES_LEN]
- [`crypto/bls/src/generic_public_key_bytes.rs:20-21`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/generic_public_key_bytes.rs#L20-L21) PublicKeyBytes holds [u8; N]
- [`crypto/bls/src/macros.rs:46`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/macros.rs#L46) ssz_append extends buf from the array

**Skeptic check.** Confirmed: serialization returns fixed arrays and SSZ appends them directly. Only Debug/Display formatting calls to_vec.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#1183](https://github.com/sigp/lighthouse/pull/1183)

</details>


<a id="bls-055"></a>
<details>
<summary><b>bls-055</b> Populate pubkey cache only when enabled — <i>n/a · low · S · memory, cpu</i></summary>

**Idea.** Insert into the BLS pubkey deserialization cache only when that cache is enabled, so disabled configurations do not pay the memory and insertion cost.

**Impact.** Lighthouse has no global BLS deserialization cache to toggle; decompressed keys live in the validator pubkey cache which is always needed.

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src)/ no deserialization cache (grep pubkey_cache finds none); [`beacon_node/beacon_chain`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain) validator_pubkey_cache holds decompressed keys by index

**Sources.** [prysm#4195](https://github.com/OffchainLabs/prysm/pull/4195)

</details>


<a id="bls-056"></a>
<details>
<summary><b>bls-056</b> Cheaper public key hashing for hash maps — <i>partial · low · S · cpu</i></summary>

**Idea.** Hash public keys from their raw (or stored uncompressed) native byte form instead of SSZ-encoding them first. Pubkey hashing in hash maps then avoids a compression and encoding step per lookup.

**Gap in Lighthouse.** GenericPublicKey::hash still compresses the point; hash serialize_uncompressed or cache bytes instead.

**Impact.** Only affects HashSet&lt;PublicKey&gt; in VC/account tooling, not the BN hot path; negligible.

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/generic_public_key_bytes.rs:102`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/generic_public_key_bytes.rs#L102) PublicKeyBytes hashes raw bytes
- [`crypto/bls/src/generic_public_key.rs:113`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/generic_public_key.rs#L113) PublicKey Hash calls serialize() (compress)
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:26`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L26) hot index map keyed by PublicKeyBytes

**Sources.** [lighthouse@7e79a2b3d](https://github.com/sigp/lighthouse/commit/7e79a2b3d310), [lighthouse@bfa2e71b4](https://github.com/sigp/lighthouse/commit/bfa2e71b468e)

</details>


<a id="bls-057"></a>
<details>
<summary><b>bls-057</b> Larger gossip signature batch size limit — <i>partial · medium · S · cpu</i></summary>

**Idea.** Raise the maximum number of signature sets per batch verification for gossip attestations (e.g. 50 to 1000, or up to the native verifier bound) so more sets share one multi-pairing and final exponentiation.

**Gap in Lighthouse.** The configurable limit (what Prysm #15467 added) already exists as hidden CLI flags; only the default is still 64. Remaining work: benchmark larger defaults (e.g. 256-1000) and raise them. Batches only form from queue depth (no time-based accumulation), so a higher cap only matters when the queue is deep.

**Impact.** Fewer final exponentiations under deep attestation queues; Prysm saw 6-16% CPU going 50-&gt;1000, likely less here since 64 already amortises most of the cost and blst parallelises within a batch.

**Best measured result.** -16% CPU no-validator, -6% validator mode (pr:prysm#15467)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/src/cli.rs:1654-1664`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L1654-L1664) hidden flag --beacon-processor-attestation-batch-size (default 64)
- [`beacon_node/src/cli.rs:1666-1677`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L1666-L1677) hidden flag --beacon-processor-aggregate-batch-size (default 64)
- [`beacon_node/src/config.rs:888-895`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/config.rs#L888-L895) flags feed BeaconProcessorConfig
- [`beacon_node/beacon_processor/src/lib.rs:99-111`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L99-L111) DEFAULT_MAX_GOSSIP_*_BATCH_SIZE = 64 with poisoning trade-off comment
- [`beacon_node/beacon_processor/src/lib.rs:1018-1034`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1018-L1034) batch_size = min(queue len, configured max)

**Second check.** Earlier review missed the hidden --beacon-processor-attestation-batch-size / --beacon-processor-aggregate-batch-size flags in cli.rs and config.rs, which make the limit operator-configurable exactly like Prysm's change; the default value is the only remaining difference.

**Verdict history.** not (checked) → partial (refuted)

**Sources.** [lodestar#9849](https://github.com/ChainSafe/lodestar/pull/9849), [prysm#15467](https://github.com/OffchainLabs/prysm/pull/15467)

</details>


<a id="bls-058"></a>
<details>
<summary><b>bls-058</b> Lazy pubkey and signature decompression — <i>implemented · medium · S · cpu, sync, startup</i></summary>

**Idea.** Keep validator pubkeys and deposit signatures as raw compressed bytes in decoded state and decompress/validate them only on first use (in place or via a cache). Loading a BeaconState from disk then no longer decompresses every key, which was a third or more of sync CPU.

**Best measured result.** pubkey init was 1/3 or more of sync CPU; getState() nearly disappears from the perf trace (pr:nimbus#1369)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/validator/validator.rs:22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/validator/validator.rs#L22) Validator.pubkey is PublicKeyBytes
- [`consensus/types/src/deposit/deposit_data.rs:20-24`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/deposit/deposit_data.rs#L20-L24) and pending deposit signature are SignatureBytes
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:21-26`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L21-L26) decompressed keys live only in the cache
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:54-80`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L54-L80) cache loaded from the store, not from state decode

**Skeptic check.** Confirmed: decoding a BeaconState never decompresses keys or signatures, and decompression happens once per validator into the cache. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#472](https://github.com/sigp/lighthouse/pull/472), [nimbus#1371](https://github.com/status-im/nimbus-eth2/pull/1371), [nimbus@db397cc5f](https://github.com/status-im/nimbus-eth2/commit/db397cc5f377), [nimbus#1369](https://github.com/status-im/nimbus-eth2/pull/1369), [nimbus@c142de4b7](https://github.com/status-im/nimbus-eth2/commit/c142de4b7f40)

</details>


<a id="bls-059"></a>
<details>
<summary><b>bls-059</b> Dispatch BLS jobs to lowest-latency worker — <i>n/a · low · latency, cpu</i></summary>

**Idea.** In a BLS verification worker pool, track recent per-job latency per worker and send the next job to the worker with the lowest latency, avoiding workers whose CPU is contended.

**Gap in Lighthouse.** Lighthouse uses blst's native thread pool with dynamic work-stealing via counter; no JS worker pool exists.

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/registry/src/*/blst-0.3.17/src/lib.rs:1337 blst uses native da_pool with shared atomic work counter

**Sources.** [lodestar#4720](https://github.com/ChainSafe/lodestar/pull/4720)

</details>


<a id="bls-060"></a>
<details>
<summary><b>bls-060</b> Plain map instead of LRU for pubkey cache — <i>implemented · low · S · memory</i></summary>

**Idea.** Store decompressed validated pubkeys in a plain map behind a mutex instead of an LRU cache, since the working set (all validators) is never usefully evicted. This drops the LRU bookkeeping heap.

**Impact.** Already done: the cache holds every validator key permanently in a Vec indexed by validator index, so there is no LRU bookkeeping.

**Best measured result.** cache memory 222 MB -&gt; 158 MB (-64 MB) (pr:prysm#16654)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:24-29`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L24-L29) pubkeys: Vec&lt;PublicKey&gt;, indices: HashMap&lt;PublicKeyBytes, usize&gt;, pubkey_bytes: Vec, no LRU and no eviction
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:174-176`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L174-L176) get(i) is a plain Vec index
- [`beacon_node/beacon_chain/src/beacon_chain.rs:507`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L507) RwLock&lt;ValidatorPubkeyCache&lt;T&gt;&gt;

**Skeptic check.** Confirmed that the pubkey cache is a plain Vec plus HashMap with no eviction. The earlier evidence is right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#16654](https://github.com/OffchainLabs/prysm/pull/16654)

</details>


<a id="bls-061"></a>
<details>
<summary><b>bls-061</b> Reuse buffers in batch verification, no per-call allocation — <i>partial · low · S · cpu, memory</i></summary>

**Idea.** In batch BLS verification and job dispatch, use preallocated pooled buffers, stack buffers sized to the typical batch (about 32 sets), or one fixed-size per-job struct instead of several heap arrays per call. This cuts allocator churn on the hot verification path.

**Gap in Lighthouse.** Allocations are sized up front but fresh per call, with an extra per-set signing_keys Vec and a sets Vec. Use SmallVec or reusable buffers in verify_signature_sets.

**Impact.** Slightly less allocator traffic per batch; negligible CPU on a mainnet node next to the pairing work.

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/impls/blst.rs:39`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L39) collects sets into a Vec
- [`crypto/bls/src/impls/blst.rs:47-50`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L47-L50) four Vec::with_capacity per call
- [`crypto/bls/src/impls/blst.rs:94`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L94) per-set Vec of pk refs

**Sources.** [lodestar@a10477b4b](https://github.com/ChainSafe/lodestar/commit/a10477b4b8ac), [lodestar@459750fec](https://github.com/ChainSafe/lodestar/commit/459750fecfa8), [lodestar@dfda58c32](https://github.com/ChainSafe/lodestar/commit/dfda58c32c2b), [lodestar@59db04a01](https://github.com/ChainSafe/lodestar/commit/59db04a01611)

</details>


<a id="bls-062"></a>
<details>
<summary><b>bls-062</b> Raise default BLS verification threads and queue size — <i>n/a · medium · cpu, latency</i></summary>

**Idea.** Set higher default (and minimum) thread counts and queue capacity for batch signature verification so nodes subscribed to many subnets do not drop or starve gossip signature batches.

**Gap in Lighthouse.** Lighthouse has no separate BLS thread pool or BLS queue; verification runs on beacon processor workers sized to CPU count.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:130`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L130) max_workers = num_cpus
- [`crypto/bls/src/impls/blst.rs:36`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L36) verify_signature_sets runs on the calling worker

**Sources.** [teku#7623](https://github.com/Consensys-Incorporated/teku/pull/7623), [teku#9287](https://github.com/Consensys-Incorporated/teku/pull/9287)

</details>


<a id="bls-063"></a>
<details>
<summary><b>bls-063</b> BLS on native thread pool, not JS workers — <i>n/a · low · cpu, latency</i></summary>

**Idea.** Run BLS verification through a native binding on the runtime's native thread pool instead of host-language worker threads, passing deserialized key and signature objects with no serialization or message passing across thread boundaries.

**Gap in Lighthouse.** Already native Rust; pubkeys are deserialized points in pubkey cache, nothing crosses a serialization boundary.

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/impls/blst.rs:36`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L36) native blst call, no worker serialization

**Sources.** [lodestar#6616](https://github.com/ChainSafe/lodestar/pull/6616), [lodestar#6894](https://github.com/ChainSafe/lodestar/pull/6894), [lodestar#5493](https://github.com/ChainSafe/lodestar/pull/5493), [lodestar#6350](https://github.com/ChainSafe/lodestar/pull/6350), [lodestar#5633](https://github.com/ChainSafe/lodestar/pull/5633)

</details>


<a id="bls-064"></a>
<details>
<summary><b>bls-064</b> Verify block attestation signatures in parallel — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** During block import, verify the aggregated signatures of the block's attestations concurrently across cores (after preparing inputs sequentially) instead of one after another, failing on the first invalid one. Block import latency then scales down with cores.

**Impact.** Already done: block attestation signature checks (hash-to-curve and Miller loops) run on all cores in the blst thread pool and stop early on the first invalid set.

**Best measured result.** 36 attestations ~1.4-1.9s sequential; expected ~4x on 4 cores (pr:ethlambda#274)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/block_signature_verifier.rs:439-460`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/block_signature_verifier.rs#L439-L460) ParallelSignatureSets::verify sends all block sets to one verify_signature_sets call
- [`crypto/bls/src/impls/blst.rs:36-117`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L36-L117) verify_signature_sets prepares inputs sequentially, then calls Signature::verify_multiple_aggregate_signatures
- ~/.cargo/registry/src/*/blst-0.3.17/src/lib.rs:1316-1389 std impl: min(pool.max_count(), n) workers on da_pool pull sets by atomic counter, run mul_n_aggregate, stop early on an invalid set through a shared AtomicBool, merge the pairings and run one finalverify
- ~/.cargo/registry/src/*/blst-0.3.17/src/lib.rs:35-50 da_pool = ThreadPool::default() (one thread per CPU); [`crypto/bls/Cargo.toml:18`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/Cargo.toml#L18) does not enable no-threads

**Second check.** Read the blst 0.3.17 Rust binding source: verify_multiple_aggregate_signatures is multithreaded over a per-CPU threadpool with early abort, so the earlier 'no rayon' finding was wrong; parallelism lives in the dependency crate, not in Lighthouse code.

**Skeptic check.** Confirmed that blst runs the per-set work in parallel and stops early. The idea itself keeps input preparation sequential. The Lighthouse loop in blst.rs:51-103 does the G2 subgroup checks and the pubkey aggregation (AggregatePublicKey::aggregate) one set after another; for Electra block attestations of about 31k keys each this residue can reach roughly 10-20 ms, but that is beyond the idea as stated.

**Verdict history.** not (checked) → implemented (refuted) → implemented (skeptic)

**Sources.** [caplin#7709](https://github.com/erigontech/erigon/pull/7709), [ethlambda#274](https://github.com/lambdaclass/ethlambda/pull/274)

</details>


<a id="bls-065"></a>
<details>
<summary><b>bls-065</b> Preallocate signature-set vectors with known capacity — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Allocate the pubkey and signature-set vectors used in block, attestation and aggregate verification with their known final length instead of growing them by pushes, avoiding repeated reallocations.

**Impact.** Already done; at most a negligible residue.

**Best measured result.** negligible improvement to init sync (pr:prysm#6285)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification/batch.rs:62`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification/batch.rs#L62),168 Vec::with_capacity for the batch signature sets
- [`consensus/state_processing/src/per_block_processing/signature_sets.rs:306`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/signature_sets.rs#L306),339,389,752 pubkey vecs with_capacity(attesting_indices_len / subcommittee size)
- [`crypto/bls/src/impls/blst.rs:47-50`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L47-L50) rands/msgs/sigs/pks with_capacity(sets.len())

**Skeptic check.** Confirmed preallocation on the attestation, aggregate and sync paths and in the blst wrapper. Only the block-level ParallelSignatureSets vec (block_signature_verifier.rs:97-126) grows by push, but it holds a few dozen entries, so this is negligible.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#15261](https://github.com/OffchainLabs/prysm/pull/15261), [prysm#6285](https://github.com/OffchainLabs/prysm/pull/6285), [lighthouse#2184](https://github.com/sigp/lighthouse/pull/2184), [lighthouse#1922](https://github.com/sigp/lighthouse/pull/1922)

</details>


<a id="bls-066"></a>
<details>
<summary><b>bls-066</b> Preassigned per-worker result slots in batch verify — <i>n/a · low · cpu</i></summary>

**Idea.** Give each batch-verify thread a result slot indexed by worker id and write its pairing state directly there, removing the shared atomic result counter and an extra stack-buffer copy.

**Gap in Lighthouse.** Batch verify thread pool lives inside the blst crate; Lighthouse cannot change it and the gain is micro.

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/registry/src/*/blst-0.3.17/src/lib.rs:1338-1369 counter/valid atomics inside blst

**Sources.** [lodestar@6fe5c3fb4](https://github.com/ChainSafe/lodestar/commit/6fe5c3fb4fdc)

</details>


<a id="bls-067"></a>
<details>
<summary><b>bls-067</b> Precompute fork-data roots for domain derivation — <i>not · low · S · cpu</i></summary>

**Idea.** Precompute the fork-data roots for the few fork versions a node can see, so computing a BLS signing domain is a lookup instead of a hash per message.

**Gap in Lighthouse.** Cache fork_data_root per (fork_version, genesis_validators_root) in ChainSpec or a small map, and use it in compute_domain. Only compute_domain and get_domain need to change.

**Impact.** One SHA-256 hash of a small container per signature set saved; sub-percent of block signature collection.

**Best measured result.** -16.7k instructions/block (-0.195% collect_sigs) (pr:silver#172)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/core/chain_spec.rs:591`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/core/chain_spec.rs#L591) get_domain -&gt; compute_domain
- [`consensus/types/src/core/chain_spec.rs:724-738`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/core/chain_spec.rs#L724-L738) compute_domain calls compute_fork_data_root (tree_hash_root) on every call
- signature_sets.rs:313,346 get_domain per attestation set

**Sources.** [silver#172](https://github.com/gattaca-com/silver/pull/172)

</details>


<a id="bls-068"></a>
<details>
<summary><b>bls-068</b> Prepopulate pubkey cache in background at startup — <i>implemented · low · S · startup, sync, cpu</i></summary>

**Idea.** At startup, decompress all validator pubkeys from the finalized state into the pubkey cache in a background task, so initial sync does not pay decompression cost block by block.

**Impact.** Already done: the cache is fully populated before sync starts, so sync never pays per-block decompression for existing validators.

**Best measured result.** sync runs at max speed from the start (total time unchanged) (pr:prysm#11482)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:54-79`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L54-L79) load_from_store reads all keys from the DB in uncompressed form at startup
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:237-241`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L237-L241) as_pubkey uses deserialize_uncompressed (blst on-curve deserialize, no decompression and no subgroup check: [`crypto/bls/src/impls/blst.rs:141-151`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L141-L151))
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:144-157`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L144-L157) first import from a state decompresses in parallel with rayon
- [`beacon_node/beacon_chain/src/builder.rs:855-860`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L855-L860) cache built or loaded before the chain starts

**Skeptic check.** Confirmed. Lighthouse does better than the idea: it persists the uncompressed keys and loads them at startup synchronously, not in a background task. Initial sync reaches full speed at once, which is the effect the idea wants.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#11482](https://github.com/OffchainLabs/prysm/pull/11482)

</details>


<a id="bls-069"></a>
<details>
<summary><b>bls-069</b> API-submitted signatures bypass gossip verification queue — <i>implemented · medium · S · latency, cpu</i></summary>

**Idea.** Verify signatures from HTTP API submissions immediately or at the front of the BLS job queue, and keep separate queues per gossip service, so API jobs are not delayed behind large gossip batches under load.

**Impact.** Already done: API submissions skip the gossip batches and are scheduled ahead of them.

**Best measured result.** under overload verifying API sets took &gt;1s before (pr:lodestar#5754)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/publish_attestations.rs:77`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_attestations.rs#L77),142 API attestations are verified one by one with verify_unaggregated_attestation_for_gossip in a Priority::P0 blocking task
- [`beacon_node/http_api/src/validator/mod.rs:1295`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L1295) API aggregates are verified individually with verify_aggregated_attestation_for_gossip
- [`beacon_node/http_api/src/sync_committees.rs:181`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/sync_committees.rs#L181),311,359 sync messages and contributions are verified directly, outside the gossip batches
- [`beacon_node/beacon_processor/src/lib.rs:956-963`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L956-L963) api_request_p0_queue is popped before the gossip aggregate and attestation batch queues
- [`beacon_node/beacon_processor/src/lib.rs:1437-1440`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1437-L1440),1553-1554 separate P0/P1 API queues, separate from the per-gossip-topic queues

**Skeptic check.** Confirmed. API attestations, aggregates and sync messages are verified individually on a P0 queue that is scheduled ahead of the gossip attestation and aggregate batch queues, and each gossip topic has its own queue.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#5754](https://github.com/ChainSafe/lodestar/pull/5754), [caplin#12000](https://github.com/erigontech/erigon/pull/12000)

</details>


<a id="bls-070"></a>
<details>
<summary><b>bls-070</b> Cache pubkey deserialization keyed by compressed bytes — <i>implemented · low · S · cpu, sync</i></summary>

**Idea.** Cache the result of deserializing a BLS public key (decompression and subgroup check) keyed by its 48-byte compressed form. Validator keys repeat, so the hit rate is high and repeated decompression is skipped.

**Impact.** Already done: each validator key is decompressed once and reused on every hot path.

**Best measured result.** up to 25% of init-sync wall time; 1 to 2 blocks/s gain (pr:prysm#3583)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:24-29`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L24-L29) decompressed pubkeys kept by index, plus a PublicKeyBytes -&gt; index map
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:184-187`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L184-L187) get_pubkey_from_pubkey_bytes looks up by the 48-byte compressed form
- [`beacon_node/beacon_chain/src/block_verification.rs:717`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L717),1056,1205,1277,2215-2218 block signature sets use the cache
- [`consensus/state_processing/src/per_block_processing.rs:149-153`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing.rs#L149-L153) the decompress closure runs only under VerifyBulk; normal import uses pre-verified signatures from the cache

**Skeptic check.** Confirmed the cache serves lookups by index and by compressed bytes on block, gossip and sync paths. Decompression still happens only on cold paths: the sync aggregate fallback (altair/sync_committee.rs:25, its comment says this is unlikely in practice), get_pubkey_from_state, and deposits. Those keys are mostly not cached validator keys anyway.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#3583](https://github.com/OffchainLabs/prysm/pull/3583)

</details>


<a id="bls-071"></a>
<details>
<summary><b>bls-071</b> Random linear combination batch verification — <i>implemented · high · S · cpu</i></summary>

**Idea.** Verify many (pubkey, message, signature) sets together with random scalar coefficients in one multi-pairing and one final exponentiation, instead of one full pairing check per signature.

**Impact.** Already used on block import, chain-segment sync and gossip attestation/aggregate batches.

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/impls/blst.rs:47-66`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L47-L66) random nonzero 64-bit scalar per set
- [`crypto/bls/src/impls/blst.rs:113-115`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L113-L115) blst verify_multiple_aggregate_signatures: one multi-pairing and one final exponentiation
- [`beacon_node/beacon_chain/src/block_verification.rs:1212`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1212),1285 block import verifies all block signatures as one batch
- [`beacon_node/beacon_chain/src/attestation_verification/batch.rs:109`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification/batch.rs#L109) gossip aggregate and attestation batches

**Skeptic check.** Confirmed: RLC batch verification is real and runs on the hot paths. Gossip sync committee messages (sync_committee_verification.rs:709) and column header signatures are still verified one at a time, but cross-message gossip batching is a separate idea.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#6479](https://github.com/OffchainLabs/prysm/pull/6479)

</details>


<a id="bls-072"></a>
<details>
<summary><b>bls-072</b> Shared read lock for pubkey cache lookups — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Take only a shared read lock on pubkey cache gets, so concurrent signature verification workers do not serialize on lookups.

**Impact.** Already done: lookups take a shared read lock and only new-validator imports take the write lock.

**Best measured result.** lock contention disappears from mainnet pprof (pr:prysm#12646)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:125`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L125),507 parking_lot RwLock&lt;ValidatorPubkeyCache&gt;
- [`beacon_node/beacon_chain/src/block_verification.rs:2215-2218`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L2215-L2218) get_validator_pubkey_cache takes .read()
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4499`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4499) write lock only to import new pubkeys at block import
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:128-132`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L128-L132) DB writes are staged and not done under the write lock

**Skeptic check.** Confirmed that every lookup takes the read lock and that the write lock is held only briefly for new deposits. The earlier evidence is right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#12646](https://github.com/OffchainLabs/prysm/pull/12646)

</details>


<a id="bls-073"></a>
<details>
<summary><b>bls-073</b> Bisect failed signature batches recursively — <i>not · medium · S · cpu</i></summary>

**Idea.** When a batch verification fails, split the batch into halves and re-verify each recursively, so one bad signature costs a logarithmic number of batch checks instead of verifying every signature individually.

**Gap in Lighthouse.** On batch failure in batch.rs (aggregated and unaggregated) and sync_committee_verification.rs, recursively split sets in halves with verify_signature_sets on sub-slices and map results back per item.

**Impact.** Only under invalid-signature spam: N individual verifies become about k*log N batch checks. No gain on honest traffic.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification/batch.rs:109-126`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification/batch.rs#L109-L126) batch failure leaves check_signatures=Yes, each item re-verified individually
- [`beacon_node/beacon_chain/src/sync_committee_verification.rs:670`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/sync_committee_verification.rs#L670) single batch bool, no split
- [`crypto/bls/src/impls/blst.rs:36`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L36) verify_signature_sets returns bool only; no bisect/split helper in [`crypto/bls`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls) or beacon_chain

**Second check.** Grepped every verify_signature_sets caller (attestation batch, sync committee, block verifier, deposits) and searched for bisect/split/halve; all fall back to per-item verification or fail the whole batch.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [teku#4124](https://github.com/Consensys-Incorporated/teku/pull/4124)

</details>


<a id="bls-074"></a>
<details>
<summary><b>bls-074</b> Relaxed atomics for verify early-exit flag — <i>implemented · low · S · cpu</i></summary>

**Idea.** Use relaxed atomic loads for the early-exit error flag in BLS worker hot loops, since the flag carries no data dependency, avoiding acquire fence costs.

**Impact.** None; every early-exit flag access in the blst worker loops LH uses is already Relaxed.

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/registry/src/*/blst-0.3.17/src/lib.rs:1352 while valid.load(Ordering::Relaxed)
- ~/.cargo/registry/src/*/blst-0.3.17/src/lib.rs:1353 counter.fetch_add(1, Ordering::Relaxed)
- ~/.cargo/registry/src/*/blst-0.3.17/src/lib.rs:1369 valid.store(false, Ordering::Relaxed)
- ~/.cargo/registry/src/*/blst-0.3.17/src/lib.rs:1229-1271 same pattern in aggregate_verify
- [`crypto/bls/src/impls/blst.rs:113`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L113) LH batch path calls verify_multiple_aggregate_signatures (the loop above)

**Skeptic check.** Verified that the blst multi-threaded verify loops reached from LH's verify_signature_sets use Relaxed for the valid flag and counter. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@4b0a1cc1b](https://github.com/ChainSafe/lodestar/commit/4b0a1cc1b204)

</details>


<a id="bls-075"></a>
<details>
<summary><b>bls-075</b> Fewer branches in Jacobian point addition — <i>n/a · low · cpu</i></summary>

**Idea.** In the Jacobian point addition used in addition chains, move the z3==0 check into the u1==u2 branch so the dominant path runs one fewer branch.

**Gap in Lighthouse.** Lighthouse uses blst C code, not Java Jacobian addition.

**Evidence (Lighthouse @ 928b61e719).**

- blst C library implements point addition

**Sources.** [teku#2174](https://github.com/Consensys-Incorporated/teku/pull/2174)

</details>


<a id="bls-076"></a>
<details>
<summary><b>bls-076</b> Do not hash to G2 twice — <i>implemented · medium · S · cpu</i></summary>

**Idea.** On the signature verify path, do not pre-hash the message to G2 when the pairing aggregate call already hashes it internally. Hash-to-curve is the most expensive step and was done twice.

**Impact.** None; hash-to-G2 runs once per message inside blst.

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/impls/blst.rs:71`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L71) msgs_refs.push(set.message.as_slice()) raw 32-byte signing root
- [`crypto/bls/src/impls/blst.rs:113`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L113) verify_multiple_aggregate_signatures(&amp;msgs_refs, DST, ...) hashes inside the pairing once
- [`crypto/bls/src/impls/blst.rs:257`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L257) fast_aggregate_verify(true, msg.as_slice(), DST, ...) single-set path also passes raw msg

**Skeptic check.** Both the batch and single-set verify paths pass raw messages to blst, and LH never pre-hashes to G2 itself. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#3453](https://github.com/Consensys-Incorporated/teku/pull/3453)

</details>


<a id="bls-077"></a>
<details>
<summary><b>bls-077</b> No mutex around BLS thread pool task spawn — <i>n/a · low · cpu, latency</i></summary>

**Idea.** Remove the mutex around task spawn in the BLS thread pool so callers do not contend on a lock when submitting verification work.

**Impact.** None; Lighthouse has no JS thread pool.

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls): native blst backend, no JS worker pool

**Sources.** [lodestar@5e2f1bbc6](https://github.com/ChainSafe/lodestar/commit/5e2f1bbc6f4d)

</details>


<a id="bls-078"></a>
<details>
<summary><b>bls-078</b> Benchmark BLS binding changes end to end — <i>n/a · low · cpu, latency</i></summary>

**Idea.** Benchmark BLS binding or backend rewrites end to end on a node before shipping and revert when they regress; a binding rewrite regressed node performance in a release candidate.

**Impact.** None; a benchmarking practice, not a code change.

**Evidence (Lighthouse @ 928b61e719).**

- process lesson, no code to compare

**Sources.** [lodestar#6853](https://github.com/ChainSafe/lodestar/pull/6853)

</details>


<a id="bls-079"></a>
<details>
<summary><b>bls-079</b> Put aggregate signature in the shared Miller loop — <i>not · low · M · cpu</i></summary>

**Idea.** In batch signature verification, pair the aggregate signature with -G1 inside the same multi-Miller loop as the message pairs instead of running a separate Miller loop for the signature.

**Gap in Lighthouse.** blst's PAIRING_FinalVerify (aggregate.c:460-497) runs a separate one-pair Miller loop for the aggregated signature against G1 after the message-pair Miller loops. Lighthouse's verify_signature_sets (crypto/bls/src/impls/blst.rs:36-117) could put the pair (sum rand_i*sig_i, -G1) into one worker's Pairing with blst_pairing_raw_aggregate, so it shares that worker's multi-Miller loop squarings, and then call finalverify with no signature accumulator. The final exponentiation is already shared.

**Impact.** About 30-50 us per verify_signature_sets call (silver measured -49 us, -7%, on a 2-group batch). The saving is near zero when the per-worker pair count is a multiple of 8. It matters most for small batches such as single-attestation API checks and small gossip batches.

**Best measured result.** block envelope batch 694 -&gt; 645 us (-7.1%) (pr:silver#348)

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/impls/blst.rs:113-116`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L113-L116) verify_multiple_aggregate_signatures(..., sigs ...)
- ~/.cargo/registry/src/*/blst-0.3.17/src/lib.rs:1347-1385 workers call mul_n_aggregate, which adds rand*sig into ctx-&gt;AggrSign; then merge and finalverify(None)
- ~/.cargo/registry/src/*/blst-0.3.17/blst/src/aggregate.c:460-497 PAIRING_FinalVerify: when AGGR_SIGN_SET it runs a separate miller_loop_n(GT, AggrSign.e2, BLS12_381_G1, 1), then conjugate, mul_fp12 with ctx-&gt;GT and one final_exp

**Skeptic check.** The earlier evidence was wrong. blst shares the final exponentiation but explicitly runs a separate Miller loop for the aggregated signature (aggregate.c:475-481), which is exactly what silver#348 removes. The gain is small, and it is largest on small batches.

**Verdict history.** implemented (checked) → not (skeptic)

**Sources.** [silver#348](https://github.com/gattaca-com/silver/pull/348)

</details>


<a id="bls-080"></a>
<details>
<summary><b>bls-080</b> Shared hash-to-G2 cache keyed by signing root — <i>not · medium · M · cpu</i></summary>

**Idea.** Keep one cache of hash-to-G2 results keyed by signing root, shared between gossip attestation verification and block signature verification (two-generation eviction), so each root is hashed to the curve once (~98us each).

**Gap in Lighthouse.** Add a signing-root -&gt; G2 point cache shared by gossip and block verification; requires lower-level blst pairing calls since verify_multiple_aggregate_signatures takes messages, not points.

**Impact.** ~98us per repeated signing root; tens to hundreds of repeats per block. Small total CPU.

**Best measured result.** saves ~98 us hash-to-curve per repeated root (pr:silver#296)

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/impls/blst.rs:36-110`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L36-L110) passes raw message byte slices (msgs_refs) to blst, which hashes to G2 internally per call
- no hash_to/G2 cache found in crypto/ or [`beacon_node/beacon_chain/src`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src)

**Second check.** Searched crypto/bls and beacon_chain for hash_to_curve/G2/message caches; the blst wrapper only takes byte messages, so no cache is possible at the current layer.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [silver#296](https://github.com/gattaca-com/silver/pull/296)

</details>


<a id="bls-081"></a>
<details>
<summary><b>bls-081</b> Load only one BLS implementation per process — <i>n/a · low · startup, memory</i></summary>

**Idea.** Avoid loading a second BLS implementation (for example a wasm build for light-client code) in the node process; use the native backend everywhere on server builds.

**Impact.** None; one native BLS backend per process already.

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/Cargo.toml:10`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/Cargo.toml#L10) fake_crypto is the only alternative, a test feature; blst is the single backend

**Sources.** [lodestar#9646](https://github.com/ChainSafe/lodestar/pull/9646)

</details>


<a id="bls-082"></a>
<details>
<summary><b>bls-082</b> Single merged block-level signature proof — <i>n/a · low · bandwidth, cpu</i></summary>

**Idea.** Replace one aggregated proof per attestation plus a proposer signature with a single merged block-level proof, so blocks are smaller and import verifies one proof; bound any later proof splitting.

**Impact.** Lean-consensus protocol design, not part of the mainnet spec Lighthouse implements.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types): attestations carry individual aggregate BLS signatures per spec

**Sources.** [ethlambda#378](https://github.com/lambdaclass/ethlambda/pull/378)

</details>


<a id="bls-083"></a>
<details>
<summary><b>bls-083</b> Single pass over keys and signatures in batch prep — <i>partial · low · S · cpu</i></summary>

**Idea.** Validate and convert public keys or semi-aggregate signatures in the same loop that aggregates them, instead of iterating the list twice, and avoid boxed integers in that loop.

**Gap in Lighthouse.** Signature checks and key aggregation share one loop and there is no boxing, but the pubkey refs are collected into a Vec before aggregate, and the sets are collected into a Vec first. Could aggregate straight from the iterator.

**Impact.** A couple of percent on the batch prep step at most.

**Best measured result.** ~2-3% ops/s, e.g. 97.7 -&gt; 100.1 at 16 sigs (pr:teku#5459)

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/impls/blst.rs:72-78`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L72-L78) signature subgroup check and conversion in the same loop as key aggregation
- [`crypto/bls/src/impls/blst.rs:94-103`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L94-L103) pubkeys are collected to a Vec then aggregated
- [`crypto/bls/src/impls/blst.rs:39`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L39) sets collected first
- blst.rs:59-66 random scalar via unsafe, no boxing

**Sources.** [teku#5459](https://github.com/Consensys-Incorporated/teku/pull/5459), [teku#5468](https://github.com/Consensys-Incorporated/teku/pull/5468)

</details>


<a id="bls-084"></a>
<details>
<summary><b>bls-084</b> Flag to skip BLS for profiling — <i>partial · low · S · cpu</i></summary>

**Idea.** Provide a runtime flag that disables signature verification (not for production) so profiles expose bottlenecks other than BLS.

**Gap in Lighthouse.** No runtime beacon-node flag; only a build feature (fake_crypto) and the lcli/test strategy exist. Would need a hidden CLI flag wired into the gossip and block signature verification entry points.

**Impact.** Profiling convenience only; no change to mainnet node cost.

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/Cargo.toml:10`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/Cargo.toml#L10) fake_crypto compile-time feature
- [`consensus/state_processing/src/per_block_processing.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing.rs) BlockSignatureStrategy::NoVerification (used by lcli/tests)
- [`beacon_node/src/cli.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs) and [`lighthouse/src/main.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/src/main.rs): no runtime signature-skip flag found

**Sources.** [prysm#3618](https://github.com/OffchainLabs/prysm/pull/3618)

</details>


<a id="bls-085"></a>
<details>
<summary><b>bls-085</b> Skip signature checks for trusted or pre-verified blocks — <i>implemented · medium · S · cpu</i></summary>

**Idea.** Pass a verify-signatures flag through block processing and skip BLS checks in the state transition for blocks already batch-verified or known valid (trusted finalized history during sync), for every fork. This removes the dominant BLS cost per block and avoids polluting the pubkey cache.

**Impact.** Already realized: import runs per_block_processing with NoVerification after one batched signature check, and stored/finalized blocks are replayed and reconstructed without BLS.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing.rs:71-77`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing.rs#L71-L77),147-165
- [`beacon_node/beacon_chain/src/block_verification.rs:1259-1287`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1259-L1287)
- [`beacon_node/beacon_chain/src/block_verification.rs:1710`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1710)
- [`consensus/state_processing/src/block_replayer.rs:114`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/block_replayer.rs#L114)
- [`beacon_node/store/src/reconstruct.rs:165`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/reconstruct.rs#L165)

**Second check.** Source PRs (nimbus#4085, lodestar flag commits) are exactly 'skip state-transition BLS for blocks already batch-verified / trusted'; Lighthouse does this via BlockSignatureStrategy::NoVerification after signature_verify_chain_segment and in BlockReplayer/reconstruction, which the earlier review missed.

**Skeptic check.** Confirmed BlockSignatureStrategy threads through per_block_processing, and every import path (gossip, RPC, chain segment) batch-verifies once and then processes with NoVerification at block_verification.rs:1710. The earlier evidence is correct. Forward sync of finalized history still verifies signatures, but that is a trust-model choice.

**Verdict history.** not (checked) → implemented (refuted) → implemented (skeptic)

**Sources.** [lodestar@476e3a5b5](https://github.com/ChainSafe/lodestar/commit/476e3a5b50f7), [lodestar@6b65c80a2](https://github.com/ChainSafe/lodestar/commit/6b65c80a294f), [nimbus#4085](https://github.com/status-im/nimbus-eth2/pull/4085)

</details>


<a id="bls-086"></a>
<details>
<summary><b>bls-086</b> Verify sparse time-critical gossip objects unbatched — <i>implemented · low · S · latency</i></summary>

**Idea.** Verify gossip objects that arrive few per slot and are time-critical (such as inclusion lists) immediately, not through a batching pool that waits up to 100ms to fill a batch.

**Impact.** None for batching delay. Inclusion lists are scheduled after the attestation/aggregate queues, which is a priority question and not the idea here.

**Best measured result.** IL validation 106ms to 9ms avg; median lag 111ms to 14ms (pr:lodestar#10282)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:4366-4384`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L4366-L4384) process_gossip_inclusion_list verifies and imports each list individually
- [`beacon_node/beacon_processor/src/lib.rs:1075`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1075) gossip_inclusion_list_queue popped as a single item, no batch
- [`beacon_node/beacon_processor/src/lib.rs:1017-1027`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1017-L1027) attestation batches only take items already queued, no timer wait

**Skeptic check.** Confirmed that ILs bypass any batching and that LH batching never waits on a timer. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#10282](https://github.com/ChainSafe/lodestar/pull/10282)

</details>


<a id="bls-087"></a>
<details>
<summary><b>bls-087</b> Do not recheck proposer signature verified at gossip — <i>implemented · medium · S · cpu</i></summary>

**Idea.** Build block signature sets without the proposer signature when that signature was already verified during gossip validation, so it is not verified a second time at import.

**Impact.** Saves one proposer signature verification per gossip block at import.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1256-1287`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1256-L1287)
- [`beacon_node/beacon_chain/src/block_verification.rs:1159`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1159)
- [`consensus/state_processing/src/per_block_processing/block_signature_verifier.rs:161-168`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/block_signature_verifier.rs#L161-L168)

**Skeptic check.** Gossip blocks reach SignatureVerifiedBlock through from_gossip_verified_block_check_slashable -&gt; from_gossip_verified_block, which calls include_all_signatures_except_proposal. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@6f562dd58](https://github.com/ChainSafe/lodestar/commit/6f562dd58c35)

</details>


<a id="bls-088"></a>
<details>
<summary><b>bls-088</b> No pubkey aggregation for single-signer attestations — <i>not · low · S · cpu</i></summary>

**Idea.** For unaggregated gossip attestations, build the signature set from the single pubkey directly instead of running a pubkey aggregation step over a one-element list.

**Gap in Lighthouse.** In verify_signature_sets, if signing_keys.len()==1 use the key directly and skip AggregatePublicKey::aggregate and the Vec of refs. Also avoid the vec![] in single_pubkey.

**Impact.** Saves a point conversion and two small allocations per unaggregated attestation; well under 1% CPU.

**Best measured result.** saves 0.8% CPU time (pr:lodestar#5406)

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/impls/blst.rs:94-103`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L94-L103) every set goes through AggregatePublicKey::aggregate even with one key
- [`crypto/bls/src/generic_signature_set.rs:82`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/generic_signature_set.rs#L82) single_pubkey builds a vec of one key
- attestation_verification/batch.rs:62 sets for unaggregated attestations

**Sources.** [lodestar#5406](https://github.com/ChainSafe/lodestar/pull/5406)

</details>


<a id="bls-089"></a>
<details>
<summary><b>bls-089</b> Yield between very large BLS batches — <i>n/a · low · cpu, latency</i></summary>

**Idea.** Insert a short pause between very large signature verification batches so other work on the same threads is not starved.

**Impact.** Batches are bounded and scheduled as separate work items, so no giant batch starves other work.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:110-111`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L110-L111) gossip batch sizes capped at 64
- [`consensus/state_processing/src/per_block_processing/verify_deposit.rs:121-122`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/verify_deposit.rs#L121-L122) par_chunks over rayon with chunk size 8

**Sources.** [teku#7596](https://github.com/Consensys-Incorporated/teku/pull/7596)

</details>


<a id="bls-090"></a>
<details>
<summary><b>bls-090</b> Route batchable vs latency-critical BLS jobs separately — <i>implemented · medium · S · latency, cpu</i></summary>

**Idea.** Send batchable signature jobs (gossip attestations) to the batching worker threads and verify non-batchable latency-critical jobs (blocks) directly, to keep BLS job wait time under a target (100ms).

**Impact.** Attestations and aggregates are batched on workers; blocks get priority and are verified directly in their own work item.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:1031-1060`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1031-L1060)
- [`beacon_node/beacon_processor/src/lib.rs:975-1000`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L975-L1000)
- [`beacon_node/beacon_processor/src/lib.rs:373-409`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L373-L409)
- [`beacon_node/beacon_chain/src/block_verification.rs:1259-1287`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1259-L1287)

**Skeptic check.** Confirmed the beacon processor forms GossipAttestationBatch and GossipAggregateBatch only for batchable work, and drains block queues before them. Sync committee messages are not batched, but that is a separate idea, not this routing mechanism.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#3793](https://github.com/ChainSafe/lodestar/pull/3793)

</details>


<a id="bls-091"></a>
<details>
<summary><b>bls-091</b> Store pubkeys uncompressed on disk to skip decompression — <i>implemented · medium · S · startup, cpu</i></summary>

**Idea.** Persist the validator pubkey cache (and key files) in decompressed/uncompressed form, so startup loads keys without decompressing every validator pubkey.

**Impact.** Startup loads the persisted pubkey cache without decompressing each key.

**Best measured result.** startup time improved dramatically (no number) (pr:lighthouse#5897)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:233`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L233)
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:238`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L238)
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:144-157`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L144-L157)

**Skeptic check.** The persisted cache stores serialize_uncompressed bytes and loads them with deserialize_uncompressed. This is the Lighthouse PR itself, so the earlier evidence is correct. Validator-client keystores are encrypted, so the 'key files' part does not apply.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#5897](https://github.com/sigp/lighthouse/pull/5897), [lighthouse@1b252c3f8](https://github.com/sigp/lighthouse/commit/1b252c3f82db), [silver#431](https://github.com/gattaca-com/silver/pull/431)

</details>


<a id="bls-092"></a>
<details>
<summary><b>bls-092</b> Fixed-size sub-batches for bulk signature verification — <i>implemented · low · S · cpu</i></summary>

**Idea.** When batch-verifying many signatures at once (such as thousands of builder deposits), split them into fixed-size sub-batches (256) so an invalid signature forces per-signature fallback only within its sub-batch.

**Impact.** Already done. On a cache miss, is_valid_deposit_signature_cached (builder_deposits_cache.rs:160-190) verifies per signature, but the cache is seeded from the head state, so a miss is uncommon.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/verify_deposit.rs:14`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/verify_deposit.rs#L14) DEPOSIT_SIGNATURE_BATCH_SIZE = 8
- [`consensus/state_processing/src/per_block_processing/verify_deposit.rs:104-148`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/verify_deposit.rs#L104-L148) is_valid_deposit_signature_batch: par_chunks sub-batches, per-entry fallback only inside the failing chunk
- [`consensus/state_processing/src/builder_deposits_cache.rs:101-135`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/builder_deposits_cache.rs#L101-L135) OnboardBuildersCache pre-verifies pending_deposits in batches ahead of the Gloas fork
- [`consensus/state_processing/src/upgrade/gloas.rs:235`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/upgrade/gloas.rs#L235) onboard_builders_from_pending_deposits uses the cache

**Skeptic check.** Verified the sub-batching with chunk-local fallback, and that it runs on the bulk Gloas onboarding path through the pre-verification cache. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#10820](https://github.com/Consensys-Incorporated/teku/pull/10820)

</details>


<a id="bls-093"></a>
<details>
<summary><b>bls-093</b> Subtract non-participants from full sync committee aggregate — <i>not · medium · S · cpu</i></summary>

**Idea.** For sync-aggregate verification, start from the precomputed aggregate pubkey of the whole sync committee and subtract the keys of non-participants, since participation is over 95%, instead of summing all participants.

**Gap in Lighthouse.** When participation &gt; 1/2, start from the decompressed (cached) committee aggregate pubkey and subtract non-participant keys; needs point negate/sub in the bls crate and signing-key representation of a precomputed aggregate.

**Impact.** ~512 additions become ~25 per block at 95% participation; tens of microseconds to ~1ms per block. Source PR targeted light-client update verification, which Lighthouse does not do in-node.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/signature_sets.rs:814-829`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/signature_sets.rs#L814-L829) collects participant pubkeys and sums them via SignatureSet::multiple_pubkeys
- [`consensus/types/src/state/beacon_state.rs:1843-1847`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1843-L1847) committee aggregate_pubkey only computed for the SyncCommittee container
- [`crypto/bls/src`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src): no subtract/negate on AggregatePublicKey

**Second check.** Checked signature_sets.rs, all aggregate_pubkey users, and crypto/bls for subtract/neg APIs; nothing uses the committee aggregate for verification.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [nimbus#5268](https://github.com/status-im/nimbus-eth2/pull/5268)

</details>


<a id="bls-094"></a>
<details>
<summary><b>bls-094</b> Configurable signature batching parameters — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Expose batch size, queue capacity and thread count of the batch signature verification service as configuration so they can be tuned empirically per machine.

**Impact.** The knobs exist. The blst internal thread pool (da_pool) size is not exposed, but that is minor.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/src/cli.rs:1618`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L1618) --beacon-processor-max-workers
- [`beacon_node/src/cli.rs:1630`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L1630) --beacon-processor-work-queue-len
- [`beacon_node/src/cli.rs:1654`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L1654),1666 --beacon-processor-attestation-batch-size / --beacon-processor-aggregate-batch-size
- [`beacon_node/src/config.rs:877-894`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/config.rs#L877-L894) wired into BeaconProcessorConfig

**Skeptic check.** Confirmed that batch size, queue length and worker count are CLI-configurable and wired into config. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#4738](https://github.com/Consensys-Incorporated/teku/pull/4738)

</details>


<a id="bls-095"></a>
<details>
<summary><b>bls-095</b> Key deposit pubkey cache by decompressed key — <i>n/a · low · cpu, memory</i></summary>

**Idea.** When verifying many deposits, operate on the decompressed pubkey rather than the compressed bytes, so the pubkey decompression cache does not grow with every deposit key.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/verify_deposit.rs:108`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/verify_deposit.rs#L108) deposits are decompressed per call, no decompression cache
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:805`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L805) pubkey_cache is a compressed-key to index map, not a decompression cache

**Sources.** [nimbus#4082](https://github.com/status-im/nimbus-eth2/pull/4082)

</details>


<a id="bls-096"></a>
<details>
<summary><b>bls-096</b> Simpler y-sign flag in point decompression — <i>n/a · low · cpu</i></summary>

**Idea.** In G1/G2 point decompression and compression, compute the y-coordinate sign flag with a simple comparison instead of a heavier field computation.

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/impls/blst.rs:257`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L257) all point (de)compression done in C blst

**Sources.** [teku#2142](https://github.com/Consensys-Incorporated/teku/pull/2142)

</details>


<a id="bls-097"></a>
<details>
<summary><b>bls-097</b> Aggregate attestation pubkeys inside the BLS library — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Verify an indexed attestation with one library aggregate-verify call over the pubkey list, letting the BLS library aggregate the keys natively, instead of adding public keys one by one in application code.

**Impact.** None; pubkeys are aggregated by blst natively on both the single and batch paths.

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/impls/blst.rs:97`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L97) AggregatePublicKey::aggregate(&amp;signing_keys, false) one native call per set in batch verify
- [`crypto/bls/src/impls/blst.rs:247-258`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L247-L258) fast_aggregate_verify passes the full pubkey slice to blst
- [`crypto/bls/src/generic_signature_set.rs:111-120`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/generic_signature_set.rs#L111-L120) SignatureSet::verify uses fast_aggregate_verify

**Skeptic check.** Both the indexed-attestation single-set path and the batch path hand the whole key list to blst in one call. No add_assign loop in application code. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@f780b7a43](https://github.com/ChainSafe/lodestar/commit/f780b7a43117), [nimbus@bfd4df912](https://github.com/status-im/nimbus-eth2/commit/bfd4df912e57)

</details>


<a id="bls-098"></a>
<details>
<summary><b>bls-098</b> Size pairing buffers from real library context size — <i>implemented · low · S · memory</i></summary>

**Idea.** Allocate each per-worker BLS pairing context buffer using the library's actual context size rather than a pointer-width-derived estimate that over-reserves on some targets. Check the pairing buffer size Lighthouse/blst bindings reserve.

**Impact.** The pairing buffer is sized from the C library's real sizeof, so it does not over-reserve.

**Best measured result.** None (commit:lodestar@dc64a27e5469)

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.lock:1801-1802 blst 0.3.17
- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/blst-0.3.17/src/lib.rs:288-289 Pairing::new allocates blst_pairing_sizeof()/8 u64 words

**Skeptic check.** Checked the locked blst 0.3.17 (the earlier note cited 0.3.16, but the code is the same). The lodestar bug was a pointer-width estimate and does not apply here.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@dc64a27e5](https://github.com/ChainSafe/lodestar/commit/dc64a27e5469)

</details>


<a id="bls-099"></a>
<details>
<summary><b>bls-099</b> Verify tiny signature batches inline on caller — <i>not · low · S · cpu, latency</i></summary>

**Idea.** Verify batches of one or two signature sets (or when only one worker exists) directly on the calling thread instead of dispatching to the BLS worker pool. This avoids queue and thread-handoff overhead that dominates for small jobs.

**Gap in Lighthouse.** In verify_signature_sets, special-case sets.len()==1 (and possibly 2) to call SignatureSet::verify / fast_aggregate_verify directly, skipping random scalars and the blst pool hand-off. Lighthouse has no own BLS worker pool; the handoff is inside blst (default threads feature).

**Impact.** Saves a thread-pool hop and 64-bit scalar muls per single-set verify; microseconds against a ~1ms pairing, so marginal.

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/impls/blst.rs:36`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L36) verify_signature_sets has no small-batch path; always draws rands, aggregates pks, calls verify_multiple_aggregate_signatures
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1484`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1484) two-set aggregate verify goes through the same path
- blst-0.3.17/src/lib.rs:1337 dispatches work to blst's da_pool even when n_workers=1 and blocks on a channel

**Sources.** [lodestar#553](https://github.com/ChainSafe/lodestar/pull/553)

</details>


<a id="bls-100"></a>
<details>
<summary><b>bls-100</b> Drop release loop over semi-aggregates in batch verify — <i>n/a · low · S · cpu, memory</i></summary>

**Idea.** In batch BLS verification, skip the explicit per-item release/cleanup pass over semi-aggregates when the library holds no external memory. This saves one pass and one list allocation per batch.

**Impact.** Teku/JNI specific cleanup pass; nothing to remove in Rust.

**Best measured result.** None (pr:teku#5456)

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/impls/blst.rs:36-117`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L36-L117) blst Rust bindings own and free their memory; no per-item release pass exists

**Sources.** [teku#5456](https://github.com/Consensys-Incorporated/teku/pull/5456)

</details>


<a id="bls-101"></a>
<details>
<summary><b>bls-101</b> Check signature subgroup once at deserialisation — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Validate signature points (subgroup and flags) once when deserialising and do not repeat the check in the verify or batch-verify path (or defer to the library, not both). Each signature then incurs the G2 subgroup check once rather than twice.

**Impact.** Each signature gets exactly one G2 subgroup check on every verify path.

**Best measured result.** None (pr:teku#4372)

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/impls/blst.rs:72-78`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L72-L78) batch path subgroup-checks each signature once
- [`crypto/bls/src/impls/blst.rs:110-112`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L110-L112) verify_multiple_aggregate_signatures with sigs_groupcheck=false
- [`crypto/bls/src/impls/blst.rs:194-196`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L194-L196) deserialize via from_bytes (no group check)
- [`crypto/bls/src/impls/blst.rs:205`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L205) single verify checks the group inside blst
- [`crypto/bls/src/impls/blst.rs:257-281`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L257-L281) fast_aggregate_verify/aggregate_verify check once inside blst; add_signature uses false

**Skeptic check.** Verified that deserialization does no group check and that single, aggregate and batch verification each check once. Earlier verdict right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#4372](https://github.com/Consensys-Incorporated/teku/pull/4372), [teku#417](https://github.com/Consensys-Incorporated/teku/pull/417)

</details>


<a id="bls-102"></a>
<details>
<summary><b>bls-102</b> Skip Pippenger for tiny multi-scalar multiplications — <i>n/a · low · S · cpu, latency</i></summary>

**Idea.** For multi-scalar multiplication over fewer than about 32 points, use per-point scalar multiplication plus summation instead of tiled Pippenger. This avoids Pippenger setup cost on small aggregate batches.

**Impact.** Lighthouse does not run a Pippenger MSM for BLS; KZG MSMs live inside c-kzg (not inspected).

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/impls/blst.rs:36-117`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L36-L117) batch verify uses blst mul_n_aggregate per set with 64-bit rands; no MSM/Pippenger call in Lighthouse BLS code
- [`crypto/bls/src/impls/blst.rs:99`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L99) pubkey aggregation is point addition, not MSM

**Sources.** [lodestar#393](https://github.com/ChainSafe/lodestar/pull/393)

</details>


<a id="bls-103"></a>
<details>
<summary><b>bls-103</b> Wake only as many BLS workers as queued items — <i>n/a · low · S · cpu, latency</i></summary>

**Idea.** When enqueuing BLS jobs, signal only as many sleeping pool workers as there are new items (tracking the sleeper count under the queue lock) rather than broadcasting to all. This avoids thundering-herd wakeups and scheduler churn for small batches.

**Impact.** No broadcast wakeup to fix; per-job wakeup already.

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/impls/blst.rs:36`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L36) no Lighthouse-owned BLS worker queue
- blst-0.3.17/src/lib.rs:41-50,1337-1350 blst uses the threadpool crate (mpsc, one wake per job), not a broadcast condvar

**Sources.** [lodestar#383](https://github.com/ChainSafe/lodestar/pull/383)

</details>


