# allocator_runtime

79 ideas: 7 not, 16 partial, 18 implemented, 38 n/a; 4 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [allocator_runtime-001](#allocator_runtime-001) **★** | Force garbage collection at end of each slot | partial | medium | S | memory |
| [allocator_runtime-002](#allocator_runtime-002) | Flag to tune GC growth percent | not | low | S | memory, cpu |
| [allocator_runtime-003](#allocator_runtime-003) | Use SHA-NI accelerated sha256 implementation | implemented | medium | S | cpu |
| [allocator_runtime-004](#allocator_runtime-004) | Benchmark mimalloc or tcmalloc as global allocator | not | low | S | memory, cpu |
| [allocator_runtime-005](#allocator_runtime-005) | Async random bytes in peer discovery | n/a | low | S | latency |
| [allocator_runtime-006](#allocator_runtime-006) | Avoid big-integer construction from literal zero | n/a | low | S | memory, cpu |
| [allocator_runtime-007](#allocator_runtime-007) | Zero-copy byte views instead of buffer copies | partial | low | M | cpu, memory |
| [allocator_runtime-008](#allocator_runtime-008) | Low-allocation hex encoding of roots and pubkeys | n/a | low |  | memory, cpu |
| [allocator_runtime-009](#allocator_runtime-009) | Move large beacon values instead of deep copying | n/a | low | S | cpu, memory |
| [allocator_runtime-010](#allocator_runtime-010) | Remove event listeners when their task ends | n/a | low | S | memory |
| [allocator_runtime-011](#allocator_runtime-011) | Avoid per-call closure allocation on hot paths | n/a | low | S | cpu, memory |
| [allocator_runtime-012](#allocator_runtime-012) | Iterate large structs by reference, precompile regexes | partial | low | S | cpu, memory |
| [allocator_runtime-013](#allocator_runtime-013) | Keep small hash buffers on the stack | n/a | low | S | memory, cpu |
| [allocator_runtime-014](#allocator_runtime-014) | Zeroed buffer for wasm snappy decompression output | implemented | low | S | memory, cpu |
| [allocator_runtime-015](#allocator_runtime-015) | Enlarge young generation for network worker heap | partial | low | S | cpu, memory |
| [allocator_runtime-016](#allocator_runtime-016) | Bound chunks per native hashing call | n/a | low | S | latency |
| [allocator_runtime-017](#allocator_runtime-017) | Cheap overflow-checked u64 multiplication | n/a | low | S | cpu |
| [allocator_runtime-018](#allocator_runtime-018) | Clear references before returning objects to pool | n/a | low | S | memory |
| [allocator_runtime-019](#allocator_runtime-019) | Complete futures on publisher thread | n/a | low | S | latency |
| [allocator_runtime-020](#allocator_runtime-020) | Configurable size of native state node pool | n/a | low | S | memory |
| [allocator_runtime-021](#allocator_runtime-021) | Hold hot constants in native integer type | n/a | low | S | cpu, memory |
| [allocator_runtime-022](#allocator_runtime-022) | Size runtime threads from container CPU quota | implemented | low | S | cpu, latency |
| [allocator_runtime-023](#allocator_runtime-023) | Serialize arena-backed proving on one thread | n/a | low |  | memory, cpu |
| [allocator_runtime-024](#allocator_runtime-024) | Bump native state-transition library | implemented | low | S | cpu |
| [allocator_runtime-025](#allocator_runtime-025) | Use jemalloc as default global allocator | implemented | low | S | memory, cpu |
| [allocator_runtime-026](#allocator_runtime-026) **★** | Jemalloc heap profiling over HTTP endpoint | partial | medium | S | memory |
| [allocator_runtime-027](#allocator_runtime-027) **★** | Tune jemalloc decay and background purging | partial | medium | S | memory |
| [allocator_runtime-028](#allocator_runtime-028) | Tune glibc malloc arenas, mmap threshold, trim | implemented | low | S | memory, cpu |
| [allocator_runtime-029](#allocator_runtime-029) | Disable async future tracking in release builds | implemented | low | S | memory |
| [allocator_runtime-030](#allocator_runtime-030) | Drop memory wiping and copies in hash path | implemented | low | S | cpu, memory |
| [allocator_runtime-031](#allocator_runtime-031) | Expose native memory as external GC buffers | n/a | low | S | memory, cpu |
| [allocator_runtime-032](#allocator_runtime-032) | Faster HTTP stream implementation for beacon API | n/a | low | S | cpu, latency |
| [allocator_runtime-033](#allocator_runtime-033) | Fewer allocations per async future | n/a | low | S | memory, cpu |
| [allocator_runtime-034](#allocator_runtime-034) | Fine-grained locking around beacon state | implemented | low | S | cpu, latency |
| [allocator_runtime-035](#allocator_runtime-035) | Fix ownership leaks at the FFI boundary | n/a | medium |  | memory |
| [allocator_runtime-036](#allocator_runtime-036) | Fix snappy stream leak in req/resp | n/a | low | S | memory |
| [allocator_runtime-037](#allocator_runtime-037) | Fix stack collector memory leak | n/a | low | S | memory |
| [allocator_runtime-038](#allocator_runtime-038) | Destroy thread-pool task objects after run | n/a | low | S | memory |
| [allocator_runtime-039](#allocator_runtime-039) | Avoid nested thread pool oversubscription | partial | low | S | cpu |
| [allocator_runtime-040](#allocator_runtime-040) | Release large init-time temporaries after startup | implemented | low | S | memory, startup |
| [allocator_runtime-041](#allocator_runtime-041) | Pool gossip decompression buffers per topic | not | low | M | memory, cpu |
| [allocator_runtime-042](#allocator_runtime-042) | Reuse SHA-256 hasher without per-call allocation | implemented | low | S | cpu, memory |
| [allocator_runtime-043](#allocator_runtime-043) | Lazy split iterators instead of split slices | n/a | low | S | memory |
| [allocator_runtime-044](#allocator_runtime-044) | Cap network library direct buffer memory | partial | low | S | memory |
| [allocator_runtime-045](#allocator_runtime-045) | Linked-list or deque FIFO job queues | implemented | low | S | cpu |
| [allocator_runtime-046](#allocator_runtime-046) | Bounded queue with internal locking for throttling | implemented | low | S | cpu, latency |
| [allocator_runtime-047](#allocator_runtime-047) | Set heap limit near real usage to fail fast | n/a | low | S | memory |
| [allocator_runtime-048](#allocator_runtime-048) | Raise runtime heap limit for memory spikes | n/a | low | S | memory, cpu |
| [allocator_runtime-049](#allocator_runtime-049) | Reduce stack usage of light-client data store | n/a | low | S | memory |
| [allocator_runtime-050](#allocator_runtime-050) | Allocate startup block summaries outside GC heap | n/a | low | S | memory |
| [allocator_runtime-051](#allocator_runtime-051) | Upgrade network library adaptive buffer allocator | n/a | low | S | memory |
| [allocator_runtime-052](#allocator_runtime-052) | Newer runtime GC with soft heap target | partial | low | M | memory |
| [allocator_runtime-053](#allocator_runtime-053) | Park idle worker threads instead of spinning | n/a | low | S | cpu |
| [allocator_runtime-054](#allocator_runtime-054) | Pin runtime version after regressions | partial | low | S | cpu, latency |
| [allocator_runtime-055](#allocator_runtime-055) | Pool snappy stream readers and writers | not | low | S | memory, cpu |
| [allocator_runtime-056](#allocator_runtime-056) | Preallocate collections with known capacity | partial | low | S | memory, cpu |
| [allocator_runtime-057](#allocator_runtime-057) | Precompute shuffled committees off the hot path | implemented | medium | S | memory, cpu |
| [allocator_runtime-058](#allocator_runtime-058) | Prover on system allocator instead of bump arena | n/a | low | S | memory, bandwidth, cpu |
| [allocator_runtime-059](#allocator_runtime-059) | Scoped bump arena only for proving threads | n/a | low | M | cpu |
| [allocator_runtime-060](#allocator_runtime-060) | Reclaim receive buffers, slab allocator for packets | implemented | low | S | cpu, latency, memory |
| [allocator_runtime-061](#allocator_runtime-061) | Release allocator instead of debug allocator | n/a | low | S | cpu, memory |
| [allocator_runtime-062](#allocator_runtime-062) | Avoid reference cycles that leak memory | not | low | S | memory |
| [allocator_runtime-063](#allocator_runtime-063) | Remove needless iterator-to-vector collections | partial | low | S | memory, cpu |
| [allocator_runtime-064](#allocator_runtime-064) | Shared constant zero hash instead of temporaries | implemented | low | S | cpu |
| [allocator_runtime-065](#allocator_runtime-065) | Reuse and stop timers in loops | implemented | low | S | memory, cpu |
| [allocator_runtime-066](#allocator_runtime-066) **★** | Async runtime tracing of task scheduling | partial | medium | M | cpu, latency |
| [allocator_runtime-067](#allocator_runtime-067) | Shared memory messaging between worker threads | n/a | low | S | latency, cpu |
| [allocator_runtime-068](#allocator_runtime-068) | Skip expensive direct buffer cleaning | n/a | low | S | memory |
| [allocator_runtime-069](#allocator_runtime-069) | Schedule job runs only below max concurrency | n/a | low | S | cpu |
| [allocator_runtime-070](#allocator_runtime-070) | Native slice-to-array conversion for byte copies | n/a | low | S | cpu, memory |
| [allocator_runtime-071](#allocator_runtime-071) | Configurable executor thread counts and queue sizes | partial | low | S | cpu, latency |
| [allocator_runtime-072](#allocator_runtime-072) | Allocate buffers uninitialized when immediately overwritten | partial | low | S | cpu, memory |
| [allocator_runtime-073](#allocator_runtime-073) | Green threads for event-channel consumers | n/a | low | S | memory, cpu, latency |
| [allocator_runtime-074](#allocator_runtime-074) | Write small messages directly when queue empty | not | low | M | latency |
| [allocator_runtime-075](#allocator_runtime-075) | Do not yield while holding state references | n/a | low | S | memory |
| [allocator_runtime-076](#allocator_runtime-076) | Avoid formatter allocations for simple string conversions | not | low | S | memory, cpu |
| [allocator_runtime-077](#allocator_runtime-077) | Drop async runtime immediately on shutdown | implemented | low | S | latency |
| [allocator_runtime-078](#allocator_runtime-078) | Run blocking validation in blocking pool | partial | low | S | latency, cpu |
| [allocator_runtime-079](#allocator_runtime-079) | Offload consensus engine to separate worker thread | n/a | low |  | cpu, latency |

★ actionable. Click an id for the full record.

## Ideas

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

**Verdict history.** not (checked) → partial (refuted)

**Sources.** [nimbus#975](https://github.com/status-im/nimbus-eth2/pull/975)

</details>


<a id="allocator_runtime-002"></a>
<details>
<summary><b>allocator_runtime-002</b> Flag to tune GC growth percent — <i>not · low · S · memory, cpu</i></summary>

**Idea.** Expose a runtime flag that sets how much the heap may grow before the next collection, so operators can trade memory for fewer collection runs. In Lighthouse the analogue is exposing allocator purge/decay knobs on the CLI.

**Gap in Lighthouse.** Add optional CLI/env flags for jemalloc decay/glibc trim in malloc_utils::configure_memory_allocator.

**Impact.** Operator memory-vs-CPU tuning only; no default gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`common/malloc_utils/src/jemalloc.rs:3`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/malloc_utils/src/jemalloc.rs#L3) jemalloc configured only via [`.cargo/config.toml`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/.cargo/config.toml)
- [`common/malloc_utils/src/glibc.rs:126`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/malloc_utils/src/glibc.rs#L126) only sets M_MMAP_THRESHOLD, env override
- [`beacon_node/src/cli.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs): no allocator flag

**Sources.** [prysm#4897](https://github.com/OffchainLabs/prysm/pull/4897)

</details>


<a id="allocator_runtime-003"></a>
<details>
<summary><b>allocator_runtime-003</b> Use SHA-NI accelerated sha256 implementation — <i>implemented · medium · S · cpu</i></summary>

**Idea.** Use a sha256 implementation that dispatches to CPU SHA extensions (SHA-NI/ARMv8 crypto) for tree hashing and pool its buffers. Check that the sha256 crate used by Lighthouse's tree hashing detects and uses SHA instructions at runtime.

**Impact.** Already in place: tree hashing in tree_hash and milhouse goes through ethereum_hashing, which dispatches to SHA-NI at runtime.

**Best measured result.** gave a nice boost on Celeron, not benchmarked (pr:caplin#7060)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/registry/src/*/ethereum_hashing-0.8.0/src/lib.rs:107-140 cpufeatures x86_sha_extensions latch; DynamicImpl::best() picks Sha2 (SHA-NI) when present, else ring
- ethereum_hashing-0.8.0/Cargo.toml:31-36 default features zero_hash_cache+ring (ring does its own ARMv8 crypto detection)
- lh-perf-research-base/Cargo.toml:153 ethereum_hashing = "0.8.0" with default features
- tree_hash merkleize_padded.rs:2 and milhouse tree.rs:4 import ethereum_hashing::hash32_concat/hash_fixed

**Skeptic check.** I confirmed the runtime CPU-feature dispatch and that both tree_hash and milhouse use this crate, so the hot tree-hash path benefits. The earlier evidence was right. There are no buffers to pool, because contexts live on the stack.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#7060](https://github.com/erigontech/erigon/pull/7060)

</details>


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


<a id="allocator_runtime-005"></a>
<details>
<summary><b>allocator_runtime-005</b> Async random bytes in peer discovery — <i>n/a · low · S · latency</i></summary>

**Idea.** Generate random bytes for peer discovery with a non-blocking API so waiting for entropy cannot block the event loop or async executor. Check whether Lighthouse's discovery code calls a blocking OS random source on an async worker thread.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- discv5-0.12.0/src/rpc.rs:33 rand::random uses non-blocking thread RNG
- discovery/mod.rs:850 NodeId::random()

**Sources.** [lodestar#4075](https://github.com/ChainSafe/lodestar/pull/4075)

</details>


<a id="allocator_runtime-006"></a>
<details>
<summary><b>allocator_runtime-006</b> Avoid big-integer construction from literal zero — <i>n/a · low · S · memory, cpu</i></summary>

**Idea.** In hot paths, construct zero big integers with the zero-value constructor instead of parsing or converting a literal, avoiding a needless allocation and initialization. Check Lighthouse hot paths that build U256/BigUint zeros through conversions.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- grep U256::from(0)/BigUint::from(0): no hits

**Sources.** [prysm#13715](https://github.com/OffchainLabs/prysm/pull/13715)

</details>


<a id="allocator_runtime-007"></a>
<details>
<summary><b>allocator_runtime-007</b> Zero-copy byte views instead of buffer copies — <i>partial · low · M · cpu, memory</i></summary>

**Idea.** In gossip encoding, req/resp, pubkey cache, shuffling, randao xor and database keys, use views over the existing bytes instead of copying into new buffers, and do byte operations in place. Check Lighthouse for to_vec/clone of byte buffers in these paths where a slice would do.

**Gap in Lighthouse.** Most paths use slices; DB key construction and hdiff buffers still allocate Vec copies; could take &amp;[u8] keys or reuse buffers in store ops.

**Impact.** Small allocation savings on store writes; likely under 1% of CPU.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1338-1435`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1338-L1435) key.as_slice().to_vec() for DB keys
- [`beacon_node/store/src/hdiff.rs:179-198`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L179-L198) to_vec of state lists

**Sources.** [lodestar#6723](https://github.com/ChainSafe/lodestar/pull/6723)

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


<a id="allocator_runtime-009"></a>
<details>
<summary><b>allocator_runtime-009</b> Move large beacon values instead of deep copying — <i>n/a · low · S · cpu, memory</i></summary>

**Idea.** Avoid generic deep-copy assignment of large beacon types (states, blocks) and pass them by move or reference, including inside the async runtime. Check Lighthouse for clone() of BeaconState or large containers where ownership could be moved.

**Impact.** None beyond audits.

**Best measured result.** genericAssign 40.65% of CPU during sync, gone after (pr:nimbus#1166)

**Evidence (Lighthouse @ 928b61e719).**

- Rust moves by default; hdiff.rs:185 uses take_validators/mem::take

**Sources.** [nimbus#1166](https://github.com/status-im/nimbus-eth2/pull/1166), [nimbus#5684](https://github.com/status-im/nimbus-eth2/pull/5684)

</details>


<a id="allocator_runtime-010"></a>
<details>
<summary><b>allocator_runtime-010</b> Remove event listeners when their task ends — <i>n/a · low · S · memory</i></summary>

**Idea.** Unregister per-slot event listeners and signal handlers when the task that added them finishes, so closures and captured data are not retained and do not accumulate. Check Lighthouse for event subscriptions or broadcast receivers that are added per slot or per request and never dropped.

**Impact.** None.

**Best measured result.** heap graph before/after, no numbers (pr:lodestar#1560)

**Evidence (Lighthouse @ 928b61e719).**

- beacon_chain/src/events.rs:222-290 broadcast subscribe
- http_api/src/lib.rs:3511 receiver owned by SSE stream

**Sources.** [lodestar#4421](https://github.com/ChainSafe/lodestar/pull/4421), [lodestar#1560](https://github.com/ChainSafe/lodestar/pull/1560)

</details>


<a id="allocator_runtime-011"></a>
<details>
<summary><b>allocator_runtime-011</b> Avoid per-call closure allocation on hot paths — <i>n/a · low · S · cpu, memory</i></summary>

**Idea.** Do not allocate a closure per timer or per response chunk; pass arguments directly or reuse one pre-bound handler, which also avoids capturing large objects that delay freeing. Check Lighthouse network handlers for boxed closures or futures created per chunk.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- No per-chunk boxed closure pattern found in lighthouse_network rpc

**Sources.** [lodestar#8832](https://github.com/ChainSafe/lodestar/pull/8832)

</details>


<a id="allocator_runtime-012"></a>
<details>
<summary><b>allocator_runtime-012</b> Iterate large structs by reference, precompile regexes — <i>partial · low · S · cpu, memory</i></summary>

**Idea.** Iterate collections of large structs by index or reference instead of copying each element by value, and compile static regexes once at module scope. Check Lighthouse hot loops for by-value iteration with clones and for Regex::new inside functions.

**Gap in Lighthouse.** Static regexes are compiled inside functions on each call; move to LazyLock/OnceLock statics in Graffiti::as_utf8_lossy, ErrorType::fmt, and the keystore name check (or replace with char filtering).

**Impact.** Saves microseconds per call; only matters on API/log paths with graffiti and RPC errors.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/core/graffiti.rs:19`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/core/graffiti.rs#L19) Regex::new per as_utf8_lossy call
- [`beacon_node/lighthouse_network/src/rpc/methods.rs:60`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/methods.rs#L60) Regex::new per ErrorType Display
- [`common/account_utils/src/validator_definitions.rs:522`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/account_utils/src/validator_definitions.rs#L522),531 Regex::new per file name

**Sources.** [caplin#22711](https://github.com/erigontech/erigon/pull/22711)

</details>


<a id="allocator_runtime-013"></a>
<details>
<summary><b>allocator_runtime-013</b> Keep small hash buffers on the stack — <i>n/a · low · S · memory, cpu</i></summary>

**Idea.** Write hot helpers so small buffers (32-byte hashes, cache keys) do not escape to the heap: slice the addressable value directly and use real inlinable functions instead of function-pointer variables. Check Lighthouse for Vec allocations of fixed small size where a stack array would do.

**Impact.** Rust has no escape-analysis heap/stack issue; hash helpers already return arrays by value. Nothing to gain.

**Best measured result.** isCode 33.7 -&gt; 24.8 ns/op, 1 alloc -&gt; 0 (pr:caplin#22741)

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.lock:3810 ethereum_hashing 0.8.0 hash_fixed returns [u8;32] by value (lib.rs:31)

**Sources.** [caplin#21503](https://github.com/erigontech/erigon/pull/21503), [caplin#22741](https://github.com/erigontech/erigon/pull/22741)

</details>


<a id="allocator_runtime-014"></a>
<details>
<summary><b>allocator_runtime-014</b> Zeroed buffer for wasm snappy decompression output — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** When decompressing snappy into an output buffer, allocate a fresh zeroed buffer instead of an uninitialised pooled one that caused heavy mark-sweep GC. Check how Lighthouse allocates snappy decompression output buffers.

**Impact.** None left: both gossip and RPC decode into fresh, bounded, zeroed buffers; there is no GC so the original problem (pooled uninitialised wasm buffer causing mark-sweep) cannot arise.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/pubsub.rs:115-124`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L115-L124) decompress_len bound then decompress_vec into a fresh exact-size Vec
- [`beacon_node/lighthouse_network/src/rpc/codec.rs:187-190`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L187-L190),283-285,319-320 RPC path: FrameDecoder read_exact into fresh vec![0; length]

**Skeptic check.** Verified gossip (pubsub.rs) and all three RPC decode paths (codec.rs) allocate fresh zeroed exact-length buffers; earlier evidence was right and the RPC path agrees.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#8671](https://github.com/ChainSafe/lodestar/pull/8671)

</details>


<a id="allocator_runtime-015"></a>
<details>
<summary><b>allocator_runtime-015</b> Enlarge young generation for network worker heap — <i>partial · low · S · cpu, memory</i></summary>

**Idea.** Size the young generation of the network thread's heap so short-lived message objects die there without repeated scavenge copying. For Lighthouse the analogue is per-thread allocator caches (tcache) sized for the network threads.

**Gap in Lighthouse.** jemalloc tcache is on by default with default sizing; Lighthouse only sets narenas:16 and does not tune tcache max/size for network threads. A tcache or dirty_decay_ms setting could be added to the malloc conf string in .cargo/config.toml, only after profiling.

**Impact.** Possibly slightly fewer arena lock hits for network threads; no measured gain, marginal.

**Best measured result.** scavenge &gt;200 MB and 3% of worker time before (pr:lodestar#5829)

**Evidence (Lighthouse @ 928b61e719).**

- [`.cargo/config.toml:2`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/.cargo/config.toml#L2) JEMALLOC malloc conf narenas:16
- [`common/malloc_utils/src/jemalloc.rs:1-10`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/malloc_utils/src/jemalloc.rs#L1-L10) conf overridable via _RJEM_MALLOC_CONF

**Sources.** [lodestar#5829](https://github.com/ChainSafe/lodestar/pull/5829)

</details>


<a id="allocator_runtime-016"></a>
<details>
<summary><b>allocator_runtime-016</b> Bound chunks per native hashing call — <i>n/a · low · S · latency</i></summary>

**Idea.** Split very large hashing layers into bounded batches per call into the native SHA256 routine so one call does not run long without a yield point. Check whether Lighthouse hashes whole large layers in one blocking call on an async worker thread.

**Impact.** Hashing runs on blocking threads, not async workers, so no yield point is needed; native sha256 is in-process Rust, not a cgo-like call.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:1657-1719`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1657-L1719) work runs via spawn_blocking
- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/tree_hash-0.12.1/src/merkle_hasher.rs:200 MerkleHasher streams leaves

**Sources.** [prysm#17542](https://github.com/OffchainLabs/prysm/pull/17542)

</details>


<a id="allocator_runtime-017"></a>
<details>
<summary><b>allocator_runtime-017</b> Cheap overflow-checked u64 multiplication — <i>n/a · low · S · cpu</i></summary>

**Idea.** Implement checked u64 multiplication with a cheap overflow test instead of widening to big integers. Check Lighthouse safe_arith and reward calculations for u128 or bigint multiplication where checked_mul would do.

**Impact.** Already uses native checked_mul; no bigint widening.

**Best measured result.** 30% faster with 32-bit operands, 8x faster when one is longer than 32 bits (pr:teku#3376)

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.lock:8807 safe_arith 0.1.0
- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/safe_arith-0.1.0/src/lib.rs:150-151 safe_mul uses checked_mul

**Sources.** [teku#3376](https://github.com/Consensys-Incorporated/teku/pull/3376)

</details>


<a id="allocator_runtime-018"></a>
<details>
<summary><b>allocator_runtime-018</b> Clear references before returning objects to pool — <i>n/a · low · S · memory</i></summary>

**Idea.** Before putting an object back into an object pool, clear every field that holds pointers or buffers so idle pooled objects do not pin block-sized memory. Check any Lighthouse object or buffer pools for retained large capacity after reuse.

**Impact.** Lighthouse allocates per message via jemalloc and frees on drop; no object pools that could pin memory.

**Evidence (Lighthouse @ 928b61e719).**

- milhouse 0.9.0 (Cargo.lock:6570) has no node pool; grep for object pools in beacon_node found none for blocks/buffers

**Sources.** [caplin#23642](https://github.com/erigontech/erigon/pull/23642), [caplin#22410](https://github.com/erigontech/erigon/pull/22410)

</details>


<a id="allocator_runtime-019"></a>
<details>
<summary><b>allocator_runtime-019</b> Complete futures on publisher thread — <i>n/a · low · S · latency</i></summary>

**Idea.** Complete returned futures on a thread owned by the publisher, not the subscriber thread, so chained continuations do not block the subscriber from its next event. Check Lighthouse channels where a receiver runs heavy continuation work inline on the event loop.

**Impact.** No future-completion-on-subscriber-thread pattern; Tokio wakers schedule continuations on the executor and heavy work goes to the beacon processor.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:1657-1719`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1657-L1719) heavy work offloaded to blocking tasks

**Sources.** [teku#2362](https://github.com/Consensys-Incorporated/teku/pull/2362)

</details>


<a id="allocator_runtime-020"></a>
<details>
<summary><b>allocator_runtime-020</b> Configurable size of native state node pool — <i>n/a · low · S · memory</i></summary>

**Idea.** Let operators size the preallocated tree-node pool used for state representation, so small nodes (bootnodes) do not reserve hundreds of MB. Check whether Lighthouse preallocates any fixed-size pool or arena for tree-states and whether it is configurable.

**Impact.** Tree-states use Arc nodes allocated on demand from jemalloc; there is no preallocated node pool to size.

**Best measured result.** 454 MiB vs 837 MiB for a bootnode (pr:lodestar#10226)

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.lock:6570 milhouse 0.9.0; [`.cargo/config.toml:2`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/.cargo/config.toml#L2) jemalloc

**Sources.** [lodestar#10226](https://github.com/ChainSafe/lodestar/pull/10226)

</details>


<a id="allocator_runtime-021"></a>
<details>
<summary><b>allocator_runtime-021</b> Hold hot constants in native integer type — <i>n/a · low · S · cpu, memory</i></summary>

**Idea.** Store hot spec constants (min deposit, max effective balance, ejection balance) in the native integer type used by arithmetic, so each use does not convert or allocate. Check Lighthouse state processing for repeated conversions of ChainSpec values inside loops.

**Impact.** Spec constants are plain u64 fields in ChainSpec; there is no boxed or converted type, so nothing to save.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/core/chain_spec.rs:85`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/core/chain_spec.rs#L85) min_deposit_amount: u64
- [`consensus/types/src/core/chain_spec.rs:87`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/core/chain_spec.rs#L87) ejection_balance: u64
- [`consensus/types/src/core/chain_spec.rs:489`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/core/chain_spec.rs#L489) max_effective_balance_for_fork returns u64

**Sources.** [teku#3367](https://github.com/Consensys-Incorporated/teku/pull/3367)

</details>


<a id="allocator_runtime-022"></a>
<details>
<summary><b>allocator_runtime-022</b> Size runtime threads from container CPU quota — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Set worker thread counts from the container cgroup CPU quota instead of host core count, avoiding throttling and oversubscription in containers. Check whether Lighthouse sizes tokio and rayon pools from num_cpus or from available_parallelism with cgroup awareness.

**Impact.** Container CPU quota already respected by every pool sizer.

**Evidence (Lighthouse @ 928b61e719).**

- [`common/task_executor/src/rayon_pool_provider.rs:26`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/task_executor/src/rayon_pool_provider.rs#L26),34 rayon pools sized from num_cpus::get()
- [`beacon_node/beacon_processor/src/lib.rs:130`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L130) max_workers = num_cpus::get()
- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/num_cpus-1.17.0/src/linux.rs:32-37,110-140 get_num_cpus uses cgroup quota (min(quota, logical)) before sched_getaffinity
- [`lighthouse/environment/src/lib.rs:172`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/environment/src/lib.rs#L172) tokio new_multi_thread with default worker count (std available_parallelism, cgroup-aware)

**Skeptic check.** Cargo.lock pins num_cpus 1.17.0, whose Linux get_num_cpus reads the cgroup quota; tokio default uses available_parallelism, also quota-aware. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#2770](https://github.com/OffchainLabs/prysm/pull/2770)

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


<a id="allocator_runtime-024"></a>
<details>
<summary><b>allocator_runtime-024</b> Bump native state-transition library — <i>implemented · low · S · cpu</i></summary>

**Idea.** Upgrade the native state-transition dependency to a release that includes performance work. Check Lighthouse dependency versions for performance-relevant crates (tree hashing, BLS, ssz) behind upstream.

**Impact.** Generic dependency-bump idea; the perf crates track sigp heads via git patches, no specific stale release found offline.

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.toml:295-303 [patch.crates-io] milhouse, ethereum_ssz, tree_hash, ssz_types pinned to recent sigp git revs
- Cargo.lock: milhouse 0.9.0, tree_hash 0.12.1, ethereum_ssz 0.10.4 (git), ethereum_hashing 0.8.0, blst 0.3.17, c-kzg 2.1.8, rust_eth_kzg 0.9.1

**Skeptic check.** Confirmed versions and git patches; this is a process idea rather than a mechanism, so 'implemented' is upheld with low confidence because upstream latest versions could not be checked offline.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#10061](https://github.com/ChainSafe/lodestar/pull/10061)

</details>


<a id="allocator_runtime-025"></a>
<details>
<summary><b>allocator_runtime-025</b> Use jemalloc as default global allocator — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** Make jemalloc the default allocator of the node (with in-process arena configuration and an opt-out), since the system allocator fragments and inflates RSS with large long-lived state allocations. Check Lighthouse's global allocator selection and its platform defaults.

**Impact.** Already default with arena tuning, background threads, metrics and opt-out.

**Best measured result.** about 1GB less RAM after a day (pr:lighthouse#2195)

**Evidence (Lighthouse @ 928b61e719).**

- [`lighthouse/Cargo.toml:79-83`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/Cargo.toml#L79-L83) malloc_utils with jemalloc on all non-Windows targets
- [`lighthouse/Cargo.toml:38-39`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/Cargo.toml#L38-L39) sysmalloc opt-out feature
- [`common/malloc_utils/src/jemalloc.rs:16-17`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/malloc_utils/src/jemalloc.rs#L16-L17) #[global_allocator] Jemalloc; metrics for arenas/resident
- [`.cargo/config.toml`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/.cargo/config.toml) JEMALLOC_SYS_WITH_MALLOC_CONF=abort_conf:true,narenas:16
- [`common/malloc_utils/Cargo.toml:37-38`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/malloc_utils/Cargo.toml#L37-L38) background_threads on Linux

**Skeptic check.** Verified jemalloc is the global allocator by default on Linux/macOS with narenas:16 configured and a sysmalloc opt-out; earlier evidence correct (only Windows uses system malloc).

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#2195](https://github.com/sigp/lighthouse/pull/2195), [lighthouse#2222](https://github.com/sigp/lighthouse/pull/2222), [lighthouse#2288](https://github.com/sigp/lighthouse/pull/2288), [lighthouse#3697](https://github.com/sigp/lighthouse/pull/3697), [lighthouse#5995](https://github.com/sigp/lighthouse/pull/5995), [teku#8751](https://github.com/Consensys-Incorporated/teku/pull/8751)

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

**Verdict history.** partial (checked) → partial (refuted)

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

**Verdict history.** not (checked) → partial (refuted)

**Sources.** [teku#10360](https://github.com/Consensys-Incorporated/teku/pull/10360), [teku#10319](https://github.com/Consensys-Incorporated/teku/pull/10319)

</details>


<a id="allocator_runtime-028"></a>
<details>
<summary><b>allocator_runtime-028</b> Tune glibc malloc arenas, mmap threshold, trim — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** When using glibc malloc, set M_MMAP_THRESHOLD (and possibly cap arenas or call malloc_trim) so large state-sized buffers are mmapped and returned to the OS, and apply it only to the beacon node. Check Lighthouse's malloc_utils for mallopt settings and their scope.

**Impact.** Mostly superseded: default builds use jemalloc with narenas capped at 16. The glibc mmap-threshold tuning is still present for sysmalloc builds.

**Best measured result.** memory footprint smaller than with jemalloc, no numbers (pr:lighthouse#2299)

**Evidence (Lighthouse @ 928b61e719).**

- lh-perf-research-base/common/malloc_utils/src/glibc.rs:20 OPTIMAL_MMAP_THRESHOLD = 128K
- [`common/malloc_utils/src/glibc.rs:126-133`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/malloc_utils/src/glibc.rs#L126-L133) configure_glibc_malloc sets M_MMAP_THRESHOLD unless MALLOC_MMAP_THRESHOLD_ is set
- [`lighthouse/src/main.rs:426-440`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/src/main.rs#L426-L440) applied only when subcommand is beacon_node and --disable-malloc-tuning is absent
- [`lighthouse/Cargo.toml:79-80`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/Cargo.toml#L79-L80) jemalloc is the default allocator on non-Windows; glibc tuning only applies with sysmalloc
- lh-perf-research-base/.cargo/config.toml JEMALLOC_SYS_WITH_MALLOC_CONF narenas:16

**Skeptic check.** I confirmed the mallopt threshold and that it is scoped to the beacon node. The earlier evidence was right but did not mention that jemalloc is now the default. I rated value low because glibc is no longer the default path.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#2937](https://github.com/sigp/lighthouse/pull/2937), [lighthouse#2299](https://github.com/sigp/lighthouse/pull/2299), [lighthouse#2398](https://github.com/sigp/lighthouse/pull/2398), [lighthouse#2397](https://github.com/sigp/lighthouse/pull/2397), [lighthouse#2296](https://github.com/sigp/lighthouse/pull/2296)

</details>


<a id="allocator_runtime-029"></a>
<details>
<summary><b>allocator_runtime-029</b> Disable async future tracking in release builds — <i>implemented · low · S · memory</i></summary>

**Idea.** Turn off debug tracking of async futures in default builds because it uses a lot of memory, especially during sync. Check Lighthouse release builds for tokio-console, task tracking or similar instrumentation enabled by default.

**Impact.** Release builds have no async task tracking; nothing to remove.

**Best measured result.** uses a lot of memory, especially during sync (pr:nimbus#1628)

**Evidence (Lighthouse @ 928b61e719).**

- lh-perf-research-base/lighthouse/Cargo.toml:36-37 console-subscriber is an opt-in feature
- [`lighthouse/src/main.rs:712-714`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/src/main.rs#L712-L714) console_subscriber::spawn only under cfg(feature = "console-subscriber")
- [`common/task_executor/src/lib.rs:144-150`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/task_executor/src/lib.rs#L144-L150) task naming only under cfg(tokio_unstable)
- lh-perf-research-base/.cargo/config.toml no tokio_unstable rustflag
- lh-perf-research-base/Cargo.toml:250 tokio features exclude tracing

**Skeptic check.** I confirmed that the console subscriber and tokio_unstable task tracking are both off by default, so the earlier evidence was right. Per-task metrics timers remain, but they are small histograms and do not track futures.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#1628](https://github.com/status-im/nimbus-eth2/pull/1628)

</details>


<a id="allocator_runtime-030"></a>
<details>
<summary><b>allocator_runtime-030</b> Drop memory wiping and copies in hash path — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Remove secure memory wiping and extra copies around digest computation in hashing of public data. Check whether Lighthouse's sha256 wrapper zeroizes contexts or copies inputs for non-secret hashing.

**Impact.** No secure wiping or input copies in the hashing path used by tree_hash/milhouse.

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ethereum_hashing-0.8.0/src/lib.rs:24-40 hash/hash_fixed/hash32_concat thin wrappers
- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ethereum_hashing-0.8.0/src/lib.rs:66-97 ring context; only copy is the 32-byte digest output; no zeroize

**Skeptic check.** Read ethereum_hashing 0.8.0: no zeroize dependency or wipe, inputs passed by slice; hash() returns a Vec but hot paths use hash_fixed/hash32_concat. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus@6f4c7b775](https://github.com/status-im/nimbus-eth2/commit/6f4c7b775cca)

</details>


<a id="allocator_runtime-031"></a>
<details>
<summary><b>allocator_runtime-031</b> Expose native memory as external GC buffers — <i>n/a · low · S · memory, cpu</i></summary>

**Idea.** Hand native memory to the managed runtime as external buffers with a size-reporting finalizer, so the garbage collector does not scan backing memory. Not directly applicable to Lighthouse; check only if Lighthouse exposes memory to a GC'd embedder.

**Impact.** Lighthouse is native Rust with no garbage-collected embedder, so external-buffer handoff does not exist.

**Best measured result.** same GC frequency, less work per cycle; no numbers (commit:lodestar@78e4678df242)

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.toml: no embedder/GC dependency

**Sources.** [lodestar@78e4678df](https://github.com/ChainSafe/lodestar/commit/78e4678df242)

</details>


<a id="allocator_runtime-032"></a>
<details>
<summary><b>allocator_runtime-032</b> Faster HTTP stream implementation for beacon API — <i>n/a · low · S · cpu, latency</i></summary>

**Idea.** Use a faster stream implementation in the HTTP server stack to raise beacon API throughput. Check Lighthouse's HTTP API server (warp/axum/hyper) for throughput limits versus a newer stack.

**Impact.** The idea is replacing Nim chronos' stream type; Lighthouse already runs on hyper/axum, and the beacon API is not a throughput bottleneck.

**Best measured result.** almost 2x http performance (pr:nimbus#8394)

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.toml:114 axum 0.8, :172 hyper 1, :276 warp 0.4 (migration to axum in progress, :304)

**Sources.** [nimbus#8394](https://github.com/status-im/nimbus-eth2/pull/8394)

</details>


<a id="allocator_runtime-033"></a>
<details>
<summary><b>allocator_runtime-033</b> Fewer allocations per async future — <i>n/a · low · S · memory, cpu</i></summary>

**Idea.** Reduce allocations per async future or task, make waiting on already-finished futures cheap, and cancel many futures in one call. Check Lighthouse hot paths that box futures or spawn a task per small item.

**Impact.** The idea targets Nim async future overhead; Rust futures are stack-state machines with no per-future heap allocation unless boxed, and the beacon processor batches work into queues.

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.toml:250 tokio multi-thread runtime; [`beacon_node/beacon_processor/src/lib.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs) uses queued work events, not a task per item

**Sources.** [nimbus#7522](https://github.com/status-im/nimbus-eth2/pull/7522)

</details>


<a id="allocator_runtime-034"></a>
<details>
<summary><b>allocator_runtime-034</b> Fine-grained locking around beacon state — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Replace a coarse lock around beacon state with fine-grained locks so readers and writers in different services contend less. Check Lighthouse for a single RwLock guarding head state or caches that many services take.

**Impact.** States are immutable milhouse values shared via Arc, not guarded by a global state lock; the prysm change (per-field state locks) has no Lighthouse analogue to fix.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:455-468`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L455-L468) separate RwLocks for fork_choice and cached_head plus recompute_head_lock
- [`beacon_node/beacon_chain/src/canonical_head.rs:627-629`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L627-L629) cached_head() clones an Arc snapshot under a short read lock
- [`beacon_node/beacon_chain/src/beacon_chain.rs:422-536`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L422-L536) per-cache locks

**Skeptic check.** Confirmed head reads take a brief read lock and clone an Arc; the remaining wide lock is the fork_choice RwLock, which is a different structure from the prysm state lock idea.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#6922](https://github.com/OffchainLabs/prysm/pull/6922)

</details>


<a id="allocator_runtime-035"></a>
<details>
<summary><b>allocator_runtime-035</b> Fix ownership leaks at the FFI boundary — <i>n/a · medium · memory</i></summary>

**Idea.** At C bindings, pass heap-owning arguments by reference so Drop runs, and free every element of returned vector wrappers, not only the backing pointer. Check Lighthouse FFI code (BLS, KZG, any C bindings) for moved arguments and shallow frees.

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/impls/blst.rs:61-64`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L61-L64) only unsafe is scalar init, no ownership transfer
- [`crypto/kzg/Cargo.toml:22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/kzg/Cargo.toml#L22) uses rust_eth_kzg safe Rust API; BLS via blst crate

**Sources.** [grandine@5cf4db0ea](https://github.com/grandinetech/grandine/commit/5cf4db0eaffb), [grandine#707](https://github.com/grandinetech/grandine/pull/707), [grandine@927eb7830](https://github.com/grandinetech/grandine/commit/927eb78307f3)

</details>


<a id="allocator_runtime-036"></a>
<details>
<summary><b>allocator_runtime-036</b> Fix snappy stream leak in req/resp — <i>n/a · low · S · memory</i></summary>

**Idea.** Update the snappy streaming codec to fix a memory leak in req/resp compression streams, and cap incoming connections at the transport level. Check Lighthouse's snappy codec use in rpc for retained per-stream state.

**Impact.** Leak was in a JS/C codec binding; Lighthouse's Rust snap codec keeps no per-stream state beyond the message, and the length limit is applied via limit_reader.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/codec.rs:127`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L127),187 - FrameEncoder/FrameDecoder created per message and dropped
- Cargo.toml:238 - snap 1.1.2 (Rust, no C binding)

**Sources.** [lodestar#5001](https://github.com/ChainSafe/lodestar/pull/5001), [lodestar#5006](https://github.com/ChainSafe/lodestar/pull/5006)

</details>


<a id="allocator_runtime-037"></a>
<details>
<summary><b>allocator_runtime-037</b> Fix stack collector memory leak — <i>n/a · low · S · memory</i></summary>

**Idea.** Update the backtrace/stack collection library to fix a memory leak. Check whether Lighthouse captures backtraces on hot paths (errors, panics hooks) and whether that leaks.

**Impact.** Backtraces are captured only on panic, never on hot paths; the leak was in a Nim library.

**Evidence (Lighthouse @ 928b61e719).**

- [`lighthouse/src/main.rs:732`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/src/main.rs#L732) - Backtrace::capture only inside the panic hook
- [`lighthouse/src/main.rs:96-102`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/src/main.rs#L96-L102) - RUST_BACKTRACE=1 set at startup

**Sources.** [nimbus#7791](https://github.com/status-im/nimbus-eth2/pull/7791)

</details>


<a id="allocator_runtime-038"></a>
<details>
<summary><b>allocator_runtime-038</b> Destroy thread-pool task objects after run — <i>n/a · low · S · memory</i></summary>

**Idea.** Make sure task objects in the thread pool used for signature verification are freed after running, to avoid a per-task leak. Check Lighthouse's signature verification job dispatch for retained task state.

**Impact.** Rust closures are dropped after execution; no manual task-object destruction exists to forget.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:1657-1676`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1657-L1676) - signature work runs as spawn_blocking closures, owned and dropped after run

**Sources.** [nimbus#2920](https://github.com/status-im/nimbus-eth2/pull/2920)

</details>


<a id="allocator_runtime-039"></a>
<details>
<summary><b>allocator_runtime-039</b> Avoid nested thread pool oversubscription — <i>partial · low · S · cpu</i></summary>

**Idea.** Avoid running several parallel runtimes at once (for example rayon inside state transition plus a solver's own threads), which oversubscribes CPUs; use one pool or plain threads. Check Lighthouse for rayon work nested inside tokio blocking tasks or other pools.

**Gap in Lighthouse.** Pools are sized separately (80%+25% of CPUs, plus the global pool and tokio blocking threads), so total runnable threads can exceed core count when several are busy. A single shared budget or sizing the pools to sum to num_cpus would remove it.

**Impact.** Small reduction in context switching during KZG/column work bursts; measured effect unknown, likely marginal.

**Evidence (Lighthouse @ 928b61e719).**

- [`common/task_executor/src/rayon_pool_provider.rs:24-41`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/task_executor/src/rayon_pool_provider.rs#L24-L41) - two extra rayon pools (25% and 80% of CPUs) plus the global rayon pool
- [`beacon_node/beacon_chain/src/kzg_utils.rs:344-477`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L344-L477) - par_iter on global pool from blocking tasks
- [`beacon_node/beacon_processor/src/lib.rs:1657`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1657) - spawn_blocking worker threads

**Sources.** [grandine@588675734](https://github.com/grandinetech/grandine/commit/5886757344cd)

</details>


<a id="allocator_runtime-040"></a>
<details>
<summary><b>allocator_runtime-040</b> Release large init-time temporaries after startup — <i>implemented · low · S · memory, startup</i></summary>

**Idea.** Drop large temporaries created during node initialization so they are not referenced for the process lifetime, and reuse a single validator pool instance. Check Lighthouse startup (genesis/checkpoint load, builder) for large values kept in long-lived structs.

**Impact.** No large init-time temporaries are kept for the process lifetime. Only a temporary startup peak remains, from cloning the checkpoint bytes.

**Evidence (Lighthouse @ 928b61e719).**

- lh-perf-research-base/beacon_node/client/src/builder.rs:343,386 genesis_state is local and moved into the chain builder
- [`beacon_node/client/src/builder.rs:388-420`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L388-L420) the WeakSubjSszBytes anchor bytes are decoded into locals and dropped after the builder call
- [`beacon_node/client/src/lib.rs:21-28`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/lib.rs#L21-L28) Client keeps only the chain Arc, network globals and listen addresses, not the config
- [`common/eth2_network_config/src/lib.rs:50-53`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2_network_config/src/lib.rs#L50-L53),86 genesis_state_bytes is a &amp;'static slice for hardcoded nets
- [`beacon_node/src/lib.rs:52`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/lib.rs#L52),125 client_config.genesis is cloned twice during startup (a temporary startup peak, dropped when building finishes)

**Skeptic check.** I confirmed that genesis and checkpoint state values are dropped after building and that Client does not keep the config. The earlier evidence was right. The Arc&lt;Eth2NetworkConfig&gt; that stays in RuntimeContext keeps only the trusted setup bytes and, for hardcoded nets, a static genesis slice.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus@0dbc7162a](https://github.com/status-im/nimbus-eth2/commit/0dbc7162ac44), [nimbus#2352](https://github.com/status-im/nimbus-eth2/pull/2352)

</details>


<a id="allocator_runtime-041"></a>
<details>
<summary><b>allocator_runtime-041</b> Pool gossip decompression buffers per topic — <i>not · low · M · memory, cpu</i></summary>

**Idea.** Keep a per-topic pool of reusable output buffers for decompressing inbound gossip on the network thread, instead of allocating a new buffer per message. Check Lighthouse's gossipsub snappy transform for per-message Vec allocation.

**Gap in Lighthouse.** In SnappyTransform::inbound_transform, the decompressed Vec is moved into the Message and kept by gossipsub and the beacon processor, so a pool would need buffer return on drop. Gain is limited to malloc cost for blocks/blobs/attestations; a thread-local reusable Decoder would save only the small decoder setup.

**Impact.** Saves one allocation per gossip message (the exact-size Vec); glibc/jemalloc handles this well, so gain is small.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/pubsub.rs:122-123`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L122-L123) - new Decoder and decompress_vec allocate a fresh Vec per inbound message
- [`beacon_node/lighthouse_network/src/types/pubsub.rs:129`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L129) - the Vec becomes Message.data and is owned downstream

**Sources.** [lodestar#8634](https://github.com/ChainSafe/lodestar/pull/8634)

</details>


<a id="allocator_runtime-042"></a>
<details>
<summary><b>allocator_runtime-042</b> Reuse SHA-256 hasher without per-call allocation — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Hash with one-shot functions on stack buffers or a pooled reusable hasher instead of allocating a hasher object per call in tree hashing. Check whether Lighthouse's hash32_concat and tree-hash paths allocate a Vec or hasher per hash.

**Impact.** Already allocation-free per hash on the milhouse and tree_hash hot paths.

**Best measured result.** Sha256(32B,32B) 78.2 -&gt; 52.1 ns, 2 allocs -&gt; 0 (pr:caplin#22489); pooled 77.30 -&gt; 47.65 ns/op (pr:prysm#15427)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/registry/src/*/ethereum_hashing-0.8.0/src/lib.rs:36-41 hash32_concat uses a stack DynamicContext and returns [u8;32]
- ethereum_hashing-0.8.0/src/lib.rs:31-33 hash_fixed returns an array
- ~/.cargo/git/checkouts/milhouse-*/d67aabd/src/tree.rs:544 milhouse internal nodes use hash32_concat
- ~/.cargo/git/checkouts/tree_hash-*/e5ea187/tree_hash/src/merkle_hasher.rs:141-151,200-203 MerkleHasher uses SmallVec buffers, one per merkleization, not per hash
- tree_hash merkleize_padded.rs:82-139 uses hash_fixed and hash32_concat

**Skeptic check.** I checked the callers in milhouse and tree_hash, not only the hashing crate. They use the stack-based functions. The only function that returns a Vec, hash(), is used by merkleize_standard, which is not the hot path.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#22489](https://github.com/erigontech/erigon/pull/22489), [prysm#15427](https://github.com/OffchainLabs/prysm/pull/15427)

</details>


<a id="allocator_runtime-043"></a>
<details>
<summary><b>allocator_runtime-043</b> Lazy split iterators instead of split slices — <i>n/a · low · S · memory</i></summary>

**Idea.** Use lazy split iterators instead of functions that build an intermediate slice of substrings in loops. Check Lighthouse parsing paths that collect split() results into Vec only to iterate.

**Impact.** Rust split is already lazy and no hot-path code collects split results only to iterate.

**Evidence (Lighthouse @ 928b61e719).**

- beacon_node, common, lighthouse, boot_node - grep for split(...).collect::&lt;Vec found no non-test hits

**Sources.** [caplin#22163](https://github.com/erigontech/erigon/pull/22163)

</details>


<a id="allocator_runtime-044"></a>
<details>
<summary><b>allocator_runtime-044</b> Cap network library direct buffer memory — <i>partial · low · S · memory</i></summary>

**Idea.** Set an explicit cap on the network library's off-heap buffer memory because the default bound is effectively far larger than needed. Check Lighthouse libp2p/yamux buffer and window limits for oversized defaults.

**Gap in Lighthouse.** Yamux is left at defaults (1 GiB per-connection receive window, 512 streams) while mplex has explicit caps. Buffers only grow if the peer sends data without being read, but a malicious peer could hold up to 1 GiB per connection. Call set_max_connection_receive_window(Some(..)) and set_max_num_streams in the yamux config.

**Impact.** Bounds worst-case per-connection memory; no change for honest peers, so a robustness gain rather than a speed gain.

**Best measured result.** default effectively allocates 256MB; capped at 32MB (pr:teku#2424)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/utils.rs:44`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/utils.rs#L44) - yamux::Config::default() with no limits set
- yamux-0.14.1/src/lib.rs:89-90 - defaults: connection receive window 1 GiB, 512 streams
- [`beacon_node/lighthouse_network/src/service/utils.rs:50-51`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/utils.rs#L50-L51) - mplex does get max streams 32 and ResetStream

**Sources.** [teku#2424](https://github.com/Consensys-Incorporated/teku/pull/2424)

</details>


<a id="allocator_runtime-045"></a>
<details>
<summary><b>allocator_runtime-045</b> Linked-list or deque FIFO job queues — <i>implemented · low · S · cpu</i></summary>

**Idea.** Back FIFO job queues with a structure that pops from the front in O(1) instead of an array whose shift is O(n). Check Lighthouse beacon processor queues for Vec::remove(0) style front removal.

**Impact.** Beacon processor queues are O(1) at the front.

**Best measured result.** array shift 3.6us/op vs list 14ns/op at 16000 items; shift up to 17% CPU (pr:lodestar#3738)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_queue.rs:31-60`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_queue.rs#L31-L60) FifoQueue on VecDeque push_back/pop_front
- [`beacon_node/beacon_processor/src/scheduler/work_queue.rs:77-88`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_queue.rs#L77-L88),237-246 PeerWork and LifoQueue also VecDeque

**Skeptic check.** All beacon processor job queues are VecDeque. Vec::remove(0) remains on small libp2p event buffers (rpc/mod.rs:150,561 events Vec; handler.rs SmallVec&lt;4&gt;), which are drained every poll and are not job queues.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#3738](https://github.com/ChainSafe/lodestar/pull/3738)

</details>


<a id="allocator_runtime-046"></a>
<details>
<summary><b>allocator_runtime-046</b> Bounded queue with internal locking for throttling — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Implement the throttling task queue as one bounded channel that carries the limit itself, instead of an unbounded queue guarded by external locks, to cut contention between producers and workers. Check Lighthouse's beacon processor work queues for external Mutex around queue plus counter.

**Impact.** Producer/worker handoff is a bounded channel with the limit inside; queues are single-owner so no external lock contention.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:148-149`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L148-L149) bounded mpsc::channel(max_work_event_queue_len)
- [`beacon_node/beacon_processor/src/scheduler/work_queue.rs:31-60`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_queue.rs#L31-L60) per-type bounded FifoQueue owned by the single manager task, no lock
- [`beacon_node/beacon_processor/src/lib.rs:170-182`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L170-L182) only Mutex is the DuplicateCache HashSet

**Skeptic check.** Verified the manager owns all queues and producers only touch the bounded tokio channel; earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#9848](https://github.com/Consensys-Incorporated/teku/pull/9848)

</details>


<a id="allocator_runtime-047"></a>
<details>
<summary><b>allocator_runtime-047</b> Set heap limit near real usage to fail fast — <i>n/a · low · S · memory</i></summary>

**Idea.** Set the runtime heap limit close to real usage so a memory bug crashes with OOM instead of causing long GC stalls. For Lighthouse the analogue is a memory limit or watchdog that fails fast instead of swapping.

**Impact.** No GC heap in Rust; a leak is bounded by the OS/cgroup OOM killer already.

**Best measured result.** old space 1.5-2GB; limit 6000 to 4096 MB (pr:lodestar#3516)

**Evidence (Lighthouse @ 928b61e719).**

- [`common/malloc_utils/src/lib.rs:1-20`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/malloc_utils/src/lib.rs#L1-L20) allocator is jemalloc/glibc, no managed heap

**Sources.** [lodestar#3516](https://github.com/ChainSafe/lodestar/pull/3516)

</details>


<a id="allocator_runtime-048"></a>
<details>
<summary><b>allocator_runtime-048</b> Raise runtime heap limit for memory spikes — <i>n/a · low · S · memory, cpu</i></summary>

**Idea.** Raise the default runtime heap ceiling so non-finality or DoS memory spikes do not crash the node or thrash the GC. Not directly applicable to Lighthouse, which has no managed heap limit.

**Impact.** No V8-style heap ceiling exists in Lighthouse.

**Evidence (Lighthouse @ 928b61e719).**

- [`common/malloc_utils/src/lib.rs:1-20`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/malloc_utils/src/lib.rs#L1-L20) native allocator, no heap ceiling

**Sources.** [lodestar#2424](https://github.com/ChainSafe/lodestar/pull/2424), [lodestar#6343](https://github.com/ChainSafe/lodestar/pull/6343), [lodestar#6345](https://github.com/ChainSafe/lodestar/pull/6345), [lodestar#2893](https://github.com/ChainSafe/lodestar/pull/2893), [lodestar#2891](https://github.com/ChainSafe/lodestar/pull/2891)

</details>


<a id="allocator_runtime-049"></a>
<details>
<summary><b>allocator_runtime-049</b> Reduce stack usage of light-client data store — <i>n/a · low · S · memory</i></summary>

**Idea.** Change how large objects are passed or held in the light-client data store so they do not sit on the stack. Check Lighthouse light-client server code for large values passed by value through deep call chains.

**Impact.** Nim stack/GC-specific; light client server objects are small and Arc/moved in Rust.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/light_client_finality_update_verification.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_finality_update_verification.rs) light client path; Rust stack-use concern is Nim-specific

**Sources.** [nimbus#7067](https://github.com/status-im/nimbus-eth2/pull/7067)

</details>


<a id="allocator_runtime-050"></a>
<details>
<summary><b>allocator_runtime-050</b> Allocate startup block summaries outside GC heap — <i>n/a · low · S · memory</i></summary>

**Idea.** Allocate the large startup table of block summaries with manual allocation outside the managed heap to lower memory. Check how Lighthouse holds block summary tables built at startup (fork choice, block roots).

**Impact.** Nothing to move out of a GC heap; Rust has none.

**Evidence (Lighthouse @ 928b61e719).**

- [`common/malloc_utils/src/lib.rs:1-20`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/malloc_utils/src/lib.rs#L1-L20) no managed GC heap; tables live in native allocator already

**Sources.** [nimbus#3270](https://github.com/status-im/nimbus-eth2/pull/3270)

</details>


<a id="allocator_runtime-051"></a>
<details>
<summary><b>allocator_runtime-051</b> Upgrade network library adaptive buffer allocator — <i>n/a · low · S · memory</i></summary>

**Idea.** Upgrade the networking library to a version whose adaptive byte buffer allocator has much lower memory overhead. Check Lighthouse libp2p buffer allocation strategy and version.

**Impact.** Netty-specific; rust-libp2p uses per-read buffers, no adaptive allocator to upgrade.

**Best measured result.** decrease memory overhead dramatically, upstream claim (pr:teku#9669)

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.lock:5779-5780 libp2p 0.57.0 (Rust, no Netty-style adaptive pooled allocator)

**Sources.** [teku#9669](https://github.com/Consensys-Incorporated/teku/pull/9669)

</details>


<a id="allocator_runtime-052"></a>
<details>
<summary><b>allocator_runtime-052</b> Newer runtime GC with soft heap target — <i>partial · low · M · memory</i></summary>

**Idea.** Run on a newer VM with a better garbage collector and a soft max heap target that can be exceeded when necessary. Not directly applicable to Lighthouse; the analogue is a soft memory target in the allocator.

**Gap in Lighthouse.** Lighthouse tunes jemalloc/glibc (arena count, trim) but has no soft memory target that scales decay with usage; would need a periodic task in malloc_utils reading RSS and adjusting purge/trim.

**Impact.** Marginal RSS reduction on some nodes; no GC cost to avoid.

**Best measured result.** lower memory usage without risk of high GC costs (pr:teku#2382)

**Evidence (Lighthouse @ 928b61e719).**

- [`common/malloc_utils/src/lib.rs:1-20`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/malloc_utils/src/lib.rs#L1-L20) jemalloc feature or glibc, selectable
- [`common/malloc_utils/src/glibc.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/malloc_utils/src/glibc.rs) glibc arena/trim tuning

**Sources.** [teku#2382](https://github.com/Consensys-Incorporated/teku/pull/2382)

</details>


<a id="allocator_runtime-053"></a>
<details>
<summary><b>allocator_runtime-053</b> Park idle worker threads instead of spinning — <i>n/a · low · S · cpu</i></summary>

**Idea.** Park idle worker threads until a wake signal or short timeout instead of busy-spinning when no work is queued. Check Lighthouse worker loops and any custom pools for spin or tight polling.

**Impact.** No busy-spin loops exist; tokio and rayon park idle workers. Nothing to gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/timer/src/lib.rs:24`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/timer/src/lib.rs#L24) sleep-based loop
- grep spin_loop/park_timeout/thread::spawn in beacon_node, common: none
- work_reprocessing_queue.rs yield_now only in tests

**Sources.** [silver#123](https://github.com/gattaca-com/silver/pull/123)

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


<a id="allocator_runtime-056"></a>
<details>
<summary><b>allocator_runtime-056</b> Preallocate collections with known capacity — <i>partial · low · S · memory, cpu</i></summary>

**Idea.** Give vectors and maps their known capacity up front instead of growing them by repeated reallocation. Check Lighthouse hot paths for Vec::new followed by push in loops of known length.

**Gap in Lighthouse.** A few Vec::new-then-push loops (single_pass.rs added_validators, upgrade/gloas.rs pending_deposits/builders) could use with_capacity; no hot spot measured.

**Impact.** Micro-gain from fewer reallocs on rare paths; unmeasurable on a mainnet node.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:396`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L396) Vec::new then push
- [`consensus/state_processing/src/upgrade/gloas.rs:250`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/upgrade/gloas.rs#L250) Vec::new in loop

**Sources.** [prysm#11317](https://github.com/OffchainLabs/prysm/pull/11317), [prysm#6517](https://github.com/OffchainLabs/prysm/pull/6517)

</details>


<a id="allocator_runtime-057"></a>
<details>
<summary><b>allocator_runtime-057</b> Precompute shuffled committees off the hot path — <i>implemented · medium · S · memory, cpu</i></summary>

**Idea.** Compute committee shufflings for previous, current and next epoch ahead of time and drop large per-slot allocations (~16MB every 12s). Check whether Lighthouse rebuilds committee structures per slot or caches them per epoch.

**Impact.** Shufflings are computed once per epoch, ahead of time, and shared through an Arc. Nothing is rebuilt per slot.

**Evidence (Lighthouse @ 928b61e719).**

- lh-perf-research-base/beacon_node/beacon_chain/src/state_advance_timer.rs:333-339 builds the Current and Next committee caches before the slot
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:397-411`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L397-L411) inserts the Next-epoch cache into shuffling_cache
- [`consensus/types/src/state/beacon_state.rs:825`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L825) committee_caches: [Arc&lt;CommitteeCache&gt;; CACHED_EPOCHS]
- [`consensus/types/src/state/beacon_state.rs:2824-2836`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2824-L2836) build_committee_cache does nothing if already initialised for that epoch
- [`consensus/state_processing/src/per_epoch_processing/altair.rs:30-32`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/altair.rs#L30-L32) builds the caches once per epoch

**Skeptic check.** I confirmed the precompute by the state advance timer and the guard that skips a rebuild when the cache is initialised. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#18522](https://github.com/erigontech/erigon/pull/18522)

</details>


<a id="allocator_runtime-058"></a>
<details>
<summary><b>allocator_runtime-058</b> Prover on system allocator instead of bump arena — <i>n/a · low · S · memory, bandwidth, cpu</i></summary>

**Idea.** Run the prover on the system allocator rather than a bump arena so resident memory does not ratchet up over the node's lifetime. Check whether Lighthouse uses bump or arena allocators whose memory is never returned.

**Impact.** Lighthouse has no prover and no arena allocator, so memory is returned normally.

**Evidence (Lighthouse @ 928b61e719).**

- [`common/malloc_utils/src/lib.rs:1`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/malloc_utils/src/lib.rs#L1) only jemalloc or glibc
- grep bump/bumpalo in repo: no hits

**Sources.** [ethlambda#539](https://github.com/lambdaclass/ethlambda/pull/539)

</details>


<a id="allocator_runtime-059"></a>
<details>
<summary><b>allocator_runtime-059</b> Scoped bump arena only for proving threads — <i>n/a · low · M · cpu</i></summary>

**Idea.** Use a bump-arena allocator only on proving threads, reset per phase, while all other threads use the system allocator. Check whether Lighthouse could use scoped arenas for short-lived heavy jobs such as epoch processing.

**Impact.** No proving threads; epoch processing relies on milhouse sharing and the global allocator, and arenas there are not a known win.

**Best measured result.** p50 aggregation 203 ms in a 1019-slot devnet, no baseline (pr:ethlambda#412)

**Evidence (Lighthouse @ 928b61e719).**

- grep bumpalo/arena: no hits
- [`common/malloc_utils/src/lib.rs:1`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/malloc_utils/src/lib.rs#L1) global allocator only

**Sources.** [ethlambda#412](https://github.com/lambdaclass/ethlambda/pull/412)

</details>


<a id="allocator_runtime-060"></a>
<details>
<summary><b>allocator_runtime-060</b> Reclaim receive buffers, slab allocator for packets — <i>implemented · low · S · cpu, latency, memory</i></summary>

**Idea.** Clear receive buffers before trying to reclaim them so reuse succeeds instead of allocating per packet batch, use a slab-style allocator for many small allocations, and poll the socket before the p2p state machine. Check Lighthouse discv5/QUIC receive paths for per-batch buffer allocation.

**Impact.** No per-packet buffer allocation on the discv5 receive path; discovery traffic is light, so remaining small copies do not matter.

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/discv5-0.12.0/src/socket/recv.rs:124-137 two stack buffers [0; MAX_PACKET_SIZE] allocated once and reused by recv_from in the loop
- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/discv5-0.12.0/src/socket/recv.rs:203-212 decode reads &amp;recv_buffer[..length]; to_vec only for unrecognized frames

**Skeptic check.** Confirmed discv5 0.12.0 (Cargo.lock) reuses two fixed receive buffers for the life of the recv task. The earlier evidence was right; the slab-allocator and poll-order parts are Go/Nim runtime details with no Rust analogue here.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [silver#55](https://github.com/gattaca-com/silver/pull/55)

</details>


<a id="allocator_runtime-061"></a>
<details>
<summary><b>allocator_runtime-061</b> Release allocator instead of debug allocator — <i>n/a · low · S · cpu, memory</i></summary>

**Idea.** Use the production allocator for long-lived state views in release builds instead of a debug allocator with tracking overhead. Check Lighthouse release profiles for debug or tracking allocators enabled.

**Impact.** Rust release builds have no tracking debug allocator; jemalloc-profiling is opt-in only.

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.toml:286 maxperf/release-debug inherit release
- [`common/malloc_utils/src/lib.rs:1`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/malloc_utils/src/lib.rs#L1) jemalloc on unix, glibc otherwise

**Sources.** [lodestar@f83914b3e](https://github.com/ChainSafe/lodestar/commit/f83914b3e360)

</details>


<a id="allocator_runtime-062"></a>
<details>
<summary><b>allocator_runtime-062</b> Avoid reference cycles that leak memory — <i>not · low · S · memory</i></summary>

**Idea.** Remove annotations or patterns that make cyclic references uncollectable, which leaked memory. Check Lighthouse for Arc cycles in caches or service handles that are never broken.

**Gap in Lighthouse.** No leak found; an audit of chain-owned tasks holding Arc&lt;BeaconChain&gt; (spawn_timer, graffiti_calculator) would be needed, using Weak where a cycle exists.

**Impact.** Prevents rare leaks only; nothing known leaks and services live for the whole process.

**Evidence (Lighthouse @ 928b61e719).**

- grep Weak&lt; in beacon_node/common: only task_executor/src/lib.rs:42 Weak&lt;Runtime&gt;
- Services hold Arc&lt;BeaconChain&gt;; no cycle seen but none guarded

**Sources.** [nimbus#1011](https://github.com/status-im/nimbus-eth2/pull/1011)

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


<a id="allocator_runtime-064"></a>
<details>
<summary><b>allocator_runtime-064</b> Shared constant zero hash instead of temporaries — <i>implemented · low · S · cpu</i></summary>

**Idea.** Pass a shared constant zero hash to calls instead of constructing and zero-filling a 32-byte temporary at each call site in hot paths. Check Lighthouse tree hashing for Hash256::zero() built in loops instead of a static.

**Impact.** Zero hashes are shared statics or consts; in Rust, a const Hash256::ZERO costs nothing extra.

**Best measured result.** saves a 32-byte zero fill per call, no timing (pr:nimbus#3770)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/tree_hash-*/e5ea187/tree_hash/src/merkleize_padded.rs:125,284 get_zero_hash returns a reference into static ZERO_HASHES
- tree_hash/src/merkle_hasher.rs:372 zero_hash returns Preimage&lt;'static&gt;
- ~/.cargo/git/checkouts/milhouse-*/d67aabd/src/tree.rs:4 uses static ethereum_hashing::ZERO_HASHES
- ethereum_hashing-0.8.0/src/lib.rs zero_hash_cache LazyLock ZERO_HASHES

**Skeptic check.** I confirmed static zero-hash tables in tree_hash and milhouse. The earlier evidence was right, but its line citations point to the registry tree_hash 0.12.1, while the lock file uses a git checkout at rev e5ea187.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#3770](https://github.com/status-im/nimbus-eth2/pull/3770)

</details>


<a id="allocator_runtime-065"></a>
<details>
<summary><b>allocator_runtime-065</b> Reuse and stop timers in loops — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** In loops and debounce helpers, keep one reusable timer or ticker and stop or reset it, instead of creating a new timer per iteration or event that lives until it fires. Check Lighthouse loops for tokio::time::sleep created per iteration inside select! where an Interval would do.

**Impact.** tokio Sleep is freed on drop, so the Go time.After leak cannot happen; the remaining per-slot sleeps run once per slot.

**Best measured result.** time.After channel is not freed until the event fires (pr:prysm#7175)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/timer/src/lib.rs:24`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/timer/src/lib.rs#L24) one sleep per slot, awaited and dropped
- [`beacon_node/network/src/service.rs:935`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L935) next_unsubscribe Sleep stored and reset, not recreated per select iteration
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:1441`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L1441) backfill event Sleep stored in a field

**Skeptic check.** Grepped all sleep( calls in beacon_node/common/validator_client: every one is per slot or per event and stored or awaited, none is recreated per select! iteration on a hot loop. The earlier verdict holds.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#7175](https://github.com/OffchainLabs/prysm/pull/7175), [prysm#13800](https://github.com/OffchainLabs/prysm/pull/13800), [prysm#7189](https://github.com/OffchainLabs/prysm/pull/7189), [prysm#7190](https://github.com/OffchainLabs/prysm/pull/7190)

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

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [lighthouse#10391](https://github.com/sigp/lighthouse/pull/10391)

</details>


<a id="allocator_runtime-067"></a>
<details>
<summary><b>allocator_runtime-067</b> Shared memory messaging between worker threads — <i>n/a · low · S · latency, cpu</i></summary>

**Idea.** Pass messages between worker and main thread through shared memory with atomics instead of copying them. Check Lighthouse cross-thread channels that clone or serialize large payloads instead of sharing an Arc.

**Impact.** None: Rust threads share memory; payloads move by ownership or Arc, no structured clone.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:143`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L143) tokio mpsc channels in one address space

**Sources.** [lodestar#8672](https://github.com/ChainSafe/lodestar/pull/8672)

</details>


<a id="allocator_runtime-068"></a>
<details>
<summary><b>allocator_runtime-068</b> Skip expensive direct buffer cleaning — <i>n/a · low · S · memory</i></summary>

**Idea.** Configure the pooled network buffer runtime to skip its costly buffer cleaner path for stability after OOMs. Relevant to Lighthouse only if it uses a comparable pooled-buffer runtime.

**Impact.** None: no Netty-style buffer cleaner exists.

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.toml:177 libp2p with tokio TCP/QUIC, no pooled direct-buffer runtime

**Sources.** [teku#10593](https://github.com/Consensys-Incorporated/teku/pull/10593)

</details>


<a id="allocator_runtime-069"></a>
<details>
<summary><b>allocator_runtime-069</b> Schedule job runs only below max concurrency — <i>n/a · low · S · cpu</i></summary>

**Idea.** When pushing to a job queue, schedule a run only if running jobs are below max concurrency, since running jobs pull the next item themselves. Check Lighthouse beacon processor for redundant wakeups or spawns per enqueued item.

**Impact.** Already done: a single manager loop owns the queues and spawns a worker only when under max_workers; no per-item wakeup.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:890`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L890) can_spawn = current_workers &lt; max_workers
- [`beacon_node/beacon_processor/src/lib.rs:1193`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1193) spawn_worker only on a dequeued event or when a queue pop yields work

**Sources.** [lodestar#3800](https://github.com/ChainSafe/lodestar/pull/3800)

</details>


<a id="allocator_runtime-070"></a>
<details>
<summary><b>allocator_runtime-070</b> Native slice-to-array conversion for byte copies — <i>n/a · low · S · cpu, memory</i></summary>

**Idea.** Convert byte slices to fixed 32-byte arrays with the native slice-to-array conversion instead of allocate-plus-copy loops in hot helpers. Check Lighthouse for Hash256::from_slice patterns that go through intermediate Vec.

**Impact.** None: Rust Hash256::from_slice is a direct copy; the Go allocate-plus-copy loop does not exist.

**Best measured result.** BenchmarkToBytes32 0.4843 -&gt; 0.2438 ns/op (pr:prysm#11838)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/config.rs:479`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L479) extend_from_slice used for message id, not a Vec to array path

**Sources.** [prysm#12608](https://github.com/OffchainLabs/prysm/pull/12608), [prysm#11838](https://github.com/OffchainLabs/prysm/pull/11838)

</details>


<a id="allocator_runtime-071"></a>
<details>
<summary><b>allocator_runtime-071</b> Configurable executor thread counts and queue sizes — <i>partial · low · S · cpu, latency</i></summary>

**Idea.** Make async worker thread counts and queue sizes configurable so large hosts can tune parallelism. Check whether Lighthouse exposes tokio worker count and beacon processor queue lengths as flags.

**Gap in Lighthouse.** Processor workers and queue lengths are flags, but tokio worker_threads and max_blocking_threads are not; only tokio's TOKIO_WORKER_THREADS env var works. Add flags in EnvironmentBuilder::multi_threaded_tokio_runtime.

**Impact.** Lets hosts with many cores or containers cap or raise tokio threads; benefit is tuning, not a default speed-up.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/src/cli.rs:1618`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L1618) --beacon-processor-max-workers
- [`beacon_node/src/cli.rs:1630`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L1630) --beacon-processor-work-queue-len
- [`lighthouse/environment/src/lib.rs:172`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/environment/src/lib.rs#L172) RuntimeBuilder::new_multi_thread() with defaults, no worker or blocking thread flag

**Sources.** [teku#7611](https://github.com/Consensys-Incorporated/teku/pull/7611)

</details>


<a id="allocator_runtime-072"></a>
<details>
<summary><b>allocator_runtime-072</b> Allocate buffers uninitialized when immediately overwritten — <i>partial · low · S · cpu, memory</i></summary>

**Idea.** Allocate sequences without zero-initialization when they are overwritten right away, such as network and era file read buffers and fork choice tracker arrays. Check Lighthouse for vec![0u8; n] buffers that are fully overwritten by a read.

**Gap in Lighthouse.** Snappy decode buffers are zero-filled then fully overwritten. Could use Vec::with_capacity plus take().read_to_end, avoiding the memset in rpc/codec.rs decode paths.

**Impact.** Saves one memset per RPC message decode (up to a few MB for blocks/columns); marginal next to snappy decode cost.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/codec.rs:188`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L188) vec![0; length] then read_exact (also 283, 319)

**Sources.** [nimbus#7098](https://github.com/status-im/nimbus-eth2/pull/7098), [nimbus#7109](https://github.com/status-im/nimbus-eth2/pull/7109)

</details>


<a id="allocator_runtime-073"></a>
<details>
<summary><b>allocator_runtime-073</b> Green threads for event-channel consumers — <i>n/a · low · S · memory, cpu, latency</i></summary>

**Idea.** Run each event-channel consumer on a lightweight task instead of a dedicated OS thread, so many subscriber channels do not each hold a thread stack. Check Lighthouse for std::thread::spawn per service or channel consumer that could be an async task.

**Impact.** Lighthouse consumers are tokio tasks already; no thread-per-subscriber.

**Best measured result.** ~70 fewer platform threads x ~1MB stack = ~70MB less committed memory (pr:teku#10426)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/builder_store/src/lib.rs:365`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/builder_store/src/lib.rs#L365) only std::thread::spawn outside tests
- grep of std::thread::spawn/Builder across repo: no per-channel consumer threads in beacon node

**Sources.** [teku#10426](https://github.com/Consensys-Incorporated/teku/pull/10426), [teku#10950](https://github.com/Consensys-Incorporated/teku/pull/10950)

</details>


<a id="allocator_runtime-074"></a>
<details>
<summary><b>allocator_runtime-074</b> Write small messages directly when queue empty — <i>not · low · M · latency</i></summary>

**Idea.** Write small outgoing messages such as attestations directly to the socket when the write queue is empty, bypassing the queue. Check Lighthouse's libp2p send path for queueing overhead on small gossip messages.

**Gap in Lighthouse.** Gossipsub in the sigp libp2p fork always goes through the per-peer queue, then the handler; a bypass would need to be in the fork's behaviour send path. The queue is a cheap in-memory push.

**Impact.** Would save at most one task wakeup per small message; the socket write still goes via yamux and the handler, so gain is tiny.

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/queue.rs:63 try_push always enqueues to priority/non_priority queues
- gossipsub handler.rs polls queue then Sink::start_send

**Sources.** [nimbus#3172](https://github.com/status-im/nimbus-eth2/pull/3172)

</details>


<a id="allocator_runtime-075"></a>
<details>
<summary><b>allocator_runtime-075</b> Do not yield while holding state references — <i>n/a · low · S · memory</i></summary>

**Idea.** Avoid suspending (await/yield) inside state transition while holding references to states, because the suspended scope keeps them alive; yield in the caller after they are dropped. Check Lighthouse async functions that hold BeaconState values across await points.

**Impact.** Rust drops values deterministically; no GC-style retention of suspended scopes, so no memory gain.

**Best measured result.** memory 4GB after 1h down to 1.1-1.8GB (pr:lodestar#2011)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:121`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L121) awaits are sleeps, no state held

**Sources.** [lodestar#2011](https://github.com/ChainSafe/lodestar/pull/2011)

</details>


<a id="allocator_runtime-076"></a>
<details>
<summary><b>allocator_runtime-076</b> Avoid formatter allocations for simple string conversions — <i>not · low · S · memory, cpu</i></summary>

**Idea.** Replace format!-style calls that only convert or join simple values with direct string building or integer-to-string helpers on hot paths. Check Lighthouse hot paths for format!/to_string used only to concatenate or stringify integers, which allocate through the formatter.

**Gap in Lighthouse.** Only replace format!/to_string in per-message paths (e.g. GossipTopic Display/String conversion if called per publish); no hot-path hit was identified.

**Impact.** Negligible: remaining format! uses are in error paths and topic construction, not per-message processing.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/topics.rs:340`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/topics.rs#L340) Display for GossipTopic uses format! (topic strings)
- [`beacon_node/lighthouse_network/src/types/topics.rs:352`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/topics.rs#L352) format! for attestation subnet topic
- [`beacon_node/beacon_processor/src`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src):no format! on the per-message path found

**Sources.** [caplin#11379](https://github.com/erigontech/erigon/pull/11379)

</details>


<a id="allocator_runtime-077"></a>
<details>
<summary><b>allocator_runtime-077</b> Drop async runtime immediately on shutdown — <i>implemented · low · S · latency</i></summary>

**Idea.** On shutdown, drop the async runtime (or use shutdown_background) once tasks complete instead of waiting for a fixed timeout. Check whether Lighthouse's runtime shutdown waits on a fixed timeout before exiting.

**Impact.** Runtime::shutdown_timeout cancels async tasks at once and returns as soon as blocking tasks finish; 15s is only a cap.

**Best measured result.** "speeds up lighthouse's shutdown time making it super fast" (pr:lighthouse#1196)

**Evidence (Lighthouse @ 928b61e719).**

- [`lighthouse/environment/src/lib.rs:40`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/environment/src/lib.rs#L40)
- [`lighthouse/environment/src/lib.rs:452-456`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/environment/src/lib.rs#L452-L456)
- [`lighthouse/src/main.rs:880`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/src/main.rs#L880)

**Skeptic check.** PR #1196 dropped shutdown_on_idle only because an old tokio bug made shutdown_timeout always wait the full timeout; with current tokio shutdown_timeout returns early, so the restored cap gives the same fast shutdown. Upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#1196](https://github.com/sigp/lighthouse/pull/1196)

</details>


<a id="allocator_runtime-078"></a>
<details>
<summary><b>allocator_runtime-078</b> Run blocking validation in blocking pool — <i>partial · low · S · latency, cpu</i></summary>

**Idea.** Run CPU-heavy or lock-holding validation, such as slashing-protection checks, inside block_in_place or a blocking pool rather than directly on an async worker. Check whether Lighthouse performs such blocking checks inline in async handlers.

**Gap in Lighthouse.** Wrap check_and_insert_block_proposal (and the voluntary-exit/other transaction paths) in spawn_blocking_handle like slashing_protect_attestations.

**Impact.** Removes one sqlite transaction (a few ms, once per proposal) from the async worker in the validator client; only matters for proposers.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/lighthouse_validator_store/src/lib.rs:1085`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/lighthouse_validator_store/src/lib.rs#L1085) attestation slashing protection runs via spawn_blocking_handle
- [`validator_client/lighthouse_validator_store/src/lib.rs:501`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/lighthouse_validator_store/src/lib.rs#L501) check_and_insert_block_proposal called inline in async sign_block

**Sources.** [grandine@f7bb32834](https://github.com/grandinetech/grandine/commit/f7bb32834980)

</details>


<a id="allocator_runtime-079"></a>
<details>
<summary><b>allocator_runtime-079</b> Offload consensus engine to separate worker thread — <i>n/a · low · cpu, latency</i></summary>

**Idea.** Run consensus-critical work (fork choice, state transition, gossip validation, BLS) behind a message interface on a dedicated worker thread so the main event loop stays free. Check whether Lighthouse runs these on the same executor as networking and API handling.

**Impact.** Lighthouse already runs gossip validation, state transition, BLS and fork choice in the BeaconProcessor worker pool and spawn_blocking/rayon, off the networking and HTTP async tasks.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:1`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1) BeaconProcessor is a dedicated multi-threaded worker pool with blocking tasks
- [`beacon_node/network/src/network_beacon_processor/mod.rs:516-530`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L516-L530) gossip work sent as Work items to the processor

**Sources.** [lodestar#10464](https://github.com/ChainSafe/lodestar/pull/10464)

</details>


