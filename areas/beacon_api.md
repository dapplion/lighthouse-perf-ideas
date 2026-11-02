# beacon_api

129 ideas: 20 not, 25 partial, 78 implemented, 6 n/a; 29 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

Ids missing from the sequence are ideas that have not been checked against Lighthouse yet.

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [beacon_api-001](#beacon_api-001) | Serve duty queries from epoch caches, not loaded states | implemented | medium |  | cpu, memory, latency |
| [beacon_api-002](#beacon_api-002) | Read sync committee duties from head state | implemented | medium |  | cpu, latency |
| [beacon_api-004](#beacon_api-004) | Serve proposer duties from a decision-root-keyed proposer cache | partial | low | S | cpu, latency |
| [beacon_api-005](#beacon_api-005) **★** | Compute duties for all validators in one committee pass | partial | medium | S | cpu, latency |
| [beacon_api-006](#beacon_api-006) | Return assignments only for requested validators | partial | low | S | memory, cpu |
| [beacon_api-008](#beacon_api-008) | Run heavy API handlers on blocking thread pool | implemented | low |  | cpu, latency |
| [beacon_api-011](#beacon_api-011) | POST variant of validators and balances queries | implemented | low |  | cpu, latency |
| [beacon_api-012](#beacon_api-012) | SSZ responses for validators and balances endpoints | partial | low | S | cpu, bandwidth, latency |
| [beacon_api-015](#beacon_api-015) | SSZ for block production endpoints | implemented | low |  | cpu, bandwidth, latency |
| [beacon_api-018](#beacon_api-018) | Accept SSZ bodies when publishing blocks | implemented | low |  | cpu, bandwidth, latency |
| [beacon_api-021](#beacon_api-021) | Request builder API responses as SSZ | implemented | medium |  | cpu, bandwidth, latency |
| [beacon_api-023](#beacon_api-023) | Generic Accept negotiation to serve SSZ | not | low | M | cpu, bandwidth |
| [beacon_api-024](#beacon_api-024) **★** | Process submitted pool messages in background after response | not | medium | M | latency |
| [beacon_api-027](#beacon_api-027) | Bounded per-subscriber SSE queues, drop slow clients | partial | low | S | latency, memory |
| [beacon_api-033](#beacon_api-033) | Emit head/block SSE event early in import | implemented | medium |  | latency |
| [beacon_api-035](#beacon_api-035) | Answer attestation_data from fork choice | implemented | medium | S | latency |
| [beacon_api-036](#beacon_api-036) | Cache attestation data per slot, no per-request state copy | implemented | medium | S | memory, cpu |
| [beacon_api-038](#beacon_api-038) | Read head state fields without cloning the state | implemented | low | S | memory, cpu |
| [beacon_api-048](#beacon_api-048) | Skip state root recompute after process_slots | implemented | medium |  | cpu |
| [beacon_api-051](#beacon_api-051) | Optimistic status from fork choice, not state hash | implemented | low | S | cpu, memory |
| [beacon_api-052](#beacon_api-052) | State root endpoint from stored block state_root | implemented | medium |  | cpu, disk, latency |
| [beacon_api-057](#beacon_api-057) | Bound state regeneration for far-out API requests | implemented | medium | S | cpu, latency |
| [beacon_api-058](#beacon_api-058) | Advance state only to epoch start for committees | implemented | medium |  | cpu, latency |
| [beacon_api-060](#beacon_api-060) | Box large async futures on block publish | implemented | low | S | memory, cpu |
| [beacon_api-065](#beacon_api-065) | Resolve state_id directly via selector | partial | low | S | cpu, disk, latency |
| [beacon_api-069](#beacon_api-069) | Separate small committee cache for HTTP committees route | implemented | low | S | cpu, memory |
| [beacon_api-073](#beacon_api-073) | Doppelganger check early return skips historical states | n/a | medium |  | cpu, startup |
| [beacon_api-075](#beacon_api-075) | Validator activation status check once per epoch | not | low | M | cpu |
| [beacon_api-078](#beacon_api-078) | Fetch blobs from EL on gossip block arrival | implemented | high |  | latency, bandwidth, sync |
| [beacon_api-079](#beacon_api-079) **★** | Query EL first, request only remaining blobs from peers | partial | medium | M | latency, bandwidth |
| [beacon_api-080](#beacon_api-080) **★** | Trigger getBlobs on first gossip column sidecar | partial | medium | S | latency, bandwidth |
| [beacon_api-081](#beacon_api-081) | Call getBlobs before block verification completes | implemented | high |  | latency, bandwidth |
| [beacon_api-082](#beacon_api-082) | Fetch blobs from EL during block lookup sync | implemented | medium |  | latency, bandwidth |
| [beacon_api-083](#beacon_api-083) | Fetch EL blobs for blocks published via API | implemented | medium |  | latency, bandwidth |
| [beacon_api-084](#beacon_api-084) **★** | Use existence-only EL blob query | not | medium | M | latency, bandwidth |
| [beacon_api-088](#beacon_api-088) **★** | Build only custodied columns from EL blobs | partial | medium | S | cpu, memory |
| [beacon_api-089](#beacon_api-089) | Publish recovered columns off the availability path | implemented | medium |  | latency, bandwidth |
| [beacon_api-090](#beacon_api-090) | Publish only needed recovered columns | implemented | medium |  | cpu, bandwidth |
| [beacon_api-091](#beacon_api-091) **★** | Mark data available at 50% columns | not | medium | M | latency, bandwidth, sync |
| [beacon_api-092](#beacon_api-092) | Reconstruct remaining columns from half | implemented | medium |  | cpu, latency, bandwidth, sync |
| [beacon_api-093](#beacon_api-093) | Delay column reconstruction to wait for gossip | implemented | low | S | cpu, latency, sync |
| [beacon_api-096](#beacon_api-096) | Run column reconstruction once per block | implemented | medium |  | cpu, memory, disk |
| [beacon_api-097](#beacon_api-097) | Dedicated thread pool for column reconstruction | implemented | medium |  | cpu, latency |
| [beacon_api-098](#beacon_api-098) | Run KZG reconstruction off async and fork-choice threads | implemented | medium |  | cpu, latency |
| [beacon_api-099](#beacon_api-099) | Bound parallelism of per-blob cell recovery | partial | low | S | cpu, memory |
| [beacon_api-100](#beacon_api-100) | Semi-supernode: custody half the columns | implemented | medium |  | cpu, disk, bandwidth |
| [beacon_api-101](#beacon_api-101) | Custody first half of columns to skip reconstruction | not | low | L | cpu, bandwidth |
| [beacon_api-104](#beacon_api-104) | Share blobs and cells by Arc, not copy | implemented | low |  | cpu, memory |
| [beacon_api-108](#beacon_api-108) **★** | Cache columns with unknown parent block | not | medium | M | latency, sync |
| [beacon_api-109](#beacon_api-109) | Index sidecar quarantine by root and slot | implemented | low |  | cpu |
| [beacon_api-110](#beacon_api-110) | Cache custody column set per node | implemented | low |  | cpu |
| [beacon_api-111](#beacon_api-111) | Batch KZG verify sidecars from RPC and sync | implemented | medium |  | cpu, latency, sync |
| [beacon_api-112](#beacon_api-112) **★** | Batch gossip column verification per block | partial | medium | M | cpu, latency |
| [beacon_api-113](#beacon_api-113) | Combine by-root sidecar requests per peer | implemented | low |  | bandwidth, sync |
| [beacon_api-115](#beacon_api-115) | Request columns only from custody peers | implemented | medium |  | bandwidth, sync |
| [beacon_api-116](#beacon_api-116) **★** | Hedge slow column requests to alternate peers | not | medium | M | latency, sync |
| [beacon_api-119](#beacon_api-119) | Validate blob sidecars without state advancement | implemented | medium |  | cpu, memory, latency |
| [beacon_api-121](#beacon_api-121) | Prune blob and column data past DA window | implemented | medium |  | disk |
| [beacon_api-122](#beacon_api-122) | Derive column retention window from chain config | implemented | medium |  | disk |
| [beacon_api-124](#beacon_api-124) | Cheap filesystem traversal for blob pruning | n/a | medium |  | cpu, disk |
| [beacon_api-125](#beacon_api-125) **★** | Incremental capped low-priority blob pruning | partial | medium | S | cpu, disk, latency |
| [beacon_api-131](#beacon_api-131) | Cache gossip-validated sidecars for import | implemented | medium |  | cpu, latency |
| [beacon_api-132](#beacon_api-132) | Drop sidecars for already-imported blocks | partial | low | S | cpu, memory, bandwidth |
| [beacon_api-133](#beacon_api-133) | Bound or fail fast on DA wait | n/a | medium |  | latency, sync |
| [beacon_api-135](#beacon_api-135) | Run DA check concurrently with execution verification | implemented | medium | S | latency |
| [beacon_api-138](#beacon_api-138) | Track received columns to skip duplicate work | implemented | medium |  | cpu, disk, bandwidth |
| [beacon_api-140](#beacon_api-140) **★** | Delay RPC fetch of missing sidecars | partial | medium | M | latency, bandwidth, sync |
| [beacon_api-141](#beacon_api-141) **★** | Request missing blobs immediately on block seen | partial | medium | S | latency |
| [beacon_api-142](#beacon_api-142) | Pull late block when blobs arrive first | implemented | medium |  | latency |
| [beacon_api-144](#beacon_api-144) **★** | Fetch missing columns within the slot | partial | medium | M | latency |
| [beacon_api-146](#beacon_api-146) **★** | Disk-backed blob quarantine | not | medium | M | memory, disk |
| [beacon_api-149](#beacon_api-149) | Drop sidecars with out-of-range index | implemented | medium |  | cpu, memory |
| [beacon_api-152](#beacon_api-152) | Keep DA entries until import completes | implemented | medium |  | cpu, memory, disk, latency, bandwidth, sync |
| [beacon_api-155](#beacon_api-155) | Import only when blob count equals commitments | implemented | low |  | latency |
| [beacon_api-156](#beacon_api-156) | Drop gossip columns outside sampling set | implemented | high |  | cpu, disk, bandwidth |
| [beacon_api-157](#beacon_api-157) | Correct proposer cache key in blob verification | implemented | medium |  | cpu, latency |
| [beacon_api-159](#beacon_api-159) | High priority retry for delayed columns | implemented | medium |  | latency |
| [beacon_api-162](#beacon_api-162) | Skip gossip proof checks for EL-supplied blobs | implemented | medium |  | cpu, latency |
| [beacon_api-163](#beacon_api-163) **★** | Cache column inclusion proof results | partial | medium | S | cpu |
| [beacon_api-164](#beacon_api-164) | Late DA check with per-block sampling tracker | implemented | medium | S | disk, latency, bandwidth |
| [beacon_api-165](#beacon_api-165) **★** | Retry getBlobs until block columns are built | partial | medium | S | latency, bandwidth |
| [beacon_api-L003](#beacon_api-L003) | pre-sized direct JSON encoding | partial | low | S | cpu, latency, memory |
| [beacon_api-L004](#beacon_api-L004) **★** | publish head before state copy | partial | medium | S | latency |
| [beacon_api-L010](#beacon_api-L010) | historic committee cache from randao | implemented | medium | S | latency, cpu |
| [beacon_api-L011](#beacon_api-L011) | pubkey cache lookup | implemented | low |  | cpu, latency |
| [beacon_api-L016](#beacon_api-L016) | hashset id filter | implemented | low |  | cpu, latency |
| [beacon_api-L017](#beacon_api-L017) | persist light client bootstrap | implemented | medium | S | cpu, disk |
| [beacon_api-L018](#beacon_api-L018) | single lock acquisition | implemented | low |  | latency |
| [beacon_api-L020](#beacon_api-L020) | server-side supply computation | not | low | S | bandwidth, cpu |
| [beacon_api-L021](#beacon_api-L021) | not-while-syncing guard on duties | implemented | medium | S | cpu, sync |
| [beacon_api-L023](#beacon_api-L023) **★** | skip duties when stalled | not | medium | S | cpu, latency |
| [beacon_api-L024](#beacon_api-L024) **★** | index lookup instead of full scan | not | medium | S | cpu, latency |
| [beacon_api-L025](#beacon_api-L025) | light client updates without state cache | implemented | medium | S | memory |
| [beacon_api-L038](#beacon_api-L038) | guard old-slot reconstruction | implemented | medium | S | cpu, latency |
| [beacon_api-L039](#beacon_api-L039) | guard old-slot reconstruction | implemented | medium | S | cpu, latency |
| [beacon_api-L040](#beacon_api-L040) **★** | refuse regen API while syncing | not | medium | S | cpu, latency, sync |
| [beacon_api-L042](#beacon_api-L042) | pubkey index map | implemented | low |  | cpu, latency |
| [beacon_api-L043](#beacon_api-L043) | share historical state reconstruction | partial | low | M | cpu, latency |
| [beacon_api-L045](#beacon_api-L045) | reuse state across history traversal | implemented | medium |  | cpu, latency |
| [beacon_api-L046](#beacon_api-L046) | stream JSON without temp strings | partial | low | M | cpu, memory, latency |
| [beacon_api-L050](#beacon_api-L050) | pubkey to index map | partial | low | S | cpu, latency |
| [beacon_api-L051](#beacon_api-L051) | per-slot committee cache for duties | implemented | low | S | cpu, latency |
| [beacon_api-L054](#beacon_api-L054) | single pass committee map | implemented | low | S | cpu, latency |
| [beacon_api-L055](#beacon_api-L055) | skip needless slot advance | implemented | medium |  | cpu, latency |
| [beacon_api-L056](#beacon_api-L056) | paginate before compute; custom marshal | n/a | low | S | cpu, memory, latency |
| [beacon_api-L060](#beacon_api-L060) | group by block root | n/a | medium |  | cpu, latency |
| [beacon_api-L062](#beacon_api-L062) | use target-root state | n/a | medium |  | cpu, latency |
| [beacon_api-L064](#beacon_api-L064) | state regen by target root | implemented | low | S | latency, cpu |
| [beacon_api-L069](#beacon_api-L069) | head getters without state copy | implemented | low | S | cpu, memory |
| [beacon_api-L071](#beacon_api-L071) | skip replay for future slot | implemented | medium |  | cpu, latency |
| [beacon_api-L073](#beacon_api-L073) | skip unchanged DB write | implemented | low | S | disk |
| [beacon_api-L076](#beacon_api-L076) | head state with next-slot cache | implemented | medium |  | cpu, latency |
| [beacon_api-L078](#beacon_api-L078) **★** | use next slot cache in rewards | partial | medium | S | latency |
| [beacon_api-L079](#beacon_api-L079) | read-only validator views | implemented | low | S | cpu, latency |
| [beacon_api-L080](#beacon_api-L080) | precompute and store updates | implemented | medium |  | cpu, latency |
| [beacon_api-L082](#beacon_api-L082) **★** | gzip HTTP responses | partial | medium | S | bandwidth |
| [beacon_api-L086](#beacon_api-L086) | reverse index for duties lookup | implemented | medium | S | cpu, latency |
| [beacon_api-L089](#beacon_api-L089) | per-request committee assignment, early exit | implemented | medium |  | cpu, memory |
| [beacon_api-L090](#beacon_api-L090) **★** | skip KZG proof computation on blob reconstruct | not | medium | M | cpu, memory, latency |
| [beacon_api-L091](#beacon_api-L091) **★** | lower gzip level | not | medium | S | cpu |
| [beacon_api-L092](#beacon_api-L092) | reject unavailable historical state early | implemented | medium |  | cpu, latency |
| [beacon_api-L094](#beacon_api-L094) | lazy filtered validator iteration | implemented | medium | S | memory, cpu, latency |
| [beacon_api-L103](#beacon_api-L103) | shared serialized event bytes | not | low | S | memory, cpu |
| [beacon_api-L104](#beacon_api-L104) **★** | stream JSON response | not | medium | M | memory |
| [beacon_api-L105](#beacon_api-L105) **★** | stream SSZ response | not | medium | M | memory |
| [beacon_api-L106](#beacon_api-L106) | reject future-slot state lookup | implemented | medium |  | cpu, latency |
| [beacon_api-L109](#beacon_api-L109) **★** | gzip REST responses | not | medium | S | bandwidth |
| [beacon_api-L110](#beacon_api-L110) | head state for duties | implemented | medium |  | cpu, latency |
| [beacon_api-L115](#beacon_api-L115) **★** | on-demand sidecar fetch for blobs | not | medium | L | bandwidth, disk |

★ actionable. Click an id for the full record.

## Ideas

<a id="beacon_api-001"></a>
<details>
<summary><b>beacon_api-001</b> Serve duty queries from epoch caches, not loaded states — <i>implemented · medium · cpu, memory, latency</i></summary>

**Idea.** Answer attester/committee duty and related validator queries for the previous, current and next epoch from the head state's committee/epoch caches (or preloaded head data) instead of loading a state from the DB or advancing a full state per request. This turns each duty request into cache lookups and keeps request floods from triggering state loads.

**Impact.** Already done; duty requests are cache lookups on the hot path.

**Best measured result.** memory required 4 GB -&gt; 10 GB, API consistently performant (pr:caplin#9457)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/attester_duties.rs:61`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L61) cached_attestation_duties
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1735`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1735) validator_attestation_duties uses with_committee_cache (shuffling cache), no state load
- [`beacon_node/http_api/src/attester_duties.rs:83`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L83) state load only for historic epochs

**Sources.** [caplin#9457](https://github.com/erigontech/erigon/pull/9457), [nimbus@678a7efaa](https://github.com/status-im/nimbus-eth2/commit/678a7efaaa8c), [nimbus#1536](https://github.com/status-im/nimbus-eth2/pull/1536), [lighthouse#636](https://github.com/sigp/lighthouse/pull/636), [prysm#16136](https://github.com/OffchainLabs/prysm/pull/16136)

</details>


<a id="beacon_api-002"></a>
<details>
<summary><b>beacon_api-002</b> Read sync committee duties from head state — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** For sync committee duties within the current or next sync period, read current_sync_committee/next_sync_committee from the head state instead of loading or replaying a state to the period start, because those fields are constant within a period.

**Impact.** Already done; head state current/next sync committee used.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/sync_committees.rs:44`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/sync_committees.rs#L44) sync_committee_duties_from_head tried first
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3032`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3032) sync_committee_duties_from_head uses head state
- [`beacon_node/http_api/src/sync_committees.rs:123`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/sync_committees.rs#L123) state load only as fallback on SyncCommitteeNotKnown

**Sources.** [prysm#16688](https://github.com/OffchainLabs/prysm/pull/16688), [grandine@5b9bf12ab](https://github.com/grandinetech/grandine/commit/5b9bf12ab2f5), [grandine#264](https://github.com/grandinetech/grandine/pull/264)

</details>


<a id="beacon_api-004"></a>
<details>
<summary><b>beacon_api-004</b> Serve proposer duties from a decision-root-keyed proposer cache — <i>partial · low · S · cpu, latency</i></summary>

**Idea.** Serve proposer duties (including next-epoch duties post-Fulu) from a shared proposer cache keyed by the shuffling decision root and primed ahead of time, and reuse cached attester shufflings, so concurrent or retried duty requests do not re-advance the head state. Use compressed pubkey bytes in duty responses so cloning and hashing are cheap.

**Gap in Lighthouse.** Next-epoch proposer duties (request_epoch == current+1) are recomputed from the head state on every request and never cached; make that branch in proposer_duties_internal look up/insert beacon_proposer_cache keyed by the next-epoch decision root (and prime it in state_advance_timer).

**Impact.** Repeated or retried next-epoch proposer duty calls (post-Fulu VCs poll this) stop advancing the head state; minor, a few ms per call.

**Best measured result.** Pyrmont: proposer duties 450ms peaks to &lt;1ms; attester duties &gt;1s to 20-30ms (pr:lighthouse#2243)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/proposer_duties.rs:135`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/proposer_duties.rs#L135) cache lookup keyed by decision root
- [`beacon_node/http_api/src/proposer_duties.rs:198`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/proposer_duties.rs#L198) compute_and_cache primes cache
- [`beacon_node/http_api/src/proposer_duties.rs:314`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/proposer_duties.rs#L314) pubkey bytes via validator_pubkey_bytes_many
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1735`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1735) attester duties via shuffling cache (with_committee_cache)
- [`beacon_node/http_api/src/proposer_duties.rs:73`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/proposer_duties.rs#L73) next-epoch branch calls compute_proposer_duties_from_head, no cache read/insert

**Sources.** [lighthouse#2243](https://github.com/sigp/lighthouse/pull/2243), [lighthouse#10459](https://github.com/sigp/lighthouse/pull/10459)

</details>


<a id="beacon_api-005"></a>
<details>
<summary><b>beacon_api-005</b> Compute duties for all validators in one committee pass — <i>partial · medium · S · cpu, latency</i></summary>

**Idea.** When a duties request names many validators, iterate the target epoch's committees once while looking up members in a validator-index set or map, instead of searching the committees separately for each validator. This turns O(validators x committees) work into a single pass.

**Gap in Lighthouse.** Shuffling/cache lookup is already shared for the batch and the member lookup is O(1), but finding the committee still scans up to epoch_committee_count ranges per validator (O(V x C) integer arithmetic). Replace the loop with direct computation (i*count/len, adjust by one) or a binary search over the monotonic ranges.

**Impact.** Small: saves up to ~2048 cheap range computations per requested validator; only noticeable for VCs with many thousands of keys.

**Best measured result.** 3.35s to 1.29-1.65s per batch (about 2-2.6x) (pr:lodestar#2717)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/attester_duties.rs:61-69`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L61-L69) cached path calls chain.validator_attestation_duties for the whole index batch
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1747-1758`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1747-L1758) one with_committee_cache lookup for the batch, then per-validator committee_cache.get_attestation_duties
- [`consensus/types/src/state/committee_cache.rs:392-397`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L392-L397) shuffled_position is an O(1) array lookup (no per-validator committee materialisation)
- [`consensus/types/src/state/committee_cache.rs:302-323`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L302-L323) linear loop over 0..epoch_committee_count per validator
- [`consensus/types/src/state/committee_cache.rs:420-433`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L420-L433) committee ranges are floor(len*i/count), so the index is directly computable

**Second check.** Checked both http_api duty paths (cached and state fallback at attester_duties.rs:157 via BeaconState::get_attestation_duties) and compute_committee_range_in_epoch; no direct-index or single-pass variant exists. Lighthouse already avoids the expensive part of the Lodestar fix (per-validator committee search over materialised lists) via shuffling_positions.

**Sources.** [lodestar#2717](https://github.com/ChainSafe/lodestar/pull/2717), [prysm#4416](https://github.com/OffchainLabs/prysm/pull/4416), [lodestar#2698](https://github.com/ChainSafe/lodestar/pull/2698)

</details>


<a id="beacon_api-006"></a>
<details>
<summary><b>beacon_api-006</b> Return assignments only for requested validators — <i>partial · low · S · memory, cpu</i></summary>

**Idea.** In duty and assignment queries, build committee assignments only for the requested validator indices (and compute proposers separately) instead of building a map over every active validator, avoiding a large per-request allocation.

**Gap in Lighthouse.** Main paths already compute per requested index with no all-validator map. Committee-assignment style endpoints are not index-filtered at build time, but no all-validator map exists, so little is left to fix.

**Impact.** Negligible; no per-request O(N_validators) allocation seen in duty paths.

**Best measured result.** over 32 MB heap with 1M validators (pr:prysm#14039)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:1752`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1752) attester duties computed only for requested indices from committee cache
- [`beacon_node/http_api/src/proposer_duties.rs:230`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/proposer_duties.rs#L230) proposers computed separately
- [`beacon_node/http_api/src/attester_duties.rs:143`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L143) historic path builds committee cache and queries per index

**Sources.** [prysm#14039](https://github.com/OffchainLabs/prysm/pull/14039)

</details>


<a id="beacon_api-008"></a>
<details>
<summary><b>beacon_api-008</b> Run heavy API handlers on blocking thread pool — <i>implemented · low · cpu, latency</i></summary>

**Idea.** Run CPU-heavy HTTP handlers (state work, signature decompression in validator registrations) on a blocking thread pool instead of the async executor, and skip needless message passing to other services, so they do not stall other async tasks.

**Impact.** Already done; async executor not stalled by state work.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/task_spawner.rs:48`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/task_spawner.rs#L48) blocking_task runs handler on beacon processor/blocking pool
- [`beacon_node/http_api/src/task_spawner.rs:97`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/task_spawner.rs#L97) blocking_json_task
- [`beacon_node/http_api/src/beacon/states.rs:853`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L853) validators handlers use blocking_json_task
- [`beacon_node/http_api/src/validator/mod.rs:86`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L86) validator endpoints use blocking_json_task

**Sources.** [lighthouse#1518](https://github.com/sigp/lighthouse/pull/1518), [grandine#467](https://github.com/grandinetech/grandine/pull/467), [grandine@54b8cd815](https://github.com/grandinetech/grandine/commit/54b8cd8158ad)

</details>


<a id="beacon_api-011"></a>
<details>
<summary><b>beacon_api-011</b> POST variant of validators and balances queries — <i>implemented · low · cpu, latency</i></summary>

**Idea.** Offer POST variants of the state validators and validator_balances endpoints that take the id list in the body, so clients fetch large validator subsets in one request instead of many per-validator GETs (each loading a state) or hitting URL length limits.

**Impact.** Already done.

**Best measured result.** qualitative: thousands of times slower with individual queries (pr:lighthouse#4872)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/beacon/states.rs:835`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L835) post_beacon_state_validators (body ids)
- [`beacon_node/http_api/src/beacon/states.rs:979`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L979) post_beacon_state_validator_balances
- [`beacon_node/http_api/src/beacon/states.rs:931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L931) post validator_identities

**Sources.** [lighthouse#4872](https://github.com/sigp/lighthouse/pull/4872), [lodestar#6655](https://github.com/ChainSafe/lodestar/pull/6655)

</details>


<a id="beacon_api-012"></a>
<details>
<summary><b>beacon_api-012</b> SSZ responses for validators and balances endpoints — <i>partial · low · S · cpu, bandwidth, latency</i></summary>

**Idea.** Serve the state validators and validator_balances endpoints as SSZ (application/octet-stream) when the Accept header asks for it, avoiding JSON encoding cost and the large JSON response for big validator sets.

**Gap in Lighthouse.** Add Accept: application/octet-stream handling to post_beacon_state_validators and get_beacon_state_validators (ValidatorData SSZ-encode list), as done for balances.

**Impact.** Large /validators responses (whole set, ~1M entries) avoid JSON encode; saves hundreds of ms CPU and several x payload for tools that fetch all validators, rare on a node.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/beacon/states.rs:979`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L979),1020 validator_balances GET/POST honour Accept ssz
- [`beacon_node/http_api/src/beacon/states.rs:835`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L835),896 validators GET/POST take no Accept header, JSON only
- [`beacon_node/http_api/src/beacon/states.rs:931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L931) validator_identities has an ssz variant

**Sources.** [grandine@5e3bd3388](https://github.com/grandinetech/grandine/commit/5e3bd3388980), [grandine#801](https://github.com/grandinetech/grandine/pull/801), [lodestar#6060](https://github.com/ChainSafe/lodestar/pull/6060), [prysm#17077](https://github.com/OffchainLabs/prysm/pull/17077), [lighthouse#10082](https://github.com/sigp/lighthouse/pull/10082)

</details>


<a id="beacon_api-015"></a>
<details>
<summary><b>beacon_api-015</b> SSZ for block production endpoints — <i>implemented · low · cpu, bandwidth, latency</i></summary>

**Idea.** Support SSZ responses for the produce-block endpoints (full and blinded) and have the validator client request SSZ by default with JSON fallback, so large blocks skip JSON encoding and decoding on both sides.

**Impact.** Already done.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/produce_block.rs:225`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/produce_block.rs#L225) Accept::Ssz branch in v3 response
- [`beacon_node/http_api/src/produce_block.rs:283`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/produce_block.rs#L283) v2 ssz
- [`validator_client/validator_services/src/block_service.rs:794`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/block_service.rs#L794) VC uses get_validator_blocks_v3_ssz
- [`validator_client/validator_services/src/block_service.rs:806`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/block_service.rs#L806) falls back on error

**Sources.** [prysm#15390](https://github.com/OffchainLabs/prysm/pull/15390), [prysm#10697](https://github.com/OffchainLabs/prysm/pull/10697), [lighthouse#4534](https://github.com/sigp/lighthouse/pull/4534)

</details>


<a id="beacon_api-018"></a>
<details>
<summary><b>beacon_api-018</b> Accept SSZ bodies when publishing blocks — <i>implemented · low · cpu, bandwidth, latency</i></summary>

**Idea.** Accept SSZ request bodies (Content-Type octet-stream) on the publish block and publish blinded block endpoints, avoiding JSON parsing of large blocks and shrinking the request.

**Impact.** Already done.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs:895`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L895) post_beacon_blocks_ssz
- [`beacon_node/http_api/src/lib.rs:1052`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L1052) blinded ssz
- [`beacon_node/http_api/src/lib.rs:977`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L977),1127 v2 ssz variants

**Sources.** [lighthouse#4504](https://github.com/sigp/lighthouse/pull/4504), [lighthouse#4479](https://github.com/sigp/lighthouse/pull/4479), [prysm#10663](https://github.com/OffchainLabs/prysm/pull/10663)

</details>


<a id="beacon_api-021"></a>
<details>
<summary><b>beacon_api-021</b> Request builder API responses as SSZ — <i>implemented · medium · cpu, bandwidth, latency</i></summary>

**Idea.** In the builder/MEV-relay client, prefer SSZ in the Accept header (and send SSZ) instead of JSON, avoiding JSON encode/decode and size for headers and payloads.

**Impact.** Already done; SSZ preferred for builder responses and requests.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/builder_client/src/lib.rs:23`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/builder_client/src/lib.rs#L23) PREFERENCE_ACCEPT_VALUE prefers octet-stream
- [`beacon_node/builder_client/src/pre_gloas_builder_http_client.rs:291`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/builder_client/src/pre_gloas_builder_http_client.rs#L291),390 header sent; line 142 SSZ used unless disable_ssz
- [`beacon_node/builder_client/src/builder_http_client.rs:2`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/builder_client/src/builder_http_client.rs#L2) same for gloas client

**Sources.** [nimbus#6970](https://github.com/status-im/nimbus-eth2/pull/6970)

</details>


<a id="beacon_api-023"></a>
<details>
<summary><b>beacon_api-023</b> Generic Accept negotiation to serve SSZ — <i>not · low · M · cpu, bandwidth</i></summary>

**Idea.** Add a generic, configurable HTTP encoding layer with Accept-header negotiation so any REST endpoint can serve SSZ instead of JSON without per-endpoint code.

**Gap in Lighthouse.** Add a generic warp filter/reply wrapper that negotiates Accept and SSZ-encodes any Encode type, replacing the per-endpoint boilerplate.

**Impact.** No runtime gain on its own; only reduces code and makes adding SSZ to remaining JSON-only endpoints cheap.

**Best measured result.** 'more compact and performant'; no numbers (pr:prysm#15381)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/beacon/states.rs:40`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L40),100,160 each endpoint repeats warp::header::optional Accept and a match accept_header
- [`beacon_node/http_api/src/lib.rs:1190`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L1190) same per-endpoint pattern

**Sources.** [prysm#15381](https://github.com/OffchainLabs/prysm/pull/15381)

</details>


<a id="beacon_api-024"></a>
<details>
<summary><b>beacon_api-024</b> Process submitted pool messages in background after response — <i>not · medium · M · latency</i></summary>

**Idea.** For submitted attestations and sync committee messages, publish to gossip and return the HTTP response right away, and run validation-heavy work (state lookup, pool processing) in a detached background task, so request latency and timeouts are not tied to processing or the gossip loop.

**Gap in Lighthouse.** Network publish happens right after gossip verification, but fork choice, naive aggregation pool insert and unknown-block reprocessing waits stay on the response path. Lighthouse would need to respond after publish and detach the rest (fork choice, pool, reprocess wait), which drops the per-item error reporting the spec defines.

**Impact.** Lower submission latency, mostly for attestations to unknown blocks that wait in the reprocess queue; no CPU saving.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/publish_attestations.rs:70-120`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_attestations.rs#L70-L120) gossip verify, publish, then fork-choice and naive pool insert all run before returning
- [`beacon_node/http_api/src/publish_attestations.rs:140-252`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_attestations.rs#L140-L252) blocking_task is awaited and reprocess oneshots are joined (join_all) before building the response
- [`beacon_node/http_api/src/beacon/pool.rs:554`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/pool.rs#L554) route awaits publish_attestations
- [`beacon_node/http_api/src/beacon/pool.rs:181`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/pool.rs#L181) sync committee route calls process_sync_committee_signatures synchronously

**Second check.** Read the full publish_attestations flow incl. reprocess handling and the pool.rs routes; reprocessing is awaited asynchronously (not blocking workers) but the HTTP response still waits for it, so nothing detached exists.

**Sources.** [prysm#3487](https://github.com/OffchainLabs/prysm/pull/3487), [caplin#24259](https://github.com/erigontech/erigon/pull/24259), [prysm#16152](https://github.com/OffchainLabs/prysm/pull/16152)

</details>


<a id="beacon_api-027"></a>
<details>
<summary><b>beacon_api-027</b> Bounded per-subscriber SSE queues, drop slow clients — <i>partial · low · S · latency, memory</i></summary>

**Idea.** Give each SSE event-stream subscriber its own bounded queue and writer task, decoupled from the event producer, and disconnect subscribers that fall behind; flush once per drained batch. This stops one slow reader from back-pressuring block import or other subscribers.

**Gap in Lighthouse.** Each subscriber has a bounded broadcast receiver and the producer never blocks (send is non-blocking), so back-pressure on import is absent. Slow clients are not disconnected, they just get dropped-message comments; no per-batch flush. Would need a Lagged counter that closes the stream in the events handler in http_api/src/lib.rs.

**Impact.** Marginal: producer is already decoupled; only saves memory held by stalled SSE clients.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/events.rs:45`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/events.rs#L45) tokio broadcast channel per topic
- [`beacon_node/http_api/src/lib.rs:3449`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L3449) BroadcastStream, Lagged -&gt; comment, stream continues

**Sources.** [teku#2886](https://github.com/Consensys-Incorporated/teku/pull/2886), [prysm#14413](https://github.com/OffchainLabs/prysm/pull/14413), [caplin#24447](https://github.com/erigontech/erigon/pull/24447), [prysm#13329](https://github.com/OffchainLabs/prysm/pull/13329)

</details>


<a id="beacon_api-033"></a>
<details>
<summary><b>beacon_api-033</b> Emit head/block SSE event early in import — <i>implemented · medium · latency</i></summary>

**Idea.** Emit the head (or block-processed) SSE event as soon as fork choice selects the new head, before slow persistence and before the EL marks an optimistic head Valid (re-emit once then), so validator clients can attest sooner.

**Impact.** Head events already fire before persist_fork_choice (500ms-1s on epoch boundaries) and before DB writes.

**Best measured result.** persist_fork_choice 500ms-1s avoided (pr:lighthouse#8718)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:4592-4640`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4592-L4640) Head SSE registered inside import_block once fork choice picks new head, before after_new_head
- [`beacon_node/beacon_chain/src/canonical_head.rs:1222-1262`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1222-L1262) second head_v2 event when payload status changes
- [`beacon_node/beacon_chain/src/canonical_head.rs:1565`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1565) persist_fork_choice now only later in after_new_head

**Sources.** [lighthouse#8718](https://github.com/sigp/lighthouse/pull/8718), [prysm#17241](https://github.com/OffchainLabs/prysm/pull/17241), [silver#277](https://github.com/gattaca-com/silver/pull/277)

</details>


<a id="beacon_api-035"></a>
<details>
<summary><b>beacon_api-035</b> Answer attestation_data from fork choice — <i>implemented · medium · S · latency</i></summary>

**Idea.** Build attestation_data from fork-choice data (head root, ancestor target root, justified checkpoint) instead of waiting for or reading the new head state, so the request does not block on state publication on empty slots.

**Impact.** Goal already met: on an empty first slot of an epoch the request hits the pre-advanced head state in the state cache (cheap milhouse clone, committee cache prebuilt); no blocking on state publication. A fork-choice-only path would save only the cache lookup.

**Best measured result.** every request answered within 3 ms; used to take 1 s on empty slots (pr:caplin#25359)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2025-2039`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2025-L2039) early_attester_cache answers during block import before the head is set
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2063-2141`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2063-L2141) head root/target/justified read from the in-memory head snapshot (fork choice output), no wait
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:1-9`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L1-L9),258-286 timer pre-advances the head state one slot at the end of each slot (incl. across the epoch boundary)
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:333-339`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L333-L339),455 builds current/next committee caches and stores the advanced state
- [`beacon_node/store/src/hot_cold_store.rs:1068-1076`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1068-L1076),1667 put_state -&gt; store_hot_state inserts into state_cache
- [`beacon_node/store/src/hot_cold_store.rs:1124-1131`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1124-L1131) get_advanced_hot_state returns that pre-advanced state from cache
- [`beacon_node/store/src/state_cache.rs:316-333`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L316-L333) get_by_block_root finds the advanced state for the head block root
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2159-2174`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2159-L2174) partial_state_advance only runs if the cached state is still in an older epoch

**Second check.** Earlier review missed the state_advance_timer: it pre-advances the head state into the next epoch at the end of the previous slot and puts it in the state cache, so the cross-epoch branch of produce_unaggregated_attestation is a cache hit, not a state load/advance, which is the Lighthouse equivalent of Caplin's fix.

**Sources.** [caplin#25359](https://github.com/erigontech/erigon/pull/25359)

</details>


<a id="beacon_api-036"></a>
<details>
<summary><b>beacon_api-036</b> Cache attestation data per slot, no per-request state copy — <i>implemented · medium · S · memory, cpu</i></summary>

**Idea.** Compute attestation_data once per slot (shared by all committees and validator clients) and reuse a shared state reference, instead of copying the head state for every attestation_data request or committee.

**Gap in Lighthouse.** No BN-side (slot, head root) -&gt; AttestationData memo across multiple VCs; each request re-reads a few fields from the head snapshot. Negligible cost, so not worth adding.

**Impact.** The per-request state copy and per-committee recomputation that Prysm/Caplin fixed do not exist in Lighthouse; a BN memo would save microseconds.

**Best measured result.** saves ~1GB runtime memory with 4k validators (pr:prysm#6025)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/attestation_service.rs:257`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L257),284,332 VC fetches attestation_data once per slot with index 0 and shares it
- [`validator_client/validator_services/src/attestation_service.rs:398-422`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L398-L422) same AttestationData cloned to every committee's aggregation task
- [`beacon_node/http_api/src/validator/mod.rs:290-296`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L290-L296) BN always uses committee index 0 (one data per slot post-Electra)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2063-2141`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2063-L2141) common path borrows the Arc head snapshot, no state copy
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:258-286`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L258-L286),455 cross-epoch path hits the pre-advanced cached state (structurally shared milhouse clone)

**Second check.** Checked the VC side (attestation_service fetches once per slot and fans out to committees) and the state-advance/state-cache path; the only missing piece is a literal BN memo, whose work it would skip is a handful of field reads.

**Sources.** [caplin#11680](https://github.com/erigontech/erigon/pull/11680), [prysm#6025](https://github.com/OffchainLabs/prysm/pull/6025), [prysm#6185](https://github.com/OffchainLabs/prysm/pull/6185)

</details>


<a id="beacon_api-038"></a>
<details>
<summary><b>beacon_api-038</b> Read head state fields without cloning the state — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** Serve API fields such as fork, genesis validators root, justified checkpoints, committee seeds and validator indices through cheap chain getters or a read-only head state reference, instead of deep-cloning the head state per request.

**Impact.** Already avoids head state copies on main routes; state.clone() is also cheap with milhouse tree states.

**Best measured result.** wasteful to copy the entire state (1.3GB in heap profile) (pr:prysm#5582)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/state_id.rs:223`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L223) map_state_and_execution_optimistic_and_finalized uses head snapshot by reference
- state_id.rs:152 fork() goes through the by-reference map

**Sources.** [prysm#3671](https://github.com/OffchainLabs/prysm/pull/3671), [prysm#4333](https://github.com/OffchainLabs/prysm/pull/4333), [prysm#11949](https://github.com/OffchainLabs/prysm/pull/11949), [prysm#5582](https://github.com/OffchainLabs/prysm/pull/5582), [prysm#4335](https://github.com/OffchainLabs/prysm/pull/4335)

</details>


<a id="beacon_api-048"></a>
<details>
<summary><b>beacon_api-048</b> Skip state root recompute after process_slots — <i>implemented · medium · cpu</i></summary>

**Idea.** When replaying a state for an API request, do not recompute the full state hash tree root if process_slots already set it; only patch the latest header state root for non-missing blocks.

**Impact.** Duties and sync-duty replays already skip full state root recomputation.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/state_advance.rs:72-112`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/state_advance.rs#L72-L112) partial_state_advance passes zero state roots, avoiding tree hashing of intermediate slots
- [`beacon_node/http_api/src/attester_duties.rs:194`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L194) uses partial_state_advance
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1552-1554`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1552-L1554) StateSkipConfig::WithoutStateRoots

**Sources.** [prysm#10852](https://github.com/OffchainLabs/prysm/pull/10852)

</details>


<a id="beacon_api-051"></a>
<details>
<summary><b>beacon_api-051</b> Optimistic status from fork choice, not state hash — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** When an API response needs execution_optimistic, derive it from the block root and fork-choice data instead of computing the full state hash tree root, avoiding large allocations and CPU per request.

**Impact.** No state hash root is computed for optimistic flag.

**Best measured result.** Fixes reported out-of-memory on API requests; no numbers (pr:prysm#12143)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/state_id.rs:60-120`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L60-L120) optimistic status from fork_choice is_optimistic_or_invalid_block_assuming_full / head_and_execution_status

**Sources.** [prysm#12143](https://github.com/OffchainLabs/prysm/pull/12143)

</details>


<a id="beacon_api-052"></a>
<details>
<summary><b>beacon_api-052</b> State root endpoint from stored block state_root — <i>implemented · medium · cpu, disk, latency</i></summary>

**Idea.** Serve the state root endpoint from the stored block's state_root field (or a root cache) instead of loading the full state and hashing it.

**Impact.** State root endpoint avoids loading and hashing the state.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/state_id.rs:23-136`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L23-L136) StateId::root resolves root without loading state
- [`beacon_node/beacon_chain/src/beacon_chain.rs:964-1014`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L964-L1014) state_root_at_slot uses split, head state roots, or forwards iterator

**Sources.** [prysm#16765](https://github.com/OffchainLabs/prysm/pull/16765)

</details>


<a id="beacon_api-057"></a>
<details>
<summary><b>beacon_api-057</b> Bound state regeneration for far-out API requests — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Reject API requests that would force regenerating or advancing a state through arbitrarily many slots: future slots beyond the clock, sync duties beyond the next period, or replays of empty slots beyond a cap, returning 404/400/503. This stops a single request from starving block import.

**Gap in Lighthouse.** BeaconChain::state_at_slot itself has no hard cap (beacon_chain.rs:1541-1547 only warns); it is reachable with a large lag only when sync state is Stalled/Synced, i.e. no peers and therefore no block import to starve. Optional: also return an error in state_at_slot above N epochs.

**Impact.** All three listed protections exist; the remaining case (stalled node with lagging head) has no competing block import.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs:474-511`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L474-L511) not_while_syncing_filter returns 503 when head_slot + sync_tolerance_epochs*32 &lt; current_slot during SyncingFinalized/SyncingHead
- [`beacon_node/beacon_chain/src/chain_config.rs:16`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/chain_config.rs#L16) DEFAULT_SYNC_TOLERANCE_EPOCHS = 2
- [`beacon_node/http_api/src/validator/mod.rs:78`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L78),125,161,197,228,267 duties, sync duties, attestation_data, etc. all wrapped in not_while_syncing_filter
- [`beacon_node/http_api/src/validator/mod.rs:283`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L283) rejects attestation_data slot &gt; current+1
- [`beacon_node/http_api/src/sync_committees.rs:96-131`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/sync_committees.rs#L96-L131) sync duties bounded to current period + 1
- [`beacon_node/http_api/src/state_id.rs:127`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L127) future-slot state ids give 404
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:37`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L37),268-275 background advance capped at MAX_ADVANCE_DISTANCE = 256 slots

**Second check.** Earlier review missed not_while_syncing_filter: the validator endpoints that would call state_at_slot with a lagging head return 503 once the head is more than 2 epochs behind the clock while syncing, which is the empty-slot replay cap the idea asks for, enforced at the API layer.

**Sources.** [lodestar#9634](https://github.com/ChainSafe/lodestar/pull/9634), [teku#3956](https://github.com/Consensys-Incorporated/teku/pull/3956), [lodestar#8665](https://github.com/ChainSafe/lodestar/pull/8665)

</details>


<a id="beacon_api-058"></a>
<details>
<summary><b>beacon_api-058</b> Advance state only to epoch start for committees — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** When computing committees for a requested slot, advance the head state only to the start of that slot's epoch (not at all if the epoch is not ahead of head), instead of slot by slot to the requested slot.

**Impact.** Committees are computed straight for the epoch, not by advancing slot by slot.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/beacon/states.rs:587-720`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L587-L720) committees built by CommitteeCache::initialized(state, epoch) from existing state with historical_committee_cache, no slot-by-slot advance
- [`beacon_node/http_api/src/attester_duties.rs:187-196`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L187-L196) advances only to epoch start

**Sources.** [prysm#4297](https://github.com/OffchainLabs/prysm/pull/4297)

</details>


<a id="beacon_api-060"></a>
<details>
<summary><b>beacon_api-060</b> Box large async futures on block publish — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** In the block publish path, box large futures (Box::pin) and pass Arcs instead of moving blocks or states by value, shrinking future sizes to avoid stack overflows and large stack copies.

**Impact.** Smaller futures, avoids stack overflow; negligible CPU.

**Best measured result.** futures 100KB to ~33KB, then ~16KB (pr:lighthouse#5104)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/publish_blocks.rs:335`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L335),353,404 Box::pin on process_block and process_gossip_data_columns

**Sources.** [lighthouse#5104](https://github.com/sigp/lighthouse/pull/5104)

</details>


<a id="beacon_api-065"></a>
<details>
<summary><b>beacon_api-065</b> Resolve state_id directly via selector — <i>partial · low · S · cpu, disk, latency</i></summary>

**Idea.** Resolve a state_id (head, finalized, root, slot) directly to the state through the matching selector instead of converting it to a slot first and looking the state up again, so head and finalized are served from in-memory states.

**Gap in Lighthouse.** Head is served from the in-memory snapshot, but finalized/justified go checkpoint -&gt; slot -&gt; state_root_at_slot -&gt; chain.get_state (state cache/DB). Could resolve finalized/justified straight to the checkpoint state root via fork choice/state cache in StateId::root and state.

**Impact.** Faster finalized/justified state API calls; rarely hot on a mainnet node.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/state_id.rs:25`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L25) root() resolves selector; Head returns early at :34 and :186; Finalized/Justified convert checkpoint to slot then state_root_at_slot at :112

**Sources.** [teku#3118](https://github.com/Consensys-Incorporated/teku/pull/3118), [teku#3119](https://github.com/Consensys-Incorporated/teku/pull/3119), [teku#3120](https://github.com/Consensys-Incorporated/teku/pull/3120), [teku#3123](https://github.com/Consensys-Incorporated/teku/pull/3123), [teku#3128](https://github.com/Consensys-Incorporated/teku/pull/3128)

</details>


<a id="beacon_api-069"></a>
<details>
<summary><b>beacon_api-069</b> Separate small committee cache for HTTP committees route — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Serve the committees HTTP route for historical epochs from a separate small committee cache, so historical queries do not evict or constrain the main chain committee/shuffling cache.

**Impact.** Historical committee queries do not evict the main shuffling cache.

**Best measured result.** Slight extra memory cost; no speedup stated (pr:lighthouse#9318)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/caches.rs:22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/caches.rs#L22) HistoricalCommitteeCache LRU separate from chain shuffling cache
- http_api/src/lib.rs:153 historical_committee_cache_size

**Sources.** [lighthouse#9318](https://github.com/sigp/lighthouse/pull/9318)

</details>


<a id="beacon_api-073"></a>
<details>
<summary><b>beacon_api-073</b> Doppelganger check early return skips historical states — <i>n/a · medium · cpu, startup</i></summary>

**Idea.** In the doppelganger/liveness check, return early when all requested keys were recently observed, so the expensive regeneration of historical states is skipped.

**Impact.** Lighthouse's liveness check reads in-memory observed attester sets and never loads historical states, bounded to prev/current/next epoch.

**Best measured result.** Not quantified; allows quicker validator restarts (pr:prysm#9964)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/validator/mod.rs:595-640`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L595-L640) liveness answered from in-memory observed_* sets
- [`beacon_node/beacon_chain/src/beacon_chain.rs:8346`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L8346) validator_seen_at_epoch

**Sources.** [prysm#9964](https://github.com/OffchainLabs/prysm/pull/9964)

</details>


<a id="beacon_api-075"></a>
<details>
<summary><b>beacon_api-075</b> Validator activation status check once per epoch — <i>not · low · M · cpu</i></summary>

**Idea.** In validator listing/status queries, compute validator activation status checks once per epoch and reuse the result, instead of on every slot or call, since assignments only change per epoch.

**Gap in Lighthouse.** Cache per-epoch status or index-by-pubkey so get_beacon_state_validators avoids a full validator scan per call; the full scan with status per validator is O(N) over ~1M validators. Add an epoch-keyed cache in validators.rs.

**Impact.** Large unfiltered /validators calls would be cheaper; only matters for heavy API consumers.

**Best measured result.** ~6% of run time was spent in list_validators (pr:prysm#11340)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/validators.rs:13-70`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validators.rs#L13-L70) computes ValidatorStatus::from_validator per validator on each request, no cache

**Sources.** [prysm#11340](https://github.com/OffchainLabs/prysm/pull/11340)

</details>


<a id="beacon_api-078"></a>
<details>
<summary><b>beacon_api-078</b> Fetch blobs from EL on gossip block arrival — <i>implemented · high · latency, bandwidth, sync</i></summary>

**Idea.** When a gossip block with blob commitments arrives, call engine_getBlobs on the local EL and build the blob/data column sidecars from the response. The block becomes available without waiting for the sidecars from gossip or peers.

**Impact.** Already done; blocks become available from EL blobs without waiting for gossip columns.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/fetch_blobs/fetch_blobs_beacon_adapter.rs:54`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/fetch_blobs_beacon_adapter.rs#L54) get_blobs_v2/v3/v4 adapter
- [`beacon_node/network/src/network_beacon_processor/mod.rs:1020`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L1020) fetch_and_process_engine_blobs builds custody columns and imports
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1936`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1936) spawn_fetch_block_columns on gossip block

**Sources.** [nimbus#7123](https://github.com/status-im/nimbus-eth2/pull/7123), [lodestar#7679](https://github.com/ChainSafe/lodestar/pull/7679), [prysm#15483](https://github.com/OffchainLabs/prysm/pull/15483), [caplin#25447](https://github.com/erigontech/erigon/pull/25447), [grandine#79](https://github.com/grandinetech/grandine/pull/79), [lodestar#7134](https://github.com/ChainSafe/lodestar/pull/7134), [nimbus#7866](https://github.com/status-im/nimbus-eth2/pull/7866)

</details>


<a id="beacon_api-079"></a>
<details>
<summary><b>beacon_api-079</b> Query EL first, request only remaining blobs from peers — <i>partial · medium · M · latency, bandwidth</i></summary>

**Idea.** When blobs or columns for a block are missing, query the local EL first and send RPC requests to peers only for the ones still missing. Share one received-sidecar set between the EL and the p2p fetch paths so no sidecar is fetched twice.

**Gap in Lighthouse.** The subtraction the earlier review asked for already exists: lookups skip columns already in the DA cache, and RPC lookup blocks trigger getBlobs. What is missing is ordering and in-flight sharing: the lookup custody request starts on block download, in parallel with (and before) the EL fetch that runs only after block processing, and ActiveCustodyRequest does not re-check the DA cache to drop columns the EL fills while requests are in flight. Fix: for recent blocks, run getBlobs first (or gate custody_lookup_request on it), and re-filter pending column indices against cached_data_column_indexes before each continue_requests.

**Impact.** Fewer redundant column RPC bytes and KZG verifications during unknown-block lookups when the EL holds the blobs; small on mainnet where gossip usually wins.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context.rs:970-991`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L970-L991) custody_lookup_request filters sampling columns by cached_data_column_indexes (gossip and EL-imported columns are skipped)
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:209-222`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L209-L222) lookup block with MissingComponents triggers fetch_engine_blobs_and_publish_full
- [`beacon_node/network/src/sync/block_lookups/single_block_lookup.rs:398-433`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/single_block_lookup.rs#L398-L433) data request starts as soon as the block is downloaded, not after the EL fetch settles
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1370`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1370) partial-column cell requests wait for local_fetch_settled

**Second check.** Found that custody_lookup_request already dedupes against the DA cache and that sync_methods triggers getBlobs for lookup blocks, so the earlier fix is already there; the remaining gap is that the RPC request is not gated on, or refreshed after, the EL result.

**Sources.** [teku#8663](https://github.com/Consensys-Incorporated/teku/pull/8663), [grandine@a850e357b](https://github.com/grandinetech/grandine/commit/a850e357b76b), [grandine#114](https://github.com/grandinetech/grandine/pull/114), [teku#8927](https://github.com/Consensys-Incorporated/teku/pull/8927)

</details>


<a id="beacon_api-080"></a>
<details>
<summary><b>beacon_api-080</b> Trigger getBlobs on first gossip column sidecar — <i>partial · medium · S · latency, bandwidth</i></summary>

**Idea.** Start the EL getBlobs fetch when the first valid data column sidecar arrives on gossip, also before its block arrives. The missing columns are then built from EL blobs sooner than with a trigger on block arrival only.

**Gap in Lighthouse.** A full Fulu data column sidecar arriving before the block passes gossip verification (it carries the signed header and commitments) but does not trigger getBlobs; only partial headers and blocks do. Fix: in process_gossip_verified_data_column, on the first column for a block root, build a PartialHeaderOrBid::PartialHeader from the column header/commitments and call fetch_engine_blobs_and_publish_full (lighthouse#7329 did this and was closed unmerged).

**Impact.** Saves tens to hundreds of ms when a full column beats the block; only matters for nodes or peers not using partial columns.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1119-1135`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1119-L1135) getBlobs triggered on first uncached partial header
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:926-1024`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L926-L1024) process_gossip_verified_data_column: republishes as partial and processes, MissingComponents only calls check_reconstruction_trigger, no getBlobs
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1242`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1242) BlockRootUnknown for full columns is Gloas-only (needs the bid); Fulu full columns verify without the block
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1936`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1936) trigger on gossip-verified block

**Second check.** Checked that the BlockRootUnknown branch the earlier review cited only fires for Gloas, and that the Fulu full-column success path has no EL trigger; lighthouse#7329 is closed unmerged.

**Sources.** [lighthouse#7329](https://github.com/sigp/lighthouse/pull/7329), [nimbus#8393](https://github.com/status-im/nimbus-eth2/pull/8393)

</details>


<a id="beacon_api-081"></a>
<details>
<summary><b>beacon_api-081</b> Call getBlobs before block verification completes — <i>implemented · high · latency, bandwidth</i></summary>

**Idea.** Start the EL getBlobs fetch as soon as a gossip block header is seen, before consensus and execution verification of the block. The local blobs then win the race against gossip and can be published.

**Impact.** Already done; the fetch runs concurrently with consensus and execution verification, publishing columns early.

**Best measured result.** 116 hits and 156 blobs published in 30 min on mainnet, up from a few hits per hour (pr:lighthouse#6600)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1936`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1936) spawn_fetch_block_columns called before chain.process_block (after gossip validation only)
- [`beacon_node/network/src/network_beacon_processor/mod.rs:960`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L960) spawn_fetch_block_columns spawns detached task, publishes columns gradually
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1127`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1127) also triggered from partial-column header

**Sources.** [lighthouse#6600](https://github.com/sigp/lighthouse/pull/6600)

</details>


<a id="beacon_api-082"></a>
<details>
<summary><b>beacon_api-082</b> Fetch blobs from EL during block lookup sync — <i>implemented · medium · latency, bandwidth</i></summary>

**Idea.** In unknown-block / lookup sync for a block by root, also try engine_getBlobs before requesting blobs or columns from peers. Availability can then resolve locally without RPC.

**Impact.** Lookup-imported blocks resolve availability from the EL without column RPC.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:208`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L208) on MissingComponents for a lookup block, calls fetch_engine_blobs_and_publish_full
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:113`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L113) fetch_and_process_engine_blobs

**Sources.** [lodestar#7724](https://github.com/ChainSafe/lodestar/pull/7724)

</details>


<a id="beacon_api-083"></a>
<details>
<summary><b>beacon_api-083</b> Fetch EL blobs for blocks published via API — <i>implemented · medium · latency, bandwidth</i></summary>

**Idea.** When a block is published through the HTTP API without blob data, still trigger the EL getBlobs fetch and the column requests for it, because later gossip duplicates of the block are ignored.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/publish_blocks.rs:222`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L222) NetworkMessage::FetchBlockColumns after publishing
- [`beacon_node/network/src/service.rs:697`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L697) spawn_fetch_block_columns with EnvelopeSource::Http

**Sources.** [lighthouse#10396](https://github.com/sigp/lighthouse/pull/10396)

</details>


<a id="beacon_api-084"></a>
<details>
<summary><b>beacon_api-084</b> Use existence-only EL blob query — <i>not · medium · M · latency, bandwidth</i></summary>

**Idea.** Use an existence-only Engine API call (HasBlobs) to learn which blobs the EL holds, so held cells can be advertised to peers at once without the slower full getBlobs round trip.

**Gap in Lighthouse.** No existence-only Engine API call (HasBlobs or similar bitmap query) and no early advertisement of held cells before the full getBlobs response. Fix: add the method in execution_layer and use its bitmap to set present cells in the partial assembler early. Needs EL support.

**Impact.** Lets partial-column peers learn held cells one EL round trip earlier; tens of ms on propagation.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engine_api/http.rs:71-73`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L71-L73) only engine_getBlobsV2/V3/V4 constants
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:398-460`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L398-L460) V4 path fetches cells and proofs

**Second check.** Searched execution_layer and fetch_blobs for has_blobs, blobs_exist, bitmap and availability queries; only the getBlobs family exists.

**Sources.** [prysm#16774](https://github.com/OffchainLabs/prysm/pull/16774)

</details>


<a id="beacon_api-088"></a>
<details>
<summary><b>beacon_api-088</b> Build only custodied columns from EL blobs — <i>partial · medium · S · cpu, memory</i></summary>

**Idea.** When data column sidecars are built from EL blobs, compute only the columns that the node custodies (column bitmap), not all 128 columns that are then filtered.

**Gap in Lighthouse.** Only the V4 path is custody-scoped. The V2/V3 fallback builds all 128 partial columns, then filters to custody and then dedupes against observed and cached columns. Fix: pass the custody indices minus already-known columns into blobs_to_partial_data_columns and build only those columns (cell computation via compute_cells still covers the whole blob).

**Impact.** Saves column assembly work and allocations per block on V2/V3 ELs for non-supernodes; cell FFT cost stays, so modest.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:158`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L158) V4 path requests only custody columns from the EL
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:686-705`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L686-L705) V2/V3 path calls blobs_to_partial_data_columns for all columns, then filters by custody_columns_indices
- [`beacon_node/beacon_chain/src/kzg_utils.rs:425-472`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L425-L472) blobs_to_partial_data_columns computes all cells and builds every column, no index parameter

**Second check.** Re-read the builder and the V2/V3 path; the custody filter and the observed/cached dedupe both run after all columns are built.

**Sources.** [nimbus#8672](https://github.com/status-im/nimbus-eth2/pull/8672)

</details>


<a id="beacon_api-089"></a>
<details>
<summary><b>beacon_api-089</b> Publish recovered columns off the availability path — <i>implemented · medium · latency, bandwidth</i></summary>

**Idea.** Publish columns recovered from EL blobs or reconstruction in a detached task after storing them, so block import and DA completion do not wait on network sends. Coalesce repeated partial publishes per (block, column).

**Impact.** Import does not wait on network sends. Explicit per-(block,column) coalescing of repeated partial publishes was not found.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/mod.rs:1013`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L1013) publish_fn spawns publish_data_columns_gradually
- [`beacon_node/network/src/network_beacon_processor/mod.rs:1271`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L1271) detached executor.spawn task
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:373`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L373) publish_fn does not await the network send

**Sources.** [nimbus#8655](https://github.com/status-im/nimbus-eth2/pull/8655), [prysm#17791](https://github.com/OffchainLabs/prysm/pull/17791)

</details>


<a id="beacon_api-090"></a>
<details>
<summary><b>beacon_api-090</b> Publish only needed recovered columns — <i>implemented · medium · cpu, bandwidth</i></summary>

**Idea.** When recovered columns are redistributed to gossip, publish only the columns that the network still needs instead of all of them.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/mod.rs:1298`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L1298) each batch filtered with observe_gossip_data_column, PriorKnown dropped
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:720`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L720) EL columns already observed on gossip dropped before import

**Sources.** [nimbus#8648](https://github.com/status-im/nimbus-eth2/pull/8648)

</details>


<a id="beacon_api-091"></a>
<details>
<summary><b>beacon_api-091</b> Mark data available at 50% columns — <i>not · medium · M · latency, bandwidth, sync</i></summary>

**Idea.** On nodes that custody all columns, treat a block as data-available once at least 50% of columns are verified (enough to reconstruct), and import it before reconstruction of the rest completes.

**Gap in Lighthouse.** Let make_available (Fulu overflow_lru_cache and Gloas pending_components) return available once &gt;= NUMBER_OF_COLUMNS/2 verified columns are held on full-custody nodes, import the block, and finish reconstruction/custody storage of the remaining columns in the background; DB/RPC serving must handle columns arriving after import. PR #7598 was closed unmerged.

**Impact.** Supernodes import without waiting for reconstruction (and its scheduled delay) when only about half the columns have arrived; saves hundreds of ms on such blocks, only on nodes custodying &gt;= 64 columns.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:212-234`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L212-L234) make_available requires received == num_of_data_columns_to_sample (Ordering::Equal), Less =&gt; None
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:620`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L620) total/2 only gates reconstruction start
- [`beacon_node/beacon_chain/src/pending_payload_cache/pending_components.rs:218-220`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/pending_components.rs#L218-L220) Gloas is_blob_data_available also needs &gt;= full sampling count
- [`beacon_node/beacon_chain/src/pending_payload_cache/mod.rs:643`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/mod.rs#L643) Gloas 50% only gates reconstruction
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3785-3870`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3785-L3870) import after 50% happens only via reconstruct_data_columns -&gt; process_availability, i.e. after reconstruction completes

**Second check.** Also checked the Gloas pending_payload_cache path and the reconstruction-to-import flow in beacon_chain.rs; both require the full sampling count before import, so the 50% threshold is never an availability shortcut.

**Sources.** [nimbus#8417](https://github.com/status-im/nimbus-eth2/pull/8417), [lighthouse#7598](https://github.com/sigp/lighthouse/pull/7598), [teku#10248](https://github.com/Consensys-Incorporated/teku/pull/10248), [grandine#424](https://github.com/grandinetech/grandine/pull/424), [lodestar#8408](https://github.com/ChainSafe/lodestar/pull/8408), [lodestar#8818](https://github.com/ChainSafe/lodestar/pull/8818)

</details>


<a id="beacon_api-092"></a>
<details>
<summary><b>beacon_api-092</b> Reconstruct remaining columns from half — <i>implemented · medium · cpu, latency, bandwidth, sync</i></summary>

**Idea.** Once at least 50% of data columns for a block are held, recover the missing columns by erasure-coding reconstruction (cell recovery), store and publish them, instead of downloading every column.

**Best measured result.** &lt;800ms to recover with 20 blobs (pr:lodestar#7940)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker.rs:537`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L537) reconstruct_data_columns
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:620`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L620) requires &gt;= total/2
- [`beacon_node/network/src/network_beacon_processor/mod.rs:1213`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L1213) attempt_data_column_reconstruction publishes recovered columns

**Sources.** [lighthouse#5781](https://github.com/sigp/lighthouse/pull/5781), [prysm#15454](https://github.com/OffchainLabs/prysm/pull/15454), [lodestar#7940](https://github.com/ChainSafe/lodestar/pull/7940), [lodestar#7935](https://github.com/ChainSafe/lodestar/pull/7935), [teku#10224](https://github.com/Consensys-Incorporated/teku/pull/10224), [prysm#17053](https://github.com/OffchainLabs/prysm/pull/17053)

</details>


<a id="beacon_api-093"></a>
<details>
<summary><b>beacon_api-093</b> Delay column reconstruction to wait for gossip — <i>implemented · low · S · cpu, latency, sync</i></summary>

**Idea.** Wait a short configurable time before starting column reconstruction (longer while syncing), because the missing columns often arrive via gossip or getBlobs and reconstruction is CPU-heavy.

**Impact.** Avoids redundant data column reconstructions; fixed delay, not configurable or sync-dependent, but same effect.

**Best measured result.** reduces the unnecessary amount of reconstructions during fast block import (commit:grandine@9e43a4aea5ad)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:73`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L73) QUEUED_RECONSTRUCTION_DELAY 150ms
- beacon_node/work_reprocessing_queue.rs:1139-1165 delay inserted/reset per block root, zero after 1/4 slot deadline

**Sources.** [lighthouse#7588](https://github.com/sigp/lighthouse/pull/7588), [grandine@9e43a4aea](https://github.com/grandinetech/grandine/commit/9e43a4aea5ad), [grandine#526](https://github.com/grandinetech/grandine/pull/526), [grandine@4f7f8f0ae](https://github.com/grandinetech/grandine/commit/4f7f8f0ae248)

</details>


<a id="beacon_api-096"></a>
<details>
<summary><b>beacon_api-096</b> Run column reconstruction once per block — <i>implemented · medium · cpu, memory, disk</i></summary>

**Idea.** Record the block roots for which column reconstruction was dispatched, is in flight or is complete, and skip new reconstruction requests for them. Share one reconstruction result across concurrent requesters.

**Best measured result.** duplicate rate 4-6% to 0 in test (pr:lighthouse#8985)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:614`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L614) reconstruction_started flag under write lock
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:592`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L592) check_and_set_reconstruction_started
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:1139`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L1139) queue dedups by block root (the race PRs 8855/8923/8985 were closed unmerged, but late duplicates just return NotStarted 'already started' without KZG work)

**Sources.** [lighthouse#8855](https://github.com/sigp/lighthouse/pull/8855), [lighthouse#8923](https://github.com/sigp/lighthouse/pull/8923), [lighthouse#8985](https://github.com/sigp/lighthouse/pull/8985), [lodestar#8383](https://github.com/ChainSafe/lodestar/pull/8383), [teku#11508](https://github.com/Consensys-Incorporated/teku/pull/11508), [teku#10296](https://github.com/Consensys-Incorporated/teku/pull/10296)

</details>


<a id="beacon_api-097"></a>
<details>
<summary><b>beacon_api-097</b> Dedicated thread pool for column reconstruction — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** Run data column computation and cell recovery on a dedicated (high-priority) thread pool, separate from the general pool and the fork choice/block import threads, so heavy KZG work does not starve other tasks.

**Best measured result.** reduces p99 latency during high load (commit:grandine@9af9e4de859b)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:3811`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3811) spawn_blocking_with_rayon_async(RayonPoolType::HighPriority) for reconstruct
- beacon_node/beacon_processor/src/rayon_manager.rs high priority pool (PR 8075)

**Sources.** [grandine@9af9e4de8](https://github.com/grandinetech/grandine/commit/9af9e4de859b), [grandine@79f20c521](https://github.com/grandinetech/grandine/commit/79f20c52179d), [grandine#362](https://github.com/grandinetech/grandine/pull/362), [lighthouse#8075](https://github.com/sigp/lighthouse/pull/8075)

</details>


<a id="beacon_api-098"></a>
<details>
<summary><b>beacon_api-098</b> Run KZG reconstruction off async and fork-choice threads — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** Call PeerDAS KZG and reconstruction functions in blocking tasks or async jobs off the caller, async runtime and single-threaded fork choice mutator. Do not spawn a new validation task per column for the same delayed block.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2457`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2457) gossip column verification in spawn_blocking_handle
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3811`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3811) reconstruction on rayon pool
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1166`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1166) canonical_head/fork choice not on async path (canonical_head.rs:787 spawn_blocking)

**Sources.** [teku#9728](https://github.com/Consensys-Incorporated/teku/pull/9728), [grandine@5d83807db](https://github.com/grandinetech/grandine/commit/5d83807db95f), [grandine@e53a535e1](https://github.com/grandinetech/grandine/commit/e53a535e114c)

</details>


<a id="beacon_api-099"></a>
<details>
<summary><b>beacon_api-099</b> Bound parallelism of per-blob cell recovery — <i>partial · low · S · cpu, memory</i></summary>

**Idea.** Run per-blob cell recovery on worker tasks with a bounded number in flight, zero-copy views of inputs and reused buffers, instead of spawning one task per blob. This limits peak memory and scheduling overhead.

**Gap in Lighthouse.** Parallelism is rayon-bounded by pool size, not one task per blob, so peak in-flight is limited. Missing: reused buffers and fully zero-copy inputs (cell_ids.to_vec(), cells.to_vec() per blob).

**Impact.** Small allocation savings during supernode reconstruction; negligible for non-supernodes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/kzg_utils.rs:889`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L889) reconstruct_data_columns uses into_par_iter over blobs (rayon, bounded by pool threads)
- beacon_node/crypto/kzg/src/lib.rs:307 recover_cells_and_compute_kzg_proofs takes cell refs but to_vec()s inputs

**Sources.** [nimbus#7758](https://github.com/status-im/nimbus-eth2/pull/7758), [nimbus#7800](https://github.com/status-im/nimbus-eth2/pull/7800), [prysm#14397](https://github.com/OffchainLabs/prysm/pull/14397)

</details>


<a id="beacon_api-100"></a>
<details>
<summary><b>beacon_api-100</b> Semi-supernode: custody half the columns — <i>implemented · medium · cpu, disk, bandwidth</i></summary>

**Idea.** Offer a mode that custodies and subscribes to 64 of 128 column subnets, enough to reconstruct all blobs, to serve blobs with about half the bandwidth and storage of a supernode.

**Best measured result.** Storage ~50% vs supernode (64 vs 128 columns) (pr:prysm#16029)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/src/cli.rs:63`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L63) --semi-supernode flag
- [`beacon_node/src/config.rs:130-134`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/config.rs#L130-L134) semi-supernode config
- [`beacon_node/beacon_chain/src/custody_context.rs:43`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L43) cgc override for semi-supernode

**Sources.** [prysm#16029](https://github.com/OffchainLabs/prysm/pull/16029), [grandine@5ff11c24d](https://github.com/grandinetech/grandine/commit/5ff11c24d141), [lodestar#8568](https://github.com/ChainSafe/lodestar/pull/8568)

</details>


<a id="beacon_api-101"></a>
<details>
<summary><b>beacon_api-101</b> Custody first half of columns to skip reconstruction — <i>not · low · L · cpu, bandwidth</i></summary>

**Idea.** Custody the first 64 columns, which hold the original blob data, so blobs can be served directly without reconstruction CPU cost.

**Gap in Lighthouse.** Custody columns are derived from node id per spec (random order list); not chosen as the first 64. Spec mandates derived custody, so a client cannot pick columns freely without breaking peer expectations.

**Impact.** Would avoid reconstruction CPU only for blob serving; spec-incompatible as a default, so low real value.

**Best measured result.** avoids reconstruction CPU load (pr:nimbus#7752)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/custody_context.rs:507`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L507) sampling_columns_for_epoch slices ordered_custody_column_indices
- [`beacon_node/beacon_chain/src/custody_context.rs:1233`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L1233) generate_data_column_indices_rand_order

**Sources.** [nimbus#7752](https://github.com/status-im/nimbus-eth2/pull/7752)

</details>


<a id="beacon_api-104"></a>
<details>
<summary><b>beacon_api-104</b> Share blobs and cells by Arc, not copy — <i>implemented · low · cpu, memory</i></summary>

**Idea.** Hold blobs, sidecars and partial-column cells behind Arc/shared references on the heap and pass them by reference to KZG and caches, so each clone does not copy 128 KiB.

**Impact.** Already cheap clones of sidecars.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/api_types.rs:161`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/api_types.rs#L161) Arc&lt;BlobSidecar&gt;/Arc&lt;DataColumnSidecar&gt; in responses
- [`beacon_node/lighthouse_network/src/types/pubsub.rs:29`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L29) Arc&lt;DataColumnSidecar&gt; gossip
- [`beacon_node/beacon_chain/src/kzg_utils.rs:889`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L889) Vec&lt;Arc&lt;DataColumnSidecar&gt;&gt;

**Sources.** [lighthouse#4593](https://github.com/sigp/lighthouse/pull/4593), [nimbus#9081](https://github.com/status-im/nimbus-eth2/pull/9081), [lighthouse#4980](https://github.com/sigp/lighthouse/pull/4980)

</details>


<a id="beacon_api-108"></a>
<details>
<summary><b>beacon_api-108</b> Cache columns with unknown parent block — <i>not · medium · M · latency, sync</i></summary>

**Idea.** Cache data column sidecars whose parent block is unknown and validate them when the parent arrives, instead of discarding and fetching them again.

**Gap in Lighthouse.** On ParentUnknown, keep the column sidecar in a bounded cache keyed by block root (or hand it to the child lookup as a real component) and re-run gossip/KZG verification once the parent imports, like the BlockRootUnknown reprocessing path; touches gossip_methods, SyncMessage::UnknownParentSidecarHeader/BlockComponent::Sidecar and the lookup download logic.

**Impact.** Avoids re-fetching columns by RPC after a parent lookup on the rare unknown-parent path; small bandwidth/latency gain, mainly after reorgs or missed blocks.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:764-776`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L764-L776) ParentUnknown column: only sends UnknownParentSidecarHeader, the sidecar is not kept
- [`beacon_node/network/src/sync/manager.rs:151-159`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L151-L159) UnknownParentSidecarHeader carries only header info, no sidecar
- [`beacon_node/network/src/sync/manager.rs:903-919`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L903-L919) handled as BlockComponent::Sidecar (no data)
- [`beacon_node/network/src/sync/block_lookups/single_block_lookup.rs:340-344`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/single_block_lookup.rs#L340-L344) Sidecar component inserts nothing; lookup re-downloads its columns itself
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:148`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L148) reprocessing queue only covers UnknownBlockDataColumn (block-root unknown), not parent unknown

**Second check.** Followed the sync path beyond gossip_methods: the sync message and the lookup's BlockComponent::Sidecar explicitly carry no data, and the lookup comment says it downloads the columns itself; the reprocessing queue only handles unknown block roots.

**Sources.** [silver#157](https://github.com/gattaca-com/silver/pull/157)

</details>


<a id="beacon_api-109"></a>
<details>
<summary><b>beacon_api-109</b> Index sidecar quarantine by root and slot — <i>implemented · low · cpu</i></summary>

**Idea.** Index the blob/column quarantine by block root and slot for O(1) lookups, and use one pop returning an Option instead of has-then-pop double access.

**Impact.** Lookups are O(1) by root with peek closures, no has-then-pop.

**Best measured result.** Stated: API calls go from O(n) to O(1) (pr:nimbus#7100)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:351`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L351) LruCache&lt;Hash256, PendingComponents&gt; keyed by block root
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:187`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L187) single peek returning Option for missing cells

**Sources.** [nimbus#7100](https://github.com/status-im/nimbus-eth2/pull/7100)

</details>


<a id="beacon_api-110"></a>
<details>
<summary><b>beacon_api-110</b> Cache custody column set per node — <i>implemented · low · cpu</i></summary>

**Idea.** Compute the custody and sampling column indices for the node id once, store them as a hash set (swapped atomically when custody count changes), and use it for O(1) membership checks.

**Impact.** Custody set computed once and sliced; no per-call derivation. Membership is a slice scan of a few columns, not a hash set, which is immaterial.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/custody_context.rs:507`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L507) sampling_columns_for_epoch returns slice of precomputed ordered list
- [`beacon_node/beacon_chain/src/custody_context.rs:525`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L525) custody_columns_for_epoch

**Sources.** [teku#10446](https://github.com/Consensys-Incorporated/teku/pull/10446), [prysm#14893](https://github.com/OffchainLabs/prysm/pull/14893), [nimbus#7210](https://github.com/status-im/nimbus-eth2/pull/7210)

</details>


<a id="beacon_api-111"></a>
<details>
<summary><b>beacon_api-111</b> Batch KZG verify sidecars from RPC and sync — <i>implemented · medium · cpu, latency, sync</i></summary>

**Idea.** Verify KZG proofs of all blob/column sidecars received by RPC or range sync for a block or batch together with batch KZG verification, instead of one by one.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker.rs:664`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L664) verify_kzg_for_data_column_list batches all columns of a block
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1122`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1122) batch verify via validate_full_data_columns
- [`beacon_node/beacon_chain/src/kzg_utils.rs:112`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L112) verify_cell_proof_batch
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:522`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L522) blob list batch

**Sources.** [prysm#13351](https://github.com/OffchainLabs/prysm/pull/13351), [lighthouse#4736](https://github.com/sigp/lighthouse/pull/4736)

</details>


<a id="beacon_api-112"></a>
<details>
<summary><b>beacon_api-112</b> Batch gossip column verification per block — <i>partial · medium · M · cpu, latency</i></summary>

**Idea.** Collect gossip data column sidecars of the same block header and verify their KZG cell proofs in one batch, with the inclusion proof and header signature verified once per batch.

**Gap in Lighthouse.** Header-once-per-block exists for partial-message columns (on by default), but full DataColumnSidecar gossip still re-checks inclusion proof and proposer signature per sidecar, and no path batches KZG cell proofs across columns of one block. Add a beacon_processor batch stage for gossip columns grouped by block root that calls verify_kzg_for_data_column_list once, with per-item fallback, and reuse a verified-header cache for full sidecars.

**Impact.** KZG batching across 8+ custody columns per block could cut gossip column job time several-fold (lodestar reports 3-4x, ~250ms); header dedupe gain is smaller since partial path already has it.

**Best measured result.** job time 3x-4x faster, saves ~250ms; ~35ms more wait time (pr:lodestar#7910)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/src/cli.rs:693-702`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L693-L702) --enable-partial-columns defaults to true
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2480-2511`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2480-L2511) verify_partial_data_column_header_for_gossip: header (inclusion proof + proposer signature) verified once per block root, later partials reuse cached header
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1316-1349`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1316-L1349) partial gossip path skips header checks when the assembler has a cached header
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1166-1192`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1166-L1192) full sidecar path KZG-verifies only cells missing from DA cache/assembler (missing_cells_for_column_sidecar), but still per-sidecar inclusion proof, signature and KZG
- [`beacon_node/beacon_processor/src/lib.rs:1311-1316`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1311-L1316) gossip_data_column_queue and gossip_partial_data_column_queue pop one item per job; no batching like GossipAttestationBatch

**Second check.** Earlier review missed the partial-columns path (default on) which caches the verified header per block root and skips header re-verification, and the missing-cells filter that avoids re-verifying known cells; KZG batching across columns is still absent.

**Sources.** [lodestar#7910](https://github.com/ChainSafe/lodestar/pull/7910)

</details>


<a id="beacon_api-113"></a>
<details>
<summary><b>beacon_api-113</b> Combine by-root sidecar requests per peer — <i>implemented · low · bandwidth, sync</i></summary>

**Idea.** Send one by-root RPC request per peer for all missing blobs or columns of a block (or several sampling requests), instead of one request per sidecar.

**Impact.** Requests batch multiple roots and indices per peer.

**Best measured result.** saves bandwidth (stated, no numbers) (pr:teku#8952)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context/requests/data_columns_by_root.rs:11`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/requests/data_columns_by_root.rs#L11) DataColumnsByRootRequestParams{block_roots, indices}
- [`beacon_node/network/src/sync/network_context.rs:904`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L904) data columns by root request

**Sources.** [teku#8952](https://github.com/Consensys-Incorporated/teku/pull/8952), [lighthouse#6256](https://github.com/sigp/lighthouse/pull/6256)

</details>


<a id="beacon_api-115"></a>
<details>
<summary><b>beacon_api-115</b> Request columns only from custody peers — <i>implemented · medium · bandwidth, sync</i></summary>

**Idea.** Send by-root column requests only to peers whose custody set contains the columns, filtered by the peer's custody mask.

**Impact.** Already only requests columns from peers whose custody set contains the column.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context/custody.rs:364`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L364) select_column_peer uses get_custodial_peers(column_index)
- [`beacon_node/network/src/sync/network_context.rs:419`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L419) get_custodial_peers -&gt; custody_peers_for_column
- [`beacon_node/network/src/sync/network_context.rs:592`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L592) by-range also filters is_custody_peer_of

**Sources.** [prysm#14452](https://github.com/OffchainLabs/prysm/pull/14452), [caplin#17392](https://github.com/erigontech/erigon/pull/17392)

</details>


<a id="beacon_api-116"></a>
<details>
<summary><b>beacon_api-116</b> Hedge slow column requests to alternate peers — <i>not · medium · M · latency, sync</i></summary>

**Idea.** After a delay, send a slow in-flight data column request again to another custody peer, bounded to a fraction of pending requests and two attempts per request.

**Gap in Lighthouse.** No duplicate/hedged request: a slow custody peer holds the column until the 10s RPC timeout or an error. Add a per-column hedge timer in ActiveCustodyRequest that re-issues the by-root request to another custody peer after a delay, capped by a fraction of pending requests and 2 attempts, first response wins.

**Impact.** Lower tail latency for lookups when one custody peer is slow; no gain in the common case.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context/custody.rs:241-271`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L241-L271) only requests columns in NotStarted state; one in-flight request per column
- [`beacon_node/network/src/sync/network_context/custody.rs:405-455`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L405-L455) ColumnRequest status NotStarted/Downloading/Downloaded with no hedge timer; retry only after on_download_error
- [`beacon_node/lighthouse_network/src/rpc/handler.rs:44`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L44) RESP_TIMEOUT 10s is the only slow-peer bound

**Second check.** Checked custody.rs request loop, ColumnRequest state machine, network_context and RPC handler timeouts for any duplicate/parallel or speculative re-request; none found.

**Sources.** [teku#11011](https://github.com/Consensys-Incorporated/teku/pull/11011)

</details>


<a id="beacon_api-119"></a>
<details>
<summary><b>beacon_api-119</b> Validate blob sidecars without state advancement — <i>implemented · medium · cpu, memory, latency</i></summary>

**Idea.** Do not run slot processing to get a state for blob sidecar validation. Use an existing state, or hold the sidecar until the block's state is ready.

**Impact.** Gossip sidecar validation does not advance state; it uses proposer cache and falls back to the parent's stored state (get_advanced_hot_state only reuses an already-cached state).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_column_verification.rs:1746`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1746) verify_proposer_and_signature uses with_proposer_cache keyed by shuffling root
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1759`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1759) only on miss loads a stored/cached state, no process_slots in the gossip path
- [`beacon_node/beacon_chain/src/blob_verification.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/blob_verification.rs) has no state use (blob sidecars no longer gossiped separately post-Fulu)

**Sources.** [grandine#192](https://github.com/grandinetech/grandine/pull/192), [grandine@f6d472f38](https://github.com/grandinetech/grandine/commit/f6d472f38b7f), [grandine#183](https://github.com/grandinetech/grandine/pull/183)

</details>


<a id="beacon_api-121"></a>
<details>
<summary><b>beacon_api-121</b> Prune blob and column data past DA window — <i>implemented · medium · disk</i></summary>

**Idea.** Delete blob/column sidecars older than the data availability retention window (and non-canonical ones at finalization), with storage keyed by slot so pruning can stream in order. This keeps disk use bounded.

**Impact.** DA-window pruning and non-canonical cleanup exist; only the slot-ordered key layout is missing, which is covered under the streaming idea.

**Best measured result.** 1.6TB in caplin dir on a Hoodi node (pr:caplin#20379)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3277`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3277) try_prune_blobs prunes blobs and columns older than DA boundary
- [`consensus/types/src/core/chain_spec.rs:941`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/core/chain_spec.rs#L941) min_epoch_data_availability_boundary
- [`beacon_node/beacon_chain/src/migrate.rs:780-786`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L780-L786) deletes blobs/columns of abandoned forks at finalization
- [`beacon_node/store/src/lib.rs:144`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/lib.rs#L144) keys are block_root+index, not slot (differs)

**Sources.** [lighthouse#3852](https://github.com/sigp/lighthouse/pull/3852), [caplin#20379](https://github.com/erigontech/erigon/pull/20379), [teku#6587](https://github.com/Consensys-Incorporated/teku/pull/6587)

</details>


<a id="beacon_api-122"></a>
<details>
<summary><b>beacon_api-122</b> Derive column retention window from chain config — <i>implemented · medium · disk</i></summary>

**Idea.** Compute the data column retention window as epochs times slots-per-epoch from the chain config, not a mainnet slot default, so chains with shorter epochs do not keep twice the data.

**Impact.** Retention is in epochs from the chain config, so shorter-epoch chains do not keep double.

**Best measured result.** gnosis retained 131072 slots against a 65536 window (2x) (pr:caplin#23610)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/core/chain_spec.rs:948`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/core/chain_spec.rs#L948) retention = current_epoch - min_epochs_for_data_column_sidecars_requests (epoch-based)
- [`consensus/types/src/core/chain_spec.rs:2409`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/core/chain_spec.rs#L2409) value configurable from the network config

**Sources.** [caplin#23610](https://github.com/erigontech/erigon/pull/23610)

</details>


<a id="beacon_api-124"></a>
<details>
<summary><b>beacon_api-124</b> Cheap filesystem traversal for blob pruning — <i>n/a · medium · cpu, disk</i></summary>

**Idea.** When pruning file-based blob storage, walk directories with the efficient directory-iteration syscall and cache root-to-slot lookups from earlier passes, instead of a stat or file read per blob.

**Impact.** Lighthouse stores sidecars in the key-value database, so there is no directory traversal or stat per blob.

**Best measured result.** The pruning routine appears to consume a ton of disk or syscall resources on some systems (pr:prysm#13425)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3277-3450`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3277-L3450) blobs/columns live in a KV DB (BeaconBlob/BeaconDataColumn), not files
- [`beacon_node/store/src/lib.rs:144`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/lib.rs#L144) get_data_column_key

**Sources.** [prysm#13425](https://github.com/OffchainLabs/prysm/pull/13425), [prysm#13410](https://github.com/OffchainLabs/prysm/pull/13410)

</details>


<a id="beacon_api-125"></a>
<details>
<summary><b>beacon_api-125</b> Incremental capped low-priority blob pruning — <i>partial · medium · S · cpu, disk, latency</i></summary>

**Idea.** Prune blobs often in small capped chunks on a low-priority single thread, reading keys only from the KV store, instead of deleting a whole epoch at once.

**Gap in Lighthouse.** Pruning is frequent (per epoch) and off the hot path, but uncapped per run: a lagging node deletes everything in one atomic batch, and existence checks read all 128 column keys per block instead of iterating existing keys. Add a max-blocks/keys cap per call and iterate stored keys from the KV store.

**Impact.** Avoids a large delete stall and many existence reads on lagging nodes; negligible at steady state.

**Best measured result.** Cap 32 per minute vs about 5 new sidecars per minute (pr:teku#6628)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3277-3330`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3277-L3330) try_prune_blobs runs after finalization on the migrator background thread, gated by epochs_per_blob_prune (default 1)
- [`beacon_node/store/src/hot_cold_store.rs:3359-3433`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3359-L3433) iterates all blocks back to the last pruned one with no per-run cap and key_exists on all column keys per block
- [`beacon_node/store/src/hot_cold_store.rs:3448-3454`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3448-L3454) all deletes applied in one do_atomically batch

**Second check.** Re-read the full try_prune_blobs body; confirmed no cap, single atomic delete batch, and per-index key_exists (the code comment itself suggests reading existing indices as a future refactor).

**Sources.** [teku#6628](https://github.com/Consensys-Incorporated/teku/pull/6628), [teku#6758](https://github.com/Consensys-Incorporated/teku/pull/6758)

</details>


<a id="beacon_api-131"></a>
<details>
<summary><b>beacon_api-131</b> Cache gossip-validated sidecars for import — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** Keep the blob/column sidecars already validated on gossip in a cache so fork choice import does not verify them again.

**Impact.** Already avoids re-verifying gossip-validated sidecars at import.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker.rs:394`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L394) put_gossip_verified_data_columns stores KzgVerified columns
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:483`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L483) put_kzg_verified_data_columns, merge_data_columns:176 keeps verified ones in PendingComponents
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:475`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L475) verify_kzg_for_available_block only used for RPC/range-supplied data

**Sources.** [teku#6636](https://github.com/Consensys-Incorporated/teku/pull/6636), [grandine@0e22c0ff9](https://github.com/grandinetech/grandine/commit/0e22c0ff9663)

</details>


<a id="beacon_api-132"></a>
<details>
<summary><b>beacon_api-132</b> Drop sidecars for already-imported blocks — <i>partial · low · S · cpu, memory, bandwidth</i></summary>

**Idea.** Ignore received blob sidecars (and do not request them) for blocks already imported into fork choice, and do not register historical sync data in the gossip blob pool, so no redundant verification or pool growth occurs.

**Gap in Lighthouse.** Gossip dedups by observed cache and by DA cache contents, but there is no early fork-choice 'already imported' ignore for full sidecars or RPC-sourced data; a late column for an imported block may still reach cache/verification until the observation path catches it. Add an is_block_data_imported check at the start of gossip column/blob verification and in lookup requests.

**Impact.** Saves occasional redundant KZG verification and cache entries; small.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_column_verification.rs:664`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L664) is_block_data_imported gate only for partial-column header caching
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1654`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1654) observation_key_is_known dedup
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1175`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1175) PriorKnownUnpublished via missing_cells_for_column_sidecar

**Sources.** [teku#7231](https://github.com/Consensys-Incorporated/teku/pull/7231), [grandine@f67342dc9](https://github.com/grandinetech/grandine/commit/f67342dc9f92), [grandine#140](https://github.com/grandinetech/grandine/pull/140)

</details>


<a id="beacon_api-133"></a>
<details>
<summary><b>beacon_api-133</b> Bound or fail fast on DA wait — <i>n/a · medium · latency, sync</i></summary>

**Idea.** During sync and payload envelope import, bound the data availability wait (for example one slot) or check availability synchronously and return an error so the batch is retried, instead of waiting indefinitely.

**Impact.** No blocking DA wait exists in Lighthouse: the cache is non-blocking and returns MissingComponents, so there is nothing to bound.

**Best measured result.** Fixed devnet sync dead-end at batch boundary (pr:prysm#16978)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:524`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L524) check_availability_and_cache_components returns MissingComponents immediately
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:676`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L676) range sync verifies coupled block+sidecars up front
- [`beacon_node/beacon_chain/src/payload_envelope_verification/import.rs:139`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/import.rs#L139) envelope import returns MissingComponents, no wait

**Sources.** [prysm#16991](https://github.com/OffchainLabs/prysm/pull/16991), [prysm#16978](https://github.com/OffchainLabs/prysm/pull/16978), [prysm#16993](https://github.com/OffchainLabs/prysm/pull/16993), [prysm#17152](https://github.com/OffchainLabs/prysm/pull/17152)

</details>


<a id="beacon_api-135"></a>
<details>
<summary><b>beacon_api-135</b> Run DA check concurrently with execution verification — <i>implemented · medium · S · latency</i></summary>

**Idea.** Run the data availability check concurrently with consensus verification and EL newPayload, in one cancel-on-failure group, not sequentially after them.

**Impact.** None left on the head path; range-sync envelopes (import.rs:420) arrive with columns already verified, and range sync is throughput-bound, not latency-bound.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/payload_envelope_verification/import.rs:89`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/import.rs#L89) envelope consensus verify + EL then check_envelope_availability_and_import:173 which is only a cache insert (put_executed_payload_envelope), never a blocking DA wait
- [`beacon_node/beacon_chain/src/pending_payload_cache/mod.rs:1`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/mod.rs#L1) Gloas DA cache: columns are KZG-verified on arrival against the block's bid, independently of the envelope; import fires when both sides are present
- [`beacon_node/beacon_chain/src/pending_payload_cache/mod.rs:321`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/mod.rs#L321) put_rpc_custody_columns / :352 put_gossip_verified_data_columns verify columns on their own path
- [`beacon_node/beacon_chain/src/payload_envelope_verification/execution_pending_envelope.rs:63`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/execution_pending_envelope.rs#L63) EL newPayload spawned as payload_verification_handle

**Second check.** The source PR (prysm#16899) is about the Gloas payload envelope; the earlier review checked the pre-Gloas range-sync block path. Lighthouse's Gloas pending_payload_cache already decouples column KZG verification from envelope execution and joins them at a cache, so the DA check never runs after the EL.

**Sources.** [prysm#16899](https://github.com/OffchainLabs/prysm/pull/16899)

</details>


<a id="beacon_api-138"></a>
<details>
<summary><b>beacon_api-138</b> Track received columns to skip duplicate work — <i>implemented · medium · cpu, disk, bandwidth</i></summary>

**Idea.** Track which data columns were received and stored per block, so a column from gossip and the same one recovered from EL is not processed, persisted or requested twice.

**Impact.** Avoids duplicate persist/publish/request of columns.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:176`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L176) merge_data_columns skips indices already cached
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:584`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L584) reconstruction re-checks cached indices before import/publish
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:642`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L642) dedupes EL-built columns against gossip-observed and DA-cached columns
- [`beacon_node/network/src/sync/network_context.rs:978`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L978) lookups request only columns not already cached

**Sources.** [prysm#14467](https://github.com/OffchainLabs/prysm/pull/14467), [teku#9409](https://github.com/Consensys-Incorporated/teku/pull/9409)

</details>


<a id="beacon_api-140"></a>
<details>
<summary><b>beacon_api-140</b> Delay RPC fetch of missing sidecars — <i>partial · medium · M · latency, bandwidth, sync</i></summary>

**Idea.** Delay RPC fetches of missing blobs/columns by a slot-time-based interval (about 0.5 to 1 s, capped by the attestation deadline), so gossip can deliver them first and redundant requests are avoided.

**Gap in Lighthouse.** RPC by-root fetch is deferred implicitly by waiting for attestation-carrying peers, not by an explicit slot-time timer (0.5-1 s capped by the attestation deadline). A block that nobody has attested yet gets no scheduled fetch.

**Impact.** Mostly avoids redundant RPC; small bandwidth saving, no CPU impact.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/manager.rs:1036`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L1036) handle_unknown_block_root waits for unknown_root_min_peers corroboration (record_unknown_root:1061)
- [`beacon_node/network/src/sync/block_lookups/mod.rs:66`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L66) LOOKUP_MAX_DURATION_NO_PEERS_SECS: lookups created from gossip components have no peers until attestations arrive, so RPC waits roughly until the attestation deadline
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1016`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1016) gossip column MissingComponents only triggers reconstruction check, no RPC

**Second check.** Also checked the beacon_processor reprocess queue and the lookup constants for an explicit RPC delay timer; the only slot-time-based timer found is for column reconstruction (work_reprocessing_queue.rs:107), not for RPC fetches.

**Sources.** [teku#10094](https://github.com/Consensys-Incorporated/teku/pull/10094), [teku#7026](https://github.com/Consensys-Incorporated/teku/pull/7026)

</details>


<a id="beacon_api-141"></a>
<details>
<summary><b>beacon_api-141</b> Request missing blobs immediately on block seen — <i>partial · medium · S · latency</i></summary>

**Idea.** When a gossip block arrives, enqueue a peer request for missing blobs at once instead of waiting for the availability wait to expire.

**Gap in Lighthouse.** On block arrival Lighthouse fetches the blob data from the EL at once and, only with --enable-partial-columns (off by default), requests the missing cells from gossip peers. It does not start a by-root RPC request for missing custody columns on block arrival.

**Impact.** Faster availability when the EL mempool lacks blobs and gossip is late; matters on poorly connected nodes, not CPU.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1934`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1934) process_gossip_verified_block calls spawn_fetch_block_columns as soon as the block is gossip-valid, before process_block
- [`beacon_node/network/src/network_beacon_processor/mod.rs:960`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L960) spawn_fetch_block_columns: engine getBlobs from the EL (fetch_engine_blobs_and_publish_full:998), then publish_partial_data_columns:1070 asks mesh peers for missing cells (request_cells bitmap)
- [`beacon_node/lighthouse_network/src/config.rs:383`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L383) enable_partial_columns defaults to false
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1972`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1972) MissingComponents does not start an RPC lookup

**Second check.** The earlier review missed spawn_fetch_block_columns, which runs on block arrival: an EL getBlobs fetch plus an optional partial-column cell request to peers. That covers the main goal of 'pull data as soon as the block is seen', but not through peer RPC.

**Sources.** [lodestar#6499](https://github.com/ChainSafe/lodestar/pull/6499)

</details>


<a id="beacon_api-142"></a>
<details>
<summary><b>beacon_api-142</b> Pull late block when blobs arrive first — <i>implemented · medium · latency</i></summary>

**Idea.** If blobs arrive on gossip but the block does not arrive by a cutoff, fetch the block and remaining blobs from peers instead of waiting.

**Impact.** Block is pulled from peers as soon as a sidecar arrives first (checked for columns, not for pre-Fulu blobs); gated by unknown_root_min_peers corroboration rather than a time cutoff.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:780`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L780) column with unknown block root sends UnknownBlockHashFromAttestation immediately, so a lookup fetches the block
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:803`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L803) column queued for reprocessing until block arrives

**Sources.** [lodestar#6534](https://github.com/ChainSafe/lodestar/pull/6534)

</details>


<a id="beacon_api-144"></a>
<details>
<summary><b>beacon_api-144</b> Fetch missing columns within the slot — <i>partial · medium · M · latency</i></summary>

**Idea.** Run the missing-column fetcher every second and request missing custody columns by root after a grace of half the time to the attestation deadline, instead of waiting a minute.

**Gap in Lighthouse.** No periodic scan of DA-cache blocks with missing custody columns that requests them by root after a grace; non-supernodes rely on attestation-triggered lookups. Add a slot-clock-driven fetch in the sync manager.

**Impact.** Shortens time-to-available for blocks missing a few custody columns; matters for head liveness, not CPU.

**Best measured result.** block stayed unavailable for over a minute before (pr:caplin#24830)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/manager.rs:1036`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L1036) by-root column fetch only via attestation/unknown-root lookups
- [`beacon_node/network/src/sync/network_context.rs:960`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L960) custody column request for non-cached indices
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:1139`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L1139) in-slot reconstruction timer (RECONSTRUCTION_DEADLINE 1/4 slot, :107) recovers columns for nodes holding &gt;=50%
- [`beacon_node/network/src/sync/block_lookups/mod.rs:779`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L779) drop_stuck_lookups only prunes

**Second check.** Also checked the reprocess queue: it has an in-slot reconstruction deadline timer, which helps supernodes but does not fetch by root; the on-arrival getBlobs fetch (beacon_api-141) also reduces the cases, but there is no periodic fetcher.

**Sources.** [caplin#24830](https://github.com/erigontech/erigon/pull/24830)

</details>


<a id="beacon_api-146"></a>
<details>
<summary><b>beacon_api-146</b> Disk-backed blob quarantine — <i>not · medium · M · memory, disk</i></summary>

**Idea.** Persist quarantined blob sidecars in a database table keyed by block root and index, deleted at finalization, so the quarantine does not hold them all in memory.

**Gap in Lighthouse.** Quarantined blobs and columns (PendingComponents) are memory only, bounded by LRU capacity and epoch pruning. The old disk overflow column (OverflowLRUCache) was deprecated and removed. To add it: a hot-DB column keyed by (block_root, index), written in put_kzg_verified_*, deleted on import or finalization.

**Impact.** Lowers peak RSS by the unimported sidecars held (tens to a few hundred MB in blob-heavy periods or sync), at the cost of disk writes. The LRU already bounds it, and Lighthouse removed a similar design before, so the gain is small.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:442`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L442) put_kzg_verified_blobs writes only to the in-memory critical LruCache
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:566`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L566) write_lock.entry(block_root) into the in-memory map, no store write
- [`beacon_node/store/src/lib.rs:374`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/lib.rs#L374),409 DBColumn::OverflowLRUCache = 33 marked DEPRECATED (the old disk overflow was removed)

**Second check.** Searched the store crate for a pending, quarantine or overflow column. Only the deprecated OverflowLRUCache DBColumn exists, which shows Lighthouse once had disk overflow and dropped it. Nothing current persists pending components.

**Sources.** [nimbus#7108](https://github.com/status-im/nimbus-eth2/pull/7108)

</details>


<a id="beacon_api-149"></a>
<details>
<summary><b>beacon_api-149</b> Drop sidecars with out-of-range index — <i>implemented · medium · cpu, memory</i></summary>

**Idea.** Track only blob sidecars whose index matches a commitment in the block, so the per-block tracker cannot grow without bound.

**Impact.** Nothing to gain; per-block trackers are already bounded.

**Evidence (Lighthouse @ 928b61e719).**

- beacon_chain/src/observed_data_sidecars.rs:192 sanitize_data_sidecar rejects index &gt;= max_num_of_items (max blobs / number_of_columns)
- beacon_chain/src/observed_data_sidecars.rs:152 observe_sidecar uses the sanitized set
- beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:162 merge_single_blob only stores if index &lt; block commitments and commitment matches
- overflow_lru_cache.rs:285 verified_blobs is a fixed vector of max_len; merge_data_columns:181 dedups by index

**Sources.** [teku#7616](https://github.com/Consensys-Incorporated/teku/pull/7616)

</details>


<a id="beacon_api-152"></a>
<details>
<summary><b>beacon_api-152</b> Keep DA entries until import completes — <i>implemented · medium · cpu, memory, disk, latency, bandwidth, sync</i></summary>

**Idea.** Do not remove a block's pending components or sampling tracker from the availability cache before fork choice import completes (evict by LRU/finality), and hold the cache write lock only for the insert. This prevents re-downloads and state re-computation.

**Impact.** Already avoids re-downloads and the insert-after-remove race.

**Evidence (Lighthouse @ 928b61e719).**

- beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:524-545 check_availability_and_cache_components never removes pending components; comment says only LRU eviction as finality advances
- overflow_lru_cache.rs:557-580 update_or_insert_pending_components takes write lock only for insert then downgrades to read
- data_availability_checker.rs:746 do_maintenance prunes by cutoff epoch

**Sources.** [lighthouse#5845](https://github.com/sigp/lighthouse/pull/5845), [lighthouse#7961](https://github.com/sigp/lighthouse/pull/7961), [teku#10219](https://github.com/Consensys-Incorporated/teku/pull/10219)

</details>


<a id="beacon_api-155"></a>
<details>
<summary><b>beacon_api-155</b> Import only when blob count equals commitments — <i>implemented · low · latency</i></summary>

**Idea.** Treat a block as complete only when the number of held blob sidecars exactly equals its KZG commitment count, so import is not triggered early and rejected.

**Impact.** Availability requires exact count match, errors on too many.

**Best measured result.** mitigates some stuttering in block updates when blobs arrived after blocks (pr:nimbus#5363)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:200`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L200) make_available compares received count to num_blobs_expected / expected columns
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:214`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L214) cmp of received vs expected

**Sources.** [nimbus#5363](https://github.com/status-im/nimbus-eth2/pull/5363)

</details>


<a id="beacon_api-156"></a>
<details>
<summary><b>beacon_api-156</b> Drop gossip columns outside sampling set — <i>implemented · high · cpu, disk, bandwidth</i></summary>

**Idea.** Drop incoming data column sidecars for columns that are not in the node's sampling set before KZG verification and storage.

**Impact.** Equivalent effect via topic subscription (1 column per subnet on mainnet); no explicit per-message check, so columns just after a custody change could slip through but cost is negligible.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/service.rs:792`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L792) subscribe_new_data_column_subnets(sampling_count) - only sampling subnets are subscribed so gossipsub never delivers other columns
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1155`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1155) verify_index_matches_subnet rejects columns on the wrong subnet before KZG (line 1180)
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1139`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1139) no explicit sampling-set check in validate_data_column_sidecar_for_gossip_fulu

**Sources.** [grandine#376](https://github.com/grandinetech/grandine/pull/376), [grandine@b970e9d91](https://github.com/grandinetech/grandine/commit/b970e9d91cbe)

</details>


<a id="beacon_api-157"></a>
<details>
<summary><b>beacon_api-157</b> Correct proposer cache key in blob verification — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** Look up the proposer for blob sidecar verification with the correct shuffling decision root, so the proposer cache hits mid-epoch instead of recomputing the shuffling.

**Impact.** Column path uses the correct decision root so mid-epoch lookups hit; blob gossip verification no longer exists.

**Evidence (Lighthouse @ 928b61e719).**

- beacon_chain/src/data_column_verification.rs:1743 proposer_shuffling_root_for_child_block(column_epoch) used as cache key
- data_column_verification.rs:1746 chain.with_proposer_cache keyed by that root
- beacon_chain/src/blob_verification.rs has no gossip path any more (only KZG helpers)

**Sources.** [lighthouse#4646](https://github.com/sigp/lighthouse/pull/4646)

</details>


<a id="beacon_api-159"></a>
<details>
<summary><b>beacon_api-159</b> High priority retry for delayed columns — <i>implemented · medium · latency</i></summary>

**Idea.** Retry delayed data column sidecars at high priority in the processing queue, since a block is waiting on them.

**Impact.** Delayed columns are retried ahead of attestation and other low-priority work, same effect.

**Evidence (Lighthouse @ 928b61e719).**

- beacon_processor/src/lib.rs:944-946 gossip_data_column_queue then unknown_block_data_column_queue popped right after gossip blocks, before attestations/aggregates
- beacon_processor/src/scheduler/work_reprocessing_queue.rs:1373 ReadyDataColumn releases queued columns when the block arrives
- beacon_processor/src/lib.rs:318-320 ReadyWork::DataColumn becomes Work::UnknownBlockDataColumn

**Sources.** [grandine@6997dfcff](https://github.com/grandinetech/grandine/commit/6997dfcff8be)

</details>


<a id="beacon_api-162"></a>
<details>
<summary><b>beacon_api-162</b> Skip gossip proof checks for EL-supplied blobs — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** When all blobs of a block come from the local EL, mark the block available and skip gossip KZG and inclusion proof verification, keeping a KZG check before persistence.

**Impact.** LH already skips KZG and inclusion-proof checks for EL-supplied blobs/columns (it skips KZG even before persistence, trusting the EL).

**Best measured result.** "doesn't call kzg proof verification and inclusion proof verification for 9 blobs per slot"; "faster block import (in happy cases)" (pr:nimbus#6913)

**Evidence (Lighthouse @ 928b61e719).**

- beacon_chain/src/fetch_blobs/mod.rs:704 EL-built columns wrapped with KzgVerifiedPartialDataColumn::from_execution_verified (no KZG, no inclusion proof)
- beacon_chain/src/data_column_verification.rs:434,492 from_execution_verified for gossip-published EL columns
- fetch_blobs/mod.rs:632-660 dedup against gossip-observed and DA-cached columns

**Sources.** [nimbus#6913](https://github.com/status-im/nimbus-eth2/pull/6913)

</details>


<a id="beacon_api-163"></a>
<details>
<summary><b>beacon_api-163</b> Cache column inclusion proof results — <i>partial · medium · S · cpu</i></summary>

**Idea.** Cache the result of the KZG commitments inclusion proof check per block (key: hash of proof inputs) so other column sidecars of the same block skip the merkle proof.

**Gap in Lighthouse.** There is a per-block verify-once cache of the header and inclusion proof, but only on the partial-columns path, which is opt-in (--enable-partial-columns, default off). Full DataColumnSidecar gossip still recomputes kzg_commitments.tree_hash_root() and the merkle proof for each column of the same block. The fix: in verify_column_inclusion_proof, compare against a cached verified (block_root, commitments_root, proof), or reuse the assembler header cache for full columns.

**Impact.** Saves a commitments tree-hash and a short merkle proof for each additional custody column per block. A few hundred microseconds to a few ms of CPU per slot. Small.

**Best measured result.** 'reduce redundant work' when verifying inclusion proofs; no numbers (pr:prysm#15217)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2488-2497`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2488-L2497) verify_partial_data_column_header_for_gossip returns the cached header from the partial assembler on an equality match, and skips the inclusion proof
- [`beacon_node/beacon_chain/src/data_column_verification.rs:647`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L647) verify_partial_column_header_inclusion_proof runs only for the first header per block, then assembler.init caches it (line 666)
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1331-1334`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1331-L1334) partial columns without a header reuse the cached verified header (new_from_cached)
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1160-1176`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1160-L1176) full columns already in the DA cache (from EL or partials) return PriorKnownUnpublished before verify_column_inclusion_proof
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1178`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1178) full gossip columns still call verify_column_inclusion_proof every time
- [`beacon_node/beacon_chain/src/chain_config.rs:184`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/chain_config.rs#L184) enable_partial_columns defaults to false

**Second check.** The earlier review missed the partial-column header cache (PartialDataColumnAssembler get_header/init). That cache does verify once per block and then checks equality, but only when partial columns are enabled. Full columns that are already known also skip the proof through missing_cells_for_column_sidecar.

**Sources.** [prysm#15217](https://github.com/OffchainLabs/prysm/pull/15217)

</details>


<a id="beacon_api-164"></a>
<details>
<summary><b>beacon_api-164</b> Late DA check with per-block sampling tracker — <i>implemented · medium · S · disk, latency, bandwidth</i></summary>

**Idea.** Track sampled columns per block in memory as they arrive by gossip, EL or RPC, fetch only the missing ones by RPC, and run the availability check as late as possible to give gossip and EL more time.

**Gap in Lighthouse.** Small refinement only: the cache snapshot is taken once, when custody_lookup_request builds the request. Columns that are already requested are not re-filtered if they then arrive by gossip or EL while the request is in flight.

**Impact.** Lighthouse already defers RPC to the latest useful point (attestation-driven, 3-peer corroboration) and fetches only the missing columns. Re-filtering in-flight requests would save only occasional duplicate DataColumnsByRoot downloads.

**Best measured result.** fewer RPC calls (no numbers) (pr:teku#10006)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1972-1978`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1972-L1978) a gossip block with MissingComponents only logs and does not start an RPC lookup, so gossip and EL get time to fill the columns
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:2880-2884`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L2880-L2884) an RPC lookup starts only later, from attestations (or columns, line 790) that reference a root that is not imported
- [`beacon_node/network/src/sync/manager.rs:1036-1056`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L1036-L1056) handle_unknown_block_root waits for corroboration from unknown_root_min_peers peers before it starts a lookup
- [`beacon_node/lighthouse_network/src/config.rs:25`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L25) DEFAULT_UNKNOWN_ROOT_MIN_PEERS = 3
- [`beacon_node/network/src/sync/network_context.rs:956-990`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L956-L990) custody_lookup_request fetches only the sampling columns not already in the DA cache
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:177`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L177) cached_data_column_indexes gives the per-block tracker fed by gossip, EL and RPC

**Second check.** Checked what starts RPC for a gossip block with missing components. Nothing does: the RPC fallback runs only from unknown-root events coming from attestations or columns, after corroboration from several peers. This is in effect Teku's late RPC/DA fallback. Eager availability checks on each arrival do not cause RPC, so they are not a gap.

**Sources.** [teku#10006](https://github.com/Consensys-Incorporated/teku/pull/10006)

</details>


<a id="beacon_api-165"></a>
<details>
<summary><b>beacon_api-165</b> Retry getBlobs until block columns are built — <i>partial · medium · S · latency, bandwidth</i></summary>

**Idea.** Poll engine_getBlobs again with short timeouts, triggered per gossip block, until the columns of a block without sidecars can be built from EL blobs.

**Gap in Lighthouse.** Lighthouse re-calls getBlobs once per distinct arrival event (partial header, gossip block, RPC lookup block, HTTP publish), so a block can get 2-3 independent attempts, but there is no timed re-poll after the last trigger misses. Add a bounded retry with short timeouts in fetch_engine_blobs_and_publish_full until the block is available or the slot cutoff passes.

**Impact.** Covers blobs that reach the EL mempool after the last trigger; builds more columns locally, saving download bandwidth and import latency. Probably modest gain because multiple event triggers already exist.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1123-1133`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1123-L1133) getBlobs triggered when a partial-column header is first seen
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1936`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1936) getBlobs triggered again (spawn_fetch_block_columns) when the gossip block is verified
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:211-222`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L211-L222) getBlobs triggered again for an RPC lookup block that is MissingComponents
- [`beacon_node/network/src/service.rs:692-702`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L692-L702) FetchBlockColumns for HTTP-published blocks
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:132-240`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L132-L240) no dedup/in-flight guard, no retry loop; miss returns Ok(None)
- [`beacon_node/execution_layer/src/engine_api/http.rs:74`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L74) ENGINE_GET_BLOBS_TIMEOUT 1s

**Second check.** Beyond the earlier review, found that getBlobs runs on several separate events (partial header and gossip block both, with no dedup), which is an event-driven re-attempt but not the timed polling the idea describes.

**Sources.** [nimbus#8012](https://github.com/status-im/nimbus-eth2/pull/8012), [nimbus#7445](https://github.com/status-im/nimbus-eth2/pull/7445)

</details>


<a id="beacon_api-L003"></a>
<details>
<summary><b>beacon_api-L003</b> pre-sized direct JSON encoding — <i>partial · low · S · cpu, latency, memory</i></summary>

**Idea.** For large JSON responses (blobs bundle), marshal directly into one pre-sized buffer with in-place hex encoding and write the already-encoded result verbatim through the RPC handler and codec, avoiding repeated reflection marshalling and compact re-scans of the payload.

**Gap in Lighthouse.** Rust serde is typed (no reflection), so the 10x reflection cost does not exist. Remaining: each blob is hex-encoded into two temporary Strings and the output Vec is not pre-sized. A hex-into-buffer serializer in ssz_types hex_fixed_vec plus a pre-sized body in blocking_json_task would remove it.

**Impact.** Blob/data-column JSON endpoints allocate ~2 extra copies per 128KB blob; small CPU saving on a rarely hit API, likely tens of percent on that call at most.

**Best measured result.** getBlobsV3 128 blobs: 309 ms -&gt; 29 ms (~10.6x); marshal 16,516 allocs -&gt; 1

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/task_spawner.rs:102`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/task_spawner.rs#L102) warp::reply::json -&gt; serde_json::to_vec, unsized growing Vec
- ~/.cargo ssz_types-0.14.1/src/serde_utils/hex_fixed_vec.rs:11 hex::encode builds String per blob
- ethereum_serde_utils-0.8.1/src/hex.rs:7-12 second String via '0x' prefix copy

**Sources.** [caplin#21606](https://github.com/erigontech/erigon/pull/21606)

</details>


<a id="beacon_api-L004"></a>
<details>
<summary><b>beacon_api-L004</b> publish head before state copy — <i>partial · medium · S · latency</i></summary>

**Idea.** Publish the selected fork-choice head (root, slot) atomically at selection time, before the state copy, and serve identity-only API endpoints from it, so public handlers need not wait ~750 ms for the memoized head state or trigger fork-choice work on a cache miss.

**Gap in Lighthouse.** API handlers never block on head computation (they read the previous CachedHead), but the new head root/slot is only published after the state load/advance and cache build. Publish (root, slot) atomically right after new_view is chosen in recompute_head_at_slot_internal and serve identity-only endpoints from it.

**Impact.** Removes lag of head root/header endpoints behind fork choice; small in steady state because the post-import state is normally a state-cache hit.

**Best measured result.** block/root endpoints lagged ~750 ms behind the selected head

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:1106-1160`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1106-L1160) new snapshot (get_full_block, get_advanced_hot_state, build_all_caches) built before cached_head write lock; only then is the new root visible
- [`beacon_node/http_api/src/block_id.rs:48-57`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L48-L57) BlockId::Head root reads canonical_head.head_and_execution_status() (old snapshot, no waiting)

**Second check.** Checked the BlockId::Head path and recompute_head: no early-published head identity exists; Lighthouse avoids the waiting half of the problem (handlers read the stale snapshot) but not the lag.

**Sources.** [caplin#23155](https://github.com/erigontech/erigon/pull/23155)

</details>


<a id="beacon_api-L010"></a>
<details>
<summary><b>beacon_api-L010</b> historic committee cache from randao — <i>implemented · medium · S · latency, cpu</i></summary>

**Idea.** Serve historic committee queries by building a committee cache for the requested past epoch directly from randao mixes in a recent state, instead of replaying to a state at that epoch.

**Impact.** Committee queries for historic epochs avoid state replay.

**Best measured result.** reconstruction usually upwards of 20s, sometimes minutes

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/beacon/states.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs):~640-690 committees endpoint builds CommitteeCache::initialized(state, epoch) from the given state's randao for old epochs
- [`beacon_node/http_api/src/caches.rs:22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/caches.rs#L22) HistoricalCommitteeCache LRU keyed by shuffling id

**Sources.** [lighthouse#3272](https://github.com/sigp/lighthouse/pull/3272)

</details>


<a id="beacon_api-L011"></a>
<details>
<summary><b>beacon_api-L011</b> pubkey cache lookup — <i>implemented · low · cpu, latency</i></summary>

**Idea.** Look up validators by pubkey through the state's pubkey-to-index cache instead of scanning the whole validator registry per query.

**Impact.** No further gain; already O(1) via validator_pubkey_cache.

**Best measured result.** queries by pubkey took 10ms+ from registry loop

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/validator/mod.rs:48-64`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L48-L64) pubkey_to_validator_index uses chain.validator_index (pubkey cache) and verifies against state
- [`beacon_node/http_api/src/beacon/states.rs:780`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L780) single validator lookup uses it
- [`beacon_node/http_api/src/validators.rs:24-47`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validators.rs#L24-L47) bulk path uses hash filter

**Sources.** [lighthouse#3559](https://github.com/sigp/lighthouse/pull/3559)

</details>


<a id="beacon_api-L016"></a>
<details>
<summary><b>beacon_api-L016</b> hashset id filter — <i>implemented · low · cpu, latency</i></summary>

**Idea.** Filter validators by requested ids/pubkeys using a HashSet lookup per state validator instead of scanning the input list per validator, turning O(n*m) into O(n).

**Impact.** Already O(n) over registry with O(1) set lookups.

**Best measured result.** 2s to 12+s with 8k IDs before (slowdown); fix removes it

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/validators.rs:24-27`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validators.rs#L24-L27) ids_filter_set HashSet&lt;&amp;ValidatorId&gt;
- [`beacon_node/http_api/src/validators.rs:41-45`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validators.rs#L41-L45) per-validator contains() on pubkey/index
- validators.rs:95-99,143-146 same for balances and POST

**Sources.** [lighthouse#5468](https://github.com/sigp/lighthouse/pull/5468)

</details>


<a id="beacon_api-L017"></a>
<details>
<summary><b>beacon_api-L017</b> persist light client bootstrap — <i>implemented · medium · S · cpu, disk</i></summary>

**Idea.** Persist light client bootstrap parts (sync committee branch by block root, sync committee by period) so bootstrap is served without expensive computation or state queries.

**Impact.** Bootstrap is served from persisted sync committee branch/committee.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/light_client_server_cache.rs:396`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_server_cache.rs#L396) get_light_client_bootstrap reads stored branch and sync committee
- [`beacon_node/beacon_chain/src/beacon_chain.rs:8374`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L8374) bootstrap served without state load
- [`beacon_node/store/src/hot_cold_store.rs:831`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L831) light client update storage

**Sources.** [lighthouse#5915](https://github.com/sigp/lighthouse/pull/5915)

</details>


<a id="beacon_api-L018"></a>
<details>
<summary><b>beacon_api-L018</b> single lock acquisition — <i>implemented · low · latency</i></summary>

**Idea.** Read all needed fields from the canonical head under one lock acquisition instead of locking twice, to cut lock contention in the syncing endpoint.

**Impact.** Already a single head read; nothing to gain.

**Best measured result.** "responses were taking 4-10s on occasion"

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:589-598`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L589-L598) head_and_execution_status takes cached_head once plus one fork choice read lock
- [`beacon_node/http_api/src/lib.rs:2452-2455`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L2452-L2455) /node/syncing uses it

**Sources.** [lighthouse#6202](https://github.com/sigp/lighthouse/pull/6202)

</details>


<a id="beacon_api-L020"></a>
<details>
<summary><b>beacon_api-L020</b> server-side supply computation — <i>not · low · S · bandwidth, cpu</i></summary>

**Idea.** Add a node-side endpoint that sums balances for a state, so clients do not download and parse 68MB of JSON validator balances.

**Gap in Lighthouse.** Add a non-standard route (e.g. GET /lighthouse/.../supply or beacon/states/{id}/total_balance) that sums state.balances() inside map_state_and_execution_optimistic_and_finalized and returns one number; also add it to eth2 client types.

**Impact.** Saves a ~68MB JSON download+parse per supply query for tooling/explorers; negligible for a validating node, only benefits API consumers.

**Best measured result.** avoids 68MB JSON download

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs), validators.rs, beacon/states.rs: grep for supply/total balance finds only validator_balances (returns full list)
- no supply endpoint in http_api/src

**Sources.** [lighthouse#7102](https://github.com/sigp/lighthouse/pull/7102)

</details>


<a id="beacon_api-L021"></a>
<details>
<summary><b>beacon_api-L021</b> not-while-syncing guard on duties — <i>implemented · medium · S · cpu, sync</i></summary>

**Idea.** Reject validator duty endpoints (e.g. proposer duties) while the node is far behind head, since computing duties requires advancing state over many slots and starves sync.

**Impact.** Proposer duties are rejected while far behind.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs:475-512`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L475-L512) not_while_syncing_filter rejects when SyncingFinalized/SyncingHead and head is beyond sync_tolerance_epochs
- [`beacon_node/http_api/src/validator/mod.rs:1403`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L1403) proposer duties route uses not_while_syncing_filter

**Sources.** [lighthouse#7962](https://github.com/sigp/lighthouse/pull/7962)

</details>


<a id="beacon_api-L023"></a>
<details>
<summary><b>beacon_api-L023</b> skip duties when stalled — <i>not · medium · S · cpu, latency</i></summary>

**Idea.** Skip proposer duty computation (expensive state advance) while sync is stalled, not only while syncing, to avoid overwhelming the work queue.

**Gap in Lighthouse.** Stalled state passes the filter, and the proposer duties handler has no own head-lag guard, so a far-behind stalled node still computes duties via state advance. Apply the head-slot-vs-tolerance check to the Stalled arm.

**Impact.** Avoids expensive state advances and api_request_p0 work-queue overflow on a stalled far-behind node; no steady-state effect.

**Best measured result.** avoids 'Work queue is full' api_request_p0 at 1024

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs:509`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L509) SyncState::Stalled =&gt; Ok(()) in not_while_syncing_filter
- [`beacon_node/http_api/src/lib.rs:2703-2706`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L2703-L2706) proposer duties route uses not_while_syncing_filter
- [`beacon_node/http_api/src/proposer_duties.rs:80-90`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/proposer_duties.rs#L80-L90) cache miss calls compute_and_cache_proposer_duties with no head-distance check
- [`beacon_node/network/src/sync/manager.rs:673`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L673) Stalled set when no advanced/synced peers

**Second check.** Also checked the proposer_duties handler itself for a head-distance or skip guard; none exists, so the earlier verdict stands.

**Sources.** [lighthouse#9538](https://github.com/sigp/lighthouse/pull/9538)

</details>


<a id="beacon_api-L024"></a>
<details>
<summary><b>beacon_api-L024</b> index lookup instead of full scan — <i>not · medium · S · cpu, latency</i></summary>

**Idea.** For validator/balance state endpoints with a requested validator set, resolve the ids to indices first and read those validators directly instead of scanning the whole registry and filtering.

**Gap in Lighthouse.** All three list endpoints scan the whole registry even for a few ids. Resolve ids to indices (index directly, pubkey via validator_pubkey_cache / state pubkey cache) and read validators().get(i)/balances().get(i); scan only when no ids (or status-only filter).

**Impact.** Subset requests drop from a full registry scan (~260 ms) to a few ms (6 ms for 100 vals per the PR).

**Best measured result.** validator_balances 100 vals: 260 ms to 6 ms; 10k: 260 to 23 ms; 100k: 320 to 110 ms

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/validators.rs:86-125`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validators.rs#L86-L125) balances endpoint scans validators().iter().zip(balances()) and filters by HashSet
- [`beacon_node/http_api/src/validators.rs:134-170`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validators.rs#L134-L170) identities endpoint does the same full scan
- [`beacon_node/http_api/src/validators.rs:9-75`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validators.rs#L9-L75) get_beacon_state_validators also full-scans with id filter

**Second check.** Read all of validators.rs including get_beacon_state_validators (not cited earlier): it uses the same full scan, so the verdict stands and the gap covers three endpoints.

**Sources.** [lighthouse#10037](https://github.com/sigp/lighthouse/pull/10037)

</details>


<a id="beacon_api-L025"></a>
<details>
<summary><b>beacon_api-L025</b> light client updates without state cache — <i>implemented · medium · S · memory</i></summary>

**Idea.** Generate light client updates only from the post-state at block import, kept as small proofs, without needing historical states in the state cache.

**Impact.** Updates are built from cached proofs, not state cache; state load only on a miss.

**Best measured result.** No numbers

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:4789`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4789) cache_state_data at import from the post-state
- [`beacon_node/beacon_chain/src/light_client_server_cache.rs:59`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_server_cache.rs#L59) stores proofs in prev_block_cache
- [`beacon_node/beacon_chain/src/light_client_server_cache.rs:271`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_server_cache.rs#L271) fallback loads state only on cache miss

**Sources.** [lodestar#3461](https://github.com/ChainSafe/lodestar/pull/3461)

</details>


<a id="beacon_api-L038"></a>
<details>
<summary><b>beacon_api-L038</b> guard old-slot reconstruction — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** In blob REST endpoints, return 404 immediately for post-Fulu slots older than the data-column availability window instead of entering the expensive column reconstruction path.

**Gap in Lighthouse.** Optional: add an explicit data-column-window check (slot &lt; earliest/retention floor -&gt; 404) before get_data_column_keys; today pruned slots exit via the key-count check with a 400 after a DB key scan.

**Impact.** Out-of-window blob requests already skip reconstruction because pruned columns make the key count too low; an explicit check would only save one key scan. Lodestar's spike came from reconstruction on its event loop; Lighthouse runs these on a blocking task.

**Best measured result.** ~407 getBlobs requests caused p99 event-loop lag spike to 18.1s

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/block_id.rs:501`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L501) get_data_columns_for_blob_reconstruction lists column keys first (cheap) and returns 400 if fewer than half are stored, before any KZG recovery
- [`beacon_node/http_api/src/block_id.rs:365`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L365) reconstruct only entered after that check

**Sources.** [lodestar#9536](https://github.com/ChainSafe/lodestar/pull/9536)

</details>


<a id="beacon_api-L039"></a>
<details>
<summary><b>beacon_api-L039</b> guard old-slot reconstruction — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** In blob REST endpoints, compute the data-column availability start as max(earliest available slot, retention floor) and return 404 early for older slots rather than attempting column reconstruction.

**Gap in Lighthouse.** Optional: add an explicit data-column-window check (slot &lt; earliest/retention floor -&gt; 404) before get_data_column_keys; today pruned slots exit via the key-count check with a 400 after a DB key scan.

**Impact.** Out-of-window blob requests already skip reconstruction because pruned columns make the key count too low; an explicit check would only save one key scan. Lodestar's spike came from reconstruction on its event loop; Lighthouse runs these on a blocking task.

**Best measured result.** ~407 getBlobs requests caused p99 event-loop lag spike to 18.1s

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/block_id.rs:501`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L501) get_data_columns_for_blob_reconstruction lists column keys first (cheap) and returns 400 if fewer than half are stored, before any KZG recovery
- [`beacon_node/http_api/src/block_id.rs:365`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L365) reconstruct only entered after that check

**Sources.** [lodestar#9537](https://github.com/ChainSafe/lodestar/pull/9537)

</details>


<a id="beacon_api-L040"></a>
<details>
<summary><b>beacon_api-L040</b> refuse regen API while syncing — <i>not · medium · S · cpu, latency, sync</i></summary>

**Idea.** Reject REST requests for arbitrary-slot or root states with 503 while the node is syncing (keep head/finalized/justified/genesis served), so expensive regen is never triggered from the API while behind.

**Gap in Lighthouse.** Add a sync check in StateId::state (or on the beacon/states and debug/beacon/states routes) for CoreStateId::Slot and Root, returning 503 not_synced as not_while_syncing_filter does; keep Head/Finalized/Justified/Genesis served.

**Impact.** Stops arbitrary-slot state loads (cold hdiff replay, hot cache churn) from competing with sync on a lagging node; matters only when tools hit the API during sync. The beacon processor already runs P1 API work below range-sync chain segments, so the gain is smaller than in Lodestar.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/state_id.rs:174`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L174) StateId::state calls chain.get_state(root, slot, true) with no sync check
- [`beacon_node/http_api/src/lib.rs:2148`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L2148) GET debug/beacon/states/{state_id} has no not_while_syncing_filter
- [`beacon_node/http_api/src/beacon/states.rs:46`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L46) beacon/states/* routes spawn Priority::P1 tasks with no sync gate
- [`beacon_node/beacon_processor/src/lib.rs:1149`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1149) P1 API requests are popped only after chain segments and gossip work (scheduling mitigation, not rejection)

**Sources.** [lodestar#9641](https://github.com/ChainSafe/lodestar/pull/9641)

</details>


<a id="beacon_api-L042"></a>
<details>
<summary><b>beacon_api-L042</b> pubkey index map — <i>implemented · low · cpu, latency</i></summary>

**Idea.** Resolve pubkeys to indices with a map built once per request instead of scanning the registry per requested pubkey.

**Impact.** Cost is O(registry) not O(ids*registry); already equivalent.

**Best measured result.** 400 ids vs 24k builders: ~6.3s to ~66ms

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/validators.rs:24-27`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validators.rs#L24-L27),41-45 requested ids put in a HashSet once, registry scanned once
- [`beacon_node/http_api/src/validator/mod.rs:48`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L48) pubkey cache for other id lookups

**Sources.** [lodestar#10408](https://github.com/ChainSafe/lodestar/pull/10408)

</details>


<a id="beacon_api-L043"></a>
<details>
<summary><b>beacon_api-L043</b> share historical state reconstruction — <i>partial · low · M · cpu, latency</i></summary>

**Idea.** Cache the serialized response of the last requested historical state and share in-flight reconstruction between concurrent readers, so multiple field reads of the same archived state reconstruct it once.

**Gap in Lighthouse.** A decoded-state cache exists so sequential reads reuse the state, but there is no in-flight dedup: concurrent cold requests for the same slot both miss and reconstruct (lock dropped before work). Add a per-slot single-flight map (Arc&lt;OnceCell&gt;/watch) in load_cold_state_by_slot.

**Impact.** Concurrent archive-state API queries (explorers, tooling) would reconstruct once instead of N times; reduces multi-second CPU/memory spikes on archive nodes, up to ~2.5x on cold triple reads.

**Best measured result.** cold read 5.93s with 3 reconstructions vs 2.18-2.33s with one

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2310-2319`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2310-L2319) historic_state_cache lock, released before reconstruction
- hot_cold_store.rs:2344,2375,2401 results put in historic_state_cache
- hot_cold_store.rs:87 Mutex&lt;HistoricStateCache&gt; caches states, not serialized responses

**Sources.** [lodestar#10458](https://github.com/ChainSafe/lodestar/pull/10458)

</details>


<a id="beacon_api-L045"></a>
<details>
<summary><b>beacon_api-L045</b> reuse state across history traversal — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** For historical state queries, reuse already replayed state across consecutive slot requests instead of replaying from a checkpoint each time.

**Impact.** Consecutive historical slot queries reuse the previous replayed state; hot states use the state cache.

**Best measured result.** getStateRoot 72.7 s -&gt; 6.7 s (up to 10x)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2306`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2306) load_cold_state_by_slot searches HistoricStateCache back through the replay range for the nearest cached prior state
- [`beacon_node/store/src/hot_cold_store.rs:2358`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2358) load_cold_state_by_slot_using_replay replays from that state and puts the result back into the cache (2401)
- [`beacon_node/store/src/historic_state_cache.rs:14`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/historic_state_cache.rs#L14) HistoricStateCache holds states and hdiff buffers

**Sources.** [nimbus#3219](https://github.com/status-im/nimbus-eth2/pull/3219)

</details>


<a id="beacon_api-L046"></a>
<details>
<summary><b>beacon_api-L046</b> stream JSON without temp strings — <i>partial · low · M · cpu, memory, latency</i></summary>

**Idea.** Stream JSON directly to the output instead of allocating temporary strings for hex arrays and numbers, which matters for huge state responses.

**Gap in Lighthouse.** Hash/root types already format on the stack. Quoted u64 (balances, slots, indices) uses format! per value and byte vectors build Strings. Replace with itoa::Buffer in quoted_int serialize (ethereum_serde_utils) and write hex via a stack/ chunked buffer; optionally stream large states.

**Impact.** JSON state/validators/balances responses (millions of integers) would allocate far fewer small Strings; maybe 20-40% off serialization CPU on huge responses, no change for SSZ clients.

**Best measured result.** 2-3x faster on state endpoint, 6-7s down to 2-3s

**Evidence (Lighthouse @ 928b61e719).**

- ethereum_serde_utils-0.8.1/src/quoted_int.rs:92 serialize_str(&amp;format!("{}", v)) allocates a String per u64
- ssz_types-0.14.1/src/serde_utils/hex_fixed_vec.rs:11 hex String temporaries
- alloy-primitives-1.7.3/src/bits/serde.rs:11-12 hashes use stack hex::Buffer (no heap)
- [`beacon_node/http_api/src/task_spawner.rs:102`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/task_spawner.rs#L102) warp::reply::json builds whole Vec in memory

**Sources.** [nimbus#7385](https://github.com/status-im/nimbus-eth2/pull/7385)

</details>


<a id="beacon_api-L050"></a>
<details>
<summary><b>beacon_api-L050</b> pubkey to index map — <i>partial · low · S · cpu, latency</i></summary>

**Idea.** Keep a pubkey to validator index map (persisted or in memory) instead of scanning the whole validator registry linearly for each pubkey lookup served via the API.

**Gap in Lighthouse.** Single-validator lookup uses the O(1) pubkey cache, but get_beacon_state_validators/_balances/_identities iterate every validator and test HashSet membership of ValidatorId::PublicKey. Resolve pubkey ids via chain.validator_index and index state.validators() directly when ids are given.

**Impact.** Queries by id on /validators, /validator_balances and /validator_identities (VC and staking-tool polling) would cost O(ids) not O(1.1M validators); saves tens of ms per request.

**Best measured result.** O(n) scan replaced by O(1) lookup

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:26`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L26) pubkey-&gt;index HashMap
- [`beacon_node/http_api/src/validator/mod.rs:48`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L48) pubkey_to_validator_index uses it
- [`beacon_node/http_api/src/validators.rs:43`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validators.rs#L43) list endpoints scan full registry per request

**Sources.** [prysm#1690](https://github.com/OffchainLabs/prysm/pull/1690)

</details>


<a id="beacon_api-L051"></a>
<details>
<summary><b>beacon_api-L051</b> per-slot committee cache for duties — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Cache the committee list per slot so duty/assignment API calls compute it once per slot instead of recomputing for every validator request.

**Impact.** Committees are computed once per epoch shuffling and reused; no per-validator recompute.

**Best measured result.** one calculation per slot instead of per RPC call

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/attester_duties.rs:143`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L143) committee cache built once per request then O(1) duty lookups
- [`beacon_node/http_api/src/beacon/states.rs:605-690`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L605-L690) committees endpoint uses HistoricalCommitteeCache and state committee cache

**Sources.** [prysm#2151](https://github.com/OffchainLabs/prysm/pull/2151)

</details>


<a id="beacon_api-L054"></a>
<details>
<summary><b>beacon_api-L054</b> single pass committee map — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Iterate committees once and store them in a map for archival assignment lookup instead of per-validator scans.

**Impact.** Committees are built once per shuffling and cached; lookups are map reads.

**Best measured result.** stated lower response times

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/caches.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/caches.rs) HistoricalCommitteeCache
- [`beacon_node/http_api/src/beacon/states.rs:636`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L636) cache lookup keyed by shuffling id
- [`beacon_node/http_api/src/attester_duties.rs:140`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L140) get_attestation_duties via committee cache

**Sources.** [prysm#4480](https://github.com/OffchainLabs/prysm/pull/4480)

</details>


<a id="beacon_api-L055"></a>
<details>
<summary><b>beacon_api-L055</b> skip needless slot advance — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** For attestation-data requests, only advance the head state through empty slots when the requested slot is in a later epoch than the state, since only the epoch-boundary root is needed.

**Impact.** Attestation data does no slot advance in the common case and only a partial advance at an epoch boundary.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2010`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2010) produce_unaggregated_attestation reads justified checkpoint and committee len straight from the head state when head epoch == request epoch (2125)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2208`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2208) partial_state_advance only if state.current_epoch() &lt; request_epoch
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2093`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2093) target root taken from head block roots without advancing

**Sources.** [prysm#4501](https://github.com/OffchainLabs/prysm/pull/4501)

</details>


<a id="beacon_api-L056"></a>
<details>
<summary><b>beacon_api-L056</b> paginate before compute; custom marshal — <i>n/a · low · S · cpu, memory, latency</i></summary>

**Idea.** For paginated validator-balance queries compute only the requested page rather than all balances then slicing; use a hand-written fixed-layout marshal for balances in the archive instead of generic SSZ.

**Gap in Lighthouse.** Beacon API has no pagination for validator balances (that was a Prysm gRPC feature), and Lighthouse has no archive that stores balances as hand-marshalled blobs; balances live in milhouse lists.

**Impact.** None.

**Best measured result.** 62207 to 10719 ns/op, 1012 to 109 allocs; archive 28187 to 8016 ns/op

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/validators.rs:86`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validators.rs#L86) balances endpoint has no pagination, filters by ids

**Sources.** [prysm#4530](https://github.com/OffchainLabs/prysm/pull/4530)

</details>


<a id="beacon_api-L060"></a>
<details>
<summary><b>beacon_api-L060</b> group by block root — <i>n/a · medium · cpu, latency</i></summary>

**Idea.** In the indexed-attestations endpoint, group attestations by beacon block root so each state or committee set is loaded once per group instead of per attestation.

**Impact.** Lighthouse has no indexed-attestations HTTP endpoint (a Prysm-specific API), so there is nothing to batch.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs:1284`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L1284),1931 only the standard attestations routes; grep for indexed_attestation in http_api finds only publish paths

**Sources.** [prysm#5441](https://github.com/OffchainLabs/prysm/pull/5441)

</details>


<a id="beacon_api-L062"></a>
<details>
<summary><b>beacon_api-L062</b> use target-root state — <i>n/a · medium · cpu, latency</i></summary>

**Idea.** When converting attestations to indexed form for an API, use the shuffling/state at the target checkpoint instead of the attested block root, so the state does not have to be regenerated by replaying slots for every distinct block root.

**Impact.** No API endpoint converts attestations to indexed form; the gossip path already uses the shuffling cache keyed by decision block rather than replaying a state per block root.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:7593`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7593) with_committee_cache resolves shuffling by (block root, epoch) via the shuffling cache keyed by decision root
- [`beacon_node/http_api/src/lib.rs:1284`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L1284) no indexed-attestations endpoint

**Sources.** [prysm#5548](https://github.com/OffchainLabs/prysm/pull/5548)

</details>


<a id="beacon_api-L064"></a>
<details>
<summary><b>beacon_api-L064</b> state regen by target root — <i>implemented · low · S · latency, cpu</i></summary>

**Idea.** When streaming indexed attestations, regenerate state keyed by the attestation target root rather than by epoch number, so committee lookup is near instant for real-time conversion.

**Impact.** Committee lookup for attestations is already by shuffling decision root, near instant; Lighthouse's SSE does not stream indexed attestations.

**Best measured result.** realtime conversion near instant

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:1350`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1350) indexed attestation built from shuffling cache
- [`beacon_node/beacon_chain/src/shuffling_cache.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs) keyed by AttestationShufflingId (epoch + decision root)

**Sources.** [prysm#5971](https://github.com/OffchainLabs/prysm/pull/5971)

</details>


<a id="beacon_api-L069"></a>
<details>
<summary><b>beacon_api-L069</b> head getters without state copy — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Provide head getters for validator index and pubkey that read from the head state without copying it.

**Impact.** Head lookups avoid state copies already.

**Best measured result.** Says cheap, no state copy

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:1628`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1628) validator_index via pubkey cache, no state
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1666`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1666) validator_pubkey/validator_pubkey_bytes
- [`beacon_node/http_api/src/state_id.rs:218`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L218) head path borrows head snapshot without copying

**Sources.** [prysm#9303](https://github.com/OffchainLabs/prysm/pull/9303)

</details>


<a id="beacon_api-L071"></a>
<details>
<summary><b>beacon_api-L071</b> skip replay for future slot — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** Reject API requests for a state at a slot beyond the head before attempting state replay, avoiding useless slot processing.

**Impact.** Future-slot state requests are rejected before replay.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:967`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L967) state_root_at_slot returns None (404) when request_slot &gt; wall-clock slot
- [`beacon_node/http_api/src/state_id.rs:104`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L104) StateId::root maps that None to not_found before any state load
- [`beacon_node/beacon_chain/src/beacon_chain.rs:986`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L986) slots between head and clock resolve to the head state root, no replay

**Sources.** [prysm#10915](https://github.com/OffchainLabs/prysm/pull/10915)

</details>


<a id="beacon_api-L073"></a>
<details>
<summary><b>beacon_api-L073</b> skip unchanged DB write — <i>implemented · low · S · disk</i></summary>

**Idea.** On proposer-preparation calls, read the stored fee recipient and write to the DB only when it changed, avoiding a DB write per validator per epoch.

**Impact.** Lighthouse never writes proposer preparation to the DB; it is an in-memory map pruned by epoch, so the per-validator DB write does not exist.

**Best measured result.** Benchmark: 10000 validators 11.7ms/op; 1000 validators 1.0ms/op (shows read check is cheap)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/lib.rs:816`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L816) update_proposer_preparation keeps in-memory map, entry.update(new) only counts changes
- [`beacon_node/http_api/src/validator/mod.rs:1015`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L1015) prepare_beacon_proposer

**Sources.** [prysm#11295](https://github.com/OffchainLabs/prysm/pull/11295)

</details>


<a id="beacon_api-L076"></a>
<details>
<summary><b>beacon_api-L076</b> head state with next-slot cache — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** For duties of the current and next epoch, use the head state with the next-slot cache instead of advancing a state by slots, avoiding an epoch transition on each request.

**Impact.** Already avoids epoch transitions in normal operation; only requests for epoch &lt; current-1 replay state.

**Best measured result.** avoids epoch transition in all calls during normal operation

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/attester_duties.rs:50`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L50) current/next epoch go to cached_attestation_duties
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1747`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1747) validator_attestation_duties uses with_committee_cache (shuffling cache, no state advance)
- [`beacon_node/http_api/src/proposer_duties.rs:135`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/proposer_duties.rs#L135) try_proposer_duties_from_cache reads cached head and proposer cache; state_advance_timer.rs pre-advances head

**Sources.** [prysm#12940](https://github.com/OffchainLabs/prysm/pull/12940)

</details>


<a id="beacon_api-L078"></a>
<details>
<summary><b>beacon_api-L078</b> use next slot cache in rewards — <i>partial · medium · S · latency</i></summary>

**Idea.** Use the cached next-slot pre-advanced state for the block rewards/value API rather than replaying and processing the epoch transition on demand.

**Gap in Lighthouse.** Only the standalone rewards endpoints replay. In get_state_before_applying_block, try chain.store.get_advanced_hot_state(block.parent_root(), block.slot(), parent_block.state_root()) first (it returns the state-cache entry pre-advanced by the state advance timer, or advances it itself), falling back to the replay.

**Impact.** Block-production value (the Prysm PR's main case) is already fast. Remaining gain: /eth/v1/beacon/rewards/blocks and sync_committee rewards for recent epoch-boundary blocks drop from hundreds of ms to tens of ms; explorer/staking-pool traffic only.

**Best measured result.** ~500ms down to ~20ms for slot-0 blocks

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_production/mod.rs:83-91`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L83-L91) block production loads the head state pre-advanced to the proposal slot via store.get_advanced_hot_state (filled by the state advance timer)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:6537-6540`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6537-L6540) consensus_block_value is computed with compute_beacon_block_reward on that already-advanced production state, so /eth/v3/validator/blocks (the Prysm PR's motivating 500ms-&gt;20ms case) never replays the epoch transition
- [`beacon_node/http_api/src/sync_committee_rewards.rs:48-76`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/sync_committee_rewards.rs#L48-L76) get_state_before_applying_block (used by /eth/v1/beacon/rewards/blocks and sync_committee rewards) still loads the parent state and runs BlockReplayer.apply_blocks(vec![], Some(block.slot())), doing the epoch transition on demand
- [`beacon_node/http_api/src/standard_block_rewards.rs:18-21`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/standard_block_rewards.rs#L18-L21)

**Second check.** The earlier review looked only at the http_api rewards path; the produce-block path (block_production/mod.rs, beacon_chain.rs:6537) already computes the block value on the state-advance-timer state, which is exactly what Prysm#13684 targeted.

**Sources.** [prysm#13684](https://github.com/OffchainLabs/prysm/pull/13684)

</details>


<a id="beacon_api-L079"></a>
<details>
<summary><b>beacon_api-L079</b> read-only validator views — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** In the validators API, iterate read-only validator views instead of copying the full validator list from the state, avoiding copies.

**Impact.** Head-state validators query copies nothing but the returned rows. Non-head states are still loaded from the DB/cache.

**Best measured result.** speeds up fetching all validators ~3x

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/state_id.rs:218`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L218) head state borrowed, not copied
- [`beacon_node/http_api/src/validators.rs:39`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validators.rs#L39) iterates state.validators().iter() read-only; clones only matched Validator for output

**Sources.** [prysm#13873](https://github.com/OffchainLabs/prysm/pull/13873)

</details>


<a id="beacon_api-L080"></a>
<details>
<summary><b>beacon_api-L080</b> precompute and store updates — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** Serve light client updates by range from precomputed updates stored in the DB instead of computing them per request, since the computation is heavy.

**Impact.** Updates are precomputed on block import and persisted; requests only read and decode them.

**Best measured result.** computing them is described as a very heavy process

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/light_client_server_cache.rs:179-205`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_server_cache.rs#L179-L205) computes the update once per block and stores the best per period via store_light_client_update
- [`beacon_node/store/src/hot_cold_store.rs:855-890`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L855-L890) get_light_client_updates reads stored SSZ by period range from DBColumn::LightClientUpdate
- [`beacon_node/http_api/src/light_client.rs:29`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/light_client.rs#L29) serves from the store

**Sources.** [prysm#14531](https://github.com/OffchainLabs/prysm/pull/14531)

</details>


<a id="beacon_api-L082"></a>
<details>
<summary><b>beacon_api-L082</b> gzip HTTP responses — <i>partial · medium · S · bandwidth</i></summary>

**Idea.** Honor Accept-Encoding gzip in the HTTP API server and compress large responses such as states, cutting bytes transferred.

**Gap in Lighthouse.** The main beacon API is already served through axum (lib.rs:3701), so adding axum_utils::CompressionLayer (tower-http, already a dependency) on axum_router would honour Accept-Encoding for all routes; restrict to large bodies via a predicate (e.g. SizeAbove) and keep SSE streams uncompressed.

**Impact.** Cuts egress bytes for large JSON responses (states, validators, light client updates) by ~5-10x for remote clients; costs node CPU, so a bandwidth saving.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_metrics/src/lib.rs:120`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_metrics/src/lib.rs#L120) .layer(CompressionLayer::new()) on the metrics server only
- [`validator_client/http_metrics/src/lib.rs:128`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/http_metrics/src/lib.rs#L128) same for VC metrics
- [`beacon_node/http_api/src/lib.rs:3693-3705`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L3693-L3705) main API: warp routes wrapped in axum Router::new().fallback_service(warp::service(routes)) with no layers added
- Cargo.toml:276 warp built with default-features=false, features=["server"] (no compression feature)

**Second check.** Checked the axum server builder (common/axum_utils/src/server) and the http_api router assembly: no compression layer; the axum wrapper makes the fix a one-line layer, smaller than the earlier gap suggested.

**Sources.** [prysm#14982](https://github.com/OffchainLabs/prysm/pull/14982)

</details>


<a id="beacon_api-L086"></a>
<details>
<summary><b>beacon_api-L086</b> reverse index for duties lookup — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** For large duty requests, build a validator-index to committee-assignment reverse map once per epoch and look up in O(1), instead of scanning slots x committees x members per validator. Keep linear scan for small requests (under ~3000).

**Gap in Lighthouse.** Residual only: the committee scan (&lt;=2048 O(1) range computations per validator) could become a division, and Gloas compute_ptc_duties (beacon_chain.rs:1768 TODO) is still O(N * slots * PTC).

**Impact.** Attester duties already avoid the slots x committees x members scan Prysm removed; the residual linear committee loop costs microseconds per validator.

**Best measured result.** 30000 validators 8.7s to 0.8s; 91% faster at 30k, 67% at 5k

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/committee_cache.rs:31`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L31) shuffling_positions: Vec&lt;NonZeroUsizeOption&gt;, a validator-index -&gt; shuffled-position reverse map
- [`consensus/types/src/state/committee_cache.rs:155-166`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L155-L166) built once when the per-epoch CommitteeCache is initialised
- [`consensus/types/src/state/committee_cache.rs:392`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L392) shuffled_position is an O(1) lookup
- [`consensus/types/src/state/committee_cache.rs:294-325`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L294-L325) get_attestation_duties: O(1) position lookup then only O(committee_count) arithmetic range checks, never scans committee members
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1745-1758`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1745-L1758) duties served from the shared per-epoch shuffling cache via with_committee_cache

**Second check.** The earlier review saw the committee loop but missed that shuffling_positions is precisely the per-epoch reverse index the idea asks for, cached with the CommitteeCache; the member scan Prysm eliminated does not exist in Lighthouse.

**Sources.** [prysm#15558](https://github.com/OffchainLabs/prysm/pull/15558)

</details>


<a id="beacon_api-L089"></a>
<details>
<summary><b>beacon_api-L089</b> per-request committee assignment, early exit — <i>implemented · medium · cpu, memory</i></summary>

**Idea.** For the duties endpoint, compute committee assignments only for the requested validator indices, exiting early once all are found, instead of precomputing every committee and building a per-validator map for the whole set.

**Impact.** No whole-set precompute or per-validator map is built; work is proportional to requested indices.

**Best measured result.** 100k validators: 12.6ms/11.8KB vs 16.7ms/7.9MB for 10 indices; 1.2-1.3x faster, 14-670x less memory

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:1752-1758`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1752-L1758) duties computed only for requested indices via cached committee cache
- [`consensus/types/src/state/committee_cache.rs:295`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L295) get_attestation_duties early-returns on first matching committee and uses shuffled_position O(1)
- [`beacon_node/http_api/src/attester_duties.rs:158`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L158) historic path also per requested index

**Sources.** [prysm#15784](https://github.com/OffchainLabs/prysm/pull/15784)

</details>


<a id="beacon_api-L090"></a>
<details>
<summary><b>beacon_api-L090</b> skip KZG proof computation on blob reconstruct — <i>not · medium · M · cpu, memory, latency</i></summary>

**Idea.** For the get-blobs API, rebuild blobs from stored data columns without computing KZG cell proofs, since the response needs only blob data.

**Gap in Lighthouse.** Two cheaper paths are missing: (1) the extension is systematic, so if columns 0..number_of_columns/2 are all held the blob is just their concatenation (the check at kzg_utils.rs:797 tests len &lt; number_of_columns instead of whether the first half is present); (2) otherwise recover cells only via ekzg-erasure-codes recover_polynomial_coefficient (or an upstream rust_eth_kzg recover_cells API) and skip the proof computation.

**Impact.** get_blobs / blob_sidecars on non-supernodes holding &gt;=50% columns: per-blob latency drops by orders of magnitude since proof computation dominates; irrelevant for supernodes holding all columns and off the consensus path.

**Best measured result.** 1 blob: 13,506x faster, 90.4% less memory; 6 blobs: 2,921x faster

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/kzg_utils.rs:797-811`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L797-L811) when fewer than all columns are present, calls kzg.recover_cells_and_compute_kzg_proofs and discards the proofs
- [`beacon_node/beacon_chain/src/kzg_utils.rs:812-817`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L812-L817) skip only when all columns are present (concatenate first half cells)
- [`crypto/kzg/src/lib.rs:307-318`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/kzg/src/lib.rs#L307-L318) wrapper exposes only the with-proofs recovery
- rust_eth_kzg-0.9.1/src/prover.rs:156 recover_cells_and_kzg_proofs is the only public recovery API; ekzg-erasure-codes-0.9.1/src/reed_solomon.rs:179 recover_polynomial_coefficient is the cells-only primitive

**Second check.** Checked rust_eth_kzg 0.9.1 and ekzg-* 0.9.1 public APIs and the full-columns shortcut in reconstruct_blobs_with_indices; only the all-columns case avoids proof computation.

**Sources.** [prysm#15902](https://github.com/OffchainLabs/prysm/pull/15902)

</details>


<a id="beacon_api-L091"></a>
<details>
<summary><b>beacon_api-L091</b> lower gzip level — <i>not · medium · S · cpu</i></summary>

**Idea.** Compress large API responses (e.g. validators list) at the fastest gzip level instead of the default level 6, since compression dominated the CPU profile.

**Gap in Lighthouse.** Depends on L082. When adding CompressionLayer to the HTTP API axum router, set .quality(CompressionLevel::Fastest); optionally the same for the metrics servers.

**Impact.** Only relevant after gzip is added to the API; avoids compression dominating CPU on large validator-list responses.

**Best measured result.** gzip was almost 40% of CPU profile on GetValidators

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs:3701`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L3701) main API has no compression layer, so no level to tune
- [`beacon_node/http_metrics/src/lib.rs:120`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_metrics/src/lib.rs#L120) CompressionLayer::new() uses tower-http's default level (no .quality(CompressionLevel::Fastest))
- [`validator_client/http_metrics/src/lib.rs:128`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/http_metrics/src/lib.rs#L128) same

**Second check.** Grepped the whole tree for CompressionLevel/quality: no level is configured anywhere.

**Sources.** [prysm#16399](https://github.com/OffchainLabs/prysm/pull/16399)

</details>


<a id="beacon_api-L092"></a>
<details>
<summary><b>beacon_api-L092</b> reject unavailable historical state early — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** Return 404 for state requests older than the earliest available or backfill low slot instead of replaying from genesis, avoiding minutes of useless state replay on the API.

**Impact.** Already avoids replaying from genesis for unavailable historical states.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:971-975`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L971-L975) state_root_at_slot returns None when slot is between historic lower and upper limits
- [`beacon_node/http_api/src/state_id.rs:105-109`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L105-L109) None becomes custom_not_found 404 before any state load

**Sources.** [prysm#16615](https://github.com/OffchainLabs/prysm/pull/16615)

</details>


<a id="beacon_api-L094"></a>
<details>
<summary><b>beacon_api-L094</b> lazy filtered validator iteration — <i>implemented · medium · S · memory, cpu, latency</i></summary>

**Idea.** Iterate validators lazily with a filter (iterator/yield) in validator-listing and counting endpoints instead of materializing the whole validator set before filtering, avoiding millions of allocations per request.

**Gap in Lighthouse.** Only residual: id filtering scans all validators instead of indexing by id; minor.

**Impact.** Matches only are materialised; no whole-set allocation before filtering.

**Best measured result.** status=withdrawal_possible: ~2.3M validators materialized -&gt; 1442

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/validators.rs:34-75`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validators.rs#L34-L75) lazy iter().zip().enumerate().filter().filter_map() collecting only matches
- validators.rs:86-125 balances endpoint the same

**Sources.** [prysm#16838](https://github.com/OffchainLabs/prysm/pull/16838)

</details>


<a id="beacon_api-L103"></a>
<details>
<summary><b>beacon_api-L103</b> shared serialized event bytes — <i>not · low · S · memory, cpu</i></summary>

**Idea.** Serialize SSE events once into a single byte buffer shared by all subscribers instead of encoding a string to bytes per subscriber.

**Gap in Lighthouse.** Serialize the EventKind once in ServerSentEventHandler::register and broadcast an Arc&lt;str&gt;/Bytes (or Arc&lt;EventKind&gt; plus cached JSON), then build the warp Event from the cached string in the http_api events handler instead of calling json_data per subscriber.

**Impact.** Saves N-1 JSON serializations per event when several SSE subscribers share a topic. Negligible on a typical node with 1-3 subscribers; only matters for heavy topics like attestations or blob/column sidecars with many subscribers.

**Best measured result.** Single byte[] stored and reused for every subscriber

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs:3436-3441`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L3436-L3441) per-subscriber BroadcastStream map calls Event::default().event(..).json_data(data), serializing on every subscriber
- [`beacon_node/beacon_chain/src/events.rs:10-36`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/events.rs#L10-L36) broadcast channels carry typed EventKind&lt;E&gt;, not pre-serialized bytes
- [`beacon_node/beacon_chain/src/events.rs:102`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/events.rs#L102) register() sends the EventKind object

**Sources.** [teku#5492](https://github.com/Consensys-Incorporated/teku/pull/5492)

</details>


<a id="beacon_api-L104"></a>
<details>
<summary><b>beacon_api-L104</b> stream JSON response — <i>not · medium · M · memory</i></summary>

**Idea.** Stream JSON API responses straight into the HTTP output stream instead of building the full body in memory; large responses (validators list is 181MB of JSON) otherwise spike heap.

**Gap in Lighthouse.** Stream large JSON list responses (validators, balances) with an incremental serializer into a chunked body instead of Vec + warp::reply::json.

**Impact.** Removes a transient heap spike of hundreds of MB on full validator-list calls; no effect on normal duty paths.

**Best measured result.** Get state validators is 181Mb of JSON

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/task_spawner.rs:97-104`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/task_spawner.rs#L97-L104) blocking_json_task serialises the whole value with warp::reply::json into one in-memory body
- [`beacon_node/http_api/src/lib.rs:3701`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L3701) warp routes served through axum fallback_service; no streamed body anywhere in http_api or warp_utils (only stream use is SSE events at lib.rs:3480)

**Second check.** Grepped http_api, warp_utils and eth2 for Body::wrap_stream/from_stream/StreamBody/chunked; the only stream is the SSE events endpoint.

**Sources.** [teku#5525](https://github.com/Consensys-Incorporated/teku/pull/5525)

</details>


<a id="beacon_api-L105"></a>
<details>
<summary><b>beacon_api-L105</b> stream SSZ response — <i>not · medium · M · memory</i></summary>

**Idea.** Write SSZ response content incrementally to the output stream rather than materialising the full SSZ bytes first.

**Gap in Lighthouse.** Encode large SSZ responses (debug/beacon/states, finalized state) incrementally to a chunked body instead of as_ssz_bytes.

**Impact.** Saves one state-sized (~250MB+ mainnet) buffer per state download; checkpoint-sync server side only.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs:2180`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L2180) debug state SSZ path calls state.as_ssz_bytes() into a full Vec before building the response
- no streaming body in [`beacon_node/http_api/src`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src) or [`common/warp_utils/src`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/warp_utils/src)

**Second check.** Checked for any SSZ streaming encoder or chunked body in http_api, warp_utils and the response helpers; none.

**Sources.** [teku#5530](https://github.com/Consensys-Incorporated/teku/pull/5530)

</details>


<a id="beacon_api-L106"></a>
<details>
<summary><b>beacon_api-L106</b> reject future-slot state lookup — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** Return not-found immediately when a state is requested for a slot beyond the head, avoiding processing empty slots to produce a state.

**Gap in Lighthouse.** Slot check uses wall-clock slot, not head slot; slots between head and wall clock resolve to head state root instead of advancing, which is cheap.

**Impact.** Future-slot requests already rejected without state processing.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:967-969`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L967-L969) request_slot &gt; self.slot() returns None
- state_id.rs:105-109 turns that into 404

**Sources.** [teku#5533](https://github.com/Consensys-Incorporated/teku/pull/5533)

</details>


<a id="beacon_api-L109"></a>
<details>
<summary><b>beacon_api-L109</b> gzip REST responses — <i>not · medium · S · bandwidth</i></summary>

**Idea.** Enable gzip content encoding on REST responses and request gzip when downloading the initial state, shrinking transfer size.

**Gap in Lighthouse.** Add .layer(CompressionLayer::new()) to the axum_router in http_api serve, and enable reqwest gzip in the eth2 client for checkpoint-sync downloads.

**Impact.** Cuts transfer size of checkpoint-sync state and big JSON responses; bandwidth only, small CPU cost.

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.toml:220 workspace reqwest features have no gzip; Cargo.lock reqwest 0.12.28/0.13.5 entries pull no async-compression
- [`beacon_node/http_api/src/lib.rs:3701-3705`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L3701-L3705) beacon API now wrapped in an axum Router but no CompressionLayer is applied
- [`beacon_node/http_metrics/src/lib.rs:120`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_metrics/src/lib.rs#L120) CompressionLayer only on the metrics server
- [`common/axum_utils/src/lib.rs:7`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/axum_utils/src/lib.rs#L7) CompressionLayer re-export exists

**Second check.** Found the beacon API is now served via axum (lib.rs:3701), so the existing CompressionLayer makes the server side a one-line change, but it is not applied; no crate enables reqwest gzip via feature unification.

**Sources.** [teku#7457](https://github.com/Consensys-Incorporated/teku/pull/7457)

</details>


<a id="beacon_api-L110"></a>
<details>
<summary><b>beacon_api-L110</b> head state for duties — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** Compute attester duties from the head state when requested epoch is current or next, avoiding cache misses and state regeneration.

**Impact.** Hot path uses head/shuffling cache, no state regeneration.

**Best measured result.** JMH showed good speed, no numbers

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/attester_duties.rs:43-50`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L43-L50) current/next epoch go to cached_attestation_duties
- attester_duties.rs:70-83 uses canonical head node via chain.validator_attestation_duties (shuffling cache/head)
- attester_duties.rs:98-120 head state reused for historic epochs when possible

**Sources.** [teku#7573](https://github.com/Consensys-Incorporated/teku/pull/7573)

</details>


<a id="beacon_api-L115"></a>
<details>
<summary><b>beacon_api-L115</b> on-demand sidecar fetch for blobs — <i>not · medium · L · bandwidth, disk</i></summary>

**Idea.** Let the get-blobs API fetch missing column sidecars from peers on demand and persist them, so nodes without full custody can serve blobs and later calls skip the network.

**Gap in Lighthouse.** When stored columns are below half, request missing columns by root from peers via the network service, persist them, then reconstruct.

**Impact.** Lets non-supernodes serve the blobs API; functionality gain that adds network load.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/block_id.rs:340-470`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L340-L470) blob endpoints read only stored columns then reconstruct
- [`beacon_node/http_api/src/block_id.rs:501-520`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L501-L520) returns 'Insufficient data columns ... run with --supernode or --semi-supernode' instead of fetching from peers
- no DataColumnsByRoot/network sender use in [`beacon_node/http_api/src`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src)

**Second check.** Searched http_api for any by-root network request or sync handle in the blob paths; only local store reads and a semi-supernode hint exist.

**Sources.** [teku#10234](https://github.com/Consensys-Incorporated/teku/pull/10234)

</details>


