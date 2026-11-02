# data_availability

97 ideas: 17 not, 18 partial, 55 implemented, 7 n/a; 28 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

The area has 163 numbered ideas; the 66 ids missing here have not been checked against Lighthouse yet.

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [data_availability-001](#data_availability-001) | Fetch blobs from EL on gossip block arrival | implemented | high |  | latency, bandwidth, sync |
| [data_availability-002](#data_availability-002) **★** | Query EL first, request only remaining blobs from peers | partial | medium | S | latency, bandwidth |
| [data_availability-003](#data_availability-003) **★** | Trigger getBlobs on first gossip column sidecar | partial | medium | S | latency, bandwidth |
| [data_availability-004](#data_availability-004) | Call getBlobs before block verification completes | implemented | medium |  | latency, bandwidth |
| [data_availability-005](#data_availability-005) | Fetch blobs from EL during block lookup sync | implemented | medium |  | latency, bandwidth |
| [data_availability-011](#data_availability-011) **★** | Build only custodied columns from EL blobs | partial | medium | S | cpu, memory |
| [data_availability-012](#data_availability-012) **★** | Publish recovered columns off the availability path | partial | medium | S | latency, bandwidth |
| [data_availability-013](#data_availability-013) | Publish only needed columns after reconstruction | implemented | medium |  | cpu, bandwidth |
| [data_availability-014](#data_availability-014) **★** | Mark data available at 50% columns | not | medium | M | latency, bandwidth, sync |
| [data_availability-015](#data_availability-015) | Reconstruct remaining columns locally from half | implemented | medium |  | cpu, latency, bandwidth, sync |
| [data_availability-016](#data_availability-016) | Delay column reconstruction, bounded by slot deadline | implemented | low |  | cpu, latency, sync |
| [data_availability-018](#data_availability-018) | Reconstruct only on nodes custodying at least half | implemented | low |  | cpu |
| [data_availability-019](#data_availability-019) | Run column reconstruction at most once per block | implemented | medium |  | cpu, memory, disk |
| [data_availability-020](#data_availability-020) | Dedicated thread pool for column reconstruction | implemented | medium |  | cpu, latency |
| [data_availability-021](#data_availability-021) | Run KZG and reconstruction off async and fork-choice threads | implemented | medium |  | cpu, latency |
| [data_availability-022](#data_availability-022) | Parallel, bounded per-blob cell recovery | implemented | medium | S | cpu, memory, latency |
| [data_availability-023](#data_availability-023) | Semi-supernode: custody half the columns | implemented | high |  | cpu, disk, bandwidth |
| [data_availability-024](#data_availability-024) | Custody first half of columns to skip reconstruction | n/a | medium | S | cpu, bandwidth |
| [data_availability-025](#data_availability-025) **★** | Background reconstruction of historical custody columns | not | medium | L | cpu, disk, bandwidth |
| [data_availability-027](#data_availability-027) | Share blobs, cells and sidecars by reference | implemented | medium | S | cpu, memory |
| [data_availability-030](#data_availability-030) | Quarantine blobs with blobless blocks until joined | implemented | medium | S | memory, latency, bandwidth, sync |
| [data_availability-031](#data_availability-031) **★** | Cache columns with unknown parent block | not | medium | M | latency, sync |
| [data_availability-032](#data_availability-032) | Per-root indexed sidecar quarantine lookups | implemented | low |  | cpu |
| [data_availability-033](#data_availability-033) | Cache custody column set per node | implemented | low | S | cpu |
| [data_availability-034](#data_availability-034) | Batch KZG verify sidecars from RPC and sync | implemented | medium | S | cpu, latency, sync |
| [data_availability-035](#data_availability-035) **★** | Batch gossip column verification per block | not | medium | M | cpu, latency |
| [data_availability-036](#data_availability-036) | Combine by-root sidecar requests per peer | implemented | medium |  | bandwidth, sync |
| [data_availability-038](#data_availability-038) | Request columns only from custody peers | implemented | medium |  | bandwidth, sync |
| [data_availability-039](#data_availability-039) **★** | Hedge slow column requests to alternate peers | not | medium | M | latency, sync |
| [data_availability-042](#data_availability-042) | Sidecar validation without state advancement | implemented | medium |  | cpu, memory, latency |
| [data_availability-044](#data_availability-044) | Prune blob and column data past DA window | implemented | medium | L | disk |
| [data_availability-045](#data_availability-045) | Derive column retention window from chain config | implemented | low | S | disk |
| [data_availability-048](#data_availability-048) | Incremental capped low-priority blob pruning | partial | low | S | cpu, disk, latency |
| [data_availability-054](#data_availability-054) **★** | Skip re-verifying already verified sidecars | partial | medium | S | cpu, latency |
| [data_availability-055](#data_availability-055) | Drop sidecars and fetches for imported blocks | partial | low | S | cpu, memory, bandwidth |
| [data_availability-056](#data_availability-056) | Bound or fail fast on DA wait | n/a | medium |  | latency, sync |
| [data_availability-058](#data_availability-058) | Run DA check concurrently with block verification | implemented | medium |  | latency |
| [data_availability-061](#data_availability-061) | Track received columns to skip duplicate work | implemented | medium |  | cpu, disk, bandwidth |
| [data_availability-063](#data_availability-063) **★** | Delay RPC fetch of missing sidecars | partial | medium | S | latency, bandwidth, sync |
| [data_availability-065](#data_availability-065) **★** | Pull late block when blobs arrive first | partial | medium | S | latency |
| [data_availability-067](#data_availability-067) **★** | Fetch missing columns within the slot | partial | medium | M | latency |
| [data_availability-069](#data_availability-069) | Disk-backed blob quarantine | n/a | medium |  | memory, disk |
| [data_availability-070](#data_availability-070) | Memory-only bounded LRU for pending components | implemented | medium |  | memory, disk |
| [data_availability-075](#data_availability-075) | Evict DA entries exactly when import completes | partial | low | S | cpu, memory, disk, latency, bandwidth, sync |
| [data_availability-077](#data_availability-077) | Free column recovery state promptly | n/a | medium |  | cpu, memory |
| [data_availability-078](#data_availability-078) | Import only when blob count equals commitments | implemented | low | S | latency |
| [data_availability-079](#data_availability-079) | Drop gossip columns outside sampling set | implemented | medium |  | cpu, disk, bandwidth |
| [data_availability-080](#data_availability-080) | Correct proposer cache key in blob verification | implemented | medium |  | cpu, latency |
| [data_availability-085](#data_availability-085) | Skip KZG and proof checks for EL-built columns | implemented | medium |  | cpu, latency |
| [data_availability-086](#data_availability-086) | Cache column inclusion proof results | not | low | S | cpu |
| [data_availability-087](#data_availability-087) | Late DA check with per-block sampling tracker | implemented | medium |  | disk, latency, bandwidth |
| [data_availability-088](#data_availability-088) **★** | Re-call getBlobs until block columns are complete | not | medium | S | latency, bandwidth |
| [data_availability-090](#data_availability-090) **★** | Allow column reconstruction while not synced | not | medium | M | sync, bandwidth |
| [data_availability-092](#data_availability-092) | Compute sidecar inclusion proofs from shared merkle subtrees | implemented | medium |  | cpu, memory |
| [data_availability-093](#data_availability-093) | Validate column sidecars at mid processor priority | implemented | medium |  | latency |
| [data_availability-094](#data_availability-094) | Fetch column subsets from many peers in parallel | implemented | medium |  | sync, bandwidth |
| [data_availability-095](#data_availability-095) **★** | Give reconstruction a multi-thread worker allocation | partial | medium | S | cpu, latency |
| [data_availability-096](#data_availability-096) **★** | Reconstruct only when needed columns are missing | partial | medium | S | cpu |
| [data_availability-097](#data_availability-097) | No reconstruction when serving column RPC | implemented | medium |  | cpu, latency |
| [data_availability-099](#data_availability-099) | Run gossip column KZG verification on blocking pool | implemented | medium |  | latency, cpu |
| [data_availability-100](#data_availability-100) | Operator flags to skip EL or blob handling | not | low | M | disk, bandwidth |
| [data_availability-101](#data_availability-101) | Mark columns available before disk write completes | n/a | low | S | latency |
| [data_availability-103](#data_availability-103) **★** | Overflow pending DA cache to disk | not | medium | L | memory |
| [data_availability-105](#data_availability-105) | Compute column sidecars from blobs in parallel | implemented | medium |  | cpu, latency |
| [data_availability-108](#data_availability-108) | Reconstruct only requested blobs for blob API | implemented | low |  | cpu, latency |
| [data_availability-109](#data_availability-109) | Request only custody cells from EL getBlobs | implemented | medium |  | bandwidth, cpu |
| [data_availability-110](#data_availability-110) | Partial data column dissemination at cell granularity | implemented | high |  | bandwidth, latency |
| [data_availability-112](#data_availability-112) | Cooldown peers that return empty column responses | not | low | S | bandwidth, sync |
| [data_availability-113](#data_availability-113) | Filter column request peers by earliest available slot | implemented | medium |  | sync |
| [data_availability-114](#data_availability-114) **★** | Rank column peers by historical response rate | not | medium | S | sync |
| [data_availability-116](#data_availability-116) | Prune stale DA and quarantine entries by finality or expiry | implemented | medium |  | memory |
| [data_availability-117](#data_availability-117) **★** | Store only original columns and rebuild extension on demand | not | high | M | disk |
| [data_availability-118](#data_availability-118) | Clean legacy unpruned column buckets at startup | n/a | low | S | disk |
| [data_availability-120](#data_availability-120) | Skip rebroadcast of columns already seen on gossip | implemented | medium |  | bandwidth, cpu |
| [data_availability-122](#data_availability-122) | Query columns by slot range during sync | implemented | medium |  | sync, bandwidth |
| [data_availability-123](#data_availability-123) | Reconstruct without holding the DA cache lock | implemented | low |  | latency |
| [data_availability-125](#data_availability-125) **★** | Wall-clock timeout on column reconstruction | not | medium | S | latency |
| [data_availability-126](#data_availability-126) **★** | Minimum custody with full-subnet sampling mode | partial | medium | M | bandwidth |
| [data_availability-129](#data_availability-129) | Gloas: check DA on the envelope, not the block | implemented | medium |  | latency |
| [data_availability-133](#data_availability-133) | Shorter per-request lifecycle for column recovery | n/a | low | S | memory |
| [data_availability-134](#data_availability-134) | Pool and retry data-unavailable blocks | implemented | medium |  | bandwidth, sync |
| [data_availability-136](#data_availability-136) | Read-only head state for sidecar verification | implemented | medium |  | cpu, memory |
| [data_availability-141](#data_availability-141) **★** | Single shared buffer for all column sources | partial | medium | M | memory |
| [data_availability-142](#data_availability-142) **★** | Singleflight proposer signature verification | partial | medium | S | cpu |
| [data_availability-143](#data_availability-143) | Skip DA check outside blob retention window | implemented | medium |  | sync, bandwidth |
| [data_availability-145](#data_availability-145) | Skip custody group derivation for supernodes | implemented | low |  | cpu |
| [data_availability-148](#data_availability-148) | Skip DA work for blocks without blob commitments | implemented | low |  | cpu |
| [data_availability-149](#data_availability-149) | Skip publishing columns while syncing | implemented | medium |  | bandwidth, cpu |
| [data_availability-150](#data_availability-150) | Skip EL column compute for imported blocks | implemented | medium |  | cpu |
| [data_availability-152](#data_availability-152) | Store blobs Snappy-compressed as on the wire | not | low | S | disk, cpu |
| [data_availability-154](#data_availability-154) **★** | Staged blob reconstruction: concatenate first | partial | medium | S | cpu, bandwidth |
| [data_availability-155](#data_availability-155) | Smaller pending-components cache capacity | implemented | medium |  | memory |
| [data_availability-156](#data_availability-156) | Persist only custody columns | implemented | medium |  | disk |
| [data_availability-158](#data_availability-158) **★** | Minimum custody until synced | partial | medium | M | sync, bandwidth, disk |
| [data_availability-161](#data_availability-161) **★** | Use EL blobs until block data is imported | not | medium | S | bandwidth, latency |
| [data_availability-162](#data_availability-162) **★** | Verify availability-critical columns first | not | medium | S | latency |
| [data_availability-163](#data_availability-163) | Verify sidecars before persisting | implemented | medium |  | disk |

★ actionable. Click an id for the full record.

## Ideas

<a id="data_availability-001"></a>
<details>
<summary><b>data_availability-001</b> Fetch blobs from EL on gossip block arrival — <i>implemented · high · latency, bandwidth, sync</i></summary>

**Idea.** When a gossip block with blob commitments arrives, call engine_getBlobs on the local EL and build the blob/data column sidecars from the response. The block becomes available without waiting for the sidecars from gossip or peers.

**Impact.** none needed

**Evidence (Lighthouse @ 928b61e719).**

- network/src/network_beacon_processor/gossip_methods.rs:1930 spawn_fetch_block_columns on gossip-valid block
- beacon_chain/src/fetch_blobs/mod.rs:132 fetch_and_process_engine_blobs_inner (getBlobsV2/V3/V4, builds columns)

**Sources.** [nimbus#7123](https://github.com/status-im/nimbus-eth2/pull/7123), [lodestar#7679](https://github.com/ChainSafe/lodestar/pull/7679), [prysm#15483](https://github.com/OffchainLabs/prysm/pull/15483), [caplin#25447](https://github.com/erigontech/erigon/pull/25447), [grandine#79](https://github.com/grandinetech/grandine/pull/79), [lodestar#7134](https://github.com/ChainSafe/lodestar/pull/7134), [nimbus#7866](https://github.com/status-im/nimbus-eth2/pull/7866)

</details>


<a id="data_availability-002"></a>
<details>
<summary><b>data_availability-002</b> Query EL first, request only remaining blobs from peers — <i>partial · medium · S · latency, bandwidth</i></summary>

**Idea.** When blobs or columns for a block are missing, query the local EL first and send RPC requests to peers only for the ones still missing. Share one received-sidecar set between the EL and the p2p fetch paths so no sidecar is fetched twice.

**Gap in Lighthouse.** The peer request is not deferred until the EL result is known: both run at once, and ActiveCustodyRequest never re-checks the DA cache, so columns the EL supplies are still downloaded from peers. Make the lookup's DataRequest wait for block processing (which already awaits getBlobs) before calling custody_lookup_request, or re-filter indices against cached_data_column_indexes before each peer request.

**Impact.** Saves redundant column download on lookups of blocks whose blobs are in the local mempool; small since gossip blocks (the common case) already trigger EL first and lookups are rare.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/block_lookups/single_block_lookup.rs:397-433`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/single_block_lookup.rs#L397-L433) custody_lookup_request is issued as soon as the block is downloaded, in the same continue_requests call that sends the block to processing
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:209-224`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L209-L224) EL getBlobs is awaited inside RPC block processing, after MissingComponents, in parallel with the peer column request
- [`beacon_node/network/src/sync/network_context.rs:970-990`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L970-L990) custody_lookup_request skips only columns already in the DA cache (cached_data_column_indexes) at send time
- [`beacon_node/network/src/sync/network_context/custody.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs) (no DA-cache re-check on retries or after EL import)

**Sources.** [teku#8663](https://github.com/Consensys-Incorporated/teku/pull/8663), [grandine@a850e357b](https://github.com/grandinetech/grandine/commit/a850e357b76b), [grandine#114](https://github.com/grandinetech/grandine/pull/114), [teku#8927](https://github.com/Consensys-Incorporated/teku/pull/8927)

</details>


<a id="data_availability-003"></a>
<details>
<summary><b>data_availability-003</b> Trigger getBlobs on first gossip column sidecar — <i>partial · medium · S · latency, bandwidth</i></summary>

**Idea.** Start the EL getBlobs fetch when the first valid data column sidecar arrives on gossip, also before its block arrives. The missing columns are then built from EL blobs sooner than with a trigger on block arrival only.

**Gap in Lighthouse.** There is no trigger on the first full Fulu DataColumnSidecar seen before its block (for example from peers that do not use partial messages, or with partial columns turned off). Fix: call fetch_engine_blobs_and_publish_full from process_gossip_verified_data_column with a PartialHeaderOrBid built from the sidecar's signed header, behind a per-block-root in-flight guard.

**Impact.** Only helps when a full column arrives before both the block and any partial header; with partial columns on by default this ordering is rare.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1117-1134`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1117-L1134) getBlobs is triggered on the first uncached Fulu partial-column header
- [`beacon_node/src/cli.rs:693-701`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L693-L701) enable-partial-columns defaults to true, so this trigger is active by default
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:926-1047`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L926-L1047) the full DataColumnSidecar gossip handler never calls fetch_engine_blobs_and_publish_full
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1066-1069`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1066-L1069) Gloas triggers getBlobs on the bid instead
- [`beacon_node/network/src/network_beacon_processor/mod.rs:960-1020`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L960-L1020) the only other triggers are a gossip/RPC/HTTP block (spawn_fetch_block_columns) and a lookup block

**Sources.** [lighthouse#7329](https://github.com/sigp/lighthouse/pull/7329), [nimbus#8393](https://github.com/status-im/nimbus-eth2/pull/8393)

</details>


<a id="data_availability-004"></a>
<details>
<summary><b>data_availability-004</b> Call getBlobs before block verification completes — <i>implemented · medium · latency, bandwidth</i></summary>

**Idea.** Start the EL getBlobs fetch as soon as a gossip block header is seen, before consensus and execution verification of the block. The local blobs then win the race against gossip and can be published.

**Impact.** n/a

**Best measured result.** 116 hits and 156 blobs published in 30 min on mainnet, up from a few hits per hour (pr:lighthouse#6600)

**Evidence (Lighthouse @ 928b61e719).**

- network/src/network_beacon_processor/gossip_methods.rs:1930 spawn_fetch_block_columns called before chain.process_block (before full verification, spawned async)

**Sources.** [lighthouse#6600](https://github.com/sigp/lighthouse/pull/6600)

</details>


<a id="data_availability-005"></a>
<details>
<summary><b>data_availability-005</b> Fetch blobs from EL during block lookup sync — <i>implemented · medium · latency, bandwidth</i></summary>

**Idea.** In unknown-block / lookup sync for a block by root, also try engine_getBlobs before requesting blobs or columns from peers. Availability can then resolve locally without RPC.

**Impact.** n/a

**Evidence (Lighthouse @ 928b61e719).**

- network/src/network_beacon_processor/sync_methods.rs:208-225 after RPC/lookup block returns MissingComponents, fetch_engine_blobs_and_publish_full(..., EnvelopeSource::Rpc)

**Sources.** [lodestar#7724](https://github.com/ChainSafe/lodestar/pull/7724)

</details>


<a id="data_availability-011"></a>
<details>
<summary><b>data_availability-011</b> Build only custodied columns from EL blobs — <i>partial · medium · S · cpu, memory</i></summary>

**Idea.** When data column sidecars are built from EL blobs, compute only the columns that the node custodies (column bitmap), not all 128 columns that are then filtered.

**Gap in Lighthouse.** On the V2/V3 path, pass the custody index set into blobs_to_partial_data_columns / build_partial_column_cells so only custody columns are assembled (cells+proofs copied, sidecars built). compute_cells still has to run the full extension per blob, so only assembly/clone/alloc work is saved. The V4 path already does this.

**Impact.** Small CPU/alloc saving per block for non-supernodes on ELs without getBlobsV4; nothing on V4 ELs or supernodes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:158`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L158) engine_getBlobsV4 path requests and assembles only custody columns
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:686`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L686) V2/V3 path calls blobs_to_partial_data_columns with no custody set
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:700`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L700) filters to custody_columns_indices only after all columns are built
- [`beacon_node/beacon_chain/src/kzg_utils.rs:425`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L425) blobs_to_partial_data_columns signature has no column filter
- [`beacon_node/beacon_chain/src/kzg_utils.rs:725`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L725) build_partial_column_cells allocates and fills all number_of_columns columns

**Second check.** Re-read the V4 dispatch and the full V2/V3 builder chain down to build_partial_column_cells; it loops over all 128 columns, and the custody filter only runs afterwards. Found no other column-subset builder.

**Sources.** [nimbus#8672](https://github.com/status-im/nimbus-eth2/pull/8672)

</details>


<a id="data_availability-012"></a>
<details>
<summary><b>data_availability-012</b> Publish recovered columns off the availability path — <i>partial · medium · S · latency, bandwidth</i></summary>

**Idea.** Publish columns recovered from EL blobs or reconstruction in a detached task after storing them, so block import and DA completion do not wait on network sends. Coalesce repeated partial publishes per (block, column).

**Gap in Lighthouse.** Publishing is already off the DA path. Repeated partial publishes per (block, column) are partly deduped in the gossipsub partial-messages extension (stale publishes are dropped, peers get only deltas), but there is no time-window coalescing like prysm#17791's 250 ms batch: each merge that adds cells still triggers its own send to every peer. Add a short debounce keyed by (block_root, column) before PublishPartialColumns if chatter is measured to matter.

**Impact.** Fewer small partial-column RPCs when many partial updates arrive for one column within a short window; no DA latency gain (already non-blocking).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/mod.rs:1213`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L1213) reconstruction result published via publish_data_columns_gradually (spawned) while import status is handled independently
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:357`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L357) publish_fn is a non-blocking callback before process of engine columns
- [`beacon_node/network/src/service.rs:689`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L689) PublishPartialColumns handled on the network task, not on the import path
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1404`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1404) PublishPartialColumns sent on every merge that updates partials
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/extensions/partial_messages.rs:497 handle_publish skips a publish whose metadata adds no new parts for that (topic, group_id)
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/extensions/partial_messages.rs:536 per-peer publish_action sends only what the peer lacks

**Second check.** Beyond the earlier review, read lighthouse_network publish_partial and the pinned sigp rust-libp2p gossipsub partial_messages handle_publish: it drops no-new-data publishes and diffs per peer, which covers part of the coalescing idea but not timed batching. The prysm coalescing PR is itself still open.

**Sources.** [nimbus#8655](https://github.com/status-im/nimbus-eth2/pull/8655), [prysm#17791](https://github.com/OffchainLabs/prysm/pull/17791)

</details>


<a id="data_availability-013"></a>
<details>
<summary><b>data_availability-013</b> Publish only needed columns after reconstruction — <i>implemented · medium · cpu, bandwidth</i></summary>

**Idea.** After columns are recovered from EL blobs or by reconstruction, publish to gossip only the missing columns the node custodies or samples and the network still needs, not every recovered column. This saves outbound bandwidth and send CPU.

**Impact.** Already saves outbound bandwidth and send CPU on reconstruction.

**Best measured result.** 'a node custodying 65 columns published at least 64 columns per reconstruction' before (pr:lodestar#9464)

**Evidence (Lighthouse @ 928b61e719).**

- beacon_chain/src/data_availability_checker.rs:597 filters reconstructed columns to sampling columns not already in cache
- network/src/network_beacon_processor/mod.rs:1305 observe_gossip_data_column drops already-seen columns before each batch publish

**Sources.** [nimbus#8648](https://github.com/status-im/nimbus-eth2/pull/8648), [lodestar#9464](https://github.com/ChainSafe/lodestar/pull/9464), [lighthouse#8269](https://github.com/sigp/lighthouse/pull/8269)

</details>


<a id="data_availability-014"></a>
<details>
<summary><b>data_availability-014</b> Mark data available at 50% columns — <i>not · medium · M · latency, bandwidth, sync</i></summary>

**Idea.** On nodes that custody all columns, treat a block as data-available once at least 50% of columns are verified (enough to reconstruct), and import it before reconstruction of the rest completes.

**Gap in Lighthouse.** lighthouse#7598 was closed unmerged. To implement, add an availability path for supernodes that succeeds with &gt;= number_of_columns/2 verified columns, import to fork choice, then fill the rest by reconstruction; DB column writes, custody/sampling checks and RPC serving must tolerate columns arriving after import.

**Impact.** Supernodes import one reconstruction time earlier (hundreds of ms) when gossip delivers 50-99% of columns; none for non-supernodes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:214`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L214) make_available requires received == num_expected_columns
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:710`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L710) get_num_expected_columns = num_of_data_columns_to_sample (128 on supernodes)
- beacon_node/beacon_chain/src/validator_custody.rs:492 should_attempt_reconstruction uses the 50% threshold only to start reconstruction
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3785`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3785) reconstruct_data_columns imports availability only after reconstruction completes

**Second check.** Checked the expected-column count source (custody context sampling size, no supernode reduction) and searched the DA checker for any half-threshold availability variant; the 50% value is only used to trigger reconstruction.

**Sources.** [nimbus#8417](https://github.com/status-im/nimbus-eth2/pull/8417), [lighthouse#7598](https://github.com/sigp/lighthouse/pull/7598), [teku#10248](https://github.com/Consensys-Incorporated/teku/pull/10248), [grandine#424](https://github.com/grandinetech/grandine/pull/424), [lodestar#8408](https://github.com/ChainSafe/lodestar/pull/8408), [lodestar#8818](https://github.com/ChainSafe/lodestar/pull/8818)

</details>


<a id="data_availability-015"></a>
<details>
<summary><b>data_availability-015</b> Reconstruct remaining columns locally from half — <i>implemented · medium · cpu, latency, bandwidth, sync</i></summary>

**Idea.** Once at least 50% of a block's data columns are held, recover the missing columns by erasure-coding cell recovery in the data availability layer, then store and publish them. This is faster than waiting for gossip or requesting every column by root from peers.

**Impact.** Already recovers missing columns locally via cell recovery.

**Best measured result.** &lt;800ms to recover with 20 blobs (pr:lodestar#7940)

**Evidence (Lighthouse @ 928b61e719).**

- beacon_chain/src/data_availability_checker.rs:537 reconstruct_data_columns using KzgVerifiedCustodyDataColumn::reconstruct_columns
- beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:620 trigger at &gt;= total/2 columns
- network/src/network_beacon_processor/gossip_methods.rs:1488 check_reconstruction_trigger

**Sources.** [lighthouse#5781](https://github.com/sigp/lighthouse/pull/5781), [prysm#15454](https://github.com/OffchainLabs/prysm/pull/15454), [lodestar#7940](https://github.com/ChainSafe/lodestar/pull/7940), [lodestar#7935](https://github.com/ChainSafe/lodestar/pull/7935), [teku#10224](https://github.com/Consensys-Incorporated/teku/pull/10224), [prysm#17053](https://github.com/OffchainLabs/prysm/pull/17053), [nimbus#6481](https://github.com/status-im/nimbus-eth2/pull/6481), [prysm#15593](https://github.com/OffchainLabs/prysm/pull/15593), [grandine#220](https://github.com/grandinetech/grandine/pull/220), [nimbus#6553](https://github.com/status-im/nimbus-eth2/pull/6553)

</details>


<a id="data_availability-016"></a>
<details>
<summary><b>data_availability-016</b> Delay column reconstruction, bounded by slot deadline — <i>implemented · low · cpu, latency, sync</i></summary>

**Idea.** After reaching 50% of columns, wait a short (configurable or randomized) delay before reconstructing, and reconstruct only if columns are still missing, with the maximum delay a fraction of slot time so it ends before the attestation deadline. Missing columns often arrive via gossip or getBlobs, and reconstruction is CPU-heavy.

**Impact.** Avoids redundant CPU-heavy reconstructions when columns arrive late via gossip/getBlobs.

**Best measured result.** reduces the unnecessary amount of reconstructions during fast block import (commit:grandine@9e43a4aea5ad)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:73`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L73) QUEUED_RECONSTRUCTION_DELAY 150ms
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:1139-1165`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L1139-L1165) DelayColumnReconstruction with slot-fraction deadline, resets delay on new column
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1488`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1488) check_reconstruction_trigger
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:592`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L592) skips if all sampling columns arrived

**Sources.** [lighthouse#7588](https://github.com/sigp/lighthouse/pull/7588), [grandine@9e43a4aea](https://github.com/grandinetech/grandine/commit/9e43a4aea5ad), [grandine#526](https://github.com/grandinetech/grandine/pull/526), [grandine@4f7f8f0ae](https://github.com/grandinetech/grandine/commit/4f7f8f0ae248), [prysm#15705](https://github.com/OffchainLabs/prysm/pull/15705), [lighthouse#7976](https://github.com/sigp/lighthouse/pull/7976), [lighthouse#8067](https://github.com/sigp/lighthouse/pull/8067)

</details>


<a id="data_availability-018"></a>
<details>
<summary><b>data_availability-018</b> Reconstruct only on nodes custodying at least half — <i>implemented · low · cpu</i></summary>

**Idea.** Enable column reconstruction only when the node samples or custodies at least 50% of columns (including validator-custody supernodes), with a dynamically computed reconstruction timeout. Other nodes skip it because recovery cannot succeed.

**Impact.** Nodes below 50% custody never attempt reconstruction; the delay is derived from slot duration.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/custody_context.rs:492`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L492) should_attempt_reconstruction requires sampling count &gt; 50% of columns
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1488-1492`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1488-L1492) gate before scheduling
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:620`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L620) requires received &gt;= half

**Sources.** [nimbus#7628](https://github.com/status-im/nimbus-eth2/pull/7628), [nimbus#7558](https://github.com/status-im/nimbus-eth2/pull/7558), [teku#9994](https://github.com/Consensys-Incorporated/teku/pull/9994), [lighthouse#8052](https://github.com/sigp/lighthouse/pull/8052)

</details>


<a id="data_availability-019"></a>
<details>
<summary><b>data_availability-019</b> Run column reconstruction at most once per block — <i>implemented · medium · cpu, memory, disk</i></summary>

**Idea.** Record per block root that reconstruction was dispatched, is in flight or is complete (flag or lock taken before checking column counts), and return immediately on new triggers. Share one reconstruction result across concurrent requesters.

**Impact.** Already avoids duplicate reconstructions per block root.

**Best measured result.** duplicate rate 4-6% to 0 in test (pr:lighthouse#8985)

**Evidence (Lighthouse @ 928b61e719).**

- beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:614 reconstruction_started flag checked and set under write lock
- beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:631 flag reset only on failure
- beacon_chain/src/pending_payload_cache/mod.rs:622 same for Gloas
- beacon_chain/src/beacon_chain.rs:3798 early return if block data already imported

**Sources.** [lighthouse#8855](https://github.com/sigp/lighthouse/pull/8855), [lighthouse#8923](https://github.com/sigp/lighthouse/pull/8923), [lighthouse#8985](https://github.com/sigp/lighthouse/pull/8985), [lodestar#8383](https://github.com/ChainSafe/lodestar/pull/8383), [teku#11508](https://github.com/Consensys-Incorporated/teku/pull/11508), [teku#10296](https://github.com/Consensys-Incorporated/teku/pull/10296), [prysm#15528](https://github.com/OffchainLabs/prysm/pull/15528), [lighthouse#5794](https://github.com/sigp/lighthouse/pull/5794)

</details>


<a id="data_availability-020"></a>
<details>
<summary><b>data_availability-020</b> Dedicated thread pool for column reconstruction — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** Run data column computation and cell recovery on a dedicated (high-priority) thread pool, separate from the general pool and the fork choice/block import threads, so heavy KZG work does not starve other tasks.

**Impact.** Already isolates KZG cell recovery on a dedicated pool.

**Best measured result.** reduces p99 latency during high load (commit:grandine@9af9e4de859b)

**Evidence (Lighthouse @ 928b61e719).**

- [`common/task_executor/src/rayon_pool_provider.rs:9`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/task_executor/src/rayon_pool_provider.rs#L9) RayonPoolType::HighPriority pool
- beacon_chain/src/beacon_chain.rs:3811 and :3845 reconstruction runs via spawn_blocking_with_rayon_async(HighPriority)

**Sources.** [grandine@9af9e4de8](https://github.com/grandinetech/grandine/commit/9af9e4de859b), [grandine@79f20c521](https://github.com/grandinetech/grandine/commit/79f20c52179d), [grandine#362](https://github.com/grandinetech/grandine/pull/362), [lighthouse#8075](https://github.com/sigp/lighthouse/pull/8075)

</details>


<a id="data_availability-021"></a>
<details>
<summary><b>data_availability-021</b> Run KZG and reconstruction off async and fork-choice threads — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** Call PeerDAS KZG and column reconstruction (including from EL blobs and for the beacon API) in blocking tasks or a background pool, off the async runtime and the single-threaded fork choice mutator. Do not spawn a new validation task per column for the same delayed block.

**Impact.** Already keeps PeerDAS KZG off the async runtime; Lighthouse has no single-threaded fork choice mutator to starve.

**Evidence (Lighthouse @ 928b61e719).**

- beacon_chain/src/beacon_chain.rs:2457 gossip column KZG verification in spawn_blocking_handle
- beacon_chain/src/fetch_blobs/mod.rs:671 EL-blob column computation in spawn_blocking_handle
- http_api/src/publish_blocks.rs:444 build_data_columns in spawn_blocking_handle
- beacon_chain/src/beacon_chain.rs:3845 reconstruction on rayon pool
- http_api/src/task_spawner.rs:86 beacon API blob reconstruction runs via blocking_response_task

**Sources.** [teku#9728](https://github.com/Consensys-Incorporated/teku/pull/9728), [grandine@5d83807db](https://github.com/grandinetech/grandine/commit/5d83807db95f), [grandine@e53a535e1](https://github.com/grandinetech/grandine/commit/e53a535e114c), [nimbus#8346](https://github.com/status-im/nimbus-eth2/pull/8346), [grandine#364](https://github.com/grandinetech/grandine/pull/364), [grandine@00e4af612](https://github.com/grandinetech/grandine/commit/00e4af612278)

</details>


<a id="data_availability-022"></a>
<details>
<summary><b>data_availability-022</b> Parallel, bounded per-blob cell recovery — <i>implemented · medium · S · cpu, memory, latency</i></summary>

**Idea.** Split column reconstruction into independent per-blob cell and proof recoveries and run them in parallel on worker tasks with a bounded number in flight, using zero-copy views of inputs and reused buffers. This cuts latency while limiting peak memory and scheduling overhead.

**Impact.** Already parallel per blob; only buffer reuse left, small gain.

**Best measured result.** logs show recovery ~644ms per blob index run concurrently (pr:prysm#14236)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/kzg_utils.rs:905`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L905) reconstruct_data_columns uses into_par_iter per blob row on bounded rayon pool
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3785`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3785) reconstruct_data_columns runs on task executor
- [`beacon_node/beacon_chain/src/kzg_utils.rs:767`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L767) reconstruct_blobs_with_indices also per blob

**Sources.** [nimbus#7758](https://github.com/status-im/nimbus-eth2/pull/7758), [nimbus#7800](https://github.com/status-im/nimbus-eth2/pull/7800), [prysm#14397](https://github.com/OffchainLabs/prysm/pull/14397), [nimbus#7351](https://github.com/status-im/nimbus-eth2/pull/7351), [nimbus#7428](https://github.com/status-im/nimbus-eth2/pull/7428), [prysm#14236](https://github.com/OffchainLabs/prysm/pull/14236)

</details>


<a id="data_availability-023"></a>
<details>
<summary><b>data_availability-023</b> Semi-supernode: custody half the columns — <i>implemented · high · cpu, disk, bandwidth</i></summary>

**Idea.** Offer a mode that custodies and subscribes to 64 of 128 column subnets, enough to reconstruct all blobs, to serve blobs with about half the bandwidth and storage of a supernode.

**Impact.** n/a

**Best measured result.** Storage ~50% vs supernode (64 vs 128 columns) (pr:prysm#16029)

**Evidence (Lighthouse @ 928b61e719).**

- beacon_chain/src/custody_context.rs:231,243 NodeCustodyType::SemiSupernode = half of custody groups
- src/cli.rs:63 --semi-supernode flag

**Sources.** [prysm#16029](https://github.com/OffchainLabs/prysm/pull/16029), [grandine@5ff11c24d](https://github.com/grandinetech/grandine/commit/5ff11c24d141), [lodestar#8568](https://github.com/ChainSafe/lodestar/pull/8568)

</details>


<a id="data_availability-024"></a>
<details>
<summary><b>data_availability-024</b> Custody first half of columns to skip reconstruction — <i>n/a · medium · S · cpu, bandwidth</i></summary>

**Idea.** Custody the first 64 columns, which hold the original blob data, so blobs can be served directly without reconstruction CPU cost.

**Impact.** Spec assigns custody groups by node_id, so a node cannot choose the first 64 columns.

**Best measured result.** avoids reconstruction CPU load (pr:nimbus#7752)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/data/data_column_custody_group.rs:28`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/data/data_column_custody_group.rs#L28),91 custody groups derived from node_id hash, not selectable

**Sources.** [nimbus#7752](https://github.com/status-im/nimbus-eth2/pull/7752)

</details>


<a id="data_availability-025"></a>
<details>
<summary><b>data_availability-025</b> Background reconstruction of historical custody columns — <i>not · medium · L · cpu, disk, bandwidth</i></summary>

**Idea.** Run a background service that reconstructs missing custody columns from stored half-sets for recent history, walking from head back to the retention floor, so full columns can be served without download.

**Gap in Lighthouse.** Add a background service that, for stored slots with &gt;=50% of columns on disk, loads them, calls kzg_utils::reconstruct_data_columns and writes missing custody columns via the historical import path (e.g. after a cgc increase) instead of custody backfill download.

**Impact.** Saves custody-backfill download bandwidth for nodes that raise cgc or turn supernode, at CPU cost.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/mod.rs:1213`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L1213) attempt_data_column_reconstruction is the only network caller, triggered from gossip_methods.rs:1510
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3785`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3785) reconstruct_data_columns works only on in-memory DA checker / pending_payload_cache entries
- [`beacon_node/beacon_chain/src/historical_data_columns.rs:190`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_data_columns.rs#L190) historical import only KZG-verifies and stores downloaded columns
- [`beacon_node/store/src/reconstruct.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/reconstruct.rs) is state reconstruction, not column reconstruction

**Second check.** Searched all reconstruct call sites in beacon_chain, network (incl. custody_backfill_sync, rpc_methods) and store; only head/gossip-time reconstruction from in-memory caches exists, and RPC serving never reconstructs from stored half-sets.

**Sources.** [nimbus#8533](https://github.com/status-im/nimbus-eth2/pull/8533)

</details>


<a id="data_availability-027"></a>
<details>
<summary><b>data_availability-027</b> Share blobs, cells and sidecars by reference — <i>implemented · medium · S · cpu, memory</i></summary>

**Idea.** Hold blobs, blob/column sidecars and partial-column cells behind Arc/reference-counted pointers and pass them by reference between gossip, EL recovery, KZG, caches, HTTP API and routing. Each handoff then does not copy the large sidecar.

**Impact.** Already by reference.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:71`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L71) cache holds KzgVerifiedCustodyDataColumn wrapping Arc&lt;DataColumnSidecar&gt;
- [`beacon_node/beacon_chain/src/data_column_verification.rs:726-736`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L726-L736) into_inner/clone_arc return Arc
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:608`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L608) clone_arc on reconstructed publish

**Sources.** [lighthouse#4593](https://github.com/sigp/lighthouse/pull/4593), [nimbus#9081](https://github.com/status-im/nimbus-eth2/pull/9081), [lighthouse#4980](https://github.com/sigp/lighthouse/pull/4980), [nimbus#8437](https://github.com/status-im/nimbus-eth2/pull/8437)

</details>


<a id="data_availability-030"></a>
<details>
<summary><b>data_availability-030</b> Quarantine blobs with blobless blocks until joined — <i>implemented · medium · S · memory, latency, bandwidth, sync</i></summary>

**Idea.** Keep gossip blobs/columns and blocks whose data is missing together in a quarantine, keeping the sidecars while the block waits, and import when both are present. Nothing is dropped and requested again.

**Impact.** Already quarantined together.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:68`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L68) PendingComponents holds block plus verified blobs/columns until both present

**Sources.** [nimbus#4808](https://github.com/status-im/nimbus-eth2/pull/4808), [nimbus#6127](https://github.com/status-im/nimbus-eth2/pull/6127)

</details>


<a id="data_availability-031"></a>
<details>
<summary><b>data_availability-031</b> Cache columns with unknown parent block — <i>not · medium · M · latency, sync</i></summary>

**Idea.** Cache data column sidecars whose parent block is unknown and validate them when the parent arrives, instead of discarding and fetching them again.

**Gap in Lighthouse.** Park ParentUnknown columns in a bounded queue keyed by parent root (the existing UnknownBlockDataColumn reprocess queue, MAXIMUM_QUEUED_DATA_COLUMNS=256, is a natural home) and re-run gossip validation when the parent imports; needs spam limits since signature cannot be checked yet.

**Impact.** Avoids re-fetching columns by RPC when a parent arrives late; small, rare bandwidth saving.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_column_verification.rs:1717`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1717) returns GossipDataColumnError::ParentUnknown
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:764-776`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L764-L776) sends only SyncMessage::UnknownParentSidecarHeader (no sidecar) and the column is ignored
- [`beacon_node/network/src/sync/manager.rs:154-160`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L154-L160) UnknownParentSidecarHeader carries only header info; manager.rs:903 passes BlockComponent::Sidecar with no payload
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:147`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L147) UnknownBlockDataColumn queue exists only for BlockRootUnknown, not ParentUnknown

**Second check.** Checked the reprocessing queue: a column-parking mechanism exists but only for the BlockRootUnknown case; the sync message for unknown-parent sidecars is explicitly decoupled from the sidecar, so the column is dropped.

**Sources.** [silver#157](https://github.com/gattaca-com/silver/pull/157)

</details>


<a id="data_availability-032"></a>
<details>
<summary><b>data_availability-032</b> Per-root indexed sidecar quarantine lookups — <i>implemented · low · cpu</i></summary>

**Idea.** Index the blob/column quarantine by block root and slot for O(1) lookups, check column completeness with one per-root gather instead of one hash lookup per column, and use one pop returning an Option instead of has-then-pop.

**Impact.** Lookups are already per root; the linear scan over &lt;=128 entries is negligible, so an index by slot or array would give no measurable gain.

**Best measured result.** Stated: API calls go from O(n) to O(1) (pr:nimbus#7100)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:351`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L351) LRU keyed by block_root holding PendingComponents
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:84-92`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L84-L92) get_cached_data_column is a linear scan of a Vec of at most 128 columns
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:213`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L213) completeness is a length compare, not per-column lookups

**Sources.** [nimbus#7100](https://github.com/status-im/nimbus-eth2/pull/7100), [nimbus#7076](https://github.com/status-im/nimbus-eth2/pull/7076)

</details>


<a id="data_availability-033"></a>
<details>
<summary><b>data_availability-033</b> Cache custody column set per node — <i>implemented · low · S · cpu</i></summary>

**Idea.** Compute the custody and sampling column indices for the node id once, store them as a hash set (swapped atomically when custody count changes), and use it for O(1) membership checks.

**Impact.** Negligible: membership scans at most 128 u64 per column.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/custody_context.rs:265`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L265) ordered_custody_column_indices computed once per CustodyContext
- [`beacon_node/beacon_chain/src/custody_context.rs:507`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L507) sampling_columns_for_epoch returns a prefix slice
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:369`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L369) membership via slice contains

**Sources.** [teku#10446](https://github.com/Consensys-Incorporated/teku/pull/10446), [prysm#14893](https://github.com/OffchainLabs/prysm/pull/14893), [nimbus#7210](https://github.com/status-im/nimbus-eth2/pull/7210)

</details>


<a id="data_availability-034"></a>
<details>
<summary><b>data_availability-034</b> Batch KZG verify sidecars from RPC and sync — <i>implemented · medium · S · cpu, latency, sync</i></summary>

**Idea.** Verify KZG proofs of all blob/column sidecars received by RPC or range sync for a block or batch together with batch KZG verification, instead of one by one.

**Impact.** Already batched.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker.rs:663`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L663) verify_columns_against_block batches via verify_kzg_for_data_column_list
- [`beacon_node/beacon_chain/src/data_column_verification.rs:512`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L512) from_batch_with_scoring batch verifies
- [`crypto/kzg/src/lib.rs:222`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/kzg/src/lib.rs#L222) verify_cell_proof_batch
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:520`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L520) verify_kzg_for_blob_list for blobs

**Sources.** [prysm#13351](https://github.com/OffchainLabs/prysm/pull/13351), [lighthouse#4736](https://github.com/sigp/lighthouse/pull/4736)

</details>


<a id="data_availability-035"></a>
<details>
<summary><b>data_availability-035</b> Batch gossip column verification per block — <i>not · medium · M · cpu, latency</i></summary>

**Idea.** Collect gossip data column sidecars of the same block header and verify their KZG cell proofs in one batch, with the inclusion proof and header signature verified once per batch.

**Gap in Lighthouse.** Add a per-block-root gossip column batching work type in the beacon processor that verifies header signature and inclusion proof once and calls verify_kzg_for_data_column_list once for the batch, falling back to per-column on failure.

**Impact.** Supernodes verify up to 128 columns per block separately; batching could cut gossip column verification CPU several-fold (Lodestar 3-4x) for a few tens of ms latency.

**Best measured result.** job time 3x-4x faster, saves ~250ms; ~35ms more wait time (pr:lodestar#7910)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_column_verification.rs:1178-1193`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1178-L1193) per-sidecar inclusion proof, proposer signature and verify_kzg_for_data_column
- [`beacon_node/beacon_processor/src/lib.rs:417`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L417) GossipDataColumnSidecar is a single AsyncFn work item; batching exists only for attestations/aggregates (lib.rs:110,390,409)
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1166`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1166) missing_cells_for_column_sidecar skips KZG for cells already known (getBlobs/partials) - dedup, not batching
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1331`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1331) partial-column path reuses a cached verified header, but only for partial messages

**Second check.** Beyond the earlier review, checked the beacon processor batching work types, the missing-cells KZG skip and the partial-column header cache; none batches full gossip columns' KZG or shares header verification across full sidecars.

**Sources.** [lodestar#7910](https://github.com/ChainSafe/lodestar/pull/7910)

</details>


<a id="data_availability-036"></a>
<details>
<summary><b>data_availability-036</b> Combine by-root sidecar requests per peer — <i>implemented · medium · bandwidth, sync</i></summary>

**Idea.** Send one by-root RPC request per peer for all missing blobs or columns of a block (or several sampling requests), instead of one request per sidecar.

**Impact.** Already one by-root request per peer for all its columns (and several blocks).

**Best measured result.** saves bandwidth (stated, no numbers) (pr:teku#8952)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context/custody.rs:205`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L205) continue_requests groups columns_to_request_by_peer
- [`beacon_node/network/src/sync/network_context/custody.rs:271`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L271) one DataColumnsByRootRequestParams per peer with all indices and block_roots

**Sources.** [teku#8952](https://github.com/Consensys-Incorporated/teku/pull/8952), [lighthouse#6256](https://github.com/sigp/lighthouse/pull/6256)

</details>


<a id="data_availability-038"></a>
<details>
<summary><b>data_availability-038</b> Request columns only from custody peers — <i>implemented · medium · bandwidth, sync</i></summary>

**Idea.** Send by-root column requests only to peers whose custody set contains the columns, and filter each request to the columns the chosen peer custodies before sending it.

**Impact.** Requests only go to peers custodying each column, indices filtered per peer.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context/custody.rs:353`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L353) select_column_peer uses cx.get_custodial_peers(column_index, slot)
- [`beacon_node/network/src/sync/network_context/custody.rs:205`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L205) indices pushed per chosen peer only

**Sources.** [prysm#14452](https://github.com/OffchainLabs/prysm/pull/14452), [caplin#17392](https://github.com/erigontech/erigon/pull/17392), [caplin#18025](https://github.com/erigontech/erigon/pull/18025)

</details>


<a id="data_availability-039"></a>
<details>
<summary><b>data_availability-039</b> Hedge slow column requests to alternate peers — <i>not · medium · M · latency, sync</i></summary>

**Idea.** After a delay, send a slow in-flight data column request again to another custody peer, bounded to a fraction of pending requests and two attempts per request.

**Gap in Lighthouse.** There is no hedging. A slow in-flight DataColumnsByRoot request is never duplicated to another custody peer. Only an RPC error or timeout moves the column back to NotStarted (max 3 attempts). The fix needs a send timestamp in Status::Downloading, a timer in ActiveCustodyRequest that re-issues still-pending columns to a different peer after a delay, a cap of 2 attempts per column, and a global cap on the fraction of hedged requests.

**Impact.** Lower tail latency for column lookups and gossip-miss recovery when a custody peer is slow. It costs a small amount of extra bandwidth.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context/custody.rs:405-415`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L405-L415) column Status is NotStarted(Instant)/Downloading(req_id)/Downloaded; no send time or deadline on Downloading
- [`beacon_node/network/src/sync/network_context/custody.rs:448-460`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L448-L460) Downloading only returns to NotStarted on download error
- [`beacon_node/network/src/sync/network_context/custody.rs:205`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L205) continue_requests only issues requests for NotStarted columns
- [`beacon_node/network/src/sync/range_sync/chain.rs:247`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_sync/chain.rs#L247) range/backfill re-request only after peer removal or batch failure, not on slowness

**Second check.** Searched sync/ and lighthouse_network/ for hedge, speculative, slow-peer and re-request logic, including range, backfill and custody_backfill. All re-requests are failure-driven. The only slow_peer hits are gossipsub scoring parameters, which do not apply to RPC.

**Sources.** [teku#11011](https://github.com/Consensys-Incorporated/teku/pull/11011)

</details>


<a id="data_availability-042"></a>
<details>
<summary><b>data_availability-042</b> Sidecar validation without state advancement — <i>implemented · medium · cpu, memory, latency</i></summary>

**Idea.** Verify a blob/column sidecar's proposer index from a proposer cache computed once per block, or use an existing state or hold the sidecar until a state exists, instead of running slot processing for each sidecar in gossip validation.

**Impact.** Proposer index comes from beacon_proposer_cache; state advance only on cache miss.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_column_verification.rs:1732`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1732) verify_proposer_and_signature
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1746`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1746) chain.with_proposer_cache keyed by shuffling root, state loaded only in miss closure at :1759

**Sources.** [grandine#192](https://github.com/grandinetech/grandine/pull/192), [grandine@f6d472f38](https://github.com/grandinetech/grandine/commit/f6d472f38b7f), [grandine#183](https://github.com/grandinetech/grandine/pull/183), [grandine@181823273](https://github.com/grandinetech/grandine/commit/1818232735c6), [prysm#14231](https://github.com/OffchainLabs/prysm/pull/14231), [prysm#17776](https://github.com/OffchainLabs/prysm/pull/17776)

</details>


<a id="data_availability-044"></a>
<details>
<summary><b>data_availability-044</b> Prune blob and column data past DA window — <i>implemented · medium · L · disk</i></summary>

**Idea.** Delete blob/column sidecars older than the data availability retention window (and non-canonical ones at finalization), with storage keyed by slot so pruning can stream in order. This keeps disk use bounded.

**Gap in Lighthouse.** Keys are block_root based (get_data_column_key), so pruning walks blocks backwards via ParentRootBlockIterator and does key_exists for all 128 column keys per block instead of a slot-ordered range delete. Same effect, bounded disk, but a slot-keyed layout would stream cheaper.

**Impact.** Pruning cost is minor on mainnet; the layout change would cut DB reads during prune only.

**Best measured result.** 1.6TB in caplin dir on a Hoodi node (pr:caplin#20379)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3277`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3277) try_prune_blobs deletes blobs and columns before DA boundary
- [`beacon_node/beacon_chain/src/migrate.rs:780`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L780) DeleteBlobs/DeleteDataColumns for abandoned forks at finalization

**Sources.** [lighthouse#3852](https://github.com/sigp/lighthouse/pull/3852), [caplin#20379](https://github.com/erigontech/erigon/pull/20379), [teku#6587](https://github.com/Consensys-Incorporated/teku/pull/6587)

</details>


<a id="data_availability-045"></a>
<details>
<summary><b>data_availability-045</b> Derive column retention window from chain config — <i>implemented · low · S · disk</i></summary>

**Idea.** Compute the data column retention window as epochs times slots-per-epoch from the chain config, not a mainnet slot default, so chains with shorter epochs do not keep twice the data.

**Impact.** None; retention is epoch-based so short-epoch chains do not over-retain.

**Best measured result.** gnosis retained 131072 slots against a 65536 window (2x) (pr:caplin#23610)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/core/chain_spec.rs:947`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/core/chain_spec.rs#L947) min_epoch_data_availability_boundary uses min_epochs_for_data_column_sidecars_requests in epochs
- [`consensus/types/src/core/chain_spec.rs:2407`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/core/chain_spec.rs#L2407) value is a config field
- [`beacon_node/store/src/hot_cold_store.rs:3263`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3263) pruning uses this boundary

**Sources.** [caplin#23610](https://github.com/erigontech/erigon/pull/23610)

</details>


<a id="data_availability-048"></a>
<details>
<summary><b>data_availability-048</b> Incremental capped low-priority blob pruning — <i>partial · low · S · cpu, disk, latency</i></summary>

**Idea.** Prune blobs often in small capped chunks on a low-priority single thread, reading keys only from the KV store, instead of deleting a whole epoch at once.

**Gap in Lighthouse.** Prune already runs about every epoch so chunks are small, but there is no per-run cap, no low-priority thread, and existence is probed with 128 key_exists calls per block. Add a cap on blocks per run in try_prune_blobs and replace get_all_data_column_keys probing with one prefix key scan on BeaconDataColumn.

**Impact.** Small: removes bursts after long pauses (checkpoint sync, prune disabled) and ~128 point lookups per block; minor on steady state.

**Best measured result.** Cap 32 per minute vs about 5 new sidecars per minute (pr:teku#6628)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3277`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3277) try_prune_blobs deletes everything from oldest_data_slot to end_epoch in one batch
- [`beacon_node/store/src/config.rs:30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L30) DEFAULT_EPOCHS_PER_BLOB_PRUNE = 1 so each run is about one epoch
- [`beacon_node/store/src/hot_cold_store.rs:3391`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3391) key_exists called per column index (128 per block) instead of key-only listing
- [`beacon_node/store/src/hot_cold_store.rs:3250`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3250) runs on the migrator thread after finalization, no priority control

**Sources.** [teku#6628](https://github.com/Consensys-Incorporated/teku/pull/6628), [teku#6758](https://github.com/Consensys-Incorporated/teku/pull/6758)

</details>


<a id="data_availability-054"></a>
<details>
<summary><b>data_availability-054</b> Skip re-verifying already verified sidecars — <i>partial · medium · S · cpu, latency</i></summary>

**Idea.** Track in the DA cache or quarantine which blob/column sidecars were already KZG-verified (gossip or EL) and at fork choice import or RPC processing verify only sidecars from unverified sources; accept identical known columns without re-verifying.

**Gap in Lighthouse.** The gossip and EL paths already skip identical known columns, and they KZG-verify only the missing cells. The RPC response path (put_rpc_custody_columns for Fulu and Gloas, and put_rpc_blobs) still verifies every sidecar, even when a column with the same content arrived by gossip while the request was in flight. The fix is to filter out exact matches against the cached KZG-verified columns before from_batch_with_scoring. Open PR sigp/lighthouse#10363 does this but is not merged.

**Impact.** Avoids redundant KZG batch verification of RPC columns that overlap with gossip arrivals during an in-flight lookup. PR #10363 measured about 1.4 ms saved per 8-column batch with 4 overlapping columns. This is a small, occasional saving.

**Best measured result.** verifySidecars often 350+ ms (samples 33 ms to 473 ms) (pr:nimbus#8542)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_column_verification.rs:422-443`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L422-L443) gossip column identical to a cached one (EL getBlobs or partials) is not re-KZG-verified: PriorKnownUnpublished
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1160-1175`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1160-L1175) same in the full gossip verification path; only missing cells go to KZG
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:187-246`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L187-L246) missing_cells_for_column_sidecar compares with the cached full column or partial cells and returns None when all are known
- [`beacon_node/network/src/sync/network_context.rs:971-990`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L971-L990) lookups request only columns not yet cached at request time
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:350-360`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L350-L360) put_rpc_custody_columns batch-KZG-verifies every returned column without a cache check
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:322-340`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L322-L340) put_rpc_blobs verifies all blobs without a cache check
- [`beacon_node/beacon_chain/src/pending_payload_cache/mod.rs:321-327`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/mod.rs#L321-L327) Gloas RPC path: from_batch_with_scoring_and_commitments, also no cache check

**Second check.** Beyond the earlier review, I found that the gossip path does skip identical cached columns and verifies only missing cells (data_column_verification.rs:431, data_availability_checker.rs:187). Lookups also exclude columns cached at request time, so the remaining gap is only RPC responses that race with gossip. Gloas pending_payload_cache has the same gap.

**Sources.** [teku#6636](https://github.com/Consensys-Incorporated/teku/pull/6636), [grandine@0e22c0ff9](https://github.com/grandinetech/grandine/commit/0e22c0ff9663), [lodestar#8139](https://github.com/ChainSafe/lodestar/pull/8139), [nimbus#8542](https://github.com/status-im/nimbus-eth2/pull/8542), [nimbus#8628](https://github.com/status-im/nimbus-eth2/pull/8628), [lighthouse#10363](https://github.com/sigp/lighthouse/pull/10363), [lighthouse#7493](https://github.com/sigp/lighthouse/pull/7493)

</details>


<a id="data_availability-055"></a>
<details>
<summary><b>data_availability-055</b> Drop sidecars and fetches for imported blocks — <i>partial · low · S · cpu, memory, bandwidth</i></summary>

**Idea.** Ignore received blob/column sidecars and skip pending RPC fetches for blocks already imported with DA satisfied or whose tracker was removed, and do not register historical sync data in the gossip blob pool. No redundant verification, requests or pool growth occur.

**Gap in Lighthouse.** A column not previously observed that arrives after the block is imported (or for a column outside the custody set) still goes through inclusion proof, signature and KZG verification. Add an early check in validate_data_column_sidecar_for_gossip_fulu against fork choice / DA checker for block_root already imported and return an ignore error. Gossip blob pool does not exist so that part is n/a.

**Impact.** Saves KZG cell verification (a few ms per late column) on duplicates arriving after import; modest, a handful of columns per block.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_column_verification.rs:1152`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1152) verify_is_unknown_sidecar drops columns already observed
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:187`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L187) missing_cells_for_column_sidecar returns None when column already cached (skips KZG)
- [`beacon_node/network/src/sync/network_context.rs:730`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L730) block_lookup_request skips fetch when block ExecutionValidated/known
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1139`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1139) no check that the block is already imported with DA satisfied before inclusion proof and KZG

**Sources.** [teku#7231](https://github.com/Consensys-Incorporated/teku/pull/7231), [grandine@f67342dc9](https://github.com/grandinetech/grandine/commit/f67342dc9f92), [grandine#140](https://github.com/grandinetech/grandine/pull/140), [teku#10789](https://github.com/Consensys-Incorporated/teku/pull/10789)

</details>


<a id="data_availability-056"></a>
<details>
<summary><b>data_availability-056</b> Bound or fail fast on DA wait — <i>n/a · medium · latency, sync</i></summary>

**Idea.** During sync, payload envelope import and block import, bound the data availability or sampling wait (for example one slot) or check availability synchronously and return an error so the batch or block is retried, instead of waiting indefinitely on a gossip subscription.

**Impact.** Lighthouse DA is a non-blocking pending-components cache; import returns MissingComponents and completes when data arrives, so there is no wait on a gossip subscription to bound.

**Best measured result.** Fixed devnet sync dead-end at batch boundary (pr:prysm#16978)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:209`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L209) MissingComponents returned, not awaited
- [`beacon_node/beacon_chain/src/payload_envelope_verification/import.rs:139`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/import.rs#L139) envelope import returns MissingComponents status

**Sources.** [prysm#16991](https://github.com/OffchainLabs/prysm/pull/16991), [prysm#16978](https://github.com/OffchainLabs/prysm/pull/16978), [prysm#16993](https://github.com/OffchainLabs/prysm/pull/16993), [prysm#17152](https://github.com/OffchainLabs/prysm/pull/17152), [prysm#16994](https://github.com/OffchainLabs/prysm/pull/16994), [teku#10694](https://github.com/Consensys-Incorporated/teku/pull/10694)

</details>


<a id="data_availability-058"></a>
<details>
<summary><b>data_availability-058</b> Run DA check concurrently with block verification — <i>implemented · medium · latency</i></summary>

**Idea.** Persist gossip blobs from the gossip handler and run the data availability check concurrently with consensus verification and EL newPayload (one cancel-on-failure group), joining only at the end instead of running sequentially.

**Impact.** Gossip sidecars are verified/persisted in their own handlers and EL getBlobs runs concurrently with block verification and newPayload; DA join is at the end.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/mod.rs:982`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L982) spawn_fetch_block_columns spawns getBlobs fetch on executor concurrent with block processing
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1127`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1127) getBlobs triggered from gossip handler
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:70`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L70) gossip sidecars land in pending cache independently; DA check is a cache join at the end

**Sources.** [prysm#16899](https://github.com/OffchainLabs/prysm/pull/16899), [prysm#12734](https://github.com/OffchainLabs/prysm/pull/12734)

</details>


<a id="data_availability-061"></a>
<details>
<summary><b>data_availability-061</b> Track received columns to skip duplicate work — <i>implemented · medium · cpu, disk, bandwidth</i></summary>

**Idea.** Track which data columns were received and stored per block, so a column from gossip and the same one recovered from EL is not processed, persisted or requested twice.

**Impact.** None needed; already avoids repeated verification, storage and EL work.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:176`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L176) merge_data_columns skips already cached index
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:632-650`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L632-L650) EL-recovered columns deduped vs gossip-observed and DA-cached
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1160-1176`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1160-L1176) PriorKnown / missing_cells check, observe_column_sidecars

**Sources.** [prysm#14467](https://github.com/OffchainLabs/prysm/pull/14467), [teku#9409](https://github.com/Consensys-Incorporated/teku/pull/9409)

</details>


<a id="data_availability-063"></a>
<details>
<summary><b>data_availability-063</b> Delay RPC fetch of missing sidecars — <i>partial · medium · S · latency, bandwidth, sync</i></summary>

**Idea.** Delay RPC fetches of missing blobs/columns by a slot-time-based interval (about 0.5 to 1 s, capped by the attestation deadline), so gossip can deliver them first and redundant requests are avoided.

**Gap in Lighthouse.** There is no explicit slot-time-based delay. The delay comes only from the trigger: Lighthouse never fetches on block arrival, waits for attestations and 3 peers, and then requests only the columns it has not cached. The Gloas column BlockRootUnknown path (gossip_methods.rs:790) and unknown-parent lookups fetch at once, with no wait capped at the attestation deadline.

**Impact.** Small. Most of the redundant by-root requests are already avoided. An explicit delay would only help the Gloas column and unknown-parent triggers.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1972`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1972) gossip block with MissingComponents starts no RPC fetch
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:2874-2886`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L2874-L2886) the lookup is started only by attestations for a block not in fork choice (about 1/3 slot)
- [`beacon_node/network/src/sync/manager.rs:1036-1056`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L1036-L1056) handle_unknown_block_root waits for corroboration from several peers
- [`beacon_node/lighthouse_network/src/config.rs:25`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L25) DEFAULT_UNKNOWN_ROOT_MIN_PEERS = 3
- [`beacon_node/network/src/sync/network_context.rs:970-992`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L970-L992) custody_lookup_request leaves out columns already received on gossip (cached_data_column_indexes)
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:73`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L73) QUEUED_RECONSTRUCTION_DELAY 150ms gives gossip time before reconstruction

**Second check.** The earlier review missed that Lighthouse does not fetch at block arrival at all. Its lookup starts from attestations at about 4s and needs 3 corroborating peers, and it filters columns already received on gossip. This gives the 'let gossip deliver first' effect without a timer.

**Sources.** [teku#10094](https://github.com/Consensys-Incorporated/teku/pull/10094), [teku#7026](https://github.com/Consensys-Incorporated/teku/pull/7026)

</details>


<a id="data_availability-065"></a>
<details>
<summary><b>data_availability-065</b> Pull late block when blobs arrive first — <i>partial · medium · S · latency</i></summary>

**Idea.** If blobs arrive on gossip but the block does not arrive by a cutoff, fetch the block and remaining blobs from peers instead of waiting.

**Gap in Lighthouse.** Gloas already does this: a column for an unknown block root starts a block lookup at once, with no cutoff. Fulu, the live fork, does not. A Fulu column carries a signed header, so with a known parent it verifies without the block, sits as MissingComponents, and the block is fetched only when attestations arrive. Add a cutoff timer after the first Fulu column for an unseen block that sends search_unknown_block for that root.

**Impact.** On Fulu, a block missed on gossip but whose columns arrive is recovered before the attestations come (about 4s), which improves head vote timing.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_column_verification.rs:1241-1246`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1241-L1246) a Gloas gossip column for an unknown block root returns BlockRootUnknown
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1386-1392`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1386-L1392) the same for partial columns ('Block not known, trigger lookup')
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:778-793`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L778-L793) BlockRootUnknown sends UnknownBlockHashFromAttestation to start a block lookup
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1173-1185`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1173-L1185) the partial column path does the same
- [`beacon_node/network/src/sync/manager.rs:921-925`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L921-L925),1036-1056 the lookup starts after peer corroboration
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1016-1023`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1016-L1023) a Fulu column with a known parent goes to the DA checker as MissingComponents and starts no block lookup

**Second check.** Found the Gloas and partial-column BlockRootUnknown path, which starts a lookup from a sidecar of an unknown block. The earlier review searched only UnknownParentSidecarHeader. Fulu remains uncovered, so the verdict is partial.

**Sources.** [lodestar#6534](https://github.com/ChainSafe/lodestar/pull/6534)

</details>


<a id="data_availability-067"></a>
<details>
<summary><b>data_availability-067</b> Fetch missing columns within the slot — <i>partial · medium · M · latency</i></summary>

**Idea.** Run the missing-column fetcher every second and request missing custody columns by root after a grace of half the time to the attestation deadline, instead of waiting a minute.

**Gap in Lighthouse.** There is no periodic fetcher that scans the DA checker for blocks with missing custody columns. Recovery inside the slot depends on attestations that reference the block, from at least 3 peers. Add a 1s tick that scans pending components past a grace period and issues custody by-root requests, so recovery does not depend on attestation traffic.

**Impact.** Low to medium. The minute-long wait that Caplin fixed does not occur in Lighthouse when attestations flow. A tick would help only when few attestations reference the block, for example a late block or a small or isolated set of peers.

**Best measured result.** block stayed unavailable for over a minute before (pr:caplin#24830)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:2874-2886`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L2874-L2886) an attestation for a block that is pending in the DA checker (not in fork choice) starts a lookup within the slot
- [`beacon_node/network/src/sync/network_context.rs:956-992`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L956-L992) custody_lookup_request fetches only the custody columns that are not yet cached
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1023`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1023),1505-1518 reconstruction is queued (QUEUED_RECONSTRUCTION_DELAY 150ms) when columns are missing
- [`beacon_node/network/src/sync/manager.rs:805-842`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L805-L842) there is no periodic missing-column tick

**Second check.** The earlier review missed the following: when a block is stuck in the DA checker, gossip attestations for it fail with UnknownHeadBlock, and that already starts an in-slot lookup that fetches only the missing custody columns. This is event-driven, not periodic.

**Sources.** [caplin#24830](https://github.com/erigontech/erigon/pull/24830)

</details>


<a id="data_availability-069"></a>
<details>
<summary><b>data_availability-069</b> Disk-backed blob quarantine — <i>n/a · medium · memory, disk</i></summary>

**Idea.** Persist quarantined blob sidecars in a database table keyed by block root and index, deleted at finalization, so the quarantine does not hold them all in memory.

**Impact.** Lighthouse deliberately removed disk overflow (sigp#5891) and bounds the in-memory LRU; a disk quarantine would go against that design.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:349`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L349) critical is an in-memory LruCache, no disk table

**Sources.** [nimbus#7108](https://github.com/status-im/nimbus-eth2/pull/7108)

</details>


<a id="data_availability-070"></a>
<details>
<summary><b>data_availability-070</b> Memory-only bounded LRU for pending components — <i>implemented · medium · memory, disk</i></summary>

**Idea.** Remove the disk overflow of the pending availability cache and keep only a bounded in-memory LRU, removing the disk I/O.

**Impact.** Already done; no disk I/O for pending components.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:349-376`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L349-L376) DataAvailabilityCheckerInner holds only RwLock&lt;LruCache&gt;, no store/overflow
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:720`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L720) do_maintenance prunes by epoch

**Sources.** [lighthouse#5891](https://github.com/sigp/lighthouse/pull/5891)

</details>


<a id="data_availability-075"></a>
<details>
<summary><b>data_availability-075</b> Evict DA entries exactly when import completes — <i>partial · low · S · cpu, memory, disk, latency, bandwidth, sync</i></summary>

**Idea.** Keep a block's pending components and sampling tracker in the availability cache until fork choice import completes, then remove them at once (otherwise LRU/finality), holding the write lock only for the insert. This prevents re-downloads and keeps the cache from growing.

**Gap in Lighthouse.** Lighthouse keeps entries (deliberately, to avoid a re-insert race) until LRU/finality, so re-downloads are prevented and the write lock is short, but entries are not freed at import completion. Could remove in the import-complete path via a remove on overflow_lru_cache after fork choice import, if the race is handled.

**Impact.** Only memory: a few tens of MB of columns held until finality; no CPU saving.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:540`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L540) comment: components are never removed manually, only LRU
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:720`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L720) do_maintenance removes entries older than cutoff epoch
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:557`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L557) write lock held only for the insert, then downgraded

**Sources.** [lighthouse#5845](https://github.com/sigp/lighthouse/pull/5845), [lighthouse#7961](https://github.com/sigp/lighthouse/pull/7961), [teku#10219](https://github.com/Consensys-Incorporated/teku/pull/10219), [lighthouse#4132](https://github.com/sigp/lighthouse/pull/4132)

</details>


<a id="data_availability-077"></a>
<details>
<summary><b>data_availability-077</b> Free column recovery state promptly — <i>n/a · medium · cpu, memory</i></summary>

**Idea.** Remove column recovery tasks from the tracking map at completion (with a timed sweep), keep references only to sidecars still pending reconstruction and store only slot and root per entry, instead of holding all retrieved sidecars for minutes.

**Impact.** Lighthouse has no per-block recovery task map retaining retrieved sidecars; reconstruction state is a flag inside the bounded pending-components LRU, freed on import or maintenance.

**Best measured result.** Heap graphs before/after shown (no numbers) (pr:teku#9648)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:592`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L592) check_and_set_reconstruction_started is a flag on LRU entry
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:720`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L720) do_maintenance

**Sources.** [teku#9890](https://github.com/Consensys-Incorporated/teku/pull/9890), [teku#9874](https://github.com/Consensys-Incorporated/teku/pull/9874), [teku#9648](https://github.com/Consensys-Incorporated/teku/pull/9648)

</details>


<a id="data_availability-078"></a>
<details>
<summary><b>data_availability-078</b> Import only when blob count equals commitments — <i>implemented · low · S · latency</i></summary>

**Idea.** Treat a block as complete only when the number of held blob sidecars exactly equals its KZG commitment count, so import is not triggered early and rejected.

**Impact.** None; import never triggers early for incomplete data.

**Best measured result.** mitigates some stuttering in block updates when blobs arrived after blocks (pr:nimbus#5363)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:209`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L209) make_available compares received column count with expected via Ordering
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:212`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L212) Equal makes available, Greater is an error, Less waits

**Sources.** [nimbus#5363](https://github.com/status-im/nimbus-eth2/pull/5363)

</details>


<a id="data_availability-079"></a>
<details>
<summary><b>data_availability-079</b> Drop gossip columns outside sampling set — <i>implemented · medium · cpu, disk, bandwidth</i></summary>

**Idea.** Drop incoming data column sidecars for columns that are not in the node's sampling set before KZG verification and storage.

**Gap in Lighthouse.** Equivalent effect: only sampling-subnet topics are subscribed, so off-set columns do not arrive via gossip; no explicit pre-KZG check in validate_data_column_sidecar_for_gossip_fulu but subscribe-level filtering makes it unnecessary except around CGC changes.

**Impact.** Already avoids KZG and storage for non-sampled columns in normal operation.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/globals.rs:36`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/globals.rs#L36),75-118 sampling_subnets
- [`beacon_node/lighthouse_network/src/service/utils.rs:302`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/utils.rs#L302) subscribes only to sampling subnets
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:404-408`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L404-L408) filter by sampling_columns after gossip verify

**Sources.** [grandine#376](https://github.com/grandinetech/grandine/pull/376), [grandine@b970e9d91](https://github.com/grandinetech/grandine/commit/b970e9d91cbe)

</details>


<a id="data_availability-080"></a>
<details>
<summary><b>data_availability-080</b> Correct proposer cache key in blob verification — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** Look up the proposer for blob sidecar verification with the correct shuffling decision root, so the proposer cache hits mid-epoch instead of recomputing the shuffling.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_column_verification.rs:1732`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1732) verify_proposer_and_signature
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1745`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1745) uses parent_block.proposer_shuffling_root_for_child_block as cache key
- [`beacon_node/beacon_chain/src/block_verification.rs:1026`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1026) same keying for blocks

**Sources.** [lighthouse#4646](https://github.com/sigp/lighthouse/pull/4646)

</details>


<a id="data_availability-085"></a>
<details>
<summary><b>data_availability-085</b> Skip KZG and proof checks for EL-built columns — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** When blobs or columns of a block are built from the local EL getBlobs response, skip gossip KZG cell proof and inclusion proof verification (the EL already verified them), keeping only structural checks or one KZG check before persistence.

**Best measured result.** 6 blobs 65.3 -&gt; 16.8 ms, 21 blobs 218 -&gt; 58 ms (benchmark); ~28 ms per blob saved (pr:caplin#25510)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:700`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L700) KzgVerifiedPartialDataColumn::from_execution_verified wraps EL-built columns with no KZG/inclusion check
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:405`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L405) V4 path takes EL cells directly

**Sources.** [nimbus#6913](https://github.com/status-im/nimbus-eth2/pull/6913), [caplin#25510](https://github.com/erigontech/erigon/pull/25510)

</details>


<a id="data_availability-086"></a>
<details>
<summary><b>data_availability-086</b> Cache column inclusion proof results — <i>not · low · S · cpu</i></summary>

**Idea.** Cache the result of the KZG commitments inclusion proof check per block (key: hash of proof inputs) so other column sidecars of the same block skip the merkle proof.

**Gap in Lighthouse.** Add a small LRU keyed by hash of (commitments root inputs, proof, body_root) consulted in verify_column_inclusion_proof and the RPC verifiers; or hash commitments once per block_root.

**Impact.** Saves a tree hash of the commitment list plus a ~4-deep merkle branch for each of up to 128 columns per block; tens of microseconds each, small total.

**Best measured result.** 'reduce redundant work' when verifying inclusion proofs; no numbers (pr:prysm#15217)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_column_verification.rs:1667`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1667) verify_column_inclusion_proof calls verify_inclusion_proof on every column
- [`consensus/types/src/data/data_column_sidecar.rs:285`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/data/data_column_sidecar.rs#L285) verify_inclusion_proof recomputes kzg_commitments.tree_hash_root and merkle branch each call
- [`beacon_node/network/src/sync/network_context/requests/data_columns_by_root.rs:63`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/requests/data_columns_by_root.rs#L63) and data_columns_by_range.rs:36 also verify per column, no cache

**Sources.** [prysm#15217](https://github.com/OffchainLabs/prysm/pull/15217)

</details>


<a id="data_availability-087"></a>
<details>
<summary><b>data_availability-087</b> Late DA check with per-block sampling tracker — <i>implemented · medium · disk, latency, bandwidth</i></summary>

**Idea.** Track sampled columns per block in memory as they arrive by gossip, EL or RPC, fetch only the missing ones by RPC, and run the availability check as late as possible to give gossip and EL more time.

**Best measured result.** fewer RPC calls (no numbers) (pr:teku#10006)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:592`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L592) per-block PendingComponents tracks columns from gossip/EL/RPC
- [`beacon_node/network/src/sync/network_context.rs:956-990`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L956-L990) custody_lookup_request skips cached_data_column_indexes and fetches only the missing columns
- [`beacon_node/network/src/sync/network_context/custody.rs:232`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L232) per-column peer request

**Sources.** [teku#10006](https://github.com/Consensys-Incorporated/teku/pull/10006)

</details>


<a id="data_availability-088"></a>
<details>
<summary><b>data_availability-088</b> Re-call getBlobs until block columns are complete — <i>not · medium · S · latency, bandwidth</i></summary>

**Idea.** Call engine_getBlobs again with short timeouts, triggered per gossip block, per arriving column and periodically, until all needed columns of the block can be built from EL blobs, instead of waiting for gossip.

**Gap in Lighthouse.** getBlobs fires at most once per trigger (gossip block, first partial header, RPC block); no re-call on later column/partial arrival and no periodic retry until custody columns are complete. Add a bounded retry loop (short timeouts, per-slot deadline) around fetch_engine_blobs_and_publish_full; V3/V4 partial merging already handles incremental results.

**Impact.** Higher EL hit rate when blobs reach the EL mempool after the block; fewer columns from gossip/RPC, earlier availability on late blobs (est. a few hundred ms in those cases).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1936`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1936) spawn_fetch_block_columns once per gossip block
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1120`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1120) getBlobs once on first (uncached) partial header only
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:217`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L217) once after RPC block
- [`beacon_node/network/src/network_beacon_processor/mod.rs:998`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L998) fetch_engine_blobs_and_publish_full: single call, MissingComponents/Ok(None) only logged
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:161`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L161) one V4 or V2/V3 attempt, no loop or timer

**Second check.** Also checked the partial-column path (publish_partial_data_columns, partial-header trigger) and the fetch_blobs V4 path for any retry/interval; the partial header trigger is a second one-shot call, not a retry.

**Sources.** [nimbus#8012](https://github.com/status-im/nimbus-eth2/pull/8012), [nimbus#7445](https://github.com/status-im/nimbus-eth2/pull/7445), [prysm#15520](https://github.com/OffchainLabs/prysm/pull/15520)

</details>


<a id="data_availability-090"></a>
<details>
<summary><b>data_availability-090</b> Allow column reconstruction while not synced — <i>not · medium · M · sync, bandwidth</i></summary>

**Idea.** Permit data column reconstruction from 50% of columns during range sync and backfill (on by default), not only at head, so sync does not have to download the remaining columns from peers.

**Gap in Lighthouse.** Range sync and backfill request every sampling column from peers and never reconstruct. Request only 50% of columns for supernode/high-custody nodes during sync and reconstruct the rest locally (reconstruct_data_columns / KzgVerifiedCustodyDataColumn::reconstruct_columns) before import; backfill would need the same in historical_blocks import.

**Impact.** Supernodes and high-custody nodes could download about half the column data during range sync and backfill, at the cost of KZG recovery CPU.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1488`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1488) check_reconstruction_trigger only called from gossip paths (1024, 1465)
- [`beacon_node/network/src/network_beacon_processor/mod.rs:1213`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L1213) attempt_data_column_reconstruction only reached from gossip
- [`beacon_node/network/src/sync/network_context.rs:987`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L987) sync requests all sampling columns from peers
- [`beacon_node/beacon_chain/src/historical_blocks.rs:482`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_blocks.rs#L482) only state reconstruction in backfill, no column reconstruction
- [`beacon_node/beacon_chain/src/custody_context.rs:492`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L492) should_attempt_reconstruction does not depend on sync state but is never consulted by sync

**Second check.** Searched sync/ (range, backfill, block_sidecar_coupling, network_context) and historical_blocks.rs for any column reconstruction; the only 'reconstruct' there is historic state reconstruction.

**Sources.** [grandine@062840454](https://github.com/grandinetech/grandine/commit/062840454cce), [grandine#334](https://github.com/grandinetech/grandine/pull/334), [grandine#361](https://github.com/grandinetech/grandine/pull/361), [grandine@ef26a3a88](https://github.com/grandinetech/grandine/commit/ef26a3a8818e)

</details>


<a id="data_availability-092"></a>
<details>
<summary><b>data_availability-092</b> Compute sidecar inclusion proofs from shared merkle subtrees — <i>implemented · medium · cpu, memory</i></summary>

**Idea.** When building blob or column sidecars for a block, compute the block body merkle subtree and the KZG commitments branch once and derive every sidecar's inclusion proof from it, instead of rebuilding the tree per sidecar; cache the proposer signature result for the block too.

**Gap in Lighthouse.** Legacy BlobSidecar::new (blob_sidecar.rs:285) still rebuilds the tree per blob but is off the Fulu path.

**Best measured result.** 2.12x faster / 53% less memory at 3 blobs; 5.16x faster / 77% less at 9 blobs (pr:prysm#15473)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/kzg_utils.rs:318`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L318) kzg_commitments_merkle_proof computed once per block
- [`beacon_node/beacon_chain/src/kzg_utils.rs:556`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L556) proof cloned into every column sidecar
- beacon_node/consensus/types/src/block/beacon_block_body.rs:369 comment prefers reused proof with complete_kzg_commitment_merkle_proof

**Sources.** [lighthouse#4968](https://github.com/sigp/lighthouse/pull/4968), [prysm#15473](https://github.com/OffchainLabs/prysm/pull/15473)

</details>


<a id="data_availability-093"></a>
<details>
<summary><b>data_availability-093</b> Validate column sidecars at mid processor priority — <i>implemented · medium · latency</i></summary>

**Idea.** Schedule gossip data column sidecar validation in the beacon processor at a priority below blocks, so a burst of sidecars does not delay block processing.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs):~905 gossip_block_queue popped before gossip_data_column_queue (line ~945) and partial column queue
- [`beacon_node/beacon_processor/src/lib.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs):~954 column_reconstruction_queue lower still

**Sources.** [grandine@212000f60](https://github.com/grandinetech/grandine/commit/212000f60657)

</details>


<a id="data_availability-094"></a>
<details>
<summary><b>data_availability-094</b> Fetch column subsets from many peers in parallel — <i>implemented · medium · sync, bandwidth</i></summary>

**Idea.** During sync or lookup, split a column request across several custody peers in parallel instead of requesting all columns from one supernode, spreading load and removing single-peer dependence.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context.rs:578`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L578) select_columns_by_range_peers_to_request picks a custody peer per column, grouping into per-peer requests
- [`beacon_node/network/src/sync/network_context/custody.rs:232-320`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L232-L320) lookup path splits columns across peers with attempts tracking

**Sources.** [prysm#14977](https://github.com/OffchainLabs/prysm/pull/14977)

</details>


<a id="data_availability-095"></a>
<details>
<summary><b>data_availability-095</b> Give reconstruction a multi-thread worker allocation — <i>partial · medium · S · cpu, latency</i></summary>

**Idea.** Let reconstruction claim several beacon processor worker slots and run on a scoped rayon pool of that size, so parallel KZG recovery does not oversubscribe cores shared with other tasks.

**Gap in Lighthouse.** Reconstruction runs on the shared HighPriority scoped rayon pool (80% of CPUs) but BeaconProcessor still counts it as one worker slot; no multi-permit allocation exists (PRs #7720/#7789 were closed unmerged). Need ColumnReconstruction to take N worker permits and install a rayon scope of size N.

**Impact.** Avoids core oversubscription on supernodes during reconstruction; small tail-latency gain for concurrent work.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:3811`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3811)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3845`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3845)
- [`common/task_executor/src/rayon_pool_provider.rs:4-47`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/task_executor/src/rayon_pool_provider.rs#L4-L47)
- [`beacon_node/beacon_processor/src/lib.rs:953`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L953)
- [`beacon_node/beacon_processor/src/lib.rs:1703`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1703)
- [`crypto/kzg/src/lib.rs:307-314`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/kzg/src/lib.rs#L307-L314)

**Second check.** Searched beacon_processor for any multi-worker/permit logic (spawn_multi, worker counts) and the KZG/rust_eth_kzg 0.9.1 context for its own thread caps; none found, and the source PRs were closed unmerged.

**Sources.** [lighthouse#7720](https://github.com/sigp/lighthouse/pull/7720), [lighthouse#7789](https://github.com/sigp/lighthouse/pull/7789)

</details>


<a id="data_availability-096"></a>
<details>
<summary><b>data_availability-096</b> Reconstruct only when needed columns are missing — <i>partial · medium · S · cpu</i></summary>

**Idea.** Trigger reconstruction (and EL getBlobs) only when one of the node's own sampling or custody columns is still missing, not when any column is missing or all columns are already held; run it at lower thread priority.

**Gap in Lighthouse.** Trigger conditions are done (also for the Gloas pending_payload_cache path). Execution is on the HighPriority rayon pool, and the reconstruction queue is polled ahead of API p0 and attestations; no low-priority pool or OS thread niceness. Switching to RayonPoolType::LowPriority would complete it.

**Impact.** Marginally less interference with block import on supernodes; only supernodes reconstruct.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/custody_context.rs:492`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L492)
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:617`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L617)
- [`beacon_node/beacon_chain/src/pending_payload_cache/mod.rs:909-920`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/mod.rs#L909-L920)
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1488-1505`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1488-L1505)
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:645-650`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L645-L650)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3811`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3811)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3845`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3845)
- [`beacon_node/beacon_processor/src/lib.rs:953`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L953)

**Second check.** Checked the Gloas reconstruction path and the beacon processor queue order: the HighPriority pool is below the global pool, but nothing runs reconstruction at lowered priority.

**Sources.** [grandine@76504f279](https://github.com/grandinetech/grandine/commit/76504f279498), [grandine#521](https://github.com/grandinetech/grandine/pull/521), [lighthouse#5806](https://github.com/sigp/lighthouse/pull/5806), [lodestar#8536](https://github.com/ChainSafe/lodestar/pull/8536)

</details>


<a id="data_availability-097"></a>
<details>
<summary><b>data_availability-097</b> No reconstruction when serving column RPC — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** When serving data columns by range or by root, return only stored columns and do not run reconstruction for missing ones; the requester fetches them elsewhere.

**Impact.** Already avoids reconstruction cost on RPC serving.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:816`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L816) handle_data_columns_by_root_request_inner reads stored columns only
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:1765`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L1765) by_range inner likewise; grep for reconstruct in rpc_methods.rs finds only EL payload reconstruction

**Sources.** [lighthouse#8051](https://github.com/sigp/lighthouse/pull/8051)

</details>


<a id="data_availability-099"></a>
<details>
<summary><b>data_availability-099</b> Run gossip column KZG verification on blocking pool — <i>implemented · medium · latency, cpu</i></summary>

**Idea.** Run gossip data column KZG and signature verification on a blocking or rayon pool instead of inline on async runtime threads, so verification does not stall the async executor.

**Impact.** Async executor not stalled by gossip column verification.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2451-2474`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2451-L2474) verify_data_column_sidecar_for_gossip uses spawn_blocking_handle
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1139-1195`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1139-L1195) signature and KZG checks run inside that closure

**Sources.** [lighthouse#9271](https://github.com/sigp/lighthouse/pull/9271)

</details>


<a id="data_availability-100"></a>
<details>
<summary><b>data_availability-100</b> Operator flags to skip EL or blob handling — <i>not · low · M · disk, bandwidth</i></summary>

**Idea.** Offer operator flags to run without an EL or to skip blob gossip, RPC and availability checks for nodes that do not need them, saving storage and bandwidth.

**Gap in Lighthouse.** Would need a flag that disables column gossip subscriptions and DA checks in the network service and data_availability_checker; unsafe for validators, so only for non-validating nodes.

**Impact.** Saves large storage and bandwidth only for non-validating nodes that opt in; no effect on normal nodes.

**Best measured result.** 1.4TB storage reduction; 70% bandwidth reduction and 300Gb storage (pr:prysm#13841)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/src/cli.rs:944`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L944) only disable-get-blobs exists
- [`beacon_node/src/cli.rs:1046`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L1046) prune-blobs and cli.rs:1056 epochs-per-blob-prune only tune pruning
- [`beacon_node/src/cli.rs:845`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L845) execution-endpoint is required for a normal node; no flag to run without EL or skip DA/blob gossip

**Sources.** [prysm#13841](https://github.com/OffchainLabs/prysm/pull/13841)

</details>


<a id="data_availability-101"></a>
<details>
<summary><b>data_availability-101</b> Mark columns available before disk write completes — <i>n/a · low · S · latency</i></summary>

**Idea.** Update the availability cache and emit the availability event as soon as columns are queued for persistence, not after the filesystem write, and evict the entries if the write fails.

**Gap in Lighthouse.** Columns are persisted during block import, and the availability cache is memory-only, so availability is not gated on a separate column disk write.

**Impact.** None.

**Best measured result.** Shows DA waiting time before/after charts (images, no numbers) (pr:prysm#16137)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:483`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L483) put_kzg_verified_data_columns is in-memory only
- [`beacon_node/store/src/hot_cold_store.rs:1315`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1315) PutDataColumns written during block import

**Sources.** [prysm#16137](https://github.com/OffchainLabs/prysm/pull/16137)

</details>


<a id="data_availability-103"></a>
<details>
<summary><b>data_availability-103</b> Overflow pending DA cache to disk — <i>not · medium · L · memory</i></summary>

**Idea.** Bound the in-memory size of the pending blocks and blobs cache with an LRU that spills evicted entries to disk, so waiting data cannot exhaust memory.

**Gap in Lighthouse.** Pending components live in a bounded in-memory LruCache and evicted entries are dropped; the DBColumn::OverflowLRUCache column is marked DEPRECATED, so the disk spill from PR #4203 was removed. Would need an eviction hook writing PendingComponents to the hot DB and a read-back on miss.

**Impact.** Only matters under long non-finality or blob spam; no gain in normal operation, and Lighthouse removed it on purpose.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:351`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L351)
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:372`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L372)
- [`beacon_node/beacon_chain/src/pending_payload_cache/mod.rs:118`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/mod.rs#L118)
- [`beacon_node/store/src/lib.rs:409`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/lib.rs#L409)

**Second check.** Also checked the Gloas pending_payload_cache (in-memory LRU only) and the store columns: the overflow column survives only as a deprecated id.

**Sources.** [lighthouse#4203](https://github.com/sigp/lighthouse/pull/4203)

</details>


<a id="data_availability-105"></a>
<details>
<summary><b>data_availability-105</b> Compute column sidecars from blobs in parallel — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** When building data column sidecars from blobs or EL cell proofs (proposal or getBlobs), compute cells and columns in parallel across cores instead of sequentially.

**Impact.** Per-blob cell and proof computation already parallel; only the final column transposition (build_data_column_sidecars_*) may be sequential, which is cheap.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/kzg_utils.rs:344`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L344),401,437,477 into_par_iter over blobs in blobs_to_data_column_sidecars_*, compute_cells
- [`beacon_node/beacon_chain/src/kzg_utils.rs:907`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L907) reconstruction also parallel over blobs

**Sources.** [prysm#14396](https://github.com/OffchainLabs/prysm/pull/14396), [prysm#16115](https://github.com/OffchainLabs/prysm/pull/16115)

</details>


<a id="data_availability-108"></a>
<details>
<summary><b>data_availability-108</b> Reconstruct only requested blobs for blob API — <i>implemented · low · cpu, latency</i></summary>

**Idea.** When serving blobs through the API, recover only the requested blob rows (cell recovery only for those rows) instead of reconstructing all blobs of the block.

**Best measured result.** Half columns, 72 blobs: all 2.84 s vs single blob 73 ms; half of blobs 1.48 s (pr:lodestar#8567)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/kzg_utils.rs:767`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L767) reconstruct_blobs_with_indices recovers only requested rows
- [`beacon_node/beacon_chain/src/kzg_utils.rs:829`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L829) blob_indices_opt
- [`beacon_node/http_api/src/block_id.rs:436`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L436) passes requested indices

**Sources.** [lodestar#8567](https://github.com/ChainSafe/lodestar/pull/8567), [prysm#15813](https://github.com/OffchainLabs/prysm/pull/15813)

</details>


<a id="data_availability-109"></a>
<details>
<summary><b>data_availability-109</b> Request only custody cells from EL getBlobs — <i>implemented · medium · bandwidth, cpu</i></summary>

**Idea.** Use engine_getBlobsV4 with a per-blob cell bitmap so the EL returns only the cells for the node's custody columns instead of full blobs.

**Impact.** Already requests only custody cells, cutting EL to CL transfer.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:158-178`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L158-L178) uses engine_getBlobsV4 when supported
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:420-436`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L420-L436) CustodyColumnsBitArray from custody column indices passed to get_blobs_v4

**Sources.** [caplin#24088](https://github.com/erigontech/erigon/pull/24088)

</details>


<a id="data_availability-110"></a>
<details>
<summary><b>data_availability-110</b> Partial data column dissemination at cell granularity — <i>implemented · high · bandwidth, latency</i></summary>

**Idea.** Exchange data columns as gossipsub partial messages so peers send and request only the cells the other side lacks (tracked with per-peer bitmaps, served from held columns, verified with partial KZG checks) instead of whole column sidecars.

**Impact.** n/a

**Best measured result.** Tested on Hoodi and Sepolia; 'advantageous', no reports of reduced performance (pr:lighthouse#9896)

**Evidence (Lighthouse @ 928b61e719).**

- beacon_chain/src/partial_data_column_assembler.rs partial column assembler
- lighthouse_network/src/service/mod.rs:113 PartialDataColumnSidecar via gossipsub partial protocol
- network/src/network_beacon_processor/gossip_methods.rs:1060 partial verification, 1370 skips cells pending from EL

**Sources.** [lodestar#9053](https://github.com/ChainSafe/lodestar/pull/9053), [prysm#17065](https://github.com/OffchainLabs/prysm/pull/17065), [lighthouse#9896](https://github.com/sigp/lighthouse/pull/9896), [prysm#17348](https://github.com/OffchainLabs/prysm/pull/17348), [silver#287](https://github.com/gattaca-com/silver/pull/287), [silver#289](https://github.com/gattaca-com/silver/pull/289), [silver#282](https://github.com/gattaca-com/silver/pull/282)

</details>


<a id="data_availability-112"></a>
<details>
<summary><b>data_availability-112</b> Cooldown peers that return empty column responses — <i>not · low · S · bandwidth, sync</i></summary>

**Idea.** After a by-root column request returns zero sidecars, exclude that peer for a short cooldown in peer selection so download loops do not re-ask it many times per second.

**Gap in Lighthouse.** Record a per-peer last-empty time in ActiveCustodyRequest and skip such peers in select_column_peer for a few seconds.

**Impact.** Fewer redundant DataColumnsByRoot requests during lookups; small CPU and bandwidth gain.

**Best measured result.** one peer got 2,351 empty by-root requests in a minute (pr:caplin#24992)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context/custody.rs:243`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L243) empty response counted as success; comment admits many retries
- [`beacon_node/network/src/sync/network_context/custody.rs:238`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L238) select_column_peer has no empty-response cooldown

**Sources.** [caplin#24992](https://github.com/erigontech/erigon/pull/24992)

</details>


<a id="data_availability-113"></a>
<details>
<summary><b>data_availability-113</b> Filter column request peers by earliest available slot — <i>implemented · medium · sync</i></summary>

**Idea.** Select peers for sidecar requests using the earliest available slot they advertise in status, so requests do not go to peers that pruned the data.

**Impact.** Requests avoid peers that pruned the data.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/peerdb/sync_status.rs:35`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/peerdb/sync_status.rs#L35) has_slot uses earliest_available_slot
- [`beacon_node/lighthouse_network/src/peer_manager/peerdb.rs:297`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/peerdb.rs#L297) good_custody_subnet_peer filters by slot; globals.rs:201 custody_peers_for_column
- [`beacon_node/network/src/sync/network_context.rs:420`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L420) column requests use it; peerdb.rs:255 synced_peers_for_epoch used by backfill and custody backfill

**Sources.** [teku#10269](https://github.com/Consensys-Incorporated/teku/pull/10269)

</details>


<a id="data_availability-114"></a>
<details>
<summary><b>data_availability-114</b> Rank column peers by historical response rate — <i>not · medium · S · sync</i></summary>

**Idea.** Choose peers for column requests by past success rate (columns received versus requested), using free request capacity only as tiebreaker.

**Gap in Lighthouse.** Failure memory is per-lookup (peer_attempts) or per-batch (failed_peers) only; global peer score is a coarse filter. Keep per-peer columns-received/requested counters (PeerDB or SyncNetworkContext) and sort on them in select_column_peer and select_columns_by_range_peers_to_request before the random tiebreak.

**Impact.** Fewer failed custody column requests and retries in lookups and range sync; small sync latency gain, not CPU.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context/custody.rs:353`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L353) select_column_peer ranks by concurrency limit, lookup_peers, per-lookup peer_attempts, random hash
- [`beacon_node/network/src/sync/network_context.rs:578`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L578) select_columns_by_range_peers_to_request ranks by per-batch peers_to_deprioritize (batch.failed_peers), concurrency limit, random
- [`beacon_node/lighthouse_network/src/peer_manager/peerdb.rs:297`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/peerdb.rs#L297) good_custody_subnet_peer filters only by connected/good gossipsub score/custody/synced

**Sources.** [teku#10277](https://github.com/Consensys-Incorporated/teku/pull/10277)

</details>


<a id="data_availability-116"></a>
<details>
<summary><b>data_availability-116</b> Prune stale DA and quarantine entries by finality or expiry — <i>implemented · medium · memory</i></summary>

**Idea.** Prune the column quarantine, pending availability cache and related per-root caches on every finalization or pruning pass by slot or epoch, not only at a size threshold, so entries for blocks that never arrive cannot accumulate.

**Impact.** Already bounded by finality/epoch plus LRU capacity.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker.rs:744`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L744) maintenance with cutoff max(finalized+1,min_epochs_for_blobs)
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:720`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L720) do_maintenance removes by epoch
- [`beacon_node/beacon_chain/src/partial_data_column_assembler.rs:256`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/partial_data_column_assembler.rs#L256) assembler do_maintenance
- [`beacon_node/beacon_chain/src/canonical_head.rs:1615`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1615) observed_column_sidecars.prune; :1656 pending_payload_cache.do_maintenance

**Sources.** [nimbus#8693](https://github.com/status-im/nimbus-eth2/pull/8693), [nimbus#8691](https://github.com/status-im/nimbus-eth2/pull/8691), [lighthouse#5895](https://github.com/sigp/lighthouse/pull/5895), [nimbus#9139](https://github.com/status-im/nimbus-eth2/pull/9139), [teku#8128](https://github.com/Consensys-Incorporated/teku/pull/8128)

</details>


<a id="data_availability-117"></a>
<details>
<summary><b>data_availability-117</b> Store only original columns and rebuild extension on demand — <i>not · high · M · disk</i></summary>

**Idea.** On supernodes, store only the first-half (original) data columns plus the extension columns' KZG proofs, and rebuild the extension columns on demand with deduplicated work, about halving column storage.

**Gap in Lighthouse.** Supernodes store all 128 columns. To halve storage: persist only columns 0..63 plus the extension cell KZG proofs, and rebuild columns 64..127 in the hot_cold_store get_data_column(s) read path (RPC DataColumnsByRoot/ByRange and HTTP), with a dedup of concurrent rebuilds per block root and an LRU of rebuilt columns; needs a DB schema change and a migration.

**Impact.** Supernode column storage roughly halves (Teku: ~508 GB to ~260 GB at 14 blobs); no effect on non-supernodes; adds CPU on serving extension columns.

**Best measured result.** ~508 GB to ~260 GB stated in #10137 for 14 blobs (pr:teku#10132)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:959-1011`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L959-L1011) put_data_column(s) writes every custody column sidecar in full to DBColumn::BeaconDataColumn
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1348-1371`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1348-L1371) get_data_columns/get_data_column read the store directly; no rebuild step
- [`beacon_node/beacon_chain/src/migrate.rs:786`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L786),846 DeleteDataColumns only for pruned or abandoned-payload blocks, not for extension columns
- [`beacon_node/http_api/src/block_id.rs:370`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L370),436 reconstruction from stored columns only to serve blobs over HTTP, not to save storage
- [`beacon_node/beacon_chain/src/kzg_utils.rs:889`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L889) reconstruct_data_columns used only by the in-memory DA checker / pending payload cache

**Sources.** [teku#10132](https://github.com/Consensys-Incorporated/teku/pull/10132), [teku#10131](https://github.com/Consensys-Incorporated/teku/pull/10131), [teku#10508](https://github.com/Consensys-Incorporated/teku/pull/10508)

</details>


<a id="data_availability-118"></a>
<details>
<summary><b>data_availability-118</b> Clean legacy unpruned column buckets at startup — <i>n/a · low · S · disk</i></summary>

**Idea.** At startup, delete in batches columns in old storage buckets that the regular pruner never covers.

**Gap in Lighthouse.** Lighthouse uses one column DB bucket with no legacy unpruned buckets.

**Impact.** None.

**Best measured result.** 55,680 expired columns across 435 roots found on Hoodi (pr:lodestar#10223)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/lib.rs:261`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/lib.rs#L261) single DBColumn::BeaconDataColumn
- [`beacon_node/store/src/hot_cold_store.rs:1349`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1349) DeleteDataColumns in regular pruning

**Sources.** [lodestar#10223](https://github.com/ChainSafe/lodestar/pull/10223)

</details>


<a id="data_availability-120"></a>
<details>
<summary><b>data_availability-120</b> Skip rebroadcast of columns already seen on gossip — <i>implemented · medium · bandwidth, cpu</i></summary>

**Idea.** Before publishing columns built from EL blobs or reconstruction, skip those already received on gossip (mark them in the gossip seen cache) and those not from the current slot.

**Gap in Lighthouse.** No explicit current-slot-only check seen, but the observed-cache and DA dedupe give the main effect.

**Impact.** Avoids redundant column publishing bandwidth.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/mod.rs:1296`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L1296) publish_data_columns_gradually filters via observe_gossip_data_column (PriorKnown skipped)
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:642`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L642),720 EL-built columns deduped against gossip-observed and DA-cached columns

**Sources.** [nimbus#8668](https://github.com/status-im/nimbus-eth2/pull/8668), [prysm#15153](https://github.com/OffchainLabs/prysm/pull/15153), [teku#8675](https://github.com/Consensys-Incorporated/teku/pull/8675)

</details>


<a id="data_availability-122"></a>
<details>
<summary><b>data_availability-122</b> Query columns by slot range during sync — <i>implemented · medium · sync, bandwidth</i></summary>

**Idea.** Request data columns by slot range during sync instead of one by-root request per block.

**Gap in Lighthouse.** Range/backfill sync already use DataColumnsByRange; only single-block lookups use by-root, which is appropriate.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/network_context.rs:26`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L26),239 DataColumnsByRange requests used by range sync
- [`beacon_node/network/src/sync/range_data_column_batch_request.rs:17`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/range_data_column_batch_request.rs#L17) batches per-peer column by-range requests

**Sources.** [silver#31](https://github.com/gattaca-com/silver/pull/31)

</details>


<a id="data_availability-123"></a>
<details>
<summary><b>data_availability-123</b> Reconstruct without holding the DA cache lock — <i>implemented · low · latency</i></summary>

**Idea.** Run erasure-coding reconstruction outside the availability cache write lock and recheck the cache before publishing, so other columns keep being processed and duplicates are not published.

**Best measured result.** Logs show reconstruction blocked incoming column processing (~500ms between verify at 15.781 and reconstructed at 16.280) (pr:lighthouse#5986)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:592`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L592) check_and_set_reconstruction_started clones columns, then lock is released
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:560`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L560) reconstruct_columns runs outside lock
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:585`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L585) rechecks cached indices before publishing

**Sources.** [lighthouse#5986](https://github.com/sigp/lighthouse/pull/5986), [lighthouse#5990](https://github.com/sigp/lighthouse/pull/5990), [lighthouse#6403](https://github.com/sigp/lighthouse/pull/6403)

</details>


<a id="data_availability-125"></a>
<details>
<summary><b>data_availability-125</b> Wall-clock timeout on column reconstruction — <i>not · medium · S · latency</i></summary>

**Idea.** Bound column reconstruction with a wall-clock timeout checked before each per-blob task and while waiting for results, so slow recovery cannot stall the node.

**Gap in Lighthouse.** No wall-clock bound on the reconstruction itself. Check a deadline per blob row in kzg_utils::reconstruct_data_columns / around the awaited rayon task, and on expiry abort and reset reconstruction state.

**Impact.** Only matters for supernodes/semi-supernodes under slow recovery; protects the HighPriority rayon pool from stalls.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:3785`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3785) reconstruct_data_columns awaits spawn_blocking_with_rayon_async on HighPriority pool with no timeout
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:537`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L537) reconstruct_data_columns: timer metric only, failure resets via handle_reconstruction_failure, no deadline
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:107`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L107) RECONSTRUCTION_DEADLINE is a start trigger (1/4 slot), not an abort

**Sources.** [nimbus#7610](https://github.com/status-im/nimbus-eth2/pull/7610)

</details>


<a id="data_availability-126"></a>
<details>
<summary><b>data_availability-126</b> Minimum custody with full-subnet sampling mode — <i>partial · medium · M · bandwidth</i></summary>

**Idea.** Offer a mode that custodies the minimum column count but subscribes to 64 column subnets to reconstruct all columns, serving fewer RPC requests than a supernode.

**Gap in Lighthouse.** Semi-supernode reaches reconstruction by advertising and serving 64 columns. No mode keeps the advertised cgc at the minimum while subscribing to 64 subnets; would need a sampling-subscription count decoupled from the advertised cgc in CustodyContext/NetworkGlobals.

**Impact.** Reconstruct-capable node with fewer RPC serving duties; saves upload bandwidth versus semi-supernode.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/custody_context.rs:231`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L231) NodeCustodyType::SemiSupernode custodies and advertises number_of_custody_groups/2
- [`beacon_node/src/cli.rs:63`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L63) --semi-supernode flag
- [`beacon_node/lighthouse_network/src/types/globals.rs:68`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/globals.rs#L68) sampling_subnets derived from spec sampling_size_custody_groups(cgc), no separate override

**Sources.** [prysm#16014](https://github.com/OffchainLabs/prysm/pull/16014)

</details>


<a id="data_availability-129"></a>
<details>
<summary><b>data_availability-129</b> Gloas: check DA on the envelope, not the block — <i>implemented · medium · latency</i></summary>

**Idea.** For Gloas, check data availability on the execution payload envelope so the beacon block enters fork choice without waiting for columns, and do not refetch an envelope already held.

**Impact.** Block enters fork choice without waiting for columns in Gloas.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/pending_payload_cache/mod.rs:1-12`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/mod.rs#L1-L12) Gloas DA cache keyed by block root; envelope imported to fork choice once columns verified
- [`beacon_node/network/src/sync/block_lookups/single_block_lookup.rs:477`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/single_block_lookup.rs#L477) envelope request only sent for processing after block processed; completes if already received

**Sources.** [silver#377](https://github.com/gattaca-com/silver/pull/377)

</details>


<a id="data_availability-133"></a>
<details>
<summary><b>data_availability-133</b> Shorter per-request lifecycle for column recovery — <i>n/a · low · S · memory</i></summary>

**Idea.** Model column recovery as per-request objects with separate download and rebuild phases and one shorter timeout, so stale requests free resources sooner.

**Gap in Lighthouse.** Lighthouse reconstructs from columns already in the DA cache, with no separate recovery request or long recovery timeout.

**Impact.** None.

**Best measured result.** timeout 2 minutes rather than 5 (pr:teku#9910)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker.rs:537`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L537) reconstruct_data_columns uses columns already in cache, no download phase
- [`beacon_node/network/src/sync/network_context/custody.rs:22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context/custody.rs#L22) ActiveCustodyRequest already per-request

**Sources.** [teku#9910](https://github.com/Consensys-Incorporated/teku/pull/9910)

</details>


<a id="data_availability-134"></a>
<details>
<summary><b>data_availability-134</b> Pool and retry data-unavailable blocks — <i>implemented · medium · bandwidth, sync</i></summary>

**Idea.** Keep blocks that failed import for missing data in a pool and retry them after more waiting instead of dropping and refetching them.

**Gap in Lighthouse.** Blocks with missing data are kept in the DA cache and completed as columns arrive, so they are not dropped and refetched.

**Impact.** Avoids refetching blocks.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:351`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L351) pending components (block plus columns) held in LRU awaiting missing data
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:744`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L744) pruned only by cutoff epoch

**Sources.** [teku#7132](https://github.com/Consensys-Incorporated/teku/pull/7132)

</details>


<a id="data_availability-136"></a>
<details>
<summary><b>data_availability-136</b> Read-only head state for sidecar verification — <i>implemented · medium · cpu, memory</i></summary>

**Idea.** Verify data column and blob sidecars against the read-only head state when it has the same validator set and shuffling, instead of copying or regenerating the parent state.

**Impact.** Already avoids loading the parent state on the hot path; a proposer cache hit needs only the shuffling root and the global pubkey cache.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_column_verification.rs:1746`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1746) with_proposer_cache keyed by shuffling decision root; state loaded only inside the miss closure
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:197`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L197) OnceCell init, state_provider only called on miss

**Sources.** [prysm#15977](https://github.com/OffchainLabs/prysm/pull/15977)

</details>


<a id="data_availability-141"></a>
<details>
<summary><b>data_availability-141</b> Single shared buffer for all column sources — <i>partial · medium · M · memory</i></summary>

**Idea.** Write full gossip columns, partial cells and EL-built columns into one per-slot column cell cache, instead of separate caches, so one buffer serves all sources.

**Gap in Lighthouse.** Gloas already has one per-block cell buffer (PendingColumn) fed by gossip full columns, partial cells, RPC and EL getBlobs. Fulu, the live mainnet fork, still keeps partial and EL cells in PartialDataColumnAssembler and full columns in the overflow_lru_cache PendingComponents, which means double lookups and conversions. Porting the Gloas design back to Fulu is the remaining work. It may not be worth doing as Gloas will replace this path.

**Impact.** Fulu only: saves duplicate cache lookups and the partial-to-full copies per column. Small CPU and memory gain, not a bottleneck. Gloas already has it.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/pending_payload_cache/pending_components.rs:31-32`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/pending_components.rs#L31-L32) Gloas PendingComponents.verified_data_columns is a per-block HashMap&lt;ColumnIndex, PendingColumn&gt; of per-cell Option&lt;(Cell, KzgProof)&gt;, partial or full
- [`beacon_node/beacon_chain/src/pending_payload_cache/pending_components.rs:96-116`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/pending_components.rs#L96-L116) merge_data_columns writes full gossip/RPC columns cell-by-cell into the same PendingColumn store
- [`beacon_node/beacon_chain/src/pending_payload_cache/pending_components.rs:122-150`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/pending_components.rs#L122-L150) merge_partial_data_columns writes partial cells into that same store
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:368-386`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L368-L386) Gloas EL getBlobs columns merge into pending_payload_cache, the same store
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:326-363`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L326-L363) Fulu EL columns go into PartialDataColumnAssembler, then full columns go to the DA checker separately
- [`beacon_node/beacon_chain/src/partial_data_column_assembler.rs:13-34`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/partial_data_column_assembler.rs#L13-L34) Fulu PartialDataColumnAssembler is separate from overflow_lru_cache PendingComponents
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:230-270`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L230-L270) Fulu missing_cells_* consults both caches

**Second check.** The earlier review looked only at the Fulu path. I found that the Gloas pending_payload_cache already uses one cell-level store for all sources, including EL getBlobs. This leaves only the Fulu split, so the verdict stays partial.

**Sources.** [silver#299](https://github.com/gattaca-com/silver/pull/299), [silver#272](https://github.com/gattaca-com/silver/pull/272)

</details>


<a id="data_availability-142"></a>
<details>
<summary><b>data_availability-142</b> Singleflight proposer signature verification — <i>partial · medium · S · cpu</i></summary>

**Idea.** Deduplicate concurrent proposer signature verification for sidecars of the same block (singleflight keyed by signing data), so one parent-state load and BLS verify serves all its columns.

**Gap in Lighthouse.** The parent-state load is single-flight. Partial-column headers are verified once per block and then reused from the assembler cache, but this is not single-flight for concurrent first arrivals. Full Fulu gossip columns still do one header BLS verify per column, up to 128 per block, even when the assembler already holds a verified header with the same signed_block_header. Fix: in verify_proposer_and_signature, or before the call at line 1185, reuse the assembler's verified header (or a small verified-header-root cache) when the signed header matches. Gloas columns carry no signed header, so this applies to Fulu only.

**Impact.** A supernode would do about 1 header BLS verify per block instead of up to 128 (about 1 ms each). This saves tens of ms of CPU in the gossip burst on Fulu.

**Best measured result.** cache misses reduced (graph); up to 128 concurrent duplicates avoided (pr:prysm#15954)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:197`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L197) OnceCell makes the proposer shuffling/state load single-flight
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2490-2501`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2490-L2501) partial-column headers: a cached verified header for the block root skips re-verification (dedup after the first verify)
- [`beacon_node/beacon_chain/src/data_column_verification.rs:654-668`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L654-L668) GossipVerifiedPartialDataColumnHeader::new verifies the signature once, then caches the header in the assembler
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1185`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1185) the full gossip column path calls verify_proposer_and_signature for every column and does not check the assembler header cache
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1774-1787`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1774-L1787) the header BLS verify runs every time it is called

**Second check.** Beyond the earlier review, I found the verified-header cache for partial-column headers (assembler.get_header / was_cached). It dedups after the first verify, but the full-column gossip path does not use it, so the verdict stays partial.

**Sources.** [prysm#15954](https://github.com/OffchainLabs/prysm/pull/15954)

</details>


<a id="data_availability-143"></a>
<details>
<summary><b>data_availability-143</b> Skip DA check outside blob retention window — <i>implemented · medium · sync, bandwidth</i></summary>

**Idea.** Skip the data availability check and blob or column download for blocks older than the sidecar retention window during sync and checkpoint origin, since the data is not required.

**Impact.** Blocks older than the retention window already skip the DA check and column download.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/custody_context.rs:574-596`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L574-L596) da_check_required_for_epoch / data_columns_required_for_block use the DA boundary
- [`beacon_node/network/src/sync/block_lookups/single_block_lookup.rs:405`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/single_block_lookup.rs#L405) lookups request columns only when required
- [`beacon_node/network/src/sync/network_context.rs:1311`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L1311) range sync column requests gated by data_columns_required_for_epoch
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:867`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L867) availability check gated on columns_required

**Sources.** [grandine@0e2fd7284](https://github.com/grandinetech/grandine/commit/0e2fd7284103), [caplin#15806](https://github.com/erigontech/erigon/pull/15806), [prysm#13686](https://github.com/OffchainLabs/prysm/pull/13686)

</details>


<a id="data_availability-145"></a>
<details>
<summary><b>data_availability-145</b> Skip custody group derivation for supernodes — <i>implemented · low · cpu</i></summary>

**Idea.** When custody group count equals the total, return all groups directly instead of running the hash-based custody group computation.

**Best measured result.** described as slight optimization (pr:lodestar#8172)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/data/data_column_custody_group.rs:35`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/data/data_column_custody_group.rs#L35) returns 0..number_of_custody_groups when count equals total

**Sources.** [lodestar#8172](https://github.com/ChainSafe/lodestar/pull/8172), [lighthouse#7890](https://github.com/sigp/lighthouse/pull/7890), [teku#9709](https://github.com/Consensys-Incorporated/teku/pull/9709), [grandine@3139203d7](https://github.com/grandinetech/grandine/commit/3139203d7269)

</details>


<a id="data_availability-148"></a>
<details>
<summary><b>data_availability-148</b> Skip DA work for blocks without blob commitments — <i>implemented · low · cpu</i></summary>

**Idea.** For blocks with zero blob commitments, skip KZG validation, quarantine lookups and sampling trackers entirely.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:210`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L210) num_expected_blobs == 0 skips blob data
- [`beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs:973`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker/overflow_lru_cache.rs#L973) num_blobs_expected == 0 shortcut
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1542`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1542) commitments_len == 0 skips KZG

**Sources.** [lodestar#7184](https://github.com/ChainSafe/lodestar/pull/7184), [nimbus#7674](https://github.com/status-im/nimbus-eth2/pull/7674), [teku#10327](https://github.com/Consensys-Incorporated/teku/pull/10327)

</details>


<a id="data_availability-149"></a>
<details>
<summary><b>data_availability-149</b> Skip publishing columns while syncing — <i>implemented · medium · bandwidth, cpu</i></summary>

**Idea.** While the node is syncing, do not publish reconstructed or EL-recovered column sidecars to gossip.

**Impact.** Reconstruction (the source of published columns after gossip) is dropped while syncing, and the RPC-sync EL path never publishes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:228-330`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L228-L330) ColumnReconstruction and DataColumn work have drop_during_sync: true
- [`beacon_node/beacon_processor/src/lib.rs:1211`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1211) events dropped when sync_state.is_syncing()
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:216`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L216) RPC-sync EL fetch uses publish_blobs=false

**Sources.** [teku#10033](https://github.com/Consensys-Incorporated/teku/pull/10033), [teku#10103](https://github.com/Consensys-Incorporated/teku/pull/10103), [teku#10104](https://github.com/Consensys-Incorporated/teku/pull/10104)

</details>


<a id="data_availability-150"></a>
<details>
<summary><b>data_availability-150</b> Skip EL column compute for imported blocks — <i>implemented · medium · cpu</i></summary>

**Idea.** Before computing columns from EL blobs, check whether the block is already imported and skip the computation.

**Impact.** Redundant column computation for already imported blocks is skipped.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:271-278`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L271-L278) fork_choice_contains_block check before computing custody columns
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:485-490`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L485-L490) same check on the V4 path

**Sources.** [lighthouse#6816](https://github.com/sigp/lighthouse/pull/6816)

</details>


<a id="data_availability-152"></a>
<details>
<summary><b>data_availability-152</b> Store blobs Snappy-compressed as on the wire — <i>not · low · S · disk, cpu</i></summary>

**Idea.** Store blob sidecars on disk Snappy-compressed in the wire encoding, so no re-encoding is needed and storage is smaller.

**Gap in Lighthouse.** Compress the SSZ bytes in put_blobs/blobs_as_kv_store_ops (zstd via StoreConfig::compress_bytes, or snappy) and decompress in get_blobs; needs a schema/format marker or migration for existing uncompressed entries. Alternatively enable leveldb Snappy compression on the blobs DB. Storing in wire (ssz_snappy) format would only save re-encoding for RPC serving, which is minor since Lighthouse serves from the in-memory SSZ.

**Impact.** Blob DB disk footprint shrinks (rollup blobs often compress; zero top bytes of each field element give at least a few percent); modest CPU added per write/read. No meaningful hot-path gain; low value.

**Best measured result.** 38 GB on sepolia (pr:caplin#9500)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L931) put_blobs writes blobs.as_ssz_bytes() raw to blobs_db, no compression
- [`beacon_node/store/src/hot_cold_store.rs:943`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L943) blobs_as_kv_store_ops also raw SSZ
- [`beacon_node/store/src/database/leveldb_impl.rs:37`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/database/leveldb_impl.rs#L37) Options::new() with no compression set; leveldb-0.8.6 options.rs:72 defaults to Compression::No
- [`beacon_node/store/src/config.rs:198`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L198) compress_bytes (zstd) exists but is used for blocks/state diffs, not BeaconBlob

**Sources.** [caplin#9500](https://github.com/erigontech/erigon/pull/9500)

</details>


<a id="data_availability-154"></a>
<details>
<summary><b>data_availability-154</b> Staged blob reconstruction: concatenate first — <i>partial · medium · S · cpu, bandwidth</i></summary>

**Idea.** Rebuild blobs first by concatenating the original first-half columns without KZG, then recover from any half by erasure coding, and only then use the network.

**Gap in Lighthouse.** In reconstruct_blobs_with_indices, if columns 0..NUMBER_OF_COLUMNS/2 are all present, concatenate their cells directly. Otherwise recover only the polynomial and evaluate the cells, with no FK20 proof computation, because only blob bytes are needed. The network fallback stage does not apply to this API path.

**Impact.** Blob sidecar and blobs API serving from columns would skip RS recovery and FK20 proof generation per blob when the first half is stored. This is tens of ms per blob for supernodes and semi-supernodes that serve blob endpoints.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/kzg_utils.rs:797-815`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L797-L815) reconstruct_blobs_with_indices concatenates cells only when all 128 columns are present, otherwise it calls recover_cells_and_compute_kzg_proofs
- [`beacon_node/http_api/src/block_id.rs:501-533`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/block_id.rs#L501-L533) get_data_columns_for_blob_reconstruction passes every stored column, with no first-half check
- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/rust_eth_kzg-0.9.1/src/recovery.rs:22-66 recover_polynomial_coeff always runs the RS erasure recovery, with no fast path when there are no erasures in the first half
- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/rust_eth_kzg-0.9.1/src/prover.rs:156-171 recovery always also computes all 128 multi-opening proofs (FK20), which blob serving discards

**Second check.** I also checked the rust_eth_kzg 0.9.1 recovery and the http_api column loader for a hidden fast path. There is none, and recovery always computes proofs too, which makes the cost worse than the earlier review said.

**Sources.** [teku#10274](https://github.com/Consensys-Incorporated/teku/pull/10274)

</details>


<a id="data_availability-155"></a>
<details>
<summary><b>data_availability-155</b> Smaller pending-components cache capacity — <i>implemented · medium · memory</i></summary>

**Idea.** Use a small capacity for the pending-components DA cache because each entry grows with blob count and few are needed.

**Impact.** Cache already small; bounds memory at about 0.4 GB worst case.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker.rs:53`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L53) OVERFLOW_LRU_CAPACITY = 32 (down from 1024; doc sizes it for 48 blobs)

**Sources.** [lighthouse#7825](https://github.com/sigp/lighthouse/pull/7825)

</details>


<a id="data_availability-156"></a>
<details>
<summary><b>data_availability-156</b> Persist only custody columns — <i>implemented · medium · disk</i></summary>

**Idea.** Persist only the columns the node must custody, not extra sampled or reconstructed columns, to cut DB writes and storage.

**Impact.** Already saves DB writes for non-supernodes on the non-custody sampling columns.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:8407`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L8407) get_blobs_or_columns_store_op retains only custody_columns_for_epoch columns (unless supernode)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3503`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3503) sampling vs custody split

**Sources.** [lighthouse#8188](https://github.com/sigp/lighthouse/pull/8188), [prysm#14083](https://github.com/OffchainLabs/prysm/pull/14083)

</details>


<a id="data_availability-158"></a>
<details>
<summary><b>data_availability-158</b> Minimum custody until synced — <i>partial · medium · M · sync, bandwidth, disk</i></summary>

**Idea.** Custody only the minimum column count until the node has been synced for a while, then grow to the balance-based count.

**Gap in Lighthouse.** Lighthouse already syncs the historical backlog at minimum custody and defers column backfill until synced, because CGC changes are keyed to the wall-clock epoch. What is missing: (1) no sync-state input, so gossip subnets and the ENR go to full CGC during sync, and epochs after registration that are still being range-synced need full CGC; (2) a persisted high CGC (restart after downtime) is never reduced to the minimum while catching up; (3) there is no stability period. Adding a sync-status gate in CustodyContext::register_validators and in the CustodyCountChanged subscription would close it.

**Impact.** Smaller than the earlier estimate: the large part of the benefit (backlog columns at minimum custody during fresh checkpoint sync) already exists. What is left helps mostly a validator node that restarts after long downtime (catch-up range sync at full CGC) and cuts gossip column load during sync.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/custody_context.rs:120-135`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L120-L135) a CGC increase takes effect only from wall-clock (current_slot + delay).epoch + 1, so older epochs keep the old (minimum) CGC
- [`beacon_node/beacon_chain/src/custody_context.rs:468-511`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L468-L511) custody_group_count_at_epoch / sampling_columns_for_epoch fall back to custody_requirement for epochs before the first increase
- [`beacon_node/network/src/sync/network_context.rs:984-991`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/network_context.rs#L984-L991) range sync fetches columns with sampling_columns_for_epoch(block_epoch), so the sync backlog is downloaded at minimum custody
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:360-370`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L360-L370) RPC columns are filtered to the epoch's sampling columns
- [`beacon_node/network/src/sync/manager.rs:683-733`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L683-L733) custody (column) backfill for the higher CGC starts only once SyncState::Synced and block backfill is complete
- [`beacon_node/network/src/sync/manager.rs:738-757`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L738-L757) custody backfill is paused while range sync runs
- [`beacon_node/network/src/service.rs:786-795`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L786-L795) gossip column subnets and ENR CGC are raised at once, not deferred until synced

**Sources.** [nimbus#8205](https://github.com/status-im/nimbus-eth2/pull/8205)

</details>


<a id="data_availability-161"></a>
<details>
<summary><b>data_availability-161</b> Use EL blobs until block data is imported — <i>not · medium · S · bandwidth, latency</i></summary>

**Idea.** Keep the EL getBlobs response while the block's data (including Gloas payload) is not yet imported, instead of discarding it once the block is in fork choice.

**Gap in Lighthouse.** Replace the two fork_choice_contains_block checks in fetch_blobs/mod.rs with BeaconChain::is_block_data_imported through the adapter, and handle the duplicate payload import after a late merge (PR lighthouse#10488 is still open).

**Impact.** Gloas only: keeps the EL getBlobs response when the block is imported before its payload, which avoids fetching cells from peers. No effect on Fulu.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:272-279`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L272-L279) (V2/V3) and :485-491 (V4) return early on fork_choice_contains_block
- [`beacon_node/beacon_chain/src/fetch_blobs/fetch_blobs_beacon_adapter.rs:146-151`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/fetch_blobs_beacon_adapter.rs#L146-L151) fork_choice_contains_block is plain contains_block and does not check payload_received
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3898-3916`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3898-L3916) is_block_data_imported (Gloas payload_received aware) exists and is used only by gossip/RPC column paths (3463, 3508, 3592, 3715, 3798), not by fetch_blobs

**Sources.** [lighthouse#10488](https://github.com/sigp/lighthouse/pull/10488)

</details>


<a id="data_availability-162"></a>
<details>
<summary><b>data_availability-162</b> Verify availability-critical columns first — <i>not · medium · S · latency</i></summary>

**Idea.** Split KZG batch verification so the sidecars that make the block available are verified first and the remaining columns in a second batch.

**Gap in Lighthouse.** In put_rpc_custody_columns, filter to sampling columns before KZG verification, then split into the columns that complete availability and the remainder. Verify and import the first group, then verify the rest in a second call.

**Impact.** Small: saves a few ms of latency on RPC/lookup paths only. Gossip already verifies per column. Filtering before verification also saves verification work that is thrown away.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker.rs:356-372`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L356-L372) put_rpc_custody_columns KZG-verifies the whole batch first and filters it to sampling columns only after that (extra columns are verified too)
- [`beacon_node/beacon_chain/src/data_column_verification.rs:507-519`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L507-L519) from_batch_with_scoring does one verify_kzg_for_data_column_list call over all columns
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:495-530`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L495-L530) range-sync batch verification is also a single batch over all blocks

**Sources.** [silver#239](https://github.com/gattaca-com/silver/pull/239)

</details>


<a id="data_availability-163"></a>
<details>
<summary><b>data_availability-163</b> Verify sidecars before persisting — <i>implemented · medium · disk</i></summary>

**Idea.** During sync and backfill, verify sidecar KZG commitments before writing them, and store columns only after block viability is known.

**Impact.** Sidecars are verified in batch before writes during range sync and custody backfill, so no DB space is wasted on invalid columns.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker.rs:495`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L495) batch_verify_kzg_for_range_sync_blocks verifies before import
- [`beacon_node/beacon_chain/src/historical_data_columns.rs:170-205`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/historical_data_columns.rs#L170-L205) custody backfill verifies KZG on the batch before blobs_db.do_atomically(ops)
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:640-665`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L640-L665) verify helper using verify_kzg_for_data_column_list

**Sources.** [prysm#13060](https://github.com/OffchainLabs/prysm/pull/13060), [nimbus#7386](https://github.com/status-im/nimbus-eth2/pull/7386)

</details>


