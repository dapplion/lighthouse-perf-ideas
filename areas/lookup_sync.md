# lookup_sync

17 ideas: 2 not, 5 partial, 10 implemented; 7 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

Ids missing from the sequence are ideas that have not been checked against Lighthouse yet.

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [lookup_sync-001](#lookup_sync-001) **★** | Prune pending lookup queue at finalization | partial | medium | S | memory, bandwidth, sync |
| [lookup_sync-002](#lookup_sync-002) | Expire pending blocks and lookups by age | implemented | medium |  | memory, sync |
| [lookup_sync-003](#lookup_sync-003) **★** | Exponential backoff for failing by-root roots | partial | medium | S | bandwidth, cpu, sync |
| [lookup_sync-004](#lookup_sync-004) | Attestations for unknown root trigger block lookup | implemented | medium |  | latency, sync |
| [lookup_sync-006](#lookup_sync-006) | Request unknown block from peers that announced it | implemented | medium |  | sync, latency, bandwidth |
| [lookup_sync-009](#lookup_sync-009) | One in-flight lookup per block root | implemented | low |  | bandwidth, cpu, sync |
| [lookup_sync-010](#lookup_sync-010) | Skip lookup if block already received or processing | implemented | low |  | bandwidth, cpu, sync |
| [lookup_sync-011](#lookup_sync-011) | Request deepest missing ancestor directly | implemented | medium |  | sync, latency, bandwidth |
| [lookup_sync-013](#lookup_sync-013) **★** | Remember invalid and unviable blocks and forks | partial | medium | S | bandwidth, cpu, sync |
| [lookup_sync-017](#lookup_sync-017) | Cap number of concurrent lookups | implemented | low |  | memory |
| [lookup_sync-020](#lookup_sync-020) **★** | Store pending unknown-parent blocks on disk | not | medium | L | memory |
| [lookup_sync-021](#lookup_sync-021) **★** | Header-only backward chain tracking for unknown chains | partial | medium | L | memory, sync |
| [lookup_sync-026](#lookup_sync-026) | Batch column by-root requests per peer | implemented | medium |  | bandwidth, sync |
| [lookup_sync-027](#lookup_sync-027) **★** | Custody-overlap peer selection for column requests | partial | medium | S | bandwidth, sync, latency |
| [lookup_sync-035](#lookup_sync-035) **★** | Time column fetching relative to gossip arrival | not | medium | S | latency, bandwidth |
| [lookup_sync-040](#lookup_sync-040) | Avoid retrying failed peers in lookups | implemented | low |  | bandwidth, sync |
| [lookup_sync-052](#lookup_sync-052) | Do not start RPC lookups from partial gossip | implemented | low | S | bandwidth, cpu |

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

**Sources.** [teku#1082](https://github.com/Consensys-Incorporated/teku/pull/1082), [prysm#4066](https://github.com/OffchainLabs/prysm/pull/4066), [prysm#4168](https://github.com/OffchainLabs/prysm/pull/4168), [nimbus#9185](https://github.com/status-im/nimbus-eth2/pull/9185), [lodestar#9852](https://github.com/ChainSafe/lodestar/pull/9852)

</details>


<a id="lookup_sync-002"></a>
<details>
<summary><b>lookup_sync-002</b> Expire pending blocks and lookups by age — <i>implemented · medium · memory, sync</i></summary>

**Idea.** Give each pending unknown-parent block or lookup a maximum lifetime (TTL or max duration) and drop it, with its children, when it expires. This bounds the queue and frees state and peers held by stuck lookups.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/mod.rs:67`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L67) LOOKUP_MAX_DURATION_STUCK_SECS
- [`beacon_node/network/src/sync/block_lookups/mod.rs:71`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L71) LOOKUP_MAX_DURATION_NO_PEERS_SECS=10
- [`beacon_node/network/src/sync/block_lookups/mod.rs:779`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L779) drop_stuck_lookups drops oldest ancestor and children

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

**Sources.** [nimbus#8372](https://github.com/status-im/nimbus-eth2/pull/8372), [lodestar#9791](https://github.com/ChainSafe/lodestar/pull/9791)

</details>


<a id="lookup_sync-004"></a>
<details>
<summary><b>lookup_sync-004</b> Attestations for unknown root trigger block lookup — <i>implemented · medium · latency, sync</i></summary>

**Idea.** When a gossip attestation references an unknown block root, start a by-root block request at once instead of waiting for the gossip block, since attestations often arrive first.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/manager.rs:921`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L921) UnknownBlockHashFromAttestation handled
- [`beacon_node/network/src/sync/manager.rs:1036`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L1036) handle_unknown_block_root -&gt; search_unknown_block
- ../network_beacon_processor/gossip_methods.rs:790 attestation sends sync message

**Sources.** [lodestar#5485](https://github.com/ChainSafe/lodestar/pull/5485)

</details>


<a id="lookup_sync-006"></a>
<details>
<summary><b>lookup_sync-006</b> Request unknown block from peers that announced it — <i>implemented · medium · sync, latency, bandwidth</i></summary>

**Idea.** Record which peers sent attestations or blocks referencing each unknown root and request the block from those peers first, deduped per (root, peer). Those peers are the ones most likely to have it.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/mod.rs:217`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L217) search_unknown_block takes peer_source
- [`beacon_node/network/src/sync/manager.rs:1066`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L1066) record_unknown_root collects reporting peers
- [`beacon_node/network/src/sync/block_lookups/mod.rs:841`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L841) add_peers_to_lookup_and_ancestors

**Sources.** [prysm#17754](https://github.com/OffchainLabs/prysm/pull/17754), [lodestar#9928](https://github.com/ChainSafe/lodestar/pull/9928)

</details>


<a id="lookup_sync-009"></a>
<details>
<summary><b>lookup_sync-009</b> One in-flight lookup per block root — <i>implemented · low · bandwidth, cpu, sync</i></summary>

**Idea.** Keep a set or state machine of in-flight lookups keyed by block root and skip creating another request for a root already being fetched or already queued (including delayed lookups and parent/child lookups). This removes duplicate concurrent downloads and processing of the same block.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/mod.rs:374`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L374) new_current_lookup finds existing lookup via is_for_block and only adds peers/components
- [`beacon_node/network/src/sync/block_lookups/mod.rs:256`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L256) search_parent_of_child reuses existing lookups
- [`beacon_node/network/src/sync/manager.rs:1043`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L1043) has_lookup_for_block

**Sources.** [lodestar@8e3b3c5fd](https://github.com/ChainSafe/lodestar/commit/8e3b3c5fd4bb), [lodestar#1699](https://github.com/ChainSafe/lodestar/pull/1699), [prysm#12903](https://github.com/OffchainLabs/prysm/pull/12903), [prysm#13013](https://github.com/OffchainLabs/prysm/pull/13013), [lighthouse#5655](https://github.com/sigp/lighthouse/pull/5655), [nimbus#5167](https://github.com/status-im/nimbus-eth2/pull/5167), [lighthouse#4668](https://github.com/sigp/lighthouse/pull/4668), [prysm#17353](https://github.com/OffchainLabs/prysm/pull/17353)

</details>


<a id="lookup_sync-010"></a>
<details>
<summary><b>lookup_sync-010</b> Skip lookup if block already received or processing — <i>implemented · low · bandwidth, cpu, sync</i></summary>

**Idea.** Before issuing a by-root request, check gossip-seen caches, the pre-import and data-availability caches, fork choice and recently completed lookups, and skip or suppress the lookup if the block is already there. Gossip-delivered blocks are then not downloaded again via RPC once per attestation.

**Best measured result.** Testing showed many more rpc_block than usual (no number) (pr:lighthouse#5681)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context.rs:706`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L706) block_lookup_request checks chain.get_block_process_status, skips if ExecutionValidated
- [`beacon_node/network/src/sync/network_context.rs:956`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L956) custody_lookup_request skips columns already cached in da_checker
- [`beacon_node/network/src/sync/manager.rs:1037`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L1037) should_search_for_block gate before unknown-root lookups
- [`beacon_node/network/src/sync/manager.rs:921`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L921) notified_unknown_roots dedup per (peer,root)

**Sources.** [prysm#16468](https://github.com/OffchainLabs/prysm/pull/16468), [lighthouse#5681](https://github.com/sigp/lighthouse/pull/5681), [lodestar#6292](https://github.com/ChainSafe/lodestar/pull/6292), [lighthouse#5682](https://github.com/sigp/lighthouse/pull/5682), [lighthouse#5840](https://github.com/sigp/lighthouse/pull/5840), [lighthouse#5722](https://github.com/sigp/lighthouse/pull/5722), [lighthouse#4732](https://github.com/sigp/lighthouse/pull/4732), [teku#7134](https://github.com/Consensys-Incorporated/teku/pull/7134), [prysm#9904](https://github.com/OffchainLabs/prysm/pull/9904), [lighthouse#5696](https://github.com/sigp/lighthouse/pull/5696)

</details>


<a id="lookup_sync-011"></a>
<details>
<summary><b>lookup_sync-011</b> Request deepest missing ancestor directly — <i>implemented · medium · sync, latency, bandwidth</i></summary>

**Idea.** When a block's parent is unknown, walk the locally held pending/queued blocks to the oldest missing ancestor and request only that root (processing queued parents first). This ends a parent-chain search in far fewer round trips than re-walking one block at a time.

**Best measured result.** "we found the previous block search never ended, so we sped it up" (pr:ethlambda#114)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/mod.rs:256`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L256) search_parent_of_child reuses existing lookups
- [`beacon_node/network/src/sync/block_lookups/mod.rs:643`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L643) on_lookup_result ParentUnknown triggers parent search
- [`beacon_node/network/src/sync/block_lookups/mod.rs:586`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L586) continue_child_lookups

**Sources.** [ethlambda#114](https://github.com/lambdaclass/ethlambda/pull/114), [nimbus#6112](https://github.com/status-im/nimbus-eth2/pull/6112), [lodestar#2165](https://github.com/ChainSafe/lodestar/pull/2165), [lighthouse#429](https://github.com/sigp/lighthouse/pull/429)

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

**Sources.** [prysm#2297](https://github.com/OffchainLabs/prysm/pull/2297), [lighthouse#1534](https://github.com/sigp/lighthouse/pull/1534), [nimbus#3312](https://github.com/status-im/nimbus-eth2/pull/3312), [nimbus#3331](https://github.com/status-im/nimbus-eth2/pull/3331), [nimbus#7006](https://github.com/status-im/nimbus-eth2/pull/7006), [nimbus#9288](https://github.com/status-im/nimbus-eth2/pull/9288)

</details>


<a id="lookup_sync-017"></a>
<details>
<summary><b>lookup_sync-017</b> Cap number of concurrent lookups — <i>implemented · low · memory</i></summary>

**Idea.** Put a hard cap on concurrent block lookups, so worst-case memory held by unvalidated lookup data stays bounded.

**Best measured result.** 200 lookups at most ~2 GB (pr:lighthouse#6015)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/mod.rs:77`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L77) const MAX_LOOKUPS: usize = 200
- [`beacon_node/network/src/sync/block_lookups/mod.rs:408`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L408) new_current_lookup drops when len &gt;= MAX_LOOKUPS

**Sources.** [lighthouse#6015](https://github.com/sigp/lighthouse/pull/6015)

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

**Sources.** [lodestar#8221](https://github.com/ChainSafe/lodestar/pull/8221)

</details>


<a id="lookup_sync-026"></a>
<details>
<summary><b>lookup_sync-026</b> Batch column by-root requests per peer — <i>implemented · medium · bandwidth, sync</i></summary>

**Idea.** Group missing data columns across columns and blocks into one by-root request per custodial peer (deterministic peer choice so requests coalesce), instead of one request per column or per block.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context/custody.rs:215`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L215) columns grouped per peer in columns_to_request_by_peer
- [`beacon_node/network/src/sync/network_context/custody.rs:252`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L252) one data_column_lookup_request per peer with block_roots and indices lists
- [`beacon_node/network/src/sync/network_context/custody.rs:353`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L353) select_column_peer uses a per-request deterministic hasher to coalesce

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

**Sources.** [nimbus#7477](https://github.com/status-im/nimbus-eth2/pull/7477), [nimbus#7492](https://github.com/status-im/nimbus-eth2/pull/7492)

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

**Sources.** [nimbus#7461](https://github.com/status-im/nimbus-eth2/pull/7461)

</details>


<a id="lookup_sync-040"></a>
<details>
<summary><b>lookup_sync-040</b> Avoid retrying failed peers in lookups — <i>implemented · low · bandwidth, sync</i></summary>

**Idea.** Remember per root (or per column) which peers failed or returned empty, cap retries per peer and exclude or deprioritise them when picking the retry peer, resetting when all are exhausted. Retries then spread over peers that may have the data instead of looping on the same one.

**Best measured result.** Retry storm: 131 WARN retries over 56 roots in ~35 s on one node, peers hit 45+ times (pr:ethlambda#186)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/single_block_lookup.rs:777`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/single_block_lookup.rs#L777) failed_peers HashSet per request
- [`beacon_node/network/src/sync/block_lookups/single_block_lookup.rs:890`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/single_block_lookup.rs#L890) record_failed_peer
- [`beacon_node/network/src/sync/network_context.rs:722`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L722) block_lookup_request de-prioritizes failed peers
- [`beacon_node/network/src/sync/network_context/custody.rs:398`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L398) MAX_CUSTODY_PEER_ATTEMPTS and select_column_peer attempt-count ordering
- [`beacon_node/network/src/sync/block_lookups/single_block_lookup.rs:917`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/single_block_lookup.rs#L917) SINGLE_BLOCK_LOOKUP_MAX_ATTEMPTS

**Sources.** [lighthouse#9542](https://github.com/sigp/lighthouse/pull/9542), [ethlambda#186](https://github.com/lambdaclass/ethlambda/pull/186), [lighthouse#6084](https://github.com/sigp/lighthouse/pull/6084), [lighthouse#8005](https://github.com/sigp/lighthouse/pull/8005)

</details>


<a id="lookup_sync-052"></a>
<details>
<summary><b>lookup_sync-052</b> Do not start RPC lookups from partial gossip — <i>implemented · low · S · bandwidth, cpu</i></summary>

**Idea.** When gossip has delivered only a block or one blob, do not start a delayed RPC lookup for the rest; let gossip deliver it, avoiding double downloads.

**Impact.** Already avoids double downloads from partial gossip; nothing further to gain.

**Best measured result.** RPC takes ~1s; delayed lookups often double download (pr:lighthouse#4992)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1016`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1016) MissingComponents for gossip column only traces and checks reconstruction, no lookup
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1972`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1972) MissingComponents for gossip block only traces, no sync message
- [`beacon_node/network/src/sync/manager.rs:886`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L886) lookups only start on UnknownParent*/attestation-referenced unknown root

**Sources.** [lighthouse#4992](https://github.com/sigp/lighthouse/pull/4992)

</details>


