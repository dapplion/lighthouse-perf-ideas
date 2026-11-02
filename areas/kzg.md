# kzg

25 ideas: 5 not, 2 partial, 17 implemented, 1 n/a; 4 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

The area has 41 numbered ideas; the 16 ids missing here have not been checked against Lighthouse yet.

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [kzg-001](#kzg-001) | Keep the KZG library at its latest release | implemented | medium |  | cpu, startup |
| [kzg-002](#kzg-002) | Enable fixed-base precomputation tables in the KZG setup | implemented | high |  | cpu, memory, latency, startup |
| [kzg-003](#kzg-003) **★** | AVX-512 IFMA FFT for blob cell extension | not | medium | L | cpu, latency |
| [kzg-004](#kzg-004) **★** | AVX-512 IFMA MSM and pairing for cell batch verify | not | medium | L | cpu, latency |
| [kzg-005](#kzg-005) | Vectorized G1 point decompression and subgroup check | not | low | L | cpu |
| [kzg-006](#kzg-006) | Use the fastest available native KZG backend | implemented | low |  | cpu, latency |
| [kzg-007](#kzg-007) | Run KZG work off the async runtime or event loop | implemented | medium |  | cpu, latency |
| [kzg-008](#kzg-008) | Dedicated prioritized executor for cell computation and recovery | implemented | medium | S | latency, cpu |
| [kzg-009](#kzg-009) **★** | Batch KZG verify all columns of a block or segment | partial | medium | S | cpu, latency, sync |
| [kzg-010](#kzg-010) **★** | Drain queued gossip columns into one KZG batch | not | medium | M | cpu, latency |
| [kzg-011](#kzg-011) | Split KZG batch verification into parallel chunks | implemented | medium | S | cpu, latency, sync |
| [kzg-012](#kzg-012) | Verify each gossip column in parallel, no batch queue | implemented | low |  | cpu, latency |
| [kzg-013](#kzg-013) | Compute and recover cells per blob in parallel | implemented | medium | S | cpu, latency |
| [kzg-014](#kzg-014) | Zip per-blob inputs before the parallel iterator | implemented | low |  | cpu, latency |
| [kzg-015](#kzg-015) | Pass blobs by reference into KZG calls | implemented | low |  | cpu, memory |
| [kzg-017](#kzg-017) | Do not copy cell recovery results per worker | not | low | S | memory, cpu |
| [kzg-022](#kzg-022) | Verify a data column's KZG proofs only once | implemented | medium | S | cpu |
| [kzg-023](#kzg-023) | Skip KZG verification for EL-sourced or locally built data | implemented | high |  | cpu, latency |
| [kzg-024](#kzg-024) | Take cell proofs from the execution client | implemented | high |  | cpu, latency |
| [kzg-025](#kzg-025) | Load the KZG trusted setup lazily and once | partial | low | S | startup, memory, cpu |
| [kzg-030](#kzg-030) | Compute cells without proofs for column reconstruction | implemented | medium | S | cpu |
| [kzg-031](#kzg-031) | Single combined recover-cells-and-proofs library call | implemented | medium | S | cpu |
| [kzg-034](#kzg-034) | Pre-generated blob bundles in tests | implemented | low |  | cpu, latency |
| [kzg-036](#kzg-036) | Correctly sized preallocation for KZG proof lists | n/a | low | S | memory |
| [kzg-041](#kzg-041) | Disable KZG library internal multithreading | implemented | medium | S | cpu |

★ actionable. Click an id for the full record.

## Ideas

<a id="kzg-001"></a>
<details>
<summary><b>kzg-001</b> Keep the KZG library at its latest release — <i>implemented · medium · cpu, startup</i></summary>

**Idea.** Bump the KZG libraries (c-kzg-4844, rust-eth-kzg, jc-kzg, blst) to the newest release to pick up upstream speedups, including faster trusted-setup context load. Check the KZG crate versions in the Lighthouse Cargo.toml against the latest upstream release.

**Impact.** Versions are recent; I could not check against the newest upstream release offline.

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.toml:224 rust_eth_kzg = "0.9"; Cargo.lock rust_eth_kzg 0.9.1, c-kzg 2.1.8, blst 0.3.17
- Cargo.lock has been bumped repeatedly (registry holds c-kzg 2.1.5-2.1.8, blst 0.3.16-17)

**Sources.** [grandine#615](https://github.com/grandinetech/grandine/pull/615), [prysm#15708](https://github.com/OffchainLabs/prysm/pull/15708), [lighthouse#7870](https://github.com/sigp/lighthouse/pull/7870), [teku#10427](https://github.com/Consensys-Incorporated/teku/pull/10427), [lighthouse#6906](https://github.com/sigp/lighthouse/pull/6906)

</details>


<a id="kzg-002"></a>
<details>
<summary><b>kzg-002</b> Enable fixed-base precomputation tables in the KZG setup — <i>implemented · high · cpu, memory, latency, startup</i></summary>

**Idea.** Load the trusted setup with a nonzero fixed-base precompute window (7 to 9 bits, higher on supernodes) so the fixed-base MSMs in cell/proof computation and cell recovery run up to about 2x faster, at tens of MiB of memory. Check the precompute argument where Lighthouse initializes its KZG context, and whether it is larger on supernodes.

**Impact.** Already on: width 8 (about 48 MiB). Not raised on supernodes (9 would be a small extra gain), but main saving is taken.

**Best measured result.** pr:lighthouse#5795: table off doubles the time to compute cells and proofs (pr:nimbus#8405: about 1.6x faster at 48 MiB)

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/kzg/src/lib.rs:76`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/kzg/src/lib.rs#L76) new_from_trusted_setup uses UsePrecomp::Yes{width: RECOMMENDED_PRECOMP_WIDTH}
- ekzg-serialization-0.9.1/src/constants.rs:65 width = 8
- [`beacon_node/client/src/builder.rs:234`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L234) precomp used whenever PeerDAS is scheduled

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
<summary><b>kzg-006</b> Use the fastest available native KZG backend — <i>implemented · low · cpu, latency</i></summary>

**Idea.** Switch blob and cell KZG operations to a faster native library (C or optimized Rust, or a runtime-selectable alternative such as Constantine) instead of a slower implementation. Check which KZG backend Lighthouse uses for column construction and cell verification and compare it in benchmarks with the alternatives.

**Impact.** Already on rust-eth-kzg with fixed-base precomputation for cell and proof work.

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/kzg/src/lib.rs:63`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/kzg/src/lib.rs#L63) Kzg wraps rust_eth_kzg::DASContext
- [`crypto/kzg/src/lib.rs:76`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/kzg/src/lib.rs#L76) new_from_trusted_setup uses UsePrecomp::Yes
- [`beacon_node/client/src/builder.rs:233`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L233) precomp only when PeerDAS scheduled

**Sources.** [prysm#17313](https://github.com/OffchainLabs/prysm/pull/17313), [lighthouse#6212](https://github.com/sigp/lighthouse/pull/6212), [nimbus#4732](https://github.com/status-im/nimbus-eth2/pull/4732)

</details>


<a id="kzg-007"></a>
<details>
<summary><b>kzg-007</b> Run KZG work off the async runtime or event loop — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** Run KZG proof verification and cell computation on worker or blocking threads, not on the async runtime or main event loop, so networking, attestation production and other tasks are not stalled. Check whether every Lighthouse KZG call on the gossip and import paths runs via spawn_blocking or the beacon processor, not inline in an async task.

**Impact.** KZG work is off the async runtime on the main paths I read; blob and block-import paths not individually checked.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2457`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2457) verify_data_column_sidecar_for_gossip runs GossipVerifiedDataColumn::new in spawn_blocking_handle
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:671`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L671) cell computation in spawn_blocking_handle
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3811`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3811),3845 reconstruction via spawn_blocking_with_rayon_async
- [`beacon_node/http_api/src/publish_blocks.rs:443`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L443) build_data_sidecars in spawn_blocking_handle

**Sources.** [lodestar#7936](https://github.com/ChainSafe/lodestar/pull/7936), [lodestar#8234](https://github.com/ChainSafe/lodestar/pull/8234), [lodestar#7989](https://github.com/ChainSafe/lodestar/pull/7989), [nimbus#8810](https://github.com/status-im/nimbus-eth2/pull/8810), [grandine#421](https://github.com/grandinetech/grandine/pull/421)

</details>


<a id="kzg-008"></a>
<details>
<summary><b>kzg-008</b> Dedicated prioritized executor for cell computation and recovery — <i>implemented · medium · S · latency, cpu</i></summary>

**Idea.** Run cell computation and cell recovery on a dedicated executor apart from the shared thread pool, and give computation for the head block priority over background recovery, to cut tail latency under load. Check whether Lighthouse's KZG compute and reconstruction share the global rayon pool and whether recovery can delay head-block work.

**Gap in Lighthouse.** Only residual: the 80% recovery pool and the global pool oversubscribe cores at the OS level, so recovery can still steal CPU from head-block compute; no OS thread priority or hard core cap. Shrinking or lowering the pool is a tuning knob, not a missing mechanism.

**Impact.** Residual tail-latency gain is small; separation and prioritisation already exist.

**Best measured result.** pr:grandine#596: reduces p99 latency during high load (no number)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:3811`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3811),3845 cell recovery runs on RayonPoolType::HighPriority pool, the only BN user of that pool (others: builder.rs:1199, beacon_chain.rs:4827, beacon_processor lib.rs:1728 use LowPriority)
- [`common/task_executor/src/rayon_pool_provider.rs:13-21`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/task_executor/src/rayon_pool_provider.rs#L13-L21) dedicated pools separate from global; global reserved for critical work
- [`common/task_executor/src/lib.rs:218-236`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/task_executor/src/lib.rs#L218-L236) spawn_blocking_with_rayon installs the dedicated pool
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:671`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L671) head-block cell computation on spawn_blocking with the global rayon pool
- [`beacon_node/beacon_processor/src/lib.rs:950-953`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L950-L953) column_reconstruction_queue is popped only after gossip block, payload, data column queues
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:73`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L73),107,1140-1143 reconstruction delayed 150ms / until 1/4 slot so head-block work goes first

**Second check.** Beyond the earlier review, checked that the HighPriority pool is effectively dedicated to reconstruction in the BN, and found the beacon processor queue order plus the reprocess delay queue that defer recovery behind gossip block/column work, which is equivalent to Grandine #596 (dedicated executor, computation over recovery).

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

**Sources.** [ethlambda#754](https://github.com/lambdaclass/ethlambda/pull/754), [lighthouse#6851](https://github.com/sigp/lighthouse/pull/6851), [nimbus#8302](https://github.com/status-im/nimbus-eth2/pull/8302), [prysm#14559](https://github.com/OffchainLabs/prysm/pull/14559), [lighthouse#4934](https://github.com/sigp/lighthouse/pull/4934), [lighthouse#7582](https://github.com/sigp/lighthouse/pull/7582), [nimbus#8275](https://github.com/status-im/nimbus-eth2/pull/8275), [lighthouse#4903](https://github.com/sigp/lighthouse/pull/4903)

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

**Sources.** [prysm#15617](https://github.com/OffchainLabs/prysm/pull/15617), [prysm#15609](https://github.com/OffchainLabs/prysm/pull/15609), [silver#177](https://github.com/gattaca-com/silver/pull/177)

</details>


<a id="kzg-011"></a>
<details>
<summary><b>kzg-011</b> Split KZG batch verification into parallel chunks — <i>implemented · medium · S · cpu, latency, sync</i></summary>

**Idea.** Split large KZG cell-proof batch verifications into fixed-size chunks run across a thread pool, and on failure search for the first invalid column instead of re-verifying everything one by one. Check whether Lighthouse's range/backfill column verification is one single-threaded batch and how it handles a failed batch.

**Impact.** Already parallel across up to 128 column chunks with attributable early exit. Chunks are per column, not fixed size, so small batches (one block) parallelise less; see kzg-009.

**Best measured result.** pr:lighthouse#7921: invalid-column worst case 12.15 s before short-circuit; epoch batch 294 ms with rayon

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/kzg/src/lib.rs:261`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/kzg/src/lib.rs#L261) column_groups.into_par_iter() runs one verify_cell_kzg_proof_batch per column index on rayon
- [`crypto/kzg/src/lib.rs:293`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/kzg/src/lib.rs#L293) collect::&lt;Result&lt;_&gt;&gt; short-circuits on first error and the error carries the failing column index
- [`crypto/kzg/src/lib.rs:275`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/kzg/src/lib.rs#L275) per-chunk span

**Sources.** [lighthouse#7921](https://github.com/sigp/lighthouse/pull/7921), [prysm#16220](https://github.com/OffchainLabs/prysm/pull/16220)

</details>


<a id="kzg-012"></a>
<details>
<summary><b>kzg-012</b> Verify each gossip column in parallel, no batch queue — <i>implemented · low · cpu, latency</i></summary>

**Idea.** On gossip, verify each data column sidecar's KZG proofs immediately on its own core instead of waiting in a batch queue, which removes queue latency. Check whether Lighthouse gossip column verification waits for or is serialized behind other columns.

**Impact.** No batching queue on gossip; each column verifies on its own worker. Within one column verify_cell_proof_batch has a single group so uses one core, which is the same as the idea.

**Best measured result.** pr:prysm#16240: gossip verification 185 ms -&gt; 26 ms, DA wait 82.2 ms -&gt; 16.3 ms

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/mod.rs:214`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L214) each gossip column is its own Work item
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:711`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L711) verify_data_column_sidecar_for_gossip awaited per column
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1182`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1182) verify_kzg_for_data_column called inline, no batch queue

**Sources.** [prysm#16240](https://github.com/OffchainLabs/prysm/pull/16240)

</details>


<a id="kzg-013"></a>
<details>
<summary><b>kzg-013</b> Compute and recover cells per blob in parallel — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Compute cells and proofs, and recover missing cells, for each blob on its own thread (bounded by core count), because the per-blob work is independent and the KZG library is single-threaded. Check Lighthouse's blobs_to_data_column_sidecars and reconstruction for a parallel iterator over blobs.

**Gap in Lighthouse.** Only the HTTP API blob reconstruction (reconstruct_blobs_with_indices) is serial; changing its into_iter to into_par_iter is trivial but off the hot path.

**Impact.** Hot paths (column reconstruction, getBlobs column building) already parallel over blobs; the API path is rare.

**Best measured result.** pr:prysm#14804: DataColumnSidecars 2117 ms -&gt; 260 ms; RecoverCellsAndProofs 2180 ms -&gt; 254 ms

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/kzg_utils.rs:399`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L399) compute_cells_with_provided_proofs uses into_par_iter over blobs
- [`beacon_node/beacon_chain/src/kzg_utils.rs:449`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L449) blobs_to_partial_data_columns into_par_iter
- [`beacon_node/beacon_chain/src/kzg_utils.rs:475`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L475) compute_cells par over blobs
- [`beacon_node/beacon_chain/src/kzg_utils.rs:898`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L898) reconstruct_data_columns (0..num_of_blobs).into_par_iter() recover per blob
- [`beacon_node/beacon_chain/src/kzg_utils.rs:767`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L767) reconstruct_blobs_with_indices is a serial .into_iter() (HTTP API path only)

**Sources.** [nimbus#7286](https://github.com/status-im/nimbus-eth2/pull/7286), [lighthouse#5805](https://github.com/sigp/lighthouse/pull/5805), [prysm#14804](https://github.com/OffchainLabs/prysm/pull/14804), [caplin#25514](https://github.com/erigontech/erigon/pull/25514), [caplin#24861](https://github.com/erigontech/erigon/pull/24861)

</details>


<a id="kzg-014"></a>
<details>
<summary><b>kzg-014</b> Zip per-blob inputs before the parallel iterator — <i>implemented · low · cpu, latency</i></summary>

**Idea.** Zip blobs and their per-blob inputs into one indexed collection before calling par_iter for cell and proof computation, so rayon splits the work evenly. Check the iterator shape in Lighthouse's blobs_to_data_column_sidecars.

**Impact.** Even rayon splitting over blobs already in place.

**Best measured result.** pr:lighthouse#7574: about 10% faster, 12.04 ms -&gt; 10.72 ms

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/kzg_utils.rs:427`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L427) compute_cells_with_provided_proofs zips blobs with proof_chunks into a Vec before into_par_iter
- [`beacon_node/beacon_chain/src/kzg_utils.rs:344`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L344) blobs_to_data_column_sidecars_gloas uses indexed slice into_par_iter

**Sources.** [lighthouse#7574](https://github.com/sigp/lighthouse/pull/7574)

</details>


<a id="kzg-015"></a>
<details>
<summary><b>kzg-015</b> Pass blobs by reference into KZG calls — <i>implemented · low · cpu, memory</i></summary>

**Idea.** Pass 128 KiB blobs to KZG verification and proof computation by reference (borrowed in the library's native type), not by value, clone or per-call copy. Check Lighthouse's kzg crate wrappers and verification helpers for blob clones or owned-blob arguments.

**Gap in Lighthouse.** Remaining blob.clone() at blob_verification.rs:52 and kzg_utils.rs:1290 are outside KZG calls (accessors/tests).

**Impact.** No per-call 128 KiB copies on the verify or compute paths.

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/kzg/src/lib.rs:98-135`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/kzg/src/lib.rs#L98-L135) all KZG calls take KzgBlobRef (&amp;[u8;BYTES_PER_BLOB])
- [`crypto/kzg/src/lib.rs:141`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/kzg/src/lib.rs#L141) verify_blob_kzg_proof_batch builds Vec of references only
- [`beacon_node/beacon_chain/src/kzg_utils.rs:344`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L344) blobs passed as &amp;Blob and converted by try_into to ref

**Sources.** [teku#6990](https://github.com/Consensys-Incorporated/teku/pull/6990), [lighthouse#4405](https://github.com/sigp/lighthouse/pull/4405), [lighthouse#4694](https://github.com/sigp/lighthouse/pull/4694), [prysm#17039](https://github.com/OffchainLabs/prysm/pull/17039), [caplin#16826](https://github.com/erigontech/erigon/pull/16826), [lighthouse#4723](https://github.com/sigp/lighthouse/pull/4723), [lighthouse#8930](https://github.com/sigp/lighthouse/pull/8930), [lighthouse#6179](https://github.com/sigp/lighthouse/pull/6179), [caplin#13624](https://github.com/erigontech/erigon/pull/13624), [lighthouse#4852](https://github.com/sigp/lighthouse/pull/4852)

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


<a id="kzg-022"></a>
<details>
<summary><b>kzg-022</b> Verify a data column&#x27;s KZG proofs only once — <i>implemented · medium · S · cpu</i></summary>

**Idea.** Verify data column KZG proofs once at each entry point (gossip, req/resp) and do not re-verify them later on the import path. Check whether Lighthouse's KzgVerified types are re-verified anywhere after gossip or RPC verification.

**Impact.** No re-verification found after gossip/RPC verification. One possible overlap: process_chain_segment verifies columns at block_verification.rs:705 and the per-block RangeSyncBlock impl at line 1412 verifies again only on the non-segment path, so no double check seen.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker.rs:350`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L350) put_rpc_custody_columns verifies once, then stores KzgVerifiedCustodyDataColumn
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:394`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L394) put_gossip_verified_data_columns takes already verified types
- [`beacon_node/beacon_chain/src/block_verification.rs:1412`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1412) RangeSyncBlock import verifies, but LookupBlock (line 1441) and gossip/SignatureVerified paths do not
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:676`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L676) backfill verifies once

**Sources.** [nimbus#7301](https://github.com/status-im/nimbus-eth2/pull/7301)

</details>


<a id="kzg-023"></a>
<details>
<summary><b>kzg-023</b> Skip KZG verification for EL-sourced or locally built data — <i>implemented · high · cpu, latency</i></summary>

**Idea.** Skip KZG proof verification for blobs and columns from the local execution client (getBlobs) and for sidecars built locally during block production, since the EL already verified them on mempool entry. Check Lighthouse's getBlobs and block production paths for KZG verification calls.

**Impact.** Both EL-sourced columns and locally built columns skip KZG verification.

**Best measured result.** pr:prysm#14671: check can cost more than 20 ms

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs):~700 KzgVerifiedPartialDataColumn::from_execution_verified for getBlobs columns
- [`beacon_node/http_api/src/publish_blocks.rs:466-495`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L466-L495) build_data_columns uses new_for_block_publishing, no gossip/KZG verification, comment says EL verified

**Sources.** [lighthouse#7771](https://github.com/sigp/lighthouse/pull/7771), [lighthouse#7713](https://github.com/sigp/lighthouse/pull/7713), [prysm#14671](https://github.com/OffchainLabs/prysm/pull/14671)

</details>


<a id="kzg-024"></a>
<details>
<summary><b>kzg-024</b> Take cell proofs from the execution client — <i>implemented · high · cpu, latency</i></summary>

**Idea.** Use the cell proofs returned by engine_getPayloadV5 and getBlobsV2 to build data column sidecars instead of computing KZG cell proofs in the beacon node. Check Lighthouse block production and getBlobs handling for compute_cells_and_proofs calls.

**Impact.** Cell proofs from EL/getBlobsV2 are reused; only the cheap cell extension (FFT, no MSM) is computed locally. Proof computation is skipped.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/kzg_utils.rs:382`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L382) compute_cells_with_provided_proofs
- [`beacon_node/beacon_chain/src/kzg_utils.rs:362`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L362) blobs_to_data_column_sidecars_gloas_with_proofs
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs):~675 BlobAndProofV2 proofs passed to blobs_to_partial_data_columns
- [`beacon_node/http_api/src/publish_blocks.rs:449`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L449) proofs passed into build_data_columns

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

**Sources.** [nimbus#7665](https://github.com/status-im/nimbus-eth2/pull/7665), [prysm#12803](https://github.com/OffchainLabs/prysm/pull/12803), [lodestar#4956](https://github.com/ChainSafe/lodestar/pull/4956), [lighthouse#5555](https://github.com/sigp/lighthouse/pull/5555)

</details>


<a id="kzg-030"></a>
<details>
<summary><b>kzg-030</b> Compute cells without proofs for column reconstruction — <i>implemented · medium · S · cpu</i></summary>

**Idea.** When only extended cells are needed (column reconstruction), call compute_cells instead of compute_cells_and_kzg_proofs to skip proof generation. Check Lighthouse's reconstruction path for the KZG call it uses.

**Gap in Lighthouse.** Column reconstruction must produce proofs for the sidecars, so proofless recovery does not apply there; the HTTP blob path (kzg_utils.rs:800) pays for proofs it discards but the library has no cells-only recover.

**Impact.** Proofless compute_cells is used wherever proofs are known; nothing left to gain on mainnet paths.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/kzg_utils.rs:399`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L399) and :449 use kzg.compute_cells (no proofs) where proofs are supplied by the EL
- [`beacon_node/beacon_chain/src/kzg_utils.rs:898`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L898) reconstruct_data_columns uses recover_cells_and_compute_kzg_proofs because reconstructed sidecars need proofs
- ~/.cargo/registry/src/*/rust_eth_kzg-0.9.1/src/prover.rs:156 only offers recover_cells_and_kzg_proofs, no cells-only recover

**Sources.** [lighthouse#7020](https://github.com/sigp/lighthouse/pull/7020)

</details>


<a id="kzg-031"></a>
<details>
<summary><b>kzg-031</b> Single combined recover-cells-and-proofs library call — <i>implemented · medium · S · cpu</i></summary>

**Idea.** Recover cells and proofs with the library's single combined call instead of recovering cells, converting to a blob and recomputing cells and proofs. Check Lighthouse's reconstruction for a recover-then-recompute sequence.

**Impact.** Single combined call already used; no recover-then-recompute sequence.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/kzg_utils.rs:898-921`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L898-L921) reconstruct_data_columns calls kzg.recover_cells_and_compute_kzg_proofs once per blob
- [`crypto/kzg/src/lib.rs:307`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/kzg/src/lib.rs#L307) wrapper over rust_eth_kzg recover_cells_and_kzg_proofs

**Sources.** [prysm#14183](https://github.com/OffchainLabs/prysm/pull/14183)

</details>


<a id="kzg-034"></a>
<details>
<summary><b>kzg-034</b> Pre-generated blob bundles in tests — <i>implemented · low · cpu, latency</i></summary>

**Idea.** Ship a pre-generated test blobs bundle (blobs, commitments, proofs) instead of computing KZG commitments and proofs in tests and mock builders. Check Lighthouse's test utilities and mock EL for KZG computation at runtime.

**Impact.** Test-only: mock EL serves pre-generated bundle and cells, so no runtime KZG in mock builder; no mainnet effect.

**Best measured result.** pr:lighthouse#4829: get_header 550 ms -&gt; 50-55 ms; test 50 s -&gt; 10 s

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/test_utils/execution_block_generator.rs:38-42`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/test_utils/execution_block_generator.rs#L38-L42) include_bytes! fixtures test_blobs_bundle.ssz, _v2.ssz, _v2_cells.ssz
- execution_block_generator.rs:1273 compute_cells only inside a validation test

**Sources.** [lighthouse#4829](https://github.com/sigp/lighthouse/pull/4829)

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


<a id="kzg-041"></a>
<details>
<summary><b>kzg-041</b> Disable KZG library internal multithreading — <i>implemented · medium · S · cpu</i></summary>

**Idea.** Configure the KZG library to run single-threaded and let the client's own thread pool parallelize, since nested library and client rayon pools conflict. Check the threading mode Lighthouse passes when creating the rust-eth-kzg context.

**Impact.** The library runs single-threaded and Lighthouse's rayon pool does the parallelism, so no nested pools.

**Best measured result.** pr:lighthouse#6309: ~20% faster single-threaded (unconfirmed)

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.toml:224 rust_eth_kzg = "0.9" with no multithreaded feature
- [`crypto/kzg/Cargo.toml:22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/kzg/Cargo.toml#L22) inherits workspace dep, no features
- ~/.cargo/registry/src/*/rust_eth_kzg-0.9.1/Cargo.toml:30 multithreaded is opt-in and not in default
- [`crypto/kzg/src/lib.rs:261`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/kzg/src/lib.rs#L261) Lighthouse parallelises with its own rayon

**Sources.** [lighthouse#6309](https://github.com/sigp/lighthouse/pull/6309)

</details>


