# backfill

14 ideas: 2 not, 1 partial, 11 implemented; 3 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

The area has 34 numbered ideas; the 20 ids missing here have not been checked against Lighthouse yet.

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [backfill-001](#backfill-001) | Backfill only to the block-request retention window | implemented | high |  | disk, bandwidth, sync, cpu |
| [backfill-002](#backfill-002) **★** | Use fork-specific shorter block-request window for backfill | not | medium | S | bandwidth, disk, sync |
| [backfill-003](#backfill-003) | Custody backfill fetches only custodied columns | implemented | medium |  | bandwidth, cpu |
| [backfill-004](#backfill-004) | Ask each peer only for its column subset | implemented | medium |  | bandwidth |
| [backfill-005](#backfill-005) **★** | Per-peer fault attribution and partial retry in backfill | partial | medium | M | sync, bandwidth |
| [backfill-006](#backfill-006) | Run backfill only when forward sync is at head | implemented | low | S | sync, bandwidth, cpu |
| [backfill-007](#backfill-007) | Batch KZG verification of backfilled columns | implemented | medium |  | cpu, disk |
| [backfill-009](#backfill-009) | Dedicated low-priority thread pool for backfill | implemented | medium |  | cpu, latency, sync |
| [backfill-011](#backfill-011) | Rate-limit backfill batch processing per slot | implemented | low | S | cpu, sync, disk |
| [backfill-014](#backfill-014) | Cap number of buffered backfill batches | implemented | low | S | cpu, bandwidth |
| [backfill-018](#backfill-018) **★** | Backfill history from era files or snapshots | not | medium | L | sync, bandwidth, disk, startup |
| [backfill-024](#backfill-024) | Parallel pipelined block range requests in backfill | implemented | low | S | sync, latency, cpu |
| [backfill-026](#backfill-026) | Cursor-based custody column backfiller | implemented | low | S | bandwidth, sync, disk |
| [backfill-034](#backfill-034) | Short pubkey cache lock in backfill signature checks | implemented | low | S | latency, cpu |

★ actionable. Click an id for the full record.

## Ideas

<a id="backfill-001"></a>
<details>
<summary><b>backfill-001</b> Backfill only to the block-request retention window — <i>implemented · high · disk, bandwidth, sync, cpu</i></summary>

**Idea.** After checkpoint sync, backfill blocks (and blobs) only back to the weak subjectivity / MIN_EPOCHS_FOR_BLOCK_REQUESTS boundary instead of genesis, with full history opt-in. Older blocks are not servable on the network, so this cuts download, verification and disk.

**Impact.** Already in place.

**Best measured result.** stops syncing back to genesis; only about the last 5 months of blocks are downloaded (pr:lighthouse#4082)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/builder.rs:942`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L942) genesis_backfill_slot defaults to a WSP-derived epoch unless --genesis-backfill
- [`beacon_node/network/src/sync/backfill_sync/mod.rs:172`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/backfill_sync/mod.rs#L172) backfill complete check vs genesis_backfill_slot
- [`beacon_node/src/cli.rs:429`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L429) genesis-backfill opt-in flag

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

**Sources.** [lighthouse#10270](https://github.com/sigp/lighthouse/pull/10270)

</details>


<a id="backfill-003"></a>
<details>
<summary><b>backfill-003</b> Custody backfill fetches only custodied columns — <i>implemented · medium · bandwidth, cpu</i></summary>

**Idea.** In data-column custody backfill, request only the columns the node custodies, not the full sampling set, because extra columns are verified and then discarded.

**Impact.** Already in place.

**Best measured result.** halves download for 4 of 8 columns (pr:lighthouse#8916)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/custody_backfill_sync/mod.rs:454`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/custody_backfill_sync/mod.rs#L454) batch built with ByRangeRequestType::Columns(get_missing_columns_for_epoch)
- [`beacon_node/network/src/sync/custody_backfill_sync/mod.rs:395`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/custody_backfill_sync/mod.rs#L395) epochs with no missing columns are skipped

**Sources.** [lighthouse#8916](https://github.com/sigp/lighthouse/pull/8916)

</details>


<a id="backfill-004"></a>
<details>
<summary><b>backfill-004</b> Ask each peer only for its column subset — <i>implemented · medium · bandwidth</i></summary>

**Idea.** When requesting data columns for custody backfill, choose peers by the requested column set and send each peer a request for only the columns it serves, instead of the full request to every peer, to avoid N-times download amplification.

**Impact.** Already in place.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context.rs:1607`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L1607) custody_backfill_data_columns_batch_request builds column set from request.columns
- [`beacon_node/network/src/sync/network_context.rs:578`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L578) select_columns_by_range_peers_to_request groups columns per peer
- [`beacon_node/network/src/sync/network_context.rs:1635`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L1635) each peer gets DataColumnsByRangeRequest with only its columns

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

**Sources.** [lighthouse#7762](https://github.com/sigp/lighthouse/pull/7762)

</details>


<a id="backfill-006"></a>
<details>
<summary><b>backfill-006</b> Run backfill only when forward sync is at head — <i>implemented · low · S · sync, bandwidth, cpu</i></summary>

**Idea.** Do not start backfill workers until the node has synced to head, and pause them whenever it falls back into range sync, so backfill does not take peers, rate-limit budget, CPU and bandwidth from forward sync and duties.

**Impact.** Backfill no longer competes with forward sync for peers and CPU; already in place.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/manager.rs:680`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L680) backfill start() only when sync_state is Synced
- [`beacon_node/network/src/sync/manager.rs:743`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L743) backfill_sync.pause() and custody pause on SyncingFinalized/SyncingHead

**Sources.** [prysm#13623](https://github.com/OffchainLabs/prysm/pull/13623), [nimbus#3263](https://github.com/status-im/nimbus-eth2/pull/3263), [nimbus#7191](https://github.com/status-im/nimbus-eth2/pull/7191), [prysm#15702](https://github.com/OffchainLabs/prysm/pull/15702), [teku#3199](https://github.com/Consensys-Incorporated/teku/pull/3199)

</details>


<a id="backfill-007"></a>
<details>
<summary><b>backfill-007</b> Batch KZG verification of backfilled columns — <i>implemented · medium · cpu, disk</i></summary>

**Idea.** Verify the KZG proofs of backfilled data columns as one batch per segment instead of one at a time, which lowers CPU and storage pressure.

**Impact.** Already in place.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/historical_data_columns.rs:190`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_data_columns.rs#L190) verify_kzg_for_data_column_list over the whole epoch list
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1122`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1122) validate_full_data_columns batched with KZG_VERIFICATION_DATA_COLUMN_BATCH_TIMES
- [`beacon_node/beacon_chain/src/historical_data_columns.rs:182`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_data_columns.rs#L182) Gloas path validate_data_columns_with_commitments batched
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:676`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L676) block backfill uses batch_verify_kzg_for_range_sync_blocks

**Sources.** [silver#209](https://github.com/gattaca-com/silver/pull/209)

</details>


<a id="backfill-009"></a>
<details>
<summary><b>backfill-009</b> Dedicated low-priority thread pool for backfill — <i>implemented · medium · cpu, latency, sync</i></summary>

**Idea.** Run backfill segment validation (signatures, KZG) on a separate low-priority executor or thread pool so its compute cannot contend with latency-critical block and attestation import.

**Impact.** Already in place.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:1727`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1727) ChainSegmentBackfill spawned on RayonPoolType::LowPriority
- [`beacon_node/network/src/network_beacon_processor/mod.rs:635`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L635) send_historic_data_columns uses Work::ChainSegmentBackfill
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:92`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L92) backfill batches rate-limited to slot offsets
- [`common/task_executor/src/rayon_pool_provider.rs:8`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/task_executor/src/rayon_pool_provider.rs#L8) separate low/high priority pools

**Sources.** [grandine@a1c626531](https://github.com/grandinetech/grandine/commit/a1c626531e49), [grandine#542](https://github.com/grandinetech/grandine/pull/542), [lighthouse#7924](https://github.com/sigp/lighthouse/pull/7924)

</details>


<a id="backfill-011"></a>
<details>
<summary><b>backfill-011</b> Rate-limit backfill batch processing per slot — <i>implemented · low · S · cpu, sync, disk</i></summary>

**Idea.** Queue backfill batches and release only a fixed number (e.g. one to three) at set points in each slot, so backfill throughput is throttled and does not compete with block and attestation processing.

**Impact.** Backfill CPU is already throttled to at most three batches per slot.

**Best measured result.** CPU usage during backfill reduced by ~5% - 20% on Goerli (pr:lighthouse#3936)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:813`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L813) backfill batches routed to reprocess queue when enable_backfill_rate_limiting (default true, :135)
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:96`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L96) BACKFILL_SCHEDULE_IN_SLOT releases a batch at 50/60/80% of slot

**Sources.** [lighthouse#3936](https://github.com/sigp/lighthouse/pull/3936), [silver#199](https://github.com/gattaca-com/silver/pull/199)

</details>


<a id="backfill-014"></a>
<details>
<summary><b>backfill-014</b> Cap number of buffered backfill batches — <i>implemented · low · S · cpu, bandwidth</i></summary>

**Idea.** Limit the number of backfill batches buffered in flight to the forward-sync level (e.g. 5 instead of 20), so fewer heavy multi-peer column requests are created and retried.

**Impact.** Already capped at 5 buffered batches, so fewer retried multi-peer column requests.

**Best measured result.** 20 -&gt; 5 batches (pr:lighthouse#7958)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/backfill_sync/mod.rs:49`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/backfill_sync/mod.rs#L49) BACKFILL_BATCH_BUFFER_SIZE = 5
- [`beacon_node/network/src/sync/backfill_sync/mod.rs:1012`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/backfill_sync/mod.rs#L1012) include_next_batch enforces the cap
- [`beacon_node/network/src/sync/custody_backfill_sync/mod.rs:32`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/custody_backfill_sync/mod.rs#L32) same cap 5

**Sources.** [lighthouse#7958](https://github.com/sigp/lighthouse/pull/7958)

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

**Sources.** [nimbus#3394](https://github.com/status-im/nimbus-eth2/pull/3394), [nimbus#4283](https://github.com/status-im/nimbus-eth2/pull/4283), [caplin#8665](https://github.com/erigontech/erigon/pull/8665)

</details>


<a id="backfill-024"></a>
<details>
<summary><b>backfill-024</b> Parallel pipelined block range requests in backfill — <i>implemented · low · S · sync, latency, cpu</i></summary>

**Idea.** Keep several backfill block-range requests in flight at once, to different peers, and sort/dedupe results before chain checks, so throughput is not limited by one request or one peer.

**Gap in Lighthouse.** Lighthouse has no explicit sort/dedupe of results before chain checks; batches are per-epoch ranges so dedupe is not needed.

**Impact.** Backfill is already pipelined across peers; a larger buffer could raise throughput but conflicts with the lighthouse#7958 cap.

**Best measured result.** 27.4 -&gt; 91.6 blk/s median on mainnet (pr:caplin#25417)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/backfill_sync/mod.rs:968`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/backfill_sync/mod.rs#L968) request_batches loops include_next_batch, keeping up to 5 batches in flight
- [`beacon_node/network/src/sync/backfill_sync/mod.rs:49`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/backfill_sync/mod.rs#L49) buffer size 5

**Sources.** [caplin#8554](https://github.com/erigontech/erigon/pull/8554), [caplin#15255](https://github.com/erigontech/erigon/pull/15255), [caplin#25417](https://github.com/erigontech/erigon/pull/25417), [nimbus#3371](https://github.com/status-im/nimbus-eth2/pull/3371)

</details>


<a id="backfill-026"></a>
<details>
<summary><b>backfill-026</b> Cursor-based custody column backfiller — <i>implemented · low · S · bandwidth, sync, disk</i></summary>

**Idea.** Run a dedicated, default-on custody column backfiller that works in batches from a persisted earliest-available-column-slot cursor, starts only when in sync, restarts when custody count grows, and advertises the slot to peers.

**Impact.** Custody column backfill exists in-tree; nothing further to gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/custody_backfill_sync/mod.rs:164`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/custody_backfill_sync/mod.rs#L164) should_start_custody_backfill_sync uses earliest custodied data column epoch cursor
- [`beacon_node/network/src/sync/custody_backfill_sync/mod.rs:200`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/custody_backfill_sync/mod.rs#L200) restart_sync / :224 restart_if_required when custody count changes
- [`beacon_node/network/src/sync/manager.rs:702`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L702) starts only after block backfill complete and Synced
- [`beacon_node/network/src/status.rs:40`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/status.rs#L40) advertises earliest_available_slot

**Sources.** [teku#10159](https://github.com/Consensys-Incorporated/teku/pull/10159), [teku#10226](https://github.com/Consensys-Incorporated/teku/pull/10226), [teku#10312](https://github.com/Consensys-Incorporated/teku/pull/10312)

</details>


<a id="backfill-034"></a>
<details>
<summary><b>backfill-034</b> Short pubkey cache lock in backfill signature checks — <i>implemented · low · S · latency, cpu</i></summary>

**Idea.** Copy the needed proposer pubkeys out of the shared pubkey cache before backfill signature verification so the lock is held only for setup, not for verification.

**Impact.** Lock is already held only for setup; verification runs unlocked.

**Best measured result.** Lock hold under load 800ms to 250us (99.97%); setup 180us, verify 7ms (pr:lighthouse#2716)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/historical_blocks.rs:357`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_blocks.rs#L357) try_read_for pubkey cache lock
- [`beacon_node/beacon_chain/src/historical_blocks.rs:404`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_blocks.rs#L404) pubkeys cloned into the signature sets
- [`beacon_node/beacon_chain/src/historical_blocks.rs:411`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_blocks.rs#L411) drop(pubkey_cache) before signature_set.verify()

**Sources.** [lighthouse#2716](https://github.com/sigp/lighthouse/pull/2716)

</details>


