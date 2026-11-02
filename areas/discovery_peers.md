# discovery_peers

40 ideas: 5 not, 7 partial, 26 implemented, 2 n/a; 5 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

Ids missing from the sequence are ideas that have not been checked against Lighthouse yet.

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [discovery_peers-001](#discovery_peers-001) | Cache ENR-derived node id | implemented | low |  | cpu |
| [discovery_peers-002](#discovery_peers-002) | O(1) hashmap-backed LRU for discv5 sessions | implemented | low |  | cpu, latency |
| [discovery_peers-003](#discovery_peers-003) **★** | Fewer peers and larger queues when subscribed to all subnets | partial | medium | S | bandwidth, cpu |
| [discovery_peers-005](#discovery_peers-005) | Dial discovered peers concurrently | implemented | medium |  | latency, sync, startup |
| [discovery_peers-009](#discovery_peers-009) | Back off when discovery finds nothing useful | implemented | low | S | cpu, bandwidth, memory |
| [discovery_peers-010](#discovery_peers-010) | Run first discovery query immediately at startup | implemented | low | S | startup, latency |
| [discovery_peers-012](#discovery_peers-012) **★** | Stop redialing peers that failed to connect | partial | medium | S | bandwidth, cpu |
| [discovery_peers-013](#discovery_peers-013) | Allow excess peers, then prune lowest-scoring | implemented | medium |  | bandwidth, cpu, memory, sync |
| [discovery_peers-014](#discovery_peers-014) | Bound discovered-node storage to k-buckets | implemented | low | S | memory, bandwidth |
| [discovery_peers-015](#discovery_peers-015) | Iterate connected peers, not the whole peer store | partial | low | S | cpu, latency |
| [discovery_peers-016](#discovery_peers-016) | Compute custody subnets once and store them | implemented | medium |  | cpu |
| [discovery_peers-018](#discovery_peers-018) | Cap concurrent outbound dial attempts | implemented | low | S | cpu, memory, bandwidth |
| [discovery_peers-020](#discovery_peers-020) | Close discovery iterators after use | n/a | medium |  | memory |
| [discovery_peers-021](#discovery_peers-021) | Reject excess inbound connections at transport layer | implemented | medium |  | cpu, bandwidth |
| [discovery_peers-022](#discovery_peers-022) | Keep minimum peers per subnet | implemented | medium |  | sync, latency, bandwidth, cpu |
| [discovery_peers-026](#discovery_peers-026) | Tune connection-manager grace and prune period | partial | low | S | cpu, bandwidth |
| [discovery_peers-027](#discovery_peers-027) | Run discovery request timeouts independently of read loop | implemented | low | S | sync |
| [discovery_peers-032](#discovery_peers-032) | Dial for a subnet only when it needs peers | partial | low | M | bandwidth, cpu |
| [discovery_peers-035](#discovery_peers-035) | Do not run unused libp2p services | implemented | low |  | bandwidth, cpu, startup |
| [discovery_peers-037](#discovery_peers-037) | Early filter and rate limit discv5 packets | implemented | medium |  | cpu, bandwidth |
| [discovery_peers-039](#discovery_peers-039) | Raise default target peer count | implemented | medium |  | bandwidth, memory, sync |
| [discovery_peers-042](#discovery_peers-042) | Avoid redundant Status re-requests | implemented | low | S | bandwidth, cpu |
| [discovery_peers-045](#discovery_peers-045) **★** | Evict stale peer-tracking sets | partial | medium | S | memory |
| [discovery_peers-048](#discovery_peers-048) | Retry peer search quickly after startup | implemented | low | S | startup, sync |
| [discovery_peers-050](#discovery_peers-050) | Filter ENRs inside the discovery service | implemented | medium |  | cpu, latency |
| [discovery_peers-051](#discovery_peers-051) | Discover subnet peers before publishing | partial | low | S | bandwidth, latency |
| [discovery_peers-055](#discovery_peers-055) | Search several subnets in one discovery query | implemented | low |  | bandwidth, cpu, latency |
| [discovery_peers-057](#discovery_peers-057) | Reject banned peers before handshake | implemented | low |  | cpu, bandwidth |
| [discovery_peers-067](#discovery_peers-067) | Stop discovery when peer target is reached | implemented | low | S | cpu, bandwidth |
| [discovery_peers-069](#discovery_peers-069) | Cooldown before reconnecting disconnected peers | implemented | low | S | bandwidth, cpu |
| [discovery_peers-071](#discovery_peers-071) | Preallocate subnet bitfield decode buffers | n/a | low |  | cpu, memory |
| [discovery_peers-072](#discovery_peers-072) | Prefix-targeted subnet peer search | not | low | M | bandwidth, latency |
| [discovery_peers-073](#discovery_peers-073) | Protect useful peers from random pruning | implemented | low |  | latency, bandwidth |
| [discovery_peers-074](#discovery_peers-074) **★** | Prune non-sync peers while syncing | not | medium | M | sync, bandwidth |
| [discovery_peers-076](#discovery_peers-076) | Ping peers less often | not | low | S | cpu, bandwidth |
| [discovery_peers-081](#discovery_peers-081) | Count pending dials against the peer limit | implemented | low |  | cpu, bandwidth, latency |
| [discovery_peers-082](#discovery_peers-082) | Skip ENRs with no dialable address | implemented | low |  | bandwidth, cpu, latency |
| [discovery_peers-087](#discovery_peers-087) | Throttle random discovery lookup rate | implemented | low |  | cpu, bandwidth, latency |
| [discovery_peers-090](#discovery_peers-090) **★** | Churn peers when head is starved | not | medium | M | bandwidth, sync |
| [discovery_peers-092](#discovery_peers-092) | Lookup-table decode of ENR subnet bitfields | not | low | S | cpu |

★ actionable. Click an id for the full record.

## Ideas

<a id="discovery_peers-001"></a>
<details>
<summary><b>discovery_peers-001</b> Cache ENR-derived node id — <i>implemented · low · cpu</i></summary>

**Idea.** Store the node id (keccak of the public key) on the ENR object once it is computed, so discovery code does not hash the key again each time the id is needed. Check the discv5 Enr type and its node_id() accessor.

**Best measured result.** pr:lodestar#3419: "critical ENR node id cache performance fix"

**Evidence (Lighthouse @ 928b61e719).**

- enr-0.14.0/src/lib.rs:244 node_id field stored on Enr
- enr-0.14.0/src/lib.rs:275-276 node_id() returns cached value
- enr-0.14.0/src/lib.rs:529,595,1199 node_id computed on build/set_public_key/decode only

**Sources.** [lodestar#3419](https://github.com/ChainSafe/lodestar/pull/3419), [teku#4810](https://github.com/Consensys-Incorporated/teku/pull/4810), [teku#4823](https://github.com/Consensys-Incorporated/teku/pull/4823)

</details>


<a id="discovery_peers-002"></a>
<details>
<summary><b>discovery_peers-002</b> O(1) hashmap-backed LRU for discv5 sessions — <i>implemented · low · cpu, latency</i></summary>

**Idea.** Keep discv5 sessions in a hashmap-backed LRU with O(1) get/insert instead of a list-based LRU that scans all entries (~5k sessions) on every access.

**Best measured result.** pr:lighthouse#2577: O(N) over ~5k sessions to O(1)

**Evidence (Lighthouse @ 928b61e719).**

- discv5-0.12.0/src/handler/mod.rs:220 sessions: LruTimeCache&lt;NodeAddress, Session&gt;
- discv5-0.12.0/src/lru_time_cache.rs:1-60 hashlink LinkedHashMap, O(1) insert/get/to_back
- [`beacon_node/lighthouse_network/src/config.rs:326`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L326) session_cache_capacity(5000)

**Sources.** [lighthouse#2577](https://github.com/sigp/lighthouse/pull/2577)

</details>


<a id="discovery_peers-003"></a>
<details>
<summary><b>discovery_peers-003</b> Fewer peers and larger queues when subscribed to all subnets — <i>partial · medium · S · bandwidth, cpu</i></summary>

**Idea.** When the node subscribes to all attestation/column subnets, lower the default peer target and raise gossip queue sizes, because each peer already covers every subnet and extra peers only add duplicate traffic.

**Gap in Lighthouse.** Queue half is already covered: the attestation queues are always sized for the subscribe-all worst case from the validator count. Missing half: subscribe_all_subnets (or supernode) does not lower the default target_peers; add that in beacon_node/src/config.rs when --target-peers is not given.

**Impact.** Only for subscribe-all/supernode nodes: fewer duplicate gossip copies and less per-peer CPU. Small.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_queue.rs:356`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_queue.rs#L356) attestation_queue sized as active_validators/slots_per_epoch: 'Capacity for a full slot's worth of attestations if subscribed to all subnets', applied to every node
- [`beacon_node/beacon_processor/src/scheduler/work_queue.rs:361`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_queue.rs#L361) unknown_block_attestation_queue same subscribe-all sizing
- [`beacon_node/client/src/builder.rs:757`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L757) queue lengths derived from state at startup
- [`beacon_node/src/config.rs:1197`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/config.rs#L1197) subscribe-all-subnets only sets the flag, no target_peers change
- [`beacon_node/lighthouse_network/src/peer_manager/config.rs:11`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/config.rs#L11) DEFAULT_TARGET_PEERS fixed

**Second check.** Read BeaconProcessorQueueLengths::from_state: queues are not static, they scale with active validator count and are explicitly sized for a subscribe-all node, so the larger-queues half exists unconditionally. Grepped every subscribe_all_subnets/supernode use; none changes target_peers.

**Sources.** [teku#8387](https://github.com/Consensys-Incorporated/teku/pull/8387)

</details>


<a id="discovery_peers-005"></a>
<details>
<summary><b>discovery_peers-005</b> Dial discovered peers concurrently — <i>implemented · medium · latency, sync, startup</i></summary>

**Idea.** Dial discovered peers in parallel (one task per dial, with a generous concurrency cap) instead of one at a time, so a slow or dead peer does not block the dial loop and a fresh node reaches its target sooner.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs:107`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs#L107) one ToSwarm::Dial per poll, swarm dials concurrently
- [`beacon_node/lighthouse_network/src/service/mod.rs:443`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L443) with_max_pending_outgoing(16) cap

**Sources.** [prysm#5021](https://github.com/OffchainLabs/prysm/pull/5021), [nimbus#1100](https://github.com/status-im/nimbus-eth2/pull/1100), [nimbus#2966](https://github.com/status-im/nimbus-eth2/pull/2966), [nimbus#1016](https://github.com/status-im/nimbus-eth2/pull/1016)

</details>


<a id="discovery_peers-009"></a>
<details>
<summary><b>discovery_peers-009</b> Back off when discovery finds nothing useful — <i>implemented · low · S · cpu, bandwidth, memory</i></summary>

**Idea.** When too few candidates exist (small devnet, empty routing table) or a query returns only useless results, back off instead of immediately re-querying, and bound lookup count by routing table size. This stops discovery from spinning a full core.

**Impact.** Prevents a spin on small/devnet networks; negligible on mainnet.

**Best measured result.** pr:prysm#14446: CPU from a whole core to near idle on small devnets

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:385-396`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L385-L396) skips recursive query when results&gt;0 but no useful peers
- metric DISCOVERY_NO_USEFUL_ENRS
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:365-376`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L365-L376) discover_peers dedups via find_peer_active, capped by FIND_NODE_QUERY_CLOSEST_PEERS

**Sources.** [prysm#14446](https://github.com/OffchainLabs/prysm/pull/14446), [prysm#6848](https://github.com/OffchainLabs/prysm/pull/6848), [lighthouse#6207](https://github.com/sigp/lighthouse/pull/6207)

</details>


<a id="discovery_peers-010"></a>
<details>
<summary><b>discovery_peers-010</b> Run first discovery query immediately at startup — <i>implemented · low · S · startup, latency</i></summary>

**Idea.** Make the discovery service fully initialized before the first peer-manager heartbeat, so the first random query starts at once instead of being skipped until the next interval (~30s).

**Impact.** Saves at most the ~30s before the first query at boot.

**Best measured result.** pr:lodestar#4980: removes a 30s wait before the first query

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:171`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L171) tokio::time::interval, whose first tick fires immediately
- [`beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs:46`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs#L46) heartbeat polled at once, calling maintain_peer_count(0)
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:340`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L340) started set at construction

**Sources.** [lodestar#5618](https://github.com/ChainSafe/lodestar/pull/5618), [lodestar#4980](https://github.com/ChainSafe/lodestar/pull/4980)

</details>


<a id="discovery_peers-012"></a>
<details>
<summary><b>discovery_peers-012</b> Stop redialing peers that failed to connect — <i>partial · medium · S · bandwidth, cpu</i></summary>

**Idea.** After a failed outbound dial, mark the peer as unreachable for a period (temporary ban or failure count) and drop its ENR from the dial cache, so discovery does not dial the same dead peer again.

**Gap in Lighthouse.** The drop-from-cache half is done (and the DHT entry is marked disconnected, which only lowers its eviction priority). No temporary unreachable mark or failure counter: a dead ENR returned again by a later discv5 query passes should_dial and is redialed. Add a per-peer dial-failure backoff checked in should_dial/peers_discovered.

**Impact.** Saves repeated dials to dead peers and pending-outgoing slots; minor.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/discovery/mod.rs:1215`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L1215) Discovery::on_dial_failure handles Transport/NoAddresses/WrongPeerId/Denied by calling disconnect_peer
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:660`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L660) disconnect_peer marks node disconnected in discv5 DHT and removes it from cached_enrs 'to prevent redialing disconnected peers'
- [`beacon_node/lighthouse_network/src/service/mod.rs:1355`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L1355) remove_cached_enr before dialing cached subnet ENRs
- [`beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs:336`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs#L336) peer manager on_dial_failure only inject_disconnect, no failure count
- [`beacon_node/lighthouse_network/src/peer_manager/peerdb.rs:153`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/peerdb.rs#L153) should_dial accepts Disconnected peers with no backoff
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:350`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L350) peers_discovered dials any ENR not in peers_to_dial

**Second check.** Found the discovery behaviour's own DialFailure handler (missed by the earlier review), which removes the ENR from cached_enrs and marks it disconnected in discv5; this is lighthouse#2382's fix. Still no time-based ban or failure count anywhere in peer_manager/peerdb.

**Sources.** [prysm#3390](https://github.com/OffchainLabs/prysm/pull/3390), [lighthouse#2382](https://github.com/sigp/lighthouse/pull/2382), [teku#1399](https://github.com/Consensys-Incorporated/teku/pull/1399)

</details>


<a id="discovery_peers-013"></a>
<details>
<summary><b>discovery_peers-013</b> Allow excess peers, then prune lowest-scoring — <i>implemented · medium · bandwidth, cpu, memory, sync</i></summary>

**Idea.** Accept peers up to target times an excess factor and, at heartbeat, disconnect the lowest-value or lowest-score peers down to target, so newly discovered useful peers always have room and the max is actually enforced.

**Best measured result.** pr:prysm#4106: peer count reduced to threshold

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:65`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L65) PEER_EXCESS_FACTOR, :75 PRIORITY_PEER_EXCESS
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:1307`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L1307) prune_excess_peers at heartbeat, score-first pruning :1360

**Sources.** [nimbus#2888](https://github.com/status-im/nimbus-eth2/pull/2888), [nimbus#917](https://github.com/status-im/nimbus-eth2/pull/917), [prysm#4106](https://github.com/OffchainLabs/prysm/pull/4106), [lighthouse#1383](https://github.com/sigp/lighthouse/pull/1383)

</details>


<a id="discovery_peers-014"></a>
<details>
<summary><b>discovery_peers-014</b> Bound discovered-node storage to k-buckets — <i>implemented · low · S · memory, bandwidth</i></summary>

**Idea.** Store discovered nodes only in the Kademlia k-buckets (no side lists of all seen nodes), so the memory for node records has a fixed upper bound, and keep recursive lookups selecting the closest peers.

**Impact.** Memory for node records is already bounded.

**Best measured result.** pr:teku#4185: upper bound on number of nodes stored in memory

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/discv5-0.12.0/src/kbucket.rs discv5 stores nodes only in k-buckets
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:161`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L161),333 cached_enrs is an LruCache(ENR_CACHE_CAPACITY), bounded

**Sources.** [teku#4185](https://github.com/Consensys-Incorporated/teku/pull/4185)

</details>


<a id="discovery_peers-015"></a>
<details>
<summary><b>discovery_peers-015</b> Iterate connected peers, not the whole peer store — <i>partial · low · S · cpu, latency</i></summary>

**Idea.** In heartbeats and subnet peer searches, iterate only currently connected peers (from the connection manager or peer DB index) instead of enumerating every known peer in the store, which also holds many disconnected or other-network peers.

**Gap in Lighthouse.** Every heartbeat and subnet query does a full scan of the PeerDB (up to ~1500+ entries) filtered by is_connected; no connected-peer index. Keep a HashSet of connected PeerIds updated in the connection state transitions and iterate it in connected_peers, connected_or_dialing_peers, good_peers_on_subnet.

**Impact.** A linear scan of at most a couple thousand in-memory entries every 30s and per subnet query; microseconds, not measurable on a mainnet node.

**Best measured result.** pr:lodestar#2238: peerStore.peers took 400-1000ms

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/peerdb.rs:209-227`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/peerdb.rs#L209-L227) connected_peers/connected_or_dialing_peers filter over the whole peers map
- [`beacon_node/lighthouse_network/src/peer_manager/peerdb.rs:281-293`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/peerdb.rs#L281-L293) good_peers_on_subnet scans all peers
- [`beacon_node/lighthouse_network/src/peer_manager/peerdb.rs:27`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/peerdb.rs#L27) MAX_DC_PEERS=500 and MAX_BANNED_PEERS=1000 bound the map

**Sources.** [lodestar#2238](https://github.com/ChainSafe/lodestar/pull/2238), [lodestar#1902](https://github.com/ChainSafe/lodestar/pull/1902)

</details>


<a id="discovery_peers-016"></a>
<details>
<summary><b>discovery_peers-016</b> Compute custody subnets once and store them — <i>implemented · medium · cpu</i></summary>

**Idea.** Compute the node's own custody subnets/columns once at startup and each peer's custody subnets once on connect or metadata update, store them in network globals and the peer DB, and read them instead of recomputing per data column query.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/globals.rs:70-80`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/globals.rs#L70-L80) own custody subnets computed once at startup
- [`beacon_node/lighthouse_network/src/peer_manager/peerdb/peer_info.rs:50`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/peerdb/peer_info.rs#L50) custody_subnets stored per peer
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:809`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L809) set on metadata update

**Sources.** [lighthouse#6308](https://github.com/sigp/lighthouse/pull/6308), [lighthouse#6218](https://github.com/sigp/lighthouse/pull/6218)

</details>


<a id="discovery_peers-018"></a>
<details>
<summary><b>discovery_peers-018</b> Cap concurrent outbound dial attempts — <i>implemented · low · S · cpu, memory, bandwidth</i></summary>

**Idea.** Track in-flight outbound dials and cap them at a small fixed number (with a semaphore or counter), so a burst of discovery results does not open hundreds of sockets and tasks at once.

**Impact.** Bounds sockets and tasks during discovery bursts.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/mod.rs:444-446`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L444-L446) with_max_pending_outgoing(Some(16)) in libp2p connection_limits
- [`beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs:107`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs#L107) one dial emitted per poll from peers_to_dial
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:364-368`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L364-L368) dial gated by target/max peer counts

**Sources.** [silver#54](https://github.com/gattaca-com/silver/pull/54), [lighthouse#1469](https://github.com/sigp/lighthouse/pull/1469), [nimbus#1460](https://github.com/status-im/nimbus-eth2/pull/1460), [caplin#11861](https://github.com/erigontech/erigon/pull/11861)

</details>


<a id="discovery_peers-020"></a>
<details>
<summary><b>discovery_peers-020</b> Close discovery iterators after use — <i>n/a · medium · memory</i></summary>

**Idea.** Close discv5 node iterators when a subnet peer search ends, so the iterators and their buffered nodes do not leak and cause OOM.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/discovery/mod.rs:851`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L851) find_node_predicate future pushed to active_queries, dropped on completion

**Sources.** [prysm#12388](https://github.com/OffchainLabs/prysm/pull/12388)

</details>


<a id="discovery_peers-021"></a>
<details>
<summary><b>discovery_peers-021</b> Reject excess inbound connections at transport layer — <i>implemented · medium · cpu, bandwidth</i></summary>

**Idea.** Enforce the peer limit at the transport/swarm layer (connection gater, connection limits, or closing the listener) so excess inbound peers are refused before identify, gossipsub subscriptions and Status/Metadata exchange run.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/mod.rs:441-459`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L441-L459) libp2p connection_limits (incoming/outgoing/total caps)
- [`beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs:156`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs#L156) handle_pending_inbound_connection rejects banned IPs

**Sources.** [lodestar#5033](https://github.com/ChainSafe/lodestar/pull/5033), [prysm#6243](https://github.com/OffchainLabs/prysm/pull/6243), [prysm#4214](https://github.com/OffchainLabs/prysm/pull/4214), [lighthouse#2455](https://github.com/sigp/lighthouse/pull/2455)

</details>


<a id="discovery_peers-022"></a>
<details>
<summary><b>discovery_peers-022</b> Keep minimum peers per subnet — <i>implemented · medium · sync, latency, bandwidth, cpu</i></summary>

**Idea.** Track which attestation, sync and custody column subnets each peer serves, keep a minimum peer count per subnet (dialing past the limit or triggering discovery when below it), and prune so peers stay spread across subnets.

**Best measured result.** pr:lodestar#8057: 25-35 peers on all subnets on devnet-2

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:61`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L61) MIN_SAMPLING_COLUMN_SUBNET_PEERS, :996 maintain_custody_peers
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:957`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L957) maintain_sync_committee_peers
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:1383`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L1383) prune keeps peers spread over custody subnets
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:773`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L773) TARGET_SUBNET_PEERS for attestation subnets

**Sources.** [lighthouse#7915](https://github.com/sigp/lighthouse/pull/7915), [lodestar#8057](https://github.com/ChainSafe/lodestar/pull/8057), [caplin#11057](https://github.com/erigontech/erigon/pull/11057)

</details>


<a id="discovery_peers-026"></a>
<details>
<summary><b>discovery_peers-026</b> Tune connection-manager grace and prune period — <i>partial · low · S · cpu, bandwidth</i></summary>

**Idea.** Use a high-watermark buffer with a short grace period and a short pruning interval for excess peers, so over-limit peers are pruned promptly without connect/disconnect churn, and protect bootnodes from pruning.

**Gap in Lighthouse.** Excess peers are pruned only on the 30s heartbeat and there is a 600s PEER_RECONNECTION_TIMEOUT instead of a short grace. Explicit bootnode protection from pruning was not found. Could run prune_excess_peers on a shorter timer and exempt boot ENRs.

**Impact.** Minor: peer count churn and bootnode connections; no measurable CPU change.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:49-50`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L49-L50) HEARTBEAT_INTERVAL=30s; prune_excess_peers runs in heartbeat (mod.rs:1479)
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:61-75`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L61-L75) PEER_EXCESS_FACTOR=0.1 buffer, PRIORITY_PEER_EXCESS=0.2
- [`beacon_node/lighthouse_network/src/service/mod.rs:441-459`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L441-L459) hard connection limits at the excess size

**Sources.** [prysm#6184](https://github.com/OffchainLabs/prysm/pull/6184), [prysm#4109](https://github.com/OffchainLabs/prysm/pull/4109), [prysm#4110](https://github.com/OffchainLabs/prysm/pull/4110)

</details>


<a id="discovery_peers-027"></a>
<details>
<summary><b>discovery_peers-027</b> Run discovery request timeouts independently of read loop — <i>implemented · low · S · sync</i></summary>

**Idea.** Drive discovery request timeouts from their own timer task so a blocked packet read loop cannot stall them, and match unsolicited responses by ip:port when the node id is not yet known.

**Impact.** Timeouts already do not depend on the read loop; unsolicited-response ip:port matching was not checked.

**Best measured result.** pr:caplin#8661: found 13/76/91 peers after 12h where it previously found none

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/discv5-0.12.0/src/handler/mod.rs:314,372 active_requests is a delay-based structure polled in the handler's tokio::select, independent of the packet read
- discv5 0.12.0 is the Lighthouse dependency

**Sources.** [caplin#8661](https://github.com/erigontech/erigon/pull/8661)

</details>


<a id="discovery_peers-032"></a>
<details>
<summary><b>discovery_peers-032</b> Dial for a subnet only when it needs peers — <i>partial · low · M · bandwidth, cpu</i></summary>

**Idea.** Dial a discovered peer for a subnet only when that subnet's mesh is short of peers, choosing candidates by the subnets they cover, instead of connecting to every ENR that advertises the subnet.

**Gap in Lighthouse.** Queries are issued only when a subnet needs peers, but results are dialed regardless of whether that subnet is still short or which subnets the candidate covers. In peers_discovered, check per-subnet deficit for the query's subnets and rank candidates by covered needed subnets.

**Impact.** Fewer unneeded dials and later prunes during subnet searches; small effect on mainnet CPU or bandwidth.

**Best measured result.** pr:lodestar#5782: ~10 long-lived subnets per peer instead of 50

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/discovery/mod.rs:766-781`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L766-L781) start_subnet_query skips the query when good_peers_on_subnet &gt;= TARGET_SUBNET_PEERS
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:351-382`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L351-L382) peers_discovered dials every returned ENR when under max/priority peer limits, with no per-subnet need check

**Sources.** [nimbus#2668](https://github.com/status-im/nimbus-eth2/pull/2668), [lodestar#5782](https://github.com/ChainSafe/lodestar/pull/5782)

</details>


<a id="discovery_peers-035"></a>
<details>
<summary><b>discovery_peers-035</b> Do not run unused libp2p services — <i>implemented · low · bandwidth, cpu, startup</i></summary>

**Idea.** Do not construct or run network behaviours that the node does not use (circuit relay, hop, libp2p ping, disabled UPnP), so they cause no streams, multicast traffic or startup work.

**Impact.** Nothing to gain; relay, libp2p ping, hop are absent and UPnP is opt-in.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/mod.rs:134-160`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L134-L160) Behaviour has only connection_limits, peer_manager, rpc, discovery, identify, upnp, gossipsub: no relay/ping/autonat
- [`beacon_node/lighthouse_network/src/service/mod.rs:462-466`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L462-L466) UPnP in Toggle, built only if upnp_enabled

**Sources.** [lodestar@901fc65e7](https://github.com/ChainSafe/lodestar/commit/901fc65e7c87), [prysm#7345](https://github.com/OffchainLabs/prysm/pull/7345), [lighthouse#6170](https://github.com/sigp/lighthouse/pull/6170)

</details>


<a id="discovery_peers-037"></a>
<details>
<summary><b>discovery_peers-037</b> Early filter and rate limit discv5 packets — <i>implemented · medium · cpu, bandwidth</i></summary>

**Idea.** Rate-limit and drop unsolicited or junk UDP packets at the start of the discv5 packet handler, before decryption and session work.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/config.rs:325`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L325) enable_packet_filter()
- [`beacon_node/lighthouse_network/src/config.rs:305-338`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L305-L338) total/ip/node rate limiter, max bans/nodes per ip
- discv5-0.12.0/src/socket/recv.rs:198-201 filter.initial_pass before decode/decrypt

**Sources.** [lighthouse#1274](https://github.com/sigp/lighthouse/pull/1274)

</details>


<a id="discovery_peers-039"></a>
<details>
<summary><b>discovery_peers-039</b> Raise default target peer count — <i>implemented · medium · bandwidth, memory, sync</i></summary>

**Idea.** Raise the default target peer count so the node covers all custody columns and subnets with a more diverse peer set; gossipsub mesh bounds keep the bandwidth cost small (+2.6% in, +5.8% out for 2x peers).

**Best measured result.** pr:lighthouse#7877: peers 91-&gt;183 cost inbound +2.6%, outbound +5.8%, memory +~8%

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/config.rs:11`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/config.rs#L11) DEFAULT_TARGET_PEERS = 200
- [`beacon_node/lighthouse_network/src/config.rs:355`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L355) default target_peers

**Sources.** [lighthouse#7877](https://github.com/sigp/lighthouse/pull/7877), [caplin#11820](https://github.com/erigontech/erigon/pull/11820), [nimbus#1130](https://github.com/status-im/nimbus-eth2/pull/1130)

</details>


<a id="discovery_peers-042"></a>
<details>
<summary><b>discovery_peers-042</b> Avoid redundant Status re-requests — <i>implemented · low · S · bandwidth, cpu</i></summary>

**Idea.** Re-request peer Status only on a slow period (every few slots or epochs), refresh a peer's last-status timestamp on every update, and stop periodic re-requests once synced, instead of re-asking every peer each slot or epoch.

**Gap in Lighthouse.** Only difference: Status keeps being re-requested every 5 min once synced instead of stopping; cost is negligible.

**Impact.** About 1 Status per peer per 5 min already; stopping when synced saves a few tiny RPCs per minute.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/config.rs:2`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/config.rs#L2) DEFAULT_STATUS_INTERVAL=300s
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:405`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L405) peer_statusd re-inserts peer in status_peers (timer reset on every Status)
- [`beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs:84-97`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs#L84-L97) periodic Status skipped while syncing

**Sources.** [grandine@993779a34](https://github.com/grandinetech/grandine/commit/993779a34eda), [prysm#4152](https://github.com/OffchainLabs/prysm/pull/4152), [lodestar#1328](https://github.com/ChainSafe/lodestar/pull/1328)

</details>


<a id="discovery_peers-045"></a>
<details>
<summary><b>discovery_peers-045</b> Evict stale peer-tracking sets — <i>partial · medium · S · memory</i></summary>

**Idea.** Bound or periodically prune side caches and sets of peer ids (every peer ever seen, per-peer side caches) so they do not grow without limit.

**Gap in Lighthouse.** banned_peers_per_ip keeps one key per IP (IPv6 /56) ever banned; counts go to 0 but the entry stays. Remove the key when the count reaches 0 in BannedPeersCount::remove_banned_peer. sigp PR 10259 (peerdb cache eviction fixes) is still open.

**Impact.** Small memory growth on long-running nodes (one HashMap entry per banned IP prefix); no CPU effect.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/peerdb.rs:1187-1230`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/peerdb.rs#L1187-L1230) shrink_to_fit bounds banned peers (MAX_BANNED_PEERS) and disconnected peers (MAX_DC_PEERS), called from inject_disconnect at :1172
- [`beacon_node/lighthouse_network/src/peer_manager/peerdb.rs:1415-1420`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/peerdb.rs#L1415-L1420) BannedPeersCount.banned_peers_per_ip HashMap&lt;IpAddr,usize&gt;
- [`beacon_node/lighthouse_network/src/peer_manager/peerdb.rs:1444-1452`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/peerdb.rs#L1444-L1452) remove_banned_peer decrements with saturating_sub but never removes zero-count keys
- [`beacon_node/lighthouse_network/src/peer_manager/peerdb.rs:1466-1481`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/peerdb.rs#L1466-L1481) banned_ips/ip_is_banned only read, never prune
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:161`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L161),333 cached_enrs is an LruCache

**Second check.** Re-read the whole BannedPeersCount impl and shrink_to_fit: no retain/remove on banned_peers_per_ip anywhere, so the leak is real; the main peer map is bounded.

**Sources.** [lighthouse#10259](https://github.com/sigp/lighthouse/pull/10259), [lodestar#3565](https://github.com/ChainSafe/lodestar/pull/3565)

</details>


<a id="discovery_peers-048"></a>
<details>
<summary><b>discovery_peers-048</b> Retry peer search quickly after startup — <i>implemented · low · S · startup, sync</i></summary>

**Idea.** Right after startup, retry peer search with short (about 1s) delays and drop duplicate immediate attempts, so first peers connect in seconds instead of half a minute.

**Gap in Lighthouse.** Possible small gap: a query returning results but zero dialable ones waits for the 30s heartbeat (mod.rs:389-398).

**Impact.** Only startup time to first peers; seconds, no steady-state effect.

**Best measured result.** pr:teku#6139: first peers at ~14s instead of ~43s after startup

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:171`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L171) heartbeat interval (first tick immediate, then 30s)
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:351-401`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L351-L401) peers_discovered re-queues discovery at once when a query returns nothing and more peers are needed
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:365-374`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L365-L374) discover_peers dedups with find_peer_active
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:227`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L227) bootnode ENRs preloaded

**Sources.** [teku#6139](https://github.com/Consensys-Incorporated/teku/pull/6139)

</details>


<a id="discovery_peers-050"></a>
<details>
<summary><b>discovery_peers-050</b> Filter ENRs inside the discovery service — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** Filter discovered ENRs for relevance (fork digest, subnet fields) inside the discovery service/thread and stop emitting an event per crawled ENR, so irrelevant records never reach the main network loop.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/discovery/mod.rs:831-844`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L831-L844) fork-digest and dialable-address predicate passed to discv5 find_node_predicate, inside the query
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:1077-1085`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L1077-L1085) discv5::Event::Discovered is ignored, no per-ENR event to the network loop
- [`beacon_node/lighthouse_network/src/config.rs:331`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L331) disable_report_discovered_peers

**Sources.** [lodestar#5104](https://github.com/ChainSafe/lodestar/pull/5104), [lighthouse#1693](https://github.com/sigp/lighthouse/pull/1693)

</details>


<a id="discovery_peers-051"></a>
<details>
<summary><b>discovery_peers-051</b> Discover subnet peers before publishing — <i>partial · low · S · bandwidth, latency</i></summary>

**Idea.** Before broadcasting an attestation on a subnet with no known peers, run discovery for that subnet and wait for at least one peer, so the message reaches someone.

**Gap in Lighthouse.** Lighthouse discovers subnet peers ahead of time and re-sends cached messages when a peer subscribes, but starts no discovery at publish time for an empty topic. Add a discover_subnet_peers call in the NoPeersSubscribedToTopic branch of publish.

**Impact.** Rare case; small inclusion gain since proactive discovery already runs.

**Best measured result.** pr:prysm#7610: attestation inclusion improvement of 6% or more

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/mod.rs:850-900`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L850-L900) publish: NoPeersSubscribedToTopic only caches message in gossip_cache for retry
- beacon_node/lighthouse_network/src/../network/src/service.rs:879-880 subnet discovery driven by subnet service from validator subscriptions, not by publish
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:380-389`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L380-L389) discover_subnet_peers

**Sources.** [prysm#7610](https://github.com/OffchainLabs/prysm/pull/7610)

</details>


<a id="discovery_peers-055"></a>
<details>
<summary><b>discovery_peers-055</b> Search several subnets in one discovery query — <i>implemented · low · bandwidth, cpu, latency</i></summary>

**Idea.** Combine peer searches for several wanted subnets into one discovery query or one filtered iterator that accepts peers matching any wanted subnet, instead of one query per subnet.

**Impact.** Already one discv5 query per group of subnets.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/discovery/mod.rs:721-735`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L721-L735) queued subnet queries grouped up to MAX_SUBNETS_IN_QUERY into one query
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:758-806`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L758-L806) start_subnet_query uses one subnet_predicate over filtered_subnets
- [`beacon_node/lighthouse_network/src/discovery/subnet_predicate.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/subnet_predicate.rs) predicate accepts a peer on any wanted subnet

**Sources.** [lighthouse#1364](https://github.com/sigp/lighthouse/pull/1364), [prysm#8048](https://github.com/OffchainLabs/prysm/pull/8048), [prysm#15471](https://github.com/OffchainLabs/prysm/pull/15471)

</details>


<a id="discovery_peers-057"></a>
<details>
<summary><b>discovery_peers-057</b> Reject banned peers before handshake — <i>implemented · low · cpu, bandwidth</i></summary>

**Idea.** On every inbound connection, check the ban list and close banned peers before the Status handshake, so a banned peer cannot trigger a handshake on each reconnect.

**Impact.** Banned peers are rejected at swarm level; no Status handshake.

**Best measured result.** pr:caplin#23606: 101 handshake attempts to one peer in 2 min; 13,827 failures across 1,638 peers in 90 min

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs:156-179`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs#L156-L179) handle_pending_inbound_connection denies banned IPs
- [`beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs:182-195`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs#L182-L195) handle_established_inbound_connection denies banned peer ids before Status
- [`beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs:222-235`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs#L222-L235) same on outbound

**Sources.** [caplin#23606](https://github.com/erigontech/erigon/pull/23606)

</details>


<a id="discovery_peers-067"></a>
<details>
<summary><b>discovery_peers-067</b> Stop discovery when peer target is reached — <i>implemented · low · S · cpu, bandwidth</i></summary>

**Idea.** Start discovery queries only when there is a free peer slot and the connected (and outbound) peer count is below target, and ease lookup frequency as the target is approached, instead of querying at a fixed fast rate.

**Gap in Lighthouse.** No graduated slowdown near target, but queries stop at target (30s heartbeat).

**Impact.** Discovery already idle at target.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:1041-1070`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L1041-L1070) maintain_peer_count emits DiscoverPeers only when connected_or_dialing &lt; target or outbound below min
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:365-374`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L365-L374) skipped if FindPeers already active
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:389-398`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L389-L398) recursion stops on no useful results

**Sources.** [ethlambda#605](https://github.com/lambdaclass/ethlambda/pull/605), [prysm#6346](https://github.com/OffchainLabs/prysm/pull/6346), [lighthouse#2993](https://github.com/sigp/lighthouse/pull/2993), [nimbus#2243](https://github.com/status-im/nimbus-eth2/pull/2243)

</details>


<a id="discovery_peers-069"></a>
<details>
<summary><b>discovery_peers-069</b> Cooldown before reconnecting disconnected peers — <i>implemented · low · S · bandwidth, cpu</i></summary>

**Idea.** After a disconnect (longer for serious goodbye reasons), keep the peer in a time-limited ban/cooldown list checked at the swarm layer and by discovery before dialing, so peers are not redialed or accepted in loops while at the limit.

**Gap in Lighthouse.** Cooldown is one 10 min period, not scaled by goodbye reason; serious reasons go through score bans.

**Impact.** Prevents redial loops; already in place.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:55`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L55) PEER_RECONNECTION_TIMEOUT=600s; line 198 temporary_banned_peers LRUTimeCache
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:300-308`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L300-L308) temp ban pushes PeerManagerEvent::Banned when at target
- [`beacon_node/lighthouse_network/src/service/mod.rs:1960-1965`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L1960-L1965) Banned calls discovery ban_peer; peer_manager/mod.rs:458-470 dial_peer checks should_dial

**Sources.** [prysm#7726](https://github.com/OffchainLabs/prysm/pull/7726), [lodestar#8067](https://github.com/ChainSafe/lodestar/pull/8067), [teku#1312](https://github.com/Consensys-Incorporated/teku/pull/1312), [lighthouse#3757](https://github.com/sigp/lighthouse/pull/3757), [lodestar#8044](https://github.com/ChainSafe/lodestar/pull/8044)

</details>


<a id="discovery_peers-071"></a>
<details>
<summary><b>discovery_peers-071</b> Preallocate subnet bitfield decode buffers — <i>n/a · low · cpu, memory</i></summary>

**Idea.** When decoding ENR subnet bitfields or set-bit indices, allocate the output once at the right size instead of growing or concatenating intermediate arrays.

**Impact.** Negligible.

**Best measured result.** pr:lodestar#10382: ~1.1us/op to ~310ns/op; 5M calls 4914ms to 710ms

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/discovery/enr.rs:58`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/enr.rs#L58) from_ssz_bytes

**Sources.** [prysm#6507](https://github.com/OffchainLabs/prysm/pull/6507), [lodestar#10382](https://github.com/ChainSafe/lodestar/pull/10382)

</details>


<a id="discovery_peers-072"></a>
<details>
<summary><b>discovery_peers-072</b> Prefix-targeted subnet peer search — <i>not · low · M · bandwidth, latency</i></summary>

**Idea.** Search for subnet peers by targeting node ids whose prefix maps to the subnet (deterministic subnet-to-node-id mapping) instead of random targets, so each query finds more subnet peers per request.

**Gap in Lighthouse.** Add a subnet-to-target-node-id mapping and pass prefix-matching targets in start_query/start_subnet_query.

**Impact.** Fewer discv5 bytes per subnet peer found; minor CPU/bandwidth, up to a few x on subnet queries.

**Best measured result.** pr:lighthouse#5090: ~3x discovery bytes/nodes found vs random search

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/discovery/mod.rs:849`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L849) NodeId::random() target
- [`beacon_node/lighthouse_network/src/discovery/subnet_predicate.rs:10`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/subnet_predicate.rs#L10) predicate filters results only

**Sources.** [lighthouse#5090](https://github.com/sigp/lighthouse/pull/5090)

</details>


<a id="discovery_peers-073"></a>
<details>
<summary><b>discovery_peers-073</b> Protect useful peers from random pruning — <i>implemented · low · latency, bandwidth</i></summary>

**Idea.** Tag in-use or useful peers as protected in the connection manager so that over-limit pruning does not drop them at random and cause churn and redials.

**Best measured result.** pr:lodestar#4997: peer connection length metric improved

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:1136`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L1136) should_protect_peer

**Sources.** [lodestar#4997](https://github.com/ChainSafe/lodestar/pull/4997)

</details>


<a id="discovery_peers-074"></a>
<details>
<summary><b>discovery_peers-074</b> Prune non-sync peers while syncing — <i>not · medium · M · sync, bandwidth</i></summary>

**Idea.** While not synced, disconnect peers that do not support sync protocols and a share of the lowest-scored sync peers each heartbeat, so slots free up for useful sync peers.

**Gap in Lighthouse.** No step disconnects Behind or low-score peers while the local node is syncing. Add a sync-state-aware branch in the PeerManager heartbeat (sync state is already in network_globals) that drops Behind/Unknown peers and a share of the lowest scored peers when SyncingFinalized/SyncingHead. The 'no sync protocol' part has no analogue in eth2.

**Impact.** Could speed initial/catch-up sync when slots are full of unhelpful peers; no steady-state saving; target peer count is high so benefit is uncertain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:1307`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L1307) prune_excess_peers has no sync-state input
- [`beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs:83-99`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs#L83-L99) the only sync-state use in the peer manager: status re-polls are paused while syncing (the opposite of pruning)
- [`beacon_node/network/src/network_beacon_processor/rpc_methods.rs:164-170`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/rpc_methods.rs#L164-L170) process_status sends Goodbye IrrelevantNetwork only for wrong fork / different finalized chain, independent of our sync state
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:1237`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L1237) is_synced_or_advanced only a sort key in custody-subnet pruning

**Second check.** Also checked network_behaviour.rs, sync/network_context goodbye_peer callers and status relevance checks: only fork/finality relevance disconnects exist, nothing tied to local sync state.

**Sources.** [lodestar#1683](https://github.com/ChainSafe/lodestar/pull/1683), [lodestar@b903a21d5](https://github.com/ChainSafe/lodestar/commit/b903a21d54c7)

</details>


<a id="discovery_peers-076"></a>
<details>
<summary><b>discovery_peers-076</b> Ping peers less often — <i>not · low · S · cpu, bandwidth</i></summary>

**Idea.** Ping connected peers at about the rate peers ping us (minutes, not seconds), to cut network work competing for the main thread.

**Gap in Lighthouse.** Raise the two default intervals in peer_manager/config.rs (to minutes) while keeping metadata seq-number refresh via pings.

**Impact.** Roughly 10x fewer ping req/resp over ~100 peers; small CPU saving (about 5-10 pings/s down to under 1).

**Best measured result.** pr:lodestar#2974: ping interval 4.01 min derived from metrics

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/config.rs:5`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/config.rs#L5) DEFAULT_PING_INTERVAL_OUTBOUND=15
- [`beacon_node/lighthouse_network/src/peer_manager/config.rs:8`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/config.rs#L8) DEFAULT_PING_INTERVAL_INBOUND=20
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:194`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L194) HashSetDelay ping timers

**Sources.** [lodestar#2974](https://github.com/ChainSafe/lodestar/pull/2974)

</details>


<a id="discovery_peers-081"></a>
<details>
<summary><b>discovery_peers-081</b> Count pending dials against the peer limit — <i>implemented · low · cpu, bandwidth, latency</i></summary>

**Idea.** Count in-flight dials toward the max/target peer count and skip dialing peers the connection limits would reject, so no dials or discovery queries are wasted near the limit.

**Best measured result.** pr:nimbus#2443: fewer failed dials/discovery requests near max peers (screenshots)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:354`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L354) connected_or_dialing + to_dial_peers
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:1041`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L1041) maintain_peer_count subtracts dialing_peers
- [`beacon_node/lighthouse_network/src/service/mod.rs:441`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L441) connection_limits

**Sources.** [nimbus@adcae8d41](https://github.com/status-im/nimbus-eth2/commit/adcae8d4161c), [nimbus#2443](https://github.com/status-im/nimbus-eth2/pull/2443), [lighthouse#5111](https://github.com/sigp/lighthouse/pull/5111)

</details>


<a id="discovery_peers-082"></a>
<details>
<summary><b>discovery_peers-082</b> Skip ENRs with no dialable address — <i>implemented · low · bandwidth, cpu, latency</i></summary>

**Idea.** Before dialing, skip ENRs with zero TCP/QUIC ports or no usable multiaddr (for example discovery-only bootnodes), so no dial slot or retry is spent on undialable records.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:459`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L459) dial_peer empty dialable_multiaddrs
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:834`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L834) eth2_fork_predicate dialable check

**Sources.** [lodestar#7712](https://github.com/ChainSafe/lodestar/pull/7712), [lighthouse#9580](https://github.com/sigp/lighthouse/pull/9580), [caplin#22271](https://github.com/erigontech/erigon/pull/22271), [nimbus#8710](https://github.com/status-im/nimbus-eth2/pull/8710)

</details>


<a id="discovery_peers-087"></a>
<details>
<summary><b>discovery_peers-087</b> Throttle random discovery lookup rate — <i>implemented · low · cpu, bandwidth, latency</i></summary>

**Idea.** Space discovery lookups out (sleep between random lookups, longer polling period) and connect to a bounded number of candidates per lookup, to cut queries per second and their CPU.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/discovery/mod.rs:366`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L366) find_peer_active guard
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:71`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L71) FIND_NODE_QUERY_CLOSEST_PEERS
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:64`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L64) MAX_CONCURRENT_SUBNET_QUERIES
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:51`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L51) HEARTBEAT_INTERVAL=30

**Sources.** [prysm#5050](https://github.com/OffchainLabs/prysm/pull/5050), [prysm#5488](https://github.com/OffchainLabs/prysm/pull/5488), [lodestar#3129](https://github.com/ChainSafe/lodestar/pull/3129)

</details>


<a id="discovery_peers-090"></a>
<details>
<summary><b>discovery_peers-090</b> Churn peers when head is starved — <i>not · medium · M · bandwidth, sync</i></summary>

**Idea.** During long non-finality, detect a starved head and churn extra useless peers while keeping peers far ahead of us, so the node finds peers that can serve it.

**Gap in Lighthouse.** No detection of a starved head (head unchanged and behind wall clock) and no extra churn in that state. Add a check in the PeerManager heartbeat that, when starved, prunes extra useless peers below target and exempts peers whose head is far ahead.

**Impact.** Helps recovery during long non-finality or stalls only; no steady-state saving.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:1307`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L1307) prune_excess_peers runs only above target and has no head-progress check
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:1219-1243`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L1219-L1243) find_prune_candidate sorts by (custody_subnet_count, is_synced_or_advanced): a weak tie-break that prunes behind peers first, not a protection for peers far ahead
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:1442`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L1442) heartbeat has no starvation detector

**Second check.** Grepped peer_manager, sync and discovery for stall/starve/stuck/head_slot logic; only the is_synced_or_advanced sort key in custody pruning touches peer head state, which is not the starvation mechanism.

**Sources.** [lodestar#7508](https://github.com/ChainSafe/lodestar/pull/7508)

</details>


<a id="discovery_peers-092"></a>
<details>
<summary><b>discovery_peers-092</b> Lookup-table decode of ENR subnet bitfields — <i>not · low · S · cpu</i></summary>

**Idea.** Decode ENR attnets/syncnets bitfields with a precomputed byte-to-bits table and no exceptions, instead of the generic SSZ bitvector path.

**Gap in Lighthouse.** Replace the BitVector decode in subnet_predicate/enr.rs with a direct bit test on the raw ENR bytes.

**Impact.** Negligible on a mainnet node; discovery is a tiny CPU share.

**Best measured result.** pr:lodestar#3550: x20 faster than ssz BitVector implementation

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/discovery/enr.rs:58`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/enr.rs#L58) attestation_bitfield from_ssz_bytes
- [`beacon_node/lighthouse_network/src/discovery/subnet_predicate.rs:17`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/subnet_predicate.rs#L17) per-ENR decode in predicate

**Sources.** [lodestar#3550](https://github.com/ChainSafe/lodestar/pull/3550)

</details>


