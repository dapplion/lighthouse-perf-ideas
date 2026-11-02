# gossip_validation

68 ideas: 11 not, 16 partial, 39 implemented, 2 n/a; 23 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

The area has 142 numbered ideas; the 74 ids missing here have not been checked against Lighthouse yet.

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [gossip_validation-001](#gossip_validation-001) | Bounded LIFO gossip job queue serving newest first | implemented | medium |  | latency, cpu |
| [gossip_validation-002](#gossip_validation-002) **★** | Adaptive drop ratio when attestation queue overflows | not | medium | S | cpu, latency |
| [gossip_validation-003](#gossip_validation-003) | Yield to networking between gossip processing batches | implemented | high | S | latency |
| [gossip_validation-004](#gossip_validation-004) | Batch BLS verification of gossip attestations and aggregates | implemented | high |  | cpu, latency |
| [gossip_validation-005](#gossip_validation-005) **★** | Route other gossip types through shared batch verifier | not | medium | M | cpu, latency |
| [gossip_validation-006](#gossip_validation-006) | Verify one message's multiple signatures in one batch | implemented | medium |  | cpu, latency |
| [gossip_validation-011](#gossip_validation-011) | Deserialize attestation signatures once through pipeline | implemented | low |  | cpu |
| [gossip_validation-012](#gossip_validation-012) | Aggregate attestation pubkeys without per-validator allocations | implemented | medium |  | cpu, memory |
| [gossip_validation-015](#gossip_validation-015) | Minimal state advance for gossip validation | implemented | medium |  | cpu, latency, memory |
| [gossip_validation-017](#gossip_validation-017) | Validate exits and BLS changes with light validator getters | implemented | low |  | cpu, memory |
| [gossip_validation-018](#gossip_validation-018) | Use in-memory head info instead of per-message state reads | implemented | medium |  | cpu, disk, latency |
| [gossip_validation-020](#gossip_validation-020) | Cheap block-known lookup in pre-validation queue | n/a | low |  | cpu |
| [gossip_validation-024](#gossip_validation-024) | Proposer index from shared per-epoch cache, no state advance | implemented | medium |  | cpu, latency |
| [gossip_validation-026](#gossip_validation-026) **★** | Ignore blocks whose parent is older than justified | not | medium | S | cpu, memory |
| [gossip_validation-028](#gossip_validation-028) **★** | Bound state advancement for old or long-skip roots | partial | high | S | cpu |
| [gossip_validation-029](#gossip_validation-029) | Order gossip validation checks cheapest first | implemented | medium | S | cpu, disk, latency |
| [gossip_validation-030](#gossip_validation-030) **★** | Cheap sidecar checks before proposer BLS signature | partial | medium | S | cpu |
| [gossip_validation-031](#gossip_validation-031) | Cheap checks before loading pre-state | implemented | medium |  | cpu, disk |
| [gossip_validation-033](#gossip_validation-033) | Seen-check sidecars first before KZG and signature | implemented | medium |  | cpu, bandwidth |
| [gossip_validation-035](#gossip_validation-035) | Seen-attestation cache checked first in attestation validation | implemented | medium |  | cpu |
| [gossip_validation-036](#gossip_validation-036) | Compact key for seen unaggregated attestation cache | implemented | low |  | cpu, memory |
| [gossip_validation-039](#gossip_validation-039) **★** | Dedup slasher ingress before BLS and queueing | not | medium | S | cpu, memory |
| [gossip_validation-041](#gossip_validation-041) **★** | Ignore further blocks from same proposer and slot | partial | medium | S | cpu |
| [gossip_validation-042](#gossip_validation-042) **★** | Atomic seen check-and-set for concurrent duplicates | partial | medium | M | cpu |
| [gossip_validation-044](#gossip_validation-044) | Ignore aggregates whose bits are subset of seen ones | implemented | medium |  | bandwidth, cpu |
| [gossip_validation-045](#gossip_validation-045) | Seen-aggregate root cache checked before any validation work | implemented | medium |  | bandwidth, cpu, latency |
| [gossip_validation-046](#gossip_validation-046) **★** | Cache validation work per distinct AttestationData | not | medium | M | cpu |
| [gossip_validation-047](#gossip_validation-047) **★** | Verify proposer header signature once across sidecars | partial | medium | S | cpu, latency |
| [gossip_validation-049](#gossip_validation-049) | Compute gossip block root once and reuse it | implemented | low |  | cpu, latency |
| [gossip_validation-050](#gossip_validation-050) **★** | Cache invalid block roots to reject descendants | partial | medium | M | cpu, latency |
| [gossip_validation-052](#gossip_validation-052) | Check snappy declared length before decompressing | implemented | medium |  | bandwidth, cpu, memory |
| [gossip_validation-053](#gossip_validation-053) **★** | Bound column sidecar size by max blobs early | partial | medium | S | cpu, memory |
| [gossip_validation-054](#gossip_validation-054) | Bound pending, deferred and future-slot gossip queues | implemented | medium |  | cpu, memory |
| [gossip_validation-055](#gossip_validation-055) **★** | Reject future-slot messages before queueing or hashing | partial | medium | S | memory, cpu |
| [gossip_validation-056](#gossip_validation-056) **★** | Cap in-flight gossip validations per large topic | partial | medium | M | cpu, memory |
| [gossip_validation-057](#gossip_validation-057) **★** | Keep compressed payload in gossip validation queue | not | medium | L | memory |
| [gossip_validation-059](#gossip_validation-059) | Reject pre-finalized gossip blocks and attestations | implemented | medium |  | cpu, bandwidth |
| [gossip_validation-061](#gossip_validation-061) | Skip gossip validation while syncing or far behind | implemented | low |  | cpu, sync |
| [gossip_validation-066](#gossip_validation-066) **★** | Batch KZG verification of gossip column sidecars | not | medium | M | cpu |
| [gossip_validation-069](#gossip_validation-069) | Remove seen caches made redundant by other dedup | not | low | S | bandwidth, cpu, memory |
| [gossip_validation-070](#gossip_validation-070) | Bypass queue gating for gossip blocks | implemented | low |  | latency |
| [gossip_validation-074](#gossip_validation-074) | Hold slightly-early gossip objects until their slot | partial | low | M | cpu, latency |
| [gossip_validation-079](#gossip_validation-079) **★** | Verify block signature before pending-queue insertion | partial | medium | M | bandwidth, cpu, memory |
| [gossip_validation-081](#gossip_validation-081) | Expire held unknown-root gossip messages | implemented | low |  | memory |
| [gossip_validation-085](#gossip_validation-085) | Per-(validator, epoch) seen caches checked before validation | implemented | low |  | bandwidth, cpu, disk, memory |
| [gossip_validation-087](#gossip_validation-087) | Size seen caches for the validator set | implemented | low | S | bandwidth, cpu |
| [gossip_validation-091](#gossip_validation-091) | Replace DB reads in gossip checks with in-memory state | implemented | low | S | cpu, disk, latency |
| [gossip_validation-092](#gossip_validation-092) **★** | Group queued attestations by data for batch verify | not | medium | M | cpu |
| [gossip_validation-097](#gossip_validation-097) | Bounded prioritized gossip work queue, blocks first | implemented | low | S | bandwidth, cpu, latency |
| [gossip_validation-101](#gossip_validation-101) | Attestation admission budget scaled to traffic | partial | low | M | cpu, memory |
| [gossip_validation-103](#gossip_validation-103) | Cheap raw-byte field reads without views | n/a | low | S | cpu |
| [gossip_validation-104](#gossip_validation-104) **★** | Peek raw SSZ bytes to skip deserialization | partial | medium | M | cpu, memory |
| [gossip_validation-107](#gossip_validation-107) | Singleflight state replays for sidecar verification | implemented | medium |  | cpu, memory |
| [gossip_validation-111](#gossip_validation-111) | Plain map for bounded seen key space | implemented | low | S | cpu, memory |
| [gossip_validation-113](#gossip_validation-113) **★** | Precompute per-shuffling committee aggregate pubkeys | not | medium | M | cpu |
| [gossip_validation-114](#gossip_validation-114) | Use proposer lookahead to skip epoch transitions | implemented | medium |  | cpu, latency, memory |
| [gossip_validation-115](#gossip_validation-115) **★** | Read-only head or parent state, no copy | partial | medium | S | cpu, latency, memory |
| [gossip_validation-116](#gossip_validation-116) | Use cached checkpoint or advanced states for validation | implemented | medium |  | cpu, latency, memory |
| [gossip_validation-117](#gossip_validation-117) | Direct state lookup by block root | implemented | low | S | cpu, latency |
| [gossip_validation-118](#gossip_validation-118) | Synchronous cached state read, conditional pool add | partial | low | S | cpu, latency |
| [gossip_validation-119](#gossip_validation-119) | Small immutable validation view cache for bids | implemented | low | S | cpu, memory |
| [gossip_validation-121](#gossip_validation-121) | Signature check before state advance | implemented | medium | S | cpu, latency |
| [gossip_validation-125](#gossip_validation-125) | Skip repeated signature verification | implemented | low | S | cpu, latency |
| [gossip_validation-127](#gossip_validation-127) **★** | Skip validating locally produced or self-published objects | partial | medium | S | cpu, latency |
| [gossip_validation-128](#gossip_validation-128) | Ignore already known blocks and columns early | implemented | medium |  | cpu |
| [gossip_validation-136](#gossip_validation-136) | Avoid copying signature batches | implemented | low | S | cpu, memory |
| [gossip_validation-140](#gossip_validation-140) | Shorter batch signature verification deadline | implemented | low | S | latency |
| [gossip_validation-142](#gossip_validation-142) **★** | Skip aggregate and contribution work without validators | not | medium | S | cpu |

★ actionable. Click an id for the full record.

## Ideas

<a id="gossip_validation-001"></a>
<details>
<summary><b>gossip_validation-001</b> Bounded LIFO gossip job queue serving newest first — <i>implemented · medium · latency, cpu</i></summary>

**Idea.** Process gossip validation jobs from a bounded queue that pops LIFO (newest first) and drops items beyond the limit, so under load fresh messages are validated before stale ones.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_queue.rs:237-259`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_queue.rs#L237-L259) LifoQueue push_front, pop_front, drops oldest when full
- [`beacon_node/beacon_processor/src/scheduler/work_queue.rs:425-434`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_queue.rs#L425-L434) attestation, aggregate, sync message/contribution queues are LifoQueue

**Sources.** [lodestar#2275](https://github.com/ChainSafe/lodestar/pull/2275)

</details>


<a id="gossip_validation-002"></a>
<details>
<summary><b>gossip_validation-002</b> Adaptive drop ratio when attestation queue overflows — <i>not · medium · S · cpu, latency</i></summary>

**Idea.** When the attestation gossip queue is full, drop a growing fraction of queued items (ratio increases per overflow up to a max, resets when the queue drains) instead of one per insert, so the node escapes sustained overload and lower-priority queues still get served.

**Gap in Lighthouse.** In LifoQueue::push (or in the attestation handling in lib.rs), count consecutive overflows and drop a growing fraction from the back, then reset when the queue drains, so lower-priority queues get served under sustained overload. LIFO already serves the newest items first, but the drop policy and the starvation of lower queues are unchanged.

**Impact.** Under sustained overload: fewer wasted stale attestations and lower-priority queues get served. No effect on a healthy mainnet node.

**Best measured result.** Attestation drops fell from 30-40% to ~10%; lower priority queues no longer dropped 100% (pr:lodestar#5355)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_queue.rs:250-259`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_queue.rs#L250-L259) LifoQueue::push drops exactly one oldest item per overflow
- [`beacon_node/beacon_processor/src/scheduler/work_queue.rs:335-362`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_queue.rs#L335-L362) queue lengths fixed or scaled by validator count at startup, not adaptive
- [`beacon_node/beacon_processor/src/scheduler/work_queue.rs:485`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_queue.rs#L485) attestation_queue is a LifoQueue
- [`beacon_node/beacon_processor/src/lib.rs:1017-1054`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1017-L1054) attestation queue drained in strict priority order ahead of lower queues

**Second check.** Searched the scheduler (work_queue.rs, work_reprocessing_queue.rs) and lib.rs for overflow, drop and expiry logic. Only fixed-length LIFO with drop-one, drop_during_sync, and delay-queue caps exist; there is no adaptive ratio.

**Sources.** [lodestar#5355](https://github.com/ChainSafe/lodestar/pull/5355)

</details>


<a id="gossip_validation-003"></a>
<details>
<summary><b>gossip_validation-003</b> Yield to networking between gossip processing batches — <i>implemented · high · S · latency</i></summary>

**Idea.** Run queued gossip/block processing in small batches or time slices and hand control back to the network/event loop between them (time-based, not per job), so CPU-heavy work does not starve networking; allow concurrency above one so signature work can batch.

**Impact.** None to gain: the source PRs fix single-threaded event loops (Nim, JS). Lighthouse gets the same result from thread isolation. CPU work never runs on the tokio core threads that drive libp2p, and the OS scheduler time-slices the threads. Batching for BLS and multi-worker concurrency are already present.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:747-748`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L747-L748) each worker is a tokio task started with spawn_blocking, separate from the async network tasks
- [`beacon_node/beacon_processor/src/lib.rs:130`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L130) max_workers = num_cpus (concurrency above one)
- [`beacon_node/beacon_processor/src/lib.rs:890`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L890) manager only spawns while current_workers &lt; max_workers
- [`beacon_node/beacon_processor/src/lib.rs:1017-1054`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1017-L1054) attestation queue drained into batches for batch BLS
- [`common/task_executor/src/lib.rs:209-229`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/task_executor/src/lib.rs#L209-L229) spawn_blocking / spawn_blocking_with_rayon run CPU work on dedicated blocking/rayon pools

**Second check.** Checked the task_executor blocking and rayon pools, and the max_workers default. The idea's goal (networking is not starved, concurrency above one, signature batching) is met by an equivalent mechanism, so a time-slice yield has no job to do here.

**Sources.** [lodestar#2472](https://github.com/ChainSafe/lodestar/pull/2472), [nimbus@76f15302a](https://github.com/status-im/nimbus-eth2/commit/76f15302a71f), [nimbus#2227](https://github.com/status-im/nimbus-eth2/pull/2227)

</details>


<a id="gossip_validation-004"></a>
<details>
<summary><b>gossip_validation-004</b> Batch BLS verification of gossip attestations and aggregates — <i>implemented · high · cpu, latency</i></summary>

**Idea.** Collect signature sets from many gossip attestations/aggregates over a short window and verify them with one randomized batch BLS call, falling back to individual verification on failure; this amortizes the final exponentiation. Verify the signature early via the batch verifier, before expensive shuffling lookups.

**Best measured result.** batch check ~0.5ms/check vs ~1ms single; throughput 2x higher; worst latency ~40ms (pr:nimbus#2439)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:110`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L110) DEFAULT_MAX_GOSSIP_ATTESTATION_BATCH_SIZE=64 and aggregate batch 64
- [`beacon_node/beacon_processor/src/lib.rs:1017-1035`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1017-L1035) pops up to batch size attestations into a GossipAttestationBatch
- [`beacon_node/beacon_processor/src/lib.rs:104-110`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L104-L110) comment: fall back to individual verification on batch failure
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:529`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L529) process_gossip_aggregate_batch

**Sources.** [prysm#10111](https://github.com/OffchainLabs/prysm/pull/10111), [teku#4106](https://github.com/Consensys-Incorporated/teku/pull/4106), [prysm#10553](https://github.com/OffchainLabs/prysm/pull/10553), [nimbus#2439](https://github.com/status-im/nimbus-eth2/pull/2439), [prysm#11144](https://github.com/OffchainLabs/prysm/pull/11144), [nimbus#6917](https://github.com/status-im/nimbus-eth2/pull/6917)

</details>


<a id="gossip_validation-005"></a>
<details>
<summary><b>gossip_validation-005</b> Route other gossip types through shared batch verifier — <i>not · medium · M · cpu, latency</i></summary>

**Idea.** Send signatures of sync committee messages, voluntary exits and payload-timeliness attestations to the shared async batch BLS verifier instead of verifying each inline, publishing or pooling only after the batch succeeds.

**Gap in Lighthouse.** Add batch Work variants and queue draining for sync committee messages and payload attestations, as is done for attestations. Call verify_signature_sets once per batch and fall back to individual checks on failure. This touches the Work enum in lib.rs, gossip_methods.rs, sync_committee_verification.rs and payload_attestation_verification. Exits are rare, so skip them.

**Impact.** About 512 sync messages per slot, plus PTC payload attestations after Gloas, are each verified with a single pubkey. Batching could save about a third to a half of that BLS time, which is a small CPU gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:390-409`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L390-L409) only GossipAttestationBatch and GossipAggregateBatch Work variants exist
- [`beacon_node/beacon_chain/src/sync_committee_verification.rs:709`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/sync_committee_verification.rs#L709) SyncCommitteeMessage signature verified alone with signature_set.verify()
- [`beacon_node/beacon_chain/src/sync_committee_verification.rs:604-670`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/sync_committee_verification.rs#L604-L670) contributions batch only their own 3 signatures, not across messages
- [`beacon_node/beacon_chain/src/payload_attestation_verification/gossip_verified_payload_attestation.rs:142`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_attestation_verification/gossip_verified_payload_attestation.rs#L142) payload attestation signature verified alone
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:2314`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L2314) sync committee messages processed one at a time

**Second check.** Also checked the Gloas payload attestation path and the contribution batch helper. Neither batches across gossip messages, so not is upheld.

**Sources.** [caplin#12485](https://github.com/erigontech/erigon/pull/12485), [caplin#12541](https://github.com/erigontech/erigon/pull/12541), [teku#11538](https://github.com/Consensys-Incorporated/teku/pull/11538), [teku#4144](https://github.com/Consensys-Incorporated/teku/pull/4144)

</details>


<a id="gossip_validation-006"></a>
<details>
<summary><b>gossip_validation-006</b> Verify one message&#x27;s multiple signatures in one batch — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** For aggregate-and-proof (selection proof, aggregator signature, aggregate signature) and sync contributions, verify all signatures of the message in a single batched multi-pairing instead of three separate verifications.

**Best measured result.** BenchmarkValidateAggregateAndProof 3931547 -&gt; 2812799 ns/op (40% better, ~1.2ms per aggregate, ~300ms per slot at 260 aggregates) (pr:prysm#7744)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:1457-1484`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1457-L1484) selection proof and aggregate signature sets verified via one verify_signature_sets call
- [`beacon_node/beacon_chain/src/sync_committee_verification.rs:640-670`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/sync_committee_verification.rs#L640-L670) three sets (selection proof, contribution-and-proof, contribution) in one verify_signature_sets

**Sources.** [caplin#12537](https://github.com/erigontech/erigon/pull/12537), [prysm#7744](https://github.com/OffchainLabs/prysm/pull/7744), [teku#3824](https://github.com/Consensys-Incorporated/teku/pull/3824)

</details>


<a id="gossip_validation-011"></a>
<details>
<summary><b>gossip_validation-011</b> Deserialize attestation signatures once through pipeline — <i>implemented · low · cpu</i></summary>

**Idea.** Parse gossip attestation/aggregate signatures once and pass the parsed signature through verification queues and the pool instead of re-parsing at each stage.

**Best measured result.** Fixed attesting regressions v1.0.10-&gt;v1.0.12 caused by repeated deserialization (pr:nimbus#2472)

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/generic_signature.rs:145`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/generic_signature.rs#L145) deserialize decompresses once into a point held in the type
- [`crypto/bls/src/generic_signature.rs:191`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/generic_signature.rs#L191) SSZ decode does this, so the parsed signature travels through queues and pool

**Sources.** [nimbus#2472](https://github.com/status-im/nimbus-eth2/pull/2472)

</details>


<a id="gossip_validation-012"></a>
<details>
<summary><b>gossip_validation-012</b> Aggregate attestation pubkeys without per-validator allocations — <i>implemented · medium · cpu, memory</i></summary>

**Idea.** Build aggregate pubkeys for attestation verification by reading the validator registry by index without allocating a deserialized pubkey object per validator.

**Best measured result.** avoids memory allocation in gossip hot path (no numbers) (pr:prysm#14178)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/signature_sets.rs:295-322`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/signature_sets.rs#L295-L322) indexed_attestation_signature_set takes Cow&lt;PublicKey&gt; via get_pubkey
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:174`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L174) get returns &amp;PublicKey from a pre-decompressed cache

**Sources.** [prysm#14178](https://github.com/OffchainLabs/prysm/pull/14178)

</details>


<a id="gossip_validation-015"></a>
<details>
<summary><b>gossip_validation-015</b> Minimal state advance for gossip validation — <i>implemented · medium · cpu, latency, memory</i></summary>

**Idea.** Validate gossip attestations, aggregates, blocks, slashings and sync messages against the existing head state or a checkpoint state cache entry, advancing a copy only when the epoch actually differs and then only to the target epoch start, rather than running process_slots to the message slot per message.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:315`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L315) with_cached_shuffling reuses head state, advances only to start of epoch before shuffling_epoch via partial_state_advance (shuffling_cache.rs:~430)
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1617`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1617) map_attestation_committees uses with_committee_cache
- [`beacon_node/beacon_chain/src/block_verification.rs:1031`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1031) with_proposer_cache; load_parent only on miss
- [`beacon_node/beacon_chain/src/sync_committee_verification.rs:473`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/sync_committee_verification.rs#L473) sync_committee_at_next_slot uses cached head

**Sources.** [prysm#4532](https://github.com/OffchainLabs/prysm/pull/4532), [lodestar@341032f35](https://github.com/ChainSafe/lodestar/commit/341032f35358), [teku#5236](https://github.com/Consensys-Incorporated/teku/pull/5236), [prysm#4474](https://github.com/OffchainLabs/prysm/pull/4474), [prysm#7357](https://github.com/OffchainLabs/prysm/pull/7357), [teku#4142](https://github.com/Consensys-Incorporated/teku/pull/4142), [prysm#16830](https://github.com/OffchainLabs/prysm/pull/16830)

</details>


<a id="gossip_validation-017"></a>
<details>
<summary><b>gossip_validation-017</b> Validate exits and BLS changes with light validator getters — <i>implemented · low · cpu, memory</i></summary>

**Idea.** Validate voluntary exits and BLS-to-execution changes using only the few validator fields needed from a cheap head-validator accessor, instead of fetching or advancing a full beacon state per message.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2841`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2841) verify_voluntary_exit_for_gossip reads fields from Arc-cloned head snapshot, no state advance or copy
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2959`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2959) BLS change verified against head state Arc ('save advancing')

**Sources.** [prysm#4612](https://github.com/OffchainLabs/prysm/pull/4612), [prysm#11694](https://github.com/OffchainLabs/prysm/pull/11694), [teku#6732](https://github.com/Consensys-Incorporated/teku/pull/6732)

</details>


<a id="gossip_validation-018"></a>
<details>
<summary><b>gossip_validation-018</b> Use in-memory head info instead of per-message state reads — <i>implemented · medium · cpu, disk, latency</i></summary>

**Idea.** Gossip validation should take head and finalized checkpoints and the head state from in-memory chain/fork-choice info (head state root, cached state) rather than reading the head state or block roots from the DB per message.

**Best measured result.** "major noticeable bottleneck from our profiling" (no numbers) (pr:prysm#2383)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:1244`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1244) verify_head_block_is_known reads fork choice (in-memory proto array) and early_attester_cache
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:358`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L358) uses canonical_head.cached_head() snapshot state
- [`beacon_node/beacon_chain/src/block_verification.rs:1925-1950`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1925-L1950) finalized checks use fork choice

**Sources.** [prysm#2383](https://github.com/OffchainLabs/prysm/pull/2383), [prysm#3288](https://github.com/OffchainLabs/prysm/pull/3288), [lodestar@6103d7b71](https://github.com/ChainSafe/lodestar/commit/6103d7b7122a)

</details>


<a id="gossip_validation-020"></a>
<details>
<summary><b>gossip_validation-020</b> Cheap block-known lookup in pre-validation queue — <i>n/a · low · cpu</i></summary>

**Idea.** In pre-validation checks of whether a referenced block root is known, use a plain fork-choice membership lookup without the descendant-of-finalized walk, leaving that check to full validation.

**Gap in Lighthouse.** Lighthouse has no separate pre-validation queue; fork choice contains_block is already a plain HashMap lookup without descendant-of-finalized walk.

**Best measured result.** hasBlockHex took 12% of main thread CPU time (pr:lodestar#5575)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:1244`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1244) verify_head_block_is_known uses fork choice get_block
- [`beacon_node/beacon_chain/src/block_verification.rs:971`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L971) contains_block

**Sources.** [lodestar#5575](https://github.com/ChainSafe/lodestar/pull/5575)

</details>


<a id="gossip_validation-024"></a>
<details>
<summary><b>gossip_validation-024</b> Proposer index from shared per-epoch cache, no state advance — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** Get the expected proposer (and committees) for gossip blocks and blob sidecars from a shared per-epoch proposer-index cache keyed by decision root, pruning old entries, instead of advancing, rewinding or loading a state.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:175`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L175) with_proposer_cache keyed by (epoch, shuffling_decision_block)
- [`beacon_node/beacon_chain/src/block_verification.rs:1031`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1031) block gossip uses it
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1750`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1750) column gossip uses it

**Sources.** [nimbus#1440](https://github.com/status-im/nimbus-eth2/pull/1440), [prysm#8107](https://github.com/OffchainLabs/prysm/pull/8107), [prysm#13423](https://github.com/OffchainLabs/prysm/pull/13423), [lodestar@8c15e1610](https://github.com/ChainSafe/lodestar/commit/8c15e16108b9)

</details>


<a id="gossip_validation-026"></a>
<details>
<summary><b>gossip_validation-026</b> Ignore blocks whose parent is older than justified — <i>not · medium · S · cpu, memory</i></summary>

**Idea.** Ignore current-epoch gossip blocks and column sidecars whose parent is canonical but older than the justified checkpoint, avoiding state regeneration to check the proposer.

**Gap in Lighthouse.** Before the proposer-cache lookup in GossipVerifiedBlock::new_without_slasher_checks and validate_data_column_sidecar_for_gossip_fulu, IGNORE current-epoch blocks/columns whose parent is canonical and older than the fork-choice justified checkpoint slot, so a lagging proposer's block does not trigger a hot-state load and advance.

**Impact.** Avoids a cold state load and multi-epoch advance per proposer-cache miss for blocks/columns built on stale canonical parents (lagging proposers, cheap DoS); rare on healthy mainnet.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1019-1050`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1019-L1050) gossip block path checks only parent-known/later-than-parent, then with_proposer_cache falls to load_parent on a miss; no justified-checkpoint check
- [`beacon_node/beacon_chain/src/block_verification.rs:2012-2028`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L2012-L2028) load_parent only rejects pre-finalized parents
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1179-1185`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1179-L1185) and 1747-1765 column path: finalized-descendant check, then get_advanced_hot_state on proposer-cache miss
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:188-200`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L188-L200) OnceCell dedups concurrent misses for one (epoch, decision root) but does not avoid the state load
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1730-1746`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1730-L1746) only finalized-based IGNOREs

**Second check.** Grepped justified across block_verification, data_column_verification, beacon_proposer_cache and gossip_methods (no hits) and read load_parent and with_proposer_cache; the only related mitigation is OnceCell dedup of concurrent cache misses, which bounds repeated work but still loads the state once.

**Sources.** [prysm#16579](https://github.com/OffchainLabs/prysm/pull/16579)

</details>


<a id="gossip_validation-028"></a>
<details>
<summary><b>gossip_validation-028</b> Bound state advancement for old or long-skip roots — <i>partial · high · S · cpu</i></summary>

**Idea.** Reject or ignore gossip blocks and votes whose parent or target block is too many slots behind, or cap slot processing to one epoch, before advancing state over long runs of empty slots for attacker-chosen roots.

**Gap in Lighthouse.** There is no default bound on the parent or target distance. Default import_max_skip_slots to a finite value (for example a few epochs), apply it to aggregates, and add an equivalent check for gossip blocks whose parent is many slots behind. The cost is already reduced (partial advance, shuffling cache keyed by decision root, promise dedup), but it is not capped.

**Impact.** DoS hardening only: an attacker who picks old non-finalized roots can force long empty-slot advances. No steady-state saving on mainnet.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:946-951`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L946-L951) skip-slot limit for unaggregated attestations only, via import_max_skip_slots
- [`beacon_node/beacon_chain/src/attestation_verification.rs:601-602`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L601-L602) aggregates explicitly exempt
- [`beacon_node/beacon_chain/src/chain_config.rs:151`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/chain_config.rs#L151) import_max_skip_slots default None
- [`beacon_node/src/cli.rs:1091-1097`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L1091-L1097) --max-skip-slots documented as disabled by default
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:315-345`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L315-L345) shuffling looked up by (epoch, decision root) and promise-deduplicated, so one old root costs one advance
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:425-460`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L425-L460) advance limited to the epoch before shuffling_epoch, and uses partial_state_advance (no state roots)
- [`beacon_node/beacon_chain/src/block_verification.rs:2173-2197`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L2173-L2197) cheap_state_advance_to_obtain_committees advances only to the block epoch start
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:346`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L346) proposer shuffling also uses partial_state_advance

**Second check.** Checked the CLI help (the limit is disabled by default on purpose), shuffling_cache with_cached_shuffling and its partial advance and dedup, and the proposer cache advance. All of them lower the cost but none caps the distance, so partial is upheld.

**Sources.** [teku#3975](https://github.com/Consensys-Incorporated/teku/pull/3975), [nimbus#1304](https://github.com/status-im/nimbus-eth2/pull/1304), [lodestar#4020](https://github.com/ChainSafe/lodestar/pull/4020)

</details>


<a id="gossip_validation-029"></a>
<details>
<summary><b>gossip_validation-029</b> Order gossip validation checks cheapest first — <i>implemented · medium · S · cpu, disk, latency</i></summary>

**Idea.** Order gossip validation rules so cheap structural REJECT checks run first, then cheap in-memory IGNOREs (slot window, bit lengths, committee bits, seen cache, invalid block, parent root, target epoch), then state loads, pool lookups, shuffling and signature checks, so invalid messages are dropped before costly work.

**Gap in Lighthouse.** Minor: the aggregate path computes the tree_hash_root of ObservedAttestationKey before the cheap committee-index check; negligible.

**Impact.** Already drops invalid messages before state loads and BLS; no meaningful saving left.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:902-980`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L902-L980) unaggregated: target epoch, slot range, committee index, fork-choice head block, target root, then pubkey length and observed attester before signature
- [`beacon_node/beacon_chain/src/attestation_verification.rs:530-640`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L530-L640) aggregate: slot range, epoch, committee index, observed subset, observed aggregator, head block known, non-empty bits, then committee/signatures
- [`beacon_node/beacon_chain/src/block_verification.rs:900-1060`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L900-L1060) gossip block: fork, future slot, blob count, finalized, duplicate, invalid roots, parent known, then proposer cache, then signature
- [`beacon_node/beacon_chain/src/sync_committee_verification.rs:462`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/sync_committee_verification.rs#L462) slot range, subnet, seen, then signature

**Sources.** [grandine@998a78869](https://github.com/grandinetech/grandine/commit/998a78869f84), [lodestar#9984](https://github.com/ChainSafe/lodestar/pull/9984), [nimbus#1379](https://github.com/status-im/nimbus-eth2/pull/1379), [nimbus#9189](https://github.com/status-im/nimbus-eth2/pull/9189), [nimbus#5610](https://github.com/status-im/nimbus-eth2/pull/5610), [teku#9595](https://github.com/Consensys-Incorporated/teku/pull/9595), [lodestar#2760](https://github.com/ChainSafe/lodestar/pull/2760), [prysm#7671](https://github.com/OffchainLabs/prysm/pull/7671), [lodestar@c56940770](https://github.com/ChainSafe/lodestar/commit/c56940770ccc)

</details>


<a id="gossip_validation-030"></a>
<details>
<summary><b>gossip_validation-030</b> Cheap sidecar checks before proposer BLS signature — <i>partial · medium · S · cpu</i></summary>

**Idea.** On blob/column sidecar gossip, run cheap checks (proposer index, seen index, parent seen) before proposer signature verification so invalid or duplicate sidecars do not cost a BLS check.

**Gap in Lighthouse.** In verify_proposer_and_signature (used by full and partial column headers, data_column_verification.rs:654 and 1185) compare signed_block_header.message.proposer_index to the cached expected index before verify_signature and return ProposerIndexMismatch; optionally the same for gossip blocks. Blob sidecars no longer exist in this tree.

**Impact.** Saves one BLS verify (~1-2 ms) per sidecar carrying a wrong proposer index; only matters under attack.

**Best measured result.** Attack estimate: signature verification about 2ms each, hundreds of malicious sidecars per validator (pr:prysm#13347)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_column_verification.rs:1150-1185`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1150-L1185) subnet, future/finalized slot, seen index (verify_is_unknown_sidecar), DA-cache PriorKnownUnpublished, inclusion proof and parent-known checks all run before verify_proposer_and_signature
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2486-2496`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2486-L2496) partial-column headers already verified for a block_root are reused from cache without a new BLS check
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1776-1801`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1776-L1801) proposer_index equality checked only after signed_block_header.verify_signature
- [`beacon_node/beacon_chain/src/block_verification.rs:1052-1103`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1052-L1103) IncorrectBlockProposer checked after BLS verify

**Second check.** Beyond the earlier review, found that the DA-checker PriorKnownUnpublished early return and the partial-column header cache also skip BLS for already-known data, but the proposer-index comparison is still after the signature check, so partial stands.

**Sources.** [lodestar@27f4ad4ae](https://github.com/ChainSafe/lodestar/commit/27f4ad4ae8ae), [prysm#13346](https://github.com/OffchainLabs/prysm/pull/13346), [prysm#13347](https://github.com/OffchainLabs/prysm/pull/13347)

</details>


<a id="gossip_validation-031"></a>
<details>
<summary><b>gossip_validation-031</b> Cheap checks before loading pre-state — <i>implemented · medium · cpu, disk</i></summary>

**Idea.** Run state-independent checks (time window, invalid-block reference, already imported) and use cached genesis time before loading or regenerating the head/parent state, so rejected messages never touch state.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:918-975`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L918-L975) future-slot, finalized slot, fork-choice contains_block, check_invalid_block_roots, finalized-descendant, parent-in-fork-choice all before any state load
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1298`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1298) slot range uses slot_clock (no state/genesis read)

**Sources.** [lodestar@755ae5056](https://github.com/ChainSafe/lodestar/commit/755ae5056acf), [prysm#6755](https://github.com/OffchainLabs/prysm/pull/6755), [teku#3087](https://github.com/Consensys-Incorporated/teku/pull/3087)

</details>


<a id="gossip_validation-033"></a>
<details>
<summary><b>gossip_validation-033</b> Seen-check sidecars first before KZG and signature — <i>implemented · medium · cpu, bandwidth</i></summary>

**Idea.** For blob and data column sidecar gossip, do the already-seen (block header/slot, proposer, index) IGNORE check first, before KZG, signature and other checks, so duplicates are neither revalidated nor re-propagated.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_column_verification.rs:1139-1160`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1139-L1160) verify_is_unknown_sidecar runs right after cheap structural/slot checks, before inclusion proof, signature and KZG
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1647`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1647) observed_column_sidecars keyed by (slot, proposer, index)
- [`beacon_node/beacon_chain/src/blob_verification.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/blob_verification.rs) has no gossip path (blob sidecars removed)

**Sources.** [teku#7963](https://github.com/Consensys-Incorporated/teku/pull/7963), [prysm#17347](https://github.com/OffchainLabs/prysm/pull/17347), [nimbus#5563](https://github.com/status-im/nimbus-eth2/pull/5563), [lodestar#8542](https://github.com/ChainSafe/lodestar/pull/8542)

</details>


<a id="gossip_validation-035"></a>
<details>
<summary><b>gossip_validation-035</b> Seen-attestation cache checked first in attestation validation — <i>implemented · medium · cpu</i></summary>

**Idea.** Check the recently-seen attestation cache at the very start of attestation validation and exit early on a hit.

**Impact.** Duplicate unaggregated attestations are rejected before committee lookup and signature work; the only work ahead of the check is a few cheap fork-choice lookups, so moving it first would save almost nothing.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:994-1011`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L994-L1011) verify_middle_checks: observed_gossip_attesters.validator_has_been_observed read-lock lookup before committee lookup and BLS
- [`beacon_node/beacon_chain/src/attestation_verification.rs:902-980`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L902-L980) early checks (slot range, fork-choice head/target lookups) run first, all cheap

**Sources.** [prysm#4206](https://github.com/OffchainLabs/prysm/pull/4206)

</details>


<a id="gossip_validation-036"></a>
<details>
<summary><b>gossip_validation-036</b> Compact key for seen unaggregated attestation cache — <i>implemented · low · cpu, memory</i></summary>

**Idea.** Key the seen-unaggregated-attestation cache by a compact fixed-size key (e.g. attester index plus data) rather than a hashed or concatenated buffer including the full aggregation bitlist.

**Impact.** Already one bit per validator per epoch; no bitlist in key.

**Best measured result.** 169 ns/280 B/4 allocs -&gt; 31 ns/24 B/1 alloc (pr:prysm#14590)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/observed_attesters.rs:88`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_attesters.rs#L88) EpochBitfield: per-epoch bitfield indexed by validator index
- [`beacon_node/beacon_chain/src/attestation_verification.rs:997`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L997) observed_gossip_attesters.validator_has_been_observed(target epoch, attester index)

**Sources.** [prysm#14590](https://github.com/OffchainLabs/prysm/pull/14590), [prysm#15034](https://github.com/OffchainLabs/prysm/pull/15034)

</details>


<a id="gossip_validation-039"></a>
<details>
<summary><b>gossip_validation-039</b> Dedup slasher ingress before BLS and queueing — <i>not · medium · S · cpu, memory</i></summary>

**Idea.** Before slasher ingestion, dedup indexed attestations on (validator_index, data hash) and skip BLS verification and queue append for already staged ones, bounding the queue.

**Gap in Lighthouse.** Dedup at slasher ingress on (validator_index, attestation_data_hash) and let process_slash_info skip BLS verify and queue append for already staged records (sigp/lighthouse#10107, not merged in this base).

**Impact.** Only for --slasher nodes: saves one BLS verify per known-attestation replay and bounds ingress queue memory.

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/attestation_queue.rs:21-25`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/attestation_queue.rs#L21-L25) AttestationQueue is a Mutex&lt;Vec&gt;, no ingress dedup
- [`slasher/src/attestation_queue.rs:53-75`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/attestation_queue.rs#L53-L75) (validator_index, data_hash) dedup only in AttestationBatch at dequeue
- [`slasher/src/slasher.rs:83-85`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/slasher.rs#L83-L85) accept_attestation just queues
- [`beacon_node/beacon_chain/src/attestation_verification.rs:494-504`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L494-L504) process_slash_info BLS-verifies then accepts every replay

**Second check.** Re-read the slasher queue, Slasher::accept_attestation and process_slash_info; the only dedup is batch-time in AttestationBatch, after signature verify and queueing.

**Sources.** [lighthouse#10107](https://github.com/sigp/lighthouse/pull/10107)

</details>


<a id="gossip_validation-041"></a>
<details>
<summary><b>gossip_validation-041</b> Ignore further blocks from same proposer and slot — <i>partial · medium · S · cpu</i></summary>

**Idea.** Once a validly signed block for (proposer, slot) was seen, ignore any further gossip block for that pair so duplicates and equivocations are not re-validated or imported.

**Gap in Lighthouse.** Do a cheap (slot, proposer) lookup via proposer_has_been_observed early in GossipVerifiedBlock::new and ignore further blocks before parent load and signature verify, while still routing the first equivocation to observed_slashable/slasher.

**Impact.** Equivocating or duplicate-id blocks still cost a proposer lookup, possible state load and a BLS verify; small except under equivocation floods.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:969-972`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L969-L972) only early pre-check is fork_choice contains_block
- [`beacon_node/beacon_chain/src/block_verification.rs:1076-1098`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1076-L1098) observe_slashable/observe_proposal (Slashable/Duplicate rejection) only after proposer-cache lookup and BLS verify
- [`beacon_node/beacon_chain/src/observed_block_producers.rs:135`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_block_producers.rs#L135) proposer_has_been_observed used only in tests
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1561`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1561) DuplicateCache is keyed by block root and checked only after gossip verification

**Second check.** Also checked the beacon processor DuplicateCache and gossip_methods block path; both act by block root and after verification, so they do not short-circuit a second block for the same (proposer, slot).

**Sources.** [nimbus#9280](https://github.com/status-im/nimbus-eth2/pull/9280)

</details>


<a id="gossip_validation-042"></a>
<details>
<summary><b>gossip_validation-042</b> Atomic seen check-and-set for concurrent duplicates — <i>partial · medium · M · cpu</i></summary>

**Idea.** Mark a block or blob as seen in one locked check-and-set (or lock around validation) so concurrent duplicates from several peers are processed only once.

**Gap in Lighthouse.** Claim the (slot, proposer[, index]) key in-flight at the early check (released on failure) in GossipVerifiedBlock::new and validate_data_column_sidecar_for_gossip_fulu/gloas, so concurrent distinct-id duplicates do the signature/KZG work once.

**Impact.** Saves repeated BLS/KZG work for concurrent distinct-message-id copies; gossipsub message-id dedup already removes byte-identical copies.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1087-1098`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1087-L1098) atomic check-and-set under observed_block_producers write lock, after signature verify
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1646-1665`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1646-L1665) verify_is_unknown_sidecar is a read-lock check only
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1166-1176`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1166-L1176) early exit only if the column is already in the DA checker
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1548-1561`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1548-L1561) DuplicateCache check_and_insert happens after gossip verification, guards import not validation

**Second check.** Checked the beacon processor DuplicateCache and DA-checker early exit as possible equivalents; neither makes the seen-check atomic before the expensive validation.

**Sources.** [prysm#13109](https://github.com/OffchainLabs/prysm/pull/13109), [prysm#3567](https://github.com/OffchainLabs/prysm/pull/3567)

</details>


<a id="gossip_validation-044"></a>
<details>
<summary><b>gossip_validation-044</b> Ignore aggregates whose bits are subset of seen ones — <i>implemented · medium · bandwidth, cpu</i></summary>

**Idea.** For each attestation data (and committee index post-Electra) track the aggregation bits of seen gossip aggregates and sync contributions, and ignore a new one whose bits are a (non-strict) subset of an already seen one, before signature verification. This skips BLS work and re-propagation for redundant aggregates.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:569-581`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L569-L581) observed_attestations.is_known_subset in aggregate verify_early_checks before signature, returns AttestationSupersetKnown
- [`beacon_node/beacon_chain/src/attestation_verification.rs:783-794`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L783-L794) observe_item again in verify_late_checks for races
- [`beacon_node/beacon_chain/src/sync_committee_verification.rs:334-342`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/sync_committee_verification.rs#L334-L342) same subset check for sync contributions
- [`beacon_node/beacon_chain/src/observed_aggregates.rs:262-300`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_aggregates.rs#L262-L300) SlotHashSet subset/superset logic keyed by data root + committee index (ObservedAttestationKey)

**Sources.** [nimbus#7043](https://github.com/status-im/nimbus-eth2/pull/7043), [nimbus#3439](https://github.com/status-im/nimbus-eth2/pull/3439), [prysm#4451](https://github.com/OffchainLabs/prysm/pull/4451), [lighthouse#3493](https://github.com/sigp/lighthouse/pull/3493), [prysm#10674](https://github.com/OffchainLabs/prysm/pull/10674), [nimbus#4490](https://github.com/status-im/nimbus-eth2/pull/4490)

</details>


<a id="gossip_validation-045"></a>
<details>
<summary><b>gossip_validation-045</b> Seen-aggregate root cache checked before any validation work — <i>implemented · medium · bandwidth, cpu, latency</i></summary>

**Idea.** Keep a per-slot seen cache of aggregate hash tree roots and aggregator messages (fed from gossip, API, blocks and local production), hashing the aggregate once, and ignore an already seen gossip aggregate at the start of validation, before signature, state work, pool insertion or propagation.

**Impact.** Minor: locally produced aggregates are not pre-seeded, and the key is the data root plus committee index rather than the full aggregate root, which is an equivalent filter.

**Best measured result.** None (pr:lodestar#4019)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:553-581`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L553-L581) key root = tree_hash_root(ObservedAttestationKey) computed once, then is_known_subset before head-block check, committee/state work, signature and pool insertion
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5022-5050`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5022-L5050) import_block_observe_attestations feeds block attestations into observed_attestations
- [`beacon_node/beacon_chain/src/attestation_verification.rs:589-600`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L589-L600) observed_aggregators check by aggregator index and epoch

**Sources.** [nimbus#2170](https://github.com/status-im/nimbus-eth2/pull/2170), [lodestar#2329](https://github.com/ChainSafe/lodestar/pull/2329), [lodestar#4019](https://github.com/ChainSafe/lodestar/pull/4019), [teku#2099](https://github.com/Consensys-Incorporated/teku/pull/2099), [lodestar#7890](https://github.com/ChainSafe/lodestar/pull/7890), [lodestar@3ce36410e](https://github.com/ChainSafe/lodestar/commit/3ce36410ef5e)

</details>


<a id="gossip_validation-046"></a>
<details>
<summary><b>gossip_validation-046</b> Cache validation work per distinct AttestationData — <i>not · medium · M · cpu</i></summary>

**Idea.** Cache per-slot gossip attestation validation results (signing root, data root, head/target checks, committee) keyed by serialized AttestationData plus committee bits, so many attestations and aggregates with identical data hash and check once; keep lookup and insert keys consistent.

**Gap in Lighthouse.** Per-slot cache keyed by (AttestationData root, committee index) holding signing root and head/target check results, reused in verify_early_checks and signature-set construction; in batch mode compute each distinct data's signing root once.

**Impact.** Saves one AttestationData hash plus fork-choice lookups per attestation; small vs BLS in Rust, low single-digit percent of gossip attestation CPU.

**Best measured result.** validateGossipAttestation was ~12% of CPU (5.8% signing root, 3.9% head/target check); reduced to under 3%; cache &lt;300kb per slot (pr:lodestar#5333)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/signature_sets.rs:313-320`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/signature_sets.rs#L313-L320) get_domain and data.signing_root recomputed per attestation
- [`beacon_node/beacon_chain/src/attestation_verification/batch.rs:60-93`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification/batch.rs#L60-L93) batch path builds a set per attestation with no per-data root reuse
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1244`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1244) verify_head_block_is_known and 1379 verify_attestation_target_root per attestation

**Second check.** Searched attestation_verification, its batch module and signature_sets for any data-root or signing-root memoisation; only shuffling/pubkey caches exist, which every client has.

**Sources.** [silver#181](https://github.com/gattaca-com/silver/pull/181), [lodestar#6788](https://github.com/ChainSafe/lodestar/pull/6788), [teku#4572](https://github.com/Consensys-Incorporated/teku/pull/4572), [lodestar#5333](https://github.com/ChainSafe/lodestar/pull/5333), [lodestar#6802](https://github.com/ChainSafe/lodestar/pull/6802), [lodestar#7589](https://github.com/ChainSafe/lodestar/pull/7589)

</details>


<a id="gossip_validation-047"></a>
<details>
<summary><b>gossip_validation-047</b> Verify proposer header signature once across sidecars — <i>partial · medium · S · cpu, latency</i></summary>

**Idea.** Cache verified (block root/header, proposer signature) results so the block and its blob/column sidecars sharing the same header skip re-verifying the proposer signature.

**Gap in Lighthouse.** Full Fulu data column sidecars (and the gossip block) do not consult the per-block-root verified header held by PartialDataColumnAssembler; check it (or a small signed-header-root cache) before verify_proposer_and_signature, and fill it from GossipVerifiedBlock::new.

**Impact.** For a node custodying many columns, saves ~1 ms BLS plus proposer lookup per extra full column per block; partial-column traffic already benefits.

**Best measured result.** Verification takes 20-40 ms on hoodi; now once per slot (pr:lodestar#8620)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2493-2500`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2493-L2500) verify_partial_data_column_header_for_gossip returns the cached verified header per block root and skips re-verification
- [`beacon_node/beacon_chain/src/partial_data_column_assembler.rs:248-253`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/partial_data_column_assembler.rs#L248-L253) get_header; 176-190 header cached from verified full columns too
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1331-1335`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1331-L1335) partial columns without header reuse the cached one
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1185`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1185) full Fulu column sidecars still call verify_proposer_and_signature every time (1732-1790)
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1217-1285`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1217-L1285) Gloas columns carry no signed header, so no per-column proposer signature

**Second check.** The earlier review missed the partial-column header cache in PartialDataColumnAssembler, which already verifies a block's header once and reuses it; the full-column and block paths do not share it.

**Sources.** [lodestar#8620](https://github.com/ChainSafe/lodestar/pull/8620), [nimbus#7949](https://github.com/status-im/nimbus-eth2/pull/7949), [teku#7749](https://github.com/Consensys-Incorporated/teku/pull/7749)

</details>


<a id="gossip_validation-049"></a>
<details>
<summary><b>gossip_validation-049</b> Compute gossip block root once and reuse it — <i>implemented · low · cpu, latency</i></summary>

**Idea.** Compute the block root once during gossip validation and carry it in the verified block/blob for proposer signature checks, error/reject paths and later stages instead of re-hashing; check slot before reading the database.

**Impact.** Root hashed once per gossip block via header; nothing left to save.

**Best measured result.** None (pr:lighthouse#4277)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:890`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L890) block root from header root (body hash already cached), computed once
- [`beacon_node/beacon_chain/src/block_verification.rs:900`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L900) BlockErrorWithRoot carries block_root into error paths
- [`beacon_node/beacon_chain/src/block_verification.rs:1134`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1134) root stored in GossipVerifiedBlock; block_verification.rs:918 slot check precedes finalized/fork-choice lookups

**Sources.** [prysm#13657](https://github.com/OffchainLabs/prysm/pull/13657), [lighthouse#4949](https://github.com/sigp/lighthouse/pull/4949), [nimbus#3143](https://github.com/status-im/nimbus-eth2/pull/3143), [lighthouse#4277](https://github.com/sigp/lighthouse/pull/4277)

</details>


<a id="gossip_validation-050"></a>
<details>
<summary><b>gossip_validation-050</b> Cache invalid block roots to reject descendants — <i>partial · medium · M · cpu, latency</i></summary>

**Idea.** Keep a bounded cache of block roots that failed validation, and immediately reject gossip blocks, attestations and aggregates that are, reference or build on them, without repeating state work or full verification when they arrive from other peers.

**Gap in Lighthouse.** No dynamic bounded cache of roots that failed consensus validation. Children of an invalid block trigger parent lookups and re-verification; attestations to it go to the unknown-block reprocess queue. Add an LRU filled on state-transition/signature failures and checked in GossipVerifiedBlock::new_without_slasher_checks, column/envelope gossip verification and attestation verification.

**Impact.** Skips repeated parent fetch, state load and state transition for re-gossiped invalid blocks and their descendants/attestations; matters only under attack or fork spam.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:3879`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3879) check_invalid_block_roots reads only static config.invalid_block_roots
- [`beacon_node/beacon_chain/src/chain_config.rs:108`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/chain_config.rs#L108) invalid_block_roots is a fixed HashSet
- [`beacon_node/beacon_chain/src/block_verification.rs:976`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L976) gossip block path consults it
- [`beacon_node/network/src/sync/block_lookups/mod.rs:282`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L282),369 ignored_chains LRUTimeCache, filled only for parent chains that are too long, not for invalid blocks
- [`beacon_node/network/src/sync/range_sync/range.rs:77`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/range.rs#L77),352 failed_chains LRU covers range-sync targets only

**Second check.** Checked sync-side caches (block_lookups ignored_chains, range_sync failed_chains): both are LRU caches of roots, but neither is filled on invalid-block results and neither is consulted on gossip. Gossipsub's duplicate cache only drops byte-identical messages.

**Sources.** [prysm#6726](https://github.com/OffchainLabs/prysm/pull/6726), [teku#4963](https://github.com/Consensys-Incorporated/teku/pull/4963), [prysm#3685](https://github.com/OffchainLabs/prysm/pull/3685), [lighthouse#9730](https://github.com/sigp/lighthouse/pull/9730)

</details>


<a id="gossip_validation-052"></a>
<details>
<summary><b>gossip_validation-052</b> Check snappy declared length before decompressing — <i>implemented · medium · bandwidth, cpu, memory</i></summary>

**Idea.** Read the uncompressed length from the snappy header and reject gossip messages outside the topic's valid size range (max gossip payload) before allocating, decompressing or SSZ decoding, including in the message-id function, so oversized messages cost no CPU or memory.

**Impact.** Already avoids allocating or decompressing oversized messages.

**Best measured result.** Prevents multi-GB allocation from a ~12MB message (pr:ethlambda#199)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/pubsub.rs:108-120`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L108-L120) SnappyTransform::inbound_transform checks compressed len, then decompress_len() against max_uncompressed_len before decompress_vec
- [`beacon_node/lighthouse_network/src/config.rs:510`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L510) max_transmit_size set; message-id fn runs on already-transformed data

**Sources.** [ethlambda#199](https://github.com/lambdaclass/ethlambda/pull/199), [prysm#6663](https://github.com/OffchainLabs/prysm/pull/6663), [teku#8899](https://github.com/Consensys-Incorporated/teku/pull/8899), [teku#2738](https://github.com/Consensys-Incorporated/teku/pull/2738), [teku#1010](https://github.com/Consensys-Incorporated/teku/pull/1010)

</details>


<a id="gossip_validation-053"></a>
<details>
<summary><b>gossip_validation-053</b> Bound column sidecar size by max blobs early — <i>partial · medium · S · cpu, memory</i></summary>

**Idea.** Reject data column sidecars carrying more blobs than the fork's max blobs per block at the decompression/size check stage, before queueing, decode or KZG work.

**Gap in Lighthouse.** For Fulu, columns are decoded (bounded only by the SSZ type limit MaxBlobCommitmentsPerBlock) and queued before the max-blobs-per-block check. Add a Fulu size cap from the topic epoch's max_blobs_per_block in PubsubMessage::decode, or set a per-topic gossipsub max transmit size.

**Impact.** Rejects oversized Fulu columns before decode and queueing; saves memory/CPU only against malicious peers.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/pubsub.rs:279-292`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L279-L292) size cap before SSZ decode, Gloas only
- [`beacon_node/lighthouse_network/src/types/pubsub.rs:106-121`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L106-L121) SnappyTransform only enforces global max_payload_size/max_compressed_len
- [`beacon_node/lighthouse_network/src/config.rs:510`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L510) single global gossipsub max_transmit_size; per-topic max_transmit_size_for_topic in the sigp rust-libp2p gossipsub (protocols/gossipsub/src/config.rs:266, behaviour.rs:637) is unused by Lighthouse
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1516`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1516) verify_commitments_len_within_max_blobs runs in the worker after decode and queueing

**Second check.** Also checked the gossipsub dependency: it supports a per-topic transmit size, but Lighthouse sets only the global max_transmit_size. The snappy transform uses only global limits.

**Sources.** [lighthouse#8198](https://github.com/sigp/lighthouse/pull/8198), [lodestar#10076](https://github.com/ChainSafe/lodestar/pull/10076)

</details>


<a id="gossip_validation-054"></a>
<details>
<summary><b>gossip_validation-054</b> Bound pending, deferred and future-slot gossip queues — <i>implemented · medium · cpu, memory</i></summary>

**Idea.** Cap, prune and expire queues of gossip blocks, attestations and sidecars held for an unknown parent or future slot (entry count, per-entry cell count, retained slot window, drop oldest) and run cheap structure checks at admission, so peers cannot pin unbounded memory.

**Gap in Lighthouse.** Caps are by entry count with delay-queue expiry; no per-entry cell/byte accounting, and unknown-parent blocks go to sync lookups rather than a held queue.

**Impact.** Memory is already bounded by counts; byte-weighted accounting would only tighten worst case.

**Best measured result.** SSZ max 4096 cells with 8-root/128-column queue allows ~8 GiB heap held (pr:prysm#16831)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:78-90`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L78-L90) MAXIMUM_QUEUED_BLOCKS 16, ENVELOPES 16, ATTESTATIONS 16384, DATA_COLUMNS 256
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:867`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L867) drops when column count full
- [`beacon_node/beacon_processor/src/scheduler/work_queue.rs:384-386`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_queue.rs#L384-L386) per-type queues capped at 1024
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:595`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L595) attestation queue cap

**Sources.** [caplin#23645](https://github.com/erigontech/erigon/pull/23645), [prysm#16831](https://github.com/OffchainLabs/prysm/pull/16831), [teku#2880](https://github.com/Consensys-Incorporated/teku/pull/2880), [prysm#16470](https://github.com/OffchainLabs/prysm/pull/16470), [caplin#12733](https://github.com/erigontech/erigon/pull/12733), [caplin#23834](https://github.com/erigontech/erigon/pull/23834), [lodestar#10388](https://github.com/ChainSafe/lodestar/pull/10388), [lodestar#10395](https://github.com/ChainSafe/lodestar/pull/10395), [prysm#3799](https://github.com/OffchainLabs/prysm/pull/3799)

</details>


<a id="gossip_validation-055"></a>
<details>
<summary><b>gossip_validation-055</b> Reject future-slot messages before queueing or hashing — <i>partial · medium · S · memory, cpu</i></summary>

**Idea.** Reject gossip blocks and sidecars whose slot is beyond wall clock plus disparity before computing hash tree roots or inserting them into pending queues, with one shared helper.

**Gap in Lighthouse.** The block body hash_tree_root is computed before the future-slot check, and nothing rejects far-future slots before the block is queued. Move the now_with_future_tolerance check to before signed_block_header() in GossipVerifiedBlock::new; a check before queueing would need a slot peek in the router.

**Impact.** Far-future blocks skip one full body hash_tree_root; negligible on honest traffic.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:886-890`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L886-L890) signed_block_header() (body tree hash) and get_block_header_root run first
- [`beacon_node/beacon_chain/src/block_verification.rs:915-925`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L915-L925) FutureSlot check comes after that, in new_without_slasher_checks
- [`beacon_node/lighthouse_network/src/types/pubsub.rs:262-275`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L262-L275) blocks decoded in full with no slot check before queueing
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1157`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1157) column future-slot check comes early

**Second check.** Re-read GossipVerifiedBlock::new and the decode path. No earlier slot check exists in pubsub decode or in the router. There is no shared future-slot helper; each verifier does its own check.

**Sources.** [prysm#17157](https://github.com/OffchainLabs/prysm/pull/17157), [prysm#17167](https://github.com/OffchainLabs/prysm/pull/17167), [nimbus#9180](https://github.com/status-im/nimbus-eth2/pull/9180)

</details>


<a id="gossip_validation-056"></a>
<details>
<summary><b>gossip_validation-056</b> Cap in-flight gossip validations per large topic — <i>partial · medium · M · cpu, memory</i></summary>

**Idea.** Limit concurrent in-flight validations per large-message topic and drop excess before SSZ decode; ignore envelopes whose state is not cached instead of regenerating.

**Gap in Lighthouse.** There is no per-topic cap on in-flight validations before decode; queues are bounded by count after decode. Envelope verification loads the state from the store instead of ignoring when the state is not cached; external builder envelopes always load it. Add a per-topic limit before PubsubMessage::decode and an ignore-on-miss path in envelope gossip verification.

**Impact.** Bounds memory and state loads under envelope or large-topic floods; little effect on healthy nodes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_queue.rs:384-386`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_queue.rs#L384-L386) count-bounded queues per work type
- [`beacon_node/lighthouse_network/src/types/pubsub.rs:195-433`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L195-L433) SSZ decode in the network layer before queueing
- [`beacon_node/beacon_chain/src/payload_envelope_verification/gossip_verified_envelope.rs:237`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/gossip_verified_envelope.rs#L237),274 load_snapshot_from_state_root on proposer cache miss and for every external builder envelope

**Second check.** Searched the sigp rust-libp2p gossipsub checkout for validation backpressure or in-flight limits and found none; its only per-topic limit is transmit size. Confirmed that the external builder path always loads the state (TODO builder pubkey cache).

**Sources.** [teku#11359](https://github.com/Consensys-Incorporated/teku/pull/11359)

</details>


<a id="gossip_validation-057"></a>
<details>
<summary><b>gossip_validation-057</b> Keep compressed payload in gossip validation queue — <i>not · medium · L · memory</i></summary>

**Idea.** Hold only the compressed payload plus a small decoded prefix for queued gossip messages, decompress in the worker, apply a byte-weighted per-topic limit, and read slot from fixed SSZ offset to drop far-future blocks before decoding.

**Gap in Lighthouse.** Queued gossip work holds fully decoded objects. There is no compressed-payload queue, no byte-weighted limit and no fixed-offset slot peek. Implementing this needs decompress and decode moved into the worker, plus a byte-budgeted queue in lighthouse_network/network and beacon_processor.

**Impact.** Less heap held per queued block under flood (Teku measured 6.2 MiB to 0.2 MiB); mostly attack resilience.

**Best measured result.** held heap per queued block 6.20 MiB -&gt; 0.20 MiB; far-future block flood no longer OOMs (pr:teku#11503)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/pubsub.rs:106-125`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L106-L125) snappy decompression in gossipsub inbound_transform on the network thread
- [`beacon_node/lighthouse_network/src/types/pubsub.rs:262-275`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L262-L275) SignedBeaconBlock::from_ssz_bytes_by_fork full decode before queueing
- [`beacon_node/beacon_processor/src/scheduler/work_queue.rs:384`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_queue.rs#L384) count-only queue limits

**Second check.** Checked the transform and decode path and the gossipsub dependency: decompression and decode are both eager. No lazy or byte-weighted queue exists under any name.

**Sources.** [teku#11503](https://github.com/Consensys-Incorporated/teku/pull/11503)

</details>


<a id="gossip_validation-059"></a>
<details>
<summary><b>gossip_validation-059</b> Reject pre-finalized gossip blocks and attestations — <i>implemented · medium · cpu, bandwidth</i></summary>

**Idea.** Reject gossip blocks and attestations older than the finalized epoch before processing, so old forks cannot trigger recursive parent lookups.

**Impact.** Already prevents old forks from triggering parent lookups.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:964`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L964) check_block_against_finalized_slot before parent lookup
- [`beacon_node/beacon_chain/src/block_verification.rs:1843`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1843) WouldRevertFinalizedSlot
- [`beacon_node/beacon_chain/src/block_verification.rs:979`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L979) check_block_is_finalized_checkpoint_or_descendant
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1270`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1270) and :1519 finalized-checkpoint-or-descendant check
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1157`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1157) PastFinalizedSlot

**Sources.** [prysm#3925](https://github.com/OffchainLabs/prysm/pull/3925)

</details>


<a id="gossip_validation-061"></a>
<details>
<summary><b>gossip_validation-061</b> Skip gossip validation while syncing or far behind — <i>implemented · low · cpu, sync</i></summary>

**Idea.** While the node is syncing or more than a few slots behind head (head state too old), do not validate gossip operations such as attestations and aggregates (keep blocks and blobs), since the results cannot be used and the work is wasted.

**Gap in Lighthouse.** Gate is on SyncState (SyncingFinalized/Head), not on head being N slots old, so a node merely a few slots behind but reported Synced still validates.

**Impact.** Wasted attestation/aggregate validation during sync is already skipped.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:1211`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1211) drops work with drop_during_sync when sync_state.is_syncing()
- [`beacon_node/network/src/network_beacon_processor/mod.rs:117`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L117),162,290 attestations/aggregates/etc set drop_during_sync: true; blocks use false (lib.rs:240-309)

**Sources.** [caplin#11855](https://github.com/erigontech/erigon/pull/11855), [teku#9190](https://github.com/Consensys-Incorporated/teku/pull/9190), [prysm#3514](https://github.com/OffchainLabs/prysm/pull/3514)

</details>


<a id="gossip_validation-066"></a>
<details>
<summary><b>gossip_validation-066</b> Batch KZG verification of gossip column sidecars — <i>not · medium · M · cpu</i></summary>

**Idea.** Verify KZG proofs of multiple gossip data column sidecars together in a batch rather than one sidecar at a time.

**Gap in Lighthouse.** Gossip columns are KZG-verified one at a time. Add a batch work type in BeaconProcessor that drains several GossipDataColumnSidecar items, runs cheap gossip checks per item, then one validate_data_columns call with per-column fault attribution on failure.

**Impact.** One multi-pairing replaces N when many columns of one block arrive together; mainly helps supernodes; not measured.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:417`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L417) GossipDataColumnSidecar(AsyncFn) is one work item per sidecar
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1035`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1035) verify_kzg_for_data_column verifies one column via iter::once (also :1060 with_commitments variant)
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:342`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L342) awaiting_data_columns_per_root only delays columns, releases them individually

**Second check.** Also checked the reprocess queue (groups columns per root but releases them singly), the partial-column verify path, and all validate_data_columns callers: none batch gossip columns.

**Sources.** [nimbus#8314](https://github.com/status-im/nimbus-eth2/pull/8314)

</details>


<a id="gossip_validation-069"></a>
<details>
<summary><b>gossip_validation-069</b> Remove seen caches made redundant by other dedup — <i>not · low · S · bandwidth, cpu, memory</i></summary>

**Idea.** Drop a duplicate-filter or seen-attestation skip cache in gossip validation when another layer (gossip message-id dedup, op pool dedup, other checks) already filters the same duplicates, saving its memory and lookups.

**Gap in Lighthouse.** Remove observed_attestations/observed_sync_contributions and the AttestationSupersetKnown path in attestation_verification.rs, relying on gossipsub message-id dedup plus op pool dedup. Lighthouse relies on the subset check to skip BLS, so removal may cost CPU.

**Impact.** Frees some memory (Caplin saw 300MB for its own cache; LH cache is smaller and pruned by slot) but may add BLS work for redundant aggregates; marginal net.

**Best measured result.** Frees 300MB of memory (pr:caplin#12937)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:431`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L431) observed_attestations (ObservedAggregateAttestations) still exists
- [`beacon_node/beacon_chain/src/attestation_verification.rs:572`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L572) is_known_subset skip before BLS; :589 observed_aggregators
- beacon_node/PR lighthouse#2750 (removal) was closed unmerged

**Sources.** [caplin#12937](https://github.com/erigontech/erigon/pull/12937), [teku#4332](https://github.com/Consensys-Incorporated/teku/pull/4332), [lighthouse#2750](https://github.com/sigp/lighthouse/pull/2750)

</details>


<a id="gossip_validation-070"></a>
<details>
<summary><b>gossip_validation-070</b> Bypass queue gating for gossip blocks — <i>implemented · low · latency</i></summary>

**Idea.** Process gossip blocks immediately, bypassing the BLS-pool and regen availability gates other gossip objects wait on.

**Impact.** Lighthouse has no BLS-pool/regen availability gate on other gossip, so blocks are simply highest-priority gossip; nothing to bypass.

**Best measured result.** delay could exceed 2s in worst case (pr:lodestar#5263)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:929`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L929) gossip_block_queue popped before attestation queues, after chain segments/rpc blocks/delayed blocks
- [`beacon_node/beacon_processor/src/lib.rs:1239`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1239) GossipBlock dispatched immediately when can_spawn

**Sources.** [lodestar#5263](https://github.com/ChainSafe/lodestar/pull/5263)

</details>


<a id="gossip_validation-074"></a>
<details>
<summary><b>gossip_validation-074</b> Hold slightly-early gossip objects until their slot — <i>partial · low · M · cpu, latency</i></summary>

**Idea.** Put gossip blocks, attestations and other items that arrive slightly early (within clock disparity or one slot) into a bounded future queue and replay them at slot or interval start, instead of dropping or repeatedly retrying them.

**Gap in Lighthouse.** Attestations/aggregates/sync messages/data columns slightly early (within clock disparity) are rejected/dropped rather than queued. Add an Early* ReprocessQueueMessage for unaggregates/aggregates handled in gossip_methods.rs FutureSlot arms.

**Impact.** Avoids dropping and re-requesting legit slightly early attestations; small CPU/bandwidth effect, mostly correctness at slot boundaries.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:659`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L659) EarlyBlock held until slot start + 5ms (MAXIMUM_QUEUED_BLOCKS cap)
- beacon_node/work_reprocessing_queue.rs:~725 EarlyEnvelope likewise
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1308`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1308) attestations from future slots return FutureSlot; network/src/network_beacon_processor/gossip_methods.rs:2629 penalises peer and drops (no hold)

**Sources.** [ethlambda#318](https://github.com/lambdaclass/ethlambda/pull/318), [teku#3187](https://github.com/Consensys-Incorporated/teku/pull/3187), [lodestar@42eb9ff6f](https://github.com/ChainSafe/lodestar/commit/42eb9ff6f755)

</details>


<a id="gossip_validation-079"></a>
<details>
<summary><b>gossip_validation-079</b> Verify block signature before pending-queue insertion — <i>partial · medium · M · bandwidth, cpu, memory</i></summary>

**Idea.** Check the proposer index and signature of a gossip block before saving it to the unknown-parent or future-slot pool, keeping at most one per proposer and slot, so invalid or unsigned blocks cannot fill pools or trigger parent lookups and sync fetches.

**Gap in Lighthouse.** Future-slot (early block) pool already holds only signature-verified blocks. Unknown-parent blocks still reach sync lookups without proposer/signature checks and with no one-per-(proposer,slot) limit; only the global MAX_LOOKUPS cap and root dedup bound them. Verify the signature via the proposer cache (when the shuffling is known from the head/finalized chain) before sending UnknownParentBlock.

**Impact.** DoS hardening of parent lookups; little steady-state CPU saving.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:921`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L921) blocks past slot+clock-disparity are rejected (FutureSlot) before any pool
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1877`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1877) ReprocessQueueMessage::EarlyBlock is queued only with a fully gossip-verified block (proposer + signature checked, observed_block_producers updated)
- [`beacon_node/beacon_chain/src/block_verification.rs:990`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L990) verify_parent_block_and_envelope_are_known returns ParentUnknown before the signature check at :1055
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1693`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1693) ParentUnknown sends SyncMessage::UnknownParentBlock unsigned
- [`beacon_node/network/src/sync/block_lookups/mod.rs:77`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L77) MAX_LOOKUPS=200 cap and :276 PARENT_DEPTH_TOLERANCE bound lookups (dedup by root, not by proposer/slot)

**Second check.** Earlier review missed that Lighthouse's future-slot queue (EarlyBlock) stores only GossipVerifiedBlocks and far-future blocks are dropped, which covers the future-slot half of the idea; the unknown-parent half is still missing.

**Sources.** [prysm#13183](https://github.com/OffchainLabs/prysm/pull/13183), [teku#11438](https://github.com/Consensys-Incorporated/teku/pull/11438), [lodestar#10087](https://github.com/ChainSafe/lodestar/pull/10087)

</details>


<a id="gossip_validation-081"></a>
<details>
<summary><b>gossip_validation-081</b> Expire held unknown-root gossip messages — <i>implemented · low · memory</i></summary>

**Idea.** Expire buffered unknown-root gossip messages for blocks seen but never imported, so the global cap does not fill permanently.

**Impact.** Held unknown-root messages already expire; global cap cannot fill permanently.

**Best measured result.** counter stuck at 16385 for 3+ hours on mainnet node (pr:lodestar#10389)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:53`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L53) QUEUED_ATTESTATION_DELAY 12s expiry via attestations_delay_queue
- beacon_node/work_reprocessing_queue.rs:595 MAXIMUM_QUEUED_ATTESTATIONS cap; :1268 awaiting_attestations_per_root pruned on expiry (regression test :1847)
- beacon_node/work_reprocessing_queue.rs:864 unknown-block data columns have their own cap and delay

**Sources.** [lodestar#10389](https://github.com/ChainSafe/lodestar/pull/10389)

</details>


<a id="gossip_validation-085"></a>
<details>
<summary><b>gossip_validation-085</b> Per-(validator, epoch) seen caches checked before validation — <i>implemented · low · bandwidth, cpu, disk, memory</i></summary>

**Idea.** Dedupe gossip attestations and aggregates with in-memory seen caches keyed by (attester or aggregator index, target epoch) and check them before state loads and BLS verification, so duplicates from the same validator in an epoch cost a map lookup, not a DB lookup or signature check.

**Impact.** Duplicates cost a bitfield lookup rather than state load or BLS.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:997`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L997) observed_gossip_attesters check in verify_middle_checks before committee cache (:1076) and BLS (:1194)
- [`beacon_node/beacon_chain/src/attestation_verification.rs:589`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L589) observed_aggregators (aggregator, target epoch) checked in verify_early_checks before late checks/signature
- [`beacon_node/beacon_chain/src/observed_attesters.rs:308`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_attesters.rs#L308) AutoPruningEpochContainer

**Sources.** [teku#4727](https://github.com/Consensys-Incorporated/teku/pull/4727), [prysm#5158](https://github.com/OffchainLabs/prysm/pull/5158), [prysm#5698](https://github.com/OffchainLabs/prysm/pull/5698), [lodestar#857](https://github.com/ChainSafe/lodestar/pull/857), [lodestar@8d860f90e](https://github.com/ChainSafe/lodestar/commit/8d860f90ef40), [teku#11307](https://github.com/Consensys-Incorporated/teku/pull/11307)

</details>


<a id="gossip_validation-087"></a>
<details>
<summary><b>gossip_validation-087</b> Size seen caches for the validator set — <i>implemented · low · S · bandwidth, cpu</i></summary>

**Idea.** Size the seen-attester and seen-aggregator gossip caches from the validator count and committee/aggregator counts over several slots, so entries are not evicted before duplicates arrive and duplicates are not revalidated.

**Impact.** Nothing to gain; per-epoch bitfields sized from observed validator count avoid premature eviction.

**Best measured result.** None (pr:prysm#13756)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/observed_attesters.rs:26`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_attesters.rs#L26) MAX_CACHED_EPOCHS=4 epochs kept, pruned by epoch not LRU
- observed_attesters.rs:344-357 new epoch container sized from mean of prior epochs, default 16384

**Sources.** [prysm#13756](https://github.com/OffchainLabs/prysm/pull/13756), [prysm#9476](https://github.com/OffchainLabs/prysm/pull/9476)

</details>


<a id="gossip_validation-091"></a>
<details>
<summary><b>gossip_validation-091</b> Replace DB reads in gossip checks with in-memory state — <i>implemented · low · S · cpu, disk, latency</i></summary>

**Idea.** Answer bad-block and seen-proposer checks in gossip validation from in-memory caches or fork choice instead of a database read per message, or drop the DB check where fork choice membership already covers it.

**Impact.** No DB read on the hot accept path.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:971`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L971) fork choice contains_block for duplicates
- beacon_chain/src/beacon_chain.rs:3880 invalid roots is in-memory config set
- observed_block_producers.rs:87 in-memory HashMap seen proposals
- block_verification.rs:1893 store.block_exists only on NotFinalizedDescendant error path

**Sources.** [lodestar#2599](https://github.com/ChainSafe/lodestar/pull/2599), [lodestar#3107](https://github.com/ChainSafe/lodestar/pull/3107), [lodestar#2682](https://github.com/ChainSafe/lodestar/pull/2682)

</details>


<a id="gossip_validation-092"></a>
<details>
<summary><b>gossip_validation-092</b> Group queued attestations by data for batch verify — <i>not · medium · M · cpu</i></summary>

**Idea.** Index the gossip attestation queue by attestation data key and pop chunks of same-data messages together, so attestations sharing data can be batch-verified with shared work.

**Gap in Lighthouse.** Queue is not keyed by AttestationData; equal-data attestations are not grouped and their messages are hashed to curve separately. Key the queue by data root and pop same-data chunks, sharing signing-root computation and hash-to-curve (or aggregate same-message sets before multi-verify).

**Impact.** Saves hash-to-curve and repeated per-data checks; small share of attestation CPU.

**Best measured result.** None (pr:lodestar#5803)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:1010`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1010) attestation queue popped in plain batches, no key by data
- [`beacon_node/beacon_chain/src/attestation_verification/batch.rs:133`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification/batch.rs#L133) batch_verify_unaggregated_attestations builds one set per attestation
- [`crypto/bls/src/impls/blst.rs:36`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L36) verify_signature_sets passes one message per set to blst (no shared hash-to-curve for equal messages)

**Second check.** Checked beacon_processor for any data-root keyed queue and the blst batch-verify wrapper for same-message dedup; none found.

**Sources.** [lodestar#5803](https://github.com/ChainSafe/lodestar/pull/5803)

</details>


<a id="gossip_validation-097"></a>
<details>
<summary><b>gossip_validation-097</b> Bounded prioritized gossip work queue, blocks first — <i>implemented · low · S · bandwidth, cpu, latency</i></summary>

**Idea.** Put all gossip messages (attestations, slashings, exits) into bounded per-type queues pulled by a scheduler with bounded concurrency that prioritizes blocks over attestations, so attestation floods cannot starve or delay block processing.

**Impact.** Already in place; attestation floods cannot starve block processing.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:759-765`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L759-L765) WorkQueues with bounded per-type queues
- lib.rs:890 max_workers bound; lib.rs:955 blocks checked before attestations
- beacon_processor/src/scheduler/work_queue.rs:335-363 queue lengths from validator count

**Sources.** [lodestar#5195](https://github.com/ChainSafe/lodestar/pull/5195), [lodestar#5350](https://github.com/ChainSafe/lodestar/pull/5350), [lighthouse#1511](https://github.com/sigp/lighthouse/pull/1511), [lighthouse#1546](https://github.com/sigp/lighthouse/pull/1546), [lodestar#5444](https://github.com/ChainSafe/lodestar/pull/5444), [caplin#11790](https://github.com/erigontech/erigon/pull/11790)

</details>


<a id="gossip_validation-101"></a>
<details>
<summary><b>gossip_validation-101</b> Attestation admission budget scaled to traffic — <i>partial · low · M · cpu, memory</i></summary>

**Idea.** Rate-limit gossip attestation processing with a node-wide budget per window sized from expected traffic (subscribed subnets times active validators per slot and subnet, with headroom), so CPU is bounded without dropping legitimate attestations.

**Gap in Lighthouse.** Lighthouse bounds attestation work by queue length (sized from validator count) and drops on overflow rather than a per-window admission budget; CPU is bounded by workers and batching. A budget would need a counter in the router before sending attestation events to BeaconProcessor::send_gossip_attestation.

**Impact.** Little: Lighthouse already sheds load via bounded queue and batch BLS; a budget could cut dedup/decode CPU under floods but risks dropping legitimate attestations (Caplin dropped 39-99%).

**Best measured result.** None (pr:caplin#24970)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_queue.rs:357`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_queue.rs#L357) attestation_queue sized from active validators / slots_per_epoch
- beacon_processor/src/lib.rs:110 batch size 64, batching verification
- no time-window rate limiter found in network/src/network_beacon_processor/gossip_methods.rs

**Sources.** [caplin#12830](https://github.com/erigontech/erigon/pull/12830), [caplin#24970](https://github.com/erigontech/erigon/pull/24970)

</details>


<a id="gossip_validation-103"></a>
<details>
<summary><b>gossip_validation-103</b> Cheap raw-byte field reads without views — <i>n/a · low · S · cpu</i></summary>

**Idea.** Read fixed-offset fields like slot from raw SSZ gossip bytes with direct byte arithmetic rather than constructing a view or decoder object, to make pre-validation field extraction cheaper.

**Impact.** Rust SSZ decode of fixed-size containers is already direct byte reads with no view/lazy object; saving would be nanoseconds per message.

**Best measured result.** None (pr:lodestar#6941)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/pubsub.rs:254`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L254) SingleAttestation::from_ssz_bytes full decode
- pubsub.rs:266 SignedBeaconBlock::from_ssz_bytes_by_fork

**Sources.** [lodestar#6941](https://github.com/ChainSafe/lodestar/pull/6941)

</details>


<a id="gossip_validation-104"></a>
<details>
<summary><b>gossip_validation-104</b> Peek raw SSZ bytes to skip deserialization — <i>partial · medium · M · cpu, memory</i></summary>

**Idea.** Extract keys (attestation data bytes, block root) from serialized gossip bytes at fixed offsets and use them as seen-cache keys, fully deserializing only on a cache miss or not at all for already-imported objects; most attestations per slot share few data values.

**Gap in Lighthouse.** Byte-identical duplicates (same block/column/attestation from many mesh peers) are already dropped by the gossipsub duplicate cache, keyed on a hash of the raw bytes, before SSZ decode; IDONTWANT also suppresses them. Missing: peeking semantic keys from bytes, e.g. AttestationData bytes shared by thousands of distinct attestations, or a block root for an already-imported block re-sent with other bytes, to skip decode and per-data validation.

**Impact.** Remaining saving is per-attestation decode and shared-data work; smaller than the earlier review stated since duplicate blocks/columns never reach decode.

**Best measured result.** None (pr:lodestar#5363)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/config.rs:492`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L492) gossip_message_id = sha256(prefix+topic+decompressed bytes)
- accba72/protocols/gossipsub/src/behaviour.rs:1950 message id computed on raw bytes; :1985 duplicate_cache.insert drops repeats before the message reaches Lighthouse
- [`beacon_node/lighthouse_network/src/service/mod.rs:1390`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L1390) PubsubMessage::decode runs only for non-duplicate messages
- [`beacon_node/lighthouse_network/src/types/pubsub.rs:254`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L254) non-duplicate attestations always fully decoded, no data-bytes keyed cache

**Second check.** Earlier review missed that the gossipsub dependency dedups on a raw-bytes message id before PubsubMessage::decode, which covers the 'skip deserialization for already-seen objects' part for identical bytes.

**Sources.** [lodestar#5363](https://github.com/ChainSafe/lodestar/pull/5363), [lodestar#10419](https://github.com/ChainSafe/lodestar/pull/10419), [lodestar#7009](https://github.com/ChainSafe/lodestar/pull/7009)

</details>


<a id="gossip_validation-107"></a>
<details>
<summary><b>gossip_validation-107</b> Singleflight state replays for sidecar verification — <i>implemented · medium · cpu, memory</i></summary>

**Idea.** Deduplicate concurrent state replays/regenerations for the same target when many data column sidecars arrive at once and each needs the same verifying state.

**Impact.** Equivalent singleflight already exists via the OnceCell in the proposer cache; sidecar verification needs only the proposer shuffling.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs):~190 cache_entry.get_or_try_init OnceCell: concurrent misses share one state load and computation
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1746`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1746) verify_proposer_and_signature uses chain.with_proposer_cache

**Sources.** [prysm#16550](https://github.com/OffchainLabs/prysm/pull/16550)

</details>


<a id="gossip_validation-111"></a>
<details>
<summary><b>gossip_validation-111</b> Plain map for bounded seen key space — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Track already-seen slashed validator indices in a plain map instead of an LRU cache, since the key space is bounded and needs no eviction bookkeeping.

**Impact.** Nothing; plain set already used.

**Best measured result.** None (pr:prysm#8332)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/observed_operations.rs:27`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_operations.rs#L27) observed_validator_indices: HashSet&lt;u64&gt;, reset at fork boundary

**Sources.** [prysm#8332](https://github.com/OffchainLabs/prysm/pull/8332)

</details>


<a id="gossip_validation-113"></a>
<details>
<summary><b>gossip_validation-113</b> Precompute per-shuffling committee aggregate pubkeys — <i>not · medium · M · cpu</i></summary>

**Idea.** Precompute aggregate public keys per committee for the shuffling and derive aggregate keys by subtracting non-participants, and pass parsed views to avoid re-parsing and re-hashing in attestation validation.

**Gap in Lighthouse.** No per-committee precomputed aggregate pubkey; each aggregate sums participant pubkeys from scratch. Cache per-shuffling committee aggregate pubkeys and derive by subtracting non-participants when participation is high.

**Impact.** Cuts G1 additions per aggregate; small next to pairing cost; adds memory.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/signature_sets.rs:295`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/signature_sets.rs#L295) indexed_attestation_signature_set collects participant pubkeys per attestation
- [`crypto/bls/src/generic_signature_set.rs:119`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/generic_signature_set.rs#L119) verify aggregates the pubkey list each time (fast_aggregate_verify)
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:39`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L39) CachedShuffling holds committees only, no aggregate pubkeys

**Second check.** Searched beacon_node/consensus/crypto for AggregatePublicKey use: only the sync committee spec field and op-pool, nothing cached for attestation committees.

**Sources.** [silver#166](https://github.com/gattaca-com/silver/pull/166)

</details>


<a id="gossip_validation-114"></a>
<details>
<summary><b>gossip_validation-114</b> Use proposer lookahead to skip epoch transitions — <i>implemented · medium · cpu, latency, memory</i></summary>

**Idea.** Post-Fulu, read the expected proposer for gossip blocks and data column sidecars from the parent state's proposer lookahead instead of advancing a state across an epoch boundary or regenerating a block-slot state.

**Impact.** Post-Fulu the parent state already holds the lookahead, so no epoch transition is run and results are cached per decision root.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/core/chain_spec.rs:1176`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/core/chain_spec.rs#L1176) proposer_shuffling_decision_slot post-Fulu is end of epoch N-2
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:321`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L321) ensure_state_can_determine_proposers_for_epoch advances only if state epoch &lt; minimum epoch
- [`consensus/types/src/state/beacon_state.rs:1655`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1655) get_beacon_proposer_indices reads proposer_lookahead
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1746`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1746) and block_verification.rs:1031 use the proposer cache keyed by decision root

**Sources.** [prysm#16202](https://github.com/OffchainLabs/prysm/pull/16202), [lodestar#9959](https://github.com/ChainSafe/lodestar/pull/9959), [lodestar#9772](https://github.com/ChainSafe/lodestar/pull/9772), [caplin#25253](https://github.com/erigontech/erigon/pull/25253)

</details>


<a id="gossip_validation-115"></a>
<details>
<summary><b>gossip_validation-115</b> Read-only head or parent state, no copy — <i>partial · medium · S · cpu, latency, memory</i></summary>

**Idea.** Validate gossip objects (exits, BLS changes, blocks) against a read-only reference to the head or parent state instead of cloning the state per message.

**Gap in Lighthouse.** Exits, BLS changes and blocks already avoid per-message copies. Proposer/attester slashing gossip validation still clones (and may advance) the head state via wall_clock_state(); switch to the head snapshot reference when head slot equals wall-clock epoch.

**Impact.** Slashings are rare and milhouse clones share structure, so the saving is tiny.

**Best measured result.** None (pr:caplin#24523)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2845`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2845) voluntary exit uses head snapshot reference
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2894`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2894) proposer slashing calls wall_clock_state()
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2921`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2921) attester slashing calls wall_clock_state()
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1612`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1612) wall_clock_state = state_at_slot(now), clones head and may run per_slot_processing
- [`beacon_node/beacon_chain/src/block_verification.rs:1031`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1031) gossip block uses proposer cache, parent state only loaded on miss

**Second check.** Re-read the slashing paths and wall_clock_state; confirmed the earlier partial verdict.

**Sources.** [prysm#11932](https://github.com/OffchainLabs/prysm/pull/11932), [prysm#13014](https://github.com/OffchainLabs/prysm/pull/13014), [prysm#15972](https://github.com/OffchainLabs/prysm/pull/15972), [caplin#24523](https://github.com/erigontech/erigon/pull/24523)

</details>


<a id="gossip_validation-116"></a>
<details>
<summary><b>gossip_validation-116</b> Use cached checkpoint or advanced states for validation — <i>implemented · medium · cpu, latency, memory</i></summary>

**Idea.** Validate gossip aggregates, blocks and sync messages against already cached states (checkpoint/target state, pre-advanced slot state, parent post-state, tip state) instead of copying the head state or regenerating.

**Impact.** Already avoids head-state copies on gossip paths.

**Best measured result.** None (pr:prysm#5737)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:1076`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1076) attestations use shuffling cache via with_committee_cache, no state copy
- [`beacon_node/beacon_chain/src/block_verification.rs:1031`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1031) block proposer checked via proposer cache before loading parent
- [`beacon_node/beacon_chain/src/block_verification.rs:2065`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L2065) parent loaded with get_advanced_hot_state (pre-advanced by state_advance_timer.rs)

**Sources.** [prysm#5737](https://github.com/OffchainLabs/prysm/pull/5737), [lodestar#2261](https://github.com/ChainSafe/lodestar/pull/2261), [teku#3385](https://github.com/Consensys-Incorporated/teku/pull/3385), [prysm#12506](https://github.com/OffchainLabs/prysm/pull/12506), [prysm#17788](https://github.com/OffchainLabs/prysm/pull/17788), [lodestar@6b148f3b7](https://github.com/ChainSafe/lodestar/commit/6b148f3b7bbc)

</details>


<a id="gossip_validation-117"></a>
<details>
<summary><b>gossip_validation-117</b> Direct state lookup by block root — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** When the block is known to be at the message slot, fetch its post state directly by block root rather than via a slot-plus-root checkpoint-state path, avoiding queue locks and key scans per message.

**Impact.** Gossip checks use a shuffling cache hit, no state lookup, on the common path.

**Best measured result.** None (pr:teku#11215)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:315`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L315) with_cached_shuffling keyed by head block root via fork choice get_block
- shuffling_cache.rs:340-350 read-lock cache hit path; no checkpoint-state cache scan
- beacon_chain/src/payload_attestation_verification/gossip_verified_payload_attestation.rs:102 uses it

**Sources.** [teku#11215](https://github.com/Consensys-Incorporated/teku/pull/11215)

</details>


<a id="gossip_validation-118"></a>
<details>
<summary><b>gossip_validation-118</b> Synchronous cached state read, conditional pool add — <i>partial · low · S · cpu, latency</i></summary>

**Idea.** For payload attestation gossip, read the state synchronously from cache instead of the regen queue, and add messages to the pool only when this node is the next proposer.

**Gap in Lighthouse.** Cached read is done; missing the condition that pool add happens only when this node is the next proposer. Gate the call in process_gossip_payload_attestation_result on a proposer-duty check for next slot.

**Impact.** Saves a small op-pool insert per payload attestation on non-proposer nodes; likely minor (sub-ms each).

**Best measured result.** None (pr:lodestar#9969)

**Evidence (Lighthouse @ 928b61e719).**

- beacon_chain/src/payload_attestation_verification/gossip_verified_payload_attestation.rs:102-110 PTC from shuffling cache, no regen queue
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:4489`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L4489) add_payload_attestation_to_pool called unconditionally
- beacon_chain/src/beacon_chain.rs:2389 add_payload_attestation_to_pool

**Sources.** [lodestar#9969](https://github.com/ChainSafe/lodestar/pull/9969)

</details>


<a id="gossip_validation-119"></a>
<details>
<summary><b>gossip_validation-119</b> Small immutable validation view cache for bids — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Cache a small immutable view of the fields bid validation needs per (parent root, slot) instead of a full advanced parent state.

**Impact.** Lighthouse never builds a per-key advanced parent state for bids, so there is no 300 MB copy to avoid.

**Best measured result.** None (pr:caplin#25331)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/payload_bid_verification/gossip_verified_bid.rs:504`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_bid_verification/gossip_verified_bid.rs#L504) verify_payload_bid_for_gossip uses a context of caches, no state
- [`beacon_node/beacon_chain/src/payload_bid_verification/gossip_verified_bid.rs:125`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_bid_verification/gossip_verified_bid.rs#L125) state checks run on the cached head state, not a per-(parent,slot) advanced state

**Sources.** [caplin#25331](https://github.com/erigontech/erigon/pull/25331)

</details>


<a id="gossip_validation-121"></a>
<details>
<summary><b>gossip_validation-121</b> Signature check before state advance — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Run the BLS signature check against the un-advanced dependent state before advancing a state copy across an epoch boundary, so forged messages never trigger an epoch transition.

**Gap in Lighthouse.** Only a cache miss loads and advances a state (with_proposer_cache / with_committee_cache closures) before the signature is checked; rare.

**Impact.** Forged messages cannot trigger epoch transitions on cache hits; miss path remains.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1031-1060`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1031-L1060) proposer from proposer cache keyed by shuffling decision root, signature verified before parent state advance
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1645`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1645) map_attestation_committees uses shuffling cache; signatures checked after, no epoch transition

**Sources.** [prysm#17656](https://github.com/OffchainLabs/prysm/pull/17656)

</details>


<a id="gossip_validation-125"></a>
<details>
<summary><b>gossip_validation-125</b> Skip repeated signature verification — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Ensure aggregate/attestation signatures are verified once: remove duplicated verification calls and honor an already-verified flag.

**Impact.** Signatures are verified once; the flag is honored.

**Best measured result.** None (pr:prysm#5676)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification/batch.rs:195`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification/batch.rs#L195) batch success sets CheckAttestationSignature::No
- [`beacon_node/beacon_chain/src/attestation_verification.rs:857`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L857) signature only checked when flag is Yes

**Sources.** [prysm#5676](https://github.com/OffchainLabs/prysm/pull/5676), [lodestar#2264](https://github.com/ChainSafe/lodestar/pull/2264)

</details>


<a id="gossip_validation-127"></a>
<details>
<summary><b>gossip_validation-127</b> Skip validating locally produced or self-published objects — <i>partial · medium · S · cpu, latency</i></summary>

**Idea.** Skip full gossip validation of objects the node produced or published itself (blocks, data columns, own messages echoed back, trusted local builder bids), keeping only required checks like equivocation.

**Gap in Lighthouse.** Locally built blocks (ProvenancedBlock::Local) still wait for full GossipVerifiedBlock::new before broadcast; Teku publishes them after only an equivocation check. Work is not duplicated (import reuses the result), so the gain is publish latency, not CPU. Gloas bids/envelopes from a trusted local builder are always validated; Lodestar adds an operator flag to skip bid validation.

**Impact.** Lower publish latency for own proposals (proposer sig verify + parent lookup moved off the critical path) and for Gloas bids from a trusted local builder; no CPU saving since import needs the checks anyway.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_column_verification.rs:395`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L395) new_for_block_publishing skips gossip checks for locally built columns
- accba72/protocols/gossipsub/src/behaviour.rs:701 published message ids enter duplicate_cache, so own messages echoed back are dropped at :1985 before any Lighthouse validation
- [`beacon_node/beacon_chain/src/block_verification.rs:1285`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1285) import reuses the gossip-verified proposer signature (include_all_signatures_except_proposal), so gossip-verifying an own block is not repeated at import
- [`beacon_node/http_api/src/publish_blocks.rs:246`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L246) own block still fully gossip-verified before broadcast
- [`beacon_node/http_api/src/beacon/execution_payload_bids.rs:117`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/execution_payload_bids.rs#L117) API-submitted bids always gossip-verified (no trusted local builder bypass)
- [`beacon_node/http_api/src/beacon/execution_payload_envelopes.rs:264`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/execution_payload_envelopes.rs#L264) envelopes gossip-verified before publish

**Second check.** Beyond the earlier review: confirmed gossipsub drops self-echoed messages via duplicate_cache (the Prysm#3403 idea), that block import reuses the gossip proposer-signature check, and that Gloas bid/envelope API paths have no trusted-local bypass.

**Sources.** [lighthouse#7973](https://github.com/sigp/lighthouse/pull/7973), [prysm#3403](https://github.com/OffchainLabs/prysm/pull/3403), [teku#8352](https://github.com/Consensys-Incorporated/teku/pull/8352), [lodestar#10429](https://github.com/ChainSafe/lodestar/pull/10429)

</details>


<a id="gossip_validation-128"></a>
<details>
<summary><b>gossip_validation-128</b> Ignore already known blocks and columns early — <i>implemented · medium · cpu</i></summary>

**Idea.** Before processing a gossip block or data column sidecar, check whether it is already in the store or block input and skip it.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:971`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L971) fork choice contains_block returns DuplicateFullyImported before parent/state load
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1647`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1647) verify_is_unknown_sidecar uses observed_column_sidecars before KZG/inclusion proof
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1162`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1162) DA checker cache check skips KZG for known cells

**Sources.** [prysm#4721](https://github.com/OffchainLabs/prysm/pull/4721), [lodestar#8382](https://github.com/ChainSafe/lodestar/pull/8382)

</details>


<a id="gossip_validation-136"></a>
<details>
<summary><b>gossip_validation-136</b> Avoid copying signature batches — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Do not copy the signature batch in the batch verifier when nothing mutates it, cutting allocations.

**Gap in Lighthouse.** Small residual: attestation_verification.rs:679 clones selection_proof for the slashable-error path, and a signature_sets Vec of Cow is allocated per batch.

**Impact.** Batch verifier does not copy signatures; the remaining allocations are minor.

**Best measured result.** None (pr:prysm#16398)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification/batch.rs:109`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification/batch.rs#L109) signature sets built from borrowed data
- [`crypto/bls/src/generic_signature_set.rs:19`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/generic_signature_set.rs#L19) Cow&lt;'a&gt; aggregate signature, borrowed
- [`crypto/bls/src/impls/blst.rs:39`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L39) verify_signature_sets collects only refs

**Sources.** [prysm#16398](https://github.com/OffchainLabs/prysm/pull/16398)

</details>


<a id="gossip_validation-140"></a>
<details>
<summary><b>gossip_validation-140</b> Shorter batch signature verification deadline — <i>implemented · low · S · latency</i></summary>

**Idea.** Cut the max wait of the gossip attestation batch verifier so batches start sooner.

**Impact.** Lighthouse has no batch wait deadline: it batches opportunistically from whatever is queued, so there is no 50ms wait to cut.

**Best measured result.** None (pr:prysm#15882)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:962`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L962) and :1018 batch is drained from the queue whenever work is available, up to 64 (lib.rs:110)

**Sources.** [prysm#15882](https://github.com/OffchainLabs/prysm/pull/15882)

</details>


<a id="gossip_validation-142"></a>
<details>
<summary><b>gossip_validation-142</b> Skip aggregate and contribution work without validators — <i>not · medium · S · cpu</i></summary>

**Idea.** Skip signature-set construction and processing of aggregates and sync contributions when no local validator needs them.

**Gap in Lighthouse.** No validator-count gating anywhere in aggregate/contribution handling. Signature checks on aggregates cannot be skipped safely because Lighthouse feeds them into fork choice and forwards them. The part that could be gated is op-pool insertion (add_to_block_inclusion_pool, add_contribution_to_block_inclusion_pool), and for contributions the whole non-forwarding post-processing, on nodes with no local validators.

**Impact.** Small: saves op-pool insertion/aggregation bookkeeping on non-validating nodes; signature work (the large part) must stay for fork choice and propagation.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/topics.rs:56`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/topics.rs#L56) BeaconAggregateAndProof and SignedContributionAndProof are core topics regardless of attached validators
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:631`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L631) verified aggregates are applied to fork choice, so their signatures are needed even without validators
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:653`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L653) aggregates added to op pool unconditionally
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:2421`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L2421) sync contributions added to op pool unconditionally

**Second check.** Searched gossip_methods, subnet_service and topics for any validator-presence condition (import_all_attestations, subscribe_all_subnets only affect subnets); none. Added that aggregates feed fork choice, so only op-pool work is safely skippable.

**Sources.** [caplin#18521](https://github.com/erigontech/erigon/pull/18521), [caplin#18524](https://github.com/erigontech/erigon/pull/18524)

</details>


