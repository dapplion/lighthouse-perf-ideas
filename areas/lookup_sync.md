# lookup_sync

56 ideas: 11 not, 14 partial, 25 implemented, 6 n/a; 7 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [lookup_sync-001](#lookup_sync-001) **★** | Prune pending lookup queue at finalization | partial | medium | S | memory, bandwidth, sync |
| [lookup_sync-002](#lookup_sync-002) | Expire pending blocks and lookups by age | implemented | medium | S | memory, sync |
| [lookup_sync-003](#lookup_sync-003) **★** | Exponential backoff for failing by-root roots | partial | medium | S | bandwidth, cpu, sync |
| [lookup_sync-004](#lookup_sync-004) | Attestations for unknown root trigger block lookup | implemented | medium | S | latency, sync |
| [lookup_sync-005](#lookup_sync-005) | Event-driven unknown-parent lookup, not timer tick | implemented | low | S | latency |
| [lookup_sync-006](#lookup_sync-006) | Request unknown block from peers that announced it | implemented | medium | S | sync, latency, bandwidth |
| [lookup_sync-007](#lookup_sync-007) | Keep failed or peerless lookups instead of dropping | partial | low | M | bandwidth, sync |
| [lookup_sync-008](#lookup_sync-008) | Lookup peer set only peers able to serve | implemented | low | S | bandwidth |
| [lookup_sync-009](#lookup_sync-009) | One in-flight lookup per block root | implemented | low | S | bandwidth, cpu, sync |
| [lookup_sync-010](#lookup_sync-010) | Skip lookup if block already received or processing | partial | low | S | bandwidth, cpu, sync |
| [lookup_sync-011](#lookup_sync-011) | Request deepest missing ancestor directly | implemented | medium | S | sync, latency, bandwidth |
| [lookup_sync-012](#lookup_sync-012) | Serve lookups from locally stored orphan blocks | not | low | M | sync, bandwidth |
| [lookup_sync-013](#lookup_sync-013) **★** | Remember invalid and unviable blocks and forks | partial | medium | S | bandwidth, cpu, sync |
| [lookup_sync-014](#lookup_sync-014) | Cache pre-finalization block roots | implemented | low | S | disk, bandwidth, cpu |
| [lookup_sync-015](#lookup_sync-015) | Verify downloaded block before retaining in lookup cache | not | low | M | memory, bandwidth |
| [lookup_sync-016](#lookup_sync-016) | Stop processing pending block once found invalid | implemented | low | S | cpu |
| [lookup_sync-017](#lookup_sync-017) | Cap number of concurrent lookups | implemented | low | S | memory |
| [lookup_sync-018](#lookup_sync-018) | Bound lookup child-peer map size | not | low | S | memory |
| [lookup_sync-019](#lookup_sync-019) | Slot-window caps on by-root payload envelopes | n/a | low |  | memory |
| [lookup_sync-020](#lookup_sync-020) **★** | Store pending unknown-parent blocks on disk | not | medium | L | memory |
| [lookup_sync-021](#lookup_sync-021) **★** | Header-only backward chain tracking for unknown chains | partial | medium | L | memory, sync |
| [lookup_sync-022](#lookup_sync-022) | Stop parent-chain lookup at finalized slot | implemented | low | S | bandwidth, sync |
| [lookup_sync-023](#lookup_sync-023) | Slot-distance bound on unknown-parent lookups | implemented | low | S | bandwidth, sync, cpu |
| [lookup_sync-024](#lookup_sync-024) | No unknown-parent lookups while range syncing | implemented | low | S | memory, bandwidth, sync |
| [lookup_sync-025](#lookup_sync-025) | Start parent lookup only after gossip validation | implemented | low | S | cpu, sync |
| [lookup_sync-026](#lookup_sync-026) | Batch column by-root requests per peer | partial | low | M | bandwidth, sync |
| [lookup_sync-027](#lookup_sync-027) **★** | Custody-overlap peer selection for column requests | partial | medium | S | bandwidth, sync, latency |
| [lookup_sync-028](#lookup_sync-028) | Filter column peers by earliest available slot | implemented | low | S | bandwidth, sync |
| [lookup_sync-029](#lookup_sync-029) | Balance lookup requests by active requests per peer | partial | low | S | sync, bandwidth |
| [lookup_sync-030](#lookup_sync-030) | Skip column requests for blocks without blobs | implemented | low | S | bandwidth, cpu |
| [lookup_sync-031](#lookup_sync-031) | Drop roots with empty column list from request | n/a | low |  | bandwidth, sync |
| [lookup_sync-032](#lookup_sync-032) | Dedupe column indices in by-root request | implemented | low | S | bandwidth |
| [lookup_sync-033](#lookup_sync-033) | Cap blocks per by-root columns request | n/a | low |  | bandwidth, sync |
| [lookup_sync-034](#lookup_sync-034) | Exclude already-stored blobs from by-root request | implemented | low | S | bandwidth |
| [lookup_sync-035](#lookup_sync-035) **★** | Time column fetching relative to gossip arrival | not | medium | S | latency, bandwidth |
| [lookup_sync-036](#lookup_sync-036) | No column fetch at Gloas block import | partial | low | M | bandwidth, latency |
| [lookup_sync-037](#lookup_sync-037) | Request blobs only after block is downloaded | implemented | low | S | bandwidth, sync |
| [lookup_sync-038](#lookup_sync-038) | Key parent blob lookups by parent root | implemented | low | S | bandwidth, sync |
| [lookup_sync-039](#lookup_sync-039) | No EL getBlobs during by-root sync | not | low | S | cpu, latency |
| [lookup_sync-040](#lookup_sync-040) | Avoid retrying failed peers in lookups | implemented | low | S | bandwidth, sync |
| [lookup_sync-041](#lookup_sync-041) | Request missing payload envelope at payload deadline | not | low | M | latency, cpu, bandwidth |
| [lookup_sync-042](#lookup_sync-042) | Fetch payload envelopes on demand only | not | low | M | bandwidth, memory |
| [lookup_sync-043](#lookup_sync-043) | Request parent envelope in parallel with parent block | not | low | M | latency, sync |
| [lookup_sync-044](#lookup_sync-044) | Batched by-root requests to best-scored peers | partial | low | S | latency, sync |
| [lookup_sync-045](#lookup_sync-045) | Redundant parallel lookup requests to two peers | not | low | M | latency, sync |
| [lookup_sync-046](#lookup_sync-046) | Run parent lookups off the sync event loop | implemented | low | S | latency, sync |
| [lookup_sync-047](#lookup_sync-047) | Pass fetched block into blob validation | n/a | low |  | disk, latency |
| [lookup_sync-048](#lookup_sync-048) | Run cheap subset check first on by-root responses | partial | low | S | cpu |
| [lookup_sync-049](#lookup_sync-049) | Compute hash tree root outside pending-blocks lock | n/a | low |  | latency |
| [lookup_sync-050](#lookup_sync-050) | DAG of unknown blocks drives by-root lookups | partial | low | M | sync |
| [lookup_sync-051](#lookup_sync-051) | Debounce unknown-root attestation events per peer | implemented | low | S | cpu |
| [lookup_sync-052](#lookup_sync-052) | Do not start RPC lookups from partial gossip | partial | low | S | bandwidth, cpu |
| [lookup_sync-053](#lookup_sync-053) | Key pending blocks queue by root in hash map | n/a | low | S | cpu, sync |
| [lookup_sync-054](#lookup_sync-054) | Import RPC-received blocks without requeue delay | implemented | low | S | latency |
| [lookup_sync-055](#lookup_sync-055) | Skip envelope lookups for roots that cannot have one | implemented | low | S | bandwidth, sync |
| [lookup_sync-056](#lookup_sync-056) | No retry for deterministic block processing errors | not | low | S | cpu, bandwidth |

★ actionable. Click an id for the full record.

## Ideas

<a id="lookup_sync-001"></a>
<details>
<summary><b>lookup_sync-001</b> Prune pending lookup queue at finalization — <i>partial · medium · S · memory, bandwidth, sync</i></summary>

**Idea.** When finality advances, drop queued unknown-parent blocks and pending by-root roots (blocks or payloads) whose slot is at or below the finalized slot. This stops the node holding and re-requesting orphaned ancestors no peer will serve.

**Gap in Lighthouse.** No finalization hook into sync: lookups and pending unknown roots at or below the new finalized slot are only removed after their block is downloaded and fails processing, by the no-peers/stuck timers, or by TTL. Add a finalization notification that calls drop_lookup_and_children for lookups whose known slot &lt;= finalized slot (and drops pending roots not descending from finalized).

**Impact.** Frees a few held lookups and avoids some by-root requests for orphaned ancestors after finality; small on a healthy node.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/mod.rs:718`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L718) prune_lookups = drop_lookups_without_peers + drop_stuck_lookups only, no finality check
- [`beacon_node/network/src/sync/manager.rs:107`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L107) SyncMessage has no finalization/new-finalized-checkpoint event
- [`beacon_node/network/src/sync/manager.rs:1151`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L1151) should_search_for_block filters by head-slot distance only while not synced, not by finalized slot
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:1095`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L1095) WouldRevertFinalizedSlot/NotFinalizedDescendant only caught when a downloaded block is processed
- [`beacon_node/network/src/sync/manager.rs:1089`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L1089) prune_pending_unknown_roots is TTL only

**Second check.** Checked every SyncMessage variant, the prune interval path, should_search_for_block and the processing error mapping for any finality-driven pruning; none exists. Gossip blocks below finality are rejected before raising unknown-parent, which limits new entries but does not prune existing ones.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [teku#1082](https://github.com/Consensys-Incorporated/teku/pull/1082), [prysm#4066](https://github.com/OffchainLabs/prysm/pull/4066), [prysm#4168](https://github.com/OffchainLabs/prysm/pull/4168), [nimbus#9185](https://github.com/status-im/nimbus-eth2/pull/9185), [lodestar#9852](https://github.com/ChainSafe/lodestar/pull/9852)

</details>


<a id="lookup_sync-002"></a>
<details>
<summary><b>lookup_sync-002</b> Expire pending blocks and lookups by age — <i>implemented · medium · S · memory, sync</i></summary>

**Idea.** Give each pending unknown-parent block or lookup a maximum lifetime (TTL or max duration) and drop it, with its children, when it expires. This bounds the queue and frees state and peers held by stuck lookups.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/mod.rs:67`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L67)
- [`beacon_node/network/src/sync/block_lookups/mod.rs:742`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L742)
- [`beacon_node/network/src/sync/block_lookups/mod.rs:779`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L779)
- [`beacon_node/network/src/sync/block_lookups/mod.rs:616`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L616)

**Skeptic check.** Lookups older than 16 min (stuck) or without peers for 10 s are dropped with drop_lookup_and_children, pruned periodically from the sync manager. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#7816](https://github.com/OffchainLabs/prysm/pull/7816), [lighthouse#5824](https://github.com/sigp/lighthouse/pull/5824)

</details>


<a id="lookup_sync-003"></a>
<details>
<summary><b>lookup_sync-003</b> Exponential backoff for failing by-root roots — <i>partial · medium · S · bandwidth, cpu, sync</i></summary>

**Idea.** Track retry count and next-retry time per missing root in a bounded map, back off exponentially after failures and stop after a max count, servicing newest roots first. Stale unservable roots then stop consuming peer request slots every loop.

**Gap in Lighthouse.** Retries are count-capped, peer-deprioritized and event-driven (no polling loop), and re-triggers from attestations are throttled to once per (peer, root) per 30s plus corroboration. But there is no per-root memory of failure after a lookup is dropped and no exponential backoff, so an unservable root can be re-looked-up every ~30s per corroborating peer set. Add a bounded LRU of failed roots with attempt count and next-retry time checked in new_current_lookup.

**Impact.** Small: Lighthouse does not have the poll-every-loop pattern that produced ~170 req/s in Lodestar; saves occasional repeat by-root requests for dead roots.

**Best measured result.** Retry rate ~170 req/s from 82 stale roots; verified by unit tests only (pr:lodestar#9791)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/single_block_lookup.rs:917`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/single_block_lookup.rs#L917) failed_downloading capped at SINGLE_BLOCK_LOOKUP_MAX_ATTEMPTS=4
- [`beacon_node/network/src/sync/network_context.rs:721`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L721) peers that already failed the request are de-prioritized
- [`beacon_node/network/src/sync/manager.rs:922`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L922) notified_unknown_roots dedups (peer, root) for 30s (NOTIFIED_UNKNOWN_ROOT_EXPIRY_SECONDS, manager.rs:93)
- [`beacon_node/network/src/sync/manager.rs:1059`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L1059) record_unknown_root requires unknown_root_min_peers distinct peers before a new lookup

**Second check.** Beyond the earlier review, found the 30s per-(peer,root) notification cache, the multi-peer corroboration gate and failed-peer deprioritization, which together act as a fixed-interval throttle but not a per-root exponential backoff.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [nimbus#8372](https://github.com/status-im/nimbus-eth2/pull/8372), [lodestar#9791](https://github.com/ChainSafe/lodestar/pull/9791)

</details>


<a id="lookup_sync-004"></a>
<details>
<summary><b>lookup_sync-004</b> Attestations for unknown root trigger block lookup — <i>implemented · medium · S · latency, sync</i></summary>

**Idea.** When a gossip attestation references an unknown block root, start a by-root block request at once instead of waiting for the gossip block, since attestations often arrive first.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:2874-2886`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L2874-L2886)
- [`beacon_node/network/src/sync/manager.rs:921`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L921)
- [`beacon_node/network/src/sync/manager.rs:1036-1057`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L1036-L1057)
- [`beacon_node/lighthouse_network/src/config.rs:25`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L25)

**Skeptic check.** UnknownHeadBlock attestations send UnknownBlockHashFromAttestation and are queued for reprocessing; sync starts search_unknown_block. One nuance: record_unknown_root waits for 3 distinct peers by default (anti-DoS), which is normally met within a fraction of a slot. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#5485](https://github.com/ChainSafe/lodestar/pull/5485)

</details>


<a id="lookup_sync-005"></a>
<details>
<summary><b>lookup_sync-005</b> Event-driven unknown-parent lookup, not timer tick — <i>implemented · low · S · latency</i></summary>

**Idea.** When a gossip block has an unknown parent, or a parent's payload arrives, request or drain the pending queue immediately instead of waiting for the next periodic tick (up to a third of a slot).

**Impact.** Unknown-parent requests and child processing are driven by events, with no tick latency.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/manager.rs:1000-1032`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L1000-L1032) handle_unknown_parent calls search_child_and_parent at once
- [`beacon_node/network/src/sync/block_lookups/mod.rs:178-210`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L178-L210),452 new lookups call continue_requests immediately
- [`beacon_node/network/src/sync/block_lookups/mod.rs:545-551`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L545-L551),586-610,684 continue_child_lookups on parent import (LookupComplete / OnlyGloasBlock)
- [`beacon_node/network/src/sync/block_lookups/mod.rs:719-722`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L719-L722) prune_lookups only drops peerless/stuck lookups

**Skeptic check.** Verified the parent request is sent on lookup creation and children resume on parent import; the timer only prunes. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#16749](https://github.com/OffchainLabs/prysm/pull/16749), [prysm#17057](https://github.com/OffchainLabs/prysm/pull/17057)

</details>


<a id="lookup_sync-006"></a>
<details>
<summary><b>lookup_sync-006</b> Request unknown block from peers that announced it — <i>implemented · medium · S · sync, latency, bandwidth</i></summary>

**Idea.** Record which peers sent attestations or blocks referencing each unknown root and request the block from those peers first, deduped per (root, peer). Those peers are the ones most likely to have it.

**Impact.** Requests go to peers that attested/sent the root; no further gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/manager.rs:1036`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L1036) handle_unknown_block_root collects reporting peers via record_unknown_root
- [`beacon_node/network/src/sync/manager.rs:921`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L921) per-(peer,root) dedup notified_unknown_roots
- [`beacon_node/network/src/sync/block_lookups/mod.rs:374`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L374) existing lookup gains peers via add_peers_to_lookup_and_ancestors
- [`beacon_node/network/src/sync/network_context.rs:708`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L708) block_lookup_request picks the peer only from lookup_peers

**Skeptic check.** Verified: reporting peers are recorded per root, deduped per (peer,root), stored in the lookup peer set, and block/column requests pick from that set. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#17754](https://github.com/OffchainLabs/prysm/pull/17754), [lodestar#9928](https://github.com/ChainSafe/lodestar/pull/9928)

</details>


<a id="lookup_sync-007"></a>
<details>
<summary><b>lookup_sync-007</b> Keep failed or peerless lookups instead of dropping — <i>partial · low · M · bandwidth, sync</i></summary>

**Idea.** Do not delete a lookup when its download fails or it has no peers; return it to pending until it is idle and a timeout passes. Downloaded components and accumulated peers survive, so the next retry does not start from zero.

**Gap in Lighthouse.** Peerless lookups are retained (PR #5839), but a lookup whose download fails SINGLE_BLOCK_LOOKUP_MAX_ATTEMPTS times returns TooManyAttempts and on_lookup_result calls drop_lookup_and_children. This throws away the lookup's peers and the downloaded components of all child lookups, which Lodestar #10137 avoids by resetting to pending until a time-based prune. LH could reset failed_downloading/failed_peers and leave the lookup in AwaitingDownload, and let drop_stuck_lookups/no-peer pruning remove it.

**Impact.** Avoids re-downloading child components and re-collecting peers after transient download failures near the head; rare in practice.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/single_block_lookup.rs:844-852`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/single_block_lookup.rs#L844-L852) no peers -&gt; LookupRequestResult::Pending, lookup kept
- [`beacon_node/network/src/sync/block_lookups/mod.rs:742-763`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L742-L763) peerless lookups dropped only after LOOKUP_MAX_DURATION_NO_PEERS_SECS
- [`beacon_node/network/src/sync/block_lookups/single_block_lookup.rs:906-923`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/single_block_lookup.rs#L906-L923) on_download_failure -&gt; TooManyAttempts after SINGLE_BLOCK_LOOKUP_MAX_ATTEMPTS
- [`beacon_node/network/src/sync/block_lookups/mod.rs:695-700`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L695-L700),613-636 Err -&gt; drop_lookup_and_children

**Skeptic check.** The no-peer half is fully implemented as cited; the download-failure half of the idea is not, since LH drops after 4 failed attempts together with its children. The earlier note called this intentional.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lighthouse#5839](https://github.com/sigp/lighthouse/pull/5839), [lodestar#10137](https://github.com/ChainSafe/lodestar/pull/10137)

</details>


<a id="lookup_sync-008"></a>
<details>
<summary><b>lookup_sync-008</b> Lookup peer set only peers able to serve — <i>implemented · low · S · bandwidth</i></summary>

**Idea.** Add a peer to a block lookup only if it must have the block's components (it sent the block or attested to it), not a peer that merely announced a descendant. Requests then do not go to peers that lack the data.

**Impact.** Lookup requests go only to peers that must hold the data.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/mod.rs:186-206`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L186-L206) child lookup created with zero peers; the sending peer is added only to the parent
- [`beacon_node/network/src/sync/block_lookups/mod.rs:841-880`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L841-L880) add_peers_to_lookup_and_ancestors adds peers only to the lookup and its ancestors
- [`beacon_node/network/src/sync/manager.rs:452`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L452),924,1036-1056 other peer sources are attestations and a status head the peer claims

**Skeptic check.** Verified every peer source (sender of a child -&gt; parent and ancestors, attesters, status head) implies the peer has the block; earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#5724](https://github.com/sigp/lighthouse/pull/5724)

</details>


<a id="lookup_sync-009"></a>
<details>
<summary><b>lookup_sync-009</b> One in-flight lookup per block root — <i>implemented · low · S · bandwidth, cpu, sync</i></summary>

**Idea.** Keep a set or state machine of in-flight lookups keyed by block root and skip creating another request for a root already being fetched or already queued (including delayed lookups and parent/child lookups). This removes duplicate concurrent downloads and processing of the same block.

**Impact.** Duplicate concurrent lookups per root are already impossible.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/mod.rs:374`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L374) new_current_lookup returns existing lookup for the root and only merges peers/components
- [`beacon_node/network/src/sync/block_lookups/mod.rs:178`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L178) search_child_and_parent and search_parent_of_child go through new_current_lookup
- [`beacon_node/network/src/sync/manager.rs:1043`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L1043) has_lookup_for_block short-circuit

**Skeptic check.** Every lookup creation path (unknown root, child, parent, payload envelope) goes through new_current_lookup which dedups by root; per-component request state machines allow one in-flight request each. Earlier verdict upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@8e3b3c5fd](https://github.com/ChainSafe/lodestar/commit/8e3b3c5fd4bb), [lodestar#1699](https://github.com/ChainSafe/lodestar/pull/1699), [prysm#12903](https://github.com/OffchainLabs/prysm/pull/12903), [prysm#13013](https://github.com/OffchainLabs/prysm/pull/13013), [lighthouse#5655](https://github.com/sigp/lighthouse/pull/5655), [nimbus#5167](https://github.com/status-im/nimbus-eth2/pull/5167), [lighthouse#4668](https://github.com/sigp/lighthouse/pull/4668), [prysm#17353](https://github.com/OffchainLabs/prysm/pull/17353), [lodestar#10347](https://github.com/ChainSafe/lodestar/pull/10347), [teku#10394](https://github.com/Consensys-Incorporated/teku/pull/10394)

</details>


<a id="lookup_sync-010"></a>
<details>
<summary><b>lookup_sync-010</b> Skip lookup if block already received or processing — <i>partial · low · S · bandwidth, cpu, sync</i></summary>

**Idea.** Before issuing a by-root request, check gossip-seen caches, the pre-import and data-availability caches, fork choice and recently completed lookups, and skip or suppress the lookup if the block is already there. Gossip-delivered blocks are then not downloaded again via RPC once per attestation.

**Gap in Lighthouse.** block_lookup_request deliberately re-downloads when get_block_process_status returns NotValidated (gossip block in execution), and handle_unknown_block_root / the gossip UnknownHeadBlock path never consult the gossip seen-block cache for blocks still in gossip verification; only ExecutionValidated (DA-pending) blocks are skipped. Lighthouse dedups processing, not the download.

**Impact.** Saves one by-root block download per root when attestations or columns arrive while the gossip block is still executing; reduced already by the 3-peer corroboration in record_unknown_root.

**Best measured result.** Testing showed many more rpc_block than usual (no number) (pr:lighthouse#5681)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context.rs:753`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L753) BlockProcessStatus::NotValidated(..) =&gt; {} re-downloads a block that is already in the DA cache pre-execution
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1390`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1390) get_block_process_status only consults DA checker and pending_payload_cache
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:2883`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L2883) attestation UnknownHeadBlock sends lookup without checking a gossip-seen/in-verification block
- [`beacon_node/network/src/sync/network_context.rs:708`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L708) ExecutionValidated is skipped (NoRequestNeeded)

**Skeptic check.** The DA-pending and fork-choice cases are covered, but the code comment at network_context.rs:745 states the block is eagerly re-downloaded while it is processing; the earlier verdict missed this NotValidated branch.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [prysm#16468](https://github.com/OffchainLabs/prysm/pull/16468), [lighthouse#5681](https://github.com/sigp/lighthouse/pull/5681), [lodestar#6292](https://github.com/ChainSafe/lodestar/pull/6292), [lighthouse#5682](https://github.com/sigp/lighthouse/pull/5682), [lighthouse#5840](https://github.com/sigp/lighthouse/pull/5840), [lighthouse#5722](https://github.com/sigp/lighthouse/pull/5722), [lighthouse#4732](https://github.com/sigp/lighthouse/pull/4732), [teku#7134](https://github.com/Consensys-Incorporated/teku/pull/7134), [prysm#9904](https://github.com/OffchainLabs/prysm/pull/9904), [lighthouse#5696](https://github.com/sigp/lighthouse/pull/5696), [prysm#4527](https://github.com/OffchainLabs/prysm/pull/4527)

</details>


<a id="lookup_sync-011"></a>
<details>
<summary><b>lookup_sync-011</b> Request deepest missing ancestor directly — <i>implemented · medium · S · sync, latency, bandwidth</i></summary>

**Idea.** When a block's parent is unknown, walk the locally held pending/queued blocks to the oldest missing ancestor and request only that root (processing queued parents first). This ends a parent-chain search in far fewer round trips than re-walking one block at a time.

**Impact.** Held ancestors are never re-requested; only the oldest missing root downloads.

**Best measured result.** "we found the previous block search never ended, so we sped it up" (pr:ethlambda#114)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/mod.rs:374`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L374) new_current_lookup reuses the existing lookup for an ancestor root instead of re-walking
- [`beacon_node/network/src/sync/block_lookups/mod.rs:178`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L178) search_child_and_parent attaches the child to an existing parent chain
- [`beacon_node/network/src/sync/block_lookups/mod.rs:586`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L586) continue_child_lookups processes queued children after the parent imports

**Skeptic check.** Downloaded blocks are held in lookups awaiting parents; a new block whose parent chain is already tracked joins the chain and only the deepest missing root is requested. This matches the nimbus/lodestar fix (no re-download of held ancestors). Upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [ethlambda#114](https://github.com/lambdaclass/ethlambda/pull/114), [nimbus#6112](https://github.com/status-im/nimbus-eth2/pull/6112), [lodestar#2165](https://github.com/ChainSafe/lodestar/pull/2165), [lighthouse#429](https://github.com/sigp/lighthouse/pull/429)

</details>


<a id="lookup_sync-012"></a>
<details>
<summary><b>lookup_sync-012</b> Serve lookups from locally stored orphan blocks — <i>not · low · M · sync, bandwidth</i></summary>

**Idea.** On a block lookup, check the local database for blocks persisted from a previous run (orphans, quarantine) and use them instead of downloading again.

**Gap in Lighthouse.** Lighthouse persists no orphan or quarantine blocks across restarts; adding one would need a new DB column and a check in new_current_lookup.

**Impact.** Would save re-downloading a few orphan blocks after restart; marginal.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/mod.rs:359-440`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L359-L440) new_current_lookup starts download without checking disk
- [`beacon_node/beacon_chain/src/pre_finalization_cache.rs:73`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pre_finalization_cache.rs#L73) store check only for finalized-block detection

**Sources.** [nimbus#6109](https://github.com/status-im/nimbus-eth2/pull/6109)

</details>


<a id="lookup_sync-013"></a>
<details>
<summary><b>lookup_sync-013</b> Remember invalid and unviable blocks and forks — <i>partial · medium · S · bandwidth, cpu, sync</i></summary>

**Idea.** Keep a cache of block roots and chains found invalid or unviable (failed lookups, bad parent) and refuse to look them up, request them or reprocess them again; remove them from missing tables and penalise peers that keep sending them.

**Gap in Lighthouse.** Only too-long lookup chains (60s), failed range chains (30s) and EL-invalid payloads (fork choice) are remembered. Blocks that fail consensus validation in a lookup (bad signature, state transition error, etc.) are retried up to 4 times, dropped with children, and not cached, so a later attestation/gossip can trigger the same download and verification. Insert penalty-bearing failed roots into a longer-lived lookup-side LRU and check it in new_current_lookup and search_parent_of_child.

**Impact.** Stops repeated download and verification of invalid forks from misbehaving peers; modest CPU/bandwidth saving.

**Best measured result.** 86 low-score disconnects in ~30 min before, 0 after; 580 penalized empty responses -&gt; 0 (pr:nimbus#9288)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/mod.rs:96`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L96) ignored_chains LRUTimeCache (from pr:lighthouse#1534), 60s expiry at mod.rs:61
- [`beacon_node/network/src/sync/block_lookups/mod.rs:282`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L282) ignored_chains only filled on chain-too-long
- [`beacon_node/network/src/sync/block_lookups/mod.rs:369`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L369) new_current_lookup refuses ignored roots
- [`beacon_node/network/src/sync/block_lookups/mod.rs:616`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L616) drop_lookup_and_children drops descendants of a failed lookup
- [`beacon_node/network/src/sync/range_sync/range.rs:352`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/range.rs#L352) range failed_chains cache, 30s
- [`beacon_node/beacon_chain/src/block_verification.rs:1512`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1512) ParentExecutionPayloadInvalid via fork choice remembers EL-invalid payloads
- [`beacon_node/beacon_chain/src/chain_config.rs:108`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/chain_config.rs#L108) invalid_block_roots is a static operator-supplied set only

**Second check.** Checked range sync failed_chains, fork choice invalid-payload tracking, the operator invalid_block_roots set and drop-with-children; none caches consensus-invalid roots for lookup sync.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [prysm#2297](https://github.com/OffchainLabs/prysm/pull/2297), [lighthouse#1534](https://github.com/sigp/lighthouse/pull/1534), [nimbus#3312](https://github.com/status-im/nimbus-eth2/pull/3312), [nimbus#3331](https://github.com/status-im/nimbus-eth2/pull/3331), [nimbus#7006](https://github.com/status-im/nimbus-eth2/pull/7006), [nimbus#9288](https://github.com/status-im/nimbus-eth2/pull/9288)

</details>


<a id="lookup_sync-014"></a>
<details>
<summary><b>lookup_sync-014</b> Cache pre-finalization block roots — <i>implemented · low · S · disk, bandwidth, cpu</i></summary>

**Idea.** Cache roots of blocks known to be at or before finalization (canonical or forked out) so attestations and lookups referencing them are rejected without disk reads or futile lookups.

**Impact.** Attestations to pre-finalization roots are rejected from an LRU cache without repeated disk reads or futile lookups.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/pre_finalization_cache.rs:46-92`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pre_finalization_cache.rs#L46-L92) is_pre_finalization_block: LRU root cache, then head state block_roots, then disk, then in-progress lookup cache
- [`beacon_node/beacon_chain/src/pre_finalization_cache.rs:94-99`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pre_finalization_cache.rs#L94-L99) pre_finalization_block_rejected caches roots of forked-out blocks
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1277`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1277) attestation path rejects outright
- [`beacon_node/beacon_chain/src/block_verification.rs:1842`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1842) check_block_against_finalized_slot feeds rejected roots into the cache

**Skeptic check.** This is Lighthouse's own PR #2909 and the code is live: canonical roots come from state/disk, forked-out roots from the block verification rejection hook. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#2909](https://github.com/sigp/lighthouse/pull/2909)

</details>


<a id="lookup_sync-015"></a>
<details>
<summary><b>lookup_sync-015</b> Verify downloaded block before retaining in lookup cache — <i>not · low · M · memory, bandwidth</i></summary>

**Idea.** In unknown-block sync, verify a downloaded block (including proposer signature) before storing it, and abort and penalise the serving and forwarding peers on failure, so invalid blocks do not occupy the cache.

**Gap in Lighthouse.** Lighthouse keeps the unverified block until the parent imports and only then verifies; a proposer-signature check before retaining would need a shuffling/head-state lookup in handle_unknown_parent.

**Impact.** Would stop invalid blocks occupying lookups and penalise forwarders earlier; lookups are already bounded by MAX_LOOKUPS and drop on stuck, so gain is small.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/mod.rs:195-210`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L195-L210) unknown-parent child stored in lookup with no verification
- [`beacon_node/network/src/sync/block_lookups/mod.rs:381-392`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L381-L392) MAX_LOOKUPS bound instead

**Sources.** [lodestar#10092](https://github.com/ChainSafe/lodestar/pull/10092)

</details>


<a id="lookup_sync-016"></a>
<details>
<summary><b>lookup_sync-016</b> Stop processing pending block once found invalid — <i>implemented · low · S · cpu</i></summary>

**Idea.** In the pending-block queue, exit processing of a block immediately when it is found invalid instead of continuing the work.

**Impact.** An invalid lookup block aborts the lookup and all child lookups immediately; no wasted follow-up processing.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/mod.rs:616-639`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L616-L639) drop_lookup_and_children recursively drops dependants
- [`beacon_node/network/src/sync/block_lookups/mod.rs:643-700`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L643-L700) on_lookup_result drops lookup on error
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:1075-1110`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L1075-L1110) invalid BlockError variants penalise peer and fail the lookup

**Skeptic check.** Prysm's fix was a control-flow bug (continuing after an invalid block in its pending queue); Lighthouse's lookup state machine has no equivalent continue-after-error path. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#7927](https://github.com/OffchainLabs/prysm/pull/7927)

</details>


<a id="lookup_sync-017"></a>
<details>
<summary><b>lookup_sync-017</b> Cap number of concurrent lookups — <i>implemented · low · S · memory</i></summary>

**Idea.** Put a hard cap on concurrent block lookups, so worst-case memory held by unvalidated lookup data stays bounded.

**Impact.** Memory held by lookups is bounded.

**Best measured result.** 200 lookups at most ~2 GB (pr:lighthouse#6015)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/mod.rs:77`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L77) const MAX_LOOKUPS: usize = 200
- [`beacon_node/network/src/sync/block_lookups/mod.rs:408`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L408) new_current_lookup refuses when single_block_lookups.len() &gt;= MAX_LOOKUPS

**Skeptic check.** All lookup kinds live in single_block_lookups and the single creation path enforces the cap. Upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#6015](https://github.com/sigp/lighthouse/pull/6015), [lodestar#3212](https://github.com/ChainSafe/lodestar/pull/3212)

</details>


<a id="lookup_sync-018"></a>
<details>
<summary><b>lookup_sync-018</b> Bound lookup child-peer map size — <i>not · low · S · memory</i></summary>

**Idea.** Cap the keys in the per-peer child-peers map used by lookups at peer count times a per-peer limit so the map cannot grow without bound.

**Gap in Lighthouse.** Add a MAX_GLOAS_CHILD_KEYS_PER_PEER cap in SingleBlockLookup::add_peer (and get_data_peers entry()), refusing new keys beyond peer_count*cap and counting refusals in a metric.

**Impact.** Only bounds memory a malicious peer can grow per lookup (lookups capped at 200); negligible on honest mainnet nodes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/single_block_lookup.rs:204`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/single_block_lookup.rs#L204) gloas_child_peers HashMap has no key cap
- [`beacon_node/network/src/sync/block_lookups/single_block_lookup.rs:686`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/single_block_lookup.rs#L686) add_peer inserts entry per execution_hash unconditionally
- grep MAX_GLOAS_CHILD_KEYS finds nothing; upstream PR 10463 is still OPEN

**Sources.** [lighthouse#10463](https://github.com/sigp/lighthouse/pull/10463)

</details>


<a id="lookup_sync-019"></a>
<details>
<summary><b>lookup_sync-019</b> Slot-window caps on by-root payload envelopes — <i>n/a · low · memory</i></summary>

**Idea.** Apply the same slot-window (not above current slot) and size caps to execution payload envelopes fetched by root as to gossip ones before storing them pending, so peers cannot pin unprunable future envelopes in memory.

**Impact.** Lighthouse does not store by-root envelopes in an unprunable pending map; they live inside a bounded, timed lookup.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/single_block_lookup.rs:204`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/single_block_lookup.rs#L204) by-root envelopes go straight to lookup processing (BlockProcessType::SinglePayloadEnvelope), no pending map
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:319`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L319) only gossip envelopes are held, in bounded, timed delay queues

**Sources.** [prysm#17175](https://github.com/OffchainLabs/prysm/pull/17175), [prysm#17176](https://github.com/OffchainLabs/prysm/pull/17176)

</details>


<a id="lookup_sync-020"></a>
<details>
<summary><b>lookup_sync-020</b> Store pending unknown-parent blocks on disk — <i>not · medium · L · memory</i></summary>

**Idea.** Store blocks waiting for a missing parent in the database and keep only root/parent-root indexes in memory, so long syncs with many pending blocks do not grow RAM unboundedly.

**Gap in Lighthouse.** Pending unknown-parent blocks live in RAM inside SingleBlockLookup (and pending components in the in-memory availability cache), bounded by MAX_LOOKUPS and depth tolerance. No DB-backed pending store exists; persisting would need a store with root/parent indexes.

**Impact.** Lowers worst-case RAM only in adversarial or deep-fork cases; negligible normally because deep chains fall back to range sync and lookups are capped.

**Best measured result.** Addresses possible OOM issues during long chain syncs (pr:ethlambda#116)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/mod.rs:77`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L77) MAX_LOOKUPS=200 in-memory cap (~2GB)
- [`beacon_node/network/src/sync/block_lookups/mod.rs:59`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L59) PARENT_DEPTH_TOLERANCE hands deep chains to range sync
- [`beacon_node/store/src/lib.rs:409`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/lib.rs#L409) OverflowLRUCache DB column marked DEPRECATED (the old disk-overflow of the availability cache was removed)
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs) pending components held in memory only

**Second check.** Also checked the data availability checker, which once spilled to disk via the OverflowLRUCache column; that column is now deprecated and the cache is memory-only.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [ethlambda#116](https://github.com/lambdaclass/ethlambda/pull/116), [lodestar@9617f9a72](https://github.com/ChainSafe/lodestar/commit/9617f9a72537)

</details>


<a id="lookup_sync-021"></a>
<details>
<summary><b>lookup_sync-021</b> Header-only backward chain tracking for unknown chains — <i>partial · medium · L · memory, sync</i></summary>

**Idea.** Track unknown chains as backward chains of headers or roots linked to fork choice without holding full blocks, then forward-sync the blocks by root, so long non-finality does not exhaust memory.

**Gap in Lighthouse.** The goal (deep unknown chains do not grow memory; discover backward, then sync forward) is met by a different mechanism: a bounded backward walk with full blocks, then a hand-off to forward range sync to the tip root. Missing: a header/root-only backward chain linked to fork choice and a forward sync by root, so the backward phase still holds up to PARENT_DEPTH_TOLERANCE full blocks per chain and the forward phase is by-range from the peers, not by-root along the known chain.

**Impact.** Small on a healthy node; memory is already bounded and deep chains already go to forward range sync. Gain is only in forky long non-finality where by-range from peers follows the wrong fork.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/mod.rs:59`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L59) PARENT_DEPTH_TOLERANCE bounds the backward by-root walk
- [`beacon_node/network/src/sync/block_lookups/mod.rs:275-337`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L275-L337) chain_too_long: drops the backward lookup chain (and its held blocks) and sends AddPeersForceRangeSync{head_root, head_slot, peers} so the chain is forward-synced instead
- [`beacon_node/network/src/sync/block_lookups/mod.rs:96`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L96) ignored_chains LRUTimeCache stops re-walking dropped chains
- [`beacon_node/network/src/sync/block_lookups/mod.rs:77`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L77) MAX_LOOKUPS=200

**Second check.** Beyond the earlier review, found the chain_too_long path that drops the lookup chain and forces forward range sync to the tip root (AddPeersForceRangeSync), which is the same backward-discover then forward-sync shape, so upgraded to partial.

**Verdict history.** not (checked) → partial (refuted)

**Sources.** [lodestar#8221](https://github.com/ChainSafe/lodestar/pull/8221)

</details>


<a id="lookup_sync-022"></a>
<details>
<summary><b>lookup_sync-022</b> Stop parent-chain lookup at finalized slot — <i>implemented · low · S · bandwidth, sync</i></summary>

**Idea.** While walking an unknown parent chain, stop once downloaded blocks reach the finalized slot or earlier and penalise the peer, so conflicting chains are not downloaded endlessly.

**Impact.** Parent walks on conflicting chains end at the first finalized-or-earlier block, with a peer penalty, and are capped in depth.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1915-1953`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1915-L1953) check_block_relevancy runs check_block_against_finalized_slot on RPC blocks before import
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:1095-1096`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L1095-L1096) WouldRevertFinalizedSlot/NotFinalizedDescendant penalise the block peer in lookups
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:858-869`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L858-L869) NotFinalizedDescendant gives PeerAction::Fatal
- [`beacon_node/network/src/sync/block_lookups/mod.rs:276`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L276) PARENT_DEPTH_TOLERANCE caps parent chain depth

**Skeptic check.** A downloaded parent at or before the finalized slot fails relevancy checks, which fails the lookup and drops its children with a penalty, the same post-download check Lodestar added. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#4134](https://github.com/ChainSafe/lodestar/pull/4134)

</details>


<a id="lookup_sync-023"></a>
<details>
<summary><b>lookup_sync-023</b> Slot-distance bound on unknown-parent lookups — <i>implemented · low · S · bandwidth, sync, cpu</i></summary>

**Idea.** Do not start by-root parent lookups for gossip blocks far beyond the local head (use range sync instead), with the max-slot-ahead threshold tuned so legitimate gaps from missed slots are still looked up.

**Impact.** Far-ahead gossip blocks do not trigger by-root parent lookups; a 32-slot tolerance keeps missed-slot gaps looked up.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/manager.rs:1151-1175`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L1151-L1175) should_search_for_block drops blocks more than SLOT_IMPORT_TOLERANCE from head while not synced
- [`beacon_node/network/src/sync/manager.rs:1001-1010`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L1001-L1010) handle_unknown_parent gates on block slot
- [`beacon_node/network/src/sync/block_lookups/mod.rs:276`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L276) PARENT_DEPTH_TOLERANCE hands deep chains to range sync

**Skeptic check.** The slot-distance bound applies while not synced, and the 32-slot tolerance is generous enough for missed or orphaned slots (the Grandine tuning concern). When synced, the depth cap and gossip future-slot rejection bound the work.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@99f416018](https://github.com/ChainSafe/lodestar/commit/99f416018faf), [grandine#370](https://github.com/grandinetech/grandine/pull/370)

</details>


<a id="lookup_sync-024"></a>
<details>
<summary><b>lookup_sync-024</b> No unknown-parent lookups while range syncing — <i>implemented · low · S · memory, bandwidth, sync</i></summary>

**Idea.** Disable or pause unknown-block-root and parent lookups while the node is range/forward syncing and enable them once synced, since range sync will fetch those blocks anyway.

**Impact.** While range syncing, unknown-root lookups are fully suppressed and parent lookups only run near head, so range sync is not duplicated.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/manager.rs:1036-1040`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L1036-L1040) handle_unknown_block_root returns 'not synced' when not synced (slot None)
- [`beacon_node/network/src/sync/manager.rs:1151-1170`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L1151-L1170) should_search_for_block only allows parent lookups within 32 slots of head while syncing
- [`beacon_node/network/src/sync/manager.rs:1129`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L1129) payload envelope lookups use the same gate

**Skeptic check.** All three unknown-block entry points (parent, attestation root, payload envelope) go through should_search_for_block. Lighthouse keeps a near-head window instead of a full unsubscribe, which has the same effect on wasted lookups.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#5654](https://github.com/ChainSafe/lodestar/pull/5654), [teku#3483](https://github.com/Consensys-Incorporated/teku/pull/3483)

</details>


<a id="lookup_sync-025"></a>
<details>
<summary><b>lookup_sync-025</b> Start parent lookup only after gossip validation — <i>implemented · low · S · cpu, sync</i></summary>

**Idea.** Trigger a parent lookup only after gossip validation finds the block otherwise processable and missing only its parent, so ignored blocks do not start lookup work.

**Impact.** Gossip blocks that are ignored for other reasons never start lookup work.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:922-988`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L922-L988) gossip checks (future slot, finalized slot, duplicate, known-invalid, finalized descendant) run before verify_parent_block_and_envelope_are_known
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1691-1695`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1691-L1695) UnknownParentBlock sent only on BlockError::ParentUnknown from gossip verification
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1981-1990`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1981-L1990) import path does not start a second lookup

**Skeptic check.** The parent lookup is started from the ParentUnknown result of gossip verification, after the cheap ignore checks. This matches the pre-Gloas behaviour Lodestar restored. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#9161](https://github.com/ChainSafe/lodestar/pull/9161)

</details>


<a id="lookup_sync-026"></a>
<details>
<summary><b>lookup_sync-026</b> Batch column by-root requests per peer — <i>partial · low · M · bandwidth, sync</i></summary>

**Idea.** Group missing data columns across columns and blocks into one by-root request per custodial peer (deterministic peer choice so requests coalesce), instead of one request per column or per block.

**Gap in Lighthouse.** Batching across blocks exists only for range sync (multi-root custody_lookup_request). Block lookups create one ActiveCustodyRequest per block (single_block_lookup.rs continue_requests passes &amp;[self.block_root]), so a parent chain of N lookups sends N separate DataColumnsByRoot requests to the same custody peer instead of one coalesced request.

**Impact.** Fewer by-root requests during multi-block lookup chains; normal single-head lookups gain nothing.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context/custody.rs:234`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L234) columns_to_request_by_peer groups columns per peer
- [`beacon_node/network/src/sync/network_context/custody.rs:301`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L301) one request carries block_roots plus indices
- [`beacon_node/network/src/sync/network_context/custody.rs:353`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L353) select_column_peer uses per-request RandomState for deterministic coalescing
- [`beacon_node/network/src/sync/block_lookups/single_block_lookup.rs:428`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/single_block_lookup.rs#L428) lookups call custody_lookup_request with &amp;[self.block_root] only

**Skeptic check.** Per-peer grouping across columns and the deterministic hasher are real; the earlier verdict did not check the across-blocks part on the lookup path, where each block is requested separately.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lighthouse#5821](https://github.com/sigp/lighthouse/pull/5821), [grandine@0925c53e0](https://github.com/grandinetech/grandine/commit/0925c53e0356), [grandine#255](https://github.com/grandinetech/grandine/pull/255), [nimbus#7486](https://github.com/status-im/nimbus-eth2/pull/7486), [nimbus#7488](https://github.com/status-im/nimbus-eth2/pull/7488)

</details>


<a id="lookup_sync-027"></a>
<details>
<summary><b>lookup_sync-027</b> Custody-overlap peer selection for column requests — <i>partial · medium · S · bandwidth, sync, latency</i></summary>

**Idea.** Choose peers for column by-root requests by how much of the needed columns they custody (supernodes best), only asking peers that custody them, and tune parallel request count accordingly.

**Gap in Lighthouse.** No scoring by how many of the needed columns a peer custodies; supernodes are not preferred. Make select_column_peer/continue_requests greedy by coverage of missing columns.

**Impact.** Fewer by-root column requests per lookup; small RPC-count and bandwidth gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context/custody.rs:353-391`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L353-L391) select_column_peer: only custodial peers of the column; sort key (at_concurrency_limit, not in lookup_peers, attempts, hash_one(peer))
- [`beacon_node/network/src/sync/network_context/custody.rs:378`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L378) per-request random_state hash gives consistent peer order so columns cluster on the same peers (coalescing by hash, not by coverage)
- [`beacon_node/network/src/sync/network_context/custody.rs:398`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L398) MAX_CUSTODY_PEER_ATTEMPTS=3

**Second check.** Re-read select_column_peer and the request batching; the consistent hash ordering coalesces columns onto shared peers, but only by chance, with no coverage term, so partial stands.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [nimbus#7477](https://github.com/status-im/nimbus-eth2/pull/7477), [nimbus#7492](https://github.com/status-im/nimbus-eth2/pull/7492), [lodestar#8330](https://github.com/ChainSafe/lodestar/pull/8330)

</details>


<a id="lookup_sync-028"></a>
<details>
<summary><b>lookup_sync-028</b> Filter column peers by earliest available slot — <i>implemented · low · S · bandwidth, sync</i></summary>

**Idea.** Only send custody column requests to peers whose advertised earliest available slot is at or before the block's slot, avoiding requests that will fail.

**Impact.** Custody column requests skip peers whose earliest_available_slot is after the block slot, avoiding requests that will fail.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context/custody.rs:364`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L364) get_custodial_peers(column_index, self.block_slot)
- [`beacon_node/lighthouse_network/src/peer_manager/peerdb.rs:297-313`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/peerdb.rs#L297-L313) good_custody_subnet_peer filters by is_synced_or_advanced_with_available_slot
- [`beacon_node/lighthouse_network/src/peer_manager/peerdb/sync_status.rs:35-41`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/peerdb/sync_status.rs#L35-L41) has_slot compares earliest_available_slot
- [`beacon_node/lighthouse_network/src/peer_manager/peerdb.rs:255-265`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/peerdb.rs#L255-L265) synced_peers_for_epoch applies the same filter for backfill and custody backfill

**Skeptic check.** This is Lighthouse PR #9447 and it is live in custody-by-root (lookups and range coupling) and in the backfill peer selection. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#9447](https://github.com/sigp/lighthouse/pull/9447)

</details>


<a id="lookup_sync-029"></a>
<details>
<summary><b>lookup_sync-029</b> Balance lookup requests by active requests per peer — <i>partial · low · S · sync, bandwidth</i></summary>

**Idea.** Pick lookup peers by fewest active requests (a peer balancer) to spread by-root requests and avoid peer rate limiting.

**Gap in Lighthouse.** Lighthouse only treats peers as full/not-full at a threshold and breaks ties randomly; it never picks the peer with the fewest active requests. Replace the bool in the sort keys with the count from ActiveRequestsPerPeer.

**Impact.** Slightly better spread of by-root requests across peers when many lookups run at once; marginal since the hard limit already avoids rate-limit hits.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context.rs:116`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L116) at_concurrency_limit counts active requests per peer vs MAX_CONCURRENT_REQUESTS
- [`beacon_node/network/src/sync/network_context.rs:716-735`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L716-L735) block lookup peer key (failed, at_limit, random)
- [`beacon_node/network/src/sync/network_context/custody.rs:353-390`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L353-L390) column peer key includes at_limit and attempt count

**Sources.** [lodestar#8219](https://github.com/ChainSafe/lodestar/pull/8219)

</details>


<a id="lookup_sync-030"></a>
<details>
<summary><b>lookup_sync-030</b> Skip column requests for blocks without blobs — <i>implemented · low · S · bandwidth, cpu</i></summary>

**Idea.** Do not issue custody column requests for blocks with zero blob commitments.

**Impact.** No column requests for zero-blob blocks, in both lookup and range sync.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/single_block_lookup.rs:398-416`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/single_block_lookup.rs#L398-L416) DataRequest::NoData when data_columns_required_for_block is false
- [`beacon_node/beacon_chain/src/custody_context.rs:595-597`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L595-L597) requires num_expected_blobs() &gt; 0
- [`beacon_node/network/src/sync/block_sidecar_coupling.rs:238-252`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_sidecar_coupling.rs#L238-L252) range sync only requests columns for blocks with blobs and skips the request when none have them

**Skeptic check.** Verified on the lookup path (PR #6814) and also on range sync, where the coupling filters blocks by num_expected_blobs before the custody request. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#6814](https://github.com/sigp/lighthouse/pull/6814)

</details>


<a id="lookup_sync-031"></a>
<details>
<summary><b>lookup_sync-031</b> Drop roots with empty column list from request — <i>n/a · low · bandwidth, sync</i></summary>

**Idea.** When building a by-root columns request for a peer, drop roots whose intersection with the peer's custody is empty so no empty entries are sent.

**Gap in Lighthouse.** Lighthouse asks every block root for the same set of indices per peer, so no per-root intersection with the peer custody exists and no empty entries are built.

**Impact.** No change needed.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context/custody.rs:295-303`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L295-L303) same indices list is applied to every block root of the request
- [`beacon_node/network/src/sync/network_context/requests/data_columns_by_root.rs:25-35`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/requests/data_columns_by_root.rs#L25-L35) identifiers built per root from one column list

**Sources.** [nimbus#7489](https://github.com/status-im/nimbus-eth2/pull/7489)

</details>


<a id="lookup_sync-032"></a>
<details>
<summary><b>lookup_sync-032</b> Dedupe column indices in by-root request — <i>implemented · low · S · bandwidth</i></summary>

**Idea.** Deduplicate missing column indices when building a column by-root request so the same column is not requested twice.

**Impact.** Already done; a column index can appear only once per by-root request.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context/custody.rs:27`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L27) column_requests is an FnvHashMap keyed by ColumnIndex
- [`beacon_node/network/src/sync/network_context/custody.rs:241-262`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L241-L262) each column index assigned to exactly one peer per round
- [`beacon_node/network/src/sync/network_context.rs:976-992`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L976-L992) indices from sampling_columns_for_epoch minus cached

**Skeptic check.** Verified column_requests is a map keyed by index and the per-peer lists are built by iterating it once, so duplicates cannot occur. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#7449](https://github.com/status-im/nimbus-eth2/pull/7449)

</details>


<a id="lookup_sync-033"></a>
<details>
<summary><b>lookup_sync-033</b> Cap blocks per by-root columns request — <i>n/a · low · bandwidth, sync</i></summary>

**Idea.** Limit the number of blocks in a by-root columns request to the peer's max-blocks-per-request, besides the sidecar cap, so requests are not rejected and retried.

**Gap in Lighthouse.** Request size is bounded by batch size (one epoch, 32 blocks, 128 columns max = 4096 sidecars), well under both caps, so no splitting is needed.

**Impact.** No change needed.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_sidecar_coupling.rs:234-262`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_sidecar_coupling.rs#L234-L262) range custody request covers one epoch batch (at most 32 roots)
- [`beacon_node/lighthouse_network/src/rpc/methods.rs:580`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/methods.rs#L580) DataColumnsByRootRequest::new errors if above max_request_blocks

**Sources.** [nimbus#9206](https://github.com/status-im/nimbus-eth2/pull/9206)

</details>


<a id="lookup_sync-034"></a>
<details>
<summary><b>lookup_sync-034</b> Exclude already-stored blobs from by-root request — <i>implemented · low · S · bandwidth</i></summary>

**Idea.** Before requesting blob sidecars by root, filter out indices already in the database so only missing blobs are requested.

**Impact.** Already done for data columns; blob by-root lookups no longer exist in sync.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context.rs:976-992`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L976-L992) custody_lookup_request filters out cached_data_column_indexes unless ignore_cache
- [`beacon_node/network/src/sync/block_lookups/single_block_lookup.rs:420-431`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/single_block_lookup.rs#L420-L431) single lookups pass ignore_cache=false
- [`beacon_node/network/src/sync/network_context/requests`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/requests)/ (no blobs_by_root request type exists)

**Skeptic check.** Confirmed the column equivalent filters indices already in the DA checker cache on the single-lookup path, and there is no blobs-by-root lookup left to apply it to. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#13012](https://github.com/OffchainLabs/prysm/pull/13012)

</details>


<a id="lookup_sync-035"></a>
<details>
<summary><b>lookup_sync-035</b> Time column fetching relative to gossip arrival — <i>not · medium · S · latency, bandwidth</i></summary>

**Idea.** Start by-root column fetching at a point timed against expected gossip arrival so columns gossip will deliver are not also fetched by RPC.

**Gap in Lighthouse.** Add a gossip-timed start for the column by-root request (for recent blocks, wait until a point after the expected column gossip arrival, then re-read cached_data_column_indexes before sending).

**Impact.** Avoids RPC download of columns that gossip delivers moments later on lookups of recent blocks; modest bandwidth saving.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/single_block_lookup.rs:396-431`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/single_block_lookup.rs#L396-L431) data request starts as soon as the block is downloaded; only the DA cache is consulted
- [`beacon_node/network/src/sync/network_context.rs:967-992`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L967-L992) custody_lookup_request waits only for a non-empty lookup_peers set, then filters cached_data_column_indexes
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:120-155`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L120-L155) gossip/RPC dedup (duplicate_cache + QUEUED_RPC_BLOCK_DELAY) is for blocks, not columns
- [`beacon_node/network/src/sync/network_context/custody.rs:20`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L20) MAX_STALE_NO_PEERS_DURATION is a give-up timer, not a start delay

**Second check.** Also checked the beacon processor reprocess queue (RPC block delay, unknown-block column queue, delayed reconstruction) and the custody request timers; none delay column fetching relative to gossip arrival.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [nimbus#7461](https://github.com/status-im/nimbus-eth2/pull/7461)

</details>


<a id="lookup_sync-036"></a>
<details>
<summary><b>lookup_sync-036</b> No column fetch at Gloas block import — <i>partial · low · M · bandwidth, latency</i></summary>

**Idea.** For Gloas blocks skip fetching custody columns at block import (DA is checked on the envelope) and drain queued gossip columns instead of re-requesting all columns from peers.

**Gap in Lighthouse.** Block import is not gated on columns for Gloas and gossip-cached columns are not refetched, but the lookup still tracks a DataRequest and fetches missing custody columns from peers at block time instead of at envelope time. Move column fetch to the envelope step.

**Impact.** Avoids column requests for Gloas blocks whose payload is withheld; small and only after Gloas.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/single_block_lookup.rs:403-433`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/single_block_lookup.rs#L403-L433) columns still requested in the block lookup for Gloas blocks (num_expected_blobs reads the bid)
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:866-873`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L866-L873) Gloas blocks import without columns (NoData allowed)
- [`beacon_node/network/src/sync/network_context.rs:976-992`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L976-L992) gossip-cached columns are skipped

**Sources.** [prysm#17232](https://github.com/OffchainLabs/prysm/pull/17232)

</details>


<a id="lookup_sync-037"></a>
<details>
<summary><b>lookup_sync-037</b> Request blobs only after block is downloaded — <i>implemented · low · S · bandwidth, sync</i></summary>

**Idea.** Do not request blobs or columns for a lookup root until the block is known, so they are requested only if the block has data and with the exact count.

**Impact.** Already done; no data request is sent before the block is known.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/single_block_lookup.rs:398-415`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/single_block_lookup.rs#L398-L415) DataRequest::WaitingForBlock until block downloaded, then data_columns_required_for_block chooses Request or NoData
- [`beacon_node/network/src/sync/block_lookups/single_block_lookup.rs:237`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/single_block_lookup.rs#L237) lookups start in WaitingForBlock

**Skeptic check.** Read the state machine: data requests begin only after peek_downloaded_data returns the block and only if it needs columns. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#5774](https://github.com/sigp/lighthouse/pull/5774)

</details>


<a id="lookup_sync-038"></a>
<details>
<summary><b>lookup_sync-038</b> Key parent blob lookups by parent root — <i>implemented · low · S · bandwidth, sync</i></summary>

**Idea.** Deduplicate parent blob lookups by the parent block root rather than the child root, so the same parent's blobs are not requested twice.

**Impact.** Already done; parent data requests are owned by the parent-root lookup and deduped by root.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/mod.rs:374-393`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L374-L393) new_current_lookup reuses an existing lookup with is_for_block(block_root)
- [`beacon_node/network/src/sync/block_lookups/mod.rs:256`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L256) search_parent_of_child creates lookup for the parent root
- [`beacon_node/network/src/sync/block_lookups/single_block_lookup.rs:420-431`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/single_block_lookup.rs#L420-L431) data request is part of the lookup for that root

**Skeptic check.** Lookups (block plus data) are keyed by their own block root and deduplicated on creation, so two children of one parent share one parent lookup. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#5432](https://github.com/sigp/lighthouse/pull/5432)

</details>


<a id="lookup_sync-039"></a>
<details>
<summary><b>lookup_sync-039</b> No EL getBlobs during by-root sync — <i>not · low · S · cpu, latency</i></summary>

**Idea.** Do not call engine getBlobs while serving by-root lookup sync; use it only for validated gossip objects.

**Gap in Lighthouse.** Lighthouse calls engine getBlobs after RPC lookup blocks (process_type lookup) when components are missing; remove or gate that call in the MissingComponents arm of the lookup block processing in sync_methods.rs.

**Impact.** Avoids one EL getBlobs call per by-root lookup block; Lodestar removed it for complexity, gain is small and may even lose a fast path, so likely skip.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:206-222`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L206-L222) lookup block with MissingComponents triggers fetch_engine_blobs_and_publish_full(EnvelopeSource::Rpc)
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1127`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1127) gossip path

**Sources.** [lodestar#8341](https://github.com/ChainSafe/lodestar/pull/8341)

</details>


<a id="lookup_sync-040"></a>
<details>
<summary><b>lookup_sync-040</b> Avoid retrying failed peers in lookups — <i>implemented · low · S · bandwidth, sync</i></summary>

**Idea.** Remember per root (or per column) which peers failed or returned empty, cap retries per peer and exclude or deprioritise them when picking the retry peer, resetting when all are exhausted. Retries then spread over peers that may have the data instead of looping on the same one.

**Impact.** Retries spread over other peers and are bounded per lookup; no retry storm.

**Best measured result.** Retry storm: 131 WARN retries over 56 roots in ~35 s on one node, peers hit 45+ times (pr:ethlambda#186)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/single_block_lookup.rs:777`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/single_block_lookup.rs#L777) failed_peers per request state
- [`beacon_node/network/src/sync/block_lookups/single_block_lookup.rs:640`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/single_block_lookup.rs#L640) record_failed_peer on block download error
- [`beacon_node/network/src/sync/network_context.rs:708`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L708) block_lookup_request sorts failed peers last
- [`beacon_node/network/src/sync/network_context/custody.rs:353`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L353) select_column_peer excludes peers over MAX_CUSTODY_PEER_ATTEMPTS and orders by attempt count
- [`beacon_node/network/src/sync/block_lookups/mod.rs:61`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L61) SINGLE_BLOCK_LOOKUP_MAX_ATTEMPTS = 4 bounds retries per lookup

**Skeptic check.** Download failures (including empty by-root responses, which are errors) are recorded and de-prioritised for block and payload requests; columns cap per-peer attempts. Minor nuance: processing failures (on_processing_failure) penalise but do not add the peer to failed_peers. Upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#9542](https://github.com/sigp/lighthouse/pull/9542), [ethlambda#186](https://github.com/lambdaclass/ethlambda/pull/186), [lighthouse#6084](https://github.com/sigp/lighthouse/pull/6084), [lighthouse#8005](https://github.com/sigp/lighthouse/pull/8005)

</details>


<a id="lookup_sync-041"></a>
<details>
<summary><b>lookup_sync-041</b> Request missing payload envelope at payload deadline — <i>not · low · M · latency, cpu, bandwidth</i></summary>

**Idea.** Do not search for a missing execution payload envelope at block arrival; record the root and, at the payload-due deadline, issue one by-root request (polling) if gossip has not delivered it, deduping triggers per payload.

**Gap in Lighthouse.** Envelope fetch is not deadline-based: lookups request the envelope immediately after the block, and attestations trigger separate searches. Would need a timer at payload-due in sync manager that issues one by-root request for blocks with payload_received false, deduped per root.

**Impact.** Gloas only: fewer premature by-root envelope requests when gossip delivers the envelope within the deadline; small bandwidth/peer-load saving.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/manager.rs:1103`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L1103) handle_unknown_payload_envelope triggered by attestations (index==1), debounced
- [`beacon_node/network/src/sync/block_lookups/single_block_lookup.rs:458-480`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/single_block_lookup.rs#L458-L480) lookups request envelope right after block download
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2242`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2242) get_payload_due only used for timing metrics

**Sources.** [lodestar#10134](https://github.com/ChainSafe/lodestar/pull/10134), [prysm#16904](https://github.com/OffchainLabs/prysm/pull/16904), [lodestar#10289](https://github.com/ChainSafe/lodestar/pull/10289)

</details>


<a id="lookup_sync-042"></a>
<details>
<summary><b>lookup_sync-042</b> Fetch payload envelopes on demand only — <i>not · low · M · bandwidth, memory</i></summary>

**Idea.** Do not fetch execution payload envelopes by RPC for every imported block; fetch one only when a child block or attestation needs the full payload.

**Gap in Lighthouse.** Every looked-up Gloas block also fetches its envelope. Make PayloadRequest lazy: only request when a child block or index==1 attestation needs it (use the existing search_payload_envelope path).

**Impact.** Gloas only: skips envelope downloads for lookup blocks nobody builds on; saves bandwidth during lookups, not on steady-state head.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/single_block_lookup.rs:456-480`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/single_block_lookup.rs#L456-L480) every Gloas lookup gets a PayloadRequest::Request after its block downloads

**Sources.** [teku#11497](https://github.com/Consensys-Incorporated/teku/pull/11497)

</details>


<a id="lookup_sync-043"></a>
<details>
<summary><b>lookup_sync-043</b> Request parent envelope in parallel with parent block — <i>not · low · M · latency, sync</i></summary>

**Idea.** When filling a block gap, request the parent's payload envelope by root concurrently with the parent block request instead of after it, saving one round trip.

**Gap in Lighthouse.** Payload request waits for the block to download (needs block for bid hash and fork check), so parent block and parent envelope are sequential. Request the envelope in parallel using the child's bid parent_block_hash (AwaitingParent already carries parent_block_hash) in the PayloadRequest init instead of waiting for the parent block.

**Impact.** Gloas only: saves one RPC round trip per parent in a gap fill, roughly 100-300 ms per hop; only matters when lookups chain.

**Best measured result.** Saves one round trip syncing to head (pr:prysm#16908)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/single_block_lookup.rs:458-480`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/single_block_lookup.rs#L458-L480) payload_request stays WaitingForBlock until block_request has downloaded data

**Sources.** [prysm#16908](https://github.com/OffchainLabs/prysm/pull/16908)

</details>


<a id="lookup_sync-044"></a>
<details>
<summary><b>lookup_sync-044</b> Batched by-root requests to best-scored peers — <i>partial · low · S · latency, sync</i></summary>

**Idea.** Request missing parent blocks by root in batches from the best-scored peers with short dial timeouts, so a slow peer does not stall lookups.

**Gap in Lighthouse.** Peers are picked randomly with failed-peer and concurrency deprioritisation, not by score, and roots are not batched. Add the peer score as a sort key in block_lookup_request and batch roots into one BlocksByRoot request.

**Impact.** Marginally fewer stalled lookups with a slow peer; negligible on mainnet nodes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context.rs:716-731`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L716-L731) peer chosen by (failed, at-concurrency-limit, random) among lookup peers; no peer score; one root per request

**Sources.** [prysm#7027](https://github.com/OffchainLabs/prysm/pull/7027)

</details>


<a id="lookup_sync-045"></a>
<details>
<summary><b>lookup_sync-045</b> Redundant parallel lookup requests to two peers — <i>not · low · M · latency, sync</i></summary>

**Idea.** Send a missing-ancestor by-root request to two peers in parallel and take the first good response, so a slow or failing peer does not stall the lookup.

**Gap in Lighthouse.** Single peer per lookup request with retry. Would send the request to two peers in block_lookup_request and keep the first response.

**Impact.** Cuts tail latency on a slow peer but doubles bandwidth for lookups; marginal.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context.rs:708`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L708) block_lookup_request sends to exactly one peer, retries on failure

**Sources.** [nimbus@a0d4c3432](https://github.com/status-im/nimbus-eth2/commit/a0d4c3432fde)

</details>


<a id="lookup_sync-046"></a>
<details>
<summary><b>lookup_sync-046</b> Run parent lookups off the sync event loop — <i>implemented · low · S · latency, sync</i></summary>

**Idea.** Run parent lookups on a separate task and report the result by message instead of inline in the sync manager, so slow lookups do not block the sync loop.

**Impact.** Already done; lookup processing runs on beacon processor workers and reports by message.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/single_block_lookup.rs:386-394`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/single_block_lookup.rs#L386-L394) send_block_for_processing hands the block to the beacon processor
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:236`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L236) result returned as SyncMessage::BlockComponentProcessed

**Skeptic check.** Lookups are non-blocking state machines; downloads are async RPC and verification/import is on workers. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#906](https://github.com/sigp/lighthouse/pull/906)

</details>


<a id="lookup_sync-047"></a>
<details>
<summary><b>lookup_sync-047</b> Pass fetched block into blob validation — <i>n/a · low · disk, latency</i></summary>

**Idea.** Pass the already-fetched block directly into blob sidecar validation rather than re-reading it from the database.

**Impact.** Nothing; blob import never re-reads the block from the DB.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:3589`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3589) process_rpc_blobs takes block_root+slot, no DB block read

**Sources.** [prysm#13062](https://github.com/OffchainLabs/prysm/pull/13062)

</details>


<a id="lookup_sync-048"></a>
<details>
<summary><b>lookup_sync-048</b> Run cheap subset check first on by-root responses — <i>partial · low · S · cpu</i></summary>

**Idea.** Check that a by-root response is a subset of what was requested before the more expensive sanity checks, rejecting bad responses earlier.

**Gap in Lighthouse.** DataColumnsByRootRequestItems::add runs verify_inclusion_proof (merkle hashing) before the cheap self.request.indices.contains(index) subset check, so a column with an unrequested index costs a proof verification before rejection. Swap the two checks.

**Impact.** Negligible CPU saved only on misbehaving peers; one merkle proof per bad column.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context/requests/blocks_by_root.rs:38-45`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/requests/blocks_by_root.rs#L38-L45) root check is the only check, done first
- [`beacon_node/network/src/sync/network_context/requests/data_columns_by_root.rs:57-71`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/requests/data_columns_by_root.rs#L57-L71) block_root check first, then verify_inclusion_proof, then the cheap requested-index check

**Skeptic check.** Blocks-by-root does the subset check first; columns-by-root checks root first but the index subset check comes after the inclusion proof, the exact ordering the nimbus PR fixed. Earlier evidence noticed this and still called it implemented.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [nimbus#7078](https://github.com/status-im/nimbus-eth2/pull/7078)

</details>


<a id="lookup_sync-049"></a>
<details>
<summary><b>lookup_sync-049</b> Compute hash tree root outside pending-blocks lock — <i>n/a · low · latency</i></summary>

**Idea.** Compute block roots before taking the pending-blocks lock so the lock is held as briefly as possible.

**Impact.** No lock around a pending-blocks map exists; sync manager is single-threaded.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/mod.rs:92`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L92) lookups are owned by the single sync task, no shared pending-blocks mutex

**Sources.** [prysm#4709](https://github.com/OffchainLabs/prysm/pull/4709)

</details>


<a id="lookup_sync-050"></a>
<details>
<summary><b>lookup_sync-050</b> DAG of unknown blocks drives by-root lookups — <i>partial · low · M · sync</i></summary>

**Idea.** Maintain a dedicated DAG of unknown blocks and their parent links and drive by-root lookups from it.

**Gap in Lighthouse.** Lighthouse tracks lookups and derives parent chains on demand each time (O(n) scans) rather than keeping a persistent DAG; a persistent root-indexed DAG would need single_block_lookups re-indexed by block_root and parent links maintained incrementally in BlockLookups.

**Impact.** Marginal CPU saving in search_parent_of_child under many concurrent lookups; function is only hot during attack or deep-fork conditions.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/mod.rs:92`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L92) single_block_lookups map by lookup id
- [`beacon_node/network/src/sync/block_lookups/parent_chain.rs:40`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/parent_chain.rs#L40) compute_parent_chains builds chains on demand
- [`beacon_node/network/src/sync/block_lookups/mod.rs:98`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L98) TODO notes lookups not indexed by block_root

**Sources.** [nimbus#8869](https://github.com/status-im/nimbus-eth2/pull/8869)

</details>


<a id="lookup_sync-051"></a>
<details>
<summary><b>lookup_sync-051</b> Debounce unknown-root attestation events per peer — <i>implemented · low · S · cpu</i></summary>

**Idea.** Debounce unknown-block-root events from attestations per (root, peer) pair so a peer forwarding thousands of attestations for one root causes one lookup update.

**Impact.** Already done; one lookup update per (peer, root) within the cache TTL.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/manager.rs:271`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L271) notified_unknown_roots LRUTimeCache&lt;(PeerId, Hash256)&gt;
- [`beacon_node/network/src/sync/manager.rs:921-926`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L921-L926) UnknownBlockHashFromAttestation skipped when (peer, root) already notified
- [`beacon_node/network/src/sync/manager.rs:927-934`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L927-L934) same debounce for unknown payload envelopes

**Skeptic check.** Confirmed the debounce by (peer, root) in the sync manager, matching lighthouse#5706. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#5706](https://github.com/sigp/lighthouse/pull/5706), [lodestar#3648](https://github.com/ChainSafe/lodestar/pull/3648)

</details>


<a id="lookup_sync-052"></a>
<details>
<summary><b>lookup_sync-052</b> Do not start RPC lookups from partial gossip — <i>partial · low · S · bandwidth, cpu</i></summary>

**Idea.** When gossip has delivered only a block or one blob, do not start a delayed RPC lookup for the rest; let gossip deliver it, avoiding double downloads.

**Gap in Lighthouse.** On Gloas, a gossip data column (or partial column) for a block not yet known (load_gloas_payload_bid returns None) immediately triggers UnknownBlockHashFromAttestation, so after 3 corroborating peers (DEFAULT_UNKNOWN_ROOT_MIN_PEERS) an RPC block lookup starts while the block is probably still arriving on gossip; there is no delay to let gossip deliver it.

**Impact.** Avoids a by-root block download per slot when columns race ahead of the block on Gloas; Fulu is unaffected.

**Best measured result.** RPC takes ~1s; delayed lookups often double download (pr:lighthouse#4992)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1016`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1016) Fulu column MissingComponents: no lookup
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1972`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1972) gossip block MissingComponents: no lookup
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:790`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L790) Gloas gossip column with BlockRootUnknown sends UnknownBlockHashFromAttestation
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1182`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1182) same for partial columns
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1242`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1242) BlockRootUnknown when no bid is cached for the column's block

**Skeptic check.** The Fulu paths the earlier evidence cited are correct (MissingComponents only traces), but it missed the Gloas BlockRootUnknown branch where partial gossip does start a lookup.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lighthouse#4992](https://github.com/sigp/lighthouse/pull/4992)

</details>


<a id="lookup_sync-053"></a>
<details>
<summary><b>lookup_sync-053</b> Key pending blocks queue by root in hash map — <i>n/a · low · S · cpu, sync</i></summary>

**Idea.** Store the queue of partially downloaded or pending blocks in a hash map keyed by block root rather than a vector, so membership, insert and removal are O(1), and prune stale entries in one retain pass.

**Impact.** The old simple_sync import_queue Vec no longer exists. Root lookups scan at most 200 lookups, which is negligible.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/mod.rs:99`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L99) lookups in FnvHashMap keyed by SingleLookupId
- [`beacon_node/network/src/sync/block_lookups/mod.rs:575`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L575) has_lookup_for_block is a linear scan over values()
- [`beacon_node/network/src/sync/block_lookups/mod.rs:77`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L77) MAX_LOOKUPS = 200

**Sources.** [lighthouse@2a7122bea](https://github.com/sigp/lighthouse/commit/2a7122beafc1)

</details>


<a id="lookup_sync-054"></a>
<details>
<summary><b>lookup_sync-054</b> Import RPC-received blocks without requeue delay — <i>implemented · low · S · latency</i></summary>

**Idea.** Process blocks received over RPC immediately instead of requeueing them with a delay meant as an equivocation mitigation, since fork choice now handles equivocating blocks and the delay only adds import latency.

**Impact.** RPC lookup blocks are imported at once; the 4s requeue applies only when the same root is already being imported from gossip.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:112-145`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L112-L145)
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:67`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L67)
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:802-822`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L802-L822)

**Skeptic check.** process_lookup_block requeues only on a duplicate_cache hit, which is a dedup, not the old equivocation delay. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#5037](https://github.com/sigp/lighthouse/pull/5037)

</details>


<a id="lookup_sync-055"></a>
<details>
<summary><b>lookup_sync-055</b> Skip envelope lookups for roots that cannot have one — <i>implemented · low · S · bandwidth, sync</i></summary>

**Idea.** Do not enqueue payload-envelope downloads for known roots that can never have an envelope (genesis, pre-fork blocks), so lookup sync does not retry impossible requests forever.

**Impact.** Envelope lookups need a fork-choice block with a bid block hash. Lookup-downloaded pre-Gloas blocks get PayloadRequest::PreGloas and request no envelope.

**Best measured result.** Eliminated genesis-root pendingPayloads loop; pending_payloads_size 0 on both nodes (pr:lodestar#9281)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/manager.rs:1103-1128`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L1103-L1128)
- [`beacon_node/network/src/sync/block_lookups/mod.rs:232-247`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L232-L247)
- [`beacon_node/network/src/sync/block_lookups/single_block_lookup.rs:458-467`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/single_block_lookup.rs#L458-L467)

**Skeptic check.** search_payload_envelope has a single caller, and it is guarded by fork-choice presence, payload_received and execution_payload_block_hash. The in-lookup payload request is skipped for pre-Gloas forks, so neither path can loop on an impossible root.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#9281](https://github.com/ChainSafe/lodestar/pull/9281)

</details>


<a id="lookup_sync-056"></a>
<details>
<summary><b>lookup_sync-056</b> No retry for deterministic block processing errors — <i>not · low · S · cpu, bandwidth</i></summary>

**Idea.** In lookup sync, classify block processing errors determined by the block root (e.g. invalid state root) as non-retryable and discard the block at once, instead of re-downloading and re-processing it several times.

**Gap in Lighthouse.** Add a non-retryable flag to BlockProcessingResult::Error for errors determined by the block root (StateRootMismatch, InvalidSignature, IncorrectBlockProposer, PerBlockProcessingError) and make SingleBlockLookup::on_block_processing_result return a drop result instead of on_processing_failure; the variants are already listed explicitly.

**Impact.** An invalid block is downloaded and processed up to 4 times; dropping at once saves 3 downloads plus 3 state transitions, but only when a peer feeds an invalid block.

**Best measured result.** Today a block with incorrect state root is downloaded and processed 5 times (pr:lighthouse#6321)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:951`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L951) StateRootMismatch, InvalidSignature etc. only yield BlockProcessingResult::Error with a penalty
- [`beacon_node/network/src/sync/block_lookups/single_block_lookup.rs:561`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/single_block_lookup.rs#L561) Error leads to on_processing_failure and AwaitingDownload again
- [`beacon_node/network/src/sync/block_lookups/single_block_lookup.rs:985`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/single_block_lookup.rs#L985) retries until SINGLE_BLOCK_LOOKUP_MAX_ATTEMPTS = 4 (mod.rs:62)

**Sources.** [lighthouse#6321](https://github.com/sigp/lighthouse/pull/6321)

</details>


