# logging_metrics

21 ideas: 2 not, 9 partial, 9 implemented, 1 n/a; 5 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

Ids missing from the sequence are ideas that have not been checked against Lighthouse yet.

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [logging_metrics-006](#logging_metrics-006) | Aggregate validator monitor metrics instead of per-validator labels | implemented | medium |  | memory, cpu |
| [logging_metrics-010](#logging_metrics-010) | Lazy log argument formatting instead of format! Strings | implemented | low | S | memory, cpu |
| [logging_metrics-011](#logging_metrics-011) | Filter log events early and format without intermediate allocations | partial | low | S | cpu, memory |
| [logging_metrics-014](#logging_metrics-014) | Static str metric labels instead of per-update Strings | implemented | low | S | cpu, memory |
| [logging_metrics-016](#logging_metrics-016) **★** | Read head state by reference when computing scrape metrics | partial | medium | S | memory, cpu |
| [logging_metrics-017](#logging_metrics-017) **★** | Settable gauges updated on writes, not computed at scrape | not | medium | M | cpu, latency |
| [logging_metrics-022](#logging_metrics-022) | Bounded metric labels: no URL or epoch labels | implemented | low | S | memory |
| [logging_metrics-023](#logging_metrics-023) | Use a faster metrics library for hot metric updates | n/a | low | L | cpu |
| [logging_metrics-027](#logging_metrics-027) | Demote or remove per-message logs on hot paths | implemented | medium |  | cpu, disk |
| [logging_metrics-028](#logging_metrics-028) | Check log level before building expensive log arguments | not | low | S | cpu, memory |
| [logging_metrics-030](#logging_metrics-030) | Log only sparse progress during sync | partial | low | S | cpu, latency |
| [logging_metrics-031](#logging_metrics-031) | Do not log expected peer behavior as errors | partial | low | S | cpu |
| [logging_metrics-033](#logging_metrics-033) | Throttle repeating warning and progress logs | partial | low | S | cpu, disk |
| [logging_metrics-034](#logging_metrics-034) | Summarize large structures in logs instead of dumping them | partial | low | S | cpu, memory, disk |
| [logging_metrics-036](#logging_metrics-036) | Persist debug objects to disk only behind a flag | implemented | low |  | disk, cpu |
| [logging_metrics-040](#logging_metrics-040) | Skip epoch metrics when head is stale | implemented | medium |  | cpu, latency |
| [logging_metrics-041](#logging_metrics-041) **★** | Avoid O(validators) registry scans for metrics | partial | medium | S | cpu |
| [logging_metrics-042](#logging_metrics-042) | No per-validator data in periodic status line | implemented | low |  | cpu, latency |
| [logging_metrics-045](#logging_metrics-045) **★** | Avoid long-lived tracing spans on long-running tasks | partial | medium | S | memory |
| [logging_metrics-046](#logging_metrics-046) **★** | Remove tracing spans from hot, cheap functions | partial | medium | S | cpu, memory |
| [logging_metrics-051](#logging_metrics-051) | Gzip-compress metrics endpoint responses | implemented | low |  | bandwidth |

★ actionable. Click an id for the full record.

## Ideas

<a id="logging_metrics-006"></a>
<details>
<summary><b>logging_metrics-006</b> Aggregate validator monitor metrics instead of per-validator labels — <i>implemented · medium · memory, cpu</i></summary>

**Idea.** Validator monitor metrics should not carry a per-validator label by default or above a small validator count; export sums and counts over all monitored validators instead. This keeps time-series cardinality O(1) instead of O(validators) and cuts scrape cost and memory.

**Best measured result.** pr:lodestar#8824: Cardinality reduced from O(n) to O(1)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_monitor.rs:49`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_monitor.rs#L49) DEFAULT_INDIVIDUAL_TRACKING_THRESHOLD=64
- [`beacon_node/beacon_chain/src/validator_monitor.rs:439`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_monitor.rs#L439) individual_tracking() gates per-validator labels
- [`beacon_node/beacon_chain/src/validator_monitor.rs:1913`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_monitor.rs#L1913) aggregatable_metric falls back to aggregate tag

**Sources.** [nimbus#3578](https://github.com/status-im/nimbus-eth2/pull/3578), [lighthouse#3728](https://github.com/sigp/lighthouse/pull/3728), [prysm#3121](https://github.com/OffchainLabs/prysm/pull/3121), [lodestar#8824](https://github.com/ChainSafe/lodestar/pull/8824), [nimbus@fa27ce76a](https://github.com/status-im/nimbus-eth2/commit/fa27ce76a334), [nimbus#3297](https://github.com/status-im/nimbus-eth2/pull/3297)

</details>


<a id="logging_metrics-010"></a>
<details>
<summary><b>logging_metrics-010</b> Lazy log argument formatting instead of format! Strings — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** Pass log arguments to the logger by reference or with lazy Display/Debug formatting instead of building Strings with format! or to_string in the log call, so filtered or emitted logs do not allocate temporaries.

**Impact.** Already done; slog-era format! removed with tracing migration. Remaining stray format! in discovery/mod.rs:1085 is trivial.

**Best measured result.** pr:lighthouse#2183: heaptrack shows temporary allocations reduced by at least 4%

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/range_sync/chain_collection.rs:500`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain_collection.rs#L500) tracing fields use %/? lazily
- [`common/logging/src/tracing_logging_layer.rs:210`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/logging/src/tracing_logging_layer.rs#L210) field values only formatted in the layer when event passes filters

**Sources.** [lighthouse#2017](https://github.com/sigp/lighthouse/pull/2017), [lighthouse#2183](https://github.com/sigp/lighthouse/pull/2183)

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


<a id="logging_metrics-014"></a>
<details>
<summary><b>logging_metrics-014</b> Static str metric labels instead of per-update Strings — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Use &amp;'static str label values for metrics (derived from enums with strum/AsRef&lt;str&gt;, or a build-time table for subnet ids) instead of allocating a String for the label on each metric update, and merge related counters into one labeled vector.

**Impact.** Already done on hot paths.

**Best measured result.** pr:lighthouse#1895: heaptrack showed ~75% of temporary allocations came from these label strings

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/attestation/subnet_id.rs:22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/attestation/subnet_id.rs#L22) static SUBNET_ID_TO_STRING table, subnet_id_to_string returns &amp;'static str
- [`consensus/types/src/sync_committee/sync_subnet_id.rs:15`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/sync_committee/sync_subnet_id.rs#L15) same for sync subnets
- [`beacon_node/http_api/src/lib.rs:284`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L284) path label is &amp;'static str

**Sources.** [lighthouse#1895](https://github.com/sigp/lighthouse/pull/1895), [lighthouse#1984](https://github.com/sigp/lighthouse/pull/1984), [lighthouse#1898](https://github.com/sigp/lighthouse/pull/1898), [lighthouse#2100](https://github.com/sigp/lighthouse/pull/2100), [lighthouse#2164](https://github.com/sigp/lighthouse/pull/2164)

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

**Sources.** [teku#2584](https://github.com/Consensys-Incorporated/teku/pull/2584), [teku#2483](https://github.com/Consensys-Incorporated/teku/pull/2483)

</details>


<a id="logging_metrics-022"></a>
<details>
<summary><b>logging_metrics-022</b> Bounded metric labels: no URL or epoch labels — <i>implemented · low · S · memory</i></summary>

**Idea.** Never use unbounded values such as request URLs, slots or epochs as metric labels or new series; use the route name or a fixed set, so series count stays bounded.

**Impact.** Series count is bounded; no slot or epoch labels found in vec metric calls.

**Best measured result.** pr:prysm#16055: http_error_count had one series per slot URL, now one per endpoint

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs:196-289`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L196-L289) path restricted to a predefined list, else 'other'
- [`beacon_node/http_api/src/metrics.rs:8`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/metrics.rs#L8) label 'path' only

**Sources.** [prysm#16055](https://github.com/OffchainLabs/prysm/pull/16055), [prysm#2636](https://github.com/OffchainLabs/prysm/pull/2636)

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

**Sources.** [lodestar#4675](https://github.com/ChainSafe/lodestar/pull/4675), [nimbus#5692](https://github.com/status-im/nimbus-eth2/pull/5692), [lodestar#6230](https://github.com/ChainSafe/lodestar/pull/6230)

</details>


<a id="logging_metrics-027"></a>
<details>
<summary><b>logging_metrics-027</b> Demote or remove per-message logs on hot paths — <i>implemented · medium · cpu, disk</i></summary>

**Idea.** Log per-message, per-peer, per-attestation and per-validator-loop events at debug/trace or not at all, instead of info/warn, because they scale with peers and validators and their formatting and writing cost CPU and disk; metrics already cover the outcome.

**Best measured result.** pr:nimbus#5776: 2000 addMapping calls 40 ms -&gt; 6.5e-05 s after removing loop logging

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1747`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1747) remaining warn!/info! are block-level or rejection paths, not per-attestation
- [`beacon_node/beacon_chain/src/validator_monitor.rs:439`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_monitor.rs#L439) per-validator logs gated by individual_tracking

**Sources.** [ethlambda#586](https://github.com/lambdaclass/ethlambda/pull/586), [lodestar@1822944a7](https://github.com/ChainSafe/lodestar/commit/1822944a7021), [lighthouse#2395](https://github.com/sigp/lighthouse/pull/2395), [prysm#7928](https://github.com/OffchainLabs/prysm/pull/7928), [nimbus#7673](https://github.com/status-im/nimbus-eth2/pull/7673), [lodestar#4040](https://github.com/ChainSafe/lodestar/pull/4040), [prysm#3680](https://github.com/OffchainLabs/prysm/pull/3680), [lighthouse#9436](https://github.com/sigp/lighthouse/pull/9436), [caplin#24702](https://github.com/erigontech/erigon/pull/24702), [caplin#22483](https://github.com/erigontech/erigon/pull/22483), [nimbus#5776](https://github.com/status-im/nimbus-eth2/pull/5776), [lodestar#3893](https://github.com/ChainSafe/lodestar/pull/3893)

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

**Sources.** [nimbus#7058](https://github.com/status-im/nimbus-eth2/pull/7058), [ethlambda#587](https://github.com/lambdaclass/ethlambda/pull/587), [prysm#16210](https://github.com/OffchainLabs/prysm/pull/16210)

</details>


<a id="logging_metrics-036"></a>
<details>
<summary><b>logging_metrics-036</b> Persist debug objects to disk only behind a flag — <i>implemented · low · disk, cpu</i></summary>

**Idea.** Write invalid SSZ objects or state dumps to disk only when a debug flag is set, and never write a full state every slot by default, so production nodes do not spend disk I/O on debug data.

**Impact.** Already opt-in; no per-slot state dump found.

**Best measured result.** pr:prysm#15226: 'writing a state to disk every slot is resource-intensive'

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/config.rs:142`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L142) invalid_block_storage: Option&lt;PathBuf&gt;, default None (config.rs:379)
- [`beacon_node/network/src/service.rs:338`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L338) InvalidBlockStorage::Enabled only when path is set

**Sources.** [lodestar#3797](https://github.com/ChainSafe/lodestar/pull/3797), [prysm#15226](https://github.com/OffchainLabs/prysm/pull/15226)

</details>


<a id="logging_metrics-040"></a>
<details>
<summary><b>logging_metrics-040</b> Skip epoch metrics when head is stale — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** Skip computing epoch participation metrics that need an old state when the head is far behind the wall-clock slot, so stalls do not trigger expensive state loads.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:4931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4931) import_block_update_validator_monitor returns early when block is older than VALIDATOR_MONITOR_HISTORIC_EPOCHS
- [`beacon_node/beacon_chain/src/validator_monitor.rs:1885`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_monitor.rs#L1885) scrape_metrics uses only in-memory summaries, no old-state load

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

**Sources.** [nimbus#2090](https://github.com/status-im/nimbus-eth2/pull/2090)

</details>


<a id="logging_metrics-042"></a>
<details>
<summary><b>logging_metrics-042</b> No per-validator data in periodic status line — <i>implemented · low · cpu, latency</i></summary>

**Idea.** Do not compute per-validator balances or status for the periodic status/log line, because it needs a linear scan over validators and forced public key decompression.

**Impact.** Status line uses chain head/sync/peer info, no validator scan.

**Best measured result.** commit:nimbus@10da7fe9dada: not viable at higher validator counts - linear scan + forced public key init makes it extremely slow

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/client/src/notifier.rs:42`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/notifier.rs#L42) spawn_notifier: no per-validator balance/status grep hits

**Sources.** [nimbus@10da7fe9d](https://github.com/status-im/nimbus-eth2/commit/10da7fe9dada), [nimbus#1475](https://github.com/status-im/nimbus-eth2/pull/1475)

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

**Sources.** [prysm#14864](https://github.com/OffchainLabs/prysm/pull/14864), [prysm#2236](https://github.com/OffchainLabs/prysm/pull/2236), [prysm#7655](https://github.com/OffchainLabs/prysm/pull/7655), [lighthouse#7707](https://github.com/sigp/lighthouse/pull/7707), [prysm#7061](https://github.com/OffchainLabs/prysm/pull/7061)

</details>


<a id="logging_metrics-051"></a>
<details>
<summary><b>logging_metrics-051</b> Gzip-compress metrics endpoint responses — <i>implemented · low · bandwidth</i></summary>

**Idea.** Compress the HTTP metrics endpoint response with gzip when the scraper sends Accept-Encoding gzip, shrinking each scrape by an order of magnitude.

**Impact.** Metrics scrape already compressed (~90% smaller).

**Best measured result.** pr:lighthouse#10338: ~966 KB to ~76 KB per scrape, ~92% reduction

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_metrics/src/lib.rs:120`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_metrics/src/lib.rs#L120) .layer(CompressionLayer::new()) (tower-http, honors Accept-Encoding)
- [`beacon_node/http_metrics/Cargo.toml`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_metrics/Cargo.toml) dev-dep flate2 for test

**Sources.** [lighthouse#10338](https://github.com/sigp/lighthouse/pull/10338)

</details>


