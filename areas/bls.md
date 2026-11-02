# bls

40 ideas: 11 not, 4 partial, 22 implemented, 3 n/a; 9 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

Ids missing from the sequence are ideas that have not been checked against Lighthouse yet.

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [bls-002](#bls-002) | Keep the BLS library on recent releases | implemented | low | S | cpu |
| [bls-006](#bls-006) | Size BLS thread pool from cgroup CPU quota | implemented | medium |  | cpu, latency |
| [bls-011](#bls-011) | Parallelize batch verification Miller loops across cores | implemented | medium |  | cpu, latency, sync |
| [bls-013](#bls-013) **★** | Multi-scalar multiplication for batch random scalars | not | medium | M | cpu, latency |
| [bls-019](#bls-019) | Batch-verify gossip BLS-to-execution changes | not | low | S | cpu |
| [bls-022](#bls-022) | Batch-verify deposit signatures within a block | not | low | M | cpu |
| [bls-025](#bls-025) **★** | Precompute committee pubkey sums and subtract non-attesters | not | high | M | cpu, latency |
| [bls-026](#bls-026) | Pass validator indices to the verifier, aggregate pubkeys there | n/a | low |  | cpu, latency |
| [bls-028](#bls-028) **★** | Run pairing product on SIMD IFMA lanes | not | medium | L | cpu, latency |
| [bls-029](#bls-029) **★** | Decompress signatures in batches | not | medium | L | cpu, latency |
| [bls-030](#bls-030) **★** | Batch-validate pubkeys during state load | partial | medium | L | startup, cpu |
| [bls-036](#bls-036) | Copy BLS points without serialize roundtrip | implemented | low |  | cpu |
| [bls-037](#bls-037) | Pass BLS points by reference, avoid copies | implemented | low |  | cpu, memory |
| [bls-041](#bls-041) | Cap batch size at the native verifier limit | n/a | medium |  | cpu |
| [bls-044](#bls-044) | Subgroup-check each pubkey once and reuse it | implemented | medium |  | cpu, memory |
| [bls-049](#bls-049) | Fast G2 cofactor clearing and subgroup check | implemented | low |  | cpu, sync |
| [bls-053](#bls-053) | Verify deposit signatures only when the outcome depends on it | implemented | medium |  | cpu, memory |
| [bls-054](#bls-054) | Fixed-size arrays for BLS serialization | implemented | low |  | cpu |
| [bls-057](#bls-057) **★** | Larger gossip signature batch size limit | partial | medium | S | cpu |
| [bls-058](#bls-058) | Lazy pubkey and signature decompression | implemented | medium |  | cpu, sync, startup |
| [bls-060](#bls-060) | Plain map instead of LRU for pubkey cache | implemented | low |  | memory |
| [bls-061](#bls-061) | Reuse buffers in batch verification, no per-call allocation | partial | low | S | cpu, memory |
| [bls-062](#bls-062) | Raise default BLS verification threads and queue size | n/a | medium |  | cpu, latency |
| [bls-064](#bls-064) | Verify block attestation signatures in parallel | implemented | medium | S | cpu, latency |
| [bls-065](#bls-065) | Preallocate signature-set vectors with known capacity | implemented | low |  | cpu, memory |
| [bls-067](#bls-067) | Precompute fork-data roots for domain derivation | not | low | S | cpu |
| [bls-068](#bls-068) | Prepopulate pubkey cache in background at startup | implemented | medium |  | startup, sync, cpu |
| [bls-069](#bls-069) | API-submitted signatures bypass gossip verification queue | implemented | medium |  | latency, cpu |
| [bls-070](#bls-070) | Cache pubkey deserialization keyed by compressed bytes | implemented | low |  | cpu, sync |
| [bls-072](#bls-072) | Shared read lock for pubkey cache lookups | implemented | low |  | cpu, latency |
| [bls-073](#bls-073) **★** | Bisect failed signature batches recursively | not | medium | S | cpu |
| [bls-079](#bls-079) | Put aggregate signature in the shared Miller loop | implemented | low |  | cpu |
| [bls-080](#bls-080) **★** | Shared hash-to-G2 cache keyed by signing root | not | medium | M | cpu |
| [bls-083](#bls-083) | Single pass over keys and signatures in batch prep | partial | low | S | cpu |
| [bls-085](#bls-085) | Skip signature checks for trusted or pre-verified blocks | implemented | medium | S | cpu |
| [bls-087](#bls-087) | Do not recheck proposer signature verified at gossip | implemented | medium | S | cpu |
| [bls-088](#bls-088) | No pubkey aggregation for single-signer attestations | not | low | S | cpu |
| [bls-090](#bls-090) | Route batchable vs latency-critical BLS jobs separately | implemented | medium | S | latency, cpu |
| [bls-091](#bls-091) | Store pubkeys uncompressed on disk to skip decompression | implemented | medium | S | startup, cpu |
| [bls-093](#bls-093) **★** | Subtract non-participants from full sync committee aggregate | not | medium | S | cpu |

★ actionable. Click an id for the full record.

## Ideas

<a id="bls-002"></a>
<details>
<summary><b>bls-002</b> Keep the BLS library on recent releases — <i>implemented · low · S · cpu</i></summary>

**Idea.** Track recent blst (or bindings) releases and the newer APIs they expose, so the client picks up upstream speedups in verification and batched multi-signature checks. Check the pinned BLS crate version against upstream.

**Impact.** Lighthouse is on blst 0.3.17, a recent release.

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.lock:1801 blst 0.3.17
- [`crypto/bls/Cargo.toml`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/Cargo.toml) blst dependency

**Sources.** [teku#6675](https://github.com/Consensys-Incorporated/teku/pull/6675), [lodestar@9e8a96ebf](https://github.com/ChainSafe/lodestar/commit/9e8a96ebf86a), [teku#8386](https://github.com/Consensys-Incorporated/teku/pull/8386), [lighthouse#2601](https://github.com/sigp/lighthouse/pull/2601)

</details>


<a id="bls-006"></a>
<details>
<summary><b>bls-006</b> Size BLS thread pool from cgroup CPU quota — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** Compute the BLS verification thread count from the cgroup CPU quota and affinity, not the host core count. This avoids oversubscription and CFS throttling in containers.

**Evidence (Lighthouse @ 928b61e719).**

- [`common/task_executor/src/rayon_pool_provider.rs:26`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/task_executor/src/rayon_pool_provider.rs#L26) uses num_cpus::get()
- blst-0.3.17/src/lib.rs:46 ThreadPool::default() uses num_cpus, which reads cgroup quota and affinity on Linux
- [`beacon_node/beacon_processor/src/lib.rs:130`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L130) max_workers = num_cpus::get()

**Sources.** [lodestar@3ae95226b](https://github.com/ChainSafe/lodestar/commit/3ae95226b31a)

</details>


<a id="bls-011"></a>
<details>
<summary><b>bls-011</b> Parallelize batch verification Miller loops across cores — <i>implemented · medium · cpu, latency, sync</i></summary>

**Idea.** Split a batch verification's multi-pairing across a thread pool (e.g. blst miller_loop_n, or per-thread partial Miller-loop accumulators merged before one final exponentiation) and enable it by default. Sync, block import and gossip batches then use all cores.

**Best measured result.** 10-20% faster sync; 8 threads about 1m29s vs 1 thread about 1m55s for 100 epochs (pr:nimbus#3493)

**Evidence (Lighthouse @ 928b61e719).**

- blst-0.3.17/src/lib.rs:1337-1347 verify_multiple_aggregate_signatures splits sets across da_pool workers (default feature, no-threads off)
- [`crypto/bls/src/impls/blst.rs:113`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L113) calls it for every batch

**Sources.** [nimbus#5300](https://github.com/status-im/nimbus-eth2/pull/5300), [nimbus#3493](https://github.com/status-im/nimbus-eth2/pull/3493), [lodestar@6da152424](https://github.com/ChainSafe/lodestar/commit/6da152424950), [lodestar@11f83eb98](https://github.com/ChainSafe/lodestar/commit/11f83eb98bcf), [lodestar@4399a853b](https://github.com/ChainSafe/lodestar/commit/4399a853be89), [lodestar@34ff8c15a](https://github.com/ChainSafe/lodestar/commit/34ff8c15ab31), [nimbus#2718](https://github.com/status-im/nimbus-eth2/pull/2718)

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

**Sources.** [lodestar@403d8c6fa](https://github.com/ChainSafe/lodestar/commit/403d8c6fa38e), [lodestar@28b43a9da](https://github.com/ChainSafe/lodestar/commit/28b43a9da89c)

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

**Sources.** [lodestar@2f90603c1](https://github.com/ChainSafe/lodestar/commit/2f90603c1bd6), [lodestar#8803](https://github.com/ChainSafe/lodestar/pull/8803), [lodestar#8946](https://github.com/ChainSafe/lodestar/pull/8946), [lodestar#9820](https://github.com/ChainSafe/lodestar/pull/9820), [lodestar#9863](https://github.com/ChainSafe/lodestar/pull/9863)

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

**Sources.** [silver#433](https://github.com/gattaca-com/silver/pull/433)

</details>


<a id="bls-036"></a>
<details>
<summary><b>bls-036</b> Copy BLS points without serialize roundtrip — <i>implemented · low · cpu</i></summary>

**Idea.** Clone public keys and signatures as in-memory structs instead of via serialize/deserialize round trips, and allocate domain buffers correctly.

**Best measured result.** Domain 29.5 ns/op -&gt; 7.55 ns/op (pr:prysm#5161)

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/impls/blst.rs:137`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L137) BlstAggregatePublicKey clone via in-memory from_public_key(to_public_key), no serialization
- [`crypto/bls/src/generic_public_key.rs:45`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/generic_public_key.rs#L45) derive(Clone) on in-memory point

**Sources.** [prysm#5161](https://github.com/OffchainLabs/prysm/pull/5161), [prysm#4770](https://github.com/OffchainLabs/prysm/pull/4770)

</details>


<a id="bls-037"></a>
<details>
<summary><b>bls-037</b> Pass BLS points by reference, avoid copies — <i>implemented · low · cpu, memory</i></summary>

**Idea.** When building signature sets, aggregating public keys and in aggregate verification, borrow cached pubkeys and signatures by reference and convert directly into aggregate types instead of cloning curve points. Each avoided clone saves a copy of a 96- or 192-byte point.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification/batch.rs:73`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification/batch.rs#L73) Cow::Borrowed pubkeys from cache
- [`beacon_node/beacon_chain/src/block_verification.rs:2241`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L2241) Cow::Borrowed pubkeys in block signature verifier
- [`crypto/bls/src/generic_signature_set.rs:68`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/generic_signature_set.rs#L68) signature and signing_keys held as Cow

**Sources.** [prysm#12944](https://github.com/OffchainLabs/prysm/pull/12944), [lighthouse#985](https://github.com/sigp/lighthouse/pull/985), [lighthouse#8610](https://github.com/sigp/lighthouse/pull/8610)

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


<a id="bls-044"></a>
<details>
<summary><b>bls-044</b> Subgroup-check each pubkey once and reuse it — <i>implemented · medium · cpu, memory</i></summary>

**Idea.** Validate each public key (infinity and subgroup check) once when first seen, record or cache the validated object, and reuse it for sync committee and other verification, aggregating trusted keys with plain point addition. Expensive group checks and re-deserialization are not repeated.

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/impls/blst.rs:93`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L93) aggregate(&amp;signing_keys,false), keys already checked
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:21`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L21) cache holds decompressed validated keys
- [`beacon_node/beacon_chain/src/sync_committee_verification.rs:652`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/sync_committee_verification.rs#L652),685 sync verification reads keys from the cache

**Sources.** [teku#4075](https://github.com/Consensys-Incorporated/teku/pull/4075), [teku#4836](https://github.com/Consensys-Incorporated/teku/pull/4836), [prysm#7971](https://github.com/OffchainLabs/prysm/pull/7971)

</details>


<a id="bls-049"></a>
<details>
<summary><b>bls-049</b> Fast G2 cofactor clearing and subgroup check — <i>implemented · low · cpu, sync</i></summary>

**Idea.** Use endomorphism-based G2 cofactor clearing in hash-to-G2 and the fast subgroup membership test, so hashing messages and checking signatures is cheaper.

**Best measured result.** hash-to-G2 more than doubled; syncing first 12k blocks ~16% faster (pr:teku#1827)

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.lock blst 0.3.17 ([`crypto/bls/src/impls/blst.rs:12`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L12) uses blst::min_pk)
- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/blst-0.3.17/blst/src/map_to_g2.c:327 clear_cofactor uses psi endomorphism

**Sources.** [teku#1827](https://github.com/Consensys-Incorporated/teku/pull/1827)

</details>


<a id="bls-053"></a>
<details>
<summary><b>bls-053</b> Verify deposit signatures only when the outcome depends on it — <i>implemented · medium · cpu, memory</i></summary>

**Idea.** When processing deposit requests or pending deposits (including Gloas builder onboarding), skip BLS signature verification for deposits whose result does not depend on it (pubkey already known or already pending, non-builder credentials), using a pubkey-to-index map. Only deposits that can create a new validator or builder pay for a pairing.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/process_operations.rs:735-760`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L735-L760) apply_deposit verifies signature only when pubkey not in registry
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:405-410`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L405-L410) pending deposits check signature only if validator unknown
- process_operations.rs:925-935 builder deposit skips non-builder credentials and known builders
- [`consensus/state_processing/src/builder_deposits_cache.rs:104-131`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/builder_deposits_cache.rs#L104-L131) batch-verified cache

**Sources.** [lighthouse#9946](https://github.com/sigp/lighthouse/pull/9946), [nimbus#8557](https://github.com/status-im/nimbus-eth2/pull/8557), [nimbus#8686](https://github.com/status-im/nimbus-eth2/pull/8686)

</details>


<a id="bls-054"></a>
<details>
<summary><b>bls-054</b> Fixed-size arrays for BLS serialization — <i>implemented · low · cpu</i></summary>

**Idea.** Return fixed-size byte arrays instead of heap-allocated Vecs from BLS public key and signature serialization and SSZ encode/decode. This removes one heap allocation per serialized key or signature.

**Best measured result.** considerably increases serialisation speeds (pr:lighthouse#1183)

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/impls/blst.rs:109`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L109) TPublicKey::serialize returns [u8; PUBLIC_KEY_BYTES_LEN]
- [`crypto/bls/src/impls/blst.rs:192`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L192) signature serialize returns [u8; SIGNATURE_BYTES_LEN]
- [`crypto/bls/src/generic_public_key_bytes.rs:17`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/generic_public_key_bytes.rs#L17) PublicKeyBytes is a fixed [u8; N]

**Sources.** [lighthouse#1183](https://github.com/sigp/lighthouse/pull/1183)

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

**Sources.** [lodestar#9849](https://github.com/ChainSafe/lodestar/pull/9849), [prysm#15467](https://github.com/OffchainLabs/prysm/pull/15467)

</details>


<a id="bls-058"></a>
<details>
<summary><b>bls-058</b> Lazy pubkey and signature decompression — <i>implemented · medium · cpu, sync, startup</i></summary>

**Idea.** Keep validator pubkeys and deposit signatures as raw compressed bytes in decoded state and decompress/validate them only on first use (in place or via a cache). Loading a BeaconState from disk then no longer decompresses every key, which was a third or more of sync CPU.

**Best measured result.** pubkey init was 1/3 or more of sync CPU; getState() nearly disappears from the perf trace (pr:nimbus#1369)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/validator/validator.rs:22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/validator/validator.rs#L22) Validator.pubkey is PublicKeyBytes
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:21-22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L21-L22) decompression only in the cache, once per validator
- validator_pubkey_cache.rs:54-75 cache loaded from store

**Sources.** [lighthouse#472](https://github.com/sigp/lighthouse/pull/472), [nimbus#1371](https://github.com/status-im/nimbus-eth2/pull/1371), [nimbus@db397cc5f](https://github.com/status-im/nimbus-eth2/commit/db397cc5f377), [nimbus#1369](https://github.com/status-im/nimbus-eth2/pull/1369)

</details>


<a id="bls-060"></a>
<details>
<summary><b>bls-060</b> Plain map instead of LRU for pubkey cache — <i>implemented · low · memory</i></summary>

**Idea.** Store decompressed validated pubkeys in a plain map behind a mutex instead of an LRU cache, since the working set (all validators) is never usefully evicted. This drops the LRU bookkeeping heap.

**Best measured result.** cache memory 222 MB -&gt; 158 MB (-64 MB) (pr:prysm#16654)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:25`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L25) pubkeys: Vec&lt;PublicKey&gt; indexed by validator index, no LRU
- validator_pubkey_cache.rs:26 indices: HashMap&lt;PublicKeyBytes, usize&gt;

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

**Sources.** [lodestar@a10477b4b](https://github.com/ChainSafe/lodestar/commit/a10477b4b8ac), [lodestar@459750fec](https://github.com/ChainSafe/lodestar/commit/459750fecfa8), [lodestar@dfda58c32](https://github.com/ChainSafe/lodestar/commit/dfda58c32c2b)

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


<a id="bls-064"></a>
<details>
<summary><b>bls-064</b> Verify block attestation signatures in parallel — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** During block import, verify the aggregated signatures of the block's attestations concurrently across cores (after preparing inputs sequentially) instead of one after another, failing on the first invalid one. Block import latency then scales down with cores.

**Gap in Lighthouse.** Core idea is done inside blst. Small residue: the Lighthouse wrapper loop in crypto/bls/src/impls/blst.rs:51-103 does the G2 signature subgroup_check and pubkey aggregation per set sequentially before handing to blst; these could be moved into the parallel phase (e.g. pass sigs_groupcheck=true to blst) for a minor latency gain.

**Impact.** Already realised: block attestation signature work scales with cores via blst's thread pool. Residual sequential subgroup checks are a minor share (order of ~10 ms for ~128 sets).

**Best measured result.** 36 attestations ~1.4-1.9s sequential; expected ~4x on 4 cores (pr:ethlambda#274)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/block_signature_verifier.rs:454-460`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/block_signature_verifier.rs#L454-L460) all block sets (incl. attestations) to one verify_signature_sets call; comment says blst parallelises
- [`crypto/bls/src/impls/blst.rs:109-111`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L109-L111) calls blst Signature::verify_multiple_aggregate_signatures
- ~/.cargo/registry/src/*/blst-0.3.17/src/lib.rs:1316-1389 std impl: spawns min(pool.max_count(), n_elems) workers on mt::da_pool(), each pulls sets via atomic counter and runs mul_n_aggregate (hash-to-curve + Miller loop), early-stops on an invalid set via shared AtomicBool, merges pairings, one finalverify
- ~/.cargo/registry/src/*/blst-0.3.17/src/lib.rs:35-50 da_pool = ThreadPool::default() (one thread per CPU) unless feature no-threads
- ~/.cargo/registry/src/*/blst-0.3.17/build.rs:51-52 sets feature="std" on all non-no_std targets; Lighthouse does not enable no-threads (Cargo.lock blst 0.3.17 depends on threadpool)

**Second check.** Read the blst 0.3.17 Rust binding source: verify_multiple_aggregate_signatures is multithreaded over a per-CPU threadpool with early abort, so the earlier 'no rayon' finding was wrong; parallelism lives in the dependency crate, not in Lighthouse code.

**Sources.** [caplin#7709](https://github.com/erigontech/erigon/pull/7709), [ethlambda#274](https://github.com/lambdaclass/ethlambda/pull/274)

</details>


<a id="bls-065"></a>
<details>
<summary><b>bls-065</b> Preallocate signature-set vectors with known capacity — <i>implemented · low · cpu, memory</i></summary>

**Idea.** Allocate the pubkey and signature-set vectors used in block, attestation and aggregate verification with their known final length instead of growing them by pushes, avoiding repeated reallocations.

**Impact.** Already done; no further gain.

**Best measured result.** negligible improvement to init sync (pr:prysm#6285)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification/batch.rs:62`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification/batch.rs#L62),168 with_capacity
- [`consensus/state_processing/src/per_block_processing/signature_sets.rs:306`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/signature_sets.rs#L306),339 with_capacity(attesting_indices_len)
- [`crypto/bls/src/impls/blst.rs:47-50`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L47-L50)

**Sources.** [prysm#15261](https://github.com/OffchainLabs/prysm/pull/15261), [prysm#6285](https://github.com/OffchainLabs/prysm/pull/6285), [lighthouse#2184](https://github.com/sigp/lighthouse/pull/2184), [lighthouse#1922](https://github.com/sigp/lighthouse/pull/1922)

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
<summary><b>bls-068</b> Prepopulate pubkey cache in background at startup — <i>implemented · medium · startup, sync, cpu</i></summary>

**Idea.** At startup, decompress all validator pubkeys from the finalized state into the pubkey cache in a background task, so initial sync does not pay decompression cost block by block.

**Best measured result.** sync runs at max speed from the start (total time unchanged) (pr:prysm#11482)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:54-75`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L54-L75) load_from_store reads uncompressed keys from the DB at startup, no state decompression
- validator_pubkey_cache.rs:144-155 first import decompresses in parallel with rayon
- [`beacon_node/beacon_chain/src/builder.rs:286`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L286) loaded at builder time

**Sources.** [prysm#11482](https://github.com/OffchainLabs/prysm/pull/11482)

</details>


<a id="bls-069"></a>
<details>
<summary><b>bls-069</b> API-submitted signatures bypass gossip verification queue — <i>implemented · medium · latency, cpu</i></summary>

**Idea.** Verify signatures from HTTP API submissions immediately or at the front of the BLS job queue, and keep separate queues per gossip service, so API jobs are not delayed behind large gossip batches under load.

**Best measured result.** under overload verifying API sets took &gt;1s before (pr:lodestar#5754)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:481-482`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L481-L482),956,1153 ApiRequestP0/P1 queues separate from gossip queues
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2308`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2308) API path verifies attestations directly, not in the gossip batch

**Sources.** [lodestar#5754](https://github.com/ChainSafe/lodestar/pull/5754), [caplin#12000](https://github.com/erigontech/erigon/pull/12000)

</details>


<a id="bls-070"></a>
<details>
<summary><b>bls-070</b> Cache pubkey deserialization keyed by compressed bytes — <i>implemented · low · cpu, sync</i></summary>

**Idea.** Cache the result of deserializing a BLS public key (decompression and subgroup check) keyed by its 48-byte compressed form. Validator keys repeat, so the hit rate is high and repeated decompression is skipped.

**Impact.** Keys are decompressed once per validator and kept, so repeated decompression is already avoided.

**Best measured result.** up to 25% of init-sync wall time; 1 to 2 blocks/s gain (pr:prysm#3583)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:24-26`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L24-L26) pubkeys Vec&lt;PublicKey&gt; plus indices HashMap&lt;PublicKeyBytes,usize&gt;
- validator_pubkey_cache.rs:119-157 decompress once on import, parallel on first start
- validator_pubkey_cache.rs:174 get(i)

**Sources.** [prysm#3583](https://github.com/OffchainLabs/prysm/pull/3583)

</details>


<a id="bls-072"></a>
<details>
<summary><b>bls-072</b> Shared read lock for pubkey cache lookups — <i>implemented · low · cpu, latency</i></summary>

**Idea.** Take only a shared read lock on pubkey cache gets, so concurrent signature verification workers do not serialize on lookups.

**Impact.** Lookups use a shared read lock; writes only on import of new validators.

**Best measured result.** lock contention disappears from mainnet pprof (pr:prysm#12646)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:507`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L507) validator_pubkey_cache: RwLock
- [`beacon_node/beacon_chain/src/sync_committee_verification.rs:621`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/sync_committee_verification.rs#L621) .read()
- gossip_verified_payload_attestation.rs:132 .read()

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

**Sources.** [teku#4124](https://github.com/Consensys-Incorporated/teku/pull/4124)

</details>


<a id="bls-079"></a>
<details>
<summary><b>bls-079</b> Put aggregate signature in the shared Miller loop — <i>implemented · low · cpu</i></summary>

**Idea.** In batch signature verification, pair the aggregate signature with -G1 inside the same multi-Miller loop as the message pairs instead of running a separate Miller loop for the signature.

**Impact.** blst's Pairing accumulates the randomised signatures and does a single final Miller loop with the generator, so no separate signature Miller loop exists.

**Best measured result.** block envelope batch 694 -&gt; 645 us (-7.1%) (pr:silver#348)

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/impls/blst.rs:113`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L113) verify_multiple_aggregate_signatures
- blst-0.3.17/src/lib.rs:1415-1435 Pairing mul_n_aggregate + commit + finalverify

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

**Sources.** [silver#296](https://github.com/gattaca-com/silver/pull/296)

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


<a id="bls-085"></a>
<details>
<summary><b>bls-085</b> Skip signature checks for trusted or pre-verified blocks — <i>implemented · medium · S · cpu</i></summary>

**Idea.** Pass a verify-signatures flag through block processing and skip BLS checks in the state transition for blocks already batch-verified or known valid (trusted finalized history during sync), for every fork. This removes the dominant BLS cost per block and avoids polluting the pubkey cache.

**Gap in Lighthouse.** Only remaining difference: forward range sync of finalized history still batch-verifies all signatures (no checkpoint-trust skip), which is a trust-model choice rather than a missing mechanism.

**Impact.** Already realized: the state transition never re-verifies BLS for batch-verified blocks, and stored/finalized blocks are replayed without BLS.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing.rs:71-77`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing.rs#L71-L77),147-164 BlockSignatureStrategy flag (NoVerification/VerifyBulk/...) threaded through per_block_processing
- [`beacon_node/beacon_chain/src/block_verification.rs:671-721`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L671-L721) signature_verify_chain_segment batch-verifies all block signatures up front
- [`beacon_node/beacon_chain/src/block_verification.rs:1706-1712`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1706-L1712) per_block_processing then runs with NoVerification ('Signatures were verified earlier')
- [`consensus/state_processing/src/block_replayer.rs:113-114`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/block_replayer.rs#L113-L114) no_signature_verification for replay of trusted stored blocks, used at [`beacon_node/store/src/hot_cold_store.rs:2566`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2566)
- [`beacon_node/store/src/reconstruct.rs:165`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/reconstruct.rs#L165) state reconstruction of finalized history uses NoVerification
- [`beacon_node/beacon_chain/src/historical_blocks.rs:393-415`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_blocks.rs#L393-L415) backfill verifies only proposer signatures in one batch

**Second check.** Source PRs (nimbus#4085, lodestar flag commits) are exactly 'skip state-transition BLS for blocks already batch-verified / trusted'; Lighthouse does this via BlockSignatureStrategy::NoVerification after signature_verify_chain_segment and in BlockReplayer/reconstruction, which the earlier review missed.

**Sources.** [lodestar@476e3a5b5](https://github.com/ChainSafe/lodestar/commit/476e3a5b50f7), [lodestar@6b65c80a2](https://github.com/ChainSafe/lodestar/commit/6b65c80a294f), [nimbus#4085](https://github.com/status-im/nimbus-eth2/pull/4085)

</details>


<a id="bls-087"></a>
<details>
<summary><b>bls-087</b> Do not recheck proposer signature verified at gossip — <i>implemented · medium · S · cpu</i></summary>

**Idea.** Build block signature sets without the proposer signature when that signature was already verified during gossip validation, so it is not verified a second time at import.

**Impact.** Already saves one signature verification per gossip block.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1252`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1252) from_gossip_verified_block 'Does not re-verify the proposer signature'
- consensus/state_processing/.../block_signature_verifier.rs:168 include_all_signatures_except_proposal

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


<a id="bls-090"></a>
<details>
<summary><b>bls-090</b> Route batchable vs latency-critical BLS jobs separately — <i>implemented · medium · S · latency, cpu</i></summary>

**Idea.** Send batchable signature jobs (gossip attestations) to the batching worker threads and verify non-batchable latency-critical jobs (blocks) directly, to keep BLS job wait time under a target (100ms).

**Impact.** Batchable vs block work already separated by the beacon processor queues; no BLS pool to add.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:1054`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1054) GossipAttestationBatch batches attestations on worker threads
- [`beacon_node/beacon_chain/src/block_verification.rs:1176`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1176) blocks verified directly in their own work item (GossipBlock, lib.rs:1239)

**Sources.** [lodestar#3793](https://github.com/ChainSafe/lodestar/pull/3793)

</details>


<a id="bls-091"></a>
<details>
<summary><b>bls-091</b> Store pubkeys uncompressed on disk to skip decompression — <i>implemented · medium · S · startup, cpu</i></summary>

**Idea.** Persist the validator pubkey cache (and key files) in decompressed/uncompressed form, so startup loads keys without decompressing every validator pubkey.

**Impact.** Startup avoids decompressing all validator keys.

**Best measured result.** startup time improved dramatically (no number) (pr:lighthouse#5897)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:233`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L233) serialize_uncompressed stored
- validator_pubkey_cache.rs:238 deserialize_uncompressed on load

**Sources.** [lighthouse#5897](https://github.com/sigp/lighthouse/pull/5897), [lighthouse@1b252c3f8](https://github.com/sigp/lighthouse/commit/1b252c3f82db)

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

**Sources.** [nimbus#5268](https://github.com/status-im/nimbus-eth2/pull/5268)

</details>


