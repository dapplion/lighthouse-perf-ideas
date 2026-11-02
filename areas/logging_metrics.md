# logging_metrics

58 ideas: 7 not, 15 partial, 19 implemented, 17 n/a; 6 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [logging_metrics-001](#logging_metrics-001) | Block-processing replay benchmark with per-phase timings | partial | low | M | cpu |
| [logging_metrics-002](#logging_metrics-002) | Chain simulator benchmark for production, attestation and import | n/a | low | S | cpu |
| [logging_metrics-003](#logging_metrics-003) | Timing metric for data column KZG verification | implemented | low | S | latency |
| [logging_metrics-004](#logging_metrics-004) | Latency histograms for each engine API call | implemented | low | S | latency |
| [logging_metrics-005](#logging_metrics-005) | Per-task duration metrics in the async executor | implemented | low | S | latency, cpu |
| [logging_metrics-006](#logging_metrics-006) | Aggregate validator monitor metrics instead of per-validator labels | implemented | medium | S | memory, cpu |
| [logging_metrics-007](#logging_metrics-007) | Batch validator monitor logs into per-outcome summaries | implemented | low | S | cpu, disk |
| [logging_metrics-008](#logging_metrics-008) | Fewer histogram buckets on high-cardinality metrics | not | low | S | memory, cpu |
| [logging_metrics-009](#logging_metrics-009) | Asynchronous aggregated logging for received data columns | n/a | low | S | latency, cpu |
| [logging_metrics-010](#logging_metrics-010) | Lazy log argument formatting instead of format! Strings | partial | low | M | memory, cpu |
| [logging_metrics-011](#logging_metrics-011) | Filter log events early and format without intermediate allocations | partial | low | S | cpu, memory |
| [logging_metrics-012](#logging_metrics-012) | Skip context parsing for log lines without context | n/a | low | S | cpu |
| [logging_metrics-013](#logging_metrics-013) | Look up per-topic metric counters once | implemented | low | S | cpu, memory |
| [logging_metrics-014](#logging_metrics-014) | Static str metric labels instead of per-update Strings | implemented | low | S | cpu, memory |
| [logging_metrics-015](#logging_metrics-015) | Zero known label values instead of resetting metric vectors | partial | low | S | cpu |
| [logging_metrics-016](#logging_metrics-016) **★** | Read head state by reference when computing scrape metrics | partial | medium | S | memory, cpu |
| [logging_metrics-017](#logging_metrics-017) **★** | Settable gauges updated on writes, not computed at scrape | not | medium | M | cpu, latency |
| [logging_metrics-018](#logging_metrics-018) | Metrics refreshed by ticker, skipped when nobody scrapes | partial | low | S | cpu, latency |
| [logging_metrics-019](#logging_metrics-019) | Refresh system stats in a blocking thread | not | low | S | latency |
| [logging_metrics-020](#logging_metrics-020) | Pack profiler mark flag into length field | n/a | low |  | memory |
| [logging_metrics-021](#logging_metrics-021) | Bound the tracing exporter span buffer | implemented | low | S | memory |
| [logging_metrics-022](#logging_metrics-022) | Bounded metric labels: no URL or epoch labels | implemented | low | S | memory |
| [logging_metrics-023](#logging_metrics-023) | Use a faster metrics library for hot metric updates | n/a | low | L | cpu |
| [logging_metrics-024](#logging_metrics-024) | Fix memory leak in the metrics client library | n/a | low |  | memory |
| [logging_metrics-025](#logging_metrics-025) | Upgrade tracing library for a faster span bundler | n/a | low |  | cpu |
| [logging_metrics-026](#logging_metrics-026) | Compile out trace-level logs in release builds | not | low | S | cpu |
| [logging_metrics-027](#logging_metrics-027) | Demote or remove per-message logs on hot paths | implemented | medium | S | cpu, disk |
| [logging_metrics-028](#logging_metrics-028) | Check log level before building expensive log arguments | not | low | S | cpu, memory |
| [logging_metrics-029](#logging_metrics-029) | Compute constant log level once at construction | n/a | low | S | cpu |
| [logging_metrics-030](#logging_metrics-030) | Log only sparse progress during sync | partial | low | S | cpu, latency |
| [logging_metrics-031](#logging_metrics-031) | Do not log expected peer behavior as errors | partial | low | S | cpu |
| [logging_metrics-032](#logging_metrics-032) | No stack traces for expected validation failures | n/a | low | S | cpu |
| [logging_metrics-033](#logging_metrics-033) | Throttle repeating warning and progress logs | partial | low | S | cpu, disk |
| [logging_metrics-034](#logging_metrics-034) | Summarize large structures in logs instead of dumping them | partial | low | S | cpu, memory, disk |
| [logging_metrics-035](#logging_metrics-035) | Write debug payload dumps to files, not logs | n/a | low | S | disk, latency |
| [logging_metrics-036](#logging_metrics-036) | Persist debug objects to disk only behind a flag | implemented | low | S | disk, cpu |
| [logging_metrics-037](#logging_metrics-037) | Disable unused p2p library internal metrics | implemented | low | S | cpu, latency |
| [logging_metrics-038](#logging_metrics-038) | Flag to disable validator reward logging | n/a | low | S | cpu |
| [logging_metrics-039](#logging_metrics-039) | Compute network metrics only when metrics are enabled | implemented | low | S | cpu |
| [logging_metrics-040](#logging_metrics-040) | Skip epoch metrics when head is stale | implemented | medium | S | cpu, latency |
| [logging_metrics-041](#logging_metrics-041) **★** | Avoid O(validators) registry scans for metrics | partial | medium | S | cpu |
| [logging_metrics-042](#logging_metrics-042) | No per-validator data in periodic status line | implemented | low | S | cpu, latency |
| [logging_metrics-043](#logging_metrics-043) | No timing instrumentation on idle-loop functions | n/a | low | S | cpu |
| [logging_metrics-044](#logging_metrics-044) | Use a JSON serializer instead of regex output building | n/a | low |  | cpu |
| [logging_metrics-045](#logging_metrics-045) **★** | Avoid long-lived tracing spans on long-running tasks | partial | medium | S | memory |
| [logging_metrics-046](#logging_metrics-046) **★** | Remove tracing spans from hot, cheap functions | partial | medium | S | cpu, memory |
| [logging_metrics-047](#logging_metrics-047) **★** | Span level follows the log filter, not forced info | partial | medium | S | cpu |
| [logging_metrics-048](#logging_metrics-048) | No-op tracing wrapper when tracing is disabled | partial | low | S | cpu |
| [logging_metrics-049](#logging_metrics-049) | Parent-based sampler exporting only instrumented root spans | implemented | low | S | cpu, bandwidth |
| [logging_metrics-050](#logging_metrics-050) | Low default trace sampling rate | not | low | S | cpu |
| [logging_metrics-051](#logging_metrics-051) | Gzip-compress metrics endpoint responses | implemented | low | S | bandwidth |
| [logging_metrics-052](#logging_metrics-052) | Instant queries for single-value dashboard panels | n/a | low |  | cpu |
| [logging_metrics-053](#logging_metrics-053) | Drop redundant _created series from metrics output | n/a | low |  | memory, cpu |
| [logging_metrics-054](#logging_metrics-054) | Skip metric collection for large DB buckets | n/a | low |  | cpu, disk |
| [logging_metrics-055](#logging_metrics-055) | Size-based rotation and compression of log files | implemented | low | S | disk |
| [logging_metrics-056](#logging_metrics-056) | Format logs and stats outside shared mutexes | n/a | low | S | latency, cpu |
| [logging_metrics-057](#logging_metrics-057) | Lightweight in-house logging instead of general tracing framework | not | low | M | cpu |
| [logging_metrics-058](#logging_metrics-058) | Log directly via tracing, removing slog-to-stdlog bridge | implemented | low | S | cpu |

★ actionable. Click an id for the full record.

## Ideas

<a id="logging_metrics-001"></a>
<details>
<summary><b>logging_metrics-001</b> Block-processing replay benchmark with per-phase timings — <i>partial · low · M · cpu</i></summary>

**Idea.** Maintain a benchmark tool that replays stored or generated blocks through state transition and import and reports per-phase timings, run in CI, so slow sections and regressions are found before release.

**Gap in Lighthouse.** lcli transition-blocks handles one block with phase timings; there is no tool that replays a range of blocks through the full import path with per-phase timings, nor CI that runs it. Would need a replay command around BeaconChain::process_block over a stored range.

**Impact.** No runtime effect; helps catch block processing regressions before release.

**Evidence (Lighthouse @ 928b61e719).**

- [`lcli/src/transition_blocks.rs:239-343`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lcli/src/transition_blocks.rs#L239-L343) times block/slot processing, cache build, tree hash for a single block
- [`beacon_node/beacon_chain/benches/benches.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/benches/benches.rs) only reconstruct bench
- no multi-block replay benchmark or CI job found

**Sources.** [nimbus#1083](https://github.com/status-im/nimbus-eth2/pull/1083), [nimbus#1022](https://github.com/status-im/nimbus-eth2/pull/1022)

</details>


<a id="logging_metrics-002"></a>
<details>
<summary><b>logging_metrics-002</b> Chain simulator benchmark for production, attestation and import — <i>n/a · low · S · cpu</i></summary>

**Idea.** Provide a simulator that drives the block pool through block production, attestation and import in one loop, so bottlenecks across the whole node pipeline show up in one benchmark.

**Impact.** Benchmark tooling only; no runtime effect on a node.

**Evidence (Lighthouse @ 928b61e719).**

- [`testing/simulator/src/main.rs:1`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/testing/simulator/src/main.rs#L1) basic-sim/fallback-sim only, full-node multi-process

**Sources.** [nimbus#956](https://github.com/status-im/nimbus-eth2/pull/956)

</details>


<a id="logging_metrics-003"></a>
<details>
<summary><b>logging_metrics-003</b> Timing metric for data column KZG verification — <i>implemented · low · S · latency</i></summary>

**Idea.** Record a histogram of the time spent verifying KZG proofs of data column sidecars, so the cost of column verification is visible on dashboards.

**Impact.** Column KZG verification cost is already visible as histograms for single (gossip) and batch (RPC/sync) paths.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/metrics.rs:2147`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/metrics.rs#L2147) KZG_VERIFICATION_DATA_COLUMN_SINGLE_TIMES
- [`beacon_node/beacon_chain/src/metrics.rs:2156`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/metrics.rs#L2156) KZG_VERIFICATION_DATA_COLUMN_BATCH_TIMES
- [`beacon_node/beacon_chain/src/data_column_verification.rs:527`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L527),1041,1067,1088,1129 timers on single and batch column KZG verification

**Skeptic check.** Verified that the histograms exist and that timers wrap every column KZG verification function, single and batch. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#17346](https://github.com/OffchainLabs/prysm/pull/17346)

</details>


<a id="logging_metrics-004"></a>
<details>
<summary><b>logging_metrics-004</b> Latency histograms for each engine API call — <i>implemented · low · S · latency</i></summary>

**Idea.** Record a Prometheus latency histogram per engine API method (newPayload, forkchoiceUpdated, getPayload...), so execution-layer slowdowns and regressions are visible.

**Impact.** Per-method EL latency is already observable for newPayload, forkchoiceUpdated, getPayload and getBlobs.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/metrics.rs:31-38`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/metrics.rs#L31-L38) EXECUTION_LAYER_REQUEST_TIMES HistogramVec labeled by method
- [`beacon_node/execution_layer/src/lib.rs:1400`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1400) get_payload timer
- [`beacon_node/execution_layer/src/lib.rs:1450`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1450) new_payload timer
- [`beacon_node/execution_layer/src/lib.rs:1565`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1565) forkchoice_updated timer
- [`beacon_node/beacon_chain/src/metrics.rs:1920`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/metrics.rs#L1920) BEACON_ENGINE_GET_BLOBS_V2_REQUEST_DURATION_SECONDS

**Skeptic check.** Confirmed the per-method histogram is used for the main engine methods, and getBlobs has its own duration histogram. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#10414](https://github.com/OffchainLabs/prysm/pull/10414)

</details>


<a id="logging_metrics-005"></a>
<details>
<summary><b>logging_metrics-005</b> Per-task duration metrics in the async executor — <i>implemented · low · S · latency, cpu</i></summary>

**Idea.** Record a count and duration metric for every task spawned by the task executor, labeled by task name, so tasks that block or stall the async runtime show up on dashboards.

**Impact.** Already present for async, blocking and block_on tasks.

**Evidence (Lighthouse @ 928b61e719).**

- [`common/task_executor/src/lib.rs:127-140`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/task_executor/src/lib.rs#L127-L140) spawn_monitor TASKS_HISTOGRAM timer by name
- [`common/task_executor/src/lib.rs:185`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/task_executor/src/lib.rs#L185),274 ASYNC_TASKS_COUNT gauge by name
- [`common/task_executor/src/lib.rs:324-347`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/task_executor/src/lib.rs#L324-L347) spawn_blocking_handle BLOCKING_TASKS_HISTOGRAM/COUNT
- [`common/task_executor/src/lib.rs:372-395`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/task_executor/src/lib.rs#L372-L395) block_on_dangerous BLOCK_ON_TASKS_HISTOGRAM/COUNT

**Skeptic check.** Lighthouse is the source PR (#2735) and the metrics are still in place. A small exception: spawn_blocking_with_rayon_async (lib.rs:241) has no name or metric, but that is a rayon job, not an executor task.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#2735](https://github.com/sigp/lighthouse/pull/2735)

</details>


<a id="logging_metrics-006"></a>
<details>
<summary><b>logging_metrics-006</b> Aggregate validator monitor metrics instead of per-validator labels — <i>implemented · medium · S · memory, cpu</i></summary>

**Idea.** Validator monitor metrics should not carry a per-validator label by default or above a small validator count; export sums and counts over all monitored validators instead. This keeps time-series cardinality O(1) instead of O(validators) and cuts scrape cost and memory.

**Impact.** Per-validator label cardinality is O(1) above 64 monitored validators. Aggregate series are always exported.

**Best measured result.** pr:lodestar#8824: Cardinality reduced from O(n) to O(1)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_monitor.rs:48`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_monitor.rs#L48) DEFAULT_INDIVIDUAL_TRACKING_THRESHOLD = 64
- [`beacon_node/beacon_chain/src/validator_monitor.rs:439`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_monitor.rs#L439) individual_tracking()
- [`beacon_node/beacon_chain/src/validator_monitor.rs:518-521`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_monitor.rs#L518-L521) per-validator balance/status gauges skipped above threshold
- [`beacon_node/beacon_chain/src/validator_monitor.rs:967`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_monitor.rs#L967),1006 inclusion distance and sync committee gauges gated
- [`beacon_node/beacon_chain/src/validator_monitor.rs:1913`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_monitor.rs#L1913) aggregatable_metric falls back to the aggregate tag

**Skeptic check.** Checked the per-validator `&[id]` label sites. Each is behind individual_tracking() or uses aggregatable_metric. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#3578](https://github.com/status-im/nimbus-eth2/pull/3578), [lighthouse#3728](https://github.com/sigp/lighthouse/pull/3728), [prysm#3121](https://github.com/OffchainLabs/prysm/pull/3121), [lodestar#8824](https://github.com/ChainSafe/lodestar/pull/8824), [nimbus@fa27ce76a](https://github.com/status-im/nimbus-eth2/commit/fa27ce76a334), [nimbus#3297](https://github.com/status-im/nimbus-eth2/pull/3297), [nimbus#4468](https://github.com/status-im/nimbus-eth2/pull/4468), [nimbus#2719](https://github.com/status-im/nimbus-eth2/pull/2719)

</details>


<a id="logging_metrics-007"></a>
<details>
<summary><b>logging_metrics-007</b> Batch validator monitor logs into per-outcome summaries — <i>implemented · low · S · cpu, disk</i></summary>

**Idea.** Instead of one log line per monitored validator per epoch, emit one line per outcome listing the validator indices or a total, and move per-validator lines to debug, so log volume does not grow with validator count.

**Impact.** Epoch summary logs are already one line per outcome; per-validator event logs only appear below the individual-tracking threshold.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_monitor.rs:1024-1062`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_monitor.rs#L1024-L1062) one info! per outcome with validators list
- [`beacon_node/beacon_chain/src/validator_monitor.rs:439-441`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_monitor.rs#L439-L441) individual_tracking threshold
- [`beacon_node/beacon_chain/src/validator_monitor.rs:1372-1398`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_monitor.rs#L1372-L1398),1449-1480 per-validator info logs gated by individual_tracking, repeats downgraded to debug

**Skeptic check.** Verified the aggregated per-outcome info lines and that per-validator attestation/aggregate logs are gated by individual_tracking(). The only ungated per-validator line is sync signatures (line 999), which the sync committee size caps.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#2606](https://github.com/sigp/lighthouse/pull/2606), [nimbus#3286](https://github.com/status-im/nimbus-eth2/pull/3286), [prysm#17083](https://github.com/OffchainLabs/prysm/pull/17083)

</details>


<a id="logging_metrics-008"></a>
<details>
<summary><b>logging_metrics-008</b> Fewer histogram buckets on high-cardinality metrics — <i>not · low · S · memory, cpu</i></summary>

**Idea.** Use a small number of histogram buckets on metrics that have many label values (for example validator monitor histograms), so the number of series, scrape size and update cost stay low.

**Gap in Lighthouse.** Switch validator monitor HistogramVecs to try_create_histogram_vec_with_buckets with ~5 buckets (e.g. 0.5,1,2,4,12 s) in metrics.rs.

**Impact.** Only nodes with many monitored validators; series count reduces ~2x (11 default buckets to ~5) on those histograms.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/metrics.rs:1297`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/metrics.rs#L1297),1313,1329,1396 validator monitor histogram vecs use try_create_histogram_vec (default buckets) with label [src, validator]
- [`beacon_node/execution_layer/src/metrics.rs:31`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/metrics.rs#L31) shows custom buckets are possible

**Sources.** [lodestar#3813](https://github.com/ChainSafe/lodestar/pull/3813)

</details>


<a id="logging_metrics-009"></a>
<details>
<summary><b>logging_metrics-009</b> Asynchronous aggregated logging for received data columns — <i>n/a · low · S · latency, cpu</i></summary>

**Idea.** Send received-data-column log events through a bounded channel to a background task that aggregates them per slot and flushes about once per second, so gossip validation does no log formatting or I/O.

**Impact.** Lighthouse does not log per received column, and tracing file writer is already async; nothing to batch.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs): no per-message info/debug log for received data columns found by grep
- [`common/logging/src/tracing_logging_layer.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/logging/src/tracing_logging_layer.rs) uses a non-blocking appender already

**Sources.** [prysm#15289](https://github.com/OffchainLabs/prysm/pull/15289)

</details>


<a id="logging_metrics-010"></a>
<details>
<summary><b>logging_metrics-010</b> Lazy log argument formatting instead of format! Strings — <i>partial · low · M · memory, cpu</i></summary>

**Idea.** Pass log arguments to the logger by reference or with lazy Display/Debug formatting instead of building Strings with format! or to_string in the log call, so filtered or emitted logs do not allocate temporaries.

**Gap in Lighthouse.** Call sites are lazy. But Lighthouse's own LoggingLayer (FieldVisitor::record_str/record_debug/record_*, on_new_span, on_event) builds intermediate Strings for every field name, value, span field copy, timestamp and location before it builds the output line. The default debug logfile emits these events constantly. Write fields straight into one reusable buffer and keep names as &amp;'static str.

**Impact.** Each emitted log line makes several small heap allocations. Lighthouse emits a high volume of debug logs to the file by default, so the allocator churn is steady. Each event costs little, but the effect is spread across the node.

**Best measured result.** pr:lighthouse#2183: heaptrack shows temporary allocations reduced by at least 4%

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain_collection.rs:500`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain_collection.rs#L500) call sites use lazy %/? fields
- [`common/logging/src/tracing_logging_layer.rs:186-237`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/logging/src/tracing_logging_layer.rs#L186-L237) FieldVisitor allocates field.name().to_string() (a &amp;'static str) plus a format!'d String for every field of every emitted event
- [`common/logging/src/tracing_logging_layer.rs:52-63`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/logging/src/tracing_logging_layer.rs#L52-L63) on_new_span copies span name and all fields into Strings for each span
- [`common/logging/src/tracing_logging_layer.rs:80-85`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/logging/src/tracing_logging_layer.rs#L80-L85) span field Vec cloned into every event
- [`common/logging/src/tracing_logging_layer.rs:72`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/logging/src/tracing_logging_layer.rs#L72),104-116,283 per-event timestamp/line/location/output Strings
- [`lighthouse/environment/src/lib.rs:230`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/environment/src/lib.rs#L230) the same LoggingLayer writes the debug-level logfile (default --logfile-debug-level debug)
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:381`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L381) and lighthouse_network/src/peer_manager/mod.rs:523 remaining eager .to_string() fields

**Skeptic check.** The earlier evidence is right for filtered events and call sites. It is wrong to say emitted logs avoid temporaries: the custom formatting layer allocates per field and per span. That is the same allocator waste the source PRs targeted.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lighthouse#2017](https://github.com/sigp/lighthouse/pull/2017), [lighthouse#2183](https://github.com/sigp/lighthouse/pull/2183), [lodestar#1752](https://github.com/ChainSafe/lodestar/pull/1752), [teku#9608](https://github.com/Consensys-Incorporated/teku/pull/9608)

</details>


<a id="logging_metrics-011"></a>
<details>
<summary><b>logging_metrics-011</b> Filter log events early and format without intermediate allocations — <i>partial · low · S · cpu, memory</i></summary>

**Idea.** In the logging layer, check whether an event is enabled for its target and output before any formatting, and write formatted output directly into one buffer (no color-then-strip, no intermediate Strings), so disabled or verbose subsystems cost little CPU.

**Gap in Lighthouse.** Per-layer filters already skip disabled events before on_event, but no event_enabled in the libp2p/discv5 layer and the main layer formats via intermediate Strings (format!, color+plain strings, JSON via serde Map). PR lighthouse#9356 (still open) does the libp2p part; rewrite build_log_text/build_log_json and FieldVisitor to write straight to a buffer.

**Impact.** Tracing was measured ~13% CPU over an epoch; roughly 2 points of total node CPU saved at best.

**Best measured result.** pr:lighthouse#9356: tracing CPU over an epoch from ~13% to ~11%

**Evidence (Lighthouse @ 928b61e719).**

- [`common/logging/src/tracing_logging_layer.rs:73`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/logging/src/tracing_logging_layer.rs#L73) on_event visits every field into Strings, builds location/level/padded strings with format!
- [`common/logging/src/tracing_libp2p_discv5_logging_layer.rs:20`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/logging/src/tracing_libp2p_discv5_logging_layer.rs#L20) on_event formats timestamp+message Strings, no event_enabled
- [`lighthouse/src/main.rs:620`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/src/main.rs#L620) per-layer with_filter(level)+workspace_filter, so disabled events are filtered before on_event

**Sources.** [nimbus#7319](https://github.com/status-im/nimbus-eth2/pull/7319), [lighthouse#9356](https://github.com/sigp/lighthouse/pull/9356)

</details>


<a id="logging_metrics-012"></a>
<details>
<summary><b>logging_metrics-012</b> Skip context parsing for log lines without context — <i>n/a · low · S · cpu</i></summary>

**Idea.** Return early in the log formatter when a log call has no context or fields, so plain log lines skip context and stack parsing work.

**Impact.** Lodestar-specific logger; Lighthouse uses tracing with structured fields.

**Evidence (Lighthouse @ 928b61e719).**

- [`common/logging/src/lib.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/logging/src/lib.rs), tracing_logging_layer.rs: tracing-based, no Lodestar-style context parsing

**Sources.** [lodestar@4926c6a98](https://github.com/ChainSafe/lodestar/commit/4926c6a983b7)

</details>


<a id="logging_metrics-013"></a>
<details>
<summary><b>logging_metrics-013</b> Look up per-topic metric counters once — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Get or create per-topic metric counters with a single get-or-insert lookup (and cache the handle) instead of looking up or creating the labeled counter twice on each message.

**Impact.** No double get-or-create; the idea's waste (two creations per new topic) does not exist.

**Evidence (Lighthouse @ 928b61e719).**

- [`common/metrics/src/lib.rs:224-240`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/metrics/src/lib.rs#L224-L240) get_int_counter/inc_counter_vec do one get_metric_with_label_values per event

**Skeptic check.** The caplin fix removed a duplicate GetOrCreateCounter on first use of a topic; Lighthouse's helpers do a single labeled lookup. Lighthouse does not cache counter handles, but that is a different optimization from the one the idea describes.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#18749](https://github.com/erigontech/erigon/pull/18749)

</details>


<a id="logging_metrics-014"></a>
<details>
<summary><b>logging_metrics-014</b> Static str metric labels instead of per-update Strings — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Use &amp;'static str label values for metrics (derived from enums with strum/AsRef&lt;str&gt;, or a build-time table for subnet ids) instead of allocating a String for the label on each metric update, and merge related counters into one labeled vector.

**Impact.** The high-frequency per-attestation and per-subnet labels are static. The few String labels left are per column, per scrape or per error, so they are negligible.

**Best measured result.** pr:lighthouse#1895: heaptrack showed ~75% of temporary allocations came from these label strings

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/attestation/subnet_id.rs:22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/attestation/subnet_id.rs#L22) static SUBNET_ID_TO_STRING, &amp;'static str labels
- [`consensus/types/src/sync_committee/sync_subnet_id.rs:15`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/sync_committee/sync_subnet_id.rs#L15) same for sync subnets
- [`beacon_node/lighthouse_network/src/service/mod.rs:883`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L883) attestation subnet label via subnet_id.as_ref()
- [`beacon_node/http_api/src/lib.rs:284`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L284) path label &amp;'static str
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:959`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L959), network/src/metrics.rs:882, http_api/src/lib.rs:287 remaining String labels (per column / per scrape / per request, low volume)

**Skeptic check.** Grepped every metric call site for to_string/format! labels. None is on a per-attestation or per-message hot path. The earlier verdict holds.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#1895](https://github.com/sigp/lighthouse/pull/1895), [lighthouse#1984](https://github.com/sigp/lighthouse/pull/1984), [lighthouse#1898](https://github.com/sigp/lighthouse/pull/1898), [lighthouse#2100](https://github.com/sigp/lighthouse/pull/2100), [lighthouse#2164](https://github.com/sigp/lighthouse/pull/2164)

</details>


<a id="logging_metrics-015"></a>
<details>
<summary><b>logging_metrics-015</b> Zero known label values instead of resetting metric vectors — <i>partial · low · S · cpu</i></summary>

**Idea.** When refreshing labeled gauges such as gossip mesh-peer counts, set known label values to zero and overwrite them instead of resetting the whole metric vector on each update, to avoid series churn and reallocation.

**Gap in Lighthouse.** Mesh-peer gauges already zero known labels. update_peer_score_metrics and update_sync_metrics still reset() whole vectors; replace with zeroing the fixed label sets (quartile names, ClientKind, sync types).

**Impact.** Removes series delete/recreate every 5-30s tick; negligible CPU, avoids brief missing series in scrapes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/metrics.rs:786-801`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/metrics.rs#L786-L801) update_gossip_metrics zeroes each known ClientKind instead of reset (done)
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:1504-1509`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L1504-L1509) update_peer_score_metrics calls gauge.reset() on PEER_SCORE_DISTRIBUTION and PEER_SCORE_PER_CLIENT
- [`beacon_node/network/src/metrics.rs:851`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/metrics.rs#L851) update_sync_metrics resets PEERS_PER_SYNC_TYPE

**Sources.** [lodestar@9ad55a49d](https://github.com/ChainSafe/lodestar/commit/9ad55a49d331)

</details>


<a id="logging_metrics-016"></a>
<details>
<summary><b>logging_metrics-016</b> Read head state by reference when computing scrape metrics — <i>partial · medium · S · memory, cpu</i></summary>

**Idea.** Compute scrape-time metrics from the head state by borrowing it under the read lock or through read-only validator views, instead of cloning the beacon state or copying every validator, and fold validator counters into one pass.

**Gap in Lighthouse.** Borrowing is done. The balance sum runs twice and the validator loop is a third pass. Remove the duplicated block and fold the counts into one pass, or cache them per head/epoch.

**Impact.** Saves two of three O(validators) list walks per scrape (tens of ms per scrape on mainnet); off the hot path.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/metrics.rs:2266`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/metrics.rs#L2266) with_head borrows the head snapshot (no state clone)
- [`beacon_node/beacon_chain/src/metrics.rs:2388-2401`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/metrics.rs#L2388-L2401) HEAD_STATE_TOTAL_VALIDATORS and balances().iter().sum() set twice
- [`beacon_node/beacon_chain/src/metrics.rs:2403-2419`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/metrics.rs#L2403-L2419) separate loop over validators for active/slashed/withdrawn
- [`beacon_node/http_metrics/src/metrics.rs:31`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_metrics/src/metrics.rs#L31) called on every /metrics scrape

**Second check.** Re-read scrape_head_state at this commit: duplicated sum block still present, no other setter for these gauges in the tree.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [lighthouse#2298](https://github.com/sigp/lighthouse/pull/2298), [prysm#12628](https://github.com/OffchainLabs/prysm/pull/12628)

</details>


<a id="logging_metrics-017"></a>
<details>
<summary><b>logging_metrics-017</b> Settable gauges updated on writes, not computed at scrape — <i>not · medium · M · cpu, latency</i></summary>

**Idea.** Update store-derived metrics (checkpoints, map sizes) into settable gauges when the store changes or at slot boundaries, so a metrics scrape never takes the store/fork-choice lock.

**Gap in Lighthouse.** Set fork-choice and store cache gauges where they change (on_block/prune/cache insert/evict) or on a per-slot timer, and drop the fork_choice read lock and store mutexes from the scrape path.

**Impact.** Scrapes stop contending with fork choice and store cache locks; removes rare scrape-time latency on block import, little CPU.

**Best measured result.** pr:teku#2483: Stated: removes need for read locks when checking map sizes

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/metrics.rs:2334-2337`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/metrics.rs#L2334-L2337) fork_choice_read_lock().scrape_for_metrics() per scrape
- [`consensus/fork_choice/src/metrics.rs:49-65`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/metrics.rs#L49-L65) only setter of FORK_CHOICE_QUEUED_ATTESTATIONS/NODES/INDICES
- [`beacon_node/store/src/hot_cold_store.rs:446-465`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L446-L465) register_metrics locks historic_state_cache, block_cache, state_cache at scrape
- [`beacon_node/beacon_chain/src/metrics.rs:2280`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/metrics.rs#L2280) state_cache_len() takes the state_cache lock again

**Second check.** Grepped every use of the fork choice and store cache gauges: the scrape functions are the only setters; no write-time update exists.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [teku#2584](https://github.com/Consensys-Incorporated/teku/pull/2584), [teku#2483](https://github.com/Consensys-Incorporated/teku/pull/2483), [ethlambda#192](https://github.com/lambdaclass/ethlambda/pull/192)

</details>


<a id="logging_metrics-018"></a>
<details>
<summary><b>logging_metrics-018</b> Metrics refreshed by ticker, skipped when nobody scrapes — <i>partial · low · S · cpu, latency</i></summary>

**Idea.** Refresh expensive metrics (system stats, epoch metrics) from an internal ticker at a configurable interval, and skip their collection when no scrape is happening, instead of computing them on every request.

**Gap in Lighthouse.** Scrape-time work is already skipped without scrapes, but there is no ticker/cache: every scrape (and every /lighthouse/ui/health call) recomputes system health and store sizes. Could cache the result for a few seconds in scrape_health_metrics and store::scrape_for_metrics.

**Impact.** Saves a few /proc and statvfs reads per scrape; only matters with several scrapers or short scrape intervals.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_metrics/src/metrics.rs:7-55`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_metrics/src/metrics.rs#L7-L55) gather_prometheus_metrics runs scrape_for_metrics, store, discovery and health scrapes on each request only (so nothing runs when nobody scrapes)
- [`beacon_node/network/src/service.rs:57`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L57),380,466 5s metrics_update ticker gated by metrics_enabled
- [`beacon_node/http_api/src/lib.rs:531-555`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L531-L555) sysinfo refreshed per request, not ticker

**Sources.** [grandine@2259019e1](https://github.com/grandinetech/grandine/commit/2259019e13c2), [lighthouse#6928](https://github.com/sigp/lighthouse/pull/6928)

</details>


<a id="logging_metrics-019"></a>
<details>
<summary><b>logging_metrics-019</b> Refresh system stats in a blocking thread — <i>not · low · S · latency</i></summary>

**Idea.** Run the system stats refresh for metrics (disk, CPU, memory syscalls) in a blocking-thread task instead of on the async runtime, so synchronous syscalls do not stall async workers.

**Gap in Lighthouse.** Wrap gather_prometheus_metrics in tokio::task::spawn_blocking in metrics_handler, and the sysinfo refresh in http_api system_info_filter in a blocking task.

**Impact.** Avoids stalling an async worker for the duration of /proc, disk-usage and store directory-size syscalls on each scrape (store::scrape_for_metrics may walk db dirs); small, but more on slow disks.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_metrics/src/lib.rs:143`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_metrics/src/lib.rs#L143) metrics_handler is async and calls gather_prometheus_metrics synchronously
- [`common/health_metrics/src/metrics.rs:107-170`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/health_metrics/src/metrics.rs#L107-L170) scrape_health_metrics does psutil /proc reads inline
- [`beacon_node/http_api/src/lib.rs:544-553`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L544-L553) sysinfo refresh_* in warp filter map, sync, on the runtime; no spawn_blocking in either file

**Sources.** [grandine#438](https://github.com/grandinetech/grandine/pull/438), [grandine@55a11ef9b](https://github.com/grandinetech/grandine/commit/55a11ef9b0f5)

</details>


<a id="logging_metrics-020"></a>
<details>
<summary><b>logging_metrics-020</b> Pack profiler mark flag into length field — <i>n/a · low · memory</i></summary>

**Idea.** Pack the open/close flag of a profiler mark into spare bits of the name-length field, shrinking each record from 32 to 24 bytes.

**Impact.** Lighthouse has no in-process profiler with mark records.

**Best measured result.** pr:silver#129: Mark record 32 bytes -&gt; 24 bytes

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.lock no profiler crate; no mark-record profiler found in repo

**Sources.** [silver#129](https://github.com/gattaca-com/silver/pull/129)

</details>


<a id="logging_metrics-021"></a>
<details>
<summary><b>logging_metrics-021</b> Bound the tracing exporter span buffer — <i>implemented · low · S · memory</i></summary>

**Idea.** Cap the in-memory span buffer of the tracing/OpenTelemetry exporter at a fixed maximum, so spans that cannot be flushed do not grow memory without bound.

**Impact.** Span buffer is bounded at 2048 and drops when full.

**Evidence (Lighthouse @ 928b61e719).**

- [`lighthouse/src/main.rs:660-698`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/src/main.rs#L660-L698) opt-in telemetry with with_batch_exporter
- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/opentelemetry_sdk-0.30.0/src/trace/span_processor.rs:310 sync_channel(max_queue_size)
- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/opentelemetry_sdk-0.30.0/src/trace/span_processor.rs:525-532 try_send drops spans when full
- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/opentelemetry_sdk-0.30.0/src/trace/span_processor.rs:59 OTEL_BSP_MAX_QUEUE_SIZE_DEFAULT 2048

**Skeptic check.** Confirmed that the SDK 0.30 BatchSpanProcessor uses a bounded sync_channel with try_send and drops spans when full. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#3188](https://github.com/OffchainLabs/prysm/pull/3188)

</details>


<a id="logging_metrics-022"></a>
<details>
<summary><b>logging_metrics-022</b> Bounded metric labels: no URL or epoch labels — <i>implemented · low · S · memory</i></summary>

**Idea.** Never use unbounded values such as request URLs, slots or epochs as metric labels or new series; use the route name or a fixed set, so series count stays bounded.

**Impact.** Series count bounded; HTTP path label restricted to fixed list, VC endpoint label is the configured (redacted) BN set.

**Best measured result.** pr:prysm#16055: http_error_count had one series per slot URL, now one per endpoint

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs:196-289`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L196-L289)
- [`validator_client/beacon_node_fallback/src/lib.rs:801`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/beacon_node_fallback/src/lib.rs#L801)
- [`beacon_node/network/src/sync/network_context.rs:1737`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L1737)

**Skeptic check.** Verified the HTTP API path whitelist with 'other' fallback; a grep of *_vec metric calls found no slot, epoch, root or peer-id labels. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#16055](https://github.com/OffchainLabs/prysm/pull/16055), [prysm#2636](https://github.com/OffchainLabs/prysm/pull/2636), [teku#684](https://github.com/Consensys-Incorporated/teku/pull/684)

</details>


<a id="logging_metrics-023"></a>
<details>
<summary><b>logging_metrics-023</b> Use a faster metrics library for hot metric updates — <i>n/a · low · L · cpu</i></summary>

**Idea.** Use a metrics library with cheap counter/gauge increments and fast collection, since per-message gossip metric updates are on the hot path.

**Gap in Lighthouse.** Lighthouse uses rust-prometheus; swapping the library would be a large redesign with small gain (atomic counters are already cheap; vec lookups hash labels). Not an applicable cheap win.

**Impact.** Hot gossip metric updates are mostly plain static counters; labeled vec lookups cost a hash per update, minor.

**Evidence (Lighthouse @ 928b61e719).**

- [`common/metrics/src/lib.rs:53`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/metrics/src/lib.rs#L53) wraps the prometheus 0.13 crate
- Cargo.toml:210 prometheus 0.13

**Sources.** [lodestar#4675](https://github.com/ChainSafe/lodestar/pull/4675), [nimbus#5692](https://github.com/status-im/nimbus-eth2/pull/5692), [lodestar#6230](https://github.com/ChainSafe/lodestar/pull/6230), [prysm#8256](https://github.com/OffchainLabs/prysm/pull/8256)

</details>


<a id="logging_metrics-024"></a>
<details>
<summary><b>logging_metrics-024</b> Fix memory leak in the metrics client library — <i>n/a · low · memory</i></summary>

**Idea.** Check that the Prometheus client library in use has no known memory leak that grows with time, and upgrade if it does.

**Impact.** Idea is about a Go Prometheus library leak; Lighthouse uses the Rust prometheus 0.13.4 and prometheus-client with no known matching leak.

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.lock prometheus 0.13.4 (rust crate), prometheus-client 0.24/0.25

**Sources.** [prysm#6921](https://github.com/OffchainLabs/prysm/pull/6921)

</details>


<a id="logging_metrics-025"></a>
<details>
<summary><b>logging_metrics-025</b> Upgrade tracing library for a faster span bundler — <i>n/a · low · cpu</i></summary>

**Idea.** Use a tracing/exporter library version with a cheaper span batching path, to cut per-span export cost.

**Impact.** Already on a recent opentelemetry with a batch exporter, opt-in and sampled; a bump would give marginal gain.

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.lock opentelemetry 0.30.0; [`lighthouse/src/main.rs:693`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/src/main.rs#L693) batch exporter; sampler only exports lh_ prefixed roots ([`common/tracing_samplers/src/lib.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/tracing_samplers/src/lib.rs))

**Sources.** [prysm#4158](https://github.com/OffchainLabs/prysm/pull/4158)

</details>


<a id="logging_metrics-026"></a>
<details>
<summary><b>logging_metrics-026</b> Compile out trace-level logs in release builds — <i>not · low · S · cpu</i></summary>

**Idea.** Set a compile-time maximum log level (for example the log/tracing release_max_level feature) so trace-level statements are removed from the binary and cost nothing at runtime.

**Gap in Lighthouse.** Add features = ["release_max_level_debug"] to the workspace tracing dependency (and to log if used) so trace! sites compile out in release builds.

**Impact.** Removes a cheap atomic level check at ~80 trace! sites; tracing's callsite cache already makes disabled events nearly free, so gain is marginal.

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.toml:255 tracing = "0.1.40" with no max_level/release_max_level feature
- Cargo.lock has no slog; PR #6103 (slog feature) no longer applies after tracing migration
- 80 trace! call sites remain (e.g. [`beacon_node/lighthouse_network/src/rpc/mod.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/mod.rs))

**Sources.** [lighthouse#6103](https://github.com/sigp/lighthouse/pull/6103)

</details>


<a id="logging_metrics-027"></a>
<details>
<summary><b>logging_metrics-027</b> Demote or remove per-message logs on hot paths — <i>implemented · medium · S · cpu, disk</i></summary>

**Idea.** Log per-message, per-peer, per-attestation and per-validator-loop events at debug/trace or not at all, instead of info/warn, because they scale with peers and validators and their formatting and writing cost CPU and disk; metrics already cover the outcome.

**Best measured result.** pr:nimbus#5776: 2000 addMapping calls 40 ms -&gt; 6.5e-05 s after removing loop logging

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:2875`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L2875)
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1747`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1747)
- [`beacon_node/beacon_chain/src/validator_monitor.rs:439`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_monitor.rs#L439)

**Skeptic check.** Per-attestation outcomes (e.g. unknown head) log at trace; remaining info/warn/error in gossip_methods are block-level, rejection or internal-error paths. Validator-monitor per-validator logs only for opted-in validators. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [ethlambda#586](https://github.com/lambdaclass/ethlambda/pull/586), [lodestar@1822944a7](https://github.com/ChainSafe/lodestar/commit/1822944a7021), [lighthouse#2395](https://github.com/sigp/lighthouse/pull/2395), [prysm#7928](https://github.com/OffchainLabs/prysm/pull/7928), [nimbus#7673](https://github.com/status-im/nimbus-eth2/pull/7673), [lodestar#4040](https://github.com/ChainSafe/lodestar/pull/4040), [prysm#3680](https://github.com/OffchainLabs/prysm/pull/3680), [lighthouse#9436](https://github.com/sigp/lighthouse/pull/9436), [caplin#24702](https://github.com/erigontech/erigon/pull/24702), [caplin#22483](https://github.com/erigontech/erigon/pull/22483), [nimbus#5776](https://github.com/status-im/nimbus-eth2/pull/5776), [lodestar#3893](https://github.com/ChainSafe/lodestar/pull/3893), [prysm#15816](https://github.com/OffchainLabs/prysm/pull/15816), [lodestar#2199](https://github.com/ChainSafe/lodestar/pull/2199), [prysm#3303](https://github.com/OffchainLabs/prysm/pull/3303), [nimbus#1788](https://github.com/status-im/nimbus-eth2/pull/1788), [lighthouse#5672](https://github.com/sigp/lighthouse/pull/5672)

</details>


<a id="logging_metrics-028"></a>
<details>
<summary><b>logging_metrics-028</b> Check log level before building expensive log arguments — <i>not · low · S · cpu, memory</i></summary>

**Idea.** Before building expensive log arguments (serializing messages, collecting events, building field contexts, running DB queries for log data), check once whether the debug/trace level is enabled and skip the work if not, so hot paths do nothing for disabled logs.

**Gap in Lighthouse.** Tracing macros already skip argument evaluation when level is disabled; the only gap is code that precomputes values outside the macro. Audit debug!/trace! sites that build values beforehand and wrap them in tracing::enabled!(Level::DEBUG).

**Impact.** Tiny; avoids occasional allocations in a few hot paths. Not measurable on mainnet.

**Best measured result.** pr:caplin#24940: 64-step walk 7.55 us, 352 allocs -&gt; 1.55 us, 0 allocs

**Evidence (Lighthouse @ 928b61e719).**

- grep for tracing::enabled!/event_enabled/log_enabled across beacon_node and common: no hits
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:1085`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L1085) trace! builds format!() argument eagerly
- tracing macros evaluate field expressions only if callsite enabled, so cost is only where arguments are computed before the macro

**Sources.** [teku#10087](https://github.com/Consensys-Incorporated/teku/pull/10087), [caplin#22488](https://github.com/erigontech/erigon/pull/22488), [prysm#2553](https://github.com/OffchainLabs/prysm/pull/2553), [caplin#24940](https://github.com/erigontech/erigon/pull/24940), [teku#10034](https://github.com/Consensys-Incorporated/teku/pull/10034)

</details>


<a id="logging_metrics-029"></a>
<details>
<summary><b>logging_metrics-029</b> Compute constant log level once at construction — <i>n/a · low · S · cpu</i></summary>

**Idea.** When a component chooses its log level from configuration that never changes (for example validator monitor), compute that level once at construction instead of on every log call.

**Impact.** Not applicable: tracing macros use a static level per call site; there is no runtime-configured level computed per call.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_monitor.rs:452`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_monitor.rs#L452) info! with fixed level at call site

**Sources.** [lodestar#6010](https://github.com/ChainSafe/lodestar/pull/6010)

</details>


<a id="logging_metrics-030"></a>
<details>
<summary><b>logging_metrics-030</b> Log only sparse progress during sync — <i>partial · low · S · cpu, latency</i></summary>

**Idea.** During range/backfill sync, do not log every block or request; log only epoch-start blocks or periodic progress, with an opt-in verbose flag.

**Gap in Lighthouse.** Lighthouse logs per batch (epoch-sized) at debug, and info only for progress, not per block. Sync block-import logs per block at info/debug are not present in sync paths I looked at; a periodic-progress-only mode is not offered as a flag.

**Impact.** Per-block logging cost is already avoided; maybe a fraction of a percent CPU saved during sync.

**Best measured result.** pr:prysm#6515: per-block logging was ~7% of CPU at 20 blocks/s

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/backfill_sync/mod.rs:792`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/backfill_sync/mod.rs#L792),878,901 debug! per batch (not per block)
- [`beacon_node/network/src/sync/range_sync/chain.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs) per-batch logging

**Sources.** [nimbus@92c38d6d4](https://github.com/status-im/nimbus-eth2/commit/92c38d6d48ef), [prysm#6515](https://github.com/OffchainLabs/prysm/pull/6515)

</details>


<a id="logging_metrics-031"></a>
<details>
<summary><b>logging_metrics-031</b> Do not log expected peer behavior as errors — <i>partial · low · S · cpu</i></summary>

**Idea.** Treat normal network events (duplicate gossip sidecars from several peers, requests for blobs we do not have, slow or overloaded peers) as normal results and do not log them as errors or warnings, to avoid log flooding.

**Gap in Lighthouse.** Duplicates are already debug or silent. Remaining: rpc_methods.rs error!/warn! on retrieval failure for peer requests; check these exclude not-found/expected cases.

**Impact.** Log volume only; negligible CPU.

**Best measured result.** pr:prysm#16536: duplicate-sidecar log was ~50% of debug log volume on a supernode

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:875`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L875) PriorKnown column -&gt; Ignore, no log
- gossip_methods.rs:1027 DuplicateFullyImported -&gt; debug!
- gossip_methods.rs:1223 PriorKnown partial column -&gt; debug!
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:849`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L849) warn! when serving a column fails (genuine local failure)

**Sources.** [prysm#16536](https://github.com/OffchainLabs/prysm/pull/16536), [caplin#16210](https://github.com/erigontech/erigon/pull/16210), [prysm#13598](https://github.com/OffchainLabs/prysm/pull/13598)

</details>


<a id="logging_metrics-032"></a>
<details>
<summary><b>logging_metrics-032</b> No stack traces for expected validation failures — <i>n/a · low · S · cpu</i></summary>

**Idea.** When logging expected block/gossip validation failures, log only the message and skip capturing and printing a stack trace.

**Impact.** Rust errors carry no stack trace; validation failures log the error value only.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/publish_blocks.rs:390`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L390) only an empty stacktraces field in a response

**Sources.** [teku#9459](https://github.com/Consensys-Incorporated/teku/pull/9459)

</details>


<a id="logging_metrics-033"></a>
<details>
<summary><b>logging_metrics-033</b> Throttle repeating warning and progress logs — <i>partial · low · S · cpu, disk</i></summary>

**Idea.** Rate-limit log lines that can repeat rapidly (queue-full warnings, inactivity-leak warnings, deposit-fetch errors, per-deposit progress), emitting at most one per interval.

**Gap in Lighthouse.** Hot-path queue-full errors in FifoQueue/LifoQueue/per-peer push (work_queue.rs) are logged per dropped item; add a TimeLatch (already used 29 places) in those queues.

**Impact.** Under overload, avoids thousands of error log lines per second and the formatting/IO cost; small CPU/log volume win only in stress.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:796`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L796) TimeLatch debounce for reprocess queue
- [`beacon_node/beacon_processor/src/lib.rs:1564`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1564) aggregate/attestation queue-full logs debounced
- [`beacon_node/beacon_processor/src/scheduler/work_queue.rs:50`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_queue.rs#L50) FifoQueue::push logs error! on every drop, no limiter
- [`beacon_node/beacon_processor/src/scheduler/work_queue.rs:141`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_queue.rs#L141) per-peer queue full error! on every drop

**Sources.** [teku#9128](https://github.com/Consensys-Incorporated/teku/pull/9128), [lodestar@38d64953f](https://github.com/ChainSafe/lodestar/commit/38d64953fa2f), [teku#7788](https://github.com/Consensys-Incorporated/teku/pull/7788), [teku#7933](https://github.com/Consensys-Incorporated/teku/pull/7933)

</details>


<a id="logging_metrics-034"></a>
<details>
<summary><b>logging_metrics-034</b> Summarize large structures in logs instead of dumping them — <i>partial · low · S · cpu, memory, disk</i></summary>

**Idea.** Log compact summaries (counts, index ranges, min/avg/max) of large values such as aggregation bits, column index lists or whole response messages instead of Debug-formatting them in full.

**Gap in Lighthouse.** No evidence of 200KB single-line dumps, but a few Debug dumps of whole objects exist (beacon_chain.rs warn on invalid attestation). Replace with root/slot/bit-count summaries.

**Impact.** Negligible on a healthy node; avoids rare huge log lines.

**Best measured result.** pr:ethlambda#587: single log lines of 200-278 KB replaced by a summary

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:6009`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6009) logs full attestation with ?att on invalid-attestation warn
- [`beacon_node/network/src/sync/network_context.rs:928`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L928) logs index lists with ?indices (custody columns, small)

**Sources.** [nimbus#7058](https://github.com/status-im/nimbus-eth2/pull/7058), [ethlambda#587](https://github.com/lambdaclass/ethlambda/pull/587), [prysm#16210](https://github.com/OffchainLabs/prysm/pull/16210), [lodestar@8a86d0667](https://github.com/ChainSafe/lodestar/commit/8a86d0667b4d), [nimbus#4544](https://github.com/status-im/nimbus-eth2/pull/4544)

</details>


<a id="logging_metrics-035"></a>
<details>
<summary><b>logging_metrics-035</b> Write debug payload dumps to files, not logs — <i>n/a · low · S · disk, latency</i></summary>

**Idea.** Write debug dumps of p2p messages and block payloads as binary files instead of hex-encoding them into log lines, avoiding large log formatting and log volume.

**Impact.** Lighthouse has no debug path that hex-encodes p2p messages or payloads into logs.

**Evidence (Lighthouse @ 928b61e719).**

- grep for dump in [`beacon_node/lighthouse_network/src`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src) found no payload hex-dump logging

**Sources.** [teku#8177](https://github.com/Consensys-Incorporated/teku/pull/8177)

</details>


<a id="logging_metrics-036"></a>
<details>
<summary><b>logging_metrics-036</b> Persist debug objects to disk only behind a flag — <i>implemented · low · S · disk, cpu</i></summary>

**Idea.** Write invalid SSZ objects or state dumps to disk only when a debug flag is set, and never write a full state every slot by default, so production nodes do not spend disk I/O on debug data.

**Impact.** Already opt-in; no per-slot state dump.

**Best measured result.** pr:prysm#15226: 'writing a state to disk every slot is resource-intensive'

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/config.rs:142`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L142)
- [`beacon_node/network/src/service.rs:338`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L338)
- [`beacon_node/beacon_chain/src/block_verification.rs:118`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L118)

**Skeptic check.** Invalid-block storage is only active with a path; pre/post state SSZ dumps in block_verification are compiled in only with the write_ssz_files feature. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#3797](https://github.com/ChainSafe/lodestar/pull/3797), [prysm#15226](https://github.com/OffchainLabs/prysm/pull/15226), [lighthouse@b316086be](https://github.com/sigp/lighthouse/commit/b316086be0e1), [lighthouse@7b7a44e2f](https://github.com/sigp/lighthouse/commit/7b7a44e2f22e)

</details>


<a id="logging_metrics-037"></a>
<details>
<summary><b>logging_metrics-037</b> Disable unused p2p library internal metrics — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Turn off the p2p/gossipsub library's internal metrics when the node does not need them, since collecting them creates garbage and periodic GC or CPU cost.

**Impact.** With metrics off, there are no libp2p metrics; Rust has no GC, so the lodestar motivation mostly does not apply.

**Best measured result.** pr:lodestar#4699: Reduced gc run time (screenshots only)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/mod.rs:355-361`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L355-L361) gossipsub.with_metrics only if libp2p_registry is Some
- [`beacon_node/client/src/builder.rs:535-539`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L535-L539) registry only when config.metrics_enabled
- [`beacon_node/lighthouse_network/src/service/mod.rs:510-512`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L510-L512) bandwidth metrics also gated

**Skeptic check.** Verified that the gossipsub and bandwidth metrics are registered only when --metrics creates a registry. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#4699](https://github.com/ChainSafe/lodestar/pull/4699)

</details>


<a id="logging_metrics-038"></a>
<details>
<summary><b>logging_metrics-038</b> Flag to disable validator reward logging — <i>n/a · low · S · cpu</i></summary>

**Idea.** Provide a flag that turns off computing and logging per-validator reward/penalty data in the validator client.

**Impact.** The Lighthouse validator client does not compute or log per-validator rewards, so there is nothing to disable.

**Evidence (Lighthouse @ 928b61e719).**

- grep -ri reward in [`validator_client/src`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/src) found nothing

**Sources.** [prysm#2319](https://github.com/OffchainLabs/prysm/pull/2319)

</details>


<a id="logging_metrics-039"></a>
<details>
<summary><b>logging_metrics-039</b> Compute network metrics only when metrics are enabled — <i>implemented · low · S · cpu</i></summary>

**Idea.** Skip computing expensive network-service metrics (per-peer and per-subnet scans) unless metrics are enabled on the command line.

**Impact.** Per-peer/per-subnet metric scans are skipped unless --metrics is on.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/service.rs:468`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L468) gossip/sync metric scans run only `if self.metrics_enabled`
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:1499`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L1499) update_peer_score_metrics returns early when !metrics_enabled
- [`beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs:284`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs#L284),323 peer count metrics gated
- [`beacon_node/lighthouse_network/src/service/mod.rs:356-383`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L356-L383),510 gossipsub/bandwidth metrics only with libp2p_registry
- [`beacon_node/src/config.rs:1490`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/config.rs#L1490) metrics_enabled set from --metrics

**Skeptic check.** Verified the network service tick, peer manager and gossipsub metrics registration are all gated on metrics being enabled; earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#2765](https://github.com/sigp/lighthouse/pull/2765)

</details>


<a id="logging_metrics-040"></a>
<details>
<summary><b>logging_metrics-040</b> Skip epoch metrics when head is stale — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Skip computing epoch participation metrics that need an old state when the head is far behind the wall-clock slot, so stalls do not trigger expensive state loads.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/metrics.rs:2266`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/metrics.rs#L2266)
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:269`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L269)
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:309`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L309)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4937`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4937)

**Skeptic check.** Metrics scrape uses only the in-memory head state (no old-state load); epoch participation summaries come from the state advance timer, which skips when head is &gt;256 slots behind, and the validator monitor skips historic epochs. Earlier evidence right but missed the state_advance_timer guard, which is the closer match.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine@06ce9931d](https://github.com/grandinetech/grandine/commit/06ce9931ddb1)

</details>


<a id="logging_metrics-041"></a>
<details>
<summary><b>logging_metrics-041</b> Avoid O(validators) registry scans for metrics — <i>partial · medium · S · cpu</i></summary>

**Idea.** Do not compute metrics that scan the whole validator registry (validator counts by status) on the hot path or inside state transition; compute them from caches or drop them.

**Gap in Lighthouse.** Not in state transition, but each scrape does an O(validators) loop (plus two balance sums). Derive counts from the epoch cache / per-epoch summary once per epoch, or drop them.

**Impact.** Removes a ~1M-element tree iteration per scrape; off the hot path.

**Best measured result.** pr:nimbus#2090: removes expensive beacon_current_validators, beacon_previous_validators metrics

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/metrics.rs:2407-2419`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/metrics.rs#L2407-L2419) O(validators) loop per scrape
- [`beacon_node/beacon_chain/src/metrics.rs:2421`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/metrics.rs#L2421) only setter of HEAD_STATE_ACTIVE_VALIDATORS
- [`consensus/state_processing/src/per_epoch_processing/epoch_processing_summary.rs:92`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/epoch_processing_summary.rs#L92) state transition only sets gauges from existing totals

**Second check.** Confirmed no cached or per-epoch setter of active/slashed/withdrawn counts exists anywhere.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [nimbus#2090](https://github.com/status-im/nimbus-eth2/pull/2090)

</details>


<a id="logging_metrics-042"></a>
<details>
<summary><b>logging_metrics-042</b> No per-validator data in periodic status line — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Do not compute per-validator balances or status for the periodic status/log line, because it needs a linear scan over validators and forced public key decompression.

**Impact.** Status lines use counts only; no balance scan or pubkey decompression.

**Best measured result.** commit:nimbus@10da7fe9dada: not viable at higher validator counts - linear scan + forced public key init makes it extremely slow

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/client/src/notifier.rs:42`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/notifier.rs#L42)
- [`validator_client/validator_services/src/notifier_service.rs:109`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/notifier_service.rs#L109)
- [`validator_client/validator_services/src/duties_service.rs:500`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L500)

**Skeptic check.** BN notifier has no validator scan; VC notifier counts local duties via pubkey-byte HashSets, no state balances or key decompression. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus@10da7fe9d](https://github.com/status-im/nimbus-eth2/commit/10da7fe9dada), [nimbus#1475](https://github.com/status-im/nimbus-eth2/pull/1475)

</details>


<a id="logging_metrics-043"></a>
<details>
<summary><b>logging_metrics-043</b> No timing instrumentation on idle-loop functions — <i>n/a · low · S · cpu</i></summary>

**Idea.** Remove timers and profiling marks from functions that run constantly in idle polling loops, so polling with no work has no instrumentation overhead.

**Impact.** Lighthouse has no timing instrumentation in idle polling loops equivalent to Silver's profiling marks.

**Evidence (Lighthouse @ 928b61e719).**

- no idle-loop profiling marks found; metrics timers sit on work paths ([`beacon_node/network/src/service.rs:468`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L468) gated)

**Sources.** [silver#160](https://github.com/gattaca-com/silver/pull/160)

</details>


<a id="logging_metrics-044"></a>
<details>
<summary><b>logging_metrics-044</b> Use a JSON serializer instead of regex output building — <i>n/a · low · cpu</i></summary>

**Idea.** Build JSON output for the API/data provider with a real JSON serializer, not regex-based string building.

**Impact.** Lighthouse already serialises JSON via serde, no regex building.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/Cargo.toml:46`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/Cargo.toml#L46) serde_json used for API output

**Sources.** [teku#563](https://github.com/Consensys-Incorporated/teku/pull/563)

</details>


<a id="logging_metrics-045"></a>
<details>
<summary><b>logging_metrics-045</b> Avoid long-lived tracing spans on long-running tasks — <i>partial · medium · S · memory</i></summary>

**Idea.** Do not attach tracing spans to long-running tasks or keep spans alive for long periods; keep only a few short root spans on key import paths, since long-lived spans accumulate memory.

**Gap in Lighthouse.** #7765/#7816 removed the worst spans, but sync still holds spans for whole range chains, lookups and custody requests. Because MetricsLayer (and the debug file layer) has no level filter, those debug spans are live in the registry by default, not only at debug. Drop or shorten them, and give MetricsLayer an events-only filter.

**Impact.** Lower steady-state memory while syncing at default config; size unknown.

**Best measured result.** pr:lighthouse#7816: Removing the old spans seem to have reduced the memory usage quite a lot

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain.rs:149-150`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L149-L150),184,199 SyncingChain stores its lh_syncing_chain span for its life
- [`beacon_node/network/src/sync/block_lookups/single_block_lookup.rs:207`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/single_block_lookup.rs#L207),218,243 lookup stores span
- [`beacon_node/network/src/sync/network_context/custody.rs:35`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L35),57,70,321 custody request and batch spans stored
- [`lighthouse/src/main.rs:663`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/src/main.rs#L663) MetricsLayer pushed with no level filter
- [`common/logging/src/tracing_metrics_layer.rs:38-67`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/logging/src/tracing_metrics_layer.rs#L38-L67) MetricsLayer implements only on_event, so default enabled()/register_callsite enable every span
- [`lighthouse/src/main.rs:147`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/src/main.rs#L147) logfile-debug-level defaults to debug

**Second check.** Correction to the earlier review: the custody backfill info_span (custody_backfill_sync/mod.rs:1034) is scoped to send_batch and is not long-lived; but the debug spans are live by default because of the unfiltered MetricsLayer and the debug-level logfile default.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [lighthouse#7816](https://github.com/sigp/lighthouse/pull/7816), [lighthouse#7765](https://github.com/sigp/lighthouse/pull/7765)

</details>


<a id="logging_metrics-046"></a>
<details>
<summary><b>logging_metrics-046</b> Remove tracing spans from hot, cheap functions — <i>partial · medium · S · cpu, memory</i></summary>

**Idea.** Do not create tracing spans around very frequent or trivial functions (DB has-checks, getters, per-signature or per-slot helpers, slasher loops), because span creation costs more than the work it measures.

**Gap in Lighthouse.** #7707 removed some spans, but cheap getters (lock accessors, get_full_block) still carry #[instrument]. With the unfiltered MetricsLayer, setting a span to debug/trace level does not disable it, so removal (or filtering MetricsLayer to events) is needed.

**Impact.** One registry span allocation per call; small except where get_full_block is called in loops (blocks-by-range serving).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:643`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L643) #[instrument(skip_all)] on cached_head_write_lock
- [`beacon_node/beacon_chain/src/canonical_head.rs:669`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L669) same on fork_choice_write_lock
- [`beacon_node/store/src/hot_cold_store.rs:630`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L630) get_full_block instrumented at info
- [`lighthouse/src/main.rs:663`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/src/main.rs#L663) unfiltered MetricsLayer enables every span callsite, even trace-level ones

**Second check.** Found no global span filter that would make these spans free; the unfiltered MetricsLayer makes every span enabled regardless of level.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [prysm#14864](https://github.com/OffchainLabs/prysm/pull/14864), [prysm#2236](https://github.com/OffchainLabs/prysm/pull/2236), [prysm#7655](https://github.com/OffchainLabs/prysm/pull/7655), [lighthouse#7707](https://github.com/sigp/lighthouse/pull/7707), [prysm#7061](https://github.com/OffchainLabs/prysm/pull/7061), [lighthouse#7636](https://github.com/sigp/lighthouse/pull/7636)

</details>


<a id="logging_metrics-047"></a>
<details>
<summary><b>logging_metrics-047</b> Span level follows the log filter, not forced info — <i>partial · medium · S · cpu</i></summary>

**Idea.** Do not force tracing spans on hot functions to info level; give them a level that the active filter can disable, so disabled spans cost almost nothing.

**Gap in Lighthouse.** Span levels were lowered to debug/trace (PR #7620), but the unfiltered MetricsLayer pushed in main.rs returns Interest::always and no max_level_hint for every callsite. So the dispatcher never disables any span or event: every trace/debug span is still allocated in the Registry and entered/exited, and every trace!/debug! event (including libp2p/yamux/discv5 dependency trace events) is built and dispatched. Fix: wrap MetricsLayer in LevelFilter::INFO (or implement register_callsite/max_level_hint) so the global max level follows the real log filters.

**Impact.** Removes span allocation and event dispatch for trace-level callsites on gossip, sync and dependency hot paths (and debug ones when the logfile level is info); small CPU saving per message.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:686`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L686),1531 hot gossip spans at level=debug
- [`lighthouse/src/main.rs:654`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/src/main.rs#L654) logging_layers.push(MetricsLayer.boxed()) with no filter
- [`common/logging/src/tracing_metrics_layer.rs:38-66`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/logging/src/tracing_metrics_layer.rs#L38-L66) MetricsLayer overrides neither register_callsite/enabled nor max_level_hint, and only uses INFO/WARN/ERROR events
- ~/.cargo/registry/src/*/tracing-subscriber-0.3.23/src/layer/mod.rs:1788-1829 Vec&lt;Layer&gt;: highest interest wins; any layer with no max_level_hint makes the hint None
- [`lighthouse/src/main.rs:147`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/src/main.rs#L147) logfile-debug-level defaults to debug

**Skeptic check.** The span attributes are at debug/trace as cited, but the level cannot disable them because an unfiltered layer enables all callsites; the earlier verdict missed this filter-composition detail.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lighthouse#7620](https://github.com/sigp/lighthouse/pull/7620)

</details>


<a id="logging_metrics-048"></a>
<details>
<summary><b>logging_metrics-048</b> No-op tracing wrapper when tracing is disabled — <i>partial · low · S · cpu</i></summary>

**Idea.** When tracing export is disabled, use a no-op span implementation so hot paths skip all span creation and attribute work.

**Gap in Lighthouse.** With telemetry off there is no OTel layer, but spans are not no-ops: the unfiltered MetricsLayer makes every span callsite 'always' interested, so each #[instrument]/span! still allocates a Registry slab entry, records fields and is entered/exited. Filtering MetricsLayer to INFO events (it ignores spans) in main.rs would make trace spans, and debug spans when file logging is at info, real no-ops.

**Impact.** Small per-span CPU/allocation saving on hot paths when tracing export is disabled.

**Evidence (Lighthouse @ 928b61e719).**

- [`lighthouse/src/main.rs:661-709`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/src/main.rs#L661-L709) OTel layer only built when --telemetry-collector-url is set
- [`lighthouse/src/main.rs:654`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/src/main.rs#L654) unfiltered MetricsLayer enables every span callsite
- [`common/logging/src/tracing_metrics_layer.rs:38`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/logging/src/tracing_metrics_layer.rs#L38) no register_callsite/max_level_hint override

**Skeptic check.** Earlier evidence was right that no OTel layer exists without the flag, but wrong that spans then cost only a filter check: the MetricsLayer keeps every span enabled at the Registry.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [prysm#14207](https://github.com/OffchainLabs/prysm/pull/14207)

</details>


<a id="logging_metrics-049"></a>
<details>
<summary><b>logging_metrics-049</b> Parent-based sampler exporting only instrumented root spans — <i>implemented · low · S · cpu, bandwidth</i></summary>

**Idea.** Use a parent-based trace sampler that exports only root spans from instrumented code paths (by name prefix) and drops the rest, to cut export overhead.

**Impact.** Only lh_-prefixed root traces are exported; children inherit the decision.

**Evidence (Lighthouse @ 928b61e719).**

- [`lighthouse/src/main.rs:687-689`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/src/main.rs#L687-L689) Sampler::ParentBased(PrefixBasedSampler::new("lh_"))
- [`common/tracing_samplers/src/lib.rs:26-49`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/tracing_samplers/src/lib.rs#L26-L49) Drop for names without the prefix

**Skeptic check.** Verified the parent-based prefix sampler is installed on the only tracer provider; matches the idea.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#8647](https://github.com/sigp/lighthouse/pull/8647)

</details>


<a id="logging_metrics-050"></a>
<details>
<summary><b>logging_metrics-050</b> Low default trace sampling rate — <i>not · low · S · cpu</i></summary>

**Idea.** Make the OpenTelemetry trace sample rate configurable with a low default (for example 1%), so span export overhead stays small.

**Gap in Lighthouse.** Add a --telemetry-sample-rate flag (default low) and wrap PrefixBasedSampler in a ratio-based check (e.g. Sampler::TraceIdRatioBased inside ParentBased) in lighthouse/src/main.rs, or have PrefixBasedSampler hash trace_id.

**Impact.** Only affects nodes that enable telemetry export; cuts export volume roughly proportionally to rate (e.g. 100x at 1%).

**Evidence (Lighthouse @ 928b61e719).**

- [`lighthouse/src/main.rs:687`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/src/main.rs#L687) sampler has no ratio, every lh_ root is sampled
- [`lighthouse/src/main.rs:272-290`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/src/main.rs#L272-L290) only telemetry-collector-url and service-name flags; grep for sample_rate/TraceIdRatio found nothing

**Sources.** [lighthouse#8561](https://github.com/sigp/lighthouse/pull/8561)

</details>


<a id="logging_metrics-051"></a>
<details>
<summary><b>logging_metrics-051</b> Gzip-compress metrics endpoint responses — <i>implemented · low · S · bandwidth</i></summary>

**Idea.** Compress the HTTP metrics endpoint response with gzip when the scraper sends Accept-Encoding gzip, shrinking each scrape by an order of magnitude.

**Impact.** Metrics scrape compressed (~90% smaller).

**Best measured result.** pr:lighthouse#10338: ~966 KB to ~76 KB per scrape, ~92% reduction

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_metrics/src/lib.rs:120`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_metrics/src/lib.rs#L120)
- [`validator_client/http_metrics/src/lib.rs:128`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/http_metrics/src/lib.rs#L128)
- [`common/axum_utils/Cargo.toml:14`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/axum_utils/Cargo.toml#L14)

**Skeptic check.** tower-http CompressionLayer with compression-gzip feature on both BN and VC metrics servers; negotiates on Accept-Encoding. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#10338](https://github.com/sigp/lighthouse/pull/10338)

</details>


<a id="logging_metrics-052"></a>
<details>
<summary><b>logging_metrics-052</b> Instant queries for single-value dashboard panels — <i>n/a · low · cpu</i></summary>

**Idea.** Use instant queries instead of range queries in shipped dashboards for panels that show one latest value, so the metrics server returns one point.

**Impact.** Dashboard query tweak, no node runtime effect (only lowers Prometheus query cost).

**Evidence (Lighthouse @ 928b61e719).**

- repo ships dashboards under scripts/ / grafana not node code

**Sources.** [lodestar#4954](https://github.com/ChainSafe/lodestar/pull/4954)

</details>


<a id="logging_metrics-053"></a>
<details>
<summary><b>logging_metrics-053</b> Drop redundant _created series from metrics output — <i>n/a · low · memory, cpu</i></summary>

**Idea.** Do not export the per-metric _created series on the metrics endpoint, which makes scrape output much larger for no use.

**Impact.** The Rust prometheus crate does not export _created, so there is nothing to drop.

**Best measured result.** pr:nimbus#7523: remove _created label (takes up a lot of space in the metrics endpoint)

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.toml:210 prometheus 0.13 (Rust client) does not emit _created series

**Sources.** [nimbus#7523](https://github.com/status-im/nimbus-eth2/pull/7523)

</details>


<a id="logging_metrics-054"></a>
<details>
<summary><b>logging_metrics-054</b> Skip metric collection for large DB buckets — <i>n/a · low · cpu, disk</i></summary>

**Idea.** Do not collect per-bucket/per-column DB statistics (key counts) for the largest or write-heavy buckets in the metrics collector, because scanning them is costly.

**Impact.** Lighthouse's store metrics collector does not scan per-bucket key counts, so there is no costly scan to skip.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/metrics.rs:406`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/metrics.rs#L406) scrape_for_metrics only sums directory sizes
- grep for key_count/column stats in [`beacon_node/store/src`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src) found none

**Sources.** [prysm#8395](https://github.com/OffchainLabs/prysm/pull/8395), [prysm#8339](https://github.com/OffchainLabs/prysm/pull/8339)

</details>


<a id="logging_metrics-055"></a>
<details>
<summary><b>logging_metrics-055</b> Size-based rotation and compression of log files — <i>implemented · low · S · disk</i></summary>

**Idea.** Rotate log files by size with gzip compression and a retention limit, so logs cannot fill the disk.

**Impact.** Log disk usage is bounded by default; gzip is opt-in.

**Evidence (Lighthouse @ 928b61e719).**

- [`lighthouse/environment/src/lib.rs:213-225`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/environment/src/lib.rs#L213-L225) LogRollerBuilder size-based rotation, max_keep_files, optional Gzip
- [`lighthouse/src/main.rs:163-188`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/src/main.rs#L163-L188) --logfile-max-size (200MB) / --logfile-max-number (10) / --logfile-compress

**Skeptic check.** Verified size-based rotation with retention and optional compression; earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine#456](https://github.com/grandinetech/grandine/pull/456), [lighthouse#2762](https://github.com/sigp/lighthouse/pull/2762), [lodestar#4509](https://github.com/ChainSafe/lodestar/pull/4509)

</details>


<a id="logging_metrics-056"></a>
<details>
<summary><b>logging_metrics-056</b> Format logs and stats outside shared mutexes — <i>n/a · low · S · latency, cpu</i></summary>

**Idea.** Do log formatting and stats computation after releasing shared locks, not while holding them, to cut lock contention on hot paths.

**Impact.** Logging goes through tracing with a non_blocking writer; formatting happens in the subscriber, not under application mutexes. Did not audit every lock site.

**Evidence (Lighthouse @ 928b61e719).**

- [`lighthouse/environment/src/lib.rs:226-232`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/environment/src/lib.rs#L226-L232) non_blocking file writer

**Sources.** [caplin#20759](https://github.com/erigontech/erigon/pull/20759)

</details>


<a id="logging_metrics-057"></a>
<details>
<summary><b>logging_metrics-057</b> Lightweight in-house logging instead of general tracing framework — <i>not · low · M · cpu</i></summary>

**Idea.** Replace the general-purpose tracing/logging framework on hot paths with a minimal logging implementation that does less work per call. Check whether Lighthouse log calls go through a heavy subscriber layer.

**Gap in Lighthouse.** Lighthouse still uses the tracing framework with custom layers; a lighter path would need to cut per-event allocation in LoggingLayer::on_event and MetricsLayer::on_event. Disabled levels are already filtered cheaply by tracing callsite interest.

**Impact.** Only matters for events actually emitted (info/warn/error, or debug runs); negligible CPU on a default mainnet node.

**Evidence (Lighthouse @ 928b61e719).**

- [`lighthouse/environment/src/tracing_common.rs:1`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/environment/src/tracing_common.rs#L1) builds on tracing-subscriber layers
- [`common/logging/src/tracing_logging_layer.rs:68`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/logging/src/tracing_logging_layer.rs#L68) LoggingLayer::on_event formats each event (local timestamp, field visitor, span scan, String allocs) then writes to a non-blocking appender
- [`common/logging/src/tracing_metrics_layer.rs:35`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/logging/src/tracing_metrics_layer.rs#L35) extra layer calls normalized_metadata per event

**Sources.** [silver#327](https://github.com/gattaca-com/silver/pull/327)

</details>


<a id="logging_metrics-058"></a>
<details>
<summary><b>logging_metrics-058</b> Log directly via tracing, removing slog-to-stdlog bridge — <i>implemented · low · S · cpu</i></summary>

**Idea.** Make the p2p/libp2p layer and submodules log straight through the single tracing subscriber instead of through a slog-to-stdlog bridge, removing per-call bridging overhead. Check whether Lighthouse still routes any logs through a bridge.

**Impact.** No slog bridge exists; libp2p core and discv5 emit tracing events into the single subscriber.

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.lock (no slog packages; only log + tracing-log)
- [`lighthouse/environment/src/tracing_common.rs:1-40`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/environment/src/tracing_common.rs#L1-L40)
- [`common/logging/src/tracing_metrics_layer.rs:4`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/logging/src/tracing_metrics_layer.rs#L4)
- [`lighthouse/src/main.rs:720`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/src/main.rs#L720)

**Skeptic check.** Confirmed no slog crate in Cargo.lock and one tracing subscriber stack. The only bridge left is log-&gt;tracing (tracing-log) for a few deps that still use the log crate (yamux, if-watch, rustls, warp, reqwest), which is the standard low-volume path and not the slog-to-stdlog bridge the idea removes.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine#303](https://github.com/grandinetech/grandine/pull/303), [grandine#422](https://github.com/grandinetech/grandine/pull/422)

</details>


