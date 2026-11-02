# kzg

43 ideas: 7 not, 7 partial, 22 implemented, 7 n/a; 6 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [kzg-001](#kzg-001) | Keep the KZG library at its latest release | implemented | low | S | cpu, startup |
| [kzg-002](#kzg-002) | Enable fixed-base precomputation tables in the KZG setup | implemented | high | S | cpu, memory, latency, startup |
| [kzg-003](#kzg-003) **★** | AVX-512 IFMA FFT for blob cell extension | not | medium | L | cpu, latency |
| [kzg-004](#kzg-004) **★** | AVX-512 IFMA MSM and pairing for cell batch verify | not | medium | L | cpu, latency |
| [kzg-005](#kzg-005) | Vectorized G1 point decompression and subgroup check | not | low | L | cpu |
| [kzg-006](#kzg-006) | Use the fastest available native KZG backend | implemented | low | M | cpu, latency |
| [kzg-007](#kzg-007) **★** | Run KZG work off the async runtime or event loop | partial | medium | S | cpu, latency |
| [kzg-008](#kzg-008) | Dedicated prioritized executor for cell computation and recovery | implemented | low | S | latency, cpu |
| [kzg-009](#kzg-009) **★** | Batch KZG verify all columns of a block or segment | partial | medium | S | cpu, latency, sync |
| [kzg-010](#kzg-010) **★** | Drain queued gossip columns into one KZG batch | not | medium | M | cpu, latency |
| [kzg-011](#kzg-011) | Split KZG batch verification into parallel chunks | implemented | medium | S | cpu, latency, sync |
| [kzg-012](#kzg-012) | Verify each gossip column in parallel, no batch queue | implemented | low | S | cpu, latency |
| [kzg-013](#kzg-013) | Compute and recover cells per blob in parallel | partial | low | S | cpu, latency |
| [kzg-014](#kzg-014) | Zip per-blob inputs before the parallel iterator | implemented | low | S | cpu, latency |
| [kzg-015](#kzg-015) | Pass blobs by reference into KZG calls | implemented | low | S | cpu, memory |
| [kzg-016](#kzg-016) | Wrap raw KZG bytes directly in SSZ commitment types | implemented | low | S | cpu, memory |
| [kzg-017](#kzg-017) | Do not copy cell recovery results per worker | not | low | S | memory, cpu |
| [kzg-018](#kzg-018) | Flatten batch inputs into one preallocated buffer | n/a | low |  | cpu, memory |
| [kzg-019](#kzg-019) | Build batch verify vectors in a single pass | implemented | low | S | cpu, memory |
| [kzg-020](#kzg-020) | Fewer allocations and clones in blob verification | implemented | low | S | memory, cpu |
| [kzg-021](#kzg-021) | Box large blob values in KZG helpers | n/a | low |  | memory |
| [kzg-022](#kzg-022) | Verify a data column's KZG proofs only once | implemented | medium | S | cpu |
| [kzg-023](#kzg-023) | Skip KZG verification for EL-sourced or locally built data | implemented | high | S | cpu, latency |
| [kzg-024](#kzg-024) **★** | Take cell proofs from the execution client | partial | high | S | cpu, latency |
| [kzg-025](#kzg-025) | Load the KZG trusted setup lazily and once | partial | low | S | startup, memory, cpu |
| [kzg-026](#kzg-026) | Embed the trusted setup in the binary | implemented | low | S | startup |
| [kzg-027](#kzg-027) | Ship precomputed G1 monomial points in the setup | implemented | low | S | startup, cpu |
| [kzg-028](#kzg-028) | Skip subgroup checks on the constant trusted setup | not | low | S | startup |
| [kzg-029](#kzg-029) | Read setup points directly into library buffers | n/a | low |  | memory, startup, cpu |
| [kzg-030](#kzg-030) | Compute cells without proofs for column reconstruction | partial | low | M | cpu |
| [kzg-031](#kzg-031) | Single combined recover-cells-and-proofs library call | implemented | low | S | cpu |
| [kzg-032](#kzg-032) | Sort matrix entries by blob row before building cells | n/a | low | S | cpu |
| [kzg-033](#kzg-033) | Benchmark KZG column verification with fixtures | not | low | S | cpu |
| [kzg-034](#kzg-034) | Pre-generated blob bundles in tests | implemented | low | S | cpu, latency |
| [kzg-035](#kzg-035) | Stack buffer for the versioned hash | implemented | low | S | memory, cpu |
| [kzg-036](#kzg-036) | Correctly sized preallocation for KZG proof lists | n/a | low | S | memory |
| [kzg-037](#kzg-037) | Compute blob byte size from count, not by streaming | n/a | low | S | cpu, memory |
| [kzg-038](#kzg-038) | Pass cell indices as native integers | implemented | low | S | cpu |
| [kzg-039](#kzg-039) | Drop length checks the KZG library already does | partial | low | S | cpu |
| [kzg-040](#kzg-040) | Single-blob KZG verify for one-blob paths | n/a | low | S | cpu, latency |
| [kzg-041](#kzg-041) | Disable KZG library internal multithreading | implemented | medium | S | cpu |
| [kzg-042](#kzg-042) | Reuse cells computed during blob verification for column building | implemented | low | S | cpu, latency |
| [kzg-043](#kzg-043) | Parse trusted setup from text without binary conversion | implemented | low | S | startup |

★ actionable. Click an id for the full record.

## Ideas

<a id="kzg-001"></a>
<details>
<summary><b>kzg-001</b> Keep the KZG library at its latest release — <i>implemented · low · S · cpu, startup</i></summary>

**Idea.** Bump the KZG libraries (c-kzg-4844, rust-eth-kzg, jc-kzg, blst) to the newest release to pick up upstream speedups, including faster trusted-setup context load. Check the KZG crate versions in the Lighthouse Cargo.toml against the latest upstream release.

**Impact.** None measurable; c-kzg 2.1.8 and blst 0.3.17 are the latest on crates.io. rust_eth_kzg 0.10.0 exists but only changes Node bindings to single-threaded.

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.toml:224
- Cargo.lock (rust_eth_kzg 0.9.1, c-kzg 2.1.8, blst 0.3.17)

**Skeptic check.** Checked crates.io: c-kzg max 2.1.8, blst max 0.3.17, rust_eth_kzg max 0.10.0, and the v0.10.0 release notes list only the Node binding change. So 0.9.1 has all the Rust-side speedups.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine#615](https://github.com/grandinetech/grandine/pull/615), [prysm#15708](https://github.com/OffchainLabs/prysm/pull/15708), [lighthouse#7870](https://github.com/sigp/lighthouse/pull/7870), [teku#10427](https://github.com/Consensys-Incorporated/teku/pull/10427), [lighthouse#6906](https://github.com/sigp/lighthouse/pull/6906)

</details>


<a id="kzg-002"></a>
<details>
<summary><b>kzg-002</b> Enable fixed-base precomputation tables in the KZG setup — <i>implemented · high · S · cpu, memory, latency, startup</i></summary>

**Idea.** Load the trusted setup with a nonzero fixed-base precompute window (7 to 9 bits, higher on supernodes) so the fixed-base MSMs in cell/proof computation and cell recovery run up to about 2x faster, at tens of MiB of memory. Check the precompute argument where Lighthouse initializes its KZG context, and whether it is larger on supernodes.

**Impact.** Main saving taken (width 8 precomp whenever PeerDAS is scheduled). The width is not raised on supernodes, a small sublinear extra gain.

**Best measured result.** pr:lighthouse#5795: table off doubles the time to compute cells and proofs (pr:nimbus#8405: about 1.6x faster at 48 MiB)

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/kzg/src/lib.rs:76-88`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/kzg/src/lib.rs#L76-L88)
- ekzg-serialization-0.9.1/src/constants.rs:65
- [`beacon_node/client/src/builder.rs:233-237`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L233-L237)

**Skeptic check.** Verified Kzg::new_from_trusted_setup uses UsePrecomp::Yes{width: RECOMMENDED_PRECOMP_WIDTH=8}, and the client builder picks it when is_peer_das_scheduled. The fixed supernode width is a minor tuning option, not a missing mechanism.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#5795](https://github.com/sigp/lighthouse/pull/5795), [nimbus#8405](https://github.com/status-im/nimbus-eth2/pull/8405), [prysm#14399](https://github.com/OffchainLabs/prysm/pull/14399), [teku#9691](https://github.com/Consensys-Incorporated/teku/pull/9691), [teku#9725](https://github.com/Consensys-Incorporated/teku/pull/9725), [teku#10197](https://github.com/Consensys-Incorporated/teku/pull/10197)

</details>


<a id="kzg-003"></a>
<details>
<summary><b>kzg-003</b> AVX-512 IFMA FFT for blob cell extension — <i>not · medium · L · cpu, latency</i></summary>

**Idea.** Compute the 128 extended cells of a blob with an 8-lane AVX-512 IFMA field FFT instead of scalar blst arithmetic, falling back to scalar when IFMA is absent. Check whether the KZG backend Lighthouse uses for compute_cells has a SIMD FFT path.

**Gap in Lighthouse.** No SIMD field FFT anywhere in the KZG stack; cell extension uses ekzg-erasure-codes/ekzg-polynomial scalar FFT over blstrs Scalar (blst ADX asm). Would need an IFMA field/FFT backend behind runtime CPU detection inside rust_eth_kzg or a replacement of Kzg::compute_cells.

**Impact.** Up to ~20x on per-blob cell extension on IFMA CPUs, but absolute cost is small on most nodes since EL getBlobsV2 supplies proofs; matters for block production and reconstruction.

**Best measured result.** pr:silver#412: 1717.6 us -&gt; 79.7 us per blob (21.55x)

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.lock: rust_eth_kzg 0.9.1, ekzg-* 0.9.1, blstrs 0.7.1, blst 0.3.17
- grep avx512\|ifma\|avx2\|_mm512\|simd\|vpmadd52 over ~/.cargo/registry/src/*/{blst-0.3.17,blstrs-0.7.1,ekzg-*-0.9.1,rust_eth_kzg-0.9.1}: no hits
- blst-0.3.17/build.rs:160-180 only ISA switch is ADX (scalar mulx/adcx), or portable

**Second check.** Searched blst assembly/build flags and all ekzg crates, not only rust_eth_kzg; the only ISA-specific path is blst's ADX scalar Montgomery multiply, which is not lane-parallel.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [silver#412](https://github.com/gattaca-com/silver/pull/412), [silver#419](https://github.com/gattaca-com/silver/pull/419)

</details>


<a id="kzg-004"></a>
<details>
<summary><b>kzg-004</b> AVX-512 IFMA MSM and pairing for cell batch verify — <i>not · medium · L · cpu, latency</i></summary>

**Idea.** Batch-verify cell KZG proofs with an 8-lane AVX-512 IFMA Pippenger MSM (signed-digit buckets, batched affine adds, lazy reduction) and run the final pairing on IFMA lanes with SHA-NI for the challenge hash. Check whether Lighthouse's cell verification backend has a vectorized MSM and pairing.

**Gap in Lighthouse.** Some algorithmic tricks from the idea (Booth signed digits, batched affine addition with batch inversion) already exist in ekzg, but only for fixed-base MSM, and nothing is vectorized; verify-path MSM and pairing go to blst scalar code. Would need an IFMA multi-lane MSM and Miller loop backend, feature-gated with fallback.

**Impact.** Up to ~4.7x cheaper cell batch verification on AVX-512 IFMA CPUs; meaningful on supernodes and range sync, small on regular nodes.

**Best measured result.** pr:silver#413: verify 128 columns 116.12 ms -&gt; 24.78 ms (4.69x vs c-kzg)

**Evidence (Lighthouse @ 928b61e719).**

- ekzg-multi-open-0.9.1/src/fk20/verifier.rs:186,200,224 g1_lincomb, :251 multi_pairings
- ekzg-bls12-381-0.9.1/src/lincomb.rs:29 G1Projective::multi_exp (blstrs -&gt; blst Pippenger, scalar ADX)
- ekzg-bls12-381-0.9.1/src/booth_encoding.rs, batch_addition.rs: signed-digit and batched affine adds exist but only in the fixed-base MSM (fixed_base_msm_window.rs:4), scalar code
- No avx512/ifma/simd hits in blst-0.3.17, blstrs-0.7.1, ekzg-*-0.9.1

**Second check.** Traced verify_multi_opening down to blstrs multi_exp/multi_pairings and checked ekzg's own MSM helpers; found non-SIMD signed-digit and batched-affine code, which does not count as the vectorized idea.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [silver#410](https://github.com/gattaca-com/silver/pull/410), [silver#413](https://github.com/gattaca-com/silver/pull/413), [silver#427](https://github.com/gattaca-com/silver/pull/427)

</details>


<a id="kzg-005"></a>
<details>
<summary><b>kzg-005</b> Vectorized G1 point decompression and subgroup check — <i>not · low · L · cpu</i></summary>

**Idea.** Decompress and subgroup-check compressed G1 points (KZG proofs, commitments, pubkeys) eight at a time with AVX-512 IFMA instead of one at a time in blst. Check how Lighthouse deserializes KZG proofs and commitments before verification.

**Gap in Lighthouse.** Would need a vectorized decompress/subgroup-check in or under rust_eth_kzg (or a fork) with runtime CPU detection; Lighthouse itself passes compressed bytes straight to the library.

**Impact.** Saves tens of microseconds per point on IFMA CPUs only; commitments and proofs per column are few, so negligible per block.

**Best measured result.** pr:silver#397: 3.67x over blst, 8.6 us vs 31.6 us per point

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/kzg/src/lib.rs:63`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/kzg/src/lib.rs#L63) Kzg wraps rust_eth_kzg DASContext only
- Cargo.lock rust_eth_kzg 0.9.1 uses ekzg-bls12-381 (portable Rust), no AVX-512 IFMA path

**Sources.** [silver#397](https://github.com/gattaca-com/silver/pull/397)

</details>


<a id="kzg-006"></a>
<details>
<summary><b>kzg-006</b> Use the fastest available native KZG backend — <i>implemented · low · M · cpu, latency</i></summary>

**Idea.** Switch blob and cell KZG operations to a faster native library (C or optimized Rust, or a runtime-selectable alternative such as Constantine) instead of a slower implementation. Check which KZG backend Lighthouse uses for column construction and cell verification and compare it in benchmarks with the alternatives.

**Impact.** Already on rust-eth-kzg (native optimized Rust on blst) with precomputation, for both blob and cell operations.

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/kzg/src/lib.rs:63-65`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/kzg/src/lib.rs#L63-L65)
- [`crypto/kzg/src/lib.rs:94-125`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/kzg/src/lib.rs#L94-L125)
- Cargo.toml:224

**Skeptic check.** Verified Kzg wraps rust_eth_kzg::DASContext for blob proofs, cell computation, cell verification and recovery. c-kzg is in Cargo.lock only through third-party deps, not used by Lighthouse KZG code.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#17313](https://github.com/OffchainLabs/prysm/pull/17313), [lighthouse#6212](https://github.com/sigp/lighthouse/pull/6212), [nimbus#4732](https://github.com/status-im/nimbus-eth2/pull/4732)

</details>


<a id="kzg-007"></a>
<details>
<summary><b>kzg-007</b> Run KZG work off the async runtime or event loop — <i>partial · medium · S · cpu, latency</i></summary>

**Idea.** Run KZG proof verification and cell computation on worker or blocking threads, not on the async runtime or main event loop, so networking, attestation production and other tasks are not stalled. Check whether every Lighthouse KZG call on the gossip and import paths runs via spawn_blocking or the beacon processor, not inline in an async task.

**Gap in Lighthouse.** Lookup-sync RPC data runs KZG inline on the tokio runtime. Work::RpcCustodyColumn and Work::RpcBlobs go through TaskSpawner::spawn_async (executor.spawn, not spawn_blocking). In that task, BeaconChain::process_rpc_custody_columns -&gt; check_rpc_custody_columns_availability_and_import calls DataAvailabilityChecker::put_rpc_custody_columns (KzgVerifiedDataColumn::from_batch_with_scoring) or PendingPayloadCache::put_rpc_custody_columns (from_batch_with_scoring_and_commitments) synchronously. process_rpc_blobs -&gt; check_rpc_blob_availability_and_import -&gt; put_rpc_blobs (KzgVerifiedBlobList::new) does the same. The checkpoint-anchor envelope branch in process_chain_segment also calls verify_columns_against_block inline in async code. Fix: wrap these KZG calls in spawn_blocking_handle, as verify_data_column_sidecar_for_gossip and verify_partial_data_column_sidecar_for_gossip already do.

**Impact.** Batch cell-proof verification of several columns times up to the blob count can block a tokio worker for tens of ms during lookups. This can stall networking and other async tasks on the shared runtime. Gossip, engine getBlobs, reconstruction, HTTP publish and range/backfill sync are already off-runtime.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:1699-1703`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1699-L1703)
- [`beacon_node/beacon_processor/src/lib.rs:1776-1784`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1776-L1784)
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:252-277`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L252-L277)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3700-3783`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3700-L3783)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4203-4216`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4203-L4216)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4264-4300`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4264-L4300)
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:322-372`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L322-L372)
- [`beacon_node/beacon_chain/src/pending_payload_cache/mod.rs:321-332`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/mod.rs#L321-L332)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3266-3270`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3266-L3270)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2514-2547`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2514-L2547)

**Skeptic check.** Earlier evidence was right for gossip columns, partial columns, fetch_blobs, reconstruction and HTTP publish. It missed the RPC lookup paths, which are AsyncFn work spawned with executor.spawn and run batch KZG verification inline.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lodestar#7936](https://github.com/ChainSafe/lodestar/pull/7936), [lodestar#8234](https://github.com/ChainSafe/lodestar/pull/8234), [lodestar#7989](https://github.com/ChainSafe/lodestar/pull/7989), [nimbus#8810](https://github.com/status-im/nimbus-eth2/pull/8810), [grandine#421](https://github.com/grandinetech/grandine/pull/421)

</details>


<a id="kzg-008"></a>
<details>
<summary><b>kzg-008</b> Dedicated prioritized executor for cell computation and recovery — <i>implemented · low · S · latency, cpu</i></summary>

**Idea.** Run cell computation and cell recovery on a dedicated executor apart from the shared thread pool, and give computation for the head block priority over background recovery, to cut tail latency under load. Check whether Lighthouse's KZG compute and reconstruction share the global rayon pool and whether recovery can delay head-block work.

**Impact.** Recovery already runs on its own rayon pool apart from head-block cell compute (global pool) and is queued and delayed behind block and column work; only OS-level oversubscription remains.

**Best measured result.** pr:grandine#596: reduces p99 latency during high load (no number)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:3811`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3811)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3845`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3845)
- [`common/task_executor/src/rayon_pool_provider.rs:4-21`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/task_executor/src/rayon_pool_provider.rs#L4-L21)
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:671`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L671)
- [`beacon_node/beacon_processor/src/lib.rs:944-953`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L944-L953)

**Second check.** Beyond the earlier review, checked that the HighPriority pool is effectively dedicated to reconstruction in the BN, and found the beacon processor queue order plus the reprocess delay queue that defer recovery behind gossip block/column work, which is equivalent to Grandine #596 (dedicated executor, computation over recovery).

**Skeptic check.** Confirmed reconstruct_data_columns runs via spawn_blocking_with_rayon_async(HighPriority) for Fulu and Gloas, while getBlobs column compute uses spawn_blocking on the global pool, and the reprocess queue delays reconstruction. Earlier evidence correct; Grandine #596 adds the same split plus compute-over-recovery priority.

**Verdict history.** partial (checked) → implemented (refuted) → implemented (skeptic)

**Sources.** [grandine#596](https://github.com/grandinetech/grandine/pull/596)

</details>


<a id="kzg-009"></a>
<details>
<summary><b>kzg-009</b> Batch KZG verify all columns of a block or segment — <i>partial · medium · S · cpu, latency, sync</i></summary>

**Idea.** When a code path holds more than one data column or blob (block import, RPC response, range sync segment, getBlobs result), verify all their KZG proofs in one batch call instead of per item, and fall back to per-item checks only to attribute a failure. Check Lighthouse's RPC, sync, getBlobs and import paths for per-column verification loops.

**Gap in Lighthouse.** Custody backfill (historical_data_columns) already batches across blocks, and blobs batch across a segment, but forward range sync (signature_verify_chain_segment) and block backfill (batch_verify_kzg_for_range_sync_blocks) still verify columns once per block. Collect (column, commitments) pairs of all blocks in the segment into one validate_data_columns_with_commitments call, as historical_data_columns.rs already does, with per-block fallback only to attribute a failure.

**Impact.** Range sync and backfill column KZG: fewer, larger multi-pairing batches and better rayon utilisation; likely 1.5-3x less KZG time while syncing, no effect at head.

**Best measured result.** pr:lighthouse#4903: batch ~32x faster than a loop (pr:prysm#14559: 32 blocks 12-13 s -&gt; 700 ms)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/historical_data_columns.rs:172-188`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_data_columns.rs#L172-L188) custody backfill groups columns of many blocks (each with its commitments) into ONE validate_data_columns_with_commitments call
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:495-525`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L495-L525) batch_verify_kzg_for_range_sync_blocks: blobs batched across segment, but columns call verify_columns_against_block per block (comment at :507)
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:676`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L676) backfill block batches use that per-block column path
- [`beacon_node/beacon_chain/src/block_verification.rs:701-706`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L701-L706) signature_verify_chain_segment verifies columns per block in the loop
- [`beacon_node/beacon_chain/src/kzg_utils.rs:119`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L119) validate_data_columns_with_commitments already accepts (column, commitments) pairs from different blocks
- [`beacon_node/beacon_chain/src/data_column_verification.rs:507-540`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L507-L540) RPC from_batch_with_scoring* batch all columns of one response

**Second check.** Found an existing cross-block column batch in custody backfill (historical_data_columns.rs) the earlier review missed, and confirmed the sync network layer does no separate KZG pre-check; the per-block loop remains in forward range sync and block backfill, so partial stands with a template to copy.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [ethlambda#754](https://github.com/lambdaclass/ethlambda/pull/754), [lighthouse#6851](https://github.com/sigp/lighthouse/pull/6851), [nimbus#8302](https://github.com/status-im/nimbus-eth2/pull/8302), [prysm#14559](https://github.com/OffchainLabs/prysm/pull/14559), [lighthouse#4934](https://github.com/sigp/lighthouse/pull/4934), [lighthouse#7582](https://github.com/sigp/lighthouse/pull/7582), [nimbus#8275](https://github.com/status-im/nimbus-eth2/pull/8275), [lighthouse#4903](https://github.com/sigp/lighthouse/pull/4903), [teku#7018](https://github.com/Consensys-Incorporated/teku/pull/7018)

</details>


<a id="kzg-010"></a>
<details>
<summary><b>kzg-010</b> Drain queued gossip columns into one KZG batch — <i>not · medium · M · cpu, latency</i></summary>

**Idea.** Feed gossip data column KZG verification through a worker that drains all pending requests into one batch call (immediately when idle, accumulating while busy), with per-item fallback on failure. Check whether Lighthouse verifies each gossip column's KZG proofs individually or batches concurrent arrivals.

**Gap in Lighthouse.** Each gossip column is its own beacon processor work item and runs its own KZG verification; no queue drains pending gossip columns into one batch. Add a batched work type for gossip columns (like GossipAttestationBatch) that runs the per-column non-KZG checks, then one validate_data_columns_with_commitments over all pending columns, falling back to per-column on failure.

**Impact.** At head many custody columns arrive together; one batch amortises pairing cost and spreads cells over rayon, possibly tens of ms earlier data availability per block.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:944`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L944) gossip_data_column_queue.pop() takes one item per worker; only attestations/aggregates have batch work variants (lib.rs:382-411, 962)
- [`beacon_node/beacon_processor/src/lib.rs:417`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L417) Work::GossipDataColumnSidecar(AsyncFn) single-item work
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1187`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1187) gossip validation calls verify_kzg_for_data_column for one column
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1035`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1035) verify_kzg_for_data_column single-column (KZG_VERIFICATION_DATA_COLUMN_SINGLE_TIMES)
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1623`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1623) missing_cells_for_column_sidecar only skips cells already verified (partial/getBlobs), not a batching mechanism

**Second check.** Checked beacon_processor queue scheduling (single pop, batch variants only for attestations/aggregates) and the cells-to-verify view that avoids re-verifying already-known cells; neither batches concurrent gossip columns, so not stands.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [prysm#15617](https://github.com/OffchainLabs/prysm/pull/15617), [prysm#15609](https://github.com/OffchainLabs/prysm/pull/15609), [silver#177](https://github.com/gattaca-com/silver/pull/177)

</details>


<a id="kzg-011"></a>
<details>
<summary><b>kzg-011</b> Split KZG batch verification into parallel chunks — <i>implemented · medium · S · cpu, latency, sync</i></summary>

**Idea.** Split large KZG cell-proof batch verifications into fixed-size chunks run across a thread pool, and on failure search for the first invalid column instead of re-verifying everything one by one. Check whether Lighthouse's range/backfill column verification is one single-threaded batch and how it handles a failed batch.

**Impact.** Batch cell-proof verification is split per column index across rayon with attributable early exit on failure.

**Best measured result.** pr:lighthouse#7921: invalid-column worst case 12.15 s before short-circuit; epoch batch 294 ms with rayon

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/kzg/src/lib.rs:232-300`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/kzg/src/lib.rs#L232-L300)
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:495-522`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L495-L522)
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:639-666`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L639-L666)

**Skeptic check.** verify_cell_proof_batch groups cells by column index, verifies each group in into_par_iter, and collect::&lt;Result&gt; returns the first failing column index. Used by range sync, backfill and RPC columns. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#7921](https://github.com/sigp/lighthouse/pull/7921), [prysm#16220](https://github.com/OffchainLabs/prysm/pull/16220)

</details>


<a id="kzg-012"></a>
<details>
<summary><b>kzg-012</b> Verify each gossip column in parallel, no batch queue — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** On gossip, verify each data column sidecar's KZG proofs immediately on its own core instead of waiting in a batch queue, which removes queue latency. Check whether Lighthouse gossip column verification waits for or is serialized behind other columns.

**Impact.** Each gossip column is its own work item that verifies KZG in its own spawn_blocking task; no batching queue.

**Best measured result.** pr:prysm#16240: gossip verification 185 ms -&gt; 26 ms, DA wait 82.2 ms -&gt; 16.3 ms

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/mod.rs:214-230`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L214-L230)
- [`beacon_node/beacon_processor/src/lib.rs:1709-1713`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1709-L1713)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2451-2477`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2451-L2477)
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1187`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1187)

**Skeptic check.** verify_data_column_sidecar_for_gossip runs GossipVerifiedDataColumn::new in spawn_blocking_handle per column, and verify_kzg_for_data_column is inline. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#16240](https://github.com/OffchainLabs/prysm/pull/16240)

</details>


<a id="kzg-013"></a>
<details>
<summary><b>kzg-013</b> Compute and recover cells per blob in parallel — <i>partial · low · S · cpu, latency</i></summary>

**Idea.** Compute cells and proofs, and recover missing cells, for each blob on its own thread (bounded by core count), because the per-blob work is independent and the KZG library is single-threaded. Check Lighthouse's blobs_to_data_column_sidecars and reconstruction for a parallel iterator over blobs.

**Gap in Lighthouse.** reconstruct_blobs_with_indices (used by reconstruct_blobs and reconstruct_blob_sidecars for the blob_sidecars / blobs HTTP API) iterates blob_indices with a serial .into_iter() and calls recover_cells_and_compute_kzg_proofs per blob, so a node with 50-99% of columns recovers every requested blob on one core.

**Impact.** Hot paths (getBlobs column build, gossip column reconstruction) are already parallel over blobs; parallelising the API blob recovery cuts blob API latency roughly by core count for full-blob requests on non-full-custody supernodes.

**Best measured result.** pr:prysm#14804: DataColumnSidecars 2117 ms -&gt; 260 ms; RecoverCellsAndProofs 2180 ms -&gt; 254 ms

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/kzg_utils.rs:382-420`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L382-L420)
- [`beacon_node/beacon_chain/src/kzg_utils.rs:425-440`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L425-L440)
- [`beacon_node/beacon_chain/src/kzg_utils.rs:475-489`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L475-L489)
- [`beacon_node/beacon_chain/src/kzg_utils.rs:889-907`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L889-L907)
- [`beacon_node/beacon_chain/src/kzg_utils.rs:767-826`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L767-L826)
- [`beacon_node/http_api/src/block_id.rs:437-451`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L437-L451)

**Skeptic check.** Verified par_iter over blobs in compute_cells_with_provided_proofs, blobs_to_partial_data_columns, compute_cells and reconstruct_data_columns. The serial recovery in reconstruct_blobs_with_indices is a real, if off-hot-path, gap that the earlier verdict noted but still called implemented.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [nimbus#7286](https://github.com/status-im/nimbus-eth2/pull/7286), [lighthouse#5805](https://github.com/sigp/lighthouse/pull/5805), [prysm#14804](https://github.com/OffchainLabs/prysm/pull/14804), [caplin#25514](https://github.com/erigontech/erigon/pull/25514), [caplin#24861](https://github.com/erigontech/erigon/pull/24861)

</details>


<a id="kzg-014"></a>
<details>
<summary><b>kzg-014</b> Zip per-blob inputs before the parallel iterator — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Zip blobs and their per-blob inputs into one indexed collection before calling par_iter for cell and proof computation, so rayon splits the work evenly. Check the iterator shape in Lighthouse's blobs_to_data_column_sidecars.

**Impact.** Indexed Vec/slice par_iter already used, so rayon splits evenly.

**Best measured result.** pr:lighthouse#7574: about 10% faster, 12.04 ms -&gt; 10.72 ms

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/kzg_utils.rs:395-401`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L395-L401)
- [`beacon_node/beacon_chain/src/kzg_utils.rs:343-344`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L343-L344)
- [`beacon_node/beacon_chain/src/kzg_utils.rs:436-437`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L436-L437)

**Skeptic check.** compute_cells_with_provided_proofs collects blobs.zip(proof_chunks) into a Vec before into_par_iter, which is the #7574 change; the other builders iterate indexed slices or Vecs. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#7574](https://github.com/sigp/lighthouse/pull/7574)

</details>


<a id="kzg-015"></a>
<details>
<summary><b>kzg-015</b> Pass blobs by reference into KZG calls — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Pass 128 KiB blobs to KZG verification and proof computation by reference (borrowed in the library's native type), not by value, clone or per-call copy. Check Lighthouse's kzg crate wrappers and verification helpers for blob clones or owned-blob arguments.

**Impact.** No 128 KiB blob copies on KZG verify or compute calls.

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/kzg/src/lib.rs:34`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/kzg/src/lib.rs#L34)
- [`crypto/kzg/src/lib.rs:97-216`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/kzg/src/lib.rs#L97-L216)
- [`beacon_node/beacon_chain/src/kzg_utils.rs:23-30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L23-L30)
- [`beacon_node/beacon_chain/src/kzg_utils.rs:230-243`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L230-L243)

**Skeptic check.** Every Kzg wrapper takes KzgBlobRef = &amp;[u8; BYTES_PER_BLOB], and the callers convert &amp;Blob to a reference with try_into. The remaining blob.clone() calls (blob_verification.rs:52 accessor, http_api block_id.rs:451) are not on KZG call paths. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#6990](https://github.com/Consensys-Incorporated/teku/pull/6990), [lighthouse#4405](https://github.com/sigp/lighthouse/pull/4405), [lighthouse#4694](https://github.com/sigp/lighthouse/pull/4694), [prysm#17039](https://github.com/OffchainLabs/prysm/pull/17039), [caplin#16826](https://github.com/erigontech/erigon/pull/16826), [lighthouse#4723](https://github.com/sigp/lighthouse/pull/4723), [lighthouse#8930](https://github.com/sigp/lighthouse/pull/8930), [lighthouse#6179](https://github.com/sigp/lighthouse/pull/6179), [caplin#13624](https://github.com/erigontech/erigon/pull/13624), [lighthouse#4852](https://github.com/sigp/lighthouse/pull/4852), [lighthouse#4818](https://github.com/sigp/lighthouse/pull/4818)

</details>


<a id="kzg-016"></a>
<details>
<summary><b>kzg-016</b> Wrap raw KZG bytes directly in SSZ commitment types — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Have the KZG interface return raw bytes that are wrapped directly in the SSZ commitment and proof types, with no intermediate wrapper type and conversion. Check whether Lighthouse converts KZG library commitment/proof types into its own types with a copy.

**Impact.** None. The SSZ commitment and proof types are the same 48-byte newtypes that the KZG wrapper returns.

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/kzg/src/lib.rs:159-165`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/kzg/src/lib.rs#L159-L165) blob_to_kzg_commitment wraps [u8;48] in KzgCommitment
- [`crypto/kzg/src/lib.rs:168-178`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/kzg/src/lib.rs#L168-L178) compute_kzg_proof wraps in KzgProof
- [`crypto/kzg/src/lib.rs:200-210`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/kzg/src/lib.rs#L200-L210) compute_cells_and_proofs maps proofs into KzgProof
- [`consensus/types/src/kzg_ext/mod.rs:3`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/kzg_ext/mod.rs#L3) the SSZ types re-export kzg::KzgCommitment/KzgProof

**Skeptic check.** Confirmed that types uses kzg::KzgCommitment/KzgProof directly, so there is no intermediate type. Cells are still copied into SSZ Cell via to_vec (kzg_utils.rs:522), but that is outside this idea's commitment/proof scope.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#8230](https://github.com/Consensys-Incorporated/teku/pull/8230)

</details>


<a id="kzg-017"></a>
<details>
<summary><b>kzg-017</b> Do not copy cell recovery results per worker — <i>not · low · S · memory, cpu</i></summary>

**Idea.** In parallel cell recovery, write each blob's ~268 KB cells-and-proofs result in place or move it, instead of copying it out of each worker. Check whether Lighthouse's reconstruction copies the per-blob cell/proof arrays when collecting results.

**Gap in Lighthouse.** Return Box'd results or write into a preallocated Vec&lt;MaybeUninit&gt;/per-blob slot via par_iter_mut in the reconstruction function (reconstruct_data_columns); the library return type still forces one copy.

**Impact.** Saves one or two 270 KB memcpys per blob during reconstruction: microseconds each, negligible against the recovery math (tens of ms).

**Best measured result.** pr:nimbus#8527: removes an extra ~270 KB copy per worker

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/kzg_utils.rs:907-923`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L907-L923) par_iter ... collect::&lt;Result&lt;Vec&lt;CellsAndKzgProofs&gt;&gt;&gt; returns each ~270 KB result by value
- [`crypto/kzg/src/lib.rs:307`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/kzg/src/lib.rs#L307) recover_cells_and_compute_kzg_proofs returns CellsAndKzgProofs by value, builds cell_ids.to_vec() and cells.to_vec()

**Sources.** [nimbus#8527](https://github.com/status-im/nimbus-eth2/pull/8527)

</details>


<a id="kzg-018"></a>
<details>
<summary><b>kzg-018</b> Flatten batch inputs into one preallocated buffer — <i>n/a · low · cpu, memory</i></summary>

**Idea.** Flatten blobs, commitments and proofs for a batch KZG call into one preallocated byte array with direct copies, instead of per-element buffers and copies. Check how Lighthouse builds the input slices for batch blob and cell verification.

**Impact.** Lighthouse passes &amp;[u8;N] refs into rust_eth_kzg, so Teku's per-element byte copying does not exist; only tiny pointer vectors are built per batch.

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/kzg/src/lib.rs:143-145`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/kzg/src/lib.rs#L143-L145) only pointer Vecs built; blob bytes never copied
- [`beacon_node/beacon_chain/src/kzg_utils.rs:237-240`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L237-L240) blobs passed as refs

**Sources.** [teku#7415](https://github.com/Consensys-Incorporated/teku/pull/7415)

</details>


<a id="kzg-019"></a>
<details>
<summary><b>kzg-019</b> Build batch verify vectors in a single pass — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** When batch-verifying data column cells, build the cells, proofs, indices and commitments vectors in one pass over the columns instead of cloning the iterator and iterating four times. Check Lighthouse's verify_cell_proof_batch caller.

**Impact.** None left. All three column validators fill the four vectors in one pass.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/kzg_utils.rs:55-114`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L55-L114) validate_full_data_columns single loop
- [`beacon_node/beacon_chain/src/kzg_utils.rs:120-162`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L120-L162) validate_data_columns_with_commitments single loop
- [`beacon_node/beacon_chain/src/kzg_utils.rs:170-228`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L170-L228) validate_partial_data_columns single loop

**Skeptic check.** All three callers of verify_cell_proof_batch (full, with-commitments, partial) use the one-pass pattern from PR 7326. Inside verify_cell_proof_batch the regrouping by column is a separate pass (lib.rs:249-258), but it is needed for the per-column parallel verification.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#7326](https://github.com/sigp/lighthouse/pull/7326)

</details>


<a id="kzg-020"></a>
<details>
<summary><b>kzg-020</b> Fewer allocations and clones in blob verification — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** In KZG blob verification allocate one vector instead of two and drop an unneeded clone. Check Lighthouse's validate_blobs helper for redundant allocations.

**Impact.** Trivial residual only: verify_kzg_for_blob_list, validate_blobs and Kzg::verify_blob_kzg_proof_batch (lib.rs:142) each build a small Vec of pointers.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/blob_verification.rs:100-115`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/blob_verification.rs#L100-L115) KzgVerifiedBlobList::new builds the KzgVerifiedBlob vec once and verifies through refs
- [`beacon_node/beacon_chain/src/blob_verification.rs:34-40`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/blob_verification.rs#L34-L40) KzgVerifiedBlob::new takes the Arc by value
- [`beacon_node/beacon_chain/src/kzg_utils.rs:231-243`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L231-L243) validate_blobs

**Skeptic check.** The PR 6282 change (one Vec, no sidecar clone) is present in blob_verification.rs. The earlier evidence pointed at kzg_utils, not at the changed file, but the conclusion holds.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#6282](https://github.com/sigp/lighthouse/pull/6282)

</details>


<a id="kzg-021"></a>
<details>
<summary><b>kzg-021</b> Box large blob values in KZG helpers — <i>n/a · low · memory</i></summary>

**Idea.** Box large blob values returned from KZG helpers instead of returning them by value, so stack frames stay small. Check Lighthouse's KZG helper return types for large unboxed arrays.

**Impact.** KZG helpers use references (rust_eth_kzg); no large Blob is returned by value, the old Box::new site is gone.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/kzg_utils.rs:23-29`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L23-L29) ssz_blob_to_kzg_blob_ref returns a reference
- kzg_utils.rs:246-262 helpers take &amp;Blob, return only commitments/proofs

**Sources.** [lighthouse#6343](https://github.com/sigp/lighthouse/pull/6343)

</details>


<a id="kzg-022"></a>
<details>
<summary><b>kzg-022</b> Verify a data column&#x27;s KZG proofs only once — <i>implemented · medium · S · cpu</i></summary>

**Idea.** Verify data column KZG proofs once at each entry point (gossip, req/resp) and do not re-verify them later on the import path. Check whether Lighthouse's KzgVerified types are re-verified anywhere after gossip or RPC verification.

**Impact.** Columns are verified once at each entry point: gossip, RPC custody, chain segment, backfill. Verified types are stored and not checked again.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker.rs:350-372`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L350-L372)
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:639-666`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L639-L666)
- [`beacon_node/beacon_chain/src/block_verification.rs:703-712`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L703-L712)
- [`beacon_node/beacon_chain/src/block_verification.rs:1395-1418`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1395-L1418)
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:666-677`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L666-L677)

**Skeptic check.** Gossip and RPC columns enter the DA cache as KzgVerified types. process_chain_segment verifies each block's columns once and wraps them as Available SignatureVerifiedBlock, so the RangeSyncBlock impl at 1412 is not reached on that path. The sync layer does no earlier KZG check. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#7301](https://github.com/status-im/nimbus-eth2/pull/7301), [nimbus#8464](https://github.com/status-im/nimbus-eth2/pull/8464), [lodestar#6066](https://github.com/ChainSafe/lodestar/pull/6066)

</details>


<a id="kzg-023"></a>
<details>
<summary><b>kzg-023</b> Skip KZG verification for EL-sourced or locally built data — <i>implemented · high · S · cpu, latency</i></summary>

**Idea.** Skip KZG proof verification for blobs and columns from the local execution client (getBlobs) and for sidecars built locally during block production, since the EL already verified them on mempool entry. Check Lighthouse's getBlobs and block production paths for KZG verification calls.

**Impact.** getBlobs v2/v3/v4 columns and locally published columns (Fulu block and Gloas envelope) skip KZG proof verification.

**Best measured result.** pr:prysm#14671: check can cost more than 20 ms

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:627`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L627)
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:704`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L704)
- [`beacon_node/http_api/src/publish_blocks.rs:462-489`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L462-L489)
- [`beacon_node/http_api/src/beacon/execution_payload_envelopes.rs:567`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/execution_payload_envelopes.rs#L567)
- [`beacon_node/beacon_chain/src/data_column_verification.rs:395-420`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L395-L420)

**Skeptic check.** fetch_blobs wraps columns built from EL responses with from_execution_verified. new_for_block_publishing checks only the commitment count, both in publish_blocks and in the Gloas envelope publish. No getBlobsV1 path remains. Earlier evidence correct and complete.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#7771](https://github.com/sigp/lighthouse/pull/7771), [lighthouse#7713](https://github.com/sigp/lighthouse/pull/7713), [prysm#14671](https://github.com/OffchainLabs/prysm/pull/14671)

</details>


<a id="kzg-024"></a>
<details>
<summary><b>kzg-024</b> Take cell proofs from the execution client — <i>partial · high · S · cpu, latency</i></summary>

**Idea.** Use the cell proofs returned by engine_getPayloadV5 and getBlobsV2 to build data column sidecars instead of computing KZG cell proofs in the beacon node. Check Lighthouse block production and getBlobs handling for compute_cells_and_proofs calls.

**Gap in Lighthouse.** Gloas self-built proposals: produce_block (block_production/gloas.rs) discards the EL cell proofs when caching the envelope in pending_payload_envelopes; when the VC publishes the signed envelope without blob data (the default Lighthouse VC Fetch flow), publish_execution_payload_envelope -&gt; build_gloas_data_columns -&gt; blobs_to_data_column_sidecars_gloas recomputes all cell proofs with compute_cells_and_proofs. Store kzg_proofs in PendingEnvelopeData and call blobs_to_data_column_sidecars_gloas_with_proofs. builder.rs:1503 build_data_columns_from_blobs also computes proofs, but only once at checkpoint-sync startup.

**Impact.** Fulu (mainnet) reuses EL proofs on every path. On Gloas every locally built proposal with blobs pays full cell-proof MSMs (expensive, on the proposal critical path before columns go out) that the EL already supplied.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/kzg_utils.rs:288`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L288) blobs_to_data_column_sidecars uses compute_cells_with_provided_proofs (Fulu block publish, block_verification.rs:827)
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:686`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L686) getBlobsV2 proofs passed to blobs_to_partial_data_columns
- [`beacon_node/http_api/src/publish_blocks.rs:449`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L449) build_data_columns with EL proofs
- [`beacon_node/beacon_chain/src/block_production/gloas.rs:917-923`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/gloas.rs#L917-L923) kzg_proofs from the payload are not stored in PendingEnvelopeData (only blobs)
- [`beacon_node/beacon_chain/src/pending_payload_envelopes.rs:13`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_envelopes.rs#L13) PendingEnvelopeData has blobs but no proofs
- [`beacon_node/http_api/src/beacon/execution_payload_envelopes.rs:225-230`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/execution_payload_envelopes.rs#L225-L230) EnvelopeOnly path takes cached blobs with proofs = None
- [`beacon_node/http_api/src/beacon/execution_payload_envelopes.rs:546`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/execution_payload_envelopes.rs#L546) None -&gt; blobs_to_data_column_sidecars_gloas
- [`beacon_node/beacon_chain/src/kzg_utils.rs:352`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L352) blobs_to_data_column_sidecars_gloas calls kzg.compute_cells_and_proofs per blob
- [`validator_client/validator_services/src/block_service.rs:1004`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/block_service.rs#L1004) Lighthouse VC Fetch path posts envelope-only (post_beacon_execution_payload_envelopes_ssz)

**Skeptic check.** Fulu block publish, getBlobsV2 and the stateless envelope path reuse EL proofs as the earlier evidence said. The earlier check missed the Gloas envelope-only publish path: there the proofs are dropped at the pending-envelope cache and recomputed.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lighthouse#7117](https://github.com/sigp/lighthouse/pull/7117), [lodestar#7686](https://github.com/ChainSafe/lodestar/pull/7686), [grandine@0e3ef89ef](https://github.com/grandinetech/grandine/commit/0e3ef89ef656), [grandine#228](https://github.com/grandinetech/grandine/pull/228)

</details>


<a id="kzg-025"></a>
<details>
<summary><b>kzg-025</b> Load the KZG trusted setup lazily and once — <i>partial · low · S · startup, memory, cpu</i></summary>

**Idea.** Load the KZG trusted setup only when a fork that needs it is scheduled or on first use, and share one loaded instance instead of loading per instance or test. Check where Lighthouse constructs its Kzg context and whether it is shared via Arc and skipped pre-Deneb.

**Gap in Lighthouse.** Setup is still always loaded even pre-Deneb (no_precomp variant), and some tests (kzg_utils.rs get_kzg, execution_block_generator.rs load_kzg) build their own Kzg instead of the shared LazyLock; route them to the test_utils statics and skip loading when Deneb is not scheduled.

**Impact.** Mainnet node startup unchanged (loaded once); only test time and negligible startup savings.

**Best measured result.** pr:lighthouse#5555: das-branch tests 990 s -&gt; 269 s

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/client/src/builder.rs:233`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L233) setup loaded once at startup; precomp only when is_peer_das_scheduled
- [`beacon_node/beacon_chain/src/test_utils.rs:121`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/test_utils.rs#L121) static LazyLock&lt;Arc&lt;Kzg&gt;&gt; shared in tests
- [`beacon_node/beacon_chain/src/kzg_utils.rs:1323`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L1323) unit test get_kzg builds a fresh Kzg with precomp per call
- [`beacon_node/beacon_chain/src/kzg_utils.rs:1568`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L1568) / lib.rs tests load_kzg() per test

**Sources.** [nimbus#7665](https://github.com/status-im/nimbus-eth2/pull/7665), [prysm#12803](https://github.com/OffchainLabs/prysm/pull/12803), [lodestar#4956](https://github.com/ChainSafe/lodestar/pull/4956), [lighthouse#5555](https://github.com/sigp/lighthouse/pull/5555), [grandine@81d2463d7](https://github.com/grandinetech/grandine/commit/81d2463d7348)

</details>


<a id="kzg-026"></a>
<details>
<summary><b>kzg-026</b> Embed the trusted setup in the binary — <i>implemented · low · S · startup</i></summary>

**Idea.** Embed the KZG trusted setup in the binary and load it from memory instead of reading a file at startup. Check whether Lighthouse uses include_bytes for the trusted setup.

**Impact.** Startup only; the setup is embedded and no file is read by default.

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/kzg/src/trusted_setup.rs:12`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/kzg/src/trusted_setup.rs#L12) include_bytes!("../trusted_setup.json")
- [`common/eth2_network_config/src/lib.rs:106`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2_network_config/src/lib.rs#L106) get_trusted_setup()
- [`beacon_node/src/config.rs:383-388`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/config.rs#L383-L388) a file is read only with --trusted-setup-file-override
- [`beacon_node/client/src/builder.rs:235`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L235) Kzg::new_from_trusted_setup

**Skeptic check.** Confirmed that the default path uses the embedded bytes; a file is read only with the override flag. The setup is still JSON hex parsed at startup, but this idea asks only about embedding it.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#3851](https://github.com/sigp/lighthouse/pull/3851)

</details>


<a id="kzg-027"></a>
<details>
<summary><b>kzg-027</b> Ship precomputed G1 monomial points in the setup — <i>implemented · low · S · startup, cpu</i></summary>

**Idea.** Ship the full trusted setup including G1 monomial points so the KZG library does not recompute them at startup. Check whether Lighthouse's embedded setup includes the monomial form.

**Impact.** None. The monomial points are shipped and loaded, not recomputed.

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/kzg/trusted_setup.json:2`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/kzg/trusted_setup.json#L2) g1_monomial present
- [`crypto/kzg/src/trusted_setup.rs:35-39`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/kzg/src/trusted_setup.rs#L35-L39) TrustedSetup carries g1_monomial, g1_lagrange, g2_monomial
- [`crypto/kzg/src/lib.rs:75-89`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/kzg/src/lib.rs#L75-L89) new_from_trusted_setup passes it to DASContext

**Skeptic check.** Checked that the embedded JSON contains g1_monomial and that the loader keeps it. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#6117](https://github.com/sigp/lighthouse/pull/6117)

</details>


<a id="kzg-028"></a>
<details>
<summary><b>kzg-028</b> Skip subgroup checks on the constant trusted setup — <i>not · low · S · startup</i></summary>

**Idea.** Skip subgroup checks on the fixed, known trusted setup points when initializing the KZG context, since the input is constant. Check the Lighthouse KZG context constructor for unchecked point deserialization.

**Gap in Lighthouse.** In load_trusted_setup use PeerDASTrustedSetup::from_json_unchecked for the embedded constant setup, keeping the checked path for a user-supplied setup file.

**Impact.** Skips subgroup checks on 4096 G1 + 65 G2 points at every start, roughly hundreds of ms; startup only.

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/kzg/src/trusted_setup.rs:159-163`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/kzg/src/trusted_setup.rs#L159-L163) load_trusted_setup uses PeerDASTrustedSetup::from_json
- ekzg-trusted-setup-0.9.1/src/lib.rs:112-115 from_json -&gt; to_trusted_setup with SubgroupCheck::Check
- same file:120 from_json_unchecked exists

**Sources.** [lighthouse#6118](https://github.com/sigp/lighthouse/pull/6118)

</details>


<a id="kzg-029"></a>
<details>
<summary><b>kzg-029</b> Read setup points directly into library buffers — <i>n/a · low · memory, startup, cpu</i></summary>

**Idea.** Read trusted setup G1 and G2 points directly into the buffers passed to the KZG library, with no intermediate copies or re-encoding. Check how Lighthouse parses its trusted setup before handing it to the library.

**Impact.** The Teku issue is JNI buffer copying around c-kzg; Lighthouse has no foreign-buffer boundary and parses once at startup.

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/kzg/src/trusted_setup.rs:159-163`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/kzg/src/trusted_setup.rs#L159-L163) JSON handed to rust_eth_kzg, which decodes into point arrays (ekzg-trusted-setup-0.9.1/src/lib.rs:41-47)

**Sources.** [teku#6790](https://github.com/Consensys-Incorporated/teku/pull/6790)

</details>


<a id="kzg-030"></a>
<details>
<summary><b>kzg-030</b> Compute cells without proofs for column reconstruction — <i>partial · low · M · cpu</i></summary>

**Idea.** When only extended cells are needed (column reconstruction), call compute_cells instead of compute_cells_and_kzg_proofs to skip proof generation. Check Lighthouse's reconstruction path for the KZG call it uses.

**Gap in Lighthouse.** On the HTTP blob path (reconstruct_blobs_with_indices, used by get_blobs / get_blob_sidecars), a node with fewer than 128 columns (semi-supernode) computes 128 KZG proofs per blob and throws them away. A cells-only recover (recover_polynomial_coeff + FFT, as in ekzg-erasure-codes recover_polynomial_coefficient) would skip the multi-opening proofs. This needs an upstream rust_eth_kzg API or a local wrapper. The loop is also sequential (into_iter).

**Impact.** Column reconstruction itself needs the proofs, so gossip and import are already optimal. The waste is only on the blobs API of non-supernodes. That load comes from L2s and indexers, not from consensus duties.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/kzg_utils.rs:409`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L409) and :449 kzg.compute_cells (no proofs) where EL supplies proofs
- [`beacon_node/beacon_chain/src/kzg_utils.rs:921`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L921) reconstruct_data_columns needs proofs for sidecars (correctly uses recover_cells_and_compute_kzg_proofs)
- [`beacon_node/beacon_chain/src/kzg_utils.rs:797-806`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L797-L806) reconstruct_blobs_with_indices calls recover_cells_and_compute_kzg_proofs and discards _kzg_proofs, taking only the first 64 cells
- [`beacon_node/http_api/src/block_id.rs:371`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L371) and :437 blob_sidecars / blobs API use this reconstruction
- [`beacon_node/http_api/src/block_id.rs:513-521`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L513-L521) semi-supernodes with 64 columns hit the recovery branch
- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/rust_eth_kzg-0.9.1/src/prover.rs:156-170 recover is polynomial recovery then compute_multi_opening_proofs; no proofless recover exposed

**Skeptic check.** Confirmed that compute_cells is used wherever proofs are known and that column reconstruction needs proofs. The earlier gap note found the API waste but still called it implemented. It is a real proof computation that is thrown away on an API path, so the verdict is partial with low value.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lighthouse#7020](https://github.com/sigp/lighthouse/pull/7020)

</details>


<a id="kzg-031"></a>
<details>
<summary><b>kzg-031</b> Single combined recover-cells-and-proofs library call — <i>implemented · low · S · cpu</i></summary>

**Idea.** Recover cells and proofs with the library's single combined call instead of recovering cells, converting to a blob and recomputing cells and proofs. Check Lighthouse's reconstruction for a recover-then-recompute sequence.

**Impact.** There is no recover, then blob, then recompute sequence. Reconstruction uses the single combined call.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/kzg_utils.rs:907-921`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L907-L921) reconstruct_data_columns calls kzg.recover_cells_and_compute_kzg_proofs once per blob (par_iter)
- [`beacon_node/beacon_chain/src/kzg_utils.rs:921-935`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L921-L935) sidecars built directly from recovered cells and proofs, no blob round-trip
- [`crypto/kzg/src/lib.rs:307`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/kzg/src/lib.rs#L307) wrapper over rust_eth_kzg recover_cells_and_kzg_proofs

**Skeptic check.** Verified that reconstruct_data_columns makes one combined call per row and builds sidecars from its output. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#14183](https://github.com/OffchainLabs/prysm/pull/14183)

</details>


<a id="kzg-032"></a>
<details>
<summary><b>kzg-032</b> Sort matrix entries by blob row before building cells — <i>n/a · low · S · cpu</i></summary>

**Idea.** Group and sort data column matrix entries by blob row before building cells and proofs or recovering, so construction is one pass over ordered entries instead of map lookups. Check how Lighthouse groups cells per blob before reconstruction.

**Impact.** Lighthouse already stores data columns indexed by blob row (column.get(row_index)), so there is no map lookup to remove; sort is once per call on at most 128 entries.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/kzg_utils.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs):~895 reconstruct_data_columns sorts columns by index once then per-row gather cells (par_iter)
- kzg_utils.rs:~775 reconstruct_blobs_with_indices same

**Sources.** [grandine#330](https://github.com/grandinetech/grandine/pull/330)

</details>


<a id="kzg-033"></a>
<details>
<summary><b>kzg-033</b> Benchmark KZG column verification with fixtures — <i>not · low · S · cpu</i></summary>

**Idea.** Add a benchmark with fixture data for data column KZG verification and batching so regressions and backend choices are measured. Check whether Lighthouse has a benchmark for column KZG verification.

**Gap in Lighthouse.** Add a criterion bench in crypto/kzg/benches calling Kzg::verify_cell_proof_batch with fixture cells (e.g. 128 columns x N blobs, and a few columns) to measure the per-column-group rayon path.

**Impact.** No runtime change; enables measuring column verification regressions and chunking choices.

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/kzg/benches/benchmark.rs:5-24`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/kzg/benches/benchmark.rs#L5-L24) only bench_init_context
- [`beacon_node/beacon_chain/benches/benches.rs:65`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/benches/benches.rs#L65) only reconstruct_N bench
- [`crypto/kzg/src/lib.rs:222`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/kzg/src/lib.rs#L222) verify_cell_proof_batch has no bench

**Sources.** [silver#203](https://github.com/gattaca-com/silver/pull/203)

</details>


<a id="kzg-034"></a>
<details>
<summary><b>kzg-034</b> Pre-generated blob bundles in tests — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Ship a pre-generated test blobs bundle (blobs, commitments, proofs) instead of computing KZG commitments and proofs in tests and mock builders. Check Lighthouse's test utilities and mock EL for KZG computation at runtime.

**Impact.** Test-only. The mock EL serves pre-generated commitments, proofs and cells, so it does no runtime KZG work.

**Best measured result.** pr:lighthouse#4829: get_header 550 ms -&gt; 50-55 ms; test 50 s -&gt; 10 s

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/test_utils/execution_block_generator.rs:38-42`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/test_utils/execution_block_generator.rs#L38-L42) include_bytes! test_blobs_bundle.ssz, _v2.ssz, _v2_cells.ssz
- [`beacon_node/execution_layer/src/test_utils/execution_block_generator.rs:1024-1045`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/test_utils/execution_block_generator.rs#L1024-L1045) generate_blobs copies the pre-generated bundle
- [`beacon_node/execution_layer/src/test_utils/execution_block_generator.rs:1240`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/test_utils/execution_block_generator.rs#L1240),1273 compute_cells only in validation tests

**Skeptic check.** Confirmed that the mock EL loads the fixtures and does not compute commitments or proofs at runtime. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#4829](https://github.com/sigp/lighthouse/pull/4829)

</details>


<a id="kzg-035"></a>
<details>
<summary><b>kzg-035</b> Stack buffer for the versioned hash — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** Compute the KZG versioned hash from a single stack buffer, with no heap slice allocation and append. Check Lighthouse's kzg_commitment_to_versioned_hash for allocations.

**Impact.** None. The function is allocation free.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/deneb.rs:4-8`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/deneb.rs#L4-L8) kzg_commitment_to_versioned_hash uses hash_fixed and an in-place version byte
- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ethereum_hashing-0.8.0/src/lib.rs:31 hash_fixed returns [u8;32]

**Skeptic check.** The function hashes the 48-byte commitment into a stack array and overwrites byte 0, with no heap use. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#18850](https://github.com/erigontech/erigon/pull/18850)

</details>


<a id="kzg-036"></a>
<details>
<summary><b>kzg-036</b> Correctly sized preallocation for KZG proof lists — <i>n/a · low · S · memory</i></summary>

**Idea.** Size preallocated KZG proof buffers by the number of proofs, not bytes times proofs. Check Lighthouse's Vec::with_capacity calls around KZG proof lists.

**Impact.** None; capacities are already count-based, no byte-size multiplication.

**Best measured result.** pr:prysm#15809: preallocation was 48x too large

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/kzg_utils.rs:511`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L511) capacity max_blobs_per_block per column
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:551`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L551) capacity num_blobs
- [`beacon_node/beacon_chain/src/pending_payload_cache/pending_column.rs:59`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/pending_column.rs#L59),94 capacity cell count

**Sources.** [prysm#15809](https://github.com/OffchainLabs/prysm/pull/15809)

</details>


<a id="kzg-037"></a>
<details>
<summary><b>kzg-037</b> Compute blob byte size from count, not by streaming — <i>n/a · low · S · cpu, memory</i></summary>

**Idea.** Compute the total byte size of blobs as count times the fixed blob size instead of streaming over every blob's bytes. Check Lighthouse for size computations that iterate over blob contents.

**Impact.** Sizes are constants from fixed-size types; no streaming size computation exists.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/core/eth_spec.rs:328`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/core/eth_spec.rs#L328) bytes_per_blob() is a typenum constant
- grep found no code iterating blob bytes to compute size

**Sources.** [teku#7256](https://github.com/Consensys-Incorporated/teku/pull/7256)

</details>


<a id="kzg-038"></a>
<details>
<summary><b>kzg-038</b> Pass cell indices as native integers — <i>implemented · low · S · cpu</i></summary>

**Idea.** Pass cell indices to the KZG library as native integers instead of converting each to a big integer type. Check the type of cell indices Lighthouse passes to verify_cell_kzg_proof_batch.

**Impact.** None. The indices stay native u64 all the way into rust_eth_kzg.

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/kzg/src/lib.rs:214-220`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/kzg/src/lib.rs#L214-L220) verify_cell_proof_batch takes indices: Vec&lt;CellIndex&gt; (u64)
- [`crypto/kzg/src/lib.rs:282-287`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/kzg/src/lib.rs#L282-L287) passes &amp;vec![column_index; n]
- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/rust_eth_kzg-0.9.1/src/verifier.rs:72-78 cell_indices: &amp;[CellIndex]

**Skeptic check.** Confirmed that the native u64 indices go into the Rust library with no bigint step (that problem was specific to Lodestar's JS binding). Only a small vec![column_index; n] is allocated per column group.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#8131](https://github.com/ChainSafe/lodestar/pull/8131)

</details>


<a id="kzg-039"></a>
<details>
<summary><b>kzg-039</b> Drop length checks the KZG library already does — <i>partial · low · S · cpu</i></summary>

**Idea.** Remove length checks before batch KZG proof verification that the library already performs. Check Lighthouse's KZG wrappers for duplicated input validation.

**Gap in Lighthouse.** Per-column length checks in validate_*_data_columns (needed for attributing errors) and the check in Kzg::verify_cell_proof_batch duplicate rust_eth_kzg's validation; the latter is kept deliberately for ef tests. Removing would only save a few comparisons.

**Impact.** Negligible: a handful of integer compares per batch.

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/kzg/src/lib.rs:238-247`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/kzg/src/lib.rs#L238-L247) length check on proofs/indices/commitments
- [`beacon_node/beacon_chain/src/kzg_utils.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs):~100,160,225 per-column repeated length checks before the call

**Sources.** [nimbus#5744](https://github.com/status-im/nimbus-eth2/pull/5744)

</details>


<a id="kzg-040"></a>
<details>
<summary><b>kzg-040</b> Single-blob KZG verify for one-blob paths — <i>n/a · low · S · cpu, latency</i></summary>

**Idea.** Verify a single gossip or RPC blob with the single-proof KZG API instead of going through the batch API. Check which KZG function Lighthouse calls for a single gossip blob sidecar.

**Impact.** None on live paths: this checkout no longer has a gossip BlobSidecar path (no BlobSidecar handling in network_beacon_processor or gossip topics); the remaining blob paths are whole-block RPC/range-sync verifications that use the batch API by design, and data columns use cell batch proofs.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/blob_verification.rs:33-40`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/blob_verification.rs#L33-L40) KzgVerifiedBlob::new -&gt; verify_kzg_for_blob (only caller: [`testing/ef_tests/src/cases/fork_choice.rs:905`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/testing/ef_tests/src/cases/fork_choice.rs#L905))
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:475-485`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L475-L485) verify_kzg_for_available_block -&gt; verify_kzg_for_blob_list (batch)
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:495-525`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L495-L525) batch_verify_kzg_for_range_sync_blocks -&gt; verify_kzg_for_blob_list
- [`beacon_node/beacon_chain/src/kzg_utils.rs:229-241`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L229-L241) validate_blobs -&gt; verify_blob_kzg_proof_batch

**Skeptic check.** validate_blob does call the single-proof API, but its only caller KzgVerifiedBlob::new is used only by ef_tests; the earlier claim that gossip single blobs use it is wrong because gossip blob processing is gone. With no single-blob hot path left, the idea does not apply.

**Verdict history.** implemented (checked) → n/a (skeptic)

**Sources.** [teku#7646](https://github.com/Consensys-Incorporated/teku/pull/7646)

</details>


<a id="kzg-041"></a>
<details>
<summary><b>kzg-041</b> Disable KZG library internal multithreading — <i>implemented · medium · S · cpu</i></summary>

**Idea.** Configure the KZG library to run single-threaded and let the client's own thread pool parallelize, since nested library and client rayon pools conflict. Check the threading mode Lighthouse passes when creating the rust-eth-kzg context.

**Impact.** The library runs single-threaded and Lighthouse's rayon pool parallelises per blob, so there are no nested pools.

**Best measured result.** pr:lighthouse#6309: ~20% faster single-threaded (unconfirmed)

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.toml:224 rust_eth_kzg = "0.9" with no features
- [`crypto/kzg/Cargo.toml:22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/kzg/Cargo.toml#L22) workspace dep, no features
- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/rust_eth_kzg-0.9.1/Cargo.toml:30-35 multithreaded is opt-in (pulls rayon)
- Cargo.lock:8626 rust_eth_kzg 0.9.1 dependency list has no rayon, so multithreaded is not enabled by any crate
- [`beacon_node/beacon_chain/src/kzg_utils.rs:907`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L907) Lighthouse parallelises per blob with its own rayon par_iter

**Skeptic check.** Cargo.lock confirms that no crate enables the rayon-backed multithreaded feature through feature unification. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#6309](https://github.com/sigp/lighthouse/pull/6309)

</details>


<a id="kzg-042"></a>
<details>
<summary><b>kzg-042</b> Reuse cells computed during blob verification for column building — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** When blobs are KZG-verified before building data columns (e.g. publishing a block with supplied blobs), keep the cells computed during verification and reuse them for column construction instead of recomputing them. Check whether Lighthouse's block publish path recomputes cells after verifying blobs.

**Impact.** Cells are computed once on the publish path; there is no verify-then-recompute to remove.

**Best measured result.** None (pr:caplin#24404)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/publish_blocks.rs:456-485`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L456-L485) build_data_columns does not KZG-verify supplied blobs (EL verified them)
- [`beacon_node/beacon_chain/src/kzg_utils.rs:306`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L306) compute_cells_with_provided_proofs computes cells once with the supplied proofs
- [`beacon_node/beacon_chain/src/data_column_verification.rs:395`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L395) new_for_block_publishing does no KZG verification

**Skeptic check.** Verified the publish path computes cells a single time with no prior blob verification pass. The idea's premise (verify then rebuild) does not occur in Lighthouse.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#24404](https://github.com/erigontech/erigon/pull/24404)

</details>


<a id="kzg-043"></a>
<details>
<summary><b>kzg-043</b> Parse trusted setup from text without binary conversion — <i>implemented · low · S · startup</i></summary>

**Idea.** Load the KZG trusted setup directly from its published text format at startup instead of first converting it to a binary file and loading that. Check whether Lighthouse has a text-to-binary conversion step in its trusted setup loading.

**Impact.** Startup only; there is no text-to-binary conversion step.

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/kzg/src/trusted_setup.rs:12`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/kzg/src/trusted_setup.rs#L12) TRUSTED_SETUP_BYTES is include_bytes of trusted_setup.json
- [`crypto/kzg/src/trusted_setup.rs:80-100`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/kzg/src/trusted_setup.rs#L80-L100) serde hex parsing of points straight from JSON
- [`crypto/kzg/src/lib.rs:68-83`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/kzg/src/lib.rs#L68-L83) load_trusted_setup feeds DASContext directly

**Skeptic check.** Verified the trusted setup is parsed from embedded JSON text directly into rust_eth_kzg. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#5659](https://github.com/ChainSafe/lodestar/pull/5659)

</details>


