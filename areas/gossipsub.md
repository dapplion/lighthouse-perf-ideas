# gossipsub

55 ideas: 12 not, 8 partial, 33 implemented, 2 n/a; 12 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

Ids missing from the sequence are ideas that have not been checked against Lighthouse yet.

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [gossipsub-001](#gossipsub-001) | Gossipsub IDONTWANT for received large messages | implemented | medium |  | bandwidth |
| [gossipsub-004](#gossipsub-004) | Time-based O(1) gossip duplicate cache | implemented | low |  | cpu, latency |
| [gossipsub-006](#gossipsub-006) **★** | Coded-chunk block broadcast (RLNC or erasure coding) | not | medium | L | latency, bandwidth |
| [gossipsub-007](#gossipsub-007) | Use the fastest snappy codec for gossip and RPC | partial | low | S | cpu, latency |
| [gossipsub-008](#gossipsub-008) | Close RPC streams asynchronously | implemented | low |  | latency |
| [gossipsub-009](#gossipsub-009) **★** | Encode gossip message once and share bytes | not | medium | M | cpu, memory, latency |
| [gossipsub-011](#gossipsub-011) | Do not republish gossip the library already forwards | implemented | low |  | bandwidth, cpu |
| [gossipsub-017](#gossipsub-017) | Bitvector for permanent subnet subscriptions | not | low | S | memory |
| [gossipsub-018](#gossipsub-018) | Bound buffered gossip awaiting unknown block | implemented | medium |  | memory |
| [gossipsub-021](#gossipsub-021) | Bound gossipsub RPC decode before unmarshalling | implemented | medium |  | memory |
| [gossipsub-024](#gossipsub-024) | Upgrade QUIC library for throughput and CPU | implemented | low |  | cpu, memory, bandwidth |
| [gossipsub-025](#gossipsub-025) | Compute gossip message id once and store it | implemented | low | S | cpu, memory |
| [gossipsub-028](#gossipsub-028) | Gossip data columns as partial cell messages | implemented | high |  | bandwidth, latency |
| [gossipsub-029](#gossipsub-029) | Compact fixed-size keys in gossip seen caches | not | low | M | cpu, memory |
| [gossipsub-030](#gossipsub-030) **★** | Reject oversized gossip by snappy header before decompress | partial | medium | S | cpu, memory |
| [gossipsub-034](#gossipsub-034) | Dedupe by message id inside gossipsub | implemented | low |  | cpu, bandwidth |
| [gossipsub-035](#gossipsub-035) | Fast message id on raw bytes before decompress | not | low | M | cpu |
| [gossipsub-036](#gossipsub-036) | Fast non-cryptographic hash for gossip fast message id | not | low | S | cpu |
| [gossipsub-037](#gossipsub-037) | Decompress gossip payload once and share it | implemented | medium | S | cpu, memory |
| [gossipsub-039](#gossipsub-039) | Run libp2p networking on its own thread | partial | low | M | latency, cpu |
| [gossipsub-040](#gossipsub-040) | Node-id derived long-lived attestation subnets | implemented | low |  | bandwidth, cpu |
| [gossipsub-042](#gossipsub-042) **★** | Gate gossip subscriptions on sync state | partial | medium | S | cpu, bandwidth, memory, sync |
| [gossipsub-043](#gossipsub-043) | Keep libp2p/gossipsub dependencies on fixed, fast versions | implemented | medium | S | memory, cpu, latency, bandwidth |
| [gossipsub-047](#gossipsub-047) | Disable gossipsub flood publish | implemented | medium | S | bandwidth, latency |
| [gossipsub-051](#gossipsub-051) | Prune or disconnect peers whose send queue stays full | implemented | medium | S | memory, bandwidth, cpu |
| [gossipsub-053](#gossipsub-053) | Subscribe only to topics valid for current fork | implemented | low |  | bandwidth, cpu |
| [gossipsub-054](#gossipsub-054) | Subscribe attestation subnets only for duties | implemented | medium | S | bandwidth, cpu |
| [gossipsub-058](#gossipsub-058) | Just-in-time short-lived duty subnet subscription | implemented | medium | S | bandwidth, cpu |
| [gossipsub-064](#gossipsub-064) | Forward gossip right after validation, before processing | implemented | high |  | latency |
| [gossipsub-065](#gossipsub-065) | Non-supernodes publish reconstructed custody columns | implemented | medium | S | latency, bandwidth |
| [gossipsub-067](#gossipsub-067) | Keep column gossip during optimistic sync | n/a | medium |  | sync, bandwidth |
| [gossipsub-068](#gossipsub-068) **★** | Cheaper gossipsub peer score computation | partial | medium | M | cpu |
| [gossipsub-069](#gossipsub-069) | Snappy-compress all gossip payloads | implemented | low |  | bandwidth |
| [gossipsub-070](#gossipsub-070) | Gossipsub topic subscription allowlist filter | implemented | medium |  | memory, cpu, bandwidth |
| [gossipsub-071](#gossipsub-071) **★** | Batch publish all sidecars of a block | partial | medium | M | latency |
| [gossipsub-072](#gossipsub-072) **★** | Lower gossipsub memory per message | not | medium | M | memory |
| [gossipsub-074](#gossipsub-074) | Lazy sweep of idle rate-limiter buckets | implemented | low | S | cpu, memory |
| [gossipsub-076](#gossipsub-076) **★** | Cap incoming connections and per-peer streams | partial | medium | S | memory, cpu |
| [gossipsub-077](#gossipsub-077) | Gossipsub seen-cache TTL spans attestation propagation window | implemented | medium |  | cpu, bandwidth |
| [gossipsub-078](#gossipsub-078) | Tune gossipsub mesh degree and gossip parameters | implemented | medium |  | bandwidth, cpu, memory |
| [gossipsub-082](#gossipsub-082) | Subscribe to duty subnet only when aggregating | implemented | medium | S | bandwidth, cpu |
| [gossipsub-085](#gossipsub-085) | Avoid redundant topic re-subscription | implemented | low | S | cpu, bandwidth |
| [gossipsub-086](#gossipsub-086) | Request bitmap for missing partial-column cells | implemented | medium | S | bandwidth |
| [gossipsub-091](#gossipsub-091) **★** | Bundle attestations via gossipsub partial messages | not | medium | L | bandwidth |
| [gossipsub-092](#gossipsub-092) | Custody all columns without all attestation subnets | implemented | medium | S | bandwidth, cpu |
| [gossipsub-093](#gossipsub-093) | Subscribe only to custody/sampling column subnets | implemented | low | S | bandwidth, cpu |
| [gossipsub-101](#gossipsub-101) | Short 8-byte gossip message ids | partial | low | S | bandwidth, memory, cpu |
| [gossipsub-102](#gossipsub-102) | Disable gossipsub message signing | implemented | low | S | cpu, bandwidth |
| [gossipsub-104](#gossipsub-104) | Per-topic bounded gossip work queues | implemented | medium | S | cpu, latency |
| [gossipsub-105](#gossipsub-105) **★** | Queue admission before decompression and message-id | not | medium | M | cpu |
| [gossipsub-117](#gossipsub-117) **★** | Raise OS UDP buffer limits for QUIC | not | medium | S | bandwidth, latency |
| [gossipsub-118](#gossipsub-118) | Reset libp2p streams on error and timeout | n/a | medium | S | memory |
| [gossipsub-120](#gossipsub-120) **★** | Interleave column sidecar publish across columns | not | medium | M | latency, bandwidth |
| [gossipsub-123](#gossipsub-123) | Fastest AEAD/hash backend for noise transport | implemented | low | S | cpu |
| [gossipsub-129](#gossipsub-129) | Parse fork digest from topic without allocation | not | low | S | cpu, memory |

★ actionable. Click an id for the full record.

## Ideas

<a id="gossipsub-001"></a>
<details>
<summary><b>gossipsub-001</b> Gossipsub IDONTWANT for received large messages — <i>implemented · medium · bandwidth</i></summary>

**Idea.** On receiving a large gossip message, send IDONTWANT to mesh peers and skip forwarding it to peers that sent IDONTWANT for it. Cuts duplicate transfers of blocks, blobs and columns.

**Impact.** Already avoids duplicate large transfers.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/config.rs:24`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L24) DEFAULT_IDONTWANT_MESSAGE_SIZE_THRESHOLD=1000
- libp2p-gossipsub(sigp fork accba72)/behaviour.rs:1953 broadcast IDONTWANT on receipt
- libp2p-gossipsub(sigp fork accba72)/behaviour.rs:713 on publish
- libp2p-gossipsub(sigp fork accba72)/behaviour.rs:3013 skip peers in dont_send on forward

**Sources.** [lighthouse#5422](https://github.com/sigp/lighthouse/pull/5422), [silver#9](https://github.com/gattaca-com/silver/pull/9), [lodestar#7359](https://github.com/ChainSafe/lodestar/pull/7359), [prysm#14428](https://github.com/OffchainLabs/prysm/pull/14428), [teku#8648](https://github.com/Consensys-Incorporated/teku/pull/8648)

</details>


<a id="gossipsub-004"></a>
<details>
<summary><b>gossipsub-004</b> Time-based O(1) gossip duplicate cache — <i>implemented · low · cpu, latency</i></summary>

**Idea.** Keep the gossipsub seen-message cache as a time-based structure with O(1) insert and expiry inside the gossipsub layer, not an LRU with O(N) updates per message, so duplicate checks do not block network threads.

**Impact.** Already done; no change needed.

**Best measured result.** pr:lighthouse#1490: fixed high CPU, nodes not following head, HTTP delays; no numbers

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/time_cache.rs:44-50 TimeCache: hash map plus VecDeque ordered by expiry
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/time_cache.rs:169-190 DuplicateCache insert/contains O(1)
- [`beacon_node/lighthouse_network/src/config.rs:495`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L495) duplicate_cache_time 2 epochs

**Sources.** [lighthouse#1490](https://github.com/sigp/lighthouse/pull/1490), [lighthouse#1400](https://github.com/sigp/lighthouse/pull/1400)

</details>


<a id="gossipsub-006"></a>
<details>
<summary><b>gossipsub-006</b> Coded-chunk block broadcast (RLNC or erasure coding) — <i>not · medium · L · latency, bandwidth</i></summary>

**Idea.** Broadcast blocks as network-coded or erasure-coded chunks (RLNC, Reed-Solomon) so peers forward distinct pieces before holding the whole block and receivers reconstruct from any k chunks. Cuts propagation time versus whole-message gossip.

**Gap in Lighthouse.** No coded-chunk block gossip. The only chunked path is the partial-messages extension for data columns (cell level, from PeerDAS erasure coding of blobs), not for blocks. Would need a new gossip protocol in the libp2p fork and network-wide spec agreement.

**Impact.** Could cut block propagation latency per hop, but needs all clients to support it; gain unproven.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/mod.rs:843`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L843) Network::publish sends the whole encoded block per topic
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/behaviour.rs:3024 forward_msg sends RpcOut::Publish with the full RawMessage
- grep -i rlnc\|reed_solomon\|erasure\|fountain\|raptor over beacon_node and the gossipsub fork: no matches

**Second check.** Searched beacon_node, network and the gossipsub fork (incl. extensions/partial_messages) for any coding scheme; only PeerDAS column cells exist, which do not apply to blocks.

**Sources.** [prysm#14813](https://github.com/OffchainLabs/prysm/pull/14813), [prysm#14830](https://github.com/OffchainLabs/prysm/pull/14830), [ethlambda#466](https://github.com/lambdaclass/ethlambda/pull/466)

</details>


<a id="gossipsub-007"></a>
<details>
<summary><b>gossipsub-007</b> Use the fastest snappy codec for gossip and RPC — <i>partial · low · S · cpu, latency</i></summary>

**Idea.** Use the fastest available snappy implementation (native or optimized, with preallocated or reused buffers) for gossip and req/resp compress and decompress, chosen per message size or topic where benchmarks show it wins. Compression runs on every gossip message, so a faster codec cuts CPU on the hot path.

**Gap in Lighthouse.** Uses the pure-Rust snap crate everywhere, which is already fast, but allocates a fresh Encoder/Decoder and output Vec for every message and does not reuse buffers or pick a codec by size. Could use thread-local reusable Encoder/Decoder and preallocated output buffers in inbound_transform/outbound_transform, or a faster crate (e.g. snap-simd/lz4-style snappy bindings).

**Impact.** Small CPU saving on gossip receive path (decompress of attestations/aggregates/blocks); likely well under 1% of node CPU. Gains mostly avoiding allocations.

**Best measured result.** 10000 B compress 51.5us (snappyjs) vs 5.9us (native); 100 B uncompress 154ns snappyjs vs 235ns native (slower for tiny uncompress) (pr:lodestar#8557)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/pubsub.rs:123-124`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L123-L124) Decoder::new() and decompress_vec per gossip message
- [`beacon_node/lighthouse_network/src/types/pubsub.rs:149-150`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L149-L150) Encoder::new() and compress_vec per message
- [`beacon_node/lighthouse_network/src/rpc/codec.rs:127`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L127),187 snap FrameEncoder/FrameDecoder per RPC message
- Cargo.lock snap 1.1.2 (pure Rust, no native/SIMD codec)

**Sources.** [teku#10912](https://github.com/Consensys-Incorporated/teku/pull/10912), [teku#10861](https://github.com/Consensys-Incorporated/teku/pull/10861), [lodestar#6483](https://github.com/ChainSafe/lodestar/pull/6483), [teku#11167](https://github.com/Consensys-Incorporated/teku/pull/11167), [lodestar#8557](https://github.com/ChainSafe/lodestar/pull/8557), [lodestar#8647](https://github.com/ChainSafe/lodestar/pull/8647), [lodestar#8670](https://github.com/ChainSafe/lodestar/pull/8670)

</details>


<a id="gossipsub-008"></a>
<details>
<summary><b>gossipsub-008</b> Close RPC streams asynchronously — <i>implemented · low · latency</i></summary>

**Idea.** Close req/resp streams with close-write plus reset, without waiting for the remote EOF on each request, so per-request latency does not include the close handshake.

**Impact.** Response is delivered to the application before the close completes, so request latency does not include the close handshake.

**Best measured result.** pr:prysm#8015: maybe latency improvements; no numbers

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/handler.rs:686-690`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L686-L690) after the single/last response the substream goes to Closing state and is closed in background
- [`beacon_node/lighthouse_network/src/rpc/handler.rs:786`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L786) Closing polled without blocking the response being delivered

**Sources.** [prysm#8015](https://github.com/OffchainLabs/prysm/pull/8015)

</details>


<a id="gossipsub-009"></a>
<details>
<summary><b>gossipsub-009</b> Encode gossip message once and share bytes — <i>not · medium · M · cpu, memory, latency</i></summary>

**Idea.** SSZ-encode and snappy-compress a published or forwarded gossip message once, then share the same byte buffer by reference across the async publish path, all peers, the message cache and the transport. Avoids re-encoding or copying the message per peer or per async frame.

**Gap in Lighthouse.** Make RawMessage.data a bytes::Bytes or Arc&lt;[u8]&gt; in the fork so per-peer RpcOut::Publish and mcache share one buffer; remove data.clone() in Behaviour::publish (pass ownership, compute msg_id first); messages have a single topic so the per-topic encode is minor.

**Impact.** Removes one memcpy of each block/column per mesh peer (about 8 to 12) plus one extra copy at publish; small CPU and allocator relief at block time.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/mod.rs:846`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L846) message.encode() inside the per-topic loop, then message_data.clone() at :849
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/behaviour.rs:635 publish passes data.clone() to outbound_transform
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/behaviour.rs:3026 forward_msg clones RawMessage per peer
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/types.rs:136 RawMessage.data: Vec&lt;u8&gt;
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/types.rs:341 RpcOut::Publish owns a RawMessage (no Arc/Bytes)

**Second check.** Checked types.rs, queue.rs and mcache.rs in the fork for Bytes/Arc sharing: none; the queue only Arcs a counter. Verdict upheld.

**Sources.** [nimbus#3830](https://github.com/status-im/nimbus-eth2/pull/3830), [nimbus#6280](https://github.com/status-im/nimbus-eth2/pull/6280), [lodestar#6597](https://github.com/ChainSafe/lodestar/pull/6597), [nimbus@6d4470a8c](https://github.com/status-im/nimbus-eth2/commit/6d4470a8c8b8), [silver#247](https://github.com/gattaca-com/silver/pull/247), [silver#202](https://github.com/gattaca-com/silver/pull/202)

</details>


<a id="gossipsub-011"></a>
<details>
<summary><b>gossipsub-011</b> Do not republish gossip the library already forwards — <i>implemented · low · bandwidth, cpu</i></summary>

**Idea.** For messages received from the network (for example attestations), do not re-serialize and republish them at the application level or again from the op pool path; let gossipsub forward and dedupe them, and publish only locally created messages once. Removes duplicate gossip and serialization work.

**Impact.** No extra work to remove; Lighthouse only publishes locally created or reconstructed messages.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/service.rs:661`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L661) received messages go through report_message_validation_result (gossipsub forwards them) rather than an app-level republish
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:942-956`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L942-L956) only locally reconstructed columns are republished
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/behaviour.rs:1986 duplicates dropped by message id

**Sources.** [caplin#13314](https://github.com/erigontech/erigon/pull/13314), [teku#5129](https://github.com/Consensys-Incorporated/teku/pull/5129), [prysm#2509](https://github.com/OffchainLabs/prysm/pull/2509)

</details>


<a id="gossipsub-017"></a>
<details>
<summary><b>gossipsub-017</b> Bitvector for permanent subnet subscriptions — <i>not · low · S · memory</i></summary>

**Idea.** Store long-lived attestation subnet subscriptions as a fixed-size bitvector instead of a hash set.

**Gap in Lighthouse.** Replace the HashSet&lt;Subnet&gt; in SubnetService with a fixed-size bitvector. The set holds at most a few subnets and is read only on subscription events.

**Impact.** Negligible: at most 64 entries, touched rarely. Not worth doing for performance.

**Best measured result.** pr:lighthouse#7317: Claims better memory efficiency, no numbers

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/subnet_service/mod.rs:94`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L94) permanent_attestation_subscriptions: HashSet&lt;Subnet&gt;
- [`beacon_node/network/src/subnet_service/mod.rs:205`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L205),440 contains() lookups
- Lighthouse PR 7317 was closed unmerged

**Sources.** [lighthouse#7317](https://github.com/sigp/lighthouse/pull/7317)

</details>


<a id="gossipsub-018"></a>
<details>
<summary><b>gossipsub-018</b> Bound buffered gossip awaiting unknown block — <i>implemented · medium · memory</i></summary>

**Idea.** Cap the gossip messages buffered while waiting for an unknown block (roots buffered per slot, roots searched per slot) so memory cannot grow without limit.

**Gap in Lighthouse.** Caps are global, not per slot or per root; that bounds memory the same way, so no change needed.

**Impact.** Memory is already bounded.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:84`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L84) MAXIMUM_QUEUED_ATTESTATIONS=16384
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:87`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L87) MAXIMUM_QUEUED_DATA_COLUMNS=256
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:78`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L78) MAXIMUM_QUEUED_BLOCKS=16, line 81 envelopes=16
- [`beacon_node/network/src/sync/manager.rs:95`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L95) MAX_PENDING_UNKNOWN_ROOTS=1024

**Sources.** [lodestar#10039](https://github.com/ChainSafe/lodestar/pull/10039)

</details>


<a id="gossipsub-021"></a>
<details>
<summary><b>gossipsub-021</b> Bound gossipsub RPC decode before unmarshalling — <i>implemented · medium · memory</i></summary>

**Idea.** Reject gossipsub RPCs above a size cap and set finite decode limits on subscriptions, messages, IHAVE/IWANT/IDONTWANT ids and PX peers before decoding, so crafted control messages cannot force large allocations.

**Gap in Lighthouse.** Limits are on total size, publish count and aggregate control bytes rather than per-field id counts, which gives the same allocation bound.

**Impact.** DoS allocation bound already in the fork.

**Best measured result.** pr:caplin#24616: unbounded allocation; short burst OOM-kills

**Evidence (Lighthouse @ 928b61e719).**

- libp2p-gossipsub(sigp fork accba72)/protocol.rs:295 validate_rpc_limits parses wire format without allocating
- libp2p-gossipsub(sigp fork accba72)/protocol.rs:349 called in decode before prost decode: total size, publish count, control size caps
- libp2p-gossipsub(sigp fork accba72)/protocol.rs:376 per-topic max size check

**Sources.** [lodestar#9117](https://github.com/ChainSafe/lodestar/pull/9117), [caplin#24616](https://github.com/erigontech/erigon/pull/24616)

</details>


<a id="gossipsub-024"></a>
<details>
<summary><b>gossipsub-024</b> Upgrade QUIC library for throughput and CPU — <i>implemented · low · cpu, memory, bandwidth</i></summary>

**Idea.** Keep the QUIC transport library current to get throughput, CPU and memory improvements in the QUIC stack.

**Impact.** Dependency is already on a current quinn; Lighthouse tracks upgrades through its libp2p fork.

**Best measured result.** pr:nimbus#8836: "should improve throughput, cpu and ram usage in quic transport"

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.lock: libp2p-quic 0.14.0 (sigp fork rev accba72), quinn 0.11.12, quinn-proto 0.11.19 (recent releases)
- Cargo.toml:177 libp2p with quic feature

**Sources.** [nimbus#8836](https://github.com/status-im/nimbus-eth2/pull/8836)

</details>


<a id="gossipsub-025"></a>
<details>
<summary><b>gossipsub-025</b> Compute gossip message id once and store it — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Compute the gossip message id (sha256 of the uncompressed payload) once per message and store it on the message object, instead of recomputing it each time the pubsub layer asks or keeping it in a separate lookup map. Removes repeated hashing and map lookups.

**Gap in Lighthouse.** Minor: the id closure (config.rs:464-486 prefix()) copies the whole payload into a new Vec before hashing; feeding Sha256::update in pieces would avoid the copy.

**Impact.** Id is hashed once per message; the avoidable cost is one payload memcpy per message, tiny.

**Best measured result.** getMsgId() took 3% of CPU time (pr:lodestar#3834)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/behaviour.rs:1950 message id computed once on receive after transform, then used for duplicate_cache, mcache and validation
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/behaviour.rs:650 once on publish
- [`beacon_node/lighthouse_network/src/config.rs:490-495`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L490-L495) gossip_message_id sha256 closure

**Sources.** [teku#3251](https://github.com/Consensys-Incorporated/teku/pull/3251), [lodestar#3834](https://github.com/ChainSafe/lodestar/pull/3834), [teku#5469](https://github.com/Consensys-Incorporated/teku/pull/5469)

</details>


<a id="gossipsub-028"></a>
<details>
<summary><b>gossipsub-028</b> Gossip data columns as partial cell messages — <i>implemented · high · bandwidth, latency</i></summary>

**Idea.** Use gossipsub partial messages to disseminate data columns at cell granularity, so peers send only the cells a peer lacks (filling the rest from EL getBlobs) rather than whole column sidecars, and republish as partials complete. Cuts column gossip bandwidth.

**Impact.** Already cuts column gossip bandwidth; enabled by default via CLI.

**Best measured result.** pr:lodestar#8748: Reduces bandwidth by ~500KiB per slot (stated)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/src/cli.rs:693`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L693) --enable-partial-columns default true
- [`beacon_node/lighthouse_network/src/service/mod.rs:375`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L375) enable_partials_for_topic for column topics
- [`beacon_node/lighthouse_network/src/service/mod.rs:907`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L907) publish_partial
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:333`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L333) EL getBlobs fills partial assembler

**Sources.** [grandine#629](https://github.com/grandinetech/grandine/pull/629), [lodestar#8748](https://github.com/ChainSafe/lodestar/pull/8748), [teku#10262](https://github.com/Consensys-Incorporated/teku/pull/10262), [lighthouse#8314](https://github.com/sigp/lighthouse/pull/8314), [prysm#15869](https://github.com/OffchainLabs/prysm/pull/15869), [lighthouse#9343](https://github.com/sigp/lighthouse/pull/9343), [nimbus#8905](https://github.com/status-im/nimbus-eth2/pull/8905), [nimbus#9035](https://github.com/status-im/nimbus-eth2/pull/9035), [prysm#16505](https://github.com/OffchainLabs/prysm/pull/16505), [prysm#16733](https://github.com/OffchainLabs/prysm/pull/16733)

</details>


<a id="gossipsub-029"></a>
<details>
<summary><b>gossipsub-029</b> Compact fixed-size keys in gossip seen caches — <i>not · low · M · cpu, memory</i></summary>

**Idea.** Store seen-message and IDONTWANT cache entries as fixed-size message ids with a cheap precomputed hash and fast equality, not as per-entry heap byte wrappers, to cut lookup CPU and memory.

**Gap in Lighthouse.** Seen cache, IDONTWANT dont_send and mcache all key on Vec&lt;u8&gt; MessageId; hashing/eq go through the slice. Change sigp/rust-libp2p gossipsub MessageId to a fixed [u8;20] (or Arc-less inline array) with precomputed hash, and update DuplicateCache, dont_send, mcache, promises; Lighthouse's gossip_message_id returns it.

**Impact.** Removes a heap alloc and clones per message id across caches; small CPU win in gossipsub event loop, likely a few percent at high peer counts.

**Best measured result.** pr:teku#11549: duplicate lookup 64.6 ns -&gt; 16.0 ns (100k entries); event-thread CPU at 450-499 peers 30.9% -&gt; 24.2%

**Evidence (Lighthouse @ 928b61e719).**

- accba72/protocols/gossipsub/src/types.rs:63 MessageId(pub Vec&lt;u8&gt;) heap-allocated id
- accba72/protocols/gossipsub/src/behaviour.rs:308 duplicate_cache: DuplicateCache&lt;MessageId&gt;
- accba72/protocols/gossipsub/src/behaviour.rs:3631 dont_send LinkedHashMap&lt;MessageId,Instant&gt;
- [`beacon_node/lighthouse_network/src/config.rs:480`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L480) builds 20-byte id into Vec

**Sources.** [teku#11549](https://github.com/Consensys-Incorporated/teku/pull/11549), [nimbus#6260](https://github.com/status-im/nimbus-eth2/pull/6260)

</details>


<a id="gossipsub-030"></a>
<details>
<summary><b>gossipsub-030</b> Reject oversized gossip by snappy header before decompress — <i>partial · medium · S · cpu, memory</i></summary>

**Idea.** Read the uncompressed length from the snappy header and compare it with the topic's SSZ max size before allocating or decompressing, rejecting oversized messages immediately. Avoids large allocations and wasted decompression on invalid messages.

**Gap in Lighthouse.** Header check exists but uses the global max_payload_size, not the topic's SSZ max. Use raw_message.topic in inbound_transform to pick a per-topic SSZ max (attestation, sync message, etc.), and optionally set per-topic max_transmit_sizes in the gossipsub config.

**Impact.** Rejects crafted oversized messages on small topics without an allocation and decompress of up to max_payload_size; matters mainly under attack.

**Best measured result.** maximal message on small-type topic: three decompressed copies -&gt; one varint read (pr:caplin#25078)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/pubsub.rs:108`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L108) compressed-size check before decompress
- [`beacon_node/lighthouse_network/src/types/pubsub.rs:115`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L115) decompress_len header read, compared to max_uncompressed_len at :116 before decompress_vec at :124
- [`beacon_node/lighthouse_network/src/service/mod.rs:346`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L346) SnappyTransform::new(spec.max_payload_size, spec.max_compressed_len()) global limits
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/protocol.rs:110 max_transmit_size_for_topic exists but Lighthouse only sets the global max_transmit_size (config.rs:510)

**Second check.** Confirmed the fork supports per-topic max_transmit_sizes but Lighthouse never sets them, and no per-topic SSZ bound is applied in pubsub.rs decode before decompress.

**Sources.** [lodestar#4169](https://github.com/ChainSafe/lodestar/pull/4169), [caplin#25078](https://github.com/erigontech/erigon/pull/25078), [lodestar#10053](https://github.com/ChainSafe/lodestar/pull/10053)

</details>


<a id="gossipsub-034"></a>
<details>
<summary><b>gossipsub-034</b> Dedupe by message id inside gossipsub — <i>implemented · low · cpu, bandwidth</i></summary>

**Idea.** Use a content-hash message id and drop already-seen messages inside the gossipsub layer, before application decoding, validation or re-propagation, so duplicates from several peers are processed once.

**Evidence (Lighthouse @ 928b61e719).**

- accba72/protocols/gossipsub/src/behaviour.rs:1934-1985 transform, compute msg_id, duplicate_cache.insert before forwarding to app
- [`beacon_node/lighthouse_network/src/config.rs:526-527`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L526-L527) duplicate_cache_time + message_id_fn

**Sources.** [lodestar@c499085c5](https://github.com/ChainSafe/lodestar/commit/c499085c51dc), [lighthouse#1025](https://github.com/sigp/lighthouse/pull/1025), [lighthouse#736](https://github.com/sigp/lighthouse/pull/736), [lodestar@ca2341667](https://github.com/ChainSafe/lodestar/commit/ca2341667911)

</details>


<a id="gossipsub-035"></a>
<details>
<summary><b>gossipsub-035</b> Fast message id on raw bytes before decompress — <i>not · low · M · cpu</i></summary>

**Idea.** Compute a cheap fast message id over the raw compressed gossip bytes and dedupe on it before snappy decompression, queueing and the spec message id, caching the decompressed payload for the full id.

**Gap in Lighthouse.** Every received copy is fully snappy-decompressed and sha256'd (over topic+data) before the duplicate check; the old fast_message_id path no longer exists. Re-add fast_message_id_fn to sigp/rust-libp2p gossipsub (hash raw_message.data, cache fast-&gt;full id, skip transform on hit) and set it in gossipsub_config().

**Impact.** Duplicate gossip copies (mesh_n~8 per message, large attestation/aggregate/column volume) would skip decompress and sha256; plausibly a noticeable cut in network-thread CPU for large messages such as blocks and data columns.

**Evidence (Lighthouse @ 928b61e719).**

- accba72/protocols/gossipsub/src/behaviour.rs:1934 inbound_transform (snappy decompress) runs before message_id at :1943
- [`beacon_node/lighthouse_network/src/types/pubsub.rs:124`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L124) decompress_vec
- [`beacon_node/lighthouse_network/src/config.rs:477-485`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L477-L485) only message_id_fn set, no fast_message_id_fn; sigp libp2p has no fast id in config.rs

**Sources.** [silver#5](https://github.com/gattaca-com/silver/pull/5), [lodestar#3745](https://github.com/ChainSafe/lodestar/pull/3745), [lighthouse#1748](https://github.com/sigp/lighthouse/pull/1748), [lighthouse#1752](https://github.com/sigp/lighthouse/pull/1752)

</details>


<a id="gossipsub-036"></a>
<details>
<summary><b>gossipsub-036</b> Fast non-cryptographic hash for gossip fast message id — <i>not · low · S · cpu</i></summary>

**Idea.** Use a fast, seeded non-cryptographic hash (xxhash, highwayhash, foldhash) returning a fixed-size integer instead of sha256 for the gossipsub fast message id, internal message-id maps and tracing, since only uniqueness over a few heartbeats is needed; the seed prevents crafted collisions.

**Gap in Lighthouse.** Only the spec sha256 message id exists, computed on a freshly allocated prefix+topic+data Vec for every received copy; no fast seeded hash. Depends on gossipsub-035: add a fast id using a seeded xxh3/foldhash on raw bytes (foldhash/twox-hash already in tree), keep sha256 only for the first copy.

**Impact.** Hashing 100s of KB of data-column/block duplicates with sha256 per copy becomes ~5-10x cheaper; matters mostly on supernodes and block propagation.

**Best measured result.** Fast hash 2 KiB payload 458 ns -&gt; 83 ns; 128 KiB 30.3 -&gt; 4.3-6.2 us (pr:silver#450)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/config.rs:478-485`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L478-L485) Sha256::digest over prefixed copy of topic+data (spec id)
- accba72/protocols/gossipsub/src/behaviour.rs:1943 only full id computed on decompressed data

**Sources.** [lodestar#4639](https://github.com/ChainSafe/lodestar/pull/4639), [prysm#3703](https://github.com/OffchainLabs/prysm/pull/3703), [lodestar#4630](https://github.com/ChainSafe/lodestar/pull/4630), [lodestar#4649](https://github.com/ChainSafe/lodestar/pull/4649), [silver#450](https://github.com/gattaca-com/silver/pull/450)

</details>


<a id="gossipsub-037"></a>
<details>
<summary><b>gossipsub-037</b> Decompress gossip payload once and share it — <i>implemented · medium · S · cpu, memory</i></summary>

**Idea.** Decompress each received gossip payload once (in the gossipsub layer or lazily cached) and carry the decompressed bytes from message-id computation through to SSZ decoding, validation and handling, instead of decompressing again in each stage.

**Impact.** Already one decompression per received message; nothing left to save.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/pubsub.rs:104`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L104) SnappyTransform::inbound_transform decompresses once in the gossipsub DataTransform
- [`beacon_node/lighthouse_network/src/config.rs:492`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L492) message_id fn hashes the already-decompressed message.data
- [`beacon_node/lighthouse_network/src/types/pubsub.rs:124`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L124) decoded data handed on to SSZ decode

**Sources.** [lighthouse#2101](https://github.com/sigp/lighthouse/pull/2101), [teku#3188](https://github.com/Consensys-Incorporated/teku/pull/3188), [lodestar#3839](https://github.com/ChainSafe/lodestar/pull/3839), [lodestar#2803](https://github.com/ChainSafe/lodestar/pull/2803)

</details>


<a id="gossipsub-039"></a>
<details>
<summary><b>gossipsub-039</b> Run libp2p networking on its own thread — <i>partial · low · M · latency, cpu</i></summary>

**Idea.** Poll the libp2p swarm (gossipsub heartbeat, pings, req/resp) on its own thread, runtime or task, separate from block/state processing and message handlers, so processing spikes or slow handlers do not stall network I/O.

**Gap in Lighthouse.** Networking is its own tokio task, separate from block/state processing (beacon processor worker threads), but not a dedicated thread/runtime: swarm polling, gossipsub heartbeat, and all NetworkMessage handling share one task. Move the swarm into its own task/runtime with a channel for NetworkMessage, or split on_network_msg handling off; or give libp2p a dedicated runtime handle.

**Impact.** Avoids head-of-line stalls from slow network-service handlers on the swarm poll; benefit is latency, not much CPU, since heavy work already runs on the beacon processor.

**Best measured result.** pr:lodestar#5898: Cites reduced I/O lag from #5896 testing

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/service.rs:467-489`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L467-L489) swarm (libp2p.next_event) polled in same tokio select loop as network_recv, validator subscriptions and subnet service
- [`beacon_node/network/src/service.rs:513`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L513) executor.spawn(service_fut,"network") its own tokio task on multi-thread runtime
- [`beacon_node/lighthouse_network/src/service/mod.rs:491`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L491) libp2p executor spawns connection tasks

**Sources.** [ethlambda#187](https://github.com/lambdaclass/ethlambda/pull/187), [lodestar#5898](https://github.com/ChainSafe/lodestar/pull/5898), [lodestar#5229](https://github.com/ChainSafe/lodestar/pull/5229)

</details>


<a id="gossipsub-040"></a>
<details>
<summary><b>gossipsub-040</b> Node-id derived long-lived attestation subnets — <i>implemented · low · bandwidth, cpu</i></summary>

**Idea.** Subscribe each node to a fixed small set (two) of long-lived attestation subnets computed from its node id per spec, not one subnet per attached validator, so gossip load per node does not scale with validator count.

**Best measured result.** pr:lodestar#5822: most nodes use significantly less resource (charts)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/subnet_service/mod.rs:133-140`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L133-L140) compute_attestation_subnets(node_id) when not subscribe_all_subnets
- [`beacon_node/network/src/subnet_service/mod.rs:171`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L171) pre-populates permanent subscriptions

**Sources.** [lodestar#5822](https://github.com/ChainSafe/lodestar/pull/5822), [lodestar#5704](https://github.com/ChainSafe/lodestar/pull/5704), [prysm#13179](https://github.com/OffchainLabs/prysm/pull/13179)

</details>


<a id="gossipsub-042"></a>
<details>
<summary><b>gossipsub-042</b> Gate gossip subscriptions on sync state — <i>partial · medium · S · cpu, bandwidth, memory, sync</i></summary>

**Idea.** Do not subscribe to gossip topics (at least attestation subnets, aggregates and other non-block topics) until the node is synced or nearly synced, keep only block gossip while optimistic, unsubscribe when far behind, and re-check on every slot or sync-state event. A syncing node then does not receive, validate or relay gossip it cannot use.

**Gap in Lighthouse.** Validation cost is already avoided after regression: when the node falls back to SyncingHead/SyncingFinalized the beacon processor drops attestation, aggregate, sync-committee and light-client gossip unvalidated (so it is not relayed either) while still processing blocks/columns. What is missing is only the subscription side: Lighthouse stays subscribed to all core topics and attestation subnets after regressing, so it still receives the bytes, decodes/dedups them and holds mesh slots; no block-only subscription while syncing and no unsubscribe on regression.

**Impact.** Remaining saving is bandwidth and gossipsub decode/mesh overhead (not BLS verification) on a node that has fallen behind after first sync; small and rare.

**Best measured result.** pr:lighthouse#1613: saves computation time attempting to validate gossip messages while not synced (no numbers)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/manager.rs:775`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L775) subscribe_core_topics only on transition into Synced (nothing subscribed before)
- [`beacon_node/network/src/service.rs:721`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L721) SubscribeCoreTopics subscribes all core topics at once; no sync-driven unsubscribe
- [`beacon_node/beacon_processor/src/lib.rs:1210`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1210) gossip work with drop_during_sync is dropped unvalidated while sync_state.is_syncing()
- [`beacon_node/network/src/network_beacon_processor/mod.rs:86`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L86) unaggregated attestations drop_during_sync: true (also aggregates :134, sync signatures/contributions :270, light client updates); blocks :178 and data columns keep processing
- [`common/eth2/src/lighthouse/sync_state.rs:82`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2/src/lighthouse/sync_state.rs#L82) is_syncing true for SyncingFinalized/SyncingHead/SyncTransition

**Second check.** Found the equivalent mechanism the earlier review missed: drop_during_sync in the beacon processor (lib.rs:1210) gates non-block gossip by sync state on every event, covering the validate/relay part of the idea; subscription gating on regression is still absent.

**Sources.** [grandine#149](https://github.com/grandinetech/grandine/pull/149), [lighthouse#1613](https://github.com/sigp/lighthouse/pull/1613), [lodestar@3e48a2d07](https://github.com/ChainSafe/lodestar/commit/3e48a2d0743c), [prysm#7468](https://github.com/OffchainLabs/prysm/pull/7468), [lodestar#1712](https://github.com/ChainSafe/lodestar/pull/1712), [nimbus@d9bf6f450](https://github.com/status-im/nimbus-eth2/commit/d9bf6f450d05), [lodestar#1117](https://github.com/ChainSafe/lodestar/pull/1117), [nimbus#1532](https://github.com/status-im/nimbus-eth2/pull/1532), [nimbus#2162](https://github.com/status-im/nimbus-eth2/pull/2162), [teku#3534](https://github.com/Consensys-Incorporated/teku/pull/3534), [prysm#4767](https://github.com/OffchainLabs/prysm/pull/4767), [teku#4914](https://github.com/Consensys-Incorporated/teku/pull/4914)

</details>


<a id="gossipsub-043"></a>
<details>
<summary><b>gossipsub-043</b> Keep libp2p/gossipsub dependencies on fixed, fast versions — <i>implemented · medium · S · memory, cpu, latency, bandwidth</i></summary>

**Idea.** Track upstream libp2p and gossipsub releases (and roll back regressed ones) to pick up hot-path performance fixes (large messages, many topics, router, muxer, crypto) and memory-leak fixes such as duplicate caches holding message references or leaked TCP connections. Upstream perf and leak fixes arrive without local work.

**Impact.** Dependencies are actively tracked via sigp fork; ongoing upkeep, no gap.

**Best measured result.** recent libp2p updates resolve some memory leaks (pr:lodestar#8049)

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.toml:177 libp2p pinned to sigp/rust-libp2p fork at rev accba72b
- Cargo.lock libp2p-gossipsub 0.51.0 from that fork (recent, includes partial messages, IDONTWANT, slow peer events)

**Sources.** [prysm#14192](https://github.com/OffchainLabs/prysm/pull/14192), [lodestar#6676](https://github.com/ChainSafe/lodestar/pull/6676), [lodestar#6711](https://github.com/ChainSafe/lodestar/pull/6711), [lighthouse#1524](https://github.com/sigp/lighthouse/pull/1524), [lodestar#6156](https://github.com/ChainSafe/lodestar/pull/6156), [prysm#12132](https://github.com/OffchainLabs/prysm/pull/12132), [prysm#15677](https://github.com/OffchainLabs/prysm/pull/15677), [lodestar#6399](https://github.com/ChainSafe/lodestar/pull/6399), [teku#3260](https://github.com/Consensys-Incorporated/teku/pull/3260), [teku#5979](https://github.com/Consensys-Incorporated/teku/pull/5979), [nimbus#2510](https://github.com/status-im/nimbus-eth2/pull/2510), [lodestar#6285](https://github.com/ChainSafe/lodestar/pull/6285), [nimbus#6859](https://github.com/status-im/nimbus-eth2/pull/6859), [teku#6134](https://github.com/Consensys-Incorporated/teku/pull/6134), [lodestar#8049](https://github.com/ChainSafe/lodestar/pull/8049), [prysm#10082](https://github.com/OffchainLabs/prysm/pull/10082), [lighthouse#7828](https://github.com/sigp/lighthouse/pull/7828), [lodestar#3489](https://github.com/ChainSafe/lodestar/pull/3489), [lighthouse#1358](https://github.com/sigp/lighthouse/pull/1358)

</details>


<a id="gossipsub-047"></a>
<details>
<summary><b>gossipsub-047</b> Disable gossipsub flood publish — <i>implemented · medium · S · bandwidth, latency</i></summary>

**Idea.** Turn off gossipsub flood publishing so own blocks and messages go to mesh peers only, not to every connected peer. Cuts upload bandwidth and propagation delay at high peer counts.

**Impact.** Already publishes to mesh only.

**Best measured result.** pr:ethlambda#588: 31 to 8 recipients, roughly 4x cut on block/aggregate traffic

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/config.rs:519`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L519) .flood_publish(false)

**Sources.** [ethlambda#588](https://github.com/lambdaclass/ethlambda/pull/588), [lodestar#6755](https://github.com/ChainSafe/lodestar/pull/6755), [lodestar#6760](https://github.com/ChainSafe/lodestar/pull/6760), [teku#8661](https://github.com/Consensys-Incorporated/teku/pull/8661), [lodestar#6815](https://github.com/ChainSafe/lodestar/pull/6815), [lighthouse#4383](https://github.com/sigp/lighthouse/pull/4383)

</details>


<a id="gossipsub-051"></a>
<details>
<summary><b>gossipsub-051</b> Prune or disconnect peers whose send queue stays full — <i>implemented · medium · S · memory, bandwidth, cpu</i></summary>

**Idea.** React to gossipsub slow-peer signals (send queue stays full) by pruning the peer from the mesh via scoring or disconnecting it, because queued message copies stay in memory and repeated forwards to it are dropped anyway.

**Impact.** Slow peers are penalized through scoring and peer manager, which leads to pruning/disconnect; queued copies bounded.

**Best measured result.** pr:ethlambda#739: ~490 MB of queued gossipsub copies in a 2.8 GB steady RSS mainnet follower

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/mod.rs:1537`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L1537) Event::SlowPeer handler reports peer with HighToleranceError after &gt;10 failed priority/non-priority messages
- [`beacon_node/lighthouse_network/src/service/gossipsub_scoring_parameters.rs:98`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/gossipsub_scoring_parameters.rs#L98) slow_peer_weight -10 in peer score

**Sources.** [ethlambda#739](https://github.com/lambdaclass/ethlambda/pull/739), [ethlambda#589](https://github.com/lambdaclass/ethlambda/pull/589)

</details>


<a id="gossipsub-053"></a>
<details>
<summary><b>gossipsub-053</b> Subscribe only to topics valid for current fork — <i>implemented · low · bandwidth, cpu</i></summary>

**Idea.** Define the topic set per fork and subscribe only to topics and subnet counts the current fork uses, unsubscribing obsolete ones (for example blob topics after PeerDAS).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/topics.rs:49-105`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/topics.rs#L49-L105) core_topics_to_subscribe per fork (data column only at fulu, no blob topics)
- [`beacon_node/network/src/service.rs:493-495`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L493-L495) unsubscribe_from_old_fork_topics after fork delay

**Sources.** [lighthouse#4016](https://github.com/sigp/lighthouse/pull/4016), [lighthouse#6932](https://github.com/sigp/lighthouse/pull/6932), [nimbus#6962](https://github.com/status-im/nimbus-eth2/pull/6962)

</details>


<a id="gossipsub-054"></a>
<details>
<summary><b>gossipsub-054</b> Subscribe attestation subnets only for duties — <i>implemented · medium · S · bandwidth, cpu</i></summary>

**Idea.** Subscribe to short-lived attestation subnets only for committees of attached validators and unsubscribe after, including at startup, instead of all subnets.

**Impact.** Already duty-driven; nodes without validators only keep the spec-required long-lived subnets.

**Best measured result.** pr:prysm#5123: reduces network spam of unaggregated attestations (no numbers)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/subnet_service/mod.rs:433`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L433) subscribe_to_subnet subscribes per duty slot only
- [`beacon_node/network/src/service.rs:765`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L765) subscribe_all_subnets is opt-in
- [`beacon_node/network/src/subnet_service/mod.rs:440`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L440) permanent (long-lived) subnets are the spec-mandated ones

**Sources.** [prysm#5123](https://github.com/OffchainLabs/prysm/pull/5123), [nimbus#1462](https://github.com/status-im/nimbus-eth2/pull/1462), [nimbus#1346](https://github.com/status-im/nimbus-eth2/pull/1346), [nimbus#2231](https://github.com/status-im/nimbus-eth2/pull/2231)

</details>


<a id="gossipsub-058"></a>
<details>
<summary><b>gossipsub-058</b> Just-in-time short-lived duty subnet subscription — <i>implemented · medium · S · bandwidth, cpu</i></summary>

**Idea.** Join a short-lived attestation/aggregation subnet only a few slots before the duty slot (while searching for subnet peers earlier) and leave right after the slot, rather than at epoch granularity or with long lead time. Cuts time subscribed and subnet traffic received.

**Impact.** Already just-in-time; further shortening would gain little.

**Best measured result.** about 25% reduction in attestation subnet topic subscription in the ideal case (pr:nimbus#2240)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/subnet_service/mod.rs:51`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L51) ADVANCE_SUBSCRIBE_SLOT_FRACTION = 1 (subscribe one slot before duty)
- [`beacon_node/network/src/subnet_service/mod.rs:425`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L425) DiscoverPeers queued early for the subnet, subscription delayed
- [`beacon_node/network/src/subnet_service/mod.rs:462`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L462) unsubscribe shortly after duty slot (UNSUBSCRIBE_AFTER_AGGREGATOR_DUTY)

**Sources.** [lighthouse#3419](https://github.com/sigp/lighthouse/pull/3419), [lighthouse#3475](https://github.com/sigp/lighthouse/pull/3475), [lodestar#5810](https://github.com/ChainSafe/lodestar/pull/5810), [nimbus#2240](https://github.com/status-im/nimbus-eth2/pull/2240), [nimbus#2555](https://github.com/status-im/nimbus-eth2/pull/2555), [teku#3854](https://github.com/Consensys-Incorporated/teku/pull/3854)

</details>


<a id="gossipsub-064"></a>
<details>
<summary><b>gossipsub-064</b> Forward gossip right after validation, before processing — <i>implemented · high · latency</i></summary>

**Idea.** Forward an ACCEPTed gossip message (notably a block) to the mesh as soon as gossip validation passes, before heavy handlers such as fork choice and full block import run. Cuts per-hop propagation delay.

**Impact.** Block/column forwarded after gossip validation, before fork choice and import.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1661`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1661) propagate Accept right after gossip verification, before import
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:728`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L728) same for data columns
- [`beacon_node/lighthouse_network/src/config.rs:524`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L524) validate_messages

**Sources.** [lodestar#9990](https://github.com/ChainSafe/lodestar/pull/9990), [silver#174](https://github.com/gattaca-com/silver/pull/174)

</details>


<a id="gossipsub-065"></a>
<details>
<summary><b>gossipsub-065</b> Non-supernodes publish reconstructed custody columns — <i>implemented · medium · S · latency, bandwidth</i></summary>

**Idea.** Let full nodes publish their custody data columns built from EL getBlobs, in random order, so columns propagate sooner.

**Impact.** Already published from getBlobs-built columns in random order.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/mod.rs:1004`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L1004) fetch_engine_blobs_and_publish_full publishes via publish_data_columns_gradually
- [`beacon_node/network/src/network_beacon_processor/mod.rs:1264`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L1264) publish_data_columns_gradually shuffles columns and publishes in batches, skipping already-seen ones
- [`beacon_node/network/src/network_beacon_processor/mod.rs:1218`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L1218) reconstruction path also publishes

**Sources.** [lighthouse#7258](https://github.com/sigp/lighthouse/pull/7258)

</details>


<a id="gossipsub-067"></a>
<details>
<summary><b>gossipsub-067</b> Keep column gossip during optimistic sync — <i>n/a · medium · sync, bandwidth</i></summary>

**Idea.** Keep data column gossip subscribed during optimistic sync (driven by custody group updates), so columns arrive by gossip and are not fetched later.

**Impact.** Lighthouse gates subscriptions on its CL SyncState, not on EL optimistic import; once Synced, column topics are subscribed even if blocks are imported optimistically, so Teku's optimistic-sync gap does not exist.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/sync/manager.rs:775-784`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L775-L784) core topics subscribed when CL sync state becomes Synced
- [`beacon_node/network/src/service.rs:721`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L721) SubscribeCoreTopics handler
- [`beacon_node/lighthouse_network/src/types/topics.rs:87-91`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/topics.rs#L87-L91) sampling subnets are core topics

**Sources.** [teku#10304](https://github.com/Consensys-Incorporated/teku/pull/10304), [teku#10348](https://github.com/Consensys-Incorporated/teku/pull/10348)

</details>


<a id="gossipsub-068"></a>
<details>
<summary><b>gossipsub-068</b> Cheaper gossipsub peer score computation — <i>partial · medium · M · cpu</i></summary>

**Idea.** Make gossipsub peer score refresh cheap with many peers and topics.

**Gap in Lighthouse.** Heartbeat score caching and slot-length decay exist. Outside the heartbeat, below_threshold recomputes the full per-topic score on every message/control event, and refresh_scores walks the full peer x topic HashMap; a cached score invalidated on stat change (or flat per-topic arrays) would need a change in the sigp gossipsub fork.

**Impact.** Small swarm-task CPU saving at 100+ peers and ~70+ topics; unlikely to be visible next to block/attestation processing.

**Best measured result.** pr:teku#3812: "gossip scoring optimisations" (no numbers)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/behaviour.rs:2321-2328 heartbeat computes each connected peer's score_report once into a HashMap and reuses it for all mesh/opportunistic-graft/median decisions
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/behaviour.rs:3717-3724 refresh_scores only runs when decay_interval fires
- [`beacon_node/lighthouse_network/src/service/gossipsub_scoring_parameters.rs:72`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/gossipsub_scoring_parameters.rs#L72) decay_interval = max(1s, slot)
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/peer_score.rs:59-68 below_threshold recomputes score_report from scratch on every call (18 call sites in behaviour.rs, e.g. per received message/IHAVE/graft)
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/peer_score.rs:270 score_report walks all topics of the peer
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/peer_score.rs:429 refresh_scores walks every peer x topic

**Sources.** [teku#3812](https://github.com/Consensys-Incorporated/teku/pull/3812)

</details>


<a id="gossipsub-069"></a>
<details>
<summary><b>gossipsub-069</b> Snappy-compress all gossip payloads — <i>implemented · low · bandwidth</i></summary>

**Idea.** Publish gossip payloads only in snappy-compressed (ssz_snappy) encoding on the wire and never also uncompressed, to cut bytes sent.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/pubsub.rs:136-150`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L136-L150) outbound_transform snappy-compresses every published payload
- [`beacon_node/lighthouse_network/src/types/pubsub.rs:106-124`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L106-L124) inbound_transform decompresses

**Sources.** [lodestar#860](https://github.com/ChainSafe/lodestar/pull/860), [nimbus#1240](https://github.com/status-im/nimbus-eth2/pull/1240), [lighthouse#984](https://github.com/sigp/lighthouse/pull/984), [teku#1722](https://github.com/Consensys-Incorporated/teku/pull/1722)

</details>


<a id="gossipsub-070"></a>
<details>
<summary><b>gossipsub-070</b> Gossipsub topic subscription allowlist filter — <i>implemented · medium · memory, cpu, bandwidth</i></summary>

**Idea.** Install a gossipsub subscription/topic filter so the router tracks peer subscriptions and accepts messages only for topics valid for the current fork digest and actually needed, before keeping state or validating them. Saves memory, bandwidth and validation.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/utils.rs:270-305`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/utils.rs#L270-L305) create_whitelist_filter of all valid topics per possible fork digest
- [`beacon_node/lighthouse_network/src/service/mod.rs:129-131`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L129-L131),332 MaxCountSubscriptionFilter&lt;WhitelistSubscriptionFilter&gt;

**Sources.** [teku@e66336f14](https://github.com/Consensys-Incorporated/teku/commit/e66336f14e83), [teku#8086](https://github.com/Consensys-Incorporated/teku/pull/8086), [lighthouse#1767](https://github.com/sigp/lighthouse/pull/1767), [prysm#7496](https://github.com/OffchainLabs/prysm/pull/7496), [teku#8112](https://github.com/Consensys-Incorporated/teku/pull/8112)

</details>


<a id="gossipsub-071"></a>
<details>
<summary><b>gossipsub-071</b> Batch publish all sidecars of a block — <i>partial · medium · M · latency</i></summary>

**Idea.** Publish all blob or column sidecars of a block in one gossipsub batch-publish call, so all sidecars go out together and propagate sooner.

**Gap in Lighthouse.** All sidecars of a block already go out together in one Publish batch, and because gossipsub publish only enqueues onto independent per-peer queues the go-pubsub 'first message reaches all peers before the second starts' problem is much weaker. What is missing is go's BatchPublish RoundRobin ordering (one copy of each column out before second copies); that would need a batch publish API in the gossipsub fork.

**Impact.** Proposer/supernode only; marginal gain in time-to-first-copy per column on bandwidth-limited uplinks.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/publish_blocks.rs:493-558`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L493-L558) proposer path collects all of a block's column sidecars and sends them in one NetworkMessage::Publish
- [`beacon_node/lighthouse_network/src/service/mod.rs:843-850`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L843-L850) Network::publish enqueues every message of that batch in one swarm call
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/behaviour.rs:624-735 publish only pushes onto per-peer queues (send_message), which drain concurrently per connection
- [`beacon_node/network/src/network_beacon_processor/mod.rs:1264-1330`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L1264-L1330) reconstruction path deliberately publishes shuffled batches with sleeps

**Sources.** [prysm#15052](https://github.com/OffchainLabs/prysm/pull/15052)

</details>


<a id="gossipsub-072"></a>
<details>
<summary><b>gossipsub-072</b> Lower gossipsub memory per message — <i>not · medium · M · memory</i></summary>

**Idea.** Use a gossipsub implementation that stores far less memory per message and avoids copies when assigning messages.

**Gap in Lighthouse.** Payloads are Vec&lt;u8&gt; and copied for the transform, the mcache and once per recipient peer queue. Switch RawMessage.data to Bytes/Arc&lt;[u8]&gt; in the gossipsub fork so mcache, per-peer queues and forwarding share one buffer.

**Impact.** Lower peak memory and memcpy for large blob/column messages (payload x mesh degree held in queues + mcache); Nimbus measured ~1/3 gossip memory, Lighthouse baseline unknown.

**Best measured result.** pr:nimbus#2172: reduces libp2p gossip memory usage to ~1/3

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/types.rs:136 RawMessage.data: Vec&lt;u8&gt;
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/types.rs:337-345 RpcOut::Publish owns a RawMessage by value
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/behaviour.rs:704 mcache.put(raw_message.clone())
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/behaviour.rs:724-729 raw_message.clone() per recipient peer (full payload copy each)
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/behaviour.rs:634-636 data.clone() for outbound_transform
- [`beacon_node/lighthouse_network/src/service/mod.rs:850`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L850) message_data.clone() per publish

**Sources.** [nimbus#2172](https://github.com/status-im/nimbus-eth2/pull/2172)

</details>


<a id="gossipsub-074"></a>
<details>
<summary><b>gossipsub-074</b> Lazy sweep of idle rate-limiter buckets — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Sweep idle per-peer rate-limiter buckets lazily in the acquire path instead of one sleeping cleanup task per limiter.

**Impact.** Nothing; there are already no per-limiter cleanup tasks. Pruning is one periodic timer (not in the acquire path, but same effect).

**Best measured result.** pr:caplin#25039: cleanup goroutines 13 -&gt; 0

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/rate_limiter.rs:93`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/rate_limiter.rs#L93) single prune_interval for the whole limiter
- rate_limiter.rs:275-280 one 30s interval, no per-bucket/per-limiter sleeping task

**Sources.** [caplin#25039](https://github.com/erigontech/erigon/pull/25039)

</details>


<a id="gossipsub-076"></a>
<details>
<summary><b>gossipsub-076</b> Cap incoming connections and per-peer streams — <i>partial · medium · S · memory, cpu</i></summary>

**Idea.** Bound incoming connection attempts and set explicit inbound/outbound stream limits per peer in the libp2p transport/connection limits, so a peer flood cannot grow memory and CPU without bound.

**Gap in Lighthouse.** Per-peer streams are bounded at the application layer (RPC 32 inbound substreams, 2 active per protocol) and by implicit yamux/swarm defaults, but yamux is left at 512 streams / 1 GiB receive window and there is no cap on total pending incoming connections (only per source). Set explicit yamux max streams/receive window in service/utils.rs and a with_max_pending_incoming limit.

**Impact.** DoS hardening only; no change at normal load.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/mod.rs:441-459`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L441-L459) ConnectionLimits: pending incoming per source 2, pending outgoing 16, established in/out/total, 1 per peer
- [`beacon_node/lighthouse_network/src/rpc/handler.rs:41`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L41),994 MAX_INBOUND_SUBSTREAMS = 32 per connection for RPC
- [`beacon_node/lighthouse_network/src/rpc/inbound_limiter.rs:126`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/inbound_limiter.rs#L126) max 2 concurrent inbound requests per protocol per peer
- [`beacon_node/lighthouse_network/src/rpc/self_limiter.rs:134`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/self_limiter.rs#L134) outbound MAX_CONCURRENT_REQUESTS per protocol
- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/yamux-0.14.1/src/lib.rs:89-90 implicit yamux defaults: 512 streams, 1 GiB connection receive window
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/swarm/src/connection/pool.rs:1020 implicit swarm cap of 128 negotiating inbound streams per connection
- [`beacon_node/lighthouse_network/src/service/utils.rs:43`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/utils.rs#L43) yamux::Config::default()

**Sources.** [lighthouse#1413](https://github.com/sigp/lighthouse/pull/1413), [caplin#11756](https://github.com/erigontech/erigon/pull/11756)

</details>


<a id="gossipsub-077"></a>
<details>
<summary><b>gossipsub-077</b> Gossipsub seen-cache TTL spans attestation propagation window — <i>implemented · medium · cpu, bandwidth</i></summary>

**Idea.** Configure the gossipsub duplicate/seen-message cache duration to cover the whole period a message can still propagate (up to two epochs for attestations), so late duplicates are dropped at the network layer instead of being re-validated and re-forwarded.

**Best measured result.** cache 2.1s to 8.4s; max RPC messages 10 to 500 (pr:lighthouse#2391)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/config.rs:507`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L507),526 duplicate_cache_time = 2 epochs

**Sources.** [lighthouse#2542](https://github.com/sigp/lighthouse/pull/2542), [teku#3257](https://github.com/Consensys-Incorporated/teku/pull/3257), [nimbus#6098](https://github.com/status-im/nimbus-eth2/pull/6098), [prysm#14030](https://github.com/OffchainLabs/prysm/pull/14030), [lighthouse#2391](https://github.com/sigp/lighthouse/pull/2391)

</details>


<a id="gossipsub-078"></a>
<details>
<summary><b>gossipsub-078</b> Tune gossipsub mesh degree and gossip parameters — <i>implemented · medium · bandwidth, cpu, memory</i></summary>

**Idea.** Set gossipsub D/D_low/D_high/D_lazy, gossip factor and history length in the network config to values tuned for Ethereum peer counts rather than library defaults, so fewer duplicate messages, IHAVEs and cached messages are handled.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/config.rs:391-451`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L391-L451) NetworkLoad presets for mesh_n, mesh_n_low/high, gossip_lazy, history_gossip
- [`beacon_node/lighthouse_network/src/config.rs:509-526`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L509-L526) history_length(12), heartbeat, flood_publish false

**Sources.** [nimbus#2169](https://github.com/status-im/nimbus-eth2/pull/2169), [lodestar#5427](https://github.com/ChainSafe/lodestar/pull/5427), [lodestar#5865](https://github.com/ChainSafe/lodestar/pull/5865), [teku#7419](https://github.com/Consensys-Incorporated/teku/pull/7419), [lighthouse#2608](https://github.com/sigp/lighthouse/pull/2608)

</details>


<a id="gossipsub-082"></a>
<details>
<summary><b>gossipsub-082</b> Subscribe to duty subnet only when aggregating — <i>implemented · medium · S · bandwidth, cpu</i></summary>

**Idea.** For attestation duties, subscribe to the subnet only if the validator is an aggregator for that slot; non-aggregators publish via gossipsub fanout without subscribing, avoiding subnet decode/verify/relay work.

**Impact.** Already avoids subnet subscription for non-aggregators; publishing goes via fanout.

**Best measured result.** 64 validators: 55 subnets subscribed vs ~4.9 aggregator subnets (estimate) (pr:caplin#25008)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/subnet_service/mod.rs:270`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L270) subscribe_to_subnet only if subscription.is_aggregator
- [`beacon_node/network/src/subnet_service/mod.rs:107-127`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L107-L127) subscribe_all_subnets is opt-in only

**Sources.** [caplin#25008](https://github.com/erigontech/erigon/pull/25008), [nimbus#2254](https://github.com/status-im/nimbus-eth2/pull/2254), [ethlambda#160](https://github.com/lambdaclass/ethlambda/pull/160), [ethlambda#265](https://github.com/lambdaclass/ethlambda/pull/265)

</details>


<a id="gossipsub-085"></a>
<details>
<summary><b>gossipsub-085</b> Avoid redundant topic re-subscription — <i>implemented · low · S · cpu, bandwidth</i></summary>

**Idea.** Skip subscribe/unsubscribe calls for topics already subscribed (core topics, subscribe-all subnets, data column topics, fixed subnet sets) and only change subscriptions when the required set changes, instead of re-issuing them every slot or epoch.

**Impact.** Nothing; subscriptions are event-driven and libp2p short-circuits duplicates.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/service.rs:756`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L756) subscribe only on fork/startup events
- network/src/service.rs:862 subnet subscribe driven by SubnetService messages only on change
- gossipsub behaviour.rs:563 subscribe() returns Ok(false) if topic already in mesh

**Sources.** [lodestar#4829](https://github.com/ChainSafe/lodestar/pull/4829), [lighthouse#4271](https://github.com/sigp/lighthouse/pull/4271), [nimbus#8688](https://github.com/status-im/nimbus-eth2/pull/8688), [prysm#15895](https://github.com/OffchainLabs/prysm/pull/15895)

</details>


<a id="gossipsub-086"></a>
<details>
<summary><b>gossipsub-086</b> Request bitmap for missing partial-column cells — <i>implemented · medium · S · bandwidth</i></summary>

**Idea.** Include a request bitmap in partial-column metadata so a peer advertises exactly which cells it still needs, letting senders transmit only requested cells; publish an empty column plus request when the EL has no blobs.

**Impact.** Done by PR 9361 (merged); empty column plus request-all is published when EL returns no blobs.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/partial.rs:36-61`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/partial.rs#L36-L61) requests bitmap in PartialColumn metadata
- [`beacon_node/lighthouse_network/src/types/partial.rs:224-232`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/partial.rs#L224-L232) sender transmits only requests minus available
- [`beacon_node/lighthouse_network/src/types/partial.rs:288`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/partial.rs#L288) PartialMessage ctor takes explicit requests
- Cargo.toml:177 libp2p with gossipsub-partial-messages

**Sources.** [lighthouse#9361](https://github.com/sigp/lighthouse/pull/9361), [prysm#16334](https://github.com/OffchainLabs/prysm/pull/16334), [prysm#16335](https://github.com/OffchainLabs/prysm/pull/16335)

</details>


<a id="gossipsub-091"></a>
<details>
<summary><b>gossipsub-091</b> Bundle attestations via gossipsub partial messages — <i>not · medium · L · bandwidth</i></summary>

**Idea.** Send attestations as gossipsub partial messages so peers exchange only missing attestation parts, reducing attestation gossip bandwidth.

**Gap in Lighthouse.** Add an attestation Partial type (aggregation-bit bitfield as metadata, grouped by AttestationData root) next to the column types in types/partial.rs, return true for Attestation/Aggregate in use_partial_messages, and route the merged parts into attestation verification in network_beacon_processor/gossip_methods.rs. This needs a cross-client spec agreement first.

**Impact.** Could cut attestation/aggregate gossip bandwidth, mostly on all-subnet nodes. Only works if other clients adopt it. Size unknown.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/topics.rs:209-214`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/topics.rs#L209-L214) use_partial_messages is true only for GossipKind::DataColumnSidecar; all other kinds, attestations included, return false
- [`beacon_node/lighthouse_network/src/service/mod.rs:372-375`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L372-L375) enable_partials_for_topic is called only for topics where use_partial_messages is true
- [`beacon_node/lighthouse_network/src/types/partial.rs:25`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/partial.rs#L25),167 the only Partial impls are OutgoingPartialColumnFulu/Gloas

**Second check.** Checked the partial-messages wiring: the gossipsub partial-messages feature is generic, but Lighthouse gates it on GossipKind and turns it on only for data columns. There is no attestation Partial impl anywhere.

**Sources.** [prysm#17210](https://github.com/OffchainLabs/prysm/pull/17210)

</details>


<a id="gossipsub-092"></a>
<details>
<summary><b>gossipsub-092</b> Custody all columns without all attestation subnets — <i>implemented · medium · S · bandwidth, cpu</i></summary>

**Idea.** Provide a separate option for supernodes to subscribe to all data column subnets without also subscribing to all attestation and sync-committee subnets, avoiding unneeded subnet gossip load.

**Impact.** Supernodes already avoid all attestation and sync-committee subnet gossip unless asked.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/src/config.rs:1198`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/config.rs#L1198) subscribe_all_subnets set only by --subscribe-all-subnets
- [`beacon_node/src/config.rs:129-134`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/config.rs#L129-L134) --supernode only sets node_custody_type
- [`beacon_node/lighthouse_network/src/types/topics.rs:62-73`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/topics.rs#L62-L73) attestation/sync subnets gated on subscribe_all_subnets
- [`beacon_node/lighthouse_network/src/types/topics.rs:93`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/topics.rs#L93) data column subnets from sampling_subnets

**Sources.** [prysm#15197](https://github.com/OffchainLabs/prysm/pull/15197), [nimbus#6764](https://github.com/status-im/nimbus-eth2/pull/6764)

</details>


<a id="gossipsub-093"></a>
<details>
<summary><b>gossipsub-093</b> Subscribe only to custody/sampling column subnets — <i>implemented · low · S · bandwidth, cpu</i></summary>

**Idea.** Subscribe only to the data column subnets the node custodies or samples rather than all column subnets, so it does not receive and validate columns it does not need (about 8 instead of 128 per slot).

**Impact.** Nothing; only sampling/custody column subnets are subscribed.

**Best measured result.** 128 logs per slot vs 8 needed (pr:lodestar#8181)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/topics.rs:87-90`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/topics.rs#L87-L90) subscribes only to opts.sampling_subnets
- lighthouse_network/src/service/mod.rs:786-793 subscribe_new_data_column_subnets uses sampling_subnets()

**Sources.** [lodestar#7607](https://github.com/ChainSafe/lodestar/pull/7607), [lodestar#7860](https://github.com/ChainSafe/lodestar/pull/7860), [lodestar#8181](https://github.com/ChainSafe/lodestar/pull/8181)

</details>


<a id="gossipsub-101"></a>
<details>
<summary><b>gossipsub-101</b> Short 8-byte gossip message ids — <i>partial · low · S · bandwidth, memory, cpu</i></summary>

**Idea.** Derive the gossip message id from a truncated hash (first 8 bytes, no base64 encoding or padding), shrinking IHAVE/IWANT control messages and id caches.

**Gap in Lighthouse.** Id is already raw bytes with no base64, but 20 bytes not 8. The consensus spec defines the id as the first 20 bytes, so shortening to 8 would break interop with other clients.

**Impact.** Control message savings from 20-&gt;8 byte ids are tiny and not allowed by spec; effectively done.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/config.rs:495-501`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L495-L501) id = first 20 bytes of sha256, raw bytes via MessageId::from(&amp;[..20])

**Sources.** [prysm#7304](https://github.com/OffchainLabs/prysm/pull/7304), [lighthouse#1083](https://github.com/sigp/lighthouse/pull/1083), [lighthouse#1607](https://github.com/sigp/lighthouse/pull/1607)

</details>


<a id="gossipsub-102"></a>
<details>
<summary><b>gossipsub-102</b> Disable gossipsub message signing — <i>implemented · low · S · cpu, bandwidth</i></summary>

**Idea.** Use anonymous/strict-no-sign gossipsub mode: do not sign published messages or verify libp2p signatures, since Ethereum messages carry their own signatures. Saves a signature and bytes per message.

**Impact.** Nothing; no libp2p signing or verification of gossip messages.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/config.rs:525`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L525) ValidationMode::Anonymous
- lighthouse_network/src/service/mod.rs:348 MessageAuthenticity::Anonymous

**Sources.** [nimbus@e470bbb52](https://github.com/status-im/nimbus-eth2/commit/e470bbb52e97), [prysm#2339](https://github.com/OffchainLabs/prysm/pull/2339), [prysm#7093](https://github.com/OffchainLabs/prysm/pull/7093)

</details>


<a id="gossipsub-104"></a>
<details>
<summary><b>gossipsub-104</b> Per-topic bounded gossip work queues — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Give each gossip message kind its own bounded queue with tuned size in the beacon processor, so a flood on one topic drops its own work instead of starving others.

**Impact.** Per-kind bounded queues already exist, so floods drop their own work.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:1292-1320`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1292-L1320) each Work kind pushes to its own queue (attestation_queue, aggregate_queue, gossip_data_column_queue, ...)
- [`beacon_node/beacon_processor/src/lib.rs:758-765`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L758-L765) BeaconProcessorQueueLengths sizes each WorkQueue

**Sources.** [lodestar#2277](https://github.com/ChainSafe/lodestar/pull/2277)

</details>


<a id="gossipsub-105"></a>
<details>
<summary><b>gossipsub-105</b> Queue admission before decompression and message-id — <i>not · medium · M · cpu</i></summary>

**Idea.** Check per-topic queue capacity before decompressing a message and computing its id, so messages that will be dropped for a full queue are never decompressed.

**Gap in Lighthouse.** Expose per-topic queue-full flags from BeaconProcessor (atomics) to the gossipsub transform/behaviour, and skip decompression and message-id for topics whose queue is full. Ignore those messages without a score penalty. A cheaper partial step is a raw-bytes fast-id dedup before the transform.

**Impact.** Under attestation floods, saves snappy decompression and sha256 on messages that are dropped anyway. Small effect on a healthy node.

**Best measured result.** "4x number of messages" attestations processed; stable peer count with subscribeAllSubnets (pr:lodestar#3554)

**Evidence (Lighthouse @ 928b61e719).**

- accba72/protocols/gossipsub/src/behaviour.rs:1922-1950 handle_received_message runs inbound_transform (snappy decompress) and then config.message_id on every message, before the duplicate-cache check and before anything is handed to the application
- [`beacon_node/lighthouse_network/src/types/pubsub.rs:106-129`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L106-L129) SnappyTransform::inbound_transform only checks size limits before decompress_vec; it does not look at topic or queue state
- [`beacon_node/lighthouse_network/src/config.rs:527`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L527) message_id_fn is the spec sha256 over the decompressed data; there is no fast_message_id on raw bytes

**Second check.** Read the sigp rust-libp2p gossipsub receive path. The transform and message-id run unconditionally before dedup. There is no fast-message-id or backpressure hook, and the transform is topic- and queue-blind.

**Sources.** [lodestar#3554](https://github.com/ChainSafe/lodestar/pull/3554)

</details>


<a id="gossipsub-117"></a>
<details>
<summary><b>gossipsub-117</b> Raise OS UDP buffer limits for QUIC — <i>not · medium · S · bandwidth, latency</i></summary>

**Idea.** Ensure OS UDP receive/send buffer maximums allow the ~7 MiB buffers QUIC requests (default cap ~208 KiB), avoiding drops and throughput limits.

**Gap in Lighthouse.** At startup, read net.core.rmem_max/wmem_max and warn when they are below about 7 MiB, and/or request larger buffers on the QUIC UDP socket (patch libp2p-quic create_socket, or a config option). Document the sysctl in the book.

**Impact.** Avoids UDP drops and throughput caps on QUIC links on stock Linux. The effect depends on how much traffic uses QUIC (it is on by default, --disable-quic turns it off).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/utils.rs:72-74`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/utils.rs#L72-L74) QUIC uses libp2p::quic::Config::new defaults with no socket tuning
- accba72/transports/quic/src/transport.rs:183-195 create_socket builds the UDP socket with socket2 and only sets only_v6 and bind; no SO_RCVBUF/SO_SNDBUF
- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/quinn-udp-0.5.16/src/fallback.rs:91-110 set_recv/send_buffer_size exist but have no caller in the dependency path
- repo-wide grep for rmem/wmem/SO_RCVBUF/recv_buffer_size in .rs/.md/.toml: no hits

**Second check.** Beyond the earlier review, I read libp2p-quic create_socket and its quinn TransportConfig setup. Neither sets socket buffer sizes, and the book has no sysctl guidance.

**Sources.** [ethlambda#296](https://github.com/lambdaclass/ethlambda/pull/296)

</details>


<a id="gossipsub-118"></a>
<details>
<summary><b>gossipsub-118</b> Reset libp2p streams on error and timeout — <i>n/a · medium · S · memory</i></summary>

**Idea.** On error and timeout paths reset streams rather than just closing them, so the muxer frees dead streams and the heap does not grow on long-running nodes.

**Impact.** rust-libp2p drops the substream object on error/timeout, which frees it in the muxer; Go-style Close vs Reset distinction does not exist here.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/handler.rs:542`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L542) substreams are owned by the handler and dropped on error or timeout
- [`beacon_node/lighthouse_network/src/service/utils.rs:44`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/utils.rs#L44) yamux default config

**Sources.** [prysm#6066](https://github.com/OffchainLabs/prysm/pull/6066)

</details>


<a id="gossipsub-120"></a>
<details>
<summary><b>gossipsub-120</b> Interleave column sidecar publish across columns — <i>not · medium · M · latency, bandwidth</i></summary>

**Idea.** When publishing many data column sidecars, order writes round robin across columns rather than all peers per column, so under limited upload bandwidth every column gets an early copy out.

**Gap in Lighthouse.** No global send-order scheduling: the proposer/builder publishes columns 0..N sequentially and every peer meshed on several columns (supernode peers) gets the low-index columns first, so under an upload limit the high-index columns get their first copy late. Fix: a batch publish in the gossipsub fork that enqueues the first mesh peer for every column, then the second, etc. (or at minimum shuffle column order in publish_column_sidecars so no column is systematically last).

**Impact.** Faster first-copy dissemination of all columns for bandwidth-limited proposers/supernodes; Prysm reports ~20-30% better dissemination at 50 Mbps publisher limit.

**Best measured result.** In early simulations with 50mbps publisher limits, improved dissemination by ~20-30% (pr:prysm#16130)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/publish_blocks.rs:500-555`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L500-L555) proposer path collects columns in index order (shuffle at :505 only under malicious_withhold_count) and publishes them as one Vec
- [`beacon_node/lighthouse_network/src/service/mod.rs:844-850`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L844-L850) calls gossipsub.publish once per message, in order
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/behaviour.rs:624 publish() is single-message; no batch/round-robin publish API in the sigp fork (grep batch\|round_robin finds nothing)
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/queue.rs:77-80 per-peer FIFO non_priority queue; a peer meshed on many column topics receives them in index order
- [`beacon_node/network/src/network_beacon_processor/mod.rs:1264-1320`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L1264-L1320) publish_data_columns_gradually shuffles and batches, but only for reconstructed columns and to avoid sending, not to interleave copies

**Second check.** Beyond the earlier review, searched the sigp rust-libp2p fork (accba72) for batch/round-robin/scheduler publish and checked the reconstruction-path gradual publisher (shuffled randomized batches); the latter is a different mechanism and does not interleave per-peer sends, so the verdict stands.

**Sources.** [prysm#16130](https://github.com/OffchainLabs/prysm/pull/16130), [prysm#16183](https://github.com/OffchainLabs/prysm/pull/16183)

</details>


<a id="gossipsub-123"></a>
<details>
<summary><b>gossipsub-123</b> Fastest AEAD/hash backend for noise transport — <i>implemented · low · S · cpu</i></summary>

**Idea.** Use the fastest available chacha20poly1305 and sha256 implementations for the noise transport (chosen by payload size where needed) and reuse the ciphertext buffer, since noise encryption runs on every byte sent.

**Impact.** Nothing; noise already uses ring's fast AEAD and hash. Buffer reuse inside libp2p-noise not checked.

**Best measured result.** chacha20poly1305Decrypt was ~10% of CPU, now 3.4% (pr:lodestar#4787)

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.lock:9481 snow 0.10.0 used by libp2p-noise
- rust-libp2p transports/noise/Cargo.toml:28 snow with ring-resolver on non-wasm targets (ring chacha20poly1305/sha256, asm optimised)

**Sources.** [lodestar#5900](https://github.com/ChainSafe/lodestar/pull/5900), [lodestar#4787](https://github.com/ChainSafe/lodestar/pull/4787)

</details>


<a id="gossipsub-129"></a>
<details>
<summary><b>gossipsub-129</b> Parse fork digest from topic without allocation — <i>not · low · S · cpu, memory</i></summary>

**Idea.** Extract the fork digest from the gossip topic string by slicing in place rather than splitting into new strings on every message.

**Gap in Lighthouse.** Make GossipTopic::decode iterate split('/') without collecting and decode the 8 hex chars into [u8;4] with a manual or hex::decode_to_slice call; it is used in PubsubMessage::decode and subnet_from_topic_hash.

**Impact.** Saves a few allocations per received gossip message; negligible CPU on a mainnet node (well under 0.5%).

**Best measured result.** 343.8 ns/op, 192 B/op, 4 allocs -&gt; 24.45 ns/op, 0 B/op, 0 allocs; function was 6.74% of all allocations (pr:prysm#10055)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/topics.rs:265-280`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/topics.rs#L265-L280) GossipTopic::decode does topic.split('/').collect::&lt;Vec&lt;_&gt;&gt;() and hex::decode (Vec) per call
- lighthouse_network/src/types/pubsub.rs:200 decode called per incoming message
- topics.rs:395 decode again for subnet_id

**Sources.** [prysm#10055](https://github.com/OffchainLabs/prysm/pull/10055)

</details>


