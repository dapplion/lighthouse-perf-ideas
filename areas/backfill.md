# backfill

41 ideas: 4 not, 7 partial, 20 implemented, 10 n/a; 3 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [backfill-001](#backfill-001) | Backfill only to the block-request retention window | implemented | high | S | disk, bandwidth, sync, cpu |
| [backfill-002](#backfill-002) **★** | Use fork-specific shorter block-request window for backfill | not | medium | S | bandwidth, disk, sync |
| [backfill-003](#backfill-003) | Custody backfill fetches only custodied columns | implemented | medium | S | bandwidth, cpu |
| [backfill-004](#backfill-004) | Ask each peer only for its column subset | implemented | medium | S | bandwidth |
| [backfill-005](#backfill-005) **★** | Per-peer fault attribution and partial retry in backfill | partial | medium | M | sync, bandwidth |
| [backfill-006](#backfill-006) | Run backfill only when forward sync is at head | implemented | low | S | sync, bandwidth, cpu |
| [backfill-007](#backfill-007) | Batch KZG verification of backfilled columns | partial | low | S | cpu, disk |
| [backfill-008](#backfill-008) | Low-priority batchable BLS verification for backfill | implemented | low | S | cpu |
| [backfill-009](#backfill-009) | Dedicated low-priority thread pool for backfill | implemented | medium | S | cpu, latency, sync |
| [backfill-010](#backfill-010) | Lowest work-queue priority for backfill segments | implemented | low | S | latency, cpu |
| [backfill-011](#backfill-011) | Rate-limit backfill batch processing per slot | implemented | low | S | cpu, sync, disk |
| [backfill-012](#backfill-012) | Pace backfill on completed disk writes | implemented | low | S | disk, sync |
| [backfill-013](#backfill-013) | Smaller column custody backfill batch size | implemented | low | S | cpu, sync |
| [backfill-014](#backfill-014) | Cap number of buffered backfill batches | implemented | low | S | cpu, bandwidth |
| [backfill-015](#backfill-015) | Size backfill batches by peer earliest available slot | implemented | low | S | sync |
| [backfill-016](#backfill-016) | Do not retry batches outside peers' serve range | partial | low | S | bandwidth, sync |
| [backfill-017](#backfill-017) | Skip data columns older than retention floor | implemented | low | S | sync, disk |
| [backfill-018](#backfill-018) **★** | Backfill history from era files or snapshots | not | medium | L | sync, bandwidth, disk, startup |
| [backfill-019](#backfill-019) | Dedicated backward historical block downloader | implemented | low | S | sync, disk |
| [backfill-020](#backfill-020) | Write downloaded history directly to snapshot format | n/a | low |  | sync, disk |
| [backfill-021](#backfill-021) | Diff-based historical state reconstruction | partial | low | M | cpu, disk |
| [backfill-022](#backfill-022) | Resumable historical state reconstruction | implemented | low | S | startup, cpu |
| [backfill-023](#backfill-023) | Stop backfill loop early, fewer DB lookups | n/a | low |  | cpu, sync |
| [backfill-024](#backfill-024) | Parallel pipelined block range requests in backfill | implemented | low | S | sync, latency, cpu |
| [backfill-025](#backfill-025) | Cheap has-block check before backfilling EL blocks | n/a | low |  | sync, bandwidth |
| [backfill-026](#backfill-026) | Cursor-based custody column backfiller | implemented | low | S | bandwidth, sync, disk |
| [backfill-027](#backfill-027) | Persistent coverage bitmap for backfilled data | n/a | low |  | sync, disk, bandwidth |
| [backfill-028](#backfill-028) | Verify backfill signatures off the storage thread | implemented | low | S | cpu, disk, sync |
| [backfill-029](#backfill-029) | Per-batch EL fork-choice update during backfill | n/a | low |  | disk, memory |
| [backfill-030](#backfill-030) | Persist downloaded-not-imported blocks across restart | not | low | M | startup, sync, bandwidth |
| [backfill-031](#backfill-031) | Reuse preallocated buffers when encoding backfilled blocks | n/a | low |  | memory, cpu |
| [backfill-032](#backfill-032) | Remove unused legacy backfill bookkeeping writes | n/a | low |  | disk |
| [backfill-033](#backfill-033) | Reuse received block roots and bytes in backfill | partial | low | M | cpu, sync |
| [backfill-034](#backfill-034) | Short pubkey cache lock in backfill signature checks | partial | low | S | latency, cpu |
| [backfill-035](#backfill-035) | Skip history download stage when backfill disabled | not | low | S | bandwidth, sync |
| [backfill-036](#backfill-036) | Skip genesis block signature check in backfill | implemented | low | S | cpu |
| [backfill-037](#backfill-037) | Checkpoint sync from finalized state only | partial | low | M | startup, sync, bandwidth |
| [backfill-038](#backfill-038) | Lock-free progress counters in backward block downloader | n/a | low |  | cpu |
| [backfill-039](#backfill-039) | Use canonical block root for backfill blob and column lookups | n/a | low |  | sync, bandwidth, disk |
| [backfill-040](#backfill-040) | Record backfill progress at anchor block slot | n/a | low |  | sync, disk |
| [backfill-041](#backfill-041) | Persist custody group count immediately on change | implemented | low | S | bandwidth, disk, sync |

★ actionable. Click an id for the full record.

## Ideas

<a id="backfill-001"></a>
<details>
<summary><b>backfill-001</b> Backfill only to the block-request retention window — <i>implemented · high · S · disk, bandwidth, sync, cpu</i></summary>

**Idea.** After checkpoint sync, backfill blocks (and blobs) only back to the weak subjectivity / MIN_EPOCHS_FOR_BLOCK_REQUESTS boundary instead of genesis, with full history opt-in. Older blocks are not servable on the network, so this cuts download, verification and disk.

**Impact.** None; already in place.

**Best measured result.** stops syncing back to genesis; only about the last 5 months of blocks are downloaded (pr:lighthouse#4082)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/builder.rs:942`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L942) genesis_backfill_slot = now - (min_validator_withdrawability_delay + churn_limit_quotient/2) epochs (= 33024, MIN_EPOCHS_FOR_BLOCK_REQUESTS) unless --genesis-backfill
- [`beacon_node/network/src/sync/backfill_sync/mod.rs:1088`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/backfill_sync/mod.rs#L1088) reset_start_epoch/check_completed stop at genesis_backfill_slot
- [`beacon_node/network/src/sync/backfill_sync/mod.rs:1110`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/backfill_sync/mod.rs#L1110) would_complete compares against genesis_backfill_slot
- [`beacon_node/beacon_chain/src/historical_blocks.rs:473`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_blocks.rs#L473) backfill completion uses the same boundary

**Skeptic check.** Confirmed that the boundary equals MIN_EPOCHS_FOR_BLOCK_REQUESTS (256 + 65536/2 = 33024 epochs) and that full history is opt-in. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#3943](https://github.com/sigp/lighthouse/pull/3943), [lighthouse#4082](https://github.com/sigp/lighthouse/pull/4082), [grandine#94](https://github.com/grandinetech/grandine/pull/94), [nimbus#4421](https://github.com/status-im/nimbus-eth2/pull/4421), [grandine@e35b912a4](https://github.com/grandinetech/grandine/commit/e35b912a4598), [teku#6581](https://github.com/Consensys-Incorporated/teku/pull/6581)

</details>


<a id="backfill-002"></a>
<details>
<summary><b>backfill-002</b> Use fork-specific shorter block-request window for backfill — <i>not · medium · S · bandwidth, disk, sync</i></summary>

**Idea.** Compute the backfill stop point from the current fork's block-request window (e.g. 14299 instead of 33024 epochs on mainnet) rather than the legacy constant, so less history is downloaded and stored.

**Gap in Lighthouse.** The backfill stop slot uses the withdrawability+churn formula. Add a fork-aware compute_min_epochs_for_block_requests to ChainSpec (Gloas mainnet: 14299) and use it for genesis_backfill_slot (upstream PR 10270 is still open).

**Impact.** Backfill would stop ~18.7k epochs (~58%) earlier after checkpoint sync under Gloas, so about 2.5x less block download, verification and storage for backfill.

**Best measured result.** 33024 to 14299 epochs mainnet (pr:lighthouse#10270)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/builder.rs:941-964`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L941-L964) genesis_backfill_slot = now - (min_validator_withdrawability_delay + churn_limit_quotient/2)
- [`consensus/types/src/core/chain_spec.rs:297`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/core/chain_spec.rs#L297),1949,2585 min_epochs_for_block_requests is a single fixed u64 (33024), with no fork-dependent compute function and no consumer outside chain_spec.rs

**Second check.** Grepped the whole tree for min_epochs_for_block_requests: all hits are in chain_spec.rs (field, config, defaults). No other fork-aware backfill window exists in builder.rs or in the backfill sync.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [lighthouse#10270](https://github.com/sigp/lighthouse/pull/10270)

</details>


<a id="backfill-003"></a>
<details>
<summary><b>backfill-003</b> Custody backfill fetches only custodied columns — <i>implemented · medium · S · bandwidth, cpu</i></summary>

**Idea.** In data-column custody backfill, request only the columns the node custodies, not the full sampling set, because extra columns are verified and then discarded.

**Impact.** None; already in place.

**Best measured result.** halves download for 4 of 8 columns (pr:lighthouse#8916)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/custody_backfill_sync/mod.rs:454`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/custody_backfill_sync/mod.rs#L454) batch built with ByRangeRequestType::Columns(get_missing_columns_for_epoch)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7963`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7963) get_missing_columns_for_epoch diffs custody_columns_for_epoch(head) vs epoch
- [`beacon_node/beacon_chain/src/custody_context.rs:525`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L525) custody_columns_for_epoch returns custody subset, not sampling_columns_for_epoch
- [`beacon_node/network/src/sync/custody_backfill_sync/mod.rs:395`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/custody_backfill_sync/mod.rs#L395) epochs with nothing missing are skipped

**Skeptic check.** Verified that the request set is the custody set minus what is already held, not the sampling set, which is the PR #8916 mechanism.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#8916](https://github.com/sigp/lighthouse/pull/8916)

</details>


<a id="backfill-004"></a>
<details>
<summary><b>backfill-004</b> Ask each peer only for its column subset — <i>implemented · medium · S · bandwidth</i></summary>

**Idea.** When requesting data columns for custody backfill, choose peers by the requested column set and send each peer a request for only the columns it serves, instead of the full request to every peer, to avoid N-times download amplification.

**Impact.** None; already in place.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context.rs:1607`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L1607) custody_backfill_data_columns_batch_request
- [`beacon_node/network/src/sync/network_context.rs:578`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L578) select_columns_by_range_peers_to_request assigns each column to one custodial peer
- [`beacon_node/network/src/sync/network_context.rs:1630`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L1630) each peer gets DataColumnsByRangeRequest with only its assigned columns

**Skeptic check.** Confirmed per-peer column grouping: each column goes to exactly one custody peer, so there is no N-times amplification. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#10048](https://github.com/sigp/lighthouse/pull/10048)

</details>


<a id="backfill-005"></a>
<details>
<summary><b>backfill-005</b> Per-peer fault attribution and partial retry in backfill — <i>partial · medium · M · sync, bandwidth</i></summary>

**Idea.** Apply range-sync style per-peer fault attribution and retry of only the missing columns to backfill batches, so one bad peer does not fail and re-download whole batches.

**Gap in Lighthouse.** Block backfill (and range sync) ignore faulty_peers from CouplingError::DataColumnPeerFailure and re-download the whole batch. They need to penalise the faulty column peers and re-request only the missing columns. Custody backfill has attribution but still re-requests the whole batch.

**Impact.** Fewer repeated full-batch downloads when one peer misbehaves. It matters only during backfill with bad peers, so the gain is small.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/backfill_sync/mod.rs:325`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/backfill_sync/mod.rs#L325) DataColumnPeerFailure is only debug-logged; download_failed(Some(*peer_id)) at :349 blames the batch peer, not the faulty column peers, and send_batch re-requests the whole batch
- [`beacon_node/network/src/sync/range_sync/chain.rs:929`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L929) range sync handles it the same way (log only)
- [`beacon_node/network/src/sync/custody_backfill_sync/mod.rs:604-625`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/custody_backfill_sync/mod.rs#L604-L625) custody backfill reports the faulty column peers (LowToleranceError) but still calls send_batch for the full batch
- [`beacon_node/network/src/sync/range_data_column_batch_request.rs:103-112`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_data_column_batch_request.rs#L103-L112) drops faulty peers' requests from the custody-backfill request map, but the caller removes the whole entry on error (network_context.rs:1665-1690), so no partial retry follows
- [`beacon_node/network/src/sync/tests/range.rs:635`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/tests/range.rs#L635) comment names retry_partial_batch, but no such function exists in the tree (stale)

**Second check.** Checked RangeDataColumnBatchRequest, network_context's on_rpc_response_result scoring and the retry_partial_batch name from the tests. Partial retry is not there: the test comment is stale, and the request entry is removed before any retry.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [lighthouse#7762](https://github.com/sigp/lighthouse/pull/7762)

</details>


<a id="backfill-006"></a>
<details>
<summary><b>backfill-006</b> Run backfill only when forward sync is at head — <i>implemented · low · S · sync, bandwidth, cpu</i></summary>

**Idea.** Do not start backfill workers until the node has synced to head, and pause them whenever it falls back into range sync, so backfill does not take peers, rate-limit budget, CPU and bandwidth from forward sync and duties.

**Impact.** Backfill does not compete with forward range sync; already in place.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/manager.rs:684`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L684) backfill_sync.start() only when sync_state is Synced
- [`beacon_node/network/src/sync/manager.rs:704`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L704) custody backfill starts only after block backfill complete
- [`beacon_node/network/src/sync/manager.rs:744`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L744) backfill_sync.pause() + custody pause on RangeSyncType::Finalized
- [`beacon_node/network/src/sync/manager.rs:756`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L756) same on RangeSyncType::Head
- [`beacon_node/network/src/sync/backfill_sync/mod.rs:874`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/backfill_sync/mod.rs#L874) send_batch refuses while Paused

**Skeptic check.** Verified update_sync_state: backfill and custody backfill start only in Synced and are paused whenever range sync (finalized or head) is active. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#13623](https://github.com/OffchainLabs/prysm/pull/13623), [nimbus#3263](https://github.com/status-im/nimbus-eth2/pull/3263), [nimbus#7191](https://github.com/status-im/nimbus-eth2/pull/7191), [prysm#15702](https://github.com/OffchainLabs/prysm/pull/15702), [teku#3199](https://github.com/Consensys-Incorporated/teku/pull/3199)

</details>


<a id="backfill-007"></a>
<details>
<summary><b>backfill-007</b> Batch KZG verification of backfilled columns — <i>partial · low · S · cpu, disk</i></summary>

**Idea.** Verify the KZG proofs of backfilled data columns as one batch per segment instead of one at a time, which lowers CPU and storage pressure.

**Gap in Lighthouse.** In block backfill (and forward range sync), batch_verify_kzg_for_range_sync_blocks calls verify_columns_against_block once per block, so data columns are batched per block, not per segment as blobs are. validate_full_data_columns already takes commitments from each sidecar, so all columns of the segment could go into one validate_full_data_columns / validate_data_columns_with_commitments call (Gloas: per-column commitments from each block's bid).

**Impact.** Saves the fixed per-call pairing check and shares per-column-index interpolation across ~32 blocks per backfill batch; modest CPU saving in backfill and range sync. The per-column-to-batch gain silver#209 got is already in Lighthouse.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/historical_data_columns.rs:182`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_data_columns.rs#L182) custody backfill: one batched KZG call per epoch (Gloas)
- [`beacon_node/beacon_chain/src/historical_data_columns.rs:190`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_data_columns.rs#L190) custody backfill: verify_kzg_for_data_column_list over the whole epoch (Fulu)
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:676`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L676) block backfill calls batch_verify_kzg_for_range_sync_blocks
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:507`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L507) 'Fulu columns carry their own commitments, so verify per block' - one KZG batch call per block
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:515`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L515) Gloas envelope columns also per block
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:521`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L521) only blobs are batched across the whole segment

**Skeptic check.** Custody column backfill really batches per epoch, and no path verifies column by column. But the main block backfill path batches columns per block, not per segment. Earlier evidence cited sync_methods.rs:676 as segment-batched, which is true only for blobs.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [silver#209](https://github.com/gattaca-com/silver/pull/209)

</details>


<a id="backfill-008"></a>
<details>
<summary><b>backfill-008</b> Low-priority batchable BLS verification for backfill — <i>implemented · low · S · cpu</i></summary>

**Idea.** Submit backfill signature sets to the BLS verifier in low-priority batchable mode so they are aggregated with other sets and never delay head-block signature work.

**Impact.** Backfill signature work is already batched and confined to a quarter of the CPUs, so head-block BLS is not delayed.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/historical_blocks.rs:393-415`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_blocks.rs#L393-L415) one ParallelSignatureSets batch per backfill segment
- [`beacon_node/beacon_processor/src/lib.rs:1726-1731`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1726-L1731) ChainSegmentBackfill on RayonPoolType::LowPriority
- [`common/task_executor/src/rayon_pool_provider.rs:4`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/task_executor/src/rayon_pool_provider.rs#L4),26-33 low-priority pool is 25% of CPUs
- [`beacon_node/beacon_processor/src/lib.rs:135`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L135) enable_backfill_rate_limiting defaults true

**Skeptic check.** Confirmed batch verification per segment on the throttled pool, which is on by default; this reaches the same goal as Lodestar's batchable mode, by other means.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#3786](https://github.com/ChainSafe/lodestar/pull/3786)

</details>


<a id="backfill-009"></a>
<details>
<summary><b>backfill-009</b> Dedicated low-priority thread pool for backfill — <i>implemented · medium · S · cpu, latency, sync</i></summary>

**Idea.** Run backfill segment validation (signatures, KZG) on a separate low-priority executor or thread pool so its compute cannot contend with latency-critical block and attestation import.

**Impact.** Backfill compute is confined to ~25% of cores; already in place.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:1726`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1726) Work::ChainSegmentBackfill spawned with spawn_blocking_with_rayon(RayonPoolType::LowPriority) when rate limiting is on (default)
- [`beacon_node/../common/task_executor/src/lib.rs:231`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/../common/task_executor/src/lib.rs#L231) thread_pool.install() so the inner rayon par_iter (signature sets) runs in the low-priority pool
- [`beacon_node/../common/task_executor/src/rayon_pool_provider.rs:4`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/../common/task_executor/src/rayon_pool_provider.rs#L4) low-priority pool is 25% of CPUs
- [`beacon_node/network/src/network_beacon_processor/mod.rs:635`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L635) custody backfill (send_historic_data_columns) also uses Work::ChainSegmentBackfill

**Skeptic check.** Verified that both block backfill and custody column backfill run inside a dedicated 25% rayon pool via install(), so parallel signature verification stays in that pool. Earlier evidence correct (lighthouse#7924).

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine@a1c626531](https://github.com/grandinetech/grandine/commit/a1c626531e49), [grandine#542](https://github.com/grandinetech/grandine/pull/542), [lighthouse#7924](https://github.com/sigp/lighthouse/pull/7924)

</details>


<a id="backfill-010"></a>
<details>
<summary><b>backfill-010</b> Lowest work-queue priority for backfill segments — <i>implemented · low · S · latency, cpu</i></summary>

**Idea.** In the beacon processor work queue, give backfill chain segments the lowest priority so they never starve gossip blocks and attestations near head.

**Impact.** Already in place (Lighthouse PR 3215 and later rate limiting).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:1156`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1156) backfill_chain_segment popped after gossip blocks, attestations, sync messages, RPC and api_request_p1
- [`beacon_node/beacon_processor/src/lib.rs:812-848`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L812-L848) backfill events routed through reprocess queue schedule
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:96`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L96) BACKFILL_SCHEDULE_IN_SLOT

**Skeptic check.** Verified that the backfill queue is near the end of the priority chain, below everything near head except light-client work, and is also time-scheduled within the slot.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#3215](https://github.com/sigp/lighthouse/pull/3215)

</details>


<a id="backfill-011"></a>
<details>
<summary><b>backfill-011</b> Rate-limit backfill batch processing per slot — <i>implemented · low · S · cpu, sync, disk</i></summary>

**Idea.** Queue backfill batches and release only a fixed number (e.g. one to three) at set points in each slot, so backfill throughput is throttled and does not compete with block and attestation processing.

**Impact.** At most three backfill batches per slot; already in place.

**Best measured result.** CPU usage during backfill reduced by ~5% - 20% on Goerli (pr:lighthouse#3936)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:135`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L135) enable_backfill_rate_limiting default true
- [`beacon_node/beacon_processor/src/lib.rs:813`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L813) backfill work events diverted into the reprocess queue
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:96`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L96) BACKFILL_SCHEDULE_IN_SLOT 1/2, 3/5, 4/5 of slot
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:1320`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L1320) ReadyBackfillSync releases one batch per scheduled time

**Skeptic check.** Verified the ChainSegmentBackfill work (block and custody column backfill) is queued and released at three points per slot. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#3936](https://github.com/sigp/lighthouse/pull/3936), [silver#199](https://github.com/gattaca-com/silver/pull/199)

</details>


<a id="backfill-012"></a>
<details>
<summary><b>backfill-012</b> Pace backfill on completed disk writes — <i>implemented · low · S · disk, sync</i></summary>

**Idea.** Mark a backfill batch as done, and request the next one, only after its disk writes complete, with a long settle timeout before retry, so backfill speed follows disk throughput.

**Impact.** Import writes and syncs the DB synchronously before success is reported, and the in-flight buffer is bounded, so backfill speed follows disk throughput.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/historical_blocks.rs:430-480`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_blocks.rs#L430-L480) blobs/hot/cold do_atomically plus sync() before returning
- [`beacon_node/network/src/sync/backfill_sync/mod.rs:49`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/backfill_sync/mod.rs#L49) BACKFILL_BATCH_BUFFER_SIZE=5
- [`beacon_node/network/src/sync/backfill_sync/mod.rs:700-706`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/backfill_sync/mod.rs#L700-L706) processing_target advances and request_batches runs only after processing result

**Skeptic check.** Confirmed that the writes are synchronous, with an explicit sync, inside import_historical_block_batch before the batch result returns; the earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [silver#207](https://github.com/gattaca-com/silver/pull/207)

</details>


<a id="backfill-013"></a>
<details>
<summary><b>backfill-013</b> Smaller column custody backfill batch size — <i>implemented · low · S · cpu, sync</i></summary>

**Idea.** Use a small batch size for data-column custody backfill (e.g. 3 instead of 10 slots) so each batch leaves CPU for duties on supernodes.

**Impact.** Custody backfill is time-scheduled within the slot, runs at lowest priority on a 25%-CPU pool, so duties keep CPU; batch size is one epoch, larger than Teku's 3, but the throttling is achieved by scheduling instead.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/custody_backfill_sync/mod.rs:40`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/custody_backfill_sync/mod.rs#L40) CUSTODY_BACKFILL_EPOCHS_PER_BATCH=1
- [`beacon_node/network/src/network_beacon_processor/mod.rs:634-650`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L634-L650) send_historic_data_columns uses Work::ChainSegmentBackfill
- [`beacon_node/beacon_processor/src/lib.rs:812-848`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L812-L848),1726-1731 same rate-limit schedule and LowPriority pool as block backfill

**Skeptic check.** Same goal (leave CPU for duties on supernodes) reached through scheduling and the pool rather than batch size; the earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#10356](https://github.com/Consensys-Incorporated/teku/pull/10356)

</details>


<a id="backfill-014"></a>
<details>
<summary><b>backfill-014</b> Cap number of buffered backfill batches — <i>implemented · low · S · cpu, bandwidth</i></summary>

**Idea.** Limit the number of backfill batches buffered in flight to the forward-sync level (e.g. 5 instead of 20), so fewer heavy multi-peer column requests are created and retried.

**Impact.** Already capped at 5.

**Best measured result.** 20 -&gt; 5 batches (pr:lighthouse#7958)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/backfill_sync/mod.rs:49`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/backfill_sync/mod.rs#L49) BACKFILL_BATCH_BUFFER_SIZE = 5
- [`beacon_node/network/src/sync/backfill_sync/mod.rs:1012`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/backfill_sync/mod.rs#L1012) include_next_batch stops at 5 Downloading/AwaitingProcessing batches
- [`beacon_node/network/src/sync/custody_backfill_sync/mod.rs:32`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/custody_backfill_sync/mod.rs#L32) same cap
- [`beacon_node/network/src/sync/custody_backfill_sync/mod.rs:434`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/custody_backfill_sync/mod.rs#L434) enforced in include_next_batch

**Skeptic check.** Verified the cap in both block and custody backfill. Earlier evidence correct (lighthouse#7958).

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#7958](https://github.com/sigp/lighthouse/pull/7958)

</details>


<a id="backfill-015"></a>
<details>
<summary><b>backfill-015</b> Size backfill batches by peer earliest available slot — <i>implemented · low · S · sync</i></summary>

**Idea.** Adjust backfill batch ranges using each peer's advertised earliest available slot so requests are not sent for ranges the peer cannot serve.

**Impact.** Peers that cannot serve a batch are never asked for it.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/peerdb.rs:250-264`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/peerdb.rs#L250-L264) synced_peers_for_epoch filters on earliest_available_slot
- [`beacon_node/network/src/sync/backfill_sync/mod.rs:46`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/backfill_sync/mod.rs#L46) one-epoch batches so the start-slot filter covers the whole batch
- [`beacon_node/network/src/sync/backfill_sync/mod.rs:879-893`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/backfill_sync/mod.rs#L879-L893) send_batch
- [`beacon_node/network/src/sync/custody_backfill_sync/mod.rs:995`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/custody_backfill_sync/mod.rs#L995),1038-1059

**Skeptic check.** Verified the filter on both the block and the custody backfill paths; because batches are one epoch, excluding peers per batch has the same effect as resizing ranges.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine@582376bb8](https://github.com/grandinetech/grandine/commit/582376bb8bdc)

</details>


<a id="backfill-016"></a>
<details>
<summary><b>backfill-016</b> Do not retry batches outside peers&#x27; serve range — <i>partial · low · S · bandwidth, sync</i></summary>

**Idea.** When a backfill blob/column batch falls outside the range peers are required to serve, drop it instead of retrying, since no peer will ever return it.

**Gap in Lighthouse.** Peer filter and batch_type avoid most out-of-range requests, but there is no explicit drop of a batch that no peer can serve; backfill_sync send_batch would pause/fail instead.

**Impact.** Avoids rare stalls or retries when peer status is stale; negligible CPU/bandwidth.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/backfill_sync/mod.rs:883-936`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/backfill_sync/mod.rs#L883-L936) no peers in range pauses backfill (NoPeer) rather than dropping the batch
- [`beacon_node/network/src/sync/network_context.rs:1296-1318`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L1296-L1318) batch_type requests columns/blobs only inside DA window

**Sources.** [grandine@9fb494002](https://github.com/grandinetech/grandine/commit/9fb49400200e), [grandine#119](https://github.com/grandinetech/grandine/pull/119)

</details>


<a id="backfill-017"></a>
<details>
<summary><b>backfill-017</b> Skip data columns older than retention floor — <i>implemented · low · S · sync, disk</i></summary>

**Idea.** Do not require or fetch data columns for backfilled blocks older than the column retention floor, so backfill windows do not stall waiting for data that is never fetched.

**Impact.** Columns older than the retention floor are neither requested nor awaited pre-Gloas.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context.rs:1296-1318`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L1296-L1318) batch_type returns Blocks when outside DA window
- [`beacon_node/beacon_chain/src/custody_context.rs:585-587`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L585-L587) data_columns_required_for_epoch gated on da_check_required_for_epoch
- [`beacon_node/network/src/sync/custody_backfill_sync/mod.rs:391`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/custody_backfill_sync/mod.rs#L391) column_data_availability_boundary

**Skeptic check.** Confirmed for current forks. One caveat: batch_type always requests columns for Gloas epochs (TODO at network_context.rs:1305), so the floor is not applied post-Gloas, but that fork is not live yet.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [silver#304](https://github.com/gattaca-com/silver/pull/304)

</details>


<a id="backfill-018"></a>
<details>
<summary><b>backfill-018</b> Backfill history from era files or snapshots — <i>not · medium · L · sync, bandwidth, disk, startup</i></summary>

**Idea.** Read finalized history from era files or downloadable prebuilt block snapshots and use them to backfill after checkpoint sync, instead of downloading each block from peers.

**Gap in Lighthouse.** Add an era-file (or snapshot) reader that feeds historical blocks into import_historical_block_batch as a source other than peers, plus file fetch and a CLI flag. Era files carry blocks and state but not blobs or columns.

**Impact.** Would replace peer download of the ~5-month backfill window (hundreds of thousands of blocks, many GB) with a file read. Saves peer bandwidth and sync time, not steady-state cost.

**Best measured result.** expected to cut backfill to download time of the files; front-fill loads mainnet in about 10s (pr:nimbus#3394)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/historical_blocks.rs:84`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_blocks.rs#L84) import_historical_block_batch has one non-test caller: [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:692`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L692) (peer-downloaded backfill batches)
- Cargo.lock has no era/e2store crate; a whole-word grep for era/e2store over .rs/.md/.toml finds nothing

**Second check.** Checked the dependency list for any era/e2store crate and every caller of the historical import. Checkpoint sync fetches only the anchor state and block, so no non-peer history source exists.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [nimbus#3394](https://github.com/status-im/nimbus-eth2/pull/3394), [nimbus#4283](https://github.com/status-im/nimbus-eth2/pull/4283), [caplin#8665](https://github.com/erigontech/erigon/pull/8665)

</details>


<a id="backfill-019"></a>
<details>
<summary><b>backfill-019</b> Dedicated backward historical block downloader — <i>implemented · low · S · sync, disk</i></summary>

**Idea.** Have a dedicated backfill service that downloads finalized blocks backward by range and writes them straight to the block store, separate from forward sync.

**Impact.** Already a separate backward service that writes batches straight to the store without state transition.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/backfill_sync/mod.rs:46`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/backfill_sync/mod.rs#L46) BACKFILL_EPOCHS_PER_BATCH, separate backward BackFillSync service
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:561`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L561) process_chain_segment_backfill
- [`beacon_node/beacon_chain/src/historical_blocks.rs:84`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_blocks.rs#L84) import_historical_block_batch
- [`beacon_node/beacon_chain/src/historical_blocks.rs:432-448`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_blocks.rs#L432-L448) direct do_atomically writes to blobs/hot/cold DBs

**Skeptic check.** Verified backfill is a distinct sync state machine downloading backward by range and import_historical_block_batch writes blocks directly to the DBs. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#6435](https://github.com/erigontech/erigon/pull/6435), [caplin#8016](https://github.com/erigontech/erigon/pull/8016)

</details>


<a id="backfill-020"></a>
<details>
<summary><b>backfill-020</b> Write downloaded history directly to snapshot format — <i>n/a · low · sync, disk</i></summary>

**Idea.** Write downloaded historical blocks straight into the frozen/snapshot (freezer) format instead of first writing them to the hot DB and re-encoding later.

**Impact.** Lighthouse has no separate frozen block format: blocks stay in the hot DB column, so there is no re-encode step to skip.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/historical_blocks.rs:197-230`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_blocks.rs#L197-L230) blocks to hot_db ops, block roots to cold_batch

**Sources.** [caplin#8459](https://github.com/erigontech/erigon/pull/8459)

</details>


<a id="backfill-021"></a>
<details>
<summary><b>backfill-021</b> Diff-based historical state reconstruction — <i>partial · low · M · cpu, disk</i></summary>

**Idea.** Reconstruct historical states from per-epoch diffs plus periodic full dumps, in parallel, instead of storing full states, so archive nodes serve old states with small storage.

**Gap in Lighthouse.** Reconstruction replays slots in one thread. Independent hierarchy segments (between snapshots) could be replayed in parallel from reconstruct_historic_states_on_range.

**Impact.** Archive nodes only: faster one-off full-history reconstruction (up to roughly core-count speedup). No effect on normal nodes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hdiff.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs) hierarchical diffs
- [`beacon_node/store/src/reconstruct.rs:131-200`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/reconstruct.rs#L131-L200) reconstruction is one sequential loop

**Sources.** [caplin#8817](https://github.com/erigontech/erigon/pull/8817)

</details>


<a id="backfill-022"></a>
<details>
<summary><b>backfill-022</b> Resumable historical state reconstruction — <i>implemented · low · S · startup, cpu</i></summary>

**Idea.** Persist the last reconstructed slot so historical state reconstruction resumes after a restart instead of starting over.

**Impact.** Progress is persisted at each commit and reconstruction resumes from state_lower_limit after restart.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/reconstruct.rs:57-77`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/reconstruct.rs#L57-L77) on_commit persists anchor.state_lower_limit via compare_and_set_anchor_info_with_write
- [`beacon_node/store/src/reconstruct.rs:188`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/reconstruct.rs#L188) on_commit called on every hierarchy commit
- [`beacon_node/beacon_chain/src/builder.rs:1158-1160`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L1158-L1160) process_reconstruction on startup
- [`beacon_node/beacon_chain/src/migrate.rs:221-235`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L221-L235) run_reconstruction batches and requeues

**Skeptic check.** Verified reconstruct_historic_states starts from anchor.state_lower_limit, writes the raised limit on each commit, and the builder restarts reconstruction at boot. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#8918](https://github.com/erigontech/erigon/pull/8918)

</details>


<a id="backfill-023"></a>
<details>
<summary><b>backfill-023</b> Stop backfill loop early, fewer DB lookups — <i>n/a · low · cpu, sync</i></summary>

**Idea.** In the backfill loop, stop as soon as the range is already covered on disk and avoid repeated has-block/frozen-block DB lookups per iteration, which removes idle CPU burn.

**Impact.** Backfill is event-driven with anchor watermarks, not a polling loop with per-iteration DB lookups, so no idle CPU burn.

**Best measured result.** reduced CPU usage to 0 (pr:caplin#11733)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/backfill_sync/mod.rs:1099`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/backfill_sync/mod.rs#L1099) check_completed
- [`beacon_node/beacon_chain/src/historical_blocks.rs:111`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_blocks.rs#L111) early return when nothing relevant

**Sources.** [caplin#11733](https://github.com/erigontech/erigon/pull/11733)

</details>


<a id="backfill-024"></a>
<details>
<summary><b>backfill-024</b> Parallel pipelined block range requests in backfill — <i>implemented · low · S · sync, latency, cpu</i></summary>

**Idea.** Keep several backfill block-range requests in flight at once, to different peers, and sort/dedupe results before chain checks, so throughput is not limited by one request or one peer.

**Impact.** Backfill already keeps several one-epoch requests in flight to different peers; results are processed in epoch order, so no sort/dedupe step is needed.

**Best measured result.** 27.4 -&gt; 91.6 blk/s median on mainnet (pr:caplin#25417)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/backfill_sync/mod.rs:968`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/backfill_sync/mod.rs#L968) request_batches loops include_next_batch and send_batch until 5 batches are in flight
- [`beacon_node/network/src/sync/backfill_sync/mod.rs:46`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/backfill_sync/mod.rs#L46) BACKFILL_EPOCHS_PER_BATCH = 1
- [`beacon_node/network/src/sync/backfill_sync/mod.rs:888`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/backfill_sync/mod.rs#L888) block_components_by_range_request picks a peer per batch from synced peers, excluding failed peers

**Skeptic check.** Verified pipelined multi-peer backfill requests. Caplin's gain came from moving off one serial request; Lighthouse already pipelines. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#8554](https://github.com/erigontech/erigon/pull/8554), [caplin#15255](https://github.com/erigontech/erigon/pull/15255), [caplin#25417](https://github.com/erigontech/erigon/pull/25417), [nimbus#3371](https://github.com/status-im/nimbus-eth2/pull/3371)

</details>


<a id="backfill-025"></a>
<details>
<summary><b>backfill-025</b> Cheap has-block check before backfilling EL blocks — <i>n/a · low · sync, bandwidth</i></summary>

**Idea.** Before fetching a historical execution payload, ask the EL with a cheap has-block call and stop at the Bellatrix slot or EL snapshot boundary, so only missing blocks are downloaded.

**Impact.** Lighthouse does not backfill execution blocks; the EL syncs itself.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/historical_blocks.rs:84`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_blocks.rs#L84) only CL data stored; no EL backfill

**Sources.** [caplin#9702](https://github.com/erigontech/erigon/pull/9702)

</details>


<a id="backfill-026"></a>
<details>
<summary><b>backfill-026</b> Cursor-based custody column backfiller — <i>implemented · low · S · bandwidth, sync, disk</i></summary>

**Idea.** Run a dedicated, default-on custody column backfiller that works in batches from a persisted earliest-available-column-slot cursor, starts only when in sync, restarts when custody count grows, and advertises the slot to peers.

**Impact.** Already in place, on by default.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/custody_backfill_sync/mod.rs:164`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/custody_backfill_sync/mod.rs#L164) should_start_custody_backfill_sync from the persisted earliest_custodied_data_column_epoch
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7900`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7900) cursor read from store data_column_custody_info
- [`beacon_node/network/src/sync/custody_backfill_sync/mod.rs:224`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/custody_backfill_sync/mod.rs#L224) restart_if_required when cgc at head changes
- [`beacon_node/network/src/sync/manager.rs:704`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L704) starts only when Synced and block backfill complete
- [`beacon_node/network/src/status.rs:33`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/status.rs#L33) status advertises earliest_available_slot from the cursor
- [`beacon_node/beacon_chain/src/historical_data_columns.rs:182`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_data_columns.rs#L182) per-epoch batches

**Skeptic check.** Verified a cursor-based custody backfiller that is on by default (no CLI flag), restarts on custody count change, and advertises the slot. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#10159](https://github.com/Consensys-Incorporated/teku/pull/10159), [teku#10226](https://github.com/Consensys-Incorporated/teku/pull/10226), [teku#10312](https://github.com/Consensys-Incorporated/teku/pull/10312)

</details>


<a id="backfill-027"></a>
<details>
<summary><b>backfill-027</b> Persistent coverage bitmap for backfilled data — <i>n/a · low · sync, disk, bandwidth</i></summary>

**Idea.** Keep a persistent bitmap of which finalized slots have complete blocks, columns and envelopes, and fetch only windows still missing data, instead of scanning disk and probing per column.

**Impact.** Coverage is tracked by contiguous watermarks (oldest block, oldest data, earliest custody epoch) with no per-column scans; a bitmap only helps with holes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/metadata.rs:277`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/metadata.rs#L277) DataInfo.oldest_data_slot
- [`beacon_node/network/src/sync/custody_backfill_sync/mod.rs:323`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/custody_backfill_sync/mod.rs#L323) earliest custodied column epoch
- [`beacon_node/beacon_chain/src/historical_blocks.rs:95`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_blocks.rs#L95) anchor.oldest_block_slot

**Sources.** [silver#243](https://github.com/gattaca-com/silver/pull/243)

</details>


<a id="backfill-028"></a>
<details>
<summary><b>backfill-028</b> Verify backfill signatures off the storage thread — <i>implemented · low · S · cpu, disk, sync</i></summary>

**Idea.** Verify backfilled block signatures in parallel fetcher threads using the batch BLS service, not inside the single-threaded storage write path, so BLS work does not slow storage.

**Impact.** BLS for backfill runs batched and multi-core in a processor worker; there is no single storage thread that it blocks.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/historical_blocks.rs:393-418`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_blocks.rs#L393-L418) one ParallelSignatureSets batch verify before any DB write
- [`consensus/state_processing/src/per_block_processing/block_signature_verifier.rs:455-461`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/block_signature_verifier.rs#L455-L461) blst spreads verification across cores
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:561`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L561) runs in a beacon processor worker, not a storage thread

**Skeptic check.** Verified the batch signature verification is outside the DB critical section and uses parallel blst. Verification and write of one batch are sequential in the same worker (no pipelining of batch N+1 verify with batch N write), but that is not the problem the Teku PR fixed. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#4183](https://github.com/Consensys-Incorporated/teku/pull/4183)

</details>


<a id="backfill-029"></a>
<details>
<summary><b>backfill-029</b> Per-batch EL fork-choice update during backfill — <i>n/a · low · disk, memory</i></summary>

**Idea.** During a large backfill flush, send a fork-choice update to the EL after each inserted batch so the EL executes and prunes as it goes, bounding pending-block storage.

**Impact.** Backfill never sends payloads to the EL, so there is no pending-block storage to bound.

**Best measured result.** peak BlockTransaction ~4.6 GB -&gt; ~726 MB (6.4x); peak mdbx.dat ~19 GB -&gt; ~9.2 GB (pr:caplin#21525)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/historical_blocks.rs:84`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_blocks.rs#L84) import_historical_block_batch only writes blinded blocks to the store, no EL call

**Sources.** [caplin#21525](https://github.com/erigontech/erigon/pull/21525)

</details>


<a id="backfill-030"></a>
<details>
<summary><b>backfill-030</b> Persist downloaded-not-imported blocks across restart — <i>not · low · M · startup, sync, bandwidth</i></summary>

**Idea.** Store downloaded but not yet imported historical blocks on disk so a restart resumes backfill instead of downloading them again.

**Gap in Lighthouse.** Downloaded-but-unprocessed batches are kept in memory only; on restart backfill resumes from the persisted anchor and refetches them. Would need persisting raw batches.

**Impact.** At most a few in-flight batches (tens of MB) are refetched after a restart; negligible.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/backfill_sync/mod.rs:162`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/backfill_sync/mod.rs#L162) batches held in an in-memory BTreeMap
- [`beacon_node/beacon_chain/src/historical_blocks.rs:470`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_blocks.rs#L470) anchor oldest_block_parent persisted only after each imported batch

**Sources.** [caplin#18320](https://github.com/erigontech/erigon/pull/18320)

</details>


<a id="backfill-031"></a>
<details>
<summary><b>backfill-031</b> Reuse preallocated buffers when encoding backfilled blocks — <i>n/a · low · memory, cpu</i></summary>

**Idea.** Encode and compress each downloaded block into one pre-sized, reused scratch buffer instead of nested appends and fresh allocations, cutting per-block garbage.

**Impact.** Rust SSZ encoding already allocates once per block; the Go nested-append garbage does not exist here.

**Best measured result.** 100 KB block: 38.2 us, 743.6 KB, 34 allocs -&gt; 5.8 us, 0.9 KB, 11 allocs (pr:caplin#22485)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:560`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L560) blinded_block.as_ssz_bytes() uses a pre-sized Vec, no compression stage in this path

**Sources.** [caplin#18980](https://github.com/erigontech/erigon/pull/18980), [caplin#22485](https://github.com/erigontech/erigon/pull/22485)

</details>


<a id="backfill-032"></a>
<details>
<summary><b>backfill-032</b> Remove unused legacy backfill bookkeeping writes — <i>n/a · low · disk</i></summary>

**Idea.** Delete dead backfill range bookkeeping that wrote to the database on every finalization.

**Impact.** Lighthouse has no legacy backfill range bookkeeping written on finalization.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/historical_blocks.rs:470`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_blocks.rs#L470) only the anchor info is updated per batch

**Sources.** [lodestar#10147](https://github.com/ChainSafe/lodestar/pull/10147), [nimbus#3215](https://github.com/status-im/nimbus-eth2/pull/3215)

</details>


<a id="backfill-033"></a>
<details>
<summary><b>backfill-033</b> Reuse received block roots and bytes in backfill — <i>partial · low · M · cpu, sync</i></summary>

**Idea.** Use the block roots already computed from received objects for parent-chain checks and write the original SSZ bytes to the store in a batch, instead of re-hashing and re-serializing each block.

**Gap in Lighthouse.** Roots are reused, but the block is cloned and re-serialized to SSZ for storage instead of writing the received bytes. Would need to carry the original SSZ bytes with the RangeSyncBlock and blind them without a re-encode (full blocks with payload need re-encoding anyway to strip the payload).

**Impact.** Saves one clone and one SSZ encode per block during backfill; small CPU cost compared with signature verification and DB writes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/historical_blocks.rs:158-160`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_blocks.rs#L158-L160) block_root taken from the available block, not rehashed
- [`beacon_node/beacon_chain/src/historical_blocks.rs:200`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_blocks.rs#L200) block cloned into block_as_kv_store_ops
- [`beacon_node/store/src/hot_cold_store.rs:534-560`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L534-L560) block split to blinded and re-encoded with as_ssz_bytes

**Sources.** [lodestar#3669](https://github.com/ChainSafe/lodestar/pull/3669)

</details>


<a id="backfill-034"></a>
<details>
<summary><b>backfill-034</b> Short pubkey cache lock in backfill signature checks — <i>partial · low · S · latency, cpu</i></summary>

**Idea.** Copy the needed proposer pubkeys out of the shared pubkey cache before backfill signature verification so the lock is held only for setup, not for verification.

**Gap in Lighthouse.** In import_historical_block_batch, block proposer signatures follow the idea, with only setup under the lock. But the Gloas self-built payload envelope signatures are verified one by one with signed_envelope.verify_signature while validator_pubkey_cache is still held. Fix: build envelope signature sets with cloned pubkeys, add them to the ParallelSignatureSets, and verify after drop(pubkey_cache).

**Impact.** After Gloas, a 32-block backfill batch holds the pubkey cache lock for ~32 serial BLS verifies (tens of ms) instead of ~250us. This reintroduces the stall lighthouse#2716 removed, and batching the envelopes also cuts their verify cost.

**Best measured result.** Lock hold under load 800ms to 250us (99.97%); setup 180us, verify 7ms (pr:lighthouse#2716)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/historical_blocks.rs:359`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_blocks.rs#L359) pubkey cache read lock taken
- [`beacon_node/beacon_chain/src/historical_blocks.rs:367`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_blocks.rs#L367) Gloas self-build envelope loop runs while the lock is held
- [`beacon_node/beacon_chain/src/historical_blocks.rs:375`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_blocks.rs#L375) signed_envelope.verify_signature() - a full BLS verify per envelope under the lock
- [`beacon_node/beacon_chain/src/historical_blocks.rs:404`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_blocks.rs#L404) block proposal pubkeys cloned into signature sets
- [`beacon_node/beacon_chain/src/historical_blocks.rs:411`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_blocks.rs#L411) drop(pubkey_cache) before the batched block signature verify at :415

**Skeptic check.** The pre-Gloas block path is as the earlier evidence says. The earlier check missed the newer envelope-verification loop in the same locked section, which verifies serially under the lock.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lighthouse#2716](https://github.com/sigp/lighthouse/pull/2716)

</details>


<a id="backfill-035"></a>
<details>
<summary><b>backfill-035</b> Skip history download stage when backfill disabled — <i>not · low · S · bandwidth, sync</i></summary>

**Idea.** Do not run the historical block download stage at all when backfill is disabled by configuration.

**Gap in Lighthouse.** Add a config flag checked in BackFillSync::new / SyncManager so the state is Completed and no batches are requested. Today backfill always runs after checkpoint sync.

**Impact.** Nodes that do not want historic blocks would skip the download, verification and DB writes of the whole ~weak subjectivity window; rare setup.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/backfill_sync/mod.rs:167-180`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/backfill_sync/mod.rs#L167-L180) backfill state only Completed when anchor complete, else Paused/started
- [`beacon_node/src/cli.rs:429-523`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L429-L523) only genesis-backfill and rate-limit flags exist, no disable flag

**Sources.** [caplin#9794](https://github.com/erigontech/erigon/pull/9794), [caplin#9820](https://github.com/erigontech/erigon/pull/9820)

</details>


<a id="backfill-036"></a>
<details>
<summary><b>backfill-036</b> Skip genesis block signature check in backfill — <i>implemented · low · S · cpu</i></summary>

**Idea.** Do not verify a proposer signature for the genesis block during backfill, since it has none.

**Impact.** Genesis block is excluded from the backfill signature set.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/historical_blocks.rs:396`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_blocks.rs#L396) filter(\|&amp;(_block, block_root)\| block_root != self.genesis_block_root)

**Skeptic check.** Verified the filter on the signature set skips the genesis block root. This is the Lighthouse PR itself; earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#3846](https://github.com/sigp/lighthouse/pull/3846)

</details>


<a id="backfill-037"></a>
<details>
<summary><b>backfill-037</b> Checkpoint sync from finalized state only — <i>partial · low · M · startup, sync, bandwidth</i></summary>

**Idea.** Allow checkpoint sync from a finalized state alone and fetch the checkpoint block over p2p, so providers can answer from a cached finalized state instead of a slow by-slot lookup.

**Gap in Lighthouse.** Lighthouse downloads the state only and derives the block slot from the state, but the block is still fetched by slot from the HTTP provider (not over p2p by root); the by-slot lookup cost on provider side remains. Would need block fetch by root from header root or via p2p BlocksByRoot.

**Impact.** Only speeds up one-time startup against slow providers; no steady-state effect.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/client/src/builder.rs:418-445`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L418-L445) downloads finalized state, then fetches the block by slot via get_beacon_blocks_ssz(BlockId::Slot(finalized_block_slot))

**Sources.** [nimbus#4251](https://github.com/status-im/nimbus-eth2/pull/4251)

</details>


<a id="backfill-038"></a>
<details>
<summary><b>backfill-038</b> Lock-free progress counters in backward block downloader — <i>n/a · low · cpu</i></summary>

**Idea.** Replace mutex-guarded progress and finished fields of the backfill downloader with atomics, so status readers and the download loop do not contend on a lock.

**Impact.** BackFillSync is owned by the single sync manager task and has no Mutex, so there is no lock contention to remove.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/backfill_sync/mod.rs:120-127`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/backfill_sync/mod.rs#L120-L127) BackFillSync owns plain fields, mutated via &amp;mut self
- [`beacon_node/network/src/sync/backfill_sync/mod.rs:583`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/backfill_sync/mod.rs#L583) processing_target updated without locks

**Sources.** [caplin#9715](https://github.com/erigontech/erigon/pull/9715)

</details>


<a id="backfill-039"></a>
<details>
<summary><b>backfill-039</b> Use canonical block root for backfill blob and column lookups — <i>n/a · low · sync, bandwidth, disk</i></summary>

**Idea.** When blocks are stored payload-stripped, key blob and column count lookups and by-root requests on the canonical block root from the index, not a hash of the stored block. This stops backfill re-requesting held data or waiting on timeouts.

**Impact.** n/a: Lighthouse stores blinded blocks whose tree hash root equals the full block root, and blob/column lookups use that block root, so no wrong-root lookup arises.

**Best measured result.** pr:caplin#23895: backward pass 1.2 slots/s never finishing to 39 s

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/historical_blocks.rs:96`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_blocks.rs#L96) backfill keyed by block_root from the block itself
- [`beacon_node/store/src/metadata.rs:99`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/metadata.rs#L99) oldest_block_slot

**Sources.** [caplin#24053](https://github.com/erigontech/erigon/pull/24053), [caplin#23895](https://github.com/erigontech/erigon/pull/23895)

</details>


<a id="backfill-040"></a>
<details>
<summary><b>backfill-040</b> Record backfill progress at anchor block slot — <i>n/a · low · sync, disk</i></summary>

**Idea.** Store the completed backfill range using the anchor block's slot, not the anchor state's slot, so pruning of old backfill entries after forward sync cannot delete it and force backfill to restart.

**Impact.** n/a: backfill progress is a single AnchorInfo (oldest_block_slot, parent root), not a list of ranges that forward sync prunes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/metadata.rs:90-99`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/metadata.rs#L90-L99) anchor_slot and oldest_block_slot are separate fields
- [`beacon_node/beacon_chain/src/historical_blocks.rs:88-117`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_blocks.rs#L88-L117) progress tracked via oldest_block_slot/oldest_block_parent

**Sources.** [lodestar#3774](https://github.com/ChainSafe/lodestar/pull/3774)

</details>


<a id="backfill-041"></a>
<details>
<summary><b>backfill-041</b> Persist custody group count immediately on change — <i>implemented · low · S · bandwidth, disk, sync</i></summary>

**Idea.** Write the custody group count to disk as soon as it changes, so an unclean shutdown does not lose it and trigger repeated custody backfill of data already held.

**Impact.** Avoids repeated custody backfill after an unclean shutdown; rare.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/validator/mod.rs:1104-1130`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L1104-L1130)
- [`beacon_node/beacon_chain/src/builder.rs:1147`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L1147)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:735`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L735)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:8465`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L8465)

**Skeptic check.** register_validators is the only runtime CGC-change site and persists right after a change; builder persists CLI-flag changes. Per-epoch backfill progress (update_and_backfill_custody_count_at_epoch in historical_data_columns.rs:214) is still only persisted on Drop, but that is outside the idea's scope, as PR #8921 itself states.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#8921](https://github.com/sigp/lighthouse/pull/8921)

</details>


