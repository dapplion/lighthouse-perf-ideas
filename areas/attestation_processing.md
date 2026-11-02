# attestation_processing

130 ideas: 18 not, 22 partial, 66 implemented, 24 n/a; 17 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [attestation_processing-001](#attestation_processing-001) | Use cached committees for attesting indices | implemented | medium | S | cpu, latency |
| [attestation_processing-002](#attestation_processing-002) | Shuffling cache keyed by epoch and dependent root | partial | low | M | cpu, memory, latency |
| [attestation_processing-003](#attestation_processing-003) | Compute committee length without building committee | implemented | low | S | cpu |
| [attestation_processing-004](#attestation_processing-004) | Cache committees-per-slot in epoch context | implemented | low | S | cpu |
| [attestation_processing-005](#attestation_processing-005) | Carry committee sizes on validated attestation | not | low | S | cpu |
| [attestation_processing-006](#attestation_processing-006) **★** | Same-message signature check for equal-data attestations | not | high | M | cpu, latency |
| [attestation_processing-007](#attestation_processing-007) **★** | Validate same-data attestations as one group | partial | medium | M | cpu, latency |
| [attestation_processing-008](#attestation_processing-008) **★** | Aggregate attestations in pool before fork choice | not | medium | M | cpu, latency |
| [attestation_processing-009](#attestation_processing-009) **★** | Batch-verify API-submitted attestations | not | medium | S | cpu |
| [attestation_processing-010](#attestation_processing-010) | Batch gossip attestation signature verification | implemented | high | S | cpu |
| [attestation_processing-011](#attestation_processing-011) **★** | Batch-verify reprocessed pending attestations | partial | medium | M | cpu, latency |
| [attestation_processing-012](#attestation_processing-012) | Amortise locks over attestation batches | partial | low | M | cpu |
| [attestation_processing-013](#attestation_processing-013) | Compute block attestations' target state once | implemented | medium | S | cpu, memory, disk |
| [attestation_processing-014](#attestation_processing-014) | Merge passes over block attestations | not | low | S | cpu |
| [attestation_processing-015](#attestation_processing-015) | Aggregate only the current slot's signatures | n/a | low | S | cpu, latency |
| [attestation_processing-016](#attestation_processing-016) | Per-aggregator subnet windows for child proof selection | n/a | low | S | cpu |
| [attestation_processing-017](#attestation_processing-017) | Always-running aggregation worker | n/a | low | S | cpu, latency |
| [attestation_processing-018](#attestation_processing-018) | Throttle aggregation before own proposal | n/a | low |  | cpu, latency |
| [attestation_processing-019](#attestation_processing-019) | Limit aggregation jobs to two child proofs | n/a | low |  | cpu, latency |
| [attestation_processing-020](#attestation_processing-020) | Run attestation aggregation at fixed slot offsets | n/a | low |  | cpu, latency |
| [attestation_processing-021](#attestation_processing-021) **★** | Process attestations and update head once per slot | partial | medium | S | cpu |
| [attestation_processing-022](#attestation_processing-022) | Verify aggregates before unaggregated attestations | implemented | medium | S | cpu, latency |
| [attestation_processing-023](#attestation_processing-023) | Prioritise attestations in processing loop; fast uint64 | implemented | low | S | cpu, latency |
| [attestation_processing-024](#attestation_processing-024) **★** | Keep gossip aggregates out of fork choice | not | medium | S | cpu |
| [attestation_processing-025](#attestation_processing-025) | Field-wise attestation data equality | not | low | S | cpu, memory |
| [attestation_processing-026](#attestation_processing-026) **★** | Allocation-free attesting indices computation | partial | medium | S | cpu, memory |
| [attestation_processing-027](#attestation_processing-027) | Iterate only set bits of aggregation bitfield | not | low | S | cpu, memory |
| [attestation_processing-028](#attestation_processing-028) | Avoid sorting attesting indices | not | low | S | cpu, memory |
| [attestation_processing-029](#attestation_processing-029) | Attesting indices as plain vector, not set | partial | low | S | cpu, memory |
| [attestation_processing-030](#attestation_processing-030) | Borrow matching committee instead of cloning all | partial | low | S | cpu, memory |
| [attestation_processing-031](#attestation_processing-031) | Verify single attestations in native form | implemented | medium | S | cpu, latency |
| [attestation_processing-032](#attestation_processing-032) | Convert attestations on worker, not async thread | implemented | medium | S | cpu, latency |
| [attestation_processing-033](#attestation_processing-033) | Check pool attestations by reference | implemented | low | S | cpu, memory |
| [attestation_processing-034](#attestation_processing-034) | Avoid implicit state copy in attestation production | n/a | low |  | cpu, memory |
| [attestation_processing-035](#attestation_processing-035) **★** | Verify signatures without building indexed attestation | partial | medium | M | cpu, memory |
| [attestation_processing-036](#attestation_processing-036) | Keep pending attestations tree-backed | n/a | low | S | cpu |
| [attestation_processing-037](#attestation_processing-037) **★** | Fetch target checkpoint state asynchronously | partial | medium | M | latency, cpu |
| [attestation_processing-038](#attestation_processing-038) | Cache checkpoint states by target checkpoint | implemented | medium | S | cpu, disk, latency |
| [attestation_processing-039](#attestation_processing-039) | Validate attestations on head state when shuffling matches | implemented | medium | S | cpu, memory, latency |
| [attestation_processing-040](#attestation_processing-040) | On shuffling miss, use epoch-boundary target state | implemented | medium | S | cpu, latency |
| [attestation_processing-041](#attestation_processing-041) | Build committee cache right after advancing state | implemented | low | S | cpu, latency |
| [attestation_processing-042](#attestation_processing-042) | Reject finalized or old-target attestations before state load | implemented | high | S | cpu, latency, disk, memory |
| [attestation_processing-043](#attestation_processing-043) | Drop attestations older than previous epoch early | implemented | medium | S | cpu, memory, bandwidth |
| [attestation_processing-044](#attestation_processing-044) | Reject far-future target epochs by clock | implemented | medium | S | cpu, latency |
| [attestation_processing-045](#attestation_processing-045) | Check target block in fork choice before work | implemented | medium | S | cpu |
| [attestation_processing-046](#attestation_processing-046) | Early return on source checkpoint mismatch | implemented | low | S | cpu |
| [attestation_processing-047](#attestation_processing-047) | Cheap rejection when attestation queues overflow | partial | low | S | cpu, disk, latency |
| [attestation_processing-048](#attestation_processing-048) | Bounded pending set instead of task per attestation | n/a | low | S | cpu, memory |
| [attestation_processing-049](#attestation_processing-049) | Size attestation queues for many-validator bursts | implemented | low | S | cpu, memory, latency |
| [attestation_processing-050](#attestation_processing-050) | Drop expired attestations from reprocess queue | implemented | low | S | cpu, latency |
| [attestation_processing-051](#attestation_processing-051) | Remove failed attestations from pending queue | n/a | low | S | cpu |
| [attestation_processing-052](#attestation_processing-052) | Deduplicate pending aggregates in queue | partial | low | S | cpu, latency |
| [attestation_processing-053](#attestation_processing-053) **★** | Park unknown-root attestations from raw bytes | not | medium | M | cpu, latency |
| [attestation_processing-054](#attestation_processing-054) | Queue unknown-block attestations, release on block import | implemented | medium | S | cpu, latency, bandwidth |
| [attestation_processing-055](#attestation_processing-055) | Per-slot attestation data cache for API | partial | low | S | cpu, latency |
| [attestation_processing-056](#attestation_processing-056) | Cache new head's attestation data before import finishes | implemented | low | S | latency |
| [attestation_processing-057](#attestation_processing-057) | Serve attestation data from state cache, not locked cache | implemented | low | S | latency, cpu |
| [attestation_processing-058](#attestation_processing-058) | Cache attestation committee schedule per epoch | implemented | low | S | cpu |
| [attestation_processing-059](#attestation_processing-059) | Reuse attester index from validation in op pool | partial | low | S | cpu |
| [attestation_processing-060](#attestation_processing-060) **★** | Subtract absent keys from committee aggregate pubkey | not | medium | M | cpu |
| [attestation_processing-061](#attestation_processing-061) | Separate worker for batched attestation verification | implemented | low | S | cpu, latency |
| [attestation_processing-062](#attestation_processing-062) | Compute cache misses outside the lock | implemented | low | S | cpu, latency |
| [attestation_processing-063](#attestation_processing-063) | Remove tracing spans from per-attestation hot paths | implemented | low | S | cpu, latency |
| [attestation_processing-064](#attestation_processing-064) | Skip re-validating own produced attestations | n/a | low | S | cpu, latency |
| [attestation_processing-065](#attestation_processing-065) | Attest as soon as the head block is processed | implemented | medium | S | latency, bandwidth |
| [attestation_processing-066](#attestation_processing-066) | Produce payload attestations on envelope receipt | implemented | low | S | latency |
| [attestation_processing-067](#attestation_processing-067) | Gossip own attestations before fork-choice validity | implemented | low | S | latency |
| [attestation_processing-068](#attestation_processing-068) | FFG/LMD consistency check from fork choice | implemented | low | S | cpu, disk, latency |
| [attestation_processing-069](#attestation_processing-069) | Bound ancestry walks with canonical slot index | n/a | low | S | cpu, latency, disk |
| [attestation_processing-070](#attestation_processing-070) | Use cached state of attested block root for validation | implemented | medium | S | cpu, memory |
| [attestation_processing-071](#attestation_processing-071) | Validate attestations against a few shared states | implemented | medium | S | cpu, memory |
| [attestation_processing-072](#attestation_processing-072) | Use the block's own state for its included attestations | implemented | low | S | cpu, memory |
| [attestation_processing-073](#attestation_processing-073) | Skip state roots when advancing state for shuffling | implemented | low | S | cpu, latency |
| [attestation_processing-074](#attestation_processing-074) | Reuse fetched fork-choice block for committee lookup | not | low | S | cpu, latency |
| [attestation_processing-075](#attestation_processing-075) | Dedupe concurrent same-target checkpoint state computations | implemented | medium | S | cpu, memory, latency |
| [attestation_processing-076](#attestation_processing-076) **★** | Bound attestation pre-state regeneration concurrency | partial | medium | S | cpu, memory |
| [attestation_processing-077](#attestation_processing-077) | Avoid coarse locks around attestation state work | implemented | low | S | cpu, latency |
| [attestation_processing-078](#attestation_processing-078) | Incremental per-block vote tally cache | n/a | low |  | cpu |
| [attestation_processing-079](#attestation_processing-079) | Cache attesting indices per attestation | implemented | low | S | cpu, memory |
| [attestation_processing-080](#attestation_processing-080) | Carry indexed attestation through deferral queues | implemented | low | S | cpu |
| [attestation_processing-081](#attestation_processing-081) | Compute attesting indices once per block attestation | implemented | low | S | cpu |
| [attestation_processing-082](#attestation_processing-082) | Pass precomputed committee into attesting-indices derivation | implemented | low | S | cpu |
| [attestation_processing-083](#attestation_processing-083) | Precompute attesting indices before voted block imports | partial | low | M | cpu, latency |
| [attestation_processing-084](#attestation_processing-084) | Lightweight non-SSZ indexed attestation on hot paths | n/a | low | S | cpu, memory |
| [attestation_processing-085](#attestation_processing-085) | Inline stack storage for aggregation bitfields | implemented | low | S | cpu, memory |
| [attestation_processing-086](#attestation_processing-086) | Bitset for validator index sets | partial | low | S | cpu, memory |
| [attestation_processing-087](#attestation_processing-087) | Size attesting-indices output by set bits | partial | low | S | memory |
| [attestation_processing-088](#attestation_processing-088) | Linear-pass sorted/unique check for indexed attestations | implemented | low | S | cpu |
| [attestation_processing-089](#attestation_processing-089) | Fuse index check with pubkey fetch, preallocate | partial | low | S | cpu, memory |
| [attestation_processing-090](#attestation_processing-090) **★** | Lazy BLS signature decompression for gossip attestations | not | medium | M | cpu |
| [attestation_processing-091](#attestation_processing-091) | Skip aggregates whose bits are a subset of seen | implemented | medium | S | cpu, bandwidth |
| [attestation_processing-092](#attestation_processing-092) | Longer post-block wait before attesting | n/a | low | S | latency |
| [attestation_processing-093](#attestation_processing-093) | Use pre-advanced current-slot state for attestation checks | implemented | medium | S | cpu, latency |
| [attestation_processing-094](#attestation_processing-094) | Compare checkpoint in place without copying | implemented | low | S | cpu, memory |
| [attestation_processing-095](#attestation_processing-095) | Offload signature aggregation to worker with deadline | n/a | low | L | cpu, latency |
| [attestation_processing-096](#attestation_processing-096) | Start aggregation early at 2/3 signatures | n/a | low | L | latency |
| [attestation_processing-097](#attestation_processing-097) | Prioritise aggregation jobs by block packing value | n/a | low | L | cpu, latency |
| [attestation_processing-098](#attestation_processing-098) | Skip aggregation jobs for single signatures | n/a | low | S | cpu |
| [attestation_processing-099](#attestation_processing-099) | Skip aggregation with no validators or when syncing | implemented | low | S | cpu |
| [attestation_processing-100](#attestation_processing-100) | Only process unaggregated attestations for duty subnets | implemented | low | S | cpu, memory |
| [attestation_processing-101](#attestation_processing-101) | Parallel gossip attestation validation before fork choice | implemented | low | S | cpu, latency |
| [attestation_processing-102](#attestation_processing-102) | Parallel verification of block attestations | implemented | medium | S | cpu, latency |
| [attestation_processing-103](#attestation_processing-103) | Async reprocessing of HTTP attestations with unknown head | implemented | low | S | latency |
| [attestation_processing-104](#attestation_processing-104) | Release queued attestations for recently imported roots | not | low | S | latency |
| [attestation_processing-105](#attestation_processing-105) **★** | Verify deferred attestations before queuing them | not | medium | M | cpu, memory |
| [attestation_processing-106](#attestation_processing-106) | Skip re-verifying gossip-verified attestation signatures | implemented | medium | S | cpu |
| [attestation_processing-107](#attestation_processing-107) | Skip signature check on already-verified pool/block attestations | implemented | low | S | cpu |
| [attestation_processing-108](#attestation_processing-108) | Verify unaggregated attestations once on pool entry | implemented | low | S | cpu |
| [attestation_processing-109](#attestation_processing-109) | Slasher detection per attestation, not per validator | implemented | low | S | cpu, disk |
| [attestation_processing-110](#attestation_processing-110) | Plain sha256 for is_aggregator check | implemented | low | S | cpu |
| [attestation_processing-111](#attestation_processing-111) | Refuse attestation production for slots before head | implemented | low | S | memory, disk |
| [attestation_processing-112](#attestation_processing-112) **★** | Reject attestations with heads many skipped slots behind | partial | medium | S | cpu, memory |
| [attestation_processing-113](#attestation_processing-113) | Check head descends from target before loading target | implemented | medium | S | cpu, disk |
| [attestation_processing-114](#attestation_processing-114) | Drop old-target attestations not on any known chain | implemented | medium | S | cpu, memory |
| [attestation_processing-115](#attestation_processing-115) | Cheap checks before fork-head ancestor walks | n/a | low |  | cpu |
| [attestation_processing-116](#attestation_processing-116) | Skip fork choice lookup for head-targeting attestations | not | low | S | cpu, latency |
| [attestation_processing-117](#attestation_processing-117) | Running counter for pending attestation cap | implemented | low | S | cpu, latency |
| [attestation_processing-118](#attestation_processing-118) | Separate queues and limits for aggregates vs singles | partial | low | M | cpu, latency |
| [attestation_processing-119](#attestation_processing-119) | Shorter attestation retention in caches | implemented | low | S | memory |
| [attestation_processing-120](#attestation_processing-120) | Skip finalized-block attestations in fork choice import | not | low | S | cpu, sync |
| [attestation_processing-121](#attestation_processing-121) | Fast-path single-bit merges and skip subgroup check | n/a | low | S | cpu, latency |
| [attestation_processing-122](#attestation_processing-122) | Skip redundant clone of attestation pre-state | n/a | low |  | cpu, memory |
| [attestation_processing-123](#attestation_processing-123) **★** | Trigger-based batching of gossip attestation BLS verification | not | medium | M | cpu, latency |
| [attestation_processing-124](#attestation_processing-124) | Single batching verifier for all attestation sources | partial | low | S | cpu |
| [attestation_processing-125](#attestation_processing-125) | Hoist base_reward_per_increment out of attestation loop | implemented | low | S | cpu |
| [attestation_processing-126](#attestation_processing-126) | In-place search instead of temporary sequence | n/a | low |  | cpu, memory |
| [attestation_processing-127](#attestation_processing-127) | Read-only validator view for slashed checks | n/a | low | S | memory, cpu |
| [attestation_processing-128](#attestation_processing-128) | Reuse gossip-computed indexed attestation downstream | implemented | low | S | cpu |
| [attestation_processing-129](#attestation_processing-129) | Handle payload attestations once block is known | implemented | low | S | latency |
| [attestation_processing-130](#attestation_processing-130) | Skip attestation simulator while syncing | implemented | low | S | cpu |

★ actionable. Click an id for the full record.

## Ideas

<a id="attestation_processing-001"></a>
<details>
<summary><b>attestation_processing-001</b> Use cached committees for attesting indices — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Resolve attesting indices in gossip verification, the op pool, fork choice vote updates and duties from a per-epoch committee/shuffling cache instead of recomputing the shuffling from a BeaconState per attestation. The shuffling is fixed for the epoch, so one computation serves every attestation.

**Impact.** Gossip attestations resolve committees from the shuffling cache. Fork choice and the op pool use the indexed attestations produced from it, and block import uses the per-epoch caches on the state.

**Best measured result.** 95% reduction in attestation processing time (best case) (pr:lighthouse#841)

**Evidence (Lighthouse @ 928b61e719).**

- lh-perf-research-base/beacon_node/beacon_chain/src/attestation_verification.rs:1547-1560 obtain_indexed_attestation_and_committees_per_slot
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1617-1640`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1617-L1640) map_attestation_committees uses chain.with_committee_cache
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7593-7612`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7593-L7612) with_committee_cache -&gt; with_cached_shuffling over shuffling_cache, reading a state from the DB only on a miss
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:397-411`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L397-L411) pre-populates shuffling_cache for the next epoch
- [`consensus/types/src/state/beacon_state.rs:825`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L825),2824-2836 block import uses Arc committee caches on the state, built once per epoch

**Skeptic check.** I confirmed the gossip path through the shuffling cache, with a DB state load only on a miss, and the per-epoch state caches for block import. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus@74dc2fffa](https://github.com/status-im/nimbus-eth2/commit/74dc2fffa60f), [nimbus#1126](https://github.com/status-im/nimbus-eth2/pull/1126), [lighthouse@3b92b6902](https://github.com/sigp/lighthouse/commit/3b92b6902802), [lodestar@59eba5ce2](https://github.com/ChainSafe/lodestar/commit/59eba5ce2246), [prysm#2265](https://github.com/OffchainLabs/prysm/pull/2265), [lighthouse#841](https://github.com/sigp/lighthouse/pull/841)

</details>


<a id="attestation_processing-002"></a>
<details>
<summary><b>attestation_processing-002</b> Shuffling cache keyed by epoch and dependent root — <i>partial · low · M · cpu, memory, latency</i></summary>

**Idea.** Key the committee/shuffling cache (and per-committee aggregate pubkeys) by (target epoch, shuffling decision/dependent root) so entries are correct across forks and shared by attestation verification, block production and API. Compute each shuffling once (at epoch transition or slot tick, deduplicating concurrent computations) so attestation committees come from the cache without recomputing the shuffling or needing a full state.

**Gap in Lighthouse.** The keyed, deduplicated, precomputed shuffling cache is present and shared by gossip verification, duties and production. Missing: per-committee aggregate public keys cached next to CachedShuffling (silver#329 keys both). Aggregate/attestation signature sets in indexed_attestation_signature_set aggregate each attester pubkey on every verification instead of starting from a cached committee aggregate.

**Impact.** Saves G1 point additions per aggregate verification (aggregates with near-full committees); small CPU win per slot.

**Best measured result.** single verify ~+100ns of ~70us; batch same or cheaper (pr:silver#329)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:129`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L129) HashMap&lt;AttestationShufflingId, CacheItem&gt; keyed by (epoch, shuffling decision root)
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:367`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L367) create_promise dedups concurrent misses
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:409`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L409) head shufflings precomputed at slot tick
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5211`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5211) import_block_update_shuffling_cache_fallible fills cache at import
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1747`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1747) attester duties use with_committee_cache
- [`beacon_node/beacon_chain/src/attestation_verification/batch.rs:133`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification/batch.rs#L133) batch verify builds per-attestation pubkey sets, no cached committee aggregate pubkey

**Skeptic check.** Verified the shuffling cache key, promise dedup, slot-tick priming and API/duties sharing; the earlier evidence was right on that core. The idea explicitly includes cached per-committee aggregate pubkeys, which Lighthouse does not have, so partial rather than implemented.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [silver#329](https://github.com/gattaca-com/silver/pull/329), [prysm#4270](https://github.com/OffchainLabs/prysm/pull/4270), [lodestar#6030](https://github.com/ChainSafe/lodestar/pull/6030), [lodestar#1178](https://github.com/ChainSafe/lodestar/pull/1178), [silver#189](https://github.com/gattaca-com/silver/pull/189)

</details>


<a id="attestation_processing-003"></a>
<details>
<summary><b>attestation_processing-003</b> Compute committee length without building committee — <i>implemented · low · S · cpu</i></summary>

**Idea.** When only a committee's size is needed (attestation validation, attesting info), compute it arithmetically from the cached active validator count instead of shuffling and materialising the committee. Avoids the shuffle and the allocation.

**Impact.** Committee size is read from an already-built committee cache; only the rare fallback in produce_unaggregated_attestation (beacon_chain.rs:2173, unadvanced state from disk) builds a committee cache to get a length.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2126`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2126) head path reads committee len from head_state committee cache
- [`consensus/types/src/state/committee_cache.rs:202`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L202) get_beacon_committee returns a slice of the cached shuffling, no allocation
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:335`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L335) advanced head state has current/next committee caches built

**Skeptic check.** Confirmed that the committee length comes from the cached shuffling as a slice length on the hot path; the arithmetic shortcut (closed lighthouse#4609) would only help the rare fallback that loads and advances a state. Earlier verdict upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#7664](https://github.com/OffchainLabs/prysm/pull/7664), [lighthouse#4609](https://github.com/sigp/lighthouse/pull/4609), [nimbus#1363](https://github.com/status-im/nimbus-eth2/pull/1363)

</details>


<a id="attestation_processing-004"></a>
<details>
<summary><b>attestation_processing-004</b> Cache committees-per-slot in epoch context — <i>implemented · low · S · cpu</i></summary>

**Idea.** Store committees-per-slot once per epoch in the epoch context, since it is constant through the epoch, and read it during gossip attestation validation instead of recomputing it from the active validator count.

**Impact.** Committees-per-slot is a stored per-epoch field; gossip subnet checks never recompute it from the active validator count.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/committee_cache.rs:142`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L142) committees_per_slot computed once at cache build
- [`consensus/types/src/state/committee_cache.rs:363`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L363) committees_per_slot() returns the stored field
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1085`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1085) gossip unaggregated path reads it from the shuffling cache's CommitteeCache

**Skeptic check.** Verified the gossip verification path takes committees_per_slot from the cached CommitteeCache. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#2759](https://github.com/ChainSafe/lodestar/pull/2759)

</details>


<a id="attestation_processing-005"></a>
<details>
<summary><b>attestation_processing-005</b> Carry committee sizes on validated attestation — <i>not · low · S · cpu</i></summary>

**Idea.** Attach the per-slot committee size map from the committee cache to the attestation object during validation so later aggregation does not look up or recompute committee sizes.

**Gap in Lighthouse.** Lighthouse returns committees_per_slot with the indexed attestation but not committee sizes; aggregation in the op pool uses attestation bitfield lengths so it does not need them.

**Impact.** Negligible; committee length is already available from the bitfield.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:1547`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1547) returns (attestation, committees_per_slot) only
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1616`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1616) committees fetched per call

**Sources.** [teku#8301](https://github.com/Consensys-Incorporated/teku/pull/8301)

</details>


<a id="attestation_processing-006"></a>
<details>
<summary><b>attestation_processing-006</b> Same-message signature check for equal-data attestations — <i>not · high · M · cpu, latency</i></summary>

**Idea.** Group unaggregated gossip attestations by (slot, attestation data root), aggregate the pubkeys and signatures of each group and do one signature check per group, falling back to per-attestation verification on failure. Verification cost scales with distinct data, not message count.

**Gap in Lighthouse.** Group the partially verified unaggregated attestations in batch_verify_unaggregated_attestations by signing root, aggregate pubkeys and signatures per group into one SignatureSet (or merge equal messages inside verify_signature_sets), keep the existing per-attestation fallback via from_indexed with CheckAttestationSignature::Yes.

**Impact.** Pairing work for gossip unaggregated batches (up to 64) drops from one hash-to-curve + Miller loop per attestation to one per distinct data; several-fold less BLS CPU on subscribed subnets.

**Best measured result.** 128 sigs: 130.5 ms vs 8.97 ms; CPU 140-160% vs &gt;=300% (pr:lodestar#5729)

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/impls/blst.rs:36`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L36) verify_signature_sets builds one (msg, agg_pk, sig, rand) tuple per set, no grouping by message
- blst-0.3.17/src/lib.rs:1335 verify_multiple_aggregate_signatures has '// TODO - check msg uniqueness?' and runs mul_n_aggregate (hash-to-curve + Miller loop) per element
- [`beacon_node/beacon_chain/src/attestation_verification/batch.rs:170`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification/batch.rs#L170) one signature set per unaggregated attestation

**Second check.** Checked the blst 0.3.17 crate itself for message dedup in the multi-verify path: none, only a TODO. No grouping in batch.rs or the beacon processor.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [prysm#3493](https://github.com/OffchainLabs/prysm/pull/3493), [lodestar#5729](https://github.com/ChainSafe/lodestar/pull/5729), [lodestar#5896](https://github.com/ChainSafe/lodestar/pull/5896)

</details>


<a id="attestation_processing-007"></a>
<details>
<summary><b>attestation_processing-007</b> Validate same-data attestations as one group — <i>partial · medium · M · cpu, latency</i></summary>

**Idea.** When draining queued or API-submitted attestations, group by attestation data, run the shared data checks, target state lookup and signing root once per group, and batch-verify the signatures, verifying individually only if the batch fails.

**Gap in Lighthouse.** The expensive parts of the idea (target state lookup once, batch signature verify with individual fallback) exist for gossip. Missing: bucketing by AttestationData so the head-block/target checks and signing-root hashing run once per bucket, and using the batch path for API submissions (see 009).

**Impact.** Small: remaining per-attestation work is a fork choice read lock, a committee cache hit and one signing-root hash (microseconds); the 50-100ms per-attestation cost the source PR fixed is state lookup, which the shuffling cache already avoids.

**Best measured result.** processing 100 attestations could take up to 10s; per-attestation 50-100ms before (pr:prysm#15801)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification/batch.rs:133`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification/batch.rs#L133) gossip unaggregated attestations are batch BLS verified with per-attestation fallback when the batch fails
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1617`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1617) map_attestation_committees takes committees from shuffling_cache via with_committee_cache, so the target-state/committee lookup happens once per shuffling, not per attestation
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:106`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L106) CacheItem::Promise coalesces concurrent misses so only one state load runs for many attestations of the same target
- [`beacon_node/beacon_chain/src/attestation_verification/batch.rs:146`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification/batch.rs#L146) IndexedUnaggregatedAttestation::verify still runs per attestation (head block, slot range, signing root)

**Second check.** Earlier review missed that the shuffling cache (with promise-based miss coalescing) already gives the once-per-target state/committee lookup, and that gossip already batch-verifies with fallback.

**Verdict history.** not (checked) → partial (refuted)

**Sources.** [lodestar#3392](https://github.com/ChainSafe/lodestar/pull/3392), [prysm#15801](https://github.com/OffchainLabs/prysm/pull/15801), [lodestar#5311](https://github.com/ChainSafe/lodestar/pull/5311)

</details>


<a id="attestation_processing-008"></a>
<details>
<summary><b>attestation_processing-008</b> Aggregate attestations in pool before fork choice — <i>not · medium · M · cpu, latency</i></summary>

**Idea.** Save gossip and API attestations straight into the fork-choice pool and aggregate equal-data ones there before applying them to fork choice, instead of a periodic batching step with many separate on-attestation calls.

**Gap in Lighthouse.** No aggregation of equal-data attestations before fork choice. Lighthouse has no periodic batching step to replace (it applies immediately), and on_attestation is a per-validator latest-message update, so aggregating first would only save write-lock acquisitions.

**Impact.** Negligible: per-validator vote work is the same with or without pre-aggregation; only lock acquisitions are saved.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2573`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2573) apply_attestation_to_fork_choice takes the fork choice write lock and calls on_attestation per verified attestation
- [`beacon_node/http_api/src/publish_attestations.rs:100`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_attestations.rs#L100) API path applies each attestation to fork choice, then to the naive aggregation pool
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2596`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2596) naive aggregation pool is separate and feeds aggregate production, not fork choice

**Second check.** Looked for any queue that aggregates before on_attestation (fork choice queued_attestations, naive aggregation pool); neither feeds aggregated votes into fork choice.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [prysm#12337](https://github.com/OffchainLabs/prysm/pull/12337)

</details>


<a id="attestation_processing-009"></a>
<details>
<summary><b>attestation_processing-009</b> Batch-verify API-submitted attestations — <i>not · medium · S · cpu</i></summary>

**Idea.** Hand attestations submitted through the validator HTTP API to the verifier as one batch so their signatures are batch verified rather than one by one.

**Gap in Lighthouse.** In publish_attestations, call chain.batch_verify_unaggregated_attestations_for_gossip over the request's SingleAttestations, then publish/apply each verified result; keep the UnknownHeadBlock reprocess path for individual failures.

**Impact.** Only for nodes serving many local validators: roughly halves BLS cost of their POSTed attestations (more with 006); nothing for ordinary nodes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/publish_attestations.rs:143`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_attestations.rs#L143) blocking task maps over the request's attestations one by one
- [`beacon_node/http_api/src/publish_attestations.rs:76`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_attestations.rs#L76) verify_and_publish_attestation calls verify_unaggregated_attestation_for_gossip (single signature check)
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:327`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L327) only caller of batch_verify_unaggregated_attestations_for_gossip outside tests

**Second check.** Confirmed the API path does not go through the beacon processor batching and no other batch caller exists.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [grandine@f8cf3c33f](https://github.com/grandinetech/grandine/commit/f8cf3c33ff1d), [grandine#198](https://github.com/grandinetech/grandine/pull/198)

</details>


<a id="attestation_processing-010"></a>
<details>
<summary><b>attestation_processing-010</b> Batch gossip attestation signature verification — <i>implemented · high · S · cpu</i></summary>

**Idea.** In the beacon processor, collect gossip attestations into batches (time-bounded or greedy) and verify their signatures together to amortise BLS cost.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:110`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L110) DEFAULT_MAX_GOSSIP_ATTESTATION_BATCH_SIZE = 64
- [`beacon_node/beacon_processor/src/lib.rs:1017`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1017) attestation_queue drained greedily into GossipAttestationBatch when 2+ queued
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:318`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L318) process_gossip_attestation_batch calls batch_verify_unaggregated_attestations_for_gossip
- [`beacon_node/beacon_chain/src/attestation_verification/batch.rs:133`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification/batch.rs#L133) batch_verify_unaggregated_attestations with individual fallback

**Skeptic check.** Verified greedy batching in the beacon processor and the batch BLS verify for gossip attestations (aggregates are batched the same way). Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#8285](https://github.com/sigp/lighthouse/pull/8285)

</details>


<a id="attestation_processing-011"></a>
<details>
<summary><b>attestation_processing-011</b> Batch-verify reprocessed pending attestations — <i>partial · medium · M · cpu, latency</i></summary>

**Idea.** When releasing queued attestations (e.g. after their block is imported), verify their signatures as one batch instead of one by one, and requeue future-slot or missing-target ones directly rather than reprocessing them.

**Gap in Lighthouse.** Released attestations get requeued directly (done) but are verified one by one via process_fn. Would need unknown_block queues to form GossipAttestationBatch/GossipAggregateBatch (or re-push released work into the normal batching queues) in BeaconProcessor::spawn_manager.

**Impact.** Fewer BLS verifications when a block arrives late and hundreds of queued attestations are released at once; batch verify is roughly 2x cheaper per sig, only on late-block slots.

**Best measured result.** attestation processing was 23% of profile (pr:lodestar#2754)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:2919`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L2919) failed unaggregate requeued as UnknownBlockUnaggregate with process_fn calling single process_gossip_attestation
- [`beacon_node/beacon_processor/src/lib.rs:1086`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1086) unknown_block_*_queue popped one item at a time (Work::UnknownBlockAttestation process_fn, lib.rs:1682)
- [`beacon_node/beacon_processor/src/lib.rs:1030`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1030) batching exists only for fresh gossip attestation_queue/aggregate_queue

**Sources.** [lodestar#2754](https://github.com/ChainSafe/lodestar/pull/2754), [teku#10431](https://github.com/Consensys-Incorporated/teku/pull/10431)

</details>


<a id="attestation_processing-012"></a>
<details>
<summary><b>attestation_processing-012</b> Amortise locks over attestation batches — <i>partial · low · M · cpu</i></summary>

**Idea.** Process attestations in batches in the handlers and take shared locks (e.g. the attestation cache lock) once per batch instead of once per attestation, amortising locking and per-call overhead.

**Gap in Lighthouse.** Handlers are batched and the pubkey cache lock is taken once per batch, but after batch BLS every attestation is imported on its own: fork-choice write lock, naive aggregation pool write lock, op pool insert, and during indexing the observed_gossip_attesters read+write locks and the fork-choice read lock in with_committee_cache. Add batch import (one fork_choice_write_lock for all on_attestation calls, one naive_aggregation_pool.write() for all inserts) and group indexing by (target root, epoch).

**Impact.** Fewer lock round-trips per gossip batch (up to 64); mostly matters under fork-choice write-lock contention with block import. Likely a small CPU and latency win.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification/batch.rs:60`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification/batch.rs#L60) one validator_pubkey_cache.read() per batch for signature set setup
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:316`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L316) gossip handler already processes attestations in batches
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:363`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L363) per-result import loop calls process_gossip_attestation_result once per attestation
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2578`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2578) fork_choice_write_lock taken per attestation in apply_attestation_to_fork_choice
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2604`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2604) naive_aggregation_pool.write() per attestation
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2712`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2712) op_pool.insert_attestation per aggregate
- [`beacon_node/beacon_chain/src/attestation_verification.rs:997`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L997) observed_gossip_attesters read lock per attestation
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1076`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1076) with_committee_cache (fork choice read lock) per attestation
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1127`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1127) observed_gossip_attesters write lock per attestation

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [grandine#908](https://github.com/grandinetech/grandine/pull/908), [prysm#16038](https://github.com/OffchainLabs/prysm/pull/16038)

</details>


<a id="attestation_processing-013"></a>
<details>
<summary><b>attestation_processing-013</b> Compute block attestations&#x27; target state once — <i>implemented · medium · S · cpu, memory, disk</i></summary>

**Idea.** Process a block's attestations in order (sorted by slot, sequentially) so the first one loads or computes the needed target checkpoint state and blocks, and the rest reuse it. This avoids concurrent or per-attestation reads and regenerations of the same state.

**Best measured result.** "reduce time in processing a block" (no numbers) (pr:prysm#2370)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/consensus_context.rs:161`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/consensus_context.rs#L161) get_indexed_attestation uses the block pre-state committee caches, memoised by attestation root
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4987`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4987) block import feeds fork choice from ctxt.get_indexed_attestation, no per-attestation state load

**Skeptic check.** Block attestations are indexed once against the single block pre-state and reused for fork choice; no target-state regeneration per attestation happens on block import. Earlier verdict upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#2370](https://github.com/OffchainLabs/prysm/pull/2370), [lodestar@268ef36df](https://github.com/ChainSafe/lodestar/commit/268ef36df6e7)

</details>


<a id="attestation_processing-014"></a>
<details>
<summary><b>attestation_processing-014</b> Merge passes over block attestations — <i>not · low · S · cpu</i></summary>

**Idea.** Combine the separate loops over a block's attestations during block processing so the list is iterated one fewer time.

**Gap in Lighthouse.** Signature set collection (BlockSignatureVerifier) and process_attestations are separate passes over attestations; merging them is a micro tweak with ConsensusContext already caching indexed attestations.

**Impact.** Micro; iteration over &lt;=8 attestations (128 pre-Electra) is trivial next to BLS and balance updates.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/process_operations.rs:308`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L308) per-attestation loop in process_attestations
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:42`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L42) called once from process_operations

**Sources.** [prysm#15849](https://github.com/OffchainLabs/prysm/pull/15849)

</details>


<a id="attestation_processing-015"></a>
<details>
<summary><b>attestation_processing-015</b> Aggregate only the current slot&#x27;s signatures — <i>n/a · low · S · cpu, latency</i></summary>

**Idea.** Run the deadline-bounded aggregation pass only over the current slot's raw gossip signatures, not all slots, so the time budget is not spent on stale or recursive-merge work.

**Impact.** Lean-consensus proof aggregation has no counterpart in Lighthouse's BLS design.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification/batch.rs:133`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification/batch.rs#L133) plain batch BLS verify, no recursive proof aggregation

**Sources.** [ethlambda#485](https://github.com/lambdaclass/ethlambda/pull/485)

</details>


<a id="attestation_processing-016"></a>
<details>
<summary><b>attestation_processing-016</b> Per-aggregator subnet windows for child proof selection — <i>n/a · low · S · cpu</i></summary>

**Idea.** Give each aggregator a different subnet window as a scoring lens when choosing child proofs, and optionally skip candidates it does not own, so aggregators avoid merging identical children.

**Impact.** Lean-consensus child-proof selection has no counterpart in Lighthouse.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification/batch.rs:28`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification/batch.rs#L28) BLS aggregates, no child proofs

**Sources.** [ethlambda#613](https://github.com/lambdaclass/ethlambda/pull/613)

</details>


<a id="attestation_processing-017"></a>
<details>
<summary><b>attestation_processing-017</b> Always-running aggregation worker — <i>n/a · low · S · cpu, latency</i></summary>

**Idea.** Keep one long-lived aggregation worker that repeatedly ranks pool candidates, proves the best and stores it, publishing at protocol time, so the prover is not idle most of the slot and has no per-slot deadline.

**Impact.** No prover exists in Lighthouse; BLS aggregation is cheap and not deadline-bound.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification/batch.rs:28`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification/batch.rs#L28) BLS aggregation is cheap and inline

**Sources.** [ethlambda#603](https://github.com/lambdaclass/ethlambda/pull/603)

</details>


<a id="attestation_processing-018"></a>
<details>
<summary><b>attestation_processing-018</b> Throttle aggregation before own proposal — <i>n/a · low · cpu, latency</i></summary>

**Idea.** Reduce aggregation to one job when this node proposes the next slot so aggregation does not compete for the prover with the deadline-bound block build.

**Impact.** Lean-consensus recursive proof aggregation; Lighthouse aggregates BLS signatures cheaply, no prover to contend with.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/common/get_attesting_indices.rs:1`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/get_attesting_indices.rs#L1) - no prover/zk aggregation in Lighthouse

**Sources.** [ethlambda#544](https://github.com/lambdaclass/ethlambda/pull/544)

</details>


<a id="attestation_processing-019"></a>
<details>
<summary><b>attestation_processing-019</b> Limit aggregation jobs to two child proofs — <i>n/a · low · cpu, latency</i></summary>

**Idea.** Limit each aggregation job to a binary merge of 2 child proofs and leave leftovers for later rounds, bounding per-round recursive verification cost and staying under the prover recursion cap.

**Impact.** Lean-consensus proof recursion cap; no equivalent in Lighthouse.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/naive_aggregation_pool.rs:239`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/naive_aggregation_pool.rs#L239) - BLS aggregation, no recursive proofs

**Sources.** [ethlambda#482](https://github.com/lambdaclass/ethlambda/pull/482)

</details>


<a id="attestation_processing-020"></a>
<details>
<summary><b>attestation_processing-020</b> Run attestation aggregation at fixed slot offsets — <i>n/a · low · cpu, latency</i></summary>

**Idea.** Schedule the fork-choice attestation aggregation work at fixed configurable offsets within the slot via a slot ticker instead of a free-running interval, and do not start the attestation service until initial sync is done.

**Impact.** Lighthouse has no free-running fork-choice aggregation interval to replace; fork choice is run on slot ticks and per import. Gain would be marginal.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:7471`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7471) - per_slot_task drives fork choice on slot tick
- [`beacon_node/beacon_processor/src/lib.rs:1014`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1014) - attestations processed as queued work, no free-running aggregation interval

**Sources.** [prysm#12377](https://github.com/OffchainLabs/prysm/pull/12377), [prysm#12349](https://github.com/OffchainLabs/prysm/pull/12349)

</details>


<a id="attestation_processing-021"></a>
<details>
<summary><b>attestation_processing-021</b> Process attestations and update head once per slot — <i>partial · medium · S · cpu</i></summary>

**Idea.** Apply pending attestations to fork choice and recompute head once per slot instead of both on tick and on proposal.

**Gap in Lighthouse.** Attestation application is batched per slot via the queue, but head is recomputed at the pre-slot timer, at slot start and on each block import, i.e. not once per slot. Could drop the per_slot_task recompute when state_advance_timer already ran for that slot.

**Impact.** Saves one get_head (proto-array apply_score_changes over all votes) per slot, likely a few ms of the fork choice write lock; small.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fork_choice/src/fork_choice.rs:1386`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1386) attestations of current slot queued; fork_choice.rs:1580 process_attestation_queue dequeues in bulk on update_time
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:212`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L212) recompute_head_at_slot(next_slot) pre-emptively before slot end
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7496`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7496) per_slot_task recomputes head again at slot start
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:207`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L207) recompute on block import

**Sources.** [prysm#12087](https://github.com/OffchainLabs/prysm/pull/12087)

</details>


<a id="attestation_processing-022"></a>
<details>
<summary><b>attestation_processing-022</b> Verify aggregates before unaggregated attestations — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** In the attestation verification queue, prioritise aggregate-and-proof messages over unaggregated attestations so limited verification CPU goes to the more valuable, time-critical messages first.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:958`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L958) comment: aggregates before unaggregates
- [`beacon_node/beacon_processor/src/lib.rs:961`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L961) aggregate_queue popped first
- [`beacon_node/beacon_processor/src/lib.rs:1017`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1017) attestation_queue only after aggregate_queue is empty

**Skeptic check.** Verified the strict priority order in the beacon processor scheduling loop. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine@bf3b57760](https://github.com/grandinetech/grandine/commit/bf3b57760e46)

</details>


<a id="attestation_processing-023"></a>
<details>
<summary><b>attestation_processing-023</b> Prioritise attestations in processing loop; fast uint64 — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Give attestation processing higher scheduling priority than other work in the processing loop, and convert bytes to uint64 with a direct load instead of a byte loop.

**Impact.** Attestations already outrank most other work in the beacon processor; byte-to-u64 is from_le_bytes in Rust.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:905-1070`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L905-L1070) strict priority chain: blocks/columns/p0 API, then aggregate_queue (969) and attestation_queue (1025) ahead of sync messages, RPC serving (1108+), slashings/exits and p1 API
- [`beacon_node/beacon_processor/src/lib.rs:110`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L110) gossip attestation batching

**Skeptic check.** Read the dequeue chain: attestations and aggregates are popped before sync committee work, req/resp serving and other gossip. The earlier verdict holds.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#2301](https://github.com/status-im/nimbus-eth2/pull/2301)

</details>


<a id="attestation_processing-024"></a>
<details>
<summary><b>attestation_processing-024</b> Keep gossip aggregates out of fork choice — <i>not · medium · S · cpu</i></summary>

**Idea.** Store gossip aggregate-and-proof attestations only in the op pool for block inclusion and do not apply them to fork choice, since their votes arrive anyway via unaggregated attestations and blocks.

**Gap in Lighthouse.** Lighthouse applies every verified gossip aggregate to fork choice (iterating all attesting indices into proto_array.process_attestation) and then to the op pool. Would skip the apply_attestation_to_fork_choice call in process_gossip_aggregate_result (keep op pool insert), accepting reliance on unaggregates and blocks.

**Impact.** Removes a write-lock acquisition plus ~hundreds of vote updates per aggregate (about 100 aggregates/slot after dedup), so less fork choice lock contention; modest CPU saving. Risk: slightly later vote visibility for validators on few subnets.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:631`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L631) process_gossip_aggregate_result calls chain.apply_attestation_to_fork_choice(&amp;verified_aggregate)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2573`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2573) apply_attestation_to_fork_choice takes fork_choice_write_lock and on_attestation

**Sources.** [lodestar#1722](https://github.com/ChainSafe/lodestar/pull/1722)

</details>


<a id="attestation_processing-025"></a>
<details>
<summary><b>attestation_processing-025</b> Field-wise attestation data equality — <i>not · low · S · cpu, memory</i></summary>

**Idea.** Compare AttestationData with a direct field-by-field equality instead of serialising or hash-tree-rooting both sides, removing allocations on the duplicate-detection hot path.

**Gap in Lighthouse.** Dedup is a hash-map lookup keyed by tree_hash_root, so a field-wise compare would only help if the key were AttestationData itself (derive Hash, key map on it). Change ObservedAggregates key type and root().

**Impact.** Saves roughly 7 sha256 compressions plus a clone per gossip aggregate/attestation; small share of CPU.

**Best measured result.** fast 18.1 ns/op 0 allocs vs slow 4363 ns/op 30 allocs (pr:prysm#5834)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/observed_aggregates.rs:178-186`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_aggregates.rs#L178-L186) root() clones AttestationData into ObservedAttestationKey and calls tree_hash_root for dedup
- [`consensus/types/src/attestation/attestation_data.rs:17`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/attestation/attestation_data.rs#L17) derives PartialEq but dedup is keyed by hash root

**Sources.** [prysm#5834](https://github.com/OffchainLabs/prysm/pull/5834)

</details>


<a id="attestation_processing-026"></a>
<details>
<summary><b>attestation_processing-026</b> Allocation-free attesting indices computation — <i>partial · medium · S · cpu, memory</i></summary>

**Idea.** Compute attesting indices/participants without intermediate vectors or sequences (preallocate, write directly) so per-attestation work in block and epoch processing does not allocate.

**Gap in Lighthouse.** Electra/Gloas get_attesting_indices allocates a Vec for committee indices, a HashSet per committee and a growing Vec. Rewrite attesting_indices_electra::get_attesting_indices to size the output from aggregation_bits.num_set_bits(), push directly, iterate committee_bits without collecting, and drop the HashSet.

**Impact.** Fewer allocations in block processing and gossip aggregate verification (called for every aggregate and block attestation); likely a small percent of block import time, not the 15% seen in the old Nimbus sim.

**Best measured result.** 15% to 1% of block_sim at 100k validators (pr:nimbus#1351)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/common/get_attesting_indices.rs:30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/get_attesting_indices.rs#L30) base version preallocates Vec::with_capacity(num_set_bits)
- [`consensus/state_processing/src/common/get_attesting_indices.rs:100`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/get_attesting_indices.rs#L100) electra version starts with vec![], collects a HashSet per committee, calls get_committee_indices that allocates a Vec, then extend and sort
- [`consensus/state_processing/src/consensus_context.rs:161`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/consensus_context.rs#L161) results memoised per attestation root so each is computed once per block

**Sources.** [nimbus#1351](https://github.com/status-im/nimbus-eth2/pull/1351), [lighthouse@a44d80006](https://github.com/sigp/lighthouse/commit/a44d80006a65)

</details>


<a id="attestation_processing-027"></a>
<details>
<summary><b>attestation_processing-027</b> Iterate only set bits of aggregation bitfield — <i>not · low · S · cpu, memory</i></summary>

**Idea.** Derive attesting indices by iterating the set bits of the aggregation bitfield directly (word-level scan) rather than testing every bit position.

**Gap in Lighthouse.** Iterate set bits (BitIter / byte-wise scan) and index into the committee slice instead of testing each position; drop the per-committee HashSet. Edit get_attesting_indices (electra) and the base variant.

**Impact.** Cuts per-attestation index derivation, used in block processing and fork choice; sparse aggregates benefit most. Small overall.

**Best measured result.** 2107 ns/op -&gt; 277 ns/op, 1057 -&gt; 576 B/op (pr:prysm#5160)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/common/get_attesting_indices.rs:116-125`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/get_attesting_indices.rs#L116-L125) enumerates every committee member and calls aggregation_bits.get(i) per position, collecting into a HashSet

**Sources.** [prysm#5160](https://github.com/OffchainLabs/prysm/pull/5160)

</details>


<a id="attestation_processing-028"></a>
<details>
<summary><b>attestation_processing-028</b> Avoid sorting attesting indices — <i>not · low · S · cpu, memory</i></summary>

**Idea.** Build attesting indices by walking the committee in aggregation-bit order and skip or minimise the generic sort, and skip sorting entirely where the spec does not need ordering. This removes the sort cost and allocation per attestation.

**Gap in Lighthouse.** Output ordering needed by IndexedAttestation requires sorted indices, and committee order is shuffled order, so the sort cannot be dropped in the indexed path; only callers needing just counts or a set (e.g. fork choice, rewards) could skip it. Add an unsorted variant and use it there.

**Impact.** Minor: saves a sort of up to a few hundred u64 per attestation on non-indexed callers.

**Best measured result.** 8% faster overall on ncli_db bench first 100k slots; ~12% on apply block (1.67ms to 1.47ms) (pr:nimbus#2274)

**Evidence (Lighthouse @ 928b61e719).**

- get_attesting_indices.rs:41 and :149 still call sort_unstable after collecting (electra path also via HashSet)
- committees are walked in order so output is already ascending in a single committee only if the committee is sorted, which it is not (shuffled)

**Sources.** [nimbus@490e4c766](https://github.com/status-im/nimbus-eth2/commit/490e4c766643), [nimbus#2274](https://github.com/status-im/nimbus-eth2/pull/2274), [prysm#2893](https://github.com/OffchainLabs/prysm/pull/2893)

</details>


<a id="attestation_processing-029"></a>
<details>
<summary><b>attestation_processing-029</b> Attesting indices as plain vector, not set — <i>partial · low · S · cpu, memory</i></summary>

**Idea.** Build attesting indices (and indexed attestations) by pushing committee members into a plain vector/array instead of deduplicating through a set, since committee members are unique by construction. This avoids set allocation and hashing.

**Gap in Lighthouse.** In attesting_indices_electra::get_attesting_indices, collect committee_attesters into a Vec (or push directly into attesting_indices and count) instead of HashSet; committee members are unique so dedup is unneeded, final sort_unstable already orders. Emptiness check can use a per-committee counter.

**Impact.** Saves a HashSet alloc and hashing per committee per block attestation in Electra+ block processing; sub-millisecond per block, tiny.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/common/get_attesting_indices.rs:27-45`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/get_attesting_indices.rs#L27-L45) - base path pushes into Vec (done)
- [`consensus/state_processing/src/common/get_attesting_indices.rs:120-130`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/get_attesting_indices.rs#L120-L130) - Electra path collects each committee into a HashSet&lt;u64&gt; then extends Vec

**Sources.** [lodestar@3818c78ef](https://github.com/ChainSafe/lodestar/commit/3818c78ef332), [nimbus#2288](https://github.com/status-im/nimbus-eth2/pull/2288)

</details>


<a id="attestation_processing-030"></a>
<details>
<summary><b>attestation_processing-030</b> Borrow matching committee instead of cloning all — <i>partial · low · S · cpu, memory</i></summary>

**Idea.** Find the attestation's committee with a search over the committee list and borrow it instead of mapping, collecting and cloning all committees; drop per-bit debug logging in the participant loop.

**Gap in Lighthouse.** VerifiedUnaggregatedAttestation::verify_late_checks copies the matching committee into a Vec (about 500 usize, ~4 KB on mainnet) for each gossip unaggregated attestation, only so it can leave the with_committee_cache closure. It then scans it twice (contains, then single_attestation_to_attestation). Find the attester's position inside the closure and return only the index (or build the Attestation there). Then no allocation is needed and there is one scan.

**Impact.** Removes one ~4 KB heap allocation and copy plus one linear scan per gossip unaggregated attestation, the highest-volume gossip message. Small CPU and allocator savings.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/committee_cache.rs:202-229`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L202-L229) get_beacon_committee borrows a shuffling slice (no clone of all committees)
- [`consensus/state_processing/src/consensus_context.rs:173`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/consensus_context.rs#L173) block processing borrows committee.committee
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1083`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1083) verify_late_checks does beacon_committee.committee.to_vec() for every gossip SingleAttestation
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1096`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1096) then committee.contains (scan 1)
- [`beacon_node/beacon_chain/src/single_attestation.rs:18-31`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/single_attestation.rs#L18-L31) single_attestation_to_attestation scans the committee again for the bit position

**Skeptic check.** The 'clone all committees' shape is gone: committee lookups borrow, as the earlier evidence says. But the earlier check missed the hottest path: unaggregated gossip verification still clones the matching committee for each message.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lighthouse@a1cdc0402](https://github.com/sigp/lighthouse/commit/a1cdc0402d70), [nimbus#7999](https://github.com/status-im/nimbus-eth2/pull/7999)

</details>


<a id="attestation_processing-031"></a>
<details>
<summary><b>attestation_processing-031</b> Verify single attestations in native form — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Receive and verify unaggregated SingleAttestation gossip messages in their native form and convert to a full attestation only after verification, removing a separate conversion work event.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:284`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L284) process_gossip_attestation takes Box&lt;SingleAttestation&gt;
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1143`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1143) single_attestation_to_attestation only in verify_late_checks after the checks
- [`beacon_node/beacon_processor/src/lib.rs:373`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L373) GossipAttestationBatch is Vec&lt;GossipAttestationPackage&lt;SingleAttestation&gt;&gt;
- [`beacon_node/http_api/src/publish_attestations.rs:77`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_attestations.rs#L77) API path also verifies SingleAttestation via the same function

**Skeptic check.** Gossip and API both verify SingleAttestation natively and convert only after verification; no separate conversion work event exists. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#7444](https://github.com/sigp/lighthouse/pull/7444)

</details>


<a id="attestation_processing-032"></a>
<details>
<summary><b>attestation_processing-032</b> Convert attestations on worker, not async thread — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Do the single-attestation to committee-attestation conversion (committee lookup) on a beacon processor worker instead of an async runtime thread so the runtime is not blocked.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/mod.rs:86`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L86) send_unaggregated_attestation wraps processing as beacon processor Work
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1076`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1076) committee lookup and conversion run inside verification on the worker
- [`beacon_node/http_api/src/publish_attestations.rs:142`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_attestations.rs#L142) API path runs verification in task_spawner.blocking_task

**Skeptic check.** The committee lookup and conversion happen on a beacon processor worker (gossip) or a blocking task (API), not on an async runtime thread. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#6934](https://github.com/sigp/lighthouse/pull/6934)

</details>


<a id="attestation_processing-033"></a>
<details>
<summary><b>attestation_processing-033</b> Check pool attestations by reference — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Inspect attestation pool entries by reference instead of copying each entry for every check.

**Impact.** Pool checks run on references; copies happen only for a new insert or an API fetch.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/naive_aggregation_pool.rs:257-297`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/naive_aggregation_pool.rs#L257-L297) insert takes AttestationRef, checks the bit with get_mut, aggregates in place, and clones only on a new entry
- [`beacon_node/beacon_chain/src/naive_aggregation_pool.rs:302`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/naive_aggregation_pool.rs#L302) get clones only the one requested aggregate

**Skeptic check.** Verified the insert/check path borrows existing entries mutably and does not copy them. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#1755](https://github.com/status-im/nimbus-eth2/pull/1755)

</details>


<a id="attestation_processing-034"></a>
<details>
<summary><b>attestation_processing-034</b> Avoid implicit state copy in attestation production — <i>n/a · low · cpu, memory</i></summary>

**Idea.** Avoid iterator/accessor patterns that silently copy the whole BeaconState during attestation production.

**Impact.** Nim implicit value copy; Rust state accessors take references and clones are explicit (and milhouse state is cheap to clone).

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:1206`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1206) - get_beacon_committee takes &amp;self

**Sources.** [nimbus#3274](https://github.com/status-im/nimbus-eth2/pull/3274)

</details>


<a id="attestation_processing-035"></a>
<details>
<summary><b>attestation_processing-035</b> Verify signatures without building indexed attestation — <i>partial · medium · M · cpu, memory</i></summary>

**Idea.** Verify attestation signatures directly from committee and aggregation bits without constructing a full indexed attestation, and skip building it entirely when signatures are not checked; avoid pointer work when adding to the pool.

**Gap in Lighthouse.** No signature-set builder works from committee and aggregation bits directly; IndexedAttestation (Vec alloc + sort) is always built, also when signatures are not verified. Only de-duplication via ConsensusContext cache exists. The indexed form is still needed afterwards for fork choice, slasher and validity checks, so the saving is one allocation/sort pass.

**Impact.** Small: one Vec allocation and sort per aggregate/block attestation; negligible next to BLS cost.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/consensus_context.rs:161`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/consensus_context.rs#L161) get_indexed_attestation caches the IndexedAttestation by attestation tree_hash_root, so the block signature verifier and process_operations build it once per block attestation
- [`consensus/state_processing/src/per_block_processing/block_signature_verifier.rs:297`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/block_signature_verifier.rs#L297) signature sets are built from the cached indexed attestation
- [`consensus/state_processing/src/per_block_processing/verify_attestation.rs:92`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/verify_attestation.rs#L92) indexed attestation is still built when verify_signatures is false (needed for is_valid_indexed_attestation sorted/non-empty checks)
- [`consensus/state_processing/src/common/get_attesting_indices.rs:25`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/get_attesting_indices.rs#L25) indices collected into a Vec and sorted
- [`consensus/state_processing/src/per_block_processing/signature_sets.rs:295`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/signature_sets.rs#L295) indexed_attestation_signature_set only accepts an IndexedAttestationRef; no committee+bits builder exists
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1558`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1558) aggregate gossip path builds IndexedAttestation before signature set

**Second check.** Checked ConsensusContext caching, signature_sets.rs builders and the VerifySignatures::False path in verify_attestation; no bits-based signature-set builder or skip-when-unverified path exists, so partial (caching only) stands.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [nimbus@f1f424cc2](https://github.com/status-im/nimbus-eth2/commit/f1f424cc2d2f), [nimbus#2503](https://github.com/status-im/nimbus-eth2/pull/2503)

</details>


<a id="attestation_processing-036"></a>
<details>
<summary><b>attestation_processing-036</b> Keep pending attestations tree-backed — <i>n/a · low · S · cpu</i></summary>

**Idea.** In block processing, keep pending attestations in their tree-backed SSZ form instead of converting them to plain objects.

**Impact.** Lodestar-specific tree-view conversion; Lighthouse state lists are milhouse trees and Electra+ has no pending attestations.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types) BeaconState uses milhouse persistent lists (already tree-backed)

**Sources.** [lodestar#2349](https://github.com/ChainSafe/lodestar/pull/2349)

</details>


<a id="attestation_processing-037"></a>
<details>
<summary><b>attestation_processing-037</b> Fetch target checkpoint state asynchronously — <i>partial · medium · M · latency, cpu</i></summary>

**Idea.** Retrieve the attestation target checkpoint state asynchronously (cache hit or regeneration off the processing thread) instead of a blocking store lookup, so attestation processing threads are not blocked by state loading.

**Gap in Lighthouse.** Lighthouse avoids the state load in the common case by proactively priming the shuffling cache off-thread (block import + state advance timer), but a real miss (reorg, non-head target) still blocks a beacon-processor worker while the state is loaded and advanced; there is no async fetch with re-queue of the attestation.

**Impact.** Only matters on shuffling cache misses during reorgs/non-finality; little effect on a healthy node.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5211`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5211) import_block_update_shuffling_cache_fallible primes current and next epoch shufflings at block import
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:167`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L167) state advance runs in spawn_blocking off the processing threads
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:409`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L409) advanced head state primes the next-epoch shuffling cache ahead of the epoch boundary
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:346`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L346) read-lock cache hit path
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:375`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L375) promise dedups concurrent misses (MAX_CONCURRENT_PROMISES=2 at :36)
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:371`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L371) miss path loads/advances state synchronously on the calling beacon-processor worker

**Second check.** Beyond the earlier review, found the proactive priming in block import and the spawn_blocking state advance timer, which is an equivalent mechanism for the hot path; the miss path is still synchronous, so partial stands.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [teku#2465](https://github.com/Consensys-Incorporated/teku/pull/2465)

</details>


<a id="attestation_processing-038"></a>
<details>
<summary><b>attestation_processing-038</b> Cache checkpoint states by target checkpoint — <i>implemented · medium · S · cpu, disk, latency</i></summary>

**Idea.** Keep an in-memory checkpoint-state cache keyed by target checkpoint, fill it with the state regenerated on a miss, and use it for attestation verification. Many attestations to the same target then share one state regeneration instead of a database load or regen each.

**Impact.** Attestation verification needs only the shuffling (pubkeys come from the validator pubkey cache), so caching the shuffling gives the same effect as a checkpoint-state cache at lower memory cost.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:315`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L315) with_cached_shuffling keyed by AttestationShufflingId
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:367`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L367) promise makes concurrent misses share one state load/advance
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:430`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L430) miss loads get_advanced_hot_state once and fills the cache

**Skeptic check.** Verified that a miss creates a promise, loads one advanced state and fills the cache, so all attestations to the same target share one regeneration. The mechanism differs (shuffling, not full state), but the effect is the same; verdict upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#1401](https://github.com/ChainSafe/lodestar/pull/1401), [prysm#9282](https://github.com/OffchainLabs/prysm/pull/9282), [prysm#3345](https://github.com/OffchainLabs/prysm/pull/3345)

</details>


<a id="attestation_processing-039"></a>
<details>
<summary><b>attestation_processing-039</b> Validate attestations on head state when shuffling matches — <i>implemented · medium · S · cpu, memory, latency</i></summary>

**Idea.** When the attestation's target epoch committees are already determined in the head (or another in-memory) state, i.e. the shuffling dependent root matches, verify it against that state and its committee cache, also for previous- and next-epoch targets. This avoids loading, regenerating or advancing the exact target checkpoint state.

**Impact.** Committees come from a cache keyed by shuffling decision root, so any state (head, imported block, advanced head) with the same dependent root serves the attestation without a target state load.

**Best measured result.** Attestation processing 1 sec -&gt; 54 ms (pr:caplin#10020)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:330`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L330)
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:349`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L349)
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:399`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L399)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5211`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5211)
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:409`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L409)
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1646`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1646)

**Skeptic check.** Verified with_cached_shuffling keys on AttestationShufflingId (decision root) and every block import primes current+next shufflings, so previous-epoch targets also hit the cache. Earlier evidence was right; the previous=None remark is not a real gap since that shuffling was primed as 'current' when the target-epoch blocks were imported.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#5482](https://github.com/Consensys-Incorporated/teku/pull/5482), [lodestar#5500](https://github.com/ChainSafe/lodestar/pull/5500), [prysm#17649](https://github.com/OffchainLabs/prysm/pull/17649), [prysm#17441](https://github.com/OffchainLabs/prysm/pull/17441), [prysm#16109](https://github.com/OffchainLabs/prysm/pull/16109), [prysm#16095](https://github.com/OffchainLabs/prysm/pull/16095), [teku#5822](https://github.com/Consensys-Incorporated/teku/pull/5822), [prysm#15095](https://github.com/OffchainLabs/prysm/pull/15095), [caplin#10020](https://github.com/erigontech/erigon/pull/10020), [prysm#15965](https://github.com/OffchainLabs/prysm/pull/15965), [teku#9215](https://github.com/Consensys-Incorporated/teku/pull/9215)

</details>


<a id="attestation_processing-040"></a>
<details>
<summary><b>attestation_processing-040</b> On shuffling miss, use epoch-boundary target state — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** On a shuffling cache miss, load the attestation's target (epoch-boundary) state to compute committees instead of the block-root state, avoiding replay of blocks and skip slots to a mid-epoch state.

**Impact.** Miss path loads the target-root state advanced near the epoch boundary (get_advanced_hot_state) and partial-advances only if needed.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:418`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L418)
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:436`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L436)
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:450`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L450)
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1646`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1646)

**Skeptic check.** map_attestation_committees passes target.root (not beacon_block_root) to with_committee_cache, and the miss path loads that block's advanced hot state; this is PR 4235's mechanism. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#4235](https://github.com/sigp/lighthouse/pull/4235)

</details>


<a id="attestation_processing-041"></a>
<details>
<summary><b>attestation_processing-041</b> Build committee cache right after advancing state — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Build the committee cache on the state used for attestation verification immediately after advancing it to the attestation slot, so later committee lookups do not rebuild it or fail.

**Impact.** Each path that advances a state for committee lookups builds the cache at once and keeps it in the shuffling cache.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:448-474`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L448-L474) gossip attestation shuffling miss: partial_state_advance and then build_committee_cache before the committee cache is cloned into the shuffling cache
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2164-2173`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2164-L2173) produce_unaggregated_attestation builds Current right after the advance
- [`beacon_node/beacon_chain/src/block_verification.rs:2197-2207`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L2197-L2207) block path builds Previous and Current after the advance

**Skeptic check.** Besides the cited production path, the gossip verification path (shuffling_cache.rs) and block verification also build the cache right after the advance. Upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@67fe21c1c](https://github.com/sigp/lighthouse/commit/67fe21c1c03f)

</details>


<a id="attestation_processing-042"></a>
<details>
<summary><b>attestation_processing-042</b> Reject finalized or old-target attestations before state load — <i>implemented · high · S · cpu, latency, disk, memory</i></summary>

**Idea.** Before loading or regenerating any state or verifying signatures, cheaply reject attestations whose target or slot is at or before finalization (or not descended from finalized), so stale attestations never trigger multi-epoch block replays.

**Impact.** Pre-finalization or non-descendant head/target roots are rejected via fork choice lookups before any committee or state work, on both unaggregated and aggregate paths (API submissions use the same gossip verification).

**Best measured result.** avoids replays of up to 32 epochs of blocks stalling processing (pr:nimbus#2361)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:1244`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1244)
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1268`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1268)
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1275`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1275)
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1635`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1635)
- [`beacon_node/beacon_chain/src/attestation_verification.rs:609`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L609)

**Skeptic check.** Confirmed verify_head_block_is_known runs in verify_early_checks of both attestation kinds and rejects HeadBlockFinalized, and target.root must be in fork choice before with_committee_cache. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@4020d1306](https://github.com/sigp/lighthouse/commit/4020d13064fb), [teku#7137](https://github.com/Consensys-Incorporated/teku/pull/7137), [nimbus#2361](https://github.com/status-im/nimbus-eth2/pull/2361), [prysm#1623](https://github.com/OffchainLabs/prysm/pull/1623)

</details>


<a id="attestation_processing-043"></a>
<details>
<summary><b>attestation_processing-043</b> Drop attestations older than previous epoch early — <i>implemented · medium · S · cpu, memory, bandwidth</i></summary>

**Idea.** Drop received attestations older than about one epoch (previous epoch) before queueing, fork-choice processing, pool insertion or re-gossip, rather than using the finalized slot as cutoff. This keeps queues and the pool small when finality lags.

**Impact.** Attestations older than the previous epoch fail PastSlot as the first check, before reprocess queueing, fork choice, pool insertion or re-gossip.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:1295`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1295)
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1334`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1334)
- [`beacon_node/beacon_chain/src/attestation_verification.rs:919`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L919)
- [`beacon_node/beacon_chain/src/attestation_verification.rs:540`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L540)

**Skeptic check.** verify_propagation_slot_range is the first check for both unaggregated and aggregate attestations, so stale ones never reach the reprocess queue or pool; they do sit briefly in the beacon processor gossip queue, which is the same as the source PRs. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@e1021e36b](https://github.com/ChainSafe/lodestar/commit/e1021e36b14a), [prysm#1905](https://github.com/OffchainLabs/prysm/pull/1905)

</details>


<a id="attestation_processing-044"></a>
<details>
<summary><b>attestation_processing-044</b> Reject far-future target epochs by clock — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Reject attestations whose target epoch is beyond the current clock epoch before loading or advancing the target state, so a crafted attestation cannot force processing many empty slots.

**Impact.** target.epoch must equal the slot's epoch and the slot must be within clock + disparity, so no far-future target can force state advances.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:909`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L909)
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1303`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1303)
- [`beacon_node/beacon_chain/src/attestation_verification.rs:546`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L546)
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:389`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L389)

**Skeptic check.** Both checks run before any state access on both gossip paths; additionally with_cached_shuffling bounds advances via the head_block_epoch check and import_max_skip_slots. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#7169](https://github.com/OffchainLabs/prysm/pull/7169)

</details>


<a id="attestation_processing-045"></a>
<details>
<summary><b>attestation_processing-045</b> Check target block in fork choice before work — <i>implemented · medium · S · cpu</i></summary>

**Idea.** Before processing a queued attestation, check that its target/beacon block is known to fork choice and skip work that is certain to fail.

**Impact.** Head and target blocks are looked up in fork choice (not the DB) before committee work; queued attestations are released only on block import into fork choice and re-run the same checks.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:1251`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1251)
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1635`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1635)
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:950`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L950)

**Skeptic check.** Lighthouse uses fork choice (plus early attester cache) rather than DB presence, which is exactly what prysm#15547 fixed; reprocessed attestations go through verify_early_checks again. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#15547](https://github.com/OffchainLabs/prysm/pull/15547)

</details>


<a id="attestation_processing-046"></a>
<details>
<summary><b>attestation_processing-046</b> Early return on source checkpoint mismatch — <i>implemented · low · S · cpu</i></summary>

**Idea.** In participation flag computation, return as soon as the source checkpoint does not match, skipping the target and head checks.

**Impact.** Block-root lookups are skipped on a source mismatch. Only the cheap Gloas payload-availability bit check runs before the error.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/common/get_attestation_participation.rs:36-37`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/get_attestation_participation.rs#L36-L37) target root lookup guarded by is_matching_source &amp;&amp;
- [`consensus/state_processing/src/common/get_attestation_participation.rs:68-70`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/get_attestation_participation.rs#L68-L70) head lookup guarded by is_matching_target
- [`consensus/state_processing/src/common/get_attestation_participation.rs:72-74`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/get_attestation_participation.rs#L72-L74) returns IncorrectAttestationSource

**Skeptic check.** PR 4270 itself was closed unmerged, but the current code gets the same effect with short-circuit &amp;&amp; on is_matching_source. The earlier verdict is right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#4270](https://github.com/sigp/lighthouse/pull/4270)

</details>


<a id="attestation_processing-047"></a>
<details>
<summary><b>attestation_processing-047</b> Cheap rejection when attestation queues overflow — <i>partial · low · S · cpu, disk, latency</i></summary>

**Idea.** Size attestation queues generously and, on rejection, drop quietly with a cheap log instead of an expensive fallback path, so overload does not amplify CPU and disk load.

**Gap in Lighthouse.** Queues are sized generously and drop in O(1) with no fallback path, but work_queue.rs push logs error! on every drop with no debounce. Debounce it in FifoQueue/LifoQueue::push as the reprocess queue does.

**Impact.** Avoids one log line per dropped message during overload; negligible CPU on normal nodes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_queue.rs:48-59`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_queue.rs#L48-L59) push drops with error! when full
- [`beacon_node/beacon_processor/src/scheduler/work_queue.rs:357`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_queue.rs#L357) attestation_queue sized by validator count
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:595-604`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L595-L604) reprocess queue drops with debounced log

**Sources.** [teku#9258](https://github.com/Consensys-Incorporated/teku/pull/9258)

</details>


<a id="attestation_processing-048"></a>
<details>
<summary><b>attestation_processing-048</b> Bounded pending set instead of task per attestation — <i>n/a · low · S · cpu, memory</i></summary>

**Idea.** Keep unprocessed pending attestations in one bounded concurrent set with an expiry and process them from a single loop, instead of spawning a task/goroutine per attestation.

**Impact.** Goroutine-per-attestation is a Caplin pattern; Lighthouse already uses a single loop with bounded queues and expiry.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:1285-1292`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1285-L1292) attestations go into bounded queues drained by one processor loop
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:84`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L84) reprocess cap 16384 with DelayQueue expiry

**Sources.** [caplin#9246](https://github.com/erigontech/erigon/pull/9246)

</details>


<a id="attestation_processing-049"></a>
<details>
<summary><b>attestation_processing-049</b> Size attestation queues for many-validator bursts — <i>implemented · low · S · cpu, memory, latency</i></summary>

**Idea.** Size the pending, gossip attestation, aggregate and reprocess queues for the validator set and subnet subscriptions (configurable), so bursts are not dropped, and drain queues in batches when idle.

**Impact.** Attestation and unknown-block attestation queues scale with active validators per slot (overprovisioned); work is drained in configurable batches of 64.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_queue.rs:335`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_queue.rs#L335)
- [`beacon_node/beacon_processor/src/scheduler/work_queue.rs:357`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_queue.rs#L357)
- [`beacon_node/beacon_processor/src/lib.rs:82`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L82)
- [`beacon_node/beacon_processor/src/lib.rs:110`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L110)
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:84`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L84)

**Skeptic check.** Confirmed BeaconProcessorQueueLengths::from_state sizing and configurable batch sizes; aggregate queue is fixed 4096, which exceeds a slot's worth of aggregates. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#12485](https://github.com/OffchainLabs/prysm/pull/12485), [teku#9229](https://github.com/Consensys-Incorporated/teku/pull/9229), [lighthouse#2535](https://github.com/sigp/lighthouse/pull/2535), [nimbus#2268](https://github.com/status-im/nimbus-eth2/pull/2268), [lighthouse#2506](https://github.com/sigp/lighthouse/pull/2506)

</details>


<a id="attestation_processing-050"></a>
<details>
<summary><b>attestation_processing-050</b> Drop expired attestations from reprocess queue — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** When an attestation expires in the reprocess queue, drop it instead of re-queueing, so an overloaded node does not death-spiral.

**Impact.** The re-queue loop the PR targeted is gone: an expired attestation gets one final verification attempt with reprocessing narrowed, and fails fast on UnknownHeadBlock before signature work. A literal drop-on-expiry would save only that cheap final attempt.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:53`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L53) QUEUED_ATTESTATION_DELAY 12s
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:1221-1260`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L1221-L1260) ReadyAttestation removes the entry and try_sends it once to ready_work_tx (dropped with 'Ignored scheduled attestation' when full)
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:85-121`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L85-L121) ReprocessAllowance; next_requeue always narrows to None so a message cannot loop
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:2880-2930`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L2880-L2930) UnknownHeadBlock requeue only if allows_block(), closure carries next_requeue()

**Skeptic check.** Verified the expiry handler and the ReprocessAllowance narrowing on the gossip aggregate/unaggregate paths. Earlier evidence was right; the cited allow_reprocess lines (2496/2524) are for light-client updates, but the attestation path uses the equivalent ReprocessAllowance enum.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#2609](https://github.com/sigp/lighthouse/pull/2609)

</details>


<a id="attestation_processing-051"></a>
<details>
<summary><b>attestation_processing-051</b> Remove failed attestations from pending queue — <i>n/a · low · S · cpu</i></summary>

**Idea.** Remove an attestation that fails verification from the pending queue so it is not retried and re-verified.

**Impact.** Lighthouse keeps no retry set: a failed attestation is verified once; the reprocess queue holds only unknown-block items, removed on release.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:1221-1250`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L1221-L1250) queued entries removed from maps on release
- [`beacon_node/beacon_processor/src/lib.rs:277-289`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L277-L289) released work processed once

**Sources.** [prysm#3704](https://github.com/OffchainLabs/prysm/pull/3704)

</details>


<a id="attestation_processing-052"></a>
<details>
<summary><b>attestation_processing-052</b> Deduplicate pending aggregates in queue — <i>partial · low · S · cpu, latency</i></summary>

**Idea.** Do not queue a pending aggregate if an equal one (same data and aggregation bits, any aggregator index) is already queued for that block root, so one aggregate per committee is processed and rebroadcast.

**Gap in Lighthouse.** queue_awaiting_attestation stores every unknown-block aggregate with no check for an equal (data, bits) one already queued for that root, so identical aggregates from different aggregators all take reprocess slots (shared 16384 cap) and are all released together; is_known_subset only dedups against already-verified aggregates, so duplicates processed concurrently (or in one batch_verify_aggregated_attestations batch) are each indexed and signature-verified before verify_late_checks rejects all but the first.

**Impact.** Saves BLS verifications and queue slots for duplicate aggregates arriving before their block; rebroadcast is already single.

**Best measured result.** Reduces queue from one aggregate per aggregator to at best 64 (MAX_COMMITTEES_PER_SLOT); no timing numbers (pr:prysm#16153)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:590`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L590)
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:950`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L950)
- [`beacon_node/beacon_chain/src/attestation_verification.rs:570`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L570)
- [`beacon_node/beacon_chain/src/attestation_verification.rs:783`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L783)
- [`beacon_node/beacon_chain/src/attestation_verification/batch.rs:40`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification/batch.rs#L40)

**Skeptic check.** observed_aggregates subset check is real and prevents duplicate rebroadcast and, for sequentially processed items, skips signature work; but it does not dedup at enqueue time in the reprocess queue nor within a concurrent batch. Earlier evidence cited a related post-verification mechanism, not pending-queue dedup.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [prysm#7326](https://github.com/OffchainLabs/prysm/pull/7326), [prysm#16153](https://github.com/OffchainLabs/prysm/pull/16153)

</details>


<a id="attestation_processing-053"></a>
<details>
<summary><b>attestation_processing-053</b> Park unknown-root attestations from raw bytes — <i>not · medium · M · cpu, latency</i></summary>

**Idea.** Extract slot and block root from the serialized attestation bytes first and park unknown-root attestations in a bounded map for reprocessing on block arrival, instead of fully deserialising and validating them first.

**Gap in Lighthouse.** No raw-byte peek of slot/beacon_block_root before SSZ decode. Lighthouse would need to read the fixed offsets of SingleAttestation in pubsub decode or the gossip handler and park unknown-root messages before decode (including signature point decompression).

**Impact.** Small: post-Electra gossip attestations are fixed-size SingleAttestation, so the only real saving is G2 point decompression for attestations with unknown roots; the reprocess queue already parks them before signature verification.

**Best measured result.** up to 16,000 attestations reprocessed at once previously (pr:lodestar#5327)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/pubsub.rs:254`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L254) SingleAttestation::from_ssz_bytes runs on every gossip attestation before any root check
- [`crypto/bls/src/generic_signature.rs:145-149`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/generic_signature.rs#L145-L149) signature bytes are decompressed (Sig::deserialize) during that decode
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:2874`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L2874) UnknownHeadBlock is reached only after decode and early verification

**Second check.** Checked pubsub.rs decode for every topic and the bls signature deserialize path; no byte-offset peek or pre-decode diversion exists anywhere, so the verdict stands.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [lodestar#5327](https://github.com/ChainSafe/lodestar/pull/5327)

</details>


<a id="attestation_processing-054"></a>
<details>
<summary><b>attestation_processing-054</b> Queue unknown-block attestations, release on block import — <i>implemented · medium · S · cpu, latency, bandwidth</i></summary>

**Idea.** Hold attestations whose block root is unknown in a bounded queue indexed by missing root (and wake-up slot), reusing decoded data, request the block, and release them on block import or slot tick. This replaces dropping them or retrying each on a fixed timer.

**Impact.** none needed

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:2874-2930`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L2874-L2930) UnknownHeadBlock sends SyncMessage::UnknownBlockHashFromAttestation and queues UnknownBlockAggregate/UnknownBlockUnaggregate with the decoded attestation in a closure
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:84`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L84) MAXIMUM_QUEUED_ATTESTATIONS 16_384
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:620-632`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L620-L632) per-root index awaiting_attestations_per_root plus delay key
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:931-975`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L931-L975) BlockImported releases all queued attestations for that root
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:53`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L53) QUEUED_ATTESTATION_DELAY 12s expiry

**Skeptic check.** Verified the gossip path queues the decoded attestation per missing root, triggers a block lookup, and releases on BlockImported with a 12s expiry and a 16k bound. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@bf2b3d061](https://github.com/ChainSafe/lodestar/commit/bf2b3d061c12), [lodestar#5286](https://github.com/ChainSafe/lodestar/pull/5286), [lighthouse#2319](https://github.com/sigp/lighthouse/pull/2319), [prysm#16909](https://github.com/OffchainLabs/prysm/pull/16909), [prysm#9679](https://github.com/OffchainLabs/prysm/pull/9679)

</details>


<a id="attestation_processing-055"></a>
<details>
<summary><b>attestation_processing-055</b> Per-slot attestation data cache for API — <i>partial · low · S · cpu, latency</i></summary>

**Idea.** Serve validator attestation-data requests for a slot from a small per-slot cache filled once from fork choice, instead of recomputing from state per request.

**Gap in Lighthouse.** No per-slot memo of attestation data: each request rebuilds it from the head snapshot (cheap). Could add a (slot,index)-keyed cache in produce_unaggregated_attestation, cleared on head change.

**Impact.** Saves microseconds per validator-client request; only the rare epoch-boundary state advance is costly and it is not cached across requests.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/early_attester_cache.rs:175`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/early_attester_cache.rs#L175) try_attest, single entry for newest head block
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2025-2039`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2025-L2039) used first in produce_unaggregated_attestation
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2063`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2063) else reads head snapshot; advanced hot state only if request epoch differs

**Sources.** [prysm#13286](https://github.com/OffchainLabs/prysm/pull/13286)

</details>


<a id="attestation_processing-056"></a>
<details>
<summary><b>attestation_processing-056</b> Cache new head&#x27;s attestation data before import finishes — <i>implemented · low · S · latency</i></summary>

**Idea.** Cache the block, attestation data and checkpoints for a block about to become head so attestations can be produced (and blocks served) before DB import or the head state update completes.

**Impact.** Attestations and block serving work before DB import and head update finish.

**Best measured result.** Head state update took up to a second (pr:caplin#12856)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:4545-4590`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4545-L4590) import_block adds the new head to early_attester_cache (block, proto block, state-derived checkpoints) before DB write and head update, also emits the head SSE event
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2025-2039`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2025-L2039) produce_unaggregated_attestation serves from early_attester_cache.try_attest first
- [`beacon_node/http_api/src/block_id.rs:132`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L132) and :280 API serves blocks from early_attester_cache
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:705`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L705) RPC blocks_by_root serves from early_attester_cache
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1640`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1640) gossip verification accepts targets in the early cache

**Skeptic check.** Confirmed the cache is filled before the DB write and used for attestation production, API and RPC block serving. Optimistic heads are excluded on purpose, which is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#12856](https://github.com/erigontech/erigon/pull/12856), [lighthouse#2872](https://github.com/sigp/lighthouse/pull/2872)

</details>


<a id="attestation_processing-057"></a>
<details>
<summary><b>attestation_processing-057</b> Serve attestation data from state cache, not locked cache — <i>implemented · low · S · latency, cpu</i></summary>

**Idea.** Remove a dedicated globally locked attester cache and serve attestation data from an advanced hot state in the state cache with committee caches built, avoiding write-lock contention on attestation production.

**Impact.** No global write-locked attester cache on attestation production; data comes from the head snapshot or the state cache.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2010-2200`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2010-L2200) produce_unaggregated_attestation: early_attester_cache, short head read, else get_advanced_hot_state + build_committee_cache
- [`beacon_node/beacon_chain/src`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src) (no attester_cache.rs; only early_attester_cache.rs remains)

**Skeptic check.** Confirmed AttesterCache is gone and the non-head-epoch path reads an advanced hot state from the store. Earlier evidence correct (line number was 2010, not 2161).

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#8469](https://github.com/sigp/lighthouse/pull/8469)

</details>


<a id="attestation_processing-058"></a>
<details>
<summary><b>attestation_processing-058</b> Cache attestation committee schedule per epoch — <i>implemented · low · S · cpu</i></summary>

**Idea.** When producing attestations for many validators, compute the committee/attestation schedule once per epoch and slot and reuse it instead of recomputing per validator.

**Impact.** Committee schedule is built once per epoch and duties are O(1) per validator lookups.

**Best measured result.** 330 s to ~17 s per block, 1.5M validators (pr:teku#7491)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:2619-2627`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2619-L2627) get_attestation_duties reads per-validator duty from the epoch CommitteeCache
- [`beacon_node/http_api/src/attester_duties.rs:61`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L61) cached_attestation_duties and :143 build_committee_cache once per epoch for all requested validators
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:315-480`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L315-L480) committee caches are shared per (decision root, epoch)

**Skeptic check.** The source PR (teku#7491) speeds up a benchmark block generator; on the real duty and production paths Lighthouse already computes committees once per epoch through CommitteeCache. The earlier verdict holds.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#7491](https://github.com/Consensys-Incorporated/teku/pull/7491)

</details>


<a id="attestation_processing-059"></a>
<details>
<summary><b>attestation_processing-059</b> Reuse attester index from validation in op pool — <i>partial · low · S · cpu</i></summary>

**Idea.** Cache the single attester index found during unaggregated attestation validation and reuse it in the op pool instead of rescanning the aggregation bitfield.

**Gap in Lighthouse.** Unaggregated attestations go to the naive aggregation pool, not the op pool. NaiveAggregationPool insert (AggregatedAttestationMap::insert) recomputes the single set bit with set_aggregation_bits(), although single_attestation_to_attestation already computed that position during validation. Pass the committee position from VerifiedUnaggregatedAttestation into add_to_naive_aggregation_pool.

**Impact.** Saves one bitfield scan plus a small Vec allocation per gossip/API unaggregated attestation; small (committee is a few hundred bits).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/single_attestation.rs:18-31`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/single_attestation.rs#L18-L31) single_attestation_to_attestation finds the committee position (aggregation_bit) during validation
- [`beacon_node/beacon_chain/src/naive_aggregation_pool.rs:257-265`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/naive_aggregation_pool.rs#L257-L265) insert rescans the bitfield via set_aggregation_bits().iter().at_most_one()
- [`consensus/types/src/attestation/attestation.rs:368-378`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/attestation/attestation.rs#L368-L378) set_aggregation_bits iterates every bit and allocates a Vec
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2699-2715`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2699-L2715) add_to_block_inclusion_pool reuses attesting_indices (aggregates only)

**Skeptic check.** Earlier evidence looked at the op pool, which only takes aggregates with indices passed through; the Lodestar case (single attester bit re-derived in the pool) is exactly the naive aggregation pool path, which still rescans.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lodestar#7209](https://github.com/ChainSafe/lodestar/pull/7209)

</details>


<a id="attestation_processing-060"></a>
<details>
<summary><b>attestation_processing-060</b> Subtract absent keys from committee aggregate pubkey — <i>not · medium · M · cpu</i></summary>

**Idea.** Cache one aggregate pubkey per committee and for high-participation attestations subtract the absent validators' keys instead of loading and adding every attester key.

**Gap in Lighthouse.** No per-committee aggregate pubkey cache and no subtract-absent path. It would need a cache keyed by shuffling id and committee, a negate-and-add step in crypto/bls (blst has no subtract), and use in the attestation signature-set builders.

**Impact.** Fewer G1 additions in block-import and aggregate attestation signature checks at high participation; Prysm measured key aggregation dropping from 56 to 11.5 ms per block.

**Best measured result.** ExecuteStateTransition CPU 131.1 to 92.3 ms per block; AggregateKeyFromIndices 56.0 to 11.5 ms; keys loaded 46,693 to 7,159 (pr:prysm#17799)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/signature_sets.rs:327-356`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/signature_sets.rs#L327-L356) indexed_attestation_signature_set_from_pubkeys loads every attester key
- [`consensus/state_processing/src/per_block_processing/signature_sets.rs:814-818`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/signature_sets.rs#L814-L818) committee pubkeys are filtered per participant (sync committee only)
- [`consensus/types/src/state/beacon_state.rs:1843`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1843) the only cached AggregatePublicKey is the sync committee aggregate
- [`crypto/bls/src/impls/blst.rs:102`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L102) aggregation always adds the participant keys

**Second check.** Searched beacon_node, consensus and crypto for AggregatePublicKey and committee pubkey caches; the only hits are the sync committee aggregate and the generic aggregate path, so the verdict stands.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [prysm#17799](https://github.com/OffchainLabs/prysm/pull/17799)

</details>


<a id="attestation_processing-061"></a>
<details>
<summary><b>attestation_processing-061</b> Separate worker for batched attestation verification — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Verify batch-arriving attestations (e.g. from the HTTP API) on a dedicated worker separate from the gossip attestation worker so they do not block each other.

**Impact.** API attestation batches run in their own queue on the shared worker pool, so they do not serialize with gossip attestation batches.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/publish_attestations.rs:137-140`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_attestations.rs#L137-L140) publish_attestations runs as blocking_task(Priority::P0)
- [`beacon_node/beacon_processor/src/lib.rs:481`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L481) Work::ApiRequestP0, own api_request_p0_queue
- [`beacon_node/beacon_processor/src/lib.rs:956`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L956) api_request_p0_queue popped ahead of gossip attestation queues (1025)

**Skeptic check.** Verified the API work type and its scheduling. Unlike Grandine, the API batch is verified one by one (verify_unaggregated_attestation_for_gossip per item, no batch signature verification), but that is a separate idea; the separation from the gossip worker holds.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine@5118229b6](https://github.com/grandinetech/grandine/commit/5118229b6fcf)

</details>


<a id="attestation_processing-062"></a>
<details>
<summary><b>attestation_processing-062</b> Compute cache misses outside the lock — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** In shared RwLock caches such as the committee cache, check for hits under the read lock, build the value outside any lock and take the write lock only to insert with a re-check.

**Impact.** Committee cache misses no longer block other readers; the attester cache that PR 8463 targeted no longer exists.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:347-354`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L347-L354) read lock for hits
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:356-377`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L356-L377) write lock only to re-check and create a promise, then dropped
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:430-487`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L430-L487) state load, advance and committee build outside the lock, short write to insert
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:188-197`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L188-L197) proposer cache uses per-epoch OnceCell get_or_try_init outside the Mutex

**Skeptic check.** Read with_cached_shuffling end to end: hit under read lock, promise under write lock, compute unlocked. Earlier evidence correct; PR 8463 was closed because the cache was removed.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#8463](https://github.com/sigp/lighthouse/pull/8463)

</details>


<a id="attestation_processing-063"></a>
<details>
<summary><b>attestation_processing-063</b> Remove tracing spans from per-attestation hot paths — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Remove tracing spans from per-attestation hot paths like indexed-attestation conversion, which run tens of thousands of times per slot interval.

**Impact.** No per-attestation spans on gossip verification, indexing, naive pool or fork-choice on_attestation.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs) (no instrument/span usage)
- [`consensus/state_processing/src/common/get_attesting_indices.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/get_attesting_indices.rs) (no spans)
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:686`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L686),1531,1913,3780,4239+ #[instrument] only on column/block/envelope/bid handlers, not process_gossip_attestation(s)/aggregate
- [`consensus/fork_choice/src/fork_choice.rs:567`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L567),626,785 spans only on get_head, get_proposer_head, on_block (not on_attestation)

**Skeptic check.** Searched the whole attestation path, including gossip handlers, fork choice and pools; spans exist only on per-block or per-request functions. Earlier verdict correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#12687](https://github.com/OffchainLabs/prysm/pull/12687)

</details>


<a id="attestation_processing-064"></a>
<details>
<summary><b>attestation_processing-064</b> Skip re-validating own produced attestations — <i>n/a · low · S · cpu, latency</i></summary>

**Idea.** Do not re-validate a locally produced attestation (latest state load plus processAttestation) before adding it to the op pool and publishing.

**Impact.** Lighthouse's BN does not sign its own attestations; the VC submits them via API and the single verification is required.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2010`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2010) produce_unaggregated_attestation only builds data; signing is in the validator client
- [`beacon_node/http_api/src/publish_attestations.rs:62`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_attestations.rs#L62) submitted attestations are verified once before publish

**Sources.** [lodestar@977bf472b](https://github.com/ChainSafe/lodestar/commit/977bf472b915)

</details>


<a id="attestation_processing-065"></a>
<details>
<summary><b>attestation_processing-065</b> Attest as soon as the head block is processed — <i>implemented · medium · S · latency, bandwidth</i></summary>

**Idea.** Produce and publish own attestations as soon as the slot's head block is processed, removing artificial waits for the fixed attestation time in the slot, to cut propagation latency.

**Impact.** none needed

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/beacon_node_fallback/src/beacon_head_monitor.rs:63-84`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/beacon_node_fallback/src/beacon_head_monitor.rs#L63-L84) head_event_or_deadline returns on the current-slot head event or the deadline
- [`validator_client/validator_services/src/attestation_service.rs:212-216`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L212-L216) attestation loop waits on the head event, not a fixed 1/3 timer
- [`validator_client/validator_services/src/attestation_service.rs:273-306`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L273-L306) fetches attestation data from the BN that sent the head and checks the block root
- [`validator_client/src/cli.rs:511`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/src/cli.rs#L511) disable_beacon_head_monitor flag means monitor is on by default
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4593`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4593) head SSE event emitted during import, before DB write

**Skeptic check.** Verified the VC attests as soon as a current-slot head SSE event arrives, enabled by default, with fallback to the deadline. The BN emits the head event from the early-attester path, so latency is minimal.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#764](https://github.com/ChainSafe/lodestar/pull/764), [lodestar#788](https://github.com/ChainSafe/lodestar/pull/788), [caplin#14128](https://github.com/erigontech/erigon/pull/14128)

</details>


<a id="attestation_processing-066"></a>
<details>
<summary><b>attestation_processing-066</b> Produce payload attestations on envelope receipt — <i>implemented · low · S · latency</i></summary>

**Idea.** Produce and broadcast payload attestations immediately once the execution payload envelope is received and validated, instead of waiting for the next scheduled step.

**Impact.** PTC attestations are produced as soon as the BN reports the payload available, with deadline fallback; on by default.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/payload_attestation_service.rs:141-157`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/payload_attestation_service.rs#L141-L157) select between deadline and PayloadAvailable event
- [`validator_client/validator_services/src/payload_attestation_service.rs:170-190`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/payload_attestation_service.rs#L170-L190) early failure retries at deadline
- [`validator_client/beacon_node_fallback/src/beacon_head_monitor.rs:286-300`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/beacon_node_fallback/src/beacon_head_monitor.rs#L286-L300) ExecutionPayloadAvailable SSE event feeds the channel
- [`validator_client/src/config.rs:144`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/src/config.rs#L144) enable_payload_available_monitor defaults to true

**Skeptic check.** Verified the trigger, the SSE source and the default config. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#8558](https://github.com/status-im/nimbus-eth2/pull/8558)

</details>


<a id="attestation_processing-067"></a>
<details>
<summary><b>attestation_processing-067</b> Gossip own attestations before fork-choice validity — <i>implemented · low · S · latency</i></summary>

**Idea.** Publish locally produced attestations immediately even if they are not yet valid for fork choice, deferring only the fork-choice application.

**Impact.** Local unaggregated attestations and aggregates are gossiped independently of fork-choice validity.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/publish_attestations.rs:76-88`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_attestations.rs#L76-L88) network publish right after gossip verification
- [`beacon_node/http_api/src/publish_attestations.rs:99-117`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_attestations.rs#L99-L117) apply_attestation_to_fork_choice after publish; its error does not undo gossip
- [`beacon_node/http_api/src/validator/mod.rs:1344-1360`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L1344-L1360) aggregates published before fork-choice application

**Skeptic check.** Checked both the unaggregated and aggregate API paths: publish precedes fork-choice application on both. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#2525](https://github.com/Consensys-Incorporated/teku/pull/2525)

</details>


<a id="attestation_processing-068"></a>
<details>
<summary><b>attestation_processing-068</b> FFG/LMD consistency check from fork choice — <i>implemented · low · S · cpu, disk, latency</i></summary>

**Idea.** Check attestation FFG/LMD consistency against in-memory fork choice data instead of database lookups and ancestor walks.

**Impact.** None left: gossip and fork choice FFG/LMD consistency checks are in-memory proto_array lookups.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:1244`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1244) verify_head_block_is_known reads ProtoBlock from fork_choice_read_lock().get_block (or early_attester_cache)
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1379`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1379) verify_attestation_target_root derives the expected target from ProtoBlock.target_root / root, no ancestor walk
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1519`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1519) finalized-descendant check via fork_choice.is_finalized_checkpoint_or_descendant (proto_array)
- [`consensus/fork_choice/src/fork_choice.rs:1197`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1197) validate_on_attestation uses proto_array

**Skeptic check.** Verified the gossip path (unaggregated and aggregate early checks) uses the ProtoBlock target_root, matching prysm#13250 which replaced DB ancestor loops with fork choice lookups. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#13250](https://github.com/OffchainLabs/prysm/pull/13250)

</details>


<a id="attestation_processing-069"></a>
<details>
<summary><b>attestation_processing-069</b> Bound ancestry walks with canonical slot index — <i>n/a · low · S · cpu, latency, disk</i></summary>

**Idea.** Replace unbounded parent-chain walks in attestation validation with an O(1) check against a canonical slot-to-root index, stopping at the first canonical block above the ancestor's slot.

**Impact.** Ancestry walks run on the in-memory proto-array node vector, not DB header reads, so the pathological cost does not occur.

**Best measured result.** ~119,000 header reads per attestation when finality lagged (pr:ethlambda#610)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fork_choice/src/fork_choice.rs:509`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L509) get_ancestor on in-memory proto_array
- [`consensus/proto_array/src/proto_array_fork_choice.rs:1284`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L1284)

**Sources.** [ethlambda#610](https://github.com/lambdaclass/ethlambda/pull/610)

</details>


<a id="attestation_processing-070"></a>
<details>
<summary><b>attestation_processing-070</b> Use cached state of attested block root for validation — <i>implemented · medium · S · cpu, memory</i></summary>

**Idea.** For gossip attestations, look up the state of the attestation's beacon_block_root in the state cache and validate against it (when it can serve the target's committees) rather than regenerating a checkpoint state for the target epoch, avoiding extra epoch transitions.

**Impact.** Committees come from a decision-root-keyed cache filled at block import, so gossip validation does not regenerate checkpoint states.

**Best measured result.** "6-7 epoch transitions in just 2 minutes" before; "exactly 1 epoch transition per epoch" after (pr:lodestar#3532)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:1617-1659`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1617-L1659) map_attestation_committees uses with_committee_cache(target.root, epoch)
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:330-353`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L330-L353) shuffling id from the fork-choice block, read-lock hit needs no state
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5198-5230`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5198-L5230) import_block_update_shuffling_cache inserts each imported block's committee caches
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:400-447`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L400-L447) on a miss reuses head state or get_advanced_hot_state, and does partial_state_advance only when the state is 2+ epochs behind

**Skeptic check.** Lighthouse does not look up the beacon_block_root state, but it reaches the same effect differently: committees are cached by shuffling decision root and filled during block import. A miss uses next-epoch lookahead and needs no epoch transition unless the target block is 2+ epochs old.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#3532](https://github.com/ChainSafe/lodestar/pull/3532), [teku#7142](https://github.com/Consensys-Incorporated/teku/pull/7142)

</details>


<a id="attestation_processing-071"></a>
<details>
<summary><b>attestation_processing-071</b> Validate attestations against a few shared states — <i>implemented · medium · S · cpu, memory</i></summary>

**Idea.** Pick the validation state from a small shared set (head, justified, finalized, or earliest state per fork with the needed committees) rather than one state per attested block, so only about three states, at most one per fork per epoch, are needed.

**Impact.** All attestations whose blocks share a decision root use one committee cache, which is at least as good as a set of about three shared states.

**Best measured result.** up to 32x fewer states required (pr:teku#5205)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:330-345`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L330-L345) BlockShufflingIds maps any block to its (decision root, epoch) shuffling id
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:25`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L25) DEFAULT_CACHE_SIZE 16, head shufflings protected from eviction (update_head_shuffling_ids)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5198-5230`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5198-L5230) cache filled at block import

**Skeptic check.** Verified that validation needs a committee cache per fork per epoch, not a state per attested block. This matches or beats the teku shared-state approach.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#5205](https://github.com/Consensys-Incorporated/teku/pull/5205)

</details>


<a id="attestation_processing-072"></a>
<details>
<summary><b>attestation_processing-072</b> Use the block&#x27;s own state for its included attestations — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** When processing attestations included in a block, validate them with that block's pre-state already in hand instead of fetching or computing a separate state for each attestation.

**Impact.** None left: block attestations go to state processing and fork choice with the block's own state and cached indices.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/process_operations.rs:242`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L242) verify_attestation_for_block_inclusion uses the block pre-state
- [`beacon_node/beacon_chain/src/block_verification.rs:1763`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1763) fork choice on_attestation for block attestations uses consensus_context.get_indexed_attestation(&amp;state, ...) with the block's post-processing state
- [`consensus/state_processing/src/consensus_context.rs:161`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/consensus_context.rs#L161) get_indexed_attestation caches per-block

**Skeptic check.** grandine 6d9994dde applies block attestations to fork choice with the block's state instead of a per-attestation target state. Lighthouse does the same in block_verification.rs (no shuffling cache or state lookup per attestation). Earlier verdict upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine@6d9994dde](https://github.com/grandinetech/grandine/commit/6d9994dde75a)

</details>


<a id="attestation_processing-073"></a>
<details>
<summary><b>attestation_processing-073</b> Skip state roots when advancing state for shuffling — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** When a state must be advanced to a future slot only to obtain shuffling for attestation production, run per-slot processing without computing state roots, and serve attestation production from cached head data.

**Impact.** Attestation production uses cached head data and skips state-root hashing when it must advance.

**Best measured result.** orders of magnitude faster attestation production in best case (pr:lighthouse#838)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2025-2039`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2025-L2039) early_attester_cache.try_attest first
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2125-2140`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2125-L2140) head-state fast path when head is in the request epoch
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2155-2170`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2155-L2170) otherwise get_advanced_hot_state plus partial_state_advance with a known state root
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:436-447`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L436-L447) shuffling misses also use partial_state_advance
- [`consensus/state_processing/src/state_advance.rs:72`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/state_advance.rs#L72) partial_state_advance skips state-root computation

**Skeptic check.** Verified that production and shuffling misses both advance with partial_state_advance, and that the head and early cache paths avoid advancing at all. This is the Lighthouse PR itself, so the earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#838](https://github.com/sigp/lighthouse/pull/838)

</details>


<a id="attestation_processing-074"></a>
<details>
<summary><b>attestation_processing-074</b> Reuse fetched fork-choice block for committee lookup — <i>not · low · S · cpu, latency</i></summary>

**Idea.** Pass the fork choice block already fetched during attestation verification into the shuffling/committee cache lookup instead of performing a second fork choice lookup under lock.

**Gap in Lighthouse.** Add with_committee_cache_for_block / with_cached_shuffling_for_block taking a ProtoBlock, and have map_attestation_committees fetch the target block once with get_block instead of contains_block, then pass it in.

**Impact.** Saves one fork choice read-lock acquisition plus hash lookup per gossip attestation; micro, small contention gain at high attestation rates.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:1638`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1638) fork_choice_read_lock().contains_block(&amp;target.root)
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:331`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L331) with_cached_shuffling takes fork choice lock again and get_block(head_block_root)
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1645`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1645) caller of with_committee_cache
- upstream PR 9577 is closed unmerged

**Sources.** [lighthouse#9577](https://github.com/sigp/lighthouse/pull/9577)

</details>


<a id="attestation_processing-075"></a>
<details>
<summary><b>attestation_processing-075</b> Dedupe concurrent same-target checkpoint state computations — <i>implemented · medium · S · cpu, memory, latency</i></summary>

**Idea.** Track in-flight checkpoint (target) state computations per target root, with a per-key lock or promise map, so concurrent attestations sharing a target wait on one computation and reuse its cached result, while different targets proceed in parallel.

**Impact.** none needed

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:362-378`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L362-L378) under the write lock, an existing Promise is waited on, else create_promise is called and the lock released before computing
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:103-123`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L103-L123) CacheItem::Promise(Receiver) and wait()
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:36`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L36) and :287-303 MAX_CONCURRENT_PROMISES 2: a third distinct in-flight shuffling is rejected

**Skeptic check.** Confirmed per-shuffling-id promise dedup. Different targets run in parallel only up to 2 at once, and later ones are rejected (MaxCommitteePromises) to bound memory. That is a deliberate cap, not a missing mechanism.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#7659](https://github.com/OffchainLabs/prysm/pull/7659), [prysm#7690](https://github.com/OffchainLabs/prysm/pull/7690), [prysm#7669](https://github.com/OffchainLabs/prysm/pull/7669)

</details>


<a id="attestation_processing-076"></a>
<details>
<summary><b>attestation_processing-076</b> Bound attestation pre-state regeneration concurrency — <i>partial · medium · S · cpu, memory</i></summary>

**Idea.** Gate attestation pre-state regeneration behind a semaphore (limit one) so attestations for different old targets do not each regenerate a state in parallel, and abort early when the request context is cancelled.

**Gap in Lighthouse.** Concurrency is bounded (2, not 1) and duplicate targets are deduplicated, but extra targets are dropped instead of queued, and there is no cancellation of an in-flight state load.

**Impact.** The memory and CPU bound already exists; queueing instead of dropping would only save some attestations on forky networks.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:36`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L36) MAX_CONCURRENT_PROMISES = 2
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:287-297`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L287-L297) create_promise refuses over the cap
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:365`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L365) callers for the same shuffling id wait on the existing promise (dedup)
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:3227-3242`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L3227-L3242) over-cap attestations are dropped with Ignore

**Second check.** Confirmed the promise cap, the same-key wait in with_cached_shuffling and the drop path in gossip_methods; found no extra semaphore or cancellation, so partial stands.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [prysm#17456](https://github.com/OffchainLabs/prysm/pull/17456)

</details>


<a id="attestation_processing-077"></a>
<details>
<summary><b>attestation_processing-077</b> Avoid coarse locks around attestation state work — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Do not hold a global/service mutex across attestation processing or pre-state fetch; do state lookup and committee computation outside the lock and hold it only for small shared updates, relying on thread-safe caches, so concurrent gossip attestations do not serialize.

**Impact.** Gossip attestations verify concurrently; state lookup and committee computation run outside locks, and concurrent misses wait on a promise rather than the cache lock.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:348`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L348) read lock for cache hits
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:375`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L375) promise created under write lock, lock dropped before state load/advance/committee build
- [`beacon_node/beacon_chain/src/attestation_verification.rs:573`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L573) observed_attestations write lock only for the subset check
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1350`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1350) pubkey cache read lock only during signature-set build

**Skeptic check.** Verified with_cached_shuffling drops the shuffling-cache write lock before any state read or committee building; all other locks on the gossip path are short. Earlier verdict correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#3399](https://github.com/OffchainLabs/prysm/pull/3399), [prysm#7656](https://github.com/OffchainLabs/prysm/pull/7656), [prysm#16197](https://github.com/OffchainLabs/prysm/pull/16197)

</details>


<a id="attestation_processing-078"></a>
<details>
<summary><b>attestation_processing-078</b> Incremental per-block vote tally cache — <i>n/a · low · cpu</i></summary>

**Idea.** Maintain, per block root, the set of attesters and total attesting balance updated as attestations arrive, so justification/finalization reads totals instead of re-walking ancestors per attester at the epoch boundary.

**Gap in Lighthouse.** Lighthouse proto-array keeps per-validator latest-vote and applies score deltas; justification totals come from progressive balances cache, not ancestor walks.

**Impact.** Design does not walk ancestors per attester; idea does not apply.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fork_choice/src/fork_choice.rs:1362`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1362) votes applied per validator to proto_array
- [`consensus/proto_array/src/proto_array_fork_choice.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs) vote tracker + delta compute

**Sources.** [prysm#435](https://github.com/OffchainLabs/prysm/pull/435), [prysm#436](https://github.com/OffchainLabs/prysm/pull/436)

</details>


<a id="attestation_processing-079"></a>
<details>
<summary><b>attestation_processing-079</b> Cache attesting indices per attestation — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Cache the committee-derived attesting/indexed indices of an attestation (keyed by attestation data hash plus aggregation bits) so the same attestation's indices are computed once and reused by every caller during block processing and validation.

**Impact.** Per-block indices are computed once and shared by signature verification, processing, fork choice, monitor and slasher.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/consensus_context.rs:161-196`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/consensus_context.rs#L161-L196) get_indexed_attestation HashMap keyed by attestation tree_hash_root
- [`beacon_node/beacon_chain/src/block_verification.rs:1763`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1763) fork choice reuses the context cache
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4987`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4987) validator monitor reuses it
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5094`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5094) slasher reuses it
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:242`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L242) state processing reuses it

**Skeptic check.** Verified that all block-import consumers share the ConsensusContext cache. Caplin#7687 uses a global LRU that also spans gossip and block, and Lighthouse has no cross-path cache, but recomputing from the committee cache is cheap. The teku#3627 scope is per block, so the earlier verdict holds.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#3627](https://github.com/Consensys-Incorporated/teku/pull/3627), [caplin#7687](https://github.com/erigontech/erigon/pull/7687)

</details>


<a id="attestation_processing-080"></a>
<details>
<summary><b>attestation_processing-080</b> Carry indexed attestation through deferral queues — <i>implemented · low · S · cpu</i></summary>

**Idea.** When an attestation is queued for a future slot or later replay, store its computed indexed attestation with it and reuse it on replay into fork choice instead of recomputing attesting indices.

**Impact.** Fork choice delay queue carries indices; other deferral queues defer before any indexing is done.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fork_choice/src/fork_choice.rs:279`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L279) QueuedAttestation stores attesting_indices
- [`consensus/fork_choice/src/fork_choice.rs:1383`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1383) on_attestation queues the indexed form for current-slot attestations
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1255`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1255) UnknownPayloadEnvelope is returned in early checks, before indexing, so the Gloas payload reprocess queue does not throw away computed indices
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:170`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L170) the unknown-block queue re-verifies, and it cannot index before the block is known

**Skeptic check.** Matches teku#1836, which saves the indexed attestation for future-slot application. I also checked the new Gloas UnknownPayload queues: the deferral happens before the committee lookup, so no work is repeated. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#1836](https://github.com/Consensys-Incorporated/teku/pull/1836)

</details>


<a id="attestation_processing-081"></a>
<details>
<summary><b>attestation_processing-081</b> Compute attesting indices once per block attestation — <i>implemented · low · S · cpu</i></summary>

**Idea.** In block attestation processing, derive attesting indices from aggregation bits once and reuse the list for the participation update, the indexed attestation, and statistics instead of recomputing it.

**Impact.** Indices derived once per block attestation via ConsensusContext.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/process_operations.rs:242-259`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L242-L259) indexed_att from verify_attestation_for_block_inclusion drives the participation loop
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:345-389`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L345-L389) same for the Gloas path
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4987`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4987) validator-monitor statistics reuse ctxt cache

**Skeptic check.** Verified the participation update, the indexed attestation and the monitor statistics all read the single cached IndexedAttestation. Earlier verdict upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine@b2c6ffc14](https://github.com/grandinetech/grandine/commit/b2c6ffc14d44)

</details>


<a id="attestation_processing-082"></a>
<details>
<summary><b>attestation_processing-082</b> Pass precomputed committee into attesting-indices derivation — <i>implemented · low · S · cpu</i></summary>

**Idea.** Let the indexed-attestation conversion take an already computed (possibly cached) beacon committee as input, so converting an attestation does not recompute the committee.

**Impact.** Committees are passed in from the shuffling cache or committee cache and are never recomputed.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/common/get_attesting_indices.rs:11`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/get_attesting_indices.rs#L11) base get_indexed_attestation(committee: &amp;[usize], ..)
- [`consensus/state_processing/src/common/get_attesting_indices.rs:57`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/get_attesting_indices.rs#L57) electra get_indexed_attestation(committees: &amp;[BeaconCommittee], ..)
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1617`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1617) map_attestation_committees supplies committees from shuffling cache on gossip
- [`consensus/state_processing/src/consensus_context.rs:170`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/consensus_context.rs#L170) block path uses state committee cache

**Skeptic check.** Same design as prysm#4284. On the block path, get_indexed_attestation_from_state rebuilds only a Vec of committee slices from the cached committee cache, not the shuffling. Earlier verdict upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#4284](https://github.com/OffchainLabs/prysm/pull/4284)

</details>


<a id="attestation_processing-083"></a>
<details>
<summary><b>attestation_processing-083</b> Precompute attesting indices before voted block imports — <i>partial · low · M · cpu, latency</i></summary>

**Idea.** Compute attesting indices for gossip attestations as they arrive, before the voted block is imported, and feed them to fork choice so block import is not delayed by attestation work.

**Gap in Lighthouse.** Attestations whose block is known get indices at gossip verification. Attestations that arrive before their block are parked in the reprocessing queue and fully verified (including indices) only after import. Pre-compute the indexed attestation for UnknownBlock items before parking, and only run signature check and fork-choice apply on release.

**Impact.** Small head-latency gain when attestations beat the block; the burst after import gets slightly cheaper, probably a few ms at most.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:1288`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1288) UnknownHeadBlock error for unknown voted block
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:2874`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L2874) unknown-head attestations are queued
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:132`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L132) UnknownBlockUnaggregate waits for block import
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2710`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2710) indices from gossip verification go to fork choice

**Sources.** [caplin#10085](https://github.com/erigontech/erigon/pull/10085)

</details>


<a id="attestation_processing-084"></a>
<details>
<summary><b>attestation_processing-084</b> Lightweight non-SSZ indexed attestation on hot paths — <i>n/a · low · S · cpu, memory</i></summary>

**Idea.** Represent indexed attestations on hot paths (validation, fork choice, pools, caches) as a plain struct with a vector of indices instead of a tree-backed SSZ object, skip sorting at construction, and convert to SSZ only when needed.

**Impact.** IndexedAttestation is a flat ssz_types VariableList, not a persistent tree, so Teku's tree-backed cost does not exist.

**Best measured result.** Allocations in 50s window 15.56 GB to 12.97 GB (-16.6%); getIndexedAttestation 472 MB to 17 MB (-96.4%); ~52 MB/s less garbage (pr:teku#10599)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/common/get_attesting_indices.rs:25`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/get_attesting_indices.rs#L25) builds a plain VariableList Vec, not a tree-backed milhouse list

**Sources.** [teku#10599](https://github.com/Consensys-Incorporated/teku/pull/10599)

</details>


<a id="attestation_processing-085"></a>
<details>
<summary><b>attestation_processing-085</b> Inline stack storage for aggregation bitfields — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Store attestation aggregation bits in an inline small-vector (e.g. SmallVec&lt;[u8;32]&gt;) so typical attestations need no heap allocation.

**Impact.** Gossip aggregates (one committee, &lt;128 bytes) need no heap allocation. Electra on-chain aggregates span several committees (about 4KB of bits) and spill to the heap, but there are at most 8 per block, which does not matter.

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/ethereum_ssz-ba970959eb75904b/974f78f/ssz/src/bitfield.rs:118 Bitfield bytes: SmallVec&lt;[u8; SMALLVEC_LEN]&gt;
- ~/.cargo/git/checkouts/ethereum_ssz-ba970959eb75904b/974f78f/ssz/src/bitfield.rs:34 SMALLVEC_LEN = 128
- [`consensus/types/src/attestation/attestation.rs:83`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/attestation/attestation.rs#L83) aggregation_bits is BitList

**Skeptic check.** Confirmed the sigp ethereum_ssz rev in Cargo.lock uses SmallVec&lt;[u8;128]&gt;. The 2M-validator comment assumes per-committee bits, so post-Electra multi-committee block aggregates do heap-allocate, but typical attestations do not.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#2182](https://github.com/sigp/lighthouse/pull/2182)

</details>


<a id="attestation_processing-086"></a>
<details>
<summary><b>attestation_processing-086</b> Bitset for validator index sets — <i>partial · low · S · cpu, memory</i></summary>

**Idea.** Use a compact integer-indexed bitset for validator index sets (attesters, seen sets) instead of a general hash set to cut hashing and allocation.

**Gap in Lighthouse.** attesting_indices_electra::get_attesting_indices builds a std HashSet&lt;u64&gt; per committee only to test emptiness and dedup (committee members are already unique): push into the Vec directly. Block-production max-cover (AttMaxCover.fresh_validators_rewards, update_covering_set, covering sets in max_cover.rs) uses HashMap&lt;u64,u64&gt; keyed by validator index, where a bitset or sorted vec would do (nimbus#2267 changed its attestation_pool for this).

**Impact.** Removes SipHash inserts per attester on Electra attestation indexing (gossip aggregates and every block attestation) and speeds up op-pool attestation packing at block production; likely a few percent of those paths.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/observed_attesters.rs:86`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_attesters.rs#L86) EpochBitfield BitVec for seen attesters (done)
- [`consensus/state_processing/src/common/get_attesting_indices.rs:119-138`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/get_attesting_indices.rs#L119-L138) attesting_indices_electra::get_attesting_indices collects each committee's attesters into a SipHash HashSet&lt;u64&gt; on every call (gossip aggregates, block processing)
- [`beacon_node/operation_pool/src/attestation.rs:23`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation.rs#L23) AttMaxCover fresh_validators_rewards: HashMap&lt;u64,u64&gt; keyed by validator index
- [`beacon_node/operation_pool/src/attestation.rs:165-174`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation.rs#L165-L174) update_covering_set does HashMap retain/contains_key per packing round

**Skeptic check.** The gossip seen-attester set is a BitVec, as the earlier evidence said. But the earlier check missed two hot validator-index hash sets: the per-committee HashSet in Electra get_attesting_indices and the op-pool max-cover HashMaps.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [nimbus#2267](https://github.com/status-im/nimbus-eth2/pull/2267)

</details>


<a id="attestation_processing-087"></a>
<details>
<summary><b>attestation_processing-087</b> Size attesting-indices output by set bits — <i>partial · low · S · memory</i></summary>

**Idea.** Allocate the attesting-indices output by the popcount of the aggregation bitlist rather than the full committee length.

**Gap in Lighthouse.** Electra/Gloas get_attesting_indices (attesting_indices_electra) uses vec![] and per-committee HashSet&lt;u64&gt;; pre-size the Vec by aggregation_bits.num_set_bits() and drop the HashSet.

**Impact.** Saves a few allocations per block attestation on Electra; negligible in total.

**Best measured result.** 544 -&gt; 480 B/op (pr:prysm#6508)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/common/get_attesting_indices.rs:30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/get_attesting_indices.rs#L30) Vec::with_capacity(num_set_bits) pre-Electra
- get_attesting_indices.rs:99 Electra uses vec![] and a HashSet per committee

**Sources.** [prysm#6508](https://github.com/OffchainLabs/prysm/pull/6508)

</details>


<a id="attestation_processing-088"></a>
<details>
<summary><b>attestation_processing-088</b> Linear-pass sorted/unique check for indexed attestations — <i>implemented · low · S · cpu</i></summary>

**Idea.** Check that indexed attestation indices are sorted and unique with a single linear pass comparing neighbours, instead of sorting, copying, or building a set.

**Impact.** Negligible; the check is already one linear pass with no sort or set.

**Best measured result.** 227693 ns/op -&gt; 827 ns/op (pr:prysm#7458)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/is_valid_indexed_attestation.rs:38`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/is_valid_indexed_attestation.rs#L38) tuple_windows neighbour check x &lt; y (sorted and unique in one pass)
- [`consensus/state_processing/src/per_block_processing/is_valid_indexed_attestation.rs:21`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/is_valid_indexed_attestation.rs#L21) attesting_indices_to_vec copy

**Skeptic check.** Confirmed the single neighbour pass in is_valid_indexed_attestation, shared by block attestations and attester slashings. Only a Vec copy remains, as the earlier note said.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#3015](https://github.com/OffchainLabs/prysm/pull/3015), [prysm#3060](https://github.com/OffchainLabs/prysm/pull/3060), [prysm#7458](https://github.com/OffchainLabs/prysm/pull/7458)

</details>


<a id="attestation_processing-089"></a>
<details>
<summary><b>attestation_processing-089</b> Fuse index check with pubkey fetch, preallocate — <i>partial · low · S · cpu, memory</i></summary>

**Idea.** When validating indexed attestations, preallocate the pubkey array to the index count and do the sorted/unique check while fetching pubkeys, avoiding intermediate lists and extra passes.

**Gap in Lighthouse.** Preallocation exists, but the sorted check is a separate pass over a copied Vec. Fuse it into indexed_attestation_signature_set's loop and drop the attesting_indices_to_vec() call in is_valid_indexed_attestation.

**Impact.** Saves one Vec&lt;u64&gt; alloc and one pass per attestation in block processing signature setup; small versus BLS cost.

**Best measured result.** 407MB vs 1.17GB allocations; 30% faster (89 to 116 ops/ms) (pr:teku#8941)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/signature_sets.rs:306`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/signature_sets.rs#L306) pubkeys Vec::with_capacity(len)
- [`consensus/state_processing/src/per_block_processing/is_valid_indexed_attestation.rs:18`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/is_valid_indexed_attestation.rs#L18) attesting_indices_to_vec copy, then separate sorted pass

**Sources.** [teku#8941](https://github.com/Consensys-Incorporated/teku/pull/8941)

</details>


<a id="attestation_processing-090"></a>
<details>
<summary><b>attestation_processing-090</b> Lazy BLS signature decompression for gossip attestations — <i>not · medium · M · cpu</i></summary>

**Idea.** Keep gossip attestation signatures compressed on decode and decompress only after cheap checks (and redundancy filters) pass, so unviable or redundant attestations never pay decompression.

**Gap in Lighthouse.** Gossip attestations and aggregates decompress the G2 signature during SSZ decode, before any cheap check. Add a compressed/lazy signature type for the gossip attestation path (the closed #4409/#4567 did this) and decompress only in the batch verifier, after verify_early_checks and the observed_aggregates/observed_attesters filters.

**Impact.** Saves one G2 decompression for each gossip attestation that the cheap checks drop (duplicates, subsets, wrong slot). Only a few percent of gossip CPU.

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/generic_aggregate_signature.rs:166`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/generic_aggregate_signature.rs#L166) deserialize builds the point at once via AggSig::deserialize
- [`crypto/bls/src/impls/blst.rs:250`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L250) blst Signature::from_bytes decompresses the G2 point at SSZ decode
- [`consensus/types/src/attestation/attestation.rs:90`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/attestation/attestation.rs#L90) Attestation.signature is AggregateSignature (decompressed point), not SignatureBytes

**Second check.** Checked the generic bls wrapper and the blst impl for a deferred or cached decompression, and the Attestation types for a SignatureBytes-style field. Only exact duplicate messages skip decode, through gossipsub message-id dedup; that is not this idea.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [lighthouse#4409](https://github.com/sigp/lighthouse/pull/4409), [lighthouse#4567](https://github.com/sigp/lighthouse/pull/4567)

</details>


<a id="attestation_processing-091"></a>
<details>
<summary><b>attestation_processing-091</b> Skip aggregates whose bits are a subset of seen — <i>implemented · medium · S · cpu, bandwidth</i></summary>

**Idea.** Track observed aggregation bits per attestation data (OR-ed or per aggregator) and treat an aggregate as redundant if its bits are a subset of already seen ones, rejecting it before BLS verification.

**Impact.** Redundant aggregates are ignored before any BLS work.

**Best measured result.** "~1 ms three-signature batch verify" skipped for redundant aggregates; no totals given (pr:silver#170)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:570`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L570) is_known_subset in verify_early_checks before BLS
- [`beacon_node/beacon_chain/src/observed_aggregates.rs:300`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_aggregates.rs#L300) is_known_subset per attestation-data root
- [`beacon_node/beacon_chain/src/observed_aggregates.rs:271`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_aggregates.rs#L271) observe_item replaces stored subsets with supersets
- [`beacon_node/beacon_chain/src/observed_aggregates.rs:127`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_aggregates.rs#L127) is_subset on aggregation bits

**Skeptic check.** Verified the subset check runs on observed aggregates keyed by committee_index+data root, ahead of signature verification. It compares against each seen aggregate, not an OR-union; the spec's IGNORE rule allows only that form, so this matches the idea.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#4669](https://github.com/OffchainLabs/prysm/pull/4669), [silver#170](https://github.com/gattaca-com/silver/pull/170)

</details>


<a id="attestation_processing-092"></a>
<details>
<summary><b>attestation_processing-092</b> Longer post-block wait before attesting — <i>n/a · low · S · latency</i></summary>

**Idea.** Delay attestation publishing a little longer after a block arrives so the head has been processed before voting, as block processing time grows.

**Impact.** n/a: the Lighthouse VC is event-driven, attesting when the BN reports the head after block import, with a spec deadline fallback, so there is no fixed post-block delay to tune.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/attestation_service.rs:295`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L295) attests on head event from the BN
- [`validator_client/validator_services/src/attestation_service.rs:316`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L316) fallback to attestation_due deadline
- [`consensus/types/src/core/chain_spec.rs:984`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/core/chain_spec.rs#L984) get_attestation_due

**Sources.** [nimbus#3518](https://github.com/status-im/nimbus-eth2/pull/3518)

</details>


<a id="attestation_processing-093"></a>
<details>
<summary><b>attestation_processing-093</b> Use pre-advanced current-slot state for attestation checks — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Validate gossip attestations and build aggregation against a state already advanced to the current/next slot (state-advance cache) instead of slot-processing the head state per attestation near epoch boundaries.

**Impact.** Committees for gossip checks come from the shuffling cache, which the state-advance timer primes before the boundary, so no slot processing happens per attestation.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:1617`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1617) map_attestation_committees via with_committee_cache
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:345`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L345) cache hit returns committee without touching a state
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:410`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L410) on a miss the head state or an advanced hot state is used, with partial_state_advance once per shuffling
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:409`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L409) advanced head state's next-epoch committee cache inserted into the shuffling cache before the epoch boundary

**Skeptic check.** Confirmed gossip verification never slot-processes per attestation; a miss computes once under a promise. The state_advance_timer priming of the shuffling cache (line 409) is the direct equivalent of the idea.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#12239](https://github.com/OffchainLabs/prysm/pull/12239), [grandine@18a073146](https://github.com/grandinetech/grandine/commit/18a073146c50), [grandine#206](https://github.com/grandinetech/grandine/pull/206)

</details>


<a id="attestation_processing-094"></a>
<details>
<summary><b>attestation_processing-094</b> Compare checkpoint in place without copying — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Compare an attestation's source checkpoint against the state's justified checkpoint by reference instead of copying the checkpoint out of the state per attestation.

**Impact.** None: Checkpoint is a 40-byte Copy value compared on the stack with no heap allocation, so nothing is left to remove.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/common/get_attestation_participation.rs:28-33`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/get_attestation_participation.rs#L28-L33)
- [`consensus/state_processing/src/per_block_processing/verify_attestation.rs:111-113`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/verify_attestation.rs#L111-L113)

**Skeptic check.** Verified both the participation-flag path and the inclusion-verification path compare data.source against a stack copy of the justified checkpoint; the Prysm issue (a heap copy out of a protobuf state) does not exist in Rust. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#8409](https://github.com/OffchainLabs/prysm/pull/8409)

</details>


<a id="attestation_processing-095"></a>
<details>
<summary><b>attestation_processing-095</b> Offload signature aggregation to worker with deadline — <i>n/a · low · L · cpu, latency</i></summary>

**Idea.** Run signature aggregation on a blocking worker thread with a deadline and cancellation, streaming results back, so the main event loop is not blocked by aggregation each slot.

**Impact.** n/a: Lighthouse aggregates incrementally by cheap point addition and runs BLS on beacon_processor workers; no costly per-slot aggregation on an actor loop. None for mainnet.

**Best measured result.** actor blocked 400-1200 ms per slot before; finality lag 3 vs 5 slots in a partition devnet (pr:ethlambda#299)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/naive_aggregation_pool.rs:281`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/naive_aggregation_pool.rs#L281) aggregate is an incremental BLS point add on arrival
- [`beacon_node/operation_pool/src/attestation_storage.rs:216`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L216) pool aggregate

**Sources.** [ethlambda#299](https://github.com/lambdaclass/ethlambda/pull/299)

</details>


<a id="attestation_processing-096"></a>
<details>
<summary><b>attestation_processing-096</b> Start aggregation early at 2/3 signatures — <i>n/a · low · L · latency</i></summary>

**Idea.** Start aggregation before the deadline once a data group holds two thirds of the expected signatures, and hold the aggregate until the scheduled publish time, giving expensive aggregation more time.

**Impact.** n/a: lean-consensus design with costly proof aggregation; Lighthouse aggregation is O(1) per message. None for mainnet.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/naive_aggregation_pool.rs:281`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/naive_aggregation_pool.rs#L281) incremental aggregation, no deadline-batched step

**Sources.** [ethlambda#487](https://github.com/lambdaclass/ethlambda/pull/487)

</details>


<a id="attestation_processing-097"></a>
<details>
<summary><b>attestation_processing-097</b> Prioritise aggregation jobs by block packing value — <i>n/a · low · L · cpu, latency</i></summary>

**Idea.** Rank and cap aggregation jobs using the proposer's packing score (current slot first, finalising over justifying) on a projected state, skipping candidates a block could not include, so limited aggregation time goes to useful work.

**Impact.** n/a: lean-consensus aggregation budgeting; Lighthouse aggregation is cheap and value-based packing happens only at block production. None for mainnet.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/max_cover.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/max_cover.rs) max-cover packing ranks attestations at proposal time
- [`beacon_node/beacon_chain/src/naive_aggregation_pool.rs:281`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/naive_aggregation_pool.rs#L281) aggregation is cheap, not prioritised

**Sources.** [ethlambda#509](https://github.com/lambdaclass/ethlambda/pull/509), [ethlambda#526](https://github.com/lambdaclass/ethlambda/pull/526)

</details>


<a id="attestation_processing-098"></a>
<details>
<summary><b>attestation_processing-098</b> Skip aggregation jobs for single signatures — <i>n/a · low · S · cpu</i></summary>

**Idea.** Do not run an aggregation job for a lone signature with no others to combine; keep it buffered until a companion arrives.

**Impact.** Lean consensus aggregation jobs do not exist in Lighthouse; the naive pool aggregates in place by bit-OR and signature add.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2596`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2596) naive pool inserts each verified unaggregated attestation immediately, no job scheduling

**Sources.** [ethlambda#483](https://github.com/lambdaclass/ethlambda/pull/483)

</details>


<a id="attestation_processing-099"></a>
<details>
<summary><b>attestation_processing-099</b> Skip aggregation with no validators or when syncing — <i>implemented · low · S · cpu</i></summary>

**Idea.** Skip attestation aggregation work when no validators are attached or the node is out of sync, since nobody uses the aggregates.

**Impact.** Already saved: without an aggregator duty for the subnet/slot, unaggregated attestations are only verified and propagated, and are never added to the naive aggregation pool.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/service.rs:567-575`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L567-L575)
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:420-422`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L420-L422)
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:448-458`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L448-L458)

**Skeptic check.** Confirmed should_process_attestation sets should_import, and process_gossip_attestation_result returns before add_to_naive_aggregation_pool when it is false. Without validators there are no aggregator subscriptions. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#908](https://github.com/status-im/nimbus-eth2/pull/908)

</details>


<a id="attestation_processing-100"></a>
<details>
<summary><b>attestation_processing-100</b> Only process unaggregated attestations for duty subnets — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Process and store single gossip attestations only for subnets/committees where a local validator has aggregation duty, so the signature pool and aggregation work shrink by the subnet count.

**Impact.** Non-duty-subnet attestations are only verified for propagation and are never stored in the naive aggregation pool.

**Best measured result.** "Only N/C (250)" of 1000 signatures stored; ~3MB to ~750KB per round at 4 subnets (pr:ethlambda#221)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/subnet_service/mod.rs:353`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L353) should_process_attestation true only for (subnet, slot) with an aggregator duty
- [`beacon_node/network/src/subnet_service/mod.rs:151`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L151) tracking disabled only with --import-all-attestations
- [`beacon_node/network/src/service.rs:572`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L572) should_process passed to handle_gossip
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:422`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L422) if !should_import, return after propagation: no naive-pool insert, no fork-choice apply

**Skeptic check.** Verified the full chain from subnet service to gossip_methods; with no aggregator duty the attestation is propagated and then dropped. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#11906](https://github.com/erigontech/erigon/pull/11906), [ethlambda#221](https://github.com/lambdaclass/ethlambda/pull/221), [lighthouse#1020](https://github.com/sigp/lighthouse/pull/1020)

</details>


<a id="attestation_processing-101"></a>
<details>
<summary><b>attestation_processing-101</b> Parallel gossip attestation validation before fork choice — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Index and validate gossip attestations on multiple threads, handing only validated votes to the single fork choice thread to apply.

**Impact.** Already parallel: batches are verified on many beacon processor workers, and only verified attestations reach apply_attestation_to_fork_choice, which is a short write-locked step.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:316`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L316)
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:432-436`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L432-L436)
- [`beacon_node/beacon_processor/src/lib.rs:110`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L110)

**Skeptic check.** Fork choice is applied on the worker under a lock rather than on one dedicated thread, but the effect is the same: validation runs in parallel and fork choice only sees validated votes. Earlier evidence correct (one path in it was missing the directory prefix).

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#3408](https://github.com/Consensys-Incorporated/teku/pull/3408)

</details>


<a id="attestation_processing-102"></a>
<details>
<summary><b>attestation_processing-102</b> Parallel verification of block attestations — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Verify the attestations included in a block in parallel across a thread pool, short-circuiting on the first failure, so block validation latency drops with core count.

**Impact.** The main cost, pairings and hash-to-curve, scales with cores through the blst pool. Failure is detected per batch, not short-circuited per attestation.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/block_signature_verifier.rs:459`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/block_signature_verifier.rs#L459) verify() of all block signature sets in one batch
- [`crypto/bls/src/impls/blst.rs:117`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L117) blst verify_multiple_aggregate_signatures (blst 0.3.17 spreads hash-to-curve and pairings over its thread pool)
- [`crypto/bls/src/impls/blst.rs:70`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L70) per-set signature subgroup check and pubkey aggregation run serially before the batch call

**Skeptic check.** Confirmed block attestations are batch-verified with a parallel blst call, which gives the idea's effect. Small residue: verify_signature_sets runs the signature subgroup checks and the pubkey aggregation serially for each set. With Electra aggregates of whole-slot size this is some milliseconds, not the dominant cost.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@b92d88d42](https://github.com/sigp/lighthouse/commit/b92d88d42bb5)

</details>


<a id="attestation_processing-103"></a>
<details>
<summary><b>attestation_processing-103</b> Async reprocessing of HTTP attestations with unknown head — <i>implemented · low · S · latency</i></summary>

**Idea.** For attestations submitted over HTTP that reference an unknown head, queue them for reprocessing and await retries on the async executor instead of blocking a worker thread.

**Impact.** Landed (lighthouse#5010): on UnknownHeadBlock or UnknownPayloadEnvelope the attestation goes into the reprocess queue and the result is awaited on a oneshot outside the blocking task.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/publish_attestations.rs:1-4`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_attestations.rs#L1-L4)
- [`beacon_node/http_api/src/publish_attestations.rs:141-188`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_attestations.rs#L141-L188)

**Skeptic check.** Verified that publish_attestations queues a QueuedUnaggregate with a process_fn and returns a Reprocessing(rx) result that is awaited asynchronously. This is the Lighthouse PR itself.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#5010](https://github.com/sigp/lighthouse/pull/5010)

</details>


<a id="attestation_processing-104"></a>
<details>
<summary><b>attestation_processing-104</b> Release queued attestations for recently imported roots — <i>not · low · S · latency</i></summary>

**Idea.** Remember recently imported block roots in the reprocess queue so attestations arriving just after the block import are released immediately rather than waiting for the queue timeout.

**Gap in Lighthouse.** Add a bounded expiring set of recently imported block roots in ReprocessQueue; in queue_awaiting_attestation, if the root is in the set, send ReadyWork immediately instead of delaying.

**Impact.** Removes up to ~12s wait for rare attestations that race the block import; slight gain in attestation inclusion and fork choice weight, tiny CPU effect.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L931) BlockImported only drains already queued work
- work_reprocessing_queue.rs:839-848 UnknownBlockAggregate/Unaggregate queue with no check of recently imported roots
- PR lighthouse#9264 is CLOSED, not merged

**Sources.** [lighthouse#9264](https://github.com/sigp/lighthouse/pull/9264)

</details>


<a id="attestation_processing-105"></a>
<details>
<summary><b>attestation_processing-105</b> Verify deferred attestations before queuing them — <i>not · medium · M · cpu, memory</i></summary>

**Idea.** BLS-verify attestations for unknown blocks or future slots at gossip time (through the batch verifier) before saving them for later, caching the valid result, so junk cannot fill pending caches and fork choice does not re-verify.

**Gap in Lighthouse.** Lighthouse queues attestations for unknown blocks without a signature check, and re-runs full gossip verification when the block arrives. To do it: on UnknownHeadBlock with a known target, get the committee and batch-verify the signature before queuing, reject and penalize when invalid, and cache the valid result so the reprocess does not verify again. The slasher path at attestation_verification.rs:446-500 already does the indexing and verification and could be reused.

**Impact.** Mostly DoS hardening. The queue is bounded to 16k and invalid signatures are rejected and penalized on reprocess, so the Teku penalty-free fork-choice cost is mostly not present. The gain is less junk in the queue and earlier peer penalties.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:2874`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L2874) UnknownHeadBlock queues the unverified attestation closure into the reprocess queue, gated only by reprocess_allowance
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:84`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L84) MAXIMUM_QUEUED_ATTESTATIONS = 16_384 bounds the queue
- [`beacon_node/beacon_chain/src/attestation_verification.rs:446`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L446) with a slasher, UnknownHeadBlock attestations whose target is known get indexed and signature-checked (line 493), but only to feed the slasher: the error is returned unchanged and the result is not cached
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:2629`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L2629) FutureSlot attestations are ignored, not saved

**Second check.** Found a similar mechanism the earlier review did not mention: with the slasher on, Lighthouse verifies signatures of unknown-head attestations whose target is known. It only feeds the slasher and does not gate or cache anything. Future-slot attestations are dropped, not deferred.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [teku#11554](https://github.com/Consensys-Incorporated/teku/pull/11554), [teku#11560](https://github.com/Consensys-Incorporated/teku/pull/11560)

</details>


<a id="attestation_processing-106"></a>
<details>
<summary><b>attestation_processing-106</b> Skip re-verifying gossip-verified attestation signatures — <i>implemented · medium · S · cpu</i></summary>

**Idea.** Mark attestations whose signature passed gossip validation and skip signature verification for them on later block import or fork choice paths.

**Impact.** Gossip and block attestations reach fork choice and the pools without a second signature check.

**Best measured result.** ~1000ms spent validating signatures wastefully (pr:lodestar#2259)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2573`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2573) apply_attestation_to_fork_choice takes a VerifiedAttestation and calls on_attestation, no signature check
- [`beacon_node/beacon_chain/src/block_verification.rs:1762`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1762) block attestations go to fork choice through the consensus_context cached indexed attestation, no re-verification
- [`consensus/fork_choice/src/fork_choice.rs:1168`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1168) on_attestation has no signature verification

**Skeptic check.** The source PRs (teku#3252, lodestar#2259) are about skipping a re-check in fork-choice processing. Lighthouse's on_attestation never verifies signatures, and the block path reuses indexed attestations that the block batch already verified. Lighthouse does still re-verify a block's aggregates that were already seen on gossip, but that is a different idea.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#3252](https://github.com/Consensys-Incorporated/teku/pull/3252), [lodestar#2259](https://github.com/ChainSafe/lodestar/pull/2259)

</details>


<a id="attestation_processing-107"></a>
<details>
<summary><b>attestation_processing-107</b> Skip signature check on already-verified pool/block attestations — <i>implemented · low · S · cpu</i></summary>

**Idea.** Use a no-verify processing variant when re-processing attestations already verified (from imported blocks re-added to the pool on reorg, or op pool attestations during block production).

**Impact.** Already saved: the op pool packs attestations without signature checks, and block processing during production uses VerifyRandao/NoVerification. A re-verify happens only with the opt-in paranoid_block_proposal flag.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5982-5990`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5982-L5990)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5992-6003`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5992-L6003)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:6529-6541`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6529-L6541)

**Skeptic check.** Confirmed that the only VerifySignatures::True on pool attestations during production is behind config.paranoid_block_proposal. Lighthouse does not re-add block attestations to the pool on reorg. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#5838](https://github.com/Consensys-Incorporated/teku/pull/5838), [prysm#3146](https://github.com/OffchainLabs/prysm/pull/3146), [lodestar@dcb94a7f2](https://github.com/ChainSafe/lodestar/commit/dcb94a7f21ef)

</details>


<a id="attestation_processing-108"></a>
<details>
<summary><b>attestation_processing-108</b> Verify unaggregated attestations once on pool entry — <i>implemented · low · S · cpu</i></summary>

**Idea.** Verify unaggregated attestation signatures on insertion into the pool instead of re-verifying them on every aggregation request.

**Impact.** Signatures are verified once at gossip or API entry; the naive aggregation pool and the op pool aggregate without re-verifying.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/lib.rs:291-296`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L291-L296)
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:316`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L316)
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:448-451`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L448-L451)

**Skeptic check.** Verified that add_to_naive_aggregation_pool takes an already VerifiedUnaggregate and that the pool assumes validity. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#4347](https://github.com/OffchainLabs/prysm/pull/4347)

</details>


<a id="attestation_processing-109"></a>
<details>
<summary><b>attestation_processing-109</b> Slasher detection per attestation, not per validator — <i>implemented · low · S · cpu, disk</i></summary>

**Idea.** Run slashing detection and span updates once per attestation batch rather than once per attesting validator, reducing DB lock acquisitions.

**Impact.** Already batched: one dequeue, one dedup and one RwTransaction per batch. Min/max span updates run once per validator chunk through array::update.

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/slasher.rs:135-202`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/slasher.rs#L135-L202)
- [`slasher/src/slasher.rs:205-255`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/slasher.rs#L205-L255)

**Skeptic check.** Confirmed process_attestations stores each attestation once and then calls process_batch per chunk subqueue, not per validator, all inside one transaction. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#5043](https://github.com/OffchainLabs/prysm/pull/5043)

</details>


<a id="attestation_processing-110"></a>
<details>
<summary><b>attestation_processing-110</b> Plain sha256 for is_aggregator check — <i>implemented · low · S · cpu</i></summary>

**Idea.** Compute is_aggregator from a plain sha256 of the selection proof bytes instead of a tree hash.

**Impact.** Already one plain sha256 over the 96 SSZ bytes of the signature.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/attestation/selection_proof.rs:54-55`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/attestation/selection_proof.rs#L54-L55)

**Skeptic check.** Verified that is_aggregator_from_modulo calls hash(&amp;self.0.as_ssz_bytes()) and does not use a tree hash. This is the Lighthouse PR itself.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#1296](https://github.com/sigp/lighthouse/pull/1296)

</details>


<a id="attestation_processing-111"></a>
<details>
<summary><b>attestation_processing-111</b> Refuse attestation production for slots before head — <i>implemented · low · S · memory, disk</i></summary>

**Idea.** Reject attestation production requests for slots earlier than the head instead of loading an old full state from disk, avoiding memory blowups.

**Impact.** Same effect by a different mechanism. Pre-finalization requests are rejected, and tree-states removed the tree-hash-cache full-state allocation that caused the OOMs.

**Best measured result.** Pyrmont: allocations about host physical memory size caused OOM kills (pr:lighthouse#2130)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2071`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2071) AttestingToFinalizedSlot rejects pre-finalization requests (no freezer reads)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2085`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2085) AttestingToAncientSlot
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2097`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2097) earlier slots use roots from the head state
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2125`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2125) same-epoch requests are served entirely from the head state
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2155`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2155) a prior-epoch request uses get_advanced_hot_state (state cache or hot DB only)

**Skeptic check.** The literal mechanism of #2130 (reject every slot before head) is gone: earlier slots are served again. Rejecting pre-finalized slots and using milhouse states removes the memory blowup. During long non-finality, a prior-epoch request on a state-cache miss can still load and replay a hot state from disk.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#2130](https://github.com/sigp/lighthouse/pull/2130)

</details>


<a id="attestation_processing-112"></a>
<details>
<summary><b>attestation_processing-112</b> Reject attestations with heads many skipped slots behind — <i>partial · medium · S · cpu, memory</i></summary>

**Idea.** Ignore gossip attestations whose head block is more than a bounded number of skipped slots behind the attestation slot, so state regeneration is never triggered for old heads.

**Gap in Lighthouse.** The TooManySkippedSlots guard exists but is off by default (import_max_skip_slots: None) and is never applied to aggregates (SignedAggregateAndProof verify_early_checks passes None). So a gossip attestation or aggregate whose head is many epochs behind still reaches with_cached_shuffling, which calls get_advanced_hot_state + partial_state_advance over all skipped epochs. Lodestar (which copied the LH error) enables a default of 32 slots for both attestations and aggregates.

**Impact.** Bounds state load/advance work caused by attestations with very old heads (DoS / minority-fork pressure); one advance per distinct shuffling id because of the promise dedup, so steady-state cost is small.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:1261`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1261) skip-slot check only runs when max_skip_slots is Some
- [`beacon_node/beacon_chain/src/chain_config.rs:151`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/chain_config.rs#L151) import_max_skip_slots defaults to None (check disabled)
- [`beacon_node/src/cli.rs:1091`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L1091) --max-skip-slots is opt-in, 'disabled by default'
- [`beacon_node/beacon_chain/src/attestation_verification.rs:611`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L611) aggregates call verify_head_block_is_known(chain, data, None): never limited
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:437`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L437) cache miss loads the old head's state and partial_state_advance at :454 runs across every skipped epoch

**Skeptic check.** The cited code is real but gated on a config that is None by default and bypassed for aggregates; the earlier verdict missed both facts. Enabling a default bound (and applying it to aggregates) is the missing part.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lodestar#5390](https://github.com/ChainSafe/lodestar/pull/5390)

</details>


<a id="attestation_processing-113"></a>
<details>
<summary><b>attestation_processing-113</b> Check head descends from target before loading target — <i>implemented · medium · S · cpu, disk</i></summary>

**Idea.** For aggregates, check that the attestation's head block descends from its target before loading the target block/state, so old targets are never loaded and advanced.

**Impact.** None; already in place.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:611`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L611) aggregate path resolves head ProtoBlock from fork choice
- [`beacon_node/beacon_chain/src/attestation_verification.rs:642`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L642) verify_attestation_target_root before any committee/state work
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1379`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1379) target derived from head ProtoBlock target_root/root, no block or state load
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1270`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1270) finalized-descendant check

**Skeptic check.** Verified that both aggregate and unaggregated paths check head-to-target consistency from the fork choice ProtoBlock before map_attestation_committees, which is the Lighthouse PR #1702 mechanism itself.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#1702](https://github.com/sigp/lighthouse/pull/1702)

</details>


<a id="attestation_processing-114"></a>
<details>
<summary><b>attestation_processing-114</b> Drop old-target attestations not on any known chain — <i>implemented · medium · S · cpu, memory</i></summary>

**Idea.** Ignore attestations whose target is old and was never a checkpoint on any known chain instead of replaying state for them, and skip slot processing on the state used for aggregate selection proof checks.

**Impact.** None beyond idea 112: no per-attestation replay; aggregate selection proof needs no processed state.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:1379`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1379) verify_attestation_target_root forces target to be the epoch-boundary block of the head's chain
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1633`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1633) map_attestation_committees drops targets unknown to fork choice / early attester cache
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:315`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L315) with_cached_shuffling keyed by shuffling decision root, promise dedup so one computation per shuffling
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1645`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1645) selection proof and signature use committee cache + pubkey cache, no state slot processing

**Skeptic check.** LH reaches the same effect differently: the target must equal the head chain's checkpoint (Prysm's 'viable checkpoint' test) and committees come from a dedup'd shuffling cache, not per-attestation replay. The remaining cost for very old heads (one state advance per shuffling) is covered by idea 112.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#12387](https://github.com/OffchainLabs/prysm/pull/12387)

</details>


<a id="attestation_processing-115"></a>
<details>
<summary><b>attestation_processing-115</b> Cheap checks before fork-head ancestor walks — <i>n/a · low · cpu</i></summary>

**Idea.** When choosing a validation state, try cheap checks (unknown block, head ancestry) first and only scan fork heads as fallback, bounding the ancestor walk by the target slot.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:7593`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7593) with_committee_cache resolves the shuffling via the shuffling cache keyed by head block root and epoch; no fork-head state scan

**Sources.** [teku#7251](https://github.com/Consensys-Incorporated/teku/pull/7251)

</details>


<a id="attestation_processing-116"></a>
<details>
<summary><b>attestation_processing-116</b> Skip fork choice lookup for head-targeting attestations — <i>not · low · S · cpu, latency</i></summary>

**Idea.** When an attestation's block is the canonical head or in the early-attester cache, skip the fork choice block lookup and its finalized-descent ancestor walk.

**Gap in Lighthouse.** Lighthouse PR 7010 was closed unmerged. In verify_head_block_is_known, check the canonical head root and early_attester_cache first and return the ProtoBlock without calling fork choice get_block and verify_attestation_is_finalized_checkpoint_or_descendant.

**Impact.** Skips a fork-choice read lock and ancestor walk per head-targeting attestation; PR claims ~6ms per attestation process (unverified, closed WIP).

**Best measured result.** approx 6ms saved per attestation process in experiments (pr:lighthouse#7010)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:1244`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1244) verify_head_block_is_known does fork_choice get_block first, early_attester_cache only as fallback
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1519`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1519) verify_attestation_is_finalized_checkpoint_or_descendant always runs after lookup

**Sources.** [lighthouse#7010](https://github.com/sigp/lighthouse/pull/7010)

</details>


<a id="attestation_processing-117"></a>
<details>
<summary><b>attestation_processing-117</b> Running counter for pending attestation cap — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Keep a running count of pending attestations updated on insert/prune/delete instead of scanning the whole pending map under lock to enforce the cap.

**Impact.** None.

**Best measured result.** limit check from ~184us to ~8ns (pr:prysm#17178)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:595`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L595) attestations_delay_queue.len() &gt;= MAXIMUM_QUEUED_ATTESTATIONS is O(1)
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:867`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L867) data columns use a running queued_data_columns_count

**Skeptic check.** Confirmed the cap checks use O(1) lengths or running counters; there is no scan over a pending map, and the reprocessing queue is a single-task actor with no lock.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#17178](https://github.com/OffchainLabs/prysm/pull/17178)

</details>


<a id="attestation_processing-118"></a>
<details>
<summary><b>attestation_processing-118</b> Separate queues and limits for aggregates vs singles — <i>partial · low · M · cpu, latency</i></summary>

**Idea.** Give aggregates and unaggregated attestations separate task queues and concurrency limits in the verifier so a flood of one cannot starve the other.

**Gap in Lighthouse.** Lighthouse has separate aggregate/unaggregated queues and batch sizes, but no separate concurrency limit or reserved worker share: the pop chain in BeaconProcessor::spawn_manager always drains aggregate_queue before attestation_queue, so a sustained aggregate flood can occupy every worker and starve unaggregated attestations (the starvation Grandine's per-type active-task counters prevent).

**Impact.** Only matters under aggregate floods; aggregates are batched up to max_gossip_aggregate_batch_size and the queue is bounded, so real-world starvation is rare.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:958-1015`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L958-L1015) aggregate_queue popped strictly before attestation_queue
- [`beacon_node/beacon_processor/src/lib.rs:1017-1060`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1017-L1060) attestation_queue only reached when aggregate_queue is empty
- [`beacon_node/beacon_processor/src/lib.rs:1292-1302`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1292-L1302) separate queues on push

**Skeptic check.** Verified the separate queues the earlier evidence cites, but the idea is per-type concurrency limits so neither starves the other; Lighthouse uses strict priority, which is the opposite for the lower-priority type.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [grandine@a8f89e57e](https://github.com/grandinetech/grandine/commit/a8f89e57e451), [grandine#175](https://github.com/grandinetech/grandine/pull/175)

</details>


<a id="attestation_processing-119"></a>
<details>
<summary><b>attestation_processing-119</b> Shorter attestation retention in caches — <i>implemented · low · S · memory</i></summary>

**Idea.** Retain stored attestations for a shorter window and drop redundant slot checks in subscription aggregation, lowering cache size and work.

**Impact.** Retention already shorter than Caplin's new 30-minute expiry; nothing left to gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/naive_aggregation_pool.rs:143`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/naive_aggregation_pool.rs#L143) SLOTS_RETAINED = 3
- [`beacon_node/operation_pool/src/attestation_storage.rs:634`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L634) prune keeps only current/previous target epoch

**Skeptic check.** Caplin cut attestation expiry to 30 minutes; Lighthouse keeps naive aggregates 3 slots and op-pool attestations about 2 epochs, so the earlier verdict holds.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#10097](https://github.com/erigontech/erigon/pull/10097)

</details>


<a id="attestation_processing-120"></a>
<details>
<summary><b>attestation_processing-120</b> Skip finalized-block attestations in fork choice import — <i>not · low · S · cpu, sync</i></summary>

**Idea.** Do not feed attestations from trusted or finalized blocks into fork choice vote processing during import, as they cannot affect head selection.

**Gap in Lighthouse.** In block_verification.rs attestation loop, skip the loop (and the indexed-attestation build) when the block slot is older than a threshold behind the wall clock (e.g. more than 2 epochs), as those votes cannot change head. Block is already rejected if at or before finalized slot (check_block_against_finalized_slot).

**Impact.** Saves per-block fork-choice vote updates and write-lock time only during range sync / backfill-like catch-up; no gain at head. Indexed attestations are likely computed anyway for signature verification.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1759`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1759) every block attestation goes through get_indexed_attestation and fork_choice.on_attestation (write lock held)
- [`consensus/fork_choice/src/fork_choice.rs:1325`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1325) on_attestation only skips zero root; validate_on_attestation does not drop old attestations when from a block

**Sources.** [lodestar@50bef7da7](https://github.com/ChainSafe/lodestar/commit/50bef7da751b)

</details>


<a id="attestation_processing-121"></a>
<details>
<summary><b>attestation_processing-121</b> Fast-path single-bit merges and skip subgroup check — <i>n/a · low · S · cpu, latency</i></summary>

**Idea.** When packing the pool, merge single-bit attestations directly instead of running max-cover, and skip the BLS subgroup check when deserializing already-verified signatures.

**Gap in Lighthouse.** Lighthouse merges single-bit attestations on insert and keeps decoded AggregateSignature in the pool, so packing does no deserialization or subgroup check; a max-cover fast path would save little.

**Impact.** Packing already runs prev/curr epochs in parallel via rayon::join.

**Best measured result.** 7s batch: 1905ms to 789ms mean; 9s: 142ms to 86ms; 11s: 17ms to 9ms (pr:prysm#12350)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation_storage.rs:457`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L457) insert aggregates into stored aggregates at insert time
- [`beacon_node/operation_pool/src/lib.rs:345`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L345) get_attestations runs maximum_cover over already-aggregated compact items
- [`crypto/bls/src/impls/blst.rs:74`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L74) subgroup check only in signature batch verification

**Sources.** [prysm#12350](https://github.com/OffchainLabs/prysm/pull/12350)

</details>


<a id="attestation_processing-122"></a>
<details>
<summary><b>attestation_processing-122</b> Skip redundant clone of attestation pre-state — <i>n/a · low · cpu, memory</i></summary>

**Idea.** Avoid cloning the attestation pre-state again when the fetched state is already an unshared copy.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs) uses committee caches, not a cloned pre-state (with_committee_cache at beacon_chain.rs:7593)

**Sources.** [prysm#6142](https://github.com/OffchainLabs/prysm/pull/6142), [prysm#8566](https://github.com/OffchainLabs/prysm/pull/8566)

</details>


<a id="attestation_processing-123"></a>
<details>
<summary><b>attestation_processing-123</b> Trigger-based batching of gossip attestation BLS verification — <i>not · medium · M · cpu, latency</i></summary>

**Idea.** Delay dispatching unaggregated gossip attestations to a worker until N are queued or a short max age expires, so BLS verification is batched even on many-core machines whose queues never fill.

**Gap in Lighthouse.** Add a hold-back in the beacon processor manager loop: when attestation_queue has fewer than N items and the oldest is younger than ~10ms, do not dispatch and arm a timer to wake the loop; track enqueue time in LifoQueue items. N and max age configurable.

**Impact.** Larger BLS batches on many-core nodes; PR measured BLS CPU -34% and total node CPU -30% on a high-subnet node, much less on default subscriptions.

**Best measured result.** BLS CPU -34%, total node CPU -30%; mean latency 104 ms -&gt; 37 ms; p99 1.80 s -&gt; 834 ms; p50 0.6 -&gt; 2.3 ms (trigger 8, max-age 10ms) (pr:lighthouse#9641)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:1017-1025`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1017-L1025) attestation_queue dispatched as soon as non-empty; batch_size&lt;2 -&gt; individual
- [`beacon_node/beacon_processor/src/lib.rs:110`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L110) only a max batch size (64), no min size or max age
- [`beacon_node/network/src/network_beacon_processor/mod.rs:86-130`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L86-L130) send_unaggregated_attestation forwards each attestation immediately, no buffering
- [`beacon_node/src/cli.rs:1654`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L1654) only --beacon-processor-attestation-batch-size (max) is configurable
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:53`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L53) DelayQueue only for unknown-block reprocessing, not batch formation

**Second check.** Checked the network-side send path, the scheduler/ submodules (work_queue, reprocessing DelayQueue), the manager poll loop and CLI flags for any min-batch, trigger or max-age mechanism; none exist, so the batch is formed only from whatever is queued at dispatch time.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [lighthouse#9641](https://github.com/sigp/lighthouse/pull/9641)

</details>


<a id="attestation_processing-124"></a>
<details>
<summary><b>attestation_processing-124</b> Single batching verifier for all attestation sources — <i>partial · low · S · cpu</i></summary>

**Idea.** Route gossip, API and locally produced attestations through one batching verifier before fork choice so their signatures can be batch-verified together.

**Gap in Lighthouse.** Make publish_attestations and the aggregate publish path call batch_verify_unaggregated/aggregated_attestations_for_gossip on the whole request instead of per item, then apply to fork choice.

**Impact.** Saves BLS verification cost for validator-client submitted attestations on nodes serving many validators (batch vs single is roughly 2x per signature); nothing for nodes without local validators.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:327`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L327) gossip unaggregates batch-verified, :538 aggregates batch-verified
- [`beacon_node/http_api/src/publish_attestations.rs:77`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_attestations.rs#L77) API attestations verified one by one with verify_unaggregated_attestation_for_gossip
- [`beacon_node/http_api/src/validator/mod.rs:1295`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L1295) API aggregates verified one by one

**Sources.** [grandine@cdbed21b7](https://github.com/grandinetech/grandine/commit/cdbed21b73d5)

</details>


<a id="attestation_processing-125"></a>
<details>
<summary><b>attestation_processing-125</b> Hoist base_reward_per_increment out of attestation loop — <i>implemented · low · S · cpu</i></summary>

**Idea.** Compute base_reward_per_increment once per block and reuse it for every attestation in process_attestations instead of recomputing it per attestation.

**Impact.** None.

**Best measured result.** process_attestations share of block_sim 1.5% -&gt; 0.25% (pr:nimbus#2704)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/epoch_cache.rs:96`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/epoch_cache.rs#L96) BaseRewardPerIncrement computed once per epoch cache build
- [`consensus/state_processing/src/epoch_cache.rs:111`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/epoch_cache.rs#L111) per-effective-balance base rewards precomputed
- [`consensus/types/src/state/beacon_state.rs:3136`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3136) get_base_reward reads epoch cache
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:280`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L280) per-attestation use is a cached lookup

**Skeptic check.** Verified that the Altair+ attestation reward path reads base rewards from the epoch cache; nothing is recomputed per attestation or per block.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#2704](https://github.com/status-im/nimbus-eth2/pull/2704), [nimbus#5458](https://github.com/status-im/nimbus-eth2/pull/5458)

</details>


<a id="attestation_processing-126"></a>
<details>
<summary><b>attestation_processing-126</b> In-place search instead of temporary sequence — <i>n/a · low · cpu, memory</i></summary>

**Idea.** Replace map-then-find patterns in attestation processing with an in-place linear search to avoid allocating a temporary sequence.

**Evidence (Lighthouse @ 928b61e719).**

- Nim-specific temporary sequence allocation; Rust iterators already search in place

**Sources.** [nimbus#1436](https://github.com/status-im/nimbus-eth2/pull/1436)

</details>


<a id="attestation_processing-127"></a>
<details>
<summary><b>attestation_processing-127</b> Read-only validator view for slashed checks — <i>n/a · low · S · memory, cpu</i></summary>

**Idea.** Read validator records through a read-only view without materializing tree nodes when checking slashed status for each attester in a block.

**Impact.** Nothing to gain: milhouse reads return references into the persistent tree, there is no per-read node materialization to avoid.

**Best measured result.** fixes ~500MB heap growth (pr:lodestar#4404)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:2408`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2408) get_validator returns &amp;Validator via milhouse get, no node materialization

**Sources.** [lodestar#4404](https://github.com/ChainSafe/lodestar/pull/4404)

</details>


<a id="attestation_processing-128"></a>
<details>
<summary><b>attestation_processing-128</b> Reuse gossip-computed indexed attestation downstream — <i>implemented · low · S · cpu</i></summary>

**Idea.** Wrap a gossip-validated attestation together with the indexed attestation computed during validation and pass both to the attestation manager and fork choice. Downstream stages then skip recomputing indices from committees.

**Impact.** Indexed attestation is computed once in gossip verification and reused by fork choice (apply_attestation_to_fork_choice) and the op pool (into_attestation_and_indices).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:322-361`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L322-L361)
- [`beacon_node/beacon_chain/src/attestation_verification.rs:390`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L390)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2573-2586`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2573-L2586)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2710-2712`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2710-L2712)

**Skeptic check.** Verified apply_attestation_to_fork_choice passes verified.indexed_attestation() and add_to_block_inclusion_pool inserts with the precomputed attesting indices. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#1971](https://github.com/Consensys-Incorporated/teku/pull/1971)

</details>


<a id="attestation_processing-129"></a>
<details>
<summary><b>attestation_processing-129</b> Handle payload attestations once block is known — <i>implemented · low · S · latency</i></summary>

**Idea.** Process and re-gossip payload attestation messages as soon as the referenced beacon block is known, without waiting for the execution payload envelope to finish importing. This removes needless delay in propagation.

**Impact.** Payload attestation gossip validation needs only the beacon block in fork choice; on success it is propagated (Accept), applied to fork choice and pooled with no envelope wait.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/payload_attestation_verification/gossip_verified_payload_attestation.rs:74-98`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_attestation_verification/gossip_verified_payload_attestation.rs#L74-L98)
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:4440-4495`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L4440-L4495)

**Skeptic check.** Confirmed the verifier looks up only fork_choice.get_block(beacon_block_root) and the handler accepts and re-gossips right after verification; no check on envelope import. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#9159](https://github.com/ChainSafe/lodestar/pull/9159)

</details>


<a id="attestation_processing-130"></a>
<details>
<summary><b>attestation_processing-130</b> Skip attestation simulator while syncing — <i>implemented · low · S · cpu</i></summary>

**Idea.** Skip the attestation simulator when the head block is more than two epochs behind the wall clock. Syncing nodes then avoid computing uncached future shufflings from old states.

**Impact.** Simulator returns early when best_slot + 2 epochs &lt; current slot.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_simulator.rs:12`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_simulator.rs#L12)
- [`beacon_node/beacon_chain/src/attestation_simulator.rs:93-104`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_simulator.rs#L93-L104)

**Skeptic check.** This is Lighthouse's own PR #5048 and the guard is present in produce_unaggregated_attestation. Upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#5048](https://github.com/sigp/lighthouse/pull/5048)

</details>


