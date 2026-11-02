# discovery_peers

104 ideas: 12 not, 18 partial, 56 implemented, 18 n/a; 5 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [discovery_peers-001](#discovery_peers-001) | Cache ENR-derived node id | implemented | low | S | cpu |
| [discovery_peers-002](#discovery_peers-002) | O(1) hashmap-backed LRU for discv5 sessions | implemented | low | S | cpu, latency |
| [discovery_peers-003](#discovery_peers-003) **★** | Fewer peers and larger queues when subscribed to all subnets | partial | medium | S | bandwidth, cpu |
| [discovery_peers-004](#discovery_peers-004) | Array-indexed peer table with one control-loop sweep | not | low | M | cpu |
| [discovery_peers-005](#discovery_peers-005) | Dial discovered peers concurrently | implemented | low | S | latency, sync, startup |
| [discovery_peers-006](#discovery_peers-006) | Use random discv5 lookups, not local-table sampling | implemented | low | S | bandwidth, sync, cpu |
| [discovery_peers-007](#discovery_peers-007) | Send peer status requests off the main loop | implemented | low | S | latency |
| [discovery_peers-008](#discovery_peers-008) | Do cheap checks before taking peer-collection lock | partial | low | S | cpu, latency |
| [discovery_peers-009](#discovery_peers-009) | Back off when discovery finds nothing useful | implemented | low | S | cpu, bandwidth, memory |
| [discovery_peers-010](#discovery_peers-010) | Run first discovery query immediately at startup | implemented | low | S | startup, latency |
| [discovery_peers-011](#discovery_peers-011) | Await identify instead of polling peerstore | n/a | low | S | latency |
| [discovery_peers-012](#discovery_peers-012) **★** | Stop redialing peers that failed to connect | partial | medium | S | bandwidth, cpu |
| [discovery_peers-013](#discovery_peers-013) | Allow excess peers, then prune lowest-scoring | implemented | medium | S | bandwidth, cpu, memory, sync |
| [discovery_peers-014](#discovery_peers-014) | Bound discovered-node storage to k-buckets | implemented | low | S | memory, bandwidth |
| [discovery_peers-015](#discovery_peers-015) | Iterate connected peers, not the whole peer store | partial | low | S | cpu, latency |
| [discovery_peers-016](#discovery_peers-016) | Compute custody subnets once and store them | implemented | medium | S | cpu |
| [discovery_peers-017](#discovery_peers-017) | Keep per-connection peer data in memory | implemented | low | S | disk, cpu |
| [discovery_peers-018](#discovery_peers-018) | Cap concurrent outbound dial attempts | implemented | low | S | cpu, memory, bandwidth |
| [discovery_peers-019](#discovery_peers-019) | Plain message passing from discovery thread | n/a | low | S | cpu |
| [discovery_peers-020](#discovery_peers-020) | Close discovery iterators after use | n/a | medium |  | memory |
| [discovery_peers-021](#discovery_peers-021) | Reject excess inbound connections at transport layer | implemented | medium | S | cpu, bandwidth |
| [discovery_peers-022](#discovery_peers-022) | Keep minimum peers per subnet | implemented | medium | S | sync, latency, bandwidth, cpu |
| [discovery_peers-023](#discovery_peers-023) | Compact LRU for discv5 caches | n/a | low | S | memory |
| [discovery_peers-024](#discovery_peers-024) | Allow concurrent discv5 requests to one peer | implemented | low | S | latency |
| [discovery_peers-025](#discovery_peers-025) | Timeout on outbound peer connect | implemented | low | S | latency |
| [discovery_peers-026](#discovery_peers-026) | Tune connection-manager grace and prune period | partial | low | S | cpu, bandwidth |
| [discovery_peers-027](#discovery_peers-027) | Run discovery request timeouts independently of read loop | implemented | low | S | sync |
| [discovery_peers-028](#discovery_peers-028) | Deduplicate peers in the dial queue | implemented | low | S | bandwidth, cpu |
| [discovery_peers-029](#discovery_peers-029) | Skip subnet query while one is unexpired | partial | low | S | bandwidth, cpu |
| [discovery_peers-030](#discovery_peers-030) | Request metadata only after peer-limit check | implemented | low | S | bandwidth |
| [discovery_peers-031](#discovery_peers-031) | Delay queues for discv5 timeouts | implemented | low | S | latency, cpu |
| [discovery_peers-032](#discovery_peers-032) | Dial for a subnet only when it needs peers | partial | low | M | bandwidth, cpu |
| [discovery_peers-033](#discovery_peers-033) | Fix discv5 lookup slowdown | n/a | low | S | cpu, latency |
| [discovery_peers-034](#discovery_peers-034) | Dial cached matching ENRs before subnet query | implemented | low | S | latency, sync |
| [discovery_peers-035](#discovery_peers-035) | Do not run unused libp2p services | implemented | low | S | bandwidth, cpu, startup |
| [discovery_peers-036](#discovery_peers-036) | Drop libp2p connection manager when client prunes itself | n/a | low | S | cpu |
| [discovery_peers-037](#discovery_peers-037) | Early filter and rate limit discv5 packets | implemented | medium | S | cpu, bandwidth |
| [discovery_peers-038](#discovery_peers-038) | Run discovery in a separate worker thread | implemented | low | S | cpu, latency |
| [discovery_peers-039](#discovery_peers-039) | Raise default target peer count | implemented | medium | S | bandwidth, memory, sync |
| [discovery_peers-040](#discovery_peers-040) | Do not write ENR to disk on every change | partial | low | S | disk |
| [discovery_peers-041](#discovery_peers-041) | No mainnet bootnodes on custom networks | implemented | low | S | bandwidth |
| [discovery_peers-042](#discovery_peers-042) | Avoid redundant Status re-requests | implemented | low | S | bandwidth, cpu |
| [discovery_peers-043](#discovery_peers-043) | Subnet discovery as soon as duties are known | implemented | low | S | latency |
| [discovery_peers-044](#discovery_peers-044) | Skip peer-status scan when already synced | implemented | low | S | cpu |
| [discovery_peers-045](#discovery_peers-045) **★** | Evict stale peer-tracking sets | partial | medium | S | memory |
| [discovery_peers-046](#discovery_peers-046) | Optimise discovery ExpirationSet structure | n/a | low |  | cpu |
| [discovery_peers-047](#discovery_peers-047) | Fast secp256k1 for discv5 signatures | partial | low | M | cpu |
| [discovery_peers-048](#discovery_peers-048) | Retry peer search quickly after startup | implemented | low | S | startup, sync |
| [discovery_peers-049](#discovery_peers-049) | Cheaper best-finalized-peer selection | partial | low | S | cpu |
| [discovery_peers-050](#discovery_peers-050) | Filter ENRs inside the discovery service | implemented | medium | S | cpu, latency |
| [discovery_peers-051](#discovery_peers-051) | Discover subnet peers before publishing | partial | low | S | bandwidth, latency |
| [discovery_peers-052](#discovery_peers-052) | Fix discv5 thread deadlock | implemented | low | S | cpu |
| [discovery_peers-053](#discovery_peers-053) | No thread or task leaks in discovery | n/a | low |  | memory, cpu |
| [discovery_peers-054](#discovery_peers-054) | Gate subnet discovery by fork activation | implemented | low | S | cpu, bandwidth |
| [discovery_peers-055](#discovery_peers-055) | Search several subnets in one discovery query | implemented | low | S | bandwidth, cpu, latency |
| [discovery_peers-056](#discovery_peers-056) | Count peers per subnet in one pass | partial | low | S | cpu |
| [discovery_peers-057](#discovery_peers-057) | Reject banned peers before handshake | implemented | low | S | cpu, bandwidth |
| [discovery_peers-058](#discovery_peers-058) | Ignore connect events for closed connections | n/a | low |  | cpu |
| [discovery_peers-059](#discovery_peers-059) | In-process p2p calls instead of local RPC | n/a | low | S | latency, cpu |
| [discovery_peers-060](#discovery_peers-060) | Do not serialize ENR in peer filter | implemented | low | S | cpu, memory |
| [discovery_peers-061](#discovery_peers-061) | Cap pending inbound connections and backlog | partial | low | S | cpu, memory |
| [discovery_peers-062](#discovery_peers-062) | Scale per-subnet peer target to total peers | partial | low | S | bandwidth, cpu |
| [discovery_peers-063](#discovery_peers-063) | Skip subnet filtering of peers during sync | implemented | low | S | sync, bandwidth |
| [discovery_peers-064](#discovery_peers-064) | Do not block startup on bootstrap connectivity | partial | low | S | startup, latency |
| [discovery_peers-065](#discovery_peers-065) | Omit UDP port to avoid serving FINDNODE | n/a | low | S | memory |
| [discovery_peers-066](#discovery_peers-066) | Drive discovery on demand from peer manager | implemented | medium | S | cpu, bandwidth |
| [discovery_peers-067](#discovery_peers-067) | Stop discovery when peer target is reached | implemented | low | S | cpu, bandwidth |
| [discovery_peers-068](#discovery_peers-068) | Pass ENRs between threads without re-encoding | n/a | low |  | cpu |
| [discovery_peers-069](#discovery_peers-069) | Cooldown before reconnecting disconnected peers | partial | low | S | bandwidth, cpu |
| [discovery_peers-070](#discovery_peers-070) | Persist known peers across restarts | implemented | low | S | startup, sync |
| [discovery_peers-071](#discovery_peers-071) | Preallocate subnet bitfield decode buffers | n/a | low |  | cpu, memory |
| [discovery_peers-072](#discovery_peers-072) | Prefix-targeted subnet peer search | not | low | M | bandwidth, latency |
| [discovery_peers-073](#discovery_peers-073) | Protect useful peers from random pruning | implemented | low | S | latency, bandwidth |
| [discovery_peers-074](#discovery_peers-074) **★** | Prune non-sync peers while syncing | not | medium | M | sync, bandwidth |
| [discovery_peers-075](#discovery_peers-075) | Linear capability exchange loop | n/a | low |  | cpu |
| [discovery_peers-076](#discovery_peers-076) | Ping peers less often | not | low | S | cpu, bandwidth |
| [discovery_peers-077](#discovery_peers-077) | Fine-grained locks in network globals | implemented | low | S | latency |
| [discovery_peers-078](#discovery_peers-078) | Shorter idle connection timeout | partial | low | S | memory, bandwidth |
| [discovery_peers-079](#discovery_peers-079) | Faster light client bootstrap peer cycling | n/a | low |  | startup, sync |
| [discovery_peers-080](#discovery_peers-080) | Skip custody group computation for supernodes | implemented | low | S | cpu |
| [discovery_peers-081](#discovery_peers-081) | Count pending dials against the peer limit | implemented | low | S | cpu, bandwidth, latency |
| [discovery_peers-082](#discovery_peers-082) | Skip ENRs with no dialable address | implemented | low | S | bandwidth, cpu, latency |
| [discovery_peers-083](#discovery_peers-083) | Disable discovery loop for tiny peer targets | not | low | S | cpu, bandwidth |
| [discovery_peers-084](#discovery_peers-084) | Skip genesis block request in peer validation | n/a | low | S | latency, bandwidth |
| [discovery_peers-085](#discovery_peers-085) | Fall back instead of dialing unreachable peers | implemented | low | S | latency |
| [discovery_peers-086](#discovery_peers-086) | Skip unused metadata fetch on peer refresh | n/a | low | S | bandwidth, latency |
| [discovery_peers-087](#discovery_peers-087) | Throttle random discovery lookup rate | implemented | low | S | cpu, bandwidth, latency |
| [discovery_peers-088](#discovery_peers-088) | Dial most useful discovered peers first | not | low | S | latency |
| [discovery_peers-089](#discovery_peers-089) | Separate poll loops for channel and swarm | implemented | low | S | cpu, latency |
| [discovery_peers-090](#discovery_peers-090) **★** | Churn peers when head is starved | not | medium | M | bandwidth, sync |
| [discovery_peers-091](#discovery_peers-091) | Do not let subnet queries starve peer search | implemented | low | S | latency |
| [discovery_peers-092](#discovery_peers-092) | Lookup-table decode of ENR subnet bitfields | not | low | S | cpu |
| [discovery_peers-093](#discovery_peers-093) | Update local ENR only when fields change | implemented | low | S | bandwidth |
| [discovery_peers-094](#discovery_peers-094) | Build peer id from ENR key without allocating | not | low | S | cpu, memory |
| [discovery_peers-095](#discovery_peers-095) | Exclude NAT'd peers from discv5 routing table | implemented | low | S | latency |
| [discovery_peers-096](#discovery_peers-096) | Run identify only after successful Status handshake | not | low | M | bandwidth, cpu |
| [discovery_peers-097](#discovery_peers-097) | Enable libp2p smart_dial address ranking | implemented | low | S | latency |
| [discovery_peers-098](#discovery_peers-098) | Lock-free atomically swapped local ENR | not | low | S | latency, cpu |
| [discovery_peers-099](#discovery_peers-099) | Mark disconnected peers in discv5 routing table | implemented | low | S | bandwidth |
| [discovery_peers-100](#discovery_peers-100) | Score peers by block-serving reliability | not | low | M | sync |
| [discovery_peers-101](#discovery_peers-101) | Retry subnet discovery when query returns nothing | implemented | low | S | bandwidth, latency |
| [discovery_peers-102](#discovery_peers-102) | Shorter ping interval to detect dead peers | implemented | low | S | latency |
| [discovery_peers-103](#discovery_peers-103) | Sleep between retries of unavailable startup value | n/a | low |  | cpu |
| [discovery_peers-104](#discovery_peers-104) | Decode ENR attnets once into set for filtering | implemented | low | S | cpu |

★ actionable. Click an id for the full record.

## Ideas

<a id="discovery_peers-001"></a>
<details>
<summary><b>discovery_peers-001</b> Cache ENR-derived node id — <i>implemented · low · S · cpu</i></summary>

**Idea.** Store the node id (keccak of the public key) on the ENR object once it is computed, so discovery code does not hash the key again each time the id is needed. Check the discv5 Enr type and its node_id() accessor.

**Impact.** The node id hash is computed once for each ENR.

**Best measured result.** pr:lodestar#3419: "critical ENR node id cache performance fix"

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/registry/src/*/enr-0.14.0/src/lib.rs:244 node_id field stored on Enr
- ~/.cargo/registry/src/*/enr-0.14.0/src/lib.rs:275-276 node_id() returns the stored value
- ~/.cargo/registry/src/*/enr-0.14.0/src/lib.rs:529,595,1199 node_id is computed only on build, key change or decode
- [`beacon_node/lighthouse_network/src/peer_manager/peerdb.rs:804`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/peerdb.rs#L804) peer_id_to_node_id is used only on rare events (connect/ban), not in a hot loop

**Skeptic check.** Verified in enr 0.14.0 (the Cargo.lock version) that Enr caches node_id. The remaining PeerId to NodeId conversions in lighthouse_network happen only on connection events. The earlier verdict was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#3419](https://github.com/ChainSafe/lodestar/pull/3419), [teku#4810](https://github.com/Consensys-Incorporated/teku/pull/4810), [teku#4823](https://github.com/Consensys-Incorporated/teku/pull/4823)

</details>


<a id="discovery_peers-002"></a>
<details>
<summary><b>discovery_peers-002</b> O(1) hashmap-backed LRU for discv5 sessions — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Keep discv5 sessions in a hashmap-backed LRU with O(1) get/insert instead of a list-based LRU that scans all entries (~5k sessions) on every access.

**Impact.** O(1) session lookup.

**Best measured result.** pr:lighthouse#2577: O(N) over ~5k sessions to O(1)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/registry/src/*/discv5-0.12.0/src/handler/mod.rs:220 sessions: LruTimeCache&lt;NodeAddress, Session&gt;
- ~/.cargo/registry/src/*/discv5-0.12.0/src/lru_time_cache.rs:1-60 hashlink LinkedHashMap; insert/get_mut/to_back are O(1)
- [`beacon_node/lighthouse_network/src/config.rs:326`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L326) session_cache_capacity(5000)

**Skeptic check.** Confirmed: discv5 0.12.0 keeps sessions in a hashlink LinkedHashMap with raw_entry lookup and to_back, so each access is O(1). The earlier verdict was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

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

**Verdict history.** not (checked) → partial (refuted)

**Sources.** [teku#8387](https://github.com/Consensys-Incorporated/teku/pull/8387)

</details>


<a id="discovery_peers-004"></a>
<details>
<summary><b>discovery_peers-004</b> Array-indexed peer table with one control-loop sweep — <i>not · low · M · cpu</i></summary>

**Idea.** Hold live peers in a pre-allocated array indexed by connection id instead of a hash map, and fold the several per-heartbeat peer iterations into one sweep with per-topic subscriber indexes. This cuts hashing and repeated full scans in the peer manager loop.

**Gap in Lighthouse.** Fold the heartbeat scans (maintain_peer_count, prune, per-custody-group counts) into one pass over connected_peers; swarm connection ids make an array table impractical.

**Impact.** Saves a few microseconds per heartbeat over ~100 peers; negligible CPU.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/peerdb.rs:42`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/peerdb.rs#L42) - HashMap&lt;PeerId,PeerInfo&gt;
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:1442`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L1442) - heartbeat with several separate connected_peers() scans (1084,1515,1575)

**Sources.** [silver#384](https://github.com/gattaca-com/silver/pull/384)

</details>


<a id="discovery_peers-005"></a>
<details>
<summary><b>discovery_peers-005</b> Dial discovered peers concurrently — <i>implemented · low · S · latency, sync, startup</i></summary>

**Idea.** Dial discovered peers in parallel (one task per dial, with a generous concurrency cap) instead of one at a time, so a slow or dead peer does not block the dial loop and a fresh node reaches its target sooner.

**Impact.** The libp2p swarm runs dials concurrently, up to 16 pending outbound connections.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs:107-118`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs#L107-L118) each poll emits ToSwarm::Dial and does not wait for the dial result
- [`beacon_node/lighthouse_network/src/service/mod.rs:443`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L443) connection_limits with_max_pending_outgoing(16)

**Skeptic check.** Verified that the peer manager hands dials to the libp2p swarm. The swarm drives each dial as its own pending connection, so a slow peer does not block the loop. The earlier verdict was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#5021](https://github.com/OffchainLabs/prysm/pull/5021), [nimbus#1100](https://github.com/status-im/nimbus-eth2/pull/1100), [nimbus#2966](https://github.com/status-im/nimbus-eth2/pull/2966), [nimbus#1016](https://github.com/status-im/nimbus-eth2/pull/1016)

</details>


<a id="discovery_peers-006"></a>
<details>
<summary><b>discovery_peers-006</b> Use random discv5 lookups, not local-table sampling — <i>implemented · low · S · bandwidth, sync, cpu</i></summary>

**Idea.** Find new peers by running filtered random-target discv5 lookups (a node iterator with a predicate) instead of periodically sampling the local routing table, giving more unique dialable peers per round.

**Impact.** Peer discovery already uses filtered random-target lookups.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/discovery/mod.rs:833-844`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L833-L844) fork-digest and dialable-address predicate
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:849-850`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L849-L850) find_node_predicate(NodeId::random(), predicate, target_peers)

**Skeptic check.** Verified that peer discovery queries run discv5 find_node_predicate against a random NodeId, with a fork and dialable predicate, and do not sample the local table. This is Lighthouse PR 975.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#2211](https://github.com/status-im/nimbus-eth2/pull/2211), [prysm#6128](https://github.com/OffchainLabs/prysm/pull/6128), [lighthouse#975](https://github.com/sigp/lighthouse/pull/975)

</details>


<a id="discovery_peers-007"></a>
<details>
<summary><b>discovery_peers-007</b> Send peer status requests off the main loop — <i>implemented · low · S · latency</i></summary>

**Idea.** Send Status RPCs to peers from a separate task so the peer-management loop does not wait on the reply.

**Impact.** None left: Status is an event pushed to the swarm and the RPC reply arrives asynchronously as a later event; the peer manager never waits on it.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:137`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L137)
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:94`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L94)

**Skeptic check.** Verified PeerManagerEvent::Status is only queued; the RPC behaviour handles the outbound stream asynchronously. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#4577](https://github.com/OffchainLabs/prysm/pull/4577)

</details>


<a id="discovery_peers-008"></a>
<details>
<summary><b>discovery_peers-008</b> Do cheap checks before taking peer-collection lock — <i>partial · low · S · cpu, latency</i></summary>

**Idea.** In request and connectivity checks, run cheap sync/state checks first and take the shared peer collection lock only for requests that pass, so discarded requests never contend for the lock.

**Gap in Lighthouse.** Request-handling paths could reorder cheap sync-state checks before taking the peers read lock; contention is mostly read locks so gain is small.

**Impact.** Micro reduction in lock contention on RPC handling; not measurable on a typical node.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/globals.rs:24`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/globals.rs#L24) - peers: RwLock&lt;PeerDB&gt;
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:1084`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L1084) - read lock taken in maintenance

**Sources.** [grandine@da6e7fa4e](https://github.com/grandinetech/grandine/commit/da6e7fa4e3bb), [grandine#412](https://github.com/grandinetech/grandine/pull/412)

</details>


<a id="discovery_peers-009"></a>
<details>
<summary><b>discovery_peers-009</b> Back off when discovery finds nothing useful — <i>implemented · low · S · cpu, bandwidth, memory</i></summary>

**Idea.** When too few candidates exist (small devnet, empty routing table) or a query returns only useless results, back off instead of immediately re-querying, and bound lookup count by routing table size. This stops discovery from spinning a full core.

**Impact.** Prevents discovery from spinning on small devnets. The effect on mainnet is negligible.

**Best measured result.** pr:prysm#14446: CPU from a whole core to near idle on small devnets

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:385-396`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L385-L396) skips the recursive query when results arrive but none are useful
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:869-871`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L869-L871) an empty FindPeers result emits no DiscoveredPeers event, so there is no immediate requery
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:51`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L51) HEARTBEAT_INTERVAL 30s drives the next query
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:365-376`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L365-L376) discover_peers allows only one active FindPeers query
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:59`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L59),673-678 subnet queries are limited to MAX_DISCOVERY_RETRY=3

**Skeptic check.** Confirmed both cases. An empty result returns None, so the node waits for the 30s heartbeat. A result with no useful peers skips the recursion. Subnet retries are bounded. The earlier verdict was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#14446](https://github.com/OffchainLabs/prysm/pull/14446), [prysm#6848](https://github.com/OffchainLabs/prysm/pull/6848), [lighthouse#6207](https://github.com/sigp/lighthouse/pull/6207)

</details>


<a id="discovery_peers-010"></a>
<details>
<summary><b>discovery_peers-010</b> Run first discovery query immediately at startup — <i>implemented · low · S · startup, latency</i></summary>

**Idea.** Make the discovery service fully initialized before the first peer-manager heartbeat, so the first random query starts at once instead of being skipped until the next interval (~30s).

**Impact.** Saves at most one heartbeat interval at boot.

**Best measured result.** pr:lodestar#4980: removes a 30s wait before the first query

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:171`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L171)
- [`beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs:46`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs#L46)
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:1442`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L1442)
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:340`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L340)
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:365`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L365)

**Skeptic check.** Discovery is built with started=true after discv5 start in the constructor; the heartbeat interval's first tick fires immediately, heartbeat() calls maintain_peer_count(0), and discover_peers only skips when !started or a query is active. Earlier evidence is right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#5618](https://github.com/ChainSafe/lodestar/pull/5618), [lodestar#4980](https://github.com/ChainSafe/lodestar/pull/4980)

</details>


<a id="discovery_peers-011"></a>
<details>
<summary><b>discovery_peers-011</b> Await identify instead of polling peerstore — <i>n/a · low · S · latency</i></summary>

**Idea.** On a new connection, run identify and await its result directly instead of polling the peer store on a timer, so peer status handling starts as soon as identify completes.

**Impact.** Lighthouse is driven by identify events, no peerstore polling.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:501`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L501) - identify() is event-driven from the libp2p Identify behaviour

**Sources.** [lodestar#6400](https://github.com/ChainSafe/lodestar/pull/6400)

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

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [prysm#3390](https://github.com/OffchainLabs/prysm/pull/3390), [lighthouse#2382](https://github.com/sigp/lighthouse/pull/2382), [teku#1399](https://github.com/Consensys-Incorporated/teku/pull/1399)

</details>


<a id="discovery_peers-013"></a>
<details>
<summary><b>discovery_peers-013</b> Allow excess peers, then prune lowest-scoring — <i>implemented · medium · S · bandwidth, cpu, memory, sync</i></summary>

**Idea.** Accept peers up to target times an excess factor and, at heartbeat, disconnect the lowest-value or lowest-score peers down to target, so newly discovered useful peers always have room and the max is actually enforced.

**Impact.** Keeps room for new useful peers while holding the target.

**Best measured result.** pr:prysm#4106: peer count reduced to threshold

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:65`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L65)
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:75`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L75)
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:425`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L425)
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:1307`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L1307)
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:1355`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L1355)
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:1484`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L1484)
- [`beacon_node/lighthouse_network/src/service/mod.rs:441`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L441)

**Skeptic check.** max_peers is target*(1+0.1), with priority excess for duty peers. At each heartbeat prune_excess_peers disconnects down to target: negative score first, then peers without long-lived subnets, then the densest custody subnet. The libp2p connection_limits enforce the max. Earlier evidence is right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#2888](https://github.com/status-im/nimbus-eth2/pull/2888), [nimbus#917](https://github.com/status-im/nimbus-eth2/pull/917), [prysm#4106](https://github.com/OffchainLabs/prysm/pull/4106), [lighthouse#1383](https://github.com/sigp/lighthouse/pull/1383)

</details>


<a id="discovery_peers-014"></a>
<details>
<summary><b>discovery_peers-014</b> Bound discovered-node storage to k-buckets — <i>implemented · low · S · memory, bandwidth</i></summary>

**Idea.** Store discovered nodes only in the Kademlia k-buckets (no side lists of all seen nodes), so the memory for node records has a fixed upper bound, and keep recursive lookups selecting the closest peers.

**Impact.** Memory for node records is already bounded.

**Best measured result.** pr:teku#4185: upper bound on number of nodes stored in memory

**Evidence (Lighthouse @ 928b61e719).**

- discv5-0.12.0/src/kbucket.rs
- discv5-0.12.0/src/service.rs:188
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:75`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L75)
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:333`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L333)
- [`beacon_node/lighthouse_network/src/peer_manager/peerdb.rs:27`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/peerdb.rs#L27)

**Skeptic check.** discv5 0.12.0 keeps node records only in k-buckets plus request-scoped maps. Lighthouse's cached_enrs is an LruCache of 50, and PeerDB caps disconnected peers at MAX_DC_PEERS=500. Earlier evidence is right.

**Verdict history.** implemented (checked) → implemented (skeptic)

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
<summary><b>discovery_peers-016</b> Compute custody subnets once and store them — <i>implemented · medium · S · cpu</i></summary>

**Idea.** Compute the node's own custody subnets/columns once at startup and each peer's custody subnets once on connect or metadata update, store them in network globals and the peer DB, and read them instead of recomputing per data column query.

**Impact.** No per-query custody recomputation.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/globals.rs:69-80`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/globals.rs#L69-L80)
- [`beacon_node/lighthouse_network/src/types/globals.rs:108`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/globals.rs#L108)
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:173`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L173)
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:787-809`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L787-L809)
- [`beacon_node/lighthouse_network/src/peer_manager/peerdb.rs:297`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/peerdb.rs#L297)
- [`beacon_node/beacon_chain/src/custody_context.rs:507`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L507)

**Skeptic check.** Own sampling subnets are computed once in NetworkGlobals::new (and again only on a cgc change). Per-peer custody subnets are computed on metadata update from the precomputed subnets_by_custody_group map and stored in PeerInfo. Sync lookups (good_custody_subnet_peer, has_good_custody_range_sync_peer) only read the stored set. The beacon chain slices precomputed ordered columns. The only per-ENR recompute is the discovery subnet_predicate, which runs on discovery results and not on column queries.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#6308](https://github.com/sigp/lighthouse/pull/6308), [lighthouse#6218](https://github.com/sigp/lighthouse/pull/6218)

</details>


<a id="discovery_peers-017"></a>
<details>
<summary><b>discovery_peers-017</b> Keep per-connection peer data in memory — <i>implemented · low · S · disk, cpu</i></summary>

**Idea.** Keep peer agent version, score, addresses and metadata in an in-memory structure that is dropped on disconnect, instead of reading and writing a persistent (possibly disk-backed) peer store on the hot path.

**Impact.** None left: PeerDB is an in-memory HashMap behind an RwLock; no disk-backed peer store exists.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/peerdb.rs:42`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/peerdb.rs#L42)
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:506`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L506)

**Skeptic check.** Lighthouse never had a persistent peerstore on the hot path; peer info, score, metadata and client info are in PeerDB in memory. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#3841](https://github.com/ChainSafe/lodestar/pull/3841), [lodestar#3838](https://github.com/ChainSafe/lodestar/pull/3838)

</details>


<a id="discovery_peers-018"></a>
<details>
<summary><b>discovery_peers-018</b> Cap concurrent outbound dial attempts — <i>implemented · low · S · cpu, memory, bandwidth</i></summary>

**Idea.** Track in-flight outbound dials and cap them at a small fixed number (with a semaphore or counter), so a burst of discovery results does not open hundreds of sockets and tasks at once.

**Impact.** Bounds sockets and tasks during discovery bursts.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/mod.rs:444`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L444)
- [`beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs:107`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs#L107)
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:1041`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L1041)

**Skeptic check.** libp2p connection_limits with_max_pending_outgoing(Some(16)) caps in-flight outbound connections, and the peer manager emits only one Dial per poll. Dials above the cap are denied, not queued: they fail as DialFailure, but the cap on sockets is real. Earlier evidence is right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [silver#54](https://github.com/gattaca-com/silver/pull/54), [lighthouse#1469](https://github.com/sigp/lighthouse/pull/1469), [nimbus#1460](https://github.com/status-im/nimbus-eth2/pull/1460), [caplin#11861](https://github.com/erigontech/erigon/pull/11861)

</details>


<a id="discovery_peers-019"></a>
<details>
<summary><b>discovery_peers-019</b> Plain message passing from discovery thread — <i>n/a · low · S · cpu</i></summary>

**Idea.** Report discovered ENRs from the discovery worker to the main thread with plain message passing instead of an observable/stream wrapper, which cost about 10% CPU on an all-subnets node.

**Impact.** Nothing to gain: Rust discv5 runs in a tokio task and reports via a channel; the Lodestar overhead was JS Observable specific.

**Best measured result.** pr:lodestar#5086: ~10% CPU on mainnet all-subnets node (profiler)

**Evidence (Lighthouse @ 928b61e719).**

- discv5-0.12.0/src/handler/active_requests.rs:176 discv5 uses plain futures streams/channels, no observable layer

**Sources.** [lodestar#5086](https://github.com/ChainSafe/lodestar/pull/5086)

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
<summary><b>discovery_peers-021</b> Reject excess inbound connections at transport layer — <i>implemented · medium · S · cpu, bandwidth</i></summary>

**Idea.** Enforce the peer limit at the transport/swarm layer (connection gater, connection limits, or closing the listener) so excess inbound peers are refused before identify, gossipsub subscriptions and Status/Metadata exchange run.

**Impact.** Excess inbound peers are refused before any application protocol runs.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/mod.rs:441-459`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L441-L459)
- [`beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs:156`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs#L156)
- [`beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs:182-211`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs#L182-L211)

**Skeptic check.** connection_limits caps established incoming, outgoing and total. handle_established_inbound_connection also returns ConnectionDenied when connected_or_dialing &gt;= max_peers and the peer has no future duty, so identify, gossipsub and Status never start. Earlier evidence cited only the ban check, but the peer-count check is on the next function.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#5033](https://github.com/ChainSafe/lodestar/pull/5033), [prysm#6243](https://github.com/OffchainLabs/prysm/pull/6243), [prysm#4214](https://github.com/OffchainLabs/prysm/pull/4214), [lighthouse#2455](https://github.com/sigp/lighthouse/pull/2455)

</details>


<a id="discovery_peers-022"></a>
<details>
<summary><b>discovery_peers-022</b> Keep minimum peers per subnet — <i>implemented · medium · S · sync, latency, bandwidth, cpu</i></summary>

**Idea.** Track which attestation, sync and custody column subnets each peer serves, keep a minimum peer count per subnet (dialing past the limit or triggering discovery when below it), and prune so peers stay spread across subnets.

**Impact.** Keeps peers spread across subnets.

**Best measured result.** pr:lodestar#8057: 25-35 peers on all subnets on devnet-2

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:61`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L61)
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:996`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L996)
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:957`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L957)
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:1145-1215`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L1145-L1215)
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:432`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L432)
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:773`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L773)

**Skeptic check.** The heartbeat runs maintain_custody_peers (discovery below 2 peers per sampling subnet) and maintain_sync_committee_peers. Attestation and sync subnet discovery follows validator duties, and priority peers may dial past max via max_priority_peers. should_protect_peer keeps the last peers on sampling, sync and least-dense attestation subnets. Attestation subnets without a duty get no minimum, but the idea does not need one.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#7915](https://github.com/sigp/lighthouse/pull/7915), [lodestar#8057](https://github.com/ChainSafe/lodestar/pull/8057), [caplin#11057](https://github.com/erigontech/erigon/pull/11057)

</details>


<a id="discovery_peers-023"></a>
<details>
<summary><b>discovery_peers-023</b> Compact LRU for discv5 caches — <i>n/a · low · S · memory</i></summary>

**Idea.** Use a compact, low-overhead LRU implementation for the discv5 caches (sessions, pending requests) to cut memory per entry.

**Impact.** Discv5 caches are already hashlink maps with a 5000-session cap; at most a few hundred KB, no meaningful memory win.

**Evidence (Lighthouse @ 928b61e719).**

- discv5-0.12.0/src/lru_time_cache.rs:1 sessions in hashlink LinkedHashMap with TTL, capacity 5000
- [`beacon_node/lighthouse_network/src/config.rs:326`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L326) session_cache_capacity(5000)
- discv5-0.12.0/src/socket/filter/mod.rs:6 hashlink LruCache

**Sources.** [nimbus#6611](https://github.com/status-im/nimbus-eth2/pull/6611)

</details>


<a id="discovery_peers-024"></a>
<details>
<summary><b>discovery_peers-024</b> Allow concurrent discv5 requests to one peer — <i>implemented · low · S · latency</i></summary>

**Idea.** Let discv5 have several outstanding requests to the same peer at once instead of serialising them behind one active request.

**Impact.** None left; requests are only queued while a handshake is pending, then sent concurrently.

**Evidence (Lighthouse @ 928b61e719).**

- discv5-0.12.0/src/handler/active_requests.rs:8
- discv5-0.12.0/src/handler/active_requests.rs:25
- discv5-0.12.0/src/handler/mod.rs:492-530

**Skeptic check.** Cargo.lock pins discv5 0.12.0; ActiveRequests maps NodeAddress to Vec&lt;RequestCall&gt; and send_request only queues to pending_requests during an active challenge or session setup. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#4997](https://github.com/sigp/lighthouse/pull/4997)

</details>


<a id="discovery_peers-025"></a>
<details>
<summary><b>discovery_peers-025</b> Timeout on outbound peer connect — <i>implemented · low · S · latency</i></summary>

**Idea.** Put a timeout on every outbound connect attempt so the discovery/dial loop cannot block forever on one peer.

**Impact.** None left: TCP transport has a 10s timeout on connect+upgrade, QUIC has its own handshake timeout, and libp2p dials are non-blocking so the loop cannot stall on one peer.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/utils.rs:58-67`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/utils.rs#L58-L67)
- [`beacon_node/lighthouse_network/src/peer_manager/peerdb.rs:435-455`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/peerdb.rs#L435-L455)

**Skeptic check.** Verified .timeout(Duration::from_secs(10)) on both TCP transport variants and cleanup_dialing_peers reverting stale Dialing states after DIAL_TIMEOUT. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#1094](https://github.com/status-im/nimbus-eth2/pull/1094)

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

**Impact.** Timeouts already do not depend on the read loop.

**Best measured result.** pr:caplin#8661: found 13/76/91 peers after 12h where it previously found none

**Evidence (Lighthouse @ 928b61e719).**

- discv5-0.12.0/src/handler/mod.rs:336-385
- discv5-0.12.0/src/socket/recv.rs:121

**Skeptic check.** In discv5 0.12.0 the socket recv runs in its own task, and the handler's tokio::select polls active_requests timeouts as a separate arm. The ip:port matching for an unknown node id is a discv4 quirk; every discv5 contact carries a node id, so that part does not apply. Earlier evidence is right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#8661](https://github.com/erigontech/erigon/pull/8661)

</details>


<a id="discovery_peers-028"></a>
<details>
<summary><b>discovery_peers-028</b> Deduplicate peers in the dial queue — <i>implemented · low · S · bandwidth, cpu</i></summary>

**Idea.** Before queuing or dialing a discovered or cached peer, skip peers that are already queued or have a pending dial, so the same peer is never dialed twice in parallel.

**Impact.** None left; dial_peer gates every path (discovery, cached ENRs, trusted peers) on should_dial which rejects Dialing/Connected peers.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:364`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L364)
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:458-475`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L458-L475)
- [`beacon_node/lighthouse_network/src/peer_manager/peerdb.rs:153-160`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/peerdb.rs#L153-L160)
- [`beacon_node/lighthouse_network/src/service/mod.rs:1339-1360`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L1339-L1360)

**Skeptic check.** peers_discovered checks peers_to_dial.contains and dial_peer checks should_dial; dial_cached_enrs_in_subnet also goes through dial_peer. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#5113](https://github.com/sigp/lighthouse/pull/5113), [lodestar#4969](https://github.com/ChainSafe/lodestar/pull/4969), [lighthouse#2992](https://github.com/sigp/lighthouse/pull/2992)

</details>


<a id="discovery_peers-029"></a>
<details>
<summary><b>discovery_peers-029</b> Skip subnet query while one is unexpired — <i>partial · low · S · bandwidth, cpu</i></summary>

**Idea.** Issue a subnet peer discovery query only when no earlier query for that subnet is still unexpired, and only once per subscription period for long-lived subnets, to cut redundant discv5 queries.

**Gap in Lighthouse.** Lighthouse dedups only queued queries and skips subnets already well-peered; it does not track an unexpired earlier query per subnet nor limit long-lived subnet queries to once per subscription period. Add a per-subnet query-expiry map in Discovery::add_subnet_query.

**Impact.** Fewer redundant discv5 FINDNODE rounds on nodes with validators or persistent subnets; small saving since the peer-count filter already prunes most.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/discovery/mod.rs:683`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L683) dedup only among queued_queries
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:758-775`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L758-L775) start_subnet_query skips subnets with &gt;= TARGET_SUBNET_PEERS good peers
- [`beacon_node/network/src/subnet_service/mod.rs:388`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L388) discover_peers_request issues a request for every subscription incl. long-lived ones

**Sources.** [grandine@e5f719c8a](https://github.com/grandinetech/grandine/commit/e5f719c8a415)

</details>


<a id="discovery_peers-030"></a>
<details>
<summary><b>discovery_peers-030</b> Request metadata only after peer-limit check — <i>implemented · low · S · bandwidth</i></summary>

**Idea.** Send the Metadata request to a new peer only after deciding not to disconnect it for exceeding the peer limit, so no stream is opened for peers that are dropped at once.

**Impact.** None left: over-limit peers are denied in handle_established_*_connection before on_connection_established, which no longer emits MetaData; metadata comes from ping/pong.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs:197-210`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs#L197-L210)
- [`beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs:236-248`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs#L236-L248)
- [`beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs:255-285`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs#L255-L285)
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:719-745`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L719-L745)

**Skeptic check.** PR #6336 moved the MetaData push after the limit check; the current code went further by denying at connection establishment and requesting metadata only on ping/pong. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#6336](https://github.com/sigp/lighthouse/pull/6336)

</details>


<a id="discovery_peers-031"></a>
<details>
<summary><b>discovery_peers-031</b> Delay queues for discv5 timeouts — <i>implemented · low · S · latency, cpu</i></summary>

**Idea.** Track discv5 session and request timeouts in delay queues that fire on expiry instead of scanning all entries for expired ones.

**Impact.** None left: request timeouts fire from HashMapDelay; session expiry pops only expired entries from the LRU front.

**Evidence (Lighthouse @ 928b61e719).**

- discv5-0.12.0/src/handler/active_requests.rs:13
- discv5-0.12.0/src/handler/mod.rs:220
- discv5-0.12.0/src/lru_time_cache.rs:85-98

**Skeptic check.** Verified HashMapDelay for request nonces and LruTimeCache::remove_expired_values stops at the first unexpired entry, so no full scan. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#788](https://github.com/sigp/lighthouse/pull/788)

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


<a id="discovery_peers-033"></a>
<details>
<summary><b>discovery_peers-033</b> Fix discv5 lookup slowdown — <i>n/a · low · S · cpu, latency</i></summary>

**Idea.** Update the discv5 library to a version without the lookup slowdown (library-level lookup performance fix).

**Impact.** None; the bug was in Prysm's Go discv5 version, not in the Rust crate.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/discovery/mod.rs:225`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L225) uses sigp discv5 0.12.0 (Cargo.lock:3207), a Rust crate unrelated to Prysm's Go library slowdown

**Sources.** [prysm#6422](https://github.com/OffchainLabs/prysm/pull/6422)

</details>


<a id="discovery_peers-034"></a>
<details>
<summary><b>discovery_peers-034</b> Dial cached matching ENRs before subnet query — <i>implemented · low · S · latency, sync</i></summary>

**Idea.** Before starting a network subnet discovery query, dial ENRs already in the local cache/routing table that match the subnet predicate and are not connected or banned, so subnet peers are found without a slow query.

**Impact.** None left beyond the original PR: cached ENRs matching the subnet predicate are dialed (via should_dial) before the subnet query is sent.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/mod.rs:1224-1229`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L1224-L1229)
- [`beacon_node/lighthouse_network/src/service/mod.rs:1339-1360`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L1339-L1360)
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:161`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L161)

**Skeptic check.** dial_cached_enrs_in_subnet runs for each subnet needing peers before discovery_mut().discover_subnet_peers; it scans the LRU cache of discovered ENRs, not the discv5 kbuckets, which matches the source PR #1376. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#1376](https://github.com/sigp/lighthouse/pull/1376)

</details>


<a id="discovery_peers-035"></a>
<details>
<summary><b>discovery_peers-035</b> Do not run unused libp2p services — <i>implemented · low · S · bandwidth, cpu, startup</i></summary>

**Idea.** Do not construct or run network behaviours that the node does not use (circuit relay, hop, libp2p ping, disabled UPnP), so they cause no streams, multicast traffic or startup work.

**Impact.** None left; unused behaviours are not compiled in and UPnP is opt-in.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/mod.rs:133-161`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L133-L161) Behaviour = connection_limits, peer_manager, eth2_rpc, discovery, identify, Toggle&lt;Upnp&gt;, gossipsub
- [`beacon_node/lighthouse_network/src/service/mod.rs:462-466`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L462-L466) UPnP built only when upnp_enabled
- Cargo.toml:177 libp2p features exclude ping/relay/autonat/mdns

**Skeptic check.** Verified the behaviour struct and libp2p feature list: no relay, libp2p ping, autonat or mdns; liveness uses the eth2 RPC Ping. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@901fc65e7](https://github.com/ChainSafe/lodestar/commit/901fc65e7c87), [prysm#7345](https://github.com/OffchainLabs/prysm/pull/7345), [lighthouse#6170](https://github.com/sigp/lighthouse/pull/6170), [prysm#6124](https://github.com/OffchainLabs/prysm/pull/6124)

</details>


<a id="discovery_peers-036"></a>
<details>
<summary><b>discovery_peers-036</b> Drop libp2p connection manager when client prunes itself — <i>n/a · low · S · cpu</i></summary>

**Idea.** Do not run the generic libp2p connection manager next to the client's own peer pruning, so peers are not pruned twice by two policies.

**Impact.** No second pruning policy exists, so no double pruning.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/mod.rs:441`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L441) only libp2p connection_limits (hard caps), no connection manager with its own pruning
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs) is the sole pruning policy

**Sources.** [prysm#16221](https://github.com/OffchainLabs/prysm/pull/16221)

</details>


<a id="discovery_peers-037"></a>
<details>
<summary><b>discovery_peers-037</b> Early filter and rate limit discv5 packets — <i>implemented · medium · S · cpu, bandwidth</i></summary>

**Idea.** Rate-limit and drop unsolicited or junk UDP packets at the start of the discv5 packet handler, before decryption and session work.

**Impact.** Junk/unsolicited UDP packets dropped before decode and session work.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/config.rs:305-312`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L305-L312) discv5 RateLimiter total/ip/node
- [`beacon_node/lighthouse_network/src/config.rs:324-342`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L324-L342) enable_packet_filter, filter_max_bans_per_ip, filter_max_nodes_per_ip
- [`beacon_node/src/config.rs:1463-1466`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/config.rs#L1463-L1466) disabled only by explicit --disable-packet-filter
- ~/.cargo/registry/src/*/discv5-0.12.0/src/socket/recv.rs:196-203 filter.initial_pass before Packet::decode

**Skeptic check.** Confirmed the filter is on by default and runs in the recv task before decode/decrypt, with expected responses permitted. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#1274](https://github.com/sigp/lighthouse/pull/1274), [lighthouse#2435](https://github.com/sigp/lighthouse/pull/2435)

</details>


<a id="discovery_peers-038"></a>
<details>
<summary><b>discovery_peers-038</b> Run discovery in a separate worker thread — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Run discv5 (UDP handling, ENR signature checks, routing table) on its own thread or runtime so it does not compete with block processing on the main event loop.

**Impact.** None left: discv5 service, handler and socket tasks run as separate tokio tasks on the multi-thread runtime, apart from the libp2p swarm loop and the beacon_processor workers.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/discovery/mod.rs:254`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L254) discv5.start()
- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/discv5-0.12.0/src/service.rs:303 Service spawned on executor
- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/discv5-0.12.0/src/handler/mod.rs:307 Handler (session crypto, ENR checks) spawned as own task
- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/discv5-0.12.0/src/socket/recv.rs:113 and send.rs:54 UDP recv/send tasks

**Skeptic check.** Verified discv5 0.12.0 spawns Service, Handler, RecvHandler and SendHandler as independent tasks. The Lodestar issue was a single JS thread; in Lighthouse's multi-thread runtime these tasks already run in parallel, so the earlier verdict is right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#4988](https://github.com/ChainSafe/lodestar/pull/4988)

</details>


<a id="discovery_peers-039"></a>
<details>
<summary><b>discovery_peers-039</b> Raise default target peer count — <i>implemented · medium · S · bandwidth, memory, sync</i></summary>

**Idea.** Raise the default target peer count so the node covers all custody columns and subnets with a more diverse peer set; gossipsub mesh bounds keep the bandwidth cost small (+2.6% in, +5.8% out for 2x peers).

**Impact.** Default already 200 (the PR #7877 change).

**Best measured result.** pr:lighthouse#7877: peers 91-&gt;183 cost inbound +2.6%, outbound +5.8%, memory +~8%

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/config.rs:11`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/config.rs#L11) DEFAULT_TARGET_PEERS = 200
- [`beacon_node/lighthouse_network/src/config.rs:355`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L355) target_peers: DEFAULT_TARGET_PEERS
- [`beacon_node/src/config.rs:1219-1222`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/config.rs#L1219-L1222) only overridden by explicit --target-peers

**Skeptic check.** The CLI has no default_value for target-peers, so the 200 default stands. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#7877](https://github.com/sigp/lighthouse/pull/7877), [caplin#11820](https://github.com/erigontech/erigon/pull/11820), [nimbus#1130](https://github.com/status-im/nimbus-eth2/pull/1130)

</details>


<a id="discovery_peers-040"></a>
<details>
<summary><b>discovery_peers-040</b> Do not write ENR to disk on every change — <i>partial · low · S · disk</i></summary>

**Idea.** Keep the current ENR in memory and expose it via the API instead of synchronously writing it to disk each time it changes.

**Gap in Lighthouse.** ENR is kept in memory, but each change still triggers a synchronous disk write on the network task.

**Impact.** Negligible: a few tiny writes per hour at most.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/discovery/enr.rs:339`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/enr.rs#L339) save_enr_to_disk does sync File::create+write_all
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:439`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L439),475,487,497,1105 called only when ENR changes
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:1103`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L1103) network_globals.local_enr kept in memory

**Sources.** [lodestar#4989](https://github.com/ChainSafe/lodestar/pull/4989)

</details>


<a id="discovery_peers-041"></a>
<details>
<summary><b>discovery_peers-041</b> No mainnet bootnodes on custom networks — <i>implemented · low · S · bandwidth</i></summary>

**Idea.** Use only the configured network's bootnodes on custom chain configs, without adding mainnet bootnodes that cause useless dials.

**Impact.** Custom networks only dial their own bootnodes; there is no mainnet fallback.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/src/config.rs:519-527`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/config.rs#L519-L527) only eth2_network_config.boot_enr of the selected network is appended
- [`common/eth2_network_config/src/lib.rs:354`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2_network_config/src/lib.rs#L354) boot_enr loaded from the testnet dir (optional)
- [`beacon_node/src/config.rs:1241-1256`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/config.rs#L1241-L1256) --boot-nodes

**Skeptic check.** Confirmed that bootnodes come only from the selected network config (or the testnet dir's boot_enr.yaml) plus --boot-nodes. There is no hardcoded mainnet list mixed in, so the earlier verdict is right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#15460](https://github.com/OffchainLabs/prysm/pull/15460)

</details>


<a id="discovery_peers-042"></a>
<details>
<summary><b>discovery_peers-042</b> Avoid redundant Status re-requests — <i>implemented · low · S · bandwidth, cpu</i></summary>

**Idea.** Re-request peer Status only on a slow period (every few slots or epochs), refresh a peer's last-status timestamp on every update, and stop periodic re-requests once synced, instead of re-asking every peer each slot or epoch.

**Impact.** About one Status per peer per 5 min; the remaining difference (continuing after synced) is negligible and needed to detect peers moving ahead.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/config.rs:2`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/config.rs#L2) DEFAULT_STATUS_INTERVAL = 300
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:403-406`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L403-L406) peer_statusd resets the per-peer status timer
- [`beacon_node/lighthouse_network/src/service/mod.rs:1665`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L1665) and :1836 peer_statusd on inbound Status request and on Status response
- [`beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs:83-97`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs#L83-L97) periodic Status not sent while SyncingFinalized/SyncingHead

**Skeptic check.** Slow period and timer refresh on every Status (both directions) are present. Lighthouse keeps re-statusing once synced instead of stopping, which the earlier check already noted as a negligible difference.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine@993779a34](https://github.com/grandinetech/grandine/commit/993779a34eda), [prysm#4152](https://github.com/OffchainLabs/prysm/pull/4152), [lodestar#1328](https://github.com/ChainSafe/lodestar/pull/1328)

</details>


<a id="discovery_peers-043"></a>
<details>
<summary><b>discovery_peers-043</b> Subnet discovery as soon as duties are known — <i>implemented · low · S · latency</i></summary>

**Idea.** Start subnet peer discovery queries as soon as attestation duties are known, instead of a few slots before the duty, so grouped queries have time to finish.

**Impact.** Discovery starts as soon as the VC sends a subscription (normally an epoch ahead).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/subnet_service/mod.rs:219`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L219) validator_subscriptions collects subnets_to_discover at subscription time
- [`beacon_node/network/src/subnet_service/mod.rs:345`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L345) discover_peers_request called immediately
- [`beacon_node/network/src/subnet_service/mod.rs:405`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L405) only requires slot &gt;= current+MIN_PEER_DISCOVERY_SLOT_LOOK_AHEAD

**Skeptic check.** This is Lighthouse's own PR #1415. The current code issues DiscoverPeers right away for every attestation and sync subscription that is at least 2 slots out, which matches the idea.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#1415](https://github.com/sigp/lighthouse/pull/1415)

</details>


<a id="discovery_peers-044"></a>
<details>
<summary><b>discovery_peers-044</b> Skip peer-status scan when already synced — <i>implemented · low · S · cpu</i></summary>

**Idea.** Skip iterating over all peer statuses for sync decisions when the node is already synced to the current epoch.

**Impact.** Micro CPU; peer iteration is skipped when the node is near head.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/manager.rs:665-669`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L665-L669) head-vs-current-slot check returns Synced before advanced_peers()/synced_peers() iteration

**Skeptic check.** Verified update_sync_state short-circuits to Synced on the head/slot tolerance check before it scans the peer DB. The peers read lock is still taken, but no iteration happens, which matches the Prysm change.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#4504](https://github.com/OffchainLabs/prysm/pull/4504)

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

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [lighthouse#10259](https://github.com/sigp/lighthouse/pull/10259), [lodestar#3565](https://github.com/ChainSafe/lodestar/pull/3565), [prysm#3522](https://github.com/OffchainLabs/prysm/pull/3522)

</details>


<a id="discovery_peers-046"></a>
<details>
<summary><b>discovery_peers-046</b> Optimise discovery ExpirationSet structure — <i>n/a · low · cpu</i></summary>

**Idea.** Use a cheaper data structure for discovery expiring-entry bookkeeping (the ExpirationSet) to cut CPU spent in peer discovery bookkeeping.

**Impact.** Teku-specific Java structure; discv5 crate has its own bookkeeping (delay_map).

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.toml:140 discv5 0.12.0 (Rust crate, no ExpirationSet)

**Sources.** [teku#6374](https://github.com/Consensys-Incorporated/teku/pull/6374)

</details>


<a id="discovery_peers-047"></a>
<details>
<summary><b>discovery_peers-047</b> Fast secp256k1 for discv5 signatures — <i>partial · low · M · cpu</i></summary>

**Idea.** Use the fastest available secp256k1 implementation for ENR signature verification and discv5 handshake ECDH/signing, which dominate discovery CPU at high peer counts.

**Gap in Lighthouse.** ENR signature verification and the discv5 handshake ECDH/sign (discv5 handler session code via enr CombinedKey/k256) use pure-Rust k256, not the faster libsecp256k1 C bindings (enr's rust-secp256k1 feature). Switching needs a feature change in enr/discv5 plus key-type plumbing.

**Impact.** k256 is an optimized implementation, so this is not a slow path like the one Teku fixed; libsecp256k1 might be about 1.5-2x faster per verify, but discovery is a small share of total CPU.

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.lock:3594-3605 enr 0.14.0 depends on k256 0.14.0 only
- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/discv5-0.12.0/Cargo.toml:89-94 enr features [k256, ed25519]
- Cargo.toml:145 enr = 0.14.0 (no rust-secp256k1 feature)

**Skeptic check.** The earlier verdict said implemented, but its own gap says Lighthouse does not use the fastest secp256k1 backend. k256 is reasonably fast, so I rate this partial rather than not.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [teku#11541](https://github.com/Consensys-Incorporated/teku/pull/11541)

</details>


<a id="discovery_peers-048"></a>
<details>
<summary><b>discovery_peers-048</b> Retry peer search quickly after startup — <i>implemented · low · S · startup, sync</i></summary>

**Idea.** Right after startup, retry peer search with short (about 1s) delays and drop duplicate immediate attempts, so first peers connect in seconds instead of half a minute.

**Impact.** Startup-only; queries chain back-to-back already, so first peers do not wait for the 30s heartbeat in the normal case.

**Best measured result.** pr:teku#6139: first peers at ~14s instead of ~43s after startup

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:171`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L171) heartbeat interval, first tick immediate
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:1442-1444`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L1442-L1444) heartbeat calls maintain_peer_count
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:389-399`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L389-L399) peers_discovered re-queues a query at once unless results had zero dialable peers
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:365-375`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L365-L375) discover_peers drops duplicates via find_peer_active
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:340`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L340) started at construction

**Skeptic check.** Lighthouse starts discovery at the first (immediate) heartbeat and chains queries immediately while below target, with duplicate suppression. Only a result set with no dialable peers falls back to the 30s heartbeat, as noted earlier.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#6139](https://github.com/Consensys-Incorporated/teku/pull/6139)

</details>


<a id="discovery_peers-049"></a>
<details>
<summary><b>discovery_peers-049</b> Cheaper best-finalized-peer selection — <i>partial · low · S · cpu</i></summary>

**Idea.** Select the best finalized peers with fewer per-peer status lookups, for example one pass and sort by finalized epoch.

**Gap in Lighthouse.** Sorting is by score, one pass over peer DB with no per-peer extra lookup; sync target selection uses range sync chains instead of finalized-peer sort. Nothing material to change.

**Impact.** Peer set is ~100; cost negligible.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/peerdb.rs:403`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/peerdb.rs#L403) best_peers_by_status sorts all peers
- peerdb.rs:420 best_by_status single-pass max_by

**Sources.** [prysm#4505](https://github.com/OffchainLabs/prysm/pull/4505)

</details>


<a id="discovery_peers-050"></a>
<details>
<summary><b>discovery_peers-050</b> Filter ENRs inside the discovery service — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Filter discovered ENRs for relevance (fork digest, subnet fields) inside the discovery service/thread and stop emitting an event per crawled ENR, so irrelevant records never reach the main network loop.

**Impact.** Irrelevant ENRs filtered inside the discv5 query; no per-ENR events reach the network loop.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/discovery/mod.rs:830-853`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L830-L853) fork-digest + dialable predicate passed into discv5 find_node_predicate
- [`beacon_node/lighthouse_network/src/config.rs:332`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L332) disable_report_discovered_peers
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:1078-1091`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L1078-L1091) discv5::Event::Discovered ignored

**Skeptic check.** Confirmed the predicate runs inside the discv5 query and Discovered events are disabled and ignored. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#5104](https://github.com/ChainSafe/lodestar/pull/5104), [lighthouse#1693](https://github.com/sigp/lighthouse/pull/1693), [nimbus#1162](https://github.com/status-im/nimbus-eth2/pull/1162), [teku#1809](https://github.com/Consensys-Incorporated/teku/pull/1809)

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


<a id="discovery_peers-052"></a>
<details>
<summary><b>discovery_peers-052</b> Fix discv5 thread deadlock — <i>implemented · low · S · cpu</i></summary>

**Idea.** Update to a discv5 version without the thread deadlock that burned CPU with no peers and stalled the client.

**Impact.** The 2020 deadlock fix has long been in the dependency.

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.toml:140 discv5 0.12.0
- Cargo.lock:3207-3208 discv5 0.12.0

**Skeptic check.** This is a dependency bump from 2020 (lighthouse#1349). The current discv5 0.12.0 is far past that fix, so the earlier verdict is right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#1349](https://github.com/sigp/lighthouse/pull/1349)

</details>


<a id="discovery_peers-053"></a>
<details>
<summary><b>discovery_peers-053</b> No thread or task leaks in discovery — <i>n/a · low · memory, cpu</i></summary>

**Idea.** Make sure discovery sessions and queries release their worker threads and tasks, so long uptime does not accumulate leaked threads.

**Impact.** JVM thread leaks; discv5 runs on a single tokio task with no per-session threads.

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.toml:140 discv5 0.12.0 tokio tasks, Rust

**Sources.** [teku#1522](https://github.com/Consensys-Incorporated/teku/pull/1522)

</details>


<a id="discovery_peers-054"></a>
<details>
<summary><b>discovery_peers-054</b> Gate subnet discovery by fork activation — <i>implemented · low · S · cpu, bandwidth</i></summary>

**Idea.** Issue discovery queries for a subnet type (sync committee, data column) only once the fork that introduces it is scheduled or active, so no endless failing queries run before it.

**Impact.** No endless failing data column or sync committee queries run before their fork.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:1463-1472`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L1463-L1472) maintain_custody_peers only when a DataColumnSidecar topic is subscribed
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:174`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L174) and :787 is_peer_das_scheduled gating
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:957`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L957) maintain_sync_committee_peers iterates only sync_committee_subnets populated by subscriptions (:411)
- [`beacon_node/network/src/subnet_service/mod.rs:276`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L276) sync subnet discovery only from VC sync-committee subscriptions

**Skeptic check.** Verified that the custody-peer discovery heartbeat is gated on data column topic subscription, which happens just before the fork, and that sync committee queries come only from validator subscriptions. This is Lighthouse's own PR #8109.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#8109](https://github.com/sigp/lighthouse/pull/8109), [nimbus@22346f3e3](https://github.com/status-im/nimbus-eth2/commit/22346f3e32d3), [caplin#16232](https://github.com/erigontech/erigon/pull/16232)

</details>


<a id="discovery_peers-055"></a>
<details>
<summary><b>discovery_peers-055</b> Search several subnets in one discovery query — <i>implemented · low · S · bandwidth, cpu, latency</i></summary>

**Idea.** Combine peer searches for several wanted subnets into one discovery query or one filtered iterator that accepts peers matching any wanted subnet, instead of one query per subnet.

**Impact.** One discv5 query per group of up to 3 subnets, accepting peers on any of them.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/discovery/mod.rs:715-746`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L715-L746) process_queue groups up to MAX_SUBNETS_IN_QUERY (3) queued subnets
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:757-813`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L757-L813) start_subnet_query builds one predicate over filtered_subnets
- [`beacon_node/lighthouse_network/src/discovery/subnet_predicate.rs:29-43`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/subnet_predicate.rs#L29-L43) subnets.iter().any(...) for attestation, sync and data-column subnets

**Skeptic check.** Verified grouping and any-subnet predicate, including data column subnets. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#1364](https://github.com/sigp/lighthouse/pull/1364), [prysm#8048](https://github.com/OffchainLabs/prysm/pull/8048), [prysm#15471](https://github.com/OffchainLabs/prysm/pull/15471)

</details>


<a id="discovery_peers-056"></a>
<details>
<summary><b>discovery_peers-056</b> Count peers per subnet in one pass — <i>partial · low · S · cpu</i></summary>

**Idea.** In periodic peer management, take one connected-peer snapshot and count peers for all needed subnets in a single pass, instead of looking up peers once per subnet.

**Gap in Lighthouse.** Replace per-subnet good_peers_on_subnet scans in maintain_sync_committee_peers / maintain_custody_peers with a single pass that builds a subnet-&gt;count map; peerdb.rs good_peers_on_subnet and has_good_peers_in_custody_subnet.

**Impact.** Peer set ~100 and runs every heartbeat (30s) with at most 4 sync + ~8-128 custody subnets, so saving is microseconds; marginal.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:955-985`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L955-L985) maintain_sync_committee_peers calls good_peers_on_subnet per subnet under a read lock each
- peerdb.rs:281 good_peers_on_subnet scans all peers per call
- service/mod.rs:1213 per-subnet scan again in discover

**Sources.** [lodestar#1898](https://github.com/ChainSafe/lodestar/pull/1898), [lodestar@aaeda6e79](https://github.com/ChainSafe/lodestar/commit/aaeda6e79f8a)

</details>


<a id="discovery_peers-057"></a>
<details>
<summary><b>discovery_peers-057</b> Reject banned peers before handshake — <i>implemented · low · S · cpu, bandwidth</i></summary>

**Idea.** On every inbound connection, check the ban list and close banned peers before the Status handshake, so a banned peer cannot trigger a handshake on each reconnect.

**Impact.** Banned peers are refused at the swarm level before any Status handshake.

**Best measured result.** pr:caplin#23606: 101 handshake attempts to one peer in 2 min; 13,827 failures across 1,638 peers in 90 min

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs:156-179`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs#L156-L179) handle_pending_inbound_connection denies banned IPs
- [`beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs:181-195`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs#L181-L195) handle_established_inbound_connection denies banned peer ids
- [`beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs:212-221`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs#L212-L221) outbound rejects banned peers
- [`beacon_node/lighthouse_network/src/service/mod.rs:139-143`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L139-L143) connection_limits and peer_manager run first so no RPC/Status starts

**Skeptic check.** Rejection happens in the NetworkBehaviour connection hooks, before handlers exist, so no Status is exchanged. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#23606](https://github.com/erigontech/erigon/pull/23606)

</details>


<a id="discovery_peers-058"></a>
<details>
<summary><b>discovery_peers-058</b> Ignore connect events for closed connections — <i>n/a · low · cpu</i></summary>

**Idea.** Ignore peer-connect events whose connection is already closed, and handle disconnects before new connects, so peer state does not leak when a disconnect event never arrives.

**Impact.** rust-libp2p swarm delivers ordered connection events and tracks connection ids; closed connections are not reported as new connects.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs:124-138`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs#L124-L138) libp2p FromSwarm ConnectionEstablished/ConnectionClosed with remaining_established

**Sources.** [lodestar#5023](https://github.com/ChainSafe/lodestar/pull/5023)

</details>


<a id="discovery_peers-059"></a>
<details>
<summary><b>discovery_peers-059</b> In-process p2p calls instead of local RPC — <i>n/a · low · S · latency, cpu</i></summary>

**Idea.** Call the p2p/networking component in-process rather than over a local network RPC, removing serialisation per call.

**Impact.** Nothing to gain: no inter-process RPC exists in Lighthouse.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/mod.rs:141`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L141) libp2p Swarm runs inside the same process; network service talks to others over tokio channels, no RPC

**Sources.** [caplin#8006](https://github.com/erigontech/erigon/pull/8006)

</details>


<a id="discovery_peers-060"></a>
<details>
<summary><b>discovery_peers-060</b> Do not serialize ENR in peer filter — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** In the discovered-peer filter hot path, do not serialize each candidate ENR (RLP plus base64); do it only when logging or reporting an error.

**Impact.** No RLP/base64 encoding per candidate in the discovery filter.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/discovery/subnet_predicate.rs:17-52`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/subnet_predicate.rs#L17-L52) reads ENR fields only; trace! fields evaluated only when trace enabled
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:833-840`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L833-L840) eth2_fork_predicate compares fork_digest and dialable addrs, no encoding
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:242`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L242) to_string only for bootnodes at startup

**Skeptic check.** Confirmed that the fork and subnet predicates decode only the fields they need and never serialize the ENR. The DataColumn predicate does compute compute_subnets_for_node per candidate, but that is a separate cost, not ENR serialization.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#16028](https://github.com/OffchainLabs/prysm/pull/16028)

</details>


<a id="discovery_peers-061"></a>
<details>
<summary><b>discovery_peers-061</b> Cap pending inbound connections and backlog — <i>partial · low · S · cpu, memory</i></summary>

**Idea.** Cap the TCP listen backlog and the number of pending (not yet upgraded) inbound connections to a small multiple of max peers, so floods do not consume handshake CPU and memory.

**Gap in Lighthouse.** No global cap on pending inbound connections and no explicit TCP backlog; only a per-source cap of 2 (a flood from many IPs is not bounded). In service/mod.rs ConnectionLimits add .with_max_pending_incoming(Some(k*max_peers)) and set libp2p::tcp::Config::listen_backlog in service/utils.rs.

**Impact.** Bounds handshake CPU and memory under a many-source inbound flood; no change on normal nodes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/mod.rs:441-459`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L441-L459) ConnectionLimits: max_pending_incoming_per_source(2), max_pending_outgoing(16), established limits from target_peers
- [`beacon_node/lighthouse_network/src/service/utils.rs:52`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/utils.rs#L52) tcp::Config::default().nodelay(true) keeps libp2p default listen backlog

**Sources.** [lodestar#5860](https://github.com/ChainSafe/lodestar/pull/5860)

</details>


<a id="discovery_peers-062"></a>
<details>
<summary><b>discovery_peers-062</b> Scale per-subnet peer target to total peers — <i>partial · low · S · bandwidth, cpu</i></summary>

**Idea.** Set the target peers per subnet in proportion to the total target peer count, so nodes with many validator subnets do not run discovery queries forever trying to reach unreachable per-subnet targets.

**Gap in Lighthouse.** PR 5177 landed as a fixed constant of 3 (tuned for the 100-peer default), not proportional. A user who lowers --target-peers with many subnets still chases 3 per subnet. Replace TARGET_SUBNET_PEERS by a value derived from config.target_peers in discovery/mod.rs and service/mod.rs subnet checks.

**Impact.** Avoids endless subnet discovery queries only for nodes with small target-peers and many subnets; default config already fine.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/mod.rs:63`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L63) TARGET_SUBNET_PEERS = 3 const
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:773-783`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L773-L783) and service/mod.rs:1215 use the constant
- [`beacon_node/lighthouse_network/src/config.rs:355`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L355) target_peers default DEFAULT_TARGET_PEERS

**Sources.** [lighthouse#5177](https://github.com/sigp/lighthouse/pull/5177)

</details>


<a id="discovery_peers-063"></a>
<details>
<summary><b>discovery_peers-063</b> Skip subnet filtering of peers during sync — <i>implemented · low · S · sync, bandwidth</i></summary>

**Idea.** While range syncing, do not filter discovered peers by attestation subnets, since subnets do not matter for sync and more discovered peers become usable.

**Impact.** General peer discovery never filters by attestation subnet, in sync or not, so all fork-matching peers are usable for range sync.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/discovery/mod.rs:385-394`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L385-L394) discover_peers starts FindPeers with \|_\| true
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:827-842`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L827-L842) start_query only adds the fork-digest and dialable-address predicate
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:1041-1071`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L1041-L1071) maintain_peer_count requests generic peers

**Skeptic check.** Verified that FindPeers uses an always-true extra predicate; subnet predicates apply only to SubnetQuery. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#2837](https://github.com/status-im/nimbus-eth2/pull/2837)

</details>


<a id="discovery_peers-064"></a>
<details>
<summary><b>discovery_peers-064</b> Do not block startup on bootstrap connectivity — <i>partial · low · S · startup, latency</i></summary>

**Idea.** Run the bootstrap connectivity check as a background task instead of a fixed blocking wait, so the rest of startup continues at once.

**Gap in Lighthouse.** Only multiaddr bootnodes (rare; default networks use ENR bootnodes) block startup until every request_enr resolves or times out; there is no fixed connectivity wait. Move the multiaddr request_enr loop in Discovery::new into a spawned task or into the poll loop so startup continues.

**Impact.** Saves seconds of startup only for users with multiaddr bootnodes; no steady-state gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/discovery/mod.rs:261-320`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L261-L320) Discovery::new awaits ENR requests for multiaddr bootnodes (while loop on FuturesUnordered) before returning
- [`beacon_node/lighthouse_network/src/service/mod.rs:400-410`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L400-L410) discovery built and awaited during network start

**Sources.** [nimbus@880b981a0](https://github.com/status-im/nimbus-eth2/commit/880b981a0ad8)

</details>


<a id="discovery_peers-065"></a>
<details>
<summary><b>discovery_peers-065</b> Omit UDP port to avoid serving FINDNODE — <i>n/a · low · S · memory</i></summary>

**Idea.** As a workaround for discovery memory growth, omit the UDP port from the local ENR so the node is not asked to serve FINDNODE requests.

**Impact.** The workaround targets a Lodestar-specific JS discv5 memory leak; omitting UDP would hurt Lighthouse discoverability.

**Best measured result.** pr:lodestar#4591: external memory stable for 3 days on test nodes

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/discovery/enr.rs:204-210`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/enr.rs#L204-L210) UDP port is put in ENR from listen config
- Cargo.lock discv5 is the Rust crate, not the discv5 JS implementation with the leak

**Sources.** [lodestar#4579](https://github.com/ChainSafe/lodestar/pull/4579), [lodestar#4591](https://github.com/ChainSafe/lodestar/pull/4591)

</details>


<a id="discovery_peers-066"></a>
<details>
<summary><b>discovery_peers-066</b> Drive discovery on demand from peer manager — <i>implemented · medium · S · cpu, bandwidth</i></summary>

**Idea.** Run discv5 lookups when the peer manager needs peers, filtering ENRs by fork digest and subnet needs before dialing and caching good results, instead of continuous background lookups.

**Impact.** Discovery is demand-driven from the peer manager, filtered by fork digest and subnet before dialing, with ENR cache.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:1041-1071`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L1041-L1071) maintain_peer_count emits DiscoverPeers only when below target/outbound minimum
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:385-394`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L385-L394) single FindPeers at a time (find_peer_active)
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:760-806`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L760-L806) subnet queries skipped when enough good peers on subnet
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:827-842`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L827-L842) fork digest and dialable predicate inside find_node_predicate
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:353-360`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L353-L360) cached_enrs

**Skeptic check.** Read the code: lookups are triggered by peer manager need, never continuously, and ENRs are filtered before dial. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#3403](https://github.com/ChainSafe/lodestar/pull/3403), [lodestar#3104](https://github.com/ChainSafe/lodestar/pull/3104)

</details>


<a id="discovery_peers-067"></a>
<details>
<summary><b>discovery_peers-067</b> Stop discovery when peer target is reached — <i>implemented · low · S · cpu, bandwidth</i></summary>

**Idea.** Start discovery queries only when there is a free peer slot and the connected (and outbound) peer count is below target, and ease lookup frequency as the target is approached, instead of querying at a fixed fast rate.

**Impact.** Discovery is idle at the peer target; query size shrinks to wanted_peers as the target is approached.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:1041-1070`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L1041-L1070) maintain_peer_count: wanted_peers=0 once connected_or_dialing &gt;= target and outbound &gt;= min
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:365-374`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L365-L374) discover_peers returns while find_peer_active
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:389-398`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L389-L398) peers_discovered stops recursion on no useful ENRs
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:51`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L51) HEARTBEAT_INTERVAL=30

**Skeptic check.** Verified that queries start only below target or below the outbound minimum, one FindPeers at a time, sized to wanted_peers (capped 16). Earlier evidence correct; wanted_peers shrinking near target gives the graduated easing.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [ethlambda#605](https://github.com/lambdaclass/ethlambda/pull/605), [prysm#6346](https://github.com/OffchainLabs/prysm/pull/6346), [lighthouse#2993](https://github.com/sigp/lighthouse/pull/2993), [nimbus#2243](https://github.com/status-im/nimbus-eth2/pull/2243)

</details>


<a id="discovery_peers-068"></a>
<details>
<summary><b>discovery_peers-068</b> Pass ENRs between threads without re-encoding — <i>n/a · low · cpu</i></summary>

**Idea.** Pass ENRs from the discovery worker to the main thread as decoded objects instead of re-encoding them, so the main thread does not verify the signature again per ENR.

**Impact.** n/a: discv5 runs as a tokio task in the same process, ENRs are passed as decoded objects, no worker re-encoding.

**Sources.** [lodestar#5073](https://github.com/ChainSafe/lodestar/pull/5073)

</details>


<a id="discovery_peers-069"></a>
<details>
<summary><b>discovery_peers-069</b> Cooldown before reconnecting disconnected peers — <i>partial · low · S · bandwidth, cpu</i></summary>

**Idea.** After a disconnect (longer for serious goodbye reasons), keep the peer in a time-limited ban/cooldown list checked at the swarm layer and by discovery before dialing, so peers are not redialed or accepted in loops while at the limit.

**Gap in Lighthouse.** temporary_banned_peers is write-only apart from expiry: no swarm-level enforcement remains (rust-libp2p dropped Swarm::ban_peer_id, and no allow_block_list behaviour is used). handle_established_inbound_connection accepts a recently disconnected peer while connected_or_dialing &lt; max_peers (target..target*1.1 slack), and it is then pruned again at the next heartbeat; should_dial/dial_cached_enrs_in_subnet also do not consult it. The cooldown only blocks discv5 rediscovery. Fix: check temporary_banned_peers in handle_established_inbound_connection/handle_established_outbound_connection and in dial_peer; optionally scale timeout by goodbye reason.

**Impact.** Stops accept-then-prune reconnect churn near the peer limit on crowded networks (the original goal of lighthouse#3757).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:301-308`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L301-L308) TemporaryBan inserts into temporary_banned_peers and emits PeerManagerEvent::Banned
- [`beacon_node/lighthouse_network/src/service/mod.rs:1960-1962`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L1960-L1962) Banned only calls discovery().ban_peer (discv5 ban_node), no swarm-level block
- [`beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs:156-212`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs#L156-L212) handle_pending/established_inbound_connection check ban_status/is_ip_banned (score/IP) only, not temporary_banned_peers
- [`beacon_node/lighthouse_network/src/peer_manager/peerdb.rs:153-160`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/peerdb.rs#L153-L160) should_dial ignores temporary bans
- [`beacon_node/lighthouse_network/src/peer_manager/peerdb.rs:176-183`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/peerdb.rs#L176-L183) ban_status is score/IP based

**Skeptic check.** lighthouse#3757 originally banned at the swarm layer; today PeerManagerEvent::Banned only reaches discv5, and no connection handler reads temporary_banned_peers. Earlier evidence cited the cache and event but missed that the swarm-layer check is gone.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [prysm#7726](https://github.com/OffchainLabs/prysm/pull/7726), [lodestar#8067](https://github.com/ChainSafe/lodestar/pull/8067), [teku#1312](https://github.com/Consensys-Incorporated/teku/pull/1312), [lighthouse#3757](https://github.com/sigp/lighthouse/pull/3757), [lodestar#8044](https://github.com/ChainSafe/lodestar/pull/8044), [prysm#3373](https://github.com/OffchainLabs/prysm/pull/3373)

</details>


<a id="discovery_peers-070"></a>
<details>
<summary><b>discovery_peers-070</b> Persist known peers across restarts — <i>implemented · low · S · startup, sync</i></summary>

**Idea.** Save known peer ENRs (or the peer store) on shutdown and load them into the routing table on startup, so discovery does not restart from the boot nodes.

**Impact.** Routing table is restored from the store after restart instead of only boot nodes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/service.rs:326-335`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L326-L335) load_dht into routing table at startup
- [`beacon_node/network/src/service.rs:1683-1698`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L1683-L1698) persist_dht in Drop
- [`beacon_node/network/src/persisted_dht.rs:23`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/persisted_dht.rs#L23) ENRs stored in the store

**Skeptic check.** Verified load on start and save on shutdown. Saving happens only on Drop, so a crash loses the update, but the idea as described (save on shutdown) is fully done.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#659](https://github.com/sigp/lighthouse/pull/659), [lodestar@04b785456](https://github.com/ChainSafe/lodestar/commit/04b785456392), [lodestar#1312](https://github.com/ChainSafe/lodestar/pull/1312)

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
<summary><b>discovery_peers-073</b> Protect useful peers from random pruning — <i>implemented · low · S · latency, bandwidth</i></summary>

**Idea.** Tag in-use or useful peers as protected in the connection manager so that over-limit pruning does not drop them at random and cause churn and redials.

**Impact.** Pruning is deterministic (score and subnet-usefulness ordered); no random connection-manager pruning exists to protect against.

**Best measured result.** pr:lodestar#4997: peer connection length metric improved

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:1136-1200`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L1136-L1200) should_protect_peer protects outbound, sampling-column, sync-committee and scarce-attestation-subnet peers
- [`beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs:197-210`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs#L197-L210) libp2p connection limits reject new inbound only, nothing prunes existing connections at random
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:1060`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L1060) build_peer_subnet_info excludes trusted peers from pruning

**Skeptic check.** Lodestar's issue was js-libp2p randomly closing untagged connections. In Lighthouse only the peer manager prunes, and it uses score and subnet utility with explicit protection. Same effect, so upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [lodestar#1683](https://github.com/ChainSafe/lodestar/pull/1683), [lodestar@b903a21d5](https://github.com/ChainSafe/lodestar/commit/b903a21d54c7)

</details>


<a id="discovery_peers-075"></a>
<details>
<summary><b>discovery_peers-075</b> Linear capability exchange loop — <i>n/a · low · cpu</i></summary>

**Idea.** Replace the O(n^2) peer capability exchange loop with a two-pass linear one.

**Impact.** n/a: Lighthouse has no O(n^2) capability exchange loop; it was Prysm specific.

**Best measured result.** pr:prysm#15384: O(n^2) to O(2n)

**Sources.** [prysm#15384](https://github.com/OffchainLabs/prysm/pull/15384)

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


<a id="discovery_peers-077"></a>
<details>
<summary><b>discovery_peers-077</b> Fine-grained locks in network globals — <i>implemented · low · S · latency</i></summary>

**Idea.** Remove the global lock around the network service and give each shared variable its own fine-grained lock in a globals struct.

**Impact.** Shared network state uses per-field locks, no global service lock.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/globals.rs:16-36`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/globals.rs#L16-L36) NetworkGlobals with one parking_lot RwLock per field
- [`beacon_node/lighthouse_network/src/types/globals.rs:89-100`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/globals.rs#L89-L100) per-field lock construction

**Skeptic check.** Verified per-field RwLocks in NetworkGlobals; this is the Lighthouse PR itself. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#840](https://github.com/sigp/lighthouse/pull/840)

</details>


<a id="discovery_peers-078"></a>
<details>
<summary><b>discovery_peers-078</b> Shorter idle connection timeout — <i>partial · low · S · memory, bandwidth</i></summary>

**Idea.** Close unused peer connections after a shorter idle timeout to free sockets and memory sooner.

**Gap in Lighthouse.** Lighthouse already uses a short 10s idle timeout; the code comment says other clients can time out, so going shorter is risky. Only a constant in service/mod.rs could change.

**Impact.** Negligible socket/memory saving.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/mod.rs:501`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L501) with_idle_connection_timeout(10s)

**Sources.** [nimbus#2262](https://github.com/status-im/nimbus-eth2/pull/2262)

</details>


<a id="discovery_peers-079"></a>
<details>
<summary><b>discovery_peers-079</b> Faster light client bootstrap peer cycling — <i>n/a · low · startup, sync</i></summary>

**Idea.** When few peers serve light client data, shorten the minimum interval between light client bootstrap queries so the client cycles through peers faster.

**Impact.** n/a: Lighthouse has no light client bootstrap peer cycling loop.

**Sources.** [nimbus#4225](https://github.com/status-im/nimbus-eth2/pull/4225)

</details>


<a id="discovery_peers-080"></a>
<details>
<summary><b>discovery_peers-080</b> Skip custody group computation for supernodes — <i>implemented · low · S · cpu</i></summary>

**Idea.** When the node custodies all groups (supernode), skip the get_custody_groups computation and use all groups directly.

**Impact.** Supernodes skip the hash loop; the computation is rare anyway.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/data/data_column_custody_group.rs:28-39`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/data/data_column_custody_group.rs#L28-L39) get_custody_groups returns 0..N when custody_group_count == number_of_custody_groups
- [`beacon_node/lighthouse_network/src/types/globals.rs:72`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/globals.rs#L72) and :111 callers go through get_custody_groups

**Skeptic check.** Verified the short-circuit is in the public get_custody_groups used by all callers. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine#290](https://github.com/grandinetech/grandine/pull/290)

</details>


<a id="discovery_peers-081"></a>
<details>
<summary><b>discovery_peers-081</b> Count pending dials against the peer limit — <i>implemented · low · S · cpu, bandwidth, latency</i></summary>

**Idea.** Count in-flight dials toward the max/target peer count and skip dialing peers the connection limits would reject, so no dials or discovery queries are wasted near the limit.

**Impact.** In-flight dials count toward limits; no excess dials or queries near max peers.

**Best measured result.** pr:nimbus#2443: fewer failed dials/discovery requests near max peers (screenshots)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:354-380`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L354-L380) peers_discovered gates on connected_or_dialing + to_dial_peers &lt; max_peers
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:1041-1050`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L1041-L1050) maintain_peer_count subtracts dialing_peers from wanted
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:458-472`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L458-L472) dial_peer uses should_dial (skips connected/dialing/banned)
- [`beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs:235-245`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs#L235-L245) outbound limit check

**Skeptic check.** Verified that dialing peers count in connected_or_dialing and in pending to_dial counts on both the dial and the discovery-request paths. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus@adcae8d41](https://github.com/status-im/nimbus-eth2/commit/adcae8d4161c), [nimbus#2443](https://github.com/status-im/nimbus-eth2/pull/2443), [lighthouse#5111](https://github.com/sigp/lighthouse/pull/5111)

</details>


<a id="discovery_peers-082"></a>
<details>
<summary><b>discovery_peers-082</b> Skip ENRs with no dialable address — <i>implemented · low · S · bandwidth, cpu, latency</i></summary>

**Idea.** Before dialing, skip ENRs with zero TCP/QUIC ports or no usable multiaddr (for example discovery-only bootnodes), so no dial slot or retry is spent on undialable records.

**Impact.** No dial slots spent on undialable ENRs.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:459-463`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L459-L463) dial_peer returns false when dialable_multiaddrs is empty
- [`common/network_utils/src/enr_ext.rs:243-260`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/network_utils/src/enr_ext.rs#L243-L260) dialable_multiaddrs_tcp omits zero ports (quic likewise)
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:832-840`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L832-L840) eth2_fork_predicate requires a dialable TCP/QUIC address
- [`beacon_node/lighthouse_network/src/service/mod.rs:600-620`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L600-L620) bootnode dial skipped when no dialable multiaddrs
- [`beacon_node/lighthouse_network/src/service/mod.rs:1339-1360`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L1339-L1360) cached-ENR subnet dials go through dial_peer

**Skeptic check.** All dial paths (discovery results, cached ENRs, trusted peers, bootnodes) filter out empty or zero-port addresses. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#7712](https://github.com/ChainSafe/lodestar/pull/7712), [lighthouse#9580](https://github.com/sigp/lighthouse/pull/9580), [caplin#22271](https://github.com/erigontech/erigon/pull/22271), [nimbus#8710](https://github.com/status-im/nimbus-eth2/pull/8710), [lighthouse#3023](https://github.com/sigp/lighthouse/pull/3023)

</details>


<a id="discovery_peers-083"></a>
<details>
<summary><b>discovery_peers-083</b> Disable discovery loop for tiny peer targets — <i>not · low · S · cpu, bandwidth</i></summary>

**Idea.** When the target peer count is tiny, disable the outbound-peer discovery loop, since on small networks every node is already connected and queries find nothing.

**Gap in Lighthouse.** Skip the outbound-only discovery branch in maintain_peer_count when target_peers is tiny (e.g. &lt;= 10).

**Impact.** Only helps devnets and tiny testnets that loop empty discovery queries; no effect on mainnet.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:1043-1069`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L1043-L1069) maintain_peer_count: no tiny-target guard, outbound-only branch always runs
- grep for '&lt;= 10' and target_peers guards in lighthouse_network/src found nothing; PR 6162 guard is gone

**Sources.** [lighthouse#6162](https://github.com/sigp/lighthouse/pull/6162)

</details>


<a id="discovery_peers-084"></a>
<details>
<summary><b>discovery_peers-084</b> Skip genesis block request in peer validation — <i>n/a · low · S · latency, bandwidth</i></summary>

**Idea.** When nothing is finalized past genesis, skip requesting the peer's genesis block during chain validation and rely on the fork digest check, saving a round trip per peer.

**Impact.** None; Lighthouse never requests the peer's genesis block, relevance is decided from the Status message and fork digest.

**Evidence (Lighthouse @ 928b61e719).**

- network/src/network_beacon_processor/rpc_methods.rs:120-165 check_peer_relevance uses Status finalized checkpoints only

**Sources.** [teku#1701](https://github.com/Consensys-Incorporated/teku/pull/1701)

</details>


<a id="discovery_peers-085"></a>
<details>
<summary><b>discovery_peers-085</b> Fall back instead of dialing unreachable peers — <i>implemented · low · S · latency</i></summary>

**Idea.** Do not stall on dialing peers that cannot be reached; fall back to requesting data from other peers or via broadcast.

**Impact.** Sync and lookups send RPCs only to connected peers; dials are asynchronous and never block data requests.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:458`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L458) dial_peer queues dials asynchronously, does not block requests
- [`beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs:336`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs#L336) on_dial_failure marks failed dials

**Skeptic check.** The prysm change is specific to an old direct-dial design; Lighthouse never dials a peer synchronously to fetch data, so the stall it fixes cannot occur. Close to n/a, upheld as implemented.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#2245](https://github.com/OffchainLabs/prysm/pull/2245)

</details>


<a id="discovery_peers-086"></a>
<details>
<summary><b>discovery_peers-086</b> Skip unused metadata fetch on peer refresh — <i>n/a · low · S · bandwidth, latency</i></summary>

**Idea.** Do not fetch peer Metadata during periodic peer refresh when the result is never used, saving a network call per peer.

**Impact.** No periodic metadata refresh exists; metadata is fetched on seq-number change and is used (subnets, custody).

**Evidence (Lighthouse @ 928b61e719).**

- lighthouse_network/src/peer_manager/mod.rs:718-745 MetaData requested only on first contact or when ping/pong seq number differs

**Sources.** [caplin#18123](https://github.com/erigontech/erigon/pull/18123)

</details>


<a id="discovery_peers-087"></a>
<details>
<summary><b>discovery_peers-087</b> Throttle random discovery lookup rate — <i>implemented · low · S · cpu, bandwidth, latency</i></summary>

**Idea.** Space discovery lookups out (sleep between random lookups, longer polling period) and connect to a bounded number of candidates per lookup, to cut queries per second and their CPU.

**Impact.** Lookup rate is bounded (serial queries, 30s heartbeat, zero at target, bounded candidates).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/discovery/mod.rs:365-374`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L365-L374) at most one FindPeers active, target capped at FIND_NODE_QUERY_CLOSEST_PEERS=16
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:64`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L64) MAX_CONCURRENT_SUBNET_QUERIES=4
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:51`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L51) HEARTBEAT_INTERVAL=30 drives maintain_peer_count
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:389-398`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L389-L398) back-to-back requery only when the last query gave useful ENRs and peers are still wanted

**Skeptic check.** Prysm's 30s polling and 15-candidate cap and Lodestar's search interval are matched by serial queries, a 30s heartbeat, a 16-result cap and no queries at target. Lighthouse has no explicit sleep between useful back-to-back queries when below target, but that is intentional fast fill and not the CPU problem the source PRs fixed.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#5050](https://github.com/OffchainLabs/prysm/pull/5050), [prysm#5488](https://github.com/OffchainLabs/prysm/pull/5488), [lodestar#3129](https://github.com/ChainSafe/lodestar/pull/3129)

</details>


<a id="discovery_peers-088"></a>
<details>
<summary><b>discovery_peers-088</b> Dial most useful discovered peers first — <i>not · low · S · latency</i></summary>

**Idea.** Sort random discovery results by usefulness (subnets covered, score) before dialing, so the dial budget goes to the best peers first.

**Gap in Lighthouse.** Collect discovery results into a Vec, sort peers with a subnet min_ttl first (and by subnet coverage) before the dial-budget loop in PeerManager::peers_discovered.

**Impact.** Dial budget when near max_peers would go to subnet-needed peers first; small, only matters when slots are scarce.

**Evidence (Lighthouse @ 928b61e719).**

- lighthouse_network/src/peer_manager/mod.rs:351 peers_discovered iterates a HashMap&lt;Enr, Option&lt;Instant&gt;&gt; in arbitrary order
- lighthouse_network/src/discovery/mod.rs:866 results collected into HashMap

**Sources.** [nimbus@3d37e0808](https://github.com/status-im/nimbus-eth2/commit/3d37e080853c)

</details>


<a id="discovery_peers-089"></a>
<details>
<summary><b>discovery_peers-089</b> Separate poll loops for channel and swarm — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** In the network service, poll the command channel and the swarm in separate loops that each stop when not ready, so a busy source cannot spin the poll loop.

**Impact.** Each source is a separate async branch; select! awaits readiness with random fairness, so no busy poll loop.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/service.rs:465-500`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L465-L500) spawn_service tokio::select! loop over network_recv, validator_subscription_recv, subnet_service and libp2p.next_event()

**Skeptic check.** The old manual poll loops were replaced by tokio::select!, which gives the same effect (no spinning, no starvation). Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@eb6ba5054](https://github.com/sigp/lighthouse/commit/eb6ba5054401)

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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [lodestar#7508](https://github.com/ChainSafe/lodestar/pull/7508)

</details>


<a id="discovery_peers-091"></a>
<details>
<summary><b>discovery_peers-091</b> Do not let subnet queries starve peer search — <i>implemented · low · S · latency</i></summary>

**Idea.** Queue and group only subnet discovery queries; always run general find-peers queries regardless of active subnet queries, so they cannot be starved.

**Impact.** FindPeers cannot be starved by subnet queries.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/discovery/mod.rs:179-180`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L179-L180) queued_queries is VecDeque&lt;SubnetQuery&gt; only
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:385-394`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L385-L394) FindPeers started immediately, not queued
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:742-748`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L742-L748) at_capacity subtracts find_peer_active
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:711-735`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L711-L735) process_queue groups subnet queries

**Skeptic check.** Verified the queue only holds subnet queries and FindPeers bypasses capacity. This is the Lighthouse PR itself; earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#2518](https://github.com/sigp/lighthouse/pull/2518)

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


<a id="discovery_peers-093"></a>
<details>
<summary><b>discovery_peers-093</b> Update local ENR only when fields change — <i>implemented · low · S · bandwidth</i></summary>

**Idea.** Update the local ENR only when a field value actually changes (and set the ip4/ip6 field matching the listen address), so the sequence number does not churn and fewer ENR updates spread in the DHT.

**Impact.** Port, socket and subnet-bitfield updates do not bump the ENR seq when the value is unchanged; this is the frequent path (listen-address events, subnet churn).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/discovery/mod.rs:417-440`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L417-L440) update_enr_tcp_port returns Ok(false) when tcp4/tcp6 already equals port
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:448-475`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L448-L475) update_enr_quic_port same for quic/quic6
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:483-491`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L483-L491) update_enr_udp_socket persists only when discv5 reports a change
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:518-524`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L518-L524) and 553-559 update_enr_bitfield returns early when the bit is already set
- ~/.cargo/registry/src/*/enr-0.14.0/src/lib.rs:585-589 Enr::insert_raw_rlp always bumps seq, so the equality guards are what prevent churn

**Skeptic check.** Confirmed the equality guards; enr::insert always increments seq, so the guards matter. update_enr_cgc, update_enr_nfd and update_eth2_enr have no guard, but their callers fire only on real changes (custody-count change, fork/BPO boundary), so there is no practical churn.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#5483](https://github.com/sigp/lighthouse/pull/5483)

</details>


<a id="discovery_peers-094"></a>
<details>
<summary><b>discovery_peers-094</b> Build peer id from ENR key without allocating — <i>not · low · S · cpu, memory</i></summary>

**Idea.** Construct the libp2p peer id from the ENR's 33-byte secp256k1 key directly into a fixed stack buffer (protobuf header plus identity multihash) rather than via an intermediate Vec. Check how the ENR-to-peer-id conversion allocates.

**Gap in Lighthouse.** Replace EnrExt::peer_id / CombinedPublicKeyExt::as_peer_id in enr_ext.rs with a fixed [u8;37] buffer (header 0x08 0x02 0x12 0x21 + 33-byte key, wrapped in identity multihash) and PeerId::from_bytes-style construction.

**Impact.** Saves 2-3 small allocations per discovered ENR; negligible CPU at discovery rates (hundreds per minute).

**Evidence (Lighthouse @ 928b61e719).**

- [`common/network_utils/src/enr_ext.rs:269`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/network_utils/src/enr_ext.rs#L269) as_peer_id: to_sec1_bytes (alloc), try_from_bytes, PeerId::from_public_key
- ~/.cargo/registry/src/*/libp2p-identity-0.3.0/src/peer_id.rs:67 from_public_key allocates via encode_protobuf (prost Vec)
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:395`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L395),878,913 enr.peer_id() on each discovered ENR

**Sources.** [silver#11](https://github.com/gattaca-com/silver/pull/11)

</details>


<a id="discovery_peers-095"></a>
<details>
<summary><b>discovery_peers-095</b> Exclude NAT&#x27;d peers from discv5 routing table — <i>implemented · low · S · latency</i></summary>

**Idea.** Do not insert peers behind NAT (unreachable) into the discv5 routing table, and tune the discv5 config, so lookups return reachable nodes and finish faster.

**Impact.** ENRs with no global, contactable address stay out of the routing table. This is the same as the PR #926 mechanism.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/config.rs:339`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L339) the default discv5 table_filter requires a global IPv4 address in the ENR
- [`beacon_node/lighthouse_network/src/config.rs:176`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L176),197,233 table_filter variants for IPv4, IPv6 and dual stack
- [`beacon_node/lighthouse_network/src/config.rs:324`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L324) tuned discv5 ConfigBuilder (ip_limit, incoming_bucket_limit, query_parallelism, timeouts)
- ~/.cargo/registry/src/*/discv5-0.12.0/src/discv5.rs:208 add_enr rejects ENRs that fail table_filter
- ~/.cargo/registry/src/*/discv5-0.12.0/src/service.rs:1263 the table_filter and contactable-address checks run before a node is inserted

**Skeptic check.** Verified the table_filter configuration in Lighthouse and the code in discv5 0.12 that applies it. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#926](https://github.com/sigp/lighthouse/pull/926)

</details>


<a id="discovery_peers-096"></a>
<details>
<summary><b>discovery_peers-096</b> Run identify only after successful Status handshake — <i>not · low · M · bandwidth, cpu</i></summary>

**Idea.** Start the peer identify exchange only after a successful STATUS handshake and deduplicate concurrent identify attempts per peer, so no streams are spent on peers that close early or are irrelevant.

**Gap in Lighthouse.** libp2p identify::Behaviour fires on connection establishment independent of STATUS. To gate it, wrap it in a custom NetworkBehaviour (or disable automatic exchange and use Behaviour::push) triggered from PeerManager after a successful Status in peer_manager/mod.rs.

**Impact.** Avoids one identify stream per peer that is disconnected before/at Status; small per-connection saving, mostly under peer churn.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/mod.rs:414-427`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L414-L427) identify::Behaviour added unconditionally, runs on every connection
- [`beacon_node/lighthouse_network/src/service/mod.rs:1927`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L1927) inject_identify_event only consumes result
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:501`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L501) identify used for client info only

**Sources.** [lodestar#8890](https://github.com/ChainSafe/lodestar/pull/8890)

</details>


<a id="discovery_peers-097"></a>
<details>
<summary><b>discovery_peers-097</b> Enable libp2p smart_dial address ranking — <i>implemented · low · S · latency</i></summary>

**Idea.** Enable the libp2p swarm smart_dial option so dialing a peer tries its addresses in ranked order instead of all or arbitrary ones. This reduces wasted dial attempts.

**Impact.** Smart dial is already turned on in the swarm config.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/mod.rs:502`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L502) swarm Config ... .with_smart_dial()

**Skeptic check.** Verified that with_smart_dial() is called on the libp2p swarm config. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#10115](https://github.com/sigp/lighthouse/pull/10115)

</details>


<a id="discovery_peers-098"></a>
<details>
<summary><b>discovery_peers-098</b> Lock-free atomically swapped local ENR — <i>not · low · S · latency, cpu</i></summary>

**Idea.** Hold the local ENR in a lock-free atomically swapped slot that discovery handlers read, with writers using compare-and-swap edits, so PING/PONG/handshake paths never take a lock or copy the record.

**Gap in Lighthouse.** Replace NetworkGlobals.local_enr RwLock&lt;Enr&gt; with ArcSwap; discv5 keeps its own copy anyway.

**Impact.** Negligible; ENR reads are rare and the lock is uncontended.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/discovery/mod.rs:437`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L437)
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:211`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L211)

**Sources.** [ethlambda#735](https://github.com/lambdaclass/ethlambda/pull/735)

</details>


<a id="discovery_peers-099"></a>
<details>
<summary><b>discovery_peers-099</b> Mark disconnected peers in discv5 routing table — <i>implemented · low · S · bandwidth</i></summary>

**Idea.** When a peer disconnects or a dial to it fails, mark it disconnected in the discv5 routing table so its slot is freed for other nodes and lookups return more connectable peers.

**Impact.** A failed dial frees the peer's DHT slot. This matches the source PR, which also marked peers only on dial failure.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/discovery/mod.rs:660`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L660) disconnect_peer calls discv5.disconnect_node and removes the cached ENR
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:1215`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L1215) on_dial_failure marks the peer disconnected for Denied (when not connected), NoAddresses, Transport, WrongPeerId and LocalPeerId errors

**Skeptic check.** The PR #2219 diff adds the mark only in notify_dial_failure. Current code does the same, and it covers more error kinds. A normal disconnect does not mark the node, in the PR or now. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#2219](https://github.com/sigp/lighthouse/pull/2219)

</details>


<a id="discovery_peers-100"></a>
<details>
<summary><b>discovery_peers-100</b> Score peers by block-serving reliability — <i>not · low · M · sync</i></summary>

**Idea.** Keep a per-peer score of how well the peer serves blocks, stored in peer metadata, so sync prefers reliable block providers.

**Gap in Lighthouse.** Add per-peer block serving success stat in PeerInfo and use it in sync peer selection (range_sync/ batch peer choice).

**Impact.** Could cut sync retries from bad peers; gain unclear.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/peerdb/peer_info.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/peerdb/peer_info.rs)

**Sources.** [lodestar@a30cf0d3c](https://github.com/ChainSafe/lodestar/commit/a30cf0d3c975)

</details>


<a id="discovery_peers-101"></a>
<details>
<summary><b>discovery_peers-101</b> Retry subnet discovery when query returns nothing — <i>implemented · low · S · bandwidth, latency</i></summary>

**Idea.** When a subnet peer discovery query returns no results, retry it, and track peers' gossipsub subnet subscriptions in the peer database, so the node reaches enough subnet peers quickly.

**Impact.** Empty subnet queries are retried up to a limit, and each peer's gossipsub subnet subscriptions are kept in the peer DB.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/discovery/mod.rs:893`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L893) an empty subnet query result requeues each subnet with add_subnet_query(retries + 1)
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:673`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L673) add_subnet_query stops at MAX_DISCOVERY_RETRY
- [`beacon_node/lighthouse_network/src/peer_manager/peerdb.rs:712`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/peerdb.rs#L712) insert_subnet / remove_subnet track gossipsub subscriptions per peer
- [`beacon_node/lighthouse_network/src/peer_manager/peerdb/peer_info.rs:442`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/peerdb/peer_info.rs#L442) PeerInfo::insert_subnet

**Skeptic check.** Verified the retry on an empty result and the per-peer subnet subscription tracking. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#2095](https://github.com/sigp/lighthouse/pull/2095)

</details>


<a id="discovery_peers-102"></a>
<details>
<summary><b>discovery_peers-102</b> Shorter ping interval to detect dead peers — <i>implemented · low · S · latency</i></summary>

**Idea.** Shorten the peer ping interval (e.g. outbound 30s to 15s, inbound 35s to 20s) so unresponsive peers are detected sooner and their slots are freed for useful peers.

**Impact.** Already done.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/config.rs:5`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/config.rs#L5)
- [`beacon_node/lighthouse_network/src/peer_manager/config.rs:8`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/config.rs#L8)

**Skeptic check.** DEFAULT_PING_INTERVAL_OUTBOUND=15 and DEFAULT_PING_INTERVAL_INBOUND=20, which are exactly the values the idea proposes. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#2132](https://github.com/sigp/lighthouse/pull/2132)

</details>


<a id="discovery_peers-103"></a>
<details>
<summary><b>discovery_peers-103</b> Sleep between retries of unavailable startup value — <i>n/a · low · cpu</i></summary>

**Idea.** When a startup loop retries reading a value that is not yet available (e.g. custody group count), sleep between attempts instead of spinning, to avoid burning CPU.

**Impact.** No spin loop exists in Lighthouse.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/service.rs:321`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L321)

**Sources.** [prysm#15735](https://github.com/OffchainLabs/prysm/pull/15735)

</details>


<a id="discovery_peers-104"></a>
<details>
<summary><b>discovery_peers-104</b> Decode ENR attnets once into set for filtering — <i>implemented · low · S · cpu</i></summary>

**Idea.** When filtering discovered peers by attestation subnet, decode the ENR attnets bitvector once into a set or test the bit directly, instead of building a list and scanning it linearly per candidate.

**Impact.** Already direct bit test.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/discovery/subnet_predicate.rs:18-33`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/subnet_predicate.rs#L18-L33)

**Skeptic check.** subnet_predicate decodes the attnets bitfield once per ENR and tests each wanted subnet with bitfield.get(i). It does not build a list or scan one. (The DataColumn arm recomputes compute_subnets_for_node for each wanted column subnet, but that is a different idea.)

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#13766](https://github.com/OffchainLabs/prysm/pull/13766)

</details>


