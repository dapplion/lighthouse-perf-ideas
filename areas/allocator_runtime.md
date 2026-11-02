# allocator_runtime

18 checked ideas, 4 actionable. [Back to the summary](../README.md).

## Actionable (4)

High or medium value, verdict `not` or `partial`.

<a id="allocator_runtime-001"></a>
<details>
<summary><b>allocator_runtime-001</b> Force garbage collection at end of each slot — <i>partial · medium · S · memory</i></summary>

**Idea.** Trigger an explicit garbage collection or memory release at the end of each slot, when the node is idle, to bound memory growth between slots. Check whether Lighthouse runs any per-slot memory release (for example malloc_trim or a jemalloc purge) from its slot timer.

**Gap in Lighthouse.** No explicit slot-aligned release. Jemalloc background threads already purge dirty pages on a ~10s decay (about one slot), so memory is returned between slots asynchronously. Only an explicit arena purge (arena.&lt;MALLCTL_ARENAS_ALL&gt;.purge) or malloc_trim(0) for sysmalloc builds from per_slot_task is missing.

**Impact.** Small for default jemalloc builds, because the background purge already does time-based release; could help sysmalloc/glibc builds and reproducible builds that link Debian libjemalloc without the compiled conf.

**Evidence (Lighthouse @ 928b61e719).**

- [`common/malloc_utils/Cargo.toml:36-38`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/malloc_utils/Cargo.toml#L36-L38) Linux builds enable tikv-jemallocator feature background_threads
- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/tikv-jemalloc-sys-0.6.1+5.3.0-1-ge13ca993e8ccb9ba9847cc330696e02839f328f7/build.rs:221-228 and :457 that feature compiles background_thread:true into malloc_conf
- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/tikv-jemalloc-sys-0.6.1+5.3.0-1-ge13ca993e8ccb9ba9847cc330696e02839f328f7/jemalloc/include/jemalloc/internal/arena_types.h:7-8 dirty_decay_ms 10s, muzzy_decay_ms 0
- [`common/malloc_utils/src/glibc.rs:14-20`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/malloc_utils/src/glibc.rs#L14-L20) fixed 128KB mmap threshold to keep glibc heap small
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7471`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7471) per_slot_task has no explicit release

**Second check.** The earlier review missed that Linux builds turn on jemalloc background purge threads via the tikv-jemallocator background_threads feature, which is a time-based equivalent of per-slot release. I confirmed no malloc_trim, mallctl purge or prof call anywhere in the workspace sources.

**Sources.** [nimbus#975](https://github.com/status-im/nimbus-eth2/pull/975)

</details>

<a id="allocator_runtime-026"></a>
<details>
<summary><b>allocator_runtime-026</b> Jemalloc heap profiling over HTTP endpoint — <i>partial · medium · S · memory</i></summary>

**Idea.** Expose jemalloc heap profiling through an HTTP debug endpoint so memory growth can be diagnosed on running nodes. Check whether Lighthouse can dump jemalloc heap profiles at runtime.

**Gap in Lighthouse.** Profiling needs a custom build plus a restart with _RJEM_MALLOC_CONF, and dumps go only to files. There is no HTTP route (http_api or http_metrics) that toggles prof.active or calls prof.dump and returns the profile.

**Impact.** Diagnostic only: lets operators debug memory growth on a running node without a restart; no direct resource saving.

**Evidence (Lighthouse @ 928b61e719).**

- [`common/malloc_utils/Cargo.toml:20`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/malloc_utils/Cargo.toml#L20) jemalloc-profiling = tikv-jemallocator/profiling
- [`lighthouse/Cargo.toml:40-41`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/Cargo.toml#L40-L41) forwards the feature
- [`common/malloc_utils/src/jemalloc.rs:9`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/malloc_utils/src/jemalloc.rs#L9) _RJEM_MALLOC_CONF runtime override (allows prof:true,lg_prof_interval/prof_final file dumps)
- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/tikv-jemalloc-sys-0.6.1+5.3.0-1-ge13ca993e8ccb9ba9847cc330696e02839f328f7/jemalloc/src/ctl.c:140-145,194 prof options exist in the bundled jemalloc

**Second check.** I searched the whole workspace for mallctl, prof.dump, prof.active, pprof and tikv_jemalloc_ctl. The only user is the stats scrape in jemalloc.rs, and http_api has no allocator route. The env-var interval dump is the only runtime path.

**Sources.** [ethlambda#180](https://github.com/lambdaclass/ethlambda/pull/180)

</details>

<a id="allocator_runtime-027"></a>
<details>
<summary><b>allocator_runtime-027</b> Tune jemalloc decay and background purging — <i>partial · medium · S · memory</i></summary>

**Idea.** Configure jemalloc with background purge threads and shorter dirty/muzzy decay times so freed pages return to the OS and RSS stays lower. Check Lighthouse's jemalloc config string for background_thread and decay settings.

**Gap in Lighthouse.** Background purge threads are already on in the normal Linux and Docker builds, and muzzy decay is already 0. What is missing: an explicit dirty_decay_ms setting (left at the 10s default), and the reproducible JEMALLOC_OVERRIDE builds, which link Debian's libjemalloc and lose both background_thread and narenas:16.

**Impact.** The main teku gain (background purge) is already in place; tuning dirty_decay_ms below 10s would only trim a little more RSS. Fixing the reproducible build conf could matter for users of those images.

**Best measured result.** 5-day memory graphs vs glibc, no numbers (pr:teku#10319)

**Evidence (Lighthouse @ 928b61e719).**

- [`common/malloc_utils/Cargo.toml:36-38`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/malloc_utils/Cargo.toml#L36-L38) tikv-jemallocator features [stats, background_threads] on Linux
- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/tikv-jemallocator-0.6.1/Cargo.toml:70 background_threads -&gt; tikv-jemalloc-sys/background_threads
- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/tikv-jemalloc-sys-0.6.1+5.3.0-1-ge13ca993e8ccb9ba9847cc330696e02839f328f7/build.rs:457 always_enabled = CARGO_FEATURE_BACKGROUND_THREADS; :221-228 adds background_thread:true; :236-244 appends JEMALLOC_SYS_WITH_MALLOC_CONF
- [`.cargo/config.toml:3`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/.cargo/config.toml#L3) abort_conf:true,narenas:16 (effective conf background_thread:true,abort_conf:true,narenas:16)
- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/tikv-jemalloc-sys-0.6.1+5.3.0-1-ge13ca993e8ccb9ba9847cc330696e02839f328f7/jemalloc/include/jemalloc/internal/arena_types.h:7-8 defaults dirty_decay_ms 10000, muzzy_decay_ms 0
- Makefile:111,127 reproducible build uses JEMALLOC_OVERRIDE (Debian libjemalloc.a), build.rs:132 returns early so the compiled conf is not applied

**Second check.** The earlier review misread build.rs: always_enabled comes from CARGO_FEATURE_BACKGROUND_THREADS, which malloc_utils turns on for Linux, so background_thread:true is compiled in. I also checked the jemalloc 5.3 decay defaults and the reproducible override path.

**Sources.** [teku#10360](https://github.com/Consensys-Incorporated/teku/pull/10360), [teku#10319](https://github.com/Consensys-Incorporated/teku/pull/10319)

</details>

<a id="allocator_runtime-066"></a>
<details>
<summary><b>allocator_runtime-066</b> Async runtime tracing of task scheduling — <i>partial · medium · M · cpu, latency</i></summary>

**Idea.** Integrate a tracing facility for the async runtime that captures scheduling and task-poll events, so executor stalls and hot tasks can be found. Check whether Lighthouse can record tokio task poll times in production.

**Gap in Lighthouse.** No production recorder of tokio poll/scheduling events: no RuntimeMetrics export, no tokio-metrics, no on_before/after_task_poll hooks; tokio-console needs a special tokio_unstable build and is interactive. Merge a dial9-style recorder (lh#10391) or export tokio RuntimeMetrics (busy duration, poll counts, queue depth, slow polls) to Prometheus.

**Impact.** Lets operators find executor stalls and hot tasks on live nodes; diagnostic only, no direct speedup.

**Evidence (Lighthouse @ 928b61e719).**

- [`lighthouse/Cargo.toml:37`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/Cargo.toml#L37) optional console-subscriber feature
- [`lighthouse/src/main.rs:712-715`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/src/main.rs#L712-L715) console_subscriber::spawn() layer
- [`common/task_executor/src/lib.rs:144-150`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/task_executor/src/lib.rs#L144-L150) task names only under cfg(tokio_unstable)
- [`common/task_executor/src/lib.rs:135`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/task_executor/src/lib.rs#L135) TASKS_HISTOGRAM times whole task lifetime
- [`common/task_executor/src/metrics.rs:19-40`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/task_executor/src/metrics.rs#L19-L40) blocking/block_on/task histograms
- [`beacon_node/beacon_processor/src/metrics.rs:31`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/metrics.rs#L31) beacon_processor_worker_time per work type
- [`lighthouse/src/main.rs:661-709`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/src/main.rs#L661-L709) OTLP span export (application spans, not task polls)

**Second check.** Grepped the workspace for RuntimeMetrics, tokio-metrics, task poll hooks, thread park hooks and tokio_unstable; only console-subscriber exists. OTLP tracing and beacon_processor worker-time histograms give per-work timing, not per-poll scheduling data.

**Sources.** [lighthouse#10391](https://github.com/sigp/lighthouse/pull/10391)

</details>

## Other checked ideas (14)

Implemented, not applicable, or low value.

<a id="allocator_runtime-004"></a>
<details>
<summary><b>allocator_runtime-004</b> Benchmark mimalloc or tcmalloc as global allocator — <i>not · low · S · memory, cpu</i></summary>

**Idea.** Allow selecting an alternative global allocator (mimalloc, tcmalloc) and benchmark it against jemalloc on state transition runtime and RSS. Check whether Lighthouse has a build feature for mimalloc and what the benchmarks showed.

**Gap in Lighthouse.** Add a mimalloc feature to malloc_utils (GlobalAlloc in lib.rs) and benchmark. The measured result (state transition 13.1 s vs 22.6 s jemalloc) is attractive but RSS doubles (45 vs 23 MiB), and the PRs were not adopted.

**Impact.** Possibly ~40% faster state-transition-heavy workloads but about 2x RSS; unclear net win on a mainnet node, and jemalloc stats/profiling metrics would be lost.

**Best measured result.** mimalloc 13,120 ms vs jemalloc 22,559 ms vs glibc 17,471 ms, but RSS 45.4 MiB vs 23.0 MiB (pr:lighthouse#10046)

**Evidence (Lighthouse @ 928b61e719).**

- [`common/malloc_utils/Cargo.toml:14-26`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/malloc_utils/Cargo.toml#L14-L26) only jemalloc and sysmalloc features
- Cargo.lock has no mimalloc crate; grep for mimalloc/tcmalloc across the tree finds nothing
- [`lighthouse/Cargo.toml:80`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/Cargo.toml#L80) malloc_utils with jemalloc

**Sources.** [lighthouse#10046](https://github.com/sigp/lighthouse/pull/10046), [lighthouse#8884](https://github.com/sigp/lighthouse/pull/8884)

</details>

<a id="allocator_runtime-055"></a>
<details>
<summary><b>allocator_runtime-055</b> Pool snappy stream readers and writers — <i>not · low · S · memory, cpu</i></summary>

**Idea.** Reuse snappy stream reader/writer objects (each with ~142 KB scratch buffers) from a pool instead of creating one per response chunk or message. Check whether Lighthouse rpc codec creates a new snappy FrameEncoder/Decoder per chunk.

**Gap in Lighthouse.** Replace per-message FrameEncoder/FrameDecoder in SSZSnappyInboundCodec/OutboundCodec encode/decode with a reused encoder (reset the inner Vec) or snap::raw::Encoder with a persistent buffer, as raw frames are single-chunk.

**Impact.** Saves roughly 130-200 KiB of allocation churn per RPC chunk (e.g. 64-block ByRange response ~8 MB of garbage); small CPU gain with jemalloc, helps RSS fragmentation.

**Best measured result.** 64-block BeaconBlocksByRange response burned ~8.7 MB of garbage (pr:caplin#23423)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/codec.rs:127`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L127) and 389 FrameEncoder::new(Vec::new()) per message
- codec.rs:187,281,318 FrameDecoder::new(limit_reader) per decode
- codec.rs:184 decoded_buffer = vec![0; length] per message
- ~/.cargo/registry/src/*/snap-1.1.2/src/write.rs:83 each FrameEncoder allocates a MAX_BLOCK_SIZE (64 KiB) src Vec

**Sources.** [caplin#23423](https://github.com/erigontech/erigon/pull/23423)

</details>

<a id="allocator_runtime-054"></a>
<details>
<summary><b>allocator_runtime-054</b> Pin runtime version after regressions — <i>partial · low · S · cpu, latency</i></summary>

**Idea.** Benchmark runtime or toolchain upgrades before rollout and pin the version when a new release regresses performance. Check whether Lighthouse pins its Rust toolchain and benchmarks compiler upgrades.

**Gap in Lighthouse.** Release builds follow the latest stable compiler with only an MSRV floor. Add a rust-toolchain.toml pin for release builds and a benchmark gate (e.g. state-transition bench) before bumping.

**Impact.** Avoids silent compiler regressions; not a measurable speedup by itself.

**Best measured result.** poor performance on Node 1.24.0-rc.0, no numbers (pr:lodestar#7291)

**Evidence (Lighthouse @ 928b61e719).**

- [`lighthouse/Cargo.toml:7`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/Cargo.toml#L7) rust-version = 1.91.0 (MSRV only)
- no rust-toolchain file; CI uses channel: stable ([`.github/workflows/test-suite.yml:121`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/.github/workflows/test-suite.yml#L121))
- Makefile/Dockerfile: no pinned compiler version found

**Sources.** [lodestar#7291](https://github.com/ChainSafe/lodestar/pull/7291)

</details>

<a id="allocator_runtime-063"></a>
<details>
<summary><b>allocator_runtime-063</b> Remove needless iterator-to-vector collections — <i>partial · low · S · memory, cpu</i></summary>

**Idea.** Do not convert iterators or views into owned vectors in hot paths and REST/sync code when they are only iterated. Check Lighthouse for collect::&lt;Vec&lt;_&gt;&gt;() followed by a single iteration.

**Gap in Lighthouse.** Most of the ~210 collect::&lt;Vec&gt; sites are required (borrow release, response bodies, ownership). A few only inspect first/len/is_empty, e.g. naive_aggregation_pool set_bits (use iter().next() plus a count) and builder_deposits_cache::seed_from_state. Needs a per-site audit; no systematic hot-path offender found.

**Impact.** Negligible on a mainnet node; these are small, non-hot allocations (aggregation pool insert is per-attestation but the Vec is tiny).

**Best measured result.** every one is an unnecessary copy/allocation (pr:nimbus#8551)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/slashings.rs:26-34`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/slashings.rs#L26-L34) collect needed to release borrow before mutating state (legit)
- [`consensus/state_processing/src/builder_deposits_cache.rs:68`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/builder_deposits_cache.rs#L68) pending_deposits.iter().collect::&lt;Vec&lt;_&gt;&gt;() just to check is_empty/len then pass on
- [`beacon_node/beacon_chain/src/naive_aggregation_pool.rs:365-371`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/naive_aggregation_pool.rs#L365-L371) set_bits collected to read first() and len
- [`beacon_node/http_api/src/validators.rs:72`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validators.rs#L72),120,168 collect into response Vec (needed, serialized)

**Sources.** [nimbus#8551](https://github.com/status-im/nimbus-eth2/pull/8551)

</details>

<a id="allocator_runtime-003"></a>
<details>
<summary><b>allocator_runtime-003</b> Use SHA-NI accelerated sha256 implementation — <i>implemented · medium · cpu</i></summary>

**Idea.** Use a sha256 implementation that dispatches to CPU SHA extensions (SHA-NI/ARMv8 crypto) for tree hashing and pool its buffers. Check that the sha256 crate used by Lighthouse's tree hashing detects and uses SHA instructions at runtime.

**Gap in Lighthouse.** 

**Best measured result.** gave a nice boost on Celeron, not benchmarked (pr:caplin#7060)

**Evidence (Lighthouse @ 928b61e719).**

- ethereum_hashing-0.8.0/src/lib.rs:111-137 cpufeatures runtime detection of x86 SHA extensions, selects sha2 asm path
- ethereum_hashing-0.8.0/Cargo.toml:31 default features include ring (ARMv8 crypto path); Cargo.toml:153 uses default features

**Sources.** [caplin#7060](https://github.com/erigontech/erigon/pull/7060)

</details>

<a id="allocator_runtime-028"></a>
<details>
<summary><b>allocator_runtime-028</b> Tune glibc malloc arenas, mmap threshold, trim — <i>implemented · medium · memory, cpu</i></summary>

**Idea.** When using glibc malloc, set M_MMAP_THRESHOLD (and possibly cap arenas or call malloc_trim) so large state-sized buffers are mmapped and returned to the OS, and apply it only to the beacon node. Check Lighthouse's malloc_utils for mallopt settings and their scope.

**Gap in Lighthouse.** 

**Best measured result.** memory footprint smaller than with jemalloc, no numbers (pr:lighthouse#2299)

**Evidence (Lighthouse @ 928b61e719).**

- [`common/malloc_utils/src/glibc.rs:20`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/malloc_utils/src/glibc.rs#L20) OPTIMAL_MMAP_THRESHOLD 128K
- glibc.rs:141-148 malloc_mmap_threshold via mallopt
- glibc.rs:~128 configure_glibc_malloc skips if env var set
- [`lighthouse/src/main.rs:429-440`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/src/main.rs#L429-L440) applied only for beacon_node subcommand, skippable by flag

**Sources.** [lighthouse#2937](https://github.com/sigp/lighthouse/pull/2937), [lighthouse#2299](https://github.com/sigp/lighthouse/pull/2299), [lighthouse#2398](https://github.com/sigp/lighthouse/pull/2398), [lighthouse#2397](https://github.com/sigp/lighthouse/pull/2397), [lighthouse#2296](https://github.com/sigp/lighthouse/pull/2296)

</details>

<a id="allocator_runtime-029"></a>
<details>
<summary><b>allocator_runtime-029</b> Disable async future tracking in release builds — <i>implemented · medium · memory</i></summary>

**Idea.** Turn off debug tracking of async futures in default builds because it uses a lot of memory, especially during sync. Check Lighthouse release builds for tokio-console, task tracking or similar instrumentation enabled by default.

**Gap in Lighthouse.** 

**Best measured result.** uses a lot of memory, especially during sync (pr:nimbus#1628)

**Evidence (Lighthouse @ 928b61e719).**

- [`lighthouse/Cargo.toml:37`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/Cargo.toml#L37) console-subscriber is an optional feature, off by default
- [`common/task_executor/src/lib.rs:144-149`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/task_executor/src/lib.rs#L144-L149) tokio_unstable naming gated by cfg
- Cargo.toml and [`.cargo/config.toml`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/.cargo/config.toml): no tokio_unstable rustflag

**Sources.** [nimbus#1628](https://github.com/status-im/nimbus-eth2/pull/1628)

</details>

<a id="allocator_runtime-040"></a>
<details>
<summary><b>allocator_runtime-040</b> Release large init-time temporaries after startup — <i>implemented · medium · memory, startup</i></summary>

**Idea.** Drop large temporaries created during node initialization so they are not referenced for the process lifetime, and reuse a single validator pool instance. Check Lighthouse startup (genesis/checkpoint load, builder) for large values kept in long-lived structs.

**Gap in Lighthouse.** 

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/client/src/builder.rs:343`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L343),414,493 genesis_state is a local variable moved into the chain builder and dropped
- [`beacon_node/client/src/config.rs:80-82`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/config.rs#L80-L82) Config holds only URL options, not state bodies

**Sources.** [nimbus@0dbc7162a](https://github.com/status-im/nimbus-eth2/commit/0dbc7162ac44), [nimbus#2352](https://github.com/status-im/nimbus-eth2/pull/2352)

</details>

<a id="allocator_runtime-057"></a>
<details>
<summary><b>allocator_runtime-057</b> Precompute shuffled committees off the hot path — <i>implemented · medium · memory, cpu</i></summary>

**Idea.** Compute committee shufflings for previous, current and next epoch ahead of time and drop large per-slot allocations (~16MB every 12s). Check whether Lighthouse rebuilds committee structures per slot or caches them per epoch.

**Gap in Lighthouse.** 

**Impact.** Already precomputed ahead of the slot by the state advance timer and held in an Arc-shared cache; nothing per-slot to remove.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:333-340`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L333-L340) builds Current and Next committee caches in state advance, before the slot
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:398-410`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L398-L410) inserts the Next-epoch committee cache into the shuffling cache
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:25`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L25) DEFAULT_CACHE_SIZE=16, plus promises (line 105) to dedupe concurrent builds
- [`consensus/state_processing/src/per_epoch_processing/altair.rs:30-32`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/altair.rs#L30-L32) builds Previous/Current/Next caches once per epoch, not per slot

**Sources.** [caplin#18522](https://github.com/erigontech/erigon/pull/18522)

</details>

<a id="allocator_runtime-042"></a>
<details>
<summary><b>allocator_runtime-042</b> Reuse SHA-256 hasher without per-call allocation — <i>implemented · low · cpu, memory</i></summary>

**Idea.** Hash with one-shot functions on stack buffers or a pooled reusable hasher instead of allocating a hasher object per call in tree hashing. Check whether Lighthouse's hash32_concat and tree-hash paths allocate a Vec or hasher per hash.

**Gap in Lighthouse.** 

**Impact.** Hasher contexts are stack enums and results are fixed arrays; no per-call heap allocation in hash32_concat or hash_fixed.

**Best measured result.** Sha256(32B,32B) 78.2 -&gt; 52.1 ns, 2 allocs -&gt; 0 (pr:caplin#22489); pooled 77.30 -&gt; 47.65 ns/op (pr:prysm#15427)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/registry/src/*/ethereum_hashing-0.8.0/src/lib.rs:36-41 hash32_concat uses a stack DynamicContext, no Vec
- ethereum_hashing-0.8.0/src/lib.rs:66-80 ring Context finalised into [u8;32]
- ethereum_hashing-0.8.0/src/lib.rs:91-96 hash_fixed returns an array
- DynamicImpl::best() picks sha2 (SHA-NI) or ring at runtime

**Sources.** [caplin#22489](https://github.com/erigontech/erigon/pull/22489), [prysm#15427](https://github.com/OffchainLabs/prysm/pull/15427)

</details>

<a id="allocator_runtime-064"></a>
<details>
<summary><b>allocator_runtime-064</b> Shared constant zero hash instead of temporaries — <i>implemented · low · S · cpu</i></summary>

**Idea.** Pass a shared constant zero hash to calls instead of constructing and zero-filling a 32-byte temporary at each call site in hot paths. Check Lighthouse tree hashing for Hash256::zero() built in loops instead of a static.

**Gap in Lighthouse.** 

**Impact.** Already shared statics/consts; Hash256::ZERO and Hash256::zero() are const in lighthouse call sites, none are in tree-hash loops.

**Best measured result.** saves a 32-byte zero fill per call, no timing (pr:nimbus#3770)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/registry/src/*/tree_hash-0.12.1/src/lib.rs:94-95 get_zero_hash returns &amp;ZERO_HASHES[height]
- ~/.cargo/registry/src/*/ethereum_hashing-0.8.0/src/lib.rs:219 static LazyLock ZERO_HASHES
- ~/.cargo/registry/src/*/tree_hash-0.12.1/src/merkle_hasher.rs:283 Hash256::ZERO is a const
- milhouse-0.9.0/src/leaf.rs:31 Hash256::ZERO const

**Sources.** [nimbus#3770](https://github.com/status-im/nimbus-eth2/pull/3770)

</details>

<a id="allocator_runtime-035"></a>
<details>
<summary><b>allocator_runtime-035</b> Fix ownership leaks at the FFI boundary — <i>n/a · medium · memory</i></summary>

**Idea.** At C bindings, pass heap-owning arguments by reference so Drop runs, and free every element of returned vector wrappers, not only the backing pointer. Check Lighthouse FFI code (BLS, KZG, any C bindings) for moved arguments and shallow frees.

**Gap in Lighthouse.** 

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/impls/blst.rs:61-64`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L61-L64) only unsafe is scalar init, no ownership transfer
- [`crypto/kzg/Cargo.toml:22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/kzg/Cargo.toml#L22) uses rust_eth_kzg safe Rust API; BLS via blst crate

**Sources.** [grandine@5cf4db0ea](https://github.com/grandinetech/grandine/commit/5cf4db0eaffb), [grandine#707](https://github.com/grandinetech/grandine/pull/707), [grandine@927eb7830](https://github.com/grandinetech/grandine/commit/927eb78307f3)

</details>

<a id="allocator_runtime-008"></a>
<details>
<summary><b>allocator_runtime-008</b> Low-allocation hex encoding of roots and pubkeys — <i>n/a · low · memory, cpu</i></summary>

**Idea.** Convert 32-byte roots and 48-byte pubkeys to hex with a specialised helper that writes into a reusable buffer or lookup table instead of string concatenation or per-call allocation, and use it everywhere roots are stringified (gossip, fork choice, cache keys). Check whether Lighthouse formats roots to hex strings on hot paths, for example as map keys or in logs that are always evaluated.

**Gap in Lighthouse.** Lighthouse keys caches and fork choice on Hash256/PublicKeyBytes byte arrays and formats hex only at logging/API edges (tracing fields are lazy), so there is no hot-path stringification to optimise.

**Impact.** Little to gain; hex formatting is off the hot path.

**Best measured result.** toRootHex 156 ns to 105 ns; GC time ~2.9% to &lt;2.3% (pr:lodestar#7060, pr:lodestar#7036)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/topics.rs:374`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/topics.rs#L374) hex::encode only for fork digest topic names
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1313`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1313) hex only in a log path
- Hot-path maps key on Hash256 (fixed bytes), not strings

**Sources.** [lodestar#7036](https://github.com/ChainSafe/lodestar/pull/7036), [lodestar#7075](https://github.com/ChainSafe/lodestar/pull/7075), [lodestar#7060](https://github.com/ChainSafe/lodestar/pull/7060), [lodestar#7065](https://github.com/ChainSafe/lodestar/pull/7065), [lodestar#7016](https://github.com/ChainSafe/lodestar/pull/7016), [lodestar#7021](https://github.com/ChainSafe/lodestar/pull/7021)

</details>

<a id="allocator_runtime-023"></a>
<details>
<summary><b>allocator_runtime-023</b> Serialize arena-backed proving on one thread — <i>n/a · low · memory, cpu</i></summary>

**Idea.** When a prover uses a per-thread arena whose slabs are never released, run all proofs on one long-lived thread or behind a one-at-a-time permit, so only one proof-peak slab is pinned. Check whether Lighthouse runs any arena-allocating crypto job on arbitrary pool threads.

**Gap in Lighthouse.** Lighthouse does not run a prover with a per-thread arena that never releases slabs; KZG/blob verification and cell recovery allocate through the global jemalloc.

**Impact.** None.

**Best measured result.** OOM about every 40 min (~29 GB RSS) fixed; slab count stays 10 vs 10 to 14 before (pr:ethlambda#641)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/registry/src/*/rust_eth_kzg-0.9.1: no thread_local arena or bump allocator in the source
- Cargo.lock kzg stack: c-kzg, rust_eth_kzg, blst; no proving arena is used

**Sources.** [ethlambda#641](https://github.com/lambdaclass/ethlambda/pull/641), [ethlambda#540](https://github.com/lambdaclass/ethlambda/pull/540)

</details>

