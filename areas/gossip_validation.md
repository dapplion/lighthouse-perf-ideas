# gossip_validation

157 ideas: 27 not, 23 partial, 80 implemented, 27 n/a; 25 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [gossip_validation-001](#gossip_validation-001) | Bounded LIFO gossip job queue serving newest first | implemented | low | S | latency, cpu |
| [gossip_validation-002](#gossip_validation-002) **★** | Adaptive drop ratio when attestation queue overflows | not | medium | S | cpu, latency |
| [gossip_validation-003](#gossip_validation-003) | Yield to networking between gossip processing batches | implemented | low | S | latency |
| [gossip_validation-004](#gossip_validation-004) | Batch BLS verification of gossip attestations and aggregates | implemented | low | S | cpu, latency |
| [gossip_validation-005](#gossip_validation-005) **★** | Route other gossip types through shared batch verifier | not | medium | M | cpu, latency |
| [gossip_validation-006](#gossip_validation-006) | Verify one message's multiple signatures in one batch | implemented | low | S | cpu, latency |
| [gossip_validation-007](#gossip_validation-007) | Do not nest parallelism around a parallel BLS library | n/a | low |  | cpu |
| [gossip_validation-008](#gossip_validation-008) | Keep genesis validators root inside the batch verifier | n/a | low |  | cpu |
| [gossip_validation-009](#gossip_validation-009) | Do not hold locks while awaiting batch verification | n/a | low |  | latency |
| [gossip_validation-010](#gossip_validation-010) | Pass decoded gossip objects to processing, avoid re-decode | implemented | low | S | cpu, latency |
| [gossip_validation-011](#gossip_validation-011) | Deserialize attestation signatures once through pipeline | implemented | low | S | cpu |
| [gossip_validation-012](#gossip_validation-012) | Aggregate attestation pubkeys without per-validator allocations | implemented | medium | S | cpu, memory |
| [gossip_validation-013](#gossip_validation-013) | Hand cached compressed pubkey bytes to BLS workers | n/a | low |  | cpu |
| [gossip_validation-014](#gossip_validation-014) | Use decompressed pubkey cache for block proposer signature | implemented | low | S | cpu |
| [gossip_validation-015](#gossip_validation-015) | Minimal state advance for gossip validation | partial | low | S | cpu, latency, memory |
| [gossip_validation-016](#gossip_validation-016) | Fast epoch-context state transition in attestation validation | implemented | low | S | cpu |
| [gossip_validation-017](#gossip_validation-017) | Validate exits and BLS changes with light validator getters | implemented | low | S | cpu, memory |
| [gossip_validation-018](#gossip_validation-018) | Use in-memory head info instead of per-message state reads | implemented | medium | S | cpu, disk, latency |
| [gossip_validation-019](#gossip_validation-019) | Fork-choice lookups for block existence instead of DB | implemented | low | S | disk, cpu |
| [gossip_validation-020](#gossip_validation-020) | Cheap block-known lookup in pre-validation queue | n/a | low |  | cpu |
| [gossip_validation-021](#gossip_validation-021) | Fetch gossip validation states asynchronously | n/a | low |  | latency |
| [gossip_validation-022](#gossip_validation-022) | Run gossip validation off the network I/O thread | n/a | low |  | latency |
| [gossip_validation-023](#gossip_validation-023) | Cache parent execution-enabled flag in fork choice | implemented | low | S | cpu, disk |
| [gossip_validation-024](#gossip_validation-024) | Proposer index from shared per-epoch cache, no state advance | implemented | medium | S | cpu, latency |
| [gossip_validation-025](#gossip_validation-025) | Ignore attestations on shuffling cache miss | partial | low | S | cpu |
| [gossip_validation-026](#gossip_validation-026) **★** | Ignore blocks whose parent is older than justified | not | medium | S | cpu, memory |
| [gossip_validation-027](#gossip_validation-027) | Ignore proposer preferences with off-head dependent root | not | low | S | cpu |
| [gossip_validation-028](#gossip_validation-028) **★** | Bound state advancement for old or long-skip roots | partial | high | S | cpu |
| [gossip_validation-029](#gossip_validation-029) | Order gossip validation checks cheapest first | partial | low | M | cpu, disk, latency |
| [gossip_validation-030](#gossip_validation-030) **★** | Cheap sidecar checks before proposer BLS signature | partial | medium | S | cpu |
| [gossip_validation-031](#gossip_validation-031) | Cheap checks before loading pre-state | implemented | medium | S | cpu, disk |
| [gossip_validation-032](#gossip_validation-032) | Check pre-state exists before fetching it | implemented | low | S | cpu, disk |
| [gossip_validation-033](#gossip_validation-033) | Seen-check sidecars first before KZG and signature | implemented | medium | S | cpu, bandwidth |
| [gossip_validation-034](#gossip_validation-034) | Dedup builder bids before regen and BLS | implemented | low | S | cpu |
| [gossip_validation-035](#gossip_validation-035) | Seen-attestation cache checked first in attestation validation | implemented | low | S | cpu |
| [gossip_validation-036](#gossip_validation-036) | Compact key for seen unaggregated attestation cache | implemented | low | S | cpu, memory |
| [gossip_validation-037](#gossip_validation-037) | Dedup payload-timeliness votes by slot and validator | implemented | low | S | cpu |
| [gossip_validation-038](#gossip_validation-038) | Send PTC attestation once per duplicated validator | implemented | low | S | bandwidth, cpu |
| [gossip_validation-039](#gossip_validation-039) **★** | Dedup slasher ingress before BLS and queueing | not | medium | S | cpu, memory |
| [gossip_validation-040](#gossip_validation-040) | Persisted dedup for payload envelopes after restart | not | low | S | cpu |
| [gossip_validation-041](#gossip_validation-041) **★** | Ignore further blocks from same proposer and slot | partial | medium | S | cpu |
| [gossip_validation-042](#gossip_validation-042) **★** | Atomic seen check-and-set for concurrent duplicates | partial | medium | M | cpu |
| [gossip_validation-043](#gossip_validation-043) | Dedup gossip messages by message id | implemented | low | S | cpu, bandwidth |
| [gossip_validation-044](#gossip_validation-044) | Ignore aggregates whose bits are subset of seen ones | implemented | medium | S | bandwidth, cpu |
| [gossip_validation-045](#gossip_validation-045) | Seen-aggregate root cache checked before any validation work | implemented | medium | S | bandwidth, cpu, latency |
| [gossip_validation-046](#gossip_validation-046) **★** | Cache validation work per distinct AttestationData | not | medium | M | cpu |
| [gossip_validation-047](#gossip_validation-047) **★** | Verify proposer header signature once across sidecars | partial | medium | S | cpu, latency |
| [gossip_validation-048](#gossip_validation-048) | Verify early attestation signatures and cache result | n/a | low | S | cpu |
| [gossip_validation-049](#gossip_validation-049) | Compute gossip block root once and reuse it | implemented | low | S | cpu, latency |
| [gossip_validation-050](#gossip_validation-050) **★** | Cache invalid block roots to reject descendants | partial | medium | M | cpu, latency |
| [gossip_validation-051](#gossip_validation-051) | Memoize fork digest computation | implemented | low | S | cpu |
| [gossip_validation-052](#gossip_validation-052) | Check snappy declared length before decompressing | implemented | medium | S | bandwidth, cpu, memory |
| [gossip_validation-053](#gossip_validation-053) **★** | Bound column sidecar size by max blobs early | partial | medium | S | cpu, memory |
| [gossip_validation-054](#gossip_validation-054) | Bound pending, deferred and future-slot gossip queues | implemented | low | S | cpu, memory |
| [gossip_validation-055](#gossip_validation-055) **★** | Reject future-slot messages before queueing or hashing | partial | medium | S | memory, cpu |
| [gossip_validation-056](#gossip_validation-056) **★** | Cap in-flight gossip validations per large topic | partial | medium | M | cpu, memory |
| [gossip_validation-057](#gossip_validation-057) **★** | Keep compressed payload in gossip validation queue | not | medium | L | memory |
| [gossip_validation-058](#gossip_validation-058) | Drop stale messages by slot read from bytes | not | low | S | cpu, memory |
| [gossip_validation-059](#gossip_validation-059) | Reject pre-finalized gossip blocks and attestations | implemented | low | S | cpu, bandwidth |
| [gossip_validation-060](#gossip_validation-060) | Heavier penalty for peers gossiping stale blocks | implemented | low | S | cpu, bandwidth |
| [gossip_validation-061](#gossip_validation-061) | Skip gossip validation while syncing or far behind | implemented | low | S | cpu, sync |
| [gossip_validation-062](#gossip_validation-062) | Drop pending messages from fatally penalized peers | not | low | S | cpu |
| [gossip_validation-063](#gossip_validation-063) | Harden aggregate validation with bounded verifier queue | implemented | low | S | cpu, bandwidth |
| [gossip_validation-064](#gossip_validation-064) | Cheap results instead of exceptions on reject paths | n/a | low | S | cpu |
| [gossip_validation-065](#gossip_validation-065) | Avoid cloning conversions between sidecar wrapper types | n/a | low | S | memory, cpu |
| [gossip_validation-066](#gossip_validation-066) **★** | Batch KZG verification of gossip column sidecars | not | medium | M | cpu |
| [gossip_validation-067](#gossip_validation-067) | Bounded wait for unknown block attestation validation | implemented | low | S | latency, bandwidth |
| [gossip_validation-068](#gossip_validation-068) | LRU-bound the seen sync contribution set | implemented | low | S | memory |
| [gossip_validation-069](#gossip_validation-069) | Remove seen caches made redundant by other dedup | not | low | S | bandwidth, cpu, memory |
| [gossip_validation-070](#gossip_validation-070) | Bypass queue gating for gossip blocks | implemented | low | S | latency |
| [gossip_validation-071](#gossip_validation-071) | Gossip compact single-validator attestations | implemented | high | S | bandwidth, cpu |
| [gossip_validation-072](#gossip_validation-072) | Construct gossip messages instead of reflection clone | n/a | low | S | cpu |
| [gossip_validation-073](#gossip_validation-073) | Process cheap gossip attestations first by cost | not | low | M | cpu, latency |
| [gossip_validation-074](#gossip_validation-074) | Hold slightly-early gossip objects until their slot | partial | low | M | cpu, latency |
| [gossip_validation-075](#gossip_validation-075) | Forward attestations to slasher after validation | implemented | low | S | latency |
| [gossip_validation-076](#gossip_validation-076) | Remove redundant finalized-descendant viability check | not | low | S | cpu |
| [gossip_validation-077](#gossip_validation-077) | Ignore BLS changes before Capella without validation | implemented | low | S | cpu, bandwidth |
| [gossip_validation-078](#gossip_validation-078) | Skip blob reconstruction for pre-Deneb blocks | implemented | low | S | cpu |
| [gossip_validation-079](#gossip_validation-079) **★** | Verify block signature before pending-queue insertion | partial | medium | M | bandwidth, cpu, memory |
| [gossip_validation-080](#gossip_validation-080) | Evict dedup entries when delayed items are dropped | n/a | low | S | memory |
| [gossip_validation-081](#gossip_validation-081) | Expire held unknown-root gossip messages | implemented | low | S | memory |
| [gossip_validation-082](#gossip_validation-082) | Extract block roots only from early messages | n/a | low | S | memory, cpu |
| [gossip_validation-083](#gossip_validation-083) | Faster subnet computation in gossip validation | n/a | low | S | cpu |
| [gossip_validation-084](#gossip_validation-084) | Index pending bids by preference slot and root | not | low | M | cpu |
| [gossip_validation-085](#gossip_validation-085) | Per-(validator, epoch) seen caches checked before validation | implemented | low | S | bandwidth, cpu, disk, memory |
| [gossip_validation-086](#gossip_validation-086) | Seen caches for exits and slashings | implemented | low | S | bandwidth, cpu |
| [gossip_validation-087](#gossip_validation-087) | Size seen caches for the validator set | implemented | low | S | bandwidth, cpu |
| [gossip_validation-088](#gossip_validation-088) | Shrink seen-attester cache lookback to two epochs | partial | low | S | memory |
| [gossip_validation-089](#gossip_validation-089) | Mark seen only after successful validation | implemented | low | S | memory |
| [gossip_validation-090](#gossip_validation-090) | Ignore votes for unseen payload without network fetch | not | low | S | bandwidth, latency |
| [gossip_validation-091](#gossip_validation-091) | Replace DB reads in gossip checks with in-memory state | implemented | low | S | cpu, disk, latency |
| [gossip_validation-092](#gossip_validation-092) **★** | Group queued attestations by data for batch verify | not | medium | M | cpu |
| [gossip_validation-093](#gossip_validation-093) | Shrink lock critical sections in seen caches | implemented | low | S | cpu, latency |
| [gossip_validation-094](#gossip_validation-094) | Prune serialized-bytes cache by key | n/a | low | S | memory |
| [gossip_validation-095](#gossip_validation-095) | Larger attestation queues and batch drain per idle | implemented | low | S | cpu, latency |
| [gossip_validation-096](#gossip_validation-096) | Shorter tuned idle timeout in gossip processor loop | n/a | low | S | cpu, latency |
| [gossip_validation-097](#gossip_validation-097) | Bounded prioritized gossip work queue, blocks first | implemented | low | S | bandwidth, cpu, latency |
| [gossip_validation-098](#gossip_validation-098) | Raise priority of rare gossip topics | not | low | S | latency |
| [gossip_validation-099](#gossip_validation-099) | Raise sync committee gossip queue concurrency | n/a | low | S | cpu, latency |
| [gossip_validation-100](#gossip_validation-100) | Do not gate gossip work during block processing | implemented | low | S | latency |
| [gossip_validation-101](#gossip_validation-101) | Attestation admission budget scaled to traffic | partial | low | M | cpu, memory |
| [gossip_validation-102](#gossip_validation-102) | Maintain queue counters instead of scanning | implemented | low | S | cpu |
| [gossip_validation-103](#gossip_validation-103) | Cheap raw-byte field reads without views | n/a | low | S | cpu |
| [gossip_validation-104](#gossip_validation-104) **★** | Peek raw SSZ bytes to skip deserialization | partial | medium | M | cpu, memory |
| [gossip_validation-105](#gossip_validation-105) | Minimum bid increment before forwarding | not | low | S | bandwidth, cpu |
| [gossip_validation-106](#gossip_validation-106) | Once-cell per shuffling key for concurrent computes | implemented | low | S | cpu, latency |
| [gossip_validation-107](#gossip_validation-107) | Singleflight state replays for sidecar verification | implemented | medium | S | cpu, memory |
| [gossip_validation-108](#gossip_validation-108) | Reduce duplicate work in aggregate validation | implemented | low | S | cpu, latency |
| [gossip_validation-109](#gossip_validation-109) | Pass gossip attestations by reference | partial | low | S | cpu, memory |
| [gossip_validation-110](#gossip_validation-110) | Penalize peers sending too-old messages | not | low | S | bandwidth, cpu |
| [gossip_validation-111](#gossip_validation-111) | Plain map for bounded seen key space | implemented | low | S | cpu, memory |
| [gossip_validation-112](#gossip_validation-112) | Only BLS-verify queued envelopes for known proposers | implemented | low | S | cpu |
| [gossip_validation-113](#gossip_validation-113) **★** | Precompute per-shuffling committee aggregate pubkeys | not | medium | M | cpu |
| [gossip_validation-114](#gossip_validation-114) | Use proposer lookahead to skip epoch transitions | implemented | medium | S | cpu, latency, memory |
| [gossip_validation-115](#gossip_validation-115) **★** | Read-only head or parent state, no copy | partial | medium | S | cpu, latency, memory |
| [gossip_validation-116](#gossip_validation-116) | Use cached checkpoint or advanced states for validation | implemented | medium | S | cpu, latency, memory |
| [gossip_validation-117](#gossip_validation-117) | Direct state lookup by block root | implemented | low | S | cpu, latency |
| [gossip_validation-118](#gossip_validation-118) | Synchronous cached state read, conditional pool add | partial | low | S | cpu, latency |
| [gossip_validation-119](#gossip_validation-119) | Small immutable validation view cache for bids | implemented | low | S | cpu, memory |
| [gossip_validation-120](#gossip_validation-120) | Ignore bids that force epoch-transition regen | n/a | low |  | cpu |
| [gossip_validation-121](#gossip_validation-121) | Signature check before state advance | partial | low | S | cpu, latency |
| [gossip_validation-122](#gossip_validation-122) **★** | Builder pubkey in fork choice for envelope sig | not | medium | M | cpu, disk, latency |
| [gossip_validation-123](#gossip_validation-123) | Drop redundant finalized-descendant check | not | low | S | cpu |
| [gossip_validation-124](#gossip_validation-124) | Drop redundant slot-window check | n/a | low | S | cpu |
| [gossip_validation-125](#gossip_validation-125) | Skip repeated signature verification | implemented | low | S | cpu, latency |
| [gossip_validation-126](#gossip_validation-126) | Single fork choice lock per attestation | not | low | S | cpu, latency |
| [gossip_validation-127](#gossip_validation-127) **★** | Skip validating locally produced or self-published objects | partial | medium | S | cpu, latency |
| [gossip_validation-128](#gossip_validation-128) | Ignore already known blocks and columns early | implemented | medium | S | cpu |
| [gossip_validation-129](#gossip_validation-129) | Do not track already imported blocks in pending pool | n/a | low | S | memory |
| [gossip_validation-130](#gossip_validation-130) | Recheck peer score after async await | not | low | M | cpu |
| [gossip_validation-131](#gossip_validation-131) | Recheck timeliness before forwarding | implemented | medium | S | bandwidth, cpu |
| [gossip_validation-132](#gossip_validation-132) | Regossip envelopes after reprocessing | implemented | low | S | latency |
| [gossip_validation-133](#gossip_validation-133) | Reject null-slot gossip before queueing | n/a | low | S | cpu, memory |
| [gossip_validation-134](#gossip_validation-134) | Queue gossip awaiting unknown dependency | implemented | low | M | latency |
| [gossip_validation-135](#gossip_validation-135) | Add attestations directly to pool after verify | implemented | low | S | cpu, latency, memory |
| [gossip_validation-136](#gossip_validation-136) | Avoid copying signature batches | implemented | low | S | cpu, memory |
| [gossip_validation-137](#gossip_validation-137) | Backoff retries of queued blocks | n/a | low | S | cpu |
| [gossip_validation-138](#gossip_validation-138) | Serialize decoding of large gossip messages | n/a | low | S | cpu, memory |
| [gossip_validation-139](#gossip_validation-139) | Shallow validation before propagation | implemented | high | S | bandwidth, cpu, latency |
| [gossip_validation-140](#gossip_validation-140) | Shorter batch signature verification deadline | implemented | low | S | latency |
| [gossip_validation-141](#gossip_validation-141) | Do not feed aggregate contents to fork choice | n/a | low | S | cpu |
| [gossip_validation-142](#gossip_validation-142) **★** | Skip aggregate and contribution work without validators | not | medium | S | cpu |
| [gossip_validation-143](#gossip_validation-143) | Committee index via accessor, no version checks | implemented | low | S | cpu |
| [gossip_validation-144](#gossip_validation-144) | Single decode-and-validate handler per topic | n/a | low | S | cpu, latency |
| [gossip_validation-145](#gossip_validation-145) | Route gossip envelopes straight to fork choice | n/a | low |  | latency |
| [gossip_validation-146](#gossip_validation-146) | Validate sidecars before caching | implemented | low | S | cpu |
| [gossip_validation-147](#gossip_validation-147) | Derive prev_randao from block data, no state replay | implemented | low | S | cpu, latency, disk |
| [gossip_validation-148](#gossip_validation-148) | Publish each light client update only once | implemented | low | S | bandwidth, cpu |
| [gossip_validation-149](#gossip_validation-149) | No event-bus emission on gossip block hot path | implemented | low | S | cpu, latency |
| [gossip_validation-150](#gossip_validation-150) **★** | Inclusion proof replaces per-sidecar proposer signature | partial | medium | S | cpu, bandwidth |
| [gossip_validation-151](#gossip_validation-151) | Iterate sync subcommittee without copying pubkeys | not | low | S | memory, cpu |
| [gossip_validation-152](#gossip_validation-152) | Precompute subnet stability offset once | implemented | low | S | cpu |
| [gossip_validation-153](#gossip_validation-153) | Verify single attestation signature before committee lookup | implemented | medium | S | cpu, latency |
| [gossip_validation-154](#gossip_validation-154) | Single regex to map gossip topic to subnet | implemented | low | S | cpu |
| [gossip_validation-155](#gossip_validation-155) | Skip hash tree root computed only for logging | implemented | low | S | cpu |
| [gossip_validation-156](#gossip_validation-156) | Validate light client gossip against local update, no storage | implemented | low | S | cpu, memory, disk |
| [gossip_validation-157](#gossip_validation-157) | Reject subscriptions to unknown gossip topics | implemented | low | S | bandwidth, memory |

★ actionable. Click an id for the full record.

## Ideas

<a id="gossip_validation-001"></a>
<details>
<summary><b>gossip_validation-001</b> Bounded LIFO gossip job queue serving newest first — <i>implemented · low · S · latency, cpu</i></summary>

**Idea.** Process gossip validation jobs from a bounded queue that pops LIFO (newest first) and drops items beyond the limit, so under load fresh messages are validated before stale ones.

**Impact.** None on live forks. The only time-sensitive gossip queue that is still FIFO is the not-yet-live Gloas payload attestation queue.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_queue.rs:237-264`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_queue.rs#L237-L264) LifoQueue push_front, pop_front, drops the oldest item when full
- [`beacon_node/beacon_processor/src/scheduler/work_queue.rs:483-497`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_queue.rs#L483-L497) attestation, aggregate, unknown-block and sync message/contribution queues are LIFO
- [`beacon_node/beacon_processor/src/scheduler/work_queue.rs:559`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_queue.rs#L559) gossip_payload_attestation_queue (Gloas PTC) is a FifoQueue

**Skeptic check.** Confirmed that bounded LIFO with drop-oldest is used for every live vote-type gossip queue. The Gloas PTC payload-attestation queue is FIFO, which is worth revisiting when Gloas ships, but it is not a gap on live forks.

**Verdict history.** implemented (checked) → implemented (skeptic)

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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [lodestar#5355](https://github.com/ChainSafe/lodestar/pull/5355)

</details>


<a id="gossip_validation-003"></a>
<details>
<summary><b>gossip_validation-003</b> Yield to networking between gossip processing batches — <i>implemented · low · S · latency</i></summary>

**Idea.** Run queued gossip/block processing in small batches or time slices and hand control back to the network/event loop between them (time-based, not per job), so CPU-heavy work does not starve networking; allow concurrency above one so signature work can batch.

**Impact.** None: the source PRs fix starvation in single-threaded event loops (JS, Nim). Lighthouse gets the same effect from thread isolation and OS time-slicing.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:747-748`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L747-L748) workers are spawn_blocking tasks, off the tokio core threads that drive libp2p
- [`beacon_node/beacon_processor/src/lib.rs:130`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L130) max_workers = num_cpus
- [`beacon_node/beacon_processor/src/lib.rs:890`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L890) the manager spawns only while current_workers &lt; max_workers
- [`beacon_node/beacon_processor/src/lib.rs:1017-1054`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1017-L1054) attestation queue drained into batches for batch BLS
- [`beacon_node/beacon_processor/src/lib.rs:1787-1805`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1787-L1805) spawn_blocking / spawn_blocking_with_rayon

**Second check.** Checked the task_executor blocking and rayon pools, and the max_workers default. The idea's goal (networking is not starved, concurrency above one, signature batching) is met by an equivalent mechanism, so a time-slice yield has no job to do here.

**Skeptic check.** Verified that CPU-heavy beacon processor work runs on blocking/rayon pools with multi-worker concurrency and BLS batching. This is the equivalent mechanism for a multi-threaded runtime, so the earlier verdict holds.

**Verdict history.** partial (checked) → implemented (refuted) → implemented (skeptic)

**Sources.** [lodestar#2472](https://github.com/ChainSafe/lodestar/pull/2472), [nimbus@76f15302a](https://github.com/status-im/nimbus-eth2/commit/76f15302a71f), [nimbus#2227](https://github.com/status-im/nimbus-eth2/pull/2227)

</details>


<a id="gossip_validation-004"></a>
<details>
<summary><b>gossip_validation-004</b> Batch BLS verification of gossip attestations and aggregates — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Collect signature sets from many gossip attestations/aggregates over a short window and verify them with one randomized batch BLS call, falling back to individual verification on failure; this amortizes the final exponentiation. Verify the signature early via the batch verifier, before expensive shuffling lookups.

**Impact.** None significant. Batching is driven by backlog (2 or more queued), not a timed window, so it applies exactly under load, where the throughput gain matters.

**Best measured result.** batch check ~0.5ms/check vs ~1ms single; throughput 2x higher; worst latency ~40ms (pr:nimbus#2439)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:110-111`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L110-L111) batch sizes of 64 for attestations and aggregates
- [`beacon_node/beacon_processor/src/lib.rs:1017-1054`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1017-L1054) pops up to the batch size into GossipAttestationBatch when 2 or more are queued
- [`beacon_node/beacon_chain/src/attestation_verification/batch.rs:28-195`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification/batch.rs#L28-L195) batch_verify_aggregated/unaggregated_attestations use one verify_signature_sets and fall back to individual verification on failure
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:316`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L316),529 process_gossip_attestation_batch / process_gossip_aggregate_batch

**Skeptic check.** Confirmed randomized batch verification with individual fallback for both unaggregated attestations and aggregates on the gossip path. Committee lookups use the shuffling cache, so the 'verify before shuffling lookup' ordering gains little here.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#10111](https://github.com/OffchainLabs/prysm/pull/10111), [teku#4106](https://github.com/Consensys-Incorporated/teku/pull/4106), [prysm#10553](https://github.com/OffchainLabs/prysm/pull/10553), [nimbus#2439](https://github.com/status-im/nimbus-eth2/pull/2439), [prysm#11144](https://github.com/OffchainLabs/prysm/pull/11144), [nimbus#6917](https://github.com/status-im/nimbus-eth2/pull/6917), [teku#11562](https://github.com/Consensys-Incorporated/teku/pull/11562)

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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [caplin#12485](https://github.com/erigontech/erigon/pull/12485), [caplin#12541](https://github.com/erigontech/erigon/pull/12541), [teku#11538](https://github.com/Consensys-Incorporated/teku/pull/11538), [teku#4144](https://github.com/Consensys-Incorporated/teku/pull/4144)

</details>


<a id="gossip_validation-006"></a>
<details>
<summary><b>gossip_validation-006</b> Verify one message&#x27;s multiple signatures in one batch — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** For aggregate-and-proof (selection proof, aggregator signature, aggregate signature) and sync contributions, verify all signatures of the message in a single batched multi-pairing instead of three separate verifications.

**Impact.** None: both message types already verify all three signatures in one batched multi-pairing.

**Best measured result.** BenchmarkValidateAggregateAndProof 3931547 -&gt; 2812799 ns/op (40% better, ~1.2ms per aggregate, ~300ms per slot at 260 aggregates) (pr:prysm#7744)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:1440-1485`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1440-L1485) verify_signed_aggregate_signatures checks the selection proof, the aggregator signature and the aggregate signature in one verify_signature_sets
- [`beacon_node/beacon_chain/src/sync_committee_verification.rs:632-672`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/sync_committee_verification.rs#L632-L672) the three sync contribution sets go in one verify_signature_sets

**Skeptic check.** Opened both functions and confirmed that the three-set arrays go to one verify_signature_sets call. The batch path in batch.rs also merges sets across messages. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#12537](https://github.com/erigontech/erigon/pull/12537), [prysm#7744](https://github.com/OffchainLabs/prysm/pull/7744), [teku#3824](https://github.com/Consensys-Incorporated/teku/pull/3824)

</details>


<a id="gossip_validation-007"></a>
<details>
<summary><b>gossip_validation-007</b> Do not nest parallelism around a parallel BLS library — <i>n/a · low · cpu</i></summary>

**Idea.** Limit attestation batch verification to one active task when the BLS library already parallelizes internally, avoiding thread oversubscription.

**Impact.** Lighthouse's blst wrapper does not parallelize internally; parallelism comes from the beacon processor's worker pool, so there is no nested parallelism to remove.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification/batch.rs:109`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification/batch.rs#L109),195 verify_signature_sets, one batch per beacon-processor work item
- [`crypto/bls`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls) (blst) verify_multiple_aggregate_signatures runs single-threaded

**Sources.** [grandine@91a6f9a18](https://github.com/grandinetech/grandine/commit/91a6f9a181ac)

</details>


<a id="gossip_validation-008"></a>
<details>
<summary><b>gossip_validation-008</b> Keep genesis validators root inside the batch verifier — <i>n/a · low · cpu</i></summary>

**Idea.** Store immutable inputs such as genesis_validators_root in the gossip batch verifier rather than passing them per check.

**Impact.** Lighthouse has no stateful gossip batch verifier object; signature sets are built from the chain per call, so the immutable input handling is a micro detail with no gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification/batch.rs:17`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification/batch.rs#L17),109 free function verify_signature_sets over prebuilt SignatureSets

**Sources.** [nimbus#4640](https://github.com/status-im/nimbus-eth2/pull/4640)

</details>


<a id="gossip_validation-009"></a>
<details>
<summary><b>gossip_validation-009</b> Do not hold locks while awaiting batch verification — <i>n/a · low · latency</i></summary>

**Idea.** When sync committee messages wait on the shared batch verifier, release the service mutex and head-state read lock during the wait so a full verification queue cannot stall other messages and state readers.

**Impact.** Sync committee messages are verified in blocking beacon-processor workers with no shared async batch queue or held mutex across awaits.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/sync_committee_verification.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/sync_committee_verification.rs) verifies synchronously on a worker thread, no await on a shared queue

**Sources.** [caplin#25605](https://github.com/erigontech/erigon/pull/25605), [caplin#24039](https://github.com/erigontech/erigon/pull/24039)

</details>


<a id="gossip_validation-010"></a>
<details>
<summary><b>gossip_validation-010</b> Pass decoded gossip objects to processing, avoid re-decode — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Hand the SSZ-decoded block/attestation from gossip validation straight to the processing queue so it is not deserialized a second time; prioritize blocks and aggregates and drop attestations when queues are full.

**Impact.** Gossip SSZ decode happens once in the network layer; processing takes decoded types, with block/aggregate priority and drop-on-full attestation queues.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs) GossipVerifiedBlock carries the decoded Arc&lt;SignedBeaconBlock&gt; into import
- [`beacon_node/beacon_chain/src/attestation_verification.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs) VerifiedUnaggregatedAttestation/VerifiedAggregatedAttestation carry decoded attestations
- [`beacon_node/beacon_processor`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor) priority order (blocks, aggregates before unaggregated) with bounded LIFO attestation queues that drop

**Skeptic check.** All three parts of the Nimbus change (single decode, priority, drop) exist in Lighthouse; earlier evidence right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus@22998fdfd](https://github.com/status-im/nimbus-eth2/commit/22998fdfd42a), [nimbus#1541](https://github.com/status-im/nimbus-eth2/pull/1541)

</details>


<a id="gossip_validation-011"></a>
<details>
<summary><b>gossip_validation-011</b> Deserialize attestation signatures once through pipeline — <i>implemented · low · S · cpu</i></summary>

**Idea.** Parse gossip attestation/aggregate signatures once and pass the parsed signature through verification queues and the pool instead of re-parsing at each stage.

**Impact.** None left: the gossip SSZ decode decompresses the signature once into the blst point, and that typed value moves through the verification queues, the naive aggregation pool and the op pool without another parse.

**Best measured result.** Fixed attesting regressions v1.0.10-&gt;v1.0.12 caused by repeated deserialization (pr:nimbus#2472)

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/generic_signature.rs:145`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/generic_signature.rs#L145)
- [`crypto/bls/src/generic_signature.rs:191`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/generic_signature.rs#L191)
- [`crypto/bls/src/impls/blst.rs:195`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L195)

**Skeptic check.** Confirmed: the SSZ Decode for GenericSignature calls deserialize, which decompresses into point. Later uses only serialize the point (for hashing) and never re-parse it. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#2472](https://github.com/status-im/nimbus-eth2/pull/2472)

</details>


<a id="gossip_validation-012"></a>
<details>
<summary><b>gossip_validation-012</b> Aggregate attestation pubkeys without per-validator allocations — <i>implemented · medium · S · cpu, memory</i></summary>

**Idea.** Build aggregate pubkeys for attestation verification by reading the validator registry by index without allocating a deserialized pubkey object per validator.

**Impact.** None left: the signature sets borrow the decompressed keys from the cache by index (Cow::Borrowed), with no allocation or decompression per validator.

**Best measured result.** avoids memory allocation in gossip hot path (no numbers) (pr:prysm#14178)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:174`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L174)
- [`beacon_node/beacon_chain/src/attestation_verification/batch.rs:73`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification/batch.rs#L73)
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1357`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1357)
- [`beacon_node/beacon_chain/src/sync_committee_verification.rs:634`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/sync_committee_verification.rs#L634)

**Skeptic check.** Confirmed on the single, batch, aggregate and sync-committee gossip paths: each one uses pubkey_cache.get(i).map(Cow::Borrowed). The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#14178](https://github.com/OffchainLabs/prysm/pull/14178)

</details>


<a id="gossip_validation-013"></a>
<details>
<summary><b>gossip_validation-013</b> Hand cached compressed pubkey bytes to BLS workers — <i>n/a · low · cpu</i></summary>

**Idea.** On attestation validation that ships pubkey bytes to BLS workers, return the cached 48-byte compressed pubkey by index instead of decompressing and re-serializing a pubkey object.

**Impact.** n/a: BLS verification runs in-process on decompressed keys from the cache, so no pubkey bytes are shipped to workers.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:179`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L179) decompressed PublicKey cache; attestation_verification.rs:1350 borrows keys

**Sources.** [lodestar@4ca51cf97](https://github.com/ChainSafe/lodestar/commit/4ca51cf972ab)

</details>


<a id="gossip_validation-014"></a>
<details>
<summary><b>gossip_validation-014</b> Use decompressed pubkey cache for block proposer signature — <i>implemented · low · S · cpu</i></summary>

**Idea.** Verify gossip block proposer signatures using an in-memory index-to-decompressed-pubkey cache instead of loading and deserializing the validator pubkey from state.

**Impact.** Gossip block and sidecar proposer signature checks use decompressed cached keys, with no state read or decompression.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1056`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1056) gossip block proposer signature uses validator_pubkey_cache.get(proposer_index)
- [`beacon_node/beacon_chain/src/block_verification.rs:2264`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L2264) verify_header_signature (sidecars) uses the same cache
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:25`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L25) pubkeys: Vec&lt;PublicKey&gt; holds decompressed keys

**Skeptic check.** Verified the gossip block path at line 1056 (the earlier evidence cited only the header/sidecar path at 2263); both use the decompressed cache.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@9ce00ba91](https://github.com/ChainSafe/lodestar/commit/9ce00ba91a73)

</details>


<a id="gossip_validation-015"></a>
<details>
<summary><b>gossip_validation-015</b> Minimal state advance for gossip validation — <i>partial · low · S · cpu, latency, memory</i></summary>

**Idea.** Validate gossip attestations, aggregates, blocks, slashings and sync messages against the existing head state or a checkpoint state cache entry, advancing a copy only when the epoch actually differs and then only to the target epoch start, rather than running process_slots to the message slot per message.

**Gap in Lighthouse.** verify_proposer_slashing_for_gossip and verify_attester_slashing_for_gossip call wall_clock_state(). That is state_at_slot(current_slot, WithStateRoots): it clones the head state and runs per_slot_processing with state-root hashing up to the wall-clock slot, and runs epoch processing if it crosses an epoch boundary. This happens for every slashing message, before the duplicate check in observed_*_slashings. They could use the head state as the exit and BLS-change paths do, or a partial advance.

**Impact.** Small: slashings are rare, so the saving is one cloned process_slots (sometimes an epoch transition) per slashing message. The attestation, aggregate, block, column and sync paths already avoid the per-message advance.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:400`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L400)
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:454`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L454)
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:175`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L175)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2894`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2894)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2924`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2924)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1612`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1612)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1557`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1557)

**Skeptic check.** Confirmed: the shuffling cache uses the head state or a cached advanced state, plus partial_state_advance only to the start of the epoch before the shuffling epoch, and block/column proposers come from the proposer cache. The earlier evidence did not cover the slashings, which the idea names, and they still run a full process_slots per message.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [prysm#4532](https://github.com/OffchainLabs/prysm/pull/4532), [lodestar@341032f35](https://github.com/ChainSafe/lodestar/commit/341032f35358), [teku#5236](https://github.com/Consensys-Incorporated/teku/pull/5236), [prysm#4474](https://github.com/OffchainLabs/prysm/pull/4474), [prysm#7357](https://github.com/OffchainLabs/prysm/pull/7357), [teku#4142](https://github.com/Consensys-Incorporated/teku/pull/4142), [prysm#16830](https://github.com/OffchainLabs/prysm/pull/16830)

</details>


<a id="gossip_validation-016"></a>
<details>
<summary><b>gossip_validation-016</b> Fast epoch-context state transition in attestation validation — <i>implemented · low · S · cpu</i></summary>

**Idea.** When attestation validation must advance state, use the fast cached-epoch-context transition path rather than the slow naive transition.

**Impact.** Attestation validation does no state transition on a cache hit; on a miss it uses the cheap partial advance from the nearest advanced state.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:1617`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1617) map_attestation_committees -&gt; with_committee_cache
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:349-353`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L349-L353) read-locked cache hit returns committees with no state work
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:418-457`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L418-L457) on a miss uses the cached head state or get_advanced_hot_state, then partial_state_advance (skips state roots) only when needed

**Skeptic check.** Verified that with_cached_shuffling only advances on a miss, and uses partial_state_advance from an advanced hot state, which is the fast path. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@5944c6aef](https://github.com/ChainSafe/lodestar/commit/5944c6aef1cd)

</details>


<a id="gossip_validation-017"></a>
<details>
<summary><b>gossip_validation-017</b> Validate exits and BLS changes with light validator getters — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Validate voluntary exits and BLS-to-execution changes using only the few validator fields needed from a cheap head-validator accessor, instead of fetching or advancing a full beacon state per message.

**Impact.** None left for exits and BLS changes: both validate against an Arc clone of the head snapshot with no state copy or advance.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2841`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2841)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2964`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2964)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2987`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2987)

**Skeptic check.** Confirmed: exits read validator fields from head_snapshot.beacon_state and use the wall-clock epoch from slot_clock, and BLS changes use the head state explicitly to avoid an advance. Slashings do not do this (see gossip_validation-015), but this idea covers only exits and BLS changes.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#4612](https://github.com/OffchainLabs/prysm/pull/4612), [prysm#11694](https://github.com/OffchainLabs/prysm/pull/11694), [teku#6732](https://github.com/Consensys-Incorporated/teku/pull/6732)

</details>


<a id="gossip_validation-018"></a>
<details>
<summary><b>gossip_validation-018</b> Use in-memory head info instead of per-message state reads — <i>implemented · medium · S · cpu, disk, latency</i></summary>

**Idea.** Gossip validation should take head and finalized checkpoints and the head state from in-memory chain/fork-choice info (head state root, cached state) rather than reading the head state or block roots from the DB per message.

**Impact.** None left: the head, finalized and parent checks read the in-memory fork choice (proto array) and the cached head. The DB is read only on a cache miss (load_parent, get_advanced_hot_state, which goes through the state cache).

**Best measured result.** "major noticeable bottleneck from our profiling" (no numbers) (pr:prysm#2383)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:1244`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1244)
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:400`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L400)
- [`beacon_node/beacon_chain/src/block_verification.rs:961`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L961)
- [`beacon_node/beacon_chain/src/payload_bid_verification/gossip_verified_bid.rs:331`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_bid_verification/gossip_verified_bid.rs#L331)

**Skeptic check.** Confirmed: the attestation, block and bid gossip paths use fork_choice_read_lock and canonical_head.cached_head(). The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#2383](https://github.com/OffchainLabs/prysm/pull/2383), [prysm#3288](https://github.com/OffchainLabs/prysm/pull/3288), [lodestar@6103d7b71](https://github.com/ChainSafe/lodestar/commit/6103d7b7122a), [lodestar#3097](https://github.com/ChainSafe/lodestar/pull/3097)

</details>


<a id="gossip_validation-019"></a>
<details>
<summary><b>gossip_validation-019</b> Fork-choice lookups for block existence instead of DB — <i>implemented · low · S · disk, cpu</i></summary>

**Idea.** Check whether a referenced block exists, its slot, or whether it matches the head via the in-memory fork-choice proto-array rather than querying the block database or loading state.

**Impact.** Existence, slot and head-match checks in gossip validation use proto-array; DB block reads occur only in load_parent (block_verification.rs:2046), where the parent block and state are needed for the state transition.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:970-973`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L970-L973) fork_choice contains_block for duplicate check
- [`beacon_node/beacon_chain/src/block_verification.rs:988`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L988) verify_parent_block_and_envelope_are_known via fork choice
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1244-1256`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1244-L1256) verify_head_block_is_known via fork_choice get_block / early_attester_cache
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1636-1643`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1636-L1643) target root via fork choice
- [`beacon_node/beacon_chain/src/payload_attestation_verification/gossip_verified_payload_attestation.rs:82-97`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_attestation_verification/gossip_verified_payload_attestation.rs#L82-L97) block existence and slot via fork choice

**Skeptic check.** Verified that the block, attestation and PTC gossip paths do existence and slot checks in fork choice. Sync committee message validation does no block lookup. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#12430](https://github.com/OffchainLabs/prysm/pull/12430), [lodestar@a9eda6ef7](https://github.com/ChainSafe/lodestar/commit/a9eda6ef7397)

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


<a id="gossip_validation-021"></a>
<details>
<summary><b>gossip_validation-021</b> Fetch gossip validation states asynchronously — <i>n/a · low · latency</i></summary>

**Idea.** Load or regenerate states for gossip validation asynchronously so validation threads are not blocked waiting on state retrieval.

**Impact.** n/a: gossip validation already runs on blocking beacon-processor workers.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:1657`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1657) spawn_blocking workers

**Sources.** [teku#2379](https://github.com/Consensys-Incorporated/teku/pull/2379)

</details>


<a id="gossip_validation-022"></a>
<details>
<summary><b>gossip_validation-022</b> Run gossip validation off the network I/O thread — <i>n/a · low · latency</i></summary>

**Idea.** Execute gossip message validation on a dedicated executor rather than the network I/O thread so slow validation does not block network reads.

**Impact.** n/a: validation runs in beacon processor workers, separate from the libp2p swarm task.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:1657`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1657) spawn_blocking
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs): validation in processor work items

**Sources.** [teku#2583](https://github.com/Consensys-Incorporated/teku/pull/2583), [lighthouse#492](https://github.com/sigp/lighthouse/pull/492)

</details>


<a id="gossip_validation-023"></a>
<details>
<summary><b>gossip_validation-023</b> Cache parent execution-enabled flag in fork choice — <i>implemented · low · S · cpu, disk</i></summary>

**Idea.** Store per-block execution/merge status in fork choice or cached block info so gossip block validation checks the parent's execution payload status without loading the parent state or block.

**Impact.** The parent execution status comes from proto-array, so no parent state load is needed.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/execution_payload.rs:219-248`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/execution_payload.rs#L219-L248) validate_execution_payload_for_gossip matches parent ProtoBlock.execution_status
- [`beacon_node/beacon_chain/src/block_verification.rs:1114`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1114) call site with the fork-choice parent_block

**Skeptic check.** Verified that the code comments state this purpose and that it uses ProtoBlock execution_status. This is the Lighthouse PR #2627 mechanism itself.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#2627](https://github.com/sigp/lighthouse/pull/2627), [nimbus#3876](https://github.com/status-im/nimbus-eth2/pull/3876)

</details>


<a id="gossip_validation-024"></a>
<details>
<summary><b>gossip_validation-024</b> Proposer index from shared per-epoch cache, no state advance — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Get the expected proposer (and committees) for gossip blocks and blob sidecars from a shared per-epoch proposer-index cache keyed by decision root, pruning old entries, instead of advancing, rewinding or loading a state.

**Impact.** None left: there is one shared OnceCell LRU (16 entries, so it prunes) keyed by (epoch, decision root), and blocks, data columns and payload envelopes all use it. A state is loaded only on a miss, and the work is not repeated across threads.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:26`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L26)
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:175`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L175)
- [`beacon_node/beacon_chain/src/block_verification.rs:1031`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1031)
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1746`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1746)
- [`beacon_node/beacon_chain/src/payload_envelope_verification/gossip_verified_envelope.rs:227`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/gossip_verified_envelope.rs#L227)

**Skeptic check.** Confirmed: the block, column and Gloas envelope gossip paths all use with_proposer_cache. Blob-sidecar gossip verification is no longer in this tree. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#1440](https://github.com/status-im/nimbus-eth2/pull/1440), [prysm#8107](https://github.com/OffchainLabs/prysm/pull/8107), [prysm#13423](https://github.com/OffchainLabs/prysm/pull/13423), [lodestar@8c15e1610](https://github.com/ChainSafe/lodestar/commit/8c15e16108b9)

</details>


<a id="gossip_validation-025"></a>
<details>
<summary><b>gossip_validation-025</b> Ignore attestations on shuffling cache miss — <i>partial · low · S · cpu</i></summary>

**Idea.** Ignore gossip attestations whose committee shuffling is not already cached instead of computing it, so attackers cannot force expensive shuffling computation.

**Gap in Lighthouse.** Lighthouse still computes a shuffling (state load and partial advance) on a miss, but at most 2 at a time and deduplicated per shuffling id; any further miss is ignored. A plain ignore-on-miss with no computation, as Nimbus proposed, is not there.

**Impact.** Small: the DoS cost is already bounded to 2 concurrent computations, deduplicated per shuffling id and limited to known targets in the gossip slot range. A pure ignore-on-miss would drop valid attestations on minority forks for little gain. The source Nimbus PR #4947 was closed without merging.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:36`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L36) MAX_CONCURRENT_PROMISES = 2
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:290-302`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L290-L302) create_promise returns MaxCommitteePromises once 2 misses are in flight
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:370-385`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L370-L385) concurrent misses for the same shuffling wait on one promise instead of recomputing
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:400-408`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L400-L408) rejects shufflings more than one epoch older than the target block
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:3227-3240`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L3227-L3240) MaxCommitteePromises maps to MessageAcceptance::Ignore
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:3217-3225`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L3217-L3225) FinalizedStateNotInHotDatabase maps to Ignore
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1628-1641`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1628-L1641) target root must be known to fork choice before any shuffling work

**Second check.** The earlier review missed the MAX_CONCURRENT_PROMISES cap and its Ignore mapping in gossip_methods.rs. Together these bound attacker-forced shuffling computation, which is the purpose of the idea. The Nimbus source PR was closed unmerged.

**Verdict history.** not (checked) → partial (refuted)

**Sources.** [nimbus#4947](https://github.com/status-im/nimbus-eth2/pull/4947)

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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [prysm#16579](https://github.com/OffchainLabs/prysm/pull/16579)

</details>


<a id="gossip_validation-027"></a>
<details>
<summary><b>gossip_validation-027</b> Ignore proposer preferences with off-head dependent root — <i>not · low · S · cpu</i></summary>

**Idea.** Ignore gossiped proposer preferences whose dependent root differs from the head's so peers cannot force off-head epoch transitions.

**Gap in Lighthouse.** Reject (IGNORE) preferences whose dependent_root != the head's dependent root for that epoch before the with_proposer_cache closure in GossipVerifiedProposerPreferences::new, so no off-head state load/advance occurs.

**Impact.** Only avoids occasional state loads on a proposer-cache miss for side forks; the attacker needs a dependent root with a real crossing child, so it is a narrow DoS guard with no mainnet steady-state gain. Also may drop legitimately useful preferences on competing forks.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/proposer_preferences_verification/gossip_verified_proposer_preferences.rs:103`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/proposer_preferences_verification/gossip_verified_proposer_preferences.rs#L103) dependent root only needs to be a known fork-choice block
- ...:126 non-head dependent root accepted if it has a child crossing the epoch boundary
- ...:160 get_advanced_hot_state on proposer-cache miss for that root

**Sources.** [prysm#17787](https://github.com/OffchainLabs/prysm/pull/17787)

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

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [teku#3975](https://github.com/Consensys-Incorporated/teku/pull/3975), [nimbus#1304](https://github.com/status-im/nimbus-eth2/pull/1304), [lodestar#4020](https://github.com/ChainSafe/lodestar/pull/4020)

</details>


<a id="gossip_validation-029"></a>
<details>
<summary><b>gossip_validation-029</b> Order gossip validation checks cheapest first — <i>partial · low · M · cpu, disk, latency</i></summary>

**Idea.** Order gossip validation rules so cheap structural REJECT checks run first, then cheap in-memory IGNOREs (slot window, bit lengths, committee bits, seen cache, invalid block, parent root, target epoch), then state loads, pool lookups, shuffling and signature checks, so invalid messages are dropped before costly work.

**Gap in Lighthouse.** On the SingleAttestation path, the in-memory REJECT checks run only after the BLS check: committee_index &lt; committees_per_slot (NoCommitteeForSlotAndIndex), attester in committee (AttesterNotInCommittee) and the subnet match (InvalidSubnetId). They are in VerifiedUnaggregatedAttestation::verify_late_checks (with_committee_cache), which runs after verify_attestation_signature in verify_slashable, and in batch.rs after the batch signature check. A message with a random attester_index or the wrong subnet therefore costs a BLS verify, or a failed batch and then single verifies, before a cheap shuffling-cache check would drop it. Separately, the aggregate path computes the ObservedAttestationKey tree_hash_root before verify_committee_index.

**Impact.** Saves BLS work only on invalid or misrouted single attestations, which is the DoS path. On honest traffic the effect is nil, because the shuffling check has to run anyway. Moving with_committee_cache earlier has a cost: on a shuffling miss, the state load would come before the signature filter.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:1032`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1032)
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1194`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1194)
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1202`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1202)
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1069`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1069)
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1096`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1096)
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1112`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1112)
- [`beacon_node/beacon_chain/src/attestation_verification.rs:556`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L556)

**Skeptic check.** Confirmed: the block, aggregate and sync orderings are cheap-first, as the earlier evidence said. The earlier evidence for the unaggregated path left out that the committee-membership and subnet checks run after the signature check.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [grandine@998a78869](https://github.com/grandinetech/grandine/commit/998a78869f84), [lodestar#9984](https://github.com/ChainSafe/lodestar/pull/9984), [nimbus#1379](https://github.com/status-im/nimbus-eth2/pull/1379), [nimbus#9189](https://github.com/status-im/nimbus-eth2/pull/9189), [nimbus#5610](https://github.com/status-im/nimbus-eth2/pull/5610), [teku#9595](https://github.com/Consensys-Incorporated/teku/pull/9595), [lodestar#2760](https://github.com/ChainSafe/lodestar/pull/2760), [prysm#7671](https://github.com/OffchainLabs/prysm/pull/7671), [lodestar@c56940770](https://github.com/ChainSafe/lodestar/commit/c56940770ccc), [prysm#14363](https://github.com/OffchainLabs/prysm/pull/14363), [nimbus#8860](https://github.com/status-im/nimbus-eth2/pull/8860), [lodestar@e9ba88bdc](https://github.com/ChainSafe/lodestar/commit/e9ba88bdcf83), [prysm#5274](https://github.com/OffchainLabs/prysm/pull/5274), [caplin#20578](https://github.com/erigontech/erigon/pull/20578), [caplin#9972](https://github.com/erigontech/erigon/pull/9972)

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

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [lodestar@27f4ad4ae](https://github.com/ChainSafe/lodestar/commit/27f4ad4ae8ae), [prysm#13346](https://github.com/OffchainLabs/prysm/pull/13346), [prysm#13347](https://github.com/OffchainLabs/prysm/pull/13347)

</details>


<a id="gossip_validation-031"></a>
<details>
<summary><b>gossip_validation-031</b> Cheap checks before loading pre-state — <i>implemented · medium · S · cpu, disk</i></summary>

**Idea.** Run state-independent checks (time window, invalid-block reference, already imported) and use cached genesis time before loading or regenerating the head/parent state, so rejected messages never touch state.

**Impact.** None left: on block gossip, the future-slot (slot_clock), finalized-slot, already-imported (fork choice), invalid-root and finalized-descendant checks all run before any state is loaded. On a proposer-cache miss, load_parent runs only after those checks.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:917`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L917)
- [`beacon_node/beacon_chain/src/block_verification.rs:961`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L961)
- [`beacon_node/beacon_chain/src/block_verification.rs:971`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L971)
- [`beacon_node/beacon_chain/src/block_verification.rs:976`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L976)
- [`beacon_node/beacon_chain/src/block_verification.rs:1031`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1031)
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1298`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1298)

**Skeptic check.** Confirmed the order in GossipVerifiedBlock::new_without_slasher_checks. The slot clock holds genesis time, so the state is never read for it. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@755ae5056](https://github.com/ChainSafe/lodestar/commit/755ae5056acf), [prysm#6755](https://github.com/OffchainLabs/prysm/pull/6755), [teku#3087](https://github.com/Consensys-Incorporated/teku/pull/3087), [lodestar@d7ce83529](https://github.com/ChainSafe/lodestar/commit/d7ce8352988e), [grandine#914](https://github.com/grandinetech/grandine/pull/914), [prysm#13490](https://github.com/OffchainLabs/prysm/pull/13490)

</details>


<a id="gossip_validation-032"></a>
<details>
<summary><b>gossip_validation-032</b> Check pre-state exists before fetching it — <i>implemented · low · S · cpu, disk</i></summary>

**Idea.** For attestation validation, check cheaply that the voted block's pre-state is available (else queue) before fetching or regenerating it, so unverifiable attestations skip state loads.

**Impact.** Attestations for unknown blocks are queued or dropped before any state load.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:1244-1256`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1244-L1256) verify_head_block_is_known (fork choice, early attester cache) returns UnknownHeadBlock for reprocessing
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1636-1643`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1636-L1643) UnknownTargetRoot check before with_committee_cache
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:330-333`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L330-L333) fork choice get_block before any state load

**Skeptic check.** Verified that the head and target are checked in fork choice before the committee or state path. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#6149](https://github.com/OffchainLabs/prysm/pull/6149), [prysm#6295](https://github.com/OffchainLabs/prysm/pull/6295)

</details>


<a id="gossip_validation-033"></a>
<details>
<summary><b>gossip_validation-033</b> Seen-check sidecars first before KZG and signature — <i>implemented · medium · S · cpu, bandwidth</i></summary>

**Idea.** For blob and data column sidecar gossip, do the already-seen (block header/slot, proposer, index) IGNORE check first, before KZG, signature and other checks, so duplicates are neither revalidated nor re-propagated.

**Impact.** Duplicate columns are dropped before inclusion proof, signature and KZG on both Fulu and Gloas paths.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_column_verification.rs:1139-1160`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1139-L1160) fulu path: verify_is_unknown_sidecar after only structural/slot checks
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1217-1240`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1217-L1240) gloas path: same ordering, before bid load and KZG
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1647-1665`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1647-L1665) observed_column_sidecars read-lock lookup returns PriorKnown
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:875`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L875) PriorKnown handled as ignore (no propagation)

**Skeptic check.** Verified both gossip column validators run the seen check before any expensive work; blob sidecar gossip no longer exists. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#7963](https://github.com/Consensys-Incorporated/teku/pull/7963), [prysm#17347](https://github.com/OffchainLabs/prysm/pull/17347), [nimbus#5563](https://github.com/status-im/nimbus-eth2/pull/5563), [lodestar#8542](https://github.com/ChainSafe/lodestar/pull/8542), [lighthouse#4164](https://github.com/sigp/lighthouse/pull/4164)

</details>


<a id="gossip_validation-034"></a>
<details>
<summary><b>gossip_validation-034</b> Dedup builder bids before regen and BLS — <i>implemented · low · S · cpu</i></summary>

**Idea.** Track seen execution payload bids per (slot/parent, builder) and check this first in bid gossip validation, before state regeneration or BLS verification.

**Impact.** Duplicate and lower-value bids are dropped before state access and BLS.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/payload_bid_verification/gossip_verified_bid.rs:301-315`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_bid_verification/gossip_verified_bid.rs#L301-L315) verify_bid_slot then seen_builder_bid_for_parent -&gt; BuilderAlreadySeen
- [`beacon_node/beacon_chain/src/payload_bid_verification/gossip_verified_bid.rs:319-328`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_bid_verification/gossip_verified_bid.rs#L319-L328) highest-bid value check also before state
- [`beacon_node/beacon_chain/src/payload_bid_verification/gossip_verified_bid.rs:351-380`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_bid_verification/gossip_verified_bid.rs#L351-L380) the state load (get_advanced_hot_state at the fork boundary) and signature checks come later

**Skeptic check.** Verified the order in GossipVerifiedPayloadBid::new. The dedup key is (slot, parent, builder), as the idea describes.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#9739](https://github.com/ChainSafe/lodestar/pull/9739), [prysm#16832](https://github.com/OffchainLabs/prysm/pull/16832), [caplin#22091](https://github.com/erigontech/erigon/pull/22091)

</details>


<a id="gossip_validation-035"></a>
<details>
<summary><b>gossip_validation-035</b> Seen-attestation cache checked first in attestation validation — <i>implemented · low · S · cpu</i></summary>

**Idea.** Check the recently-seen attestation cache at the very start of attestation validation and exit early on a hit.

**Impact.** Duplicates exit before committee computation and signature; preceding work is a few cheap fork-choice reads, plus gossipsub message-id dedup handles identical bytes earlier.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:902-977`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L902-L977) verify_early_checks: only epoch/slot-range/fork-choice lookups
- [`beacon_node/beacon_chain/src/attestation_verification.rs:993-1011`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L993-L1011) verify_middle_checks: observed_gossip_attesters lookup before committee lookup and BLS

**Skeptic check.** Confirmed the seen check is ahead of all costly work; it is not literally first but the remaining reordering win is negligible. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#4206](https://github.com/OffchainLabs/prysm/pull/4206)

</details>


<a id="gossip_validation-036"></a>
<details>
<summary><b>gossip_validation-036</b> Compact key for seen unaggregated attestation cache — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Key the seen-unaggregated-attestation cache by a compact fixed-size key (e.g. attester index plus data) rather than a hashed or concatenated buffer including the full aggregation bitlist.

**Impact.** Lookup is a bit index, no hashing or allocation; already more compact than the Prysm key.

**Best measured result.** 169 ns/280 B/4 allocs -&gt; 31 ns/24 B/1 alloc (pr:prysm#14590)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/observed_attesters.rs:86-130`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_attesters.rs#L86-L130) EpochBitfield: one bit per validator index per epoch
- [`beacon_node/beacon_chain/src/attestation_verification.rs:999-1003`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L999-L1003) lookup by (target epoch, attester_index)

**Skeptic check.** Verified the unaggregated seen cache is a per-epoch BitVec keyed by validator index, no bitlist or buffer involved. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#14590](https://github.com/OffchainLabs/prysm/pull/14590), [prysm#15034](https://github.com/OffchainLabs/prysm/pull/15034)

</details>


<a id="gossip_validation-037"></a>
<details>
<summary><b>gossip_validation-037</b> Dedup payload-timeliness votes by slot and validator — <i>implemented · low · S · cpu</i></summary>

**Idea.** Deduplicate payload-timeliness-committee gossip votes by (slot, validator_index) so repeated votes are not reprocessed or re-verified.

**Impact.** Duplicate PTC votes are dropped before BLS.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/payload_attestation_verification/gossip_verified_payload_attestation.rs:60-72`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_attestation_verification/gossip_verified_payload_attestation.rs#L60-L72) validator_has_been_observed(slot, validator_index) before the fork choice, shuffling and BLS work
- [`beacon_node/beacon_chain/src/payload_attestation_verification/gossip_verified_payload_attestation.rs:149-160`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_attestation_verification/gossip_verified_payload_attestation.rs#L149-L160) observe_validator under the write lock after verification
- [`beacon_node/beacon_chain/src/observed_attesters.rs:45`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_attesters.rs#L45) ObservedPayloadAttesters

**Skeptic check.** Verified that the dedup by (slot, validator_index) runs first and that the race recheck uses the write lock. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#8977](https://github.com/status-im/nimbus-eth2/pull/8977), [teku#10186](https://github.com/Consensys-Incorporated/teku/pull/10186)

</details>


<a id="gossip_validation-038"></a>
<details>
<summary><b>gossip_validation-038</b> Send PTC attestation once per duplicated validator — <i>implemented · low · S · bandwidth, cpu</i></summary>

**Idea.** When a validator appears several times in the payload timeliness committee, publish its payload attestation once.

**Impact.** The VC sends one message per validator, even when the validator holds several PTC seats.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:1797-1811`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1797-L1811) one PtcDuty per requested validator index
- [`consensus/types/src/state/beacon_state.rs:3685-3698`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3685-L3698) get_ptc_assignment returns the first slot only (one Option&lt;Slot&gt;)
- [`validator_client/validator_services/src/payload_attestation_service.rs:369-405`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/payload_attestation_service.rs#L369-L405) signs one message per duty

**Skeptic check.** Verified that duties are keyed by validator, not by committee position, so a duplicated seat gives no duplicate message. Separately, get_ptc_assignment recomputes get_ptc for each slot for each validator, which is a different cost.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#8777](https://github.com/status-im/nimbus-eth2/pull/8777)

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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [lighthouse#10107](https://github.com/sigp/lighthouse/pull/10107)

</details>


<a id="gossip_validation-040"></a>
<details>
<summary><b>gossip_validation-040</b> Persisted dedup for payload envelopes after restart — <i>not · low · S · cpu</i></summary>

**Idea.** When the in-memory observed cache is empty after restart, dedup gossip payload envelopes against fork choice's persisted payload-received flag before hashing and verifying the signature.

**Gap in Lighthouse.** In GossipVerifiedEnvelope::new, after fork_choice get_block, also return EnvelopeAlreadySeen for Gossip source when the proto node's payload_received flag is set, before verify_envelope_consistency and the signature check.

**Impact.** Saves one signing-root hash plus one BLS verify per duplicate envelope, only in the window after a restart; negligible on a steady node.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/payload_envelope_verification/gossip_verified_envelope.rs:174-185`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/gossip_verified_envelope.rs#L174-L185) dedup uses only in-memory ObservedPayloadEnvelopes
- ...:154 proto_block already in hand but payload_received not consulted
- ...:212-284 signature verified after; OPEN PR sigp/lighthouse#10414 not in tree

**Sources.** [lighthouse#10414](https://github.com/sigp/lighthouse/pull/10414)

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

**Verdict history.** partial (checked) → partial (refuted)

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

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [prysm#13109](https://github.com/OffchainLabs/prysm/pull/13109), [prysm#3567](https://github.com/OffchainLabs/prysm/pull/3567), [lighthouse#10182](https://github.com/sigp/lighthouse/pull/10182)

</details>


<a id="gossip_validation-043"></a>
<details>
<summary><b>gossip_validation-043</b> Dedup gossip messages by message id — <i>implemented · low · S · cpu, bandwidth</i></summary>

**Idea.** Keep a shared set of received gossip message ids and drop duplicates before validating or forwarding them.

**Impact.** Duplicates never reach Lighthouse validation or the forward path.

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/behaviour.rs:1985-1992 duplicate_cache.insert(msg_id) drops seen messages before they are delivered to the application or forwarded
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/behaviour.rs:1933 inbound_transform (snappy decompress) and 1950 message_id run before the dedup
- [`beacon_node/lighthouse_network/src/config.rs:527`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L527) message_id_fn(gossip_message_id)

**Skeptic check.** Verified that the dedup by message id comes before application validation and forwarding, which is what the idea describes. Each duplicate is still snappy-decompressed and hashed before the check, because the fork has no fast_message_id. That is a separate pre-decompression optimization.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#567](https://github.com/Consensys-Incorporated/teku/pull/567), [lodestar#660](https://github.com/ChainSafe/lodestar/pull/660), [teku#980](https://github.com/Consensys-Incorporated/teku/pull/980)

</details>


<a id="gossip_validation-044"></a>
<details>
<summary><b>gossip_validation-044</b> Ignore aggregates whose bits are subset of seen ones — <i>implemented · medium · S · bandwidth, cpu</i></summary>

**Idea.** For each attestation data (and committee index post-Electra) track the aggregation bits of seen gossip aggregates and sync contributions, and ignore a new one whose bits are a (non-strict) subset of an already seen one, before signature verification. This skips BLS work and re-propagation for redundant aggregates.

**Impact.** Redundant aggregates and contributions skip BLS and are not propagated.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:555-581`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L555-L581) ObservedAttestationKey(data, committee_index) root then is_known_subset before aggregator, state and signature checks
- [`beacon_node/beacon_chain/src/sync_committee_verification.rs:325-341`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/sync_committee_verification.rs#L325-L341) same subset check for sync contributions
- [`beacon_node/beacon_chain/src/observed_aggregates.rs:262-300`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_aggregates.rs#L262-L300) SlotHashSet non-strict subset/superset tracking

**Skeptic check.** Verified non-strict subset IGNORE for aggregates (with committee index post-Electra) and sync contributions before signature work. This is Lighthouse's own PR 3493; earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#7043](https://github.com/status-im/nimbus-eth2/pull/7043), [nimbus#3439](https://github.com/status-im/nimbus-eth2/pull/3439), [prysm#4451](https://github.com/OffchainLabs/prysm/pull/4451), [lighthouse#3493](https://github.com/sigp/lighthouse/pull/3493), [prysm#10674](https://github.com/OffchainLabs/prysm/pull/10674), [nimbus#4490](https://github.com/status-im/nimbus-eth2/pull/4490), [teku#5440](https://github.com/Consensys-Incorporated/teku/pull/5440), [teku#5439](https://github.com/Consensys-Incorporated/teku/pull/5439)

</details>


<a id="gossip_validation-045"></a>
<details>
<summary><b>gossip_validation-045</b> Seen-aggregate root cache checked before any validation work — <i>implemented · medium · S · bandwidth, cpu, latency</i></summary>

**Idea.** Keep a per-slot seen cache of aggregate hash tree roots and aggregator messages (fed from gossip, API, blocks and local production), hashing the aggregate once, and ignore an already seen gossip aggregate at the start of validation, before signature, state work, pool insertion or propagation.

**Impact.** Seen aggregates ignored at the start of validation; API-submitted (including local) aggregates go through the same verifier and are observed, and block-included ones are pre-seeded.

**Best measured result.** None (pr:lodestar#4019)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:555-581`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L555-L581) key root hashed once, subset check before head-block, committee, signature and pool work
- [`beacon_node/beacon_chain/src/attestation_verification.rs:589-600`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L589-L600) observed_aggregators check by (epoch, aggregator_index)
- [`beacon_node/beacon_chain/src/attestation_verification.rs:783-794`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L783-L794) observe_item after verification
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5039`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5039) block attestations fed into observed_attestations

**Skeptic check.** Verified the cache is fed from gossip, API (same verify path) and blocks, and is checked before any state or BLS work; the data-root+bits subset key is a stronger filter than an exact aggregate root. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

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

**Verdict history.** not (checked) → not (refuted)

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

**Verdict history.** not (checked) → partial (refuted)

**Sources.** [lodestar#8620](https://github.com/ChainSafe/lodestar/pull/8620), [nimbus#7949](https://github.com/status-im/nimbus-eth2/pull/7949), [teku#7749](https://github.com/Consensys-Incorporated/teku/pull/7749), [prysm#13245](https://github.com/OffchainLabs/prysm/pull/13245)

</details>


<a id="gossip_validation-048"></a>
<details>
<summary><b>gossip_validation-048</b> Verify early attestation signatures and cache result — <i>n/a · low · S · cpu</i></summary>

**Idea.** For attestations arriving before their propagation window, verify the BLS signature at gossip time and cache the result so fork choice does not re-verify later.

**Impact.** Lighthouse does not defer future-slot attestations to fork choice; the ones queued for an unknown block get verified once on replay, so there is no duplicated BLS to cache away.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:1297-1310`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1297-L1310) verify_propagation_slot_range returns FutureSlot beyond the clock-disparity tolerance
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:2629-2650`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L2629-L2650) FutureSlot is penalised and dropped, not queued
- work_reprocessing_queue.rs:132-142 only unknown-block/payload attestations are queued and then fully verified once

**Sources.** [teku#10961](https://github.com/Consensys-Incorporated/teku/pull/10961)

</details>


<a id="gossip_validation-049"></a>
<details>
<summary><b>gossip_validation-049</b> Compute gossip block root once and reuse it — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Compute the block root once during gossip validation and carry it in the verified block/blob for proposer signature checks, error/reject paths and later stages instead of re-hashing; check slot before reading the database.

**Impact.** One hash per gossip block; no canonical_root recomputation found in network gossip handlers.

**Best measured result.** None (pr:lighthouse#4277)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:886-892`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L886-L892) root computed once from the signed header
- [`beacon_node/beacon_chain/src/block_verification.rs:893-902`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L893-L902) root carried into slasher and BlockErrorWithRoot error paths
- [`beacon_node/beacon_chain/src/block_verification.rs:906-926`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L906-L926) new_without_slasher_checks takes block_root; future-slot check runs before DB/fork-choice lookups

**Skeptic check.** Verified the gossip block root is computed once and threaded through verification and error paths, and slot checks come first. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

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

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [prysm#6726](https://github.com/OffchainLabs/prysm/pull/6726), [teku#4963](https://github.com/Consensys-Incorporated/teku/pull/4963), [prysm#3685](https://github.com/OffchainLabs/prysm/pull/3685), [lighthouse#9730](https://github.com/sigp/lighthouse/pull/9730)

</details>


<a id="gossip_validation-051"></a>
<details>
<summary><b>gossip_validation-051</b> Memoize fork digest computation — <i>implemented · low · S · cpu</i></summary>

**Idea.** Memoize the fork digest keyed by fork version and genesis validators root instead of recomputing it for every gossip message.

**Impact.** None left: no per-message digest hashing on gossip encode or decode.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/fork/fork_context.rs:49-75`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/fork/fork_context.rs#L49-L75) ForkContext::new computes every digest once via spec.compute_fork_digest
- [`consensus/types/src/fork/fork_context.rs:93`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/fork/fork_context.rs#L93) current_fork_digest returns the cached value
- [`beacon_node/lighthouse_network/src/types/pubsub.rs:211`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L211) decode looks up fork by cached digest bytes (get_fork_from_context_bytes)
- [`beacon_node/lighthouse_network/src/types/pubsub.rs:717`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L717) outbound topics use cached current_fork_digest
- [`beacon_node/network/src/service.rs:501`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L501) compute_fork_digest only at fork scheduling

**Skeptic check.** Prysm cached ComputeForkDigest because it ran per gossip message; Lighthouse precomputes all digests in ForkContext and only does map lookups per message. The remaining compute_fork_digest calls (light-client API, fork scheduling) are off the hot path. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#11931](https://github.com/OffchainLabs/prysm/pull/11931)

</details>


<a id="gossip_validation-052"></a>
<details>
<summary><b>gossip_validation-052</b> Check snappy declared length before decompressing — <i>implemented · medium · S · bandwidth, cpu, memory</i></summary>

**Idea.** Read the uncompressed length from the snappy header and reject gossip messages outside the topic's valid size range (max gossip payload) before allocating, decompressing or SSZ decoding, including in the message-id function, so oversized messages cost no CPU or memory.

**Impact.** Oversized claims are rejected without allocation or decompression; bound is the global MAX_PAYLOAD_SIZE rather than per-topic, which matches the spec and the Teku/ethlambda fixes.

**Best measured result.** Prevents multi-GB allocation from a ~12MB message (pr:ethlambda#199)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/pubsub.rs:106-121`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L106-L121) inbound_transform checks compressed len and decompress_len() against max_uncompressed_len before decompress_vec
- [`beacon_node/lighthouse_network/src/service/mod.rs:345-351`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L345-L351) SnappyTransform installed as the gossipsub data transform, so message-id runs on bounded output
- [`beacon_node/lighthouse_network/src/types/pubsub.rs:535-548`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L535-L548) partial column messages size-capped before decode

**Skeptic check.** Verified the header-length check precedes allocation for every gossip message, and the message-id function only sees transformed data. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

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

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [lighthouse#8198](https://github.com/sigp/lighthouse/pull/8198), [lodestar#10076](https://github.com/ChainSafe/lodestar/pull/10076)

</details>


<a id="gossip_validation-054"></a>
<details>
<summary><b>gossip_validation-054</b> Bound pending, deferred and future-slot gossip queues — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Cap, prune and expire queues of gossip blocks, attestations and sidecars held for an unknown parent or future slot (entry count, per-entry cell count, retained slot window, drop oldest) and run cheap structure checks at admission, so peers cannot pin unbounded memory.

**Impact.** Every deferred/future/unknown-parent holding structure is count-bounded with delay expiry, and per-column cell count is bounded by the max-blobs check before queuing; byte accounting would only tighten worst case.

**Best measured result.** SSZ max 4096 cells with 8-root/128-column queue allows ~8 GiB heap held (pr:prysm#16831)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:78-90`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L78-L90) caps for blocks, envelopes, attestations, columns, LC updates
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:595`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L595),670,807,867 drop-on-full checks
- [`beacon_node/network/src/sync/block_lookups/mod.rs:77`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L77),408 MAX_LOOKUPS 200 for unknown-parent lookups
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:367-372`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L367-L372) pending components in a bounded LRU
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1150`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1150) commitments-length check at admission bounds per-column size

**Skeptic check.** Verified caps on reprocess queues, lookups and the DA cache; the per-entry cell concern from Prysm 16831 is covered by the commitments-length check. Earlier evidence was correct, gap text was minor.

**Verdict history.** implemented (checked) → implemented (skeptic)

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

**Verdict history.** partial (checked) → partial (refuted)

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

**Verdict history.** partial (checked) → partial (refuted)

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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [teku#11503](https://github.com/Consensys-Incorporated/teku/pull/11503)

</details>


<a id="gossip_validation-058"></a>
<details>
<summary><b>gossip_validation-058</b> Drop stale messages by slot read from bytes — <i>not · low · S · cpu, memory</i></summary>

**Idea.** Read the slot from the serialized gossip bytes and ignore messages older than a window (e.g. 32 slots) before deserializing or queueing them.

**Gap in Lighthouse.** Peek the slot from SSZ bytes at fixed offsets in inject_gs_event / PubsubMessage::decode and Ignore messages outside the propagation window before full decode and queueing.

**Impact.** Saves SSZ decode and queue slots for stale attestations/blocks; small since honest traffic is rarely stale.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/mod.rs:1390`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L1390) full PubsubMessage::decode before any slot check
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1298`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1298) verify_propagation_slot_range runs after decode and queueing
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:2654`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L2654) PastSlot handled post-decode

**Sources.** [lodestar#5394](https://github.com/ChainSafe/lodestar/pull/5394)

</details>


<a id="gossip_validation-059"></a>
<details>
<summary><b>gossip_validation-059</b> Reject pre-finalized gossip blocks and attestations — <i>implemented · low · S · cpu, bandwidth</i></summary>

**Idea.** Reject gossip blocks and attestations older than the finalized epoch before processing, so old forks cannot trigger recursive parent lookups.

**Impact.** Old-fork blocks and attestations are rejected before parent lookup; pruned pre-finalization roots trigger at most one bounded lookup.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:961`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L961) check_block_against_finalized_slot before parent load
- [`beacon_node/beacon_chain/src/block_verification.rs:1841`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1841) slot &lt;= finalized_slot -&gt; WouldRevertFinalizedSlot + pre_finalization_block_rejected
- [`beacon_node/beacon_chain/src/block_verification.rs:1878-1903`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1878-L1903) non-descendant with parent in DB -&gt; NotFinalizedDescendant (no lookup)
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1270`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1270) HeadBlockFinalized for known non-descendant heads
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1277`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1277) is_pre_finalization_block cache bounds lookups
- [`beacon_node/beacon_chain/src/pre_finalization_cache.rs:46-81`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pre_finalization_cache.rs#L46-L81) one lookup per pruned root, LOOKUP_LIMIT

**Skeptic check.** Verified gossip block path rejects pre-finalized slots and non-finalized-descendants before verify_parent_block_and_envelope_are_known, and attestations go through the finalized-descendant check plus the pre-finalization cache. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#3925](https://github.com/OffchainLabs/prysm/pull/3925), [prysm#6549](https://github.com/OffchainLabs/prysm/pull/6549), [caplin#10851](https://github.com/erigontech/erigon/pull/10851)

</details>


<a id="gossip_validation-060"></a>
<details>
<summary><b>gossip_validation-060</b> Heavier penalty for peers gossiping stale blocks — <i>implemented · low · S · cpu, bandwidth</i></summary>

**Idea.** Penalize peers that gossip pre-finalization blocks heavily enough that they are banned sooner, cutting repeated validation and bandwidth.

**Impact.** Peers that gossip finalized-slot blocks are scored down quickly; this only matters for buggy peers.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1730-1741`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1730-L1741) WouldRevertFinalizedSlot gossip block: Ignore plus LowToleranceError penalty
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:855-868`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L855-L868) data column NotFinalizedDescendant also gets LowToleranceError

**Skeptic check.** This is Lighthouse's own PR 6050, and it is present at the cited line. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#6050](https://github.com/sigp/lighthouse/pull/6050)

</details>


<a id="gossip_validation-061"></a>
<details>
<summary><b>gossip_validation-061</b> Skip gossip validation while syncing or far behind — <i>implemented · low · S · cpu, sync</i></summary>

**Idea.** While the node is syncing or more than a few slots behind head (head state too old), do not validate gossip operations such as attestations and aggregates (keep blocks and blobs), since the results cannot be used and the work is wasted.

**Impact.** Attestation/aggregate validation is skipped while range-syncing; when only a few slots behind, attestations to unknown heads are parked in the reprocess queue before BLS, so little work is wasted.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:1209-1225`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1209-L1225) incoming events with drop_during_sync dropped while sync_state.is_syncing()
- [`beacon_node/network/src/network_beacon_processor/mod.rs:117`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L117),162,290 attestations/aggregates set drop_during_sync: true
- [`beacon_node/beacon_processor/src/lib.rs:240-309`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L240-L309) blocks/blobs/columns use drop_during_sync: false
- [`common/eth2/src/lighthouse/sync_state.rs:82-92`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2/src/lighthouse/sync_state.rs#L82-L92) is_syncing covers SyncingFinalized/SyncingHead/SyncTransition
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:595-624`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L595-L624) unknown-head attestations parked without BLS

**Skeptic check.** Confirmed drop at dispatch for new events (items already queued before sync started are still processed, which is negligible). The 'few slots behind' case differs from teku/prysm but LH's unknown-head handling avoids the wasted BLS work, so the earlier verdict holds.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#11855](https://github.com/erigontech/erigon/pull/11855), [teku#9190](https://github.com/Consensys-Incorporated/teku/pull/9190), [prysm#3514](https://github.com/OffchainLabs/prysm/pull/3514)

</details>


<a id="gossip_validation-062"></a>
<details>
<summary><b>gossip_validation-062</b> Drop pending messages from fatally penalized peers — <i>not · low · S · cpu</i></summary>

**Idea.** After a fatal peer action, drop that peer's pending gossip messages until disconnect rather than processing them.

**Gap in Lighthouse.** Before processing a queued gossip Work item, check the peer is still connected and not banned (NetworkGlobals peers) and Ignore otherwise, in the gossip handlers in gossip_methods.rs.

**Impact.** Only avoids validating already-queued messages of a just-banned peer; rare edge case.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:229`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L229) gossip_penalize_peer only sends ReportPeer
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:263`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L263) ban handled in peer manager, no purge of queued work
- [`beacon_node/beacon_processor/src/lib.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs) queues carry no peer-state check

**Sources.** [lodestar#10239](https://github.com/ChainSafe/lodestar/pull/10239)

</details>


<a id="gossip_validation-063"></a>
<details>
<summary><b>gossip_validation-063</b> Harden aggregate validation with bounded verifier queue — <i>implemented · low · S · cpu, bandwidth</i></summary>

**Idea.** Bound the aggregate-and-proof batch verifier queue and reject cheap duplicates or invalid aggregates before signature work.

**Impact.** Cheap duplicate and empty-aggregate rejection already happens before BLS work, and the queue is bounded.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:571-582`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L571-L582) observed_attestations is_known_subset before signature work
- [`beacon_node/beacon_chain/src/attestation_verification.rs:586-599`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L586-L599) observed_aggregators per (target epoch, aggregator) check before signature work
- [`beacon_node/beacon_chain/src/attestation_verification.rs:647`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L647) EmptyAggregationBitfield rejected early
- [`beacon_node/beacon_processor/src/lib.rs:1302`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1302) bounded aggregate_queue with batch verification

**Skeptic check.** Caplin's fix added a seen-aggregator-per-epoch cache, a participants check and a batch threshold. Lighthouse has the same checks in IndexedAggregatedAttestation::verify_early_checks, ahead of batch signature verification. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#11998](https://github.com/erigontech/erigon/pull/11998)

</details>


<a id="gossip_validation-064"></a>
<details>
<summary><b>gossip_validation-064</b> Cheap results instead of exceptions on reject paths — <i>n/a · low · S · cpu</i></summary>

**Idea.** On gossip reject/ignore paths return result codes or plain objects instead of throwing stack-capturing errors and converting error metadata to JSON, since this cost is paid for every invalid or duplicate message.

**Impact.** Rust errors are plain enums without stack capture or JSON conversion, so the JS exception cost does not exist.

**Best measured result.** "Object ... 578 ops/s vs AttestationError 115 ops/s" (about 5x); "4% of the cpu time" (pr:lodestar#3448)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:2654`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L2654) errors are plain Result enum values

**Sources.** [lodestar#3448](https://github.com/ChainSafe/lodestar/pull/3448), [lodestar@5de5346d9](https://github.com/ChainSafe/lodestar/commit/5de5346d987d), [lodestar#3401](https://github.com/ChainSafe/lodestar/pull/3401), [nimbus@3b06e0f65](https://github.com/status-im/nimbus-eth2/commit/3b06e0f657ee)

</details>


<a id="gossip_validation-065"></a>
<details>
<summary><b>gossip_validation-065</b> Avoid cloning conversions between sidecar wrapper types — <i>n/a · low · S · memory, cpu</i></summary>

**Idea.** Use one sidecar validation path across forks so validation does not convert between Arc-wrapped and inner types, which clones.

**Impact.** The Arc-wrapper conversion clone is specific to Grandine's types; Lighthouse has no double wrapper.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/pubsub.rs:195`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L195) sidecars decoded per fork into owned types

**Sources.** [grandine#657](https://github.com/grandinetech/grandine/pull/657)

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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [nimbus#8314](https://github.com/status-im/nimbus-eth2/pull/8314)

</details>


<a id="gossip_validation-067"></a>
<details>
<summary><b>gossip_validation-067</b> Bounded wait for unknown block attestation validation — <i>implemented · low · S · latency, bandwidth</i></summary>

**Idea.** For attestations whose block is unknown, wait a bounded time on a per-root readiness signal and finish validation inline instead of returning Ignore, with global/per-peer/per-root limits.

**Impact.** Lighthouse already gets the effect Prysm wanted: the gossip message stays pending (manual validation) until the block arrives, and is then Accepted and propagated, not Ignored. Only Prysm's per-peer/per-root caps differ.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:2874-2942`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L2874-L2942) UnknownHeadBlock: no validation result yet; triggers a block lookup and queues the attestation for reprocessing
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:53`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L53) QUEUED_ATTESTATION_DELAY 12s bound
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:84`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L84),595 global cap of 16384 queued attestations
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:950`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L950) released per root on block import

**Skeptic check.** Verified that Lighthouse does not call propagate_validation_result on the reprocess path, so the later re-validation returns Accept to gossipsub. This is the outcome Prysm's PR adds. Ignore is used only when the reprocess allowance is used up.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#17236](https://github.com/OffchainLabs/prysm/pull/17236)

</details>


<a id="gossip_validation-068"></a>
<details>
<summary><b>gossip_validation-068</b> LRU-bound the seen sync contribution set — <i>implemented · low · S · memory</i></summary>

**Idea.** Bound seen sets (e.g. sync contributions) with an LRU or slot pruning instead of an ever-growing map.

**Impact.** None: the seen sets are bounded by slot count and by per-slot capacity.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/observed_aggregates.rs:19`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_aggregates.rs#L19) ObservedSyncContributions = ObservedAggregates
- [`beacon_node/beacon_chain/src/observed_aggregates.rs:296`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_aggregates.rs#L296) per-slot max_capacity ReachedMaxObservationsPerSlot
- [`beacon_node/beacon_chain/src/observed_aggregates.rs:429-436`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_aggregates.rs#L429-L436) prune by slot window
- [`beacon_node/beacon_chain/src/observed_aggregates.rs:438-450`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_aggregates.rs#L438-L450) get_set_index replaces the lowest-slot set once max_capacity slots exist

**Skeptic check.** The set count is bounded even without an explicit prune call, because get_set_index replaces the oldest set. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#25349](https://github.com/erigontech/erigon/pull/25349)

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
<summary><b>gossip_validation-070</b> Bypass queue gating for gossip blocks — <i>implemented · low · S · latency</i></summary>

**Idea.** Process gossip blocks immediately, bypassing the BLS-pool and regen availability gates other gossip objects wait on.

**Impact.** No BLS-pool or regen gate exists in Lighthouse; gossip blocks are the highest-priority gossip work and wait at most for one free worker.

**Best measured result.** delay could exceed 2s in worst case (pr:lodestar#5263)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:1238-1250`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1238-L1250) GossipBlock dispatched immediately via push_and_pop when can_spawn
- [`beacon_node/beacon_processor/src/lib.rs:929`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L929) gossip_block_queue popped before aggregate (:969) and attestation (:1025) queues

**Skeptic check.** Verified the dispatch arm and pop order. Lighthouse has no equivalent gating to bypass, so the effect lodestar sought (blocks not delayed behind attestation BLS) already holds.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#5263](https://github.com/ChainSafe/lodestar/pull/5263)

</details>


<a id="gossip_validation-071"></a>
<details>
<summary><b>gossip_validation-071</b> Gossip compact single-validator attestations — <i>implemented · high · S · bandwidth, cpu</i></summary>

**Idea.** Use a SingleAttestation format (committee index, attester index, data, signature) on gossip instead of a full aggregation-bits attestation, shrinking messages and skipping bitfield handling.

**Impact.** Already shipped (Lighthouse PR 6488).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/pubsub.rs:253-259`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L253-L259) attestation subnet topic decodes SingleAttestation
- [`beacon_node/network/src/network_beacon_processor/mod.rs:90`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L90) SingleAttestation gossip processing

**Skeptic check.** Subnet attestations are decoded as SingleAttestation, as the cited code shows. This is Lighthouse's own PR. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#6488](https://github.com/sigp/lighthouse/pull/6488)

</details>


<a id="gossip_validation-072"></a>
<details>
<summary><b>gossip_validation-072</b> Construct gossip messages instead of reflection clone — <i>n/a · low · S · cpu</i></summary>

**Idea.** Create a fresh empty message per gossip topic via a constructor rather than cloning a template via reflection.

**Impact.** Rust decodes into typed values; no reflection clone exists.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/pubsub.rs:253`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L253) messages decoded by SSZ into concrete enum variants, no template clone

**Sources.** [prysm#14201](https://github.com/OffchainLabs/prysm/pull/14201)

</details>


<a id="gossip_validation-073"></a>
<details>
<summary><b>gossip_validation-073</b> Process cheap gossip attestations first by cost — <i>not · low · M · cpu, latency</i></summary>

**Idea.** Estimate each queued attestation's processing cost (e.g. whether its target state is cached) and process cheap ones first, deferring expensive ones.

**Gap in Lighthouse.** Compute a per-attestation cost (is the target shuffling cached) when queuing in the BeaconProcessor and pop cheap ones first or defer uncached ones to a separate queue.

**Impact.** Only helps when shuffling cache misses occur (e.g. after reorgs or sync); on a healthy node nearly all attestations hit the cache, so gain is small and speculative.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:1017-1054`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1017-L1054) attestation_queue popped in queue order and batched, no cost estimate
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1076`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1076),1645 committee cache lookup via shuffling cache with state-load fallback

**Sources.** [prysm#7566](https://github.com/OffchainLabs/prysm/pull/7566)

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


<a id="gossip_validation-075"></a>
<details>
<summary><b>gossip_validation-075</b> Forward attestations to slasher after validation — <i>implemented · low · S · latency</i></summary>

**Idea.** Forward validated attestations to the slasher asynchronously after validation completes so slasher work is off the gossip path.

**Impact.** Slasher DB work is already off the gossip path. Only an enqueue and an IndexedAttestation clone remain, and only on slasher nodes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:835-840`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L835-L840) apply_to_slasher (aggregate) only calls accept_attestation after verification
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1170-1175`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1170-L1175) apply_to_slasher (unaggregated)
- [`slasher/src/slasher.rs:83-85`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/slasher.rs#L83-L85) accept_attestation only pushes to attestation_queue
- [`slasher/src/slasher.rs:93`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/slasher.rs#L93) process_queued runs in the separate slasher service

**Skeptic check.** Verified that the gossip path does only the enqueue, and the heavy batch processing runs in the slasher service. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#14330](https://github.com/OffchainLabs/prysm/pull/14330)

</details>


<a id="gossip_validation-076"></a>
<details>
<summary><b>gossip_validation-076</b> Remove redundant finalized-descendant viability check — <i>not · low · S · cpu</i></summary>

**Idea.** Drop attestation viability checks already guaranteed by fork choice containing only finalized descendants.

**Gap in Lighthouse.** Proto-array keeps non-viable branches until pruned, so the check is not strictly redundant; dropping it would require proving fork choice only holds finalized descendants (prune on finality). Could remove the call and rely on fork-choice pruning.

**Impact.** Saves one read-lock plus a short node walk per attestation; negligible, and the fast path usually returns at once.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:1270`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1270),1519 verify_attestation_is_finalized_checkpoint_or_descendant still called
- [`consensus/proto_array/src/proto_array.rs:2251`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L2251) is_finalized_checkpoint_or_descendant has checkpoint fast-path then ancestor walk

**Sources.** [nimbus#1433](https://github.com/status-im/nimbus-eth2/pull/1433)

</details>


<a id="gossip_validation-077"></a>
<details>
<summary><b>gossip_validation-077</b> Ignore BLS changes before Capella without validation — <i>implemented · low · S · cpu, bandwidth</i></summary>

**Idea.** Ignore bls_to_execution_change gossip received before Capella without BLS verification or relay.

**Impact.** Already done; not relevant on mainnet after Capella.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2986-2992`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2986-L2992) verify_bls_to_execution_change_for_gossip returns BlsToExecutionPriorToCapella before any signature work
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:2264-2270`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L2264-L2270) Ignore, no penalty, no relay

**Skeptic check.** The pre-Capella check runs before verification, and the result is Ignore with no penalty. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#6537](https://github.com/Consensys-Incorporated/teku/pull/6537)

</details>


<a id="gossip_validation-078"></a>
<details>
<summary><b>gossip_validation-078</b> Skip blob reconstruction for pre-Deneb blocks — <i>implemented · low · S · cpu</i></summary>

**Idea.** Return early from blob sidecar reconstruction when the block is pre-Deneb.

**Impact.** None left: the gossip-block EL blob fetch and the HTTP reconstruction both skip pre-Deneb blocks.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:64-76`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L64-L76) PartialHeaderOrBid::try_from_block returns None for blocks without blob commitments (pre-Deneb)
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:144-147`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L144-L147) early return when no versioned hashes
- [`beacon_node/http_api/src/block_id.rs:358-363`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L358-L363) and 409-413 pre-Deneb rejected before reconstruction

**Skeptic check.** The Prysm change is on the gossip block subscriber's EL blob reconstruction, not on HTTP. The earlier evidence cited only the HTTP path, but the matching Lighthouse path (fetch_blobs) also exits early because it cannot build a header or bid for blocks with no commitments.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#14605](https://github.com/OffchainLabs/prysm/pull/14605)

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

**Verdict history.** not (checked) → partial (refuted)

**Sources.** [prysm#13183](https://github.com/OffchainLabs/prysm/pull/13183), [teku#11438](https://github.com/Consensys-Incorporated/teku/pull/11438), [lodestar#10087](https://github.com/ChainSafe/lodestar/pull/10087)

</details>


<a id="gossip_validation-080"></a>
<details>
<summary><b>gossip_validation-080</b> Evict dedup entries when delayed items are dropped — <i>n/a · low · S · memory</i></summary>

**Idea.** When a full delayed queue drops an item, also remove its entries from received/dedup collections so they do not leak or block reprocessing.

**Impact.** No leak exists: Lighthouse inserts into dedup sets only after the capacity check, and gossip dedup lives in seen caches written after verification.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:595`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L595): attestation queue drops new item on full before any bookkeeping
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:670-682`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L670-L682): block root set checked for capacity before insert

**Sources.** [grandine#935](https://github.com/grandinetech/grandine/pull/935)

</details>


<a id="gossip_validation-081"></a>
<details>
<summary><b>gossip_validation-081</b> Expire held unknown-root gossip messages — <i>implemented · low · S · memory</i></summary>

**Idea.** Expire buffered unknown-root gossip messages for blocks seen but never imported, so the global cap does not fill permanently.

**Impact.** Every unknown-root buffer has a timer, so the global cap cannot fill permanently.

**Best measured result.** counter stuck at 16385 for 3+ hours on mainnet node (pr:lodestar#10389)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:53`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L53) QUEUED_ATTESTATION_DELAY 12s
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:595`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L595) MAXIMUM_QUEUED_ATTESTATIONS cap on delay queue
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:1262-1285`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L1262-L1285) expiry prunes awaiting_attestations_per_root and per_payload
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:780-798`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L780-L798) envelopes capped and timed
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:867-893`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L867-L893),1377 data columns capped, counter decremented on expiry

**Skeptic check.** Verified expiry for attestations, payload attestations, envelopes, data columns and LC updates; the cap is on live timed entries, unlike lodestar's stuck counter. Earlier evidence correct (paths slightly mis-prefixed).

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#10389](https://github.com/ChainSafe/lodestar/pull/10389)

</details>


<a id="gossip_validation-082"></a>
<details>
<summary><b>gossip_validation-082</b> Extract block roots only from early messages — <i>n/a · low · S · memory, cpu</i></summary>

**Idea.** Extract referenced block roots only from gossip messages arriving before their block, not all messages, to cut allocations.

**Impact.** Rust has no GC; the Lodestar root-extraction cost was JS garbage collection and has no Lighthouse counterpart.

**Best measured result.** up to 0.4% of gc time saved (pr:lodestar#7208)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/pubsub.rs:567`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L567): block root read from SSZ group id bytes, no GC allocation

**Sources.** [lodestar#7208](https://github.com/ChainSafe/lodestar/pull/7208)

</details>


<a id="gossip_validation-083"></a>
<details>
<summary><b>gossip_validation-083</b> Faster subnet computation in gossip validation — <i>n/a · low · S · cpu</i></summary>

**Idea.** Speed up subnet computation and block verification in gossip validation (unmerged; mechanism unclear).

**Impact.** Unmerged PR with unclear mechanism; Lighthouse subnet computation is plain integer math.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:1129`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1129): subnet check uses cheap arithmetic

**Sources.** [lodestar#1278](https://github.com/ChainSafe/lodestar/pull/1278)

</details>


<a id="gossip_validation-084"></a>
<details>
<summary><b>gossip_validation-084</b> Index pending bids by preference slot and root — <i>not · low · M · cpu</i></summary>

**Idea.** Index pending execution payload bids by proposer-preference slot and dependent root so retries revalidate only matching bids.

**Gap in Lighthouse.** Lighthouse has no pending-bid pool; a bid arriving before its proposer preferences is ignored. Adding a pool indexed by (slot, dependent_root) retried from process_gossip_proposer_preferences would match Teku.

**Impact.** Only helps Gloas bid propagation when preferences arrive late; small and no cost on current mainnet.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:4263-4290`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L4263-L4290): NoProposerPreferences bid result is Ignore, no retry
- [`beacon_node/beacon_chain/src/proposer_preferences_verification/proposer_preference_cache.rs:12`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/proposer_preferences_verification/proposer_preference_cache.rs#L12): preferences cache keyed (slot, dependent_root)
- [`beacon_node/beacon_chain/src/pending_payload_cache/mod.rs:49`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/mod.rs#L49): holds bid+columns by block root, not a retry pool of bids

**Sources.** [teku#11351](https://github.com/Consensys-Incorporated/teku/pull/11351)

</details>


<a id="gossip_validation-085"></a>
<details>
<summary><b>gossip_validation-085</b> Per-(validator, epoch) seen caches checked before validation — <i>implemented · low · S · bandwidth, cpu, disk, memory</i></summary>

**Idea.** Dedupe gossip attestations and aggregates with in-memory seen caches keyed by (attester or aggregator index, target epoch) and check them before state loads and BLS verification, so duplicates from the same validator in an epoch cost a map lookup, not a DB lookup or signature check.

**Impact.** Duplicate attestations/aggregates cost an in-memory bitfield/hashset lookup, no state load or BLS.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:996-1006`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L996-L1006) observed_gossip_attesters (validator, target epoch) checked in verify_middle_checks
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1026-1060`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1026-L1060) verify_slashable runs early+middle checks before any signature work
- [`beacon_node/beacon_chain/src/attestation_verification.rs:572`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L572),589 observed_attestations and observed_aggregators checked in aggregate verify_early_checks
- [`beacon_node/beacon_chain/src/attestation_verification.rs:452`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L452),494 committee lookup and signature after early checks

**Skeptic check.** Confirmed ordering: SingleAttestation carries attester_index so the seen check needs no committee; aggregates check aggregator seen before committee/signature. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#4727](https://github.com/Consensys-Incorporated/teku/pull/4727), [prysm#5158](https://github.com/OffchainLabs/prysm/pull/5158), [prysm#5698](https://github.com/OffchainLabs/prysm/pull/5698), [lodestar#857](https://github.com/ChainSafe/lodestar/pull/857), [lodestar@8d860f90e](https://github.com/ChainSafe/lodestar/commit/8d860f90ef40), [teku#11307](https://github.com/Consensys-Incorporated/teku/pull/11307), [caplin#24376](https://github.com/erigontech/erigon/pull/24376)

</details>


<a id="gossip_validation-086"></a>
<details>
<summary><b>gossip_validation-086</b> Seen caches for exits and slashings — <i>implemented · low · S · bandwidth, cpu</i></summary>

**Idea.** Extend gossip seen caches to voluntary exits, proposer slashings and attester slashings so duplicate operations are dropped before validation.

**Impact.** Already done; duplicates are dropped before signature verification.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/observed_operations.rs:87-122`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_operations.rs#L87-L122) verify_and_observe_parametric short-circuits AlreadyKnown before validate()
- [`beacon_node/beacon_chain/src/beacon_chain.rs:468-472`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L468-L472) observed_voluntary_exits/proposer/attester slashing caches
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2870`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2870),2896,2926 gossip verify functions use the caches
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:2054`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L2054),2120,2184 AlreadyKnown handled on gossip

**Skeptic check.** Confirmed: duplicates are checked against the observed validator indices before validation, and the indices are added only after validation succeeds. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#5174](https://github.com/OffchainLabs/prysm/pull/5174), [lighthouse#1253](https://github.com/sigp/lighthouse/pull/1253)

</details>


<a id="gossip_validation-087"></a>
<details>
<summary><b>gossip_validation-087</b> Size seen caches for the validator set — <i>implemented · low · S · bandwidth, cpu</i></summary>

**Idea.** Size the seen-attester and seen-aggregator gossip caches from the validator count and committee/aggregator counts over several slots, so entries are not evicted before duplicates arrive and duplicates are not revalidated.

**Impact.** No LRU eviction exists: per-epoch bitfields/sets hold every validator for 4 epochs, so duplicates are never revalidated due to eviction.

**Best measured result.** None (pr:prysm#13756)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/observed_attesters.rs:26-37`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_attesters.rs#L26-L37) MAX_CACHED_EPOCHS=4, pruned by epoch
- [`beacon_node/beacon_chain/src/observed_attesters.rs:341-361`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_attesters.rs#L341-L361) per-epoch item grows unbounded, initial capacity = mean of prior epochs
- [`beacon_node/beacon_chain/src/observed_attesters.rs:92-101`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_attesters.rs#L92-L101) EpochBitfield default 16384 (preallocation only)

**Skeptic check.** Verified capacity is just a preallocation hint and entries are dropped only when their epoch leaves the window, which covers the whole gossip validity range. The prysm problem (fixed-size LRU too small) does not exist here.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#13756](https://github.com/OffchainLabs/prysm/pull/13756), [prysm#9476](https://github.com/OffchainLabs/prysm/pull/9476)

</details>


<a id="gossip_validation-088"></a>
<details>
<summary><b>gossip_validation-088</b> Shrink seen-attester cache lookback to two epochs — <i>partial · low · S · memory</i></summary>

**Idea.** Keep only the epochs that can still be valid for attestation inclusion (2 epochs after EIP-7045) in the seen-attesters cache, so the cache holds less memory.

**Gap in Lighthouse.** Lighthouse keeps 4 epochs; with EIP-7045 only current and previous plus the clock-disparity next epoch (3) are needed. Lower MAX_CACHED_EPOCHS to 3, checking the sync/aggregator containers sharing it.

**Impact.** Saves about one epoch of validator bitfield (~150KB per container); negligible.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/observed_attesters.rs:37`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_attesters.rs#L37): MAX_CACHED_EPOCHS = 4 (N+1..N-2)
- [`beacon_node/beacon_chain/src/observed_attesters.rs:410`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_attesters.rs#L410): max_capacity returns it

**Sources.** [lodestar#7838](https://github.com/ChainSafe/lodestar/pull/7838)

</details>


<a id="gossip_validation-089"></a>
<details>
<summary><b>gossip_validation-089</b> Mark seen only after successful validation — <i>implemented · low · S · memory</i></summary>

**Idea.** Insert aggregate attestations into the dedup seen cache only after they pass validation, so invalid messages cannot grow the cache or poison it.

**Impact.** Already done; invalid aggregates do not populate the seen caches.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:570-599`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L570-L599) only read checks (is_known_subset, validator_has_been_observed) before verification; 'do not observe yet'
- [`beacon_node/beacon_chain/src/attestation_verification.rs:856-879`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L856-L879) verify_late_checks runs after signature check
- [`beacon_node/beacon_chain/src/attestation_verification.rs:783-810`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L783-L810) observe_item / observe_validator in late checks
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1120-1135`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1120-L1135) unaggregated observed after full verification

**Skeptic check.** Confirmed that verify_late_checks is called only after verify_signed_aggregate_signatures succeeds, and that the earlier checks are lookups only. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#5959](https://github.com/OffchainLabs/prysm/pull/5959)

</details>


<a id="gossip_validation-090"></a>
<details>
<summary><b>gossip_validation-090</b> Ignore votes for unseen payload without network fetch — <i>not · low · S · bandwidth, latency</i></summary>

**Idea.** When an attestation or aggregate votes for an execution payload envelope not yet seen, return Ignore without fetching the envelope from peers, so unverified gossip cannot trigger network requests.

**Gap in Lighthouse.** Lighthouse triggers a sync lookup for the envelope from unverified attestations (as it does for unknown blocks), bounded by reprocess_allowance.allows_payload(). Ignoring without fetch would need dropping the send_sync_message call in the UnknownPayloadEnvelope arm.

**Impact.** Avoids peer-triggered envelope lookups from unverified gossip; a DoS-hardening gain, not a throughput one, and only post-Gloas.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:627-633`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L627-L633): UnknownPayloadEnvelope returned before signature verification
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:2959-2972`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L2959-L2972): sends UnknownPayloadEnvelopeFromAttestation to sync, then requeues

**Sources.** [prysm#17712](https://github.com/OffchainLabs/prysm/pull/17712)

</details>


<a id="gossip_validation-091"></a>
<details>
<summary><b>gossip_validation-091</b> Replace DB reads in gossip checks with in-memory state — <i>implemented · low · S · cpu, disk, latency</i></summary>

**Idea.** Answer bad-block and seen-proposer checks in gossip validation from in-memory caches or fork choice instead of a database read per message, or drop the DB check where fork choice membership already covers it.

**Impact.** No per-message DB read on the gossip accept path for blocks or attestations.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:970-973`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L970-L973) fork choice contains_block for duplicates
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3879-3885`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3879-L3885) check_invalid_block_roots is an in-memory config set
- [`beacon_node/beacon_chain/src/block_verification.rs:1891-1894`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1891-L1894) store.block_exists only on the non-finalized-descendant error path
- [`beacon_node/beacon_chain/src/pre_finalization_cache.rs:46-77`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pre_finalization_cache.rs#L46-L77) disk read only for unknown attestation heads, cached

**Skeptic check.** Grepped block, blob, data column and attestation verification for store reads: only the error-path block_exists, split info (in memory) and the cached pre-finalization lookup remain. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [lodestar#5803](https://github.com/ChainSafe/lodestar/pull/5803)

</details>


<a id="gossip_validation-093"></a>
<details>
<summary><b>gossip_validation-093</b> Shrink lock critical sections in seen caches — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Compute cache keys and do processing before taking the seen-cache or pending-attestation lock, holding it only for the map lookup or insert, to cut lock contention across concurrent gossip validations.

**Impact.** Key generation is already outside the critical sections. The subset check takes a write lock (observed_aggregates.rs:407 &amp;mut for get_set_index), which is a small residual.

**Best measured result.** None (pr:prysm#15572)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:556-562`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L556-L562) observed_attestation_key_root tree-hashed before taking the lock
- [`beacon_node/beacon_chain/src/attestation_verification.rs:570-581`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L570-L581) lock held only for is_known_subset with the precomputed root
- [`beacon_node/beacon_chain/src/attestation_verification.rs:786-790`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L786-L790) observe_item reuses Some(root), no hashing under lock
- [`beacon_node/beacon_chain/src/attestation_verification.rs:996-1001`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L996-L1001),1126-1129 attester caches keyed by validator index

**Skeptic check.** Confirmed that the Prysm mechanism (generate the key outside the lock) matches Lighthouse: the key root is computed once and passed into both lock sections. The only leftover is that is_known_subset takes .write() rather than .read(), and that costs little.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#15572](https://github.com/OffchainLabs/prysm/pull/15572), [prysm#15579](https://github.com/OffchainLabs/prysm/pull/15579), [prysm#4849](https://github.com/OffchainLabs/prysm/pull/4849)

</details>


<a id="gossip_validation-094"></a>
<details>
<summary><b>gossip_validation-094</b> Prune serialized-bytes cache by key — <i>n/a · low · S · memory</i></summary>

**Idea.** When a block input is written to DB, evict only its own entries from the cache of serialized gossip bytes rather than clearing the whole cache, so other entries remain reusable and avoid re-serialization.

**Impact.** Lighthouse keeps no cache of serialized gossip bytes keyed per block input, so there is nothing to prune.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:2033`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L2033) (as_ssz_bytes only in error log path)

**Sources.** [lodestar#9007](https://github.com/ChainSafe/lodestar/pull/9007)

</details>


<a id="gossip_validation-095"></a>
<details>
<summary><b>gossip_validation-095</b> Larger attestation queues and batch drain per idle — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Size the gossip attestation and aggregate queues for large validator sets and drain a batch on every idle loop iteration, so slot-boundary bursts are not dropped.

**Impact.** Already done; queues scale with the validator set and drain in batches.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_queue.rs:335-365`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_queue.rs#L335-L365) attestation queues sized active_validators*overprovision/slots_per_epoch, aggregate queue 4096
- [`beacon_node/beacon_processor/src/lib.rs:958-1030`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L958-L1030) batches of up to 64 aggregates/attestations formed whenever a worker is free

**Skeptic check.** Confirmed that the queue sizes come from the active validator count, and that batch drain happens on each idle-worker iteration. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus@43c64d32f](https://github.com/status-im/nimbus-eth2/commit/43c64d32f802)

</details>


<a id="gossip_validation-096"></a>
<details>
<summary><b>gossip_validation-096</b> Shorter tuned idle timeout in gossip processor loop — <i>n/a · low · S · cpu, latency</i></summary>

**Idea.** Tune the gossip processor idle timeout down so queued attestations and aggregates get processed sooner when the node is idle, balancing latency against CPU.

**Impact.** The manager task wakes on each work or idle event in tokio; there is no idle timeout to tune.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:688-700`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L688-L700) (event-driven poll with biased select over idle/work/reprocess streams, no idle timer)

**Sources.** [nimbus@c0e11cfba](https://github.com/status-im/nimbus-eth2/commit/c0e11cfba6d0), [nimbus@8f6ce4f88](https://github.com/status-im/nimbus-eth2/commit/8f6ce4f88d53)

</details>


<a id="gossip_validation-097"></a>
<details>
<summary><b>gossip_validation-097</b> Bounded prioritized gossip work queue, blocks first — <i>implemented · low · S · bandwidth, cpu, latency</i></summary>

**Idea.** Put all gossip messages (attestations, slashings, exits) into bounded per-type queues pulled by a scheduler with bounded concurrency that prioritizes blocks over attestations, so attestation floods cannot starve or delay block processing.

**Impact.** Attestation floods are bounded (LIFO drops oldest) and cannot starve block processing.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_queue.rs:357-367`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_queue.rs#L357-L367),483-522 bounded Lifo/Fifo queues per type sized from validator count
- [`beacon_node/beacon_processor/src/lib.rs:890`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L890) can_spawn bounded by max_workers
- [`beacon_node/beacon_processor/src/lib.rs:929`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L929) gossip blocks popped before aggregates (:969) and attestations (:1025)
- [`beacon_node/beacon_processor/src/lib.rs:1238`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1238) gossip blocks dispatched immediately when a worker is free

**Skeptic check.** This is the Lighthouse BeaconProcessor itself (lighthouse#1511/#1546). Verified bounded queues, worker cap and block-first priority.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#5195](https://github.com/ChainSafe/lodestar/pull/5195), [lodestar#5350](https://github.com/ChainSafe/lodestar/pull/5350), [lighthouse#1511](https://github.com/sigp/lighthouse/pull/1511), [lighthouse#1546](https://github.com/sigp/lighthouse/pull/1546), [lodestar#5444](https://github.com/ChainSafe/lodestar/pull/5444), [caplin#11790](https://github.com/erigontech/erigon/pull/11790)

</details>


<a id="gossip_validation-098"></a>
<details>
<summary><b>gossip_validation-098</b> Raise priority of rare gossip topics — <i>not · low · S · latency</i></summary>

**Idea.** Give rare topics such as voluntary exits and BLS-to-execution changes higher queue priority than attestations so they do not wait behind attestation bursts.

**Gap in Lighthouse.** Rare topics are intentionally last in the priority chain; moving exits/BLS changes up would mean reordering in the manager loop around lib.rs:1141.

**Impact.** Exits and BLS-to-execution changes are rare and low value to the node; reordering would only help latency of those messages in bursts, with no mainnet throughput gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:1130-1147`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1130-L1147) (slashings and exits deliberately checked late, after attestations and sync messages)

**Sources.** [lodestar#5407](https://github.com/ChainSafe/lodestar/pull/5407)

</details>


<a id="gossip_validation-099"></a>
<details>
<summary><b>gossip_validation-099</b> Raise sync committee gossip queue concurrency — <i>n/a · low · S · cpu, latency</i></summary>

**Idea.** Increase the processing concurrency or worker share for sync committee message and contribution queues so more of them are processed per slot.

**Impact.** Lighthouse has one shared worker pool with priority order, no per-queue concurrency share to raise.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:1077`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1077) (sync messages processed after attestations from one shared worker pool)
- [`beacon_node/beacon_processor/src/scheduler/work_queue.rs:368-369`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_queue.rs#L368-L369) (sync queues 2048/1024)

**Sources.** [lodestar#2906](https://github.com/ChainSafe/lodestar/pull/2906)

</details>


<a id="gossip_validation-100"></a>
<details>
<summary><b>gossip_validation-100</b> Do not gate gossip work during block processing — <i>implemented · low · S · latency</i></summary>

**Idea.** Remove any gate that pauses gossip job processing while a current-slot block is imported, since it causes large job wait times.

**Impact.** No gate exists, so the Lodestar wait-time problem does not occur; blocks have only priority, and other workers keep processing gossip.

**Best measured result.** None (pr:lodestar#7848)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:897-1200`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L897-L1200) work dispatch has priority ordering but no flag that pauses gossip work during block import

**Skeptic check.** Lodestar removed an isProcessingCurrentSlotBlock flag. Grep found no equivalent flag in the beacon processor. Attestations for a block that is not yet imported wait per message in the reprocess queue, and no global gate exists.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#7848](https://github.com/ChainSafe/lodestar/pull/7848)

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


<a id="gossip_validation-102"></a>
<details>
<summary><b>gossip_validation-102</b> Maintain queue counters instead of scanning — <i>implemented · low · S · cpu</i></summary>

**Idea.** Keep running counts of gossip messages queued while awaiting a block or payload instead of summing per-root set sizes on every message, replacing an O(N) hot-path scan with O(1).

**Impact.** Already O(1); no per-root sum on the hot path.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:343-344`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L343-L344) queued_data_columns_count maintained counter
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:595`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L595) attestation cap uses attestations_delay_queue.len() O(1)
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:867`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L867) data column cap uses the counter
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:1399-1434`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L1399-L1434) metrics use len()

**Skeptic check.** Confirmed that every capacity check in the reprocess queue uses a delay-queue len() or the maintained queued_data_columns_count, and never sums sets per root. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#9170](https://github.com/ChainSafe/lodestar/pull/9170)

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

**Verdict history.** not (checked) → partial (refuted)

**Sources.** [lodestar#5363](https://github.com/ChainSafe/lodestar/pull/5363), [lodestar#10419](https://github.com/ChainSafe/lodestar/pull/10419), [lodestar#7009](https://github.com/ChainSafe/lodestar/pull/7009), [lodestar#6883](https://github.com/ChainSafe/lodestar/pull/6883), [lodestar#6715](https://github.com/ChainSafe/lodestar/pull/6715)

</details>


<a id="gossip_validation-105"></a>
<details>
<summary><b>gossip_validation-105</b> Minimum bid increment before forwarding — <i>not · low · S · bandwidth, cpu</i></summary>

**Idea.** Forward a gossip builder bid only if it beats the current best bid for its tuple by a minimum increment, so tiny-increment bid spam is neither validated nor propagated.

**Gap in Lighthouse.** Replace the strict `bid_value <= cached` check with a minimum increment over the cached value (lodestar: min(max(0.0001 ETH, 3%), 0.01 ETH)), as the bid_value_over_threshold TODO in GossipVerifiedPayloadBid::new suggests.

**Impact.** Fewer BLS signature checks and forwards of tiny-increment bids. The existing one-bid-per-builder-per-(slot, parent) dedup already stops a single builder from laddering, so the extra saving only applies when many builders bid against each other.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/payload_bid_verification/gossip_verified_bid.rs:318-329`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_bid_verification/gossip_verified_bid.rs#L318-L329) only rejects bid_value &lt;= cached value (TODO(gloas): bid_value_over_threshold)
- [`beacon_node/beacon_chain/src/payload_bid_verification/payload_bid_cache.rs:92-115`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_bid_verification/payload_bid_cache.rs#L92-L115) observe_bid replaces on any strictly higher value
- [`beacon_node/beacon_chain/src/payload_bid_verification/gossip_verified_bid.rs:304-316`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_bid_verification/gossip_verified_bid.rs#L304-L316) seen_builder_bid_for_parent rejects a second bid from the same builder for (slot, parent)

**Verdict history.** not (checked) → not (refuted)

**Sources.** [lodestar#9706](https://github.com/ChainSafe/lodestar/pull/9706), [teku#10198](https://github.com/Consensys-Incorporated/teku/pull/10198)

</details>


<a id="gossip_validation-106"></a>
<details>
<summary><b>gossip_validation-106</b> Once-cell per shuffling key for concurrent computes — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Guard the proposer shuffling cache with a per-(epoch, decision root) once-cell or promise so concurrent gossip verifications wait for a single computation instead of each recomputing it.

**Impact.** Already done; concurrent gossip verifications share one computation of the proposer shuffling.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:85-87`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L85-L87) LruCache&lt;(Epoch, Hash256), Arc&lt;OnceCell&lt;EpochBlockProposers&gt;&gt;&gt;
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:188-200`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L188-L200) get_or_insert_key then get_or_try_init outside the mutex
- [`beacon_node/beacon_chain/src/block_verification.rs:1031`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1031) block gossip uses with_proposer_cache
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1746`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1746) column gossip uses it
- [`beacon_node/beacon_chain/src/payload_envelope_verification/gossip_verified_envelope.rs:227`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/gossip_verified_envelope.rs#L227) envelope gossip uses it

**Skeptic check.** This is the Lighthouse PR itself (#7304). Confirmed the OnceCell is used on every gossip verification path for blocks, columns, envelopes and proposer preferences.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#7304](https://github.com/sigp/lighthouse/pull/7304)

</details>


<a id="gossip_validation-107"></a>
<details>
<summary><b>gossip_validation-107</b> Singleflight state replays for sidecar verification — <i>implemented · medium · S · cpu, memory</i></summary>

**Idea.** Deduplicate concurrent state replays/regenerations for the same target when many data column sidecars arrive at once and each needs the same verifying state.

**Impact.** Concurrent sidecars for the same block share one state load through the OnceCell keyed by (epoch, decision root); no duplicate replays.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:188-197`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L188-L197) get_or_insert_key returns a shared Arc&lt;OnceCell&gt;; get_or_try_init runs state_provider once while concurrent callers wait
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1746-1769`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1746-L1769) verify_proposer_and_signature: the only state need of column gossip is the proposer, loaded inside the with_proposer_cache closure
- [`beacon_node/store/src/hot_cold_store.rs:1124-1185`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1124-L1185) get_advanced_hot_state checks the state cache first and caches the loaded state

**Skeptic check.** Verified the OnceCell singleflight and that column gossip verification needs no other state than the proposer lookup. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#16550](https://github.com/OffchainLabs/prysm/pull/16550), [caplin#22683](https://github.com/erigontech/erigon/pull/22683)

</details>


<a id="gossip_validation-108"></a>
<details>
<summary><b>gossip_validation-108</b> Reduce duplicate work in aggregate validation — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Share checks and cached states across the steps of gossip aggregate-and-proof validation so the same state or computation is not produced twice per message.

**Impact.** Aggregate validation already does one committee lookup per message and shares it across the aggregator, membership and indexing checks; no duplicate state work.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:1617-1660`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1617-L1660) map_attestation_committees resolves committees once via with_committee_cache (shuffling cache, state load only on miss)
- [`beacon_node/beacon_chain/src/attestation_verification.rs:679-770`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L679-L770) one closure does the selection-proof aggregator check, committee membership and indexed attestation from the same committee lookup
- [`beacon_node/beacon_chain/src/attestation_verification.rs:556-562`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L556-L562) observed_attestation_key_root computed once in early checks and reused in verify_late_checks (line 810)

**Skeptic check.** Read IndexedAggregatedAttestation::verify_slashable and map_attestation_committees: one committee-cache read feeds every check, and the key root is reused. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#1438](https://github.com/ChainSafe/lodestar/pull/1438)

</details>


<a id="gossip_validation-109"></a>
<details>
<summary><b>gossip_validation-109</b> Pass gossip attestations by reference — <i>partial · low · S · cpu, memory</i></summary>

**Idea.** Take gossip attestations by reference in the processing entry point and clone only the small attestation data where needed, not the whole signed object.

**Gap in Lighthouse.** On the unaggregated gossip hot path (process_gossip_attestation and process_gossip_attestation_batch) the Attestation that verification already built and owns is deep-cloned via clone_as_attestation and the original is discarded; VerifiedUnaggregatedAttestation needs an into_parts/into_attestation_and_indexed accessor so the owned value is moved. The aggregate path also clones the selection proof signature (attestation_verification.rs:687, flagged by a TODO comment).

**Impact.** Saves one heap-allocated Attestation clone (aggregation bitlist plus signature) per gossip unaggregated attestation, which is thousands per slot; small CPU and allocator gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:280-301`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L280-L301) process_gossip_attestation verifies &amp;attestation, then calls verified_attestation.attestation().clone_as_attestation() and then into_indexed_attestation(), which drops the owned Attestation
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:357`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L357) same clone_as_attestation in process_gossip_attestation_batch
- [`beacon_node/beacon_chain/src/attestation_verification.rs:352-362`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L352-L362) VerifiedUnaggregatedAttestation owns `attestation: Attestation<E>` but only exposes into_indexed_attestation, so callers cannot move it out
- [`consensus/types/src/attestation/attestation.rs:339-344`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/attestation/attestation.rs#L339-L344) clone_as_attestation clones the whole attestation (bits, data, signature)
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:177-182`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L177-L182) aggregates are moved out of the Box without a clone (done right there)

**Skeptic check.** Messages are boxed and verified by reference as the earlier check said, and aggregates move without a clone. But the earlier claim that the clone at line 294 is needed is wrong: the verified struct already owns that Attestation and drops it right after the clone.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [ethlambda#278](https://github.com/lambdaclass/ethlambda/pull/278)

</details>


<a id="gossip_validation-110"></a>
<details>
<summary><b>gossip_validation-110</b> Penalize peers sending too-old messages — <i>not · low · S · bandwidth, cpu</i></summary>

**Idea.** Penalize peers strictly for attestations and sync messages older than the earliest permissible slot (after clock disparity) to discourage spam of stale messages.

**Gap in Lighthouse.** Set STRICT_LATE_MESSAGE_PENALTIES true, or make the hindsight-invalid penalty unconditional (keeping tolerance high) in the AttnError::PastSlot and SyncCommitteeError::PastSlot arms. PR 4873 was closed unmerged.

**Impact.** Only a peer-scoring hardening against stale-message spam; no direct CPU saving on a normal node.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:76`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L76) STRICT_LATE_MESSAGE_PENALTIES = false
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:2654-2675`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L2654-L2675) attestation PastSlot only Ignore, penalty gated by the false const
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:3350-3395`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L3350-L3395) sync PastSlot same

**Sources.** [lighthouse#4873](https://github.com/sigp/lighthouse/pull/4873)

</details>


<a id="gossip_validation-111"></a>
<details>
<summary><b>gossip_validation-111</b> Plain map for bounded seen key space — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Track already-seen slashed validator indices in a plain map instead of an LRU cache, since the key space is bounded and needs no eviction bookkeeping.

**Impact.** None; Lighthouse already uses a plain set for the bounded validator-index key space.

**Best measured result.** None (pr:prysm#8332)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/observed_operations.rs:27`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_operations.rs#L27) observed_validator_indices: HashSet&lt;u64&gt; for exits, proposer slashings and attester-slashed indices, no LRU

**Skeptic check.** Confirmed ObservedOperations uses a plain HashSet&lt;u64&gt; including the attester-slashing intersection indices, which is exactly the Prysm change. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#8332](https://github.com/OffchainLabs/prysm/pull/8332)

</details>


<a id="gossip_validation-112"></a>
<details>
<summary><b>gossip_validation-112</b> Only BLS-verify queued envelopes for known proposers — <i>implemented · low · S · cpu</i></summary>

**Idea.** For a gossip payload envelope whose block is unknown and that will only be queued, ignore it unless it is non-self-built or its proposer is in the known lookahead, so unknown-parent envelopes cannot force signature checks.

**Impact.** Unknown-parent envelopes never trigger BLS work before the block is known, so the Prysm DoS vector does not exist.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/payload_envelope_verification/gossip_verified_envelope.rs:162-168`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/gossip_verified_envelope.rs#L162-L168) BlockRootUnknown is returned from the fork choice lookup before any store read or signature check
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:3894-3925`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L3894-L3925) unknown-block envelope is IGNOREd and a closure that re-runs full verification is sent to the reprocess queue
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:115`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L115) UnknownBlockForEnvelope queued by block root

**Skeptic check.** Verified that GossipVerifiedEnvelope::new exits at the fork choice lookup before signature verification and that the queued path re-verifies only after block import. Earlier evidence was right; the effect is the same with a stronger rule.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#16461](https://github.com/OffchainLabs/prysm/pull/16461)

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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [silver#166](https://github.com/gattaca-com/silver/pull/166)

</details>


<a id="gossip_validation-114"></a>
<details>
<summary><b>gossip_validation-114</b> Use proposer lookahead to skip epoch transitions — <i>implemented · medium · S · cpu, latency, memory</i></summary>

**Idea.** Post-Fulu, read the expected proposer for gossip blocks and data column sidecars from the parent state's proposer lookahead instead of advancing a state across an epoch boundary or regenerating a block-slot state.

**Impact.** Post-Fulu, a parent state in epoch E-1 or E is used as is; the lookahead gives the proposer and no epoch transition runs unless the parent is more than one epoch behind (which the lookahead cannot cover anyway).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:321-355`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L321-L355) ensure_state_can_determine_proposers_for_epoch advances only when state epoch &lt; decision_slot+1 epoch (post-Fulu: E-1)
- [`beacon_node/beacon_chain/src/block_verification.rs:1031-1050`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1031-L1050) gossip block proposer via with_proposer_cache, miss loads parent state un-advanced (load_parent -&gt; get_advanced_hot_state at block_verification.rs:2065)
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1746-1769`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1746-L1769) column proposer via with_proposer_cache with the parent state
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:219`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L219) get_beacon_proposer_indices reads the lookahead

**Skeptic check.** Verified both gossip block and column paths read the proposer from the parent state's lookahead via the proposer cache and only advance when strictly needed. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

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

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [prysm#11932](https://github.com/OffchainLabs/prysm/pull/11932), [prysm#13014](https://github.com/OffchainLabs/prysm/pull/13014), [prysm#15972](https://github.com/OffchainLabs/prysm/pull/15972), [caplin#24523](https://github.com/erigontech/erigon/pull/24523)

</details>


<a id="gossip_validation-116"></a>
<details>
<summary><b>gossip_validation-116</b> Use cached checkpoint or advanced states for validation — <i>implemented · medium · S · cpu, latency, memory</i></summary>

**Idea.** Validate gossip aggregates, blocks and sync messages against already cached states (checkpoint/target state, pre-advanced slot state, parent post-state, tip state) instead of copying the head state or regenerating.

**Impact.** Attestation, aggregate, sync message and block gossip already use cached committees or cached/advanced states; no full head-state copy or regeneration on the common path.

**Best measured result.** None (pr:prysm#5737)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:315-460`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L315-L460) with_cached_shuffling: read-lock hit, promise on miss, uses the head snapshot (CoW clone) or get_advanced_hot_state from the state cache
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1430-1456`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1430-L1456) sync_committee_at_epoch reads the committee from the head state by reference via with_head
- [`beacon_node/beacon_chain/src/block_verification.rs:2059-2065`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L2059-L2065) block parent from get_advanced_hot_state (pre-advanced by state_advance_timer)

**Skeptic check.** Checked attestation, sync committee and block gossip paths; all use caches and milhouse CoW states. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#5737](https://github.com/OffchainLabs/prysm/pull/5737), [lodestar#2261](https://github.com/ChainSafe/lodestar/pull/2261), [teku#3385](https://github.com/Consensys-Incorporated/teku/pull/3385), [prysm#12506](https://github.com/OffchainLabs/prysm/pull/12506), [prysm#17788](https://github.com/OffchainLabs/prysm/pull/17788), [lodestar@6b148f3b7](https://github.com/ChainSafe/lodestar/commit/6b148f3b7bbc)

</details>


<a id="gossip_validation-117"></a>
<details>
<summary><b>gossip_validation-117</b> Direct state lookup by block root — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** When the block is known to be at the message slot, fetch its post state directly by block root rather than via a slot-plus-root checkpoint-state path, avoiding queue locks and key scans per message.

**Impact.** Both Teku targets (payload attestation and execution payload envelope validators) already look up by block/state root without a checkpoint-state queue.

**Best measured result.** None (pr:teku#11215)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/payload_attestation_verification/gossip_verified_payload_attestation.rs:84-111`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_attestation_verification/gossip_verified_payload_attestation.rs#L84-L111) block-at-slot check, then PTC from with_cached_shuffling keyed by beacon_block_root
- [`beacon_node/beacon_chain/src/payload_envelope_verification/mod.rs:372-389`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/mod.rs#L372-L389) load_snapshot_from_state_root uses get_hot_state(block_state_root) directly, no advance
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:349-354`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L349-L354) read-lock hit path

**Skeptic check.** Verified both analogues of the Teku validators: payload attestations hit the shuffling cache, and external-builder envelopes load the block's post state directly by state root. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

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

**Impact.** No per-(parent, slot) advanced state is copied or retained for bids, so the memory cost the Caplin PR removes does not exist in Lighthouse.

**Best measured result.** None (pr:caplin#25331)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/payload_bid_verification/gossip_verified_bid.rs:331-389`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_bid_verification/gossip_verified_bid.rs#L331-L389) GossipVerifiedPayloadBid::new borrows cached_head.snapshot.beacon_state; only at the Gloas fork boundary loads an advanced head state
- [`beacon_node/beacon_chain/src/payload_bid_verification/gossip_verified_bid.rs:125-157`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_bid_verification/gossip_verified_bid.rs#L125-L157) verify_bid_state_conditions reads builder fields from the borrowed state

**Skeptic check.** Confirmed bid validation borrows the head snapshot by reference and caches no state per key. Earlier evidence was right (line numbers slightly off).

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#25331](https://github.com/erigontech/erigon/pull/25331)

</details>


<a id="gossip_validation-120"></a>
<details>
<summary><b>gossip_validation-120</b> Ignore bids that force epoch-transition regen — <i>n/a · low · cpu</i></summary>

**Idea.** Ignore execution payload bids that build on the head's parent at epoch boundaries, since validating them forces regenerating an unusable parent state through an epoch transition.

**Impact.** Lighthouse validates parent-building bids against the cached head state and cached randao values, never regenerating the parent state through an epoch transition.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/payload_bid_verification/gossip_verified_bid.rs:354-396`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_bid_verification/gossip_verified_bid.rs#L354-L396) uses the cached head snapshot state (or get_advanced_hot_state only at the Gloas fork boundary)
- [`beacon_node/beacon_chain/src/payload_bid_verification/gossip_verified_bid.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_bid_verification/gossip_verified_bid.rs):~440 prev_randao taken from cached_head.parent_random()

**Sources.** [lodestar#9756](https://github.com/ChainSafe/lodestar/pull/9756)

</details>


<a id="gossip_validation-121"></a>
<details>
<summary><b>gossip_validation-121</b> Signature check before state advance — <i>partial · low · S · cpu, latency</i></summary>

**Idea.** Run the BLS signature check against the un-advanced dependent state before advancing a state copy across an epoch boundary, so forged messages never trigger an epoch transition.

**Gap in Lighthouse.** GossipVerifiedProposerPreferences::new runs with_proposer_cache (state load and epoch-crossing partial_state_advance on a miss) before verify_signature. The validator_index is in the message, so the signature can be checked first with validator_pubkey_cache and spec.fork_at_epoch(proposal_epoch), which is exactly prysm#17656. Lighthouse's proposer-cache memoisation limits the cost to once per (proposal_epoch, dependent_root), but a forged message on a new qualifying fork-choice tip still pays an epoch transition.

**Impact.** Removes a DoS vector where forged proposer preferences referencing a new valid dependent root trigger an epoch transition before BLS rejection; bounded today by the per-key cache.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/proposer_preferences_verification/gossip_verified_proposer_preferences.rs:133-169`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/proposer_preferences_verification/gossip_verified_proposer_preferences.rs#L133-L169) on a proposer-cache miss, get_advanced_hot_state + ensure_state_can_determine_proposers_for_epoch (partial_state_advance across the epoch) runs first
- [`beacon_node/beacon_chain/src/proposer_preferences_verification/gossip_verified_proposer_preferences.rs:178-194`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/proposer_preferences_verification/gossip_verified_proposer_preferences.rs#L178-L194) signature checked only after, although it needs only pubkey_cache.get(validator_index) and the fork
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:188-197`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L188-L197) OnceCell caches the result per (epoch, dependent_root), so repeats of the same key do not re-advance

**Skeptic check.** The source PR is about the proposer_preferences topic. The Lighthouse version of it advances the state before the signature check on a cache miss. The earlier evidence cited block and attestation paths, where the proposer or committee is needed to get the pubkey, so reordering there is not possible.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [prysm#17656](https://github.com/OffchainLabs/prysm/pull/17656)

</details>


<a id="gossip_validation-122"></a>
<details>
<summary><b>gossip_validation-122</b> Builder pubkey in fork choice for envelope sig — <i>not · medium · M · cpu, disk, latency</i></summary>

**Idea.** Store the builder pubkey on the fork choice node so gossip payload envelope signatures can be checked without loading or replaying a block state.

**Gap in Lighthouse.** Store the builder pubkey (or the builder index plus a builder pubkey cache) on the proto-array node, and in the external-builder branch of GossipVerifiedEnvelope::new call verify_signature with that pubkey and the fork. Do not load the snapshot there.

**Impact.** Gossip checks of external-builder envelopes would no longer need the block state, so spam with bad signatures could not force state loads. The gain is partial: the block's post-state is usually still in the hot state cache, and import reuses the snapshot.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/payload_envelope_verification/gossip_verified_envelope.rs:271-282`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/gossip_verified_envelope.rs#L271-L282) external-builder envelopes load the block state and call verify_signature_with_state (TODO(gloas): builder pubkey cache)
- [`beacon_node/beacon_chain/src/payload_envelope_verification/gossip_verified_envelope.rs:224-270`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/gossip_verified_envelope.rs#L224-L270) only the self-build path uses the proposer cache and the validator pubkey cache
- [`beacon_node/beacon_chain/src/payload_envelope_verification/mod.rs:372-396`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/mod.rs#L372-L396) load_snapshot_from_state_root calls store.get_hot_state (a state cache hit usually, a disk replay otherwise)
- [`consensus/proto_array/src/proto_array.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs) has no builder field on ProtoNode

**Verdict history.** not (checked) → not (refuted)

**Sources.** [prysm#17652](https://github.com/OffchainLabs/prysm/pull/17652)

</details>


<a id="gossip_validation-123"></a>
<details>
<summary><b>gossip_validation-123</b> Drop redundant finalized-descendant check — <i>not · low · S · cpu</i></summary>

**Idea.** Skip an explicit finalized-descendant check on gossip blocks where loading the parent state or fork choice membership already implies it.

**Gap in Lighthouse.** Could drop the explicit finalized-descendant check since fork choice get_block of the parent already enforces it, in check_block_is_finalized_checkpoint_or_descendant.

**Impact.** One hash lookup in proto-array per gossip block; unmeasurable, and the split-block check there is still needed.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:981`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L981) explicit check_block_is_finalized_checkpoint_or_descendant under already-held fork choice lock
- [`beacon_node/beacon_chain/src/block_verification.rs:1874`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1874) also needs split-block descent check, not implied by parent lookup

**Sources.** [lodestar@26b11fa27](https://github.com/ChainSafe/lodestar/commit/26b11fa27b11)

</details>


<a id="gossip_validation-124"></a>
<details>
<summary><b>gossip_validation-124</b> Drop redundant slot-window check — <i>n/a · low · S · cpu</i></summary>

**Idea.** Remove an attestation slot-window check implied by the later clock-disparity check, and compute the epoch once.

**Impact.** Lighthouse has no redundant clock-validation check to remove; at most three slot clock reads could be folded into one.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:1298`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1298) verify_propagation_slot_range has no separate 128-slot clock check; only a future-tolerance and earliest-slot check

**Sources.** [prysm#13813](https://github.com/OffchainLabs/prysm/pull/13813)

</details>


<a id="gossip_validation-125"></a>
<details>
<summary><b>gossip_validation-125</b> Skip repeated signature verification — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Ensure aggregate/attestation signatures are verified once: remove duplicated verification calls and honor an already-verified flag.

**Impact.** Each gossip attestation or aggregate signature is verified once (batch or individual fallback), and pool and fork choice inserts take the verified wrappers.

**Best measured result.** None (pr:prysm#5676)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification/batch.rs:195-199`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification/batch.rs#L195-L199) batch success sets CheckAttestationSignature::No
- [`beacon_node/beacon_chain/src/attestation_verification/batch.rs:203-211`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification/batch.rs#L203-L211) from_indexed is called with that flag
- [`beacon_node/beacon_chain/src/attestation_verification.rs:849-866`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L849-L866) aggregate signatures checked only when the flag is Yes
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:2710`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L2710) add_to_block_inclusion_pool takes verified wrappers with no re-verification

**Skeptic check.** Read the batch and single paths: individual checks happen only after a failed batch, and the downstream inserts do not verify again. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#5676](https://github.com/OffchainLabs/prysm/pull/5676), [lodestar#2264](https://github.com/ChainSafe/lodestar/pull/2264), [teku#6113](https://github.com/Consensys-Incorporated/teku/pull/6113)

</details>


<a id="gossip_validation-126"></a>
<details>
<summary><b>gossip_validation-126</b> Single fork choice lock per attestation — <i>not · low · S · cpu, latency</i></summary>

**Idea.** Take the fork choice read lock once in attestation gossip verification and run all head-block checks under it.

**Gap in Lighthouse.** The upstream PR is still open and not in this checkout. Take one read lock in verify_head_block_is_known and skip the second is_finalized_checkpoint_or_descendant for blocks found in fork choice (keep it for early attester cache hits and the split-block check).

**Impact.** Halves fork choice read-lock acquisitions per unaggregated attestation, thousands per slot; small CPU/contention gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:1251`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1251) verify_head_block_is_known takes fork_choice_read_lock for get_block
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1527`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1527) verify_attestation_is_finalized_checkpoint_or_descendant takes the lock a second time
- beacon_node/consensus/fork_choice/src/fork_choice.rs:1606 get_block already filters to finalized descendants

**Sources.** [lighthouse#9616](https://github.com/sigp/lighthouse/pull/9616)

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

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [lighthouse#7973](https://github.com/sigp/lighthouse/pull/7973), [prysm#3403](https://github.com/OffchainLabs/prysm/pull/3403), [teku#8352](https://github.com/Consensys-Incorporated/teku/pull/8352), [lodestar#10429](https://github.com/ChainSafe/lodestar/pull/10429)

</details>


<a id="gossip_validation-128"></a>
<details>
<summary><b>gossip_validation-128</b> Ignore already known blocks and columns early — <i>implemented · medium · S · cpu</i></summary>

**Idea.** Before processing a gossip block or data column sidecar, check whether it is already in the store or block input and skip it.

**Impact.** Known blocks and columns are dropped before parent load, inclusion proof and KZG work.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:970-972`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L970-L972) fork_choice contains_block -&gt; DuplicateFullyImported before parent/state load
- [`beacon_node/beacon_chain/src/block_verification.rs:1086-1095`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1086-L1095) observed_block_producers -&gt; DuplicateImportStatusUnknown
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1158`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1158) verify_is_unknown_sidecar before inclusion proof and KZG
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1166-1176`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1166-L1176) DA checker hit returns PriorKnownUnpublished without KZG
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1239`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1239) same check on the Gloas path

**Skeptic check.** Verified the block check (fork choice, post-finalization, equivalent to prysm's DB check) and the column checks (observed cache plus DA-checker cache, equivalent to lodestar's block-input check) on both Fulu and Gloas gossip paths. Earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#4721](https://github.com/OffchainLabs/prysm/pull/4721), [lodestar#8382](https://github.com/ChainSafe/lodestar/pull/8382)

</details>


<a id="gossip_validation-129"></a>
<details>
<summary><b>gossip_validation-129</b> Do not track already imported blocks in pending pool — <i>n/a · low · S · memory</i></summary>

**Idea.** Do not create pending-pool trackers for blocks already imported, since trackers linger for slots and can leak.

**Impact.** Lighthouse's availability cache is size-bounded LRU with no per-block tracker that lingers; an already-imported block does not leak a tracker in the same way.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:442`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L442) pending components live in a bounded LRU cache and are consumed on import

**Sources.** [teku#7711](https://github.com/Consensys-Incorporated/teku/pull/7711)

</details>


<a id="gossip_validation-130"></a>
<details>
<summary><b>gossip_validation-130</b> Recheck peer score after async await — <i>not · low · M · cpu</i></summary>

**Idea.** After an async state lookup in gossip validation, recheck whether the sender became a banned peer and skip the remaining expensive validation.

**Gap in Lighthouse.** After the async state load in verify_envelope_for_gossip, pass a closure to check whether the sender is now banned and return Ignore before computing the signing root.

**Impact.** Saves envelope signing-root hashing for a banned peer in a narrow race; only matters under attack.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/payload_envelope_verification/gossip_verified_envelope.rs:411`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/gossip_verified_envelope.rs#L411) envelope verification awaits state lookup then does signature work
- [`beacon_node/lighthouse_network/src/service/mod.rs:1961`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L1961) banning acts at discovery/swarm level, queued gossip work is not rechecked

**Sources.** [lodestar#10420](https://github.com/ChainSafe/lodestar/pull/10420)

</details>


<a id="gossip_validation-131"></a>
<details>
<summary><b>gossip_validation-131</b> Recheck timeliness before forwarding — <i>implemented · medium · S · bandwidth, cpu</i></summary>

**Idea.** After queued processing, re-check that attestations and sync messages are still timely before accepting them for propagation.

**Impact.** Stale queued attestations and sync messages are IGNOREd rather than forwarded.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:3674-3688`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L3674-L3688) propagate_attestation_if_timely rechecks verify_propagation_slot_range
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:416`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L416) and :607 used for unaggregated and aggregated results, including reprocessed ones
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:3709-3722`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L3709-L3722) propagate_sync_message_if_timely
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:2342`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L2342) and :2405 used for sync messages and contributions

**Skeptic check.** This is Lighthouse's own PR, and the helpers are live on every attestation and sync result path. Payload attestations accept right after a verification that itself checks the current slot, so the effect is the same there.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#2978](https://github.com/sigp/lighthouse/pull/2978)

</details>


<a id="gossip_validation-132"></a>
<details>
<summary><b>gossip_validation-132</b> Regossip envelopes after reprocessing — <i>implemented · low · S · latency</i></summary>

**Idea.** After importing a payload envelope from the reprocess queue, propagate it on gossip if it is still timely.

**Impact.** Reprocessed envelopes are regossiped when they are still in the current slot.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:3692-3705`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L3692-L3705) propagate_envelope_if_timely
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:3911-3921`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L3911-L3921) reprocess closure re-verifies the envelope and calls propagate_envelope_if_timely before import

**Skeptic check.** This is Lighthouse's own PR, and the code is present on the unknown-block reprocess path. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#9210](https://github.com/sigp/lighthouse/pull/9210)

</details>


<a id="gossip_validation-133"></a>
<details>
<summary><b>gossip_validation-133</b> Reject null-slot gossip before queueing — <i>n/a · low · S · cpu, memory</i></summary>

**Idea.** Reject and penalize gossip messages on slot-bearing topics when no slot can be extracted, rather than queueing them.

**Impact.** Lighthouse does not extract the slot from raw bytes to route queues; undecodable messages are rejected at decode time.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:229`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L229) gossip_penalize_peer; messages are SSZ-decoded in the network layer before queueing, so the slot is always present

**Sources.** [lodestar#10241](https://github.com/ChainSafe/lodestar/pull/10241)

</details>


<a id="gossip_validation-134"></a>
<details>
<summary><b>gossip_validation-134</b> Queue gossip awaiting unknown dependency — <i>implemented · low · M · latency</i></summary>

**Idea.** Hold gossip messages whose block or payload is unknown in a root-keyed queue and reprocess them on arrival, extracting slot and root from bytes before decoding.

**Impact.** Hold-and-release by block root and by envelope root already exists for the Gloas types the Lodestar PR targets.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:111-151`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L111-L151) root-keyed queues for unknown block (unaggregate, aggregate, payload attestation, data column, envelope) and unknown payload envelope (UnknownPayloadUnaggregate/Aggregate)
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:124-127`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L124-L127) BlockImported and PayloadEnvelopeImported release the queues
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:2960-2975`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L2960-L2975) UnknownPayloadEnvelope triggers an envelope lookup and queueing
- [`beacon_node/lighthouse_network/src/types/pubsub.rs:195`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L195) full SSZ decode before routing

**Skeptic check.** Confirmed that both the await-block and await-envelope queues exist, the second being the core of lodestar#9025. Lighthouse decodes before it queues instead of reading slot and root from the raw bytes. Lodestar needs that because it decodes on its main thread; Lighthouse decodes off that path, so the effect is equivalent.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#9025](https://github.com/ChainSafe/lodestar/pull/9025)

</details>


<a id="gossip_validation-135"></a>
<details>
<summary><b>gossip_validation-135</b> Add attestations directly to pool after verify — <i>implemented · low · S · cpu, latency, memory</i></summary>

**Idea.** After signature check, add attestations directly to the pool without an intermediate queue, pass a single validator index for single votes, and free decompressed buffers before async validation.

**Impact.** There is no intermediate queue between signature verification and the pools, and SingleAttestation already carries one attester index.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:390-470`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L390-L470) verified unaggregate goes straight to fork choice and add_to_naive_aggregation_pool in the same worker
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:592-660`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L592-L660) verified aggregate goes straight to fork choice and add_to_block_inclusion_pool
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2596-2633`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2596-L2633) add_to_naive_aggregation_pool takes the attestation by reference

**Skeptic check.** Verified that pool insertion happens inline after verification. Freeing the decompressed buffer is specific to Nim memory management. The only leftover clone on this path is covered under gossip_validation-109.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#2519](https://github.com/status-im/nimbus-eth2/pull/2519)

</details>


<a id="gossip_validation-136"></a>
<details>
<summary><b>gossip_validation-136</b> Avoid copying signature batches — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Do not copy the signature batch in the batch verifier when nothing mutates it, cutting allocations.

**Impact.** No defensive copy of the batch exists to remove; the remaining per-batch Vecs in blst.rs are needed by the blst API.

**Best measured result.** None (pr:prysm#16398)

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/generic_signature_set.rs:19`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/generic_signature_set.rs#L19) Cow aggregate signature, borrowed
- [`crypto/bls/src/impls/blst.rs:36-39`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L36-L39) verify_signature_sets takes an iterator of &amp;SignatureSet and collects refs
- [`beacon_node/beacon_chain/src/attestation_verification/batch.rs:109`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification/batch.rs#L109) signature sets built from borrowed data

**Skeptic check.** Prysm removed a SignatureBatch.Copy() before handing the set to its verifier goroutine; Lighthouse passes references through verify_signature_sets and never clones the batch. Earlier verdict is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#16398](https://github.com/OffchainLabs/prysm/pull/16398)

</details>


<a id="gossip_validation-137"></a>
<details>
<summary><b>gossip_validation-137</b> Backoff retries of queued blocks — <i>n/a · low · S · cpu</i></summary>

**Idea.** Back off retries of queued gossip blocks failing on execution status instead of retrying every tick.

**Impact.** Lighthouse has no per-tick retry of queued gossip blocks; failures on execution status are ignored and recovered via lookups, so there is nothing to back off.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1756-1760`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1756-L1760) EL-status block errors are just Ignored, not queued
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:802-826`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L802-L826) RPC block delay queue is a single fixed 4s delay, no tick retry loop
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:67`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L67) QUEUED_RPC_BLOCK_DELAY

**Sources.** [caplin#23646](https://github.com/erigontech/erigon/pull/23646)

</details>


<a id="gossip_validation-138"></a>
<details>
<summary><b>gossip_validation-138</b> Serialize decoding of large gossip messages — <i>n/a · low · S · cpu, memory</i></summary>

**Idea.** Take the block-validation lock before decoding gossiped blocks/envelopes so only one large SSZ decode runs at a time.

**Impact.** Gossip decode runs on the single network service task, so large decodes are already serialized by construction; no concurrent decode memory spike as in Prysm's goroutines.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/mod.rs:1390`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L1390) PubsubMessage::decode called inline in the single network service poll loop
- [`beacon_node/lighthouse_network/src/types/pubsub.rs:266`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L266) block decode

**Sources.** [prysm#17647](https://github.com/OffchainLabs/prysm/pull/17647)

</details>


<a id="gossip_validation-139"></a>
<details>
<summary><b>gossip_validation-139</b> Shallow validation before propagation — <i>implemented · high · S · bandwidth, cpu, latency</i></summary>

**Idea.** Split gossip verification into a cheap propagation check with seen caches, then later pool and fork choice import, so forwarding is fast.

**Impact.** Already done: gossip verification with seen caches gates propagation; fork choice, op pool and block/column import run after Accept.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:416-420`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L416-L420) propagate_attestation_if_timely before fork choice/pool import
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:432-460`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L432-L460) apply_attestation_to_fork_choice and add_to_naive_aggregation_pool after propagation
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1661`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1661) block MessageAcceptance::Accept right after gossip verification, before import
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:728`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L728) data column Accept before process_gossip_verified_data_column

**Skeptic check.** Confirmed on attestations, blocks and data columns: Accept is sent after the cheap gossip checks and before the import work. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#608](https://github.com/sigp/lighthouse/pull/608), [lighthouse#983](https://github.com/sigp/lighthouse/pull/983)

</details>


<a id="gossip_validation-140"></a>
<details>
<summary><b>gossip_validation-140</b> Shorter batch signature verification deadline — <i>implemented · low · S · latency</i></summary>

**Idea.** Cut the max wait of the gossip attestation batch verifier so batches start sooner.

**Impact.** There is no batch deadline: a worker takes the queued items at once, so the idea's latency cost does not exist in Lighthouse.

**Best measured result.** None (pr:prysm#15882)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:961-1010`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L961-L1010) aggregate batch formed from whatever is queued, no wait
- [`beacon_node/beacon_processor/src/lib.rs:1015-1030`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1015-L1030) attestation batch formed the same way
- [`beacon_node/beacon_processor/src/lib.rs:110-111`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L110-L111) max batch 64

**Skeptic check.** Confirmed batching is opportunistic: when a worker is free it drains up to 64 queued items, or processes a single item on its own. Earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#15882](https://github.com/OffchainLabs/prysm/pull/15882), [prysm#15901](https://github.com/OffchainLabs/prysm/pull/15901)

</details>


<a id="gossip_validation-141"></a>
<details>
<summary><b>gossip_validation-141</b> Do not feed aggregate contents to fork choice — <i>n/a · low · S · cpu</i></summary>

**Idea.** Store gossip aggregates only in the pool and do not push their attestations through the per-attestation chain/fork choice path.

**Impact.** Skipping would drop LMD votes from subnets the node is not subscribed to, making fork choice less accurate; the per-aggregate on_attestation cost is small and queued, so not worth removing.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:631`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L631) aggregates applied to fork choice
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2573`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2573) apply_attestation_to_fork_choice

**Sources.** [lodestar@4728d52a0](https://github.com/ChainSafe/lodestar/commit/4728d52a0f57)

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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [caplin#18521](https://github.com/erigontech/erigon/pull/18521), [caplin#18524](https://github.com/erigontech/erigon/pull/18524)

</details>


<a id="gossip_validation-143"></a>
<details>
<summary><b>gossip_validation-143</b> Committee index via accessor, no version checks — <i>implemented · low · S · cpu</i></summary>

**Idea.** Get the committee index through the attestation type accessor when computing the subnet instead of fork version checks and bit scans.

**Impact.** No fork-version checks; the hot SingleAttestation path is a field read.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/attestation/subnet_id.rs:53-66`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/attestation/subnet_id.rs#L53-L66) compute_subnet_for_attestation uses AttestationRef::committee_index()
- [`consensus/types/src/attestation/subnet_id.rs:70-81`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/attestation/subnet_id.rs#L70-L81) compute_subnet_for_single_attestation reads SingleAttestation.committee_index field
- [`consensus/types/src/attestation/attestation.rs:360-366`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/attestation/attestation.rs#L360-L366) accessor matches on variant; Electra variant uses find() on committee_bits with early exit (attestation.rs:383-389)

**Skeptic check.** Prysm #15116 only replaced a version branch with GetCommitteeIndex(), which still scans bits for Electra aggregates. LH has the same shape, and its Electra scan exits early. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#15116](https://github.com/OffchainLabs/prysm/pull/15116)

</details>


<a id="gossip_validation-144"></a>
<details>
<summary><b>gossip_validation-144</b> Single decode-and-validate handler per topic — <i>n/a · low · S · cpu, latency</i></summary>

**Idea.** Use one generic gossip handler that decodes and validates in a single pass per topic.

**Impact.** Go handler-structure refactor; Lighthouse already decodes once per message and dispatches to a per-topic verify function with no redundant passes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/pubsub.rs:195`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L195) single decode function per topic
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs) one process_gossip_* per topic

**Sources.** [caplin#6614](https://github.com/erigontech/erigon/pull/6614)

</details>


<a id="gossip_validation-145"></a>
<details>
<summary><b>gossip_validation-145</b> Route gossip envelopes straight to fork choice — <i>n/a · low · latency</i></summary>

**Idea.** Send a gossip-received execution payload envelope directly to fork choice import instead of through an extra sync service queue hop.

**Impact.** LH has no intermediate sync-service hop for gossip envelopes; they go straight to the beacon processor.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/mod.rs:465`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L465) gossip envelope queued directly as Work::GossipExecutionPayload

**Sources.** [grandine@5e939e582](https://github.com/grandinetech/grandine/commit/5e939e58247b)

</details>


<a id="gossip_validation-146"></a>
<details>
<summary><b>gossip_validation-146</b> Validate sidecars before caching — <i>implemented · low · S · cpu</i></summary>

**Idea.** Validate a gossip data column sidecar before adding it to the block input cache so invalid ones do no downstream work.

**Impact.** Invalid gossip sidecars are rejected before they reach the DA checker or the block input cache.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:711-714`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L711-L714) verify_data_column_sidecar_for_gossip before any cache insert
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1139-1210`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1139-L1210) validate_data_column_sidecar_for_gossip_fulu: structural, subnet, slot, inclusion proof, proposer signature and KZG checks; the DA cache is only read (missing_cells_for_column_sidecar)
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1310-1340`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1310-L1340) partial columns also verify the header before use

**Skeptic check.** Verified that the gossip path only reads the DA cache before full validation, and only GossipVerifiedDataColumn is inserted. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#7955](https://github.com/ChainSafe/lodestar/pull/7955)

</details>


<a id="gossip_validation-147"></a>
<details>
<summary><b>gossip_validation-147</b> Derive prev_randao from block data, no state replay — <i>implemented · low · S · cpu, latency, disk</i></summary>

**Idea.** Obtain the expected prev_randao for a parent block from that block's randao_reveal hash XOR its execution prev_randao instead of loading or replaying a state, and use it as a cheap bid-validation check. Check whether gossip bid validation replays or loads a state to learn prev_randao.

**Impact.** Bid prev_randao check reads the randao from the cached head snapshot (head state mix, or latest_execution_payload_bid.prev_randao for the parent); no state load or replay.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/payload_bid_verification/gossip_verified_bid.rs:426-446`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_bid_verification/gossip_verified_bid.rs#L426-L446)
- [`beacon_node/beacon_chain/src/canonical_head.rs:346-372`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L346-L372)

**Skeptic check.** Verified: the bid check picks head_random() or parent_random() from cached_head after is_bid_compatible_with_head, which limits parents to head or head's parent. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#8592](https://github.com/status-im/nimbus-eth2/pull/8592), [nimbus#8609](https://github.com/status-im/nimbus-eth2/pull/8609)

</details>


<a id="gossip_validation-148"></a>
<details>
<summary><b>gossip_validation-148</b> Publish each light client update only once — <i>implemented · low · S · bandwidth, cpu</i></summary>

**Idea.** Track the latest broadcast light client finality and optimistic update and gossip each only once, so repeated triggers do not re-publish or re-validate the same update.

**Impact.** Each LC finality/optimistic update is gossiped once; light-client-server nodes only.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/light_client_server_cache.rs:39-41`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_server_cache.rs#L39-L41)
- [`beacon_node/beacon_chain/src/light_client_server_cache.rs:305-321`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_server_cache.rs#L305-L321)
- [`beacon_node/http_api/src/sync_committees.rs:323`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/sync_committees.rs#L323)
- [`beacon_node/http_api/src/sync_committees.rs:339`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/sync_committees.rs#L339)

**Skeptic check.** This idea is Lighthouse's own PR #7023. The should_broadcast_* functions compare against the last broadcast update, and the http_api publish path uses them.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#7023](https://github.com/sigp/lighthouse/pull/7023)

</details>


<a id="gossip_validation-149"></a>
<details>
<summary><b>gossip_validation-149</b> No event-bus emission on gossip block hot path — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Do not emit a per-block event from the gossip block handler on the validation path; defer it or make it cheap.

**Impact.** Nothing to gain; the event is emitted only when there are block_gossip subscribers, and its payload is a slot and a root.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1117-1125`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1117-L1125)

**Skeptic check.** Verified: the has_block_gossip_subscribers() guard is on the gossip verification path. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus@ebbad2a44](https://github.com/status-im/nimbus-eth2/commit/ebbad2a44927)

</details>


<a id="gossip_validation-150"></a>
<details>
<summary><b>gossip_validation-150</b> Inclusion proof replaces per-sidecar proposer signature — <i>partial · medium · S · cpu, bandwidth</i></summary>

**Idea.** Carry a Merkle inclusion proof of the KZG commitment in blob sidecars so gossip validation checks a hash path instead of a proposer BLS signature per sidecar.

**Gap in Lighthouse.** The inclusion-proof sidecar format (spec #3531) is implemented. But validate_data_column_sidecar_for_gossip_fulu calls verify_proposer_and_signature for every column sidecar, and that function does a full BLS verify of signed_block_header each time. No cache keyed by header root records that a header's signature was already verified, so N custody columns of one block cost N identical proposer-signature verifications. The fix: keep a small header_root -&gt; verified cache (or reuse the block's verified signature) and skip the BLS verify on a hit.

**Impact.** Up to 128 redundant BLS verifies per slot on a supernode (8+ on a normal node), about 1ms CPU each, on the gossip column path. Pre-Gloas only: Gloas columns carry no header.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_column_verification.rs:1139-1206`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1139-L1206)
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1676`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1676)
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1732-1791`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1732-L1791)
- [`beacon_node/beacon_chain/src/data_column_verification.rs:654`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L654)

**Skeptic check.** The earlier evidence was right that the inclusion-proof format is implemented. It missed that the proposer header signature is still checked once per sidecar with no memoization, so the effect the idea describes (one hash path per sidecar instead of one BLS verify per sidecar) is not reached.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lodestar#6089](https://github.com/ChainSafe/lodestar/pull/6089)

</details>


<a id="gossip_validation-151"></a>
<details>
<summary><b>gossip_validation-151</b> Iterate sync subcommittee without copying pubkeys — <i>not · low · S · memory, cpu</i></summary>

**Idea.** Iterate the sync subcommittee as a slice or iterator over the full sync committee pubkey array rather than copying it into a new vector on each sync message validation, avoiding an allocation per message.

**Gap in Lighthouse.** get_subcommittee_pubkeys could return &amp;[PublicKeyBytes] (sync_committee_verification.rs:318 borrows the Arc'd committee) and the participant filter could iterate the slice. subcommittee_positions_for_public_key could use a pubkey-to-index cache or avoid the HashMap.

**Impact.** Saves a ~6KB copy per sync contribution (about 64 per slot) and a HashMap allocation per sync message (about 512 per slot); a few microseconds each, negligible overall.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/sync_committee/sync_committee.rs:52-67`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/sync_committee/sync_committee.rs#L52-L67) get_subcommittee_pubkeys does s.to_vec() (128 x 48B)
- [`beacon_node/beacon_chain/src/sync_committee_verification.rs:318-322`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/sync_committee_verification.rs#L318-L322),373 contribution path uses the copy
- [`consensus/types/src/sync_committee/sync_committee.rs:72-88`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/sync_committee/sync_committee.rs#L72-L88) message path scans 512 pubkeys and allocates a HashMap per message

**Sources.** [nimbus#2965](https://github.com/status-im/nimbus-eth2/pull/2965)

</details>


<a id="gossip_validation-152"></a>
<details>
<summary><b>gossip_validation-152</b> Precompute subnet stability offset once — <i>implemented · low · S · cpu</i></summary>

**Idea.** Compute the per-node stability-subnet offset once at init in machine-word integers so recurring subnet computation avoids 256-bit division or modulo.

**Impact.** The computation runs once at SubnetService init; the U256 work is a single shift. No recurring cost.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/attestation/subnet_id.rs:104-128`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/attestation/subnet_id.rs#L104-L128)
- [`beacon_node/network/src/subnet_service/mod.rs:137`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L137)

**Skeptic check.** Verified: the only non-test caller is SubnetService init, and the results are used as permanent subscriptions. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#8943](https://github.com/status-im/nimbus-eth2/pull/8943)

</details>


<a id="gossip_validation-153"></a>
<details>
<summary><b>gossip_validation-153</b> Verify single attestation signature before committee lookup — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** For unaggregated attestations that carry the attester index, verify the BLS signature before computing or fetching the committee shuffling, so invalid or spam attestations are rejected without shuffling cost.

**Impact.** Invalid single attestations are rejected at signature verification, before the with_committee_cache shuffling lookup in verify_late_checks.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:902-1008`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L902-L1008)
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1026-1053`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1026-L1053)
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1066-1110`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1066-L1110)
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1168-1200`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1168-L1200)

**Skeptic check.** Verified: the early and middle checks do no committee lookup, to_indexed uses attester_index directly, and the signature is checked before verify_late_checks does the committee and subnet lookups. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#8676](https://github.com/Consensys-Incorporated/teku/pull/8676)

</details>


<a id="gossip_validation-154"></a>
<details>
<summary><b>gossip_validation-154</b> Single regex to map gossip topic to subnet — <i>implemented · low · S · cpu</i></summary>

**Idea.** Match an attestation subnet topic with one precompiled regex and parse the subnet index from a capture group, instead of building and comparing the topic string for each of the 64 subnets per message.

**Impact.** Topic decode is a single pass: split, match, then strip_prefix and parse. There is no per-subnet string building, only one small Vec and a 4-byte hex decode per call.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/topics.rs:265-305`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/topics.rs#L265-L305)
- [`beacon_node/lighthouse_network/src/types/topics.rs:398-413`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/topics.rs#L398-L413)

**Skeptic check.** Verified: subnet_topic_index parses the index from the prefix-stripped name. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@f756dcb3f](https://github.com/ChainSafe/lodestar/commit/f756dcb3f310)

</details>


<a id="gossip_validation-155"></a>
<details>
<summary><b>gossip_validation-155</b> Skip hash tree root computed only for logging — <i>implemented · low · S · cpu</i></summary>

**Idea.** Do not compute hash tree root of attestations or aggregates for log context on every gossip message; log it only on error paths.

**Impact.** No hash tree root is computed only for logging on the success path. The two logging roots sit in slasher error branches, and tracing evaluates them lazily.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:455-479`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L455-L479)
- [`beacon_node/beacon_chain/src/attestation_verification.rs:562`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L562)

**Skeptic check.** Verified: the root at line 562 is the aggregate dedup key, and gossip_methods.rs computes no tree_hash_root or canonical_root for logging. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#2202](https://github.com/ChainSafe/lodestar/pull/2202)

</details>


<a id="gossip_validation-156"></a>
<details>
<summary><b>gossip_validation-156</b> Validate light client gossip against local update, no storage — <i>implemented · low · S · cpu, memory, disk</i></summary>

**Idea.** Validate gossiped light client updates by comparing with the locally computed update without storing received ones, and exit early when no local update exists to compare.

**Impact.** None left; gossiped updates are validated by comparison with the local one and not stored beyond one dedup clone.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/light_client_finality_update_verification.rs:105-108`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_finality_update_verification.rs#L105-L108) get_latest_finality_update().ok_or(FailedConstructingUpdate) exits early with no local update
- [`beacon_node/beacon_chain/src/light_client_finality_update_verification.rs:119-155`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_finality_update_verification.rs#L119-L155) equality comparison against the locally built update
- [`beacon_node/beacon_chain/src/light_client_finality_update_verification.rs:157-159`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_finality_update_verification.rs#L157-L159) only stores the accepted update as the latest-broadcasted dedup marker
- [`beacon_node/beacon_chain/src/light_client_optimistic_update_verification.rs:112-113`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_optimistic_update_verification.rs#L112-L113),152 same pattern for optimistic updates

**Skeptic check.** Confirmed both finality and optimistic verification compare with the local cache update, exit early when none exists, and keep only the last broadcast copy. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#15783](https://github.com/OffchainLabs/prysm/pull/15783)

</details>


<a id="gossip_validation-157"></a>
<details>
<summary><b>gossip_validation-157</b> Reject subscriptions to unknown gossip topics — <i>implemented · low · S · bandwidth, memory</i></summary>

**Idea.** Keep a precomputed set of valid topics and reject peer subscriptions to any other topic, so the router tracks no mesh state and forwards no traffic for arbitrary topics.

**Impact.** Peer subscriptions to unknown topics are dropped, so no mesh or forwarding state is kept for them.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/mod.rs:332`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L332) MaxCountSubscriptionFilter over a whitelist
- [`beacon_node/lighthouse_network/src/service/utils.rs:268-300`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/utils.rs#L268-L300) create_whitelist_filter precomputes topic hashes for all fork digests
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/behaviour.rs:2111 filter_incoming_subscriptions applied before peer topic state is updated
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/subscription_filter.rs:102-130 whitelist and max-count filters

**Skeptic check.** Verified the whitelist hash set is built at startup and the gossipsub behaviour filters incoming subscriptions through it. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#2237](https://github.com/status-im/nimbus-eth2/pull/2237)

</details>


